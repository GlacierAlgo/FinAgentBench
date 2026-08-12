"""Live-Web shadow runs whose predictions are sealed before outcomes exist."""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
import tempfile
import time
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

from finagentbench.case import CaseValidationError
from finagentbench.walkforward import (
    WalkForwardScenario,
    validate_realized_outcome,
)

ARTIFACT_TYPE = "finagentbench_live_shadow_seal"
RESOLUTION_TYPE = "finagentbench_live_shadow_resolution"
LABEL_TYPE = "finagentbench_live_shadow_label"
CANONICALIZATION = "json-sort-keys-utf8-v1"


def load_live_shadow_scenario(
    path: Path,
) -> tuple[dict[str, Any], WalkForwardScenario]:
    """Load one outcome-free live-shadow scenario source file."""
    payload = _read_object(path)
    scenario = WalkForwardScenario.from_dict(payload, source=str(path))
    if scenario.mode != "live_shadow":
        raise CaseValidationError(f"{path}: scenario mode must be live_shadow")
    if scenario.search_policy.latest_published_at != scenario.as_of:
        raise CaseValidationError(
            f"{path}: live-shadow search cutoff must equal as_of"
        )
    return payload, scenario


def run_live_shadow_codex_matrix(
    scenario_source: dict[str, Any],
    scenario: WalkForwardScenario,
    *,
    models: tuple[str, ...],
    reasoning_effort: str,
    workers: int,
    timeout_seconds: int,
    progress: Callable[[dict[str, Any]], None] | None = None,
    now: datetime | None = None,
) -> dict[str, Any]:
    """Run isolated Codex sessions with native real-Web search, then seal them."""
    if not models:
        raise CaseValidationError("live-shadow run requires at least one model")
    current = now or datetime.now(UTC)
    market_today = current.astimezone(_scenario_timezone(scenario)).date()
    if scenario.as_of != market_today:
        raise CaseValidationError(
            "live-shadow real-Web runs must be executed on the scenario as_of date"
        )

    started_at = datetime.now(UTC)
    codex_version = _command_output(["codex", "--version"])
    results = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(
                _run_case,
                scenario,
                model=model,
                reasoning_effort=reasoning_effort,
                timeout_seconds=timeout_seconds,
            ): model
            for model in models
        }
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            if progress is not None:
                progress(result)
    results.sort(key=lambda item: item["model"])
    completed_at = datetime.now(UTC)
    agent_payload = scenario.agent_payload()
    record = {
        "schema_version": 1,
        "artifact_type": ARTIFACT_TYPE,
        "sealed_at": completed_at.isoformat(),
        "scenario_source": scenario_source,
        "scenario_sha256": _digest(scenario_source),
        "agent_payload": agent_payload,
        "agent_payload_sha256": _digest(agent_payload),
        "harness": {
            "name": "codex-cli-native-live-web",
            "version": codex_version,
            "sandbox": "read-only",
            "web_search": "native Responses web_search",
            "session_persistence": False,
            "outcome_visible_to_agent": False,
        },
        "matrix": {
            "models": list(models),
            "reasoning_effort": reasoning_effort,
            "repeats": 1,
        },
        "started_at": started_at.isoformat(),
        "completed_at": completed_at.isoformat(),
        "duration_seconds": round(
            (completed_at - started_at).total_seconds(), 3
        ),
        "results": results,
        "timestamp_guardrail": (
            "The SHA-256 commitment binds these bytes but does not independently "
            "prove when they existed; publish the artifact or digest to an "
            "externally timestamped append-only system before resolution."
        ),
    }
    return _with_commitment(record)


def verify_live_shadow_seal(payload: dict[str, Any]) -> str:
    """Verify the top-level seal plus embedded scenario and trace digests."""
    digest = _verify_commitment(payload, expected_type=ARTIFACT_TYPE)
    if payload.get("scenario_sha256") != _digest(payload.get("scenario_source")):
        raise CaseValidationError("live-shadow seal: scenario digest mismatch")
    if payload.get("agent_payload_sha256") != _digest(payload.get("agent_payload")):
        raise CaseValidationError("live-shadow seal: agent payload digest mismatch")
    for index, result in enumerate(payload.get("results", [])):
        if not isinstance(result, dict):
            raise CaseValidationError(
                f"live-shadow seal: results[{index}] must be an object"
            )
        events = result.get("events")
        if result.get("events_sha256") != _digest(events):
            raise CaseValidationError(
                f"live-shadow seal: results[{index}] trace digest mismatch"
            )
    return digest


def resolve_live_shadow_seal(
    seal: dict[str, Any],
    label: dict[str, Any],
    *,
    today: date | None = None,
) -> dict[str, Any]:
    """Attach a matured label to an intact seal and score completed predictions."""
    seal_digest = verify_live_shadow_seal(seal)
    scenario = WalkForwardScenario.from_dict(
        _object(seal.get("scenario_source"), "scenario_source", "seal"),
        source="sealed scenario",
    )
    if scenario.mode != "live_shadow":
        raise CaseValidationError("sealed scenario: mode must be live_shadow")
    metrics, resolved_at, event_occurred = _validate_resolution_label(
        label,
        scenario=scenario,
        today=today or datetime.now(_scenario_timezone(scenario)).date(),
    )
    scored = []
    for run in seal["results"]:
        item = {
            "model": run["model"],
            "reasoning_effort": run["reasoning_effort"],
            "status": run["status"],
        }
        if run["status"] == "completed":
            item["submission"] = run["submission"]
            item["score"] = _score_probability(
                run["submission"],
                scenario=scenario,
                event_occurred=event_occurred,
            )
        scored.append(item)
    record = {
        "schema_version": 1,
        "artifact_type": RESOLUTION_TYPE,
        "created_at": datetime.now(UTC).isoformat(),
        "seal_commitment_sha256": seal_digest,
        "scenario_id": scenario.id,
        "resolved_at": resolved_at.isoformat(),
        "event_occurred": event_occurred,
        "realized_metrics": metrics,
        "label": label,
        "results": scored,
    }
    return _with_commitment(record)


def verify_live_shadow_resolution(payload: dict[str, Any]) -> str:
    """Verify a resolution artifact's own commitment."""
    return _verify_commitment(payload, expected_type=RESOLUTION_TYPE)


def _run_case(
    scenario: WalkForwardScenario,
    *,
    model: str,
    reasoning_effort: str,
    timeout_seconds: int,
) -> dict[str, Any]:
    started = time.monotonic()
    executed_at = datetime.now(UTC)
    with tempfile.TemporaryDirectory(prefix="finagentbench-live-shadow-") as raw:
        directory = Path(raw)
        schema_path = directory / "response-schema.json"
        output_path = directory / "response.json"
        schema_path.write_text(
            json.dumps(scenario.response_contract, ensure_ascii=False),
            encoding="utf-8",
        )
        prompt = (
            "你正在参加 FinAgentBench live-shadow 测试。必须使用原生实时 Web 搜索至少一次，"
            "并综合多份截至 as_of 已公开的证据。优先使用交易所、监管机构、公司法定披露和"
            "可核验的一手行业资料；不要把新闻标题当成已证实事实。不得寻找隐藏标签，因为"
            "目标结果在本次预测封存时尚未发生。evidence_urls 必须填写你实际使用的直接来源"
            "URL，且来源域名必须属于 search_tool.allowed_domains。目标事件和阈值以 target "
            "为准，相关性不得写成已经证明的因果关系。"
            "最终只返回符合 response_contract 的 JSON。题目如下：\n\n"
            + json.dumps(scenario.agent_payload(), ensure_ascii=False, indent=2)
        )
        command = [
            "codex",
            "--search",
            "exec",
            "--ignore-user-config",
            "--ignore-rules",
            "--model",
            model,
            "--config",
            f'model_reasoning_effort="{reasoning_effort}"',
            "--sandbox",
            "read-only",
            "--skip-git-repo-check",
            "--ephemeral",
            "--output-schema",
            str(schema_path),
            "--output-last-message",
            str(output_path),
            "--json",
            "--cd",
            str(directory),
            "-",
        ]
        try:
            completed = subprocess.run(
                command,
                input=prompt,
                text=True,
                capture_output=True,
                timeout=timeout_seconds,
                check=False,
            )
        except subprocess.TimeoutExpired as error:
            return _failure(
                model,
                reasoning_effort,
                executed_at=executed_at,
                started=started,
                error=f"timeout after {timeout_seconds}s",
                stdout=error.stdout or "",
            )
        if completed.returncode != 0:
            return _failure(
                model,
                reasoning_effort,
                executed_at=executed_at,
                started=started,
                error=f"codex exited {completed.returncode}: {completed.stderr[-3000:]}",
                stdout=completed.stdout,
            )
        events, usage = _parse_events(completed.stdout)
        search_calls = _web_search_call_count(events)
        try:
            submission = json.loads(output_path.read_text(encoding="utf-8"))
            _validate_live_submission(submission, scenario=scenario)
            if search_calls == 0:
                raise CaseValidationError(
                    "model completed without an observable live Web search call"
                )
        except (OSError, json.JSONDecodeError, CaseValidationError) as error:
            return _failure_from_events(
                model,
                reasoning_effort,
                executed_at=executed_at,
                started=started,
                error=f"invalid model response: {error}",
                events=events,
                usage=usage,
            )
        return {
            "model": model,
            "reasoning_effort": reasoning_effort,
            "status": "completed",
            "executed_at": executed_at.isoformat(),
            "latency_seconds": round(time.monotonic() - started, 3),
            "web_search_calls": search_calls,
            "submission": submission,
            "events": events,
            "events_sha256": _digest(events),
            "usage": usage,
        }


def _failure(
    model: str,
    reasoning_effort: str,
    *,
    executed_at: datetime,
    started: float,
    error: str,
    stdout: str | bytes,
) -> dict[str, Any]:
    if isinstance(stdout, bytes):
        stdout = stdout.decode("utf-8", errors="replace")
    events, usage = _parse_events(stdout)
    return _failure_from_events(
        model,
        reasoning_effort,
        executed_at=executed_at,
        started=started,
        error=error,
        events=events,
        usage=usage,
    )


def _failure_from_events(
    model: str,
    reasoning_effort: str,
    *,
    executed_at: datetime,
    started: float,
    error: str,
    events: list[dict[str, Any]],
    usage: dict[str, int],
) -> dict[str, Any]:
    return {
        "model": model,
        "reasoning_effort": reasoning_effort,
        "status": "failed",
        "executed_at": executed_at.isoformat(),
        "latency_seconds": round(time.monotonic() - started, 3),
        "error": error,
        "web_search_calls": _web_search_call_count(events),
        "events": events,
        "events_sha256": _digest(events),
        "usage": usage,
    }


def _validate_live_submission(
    submission: Any, *, scenario: WalkForwardScenario
) -> None:
    if not isinstance(submission, dict):
        raise CaseValidationError("live-shadow submission must be an object")
    required = {
        "event_probability",
        "prediction",
        "evidence_urls",
        "analysis_summary",
    }
    missing = sorted(required - submission.keys())
    if missing:
        raise CaseValidationError(
            f"live-shadow submission missing: {', '.join(missing)}"
        )
    probability = submission["event_probability"]
    if (
        not isinstance(probability, (int, float))
        or isinstance(probability, bool)
        or not math.isfinite(float(probability))
        or not 0 <= float(probability) <= 1
    ):
        raise CaseValidationError("event_probability must be between 0 and 1")
    prediction = submission["prediction"]
    implied = "event" if float(probability) >= 0.5 else "no_event"
    if prediction != implied:
        raise CaseValidationError(
            "prediction must agree with the 0.5 probability threshold"
        )
    urls = submission["evidence_urls"]
    if not isinstance(urls, list) or not urls:
        raise CaseValidationError("evidence_urls must be a non-empty list")
    for url in urls:
        if not isinstance(url, str) or urlparse(url).scheme not in {"http", "https"}:
            raise CaseValidationError("evidence_urls must contain HTTP(S) URLs")
        host = (urlparse(url).hostname or "").lower()
        if not any(
            host == domain or host.endswith(f".{domain}")
            for domain in scenario.search_policy.allowed_domains
        ):
            raise CaseValidationError(
                f"evidence URL domain {host!r} is not allowlisted"
            )
    if not isinstance(submission["analysis_summary"], str) or not submission[
        "analysis_summary"
    ].strip():
        raise CaseValidationError("analysis_summary must be non-empty")


def _validate_resolution_label(
    label: dict[str, Any],
    *,
    scenario: WalkForwardScenario,
    today: date,
) -> tuple[dict[str, float], date, bool]:
    required = {
        "schema_version",
        "artifact_type",
        "scenario_id",
        "resolved_at",
        "event_occurred",
        "realized",
        "outcome_sources",
    }
    missing = sorted(required - label.keys())
    if missing:
        raise CaseValidationError(
            f"live-shadow label missing: {', '.join(missing)}"
        )
    if label["schema_version"] != 1 or label["artifact_type"] != LABEL_TYPE:
        raise CaseValidationError("live-shadow label contract is unsupported")
    if label["scenario_id"] != scenario.id:
        raise CaseValidationError("live-shadow label scenario_id mismatch")
    try:
        resolved_at = date.fromisoformat(label["resolved_at"])
    except (TypeError, ValueError) as error:
        raise CaseValidationError(
            "live-shadow label resolved_at must be YYYY-MM-DD"
        ) from error
    if not scenario.as_of < resolved_at <= scenario.window_end:
        raise CaseValidationError(
            "live-shadow label resolved_at must be inside the prediction window"
        )
    if resolved_at > today:
        raise CaseValidationError("live-shadow label cannot resolve in the future")
    sources = label["outcome_sources"]
    if not isinstance(sources, list) or not sources:
        raise CaseValidationError("outcome_sources must be a non-empty list")
    for index, source in enumerate(sources):
        if not isinstance(source, dict) or not source:
            raise CaseValidationError(
                f"outcome_sources[{index}] must be a non-empty object"
            )
        published_at = source.get("published_at")
        if published_at is not None:
            try:
                published = date.fromisoformat(published_at)
            except (TypeError, ValueError) as error:
                raise CaseValidationError(
                    f"outcome_sources[{index}] published_at must be YYYY-MM-DD"
                ) from error
            if published > resolved_at:
                raise CaseValidationError(
                    f"outcome_sources[{index}] is published after resolved_at"
                )
    event_occurred = label["event_occurred"]
    realized = _object(label["realized"], "realized", "live-shadow label")
    metrics = validate_realized_outcome(
        scenario,
        realized,
        event_occurred=event_occurred,
        source="live-shadow label",
    )
    return metrics, resolved_at, event_occurred


def _score_probability(
    submission: dict[str, Any],
    *,
    scenario: WalkForwardScenario,
    event_occurred: bool,
) -> dict[str, Any]:
    _validate_live_submission(submission, scenario=scenario)
    probability = float(submission["event_probability"])
    observed = float(event_occurred)
    brier_loss = (probability - observed) ** 2
    clipped = min(max(probability, 1e-15), 1 - 1e-15)
    log_loss = -(
        observed * math.log(clipped) + (1 - observed) * math.log(1 - clipped)
    )
    expected = "event" if event_occurred else "no_event"
    return {
        "brier_score": round(100 * (1 - brier_loss), 6),
        "brier_loss": round(brier_loss, 8),
        "log_loss": round(log_loss, 8),
        "classification_correct": submission["prediction"] == expected,
    }


def _with_commitment(record: dict[str, Any]) -> dict[str, Any]:
    return {
        **record,
        "commitment": {
            "algorithm": "sha256",
            "canonicalization": CANONICALIZATION,
            "payload_sha256": _digest(record),
        },
    }


def _verify_commitment(payload: dict[str, Any], *, expected_type: str) -> str:
    if not isinstance(payload, dict) or payload.get("artifact_type") != expected_type:
        raise CaseValidationError(f"expected artifact_type {expected_type}")
    commitment = payload.get("commitment")
    if not isinstance(commitment, dict):
        raise CaseValidationError("artifact commitment is missing")
    if commitment.get("algorithm") != "sha256":
        raise CaseValidationError("artifact commitment algorithm is unsupported")
    if commitment.get("canonicalization") != CANONICALIZATION:
        raise CaseValidationError("artifact canonicalization is unsupported")
    record = {key: value for key, value in payload.items() if key != "commitment"}
    calculated = _digest(record)
    if commitment.get("payload_sha256") != calculated:
        raise CaseValidationError("artifact commitment digest mismatch")
    return calculated


def _digest(payload: Any) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _parse_events(stdout: str) -> tuple[list[dict[str, Any]], dict[str, int]]:
    events = []
    usage = {}
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(event, dict):
            continue
        events.append(event)
        candidate = event.get("usage")
        if isinstance(candidate, dict):
            usage = {
                key: int(value)
                for key, value in candidate.items()
                if isinstance(value, int) and not isinstance(value, bool)
            }
    return events, usage


def _web_search_call_count(events: list[dict[str, Any]]) -> int:
    calls = 0
    for event in events:
        if event.get("type") != "item.completed":
            continue
        item = event.get("item")
        if not isinstance(item, dict):
            continue
        item_type = str(item.get("type", "")).lower()
        if "web_search" in item_type or item_type == "web_search_call":
            calls += 1
    return calls


def _scenario_timezone(scenario: WalkForwardScenario) -> ZoneInfo:
    if scenario.security.exchange in {"SSE", "SZSE", "BSE"}:
        return ZoneInfo("Asia/Shanghai")
    return ZoneInfo("UTC")


def _read_object(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise CaseValidationError(f"{path}: invalid JSON: {error}") from error
    return _object(payload, "top-level value", str(path))


def _object(value: Any, field: str, source: str) -> dict[str, Any]:
    if not isinstance(value, dict) or not value:
        raise CaseValidationError(f"{source}: {field} must be a non-empty object")
    return value


def _command_output(command: list[str]) -> str:
    completed = subprocess.run(
        command, text=True, capture_output=True, check=True, timeout=10
    )
    return completed.stdout.strip()

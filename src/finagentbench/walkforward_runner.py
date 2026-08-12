"""Codex replay runner for A-share cases with a frozen search tool."""

from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
import time
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from finagentbench.adapter import (
    AdapterError,
    StdioAdapter,
    build_adapter_request,
)
from finagentbench.walkforward import (
    WalkForwardCase,
    score_walkforward_submission,
)


@dataclass(frozen=True)
class WalkForwardRunSpec:
    model: str
    reasoning_effort: str
    case: WalkForwardCase


def run_walkforward_codex_matrix(
    cases: tuple[WalkForwardCase, ...],
    *,
    models: tuple[str, ...],
    reasoning_effort: str,
    workers: int,
    timeout_seconds: int,
    progress: Callable[[dict[str, Any]], None] | None = None,
) -> dict[str, Any]:
    """Run isolated Codex sessions with only scenario and frozen-search access."""
    specs = [
        WalkForwardRunSpec(model=model, reasoning_effort=reasoning_effort, case=case)
        for model in models
        for case in cases
    ]
    started_at = datetime.now(UTC)
    codex_version = _command_output(["codex", "--version"])
    results = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(_run_case, spec, timeout_seconds=timeout_seconds): spec
            for spec in specs
        }
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            if progress is not None:
                progress(result)
    results.sort(key=lambda item: (item["model"], item["scenario_id"]))
    completed_at = datetime.now(UTC)
    return {
        "schema_version": 1,
        "started_at": started_at.isoformat(),
        "completed_at": completed_at.isoformat(),
        "duration_seconds": round((completed_at - started_at).total_seconds(), 3),
        "harness": {
            "name": "codex-cli-frozen-search",
            "version": codex_version,
            "sandbox": "read-only",
            "external_data": "frozen point-in-time evidence corpus",
            "session_persistence": False,
            "outcome_visible_to_agent": False,
        },
        "matrix": {
            "models": list(models),
            "reasoning_effort": reasoning_effort,
            "case_count": len(cases),
            "repeats": 1,
            "case_suite_sha256": _suite_digest(cases),
        },
        "scoring_contract": {
            "version": 1,
            "brier_score_weight": 0.85,
            "evidence_f1_weight": 0.15,
            "diagnostics": ["brier_loss", "log_loss", "classification_accuracy"],
        },
        "results": results,
        "summary": summarize_walkforward_results(results),
    }


def run_walkforward_adapter_matrix(
    cases: tuple[WalkForwardCase, ...],
    *,
    models: tuple[str, ...],
    reasoning_effort: str,
    workers: int,
    timeout_seconds: int,
    adapter: StdioAdapter,
    progress: Callable[[dict[str, Any]], None] | None = None,
) -> dict[str, Any]:
    """Run frozen-search cases through a provider-neutral stdio adapter."""
    adapter.require_capability("frozen_search")
    specs = [
        WalkForwardRunSpec(
            model=model,
            reasoning_effort=reasoning_effort,
            case=case,
        )
        for model in models
        for case in cases
    ]
    started_at = datetime.now(UTC)
    harness = adapter.harness_metadata(
        external_data="frozen point-in-time evidence corpus"
    )
    results = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(
                _run_adapter_case,
                spec,
                adapter=adapter,
                timeout_seconds=timeout_seconds,
            ): spec
            for spec in specs
        }
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            if progress is not None:
                progress(result)
    results.sort(key=lambda item: (item["model"], item["scenario_id"]))
    completed_at = datetime.now(UTC)
    return {
        "schema_version": 1,
        "started_at": started_at.isoformat(),
        "completed_at": completed_at.isoformat(),
        "duration_seconds": round((completed_at - started_at).total_seconds(), 3),
        "harness": harness,
        "matrix": {
            "models": list(models),
            "reasoning_effort": reasoning_effort,
            "case_count": len(cases),
            "repeats": 1,
            "case_suite_sha256": _suite_digest(cases),
        },
        "scoring_contract": {
            "version": 1,
            "brier_score_weight": 0.85,
            "evidence_f1_weight": 0.15,
            "diagnostics": [
                "brier_loss",
                "log_loss",
                "classification_accuracy",
            ],
        },
        "results": results,
        "summary": summarize_walkforward_results(results),
    }


def summarize_walkforward_results(
    results: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    summaries = []
    for model in sorted({item["model"] for item in results}):
        model_results = [item for item in results if item["model"] == model]
        successful = [item for item in model_results if item["status"] == "completed"]
        scores = [item["score"] for item in successful]
        usage = [_usage_totals(item.get("usage", {})) for item in successful]
        summaries.append(
            {
                "model": model,
                "completed": len(successful),
                "failed": len(model_results) - len(successful),
                "mean_score": _mean(item["total"] for item in scores),
                "mean_brier_loss": _mean(item["brier_loss"] for item in scores),
                "mean_log_loss": _mean(item["log_loss"] for item in scores),
                "classification_accuracy": _mean(
                    float(item["classification_correct"]) for item in scores
                ),
                "mean_evidence_f1": _mean(item["evidence_f1"] for item in scores),
                "search_usage_rate": _mean(
                    float(item["search_calls"] > 0) for item in successful
                ),
                "mean_latency_seconds": _mean(
                    item["latency_seconds"] for item in successful
                ),
                "input_tokens": sum(item["input_tokens"] for item in usage),
                "cached_input_tokens": sum(
                    item["cached_input_tokens"] for item in usage
                ),
                "output_tokens": sum(item["output_tokens"] for item in usage),
            }
        )
    return summaries


def render_walkforward_report(run: dict[str, Any]) -> str:
    harness_label = _harness_label(run["harness"])
    lines = [
        "# FinAgentBench A-share frozen-web replay",
        "",
        (
            f"Harness: `{harness_label}` · effort: "
            f"`{run['matrix']['reasoning_effort']}` · "
            f"cases: {run['matrix']['case_count']} · repeats: "
            f"{run['matrix']['repeats']}"
        ),
        f"Case suite: `{run['matrix']['case_suite_sha256']}`",
        "",
        "| Model | Score | Brier loss | Log loss | Accuracy | Evidence F1 | Search use | Latency | Failures |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in run["summary"]:
        lines.append(
            "| {model} | {score:.2f} | {brier:.4f} | {log:.4f} | "
            "{accuracy:.1%} | {evidence:.3f} | {search:.1%} | "
            "{latency:.2f}s | {failed} |".format(
                model=item["model"],
                score=item["mean_score"],
                brier=item["mean_brier_loss"],
                log=item["mean_log_loss"],
                accuracy=item["classification_accuracy"],
                evidence=item["mean_evidence_f1"],
                search=item["search_usage_rate"],
                latency=item["mean_latency_seconds"],
                failed=item["failed"],
            )
        )
    lines.extend(
        [
            "",
            "## Interpretation guardrails",
            "",
            "- This is a public historical development set, not a sealed leaderboard.",
            "- Search was restricted to frozen documents/news published by each as-of date.",
            "- The outcome label was loaded only after the model returned its prediction.",
            "- Brier and log loss assess probability quality; this run is too small for calibration claims.",
            "",
            "## Per-scenario results",
            "",
            "| Model | Scenario | Probability | Outcome | Score | Brier loss | Evidence F1 | Searches |",
            "| --- | --- | ---: | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in run["results"]:
        if item["status"] != "completed":
            lines.append(
                f"| {item['model']} | {item['scenario_id']} | — | — | failed | — | — | — |"
            )
            continue
        outcome = "event" if item["outcome"] else "no_event"
        lines.append(
            f"| {item['model']} | {item['scenario_id']} | "
            f"{item['submission']['event_probability']:.3f} | {outcome} | "
            f"{item['score']['total']:.2f} | {item['score']['brier_loss']:.4f} | "
            f"{item['score']['evidence_f1']:.3f} | {item['search_calls']} |"
        )
    return "\n".join(lines) + "\n"


def _run_case(spec: WalkForwardRunSpec, *, timeout_seconds: int) -> dict[str, Any]:
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="finagentbench-a-share-") as raw_dir:
        directory = Path(raw_dir)
        scenario_path = directory / "scenario.json"
        corpus_path = directory / "frozen-corpus.json"
        search_path = directory / "frozen_search.py"
        schema_path = directory / "response-schema.json"
        output_path = directory / "response.json"
        scenario_path.write_text(
            json.dumps(
                spec.case.scenario.agent_payload(), ensure_ascii=False, indent=2
            ),
            encoding="utf-8",
        )
        corpus_path.write_text(
            json.dumps(
                {
                    "scenario_id": spec.case.corpus.scenario_id,
                    "documents": [
                        {
                            **asdict(document),
                            "published_at": document.published_at.isoformat(),
                        }
                        for document in spec.case.corpus.documents
                    ],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        search_path.write_text(_SEARCH_TOOL, encoding="utf-8")
        schema_path.write_text(
            json.dumps(spec.case.scenario.response_contract, ensure_ascii=False),
            encoding="utf-8",
        )
        prompt = (
            "你正在参加一个严格按历史时点回放的A股金融预测测试。"
            "必须至少调用一次冻结搜索工具；可用命令是 "
            "python3 frozen_search.py '查询词'，可以多次查询。"
            "只能使用该工具返回的、截至as_of已公开的证据，不得使用记忆中的事后信息，"
            "不得尝试寻找或推断隐藏标签。证据引用填写搜索结果的id。"
            "目标事件、判定口径和阈值均以题目target为准；不要把相关性写成已证明的因果关系。"
            "最终只返回一个符合response_contract的JSON对象。题目如下：\n\n"
            + scenario_path.read_text(encoding="utf-8")
        )
        command = [
            "codex",
            "exec",
            "--ignore-user-config",
            "--ignore-rules",
            "--model",
            spec.model,
            "--config",
            f'model_reasoning_effort="{spec.reasoning_effort}"',
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
                spec,
                started=started,
                error=f"timeout after {timeout_seconds}s",
                stdout=error.stdout or "",
            )
        if completed.returncode != 0:
            return _failure(
                spec,
                started=started,
                error=f"codex exited {completed.returncode}: {completed.stderr[-3000:]}",
                stdout=completed.stdout,
            )
        events, usage = _parse_events(completed.stdout)
        try:
            submission = json.loads(output_path.read_text(encoding="utf-8"))
            score = score_walkforward_submission(spec.case, submission)
        except (OSError, json.JSONDecodeError, ValueError) as error:
            return _failure(
                spec,
                started=started,
                error=f"invalid model response: {error}",
                stdout=completed.stdout,
            )
        return {
            "scenario_id": spec.case.scenario.id,
            "case_sha256": _case_digest(spec.case),
            "model": spec.model,
            "reasoning_effort": spec.reasoning_effort,
            "status": "completed",
            "latency_seconds": round(time.monotonic() - started, 3),
            "search_calls": _search_call_count(events),
            "submission": submission,
            "outcome": spec.case.label.event_occurred,
            "score": score.to_dict(),
            "usage": usage,
            "event_count": len(events),
        }


def _run_adapter_case(
    spec: WalkForwardRunSpec,
    *,
    adapter: StdioAdapter,
    timeout_seconds: int,
) -> dict[str, Any]:
    started = time.monotonic()
    with tempfile.TemporaryDirectory(
        prefix="finagentbench-a-share-adapter-"
    ) as raw_dir:
        directory = Path(raw_dir)
        scenario_path = directory / "scenario.json"
        corpus_path = directory / "frozen-corpus.json"
        search_path = directory / "frozen_search.py"
        scenario_path.write_text(
            json.dumps(
                spec.case.scenario.agent_payload(),
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        corpus_path.write_text(
            json.dumps(
                {
                    "scenario_id": spec.case.corpus.scenario_id,
                    "documents": [
                        {
                            **asdict(document),
                            "published_at": document.published_at.isoformat(),
                        }
                        for document in spec.case.corpus.documents
                    ],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        search_path.write_text(_SEARCH_TOOL, encoding="utf-8")
        prompt = (
            "你正在参加一个严格按历史时点回放的A股金融预测测试。"
            "必须至少调用一次冻结搜索工具；adapter应提供名为frozen_search的工具，"
            "其唯一参数是查询词。只能使用该工具返回的、截至as_of已公开的证据，"
            "不得使用记忆中的事后信息，不得尝试寻找或推断隐藏标签。"
            "证据引用填写搜索结果的id。目标事件、判定口径和阈值均以题目target为准；"
            "不要把相关性写成已证明的因果关系。"
            "最终只返回一个符合response_contract的JSON对象。题目如下：\n\n"
            + scenario_path.read_text(encoding="utf-8")
        )
        request = build_adapter_request(
            task="a_share_frozen_web",
            model=spec.model,
            reasoning_effort=spec.reasoning_effort,
            prompt=prompt,
            response_contract=spec.case.scenario.response_contract,
            required_tools=("frozen_search",),
            available_files=(
                "scenario.json",
                "frozen-corpus.json",
                "frozen_search.py",
            ),
        )
        try:
            output = adapter.run(
                request,
                directory=directory,
                timeout_seconds=timeout_seconds,
            )
            score = score_walkforward_submission(spec.case, output.submission)
        except (AdapterError, ValueError) as error:
            return {
                "scenario_id": spec.case.scenario.id,
                "case_sha256": _case_digest(spec.case),
                "model": spec.model,
                "reasoning_effort": spec.reasoning_effort,
                "status": "failed",
                "latency_seconds": round(time.monotonic() - started, 3),
                "error": str(error),
                "usage": {},
            }
    result = {
        "scenario_id": spec.case.scenario.id,
        "case_sha256": _case_digest(spec.case),
        "model": spec.model,
        "reasoning_effort": spec.reasoning_effort,
        "status": "completed",
        "latency_seconds": round(time.monotonic() - started, 3),
        "search_calls": output.tool_calls.get("frozen_search", 0),
        "submission": output.submission,
        "outcome": spec.case.label.event_occurred,
        "score": score.to_dict(),
        "usage": output.usage,
        "event_count": len(output.events),
    }
    if output.metadata:
        result["adapter_metadata"] = output.metadata
    return result


def _failure(
    spec: WalkForwardRunSpec, *, started: float, error: str, stdout: str | bytes
) -> dict[str, Any]:
    if isinstance(stdout, bytes):
        stdout = stdout.decode("utf-8", errors="replace")
    events, usage = _parse_events(stdout)
    return {
        "scenario_id": spec.case.scenario.id,
        "case_sha256": _case_digest(spec.case),
        "model": spec.model,
        "reasoning_effort": spec.reasoning_effort,
        "status": "failed",
        "latency_seconds": round(time.monotonic() - started, 3),
        "error": error,
        "usage": usage,
        "events_tail": events[-5:],
    }


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


def _usage_totals(usage: dict[str, int]) -> dict[str, int]:
    return {
        "input_tokens": usage.get("input_tokens", 0),
        "cached_input_tokens": usage.get("cached_input_tokens", 0),
        "output_tokens": usage.get("output_tokens", 0),
    }


def _search_call_count(events: list[dict[str, Any]]) -> int:
    calls = 0
    for event in events:
        if event.get("type") != "item.completed":
            continue
        item = event.get("item")
        if not isinstance(item, dict) or item.get("type") != "command_execution":
            continue
        command = item.get("command", "")
        if isinstance(command, str) and "frozen_search.py" in command:
            calls += 1
    return calls


def _mean(values: Any) -> float:
    items = list(values)
    return round(sum(items) / len(items), 6) if items else 0.0


def _command_output(command: list[str]) -> str:
    completed = subprocess.run(
        command, text=True, capture_output=True, check=True, timeout=10
    )
    return completed.stdout.strip()


def _harness_label(harness: dict[str, Any]) -> str:
    name = str(harness.get("name", "")).strip()
    version = str(harness.get("version", "")).strip()
    if name and name.lower() not in version.lower():
        return f"{name} {version}".strip()
    return version or name or "unknown"


def _case_digest(case: WalkForwardCase) -> str:
    payload = {
        "scenario": case.scenario.agent_payload(),
        "corpus": [
            {**asdict(item), "published_at": item.published_at.isoformat()}
            for item in case.corpus.documents
        ],
        "label": {
            **asdict(case.label),
            "resolved_at": case.label.resolved_at.isoformat(),
            "observed_at": (
                case.label.observed_at.isoformat()
                if case.label.observed_at is not None
                else None
            ),
        },
    }
    encoded = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _suite_digest(cases: tuple[WalkForwardCase, ...]) -> str:
    manifest = "\n".join(
        f"{case.scenario.id}:{_case_digest(case)}"
        for case in sorted(cases, key=lambda item: item.scenario.id)
    )
    return hashlib.sha256(manifest.encode("utf-8")).hexdigest()


_SEARCH_TOOL = r"""#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

if len(sys.argv) != 2 or not sys.argv[1].strip():
    raise SystemExit("usage: python3 frozen_search.py 'query'")
query = sys.argv[1].lower().strip()
terms = {part for part in re.split(r"[^\w\u4e00-\u9fff]+", query) if part}
compact = re.sub(r"[^\w\u4e00-\u9fff]", "", query)
if len(compact) >= 2:
    terms.update(compact[index:index + 2] for index in range(len(compact) - 1))
payload = json.loads(Path(__file__).with_name("frozen-corpus.json").read_text())
matches = []
for document in payload["documents"]:
    haystack = f"{document['title']}\n{document['content']}".lower()
    score = sum(haystack.count(term) * len(term) for term in terms)
    if score <= 0:
        continue
    matches.append({
        "id": document["id"],
        "title": document["title"],
        "published_at": document["published_at"],
        "source": document["source"],
        "url": document["url"],
        "content": document["content"],
        "score": score,
    })
matches.sort(key=lambda item: (-item["score"], item["id"]))
print(json.dumps(matches[:5], ensure_ascii=False, indent=2))
"""

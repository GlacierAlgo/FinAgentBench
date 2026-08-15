"""End-to-end Codex baseline for self-contained Markdown points."""

from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
import time
from collections import Counter
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from pitfall.errors import CaseValidationError
from pitfall.evaluation import (
    JUDGE_MODEL,
    JUDGE_REASONING_EFFORT,
    EvaluationClass,
    parse_evaluation,
)
from pitfall.point import Point

ARTIFACT_TYPE = "pitfall_point_baseline"


def run_point_baseline(
    points: tuple[Point, ...],
    *,
    model: str,
    reasoning_effort: str,
    workers: int,
    timeout_seconds: int,
    output: Path,
    resume: bool,
    progress: Callable[[dict[str, Any]], None] | None = None,
) -> dict[str, Any]:
    """Run Question -> Answer -> pinned Judge and checkpoint every point."""
    if not points:
        raise CaseValidationError("baseline requires at least one point")
    if not model.strip():
        raise CaseValidationError("baseline model must be non-empty")
    if workers < 1:
        raise CaseValidationError("baseline workers must be positive")
    if timeout_seconds < 10:
        raise CaseValidationError("baseline timeout must be at least 10 seconds")

    point_ids = [point.id for point in points]
    if len(point_ids) != len(set(point_ids)):
        raise CaseValidationError("baseline point ids must be unique")

    started_at = datetime.now(UTC).isoformat()
    results_by_id: dict[str, dict[str, Any]] = {}
    codex_version = _command_output(["codex", "--version"])
    if resume and output.exists():
        previous = _read_json(output)
        _validate_resume(
            previous,
            points=points,
            model=model,
            reasoning_effort=reasoning_effort,
        )
        started_at = previous["started_at"]
        codex_version = previous["harness"]["version"]
        results_by_id = {
            item["point_id"]: item
            for item in previous["results"]
            if item.get("status") == "completed"
        }

    pending = [point for point in points if point.id not in results_by_id]
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(
                _run_point,
                point,
                model=model,
                reasoning_effort=reasoning_effort,
                timeout_seconds=timeout_seconds,
            ): point
            for point in pending
        }
        for future in as_completed(futures):
            point = futures[future]
            try:
                result = future.result()
            except Exception as error:  # noqa: BLE001 - checkpoint the batch
                result = {
                    **_point_identity(point),
                    "status": "failed_runner",
                    "error": f"{type(error).__name__}: {error}",
                }
            results_by_id[point.id] = result
            record = _build_record(
                points=points,
                model=model,
                reasoning_effort=reasoning_effort,
                codex_version=codex_version,
                started_at=started_at,
                results=list(results_by_id.values()),
                running=True,
            )
            _write_json_atomic(output, record)
            if progress is not None:
                progress(result)

    record = _build_record(
        points=points,
        model=model,
        reasoning_effort=reasoning_effort,
        codex_version=codex_version,
        started_at=started_at,
        results=list(results_by_id.values()),
        running=False,
    )
    _write_json_atomic(output, record)
    return record


def verify_point_baseline(
    payload: dict[str, Any], points: tuple[Point, ...]
) -> None:
    """Prove exact point coverage, current hashes, and valid Judge outputs."""
    if payload.get("schema_version") != 1:
        raise CaseValidationError("baseline schema_version must be 1")
    if payload.get("artifact_type") != ARTIFACT_TYPE:
        raise CaseValidationError(f"expected artifact_type {ARTIFACT_TYPE}")
    if payload.get("status") != "complete":
        raise CaseValidationError("baseline artifact is not complete")
    judge = payload.get("judge")
    if judge != {
        "model": JUDGE_MODEL,
        "reasoning_effort": JUDGE_REASONING_EFFORT,
    }:
        raise CaseValidationError("baseline Judge runtime is not pinned")

    expected = {point.id: point for point in points}
    results = payload.get("results")
    if not isinstance(results, list):
        raise CaseValidationError("baseline results must be a list")
    actual_ids = [item.get("point_id") for item in results if isinstance(item, dict)]
    if len(actual_ids) != len(results) or set(actual_ids) != set(expected):
        raise CaseValidationError("baseline results do not exactly cover selected points")
    if len(actual_ids) != len(set(actual_ids)):
        raise CaseValidationError("baseline results contain duplicate point ids")
    if payload.get("point_count") != len(points):
        raise CaseValidationError("baseline point_count mismatch")
    if payload.get("point_suite_sha256") != _suite_digest(points):
        raise CaseValidationError("baseline point suite digest mismatch")

    for item in results:
        point = expected[item["point_id"]]
        identity = _point_identity(point)
        for key, value in identity.items():
            if item.get(key) != value:
                raise CaseValidationError(
                    f"{point.id}: baseline {key} does not match current point"
                )
        if item.get("status") != "completed":
            raise CaseValidationError(f"{point.id}: baseline result is not completed")
        if not isinstance(item.get("answer"), str):
            raise CaseValidationError(f"{point.id}: baseline answer must be text")
        evaluation = item.get("evaluation")
        if not isinstance(evaluation, dict):
            raise CaseValidationError(f"{point.id}: evaluation must be an object")
        parsed = parse_evaluation(
            f"Class: {evaluation.get('class', '')}\n\n"
            f"{evaluation.get('decisive_reason', '')}"
        )
        if parsed.classification.value != evaluation.get("class"):
            raise CaseValidationError(f"{point.id}: evaluation class mismatch")

    expected_summary = summarize_baseline_results(results)
    if payload.get("summary") != expected_summary:
        raise CaseValidationError("baseline summary mismatch")


def render_baseline_report(payload: dict[str, Any]) -> str:
    """Render a compact report with pointwise progressive disclosure."""
    summary = payload["summary"]
    lines = [
        "# PITFALL end-to-end point baseline",
        "",
        (
            f"Agent: `{payload['agent']['model']}` / "
            f"`{payload['agent']['reasoning_effort']}` · Judge: "
            f"`{payload['judge']['model']}` / "
            f"`{payload['judge']['reasoning_effort']}` · "
            f"points: {payload['point_count']}"
        ),
        "",
        (
            f"Status: **{payload['status']}** · completed: "
            f"{summary['completed']} · failed: {summary['failed']}"
        ),
        "",
        "## Classification",
        "",
        "| Class | Count |",
        "| --- | ---: |",
    ]
    for classification in EvaluationClass:
        lines.append(
            f"| `{classification.value}` | "
            f"{summary['class_counts'][classification.value]} |"
        )
    lines.extend(
        [
            "",
            "## Usage",
            "",
            f"- Agent input tokens: {summary['agent_usage']['input_tokens']}",
            f"- Agent output tokens: {summary['agent_usage']['output_tokens']}",
            f"- Judge input tokens: {summary['judge_usage']['input_tokens']}",
            f"- Judge output tokens: {summary['judge_usage']['output_tokens']}",
            f"- Agent Web searches: {summary['web_search_calls']}",
            "",
            "## Pointwise results",
            "",
        ]
    )
    for item in payload["results"]:
        classification = item.get("evaluation", {}).get("class", item["status"])
        lines.extend([f"### {item['point_id']} — `{classification}`", ""])
        if item["status"] != "completed":
            lines.extend([f"Error: {item.get('error', 'unknown failure')}", ""])
            continue
        lines.extend(
            [
                _clean_markdown(item["evaluation"]["decisive_reason"]),
                "",
                "<details>",
                "<summary>Answer</summary>",
                "",
                _clean_markdown(item["answer"]),
                "",
                "</details>",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def summarize_baseline_results(results: list[dict[str, Any]]) -> dict[str, Any]:
    completed = [item for item in results if item.get("status") == "completed"]
    classes = Counter(item["evaluation"]["class"] for item in completed)
    return {
        "completed": len(completed),
        "failed": len(results) - len(completed),
        "class_counts": {
            classification.value: classes[classification.value]
            for classification in EvaluationClass
        },
        "agent_usage": _sum_usage(item.get("agent", {}).get("usage", {}) for item in results),
        "judge_usage": _sum_usage(item.get("judge", {}).get("usage", {}) for item in results),
        "web_search_calls": sum(
            item.get("agent", {}).get("web_search_calls", 0) for item in results
        ),
    }


def _run_point(
    point: Point,
    *,
    model: str,
    reasoning_effort: str,
    timeout_seconds: int,
) -> dict[str, Any]:
    started = time.monotonic()
    identity = _point_identity(point)
    agent = _invoke_codex(
        prompt=_agent_prompt(point),
        model=model,
        reasoning_effort=reasoning_effort,
        timeout_seconds=timeout_seconds,
        web_search=True,
    )
    if agent["status"] != "completed":
        return {
            **identity,
            "status": "failed_agent",
            "latency_seconds": round(time.monotonic() - started, 3),
            "agent": agent,
            "error": agent["error"],
        }

    answer = agent["message"]
    judge = _invoke_codex(
        prompt=_judge_prompt(point, answer),
        model=JUDGE_MODEL,
        reasoning_effort=JUDGE_REASONING_EFFORT,
        timeout_seconds=timeout_seconds,
        web_search=False,
    )
    if judge["status"] != "completed":
        return {
            **identity,
            "status": "failed_judge",
            "latency_seconds": round(time.monotonic() - started, 3),
            "agent": agent,
            "answer": answer,
            "judge": judge,
            "error": judge["error"],
        }
    try:
        evaluation = parse_evaluation(judge["message"])
    except CaseValidationError as error:
        return {
            **identity,
            "status": "failed_judge",
            "latency_seconds": round(time.monotonic() - started, 3),
            "agent": agent,
            "answer": answer,
            "judge": judge,
            "error": f"invalid Judge response: {error}",
        }
    return {
        **identity,
        "status": "completed",
        "latency_seconds": round(time.monotonic() - started, 3),
        "agent": agent,
        "answer": answer,
        "judge": judge,
        "evaluation": {
            "class": evaluation.classification.value,
            "decisive_reason": evaluation.decisive_reason,
        },
    }


def _invoke_codex(
    *,
    prompt: str,
    model: str,
    reasoning_effort: str,
    timeout_seconds: int,
    web_search: bool,
) -> dict[str, Any]:
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="pitfall-point-") as raw:
        directory = Path(raw)
        output_path = directory / "last-message.md"
        command = ["codex"]
        if web_search:
            command.append("--search")
        command.extend(
            [
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
                "--output-last-message",
                str(output_path),
                "--json",
                "--cd",
                str(directory),
                "-",
            ]
        )
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
            stdout = error.stdout or ""
            if isinstance(stdout, bytes):
                stdout = stdout.decode("utf-8", errors="replace")
            events, usage = _parse_events(stdout)
            return {
                "status": "failed",
                "latency_seconds": round(time.monotonic() - started, 3),
                "error": f"timeout after {timeout_seconds}s",
                "usage": usage,
                "events_tail": events[-5:],
            }

        events, usage = _parse_events(completed.stdout)
        if completed.returncode != 0:
            return {
                "status": "failed",
                "latency_seconds": round(time.monotonic() - started, 3),
                "error": (
                    f"codex exited {completed.returncode}: "
                    f"{completed.stderr[-3000:]}"
                ),
                "usage": usage,
                "events_tail": events[-5:],
            }
        try:
            message = output_path.read_text(encoding="utf-8")
        except OSError as error:
            return {
                "status": "failed",
                "latency_seconds": round(time.monotonic() - started, 3),
                "error": f"cannot read Codex final message: {error}",
                "usage": usage,
                "events_tail": events[-5:],
            }
        tool_counts = _tool_counts(events)
        return {
            "status": "completed",
            "latency_seconds": round(time.monotonic() - started, 3),
            "message": message,
            "usage": usage,
            "event_count": len(events),
            "tool_counts": tool_counts,
            "web_search_calls": sum(
                count
                for name, count in tool_counts.items()
                if "web_search" in name
            ),
        }


def _agent_prompt(point: Point) -> str:
    return (
        "你正在参加 PITFALL 端到端金融推理 baseline。你只能看到 Question，"
        "看不到 Ground Truth。你可以按需使用原生 Web 搜索、代码和其他可用工具；"
        "必须遵守题目给出的时间边界、证据边界与输出要求。不要讨论评分或猜测隐藏答案。"
        "最终返回一份自包含、可核验的答案。\n\n"
        "<Question>\n"
        f"{point.agent_payload()}\n"
        "</Question>"
    )


def _judge_prompt(point: Point, answer: str) -> str:
    classes = (
        "- completely_correct：最终答案及所有影响结论的关键主张均正确。\n"
        "- numeric_factual_error：金额、比例、数量、价格或其他数值事实错误。\n"
        "- non_numeric_factual_error：实体、事件、状态、方向或制度等事实错误。\n"
        "- analysis_assumption_error：依赖无依据的前提、代理变量、外推或边界。\n"
        "- analysis_logic_error：事实可接受，但计算、比较或推导无效。\n"
        "- other_error：空答、拒答、跑题、不可解析或缺失关键输出。"
    )
    return (
        "你是 PITFALL Judge。只比较 Question、Answer 与 Ground Truth，"
        "把 Answer 归入且只归入以下六类之一。多个错误并存时，选择可见推理链中"
        "最早导致最终结论失效的决定性错误。读错数字属于 numeric_factual_error；"
        "数字正确但计算错属于 analysis_logic_error。\n\n"
        f"{classes}\n\n"
        "严格只输出以下 Markdown 合同，不要添加标题、代码块或其他字段：\n\n"
        "Class: <class>\n\n<最短充分的 decisive_reason>\n\n"
        f"<Question>\n{point.question}\n</Question>\n\n"
        f"<Answer>\n{answer}\n</Answer>\n\n"
        f"<GroundTruth>\n{point.ground_truth}\n</GroundTruth>"
    )


def _build_record(
    *,
    points: tuple[Point, ...],
    model: str,
    reasoning_effort: str,
    codex_version: str,
    started_at: str,
    results: list[dict[str, Any]],
    running: bool,
) -> dict[str, Any]:
    ordered = sorted(results, key=lambda item: item["point_id"])
    all_completed = len(ordered) == len(points) and all(
        item.get("status") == "completed" for item in ordered
    )
    status = "running" if running else ("complete" if all_completed else "incomplete")
    return {
        "schema_version": 1,
        "artifact_type": ARTIFACT_TYPE,
        "status": status,
        "started_at": started_at,
        "updated_at": datetime.now(UTC).isoformat(),
        "harness": {
            "name": "codex-cli-native-web",
            "version": codex_version,
            "sandbox": "read-only",
            "session_persistence": False,
            "ground_truth_visible_to_agent": False,
        },
        "agent": {"model": model, "reasoning_effort": reasoning_effort},
        "judge": {
            "model": JUDGE_MODEL,
            "reasoning_effort": JUDGE_REASONING_EFFORT,
        },
        "point_count": len(points),
        "point_suite_sha256": _suite_digest(points),
        "results": ordered,
        "summary": summarize_baseline_results(ordered),
    }


def _validate_resume(
    payload: dict[str, Any],
    *,
    points: tuple[Point, ...],
    model: str,
    reasoning_effort: str,
) -> None:
    if payload.get("artifact_type") != ARTIFACT_TYPE:
        raise CaseValidationError("cannot resume a different artifact type")
    if payload.get("point_suite_sha256") != _suite_digest(points):
        raise CaseValidationError("cannot resume with a different point suite")
    if payload.get("agent") != {
        "model": model,
        "reasoning_effort": reasoning_effort,
    }:
        raise CaseValidationError("cannot resume with a different agent runtime")
    if payload.get("judge") != {
        "model": JUDGE_MODEL,
        "reasoning_effort": JUDGE_REASONING_EFFORT,
    }:
        raise CaseValidationError("cannot resume with a different Judge runtime")


def _point_identity(point: Point) -> dict[str, str]:
    return {
        "point_id": point.id,
        "point_sha256": _sha256_text(point.source.read_text(encoding="utf-8")),
        "question_sha256": _sha256_text(point.question),
        "ground_truth_sha256": _sha256_text(point.ground_truth),
    }


def _suite_digest(points: tuple[Point, ...]) -> str:
    manifest = "\n".join(
        f"{point.id}:{_point_identity(point)['point_sha256']}"
        for point in sorted(points, key=lambda item: item.id)
    )
    return _sha256_text(manifest)


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _clean_markdown(value: str) -> str:
    return "\n".join(line.rstrip() for line in value.splitlines())


def _parse_events(stdout: str) -> tuple[list[dict[str, Any]], dict[str, int]]:
    events = []
    usage: dict[str, int] = {}
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


def _tool_counts(events: list[dict[str, Any]]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for event in events:
        if event.get("type") != "item.completed":
            continue
        item = event.get("item")
        if not isinstance(item, dict):
            continue
        item_type = str(item.get("type", "unknown"))
        if item_type not in {"agent_message", "reasoning"}:
            counts[item_type] += 1
    return dict(sorted(counts.items()))


def _sum_usage(usages: Any) -> dict[str, int]:
    keys = (
        "input_tokens",
        "cached_input_tokens",
        "cache_write_input_tokens",
        "output_tokens",
        "reasoning_output_tokens",
    )
    items = list(usages)
    return {key: sum(item.get(key, 0) for item in items) for key in keys}


def _read_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise CaseValidationError(f"{path}: invalid baseline artifact: {error}") from error
    if not isinstance(payload, dict):
        raise CaseValidationError(f"{path}: baseline artifact must be an object")
    return payload


def _write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _command_output(command: list[str]) -> str:
    completed = subprocess.run(
        command, text=True, capture_output=True, check=True, timeout=10
    )
    return completed.stdout.strip()

"""Controlled local runners for FinAgentBench model comparisons."""

from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
import time
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from finagentbench.adapter import (
    AdapterError,
    StdioAdapter,
    build_adapter_request,
)
from finagentbench.case import BenchmarkCase
from finagentbench.scoring import score_submission


@dataclass(frozen=True)
class RunSpec:
    model: str
    reasoning_effort: str
    case: BenchmarkCase


def run_codex_matrix(
    cases: tuple[BenchmarkCase, ...],
    *,
    models: tuple[str, ...],
    reasoning_effort: str,
    workers: int,
    timeout_seconds: int,
    progress: Callable[[dict[str, Any]], None] | None = None,
) -> dict[str, Any]:
    specs = [
        RunSpec(model=model, reasoning_effort=reasoning_effort, case=case)
        for model in models
        for case in cases
    ]
    started_at = datetime.now(UTC)
    codex_version = _command_output(["codex", "--version"])
    results: list[dict[str, Any]] = []

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(
                _run_codex_case, spec, timeout_seconds=timeout_seconds
            ): spec
            for spec in specs
        }
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            if progress is not None:
                progress(result)

    results.sort(key=lambda item: (item["model"], item["case_id"]))
    completed_at = datetime.now(UTC)
    return {
        "schema_version": 1,
        "started_at": started_at.isoformat(),
        "completed_at": completed_at.isoformat(),
        "duration_seconds": round((completed_at - started_at).total_seconds(), 3),
        "harness": {
            "name": "codex-cli",
            "version": codex_version,
            "sandbox": "read-only",
            "external_data": False,
            "session_persistence": False,
        },
        "matrix": {
            "models": list(models),
            "reasoning_effort": reasoning_effort,
            "case_count": len(cases),
            "repeats": 1,
            "case_suite_sha256": _case_suite_digest(cases),
        },
        "scoring_contract": {
            "version": 1,
            "prediction_points": 40,
            "premise_points": 25,
            "evidence_f1_points": 25,
            "calibration_points": 10,
        },
        "results": results,
        "summary": summarize_results(results),
    }


def run_adapter_matrix(
    cases: tuple[BenchmarkCase, ...],
    *,
    models: tuple[str, ...],
    reasoning_effort: str,
    workers: int,
    timeout_seconds: int,
    adapter: StdioAdapter,
    progress: Callable[[dict[str, Any]], None] | None = None,
) -> dict[str, Any]:
    """Run public cases through a provider-neutral stdio harness adapter."""
    specs = [
        RunSpec(model=model, reasoning_effort=reasoning_effort, case=case)
        for model in models
        for case in cases
    ]
    started_at = datetime.now(UTC)
    harness = adapter.harness_metadata(external_data=False)
    results: list[dict[str, Any]] = []
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
    results.sort(key=lambda item: (item["model"], item["case_id"]))
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
            "case_suite_sha256": _case_suite_digest(cases),
        },
        "scoring_contract": {
            "version": 1,
            "prediction_points": 40,
            "premise_points": 25,
            "evidence_f1_points": 25,
            "calibration_points": 10,
        },
        "results": results,
        "summary": summarize_results(results),
    }


def summarize_results(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    models = sorted({item["model"] for item in results})
    summaries = []
    for model in models:
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
                "prediction_accuracy": _mean(
                    float(item["prediction_correct"]) for item in scores
                ),
                "premise_accuracy": _mean(
                    float(item["premise_correct"]) for item in scores
                ),
                "mean_evidence_f1": _mean(item["evidence_f1"] for item in scores),
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


def render_markdown_report(run: dict[str, Any]) -> str:
    harness_label = _harness_label(run["harness"])
    lines = [
        "# FinAgentBench public synthetic smoke baseline",
        "",
        (
            f"Harness: `{harness_label}` · effort: "
            f"`{run['matrix']['reasoning_effort']}` · "
            f"cases: {run['matrix']['case_count']} · repeats: {run['matrix']['repeats']}"
        ),
        f"Case suite: `{run['matrix']['case_suite_sha256']}`",
        "",
        "| Model | Score | Prediction | Premise | Evidence F1 | Latency | Failures |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in run["summary"]:
        lines.append(
            "| {model} | {score:.2f} | {prediction:.1%} | {premise:.1%} | "
            "{evidence:.3f} | {latency:.2f}s | {failed} |".format(
                model=item["model"],
                score=item["mean_score"],
                prediction=item["prediction_accuracy"],
                premise=item["premise_accuracy"],
                evidence=item["mean_evidence_f1"],
                latency=item["mean_latency_seconds"],
                failed=item["failed"],
            )
        )

    guardrails = [
        "",
        "## Interpretation guardrails",
        "",
        "- This is one run over public synthetic cases, not a contamination-resistant leaderboard.",
        "- Latency was measured with the configured local concurrency and is not a stable speed ranking.",
        "- The score grades structured conclusions and evidence selection, not private chain of thought.",
    ]
    if run["summary"] and all(
        item["prediction_accuracy"] == 1.0 for item in run["summary"]
    ):
        guardrails.append(
            "- Every model reached 100% prediction accuracy, so the suite has a ceiling effect "
            "and does not yet separate frontier model capability."
        )
    lines.extend(guardrails)

    lines.extend(
        [
            "",
            (
                "The score is a public contract score: prediction 40, premise check 25, "
                "evidence selection F1 25, confidence calibration 10. It does not claim "
                "to measure private chain of thought or replace semantic/human review."
            ),
            "",
            "## Per-case results",
            "",
            "| Model | Case | Score | Prediction | Premise | Evidence F1 | Latency |",
            "| --- | --- | ---: | --- | --- | ---: | ---: |",
        ]
    )
    for item in run["results"]:
        if item["status"] == "completed":
            score = item["score"]
            lines.append(
                f"| {item['model']} | {item['case_id']} | {score['total']:.2f} | "
                f"{'✓' if score['prediction_correct'] else '✗'} | "
                f"{'✓' if score['premise_correct'] else '✗'} | "
                f"{score['evidence_f1']:.3f} | {item['latency_seconds']:.2f}s |"
            )
        else:
            lines.append(
                f"| {item['model']} | {item['case_id']} | — | failed | failed | — | "
                f"{item['latency_seconds']:.2f}s |"
            )
    return "\n".join(lines) + "\n"


def _run_codex_case(spec: RunSpec, *, timeout_seconds: int) -> dict[str, Any]:
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="finagentbench-") as raw_temp_dir:
        temp_dir = Path(raw_temp_dir)
        schema_path = temp_dir / "response-schema.json"
        output_path = temp_dir / "response.json"
        schema_path.write_text(
            json.dumps(spec.case.response_contract, ensure_ascii=False),
            encoding="utf-8",
        )
        prompt = (
            "You are being evaluated on a point-in-time financial prediction case. "
            "Use only the supplied evidence. Do not browse, inspect files, or use external "
            "knowledge to add facts. Return only one JSON object conforming to the response "
            "contract. evidence_ids must contain only the evidence that materially supports "
            "your conclusion; do not select every item by default.\n\n"
            + json.dumps(spec.case.agent_payload(), ensure_ascii=False, indent=2)
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
            str(temp_dir),
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
            return _failure_result(
                spec,
                started=started,
                error=f"timeout after {timeout_seconds}s",
                stdout=error.stdout or "",
            )

        latency = round(time.monotonic() - started, 3)
        events, usage = _parse_events(completed.stdout)
        if completed.returncode != 0:
            stderr = completed.stderr
            return _failure_result(
                spec,
                started=started,
                error=(
                    f"codex exited {completed.returncode}:\n"
                    f"{stderr[:2000]}\n... stderr tail ...\n{stderr[-2000:]}"
                ),
                stdout=completed.stdout,
            )
        try:
            submission = json.loads(output_path.read_text(encoding="utf-8"))
            score = score_submission(spec.case, submission)
        except (OSError, json.JSONDecodeError, ValueError) as error:
            return _failure_result(
                spec,
                started=started,
                error=f"invalid model response: {error}",
                stdout=completed.stdout,
            )

        return {
            "case_id": spec.case.id,
            "case_sha256": _case_digest(spec.case),
            "model": spec.model,
            "reasoning_effort": spec.reasoning_effort,
            "status": "completed",
            "latency_seconds": latency,
            "submission": submission,
            "score": score.to_dict(),
            "usage": usage,
            "event_count": len(events),
        }


def _run_adapter_case(
    spec: RunSpec,
    *,
    adapter: StdioAdapter,
    timeout_seconds: int,
) -> dict[str, Any]:
    started = time.monotonic()
    prompt = (
        "You are being evaluated on a point-in-time financial prediction case. "
        "Use only the supplied evidence. Do not browse, inspect files, or use external "
        "knowledge to add facts. Return only one JSON object conforming to the response "
        "contract. evidence_ids must contain only the evidence that materially supports "
        "your conclusion; do not select every item by default.\n\n"
        + json.dumps(spec.case.agent_payload(), ensure_ascii=False, indent=2)
    )
    request = build_adapter_request(
        task="synthetic",
        model=spec.model,
        reasoning_effort=spec.reasoning_effort,
        prompt=prompt,
        response_contract=spec.case.response_contract,
    )
    with tempfile.TemporaryDirectory(prefix="finagentbench-adapter-") as raw_dir:
        try:
            output = adapter.run(
                request,
                directory=Path(raw_dir),
                timeout_seconds=timeout_seconds,
            )
            score = score_submission(spec.case, output.submission)
        except (AdapterError, ValueError) as error:
            return {
                "case_id": spec.case.id,
                "case_sha256": _case_digest(spec.case),
                "model": spec.model,
                "reasoning_effort": spec.reasoning_effort,
                "status": "failed",
                "latency_seconds": round(time.monotonic() - started, 3),
                "error": str(error),
                "usage": {},
            }
    result = {
        "case_id": spec.case.id,
        "case_sha256": _case_digest(spec.case),
        "model": spec.model,
        "reasoning_effort": spec.reasoning_effort,
        "status": "completed",
        "latency_seconds": round(time.monotonic() - started, 3),
        "submission": output.submission,
        "score": score.to_dict(),
        "usage": output.usage,
        "event_count": len(output.events),
    }
    if output.metadata:
        result["adapter_metadata"] = output.metadata
    return result


def _failure_result(
    spec: RunSpec, *, started: float, error: str, stdout: str | bytes
) -> dict[str, Any]:
    if isinstance(stdout, bytes):
        stdout = stdout.decode("utf-8", errors="replace")
    events, usage = _parse_events(stdout)
    return {
        "case_id": spec.case.id,
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


def _usage_totals(usage: dict[str, int]) -> dict[str, int]:
    return {
        "input_tokens": usage.get("input_tokens", 0),
        "cached_input_tokens": usage.get("cached_input_tokens", 0),
        "output_tokens": usage.get("output_tokens", 0),
    }


def _mean(values: Any) -> float:
    items = list(values)
    if not items:
        return 0.0
    return round(sum(items) / len(items), 4)


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


def _case_digest(case: BenchmarkCase) -> str:
    payload = {
        "agent_payload": case.agent_payload(),
        "answer_key": {
            "prediction": case.answer_key.prediction,
            "premise_assessment": case.answer_key.premise_assessment,
            "evidence_ids": list(case.answer_key.evidence_ids),
        },
        "rubric": [
            {
                "id": item.id,
                "description": item.description,
                "weight": item.weight,
            }
            for item in case.rubric
        ],
    }
    encoded = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _case_suite_digest(cases: tuple[BenchmarkCase, ...]) -> str:
    manifest = "\n".join(
        f"{case.id}:{_case_digest(case)}"
        for case in sorted(cases, key=lambda item: item.id)
    )
    return hashlib.sha256(manifest.encode("utf-8")).hexdigest()

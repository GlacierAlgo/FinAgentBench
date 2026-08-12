"""Build the public development radar from committed benchmark artifacts."""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from pathlib import Path
from statistics import fmean
from typing import Any

from finagentbench.case import CaseValidationError


def build_radar_data(repo_root: Path, manifest_path: Path) -> dict[str, Any]:
    """Normalize committed A-share replays into a compact static-site payload."""
    root = repo_root.resolve()
    manifest = _read_object(manifest_path)
    if manifest.get("schema_version") != 1:
        raise CaseValidationError("radar source manifest schema_version must be 1")
    suites = manifest.get("suites")
    if not isinstance(suites, list) or not suites:
        raise CaseValidationError("radar source manifest requires suites")
    family_labels = manifest.get("family_labels")
    if not isinstance(family_labels, dict):
        raise CaseValidationError("radar source manifest requires family_labels")

    scenarios = _load_objects(root / "src/finagentbench/a_share/scenarios")
    labels = _load_objects(root / "src/finagentbench/a_share/labels")
    cases: dict[str, dict[str, Any]] = {}
    experiment_suites = []
    model_order: list[str] = []
    result_count = 0

    for suite_source in suites:
        suite_id, suite_title, result_path = _suite_source(suite_source, root=root)
        artifact = _read_object(result_path)
        harness = _object(artifact.get("harness"), field=f"{suite_id}.harness")
        matrix = _object(artifact.get("matrix"), field=f"{suite_id}.matrix")
        if harness.get("outcome_visible_to_agent") is not False:
            raise CaseValidationError(f"{suite_id}: outcome must be hidden from agent")
        suite_models = matrix.get("models")
        if not isinstance(suite_models, list) or not suite_models:
            raise CaseValidationError(f"{suite_id}: matrix.models must be a list")
        for model in suite_models:
            if not isinstance(model, str) or not model:
                raise CaseValidationError(f"{suite_id}: invalid model ID")
            if model not in model_order:
                model_order.append(model)

        results = artifact.get("results")
        if not isinstance(results, list):
            raise CaseValidationError(f"{suite_id}: results must be a list")
        scenario_ids = {
            item.get("scenario_id") for item in results if isinstance(item, dict)
        }
        if None in scenario_ids or len(scenario_ids) != matrix.get("case_count"):
            raise CaseValidationError(f"{suite_id}: result case count mismatch")
        expected_results = len(scenario_ids) * len(suite_models) * matrix.get(
            "repeats", 1
        )
        if len(results) != expected_results:
            raise CaseValidationError(f"{suite_id}: result matrix is incomplete")

        seen_runs = set()
        for raw_result in results:
            result = _object(raw_result, field=f"{suite_id}.result")
            scenario_id = _string(result.get("scenario_id"), field="scenario_id")
            model = _string(result.get("model"), field="model")
            repeat_index = result.get("repeat_index", 1)
            identity = (scenario_id, model, repeat_index)
            if identity in seen_runs:
                raise CaseValidationError(f"{suite_id}: duplicate run {identity}")
            seen_runs.add(identity)
            scenario = scenarios.get(scenario_id)
            label = labels.get(scenario_id)
            if scenario is None or label is None:
                raise CaseValidationError(f"{suite_id}: missing case {scenario_id}")
            existing = cases.get(scenario_id)
            if existing is not None and existing["suite_id"] != suite_id:
                raise CaseValidationError(
                    f"radar scenario appears in multiple suites: {scenario_id}"
                )
            if existing is None:
                target = _object(scenario.get("target"), field=f"{scenario_id}.target")
                event = _string(target.get("event"), field=f"{scenario_id}.event")
                security = _object(
                    scenario.get("security"), field=f"{scenario_id}.security"
                )
                family = _family_for(event, family_labels=family_labels)
                existing = {
                    "id": scenario_id,
                    "suite_id": suite_id,
                    "suite_title": suite_title,
                    "family": family[0],
                    "family_label": family[1],
                    "company": _string(
                        security.get("name_as_of"), field=f"{scenario_id}.company"
                    ),
                    "ticker": _string(
                        security.get("ticker"), field=f"{scenario_id}.ticker"
                    ),
                    "as_of": _string(scenario.get("as_of"), field="as_of"),
                    "window_end": _string(
                        _object(
                            scenario.get("prediction_window"),
                            field=f"{scenario_id}.prediction_window",
                        ).get("end"),
                        field="window_end",
                    ),
                    "event": event,
                    "target_definition": _string(
                        target.get("definition"), field=f"{scenario_id}.definition"
                    ),
                    "outcome": _boolean(
                        label.get("event_occurred"), field=f"{scenario_id}.outcome"
                    ),
                    "runs": [],
                }
                cases[scenario_id] = existing
            existing["runs"].append(_normalize_run(result, repeat_index=repeat_index))
            result_count += 1

        relative_result_path = result_path.relative_to(root).as_posix()
        experiment_suites.append(
            {
                "id": suite_id,
                "title": suite_title,
                "case_count": len(scenario_ids),
                "result_path": relative_result_path,
                "result_sha256": _file_sha256(result_path),
                "case_suite_sha256": matrix.get("case_suite_sha256"),
                "reasoning_effort": matrix.get("reasoning_effort"),
                "repeats": matrix.get("repeats", 1),
                "harness": harness,
                "completed_at": artifact.get("completed_at"),
            }
        )

    case_list = sorted(cases.values(), key=lambda item: (item["as_of"], item["id"]))
    for case in case_list:
        case["runs"].sort(
            key=lambda item: (model_order.index(item["model"]), item["repeat_index"])
        )
    summaries = _summaries(case_list, model_order=model_order)
    event_count = sum(case["outcome"] for case in case_list)
    record = {
        "schema_version": 1,
        "artifact_type": "finagentbench_public_radar",
        "tier": "development_diagnostics",
        "title": _string(manifest.get("title"), field="title"),
        "subtitle": _string(manifest.get("subtitle"), field="subtitle"),
        "source_completed_at": max(
            suite["completed_at"] for suite in experiment_suites
        ),
        "coverage": {
            "case_count": len(case_list),
            "event_count": event_count,
            "no_event_count": len(case_list) - event_count,
            "model_count": len(model_order),
            "attempt_count": result_count,
            "sealed_eligible_suite_count": 0,
        },
        "leaderboard": {
            "status": "not_yet_eligible",
            "eligible_suite_count": 0,
            "reason": (
                "No matured pre-registered sealed hard-case suite exists yet. "
                "These public historical replays are development diagnostics."
            ),
        },
        "models": model_order,
        "experiment_suites": experiment_suites,
        "model_summaries": summaries["models"],
        "suite_summaries": summaries["suites"],
        "family_summaries": summaries["families"],
        "cases": case_list,
        "methodology": manifest.get("methodology", []),
    }
    record["data_sha256"] = _digest(record)
    return record


def render_radar_data_js(payload: dict[str, Any]) -> str:
    """Return an offline-friendly JavaScript assignment."""
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return f"window.FINAGENTBENCH_RADAR_DATA={encoded};\n"


def _summaries(cases: list[dict[str, Any]], *, model_order: list[str]) -> dict[str, Any]:
    model_runs: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    suite_runs: defaultdict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    family_runs: defaultdict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    suite_titles: dict[str, str] = {}
    family_labels: dict[str, str] = {}
    for case in cases:
        suite_titles[case["suite_id"]] = case["suite_title"]
        family_labels[case["family"]] = case["family_label"]
        for run in case["runs"]:
            model_runs[run["model"]].append(run)
            suite_runs[(case["suite_id"], run["model"])].append(run)
            family_runs[(case["family"], run["model"])].append(run)

    return {
        "models": [
            {"model": model, **_run_summary(model_runs[model])}
            for model in model_order
        ],
        "suites": [
            {
                "suite_id": suite_id,
                "suite_title": suite_titles[suite_id],
                "model": model,
                **_run_summary(suite_runs[(suite_id, model)]),
            }
            for suite_id in suite_titles
            for model in model_order
        ],
        "families": [
            {
                "family": family,
                "family_label": family_labels[family],
                "model": model,
                **_run_summary(family_runs[(family, model)]),
            }
            for family in family_labels
            for model in model_order
        ],
    }


def _run_summary(runs: list[dict[str, Any]]) -> dict[str, Any]:
    completed = [run for run in runs if run["status"] == "completed"]
    if not completed:
        return {
            "attempt_count": len(runs),
            "completed_count": 0,
            "mean_brier_loss": None,
            "mean_log_loss": None,
            "accuracy": None,
            "mean_search_calls": None,
            "search_coverage": 0,
            "mean_latency_seconds": None,
            "total_input_tokens": 0,
            "total_output_tokens": 0,
        }
    return {
        "attempt_count": len(runs),
        "completed_count": len(completed),
        "mean_brier_loss": _mean(completed, "brier_loss"),
        "mean_log_loss": _mean(completed, "log_loss"),
        "accuracy": round(fmean(run["classification_correct"] for run in completed), 6),
        "mean_search_calls": _mean(completed, "search_calls"),
        "search_coverage": round(
            fmean(run["search_calls"] > 0 for run in completed), 6
        ),
        "mean_latency_seconds": _mean(completed, "latency_seconds"),
        "total_input_tokens": sum(run["input_tokens"] for run in completed),
        "total_output_tokens": sum(run["output_tokens"] for run in completed),
    }


def _normalize_run(result: dict[str, Any], *, repeat_index: Any) -> dict[str, Any]:
    model = _string(result.get("model"), field="result.model")
    status = result.get("status")
    if status not in {"completed", "failed"}:
        raise CaseValidationError(f"{model}: unsupported result status")
    if not isinstance(repeat_index, int) or isinstance(repeat_index, bool):
        raise CaseValidationError(f"{model}: repeat_index must be an integer")
    normalized: dict[str, Any] = {
        "model": model,
        "repeat_index": repeat_index,
        "status": status,
        "search_calls": _nonnegative_number(
            result.get("search_calls", 0), field=f"{model}.search_calls"
        ),
        "latency_seconds": _nonnegative_number(
            result.get("latency_seconds", 0), field=f"{model}.latency_seconds"
        ),
    }
    if status == "failed":
        normalized["error"] = str(result.get("error", "unknown failure"))
        return normalized
    submission = _object(result.get("submission"), field=f"{model}.submission")
    score = _object(result.get("score"), field=f"{model}.score")
    usage = _object(result.get("usage", {}), field=f"{model}.usage")
    normalized.update(
        {
            "event_probability": _probability(
                submission.get("event_probability"), field=f"{model}.probability"
            ),
            "prediction": submission.get("prediction"),
            "brier_loss": _nonnegative_number(
                score.get("brier_loss"), field=f"{model}.brier_loss"
            ),
            "log_loss": _nonnegative_number(
                score.get("log_loss"), field=f"{model}.log_loss"
            ),
            "classification_correct": _boolean(
                score.get("classification_correct"), field=f"{model}.correct"
            ),
            "evidence_f1": _probability(
                score.get("evidence_f1"), field=f"{model}.evidence_f1"
            ),
            "input_tokens": _nonnegative_int(
                usage.get("input_tokens", 0), field=f"{model}.input_tokens"
            ),
            "output_tokens": _nonnegative_int(
                usage.get("output_tokens", 0), field=f"{model}.output_tokens"
            ),
        }
    )
    return normalized


def _suite_source(value: Any, *, root: Path) -> tuple[str, str, Path]:
    source = _object(value, field="suite")
    suite_id = _string(source.get("id"), field="suite.id")
    title = _string(source.get("title"), field=f"{suite_id}.title")
    relative = Path(_string(source.get("result_path"), field=f"{suite_id}.result_path"))
    path = (root / relative).resolve()
    if root not in path.parents:
        raise CaseValidationError(f"{suite_id}: result_path escapes repository")
    return suite_id, title, path


def _family_for(event: str, *, family_labels: dict[str, Any]) -> tuple[str, str]:
    for family, source in family_labels.items():
        item = _object(source, field=f"family_labels.{family}")
        events = item.get("events")
        if isinstance(events, list) and event in events:
            return family, _string(item.get("label"), field=f"{family}.label")
    raise CaseValidationError(f"radar family missing for event: {event}")


def _load_objects(directory: Path) -> dict[str, dict[str, Any]]:
    objects = {}
    for path in sorted(directory.glob("*.json")):
        payload = _read_object(path)
        object_id = _string(
            payload.get("id", payload.get("scenario_id")), field=f"{path}.id"
        )
        if object_id in objects:
            raise CaseValidationError(f"duplicate JSON object ID: {object_id}")
        objects[object_id] = payload
    return objects


def _read_object(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise CaseValidationError(f"cannot read radar source {path}: {error}") from error
    return _object(payload, field=str(path))


def _file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _digest(payload: Any) -> str:
    encoded = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _mean(items: list[dict[str, Any]], key: str) -> float:
    return round(fmean(float(item[key]) for item in items), 6)


def _object(value: Any, *, field: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise CaseValidationError(f"radar {field} must be an object")
    return value


def _string(value: Any, *, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CaseValidationError(f"radar {field} must be a non-empty string")
    return value.strip()


def _boolean(value: Any, *, field: str) -> bool:
    if not isinstance(value, bool):
        raise CaseValidationError(f"radar {field} must be a boolean")
    return value


def _nonnegative_int(value: Any, *, field: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise CaseValidationError(f"radar {field} must be a non-negative integer")
    return value


def _nonnegative_number(value: Any, *, field: str) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
        raise CaseValidationError(f"radar {field} must be non-negative")
    return float(value)


def _probability(value: Any, *, field: str) -> float:
    number = _nonnegative_number(value, field=field)
    if number > 1:
        raise CaseValidationError(f"radar {field} must be between zero and one")
    return number

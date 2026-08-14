from copy import deepcopy
from datetime import UTC, datetime

import pytest

from pitfall.case import CaseValidationError
from pitfall.live_shadow import (
    _digest,
    run_live_shadow_codex_matrix,
    verify_live_shadow_seal,
)
from pitfall.sealed_suite import (
    finalize_suite,
    preregister_suite,
    verify_finalized_suite,
    verify_public_plan_commitment,
    verify_suite_plan,
)
from pitfall.walkforward import WalkForwardScenario


def _scenario(index: int) -> dict:
    ticker = f"60{index:04d}"
    return {
        "schema_version": 2,
        "id": f"cn-a-live-suite-{index}",
        "suite": "a_share_live_shadow_hard_v1",
        "mode": "live_shadow",
        "security": {
            "order_book_id": f"{ticker}.XSHG",
            "ticker": ticker,
            "name_as_of": f"测试公司{index}",
            "exchange": "SSE",
        },
        "as_of": "2026-08-12",
        "prediction_window": {
            "end": "2027-04-30",
            "description": "截至2026年年度报告披露",
        },
        "target": {
            "event": "commercial_validation",
            "definition": "下一年度收入继续兑现",
            "criteria_mode": "all",
            "criteria": [
                {
                    "metric": "revenue_growth",
                    "comparison": ">=",
                    "value": 0.2,
                    "description": "收入增长至少20%",
                }
            ],
        },
        "prompt": "使用实时网络证据预测下一年度商业兑现。",
        "search_policy": {
            "mode": "live_web",
            "latest_published_at": "2026-08-12",
            "allowed_domains": ["sse.com.cn"],
        },
        "response_contract": {
            "type": "object",
            "required": [
                "event_probability",
                "prediction",
                "evidence_urls",
                "analysis_summary",
            ],
            "properties": {
                "event_probability": {
                    "type": "number",
                    "minimum": 0,
                    "maximum": 1,
                },
                "prediction": {
                    "type": "string",
                    "enum": ["event", "no_event"],
                },
                "evidence_urls": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "analysis_summary": {"type": "string", "minLength": 1},
            },
            "additionalProperties": False,
        },
        "authoring_provenance": {"status": "unresolved_live_shadow"},
    }


def _suite_source() -> dict:
    families = ["rd", "rd", "factory", "factory", "cash", "cash"]
    return {
        "schema_version": 1,
        "suite_id": "a-share-shadow-hard-2026",
        "policy": {
            "required_models": ["model-a", "model-b"],
            "reasoning_effort": "low",
            "repeats": 3,
            "required_web_search_calls": 1,
            "minimum_case_count": 6,
            "minimum_family_count": 3,
            "minimum_cases_per_family": 2,
            "primary_metric": "mean_brier_loss",
        },
        "cases": [
            {
                "slot_id": f"slot-{index}",
                "family": family,
                "scenario": _scenario(index),
            }
            for index, family in enumerate(families, start=1)
        ],
    }


def _completed_run(model: str, effort: str) -> dict:
    events = [
        {
            "type": "item.completed",
            "item": {"type": "web_search", "query": "公司 年报 研发"},
        }
    ]
    return {
        "model": model,
        "reasoning_effort": effort,
        "status": "completed",
        "executed_at": "2026-08-12T02:00:00+00:00",
        "latency_seconds": 1.0,
        "web_search_calls": 1,
        "submission": {
            "event_probability": 0.7,
            "prediction": "event",
            "evidence_urls": ["https://www.sse.com.cn/example"],
            "analysis_summary": "证据支持增长，但不是因果证明。",
        },
        "events": events,
        "events_sha256": _digest(events),
        "usage": {},
    }


def _seal(scenario_source: dict, monkeypatch, *, models=None) -> dict:
    scenario = WalkForwardScenario.from_dict(scenario_source)
    monkeypatch.setattr(
        "pitfall.live_shadow._command_output",
        lambda command: "codex test",
    )
    monkeypatch.setattr(
        "pitfall.live_shadow._run_case",
        lambda scenario, model, reasoning_effort, timeout_seconds: _completed_run(
            model, reasoning_effort
        ),
    )
    return run_live_shadow_codex_matrix(
        scenario_source,
        scenario,
        models=models or ("model-a", "model-b"),
        reasoning_effort="low",
        workers=2,
        timeout_seconds=30,
        repeats=3,
        now=datetime(2026, 8, 12, 2, tzinfo=UTC),
    )


def test_suite_preregistration_hides_scenarios_in_public_commitment() -> None:
    plan, public = preregister_suite(
        _suite_source(),
        now=datetime(2026, 8, 11, 2, tzinfo=UTC),
    )

    assert verify_suite_plan(plan) == plan["commitment"]["payload_sha256"]
    assert (
        verify_public_plan_commitment(public) == public["commitment"]["payload_sha256"]
    )
    rendered = str(public)
    assert "scenario_source" not in rendered
    assert "cn-a-live-suite-1" not in rendered
    assert public["case_count"] == 6
    assert public["family_counts"] == {"cash": 2, "factory": 2, "rd": 2}

    tampered = deepcopy(public)
    tampered["case_count"] = 7
    with pytest.raises(CaseValidationError, match="commitment digest mismatch"):
        verify_public_plan_commitment(tampered)


def test_live_shadow_repeats_are_bound_into_the_seal(monkeypatch) -> None:
    seal = _seal(_scenario(1), monkeypatch)

    assert seal["matrix"]["repeats"] == 3
    assert len(seal["results"]) == 6
    assert [(item["model"], item["repeat_index"]) for item in seal["results"]] == [
        ("model-a", 1),
        ("model-a", 2),
        ("model-a", 3),
        ("model-b", 1),
        ("model-b", 2),
        ("model-b", 3),
    ]
    assert verify_live_shadow_seal(seal) == seal["commitment"]["payload_sha256"]


def test_finalize_suite_rejects_cherry_picking_and_wrong_matrix(monkeypatch) -> None:
    source = _suite_source()
    plan, public = preregister_suite(
        source,
        now=datetime(2026, 8, 11, 2, tzinfo=UTC),
    )
    seals = [_seal(item["scenario"], monkeypatch) for item in source["cases"]]

    with pytest.raises(CaseValidationError, match="exactly one seal per slot"):
        finalize_suite(plan, public, seals[:-1])

    wrong_matrix = _seal(
        source["cases"][0]["scenario"],
        monkeypatch,
        models=("model-a", "model-c"),
    )
    with pytest.raises(CaseValidationError, match="model matrix"):
        finalize_suite(plan, public, [wrong_matrix, *seals[1:]])

    wrong_effort = deepcopy(seals[0])
    wrong_effort["results"][0]["reasoning_effort"] = "high"
    unsigned = {
        key: value for key, value in wrong_effort.items() if key != "commitment"
    }
    wrong_effort["commitment"]["payload_sha256"] = _digest(unsigned)
    with pytest.raises(CaseValidationError, match="attempt reasoning effort"):
        finalize_suite(plan, public, [wrong_effort, *seals[1:]])

    suite = finalize_suite(
        plan,
        public,
        seals,
        now=datetime(2026, 8, 12, 4, tzinfo=UTC),
    )

    assert len(suite["members"]) == 6
    assert all(item["attempt_count"] == 6 for item in suite["members"])
    assert suite["outcome_status"] == "unresolved"
    assert verify_finalized_suite(suite) == suite["commitment"]["payload_sha256"]

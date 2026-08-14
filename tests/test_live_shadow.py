from copy import deepcopy
from datetime import UTC, date, datetime

import pytest

from pitfall.errors import CaseValidationError
from pitfall.live_shadow import (
    LABEL_TYPE,
    _digest,
    resolve_live_shadow_seal,
    run_live_shadow_codex_matrix,
    verify_live_shadow_resolution,
    verify_live_shadow_seal,
)
from pitfall.walkforward import WalkForwardScenario


def _scenario_payload() -> dict:
    return {
        "schema_version": 2,
        "id": "cn-a-live-shadow-test",
        "suite": "a_share_live_shadow_v1",
        "mode": "live_shadow",
        "security": {
            "order_book_id": "688041.XSHG",
            "ticker": "688041",
            "name_as_of": "海光信息",
            "exchange": "SSE",
        },
        "as_of": "2026-08-12",
        "prediction_window": {
            "end": "2027-04-30",
            "description": "截至2026年年报披露",
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
        "prompt": "使用实时网络证据预测海光信息下一年度商业兑现。",
        "search_policy": {
            "mode": "live_web",
            "latest_published_at": "2026-08-12",
            "allowed_domains": ["sse.com.cn", "cninfo.com.cn"],
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


def _completed_run(model: str, effort: str) -> dict:
    events = [
        {
            "type": "item.completed",
            "item": {"type": "web_search", "query": "海光信息 研发"},
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
            "analysis_summary": "产品与订单证据支持增长，但不是因果证明。",
        },
        "events": events,
        "events_sha256": _digest(events),
        "usage": {},
    }


def test_live_shadow_seal_binds_scenario_submission_and_trace(monkeypatch) -> None:
    source = _scenario_payload()
    scenario = WalkForwardScenario.from_dict(source)
    monkeypatch.setattr(
        "pitfall.live_shadow._command_output", lambda command: "codex test"
    )
    monkeypatch.setattr(
        "pitfall.live_shadow._run_case",
        lambda scenario, model, reasoning_effort, timeout_seconds: _completed_run(
            model, reasoning_effort
        ),
    )

    seal = run_live_shadow_codex_matrix(
        source,
        scenario,
        models=("model-a",),
        reasoning_effort="low",
        workers=1,
        timeout_seconds=30,
        now=datetime(2026, 8, 12, 2, tzinfo=UTC),
    )

    assert verify_live_shadow_seal(seal) == seal["commitment"]["payload_sha256"]
    assert seal["agent_payload"]["search_tool"]["name"] == "live_web_search"
    assert "evidence_urls" in seal["agent_payload"]["response_contract"]["required"]

    tampered = deepcopy(seal)
    tampered["results"][0]["submission"]["event_probability"] = 0.9
    with pytest.raises(CaseValidationError, match="commitment digest mismatch"):
        verify_live_shadow_seal(tampered)


def test_live_shadow_resolution_scores_only_after_maturity(monkeypatch) -> None:
    source = _scenario_payload()
    scenario = WalkForwardScenario.from_dict(source)
    monkeypatch.setattr(
        "pitfall.live_shadow._command_output", lambda command: "codex test"
    )
    monkeypatch.setattr(
        "pitfall.live_shadow._run_case",
        lambda scenario, model, reasoning_effort, timeout_seconds: _completed_run(
            model, reasoning_effort
        ),
    )
    seal = run_live_shadow_codex_matrix(
        source,
        scenario,
        models=("model-a",),
        reasoning_effort="low",
        workers=1,
        timeout_seconds=30,
        now=datetime(2026, 8, 12, 2, tzinfo=UTC),
    )
    label = {
        "schema_version": 1,
        "artifact_type": LABEL_TYPE,
        "scenario_id": scenario.id,
        "resolved_at": "2027-03-01",
        "event_occurred": True,
        "realized": {
            "observations": {"revenue_start": 100.0, "revenue_end": 130.0},
            "derivations": [
                {
                    "metric": "revenue_growth",
                    "operation": "pct_change",
                    "inputs": ["revenue_start", "revenue_end"],
                    "value": 0.3,
                }
            ],
        },
        "outcome_sources": [
            {
                "title": "年度报告",
                "published_at": "2027-03-01",
                "url": "https://www.sse.com.cn/outcome.pdf",
            }
        ],
    }

    with pytest.raises(CaseValidationError, match="cannot resolve in the future"):
        resolve_live_shadow_seal(seal, label, today=date(2027, 2, 28))

    resolution = resolve_live_shadow_seal(seal, label, today=date(2027, 3, 1))

    assert resolution["results"][0]["score"]["brier_loss"] == 0.09
    assert resolution["results"][0]["score"]["classification_correct"]
    assert (
        verify_live_shadow_resolution(resolution)
        == resolution["commitment"]["payload_sha256"]
    )


def test_live_web_run_rejects_backdated_scenario() -> None:
    source = _scenario_payload()
    scenario = WalkForwardScenario.from_dict(source)

    with pytest.raises(CaseValidationError, match="executed on the scenario as_of"):
        run_live_shadow_codex_matrix(
            source,
            scenario,
            models=("model-a",),
            reasoning_effort="low",
            workers=1,
            timeout_seconds=30,
            now=datetime(2026, 8, 13, 2, tzinfo=UTC),
        )

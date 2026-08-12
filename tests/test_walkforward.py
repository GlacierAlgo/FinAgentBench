import json

import pytest

from finagentbench.case import CaseValidationError
from finagentbench.cli import (
    BUILTIN_A_SHARE_CORPORA,
    BUILTIN_A_SHARE_LABELS,
    BUILTIN_A_SHARE_SCENARIOS,
)
from finagentbench.walkforward import (
    FrozenCorpus,
    load_walkforward_suite,
    score_walkforward_submission,
)
from finagentbench.walkforward_runner import (
    _search_call_count,
    render_walkforward_report,
    summarize_walkforward_results,
)


def _cases():
    return load_walkforward_suite(
        BUILTIN_A_SHARE_SCENARIOS,
        BUILTIN_A_SHARE_CORPORA,
        BUILTIN_A_SHARE_LABELS,
    )


def test_builtin_a_share_suite_is_balanced_and_point_in_time() -> None:
    cases = _cases()

    assert len(cases) == 6
    assert sum(case.label.event_occurred for case in cases) == 3
    for case in cases:
        assert all(
            document.published_at <= case.scenario.as_of
            for document in case.corpus.documents
        )


def test_agent_payload_does_not_expose_outcome_or_rqdata_provenance() -> None:
    rendered = json.dumps(_cases()[0].scenario.agent_payload(), ensure_ascii=False)

    assert "event_occurred" not in rendered
    assert "resolved_at" not in rendered
    assert "asset_impairment_loss" not in rendered
    assert "download_rqdata" not in rendered


def test_frozen_search_finds_relevant_pre_as_of_filings() -> None:
    case = next(
        item
        for item in _cases()
        if item.scenario.security.order_book_id == "300467.XSHE"
    )

    results = case.corpus.search("商誉 减值 狮之吼")

    assert results[0]["id"] == "h1-goodwill-note"
    assert all(item["published_at"] <= "2019-10-30" for item in results)


def test_future_document_is_rejected_from_historical_corpus() -> None:
    case = _cases()[0]
    payload = {
        "schema_version": 1,
        "scenario_id": case.scenario.id,
        "documents": [
            {
                "id": "leak",
                "title": "Future annual report",
                "published_at": "2020-04-30",
                "source": "test",
                "url": "https://static.cninfo.com.cn/future.pdf",
                "content": "This reveals the outcome.",
            }
        ],
    }

    with pytest.raises(CaseValidationError, match="leaks past search cutoff"):
        FrozenCorpus.from_dict(payload, scenario=case.scenario)


def test_probability_scoring_rewards_calibrated_confidence() -> None:
    case = next(item for item in _cases() if item.label.event_occurred)
    common = {
        "prediction": "event",
        "evidence_ids": list(case.label.expected_evidence_ids),
        "analysis_summary": "The frozen filings support a material impairment risk.",
    }

    high = score_walkforward_submission(
        case, {**common, "event_probability": 0.9}
    )
    low = score_walkforward_submission(
        case, {**common, "event_probability": 0.6}
    )

    assert high.total > low.total
    assert high.brier_loss < low.brier_loss


def test_perfect_no_event_prediction_scores_100() -> None:
    case = next(item for item in _cases() if not item.label.event_occurred)
    result = score_walkforward_submission(
        case,
        {
            "event_probability": 0.0,
            "prediction": "no_event",
            "evidence_ids": list(case.label.expected_evidence_ids),
            "analysis_summary": "High goodwill alone is not a sufficient trigger.",
        },
    )

    assert result.total == 100
    assert result.classification_correct


def test_walkforward_summary_and_report_include_probability_metrics() -> None:
    result = {
        "model": "model-a",
        "scenario_id": "scenario-a",
        "status": "completed",
        "latency_seconds": 2.0,
        "search_calls": 1,
        "submission": {"event_probability": 0.8},
        "outcome": True,
        "score": {
            "total": 96.6,
            "brier_loss": 0.04,
            "log_loss": 0.2231,
            "classification_correct": True,
            "evidence_f1": 1.0,
        },
        "usage": {},
    }
    summary = summarize_walkforward_results([result])
    run = {
        "harness": {"version": "codex-cli test"},
        "matrix": {
            "reasoning_effort": "low",
            "case_count": 1,
            "repeats": 1,
            "case_suite_sha256": "abc123",
        },
        "summary": summary,
        "results": [result],
    }

    assert summary[0]["mean_brier_loss"] == 0.04
    assert summary[0]["search_usage_rate"] == 1.0
    assert "Brier loss" in render_walkforward_report(run)


def test_search_calls_count_only_completed_commands() -> None:
    item = {
        "type": "command_execution",
        "command": "python3 frozen_search.py '商誉 减值'",
    }
    events = [
        {"type": "item.started", "item": item},
        {"type": "item.completed", "item": item},
        {"type": "item.completed", "item": {"type": "agent_message"}},
    ]

    assert _search_call_count(events) == 1

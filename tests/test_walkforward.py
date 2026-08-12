import json
from copy import deepcopy

import pytest

from finagentbench.case import CaseValidationError
from finagentbench.cli import (
    BUILTIN_A_SHARE_CORPORA,
    BUILTIN_A_SHARE_LABELS,
    BUILTIN_A_SHARE_SCENARIOS,
)
from finagentbench.walkforward import (
    FrozenCorpus,
    WalkForwardLabel,
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


def test_builtin_goodwill_slice_is_balanced_and_all_cases_are_point_in_time() -> None:
    cases = _cases()
    goodwill_cases = tuple(
        case
        for case in cases
        if case.scenario.suite == "a_share_walk_forward_v1"
    )

    assert len(cases) >= 24
    assert len(goodwill_cases) == 6
    assert sum(case.label.event_occurred for case in goodwill_cases) == 3
    for case in cases:
        assert all(
            document.published_at <= case.scenario.as_of
            for document in case.corpus.documents
        )


def test_a_share_trap_families_have_matched_positive_and_negative_cases() -> None:
    trap_cases = tuple(
        case for case in _cases() if case.scenario.suite == "a_share_traps_v1"
    )
    families = {
        "st_transition": tuple(
            case for case in trap_cases if "st-transition" in case.scenario.id
        ),
        "receivables": tuple(
            case for case in trap_cases if "receivables" in case.scenario.id
        ),
        "inventory": tuple(
            case for case in trap_cases if "inventory" in case.scenario.id
        ),
        "audit_opinion": tuple(
            case for case in trap_cases if "audit-opinion" in case.scenario.id
        ),
        "performance_commitment": tuple(
            case
            for case in trap_cases
            if "performance-commitment" in case.scenario.id
        ),
        "pledge_control": tuple(
            case for case in trap_cases if "pledge-control" in case.scenario.id
        ),
        "pledge_freeze": tuple(
            case for case in trap_cases if "pledge-freeze" in case.scenario.id
        ),
    }

    assert len(trap_cases) >= 14
    for cases in families.values():
        assert len(cases) == 2
        assert {case.label.event_occurred for case in cases} == {False, True}
        assert all(
            "run-llama/liteparse 2.11.1 git 53e4fc8"
            in case.scenario.authoring_provenance["pdf_text_tool"]
            for case in cases
        )


def test_generic_derivation_chain_recomputes_incremental_credit_impairment() -> None:
    case = next(
        item
        for item in _cases()
        if item.scenario.id == "cn-a-2019q3-receivables-300461"
    )

    assert case.label.event_occurred
    assert case.label.realized_metrics[
        "incremental_credit_impairment_loss"
    ] == pytest.approx(116971965.03)
    assert case.label.realized_metrics[
        "incremental_credit_impairment_to_q3_equity"
    ] == pytest.approx(0.7275933568188709)


def test_agent_payload_does_not_expose_outcome_or_rqdata_provenance() -> None:
    rendered = json.dumps(_cases()[0].scenario.agent_payload(), ensure_ascii=False)

    assert "event_occurred" not in rendered
    assert "resolved_at" not in rendered
    assert "asset_impairment_loss" not in rendered
    assert "download_rqdata" not in rendered


def test_hygon_business_decision_case_has_generic_auditable_outcome() -> None:
    case = next(
        item
        for item in _cases()
        if item.scenario.id == "cn-a-2022-hygon-rd-commercial-validation"
    )

    assert case.scenario.schema_version == 2
    assert case.scenario.criteria_mode == "all"
    assert {item.metric for item in case.scenario.criteria} == {
        "revenue_cagr_2021_2024",
        "gross_margin_2024",
        "operating_cash_flow_2024",
    }
    assert case.label.event_occurred
    assert case.label.realized_metrics["revenue_cagr_2021_2024"] == pytest.approx(
        0.5828353892403499
    )
    assert case.label.realized_metrics["gross_margin_2024"] == pytest.approx(
        0.6372019640046754
    )

    rendered = json.dumps(case.scenario.agent_payload(), ensure_ascii=False)
    assert "revenue_2024" not in rendered
    assert "event_occurred" not in rendered
    assert "rqdata" not in rendered.lower()


def test_business_decisions_have_matched_rnd_and_factory_controls() -> None:
    business_cases = tuple(
        case
        for case in _cases()
        if case.scenario.suite == "a_share_business_decision_v1"
    )
    rnd_cases = tuple(
        case for case in business_cases if "-rd-commercial-validation" in case.scenario.id
    )
    factory_cases = tuple(
        case
        for case in business_cases
        if "-factory-commercial-validation" in case.scenario.id
    )

    assert len(business_cases) == 4
    assert len(rnd_cases) == 2
    assert {case.label.event_occurred for case in rnd_cases} == {False, True}
    assert len(factory_cases) == 2
    assert {case.label.event_occurred for case in factory_cases} == {False, True}

    factory_contracts = {
        tuple(
            (criterion.metric, criterion.comparison, criterion.value)
            for criterion in case.scenario.criteria
        )
        for case in factory_cases
    }
    assert len(factory_contracts) == 1
    assert all(
        "run-llama/liteparse 2.11.1 git 53e4fc8"
        in case.scenario.authoring_provenance["pdf_text_tool"]
        for case in business_cases
    )
    assert all(
        any(
            domain in document.url
            for domain in ("cs.com.cn", "stcn.com")
            for document in case.corpus.documents
        )
        for case in business_cases
    )
    assert all(
        "news_evidence_policy" in case.scenario.authoring_provenance
        for case in business_cases
    )

    catl = next(
        case for case in factory_cases if case.scenario.security.ticker == "300750"
    )
    dynanonic = next(
        case for case in factory_cases if case.scenario.security.ticker == "300769"
    )
    assert catl.label.realized_metrics[
        "announced_factory_schedule_validation"
    ] == 1
    assert dynanonic.label.realized_metrics[
        "announced_factory_schedule_validation"
    ] == 0
    assert dynanonic.label.realized_metrics["gross_margin_outcome"] < 0


def test_pledge_freeze_pair_is_same_company_balanced_and_non_mechanical() -> None:
    cases = tuple(
        case for case in _cases() if "pledge-freeze" in case.scenario.id
    )

    assert len(cases) == 2
    assert {case.scenario.security.order_book_id for case in cases} == {
        "603766.XSHG"
    }
    assert {case.scenario.target_event for case in cases} == {
        "material_controller_share_judicial_freeze"
    }
    assert {case.label.event_occurred for case in cases} == {False, True}

    negative = next(case for case in cases if not case.label.event_occurred)
    positive = next(case for case in cases if case.label.event_occurred)
    assert negative.label.realized_metrics[
        "controller_judicial_freeze_to_as_of_holding"
    ] == 0
    assert positive.label.realized_metrics[
        "controller_judicial_freeze_to_as_of_holding"
    ] == pytest.approx(0.36624958940468266)
    assert "不声称接近满仓质押必然导致冻结" in negative.scenario.target_definition
    assert "不声称接近满仓质押必然导致冻结" in positive.scenario.target_definition


def test_generic_label_rejects_a_tampered_derived_metric() -> None:
    case = next(
        item
        for item in _cases()
        if item.scenario.id == "cn-a-2022-hygon-rd-commercial-validation"
    )
    payload = {
        "schema_version": case.label.schema_version,
        "scenario_id": case.label.scenario_id,
        "resolved_at": case.label.resolved_at.isoformat(),
        "event_occurred": case.label.event_occurred,
        "realized": deepcopy(case.label.realized),
        "expected_evidence_ids": list(case.label.expected_evidence_ids),
        "outcome_sources": list(case.label.outcome_sources),
    }
    payload["realized"]["derivations"][0]["value"] = 0.1

    with pytest.raises(CaseValidationError, match="does not match cagr"):
        WalkForwardLabel.from_dict(
            payload,
            scenario=case.scenario,
            corpus=case.corpus,
            source="tampered-label",
        )


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

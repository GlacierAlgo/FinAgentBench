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


def test_st_speculative_runup_family_is_balanced_and_rejects_remediation_shortcuts() -> None:
    cases = tuple(
        case
        for case in _cases()
        if case.scenario.suite == "a_share_st_outcomes_v1"
    )

    assert len(cases) == 18
    assert sum(case.label.event_occurred for case in cases) == 9
    positives = {
        case.scenario.security.ticker
        for case in cases
        if case.label.event_occurred
    }
    negatives = {
        case.scenario.security.ticker
        for case in cases
        if not case.label.event_occurred
    }
    assert positives == {
        "000408",
        "000525",
        "000564",
        "002176",
        "300325",
        "600078",
        "600702",
        "601020",
        "603032",
    }
    assert negatives == {
        "000939",
        "002477",
        "002650",
        "002656",
        "002680",
        "600290",
        "600300",
        "600518",
        "600781",
    }
    assert {
        tuple(
            (criterion.metric, criterion.comparison, criterion.value)
            for criterion in case.scenario.criteria
        )
        for case in cases
    } == {
        (
            ("max_adjusted_close_return_365d", ">=", 1.0),
            ("max_excess_return_vs_510300_365d", ">=", 0.8),
        )
    }
    assert sum(
        case.scenario.authoring_provenance["st_cause_taxonomy"].startswith(
            "non_operating_governance/"
        )
        for case in cases
    ) == 10
    assert {
        case.label.event_occurred
        for case in cases
        if case.label.realized_metrics["risk_warning_removed_by_window_end"] == 1
    } == {False, True}
    assert {
        case.label.event_occurred
        for case in cases
        if case.label.realized_metrics["risk_warning_removed_by_window_end"] == 0
    } == {False, True}
    assert {
        case.label.realized_metrics["common_trading_sessions"] for case in cases
    } == {113, 241, 242, 243, 244}

    by_ticker = {case.scenario.security.ticker: case for case in cases}
    threshold_boundary = by_ticker["002650"]
    assert not threshold_boundary.label.event_occurred
    assert threshold_boundary.label.realized_metrics[
        "max_adjusted_close_return_365d"
    ] >= 1.0
    assert threshold_boundary.label.realized_metrics[
        "max_excess_return_vs_510300_365d"
    ] == pytest.approx(0.7907361841205645)
    assert threshold_boundary.label.realized_metrics[
        "max_excess_return_vs_510300_365d"
    ] < 0.8

    truncated_path = by_ticker["002477"]
    assert truncated_path.label.realized_metrics["common_trading_sessions"] == 113
    assert not truncated_path.label.event_occurred
    assert "do not impute" in truncated_path.label.outcome_sources[0][
        "observation_policy"
    ]

    all_cases = {case.scenario.id: case for case in _cases()}
    reused_corpora = {
        "cn-a-2020-st-speculative-runup-000408":
            "cn-a-2020-st-remediation-000408",
        "cn-a-2020-st-speculative-runup-002650":
            "cn-a-2020-st-remediation-002650",
        "cn-a-2019-st-speculative-runup-600518":
            "cn-a-2019-st-remediation-600518",
        "cn-a-2019-st-speculative-runup-600781":
            "cn-a-2019-st-remediation-600781",
        "cn-a-2019-st-speculative-runup-002477":
            "cn-a-2019-forced-delisting-002477",
        "cn-a-2018-st-speculative-runup-002680":
            "cn-a-2018-forced-delisting-002680",
        "cn-a-2018-st-speculative-runup-000939":
            "cn-a-2018-forced-delisting-000939",
    }
    for runup_id, source_id in reused_corpora.items():
        assert all_cases[runup_id].corpus.documents == all_cases[
            source_id
        ].corpus.documents

    assert all(
        document.published_at <= case.scenario.as_of
        for case in cases
        for document in case.corpus.documents
    )
    assert all(
        "not whether" in case.scenario.authoring_provenance["causal_guardrail"]
        or "deliberately not treated" in case.scenario.authoring_provenance[
            "causal_guardrail"
        ]
        for case in cases
    )


def test_st_remediation_family_requires_full_exchange_approved_removal() -> None:
    cases = tuple(
        case
        for case in _cases()
        if case.scenario.suite == "a_share_st_remediation_v1"
    )

    assert len(cases) == 12
    assert sum(case.label.event_occurred for case in cases) == 6
    assert {case.scenario.target_event for case in cases} == {
        "exchange_approved_full_risk_warning_removal_24m"
    }
    assert {
        tuple(
            (criterion.metric, criterion.comparison, criterion.value)
            for criterion in case.scenario.criteria
        )
        for case in cases
    } == {(('full_risk_warning_removal_count_24m', '>=', 1),)}

    positives = {
        case.scenario.security.ticker
        for case in cases
        if case.label.event_occurred
    }
    negatives = {
        case.scenario.security.ticker
        for case in cases
        if not case.label.event_occurred
    }
    assert positives == {
        "000408",
        "002168",
        "002650",
        "600080",
        "600300",
        "600702",
    }
    assert negatives == {
        "000525",
        "002656",
        "600078",
        "600290",
        "600518",
        "600781",
    }

    for case in cases:
        metrics = case.label.realized_metrics
        assert (
            metrics["full_risk_warning_removal_count_24m"] >= 1
        ) is case.label.event_occurred
        assert metrics["full_risk_warning_removed_by_window_end"] == int(
            case.label.event_occurred
        )
        assert metrics["risk_warning_present_at_window_end"] == int(
            not case.label.event_occurred
        )
        assert all(
            document.published_at <= case.scenario.as_of
            for document in case.corpus.documents
        )
        assert "*ST-to-ST downgrade" in case.scenario.authoring_provenance[
            "outcome_contract"
        ]

        payload = json.dumps(case.scenario.agent_payload(), ensure_ascii=False)
        assert "later_context_not_counted" not in payload
        assert "approved_effective_date" not in payload
        assert "2024-07-04" not in payload
        assert "2025-06-13" not in payload

        if case.label.event_occurred:
            removal = next(
                source
                for source in case.label.outcome_sources
                if source["type"]
                == "official_exchange_approved_full_risk_warning_removal"
            )
            assert removal["approved_effective_date"] <= (
                case.scenario.window_end.isoformat()
            )
            assert removal["all_risk_warnings_removed"]
            assert removal["exits_risk_warning_board"]
            assert "ST" not in removal["resulting_symbol"]

    partial_only = {
        case.scenario.security.ticker
        for case in cases
        if case.label.realized_metrics["partial_only_removal_count_24m"] >= 1
    }
    assert partial_only == {"600078", "600290", "600781"}
    assert all(
        not case.label.event_occurred
        for case in cases
        if case.scenario.security.ticker in partial_only
    )


def test_next_annual_audit_family_uses_the_first_financial_statement_opinion() -> None:
    cases = tuple(
        case
        for case in _cases()
        if case.scenario.suite == "a_share_next_annual_audit_v1"
    )
    remediation_by_ticker = {
        case.scenario.security.ticker: case
        for case in _cases()
        if case.scenario.suite == "a_share_st_remediation_v1"
    }

    assert len(cases) == 12
    assert sum(case.label.event_occurred for case in cases) == 6
    assert {case.scenario.target_event for case in cases} == {
        "first_post_snapshot_annual_financial_statement_nonstandard_audit_18m"
    }
    assert {
        tuple(
            (criterion.metric, criterion.comparison, criterion.value)
            for criterion in case.scenario.criteria
        )
        for case in cases
    } == {
        (
            (
                "qualifying_nonstandard_first_annual_audit_count_18m",
                ">=",
                1,
            ),
        )
    }

    positives = {
        case.scenario.security.ticker
        for case in cases
        if case.label.event_occurred
    }
    negatives = {
        case.scenario.security.ticker
        for case in cases
        if not case.label.event_occurred
    }
    assert positives == {
        "000525",
        "002168",
        "600078",
        "600290",
        "600518",
        "600781",
    }
    assert negatives == {
        "000408",
        "002650",
        "002656",
        "600080",
        "600300",
        "600702",
    }

    outcome_pairs = set()
    for case in cases:
        ticker = case.scenario.security.ticker
        remediation = remediation_by_ticker[ticker]
        outcome_pairs.add(
            (remediation.label.event_occurred, case.label.event_occurred)
        )
        assert case.scenario.as_of == remediation.scenario.as_of
        assert case.corpus.documents == remediation.corpus.documents
        assert all(
            document.published_at <= case.scenario.as_of
            for document in case.corpus.documents
        )

        metrics = case.label.realized_metrics
        assert metrics["first_post_snapshot_annual_audit_report_count_18m"] == 1
        assert metrics["qualifying_nonstandard_first_annual_audit_count_18m"] == int(
            case.label.event_occurred
        )
        assert metrics["first_annual_audit_nonstandard"] == int(
            case.label.event_occurred
        )
        assert metrics["first_annual_audit_standard_unqualified"] == int(
            not case.label.event_occurred
        )
        assert metrics["internal_control_audit_used_for_label"] == 0

        assert len(case.label.outcome_sources) == 1
        source = case.label.outcome_sources[0]
        assert source["type"] == (
            "official_first_post_snapshot_annual_financial_statement_audit_report"
        )
        assert case.scenario.as_of.isoformat() < source["published_at"]
        assert source["published_at"] <= case.scenario.window_end.isoformat()
        assert source["is_first_annual_financial_statement_audit_after_snapshot"]
        assert source["inside_18_calendar_month_window"]
        assert source["internal_control_opinion_not_used"]
        assert source["qualifies_as_nonstandard"] is case.label.event_occurred
        assert source["pdf_text_tool"] == (
            "run-llama/liteparse 2.11.1 git "
            "53e4fc813d35f76d0169923d2c451b3c8700edb0"
        )
        assert source["pdf_text_mode"] == (
            "native PDFium text extraction (--no-ocr)"
        )

        payload = json.dumps(case.scenario.agent_payload(), ensure_ascii=False)
        assert "audit_opinion" not in payload
        assert "qualification_basis" not in payload
        assert "qualifies_as_nonstandard" not in payload
        assert source["url"] not in payload
        assert source["sha256"] not in payload
        assert source["published_at"] not in payload

    assert outcome_pairs == {
        (False, False),
        (False, True),
        (True, False),
        (True, True),
    }

    chengxing = next(
        case for case in cases if case.scenario.security.ticker == "600078"
    )
    assert "强调事项段" in chengxing.label.outcome_sources[0]["audit_opinion"]
    assert chengxing.label.event_occurred


def test_forced_delisting_family_uses_fixed_first_warning_window() -> None:
    cases = tuple(
        case
        for case in _cases()
        if case.scenario.suite == "a_share_forced_delisting_v1"
    )
    remediation_by_ticker = {
        case.scenario.security.ticker: case
        for case in _cases()
        if case.scenario.suite == "a_share_st_remediation_v1"
    }

    assert len(cases) == 12
    assert sum(case.label.event_occurred for case in cases) == 6
    assert {case.scenario.target_event for case in cases} == {
        "exchange_decided_forced_delisting_60m"
    }
    assert {
        tuple(
            (criterion.metric, criterion.comparison, criterion.value)
            for criterion in case.scenario.criteria
        )
        for case in cases
    } == {
        (("exchange_forced_delisting_decision_count_60m", ">=", 1),)
    }

    positives = {
        case.scenario.security.ticker
        for case in cases
        if case.label.event_occurred
    }
    negatives = {
        case.scenario.security.ticker
        for case in cases
        if not case.label.event_occurred
    }
    assert positives == {
        "000939",
        "002450",
        "002477",
        "002680",
        "600290",
        "600781",
    }
    assert negatives == {
        "000408",
        "002650",
        "002656",
        "600080",
        "600518",
        "600702",
    }
    assert {
        case.scenario.authoring_provenance["matching_role"] for case in cases
    } == {"event", "no_event_hard_control"}

    routes = set()
    for case in cases:
        assert case.scenario.window_end.year == case.scenario.as_of.year + 5
        assert (
            case.scenario.window_end.month,
            case.scenario.window_end.day,
        ) == (case.scenario.as_of.month, case.scenario.as_of.day)
        assert all(
            document.published_at <= case.scenario.as_of
            for document in case.corpus.documents
        )
        assert "60-calendar-month" in case.scenario.authoring_provenance[
            "outcome_contract"
        ]
        assert "first trading day" in case.scenario.authoring_provenance[
            "first_warning_start_contract"
        ]

        metrics = case.label.realized_metrics
        assert metrics["first_risk_warning_day_verified"] == 1
        assert metrics["exchange_forced_delisting_decision_count_60m"] == int(
            case.label.event_occurred
        )
        route_count = sum(
            metrics[name]
            for name in (
                "major_illegality_route_decision_count_60m",
                "financial_route_decision_count_60m",
                "transaction_route_decision_count_60m",
            )
        )
        assert route_count == int(case.label.event_occurred)
        assert metrics["survived_fixed_window_without_forced_delisting"] == int(
            not case.label.event_occurred
        )

        status = next(
            source
            for source in case.label.outcome_sources
            if source["type"] == "rqdata_forced_delisting_status_crosscheck"
        )
        assert status["window"] == (
            f"{case.scenario.as_of.isoformat()}/"
            f"{case.scenario.window_end.isoformat()}"
        )
        assert status["first_risk_warning_trading_day"] == (
            case.scenario.as_of.isoformat()
        )
        assert status["forced_delisting_decision_within_window"] is (
            case.label.event_occurred
        )
        assert status["survived_fixed_window"] is (not case.label.event_occurred)

        payload = json.dumps(case.scenario.agent_payload(), ensure_ascii=False)
        assert "decision_date" not in payload
        assert "decision_reason" not in payload
        assert "delisting_route" not in payload

        if case.label.event_occurred:
            decision = next(
                source
                for source in case.label.outcome_sources
                if source["type"] == "official_exchange_forced_delisting_decision"
            )
            routes.add(decision["delisting_route"])
            assert decision["decision_date"] <= (
                case.scenario.window_end.isoformat()
            )
            assert decision["published_at"] <= case.label.resolved_at.isoformat()
            assert decision["is_exchange_final_decision"]
            assert decision["forced_not_voluntary"]
            assert decision["inside_60_calendar_month_window"]
            assert decision["pdf_text_tool"] == (
                "run-llama/liteparse 2.11.1 git "
                "53e4fc813d35f76d0169923d2c451b3c8700edb0"
            )
            assert decision["pdf_text_mode"] == (
                "native PDFium text extraction (--no-ocr)"
            )
            assert decision["url"] not in payload
            assert decision["sha256"] not in payload
            assert decision["decision_date"] not in payload

    assert routes == {"financial", "major_illegality", "transaction"}

    reused_tickers = {
        "000408",
        "002650",
        "002656",
        "600080",
        "600290",
        "600518",
        "600702",
        "600781",
    }
    for case in cases:
        ticker = case.scenario.security.ticker
        if ticker in reused_tickers:
            assert case.corpus.documents == remediation_by_ticker[ticker].corpus.documents

    modeng = next(
        case for case in cases if case.scenario.security.ticker == "002656"
    )
    assert not modeng.label.event_occurred
    assert modeng.scenario.window_end.isoformat() == "2025-01-13"
    modeng_status = modeng.label.outcome_sources[0]
    assert "2025-01-14" in modeng_status["later_context_not_counted"]


def test_public_debt_default_family_matches_real_payment_opportunities() -> None:
    cases = tuple(
        case
        for case in _cases()
        if case.scenario.suite == "a_share_public_debt_default_v1"
    )

    assert len(cases) == 4
    assert sum(case.label.event_occurred for case in cases) == 2
    assert {
        tuple(
            (criterion.metric, criterion.comparison, criterion.value)
            for criterion in case.scenario.criteria
        )
        for case in cases
    } == {(("material_public_debt_payment_failure_count_120d", ">=", 1),)}
    assert {
        case.scenario.authoring_provenance["matching_role"] for case in cases
    } == {"event", "no_event_hard_control"}

    for case in cases:
        metrics = case.label.realized_metrics
        assert metrics["scheduled_material_public_debt_payment_count_120d"] >= 1
        assert metrics["scheduled_material_public_debt_payment_amount_rmb"] >= 50_000_000
        assert (
            metrics["material_public_debt_payment_failure_count_120d"]
            + metrics["material_public_debt_payment_completed_count_120d"]
            == metrics["scheduled_material_public_debt_payment_count_120d"]
        )
        assert (
            metrics["material_public_debt_payment_failure_amount_rmb"]
            + metrics["material_public_debt_payment_completed_amount_rmb"]
            == pytest.approx(
                metrics["scheduled_material_public_debt_payment_amount_rmb"]
            )
        )
        assert (
            metrics["material_public_debt_payment_failure_count_120d"] >= 1
        ) is case.label.event_occurred
        assert "CNY50m" in case.scenario.authoring_provenance[
            "opportunity_contract"
        ]

    by_ticker = {case.scenario.security.ticker: case for case in cases}
    assert by_ticker["002450"].label.realized_metrics[
        "scheduled_material_public_debt_payment_count_120d"
    ] == 3
    assert by_ticker["600518"].label.realized_metrics[
        "scheduled_material_public_debt_payment_count_120d"
    ] == 4
    assert by_ticker["000413"].label.realized_metrics[
        "scheduled_material_public_debt_payment_count_120d"
    ] == 2
    assert by_ticker["002310"].label.realized_metrics[
        "scheduled_material_public_debt_payment_count_120d"
    ] == 2

    kangmei_payload = json.dumps(
        by_ticker["600518"].scenario.agent_payload(), ensure_ascii=False
    )
    assert "later found" not in kangmei_payload
    assert "hard_negative_reason" not in kangmei_payload
    assert "event_occurred" not in kangmei_payload


def test_cash_reality_pair_requires_parent_level_payment_capacity() -> None:
    cases = tuple(
        case
        for case in _cases()
        if case.scenario.suite == "a_share_cash_reality_v1"
    )

    assert len(cases) == 2
    assert {case.label.event_occurred for case in cases} == {False, True}
    assert {case.scenario.target_event for case in cases} == {
        "announced_cash_dividend_payment_failure_10d"
    }
    assert {
        case.scenario.authoring_provenance["matching_role"] for case in cases
    } == {"event", "no_event_hard_control"}
    assert all(
        case.label.realized_metrics["announced_cash_dividend_amount_rmb"]
        >= 50_000_000
        for case in cases
    )
    assert all(
        case.label.realized_metrics["consolidated_cash_to_announced_dividend"]
        > 20
        for case in cases
    )

    by_ticker = {case.scenario.security.ticker: case for case in cases}
    furen = by_ticker["600781"]
    kangde = by_ticker["002450"]
    assert furen.label.event_occurred
    assert not kangde.label.event_occurred
    assert furen.label.realized_metrics[
        "parent_cash_to_announced_dividend"
    ] < 0.01
    assert kangde.label.realized_metrics[
        "parent_cash_to_announced_dividend"
    ] > 30
    assert furen.label.realized_metrics["cash_dividend_paid_amount_rmb"] == 0
    assert kangde.label.realized_metrics[
        "cash_dividend_paid_amount_rmb"
    ] == pytest.approx(
        kangde.label.realized_metrics["announced_cash_dividend_amount_rmb"]
    )

    payload = json.dumps(kangde.scenario.agent_payload(), ensure_ascii=False)
    assert "later found" not in payload
    assert "hard_negative_reason" not in payload
    assert "debt defaults" not in payload


def test_enforcement_family_uses_fixed_window_and_temporal_hard_controls() -> None:
    cases = tuple(
        case
        for case in _cases()
        if case.scenario.suite == "a_share_enforcement_v1"
    )

    assert len(cases) == 6
    assert sum(case.label.event_occurred for case in cases) == 3
    assert {case.scenario.target_event for case in cases} == {
        "regulator_confirmed_material_financial_misstatement_30m"
    }
    assert {
        tuple(
            (criterion.metric, criterion.comparison, criterion.value)
            for criterion in case.scenario.criteria
        )
        for case in cases
    } == {
        (("qualifying_final_enforcement_decision_count_30m", ">=", 1),)
    }

    for case in cases:
        metrics = case.label.realized_metrics
        assert (
            metrics["qualifying_final_enforcement_decision_count_30m"] >= 1
        ) is case.label.event_occurred
        if case.label.event_occurred:
            assert metrics["largest_confirmed_material_amount_rmb"] >= 100_000_000
            decision = next(
                source
                for source in case.label.outcome_sources
                if source["type"]
                == "official_final_administrative_penalty_decision"
            )
            assert decision["decision_date"] <= case.scenario.window_end.isoformat()
        else:
            assert metrics["largest_confirmed_material_amount_rmb"] == 0

        payload = json.dumps(case.scenario.agent_payload(), ensure_ascii=False)
        assert "hard_negative_reason" not in payload
        assert "post_window" not in payload
        assert "2025" not in payload
        assert all(
            document.published_at <= case.scenario.as_of
            for document in case.corpus.documents
        )

    by_ticker = {case.scenario.security.ticker: case for case in cases}
    dongxu = by_ticker["000413"]
    assert not dongxu.label.event_occurred
    later_dongxu = next(
        source
        for source in dongxu.label.outcome_sources
        if source["type"] == "official_post_window_final_decision_context"
    )
    assert later_dongxu["decision_date"] > dongxu.scenario.window_end.isoformat()
    assert later_dongxu["not_counted"]

    oriental = by_ticker["002310"]
    later_oriental = next(
        source
        for source in oriental.label.outcome_sources
        if source["type"]
        == "official_post_window_subthreshold_decision_context"
    )
    assert later_oriental["decision_date"] > oriental.scenario.window_end.isoformat()
    assert later_oriental["confirmed_amount_rmb"] < 100_000_000
    assert any(
        document.url.startswith("https://www.sohu.com/")
        or document.url.startswith("https://www.cs.com.cn/")
        for case in cases
        for document in case.corpus.documents
    )


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

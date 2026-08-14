import json
from copy import deepcopy
from pathlib import Path

import pytest

from pitfall.a_share.dossier import (
    ISSUER_DOMAINS,
    IssuerDossier,
    dossier_digest,
    load_dossier,
    load_dossiers,
)
from pitfall.errors import CaseValidationError


def _payload() -> dict:
    event_specs = [
        (
            "original-name",
            "identity",
            "security_name_change",
            "2009-11-11",
            "2009-11-11",
            {"security_name": "湘鄂情"},
        ),
        (
            "management-snapshot",
            "governance",
            "management_team_snapshot",
            "2014-03-01",
            "2014-03-01",
            {"chairperson": "person-a"},
        ),
        (
            "controller-snapshot",
            "governance",
            "controller_snapshot",
            "2014-03-02",
            "2014-03-02",
            {"controller": "controller-a"},
        ),
        (
            "business-pivot",
            "commercial",
            "new_segment_announced",
            "2014-05-01",
            "2014-05-01",
            {"primary_business_segment": "cloud_services"},
        ),
        (
            "capital-plan",
            "capital_allocation",
            "investment_plan_announced",
            "2014-05-02",
            "2014-05-02",
            {},
        ),
        (
            "project-start",
            "operations",
            "project_construction_started",
            "2014-05-03",
            "2014-05-03",
            {"project_status": "construction"},
        ),
        (
            "quarterly-results",
            "reporting",
            "quarterly_report_published",
            "2014-05-04",
            "2014-03-31",
            {},
        ),
        (
            "audit-opinion",
            "reporting",
            "annual_audit_opinion",
            "2014-05-05",
            "2013-12-31",
            {"audit_opinion": "unqualified"},
        ),
        (
            "regulatory-letter",
            "regulatory",
            "exchange_inquiry_received",
            "2014-05-06",
            "2014-05-06",
            {},
        ),
        (
            "credit-facility",
            "financing",
            "credit_facility_signed",
            "2014-05-07",
            "2014-05-07",
            {"financing_status": "facility_signed"},
        ),
        (
            "receivables-snapshot",
            "working_capital",
            "receivables_snapshot",
            "2014-05-08",
            "2014-03-31",
            {},
        ),
        (
            "debt-payment",
            "cash_payment",
            "public_debt_payment_completed",
            "2014-05-09",
            "2014-05-09",
            {},
        ),
        (
            "market-snapshot",
            "market",
            "market_path_snapshot",
            "2014-05-10",
            "2014-05-09",
            {},
        ),
        (
            "announced-rename",
            "identity",
            "security_name_change",
            "2014-07-18",
            "2014-08-01",
            {"security_name": "中科云网"},
        ),
        (
            "future-st",
            "listing",
            "risk_warning_status_change",
            "2015-04-29",
            "2015-04-30",
            {"risk_warning_status": "star_st"},
        ),
    ]
    sources = []
    events = []
    for event_id, domain, event_type, info_date, effective_date, updates in event_specs:
        source_id = f"source-{event_id}"
        sources.append(
            {
                "id": source_id,
                "published_at": info_date,
                "source_type": "official_filing",
                "title": f"Source for {event_id}",
                "locator": f"fixture://{source_id}",
            }
        )
        events.append(
            {
                "id": event_id,
                "domain": domain,
                "event_type": event_type,
                "info_date": info_date,
                "effective_date": effective_date,
                "summary": f"Summary for {event_id}",
                "source_ids": [source_id],
                "state_updates": updates,
                "details": {"fixture_fact": event_id},
            }
        )
    return {
        "schema_version": 1,
        "dossier_id": "issuer-002306-xshe",
        "issuer": {
            "order_book_id": "002306.XSHE",
            "ticker": "002306",
            "exchange": "XSHE",
        },
        "events": events,
        "sources": sources,
    }


def test_dossier_connects_operating_domains_and_has_stable_digest() -> None:
    payload = _payload()
    dossier = IssuerDossier.from_dict(payload)
    reordered = deepcopy(payload)
    reordered["events"].reverse()
    reordered["sources"].reverse()

    assert dossier.issuer.order_book_id == "002306.XSHE"
    assert {event.domain for event in dossier.events} == ISSUER_DOMAINS
    assert dossier_digest(dossier) == dossier.digest()
    assert dossier.digest() == IssuerDossier.from_dict(reordered).digest()
    assert len(dossier.digest()) == 64


def test_as_of_slice_separates_visible_plans_from_effective_state() -> None:
    dossier = IssuerDossier.from_dict(_payload())

    announced = dossier.as_of_slice("2014-07-20")
    assert "announced-rename" in {event.id for event in announced.visible_events}
    assert "announced-rename" not in {event.id for event in announced.effective_events}
    assert [event.id for event in announced.planned_events] == ["announced-rename"]
    assert announced.current_state["security_name"] == "湘鄂情"

    effective = dossier.as_of_slice("2014-08-01")
    assert "announced-rename" in {event.id for event in effective.effective_events}
    assert effective.current_state["security_name"] == "中科云网"


def test_as_of_slice_excludes_future_information_from_events_and_sources() -> None:
    dossier = IssuerDossier.from_dict(_payload())
    public_slice = dossier.as_of_slice("2014-08-01")
    rendered = json.dumps(public_slice.to_dict(), ensure_ascii=False)

    assert "future-st" not in rendered
    assert "source-future-st" not in rendered
    assert "star_st" not in rendered
    assert all(
        event.info_date <= public_slice.as_of for event in public_slice.visible_events
    )
    assert all(
        event.info_date <= public_slice.as_of
        and event.effective_date <= public_slice.as_of
        for event in public_slice.effective_events
    )
    assert all(item.published_at <= public_slice.as_of for item in public_slice.sources)


def test_validation_rejects_source_after_declared_info_date() -> None:
    payload = _payload()
    payload["sources"][-1]["published_at"] = "2015-05-01"

    with pytest.raises(CaseValidationError, match="after its info_date"):
        IssuerDossier.from_dict(payload)


def test_loaders_validate_files_and_duplicate_stable_identity(tmp_path) -> None:
    first = tmp_path / "first.json"
    first.write_text(json.dumps(_payload(), ensure_ascii=False), encoding="utf-8")

    loaded = load_dossier(first)
    assert loaded.issuer.order_book_id == "002306.XSHE"
    assert load_dossiers(tmp_path) == (loaded,)

    duplicate = deepcopy(_payload())
    duplicate["dossier_id"] = "another-dossier-id"
    (tmp_path / "second.json").write_text(
        json.dumps(duplicate, ensure_ascii=False), encoding="utf-8"
    )
    with pytest.raises(CaseValidationError, match="order_book_ids must be unique"):
        load_dossiers(tmp_path)


def test_builtin_zhongke_dossier_preserves_rename_and_warning_effective_dates() -> None:
    path = (
        Path(__file__).parents[1]
        / "src/pitfall/a_share/dossiers/issuer-002306-xshe.json"
    )
    dossier = load_dossier(path)

    assert dossier.issuer.order_book_id == "002306.XSHE"
    assert len(dossier.events) >= 25
    announced = dossier.as_of_slice("2016-05-13")
    effective = dossier.as_of_slice("2016-05-16")
    assert announced.current_state["security_name"] == "*ST云网"
    assert announced.current_state["risk_warning_status"] == "star_st"
    assert [event.id for event in announced.planned_events] == [
        "full-risk-warning-removal-2016"
    ]
    assert effective.current_state["security_name"] == "中科云网"
    assert effective.current_state["risk_warning_status"] == "none"

    rename_plan = dossier.as_of_slice("2014-07-02")
    assert [event.id for event in rename_plan.planned_events] == [
        "legal-name-change-planned"
    ]
    assert "legal_name" not in rename_plan.current_state

    latest = dossier.as_of_slice("2026-06-12").current_state
    assert latest["audit_opinion"] == "unqualified"
    assert latest["latest_report_period"] == "2025q2"
    assert latest["primary_business_segments"] == [
        "group_meals",
        "photovoltaic_battery",
    ]
    assert latest["public_bond_listing_status"] == "redeemed"
    assert latest["public_bond_rating"] is None

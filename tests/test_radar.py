from pathlib import Path

from finagentbench.radar import build_radar_data, render_radar_data_js

REPO_ROOT = Path(__file__).parents[1]


def test_radar_builds_balanced_distinct_a_share_development_set() -> None:
    payload = build_radar_data(REPO_ROOT, REPO_ROOT / "radar/source-manifest.json")

    assert payload["tier"] == "development_diagnostics"
    assert payload["coverage"] == {
        "case_count": 90,
        "event_count": 45,
        "no_event_count": 45,
        "model_count": 3,
        "attempt_count": 270,
        "sealed_eligible_suite_count": 0,
    }
    assert len({case["id"] for case in payload["cases"]}) == 90
    assert {len(case["runs"]) for case in payload["cases"]} == {3}
    assert all(
        run["search_calls"] >= 1
        for case in payload["cases"]
        for run in case["runs"]
        if run["status"] == "completed"
    )
    assert {item["family"] for item in payload["family_summaries"]} == {
        "goodwill",
        "pledge-control",
        "pledge-freeze",
        "inventory",
        "performance-commitment",
        "receivables",
        "audit-opinion",
        "st-transition",
        "rd-validation",
        "factory-validation",
        "cash-reality",
        "public-debt-default",
        "enforcement",
        "next-annual-audit",
        "st-remediation",
        "forced-delisting",
        "st-market-path",
    }


def test_radar_never_promotes_public_replays_to_sealed_leaderboard() -> None:
    payload = build_radar_data(REPO_ROOT, REPO_ROOT / "radar/source-manifest.json")

    assert payload["leaderboard"]["status"] == "not_yet_eligible"
    assert payload["leaderboard"]["eligible_suite_count"] == 0
    assert all(item["repeats"] == 1 for item in payload["experiment_suites"])
    assert all(item["harness"]["outcome_visible_to_agent"] is False for item in payload["experiment_suites"])
    assert render_radar_data_js(payload).startswith(
        "window.FINAGENTBENCH_RADAR_DATA="
    )

"""Pre-registered cohorts of live-shadow cases and prediction seals."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from datetime import UTC, datetime
from typing import Any
from zoneinfo import ZoneInfo

from finagentbench.case import CaseValidationError
from finagentbench.live_shadow import (
    CANONICALIZATION,
    verify_live_shadow_seal,
)
from finagentbench.walkforward import WalkForwardScenario

PLAN_TYPE = "finagentbench_sealed_suite_plan"
PUBLIC_PLAN_TYPE = "finagentbench_sealed_suite_plan_commitment"
SUITE_TYPE = "finagentbench_sealed_suite"


def preregister_suite(
    source: dict[str, Any],
    *,
    now: datetime | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Create a private outcome-free plan and a publishable opaque commitment."""
    current = now or datetime.now(UTC)
    if current.tzinfo is None:
        raise CaseValidationError("suite registration time must be timezone-aware")
    suite_id, policy, cases = _validate_source(source, registered_at=current)
    registered_at = current.astimezone(UTC).isoformat()
    plan_record = {
        "schema_version": 1,
        "artifact_type": PLAN_TYPE,
        "suite_id": suite_id,
        "registered_at": registered_at,
        "policy": policy,
        "cases": cases,
        "publication_guardrail": (
            "Keep this full plan private until its cases are sealed. Publish the "
            "separate opaque commitment to an externally timestamped append-only "
            "surface before the first model run."
        ),
    }
    plan = _with_commitment(plan_record)
    family_counts = Counter(item["family"] for item in cases)
    scenarios = [
        WalkForwardScenario.from_dict(item["scenario_source"])
        for item in cases
    ]
    public_record = {
        "schema_version": 1,
        "artifact_type": PUBLIC_PLAN_TYPE,
        "suite_id": suite_id,
        "registered_at": registered_at,
        "case_count": len(cases),
        "family_counts": dict(sorted(family_counts.items())),
        "first_as_of": min(item.as_of for item in scenarios).isoformat(),
        "last_window_end": max(item.window_end for item in scenarios).isoformat(),
        "required_model_count": len(policy["required_models"]),
        "repeats": policy["repeats"],
        "plan_commitment_sha256": plan["commitment"]["payload_sha256"],
        "policy_sha256": _digest(policy),
        "timestamp_guardrail": (
            "This hash binds the private plan bytes but does not independently prove "
            "when they existed; externally timestamp this artifact before the first run."
        ),
    }
    return plan, _with_commitment(public_record)


def verify_suite_plan(payload: dict[str, Any]) -> str:
    """Verify a private suite plan and every embedded outcome-free scenario."""
    digest = _verify_commitment(payload, expected_type=PLAN_TYPE)
    required = {"suite_id", "registered_at", "policy", "cases"}
    missing = sorted(required - payload.keys())
    if missing:
        raise CaseValidationError(f"sealed suite plan missing: {', '.join(missing)}")
    registered_at = _datetime(payload["registered_at"], field="registered_at")
    source = {
        "schema_version": 1,
        "suite_id": payload["suite_id"],
        "policy": payload["policy"],
        "cases": [
            {
                "slot_id": item.get("slot_id"),
                "family": item.get("family"),
                "scenario": item.get("scenario_source"),
            }
            for item in _list(payload["cases"], field="cases")
            if isinstance(item, dict)
        ],
    }
    _, _, cases = _validate_source(source, registered_at=registered_at)
    raw_cases = _list(payload["cases"], field="cases")
    if len(cases) != len(raw_cases):
        raise CaseValidationError("sealed suite plan cases must be objects")
    for index, (stored, validated) in enumerate(zip(raw_cases, cases, strict=True)):
        if stored.get("scenario_sha256") != validated["scenario_sha256"]:
            raise CaseValidationError(
                f"sealed suite plan cases[{index}] scenario digest mismatch"
            )
    return digest


def verify_public_plan_commitment(payload: dict[str, Any]) -> str:
    """Verify the publishable opaque commitment without revealing scenarios."""
    digest = _verify_commitment(payload, expected_type=PUBLIC_PLAN_TYPE)
    required = {
        "suite_id",
        "registered_at",
        "case_count",
        "family_counts",
        "first_as_of",
        "last_window_end",
        "required_model_count",
        "repeats",
        "plan_commitment_sha256",
        "policy_sha256",
    }
    missing = sorted(required - payload.keys())
    if missing:
        raise CaseValidationError(
            f"sealed suite public commitment missing: {', '.join(missing)}"
        )
    if _positive_int(payload["case_count"], field="case_count") < 6:
        raise CaseValidationError("sealed suite public case_count must be at least 6")
    if _positive_int(payload["required_model_count"], field="required_model_count") < 2:
        raise CaseValidationError(
            "sealed suite public required_model_count must be at least 2"
        )
    if _positive_int(payload["repeats"], field="repeats") < 3:
        raise CaseValidationError("sealed suite public repeats must be at least 3")
    family_counts = payload["family_counts"]
    if not isinstance(family_counts, dict) or len(family_counts) < 3:
        raise CaseValidationError(
            "sealed suite public family_counts must contain at least 3 families"
        )
    if any(
        not isinstance(name, str)
        or not name.strip()
        or _positive_int(count, field=f"family_counts.{name}") < 2
        for name, count in family_counts.items()
    ):
        raise CaseValidationError(
            "sealed suite public families must each contain at least 2 cases"
        )
    if sum(family_counts.values()) != payload["case_count"]:
        raise CaseValidationError("sealed suite public family counts do not add up")
    _datetime(payload["registered_at"], field="registered_at")
    _sha256(payload["plan_commitment_sha256"], field="plan_commitment_sha256")
    _sha256(payload["policy_sha256"], field="policy_sha256")
    return digest


def finalize_suite(
    plan: dict[str, Any],
    public_commitment: dict[str, Any],
    seals: list[dict[str, Any]],
    *,
    now: datetime | None = None,
) -> dict[str, Any]:
    """Bind one intact live-shadow seal to every pre-registered case slot."""
    plan_digest = verify_suite_plan(plan)
    public_digest = verify_public_plan_commitment(public_commitment)
    if public_commitment["plan_commitment_sha256"] != plan_digest:
        raise CaseValidationError("public commitment does not match private plan")
    if public_commitment["policy_sha256"] != _digest(plan["policy"]):
        raise CaseValidationError("public commitment policy digest mismatch")
    if public_commitment["suite_id"] != plan["suite_id"]:
        raise CaseValidationError("public commitment suite_id mismatch")
    planned_by_sha = {
        item["scenario_sha256"]: item for item in plan["cases"]
    }
    if len(seals) != len(planned_by_sha):
        raise CaseValidationError("finalized suite requires exactly one seal per slot")
    policy = plan["policy"]
    registered_at = _datetime(plan["registered_at"], field="registered_at")
    members = []
    seen = set()
    for seal in seals:
        seal_digest = verify_live_shadow_seal(seal)
        scenario_sha = seal.get("scenario_sha256")
        planned = planned_by_sha.get(scenario_sha)
        if planned is None:
            raise CaseValidationError("suite seal scenario was not pre-registered")
        if scenario_sha in seen:
            raise CaseValidationError("suite contains a duplicate scenario seal")
        seen.add(scenario_sha)
        _validate_seal_matrix(seal, policy=policy)
        started_at = _datetime(seal.get("started_at"), field="seal.started_at")
        if started_at < registered_at:
            raise CaseValidationError("suite seal predates plan registration")
        scenario = WalkForwardScenario.from_dict(planned["scenario_source"])
        results = _list(seal.get("results"), field="seal.results")
        members.append(
            {
                "slot_id": planned["slot_id"],
                "family": planned["family"],
                "scenario_id": scenario.id,
                "scenario_sha256": scenario_sha,
                "seal_commitment_sha256": seal_digest,
                "as_of": scenario.as_of.isoformat(),
                "window_end": scenario.window_end.isoformat(),
                "attempt_count": len(results),
                "completed_count": sum(
                    item.get("status") == "completed"
                    for item in results
                    if isinstance(item, dict)
                ),
            }
        )
    members.sort(key=lambda item: item["slot_id"])
    current = now or datetime.now(UTC)
    if current.tzinfo is None:
        raise CaseValidationError("suite finalization time must be timezone-aware")
    record = {
        "schema_version": 1,
        "artifact_type": SUITE_TYPE,
        "suite_id": plan["suite_id"],
        "created_at": current.astimezone(UTC).isoformat(),
        "plan_commitment_sha256": plan_digest,
        "public_plan_commitment_sha256": public_digest,
        "policy": policy,
        "members": members,
        "outcome_status": "unresolved",
        "resolution_guardrail": (
            "Every member remains in the cohort, including failed attempts. Aggregate "
            "scores may be created only after every member has a verified matured resolution."
        ),
    }
    return _with_commitment(record)


def verify_finalized_suite(payload: dict[str, Any]) -> str:
    """Verify a finalized unresolved suite index and its cohort invariants."""
    digest = _verify_commitment(payload, expected_type=SUITE_TYPE)
    required = {
        "suite_id",
        "created_at",
        "plan_commitment_sha256",
        "public_plan_commitment_sha256",
        "policy",
        "members",
        "outcome_status",
    }
    missing = sorted(required - payload.keys())
    if missing:
        raise CaseValidationError(f"finalized suite missing: {', '.join(missing)}")
    policy = _validate_policy(payload["policy"])
    members = _list(payload["members"], field="members")
    if len(members) < policy["minimum_case_count"]:
        raise CaseValidationError("finalized suite contains too few members")
    slot_ids = set()
    scenario_hashes = set()
    family_counts: Counter[str] = Counter()
    expected_attempts = len(policy["required_models"]) * policy["repeats"]
    for index, member in enumerate(members):
        if not isinstance(member, dict):
            raise CaseValidationError(f"members[{index}] must be an object")
        slot_id = _string(member.get("slot_id"), field=f"members[{index}].slot_id")
        family = _string(member.get("family"), field=f"members[{index}].family")
        scenario_sha = _sha256(
            member.get("scenario_sha256"),
            field=f"members[{index}].scenario_sha256",
        )
        _sha256(
            member.get("seal_commitment_sha256"),
            field=f"members[{index}].seal_commitment_sha256",
        )
        if slot_id in slot_ids or scenario_sha in scenario_hashes:
            raise CaseValidationError("finalized suite member identities must be unique")
        slot_ids.add(slot_id)
        scenario_hashes.add(scenario_sha)
        family_counts[family] += 1
        if member.get("attempt_count") != expected_attempts:
            raise CaseValidationError("finalized suite attempt_count mismatch")
        completed = member.get("completed_count")
        if (
            not isinstance(completed, int)
            or isinstance(completed, bool)
            or not 0 <= completed <= expected_attempts
        ):
            raise CaseValidationError("finalized suite completed_count is invalid")
    _validate_case_distribution(
        member_count=len(members),
        family_counts=family_counts,
        policy=policy,
    )
    if payload["outcome_status"] != "unresolved":
        raise CaseValidationError("new finalized suites must remain unresolved")
    _datetime(payload["created_at"], field="created_at")
    _sha256(payload["plan_commitment_sha256"], field="plan_commitment_sha256")
    _sha256(
        payload["public_plan_commitment_sha256"],
        field="public_plan_commitment_sha256",
    )
    return digest


def _validate_source(
    source: dict[str, Any],
    *,
    registered_at: datetime,
) -> tuple[str, dict[str, Any], list[dict[str, Any]]]:
    if not isinstance(source, dict) or source.get("schema_version") != 1:
        raise CaseValidationError("sealed suite source schema_version must be 1")
    required = {"suite_id", "policy", "cases"}
    missing = sorted(required - source.keys())
    if missing:
        raise CaseValidationError(f"sealed suite source missing: {', '.join(missing)}")
    suite_id = _string(source["suite_id"], field="suite_id")
    policy = _validate_policy(source["policy"])
    raw_cases = _list(source["cases"], field="cases")
    cases = []
    slot_ids = set()
    scenario_ids = set()
    scenario_hashes = set()
    family_counts: Counter[str] = Counter()
    for index, raw in enumerate(raw_cases):
        if not isinstance(raw, dict):
            raise CaseValidationError(f"cases[{index}] must be an object")
        slot_id = _string(raw.get("slot_id"), field=f"cases[{index}].slot_id")
        family = _string(raw.get("family"), field=f"cases[{index}].family")
        scenario_source = raw.get("scenario")
        if not isinstance(scenario_source, dict):
            raise CaseValidationError(f"cases[{index}].scenario must be an object")
        scenario = WalkForwardScenario.from_dict(
            scenario_source,
            source=f"sealed suite cases[{index}].scenario",
        )
        if scenario.mode != "live_shadow":
            raise CaseValidationError("sealed suite cases must use live_shadow mode")
        market_registered = registered_at.astimezone(_timezone(scenario)).date()
        if scenario.as_of < market_registered:
            raise CaseValidationError("sealed suite cannot preregister a past as_of")
        scenario_sha = _digest(scenario_source)
        if (
            slot_id in slot_ids
            or scenario.id in scenario_ids
            or scenario_sha in scenario_hashes
        ):
            raise CaseValidationError("sealed suite case identities must be unique")
        slot_ids.add(slot_id)
        scenario_ids.add(scenario.id)
        scenario_hashes.add(scenario_sha)
        family_counts[family] += 1
        cases.append(
            {
                "slot_id": slot_id,
                "family": family,
                "scenario_source": scenario_source,
                "scenario_sha256": scenario_sha,
            }
        )
    _validate_case_distribution(
        member_count=len(cases),
        family_counts=family_counts,
        policy=policy,
    )
    return suite_id, policy, cases


def _validate_policy(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise CaseValidationError("sealed suite policy must be an object")
    required = {
        "required_models",
        "reasoning_effort",
        "repeats",
        "required_web_search_calls",
        "minimum_case_count",
        "minimum_family_count",
        "minimum_cases_per_family",
        "primary_metric",
    }
    missing = sorted(required - value.keys())
    if missing:
        raise CaseValidationError(f"sealed suite policy missing: {', '.join(missing)}")
    models = value["required_models"]
    if (
        not isinstance(models, list)
        or len(models) < 2
        or not all(isinstance(item, str) and item.strip() for item in models)
        or len(set(models)) != len(models)
    ):
        raise CaseValidationError("required_models must contain at least 2 unique IDs")
    effort = _string(value["reasoning_effort"], field="reasoning_effort")
    if effort not in {"low", "medium", "high", "xhigh", "max"}:
        raise CaseValidationError("sealed suite reasoning_effort is unsupported")
    repeats = _positive_int(value["repeats"], field="repeats")
    if repeats < 3:
        raise CaseValidationError("sealed hard suite requires at least 3 repeats")
    searches = _positive_int(
        value["required_web_search_calls"],
        field="required_web_search_calls",
    )
    minimum_cases = _positive_int(
        value["minimum_case_count"], field="minimum_case_count"
    )
    minimum_families = _positive_int(
        value["minimum_family_count"], field="minimum_family_count"
    )
    minimum_per_family = _positive_int(
        value["minimum_cases_per_family"],
        field="minimum_cases_per_family",
    )
    if minimum_cases < 6 or minimum_families < 3 or minimum_per_family < 2:
        raise CaseValidationError(
            "sealed hard suite requires >=6 cases, >=3 families, and >=2 cases per family"
        )
    if value["primary_metric"] != "mean_brier_loss":
        raise CaseValidationError("sealed suite primary_metric must be mean_brier_loss")
    return {
        "required_models": [item.strip() for item in models],
        "reasoning_effort": effort,
        "repeats": repeats,
        "required_web_search_calls": searches,
        "minimum_case_count": minimum_cases,
        "minimum_family_count": minimum_families,
        "minimum_cases_per_family": minimum_per_family,
        "primary_metric": "mean_brier_loss",
    }


def _validate_case_distribution(
    *,
    member_count: int,
    family_counts: Counter[str],
    policy: dict[str, Any],
) -> None:
    if member_count < policy["minimum_case_count"]:
        raise CaseValidationError("sealed suite contains too few cases")
    if len(family_counts) < policy["minimum_family_count"]:
        raise CaseValidationError("sealed suite contains too few families")
    if any(
        count < policy["minimum_cases_per_family"]
        for count in family_counts.values()
    ):
        raise CaseValidationError("every sealed suite family needs enough cases")


def _validate_seal_matrix(seal: dict[str, Any], *, policy: dict[str, Any]) -> None:
    matrix = seal.get("matrix")
    if not isinstance(matrix, dict):
        raise CaseValidationError("suite seal matrix is missing")
    if matrix.get("models") != policy["required_models"]:
        raise CaseValidationError("suite seal model matrix differs from plan")
    if matrix.get("reasoning_effort") != policy["reasoning_effort"]:
        raise CaseValidationError("suite seal reasoning effort differs from plan")
    if matrix.get("repeats") != policy["repeats"]:
        raise CaseValidationError("suite seal repeats differ from plan")
    results = _list(seal.get("results"), field="seal.results")
    expected = {
        (model, repeat_index)
        for model in policy["required_models"]
        for repeat_index in range(1, policy["repeats"] + 1)
    }
    observed = set()
    for index, result in enumerate(results):
        if not isinstance(result, dict):
            raise CaseValidationError(f"seal.results[{index}] must be an object")
        if result.get("reasoning_effort") != policy["reasoning_effort"]:
            raise CaseValidationError(
                "suite seal attempt reasoning effort differs from plan"
            )
        status = result.get("status")
        if status not in {"completed", "failed"}:
            raise CaseValidationError("suite seal attempt status is invalid")
        search_calls = result.get("web_search_calls")
        if (
            not isinstance(search_calls, int)
            or isinstance(search_calls, bool)
            or search_calls < 0
        ):
            raise CaseValidationError(
                "suite seal attempt web_search_calls is invalid"
            )
        identity = (result.get("model"), result.get("repeat_index"))
        if identity in observed:
            raise CaseValidationError("suite seal contains duplicate attempts")
        observed.add(identity)
        if (
            status == "completed"
            and search_calls < policy["required_web_search_calls"]
        ):
            raise CaseValidationError(
                "completed suite attempt did not meet the search-call minimum"
            )
    if observed != expected:
        raise CaseValidationError("suite seal attempt matrix is incomplete")


def _with_commitment(record: dict[str, Any]) -> dict[str, Any]:
    return {
        **record,
        "commitment": {
            "algorithm": "sha256",
            "canonicalization": CANONICALIZATION,
            "payload_sha256": _digest(record),
        },
    }


def _verify_commitment(payload: dict[str, Any], *, expected_type: str) -> str:
    if not isinstance(payload, dict) or payload.get("artifact_type") != expected_type:
        raise CaseValidationError(f"expected artifact_type {expected_type}")
    commitment = payload.get("commitment")
    if not isinstance(commitment, dict):
        raise CaseValidationError("sealed suite commitment is missing")
    if commitment.get("algorithm") != "sha256":
        raise CaseValidationError("sealed suite commitment algorithm is unsupported")
    if commitment.get("canonicalization") != CANONICALIZATION:
        raise CaseValidationError("sealed suite canonicalization is unsupported")
    record = {key: value for key, value in payload.items() if key != "commitment"}
    calculated = _digest(record)
    if commitment.get("payload_sha256") != calculated:
        raise CaseValidationError("sealed suite commitment digest mismatch")
    return calculated


def _digest(payload: Any) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _datetime(value: Any, *, field: str) -> datetime:
    if not isinstance(value, str):
        raise CaseValidationError(f"sealed suite {field} must be an ISO datetime")
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError as error:
        raise CaseValidationError(
            f"sealed suite {field} must be an ISO datetime"
        ) from error
    if parsed.tzinfo is None:
        raise CaseValidationError(f"sealed suite {field} must include a timezone")
    return parsed


def _positive_int(value: Any, *, field: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise CaseValidationError(f"sealed suite {field} must be a positive integer")
    return value


def _sha256(value: Any, *, field: str) -> str:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(character not in "0123456789abcdef" for character in value)
    ):
        raise CaseValidationError(f"sealed suite {field} must be a SHA-256 hex digest")
    return value


def _string(value: Any, *, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CaseValidationError(f"sealed suite {field} must be a non-empty string")
    return value.strip()


def _list(value: Any, *, field: str) -> list[Any]:
    if not isinstance(value, list):
        raise CaseValidationError(f"sealed suite {field} must be a list")
    return value


def _timezone(scenario: WalkForwardScenario) -> ZoneInfo:
    if scenario.security.exchange in {"SSE", "SZSE", "BSE"}:
        return ZoneInfo("Asia/Shanghai")
    return ZoneInfo("UTC")

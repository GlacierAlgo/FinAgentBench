"""Validation for unresolved live-shadow scenario artifacts."""

from __future__ import annotations

import math
import re
from dataclasses import asdict, dataclass
from datetime import date
from typing import Any

from pitfall.errors import CaseValidationError


@dataclass(frozen=True)
class Security:
    order_book_id: str
    ticker: str
    name_as_of: str
    exchange: str


@dataclass(frozen=True)
class SearchPolicy:
    mode: str
    latest_published_at: date
    allowed_domains: tuple[str, ...]


@dataclass(frozen=True)
class TargetCriterion:
    metric: str
    comparison: str
    value: float
    description: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class WalkForwardScenario:
    schema_version: int
    id: str
    suite: str
    mode: str
    security: Security
    as_of: date
    window_end: date
    target_event: str
    target_definition: str
    criteria_mode: str
    criteria: tuple[TargetCriterion, ...]
    legacy_threshold: float | None
    legacy_denominator: str | None
    prompt: str
    search_policy: SearchPolicy
    response_contract: dict[str, Any]
    authoring_provenance: dict[str, Any]

    @property
    def threshold(self) -> float | None:
        """Retain the v1 impairment-threshold accessor for callers."""
        return self.legacy_threshold

    @property
    def denominator(self) -> str | None:
        """Retain the v1 impairment-denominator accessor for callers."""
        return self.legacy_denominator

    @classmethod
    def from_dict(
        cls, payload: dict[str, Any], *, source: str = "<memory>"
    ) -> WalkForwardScenario:
        required = {
            "schema_version",
            "id",
            "suite",
            "mode",
            "security",
            "as_of",
            "prediction_window",
            "target",
            "prompt",
            "search_policy",
            "response_contract",
            "authoring_provenance",
        }
        _require_fields(payload, required, source=source)
        schema_version = payload["schema_version"]
        if schema_version not in {1, 2}:
            raise CaseValidationError(f"{source}: schema_version must be 1 or 2")

        mode = _string(payload["mode"], field="mode", source=source)
        if mode not in {"historical_frozen_web", "live_shadow"}:
            raise CaseValidationError(f"{source}: unsupported mode {mode!r}")

        security_payload = _object(payload["security"], "security", source)
        _require_fields(
            security_payload,
            {"order_book_id", "ticker", "name_as_of", "exchange"},
            source=f"{source}: security",
        )
        security = Security(
            order_book_id=_string(
                security_payload["order_book_id"],
                field="order_book_id",
                source=f"{source}: security",
            ),
            ticker=_string(
                security_payload["ticker"],
                field="ticker",
                source=f"{source}: security",
            ),
            name_as_of=_string(
                security_payload["name_as_of"],
                field="name_as_of",
                source=f"{source}: security",
            ),
            exchange=_string(
                security_payload["exchange"],
                field="exchange",
                source=f"{source}: security",
            ),
        )
        as_of = _date(payload["as_of"], field="as_of", source=source)

        window = _object(payload["prediction_window"], "prediction_window", source)
        _require_fields(window, {"end", "description"}, source=f"{source}: window")
        window_end = _date(window["end"], field="end", source=f"{source}: window")
        if window_end <= as_of:
            raise CaseValidationError(
                f"{source}: prediction window must end after as_of"
            )

        target = _object(payload["target"], "target", source)
        target_source = f"{source}: target"
        if schema_version == 1:
            _require_fields(
                target,
                {"event", "threshold", "denominator", "definition"},
                source=target_source,
            )
            threshold = _probability(
                target["threshold"], field="threshold", source=target_source
            )
            if threshold == 0:
                raise CaseValidationError(
                    f"{source}: target threshold must be positive"
                )
            denominator = _string(
                target["denominator"], field="denominator", source=target_source
            )
            criteria_mode = "all"
            criteria = (
                TargetCriterion(
                    metric="asset_impairment_ratio",
                    comparison=">",
                    value=threshold,
                    description=_string(
                        target["definition"],
                        field="definition",
                        source=target_source,
                    ),
                ),
            )
        else:
            _require_fields(
                target,
                {"event", "definition", "criteria_mode", "criteria"},
                source=target_source,
            )
            threshold = None
            denominator = None
            criteria_mode = _string(
                target["criteria_mode"],
                field="criteria_mode",
                source=target_source,
            )
            if criteria_mode not in {"all", "any"}:
                raise CaseValidationError(
                    f"{target_source}: criteria_mode must be all or any"
                )
            criteria = _target_criteria(target["criteria"], source=target_source)

        policy_payload = _object(payload["search_policy"], "search_policy", source)
        _require_fields(
            policy_payload,
            {"mode", "latest_published_at", "allowed_domains"},
            source=f"{source}: search_policy",
        )
        policy_mode = _string(
            policy_payload["mode"],
            field="mode",
            source=f"{source}: search_policy",
        )
        expected_policy = (
            "frozen_corpus_only" if mode == "historical_frozen_web" else "live_web"
        )
        if policy_mode != expected_policy:
            raise CaseValidationError(
                f"{source}: {mode} requires search_policy mode {expected_policy}"
            )
        latest = _date(
            policy_payload["latest_published_at"],
            field="latest_published_at",
            source=f"{source}: search_policy",
        )
        if latest > as_of:
            raise CaseValidationError(
                f"{source}: search cutoff {latest} is after as_of {as_of}"
            )
        domains = _string_list(
            policy_payload["allowed_domains"],
            field="allowed_domains",
            source=f"{source}: search_policy",
        )

        response_contract = _object(
            payload["response_contract"], "response_contract", source
        )
        properties = response_contract.get("properties", {})
        evidence_field = (
            "evidence_ids" if mode == "historical_frozen_web" else "evidence_urls"
        )
        required_response_fields = {
            "event_probability",
            "prediction",
            evidence_field,
            "analysis_summary",
        }
        if not required_response_fields <= set(properties):
            raise CaseValidationError(
                f"{source}: response_contract is missing required properties"
            )

        return cls(
            schema_version=schema_version,
            id=_string(payload["id"], field="id", source=source),
            suite=_string(payload["suite"], field="suite", source=source),
            mode=mode,
            security=security,
            as_of=as_of,
            window_end=window_end,
            target_event=_string(
                target["event"], field="event", source=f"{source}: target"
            ),
            target_definition=_string(
                target["definition"], field="definition", source=target_source
            ),
            criteria_mode=criteria_mode,
            criteria=criteria,
            legacy_threshold=threshold,
            legacy_denominator=denominator,
            prompt=_string(payload["prompt"], field="prompt", source=source),
            search_policy=SearchPolicy(
                mode=policy_mode,
                latest_published_at=latest,
                allowed_domains=domains,
            ),
            response_contract=response_contract,
            authoring_provenance=_object(
                payload["authoring_provenance"], "authoring_provenance", source
            ),
        )

    def agent_payload(self) -> dict[str, Any]:
        """Return the scenario without author-only provenance or outcome data."""
        if self.schema_version == 1:
            target = {
                "event": self.target_event,
                "threshold": self.legacy_threshold,
                "denominator": self.legacy_denominator,
            }
        else:
            target = {
                "event": self.target_event,
                "definition": self.target_definition,
                "criteria_mode": self.criteria_mode,
                "criteria": [criterion.to_dict() for criterion in self.criteria],
            }
        search_name = (
            "frozen_search"
            if self.search_policy.mode == "frozen_corpus_only"
            else "live_web_search"
        )
        return {
            "scenario_id": self.id,
            "suite": self.suite,
            "mode": self.mode,
            "security": asdict(self.security),
            "as_of": self.as_of.isoformat(),
            "prediction_window_end": self.window_end.isoformat(),
            "target": target,
            "prompt": self.prompt,
            "search_tool": {
                "name": search_name,
                "policy": self.search_policy.mode,
                "latest_published_at": (
                    self.search_policy.latest_published_at.isoformat()
                ),
                "allowed_domains": list(self.search_policy.allowed_domains),
            },
            "response_contract": self.response_contract,
        }


def validate_realized_outcome(
    scenario: WalkForwardScenario,
    realized: dict[str, Any],
    *,
    event_occurred: bool,
    source: str = "<memory>",
) -> dict[str, float]:
    """Recompute realized metrics and require the event to match the scenario."""
    if not isinstance(event_occurred, bool):
        raise CaseValidationError(f"{source}: event_occurred must be boolean")
    if scenario.schema_version == 1:
        metrics = _legacy_realized_metrics(realized, source=source)
    else:
        metrics = _generic_realized_metrics(realized, source=source)
    criterion_results = [
        _criterion_matches(criterion, metrics, source=source)
        for criterion in scenario.criteria
    ]
    calculated_event = (
        all(criterion_results)
        if scenario.criteria_mode == "all"
        else any(criterion_results)
    )
    if event_occurred != calculated_event:
        raise CaseValidationError(
            f"{source}: event label disagrees with target criteria"
        )
    return metrics


def _legacy_realized_metrics(
    realized: dict[str, Any], *, source: str
) -> dict[str, float]:
    realized_source = f"{source}: realized"
    _require_fields(
        realized,
        {"asset_impairment_loss", "pre_as_of_equity", "ratio"},
        realized_source,
    )
    loss = _non_negative_number(
        realized["asset_impairment_loss"],
        field="asset_impairment_loss",
        source=realized_source,
    )
    equity = _positive_number(
        realized["pre_as_of_equity"],
        field="pre_as_of_equity",
        source=realized_source,
    )
    ratio = _non_negative_number(
        realized["ratio"], field="ratio", source=realized_source
    )
    calculated = loss / equity
    if not math.isclose(ratio, calculated, rel_tol=1e-8, abs_tol=1e-10):
        raise CaseValidationError(
            f"{source}: realized ratio does not equal loss / equity"
        )
    return {
        "asset_impairment_loss": loss,
        "pre_as_of_equity": equity,
        "asset_impairment_ratio": ratio,
    }


def _generic_realized_metrics(
    realized: dict[str, Any], *, source: str
) -> dict[str, float]:
    realized_source = f"{source}: realized"
    _require_fields(realized, {"observations", "derivations"}, realized_source)
    raw_observations = _object(
        realized["observations"], "observations", realized_source
    )
    metrics = {
        _metric_name(name, source=f"{realized_source}: observations"): _number(
            value,
            field=str(name),
            source=f"{realized_source}: observations",
        )
        for name, value in raw_observations.items()
    }
    raw_derivations = realized["derivations"]
    if not isinstance(raw_derivations, list):
        raise CaseValidationError(f"{realized_source}: derivations must be a list")
    for index, raw in enumerate(raw_derivations):
        item_source = f"{realized_source}: derivations[{index}]"
        item = _object(raw, "derivation", item_source)
        _require_fields(
            item,
            {"metric", "operation", "inputs", "value"},
            item_source,
        )
        metric = _metric_name(item["metric"], source=item_source)
        if metric in metrics:
            raise CaseValidationError(f"{item_source}: duplicate metric {metric!r}")
        inputs = _string_list(item["inputs"], field="inputs", source=item_source)
        unknown = sorted(set(inputs) - metrics.keys())
        if unknown:
            raise CaseValidationError(
                f"{item_source}: unknown input metrics: {', '.join(unknown)}"
            )
        operation = _string(item["operation"], field="operation", source=item_source)
        calculated = _calculate_derivation(
            operation,
            [metrics[name] for name in inputs],
            item,
            source=item_source,
        )
        stated = _number(item["value"], field="value", source=item_source)
        if not math.isclose(stated, calculated, rel_tol=1e-8, abs_tol=1e-10):
            raise CaseValidationError(
                f"{item_source}: value does not match {operation} calculation"
            )
        metrics[metric] = stated
    return metrics


def _calculate_derivation(
    operation: str,
    inputs: list[float],
    payload: dict[str, Any],
    *,
    source: str,
) -> float:
    if operation == "ratio":
        _require_input_count(inputs, 2, operation, source)
        if inputs[1] == 0:
            raise CaseValidationError(f"{source}: ratio denominator must be nonzero")
        return inputs[0] / inputs[1]
    if operation == "margin":
        _require_input_count(inputs, 2, operation, source)
        if inputs[0] == 0:
            raise CaseValidationError(f"{source}: margin revenue must be nonzero")
        return (inputs[0] - inputs[1]) / inputs[0]
    if operation == "difference":
        _require_input_count(inputs, 2, operation, source)
        return inputs[0] - inputs[1]
    if operation == "pct_change":
        _require_input_count(inputs, 2, operation, source)
        if inputs[0] == 0:
            raise CaseValidationError(
                f"{source}: pct_change starting value must be nonzero"
            )
        return inputs[1] / inputs[0] - 1
    if operation == "cagr":
        _require_input_count(inputs, 2, operation, source)
        periods = _positive_number(
            payload.get("periods"), field="periods", source=source
        )
        if inputs[0] <= 0 or inputs[1] < 0:
            raise CaseValidationError(
                f"{source}: cagr requires a positive start and non-negative end"
            )
        return (inputs[1] / inputs[0]) ** (1 / periods) - 1
    raise CaseValidationError(f"{source}: unsupported operation {operation!r}")


def _require_input_count(
    inputs: list[float], expected: int, operation: str, source: str
) -> None:
    if len(inputs) != expected:
        raise CaseValidationError(
            f"{source}: {operation} requires exactly {expected} inputs"
        )


def _criterion_matches(
    criterion: TargetCriterion,
    metrics: dict[str, float],
    *,
    source: str,
) -> bool:
    if criterion.metric not in metrics:
        raise CaseValidationError(
            f"{source}: realized metrics are missing {criterion.metric!r}"
        )
    actual = metrics[criterion.metric]
    expected = criterion.value
    return {
        ">": actual > expected,
        ">=": actual >= expected,
        "<": actual < expected,
        "<=": actual <= expected,
        "==": math.isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-12),
    }[criterion.comparison]


def _target_criteria(value: Any, *, source: str) -> tuple[TargetCriterion, ...]:
    if not isinstance(value, list) or not value:
        raise CaseValidationError(f"{source}: criteria must be a non-empty list")
    criteria = []
    for index, raw in enumerate(value):
        item_source = f"{source}: criteria[{index}]"
        item = _object(raw, "criterion", item_source)
        _require_fields(
            item,
            {"metric", "comparison", "value", "description"},
            item_source,
        )
        comparison = _string(item["comparison"], field="comparison", source=item_source)
        if comparison not in {">", ">=", "<", "<=", "=="}:
            raise CaseValidationError(
                f"{item_source}: unsupported comparison {comparison!r}"
            )
        criteria.append(
            TargetCriterion(
                metric=_metric_name(item["metric"], source=item_source),
                comparison=comparison,
                value=_number(item["value"], field="value", source=item_source),
                description=_string(
                    item["description"], field="description", source=item_source
                ),
            )
        )
    signatures = ((item.metric, item.comparison, item.value) for item in criteria)
    _unique(signatures, "criteria", source)
    return tuple(criteria)


def _metric_name(value: Any, *, source: str) -> str:
    metric = _string(value, field="metric", source=source)
    if not re.fullmatch(r"[a-z][a-z0-9_]*", metric):
        raise CaseValidationError(f"{source}: metric must use lowercase snake_case")
    return metric


def _require_fields(payload: dict[str, Any], required: set[str], source: str) -> None:
    missing = sorted(required - payload.keys())
    if missing:
        raise CaseValidationError(f"{source}: missing fields: {', '.join(missing)}")


def _object(value: Any, field: str, source: str) -> dict[str, Any]:
    if not isinstance(value, dict) or not value:
        raise CaseValidationError(f"{source}: {field} must be a non-empty object")
    return value


def _string(value: Any, *, field: str, source: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CaseValidationError(f"{source}: {field} must be a non-empty string")
    return value.strip()


def _string_list(value: Any, *, field: str, source: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not value:
        raise CaseValidationError(f"{source}: {field} must be a non-empty list")
    items = tuple(_string(item, field=f"{field} item", source=source) for item in value)
    _unique(items, field, source)
    return items


def _date(value: Any, *, field: str, source: str) -> date:
    raw = _string(value, field=field, source=source)
    try:
        return date.fromisoformat(raw)
    except ValueError as error:
        raise CaseValidationError(f"{source}: {field} must be YYYY-MM-DD") from error


def _number(value: Any, *, field: str, source: str) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise CaseValidationError(f"{source}: {field} must be numeric")
    result = float(value)
    if not math.isfinite(result):
        raise CaseValidationError(f"{source}: {field} must be finite")
    return result


def _non_negative_number(value: Any, *, field: str, source: str) -> float:
    result = _number(value, field=field, source=source)
    if result < 0:
        raise CaseValidationError(f"{source}: {field} must be non-negative")
    return result


def _positive_number(value: Any, *, field: str, source: str) -> float:
    result = _number(value, field=field, source=source)
    if result <= 0:
        raise CaseValidationError(f"{source}: {field} must be positive")
    return result


def _probability(value: Any, *, field: str, source: str) -> float:
    result = _number(value, field=field, source=source)
    if not 0 <= result <= 1:
        raise CaseValidationError(f"{source}: {field} must be between 0 and 1")
    return result


def _unique(values: Any, field: str, source: str) -> None:
    items = list(values)
    if len(items) != len(set(items)):
        raise CaseValidationError(f"{source}: {field} must be unique")

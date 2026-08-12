"""Point-in-time A-share walk-forward scenarios and probabilistic scoring."""

from __future__ import annotations

import json
import math
import re
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from finagentbench.case import CaseValidationError


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
class WalkForwardScenario:
    id: str
    suite: str
    mode: str
    security: Security
    as_of: date
    window_end: date
    target_event: str
    threshold: float
    denominator: str
    prompt: str
    search_policy: SearchPolicy
    response_contract: dict[str, Any]
    authoring_provenance: dict[str, Any]

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
        if payload["schema_version"] != 1:
            raise CaseValidationError(f"{source}: schema_version must be 1")

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
        _require_fields(
            target,
            {"event", "threshold", "denominator", "definition"},
            source=f"{source}: target",
        )
        threshold = _probability(
            target["threshold"], field="threshold", source=f"{source}: target"
        )
        if threshold == 0:
            raise CaseValidationError(f"{source}: target threshold must be positive")

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
        required_response_fields = {
            "event_probability",
            "prediction",
            "evidence_ids",
            "analysis_summary",
        }
        if not required_response_fields <= set(properties):
            raise CaseValidationError(
                f"{source}: response_contract is missing required properties"
            )

        return cls(
            id=_string(payload["id"], field="id", source=source),
            suite=_string(payload["suite"], field="suite", source=source),
            mode=mode,
            security=security,
            as_of=as_of,
            window_end=window_end,
            target_event=_string(
                target["event"], field="event", source=f"{source}: target"
            ),
            threshold=threshold,
            denominator=_string(
                target["denominator"],
                field="denominator",
                source=f"{source}: target",
            ),
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
        return {
            "scenario_id": self.id,
            "suite": self.suite,
            "mode": self.mode,
            "security": asdict(self.security),
            "as_of": self.as_of.isoformat(),
            "prediction_window_end": self.window_end.isoformat(),
            "target": {
                "event": self.target_event,
                "threshold": self.threshold,
                "denominator": self.denominator,
            },
            "prompt": self.prompt,
            "search_tool": {
                "name": "frozen_search",
                "policy": self.search_policy.mode,
                "latest_published_at": (
                    self.search_policy.latest_published_at.isoformat()
                ),
                "allowed_domains": list(self.search_policy.allowed_domains),
            },
            "response_contract": self.response_contract,
        }


@dataclass(frozen=True)
class FrozenDocument:
    id: str
    title: str
    published_at: date
    source: str
    url: str
    content: str


@dataclass(frozen=True)
class FrozenCorpus:
    scenario_id: str
    documents: tuple[FrozenDocument, ...]

    @classmethod
    def from_dict(
        cls,
        payload: dict[str, Any],
        *,
        scenario: WalkForwardScenario,
        source: str = "<memory>",
    ) -> FrozenCorpus:
        _require_fields(payload, {"schema_version", "scenario_id", "documents"}, source)
        if payload["schema_version"] != 1:
            raise CaseValidationError(f"{source}: schema_version must be 1")
        scenario_id = _string(
            payload["scenario_id"], field="scenario_id", source=source
        )
        if scenario_id != scenario.id:
            raise CaseValidationError(
                f"{source}: corpus scenario_id does not match {scenario.id}"
            )
        raw_documents = payload["documents"]
        if not isinstance(raw_documents, list) or not raw_documents:
            raise CaseValidationError(f"{source}: documents must be a non-empty list")
        documents = []
        for index, raw in enumerate(raw_documents):
            item_source = f"{source}: documents[{index}]"
            document = _object(raw, "document", item_source)
            _require_fields(
                document,
                {"id", "title", "published_at", "source", "url", "content"},
                item_source,
            )
            published_at = _date(
                document["published_at"],
                field="published_at",
                source=item_source,
            )
            if published_at > scenario.search_policy.latest_published_at:
                raise CaseValidationError(
                    f"{item_source}: document leaks past search cutoff"
                )
            url = _string(document["url"], field="url", source=item_source)
            host = (urlparse(url).hostname or "").lower()
            if not any(
                host == domain or host.endswith(f".{domain}")
                for domain in scenario.search_policy.allowed_domains
            ):
                raise CaseValidationError(
                    f"{item_source}: URL domain {host!r} is not allowlisted"
                )
            documents.append(
                FrozenDocument(
                    id=_string(document["id"], field="id", source=item_source),
                    title=_string(
                        document["title"], field="title", source=item_source
                    ),
                    published_at=published_at,
                    source=_string(
                        document["source"], field="source", source=item_source
                    ),
                    url=url,
                    content=_string(
                        document["content"], field="content", source=item_source
                    ),
                )
            )
        _unique((item.id for item in documents), "document IDs", source)
        return cls(scenario_id=scenario_id, documents=tuple(documents))

    def search(self, query: str, *, limit: int = 5) -> list[dict[str, Any]]:
        """Search the frozen corpus with a deterministic lexical ranker."""
        query = _string(query, field="query", source="search")
        if limit <= 0:
            raise CaseValidationError("search: limit must be positive")
        needles = _search_terms(query)
        matches = []
        for document in self.documents:
            haystack = f"{document.title}\n{document.content}".lower()
            score = sum(haystack.count(term) * len(term) for term in needles)
            if score <= 0:
                continue
            position = min(
                (haystack.find(term) for term in needles if term in haystack),
                default=0,
            )
            start = max(0, position - 90)
            end = min(len(haystack), position + 310)
            matches.append(
                {
                    "id": document.id,
                    "title": document.title,
                    "published_at": document.published_at.isoformat(),
                    "source": document.source,
                    "url": document.url,
                    "snippet": haystack[start:end].strip(),
                    "score": score,
                }
            )
        matches.sort(key=lambda item: (-item["score"], item["id"]))
        return matches[:limit]


@dataclass(frozen=True)
class WalkForwardLabel:
    scenario_id: str
    resolved_at: date
    event_occurred: bool
    impairment_loss: float
    pre_as_of_equity: float
    realized_ratio: float
    expected_evidence_ids: tuple[str, ...]
    outcome_sources: tuple[dict[str, Any], ...]

    @classmethod
    def from_dict(
        cls,
        payload: dict[str, Any],
        *,
        scenario: WalkForwardScenario,
        corpus: FrozenCorpus,
        source: str = "<memory>",
    ) -> WalkForwardLabel:
        required = {
            "schema_version",
            "scenario_id",
            "resolved_at",
            "event_occurred",
            "realized",
            "expected_evidence_ids",
            "outcome_sources",
        }
        _require_fields(payload, required, source)
        if payload["schema_version"] != 1:
            raise CaseValidationError(f"{source}: schema_version must be 1")
        scenario_id = _string(
            payload["scenario_id"], field="scenario_id", source=source
        )
        if scenario_id != scenario.id or scenario_id != corpus.scenario_id:
            raise CaseValidationError(f"{source}: label scenario_id mismatch")
        resolved_at = _date(
            payload["resolved_at"], field="resolved_at", source=source
        )
        if not scenario.as_of < resolved_at <= scenario.window_end:
            raise CaseValidationError(
                f"{source}: resolved_at must be inside the prediction window"
            )
        event_occurred = payload["event_occurred"]
        if not isinstance(event_occurred, bool):
            raise CaseValidationError(f"{source}: event_occurred must be boolean")
        realized = _object(payload["realized"], "realized", source)
        _require_fields(
            realized,
            {"asset_impairment_loss", "pre_as_of_equity", "ratio"},
            f"{source}: realized",
        )
        loss = _non_negative_number(
            realized["asset_impairment_loss"],
            field="asset_impairment_loss",
            source=f"{source}: realized",
        )
        equity = _positive_number(
            realized["pre_as_of_equity"],
            field="pre_as_of_equity",
            source=f"{source}: realized",
        )
        ratio = _non_negative_number(
            realized["ratio"], field="ratio", source=f"{source}: realized"
        )
        calculated = loss / equity
        if not math.isclose(ratio, calculated, rel_tol=1e-8, abs_tol=1e-10):
            raise CaseValidationError(
                f"{source}: realized ratio does not equal loss / equity"
            )
        if event_occurred != (ratio > scenario.threshold):
            raise CaseValidationError(
                f"{source}: event label disagrees with target threshold"
            )
        expected = _string_list(
            payload["expected_evidence_ids"],
            field="expected_evidence_ids",
            source=source,
        )
        unknown = sorted(set(expected) - {item.id for item in corpus.documents})
        if unknown:
            raise CaseValidationError(
                f"{source}: unknown expected evidence IDs: {', '.join(unknown)}"
            )
        sources = payload["outcome_sources"]
        if not isinstance(sources, list) or not sources:
            raise CaseValidationError(
                f"{source}: outcome_sources must be a non-empty list"
            )
        if any(not isinstance(item, dict) or not item for item in sources):
            raise CaseValidationError(
                f"{source}: outcome_sources items must be non-empty objects"
            )
        return cls(
            scenario_id=scenario_id,
            resolved_at=resolved_at,
            event_occurred=event_occurred,
            impairment_loss=loss,
            pre_as_of_equity=equity,
            realized_ratio=ratio,
            expected_evidence_ids=expected,
            outcome_sources=tuple(sources),
        )


@dataclass(frozen=True)
class WalkForwardScore:
    total: float
    brier_score: float
    brier_loss: float
    log_loss: float
    evidence_f1: float
    classification_correct: bool

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class WalkForwardCase:
    scenario: WalkForwardScenario
    corpus: FrozenCorpus
    label: WalkForwardLabel


def score_walkforward_submission(
    case: WalkForwardCase, submission: dict[str, Any]
) -> WalkForwardScore:
    """Score a probabilistic prediction; explanation text is retained for review."""
    if not isinstance(submission, dict):
        raise CaseValidationError("submission must be a JSON object")
    required = {
        "event_probability",
        "prediction",
        "evidence_ids",
        "analysis_summary",
    }
    _require_fields(submission, required, source="submission")
    probability = _probability(
        submission["event_probability"],
        field="event_probability",
        source="submission",
    )
    prediction = submission["prediction"]
    if prediction not in {"event", "no_event"}:
        raise CaseValidationError("submission: prediction must be event or no_event")
    implied = "event" if probability >= 0.5 else "no_event"
    if prediction != implied:
        raise CaseValidationError(
            "submission: prediction must agree with the 0.5 probability threshold"
        )
    evidence_ids = _string_list(
        submission["evidence_ids"], field="evidence_ids", source="submission"
    )
    unknown = sorted(
        set(evidence_ids) - {item.id for item in case.corpus.documents}
    )
    if unknown:
        raise CaseValidationError(
            f"submission: unknown evidence IDs: {', '.join(unknown)}"
        )
    _string(
        submission["analysis_summary"],
        field="analysis_summary",
        source="submission",
    )
    observed = float(case.label.event_occurred)
    brier_loss = (probability - observed) ** 2
    brier_score = 100 * (1 - brier_loss)
    clipped = min(max(probability, 1e-15), 1 - 1e-15)
    log_loss = -(
        observed * math.log(clipped) + (1 - observed) * math.log(1 - clipped)
    )
    evidence_f1 = _f1(set(evidence_ids), set(case.label.expected_evidence_ids))
    total = 0.85 * brier_score + 15 * evidence_f1
    expected_prediction = "event" if case.label.event_occurred else "no_event"
    return WalkForwardScore(
        total=round(total, 6),
        brier_score=round(brier_score, 6),
        brier_loss=round(brier_loss, 8),
        log_loss=round(log_loss, 8),
        evidence_f1=round(evidence_f1, 6),
        classification_correct=prediction == expected_prediction,
    )


def load_walkforward_suite(
    scenario_dir: Path, corpus_dir: Path, label_dir: Path
) -> tuple[WalkForwardCase, ...]:
    scenario_paths = _json_paths(scenario_dir, "scenario")
    corpus_paths = {path.stem: path for path in _json_paths(corpus_dir, "corpus")}
    label_paths = {path.stem: path for path in _json_paths(label_dir, "label")}
    cases = []
    for scenario_path in scenario_paths:
        scenario = WalkForwardScenario.from_dict(
            _read_object(scenario_path), source=str(scenario_path)
        )
        corpus_path = corpus_paths.pop(scenario.id, None)
        label_path = label_paths.pop(scenario.id, None)
        if corpus_path is None or label_path is None:
            raise CaseValidationError(
                f"{scenario_path}: matching corpus and label are required"
            )
        corpus = FrozenCorpus.from_dict(
            _read_object(corpus_path), scenario=scenario, source=str(corpus_path)
        )
        label = WalkForwardLabel.from_dict(
            _read_object(label_path),
            scenario=scenario,
            corpus=corpus,
            source=str(label_path),
        )
        cases.append(WalkForwardCase(scenario=scenario, corpus=corpus, label=label))
    _unique((case.scenario.id for case in cases), "scenario IDs", str(scenario_dir))
    if corpus_paths or label_paths:
        extras = sorted(set(corpus_paths) | set(label_paths))
        raise CaseValidationError(
            f"orphan corpus/label files without scenarios: {', '.join(extras)}"
        )
    return tuple(cases)


def _read_object(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise CaseValidationError(f"{path}: invalid JSON: {error}") from error
    if not isinstance(payload, dict):
        raise CaseValidationError(f"{path}: top-level value must be an object")
    return payload


def _json_paths(directory: Path, kind: str) -> list[Path]:
    if not directory.is_dir():
        raise CaseValidationError(f"{kind} directory does not exist: {directory}")
    paths = sorted(directory.glob("*.json"))
    if not paths:
        raise CaseValidationError(f"{kind} directory contains no JSON: {directory}")
    return paths


def _search_terms(query: str) -> set[str]:
    normalized = re.sub(r"\s+", " ", query.lower()).strip()
    terms = {part for part in re.split(r"[^\w\u4e00-\u9fff]+", normalized) if part}
    compact = re.sub(r"[^\w\u4e00-\u9fff]", "", normalized)
    if len(compact) >= 2:
        terms.update(compact[index : index + 2] for index in range(len(compact) - 1))
    return terms


def _f1(predicted: set[str], expected: set[str]) -> float:
    if not predicted and not expected:
        return 1.0
    if not predicted or not expected:
        return 0.0
    true_positives = len(predicted & expected)
    precision = true_positives / len(predicted)
    recall = true_positives / len(expected)
    return 2 * precision * recall / (precision + recall)


def _require_fields(
    payload: dict[str, Any], required: set[str], source: str
) -> None:
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
    items = tuple(
        _string(item, field=f"{field} item", source=source) for item in value
    )
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

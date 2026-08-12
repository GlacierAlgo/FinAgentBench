"""Case loading and validation for FinAgentBench."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


class CaseValidationError(ValueError):
    """Raised when a benchmark case violates the public case contract."""


@dataclass(frozen=True)
class EvidenceItem:
    id: str
    text: str
    observed_at: date
    source: str


@dataclass(frozen=True)
class RubricItem:
    id: str
    description: str
    weight: int


@dataclass(frozen=True)
class AnswerKey:
    prediction: str
    premise_assessment: str
    evidence_ids: tuple[str, ...]


@dataclass(frozen=True)
class BenchmarkCase:
    id: str
    title: str
    category: str
    jurisdiction: str
    as_of: date
    prediction_horizon: str
    prompt: str
    evidence: tuple[EvidenceItem, ...]
    response_contract: dict[str, Any]
    rubric: tuple[RubricItem, ...]
    answer_key: AnswerKey

    @classmethod
    def from_dict(
        cls, payload: dict[str, Any], *, source: str = "<memory>"
    ) -> BenchmarkCase:
        required = {
            "id",
            "title",
            "category",
            "jurisdiction",
            "as_of",
            "prediction_horizon",
            "prompt",
            "evidence",
            "response_contract",
            "rubric",
            "answer_key",
        }
        missing = sorted(required - payload.keys())
        if missing:
            raise CaseValidationError(f"{source}: missing fields: {', '.join(missing)}")

        case_id = _non_empty_string(payload["id"], field="id", source=source)
        as_of = _iso_date(payload["as_of"], field="as_of", source=source)

        raw_evidence = payload["evidence"]
        if not isinstance(raw_evidence, list) or not raw_evidence:
            raise CaseValidationError(f"{source}: evidence must be a non-empty list")

        evidence: list[EvidenceItem] = []
        for index, item in enumerate(raw_evidence):
            item_source = f"{source}: evidence[{index}]"
            if not isinstance(item, dict):
                raise CaseValidationError(f"{item_source} must be an object")
            observed_at = _iso_date(
                item.get("observed_at"), field="observed_at", source=item_source
            )
            if observed_at > as_of:
                raise CaseValidationError(
                    f"{item_source}: observed_at {observed_at} is after as_of {as_of}"
                )
            evidence.append(
                EvidenceItem(
                    id=_non_empty_string(
                        item.get("id"), field="id", source=item_source
                    ),
                    text=_non_empty_string(
                        item.get("text"), field="text", source=item_source
                    ),
                    observed_at=observed_at,
                    source=_non_empty_string(
                        item.get("source"), field="source", source=item_source
                    ),
                )
            )

        _ensure_unique(
            (item.id for item in evidence), field="evidence IDs", source=source
        )

        response_contract = payload["response_contract"]
        if not isinstance(response_contract, dict) or not response_contract:
            raise CaseValidationError(
                f"{source}: response_contract must be a non-empty object"
            )

        raw_answer_key = payload["answer_key"]
        if not isinstance(raw_answer_key, dict):
            raise CaseValidationError(f"{source}: answer_key must be an object")
        prediction = _non_empty_string(
            raw_answer_key.get("prediction"),
            field="prediction",
            source=f"{source}: answer_key",
        )
        allowed_predictions = (
            response_contract.get("properties", {})
            .get("prediction", {})
            .get("enum", [])
        )
        if prediction not in allowed_predictions:
            raise CaseValidationError(
                f"{source}: answer_key prediction is not allowed by response_contract"
            )
        premise_assessment = _non_empty_string(
            raw_answer_key.get("premise_assessment"),
            field="premise_assessment",
            source=f"{source}: answer_key",
        )
        if premise_assessment not in {"valid", "partly_valid", "invalid"}:
            raise CaseValidationError(
                f"{source}: answer_key premise_assessment must be valid, partly_valid, or invalid"
            )
        raw_expected_evidence = raw_answer_key.get("evidence_ids")
        if not isinstance(raw_expected_evidence, list) or not raw_expected_evidence:
            raise CaseValidationError(
                f"{source}: answer_key evidence_ids must be a non-empty list"
            )
        expected_evidence_ids = tuple(
            _non_empty_string(
                item, field="evidence_ids item", source=f"{source}: answer_key"
            )
            for item in raw_expected_evidence
        )
        _ensure_unique(
            expected_evidence_ids, field="answer_key evidence_ids", source=source
        )
        unknown_evidence = sorted(
            set(expected_evidence_ids) - {item.id for item in evidence}
        )
        if unknown_evidence:
            raise CaseValidationError(
                f"{source}: answer_key references unknown evidence: {', '.join(unknown_evidence)}"
            )

        raw_rubric = payload["rubric"]
        if not isinstance(raw_rubric, list) or not raw_rubric:
            raise CaseValidationError(f"{source}: rubric must be a non-empty list")

        rubric: list[RubricItem] = []
        for index, item in enumerate(raw_rubric):
            item_source = f"{source}: rubric[{index}]"
            if not isinstance(item, dict):
                raise CaseValidationError(f"{item_source} must be an object")
            weight = item.get("weight")
            if not isinstance(weight, int) or isinstance(weight, bool) or weight <= 0:
                raise CaseValidationError(
                    f"{item_source}: weight must be a positive integer"
                )
            rubric.append(
                RubricItem(
                    id=_non_empty_string(
                        item.get("id"), field="id", source=item_source
                    ),
                    description=_non_empty_string(
                        item.get("description"), field="description", source=item_source
                    ),
                    weight=weight,
                )
            )

        _ensure_unique((item.id for item in rubric), field="rubric IDs", source=source)
        rubric_weight = sum(item.weight for item in rubric)
        if rubric_weight != 100:
            raise CaseValidationError(
                f"{source}: rubric weights must total 100, got {rubric_weight}"
            )

        return cls(
            id=case_id,
            title=_non_empty_string(payload["title"], field="title", source=source),
            category=_non_empty_string(
                payload["category"], field="category", source=source
            ),
            jurisdiction=_non_empty_string(
                payload["jurisdiction"], field="jurisdiction", source=source
            ),
            as_of=as_of,
            prediction_horizon=_non_empty_string(
                payload["prediction_horizon"],
                field="prediction_horizon",
                source=source,
            ),
            prompt=_non_empty_string(payload["prompt"], field="prompt", source=source),
            evidence=tuple(evidence),
            response_contract=response_contract,
            rubric=tuple(rubric),
            answer_key=AnswerKey(
                prediction=prediction,
                premise_assessment=premise_assessment,
                evidence_ids=expected_evidence_ids,
            ),
        )

    def agent_payload(self) -> dict[str, Any]:
        """Return only information the evaluated agent is allowed to see."""
        return {
            "case_id": self.id,
            "title": self.title,
            "category": self.category,
            "jurisdiction": self.jurisdiction,
            "as_of": self.as_of.isoformat(),
            "prediction_horizon": self.prediction_horizon,
            "prompt": self.prompt,
            "evidence": [
                {
                    "id": item.id,
                    "text": item.text,
                    "observed_at": item.observed_at.isoformat(),
                    "source": item.source,
                }
                for item in self.evidence
            ],
            "response_contract": self.response_contract,
        }


def load_case(path: Path) -> BenchmarkCase:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise CaseValidationError(f"{path}: invalid JSON: {error}") from error
    if not isinstance(payload, dict):
        raise CaseValidationError(f"{path}: top-level JSON value must be an object")
    return BenchmarkCase.from_dict(payload, source=str(path))


def load_cases(directory: Path) -> tuple[BenchmarkCase, ...]:
    if not directory.is_dir():
        raise CaseValidationError(f"case directory does not exist: {directory}")
    paths = sorted(directory.glob("*.json"))
    if not paths:
        raise CaseValidationError(f"case directory contains no JSON cases: {directory}")
    cases = tuple(load_case(path) for path in paths)
    _ensure_unique((case.id for case in cases), field="case IDs", source=str(directory))
    return cases


def _non_empty_string(value: Any, *, field: str, source: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CaseValidationError(f"{source}: {field} must be a non-empty string")
    return value.strip()


def _iso_date(value: Any, *, field: str, source: str) -> date:
    raw = _non_empty_string(value, field=field, source=source)
    try:
        return date.fromisoformat(raw)
    except ValueError as error:
        raise CaseValidationError(f"{source}: {field} must be YYYY-MM-DD") from error


def _ensure_unique(values: Any, *, field: str, source: str) -> None:
    items = list(values)
    if len(items) != len(set(items)):
        raise CaseValidationError(f"{source}: {field} must be unique")

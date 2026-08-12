"""Deterministic contract scoring for public FinAgentBench cases."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from finagentbench.case import BenchmarkCase, CaseValidationError


@dataclass(frozen=True)
class ScoreBreakdown:
    total: float
    prediction: float
    premise: float
    evidence: float
    calibration: float
    prediction_correct: bool
    premise_correct: bool
    evidence_f1: float

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def score_submission(case: BenchmarkCase, submission: dict[str, Any]) -> ScoreBreakdown:
    """Score observable answer fields without pretending to grade hidden reasoning."""
    _validate_submission(case, submission)
    prediction_correct = submission["prediction"] == case.answer_key.prediction
    premise_correct = (
        submission["premise_assessment"] == case.answer_key.premise_assessment
    )
    evidence_f1 = _f1(
        set(submission["evidence_ids"]), set(case.answer_key.evidence_ids)
    )
    confidence = float(submission["confidence"])

    prediction_score = 40.0 if prediction_correct else 0.0
    premise_score = 25.0 if premise_correct else 0.0
    evidence_score = 25.0 * evidence_f1
    calibration_score = 10.0 * (
        1.0 - (1.0 - confidence) ** 2 if prediction_correct else 1.0 - confidence**2
    )
    total = prediction_score + premise_score + evidence_score + calibration_score

    return ScoreBreakdown(
        total=round(total, 4),
        prediction=round(prediction_score, 4),
        premise=round(premise_score, 4),
        evidence=round(evidence_score, 4),
        calibration=round(calibration_score, 4),
        prediction_correct=prediction_correct,
        premise_correct=premise_correct,
        evidence_f1=round(evidence_f1, 4),
    )


def _validate_submission(case: BenchmarkCase, submission: dict[str, Any]) -> None:
    if not isinstance(submission, dict):
        raise CaseValidationError("submission must be a JSON object")
    required = {
        "prediction",
        "confidence",
        "premise_assessment",
        "evidence_ids",
        "explanation",
    }
    missing = sorted(required - submission.keys())
    if missing:
        raise CaseValidationError(f"submission missing fields: {', '.join(missing)}")

    prediction = submission["prediction"]
    prediction_enum = (
        case.response_contract.get("properties", {})
        .get("prediction", {})
        .get("enum", [])
    )
    if prediction not in prediction_enum:
        raise CaseValidationError(
            f"submission prediction is not allowed: {prediction!r}"
        )
    if submission["premise_assessment"] not in {"valid", "partly_valid", "invalid"}:
        raise CaseValidationError("submission premise_assessment is not allowed")

    confidence = submission["confidence"]
    if (
        not isinstance(confidence, (int, float))
        or isinstance(confidence, bool)
        or not 0 <= confidence <= 1
    ):
        raise CaseValidationError("submission confidence must be between 0 and 1")

    evidence_ids = submission["evidence_ids"]
    if not isinstance(evidence_ids, list) or any(
        not isinstance(item, str) for item in evidence_ids
    ):
        raise CaseValidationError("submission evidence_ids must be a list of strings")
    if len(evidence_ids) != len(set(evidence_ids)):
        raise CaseValidationError("submission evidence_ids must be unique")
    unknown = sorted(set(evidence_ids) - {item.id for item in case.evidence})
    if unknown:
        raise CaseValidationError(
            f"submission references unknown evidence: {', '.join(unknown)}"
        )
    explanation = submission["explanation"]
    if not isinstance(explanation, str) or not explanation.strip():
        raise CaseValidationError("submission explanation must be a non-empty string")


def _f1(predicted: set[str], expected: set[str]) -> float:
    if not predicted and not expected:
        return 1.0
    if not predicted or not expected:
        return 0.0
    true_positives = len(predicted & expected)
    precision = true_positives / len(predicted)
    recall = true_positives / len(expected)
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)

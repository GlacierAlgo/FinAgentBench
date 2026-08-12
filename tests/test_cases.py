import json

import pytest

from finagentbench.case import BenchmarkCase, CaseValidationError, load_cases
from finagentbench.cli import BUILTIN_CASES
from finagentbench.scoring import score_submission


def test_builtin_cases_are_valid_and_unique() -> None:
    cases = load_cases(BUILTIN_CASES)

    assert len(cases) == 12
    assert len({case.id for case in cases}) == len(cases)


def test_agent_payload_never_exposes_rubric() -> None:
    case = load_cases(BUILTIN_CASES)[0]

    rendered = json.dumps(case.agent_payload())

    assert "rubric" not in rendered
    assert "answer_key" not in rendered
    assert "reject-false-depreciation-premise" not in rendered


def test_perfect_structured_answer_scores_100() -> None:
    case = next(
        item
        for item in load_cases(BUILTIN_CASES)
        if item.id == "goodwill-impairment-risk"
    )
    submission = {
        "prediction": case.answer_key.prediction,
        "confidence": 1.0,
        "premise_assessment": case.answer_key.premise_assessment,
        "evidence_ids": list(case.answer_key.evidence_ids),
        "explanation": "The supplied evidence supports the keyed conclusion.",
    }

    score = score_submission(case, submission)

    assert score.total == 100
    assert score.evidence_f1 == 1


def test_irrelevant_evidence_reduces_score() -> None:
    case = next(
        item
        for item in load_cases(BUILTIN_CASES)
        if item.id == "goodwill-impairment-risk"
    )
    submission = {
        "prediction": case.answer_key.prediction,
        "confidence": 1.0,
        "premise_assessment": case.answer_key.premise_assessment,
        "evidence_ids": [*case.answer_key.evidence_ids, "dividend-policy"],
        "explanation": "The supplied evidence supports the keyed conclusion.",
    }

    score = score_submission(case, submission)

    assert score.total < 100
    assert score.evidence_f1 < 1


def test_future_evidence_is_rejected() -> None:
    payload = {
        "id": "future-leak",
        "title": "Future leak",
        "category": "pit",
        "jurisdiction": "test",
        "as_of": "2025-01-01",
        "prediction_horizon": "one day",
        "prompt": "Predict an outcome.",
        "evidence": [
            {
                "id": "leak",
                "text": "This fact arrived too late.",
                "observed_at": "2025-01-02",
                "source": "test fixture",
            }
        ],
        "response_contract": {"type": "object"},
        "rubric": [{"id": "pit", "description": "No leakage.", "weight": 100}],
        "answer_key": {
            "prediction": "high",
            "premise_assessment": "valid",
            "evidence_ids": ["leak"],
        },
    }

    with pytest.raises(CaseValidationError, match="is after as_of"):
        BenchmarkCase.from_dict(payload)

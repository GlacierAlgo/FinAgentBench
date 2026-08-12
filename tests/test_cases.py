import json

import pytest

from finagentbench.case import BenchmarkCase, CaseValidationError, load_cases
from finagentbench.cli import BUILTIN_CASES


def test_builtin_cases_are_valid_and_unique() -> None:
    cases = load_cases(BUILTIN_CASES)

    assert cases
    assert len({case.id for case in cases}) == len(cases)


def test_agent_payload_never_exposes_rubric() -> None:
    case = load_cases(BUILTIN_CASES)[0]

    rendered = json.dumps(case.agent_payload())

    assert "rubric" not in rendered
    assert "reject-false-depreciation-premise" not in rendered


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
                "source": "test fixture"
            }
        ],
        "response_contract": {"type": "object"},
        "rubric": [{"id": "pit", "description": "No leakage.", "weight": 100}]
    }

    with pytest.raises(CaseValidationError, match="is after as_of"):
        BenchmarkCase.from_dict(payload)


import pytest

from pitfall.errors import CaseValidationError
from pitfall.evaluation import (
    JUDGE_MODEL,
    JUDGE_REASONING_EFFORT,
    EvaluationClass,
    parse_evaluation,
)


def test_judge_runtime_is_pinned() -> None:
    assert JUDGE_MODEL == "gpt-5.6-sol"
    assert JUDGE_REASONING_EFFORT == "xhigh"


def test_evaluation_classes_are_exactly_the_six_public_classes() -> None:
    assert {item.value for item in EvaluationClass} == {
        "completely_correct",
        "numeric_factual_error",
        "non_numeric_factual_error",
        "analysis_assumption_error",
        "analysis_logic_error",
        "other_error",
    }


@pytest.mark.parametrize("classification", list(EvaluationClass))
def test_each_public_class_parses(classification: EvaluationClass) -> None:
    result = parse_evaluation(
        f"Class: {classification.value}\n\nThis is the decisive reason.\n"
    )

    assert result.classification is classification
    assert result.decisive_reason == "This is the decisive reason."


@pytest.mark.parametrize(
    "markdown",
    [
        "Class: seventh_class\n\nReason.",
        "completely_correct\n\nReason.",
        "Class: completely_correct",
    ],
)
def test_invalid_evaluation_is_rejected(markdown: str) -> None:
    with pytest.raises(CaseValidationError):
        parse_evaluation(markdown)

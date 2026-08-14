"""Six-class answer evaluation contract."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from pitfall.errors import CaseValidationError


class EvaluationClass(StrEnum):
    COMPLETELY_CORRECT = "completely_correct"
    NUMERIC_FACTUAL_ERROR = "numeric_factual_error"
    NON_NUMERIC_FACTUAL_ERROR = "non_numeric_factual_error"
    ANALYSIS_ASSUMPTION_ERROR = "analysis_assumption_error"
    ANALYSIS_LOGIC_ERROR = "analysis_logic_error"
    OTHER_ERROR = "other_error"


@dataclass(frozen=True)
class Evaluation:
    classification: EvaluationClass
    decisive_reason: str


def parse_evaluation(markdown: str) -> Evaluation:
    """Parse the intentionally small judge output contract."""
    normalized = markdown.replace("\r\n", "\n").strip()
    lines = normalized.splitlines()
    if not lines or not lines[0].startswith("Class: "):
        raise CaseValidationError("evaluation must start with 'Class: <class>'")
    raw_class = lines[0].removeprefix("Class: ").strip()
    try:
        classification = EvaluationClass(raw_class)
    except ValueError as error:
        allowed = ", ".join(item.value for item in EvaluationClass)
        raise CaseValidationError(
            f"unknown evaluation class {raw_class!r}; allowed: {allowed}"
        ) from error
    reason = "\n".join(lines[1:]).strip()
    if not reason:
        raise CaseValidationError("evaluation requires a decisive reason")
    return Evaluation(classification=classification, decisive_reason=reason)

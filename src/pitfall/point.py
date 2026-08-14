"""Minimal Markdown datapoints for PITFALL."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from pitfall.errors import CaseValidationError

SECTION_TITLES = ("Question", "Ground Truth", "Provenance")
TEMPLATE_NAME = "META.md"

_ID_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
_H2_PATTERN = re.compile(r"^## (.+)$", re.MULTILINE)
_PLACEHOLDER_PATTERN = re.compile(r"{{[^{}]+}}")


@dataclass(frozen=True)
class Point:
    """One self-contained, pointwise evaluation unit."""

    id: str
    question: str
    ground_truth: str
    provenance: str
    source: Path

    @classmethod
    def from_markdown(cls, markdown: str, *, source: Path) -> Point:
        normalized = markdown.replace("\r\n", "\n")
        lines = normalized.splitlines()
        if not lines or not lines[0].startswith("# "):
            raise CaseValidationError(f"{source}: first line must be '# <id>'")
        point_id = lines[0][2:].strip()
        if not _ID_PATTERN.fullmatch(point_id):
            raise CaseValidationError(
                f"{source}: id must be a lowercase ASCII kebab-case slug"
            )
        if source.stem != point_id:
            raise CaseValidationError(
                f"{source}: filename stem must match point id {point_id!r}"
            )
        if _PLACEHOLDER_PATTERN.search(normalized):
            raise CaseValidationError(f"{source}: unresolved template placeholder")

        headings = list(_H2_PATTERN.finditer(normalized))
        found_titles = tuple(match.group(1).strip() for match in headings)
        if found_titles != SECTION_TITLES:
            expected = ", ".join(SECTION_TITLES)
            found = ", ".join(found_titles) or "none"
            raise CaseValidationError(
                f"{source}: H2 sections must be exactly {expected}; found {found}"
            )

        sections: dict[str, str] = {}
        for index, match in enumerate(headings):
            start = match.end()
            end = headings[index + 1].start() if index + 1 < len(headings) else None
            sections[match.group(1).strip()] = normalized[start:end].strip()

        question = _nonempty(sections["Question"], source=source, field="Question")
        ground_truth = _unwrap_details(
            sections["Ground Truth"], source=source, field="Ground Truth"
        )
        provenance = _unwrap_details(
            sections["Provenance"], source=source, field="Provenance"
        )
        return cls(
            id=point_id,
            question=question,
            ground_truth=ground_truth,
            provenance=provenance,
            source=source,
        )

    def agent_payload(self) -> str:
        """Return the only point content visible to an evaluated agent."""
        return self.question


def load_point(path: Path) -> Point:
    try:
        markdown = path.read_text(encoding="utf-8")
    except OSError as error:
        raise CaseValidationError(f"cannot read point {path}: {error}") from error
    return Point.from_markdown(markdown, source=path)


def load_points(directory: Path) -> tuple[Point, ...]:
    if not directory.is_dir():
        raise CaseValidationError(f"point directory does not exist: {directory}")
    validate_meta_template(directory / TEMPLATE_NAME)
    paths = sorted(
        path for path in directory.rglob("*.md") if path.name != TEMPLATE_NAME
    )
    if not paths:
        raise CaseValidationError(
            f"point directory contains no Markdown points: {directory}"
        )
    points = tuple(load_point(path) for path in paths)
    ids = [point.id for point in points]
    if len(ids) != len(set(ids)):
        duplicates = sorted({point_id for point_id in ids if ids.count(point_id) > 1})
        raise CaseValidationError(
            f"{directory}: duplicate point ids: {', '.join(duplicates)}"
        )
    return points


def validate_meta_template(path: Path) -> None:
    try:
        markdown = path.read_text(encoding="utf-8")
    except OSError as error:
        raise CaseValidationError(
            f"cannot read point template {path}: {error}"
        ) from error
    required_fragments = (
        "# {{id}}",
        "## Question",
        "{{question}}",
        "## Ground Truth",
        "{{ground_truth}}",
        "## Provenance",
        "{{provenance}}",
    )
    missing = [fragment for fragment in required_fragments if fragment not in markdown]
    if missing:
        raise CaseValidationError(
            f"{path}: missing template fragments: {', '.join(missing)}"
        )
    headings = tuple(match.group(1).strip() for match in _H2_PATTERN.finditer(markdown))
    if headings != SECTION_TITLES:
        raise CaseValidationError(
            f"{path}: template H2 sections must be exactly {', '.join(SECTION_TITLES)}"
        )


def _unwrap_details(value: str, *, source: Path, field: str) -> str:
    lines = value.splitlines()
    if (
        len(lines) < 5
        or lines[0].strip() != "<details>"
        or lines[-1].strip() != "</details>"
    ):
        raise CaseValidationError(
            f"{source}: {field} must be wrapped in a <details> block"
        )
    if not lines[1].strip().startswith("<summary>") or not lines[1].strip().endswith(
        "</summary>"
    ):
        raise CaseValidationError(f"{source}: {field} requires a one-line <summary>")
    body = "\n".join(lines[2:-1]).strip()
    return _nonempty(body, source=source, field=field)


def _nonempty(value: str, *, source: Path, field: str) -> str:
    stripped = value.strip()
    if not stripped:
        raise CaseValidationError(f"{source}: {field} must not be empty")
    return stripped

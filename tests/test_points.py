from pathlib import Path

import pytest
from click.testing import CliRunner

from pitfall.cli import BUILTIN_POINTS, main
from pitfall.errors import CaseValidationError
from pitfall.point import Point, load_points, validate_meta_template


def test_builtin_points_are_valid_unique_and_pointwise() -> None:
    points = load_points(BUILTIN_POINTS)

    assert len(points) == 174
    assert len({point.id for point in points}) == 174
    assert sum(point.source.parent.name == "synthetic" for point in points) == 12
    assert sum(point.source.parent.name == "a-share" for point in points) == 162
    assert not tuple(BUILTIN_POINTS.rglob("*.json"))


def test_meta_is_the_single_placeholder_template() -> None:
    template = BUILTIN_POINTS / "META.md"

    validate_meta_template(template)
    markdown = template.read_text(encoding="utf-8")
    placeholders = {part for part in markdown.split() if part.startswith("{{")}
    assert {"{{id}}", "{{question}}", "{{ground_truth}}", "{{provenance}}"} <= (
        placeholders
    )


def test_agent_payload_contains_only_the_question() -> None:
    point = next(
        item
        for item in load_points(BUILTIN_POINTS)
        if item.id == "goodwill-impairment-risk"
    )

    payload = point.agent_payload()

    assert payload == point.question
    assert "Reported goodwill is CU 4.5 billion" in payload
    assert "Prediction: **high**" not in payload
    assert point.ground_truth not in payload
    assert point.provenance not in payload


def test_a_share_point_is_self_contained_and_auditable() -> None:
    point = next(
        item
        for item in load_points(BUILTIN_POINTS)
        if item.id == "cn-a-2014-new-industry-scale-600766"
    )

    assert "冻结资料 / Frozen evidence (2)" in point.question
    assert "托管期间矿业公司产权仍归原股东" in point.question
    assert "事件未发生 / no event" in point.ground_truth
    assert "1202114703.PDF" in point.provenance
    assert "冻结搜索工具" not in point.question


@pytest.mark.parametrize(
    ("markdown", "message"),
    [
        (
            "# bad\n\n## Question\n\nQ\n\n## Provenance\n\nP\n",
            "H2 sections must be exactly",
        ),
        (
            "# bad\n\n## Question\n\nQ\n\n## Ground Truth\n\nG\n\n## Provenance\n\nP\n",
            "must be wrapped",
        ),
        (
            (
                "# bad\n\n## Question\n\n{{question}}\n\n"
                "## Ground Truth\n\nG\n\n## Provenance\n\nP\n"
            ),
            "unresolved template placeholder",
        ),
    ],
)
def test_malformed_point_is_rejected(markdown: str, message: str) -> None:
    with pytest.raises(CaseValidationError, match=message):
        Point.from_markdown(markdown, source=Path("bad.md"))


def test_cli_render_and_show_keep_the_visibility_boundary() -> None:
    runner = CliRunner()

    rendered = runner.invoke(main, ["render", "goodwill-impairment-risk"])
    shown = runner.invoke(main, ["show", "goodwill-impairment-risk"])

    assert rendered.exit_code == 0
    assert "Reported goodwill is CU 4.5 billion" in rendered.output
    assert "## Ground Truth" not in rendered.output
    assert shown.exit_code == 0
    assert "## Ground Truth" in shown.output


def test_cli_validate_discovers_every_nested_point() -> None:
    result = CliRunner().invoke(main, ["validate"])

    assert result.exit_code == 0
    assert "Validated 174 point(s)" in result.output

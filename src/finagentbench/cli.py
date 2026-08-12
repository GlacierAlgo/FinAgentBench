"""Command-line interface for authoring and inspecting benchmark cases."""

from __future__ import annotations

import json
from pathlib import Path

import click

from finagentbench.case import BenchmarkCase, CaseValidationError, load_cases

BUILTIN_CASES = Path(__file__).with_name("cases")


@click.group()
@click.version_option(package_name="finagentbench")
def main() -> None:
    """Inspect and validate FinAgentBench evidence packets."""


def cases_dir_option(function):
    return click.option(
        "--cases-dir",
        type=click.Path(path_type=Path, file_okay=False),
        default=BUILTIN_CASES,
        show_default=True,
        help="Directory containing benchmark case JSON files.",
    )(function)


@main.command("list")
@cases_dir_option
def list_command(cases_dir: Path) -> None:
    """List available benchmark cases."""
    cases = _load_or_fail(cases_dir)
    for case in cases:
        click.echo(f"{case.id}\t{case.category}\t{case.title}")


@main.command()
@cases_dir_option
def validate(cases_dir: Path) -> None:
    """Validate every case and cross-case invariant."""
    cases = _load_or_fail(cases_dir)
    click.echo(f"Validated {len(cases)} case(s) in {cases_dir}")


@main.command()
@click.argument("case_id")
@cases_dir_option
def render(case_id: str, cases_dir: Path) -> None:
    """Render the rubric-free JSON payload given to an evaluated agent."""
    case = _find_case(case_id, _load_or_fail(cases_dir))
    click.echo(json.dumps(case.agent_payload(), ensure_ascii=False, indent=2))


@main.command()
@click.argument("case_id")
@click.option(
    "--include-rubric",
    is_flag=True,
    help="Include the authoring rubric. Never expose this to evaluated agents.",
)
@cases_dir_option
def show(case_id: str, include_rubric: bool, cases_dir: Path) -> None:
    """Show case metadata for benchmark authors."""
    case = _find_case(case_id, _load_or_fail(cases_dir))
    payload = case.agent_payload()
    if include_rubric:
        payload["rubric"] = [
            {
                "id": item.id,
                "description": item.description,
                "weight": item.weight,
            }
            for item in case.rubric
        ]
    click.echo(json.dumps(payload, ensure_ascii=False, indent=2))


def _load_or_fail(cases_dir: Path) -> tuple[BenchmarkCase, ...]:
    try:
        return load_cases(cases_dir)
    except CaseValidationError as error:
        raise click.ClickException(str(error)) from error


def _find_case(case_id: str, cases: tuple[BenchmarkCase, ...]) -> BenchmarkCase:
    for case in cases:
        if case.id == case_id:
            return case
    available = ", ".join(case.id for case in cases)
    raise click.ClickException(f"unknown case {case_id!r}; available: {available}")


if __name__ == "__main__":
    main()


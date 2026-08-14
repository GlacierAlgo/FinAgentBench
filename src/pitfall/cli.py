"""Command-line interface for PITFALL points and runtime artifacts."""

from __future__ import annotations

import json
from pathlib import Path

import click

from pitfall.errors import CaseValidationError
from pitfall.evaluation import parse_evaluation
from pitfall.live_shadow import (
    ARTIFACT_TYPE,
    RESOLUTION_TYPE,
    load_live_shadow_scenario,
    resolve_live_shadow_seal,
    run_live_shadow_codex_matrix,
    verify_live_shadow_resolution,
    verify_live_shadow_seal,
)
from pitfall.point import Point, load_points
from pitfall.radar import build_radar_data, render_radar_data_js
from pitfall.sealed_suite import (
    PLAN_TYPE,
    PUBLIC_PLAN_TYPE,
    SUITE_TYPE,
    finalize_suite,
    preregister_suite,
    verify_finalized_suite,
    verify_public_plan_commitment,
    verify_suite_plan,
)

BUILTIN_POINTS = Path(__file__).with_name("points")


@click.group()
@click.version_option(package_name="pitfall")
def main() -> None:
    """Inspect self-contained PITFALL Markdown points."""


def points_dir_option(function):
    return click.option(
        "--points-dir",
        type=click.Path(path_type=Path, file_okay=False),
        default=BUILTIN_POINTS,
        show_default=True,
        help="Directory containing Markdown points and META.md.",
    )(function)


@main.command("list")
@points_dir_option
def list_command(points_dir: Path) -> None:
    """List one stable point ID per line."""
    for point in _load_points_or_fail(points_dir):
        click.echo(point.id)


@main.command()
@points_dir_option
def validate(points_dir: Path) -> None:
    """Validate the template and every point."""
    points = _load_points_or_fail(points_dir)
    click.echo(f"Validated {len(points)} point(s) in {points_dir}")


@main.command()
@click.argument("point_id")
@points_dir_option
def render(point_id: str, points_dir: Path) -> None:
    """Render only the Question visible to an evaluated agent."""
    point = _find_point(point_id, _load_points_or_fail(points_dir))
    click.echo(point.agent_payload())


@main.command()
@click.argument("point_id")
@points_dir_option
def show(point_id: str, points_dir: Path) -> None:
    """Show the full author-facing Markdown point, including hidden sections."""
    point = _find_point(point_id, _load_points_or_fail(points_dir))
    click.echo(point.source.read_text(encoding="utf-8"), nl=False)


@main.command("evaluation-validate")
@click.argument("evaluation", type=click.Path(path_type=Path, dir_okay=False))
def evaluation_validate(evaluation: Path) -> None:
    """Validate one six-class judge output."""
    try:
        result = parse_evaluation(evaluation.read_text(encoding="utf-8"))
    except (OSError, CaseValidationError) as error:
        raise click.ClickException(str(error)) from error
    click.echo(f"{result.classification.value}\t{result.decisive_reason}")


@main.group("radar")
def radar_group() -> None:
    """Build the offline public benchmark radar."""


@radar_group.command("build")
@click.option(
    "--repo-root",
    type=click.Path(path_type=Path, file_okay=False),
    default=Path.cwd(),
    show_default=True,
)
@click.option(
    "--manifest",
    type=click.Path(path_type=Path, dir_okay=False),
    default=Path("radar/source-manifest.json"),
    show_default=True,
)
@click.option(
    "--output",
    type=click.Path(path_type=Path, dir_okay=False),
    default=Path("radar/data.js"),
    show_default=True,
)
def radar_build(repo_root: Path, manifest: Path, output: Path) -> None:
    """Compile committed result artifacts into an offline JavaScript payload."""
    try:
        payload = build_radar_data(repo_root, manifest)
    except CaseValidationError as error:
        raise click.ClickException(str(error)) from error
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_radar_data_js(payload), encoding="utf-8")
    click.echo(
        f"Wrote {payload['coverage']['case_count']} cases and "
        f"{payload['coverage']['attempt_count']} attempts to {output}: "
        f"{payload['data_sha256']}"
    )


@main.group("suite")
def suite_group() -> None:
    """Pre-register and finalize contamination-resistant shadow cohorts."""


@suite_group.command("preregister")
@click.argument("source", type=click.Path(path_type=Path, dir_okay=False))
@click.option(
    "--plan-output",
    type=click.Path(path_type=Path, dir_okay=False),
    required=True,
    help="Private outcome-free plan; do not publish before all runs are sealed.",
)
@click.option(
    "--commitment-output",
    type=click.Path(path_type=Path, dir_okay=False),
    required=True,
    help="Opaque plan commitment to publish before the first run.",
)
def suite_preregister(
    source: Path,
    plan_output: Path,
    commitment_output: Path,
) -> None:
    """Commit a hard-suite cohort before its first model run."""
    try:
        plan, commitment = preregister_suite(_read_json_object(source))
    except CaseValidationError as error:
        raise click.ClickException(str(error)) from error
    _write_json(plan_output, plan)
    _write_json(commitment_output, commitment)
    click.echo(
        f"Wrote private plan {plan_output} and public commitment "
        f"{commitment_output}: {commitment['commitment']['payload_sha256']}"
    )


@suite_group.command("finalize")
@click.argument("plan", type=click.Path(path_type=Path, dir_okay=False))
@click.argument("public_commitment", type=click.Path(path_type=Path, dir_okay=False))
@click.option(
    "--seal",
    "seals",
    type=click.Path(path_type=Path, dir_okay=False),
    multiple=True,
    required=True,
    help="One live-shadow seal per pre-registered slot. Repeat this option.",
)
@click.option(
    "--output",
    type=click.Path(path_type=Path, dir_okay=False),
    required=True,
)
def suite_finalize(
    plan: Path,
    public_commitment: Path,
    seals: tuple[Path, ...],
    output: Path,
) -> None:
    """Bind all planned slots to their intact prediction seals."""
    try:
        artifact = finalize_suite(
            _read_json_object(plan),
            _read_json_object(public_commitment),
            [_read_json_object(path) for path in seals],
        )
    except CaseValidationError as error:
        raise click.ClickException(str(error)) from error
    _write_json(output, artifact)
    click.echo(
        f"Finalized {len(artifact['members'])} suite member(s) to {output}: "
        f"{artifact['commitment']['payload_sha256']}"
    )


@suite_group.command("verify")
@click.argument("artifact", type=click.Path(path_type=Path, dir_okay=False))
def suite_verify(artifact: Path) -> None:
    """Verify a private plan, public commitment, or finalized suite index."""
    try:
        payload = _read_json_object(artifact)
        artifact_type = payload.get("artifact_type")
        if artifact_type == PLAN_TYPE:
            digest = verify_suite_plan(payload)
        elif artifact_type == PUBLIC_PLAN_TYPE:
            digest = verify_public_plan_commitment(payload)
        elif artifact_type == SUITE_TYPE:
            digest = verify_finalized_suite(payload)
        else:
            raise CaseValidationError(
                f"{artifact}: unsupported suite artifact_type {artifact_type!r}"
            )
    except CaseValidationError as error:
        raise click.ClickException(str(error)) from error
    click.echo(f"Verified {artifact_type}: {digest}")


@main.group("shadow")
def shadow_group() -> None:
    """Run, seal, verify, and later resolve real-Web shadow predictions."""


@shadow_group.command("run")
@click.argument("scenario", type=click.Path(path_type=Path, dir_okay=False))
@click.option("--model", "models", multiple=True, required=True)
@click.option(
    "--reasoning-effort",
    type=click.Choice(["low", "medium", "high", "xhigh", "max"]),
    default="low",
    show_default=True,
)
@click.option("--workers", type=click.IntRange(1, 8), default=1, show_default=True)
@click.option("--repeats", type=click.IntRange(1, 10), default=1, show_default=True)
@click.option(
    "--timeout-seconds", type=click.IntRange(10), default=300, show_default=True
)
@click.option(
    "--output",
    type=click.Path(path_type=Path, dir_okay=False),
    required=True,
    help="Outcome-free sealed prediction artifact.",
)
def shadow_run(
    scenario: Path,
    models: tuple[str, ...],
    reasoning_effort: str,
    workers: int,
    repeats: int,
    timeout_seconds: int,
    output: Path,
) -> None:
    """Use native live Web on the scenario as-of date and seal every trace."""
    try:
        source, parsed = load_live_shadow_scenario(scenario)

        def progress(item: dict) -> None:
            marker = "ok" if item["status"] == "completed" else "FAILED"
            click.echo(f"[{marker}] {item['model']} / {parsed.id}", err=True)

        seal = run_live_shadow_codex_matrix(
            source,
            parsed,
            models=models,
            reasoning_effort=reasoning_effort,
            workers=workers,
            timeout_seconds=timeout_seconds,
            repeats=repeats,
            progress=progress,
        )
    except CaseValidationError as error:
        raise click.ClickException(str(error)) from error
    _write_json(output, seal)
    click.echo(
        f"Sealed {len(seal['results'])} prediction(s) to {output} with digest "
        f"{seal['commitment']['payload_sha256']}"
    )


@shadow_group.command("verify")
@click.argument("artifact", type=click.Path(path_type=Path, dir_okay=False))
def shadow_verify(artifact: Path) -> None:
    """Verify a shadow seal or resolution commitment and all trace hashes."""
    try:
        payload = _read_json_object(artifact)
        artifact_type = payload.get("artifact_type")
        if artifact_type == ARTIFACT_TYPE:
            digest = verify_live_shadow_seal(payload)
        elif artifact_type == RESOLUTION_TYPE:
            digest = verify_live_shadow_resolution(payload)
        else:
            raise CaseValidationError(
                f"{artifact}: unsupported shadow artifact_type {artifact_type!r}"
            )
    except CaseValidationError as error:
        raise click.ClickException(str(error)) from error
    click.echo(f"Verified {artifact_type}: {digest}")


@shadow_group.command("resolve")
@click.argument("seal", type=click.Path(path_type=Path, dir_okay=False))
@click.argument("label", type=click.Path(path_type=Path, dir_okay=False))
@click.option(
    "--output",
    type=click.Path(path_type=Path, dir_okay=False),
    required=True,
    help="Resolution artifact bound to the original seal digest.",
)
def shadow_resolve(seal: Path, label: Path, output: Path) -> None:
    """After the horizon matures, validate a label and score the sealed runs."""
    try:
        resolution = resolve_live_shadow_seal(
            _read_json_object(seal),
            _read_json_object(label),
        )
    except CaseValidationError as error:
        raise click.ClickException(str(error)) from error
    _write_json(output, resolution)
    click.echo(
        f"Resolved {resolution['scenario_id']} to {output}; commitment "
        f"{resolution['commitment']['payload_sha256']}"
    )


def _load_points_or_fail(points_dir: Path) -> tuple[Point, ...]:
    try:
        return load_points(points_dir)
    except CaseValidationError as error:
        raise click.ClickException(str(error)) from error


def _find_point(point_id: str, points: tuple[Point, ...]) -> Point:
    for point in points:
        if point.id == point_id:
            return point
    raise click.ClickException(f"unknown point {point_id!r}")


def _read_json_object(path: Path) -> dict:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise CaseValidationError(f"{path}: invalid JSON: {error}") from error
    if not isinstance(payload, dict):
        raise CaseValidationError(f"{path}: top-level value must be an object")
    return payload


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

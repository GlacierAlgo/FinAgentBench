"""Command-line interface for authoring and inspecting benchmark cases."""

from __future__ import annotations

import json
from pathlib import Path

import click

from finagentbench.adapter import AdapterError, StdioAdapter
from finagentbench.case import BenchmarkCase, CaseValidationError, load_cases
from finagentbench.live_shadow import (
    ARTIFACT_TYPE,
    RESOLUTION_TYPE,
    load_live_shadow_scenario,
    resolve_live_shadow_seal,
    run_live_shadow_codex_matrix,
    verify_live_shadow_resolution,
    verify_live_shadow_seal,
)
from finagentbench.radar import build_radar_data, render_radar_data_js
from finagentbench.runner import (
    render_markdown_report,
    run_adapter_matrix,
    run_codex_matrix,
)
from finagentbench.scoring import score_submission
from finagentbench.sealed_suite import (
    PLAN_TYPE,
    PUBLIC_PLAN_TYPE,
    SUITE_TYPE,
    finalize_suite,
    preregister_suite,
    verify_finalized_suite,
    verify_public_plan_commitment,
    verify_suite_plan,
)
from finagentbench.walkforward import (
    WalkForwardCase,
    load_walkforward_suite,
    score_walkforward_submission,
)
from finagentbench.walkforward_runner import (
    render_walkforward_report,
    run_walkforward_adapter_matrix,
    run_walkforward_codex_matrix,
)

BUILTIN_CASES = Path(__file__).with_name("cases")
BUILTIN_A_SHARE = Path(__file__).with_name("a_share")
BUILTIN_A_SHARE_SCENARIOS = BUILTIN_A_SHARE / "scenarios"
BUILTIN_A_SHARE_CORPORA = BUILTIN_A_SHARE / "corpora"
BUILTIN_A_SHARE_LABELS = BUILTIN_A_SHARE / "labels"


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
        payload["answer_key"] = {
            "prediction": case.answer_key.prediction,
            "premise_assessment": case.answer_key.premise_assessment,
            "evidence_ids": list(case.answer_key.evidence_ids),
        }
    click.echo(json.dumps(payload, ensure_ascii=False, indent=2))


@main.command()
@click.argument("case_id")
@click.argument("submission", type=click.Path(path_type=Path, dir_okay=False))
@cases_dir_option
def score(case_id: str, submission: Path, cases_dir: Path) -> None:
    """Score one structured submission against a public answer key."""
    case = _find_case(case_id, _load_or_fail(cases_dir))
    try:
        payload = json.loads(submission.read_text(encoding="utf-8"))
        breakdown = score_submission(case, payload)
    except (OSError, json.JSONDecodeError, CaseValidationError) as error:
        raise click.ClickException(str(error)) from error
    click.echo(json.dumps(breakdown.to_dict(), ensure_ascii=False, indent=2))


@main.command()
@click.option("--model", "models", multiple=True, required=True)
@click.option(
    "--case-id",
    "case_ids",
    multiple=True,
    help="Run only selected case IDs. Repeat for more than one case.",
)
@click.option(
    "--reasoning-effort",
    type=click.Choice(["low", "medium", "high", "xhigh", "max"]),
    default="low",
    show_default=True,
)
@click.option("--workers", type=click.IntRange(1, 8), default=1, show_default=True)
@click.option(
    "--timeout-seconds", type=click.IntRange(10), default=180, show_default=True
)
@click.option(
    "--adapter-manifest",
    type=click.Path(path_type=Path, dir_okay=False, exists=True),
    help="Use a finagentbench-stdio-v1 harness manifest instead of Codex CLI.",
)
@click.option(
    "--output",
    type=click.Path(path_type=Path, dir_okay=False),
    required=True,
    help="JSON result artifact.",
)
@click.option(
    "--report-output",
    type=click.Path(path_type=Path, dir_okay=False),
    help="Optional Markdown report artifact.",
)
@cases_dir_option
def benchmark(
    models: tuple[str, ...],
    case_ids: tuple[str, ...],
    reasoning_effort: str,
    workers: int,
    timeout_seconds: int,
    adapter_manifest: Path | None,
    output: Path,
    report_output: Path | None,
    cases_dir: Path,
) -> None:
    """Run a controlled harness/model matrix over selected public cases."""
    cases = _load_or_fail(cases_dir)
    if case_ids:
        cases = tuple(_find_case(case_id, cases) for case_id in case_ids)
    adapter = _load_adapter_or_fail(adapter_manifest)
    harness_name = adapter.name if adapter is not None else "codex-cli"
    click.echo(
        f"Running {len(models)} model(s) × {len(cases)} case(s) "
        f"through {harness_name} at effort={reasoning_effort} "
        f"with {workers} worker(s)"
    )

    def progress(item: dict) -> None:
        marker = "ok" if item["status"] == "completed" else "FAILED"
        click.echo(f"[{marker}] {item['model']} / {item['case_id']}", err=True)

    run_function = run_adapter_matrix if adapter is not None else run_codex_matrix
    run_kwargs = {
        "models": models,
        "reasoning_effort": reasoning_effort,
        "workers": workers,
        "timeout_seconds": timeout_seconds,
        "progress": progress,
    }
    if adapter is not None:
        run_kwargs["adapter"] = adapter
    try:
        run = run_function(cases, **run_kwargs)
    except AdapterError as error:
        raise click.ClickException(str(error)) from error
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(run, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    click.echo(f"Wrote {output}")
    if report_output is not None:
        report_output.parent.mkdir(parents=True, exist_ok=True)
        report_output.write_text(render_markdown_report(run), encoding="utf-8")
        click.echo(f"Wrote {report_output}")


@main.command()
@click.argument("result", type=click.Path(path_type=Path, dir_okay=False))
@click.option(
    "--output", type=click.Path(path_type=Path, dir_okay=False), help="Markdown file."
)
def report(result: Path, output: Path | None) -> None:
    """Render a Markdown comparison from a benchmark result artifact."""
    try:
        run = json.loads(result.read_text(encoding="utf-8"))
        markdown = render_markdown_report(run)
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        raise click.ClickException(str(error)) from error
    if output is None:
        click.echo(markdown, nl=False)
        return
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(markdown, encoding="utf-8")
    click.echo(f"Wrote {output}")


@main.group("a-share")
def a_share_group() -> None:
    """Work with real A-share walk-forward scenarios."""


def a_share_dirs(function):
    function = click.option(
        "--labels-dir",
        type=click.Path(path_type=Path, file_okay=False),
        default=BUILTIN_A_SHARE_LABELS,
        show_default=True,
    )(function)
    function = click.option(
        "--corpora-dir",
        type=click.Path(path_type=Path, file_okay=False),
        default=BUILTIN_A_SHARE_CORPORA,
        show_default=True,
    )(function)
    return click.option(
        "--scenarios-dir",
        type=click.Path(path_type=Path, file_okay=False),
        default=BUILTIN_A_SHARE_SCENARIOS,
        show_default=True,
    )(function)


@a_share_group.command("validate")
@a_share_dirs
def a_share_validate(
    scenarios_dir: Path, corpora_dir: Path, labels_dir: Path
) -> None:
    """Validate time cutoffs, corpus domains, labels, and pair coverage."""
    cases = _load_a_share_or_fail(scenarios_dir, corpora_dir, labels_dir)
    positives = sum(case.label.event_occurred for case in cases)
    click.echo(
        f"Validated {len(cases)} A-share scenario(s): "
        f"{positives} event / {len(cases) - positives} no-event"
    )


@a_share_group.command("list")
@a_share_dirs
def a_share_list(scenarios_dir: Path, corpora_dir: Path, labels_dir: Path) -> None:
    """List A-share scenarios without exposing their outcomes."""
    cases = _load_a_share_or_fail(scenarios_dir, corpora_dir, labels_dir)
    for case in cases:
        scenario = case.scenario
        click.echo(
            f"{scenario.id}\t{scenario.as_of}\t"
            f"{scenario.security.ticker}\t{scenario.security.name_as_of}"
        )


@a_share_group.command("render")
@click.argument("scenario_id")
@a_share_dirs
def a_share_render(
    scenario_id: str, scenarios_dir: Path, corpora_dir: Path, labels_dir: Path
) -> None:
    """Render only the task payload visible to an evaluated agent."""
    case = _find_a_share(
        scenario_id,
        _load_a_share_or_fail(scenarios_dir, corpora_dir, labels_dir),
    )
    click.echo(
        json.dumps(case.scenario.agent_payload(), ensure_ascii=False, indent=2)
    )


@a_share_group.command("search")
@click.argument("scenario_id")
@click.argument("query")
@click.option("--limit", type=click.IntRange(1, 20), default=5, show_default=True)
@a_share_dirs
def a_share_search(
    scenario_id: str,
    query: str,
    limit: int,
    scenarios_dir: Path,
    corpora_dir: Path,
    labels_dir: Path,
) -> None:
    """Run the deterministic as-of-bounded search used for historical replay."""
    case = _find_a_share(
        scenario_id,
        _load_a_share_or_fail(scenarios_dir, corpora_dir, labels_dir),
    )
    click.echo(
        json.dumps(case.corpus.search(query, limit=limit), ensure_ascii=False, indent=2)
    )


@a_share_group.command("score")
@click.argument("scenario_id")
@click.argument("submission", type=click.Path(path_type=Path, dir_okay=False))
@a_share_dirs
def a_share_score(
    scenario_id: str,
    submission: Path,
    scenarios_dir: Path,
    corpora_dir: Path,
    labels_dir: Path,
) -> None:
    """Score a probability, prediction, and cited frozen evidence."""
    case = _find_a_share(
        scenario_id,
        _load_a_share_or_fail(scenarios_dir, corpora_dir, labels_dir),
    )
    try:
        payload = json.loads(submission.read_text(encoding="utf-8"))
        result = score_walkforward_submission(case, payload)
    except (OSError, json.JSONDecodeError, CaseValidationError) as error:
        raise click.ClickException(str(error)) from error
    click.echo(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))


@a_share_group.command("benchmark")
@click.option("--model", "models", multiple=True, required=True)
@click.option(
    "--scenario-id",
    "scenario_ids",
    multiple=True,
    help="Run only selected scenario IDs. Repeat for more than one scenario.",
)
@click.option(
    "--reasoning-effort",
    type=click.Choice(["low", "medium", "high", "xhigh", "max"]),
    default="low",
    show_default=True,
)
@click.option("--workers", type=click.IntRange(1, 8), default=1, show_default=True)
@click.option(
    "--timeout-seconds", type=click.IntRange(10), default=180, show_default=True
)
@click.option(
    "--adapter-manifest",
    type=click.Path(path_type=Path, dir_okay=False, exists=True),
    help="Use a frozen-search stdio harness manifest instead of Codex CLI.",
)
@click.option(
    "--output",
    type=click.Path(path_type=Path, dir_okay=False),
    required=True,
    help="JSON result artifact.",
)
@click.option(
    "--report-output",
    type=click.Path(path_type=Path, dir_okay=False),
    help="Optional Markdown report artifact.",
)
@a_share_dirs
def a_share_benchmark(
    models: tuple[str, ...],
    scenario_ids: tuple[str, ...],
    reasoning_effort: str,
    workers: int,
    timeout_seconds: int,
    adapter_manifest: Path | None,
    output: Path,
    report_output: Path | None,
    scenarios_dir: Path,
    corpora_dir: Path,
    labels_dir: Path,
) -> None:
    """Compare models using only the frozen historical search tool."""
    cases = _load_a_share_or_fail(scenarios_dir, corpora_dir, labels_dir)
    if scenario_ids:
        cases = tuple(_find_a_share(scenario_id, cases) for scenario_id in scenario_ids)
    adapter = _load_adapter_or_fail(adapter_manifest)
    harness_name = adapter.name if adapter is not None else "codex-cli"
    click.echo(
        f"Running {len(models)} model(s) × {len(cases)} A-share scenario(s) "
        f"through {harness_name} at effort={reasoning_effort} "
        f"with {workers} worker(s)"
    )

    def progress(item: dict) -> None:
        marker = "ok" if item["status"] == "completed" else "FAILED"
        click.echo(f"[{marker}] {item['model']} / {item['scenario_id']}", err=True)

    run_function = (
        run_walkforward_adapter_matrix
        if adapter is not None
        else run_walkforward_codex_matrix
    )
    run_kwargs = {
        "models": models,
        "reasoning_effort": reasoning_effort,
        "workers": workers,
        "timeout_seconds": timeout_seconds,
        "progress": progress,
    }
    if adapter is not None:
        run_kwargs["adapter"] = adapter
    try:
        run = run_function(cases, **run_kwargs)
    except AdapterError as error:
        raise click.ClickException(str(error)) from error
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(run, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    click.echo(f"Wrote {output}")
    if report_output is not None:
        report_output.parent.mkdir(parents=True, exist_ok=True)
        report_output.write_text(render_walkforward_report(run), encoding="utf-8")
        click.echo(f"Wrote {report_output}")


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


def _load_or_fail(cases_dir: Path) -> tuple[BenchmarkCase, ...]:
    try:
        return load_cases(cases_dir)
    except CaseValidationError as error:
        raise click.ClickException(str(error)) from error


def _load_adapter_or_fail(path: Path | None) -> StdioAdapter | None:
    if path is None:
        return None
    try:
        return StdioAdapter.from_path(path)
    except AdapterError as error:
        raise click.ClickException(str(error)) from error


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


def _find_case(case_id: str, cases: tuple[BenchmarkCase, ...]) -> BenchmarkCase:
    for case in cases:
        if case.id == case_id:
            return case
    available = ", ".join(case.id for case in cases)
    raise click.ClickException(f"unknown case {case_id!r}; available: {available}")


def _load_a_share_or_fail(
    scenarios_dir: Path, corpora_dir: Path, labels_dir: Path
) -> tuple[WalkForwardCase, ...]:
    try:
        return load_walkforward_suite(scenarios_dir, corpora_dir, labels_dir)
    except CaseValidationError as error:
        raise click.ClickException(str(error)) from error


def _find_a_share(
    scenario_id: str, cases: tuple[WalkForwardCase, ...]
) -> WalkForwardCase:
    for case in cases:
        if case.scenario.id == scenario_id:
            return case
    available = ", ".join(case.scenario.id for case in cases)
    raise click.ClickException(
        f"unknown A-share scenario {scenario_id!r}; available: {available}"
    )


if __name__ == "__main__":
    main()

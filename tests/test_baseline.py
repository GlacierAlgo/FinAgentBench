import json
from pathlib import Path

import pytest

from pitfall import baseline
from pitfall.errors import CaseValidationError
from pitfall.point import Point


def _point(tmp_path: Path, point_id: str = "test-point") -> Point:
    source = tmp_path / f"{point_id}.md"
    source.write_text(
        f"# {point_id}\n\n## Question\n\nQuestion body\n\n"
        "## Ground Truth\n\n<details>\n<summary>hidden</summary>\n\n"
        "Ground truth body\n\n</details>\n\n## Provenance\n\n"
        "<details>\n<summary>audit</summary>\n\nSource\n\n</details>\n",
        encoding="utf-8",
    )
    return Point(
        id=point_id,
        question="Question body",
        ground_truth="Ground truth body",
        provenance="Source",
        source=source,
    )


def _completed(message: str, *, searches: int = 0) -> dict:
    return {
        "status": "completed",
        "latency_seconds": 1.0,
        "message": message,
        "usage": {"input_tokens": 10, "output_tokens": 2},
        "event_count": 2,
        "tool_counts": {"web_search": searches} if searches else {},
        "web_search_calls": searches,
    }


def test_point_run_hides_ground_truth_from_agent_and_pins_judge(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    point = _point(tmp_path)
    calls = []

    def fake_invoke(**kwargs):
        calls.append(kwargs)
        if len(calls) == 1:
            return _completed("Agent answer", searches=1)
        return _completed("Class: completely_correct\n\nMatches ground truth.")

    monkeypatch.setattr(baseline, "_invoke_codex", fake_invoke)

    result = baseline._run_point(
        point,
        model="agent-model",
        reasoning_effort="high",
        timeout_seconds=30,
    )

    assert result["status"] == "completed"
    assert result["evaluation"]["class"] == "completely_correct"
    assert "Ground truth body" not in calls[0]["prompt"]
    assert "Ground truth body" in calls[1]["prompt"]
    assert calls[1]["model"] == "gpt-5.6-sol"
    assert calls[1]["reasoning_effort"] == "xhigh"
    assert calls[1]["web_search"] is False


def test_baseline_checkpoints_and_verifies_exact_coverage(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    points = (_point(tmp_path, "point-a"), _point(tmp_path, "point-b"))
    monkeypatch.setattr(baseline, "_command_output", lambda command: "codex test")
    monkeypatch.setattr(
        baseline,
        "_run_point",
        lambda point, **kwargs: {
            **baseline._point_identity(point),
            "status": "completed",
            "agent": _completed("answer", searches=1),
            "answer": "answer",
            "judge": _completed(
                "Class: completely_correct\n\nMatches ground truth."
            ),
            "evaluation": {
                "class": "completely_correct",
                "decisive_reason": "Matches ground truth.",
            },
        },
    )
    output = tmp_path / "baseline.json"

    payload = baseline.run_point_baseline(
        points,
        model="agent-model",
        reasoning_effort="high",
        workers=2,
        timeout_seconds=30,
        output=output,
        resume=False,
    )

    assert json.loads(output.read_text(encoding="utf-8")) == payload
    baseline.verify_point_baseline(payload, points)
    assert payload["status"] == "complete"
    assert payload["summary"]["completed"] == 2

    missing = json.loads(json.dumps(payload))
    missing["results"].pop()
    with pytest.raises(CaseValidationError, match="exactly cover"):
        baseline.verify_point_baseline(missing, points)


def test_incomplete_baseline_does_not_verify(tmp_path: Path) -> None:
    point = _point(tmp_path)
    payload = {
        "schema_version": 1,
        "artifact_type": baseline.ARTIFACT_TYPE,
        "status": "incomplete",
    }
    with pytest.raises(CaseValidationError, match="not complete"):
        baseline.verify_point_baseline(payload, (point,))

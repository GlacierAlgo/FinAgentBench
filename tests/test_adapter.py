import importlib.util
import json
import sys
from pathlib import Path

import pytest

from finagentbench.adapter import AdapterError, StdioAdapter
from finagentbench.case import load_cases
from finagentbench.cli import (
    BUILTIN_A_SHARE_CORPORA,
    BUILTIN_A_SHARE_LABELS,
    BUILTIN_A_SHARE_SCENARIOS,
    BUILTIN_CASES,
)
from finagentbench.runner import run_adapter_matrix
from finagentbench.walkforward import load_walkforward_suite
from finagentbench.walkforward_runner import run_walkforward_adapter_matrix


def _opencode_adapter_module():
    source = (
        Path(__file__).parents[1] / "examples" / "adapters" / "opencode_stdio.py"
    )
    spec = importlib.util.spec_from_file_location("opencode_stdio", source)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _adapter(tmp_path: Path, *, frozen_search: bool = True) -> StdioAdapter:
    script = tmp_path / "fake_adapter.py"
    script.write_text(
        """
import json
import sys
from pathlib import Path

request = json.load(sys.stdin)
Path(__file__).with_name("captured.json").write_text(
    json.dumps(request, ensure_ascii=False), encoding="utf-8"
)
if request["task"] == "synthetic":
    submission = {
        "prediction": "high",
        "confidence": 0.9,
        "premise_assessment": "invalid",
        "evidence_ids": [
            "balance-sheet",
            "accounting-policy",
            "operating-trend",
            "headroom",
            "sensitivity",
            "rates",
        ],
        "explanation": "Goodwill is impaired rather than depreciated.",
    }
    search_calls = 0
else:
    submission = {
        "event_probability": 0.1,
        "prediction": "no_event",
        "evidence_ids": [
            "prospectus-product-transition",
            "inquiry-customer-ecosystem-risk",
            "second-inquiry-orders-and-roadmap",
        ],
        "analysis_summary": "Concentration and cash conversion constrain validation.",
    }
    search_calls = 2
print(json.dumps({
    "schema_version": 1,
    "submission": submission,
    "usage": {"input_tokens": 10, "output_tokens": 5},
    "tool_calls": {"frozen_search": search_calls},
    "events": [{"type": "final"}],
    "metadata": {"fixture": True},
}))
""".strip()
        + "\n",
        encoding="utf-8",
    )
    manifest = tmp_path / "adapter.json"
    manifest.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "name": "fixture-adapter",
                "version": "fixture 1",
                "command": [sys.executable, "{manifest_dir}/fake_adapter.py"],
                "capabilities": {
                    "structured_output": True,
                    "frozen_search": frozen_search,
                },
                "execution": {
                    "sandbox": "fixture temp directory",
                    "external_data_access": False,
                    "session_persistence": False,
                    "outcome_visible_to_agent": False,
                    "reasoning_effort_contract": "fixture",
                },
            }
        )
        + "\n",
        encoding="utf-8",
    )
    return StdioAdapter.from_path(manifest)


def test_stdio_adapter_runs_public_case_without_exposing_answer_key(
    tmp_path: Path,
) -> None:
    case = next(
        item for item in load_cases(BUILTIN_CASES) if item.id == "goodwill-impairment-risk"
    )
    adapter = _adapter(tmp_path)

    run = run_adapter_matrix(
        (case,),
        models=("fixture-model",),
        reasoning_effort="low",
        workers=1,
        timeout_seconds=10,
        adapter=adapter,
    )

    assert run["harness"]["protocol"] == "finagentbench-stdio-v1"
    assert run["harness"]["manifest_sha256"] == adapter.manifest_sha256
    assert run["results"][0]["status"] == "completed"
    assert run["results"][0]["score"]["prediction_correct"]
    captured = (tmp_path / "captured.json").read_text(encoding="utf-8")
    assert "answer_key" not in captured
    assert "rubric" not in captured


def test_stdio_adapter_runs_frozen_search_case_without_exposing_label(
    tmp_path: Path,
) -> None:
    cases = load_walkforward_suite(
        BUILTIN_A_SHARE_SCENARIOS,
        BUILTIN_A_SHARE_CORPORA,
        BUILTIN_A_SHARE_LABELS,
    )
    case = next(
        item
        for item in cases
        if item.scenario.id == "cn-a-2020-cambricon-rd-commercial-validation"
    )
    adapter = _adapter(tmp_path)

    run = run_walkforward_adapter_matrix(
        (case,),
        models=("fixture-model",),
        reasoning_effort="low",
        workers=1,
        timeout_seconds=10,
        adapter=adapter,
    )

    result = run["results"][0]
    assert result["status"] == "completed"
    assert result["search_calls"] == 2
    assert result["score"]["classification_correct"]
    captured = (tmp_path / "captured.json").read_text(encoding="utf-8")
    assert "event_occurred" not in captured
    assert "resolved_at" not in captured
    assert "rqdata" not in captured.lower()


def test_a_share_runner_rejects_adapter_without_frozen_search(
    tmp_path: Path,
) -> None:
    adapter = _adapter(tmp_path, frozen_search=False)

    with pytest.raises(AdapterError, match="frozen_search"):
        run_walkforward_adapter_matrix(
            (),
            models=("fixture-model",),
            reasoning_effort="low",
            workers=1,
            timeout_seconds=10,
            adapter=adapter,
        )


def test_opencode_reference_adapter_parses_text_tools_and_usage() -> None:
    adapter_module = _opencode_adapter_module()
    events = [
        {
            "type": "tool_use",
            "part": {
                "tool": "bash",
                "state": {
                    "status": "completed",
                    "input": {
                        "command": "python3 frozen_search.py '客户 集中度'",
                    },
                },
            },
        },
        {
            "type": "step_finish",
            "part": {
                "tokens": {
                    "input": 100,
                    "output": 20,
                    "reasoning": 5,
                    "cache": {"read": 40, "write": 0},
                }
            },
        },
        {"type": "text", "part": {"text": '{"event_probability":0.1}'}},
    ]

    assert adapter_module._frozen_search_calls(events) == 1
    assert adapter_module._final_text(events) == '{"event_probability":0.1}'
    assert adapter_module._usage(events) == {
        "input_tokens": 100,
        "cached_input_tokens": 40,
        "output_tokens": 20,
        "reasoning_tokens": 5,
    }


def test_opencode_reference_adapter_writes_restricted_permissions(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    adapter_module = _opencode_adapter_module()
    monkeypatch.chdir(tmp_path)

    adapter_module._write_restricted_config(allow_frozen_search=True)

    config = json.loads((tmp_path / "opencode.json").read_text(encoding="utf-8"))
    assert config["permission"]["*"] == "deny"
    assert config["permission"]["bash"] == {
        "*": "deny",
        "python3 frozen_search.py *": "allow",
    }

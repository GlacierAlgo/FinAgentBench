"""Reference finagentbench-stdio-v1 adapter for OpenCode.

The adapter deliberately exposes no general tools. Historical A-share runs may
only execute ``python3 frozen_search.py <query>`` in the temporary case folder.
Provider authentication remains owned by OpenCode and is never placed in the
adapter manifest or result artifact.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


def main() -> int:
    try:
        request = _read_request()
        task = _string(request, "task")
        model = _string(request, "model")
        prompt = _string(request, "prompt")
        if task not in {"synthetic", "a_share_frozen_web"}:
            raise ValueError(f"unsupported task {task!r}")
        _write_restricted_config(allow_frozen_search=task == "a_share_frozen_web")
        command = [
            "opencode",
            "run",
            "--pure",
            "--model",
            model,
            "--format",
            "json",
            "--dir",
            str(Path.cwd()),
        ]
        variant = _variant_for(model, _string(request, "reasoning_effort"))
        if variant is not None:
            command.extend(["--variant", variant])
        command.extend(["--", prompt])
        completed = subprocess.run(
            command,
            text=True,
            capture_output=True,
            check=False,
        )
        events = _events(completed.stdout)
        errors = [event for event in events if event.get("type") == "error"]
        if completed.returncode != 0 or errors:
            detail = errors[-1] if errors else completed.stderr[-3000:]
            raise RuntimeError(
                f"opencode failed with exit {completed.returncode}: {detail}"
            )
        final_text = _final_text(events)
        submission = json.loads(final_text)
        if not isinstance(submission, dict):
            raise TypeError("OpenCode final text must be one JSON object")
        payload = {
            "schema_version": 1,
            "submission": submission,
            "usage": _usage(events),
            "tool_calls": {
                "frozen_search": _frozen_search_calls(events),
            },
            "events": [_event_summary(event) for event in events],
            "metadata": {
                "provider_model": model,
                "reasoning_effort_applied": variant is not None,
                "provider_variant": variant,
            },
        }
        sys.stdout.write(json.dumps(payload, ensure_ascii=False))
        return 0
    except (
        OSError,
        TypeError,
        ValueError,
        RuntimeError,
        json.JSONDecodeError,
    ) as error:
        sys.stderr.write(f"opencode stdio adapter: {error}\n")
        return 2


def _read_request() -> dict[str, Any]:
    payload = json.load(sys.stdin)
    if not isinstance(payload, dict) or payload.get("schema_version") != 1:
        raise ValueError("expected a finagentbench-stdio-v1 request")
    return payload


def _write_restricted_config(*, allow_frozen_search: bool) -> None:
    permission: dict[str, Any] = {"*": "deny"}
    if allow_frozen_search:
        permission["bash"] = {
            "*": "deny",
            "python3 frozen_search.py *": "allow",
        }
    config = {
        "$schema": "https://opencode.ai/config.json",
        "permission": permission,
    }
    Path("opencode.json").write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _variant_for(model: str, effort: str) -> str | None:
    raw = os.environ.get("FINAGENTBENCH_OPENCODE_VARIANTS")
    if not raw:
        return None
    payload = json.loads(raw)
    if not isinstance(payload, dict):
        raise TypeError("FINAGENTBENCH_OPENCODE_VARIANTS must be a JSON object")
    model_map = payload.get(model, {})
    if not isinstance(model_map, dict):
        raise TypeError("model variant mapping must be an object")
    variant = model_map.get(effort)
    if variant is None:
        return None
    if not isinstance(variant, str) or not variant.strip():
        raise ValueError("mapped OpenCode variant must be a non-empty string")
    return variant.strip()


def _events(stdout: str) -> list[dict[str, Any]]:
    events = []
    for line in stdout.splitlines():
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"invalid OpenCode JSON event: {error}") from error
        if not isinstance(event, dict):
            raise TypeError("OpenCode event must be an object")
        events.append(event)
    if not events:
        raise ValueError("OpenCode returned no JSON events")
    return events


def _final_text(events: list[dict[str, Any]]) -> str:
    texts = []
    for event in events:
        if event.get("type") != "text":
            continue
        part = event.get("part")
        if isinstance(part, dict) and isinstance(part.get("text"), str):
            text = part["text"].strip()
            if text:
                texts.append(text)
    if not texts:
        raise ValueError("OpenCode returned no completed text event")
    return texts[-1]


def _usage(events: list[dict[str, Any]]) -> dict[str, int]:
    usage = {
        "input_tokens": 0,
        "cached_input_tokens": 0,
        "output_tokens": 0,
        "reasoning_tokens": 0,
    }
    for event in events:
        if event.get("type") != "step_finish":
            continue
        part = event.get("part")
        tokens = part.get("tokens") if isinstance(part, dict) else None
        if not isinstance(tokens, dict):
            continue
        usage["input_tokens"] += _nonnegative_int(tokens.get("input", 0))
        usage["output_tokens"] += _nonnegative_int(tokens.get("output", 0))
        usage["reasoning_tokens"] += _nonnegative_int(tokens.get("reasoning", 0))
        cache = tokens.get("cache", {})
        if isinstance(cache, dict):
            usage["cached_input_tokens"] += _nonnegative_int(cache.get("read", 0))
    return usage


def _frozen_search_calls(events: list[dict[str, Any]]) -> int:
    calls = 0
    for event in events:
        if event.get("type") != "tool_use":
            continue
        part = event.get("part")
        if not isinstance(part, dict) or part.get("tool") != "bash":
            continue
        state = part.get("state")
        if not isinstance(state, dict) or state.get("status") not in {
            "completed",
            "error",
        }:
            continue
        inputs = state.get("input")
        command = inputs.get("command") if isinstance(inputs, dict) else None
        if isinstance(command, str) and "frozen_search.py" in command:
            calls += 1
    return calls


def _event_summary(event: dict[str, Any]) -> dict[str, Any]:
    summary: dict[str, Any] = {"type": str(event.get("type", "unknown"))}
    part = event.get("part")
    if isinstance(part, dict) and isinstance(part.get("tool"), str):
        summary["tool"] = part["tool"]
        state = part.get("state")
        if isinstance(state, dict) and isinstance(state.get("status"), str):
            summary["status"] = state["status"]
    return summary


def _string(payload: dict[str, Any], field: str) -> str:
    value = payload.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"request {field} must be a non-empty string")
    return value.strip()


def _nonnegative_int(value: Any) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        return 0
    return value


if __name__ == "__main__":
    raise SystemExit(main())

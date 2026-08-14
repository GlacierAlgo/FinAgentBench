"""Provider-neutral stdio adapter contract for external agent harnesses."""

from __future__ import annotations

import hashlib
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any


class AdapterError(ValueError):
    """Raised when an adapter manifest or execution violates the contract."""


@dataclass(frozen=True)
class AdapterOutput:
    submission: dict[str, Any]
    usage: dict[str, int]
    tool_calls: dict[str, int]
    events: tuple[dict[str, Any], ...]
    metadata: dict[str, Any]


@dataclass(frozen=True)
class StdioAdapter:
    name: str
    command: tuple[str, ...]
    version: str | None
    version_command: tuple[str, ...] | None
    capabilities: dict[str, bool]
    execution: dict[str, Any]
    manifest_dir: Path
    manifest_sha256: str

    @classmethod
    def from_path(cls, path: Path) -> StdioAdapter:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise AdapterError(
                f"cannot load adapter manifest {path}: {error}"
            ) from error
        if not isinstance(payload, dict):
            raise AdapterError("adapter manifest must be a JSON object")
        required = {
            "schema_version",
            "name",
            "command",
            "capabilities",
            "execution",
        }
        missing = sorted(required - payload.keys())
        if missing:
            raise AdapterError(f"adapter manifest missing fields: {', '.join(missing)}")
        if payload["schema_version"] != 1:
            raise AdapterError("adapter manifest schema_version must be 1")
        name = _nonempty_string(payload["name"], field="name")
        command = _command(payload["command"], field="command")
        version = payload.get("version")
        version_command_payload = payload.get("version_command")
        if (version is None) == (version_command_payload is None):
            raise AdapterError(
                "adapter manifest requires exactly one of version or version_command"
            )
        parsed_version = (
            _nonempty_string(version, field="version") if version is not None else None
        )
        version_command = (
            _command(version_command_payload, field="version_command")
            if version_command_payload is not None
            else None
        )
        capabilities = _capabilities(payload["capabilities"])
        execution = _execution(payload["execution"])
        manifest_dir = path.resolve().parent
        encoded = json.dumps(
            payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        return cls(
            name=name,
            command=tuple(_expand_manifest_dir(command, manifest_dir)),
            version=parsed_version,
            version_command=(
                tuple(_expand_manifest_dir(version_command, manifest_dir))
                if version_command is not None
                else None
            ),
            capabilities=capabilities,
            execution=execution,
            manifest_dir=manifest_dir,
            manifest_sha256=hashlib.sha256(encoded).hexdigest(),
        )

    def require_capability(self, name: str) -> None:
        if not self.capabilities.get(name, False):
            raise AdapterError(
                f"adapter {self.name!r} does not declare required capability {name!r}"
            )

    def harness_metadata(self, *, external_data: bool | str) -> dict[str, Any]:
        version = self.version
        if self.version_command is not None:
            try:
                completed = subprocess.run(
                    self.version_command,
                    cwd=self.manifest_dir,
                    text=True,
                    capture_output=True,
                    check=False,
                    timeout=10,
                )
            except (OSError, subprocess.TimeoutExpired) as error:
                raise AdapterError(
                    f"adapter version command failed: {error}"
                ) from error
            if completed.returncode != 0:
                raise AdapterError(
                    "adapter version command exited "
                    f"{completed.returncode}: {completed.stderr[-1000:]}"
                )
            version = completed.stdout.strip()
            if not version:
                raise AdapterError("adapter version command returned an empty version")
        return {
            "name": self.name,
            "version": version,
            "protocol": "pitfall-stdio-v1",
            "manifest_sha256": self.manifest_sha256,
            "sandbox": self.execution["sandbox"],
            "external_data": external_data,
            "external_data_access": self.execution["external_data_access"],
            "session_persistence": self.execution["session_persistence"],
            "outcome_visible_to_agent": self.execution["outcome_visible_to_agent"],
            "reasoning_effort_contract": self.execution["reasoning_effort_contract"],
        }

    def run(
        self,
        request: dict[str, Any],
        *,
        directory: Path,
        timeout_seconds: int,
    ) -> AdapterOutput:
        try:
            completed = subprocess.run(
                self.command,
                cwd=directory,
                input=json.dumps(request, ensure_ascii=False),
                text=True,
                capture_output=True,
                check=False,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired as error:
            raise AdapterError(f"timeout after {timeout_seconds}s") from error
        except OSError as error:
            raise AdapterError(f"cannot execute adapter: {error}") from error
        if completed.returncode != 0:
            raise AdapterError(
                f"adapter exited {completed.returncode}: {completed.stderr[-3000:]}"
            )
        try:
            payload = json.loads(completed.stdout)
        except json.JSONDecodeError as error:
            raise AdapterError(
                "adapter stdout must be exactly one JSON envelope: "
                f"{error}; stderr tail={completed.stderr[-1000:]!r}"
            ) from error
        return _adapter_output(payload)


def build_adapter_request(
    *,
    task: str,
    model: str,
    reasoning_effort: str,
    prompt: str,
    response_contract: dict[str, Any],
    required_tools: tuple[str, ...] = (),
    available_files: tuple[str, ...] = (),
) -> dict[str, Any]:
    """Build the only payload visible to an external harness adapter."""
    return {
        "schema_version": 1,
        "task": task,
        "model": model,
        "reasoning_effort": reasoning_effort,
        "prompt": prompt,
        "response_contract": response_contract,
        "working_directory": ".",
        "required_tools": list(required_tools),
        "available_files": list(available_files),
    }


def _adapter_output(payload: Any) -> AdapterOutput:
    if not isinstance(payload, dict):
        raise AdapterError("adapter output must be a JSON object")
    if payload.get("schema_version") != 1:
        raise AdapterError("adapter output schema_version must be 1")
    submission = payload.get("submission")
    if not isinstance(submission, dict):
        raise AdapterError("adapter output submission must be an object")
    usage = _integer_map(payload.get("usage", {}), field="usage")
    tool_calls = _integer_map(payload.get("tool_calls", {}), field="tool_calls")
    raw_events = payload.get("events", [])
    if not isinstance(raw_events, list) or not all(
        isinstance(item, dict) for item in raw_events
    ):
        raise AdapterError("adapter output events must be a list of objects")
    metadata = payload.get("metadata", {})
    if not isinstance(metadata, dict):
        raise AdapterError("adapter output metadata must be an object")
    return AdapterOutput(
        submission=submission,
        usage=usage,
        tool_calls=tool_calls,
        events=tuple(raw_events),
        metadata=metadata,
    )


def _command(value: Any, *, field: str) -> list[str]:
    if not isinstance(value, list) or not value:
        raise AdapterError(f"adapter {field} must be a non-empty string list")
    result = []
    for item in value:
        result.append(_nonempty_string(item, field=field))
    return result


def _capabilities(value: Any) -> dict[str, bool]:
    if not isinstance(value, dict):
        raise AdapterError("adapter capabilities must be an object")
    required = {"structured_output", "frozen_search"}
    missing = sorted(required - value.keys())
    if missing:
        raise AdapterError(f"adapter capabilities missing fields: {', '.join(missing)}")
    result = {}
    for key, item in value.items():
        if not isinstance(key, str) or not isinstance(item, bool):
            raise AdapterError("adapter capabilities must map strings to booleans")
        result[key] = item
    if not result["structured_output"]:
        raise AdapterError("adapter must support structured_output")
    return result


def _execution(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise AdapterError("adapter execution must be an object")
    required = {
        "sandbox",
        "external_data_access",
        "session_persistence",
        "outcome_visible_to_agent",
        "reasoning_effort_contract",
    }
    missing = sorted(required - value.keys())
    if missing:
        raise AdapterError(f"adapter execution missing fields: {', '.join(missing)}")
    if value["outcome_visible_to_agent"] is not False:
        raise AdapterError("outcome_visible_to_agent must be false")
    for field in (
        "external_data_access",
        "session_persistence",
        "outcome_visible_to_agent",
    ):
        if not isinstance(value[field], bool):
            raise AdapterError(f"adapter execution {field} must be boolean")
    return {
        "sandbox": _nonempty_string(value["sandbox"], field="execution.sandbox"),
        "external_data_access": value["external_data_access"],
        "session_persistence": value["session_persistence"],
        "outcome_visible_to_agent": value["outcome_visible_to_agent"],
        "reasoning_effort_contract": _nonempty_string(
            value["reasoning_effort_contract"],
            field="execution.reasoning_effort_contract",
        ),
    }


def _integer_map(value: Any, *, field: str) -> dict[str, int]:
    if not isinstance(value, dict):
        raise AdapterError(f"adapter output {field} must be an object")
    result = {}
    for key, item in value.items():
        if (
            not isinstance(key, str)
            or not isinstance(item, int)
            or isinstance(item, bool)
            or item < 0
        ):
            raise AdapterError(
                f"adapter output {field} must map strings to non-negative integers"
            )
        result[key] = item
    return result


def _nonempty_string(value: Any, *, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise AdapterError(f"adapter {field} must be a non-empty string")
    return value.strip()


def _expand_manifest_dir(command: list[str], manifest_dir: Path) -> list[str]:
    return [item.replace("{manifest_dir}", str(manifest_dir)) for item in command]

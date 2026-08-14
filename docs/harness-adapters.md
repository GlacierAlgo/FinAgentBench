# Harness adapter protocol

PITFALL's experiment is a complete configuration: model, reasoning
setting, harness, tools, evidence snapshot, and runtime version. The
`pitfall-stdio-v1` protocol lets a non-Codex harness join that experiment
without importing provider SDKs into the benchmark core.

## Trust boundary

An adapter is trusted measurement code. It receives an outcome-free prompt and
response schema, invokes one model/harness session, and returns the structured
submission plus usage and tool-call diagnostics. It never receives the answer
key, rubric, future label, RQData provenance, or score.

For historical A-share replay the runner creates an isolated temporary folder
containing:

- `scenario.json`, containing the same outcome-free payload as the prompt;
- `frozen-corpus.json`, containing only official documents published by the
  as-of cutoff;
- `frozen_search.py`, the deterministic search implementation.

The adapter manifest must explicitly declare whether it supports frozen search,
whether the harness can reach external data, whether sessions persist, its
sandbox boundary, and how the requested reasoning-effort label maps to the
provider. These declarations and the canonical manifest SHA-256 are bound into
every result artifact.

## Manifest

```json
{
  "schema_version": 1,
  "name": "my-harness",
  "version_command": ["my-harness", "--version"],
  "command": ["python3", "{manifest_dir}/adapter.py"],
  "capabilities": {
    "structured_output": true,
    "frozen_search": true
  },
  "execution": {
    "sandbox": "precise, auditable sandbox description",
    "external_data_access": false,
    "session_persistence": false,
    "outcome_visible_to_agent": false,
    "reasoning_effort_contract": "how low/medium/high is mapped or why provider default is used"
  }
}
```

Use either a fixed `version` string or `version_command`, never both. Command
tokens are executed directly without a shell. `{manifest_dir}` expands to the
absolute directory containing the manifest. Credentials belong in the
harness's normal credential store or environment and must not appear in the
manifest.

## Request and response

The runner writes one request object to adapter stdin:

```json
{
  "schema_version": 1,
  "task": "a_share_frozen_web",
  "model": "provider/model-id",
  "reasoning_effort": "low",
  "prompt": "... outcome-free prompt ...",
  "response_contract": {},
  "working_directory": ".",
  "required_tools": ["frozen_search"],
  "available_files": [
    "scenario.json",
    "frozen-corpus.json",
    "frozen_search.py"
  ]
}
```

The adapter must write exactly one JSON envelope to stdout. Logs go to stderr.

```json
{
  "schema_version": 1,
  "submission": {},
  "usage": {
    "input_tokens": 0,
    "cached_input_tokens": 0,
    "output_tokens": 0
  },
  "tool_calls": {
    "frozen_search": 1
  },
  "events": [],
  "metadata": {
    "reasoning_effort_applied": true
  }
}
```

`usage` and `tool_calls` may include additional non-negative integer fields.
`events` is an optional list of compact event objects; the current historical
runner records its count. `metadata` is optional and should contain only
non-secret experiment diagnostics.

## OpenCode reference adapter

The repository includes
[`examples/adapters/opencode.json`](../examples/adapters/opencode.json) and its
Python adapter. OpenCode supports multiple providers and emits raw JSON events.
The reference adapter parses completed text, tool, and token events. It writes a
temporary OpenCode permission policy that denies all tools for synthetic cases
and, for A-share replay, allows only
`python3 frozen_search.py <query>` while denying every other tool.

Authenticate and verify the desired provider in OpenCode first:

```bash
opencode providers login
opencode models
```

Then run any listed provider/model ID:

```bash
uv run pitfall a-share benchmark \
  --adapter-manifest examples/adapters/opencode.json \
  --model provider/model-id \
  --scenario-id cn-a-2020-cambricon-rd-commercial-validation \
  --output results/opencode-a-share.json \
  --report-output results/opencode-a-share.md
```

OpenCode variants are provider-specific. The reference adapter does not claim
that PITFALL's `low` label was applied unless an explicit mapping exists:

```bash
export PITFALL_OPENCODE_VARIANTS='{"provider/model-id":{"low":"low","high":"high"}}'
```

If no mapping exists, the provider default is used and
`reasoning_effort_applied` is false in each result. The included reference
manifest truthfully records that OpenCode persists local session records even
though every benchmark call starts a new session.

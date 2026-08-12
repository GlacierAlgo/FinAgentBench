# FinAgentBench A-share frozen-web replay

Harness: `codex-cli 0.146.0` · effort: `low` · cases: 1 · repeats: 1
Case suite: `8270063389d3b0fbbe7779d062c8d0a35dca11e36ed1be8e55032187137a7773`

| Model | Score | Brier loss | Log loss | Accuracy | Evidence F1 | Search use | Latency | Failures |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | 91.30 | 0.1024 | 0.3857 | 100.0% | 1.000 | 100.0% | 29.35s | 0 |
| gpt-5.6-sol | 85.01 | 0.1764 | 0.5447 | 100.0% | 1.000 | 100.0% | 41.61s | 0 |
| gpt-5.6-terra | 86.40 | 0.1600 | 0.5108 | 100.0% | 1.000 | 100.0% | 51.86s | 0 |

## Interpretation guardrails

- This is a public historical development set, not a sealed leaderboard.
- Search was restricted to official documents published by each as-of date.
- The outcome label was loaded only after the model returned its prediction.
- Brier and log loss assess probability quality; this run is too small for calibration claims.

## Per-scenario results

| Model | Scenario | Probability | Outcome | Score | Brier loss | Evidence F1 | Searches |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | cn-a-2022-hygon-rd-commercial-validation | 0.680 | event | 91.30 | 0.1024 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2022-hygon-rd-commercial-validation | 0.580 | event | 85.01 | 0.1764 | 1.000 | 7 |
| gpt-5.6-terra | cn-a-2022-hygon-rd-commercial-validation | 0.600 | event | 86.40 | 0.1600 | 1.000 | 3 |

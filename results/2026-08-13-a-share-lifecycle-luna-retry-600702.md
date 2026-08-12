# FinAgentBench A-share frozen-web replay

Harness: `codex-cli-frozen-search codex-cli 0.146.0` · effort: `low` · cases: 1 · repeats: 1
Case suite: `98f5b0c4650421d81fc7ea459fdcc76e40fb04e04b4ae4c199048d7016c1ce4e`

| Model | Score | Brier loss | Log loss | Accuracy | Evidence F1 | Search use | Latency | Failures |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | 99.99 | 0.0001 | 0.0100 | 100.0% | 1.000 | 100.0% | 22.63s | 0 |

## Interpretation guardrails

- This is a public historical development set, not a sealed leaderboard.
- Search was restricted to frozen documents/news published by each as-of date.
- The outcome label was loaded only after the model returned its prediction.
- Brier and log loss assess probability quality; this run is too small for calibration claims.

## Per-scenario results

| Model | Scenario | Probability | Outcome | Score | Brier loss | Evidence F1 | Searches |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | cn-a-2020-occupation-star-st-regime-600702 | 0.010 | no_event | 99.99 | 0.0001 | 1.000 | 2 |

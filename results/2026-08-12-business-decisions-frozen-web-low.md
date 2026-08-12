# FinAgentBench A-share frozen-web replay

Harness: `codex-cli 0.146.0` · effort: `low` · cases: 4 · repeats: 1
Case suite: `2e856b71376b8c5d740b863e5724a21555bfb965303423b96e867d422d23e2ea`

| Model | Score | Brier loss | Log loss | Accuracy | Evidence F1 | Search use | Latency | Failures |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | 93.27 | 0.0792 | 0.3293 | 100.0% | 1.000 | 100.0% | 28.36s | 0 |
| gpt-5.6-sol | 89.91 | 0.1187 | 0.4065 | 100.0% | 1.000 | 100.0% | 33.35s | 0 |
| gpt-5.6-terra | 88.88 | 0.1308 | 0.4459 | 100.0% | 1.000 | 100.0% | 29.06s | 0 |

## Interpretation guardrails

- This is a public historical development set, not a sealed leaderboard.
- Search was restricted to official documents published by each as-of date.
- The outcome label was loaded only after the model returned its prediction.
- Brier and log loss assess probability quality; this run is too small for calibration claims.

## Per-scenario results

| Model | Scenario | Probability | Outcome | Score | Brier loss | Evidence F1 | Searches |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | cn-a-2019-catl-factory-commercial-validation | 0.720 | event | 93.34 | 0.0784 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2020-cambricon-rd-commercial-validation | 0.240 | no_event | 95.10 | 0.0576 | 1.000 | 2 |
| gpt-5.6-luna | cn-a-2021-dynanonic-factory-commercial-validation | 0.280 | no_event | 93.34 | 0.0784 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2022-hygon-rd-commercial-validation | 0.680 | event | 91.30 | 0.1024 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2019-catl-factory-commercial-validation | 0.580 | event | 85.01 | 0.1764 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2020-cambricon-rd-commercial-validation | 0.140 | no_event | 98.33 | 0.0196 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2021-dynanonic-factory-commercial-validation | 0.320 | no_event | 91.30 | 0.1024 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2022-hygon-rd-commercial-validation | 0.580 | event | 85.01 | 0.1764 | 1.000 | 7 |
| gpt-5.6-terra | cn-a-2019-catl-factory-commercial-validation | 0.640 | event | 88.98 | 0.1296 | 1.000 | 1 |
| gpt-5.6-terra | cn-a-2020-cambricon-rd-commercial-validation | 0.270 | no_event | 93.80 | 0.0729 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2021-dynanonic-factory-commercial-validation | 0.380 | no_event | 87.73 | 0.1444 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2022-hygon-rd-commercial-validation | 0.580 | event | 85.01 | 0.1764 | 1.000 | 1 |

# FinAgentBench A-share frozen-web replay

Harness: `codex-cli-frozen-search codex-cli 0.146.0` · effort: `low` · cases: 4 · repeats: 1
Case suite: `41cc8daf94c2994bc4fe6e2a9fe408db94b7c364fd6ad882d79cf847e688c81e`

| Model | Score | Brier loss | Log loss | Accuracy | Evidence F1 | Search use | Latency | Failures |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | 92.40 | 0.0894 | 0.3477 | 100.0% | 1.000 | 100.0% | 26.75s | 0 |
| gpt-5.6-sol | 90.28 | 0.1143 | 0.4023 | 100.0% | 1.000 | 100.0% | 34.17s | 0 |
| gpt-5.6-terra | 91.69 | 0.0977 | 0.3665 | 100.0% | 1.000 | 100.0% | 31.29s | 0 |

## Interpretation guardrails

- This is a public historical development set, not a sealed leaderboard.
- Search was restricted to frozen documents/news published by each as-of date.
- The outcome label was loaded only after the model returned its prediction.
- Brier and log loss assess probability quality; this run is too small for calibration claims.

## Per-scenario results

| Model | Scenario | Probability | Outcome | Score | Brier loss | Evidence F1 | Searches |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | cn-a-2019-catl-factory-commercial-validation | 0.680 | event | 91.30 | 0.1024 | 1.000 | 3 |
| gpt-5.6-luna | cn-a-2020-cambricon-rd-commercial-validation | 0.180 | no_event | 97.25 | 0.0324 | 1.000 | 2 |
| gpt-5.6-luna | cn-a-2021-dynanonic-factory-commercial-validation | 0.380 | no_event | 87.73 | 0.1444 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2022-hygon-rd-commercial-validation | 0.720 | event | 93.34 | 0.0784 | 1.000 | 2 |
| gpt-5.6-sol | cn-a-2019-catl-factory-commercial-validation | 0.560 | event | 83.54 | 0.1936 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2020-cambricon-rd-commercial-validation | 0.180 | no_event | 97.25 | 0.0324 | 1.000 | 6 |
| gpt-5.6-sol | cn-a-2021-dynanonic-factory-commercial-validation | 0.340 | no_event | 90.17 | 0.1156 | 1.000 | 6 |
| gpt-5.6-sol | cn-a-2022-hygon-rd-commercial-validation | 0.660 | event | 90.17 | 0.1156 | 1.000 | 4 |
| gpt-5.6-terra | cn-a-2019-catl-factory-commercial-validation | 0.690 | event | 91.83 | 0.0961 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2020-cambricon-rd-commercial-validation | 0.180 | no_event | 97.25 | 0.0324 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2021-dynanonic-factory-commercial-validation | 0.320 | no_event | 91.30 | 0.1024 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2022-hygon-rd-commercial-validation | 0.600 | event | 86.40 | 0.1600 | 1.000 | 2 |

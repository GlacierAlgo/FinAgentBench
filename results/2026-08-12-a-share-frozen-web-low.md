# FinAgentBench A-share frozen-web replay

Harness: `codex-cli 0.146.0` · effort: `low` · cases: 6 · repeats: 1
Case suite: `d2673f02f6d75b2ef804d448bdd7182db822f3c5eb5704bc21b08acb7f8d2d22`

| Model | Score | Brier loss | Log loss | Accuracy | Evidence F1 | Search use | Latency | Failures |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | 90.75 | 0.1088 | 0.3737 | 83.3% | 1.000 | 100.0% | 46.73s | 0 |
| gpt-5.6-sol | 92.74 | 0.0854 | 0.3328 | 100.0% | 1.000 | 100.0% | 34.70s | 0 |
| gpt-5.6-terra | 94.32 | 0.0668 | 0.2816 | 100.0% | 1.000 | 100.0% | 42.16s | 0 |

## Interpretation guardrails

- This is a public historical development set, not a sealed leaderboard.
- Search was restricted to official documents published by each as-of date.
- The outcome label was loaded only after the model returned its prediction.
- Brier and log loss assess probability quality; six cases are too few for calibration claims.

## Per-scenario results

| Model | Scenario | Probability | Outcome | Score | Brier loss | Evidence F1 | Searches |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | cn-a-2019q3-goodwill-002425 | 0.280 | no_event | 93.34 | 0.0784 | 1.000 | 3 |
| gpt-5.6-luna | cn-a-2019q3-goodwill-002681 | 0.820 | event | 97.25 | 0.0324 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2019q3-goodwill-002739 | 0.820 | event | 97.25 | 0.0324 | 1.000 | 5 |
| gpt-5.6-luna | cn-a-2019q3-goodwill-300058 | 0.560 | no_event | 73.34 | 0.3136 | 1.000 | 3 |
| gpt-5.6-luna | cn-a-2019q3-goodwill-300276 | 0.420 | no_event | 85.01 | 0.1764 | 1.000 | 3 |
| gpt-5.6-luna | cn-a-2019q3-goodwill-300467 | 0.860 | event | 98.33 | 0.0196 | 1.000 | 3 |
| gpt-5.6-sol | cn-a-2019q3-goodwill-002425 | 0.220 | no_event | 95.89 | 0.0484 | 1.000 | 8 |
| gpt-5.6-sol | cn-a-2019q3-goodwill-002681 | 0.580 | event | 85.01 | 0.1764 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2019q3-goodwill-002739 | 0.620 | event | 87.73 | 0.1444 | 1.000 | 6 |
| gpt-5.6-sol | cn-a-2019q3-goodwill-300058 | 0.180 | no_event | 97.25 | 0.0324 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2019q3-goodwill-300276 | 0.180 | no_event | 97.25 | 0.0324 | 1.000 | 2 |
| gpt-5.6-sol | cn-a-2019q3-goodwill-300467 | 0.720 | event | 93.34 | 0.0784 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2019q3-goodwill-002425 | 0.160 | no_event | 97.82 | 0.0256 | 1.000 | 5 |
| gpt-5.6-terra | cn-a-2019q3-goodwill-002681 | 0.860 | event | 98.33 | 0.0196 | 1.000 | 4 |
| gpt-5.6-terra | cn-a-2019q3-goodwill-002739 | 0.720 | event | 93.34 | 0.0784 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2019q3-goodwill-300058 | 0.150 | no_event | 98.09 | 0.0225 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2019q3-goodwill-300276 | 0.420 | no_event | 85.01 | 0.1764 | 1.000 | 5 |
| gpt-5.6-terra | cn-a-2019q3-goodwill-300467 | 0.720 | event | 93.34 | 0.0784 | 1.000 | 4 |

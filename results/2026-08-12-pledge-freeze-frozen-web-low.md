# FinAgentBench A-share frozen-web replay

Harness: `codex-cli-frozen-search codex-cli 0.146.0` · effort: `low` · cases: 2 · repeats: 1
Case suite: `ac2d1fdf1345b1d43baec20d7caaa33ce35b79a52cd299fb17e5fce851992063`

| Model | Score | Brier loss | Log loss | Accuracy | Evidence F1 | Search use | Latency | Failures |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | 81.35 | 0.2194 | 0.6266 | 50.0% | 1.000 | 100.0% | 28.02s | 0 |
| gpt-5.6-sol | 87.40 | 0.1482 | 0.4862 | 100.0% | 1.000 | 100.0% | 33.50s | 0 |
| gpt-5.6-terra | 88.95 | 0.1300 | 0.4468 | 100.0% | 1.000 | 100.0% | 35.16s | 0 |

## Interpretation guardrails

- This is a public historical development set, not a sealed leaderboard.
- Search was restricted to frozen documents/news published by each as-of date.
- The outcome label was loaded only after the model returned its prediction.
- Brier and log loss assess probability quality; this run is too small for calibration claims.

## Per-scenario results

| Model | Scenario | Probability | Outcome | Score | Brier loss | Evidence F1 | Searches |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | cn-a-2017q3-pledge-freeze-603766 | 0.320 | no_event | 91.30 | 0.1024 | 1.000 | 2 |
| gpt-5.6-luna | cn-a-2018q3-pledge-freeze-603766 | 0.420 | event | 71.41 | 0.3364 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2017q3-pledge-freeze-603766 | 0.380 | no_event | 87.73 | 0.1444 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2018q3-pledge-freeze-603766 | 0.610 | event | 87.07 | 0.1521 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2017q3-pledge-freeze-603766 | 0.340 | no_event | 90.17 | 0.1156 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2018q3-pledge-freeze-603766 | 0.620 | event | 87.73 | 0.1444 | 1.000 | 3 |

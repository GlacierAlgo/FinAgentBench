# FinAgentBench A-share frozen-web replay

Harness: `codex-cli-frozen-search codex-cli 0.146.0` · effort: `low` · cases: 8 · repeats: 1
Case suite: `196650bd13d3badb377f85b102fc451d69ed605c98989d6a2a43699f992e03a4`

| Model | Score | Brier loss | Log loss | Accuracy | Evidence F1 | Search use | Latency | Failures |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | 79.68 | 0.2391 | 0.6678 | 50.0% | 1.000 | 100.0% | 29.73s | 0 |
| gpt-5.6-sol | 82.06 | 0.2111 | 0.6089 | 62.5% | 1.000 | 100.0% | 39.59s | 0 |
| gpt-5.6-terra | 77.27 | 0.2674 | 0.7271 | 42.9% | 1.000 | 100.0% | 32.12s | 1 |

## Interpretation guardrails

- This is a public historical development set, not a sealed leaderboard.
- Search was restricted to frozen documents/news published by each as-of date.
- The outcome label was loaded only after the model returned its prediction.
- Brier and log loss assess probability quality; this run is too small for calibration claims.

## Per-scenario results

| Model | Scenario | Probability | Outcome | Score | Brier loss | Evidence F1 | Searches |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | cn-a-2025-auto-payment-cycle-000700 | 0.420 | event | 71.41 | 0.3364 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2025-auto-payment-cycle-002284 | 0.320 | event | 60.70 | 0.4624 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2025-auto-payment-cycle-300258 | 0.420 | event | 71.41 | 0.3364 | 1.000 | 5 |
| gpt-5.6-luna | cn-a-2025-auto-payment-cycle-600660 | 0.420 | event | 71.41 | 0.3364 | 1.000 | 2 |
| gpt-5.6-luna | cn-a-2025-auto-payment-cycle-600741 | 0.250 | no_event | 94.69 | 0.0625 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2025-auto-payment-cycle-600933 | 0.380 | no_event | 87.73 | 0.1444 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2025-auto-payment-cycle-601689 | 0.380 | no_event | 87.73 | 0.1444 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2025-auto-payment-cycle-601799 | 0.300 | no_event | 92.35 | 0.0900 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2025-auto-payment-cycle-000700 | 0.580 | event | 85.01 | 0.1764 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2025-auto-payment-cycle-002284 | 0.430 | event | 72.38 | 0.3249 | 1.000 | 7 |
| gpt-5.6-sol | cn-a-2025-auto-payment-cycle-300258 | 0.440 | event | 73.34 | 0.3136 | 1.000 | 8 |
| gpt-5.6-sol | cn-a-2025-auto-payment-cycle-600660 | 0.320 | event | 60.70 | 0.4624 | 1.000 | 8 |
| gpt-5.6-sol | cn-a-2025-auto-payment-cycle-600741 | 0.270 | no_event | 93.80 | 0.0729 | 1.000 | 9 |
| gpt-5.6-sol | cn-a-2025-auto-payment-cycle-600933 | 0.430 | no_event | 84.28 | 0.1849 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2025-auto-payment-cycle-601689 | 0.240 | no_event | 95.10 | 0.0576 | 1.000 | 7 |
| gpt-5.6-sol | cn-a-2025-auto-payment-cycle-601799 | 0.310 | no_event | 91.83 | 0.0961 | 1.000 | 5 |
| gpt-5.6-terra | cn-a-2025-auto-payment-cycle-000700 | 0.340 | event | 62.97 | 0.4356 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2025-auto-payment-cycle-002284 | 0.360 | event | 65.18 | 0.4096 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2025-auto-payment-cycle-300258 | 0.400 | event | 69.40 | 0.3600 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2025-auto-payment-cycle-600660 | 0.420 | event | 71.41 | 0.3364 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2025-auto-payment-cycle-600741 | — | — | failed | — | — | — |
| gpt-5.6-terra | cn-a-2025-auto-payment-cycle-600933 | 0.380 | no_event | 87.73 | 0.1444 | 1.000 | 1 |
| gpt-5.6-terra | cn-a-2025-auto-payment-cycle-601689 | 0.300 | no_event | 92.35 | 0.0900 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2025-auto-payment-cycle-601799 | 0.310 | no_event | 91.83 | 0.0961 | 1.000 | 2 |

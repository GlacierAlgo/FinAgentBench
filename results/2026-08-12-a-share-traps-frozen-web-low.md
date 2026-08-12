# FinAgentBench A-share frozen-web replay

Harness: `codex-cli 0.146.0` · effort: `low` · cases: 12 · repeats: 1
Case suite: `a6cbd558b1fb4ee90b2b576a889edee8a21393bfb43222cd046dc6dd4ae60c1b`

| Model | Score | Brier loss | Log loss | Accuracy | Evidence F1 | Search use | Latency | Failures |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | 84.11 | 0.1870 | 0.5608 | 75.0% | 1.000 | 100.0% | 30.91s | 0 |
| gpt-5.6-sol | 85.79 | 0.1672 | 0.5073 | 83.3% | 1.000 | 100.0% | 35.09s | 0 |
| gpt-5.6-terra | 78.25 | 0.2558 | 0.6945 | 50.0% | 1.000 | 100.0% | 41.11s | 0 |

## Interpretation guardrails

- This is a public historical development set, not a sealed leaderboard.
- Search was restricted to official documents published by each as-of date.
- The outcome label was loaded only after the model returned its prediction.
- Brier and log loss assess probability quality; this run is too small for calibration claims.

## Per-scenario results

| Model | Scenario | Probability | Outcome | Score | Brier loss | Evidence F1 | Searches |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | cn-a-2017q3-pledge-control-002310 | 0.560 | no_event | 73.34 | 0.3136 | 1.000 | 3 |
| gpt-5.6-luna | cn-a-2018q3-pledge-control-002310 | 0.680 | event | 91.30 | 0.1024 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2019q3-inventory-300278 | 0.680 | event | 91.30 | 0.1024 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2019q3-inventory-300442 | 0.180 | no_event | 97.25 | 0.0324 | 1.000 | 3 |
| gpt-5.6-luna | cn-a-2019q3-performance-commitment-300276 | 0.350 | no_event | 89.59 | 0.1225 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2019q3-performance-commitment-300467 | 0.780 | event | 95.89 | 0.0484 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2019q3-receivables-300455 | 0.120 | no_event | 98.78 | 0.0144 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2019q3-receivables-300461 | 0.680 | event | 91.30 | 0.1024 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2022q3-audit-opinion-000506 | 0.720 | no_event | 55.94 | 0.5184 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2023q3-audit-opinion-000506 | 0.620 | event | 87.73 | 0.1444 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2023q3-st-transition-002786 | 0.800 | no_event | 45.60 | 0.6400 | 1.000 | 7 |
| gpt-5.6-luna | cn-a-2023q3-st-transition-600375 | 0.680 | event | 91.30 | 0.1024 | 1.000 | 3 |
| gpt-5.6-sol | cn-a-2017q3-pledge-control-002310 | 0.200 | no_event | 96.60 | 0.0400 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2018q3-pledge-control-002310 | 0.620 | event | 87.73 | 0.1444 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2019q3-inventory-300278 | 0.580 | event | 85.01 | 0.1764 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2019q3-inventory-300442 | 0.240 | no_event | 95.10 | 0.0576 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2019q3-performance-commitment-300276 | 0.280 | no_event | 93.34 | 0.0784 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2019q3-performance-commitment-300467 | 0.740 | event | 94.25 | 0.0676 | 1.000 | 3 |
| gpt-5.6-sol | cn-a-2019q3-receivables-300455 | 0.020 | no_event | 99.97 | 0.0004 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2019q3-receivables-300461 | 0.620 | event | 87.73 | 0.1444 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2022q3-audit-opinion-000506 | 0.780 | no_event | 48.29 | 0.6084 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2023q3-audit-opinion-000506 | 0.620 | event | 87.73 | 0.1444 | 1.000 | 8 |
| gpt-5.6-sol | cn-a-2023q3-st-transition-002786 | 0.720 | no_event | 55.94 | 0.5184 | 1.000 | 9 |
| gpt-5.6-sol | cn-a-2023q3-st-transition-600375 | 0.840 | event | 97.82 | 0.0256 | 1.000 | 8 |
| gpt-5.6-terra | cn-a-2017q3-pledge-control-002310 | 0.240 | no_event | 95.10 | 0.0576 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2018q3-pledge-control-002310 | 0.430 | event | 72.38 | 0.3249 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2019q3-inventory-300278 | 0.420 | event | 71.41 | 0.3364 | 1.000 | 5 |
| gpt-5.6-terra | cn-a-2019q3-inventory-300442 | 0.420 | no_event | 85.01 | 0.1764 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2019q3-performance-commitment-300276 | 0.630 | no_event | 66.26 | 0.3969 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2019q3-performance-commitment-300467 | 0.720 | event | 93.34 | 0.0784 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2019q3-receivables-300455 | 0.040 | no_event | 99.86 | 0.0016 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2019q3-receivables-300461 | 0.250 | event | 52.19 | 0.5625 | 1.000 | 4 |
| gpt-5.6-terra | cn-a-2022q3-audit-opinion-000506 | 0.700 | no_event | 58.35 | 0.4900 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2023q3-audit-opinion-000506 | 0.720 | event | 93.34 | 0.0784 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2023q3-st-transition-002786 | 0.720 | no_event | 55.94 | 0.5184 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2023q3-st-transition-600375 | 0.780 | event | 95.89 | 0.0484 | 1.000 | 4 |

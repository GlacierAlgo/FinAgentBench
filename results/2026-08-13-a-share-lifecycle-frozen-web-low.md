# FinAgentBench A-share frozen-web replay

Harness: `codex-cli-frozen-search codex-cli 0.146.0` · effort: `low` · cases: 52 · repeats: 1
Case suite: `3cd8ac5e18967cf53d7ebdcda6977e66182e614ef12b5fce4c190d4f4fcb99d2`

| Model | Score | Brier loss | Log loss | Accuracy | Evidence F1 | Search use | Latency | Failures |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | 85.95 | 0.1652 | 0.4815 | 72.5% | 1.000 | 100.0% | 30.39s | 1 |
| gpt-5.6-sol | 88.14 | 0.1396 | 0.4212 | 80.8% | 1.000 | 100.0% | 39.49s | 0 |
| gpt-5.6-terra | 87.97 | 0.1416 | 0.4234 | 76.9% | 1.000 | 100.0% | 33.50s | 0 |

## Interpretation guardrails

- This is a public historical development set, not a sealed leaderboard.
- Search was restricted to frozen documents/news published by each as-of date.
- The outcome label was loaded only after the model returned its prediction.
- Brier and log loss assess probability quality; this run is too small for calibration claims.

## Per-scenario results

| Model | Scenario | Probability | Outcome | Score | Brier loss | Evidence F1 | Searches |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| gpt-5.6-luna | cn-a-2014-new-industry-scale-600766 | 0.150 | no_event | 98.09 | 0.0225 | 1.000 | 5 |
| gpt-5.6-luna | cn-a-2014-new-media-shutdown-12m-002306 | 0.680 | event | 91.30 | 0.1024 | 1.000 | 5 |
| gpt-5.6-luna | cn-a-2014-public-bond-default-6m-002306 | 0.880 | event | 98.78 | 0.0144 | 1.000 | 5 |
| gpt-5.6-luna | cn-a-2015-acquisition-commitment-validation-000547 | 0.350 | event | 64.09 | 0.4225 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2015-cross-industry-scale-002027 | 0.900 | event | 99.15 | 0.0100 | 1.000 | 5 |
| gpt-5.6-luna | cn-a-2015-new-industry-scale-600862 | 0.420 | event | 71.41 | 0.3364 | 1.000 | 5 |
| gpt-5.6-luna | cn-a-2015-new-segment-scale-600696 | 0.180 | no_event | 97.25 | 0.0324 | 1.000 | 5 |
| gpt-5.6-luna | cn-a-2015-repeat-st-600381 | 0.720 | event | 93.34 | 0.0784 | 1.000 | 6 |
| gpt-5.6-luna | cn-a-2016-backdoor-sustained-000820 | 0.350 | no_event | 89.59 | 0.1225 | 1.000 | 5 |
| gpt-5.6-luna | cn-a-2016-cross-industry-scale-002260 | 0.080 | no_event | 99.46 | 0.0064 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2016-repeat-st-002306 | 0.720 | event | 93.34 | 0.0784 | 1.000 | 7 |
| gpt-5.6-luna | cn-a-2016-repeat-st-600381 | 0.620 | no_event | 67.33 | 0.3844 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2016-st-recurrence-24m-002306 | 0.820 | event | 97.25 | 0.0324 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2017-backdoor-sustained-600760 | 0.680 | event | 91.30 | 0.1024 | 1.000 | 7 |
| gpt-5.6-luna | cn-a-2017-full-risk-warning-removal-24m-002306 | 0.080 | no_event | 99.46 | 0.0064 | 1.000 | 7 |
| gpt-5.6-luna | cn-a-2017-new-segment-scale-600882 | 0.350 | event | 64.09 | 0.4225 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2017-repeat-st-000504 | 0.650 | event | 89.59 | 0.1225 | 1.000 | 5 |
| gpt-5.6-luna | cn-a-2017-shengyun-waste-project-commercial-validation | 0.120 | no_event | 98.78 | 0.0144 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2017-shenwu-technology-commercial-validation | 0.120 | no_event | 98.78 | 0.0144 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2017-weiming-waste-project-commercial-validation | 0.780 | event | 95.89 | 0.0484 | 1.000 | 2 |
| gpt-5.6-luna | cn-a-2018-governance-cash-compensation-603188 | 0.250 | event | 52.19 | 0.5625 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2018-major-illegal-delisting-002680 | 0.990 | event | 99.99 | 0.0001 | 1.000 | 2 |
| gpt-5.6-luna | cn-a-2018-naura-technology-commercial-validation | 0.720 | event | 93.34 | 0.0784 | 1.000 | 3 |
| gpt-5.6-luna | cn-a-2018-repeat-st-600225 | 0.720 | event | 93.34 | 0.0784 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2018-tianshen-acquisition-commercial-validation | 0.280 | no_event | 93.34 | 0.0784 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2019-audit-opinion-star-st-600518 | 0.010 | no_event | 99.99 | 0.0001 | 1.000 | 2 |
| gpt-5.6-luna | cn-a-2019-governance-fund-recovery-600290 | 0.080 | no_event | 99.46 | 0.0064 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2019-governance-share-compensation-600666 | 0.080 | no_event | 99.46 | 0.0064 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2020-acquisition-commitment-validation-000004 | 0.420 | no_event | 85.01 | 0.1764 | 1.000 | 5 |
| gpt-5.6-luna | cn-a-2020-audit-opinion-star-st-000408 | 0.990 | event | 99.99 | 0.0001 | 1.000 | 2 |
| gpt-5.6-luna | cn-a-2020-governance-fund-recovery-600702 | 0.300 | event | 58.35 | 0.4900 | 1.000 | 3 |
| gpt-5.6-luna | cn-a-2020-governance-guarantee-release-002650 | 0.180 | event | 42.85 | 0.6724 | 1.000 | 3 |
| gpt-5.6-luna | cn-a-2020-governance-guarantee-release-002656 | 0.120 | no_event | 98.78 | 0.0144 | 1.000 | 5 |
| gpt-5.6-luna | cn-a-2020-governance-share-compensation-300266 | 0.180 | event | 42.85 | 0.6724 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2020-major-illegal-delisting-600518 | 0.420 | no_event | 85.01 | 0.1764 | 1.000 | 3 |
| gpt-5.6-luna | cn-a-2020-occupation-star-st-regime-600702 | — | — | failed | — | — | — |
| gpt-5.6-luna | cn-a-2020-shanshan-acquisition-commercial-validation | 0.560 | event | 83.54 | 0.1936 | 1.000 | 3 |
| gpt-5.6-luna | cn-a-2021-game-segment-divestiture-24m-002555 | 0.080 | no_event | 99.46 | 0.0064 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2021-repeat-st-000408 | 0.420 | no_event | 85.01 | 0.1764 | 1.000 | 6 |
| gpt-5.6-luna | cn-a-2021-repeat-st-000504 | 0.620 | no_event | 67.33 | 0.3844 | 1.000 | 2 |
| gpt-5.6-luna | cn-a-2021-repeat-st-002168 | 0.720 | event | 93.34 | 0.0784 | 1.000 | 6 |
| gpt-5.6-luna | cn-a-2021-repeat-st-002306 | 0.620 | no_event | 67.33 | 0.3844 | 1.000 | 5 |
| gpt-5.6-luna | cn-a-2021-repeat-st-002650 | 0.680 | event | 91.30 | 0.1024 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2021-repeat-st-600080 | 0.580 | no_event | 71.41 | 0.3364 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2021-repeat-st-600860 | 0.580 | no_event | 71.41 | 0.3364 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2022-battery-operation-24m-002634 | 0.350 | event | 64.09 | 0.4225 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2022-game-segment-divestiture-24m-002306 | 0.250 | event | 52.19 | 0.5625 | 1.000 | 5 |
| gpt-5.6-luna | cn-a-2022-governance-cash-compensation-300709 | 0.150 | no_event | 98.09 | 0.0225 | 1.000 | 2 |
| gpt-5.6-luna | cn-a-2023-battery-operation-24m-002306 | 0.180 | no_event | 97.25 | 0.0324 | 1.000 | 4 |
| gpt-5.6-luna | cn-a-2025-financial-star-st-regime-603580 | 0.980 | event | 99.97 | 0.0004 | 1.000 | 2 |
| gpt-5.6-luna | cn-a-2025-financial-star-st-regime-688004 | 0.010 | no_event | 99.99 | 0.0001 | 1.000 | 2 |
| gpt-5.6-luna | cn-a-2025-occupation-star-st-regime-000040 | 0.970 | event | 99.92 | 0.0009 | 1.000 | 2 |
| gpt-5.6-sol | cn-a-2014-new-industry-scale-600766 | 0.220 | no_event | 95.89 | 0.0484 | 1.000 | 7 |
| gpt-5.6-sol | cn-a-2014-new-media-shutdown-12m-002306 | 0.620 | event | 87.73 | 0.1444 | 1.000 | 8 |
| gpt-5.6-sol | cn-a-2014-public-bond-default-6m-002306 | 0.840 | event | 97.82 | 0.0256 | 1.000 | 3 |
| gpt-5.6-sol | cn-a-2015-acquisition-commitment-validation-000547 | 0.580 | event | 85.01 | 0.1764 | 1.000 | 8 |
| gpt-5.6-sol | cn-a-2015-cross-industry-scale-002027 | 0.900 | event | 99.15 | 0.0100 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2015-new-industry-scale-600862 | 0.920 | event | 99.46 | 0.0064 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2015-new-segment-scale-600696 | 0.180 | no_event | 97.25 | 0.0324 | 1.000 | 6 |
| gpt-5.6-sol | cn-a-2015-repeat-st-600381 | 0.420 | event | 71.41 | 0.3364 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2016-backdoor-sustained-000820 | 0.670 | no_event | 61.84 | 0.4489 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2016-cross-industry-scale-002260 | 0.030 | no_event | 99.92 | 0.0009 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2016-repeat-st-002306 | 0.670 | event | 90.74 | 0.1089 | 1.000 | 8 |
| gpt-5.6-sol | cn-a-2016-repeat-st-600381 | 0.380 | no_event | 87.73 | 0.1444 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2016-st-recurrence-24m-002306 | 0.680 | event | 91.30 | 0.1024 | 1.000 | 6 |
| gpt-5.6-sol | cn-a-2017-backdoor-sustained-600760 | 0.820 | event | 97.25 | 0.0324 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2017-full-risk-warning-removal-24m-002306 | 0.180 | no_event | 97.25 | 0.0324 | 1.000 | 8 |
| gpt-5.6-sol | cn-a-2017-new-segment-scale-600882 | 0.620 | event | 87.73 | 0.1444 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2017-repeat-st-000504 | 0.680 | event | 91.30 | 0.1024 | 1.000 | 8 |
| gpt-5.6-sol | cn-a-2017-shengyun-waste-project-commercial-validation | 0.240 | no_event | 95.10 | 0.0576 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2017-shenwu-technology-commercial-validation | 0.270 | no_event | 93.80 | 0.0729 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2017-weiming-waste-project-commercial-validation | 0.680 | event | 91.30 | 0.1024 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2018-governance-cash-compensation-603188 | 0.280 | event | 55.94 | 0.5184 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2018-major-illegal-delisting-002680 | 0.960 | event | 99.86 | 0.0016 | 1.000 | 3 |
| gpt-5.6-sol | cn-a-2018-naura-technology-commercial-validation | 0.620 | event | 87.73 | 0.1444 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2018-repeat-st-600225 | 0.620 | event | 87.73 | 0.1444 | 1.000 | 8 |
| gpt-5.6-sol | cn-a-2018-tianshen-acquisition-commercial-validation | 0.360 | no_event | 88.98 | 0.1296 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2019-audit-opinion-star-st-600518 | 0.010 | no_event | 99.99 | 0.0001 | 1.000 | 3 |
| gpt-5.6-sol | cn-a-2019-governance-fund-recovery-600290 | 0.060 | no_event | 99.69 | 0.0036 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2019-governance-share-compensation-600666 | 0.040 | no_event | 99.86 | 0.0016 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2020-acquisition-commitment-validation-000004 | 0.430 | no_event | 84.28 | 0.1849 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2020-audit-opinion-star-st-000408 | 0.990 | event | 99.99 | 0.0001 | 1.000 | 6 |
| gpt-5.6-sol | cn-a-2020-governance-fund-recovery-600702 | 0.280 | event | 55.94 | 0.5184 | 1.000 | 2 |
| gpt-5.6-sol | cn-a-2020-governance-guarantee-release-002650 | 0.380 | event | 67.33 | 0.3844 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2020-governance-guarantee-release-002656 | 0.100 | no_event | 99.15 | 0.0100 | 1.000 | 11 |
| gpt-5.6-sol | cn-a-2020-governance-share-compensation-300266 | 0.280 | event | 55.94 | 0.5184 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2020-major-illegal-delisting-600518 | 0.080 | no_event | 99.46 | 0.0064 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2020-occupation-star-st-regime-600702 | 0.020 | no_event | 99.97 | 0.0004 | 1.000 | 2 |
| gpt-5.6-sol | cn-a-2020-shanshan-acquisition-commercial-validation | 0.620 | event | 87.73 | 0.1444 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2021-game-segment-divestiture-24m-002555 | 0.030 | no_event | 99.92 | 0.0009 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2021-repeat-st-000408 | 0.340 | no_event | 90.17 | 0.1156 | 1.000 | 8 |
| gpt-5.6-sol | cn-a-2021-repeat-st-000504 | 0.610 | no_event | 68.37 | 0.3721 | 1.000 | 8 |
| gpt-5.6-sol | cn-a-2021-repeat-st-002168 | 0.640 | event | 88.98 | 0.1296 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2021-repeat-st-002306 | 0.620 | no_event | 67.33 | 0.3844 | 1.000 | 7 |
| gpt-5.6-sol | cn-a-2021-repeat-st-002650 | 0.620 | event | 87.73 | 0.1444 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2021-repeat-st-600080 | 0.420 | no_event | 85.01 | 0.1764 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2021-repeat-st-600860 | 0.430 | no_event | 84.28 | 0.1849 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2022-battery-operation-24m-002634 | 0.380 | event | 67.33 | 0.3844 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2022-game-segment-divestiture-24m-002306 | 0.380 | event | 67.33 | 0.3844 | 1.000 | 8 |
| gpt-5.6-sol | cn-a-2022-governance-cash-compensation-300709 | 0.150 | no_event | 98.09 | 0.0225 | 1.000 | 5 |
| gpt-5.6-sol | cn-a-2023-battery-operation-24m-002306 | 0.340 | no_event | 90.17 | 0.1156 | 1.000 | 6 |
| gpt-5.6-sol | cn-a-2025-financial-star-st-regime-603580 | 0.990 | event | 99.99 | 0.0001 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2025-financial-star-st-regime-688004 | 0.010 | no_event | 99.99 | 0.0001 | 1.000 | 4 |
| gpt-5.6-sol | cn-a-2025-occupation-star-st-regime-000040 | 0.960 | event | 99.86 | 0.0016 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2014-new-industry-scale-600766 | 0.160 | no_event | 97.82 | 0.0256 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2014-new-media-shutdown-12m-002306 | 0.740 | event | 94.25 | 0.0676 | 1.000 | 4 |
| gpt-5.6-terra | cn-a-2014-public-bond-default-6m-002306 | 0.720 | event | 93.34 | 0.0784 | 1.000 | 4 |
| gpt-5.6-terra | cn-a-2015-acquisition-commitment-validation-000547 | 0.390 | event | 68.37 | 0.3721 | 1.000 | 8 |
| gpt-5.6-terra | cn-a-2015-cross-industry-scale-002027 | 0.840 | event | 97.82 | 0.0256 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2015-new-industry-scale-600862 | 0.820 | event | 97.25 | 0.0324 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2015-new-segment-scale-600696 | 0.120 | no_event | 98.78 | 0.0144 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2015-repeat-st-600381 | 0.720 | event | 93.34 | 0.0784 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2016-backdoor-sustained-000820 | 0.240 | no_event | 95.10 | 0.0576 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2016-cross-industry-scale-002260 | 0.030 | no_event | 99.92 | 0.0009 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2016-repeat-st-002306 | 0.720 | event | 93.34 | 0.0784 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2016-repeat-st-600381 | 0.320 | no_event | 91.30 | 0.1024 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2016-st-recurrence-24m-002306 | 0.720 | event | 93.34 | 0.0784 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2017-backdoor-sustained-600760 | 0.820 | event | 97.25 | 0.0324 | 1.000 | 4 |
| gpt-5.6-terra | cn-a-2017-full-risk-warning-removal-24m-002306 | 0.120 | no_event | 98.78 | 0.0144 | 1.000 | 4 |
| gpt-5.6-terra | cn-a-2017-new-segment-scale-600882 | 0.300 | event | 58.35 | 0.4900 | 1.000 | 4 |
| gpt-5.6-terra | cn-a-2017-repeat-st-000504 | 0.610 | event | 87.07 | 0.1521 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2017-shengyun-waste-project-commercial-validation | 0.220 | no_event | 95.89 | 0.0484 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2017-shenwu-technology-commercial-validation | 0.240 | no_event | 95.10 | 0.0576 | 1.000 | 4 |
| gpt-5.6-terra | cn-a-2017-weiming-waste-project-commercial-validation | 0.780 | event | 95.89 | 0.0484 | 1.000 | 4 |
| gpt-5.6-terra | cn-a-2018-governance-cash-compensation-603188 | 0.280 | event | 55.94 | 0.5184 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2018-major-illegal-delisting-002680 | 0.950 | event | 99.79 | 0.0025 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2018-naura-technology-commercial-validation | 0.720 | event | 93.34 | 0.0784 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2018-repeat-st-600225 | 0.660 | event | 90.17 | 0.1156 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2018-tianshen-acquisition-commercial-validation | 0.320 | no_event | 91.30 | 0.1024 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2019-audit-opinion-star-st-600518 | 0.010 | no_event | 99.99 | 0.0001 | 1.000 | 1 |
| gpt-5.6-terra | cn-a-2019-governance-fund-recovery-600290 | 0.080 | no_event | 99.46 | 0.0064 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2019-governance-share-compensation-600666 | 0.080 | no_event | 99.46 | 0.0064 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2020-acquisition-commitment-validation-000004 | 0.420 | no_event | 85.01 | 0.1764 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2020-audit-opinion-star-st-000408 | 0.990 | event | 99.99 | 0.0001 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2020-governance-fund-recovery-600702 | 0.320 | event | 60.70 | 0.4624 | 1.000 | 4 |
| gpt-5.6-terra | cn-a-2020-governance-guarantee-release-002650 | 0.280 | event | 55.94 | 0.5184 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2020-governance-guarantee-release-002656 | 0.100 | no_event | 99.15 | 0.0100 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2020-governance-share-compensation-300266 | 0.280 | event | 55.94 | 0.5184 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2020-major-illegal-delisting-600518 | 0.080 | no_event | 99.46 | 0.0064 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2020-occupation-star-st-regime-600702 | 0.010 | no_event | 99.99 | 0.0001 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2020-shanshan-acquisition-commercial-validation | 0.380 | event | 67.33 | 0.3844 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2021-game-segment-divestiture-24m-002555 | 0.020 | no_event | 99.97 | 0.0004 | 1.000 | 4 |
| gpt-5.6-terra | cn-a-2021-repeat-st-000408 | 0.280 | no_event | 93.34 | 0.0784 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2021-repeat-st-000504 | 0.580 | no_event | 71.41 | 0.3364 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2021-repeat-st-002168 | 0.680 | event | 91.30 | 0.1024 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2021-repeat-st-002306 | 0.740 | no_event | 53.45 | 0.5476 | 1.000 | 1 |
| gpt-5.6-terra | cn-a-2021-repeat-st-002650 | 0.700 | event | 92.35 | 0.0900 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2021-repeat-st-600080 | 0.620 | no_event | 67.33 | 0.3844 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2021-repeat-st-600860 | 0.600 | no_event | 69.40 | 0.3600 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2022-battery-operation-24m-002634 | 0.280 | event | 55.94 | 0.5184 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2022-game-segment-divestiture-24m-002306 | 0.640 | event | 88.98 | 0.1296 | 1.000 | 4 |
| gpt-5.6-terra | cn-a-2022-governance-cash-compensation-300709 | 0.060 | no_event | 99.69 | 0.0036 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2023-battery-operation-24m-002306 | 0.220 | no_event | 95.89 | 0.0484 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2025-financial-star-st-regime-603580 | 0.990 | event | 99.99 | 0.0001 | 1.000 | 2 |
| gpt-5.6-terra | cn-a-2025-financial-star-st-regime-688004 | 0.010 | no_event | 99.99 | 0.0001 | 1.000 | 3 |
| gpt-5.6-terra | cn-a-2025-occupation-star-st-regime-000040 | 0.980 | event | 99.97 | 0.0004 | 1.000 | 2 |

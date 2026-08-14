# dividend-yield-cut-risk

## Question

A colleague says: 'A 12% dividend yield guarantees a high cash return next year.' Assess the premise and predict the risk of a dividend cut during the horizon.

### 任务边界 / Task boundary

- 信息截止 / As of: 2025-10-15
- 预测区间 / Horizon: next 12 months
- 会计辖区 / Jurisdiction: Generic corporate finance analysis

### 已知资料 / Evidence

### dividend-cash

- 观察日期 / Observed: 2025-10-10
- 来源 / Source: Synthetic dividend schedule

The current annual dividend requires CU 120 million of cash.

### free-cash-flow

- 观察日期 / Observed: 2025-10-10
- 来源 / Source: Synthetic cash-flow forecast

Trailing free cash flow was CU 70 million and management's base case for next year is CU 65-80 million.

### leverage

- 观察日期 / Observed: 2025-10-10
- 来源 / Source: Synthetic debt note

Net leverage is 4.8x, above the board's 3.5x target.

### distribution-covenant

- 观察日期 / Observed: 2025-10-10
- 来源 / Source: Synthetic facility agreement

The revolving facility prohibits distributions when net leverage exceeds 4.5x unless lenders waive the restriction.

### maturity

- 观察日期 / Observed: 2025-10-10
- 来源 / Source: Synthetic maturity schedule

CU 300 million of debt matures in nine months and refinancing discussions are incomplete.

### share-price

- 观察日期 / Observed: 2025-10-15
- 来源 / Source: Synthetic PIT market snapshot

The share price declined 38% over the prior six months, mechanically raising the trailing dividend yield.

### brand-campaign

- 观察日期 / Observed: 2025-10-01
- 来源 / Source: Synthetic marketing release

The company launched a new advertising campaign.

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Prediction: **high**
- 前提判断 / Premise: **invalid**
- 决定性资料 / Decisive evidence: `dividend-cash`, `free-cash-flow`, `leverage`, `distribution-covenant`, `maturity`, `share-price`

### 判定要点 / Decisive points

- Recognises yield as price-relative, not a guaranteed future payment.
- Compares dividend cash needs with free cash flow.
- Uses leverage, covenant, and maturity constraints.
- Predicts high cut risk without claiming the board decision is known.

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: synthetic
- **legacy_title**: High dividend yield versus sustainable cash return
- **legacy_category**: equity-income

</details>

# operating-leverage-eps

## Question

A colleague says: 'If revenue falls 5%, EPS should also fall about 5%.' Assess the premise and predict the likelihood that EPS falls by more than 15% under the supplied scenario.

### 任务边界 / Task boundary

- 信息截止 / As of: 2025-11-01
- 预测区间 / Horizon: next fiscal year under the supplied scenario
- 会计辖区 / Jurisdiction: Generic management accounting

### 已知资料 / Evidence

### base-income

- 观察日期 / Observed: 2025-11-01
- 来源 / Source: Synthetic base-case income statement

Base revenue is CU 1.0 billion, variable operating costs are CU 400 million, and fixed operating costs are CU 500 million, producing CU 100 million EBIT.

### scenario

- 观察日期 / Observed: 2025-11-01
- 来源 / Source: Synthetic scenario definition

The scenario is a 5% revenue decline with constant unit pricing and mix.

### cost-behaviour

- 观察日期 / Observed: 2025-11-01
- 来源 / Source: Synthetic cost behaviour assumption

Variable costs move proportionally with revenue; fixed costs do not change during the horizon.

### below-ebit

- 观察日期 / Observed: 2025-11-01
- 来源 / Source: Synthetic EPS bridge assumptions

Interest expense, tax rate, and diluted share count remain unchanged in the scenario.

### calculation

- 观察日期 / Observed: 2025-11-01
- 来源 / Source: Synthetic verifier calculation

A 5% revenue decline reduces revenue by CU 50 million and variable cost by CU 20 million, so EBIT falls CU 30 million or 30%.

### uniform

- 观察日期 / Observed: 2025-10-15
- 来源 / Source: Synthetic internal newsletter

Employees received new uniforms during the quarter.

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Prediction: **high**
- 前提判断 / Premise: **invalid**
- 决定性资料 / Decisive evidence: `base-income`, `scenario`, `cost-behaviour`, `below-ebit`, `calculation`

### 判定要点 / Decisive points

- Rejects a one-for-one revenue-to-EPS assumption.
- Uses variable-cost savings to derive the EBIT change.
- Recognises the 30% EBIT decline from a 5% revenue decline.
- Uses unchanged below-EBIT items and shares to infer an EPS decline above 15%.

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: synthetic
- **legacy_title**: Revenue decline versus EPS decline under operating leverage
- **legacy_category**: earnings-sensitivity

</details>

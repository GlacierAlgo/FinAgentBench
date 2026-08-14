# deferred-revenue-cash-receipts

## Question

A colleague says: 'Deferred revenue grew 40%, so customer cash receipts must grow by at least 20% next year.' Assess the premise and predict the likelihood that customer cash receipts grow by at least 20% during the horizon.

### 任务边界 / Task boundary

- 信息截止 / As of: 2025-02-15
- 预测区间 / Horizon: next 12 months
- 会计辖区 / Jurisdiction: US GAAP

### 已知资料 / Evidence

### accounting-policy

- 观察日期 / Observed: 2025-02-10
- 来源 / Source: Synthetic FY2024 revenue policy

The company bills most three-year subscriptions upfront; cash received before service is recorded as deferred revenue and recognised over the contract term.

### acquisition-effect

- 观察日期 / Observed: 2025-02-10
- 来源 / Source: Synthetic acquisition note

Thirty-one percentage points of deferred-revenue growth came from acquiring a company whose customers had already paid before closing.

### bookings

- 观察日期 / Observed: 2025-02-10
- 来源 / Source: Synthetic operating metrics

Organic annual contract value bookings grew 3% in FY2024.

### renewals

- 观察日期 / Observed: 2025-02-10
- 来源 / Source: Synthetic contract schedule

Contracts representing 46% of the opening subscription base are not scheduled for renewal during the next 12 months.

### churn

- 观察日期 / Observed: 2025-02-10
- 来源 / Source: Synthetic KPI disclosure

Gross revenue retention fell from 94% to 88% over the last two quarters.

### office

- 观察日期 / Observed: 2025-02-12
- 来源 / Source: Synthetic corporate announcement

The company renewed its headquarters lease for five years.

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Prediction: **low**
- 前提判断 / Premise: **invalid**
- 决定性资料 / Decisive evidence: `accounting-policy`, `acquisition-effect`, `bookings`, `renewals`, `churn`

### 判定要点 / Decisive points

- Separates the deferred-revenue balance from future cash receipts.
- Recognises acquired deferred revenue as already collected cash.
- Uses bookings, renewal timing, and retention as forward indicators.
- Makes a directional prediction without claiming zero receipts growth.

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: synthetic
- **legacy_title**: Deferred revenue growth versus future cash receipts
- **legacy_category**: cash-flow-quality

</details>

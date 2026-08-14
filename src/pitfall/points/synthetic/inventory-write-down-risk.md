# inventory-write-down-risk

## Question

A colleague says: 'Inventory rose 55%, proving demand is strong.' Assess the premise and predict the risk of a material inventory-related gross-margin charge or discounting during the horizon.

### 任务边界 / Task boundary

- 信息截止 / As of: 2025-04-30
- 预测区间 / Horizon: next two quarters
- 会计辖区 / Jurisdiction: US GAAP

### 已知资料 / Evidence

### inventory-growth

- 观察日期 / Observed: 2025-04-25
- 来源 / Source: Synthetic Q1 filing

Finished-goods inventory increased 55% year over year while unit shipments declined 8%.

### inventory-days

- 观察日期 / Observed: 2025-04-25
- 来源 / Source: Synthetic Q1 filing

Inventory days increased from 70 to 128 days.

### product-age

- 观察日期 / Observed: 2025-04-25
- 来源 / Source: Synthetic inventory note

Products older than nine months rose from 7% to 22% of finished goods.

### pricing

- 观察日期 / Observed: 2025-04-28
- 来源 / Source: Synthetic PIT channel survey

Channel partners began offering 15% rebates on the prior product generation.

### orders

- 观察日期 / Observed: 2025-04-25
- 来源 / Source: Synthetic operating disclosure

Firm backlog covers 34% of the finished-goods balance, down from 81% a year earlier.

### power-contract

- 观察日期 / Observed: 2025-04-20
- 来源 / Source: Synthetic sustainability release

The main factory signed a three-year renewable electricity contract.

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Prediction: **high**
- 前提判断 / Premise: **invalid**
- 决定性资料 / Decisive evidence: `inventory-growth`, `inventory-days`, `product-age`, `pricing`, `orders`

### 判定要点 / Decisive points

- Rejects inventory growth as standalone proof of demand.
- Connects shipments, days, age, and backlog to weak sell-through.
- Links rebates and ageing to gross-margin pressure.
- Predicts high charge or discounting risk without inventing a write-down amount.

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: synthetic
- **legacy_title**: Inventory growth as demand signal or margin risk
- **legacy_category**: working-capital-and-margins

</details>

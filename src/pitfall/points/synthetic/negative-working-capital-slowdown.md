# negative-working-capital-slowdown

## Question

A colleague says: 'Negative working capital is always a source of cash, so a revenue slowdown will improve liquidity.' Assess the premise and predict the risk of a material working-capital cash outflow during the horizon.

### 任务边界 / Task boundary

- 信息截止 / As of: 2025-07-15
- 预测区间 / Horizon: next two quarters
- 会计辖区 / Jurisdiction: Generic cash-flow analysis

### 已知资料 / Evidence

### customer-terms

- 观察日期 / Observed: 2025-07-10
- 来源 / Source: Synthetic working-capital note

Customers pay an average of 35 days before delivery, creating contract liabilities during growth.

### supplier-terms

- 观察日期 / Observed: 2025-07-10
- 来源 / Source: Synthetic working-capital note

Suppliers are paid 55 days after goods are received.

### revenue-outlook

- 观察日期 / Observed: 2025-07-10
- 来源 / Source: Synthetic order schedule

Confirmed orders imply a 20% sequential revenue decline in each of the next two quarters.

### unwind-model

- 观察日期 / Observed: 2025-07-10
- 来源 / Source: Synthetic treasury stress test

At the confirmed order level, customer prepayments fall CU 90 million before supplier payables decline, producing a projected CU 70 million cash outflow.

### cash

- 观察日期 / Observed: 2025-07-10
- 来源 / Source: Synthetic liquidity report

Unrestricted cash is CU 110 million and minimum operating cash is CU 60 million.

### warehouse

- 观察日期 / Observed: 2025-07-01
- 来源 / Source: Synthetic press release

The company opened a new warehouse in a neighbouring region.

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Prediction: **high**
- 前提判断 / Premise: **invalid**
- 决定性资料 / Decisive evidence: `customer-terms`, `supplier-terms`, `revenue-outlook`, `unwind-model`, `cash`

### 判定要点 / Decisive points

- Rejects the idea that negative working capital always generates cash.
- Explains how fewer prepayments precede payable relief during slowdown.
- Uses the treasury stress test and revenue path.
- Relates the projected outflow to available cash.

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: synthetic
- **legacy_title**: Negative working capital during a growth reversal
- **legacy_category**: liquidity

</details>

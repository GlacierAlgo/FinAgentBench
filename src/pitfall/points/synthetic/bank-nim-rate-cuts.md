# bank-nim-rate-cuts

## Question

A colleague says: 'Policy-rate cuts automatically reduce every bank's net interest margin.' Assess the premise and predict this bank's risk that NIM contracts by more than 20 basis points during the horizon.

### 任务边界 / Task boundary

- 信息截止 / As of: 2025-06-30
- 预测区间 / Horizon: next two quarters
- 会计辖区 / Jurisdiction: Generic bank disclosure

### 已知资料 / Evidence

### asset-repricing

- 观察日期 / Observed: 2025-06-25
- 来源 / Source: Synthetic asset-liability report

Sixty-five percent of earning assets reprice within three months of the policy rate.

### deposit-floor

- 观察日期 / Observed: 2025-06-25
- 来源 / Source: Synthetic deposit note

Forty-five percent of deposits are already non-interest-bearing and another 30% currently pays less than 25 basis points.

### deposit-beta

- 观察日期 / Observed: 2025-06-25
- 来源 / Source: Synthetic ALCO sensitivity

Management estimates only 20% downside deposit beta for the first 100 basis points of cuts because many deposit rates are near their floors.

### hedges

- 观察日期 / Observed: 2025-06-25
- 来源 / Source: Synthetic hedge note

Receive-fixed swaps cover 8% of earning assets and are estimated to offset 4 basis points of NIM compression in the rate scenario.

### rate-path

- 观察日期 / Observed: 2025-06-30
- 来源 / Source: Synthetic PIT market snapshot

The forward curve prices 75 basis points of policy-rate cuts over the next two quarters.

### nim-sensitivity

- 观察日期 / Observed: 2025-06-25
- 来源 / Source: Synthetic ALCO sensitivity

ALCO estimates that the 75 basis point cut path would reduce NIM by 27 basis points after the swap offset, with the current balance sheet held constant.

### branches

- 观察日期 / Observed: 2025-06-18
- 来源 / Source: Synthetic investor presentation

The bank plans to refurbish twelve branches this year.

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Prediction: **high**
- 前提判断 / Premise: **invalid**
- 决定性资料 / Decisive evidence: `asset-repricing`, `deposit-floor`, `deposit-beta`, `hedges`, `rate-path`, `nim-sensitivity`

### 判定要点 / Decisive points

- Explains that NIM response depends on repricing gaps and betas.
- Identifies faster asset repricing than deposit repricing.
- Accounts for deposit floors and limited hedge offset.
- Predicts high contraction risk for this bank rather than all banks.

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: synthetic
- **legacy_title**: Policy-rate cuts and bank net interest margin
- **legacy_category**: banking

</details>

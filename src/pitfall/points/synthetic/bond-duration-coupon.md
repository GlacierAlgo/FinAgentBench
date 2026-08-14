# bond-duration-coupon

## Question

A colleague says: 'A 10% coupon makes a bond safe from interest-rate losses.' Assess the premise and predict the risk that Bond H loses more than 6% of market value under the stated shock.

### 任务边界 / Task boundary

- 信息截止 / As of: 2025-05-01
- 预测区间 / Horizon: immediate parallel 100 bp yield shock
- 会计辖区 / Jurisdiction: Market-value analysis

### 已知资料 / Evidence

### bond-h

- 观察日期 / Observed: 2025-05-01
- 来源 / Source: Synthetic bond analytics snapshot

Bond H has a 10% coupon, 18 years to maturity, a 4.0% yield, modified duration of 8.1, and positive convexity of 92.

### shock

- 观察日期 / Observed: 2025-05-01
- 来源 / Source: Synthetic scenario definition

The scenario is an immediate parallel 100 basis point increase in yield with no credit-spread change.

### duration-rule

- 观察日期 / Observed: 2025-05-01
- 来源 / Source: Case-supplied valuation rule

For a small yield change, approximate percentage price change is negative modified duration times the yield change, with a convexity adjustment.

### convexity

- 观察日期 / Observed: 2025-05-01
- 来源 / Source: Synthetic verifier calculation

Using the supplied duration and convexity, the second-order approximation is about -7.64%.

### spread-constant

- 观察日期 / Observed: 2025-05-01
- 来源 / Source: Synthetic scenario definition

The scenario holds Bond H's credit spread constant, isolating the Treasury-yield effect.

### credit-rating

- 观察日期 / Observed: 2025-05-01
- 来源 / Source: Synthetic security terms

Bond H is rated investment grade.

### issuer-logo

- 观察日期 / Observed: 2025-04-10
- 来源 / Source: Synthetic press release

The issuer introduced a new corporate logo last quarter.

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Prediction: **high**
- 前提判断 / Premise: **invalid**
- 决定性资料 / Decisive evidence: `bond-h`, `shock`, `duration-rule`, `convexity`, `spread-constant`

### 判定要点 / Decisive points

- Rejects coupon size as sufficient protection from rate risk.
- Uses modified duration as the primary sensitivity measure.
- Applies the defined 100 bp shock and convexity adjustment.
- Does not rely on credit rating when spread is held constant.

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: synthetic
- **legacy_title**: Coupon size versus interest-rate sensitivity
- **legacy_category**: fixed-income

</details>

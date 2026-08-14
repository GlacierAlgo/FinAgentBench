# covenant-adjusted-ebitda

## Question

A colleague says: 'Adjusted EBITDA grew 20%, so the leverage covenant is safe.' Assess the premise and predict the risk of a covenant breach at the next test.

### 任务边界 / Task boundary

- 信息截止 / As of: 2025-09-30
- 预测区间 / Horizon: next covenant test in 30 days
- 会计辖区 / Jurisdiction: Contract-defined credit analysis

### 已知资料 / Evidence

### management-ebitda

- 观察日期 / Observed: 2025-09-25
- 来源 / Source: Synthetic investor presentation

Management reports trailing adjusted EBITDA of CU 120 million after CU 40 million of projected synergies and restructuring add-backs.

### covenant-definition

- 观察日期 / Observed: 2025-09-25
- 来源 / Source: Synthetic credit agreement calculation

The credit agreement permits no projected synergies and caps restructuring add-backs at CU 5 million; covenant EBITDA is CU 80 million.

### debt

- 观察日期 / Observed: 2025-09-30
- 来源 / Source: Synthetic lender certificate

Covenant net debt is CU 400 million at the as-of date.

### threshold

- 观察日期 / Observed: 2025-09-25
- 来源 / Source: Synthetic credit agreement

The maximum net-debt-to-covenant-EBITDA ratio is 4.5x.

### cure

- 观察日期 / Observed: 2025-09-25
- 来源 / Source: Synthetic treasury note

No equity cure has been committed and the company has 30 days after testing to deliver the certificate.

### award

- 观察日期 / Observed: 2025-09-20
- 来源 / Source: Synthetic press release

The company received an industry safety award.

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Prediction: **high**
- 前提判断 / Premise: **invalid**
- 决定性资料 / Decisive evidence: `management-ebitda`, `covenant-definition`, `debt`, `threshold`, `cure`

### 判定要点 / Decisive points

- Uses lender-defined rather than management-adjusted EBITDA.
- Calculates 400/80 = 5.0x versus the 4.5x maximum.
- Rejects headline adjusted growth as proof of compliance.
- Notes the absence of a committed cure while avoiding certainty.

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: synthetic
- **legacy_title**: Management-adjusted EBITDA versus covenant EBITDA
- **legacy_category**: credit-and-covenants

</details>

# cn-a-2025-financial-star-st-regime-688004

## Question

你处在2025-04-18收盘后的信息环境。博汇科技已披露2024年年度报告，as-of时证券简称尚未冠以*ST。请只使用下方冻结资料，识别2024年年报首年适用的科创板财务类退市风险警示规则，正确使用利润三项孰低与扣除后营业收入，并预测公司是否会在2025-08-22前因该年度报告的财务类指标首次被实施*ST。不要把亏损、ST与*ST混同，也不要套用主板或其他年份的阈值。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 博汇科技 (688004, SSE STAR)
- 信息截止 / As of: 2025-04-18
- 预测窗口结束 / Window end: 2025-08-22
- 目标事件 / Target: `new_star_st_from_latest_annual_financial_trigger`
- 判定定义 / Definition: 公司在as-of时尚未被实施退市风险警示，并因截至as-of已披露的最近一个年度报告触及当时适用的财务类退市风险警示指标，于预测窗口内首次被交易所实施退市风险警示（证券简称冠以“*ST”）。其他风险警示“ST”、窗口前已存在的*ST及其他原因导致的证券简称变化均不计入

#### 判定条件 / Criteria

- `new_annual_financial_star_st_effective_count >= 1` — 预测窗口内因最近年度报告财务类指标首次生效的*ST退市风险警示次数至少为1

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 上交所科创板2024年4月上市规则及衔接安排：2024年报首用1亿元组合指标

- Evidence ID: `sse-star-2024-financial-rule`
- 发布日期 / Published: 2024-04-30
- 来源 / Source: 上海证券交易所
- URL: https://www.sse.com.cn/lawandrules/sselawsrules/repeal/rules/c/c_20240430_10777832.shtml

上证发〔2024〕52号通知明确，科创板新《上市规则》第12.4.2条第一款第（一）项以上市公司2024年年报为首个适用年度报告。科创板第12.4.2条第（一）项规定：最近一个会计年度经审计的利润总额、净利润或者扣除非经常性损益后的净利润孰低者为负值且营业收入低于1亿元，交易所对股票实施退市风险警示。科创板规则还要求营业收入扣除与主营业务无关和不具备商业实质的收入。该1亿元阈值不同于同期主板3亿元阈值。

### 博汇科技2024年年度报告：利润为负但扣除后营业收入1.7283亿元

- Evidence ID: `688004-fy2024-financials`
- 发布日期 / Published: 2025-04-18
- 来源 / Source: 上海证券交易所科创板法定披露
- URL: https://star.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-18/688004_20250418_2ACO.pdf

公司2024年营业收入17,282.72万元，扣除与主营业务无关的业务收入和不具备商业实质的收入后的营业收入同为17,282.72万元，即172,827,200元。归属于上市公司股东的净利润为-3,847.25万元，扣除非经常性损益后的净利润为-4,197.11万元。立信会计师事务所对年度财务报表出具标准无保留意见。公司2024年末归属于上市公司股东的净资产为61,531.82万元。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `new_star_st_from_latest_annual_financial_trigger`
- 结果日期 / Resolved at: 2025-08-22
- 可观察日期 / Observed at: 2025-08-22

### 实际结果 / Realized outcome

- **observations**:
  - **new_annual_financial_star_st_effective_count**: 0
  - **fy2024_post_deduction_revenue**: 172827200
  - **fy2024_parent_net_profit**: -38472500
  - **applicable_revenue_threshold**: 100000000
- **derivations**:


### 对应的题内资料 / Expected evidence

- `sse-star-2024-financial-rule`
- `688004-fy2024-financials`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_rule_regime_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 688004.XSHG
  - **ticker**: 688004
  - **name_as_of**: 博汇科技
  - **exchange**: SSE STAR
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2025-04-18
  - **allowed_domains**:
    - sse.com.cn
- **scenario_authoring**:
  - **dataset**: official_exchange_and_issuer_filings
  - **access**: read_only
  - **matching_group**: annual-financial-star-st-board-regime-v1
  - **matching_role**: no_event
  - **matching_axes**:
    - same_fiscal_year
    - same_profit_sign
    - post_deduction_revenue_between_100m_and_300m
    - different_board_rule
  - **rule_snapshot_id**: sse-star-2024-04-30-12.4.2
  - **exact_contract**: new_star_st_from_latest_annual_financial_trigger-v1
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **688004_20250418_2ACO.pdf**: 58c9fa87ec549227d8106f24c50747073d6af4380f3885a0b18a512499377dc1
    - **sse_star_2024_rule.docx**: f02e8423e467102e30b419f4e01a42600fa315557eca0ac059740114fe849f15
  - **leakage_guard**: Corpus contains only the applicable rule and annual-report facts published by as_of; the later unchanged security status remains label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_interim_report
    - **title**: 博汇科技2025年半年度报告：证券简称仍为博汇科技
    - **published_at**: 2025-08-22
    - **url**: https://star.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-08-22/688004_20250822_0SSE.pdf
    - **fields**:
      - 公司简称
      - 股票代码
      - 半年度报告披露时证券状态

</details>

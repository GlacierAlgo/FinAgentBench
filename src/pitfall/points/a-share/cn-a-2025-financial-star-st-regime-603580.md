# cn-a-2025-financial-star-st-regime-603580

## Question

你处在2025-04-29收盘后的信息环境。艾艾精工已披露2024年年度报告，as-of时证券简称尚未冠以*ST。请只使用下方冻结资料，识别2024年年报首年适用的上交所主板财务类退市风险警示规则，正确使用利润三项孰低与扣除后营业收入，并预测公司是否会在2025-08-22前因该年度报告的财务类指标首次被实施*ST。不要把亏损、ST与*ST混同，也不要套用其他板块或其他年份的阈值。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 艾艾精工 (603580, SSE)
- 信息截止 / As of: 2025-04-29
- 预测窗口结束 / Window end: 2025-08-22
- 目标事件 / Target: `new_star_st_from_latest_annual_financial_trigger`
- 判定定义 / Definition: 公司在as-of时尚未被实施退市风险警示，并因截至as-of已披露的最近一个年度报告触及当时适用的财务类退市风险警示指标，于预测窗口内首次被交易所实施退市风险警示（证券简称冠以“*ST”）。其他风险警示“ST”、窗口前已存在的*ST及其他原因导致的证券简称变化均不计入

#### 判定条件 / Criteria

- `new_annual_financial_star_st_effective_count >= 1` — 预测窗口内因最近年度报告财务类指标首次生效的*ST退市风险警示次数至少为1

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 上交所主板2024年4月上市规则及衔接安排：2024年报首用3亿元组合指标

- Evidence ID: `sse-main-2024-financial-rule`
- 发布日期 / Published: 2024-04-30
- 来源 / Source: 上海证券交易所
- URL: https://www.sse.com.cn/lawandrules/sselawsrules/repeal/rules/c/c_20240430_10777828.shtml

上证发〔2024〕51号通知明确，新《上市规则》第9.3.2条第一款第（一）项以上市公司2024年年报为首个适用年度报告。主板第9.3.2条第（一）项规定：最近一个会计年度经审计的利润总额、净利润或者扣除非经常性损益后的净利润孰低者为负值，且营业收入低于3亿元，交易所对股票实施退市风险警示。第9.3.3条要求营业收入扣除与主营业务无关的业务收入和不具备商业实质的收入。该规则是主板口径，不应与科创板1亿元阈值混用。

### 艾艾精工2024年年度报告：利润为负且扣除后营业收入1.6588亿元

- Evidence ID: `603580-fy2024-financials`
- 发布日期 / Published: 2025-04-29
- 来源 / Source: 上海证券交易所法定披露
- URL: https://www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-04-29/603580_20250429_EQO1.pdf

公司2024年营业收入167,532,546.07元，扣除与主营业务无关的业务收入和不具备商业实质的收入后的营业收入165,882,917.06元。归属于上市公司股东的净利润为-8,846,090.64元，归属于上市公司股东的扣除非经常性损益后的净利润为-3,988,338.45元。容诚会计师事务所对年度财务报表出具标准无保留意见。判断组合指标时应比较利润三项孰低并使用扣除后营业收入。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `new_star_st_from_latest_annual_financial_trigger`
- 结果日期 / Resolved at: 2025-04-30
- 可观察日期 / Observed at: 2025-04-30

### 实际结果 / Realized outcome

- **observations**:
  - **new_annual_financial_star_st_effective_count**: 1
  - **fy2024_post_deduction_revenue**: 165882917.06
  - **fy2024_parent_net_profit**: -8846090.64
  - **applicable_revenue_threshold**: 300000000
- **derivations**:


### 对应的题内资料 / Expected evidence

- `sse-main-2024-financial-rule`
- `603580-fy2024-financials`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_rule_regime_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 603580.XSHG
  - **ticker**: 603580
  - **name_as_of**: 艾艾精工
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2025-04-29
  - **allowed_domains**:
    - sse.com.cn
- **scenario_authoring**:
  - **dataset**: official_exchange_and_issuer_filings
  - **access**: read_only
  - **matching_group**: annual-financial-star-st-board-regime-v1
  - **matching_role**: event
  - **matching_axes**:
    - same_fiscal_year
    - same_profit_sign
    - post_deduction_revenue_between_100m_and_300m
    - different_board_rule
  - **rule_snapshot_id**: sse-main-2024-04-30-9.3.2
  - **exact_contract**: new_star_st_from_latest_annual_financial_trigger-v1
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **603580_20250429_EQO1.pdf**: 7bfca44833d7e6061224bea33718fcefd9a2cea86632936e5c4d58da0ff679d0
    - **sse_main_2024_rule.docx**: 258f8d39ef06ff4c0881a071cb7b36458116f40329fd2d9e42776553868926d7
  - **leakage_guard**: Corpus contains only the applicable rule and annual-report facts published by as_of; the later effective *ST status remains label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_risk_warning_notice
    - **title**: 艾艾精工关于实施退市风险警示暨停牌的公告
    - **published_at**: 2025-04-29
    - **url**: https://static.cninfo.com.cn/finalpage/2025-04-29/1223390971.PDF
    - **effective_at**: 2025-04-30
    - **fields**:
      - 第9.3.2条第一款第（一）项
      - *ST艾艾
      - 实施退市风险警示起始日

</details>

# cn-a-2017-full-risk-warning-removal-24m-002306

## Question

你处在2017-04-27收盘后的信息环境。中科云网因2016年经审计归母净资产为负而再次被实施*ST。请使用冻结材料，预测未来24个月内能否达到target定义的完整摘帽。分别评估团膳主营的收入和盈利容量、负净资产缺口、现金资源、扣非经营质量和持续经营不确定性，并区分一次性收益使退市指标改善与公司消除全部其他风险警示的更高门槛。不要把未来控制权变化当成已知，也不要把*ST降为ST或提交申请当作完整摘帽。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST云网 (002306, SZSE)
- 信息截止 / As of: 2017-04-27
- 预测窗口结束 / Window end: 2019-04-27
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 判定定义 / Definition: 自2017-04-27再次实施*ST起的24个自然月内，深圳证券交易所审核同意撤销公司股票交易的全部退市风险警示和全部其他风险警示，且完整撤销实际生效、证券简称不再含ST或*ST。公司提出申请、财务指标暂时转正、只撤销退市风险警示但继续实施其他风险警示、*ST降为ST或窗口外完整摘帽均不计

#### 判定条件 / Criteria

- `full_risk_warning_removal_count_24m >= 1` — 窗口内交易所批准并实际生效的完整撤销全部风险警示至少一次

<details>
<summary>冻结资料 / Frozen evidence (1)</summary>

### 中科云网2016年年报：归母净资产再度为负，收入收缩至约1亿元

- Evidence ID: `annual-2016-negative-equity-and-contracted-business`
- 发布日期 / Published: 2017-04-26
- 来源 / Source: 巨潮资讯法定年度报告
- URL: https://static.cninfo.com.cn/finalpage/2017-04-26/1203386420.PDF

2016年公司营业收入约100,286,000元、归母净利润约-54,078,000元，年末归母净资产约-32,094,700元、货币资金20,389,992.58元。上一年通过资产出售等措施实现摘帽后，仅保留的团膳业务规模明显收缩，亏损迅速侵蚀本来很薄的净资产。负净资产直接触发再次实施退市风险警示，也意味着未来完整摘帽不仅要跨回财务门槛，还需消除可能继续存在的其他风险警示依据。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 结果日期 / Resolved at: 2019-04-27
- 可观察日期 / Observed at: 2019-04-29

### 实际结果 / Realized outcome

- **observations**:
  - **full_risk_warning_removal_count_24m**: 0
  - **full_risk_warning_removed_by_window_end**: 0
  - **risk_warning_present_at_window_end**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `annual-2016-negative-equity-and-contracted-business`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_remediation_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002306.XSHE
  - **ticker**: 002306
  - **name_as_of**: *ST云网
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2017-04-27
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - symbol_change
    - is_st
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=002306.XSHE; if_adjusted=0; 2016q4 official and PIT values available by as_of; full versus partial warning-removal states checked through 2019-04-27
  - **matching_group**: risk-warning-day-full-removal-24m-v1
  - **matching_role**: no_event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2016_annual_report**: 8422b60c4f52618da17fdea3859659424528a105f04d2469f8c0da0f1aea6ef1
    - **2019_partial_removal_notice**: c4ab766063a373f2a8b8814ea9fbdb938c5a07d4780580f7c2111bd19cc96f9a
  - **outcome_contract**: Only exchange-approved removal of every ST/*ST warning that becomes effective by 2019-04-27 counts; an application, partial removal, *ST-to-ST downgrade or later full removal does not.
  - **leakage_guard**: The subsequent controller change, 2018 results, 2019 partial removal and 2021 full removal remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: rqdata_risk_warning_status_crosscheck
    - **paths**:
      - data/db/symbol_change.parquet
      - data/db/is_st.parquet
    - **source**: aliyun:/dev/data1/download_rqdata
    - **access**: read_only
    - **window**: 2017-04-27/2019-04-27
    - **earliest_sufficient_observation_date**: 2019-04-29
    - **full_removal_within_window**: false

</details>

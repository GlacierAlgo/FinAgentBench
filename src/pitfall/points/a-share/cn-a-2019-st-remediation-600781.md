# cn-a-2019-st-remediation-600781

## Question

你处在2019-09-03收盘后的信息环境。ST辅仁因16.35625亿元控股股东占用和违规担保戴帽，此前公司在合并报表显示大量现金和利润时却无法支付约6,274万元分红，半年报现金又骤降91.88%。请使用下方冻结资料，预测未来24个自然月内是否会发生target定义的完整撤销全部风险警示。必须区分合并利润、母公司可支配现金、关联应收可回收性、控制人股权全冻结、债务逾期、调查和审计风险；未来若仅从*ST降为ST仍不算完整摘帽。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST辅仁 (600781, SSE)
- 信息截止 / As of: 2019-09-03
- 预测窗口结束 / Window end: 2021-09-03
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来24个自然月内，证券交易所审核同意撤销公司股票交易的全部退市风险警示和全部其他风险警示，且生效后的证券简称不再含ST或*ST、股票退出风险警示板。仅提交或获董事会通过申请、占款或担保已清偿、审计意见改善、撤销一项叠加警示但仍保留任一风险警示、*ST降为ST、暂停上市后恢复或最终退市均不计为事件

#### 判定条件 / Criteria

- `full_risk_warning_removal_count_24m >= 1` — 窗口内经交易所审核同意并生效的完整撤销全部风险警示至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 辅仁药业实施其他风险警示公告：16.35625亿元占用、违规担保与控股股东全冻结

- Evidence ID: `st-notice-occupation-guarantee-and-freeze`
- 发布日期 / Published: 2019-08-31
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2019-08-31/1206870184.PDF

公司自2019年9月3日起变更为ST辅仁。公告称向控股股东及关联方提供借款余额16.35625亿元，未经批准提供连带责任担保1.4亿元、剩余担保6,202万元，预计一个月内无法解决。控股股东持有的45.03%上市公司股份已100%冻结并多次轮候冻结；公司存在债务逾期、流动性不足、产能和销售受影响、证监会调查，以及2018年度现金分红仍未实施。

### 辅仁药业2019年半年报：利润仍正但现金骤降91.88%、其他应收款暴增

- Evidence ID: `h1-cash-collapse-and-related-receivables`
- 发布日期 / Published: 2019-08-31
- 来源 / Source: 巨潮资讯法定半年度报告
- URL: https://static.cninfo.com.cn/finalpage/2019-08-31/1206870186.PDF

2019年上半年营业收入27.6896亿元、归母净利润3.9900亿元、扣非归母净利润3.6213亿元、经营活动现金流净额2.5226亿元；但期末货币资金仅1.3445亿元，较年初16.5636亿元下降91.88%，其中1.2771亿元受限。其他应收款从1,742.68万元增至18.3482亿元，主要系关联方借款；短期借款23.8741亿元。母公司货币资金仅35.57万元。账面利润并未形成可支配清偿能力。

### 戴帽前调查报道：18亿元一季报现金却拿不出6,000万元分红

- Evidence ID: `pre-st-dividend-failure-investigation`
- 发布日期 / Published: 2019-08-06
- 来源 / Source: 中国证券报·中证网转载每日经济新闻
- URL: https://www.cs.com.cn/ssgs/gsxw/201908/t20190806_5975027.html

报道指出公司一季报显示约18.16亿元货币资金，却在7月无法按期实施约6,000万元现金分红，随后暴露资金受限、债务和控制人体系问题。该极端现金可得性矛盾在正式戴帽前已经公开，是判断关联应收可回收、母公司支付能力和治理可信度的重要先验，而不是需要未来信息才能发现的线索。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 结果日期 / Resolved at: 2021-09-03

### 实际结果 / Realized outcome

- **observations**:
  - **full_risk_warning_removal_count_24m**: 0
  - **full_risk_warning_removed_by_window_end**: 0
  - **partial_only_removal_count_24m**: 1
  - **calendar_days_to_full_removal_or_zero**: 0
  - **risk_warning_present_at_window_end**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-occupation-guarantee-and-freeze`
- `h1-cash-collapse-and-related-receivables`
- `pre-st-dividend-failure-investigation`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_remediation_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600781.XSHG
  - **ticker**: 600781
  - **name_as_of**: ST辅仁
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-09-03
  - **allowed_domains**:
    - cninfo.com.cn
    - cs.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - is_st
    - special_treatment_info
  - **row_policy**: stock_code=600781.XSHG; quarter=2019q2; info_date=2019-08-31; if_adjusted=0; first risk-warning trading day=2019-09-03
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation+illegal_guarantees+liquidity_crisis
  - **matching_group**: first-risk-warning-day-full-removal-24m-v1
  - **matching_role**: no_event_hard_cash_reality
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: ec3e34a584c40558e80f65e6023dd85ad238a1b1cf6163a9dd09dc3e2130fc51
    - **h1_report**: cc631eb09efd9844a615fbc7b2daae85ad238a1b1cf6163a9dd09dc3e2130fc51
  - **status_source_sha256**:
    - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
    - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
  - **outcome_contract**: Only an exchange-approved removal of every ST/*ST warning that becomes effective inside the 24-calendar-month window counts. An application, remediation, *ST-to-ST downgrade, continued ST status, or delisting does not.
  - **news_evidence_policy**: Only documents published no later than as_of enter the frozen corpus. Media reporting is an attributed point-in-time clue, never label authority.
  - **leakage_guard**: All removal approvals, later ST transitions, restructurings, delistings and post_as_of remediation facts remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: rqdata_risk_warning_status_crosscheck
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2019-09-03/2021-09-03
    - **full_removal_within_window**: false
    - **partial_only_removal_count_24m**: 1
    - **later_context_not_counted**: 窗口内公司一度由*ST降为ST但从未退出风险警示板；其后再次被*ST并于2023年退市，完整撤销从未发生。

</details>

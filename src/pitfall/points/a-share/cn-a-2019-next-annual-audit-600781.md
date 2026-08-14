# cn-a-2019-next-annual-audit-600781

## Question

你处在2019-09-03收盘后的信息环境，ST辅仁已经进入风险警示状态。请仅使用下方冻结资料，预测快照后严格首份年度财务报表审计报告是否会在未来18个自然月内构成target定义的非标准审计报告。把资金占用或违规担保规模、清偿与可审计性、报表层重大错报、审计范围受限、持续经营和现金质量分别判断；不要把ST/*ST标签、整改承诺、后来摘帽或退市、股价表现、以及内部控制审计意见直接当成财务报表审计结论。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST辅仁 (600781, SSE)
- 信息截止 / As of: 2019-09-03
- 预测窗口结束 / Window end: 2021-03-03
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 判定定义 / Definition: 在快照日之后严格首次公开披露、且不晚于未来18个自然月窗口结束日的年度财务报表审计报告，是否为非标准审计报告。保留意见、否定意见、无法表示意见，以及带强调事项段、持续经营重大不确定性段或其他信息未更正重大错报说明的无保留意见均计为事件；标准无保留意见不计。只认年度财务报表审计报告，不认内部控制审计报告、监管问询、业绩预告、整改声明或更晚年度报告

#### 判定条件 / Criteria

- `qualifying_nonstandard_first_annual_audit_count_18m >= 1` — 窗口内首份快照后年度财务报表审计报告符合非标准定义

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

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 结果日期 / Resolved at: 2020-06-24

### 实际结果 / Realized outcome

- **observations**:
  - **qualifying_nonstandard_first_annual_audit_count_18m**: 1
  - **first_post_snapshot_annual_audit_report_count_18m**: 1
  - **first_annual_audit_nonstandard**: 1
  - **first_annual_audit_standard_unqualified**: 0
  - **calendar_days_to_first_annual_audit**: 295
  - **internal_control_audit_used_for_label**: 0
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
- **suite**: a_share_next_annual_audit_v1
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
  - **row_policy**: stock_code=600781.XSHG; only point-in-time financial rows and public evidence available no later than 2019-09-03; the first annual financial-statement audit report strictly after the snapshot is resolved inside a fixed 18-calendar-month window
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation+illegal_guarantees+liquidity_crisis
  - **matching_group**: first-post-snapshot-annual-financial-audit-18m-v1
  - **matching_role**: event_nonstandard_audit
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: ec3e34a584c40558e80f65e6023dd85ad238a1b1cf6163a9dd09dc3e2130fc51
    - **h1_report**: cc631eb09efd9844a615fbc7b2daae85ad238a1b1cf6163a9dd09dc3e2130fc51
  - **news_evidence_policy**: Only documents published no later than as_of enter the frozen corpus. Media reporting is an attributed point-in-time clue, never label authority.
  - **outcome_contract**: Use only the first annual financial-statement audit report publicly disclosed strictly after as_of and no later than window_end. Qualified, adverse, disclaimer, or unqualified with an emphasis, going-concern material-uncertainty, or uncorrected-other-information paragraph counts as nonstandard. Internal-control audit opinions never determine this label.
  - **label_authority**: The exact future annual financial-statement audit report is label-side only; annual-report summaries may corroborate but cannot replace the signed audit report.
  - **leakage_guard**: All future audit reports, audit-opinion wording, later remediation, warning-removal, delisting and price outcomes remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_first_post_snapshot_annual_financial_statement_audit_report
    - **title**: 辅仁2019年度财务报表审计报告
    - **fiscal_year**: 2019
    - **published_at**: 2020-06-24
    - **url**: https://static.cninfo.com.cn/finalpage/2020-06-24/1207956931.PDF
    - **sha256**: eb29280370f41a6fed525a1f5921df0e3470abad3580fe4ba0bb61722d20c99d
    - **audit_opinion**: 无法表示意见
    - **qualifies_as_nonstandard**: true
    - **qualification_basis**: 财务报表审计报告为无法表示意见
    - **is_first_annual_financial_statement_audit_after_snapshot**: true
    - **inside_18_calendar_month_window**: true
    - **internal_control_opinion_not_used**: true
    - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
    - **pdf_text_mode**: native PDFium text extraction (--no-ocr)

</details>

# cn-a-2021-next-annual-audit-600300

## Question

你处在2021-04-27收盘后的信息环境，ST维维已经进入风险警示状态。请仅使用下方冻结资料，预测快照后严格首份年度财务报表审计报告是否会在未来18个自然月内构成target定义的非标准审计报告。把资金占用或违规担保规模、清偿与可审计性、报表层重大错报、审计范围受限、持续经营和现金质量分别判断；不要把ST/*ST标签、整改承诺、后来摘帽或退市、股价表现、以及内部控制审计意见直接当成财务报表审计结论。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST维维 (600300, SSE)
- 信息截止 / As of: 2021-04-27
- 预测窗口结束 / Window end: 2022-10-27
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 判定定义 / Definition: 在快照日之后严格首次公开披露、且不晚于未来18个自然月窗口结束日的年度财务报表审计报告，是否为非标准审计报告。保留意见、否定意见、无法表示意见，以及带强调事项段、持续经营重大不确定性段或其他信息未更正重大错报说明的无保留意见均计为事件；标准无保留意见不计。只认年度财务报表审计报告，不认内部控制审计报告、监管问询、业绩预告、整改声明或更晚年度报告

#### 判定条件 / Criteria

- `qualifying_nonstandard_first_annual_audit_count_18m >= 1` — 窗口内首份快照后年度财务报表审计报告符合非标准定义

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 维维股份实施其他风险警示公告：内控重大缺陷仍在，但占用本息已收回

- Evidence ID: `st-notice-remediation-before-first-st-day`
- 发布日期 / Published: 2021-04-26
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/new/2021-04-26/600300_20210426_1.pdf

公司自2021年4月27日起变更为ST维维。戴帽原因是会计师对2020年度内部控制出具否定意见：关联资金拆借未履行董事会、股东大会决策程序，也未及时披露，内部控制未能防止、发现和纠正违规，构成重大缺陷。与多数未解决占用案例不同，公告明确称新一届董事会已在2021年4月21日前解决资金占用和违规担保问题，并收回占用资金本息。这使案例能够检验“整改完成或未来摘帽必然带来大炒”的错误捷径。

### 维维股份2020年年度报告：现金流改善但利润主要来自处置，植物蛋白产能利用不足

- Evidence ID: `annual-core-profit-disposal-gains-and-capacity`
- 发布日期 / Published: 2021-04-24
- 来源 / Source: 上海证券交易所法定年度报告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/new/2021-04-24/600300_20210424_2.pdf

2020年营业收入47.9882亿元，同比下降4.77%；归母净利润4.3573亿元，但扣非归母净利润仅6,111.52万元。年报解释出售枝江酒业形成投资收益约1.32亿元，土地征收形成资产处置收益约2.10亿元，合计对利润贡献很大。经营活动现金流净额8.9638亿元；货币资金22.2749亿元、短期借款24.2661亿元。固体饮料收入17.5119亿元基本持平，植物蛋白饮料收入4.4024亿元下降14.53%。主要豆奶/乳品工厂多处实际产能明显低于设计产能，例如总部豆奶粉设计6万吨、实际2.41万吨。占用期末利息2,692.29万元已于2021年4月21日清偿。

### 戴帽前治理报道：多年虚假货款通道占用与董监高知情风险

- Evidence ID: `contemporaneous-governance-history-and-sanctions`
- 发布日期 / Published: 2021-04-01
- 来源 / Source: 新浪财经转载的资本市场调查报道
- URL: https://finance.sina.com.cn/stock/s/2021-04-01/doc-ikmyaawa3549966.shtml

报道根据监管处罚和交易所纪律处分梳理，2017至2019年维维集团通过虚假支付货款等中间通道持续占用上市公司资金，年度累计占用从约7亿元升至11.54亿元；部分上市公司高管知悉并配合调度，其他董监高签署定期报告但未勤勉尽责。上交所认为“个人所为、董事会不知情”的申辩反而说明内控存在重大缺陷。该历史提高治理风险先验；但在as_of前占用本息已经收回，模型仍需把历史缺陷与当前修复进度分开。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 结果日期 / Resolved at: 2022-03-05

### 实际结果 / Realized outcome

- **observations**:
  - **qualifying_nonstandard_first_annual_audit_count_18m**: 0
  - **first_post_snapshot_annual_audit_report_count_18m**: 1
  - **first_annual_audit_nonstandard**: 0
  - **first_annual_audit_standard_unqualified**: 1
  - **calendar_days_to_first_annual_audit**: 312
  - **internal_control_audit_used_for_label**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-remediation-before-first-st-day`
- `annual-core-profit-disposal-gains-and-capacity`
- `contemporaneous-governance-history-and-sanctions`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_next_annual_audit_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600300.XSHG
  - **ticker**: 600300
  - **name_as_of**: ST维维
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-04-27
  - **allowed_domains**:
    - sse.com.cn
    - sina.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - is_st
    - special_treatment_info
  - **row_policy**: stock_code=600300.XSHG; only point-in-time financial rows and public evidence available no later than 2021-04-27; the first annual financial-statement audit report strictly after the snapshot is resolved inside a fixed 18-calendar-month window
  - **st_cause_taxonomy**: non_operating_governance/remediated_related_party_fund_occupation+adverse_internal_control
  - **matching_group**: first-post-snapshot-annual-financial-audit-18m-v1
  - **matching_role**: no_event_standard_audit_hard_control
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: a7fbfd34ccde4ee257ab4d18ad32c51156db5a4e78dd44b14b43c54f2195c2cb
    - **2020_annual_report**: 7bbd8699a7d194a1cbf150111ad520500a9ab1963de2c04b1720f0281bd019aa
  - **news_evidence_policy**: Contemporaneous reporting may expose governance history; official filings and RQData remain the authority for remediation, financial facts, and the label.
  - **outcome_contract**: Use only the first annual financial-statement audit report publicly disclosed strictly after as_of and no later than window_end. Qualified, adverse, disclaimer, or unqualified with an emphasis, going-concern material-uncertainty, or uncorrected-other-information paragraph counts as nonstandard. Internal-control audit opinions never determine this label.
  - **label_authority**: The exact future annual financial-statement audit report is label-side only; annual-report summaries may corroborate but cannot replace the signed audit report.
  - **leakage_guard**: All future audit reports, audit-opinion wording, later remediation, warning-removal, delisting and price outcomes remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_first_post_snapshot_annual_financial_statement_audit_report
    - **title**: 维维2021年度财务报表审计报告
    - **fiscal_year**: 2021
    - **published_at**: 2022-03-05
    - **url**: https://static.cninfo.com.cn/finalpage/2022-03-05/1212511442.PDF
    - **sha256**: f2a5fc285ff5a008f33f13a70c857482eae8f2352b8c93ac8a2240954368f7e3
    - **audit_opinion**: 标准无保留意见
    - **qualifies_as_nonstandard**: false
    - **qualification_basis**: 财务报表审计报告为标准无保留意见
    - **is_first_annual_financial_statement_audit_after_snapshot**: true
    - **inside_18_calendar_month_window**: true
    - **internal_control_opinion_not_used**: true
    - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
    - **pdf_text_mode**: native PDFium text extraction (--no-ocr)

</details>

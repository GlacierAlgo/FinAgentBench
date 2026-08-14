# cn-a-2019-next-annual-audit-600518

## Question

你处在2019-05-21收盘后的信息环境，ST康美已经进入风险警示状态。请仅使用下方冻结资料，预测快照后严格首份年度财务报表审计报告是否会在未来18个自然月内构成target定义的非标准审计报告。把资金占用或违规担保规模、清偿与可审计性、报表层重大错报、审计范围受限、持续经营和现金质量分别判断；不要把ST/*ST标签、整改承诺、后来摘帽或退市、股价表现、以及内部控制审计意见直接当成财务报表审计结论。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST康美 (600518, SSE)
- 信息截止 / As of: 2019-05-21
- 预测窗口结束 / Window end: 2020-11-21
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 判定定义 / Definition: 在快照日之后严格首次公开披露、且不晚于未来18个自然月窗口结束日的年度财务报表审计报告，是否为非标准审计报告。保留意见、否定意见、无法表示意见，以及带强调事项段、持续经营重大不确定性段或其他信息未更正重大错报说明的无保留意见均计为事件；标准无保留意见不计。只认年度财务报表审计报告，不认内部控制审计报告、监管问询、业绩预告、整改声明或更晚年度报告

#### 判定条件 / Criteria

- `qualifying_nonstandard_first_annual_audit_count_18m >= 1` — 窗口内首份快照后年度财务报表审计报告符合非标准定义

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 康美药业实施其他风险警示公告：88.79亿元关联资金用于购买公司股票

- Evidence ID: `st-notice-8.879b-related-fund-flow`
- 发布日期 / Published: 2019-05-18
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2019-05-18/1206283586.PDF

公司自2019年5月21日起变更为ST康美。公告称公司与关联公司存在88.79亿元资金往来，该资金被关联公司用于购买公司股票，触及投资者难以判断公司前景、权益可能受损的情形。公司承认治理、资金管理和关联交易内控存在重大缺陷，只表示督促关联方多途径解决并整改，没有给出锁定资金、清偿时间表或审计验证。

### 康美药业2019年一季报：更正后现金骤降、巨额存货与短债

- Evidence ID: `q1-cash-collapse-inventory-and-short-debt`
- 发布日期 / Published: 2019-04-30
- 来源 / Source: 巨潮资讯法定季度报告
- URL: https://static.cninfo.com.cn/finalpage/2019-04-30/1206168279.PDF

更正口径下，2019年一季度营业收入49.0164亿元、归母净利润2.2088亿元、扣非归母净利润1.7091亿元、经营活动现金流净额6.7395亿元。期末货币资金10.4801亿元，较年初减少43.02%；存货336.6041亿元、短期借款149.40亿元、流动负债249.7790亿元、总负债452.7493亿元。筹资现金流净额-12.9980亿元。正经营现金流远小于资金占用与融资规模，且报表刚经历巨额差错更正。

### 中证网戴帽报道：88.79亿元资金往来直接触发风险警示

- Evidence ID: `contemporaneous-st-report`
- 发布日期 / Published: 2019-05-18
- 来源 / Source: 中国证券报·中证网
- URL: https://www.cs.com.cn/ssgs/gsxw/201905/t20190518_5950494.html

同时点报道确认公司将于5月21日起被实施其他风险警示，原因是88.79亿元关联资金被用于购买公司股票并使投资者难以判断前景。新闻没有提供已经到账的清偿资源或交易所撤销意见，因此只用于交叉核验市场当时可见的信息，不能支持“很快摘帽”的结论。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 结果日期 / Resolved at: 2020-06-18

### 实际结果 / Realized outcome

- **observations**:
  - **qualifying_nonstandard_first_annual_audit_count_18m**: 1
  - **first_post_snapshot_annual_audit_report_count_18m**: 1
  - **first_annual_audit_nonstandard**: 1
  - **first_annual_audit_standard_unqualified**: 0
  - **calendar_days_to_first_annual_audit**: 394
  - **internal_control_audit_used_for_label**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-8.879b-related-fund-flow`
- `q1-cash-collapse-inventory-and-short-debt`
- `contemporaneous-st-report`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_next_annual_audit_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600518.XSHG
  - **ticker**: 600518
  - **name_as_of**: ST康美
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-05-21
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
  - **row_policy**: stock_code=600518.XSHG; only point-in-time financial rows and public evidence available no later than 2019-05-21; the first annual financial-statement audit report strictly after the snapshot is resolved inside a fixed 18-calendar-month window
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_flow+internal_control_material_weakness
  - **matching_group**: first-post-snapshot-annual-financial-audit-18m-v1
  - **matching_role**: event_nonstandard_audit
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: 0dbe732b03eb90ba8cd5dabc9757b42700f774d2ad6fb9195777119a249f8172
    - **q1_report**: 684b1c371ca5e2f564b638ad5cbdfd9bd72ae0a36cc041d1bac076475612c402
  - **news_evidence_policy**: Only documents published no later than as_of enter the frozen corpus. Media reporting is an attributed point-in-time clue, never label authority.
  - **outcome_contract**: Use only the first annual financial-statement audit report publicly disclosed strictly after as_of and no later than window_end. Qualified, adverse, disclaimer, or unqualified with an emphasis, going-concern material-uncertainty, or uncorrected-other-information paragraph counts as nonstandard. Internal-control audit opinions never determine this label.
  - **label_authority**: The exact future annual financial-statement audit report is label-side only; annual-report summaries may corroborate but cannot replace the signed audit report.
  - **leakage_guard**: All future audit reports, audit-opinion wording, later remediation, warning-removal, delisting and price outcomes remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_first_post_snapshot_annual_financial_statement_audit_report
    - **title**: 康美2019年度财务报表审计报告
    - **fiscal_year**: 2019
    - **published_at**: 2020-06-18
    - **url**: https://static.cninfo.com.cn/finalpage/2020-06-18/1207936074.PDF
    - **sha256**: e8c178ab9b9b24026816d6d96ab2ea3952d9893ff00ee83ee18f26ef59a3127e
    - **audit_opinion**: 带强调事项段的保留意见
    - **qualifies_as_nonstandard**: true
    - **qualification_basis**: 财务报表审计报告为带强调事项段的保留意见
    - **is_first_annual_financial_statement_audit_after_snapshot**: true
    - **inside_18_calendar_month_window**: true
    - **internal_control_opinion_not_used**: true
    - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
    - **pdf_text_mode**: native PDFium text extraction (--no-ocr)

</details>

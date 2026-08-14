# cn-a-2020-next-annual-audit-600080

## Question

你处在2020-06-02收盘后的信息环境，ST金花已经进入风险警示状态。请仅使用下方冻结资料，预测快照后严格首份年度财务报表审计报告是否会在未来18个自然月内构成target定义的非标准审计报告。把资金占用或违规担保规模、清偿与可审计性、报表层重大错报、审计范围受限、持续经营和现金质量分别判断；不要把ST/*ST标签、整改承诺、后来摘帽或退市、股价表现、以及内部控制审计意见直接当成财务报表审计结论。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST金花 (600080, SSE)
- 信息截止 / As of: 2020-06-02
- 预测窗口结束 / Window end: 2021-12-02
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 判定定义 / Definition: 在快照日之后严格首次公开披露、且不晚于未来18个自然月窗口结束日的年度财务报表审计报告，是否为非标准审计报告。保留意见、否定意见、无法表示意见，以及带强调事项段、持续经营重大不确定性段或其他信息未更正重大错报说明的无保留意见均计为事件；标准无保留意见不计。只认年度财务报表审计报告，不认内部控制审计报告、监管问询、业绩预告、整改声明或更晚年度报告

#### 判定条件 / Criteria

- `qualifying_nonstandard_first_annual_audit_count_18m >= 1` — 窗口内首份快照后年度财务报表审计报告符合非标准定义

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 金花股份实施其他风险警示公告：尚有1.6772亿元占用与存单质押未解

- Evidence ID: `st-notice-occupation-and-pledged-deposit`
- 发布日期 / Published: 2020-06-01
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-06-01/1207878970.PDF

公司自2020年6月2日起变更为ST金花。2019年控股股东及关联方资金占用发生额2.7777亿元、存单质押6,800万元，合计3.4577亿元，占最近一期经审计净资产20.15%；截至公告日仍有1.6772亿元未归还或解除，占净资产9.78%。控股股东承诺转让所持股份，并在6月30日前归还资金及占用费，但披露时尚未完成。

### 金花股份2020年一季报：低有息负债与疫情下收入现金流承压

- Evidence ID: `q1-low-leverage-but-pandemic-pressure`
- 发布日期 / Published: 2020-04-30
- 来源 / Source: 巨潮资讯法定季度报告
- URL: https://static.cninfo.com.cn/finalpage/2020-04-30/1207688572.PDF

2020年一季度营业收入1.0778亿元，同比下降28.09%；归母净利润-104.34万元，扣非归母净利润-270.96万元，经营活动现金流净额-1,458.22万元。期末货币资金2.4680亿元、归母净资产17.1412亿元，合并资产负债表没有短期借款，流动负债1.6223亿元。低杠杆和账面现金使问题可能可修复，但占用金额接近现金的68%，且现金是否自由可用需要结合存单质押判断。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 结果日期 / Resolved at: 2021-04-23

### 实际结果 / Realized outcome

- **observations**:
  - **qualifying_nonstandard_first_annual_audit_count_18m**: 0
  - **first_post_snapshot_annual_audit_report_count_18m**: 1
  - **first_annual_audit_nonstandard**: 0
  - **first_annual_audit_standard_unqualified**: 1
  - **calendar_days_to_first_annual_audit**: 325
  - **internal_control_audit_used_for_label**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-occupation-and-pledged-deposit`
- `q1-low-leverage-but-pandemic-pressure`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_next_annual_audit_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600080.XSHG
  - **ticker**: 600080
  - **name_as_of**: ST金花
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-06-02
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - is_st
    - special_treatment_info
  - **row_policy**: stock_code=600080.XSHG; only point-in-time financial rows and public evidence available no later than 2020-06-02; the first annual financial-statement audit report strictly after the snapshot is resolved inside a fixed 18-calendar-month window
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation+pledged_deposit
  - **matching_group**: first-post-snapshot-annual-financial-audit-18m-v1
  - **matching_role**: no_event_standard_audit_hard_control
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: 076582de2b46d70471f15ac8ab1d8cb96fb821375bf3098931bd817208960ba9
    - **q1_report**: 9da6aaa89af6b1b0c42787c6f495116ba4367220f0c7e2ff6d008c33c99bef1f
  - **news_evidence_policy**: Only documents published no later than as_of enter the frozen corpus. Media reporting is an attributed point-in-time clue, never label authority.
  - **outcome_contract**: Use only the first annual financial-statement audit report publicly disclosed strictly after as_of and no later than window_end. Qualified, adverse, disclaimer, or unqualified with an emphasis, going-concern material-uncertainty, or uncorrected-other-information paragraph counts as nonstandard. Internal-control audit opinions never determine this label.
  - **label_authority**: The exact future annual financial-statement audit report is label-side only; annual-report summaries may corroborate but cannot replace the signed audit report.
  - **leakage_guard**: All future audit reports, audit-opinion wording, later remediation, warning-removal, delisting and price outcomes remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_first_post_snapshot_annual_financial_statement_audit_report
    - **title**: 金花2020年度财务报表审计报告
    - **fiscal_year**: 2020
    - **published_at**: 2021-04-23
    - **url**: https://static.cninfo.com.cn/finalpage/2021-04-23/1209776507.PDF
    - **sha256**: 524bd1b8ea54d18bcb727115a000ba043494ce80a99b585e3d3ef4f2c819f0ba
    - **audit_opinion**: 标准无保留意见
    - **qualifies_as_nonstandard**: false
    - **qualification_basis**: 财务报表审计报告为标准无保留意见；内部控制报告意见不用于本标签
    - **is_first_annual_financial_statement_audit_after_snapshot**: true
    - **inside_18_calendar_month_window**: true
    - **internal_control_opinion_not_used**: true
    - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
    - **pdf_text_mode**: native PDFium text extraction (--no-ocr)

</details>

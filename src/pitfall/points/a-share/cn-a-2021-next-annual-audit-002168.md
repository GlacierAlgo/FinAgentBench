# cn-a-2021-next-annual-audit-002168

## Question

你处在2021-03-03收盘后的信息环境，ST惠程已经进入风险警示状态。请仅使用下方冻结资料，预测快照后严格首份年度财务报表审计报告是否会在未来18个自然月内构成target定义的非标准审计报告。把资金占用或违规担保规模、清偿与可审计性、报表层重大错报、审计范围受限、持续经营和现金质量分别判断；不要把ST/*ST标签、整改承诺、后来摘帽或退市、股价表现、以及内部控制审计意见直接当成财务报表审计结论。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST惠程 (002168, SZSE)
- 信息截止 / As of: 2021-03-03
- 预测窗口结束 / Window end: 2022-09-03
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 判定定义 / Definition: 在快照日之后严格首次公开披露、且不晚于未来18个自然月窗口结束日的年度财务报表审计报告，是否为非标准审计报告。保留意见、否定意见、无法表示意见，以及带强调事项段、持续经营重大不确定性段或其他信息未更正重大错报说明的无保留意见均计为事件；标准无保留意见不计。只认年度财务报表审计报告，不认内部控制审计报告、监管问询、业绩预告、整改声明或更晚年度报告

#### 判定条件 / Criteria

- `qualifying_nonstandard_first_annual_audit_count_18m >= 1` — 窗口内首份快照后年度财务报表审计报告符合非标准定义

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 惠程科技实施其他风险警示公告：已还3.10亿元但6,067.49万元余额逾期

- Evidence ID: `st-notice-small-residual-after-large-repayments`
- 发布日期 / Published: 2021-03-02
- 来源 / Source: 深圳证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2021-03-02/1209318659.PDF

公司自2021年3月3日起变更为ST惠程。公告称控股股东中驰惠程及关联方非经营性占用上市公司资金；截至公告日累计已归还31,015.42万元，余额6,067.49万元，但未能在3月2日前完成归还，因而触发其他风险警示。控制人承诺在2020年年报披露前、尽量一个月内以现金、现金等价物或优质资产抵债解决。已归还大部分和明确短期承诺提高可修复性，但公告没有证明剩余款项已进入公司账户。

### 惠程科技2020年三季报：小幅盈利、现金流转正与高商誉并存

- Evidence ID: `q3-positive-cash-flow-but-large-goodwill`
- 发布日期 / Published: 2020-10-30
- 来源 / Source: 巨潮资讯法定季度报告
- URL: https://static.cninfo.com.cn/finalpage/2020-10-30/1208652937.PDF

2020年前三季度营业收入6.7623亿元，归母净利润2,570.66万元，扣非归母净利润2,220.41万元，经营活动现金流净额1.6886亿元。期末货币资金2.6226亿元、短期借款1.57亿元、流动负债6.0970亿元、归母净资产18.3828亿元；商誉12.2060亿元，约为归母净资产的66%。剩余占用款相对账面净资产不大，但上市公司自身资产质量和高商誉意味着不能只看一个清偿比例。

### 戴帽前媒体报道：2月25日再还2.01亿元，剩余6,067.49万元

- Evidence ID: `pre-st-media-repayment-trajectory`
- 发布日期 / Published: 2021-03-01
- 来源 / Source: 中国农业银行报转载的市场观察
- URL: https://paper.people.com.cn/zgnyb/html/2021-03/01/content_2036466.htm

截至戴帽前的公开报道，控股股东在2月25日通过银行转账归还2.01亿元，加上此前1.09亿元，累计归还约3.10亿元，非经营性占用余额为6,067.49万元。该付款轨迹是比口头承诺更强的点时证据，但最后一笔是否按期到账、是否还有其他风险警示原因以及交易所是否批准仍需独立判断。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 结果日期 / Resolved at: 2021-04-30

### 实际结果 / Realized outcome

- **observations**:
  - **qualifying_nonstandard_first_annual_audit_count_18m**: 1
  - **first_post_snapshot_annual_audit_report_count_18m**: 1
  - **first_annual_audit_nonstandard**: 1
  - **first_annual_audit_standard_unqualified**: 0
  - **calendar_days_to_first_annual_audit**: 58
  - **internal_control_audit_used_for_label**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-small-residual-after-large-repayments`
- `q3-positive-cash-flow-but-large-goodwill`
- `pre-st-media-repayment-trajectory`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_next_annual_audit_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002168.XSHE
  - **ticker**: 002168
  - **name_as_of**: ST惠程
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-03-03
  - **allowed_domains**:
    - cninfo.com.cn
    - people.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - is_st
    - special_treatment_info
  - **row_policy**: stock_code=002168.XSHE; only point-in-time financial rows and public evidence available no later than 2021-03-03; the first annual financial-statement audit report strictly after the snapshot is resolved inside a fixed 18-calendar-month window
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation
  - **matching_group**: first-post-snapshot-annual-financial-audit-18m-v1
  - **matching_role**: event_nonstandard_audit
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: dd6b96e80d3d50dcb504b0f7d86897be967d9a2f3c23252c80515f09e0e615fb
    - **q3_report**: be6130f02b33c04743ab48fbd40090fb6f0e40a0a5b49090c51101bbb6dc6c37
  - **news_evidence_policy**: Only documents published no later than as_of enter the frozen corpus. Media reporting is an attributed point-in-time clue, never label authority.
  - **outcome_contract**: Use only the first annual financial-statement audit report publicly disclosed strictly after as_of and no later than window_end. Qualified, adverse, disclaimer, or unqualified with an emphasis, going-concern material-uncertainty, or uncorrected-other-information paragraph counts as nonstandard. Internal-control audit opinions never determine this label.
  - **label_authority**: The exact future annual financial-statement audit report is label-side only; annual-report summaries may corroborate but cannot replace the signed audit report.
  - **leakage_guard**: All future audit reports, audit-opinion wording, later remediation, warning-removal, delisting and price outcomes remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_first_post_snapshot_annual_financial_statement_audit_report
    - **title**: 惠程2020年度财务报表审计报告
    - **fiscal_year**: 2020
    - **published_at**: 2021-04-30
    - **url**: https://static.cninfo.com.cn/finalpage/2021-04-30/1209872163.PDF
    - **sha256**: f645476925c7108ffb9a8d50cefebe1bb800cf6f6b5d947735c6fac676c0d0d1
    - **audit_opinion**: 保留意见
    - **qualifies_as_nonstandard**: true
    - **qualification_basis**: 财务报表审计报告为保留意见
    - **is_first_annual_financial_statement_audit_after_snapshot**: true
    - **inside_18_calendar_month_window**: true
    - **internal_control_opinion_not_used**: true
    - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
    - **pdf_text_mode**: native PDFium text extraction (--no-ocr)

</details>

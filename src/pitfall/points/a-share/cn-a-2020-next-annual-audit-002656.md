# cn-a-2020-next-annual-audit-002656

## Question

你处在2020-01-13收盘后的信息环境，ST摩登已经进入风险警示状态。请仅使用下方冻结资料，预测快照后严格首份年度财务报表审计报告是否会在未来18个自然月内构成target定义的非标准审计报告。把资金占用或违规担保规模、清偿与可审计性、报表层重大错报、审计范围受限、持续经营和现金质量分别判断；不要把ST/*ST标签、整改承诺、后来摘帽或退市、股价表现、以及内部控制审计意见直接当成财务报表审计结论。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST摩登 (002656, SZSE)
- 信息截止 / As of: 2020-01-13
- 预测窗口结束 / Window end: 2021-07-13
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 判定定义 / Definition: 在快照日之后严格首次公开披露、且不晚于未来18个自然月窗口结束日的年度财务报表审计报告，是否为非标准审计报告。保留意见、否定意见、无法表示意见，以及带强调事项段、持续经营重大不确定性段或其他信息未更正重大错报说明的无保留意见均计为事件；标准无保留意见不计。只认年度财务报表审计报告，不认内部控制审计报告、监管问询、业绩预告、整改声明或更晚年度报告

#### 判定条件 / Criteria

- `qualifying_nonstandard_first_annual_audit_count_18m >= 1` — 窗口内首份快照后年度财务报表审计报告符合非标准定义

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 摩登大道实施其他风险警示公告：实控人越权形成3.3亿元未解除担保

- Evidence ID: `st-notice-illegal-guarantees`
- 发布日期 / Published: 2020-01-10
- 来源 / Source: 深圳证券交易所法定公告PDF镜像
- URL: https://pdf.dfcfw.com/pdf/H2_AN202001091373794217_1.PDF

公司自2020年1月13日起变更为ST摩登。公告称控股股东违反规定程序，以公司及子公司名义对外提供担保；截至披露日，未经审议且未及时披露的担保余额3.30亿元，不含利息等费用，占最近年度经审计净资产13.86%。四笔披露担保中仅一笔解除，未解除事项包含为关联方及实控人债务提供担保。董事会只能督促被担保人筹资并通过司法途径解决，责任解除时间和损失金额均不确定。

### 摩登大道2019年三季报：单季亏损、收入下滑与货币资金骤降

- Evidence ID: `q3-operating-decline-cash-and-goodwill`
- 发布日期 / Published: 2019-10-31
- 来源 / Source: 深圳证券交易所法定季度报告PDF镜像
- URL: http://file.finance.sina.com.cn/211.154.219.97:9494/MRGG/CNSESZ_STOCK/2019/2019-10/2019-10-31/5723997.PDF

2019年前三季度营业收入9.6126亿元，同比下降8.25%；归母净利润-2,512.93万元，扣非归母净利润-2,813.47万元；第三季度单季收入下降35.98%、归母净利润-5,638.10万元。经营活动现金流净额1.2291亿元为正，但期末货币资金1.3922亿元，较年初下降54.08%；其他应收款同比大增，主要包括对子公司涉及澳门国际银行款项9,560.96万元。期末商誉4.0907亿元，占归母净资产约17.5%。非经营性违规担保出现时，主营趋势、现金缓冲和资产质量也在恶化。

### 摩登大道治理报道：高管集中离职、账户冻结与反复战略转型

- Evidence ID: `management-exits-and-strategy-instability`
- 发布日期 / Published: 2019-10-14
- 来源 / Source: 中国经济网转载的每日经济新闻调查
- URL: https://finance.ce.cn/stock/gsgdbd/201910/14/t20191014_33331889.shtml

报道梳理公司独立董事和财务总监集中离职，部分独董此前明确反对实控人越权担保；公司在办理银行业务时发现账户冻结，随后才自查出未经过董事会、股东大会和用章审批的担保。报道还回顾公司从服装零售、跨境电商到其他方向的多次战略调整，以及消费行业放缓和渠道压力。治理监督者退出、实控人越权和主营承压共同削弱“仅是非经营性问题、很快可修复”的叙事。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 结果日期 / Resolved at: 2020-05-30

### 实际结果 / Realized outcome

- **observations**:
  - **qualifying_nonstandard_first_annual_audit_count_18m**: 0
  - **first_post_snapshot_annual_audit_report_count_18m**: 1
  - **first_annual_audit_nonstandard**: 0
  - **first_annual_audit_standard_unqualified**: 1
  - **calendar_days_to_first_annual_audit**: 138
  - **internal_control_audit_used_for_label**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-illegal-guarantees`
- `q3-operating-decline-cash-and-goodwill`
- `management-exits-and-strategy-instability`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_next_annual_audit_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002656.XSHE
  - **ticker**: 002656
  - **name_as_of**: ST摩登
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-01-13
  - **allowed_domains**:
    - dfcfw.com
    - sina.com.cn
    - ce.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - is_st
    - special_treatment_info
  - **row_policy**: stock_code=002656.XSHE; only point-in-time financial rows and public evidence available no later than 2020-01-13; the first annual financial-statement audit report strictly after the snapshot is resolved inside a fixed 18-calendar-month window
  - **st_cause_taxonomy**: non_operating_governance/illegal_guarantees
  - **matching_group**: first-post-snapshot-annual-financial-audit-18m-v1
  - **matching_role**: no_event_standard_audit_hard_control
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice_exchange_mirror**: 09d3b381eac2bfecf8ef504fb3203b2f3dadfe0f0b676e072d67bcc9885e66e2
    - **2019_third_quarter_report_exchange_mirror**: d7f82607f662f6cc1cf66c974f08ad11fd83e5eed98b1fb776697e3707976e96
  - **news_evidence_policy**: Contemporaneous reporting may provide management-turnover and strategy context; filings remain authority for the guarantee exposure and PIT financials.
  - **outcome_contract**: Use only the first annual financial-statement audit report publicly disclosed strictly after as_of and no later than window_end. Qualified, adverse, disclaimer, or unqualified with an emphasis, going-concern material-uncertainty, or uncorrected-other-information paragraph counts as nonstandard. Internal-control audit opinions never determine this label.
  - **label_authority**: The exact future annual financial-statement audit report is label-side only; annual-report summaries may corroborate but cannot replace the signed audit report.
  - **leakage_guard**: All future audit reports, audit-opinion wording, later remediation, warning-removal, delisting and price outcomes remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_first_post_snapshot_annual_financial_statement_audit_report
    - **title**: 摩登2019年度财务报表审计报告
    - **fiscal_year**: 2019
    - **published_at**: 2020-05-30
    - **url**: https://static.cninfo.com.cn/finalpage/2020-05-30/1207878595.PDF
    - **sha256**: dd461545558c4a10ddca8efbfcf07da0b36b9efa57d6d7a2e1248b303e896656
    - **audit_opinion**: 标准无保留意见
    - **qualifies_as_nonstandard**: false
    - **qualification_basis**: 财务报表审计报告为标准无保留意见
    - **is_first_annual_financial_statement_audit_after_snapshot**: true
    - **inside_18_calendar_month_window**: true
    - **internal_control_opinion_not_used**: true
    - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
    - **pdf_text_mode**: native PDFium text extraction (--no-ocr)

</details>

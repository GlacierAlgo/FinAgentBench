# cn-a-2020-next-annual-audit-000408

## Question

你处在2020-05-06收盘后的信息环境，*ST藏格已经进入风险警示状态。请仅使用下方冻结资料，预测快照后严格首份年度财务报表审计报告是否会在未来18个自然月内构成target定义的非标准审计报告。把资金占用或违规担保规模、清偿与可审计性、报表层重大错报、审计范围受限、持续经营和现金质量分别判断；不要把ST/*ST标签、整改承诺、后来摘帽或退市、股价表现、以及内部控制审计意见直接当成财务报表审计结论。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST藏格 (000408, SZSE)
- 信息截止 / As of: 2020-05-06
- 预测窗口结束 / Window end: 2021-11-06
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 判定定义 / Definition: 在快照日之后严格首次公开披露、且不晚于未来18个自然月窗口结束日的年度财务报表审计报告，是否为非标准审计报告。保留意见、否定意见、无法表示意见，以及带强调事项段、持续经营重大不确定性段或其他信息未更正重大错报说明的无保留意见均计为事件；标准无保留意见不计。只认年度财务报表审计报告，不认内部控制审计报告、监管问询、业绩预告、整改声明或更晚年度报告

#### 判定条件 / Criteria

- `qualifying_nonstandard_first_annual_audit_count_18m >= 1` — 窗口内首份快照后年度财务报表审计报告符合非标准定义

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 藏格控股退市风险警示公告：2019年财报被出具无法表示意见

- Evidence ID: `star-st-notice-audit-disclaimer`
- 发布日期 / Published: 2020-04-30
- 来源 / Source: 深圳证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-04-30/1207687963.PDF

公司自2020年5月6日起变更为*ST藏格。直接触发条件是2019年度财务会计报告被中审众环出具无法表示意见。董事会提出自查关联资金、强化资产人员财务独立和内部审计，但仅是拟采取措施；若2020年度仍被出具否定或无法表示意见，当时规则下股票可能暂停上市。

### 藏格控股2019年审计报告：低现金、关联占用与巨龙铜业抵债资产风险

- Evidence ID: `audit-report-occupation-and-risky-equity-setoff`
- 发布日期 / Published: 2020-04-30
- 来源 / Source: 巨潮资讯法定审计报告
- URL: https://static.cninfo.com.cn/finalpage/2020-04-30/1207687966.PDF

2019年末货币资金8,209.96万元、应收账款10.6515亿元、其他应收款4.7458亿元，短期借款4.15亿元；营业收入20.6415亿元、归母净利润3.5952亿元、经营活动现金流净额2.7700亿元。附注披露控股股东相关直接占用余额2.6488亿元，并通过客户欠款形成间接占用；公司以25.9亿元受让巨龙铜业37%股权抵偿占款。该联营企业又为关联方约30亿元借款提供担保、存在逾期负债、停建停采和持续经营重大不确定性，说明“以资抵债”并非无风险现金回收。

### 藏格控股2020年一季报PIT财务：利润和经营现金流为正但现金较薄

- Evidence ID: `q1-profitable-operation-but-thin-cash`
- 发布日期 / Published: 2020-04-30
- 来源 / Source: 只读RQData点时财务记录（对应法定一季报）
- URL: https://static.cninfo.com.cn/finalpage/2020-04-30/1207687954.PDF

只读PIT记录显示2020年一季度营业收入2.7242亿元、归母净利润2,438.08万元、扣非归母净利润3,533.01万元、经营活动现金流净额1.1272亿元；期末货币资金6,857.37万元、短期借款2.95亿元、归母净资产78.6092亿元。经营仍能产生现金，但风险警示源于审计证据和治理，而不是单一季度是否盈利。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 结果日期 / Resolved at: 2021-04-13

### 实际结果 / Realized outcome

- **observations**:
  - **qualifying_nonstandard_first_annual_audit_count_18m**: 0
  - **first_post_snapshot_annual_audit_report_count_18m**: 1
  - **first_annual_audit_nonstandard**: 0
  - **first_annual_audit_standard_unqualified**: 1
  - **calendar_days_to_first_annual_audit**: 342
  - **internal_control_audit_used_for_label**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `star-st-notice-audit-disclaimer`
- `audit-report-occupation-and-risky-equity-setoff`
- `q1-profitable-operation-but-thin-cash`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_next_annual_audit_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000408.XSHE
  - **ticker**: 000408
  - **name_as_of**: *ST藏格
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-05-06
  - **allowed_domains**:
    - cninfo.com.cn
    - szse.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - is_st
    - special_treatment_info
  - **row_policy**: stock_code=000408.XSHE; only point-in-time financial rows and public evidence available no later than 2020-05-06; the first annual financial-statement audit report strictly after the snapshot is resolved inside a fixed 18-calendar-month window
  - **st_cause_taxonomy**: mixed_delisting_and_governance/audit_disclaimer+related_party_fund_occupation
  - **matching_group**: first-post-snapshot-annual-financial-audit-18m-v1
  - **matching_role**: no_event_standard_audit_hard_control
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: eef850276dc97754959ec1148d1909c36978a194951d2dc4e386371b5c2f3d06
    - **audit_report**: 1048a3e2adbd166c9dd05ea810d5bb0afb3adaaf949d38a454f180856b69ac69
  - **news_evidence_policy**: Only documents published no later than as_of enter the frozen corpus. Media reporting is an attributed point-in-time clue, never label authority.
  - **outcome_contract**: Use only the first annual financial-statement audit report publicly disclosed strictly after as_of and no later than window_end. Qualified, adverse, disclaimer, or unqualified with an emphasis, going-concern material-uncertainty, or uncorrected-other-information paragraph counts as nonstandard. Internal-control audit opinions never determine this label.
  - **label_authority**: The exact future annual financial-statement audit report is label-side only; annual-report summaries may corroborate but cannot replace the signed audit report.
  - **leakage_guard**: All future audit reports, audit-opinion wording, later remediation, warning-removal, delisting and price outcomes remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_first_post_snapshot_annual_financial_statement_audit_report
    - **title**: *ST藏格2020年度财务报表审计报告
    - **fiscal_year**: 2020
    - **published_at**: 2021-04-13
    - **url**: https://static.cninfo.com.cn/finalpage/2021-04-13/1209678615.PDF
    - **sha256**: aa5532f5476c83b9556e27603900949ea81932a736ebd513e05f2be540b64e71
    - **audit_opinion**: 标准的无保留意见
    - **qualifies_as_nonstandard**: false
    - **qualification_basis**: 财务报表审计报告为标准无保留意见
    - **is_first_annual_financial_statement_audit_after_snapshot**: true
    - **inside_18_calendar_month_window**: true
    - **internal_control_opinion_not_used**: true
    - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
    - **pdf_text_mode**: native PDFium text extraction (--no-ocr)

</details>

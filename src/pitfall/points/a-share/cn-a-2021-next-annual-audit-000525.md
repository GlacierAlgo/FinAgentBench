# cn-a-2021-next-annual-audit-000525

## Question

你处在2021-05-06收盘后的信息环境，ST红太阳已经进入风险警示状态。请仅使用下方冻结资料，预测快照后严格首份年度财务报表审计报告是否会在未来18个自然月内构成target定义的非标准审计报告。把资金占用或违规担保规模、清偿与可审计性、报表层重大错报、审计范围受限、持续经营和现金质量分别判断；不要把ST/*ST标签、整改承诺、后来摘帽或退市、股价表现、以及内部控制审计意见直接当成财务报表审计结论。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST红太阳 (000525, SZSE)
- 信息截止 / As of: 2021-05-06
- 预测窗口结束 / Window end: 2022-11-06
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 判定定义 / Definition: 在快照日之后严格首次公开披露、且不晚于未来18个自然月窗口结束日的年度财务报表审计报告，是否为非标准审计报告。保留意见、否定意见、无法表示意见，以及带强调事项段、持续经营重大不确定性段或其他信息未更正重大错报说明的无保留意见均计为事件；标准无保留意见不计。只认年度财务报表审计报告，不认内部控制审计报告、监管问询、业绩预告、整改声明或更晚年度报告

#### 判定条件 / Criteria

- `qualifying_nonstandard_first_annual_audit_count_18m >= 1` — 窗口内首份快照后年度财务报表审计报告符合非标准定义

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 红太阳实施其他风险警示公告：近29.64亿元占用预计一个月内无法解决

- Evidence ID: `st-notice-near-three-billion-occupation`
- 发布日期 / Published: 2021-04-29
- 来源 / Source: 深圳证券交易所法定公告PDF镜像
- URL: https://pdf.dfcfw.com/pdf/H2_AN202104291488680395_1.pdf

公司自2021年5月6日起变更为ST红太阳，日涨跌幅限制5%。公告称截至2021年4月28日，控股股东南一农集团及关联方非经营性占用余额29.639845亿元，预计无法在一个月内解决；2020年度内部控制审计报告为否定意见。公告解释控股股东流动性危机源于融资收紧，并披露部分所谓归还资金随后又被用于为控股股东和红太阳集团融资提供担保质押，最终被银行划转，显示资金回流并不等于风险实质消除。公司同时仍处于证监会立案调查期间。

### 红太阳2020年年度报告：农药主业、扣非亏损和现金短债矛盾

- Evidence ID: `annual-agrochemical-financial-stress`
- 发布日期 / Published: 2021-04-30
- 来源 / Source: 巨潮资讯法定年度报告
- URL: https://static.cninfo.com.cn/finalpage/2021-04-30/1209871241.PDF

2020年营业收入40.2200亿元，同比下降12.84%；归母净利润-1.5381亿元，扣非归母净利润-2.6609亿元；经营活动现金流净额2.3124亿元。农药销售收入39.8589亿元、占收入99.10%，毛利率18.77%，同比下降13.49个百分点；产量22.90万吨、销量19.50万吨、库存同比增长17%。期末货币资金1.9811亿元，短期借款37.9076亿元，流动资产55.8644亿元低于流动负债64.6997亿元；其他应收款32.2476亿元，接近当年收入的80%，主要风险与关联占用一致。年报称出口和汇率受疫情冲击，并计提存货与应收减值1.0635亿元。

### 2021年4月农化行业报告：草甘膦涨价，但不可无证据外推到红太阳

- Evidence ID: `sector-boom-with-exposure-attribution-trap`
- 发布日期 / Published: 2021-04-30
- 来源 / Source: 国信证券行业报告（东方财富PDF镜像）
- URL: https://pdf.dfcfw.com/pdf/H3_AP202105061490021000_1.pdf

行业报告称草甘膦报价35,312元/吨，30日上涨12.10%，较年初上涨29.09%，并判断全球粮食安全、供给集中和高开工率可能延长景气；其列示的主要草甘膦企业包括兴发、江山、新安和扬农，并未列出红太阳。红太阳年报只按“农药销售”汇总披露，未在该表证明草甘膦原药产能。因此该报告既是行业上行信号，也是暴露归因陷阱：模型必须寻找公司产品结构证据，不能把热门品种涨价自动当成红太阳盈利催化。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 结果日期 / Resolved at: 2022-04-30

### 实际结果 / Realized outcome

- **observations**:
  - **qualifying_nonstandard_first_annual_audit_count_18m**: 1
  - **first_post_snapshot_annual_audit_report_count_18m**: 1
  - **first_annual_audit_nonstandard**: 1
  - **first_annual_audit_standard_unqualified**: 0
  - **calendar_days_to_first_annual_audit**: 359
  - **internal_control_audit_used_for_label**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-near-three-billion-occupation`
- `annual-agrochemical-financial-stress`
- `sector-boom-with-exposure-attribution-trap`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_next_annual_audit_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000525.XSHE
  - **ticker**: 000525
  - **name_as_of**: ST红太阳
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-05-06
  - **allowed_domains**:
    - cninfo.com.cn
    - dfcfw.com
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - is_st
    - special_treatment_info
  - **row_policy**: stock_code=000525.XSHE; only point-in-time financial rows and public evidence available no later than 2021-05-06; the first annual financial-statement audit report strictly after the snapshot is resolved inside a fixed 18-calendar-month window
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation+adverse_internal_control
  - **matching_group**: first-post-snapshot-annual-financial-audit-18m-v1
  - **matching_role**: event_nonstandard_audit
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice_exchange_mirror**: a09e14a6a5860d11fcfb194c5449bcf87e94edd3ca4951aa85dca44bde64ddf6
    - **2020_annual_report**: 92441de1093f0fbf952e60343afe48da4852733508b35c83b487700dbc51fa0c
  - **news_evidence_policy**: A contemporaneous sector report is deliberately included as a possible exposure-misattribution trap; the company filing must support any claimed product linkage.
  - **outcome_contract**: Use only the first annual financial-statement audit report publicly disclosed strictly after as_of and no later than window_end. Qualified, adverse, disclaimer, or unqualified with an emphasis, going-concern material-uncertainty, or uncorrected-other-information paragraph counts as nonstandard. Internal-control audit opinions never determine this label.
  - **label_authority**: The exact future annual financial-statement audit report is label-side only; annual-report summaries may corroborate but cannot replace the signed audit report.
  - **leakage_guard**: All future audit reports, audit-opinion wording, later remediation, warning-removal, delisting and price outcomes remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_first_post_snapshot_annual_financial_statement_audit_report
    - **title**: 红太阳2021年度财务报表审计报告
    - **fiscal_year**: 2021
    - **published_at**: 2022-04-30
    - **url**: https://static.cninfo.com.cn/finalpage/2022-04-30/1213264695.PDF
    - **sha256**: ab2da0b8a514787b8647df2994045482e01b0526f3aeeb3a05f279231ffca95c
    - **audit_opinion**: 保留意见
    - **qualifies_as_nonstandard**: true
    - **qualification_basis**: 财务报表审计报告为保留意见
    - **is_first_annual_financial_statement_audit_after_snapshot**: true
    - **inside_18_calendar_month_window**: true
    - **internal_control_opinion_not_used**: true
    - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
    - **pdf_text_mode**: native PDFium text extraction (--no-ocr)

</details>

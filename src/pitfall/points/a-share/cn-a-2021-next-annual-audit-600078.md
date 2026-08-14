# cn-a-2021-next-annual-audit-600078

## Question

你处在2021-05-06收盘后的信息环境，*ST澄星已经进入风险警示状态。请仅使用下方冻结资料，预测快照后严格首份年度财务报表审计报告是否会在未来18个自然月内构成target定义的非标准审计报告。把资金占用或违规担保规模、清偿与可审计性、报表层重大错报、审计范围受限、持续经营和现金质量分别判断；不要把ST/*ST标签、整改承诺、后来摘帽或退市、股价表现、以及内部控制审计意见直接当成财务报表审计结论。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST澄星 (600078, SSE)
- 信息截止 / As of: 2021-05-06
- 预测窗口结束 / Window end: 2022-11-06
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 判定定义 / Definition: 在快照日之后严格首次公开披露、且不晚于未来18个自然月窗口结束日的年度财务报表审计报告，是否为非标准审计报告。保留意见、否定意见、无法表示意见，以及带强调事项段、持续经营重大不确定性段或其他信息未更正重大错报说明的无保留意见均计为事件；标准无保留意见不计。只认年度财务报表审计报告，不认内部控制审计报告、监管问询、业绩预告、整改声明或更晚年度报告

#### 判定条件 / Criteria

- `qualifying_nonstandard_first_annual_audit_count_18m >= 1` — 窗口内首份快照后年度财务报表审计报告符合非标准定义

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 澄星股份退市风险警示公告：负净资产、无法表示意见、内控否定与资金占用并存

- Evidence ID: `star-st-notice-multiple-triggers`
- 发布日期 / Published: 2021-04-30
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/new/2021-04-30/600078_20210430_20.pdf

公司自2021年5月6日起变更为*ST澄星，日涨跌幅限制5%。公告列出四类相互叠加的风险：2020年度财务报告内部控制被出具否定意见；控股股东及关联方资金占用到期未解决；经审计期末净资产为负；年度财务报告被出具无法表示意见。因此公司既触发其他风险警示，也触发退市风险警示。董事会仅表示将督促控股股东多途径解决占用并加强内控，没有给出已锁定的清偿资源或完成日期。

### 澄星股份2020年年度报告：22.16亿元亏损、负权益与黄磷产品敞口

- Evidence ID: `annual-loss-debt-and-phosphorus-exposure`
- 发布日期 / Published: 2021-04-30
- 来源 / Source: 上海证券交易所法定年度报告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/new/2021-04-30/600078_20210430_2.pdf

2020年营业收入31.3655亿元，同比下降5.24%；归母净利润-22.1586亿元，扣非归母净利润-22.5797亿元；期末归母净资产-4.7615亿元。经营活动现金流净额7.3079亿元为正，但货币资金仅3.9637亿元，短期借款37.1544亿元，流动负债50.2446亿元而流动资产16.4127亿元。报告披露控股股东及相关方期末非经营性占用21.7760亿元，其中通过绿澄化工形成15.6789亿元。黄磷收入9.7279亿元、同比增长43.38%，销量7.06万吨、期末库存3.80万吨，但黄磷毛利率仅10.08%且同比下降5.93个百分点。行业敞口、正经营现金流与极端偿债/治理风险并存。

### 2021年4月化工行业报告：草甘膦景气与黄磷成本传导

- Evidence ID: `contemporaneous-yellow-phosphorus-chain-pricing`
- 发布日期 / Published: 2021-04-30
- 来源 / Source: 国信证券行业报告（东方财富PDF镜像）
- URL: https://pdf.dfcfw.com/pdf/H3_AP202105061490021000_1.pdf

行业报告称截至4月28日草甘膦报价35,312元/吨，较年初上涨29.09%、同比上涨约73%，生产商订单多排至2021年8月；黄磷报价17,481元/吨，较年初上涨10.46%，是甘氨酸法草甘膦的重要成本项之一。报告判断环保约束、供应偏紧和农产品景气可能支撑产业链，但重点标的是草甘膦龙头，不是澄星股份。对澄星只能把黄磷价格作为潜在经营杠杆，必须结合其产销、毛利、债务和资金占用，不能把下游景气直接移植为公司利润或股价结论。

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

- `star-st-notice-multiple-triggers`
- `annual-loss-debt-and-phosphorus-exposure`
- `contemporaneous-yellow-phosphorus-chain-pricing`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_next_annual_audit_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600078.XSHG
  - **ticker**: 600078
  - **name_as_of**: *ST澄星
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-05-06
  - **allowed_domains**:
    - sse.com.cn
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
  - **row_policy**: stock_code=600078.XSHG; only point-in-time financial rows and public evidence available no later than 2021-05-06; the first annual financial-statement audit report strictly after the snapshot is resolved inside a fixed 18-calendar-month window
  - **st_cause_taxonomy**: mixed_delisting_and_governance/negative_equity+audit_disclaimer+related_party_fund_occupation
  - **matching_group**: first-post-snapshot-annual-financial-audit-18m-v1
  - **matching_role**: event_nonstandard_audit
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: 0a159af4d13992484fc30f9331f9fb523cc32ac9918ba8fee814fb75ee17efad
    - **2020_annual_report**: 525a725eb1ff14d84fb882213090432709f489a5963c963887771970e8644379
    - **contemporaneous_industry_report**: 50a099ec575f6587928aaa270ce3896509d227a7d46e6067260369cfae54a6f9
  - **news_evidence_policy**: The contemporaneous chemical-industry report supplies only point-in-time price-chain context; company filings remain the authority on direct exposure and balance-sheet risk.
  - **outcome_contract**: Use only the first annual financial-statement audit report publicly disclosed strictly after as_of and no later than window_end. Qualified, adverse, disclaimer, or unqualified with an emphasis, going-concern material-uncertainty, or uncorrected-other-information paragraph counts as nonstandard. Internal-control audit opinions never determine this label.
  - **label_authority**: The exact future annual financial-statement audit report is label-side only; annual-report summaries may corroborate but cannot replace the signed audit report.
  - **leakage_guard**: All future audit reports, audit-opinion wording, later remediation, warning-removal, delisting and price outcomes remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_first_post_snapshot_annual_financial_statement_audit_report
    - **title**: *ST澄星2021年度财务报表审计报告
    - **fiscal_year**: 2021
    - **published_at**: 2022-04-30
    - **url**: https://static.cninfo.com.cn/finalpage/2022-04-30/1213268101.PDF
    - **sha256**: ad5c40d34afbc88c5f33e8dbd067e4dd895759f872d42d2d0c527ad328148132
    - **audit_opinion**: 带强调事项段、持续经营重大不确定性段落、其他信息段落中包含其他信息未更正重大错报说明的无保留意见
    - **qualifies_as_nonstandard**: true
    - **qualification_basis**: 财务报表审计报告虽为无保留意见，但包含强调事项段、持续经营重大不确定性段和其他信息未更正重大错报说明，按目标定义计为非标准
    - **is_first_annual_financial_statement_audit_after_snapshot**: true
    - **inside_18_calendar_month_window**: true
    - **internal_control_opinion_not_used**: true
    - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
    - **pdf_text_mode**: native PDFium text extraction (--no-ocr)

</details>

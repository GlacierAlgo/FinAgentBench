# cn-a-2020-next-annual-audit-600702

## Question

你处在2020-09-22收盘后的信息环境，ST舍得已经进入风险警示状态。请仅使用下方冻结资料，预测快照后严格首份年度财务报表审计报告是否会在未来18个自然月内构成target定义的非标准审计报告。把资金占用或违规担保规模、清偿与可审计性、报表层重大错报、审计范围受限、持续经营和现金质量分别判断；不要把ST/*ST标签、整改承诺、后来摘帽或退市、股价表现、以及内部控制审计意见直接当成财务报表审计结论。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST舍得 (600702, SSE)
- 信息截止 / As of: 2020-09-22
- 预测窗口结束 / Window end: 2022-03-22
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 判定定义 / Definition: 在快照日之后严格首次公开披露、且不晚于未来18个自然月窗口结束日的年度财务报表审计报告，是否为非标准审计报告。保留意见、否定意见、无法表示意见，以及带强调事项段、持续经营重大不确定性段或其他信息未更正重大错报说明的无保留意见均计为事件；标准无保留意见不计。只认年度财务报表审计报告，不认内部控制审计报告、监管问询、业绩预告、整改声明或更晚年度报告

#### 判定条件 / Criteria

- `qualifying_nonstandard_first_annual_audit_count_18m >= 1` — 窗口内首份快照后年度财务报表审计报告符合非标准定义

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 舍得酒业实施其他风险警示公告：4.7486亿元资金占用未按承诺归还

- Evidence ID: `st-notice-cause-and-unresolved-occupation`
- 发布日期 / Published: 2020-09-21
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2020-09-21/600702_20200921_1.pdf

公告称公司自2020年9月22日起变更为ST舍得，日涨跌幅限制5%。截至2020年8月19日，间接控股股东天洋控股及关联方非经营性占用本金4.40亿元、利息3,486万元，合计4.7486亿元；截至公告日仍未在9月19日承诺期限前归还。董事会提出督促筹资、制定还款计划，并明确可能通过股权转让等方式弥补占用。戴帽直接原因是非经营性资金占用与治理问题，而不是年报亏损触发的退市风险警示；但资金是否能回收及控制权路径高度不确定。

### 舍得酒业2020年半年度报告：高毛利主业承压、经营现金流为负并出现大额拆借

- Evidence ID: `h1-financials-and-liquor-operations`
- 发布日期 / Published: 2020-08-29
- 来源 / Source: 上海证券交易所法定半年度报告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2020-08-29/600702_20200829_2.pdf

2020年上半年营业收入10.2590亿元，同比下降15.95%；归母净利润1.6419亿元，同比下降11.45%；扣非归母净利润1.4723亿元；经营活动现金流净额-6,145.03万元。营业成本2.5646亿元，对应综合毛利率约75%。期末货币资金11.5877亿元、短期借款10.04亿元、存货25.2790亿元、归母净资产32.1723亿元。其他应收款从年初4,665.09万元增至5.2505亿元，其中对蓬山酒业拆借款本金4.40亿元及占用费3,160万元；报告称疫情使销售、回款和营销活动下降。高毛利、品牌和存酒资产与治理抽血、负经营现金流同时存在。

### 中证网食品饮料行业观点：白酒场景复苏但板块分化，舍得中报被列为超预期

- Evidence ID: `contemporaneous-liquor-recovery-and-differentiation`
- 发布日期 / Published: 2020-09-08
- 来源 / Source: 中国证券报·中证网转载的兴业证券行业观点
- URL: https://www.cs.com.cn/gppd/sdqs/202009/t20200908_6092739.html

同时点行业观点认为疫情冲击具有阶段性，白酒三季度复苏弹性可期，但竞争格局将进一步分化，高端酒更稳健、区域次高端品牌才可能持续增长。观点明确将舍得酒业列为中报超预期、值得重点关注的公司之一，同时列示宏观下滑、成本上升、食品安全和行业竞争等风险。这提供当时已有的行业与公司经营预期，不能证明资金占用会解决，也不能直接推出股价路径。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 结果日期 / Resolved at: 2021-04-29

### 实际结果 / Realized outcome

- **observations**:
  - **qualifying_nonstandard_first_annual_audit_count_18m**: 0
  - **first_post_snapshot_annual_audit_report_count_18m**: 1
  - **first_annual_audit_nonstandard**: 0
  - **first_annual_audit_standard_unqualified**: 1
  - **calendar_days_to_first_annual_audit**: 219
  - **internal_control_audit_used_for_label**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-cause-and-unresolved-occupation`
- `h1-financials-and-liquor-operations`
- `contemporaneous-liquor-recovery-and-differentiation`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_next_annual_audit_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600702.XSHG
  - **ticker**: 600702
  - **name_as_of**: ST舍得
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-09-22
  - **allowed_domains**:
    - sse.com.cn
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
  - **row_policy**: stock_code=600702.XSHG; only point-in-time financial rows and public evidence available no later than 2020-09-22; the first annual financial-statement audit report strictly after the snapshot is resolved inside a fixed 18-calendar-month window
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation
  - **matching_group**: first-post-snapshot-annual-financial-audit-18m-v1
  - **matching_role**: no_event_standard_audit_hard_control
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: 6a964e0c45d9afc2f6b1f2a360c820253ebb51f5d69e6a90bfc69031b665e16d
    - **2020_half_year_report**: 00679be8d6b8fb0dee1e9b81b32bebbae9717c4a18648813ea4450cc36a29475
  - **news_evidence_policy**: Only contemporaneous industry framing published no later than as_of may enter the corpus; it cannot reveal or define the future price label.
  - **outcome_contract**: Use only the first annual financial-statement audit report publicly disclosed strictly after as_of and no later than window_end. Qualified, adverse, disclaimer, or unqualified with an emphasis, going-concern material-uncertainty, or uncorrected-other-information paragraph counts as nonstandard. Internal-control audit opinions never determine this label.
  - **label_authority**: The exact future annual financial-statement audit report is label-side only; annual-report summaries may corroborate but cannot replace the signed audit report.
  - **leakage_guard**: All future audit reports, audit-opinion wording, later remediation, warning-removal, delisting and price outcomes remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_first_post_snapshot_annual_financial_statement_audit_report
    - **title**: 舍得2020年度财务报表审计报告
    - **fiscal_year**: 2020
    - **published_at**: 2021-04-29
    - **url**: https://static.cninfo.com.cn/finalpage/2021-04-29/1209860907.PDF
    - **sha256**: 4cb7ca82df909fc9212c11a8c085418bf8f183a7928637f66894ac63895f83a2
    - **audit_opinion**: 标准无保留意见
    - **qualifies_as_nonstandard**: false
    - **qualification_basis**: 财务报表审计报告为标准无保留意见
    - **is_first_annual_financial_statement_audit_after_snapshot**: true
    - **inside_18_calendar_month_window**: true
    - **internal_control_opinion_not_used**: true
    - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
    - **pdf_text_mode**: native PDFium text extraction (--no-ocr)

</details>

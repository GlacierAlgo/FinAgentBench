# cn-a-2019-next-annual-audit-600290

## Question

你处在2019-12-26收盘后的信息环境，ST华仪已经进入风险警示状态。请仅使用下方冻结资料，预测快照后严格首份年度财务报表审计报告是否会在未来18个自然月内构成target定义的非标准审计报告。把资金占用或违规担保规模、清偿与可审计性、报表层重大错报、审计范围受限、持续经营和现金质量分别判断；不要把ST/*ST标签、整改承诺、后来摘帽或退市、股价表现、以及内部控制审计意见直接当成财务报表审计结论。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST华仪 (600290, SSE)
- 信息截止 / As of: 2019-12-26
- 预测窗口结束 / Window end: 2021-06-26
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 判定定义 / Definition: 在快照日之后严格首次公开披露、且不晚于未来18个自然月窗口结束日的年度财务报表审计报告，是否为非标准审计报告。保留意见、否定意见、无法表示意见，以及带强调事项段、持续经营重大不确定性段或其他信息未更正重大错报说明的无保留意见均计为事件；标准无保留意见不计。只认年度财务报表审计报告，不认内部控制审计报告、监管问询、业绩预告、整改声明或更晚年度报告

#### 判定条件 / Criteria

- `qualifying_nonstandard_first_annual_audit_count_18m >= 1` — 窗口内首份快照后年度财务报表审计报告符合非标准定义

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 华仪电气实施其他风险警示公告：10.58亿元占用与9.259亿元违规担保

- Evidence ID: `st-notice-occupation-and-guarantees`
- 发布日期 / Published: 2019-12-25
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2019-12-25/600290_20191225_1.pdf

公司自2019年12月26日起变更为ST华仪。公告称违规担保金额9.2590亿元，占最近一期经审计净资产22.75%，其中逾期担保2.14亿元；关联方资金占用余额10.58亿元，占净资产26.00%。控股股东未在自2019年11月25日起一个月的承诺期限内解决，直接触发其他风险警示。公告没有可验证的还款资金，只表示继续催促、通过法律途径处理并至少每月披露进展。

### 华仪电气2019年三季报：账面现金较高，但收入、扣非利润与应收质量偏弱

- Evidence ID: `q3-cash-receivables-and-weak-operations`
- 发布日期 / Published: 2019-10-31
- 来源 / Source: 上海证券交易所法定季度报告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2019-10-31/600290_2019_3.pdf

2019年前三季度营业收入8.0757亿元，同比下降25.75%；归母净利润1,102.28万元，同比下降36.04%，扣非归母净利润-2,982.85万元；经营活动现金流净额1.0042亿元。期末货币资金15.7874亿元、短期借款5.3413亿元，看似流动性充裕，但应收账款21.0521亿元，是前三季度收入的约2.61倍，另有预付款2.5007亿元。结合随后披露的10.58亿元控股股东占用，账面现金不能被机械视为可自由使用资金。

### 2019年风电设备行业观点：三年抢装开启，但采购向龙头集中

- Evidence ID: `wind-installation-boom-and-leader-concentration`
- 发布日期 / Published: 2019-06-03
- 来源 / Source: 中国证券报·中证网转载的兴业证券行业观点
- URL: https://www.cs.com.cn/gppd/sdqs/201906/t20190603_5954690.html

行业观点预计补贴并网期限推动2019至2021年风电持续抢装，年均装机规模可能超过30GW，短期需求和盈利迎来拐点；同时强调平价时代运营商更重视发电效率、产品质量和运维费用，市场份额可能进一步向龙头集中。推荐名单聚焦金风科技、天顺风能等细分龙头，没有华仪电气。该材料说明行业总量向好和尾部厂商兑现可能分化，不能用“风电抢装”掩盖公司应收、占用与治理风险。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 结果日期 / Resolved at: 2020-04-24

### 实际结果 / Realized outcome

- **observations**:
  - **qualifying_nonstandard_first_annual_audit_count_18m**: 1
  - **first_post_snapshot_annual_audit_report_count_18m**: 1
  - **first_annual_audit_nonstandard**: 1
  - **first_annual_audit_standard_unqualified**: 0
  - **calendar_days_to_first_annual_audit**: 120
  - **internal_control_audit_used_for_label**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-occupation-and-guarantees`
- `q3-cash-receivables-and-weak-operations`
- `wind-installation-boom-and-leader-concentration`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_next_annual_audit_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600290.XSHG
  - **ticker**: 600290
  - **name_as_of**: ST华仪
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-12-26
  - **allowed_domains**:
    - sse.com.cn
    - cs.com.cn
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
  - **row_policy**: stock_code=600290.XSHG; only point-in-time financial rows and public evidence available no later than 2019-12-26; the first annual financial-statement audit report strictly after the snapshot is resolved inside a fixed 18-calendar-month window
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation+illegal_guarantees
  - **matching_group**: first-post-snapshot-annual-financial-audit-18m-v1
  - **matching_role**: event_nonstandard_audit
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: d6aad276b1294a65a1bfaaa71f7591236bb680d8f10c04e972b916147f43bc67
    - **2019_third_quarter_report**: 53fa5ec62fdfab02628c876388e25e3705497e8bcd6e49e9a22aff3cfde66314
  - **news_evidence_policy**: Contemporaneous news may frame the wind-installation cycle and disclosed governance failures; official filings and RQData remain label authority.
  - **outcome_contract**: Use only the first annual financial-statement audit report publicly disclosed strictly after as_of and no later than window_end. Qualified, adverse, disclaimer, or unqualified with an emphasis, going-concern material-uncertainty, or uncorrected-other-information paragraph counts as nonstandard. Internal-control audit opinions never determine this label.
  - **label_authority**: The exact future annual financial-statement audit report is label-side only; annual-report summaries may corroborate but cannot replace the signed audit report.
  - **leakage_guard**: All future audit reports, audit-opinion wording, later remediation, warning-removal, delisting and price outcomes remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_first_post_snapshot_annual_financial_statement_audit_report
    - **title**: 华仪2019年度财务报表审计报告
    - **fiscal_year**: 2019
    - **published_at**: 2020-04-24
    - **url**: https://static.cninfo.com.cn/finalpage/2020-04-24/1207588634.PDF
    - **sha256**: 22a94ac0d51b470951fd7e585d952131fb42d0dcd1f6ebd0270b79ee7f08fbc0
    - **audit_opinion**: 保留意见
    - **qualifies_as_nonstandard**: true
    - **qualification_basis**: 财务报表审计报告为保留意见
    - **is_first_annual_financial_statement_audit_after_snapshot**: true
    - **inside_18_calendar_month_window**: true
    - **internal_control_opinion_not_used**: true
    - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
    - **pdf_text_mode**: native PDFium text extraction (--no-ocr)

</details>

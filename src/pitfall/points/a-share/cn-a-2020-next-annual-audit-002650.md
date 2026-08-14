# cn-a-2020-next-annual-audit-002650

## Question

你处在2020-06-15收盘后的信息环境，ST加加已经进入风险警示状态。请仅使用下方冻结资料，预测快照后严格首份年度财务报表审计报告是否会在未来18个自然月内构成target定义的非标准审计报告。把资金占用或违规担保规模、清偿与可审计性、报表层重大错报、审计范围受限、持续经营和现金质量分别判断；不要把ST/*ST标签、整改承诺、后来摘帽或退市、股价表现、以及内部控制审计意见直接当成财务报表审计结论。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST加加 (002650, SZSE)
- 信息截止 / As of: 2020-06-15
- 预测窗口结束 / Window end: 2021-12-15
- 目标事件 / Target: `first_post_snapshot_annual_financial_statement_nonstandard_audit_18m`
- 判定定义 / Definition: 在快照日之后严格首次公开披露、且不晚于未来18个自然月窗口结束日的年度财务报表审计报告，是否为非标准审计报告。保留意见、否定意见、无法表示意见，以及带强调事项段、持续经营重大不确定性段或其他信息未更正重大错报说明的无保留意见均计为事件；标准无保留意见不计。只认年度财务报表审计报告，不认内部控制审计报告、监管问询、业绩预告、整改声明或更晚年度报告

#### 判定条件 / Criteria

- `qualifying_nonstandard_first_annual_audit_count_18m >= 1` — 窗口内首份快照后年度财务报表审计报告符合非标准定义

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 加加食品实施其他风险警示公告：4.6605亿元违规担保与刚签署的清偿协议

- Evidence ID: `st-notice-signed-settlement-but-unpaid`
- 发布日期 / Published: 2020-06-12
- 来源 / Source: 深圳证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-06-12/1207919359.PDF

公司自2020年6月15日起变更为ST加加。违规担保本金4.6605亿元，占最近一期经审计净资产19.94%，一个月内未解决。公告同时披露控制人获得2.8亿元第三方资金额度，并分别与三湘银行、优选资本签署协议：在6月30日前支付首笔1亿元和不低于1.8亿元后，相关担保责任才解除。协议和额度是具体路径，但披露日尚未满足付款与解除条件。

### 加加食品2020年一季度PIT财务：盈利、正现金流和低上市公司杠杆

- Evidence ID: `q1-strong-balance-sheet-at-listed-company`
- 发布日期 / Published: 2020-04-28
- 来源 / Source: 只读RQData点时财务记录（对应法定一季报）
- URL: https://static.cninfo.com.cn/finalpage/2020-04-28/1207639554.PDF

2020年一季度营业收入4.9211亿元、归母净利润5,026.82万元、扣非归母净利润5,006.71万元、经营活动现金流净额1.1633亿元。期末货币资金4.6015亿元、短期借款5,503.63万元、总负债3.9580亿元、归母净资产23.8711亿元。上市公司本体财务缓冲较强，但违规担保债务属于控制人融资链，不能仅用上市公司账面现金机械抵销。

### 戴帽前报道：实控人称利空出清、6月底解决并可很快摘帽

- Evidence ID: `contemporaneous-controller-claims-fast-removal`
- 发布日期 / Published: 2020-06-12
- 来源 / Source: 中国证券报·中证网转载证券时报e公司报道
- URL: https://www.cs.com.cn/ssgs/gsxw/202006/t20200612_6066759.html

报道复述两份清偿/和解协议及6月30日首付款条件，实控人进一步声称违规担保可在月底前解决、之后能够很快摘帽，公司经营正常。该表态提供管理层预期，却具有明显激励偏差；模型应以付款、担保法律解除和交易所审核为后续门槛，不能把采访表态当成结果。

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
  - **calendar_days_to_first_annual_audit**: 318
  - **internal_control_audit_used_for_label**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-signed-settlement-but-unpaid`
- `q1-strong-balance-sheet-at-listed-company`
- `contemporaneous-controller-claims-fast-removal`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_next_annual_audit_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002650.XSHE
  - **ticker**: 002650
  - **name_as_of**: ST加加
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-06-15
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
  - **row_policy**: stock_code=002650.XSHE; only point-in-time financial rows and public evidence available no later than 2020-06-15; the first annual financial-statement audit report strictly after the snapshot is resolved inside a fixed 18-calendar-month window
  - **st_cause_taxonomy**: non_operating_governance/illegal_guarantees
  - **matching_group**: first-post-snapshot-annual-financial-audit-18m-v1
  - **matching_role**: no_event_standard_audit_hard_control
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: fdb701da870263744592c52572bd2585a6e1ece51448874a9fd19f80e44b1ef6
    - **audit_report**: 9a77ffee4a8b33b5bc8c4a6b87f48c19b85f4335b66a8239c045d22dafc15883
  - **news_evidence_policy**: Only documents published no later than as_of enter the frozen corpus. Media reporting is an attributed point-in-time clue, never label authority.
  - **outcome_contract**: Use only the first annual financial-statement audit report publicly disclosed strictly after as_of and no later than window_end. Qualified, adverse, disclaimer, or unqualified with an emphasis, going-concern material-uncertainty, or uncorrected-other-information paragraph counts as nonstandard. Internal-control audit opinions never determine this label.
  - **label_authority**: The exact future annual financial-statement audit report is label-side only; annual-report summaries may corroborate but cannot replace the signed audit report.
  - **leakage_guard**: All future audit reports, audit-opinion wording, later remediation, warning-removal, delisting and price outcomes remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_first_post_snapshot_annual_financial_statement_audit_report
    - **title**: 加加2020年度财务报表审计报告
    - **fiscal_year**: 2020
    - **published_at**: 2021-04-29
    - **url**: https://static.cninfo.com.cn/finalpage/2021-04-29/1209857065.PDF
    - **sha256**: 4bae1d3b06378192190915e9dda139bc16cd93565d17c70d7615e56357f94bec
    - **audit_opinion**: 标准的无保留意见
    - **qualifies_as_nonstandard**: false
    - **qualification_basis**: 财务报表审计报告为标准无保留意见
    - **is_first_annual_financial_statement_audit_after_snapshot**: true
    - **inside_18_calendar_month_window**: true
    - **internal_control_opinion_not_used**: true
    - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
    - **pdf_text_mode**: native PDFium text extraction (--no-ocr)

</details>

# cn-a-2020-st-remediation-002650

## Question

你处在2020-06-15收盘后的信息环境。ST加加因4.6605亿元违规担保未在一个月内解除而戴帽，但控制人与两名债权方刚签署清偿或和解协议，并声称获得2.8亿元第三方额度。请使用下方冻结资料，预测未来24个自然月内是否会发生target定义的完整撤销全部风险警示。请区分协议签署、首笔付款、担保责任法律解除、诉讼终局和交易所审核，并结合公司现金、净资产、盈利与控制人高质押冻结；实控人对媒体称“很快摘帽”不能替代证据。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST加加 (002650, SZSE)
- 信息截止 / As of: 2020-06-15
- 预测窗口结束 / Window end: 2022-06-15
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来24个自然月内，证券交易所审核同意撤销公司股票交易的全部退市风险警示和全部其他风险警示，且生效后的证券简称不再含ST或*ST、股票退出风险警示板。仅提交或获董事会通过申请、占款或担保已清偿、审计意见改善、撤销一项叠加警示但仍保留任一风险警示、*ST降为ST、暂停上市后恢复或最终退市均不计为事件

#### 判定条件 / Criteria

- `full_risk_warning_removal_count_24m >= 1` — 窗口内经交易所审核同意并生效的完整撤销全部风险警示至少一次

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

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 结果日期 / Resolved at: 2021-07-28

### 实际结果 / Realized outcome

- **observations**:
  - **full_risk_warning_removal_count_24m**: 1
  - **full_risk_warning_removed_by_window_end**: 1
  - **partial_only_removal_count_24m**: 0
  - **calendar_days_to_full_removal_or_zero**: 408
  - **risk_warning_present_at_window_end**: 0
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
- **suite**: a_share_st_remediation_v1
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
  - **row_policy**: stock_code=002650.XSHE; quarter=2020q1; info_date=2020-04-28; if_adjusted=0; first risk-warning trading day=2020-06-15
  - **st_cause_taxonomy**: non_operating_governance/illegal_guarantees
  - **matching_group**: first-risk-warning-day-full-removal-24m-v1
  - **matching_role**: event_illegal_guarantee_settlement
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: fdb701da870263744592c52572bd2585a6e1ece51448874a9fd19f80e44b1ef6
    - **audit_report**: 9a77ffee4a8b33b5bc8c4a6b87f48c19b85f4335b66a8239c045d22dafc15883
  - **status_source_sha256**:
    - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
    - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
  - **outcome_contract**: Only an exchange-approved removal of every ST/*ST warning that becomes effective inside the 24-calendar-month window counts. An application, remediation, *ST-to-ST downgrade, continued ST status, or delisting does not.
  - **news_evidence_policy**: Only documents published no later than as_of enter the frozen corpus. Media reporting is an attributed point-in-time clue, never label authority.
  - **leakage_guard**: All removal approvals, later ST transitions, restructurings, delistings and post_as_of remediation facts remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_exchange_approved_full_risk_warning_removal
    - **title**: 加加食品关于公司股票撤销其他风险警示暨停复牌的公告
    - **approved_effective_date**: 2021-07-28
    - **published_at**: 2021-07-28
    - **url**: https://static.cninfo.com.cn/finalpage/2021-07-27/1210573032.PDF
    - **sha256**: fba7637fef2adb506b4fb221a0bcab28ff0cf07b3c14d9b10a9e064fdab7c6d1
    - **resulting_symbol**: 加加食品
    - **exits_risk_warning_board**: true
    - **all_risk_warnings_removed**: true
  - **item 2**:
    - **type**: rqdata_risk_warning_status_crosscheck
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2020-06-15/2022-06-15
    - **full_removal_within_window**: true
    - **partial_only_removal_count_24m**: 0

</details>

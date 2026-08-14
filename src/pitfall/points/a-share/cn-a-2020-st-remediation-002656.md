# cn-a-2020-st-remediation-002656

## Question

你处在2020-01-13收盘后的信息环境。ST摩登因实控人越权形成3.3亿元未解除担保而戴帽，同时存在账户冻结、监督者离职、单季亏损和现金缓冲下降。请使用下方冻结资料，预测未来24个自然月内是否会发生target定义的完整撤销全部风险警示。把担保合同是否生效、诉讼终局、责任解除、资金占用或新增内控问题和交易所审核逐层分析；董事会催收和诉讼计划本身不算整改完成。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST摩登 (002656, SZSE)
- 信息截止 / As of: 2020-01-13
- 预测窗口结束 / Window end: 2022-01-13
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来24个自然月内，证券交易所审核同意撤销公司股票交易的全部退市风险警示和全部其他风险警示，且生效后的证券简称不再含ST或*ST、股票退出风险警示板。仅提交或获董事会通过申请、占款或担保已清偿、审计意见改善、撤销一项叠加警示但仍保留任一风险警示、*ST降为ST、暂停上市后恢复或最终退市均不计为事件

#### 判定条件 / Criteria

- `full_risk_warning_removal_count_24m >= 1` — 窗口内经交易所审核同意并生效的完整撤销全部风险警示至少一次

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
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 结果日期 / Resolved at: 2022-01-13

### 实际结果 / Realized outcome

- **observations**:
  - **full_risk_warning_removal_count_24m**: 0
  - **full_risk_warning_removed_by_window_end**: 0
  - **partial_only_removal_count_24m**: 0
  - **calendar_days_to_full_removal_or_zero**: 0
  - **risk_warning_present_at_window_end**: 1
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
- **suite**: a_share_st_remediation_v1
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
  - **row_policy**: stock_code=002656.XSHE; if_adjusted=0 for 2019q3 PIT fundamentals; risk-warning events/status checked through the fixed 24-month window
  - **st_cause_taxonomy**: non_operating_governance/illegal_guarantees
  - **matching_group**: first-risk-warning-day-full-removal-24m-v1
  - **matching_role**: no_event_hard_control
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice_exchange_mirror**: 09d3b381eac2bfecf8ef504fb3203b2f3dadfe0f0b676e072d67bcc9885e66e2
    - **2019_third_quarter_report_exchange_mirror**: d7f82607f662f6cc1cf66c974f08ad11fd83e5eed98b1fb776697e3707976e96
  - **news_evidence_policy**: Contemporaneous reporting may provide management-turnover and strategy context; filings remain authority for the guarantee exposure and PIT financials.
  - **outcome_contract**: Only an exchange-approved removal of every ST/*ST warning that becomes effective inside the 24-calendar-month window counts. An application, remediation, *ST-to-ST downgrade, continued ST status, or delisting does not.
  - **status_source_sha256**:
    - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
    - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
  - **leakage_guard**: All removal approvals, later ST transitions, restructurings, delistings and post-as_of remediation facts remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: rqdata_risk_warning_status_crosscheck
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2020-01-13/2022-01-13
    - **full_removal_within_window**: false
    - **partial_only_removal_count_24m**: 0
    - **later_context_not_counted**: 截至2022-01-13窗口末仍为ST摩登，违规担保及资金占用等事项未形成交易所批准的完整摘帽。

</details>

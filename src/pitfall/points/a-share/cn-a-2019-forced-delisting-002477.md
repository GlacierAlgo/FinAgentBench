# cn-a-2019-forced-delisting-002477

## Question

你处在2019-04-26收盘后的信息环境。*ST雏鹰的2019年一季末归母权益已转负，收入不足营业成本，流动负债149亿元，债务逾期、诉讼和冻结广泛存在，年报审计无法表示意见；公司仍寄望债务重组、剥离资产和猪周期改善。请使用下方冻结资料，预测未来60个自然月内是否会发生target定义的交易所强制终止上市决定。除财务与审计路径外，也要考虑市场价格、披露和重大违法等相互竞争的退市路径。 给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST雏鹰 (002477, SZSE)
- 信息截止 / As of: 2019-04-26
- 预测窗口结束 / Window end: 2024-04-26
- 目标事件 / Target: `exchange_decided_forced_delisting_60m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来60个自然月内，证券交易所作出强制终止公司股票上市的最终决定。财务类、交易类、重大违法类以及规范类强制退市均计入；仅风险提示、继续ST或*ST、停牌或暂停上市、公司申请或自愿退市、重整或重组、进入退市整理期但缺少交易所终止上市决定、以及窗口结束后才作出的决定均不计入

#### 判定条件 / Criteria

- `exchange_forced_delisting_decision_count_60m >= 1` — 窗口内交易所作出强制终止上市最终决定至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 雏鹰农牧2019年一季报：归母权益转负、收入不抵成本且现金高度受限

- Evidence ID: `q1-negative-equity-and-cash-conversion-gap`
- 发布日期 / Published: 2019-04-25
- 来源 / Source: 巨潮资讯法定季度报告
- URL: https://static.cninfo.com.cn/finalpage/2019-04-25/1206091341.PDF

2019年一季度营业收入3.9641亿元，而营业成本8.2117亿元、财务费用2.2941亿元、归母净亏损11.0304亿元；经营活动现金流净额仍为正4,662.62万元。期末货币资金4.2025亿元，但现金及现金等价物仅4,185.95万元；流动负债149.1044亿元、负债合计181.9921亿元，归母所有者权益已降至-1,043.02万元。正经营现金流不能抵消负毛利、巨额短债、融资费用和负净资产。

### 雏鹰农牧披露新增诉讼与大范围债务逾期

- Evidence ID: `overdue-debt-litigation-and-frozen-assets`
- 发布日期 / Published: 2019-04-13
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2019-04-13/1206016281.PDF

公司在被证监会立案调查期间自查披露大量诉讼、仲裁和债务逾期。逾期清单覆盖银行短期借款、信托贷款、融资租赁、保理和其他融资，包括单笔5.99亿元个人借款以及多笔亿元级金融机构债务；部分案件已导致资产查封或诉讼。债务分散、交叉违约与司法保全提高了重组协调难度。

### 雏鹰农牧首次*ST：审计无法表示意见并提示持续经营危机

- Evidence ID: `first-delisting-risk-warning-audit-disclaimer`
- 发布日期 / Published: 2019-04-25
- 来源 / Source: 巨潮资讯法定风险警示公告
- URL: https://static.cninfo.com.cn/finalpage/2019-04-25/1206091348.PDF

公司因2018年度财务报告被出具无法表示意见，自2019年4月26日起实施退市风险警示并更名*ST雏鹰。审计基础事项包括无法偿付到期债务、众多司法诉讼、银行账户和资产冻结、生产经营受损，以及管理层未能提供改善持续经营能力计划的充分证据。董事会提出剥离非主业资产、债务重组、诉讼应对和聚焦养猪，但尚无已完成的债务削减、资本注入或审计证据。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `exchange_decided_forced_delisting_60m`
- 结果日期 / Resolved at: 2019-08-20

### 实际结果 / Realized outcome

- **observations**:
  - **exchange_forced_delisting_decision_count_60m**: 1
  - **major_illegality_route_decision_count_60m**: 0
  - **financial_route_decision_count_60m**: 0
  - **transaction_route_decision_count_60m**: 1
  - **calendar_days_to_exchange_decision_or_zero**: 115
  - **survived_fixed_window_without_forced_delisting**: 0
  - **first_risk_warning_day_verified**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `q1-negative-equity-and-cash-conversion-gap`
- `overdue-debt-litigation-and-frozen-assets`
- `first-delisting-risk-warning-audit-disclaimer`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_forced_delisting_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002477.XSHE
  - **ticker**: 002477
  - **name_as_of**: *ST雏鹰
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-04-26
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - is_st
    - special_treatment_info
  - **row_policy**: stock_code=002477.XSHE; quarter=2019q1; info_date=2019-04-25; if_adjusted=0; first *ST day and later status read from special_treatment_info
  - **st_cause_taxonomy**: operating_financial_and_market/audit_disclaimer+negative_equity+debt_overdue
  - **matching_group**: first-risk-warning-day-forced-delisting-60m-v1
  - **matching_role**: event
  - **first_warning_start_contract**: The snapshot is the first trading day on which ST or *ST is active, not merely the prior announcement date.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **q1_report**: 4a723a4face2b392c512a6fb2638c2e0535ed10298e8a1cc42cd1f06fb19a229
    - **overdue_notice**: ae5d31291bbee2f7cb9af106724aa906ff82b9ad6dc0196c39d2aa69a4edc0c0
    - **st_notice**: 74a1049ef6c1d893342c39df87b998dc60b0fe1c7bce109ea584bec9d268a6a3
  - **news_evidence_policy**: Only contemporaneous public information no later than as_of may enter the corpus; official filings and read-only RQData remain point-in-time and label authority.
  - **outcome_contract**: Only a final securities-exchange decision to forcibly terminate the listing inside the fixed 60-calendar-month window counts. Risk warnings, suspension, an issuer application, voluntary delisting, restructuring, a delisting-risk notice, entry into a delisting period without the decision, or a decision after the window do not count.
  - **status_source_sha256**:
    - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
    - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
  - **leakage_guard**: All exchange decisions, later delisting routes, later warning transitions, restructurings, penalties and post-as_of financial results remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_exchange_forced_delisting_decision
    - **title**: 雏鹰农牧关于公司股票终止上市的公告
    - **decision_date**: 2019-08-19
    - **published_at**: 2019-08-20
    - **url**: https://static.cninfo.com.cn/finalpage/2019-08-20/1206546611.PDF
    - **sha256**: fe2c1f75ef89901c3af70ba3660d39687137ce7522f863f58d1a1369d2ecd5b7
    - **delisting_route**: transaction
    - **decision_reason**: 公司股票连续20个交易日每日收盘价低于1元面值，触及交易类终止上市。
    - **is_exchange_final_decision**: true
    - **forced_not_voluntary**: true
    - **inside_60_calendar_month_window**: true
    - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
    - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **item 2**:
    - **type**: rqdata_forced_delisting_status_crosscheck
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2019-04-26/2024-04-26
    - **first_risk_warning_trading_day**: 2019-04-26
    - **forced_delisting_decision_within_window**: true
    - **survived_fixed_window**: false

</details>

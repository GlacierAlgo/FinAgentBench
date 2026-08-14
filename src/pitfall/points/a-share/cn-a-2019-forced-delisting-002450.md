# cn-a-2019-forced-delisting-002450

## Question

你处在2019-01-23收盘后的信息环境。ST康得新三个月前仍披露150亿元货币资金和22亿元前三季度利润，如今两期超短融已经实质违约、22个银行账户被冻结。请使用下方冻结资料，预测未来60个自然月内是否会发生target定义的交易所强制终止上市决定。请区分账面现金与可支配资金，分析违约和冻结能否修复、审计或监管核查升级、持续经营及多种强制退市路径；不要用尚未发生的调查结论或退市结果。 给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST康得新 (002450, SZSE)
- 信息截止 / As of: 2019-01-23
- 预测窗口结束 / Window end: 2024-01-23
- 目标事件 / Target: `exchange_decided_forced_delisting_60m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来60个自然月内，证券交易所作出强制终止公司股票上市的最终决定。财务类、交易类、重大违法类以及规范类强制退市均计入；仅风险提示、继续ST或*ST、停牌或暂停上市、公司申请或自愿退市、重整或重组、进入退市整理期但缺少交易所终止上市决定、以及窗口结束后才作出的决定均不计入

#### 判定条件 / Criteria

- `exchange_forced_delisting_decision_count_60m >= 1` — 窗口内交易所作出强制终止上市最终决定至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 康得新2018年三季报：150亿元账面现金与高融资成本并存

- Evidence ID: `q3-large-cash-and-financing-paradox`
- 发布日期 / Published: 2018-10-23
- 来源 / Source: 巨潮资讯法定季度报告
- URL: https://static.cninfo.com.cn/finalpage/2018-10-23/1205522221.PDF

截至2018年9月末，合并口径货币资金150.1353亿元、应收账款71.4510亿元、流动负债121.0236亿元、负债合计166.9339亿元、归母权益200.0600亿元。前三季度营业收入108.3475亿元、归母净利润22.0144亿元、经营活动现金流净额20.7367亿元；但利息费用5.5755亿元，显著高于利息收入1.9792亿元。公司在持有巨额现金的同时仍承担大量有息融资成本，账面现金数量不能独立证明到期可动用性。

### 康得新公告10.41亿元超短融本息实质违约

- Evidence ID: `first-scp-default-despite-reported-cash`
- 发布日期 / Published: 2019-01-16
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2019-01-16/1205773010.PDF

18康得新SCP001应于2019年1月15日兑付。公司公告称截至当日营业终了未能筹措足额偿付资金，10亿元本金及利息合计10.406849亿元不能按期足额偿付，已构成实质违约；解释为销售回款缓慢和资金周转暂时困难，并称生产经营正常。该事实与三个月前披露的150亿元货币资金形成强烈矛盾。

### 康得新首次实施ST：22个银行账户被冻结且两期超短融违约

- Evidence ID: `first-st-bank-account-freeze`
- 发布日期 / Published: 2019-01-22
- 来源 / Source: 巨潮资讯法定风险警示公告
- URL: https://static.cninfo.com.cn/finalpage/2019-01-22/1205786099.PDF

公司自2019年1月23日起实施其他风险警示并更名ST康得新。公司获悉22个银行账户被冻结，其中5个属于主要账户，暂未取得司法机关对应函件；公告同时确认2018年度第一、二期超短期融资券均已实质违约，并称计划依靠恢复授信、应收回款以及与债权人和法院协商解除冻结。主要账户冻结与连续公开债务违约说明流动性和资金控制问题已从异常信号转为现实约束。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `exchange_decided_forced_delisting_60m`
- 结果日期 / Resolved at: 2021-04-07

### 实际结果 / Realized outcome

- **observations**:
  - **exchange_forced_delisting_decision_count_60m**: 1
  - **major_illegality_route_decision_count_60m**: 1
  - **financial_route_decision_count_60m**: 0
  - **transaction_route_decision_count_60m**: 0
  - **calendar_days_to_exchange_decision_or_zero**: 804
  - **survived_fixed_window_without_forced_delisting**: 0
  - **first_risk_warning_day_verified**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `q3-large-cash-and-financing-paradox`
- `first-scp-default-despite-reported-cash`
- `first-st-bank-account-freeze`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_forced_delisting_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002450.XSHE
  - **ticker**: 002450
  - **name_as_of**: ST康得新
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-01-23
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
  - **row_policy**: stock_code=002450.XSHE; quarter=2018q3; info_date=2018-10-23; if_adjusted=0; first ST day and later status read from special_treatment_info
  - **st_cause_taxonomy**: mixed_financial_and_illegality/public_debt_default+bank_account_freeze+financial_fraud
  - **matching_group**: first-risk-warning-day-forced-delisting-60m-v1
  - **matching_role**: event
  - **first_warning_start_contract**: The snapshot is the first trading day on which ST or *ST is active, not merely the prior announcement date.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **q3_report**: b3d7c478a1f19f71f45c811c011407e7cb738779695f94b8adbc2fde6e1385a8
    - **first_default**: fd7fb5854b3175b6c3b1e41365cbd493aa9a8861afd20b95b2ebb4eddfd71572
    - **st_notice**: 0ac33745287723a6314858d778ea8a52fcef3fea501d80e69385df9d9a71c552
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
    - **title**: 康得新关于公司股票终止上市的公告
    - **decision_date**: 2021-04-06
    - **published_at**: 2021-04-07
    - **url**: https://static.cninfo.com.cn/finalpage/2021-04-07/1209643701.PDF
    - **sha256**: 58bad65dae8d519b570bb2a44fe70a7853c6df3fab88ce33490b64a0444a4985
    - **delisting_route**: major_illegality
    - **decision_reason**: 证监会认定2015至2018年年报虚假记载，追溯后连续亏损；交易所决定实施重大违法强制退市。
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
    - **window**: 2019-01-23/2024-01-23
    - **first_risk_warning_trading_day**: 2019-01-23
    - **forced_delisting_decision_within_window**: true
    - **survived_fixed_window**: false

</details>

# cn-a-2018-forced-delisting-000939

## Question

你处在2018-07-02收盘后的信息环境。*ST凯迪因2017年报无法表示意见戴帽，年内待偿有息债务约150亿元，母子公司大量账户冻结，利润、减值和融资现金流均恶化；公司提出封闭运营、出售资产和多层重组。请使用下方冻结资料，预测未来60个自然月内是否会发生target定义的交易所强制终止上市决定。重点判断重组方案的执行依赖、持续经营、下一年度审计和净资产修复，而不是把重组口号直接当作存续。 给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST凯迪 (000939, SZSE)
- 信息截止 / As of: 2018-07-02
- 预测窗口结束 / Window end: 2023-07-02
- 目标事件 / Target: `exchange_decided_forced_delisting_60m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来60个自然月内，证券交易所作出强制终止公司股票上市的最终决定。财务类、交易类、重大违法类以及规范类强制退市均计入；仅风险提示、继续ST或*ST、停牌或暂停上市、公司申请或自愿退市、重整或重组、进入退市整理期但缺少交易所终止上市决定、以及窗口结束后才作出的决定均不计入

#### 判定条件 / Criteria

- `exchange_forced_delisting_decision_count_60m >= 1` — 窗口内交易所作出强制终止上市最终决定至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 凯迪生态2017年报：无法表示意见、巨额亏损与2018年集中兑付

- Evidence ID: `annual-disclaimer-debt-and-cash-burn`
- 发布日期 / Published: 2018-06-29
- 来源 / Source: 巨潮资讯法定年度报告
- URL: https://static.cninfo.com.cn/finalpage/2018-06-29/1205105058.PDF

2017年末货币资金24.5264亿元、应收账款27.2310亿元、其他应收款23.5586亿元、存货30.8231亿元，流动负债160.1837亿元、负债合计278.3560亿元、归母权益94.844亿元。全年营业收入54.4574亿元、归母净亏损23.8051亿元、财务费用14.5789亿元、资产减值损失21.1732亿元；投资与筹资现金流净额分别为-21.7617亿元和-32.93亿元。审计师出具无法表示意见，并指出2018年到期有息债务本息147.53亿元、持续经营存在重大不确定性。

### 凯迪生态公告母子公司47个账户被冻结

- Evidence ID: `bank-accounts-frozen-after-default`
- 发布日期 / Published: 2018-05-24
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2018-05-24/1204998051.PDF

因中票违约引发信用风险和债权人保全，公司母公司9个账户被冻结，冻结申请金额10.7580亿元，而被冻结账户实际余额仅2,444.25万元；24家子公司另有38个账户被冻结，冻结申请金额14.5596亿元、实际余额2,283.85万元。账户体系广泛冻结且余额远低于债权主张，限制电厂燃料采购、工资与日常运营。

### 凯迪生态首次*ST：无法表示意见且一年内约150亿元债务待处理

- Evidence ID: `first-delisting-risk-warning-audit-disclaimer`
- 发布日期 / Published: 2018-06-29
- 来源 / Source: 巨潮资讯法定风险警示公告
- URL: https://static.cninfo.com.cn/finalpage/2018-06-29/1205105065.PDF

公司因2017年度财务报告被出具无法表示意见，自2018年7月2日起实施退市风险警示并更名*ST凯迪。董事会称将通过电厂封闭运营、债务重组、资产处置和引入第三方恢复经营；同时披露截至2018年5月有息债务本息余额超过240亿元，一年内到期约150亿元。方案依赖多方债权人、资产买方和新投资者，尚不是已执行的资本补足或审计闭环。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `exchange_decided_forced_delisting_60m`
- 结果日期 / Resolved at: 2020-10-29

### 实际结果 / Realized outcome

- **observations**:
  - **exchange_forced_delisting_decision_count_60m**: 1
  - **major_illegality_route_decision_count_60m**: 0
  - **financial_route_decision_count_60m**: 1
  - **transaction_route_decision_count_60m**: 0
  - **calendar_days_to_exchange_decision_or_zero**: 849
  - **survived_fixed_window_without_forced_delisting**: 0
  - **first_risk_warning_day_verified**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `annual-disclaimer-debt-and-cash-burn`
- `bank-accounts-frozen-after-default`
- `first-delisting-risk-warning-audit-disclaimer`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_forced_delisting_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000939.XSHE
  - **ticker**: 000939
  - **name_as_of**: *ST凯迪
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2018-07-02
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
  - **row_policy**: stock_code=000939.XSHE; quarter=2017q4; info_date=2018-06-29; if_adjusted=0; first *ST day and later status read from special_treatment_info
  - **st_cause_taxonomy**: operating_and_financial/audit_disclaimer+debt_default+bank_account_freeze
  - **matching_group**: first-risk-warning-day-forced-delisting-60m-v1
  - **matching_role**: event
  - **first_warning_start_contract**: The snapshot is the first trading day on which ST or *ST is active, not merely the prior announcement date.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **annual_report**: e75c8ddfe0aa98328eb3c09be8b7462dfaa2cfb4cd277402055a641ebe5436dc
    - **account_freeze**: 11954c8cd0e1618acc3b07592d0e32c10cc4b0fd088141951624e5e5853d8daa
    - **st_notice**: b77f850493a03903386ffd7544c9888c2beb9961b355cfb3478056ea7048b7c7
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
    - **title**: 凯迪生态关于公司股票终止上市的公告
    - **decision_date**: 2020-10-28
    - **published_at**: 2020-10-29
    - **url**: https://static.cninfo.com.cn/finalpage/2020-10-29/1208638221.PDF
    - **sha256**: 83b124bef2cd3062c50a6bc07a93ffea5ce15dc50af32cfb9d095c1b978ce79c
    - **delisting_route**: financial
    - **decision_reason**: 暂停上市后首个年报继续显示净利润和净资产为负，财务报告再次无法表示意见，触及财务类终止上市。
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
    - **window**: 2018-07-02/2023-07-02
    - **first_risk_warning_trading_day**: 2018-07-02
    - **forced_delisting_decision_within_window**: true
    - **survived_fixed_window**: false

</details>

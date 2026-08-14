# cn-a-2019-forced-delisting-600781

## Question

你处在2019-09-03收盘后的信息环境。ST辅仁因16.35625亿元控股股东占用和违规担保戴帽，此前公司在合并报表显示大量现金和利润时却无法支付约6,274万元分红，半年报现金又骤降91.88%。请使用下方冻结资料，预测未来60个自然月内是否会发生target定义的交易所强制终止上市决定。必须区分合并利润、母公司可支配现金、关联应收回收、控制人股权冻结、债务逾期、调查与下一年审计风险。 给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST辅仁 (600781, SSE)
- 信息截止 / As of: 2019-09-03
- 预测窗口结束 / Window end: 2024-09-03
- 目标事件 / Target: `exchange_decided_forced_delisting_60m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来60个自然月内，证券交易所作出强制终止公司股票上市的最终决定。财务类、交易类、重大违法类以及规范类强制退市均计入；仅风险提示、继续ST或*ST、停牌或暂停上市、公司申请或自愿退市、重整或重组、进入退市整理期但缺少交易所终止上市决定、以及窗口结束后才作出的决定均不计入

#### 判定条件 / Criteria

- `exchange_forced_delisting_decision_count_60m >= 1` — 窗口内交易所作出强制终止上市最终决定至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 辅仁药业实施其他风险警示公告：16.35625亿元占用、违规担保与控股股东全冻结

- Evidence ID: `st-notice-occupation-guarantee-and-freeze`
- 发布日期 / Published: 2019-08-31
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2019-08-31/1206870184.PDF

公司自2019年9月3日起变更为ST辅仁。公告称向控股股东及关联方提供借款余额16.35625亿元，未经批准提供连带责任担保1.4亿元、剩余担保6,202万元，预计一个月内无法解决。控股股东持有的45.03%上市公司股份已100%冻结并多次轮候冻结；公司存在债务逾期、流动性不足、产能和销售受影响、证监会调查，以及2018年度现金分红仍未实施。

### 辅仁药业2019年半年报：利润仍正但现金骤降91.88%、其他应收款暴增

- Evidence ID: `h1-cash-collapse-and-related-receivables`
- 发布日期 / Published: 2019-08-31
- 来源 / Source: 巨潮资讯法定半年度报告
- URL: https://static.cninfo.com.cn/finalpage/2019-08-31/1206870186.PDF

2019年上半年营业收入27.6896亿元、归母净利润3.9900亿元、扣非归母净利润3.6213亿元、经营活动现金流净额2.5226亿元；但期末货币资金仅1.3445亿元，较年初16.5636亿元下降91.88%，其中1.2771亿元受限。其他应收款从1,742.68万元增至18.3482亿元，主要系关联方借款；短期借款23.8741亿元。母公司货币资金仅35.57万元。账面利润并未形成可支配清偿能力。

### 戴帽前调查报道：18亿元一季报现金却拿不出6,000万元分红

- Evidence ID: `pre-st-dividend-failure-investigation`
- 发布日期 / Published: 2019-08-06
- 来源 / Source: 中国证券报·中证网转载每日经济新闻
- URL: https://www.cs.com.cn/ssgs/gsxw/201908/t20190806_5975027.html

报道指出公司一季报显示约18.16亿元货币资金，却在7月无法按期实施约6,000万元现金分红，随后暴露资金受限、债务和控制人体系问题。该极端现金可得性矛盾在正式戴帽前已经公开，是判断关联应收可回收、母公司支付能力和治理可信度的重要先验，而不是需要未来信息才能发现的线索。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `exchange_decided_forced_delisting_60m`
- 结果日期 / Resolved at: 2023-05-23

### 实际结果 / Realized outcome

- **observations**:
  - **exchange_forced_delisting_decision_count_60m**: 1
  - **major_illegality_route_decision_count_60m**: 0
  - **financial_route_decision_count_60m**: 1
  - **transaction_route_decision_count_60m**: 0
  - **calendar_days_to_exchange_decision_or_zero**: 1357
  - **survived_fixed_window_without_forced_delisting**: 0
  - **first_risk_warning_day_verified**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-occupation-guarantee-and-freeze`
- `h1-cash-collapse-and-related-receivables`
- `pre-st-dividend-failure-investigation`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_forced_delisting_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600781.XSHG
  - **ticker**: 600781
  - **name_as_of**: ST辅仁
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-09-03
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
  - **row_policy**: stock_code=600781.XSHG; quarter=2019q2; info_date=2019-08-31; if_adjusted=0; first risk-warning trading day=2019-09-03
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation+illegal_guarantees+liquidity_crisis
  - **matching_group**: first-risk-warning-day-forced-delisting-60m-v1
  - **matching_role**: event
  - **first_warning_start_contract**: The snapshot is the first trading day on which ST or *ST is active, not merely the prior announcement date.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: ec3e34a584c40558e80f65e6023dd85ad238a1b1cf6163a9dd09dc3e2130fc51
    - **h1_report**: cc631eb09efd9844a615fbc7b2daae85ad238a1b1cf6163a9dd09dc3e2130fc51
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
    - **title**: 辅仁药业关于收到股票终止上市决定的公告
    - **decision_date**: 2023-05-22
    - **published_at**: 2023-05-23
    - **url**: https://static.cninfo.com.cn/finalpage/2023-05-23/1216874065.PDF
    - **sha256**: c73497c931485263b0a3153c81981cdffb0eb2bd9fc6fde40ff1bd3d7049cf8f
    - **delisting_route**: financial
    - **decision_reason**: 退市风险警示后年报继续显示期末净资产为负且审计无法表示意见，触及财务类终止上市。
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
    - **window**: 2019-09-03/2024-09-03
    - **first_risk_warning_trading_day**: 2019-09-03
    - **forced_delisting_decision_within_window**: true
    - **survived_fixed_window**: false

</details>

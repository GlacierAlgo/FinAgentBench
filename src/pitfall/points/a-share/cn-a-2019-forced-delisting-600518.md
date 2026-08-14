# cn-a-2019-forced-delisting-600518

## Question

你处在2019-05-21收盘后的信息环境。ST康美因88.79亿元关联资金被用于购买公司股票、治理和内控重大缺陷而戴帽，年报刚发生巨额差错更正，现金、存货与短债之间存在显著矛盾。请使用下方冻结资料，预测未来60个自然月内是否会发生target定义的交易所强制终止上市决定。请比较处罚或审计升级、债务与持续经营风险、可执行重整和资本补足、主营造血能力及各种强制退市口径；不要把严重造假自动等同于窗口内必然退市。 给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST康美 (600518, SSE)
- 信息截止 / As of: 2019-05-21
- 预测窗口结束 / Window end: 2024-05-21
- 目标事件 / Target: `exchange_decided_forced_delisting_60m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来60个自然月内，证券交易所作出强制终止公司股票上市的最终决定。财务类、交易类、重大违法类以及规范类强制退市均计入；仅风险提示、继续ST或*ST、停牌或暂停上市、公司申请或自愿退市、重整或重组、进入退市整理期但缺少交易所终止上市决定、以及窗口结束后才作出的决定均不计入

#### 判定条件 / Criteria

- `exchange_forced_delisting_decision_count_60m >= 1` — 窗口内交易所作出强制终止上市最终决定至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 康美药业实施其他风险警示公告：88.79亿元关联资金用于购买公司股票

- Evidence ID: `st-notice-8.879b-related-fund-flow`
- 发布日期 / Published: 2019-05-18
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2019-05-18/1206283586.PDF

公司自2019年5月21日起变更为ST康美。公告称公司与关联公司存在88.79亿元资金往来，该资金被关联公司用于购买公司股票，触及投资者难以判断公司前景、权益可能受损的情形。公司承认治理、资金管理和关联交易内控存在重大缺陷，只表示督促关联方多途径解决并整改，没有给出锁定资金、清偿时间表或审计验证。

### 康美药业2019年一季报：更正后现金骤降、巨额存货与短债

- Evidence ID: `q1-cash-collapse-inventory-and-short-debt`
- 发布日期 / Published: 2019-04-30
- 来源 / Source: 巨潮资讯法定季度报告
- URL: https://static.cninfo.com.cn/finalpage/2019-04-30/1206168279.PDF

更正口径下，2019年一季度营业收入49.0164亿元、归母净利润2.2088亿元、扣非归母净利润1.7091亿元、经营活动现金流净额6.7395亿元。期末货币资金10.4801亿元，较年初减少43.02%；存货336.6041亿元、短期借款149.40亿元、流动负债249.7790亿元、总负债452.7493亿元。筹资现金流净额-12.9980亿元。正经营现金流远小于资金占用与融资规模，且报表刚经历巨额差错更正。

### 中证网戴帽报道：88.79亿元资金往来直接触发风险警示

- Evidence ID: `contemporaneous-st-report`
- 发布日期 / Published: 2019-05-18
- 来源 / Source: 中国证券报·中证网
- URL: https://www.cs.com.cn/ssgs/gsxw/201905/t20190518_5950494.html

同时点报道确认公司将于5月21日起被实施其他风险警示，原因是88.79亿元关联资金被用于购买公司股票并使投资者难以判断前景。新闻没有提供已经到账的清偿资源或交易所撤销意见，因此只用于交叉核验市场当时可见的信息，不能支持“很快摘帽”的结论。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `exchange_decided_forced_delisting_60m`
- 结果日期 / Resolved at: 2024-05-21

### 实际结果 / Realized outcome

- **observations**:
  - **exchange_forced_delisting_decision_count_60m**: 0
  - **major_illegality_route_decision_count_60m**: 0
  - **financial_route_decision_count_60m**: 0
  - **transaction_route_decision_count_60m**: 0
  - **calendar_days_to_exchange_decision_or_zero**: 0
  - **survived_fixed_window_without_forced_delisting**: 1
  - **first_risk_warning_day_verified**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-8.879b-related-fund-flow`
- `q1-cash-collapse-inventory-and-short-debt`
- `contemporaneous-st-report`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_forced_delisting_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600518.XSHG
  - **ticker**: 600518
  - **name_as_of**: ST康美
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-05-21
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
  - **row_policy**: stock_code=600518.XSHG; quarter=2019q1; info_date=2019-04-30; if_adjusted=0; first risk-warning trading day=2019-05-21
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_flow+internal_control_material_weakness
  - **matching_group**: first-risk-warning-day-forced-delisting-60m-v1
  - **matching_role**: no_event_hard_control
  - **first_warning_start_contract**: The snapshot is the first trading day on which ST or *ST is active, not merely the prior announcement date.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: 0dbe732b03eb90ba8cd5dabc9757b42700f774d2ad6fb9195777119a249f8172
    - **q1_report**: 684b1c371ca5e2f564b638ad5cbdfd9bd72ae0a36cc041d1bac076475612c402
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
    - **type**: rqdata_forced_delisting_status_crosscheck
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2019-05-21/2024-05-21
    - **first_risk_warning_trading_day**: 2019-05-21
    - **forced_delisting_decision_within_window**: false
    - **survived_fixed_window**: true

</details>

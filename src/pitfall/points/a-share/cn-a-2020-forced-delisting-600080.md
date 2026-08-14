# cn-a-2020-forced-delisting-600080

## Question

你处在2020-06-02收盘后的信息环境。ST金花因控股股东占用资金及存单质押未解决而戴帽，尚未归还1.6772亿元，控股股东承诺通过股份转让归还；医药主业和净资产仍在。请使用下方冻结资料，预测未来60个自然月内是否会发生target定义的交易所强制终止上市决定。重点检验清偿可执行性、审计与内控后续验证、公司自身现金流、控制权方案以及财务、重大违法和交易价格类退市路径。 给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST金花 (600080, SSE)
- 信息截止 / As of: 2020-06-02
- 预测窗口结束 / Window end: 2025-06-02
- 目标事件 / Target: `exchange_decided_forced_delisting_60m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来60个自然月内，证券交易所作出强制终止公司股票上市的最终决定。财务类、交易类、重大违法类以及规范类强制退市均计入；仅风险提示、继续ST或*ST、停牌或暂停上市、公司申请或自愿退市、重整或重组、进入退市整理期但缺少交易所终止上市决定、以及窗口结束后才作出的决定均不计入

#### 判定条件 / Criteria

- `exchange_forced_delisting_decision_count_60m >= 1` — 窗口内交易所作出强制终止上市最终决定至少一次

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 金花股份实施其他风险警示公告：尚有1.6772亿元占用与存单质押未解

- Evidence ID: `st-notice-occupation-and-pledged-deposit`
- 发布日期 / Published: 2020-06-01
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-06-01/1207878970.PDF

公司自2020年6月2日起变更为ST金花。2019年控股股东及关联方资金占用发生额2.7777亿元、存单质押6,800万元，合计3.4577亿元，占最近一期经审计净资产20.15%；截至公告日仍有1.6772亿元未归还或解除，占净资产9.78%。控股股东承诺转让所持股份，并在6月30日前归还资金及占用费，但披露时尚未完成。

### 金花股份2020年一季报：低有息负债与疫情下收入现金流承压

- Evidence ID: `q1-low-leverage-but-pandemic-pressure`
- 发布日期 / Published: 2020-04-30
- 来源 / Source: 巨潮资讯法定季度报告
- URL: https://static.cninfo.com.cn/finalpage/2020-04-30/1207688572.PDF

2020年一季度营业收入1.0778亿元，同比下降28.09%；归母净利润-104.34万元，扣非归母净利润-270.96万元，经营活动现金流净额-1,458.22万元。期末货币资金2.4680亿元、归母净资产17.1412亿元，合并资产负债表没有短期借款，流动负债1.6223亿元。低杠杆和账面现金使问题可能可修复，但占用金额接近现金的68%，且现金是否自由可用需要结合存单质押判断。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `exchange_decided_forced_delisting_60m`
- 结果日期 / Resolved at: 2025-06-02

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

- `st-notice-occupation-and-pledged-deposit`
- `q1-low-leverage-but-pandemic-pressure`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_forced_delisting_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600080.XSHG
  - **ticker**: 600080
  - **name_as_of**: ST金花
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-06-02
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
  - **row_policy**: stock_code=600080.XSHG; quarter=2020q1; info_date=2020-04-30; if_adjusted=0; first risk-warning trading day=2020-06-02
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation+pledged_deposit
  - **matching_group**: first-risk-warning-day-forced-delisting-60m-v1
  - **matching_role**: no_event_hard_control
  - **first_warning_start_contract**: The snapshot is the first trading day on which ST or *ST is active, not merely the prior announcement date.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: 076582de2b46d70471f15ac8ab1d8cb96fb821375bf3098931bd817208960ba9
    - **q1_report**: 9da6aaa89af6b1b0c42787c6f495116ba4367220f0c7e2ff6d008c33c99bef1f
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
    - **window**: 2020-06-02/2025-06-02
    - **first_risk_warning_trading_day**: 2020-06-02
    - **forced_delisting_decision_within_window**: false
    - **survived_fixed_window**: true

</details>

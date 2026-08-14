# cn-a-2020-forced-delisting-000408

## Question

你处在2020-05-06收盘后的信息环境。*ST藏格因2019年报无法表示意见戴帽，审计材料暴露关联占用、以巨龙铜业股权抵债及抵债资产担保和持续经营不确定性，但钾肥主业仍有现金流和资产基础。请使用下方冻结资料，预测未来60个自然月内是否会发生target定义的交易所强制终止上市决定。分别评估下一年审计可验证性、占款清偿资源、抵债资产质量、债务和净资产、重整或控制权变化及交易所规则。 给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST藏格 (000408, SZSE)
- 信息截止 / As of: 2020-05-06
- 预测窗口结束 / Window end: 2025-05-06
- 目标事件 / Target: `exchange_decided_forced_delisting_60m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来60个自然月内，证券交易所作出强制终止公司股票上市的最终决定。财务类、交易类、重大违法类以及规范类强制退市均计入；仅风险提示、继续ST或*ST、停牌或暂停上市、公司申请或自愿退市、重整或重组、进入退市整理期但缺少交易所终止上市决定、以及窗口结束后才作出的决定均不计入

#### 判定条件 / Criteria

- `exchange_forced_delisting_decision_count_60m >= 1` — 窗口内交易所作出强制终止上市最终决定至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 藏格控股退市风险警示公告：2019年财报被出具无法表示意见

- Evidence ID: `star-st-notice-audit-disclaimer`
- 发布日期 / Published: 2020-04-30
- 来源 / Source: 深圳证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-04-30/1207687963.PDF

公司自2020年5月6日起变更为*ST藏格。直接触发条件是2019年度财务会计报告被中审众环出具无法表示意见。董事会提出自查关联资金、强化资产人员财务独立和内部审计，但仅是拟采取措施；若2020年度仍被出具否定或无法表示意见，当时规则下股票可能暂停上市。

### 藏格控股2019年审计报告：低现金、关联占用与巨龙铜业抵债资产风险

- Evidence ID: `audit-report-occupation-and-risky-equity-setoff`
- 发布日期 / Published: 2020-04-30
- 来源 / Source: 巨潮资讯法定审计报告
- URL: https://static.cninfo.com.cn/finalpage/2020-04-30/1207687966.PDF

2019年末货币资金8,209.96万元、应收账款10.6515亿元、其他应收款4.7458亿元，短期借款4.15亿元；营业收入20.6415亿元、归母净利润3.5952亿元、经营活动现金流净额2.7700亿元。附注披露控股股东相关直接占用余额2.6488亿元，并通过客户欠款形成间接占用；公司以25.9亿元受让巨龙铜业37%股权抵偿占款。该联营企业又为关联方约30亿元借款提供担保、存在逾期负债、停建停采和持续经营重大不确定性，说明“以资抵债”并非无风险现金回收。

### 藏格控股2020年一季报PIT财务：利润和经营现金流为正但现金较薄

- Evidence ID: `q1-profitable-operation-but-thin-cash`
- 发布日期 / Published: 2020-04-30
- 来源 / Source: 只读RQData点时财务记录（对应法定一季报）
- URL: https://static.cninfo.com.cn/finalpage/2020-04-30/1207687954.PDF

只读PIT记录显示2020年一季度营业收入2.7242亿元、归母净利润2,438.08万元、扣非归母净利润3,533.01万元、经营活动现金流净额1.1272亿元；期末货币资金6,857.37万元、短期借款2.95亿元、归母净资产78.6092亿元。经营仍能产生现金，但风险警示源于审计证据和治理，而不是单一季度是否盈利。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `exchange_decided_forced_delisting_60m`
- 结果日期 / Resolved at: 2025-05-06

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

- `star-st-notice-audit-disclaimer`
- `audit-report-occupation-and-risky-equity-setoff`
- `q1-profitable-operation-but-thin-cash`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_forced_delisting_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000408.XSHE
  - **ticker**: 000408
  - **name_as_of**: *ST藏格
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-05-06
  - **allowed_domains**:
    - cninfo.com.cn
    - szse.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - is_st
    - special_treatment_info
  - **row_policy**: stock_code=000408.XSHE; quarter=2020q1 and 2019q4; info_date=2020-04-30; if_adjusted=0; first risk-warning trading day=2020-05-06
  - **st_cause_taxonomy**: mixed_delisting_and_governance/audit_disclaimer+related_party_fund_occupation
  - **matching_group**: first-risk-warning-day-forced-delisting-60m-v1
  - **matching_role**: no_event_hard_control
  - **first_warning_start_contract**: The snapshot is the first trading day on which ST or *ST is active, not merely the prior announcement date.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: eef850276dc97754959ec1148d1909c36978a194951d2dc4e386371b5c2f3d06
    - **audit_report**: 1048a3e2adbd166c9dd05ea810d5bb0afb3adaaf949d38a454f180856b69ac69
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
    - **window**: 2020-05-06/2025-05-06
    - **first_risk_warning_trading_day**: 2020-05-06
    - **forced_delisting_decision_within_window**: false
    - **survived_fixed_window**: true

</details>

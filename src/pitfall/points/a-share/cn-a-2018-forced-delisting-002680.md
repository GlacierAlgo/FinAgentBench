# cn-a-2018-forced-delisting-002680

## Question

你处在2018-07-26收盘后的信息环境。ST长生最近一季仍盈利且净资产远高于负债，但药监核查已确认编造疫苗生产和检验记录，核心GMP证书被收回、所有产品暂停批签发并全面停产，多名高管无法履职。请使用下方冻结资料，预测未来60个自然月内是否会发生target定义的交易所强制终止上市决定。不要只套用资不抵债框架；应分别评估重大违法规则、许可与信誉不可逆性、公司剩余资产价值、治理修复和交易所裁量。 给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST长生 (002680, SZSE)
- 信息截止 / As of: 2018-07-26
- 预测窗口结束 / Window end: 2023-07-26
- 目标事件 / Target: `exchange_decided_forced_delisting_60m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来60个自然月内，证券交易所作出强制终止公司股票上市的最终决定。财务类、交易类、重大违法类以及规范类强制退市均计入；仅风险提示、继续ST或*ST、停牌或暂停上市、公司申请或自愿退市、重整或重组、进入退市整理期但缺少交易所终止上市决定、以及窗口结束后才作出的决定均不计入

#### 判定条件 / Criteria

- `exchange_forced_delisting_decision_count_60m >= 1` — 窗口内交易所作出强制终止上市最终决定至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 长生生物2018年一季报：利润高增且账面偿债能力充足

- Evidence ID: `q1-profitable-solvent-financial-snapshot`
- 发布日期 / Published: 2018-04-25
- 来源 / Source: 巨潮资讯法定季度报告
- URL: https://static.cninfo.com.cn/finalpage/2018-04-25/1204733785.PDF

2018年一季度营业收入3.4637亿元、归母净利润1.5725亿元、扣非净利润1.3734亿元、经营活动现金流净额8,738.05万元，同比分别增长54.05%、72.22%、96.05%和409.26%。期末货币资金8,267.83万元、应收账款8.7220亿元、流动负债5.7612亿元、负债合计6.5081亿元、归母权益约40.14亿元。静态财务报表呈现盈利、高权益和低负债，并没有典型资不抵债路径。

### 药监核查进展：企业编造狂犬疫苗生产与检验记录

- Evidence ID: `regulator-found-fabricated-production-records`
- 发布日期 / Published: 2018-07-23
- 来源 / Source: 巨潮资讯转载国家药监局核查结论的法定公告
- URL: https://static.cninfo.com.cn/finalpage/2018-07-23/1205221917.PDF

公司转述国家药监局现场核查进展：已经查明企业编造生产记录和产品检验记录、随意变更工艺参数和设备，严重违反药品管理法和GMP；监管要求收回GMP证书、停止狂犬疫苗生产，并对企业立案调查。公司称复产时间无法预计，停产将对生产经营产生较大影响。该风险不是普通周期波动，而是核心产品合规和经营许可基础受到破坏。

### 长生生物首次ST：所有产品暂停批签发并全面停产

- Evidence ID: `first-st-full-production-shutdown`
- 发布日期 / Published: 2018-07-25
- 来源 / Source: 巨潮资讯法定风险警示公告
- URL: https://static.cninfo.com.cn/finalpage/2018-07-25/1205226262.PDF

公司自2018年7月26日起实施其他风险警示并更名ST长生。公告称狂犬疫苗GMP证书已被收回、狂犬和百白破疫苗被责令停产、所有产品暂停批签发，公司又决定其他产品全面自主停产，复产时间不确定，生产经营受到严重影响；董事长等人员被公安机关带走审查。即使此前资产负债表健康，核心许可、质量信誉、治理层履职和现金流来源已同时承压。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `exchange_decided_forced_delisting_60m`
- 结果日期 / Resolved at: 2019-10-09

### 实际结果 / Realized outcome

- **observations**:
  - **exchange_forced_delisting_decision_count_60m**: 1
  - **major_illegality_route_decision_count_60m**: 1
  - **financial_route_decision_count_60m**: 0
  - **transaction_route_decision_count_60m**: 0
  - **calendar_days_to_exchange_decision_or_zero**: 439
  - **survived_fixed_window_without_forced_delisting**: 0
  - **first_risk_warning_day_verified**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `q1-profitable-solvent-financial-snapshot`
- `regulator-found-fabricated-production-records`
- `first-st-full-production-shutdown`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_forced_delisting_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002680.XSHE
  - **ticker**: 002680
  - **name_as_of**: ST长生
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2018-07-26
  - **allowed_domains**:
    - cninfo.com.cn
    - gov.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - is_st
    - special_treatment_info
  - **row_policy**: stock_code=002680.XSHE; quarter=2018q1; info_date=2018-04-25; if_adjusted=0; first ST day and later status read from special_treatment_info
  - **st_cause_taxonomy**: non_financial_catastrophe/product_safety+fabricated_production_records+license_shutdown
  - **matching_group**: first-risk-warning-day-forced-delisting-60m-v1
  - **matching_role**: event
  - **first_warning_start_contract**: The snapshot is the first trading day on which ST or *ST is active, not merely the prior announcement date.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **q1_report**: 3b5618ad29960cdf496526d29153f1b85f21a9a162631cb390a838236471df20
    - **investigation_progress**: d338d836356f0625a7078da1480049c1429860b7f50afef51ee73115e538b54e
    - **st_notice**: e1b9d95bcac5dc9a5b3321f97bc5b1856fdcfe497f240bc2464f0c603668a10a
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
    - **title**: 长生生物关于公司股票终止上市的公告
    - **decision_date**: 2019-10-08
    - **published_at**: 2019-10-09
    - **url**: https://static.cninfo.com.cn/finalpage/2019-10-09/1206967384.PDF
    - **sha256**: f252c4ebad79e80a2ffeeb27fd2795d1e7812d00021fbb89bb08fb025aa1911a
    - **delisting_route**: major_illegality
    - **decision_reason**: 公司触及重大违法强制退市情形，交易所在暂停上市后作出终止上市决定。
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
    - **window**: 2018-07-26/2023-07-26
    - **first_risk_warning_trading_day**: 2018-07-26
    - **forced_delisting_decision_within_window**: true
    - **survived_fixed_window**: false

</details>

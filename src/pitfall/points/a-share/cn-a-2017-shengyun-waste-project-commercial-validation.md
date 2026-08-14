# cn-a-2017-shengyun-waste-project-commercial-validation

## Question

你处在2017-04-27收盘后的信息环境。盛运环保称已形成垃圾焚烧发电设计、设备、建设、投资和运营全产业链，多个项目处于点火试投产、二期扩建、开工或前期准备，但BOT/PPP扩张需要长期资本且基线经营现金为负。请使用下方冻结资料，沿融资、项目建设、投产、收入与毛利、应收和工程资产、现金、短债、权益与审计链条，预测项目组合能否在2018财年达到target定义的商业兑现事件。该标签不证明任何单个项目导致公司结果，也不评价股价。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 盛运环保 (300090, SZSE)
- 信息截止 / As of: 2017-04-27
- 预测窗口结束 / Window end: 2019-05-31
- 目标事件 / Target: `waste_project_portfolio_commercial_validation`
- 判定定义 / Definition: 垃圾焚烧项目组合的公司层面商业兑现事件而非单个项目因果证明：2018财年同时满足收入增长、毛利、盈利、经营现金、短债覆盖、权益保全和审计质量七项条件。收入CAGR=(2018收入/2016收入)^(1/2)-1；毛利率=(收入-营业成本)/收入；短债覆盖=期末货币资金/(短期借款+一年内到期非流动负债)；权益保全=2018归母权益/2016归母权益；标准无保留审计记1，其余记0。

#### 判定条件 / Criteria

- `revenue_cagr_baseline_to_outcome >= 0.15` — 2016年至2018年营业收入复合年增长率不低于15%
- `gross_margin_outcome >= 0.2` — 2018年综合毛利率不低于20%
- `net_profit_outcome > 0` — 2018年归母净利润为正
- `operating_cash_flow_outcome > 0` — 2018年经营活动产生的现金流量净额为正
- `cash_to_short_term_interest_bearing_debt_outcome >= 0.5` — 2018年末货币资金覆盖至少50%的短期借款和一年内到期非流动负债
- `equity_retention_baseline_to_outcome >= 0.8` — 2018年末归母权益至少保留2016年末的80%
- `standard_unqualified_audit_flag_outcome >= 1` — 2018年财务报表审计意见为标准无保留意见

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 盛运环保2016年年报：BOT/PPP项目梯队与资本合作模式

- Evidence ID: `annual-project-pipeline-and-capital-model`
- 发布日期 / Published: 2017-04-27
- 来源 / Source: 盛运环保法定年度报告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2017-04-27/1203405116.PDF

年报称公司形成生活垃圾焚烧发电总体设计、设备制造、施工总承包、投资与运营的一体化模式。2016年有8个项目由建设转入点火试投产，6个项目开始二期扩建，12个项目开工建设，另有12个拟开工项目进入前期准备。公司与多类金融和产业资本合作设立产业基金、并购基金，投向PPP、BOT、BOO和EPC项目。年报也提示BOT项目审批和前期周期长、建设及运营存在环保风险、项目竞争可能压低垃圾处置费。这是一条需要从融资一直验证到投产、回款和偿债的项目链，而不是签约数量题。

### 盛运环保2016年年报：运营项目、技术设备与扣非利润

- Evidence ID: `annual-operating-substance-and-profit-quality`
- 发布日期 / Published: 2017-04-27
- 来源 / Source: 盛运环保法定年度报告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2017-04-27/1203405116.PDF

公司披露2016年推进垃圾焚烧、固废、医废、餐厨垃圾和生物质热电业务，自主研制500吨/日生活垃圾机械焚烧系统。全年营业收入1,572,382,068.00元、归母净利润119,081,512.58元，但扣除非经常性损益后的归母净利润为-2,635,400元；环境治理-固废治理收入941,625,914.91元，垃圾焚烧及发电收入180,623,441.09元。利润口径与项目数量并不自动代表现金型商业兑现。

### 盛运环保2016年PIT项目资产负债链：在建工程、现金与债务

- Evidence ID: `annual-pit-project-balance-sheet`
- 发布日期 / Published: 2017-04-27
- 来源 / Source: 盛运环保法定年度报告及只读RQData点时记录
- URL: https://static.cninfo.com.cn/finalpage/2017-04-27/1203405093.PDF

2016年营业成本1,046,923,493.36元，经营活动现金流净额-630,203,468.58元，购建固定资产等支付现金795,535,675.53元。年末货币资金2,089,370,082.84元，应收账款净额996,397,749.08元，其他应收款778,924,083.48元，在建工程1,838,214,258.82元；短期借款1,199,775,000.00元，一年内到期非流动负债45,000,000.00元，长期借款977,799,071.72元，应付债券998,006,720.43元，归母权益5,175,475,280.89元。点时口径为300090.XSHE、2016q4、if_adjusted=0、最早info_date=2017-04-27。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `waste_project_portfolio_commercial_validation`
- 结果日期 / Resolved at: 2018-12-31
- 可观察日期 / Observed at: 2019-04-30

### 实际结果 / Realized outcome

- **observations**:
  - **revenue_baseline**: 1572382068.0
  - **revenue_outcome**: 515475081.42
  - **operating_cost_outcome**: 507321747.95
  - **net_profit_outcome**: -3112849776.06
  - **operating_cash_flow_outcome**: 546986584.99
  - **cash_outcome**: 96128677.52
  - **short_term_interest_bearing_debt_outcome**: 2988994964.8
  - **equity_baseline**: 5175475280.89
  - **equity_outcome**: 174060760.37
  - **standard_unqualified_audit_flag_outcome**: 0
- **derivations**:
  - **item 1**:
    - **metric**: revenue_cagr_baseline_to_outcome
    - **operation**: cagr
    - **inputs**:
      - revenue_baseline
      - revenue_outcome
    - **periods**: 2
    - **value**: -0.4274349999631508
  - **item 2**:
    - **metric**: gross_margin_outcome
    - **operation**: margin
    - **inputs**:
      - revenue_outcome
      - operating_cost_outcome
    - **value**: 0.015817124365235486
  - **item 3**:
    - **metric**: cash_to_short_term_interest_bearing_debt_outcome
    - **operation**: ratio
    - **inputs**:
      - cash_outcome
      - short_term_interest_bearing_debt_outcome
    - **value**: 0.032160869674276005
  - **item 4**:
    - **metric**: equity_retention_baseline_to_outcome
    - **operation**: ratio
    - **inputs**:
      - equity_outcome
      - equity_baseline
    - **value**: 0.03363184073406832

### 对应的题内资料 / Expected evidence

- `annual-project-pipeline-and-capital-model`
- `annual-operating-substance-and-profit-quality`
- `annual-pit-project-balance-sheet`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_operating_chain_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 300090.XSHE
  - **ticker**: 300090
  - **name_as_of**: 盛运环保
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2017-04-27
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=300090.XSHE; if_adjusted=0; earliest info_date per selected annual report; baseline quarter=2016q4 info_date=2017-04-27; outcome quarter=2018q4 info_date=2019-04-30; updated 2018 annual report published 2019-05-16 controls filing text and audit opinion
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2016_annual_report**: 7ae10cf94ddce7aecb80ed1853dd7f3c7d4f15ab2fa3df4be626f250be6972d0
    - **2016_annual_summary**: e4a64b28401358b70779edd3c57c5f05b1cb6ca9c937275e0069a3f069a67e09
  - **causal_guardrail**: The label measures company-level portfolio validation under a fixed hurdle, not causal attribution to any project.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **1203405116.PDF**: 7ae10cf94ddce7aecb80ed1853dd7f3c7d4f15ab2fa3df4be626f250be6972d0
    - **1203405093.PDF**: e4a64b28401358b70779edd3c57c5f05b1cb6ca9c937275e0069a3f069a67e09
- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 安徽盛运环保（集团）股份有限公司2018年年度报告
    - **published_at**: 2019-04-30
    - **url**: https://static.cninfo.com.cn/finalpage/2019-04-30/1206165488.PDF
    - **fields**:
      - 营业收入
      - 营业成本
      - 归属于上市公司股东的净利润
      - 经营活动产生的现金流量净额
      - 货币资金
      - 短期借款
      - 一年内到期的非流动负债
      - 归属于母公司股东权益
      - 审计意见类型
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: f0888debf0aa3d2846c81d9742b9bff51d97bbd3d389bc8140504ef8cfbaef4e
    - **later_corroboration**:
      - **title**: 安徽盛运环保（集团）股份有限公司2018年年度报告（更新后）
      - **published_at**: 2019-05-16
      - **url**: https://static.cninfo.com.cn/finalpage/2019-05-16/1206273382.PDF
      - **sha256**: ef75fe9167293859c0f8e074239dd0d7bc4b20f6b749b2386633fe7165cf1645
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2016q4/data.parquet
      - data/db/rq_income_statement_pit/quarter=2018q4/data.parquet
      - data/db/rq_balance_sheet_pit/quarter=2016q4/data.parquet
      - data/db/rq_balance_sheet_pit/quarter=2018q4/data.parquet
      - data/db/rq_cash_flow_pit/quarter=2018q4/data.parquet
    - **fields**:
      - revenue
      - cost_of_goods_sold
      - net_profit_parent_company
      - cash_flow_from_operating_activities
      - cash_equivalent
      - short_term_loans
      - non_current_liability_due_one_year
      - equity_parent_company
    - **row_policy**: stock_code=300090.XSHE; if_adjusted=0; baseline 2016q4 selected earliest info_date=2017-04-27; outcome 2018q4 selected earliest info_date=2019-04-30; later updated filing only corroborates the earliest-sufficient outcome

</details>

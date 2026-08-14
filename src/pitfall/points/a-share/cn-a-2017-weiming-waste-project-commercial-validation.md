# cn-a-2017-weiming-waste-project-commercial-validation

## Question

你处在2017-04-15收盘后的信息环境。伟明环保披露覆盖研发、设备制造、投资建设和运营的一体化链条，已有13个运营项目和持续扩建/新建项目，同时投入会占用现金。请使用下方冻结资料，沿项目获取、建设、投产、垃圾处理量与上网电量、收入与毛利、现金回收、资本开支、短债、权益和审计链条，预测项目组合能否在2019财年达到target定义的商业兑现事件。该标签不证明任何单个项目导致公司结果，也不评价股价。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 伟明环保 (603568, SSE)
- 信息截止 / As of: 2017-04-15
- 预测窗口结束 / Window end: 2020-04-30
- 目标事件 / Target: `waste_project_portfolio_commercial_validation`
- 判定定义 / Definition: 垃圾焚烧项目组合的公司层面商业兑现事件而非单个项目因果证明：2019财年同时满足收入增长、毛利、盈利、经营现金、短债覆盖、权益保全和审计质量七项条件。收入CAGR=(2019收入/2016收入)^(1/3)-1；毛利率=(收入-营业成本)/收入；短债覆盖=期末货币资金/(短期借款+一年内到期非流动负债)；权益保全=2019归母权益/2016归母权益；标准无保留审计记1，其余记0。

#### 判定条件 / Criteria

- `revenue_cagr_baseline_to_outcome >= 0.15` — 2016年至2019年营业收入复合年增长率不低于15%
- `gross_margin_outcome >= 0.2` — 2019年综合毛利率不低于20%
- `net_profit_outcome > 0` — 2019年归母净利润为正
- `operating_cash_flow_outcome > 0` — 2019年经营活动产生的现金流量净额为正
- `cash_to_short_term_interest_bearing_debt_outcome >= 0.5` — 2019年末货币资金覆盖至少50%的短期借款和一年内到期非流动负债
- `equity_retention_baseline_to_outcome >= 0.8` — 2019年末归母权益至少保留2016年末的80%
- `standard_unqualified_audit_flag_outcome >= 1` — 2019年财务报表审计意见为标准无保留意见

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 伟明环保2016年年报：已运营项目、处理量与复制能力

- Evidence ID: `annual-operating-project-base`
- 发布日期 / Published: 2017-04-15
- 来源 / Source: 伟明环保法定年度报告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2017-04-15/1203301568.PDF

截至2016年末，公司有13个生活垃圾焚烧处理运营项目，其中12个BOT项目；全年垃圾入库量336.98万吨、同比增长9.11%，上网电量9.22亿度、同比增长11.68%。永强二期已并网试运行并于2017年初正式运营，武义、温州餐厨、苍南等项目进入建设，界首PPP项目完成环评和核准。公司称业务覆盖核心技术研发、设备研制、投资建设和运营，全链条有助于控制成本、建设进度和维护，但扩建和新建仍需持续资本投入。

### 伟明环保2016年PIT财务链：高毛利运营、经营现金和建设投入

- Evidence ID: `annual-pit-cash-and-capex-chain`
- 发布日期 / Published: 2017-04-15
- 来源 / Source: 伟明环保法定年度报告及只读RQData点时记录
- URL: https://static.cninfo.com.cn/finalpage/2017-04-15/1203301568.PDF

2016年营业收入693,169,189.43元、营业成本262,972,035.54元、归母净利润328,557,875.28元、经营活动现金流净额427,969,901.70元；项目运营主营收入668,721,609.35元、毛利率62.45%。年末货币资金341,314,463.68元，应收账款净额216,383,474.15元，在建工程285,124,052.15元；无短期借款，一年内到期非流动负债60,520,000.00元，长期借款286,659,998.00元，归母权益1,917,956,277.62元。购建固定资产等支付现金246,728,230.45元。点时口径为603568.XSHG、2016q4、if_adjusted=0、最早info_date=2017-04-15。

### 伟明环保2016年社会责任报告：运营标准、排放与社区约束

- Evidence ID: `social-responsibility-operations`
- 发布日期 / Published: 2017-04-15
- 来源 / Source: 伟明环保法定社会责任报告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2017-04-15/1203301574.PDF

社会责任报告从垃圾接收、焚烧发电、烟气和渗滤液处理等环节描述项目运营，并披露公司持续推进项目建设、环保设施运行和公众沟通。垃圾焚烧项目的商业稳定性不仅取决于签约与建设，还取决于长期达标运营、垃圾量、电力销售、处置费回收和社区接受度；这些约束需要与年报的处理量、现金流和资本开支共同判断。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `waste_project_portfolio_commercial_validation`
- 结果日期 / Resolved at: 2019-12-31
- 可观察日期 / Observed at: 2020-04-25

### 实际结果 / Realized outcome

- **observations**:
  - **revenue_baseline**: 693169189.43
  - **revenue_outcome**: 2038106159.94
  - **operating_cost_outcome**: 774740431.83
  - **net_profit_outcome**: 974452074.12
  - **operating_cash_flow_outcome**: 867871626.27
  - **cash_outcome**: 802031605.29
  - **short_term_interest_bearing_debt_outcome**: 52567272.59
  - **equity_baseline**: 1917956277.62
  - **equity_outcome**: 4210362109.41
  - **standard_unqualified_audit_flag_outcome**: 1
- **derivations**:
  - **item 1**:
    - **metric**: revenue_cagr_baseline_to_outcome
    - **operation**: cagr
    - **inputs**:
      - revenue_baseline
      - revenue_outcome
    - **periods**: 3
    - **value**: 0.4326139760851686
  - **item 2**:
    - **metric**: gross_margin_outcome
    - **operation**: margin
    - **inputs**:
      - revenue_outcome
      - operating_cost_outcome
    - **value**: 0.6198723859149675
  - **item 3**:
    - **metric**: cash_to_short_term_interest_bearing_debt_outcome
    - **operation**: ratio
    - **inputs**:
      - cash_outcome
      - short_term_interest_bearing_debt_outcome
    - **value**: 15.257242116125544
  - **item 4**:
    - **metric**: equity_retention_baseline_to_outcome
    - **operation**: ratio
    - **inputs**:
      - equity_outcome
      - equity_baseline
    - **value**: 2.1952336236958727

### 对应的题内资料 / Expected evidence

- `annual-operating-project-base`
- `annual-pit-cash-and-capex-chain`
- `social-responsibility-operations`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_operating_chain_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 603568.XSHG
  - **ticker**: 603568
  - **name_as_of**: 伟明环保
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2017-04-15
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=603568.XSHG; if_adjusted=0; earliest info_date per selected annual report; baseline quarter=2016q4 info_date=2017-04-15; outcome quarter=2019q4 info_date=2020-04-25
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2016_annual_report**: 7103a4fafd55ddb3bcdecf409c393df8564b9f1fdfb9e4c1f570033080addcf2
    - **2016_social_responsibility_report**: d955af752261ef35f553ab9f1f1721e43c6b2a2e68c0440c1389fc5ce7d55490
  - **causal_guardrail**: The label measures company-level portfolio validation under a fixed hurdle, not causal attribution to any project.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **1203301568.PDF**: 7103a4fafd55ddb3bcdecf409c393df8564b9f1fdfb9e4c1f570033080addcf2
    - **1203301574.PDF**: d955af752261ef35f553ab9f1f1721e43c6b2a2e68c0440c1389fc5ce7d55490
- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 浙江伟明环保股份有限公司2019年年度报告
    - **published_at**: 2020-04-25
    - **url**: https://static.cninfo.com.cn/finalpage/2020-04-25/1207611297.PDF
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
      - **sha256**: c9419f85f43dab5d92d6af7ffe982c9d99cac950d5411df843d7701c01de9b62
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2016q4/data.parquet
      - data/db/rq_income_statement_pit/quarter=2019q4/data.parquet
      - data/db/rq_balance_sheet_pit/quarter=2016q4/data.parquet
      - data/db/rq_balance_sheet_pit/quarter=2019q4/data.parquet
      - data/db/rq_cash_flow_pit/quarter=2019q4/data.parquet
    - **fields**:
      - revenue
      - cost_of_goods_sold
      - net_profit_parent_company
      - cash_flow_from_operating_activities
      - cash_equivalent
      - short_term_loans
      - non_current_liability_due_one_year
      - equity_parent_company
    - **row_policy**: stock_code=603568.XSHG; if_adjusted=0; baseline 2016q4 earliest info_date=2017-04-15; outcome 2019q4 earliest info_date=2020-04-25; null short_term_loans treated as zero only in the declared sum

</details>

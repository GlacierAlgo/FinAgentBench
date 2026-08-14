# cn-a-2020-shanshan-acquisition-commercial-validation

## Question

你处在2020-07-17收盘后的信息环境。杉杉股份计划以自有及借款资金收购LG化学LCD偏光片业务，标的主要工厂、人员和客户在中国，但研发、采购、销售和核心技术支持原由LG化学体系控制，交易还会新增长期贷款并要求跨行业整合。请使用下方冻结资料，沿融资、交割与整合、研发采购生产销售独立化、收入与毛利、现金回收、短债、权益与审计链条，预测该资本配置能否在2022财年达到target定义的商业兑现事件。该标签不证明收购是结果的唯一原因，也不评价股价。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 杉杉股份 (600884, SSE)
- 信息截止 / As of: 2020-07-17
- 预测窗口结束 / Window end: 2023-04-30
- 目标事件 / Target: `acquisition_portfolio_commercial_validation`
- 判定定义 / Definition: 重大跨行业收购后的公司层面商业兑现事件而非收购因果证明：2022财年同时满足收入增长、毛利、盈利、经营现金、短债覆盖、权益保全和审计质量七项条件。收入CAGR=(2022收入/2019收入)^(1/3)-1；毛利率=(收入-营业成本)/收入；短债覆盖=期末货币资金/(短期借款+一年内到期非流动负债)；权益保全=2022归母权益/2019归母权益；标准无保留审计记1，其余记0。

#### 判定条件 / Criteria

- `revenue_cagr_baseline_to_outcome >= 0.15` — 2019年至2022年营业收入复合年增长率不低于15%
- `gross_margin_outcome >= 0.2` — 2022年综合毛利率不低于20%
- `net_profit_outcome > 0` — 2022年归母净利润为正
- `operating_cash_flow_outcome > 0` — 2022年经营活动产生的现金流量净额为正
- `cash_to_short_term_interest_bearing_debt_outcome >= 0.5` — 2022年末货币资金覆盖至少50%的短期借款和一年内到期非流动负债
- `equity_retention_baseline_to_outcome >= 0.8` — 2022年末归母权益至少保留2019年末的80%
- `standard_unqualified_audit_flag_outcome >= 1` — 2022年财务报表审计意见为标准无保留意见

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 杉杉股份收购问询回复：偏光片市场、标的地位与全环节整合

- Evidence ID: `acquisition-market-and-integration`
- 发布日期 / Published: 2020-07-17
- 来源 / Source: 杉杉股份重大资产购买问询回复（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2020-07-17/1208040922.PDF

回复披露，拟收购LG化学LCD偏光片业务。根据公司引用的IHS数据，2020至2022年中国大陆偏光片总需求高于产能，标的大型偏光片2018年、2019年及2020年一季度全球份额分别约27%、27%和26%，主要工厂、产线、生产人员和销售客户位于中国。交易前研发、采购、生产和销售体系主要受LG化学总部控制，核心技术人员和技术支持也主要在韩国；公司计划使标的形成独立研发、采购、生产和销售体系并尽力留任人员。市场份额是强线索，但人员、技术、供应商和客户体系能否平稳拆分整合仍是关键风险。

### 杉杉股份收购问询回复：对价融资、利息覆盖与失败预案

- Evidence ID: `acquisition-financing-and-downside`
- 发布日期 / Published: 2020-07-17
- 来源 / Source: 杉杉股份重大资产购买问询回复（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2020-07-17/1208040922.PDF

公司计划先用自有资金和银行贷款支付对价，定增资金到位后置换，拟保留不超过16亿元长期借款；回复测算一年利息不超过7,440万元。若定增未募足，公司称可出售部分金融资产或向控股股东借款。中国大陆交割日需支付初始认购价格80%，即6.16亿美元；剩余30%股权将在交割后三年内按固定价格分阶段收购并作为金融负债处理。2019年上市公司经营现金流净额8.86亿元，标的未经审计模拟经营现金流净额19.29亿元。融资结构意味着判断必须覆盖交割、整合现金流、利息和后续支付，而不能只看产业趋势。

### 杉杉股份2019年PIT基线：收入、研发、现金与杠杆

- Evidence ID: `baseline-annual-pit-financial-chain`
- 发布日期 / Published: 2020-04-27
- 来源 / Source: 杉杉股份法定年度报告及只读RQData点时记录
- URL: https://static.cninfo.com.cn/finalpage/2020-04-27/1207620697.PDF

2019年营业收入8,679,910,968.83元、营业成本6,839,412,732.26元、归母净利润269,808,780.07元、经营活动现金流净额886,437,952.61元、研发费用411,881,794.27元。年末货币资金2,306,599,524.38元，应收账款净额2,971,553,206.57元，存货1,289,399,733.92元，在建工程1,532,160,308.18元；短期借款3,546,941,904.17元，一年内到期非流动负债1,212,749,605.34元，长期借款1,603,046,858.90元，归母权益11,822,582,211.12元。点时口径为600884.XSHG、2019q4、if_adjusted=0、最早info_date=2020-04-27。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `acquisition_portfolio_commercial_validation`
- 结果日期 / Resolved at: 2022-12-31
- 可观察日期 / Observed at: 2023-04-20

### 实际结果 / Realized outcome

- **observations**:
  - **revenue_baseline**: 8679910968.83
  - **revenue_outcome**: 21701617268.32
  - **operating_cost_outcome**: 16487393265.82
  - **net_profit_outcome**: 2691262599.6
  - **operating_cash_flow_outcome**: 506497694.79
  - **cash_outcome**: 4742265435.59
  - **short_term_interest_bearing_debt_outcome**: 5832525141.92
  - **equity_baseline**: 11822582211.12
  - **equity_outcome**: 23053341900.8
  - **standard_unqualified_audit_flag_outcome**: 1
- **derivations**:
  - **item 1**:
    - **metric**: revenue_cagr_baseline_to_outcome
    - **operation**: cagr
    - **inputs**:
      - revenue_baseline
      - revenue_outcome
    - **periods**: 3
    - **value**: 0.35724716483466956
  - **item 2**:
    - **metric**: gross_margin_outcome
    - **operation**: margin
    - **inputs**:
      - revenue_outcome
      - operating_cost_outcome
    - **value**: 0.24026891351142385
  - **item 3**:
    - **metric**: cash_to_short_term_interest_bearing_debt_outcome
    - **operation**: ratio
    - **inputs**:
      - cash_outcome
      - short_term_interest_bearing_debt_outcome
    - **value**: 0.8130724377861663
  - **item 4**:
    - **metric**: equity_retention_baseline_to_outcome
    - **operation**: ratio
    - **inputs**:
      - equity_outcome
      - equity_baseline
    - **value**: 1.9499413486096675

### 对应的题内资料 / Expected evidence

- `acquisition-market-and-integration`
- `acquisition-financing-and-downside`
- `baseline-annual-pit-financial-chain`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_operating_chain_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600884.XSHG
  - **ticker**: 600884
  - **name_as_of**: 杉杉股份
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-07-17
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=600884.XSHG; if_adjusted=0; earliest info_date per selected annual report; baseline quarter=2019q4 info_date=2020-04-27 no later than as_of; outcome quarter=2022q4 info_date=2023-04-20
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2019_annual_report**: 76e267dfd1dd06d838ea41fa7e4cca1899dc2e89a808849fe06cbcc605cab480
    - **acquisition_response**: d930e894b6e77c49156c724ae73f7362cf56a6329617688d4d5d8b470f91cdb0
  - **causal_guardrail**: The label measures later company-level acquisition validation under a fixed hurdle, not causal attribution to the transaction.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **1208040922.PDF**: d930e894b6e77c49156c724ae73f7362cf56a6329617688d4d5d8b470f91cdb0
    - **1207620697.PDF**: 76e267dfd1dd06d838ea41fa7e4cca1899dc2e89a808849fe06cbcc605cab480
- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 宁波杉杉股份有限公司2022年年度报告
    - **published_at**: 2023-04-20
    - **url**: https://static.cninfo.com.cn/finalpage/2023-04-20/1216475191.PDF
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
      - **sha256**: deb42bf19fdf8fe42178cb2f0175ae8730875263ba12c0beca899394a2dbe3d5
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2019q4/data.parquet
      - data/db/rq_income_statement_pit/quarter=2022q4/data.parquet
      - data/db/rq_balance_sheet_pit/quarter=2019q4/data.parquet
      - data/db/rq_balance_sheet_pit/quarter=2022q4/data.parquet
      - data/db/rq_cash_flow_pit/quarter=2022q4/data.parquet
    - **fields**:
      - revenue
      - cost_of_goods_sold
      - net_profit_parent_company
      - cash_flow_from_operating_activities
      - cash_equivalent
      - short_term_loans
      - non_current_liability_due_one_year
      - equity_parent_company
    - **row_policy**: stock_code=600884.XSHG; if_adjusted=0; baseline 2019q4 earliest info_date=2020-04-27; outcome 2022q4 earliest info_date=2023-04-20

</details>

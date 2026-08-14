# cn-a-2018-naura-technology-commercial-validation

## Question

你处在2018-04-12收盘后的信息环境。北方华创披露半导体关键工艺设备的客户端验证与产业化、订单带来的备货和扩产，同时面临国际竞争、人才、知识产权及研发资本化风险。请使用下方冻结资料，从技术与客户验证、订单执行、扩产、收入与毛利、存货和应收、经营现金、短债与审计质量等环节，预测公司能否在2020财年达到target定义的技术业务商业兑现事件。该标签不证明研发是结果的唯一原因，也不评价股票收益。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 北方华创 (002371, SZSE)
- 信息截止 / As of: 2018-04-12
- 预测窗口结束 / Window end: 2021-04-30
- 目标事件 / Target: `technology_business_commercial_validation`
- 判定定义 / Definition: 公司层面的技术商业兑现事件而非研发投入的因果证明：2020财年同时满足预先声明的收入增长、毛利、盈利、经营现金、短债覆盖、权益保全和审计质量七项条件。收入CAGR=(2020收入/2017收入)^(1/3)-1；毛利率=(收入-营业成本)/收入；短债覆盖=期末货币资金/(短期借款+一年内到期非流动负债)；权益保全=2020归母权益/2017归母权益；标准无保留审计记1，其余记0。

#### 判定条件 / Criteria

- `revenue_cagr_baseline_to_outcome >= 0.2` — 2017年至2020年营业收入复合年增长率不低于20%
- `gross_margin_outcome >= 0.25` — 2020年综合毛利率不低于25%
- `net_profit_outcome > 0` — 2020年归母净利润为正
- `operating_cash_flow_outcome > 0` — 2020年经营活动产生的现金流量净额为正
- `cash_to_short_term_interest_bearing_debt_outcome >= 0.5` — 2020年末货币资金覆盖至少50%的短期借款和一年内到期非流动负债
- `equity_retention_baseline_to_outcome >= 0.8` — 2020年末归母权益至少保留2017年末的80%
- `standard_unqualified_audit_flag_outcome >= 1` — 2020年财务报表审计意见为标准无保留意见

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 北方华创2017年年报：关键设备产业化、客户验证与竞争风险

- Evidence ID: `annual-product-customer-validation`
- 发布日期 / Published: 2018-04-12
- 来源 / Source: 北方华创法定年度报告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2018-04-12/1204618312.PDF

年报披露，公司产品覆盖刻蚀机、PVD、CVD、氧化炉、扩散炉、清洗机和质量流量控制器等关键工艺装备。承担的14nm制程设备已交付客户端工艺验证，28nm及以上制程设备已批量进入国内主流集成电路生产线，部分成为龙头芯片厂商量产线Baseline机台；8英寸设备也进入主流代工厂和IDM企业。公司同时提示国际竞争加剧、知识产权冲突和核心技术人才流失风险。这些客户端与量产线信息构成商业验证线索，但仍需用未来规模、毛利和现金结果验证。

### 北方华创2017年年报：订单、扩产、存货与研发资本化

- Evidence ID: `annual-orders-expansion-and-inventory`
- 发布日期 / Published: 2018-04-12
- 来源 / Source: 北方华创法定年度报告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2018-04-12/1204618312.PDF

2017年营业收入2,222,818,469.69元，其中半导体设备收入1,133,849,163.98元、同比增长39.47%；年报列示多份单晶炉设备合同已履行或正在履行。电子工艺装备生产规模和订单增长带动备货：年末存货2,032,528,852.44元、同比增长72.53%，其中电子工艺装备库存量口径同比增长133.83%；在建工程320,313,019.95元、同比增长50.98%，主要因微电子装备扩产项目。开发支出796,823,510.70元、同比增长79.21%，主要因资本化研发投入增加。订单与库存同步上升既可能支持交付，也可能放大执行和回款风险。

### 北方华创2017年PIT财务链：利润、现金、应收、短债与权益

- Evidence ID: `annual-pit-financial-chain`
- 发布日期 / Published: 2018-04-12
- 来源 / Source: 北方华创法定年度报告及只读RQData点时记录
- URL: https://static.cninfo.com.cn/finalpage/2018-04-12/1204618249.PDF

2017年营业收入2,222,818,469.69元、营业成本1,409,548,683.35元、归母净利润125,610,225.49元、经营活动现金流净额31,620,679.25元。年末货币资金1,020,266,834.88元，应收账款净额734,912,166.84元，存货2,032,528,852.44元；短期借款429,575,282.32元，一年内到期非流动负债90,385,733.86元，归母权益3,307,685,414.27元。销售商品、提供劳务收到现金2,124,420,496.18元。点时口径为002371.XSHE、2017q4、if_adjusted=0、最早info_date=2018-04-12。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `technology_business_commercial_validation`
- 结果日期 / Resolved at: 2020-12-31
- 可观察日期 / Observed at: 2021-04-29

### 实际结果 / Realized outcome

- **observations**:
  - **revenue_baseline**: 2222818469.69
  - **revenue_outcome**: 6056043031.2
  - **operating_cost_outcome**: 3834262926.92
  - **net_profit_outcome**: 536930435.37
  - **operating_cash_flow_outcome**: 1385139594.68
  - **cash_outcome**: 2642404146.96
  - **short_term_interest_bearing_debt_outcome**: 630259929.68
  - **equity_baseline**: 3307685414.27
  - **equity_outcome**: 6780875585.98
  - **standard_unqualified_audit_flag_outcome**: 1
- **derivations**:
  - **item 1**:
    - **metric**: revenue_cagr_baseline_to_outcome
    - **operation**: cagr
    - **inputs**:
      - revenue_baseline
      - revenue_outcome
    - **periods**: 3
    - **value**: 0.39667379632885136
  - **item 2**:
    - **metric**: gross_margin_outcome
    - **operation**: margin
    - **inputs**:
      - revenue_outcome
      - operating_cost_outcome
    - **value**: 0.3668699335248541
  - **item 3**:
    - **metric**: cash_to_short_term_interest_bearing_debt_outcome
    - **operation**: ratio
    - **inputs**:
      - cash_outcome
      - short_term_interest_bearing_debt_outcome
    - **value**: 4.192562500842502
  - **item 4**:
    - **metric**: equity_retention_baseline_to_outcome
    - **operation**: ratio
    - **inputs**:
      - equity_outcome
      - equity_baseline
    - **value**: 2.050036426295554

### 对应的题内资料 / Expected evidence

- `annual-product-customer-validation`
- `annual-orders-expansion-and-inventory`
- `annual-pit-financial-chain`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_operating_chain_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002371.XSHE
  - **ticker**: 002371
  - **name_as_of**: 北方华创
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2018-04-12
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=002371.XSHE; if_adjusted=0; earliest info_date per selected annual report; baseline quarter=2017q4 info_date=2018-04-12; outcome quarter=2020q4 info_date=2021-04-29
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2017_annual_report**: 49f45b7a7cf55b3b3978f88a80253f1520aa26482ce2f3cbdc1f82850a19fa2f
    - **2017_annual_summary**: 67b2834a4fba09afa3398c797c2e9b5561b7163b87626638645ff13d6c4ef77c
  - **causal_guardrail**: The label measures later company-level commercial validation under a fixed hurdle, not causal attribution to R&D spending.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **1204618312.PDF**: 49f45b7a7cf55b3b3978f88a80253f1520aa26482ce2f3cbdc1f82850a19fa2f
    - **1204618249.PDF**: 67b2834a4fba09afa3398c797c2e9b5561b7163b87626638645ff13d6c4ef77c
- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 北方华创科技集团股份有限公司2020年年度报告
    - **published_at**: 2021-04-29
    - **url**: https://static.cninfo.com.cn/finalpage/2021-04-29/1209852702.PDF
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
      - **sha256**: 11e896cd661a64a1a4f6a62a32275fe3494ac9600f8df3764fd7a8dae33cb18e
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2017q4/data.parquet
      - data/db/rq_income_statement_pit/quarter=2020q4/data.parquet
      - data/db/rq_balance_sheet_pit/quarter=2017q4/data.parquet
      - data/db/rq_balance_sheet_pit/quarter=2020q4/data.parquet
      - data/db/rq_cash_flow_pit/quarter=2020q4/data.parquet
    - **fields**:
      - revenue
      - cost_of_goods_sold
      - net_profit_parent_company
      - cash_flow_from_operating_activities
      - cash_equivalent
      - short_term_loans
      - non_current_liability_due_one_year
      - equity_parent_company
    - **row_policy**: stock_code=002371.XSHE; if_adjusted=0; baseline 2017q4 earliest info_date=2018-04-12; outcome 2020q4 earliest info_date=2021-04-29

</details>

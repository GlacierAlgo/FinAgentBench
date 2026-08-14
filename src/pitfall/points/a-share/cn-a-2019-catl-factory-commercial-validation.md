# cn-a-2019-catl-factory-commercial-validation

## Question

你处在2019-04-25收盘后的信息环境。宁德时代公告拟以不超过46.24亿元建设湖西锂离子电池扩建项目，计划建设期36个月。请使用下方冻结资料，预测该工厂投资能否在2022年年报时达到target定义的后续商业验证。请综合项目规模与资金、既有产能和市场份额、行业需求、客户与竞争、技术迭代、原材料和周期风险、现金创造及产能消化能力。结果规则检验项目里程碑和公司层面的经营兑现，不声称该项目单独造成收入增长，也不是严格的反事实“最优投资”证明。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 宁德时代 (300750, SZSE)
- 信息截止 / As of: 2019-04-25
- 预测窗口结束 / Window end: 2023-04-30
- 目标事件 / Target: `announced_factory_commercial_validation_by_fy2022`
- 判定定义 / Definition: 工厂投资的后续商业验证而非单项目因果回报证明：建设进度、公司增长、毛利、经营现金流和产能利用率同时满足预先声明条件

#### 判定条件 / Criteria

- `announced_factory_schedule_validation >= 1` — 公告项目在原计划期附近被正式披露达到预定可使用状态或等价明确里程碑
- `revenue_cagr_baseline_to_outcome >= 0.2` — 公告前完整年度至结果年度营业收入复合年增长率不低于20%
- `gross_margin_outcome >= 0.1` — 结果年度综合毛利率不低于10%
- `operating_cash_flow_outcome > 0` — 结果年度经营活动产生的现金流量净额为正
- `capacity_utilization_outcome >= 0.75` — 结果年度相关制造业务披露的产能利用率不低于75%

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 宁德时代关于投资建设湖西锂离子电池扩建项目的公告

- Evidence ID: `huxi-expansion-announcement`
- 发布日期 / Published: 2019-04-25
- 来源 / Source: 宁德时代法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2019-04-25/1206093007.PDF

公告披露，宁德时代拟建设湖西锂离子电池扩建项目，总投资不超过人民币46.24亿元，占地约855亩，建设期36个月，资金来源为企业自筹。公司称项目用于满足市场需求、推进发展战略并巩固市场地位；实际建设进度将受资金安排、审批、市场环境等影响。大额资本支出与明确工期形成可验证承诺，但公告没有保证产能利用、盈利或现金回报。

### 宁德时代2018年年度报告：市场份额、增长基础与经营风险

- Evidence ID: `fy2018-market-and-capacity-base`
- 发布日期 / Published: 2019-04-25
- 来源 / Source: 宁德时代法定年度报告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2019-04-25/1206093043.PDF

2018年年度报告披露营业收入296.11亿元，动力电池系统销量同比增长47.18%。按报告引用数据，公司2018年国内动力电池装机约23.4GWh、市场份额约41%，客户和规模基础支持扩产。报告同时提示新能源汽车政策、行业竞争、技术路线、产能扩张、原材料价格、客户集中及存货等风险；扩产项目需要经历设备、爬坡、客户需求和资金回收验证。湖西园区已有前期项目和募集资金投入，新增46.24亿元扩建应结合既有制造能力与未来需求判断，而不能只依据行业增长口号。

### 动力电池装机量高速增长、行业集中度提升

- Evidence ID: `industry-news-demand-and-competition`
- 发布日期 / Published: 2019-04-10
- 来源 / Source: 中国证券报·中证网（申万宏源行业观点）
- URL: https://www.cs.com.cn/gppd/sdqs/201904/t20190410_5937531.html

报道援引真锂研究数据称，宁德时代2019年1至2月动力电池装机3.08GWh、同比增长156.9%，市场份额41.12%；同期国内动力电池企业数量由2017年的135家降至2018年的90家，新增产能向一线企业集中。报道还梳理公司与上汽、广汽、吉利、北汽新能源的合作、既有湖西和江苏产能计划及海外客户与德国工厂规划。这些外部装机和行业集中信号支持扩产需求判断，但分析师评级和需求预测不是项目按期投产、利用率与回报的保证。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `announced_factory_commercial_validation_by_fy2022`
- 结果日期 / Resolved at: 2023-03-10

### 实际结果 / Realized outcome

- **observations**:
  - **announced_factory_schedule_validation**: 1
  - **revenue_baseline**: 29611265434.22
  - **revenue_outcome**: 328593987500.0
  - **operating_cost_outcome**: 262049609200.0
  - **operating_cash_flow_outcome**: 61208843300.0
  - **capacity_utilization_outcome**: 0.834
- **derivations**:
  - **item 1**:
    - **metric**: revenue_cagr_baseline_to_outcome
    - **operation**: cagr
    - **inputs**:
      - revenue_baseline
      - revenue_outcome
    - **periods**: 4
    - **value**: 0.8251588193489803
  - **item 2**:
    - **metric**: gross_margin_outcome
    - **operation**: margin
    - **inputs**:
      - revenue_outcome
      - operating_cost_outcome
    - **value**: 0.20251246471757187

### 对应的题内资料 / Expected evidence

- `huxi-expansion-announcement`
- `fy2018-market-and-capacity-base`
- `industry-news-demand-and-competition`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_business_decision_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 300750.XSHE
  - **ticker**: 300750
  - **name_as_of**: 宁德时代
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-04-25
  - **allowed_domains**:
    - cninfo.com.cn
    - cs.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=300750.XSHE; if_adjusted=0; earliest info_date per annual report; 2018 agent baseline; 2022 outcome
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **news_evidence_policy**: Contemporaneous news may supply industry demand and competitive context; official filings and RQData remain label authority.
  - **causal_guardrail**: The label combines a disclosed project milestone with company-level commercial validation; it does not attribute company outcomes solely to this factory or prove counterfactual optimality.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 宁德时代新能源科技股份有限公司2022年年度报告
    - **published_at**: 2023-03-10
    - **url**: https://static.cninfo.com.cn/finalpage/2023-03-10/1216084559.PDF
    - **fields**:
      - 湖西锂离子电池扩建项目投资进度与效益
      - 营业收入
      - 营业成本
      - 经营活动现金流量净额
      - 动力电池系统产能利用率
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2018q4/data.parquet
      - data/db/rq_income_statement_pit/quarter=2022q4/data.parquet
      - data/db/rq_cash_flow_pit/quarter=2022q4/data.parquet
    - **fields**:
      - revenue
      - gross_profit
      - cash_flow_from_operating_activities
    - **row_policy**: stock_code=300750.XSHE; if_adjusted=0; earliest info_date

</details>

# cn-a-2022-hygon-rd-commercial-validation

## Question

你处在2022-08-11收盘后的信息环境。海光信息即将上市，历史研发强度和研发资本化比例很高，CPU/DCU多代产品处于不同商业化阶段。请使用下方冻结资料，预测其上市前研发与产品路线能否在2024年年报中达到target定义的商业兑现事件。请同时评估产品竞争力、客户与订单验证、技术迭代、生态与供应链约束、客户/关联交易集中度及财务质量。该事件是可审计的结果规则，不代表研发投入已经被证明是收入增长的唯一原因，也不评价股票收益。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 海光信息 (688041, SSE)
- 信息截止 / As of: 2022-08-11
- 预测窗口结束 / Window end: 2025-04-30
- 目标事件 / Target: `pre_listing_rnd_commercial_validation_by_fy2024`
- 判定定义 / Definition: 商业兑现事件而非研发投入与结果之间的因果证明：2024年年度报告同时满足预先声明的增长、毛利与现金流三项条件

#### 判定条件 / Criteria

- `revenue_cagr_2021_2024 >= 0.3` — 2021年至2024年营业收入复合年增长率不低于30%
- `gross_margin_2024 >= 0.5` — 2024年综合毛利率不低于50%
- `operating_cash_flow_2024 > 0` — 2024年经营活动产生的现金流量净额为正

<details>
<summary>冻结资料 / Frozen evidence (4)</summary>

### 海光信息发行注册环节反馈意见落实函之回复报告：持续经营与产品迭代

- Evidence ID: `registration-feedback-product-roadmap`
- 发布日期 / Published: 2022-06-22
- 来源 / Source: 上海证券交易所科创板发行上市审核
- URL: https://static.sse.com.cn/stock/disclosure/announcement/c/202206/001043_20220622_E5LP.pdf

回复报告第3页披露，截至报告期末海光一号、海光二号已实现商业化应用，海光三号完成实验室验证，海光四号处于研发阶段；海光一号、二号已在政府、三大运营商、五大国有银行等行业用户应用。深算一号已完成量产并规模化应用于人工智能智算中心，深算二号完成验证仿真。第13页披露，深算一号已经开始规模化销售，深算二号在增加计算单元规模、改进片上网络协议和优化访存子系统等方面迭代，当时预计2022年5月流片；海光三号相对海光二号综合性能提升20%以上。回复称2019年被列入实体清单、AMD停止技术交流后，公司仍独立迭代多款CPU和DCU产品。第16页称CPU兼容x86指令集和主流操作系统、应用软件，DCU采用GPGPU架构并兼容“类CUDA”环境；公司产品已用于电信、金融、互联网、教育、交通等领域。但以上产品进展和竞争力判断主要来自发行人及中介回复，仍需结合商业订单、客户结构与外部约束判断。

### 海光信息科创板首轮问询回复：市场份额、订单与客户认证

- Evidence ID: `ipo-inquiry-commercialization`
- 发布日期 / Published: 2022-03-04
- 来源 / Source: 上海证券交易所科创板发行上市审核
- URL: https://static.sse.com.cn/stock/disclosure/announcement/c/202203/001043_20220304_7DDI.pdf

问询回复披露，根据IDC数据，2020年国内x86服务器芯片出货量698.1万颗，Intel与AMD合计份额超过95%，海光CPU销量约占总体市场的3.75%，说明国产细分地位与总体市场竞争压力并存。截至2022年1月31日，公司在手订单约21.07亿元。公司解释，处理器大规模量产前需完成与主流内存、硬盘、网卡等硬件，以及操作系统、中间件、数据库和应用软件的大规模适配测试，并通过整机厂客户认证。回复同时披露产品已通过浪潮、联想、新华三、同方等整机厂适配并进入部分金融、电信等终端场景；这些订单、适配和认证构成早期商业验证，但不能保证未来收入、毛利和现金流一定达到目标。

### 海光信息上市公告书：研发投入、2021经营结果与集中度风险

- Evidence ID: `listing-announcement-risk-financials`
- 发布日期 / Published: 2022-08-11
- 来源 / Source: 海光信息法定上市公告书（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2022-08-11/1214267801.PDF

上市公告书第6页披露，2021年公司首次盈利，营业收入231,041.53万元、毛利129,270.73万元，主要原因包括市场需求增长和DCU产品规模销售；同时提示公司成立时间较短，只有海光一号、海光二号、深算一号实现销售和商业化应用，多款产品仍在研发，供应紧缺、产能、竞争力、市场开拓和研发投入不能及时转化为产品收入都可能造成业绩波动。第7页披露，报告期累计研发投入353,902.71万元，占累计营业收入95.35%；研发支出资本化比例分别为79.71%、51.18%、53.02%，形成较大自研无形资产，存在技术替代或市场变化导致减值的风险。同期关联销售占比分别为87.39%、55.83%、65.95%；截至2022年1月末在手订单约21亿元，其中关联方订单12.74亿元。第8页披露，前三年前五大客户销售占比分别为99.12%、92.21%、91.23%，且实体清单可能影响晶圆流片、EDA、IP、研发进度、工艺更新与供应链保障。

### 海光信息申购前新闻：高端处理器定位与高速增长预期

- Evidence ID: `contemporaneous-news-growth-expectation`
- 发布日期 / Published: 2022-08-01
- 来源 / Source: 证券时报
- URL: https://news.stcn.com/sd/202208/t20220801_4770751.html

证券时报在新股申购周报道中将海光信息列为高端处理器国内领先企业，主营海光CPU和DCU，并列出发行资料中的2022年前三季度预测：营业收入约36.7亿至40.8亿元、同比增长170%至200%，归母净利润6.1亿至7亿元、同比增长392%至465%。这份同时点新闻表明市场当时已有强增长预期，能够与在手订单和产品量产证据交叉核对；但报道数字来自发行材料，不能替代客户分散、现金回收、供应链和国际竞争力验证。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `pre_listing_rnd_commercial_validation_by_fy2024`
- 结果日期 / Resolved at: 2025-03-01

### 实际结果 / Realized outcome

- **observations**:
  - **revenue_2021**: 2310415312.15
  - **revenue_2024**: 9162148135.92
  - **operating_cost_2024**: 3324009349.21
  - **operating_cash_flow_2024**: 977081091.31
- **derivations**:
  - **item 1**:
    - **metric**: revenue_cagr_2021_2024
    - **operation**: cagr
    - **inputs**:
      - revenue_2021
      - revenue_2024
    - **periods**: 3
    - **value**: 0.5828353892060956
  - **item 2**:
    - **metric**: gross_margin_2024
    - **operation**: margin
    - **inputs**:
      - revenue_2024
      - operating_cost_2024
    - **value**: 0.6372019640046754

### 对应的题内资料 / Expected evidence

- `registration-feedback-product-roadmap`
- `ipo-inquiry-commercialization`
- `listing-announcement-risk-financials`
- `contemporaneous-news-growth-expectation`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_business_decision_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 688041.XSHG
  - **ticker**: 688041
  - **name_as_of**: 海光信息
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2022-08-11
  - **allowed_domains**:
    - sse.com.cn
    - cninfo.com.cn
    - stcn.com
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=688041.XSHG; if_adjusted=0; earliest info_date per annual report; 2021 agent baseline; 2024 outcome
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **registration_feedback**: 40c903773bc342731c426b8ac9a2bbc267317443847e4b2f25cd5a00a3ba65f9
    - **ipo_inquiry**: 7c839c74cfb2b476758d74a01b4480bbc2215a5b62dc8570dade823f291c542e
    - **listing_announcement**: 737a8bc42f7a02fdbeb23991309c9c7824e4db32d27066261f46ddef7947e6fd
  - **news_evidence_policy**: Contemporaneous news may supply market framing and externally selected risk signals; official filings and RQData remain label authority.
  - **causal_guardrail**: The label measures later commercial validation under a predeclared rule, not causal attribution to R&D spending.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 海光信息技术股份有限公司2024年年度报告
    - **published_at**: 2025-03-01
    - **url**: https://star.sse.com.cn/disclosure/listedinfo/announcement/c/new/2025-03-01/688041_20250301_Q41F.pdf
    - **fields**:
      - 营业收入
      - 营业成本
      - 经营活动产生的现金流量净额
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2021q4/data.parquet
      - data/db/rq_income_statement_pit/quarter=2024q4/data.parquet
      - data/db/rq_cash_flow_pit/quarter=2024q4/data.parquet
    - **fields**:
      - revenue
      - gross_profit
      - cash_flow_from_operating_activities
    - **row_policy**: stock_code=688041.XSHG; if_adjusted=0; earliest info_date

</details>

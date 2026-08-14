# cn-a-2020-cambricon-rd-commercial-validation

## Question

你处在2020-06-22收盘后的信息环境。寒武纪已披露招股说明书，历史收入快速增长且持续高强度研发，但客户、产品形态和订单结构变化很快。请使用下方冻结资料，预测其上市前研发与AI芯片产品路线能否在2022年年报中达到target定义的商业兑现事件。请同时评估产品竞争力与软件生态、客户和订单验证、客户集中度、边缘与云端产品放量、供应链依赖及财务质量。该事件是可审计的结果规则，不代表研发投入已经被证明是收入增长的唯一原因，也不评价股票收益。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 寒武纪 (688256, SSE)
- 信息截止 / As of: 2020-06-22
- 预测窗口结束 / Window end: 2023-04-30
- 目标事件 / Target: `pre_listing_rnd_commercial_validation_by_fy2022`
- 判定定义 / Definition: 商业兑现事件而非研发投入与结果之间的因果证明：2022年年度报告同时满足预先声明的增长、毛利与现金流三项条件

#### 判定条件 / Criteria

- `revenue_cagr_2019_2022 >= 0.3` — 2019年至2022年营业收入复合年增长率不低于30%
- `gross_margin_2022 >= 0.5` — 2022年综合毛利率不低于50%
- `operating_cash_flow_2022 > 0` — 2022年经营活动产生的现金流量净额为正

<details>
<summary>冻结资料 / Frozen evidence (4)</summary>

### 寒武纪招股说明书：收入增长、产品结构变化与持续亏损

- Evidence ID: `prospectus-product-transition`
- 发布日期 / Published: 2020-06-22
- 来源 / Source: 上海证券交易所科创板发行上市审核
- URL: https://static.sse.com.cn/stock/disclosure/announcement/c/202006/000354_20200622_AWSW.pdf

招股说明书披露，2017年至2019年营业收入由784.33万元增至44,393.85万元，但业务结构快速变化：终端智能处理器IP授权收入在华为海思停止合作后下降，云端智能芯片及加速卡2019年收入主要来自关联方中科曙光，关联销售6,384.43万元、占该类收入80.94%，其他云端客户仅1,503.81万元；边缘智能芯片尚未形成规模收入。智能计算集群系统2019年确认18,570.66万元收入，但当时尚无其他同类订单。公司报告期持续亏损且预计短期内仍不能盈利。高速增长、产品落地和国内AI算力需求是正面证据，收入基数低、业务跳变和订单可重复性则是重要反向证据。

### 寒武纪首轮问询回复：客户集中、竞争生态与商业化风险

- Evidence ID: `inquiry-customer-ecosystem-risk`
- 发布日期 / Published: 2020-05-07
- 来源 / Source: 上海证券交易所科创板发行上市审核
- URL: https://static.sse.com.cn/stock/disclosure/announcement/c/202005/000354_20200507_QK2Z.pdf

问询回复显示，2017年至2019年前五大客户销售占比分别为100%、99.95%和95.44%，单一大客户和关联客户变化可显著影响收入。发行人承认英伟达在云端AI芯片市场占主导地位，寒武纪在软件生态、开发者积累和销售网络方面仍弱；新芯片需要客户导入、适配和量产验证。公司采用Fabless模式，晶圆制造、EDA/IP等环节供应商集中，台积电以及Cadence、Synopsys、ARM等境外供应商依赖带来交付和迭代风险。客户验证、在研产品和国产替代机会支持成长判断，但不能直接推出稳定订单、现金回收或高毛利持续兑现。

### 寒武纪第二轮问询回复：在手项目、产品路线与收入可持续性

- Evidence ID: `second-inquiry-orders-and-roadmap`
- 发布日期 / Published: 2020-05-20
- 来源 / Source: 上海证券交易所科创板发行上市审核
- URL: https://static.sse.com.cn/stock/disclosure/announcement/c/202005/000354_20200520_L0C9.pdf

第二轮问询继续要求发行人说明收入可持续性、智能计算集群业务是否具有偶发性以及芯片客户拓展。回复列示云端、边缘端和终端产品路线及部分在手项目，但多项产品仍处于研发、测试或客户导入阶段；不同产品线从技术验证到规模销售存在较长链条。发行人强调算法、编译器和软硬件协同能力，也提示研发投入大、产品迭代快、市场竞争激烈及客户采购节奏不确定。判断商业兑现需要把产品技术叙事同可重复订单、客户分散度、毛利和经营现金流共同验证。

### 寒武纪冲刺科创板：估值上升与商业化压力并存

- Evidence ID: `contemporaneous-news-commercialization-warning`
- 发布日期 / Published: 2020-06-04
- 来源 / Source: 中国证券报·中证网
- URL: https://www.cs.com.cn/ssgs/gsxw/202006/t20200604_6063798.html

中国证券报在寒武纪过会后报道，保荐机构以市销率和2020年6亿至9亿元收入预测支撑估值，但公司同期预计2020年上半年收入仅0.82亿至0.86亿元，同比下降约12.24%至16.32%，主要受华为海思终端智能处理器IP授权收入下降及疫情影响；预计上半年亏损2.1亿至2.3亿元，研发投入增加是主要原因。报道把高估值与客户变化、短期收入下滑和研发烧钱并置，提供了独立于发行人长篇技术叙事的商业化风险入口，但其中收入与亏损数字仍源自公司披露。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `pre_listing_rnd_commercial_validation_by_fy2022`
- 结果日期 / Resolved at: 2023-04-29

### 实际结果 / Realized outcome

- **observations**:
  - **revenue_2019**: 443938465.82
  - **revenue_2022**: 729034623.05
  - **operating_cost_2022**: 249622353.64
  - **operating_cash_flow_2022**: -1329861090.04
- **derivations**:
  - **item 1**:
    - **metric**: revenue_cagr_2019_2022
    - **operation**: cagr
    - **inputs**:
      - revenue_2019
      - revenue_2022
    - **periods**: 3
    - **value**: 0.179800182744708
  - **item 2**:
    - **metric**: gross_margin_2022
    - **operation**: margin
    - **inputs**:
      - revenue_2022
      - operating_cost_2022
    - **value**: 0.6575987672633761

### 对应的题内资料 / Expected evidence

- `prospectus-product-transition`
- `inquiry-customer-ecosystem-risk`
- `second-inquiry-orders-and-roadmap`
- `contemporaneous-news-commercialization-warning`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_business_decision_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 688256.XSHG
  - **ticker**: 688256
  - **name_as_of**: 寒武纪
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-06-22
  - **allowed_domains**:
    - sse.com.cn
    - cs.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=688256.XSHG; if_adjusted=0; earliest info_date per annual report; 2019 agent baseline; 2022 outcome
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **news_evidence_policy**: Contemporaneous news may supply market framing and externally selected risk signals; official filings and RQData remain label authority.
  - **causal_guardrail**: The label measures later commercial validation under a predeclared rule, not causal attribution to R&D spending.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 中科寒武纪科技股份有限公司2022年年度报告摘要
    - **published_at**: 2023-04-29
    - **url**: https://star.sse.com.cn/disclosure/listedinfo/announcement/c/new/2023-04-29/688256_20230429_U7IG.pdf
    - **fields**:
      - 营业收入
      - 营业成本
      - 经营活动产生的现金流量净额
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2019q4/data.parquet
      - data/db/rq_income_statement_pit/quarter=2022q4/data.parquet
      - data/db/rq_cash_flow_pit/quarter=2022q4/data.parquet
    - **fields**:
      - revenue
      - gross_profit
      - cash_flow_from_operating_activities
    - **row_policy**: stock_code=688256.XSHG; if_adjusted=0; earliest info_date

</details>

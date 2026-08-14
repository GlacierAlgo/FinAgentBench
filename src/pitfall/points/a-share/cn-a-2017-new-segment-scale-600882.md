# cn-a-2017-new-segment-scale-600882

## Question

你处在2017-08-04收盘后的信息环境。广泽股份已从地产相关资产转向乳制品，并披露奶酪加工建设项目和非公开发行材料。请使用下方冻结资料，预测奶酪新分部能否在2019年度达到target定义的商业规模。重点分析既有销量与产能瓶颈、产品与渠道扩张、技术人才、消费需求、竞争与进口替代、融资和建设执行风险；不得把未来更名或品牌口号直接当作兑现。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 广泽股份 (600882, SSE)
- 信息截止 / As of: 2017-08-04
- 预测窗口结束 / Window end: 2020-08-04
- 目标事件 / Target: `announced_new_segment_scaled_at_registered_outcome_within_36_month_window`
- 判定定义 / Definition: 在预先登记的结果年度，新业务分部收入占公司营业收入至少50%，且该分部毛利润为正；名称变更、公告措辞和股价表现均不作为判定条件

#### 判定条件 / Criteria

- `new_segment_revenue_share_outcome >= 0.5` — 结果年度新业务分部收入除以公司营业收入不低于50%
- `new_segment_gross_profit_outcome > 0` — 结果年度新业务分部收入减营业成本为正

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 广泽股份2016年年度报告：乳制品转型的经营基线

- Evidence ID: `fy2016-cheese-base`
- 发布日期 / Published: 2017-03-17
- 来源 / Source: 广泽股份法定年度报告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2017-03-17/1203168896.PDF

年度报告披露公司完成乳制品相关资产整合，形成液态奶、奶酪和乳制品贸易业务。报告提供奶酪收入、销量、产能与毛利等经营基线，也提示原料价格、食品安全、市场竞争、渠道建设和新品推广风险。判断后续规模化应依赖可复核的收入结构与盈利，而非资产名称或产业标签。

### 广泽股份非公开发行A股股票预案：奶酪加工建设项目

- Evidence ID: `cheese-capacity-prospectus`
- 发布日期 / Published: 2017-08-04
- 来源 / Source: 广泽股份法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2017-08-04/1203759111.PDF

预案称妙可蓝多2014至2016年奶酪销量由980吨增至4,190.68吨，现有产能难以满足扩张需要；募投项目拟丰富原制、再制和休闲奶酪产品并拓展全国渠道。材料列示项目投产后的预计收入和回收期，同时说明行业尚处早期、技术和渠道执行、产能消化及预测假设均需后续验证。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `announced_new_segment_scaled_at_registered_outcome_within_36_month_window`
- 结果日期 / Resolved at: 2019-12-31
- 可观察日期 / Observed at: 2020-04-29

### 实际结果 / Realized outcome

- **observations**:
  - **total_revenue_outcome**: 1744349052.12
  - **new_segment_revenue_outcome**: 921277142.36
  - **new_segment_cost_outcome**: 540952992.46
- **derivations**:
  - **item 1**:
    - **metric**: new_segment_revenue_share_outcome
    - **operation**: ratio
    - **inputs**:
      - new_segment_revenue_outcome
      - total_revenue_outcome
    - **value**: 0.5281495359201893
  - **item 2**:
    - **metric**: new_segment_gross_profit_outcome
    - **operation**: difference
    - **inputs**:
      - new_segment_revenue_outcome
      - new_segment_cost_outcome
    - **value**: 380324149.9

### 对应的题内资料 / Expected evidence

- `fy2016-cheese-base`
- `cheese-capacity-prospectus`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_name_business_transition_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600882.XSHG
  - **ticker**: 600882
  - **name_as_of**: 广泽股份
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2017-08-04
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
  - **row_policy**: stock_code=600882.XSHG; quarter=2019q4; if_adjusted=0; selected earliest info_date=2020-04-29; official annual-report product table defines target revenue and cost
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **news_evidence_policy**: Frozen evidence is limited to contemporaneous issuer filings.
  - **causal_guardrail**: The benchmark tests commercial scaling of the named new segment, not whether a rename itself is good or bad.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **fy2016-cheese-base**: 52edfe9c4f1ef1f16c21e7191bffbed95e2bb7fcb82e3f16652103901e438f9f
    - **cheese-capacity-prospectus**: a7148c9ef549b85cb02bc8e1ea559df37f02bb4308c895faea190e4a4d93dca2
- **label_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **outcome_source_sha256**:
    - **1207661081.PDF**: 18826f8e6325d336cd4d7d2f2101eb1e14394e37ca4ebb71f816822af28d6a2b
- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 上海妙可蓝多食品科技股份有限公司2019年年度报告
    - **published_at**: 2020-04-29
    - **url**: https://static.cninfo.com.cn/finalpage/2020-04-29/1207661081.PDF
    - **fields**:
      - 营业收入
      - 奶酪营业收入
      - 奶酪营业成本
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2019q4/data.parquet
    - **fields**:
      - revenue
      - gross_profit
    - **row_policy**: stock_code=600882.XSHG; quarter=2019q4; if_adjusted=0; selected earliest info_date=2020-04-29

</details>

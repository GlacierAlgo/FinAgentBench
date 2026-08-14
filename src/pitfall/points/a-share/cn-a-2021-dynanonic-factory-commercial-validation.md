# cn-a-2021-dynanonic-factory-commercial-validation

## Question

你处在2021-09-04收盘后的信息环境。德方纳米公告与曲靖市沾益区签订年产20万吨磷酸铁锂前驱体项目框架协议，预计总投资约8亿元、建设期24个月。请使用下方冻结资料，预测该工厂投资能否在2024年年报时达到target定义的后续商业验证。请综合项目所处协议阶段、资金和审批、既有扩产执行、行业需求与供给、产品价格和毛利、客户竞争、现金创造及产能消化能力。结果规则检验项目里程碑和公司层面的经营兑现，不声称该项目单独造成收入增长，也不是严格的反事实“最优投资”证明。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 德方纳米 (300769, SZSE)
- 信息截止 / As of: 2021-09-04
- 预测窗口结束 / Window end: 2025-04-30
- 目标事件 / Target: `announced_factory_commercial_validation_by_fy2024`
- 判定定义 / Definition: 工厂投资的后续商业验证而非单项目因果回报证明：建设进度、公司增长、毛利、经营现金流和产能利用率同时满足预先声明条件

#### 判定条件 / Criteria

- `announced_factory_schedule_validation >= 1` — 公告项目在原计划期附近被正式披露达到预定可使用状态或等价明确里程碑
- `revenue_cagr_baseline_to_outcome >= 0.2` — 公告前完整年度至结果年度营业收入复合年增长率不低于20%
- `gross_margin_outcome >= 0.1` — 结果年度综合毛利率不低于10%
- `operating_cash_flow_outcome > 0` — 结果年度经营活动产生的现金流量净额为正
- `capacity_utilization_outcome >= 0.75` — 结果年度相关制造业务披露的产能利用率不低于75%

<details>
<summary>冻结资料 / Frozen evidence (4)</summary>

### 德方纳米关于签订年产20万吨磷酸铁锂前驱体项目框架合作协议的公告

- Evidence ID: `precursor-framework-announcement`
- 发布日期 / Published: 2021-09-04
- 来源 / Source: 德方纳米法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2021-09-04/1210970944.PDF

公告披露，公司与曲靖市沾益区人民政府签订年产20万吨磷酸铁锂前驱体项目框架合作协议，预计总投资约8亿元、占地约260亩、建设期24个月，资金来源为自有或自筹资金。协议仅为框架安排，后续土地、审批、环境影响评价和具体投资仍存在不确定性。公司明确提示政策、市场、技术、资金和项目达产后产能利用不足等风险。大规模需求预期是正面信号，但框架协议与可使用产能之间仍有多道执行关口。

### 德方纳米2020年年度报告摘要：价格下行、毛利与扩产基础

- Evidence ID: `fy2020-margin-and-expansion-base`
- 发布日期 / Published: 2021-04-28
- 来源 / Source: 德方纳米法定年度报告摘要（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2021-04-28/1209838647.PDF

2020年公司营业收入约9.42亿元。受磷酸铁锂价格和原材料变化影响，主要产品平均销售价格同比下降超过30%，产品毛利率约10.18%，盈利缓冲已经较薄。报告披露既有产能建设曾受进度影响，在报告时点公司产能约8万吨，并计划继续扩张。需求恢复、技术积累和客户基础支持规模增长；售价波动、低毛利、多个项目并行带来的资本开支与爬坡压力，则使新增20万吨前驱体项目的商业兑现不能由行业景气直接推出。

### 德方纳米2021年半年度报告摘要：需求反弹与扩张压力

- Evidence ID: `h1-2021-demand-cash-and-risk`
- 发布日期 / Published: 2021-08-28
- 来源 / Source: 德方纳米法定半年度报告摘要（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2021-08-28/1210901706.PDF

2021年上半年新能源汽车与储能需求改善，公司销量和收入快速上升，为扩产提供强需求证据。与此同时，磷酸铁锂行业进入集中扩产期，产品价格随原材料和供需快速变化；新增项目需要持续融资、工程建设、客户认证和产能爬坡。公司已有多个正极材料项目推进，资源分配和建设执行能力应与单个框架协议区分。预测应同时权衡高增长窗口与供给扩张后价格、毛利和利用率回落的可能。

### 新能源车高景气下的锂资源紧平衡与集体扩产

- Evidence ID: `industry-news-tight-supply-and-expansion-wave`
- 发布日期 / Published: 2021-08-24
- 来源 / Source: 中国证券报
- URL: https://epaper.cs.com.cn/zgzqb/images/2021-08/24/A06/zqDB1124.pdf

中国证券报在项目公告前报道，新能源车产业链排产增加，磷酸铁锂扩产需求向好；同时锂资源现货供应紧张、短期供需处于紧平衡。报道列举多家锂电材料企业同步扩产，并引用政策目标说明长期需求空间。该产业证据同时给出正反两面：终端需求支持扩建，但原料紧张、成本上升和集体扩产意味着项目建成时可能面临供给竞争与毛利回落，不能用当期景气直接证明单个20万吨框架项目会按期商业兑现。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `announced_factory_commercial_validation_by_fy2024`
- 结果日期 / Resolved at: 2025-04-29

### 实际结果 / Realized outcome

- **observations**:
  - **announced_factory_schedule_validation**: 0
  - **revenue_baseline**: 942128306.07
  - **revenue_outcome**: 7612941216.46
  - **operating_cost_outcome**: 7965986554.15
  - **operating_cash_flow_outcome**: 143079360.69
  - **capacity_utilization_outcome**: 0.7727
- **derivations**:
  - **item 1**:
    - **metric**: revenue_cagr_baseline_to_outcome
    - **operation**: cagr
    - **inputs**:
      - revenue_baseline
      - revenue_outcome
    - **periods**: 4
    - **value**: 0.6860117852523948
  - **item 2**:
    - **metric**: gross_margin_outcome
    - **operation**: margin
    - **inputs**:
      - revenue_outcome
      - operating_cost_outcome
    - **value**: -0.04637436802042789

### 对应的题内资料 / Expected evidence

- `precursor-framework-announcement`
- `fy2020-margin-and-expansion-base`
- `h1-2021-demand-cash-and-risk`
- `industry-news-tight-supply-and-expansion-wave`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_business_decision_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 300769.XSHE
  - **ticker**: 300769
  - **name_as_of**: 德方纳米
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-09-04
  - **allowed_domains**:
    - cninfo.com.cn
    - cs.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=300769.XSHE; if_adjusted=0; earliest info_date per annual report; 2020 agent baseline; 2024 outcome
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **news_evidence_policy**: Contemporaneous news may supply industry demand, input-supply, and collective-capacity context; official filings and RQData remain label authority.
  - **causal_guardrail**: The label combines a disclosed project milestone with company-level commercial validation; it does not attribute company outcomes solely to this factory or prove counterfactual optimality.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 德方纳米2023年向特定对象发行股票审核问询函回复报告
    - **published_at**: 2023-09-20
    - **url**: https://static.cninfo.com.cn/finalpage/2023-09-20/1217904923.PDF
    - **fields**:
      - 年产20万吨磷酸铁锂前驱体项目建设进展
      - 远期规划与建设时间计划
  - **item 2**:
    - **type**: official_filing
    - **title**: 深圳市德方纳米科技股份有限公司2024年年度报告
    - **published_at**: 2025-04-29
    - **url**: https://static.cninfo.com.cn/finalpage/2025-04-29/1223370444.PDF
    - **fields**:
      - 营业收入
      - 营业成本
      - 经营活动现金流量净额
      - 磷酸盐系正极材料产能利用率
  - **item 3**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2020q4/data.parquet
      - data/db/rq_income_statement_pit/quarter=2024q4/data.parquet
      - data/db/rq_cash_flow_pit/quarter=2024q4/data.parquet
    - **fields**:
      - revenue
      - gross_profit
      - cash_flow_from_operating_activities
    - **row_policy**: stock_code=300769.XSHE; if_adjusted=0; earliest info_date

</details>

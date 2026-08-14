# cn-a-2019q3-performance-commitment-300276

## Question

你处在2019-10-19收盘后的信息环境。请使用下方冻结资料，预测三丰智能并购标的上海鑫燕隆2019年度承诺口径净利润是否会比2.582亿元承诺值低20%以上。需要区分上市公司合并利润、标的公司利润和承诺口径净利润，并综合上年承诺完成情况、在手订单、项目验收周期、汽车行业与现金流。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 三丰智能 (300276, SZSE)
- 信息截止 / As of: 2019-10-19
- 预测窗口结束 / Window end: 2020-06-30
- 目标事件 / Target: `material_performance_commitment_shortfall`
- 判定定义 / Definition: 并购标的鑫燕隆2019年度经专项审核的实际承诺口径净利润，比承诺净利润低20%以上

#### 判定条件 / Criteria

- `performance_commitment_shortfall_rate > 0.2` — （承诺净利润-实际承诺口径净利润）/承诺净利润超过20%

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 海通证券关于鑫燕隆2018年度业绩承诺完成情况的核查意见

- Evidence ID: `2018-commitment-met`
- 发布日期 / Published: 2019-04-16
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-04-16/1206021555.PDF

鑫燕隆2017、2018、2019年承诺口径净利润分别不低于1.801亿元、2.176亿元、2.582亿元。经专项审核，2018年实际承诺口径净利润2.1896亿元，比承诺多135.64万元，完成比例100.62%。2019承诺要求同比增长17.93%，仍有执行风险但上年不存在缺口。

### 三丰智能2019年第三季度报告：订单与项目验收

- Evidence ID: `2019-q3-orders-and-cash`
- 发布日期 / Published: 2019-10-19
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-10-19/1206993362.PDF

前三季度上市公司合并营业收入13.24亿元、归母净利润1.84亿元、经营活动现金流净额6,624.65万元；归母净利润同比上升0.49%。报告披露含税在手销售订单34.21亿元，并预计部分项目在第四季度验收。订单和验收计划支持承诺实现，但汽车项目验收节奏与合并口径差异仍需折价。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `material_performance_commitment_shortfall`
- 结果日期 / Resolved at: 2020-04-30

### 实际结果 / Realized outcome

- **observations**:
  - **promised_profit**: 258200000
  - **actual_commitment_basis_profit**: 260239200
- **derivations**:
  - **item 1**:
    - **metric**: performance_commitment_shortfall
    - **operation**: difference
    - **inputs**:
      - promised_profit
      - actual_commitment_basis_profit
    - **value**: -2039200
  - **item 2**:
    - **metric**: performance_commitment_shortfall_rate
    - **operation**: ratio
    - **inputs**:
      - performance_commitment_shortfall
      - promised_profit
    - **value**: -0.007897753679318357

### 对应的题内资料 / Expected evidence

- `2018-commitment-met`
- `2019-q3-orders-and-cash`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_traps_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 300276.XSHE
  - **ticker**: 300276
  - **name_as_of**: 三丰智能
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-10-19
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: official CNINFO filings; aliyun:/dev/data1/download_rqdata used only for listed-company financial cross-checks
  - **access**: read_only
  - **data_lake_gap**: The local snapshot has no populated performance-commitment table; the signed special assurance report is label authority.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0; Rust CLI; PDFium native text
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_special_assurance_report
    - **title**: 三丰智能业绩承诺完成情况审核报告
    - **published_at**: 2020-04-30
    - **url**: https://static.cninfo.com.cn/finalpage/2020-04-30/1207679569.PDF
    - **fields**:
      - 业绩承诺金额
      - 实际实现金额
      - 预测完成率

</details>

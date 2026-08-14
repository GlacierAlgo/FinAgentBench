# cn-a-2019q3-inventory-300442

## Question

你处在2019-10-26收盘后的信息环境。请使用下方冻结资料，预测普丽盛2019年年度报告确认的存货跌价损失是否会超过2019Q3归母权益的10%。重点综合存货/权益、未结转项目、订单与验收、行业需求、周转和现金流；不要把高存货余额或负现金流机械等同于跌价。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 普丽盛 (300442, SZSE)
- 信息截止 / As of: 2019-10-26
- 预测窗口结束 / Window end: 2020-06-30
- 目标事件 / Target: `material_inventory_write_down`
- 判定定义 / Definition: 2019年年度报告确认的存货跌价损失绝对值超过2019Q3归母权益的10%

#### 判定条件 / Criteria

- `inventory_write_down_to_q3_equity > 0.1` — 年度存货跌价损失占2019Q3归母权益比例超过10%

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 普丽盛2019年半年度报告：需求、项目与存货

- Evidence ID: `2019-h1-packaging-inventory`
- 发布日期 / Published: 2019-08-29
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-08-29/1206657839.PDF

2019年上半年营业收入2.97亿元，同比下降10.62%；经营活动现金流净额-1.21亿元。期末存货5.96亿元，占总资产38.24%，较年初增加。公司称宏观环境、下游需求萎缩和同行竞争加剧，但纸铝复合无菌灌装机收入增长，部分业务和资产处置也改善了利润。

### 普丽盛2019年第三季度报告：存货增加的项目解释

- Evidence ID: `2019-q3-unbilled-projects-control`
- 发布日期 / Published: 2019-10-26
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-10-26/1207020100.PDF

截至2019-09-30，存货6.59亿元，占归母权益7.46亿元的88.40%，较年初增加33.54%。公司解释增加主要来自普丽盛博雅汾酒项目和COMAN蒙牛项目已生产完成但尚未结转收入。前三季度营业收入4.20亿元、归母净利润1,894.25万元，经营活动现金流净额-1.25亿元；负现金流主要因销售回笼减少和采购支付增加。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `material_inventory_write_down`
- 结果日期 / Resolved at: 2020-05-23

### 实际结果 / Realized outcome

- **observations**:
  - **fy_inventory_write_down_loss**: 7211593.69
  - **q3_parent_equity**: 745803613.02
- **derivations**:
  - **item 1**:
    - **metric**: inventory_write_down_to_q3_equity
    - **operation**: ratio
    - **inputs**:
      - fy_inventory_write_down_loss
      - q3_parent_equity
    - **value**: 0.00966956121437643

### 对应的题内资料 / Expected evidence

- `2019-h1-packaging-inventory`
- `2019-q3-unbilled-projects-control`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_traps_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 300442.XSHE
  - **ticker**: 300442
  - **name_as_of**: 普丽盛
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-10-26
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_balance_sheet_pit
    - rq_income_statement_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=300442.XSHE; if_adjusted=0; first visible 2019q3 and 2019q4 filing rows
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0; Rust CLI; --no-ocr
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 普丽盛2019年年度报告
    - **published_at**: 2020-05-23
    - **url**: https://static.cninfo.com.cn/finalpage/2020-05-23/1207850503.PDF
    - **fields**:
      - 存货跌价损失
      - 存货跌价准备
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_balance_sheet_pit/quarter=2019q3/data.parquet
      - data/db/rq_income_statement_pit/quarter=2019q4/data.parquet
    - **fields**:
      - inventory
      - equity_parent_company
      - adjust_asset_impairment
    - **row_policy**: 300442.XSHE; if_adjusted=0; first visible filing row per quarter; official filing is authority for the inventory-only loss

</details>

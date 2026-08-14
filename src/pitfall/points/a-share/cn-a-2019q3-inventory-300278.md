# cn-a-2019q3-inventory-300278

## Question

你处在2019-10-29收盘后的信息环境。请使用下方冻结资料，预测华昌达2019年年度报告确认的存货跌价损失是否会超过2019Q3归母权益的10%。重点综合存货/权益、项目验收与订单、行业需求、周转和现金流、历史减值及公司特定经营事件；不要把高存货余额机械等同于跌价。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 华昌达 (300278, SZSE)
- 信息截止 / As of: 2019-10-29
- 预测窗口结束 / Window end: 2020-06-30
- 目标事件 / Target: `material_inventory_write_down`
- 判定定义 / Definition: 2019年年度报告确认的存货跌价损失绝对值超过2019Q3归母权益的10%

#### 判定条件 / Criteria

- `inventory_write_down_to_q3_equity > 0.1` — 年度存货跌价损失占2019Q3归母权益比例超过10%

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 华昌达2019年半年度报告（更新后）：汽车项目与经营压力

- Evidence ID: `2019-h1-auto-project-stress`
- 发布日期 / Published: 2019-09-20
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-09-20/1206940411.PDF

2019年上半年营业收入8.17亿元，同比下降32.34%，公司解释为汽车行业环境影响、完工验收项目减少；归母净利润-4.93亿元，经营现金流净额-4,497.82万元。期末存货11.03亿元，占总资产26.34%。报告已确认预计负债、商誉减值与固定资产处置损失，但这些项目不能直接替代对存货可变现净值的判断。

### 华昌达2019年第三季度报告：存货、收入与现金流

- Evidence ID: `2019-q3-inventory-overhang`
- 发布日期 / Published: 2019-10-29
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-10-29/1207029380.PDF

截至2019-09-30，存货11.31亿元，高于归母权益10.35亿元。前三季度营业收入11.18亿元，同比下降42.67%；归母净利润-6.71亿元；经营活动现金流净额仅686.50万元，同比下降89.52%。报告称营业收入下降主要受诉讼和汽车行业整体环境影响、完工验收项目同比减少。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `material_inventory_write_down`
- 结果日期 / Resolved at: 2020-06-30

### 实际结果 / Realized outcome

- **observations**:
  - **fy_inventory_write_down_loss**: 243175356.15
  - **q3_parent_equity**: 1034874994.38
- **derivations**:
  - **item 1**:
    - **metric**: inventory_write_down_to_q3_equity
    - **operation**: ratio
    - **inputs**:
      - fy_inventory_write_down_loss
      - q3_parent_equity
    - **value**: 0.2349804154807005

### 对应的题内资料 / Expected evidence

- `2019-h1-auto-project-stress`
- `2019-q3-inventory-overhang`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_traps_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 300278.XSHE
  - **ticker**: 300278
  - **name_as_of**: 华昌达
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-10-29
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_balance_sheet_pit
    - rq_income_statement_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=300278.XSHE; if_adjusted=0; first visible 2019q3 snapshot; first complete FY2019 filing row
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0; Rust CLI; --no-ocr
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 华昌达2019年年度报告
    - **published_at**: 2020-06-30
    - **url**: https://static.cninfo.com.cn/finalpage/2020-06-30/1207968770.PDF
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
    - **row_policy**: 300278.XSHE; if_adjusted=0; first visible Q3 row and first complete FY2019 row; official filing is authority for the inventory-only loss

</details>

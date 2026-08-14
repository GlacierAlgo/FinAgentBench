# cn-a-2019q3-goodwill-002425

## Question

你处在2019-10-25收盘后的信息环境。请使用下方冻结资料检索当时已经公开的正式披露，预测凯撒文化在2019年年度报告中确认的资产减值损失是否会超过2019Q3归母权益的10%。商誉不计提折旧或摊销；目标是减值事件。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 凯撒文化 (002425, SZSE)
- 信息截止 / As of: 2019-10-25
- 预测窗口结束 / Window end: 2020-06-30
- 目标事件 / Target: `material_asset_impairment`
- 判定定义 / Definition: 2019年年度报告确认的资产减值损失绝对值超过2019Q3归母权益的10%
- 阈值 / Threshold: 0.1
- 分母 / Denominator: 2019Q3归属于母公司股东权益

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 凯撒文化2019年第三季度报告全文

- Evidence ID: `q3-report`
- 发布日期 / Published: 2019-10-25
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-10-25/1207012540.PDF

截至2019-09-30，合并口径商誉2,235,166,768.36元，总资产4,984,064,059.09元，归属于母公司股东权益4,074,066,394.03元。2019年1-9月营业收入603,608,196.57元，归母净利润203,120,223.17元，经营活动现金流净额134,568,590.79元。

### 凯撒文化2019年半年度报告：商誉附注

- Evidence ID: `h1-goodwill-note`
- 发布日期 / Published: 2019-08-28
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-08-28/1206651906.PDF

半年报披露商誉原值2,235,166,768.36元，来自酷牛互动665,141,049.85元、杭州幻文466,879,589.27元、天上友嘉1,103,146,129.24元。商誉减值准备表未列示期初或本期计提金额。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `material_asset_impairment`
- 结果日期 / Resolved at: 2020-04-29

### 实际结果 / Realized outcome

- **asset_impairment_loss**: 79003054.76
- **pre_as_of_equity**: 4074066394.03
- **ratio**: 0.019391695450954954

### 对应的题内资料 / Expected evidence

- `q3-report`
- `h1-goodwill-note`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_walk_forward_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002425.XSHE
  - **ticker**: 002425
  - **name_as_of**: 凯撒文化
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-10-25
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **row_policy**: if_adjusted=0; earliest info_date per stock_code; 2019q3 agent snapshot; 2019q4 outcome
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 凯撒文化2019年年度报告
    - **published_at**: 2020-04-29
    - **url**: https://static.cninfo.com.cn/finalpage/2020-04-29/1207663699.PDF
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_balance_sheet_pit/quarter=2019q3/data.parquet
      - data/db/rq_income_statement_pit/quarter=2019q4/data.parquet
    - **fields**:
      - equity_parent_company
      - adjust_asset_impairment
    - **row_policy**: stock_code=002425.XSHE; if_adjusted=0; earliest info_date

</details>

# cn-a-2019q3-goodwill-002739

## Question

你处在2019-10-30收盘后的信息环境。请使用下方冻结资料检索当时已经公开的正式披露，预测万达电影在2019年年度报告中确认的资产减值损失是否会超过2019Q3归母权益的10%。商誉不计提折旧或摊销；目标是减值事件。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 万达电影 (002739, SZSE)
- 信息截止 / As of: 2019-10-30
- 预测窗口结束 / Window end: 2020-06-30
- 目标事件 / Target: `material_asset_impairment`
- 判定定义 / Definition: 2019年年度报告确认的资产减值损失绝对值超过2019Q3归母权益的10%
- 阈值 / Threshold: 0.1
- 分母 / Denominator: 2019Q3归属于母公司股东权益

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 万达电影2019年第三季度报告全文

- Evidence ID: `q3-report`
- 发布日期 / Published: 2019-10-30
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-10-30/1207035936.PDF

截至2019-09-30，合并口径商誉13,452,903,180.32元，总资产32,078,517,528.61元，归属于母公司股东权益19,517,360,597.40元。2019年1-9月营业收入11,594,141,839.57元，归母净利润829,472,367.20元，经营活动现金流净额1,043,821,491.97元。报告列示营业收入较调整后上年同期下降7.45%，归母净利润下降57.25%，经营现金流净额下降45.78%。

### 万达电影2019年半年度报告：商誉附注

- Evidence ID: `h1-goodwill-note`
- 发布日期 / Published: 2019-08-21
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-08-21/1206549015.PDF

半年报披露商誉期末原值13,464,245,557.32元，主要资产组包括HG Holdco 3,312,256,972.03元、互爱互动2,307,254,072.13元、影时光相关资产组2,125,226,776.59元、万达传媒1,033,059,987.53元、上海骋亚984,595,676.99元、新媒诚品618,351,873.53元等。公司说明每年末执行商誉减值测试并估计可收回金额。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `material_asset_impairment`
- 结果日期 / Resolved at: 2020-04-22

### 实际结果 / Realized outcome

- **asset_impairment_loss**: 5897853464.62
- **pre_as_of_equity**: 19517360597.4
- **ratio**: 0.30218499244235314

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
  - **order_book_id**: 002739.XSHE
  - **ticker**: 002739
  - **name_as_of**: 万达电影
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-10-30
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
    - **title**: 万达电影2019年年度报告
    - **published_at**: 2020-04-22
    - **url**: https://static.cninfo.com.cn/finalpage/2020-04-22/1207551036.PDF
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_balance_sheet_pit/quarter=2019q3/data.parquet
      - data/db/rq_income_statement_pit/quarter=2019q4/data.parquet
    - **fields**:
      - equity_parent_company
      - adjust_asset_impairment
    - **row_policy**: stock_code=002739.XSHE; if_adjusted=0; earliest info_date

</details>

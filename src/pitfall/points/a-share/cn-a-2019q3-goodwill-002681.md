# cn-a-2019q3-goodwill-002681

## Question

你处在2019-10-28收盘后的信息环境。请使用下方冻结资料检索当时已经公开的正式披露，预测奋达科技在2019年年度报告中确认的资产减值损失是否会超过2019Q3归母权益的10%。商誉不计提折旧或摊销；目标是减值事件。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 奋达科技 (002681, SZSE)
- 信息截止 / As of: 2019-10-28
- 预测窗口结束 / Window end: 2020-06-30
- 目标事件 / Target: `material_asset_impairment`
- 判定定义 / Definition: 2019年年度报告确认的资产减值损失绝对值超过2019Q3归母权益的10%
- 阈值 / Threshold: 0.1
- 分母 / Denominator: 2019Q3归属于母公司股东权益

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 奋达科技2019年第三季度报告全文

- Evidence ID: `q3-report`
- 发布日期 / Published: 2019-10-28
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-10-28/1207020025.PDF

截至2019-09-30，合并口径商誉2,799,747,096.97元，总资产7,572,838,613.19元，归属于母公司股东权益5,358,780,810.08元。2019年1-9月营业收入2,495,281,956.18元，归母净利润134,772,536.34元，经营活动现金流净额501,641,977.78元。

### 奋达科技2019年半年度报告：商誉附注

- Evidence ID: `h1-goodwill-note`
- 发布日期 / Published: 2019-08-23
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-08-23/1206555899.PDF

半年报披露商誉原值3,455,523,069.60元，集中于欧朋达科技910,093,398.51元和深圳市富诚达科技2,545,429,671.09元。与三季报披露的商誉净额相比，原值高度集中在两个并购资产组；年末仍需依据资产组可收回金额进行减值测试。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `material_asset_impairment`
- 结果日期 / Resolved at: 2020-04-30

### 实际结果 / Realized outcome

- **asset_impairment_loss**: 3152473982.19
- **pre_as_of_equity**: 5358780810.08
- **ratio**: 0.5882819420902826

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
  - **order_book_id**: 002681.XSHE
  - **ticker**: 002681
  - **name_as_of**: 奋达科技
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-10-28
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
    - **title**: 奋达科技2019年年度报告
    - **published_at**: 2020-04-30
    - **url**: https://static.cninfo.com.cn/finalpage/2020-04-30/1207687470.PDF
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_balance_sheet_pit/quarter=2019q3/data.parquet
      - data/db/rq_income_statement_pit/quarter=2019q4/data.parquet
    - **fields**:
      - equity_parent_company
      - adjust_asset_impairment
    - **row_policy**: stock_code=002681.XSHE; if_adjusted=0; earliest info_date

</details>

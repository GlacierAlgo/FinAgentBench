# cn-a-2019q3-goodwill-300058

## Question

你处在2019-10-22收盘后的信息环境。请使用下方冻结资料检索当时已经公开的正式披露，预测蓝色光标在2019年年度报告中确认的资产减值损失是否会超过2019Q3归母权益的10%。商誉不计提折旧或摊销；目标是减值事件。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 蓝色光标 (300058, SZSE)
- 信息截止 / As of: 2019-10-22
- 预测窗口结束 / Window end: 2020-06-30
- 目标事件 / Target: `material_asset_impairment`
- 判定定义 / Definition: 2019年年度报告确认的资产减值损失绝对值超过2019Q3归母权益的10%
- 阈值 / Threshold: 0.1
- 分母 / Denominator: 2019Q3归属于母公司股东权益

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 蓝色光标2019年第三季度报告全文

- Evidence ID: `q3-report`
- 发布日期 / Published: 2019-10-22
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-10-22/1206998762.PDF

截至2019-09-30，合并口径商誉4,910,805,952.73元，总资产18,617,738,296.70元，归属于母公司股东权益8,708,205,806.75元。2019年1-9月营业收入19,687,602,992.67元，归母净利润627,998,166.59元，经营活动现金流净额357,365,436.42元。

### 蓝色光标2019年半年度报告：商誉附注

- Evidence ID: `h1-goodwill-note`
- 发布日期 / Published: 2019-08-23
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-08-23/1206556586.PDF

半年报披露商誉原值5,153,276,956.06元，分散于Domob、多盟智胜、Vision 7、东方博杰、Madhouse、We Are Very Social、今久广告等多个资产组；已计提商誉减值准备289,113,134.37元。公司说明年末按预计未来现金流量现值测试，资产组可收回金额低于账面价值时确认减值。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `material_asset_impairment`
- 结果日期 / Resolved at: 2020-04-28

### 实际结果 / Realized outcome

- **asset_impairment_loss**: 26037927.96
- **pre_as_of_equity**: 8708205806.75
- **ratio**: 0.0029900450836631808

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
  - **order_book_id**: 300058.XSHE
  - **ticker**: 300058
  - **name_as_of**: 蓝色光标
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-10-22
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
    - **title**: 蓝色光标2019年年度报告
    - **published_at**: 2020-04-28
    - **url**: https://static.cninfo.com.cn/finalpage/2020-04-28/1207639736.PDF
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_balance_sheet_pit/quarter=2019q3/data.parquet
      - data/db/rq_income_statement_pit/quarter=2019q4/data.parquet
    - **fields**:
      - equity_parent_company
      - adjust_asset_impairment
    - **row_policy**: stock_code=300058.XSHE; if_adjusted=0; earliest info_date

</details>

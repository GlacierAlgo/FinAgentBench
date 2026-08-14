# cn-a-2019q3-receivables-300461

## Question

你处在2019-10-29收盘后的信息环境。请使用下方冻结资料，预测田中精机2019年报累计信用减值损失相对三季报已确认金额的新增部分，是否会超过2019Q3归母权益的20%。重点综合应收账款/营收、现金回收、客户与子公司质量、账龄和已经出现的损失信号；不要把高应收余额机械等同于新增坏账。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 田中精机 (300461, SZSE)
- 信息截止 / As of: 2019-10-29
- 预测窗口结束 / Window end: 2020-06-30
- 目标事件 / Target: `large_incremental_q4_credit_impairment`
- 判定定义 / Definition: 2019年报累计信用减值损失减去前三季度已确认信用减值损失后的新增金额，超过2019Q3归母权益的20%

#### 判定条件 / Criteria

- `incremental_credit_impairment_to_q3_equity > 0.2` — 第四季度新增信用减值损失占2019Q3归母权益比例超过20%

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 田中精机2019年半年度报告：应收风险与现金回收

- Evidence ID: `2019-h1-receivables-warning`
- 发布日期 / Published: 2019-08-30
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-08-30/1206730549.PDF

2019年上半年营业收入3.33亿元、经营活动现金流净额仅79.95万元。期末应收账款3.62亿元，占流动资产42.48%；半年报明确提示应收账款不能及时收回和坏账损失风险，并披露信用减值损失7,805.43万元，其中应收账款坏账损失6,247.54万元、长期应收款坏账损失1,172.48万元。

### 田中精机2019年第三季度报告（更新后）：收入、应收与现金流背离

- Evidence ID: `2019-q3-receivables-divergence`
- 发布日期 / Published: 2019-10-29
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-10-29/1207035176.PDF

截至2019-09-30，应收账款3.50亿元，而前三季度营业收入4.46亿元，归母权益1.61亿元。前三季度经营活动现金流净额1,795.27万元，同比下降78.02%，报告解释为销售商品收到的现金减少。公司预计全年累计净利润可能亏损，原因包括信用减值、资产减值和公允价值变动；这些信号支持风险判断，但目标只计算三季报之后新增的信用减值。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `large_incremental_q4_credit_impairment`
- 结果日期 / Resolved at: 2020-04-29

### 实际结果 / Realized outcome

- **observations**:
  - **fy_credit_impairment_loss**: 203509634.42
  - **q3_credit_impairment_loss**: 86537669.39
  - **q3_parent_equity**: 160765575.9
- **derivations**:
  - **item 1**:
    - **metric**: incremental_credit_impairment_loss
    - **operation**: difference
    - **inputs**:
      - fy_credit_impairment_loss
      - q3_credit_impairment_loss
    - **value**: 116971965.03
  - **item 2**:
    - **metric**: incremental_credit_impairment_to_q3_equity
    - **operation**: ratio
    - **inputs**:
      - incremental_credit_impairment_loss
      - q3_parent_equity
    - **value**: 0.7275933568188709

### 对应的题内资料 / Expected evidence

- `2019-h1-receivables-warning`
- `2019-q3-receivables-divergence`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_traps_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 300461.XSHE
  - **ticker**: 300461
  - **name_as_of**: 田中精机
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
  - **row_policy**: stock_code=300461.XSHE; if_adjusted=0; first visible 2019q3 and 2019q4 filing rows
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0; Rust CLI; --no-ocr
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 田中精机2019年年度报告
    - **published_at**: 2020-04-29
    - **url**: https://static.cninfo.com.cn/finalpage/2020-04-29/1207666231.PDF
    - **fields**:
      - 信用减值损失
      - 应收账款坏账损失
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_balance_sheet_pit/quarter=2019q3/data.parquet
      - data/db/rq_income_statement_pit/quarter=2019q3/data.parquet
      - data/db/rq_income_statement_pit/quarter=2019q4/data.parquet
    - **fields**:
      - equity_parent_company
      - adjust_credit_asset_impairment
    - **row_policy**: 300461.XSHE; if_adjusted=0; first visible filing row per quarter; loss signs normalized to positive magnitudes

</details>

# cn-a-2019q3-receivables-300455

## Question

你处在2019-10-30收盘后的信息环境。请使用下方冻结资料，预测康拓红外2019年报累计信用减值损失相对三季报已确认金额的新增部分，是否会超过2019Q3归母权益的20%。重点综合应收账款/营收、现金回收、客户性质、结算模式、账龄和已确认损失；不要把高应收余额机械等同于新增坏账。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 康拓红外 (300455, SZSE)
- 信息截止 / As of: 2019-10-30
- 预测窗口结束 / Window end: 2020-06-30
- 目标事件 / Target: `large_incremental_q4_credit_impairment`
- 判定定义 / Definition: 2019年报累计信用减值损失减去前三季度已确认信用减值损失后的新增金额，超过2019Q3归母权益的20%

#### 判定条件 / Criteria

- `incremental_credit_impairment_to_q3_equity > 0.2` — 第四季度新增信用减值损失占2019Q3归母权益比例超过20%

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 康拓红外2019年半年度报告：铁路客户结算与现金流

- Evidence ID: `2019-h1-state-customer-context`
- 发布日期 / Published: 2019-07-30
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-07-30/1206480969.PDF

2019年上半年营业收入1.07亿元、经营活动现金流净额2,869.45万元。期末应收账款2.89亿元，占总资产34.40%。公司提示铁路行业业务和结算模式导致应收账款普遍较高，客户主要为全国铁路局集团；高余额带来流动性和坏账风险，但客户属性、正经营现金流和稳定盈利构成重要反向证据。

### 康拓红外2019年第三季度报告：高应收但盈利稳定

- Evidence ID: `2019-q3-high-ar-control`
- 发布日期 / Published: 2019-10-30
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-10-30/1207038622.PDF

截至2019-09-30，应收账款3.24亿元，约为前三季度营业收入1.66亿元的1.95倍；归母权益7.65亿元。前三季度归母净利润4,407.76万元，同比增长2.03%，经营活动现金流净额710.15万元。报表未列示累计信用减值损失，但高应收/营收比仍构成表面上很强的风险信号，要求模型进一步判断客户质量与回款周期。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `large_incremental_q4_credit_impairment`
- 结果日期 / Resolved at: 2020-04-28

### 实际结果 / Realized outcome

- **observations**:
  - **fy_credit_impairment_loss**: 2085612.83
  - **q3_credit_impairment_loss**: 0
  - **q3_parent_equity**: 765478113.33
- **derivations**:
  - **item 1**:
    - **metric**: incremental_credit_impairment_loss
    - **operation**: difference
    - **inputs**:
      - fy_credit_impairment_loss
      - q3_credit_impairment_loss
    - **value**: 2085612.83
  - **item 2**:
    - **metric**: incremental_credit_impairment_to_q3_equity
    - **operation**: ratio
    - **inputs**:
      - incremental_credit_impairment_loss
      - q3_parent_equity
    - **value**: 0.002724588454824816

### 对应的题内资料 / Expected evidence

- `2019-h1-state-customer-context`
- `2019-q3-high-ar-control`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_traps_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 300455.XSHE
  - **ticker**: 300455
  - **name_as_of**: 康拓红外
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-10-30
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_balance_sheet_pit
    - rq_income_statement_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=300455.XSHE; if_adjusted=0; first visible 2019q3 and 2019q4 filing rows
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0; Rust CLI; --no-ocr
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 康拓红外2019年年度报告
    - **published_at**: 2020-04-28
    - **url**: https://static.cninfo.com.cn/finalpage/2020-04-28/1207645014.PDF
    - **fields**:
      - 信用减值损失
      - 应收账款坏账准备
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_balance_sheet_pit/quarter=2019q3/data.parquet
      - data/db/rq_income_statement_pit/quarter=2019q3/data.parquet
      - data/db/rq_income_statement_pit/quarter=2019q4/data.parquet
    - **fields**:
      - equity_parent_company
      - adjust_credit_asset_impairment
    - **row_policy**: 300455.XSHE; if_adjusted=0; first visible filing row per quarter; absent Q3 credit impairment normalized to zero; loss signs normalized to positive magnitudes

</details>

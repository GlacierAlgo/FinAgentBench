# cn-a-2023q3-st-transition-002786

## Question

你处在2023-10-31收盘后的信息环境，银宝山新当时尚未被实施ST或*ST。请使用下方冻结资料，结合交易所风险警示规则、前三季度与历史年报、盈利持续性、净资产缓冲和可能的非经常性损益，预测公司是否会在2024-06-30前首次被实施ST或*ST。不要把连续亏损或低净资产机械等同于ST；需要识别可能触发或避免触发的具体规则。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 银宝山新 (002786, SZSE)
- 信息截止 / As of: 2023-10-31
- 预测窗口结束 / Window end: 2024-06-30
- 目标事件 / Target: `new_st_or_star_st_by_2024_06_30`
- 判定定义 / Definition: 公司在as-of时未被实施ST或*ST，并在预测窗口内首次被实施ST或*ST风险警示

#### 判定条件 / Criteria

- `new_st_or_star_st_flag >= 1` — 预测窗口内出现新的ST或*ST状态记为1，否则记为0

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 银宝山新2022年年度报告：连续亏损但未触发风险警示

- Evidence ID: `2022-annual-losses`
- 发布日期 / Published: 2023-04-29
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2023-04-29/1216695501.PDF

2022年营业收入25.97亿元、归母净利润-2.58亿元、扣非归母净利润-2.49亿元；年末归母净资产2.41亿元，同比下降51.77%。公司最近三个会计年度扣非前后净利润孰低均为负，但年报勾选最近一年审计报告未显示持续经营能力存在不确定性，且扣除后营业收入25.25亿元。

### 银宝山新2023年三季度报告：亏损与低净资产

- Evidence ID: `2023-q3-thin-equity-control`
- 发布日期 / Published: 2023-10-31
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2023-10-31/1218203248.PDF

截至2023-09-30，公司总资产37.06亿元，归母净资产仅9,532.73万元，较上年末下降60.49%。前三季度营业收入17.21亿元、归母净利润-1.43亿元、扣非归母净利润-1.70亿元，经营现金流净额5,892.07万元。该案例与汉马科技一样有连续亏损和薄净资产，但风险警示取决于全年审计结果与规则触发项，而不是风险特征数量。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `new_st_or_star_st_by_2024_06_30`
- 结果日期 / Resolved at: 2024-04-29

### 实际结果 / Realized outcome

- **observations**:
  - **new_st_or_star_st_flag**: 0
  - **fy2023_parent_equity**: 493636920.63
  - **fy2023_parent_net_profit**: 244790653.93
- **derivations**:


### 对应的题内资料 / Expected evidence

- `2022-annual-losses`
- `2023-q3-thin-equity-control`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_traps_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002786.XSHE
  - **ticker**: 002786
  - **name_as_of**: 银宝山新
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2023-10-31
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - is_st
    - rq_balance_sheet_pit
    - rq_income_statement_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=002786.XSHE; if_adjusted=0; first visible 2023q3 row; is_st at 2023-10-31 and 2024-06-28
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0; Rust CLI; --no-ocr
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 银宝山新2023年年度报告
    - **published_at**: 2024-04-29
    - **url**: https://static.cninfo.com.cn/finalpage/2024-04-29/1219865365.PDF
    - **fields**:
      - 归属于上市公司股东的净资产
      - 归属于上市公司股东的净利润
      - 非标准审计意见提示
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/is_st.parquet
      - data/db/rq_balance_sheet_pit/quarter=2023q4/data.parquet
      - data/db/rq_income_statement_pit/quarter=2023q4/data.parquet
    - **fields**:
      - is_st
      - equity_parent_company
      - net_profit_parent_company
    - **row_policy**: 002786.XSHE; is_st false at both 2023-10-31 and 2024-06-28; first visible FY2023 filing row

</details>

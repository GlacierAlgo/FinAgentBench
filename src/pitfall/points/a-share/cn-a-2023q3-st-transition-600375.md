# cn-a-2023q3-st-transition-600375

## Question

你处在2023-10-28收盘后的信息环境，汉马科技当时尚未被实施ST或*ST。请使用下方冻结资料，结合交易所风险警示规则、前三季度与历史年报、盈利持续性、净资产缓冲和审计风险，预测公司是否会在2024-06-30前首次被实施ST或*ST。不要把亏损本身机械等同于ST；需要识别可能触发的具体规则。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 汉马科技 (600375, SSE)
- 信息截止 / As of: 2023-10-28
- 预测窗口结束 / Window end: 2024-06-30
- 目标事件 / Target: `new_st_or_star_st_by_2024_06_30`
- 判定定义 / Definition: 公司在as-of时未被实施ST或*ST，并在预测窗口内首次被实施ST或*ST风险警示

#### 判定条件 / Criteria

- `new_st_or_star_st_flag >= 1` — 预测窗口内出现新的ST或*ST状态记为1，否则记为0

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 汉马科技2022年年度报告：连续亏损与净资产缓冲

- Evidence ID: `2022-annual-risk-buffer`
- 发布日期 / Published: 2023-03-31
- 来源 / Source: 巨潮资讯（上交所法定信息披露）
- URL: https://static.cninfo.com.cn/finalpage/2023-03-31/1216278640.PDF

2022年营业收入34.29亿元，同比下降35.55%；归属于上市公司股东的净利润-14.66亿元，2021年为-13.36亿元；2022年末归母净资产仅1.70亿元，同比下降89.70%。报告显示连续大额亏损已显著压缩净资产缓冲，但截至该年末归母净资产仍为正。

### 汉马科技2023年第三季度报告：净资产接近耗尽

- Evidence ID: `2023-q3-thin-equity`
- 发布日期 / Published: 2023-10-28
- 来源 / Source: 巨潮资讯（上交所法定信息披露）
- URL: https://static.cninfo.com.cn/finalpage/2023-10-28/1218185724.PDF

截至2023-09-30，公司总资产87.80亿元，归属于上市公司股东的所有者权益仅2,368.64万元，较上年末下降83.36%。2023年前三季度营业收入26.55亿元、归母净利润-1.28亿元、扣非归母净利润-5.78亿元；经营现金流净额3.90亿元。单季经营改善和正经营现金流构成反向证据，但极薄的净资产意味着第四季度损失或年审调整可能改变风险警示结论。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `new_st_or_star_st_by_2024_06_30`
- 结果日期 / Resolved at: 2024-04-01

### 实际结果 / Realized outcome

- **observations**:
  - **new_st_or_star_st_flag**: 1
  - **fy2023_parent_equity**: -814580276.71
  - **fy2023_parent_net_profit**: -962688930.49
- **derivations**:


### 对应的题内资料 / Expected evidence

- `2022-annual-risk-buffer`
- `2023-q3-thin-equity`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_traps_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600375.XSHG
  - **ticker**: 600375
  - **name_as_of**: 汉马科技
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2023-10-28
  - **allowed_domains**:
    - cninfo.com.cn
    - sse.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - is_st
    - special_treatment_info
    - rq_balance_sheet_pit
    - rq_income_statement_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=600375.XSHG; if_adjusted=0; first visible 2023q3 row; is_st at 2023-10-31 and 2024-06-28
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0; Rust CLI; --no-ocr
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 汉马科技2023年年度报告
    - **published_at**: 2024-03-29
    - **url**: https://static.cninfo.com.cn/finalpage/2024-03-29/1219443117.PDF
    - **fields**:
      - 归属于上市公司股东的净资产
      - 归属于上市公司股东的净利润
  - **item 2**:
    - **type**: official_risk_warning_notice
    - **title**: 关于公司股票被实施退市风险警示及叠加其他风险警示暨公司股票停牌的公告
    - **published_at**: 2024-03-29
    - **url**: https://static.cninfo.com.cn/finalpage/2024-03-29/1219443094.PDF
    - **effective_at**: 2024-04-01
  - **item 3**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/is_st.parquet
      - data/db/special_treatment_info.parquet
      - data/db/rq_balance_sheet_pit/quarter=2023q4/data.parquet
    - **fields**:
      - is_st
      - type
      - description
      - equity_parent_company
    - **row_policy**: 600375.XSHG; is_st false at 2023-10-31 and true at 2024-06-28; special treatment effective 2024-04-01

</details>

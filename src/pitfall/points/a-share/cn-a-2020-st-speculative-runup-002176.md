# cn-a-2020-st-speculative-runup-002176

## Question

你处在2020-04-30收盘后的信息环境，今天是江特电机本轮风险警示事件首次以*ST江特交易的日期。请使用下方冻结资料预测未来365个自然日是否出现target定义的异常大幅收盘上涨。连续两年巨亏、负经营现金流、短债高于现金并伴随商誉与资产减值；同时公司拟退出汽车、聚焦电机和锂盐并拥有锂云母资源。请把资产负债表生存、产能执行、锂价周期和高弹性资源叙事分别建模，不能以“资源股会反转”替代点时概率判断。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST江特 (002176, SZSE)
- 信息截止 / As of: 2020-04-30
- 预测窗口结束 / Window end: 2021-04-30
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以当前风险警示事件首次生效交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改、重整、资产题材或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 江特电机2019年报摘要：连续巨亏、现金流承压与大额减值

- Evidence ID: `annual-two-year-losses-cash-and-impairments`
- 发布日期 / Published: 2020-04-29
- 来源 / Source: 巨潮资讯法定年报摘要及只读RQData点时记录
- URL: https://static.cninfo.com.cn/finalpage/2020-04-29/1207666795.PDF

2019年营业收入25.945亿元、归母净利润-20.244亿元、扣非归母净利润-14.757亿元；经营活动现金流净额-9,923.58万元。期末货币资金4.7058亿元，而短期借款17.569亿元、流动负债36.503亿元；融资现金流净额-11.372亿元。公司受新能源汽车补贴退坡、碳酸锂价格下跌、汽车和电机子公司亏损影响，并计提商誉及其他资产减值。高资源属性与严重财务压力在同一快照中并存。

### 江特电机退市风险警示公告：连续两年亏损并计划退出汽车、聚焦锂盐与电机

- Evidence ID: `star-st-notice-lithium-optionality-and-execution-risk`
- 发布日期 / Published: 2020-04-29
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-04-29/1207666802.PDF

公司2018年、2019年经审计归母净利润分别为-16.6048亿元和-20.2445亿元，自2020年4月30日起实施*ST。董事会称亏损来自补贴退坡、锂价下跌、汽车及电机业务下滑、商誉减值和资产处置，并提出逐步退出汽车产业、聚焦电机和锂盐，释放宜丰矿区锂资源加工能力。资源与转型计划提供可选性，但公告中的计划不等于产量、价格、融资或扭亏已经兑现。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2021-04-30

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 21.647876
  - **peak_adjusted_close_365d**: 98.128396
  - **as_of_510300_close**: 3.908
  - **stock_close_on_max_excess_date**: 98.128396
  - **etf_close_on_max_excess_date**: 5.089
  - **common_trading_sessions**: 244
  - **risk_warning_removed_by_window_end**: 1
- **derivations**:
  - **item 1**:
    - **metric**: max_adjusted_close_return_365d
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - peak_adjusted_close_365d
    - **value**: 3.5329341317365266
  - **item 2**:
    - **metric**: stock_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - stock_close_on_max_excess_date
    - **value**: 3.5329341317365266
  - **item 3**:
    - **metric**: etf_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_510300_close
      - etf_close_on_max_excess_date
    - **value**: 0.3022006141248721
  - **item 4**:
    - **metric**: max_excess_return_vs_510300_365d
    - **operation**: difference
    - **inputs**:
      - stock_return_on_max_excess_date
      - etf_return_on_max_excess_date
    - **value**: 3.2307335176116547

### 对应的题内资料 / Expected evidence

- `annual-two-year-losses-cash-and-impairments`
- `star-st-notice-lithium-optionality-and-execution-risk`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002176.XSHE
  - **ticker**: 002176
  - **name_as_of**: *ST江特
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-04-30
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - rq_adj_bwd_price_daily
    - etf_raw_price_daily
    - is_st
  - **row_policy**: stock_code=002176.XSHE; quarter=2019q4; info_date=2020-04-29; if_adjusted=0; current warning episode starts 2020-04-30; daily prices 2020-04-30 through 2021-04-30; benchmark=510300.XSHG
  - **st_cause_taxonomy**: operating_financial/two_year_losses+goodwill_and_asset_impairments
  - **matching_group**: current-risk-warning-episode-market-path-365d-v1
  - **matching_role**: event_deep_loss_lithium_optionality
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **annual_report_summary**: b2425e125808f23b418c94cc8c391750852f72d2fcbbea60129ccf0845b3f7b2
    - **st_notice**: c4fbad61e45f6a34c386c70a5a3c578902355ee22f35e768346866b055238aaf
  - **news_evidence_policy**: Only documents published no later than as_of enter the frozen corpus. Filings and point-in-time data remain authoritative; narratives are hypotheses, never outcome labels.
  - **outcome_label_policy**: Stock backward-adjusted closes and raw 510300 closes are aligned by trade_date; maxima use available closing observations only over the predeclared 365-calendar-day window. Suspension or delisting may shorten the observed trading path and is not imputed.
  - **causal_guardrail**: The label measures an ex post market path, not whether ST designation, remediation, restructuring, scandal severity, shell value, commodity exposure, or fundamentals caused that path.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: rqdata_daily_price
    - **paths**:
      - data/db/rq_adj_bwd_price_daily/trade_date=YYYY-MM-DD/data.parquet
      - data/db/etf_raw_price_daily/trade_date=YYYY-MM-DD/data.parquet
    - **window**: 2020-04-30/2021-04-30
    - **stock_code**: 002176.XSHE
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2021-04-19
    - **max_excess_date**: 2021-04-19
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
    - **observation_policy**: Use aligned closing observations that exist inside the fixed calendar window; do not impute prices across suspension or after delisting.
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **current_warning_episode_start**: 2020-04-30
    - **risk_warning_removed_by_window_end**: true

</details>

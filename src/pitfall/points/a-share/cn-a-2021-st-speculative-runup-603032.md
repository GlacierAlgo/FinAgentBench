# cn-a-2021-st-speculative-runup-603032

## Question

你处在2021-04-28收盘后的信息环境，今天是德新交运本轮风险警示事件首次以*ST德新交易的日期。请使用下方冻结资料预测未来365个自然日是否出现target定义的异常大幅收盘上涨。公司因亏损且扣除后收入不足1亿元戴帽，但净资产为正、负债很低；戴帽前股价已连续涨停，静态/动态市盈率约300.8/2079倍。请区分低杠杆生存能力、微小收入基数、转型可选性、已透支估值和交易拥挤，不因先前涨停直接外推未来翻倍。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST德新 (603032, SSE)
- 信息截止 / As of: 2021-04-28
- 预测窗口结束 / Window end: 2022-04-28
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以当前风险警示事件首次生效交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改、重整、资产题材或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 德新交运2020年报摘要：收入不足一亿元、扣非连续亏损但资产负债表较轻

- Evidence ID: `annual-small-revenue-loss-and-low-leverage`
- 发布日期 / Published: 2021-04-27
- 来源 / Source: 巨潮资讯法定年报摘要及只读RQData点时记录
- URL: https://static.cninfo.com.cn/finalpage/2021-04-27/1209819501.PDF

2020年营业收入5,143.40万元，同比下降48.05%；归母净利润-861.72万元，扣非归母净利润-3,225.06万元，经营活动现金流净额-1,070.43万元。期末总资产8.0379亿元、归母净资产6.7343亿元；只读PIT记录显示货币资金7,340.83万元、流动负债4,365.02万元、总负债1.3013亿元。利润为负且扣除后营业收入低于1亿元触发退市风险警示，但低杠杆与仍为正的净资产使其不同于典型资不抵债样本。

### 德新交运异常波动公告：戴帽风险前已连续涨停且估值极端

- Evidence ID: `pre-st-valuation-and-limit-up-warning`
- 发布日期 / Published: 2021-03-16
- 来源 / Source: 上海证券交易所法定公告PDF镜像
- URL: https://file.finance.sina.com.cn/211.154.219.97%3A9494/MRGG/CNSESH_STOCK/2021/2021-3/2021-03-16/6949582.PDF

公司披露股价连续多个交易日涨停；截至2021年3月15日收盘价13.43元，静态市盈率300.8倍、动态市盈率2079倍，远高于同行。公司同时再次提示预计2020年归母净利润亏损600万至900万元、扣非亏损2,765万至3,065万元；若经审计净利润为负且营业收入低于1亿元，年报披露后股票可能被实施退市风险警示。点时信息同时包含极端估值、既有投机热度和明确戴帽风险，不能把任何一项机械外推为未来翻倍。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2022-04-28

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 13.8046167
  - **peak_adjusted_close_365d**: 109.9529856
  - **as_of_510300_close**: 5.127
  - **stock_close_on_max_excess_date**: 109.9529856
  - **etf_close_on_max_excess_date**: 5.033
  - **common_trading_sessions**: 243
  - **risk_warning_removed_by_window_end**: 0
- **derivations**:
  - **item 1**:
    - **metric**: max_adjusted_close_return_365d
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - peak_adjusted_close_365d
    - **value**: 6.964943032427695
  - **item 2**:
    - **metric**: stock_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - stock_close_on_max_excess_date
    - **value**: 6.964943032427695
  - **item 3**:
    - **metric**: etf_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_510300_close
      - etf_close_on_max_excess_date
    - **value**: -0.01833430856251206
  - **item 4**:
    - **metric**: max_excess_return_vs_510300_365d
    - **operation**: difference
    - **inputs**:
      - stock_return_on_max_excess_date
      - etf_return_on_max_excess_date
    - **value**: 6.983277340990207

### 对应的题内资料 / Expected evidence

- `annual-small-revenue-loss-and-low-leverage`
- `pre-st-valuation-and-limit-up-warning`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 603032.XSHG
  - **ticker**: 603032
  - **name_as_of**: *ST德新
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-04-28
  - **allowed_domains**:
    - cninfo.com.cn
    - sina.com.cn
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
  - **row_policy**: stock_code=603032.XSHG; quarter=2020q4; info_date=2021-04-27; if_adjusted=0; current warning episode starts 2021-04-28; daily prices 2021-04-28 through 2022-04-28; benchmark=510300.XSHG
  - **st_cause_taxonomy**: operating_financial/negative_profit+sub_100m_revenue
  - **matching_group**: current-risk-warning-episode-market-path-365d-v1
  - **matching_role**: event_low_leverage_micro_revenue_extreme_valuation
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **annual_report_summary**: 9a6a02c708cbebeabe6707da65bf4c85d6377fbe5ead7c4442a84769391fac80
    - **pre_st_risk_notice**: 92f55ae8c111098cbe1d783e7fb3d65336fac0d41d800ccdbeff5e6a1bb0ef3d
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
    - **window**: 2021-04-28/2022-04-28
    - **stock_code**: 603032.XSHG
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2021-12-17
    - **max_excess_date**: 2021-12-17
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
    - **observation_policy**: Use aligned closing observations that exist inside the fixed calendar window; do not impute prices across suspension or after delisting.
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **current_warning_episode_start**: 2021-04-28
    - **risk_warning_removed_by_window_end**: false

</details>

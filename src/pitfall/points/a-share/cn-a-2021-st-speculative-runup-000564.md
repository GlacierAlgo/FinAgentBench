# cn-a-2021-st-speculative-runup-000564

## Question

你处在2021-02-19收盘后的信息环境，今天是供销大集本轮风险警示事件首次以*ST大集交易的日期。请使用下方冻结资料预测未来365个自然日是否出现target定义的异常大幅收盘上涨。法院已因不能清偿到期债务且明显缺乏清偿能力受理重整；公司收入骤降、扣非亏损、经营现金流为负，同时重整可能改善资本结构，也可能失败并转入清算。请把债权稀释、关联占用/担保整改、零售主业生存与重整壳弹性分开，不把法院受理机械解释为必然炒作。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST大集 (000564, SZSE)
- 信息截止 / As of: 2021-02-19
- 预测窗口结束 / Window end: 2022-02-19
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以当前风险警示事件首次生效交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改、重整、资产题材或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 供销大集2020年三季报：收入骤降、扣非亏损与经营现金流流出

- Evidence ID: `q3-retail-collapse-cash-debt-and-negative-ocf`
- 发布日期 / Published: 2020-10-31
- 来源 / Source: 深圳证券交易所法定季度报告PDF镜像及只读RQData点时记录
- URL: https://file.finance.sina.com.cn/211.154.219.97%3A9494/MRGG/CNSESZ_STOCK/2020/2020-10/2020-10-31/6701754.PDF

2020年前三季度营业收入17.4478亿元，同比下降63.36%；归母净利润-2.2029亿元、扣非归母净利润-5.1438亿元，经营活动现金流净额-8.1088亿元。期末货币资金47.946亿元、存货57.664亿元，短期借款66.721亿元、流动负债160.010亿元、总负债201.086亿元。投资活动现金流净额47.993亿元主要不能替代持续经营造血；公司还披露大股东多项股份质押和冻结。

### 供销大集法院重整暨*ST公告：明显缺乏清偿能力，同时存在重整与清算两条路径

- Evidence ID: `court-accepted-restructuring-insolvency-and-two-sided-optionality`
- 发布日期 / Published: 2021-02-10
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2021-02-10/1209270490.PDF

海南高院于2021年2月10日裁定受理债权人对供销大集的重整申请，公司自2021年2月19日起实施*ST。申请理由是公司不能清偿到期债务且明显缺乏清偿能力。公告同时披露股东及关联方非经营性资金占用、未披露担保和需关注资产损失的整改计划。重整若成功可能改善资本结构，若计划未获批准或执行失败则可能破产清算并终止上市；这一双向分布不能被简化为“重整必炒”或“资不抵债必跌”。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2022-02-19

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 6.4623054
  - **peak_adjusted_close_365d**: 17.6709368
  - **as_of_510300_close**: 5.796
  - **stock_close_on_max_excess_date**: 17.6709368
  - **etf_close_on_max_excess_date**: 4.979
  - **common_trading_sessions**: 243
  - **risk_warning_removed_by_window_end**: 0
- **derivations**:
  - **item 1**:
    - **metric**: max_adjusted_close_return_365d
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - peak_adjusted_close_365d
    - **value**: 1.7344632768361583
  - **item 2**:
    - **metric**: stock_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - stock_close_on_max_excess_date
    - **value**: 1.7344632768361583
  - **item 3**:
    - **metric**: etf_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_510300_close
      - etf_close_on_max_excess_date
    - **value**: -0.14095928226363008
  - **item 4**:
    - **metric**: max_excess_return_vs_510300_365d
    - **operation**: difference
    - **inputs**:
      - stock_return_on_max_excess_date
      - etf_return_on_max_excess_date
    - **value**: 1.8754225590997884

### 对应的题内资料 / Expected evidence

- `q3-retail-collapse-cash-debt-and-negative-ocf`
- `court-accepted-restructuring-insolvency-and-two-sided-optionality`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000564.XSHE
  - **ticker**: 000564
  - **name_as_of**: *ST大集
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-02-19
  - **allowed_domains**:
    - sina.com.cn
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
  - **row_policy**: stock_code=000564.XSHE; quarter=2020q3; info_date=2020-10-31; if_adjusted=0; court accepted reorganization on 2021-02-10; current warning episode starts 2021-02-19; daily prices 2021-02-19 through 2022-02-19; benchmark=510300.XSHG
  - **st_cause_taxonomy**: court_restructuring/accepted_insolvency_reorganization+governance_overhang
  - **matching_group**: current-risk-warning-episode-market-path-365d-v1
  - **matching_role**: event_restructuring_two_sided_optionality
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **third_quarter_report_exchange_mirror**: 28025d78184bb2c859b460bfd8ad4e6e0599a7ca0d7d30ec4a9e3223a830ac8b
    - **court_reorganization_and_st_notice**: 4dff12c697dd5e366722f5fb76b28aaa870681ba413127705cd3afebba3e2a93
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
    - **window**: 2021-02-19/2022-02-19
    - **stock_code**: 000564.XSHE
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2021-12-03
    - **max_excess_date**: 2021-12-03
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
    - **observation_policy**: Use aligned closing observations that exist inside the fixed calendar window; do not impute prices across suspension or after delisting.
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **current_warning_episode_start**: 2021-02-19
    - **risk_warning_removed_by_window_end**: false

</details>

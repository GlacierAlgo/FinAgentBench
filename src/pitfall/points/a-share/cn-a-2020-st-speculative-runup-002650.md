# cn-a-2020-st-speculative-runup-002650

## Question

你处在2020-06-15收盘后的信息环境，今天是加加食品本轮风险警示事件首次以ST加加交易的日期。请使用下方冻结资料预测未来365个自然日是否出现target定义的异常大幅收盘上涨。风险警示源于控股股东资金占用和违规担保，主营调味品仍有经营基础，但控制人偿债承诺、司法处置和内控整改存在执行风险。必须同时判断股票自身翻倍与相对510300超额80个百分点两个门槛；接近任何单一门槛都不能算事件。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST加加 (002650, SZSE)
- 信息截止 / As of: 2020-06-15
- 预测窗口结束 / Window end: 2021-06-15
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以当前风险警示事件首次生效交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改、重整、资产题材或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 加加食品实施其他风险警示公告：4.6605亿元违规担保与刚签署的清偿协议

- Evidence ID: `st-notice-signed-settlement-but-unpaid`
- 发布日期 / Published: 2020-06-12
- 来源 / Source: 深圳证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-06-12/1207919359.PDF

公司自2020年6月15日起变更为ST加加。违规担保本金4.6605亿元，占最近一期经审计净资产19.94%，一个月内未解决。公告同时披露控制人获得2.8亿元第三方资金额度，并分别与三湘银行、优选资本签署协议：在6月30日前支付首笔1亿元和不低于1.8亿元后，相关担保责任才解除。协议和额度是具体路径，但披露日尚未满足付款与解除条件。

### 加加食品2020年一季度PIT财务：盈利、正现金流和低上市公司杠杆

- Evidence ID: `q1-strong-balance-sheet-at-listed-company`
- 发布日期 / Published: 2020-04-28
- 来源 / Source: 只读RQData点时财务记录（对应法定一季报）
- URL: https://static.cninfo.com.cn/finalpage/2020-04-28/1207639554.PDF

2020年一季度营业收入4.9211亿元、归母净利润5,026.82万元、扣非归母净利润5,006.71万元、经营活动现金流净额1.1633亿元。期末货币资金4.6015亿元、短期借款5,503.63万元、总负债3.9580亿元、归母净资产23.8711亿元。上市公司本体财务缓冲较强，但违规担保债务属于控制人融资链，不能仅用上市公司账面现金机械抵销。

### 戴帽前报道：实控人称利空出清、6月底解决并可很快摘帽

- Evidence ID: `contemporaneous-controller-claims-fast-removal`
- 发布日期 / Published: 2020-06-12
- 来源 / Source: 中国证券报·中证网转载证券时报e公司报道
- URL: https://www.cs.com.cn/ssgs/gsxw/202006/t20200612_6066759.html

报道复述两份清偿/和解协议及6月30日首付款条件，实控人进一步声称违规担保可在月底前解决、之后能够很快摘帽，公司经营正常。该表态提供管理层预期，却具有明显激励偏差；模型应以付款、担保法律解除和交易所审核为后续门槛，不能把采访表态当成结果。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2021-06-15

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 37.3462235
  - **peak_adjusted_close_365d**: 74.9676568
  - **as_of_510300_close**: 3.956
  - **stock_close_on_max_excess_date**: 74.9676568
  - **etf_close_on_max_excess_date**: 4.813
  - **common_trading_sessions**: 243
  - **risk_warning_removed_by_window_end**: 0
- **derivations**:
  - **item 1**:
    - **metric**: max_adjusted_close_return_365d
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - peak_adjusted_close_365d
    - **value**: 1.0073691467090375
  - **item 2**:
    - **metric**: stock_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - stock_close_on_max_excess_date
    - **value**: 1.0073691467090375
  - **item 3**:
    - **metric**: etf_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_510300_close
      - etf_close_on_max_excess_date
    - **value**: 0.2166329625884731
  - **item 4**:
    - **metric**: max_excess_return_vs_510300_365d
    - **operation**: difference
    - **inputs**:
      - stock_return_on_max_excess_date
      - etf_return_on_max_excess_date
    - **value**: 0.7907361841205645

### 对应的题内资料 / Expected evidence

- `st-notice-signed-settlement-but-unpaid`
- `q1-strong-balance-sheet-at-listed-company`
- `contemporaneous-controller-claims-fast-removal`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002650.XSHE
  - **ticker**: 002650
  - **name_as_of**: ST加加
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-06-15
  - **allowed_domains**:
    - cninfo.com.cn
    - cs.com.cn
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
  - **row_policy**: stock_code=002650.XSHE; 2019q4 and 2020q1 PIT fundamentals available by 2020-04-30; current warning episode starts 2020-06-15; daily prices 2020-06-15 through 2021-06-15; benchmark=510300.XSHG
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation+illegal_guarantees
  - **matching_group**: current-risk-warning-episode-market-path-365d-v1
  - **matching_role**: no_event_threshold_boundary_stock_double_but_excess_79pp
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: fdb701da870263744592c52572bd2585a6e1ece51448874a9fd19f80e44b1ef6
    - **audit_report**: 9a77ffee4a8b33b5bc8c4a6b87f48c19b85f4335b66a8239c045d22dafc15883
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
    - **window**: 2020-06-15/2021-06-15
    - **stock_code**: 002650.XSHE
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2020-08-24
    - **max_excess_date**: 2020-08-24
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
    - **observation_policy**: Use aligned closing observations that exist inside the fixed calendar window; do not impute prices across suspension or after delisting.
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **current_warning_episode_start**: 2020-06-15
    - **risk_warning_removed_by_window_end**: false

</details>

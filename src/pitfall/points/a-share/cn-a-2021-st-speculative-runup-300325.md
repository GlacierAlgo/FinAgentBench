# cn-a-2021-st-speculative-runup-300325

## Question

你处在2021-02-02收盘后的信息环境，今天是德威新材本轮风险警示事件首次以ST德威交易的日期。请使用下方冻结资料预测未来365个自然日是否出现target定义的异常大幅收盘上涨。三季报曾称无违规担保，三个月后公告却披露潜在责任2.44亿元且未按期解决；同时现金约1.06亿元、短借约15.81亿元并持续亏损。请把信息质量断裂、控制人清偿能力、主营材料业务弹性和小市值投机路径分开评估；严重治理风险既可能压垮公司，也不排除短期高波动。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST德威 (300325, SZSE)
- 信息截止 / As of: 2021-02-02
- 预测窗口结束 / Window end: 2022-02-02
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以当前风险警示事件首次生效交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改、重整、资产题材或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 德威新材2020年三季报：报告称无违规担保，但现金、短债与亏损已严重错配

- Evidence ID: `q3-denial-loss-and-debt-pressure`
- 发布日期 / Published: 2020-10-29
- 来源 / Source: 深圳证券交易所法定季度报告PDF镜像及只读RQData点时记录
- URL: http://file.finance.sina.com.cn/211.154.219.97:9494/MRGG/CNSESZ_STOCK/2020/2020-10/2020-10-29/6688169.PDF

三季报明确勾选“公司报告期无违规对外担保情况”且称不存在控股股东及其关联方非经营性资金占用。与此同时，2020年前三季度营业收入7.0400亿元、归母净利润-6,429.68万元、扣非归母净利润-7,605.00万元；期末货币资金1.0557亿元，短期借款15.8116亿元、流动负债21.275亿元，经营活动现金流净额仅1,514.19万元。披露否认与财务压力之间的张力要求模型保留信息质量风险。

### 德威新材实施其他风险警示公告：未解决违规担保暴露此前披露断裂

- Evidence ID: `st-notice-later-disclosed-illegal-guarantees`
- 发布日期 / Published: 2021-02-01
- 来源 / Source: 深圳证券交易所法定公告
- URL: http://disc.static.szse.cn/download/disc/disk02/finalpage/2021-02-01/74b263f6-f480-4313-bd4f-a85f500c1ac1.PDF

截至公告时，扣除控股股东已支付和司法拍卖划扣金额，公司对违规担保合计可能承担2.4417亿元责任，占2019年经审计归母净资产30.82%；公司未能在承诺期限2021年1月29日前解决，自2021年2月2日起被实施ST。四笔事项涉诉，公司只能与债权人协商免责，并依赖控股股东筹资或拍卖资产偿债。该公告与三个月前季报“无违规担保”的表述形成可审计的信息断裂。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2022-02-02

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 15.1848
  - **peak_adjusted_close_365d**: 33.4476
  - **as_of_510300_close**: 5.491
  - **stock_close_on_max_excess_date**: 33.4476
  - **etf_close_on_max_excess_date**: 5.209
  - **common_trading_sessions**: 241
  - **risk_warning_removed_by_window_end**: 0
- **derivations**:
  - **item 1**:
    - **metric**: max_adjusted_close_return_365d
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - peak_adjusted_close_365d
    - **value**: 1.202702702702703
  - **item 2**:
    - **metric**: stock_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - stock_close_on_max_excess_date
    - **value**: 1.202702702702703
  - **item 3**:
    - **metric**: etf_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_510300_close
      - etf_close_on_max_excess_date
    - **value**: -0.051356765616463296
  - **item 4**:
    - **metric**: max_excess_return_vs_510300_365d
    - **operation**: difference
    - **inputs**:
      - stock_return_on_max_excess_date
      - etf_return_on_max_excess_date
    - **value**: 1.2540594683191664

### 对应的题内资料 / Expected evidence

- `q3-denial-loss-and-debt-pressure`
- `st-notice-later-disclosed-illegal-guarantees`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 300325.XSHE
  - **ticker**: 300325
  - **name_as_of**: ST德威
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-02-02
  - **allowed_domains**:
    - sina.com.cn
    - szse.cn
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
  - **row_policy**: stock_code=300325.XSHE; quarter=2020q3; info_date=2020-10-29; if_adjusted=0; current warning episode starts 2021-02-02; daily prices 2021-02-02 through 2022-02-02; benchmark=510300.XSHG
  - **st_cause_taxonomy**: non_operating_governance/illegal_guarantees+disclosure_discontinuity
  - **matching_group**: current-risk-warning-episode-market-path-365d-v1
  - **matching_role**: event_illegal_guarantee_disclosure_break
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **third_quarter_report_exchange_mirror**: cfde60682b17830fa67912ac1d0c75141049459f06a3e8494598a8ba5daf6882
    - **st_notice**: 5205d296684f570ed5b6c69f6568127bc5b6ae9e31ad8d6cf872c08bfccc0fc4
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
    - **window**: 2021-02-02/2022-02-02
    - **stock_code**: 300325.XSHE
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2021-07-22
    - **max_excess_date**: 2021-07-22
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
    - **observation_policy**: Use aligned closing observations that exist inside the fixed calendar window; do not impute prices across suspension or after delisting.
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **current_warning_episode_start**: 2021-02-02
    - **risk_warning_removed_by_window_end**: false

</details>

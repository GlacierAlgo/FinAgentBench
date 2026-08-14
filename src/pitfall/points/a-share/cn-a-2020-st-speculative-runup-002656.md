# cn-a-2020-st-speculative-runup-002656

## Question

你处在2020-01-13收盘后的信息环境，今天是摩登大道首次以ST摩登交易的日期。请使用下方冻结资料，预测未来365个自然日是否会出现target定义的异常大幅收盘上涨。戴帽直接原因是实控人越权形成3.3亿元违规担保，但请继续核对高管集体离职、账户冻结、收入与利润趋势、货币资金下降、海外品牌与渠道、商誉和潜在诉讼损失。非经营性戴帽不代表主营没有恶化，也不自动产生壳价值炒作。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST摩登 (002656, SZSE)
- 信息截止 / As of: 2020-01-13
- 预测窗口结束 / Window end: 2021-01-12
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以首次实施风险警示交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1.0` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 摩登大道实施其他风险警示公告：实控人越权形成3.3亿元未解除担保

- Evidence ID: `st-notice-illegal-guarantees`
- 发布日期 / Published: 2020-01-10
- 来源 / Source: 深圳证券交易所法定公告PDF镜像
- URL: https://pdf.dfcfw.com/pdf/H2_AN202001091373794217_1.PDF

公司自2020年1月13日起变更为ST摩登。公告称控股股东违反规定程序，以公司及子公司名义对外提供担保；截至披露日，未经审议且未及时披露的担保余额3.30亿元，不含利息等费用，占最近年度经审计净资产13.86%。四笔披露担保中仅一笔解除，未解除事项包含为关联方及实控人债务提供担保。董事会只能督促被担保人筹资并通过司法途径解决，责任解除时间和损失金额均不确定。

### 摩登大道2019年三季报：单季亏损、收入下滑与货币资金骤降

- Evidence ID: `q3-operating-decline-cash-and-goodwill`
- 发布日期 / Published: 2019-10-31
- 来源 / Source: 深圳证券交易所法定季度报告PDF镜像
- URL: http://file.finance.sina.com.cn/211.154.219.97:9494/MRGG/CNSESZ_STOCK/2019/2019-10/2019-10-31/5723997.PDF

2019年前三季度营业收入9.6126亿元，同比下降8.25%；归母净利润-2,512.93万元，扣非归母净利润-2,813.47万元；第三季度单季收入下降35.98%、归母净利润-5,638.10万元。经营活动现金流净额1.2291亿元为正，但期末货币资金1.3922亿元，较年初下降54.08%；其他应收款同比大增，主要包括对子公司涉及澳门国际银行款项9,560.96万元。期末商誉4.0907亿元，占归母净资产约17.5%。非经营性违规担保出现时，主营趋势、现金缓冲和资产质量也在恶化。

### 摩登大道治理报道：高管集中离职、账户冻结与反复战略转型

- Evidence ID: `management-exits-and-strategy-instability`
- 发布日期 / Published: 2019-10-14
- 来源 / Source: 中国经济网转载的每日经济新闻调查
- URL: https://finance.ce.cn/stock/gsgdbd/201910/14/t20191014_33331889.shtml

报道梳理公司独立董事和财务总监集中离职，部分独董此前明确反对实控人越权担保；公司在办理银行业务时发现账户冻结，随后才自查出未经过董事会、股东大会和用章审批的担保。报道还回顾公司从服装零售、跨境电商到其他方向的多次战略调整，以及消费行业放缓和渠道压力。治理监督者退出、实控人越权和主营承压共同削弱“仅是非经营性问题、很快可修复”的叙事。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2021-01-12

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 20.7338307
  - **peak_adjusted_close_365d**: 20.7338307
  - **as_of_510300_close**: 4.202
  - **stock_close_on_max_excess_date**: 20.7338307
  - **etf_close_on_max_excess_date**: 4.202
  - **common_trading_sessions**: 243
  - **risk_warning_removed_by_window_end**: 0
- **derivations**:
  - **item 1**:
    - **metric**: max_adjusted_close_return_365d
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - peak_adjusted_close_365d
    - **value**: 0.0
  - **item 2**:
    - **metric**: stock_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - stock_close_on_max_excess_date
    - **value**: 0.0
  - **item 3**:
    - **metric**: etf_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_510300_close
      - etf_close_on_max_excess_date
    - **value**: 0.0
  - **item 4**:
    - **metric**: max_excess_return_vs_510300_365d
    - **operation**: difference
    - **inputs**:
      - stock_return_on_max_excess_date
      - etf_return_on_max_excess_date
    - **value**: 0.0

### 对应的题内资料 / Expected evidence

- `st-notice-illegal-guarantees`
- `q3-operating-decline-cash-and-goodwill`
- `management-exits-and-strategy-instability`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002656.XSHE
  - **ticker**: 002656
  - **name_as_of**: ST摩登
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-01-13
  - **allowed_domains**:
    - dfcfw.com
    - sina.com.cn
    - ce.cn
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
  - **row_policy**: stock_code=002656.XSHE; if_adjusted=0 for 2019q3 PIT fundamentals; daily prices from 2020-01-13 through 2021-01-12; benchmark=510300.XSHG
  - **st_cause_taxonomy**: non_operating_governance/illegal_guarantees
  - **matching_group**: first-st-day-governance-risk-365d-v1
  - **matching_role**: no_event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice_exchange_mirror**: 09d3b381eac2bfecf8ef504fb3203b2f3dadfe0f0b676e072d67bcc9885e66e2
    - **2019_third_quarter_report_exchange_mirror**: d7f82607f662f6cc1cf66c974f08ad11fd83e5eed98b1fb776697e3707976e96
  - **news_evidence_policy**: Contemporaneous reporting may provide management-turnover and strategy context; filings remain authority for the guarantee exposure and PIT financials.
  - **outcome_label_policy**: Stock backward-adjusted closes and raw 510300 closes are aligned by trade_date; maxima use closing observations only over the predeclared 365-calendar-day window.
  - **causal_guardrail**: The label measures an ex post market path, not whether ST designation, governance failure, shell value, or fundamentals caused that path.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: rqdata_daily_price
    - **paths**:
      - data/db/rq_adj_bwd_price_daily/trade_date=YYYY-MM-DD/data.parquet
      - data/db/etf_raw_price_daily/trade_date=YYYY-MM-DD/data.parquet
    - **window**: 2020-01-13/2021-01-12
    - **stock_code**: 002656.XSHE
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2020-01-13
    - **max_excess_date**: 2020-01-13
    - **window_end_return**: -0.6879795396419437
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **st_start**: 2020-01-13
    - **risk_warning_removed_by_window_end**: false

</details>

# cn-a-2019-st-speculative-runup-600290

## Question

你处在2019-12-26收盘后的信息环境，今天是华仪电气首次以ST华仪交易的日期。请使用下方冻结资料，预测未来365个自然日是否会出现target定义的异常大幅收盘上涨。区分风电行业抢装与公司自身订单、应收和盈利质量，核对账面货币资金与10.58亿元控股股东占用、9.259亿元违规担保之间的冲突，以及募集资金、控制人流动性和监管调查风险。行业向好不能替代公司兑现。不要把戴帽、未来退市或后来股价路径作因果捷径。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST华仪 (600290, SSE)
- 信息截止 / As of: 2019-12-26
- 预测窗口结束 / Window end: 2020-12-25
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以首次实施风险警示交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1.0` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 华仪电气实施其他风险警示公告：10.58亿元占用与9.259亿元违规担保

- Evidence ID: `st-notice-occupation-and-guarantees`
- 发布日期 / Published: 2019-12-25
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2019-12-25/600290_20191225_1.pdf

公司自2019年12月26日起变更为ST华仪。公告称违规担保金额9.2590亿元，占最近一期经审计净资产22.75%，其中逾期担保2.14亿元；关联方资金占用余额10.58亿元，占净资产26.00%。控股股东未在自2019年11月25日起一个月的承诺期限内解决，直接触发其他风险警示。公告没有可验证的还款资金，只表示继续催促、通过法律途径处理并至少每月披露进展。

### 华仪电气2019年三季报：账面现金较高，但收入、扣非利润与应收质量偏弱

- Evidence ID: `q3-cash-receivables-and-weak-operations`
- 发布日期 / Published: 2019-10-31
- 来源 / Source: 上海证券交易所法定季度报告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2019-10-31/600290_2019_3.pdf

2019年前三季度营业收入8.0757亿元，同比下降25.75%；归母净利润1,102.28万元，同比下降36.04%，扣非归母净利润-2,982.85万元；经营活动现金流净额1.0042亿元。期末货币资金15.7874亿元、短期借款5.3413亿元，看似流动性充裕，但应收账款21.0521亿元，是前三季度收入的约2.61倍，另有预付款2.5007亿元。结合随后披露的10.58亿元控股股东占用，账面现金不能被机械视为可自由使用资金。

### 2019年风电设备行业观点：三年抢装开启，但采购向龙头集中

- Evidence ID: `wind-installation-boom-and-leader-concentration`
- 发布日期 / Published: 2019-06-03
- 来源 / Source: 中国证券报·中证网转载的兴业证券行业观点
- URL: https://www.cs.com.cn/gppd/sdqs/201906/t20190603_5954690.html

行业观点预计补贴并网期限推动2019至2021年风电持续抢装，年均装机规模可能超过30GW，短期需求和盈利迎来拐点；同时强调平价时代运营商更重视发电效率、产品质量和运维费用，市场份额可能进一步向龙头集中。推荐名单聚焦金风科技、天顺风能等细分龙头，没有华仪电气。该材料说明行业总量向好和尾部厂商兑现可能分化，不能用“风电抢装”掩盖公司应收、占用与治理风险。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2020-12-25

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 16.6944872
  - **peak_adjusted_close_365d**: 16.6944872
  - **as_of_510300_close**: 4.021
  - **stock_close_on_max_excess_date**: 16.6944872
  - **etf_close_on_max_excess_date**: 4.021
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

- `st-notice-occupation-and-guarantees`
- `q3-cash-receivables-and-weak-operations`
- `wind-installation-boom-and-leader-concentration`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600290.XSHG
  - **ticker**: 600290
  - **name_as_of**: ST华仪
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-12-26
  - **allowed_domains**:
    - sse.com.cn
    - cs.com.cn
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
  - **row_policy**: stock_code=600290.XSHG; if_adjusted=0 for 2019q3 PIT fundamentals; daily prices from 2019-12-26 through 2020-12-25; benchmark=510300.XSHG
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation+illegal_guarantees
  - **matching_group**: first-st-day-governance-risk-365d-v1
  - **matching_role**: no_event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: d6aad276b1294a65a1bfaaa71f7591236bb680d8f10c04e972b916147f43bc67
    - **2019_third_quarter_report**: 53fa5ec62fdfab02628c876388e25e3705497e8bcd6e49e9a22aff3cfde66314
  - **news_evidence_policy**: Contemporaneous news may frame the wind-installation cycle and disclosed governance failures; official filings and RQData remain label authority.
  - **outcome_label_policy**: Stock backward-adjusted closes and raw 510300 closes are aligned by trade_date; maxima use closing observations only over the predeclared 365-calendar-day window.
  - **causal_guardrail**: The label measures an ex post market path, not whether sector demand, ST designation, regulatory action, or fundamentals caused that path.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: rqdata_daily_price
    - **paths**:
      - data/db/rq_adj_bwd_price_daily/trade_date=YYYY-MM-DD/data.parquet
      - data/db/etf_raw_price_daily/trade_date=YYYY-MM-DD/data.parquet
    - **window**: 2019-12-26/2020-12-25
    - **stock_code**: 600290.XSHG
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2019-12-26
    - **max_excess_date**: 2019-12-26
    - **window_end_return**: -0.19578313253012047
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **st_start**: 2019-12-26
    - **risk_warning_removed_by_window_end**: false

</details>

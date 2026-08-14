# cn-a-2021-st-speculative-runup-000525

## Question

你处在2021-05-06收盘后的信息环境，今天是红太阳首次以ST红太阳交易的日期。请使用下方冻结资料，预测未来365个自然日是否会出现target定义的异常大幅收盘上涨。先区分主营农药经营和控股股东近30亿元非经营性占用，核对货币资金、短债、其他应收款、扣非利润、产品价格与公司的真实产品暴露；行业报告中的草甘膦景气不能在缺少产能证据时直接套到公司。再评估治理修复、债务与重整选项、供给周期和退市风险。不要把摘帽、重整或后来上涨作因果捷径。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST红太阳 (000525, SZSE)
- 信息截止 / As of: 2021-05-06
- 预测窗口结束 / Window end: 2022-05-06
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以首次实施风险警示交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1.0` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 红太阳实施其他风险警示公告：近29.64亿元占用预计一个月内无法解决

- Evidence ID: `st-notice-near-three-billion-occupation`
- 发布日期 / Published: 2021-04-29
- 来源 / Source: 深圳证券交易所法定公告PDF镜像
- URL: https://pdf.dfcfw.com/pdf/H2_AN202104291488680395_1.pdf

公司自2021年5月6日起变更为ST红太阳，日涨跌幅限制5%。公告称截至2021年4月28日，控股股东南一农集团及关联方非经营性占用余额29.639845亿元，预计无法在一个月内解决；2020年度内部控制审计报告为否定意见。公告解释控股股东流动性危机源于融资收紧，并披露部分所谓归还资金随后又被用于为控股股东和红太阳集团融资提供担保质押，最终被银行划转，显示资金回流并不等于风险实质消除。公司同时仍处于证监会立案调查期间。

### 红太阳2020年年度报告：农药主业、扣非亏损和现金短债矛盾

- Evidence ID: `annual-agrochemical-financial-stress`
- 发布日期 / Published: 2021-04-30
- 来源 / Source: 巨潮资讯法定年度报告
- URL: https://static.cninfo.com.cn/finalpage/2021-04-30/1209871241.PDF

2020年营业收入40.2200亿元，同比下降12.84%；归母净利润-1.5381亿元，扣非归母净利润-2.6609亿元；经营活动现金流净额2.3124亿元。农药销售收入39.8589亿元、占收入99.10%，毛利率18.77%，同比下降13.49个百分点；产量22.90万吨、销量19.50万吨、库存同比增长17%。期末货币资金1.9811亿元，短期借款37.9076亿元，流动资产55.8644亿元低于流动负债64.6997亿元；其他应收款32.2476亿元，接近当年收入的80%，主要风险与关联占用一致。年报称出口和汇率受疫情冲击，并计提存货与应收减值1.0635亿元。

### 2021年4月农化行业报告：草甘膦涨价，但不可无证据外推到红太阳

- Evidence ID: `sector-boom-with-exposure-attribution-trap`
- 发布日期 / Published: 2021-04-30
- 来源 / Source: 国信证券行业报告（东方财富PDF镜像）
- URL: https://pdf.dfcfw.com/pdf/H3_AP202105061490021000_1.pdf

行业报告称草甘膦报价35,312元/吨，30日上涨12.10%，较年初上涨29.09%，并判断全球粮食安全、供给集中和高开工率可能延长景气；其列示的主要草甘膦企业包括兴发、江山、新安和扬农，并未列出红太阳。红太阳年报只按“农药销售”汇总披露，未在该表证明草甘膦原药产能。因此该报告既是行业上行信号，也是暴露归因陷阱：模型必须寻找公司产品结构证据，不能把热门品种涨价自动当成红太阳盈利催化。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2022-05-06

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 34.63593
  - **peak_adjusted_close_365d**: 84.632142
  - **as_of_510300_close**: 5.061
  - **stock_close_on_max_excess_date**: 84.632142
  - **etf_close_on_max_excess_date**: 3.903
  - **common_trading_sessions**: 243
  - **risk_warning_removed_by_window_end**: 0
- **derivations**:
  - **item 1**:
    - **metric**: max_adjusted_close_return_365d
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - peak_adjusted_close_365d
    - **value**: 1.4434782608695653
  - **item 2**:
    - **metric**: stock_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - stock_close_on_max_excess_date
    - **value**: 1.4434782608695653
  - **item 3**:
    - **metric**: etf_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_510300_close
      - etf_close_on_max_excess_date
    - **value**: -0.22880853586247774
  - **item 4**:
    - **metric**: max_excess_return_vs_510300_365d
    - **operation**: difference
    - **inputs**:
      - stock_return_on_max_excess_date
      - etf_return_on_max_excess_date
    - **value**: 1.6722867967320432

### 对应的题内资料 / Expected evidence

- `st-notice-near-three-billion-occupation`
- `annual-agrochemical-financial-stress`
- `sector-boom-with-exposure-attribution-trap`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000525.XSHE
  - **ticker**: 000525
  - **name_as_of**: ST红太阳
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-05-06
  - **allowed_domains**:
    - cninfo.com.cn
    - dfcfw.com
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
  - **row_policy**: stock_code=000525.XSHE; if_adjusted=0 for 2020q4 PIT fundamentals; daily prices from 2021-05-06 through 2022-05-06; benchmark=510300.XSHG
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation+adverse_internal_control
  - **matching_group**: first-st-day-governance-risk-365d-v1
  - **matching_role**: event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice_exchange_mirror**: a09e14a6a5860d11fcfb194c5449bcf87e94edd3ca4951aa85dca44bde64ddf6
    - **2020_annual_report**: 92441de1093f0fbf952e60343afe48da4852733508b35c83b487700dbc51fa0c
  - **news_evidence_policy**: A contemporaneous sector report is deliberately included as a possible exposure-misattribution trap; the company filing must support any claimed product linkage.
  - **outcome_label_policy**: Stock backward-adjusted closes and raw 510300 closes are aligned by trade_date; maxima use closing observations only over the predeclared 365-calendar-day window.
  - **causal_guardrail**: The label measures an ex post market path, not whether agrochemical prices, ST designation, remediation, restructuring, or fundamentals caused that path.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: rqdata_daily_price
    - **paths**:
      - data/db/rq_adj_bwd_price_daily/trade_date=YYYY-MM-DD/data.parquet
      - data/db/etf_raw_price_daily/trade_date=YYYY-MM-DD/data.parquet
    - **window**: 2021-05-06/2022-05-06
    - **stock_code**: 000525.XSHE
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2022-05-06
    - **max_excess_date**: 2022-05-06
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **st_start**: 2021-05-06
    - **risk_warning_removed_by_window_end**: false

</details>

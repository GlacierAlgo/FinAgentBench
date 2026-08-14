# cn-a-2018-st-speculative-runup-002680

## Question

你处在2018-07-26收盘后的信息环境，今天是长生生物本轮风险警示事件首次以ST长生交易的日期。请使用下方冻结资料预测未来365个自然日是否出现target定义的异常大幅收盘上涨。疫苗生产记录造假涉及公共健康、监管处罚、停产召回、赔偿和重大违法退市尾部；历史盈利或疫苗牌照不等于资产仍可持续。请区分超跌反弹想象与交易连续性、重大违法终局和严格双门槛，不把所有ST都套用壳炒作先验。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST长生 (002680, SZSE)
- 信息截止 / As of: 2018-07-26
- 预测窗口结束 / Window end: 2019-07-26
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以当前风险警示事件首次生效交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改、重整、资产题材或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 长生生物2018年一季报：利润高增且账面偿债能力充足

- Evidence ID: `q1-profitable-solvent-financial-snapshot`
- 发布日期 / Published: 2018-04-25
- 来源 / Source: 巨潮资讯法定季度报告
- URL: https://static.cninfo.com.cn/finalpage/2018-04-25/1204733785.PDF

2018年一季度营业收入3.4637亿元、归母净利润1.5725亿元、扣非净利润1.3734亿元、经营活动现金流净额8,738.05万元，同比分别增长54.05%、72.22%、96.05%和409.26%。期末货币资金8,267.83万元、应收账款8.7220亿元、流动负债5.7612亿元、负债合计6.5081亿元、归母权益约40.14亿元。静态财务报表呈现盈利、高权益和低负债，并没有典型资不抵债路径。

### 药监核查进展：企业编造狂犬疫苗生产与检验记录

- Evidence ID: `regulator-found-fabricated-production-records`
- 发布日期 / Published: 2018-07-23
- 来源 / Source: 巨潮资讯转载国家药监局核查结论的法定公告
- URL: https://static.cninfo.com.cn/finalpage/2018-07-23/1205221917.PDF

公司转述国家药监局现场核查进展：已经查明企业编造生产记录和产品检验记录、随意变更工艺参数和设备，严重违反药品管理法和GMP；监管要求收回GMP证书、停止狂犬疫苗生产，并对企业立案调查。公司称复产时间无法预计，停产将对生产经营产生较大影响。该风险不是普通周期波动，而是核心产品合规和经营许可基础受到破坏。

### 长生生物首次ST：所有产品暂停批签发并全面停产

- Evidence ID: `first-st-full-production-shutdown`
- 发布日期 / Published: 2018-07-25
- 来源 / Source: 巨潮资讯法定风险警示公告
- URL: https://static.cninfo.com.cn/finalpage/2018-07-25/1205226262.PDF

公司自2018年7月26日起实施其他风险警示并更名ST长生。公告称狂犬疫苗GMP证书已被收回、狂犬和百白破疫苗被责令停产、所有产品暂停批签发，公司又决定其他产品全面自主停产，复产时间不确定，生产经营受到严重影响；董事长等人员被公安机关带走审查。即使此前资产负债表健康，核心许可、质量信誉、治理层履职和现金流来源已同时承压。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2019-07-26

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 40.2438528
  - **peak_adjusted_close_365d**: 40.2438528
  - **as_of_510300_close**: 3.591
  - **stock_close_on_max_excess_date**: 40.2438528
  - **etf_close_on_max_excess_date**: 3.591
  - **common_trading_sessions**: 244
  - **risk_warning_removed_by_window_end**: 0
- **derivations**:
  - **item 1**:
    - **metric**: max_adjusted_close_return_365d
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - peak_adjusted_close_365d
    - **value**: 0
  - **item 2**:
    - **metric**: stock_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - stock_close_on_max_excess_date
    - **value**: 0
  - **item 3**:
    - **metric**: etf_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_510300_close
      - etf_close_on_max_excess_date
    - **value**: 0
  - **item 4**:
    - **metric**: max_excess_return_vs_510300_365d
    - **operation**: difference
    - **inputs**:
      - stock_return_on_max_excess_date
      - etf_return_on_max_excess_date
    - **value**: 0

### 对应的题内资料 / Expected evidence

- `q1-profitable-solvent-financial-snapshot`
- `regulator-found-fabricated-production-records`
- `first-st-full-production-shutdown`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002680.XSHE
  - **ticker**: 002680
  - **name_as_of**: ST长生
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2018-07-26
  - **allowed_domains**:
    - cninfo.com.cn
    - gov.cn
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
  - **row_policy**: stock_code=002680.XSHE; 2017q4 and 2018q1 PIT fundamentals plus official investigation documents available by 2018-07-26; current warning episode starts 2018-07-26; daily prices 2018-07-26 through 2019-07-26 when observations exist; benchmark=510300.XSHG
  - **st_cause_taxonomy**: major_illegality/vaccine_data_fraud+public_health_harm
  - **matching_group**: current-risk-warning-episode-market-path-365d-v1
  - **matching_role**: no_event_major_illegality_terminal_risk
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **q1_report**: 3b5618ad29960cdf496526d29153f1b85f21a9a162631cb390a838236471df20
    - **investigation_progress**: d338d836356f0625a7078da1480049c1429860b7f50afef51ee73115e538b54e
    - **st_notice**: e1b9d95bcac5dc9a5b3321f97bc5b1856fdcfe497f240bc2464f0c603668a10a
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
    - **window**: 2018-07-26/2019-07-26
    - **stock_code**: 002680.XSHE
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2018-07-26
    - **max_excess_date**: 2018-07-26
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
    - **observation_policy**: Use aligned closing observations that exist inside the fixed calendar window; do not impute prices across suspension or after delisting.
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **current_warning_episode_start**: 2018-07-26
    - **risk_warning_removed_by_window_end**: false

</details>

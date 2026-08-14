# cn-a-2018-st-speculative-runup-000939

## Question

你处在2018-07-02收盘后的信息环境，今天是凯迪生态本轮风险警示事件首次以*ST凯迪交易的日期。请使用下方冻结资料预测未来365个自然日内、在仍有可交易收盘观测的日期中是否出现target定义的异常大幅上涨。公司债券违约、审计无法表示意见、银行账户冻结和项目现金流错配均指向极端流动性风险；生物质电站资产规模不等于可自由变现价值。请把停牌造成的路径截断纳入概率，不把资产账面规模或重组传闻当作可交易收益。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST凯迪 (000939, SZSE)
- 信息截止 / As of: 2018-07-02
- 预测窗口结束 / Window end: 2019-07-02
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以当前风险警示事件首次生效交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改、重整、资产题材或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 凯迪生态2017年报：无法表示意见、巨额亏损与2018年集中兑付

- Evidence ID: `annual-disclaimer-debt-and-cash-burn`
- 发布日期 / Published: 2018-06-29
- 来源 / Source: 巨潮资讯法定年度报告
- URL: https://static.cninfo.com.cn/finalpage/2018-06-29/1205105058.PDF

2017年末货币资金24.5264亿元、应收账款27.2310亿元、其他应收款23.5586亿元、存货30.8231亿元，流动负债160.1837亿元、负债合计278.3560亿元、归母权益94.844亿元。全年营业收入54.4574亿元、归母净亏损23.8051亿元、财务费用14.5789亿元、资产减值损失21.1732亿元；投资与筹资现金流净额分别为-21.7617亿元和-32.93亿元。审计师出具无法表示意见，并指出2018年到期有息债务本息147.53亿元、持续经营存在重大不确定性。

### 凯迪生态公告母子公司47个账户被冻结

- Evidence ID: `bank-accounts-frozen-after-default`
- 发布日期 / Published: 2018-05-24
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2018-05-24/1204998051.PDF

因中票违约引发信用风险和债权人保全，公司母公司9个账户被冻结，冻结申请金额10.7580亿元，而被冻结账户实际余额仅2,444.25万元；24家子公司另有38个账户被冻结，冻结申请金额14.5596亿元、实际余额2,283.85万元。账户体系广泛冻结且余额远低于债权主张，限制电厂燃料采购、工资与日常运营。

### 凯迪生态首次*ST：无法表示意见且一年内约150亿元债务待处理

- Evidence ID: `first-delisting-risk-warning-audit-disclaimer`
- 发布日期 / Published: 2018-06-29
- 来源 / Source: 巨潮资讯法定风险警示公告
- URL: https://static.cninfo.com.cn/finalpage/2018-06-29/1205105065.PDF

公司因2017年度财务报告被出具无法表示意见，自2018年7月2日起实施退市风险警示并更名*ST凯迪。董事会称将通过电厂封闭运营、债务重组、资产处置和引入第三方恢复经营；同时披露截至2018年5月有息债务本息余额超过240亿元，一年内到期约150亿元。方案依赖多方债权人、资产买方和新投资者，尚不是已执行的资本补足或审计闭环。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2019-07-02

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 89.57178
  - **peak_adjusted_close_365d**: 89.57178
  - **as_of_510300_close**: 3.443
  - **stock_close_on_max_excess_date**: 89.57178
  - **etf_close_on_max_excess_date**: 3.443
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

- `annual-disclaimer-debt-and-cash-burn`
- `bank-accounts-frozen-after-default`
- `first-delisting-risk-warning-audit-disclaimer`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000939.XSHE
  - **ticker**: 000939
  - **name_as_of**: *ST凯迪
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2018-07-02
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
  - **row_policy**: stock_code=000939.XSHE; 2017q4 PIT fundamentals and official default/audit documents available by 2018-07-02; current warning episode starts 2018-07-02; aligned closing prices through 2019-07-02 when observations exist; benchmark=510300.XSHG
  - **st_cause_taxonomy**: operating_financial/debt_default+audit_disclaimer+liquidity_crisis
  - **matching_group**: current-risk-warning-episode-market-path-365d-v1
  - **matching_role**: no_event_debt_default_suspension
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **annual_report**: e75c8ddfe0aa98328eb3c09be8b7462dfaa2cfb4cd277402055a641ebe5436dc
    - **account_freeze**: 11954c8cd0e1618acc3b07592d0e32c10cc4b0fd088141951624e5e5853d8daa
    - **st_notice**: b77f850493a03903386ffd7544c9888c2beb9961b355cfb3478056ea7048b7c7
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
    - **window**: 2018-07-02/2019-07-02
    - **stock_code**: 000939.XSHE
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2018-07-02
    - **max_excess_date**: 2018-07-02
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
    - **observation_policy**: Use aligned closing observations that exist inside the fixed calendar window; do not impute prices across suspension or after delisting.
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **current_warning_episode_start**: 2018-07-02
    - **risk_warning_removed_by_window_end**: false

</details>

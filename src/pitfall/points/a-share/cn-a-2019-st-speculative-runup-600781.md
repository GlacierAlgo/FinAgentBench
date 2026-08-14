# cn-a-2019-st-speculative-runup-600781

## Question

你处在2019-09-03收盘后的信息环境，今天是辅仁药业本轮风险警示事件首次以ST辅仁交易的日期。请使用下方冻结资料预测未来365个自然日是否出现target定义的异常大幅收盘上涨。公司账面巨额现金与无法支付小额分红相冲突，监管问询、资金受限、关联占用和债务压力使现金真实性成为核心。药品资产与壳价值只能作为次级可选性。请判断是否可能同时越过股票翻倍与相对510300超额80个百分点门槛，不因“非经营性问题”标签忽略流动性传染。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST辅仁 (600781, SSE)
- 信息截止 / As of: 2019-09-03
- 预测窗口结束 / Window end: 2020-09-02
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以当前风险警示事件首次生效交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改、重整、资产题材或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 辅仁药业实施其他风险警示公告：16.35625亿元占用、违规担保与控股股东全冻结

- Evidence ID: `st-notice-occupation-guarantee-and-freeze`
- 发布日期 / Published: 2019-08-31
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2019-08-31/1206870184.PDF

公司自2019年9月3日起变更为ST辅仁。公告称向控股股东及关联方提供借款余额16.35625亿元，未经批准提供连带责任担保1.4亿元、剩余担保6,202万元，预计一个月内无法解决。控股股东持有的45.03%上市公司股份已100%冻结并多次轮候冻结；公司存在债务逾期、流动性不足、产能和销售受影响、证监会调查，以及2018年度现金分红仍未实施。

### 辅仁药业2019年半年报：利润仍正但现金骤降91.88%、其他应收款暴增

- Evidence ID: `h1-cash-collapse-and-related-receivables`
- 发布日期 / Published: 2019-08-31
- 来源 / Source: 巨潮资讯法定半年度报告
- URL: https://static.cninfo.com.cn/finalpage/2019-08-31/1206870186.PDF

2019年上半年营业收入27.6896亿元、归母净利润3.9900亿元、扣非归母净利润3.6213亿元、经营活动现金流净额2.5226亿元；但期末货币资金仅1.3445亿元，较年初16.5636亿元下降91.88%，其中1.2771亿元受限。其他应收款从1,742.68万元增至18.3482亿元，主要系关联方借款；短期借款23.8741亿元。母公司货币资金仅35.57万元。账面利润并未形成可支配清偿能力。

### 戴帽前调查报道：18亿元一季报现金却拿不出6,000万元分红

- Evidence ID: `pre-st-dividend-failure-investigation`
- 发布日期 / Published: 2019-08-06
- 来源 / Source: 中国证券报·中证网转载每日经济新闻
- URL: https://www.cs.com.cn/ssgs/gsxw/201908/t20190806_5975027.html

报道指出公司一季报显示约18.16亿元货币资金，却在7月无法按期实施约6,000万元现金分红，随后暴露资金受限、债务和控制人体系问题。该极端现金可得性矛盾在正式戴帽前已经公开，是判断关联应收可回收、母公司支付能力和治理可信度的重要先验，而不是需要未来信息才能发现的线索。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2020-09-02

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 14.582694
  - **peak_adjusted_close_365d**: 14.582694
  - **as_of_510300_close**: 3.908
  - **stock_close_on_max_excess_date**: 14.582694
  - **etf_close_on_max_excess_date**: 3.908
  - **common_trading_sessions**: 243
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

- `st-notice-occupation-guarantee-and-freeze`
- `h1-cash-collapse-and-related-receivables`
- `pre-st-dividend-failure-investigation`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600781.XSHG
  - **ticker**: 600781
  - **name_as_of**: ST辅仁
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-09-03
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
  - **row_policy**: stock_code=600781.XSHG; 2018q4 and 2019q1 PIT fundamentals available before warning episode; current warning episode starts 2019-09-03; daily prices 2019-09-03 through 2020-09-02; benchmark=510300.XSHG
  - **st_cause_taxonomy**: non_operating_governance/cash_authenticity+related_party_fund_occupation
  - **matching_group**: current-risk-warning-episode-market-path-365d-v1
  - **matching_role**: no_event_cash_reality_collapse
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: ec3e34a584c40558e80f65e6023dd85ad238a1b1cf6163a9dd09dc3e2130fc51
    - **h1_report**: cc631eb09efd9844a615fbc7b2daae85ad238a1b1cf6163a9dd09dc3e2130fc51
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
    - **window**: 2019-09-03/2020-09-02
    - **stock_code**: 600781.XSHG
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2019-09-03
    - **max_excess_date**: 2019-09-03
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
    - **observation_policy**: Use aligned closing observations that exist inside the fixed calendar window; do not impute prices across suspension or after delisting.
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **current_warning_episode_start**: 2019-09-03
    - **risk_warning_removed_by_window_end**: false

</details>

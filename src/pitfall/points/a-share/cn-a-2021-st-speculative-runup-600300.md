# cn-a-2021-st-speculative-runup-600300

## Question

你处在2021-04-27收盘后的信息环境，今天是维维股份首次以ST维维交易的日期。请使用下方冻结资料，预测未来365个自然日是否会出现target定义的异常大幅收盘上涨。戴帽源于历史关联资金拆借和内控否定意见，但公告称占用本息已经收回；请判断整改、国资股东、植物蛋白概念、实际产能利用、扣非利润和处置收益质量是否足以支持异常市场路径。摘帽可预期性不等于股价翻倍，行业故事也不等于经营兑现。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST维维 (600300, SSE)
- 信息截止 / As of: 2021-04-27
- 预测窗口结束 / Window end: 2022-04-27
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以首次实施风险警示交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1.0` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 维维股份实施其他风险警示公告：内控重大缺陷仍在，但占用本息已收回

- Evidence ID: `st-notice-remediation-before-first-st-day`
- 发布日期 / Published: 2021-04-26
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/new/2021-04-26/600300_20210426_1.pdf

公司自2021年4月27日起变更为ST维维。戴帽原因是会计师对2020年度内部控制出具否定意见：关联资金拆借未履行董事会、股东大会决策程序，也未及时披露，内部控制未能防止、发现和纠正违规，构成重大缺陷。与多数未解决占用案例不同，公告明确称新一届董事会已在2021年4月21日前解决资金占用和违规担保问题，并收回占用资金本息。这使案例能够检验“整改完成或未来摘帽必然带来大炒”的错误捷径。

### 维维股份2020年年度报告：现金流改善但利润主要来自处置，植物蛋白产能利用不足

- Evidence ID: `annual-core-profit-disposal-gains-and-capacity`
- 发布日期 / Published: 2021-04-24
- 来源 / Source: 上海证券交易所法定年度报告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/new/2021-04-24/600300_20210424_2.pdf

2020年营业收入47.9882亿元，同比下降4.77%；归母净利润4.3573亿元，但扣非归母净利润仅6,111.52万元。年报解释出售枝江酒业形成投资收益约1.32亿元，土地征收形成资产处置收益约2.10亿元，合计对利润贡献很大。经营活动现金流净额8.9638亿元；货币资金22.2749亿元、短期借款24.2661亿元。固体饮料收入17.5119亿元基本持平，植物蛋白饮料收入4.4024亿元下降14.53%。主要豆奶/乳品工厂多处实际产能明显低于设计产能，例如总部豆奶粉设计6万吨、实际2.41万吨。占用期末利息2,692.29万元已于2021年4月21日清偿。

### 戴帽前治理报道：多年虚假货款通道占用与董监高知情风险

- Evidence ID: `contemporaneous-governance-history-and-sanctions`
- 发布日期 / Published: 2021-04-01
- 来源 / Source: 新浪财经转载的资本市场调查报道
- URL: https://finance.sina.com.cn/stock/s/2021-04-01/doc-ikmyaawa3549966.shtml

报道根据监管处罚和交易所纪律处分梳理，2017至2019年维维集团通过虚假支付货款等中间通道持续占用上市公司资金，年度累计占用从约7亿元升至11.54亿元；部分上市公司高管知悉并配合调度，其他董监高签署定期报告但未勤勉尽责。上交所认为“个人所为、董事会不知情”的申辩反而说明内控存在重大缺陷。该历史提高治理风险先验；但在as_of前占用本息已经收回，模型仍需把历史缺陷与当前修复进度分开。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2022-04-27

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 26.9628848
  - **peak_adjusted_close_365d**: 34.6478433
  - **as_of_510300_close**: 5.089
  - **stock_close_on_max_excess_date**: 33.103035
  - **etf_close_on_max_excess_date**: 4.101
  - **common_trading_sessions**: 243
  - **risk_warning_removed_by_window_end**: 1
- **derivations**:
  - **item 1**:
    - **metric**: max_adjusted_close_return_365d
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - peak_adjusted_close_365d
    - **value**: 0.28501989149172946
  - **item 2**:
    - **metric**: stock_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - stock_close_on_max_excess_date
    - **value**: 0.2277260109793593
  - **item 3**:
    - **metric**: etf_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_510300_close
      - etf_close_on_max_excess_date
    - **value**: -0.19414423265867564
  - **item 4**:
    - **metric**: max_excess_return_vs_510300_365d
    - **operation**: difference
    - **inputs**:
      - stock_return_on_max_excess_date
      - etf_return_on_max_excess_date
    - **value**: 0.42187024363803494

### 对应的题内资料 / Expected evidence

- `st-notice-remediation-before-first-st-day`
- `annual-core-profit-disposal-gains-and-capacity`
- `contemporaneous-governance-history-and-sanctions`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600300.XSHG
  - **ticker**: 600300
  - **name_as_of**: ST维维
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-04-27
  - **allowed_domains**:
    - sse.com.cn
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
  - **row_policy**: stock_code=600300.XSHG; if_adjusted=0 for 2020q4 PIT fundamentals; daily prices from 2021-04-27 through 2022-04-27; benchmark=510300.XSHG
  - **st_cause_taxonomy**: non_operating_governance/remediated_related_party_fund_occupation+adverse_internal_control
  - **matching_group**: first-st-day-governance-risk-365d-v1
  - **matching_role**: no_event_remediation_control
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: a7fbfd34ccde4ee257ab4d18ad32c51156db5a4e78dd44b14b43c54f2195c2cb
    - **2020_annual_report**: 7bbd8699a7d194a1cbf150111ad520500a9ab1963de2c04b1720f0281bd019aa
  - **news_evidence_policy**: Contemporaneous reporting may expose governance history; official filings and RQData remain the authority for remediation, financial facts, and the label.
  - **outcome_label_policy**: Stock backward-adjusted closes and raw 510300 closes are aligned by trade_date; maxima use closing observations only over the predeclared 365-calendar-day window.
  - **causal_guardrail**: The label measures an ex post market path; remediation and later risk-warning removal are deliberately not treated as sufficient causes of a run-up.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: rqdata_daily_price
    - **paths**:
      - data/db/rq_adj_bwd_price_daily/trade_date=YYYY-MM-DD/data.parquet
      - data/db/etf_raw_price_daily/trade_date=YYYY-MM-DD/data.parquet
    - **window**: 2021-04-27/2022-04-27
    - **stock_code**: 600300.XSHG
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2022-03-03
    - **max_excess_date**: 2022-04-11
    - **window_end_return**: -0.08602619182647686
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **st_start**: 2021-04-27
    - **risk_warning_removed**: 2022-04-12

</details>

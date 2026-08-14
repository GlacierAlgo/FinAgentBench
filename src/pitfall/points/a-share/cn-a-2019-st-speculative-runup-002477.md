# cn-a-2019-st-speculative-runup-002477

## Question

你处在2019-04-26收盘后的信息环境，今天是雏鹰农牧本轮风险警示事件首次以*ST雏鹰交易的日期。请使用下方冻结资料预测未来365个自然日内、在仍有可交易收盘观测的日期中是否出现target定义的异常大幅上涨。公司债务违约、持续亏损、流动性枯竭和生猪资产处置困难同时存在；低价股可能吸引投机，但停牌或面值退市会截断可实现路径。请显式考虑不完整交易观察期，不把盘中波动或退市整理期之外的价格想象成收盘收益。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST雏鹰 (002477, SZSE)
- 信息截止 / As of: 2019-04-26
- 预测窗口结束 / Window end: 2020-04-25
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以当前风险警示事件首次生效交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改、重整、资产题材或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 雏鹰农牧2019年一季报：归母权益转负、收入不抵成本且现金高度受限

- Evidence ID: `q1-negative-equity-and-cash-conversion-gap`
- 发布日期 / Published: 2019-04-25
- 来源 / Source: 巨潮资讯法定季度报告
- URL: https://static.cninfo.com.cn/finalpage/2019-04-25/1206091341.PDF

2019年一季度营业收入3.9641亿元，而营业成本8.2117亿元、财务费用2.2941亿元、归母净亏损11.0304亿元；经营活动现金流净额仍为正4,662.62万元。期末货币资金4.2025亿元，但现金及现金等价物仅4,185.95万元；流动负债149.1044亿元、负债合计181.9921亿元，归母所有者权益已降至-1,043.02万元。正经营现金流不能抵消负毛利、巨额短债、融资费用和负净资产。

### 雏鹰农牧披露新增诉讼与大范围债务逾期

- Evidence ID: `overdue-debt-litigation-and-frozen-assets`
- 发布日期 / Published: 2019-04-13
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2019-04-13/1206016281.PDF

公司在被证监会立案调查期间自查披露大量诉讼、仲裁和债务逾期。逾期清单覆盖银行短期借款、信托贷款、融资租赁、保理和其他融资，包括单笔5.99亿元个人借款以及多笔亿元级金融机构债务；部分案件已导致资产查封或诉讼。债务分散、交叉违约与司法保全提高了重组协调难度。

### 雏鹰农牧首次*ST：审计无法表示意见并提示持续经营危机

- Evidence ID: `first-delisting-risk-warning-audit-disclaimer`
- 发布日期 / Published: 2019-04-25
- 来源 / Source: 巨潮资讯法定风险警示公告
- URL: https://static.cninfo.com.cn/finalpage/2019-04-25/1206091348.PDF

公司因2018年度财务报告被出具无法表示意见，自2019年4月26日起实施退市风险警示并更名*ST雏鹰。审计基础事项包括无法偿付到期债务、众多司法诉讼、银行账户和资产冻结、生产经营受损，以及管理层未能提供改善持续经营能力计划的充分证据。董事会提出剥离非主业资产、债务重组、诉讼应对和聚焦养猪，但尚无已完成的债务削减、资本注入或审计证据。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2020-04-25

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 55.897023
  - **peak_adjusted_close_365d**: 55.897023
  - **as_of_510300_close**: 3.879
  - **stock_close_on_max_excess_date**: 55.897023
  - **etf_close_on_max_excess_date**: 3.879
  - **common_trading_sessions**: 113
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

- `q1-negative-equity-and-cash-conversion-gap`
- `overdue-debt-litigation-and-frozen-assets`
- `first-delisting-risk-warning-audit-disclaimer`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002477.XSHE
  - **ticker**: 002477
  - **name_as_of**: *ST雏鹰
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-04-26
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
  - **row_policy**: stock_code=002477.XSHE; PIT fundamentals and official warning documents available by 2019-04-26; current warning episode starts 2019-04-26; aligned closing prices through 2020-04-25 when observations exist; benchmark=510300.XSHG
  - **st_cause_taxonomy**: operating_financial/debt_crisis+transaction_delisting_risk
  - **matching_group**: current-risk-warning-episode-market-path-365d-v1
  - **matching_role**: no_event_suspension_and_transaction_delisting
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **q1_report**: 4a723a4face2b392c512a6fb2638c2e0535ed10298e8a1cc42cd1f06fb19a229
    - **overdue_notice**: ae5d31291bbee2f7cb9af106724aa906ff82b9ad6dc0196c39d2aa69a4edc0c0
    - **st_notice**: 74a1049ef6c1d893342c39df87b998dc60b0fe1c7bce109ea584bec9d268a6a3
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
    - **window**: 2019-04-26/2020-04-25
    - **stock_code**: 002477.XSHE
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2019-04-26
    - **max_excess_date**: 2019-04-26
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
    - **observation_policy**: Use aligned closing observations that exist inside the fixed calendar window; do not impute prices across suspension or after delisting.
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **current_warning_episode_start**: 2019-04-26
    - **risk_warning_removed_by_window_end**: false

</details>

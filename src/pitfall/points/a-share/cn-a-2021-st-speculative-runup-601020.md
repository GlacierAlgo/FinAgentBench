# cn-a-2021-st-speculative-runup-601020

## Question

你处在2021-04-30收盘后的信息环境，今天是华钰矿业本轮风险警示事件首次以ST华钰交易的日期。请使用下方冻结资料预测未来365个自然日是否出现target定义的异常大幅收盘上涨。公司盈利且经营现金流为正，但现金很薄，审计师无法确认关联方和资金占用完整性并提示持续经营重大不确定性；海外锑金项目和黄金资源又提供高弹性叙事。请分别评估治理折价、融资约束、项目兑现与商品价格暴露，不把非经营性戴帽或矿产储量机械等同于炒作。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST华钰 (601020, SSE)
- 信息截止 / As of: 2021-04-30
- 预测窗口结束 / Window end: 2022-04-30
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以当前风险警示事件首次生效交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改、重整、资产题材或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 华钰矿业2020年报摘要：收入利润为正、经营现金流强，但现金缓冲很薄

- Evidence ID: `annual-profit-cashflow-mineral-projects-and-thin-cash`
- 发布日期 / Published: 2021-04-29
- 来源 / Source: 巨潮资讯法定年报摘要及只读RQData点时记录
- URL: https://static.cninfo.com.cn/finalpage/2021-04-29/1209860984.PDF

2020年营业收入23.789亿元、归母净利润7,238.05万元、扣非归母净利润6,896.63万元，经营活动现金流净额5.4340亿元；期末货币资金仅3,275.30万元，短期借款1.20亿元、流动负债10.132亿元、总负债17.370亿元。公司从事铅锌铜锑银金矿业，披露塔铝金业项目预计2021年下半年投产，并推进泥堡金矿等项目。经营和资源项目提供上行可选性，但现金、建设进度与金属价格均构成约束。

### 华钰矿业2020年审计报告：关联方完整性受限并存在持续经营重大不确定性

- Evidence ID: `qualified-audit-related-parties-and-going-concern`
- 发布日期 / Published: 2021-04-29
- 来源 / Source: 巨潮资讯法定审计报告
- URL: https://static.cninfo.com.cn/finalpage/2021-04-29/1209860987.PDF

审计师出具保留意见：公司补充披露西藏开恒和西藏诚康为关联方，但未提供足够资料，审计师无法判断是否还存在其他未披露关联关系和交易，也无法判断是否涉及关联方资金占用。报告还强调持续经营重大不确定性：期末货币资金约0.33亿元、一年内到期长期借款1.44亿元、对外担保1.70亿元。相关交易授权审批内部控制存在重大缺陷，年度内部控制报告被出具否定意见；盈利和正经营现金流并不能消除治理与偿债尾部风险。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2022-04-30

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 8.1568773
  - **peak_adjusted_close_365d**: 19.3275819
  - **as_of_510300_close**: 5.128
  - **stock_close_on_max_excess_date**: 19.3275819
  - **etf_close_on_max_excess_date**: 4.139
  - **common_trading_sessions**: 242
  - **risk_warning_removed_by_window_end**: 0
- **derivations**:
  - **item 1**:
    - **metric**: max_adjusted_close_return_365d
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - peak_adjusted_close_365d
    - **value**: 1.369482976040353
  - **item 2**:
    - **metric**: stock_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - stock_close_on_max_excess_date
    - **value**: 1.369482976040353
  - **item 3**:
    - **metric**: etf_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_510300_close
      - etf_close_on_max_excess_date
    - **value**: -0.19286271450858028
  - **item 4**:
    - **metric**: max_excess_return_vs_510300_365d
    - **operation**: difference
    - **inputs**:
      - stock_return_on_max_excess_date
      - etf_return_on_max_excess_date
    - **value**: 1.5623456905489332

### 对应的题内资料 / Expected evidence

- `annual-profit-cashflow-mineral-projects-and-thin-cash`
- `qualified-audit-related-parties-and-going-concern`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 601020.XSHG
  - **ticker**: 601020
  - **name_as_of**: ST华钰
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-04-30
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
  - **row_policy**: stock_code=601020.XSHG; quarter=2020q4; info_date=2021-04-29; if_adjusted=0; current warning episode starts 2021-04-30; daily prices 2021-04-30 through 2022-04-30; benchmark=510300.XSHG
  - **st_cause_taxonomy**: non_operating_governance/adverse_internal_control+unresolved_related_party_completeness
  - **matching_group**: current-risk-warning-episode-market-path-365d-v1
  - **matching_role**: event_governance_risk_mineral_optionality
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **annual_report_summary**: b2374a5fefc20144f75d1e86b2b1bdac4d8212e55c84955e26450457b81f4c93
    - **audit_report**: 2656c38be89225a429aa69318d44376e09f86d8ee676b8a0e63866336582bf88
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
    - **window**: 2021-04-30/2022-04-30
    - **stock_code**: 601020.XSHG
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2022-04-13
    - **max_excess_date**: 2022-04-13
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
    - **observation_policy**: Use aligned closing observations that exist inside the fixed calendar window; do not impute prices across suspension or after delisting.
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **current_warning_episode_start**: 2021-04-30
    - **risk_warning_removed_by_window_end**: false

</details>

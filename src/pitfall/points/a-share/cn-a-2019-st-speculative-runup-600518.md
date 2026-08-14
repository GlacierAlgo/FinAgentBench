# cn-a-2019-st-speculative-runup-600518

## Question

你处在2019-05-21收盘后的信息环境，今天是康美药业本轮风险警示事件首次以ST康美交易的日期。请使用下方冻结资料预测未来365个自然日是否出现target定义的异常大幅收盘上涨。会计差错涉及巨额货币资金、收入成本和关联往来，债券与经营流动性压力同时存在。中药资产、品牌与大股东整改承诺不能抵消信息可信度断裂。请区分可能的技术反弹与需要同时满足翻倍、相对510300超额80个百分点的严格事件，不把“重大丑闻后必有妖股行情”作为规则。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST康美 (600518, SSE)
- 信息截止 / As of: 2019-05-21
- 预测窗口结束 / Window end: 2020-05-20
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以当前风险警示事件首次生效交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改、重整、资产题材或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 康美药业实施其他风险警示公告：88.79亿元关联资金用于购买公司股票

- Evidence ID: `st-notice-8.879b-related-fund-flow`
- 发布日期 / Published: 2019-05-18
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2019-05-18/1206283586.PDF

公司自2019年5月21日起变更为ST康美。公告称公司与关联公司存在88.79亿元资金往来，该资金被关联公司用于购买公司股票，触及投资者难以判断公司前景、权益可能受损的情形。公司承认治理、资金管理和关联交易内控存在重大缺陷，只表示督促关联方多途径解决并整改，没有给出锁定资金、清偿时间表或审计验证。

### 康美药业2019年一季报：更正后现金骤降、巨额存货与短债

- Evidence ID: `q1-cash-collapse-inventory-and-short-debt`
- 发布日期 / Published: 2019-04-30
- 来源 / Source: 巨潮资讯法定季度报告
- URL: https://static.cninfo.com.cn/finalpage/2019-04-30/1206168279.PDF

更正口径下，2019年一季度营业收入49.0164亿元、归母净利润2.2088亿元、扣非归母净利润1.7091亿元、经营活动现金流净额6.7395亿元。期末货币资金10.4801亿元，较年初减少43.02%；存货336.6041亿元、短期借款149.40亿元、流动负债249.7790亿元、总负债452.7493亿元。筹资现金流净额-12.9980亿元。正经营现金流远小于资金占用与融资规模，且报表刚经历巨额差错更正。

### 中证网戴帽报道：88.79亿元资金往来直接触发风险警示

- Evidence ID: `contemporaneous-st-report`
- 发布日期 / Published: 2019-05-18
- 来源 / Source: 中国证券报·中证网
- URL: https://www.cs.com.cn/ssgs/gsxw/201905/t20190518_5950494.html

同时点报道确认公司将于5月21日起被实施其他风险警示，原因是88.79亿元关联资金被用于购买公司股票并使投资者难以判断前景。新闻没有提供已经到账的清偿资源或交易所撤销意见，因此只用于交叉核验市场当时可见的信息，不能支持“很快摘帽”的结论。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2020-05-20

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 283.466023
  - **peak_adjusted_close_365d**: 283.466023
  - **as_of_510300_close**: 3.651
  - **stock_close_on_max_excess_date**: 283.466023
  - **etf_close_on_max_excess_date**: 3.651
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

- `st-notice-8.879b-related-fund-flow`
- `q1-cash-collapse-inventory-and-short-debt`
- `contemporaneous-st-report`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600518.XSHG
  - **ticker**: 600518
  - **name_as_of**: ST康美
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-05-21
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
  - **row_policy**: stock_code=600518.XSHG; 2018q4 and 2019q1 PIT fundamentals available by 2019-04-30; current warning episode starts 2019-05-21; daily prices 2019-05-21 through 2020-05-20; benchmark=510300.XSHG
  - **st_cause_taxonomy**: non_operating_governance/false_financial_reporting+related_party_fund_occupation
  - **matching_group**: current-risk-warning-episode-market-path-365d-v1
  - **matching_role**: no_event_major_fraud_and_liquidity_damage
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: 0dbe732b03eb90ba8cd5dabc9757b42700f774d2ad6fb9195777119a249f8172
    - **q1_report**: 684b1c371ca5e2f564b638ad5cbdfd9bd72ae0a36cc041d1bac076475612c402
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
    - **window**: 2019-05-21/2020-05-20
    - **stock_code**: 600518.XSHG
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2019-05-21
    - **max_excess_date**: 2019-05-21
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
    - **observation_policy**: Use aligned closing observations that exist inside the fixed calendar window; do not impute prices across suspension or after delisting.
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **current_warning_episode_start**: 2019-05-21
    - **risk_warning_removed_by_window_end**: false

</details>

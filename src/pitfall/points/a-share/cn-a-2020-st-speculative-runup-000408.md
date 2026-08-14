# cn-a-2020-st-speculative-runup-000408

## Question

你处在2020-05-06收盘后的信息环境，今天是藏格控股本轮风险警示事件首次以*ST藏格交易的日期。请使用下方冻结资料，预测未来365个自然日是否出现target定义的异常大幅收盘上涨。审计无法表示意见、关联占用和巨龙铜业抵债资产的不确定性压低可信度；钾肥经营现金流、资产资源属性与债务清理又可能形成非线性可选性。请把经营修复概率、治理尾部风险、估值/题材弹性与市场基准分开，不把摘帽或锂资源叙事当作翻倍的充分条件。给出概率、二元判断、关键证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST藏格 (000408, SZSE)
- 信息截止 / As of: 2020-05-06
- 预测窗口结束 / Window end: 2021-05-06
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以当前风险警示事件首次生效交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改、重整、资产题材或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 藏格控股退市风险警示公告：2019年财报被出具无法表示意见

- Evidence ID: `star-st-notice-audit-disclaimer`
- 发布日期 / Published: 2020-04-30
- 来源 / Source: 深圳证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-04-30/1207687963.PDF

公司自2020年5月6日起变更为*ST藏格。直接触发条件是2019年度财务会计报告被中审众环出具无法表示意见。董事会提出自查关联资金、强化资产人员财务独立和内部审计，但仅是拟采取措施；若2020年度仍被出具否定或无法表示意见，当时规则下股票可能暂停上市。

### 藏格控股2019年审计报告：低现金、关联占用与巨龙铜业抵债资产风险

- Evidence ID: `audit-report-occupation-and-risky-equity-setoff`
- 发布日期 / Published: 2020-04-30
- 来源 / Source: 巨潮资讯法定审计报告
- URL: https://static.cninfo.com.cn/finalpage/2020-04-30/1207687966.PDF

2019年末货币资金8,209.96万元、应收账款10.6515亿元、其他应收款4.7458亿元，短期借款4.15亿元；营业收入20.6415亿元、归母净利润3.5952亿元、经营活动现金流净额2.7700亿元。附注披露控股股东相关直接占用余额2.6488亿元，并通过客户欠款形成间接占用；公司以25.9亿元受让巨龙铜业37%股权抵偿占款。该联营企业又为关联方约30亿元借款提供担保、存在逾期负债、停建停采和持续经营重大不确定性，说明“以资抵债”并非无风险现金回收。

### 藏格控股2020年一季报PIT财务：利润和经营现金流为正但现金较薄

- Evidence ID: `q1-profitable-operation-but-thin-cash`
- 发布日期 / Published: 2020-04-30
- 来源 / Source: 只读RQData点时财务记录（对应法定一季报）
- URL: https://static.cninfo.com.cn/finalpage/2020-04-30/1207687954.PDF

只读PIT记录显示2020年一季度营业收入2.7242亿元、归母净利润2,438.08万元、扣非归母净利润3,533.01万元、经营活动现金流净额1.1272亿元；期末货币资金6,857.37万元、短期借款2.95亿元、归母净资产78.6092亿元。经营仍能产生现金，但风险警示源于审计证据和治理，而不是单一季度是否盈利。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2021-05-06

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 23.3676924
  - **peak_adjusted_close_365d**: 72.7120914
  - **as_of_510300_close**: 3.918
  - **stock_close_on_max_excess_date**: 72.7120914
  - **etf_close_on_max_excess_date**: 5.061
  - **common_trading_sessions**: 244
  - **risk_warning_removed_by_window_end**: 0
- **derivations**:
  - **item 1**:
    - **metric**: max_adjusted_close_return_365d
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - peak_adjusted_close_365d
    - **value**: 2.1116504854368934
  - **item 2**:
    - **metric**: stock_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - stock_close_on_max_excess_date
    - **value**: 2.1116504854368934
  - **item 3**:
    - **metric**: etf_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_510300_close
      - etf_close_on_max_excess_date
    - **value**: 0.291730474732006
  - **item 4**:
    - **metric**: max_excess_return_vs_510300_365d
    - **operation**: difference
    - **inputs**:
      - stock_return_on_max_excess_date
      - etf_return_on_max_excess_date
    - **value**: 1.8199200107048874

### 对应的题内资料 / Expected evidence

- `star-st-notice-audit-disclaimer`
- `audit-report-occupation-and-risky-equity-setoff`
- `q1-profitable-operation-but-thin-cash`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000408.XSHE
  - **ticker**: 000408
  - **name_as_of**: *ST藏格
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-05-06
  - **allowed_domains**:
    - cninfo.com.cn
    - szse.cn
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
  - **row_policy**: stock_code=000408.XSHE; quarter=2020q1 and 2019q4 PIT records available by 2020-04-30; current warning episode starts 2020-05-06; daily prices 2020-05-06 through 2021-05-06; benchmark=510300.XSHG
  - **st_cause_taxonomy**: mixed_delisting_and_governance/audit_disclaimer+related_party_fund_occupation
  - **matching_group**: current-risk-warning-episode-market-path-365d-v1
  - **matching_role**: event_audit_disclaimer_resource_optionality
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: eef850276dc97754959ec1148d1909c36978a194951d2dc4e386371b5c2f3d06
    - **audit_report**: 1048a3e2adbd166c9dd05ea810d5bb0afb3adaaf949d38a454f180856b69ac69
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
    - **window**: 2020-05-06/2021-05-06
    - **stock_code**: 000408.XSHE
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2021-05-06
    - **max_excess_date**: 2021-05-06
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
    - **observation_policy**: Use aligned closing observations that exist inside the fixed calendar window; do not impute prices across suspension or after delisting.
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **current_warning_episode_start**: 2020-05-06
    - **risk_warning_removed_by_window_end**: false

</details>

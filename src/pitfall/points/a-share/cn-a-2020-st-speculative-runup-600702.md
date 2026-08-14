# cn-a-2020-st-speculative-runup-600702

## Question

你处在2020-09-22收盘后的信息环境，今天是舍得酒业首次以ST舍得交易的日期。请使用下方冻结资料，预测未来365个自然日是否会出现target定义的异常大幅收盘上涨。先区分戴帽原因属于经营恶化、会计/偿债风险还是非经营性资金占用与治理失灵，再评估占用资金可修复性、控制权变化选项、白酒经营质量、行业景气与公司真实暴露、现金流和资产负债表约束。不要把摘帽、重整、行业上涨或后来股价上涨互相作因果替代。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST舍得 (600702, SSE)
- 信息截止 / As of: 2020-09-22
- 预测窗口结束 / Window end: 2021-09-22
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以首次实施风险警示交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1.0` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 舍得酒业实施其他风险警示公告：4.7486亿元资金占用未按承诺归还

- Evidence ID: `st-notice-cause-and-unresolved-occupation`
- 发布日期 / Published: 2020-09-21
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2020-09-21/600702_20200921_1.pdf

公告称公司自2020年9月22日起变更为ST舍得，日涨跌幅限制5%。截至2020年8月19日，间接控股股东天洋控股及关联方非经营性占用本金4.40亿元、利息3,486万元，合计4.7486亿元；截至公告日仍未在9月19日承诺期限前归还。董事会提出督促筹资、制定还款计划，并明确可能通过股权转让等方式弥补占用。戴帽直接原因是非经营性资金占用与治理问题，而不是年报亏损触发的退市风险警示；但资金是否能回收及控制权路径高度不确定。

### 舍得酒业2020年半年度报告：高毛利主业承压、经营现金流为负并出现大额拆借

- Evidence ID: `h1-financials-and-liquor-operations`
- 发布日期 / Published: 2020-08-29
- 来源 / Source: 上海证券交易所法定半年度报告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2020-08-29/600702_20200829_2.pdf

2020年上半年营业收入10.2590亿元，同比下降15.95%；归母净利润1.6419亿元，同比下降11.45%；扣非归母净利润1.4723亿元；经营活动现金流净额-6,145.03万元。营业成本2.5646亿元，对应综合毛利率约75%。期末货币资金11.5877亿元、短期借款10.04亿元、存货25.2790亿元、归母净资产32.1723亿元。其他应收款从年初4,665.09万元增至5.2505亿元，其中对蓬山酒业拆借款本金4.40亿元及占用费3,160万元；报告称疫情使销售、回款和营销活动下降。高毛利、品牌和存酒资产与治理抽血、负经营现金流同时存在。

### 中证网食品饮料行业观点：白酒场景复苏但板块分化，舍得中报被列为超预期

- Evidence ID: `contemporaneous-liquor-recovery-and-differentiation`
- 发布日期 / Published: 2020-09-08
- 来源 / Source: 中国证券报·中证网转载的兴业证券行业观点
- URL: https://www.cs.com.cn/gppd/sdqs/202009/t20200908_6092739.html

同时点行业观点认为疫情冲击具有阶段性，白酒三季度复苏弹性可期，但竞争格局将进一步分化，高端酒更稳健、区域次高端品牌才可能持续增长。观点明确将舍得酒业列为中报超预期、值得重点关注的公司之一，同时列示宏观下滑、成本上升、食品安全和行业竞争等风险。这提供当时已有的行业与公司经营预期，不能证明资金占用会解决，也不能直接推出股价路径。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `large_post_st_speculative_runup`
- 结果日期 / Resolved at: 2021-09-22

### 实际结果 / Realized outcome

- **observations**:
  - **as_of_adjusted_close**: 107.0687656
  - **peak_adjusted_close_365d**: 836.3426403
  - **as_of_510300_close**: 4.699
  - **stock_close_on_max_excess_date**: 836.3426403
  - **etf_close_on_max_excess_date**: 5.204
  - **common_trading_sessions**: 243
  - **risk_warning_removed_by_window_end**: 1
- **derivations**:
  - **item 1**:
    - **metric**: max_adjusted_close_return_365d
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - peak_adjusted_close_365d
    - **value**: 6.811266298002411
  - **item 2**:
    - **metric**: stock_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - stock_close_on_max_excess_date
    - **value**: 6.811266298002411
  - **item 3**:
    - **metric**: etf_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_510300_close
      - etf_close_on_max_excess_date
    - **value**: 0.10746967439880817
  - **item 4**:
    - **metric**: max_excess_return_vs_510300_365d
    - **operation**: difference
    - **inputs**:
      - stock_return_on_max_excess_date
      - etf_return_on_max_excess_date
    - **value**: 6.703796623603603

### 对应的题内资料 / Expected evidence

- `st-notice-cause-and-unresolved-occupation`
- `h1-financials-and-liquor-operations`
- `contemporaneous-liquor-recovery-and-differentiation`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600702.XSHG
  - **ticker**: 600702
  - **name_as_of**: ST舍得
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-09-22
  - **allowed_domains**:
    - sse.com.cn
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
  - **row_policy**: stock_code=600702.XSHG; if_adjusted=0 for 2020q2 PIT fundamentals; daily prices from 2020-09-22 through 2021-09-22; benchmark=510300.XSHG
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation
  - **matching_group**: first-st-day-governance-risk-365d-v1
  - **matching_role**: event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: 6a964e0c45d9afc2f6b1f2a360c820253ebb51f5d69e6a90bfc69031b665e16d
    - **2020_half_year_report**: 00679be8d6b8fb0dee1e9b81b32bebbae9717c4a18648813ea4450cc36a29475
  - **news_evidence_policy**: Only contemporaneous industry framing published no later than as_of may enter the corpus; it cannot reveal or define the future price label.
  - **outcome_label_policy**: Stock backward-adjusted closes and raw 510300 closes are aligned by trade_date; maxima use closing observations only over the predeclared 365-calendar-day window.
  - **causal_guardrail**: The label measures an ex post market path, not whether ST designation, remediation, control transfer, or fundamentals caused that path.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: rqdata_daily_price
    - **paths**:
      - data/db/rq_adj_bwd_price_daily/trade_date=YYYY-MM-DD/data.parquet
      - data/db/etf_raw_price_daily/trade_date=YYYY-MM-DD/data.parquet
    - **window**: 2020-09-22/2021-09-22
    - **stock_code**: 600702.XSHG
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2021-07-21
    - **max_excess_date**: 2021-07-21
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **st_start**: 2020-09-22
    - **risk_warning_removed**: 2021-05-19

</details>

# cn-a-2021-st-speculative-runup-600078

## Question

你处在2021-05-06收盘后的信息环境，今天是澄星股份首次以*ST澄星交易的日期。请使用下方冻结资料，预测未来365个自然日是否会出现target定义的异常大幅收盘上涨。请拆分负净资产、无法表示意见、控股股东资金占用、债务压力和黄磷产业链景气，不要把原料涨价机械等同于公司利润改善；同时评估存量产能、产品结构、经营现金流、重整或控制权选项与退市尾部风险。不要把摘帽、重整或后来股价上涨作因果捷径。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST澄星 (600078, SSE)
- 信息截止 / As of: 2021-05-06
- 预测窗口结束 / Window end: 2022-05-06
- 目标事件 / Target: `large_post_st_speculative_runup`
- 判定定义 / Definition: 市场路径事件而非因果归因：以首次实施风险警示交易日收盘价为基准，未来365个自然日内的最大后复权收盘收益不低于100%，且任一同期交易日相对沪深300ETF（510300.XSHG）的最大累计收益差不低于80个百分点；两项极值可以发生在不同日期，不使用盘中最高价，也不声称戴帽、整改或行业景气导致上涨

#### 判定条件 / Criteria

- `max_adjusted_close_return_365d >= 1.0` — 窗口内最大后复权收盘收益不低于100%
- `max_excess_return_vs_510300_365d >= 0.8` — 窗口内相对沪深300ETF的最大同期累计收益差不低于80个百分点

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 澄星股份退市风险警示公告：负净资产、无法表示意见、内控否定与资金占用并存

- Evidence ID: `star-st-notice-multiple-triggers`
- 发布日期 / Published: 2021-04-30
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/new/2021-04-30/600078_20210430_20.pdf

公司自2021年5月6日起变更为*ST澄星，日涨跌幅限制5%。公告列出四类相互叠加的风险：2020年度财务报告内部控制被出具否定意见；控股股东及关联方资金占用到期未解决；经审计期末净资产为负；年度财务报告被出具无法表示意见。因此公司既触发其他风险警示，也触发退市风险警示。董事会仅表示将督促控股股东多途径解决占用并加强内控，没有给出已锁定的清偿资源或完成日期。

### 澄星股份2020年年度报告：22.16亿元亏损、负权益与黄磷产品敞口

- Evidence ID: `annual-loss-debt-and-phosphorus-exposure`
- 发布日期 / Published: 2021-04-30
- 来源 / Source: 上海证券交易所法定年度报告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/new/2021-04-30/600078_20210430_2.pdf

2020年营业收入31.3655亿元，同比下降5.24%；归母净利润-22.1586亿元，扣非归母净利润-22.5797亿元；期末归母净资产-4.7615亿元。经营活动现金流净额7.3079亿元为正，但货币资金仅3.9637亿元，短期借款37.1544亿元，流动负债50.2446亿元而流动资产16.4127亿元。报告披露控股股东及相关方期末非经营性占用21.7760亿元，其中通过绿澄化工形成15.6789亿元。黄磷收入9.7279亿元、同比增长43.38%，销量7.06万吨、期末库存3.80万吨，但黄磷毛利率仅10.08%且同比下降5.93个百分点。行业敞口、正经营现金流与极端偿债/治理风险并存。

### 2021年4月化工行业报告：草甘膦景气与黄磷成本传导

- Evidence ID: `contemporaneous-yellow-phosphorus-chain-pricing`
- 发布日期 / Published: 2021-04-30
- 来源 / Source: 国信证券行业报告（东方财富PDF镜像）
- URL: https://pdf.dfcfw.com/pdf/H3_AP202105061490021000_1.pdf

行业报告称截至4月28日草甘膦报价35,312元/吨，较年初上涨29.09%、同比上涨约73%，生产商订单多排至2021年8月；黄磷报价17,481元/吨，较年初上涨10.46%，是甘氨酸法草甘膦的重要成本项之一。报告判断环保约束、供应偏紧和农产品景气可能支撑产业链，但重点标的是草甘膦龙头，不是澄星股份。对澄星只能把黄磷价格作为潜在经营杠杆，必须结合其产销、毛利、债务和资金占用，不能把下游景气直接移植为公司利润或股价结论。

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
  - **as_of_adjusted_close**: 15.9294342
  - **peak_adjusted_close_365d**: 79.9998522
  - **as_of_510300_close**: 5.061
  - **stock_close_on_max_excess_date**: 77.2371828
  - **etf_close_on_max_excess_date**: 4.064
  - **common_trading_sessions**: 243
  - **risk_warning_removed_by_window_end**: 0
- **derivations**:
  - **item 1**:
    - **metric**: max_adjusted_close_return_365d
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - peak_adjusted_close_365d
    - **value**: 4.022140221402214
  - **item 2**:
    - **metric**: stock_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_adjusted_close
      - stock_close_on_max_excess_date
    - **value**: 3.8487084870848713
  - **item 3**:
    - **metric**: etf_return_on_max_excess_date
    - **operation**: pct_change
    - **inputs**:
      - as_of_510300_close
      - etf_close_on_max_excess_date
    - **value**: -0.19699664098004344
  - **item 4**:
    - **metric**: max_excess_return_vs_510300_365d
    - **operation**: difference
    - **inputs**:
      - stock_return_on_max_excess_date
      - etf_return_on_max_excess_date
    - **value**: 4.045705128064915

### 对应的题内资料 / Expected evidence

- `star-st-notice-multiple-triggers`
- `annual-loss-debt-and-phosphorus-exposure`
- `contemporaneous-yellow-phosphorus-chain-pricing`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_outcomes_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600078.XSHG
  - **ticker**: 600078
  - **name_as_of**: *ST澄星
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-05-06
  - **allowed_domains**:
    - sse.com.cn
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
  - **row_policy**: stock_code=600078.XSHG; if_adjusted=0 for 2020q4 PIT fundamentals; daily prices from 2021-05-06 through 2022-05-06; benchmark=510300.XSHG
  - **st_cause_taxonomy**: mixed_delisting_and_governance/negative_equity+audit_disclaimer+related_party_fund_occupation
  - **matching_group**: first-st-day-governance-risk-365d-v1
  - **matching_role**: event_hard_mixed_cause
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: 0a159af4d13992484fc30f9331f9fb523cc32ac9918ba8fee814fb75ee17efad
    - **2020_annual_report**: 525a725eb1ff14d84fb882213090432709f489a5963c963887771970e8644379
    - **contemporaneous_industry_report**: 50a099ec575f6587928aaa270ce3896509d227a7d46e6067260369cfae54a6f9
  - **news_evidence_policy**: The contemporaneous chemical-industry report supplies only point-in-time price-chain context; company filings remain the authority on direct exposure and balance-sheet risk.
  - **outcome_label_policy**: Stock backward-adjusted closes and raw 510300 closes are aligned by trade_date; maxima use closing observations only over the predeclared 365-calendar-day window.
  - **causal_guardrail**: The label measures an ex post market path, not whether commodity prices, ST designation, remediation, restructuring, or fundamentals caused that path.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: rqdata_daily_price
    - **paths**:
      - data/db/rq_adj_bwd_price_daily/trade_date=YYYY-MM-DD/data.parquet
      - data/db/etf_raw_price_daily/trade_date=YYYY-MM-DD/data.parquet
    - **window**: 2021-05-06/2022-05-06
    - **stock_code**: 600078.XSHG
    - **benchmark**: 510300.XSHG
    - **total_return_peak_date**: 2021-12-16
    - **max_excess_date**: 2022-04-20
    - **formula**: stock_return=close_t/close_as_of-1; etf_return=etf_close_t/etf_close_as_of-1; excess=stock_return-etf_return
  - **item 2**:
    - **type**: rqdata_st_status
    - **path**: data/db/is_st.parquet
    - **st_start**: 2021-05-06
    - **risk_warning_removed_by_window_end**: false
    - **note**: The star-ST designation was downgraded later, but full risk-warning removal did not occur inside the price window.

</details>

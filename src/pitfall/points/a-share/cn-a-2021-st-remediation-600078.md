# cn-a-2021-st-remediation-600078

## Question

你处在2021-05-06收盘后的信息环境。*ST澄星同时存在负净资产、无法表示意见、内控否定和21.78亿元关联占用。请使用下方冻结资料，预测未来24个自然月内是否会发生target定义的完整撤销全部风险警示。分别分析财务类退市风险、其他风险警示、占款清偿、审计意见和交易所审核；即使未来从*ST降为ST，只要仍留在风险警示板就不算事件。黄磷价格上涨也不能替代资产负债表修复。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST澄星 (600078, SSE)
- 信息截止 / As of: 2021-05-06
- 预测窗口结束 / Window end: 2023-05-06
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来24个自然月内，证券交易所审核同意撤销公司股票交易的全部退市风险警示和全部其他风险警示，且生效后的证券简称不再含ST或*ST、股票退出风险警示板。仅提交或获董事会通过申请、占款或担保已清偿、审计意见改善、撤销一项叠加警示但仍保留任一风险警示、*ST降为ST、暂停上市后恢复或最终退市均不计为事件

#### 判定条件 / Criteria

- `full_risk_warning_removal_count_24m >= 1` — 窗口内经交易所审核同意并生效的完整撤销全部风险警示至少一次

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

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 结果日期 / Resolved at: 2023-05-06

### 实际结果 / Realized outcome

- **observations**:
  - **full_risk_warning_removal_count_24m**: 0
  - **full_risk_warning_removed_by_window_end**: 0
  - **partial_only_removal_count_24m**: 1
  - **calendar_days_to_full_removal_or_zero**: 0
  - **risk_warning_present_at_window_end**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `star-st-notice-multiple-triggers`
- `annual-loss-debt-and-phosphorus-exposure`
- `contemporaneous-yellow-phosphorus-chain-pricing`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_remediation_v1
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
    - is_st
    - special_treatment_info
  - **row_policy**: stock_code=600078.XSHG; if_adjusted=0 for 2020q4 PIT fundamentals; risk-warning events/status checked through the fixed 24-month window
  - **st_cause_taxonomy**: mixed_delisting_and_governance/negative_equity+audit_disclaimer+related_party_fund_occupation
  - **matching_group**: first-risk-warning-day-full-removal-24m-v1
  - **matching_role**: no_event_hard_control
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: 0a159af4d13992484fc30f9331f9fb523cc32ac9918ba8fee814fb75ee17efad
    - **2020_annual_report**: 525a725eb1ff14d84fb882213090432709f489a5963c963887771970e8644379
    - **contemporaneous_industry_report**: 50a099ec575f6587928aaa270ce3896509d227a7d46e6067260369cfae54a6f9
  - **news_evidence_policy**: The contemporaneous chemical-industry report supplies only point-in-time price-chain context; company filings remain the authority on direct exposure and balance-sheet risk.
  - **outcome_contract**: Only an exchange-approved removal of every ST/*ST warning that becomes effective inside the 24-calendar-month window counts. An application, remediation, *ST-to-ST downgrade, continued ST status, or delisting does not.
  - **status_source_sha256**:
    - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
    - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
  - **leakage_guard**: All removal approvals, later ST transitions, restructurings, delistings and post-as_of remediation facts remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: rqdata_risk_warning_status_crosscheck
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2021-05-06/2023-05-06
    - **full_removal_within_window**: false
    - **partial_only_removal_count_24m**: 1
    - **later_context_not_counted**: 2022-08-16仅由*ST澄星降为ST澄星，仍留在风险警示板；完整摘帽直到2024-06-24才生效。

</details>

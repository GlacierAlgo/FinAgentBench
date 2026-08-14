# cn-a-2021-st-remediation-000525

## Question

你处在2021-05-06收盘后的信息环境。ST红太阳因近29.64亿元非经营性占用与内部控制否定意见而戴帽，且此前部分所谓归还资金又被质押划转。请使用下方冻结资料，预测未来24个自然月内是否会发生target定义的完整撤销全部风险警示。必须把农化行业景气与公司清偿能力分开，检验占款真实性、控制人融资链、审计验证和交易所审核；重整预期、行业涨价或撤销一项叠加警示均不算完整摘帽。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST红太阳 (000525, SZSE)
- 信息截止 / As of: 2021-05-06
- 预测窗口结束 / Window end: 2023-05-06
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来24个自然月内，证券交易所审核同意撤销公司股票交易的全部退市风险警示和全部其他风险警示，且生效后的证券简称不再含ST或*ST、股票退出风险警示板。仅提交或获董事会通过申请、占款或担保已清偿、审计意见改善、撤销一项叠加警示但仍保留任一风险警示、*ST降为ST、暂停上市后恢复或最终退市均不计为事件

#### 判定条件 / Criteria

- `full_risk_warning_removal_count_24m >= 1` — 窗口内经交易所审核同意并生效的完整撤销全部风险警示至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 红太阳实施其他风险警示公告：近29.64亿元占用预计一个月内无法解决

- Evidence ID: `st-notice-near-three-billion-occupation`
- 发布日期 / Published: 2021-04-29
- 来源 / Source: 深圳证券交易所法定公告PDF镜像
- URL: https://pdf.dfcfw.com/pdf/H2_AN202104291488680395_1.pdf

公司自2021年5月6日起变更为ST红太阳，日涨跌幅限制5%。公告称截至2021年4月28日，控股股东南一农集团及关联方非经营性占用余额29.639845亿元，预计无法在一个月内解决；2020年度内部控制审计报告为否定意见。公告解释控股股东流动性危机源于融资收紧，并披露部分所谓归还资金随后又被用于为控股股东和红太阳集团融资提供担保质押，最终被银行划转，显示资金回流并不等于风险实质消除。公司同时仍处于证监会立案调查期间。

### 红太阳2020年年度报告：农药主业、扣非亏损和现金短债矛盾

- Evidence ID: `annual-agrochemical-financial-stress`
- 发布日期 / Published: 2021-04-30
- 来源 / Source: 巨潮资讯法定年度报告
- URL: https://static.cninfo.com.cn/finalpage/2021-04-30/1209871241.PDF

2020年营业收入40.2200亿元，同比下降12.84%；归母净利润-1.5381亿元，扣非归母净利润-2.6609亿元；经营活动现金流净额2.3124亿元。农药销售收入39.8589亿元、占收入99.10%，毛利率18.77%，同比下降13.49个百分点；产量22.90万吨、销量19.50万吨、库存同比增长17%。期末货币资金1.9811亿元，短期借款37.9076亿元，流动资产55.8644亿元低于流动负债64.6997亿元；其他应收款32.2476亿元，接近当年收入的80%，主要风险与关联占用一致。年报称出口和汇率受疫情冲击，并计提存货与应收减值1.0635亿元。

### 2021年4月农化行业报告：草甘膦涨价，但不可无证据外推到红太阳

- Evidence ID: `sector-boom-with-exposure-attribution-trap`
- 发布日期 / Published: 2021-04-30
- 来源 / Source: 国信证券行业报告（东方财富PDF镜像）
- URL: https://pdf.dfcfw.com/pdf/H3_AP202105061490021000_1.pdf

行业报告称草甘膦报价35,312元/吨，30日上涨12.10%，较年初上涨29.09%，并判断全球粮食安全、供给集中和高开工率可能延长景气；其列示的主要草甘膦企业包括兴发、江山、新安和扬农，并未列出红太阳。红太阳年报只按“农药销售”汇总披露，未在该表证明草甘膦原药产能。因此该报告既是行业上行信号，也是暴露归因陷阱：模型必须寻找公司产品结构证据，不能把热门品种涨价自动当成红太阳盈利催化。

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
  - **partial_only_removal_count_24m**: 0
  - **calendar_days_to_full_removal_or_zero**: 0
  - **risk_warning_present_at_window_end**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-near-three-billion-occupation`
- `annual-agrochemical-financial-stress`
- `sector-boom-with-exposure-attribution-trap`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_remediation_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000525.XSHE
  - **ticker**: 000525
  - **name_as_of**: ST红太阳
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-05-06
  - **allowed_domains**:
    - cninfo.com.cn
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
  - **row_policy**: stock_code=000525.XSHE; if_adjusted=0 for 2020q4 PIT fundamentals; risk-warning events/status checked through the fixed 24-month window
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation+adverse_internal_control
  - **matching_group**: first-risk-warning-day-full-removal-24m-v1
  - **matching_role**: no_event_hard_control
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice_exchange_mirror**: a09e14a6a5860d11fcfb194c5449bcf87e94edd3ca4951aa85dca44bde64ddf6
    - **2020_annual_report**: 92441de1093f0fbf952e60343afe48da4852733508b35c83b487700dbc51fa0c
  - **news_evidence_policy**: A contemporaneous sector report is deliberately included as a possible exposure-misattribution trap; the company filing must support any claimed product linkage.
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
    - **partial_only_removal_count_24m**: 0
    - **later_context_not_counted**: 截至2023-05-06窗口末仍为ST红太阳；完整撤销其他风险警示直到2025-06-13才生效。

</details>

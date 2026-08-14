# cn-a-2021-st-remediation-002168

## Question

你处在2021-03-03收盘后的信息环境。ST惠程因控股股东及关联方未按期归还非经营性占用资金而首次戴帽；此前已累计归还3.101542亿元，余额为6,067.49万元，并承诺最迟在年报前解决。请使用下方冻结资料，预测未来24个自然月内是否会发生target定义的完整撤销全部风险警示。请核验剩余金额相对已归还金额、上市公司现金和净资产的比例，区分可执行现金来源与控制人承诺，同时考虑高商誉、主业盈利和内控复发风险；不要把还款承诺或媒体判断直接当作交易所批准。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST惠程 (002168, SZSE)
- 信息截止 / As of: 2021-03-03
- 预测窗口结束 / Window end: 2023-03-03
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来24个自然月内，证券交易所审核同意撤销公司股票交易的全部退市风险警示和全部其他风险警示，且生效后的证券简称不再含ST或*ST、股票退出风险警示板。仅提交或获董事会通过申请、占款或担保已清偿、审计意见改善、撤销一项叠加警示但仍保留任一风险警示、*ST降为ST、暂停上市后恢复或最终退市均不计为事件

#### 判定条件 / Criteria

- `full_risk_warning_removal_count_24m >= 1` — 窗口内经交易所审核同意并生效的完整撤销全部风险警示至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 惠程科技实施其他风险警示公告：已还3.10亿元但6,067.49万元余额逾期

- Evidence ID: `st-notice-small-residual-after-large-repayments`
- 发布日期 / Published: 2021-03-02
- 来源 / Source: 深圳证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2021-03-02/1209318659.PDF

公司自2021年3月3日起变更为ST惠程。公告称控股股东中驰惠程及关联方非经营性占用上市公司资金；截至公告日累计已归还31,015.42万元，余额6,067.49万元，但未能在3月2日前完成归还，因而触发其他风险警示。控制人承诺在2020年年报披露前、尽量一个月内以现金、现金等价物或优质资产抵债解决。已归还大部分和明确短期承诺提高可修复性，但公告没有证明剩余款项已进入公司账户。

### 惠程科技2020年三季报：小幅盈利、现金流转正与高商誉并存

- Evidence ID: `q3-positive-cash-flow-but-large-goodwill`
- 发布日期 / Published: 2020-10-30
- 来源 / Source: 巨潮资讯法定季度报告
- URL: https://static.cninfo.com.cn/finalpage/2020-10-30/1208652937.PDF

2020年前三季度营业收入6.7623亿元，归母净利润2,570.66万元，扣非归母净利润2,220.41万元，经营活动现金流净额1.6886亿元。期末货币资金2.6226亿元、短期借款1.57亿元、流动负债6.0970亿元、归母净资产18.3828亿元；商誉12.2060亿元，约为归母净资产的66%。剩余占用款相对账面净资产不大，但上市公司自身资产质量和高商誉意味着不能只看一个清偿比例。

### 戴帽前媒体报道：2月25日再还2.01亿元，剩余6,067.49万元

- Evidence ID: `pre-st-media-repayment-trajectory`
- 发布日期 / Published: 2021-03-01
- 来源 / Source: 中国农业银行报转载的市场观察
- URL: https://paper.people.com.cn/zgnyb/html/2021-03/01/content_2036466.htm

截至戴帽前的公开报道，控股股东在2月25日通过银行转账归还2.01亿元，加上此前1.09亿元，累计归还约3.10亿元，非经营性占用余额为6,067.49万元。该付款轨迹是比口头承诺更强的点时证据，但最后一笔是否按期到账、是否还有其他风险警示原因以及交易所是否批准仍需独立判断。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 结果日期 / Resolved at: 2021-04-09

### 实际结果 / Realized outcome

- **observations**:
  - **full_risk_warning_removal_count_24m**: 1
  - **full_risk_warning_removed_by_window_end**: 1
  - **partial_only_removal_count_24m**: 0
  - **calendar_days_to_full_removal_or_zero**: 37
  - **risk_warning_present_at_window_end**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-small-residual-after-large-repayments`
- `q3-positive-cash-flow-but-large-goodwill`
- `pre-st-media-repayment-trajectory`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_remediation_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002168.XSHE
  - **ticker**: 002168
  - **name_as_of**: ST惠程
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-03-03
  - **allowed_domains**:
    - cninfo.com.cn
    - people.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - is_st
    - special_treatment_info
  - **row_policy**: stock_code=002168.XSHE; quarter=2020q3; info_date=2020-10-30; if_adjusted=0; first risk-warning trading day=2021-03-03
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation
  - **matching_group**: first-risk-warning-day-full-removal-24m-v1
  - **matching_role**: event_fast_remediation
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: dd6b96e80d3d50dcb504b0f7d86897be967d9a2f3c23252c80515f09e0e615fb
    - **q3_report**: be6130f02b33c04743ab48fbd40090fb6f0e40a0a5b49090c51101bbb6dc6c37
  - **status_source_sha256**:
    - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
    - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
  - **outcome_contract**: Only an exchange-approved removal of every ST/*ST warning that becomes effective inside the 24-calendar-month window counts. An application, remediation, *ST-to-ST downgrade, continued ST status, or delisting does not.
  - **news_evidence_policy**: Only documents published no later than as_of enter the frozen corpus. Media reporting is an attributed point-in-time clue, never label authority.
  - **leakage_guard**: All removal approvals, later ST transitions, restructurings, delistings and post_as_of remediation facts remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_exchange_approved_full_risk_warning_removal
    - **title**: 惠程科技关于公司股票撤销其他风险警示暨停牌的公告
    - **approved_effective_date**: 2021-04-09
    - **published_at**: 2021-04-09
    - **url**: https://static.cninfo.com.cn/finalpage/2021-04-08/1209648558.PDF
    - **sha256**: 7ac498f4d5f799406940d6dcc5a92e206f41fca7881cdbae486009261ee0e023
    - **resulting_symbol**: 惠程科技
    - **exits_risk_warning_board**: true
    - **all_risk_warnings_removed**: true
  - **item 2**:
    - **type**: rqdata_risk_warning_status_crosscheck
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2021-03-03/2023-03-03
    - **full_removal_within_window**: true
    - **partial_only_removal_count_24m**: 0

</details>

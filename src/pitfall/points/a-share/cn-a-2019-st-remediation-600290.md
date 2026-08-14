# cn-a-2019-st-remediation-600290

## Question

你处在2019-12-26收盘后的信息环境。ST华仪因10.58亿元占用和9.259亿元违规担保未在承诺期内解决而戴帽，主营收入、扣非利润和应收质量也偏弱。请使用下方冻结资料，预测未来24个自然月内是否会发生target定义的完整撤销全部风险警示。分别评估控股股东可执行的清偿资源、违规担保司法解除、经营和审计新增风险、以及交易所最终审核；特别注意未来即使退市风险警示被降级为其他风险警示，仍不等于完整摘帽。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST华仪 (600290, SSE)
- 信息截止 / As of: 2019-12-26
- 预测窗口结束 / Window end: 2021-12-26
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来24个自然月内，证券交易所审核同意撤销公司股票交易的全部退市风险警示和全部其他风险警示，且生效后的证券简称不再含ST或*ST、股票退出风险警示板。仅提交或获董事会通过申请、占款或担保已清偿、审计意见改善、撤销一项叠加警示但仍保留任一风险警示、*ST降为ST、暂停上市后恢复或最终退市均不计为事件

#### 判定条件 / Criteria

- `full_risk_warning_removal_count_24m >= 1` — 窗口内经交易所审核同意并生效的完整撤销全部风险警示至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 华仪电气实施其他风险警示公告：10.58亿元占用与9.259亿元违规担保

- Evidence ID: `st-notice-occupation-and-guarantees`
- 发布日期 / Published: 2019-12-25
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2019-12-25/600290_20191225_1.pdf

公司自2019年12月26日起变更为ST华仪。公告称违规担保金额9.2590亿元，占最近一期经审计净资产22.75%，其中逾期担保2.14亿元；关联方资金占用余额10.58亿元，占净资产26.00%。控股股东未在自2019年11月25日起一个月的承诺期限内解决，直接触发其他风险警示。公告没有可验证的还款资金，只表示继续催促、通过法律途径处理并至少每月披露进展。

### 华仪电气2019年三季报：账面现金较高，但收入、扣非利润与应收质量偏弱

- Evidence ID: `q3-cash-receivables-and-weak-operations`
- 发布日期 / Published: 2019-10-31
- 来源 / Source: 上海证券交易所法定季度报告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2019-10-31/600290_2019_3.pdf

2019年前三季度营业收入8.0757亿元，同比下降25.75%；归母净利润1,102.28万元，同比下降36.04%，扣非归母净利润-2,982.85万元；经营活动现金流净额1.0042亿元。期末货币资金15.7874亿元、短期借款5.3413亿元，看似流动性充裕，但应收账款21.0521亿元，是前三季度收入的约2.61倍，另有预付款2.5007亿元。结合随后披露的10.58亿元控股股东占用，账面现金不能被机械视为可自由使用资金。

### 2019年风电设备行业观点：三年抢装开启，但采购向龙头集中

- Evidence ID: `wind-installation-boom-and-leader-concentration`
- 发布日期 / Published: 2019-06-03
- 来源 / Source: 中国证券报·中证网转载的兴业证券行业观点
- URL: https://www.cs.com.cn/gppd/sdqs/201906/t20190603_5954690.html

行业观点预计补贴并网期限推动2019至2021年风电持续抢装，年均装机规模可能超过30GW，短期需求和盈利迎来拐点；同时强调平价时代运营商更重视发电效率、产品质量和运维费用，市场份额可能进一步向龙头集中。推荐名单聚焦金风科技、天顺风能等细分龙头，没有华仪电气。该材料说明行业总量向好和尾部厂商兑现可能分化，不能用“风电抢装”掩盖公司应收、占用与治理风险。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 结果日期 / Resolved at: 2021-12-26

### 实际结果 / Realized outcome

- **observations**:
  - **full_risk_warning_removal_count_24m**: 0
  - **full_risk_warning_removed_by_window_end**: 0
  - **partial_only_removal_count_24m**: 1
  - **calendar_days_to_full_removal_or_zero**: 0
  - **risk_warning_present_at_window_end**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-occupation-and-guarantees`
- `q3-cash-receivables-and-weak-operations`
- `wind-installation-boom-and-leader-concentration`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_remediation_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600290.XSHG
  - **ticker**: 600290
  - **name_as_of**: ST华仪
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-12-26
  - **allowed_domains**:
    - sse.com.cn
    - cs.com.cn
    - ce.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - is_st
    - special_treatment_info
  - **row_policy**: stock_code=600290.XSHG; if_adjusted=0 for 2019q3 PIT fundamentals; risk-warning events/status checked through the fixed 24-month window
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation+illegal_guarantees
  - **matching_group**: first-risk-warning-day-full-removal-24m-v1
  - **matching_role**: no_event_hard_control
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: d6aad276b1294a65a1bfaaa71f7591236bb680d8f10c04e972b916147f43bc67
    - **2019_third_quarter_report**: 53fa5ec62fdfab02628c876388e25e3705497e8bcd6e49e9a22aff3cfde66314
  - **news_evidence_policy**: Contemporaneous news may frame the wind-installation cycle and disclosed governance failures; official filings and RQData remain label authority.
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
    - **window**: 2019-12-26/2021-12-26
    - **full_removal_within_window**: false
    - **partial_only_removal_count_24m**: 1
    - **later_context_not_counted**: 窗口内2021-05-17仅由*ST华仪降为ST华仪，仍在风险警示板；此后再次*ST并退市，从未完整摘帽。

</details>

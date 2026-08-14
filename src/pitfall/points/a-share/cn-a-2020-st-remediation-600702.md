# cn-a-2020-st-remediation-600702

## Question

你处在2020-09-22收盘后的信息环境。ST舍得因4.7486亿元非经营性资金占用未按承诺归还而首次戴帽，但白酒主业仍有高毛利、品牌和存酒资产。请使用下方冻结资料，预测未来24个自然月内是否会发生target定义的完整撤销全部风险警示。把占款清偿、控制权变化、内控修复、交易所审核和经营持续性拆成独立条件；不要把白酒景气、可能的股权转让、后来股价上涨或仅提交申请当作摘帽事实。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST舍得 (600702, SSE)
- 信息截止 / As of: 2020-09-22
- 预测窗口结束 / Window end: 2022-09-22
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来24个自然月内，证券交易所审核同意撤销公司股票交易的全部退市风险警示和全部其他风险警示，且生效后的证券简称不再含ST或*ST、股票退出风险警示板。仅提交或获董事会通过申请、占款或担保已清偿、审计意见改善、撤销一项叠加警示但仍保留任一风险警示、*ST降为ST、暂停上市后恢复或最终退市均不计为事件

#### 判定条件 / Criteria

- `full_risk_warning_removal_count_24m >= 1` — 窗口内经交易所审核同意并生效的完整撤销全部风险警示至少一次

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
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 结果日期 / Resolved at: 2021-05-19

### 实际结果 / Realized outcome

- **observations**:
  - **full_risk_warning_removal_count_24m**: 1
  - **full_risk_warning_removed_by_window_end**: 1
  - **partial_only_removal_count_24m**: 0
  - **calendar_days_to_full_removal_or_zero**: 239
  - **risk_warning_present_at_window_end**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-cause-and-unresolved-occupation`
- `h1-financials-and-liquor-operations`
- `contemporaneous-liquor-recovery-and-differentiation`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_remediation_v1
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
    - is_st
    - special_treatment_info
  - **row_policy**: stock_code=600702.XSHG; if_adjusted=0 for 2020q2 PIT fundamentals; risk-warning events/status checked through the fixed 24-month window
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation
  - **matching_group**: first-risk-warning-day-full-removal-24m-v1
  - **matching_role**: event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: 6a964e0c45d9afc2f6b1f2a360c820253ebb51f5d69e6a90bfc69031b665e16d
    - **2020_half_year_report**: 00679be8d6b8fb0dee1e9b81b32bebbae9717c4a18648813ea4450cc36a29475
  - **news_evidence_policy**: Only contemporaneous industry framing published no later than as_of may enter the corpus; it cannot reveal or define the future price label.
  - **outcome_contract**: Only an exchange-approved removal of every ST/*ST warning that becomes effective inside the 24-calendar-month window counts. An application, remediation, *ST-to-ST downgrade, continued ST status, or delisting does not.
  - **status_source_sha256**:
    - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
    - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
  - **leakage_guard**: All removal approvals, later ST transitions, restructurings, delistings and post-as_of remediation facts remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_exchange_approved_full_risk_warning_removal
    - **title**: 舍得酒业关于公司股票撤销其他风险警示暨停牌的公告
    - **approved_effective_date**: 2021-05-19
    - **published_at**: 2021-05-19
    - **url**: https://static.cninfo.com.cn/finalpage/2021-05-18/1209994983.PDF
    - **sha256**: e4cf9544ff82d83741cf5c4b57940b230e9d4d7174f60707a6a1f12033937d73
    - **resulting_symbol**: 舍得酒业
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
    - **window**: 2020-09-22/2022-09-22
    - **full_removal_within_window**: true
    - **partial_only_removal_count_24m**: 0

</details>

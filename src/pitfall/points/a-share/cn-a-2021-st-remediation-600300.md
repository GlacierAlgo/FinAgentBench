# cn-a-2021-st-remediation-600300

## Question

你处在2021-04-27收盘后的信息环境。ST维维的历史占款本息和违规担保在戴帽前已处理，但2020年度财务报告内部控制仍被出具否定意见。请使用下方冻结资料，预测未来24个自然月内是否会发生target定义的完整撤销全部风险警示。重点判断已经清偿与内控重大缺陷消除、下一年度审计验证、交易所审核之间的差别，并评估扣非盈利、非经常性处置收益和主业产能利用；不得把“占款已还”机械等同于“立即摘帽”。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST维维 (600300, SSE)
- 信息截止 / As of: 2021-04-27
- 预测窗口结束 / Window end: 2023-04-27
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来24个自然月内，证券交易所审核同意撤销公司股票交易的全部退市风险警示和全部其他风险警示，且生效后的证券简称不再含ST或*ST、股票退出风险警示板。仅提交或获董事会通过申请、占款或担保已清偿、审计意见改善、撤销一项叠加警示但仍保留任一风险警示、*ST降为ST、暂停上市后恢复或最终退市均不计为事件

#### 判定条件 / Criteria

- `full_risk_warning_removal_count_24m >= 1` — 窗口内经交易所审核同意并生效的完整撤销全部风险警示至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 维维股份实施其他风险警示公告：内控重大缺陷仍在，但占用本息已收回

- Evidence ID: `st-notice-remediation-before-first-st-day`
- 发布日期 / Published: 2021-04-26
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/new/2021-04-26/600300_20210426_1.pdf

公司自2021年4月27日起变更为ST维维。戴帽原因是会计师对2020年度内部控制出具否定意见：关联资金拆借未履行董事会、股东大会决策程序，也未及时披露，内部控制未能防止、发现和纠正违规，构成重大缺陷。与多数未解决占用案例不同，公告明确称新一届董事会已在2021年4月21日前解决资金占用和违规担保问题，并收回占用资金本息。这使案例能够检验“整改完成或未来摘帽必然带来大炒”的错误捷径。

### 维维股份2020年年度报告：现金流改善但利润主要来自处置，植物蛋白产能利用不足

- Evidence ID: `annual-core-profit-disposal-gains-and-capacity`
- 发布日期 / Published: 2021-04-24
- 来源 / Source: 上海证券交易所法定年度报告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/new/2021-04-24/600300_20210424_2.pdf

2020年营业收入47.9882亿元，同比下降4.77%；归母净利润4.3573亿元，但扣非归母净利润仅6,111.52万元。年报解释出售枝江酒业形成投资收益约1.32亿元，土地征收形成资产处置收益约2.10亿元，合计对利润贡献很大。经营活动现金流净额8.9638亿元；货币资金22.2749亿元、短期借款24.2661亿元。固体饮料收入17.5119亿元基本持平，植物蛋白饮料收入4.4024亿元下降14.53%。主要豆奶/乳品工厂多处实际产能明显低于设计产能，例如总部豆奶粉设计6万吨、实际2.41万吨。占用期末利息2,692.29万元已于2021年4月21日清偿。

### 戴帽前治理报道：多年虚假货款通道占用与董监高知情风险

- Evidence ID: `contemporaneous-governance-history-and-sanctions`
- 发布日期 / Published: 2021-04-01
- 来源 / Source: 新浪财经转载的资本市场调查报道
- URL: https://finance.sina.com.cn/stock/s/2021-04-01/doc-ikmyaawa3549966.shtml

报道根据监管处罚和交易所纪律处分梳理，2017至2019年维维集团通过虚假支付货款等中间通道持续占用上市公司资金，年度累计占用从约7亿元升至11.54亿元；部分上市公司高管知悉并配合调度，其他董监高签署定期报告但未勤勉尽责。上交所认为“个人所为、董事会不知情”的申辩反而说明内控存在重大缺陷。该历史提高治理风险先验；但在as_of前占用本息已经收回，模型仍需把历史缺陷与当前修复进度分开。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 结果日期 / Resolved at: 2022-04-12

### 实际结果 / Realized outcome

- **observations**:
  - **full_risk_warning_removal_count_24m**: 1
  - **full_risk_warning_removed_by_window_end**: 1
  - **partial_only_removal_count_24m**: 0
  - **calendar_days_to_full_removal_or_zero**: 350
  - **risk_warning_present_at_window_end**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-remediation-before-first-st-day`
- `annual-core-profit-disposal-gains-and-capacity`
- `contemporaneous-governance-history-and-sanctions`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_remediation_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600300.XSHG
  - **ticker**: 600300
  - **name_as_of**: ST维维
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-04-27
  - **allowed_domains**:
    - sse.com.cn
    - sina.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - is_st
    - special_treatment_info
  - **row_policy**: stock_code=600300.XSHG; if_adjusted=0 for 2020q4 PIT fundamentals; risk-warning events/status checked through the fixed 24-month window
  - **st_cause_taxonomy**: non_operating_governance/remediated_related_party_fund_occupation+adverse_internal_control
  - **matching_group**: first-risk-warning-day-full-removal-24m-v1
  - **matching_role**: event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: a7fbfd34ccde4ee257ab4d18ad32c51156db5a4e78dd44b14b43c54f2195c2cb
    - **2020_annual_report**: 7bbd8699a7d194a1cbf150111ad520500a9ab1963de2c04b1720f0281bd019aa
  - **news_evidence_policy**: Contemporaneous reporting may expose governance history; official filings and RQData remain the authority for remediation, financial facts, and the label.
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
    - **title**: 维维股份关于公司股票撤销其他风险警示暨停牌的公告
    - **approved_effective_date**: 2022-04-12
    - **published_at**: 2022-04-12
    - **url**: https://static.cninfo.com.cn/finalpage/2022-04-11/1212869835.PDF
    - **sha256**: b4368d3a45c50a1ebec12a4d6569b935302a238e63658aac4ccff3d0162f2af1
    - **resulting_symbol**: 维维股份
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
    - **window**: 2021-04-27/2023-04-27
    - **full_removal_within_window**: true
    - **partial_only_removal_count_24m**: 0

</details>

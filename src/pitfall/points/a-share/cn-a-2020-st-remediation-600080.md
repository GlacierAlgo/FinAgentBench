# cn-a-2020-st-remediation-600080

## Question

你处在2020-06-02收盘后的信息环境。ST金花因控股股东占用资金及存单质押未在一个月内解决而戴帽，尚未归还金额1.6772亿元，控股股东承诺通过转让股份在6月30日前归还。请使用下方冻结资料，预测未来24个自然月内是否会发生target定义的完整撤销全部风险警示。重点检验股份转让资金是否具有可执行性、占用规模相对净资产和公司现金、审计保留或内控后续验证，以及交易所审核；不要把承诺日期等同于到账日。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST金花 (600080, SSE)
- 信息截止 / As of: 2020-06-02
- 预测窗口结束 / Window end: 2022-06-02
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来24个自然月内，证券交易所审核同意撤销公司股票交易的全部退市风险警示和全部其他风险警示，且生效后的证券简称不再含ST或*ST、股票退出风险警示板。仅提交或获董事会通过申请、占款或担保已清偿、审计意见改善、撤销一项叠加警示但仍保留任一风险警示、*ST降为ST、暂停上市后恢复或最终退市均不计为事件

#### 判定条件 / Criteria

- `full_risk_warning_removal_count_24m >= 1` — 窗口内经交易所审核同意并生效的完整撤销全部风险警示至少一次

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 金花股份实施其他风险警示公告：尚有1.6772亿元占用与存单质押未解

- Evidence ID: `st-notice-occupation-and-pledged-deposit`
- 发布日期 / Published: 2020-06-01
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-06-01/1207878970.PDF

公司自2020年6月2日起变更为ST金花。2019年控股股东及关联方资金占用发生额2.7777亿元、存单质押6,800万元，合计3.4577亿元，占最近一期经审计净资产20.15%；截至公告日仍有1.6772亿元未归还或解除，占净资产9.78%。控股股东承诺转让所持股份，并在6月30日前归还资金及占用费，但披露时尚未完成。

### 金花股份2020年一季报：低有息负债与疫情下收入现金流承压

- Evidence ID: `q1-low-leverage-but-pandemic-pressure`
- 发布日期 / Published: 2020-04-30
- 来源 / Source: 巨潮资讯法定季度报告
- URL: https://static.cninfo.com.cn/finalpage/2020-04-30/1207688572.PDF

2020年一季度营业收入1.0778亿元，同比下降28.09%；归母净利润-104.34万元，扣非归母净利润-270.96万元，经营活动现金流净额-1,458.22万元。期末货币资金2.4680亿元、归母净资产17.1412亿元，合并资产负债表没有短期借款，流动负债1.6223亿元。低杠杆和账面现金使问题可能可修复，但占用金额接近现金的68%，且现金是否自由可用需要结合存单质押判断。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 结果日期 / Resolved at: 2021-05-12

### 实际结果 / Realized outcome

- **observations**:
  - **full_risk_warning_removal_count_24m**: 1
  - **full_risk_warning_removed_by_window_end**: 1
  - **partial_only_removal_count_24m**: 0
  - **calendar_days_to_full_removal_or_zero**: 344
  - **risk_warning_present_at_window_end**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-occupation-and-pledged-deposit`
- `q1-low-leverage-but-pandemic-pressure`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_remediation_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600080.XSHG
  - **ticker**: 600080
  - **name_as_of**: ST金花
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-06-02
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - is_st
    - special_treatment_info
  - **row_policy**: stock_code=600080.XSHG; quarter=2020q1; info_date=2020-04-30; if_adjusted=0; first risk-warning trading day=2020-06-02
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_occupation+pledged_deposit
  - **matching_group**: first-risk-warning-day-full-removal-24m-v1
  - **matching_role**: event_controller_asset_sale
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: 076582de2b46d70471f15ac8ab1d8cb96fb821375bf3098931bd817208960ba9
    - **q1_report**: 9da6aaa89af6b1b0c42787c6f495116ba4367220f0c7e2ff6d008c33c99bef1f
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
    - **title**: 金花股份关于公司股票撤销其他风险警示暨停牌的公告
    - **approved_effective_date**: 2021-05-12
    - **published_at**: 2021-05-12
    - **url**: https://static.cninfo.com.cn/finalpage/2021-05-11/1209948204.PDF
    - **sha256**: 4dfa11935a34b5e8c152bae332cd362c43b85c536c19378ee3274c009917c940
    - **resulting_symbol**: 金花股份
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
    - **window**: 2020-06-02/2022-06-02
    - **full_removal_within_window**: true
    - **partial_only_removal_count_24m**: 0

</details>

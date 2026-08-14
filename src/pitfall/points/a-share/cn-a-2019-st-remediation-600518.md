# cn-a-2019-st-remediation-600518

## Question

你处在2019-05-21收盘后的信息环境。ST康美因88.79亿元关联资金被用于购买公司股票、治理和内控重大缺陷而戴帽，年报还刚发生巨额前期差错更正。请使用下方冻结资料，预测未来24个自然月内是否会发生target定义的完整撤销全部风险警示。重点比较占用规模与可执行清偿资源、存货和短债压力、现金骤降、调查与审计不确定性以及潜在新增退市风险；董事会整改表态和单季正现金流不能替代监管与交易所闭环。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST康美 (600518, SSE)
- 信息截止 / As of: 2019-05-21
- 预测窗口结束 / Window end: 2021-05-21
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 判定定义 / Definition: 自首次实施ST或*ST风险警示的交易日起未来24个自然月内，证券交易所审核同意撤销公司股票交易的全部退市风险警示和全部其他风险警示，且生效后的证券简称不再含ST或*ST、股票退出风险警示板。仅提交或获董事会通过申请、占款或担保已清偿、审计意见改善、撤销一项叠加警示但仍保留任一风险警示、*ST降为ST、暂停上市后恢复或最终退市均不计为事件

#### 判定条件 / Criteria

- `full_risk_warning_removal_count_24m >= 1` — 窗口内经交易所审核同意并生效的完整撤销全部风险警示至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 康美药业实施其他风险警示公告：88.79亿元关联资金用于购买公司股票

- Evidence ID: `st-notice-8.879b-related-fund-flow`
- 发布日期 / Published: 2019-05-18
- 来源 / Source: 上海证券交易所法定公告
- URL: https://static.cninfo.com.cn/finalpage/2019-05-18/1206283586.PDF

公司自2019年5月21日起变更为ST康美。公告称公司与关联公司存在88.79亿元资金往来，该资金被关联公司用于购买公司股票，触及投资者难以判断公司前景、权益可能受损的情形。公司承认治理、资金管理和关联交易内控存在重大缺陷，只表示督促关联方多途径解决并整改，没有给出锁定资金、清偿时间表或审计验证。

### 康美药业2019年一季报：更正后现金骤降、巨额存货与短债

- Evidence ID: `q1-cash-collapse-inventory-and-short-debt`
- 发布日期 / Published: 2019-04-30
- 来源 / Source: 巨潮资讯法定季度报告
- URL: https://static.cninfo.com.cn/finalpage/2019-04-30/1206168279.PDF

更正口径下，2019年一季度营业收入49.0164亿元、归母净利润2.2088亿元、扣非归母净利润1.7091亿元、经营活动现金流净额6.7395亿元。期末货币资金10.4801亿元，较年初减少43.02%；存货336.6041亿元、短期借款149.40亿元、流动负债249.7790亿元、总负债452.7493亿元。筹资现金流净额-12.9980亿元。正经营现金流远小于资金占用与融资规模，且报表刚经历巨额差错更正。

### 中证网戴帽报道：88.79亿元资金往来直接触发风险警示

- Evidence ID: `contemporaneous-st-report`
- 发布日期 / Published: 2019-05-18
- 来源 / Source: 中国证券报·中证网
- URL: https://www.cs.com.cn/ssgs/gsxw/201905/t20190518_5950494.html

同时点报道确认公司将于5月21日起被实施其他风险警示，原因是88.79亿元关联资金被用于购买公司股票并使投资者难以判断前景。新闻没有提供已经到账的清偿资源或交易所撤销意见，因此只用于交叉核验市场当时可见的信息，不能支持“很快摘帽”的结论。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `exchange_approved_full_risk_warning_removal_24m`
- 结果日期 / Resolved at: 2021-05-21

### 实际结果 / Realized outcome

- **observations**:
  - **full_risk_warning_removal_count_24m**: 0
  - **full_risk_warning_removed_by_window_end**: 0
  - **partial_only_removal_count_24m**: 0
  - **calendar_days_to_full_removal_or_zero**: 0
  - **risk_warning_present_at_window_end**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `st-notice-8.879b-related-fund-flow`
- `q1-cash-collapse-inventory-and-short-debt`
- `contemporaneous-st-report`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_remediation_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600518.XSHG
  - **ticker**: 600518
  - **name_as_of**: ST康美
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-05-21
  - **allowed_domains**:
    - cninfo.com.cn
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
  - **row_policy**: stock_code=600518.XSHG; quarter=2019q1; info_date=2019-04-30; if_adjusted=0; first risk-warning trading day=2019-05-21
  - **st_cause_taxonomy**: non_operating_governance/related_party_fund_flow+internal_control_material_weakness
  - **matching_group**: first-risk-warning-day-full-removal-24m-v1
  - **matching_role**: no_event_hard_fraud_and_liquidity
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **st_notice**: 0dbe732b03eb90ba8cd5dabc9757b42700f774d2ad6fb9195777119a249f8172
    - **q1_report**: 684b1c371ca5e2f564b638ad5cbdfd9bd72ae0a36cc041d1bac076475612c402
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
    - **type**: rqdata_risk_warning_status_crosscheck
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2019-05-21/2021-05-21
    - **full_removal_within_window**: false
    - **partial_only_removal_count_24m**: 0
    - **later_context_not_counted**: 完整撤销其他风险警示最终于2024-07-04生效，显著晚于24个月窗口；2021-04-29窗口内反而由ST升级为*ST。

</details>

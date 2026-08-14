# cn-a-2020-major-illegal-delisting-600518

## Question

你处在2020-05-14收盘后的信息环境。证监会已宣布对ST康美作出行政处罚及市场禁入决定，并认定2016至2018年长期、系统财务造假。请只使用下方冻结资料，按本案发生和认定时适用的重大违法强制退市规则，预测上交所是否会在固定50个自然月窗口内就同一案件作出重大违法强制终止上市最终决定。不要把造假金额巨大、行政处罚、ST、破产重整或今天更严格的财务造假退市标准自动等同于历史规则下的最终强制退市决定。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST康美 (600518, SSE)
- 信息截止 / As of: 2020-05-14
- 预测窗口结束 / Window end: 2024-07-14
- 目标事件 / Target: `major_illegality_forced_delisting_final_decision_50m`
- 判定定义 / Definition: 交易所在as-of后50个自然月内，依据截至as-of已公开的违法事实或其后对同一案件的正式认定，作出重大违法强制终止公司股票上市的最终决定。行政处罚、风险警示、重大违法退市程序启动、暂停上市、其他退市路径及窗口外决定均不计入

#### 判定条件 / Criteria

- `exchange_major_illegality_forced_delisting_final_decision_count_50m >= 1` — 固定50个自然月窗口内交易所作出的重大违法强制终止上市最终决定至少为1次

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 上交所2018年重大违法强制退市规则：欺诈发行、重大信息披露违法与五大安全领域

- Evidence ID: `sse-2018-major-illegal-regime`
- 发布日期 / Published: 2018-11-16
- 来源 / Source: 上海证券交易所
- URL: https://www.sse.com.cn/aboutus/mediacenter/hotandd/c/c_20181116_4678360.shtml

上交所2018年11月16日发布重大违法强制退市新规，区分欺诈发行和重大信息披露违法，并新增国家安全、公共安全、生态安全、生产安全和公众健康安全等领域的重大违法情形。针对年报财务指标造假，规则强调违法事实达到重大违法标准并使公司实际已触及的财务类退市指标被规避，不能仅因造假金额巨大或受到行政处罚就自动推导出交易所已经或必将作出重大违法强制终止上市决定。判断必须使用当时规则，不能倒套后来扩围的量化造假退市标准。

### 证监会对康美药业作出处罚及禁入决定：2016至2018年长期系统财务造假

- Evidence ID: `csrc-2020-kangmei-final-findings`
- 发布日期 / Published: 2020-05-14
- 来源 / Source: 中国证券监督管理委员会
- URL: https://www.csrc.gov.cn/csrc/c100028/c1000782/content.shtml

证监会宣布已对康美药业作出行政处罚及市场禁入决定。最终认定公司2016年至2018年虚增巨额营业收入，通过伪造、变造大额定期存单等虚增货币资金，将不满足确认和计量条件的工程纳入报表并虚增固定资产，还存在控股股东及其关联方非经营性资金占用，导致相关年报虚假记载和重大遗漏。证监会将其定性为有预谋、有组织、长期、系统的财务欺诈，并移送涉嫌犯罪行为。行政处罚的严重性本身不等于目标所定义的交易所重大违法强制终止上市最终决定。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `major_illegality_forced_delisting_final_decision_50m`
- 结果日期 / Resolved at: 2024-07-14
- 可观察日期 / Observed at: 2024-07-15

### 实际结果 / Realized outcome

- **observations**:
  - **exchange_major_illegality_forced_delisting_final_decision_count_50m**: 0
  - **csrc_final_administrative_penalty_count**: 1
  - **continued_listing_at_window_cutoff**: 1
  - **other_risk_warning_removed_before_cutoff**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `sse-2018-major-illegal-regime`
- `csrc-2020-kangmei-final-findings`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_rule_regime_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600518.XSHG
  - **ticker**: 600518
  - **name_as_of**: ST康美
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-05-14
  - **allowed_domains**:
    - sse.com.cn
    - csrc.gov.cn
- **scenario_authoring**:
  - **dataset**: official_regulator_and_exchange_records
  - **access**: read_only
  - **matching_group**: major-illegality-forced-delisting-historical-regime-v1
  - **matching_role**: no_event
  - **matching_axes**:
    - official_fraud_or_illegality_finding
    - historical_2018_major_illegality_regime
    - fixed_50_calendar_month_window
    - final_exchange_decision_only
  - **rule_snapshot_id**: sse-major-illegality-2018-11-16
  - **exact_contract**: major_illegality_forced_delisting_final_decision_50m-v1
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:

  - **leakage_guard**: Corpus contains only the contemporaneous 2018 exchange rule explanation and the regulator's as-of final findings; later continued listing and risk-warning removal remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_other_risk_warning_removal_notice
    - **title**: 康美药业关于撤销其他风险警示暨停牌的公告
    - **published_at**: 2024-07-03
    - **url**: https://static.cninfo.com.cn/finalpage/2024-07-03/1220520500.PDF
    - **effective_at**: 2024-07-04
    - **fields**:
      - 撤销其他风险警示
      - 证券简称变更为康美药业
      - 继续上市交易
  - **item 2**:
    - **type**: official_issuer_filing_at_cutoff
    - **title**: 康美药业2024年半年度业绩预盈公告
    - **published_at**: 2024-07-13
    - **url**: https://static.cninfo.com.cn/finalpage/2024-07-13/1220626359.PDF
    - **fields**:
      - 证券代码600518
      - 证券简称康美药业
      - 持续披露上市公司业绩

</details>

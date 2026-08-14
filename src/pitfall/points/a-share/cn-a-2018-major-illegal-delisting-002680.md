# cn-a-2018-major-illegal-delisting-002680

## Question

你处在2018-11-16收盘后的信息环境。*ST长生的问题疫苗、年报虚假记载和主管机关处置事实已经公开，深交所也已按当日发布的重大违法强制退市实施办法启动机制。请只使用下方冻结资料，按当时有效而非今天的重大违法规则，预测深交所是否会在固定50个自然月窗口内就同一案件作出重大违法强制终止上市最终决定。程序启动、行政处罚、暂停上市和最终终止上市决定必须严格区分。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST长生 (002680, SZSE)
- 信息截止 / As of: 2018-11-16
- 预测窗口结束 / Window end: 2023-01-16
- 目标事件 / Target: `major_illegality_forced_delisting_final_decision_50m`
- 判定定义 / Definition: 交易所在as-of后50个自然月内，依据截至as-of已公开的违法事实或其后对同一案件的正式认定，作出重大违法强制终止公司股票上市的最终决定。行政处罚、风险警示、重大违法退市程序启动、暂停上市、其他退市路径及窗口外决定均不计入

#### 判定条件 / Criteria

- `exchange_major_illegality_forced_delisting_final_decision_count_50m >= 1` — 固定50个自然月窗口内交易所作出的重大违法强制终止上市最终决定至少为1次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 深交所上市公司重大违法强制退市实施办法：五类公共安全重大违法情形

- Evidence ID: `szse-2018-major-illegal-measures`
- 发布日期 / Published: 2018-11-16
- 来源 / Source: 深圳证券交易所
- URL: https://docs.static.szse.cn/www/disclosure/notice/W020181116826735975725.pdf

深交所2018年11月16日发布并施行《上市公司重大违法强制退市实施办法》。第五条第二项把涉及国家安全、公共安全、生态安全、生产安全和公众健康安全等领域的违法行为，情节恶劣、严重损害国家利益、社会公共利益或者严重影响上市地位，列为重大违法强制退市情形。规则还规定交易所依程序作出是否对公司实施重大违法强制退市的决定；程序启动、风险警示和暂停上市本身均不是最终终止上市决定。

### 证监会严惩长生生物信披违法案：问题疫苗、停产召回与2015至2017年年报虚假记载

- Evidence ID: `csrc-2018-changsheng-vaccine-facts`
- 发布日期 / Published: 2018-10-16
- 来源 / Source: 中国证券监督管理委员会
- URL: https://www.csrc.gov.cn/csrc/c100028/c1001165/content.shtml

证监会公开长生生物问题疫苗案事实：未按规定披露问题疫苗不符合标准、停产和召回，相关公告存在误导性陈述及重大遗漏，未披露药监调查和狂犬疫苗GMP证书失效导致主业停产，并在2015年至2017年年报及内部控制自我评价报告中虚假记载。证监会拟作顶格行政处罚并对核心责任人终身市场禁入。

### 深交所启动长生生物重大违法强制退市机制

- Evidence ID: `szse-2018-changsheng-mechanism-launch`
- 发布日期 / Published: 2018-11-16
- 来源 / Source: 深圳证券交易所
- URL: https://www.szse.cn/aboutus/trends/news/t20181116_557594.html

深交所说明，长生生物主要子公司因违法生产狂犬病疫苗被药品监管部门吊销药品生产许可证、没收违法所得并处巨额罚款，违法行为涉及公众健康安全，情节恶劣，严重损害社会公共利益。依据当日发布的实施办法第五条第二项，深交所启动对长生生物重大违法强制退市机制。启动机制是强烈先验，但目标仍要求未来出现交易所最终终止上市决定。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `major_illegality_forced_delisting_final_decision_50m`
- 结果日期 / Resolved at: 2019-10-08
- 可观察日期 / Observed at: 2019-10-08

### 实际结果 / Realized outcome

- **observations**:
  - **exchange_major_illegality_forced_delisting_final_decision_count_50m**: 1
  - **major_illegality_mechanism_launch_count**: 1
  - **major_illegality_forced_delisting_initial_decision_count**: 1
  - **final_termination_decision_count**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `szse-2018-major-illegal-measures`
- `csrc-2018-changsheng-vaccine-facts`
- `szse-2018-changsheng-mechanism-launch`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_rule_regime_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002680.XSHE
  - **ticker**: 002680
  - **name_as_of**: *ST长生
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2018-11-16
  - **allowed_domains**:
    - szse.cn
    - csrc.gov.cn
- **scenario_authoring**:
  - **dataset**: official_regulator_exchange_and_issuer_filings
  - **access**: read_only
  - **matching_group**: major-illegality-forced-delisting-historical-regime-v1
  - **matching_role**: event
  - **matching_axes**:
    - official_fraud_or_illegality_finding
    - historical_2018_major_illegality_regime
    - fixed_50_calendar_month_window
    - final_exchange_decision_only
  - **rule_snapshot_id**: szse-major-illegality-2018-11-16-5.2
  - **exact_contract**: major_illegality_forced_delisting_final_decision_50m-v1
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **szse_2018_major_illegal_measures.pdf**: 70c44fe1ab59ec27b7cf0b89a4a7b3d2c26211117223823d465e4951fc8743cf
  - **leakage_guard**: Corpus stops at the official mechanism launch on as_of; the later exchange termination decision remains label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_exchange_final_termination_decision
    - **title**: 深交所关于长生生物科技股份有限公司股票终止上市的公告
    - **published_at**: 2019-10-08
    - **url**: https://www.szse.cn/disclosure/notice/company/t20191008_571144.html
    - **effective_at**: 2019-10-08
    - **fields**:
      - 重大违法强制退市
      - 终止上市决定
      - 深证上〔2019〕618号

</details>

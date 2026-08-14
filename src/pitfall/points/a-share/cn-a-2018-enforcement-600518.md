# cn-a-2018-enforcement-600518

## Question

你处在2018-10-27的信息环境。请使用下方冻结资料，判断康美药业未来30个自然月内是否会发生target定义的重大财务错报最终监管认定。重点审视存贷双高、利息支出与利息收入的不对称、利润现金转化、巨额存货和股东高质押，并比较法定报告与当时媒体对现金真实性的质疑。请分别评估底层报表失真风险、可被外部取证的程度和最终执法在窗口内落地的概率；不得使用窗口后的调查、处罚、ST或更正结果。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 康美药业 (600518, SSE)
- 信息截止 / As of: 2018-10-27
- 预测窗口结束 / Window end: 2021-04-27
- 目标事件 / Target: `regulator_confirmed_material_financial_misstatement_30m`
- 判定定义 / Definition: 未来30个自然月内，中国证监会或其派出机构出具日期落在窗口内的最终《行政处罚决定书》，正式认定公司在as_of之前已经公开的定期报告、发行文件或重组文件中，单项或同一事项累计存在不低于1亿元的虚增或虚减营业收入、利润、货币资金或其他资产，或未披露不低于1亿元的控股股东及关联方非经营性资金占用、违规担保。立案调查、交易所问询、监管措施、行政处罚事先告知、媒体质疑和公司自查均不计；处罚决定晚于窗口也不计。本题预测固定期限内的重大违法最终认定，不等同于判断公司最终是否造假、是否ST或是否违约

#### 判定条件 / Criteria

- `qualifying_final_enforcement_decision_count_30m >= 1` — 窗口内满足监管主体、最终决定、点时文件和1亿元重大性门槛的处罚决定至少一份

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 康美药业2018年半年报：399亿元货币资金、124.5亿元短借与4.52亿元经营现金流

- Evidence ID: `h1-reported-cash-and-low-cash-conversion`
- 发布日期 / Published: 2018-08-29
- 来源 / Source: 巨潮资讯法定半年度报告
- URL: https://static.cninfo.com.cn/finalpage/2018-08-29/1205349494.PDF

截至2018年6月末，合并口径货币资金398.8540亿元、短期借款124.5204亿元；母公司货币资金374.6933亿元。上半年营业收入169.5934亿元、归母净利润25.9291亿元，但经营活动现金流净额仅4.5188亿元，同比下降57.57%；筹资现金流净额67.1881亿元。利息支出7.9775亿元而利息收入1.4308亿元。公司称受限货币资金仅6034.14万元、无逾期短借，并明确勾选不存在控股股东及关联方非经营性占用。现金规模、融资成本和现金转化之间存在强烈张力，而否定性披露仍需外部证据验证。

### 康美药业2018年第三季度报告：现金378亿元、债务融资和财务费用同步上升

- Evidence ID: `q3-larger-cash-and-more-extreme-carry-cost`
- 发布日期 / Published: 2018-10-27
- 来源 / Source: 巨潮资讯法定定期报告
- URL: https://static.cninfo.com.cn/finalpage/2018-10-27/1205546609.PDF

截至2018年9月末，合并口径货币资金377.8846亿元、短期借款124.5173亿元、应付债券147.7427亿元、流动负债294.0493亿元、应收账款61.0559亿元、存货184.4986亿元，归母权益346.2005亿元。前三季度营业收入254.2843亿元、归母净利润38.4730亿元、经营活动现金流净额12.9322亿元。利息费用13.0080亿元而利息收入2.4047亿元，财务费用同比增加63.56%。报告仍勾选无控股股东非经营性占款和无违规担保；这些是公司陈述，不是资金真实性的独立确认。

### 财联社2018年7月调查：360亿元现金与持续高成本融资是否合理

- Evidence ID: `contemporaneous-media-cash-paradox`
- 发布日期 / Published: 2018-07-31
- 来源 / Source: 财联社报道，经搜狐转载的冻结网页
- URL: https://www.sohu.com/a/244376293_313745

报道依据当时公开财报指出：2018年一季度货币资金366.4亿元，2017年利息支出12.15亿元，2017年末披露的受限货币资金仅8868.52万元，公司却继续通过公司债、银行借款、配股等方式大规模融资；控股股东截至一季度持股质押率约94.96%。报道还关注157亿元左右存货、消耗性生物资产及资产减值快速上升，并明确把“现金是否只是摆设”作为待核实疑问，而非既成事实。该文证明相关异常在点时已可被互联网搜索发现。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `regulator_confirmed_material_financial_misstatement_30m`
- 结果日期 / Resolved at: 2020-05-13

### 实际结果 / Realized outcome

- **observations**:
  - **qualifying_final_enforcement_decision_count_30m**: 1
  - **largest_confirmed_material_amount_rmb**: 36188038359.5
- **derivations**:


### 对应的题内资料 / Expected evidence

- `h1-reported-cash-and-low-cash-conversion`
- `q3-larger-cash-and-more-extreme-carry-cost`
- `contemporaneous-media-cash-paradox`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_enforcement_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600518.XSHG
  - **ticker**: 600518
  - **name_as_of**: 康美药业
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2018-10-27
  - **allowed_domains**:
    - cninfo.com.cn
    - sohu.com
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=600518.XSHG; quarter=2018q3; info_date=2018-10-27; if_adjusted=0
  - **matching_group**: severe-financial-governance-signal-30m-v1
  - **matching_role**: event
  - **outcome_contract**: Only a dated final CSRC or regional-bureau administrative penalty decision inside the 30-month window can create an event; investigation signals and post-window decisions cannot.
  - **news_evidence_policy**: Contemporaneous reporting is frozen as an ex-ante search result and is attributed as analysis, not treated as an adjudicated fact.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2018_q3_report**: bc31d7e1f8407a7c2d70ba9bc9a9163ef45db005c171c747cd1766b51d1daf6e
    - **2018_h1_report**: 4a6c4f8cb8fbbd3e5c84fc3c3ed18cdbd35705127469edb8fac7d5eb68fd40ba
  - **leakage_guard**: All investigations, penalties, restatements, court findings, ST labels and payment outcomes after as_of remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_final_administrative_penalty_decision
    - **title**: 中国证监会行政处罚决定书（康美药业股份有限公司、马兴田、许冬瑾等22名责任人员）
    - **decision_no**: 〔2020〕24号
    - **decision_date**: 2020-05-13
    - **published_at**: 2020-05-13
    - **url**: https://www.csrc.gov.cn/csrc/c101928/c1042341/content.shtml
    - **sha256**: b13b63f6ec77c7887c03f65b539e0c53bb75f08cea5317e6f034f1df3c58714f
    - **qualifying_pre_as_of_document**: 2018年半年度报告
    - **largest_confirmed_material_amount_rmb**: 36188038359.5
    - **finding**: 最终决定认定2018年半年报虚增货币资金361.8804亿元，并同时认定虚增收入、利润及未披露关联方非经营性占用；决定日期在30个月窗口内。

</details>

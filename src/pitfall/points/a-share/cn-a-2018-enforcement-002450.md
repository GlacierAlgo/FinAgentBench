# cn-a-2018-enforcement-002450

## Question

你处在2018-10-23的信息环境。请使用下方冻结资料，判断康得新未来30个自然月内是否会发生target定义的重大财务错报最终监管认定。重点比较三季报中的现金、债务、利润和经营现金流，2017年年报问询对185亿元现金真实性及关联方占用的追问、会计师所述核查程序与结论，以及母公司现金、控股股东质押和融资成本。请区分报表异常、审计证据质量、实际错报与最终执法时点；不得使用后来债券违约、处罚、ST或退市信息。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 康得新 (002450, SZSE)
- 信息截止 / As of: 2018-10-23
- 预测窗口结束 / Window end: 2021-04-23
- 目标事件 / Target: `regulator_confirmed_material_financial_misstatement_30m`
- 判定定义 / Definition: 未来30个自然月内，中国证监会或其派出机构出具日期落在窗口内的最终《行政处罚决定书》，正式认定公司在as_of之前已经公开的定期报告、发行文件或重组文件中，单项或同一事项累计存在不低于1亿元的虚增或虚减营业收入、利润、货币资金或其他资产，或未披露不低于1亿元的控股股东及关联方非经营性资金占用、违规担保。立案调查、交易所问询、监管措施、行政处罚事先告知、媒体质疑和公司自查均不计；处罚决定晚于窗口也不计。本题预测固定期限内的重大违法最终认定，不等同于判断公司最终是否造假、是否ST或是否违约

#### 判定条件 / Criteria

- `qualifying_final_enforcement_decision_count_30m >= 1` — 窗口内满足监管主体、最终决定、点时文件和1亿元重大性门槛的处罚决定至少一份

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 2017年报问询回复：深交所追问185亿元现金真实性，会计师称审计程序充分

- Evidence ID: `annual-inquiry-and-auditor-cash-assurance`
- 发布日期 / Published: 2018-05-18
- 来源 / Source: 巨潮资讯年报问询回复
- URL: https://static.cninfo.com.cn/finalpage/2018-05-18/1204953365.PDF

深交所问询指出，2015至2017年末公司货币资金分别为100.87亿元、153.89亿元、185.04亿元，占总资产约55%，同期有息负债从50.59亿元升至110.05亿元、2017年财务费用5.53亿元，要求核查现金真实性、安全性、权利限制、关联方资金往来及为何未列为关键审计事项。会计师回复称2017年末货币资金185.0414亿元，其中34.2564亿元受限；已执行银行函证、对账单、存单和利息合理性检查，期末资金真实存在，不存在其他关联方非经营性占用，且货币资金不涉及复杂判断，故未列为关键审计事项。问询本身和核查结论必须分别赋权。

### 康得新2018年半年报：合并现金167.81亿元、母公司现金75.63亿元、控股股东质押率91.30%

- Evidence ID: `h1-consolidated-parent-liquidity-and-pledge`
- 发布日期 / Published: 2018-08-17
- 来源 / Source: 巨潮资讯法定半年度报告
- URL: https://static.cninfo.com.cn/finalpage/2018-08-17/1205298768.PDF

2018年6月末合并货币资金167.8111亿元，其中8.7860亿元受限；短期借款63.8322亿元、应付债券39.6499亿元、应收账款64.3304亿元。上半年营业收入72.4058亿元、归母净利润15.1324亿元、经营活动现金流6.3590亿元，同比下降63.86%。母公司口径货币资金75.6288亿元、其他应收款44.5927亿元且无短期借款。控股股东康得集团持有851,414,682股，其中777,337,646股质押，质押率约91.30%。母公司现金可见并不自动证明资金没有被集团安排限制。

### 康得新2018年第三季度报告：账面现金150亿元，但利息支出显著高于利息收入

- Evidence ID: `q3-cash-profit-and-financing-paradox`
- 发布日期 / Published: 2018-10-23
- 来源 / Source: 巨潮资讯法定定期报告
- URL: https://static.cninfo.com.cn/finalpage/2018-10-23/1205522221.PDF

截至2018年9月末，合并口径货币资金150.1353亿元、短期借款61.8081亿元、应付债券40.4654亿元、流动负债121.0236亿元、应收账款71.4517亿元，归母权益200.0600亿元。前三季度营业收入108.3475亿元、归母净利润22.0144亿元、经营活动现金流净额20.7367亿元。同期利息费用5.5755亿元而利息收入仅1.9792亿元。报告还称不存在控股股东及关联方非经营性占款、无违规对外担保；应结合年报问询所依赖的审计证据边界判断，而不能把管理层勾选当成独立证明。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `regulator_confirmed_material_financial_misstatement_30m`
- 结果日期 / Resolved at: 2020-09-22

### 实际结果 / Realized outcome

- **observations**:
  - **qualifying_final_enforcement_decision_count_30m**: 1
  - **largest_confirmed_material_amount_rmb**: 10288447275.09
- **derivations**:


### 对应的题内资料 / Expected evidence

- `annual-inquiry-and-auditor-cash-assurance`
- `h1-consolidated-parent-liquidity-and-pledge`
- `q3-cash-profit-and-financing-paradox`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_enforcement_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002450.XSHE
  - **ticker**: 002450
  - **name_as_of**: 康得新
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2018-10-23
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=002450.XSHE; quarter=2018q3; info_date=2018-10-23; if_adjusted=0
  - **matching_group**: severe-financial-governance-signal-30m-v1
  - **matching_role**: event
  - **outcome_contract**: Only a dated final CSRC or regional-bureau administrative penalty decision inside the 30-month window can create an event; investigation signals and post-window decisions cannot.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2018_q3_report**: b3d7c478a1f19f71f45c811c011407e7cb738779695f94b8adbc2fde6e1385a8
    - **2018_h1_report**: 77a875346557d5dc5b81e97149034b0a7edf73a5822115e6c4cfca696dfad05f
    - **2017_annual_inquiry_reply**: ebc04fd1cfb2babca244894e04f43ace52231f4e0688e552ade4510dc13441af
  - **leakage_guard**: All defaults, investigations, penalties, restatements, ST labels and delisting information after as_of remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_final_administrative_penalty_decision
    - **title**: 中国证监会行政处罚决定书（康得新、钟玉等13人）
    - **decision_no**: 〔2020〕71号
    - **decision_date**: 2020-09-22
    - **published_at**: 2020-09-22
    - **url**: https://www.csrc.gov.cn/csrc/c101928/c1042302/content.shtml
    - **sha256**: 4fae13599f4f0d5bd016ea058cd1c96dae1c3a3bdd70b2eeb16e92c46709a7c5
    - **qualifying_pre_as_of_document**: 2017年年度报告
    - **largest_confirmed_material_amount_rmb**: 10288447275.09
    - **finding**: 最终决定认定2017年年报中北京银行账户组披露余额102.8845亿元但实际余额为0，并认定当年虚增利润39.0821亿元及未披露重大关联担保；决定日期在30个月窗口内。

</details>

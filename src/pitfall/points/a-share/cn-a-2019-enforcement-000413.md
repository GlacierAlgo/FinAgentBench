# cn-a-2019-enforcement-000413

## Question

你处在2019-10-31的信息环境。请使用下方冻结资料，判断东旭光电未来30个自然月内是否会发生target定义的重大财务错报最终监管认定。重点核查183亿元现金与极弱经营现金流、利息收支、应收和债务的组合，87.78亿元存款集中于关联财务公司的可动用性，以及公司专项评估的独立性。强异常可以提高底层失真概率，但题目只计算窗口内最终处罚；不得使用后来违约、调查、处罚、退市或更正信息。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 东旭光电 (000413, SZSE)
- 信息截止 / As of: 2019-10-31
- 预测窗口结束 / Window end: 2022-04-30
- 目标事件 / Target: `regulator_confirmed_material_financial_misstatement_30m`
- 判定定义 / Definition: 未来30个自然月内，中国证监会或其派出机构出具日期落在窗口内的最终《行政处罚决定书》，正式认定公司在as_of之前已经公开的定期报告、发行文件或重组文件中，单项或同一事项累计存在不低于1亿元的虚增或虚减营业收入、利润、货币资金或其他资产，或未披露不低于1亿元的控股股东及关联方非经营性资金占用、违规担保。立案调查、交易所问询、监管措施、行政处罚事先告知、媒体质疑和公司自查均不计；处罚决定晚于窗口也不计。本题预测固定期限内的重大违法最终认定，不等同于判断公司最终是否造假、是否ST或是否违约

#### 判定条件 / Criteria

- `qualifying_final_enforcement_decision_count_30m >= 1` — 窗口内满足监管主体、最终决定、点时文件和1亿元重大性门槛的处罚决定至少一份

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 东旭光电2019年第三季度报告：现金183亿元但经营现金流仅1.27亿元

- Evidence ID: `q3-cash-profit-and-working-capital-pressure`
- 发布日期 / Published: 2019-10-31
- 来源 / Source: 巨潮资讯法定定期报告
- URL: https://static.cninfo.com.cn/finalpage/2019-10-31/1207047204.PDF

截至2019年9月末，合并口径货币资金183.1633亿元、短期借款101.2915亿元、应付票据12.4511亿元、应付债券52.8389亿元、流动负债270.4604亿元、应收账款118.0107亿元、商誉27.0240亿元，归母权益332.8240亿元。前三季度营业收入125.6620亿元、归母净利润11.3488亿元、扣非净利润9.6203亿元，但经营活动现金流净额只有1.2711亿元；利息费用8.9774亿元、利息收入3.1902亿元。报告仍勾选无控股股东非经营性占款和无违规担保。强烈的现金、利润、营运资本与融资成本矛盾应提高怀疑，但不能单独确定监管落地日期。

### 东旭光电2018年报：巨额现金和融资并存，报告仍给出历史履约与治理保证

- Evidence ID: `annual-mtn-and-positive-assurances`
- 发布日期 / Published: 2019-04-30
- 来源 / Source: 巨潮资讯法定年度报告
- URL: https://static.cninfo.com.cn/finalpage/2019-04-30/1206163741.PDF

2018年报列示2016年发行的中期票据共47亿元、短期和长期有息负债规模较大，同时披露历史债券按时付息。公司及管理层对报告真实、准确、完整作出保证，报告亦未承认控股股东非经营性占用。对本题而言，历史履约和格式化保证是反向证据，但其验证力弱于独立银行流水、客户供应商闭环和关联资金穿透；应与三季报中的现金流矛盾共同评估。

### 东旭集团财务公司2019年半年风险评估：上市公司87.78亿元存款集中于关联财务公司

- Evidence ID: `finance-company-concentration-and-self-assessed-safety`
- 发布日期 / Published: 2019-08-31
- 来源 / Source: 巨潮资讯法定专项报告
- URL: https://static.cninfo.com.cn/finalpage/2019-08-31/1206868029.PDF

专项报告称东旭集团财务公司注册资本50亿元，其中东旭集团出资30亿元、上市公司出资20亿元；截至2019年6月末总资产286.46亿元、负债234.64亿元、净资产51.82亿元，上半年净利润0.42亿元。东旭光电在财务公司的贷款余额为零、存款余额高达87.78亿元，约占同期合并货币资金196.08亿元的44.8%。报告由上市公司查验关联财务公司资料后认为未发现重大内控缺陷、监管指标合规、关联存款风险可控。集中度是可核实事实，“风险可控”则是关联体系内评估，两者证据权重不同。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `regulator_confirmed_material_financial_misstatement_30m`
- 结果日期 / Resolved at: 2022-04-30

### 实际结果 / Realized outcome

- **observations**:
  - **qualifying_final_enforcement_decision_count_30m**: 0
  - **largest_confirmed_material_amount_rmb**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `q3-cash-profit-and-working-capital-pressure`
- `annual-mtn-and-positive-assurances`
- `finance-company-concentration-and-self-assessed-safety`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_enforcement_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000413.XSHE
  - **ticker**: 000413
  - **name_as_of**: 东旭光电
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-10-31
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=000413.XSHE; quarter=2019q3; info_date=2019-10-31; if_adjusted=0
  - **matching_group**: severe-financial-governance-signal-30m-v1
  - **matching_role**: no_event_temporal_hard_control
  - **hard_negative_reason**: The point-in-time anomalies are severe and a much later final decision confirmed large historical fraud, but no qualifying final decision was issued inside the predeclared 30-month window.
  - **outcome_contract**: Only a dated final CSRC or regional-bureau administrative penalty decision inside the 30-month window can create an event; investigation signals and post-window decisions cannot.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2019_q3_report**: 6549fdba3ee07482e6c36fc69fe946e9ca4473fbaf8c4b94d93cfc86f8aa0c9f
    - **2018_annual_report**: fa24cc35ec2e7a1c38b863e7aa476543336e673b2bb41b2969955e50b0ff07c9
    - **finance_company_risk_report**: 1221ef29da4cfb2c5fc4fcc4ff0cdf149262915549db2fd0281b4859096b70ea
  - **leakage_guard**: All defaults, investigations, enforcement decisions, restatements and delisting information after as_of remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: csrc_final_enforcement_registry_search
    - **title**: 中国证监会及派出机构行政处罚决定检索：东旭光电科技股份有限公司
    - **queried_at**: 2026-08-12
    - **url**: https://neris.csrc.gov.cn/falvfagui/rdqsHeader/mainbody?navbarId=3
    - **query**: 东旭光电科技股份有限公司
    - **window_end**: 2022-04-30
    - **qualifying_decisions_through_window_end**: 0
    - **result**: 截至预设窗口终点没有日期落在窗口内且满足本题口径的最终行政处罚决定。
  - **item 2**:
    - **type**: official_post_window_final_decision_context
    - **title**: 河北证监局行政处罚决定书〔2025〕2号
    - **decision_date**: 2025-06-05
    - **published_at**: 2025-06-06
    - **url**: https://www.csrc.gov.cn/hebei/c103646/c7562784/content.shtml
    - **sha256**: e54386983d78330ab60aeb125b8b858a65fab7949c53334c62c413a835affd4d
    - **not_counted**: true
    - **classification**: post_window_hard_negative_context
    - **finding**: 该决定在窗口结束三年多后才正式认定2015至2019年虚增收入和利润及长期资金占用；它证明本例不是干净公司，却不能反向改写固定窗口标签。

</details>

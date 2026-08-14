# cn-a-2019-enforcement-600781

## Question

你处在2019-04-30的信息环境。请使用下方冻结资料，判断辅仁药业未来30个自然月内是否会发生target定义的重大财务错报最终监管认定。重点比较2018年报和2019年一季报的合并与母公司现金、短期债务、经营现金流、财务费用，以及年报对非经营性占用和违规担保的否定陈述与无保留审计意见。请判断这些材料能否支持现金可得性和治理链条的真实性，并单独估计最终处罚在窗口内落地的概率；不得使用4月30日之后的分红、冻结、调查、处罚或ST信息。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 辅仁药业 (600781, SSE)
- 信息截止 / As of: 2019-04-30
- 预测窗口结束 / Window end: 2021-10-30
- 目标事件 / Target: `regulator_confirmed_material_financial_misstatement_30m`
- 判定定义 / Definition: 未来30个自然月内，中国证监会或其派出机构出具日期落在窗口内的最终《行政处罚决定书》，正式认定公司在as_of之前已经公开的定期报告、发行文件或重组文件中，单项或同一事项累计存在不低于1亿元的虚增或虚减营业收入、利润、货币资金或其他资产，或未披露不低于1亿元的控股股东及关联方非经营性资金占用、违规担保。立案调查、交易所问询、监管措施、行政处罚事先告知、媒体质疑和公司自查均不计；处罚决定晚于窗口也不计。本题预测固定期限内的重大违法最终认定，不等同于判断公司最终是否造假、是否ST或是否违约

#### 判定条件 / Criteria

- `qualifying_final_enforcement_decision_count_30m >= 1` — 窗口内满足监管主体、最终决定、点时文件和1亿元重大性门槛的处罚决定至少一份

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 辅仁药业2018年报：无保留审计与否定占款陈述下，母公司现金仅47.93万元

- Evidence ID: `annual-clean-opinion-and-parent-cash-gap`
- 发布日期 / Published: 2019-04-20
- 来源 / Source: 上海证券交易所法定年度报告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2019-04-20/600781_2018_n.pdf

2018年报勾选不存在控股股东及关联方非经营性占用、也不存在违反决策程序对外担保，瑞华出具标准无保留意见。合并口径货币资金16.5636亿元、短期借款24.8850亿元、经营活动现金流净额10.3234亿元、财务费用2.4449亿元；其中2.8145亿元货币资金受限。母公司口径货币资金只有479,278.87元、短期借款5000万元，合并与母公司现金可得性差异极大。控股股东持有45.03%股份，其中5401.50万股已质押。无保留意见提供审计保证，但并非绝对排除串通、账外占用或控制人凌驾内控。

### 辅仁药业2019年一季报：合并现金18.16亿元，母公司现金仅11.22万元

- Evidence ID: `q1-consolidated-parent-cash-chasm`
- 发布日期 / Published: 2019-04-30
- 来源 / Source: 上海证券交易所法定定期报告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2019-04-30/600781_2019_1.pdf

2019年3月末合并报表货币资金18.1577亿元、短期借款25.2872亿元、流动负债44.9036亿元、应收账款29.4266亿元；一季度营业收入13.6979亿元、归母净利润2.1512亿元、经营活动现金流净额2.2504亿元。可是母公司资产负债表货币资金只有112,160.04元、短期借款4900万元，母公司一季度经营活动现金流为-178,029.95元。合并利润与现金集中在子公司本可有正常业务原因，但在控股股东体系下也提高资金上划、账外安排和外部核验难度。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `regulator_confirmed_material_financial_misstatement_30m`
- 结果日期 / Resolved at: 2020-10-13

### 实际结果 / Realized outcome

- **observations**:
  - **qualifying_final_enforcement_decision_count_30m**: 1
  - **largest_confirmed_material_amount_rmb**: 1336632800
- **derivations**:


### 对应的题内资料 / Expected evidence

- `annual-clean-opinion-and-parent-cash-gap`
- `q1-consolidated-parent-cash-chasm`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_enforcement_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600781.XSHG
  - **ticker**: 600781
  - **name_as_of**: 辅仁药业
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-04-30
  - **allowed_domains**:
    - sse.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=600781.XSHG; quarter=2019q1; info_date=2019-04-30; if_adjusted=0
  - **matching_group**: severe-financial-governance-signal-30m-v1
  - **matching_role**: event
  - **outcome_contract**: Only a dated final CSRC or regional-bureau administrative penalty decision inside the 30-month window can create an event; investigation signals and post-window decisions cannot.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2018_annual_report**: ce99deb626da7b2a208f4ab9f1ca6a106d5dcb0f1d7fe605dc5cad286aef7c96
    - **2019_q1_report**: d06b7f2450e92b49d1a525b10ce13e2efddbac04b779cd7d0a38fb67d2346bbe
  - **leakage_guard**: All dividend failures, freezes, investigations, penalties, restatements and ST labels after as_of remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_final_administrative_penalty_decision
    - **title**: 中国证监会行政处罚决定书（辅仁药业）
    - **decision_no**: 〔2020〕79号
    - **decision_date**: 2020-10-13
    - **published_at**: 2020-10-13
    - **url**: https://www.csrc.gov.cn/csrc/c101928/c1042297/content.shtml
    - **sha256**: 0e467e2458ef186222c12664a680b1b520777ada6cf80f5cec803628fb6439b5
    - **qualifying_pre_as_of_document**: 2018年年度报告
    - **largest_confirmed_material_amount_rmb**: 1336632800
    - **finding**: 最终决定认定2018年报未披露关联方资金占用期末余额13.3663亿元并相应虚增货币资金，另有4笔合计1.4亿元关联担保未披露；决定日期在30个月窗口内。

</details>

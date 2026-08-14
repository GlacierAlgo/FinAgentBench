# cn-a-2019-enforcement-002310

## Question

你处在2019-10-31的信息环境。请使用下方冻结资料，判断东方园林未来30个自然月内是否会发生target定义的重大财务错报最终监管认定。公司已经亏损、经营现金流大幅为负、货币资金大多受限且债务沉重，但北京朝阳国资已完成控制权交割并对部分存续债提供具体担保。请区分真实经营和流动性困境、报表错报风险、国资救助与达到1亿元门槛的最终处罚概率；不得使用窗口后的处罚、ST或重整信息。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 东方园林 (002310, SZSE)
- 信息截止 / As of: 2019-10-31
- 预测窗口结束 / Window end: 2022-04-30
- 目标事件 / Target: `regulator_confirmed_material_financial_misstatement_30m`
- 判定定义 / Definition: 未来30个自然月内，中国证监会或其派出机构出具日期落在窗口内的最终《行政处罚决定书》，正式认定公司在as_of之前已经公开的定期报告、发行文件或重组文件中，单项或同一事项累计存在不低于1亿元的虚增或虚减营业收入、利润、货币资金或其他资产，或未披露不低于1亿元的控股股东及关联方非经营性资金占用、违规担保。立案调查、交易所问询、监管措施、行政处罚事先告知、媒体质疑和公司自查均不计；处罚决定晚于窗口也不计。本题预测固定期限内的重大违法最终认定，不等同于判断公司最终是否造假、是否ST或是否违约

#### 判定条件 / Criteria

- `qualifying_final_enforcement_decision_count_30m >= 1` — 窗口内满足监管主体、最终决定、点时文件和1亿元重大性门槛的处罚决定至少一份

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 东方园林2019年第三季度报告：经营现金流恶化、亏损与国资入主同时发生

- Evidence ID: `q3-distress-and-completed-control-transfer`
- 发布日期 / Published: 2019-10-31
- 来源 / Source: 巨潮资讯法定定期报告
- URL: https://static.cninfo.com.cn/finalpage/2019-10-31/1207047833.PDF

截至2019年9月末，公司货币资金12.9259亿元、短期借款37.6086亿元、应付债券22.9456亿元、流动负债248.0905亿元、应收账款93.0647亿元、存货145.7445亿元。前三季度营业收入38.3612亿元、归母净亏损8.8550亿元、经营现金流净额-14.3006亿元，利息费用6.6811亿元而利息收入仅822.4万元。公司明确披露流动性紧张、工程放缓、融资成本上升；同时披露2019年9月30日股权过户完成，北京朝汇鑫成为控股股东、朝阳区国资委成为实际控制人。已披露的经营困境不等于隐瞒或虚构，更不能直接替代重大错报处罚标签。

### 东方园林2019年半年报：14.82亿元现金中10.19亿元受限，经营现金流为负

- Evidence ID: `h1-restricted-cash-and-explicit-distress`
- 发布日期 / Published: 2019-08-24
- 来源 / Source: 巨潮资讯法定半年度报告
- URL: https://static.cninfo.com.cn/finalpage/2019-08-24/1206568646.PDF

半年报披露货币资金14.8155亿元，其中10.1866亿元受限；经营活动现金流净额-8.0051亿元，公司评级展望被列入负面观察。报告主动解释融资环境收紧、PPP工程放缓和流动性压力，并披露控股权变更安排及潜在资金支持。风险被较充分地公开呈现，降低了把“数字差”机械等同于隐瞒重大错报的合理性，但长周期项目收入和成本确认仍具有估计不确定性。

### 朝阳国资中心为东方园林两期存续债提供无条件不可撤销连带担保

- Evidence ID: `state-credit-support-already-effective`
- 发布日期 / Published: 2019-09-20
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2019-09-20/1206940064.PDF

北京市朝阳区国有资本经营管理中心已为16东林02余额4.2111亿元和16东林03余额6亿元的本金、利息、违约金及实现债权费用提供无条件、不可撤销连带责任保证，担保函自出具日起生效。公告列示担保人2018年末总资产1,073.17亿元、净资产297.87亿元，AAA评级，贷款偿还率和利息偿付率均为100%。国资支持可缓和流动性和持续经营压力，却既不能证明历史报表完全准确，也不能构成监管处罚的前置事实。

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

- `q3-distress-and-completed-control-transfer`
- `h1-restricted-cash-and-explicit-distress`
- `state-credit-support-already-effective`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_enforcement_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002310.XSHE
  - **ticker**: 002310
  - **name_as_of**: 东方园林
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
  - **row_policy**: stock_code=002310.XSHE; quarter=2019q3; info_date=2019-10-31; if_adjusted=0
  - **matching_group**: severe-financial-governance-signal-30m-v1
  - **matching_role**: no_event_threshold_and_temporal_control
  - **hard_negative_reason**: Severe disclosed operating distress is not equivalent to material fraud enforcement. A later 2024 accounting-error decision was both post-window and below the CNY100m threshold.
  - **outcome_contract**: Only a dated final CSRC or regional-bureau administrative penalty decision inside the 30-month window can create an event; investigation signals, subthreshold matters and post-window decisions cannot.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2019_q3_report**: 5c00d92e78bd3620e736cc881a6cc2a7083028c5665bb982b94f4c6aabd08d91
    - **2019_half_year_report**: f93530bde18603f6de3f90793f5aea2046881c6dba1dd32d268a76b925bb4d7e
    - **state_guarantee_notice**: ca8916533da142c308c4f6aa1a47ac3c7f692197f1bf435984fd5e5940f3592a
  - **leakage_guard**: All later enforcement, ST, restructuring and bankruptcy information remains label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: csrc_final_enforcement_registry_search
    - **title**: 中国证监会及派出机构行政处罚决定检索：北京东方园林环境股份有限公司
    - **queried_at**: 2026-08-12
    - **url**: https://neris.csrc.gov.cn/falvfagui/rdqsHeader/mainbody?navbarId=3
    - **query**: 北京东方园林环境股份有限公司
    - **window_end**: 2022-04-30
    - **qualifying_decisions_through_window_end**: 0
    - **result**: 截至预设窗口终点没有日期落在窗口内且满足本题口径的最终行政处罚决定。
  - **item 2**:
    - **type**: official_post_window_subthreshold_decision_context
    - **title**: 北京证监局行政处罚决定书〔2024〕1号
    - **decision_date**: 2024-01-29
    - **published_at**: 2024-01-30
    - **url**: https://www.csrc.gov.cn/beijing/c105546/c7460231/content.shtml
    - **sha256**: 1f7587d170b95adaee5018d03cf954da156cbc129bbf4d9ae879e43daa61c8fc
    - **not_counted**: true
    - **classification**: post_window_and_below_materiality_context
    - **confirmed_amount_rmb**: 35418400
    - **finding**: 2024年最终决定认定2019年收入、利润和资产各虚增3541.84万元；决定日期晚于窗口且金额低于1亿元门槛，两个条件均不满足。

</details>

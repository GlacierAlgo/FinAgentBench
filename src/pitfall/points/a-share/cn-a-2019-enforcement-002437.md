# cn-a-2019-enforcement-002437

## Question

你处在2019-04-24的信息环境。请使用下方冻结资料，判断誉衡药业未来30个自然月内是否会发生target定义的重大财务错报最终监管认定。公司经历并购后遗症、商誉减值、控股股东近乎满额质押和全部冻结，交易所曾反复关注资金链；另一方面，年报为标准无保留意见，经营现金流较强，一季报仍称不存在非经营性占用和违规担保。请区分控股股东债务危机、上市公司经营问题、报表重大错报和最终执法时点，不要把高商誉或质押机械等同于处罚。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 誉衡药业 (002437, SZSE)
- 信息截止 / As of: 2019-04-24
- 预测窗口结束 / Window end: 2021-10-24
- 目标事件 / Target: `regulator_confirmed_material_financial_misstatement_30m`
- 判定定义 / Definition: 未来30个自然月内，中国证监会或其派出机构出具日期落在窗口内的最终《行政处罚决定书》，正式认定公司在as_of之前已经公开的定期报告、发行文件或重组文件中，单项或同一事项累计存在不低于1亿元的虚增或虚减营业收入、利润、货币资金或其他资产，或未披露不低于1亿元的控股股东及关联方非经营性资金占用、违规担保。立案调查、交易所问询、监管措施、行政处罚事先告知、媒体质疑和公司自查均不计；处罚决定晚于窗口也不计。本题预测固定期限内的重大违法最终认定，不等同于判断公司最终是否造假、是否ST或是否违约

#### 判定条件 / Criteria

- `qualifying_final_enforcement_decision_count_30m >= 1` — 窗口内满足监管主体、最终决定、点时文件和1亿元重大性门槛的处罚决定至少一份

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 誉衡药业2018年报：商誉33.60亿元、计提2.66亿元减值，但审计意见标准无保留

- Evidence ID: `annual-goodwill-impairment-and-clean-audit`
- 发布日期 / Published: 2019-04-24
- 来源 / Source: 巨潮资讯法定年度报告
- URL: https://static.cninfo.com.cn/finalpage/2019-04-24/1206078184.PDF

2018年公司归母净利润1.2877亿元、扣非净利润仅96.93万元，主要受商誉、应收、固定资产、无形资产和存货合计3.8202亿元减值影响；其中商誉减值2.6612亿元。期末商誉仍为33.6023亿元，占归母净资产77.71%，管理层提示若并购企业不达预期还会继续减值。与此同时，经营活动现金流净额11.6276亿元、货币资金13.0501亿元、短期借款16.5343亿元。上会会计师事务所出具标准无保留意见，并把收入确认和商誉减值列为关键审计事项。高商誉和已确认减值反映经营判断失败，不自动等于财务造假。

### 誉衡药业2019年一季报：控股股东股份全冻，上市公司经营现金流仍为2.07亿元

- Evidence ID: `q1-controller-freeze-but-positive-cash-flow`
- 发布日期 / Published: 2019-04-24
- 来源 / Source: 巨潮资讯法定第一季度报告
- URL: https://static.cninfo.com.cn/finalpage/2019-04-24/1206078195.PDF

2019年3月末公司货币资金12.8549亿元、短期借款18.3294亿元、商誉33.6023亿元；一季度营业收入12.5919亿元、归母净利润8548.89万元、经营现金流净额2.0704亿元。控股股东誉衡集团持有929,789,325股，质押929,429,011股且全部被冻结；实际控制人持股也被冻结。报告仍勾选不存在控股股东及关联方非经营性占用和违规对外担保。控制人融资困境增加治理风险，但上市公司当期现金流和披露并未形成对重大错报的直接认定。

### 中证网2018年调查：两个月三份关注函、易主失败与近满额质押

- Evidence ID: `contemporaneous-repeated-inquiries-and-pledge-distress`
- 发布日期 / Published: 2018-06-20
- 来源 / Source: 上海证券报报道，经中证网发布的冻结网页
- URL: https://www.cs.com.cn/ssgs/gsxw/201806/t20180620_5825911.html

报道梳理公司两个月内收到三份关注函：拟40亿元收购一家2017年收入仅144.49万元、承诺未来三年净利润18亿元的胰岛素企业；出售优质资产和控制权转让计划突然终止；交易所要求说明资金链和债务是否影响经营。誉衡集团和誉衡国际持股质押率分别达99.35%和99.55%，部分质押触及平仓线、发生强制平仓和被动减持，誉衡集团另有30.42%持股被冻结。公司则强调上市公司与控股股东主体独立。该报道提供强治理压力，却未声称上市公司财报已经虚假。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `regulator_confirmed_material_financial_misstatement_30m`
- 结果日期 / Resolved at: 2021-10-24

### 实际结果 / Realized outcome

- **observations**:
  - **qualifying_final_enforcement_decision_count_30m**: 0
  - **largest_confirmed_material_amount_rmb**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `annual-goodwill-impairment-and-clean-audit`
- `q1-controller-freeze-but-positive-cash-flow`
- `contemporaneous-repeated-inquiries-and-pledge-distress`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_enforcement_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002437.XSHE
  - **ticker**: 002437
  - **name_as_of**: 誉衡药业
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-04-24
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
  - **row_policy**: stock_code=002437.XSHE; quarter=2019q1; info_date=2019-04-24; if_adjusted=0
  - **matching_group**: severe-financial-governance-signal-30m-v1
  - **matching_role**: no_event_hard_control
  - **hard_negative_reason**: Controller distress, repeated exchange attention and very large goodwill create a difficult ex-ante risk profile, but no qualifying company financial-misstatement final decision was issued inside the window.
  - **outcome_contract**: Only a dated final CSRC or regional-bureau administrative penalty decision inside the 30-month window can create an event; investigation signals and post-window decisions cannot.
  - **news_evidence_policy**: Contemporaneous reporting is frozen as an ex-ante search result and attributed as analysis rather than adjudicated fact.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2018_annual_report**: f4f796a851e9dff9e6dbab7df1f039e2d7a5679e6a0ea5bb6cc2c202fc7d534d
    - **2019_q1_report**: 9c01b48c078a5848787115e56df0cef37123c502fc585fa009f98f30ed58c2cf
  - **leakage_guard**: All post-as-of investigations, enforcement, ownership changes, later impairments and ST information remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: csrc_final_enforcement_registry_search
    - **title**: 中国证监会及派出机构行政处罚决定检索：哈尔滨誉衡药业股份有限公司
    - **queried_at**: 2026-08-12
    - **url**: https://neris.csrc.gov.cn/falvfagui/rdqsHeader/mainbody?navbarId=3
    - **query**: 哈尔滨誉衡药业股份有限公司
    - **window_end**: 2021-10-24
    - **qualifying_decisions_through_window_end**: 0
    - **result**: 截至预设窗口终点，没有针对公司as_of前财务报告且满足1亿元重大性口径的最终行政处罚决定；自然人内幕交易等不同违法类型不计。
  - **item 2**:
    - **type**: official_periodic_report_context
    - **title**: 誉衡药业2020年年度报告
    - **published_at**: 2021-04-24
    - **url**: https://static.cninfo.com.cn/finalpage/2021-04-24/1209788130.PDF
    - **not_counted_as_enforcement**: true
    - **finding**: 窗口内后续法定报告用于核对公司持续披露轨迹；定期报告或审计意见本身不是行政处罚决定，也不能单独证明永久不存在错报。

</details>

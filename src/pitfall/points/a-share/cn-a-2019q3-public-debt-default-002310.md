# cn-a-2019q3-public-debt-default-002310

## Question

你处在2019-10-31收盘后的信息环境。请使用下方冻结资料，判断东方园林未来120个自然日是否会发生target定义的重大公开债务兑付失败。先确认19东林01和19东林02的付息与投资者回售窗口，再综合账面现金、受限资金、经营现金流、应收和存货沉淀、亏损与融资成本、历史技术性延迟、国资控制权交割和外部担保。国资背景不能机械等同于兜底，历史延迟也不能机械等同于再次违约；应判断支持是否已经落地且覆盖哪些债务。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 东方园林 (002310, SZSE)
- 信息截止 / As of: 2019-10-31
- 预测窗口结束 / Window end: 2020-02-28
- 目标事件 / Target: `material_public_debt_payment_failure_120d`
- 判定定义 / Definition: 发行人在未来120个自然日内，至少一次对计划兑付金额不低于5000万元的公开发行公司债、中期票据、短融或超短融本金、利息或投资者回售款，截至法定兑付日营业终了未按约足额支付，并由发行人或清算机构正式披露。后续补足不撤销已发生事件；银行贷款、供应商欠款、商业承兑汇票及未公开私人展期不计入。本题预测近期公开兑付失败，不等同于预测最终财务造假、ST或长期破产

#### 判定条件 / Criteria

- `material_public_debt_payment_failure_count_120d >= 1` — 窗口内满足口径的公开债务兑付失败至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 东方园林2019年第三季度报告：经营现金流恶化、亏损与国资入主同时发生

- Evidence ID: `q3-distress-and-completed-control-transfer`
- 发布日期 / Published: 2019-10-31
- 来源 / Source: 巨潮资讯法定定期报告
- URL: https://static.cninfo.com.cn/finalpage/2019-10-31/1207047833.PDF

截至2019年9月末，公司货币资金12.9259亿元、短期借款37.6086亿元、应付债券22.9456亿元、流动负债248.0905亿元、应收账款93.0647亿元、存货145.7445亿元。前三季度营业收入38.3612亿元、归母净亏损8.8550亿元、经营现金流净额-14.3006亿元，利息费用6.6811亿元而利息收入仅822.4万元。公司明确称自身流动性紧张、工程放缓、融资成本上升；同时披露2019年9月30日股权过户完成，北京朝汇鑫成为控股股东、北京市朝阳区国资委成为实际控制人，并预计流动性改善。困难是已实现数据，改善是管理层预期，不能混为一谈。

### 东方园林2019年半年度报告：两期13亿元公司债将在一年末触发回售选择权

- Evidence ID: `bond-put-opportunity-and-prior-technical-delay`
- 发布日期 / Published: 2019-08-24
- 来源 / Source: 巨潮资讯法定半年度报告
- URL: https://static.cninfo.com.cn/finalpage/2019-08-24/1206568646.PDF

19东林01于2019年1月15日发行5.2亿元、利率7.50%，19东林02于2019年2月1日发行7.8亿元、利率7.50%；两期均为2年期、在第1年末设置发行人调息和投资者回售选择权，因此付息及可能的回售款落在预测窗口。报告还披露货币资金14.8155亿元中10.1866亿元受限，经营现金流-8.0051亿元，并把公司评级展望列入负面观察；受托管理人记录18东方园林CP002曾因操作问题未及时兑付。公司同时称新控股股东将通过直接资金支持和增信保障债务兑付。

### 朝阳国资中心为东方园林两期存续债提供无条件不可撤销连带担保

- Evidence ID: `state-credit-support-already-effective`
- 发布日期 / Published: 2019-09-20
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2019-09-20/1206940064.PDF

北京市朝阳区国有资本经营管理中心已为16东林02余额4.2111亿元和16东林03余额6亿元的本金、利息、违约金及实现债权费用提供无条件、不可撤销连带责任保证，担保函自出具日起生效。公告列示担保人2018年末总资产1,073.17亿元、净资产297.87亿元，AAA评级，贷款偿还率和利息偿付率均为100%。该担保不直接覆盖19东林01/02，不能视为这两期债券的法律兜底；但它与已完成的控制权交割共同提供了“国资支持已从意向走向具体行动”的点时证据。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `material_public_debt_payment_failure_120d`
- 结果日期 / Resolved at: 2020-02-28

### 实际结果 / Realized outcome

- **observations**:
  - **scheduled_material_public_debt_payment_count_120d**: 2
  - **scheduled_material_public_debt_payment_amount_rmb**: 168580425
  - **material_public_debt_payment_failure_count_120d**: 0
  - **material_public_debt_payment_failure_amount_rmb**: 0
  - **material_public_debt_payment_completed_count_120d**: 2
  - **material_public_debt_payment_completed_amount_rmb**: 168580425
- **derivations**:


### 对应的题内资料 / Expected evidence

- `q3-distress-and-completed-control-transfer`
- `bond-put-opportunity-and-prior-technical-delay`
- `state-credit-support-already-effective`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_public_debt_default_v1
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
  - **matching_group**: reported-cash-public-maturity-120d-v1
  - **matching_role**: no_event_hard_control
  - **opportunity_contract**: At least one ex-ante identifiable public-debt payment of CNY50m or more falls inside the 120-day window.
  - **hard_negative_reason**: Severe negative operating cash flow, losses, a prior technical payment delay and near-term put dates coexist with completed state-control transfer and concrete credit support.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2019_q3_report**: 5c00d92e78bd3620e736cc881a6cc2a7083028c5665bb982b94f4c6aabd08d91
    - **2019_half_year_report**: f93530bde18603f6de3f90793f5aea2046881c6dba1dd32d268a76b925bb4d7e
    - **state_guarantee_notice**: ca8916533da142c308c4f6aa1a47ac3c7f692197f1bf435984fd5e5940f3592a
  - **outcome_label_policy**: Only issuer or clearing-house end-of-due-date disclosures count; later cure does not erase an event.
  - **leakage_guard**: Post-as-of put elections, payment-completion notices and later financial reports are label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_payment_notice
    - **title**: 关于19东林01公司债券回售结果的公告
    - **published_at**: 2020-01-13
    - **url**: https://static.cninfo.com.cn/finalpage/2020-01-13/1207246295.PDF
    - **sha256**: 5a9fb0c6e76e3b330c3b5e8eb70486be897b2825bcfe2a6f9b086a7f9e897641
    - **instrument**: 19东林01
    - **funds_arrival_at**: 2020-01-15
    - **amount_rmb**: 75580025
    - **result**: 公告出具日前回售本金及利息已足额兑付
  - **item 2**:
    - **type**: official_issuer_payment_notice
    - **title**: 关于19东林02公司债券回售结果的公告
    - **published_at**: 2020-01-23
    - **url**: https://static.cninfo.com.cn/finalpage/2020-01-23/1207284598.PDF
    - **sha256**: e3ae29dde389e966d26593f17624646eb0466d18b554d84c71ae75f33e8d573a
    - **instrument**: 19东林02
    - **funds_arrival_at**: 2020-02-03
    - **amount_rmb**: 93000400
    - **result**: 公告出具日前回售本金及利息已足额兑付

</details>

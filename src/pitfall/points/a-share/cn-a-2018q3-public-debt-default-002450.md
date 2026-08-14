# cn-a-2018q3-public-debt-default-002450

## Question

你处在2018-10-23收盘后的信息环境。请使用下方冻结资料，判断康得新未来120个自然日是否会发生target定义的重大公开债务兑付失败。先确认窗口内真实到期的公开债务及金额，再把合并报表货币资金与母公司资金、受限或关联控制可能性、经营现金流、应收账款、利息收入和利息费用、再融资依赖及治理披露交叉核对。巨额账面现金既不是必然安全，也不能仅凭异常就直接判定违约；不要使用窗口后的调查、ST或退市结果。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 康得新 (002450, SZSE)
- 信息截止 / As of: 2018-10-23
- 预测窗口结束 / Window end: 2019-02-20
- 目标事件 / Target: `material_public_debt_payment_failure_120d`
- 判定定义 / Definition: 发行人在未来120个自然日内，至少一次对计划兑付金额不低于5000万元的公开发行公司债、中期票据、短融或超短融本金、利息或投资者回售款，截至法定兑付日营业终了未按约足额支付，并由发行人或清算机构正式披露。后续补足不撤销已发生事件；银行贷款、供应商欠款、商业承兑汇票及未公开私人展期不计入。本题预测近期公开兑付失败，不等同于预测最终财务造假、ST或长期破产

#### 判定条件 / Criteria

- `material_public_debt_payment_failure_count_120d >= 1` — 窗口内满足口径的公开债务兑付失败至少一次

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 康得新2018年第三季度报告：账面现金150亿元，但利息支出显著高于利息收入

- Evidence ID: `q3-cash-profit-and-financing-paradox`
- 发布日期 / Published: 2018-10-23
- 来源 / Source: 巨潮资讯法定定期报告
- URL: https://static.cninfo.com.cn/finalpage/2018-10-23/1205522221.PDF

截至2018年9月末，合并口径货币资金150.1353亿元、短期借款61.8081亿元、应付债券40.4654亿元、流动负债121.0236亿元、应收账款71.4517亿元，归母权益200.0600亿元。前三季度营业收入108.3475亿元、归母净利润22.0144亿元、扣非净利润21.6036亿元、经营活动现金流净额20.7367亿元。与此同时，前三季度利息费用5.5755亿元而利息收入仅1.9792亿元：公司在持有巨额现金的同时仍承担大量有息融资成本。报告还勾选公司不存在控股股东及关联方非经营性占款、无违规对外担保；这些是截至当时的公司披露，不是对资金可自由动用的外部验证。

### 康得新2018年度第一、二期超短期融资券发行结果：15亿元均将在2019年1月到期

- Evidence ID: `two-scp-maturities-inside-window`
- 发布日期 / Published: 2018-05-03
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2018-05-03/1204888171.PDF

18康得新SCP001实际发行10亿元，期限270日，票面利率5.50%，起息日2018年4月20日，兑付日2019年1月15日；18康得新SCP002实际发行5亿元，期限270日，票面利率5.83%，起息日2018年4月26日，兑付日2019年1月21日。两笔公开债务均落在预测窗口内，合计本金15亿元，相对于三季报账面现金很小，因此问题不只是静态现金数量，而是现金真实性、控制权和到期日可用性。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `material_public_debt_payment_failure_120d`
- 结果日期 / Resolved at: 2019-01-15

### 实际结果 / Realized outcome

- **observations**:
  - **scheduled_material_public_debt_payment_count_120d**: 3
  - **scheduled_material_public_debt_payment_amount_rmb**: 1617247945.21
  - **material_public_debt_payment_failure_count_120d**: 3
  - **material_public_debt_payment_failure_amount_rmb**: 1617247945.21
  - **material_public_debt_payment_completed_count_120d**: 0
  - **material_public_debt_payment_completed_amount_rmb**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `q3-cash-profit-and-financing-paradox`
- `two-scp-maturities-inside-window`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_public_debt_default_v1
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
  - **matching_group**: reported-cash-public-maturity-120d-v1
  - **matching_role**: event
  - **opportunity_contract**: At least one ex-ante identifiable public-debt payment of CNY50m or more falls inside the 120-day window.
  - **later_adjudicated_context**: Regulator-confirmed multi-year financial fraud informed candidate selection only and is excluded from the frozen corpus and prompt.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2018_q3_report**: b3d7c478a1f19f71f45c811c011407e7cb738779695f94b8adbc2fde6e1385a8
    - **2018_scp_issuance_result**: 4f503805c33672c0e7a5ffddb6691ce7911a2e0e502714f22b5cf7e61d61469e
  - **outcome_label_policy**: Only issuer or clearing-house end-of-due-date disclosures count; later cure does not erase an event.
  - **leakage_guard**: Post-as-of investigations, risk-warning status, penalties, restatements and delisting information are label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_default_notice
    - **title**: 2018年度第一期超短期融资券未按期兑付本息的公告
    - **published_at**: 2019-01-16
    - **url**: https://static.cninfo.com.cn/finalpage/2019-01-16/1205773010.PDF
    - **sha256**: fd7fb5854b3175b6c3b1e41365cbd493aa9a8861afd20b95b2ebb4eddfd71572
    - **instrument**: 18康得新SCP001
    - **due_at**: 2019-01-15
    - **amount_rmb**: 1040684931.51
    - **result**: 截至兑付日营业终了未按期足额偿付本息，构成实质违约
  - **item 2**:
    - **type**: official_issuer_default_notice
    - **title**: 2018年度第二期超短期融资券未能按期足额偿付本息的公告
    - **published_at**: 2019-01-22
    - **url**: https://static.cninfo.com.cn/finalpage/2019-01-22/1205786098.PDF
    - **sha256**: d46c5a28407585dea45e676401b4f6683eae88258de9eb06889965c0e03869e0
    - **instrument**: 18康得新SCP002
    - **due_at**: 2019-01-21
    - **amount_rmb**: 521563013.7
    - **result**: 截至兑付日营业终了未按期足额偿付本息，构成实质违约
  - **item 3**:
    - **type**: official_issuer_default_notice
    - **title**: 2017年度第一期中期票据未能按期足额偿付利息的公告
    - **published_at**: 2019-02-18
    - **url**: https://www.hkexnews.hk/listedco/listconews/sehk/2019/0218/LTN201902189995_C.PDF
    - **sha256**: 6a20d7f9ebe1a198b72c93d9f5daa0bf7d9719cc92c425aceeb48a64ca04e176
    - **instrument**: 17康得新MTN001
    - **due_at**: 2019-02-15
    - **amount_rmb**: 55000000
    - **result**: 截至付息日终未按期足额偿付利息，构成实质性违约

</details>

# cn-a-2018q3-public-debt-default-600518

## Question

你处在2018-10-27的信息环境。请使用下方冻结资料，判断康美药业未来120个自然日是否会发生target定义的重大公开债务兑付失败。先确认窗口内真实到期的公开债务及金额，再审视存贷双高、利息收支不对称、经营现金流相对利润和债务的覆盖、库存与应收占用、持续融资需求和可动用流动性。异常财务结构应提高怀疑，但本题只判定近期兑付结果，不能把可能的报表失真、后来监管结论或长期信用风险直接替代标签。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 康美药业 (600518, SSE)
- 信息截止 / As of: 2018-10-27
- 预测窗口结束 / Window end: 2019-02-24
- 目标事件 / Target: `material_public_debt_payment_failure_120d`
- 判定定义 / Definition: 发行人在未来120个自然日内，至少一次对计划兑付金额不低于5000万元的公开发行公司债、中期票据、短融或超短融本金、利息或投资者回售款，截至法定兑付日营业终了未按约足额支付，并由发行人或清算机构正式披露。后续补足不撤销已发生事件；银行贷款、供应商欠款、商业承兑汇票及未公开私人展期不计入。本题预测近期公开兑付失败，不等同于预测最终财务造假、ST或长期破产

#### 判定条件 / Criteria

- `material_public_debt_payment_failure_count_120d >= 1` — 窗口内满足口径的公开债务兑付失败至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 康美药业2018年第三季度报告：现金378亿元、债务融资和财务费用同步上升

- Evidence ID: `q3-larger-cash-and-more-extreme-carry-cost`
- 发布日期 / Published: 2018-10-27
- 来源 / Source: 巨潮资讯法定定期报告
- URL: https://static.cninfo.com.cn/finalpage/2018-10-27/1205546609.PDF

截至2018年9月末，合并口径货币资金377.8846亿元、短期借款124.5173亿元、应付债券147.7427亿元、流动负债294.0493亿元、应收账款61.0559亿元、存货184.4986亿元，归母权益346.2005亿元。前三季度营业收入254.2843亿元、归母净利润38.4730亿元、扣非净利润38.0587亿元、经营活动现金流净额12.9322亿元。利息费用13.0080亿元而利息收入2.4047亿元，财务费用10.9932亿元、同比增加63.56%；公司解释为银行借款和发行债券增加。比康得新更大的存贷双高和较弱的利润现金转化构成明显异常，但异常本身不等于窗口内必然兑付失败。

### 康美药业2018年度第三期超短期融资券发行结果：20亿元于2019年2月12日兑付

- Evidence ID: `scp003-maturity-inside-window`
- 发布日期 / Published: 2018-05-22
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2018-05-22/1204980553.PDF

18康美SCP003（代码011800952）实际发行总额20亿元，期限270日，票面利率5.90%，起息日2018年5月18日，兑付日2019年2月12日。该笔公开债务完整落在预测窗口内，金额远超5000万元入选门槛；判断必须同时考虑财务异常和公司是否仍能调动外部融资或其他资源完成单次公开兑付。

### 康美药业2018年半年度报告：窗口内还有两期超短融和15康美债年度付息

- Evidence ID: `h1-complete-public-debt-calendar`
- 发布日期 / Published: 2018-08-29
- 来源 / Source: 巨潮资讯法定半年度报告
- URL: https://static.cninfo.com.cn/finalpage/2018-08-29/1205349494.PDF

半年报附注明确列示：18康美SCP001发行15亿元、利率5.38%、兑付日2018年12月2日；18康美SCP002发行15亿元、利率5.49%、兑付日2018年12月11日；18康美SCP003发行20亿元、利率5.90%、兑付日2019年2月12日。公司债章节同时列示15康美债余额24亿元、票面利率5.33%、每年付息一次，因此2019年1月还需支付约1.2792亿元年度利息。由此，预测窗内不是单笔20亿元到期，而是至少四笔均超过5000万元门槛的公开支付机会；完整机会集合可防止事后只挑选最容易解释的一笔。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `material_public_debt_payment_failure_120d`
- 结果日期 / Resolved at: 2019-02-24

### 实际结果 / Realized outcome

- **observations**:
  - **scheduled_material_public_debt_payment_count_120d**: 4
  - **scheduled_material_public_debt_payment_amount_rmb**: 5335820000
  - **material_public_debt_payment_failure_count_120d**: 0
  - **material_public_debt_payment_failure_amount_rmb**: 0
  - **material_public_debt_payment_completed_count_120d**: 4
  - **material_public_debt_payment_completed_amount_rmb**: 5335820000
- **derivations**:


### 对应的题内资料 / Expected evidence

- `q3-larger-cash-and-more-extreme-carry-cost`
- `scp003-maturity-inside-window`
- `h1-complete-public-debt-calendar`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_public_debt_default_v1
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
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=600518.XSHG; quarter=2018q3; info_date=2018-10-27; if_adjusted=0
  - **matching_group**: reported-cash-public-maturity-120d-v1
  - **matching_role**: no_event_hard_control
  - **opportunity_contract**: At least one ex-ante identifiable public-debt payment of CNY50m or more falls inside the 120-day window.
  - **hard_negative_reason**: The issuer was later found to have materially false cash and profits, yet the predeclared near-term instrument was paid in full; fraud suspicion is therefore not a mechanical default label.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2018_q3_report**: bc31d7e1f8407a7c2d70ba9bc9a9163ef45db005c171c747cd1766b51d1daf6e
    - **2018_h1_report**: 4a6c4f8cb8fbbd3e5c84fc3c3ed18cdbd35705127469edb8fac7d5eb68fd40ba
    - **2018_scp003_issuance_result**: 50a7f1558794603e08172a355d35c7fe3ef1b4f3fbbf20470031b8bc10b63fdb
  - **outcome_label_policy**: Only issuer or clearing-house end-of-due-date disclosures count; later cure does not erase an event.
  - **leakage_guard**: Post-as-of investigations, penalties, restatements, ST status and restructuring information are label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_payment_notice
    - **title**: 2018年度第一期超短期融资券到期兑付的公告
    - **published_at**: 2018-12-04
    - **url**: https://static.cninfo.com.cn/finalpage/2018-12-04/1205646056.PDF
    - **sha256**: 335fc69ba9fe3650812897d95a38454753955bccbeb7697aa62fad89d28cae3d
    - **instrument**: 18康美SCP001
    - **due_at**: 2018-12-03
    - **amount_rmb**: 1559695890.41
    - **result**: 本息足额兑付
  - **item 2**:
    - **type**: official_issuer_payment_notice
    - **title**: 2018年度第二期超短期融资券到期兑付的公告
    - **published_at**: 2018-12-12
    - **url**: https://static.cninfo.com.cn/finalpage/2018-12-12/1205663175.PDF
    - **sha256**: c81e529deeea6a781934987da8f1f044c987385fb4bd4c7687db2aa68c7e97eb
    - **instrument**: 18康美SCP002
    - **due_at**: 2018-12-11
    - **amount_rmb**: 1560916438.36
    - **result**: 本息足额兑付
  - **item 3**:
    - **type**: official_interest_notice_and_later_periodic_confirmation
    - **title**: 2015年公司债券2019年付息公告及2019年半年度报告履约确认
    - **published_at**: 2019-08-29
    - **url**: https://static.cninfo.com.cn/finalpage/2019-08-29/1206660760.PDF
    - **sha256**: 54aa043f4d980b6eab1def8f7fde5d805d100794c696d90c0be4fe63790a9cac
    - **notice_url**: https://static.cninfo.com.cn/finalpage/2019-01-15/1205769214.PDF
    - **notice_sha256**: 6ab1f37874266814f40076b2432b0eef702f44fc61789758480813c9026f4b29
    - **instrument**: 15康美债
    - **due_at**: 2019-01-28
    - **amount_rmb**: 127920000
    - **result**: 半年报确认已支付本计息年度利息
  - **item 4**:
    - **type**: official_issuer_payment_notice
    - **title**: 2018年度第三期超短期融资券到期兑付的公告
    - **published_at**: 2019-02-13
    - **url**: https://static.cninfo.com.cn/finalpage/2019-02-13/1205827203.PDF
    - **sha256**: d2220988d1ce16b8927b3df9b91df3f18d0cf419416ed204b3c0fcfc63b2078c
    - **instrument**: 18康美SCP003
    - **due_at**: 2019-02-12
    - **amount_rmb**: 2087287671.23
    - **result**: 本息足额兑付

</details>

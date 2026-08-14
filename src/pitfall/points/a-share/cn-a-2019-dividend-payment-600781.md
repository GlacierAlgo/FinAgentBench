# cn-a-2019-dividend-payment-600781

## Question

你处在2019-07-16权益分派实施公告发布后的信息环境。请使用下方冻结资料，判断辅仁药业公告的6271.58万元现金红利是否会在未来10个自然日发生target定义的支付失败。不能只用合并货币资金除以分红额：请区分上市公司母公司与子公司现金、经营现金流和利润、短期债务、资金归集能力、控股股东股权冻结、未履行审批的关联担保及其是否已经解除。治理异常应改变置信度，但不能直接替代付款标签。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 辅仁药业 (600781, SSE)
- 信息截止 / As of: 2019-07-16
- 预测窗口结束 / Window end: 2019-07-26
- 目标事件 / Target: `announced_cash_dividend_payment_failure_10d`
- 判定定义 / Definition: 公司已经发布权益分派实施公告并给出确定发放日及不低于5000万元的现金红利总额，但在未来10个自然日内取消或推迟原登记日/除息日/发放日、正式承认未完成分红款划转，或截至原定发放日营业终了仍未按公告足额支付。此后补发不撤销已发生事件；仅调整税款、尾差或不影响足额付款的技术安排不计入。本题测试特定已公告现金支付能否落地，不等同于预测最终财务造假、ST或退市

#### 判定条件 / Criteria

- `announced_cash_dividend_payment_failure_count_10d >= 1` — 窗口内正式取消、推迟或未足额支付已公告现金红利至少一次

<details>
<summary>冻结资料 / Frozen evidence (4)</summary>

### 辅仁药业2019年一季报：合并现金18.16亿元，母公司现金仅11.22万元

- Evidence ID: `q1-consolidated-parent-cash-chasm`
- 发布日期 / Published: 2019-04-30
- 来源 / Source: 上海证券交易所法定定期报告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2019-04-30/600781_2019_1.pdf

2019年3月末合并报表货币资金18.1577亿元、短期借款25.2872亿元、流动负债44.9036亿元、应收账款29.4266亿元；一季度营业收入13.6979亿元、归母净利润2.1512亿元、经营活动现金流净额2.2504亿元。若只看合并口径，6271.58万元分红约有28.95倍现金覆盖。可是母公司资产负债表货币资金只有112,160.04元、短期借款4900万元，母公司一季度经营活动现金流为-178,029.95元。分红法律义务在上市母公司层面，子公司利润与现金能否及时上划是独立于合并总量的关键问题。

### 补充披露关联方反担保：未经董事会或股东大会审批，但3000万元责任已解除

- Evidence ID: `unapproved-related-guarantee-control-failure`
- 发布日期 / Published: 2019-05-14
- 来源 / Source: 上海证券交易所法定临时公告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2019-05-14/600781_20190514_1.pdf

公司补充披露，2018年1月曾与实控人朱文臣、控股股东共同为关联方宋河实业3000万元融资提供连带反担保，事项未履行上市公司审批程序，经办人员也未向董事会报告。截至2019年5月5日相关方已偿清全部款项，公司未承担还款责任且担保责任解除。该事件不再形成直接现金缺口，却提供了关联体系绕过正式审批和信息上报链条的治理证据；应与“责任已解除”的反向事实同时赋权。

### 控股股东持股100%被冻结：45.03%上市公司股份全部进入冻结状态

- Evidence ID: `controller-holding-fully-frozen`
- 发布日期 / Published: 2019-07-04
- 来源 / Source: 上海证券交易所法定临时公告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2019-07-04/600781_20190704_1.pdf

公告显示控股股东辅仁集团持有282,403,538股，占公司总股本45.03%；本次轮候冻结后累计被冻结282,403,538股，占其持股100%，其中已质押67,951,412股。公司称冻结暂不会影响控制权、控股股东正在妥善处理。冻结直接针对股东股份而非上市公司银行账户，不能等同于公司必然付不出分红；但它表明控股股东外部融资压力和集团支持能力已显著恶化。

### 2018年度权益分派实施公告：6271.58万元现金红利定于7月22日发放

- Evidence ID: `formal-dividend-implementation-notice`
- 发布日期 / Published: 2019-07-16
- 来源 / Source: 上海证券交易所法定临时公告
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2019-07-16/600781_20190716_1.pdf

公司以总股本627,157,512股为基数，每股派发现金红利0.10元（含税），合计62,715,751.20元；股权登记日2019年7月19日，除息日和现金红利发放日均为7月22日。无限售流通股红利拟委托中国结算上海分公司通过资金清算系统派发。实施公告把模糊分红意愿转化成有金额、对象和日期的短期支付机会，但公告本身并不构成付款已完成。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `announced_cash_dividend_payment_failure_10d`
- 结果日期 / Resolved at: 2019-07-20

### 实际结果 / Realized outcome

- **observations**:
  - **announced_cash_dividend_amount_rmb**: 62715751.2
  - **consolidated_cash_as_of_rmb**: 1815767804.26
  - **parent_company_cash_as_of_rmb**: 112160.04
  - **announced_cash_dividend_payment_failure_count_10d**: 1
  - **cash_dividend_paid_amount_rmb**: 0
- **derivations**:
  - **item 1**:
    - **metric**: consolidated_cash_to_announced_dividend
    - **operation**: ratio
    - **inputs**:
      - consolidated_cash_as_of_rmb
      - announced_cash_dividend_amount_rmb
    - **value**: 28.952340831723944
  - **item 2**:
    - **metric**: parent_cash_to_announced_dividend
    - **operation**: ratio
    - **inputs**:
      - parent_company_cash_as_of_rmb
      - announced_cash_dividend_amount_rmb
    - **value**: 0.001788387093416494

### 对应的题内资料 / Expected evidence

- `q1-consolidated-parent-cash-chasm`
- `unapproved-related-guarantee-control-failure`
- `controller-holding-fully-frozen`
- `formal-dividend-implementation-notice`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_cash_reality_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600781.XSHG
  - **ticker**: 600781
  - **name_as_of**: 辅仁药业
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-07-16
  - **allowed_domains**:
    - sse.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - dividend_info
    - dividend
  - **row_policy**: stock_code=600781.XSHG; quarter=2019q1; info_date=2019-04-30; if_adjusted=0; dividend effective_date=2018-12-31
  - **matching_group**: implementation-notice-cash-dividend-cny50m-v1
  - **matching_role**: event
  - **opportunity_contract**: A formal implementation notice specifies a cash-dividend payment of at least CNY50m and a payable date inside the 10-day window.
  - **later_adjudicated_context**: Later regulator findings about false cash disclosure and related-party occupation informed candidate selection only and are excluded from the frozen corpus and prompt.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2019_q1_report**: d06b7f2450e92b49d1a525b10ce13e2efddbac04b779cd7d0a38fb67d2346bbe
    - **related_guarantee_supplement**: 4e0863e7d2e6d77445c295eee91568bb1cf0a329d53591014f5277fff13f8a9c
    - **controller_freeze_notice**: 0ce1d65dd96afa0c95ad53f4cf1ecad3bcd14985ce12934f3ce476a7b39bd0f4
    - **dividend_implementation_notice**: 1a0a975c6a770700412705c0f8b9b3c4caff584dca4208994ad7a2d54bce1c06
  - **outcome_label_policy**: An issuer cancellation, postponement, admitted funding-transfer failure, or nonpayment at the announced date counts; later cure does not erase the event.
  - **leakage_guard**: Post-as-of cancellation, inquiries, actual cash availability, investigation, penalties, ST status and delisting are label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_cancellation_notice
    - **title**: 关于调整2018年年度权益分派有关事项暨继续停牌的公告
    - **published_at**: 2019-07-20
    - **url**: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2019-07-20/600781_20190720_1.pdf
    - **sha256**: 530c9be370f5511ec9dd048e3ee82e5801cfe0a4ecf3151ed4d931a8438e6af1
    - **scheduled_payable_at**: 2019-07-22
    - **outcome**: 因资金安排原因未完成分红款划转，原登记日、除息日和现金红利发放日全部取消
  - **item 2**:
    - **type**: rqdata_dividend_outcome
    - **paths**:
      - data/db/dividend_info.parquet
      - data/db/dividend.parquet
    - **stock_code**: 600781.XSHG
    - **effective_date**: 2018-12-31
    - **result**: dividend_info保留每10股1元现金方案但ex_dividend_date为空；completed dividend表不存在2018q4记录

</details>

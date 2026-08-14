# cn-a-2018-dividend-payment-002450

## Question

你处在2018-09-21权益分派实施公告发布后的信息环境。请使用下方冻结资料，判断康得新公告的约2.48亿元现金红利是否会在未来10个自然日发生target定义的支付失败。请把合并与母公司货币资金、受限现金、经营现金流、应收账款、短期债务、控股股东高比例质押和中国结算代派安排放在同一资金可达性框架内。账面异常和控股股东压力不能直接替代当次付款结果，也不得使用后来债务违约、调查或退市信息。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 康得新 (002450, SZSE)
- 信息截止 / As of: 2018-09-21
- 预测窗口结束 / Window end: 2018-10-01
- 目标事件 / Target: `announced_cash_dividend_payment_failure_10d`
- 判定定义 / Definition: 公司已经发布权益分派实施公告并给出确定发放日及不低于5000万元的现金红利总额，但在未来10个自然日内取消或推迟原登记日/除息日/发放日、正式承认未完成分红款划转，或截至原定发放日营业终了仍未按公告足额支付。此后补发不撤销已发生事件；仅调整税款、尾差或不影响足额付款的技术安排不计入。本题测试特定已公告现金支付能否落地，不等同于预测最终财务造假、ST或退市

#### 判定条件 / Criteria

- `announced_cash_dividend_payment_failure_count_10d >= 1` — 窗口内正式取消、推迟或未足额支付已公告现金红利至少一次

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 康得新2018年半年报：合并现金167.81亿元，母公司现金75.63亿元

- Evidence ID: `h1-consolidated-and-parent-liquidity`
- 发布日期 / Published: 2018-08-17
- 来源 / Source: 巨潮资讯法定半年度报告
- URL: https://static.cninfo.com.cn/finalpage/2018-08-17/1205298768.PDF

2018年6月末合并货币资金167.8111亿元，其中8.7860亿元受限；短期借款63.8322亿元、应付债券39.6499亿元、应收账款64.3304亿元。上半年营业收入72.4058亿元、归母净利润15.1324亿元、经营活动现金流6.3590亿元，同比下降63.86%。母公司口径货币资金75.6288亿元、其他应收款44.5927亿元且无短期借款，约为拟派现金总额的30.53倍。控股股东康得集团持有851,414,682股，其中777,337,646股质押，质押率约91.30%。高质押和应收上升构成治理及资金质量风险，但母公司层面的可见现金覆盖与辅仁药业形成关键反差。

### 2017年度权益分派实施公告：约2.48亿元现金红利定于9月28日代派

- Evidence ID: `formal-dividend-implementation-notice`
- 发布日期 / Published: 2018-09-21
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2018-09-21/1205458669.PDF

公司以3,540,900,282股为基数，每10股派0.699500元现金（含税），据此现金总额约247,685,974.73元；股权登记日2018年9月27日，除权除息日为9月28日。除控股股东康得投资集团的红利由公司自行派发外，其余A股股东现金红利委托中国结算深圳分公司于9月28日直接划入资金账户。公告把支付金额、日期和清算路径全部固定下来，但仍需判断到期是否实际落地。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `announced_cash_dividend_payment_failure_10d`
- 结果日期 / Resolved at: 2018-10-01

### 实际结果 / Realized outcome

- **observations**:
  - **announced_cash_dividend_amount_rmb**: 247685974.73
  - **consolidated_cash_as_of_rmb**: 16781114176.87
  - **parent_company_cash_as_of_rmb**: 7562878648.19
  - **announced_cash_dividend_payment_failure_count_10d**: 0
  - **cash_dividend_paid_amount_rmb**: 247685974.73
- **derivations**:
  - **item 1**:
    - **metric**: consolidated_cash_to_announced_dividend
    - **operation**: ratio
    - **inputs**:
      - consolidated_cash_as_of_rmb
      - announced_cash_dividend_amount_rmb
    - **value**: 67.75157210723361
  - **item 2**:
    - **metric**: parent_cash_to_announced_dividend
    - **operation**: ratio
    - **inputs**:
      - parent_company_cash_as_of_rmb
      - announced_cash_dividend_amount_rmb
    - **value**: 30.534141694677

### 对应的题内资料 / Expected evidence

- `h1-consolidated-and-parent-liquidity`
- `formal-dividend-implementation-notice`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_cash_reality_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002450.XSHE
  - **ticker**: 002450
  - **name_as_of**: 康得新
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2018-09-21
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
    - dividend_info
    - dividend
  - **row_policy**: stock_code=002450.XSHE; quarter=2018q2; info_date=2018-08-17; if_adjusted=0; dividend effective_date=2017-12-31
  - **matching_group**: implementation-notice-cash-dividend-cny50m-v1
  - **matching_role**: no_event_hard_control
  - **opportunity_contract**: A formal implementation notice specifies a cash-dividend payment of at least CNY50m and a payable date inside the 10-day window.
  - **hard_negative_reason**: The issuer was later found to have materially false financial reporting and defaulted on debt, but this particular predeclared cash dividend was paid; later scandal status is not a mechanical payment-failure label.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2018_h1_report**: 77a875346557d5dc5b81e97149034b0a7edf73a5822115e6c4cfca696dfad05f
    - **dividend_implementation_notice**: a4a07caccf36c8553edac14e7d44c8690b249f057d7732eed31377da112ee839
  - **outcome_label_policy**: An issuer cancellation, postponement, admitted funding-transfer failure, or nonpayment at the announced date counts; later cure does not erase the event.
  - **leakage_guard**: Post-as-of payment confirmation, debt defaults, investigations, penalties, ST status and delisting are label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: rqdata_completed_dividend
    - **paths**:
      - data/db/dividend_info.parquet
      - data/db/dividend.parquet
    - **stock_code**: 002450.XSHE
    - **quarter**: 2017q4
    - **declaration_announcement_date**: 2018-09-21
    - **book_closure_date**: 2018-09-27
    - **ex_dividend_date**: 2018-09-28
    - **payable_date**: 2018-09-28
    - **cash_per_10_shares_before_tax**: 0.6995
  - **item 2**:
    - **type**: official_periodic_confirmation
    - **title**: 康得新2018年第三季度报告：权益分派实施
    - **published_at**: 2018-10-23
    - **url**: https://static.cninfo.com.cn/finalpage/2018-10-23/1205522221.PDF
    - **sha256**: b3d7c478a1f19f71f45c811c011407e7cb738779695f94b8adbc2fde6e1385a8
    - **outcome**: 重大事项章节列示2017年度权益分派实施及2018年9月28日除权除息日

</details>

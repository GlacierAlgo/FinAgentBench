# cn-a-2014-public-bond-default-6m-002306

## Question

你处在2014-10-31收盘后的信息环境。中科云网的12湘鄂债已被下调至BBB并实施债券风险警示，投资者回售兑付日在预测窗口内。请使用冻结材料，预测公司未来6个自然月内是否会发生target定义的重大公开债务兑付失败。把确切到期义务与账面现金、经营现金流、扣非亏损、资产处置依赖、融资可得性和增信安排逐项对齐；BBB或ST债本身不是违约标签，账面现金也必须与回售规模和使用约束比较。不要使用2014-10-31之后的筹资、年报、股票*ST或实际兑付结果。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 中科云网 (002306, SZSE)
- 信息截止 / As of: 2014-10-31
- 预测窗口结束 / Window end: 2015-04-30
- 目标事件 / Target: `material_public_debt_payment_failure_6m`
- 判定定义 / Definition: 发行人在未来6个自然月内，至少一次对计划兑付金额不低于5000万元的公开发行公司债本金、利息或投资者回售款，截至约定兑付日营业终了未按约足额支付，并由发行人、交易所或清算机构正式披露。后续筹资补足或最终兑付不撤销已经发生的事件；股票ST、债项评级下调、银行贷款、供应商欠款和未公开私人展期不计入

#### 判定条件 / Criteria

- `material_public_debt_payment_failure_count_6m >= 1` — 窗口内满足金额和官方披露口径的公开债务兑付失败至少一次

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 12湘鄂债评级降至BBB并实施风险警示，回售兑付日为2015年4月7日

- Evidence ID: `bond-bbb-put-date-and-risk-warning`
- 发布日期 / Published: 2014-10-15
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2014-10-15/1200300157.PDF

公司披露主体及12湘鄂债信用等级降至BBB、评级展望为负面，债券简称变更为ST湘鄂债。公告列明投资者回售资金及第三期利息兑付日为2015年4月7日，明确落在预测窗口内。评级下调和风险警示不是实际兑付失败，但它们要求预测者把确定到期义务、增信安排与公司的可动用现金和再融资能力相匹配。

### 中科云网2014年三季报：扣非亏损扩大且经营现金流为负

- Evidence ID: `q3-2014-loss-cash-and-nonrecurring-support`
- 发布日期 / Published: 2014-10-31
- 来源 / Source: 证券时报刊载的发行人法定季度报告
- URL: https://epaper.stcn.com/paper/zqsb/html/2014-10/31/content_626196.htm

截至2014年9月末，公司货币资金98,666,404.16元。前三季度营业收入558,521,000.73元、归母净利润-95,626,027.72元、扣非归母净利润-176,572,532.03元、经营活动现金流净额-58,001,042.12元。归母亏损小于扣非亏损，表明非经常性项目提供了显著支撑；不足1亿元的期末现金还需同时覆盖持续经营消耗和2015年4月的公开债券回售与利息义务。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `material_public_debt_payment_failure_6m`
- 结果日期 / Resolved at: 2015-04-07
- 可观察日期 / Observed at: 2015-04-07

### 实际结果 / Realized outcome

- **observations**:
  - **scheduled_material_public_debt_payment_count_6m**: 1
  - **material_public_debt_payment_failure_count_6m**: 1
  - **material_public_debt_payment_completed_count_6m**: 0
  - **scheduled_payment_amount_rmb**: 402034300
  - **funds_raised_for_payment_rmb**: 161403300
  - **reported_funding_shortfall_rmb**: 240631000
- **derivations**:


### 对应的题内资料 / Expected evidence

- `bond-bbb-put-date-and-risk-warning`
- `q3-2014-loss-cash-and-nonrecurring-support`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_public_debt_default_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002306.XSHE
  - **ticker**: 002306
  - **name_as_of**: 中科云网
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2014-10-31
  - **allowed_domains**:
    - cninfo.com.cn
    - stcn.com
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=002306.XSHE; quarter=2014q3; info_date<=2014-10-31; if_adjusted=0; public-bond maturity and payment result adjudicated from issuer filings
  - **matching_group**: identified-public-debt-maturity-6m-v1
  - **matching_role**: event
  - **opportunity_contract**: A publicly disclosed bond interest/put payment of at least CNY50m is scheduled inside the six-month window.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2014_bond_rating_notice**: 44cdea6f0bc9872d763d4140a815e27333b5028011cf42e897202758237edb89
    - **2015_default_risk_notice**: b64dc1bb17c67dd59ad5058ea17f920b1ce882005d7bc152e961673d3cb65ef9
  - **outcome_contract**: Issuer-, exchange- or clearing-house-confirmed failure to pay by the due-date close counts; a later cure does not erase the event.
  - **leakage_guard**: The April 2015 funding shortfall, payment failure, annual report, stock *ST status and later bond cure remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_default_notice
    - **title**: 中科云网科技集团股份有限公司2012年公司债券违约公告
    - **published_at**: 2015-04-07
    - **url**: https://static.cninfo.com.cn/finalpage/2015-04-07/1200789243.PDF
    - **sha256**: 3eb1ea4a49d0699deaa860c94776695723cb676eefec92b412725e8764666183
    - **instrument**: ST湘鄂债（112072）
    - **due_at**: 2015-04-07
    - **result**: 第三期利息及投资者回售款未按期足额支付，构成实质违约；公告披露已筹资金161,403,300元、资金缺口240,631,000元

</details>

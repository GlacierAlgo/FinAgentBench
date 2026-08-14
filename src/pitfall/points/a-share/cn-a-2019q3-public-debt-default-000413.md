# cn-a-2019q3-public-debt-default-000413

## Question

你处在2019-10-31收盘后的信息环境。请使用下方冻结资料，判断东旭光电未来120个自然日是否会发生target定义的重大公开债务兑付失败。必须先定位中票的回售付息压力，再拆解合并货币资金中受限资金与集团财务公司存款的可用性，比较利润、经营现金流、应收账款、短期借款和利息负担，并审视财务公司风险评估是实质保障还是关联方自我陈述。不要把账面现金、评级、公司声称风险可控或后来违约机械替代推理。给出概率、二元判断、证据ID与简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 东旭光电 (000413, SZSE)
- 信息截止 / As of: 2019-10-31
- 预测窗口结束 / Window end: 2020-02-28
- 目标事件 / Target: `material_public_debt_payment_failure_120d`
- 判定定义 / Definition: 发行人在未来120个自然日内，至少一次对计划兑付金额不低于5000万元的公开发行公司债、中期票据、短融或超短融本金、利息或投资者回售款，截至法定兑付日营业终了未按约足额支付，并由发行人或清算机构正式披露。后续补足不撤销已发生事件；银行贷款、供应商欠款、商业承兑汇票及未公开私人展期不计入。本题预测近期公开兑付失败，不等同于预测最终财务造假、ST或长期破产

#### 判定条件 / Criteria

- `material_public_debt_payment_failure_count_120d >= 1` — 窗口内满足口径的公开债务兑付失败至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 东旭光电2019年第三季度报告：现金183亿元但经营现金流仅1.27亿元

- Evidence ID: `q3-cash-profit-and-working-capital-pressure`
- 发布日期 / Published: 2019-10-31
- 来源 / Source: 巨潮资讯法定定期报告
- URL: https://static.cninfo.com.cn/finalpage/2019-10-31/1207047204.PDF

截至2019年9月末，合并口径货币资金183.1633亿元、短期借款101.2915亿元、应付票据12.4511亿元、应付债券52.8389亿元、流动负债270.4604亿元、应收账款118.0107亿元、商誉27.0240亿元，归母权益332.8240亿元。前三季度营业收入125.6620亿元、归母净利润11.3488亿元、扣非净利润9.6203亿元，但经营活动现金流净额只有1.2711亿元；利息费用8.9774亿元、利息收入3.1902亿元。报告仍勾选无控股股东非经营性占款和无违规担保。账面现金足以覆盖近期回售不代表资金在到期日可提取。

### 东旭光电2018年年度报告：47亿元中票含3+2年品种，2019年进入首个回售节点

- Evidence ID: `mtn-structure-and-prior-payment-record`
- 发布日期 / Published: 2019-04-30
- 来源 / Source: 巨潮资讯法定年度报告
- URL: https://static.cninfo.com.cn/finalpage/2019-04-30/1206163741.PDF

公司披露2016年中期票据共47亿元，分两期发行：第一期合计30亿元，含3+2年与5年两个品种；第二期合计17亿元，同样含3+2年与5年品种，均每年付息、到期还本。账面附注列示第一期发行日为2016年11月17日、第二期为2016年12月2日，意味着3+2年品种将在预测窗口内进入投资者回售和付息节点。报告同时称15东旭债此前按时付息，说明历史履约记录不能单独排除即将到来的集中兑付风险。

### 东旭集团财务公司2019年半年风险评估：上市公司87.78亿元存款集中于关联财务公司

- Evidence ID: `finance-company-concentration-and-self-assessed-safety`
- 发布日期 / Published: 2019-08-31
- 来源 / Source: 巨潮资讯法定专项报告
- URL: https://static.cninfo.com.cn/finalpage/2019-08-31/1206868029.PDF

专项报告称东旭集团财务公司注册资本50亿元，其中东旭集团出资30亿元、上市公司出资20亿元；截至2019年6月末总资产286.46亿元、负债234.64亿元、净资产51.82亿元，上半年净利润0.42亿元。东旭光电在财务公司的贷款余额为零、存款余额高达87.78亿元，约占同期合并货币资金196.08亿元的44.8%。报告由上市公司查验关联财务公司资料后认为未发现重大内控缺陷、监管指标合规、关联存款风险可控。集中度是可核实事实，“风险可控”则属于关联体系内评估，二者需要分开赋权。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `material_public_debt_payment_failure_120d`
- 结果日期 / Resolved at: 2019-11-18

### 实际结果 / Realized outcome

- **observations**:
  - **scheduled_material_public_debt_payment_count_120d**: 2
  - **scheduled_material_public_debt_payment_amount_rmb**: 3554000000
  - **material_public_debt_payment_failure_count_120d**: 2
  - **material_public_debt_payment_failure_amount_rmb**: 3554000000
  - **material_public_debt_payment_completed_count_120d**: 0
  - **material_public_debt_payment_completed_amount_rmb**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `q3-cash-profit-and-working-capital-pressure`
- `mtn-structure-and-prior-payment-record`
- `finance-company-concentration-and-self-assessed-safety`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_public_debt_default_v1
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
  - **matching_group**: reported-cash-public-maturity-120d-v1
  - **matching_role**: event
  - **opportunity_contract**: At least one ex-ante identifiable public-debt payment of CNY50m or more falls inside the 120-day window.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2019_q3_report**: 6549fdba3ee07482e6c36fc69fe946e9ca4473fbaf8c4b94d93cfc86f8aa0c9f
    - **2018_annual_report**: fa24cc35ec2e7a1c38b863e7aa476543336e673b2bb41b2969955e50b0ff07c9
    - **finance_company_risk_report**: 1221ef29da4cfb2c5fc4fcc4ff0cdf149262915549db2fd0281b4859096b70ea
  - **outcome_label_policy**: Only issuer or clearing-house end-of-due-date disclosures count; later cure does not erase an event.
  - **leakage_guard**: Post-as-of default notices, inquiries, restatements, penalties and ST status are label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_default_notice
    - **title**: 关于2016年度第一期中期票据回售付息未能如期兑付的提示性公告
    - **published_at**: 2019-11-19
    - **url**: https://static.cninfo.com.cn/finalpage/2019-11-19/1207099931.PDF
    - **sha256**: eab3cfd0392deb28ad9df6b7381453d93212b717edf5f5e2028386773aaea9db
    - **instruments**:
      - **item 1**:
        - **instrument**: 16东旭光电MTN001A
        - **due_at**: 2019-11-18
        - **amount_rmb**: 1969000000
        - **eligible**: true
      - **item 2**:
        - **instrument**: 16东旭光电MTN001B
        - **due_at**: 2019-11-18
        - **amount_rmb**: 41000000
        - **eligible**: false
        - **exclusion**: 单笔计划支付金额低于5000万元
    - **result**: 两品种应付利息及相关回售款均未如期兑付
  - **item 2**:
    - **type**: official_issuer_default_notice
    - **title**: 关于2016年度第二期中期票据回售付息未能如期兑付的提示性公告
    - **published_at**: 2019-12-03
    - **url**: https://static.cninfo.com.cn/finalpage/2019-12-03/1207130738.PDF
    - **sha256**: 89f709572e40247f50aaaf06bd150af8039de084684b2a9ddbe15de20f715159
    - **instrument**: 16东旭光电MTN002
    - **due_at**: 2019-12-02
    - **amount_rmb**: 1585000000
    - **result**: 应付利息及相关回售款未如期兑付

</details>

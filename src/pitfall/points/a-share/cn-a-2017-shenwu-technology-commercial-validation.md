# cn-a-2017-shenwu-technology-commercial-validation

## Question

你处在2017-03-27收盘后的信息环境。神雾环保披露蓄热式电石生产、乙炔化工新工艺等技术及多个EPC/示范项目，也披露了大额工程订单对流动资金、项目进度和应收回收的要求。请使用下方冻结资料，从技术验证、客户与关联网络、订单执行、收入与毛利、应收与存货、现金回收、短债和审计可验证性等环节，预测公司能否在2018财年达到target定义的技术业务商业兑现事件。该标签只判断公司层面的可审计结果，不证明技术是结果的唯一原因，也不评价股价。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 神雾环保 (300156, SZSE)
- 信息截止 / As of: 2017-03-27
- 预测窗口结束 / Window end: 2019-05-31
- 目标事件 / Target: `technology_business_commercial_validation`
- 判定定义 / Definition: 公司层面的技术商业兑现事件而非技术投入的因果证明：2018财年同时满足预先声明的收入增长、毛利、盈利、经营现金、短债覆盖、权益保全和审计质量七项条件。收入CAGR=(2018收入/2016收入)^(1/2)-1；毛利率=(收入-营业成本)/收入；短债覆盖=期末货币资金/(短期借款+一年内到期非流动负债)；权益保全=2018归母权益/2016归母权益；标准无保留审计记1，其余记0。

#### 判定条件 / Criteria

- `revenue_cagr_baseline_to_outcome >= 0.2` — 2016年至2018年营业收入复合年增长率不低于20%
- `gross_margin_outcome >= 0.25` — 2018年综合毛利率不低于25%
- `net_profit_outcome > 0` — 2018年归母净利润为正
- `operating_cash_flow_outcome > 0` — 2018年经营活动产生的现金流量净额为正
- `cash_to_short_term_interest_bearing_debt_outcome >= 0.5` — 2018年末货币资金覆盖至少50%的短期借款和一年内到期非流动负债
- `equity_retention_baseline_to_outcome >= 0.8` — 2018年末归母权益至少保留2016年末的80%
- `standard_unqualified_audit_flag_outcome >= 1` — 2018年财务报表审计意见为标准无保留意见

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 神雾环保更新后2016年年报：技术、示范工程与订单扩张

- Evidence ID: `updated-annual-technology-and-projects`
- 发布日期 / Published: 2017-03-27
- 来源 / Source: 神雾环保法定年度报告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2017-03-27/1203202193.PDF

更新后年报披露，公司以工程总承包等模式为煤化工和石油化工客户提供节能环保解决方案。2016年蓄热式电石生产新工艺通过工信部组织的国家级科技成果鉴定；内蒙古港原技改项目于2月底竣工投产，公司称各项节能指标符合预期，并据此新签新疆胜沃二期、乌海项目重大订单及中标包头项目。公司同时提示，单体乙炔化工项目体量大、建设周期长，进度受业主资金、供应商和分包商履约等影响，执行需要充足流动资金；应收账款占资产比例较大，若客户不能按合同付款会产生坏账风险。以上均为公司截至当时的披露，不等于未来商业结果已经兑现。

### 神雾环保更新后2016年年报与PIT财务链：收入、工程资产、现金和债务

- Evidence ID: `updated-annual-pit-financial-chain`
- 发布日期 / Published: 2017-03-27
- 来源 / Source: 神雾环保法定年度报告及只读RQData点时记录
- URL: https://static.cninfo.com.cn/finalpage/2017-03-27/1203202193.PDF

2016年营业收入3,125,095,692.33元、营业成本2,048,528,986.10元、归母净利润705,757,447.74元、经营活动现金流净额217,525,065.10元。年末货币资金1,959,542,066.23元，应收账款净额1,056,809,299.68元，存货951,535,814.45元，其中年报称存货增长与在建项目已完工未结算有关；短期借款533,800,000.00元，一年内到期非流动负债180,279,407.52元，应付债券434,713,471.48元，归母权益2,520,931,396.71元。销售商品、提供劳务收到现金2,485,301,777.02元。点时口径为300156.XSHE、2016q4、if_adjusted=0、截至as_of可见的最早info_date=2017-03-25；3月27日更新后年报作为文字与更正权威。

### 神雾环保2016年年报更正：应收集中、分包成本与现金流分类

- Evidence ID: `annual-correction-concentration-and-cash`
- 发布日期 / Published: 2017-03-27
- 来源 / Source: 神雾环保法定更正公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2017-03-27/1203202192.PDF

更正公告将工程总承包分包成本2016年同比增幅更正为530.82%，金额1,156,725,308.63元、占该产品营业成本56.47%。公告还列示应收账款期末前五名余额合计1,020,897,648.20元，占应收账款期末余额合计数84.75%，其中新疆胜沃、乌海洪远、新疆圣雄和内蒙古港原为主要欠款方；同时更正现金流附注，2016年收到和支付的其他经营活动现金分别为66,797,345.30元和121,430,207.92元，并说明上年与神雾集团往来较大。更正本身要求分析者同时核验利润确认、客户网络、应收集中与现金真实性，不能只看技术鉴定或订单金额。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `technology_business_commercial_validation`
- 结果日期 / Resolved at: 2018-12-31
- 可观察日期 / Observed at: 2019-04-30

### 实际结果 / Realized outcome

- **observations**:
  - **revenue_baseline**: 3125095692.33
  - **revenue_outcome**: 51252984.85
  - **operating_cost_outcome**: 17875101.7
  - **net_profit_outcome**: -1493820999.4
  - **operating_cash_flow_outcome**: -381353184.7
  - **cash_outcome**: 10392424.51
  - **short_term_interest_bearing_debt_outcome**: 1773666845.48
  - **equity_baseline**: 2520931396.71
  - **equity_outcome**: 1286038645.08
  - **standard_unqualified_audit_flag_outcome**: 0
- **derivations**:
  - **item 1**:
    - **metric**: revenue_cagr_baseline_to_outcome
    - **operation**: cagr
    - **inputs**:
      - revenue_baseline
      - revenue_outcome
    - **periods**: 2
    - **value**: -0.8719357468112889
  - **item 2**:
    - **metric**: gross_margin_outcome
    - **operation**: margin
    - **inputs**:
      - revenue_outcome
      - operating_cost_outcome
    - **value**: 0.6512378400533292
  - **item 3**:
    - **metric**: cash_to_short_term_interest_bearing_debt_outcome
    - **operation**: ratio
    - **inputs**:
      - cash_outcome
      - short_term_interest_bearing_debt_outcome
    - **value**: 0.0058592878005720075
  - **item 4**:
    - **metric**: equity_retention_baseline_to_outcome
    - **operation**: ratio
    - **inputs**:
      - equity_outcome
      - equity_baseline
    - **value**: 0.5101442454000829

### 对应的题内资料 / Expected evidence

- `updated-annual-technology-and-projects`
- `updated-annual-pit-financial-chain`
- `annual-correction-concentration-and-cash`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_operating_chain_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 300156.XSHE
  - **ticker**: 300156
  - **name_as_of**: 神雾环保
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2017-03-27
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=300156.XSHE; if_adjusted=0; baseline quarter=2016q4 and earliest info_date=2017-03-25 no later than as_of; outcome quarter=2018q4 and earliest info_date=2019-04-30; updated official annual reports control filing text and audit opinion
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **updated_2016_annual_report**: 02c8bc274ce1b02552306850b17c1d94b878858b462a7ba02ae067713e9274fd
    - **2016_annual_report_correction**: bff137021f65a6e28920c5ca002d7f10eaa99a67329bce5c9d1bc58f23f3cd23
  - **causal_guardrail**: The label measures later company-level commercial validation under a fixed hurdle, not causal attribution to the disclosed technology.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **1203202193.PDF**: 02c8bc274ce1b02552306850b17c1d94b878858b462a7ba02ae067713e9274fd
    - **1203202192.PDF**: bff137021f65a6e28920c5ca002d7f10eaa99a67329bce5c9d1bc58f23f3cd23
- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 神雾环保技术股份有限公司2018年年度报告
    - **published_at**: 2019-04-30
    - **url**: https://static.cninfo.com.cn/finalpage/2019-04-30/1206165978.PDF
    - **fields**:
      - 营业收入
      - 营业成本
      - 归属于上市公司股东的净利润
      - 经营活动产生的现金流量净额
      - 货币资金
      - 短期借款
      - 一年内到期的非流动负债
      - 归属于母公司股东权益
      - 审计意见类型
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 147be0e07406f88b797299aa4d073cc59d5c2d7262d7282c9f0c29fbe8635425
    - **later_corroboration**:
      - **title**: 神雾环保技术股份有限公司2018年年度报告（更新后）
      - **published_at**: 2019-05-30
      - **url**: https://static.cninfo.com.cn/finalpage/2019-05-30/1206320345.PDF
      - **sha256**: 82b62440a8f91f50d9e20256b53737d71d7624c339524e58d469f615cf09a31f
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2016q4/data.parquet
      - data/db/rq_income_statement_pit/quarter=2018q4/data.parquet
      - data/db/rq_balance_sheet_pit/quarter=2016q4/data.parquet
      - data/db/rq_balance_sheet_pit/quarter=2018q4/data.parquet
      - data/db/rq_cash_flow_pit/quarter=2018q4/data.parquet
    - **fields**:
      - revenue
      - cost_of_goods_sold
      - net_profit_parent_company
      - cash_flow_from_operating_activities
      - cash_equivalent
      - short_term_loans
      - non_current_liability_due_one_year
      - equity_parent_company
    - **row_policy**: stock_code=300156.XSHE; if_adjusted=0; baseline 2016q4 selected earliest info_date=2017-03-25; outcome 2018q4 selected earliest info_date=2019-04-30; later updated filing only corroborates the earliest-sufficient outcome

</details>

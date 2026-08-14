# cn-a-2025-auto-payment-cycle-600933

## Question

你处在2025-06-11收盘后的信息环境。爱柯迪客户遍布欧美与亚洲，墨西哥二期和马来西亚工厂正在扩张，2024年经营现金流充足且客户并不过度集中。预测其2025财年能否同时达到target三项门槛。请把海外本地化的订单优势与爬坡、备货、验收和应收占用同时考虑，并区分高现金收款率、高经营现金流率与应收天数下降这三个条件；不要只凭优质客户或出海故事押注。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 爱柯迪 (600933, SSE)
- 信息截止 / As of: 2025-06-11
- 预测窗口结束 / Window end: 2026-04-30
- 目标事件 / Target: `fy2025_trade_receivable_relief_and_cash_conversion`
- 判定定义 / Definition: 在2025财年，按RQData PIT未调整合并口径计算的票据及应收账款周转天数较2024财年至少缩短5天，同时销售商品、提供劳务收到的现金/营业收入不低于90%，经营活动产生的现金流量净额/营业收入不低于10%。票据及应收账款周转天数=365×(本年末与上年末bill_accts_receivable均值)/本年营业收入；三项须同时满足。该标签只描述政策生效后的经营结果，不将政策、整车厂承诺或客户关系认定为因果

#### 判定条件 / Criteria

- `trade_receivable_days_change_vs_fy2024 <= -5` — 2025财年票据及应收账款周转天数较2024财年至少缩短5天
- `cash_received_from_sales_to_revenue_fy2025 >= 0.9` — 2025财年销售商品、提供劳务收到的现金不低于营业收入的90%
- `operating_cash_flow_to_revenue_fy2025 >= 0.1` — 2025财年经营活动现金流量净额不低于营业收入的10%

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 《保障中小企业款项支付条例》：60日规则的主体边界与非现金支付约束

- Evidence ID: `payment-rule-boundary`
- 发布日期 / Published: 2025-03-24
- 来源 / Source: 工业和信息化部转载国务院令第802号
- URL: https://wap.miit.gov.cn/xwfb/gxdt/sjdt/art/2025/art_2610a93b60554b9c81d6e37c2bc8232f.html

修订条例自2025年6月1日起施行，法定60日及非现金支付约束针对大型企业采购中小企业。上市零部件集团并不自动是条例所称中小企业，不能将政策方向直接当作回款结果。

### 爱柯迪2024年报与PIT营运资金基线

- Evidence ID: `fy2024-working-capital-baseline`
- 发布日期 / Published: 2025-03-31
- 来源 / Source: 爱柯迪2024年年度报告及只读RQData PIT
- URL: https://static.cninfo.com.cn/finalpage/2025-03-31/1222962093.PDF

未调整合并口径：2023年末票据及应收账款1,861,034,872.43元，2024年末2,098,530,606.04元；2024年营业收入6,746,046,655.82元，据固定公式计算周转天数107.118天。销售商品、提供劳务收到现金7,030,968,127.36元，经营活动现金流净额1,708,759,381.59元。前五大客户销售占38.60%。

### 爱柯迪全球化产能：墨西哥二期与马来西亚工厂

- Evidence ID: `operating-chain-exposure`
- 发布日期 / Published: 2025-03-31
- 来源 / Source: 爱柯迪2024年年度报告
- URL: https://static.cninfo.com.cn/finalpage/2025-03-31/1222962093.PDF

公司客户覆盖全球大型零部件商及主机厂，墨西哥一期已全面量产、二期计划2025年投产，马来西亚厂已开始原材料和锌合金产品生产；境外资产约11.50亿元、占总资产8.06%。全球客户分散和本地化可能提升条款与订单，也会带来新基地爬坡、备货和验收占款。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `fy2025_trade_receivable_relief_and_cash_conversion`
- 结果日期 / Resolved at: 2025-12-31
- 可观察日期 / Observed at: 2026-04-30

### 实际结果 / Realized outcome

- **observations**:
  - **trade_receivables_fy2023_end**: 1861034872.43
  - **trade_receivables_fy2024_end**: 2098530606.04
  - **trade_receivables_fy2025_end**: 2681368485.66
  - **revenue_fy2024**: 6746046655.82
  - **revenue_fy2025**: 7413175929.8
  - **cash_received_from_sales_fy2025**: 7591996375.22
  - **operating_cash_flow_fy2025**: 2025088578.68
  - **trade_receivable_days_fy2024**: 107.1176552266134
  - **trade_receivable_days_fy2025**: 117.67312586344954
- **derivations**:
  - **item 1**:
    - **metric**: trade_receivable_days_change_vs_fy2024
    - **operation**: difference
    - **inputs**:
      - trade_receivable_days_fy2025
      - trade_receivable_days_fy2024
    - **value**: 10.555470636836148
  - **item 2**:
    - **metric**: cash_received_from_sales_to_revenue_fy2025
    - **operation**: ratio
    - **inputs**:
      - cash_received_from_sales_fy2025
      - revenue_fy2025
    - **value**: 1.024121975130951
  - **item 3**:
    - **metric**: operating_cash_flow_to_revenue_fy2025
    - **operation**: ratio
    - **inputs**:
      - operating_cash_flow_fy2025
      - revenue_fy2025
    - **value**: 0.2731742235523385

### 对应的题内资料 / Expected evidence

- `payment-rule-boundary`
- `fy2024-working-capital-baseline`
- `operating-chain-exposure`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_auto_payment_cycle_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600933.XSHG
  - **ticker**: 600933
  - **name_as_of**: 爱柯迪
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2025-06-11
  - **allowed_domains**:
    - cninfo.com.cn
    - szse.cn
    - miit.gov.cn
    - saicmotor.com
- **scenario_authoring**:
  - **dataset**: read-only download_rqdata/data/db
  - **tables**:
    - rq_balance_sheet_pit
    - rq_income_statement_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=600933.XSHG; if_adjusted=0; annual quarters 2023q4/2024q4/2025q4; select earliest info_date row for each statutory annual result
  - **matching_group**: auto-supplier-policy-working-capital-fy2025-v1
  - **matching_role**: hard_no_event_strong_cash
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git a8c193cdeb789d1af1d3e3b6d3323a5c9c77c7f9; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **rqdata_file_sha256**:
    - **rq_balance_sheet_pit_2023q4**: 5f27719ecb2c1931347687d0654d204f8ca38a4693a354f772f0e213c5b52125
    - **rq_balance_sheet_pit_2024q4**: dd2183175161521c553f3d45db3a8665081ac864a2dfd1395fe593c4d157cc35
    - **rq_balance_sheet_pit_2025q4**: 0f8560af410da22bd75bb0a11aa0e81d09ad60d40b6aa6da9a8690424e99ef50
    - **rq_income_statement_pit_2024q4**: f2bc40d59ade4e2f8d8943bb295c8d5936649433ee9c68a9fee10deda084555f
    - **rq_income_statement_pit_2025q4**: 1e56e955584e59de79801ceb2c9585b07624a7ba437d56406f9a2bcc7ad61f85
    - **rq_cash_flow_pit_2024q4**: 07e292df29d5b638e8bbe0874e38dff4106575baf4cbc360e6a19e8702d8a833
    - **rq_cash_flow_pit_2025q4**: da068cde580c8b37d3e3bb62ef7394fe7dc8ae4a4738113b4731792b2e42d942
  - **outcome_contract**: Fixed FY2025 three-hurdle test; annual PIT rows and official annual report are label authority; no causal attribution to policy.
  - **leakage_guard**: Only sources public by 2025-06-11 enter the corpus; FY2025 figures and annual report remain label-side only.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git a8c193cdeb789d1af1d3e3b6d3323a5c9c77c7f9
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **1222962093.PDF**: 70d6b2b600c38f1effdea8fa05498c0d15a76104d9a92c6fee12785470c2e249
    - **payment-regulation.html**: 3ee6f8b12670faadfa0b26614079752dcda0c1d77af1caccfaf18c922699af72
- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_annual_report
    - **title**: 爱柯迪股份有限公司2024年年度报告
    - **published_at**: 2025-03-31
    - **url**: https://static.cninfo.com.cn/finalpage/2025-03-31/1222962093.PDF
    - **period_end**: 2024-12-31
    - **result**: 提供2023年末、2024年末票据及应收账款与2024年度基线
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git a8c193cdeb789d1af1d3e3b6d3323a5c9c77c7f9
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 70d6b2b600c38f1effdea8fa05498c0d15a76104d9a92c6fee12785470c2e249
  - **item 2**:
    - **type**: official_annual_report
    - **title**: 爱柯迪股份有限公司2025年年度报告
    - **published_at**: 2026-04-30
    - **url**: https://static.cninfo.com.cn/finalpage/2026-04-30/1225261228.PDF
    - **period_end**: 2025-12-31
    - **result**: 现金收款率与经营现金流率过线，但应收天数增加10.555天，故整体未过线
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git a8c193cdeb789d1af1d3e3b6d3323a5c9c77c7f9
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 866b075a72a8c9151f4b2004ce0cb5bdf669194fa34bae0d9d5768eb3a9a007b

</details>

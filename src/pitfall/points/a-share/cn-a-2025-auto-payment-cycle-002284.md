# cn-a-2025-auto-payment-cycle-002284

## Question

你处在2025-06-11收盘后的信息环境。亚太股份是制动系统一级供应商，国内OEM配套占比超过90%，为整车厂零库存要求设置外库，海外销量仍较小。预测其2025财年能否同时达到target三项门槛。请把订单增长、仓储安全库存、整车厂验收结算、票据与现金回款以及电子产品放量放进同一现金转换链；不要用政策口号代替财务判断。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 亚太股份 (002284, SZSE)
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

修订条例自2025年6月1日起施行，适用于大型企业向中小企业采购后的付款，原则60日并约束强制商业汇票等变相延长账期的做法。上市供应商并不自动满足中小企业身份，政策是分析变量而不是结果。

### 亚太股份2024年报与PIT营运资金基线

- Evidence ID: `fy2024-working-capital-baseline`
- 发布日期 / Published: 2025-03-29
- 来源 / Source: 亚太股份2024年年度报告及只读RQData PIT
- URL: https://static.cninfo.com.cn/finalpage/2025-03-29/1222940048.PDF

未调整合并口径：2023年末票据及应收账款815,957,619.38元，2024年末958,214,259.91元；2024年营业收入4,260,388,741.13元，据固定公式计算周转天数75.999天。销售商品、提供劳务收到现金4,966,230,246.57元，经营活动现金流净额787,961,631.08元。

### 亚太股份OEM交付链：外库、安全库存与整车厂订单

- Evidence ID: `operating-chain-exposure`
- 发布日期 / Published: 2025-03-29
- 来源 / Source: 亚太股份2024年年度报告
- URL: https://static.cninfo.com.cn/finalpage/2025-03-29/1222940048.PDF

公司是制动系统一级供应商，进入大众、通用、本田、日产、Stellantis等采购平台；国内配套市场收入占比长期超过90%，海外销量较小。为满足整车厂零库存管理，公司在整车厂附近设置仓储点并存放安全库存，按实际需求配送。订单、验收、外库存货与结算共同决定现金转换。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `fy2025_trade_receivable_relief_and_cash_conversion`
- 结果日期 / Resolved at: 2025-12-31
- 可观察日期 / Observed at: 2026-03-31

### 实际结果 / Realized outcome

- **observations**:
  - **trade_receivables_fy2023_end**: 815957619.38
  - **trade_receivables_fy2024_end**: 958214259.91
  - **trade_receivables_fy2025_end**: 1112319959.04
  - **revenue_fy2024**: 4260388741.13
  - **revenue_fy2025**: 5607128129.86
  - **cash_received_from_sales_fy2025**: 5325511985.89
  - **operating_cash_flow_fy2025**: 1348698620.98
  - **trade_receivable_days_fy2024**: 75.99925444468849
  - **trade_receivable_days_fy2025**: 67.39144999131842
- **derivations**:
  - **item 1**:
    - **metric**: trade_receivable_days_change_vs_fy2024
    - **operation**: difference
    - **inputs**:
      - trade_receivable_days_fy2025
      - trade_receivable_days_fy2024
    - **value**: -8.607804453370065
  - **item 2**:
    - **metric**: cash_received_from_sales_to_revenue_fy2025
    - **operation**: ratio
    - **inputs**:
      - cash_received_from_sales_fy2025
      - revenue_fy2025
    - **value**: 0.9497753328534994
  - **item 3**:
    - **metric**: operating_cash_flow_to_revenue_fy2025
    - **operation**: ratio
    - **inputs**:
      - operating_cash_flow_fy2025
      - revenue_fy2025
    - **value**: 0.24053286990138295

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
  - **order_book_id**: 002284.XSHE
  - **ticker**: 002284
  - **name_as_of**: 亚太股份
  - **exchange**: SZSE
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
  - **row_policy**: stock_code=002284.XSHE; if_adjusted=0; annual quarters 2023q4/2024q4/2025q4; select earliest info_date row for each statutory annual result
  - **matching_group**: auto-supplier-policy-working-capital-fy2025-v1
  - **matching_role**: event
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
    - **1222940048.PDF**: 2b394162bb2338cd20bc43c65044d4add1c17e3c4cb265556bd5dc8e6a26ef75
    - **payment-regulation.html**: 3ee6f8b12670faadfa0b26614079752dcda0c1d77af1caccfaf18c922699af72
- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_annual_report
    - **title**: 浙江亚太机电股份有限公司2024年年度报告
    - **published_at**: 2025-03-29
    - **url**: https://static.cninfo.com.cn/finalpage/2025-03-29/1222940048.PDF
    - **period_end**: 2024-12-31
    - **result**: 提供2023年末、2024年末票据及应收账款与2024年度基线
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git a8c193cdeb789d1af1d3e3b6d3323a5c9c77c7f9
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 2b394162bb2338cd20bc43c65044d4add1c17e3c4cb265556bd5dc8e6a26ef75
  - **item 2**:
    - **type**: official_annual_report
    - **title**: 浙江亚太机电股份有限公司2025年年度报告
    - **published_at**: 2026-03-31
    - **url**: https://disc.static.szse.cn/download/disc/disk03/finalpage/2026-03-31/df1d44ba-ceac-4794-a1bc-1375aaa2d144.PDF
    - **period_end**: 2025-12-31
    - **result**: 2025年三项固定门槛全部满足
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git a8c193cdeb789d1af1d3e3b6d3323a5c9c77c7f9
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 42cbc9c80def39c15128f35bdc3bae9f802a37dc3e9c147d8d4c0756600fe841

</details>

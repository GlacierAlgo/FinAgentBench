# cn-a-2025-auto-payment-cycle-601799

## Question

你处在2025-06-11收盘后的信息环境。星宇股份为多家整车厂定制开发车灯，前五大客户销售占比较高，开发周期长并在推进海外工厂。预测其2025财年能否同时达到target三项门槛。请识别收入增长对平均应收天数的机械影响，并综合客户验收、商业票据、项目开发周期、海外产能和现金回款；即使现金收款率和经营现金流改善，也不能自动推出账期缩短。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 星宇股份 (601799, SSE)
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

修订条例自2025年6月1日起施行，法定60日及非现金支付约束针对大型企业采购中小企业。上市零部件集团并不自动是条例所称中小企业，行业政策只构成先验信息。

### 星宇股份2024年报与PIT营运资金基线

- Evidence ID: `fy2024-working-capital-baseline`
- 发布日期 / Published: 2025-03-20
- 来源 / Source: 星宇股份2024年年度报告及只读RQData PIT
- URL: https://static.cninfo.com.cn/finalpage/2025-03-20/1222846861.PDF

未调整合并口径：2023年末票据及应收账款4,398,135,694.48元，2024年末6,108,932,661.51元；2024年营业收入13,252,933,664.95元，据固定公式计算周转天数144.688天。销售商品、提供劳务收到现金12,573,403,590.98元，经营活动现金流净额909,217,268.12元。前五大客户销售占66.70%。

### 星宇车灯项目链：客户认证、同步开发与海外工厂

- Evidence ID: `operating-chain-exposure`
- 发布日期 / Published: 2025-03-20
- 来源 / Source: 星宇股份2024年年度报告
- URL: https://static.cninfo.com.cn/finalpage/2025-03-20/1222846861.PDF

车灯须经过整车厂认证、同步设计、模具和样件、OTS、试生产、PPAP后才批量供货，开发周期长且客户集中。公司计划稳定提升海外工厂效能。项目节点和验收可使收入、票据与应收在年末错位，因此需看固定公式而非单项现金流。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `fy2025_trade_receivable_relief_and_cash_conversion`
- 结果日期 / Resolved at: 2025-12-31
- 可观察日期 / Observed at: 2026-03-20

### 实际结果 / Realized outcome

- **observations**:
  - **trade_receivables_fy2023_end**: 4398135694.48
  - **trade_receivables_fy2024_end**: 6108932661.51
  - **trade_receivables_fy2025_end**: 7149613898.47
  - **revenue_fy2024**: 13252933664.95
  - **revenue_fy2025**: 15256665866.59
  - **cash_received_from_sales_fy2025**: 15430078996.46
  - **operating_cash_flow_fy2025**: 2436690466.04
  - **trade_receivable_days_fy2024**: 144.6879629405743
  - **trade_receivable_days_fy2025**: 158.5985279060956
- **derivations**:
  - **item 1**:
    - **metric**: trade_receivable_days_change_vs_fy2024
    - **operation**: difference
    - **inputs**:
      - trade_receivable_days_fy2025
      - trade_receivable_days_fy2024
    - **value**: 13.910564965521303
  - **item 2**:
    - **metric**: cash_received_from_sales_to_revenue_fy2025
    - **operation**: ratio
    - **inputs**:
      - cash_received_from_sales_fy2025
      - revenue_fy2025
    - **value**: 1.0113663844634462
  - **item 3**:
    - **metric**: operating_cash_flow_to_revenue_fy2025
    - **operation**: ratio
    - **inputs**:
      - operating_cash_flow_fy2025
      - revenue_fy2025
    - **value**: 0.1597131697939336

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
  - **order_book_id**: 601799.XSHG
  - **ticker**: 601799
  - **name_as_of**: 星宇股份
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
  - **row_policy**: stock_code=601799.XSHG; if_adjusted=0; annual quarters 2023q4/2024q4/2025q4; select earliest info_date row for each statutory annual result
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
    - **1222846861.PDF**: 0f4e6950ea514f7a16a5817d9541d4d7006337206af6e44bf99cf74c690a55fe
    - **payment-regulation.html**: 3ee6f8b12670faadfa0b26614079752dcda0c1d77af1caccfaf18c922699af72
- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_annual_report
    - **title**: 常州星宇车灯股份有限公司2024年年度报告
    - **published_at**: 2025-03-20
    - **url**: https://static.cninfo.com.cn/finalpage/2025-03-20/1222846861.PDF
    - **period_end**: 2024-12-31
    - **result**: 提供2023年末、2024年末票据及应收账款与2024年度基线
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git a8c193cdeb789d1af1d3e3b6d3323a5c9c77c7f9
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 0f4e6950ea514f7a16a5817d9541d4d7006337206af6e44bf99cf74c690a55fe
  - **item 2**:
    - **type**: official_annual_report
    - **title**: 常州星宇车灯股份有限公司2025年年度报告
    - **published_at**: 2026-03-20
    - **url**: https://static.cninfo.com.cn/finalpage/2026-03-20/1225018561.PDF
    - **period_end**: 2025-12-31
    - **result**: 现金收款率与经营现金流率过线，但应收天数增加13.911天，故整体未过线
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git a8c193cdeb789d1af1d3e3b6d3323a5c9c77c7f9
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: fb08f605a1a3c5f56cd9ec8cc9c00b8bc2b9be13d21c64ca2e2c69af0d0bb012

</details>

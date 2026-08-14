# cn-a-2025-auto-payment-cycle-000700

## Question

你处在2025-06-11收盘后的信息环境。模塑科技为多家豪华品牌和新能源整车厂供应外饰件，前五大客户集中度较高，墨西哥工厂又使海外资产、在途库存与本地交付进入现金周期。预测其2025财年能否同时达到target三项门槛。请判断2024年应收下降是否可持续，并综合客户议价、收入变化、海外扩产、票据与现金回款；不要把政策或出海叙事直接当成结果。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 模塑科技 (000700, SZSE)
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

修订条例自2025年6月1日起施行，适用于机关、事业单位和大型企业采购中小企业货物、工程、服务的付款。大型企业原则上应自交付之日起60日内向中小企业付款；不得强制接受商业汇票、应收账款电子凭证，亦不得用其变相延长账期。上市供应商是否属于合同订立时的中小企业须另行判断，政策方向不是结果标签。

### 模塑科技2024年报与PIT营运资金基线

- Evidence ID: `fy2024-working-capital-baseline`
- 发布日期 / Published: 2025-04-29
- 来源 / Source: 模塑科技2024年年度报告及只读RQData PIT
- URL: https://disc.static.szse.cn/download/disc/disk03/finalpage/2025-04-28/ff677756-c8c1-423f-ab23-8f89d9310cef.PDF

未调整合并口径：2023年末票据及应收账款2,034,881,978.20元，2024年末1,288,709,886.94元；2024年营业收入7,136,130,278.47元，据固定公式计算周转天数84.998天。销售商品、提供劳务收到现金7,107,275,669.42元，经营活动现金流净额1,206,053,623.53元。前五大客户销售占59.56%，关联方销售占4.80%。

### 模塑科技客户与墨西哥产能：从出口转向产能输出

- Evidence ID: `operating-chain-exposure`
- 发布日期 / Published: 2025-04-29
- 来源 / Source: 模塑科技2024年年度报告
- URL: https://disc.static.szse.cn/download/disc/disk03/finalpage/2025-04-28/ff677756-c8c1-423f-ab23-8f89d9310cef.PDF

公司为宝马、北京奔驰、上汽奥迪、上汽通用、上汽大众及多家新能源车企供应外饰件，强调由产品出口转向产能输出。墨西哥名华资产约20.90亿元、占公司净资产52.06%，海外工厂带来本地交付优势，也使产能、备货、文化与运营管理进入现金周期。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `fy2025_trade_receivable_relief_and_cash_conversion`
- 结果日期 / Resolved at: 2025-12-31
- 可观察日期 / Observed at: 2026-04-29

### 实际结果 / Realized outcome

- **observations**:
  - **trade_receivables_fy2023_end**: 2034881978.2
  - **trade_receivables_fy2024_end**: 1288709886.94
  - **trade_receivables_fy2025_end**: 1331048268.37
  - **revenue_fy2024**: 7136130278.47
  - **revenue_fy2025**: 7108021024.76
  - **cash_received_from_sales_fy2025**: 6574454268.3
  - **operating_cash_flow_fy2025**: 845789046.4
  - **trade_receivable_days_fy2024**: 84.99781978729467
  - **trade_receivable_days_fy2025**: 67.26286566663863
- **derivations**:
  - **item 1**:
    - **metric**: trade_receivable_days_change_vs_fy2024
    - **operation**: difference
    - **inputs**:
      - trade_receivable_days_fy2025
      - trade_receivable_days_fy2024
    - **value**: -17.73495412065604
  - **item 2**:
    - **metric**: cash_received_from_sales_to_revenue_fy2025
    - **operation**: ratio
    - **inputs**:
      - cash_received_from_sales_fy2025
      - revenue_fy2025
    - **value**: 0.9249345556799312
  - **item 3**:
    - **metric**: operating_cash_flow_to_revenue_fy2025
    - **operation**: ratio
    - **inputs**:
      - operating_cash_flow_fy2025
      - revenue_fy2025
    - **value**: 0.11899079131220743

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
  - **order_book_id**: 000700.XSHE
  - **ticker**: 000700
  - **name_as_of**: 模塑科技
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
  - **row_policy**: stock_code=000700.XSHE; if_adjusted=0; annual quarters 2023q4/2024q4/2025q4; select earliest info_date row for each statutory annual result
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
    - **ff677756-c8c1-423f-ab23-8f89d9310cef.PDF**: 16fe34809972098761d32baaed82a6546423f23e23c87fb8b2c19c40e44a673e
    - **payment-regulation.html**: 3ee6f8b12670faadfa0b26614079752dcda0c1d77af1caccfaf18c922699af72
- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_annual_report
    - **title**: 江南模塑科技股份有限公司2024年年度报告
    - **published_at**: 2025-04-29
    - **url**: https://disc.static.szse.cn/download/disc/disk03/finalpage/2025-04-28/ff677756-c8c1-423f-ab23-8f89d9310cef.PDF
    - **period_end**: 2024-12-31
    - **result**: 提供2023年末、2024年末票据及应收账款与2024年度基线
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git a8c193cdeb789d1af1d3e3b6d3323a5c9c77c7f9
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 16fe34809972098761d32baaed82a6546423f23e23c87fb8b2c19c40e44a673e
  - **item 2**:
    - **type**: official_annual_report
    - **title**: 江南模塑科技股份有限公司2025年年度报告
    - **published_at**: 2026-04-29
    - **url**: https://disc.static.szse.cn/download/disc/disk03/finalpage/2026-04-29/553fa980-b493-421f-a61e-a2af68c116e2.PDF
    - **period_end**: 2025-12-31
    - **result**: 2025年三项固定门槛全部满足
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git a8c193cdeb789d1af1d3e3b6d3323a5c9c77c7f9
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: b6390a1be55fa94076ab7d1ce9bdf8c92573d860bb9dc31d434ecf0ceb036883

</details>

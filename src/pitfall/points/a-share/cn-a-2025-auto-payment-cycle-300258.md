# cn-a-2025-auto-payment-cycle-300258

## Question

你处在2025-06-11收盘后的信息环境。精锻科技出口收入接近30%，计划让泰国工厂在2025年进入试产和批量供货，前五大客户占比较高。预测其2025财年能否同时达到target三项门槛。请综合出口替代、海外产能爬坡、客户验收与备货、汇率、票据回款和原有高经营现金流；不要把海外扩张简单等同于更快回款。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 精锻科技 (300258, SZSE)
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

修订条例自2025年6月1日起施行，适用于大型企业向中小企业采购后的付款，原则60日并约束强制商业汇票等变相延长账期的做法。供应商规模身份与合同条件必须单独核实，政策并不保证上市供应商应收下降。

### 精锻科技2024年报与PIT营运资金基线

- Evidence ID: `fy2024-working-capital-baseline`
- 发布日期 / Published: 2025-04-19
- 来源 / Source: 精锻科技2024年年度报告及只读RQData PIT
- URL: https://static.cninfo.com.cn/finalpage/2025-04-19/1223153202.PDF

未调整合并口径：2023年末票据及应收账款535,370,190.32元，2024年末542,777,287.10元；2024年营业收入2,025,226,020.56元，据固定公式计算周转天数97.156天。销售商品、提供劳务收到现金1,979,334,639.64元，经营活动现金流净额541,560,734.78元。前五大客户销售占49.54%。

### 精锻科技出海链：近30%出口、泰国产能与客户本地化

- Evidence ID: `operating-chain-exposure`
- 发布日期 / Published: 2025-04-19
- 来源 / Source: 精锻科技2024年年度报告
- URL: https://static.cninfo.com.cn/finalpage/2025-04-19/1223153202.PDF

公司披露出口收入接近总收入30%、北美直接出口接近8%，计划泰国工厂2025年6月小批试产、下半年批量供货，并规划北非基地。属地化可响应供应链多元化，但产能爬坡、备货、贸易争端和汇率会同时影响应收与现金。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `fy2025_trade_receivable_relief_and_cash_conversion`
- 结果日期 / Resolved at: 2025-12-31
- 可观察日期 / Observed at: 2026-04-21

### 实际结果 / Realized outcome

- **observations**:
  - **trade_receivables_fy2023_end**: 535370190.32
  - **trade_receivables_fy2024_end**: 542777287.1
  - **trade_receivables_fy2025_end**: 444989897.45
  - **revenue_fy2024**: 2025226020.56
  - **revenue_fy2025**: 2038654724.57
  - **cash_received_from_sales_fy2025**: 1989780647
  - **operating_cash_flow_fy2025**: 471359175.23
  - **trade_receivable_days_fy2024**: 97.15553357088653
  - **trade_receivable_days_fy2025**: 88.42473863169627
- **derivations**:
  - **item 1**:
    - **metric**: trade_receivable_days_change_vs_fy2024
    - **operation**: difference
    - **inputs**:
      - trade_receivable_days_fy2025
      - trade_receivable_days_fy2024
    - **value**: -8.730794939190261
  - **item 2**:
    - **metric**: cash_received_from_sales_to_revenue_fy2025
    - **operation**: ratio
    - **inputs**:
      - cash_received_from_sales_fy2025
      - revenue_fy2025
    - **value**: 0.9760263094181832
  - **item 3**:
    - **metric**: operating_cash_flow_to_revenue_fy2025
    - **operation**: ratio
    - **inputs**:
      - operating_cash_flow_fy2025
      - revenue_fy2025
    - **value**: 0.23121089096115613

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
  - **order_book_id**: 300258.XSHE
  - **ticker**: 300258
  - **name_as_of**: 精锻科技
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
  - **row_policy**: stock_code=300258.XSHE; if_adjusted=0; annual quarters 2023q4/2024q4/2025q4; select earliest info_date row for each statutory annual result
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
    - **1223153202.PDF**: bf960d40183ceab3ba9dce54b1d3b6987d4a35c36036446cc7729c8e83debaa7
    - **payment-regulation.html**: 3ee6f8b12670faadfa0b26614079752dcda0c1d77af1caccfaf18c922699af72
- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_annual_report
    - **title**: 江苏太平洋精锻科技股份有限公司2024年年度报告
    - **published_at**: 2025-04-19
    - **url**: https://static.cninfo.com.cn/finalpage/2025-04-19/1223153202.PDF
    - **period_end**: 2024-12-31
    - **result**: 提供2023年末、2024年末票据及应收账款与2024年度基线
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git a8c193cdeb789d1af1d3e3b6d3323a5c9c77c7f9
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: bf960d40183ceab3ba9dce54b1d3b6987d4a35c36036446cc7729c8e83debaa7
  - **item 2**:
    - **type**: official_annual_report
    - **title**: 江苏太平洋精锻科技股份有限公司2025年年度报告
    - **published_at**: 2026-04-21
    - **url**: https://disc.static.szse.cn/download/disc/disk03/finalpage/2026-04-21/cbad005e-4b6e-4d8c-8186-94aaf8485408.PDF
    - **period_end**: 2025-12-31
    - **result**: 2025年三项固定门槛全部满足
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git a8c193cdeb789d1af1d3e3b6d3323a5c9c77c7f9
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 5c62227d0fa55c69140ffd6c191a260c59b3d154cd84435dcd6cee32670d1f0c

</details>

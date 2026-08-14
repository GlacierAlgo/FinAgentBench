# cn-a-2025-auto-payment-cycle-600741

## Question

你处在2025-06-11收盘后的信息环境。华域汽车由上汽体系控制，2024年关联客户销售占比较高，但来自上汽以外整车客户的主营收入已占62.2%；同日上汽又公开承诺将供应商支付账期统一至60天内并减少商业承兑汇票。预测华域2025财年能否同时达到target三项门槛。请先判断上市公司华域是否当然属于条例保护的中小企业，再区分集团承诺、关联交易议价、收入增长、应收票据/账款、应收款项融资和真实现金回款；不要把“上汽小弟”或60天承诺直接翻译为标签。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 华域汽车 (600741, SSE)
- 信息截止 / As of: 2025-06-11
- 预测窗口结束 / Window end: 2026-04-30
- 目标事件 / Target: `fy2025_trade_receivable_relief_and_cash_conversion`
- 判定定义 / Definition: 在2025财年，按RQData PIT未调整合并口径计算的票据及应收账款周转天数较2024财年至少缩短5天，同时销售商品、提供劳务收到的现金/营业收入不低于90%，经营活动产生的现金流量净额/营业收入不低于10%。票据及应收账款周转天数=365×(本年末与上年末bill_accts_receivable均值)/本年营业收入；三项须同时满足。该标签只描述政策生效后的经营结果，不将政策、整车厂承诺或客户关系认定为因果

#### 判定条件 / Criteria

- `trade_receivable_days_change_vs_fy2024 <= -5` — 2025财年票据及应收账款周转天数较2024财年至少缩短5天
- `cash_received_from_sales_to_revenue_fy2025 >= 0.9` — 2025财年销售商品、提供劳务收到的现金不低于营业收入的90%
- `operating_cash_flow_to_revenue_fy2025 >= 0.1` — 2025财年经营活动现金流量净额不低于营业收入的10%

<details>
<summary>冻结资料 / Frozen evidence (4)</summary>

### 《保障中小企业款项支付条例》：60日规则的主体边界与非现金支付约束

- Evidence ID: `payment-rule-boundary`
- 发布日期 / Published: 2025-03-24
- 来源 / Source: 工业和信息化部转载国务院令第802号
- URL: https://wap.miit.gov.cn/xwfb/gxdt/sjdt/art/2025/art_2610a93b60554b9c81d6e37c2bc8232f.html

修订条例自2025年6月1日起施行。法定60日规则针对大型企业采购中小企业的交易，并限制强制商业汇票、应收账款电子凭证等变相延长账期。华域是大型上市零部件集团，不能仅因其向整车厂供货便假设自身属于条例保护的中小企业。

### 上汽集团承诺供应商支付账期统一至60天内

- Evidence ID: `saic-60-day-commitment`
- 发布日期 / Published: 2025-06-11
- 来源 / Source: 上海汽车集团股份有限公司官方网站
- URL: https://www.saicmotor.com/chinese/xwzx/xwk/2025/61888.shtml

上汽集团宣布将供应商支付账期统一至60天内，并且不采用商业承兑汇票等增加供应商资金压力的结算方式。该表态比条例的中小企业边界更宽，但题目仍以华域自身2025财年法定财务结果裁决，不预设承诺必然、立即或完整传导至所有关联交易。

### 华域汽车2024年报与PIT营运资金基线

- Evidence ID: `fy2024-working-capital-baseline`
- 发布日期 / Published: 2025-04-29
- 来源 / Source: 华域汽车2024年年度报告及只读RQData PIT
- URL: https://static.cninfo.com.cn/finalpage/2025-04-29/1223375149.PDF

未调整合并口径：2023年末票据及应收账款40,011,036,602.90元，2024年末46,550,434,734.75元；2024年营业收入168,852,183,839.32元，据固定公式计算周转天数93.558天。销售商品、提供劳务收到现金141,284,424,242.93元，经营活动现金流净额8,139,847,784.94元。前五大客户销售占42.18%，其中关联方占25.13%。

### 华域汽车客户结构：上汽关联与业外客户并存

- Evidence ID: `operating-chain-exposure`
- 发布日期 / Published: 2025-04-29
- 来源 / Source: 华域汽车2024年年度报告
- URL: https://static.cninfo.com.cn/finalpage/2025-04-29/1223375149.PDF

按含海外业务的汇总口径，公司主营业务收入62.2%来自上汽集团以外整车客户；公司同时提示整车竞争会把降价和回款压力传导给零部件企业。关联关系可能降低信用风险或协同成本，但也可能反映集团结算安排，不能等同于更短账期。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `fy2025_trade_receivable_relief_and_cash_conversion`
- 结果日期 / Resolved at: 2025-12-31
- 可观察日期 / Observed at: 2026-03-31

### 实际结果 / Realized outcome

- **observations**:
  - **trade_receivables_fy2023_end**: 40011036602.9
  - **trade_receivables_fy2024_end**: 46550434734.75
  - **trade_receivables_fy2025_end**: 52495031137.88
  - **revenue_fy2024**: 168852183839.32
  - **revenue_fy2025**: 183998900513.66
  - **cash_received_from_sales_fy2025**: 142711338667.94
  - **operating_cash_flow_fy2025**: 9523102797.47
  - **trade_receivable_days_fy2024**: 93.55797573902875
  - **trade_receivable_days_fy2025**: 98.23861703137209
- **derivations**:
  - **item 1**:
    - **metric**: trade_receivable_days_change_vs_fy2024
    - **operation**: difference
    - **inputs**:
      - trade_receivable_days_fy2025
      - trade_receivable_days_fy2024
    - **value**: 4.6806412923433385
  - **item 2**:
    - **metric**: cash_received_from_sales_to_revenue_fy2025
    - **operation**: ratio
    - **inputs**:
      - cash_received_from_sales_fy2025
      - revenue_fy2025
    - **value**: 0.7756097360883152
  - **item 3**:
    - **metric**: operating_cash_flow_to_revenue_fy2025
    - **operation**: ratio
    - **inputs**:
      - operating_cash_flow_fy2025
      - revenue_fy2025
    - **value**: 0.051756302732705775

### 对应的题内资料 / Expected evidence

- `payment-rule-boundary`
- `saic-60-day-commitment`
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
  - **order_book_id**: 600741.XSHG
  - **ticker**: 600741
  - **name_as_of**: 华域汽车
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
  - **row_policy**: stock_code=600741.XSHG; if_adjusted=0; annual quarters 2023q4/2024q4/2025q4; select earliest info_date row for each statutory annual result
  - **matching_group**: auto-supplier-policy-working-capital-fy2025-v1
  - **matching_role**: hard_no_event_policy_affiliation
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
    - **1223375149.PDF**: 0e6c40acb8919acef249e2ce3520ff7c7bba00f524e8ccff34d1d58f88f996c8
    - **payment-regulation.html**: 3ee6f8b12670faadfa0b26614079752dcda0c1d77af1caccfaf18c922699af72
    - **saic-60day.html**: 6971c580bcc4c4af5783284151e62860f864d586924bd4d94eca71785e5cc5d2
- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_annual_report
    - **title**: 华域汽车系统股份有限公司2024年年度报告
    - **published_at**: 2025-04-29
    - **url**: https://static.cninfo.com.cn/finalpage/2025-04-29/1223375149.PDF
    - **period_end**: 2024-12-31
    - **result**: 提供2023年末、2024年末票据及应收账款与2024年度基线
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git a8c193cdeb789d1af1d3e3b6d3323a5c9c77c7f9
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 0e6c40acb8919acef249e2ce3520ff7c7bba00f524e8ccff34d1d58f88f996c8
  - **item 2**:
    - **type**: official_annual_report
    - **title**: 华域汽车系统股份有限公司2025年年度报告
    - **published_at**: 2026-03-31
    - **url**: https://static.cninfo.com.cn/finalpage/2026-03-31/1225052214.PDF
    - **period_end**: 2025-12-31
    - **result**: 应收天数上升4.681天，现金收款率77.56%、经营现金流率5.18%，三项均未过线
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git a8c193cdeb789d1af1d3e3b6d3323a5c9c77c7f9
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 19d879f380cc042f4f5d91cb952c939f95b4e953366e8045da1e3a58760065f4

</details>

# cn-a-2022-game-segment-divestiture-24m-002306

## Question

你处在2022-03-18收盘后的信息环境。中科云网的互联网游戏推广及运营收入主要来自2020年收购的重庆微音，已成为公司重要业务组成。请使用冻结材料，预测未来24个月内是否会发生target定义的重大游戏板块剥离。评估该业务的收入贡献、盈利与现金质量、收购后的整合稳定性、对单一子公司的依赖、公司既往频繁调整业务边界以及潜在的新业务资本需求；不得因为公司历史改名或管理层评价直接给出标签，也不要使用未来光伏转型或股权出售结果。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 中科云网 (002306, SZSE)
- 信息截止 / As of: 2022-03-18
- 预测窗口结束 / Window end: 2024-03-18
- 目标事件 / Target: `material_game_segment_divestiture_24m`
- 判定定义 / Definition: 未来24个月内，公司将截至快照日贡献至少50%合并收入的核心游戏运营子公司全部股权转让给非合并范围主体并完成控制权交割，使该子公司退出合并报表范围。只披露转让意向、董事会预案、少数股权出售、业务自然萎缩或仍受公司控制的内部重组不计

#### 判定条件 / Criteria

- `material_game_segment_divestiture_count_24m >= 1` — 窗口内至少一次完成100%游戏子公司控制权转让并退出合并范围

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 2020年年报问询回复：收购重庆微音后游戏收入占公司六成以上

- Evidence ID: `game-acquisition-and-2020-revenue-concentration`
- 发布日期 / Published: 2021-04-06
- 来源 / Source: 巨潮资讯交易所问询回复
- URL: https://static.cninfo.com.cn/finalpage/2021-04-06/1209637823.PDF

公司于2020年7月收购重庆微音100%股权，进入互联网游戏推广及运营业务。该业务2020年实现收入172,435,553.39元，占公司营业收入63.24%，意味着游戏板块在收购当年即成为最重要的收入来源之一。高度集中既说明短期战略重要性，也意味着单一子公司经营和渠道变化会显著影响公司整体业务结构。

### 2021年半年报：游戏推广及运营继续构成主要业务

- Evidence ID: `h1-2021-game-operation-update`
- 发布日期 / Published: 2021-08-18
- 来源 / Source: 巨潮资讯法定半年度报告
- URL: https://static.cninfo.com.cn/finalpage/2021-08-18/1210768962.PDF

半年报继续将互联网游戏推广及运营列为主要经营板块，并由重庆微音承载。预测未来是否出售时，应同时看到这一业务已形成现实收入贡献，以及公司的业务组合长期经历餐饮资产剥离、新媒体尝试、团膳收缩和新板块进入；历史调整只能作为资本配置行为证据，不能直接替代未来交易标签。

### 2021年年度报告摘要：游戏板块收入约2.16亿元

- Evidence ID: `annual-2021-game-revenue-materiality`
- 发布日期 / Published: 2022-03-18
- 来源 / Source: 巨潮资讯法定年度报告摘要
- URL: https://static.cninfo.com.cn/finalpage/2022-03-18/1212610197.PDF

公司2021年互联网游戏推广及运营业务收入约216,291,400元，继续构成重要收入来源。业务的收入规模提高了立即出售的机会成本，但是否能形成稳定利润和现金、渠道依赖是否可持续、公司未来是否需要为其他转型回收资本，仍是预测24个月内控制权交易的核心变量。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `material_game_segment_divestiture_24m`
- 结果日期 / Resolved at: 2023-09-01
- 可观察日期 / Observed at: 2024-04-30

### 实际结果 / Realized outcome

- **observations**:
  - **material_game_segment_divestiture_count_24m**: 1
  - **ownership_interest_sold**: 1
  - **subsidiary_exited_consolidation**: 1
  - **game_revenue_share_at_as_of**: 0.6324
  - **calendar_days_from_as_of_to_deconsolidation**: 532
- **derivations**:


### 对应的题内资料 / Expected evidence

- `game-acquisition-and-2020-revenue-concentration`
- `h1-2021-game-operation-update`
- `annual-2021-game-revenue-materiality`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_segment_exit_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002306.XSHE
  - **ticker**: 002306
  - **name_as_of**: 中科云网
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2022-03-18
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=002306.XSHE; if_adjusted=0; financial facts limited to info_date<=2022-03-18; subsidiary scope and deconsolidation adjudicated from issuer filings
  - **matching_group**: material-controlled-segment-divestiture-24m-v1
  - **matching_role**: event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2020_annual_inquiry_response**: 53cc1772976f2cd1dd82c55985cd3cb692b1b2590b0f5fa486e1d3b2410cb879
    - **2021_half_year_report**: 1769fe51ce58f0d6ec059d9beb2fb90eae27610c5d9dc5fc4bfe5829d69d9b95
    - **2021_annual_report_summary**: 11be8fa4a215ec9abd6c9f4f7a64fa3817948e06b728341cfb2a39468234de40
    - **2023_game_sale_notice**: 46fbd462e8880f110f482c93a08bf79f104e6882172e7cbc4f1f78884aab6f49
    - **2023_annual_report**: 8654d50e1eed933e20421258d2fb216227a1cd41e1160099fccda3e2347560dd
  - **outcome_contract**: A sale counts only after the wholly owned game subsidiary transfers outside the group and is confirmed to leave consolidation within 24 calendar months.
  - **leakage_guard**: The later photovoltaic pivot, proposed sale, shareholder approval, closing and 2023 annual-report confirmation remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_transaction_notice
    - **title**: 关于出售全资子公司100%股权的公告
    - **published_at**: 2023-08-16
    - **url**: https://static.cninfo.com.cn/finalpage/2023-08-16/1217545408.PDF
    - **subsidiary**: 重庆微音
    - **ownership_sold**: 1
    - **result**: 董事会于2023-08-15审议通过出售100%股权，尚待股东大会批准
  - **item 2**:
    - **type**: official_shareholder_resolution
    - **title**: 中科云网科技集团股份有限公司2023年第五次临时股东大会决议公告
    - **published_at**: 2023-09-01
    - **meeting_at**: 2023-08-31
    - **url**: https://static.cninfo.com.cn/finalpage/2023-09-01/1217735550.PDF
    - **result**: 股东大会审议通过出售重庆微音100%股权
  - **item 3**:
    - **type**: official_annual_report
    - **title**: 中科云网科技集团股份有限公司2023年年度报告
    - **published_at**: 2024-04-30
    - **url**: https://static.cninfo.com.cn/finalpage/2024-04-30/1219923026.PDF
    - **effective_at**: 2023-09-01
    - **result**: 年报确认重庆微音自2023年9月起不再纳入合并报表范围

</details>

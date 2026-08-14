# cn-a-2023-battery-operation-24m-002306

## Question

你处在2023-06-30收盘后的信息环境。中科云网已宣布跨界建设5GW N型TOPCon电池项目并签署逾亿元设备采购合同。请使用冻结材料，预测未来24个月内其受控自有电池片产线能否达到target定义的正式运营。重点检验公司现金与项目资本开支的量级差、项目公司资本金、设备合同只是采购里程碑、厂房和配套建设、团队与技术、爬坡良率、订单兑现方式。不要把光伏行业收入、组件/边框销售、贸易收入、委外加工或租线出货误当作自有电池片产线投产。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 中科云网 (002306, SZSE)
- 信息截止 / As of: 2023-06-30
- 预测窗口结束 / Window end: 2025-06-30
- 目标事件 / Target: `own_battery_cell_line_formal_operation_24m`
- 判定定义 / Definition: 经营事实截止日固定为项目投资或关键设备采购公告后24个自然月；截至该日，公司控制的自有N型TOPCon电池片生产线已经正式投产，且法定报告确认该自有产线产生实际电池片产量或销售收入。设备采购、到货、安装、调试、试生产或产能规划本身不计；通过外部委托加工、租赁产线、贸易、组件或边框业务完成交付也不计为自有电池片产线正式运营

#### 判定条件 / Criteria

- `own_battery_cell_line_formal_operation_count_24m >= 1` — 窗口内至少一条受控自有电池片生产线同时满足正式投产与实际自产产销披露

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 光伏跨界问询回复：5GW规划、首期出资与现金规模

- Evidence ID: `pv-inquiry-5gw-capital-gap`
- 发布日期 / Published: 2022-12-01
- 来源 / Source: 巨潮资讯交易所问询回复
- URL: https://static.cninfo.com.cn/finalpage/2022-12-01/1215242085.PDF

公司披露与同翎新能源合作进入N型TOPCon电池研发和生产制造，规划建设5GW产能；公司拟对项目公司首期投入4,200万元，而2022年三季度末可支配货币资金约8,500万元。回复列示了资金来源、项目经验与审批风险，也表明拟建制造产能与当时公司的资金体量存在明显差距，后续融资、厂房设备、技术与量产爬坡均是独立执行环节。

### 中科高邮增资公告：引入资金推进电池片项目

- Evidence ID: `project-company-capital-increase-2023`
- 发布日期 / Published: 2023-06-29
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2023-06-29/1217157012.PDF

公司披露对控股项目公司中科高邮实施增资并引入相关投资安排，以推进N型高效太阳能电池片项目。资本金到位是项目建设的重要条件，但公告中的股权和出资安排不等于厂房建成、设备联调、良率达标或自有产线形成商业产出。

### 中科高邮设备采购合同：合同总额1.065962亿元，尚非投产证明

- Evidence ID: `equipment-contracts-not-production`
- 发布日期 / Published: 2023-06-30
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2023-06-30/1217169939.PDF

控股子公司中科高邮签署光伏电池自动化设备采购合同，合同金额合计106,596,200元。采购合同显示项目进入设备投入阶段，但设备仍需交付、安装、调试并与厂房、公辅系统和工艺团队配套；公告不能单独证明生产线将在固定期限内正式投产，更不能证明未来收入来自自有产线而非委外、租线或贸易。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `own_battery_cell_line_formal_operation_24m`
- 结果日期 / Resolved at: 2025-06-30
- 可观察日期 / Observed at: 2025-08-27

### 实际结果 / Realized outcome

- **observations**:
  - **own_battery_cell_line_formal_operation_count_24m**: 0
  - **installed_or_commissioning_line_count_at_window_end**: 2
  - **formal_operation_confirmed_at_window_end**: 0
  - **outsourced_or_rented_line_delivery_mode_disclosed**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `pv-inquiry-5gw-capital-gap`
- `project-company-capital-increase-2023`
- `equipment-contracts-not-production`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_project_operation_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002306.XSHE
  - **ticker**: 002306
  - **name_as_of**: 中科云网
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2023-06-30
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_balance_sheet_pit
    - rq_income_statement_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=002306.XSHE; if_adjusted=0; financial rows limited to info_date<=2023-06-30; project milestones adjudicated from issuer filings
  - **matching_group**: cross-industry-owned-production-line-formal-operation-24m-v1
  - **matching_role**: no_event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2022_pv_inquiry_response**: 7b36a68de76b60ce361de49742d6f4ee4c3febcc246e4a70efbe322fd96d1ff8
    - **2023_project_company_capital_notice**: ad2098e932d93a9840f473eb1e49f398111a5f7634312c8075e0bdc9965bcbc6
    - **2023_equipment_contract_notice**: 9030d56fe6b9e551b27bb4630b702eccfc7c6fb99deebe809c1aa4bbc520196b
    - **2025_half_year_report**: 3e76399fccc40a947c0a1343d16a88572437df78563bb28a3717ac17d7b220d7
  - **outcome_contract**: Formal operation must exist by the fixed 2025-06-30 operating cutoff and requires the first statutory report covering that cutoff to confirm an owned-line production milestone plus actual self-manufactured battery-cell output or revenue; outsourced, rented-line and trading deliveries are excluded.
  - **leakage_guard**: Construction progress, later installation/commissioning, outsourcing disclosures, 2024 losses and 2025 risk-warning status remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_periodic_report
    - **title**: 中科云网科技集团股份有限公司2025年半年度报告
    - **published_at**: 2025-08-27
    - **url**: https://static.cninfo.com.cn/finalpage/2025-08-27/1224584470.PDF
    - **period_end**: 2025-06-30
    - **result**: 两条电池片生产线已进场安装调试但暂未投产；订单主要通过委托加工及租赁产线交付，因此不满足自有产线正式运营口径

</details>

# cn-a-2022-battery-operation-24m-002634

## Question

你处在2022-12-09收盘后的信息环境。棒杰股份原有核心业务为无缝服装，现宣布投资约26亿元建设扬州10GW高效光伏电池片项目，其中设备投资约16亿元、项目公司注册资本5亿元。请使用冻结材料，预测未来24个月内其受控自有电池片产线能否达到target定义的正式运营。重点比较公司现金、经营现金流和项目投资量级，拆解项目公司资本金、租赁厂房、设备与公辅系统、跨界团队和技术、客户开拓、良率爬坡及价格周期等环节。不要把签约、资金安排、设备到货、调试、试生产，或贸易、组件、委外及租线出货误当作自有电池片产线正式投产。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 棒杰股份 (002634, SZSE)
- 信息截止 / As of: 2022-12-09
- 预测窗口结束 / Window end: 2024-12-09
- 目标事件 / Target: `own_battery_cell_line_formal_operation_24m`
- 判定定义 / Definition: 经营事实截止日固定为项目投资或关键设备采购公告后24个自然月；截至该日，公司控制的自有N型TOPCon电池片生产线已经正式投产，且法定报告确认该自有产线产生实际电池片产量或销售收入。设备采购、到货、安装、调试、试生产或产能规划本身不计；通过外部委托加工、租赁产线、贸易、组件或边框业务完成交付也不计为自有电池片产线正式运营

#### 判定条件 / Criteria

- `own_battery_cell_line_formal_operation_count_24m >= 1` — 窗口内至少一条受控自有电池片生产线同时满足正式投产与实际自产产销披露

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 棒杰股份2022年三季报PIT财务基线：存量服装经营与项目资金量级

- Evidence ID: `q3-2022-pit-capital-base`
- 发布日期 / Published: 2022-10-26
- 来源 / Source: 棒杰股份法定季度报告及只读RQData点时记录
- URL: https://static.cninfo.com.cn/finalpage/2022-10-26/1214901309.PDF

2022年前三季度营业收入497,238,184.88元、归母净利润61,461,388.68元、经营活动现金流净额26,847,548.03元；9月末货币资金190,790,422.42元、总资产1,121,200,723.86元、短期借款60,000,000.00元。购建固定资产、无形资产和其他长期资产支付现金32,006,640.79元。点时口径为002634.XSHE、2022q3、if_adjusted=0、截至as_of最新info_date=2022-10-26。该基线反映项目宣布前公司的现实融资与执行能力，而非后来光伏产线结果。

### 扬州10GW项目投资协议：租赁厂房、设备投入与项目公司资本金

- Evidence ID: `yangzhou-10gw-project-structure`
- 发布日期 / Published: 2022-12-09
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2022-12-09/1215304365.PDF

公司原有主营业务为无缝服装，拟形成“无缝服装+光伏”双主业。投资协议约定建设年产10GW高效光伏电池片项目，经营内容为TOPCon电池片研发、生产和销售；项目采用租赁厂房、购置生产设备的方式，计划总投资约26亿元（含流动资金），其中设备投资约16亿元，项目公司注册资本5亿元并由公司体系以货币出资。资金来源为自有及自筹资金。协议、设立项目公司和资本金安排均是必要前置环节，但并不证明生产线已经建成或形成自产产销。

### 项目风险披露：跨界团队、融资、客户、技术与按期投产相互约束

- Evidence ID: `project-execution-risk-chain`
- 发布日期 / Published: 2022-12-09
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2022-12-09/1215304365.PDF

公告明确公司尚未正式开展光伏生产，长期稳定客户资源能否取得存在不确定性；产品尚未大规模量产，成本、性能稳定性和技术先进性仍需验证。光伏业务依赖稳定专业团队，并需持续投入扩产、研发、生产运营、市场推广和人才资金。公司拟通过政府代建、自筹、金融机构贷款及产业基金等安排资金，但也提示融资未及时足额到位、工程滞后或方案调整可能导致项目无法按期投产或达产。模型需综合这些跨环节约束，而不能仅凭10GW规划给出结论。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `own_battery_cell_line_formal_operation_24m`
- 结果日期 / Resolved at: 2023-12-31
- 可观察日期 / Observed at: 2024-04-26

### 实际结果 / Realized outcome

- **observations**:
  - **own_battery_cell_line_formal_operation_count_24m**: 1
  - **own_line_formal_operation_confirmed**: 1
  - **self_manufactured_battery_cell_output_mw**: 426.45
  - **battery_cell_sales_mw**: 382.24
  - **photovoltaic_product_revenue_rmb**: 229492535.7
- **derivations**:


### 对应的题内资料 / Expected evidence

- `q3-2022-pit-capital-base`
- `yangzhou-10gw-project-structure`
- `project-execution-risk-chain`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_project_operation_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002634.XSHE
  - **ticker**: 002634
  - **name_as_of**: 棒杰股份
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2022-12-09
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_balance_sheet_pit
    - rq_income_statement_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=002634.XSHE; if_adjusted=0; quarter=2022q3; select the latest row with info_date<=2022-12-09, which is info_date=2022-10-26; project milestones adjudicated from issuer filings
  - **matching_group**: cross-industry-owned-production-line-formal-operation-24m-v1
  - **matching_role**: event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2022_q3_report**: 0c87e78da94a462e10f3003a52a239753e48fd186de56688ee040afde746ce85
    - **2022_project_investment_notice**: c8deb50423317b38c164661c467b2bd2ed97e4d41ff042941765430df563bf3f
    - **2023_project_operation_notice**: 226726f5f67635d8c38f2f851ef3cac0143c2132f118c739f84b4acffd320483
    - **2023_annual_report**: 3aa6663ec0b009a401a5d816e71f1864bb32fa2162421c39f714266917e0c4d8
  - **rqdata_file_sha256**:
    - **rq_balance_sheet_pit_2022q3**: ffbeed03f56a65549168be1451b3a7f244b3b77a2f9b52520d8e7bf7357d5fb9
    - **rq_income_statement_pit_2022q3**: bb76c01f9e6b250111f9659c8d88932bbae1b2d3c09813c6dcdb7ace45a3bcb7
    - **rq_cash_flow_pit_2022q3**: 11376d1ac8cb87c1194575c3479eca64cf5a5bd1785e6d538cd983e21e32a086
  - **outcome_contract**: Formal operation requires both an issuer-confirmed controlled own-line production milestone by 2024-12-09 and statutory-report evidence of actual self-manufactured battery-cell output or revenue; outsourced, rented-line and trading deliveries are excluded.
  - **leakage_guard**: The later first-cell announcement, ramp-up, photovoltaic revenue, controlled-line output and sales remain label-side only.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **1214901309.PDF**: 0c87e78da94a462e10f3003a52a239753e48fd186de56688ee040afde746ce85
    - **1215304365.PDF**: c8deb50423317b38c164661c467b2bd2ed97e4d41ff042941765430df563bf3f
- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_project_operation_notice
    - **title**: 关于扬州年产10GW高效光伏电池项目进展的公告
    - **published_at**: 2023-09-26
    - **url**: https://static.cninfo.com.cn/finalpage/2023-09-26/1217945755.PDF
    - **result**: 公司披露扬州项目已实现首片下线并逐步投产，同时提示仍需经历产能爬坡
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 226726f5f67635d8c38f2f851ef3cac0143c2132f118c739f84b4acffd320483
  - **item 2**:
    - **type**: official_annual_report
    - **title**: 浙江棒杰控股集团股份有限公司2023年年度报告
    - **published_at**: 2024-04-26
    - **url**: https://static.cninfo.com.cn/finalpage/2024-04-26/1219824132.PDF
    - **period_end**: 2023-12-31
    - **result**: 年报确认扬州10GW TOPCon生产基地于2023年第三季度末投产，第四季度形成光伏收入，并披露电池片生产426.45MW、销售382.24MW
    - **fields**:
      - 扬州10GW TOPCon电池生产基地投产
      - 光伏产品营业收入
      - 光伏电池片生产量
      - 光伏电池片销售量
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 3aa6663ec0b009a401a5d816e71f1864bb32fa2162421c39f714266917e0c4d8

</details>

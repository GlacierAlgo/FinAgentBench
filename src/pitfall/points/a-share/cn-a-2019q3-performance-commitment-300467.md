# cn-a-2019q3-performance-commitment-300467

## Question

你处在2019-10-30收盘后的信息环境。请使用下方冻结资料，预测迅游科技并购标的成都狮之吼2019年度承诺口径净利润是否会比3.2448亿元承诺值低20%以上。需要区分上市公司合并利润、标的公司利润和承诺口径净利润，并综合上年承诺完成情况、标的经营趋势、商誉减值、现金流与行业变化。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 迅游科技 (300467, SZSE)
- 信息截止 / As of: 2019-10-30
- 预测窗口结束 / Window end: 2020-06-30
- 目标事件 / Target: `material_performance_commitment_shortfall`
- 判定定义 / Definition: 并购标的狮之吼2019年度经专项审核的实际承诺口径净利润，比承诺净利润低20%以上

#### 判定条件 / Criteria

- `performance_commitment_shortfall_rate > 0.2` — （承诺净利润-实际承诺口径净利润）/承诺净利润超过20%

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 狮之吼2018年度业绩承诺实现情况专项审核报告

- Evidence ID: `2018-commitment-warning`
- 发布日期 / Published: 2019-04-27
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-04-27/1206122303.PDF

交易对方承诺狮之吼2017、2018、2019年度承诺口径净利润分别不低于1.92亿元、2.496亿元、3.2448亿元。2018年实际承诺口径净利润2.2459亿元，比承诺少2,500.51万元，短缺约10.02%。标的上年已经未达承诺但尚未达到本案例20%的重大缺口门槛，2019承诺值还需同比增长44.47%。

### 迅游科技2019年第三季度报告：合并业绩并非标的承诺口径

- Evidence ID: `2019-q3-consolidated-results`
- 发布日期 / Published: 2019-10-30
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2019-10-30/1207038564.PDF

截至2019-09-30，上市公司合并营业收入3.80亿元、归母净利润1.18亿元、经营活动现金流净额1.33亿元，合并商誉净额14.17亿元。半年报披露收购狮之吼形成商誉原值22.70亿元且此前已计提8.53亿元减值。合并盈利和正现金流是反向证据，但不能替代狮之吼扣除非经常性损益、剔除募集资金项目收益后的承诺口径。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `material_performance_commitment_shortfall`
- 结果日期 / Resolved at: 2020-04-28

### 实际结果 / Realized outcome

- **observations**:
  - **promised_profit**: 324480000
  - **actual_commitment_basis_profit**: 44690003.24
- **derivations**:
  - **item 1**:
    - **metric**: performance_commitment_shortfall
    - **operation**: difference
    - **inputs**:
      - promised_profit
      - actual_commitment_basis_profit
    - **value**: 279789996.76
  - **item 2**:
    - **metric**: performance_commitment_shortfall_rate
    - **operation**: ratio
    - **inputs**:
      - performance_commitment_shortfall
      - promised_profit
    - **value**: 0.8622719328155818

### 对应的题内资料 / Expected evidence

- `2018-commitment-warning`
- `2019-q3-consolidated-results`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_traps_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 300467.XSHE
  - **ticker**: 300467
  - **name_as_of**: 迅游科技
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-10-30
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: official CNINFO filings; aliyun:/dev/data1/download_rqdata used only for listed-company financial cross-checks
  - **access**: read_only
  - **data_lake_gap**: The local snapshot has no populated performance-commitment table; the signed special assurance report is label authority.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0; Rust CLI; PDFium native text plus chi_sim+eng OCR for scanned reports
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_special_assurance_report
    - **title**: 关于成都狮之吼科技有限公司2019年度业绩承诺实现情况说明专项审核报告
    - **published_at**: 2020-04-28
    - **url**: https://static.cninfo.com.cn/finalpage/2020-04-28/1207642649.PDF
    - **fields**:
      - 利润预测数
      - 实际盈利数
      - 差异

</details>

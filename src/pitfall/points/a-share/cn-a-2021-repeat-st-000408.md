# cn-a-2021-repeat-st-000408

## Question

你处在2021-05-11收盘后的信息环境。交易所已批准*ST藏格撤销全部退市风险警示，2021-05-12生效。请预测至2025-05-12（含）是否会开始新的独立ST或*ST episode。请评估财务更正与内控问题的整改深度、资源主业现金流和治理约束，避免历史频次这一单一捷径。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST藏格 (000408, SZSE)
- 信息截止 / As of: 2021-05-11
- 预测窗口结束 / Window end: 2025-05-12
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 判定定义 / Definition: 公司股票完整撤销全部ST或*ST风险警示正式生效后48个自然月内，是否至少开始一次新的、独立的ST或*ST风险警示episode。只有此前已完整退出风险警示状态后再次正式进入才计数；同一episode内ST与*ST互转、叠加警示或部分撤销不另计。

#### 判定条件 / Criteria

- `new_independent_st_episode_count_48m >= 1` — 完整摘除全部风险警示生效后48个自然月内，至少开始一次新的独立ST或*ST episode

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 藏格控股关于公司股票交易被实施退市风险警示的公告

- Evidence ID: `prior-st-2020-accounting-warning`
- 发布日期 / Published: 2020-04-30
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-04-30/1207687963.PDF

公司2019年度财务报告被审计机构出具无法表示意见的审计报告，因而触发退市风险警示。无法表示意见反映当时财务报告可验证性存在重大障碍，但历史触发原因本身不能代替对整改后是否复发的判断。

### 藏格控股关于撤销退市风险警示暨停复牌的公告

- Evidence ID: `full-removal-2021-approved`
- 发布日期 / Published: 2021-05-11
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2021-05-11/1209950332.PDF

深交所批准撤销全部退市风险警示，2021年5月12日复牌并恢复简称藏格控股。正式完整摘帽开启48个月预测时钟；历史问题严重度不能替代对整改后持续状态的判断。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 结果日期 / Resolved at: 2025-05-12
- 可观察日期 / Observed at: 2025-05-12

### 实际结果 / Realized outcome

- **observations**:
  - **new_independent_st_episode_count_48m**: 0
  - **new_episode_count_after_window_through_2026_08_12**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `prior-st-2020-accounting-warning`
- `full-removal-2021-approved`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_repeat_st_governance_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000408.XSHE
  - **ticker**: 000408
  - **name_as_of**: *ST藏格
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-05-11
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - is_st
    - special_treatment_info
    - symbol_change
  - **row_policy**: stock_code=000408.XSHE; as_of=full-removal announcement info_date 2021-05-11; prediction starts at official full-removal change_date 2021-05-12; window_end=same month/day plus 4 calendar years, inclusive
  - **episode_rule**: Sort daily is_st by stock/date. A new episode starts only on False-to-True after a prior False interval; ST-to-*ST, *ST-to-ST, additive warnings and partial removal inside an uninterrupted True interval are one episode. Official announcement change_date is label authority.
  - **governance_matching_axis**: governance continuity/change retained as unknown where official as-of evidence is insufficient; matching feature only
  - **matching_group**: full-removal-repeat-st-48m-v1
  - **matching_role**: no_event/governance_unknown
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **prior_st_notice**: eef850276dc97754959ec1148d1909c36978a194951d2dc4e386371b5c2f3d06
    - **full_removal_notice**: fe96fdb7116f989dd8e2391d9ffbf16fccc078d6229b906c4288ef3e47f160fa
  - **status_source_sha256**:
    - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
    - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
  - **negative_absence_cutoff**: 2026-08-12
  - **outcome_contract**: Official full-removal change_date starts the inclusive 48-calendar-month clock; only an official later change_date starting a new independent ST/*ST episode on or before window_end counts.
  - **date_discrepancy_policy**: An is_st flip on a suspension day before the official effective/resumption date is retained only as a dataset discrepancy; official change_date controls.
  - **leakage_guard**: Only documents published no later than as_of enter the corpus; negative absence is established label-side through both status tables at the stated cutoff.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: rqdata_negative_absence_crosscheck
    - **authoring_verified_through**: 2026-08-12
    - **earliest_sufficient_observation_date**: 2025-05-12
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2021-05-12/2025-05-12
    - **official_new_episode_change_dates_inside_window**:

    - **first_official_change_date_after_window**: null
    - **episode_count**: 0

</details>

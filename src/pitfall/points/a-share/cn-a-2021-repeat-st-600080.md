# cn-a-2021-repeat-st-600080

## Question

你处在2021-05-11收盘后的信息环境。交易所已批准ST金花撤销全部其他风险警示，2021-05-12生效。请预测至2025-05-12（含）是否会开始新的独立ST或*ST episode。请综合资金占用整改、财务韧性和控制治理变化，严格遵守48个月边界，不要用窗口外事实作推理输入。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST金花 (600080, SSE)
- 信息截止 / As of: 2021-05-11
- 预测窗口结束 / Window end: 2025-05-12
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 判定定义 / Definition: 公司股票完整撤销全部ST或*ST风险警示正式生效后48个自然月内，是否至少开始一次新的、独立的ST或*ST风险警示episode。只有此前已完整退出风险警示状态后再次正式进入才计数；同一episode内ST与*ST互转、叠加警示或部分撤销不另计。

#### 判定条件 / Criteria

- `new_independent_st_episode_count_48m >= 1` — 完整摘除全部风险警示生效后48个自然月内，至少开始一次新的独立ST或*ST episode

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 金花股份关于股票实施其他风险警示的公告

- Evidence ID: `prior-st-2020-fund-occupation`
- 发布日期 / Published: 2020-06-01
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-06-01/1207878970.PDF

公司因原控股股东及关联方非经营性资金占用等内部控制事项被实施其他风险警示。该原因可以通过清偿解除当期警示，但未来风险取决于控制权、董事会约束和经营现金流是否形成持续修复。

### 金花股份关于撤销其他风险警示暨停牌的公告

- Evidence ID: `full-removal-2021-approved`
- 发布日期 / Published: 2021-05-11
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2021-05-11/1209948204.PDF

上交所同意撤销全部其他风险警示，2021年5月12日起恢复简称金花股份。公告证明占款等本轮原因达到撤销条件；预测仍应对未来四年的独立新触发作概率判断。

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
  - **new_episode_count_after_window_through_2026_08_12**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `prior-st-2020-fund-occupation`
- `full-removal-2021-approved`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_repeat_st_governance_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600080.XSHG
  - **ticker**: 600080
  - **name_as_of**: ST金花
  - **exchange**: SSE
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
  - **row_policy**: stock_code=600080.XSHG; as_of=full-removal announcement info_date 2021-05-11; prediction starts at official full-removal change_date 2021-05-12; window_end=same month/day plus 4 calendar years, inclusive
  - **episode_rule**: Sort daily is_st by stock/date. A new episode starts only on False-to-True after a prior False interval; ST-to-*ST, *ST-to-ST, additive warnings and partial removal inside an uninterrupted True interval are one episode. Official announcement change_date is label authority.
  - **governance_matching_axis**: controller and chairman changed after as_of; matching feature only, not a management-quality label
  - **matching_group**: full-removal-repeat-st-48m-v1
  - **matching_role**: no_event/control_change/later_recurrence
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **prior_st_notice**: 076582de2b46d70471f15ac8ab1d8cb96fb821375bf3098931bd817208960ba9
    - **full_removal_notice**: 4dfa11935a34b5e8c152bae332cd362c43b85c536c19378ee3274c009917c940
  - **status_source_sha256**:
    - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
    - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
  - **negative_absence_cutoff**: 2026-08-12
  - **outcome_contract**: Official full-removal change_date starts the inclusive 48-calendar-month clock; only an official later change_date starting a new independent ST/*ST episode on or before window_end counts.
  - **date_discrepancy_policy**: An is_st flip on a suspension day before the official effective/resumption date is retained only as a dataset discrepancy; official change_date controls.
  - **leakage_guard**: Only documents published no later than as_of enter the corpus; the 2026 later episode remains label-side only.
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

    - **first_official_change_date_after_window**: 2026-04-30
    - **episode_count**: 0

</details>

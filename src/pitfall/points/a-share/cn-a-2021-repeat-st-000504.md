# cn-a-2021-repeat-st-000504

## Question

你处在2021-04-27收盘后的信息环境。交易所已批准ST生物撤销全部其他风险警示，2021-04-28生效。请预测至2025-04-28（含）是否会开始新的独立ST或*ST episode。请正确处理48个月固定边界，区分此前部分撤销和本次完整摘帽，并把控制链连续性与管理更替作为分析变量。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST生物 (000504, SZSE)
- 信息截止 / As of: 2021-04-27
- 预测窗口结束 / Window end: 2025-04-28
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 判定定义 / Definition: 公司股票完整撤销全部ST或*ST风险警示正式生效后48个自然月内，是否至少开始一次新的、独立的ST或*ST风险警示episode。只有此前已完整退出风险警示状态后再次正式进入才计数；同一episode内ST与*ST互转、叠加警示或部分撤销不另计。

#### 判定条件 / Criteria

- `new_independent_st_episode_count_48m >= 1` — 完整摘除全部风险警示生效后48个自然月内，至少开始一次新的独立ST或*ST episode

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 南华生物关于公司股票交易实行退市风险警示的公告

- Evidence ID: `prior-st-2019-new-episode`
- 发布日期 / Published: 2019-04-30
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2019-04-30/1206163375.PDF

公司在2017年完整摘帽后又于2019年形成一段新的风险警示episode，历史上存在复发。该事实是先验信号，但不能替代对2021年后固定窗口的经营和治理判断。

### 南华生物撤销退市风险警示并继续实行其他风险警示公告

- Evidence ID: `partial-removal-2020-st-remained`
- 发布日期 / Published: 2020-06-11
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-06-11/1207916428.PDF

公司仅撤销退市风险警示而继续实行其他风险警示，简称改为ST生物。is_st连续为真，这次部分撤销既不是完整摘帽，也不是新的独立episode。

### 南华生物关于撤销其他风险警示暨停复牌的公告

- Evidence ID: `full-removal-2021-approved`
- 发布日期 / Published: 2021-04-27
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2021-04-27/1209813030.PDF

深交所批准撤销全部其他风险警示，2021年4月28日复牌并恢复简称南华生物。这是连续episode的正式终点，新的48个月时钟自该官方生效日开始。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 结果日期 / Resolved at: 2025-04-28
- 可观察日期 / Observed at: 2025-04-29

### 实际结果 / Realized outcome

- **observations**:
  - **new_independent_st_episode_count_48m**: 0
  - **first_new_episode_after_window_days**: 2
  - **new_episode_count_after_window_through_2026_08_12**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `prior-st-2019-new-episode`
- `partial-removal-2020-st-remained`
- `full-removal-2021-approved`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_repeat_st_governance_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000504.XSHE
  - **ticker**: 000504
  - **name_as_of**: ST生物
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-04-27
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - is_st
    - special_treatment_info
    - symbol_change
  - **row_policy**: stock_code=000504.XSHE; as_of=full-removal announcement info_date 2021-04-27; prediction starts at official full-removal change_date 2021-04-28; window_end=same month/day plus 4 calendar years, inclusive
  - **episode_rule**: Sort daily is_st by stock/date. A new episode starts only on False-to-True after a prior False interval; ST-to-*ST, *ST-to-ST, additive warnings and partial removal inside an uninterrupted True interval are one episode. Official announcement change_date is label authority.
  - **governance_matching_axis**: ultimate provincial state-control chain continuity with chairman turnover; matching feature only
  - **matching_group**: full-removal-repeat-st-48m-v1
  - **matching_role**: no_event/control_continuity/temporal_hard_negative
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **prior_st_notice**: 2cba2ed7abc8ad9d07fe8031b6276b4f6af934e476de89f8bd9e9f9397859490
    - **partial_removal_notice**: c6a236f26409f7c201e8643dd3fa7a31564212e335dc7ded4f10010ffa0040a7
    - **full_removal_notice**: 84599681a76294d160551f8710272751232d426430767f77052c3006fc38a97d
  - **status_source_sha256**:
    - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
    - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
  - **negative_absence_cutoff**: 2026-08-12
  - **outcome_contract**: Official full-removal change_date starts the inclusive 48-calendar-month clock; only an official later change_date starting a new independent ST/*ST episode on or before window_end counts.
  - **date_discrepancy_policy**: An is_st flip on a suspension day before the official effective/resumption date is retained only as a dataset discrepancy; official change_date controls.
  - **leakage_guard**: Only documents published no later than as_of enter the corpus; the 2025 re-warning two days after the boundary remains label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_first_new_episode_after_window
    - **title**: 南华生物关于公司股票交易被实施退市风险警示暨停牌的公告
    - **published_at**: 2025-04-29
    - **effective_change_date**: 2025-04-30
    - **url**: https://static.cninfo.com.cn/finalpage/2025-04-29/1223381439.PDF
    - **sha256**: 298c92b37fa377bb55c13e4b34bf9f5884939f963815239c1b7742408d863653
    - **window_end**: 2025-04-28
    - **inside_window**: false
  - **item 2**:
    - **type**: rqdata_negative_absence_crosscheck
    - **authoring_verified_through**: 2026-08-12
    - **earliest_sufficient_observation_date**: 2025-04-29
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2021-04-28/2025-04-28
    - **official_new_episode_change_dates_inside_window**:

    - **first_official_change_date_after_window**: 2025-04-30
    - **episode_count**: 0

</details>

# cn-a-2016-repeat-st-600381

## Question

你处在2016-11-18收盘后的信息环境。交易所已批准ST春天撤销全部其他风险警示，2016-11-21生效。请预测至2020-11-21（含）是否会开始新的独立ST或*ST episode。请分析整改与主营可持续性、控制人和董事长连续性，但不得把管理层身份本身当作结果标签。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST春天 (600381, SSE)
- 信息截止 / As of: 2016-11-18
- 预测窗口结束 / Window end: 2020-11-21
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 判定定义 / Definition: 公司股票完整撤销全部ST或*ST风险警示正式生效后48个自然月内，是否至少开始一次新的、独立的ST或*ST风险警示episode。只有此前已完整退出风险警示状态后再次正式进入才计数；同一episode内ST与*ST互转、叠加警示或部分撤销不另计。

#### 判定条件 / Criteria

- `new_independent_st_episode_count_48m >= 1` — 完整摘除全部风险警示生效后48个自然月内，至少开始一次新的独立ST或*ST episode

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 青海春天关于公司股票实施其他风险警示暨股票复牌的公告

- Evidence ID: `prior-st-2016-control-warning`
- 发布日期 / Published: 2016-06-28
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2016-06-28/1202419344.PDF

公司在2016年3月31日收到通知后停止冬虫夏草纯粉片产品试点和生产，生产经营受到严重影响且预计三个月内不能恢复正常，股票自2016年6月29日起被实施其他风险警示。该事件提示应区分新业务承诺与可持续经营事实。

### 青海春天关于撤销其他风险警示暨停牌的公告

- Evidence ID: `full-removal-2016-approved`
- 发布日期 / Published: 2016-11-18
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2016-11-18/1202834525.PDF

上交所同意撤销全部其他风险警示；公司披露整体营运正常、核心团队稳定，2016年11月21日起简称恢复为青海春天并退出风险警示板。规则层面的整改完成并不自动指向未来复发或不复发。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 结果日期 / Resolved at: 2020-11-21
- 可观察日期 / Observed at: 2020-11-23

### 实际结果 / Realized outcome

- **observations**:
  - **new_independent_st_episode_count_48m**: 0
  - **new_episode_count_after_window_through_2026_08_12**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `prior-st-2016-control-warning`
- `full-removal-2016-approved`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_repeat_st_governance_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600381.XSHG
  - **ticker**: 600381
  - **name_as_of**: ST春天
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2016-11-18
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - is_st
    - special_treatment_info
    - symbol_change
  - **row_policy**: stock_code=600381.XSHG; as_of=full-removal announcement info_date 2016-11-18; prediction starts at official full-removal change_date 2016-11-21; window_end=same month/day plus 4 calendar years, inclusive
  - **episode_rule**: Sort daily is_st by stock/date. A new episode starts only on False-to-True after a prior False interval; ST-to-*ST, *ST-to-ST, additive warnings and partial removal inside an uninterrupted True interval are one episode. Official announcement change_date is label authority.
  - **governance_matching_axis**: controller and chairman continuity; matching feature only, not a management-quality label
  - **matching_group**: full-removal-repeat-st-48m-v1
  - **matching_role**: no_event/control_continuity/same_issuer_temporal
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **prior_st_notice**: 3e5a1df2c55f00ea3435147ef373be27dee92860305ab8401e94c4365acc25e7
    - **full_removal_notice**: 6581dd67fa193702bc021dd7ca3734e9e02203e94f64279e78e4e250455fcbab
  - **status_source_sha256**:
    - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
    - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
  - **negative_absence_cutoff**: 2026-08-12
  - **outcome_contract**: Official full-removal change_date starts the inclusive 48-calendar-month clock; only an official later change_date starting a new independent ST/*ST episode on or before window_end counts.
  - **date_discrepancy_policy**: An is_st flip on a suspension day before the official effective/resumption date is retained only as a dataset discrepancy; official change_date controls.
  - **leakage_guard**: Only documents published no later than as_of enter the corpus; the 2024 later episode remains label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: rqdata_negative_absence_crosscheck
    - **authoring_verified_through**: 2026-08-12
    - **earliest_sufficient_observation_date**: 2020-11-23
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2016-11-21/2020-11-21
    - **official_new_episode_change_dates_inside_window**:

    - **first_official_change_date_after_window**: 2024-05-06
    - **episode_count**: 0

</details>

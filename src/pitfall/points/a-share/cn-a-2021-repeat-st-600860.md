# cn-a-2021-repeat-st-600860

## Question

你处在2021-04-01收盘后的信息环境。交易所已批准*ST京城撤销全部退市风险警示，2021-04-02生效。请预测至2025-04-02（含）是否会开始新的独立ST或*ST episode。请综合周期性经营、扭亏质量、资产负债与治理稳定性，不要因历史多次戴帽直接给确定性结论。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST京城 (600860, SSE)
- 信息截止 / As of: 2021-04-01
- 预测窗口结束 / Window end: 2025-04-02
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 判定定义 / Definition: 公司股票完整撤销全部ST或*ST风险警示正式生效后48个自然月内，是否至少开始一次新的、独立的ST或*ST风险警示episode。只有此前已完整退出风险警示状态后再次正式进入才计数；同一episode内ST与*ST互转、叠加警示或部分撤销不另计。

#### 判定条件 / Criteria

- `new_independent_st_episode_count_48m >= 1` — 完整摘除全部风险警示生效后48个自然月内，至少开始一次新的独立ST或*ST episode

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 京城股份关于股票实施退市风险警示的公告

- Evidence ID: `prior-st-2020-loss-warning`
- 发布日期 / Published: 2020-03-28
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-03-28/1207417440.PDF

公司因连续两个会计年度经审计净利润为负而被实施退市风险警示。气体储运装备业务具有周期性，历史亏损是风险先验，但固定窗口结果仍取决于后续盈利质量和财务缓冲。

### 京城股份关于撤销退市风险警示暨停牌的公告

- Evidence ID: `full-removal-2021-approved`
- 发布日期 / Published: 2021-04-01
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2021-04-01/1209567630.PDF

上交所同意撤销全部退市风险警示，2021年4月2日起恢复简称京城股份。规则条件当期已满足，基准要求预测此后整整48个月内是否形成新的独立episode，而不是泛化为公司永不再戴帽。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 结果日期 / Resolved at: 2025-04-02
- 可观察日期 / Observed at: 2025-04-02

### 实际结果 / Realized outcome

- **observations**:
  - **new_independent_st_episode_count_48m**: 0
  - **new_episode_count_after_window_through_2026_08_12**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `prior-st-2020-loss-warning`
- `full-removal-2021-approved`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_repeat_st_governance_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600860.XSHG
  - **ticker**: 600860
  - **name_as_of**: *ST京城
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-04-01
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - is_st
    - special_treatment_info
    - symbol_change
  - **row_policy**: stock_code=600860.XSHG; as_of=full-removal announcement info_date 2021-04-01; prediction starts at official full-removal change_date 2021-04-02; window_end=same month/day plus 4 calendar years, inclusive
  - **episode_rule**: Sort daily is_st by stock/date. A new episode starts only on False-to-True after a prior False interval; ST-to-*ST, *ST-to-ST, additive warnings and partial removal inside an uninterrupted True interval are one episode. Official announcement change_date is label authority.
  - **governance_matching_axis**: control/management continuity or change is a matched analysis feature, never a good-management/bad-management label
  - **matching_group**: full-removal-repeat-st-48m-v1
  - **matching_role**: no_event/governance_matched
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **prior_st_notice**: e526d1476d259b8c8c9de298ee39c1a3acb070e60c9761359b826b5e950d7502
    - **full_removal_notice**: c5d444e69aef4db15ce08a9c04b06c8c4b92ce1308411d436aa93dbd48a71264
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
    - **earliest_sufficient_observation_date**: 2025-04-02
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2021-04-02/2025-04-02
    - **official_new_episode_change_dates_inside_window**:

    - **first_official_change_date_after_window**: null
    - **episode_count**: 0

</details>

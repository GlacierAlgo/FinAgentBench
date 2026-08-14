# cn-a-2021-repeat-st-002650

## Question

你处在2021-07-27收盘后的信息环境。交易所已批准ST加加撤销全部其他风险警示，2021-07-28生效。请基于冻结证据预测：自该生效日起至2025-07-28（含）是否会开始新的独立ST或*ST episode。重点判断占款/担保整改是否代表治理机制持续改善，并把控制人连续性作为风险特征而非价值判断。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST加加 (002650, SZSE)
- 信息截止 / As of: 2021-07-27
- 预测窗口结束 / Window end: 2025-07-28
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 判定定义 / Definition: 公司股票完整撤销全部ST或*ST风险警示正式生效后48个自然月内，是否至少开始一次新的、独立的ST或*ST风险警示episode。只有此前已完整退出风险警示状态后再次正式进入才计数；同一episode内ST与*ST互转、叠加警示或部分撤销不另计。

#### 判定条件 / Criteria

- `new_independent_st_episode_count_48m >= 1` — 完整摘除全部风险警示生效后48个自然月内，至少开始一次新的独立ST或*ST episode

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 加加食品关于公司股票交易实行其他风险警示的公告

- Evidence ID: `prior-st-2020-governance-warning`
- 发布日期 / Published: 2020-06-12
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-06-12/1207919359.PDF

公告披露公司尚未解决的违规对外担保本金余额为4.6605亿元，占最近一期经审计净资产的19.94%，因而被实施其他风险警示。触发原因不是主营收入门槛；预测复发时应考察担保解除与制度整改，而不能把一次形式整改当作永久改善。

### 加加食品关于撤销其他风险警示暨停复牌的公告

- Evidence ID: `full-removal-2021-approved`
- 发布日期 / Published: 2021-07-27
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2021-07-27/1210573032.PDF

深交所审核同意撤销公司股票全部其他风险警示；股票停牌后于2021年7月28日复牌，简称恢复为加加食品并退出风险警示板。本次审批证明当期撤销条件成立，但不等于同一控制人家族下的内控复发概率为零。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 结果日期 / Resolved at: 2024-04-30
- 可观察日期 / Observed at: 2024-04-29

### 实际结果 / Realized outcome

- **observations**:
  - **new_independent_st_episode_count_48m**: 1
  - **full_removal_effective_before_new_episode**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `prior-st-2020-governance-warning`
- `full-removal-2021-approved`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_repeat_st_governance_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002650.XSHE
  - **ticker**: 002650
  - **name_as_of**: ST加加
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-07-27
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - is_st
    - special_treatment_info
    - symbol_change
  - **row_policy**: stock_code=002650.XSHE; as_of=full-removal announcement info_date 2021-07-27; prediction starts at official full-removal change_date 2021-07-28; window_end=same month/day plus 4 calendar years, inclusive
  - **episode_rule**: Sort daily is_st by stock/date. A new episode starts only on False-to-True after a prior False interval; ST-to-*ST, *ST-to-ST, additive warnings and partial removal inside an uninterrupted True interval are one episode. Official announcement change_date is label authority.
  - **governance_matching_axis**: controller-family continuity with chairman turnover; matching feature only, not a management-quality label
  - **matching_group**: full-removal-repeat-st-48m-v1
  - **matching_role**: event/control_continuity
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **prior_st_notice**: fdb701da870263744592c52572bd2585a6e1ece51448874a9fd19f80e44b1ef6
    - **full_removal_notice**: fba7637fef2adb506b4fb221a0bcab28ff0cf07b3c14d9b10a9e064fdab7c6d1
  - **status_source_sha256**:
    - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
    - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
  - **outcome_contract**: Official full-removal change_date starts the inclusive 48-calendar-month clock; only an official later change_date starting a new independent ST/*ST episode on or before window_end counts.
  - **date_discrepancy_policy**: An is_st flip on a suspension day before the official effective/resumption date is retained only as a dataset discrepancy; official change_date controls.
  - **leakage_guard**: Only documents published no later than as_of enter the corpus; later re-warning notices and status rows remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_new_independent_st_episode
    - **title**: 加加食品关于公司股票交易被实施其他风险警示暨停牌的公告
    - **published_at**: 2024-04-29
    - **effective_change_date**: 2024-04-30
    - **url**: https://static.cninfo.com.cn/finalpage/2024-04-29/1219872724.PDF
    - **sha256**: 0ac4f30dbc3df426497cbeee7fa99fe8fc754964235e837ae624bd47067b9f1e
    - **prior_full_removal_effective_date**: 2021-07-28
    - **new_independent_episode**: true
  - **item 2**:
    - **type**: rqdata_status_transition_crosscheck
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2021-07-28/2025-07-28
    - **official_new_episode_change_dates**:
      - 2024-04-30
    - **episode_count**: 1

</details>

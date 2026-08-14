# cn-a-2021-repeat-st-002306

## Question

你处在2021-04-13收盘后的信息环境。交易所已批准ST云网撤销全部其他风险警示，2021-04-14生效。请预测至2025-04-14（含）是否会开始新的独立ST或*ST episode。请正确处理固定窗口边界，结合此前*ST降ST、最终完整摘帽和控制权变化判断复发风险。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST云网 (002306, SZSE)
- 信息截止 / As of: 2021-04-13
- 预测窗口结束 / Window end: 2025-04-14
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 判定定义 / Definition: 公司股票完整撤销全部ST或*ST风险警示正式生效后48个自然月内，是否至少开始一次新的、独立的ST或*ST风险警示episode。只有此前已完整退出风险警示状态后再次正式进入才计数；同一episode内ST与*ST互转、叠加警示或部分撤销不另计。

#### 判定条件 / Criteria

- `new_independent_st_episode_count_48m >= 1` — 完整摘除全部风险警示生效后48个自然月内，至少开始一次新的独立ST或*ST episode

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 中科云网关于公司股票交易被实施退市风险警示的公告

- Evidence ID: `prior-st-2017-new-episode`
- 发布日期 / Published: 2017-04-26
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2017-04-26/1203386418.PDF

公司在2016年完整摘帽后，因2016年度经审计期末净资产为负值，自2017年4月27日起被实施退市风险警示，形成新的独立*ST episode。2017年6月因银行账户被冻结而叠加的其他风险警示发生在同一episode内，并非此次episode的起因或又一次复发。该历史事实是先验信号，但不能替代对2021年后固定四年窗口的判断。

### 中科云网撤销退市风险警示并继续实行其他风险警示公告

- Evidence ID: `partial-removal-2019-st-remained`
- 发布日期 / Published: 2019-07-31
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2019-07-31/1206484669.PDF

公司撤销退市风险警示，但继续被实施其他风险警示，证券简称由*ST云网变为ST云网。因此2019年不是一个episode结束或新episode开始，不能重置复发时钟。

### 中科云网关于撤销其他风险警示暨停复牌的公告

- Evidence ID: `full-removal-2021-approved`
- 发布日期 / Published: 2021-04-13
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2021-04-13/1209675625.PDF

深交所批准撤销最后一项其他风险警示，2021年4月14日复牌并恢复简称中科云网。只有这次完整退出才结束2017年以来的连续episode并开启新的48个月预测时钟。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 结果日期 / Resolved at: 2025-04-14
- 可观察日期 / Observed at: 2025-04-15

### 实际结果 / Realized outcome

- **observations**:
  - **new_independent_st_episode_count_48m**: 0
  - **first_new_episode_after_window_days**: 2
  - **new_episode_count_after_window_through_2026_08_12**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `prior-st-2017-new-episode`
- `partial-removal-2019-st-remained`
- `full-removal-2021-approved`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_repeat_st_governance_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002306.XSHE
  - **ticker**: 002306
  - **name_as_of**: ST云网
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-04-13
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - is_st
    - special_treatment_info
    - symbol_change
  - **row_policy**: stock_code=002306.XSHE; as_of=full-removal announcement info_date 2021-04-13; prediction starts at official full-removal change_date 2021-04-14; window_end=same month/day plus 4 calendar years, inclusive
  - **episode_rule**: Sort daily is_st by stock/date. A new episode starts only on False-to-True after a prior False interval; ST-to-*ST, *ST-to-ST, additive warnings and partial removal inside an uninterrupted True interval are one episode. Official announcement change_date is label authority.
  - **governance_matching_axis**: controller changed before as_of; matching feature only, not a management-quality label
  - **matching_group**: full-removal-repeat-st-48m-v1
  - **matching_role**: no_event/control_change/temporal_hard_negative
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **prior_st_notice**: 65cb95ae32d75815de75352a3313131dc051d3feeb74f01d1e8cb76bda9fcd47
    - **partial_removal_notice**: c4ab766063a373f2a8b8814ea9fbdb938c5a07d4780580f7c2111bd19cc96f9a
    - **full_removal_notice**: 6b3a827d80ebcdc58ff1b5b64b91252c136f88ca226278a2a2207ff72c395ff4
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
    - **title**: 中科云网科技集团股份有限公司关于公司股票交易被实施退市风险警示叠加其他风险警示暨停牌的公告
    - **published_at**: 2025-04-15
    - **effective_change_date**: 2025-04-16
    - **url**: https://static.cninfo.com.cn/finalpage/2025-04-15/1223097496.PDF
    - **sha256**: 66c2a903a3a3b609033322a9ee351de15a3489ee87b4b778f7e2a91fa7119242
    - **window_end**: 2025-04-14
    - **inside_window**: false
  - **item 2**:
    - **type**: rqdata_negative_absence_crosscheck
    - **authoring_verified_through**: 2026-08-12
    - **earliest_sufficient_observation_date**: 2025-04-15
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2021-04-14/2025-04-14
    - **official_new_episode_change_dates_inside_window**:

    - **first_official_change_date_after_window**: 2025-04-16
    - **episode_count**: 0

</details>

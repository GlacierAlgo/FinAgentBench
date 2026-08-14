# cn-a-2017-repeat-st-000504

## Question

你处在2017-05-11收盘后的信息环境。交易所已批准*ST生物撤销全部退市风险警示，2017-05-12生效。请预测至2021-05-12（含）是否会开始新的独立ST或*ST episode。请评估扭亏质量、主业稳定性、国资控制链连续性与董事长更替；不要把控制人性质当作结论。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST生物 (000504, SZSE)
- 信息截止 / As of: 2017-05-11
- 预测窗口结束 / Window end: 2021-05-12
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 判定定义 / Definition: 公司股票完整撤销全部ST或*ST风险警示正式生效后48个自然月内，是否至少开始一次新的、独立的ST或*ST风险警示episode。只有此前已完整退出风险警示状态后再次正式进入才计数；同一episode内ST与*ST互转、叠加警示或部分撤销不另计。

#### 判定条件 / Criteria

- `new_independent_st_episode_count_48m >= 1` — 完整摘除全部风险警示生效后48个自然月内，至少开始一次新的独立ST或*ST episode

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 南华生物关于公司股票交易实行退市风险警示的公告

- Evidence ID: `prior-st-2016-loss-warning`
- 发布日期 / Published: 2016-04-25
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2016-04-25/1202229463.PDF

公司因连续两个会计年度经审计净利润为负，自2016年4月26日起被实施退市风险警示。该原因直接指向主业持续盈利能力，预测复发不能只看下一年度账面扭亏。

### 南华生物关于撤销退市风险警示暨停牌的公告

- Evidence ID: `full-removal-2017-approved`
- 发布日期 / Published: 2017-05-11
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2017-05-11/1203492613.PDF

深交所同意撤销全部退市风险警示，公司于2017年5月12日复牌并恢复为南华生物。规则条件当期已满足，但公司体量、扣非盈利和主营稳定性决定完整摘帽后是否仍可能形成新的独立风险警示episode。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 结果日期 / Resolved at: 2019-05-06
- 可观察日期 / Observed at: 2019-04-30

### 实际结果 / Realized outcome

- **observations**:
  - **new_independent_st_episode_count_48m**: 1
  - **full_removal_effective_before_new_episode**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `prior-st-2016-loss-warning`
- `full-removal-2017-approved`

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
  - **name_as_of**: *ST生物
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2017-05-11
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - is_st
    - special_treatment_info
    - symbol_change
  - **row_policy**: stock_code=000504.XSHE; as_of=full-removal announcement info_date 2017-05-11; prediction starts at official full-removal change_date 2017-05-12; window_end=same month/day plus 4 calendar years, inclusive
  - **episode_rule**: Sort daily is_st by stock/date. A new episode starts only on False-to-True after a prior False interval; ST-to-*ST, *ST-to-ST, additive warnings and partial removal inside an uninterrupted True interval are one episode. Official announcement change_date is label authority.
  - **governance_matching_axis**: ultimate provincial state-control chain continuity with chairman turnover; matching feature only
  - **matching_group**: full-removal-repeat-st-48m-v1
  - **matching_role**: event/control_continuity
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **prior_st_notice**: fbeac781efc10a559dd7d48945394b426cf3754b1ef67be51063f9ea5afd8c7d
    - **full_removal_notice**: 705e18524cb71ee051eb4806fcc3180c46f12f29e412d6d130ae5999629fbaeb
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
    - **title**: 南华生物关于公司股票交易实行退市风险警示的公告
    - **published_at**: 2019-04-30
    - **effective_change_date**: 2019-05-06
    - **url**: https://static.cninfo.com.cn/finalpage/2019-04-30/1206163375.PDF
    - **sha256**: 2cba2ed7abc8ad9d07fe8031b6276b4f6af934e476de89f8bd9e9f9397859490
    - **prior_full_removal_effective_date**: 2017-05-12
    - **new_independent_episode**: true
  - **item 2**:
    - **type**: rqdata_status_transition_crosscheck
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2017-05-12/2021-05-12
    - **official_new_episode_change_dates**:
      - 2019-05-06
    - **episode_count**: 1

</details>

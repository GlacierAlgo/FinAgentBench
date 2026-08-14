# cn-a-2018-repeat-st-600225

## Question

你处在2018-05-04收盘后的信息环境。交易所已批准*ST松江撤销全部退市风险警示，2018-05-07生效。请预测至2022-05-07（含）是否会开始新的独立ST或*ST episode。请区分一次性扭亏与可持续经营改善，并分析国资控制链和经营管理变化，但不要把治理身份直接当作标签。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST松江 (600225, SSE)
- 信息截止 / As of: 2018-05-04
- 预测窗口结束 / Window end: 2022-05-07
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 判定定义 / Definition: 公司股票完整撤销全部ST或*ST风险警示正式生效后48个自然月内，是否至少开始一次新的、独立的ST或*ST风险警示episode。只有此前已完整退出风险警示状态后再次正式进入才计数；同一episode内ST与*ST互转、叠加警示或部分撤销不另计。

#### 判定条件 / Criteria

- `new_independent_st_episode_count_48m >= 1` — 完整摘除全部风险警示生效后48个自然月内，至少开始一次新的独立ST或*ST episode

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 天津松江关于公司股票实施退市风险警示的公告

- Evidence ID: `prior-st-2017-loss-warning`
- 发布日期 / Published: 2017-03-18
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2017-03-18/1203174629.PDF

因连续两个会计年度经审计净利润为负，公司股票被实施退市风险警示。连续亏损反映当时经营造血能力不足；后续摘帽是否依赖非经常性收益及资产处置，是判断再次触发的重要问题。

### 天津松江关于撤销退市风险警示暨停牌的公告

- Evidence ID: `full-removal-2018-approved`
- 发布日期 / Published: 2018-05-04
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2018-05-04/1204906819.PDF

上交所同意撤销全部退市风险警示，公司于2018年5月7日复牌并恢复简称天津松江。摘帽依据当期财务指标已不再触发规则；冻结证据并未保证房地产等存量业务在未来四年持续盈利。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 结果日期 / Resolved at: 2020-04-24
- 可观察日期 / Observed at: 2020-04-23

### 实际结果 / Realized outcome

- **observations**:
  - **new_independent_st_episode_count_48m**: 1
  - **full_removal_effective_before_new_episode**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `prior-st-2017-loss-warning`
- `full-removal-2018-approved`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_repeat_st_governance_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600225.XSHG
  - **ticker**: 600225
  - **name_as_of**: *ST松江
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2018-05-04
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - is_st
    - special_treatment_info
    - symbol_change
  - **row_policy**: stock_code=600225.XSHG; as_of=full-removal announcement info_date 2018-05-04; prediction starts at official full-removal change_date 2018-05-07; window_end=same month/day plus 4 calendar years, inclusive
  - **episode_rule**: Sort daily is_st by stock/date. A new episode starts only on False-to-True after a prior False interval; ST-to-*ST, *ST-to-ST, additive warnings and partial removal inside an uninterrupted True interval are one episode. Official announcement change_date is label authority.
  - **governance_matching_axis**: ultimate state controller continuity with intermediate owner/management change; matching feature only
  - **matching_group**: full-removal-repeat-st-48m-v1
  - **matching_role**: event/mixed_governance_change
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **prior_st_notice**: 4dec4ddd12b404af4cafab4af07998c7ccbbc6241a9c9f9975e1a7ca52670708
    - **full_removal_notice**: d63a7cd4da3a6ca0084af6f537b3ac3ba4ad718b39b0975a67493bf465a32cdc
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
    - **title**: 天津松江关于公司股票实施退市风险警示暨停牌的公告
    - **published_at**: 2020-04-23
    - **effective_change_date**: 2020-04-24
    - **url**: https://static.cninfo.com.cn/finalpage/2020-04-23/1207558095.PDF
    - **sha256**: d209eca66510bce31bc256d88204394ccf842239099f332c34f6cf043a6d90e4
    - **prior_full_removal_effective_date**: 2018-05-07
    - **new_independent_episode**: true
  - **item 2**:
    - **type**: rqdata_status_transition_crosscheck
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2018-05-07/2022-05-07
    - **official_new_episode_change_dates**:
      - 2020-04-24
    - **episode_count**: 1

</details>

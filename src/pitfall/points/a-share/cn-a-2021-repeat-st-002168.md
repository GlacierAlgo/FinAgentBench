# cn-a-2021-repeat-st-002168

## Question

你处在2021-04-08收盘后的信息环境。交易所已批准ST惠程撤销全部其他风险警示，2021-04-09生效。请预测至2025-04-09（含）是否会开始新的独立ST或*ST episode。请综合占款清偿、主业和资产质量、控制权可能变化对制度性复发风险的影响；治理变化本身不是好坏标签。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST惠程 (002168, SZSE)
- 信息截止 / As of: 2021-04-08
- 预测窗口结束 / Window end: 2025-04-09
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 判定定义 / Definition: 公司股票完整撤销全部ST或*ST风险警示正式生效后48个自然月内，是否至少开始一次新的、独立的ST或*ST风险警示episode。只有此前已完整退出风险警示状态后再次正式进入才计数；同一episode内ST与*ST互转、叠加警示或部分撤销不另计。

#### 判定条件 / Criteria

- `new_independent_st_episode_count_48m >= 1` — 完整摘除全部风险警示生效后48个自然月内，至少开始一次新的独立ST或*ST episode

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 惠程科技关于公司股票交易实行其他风险警示的公告

- Evidence ID: `prior-st-2021-fund-occupation`
- 发布日期 / Published: 2021-03-02
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2021-03-02/1209318659.PDF

公司因控股股东及关联方非经营性占用资金未按期全部归还而自2021年3月3日起成为ST惠程；公告列示累计归还31,015.42万元、余额6,067.49万元。付款进度是整改信号，但风险源涉及控制人行为及内控约束。

### 惠程科技关于公司股票撤销其他风险警示暨停牌的公告

- Evidence ID: `full-removal-2021-approved`
- 发布日期 / Published: 2021-04-08
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2021-04-08/1209648558.PDF

深交所同意撤销全部其他风险警示；股票于2021年4月9日复牌并恢复简称惠程科技，完整退出风险警示板。占用资金已清偿使本轮警示解除，但预测任务要求进一步判断未来四年是否会因新的独立原因再次被实施ST或*ST。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 结果日期 / Resolved at: 2024-09-19
- 可观察日期 / Observed at: 2024-09-14

### 实际结果 / Realized outcome

- **observations**:
  - **new_independent_st_episode_count_48m**: 1
  - **full_removal_effective_before_new_episode**: 1
  - **rqdata_is_st_early_flip_discrepancy_days**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `prior-st-2021-fund-occupation`
- `full-removal-2021-approved`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_repeat_st_governance_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002168.XSHE
  - **ticker**: 002168
  - **name_as_of**: ST惠程
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-04-08
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - is_st
    - special_treatment_info
    - symbol_change
  - **row_policy**: stock_code=002168.XSHE; as_of=full-removal announcement info_date 2021-04-08; prediction starts at official full-removal change_date 2021-04-09; window_end=same month/day plus 4 calendar years, inclusive
  - **episode_rule**: Sort daily is_st by stock/date. A new episode starts only on False-to-True after a prior False interval; ST-to-*ST, *ST-to-ST, additive warnings and partial removal inside an uninterrupted True interval are one episode. Official announcement change_date is label authority.
  - **governance_matching_axis**: controller and chairman changed after as_of; matching feature only, not a management-quality label
  - **matching_group**: full-removal-repeat-st-48m-v1
  - **matching_role**: event/control_change
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **prior_st_notice**: dd6b96e80d3d50dcb504b0f7d86897be967d9a2f3c23252c80515f09e0e615fb
    - **full_removal_notice**: 7ac498f4d5f799406940d6dcc5a92e206f41fca7881cdbae486009261ee0e023
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
    - **title**: 惠程科技关于公司股票被实施其他风险警示暨股票停复牌的提示性公告
    - **published_at**: 2024-09-14
    - **effective_change_date**: 2024-09-19
    - **url**: https://static.cninfo.com.cn/finalpage/2024-09-14/1221223182.PDF
    - **sha256**: b419f2f1ec09a34e512b82be8286465f6285ca31f68ba8ab08e013ef524f5604
    - **prior_full_removal_effective_date**: 2021-04-09
    - **new_independent_episode**: true
  - **item 2**:
    - **type**: rqdata_status_transition_crosscheck_with_suspension_discrepancy
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2021-04-09/2025-04-09
    - **official_new_episode_change_dates**:
      - 2024-09-19
    - **is_st_first_true_date**: 2024-09-18
    - **discrepancy_note**: 2024-09-18 was the suspension day; official warning and resumed trading took effect 2024-09-19, which controls the label
    - **episode_count**: 1

</details>

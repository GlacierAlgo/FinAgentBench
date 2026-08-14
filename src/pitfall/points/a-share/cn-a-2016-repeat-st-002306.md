# cn-a-2016-repeat-st-002306

## Question

你处在2016-05-13收盘后的信息环境。交易所已批准*ST云网撤销全部退市风险警示和其他风险警示，2016-05-16生效。请基于冻结证据预测：自该生效日起至2020-05-16（含）是否会开始新的独立ST或*ST episode。请区分历史戴帽原因是否真正消除、经营可持续性与控制治理变化；不要把同一episode内*ST降为ST或叠加警示误算为复发。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST云网 (002306, SZSE)
- 信息截止 / As of: 2016-05-13
- 预测窗口结束 / Window end: 2020-05-16
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 判定定义 / Definition: 公司股票完整撤销全部ST或*ST风险警示正式生效后48个自然月内，是否至少开始一次新的、独立的ST或*ST风险警示episode。只有此前已完整退出风险警示状态后再次正式进入才计数；同一episode内ST与*ST互转、叠加警示或部分撤销不另计。

#### 判定条件 / Criteria

- `new_independent_st_episode_count_48m >= 1` — 完整摘除全部风险警示生效后48个自然月内，至少开始一次新的独立ST或*ST episode

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 中科云网关于股票交易实行退市风险警示的公告

- Evidence ID: `prior-st-2015-operating-loss`
- 发布日期 / Published: 2015-04-29
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2015-04-29/1200935442.PDF

公司连续两个会计年度经审计净利润为负，股票自2015年4月30日起被实施退市风险警示。该触发源于持续经营亏损而非单一行政手续，提示完整摘帽后仍需判断盈利基础能否延续。

### 中科云网撤销退市风险警示及其他风险警示公告

- Evidence ID: `full-removal-2016-approved`
- 发布日期 / Published: 2016-05-13
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2016-05-13/1202319588.PDF

深交所同意公司撤销全部退市风险警示和其他风险警示；2016年5月16日继续停牌、不复牌，但撤销风险警示及证券简称恢复为中科云网自该日生效。这是完整退出风险警示状态，故48个月预测时钟从2016年5月16日起算。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 结果日期 / Resolved at: 2017-04-27
- 可观察日期 / Observed at: 2017-04-26

### 实际结果 / Realized outcome

- **observations**:
  - **new_independent_st_episode_count_48m**: 1
  - **full_removal_effective_before_new_episode**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `prior-st-2015-operating-loss`
- `full-removal-2016-approved`

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
  - **name_as_of**: *ST云网
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2016-05-13
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - is_st
    - special_treatment_info
    - symbol_change
  - **row_policy**: stock_code=002306.XSHE; as_of=full-removal announcement info_date 2016-05-13; prediction starts at official full-removal change_date 2016-05-16; window_end=same month/day plus 4 calendar years, inclusive
  - **episode_rule**: Sort daily is_st by stock/date. A new episode starts only on False-to-True after a prior False interval; ST-to-*ST, *ST-to-ST, additive warnings and partial removal inside an uninterrupted True interval are one episode. Official announcement change_date is label authority.
  - **governance_matching_axis**: control/management continuity or change is a matched analysis feature, never a good-management/bad-management label
  - **matching_group**: full-removal-repeat-st-48m-v1
  - **matching_role**: event/control_change_later
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **prior_st_notice**: 4c2af70783b48764023bd235a7523d1486d99dcba15caa3fffe2649c4d679921
    - **full_removal_notice**: 7fe8062688237f8c96b61d9257330762b3012d72e50e128792fc4c169fa1543a
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
    - **title**: 中科云网关于公司股票交易被实行退市风险警示暨停牌的公告
    - **published_at**: 2017-04-26
    - **effective_change_date**: 2017-04-27
    - **trigger**: 2016年度经审计期末净资产为负值
    - **url**: https://static.cninfo.com.cn/finalpage/2017-04-26/1203386418.PDF
    - **sha256**: 65cb95ae32d75815de75352a3313131dc051d3feeb74f01d1e8cb76bda9fcd47
    - **prior_full_removal_effective_date**: 2016-05-16
    - **new_independent_episode**: true
    - **distinction**: 2017-06-08银行账户被冻结所触发的其他风险警示属于同一已开始episode的后续叠加，不是本事件
  - **item 2**:
    - **type**: rqdata_status_transition_crosscheck
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2016-05-16/2020-05-16
    - **official_new_episode_change_dates**:
      - 2017-04-27
    - **episode_count**: 1

</details>

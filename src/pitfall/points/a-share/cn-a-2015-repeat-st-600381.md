# cn-a-2015-repeat-st-600381

## Question

你处在2015-02-09收盘后的信息环境。交易所已批准*ST贤成撤销全部风险警示，2015-02-10生效。请预测至2019-02-10（含）是否会开始新的独立ST或*ST episode。请判断重整和资产置换是否真正修复持续经营及治理基础，避免把更名或单次盈利当成充分条件。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST贤成 (600381, SSE)
- 信息截止 / As of: 2015-02-09
- 预测窗口结束 / Window end: 2019-02-10
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 判定定义 / Definition: 公司股票完整撤销全部ST或*ST风险警示正式生效后48个自然月内，是否至少开始一次新的、独立的ST或*ST风险警示episode。只有此前已完整退出风险警示状态后再次正式进入才计数；同一episode内ST与*ST互转、叠加警示或部分撤销不另计。

#### 判定条件 / Criteria

- `new_independent_st_episode_count_48m >= 1` — 完整摘除全部风险警示生效后48个自然月内，至少开始一次新的独立ST或*ST episode

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 青海贤成矿业股份有限公司关于公司股票交易实施其他风险警示的公告

- Evidence ID: `prior-st-2013-operating-warning`
- 发布日期 / Published: 2013-03-05
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2013-03-05/62181913.PDF

2012年煤炭行业低迷、安全检查及资金困难导致四家煤炭子公司全部或间歇停工，华阳煤业和光富矿业预计三个月内难以恢复；公司还涉及大量借款、担保诉讼，资产及募集资金被冻结、查封。因生产经营活动受到严重影响且预计三个月内不能恢复正常，上交所自2013年3月6日起实施其他风险警示，简称变为ST贤成。此后债务重整和资产调整能否真正恢复持续经营，不能由更名或重整完成本身替代判断。

### 贤成矿业关于撤销公司股票退市风险警示的公告

- Evidence ID: `full-removal-2015-approved`
- 发布日期 / Published: 2015-02-09
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2015-02-09/1200620458.PDF

上交所同意撤销公司股票全部风险警示，2015年2月10日起生效。公告确认了规则层面的完整摘帽；经历重整后的盈利结构、内部控制和新业务稳定性仍需作为未来48个月独立复发概率的核心输入。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `new_independent_st_episode_within_48m_after_full_removal`
- 结果日期 / Resolved at: 2016-06-29
- 可观察日期 / Observed at: 2016-06-28

### 实际结果 / Realized outcome

- **observations**:
  - **new_independent_st_episode_count_48m**: 1
  - **full_removal_effective_before_new_episode**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `prior-st-2013-operating-warning`
- `full-removal-2015-approved`

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
  - **name_as_of**: *ST贤成
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2015-02-09
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - is_st
    - special_treatment_info
    - symbol_change
  - **row_policy**: stock_code=600381.XSHG; as_of=full-removal announcement info_date 2015-02-09; prediction starts at official full-removal change_date 2015-02-10; window_end=same month/day plus 4 calendar years, inclusive
  - **episode_rule**: Sort daily is_st by stock/date. A new episode starts only on False-to-True after a prior False interval; ST-to-*ST, *ST-to-ST, additive warnings and partial removal inside an uninterrupted True interval are one episode. Official announcement change_date is label authority.
  - **governance_matching_axis**: post-restructuring controller/chairman continuity; matching feature only, not a management-quality label
  - **matching_group**: full-removal-repeat-st-48m-v1
  - **matching_role**: event/control_continuity
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **prior_st_notice**: 637c635b000cbf143e08bf9f52bbf02ab7d5368a1b6a4fe9ecd2366e4b1dfeda
    - **full_removal_notice**: 216c622f4f660d01374cc9f332d9adc5282b329737d2b008429df727e21682c9
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
    - **title**: 青海春天关于公司股票实施其他风险警示暨股票复牌的公告
    - **published_at**: 2016-06-28
    - **effective_change_date**: 2016-06-29
    - **url**: https://static.cninfo.com.cn/finalpage/2016-06-28/1202419344.PDF
    - **sha256**: 3e5a1df2c55f00ea3435147ef373be27dee92860305ab8401e94c4365acc25e7
    - **prior_full_removal_effective_date**: 2015-02-10
    - **new_independent_episode**: true
  - **item 2**:
    - **type**: rqdata_status_transition_crosscheck
    - **paths**:
      - data/db/special_treatment_info.parquet
      - data/db/is_st.parquet
    - **source_sha256**:
      - **special_treatment_info**: 7bb080a0efec221f39ed0d890c289d29cd3a25088cb867903b8f240fad63846f
      - **is_st**: 5719cc47e294e146e64d901338a88f3169e3d3b4df29a52d0b5e37c6fcbf3af8
    - **window**: 2015-02-10/2019-02-10
    - **official_new_episode_change_dates**:
      - 2016-06-29
    - **episode_count**: 1

</details>

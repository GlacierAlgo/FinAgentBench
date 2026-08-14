# cn-a-2019-governance-fund-recovery-600290

## Question

你处在2019-12-26收盘后的信息环境。ST华仪公告关联方资金占用余额10.58亿元，控股股东承诺一个月内解决但已违约，同时还存在大额违规担保。请使用冻结搜索材料，预测未来13个自然月内是否达到target定义的全额现金清偿。区分账面资产、控股股东口头或书面方案与上市公司真实现金回收，评估控制人偿付网络和治理执行力；控制人或管理层延续只能用于推理，不能替代字面事件。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST华仪 (600290, SSE)
- 信息截止 / As of: 2019-12-26
- 预测窗口结束 / Window end: 2021-01-26
- 目标事件 / Target: `full_scoped_non_operating_fund_occupation_cash_recovery_13m`
- 判定定义 / Definition: 快照日公告量化的全部非经营性资金占用本金，以及快照日已明确应付的资金占用利息，在13个自然月窗口内均以现金实际进入上市公司账户。仅有还款承诺、筹资方案、股权拍卖安排、司法裁定但未到账、资产抵债或部分回款均不计；窗口后到账不计。

#### 判定条件 / Criteria

- `full_scoped_fund_occupation_cash_recovery_count_13m >= 1` — 窗口内所有快照范围本金及快照日已明确应付利息均以现金到账，完整清偿事件至少一次

<details>
<summary>冻结资料 / Frozen evidence (1)</summary>

### 华仪电气实施其他风险警示：10.58亿元关联方占用与控股股东承诺失约

- Evidence ID: `snapshot-st-fund-occupation`
- 发布日期 / Published: 2019-12-25
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2019-12-25/1207191681.PDF

公司公告股票自2019年12月26日起变更为ST华仪。自查发现关联方资金占用余额合计10.58亿元，占最近一期经审计净资产26.00%；另有违规担保92,590万元，其中逾期对外担保21,400万元。控股股东未在2019年11月25日起一个月的承诺期内解决资金占用和违规担保。董事会只能表示持续督促、催促偿债并争取通过法律途径处理，没有披露占用款现金回收。快照把高额占用、同一控制人网络的担保连带风险和首轮承诺失约同时摆在预测者面前。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `full_scoped_non_operating_fund_occupation_cash_recovery_13m`
- 结果日期 / Resolved at: 2021-01-26
- 可观察日期 / Observed at: 2021-02-23

### 实际结果 / Realized outcome

- **observations**:
  - **full_scoped_fund_occupation_cash_recovery_count_13m**: 0
  - **fund_occupation_balance_yuan_at_observation**: 1141025100
  - **cash_repayment_received_flag_at_observation**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `snapshot-st-fund-occupation`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_governance_obligation_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600290.XSHG
  - **ticker**: 600290
  - **name_as_of**: ST华仪
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-12-26
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_basic_info.parquet
    - symbol_change.parquet
    - special_treatment_info.parquet
  - **row_policy**: 600290.XSHG identity and the 2019-12-26 first ST effective date were checked point-in-time; official issuer filings remain label authority
  - **matching_group**: governance-fund-occupation-cash-recovery-13m-v1
  - **matching_role**: no_event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **snapshot_st_notice**: d6aad276b1294a65a1bfaaa71f7591236bb680d8f10c04e972b916147f43bc67
  - **outcome_contract**: Only actual cash receipt of every snapshot-scoped principal amount and snapshot-explicit occupation interest by 2021-01-26 counts.
  - **leakage_guard**: Later repayment progress, restructuring, enforcement losses and risk-warning status remain label-side only. Controller or management continuity is an analysis feature, never a criterion.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_monthly_fund_occupation_progress
    - **title**: 华仪电气关于控股股东资金占用及违规担保事项的进展公告
    - **published_at**: 2021-02-23
    - **url**: https://static.cninfo.com.cn/finalpage/2021-02-23/1209289889.PDF
    - **result**: 窗口结束后的第一份月度进展公告仍披露关联方资金占用余额1,141,025,100元，并明确公司截至公告日尚未收到任何归还款项，因此不可能在2021-01-26前完成快照范围全额现金清偿。
    - **extraction**:
      - **tool**: run-llama/liteparse
      - **version**: 2.11.1
      - **git_commit**: 5109b46e7f960a52ea9833704c9484c835c6ef4f
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 4764adb8ce7b89ce640c62e517be4c4fa9b95572a9123fab04bba2a6ff2106ed

</details>

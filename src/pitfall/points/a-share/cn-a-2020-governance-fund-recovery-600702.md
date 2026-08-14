# cn-a-2020-governance-fund-recovery-600702

## Question

你处在2020-09-22收盘后的信息环境。ST舍得公告的快照范围为天洋控股及关联方占用本金4.4亿元和已明确利息3,486万元，承诺期限已经落空。请使用冻结搜索材料，预测未来13个自然月内是否达到target定义的全额现金清偿。评估控制人资产与股权的可执行性、公司治理和追索路径；不要把筹资承诺、股权转让或拍卖安排当成现金到账，也不要把控制权是否延续写进事件标准。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST舍得 (600702, SSE)
- 信息截止 / As of: 2020-09-22
- 预测窗口结束 / Window end: 2021-10-22
- 目标事件 / Target: `full_scoped_non_operating_fund_occupation_cash_recovery_13m`
- 判定定义 / Definition: 快照日公告量化的全部非经营性资金占用本金，以及快照日已明确应付的资金占用利息，在13个自然月窗口内均以现金实际进入上市公司账户。仅有还款承诺、筹资方案、股权拍卖安排、司法裁定但未到账、资产抵债或部分回款均不计；窗口后到账不计。

#### 判定条件 / Criteria

- `full_scoped_fund_occupation_cash_recovery_count_13m >= 1` — 窗口内所有快照范围本金及快照日已明确应付利息均以现金到账，完整清偿事件至少一次

<details>
<summary>冻结资料 / Frozen evidence (1)</summary>

### 舍得酒业实施其他风险警示：4.4亿元本金及3,486万元利息逾期未归还

- Evidence ID: `snapshot-st-fund-occupation`
- 发布日期 / Published: 2020-09-21
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-09-21/1208462729.PDF

公司公告股票自2020年9月22日起变更为ST舍得。经自查并经会计师确认，截至2020年8月19日，间接控股股东天洋控股及其关联方非经营性占用本金44,000.00万元、资金占用利息3,486.00万元，合计47,486.00万元；截至公告日仍未在2020年9月19日承诺期限前归还。董事会提出继续督促筹资、制定还款计划并通过股权转让等方式弥补，但没有披露任何现金已到账。该快照同时显示问题集中于一个控制人网络、金额已明确、承诺已首次失约；未来是否清偿取决于可执行资产和追索能否转化为上市公司账户中的现金。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `full_scoped_non_operating_fund_occupation_cash_recovery_13m`
- 结果日期 / Resolved at: 2021-01-08
- 可观察日期 / Observed at: 2021-01-09

### 实际结果 / Realized outcome

- **observations**:
  - **full_scoped_fund_occupation_cash_recovery_count_13m**: 1
  - **snapshot_scoped_principal_yuan**: 440000000
  - **snapshot_explicit_interest_yuan**: 34860000
  - **cash_received_yuan**: 484172652
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
  - **order_book_id**: 600702.XSHG
  - **ticker**: 600702
  - **name_as_of**: ST舍得
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-09-22
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_basic_info.parquet
    - symbol_change.parquet
    - special_treatment_info.parquet
  - **row_policy**: 600702.XSHG identity and the 2020-09-22 first ST effective date were checked point-in-time; official issuer filings remain label authority
  - **matching_group**: governance-fund-occupation-cash-recovery-13m-v1
  - **matching_role**: event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **snapshot_st_notice**: 00e8cf1a291dab92d5da6512a9e9042dab657f9cf75e205402d908d0c313929c
  - **outcome_contract**: Only actual cash receipt of every snapshot-scoped principal amount and snapshot-explicit occupation interest by 2021-10-22 counts.
  - **leakage_guard**: Court enforcement, cash receipts, controller auction results and later risk-warning changes remain label-side only. Controller or management continuity is an analysis feature, never a criterion.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_fund_recovery_progress
    - **title**: 舍得酒业关于天洋控股集团有限公司及其关联方资金占用事项的进展公告
    - **published_at**: 2021-01-09
    - **url**: https://static.cninfo.com.cn/finalpage/2021-01-09/1209077643.PDF
    - **result**: 四川省遂宁市中级人民法院从天洋控股所持沱牌舍得集团70%股权拍卖款中先予划转资金占用款及资金占用费等484,172,652元，公司于2021-01-08收到；金额覆盖快照量化的4.4亿元本金和3,486万元利息。
    - **extraction**:
      - **tool**: run-llama/liteparse
      - **version**: 2.11.1
      - **git_commit**: 5109b46e7f960a52ea9833704c9484c835c6ef4f
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 7c64e6d7bb65e38aa01aeaea491de852d64e7a1387e56855320448379bdb7e14

</details>

# cn-a-2022-governance-cash-compensation-300709

## Question

你处在2022-05-06收盘后的信息环境。精研科技收购安特信60%股权后，2021年度应补偿现金204,344,405.48元；合同允许从9,000万元应付未付交易款中直接扣除，但其余部分尚在磋商，且补偿额已超过交易作价。请使用冻结搜索材料，预测未来12个自然月内是否达到target定义的全额完成。区分合同授权且不可撤销的抵扣、真实现金到账与仅在谈判中的方案，并权衡原股东继续承担经营管理对追偿强度的影响；人员连续性不能进入事件标准。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 精研科技 (300709, SZSE)
- 信息截止 / As of: 2022-05-06
- 预测窗口结束 / Window end: 2023-05-06
- 目标事件 / Target: `full_scoped_cash_performance_compensation_completion_12m`
- 判定定义 / Definition: 快照日公告量化的业绩补偿现金本金及届时合同明确要求的逾期利息或违约金，在12个自然月内全部实际到账；仅允许将合同明示授权且已不可撤销完成的应付未付交易价款抵扣计入完成。承诺、展期、诉讼或保全、还款计划、协商或部分支付均不计；窗口后完成不计。

#### 判定条件 / Criteria

- `full_scoped_cash_performance_compensation_completion_count_12m >= 1` — 窗口内快照范围现金补偿本金及合同要求的逾期利息或违约金全部完成，完整履约事件至少一次

<details>
<summary>冻结资料 / Frozen evidence (1)</summary>

### 精研科技披露安特信2021年度业绩补偿进展：2.043亿元义务仍在磋商

- Evidence ID: `snapshot-2021-cash-compensation-progress`
- 发布日期 / Published: 2022-05-06
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2022-05-06/1213282480.PDF

精研科技以1.8亿元现金收购安特信60%股权。安特信2021年扣非净利润为-57,737,762.19元，未完成承诺，按股权转让协议计算应补偿204,344,405.48元。协议明示公司有权从9,000万元应付未付交易款中直接扣除同额补偿，公司已将该9,000万元确认为金融资产；剩余补偿尚在磋商，原股东没有提出最终解决方案。公告称补偿额超过安特信60%股权交易作价，交易对方实际收到的款项更低，部分补偿可能无法收回；公司还把原股东构成的管理团队稳定和标的持续经营列为协商考量。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `full_scoped_cash_performance_compensation_completion_12m`
- 结果日期 / Resolved at: 2023-05-06
- 可观察日期 / Observed at: 2023-05-30

### 实际结果 / Realized outcome

- **observations**:
  - **full_scoped_cash_performance_compensation_completion_count_12m**: 0
  - **snapshot_scoped_2021_compensation_yuan**: 204344405.48
  - **contract_authorized_offset_yuan**: 90000000
  - **cash_compensation_received_yuan**: 7100000
  - **minimum_uncompleted_snapshot_scope_yuan**: 107244405.48
- **derivations**:


### 对应的题内资料 / Expected evidence

- `snapshot-2021-cash-compensation-progress`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_governance_obligation_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 300709.XSHE
  - **ticker**: 300709
  - **name_as_of**: 精研科技
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2022-05-06
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_basic_info.parquet
  - **row_policy**: 300709.XSHE point-in-time security identity was cross-checked; official issuer filings remain label authority
  - **matching_group**: governance-cash-performance-compensation-completion-12m-v1
  - **matching_role**: no_event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **snapshot_compensation_progress**: 4d0adeb45f63b0aa1d7ad28554db1382da80a688553a9b9ce5c5f50b315c4918
  - **outcome_contract**: All snapshot-scoped 2021 cash compensation, after only a completed contract-authorized offset, must be actually received by 2023-05-06.
  - **leakage_guard**: Subsequent partial payments, repayment proposals, litigation and later-year compensation remain label-side only. Controller, management or seller continuity is an analysis feature, never a criterion.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_compensation_progress_after_window
    - **title**: 精研科技关于深圳市安特信技术有限公司2022年度业绩承诺实现情况及业绩补偿的进展公告
    - **published_at**: 2023-05-30
    - **url**: https://static.cninfo.com.cn/finalpage/2023-05-30/1216931959.PDF
    - **result**: 窗口结束后的首份专项进展只确认合同授权抵扣9,000万元和累计现金支付710万元，合计9,710万元，低于快照所列2021年度补偿204,344,405.48元；公告仍称原股东未达成最终方案。因此至少107,244,405.48元快照范围义务未完成。
    - **extraction**:
      - **tool**: run-llama/liteparse
      - **version**: 2.11.1
      - **git_commit**: 5109b46e7f960a52ea9833704c9484c835c6ef4f
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 5c17121049b4a81e2b328256733a97c2a97ff6305b454a3f9f5b9a48fd5f2947

</details>

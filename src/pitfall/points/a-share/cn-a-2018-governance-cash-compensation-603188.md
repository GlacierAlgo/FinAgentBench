# cn-a-2018-governance-cash-compensation-603188

## Question

你处在2018-08-21收盘后的信息环境。亚邦股份收购江苏道博的17名转让方应支付2,322.31万元现金补偿，快照时只收到300万元，剩余款因个人财务原因被展期至年末，并约定逾期利息与后续违约金。请使用冻结搜索材料，预测未来12个自然月内是否达到target定义的全额完成。评估多义务人连带偿付能力、既有小额付款的信号价值和诉讼威慑；不能把展期承诺或部分到账当作完成。管理层或原股东连续性只作分析特征。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST亚邦 (603188, SSE)
- 信息截止 / As of: 2018-08-21
- 预测窗口结束 / Window end: 2019-08-21
- 目标事件 / Target: `full_scoped_cash_performance_compensation_completion_12m`
- 判定定义 / Definition: 快照日公告量化的业绩补偿现金本金及届时合同明确要求的逾期利息或违约金，在12个自然月内全部实际到账；仅允许将合同明示授权且已不可撤销完成的应付未付交易价款抵扣计入完成。承诺、展期、诉讼或保全、还款计划、协商或部分支付均不计；窗口后完成不计。

#### 判定条件 / Criteria

- `full_scoped_cash_performance_compensation_completion_count_12m >= 1` — 窗口内快照范围现金补偿本金及合同要求的逾期利息或违约金全部完成，完整履约事件至少一次

<details>
<summary>冻结资料 / Frozen evidence (1)</summary>

### 亚邦股份收到部分业绩补偿款：17名转让方获准延期并承担逾期利息

- Evidence ID: `snapshot-cash-compensation-extension`
- 发布日期 / Published: 2018-08-21
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2018-08-21/1205308764.PDF

公司以4.5亿元现金收购江苏道博100%股权，2017年标的扣非净利润4,318.03万元，仅完成承诺的74.45%。17名自然人转让方按协议应现金补偿3,933.28万元，扣除尚未支付的股权转让款1,610.97万元后仍应付2,322.31万元。快照时公司只收到其中一名转让方张华支付的300万元；其余义务人以个人财务原因为由未能按时全付，并承诺在2018年12月31日前支付全部2,322.31万元及自2018年6月3日起计算的逾期利息，逾期后还将按日万分之六承担违约金。公司称届时未清偿将诉诸法律。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `full_scoped_cash_performance_compensation_completion_12m`
- 结果日期 / Resolved at: 2019-01-09
- 可观察日期 / Observed at: 2019-01-11

### 实际结果 / Realized outcome

- **observations**:
  - **full_scoped_cash_performance_compensation_completion_count_12m**: 1
  - **cash_compensation_and_interest_received_yuan**: 23672500
  - **contractual_penalty_received_yuan**: 51100
- **derivations**:


### 对应的题内资料 / Expected evidence

- `snapshot-cash-compensation-extension`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_governance_obligation_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 603188.XSHG
  - **ticker**: 603188
  - **name_as_of**: ST亚邦
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2018-08-21
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_basic_info.parquet
  - **row_policy**: 603188.XSHG point-in-time security identity was cross-checked; official issuer filings remain label authority
  - **matching_group**: governance-cash-performance-compensation-completion-12m-v1
  - **matching_role**: event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **snapshot_compensation_progress**: c852024e01ebec29a4d9c04a20f59720eff0235b8bccdf3048e51f45ab3a4944
  - **outcome_contract**: All snapshot-scoped cash compensation plus contractually required interest and penalty must be actually received by 2019-08-21.
  - **leakage_guard**: Subsequent payments, litigation actions and withdrawal remain label-side only. Controller, management or seller continuity is an analysis feature, never a criterion.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_cash_compensation_completion
    - **title**: 亚邦股份关于收到部分业绩补偿款的进展公告
    - **published_at**: 2019-01-11
    - **url**: https://static.cninfo.com.cn/finalpage/2019-01-11/1205733584.PDF
    - **result**: 公司于2019-01-09收到剩余补偿款及逾期利息1,066.48万元和违约金5.11万元；累计收到2017年度业绩补偿款及逾期利息2,367.25万元、违约金5.11万元，公告明确17名转让方的业绩承诺及补偿义务全部履行完毕。
    - **extraction**:
      - **tool**: run-llama/liteparse
      - **version**: 2.11.1
      - **git_commit**: 5109b46e7f960a52ea9833704c9484c835c6ef4f
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 74cb693be5d5c91529c9dd0cdf9c694251576c33f0f4437d86a5a30b0006f67d

</details>

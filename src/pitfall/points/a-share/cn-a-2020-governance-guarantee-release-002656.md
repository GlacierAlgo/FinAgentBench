# cn-a-2020-governance-guarantee-release-002656

## Question

你处在2020-01-13收盘后的信息环境。ST摩登披露四笔越权关联担保中仅一笔解除，剩余三笔合计3.3亿元且未含利息等费用，责任形式和债权人各不相同。请使用冻结搜索材料，预测未来13个自然月内是否达到target定义的全部担保解除。逐笔考虑诉讼和债权网络、控股股东可执行资源及治理执行力，不能把单笔胜诉、部分解除、反担保或协商方案外推为全量归零；控制人或管理层延续只用于推理。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST摩登 (002656, SZSE)
- 信息截止 / As of: 2020-01-13
- 预测窗口结束 / Window end: 2021-02-13
- 目标事件 / Target: `full_scoped_illegal_related_guarantee_release_13m`
- 判定定义 / Definition: 快照日公告量化且未解除的全部违规关联担保，在13个自然月内均取得使上市公司残余法律担保暴露归零的有效判决、债权人书面解除或其他官方生效文件。清偿或和解计划、融资额度、反担保或质押、提起诉讼、部分付款或部分解除均不计；窗口后解除不计。

#### 判定条件 / Criteria

- `full_scoped_illegal_guarantee_release_count_13m >= 1` — 窗口内所有快照范围违规关联担保的上市公司残余法律暴露归零，完整解除事件至少一次

<details>
<summary>冻结资料 / Frozen evidence (1)</summary>

### 摩登大道实施其他风险警示：三笔合计3.3亿元违规关联担保尚未解除

- Evidence ID: `snapshot-st-illegal-guarantees`
- 发布日期 / Published: 2020-01-10
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-01-10/1207237985.PDF

公司公告股票自2020年1月13日起变更为ST摩登。四笔未经审议、未及时披露的关联担保中，广州连卡福为花园里公司对厦门国际银行10,570万元借款提供的有限责任担保已解除；其余三笔未解除，分别为立嘉小贷对立根小贷8,000万元连带责任担保、广州连卡福为花园里公司对澳门国际银行10,000万元有限责任担保、公司为林永飞对周志聪15,000万元借款提供的连带责任担保，未解除余额合计33,000万元且未含利息等费用。董事会仅表示督促被担保人筹资并通过司法途径解决，三笔不同债权关系必须逐笔归零。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `full_scoped_illegal_related_guarantee_release_13m`
- 结果日期 / Resolved at: 2021-02-13
- 可观察日期 / Observed at: 2021-04-16

### 实际结果 / Realized outcome

- **observations**:
  - **full_scoped_illegal_guarantee_release_count_13m**: 0
  - **residual_illegal_guarantee_balance_yuan_at_observation**: 322852860.97
  - **residual_listed_company_legal_guarantee_exposure_flag**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `snapshot-st-illegal-guarantees`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_governance_obligation_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002656.XSHE
  - **ticker**: 002656
  - **name_as_of**: ST摩登
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-01-13
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_basic_info.parquet
    - symbol_change.parquet
    - special_treatment_info.parquet
  - **row_policy**: 002656.XSHE identity and the 2020-01-13 first ST effective date were checked point-in-time; official creditor, court and issuer documents remain label authority
  - **matching_group**: governance-illegal-guarantee-full-release-13m-v1
  - **matching_role**: no_event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **snapshot_st_notice**: 09d3b381eac2bfecf8ef504fb3203b2f3dadfe0f0b676e072d67bcc9885e66e2
  - **outcome_contract**: Every quantified unresolved illegal related-party guarantee in the snapshot must have zero residual listed-company legal exposure by 2021-02-13.
  - **leakage_guard**: Subsequent judgments, releases, annual-report balances and risk-warning changes remain label-side only. Controller or management continuity is an analysis feature, never a criterion.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_2020_annual_report
    - **title**: 摩登大道时尚集团股份有限公司2020年年度报告全文
    - **published_at**: 2021-04-16
    - **url**: https://static.cninfo.com.cn/finalpage/2021-04-16/1209704481.PDF
    - **result**: 年报在窗口结束后披露截至报告披露日违规担保余额仍为322,852,860.97元，四项关联担保在期末关联担保表中均列为未履行完毕，故快照范围不可能已在2021-02-13前全部解除。
    - **extraction**:
      - **tool**: run-llama/liteparse
      - **version**: 2.11.1
      - **git_commit**: 5109b46e7f960a52ea9833704c9484c835c6ef4f
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 2ca0547e1797694d6c7fe551d80883ba389559d26e842188c5808f1616f50386

</details>

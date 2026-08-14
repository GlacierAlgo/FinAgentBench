# cn-a-2020-governance-guarantee-release-002650

## Question

你处在2020-06-15收盘后的信息环境。ST加加公告仍有4.6605亿元违规担保；控股股东声称取得2.8亿元专项资金额度，并已与两个主要债权人签署清偿或和解协议，但条件尚未实际成就。请使用冻结搜索材料，预测未来13个自然月内是否达到target定义的全部担保解除。重点判断资金安排、协议条件、债权人确认和法律暴露，而不是把签约或反担保当成解除；控制人连续性仅作分析特征。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST加加 (002650, SZSE)
- 信息截止 / As of: 2020-06-15
- 预测窗口结束 / Window end: 2021-07-15
- 目标事件 / Target: `full_scoped_illegal_related_guarantee_release_13m`
- 判定定义 / Definition: 快照日公告量化且未解除的全部违规关联担保，在13个自然月内均取得使上市公司残余法律担保暴露归零的有效判决、债权人书面解除或其他官方生效文件。清偿或和解计划、融资额度、反担保或质押、提起诉讼、部分付款或部分解除均不计；窗口后解除不计。

#### 判定条件 / Criteria

- `full_scoped_illegal_guarantee_release_count_13m >= 1` — 窗口内所有快照范围违规关联担保的上市公司残余法律暴露归零，完整解除事件至少一次

<details>
<summary>冻结资料 / Frozen evidence (1)</summary>

### 加加食品实施其他风险警示：4.6605亿元违规担保与有条件和解安排

- Evidence ID: `snapshot-st-illegal-guarantees`
- 发布日期 / Published: 2020-06-12
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-06-12/1207919359.PDF

公司公告股票自2020年6月15日起变更为ST加加，快照日违规对外担保本金余额合计46,605万元，占最近一期经审计净资产19.94%，一个月整改期已经届满。公告同时披露控股股东获得第三方2.8亿元专项资金额度，并分别与湖南三湘银行、优选资本签署债务清偿或和解协议：只有首笔清偿款在2020年6月30日前付至债权人指定账户后，上市公司相关担保义务与责任才解除。因而融资额度和签约是强烈的正向前置信号，但在条件实际成就及债权人确认前都不是法律暴露归零。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `full_scoped_illegal_related_guarantee_release_13m`
- 结果日期 / Resolved at: 2020-06-30
- 可观察日期 / Observed at: 2020-07-01

### 实际结果 / Realized outcome

- **observations**:
  - **full_scoped_illegal_guarantee_release_count_13m**: 1
  - **snapshot_scoped_illegal_guarantee_principal_yuan**: 466050000
  - **residual_listed_company_legal_guarantee_exposure_flag**: 0
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
  - **order_book_id**: 002650.XSHE
  - **ticker**: 002650
  - **name_as_of**: ST加加
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-06-15
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_basic_info.parquet
    - symbol_change.parquet
    - special_treatment_info.parquet
  - **row_policy**: 002650.XSHE identity and the 2020-06-15 first ST effective date were checked point-in-time; official creditor and issuer documents remain label authority
  - **matching_group**: governance-illegal-guarantee-full-release-13m-v1
  - **matching_role**: event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **snapshot_st_notice**: fdb701da870263744592c52572bd2585a6e1ece51448874a9fd19f80e44b1ef6
  - **outcome_contract**: Every quantified unresolved illegal related-party guarantee in the snapshot must have zero residual listed-company legal exposure by 2021-07-15.
  - **leakage_guard**: Subsequent creditor confirmations, settlement performance and risk-warning changes remain label-side only. Controller or management continuity is an analysis feature, never a criterion.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_creditor_release_confirmation
    - **title**: 加加食品关于解除违规担保的进展公告
    - **published_at**: 2020-07-01
    - **url**: https://static.cninfo.com.cn/finalpage/2020-07-01/1207977223.PDF
    - **result**: 优选资本于2020-06-30确认收到1.8亿元首笔清偿款，三湘银行同日出具担保责任解除确认函并确认第三方担保已签署；公告据两套协议和债权人文件确认加加食品及子公司对两方均不再负任何义务与责任，覆盖快照全部违规担保。
    - **extraction**:
      - **tool**: run-llama/liteparse
      - **version**: 2.11.1
      - **git_commit**: 5109b46e7f960a52ea9833704c9484c835c6ef4f
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 4454d81cff2eb050bc32420b3919a5028ad4ceb3fd86d18ad880df949ee25b88

</details>

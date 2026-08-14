# cn-a-2020-governance-share-compensation-300266

## Question

你处在2020-08-31收盘后的信息环境。兴源环境收购浙江源态形成的12名补偿义务人应补偿10,623,743股，股东大会通过方案后两个月期限已经届满但无人履行，浙江证监局已发监管关注函。请使用冻结搜索材料，预测未来24个自然月内是否达到target定义的全部补偿股份回购注销。分析股份锁定与可得性、义务人数量、监管和法律执行路径；不能把达成一致、批准方案或部分注销当成全量完成。现金分红返还不属于本题target，义务人或管理层连续性只作分析。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 兴源环境 (300266, SZSE)
- 信息截止 / As of: 2020-08-31
- 预测窗口结束 / Window end: 2022-08-31
- 目标事件 / Target: `full_scoped_share_performance_compensation_repurchase_cancellation_24m`
- 判定定义 / Definition: 快照日公告量化的全部业绩补偿股份，在24个自然月内均完成回购并在中国结算或其他官方登记中注销。达成一致、董事会或股东大会批准、监管催告、诉讼、判决、司法拍卖、重整方案、锁定期延长或仅部分回购注销均不计；窗口后完成不计。

#### 判定条件 / Criteria

- `full_scoped_share_compensation_repurchase_cancellation_count_24m >= 1` — 窗口内快照范围全部业绩补偿股份完成回购并在官方登记中注销，完整履约事件至少一次

<details>
<summary>冻结资料 / Frozen evidence (1)</summary>

### 兴源环境及12名补偿义务人收到监管关注函：1,062万股补偿超期未履行

- Evidence ID: `snapshot-share-compensation-regulatory-letter`
- 发布日期 / Published: 2020-08-31
- 来源 / Source: 巨潮资讯法定公告
- URL: https://static.cninfo.com.cn/finalpage/2020-08-31/1208358442.PDF

浙江源态2017至2019年累计未实现业绩承诺3,893.03万元。按盈利预测补偿协议，经纬中耀等12名原股东应补偿兴源环境10,623,743股并另行返还现金分红212,474.86元；2020年6月2日股东大会通过方案，合同要求两个月内回购注销对应股份。到监管关注函披露日，12名义务人仍未履行任何补偿义务。浙江证监局要求上市公司尽快采取法律手段、要求义务人提交具体履行方案；公司表示不排除诉讼。监管压力增强了执行可能，但函件、方案和未来诉讼本身均不是中国结算层面的注销完成。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `full_scoped_share_performance_compensation_repurchase_cancellation_24m`
- 结果日期 / Resolved at: 2021-06-24
- 可观察日期 / Observed at: 2021-06-26

### 实际结果 / Realized outcome

- **observations**:
  - **full_scoped_share_compensation_repurchase_cancellation_count_24m**: 1
  - **snapshot_scoped_compensation_shares**: 10623743
  - **repurchased_and_cancelled_shares**: 10623743
  - **final_batch_cancelled_shares**: 4861425
- **derivations**:


### 对应的题内资料 / Expected evidence

- `snapshot-share-compensation-regulatory-letter`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_governance_obligation_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 300266.XSHE
  - **ticker**: 300266
  - **name_as_of**: 兴源环境
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-08-31
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_basic_info.parquet
  - **row_policy**: 300266.XSHE point-in-time security identity was cross-checked; official issuer and CSDC-linked filings remain label authority
  - **matching_group**: governance-share-performance-compensation-cancellation-24m-v1
  - **matching_role**: event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **snapshot_regulatory_attention**: c52583e2c64bbaeca97d579f38f6d4813d755ae4f9074e29c52543171e0f70a8
  - **outcome_contract**: Every one of the 10,623,743 snapshot-scoped compensation shares must be repurchased and cancelled in official registration by 2022-08-31; cash-dividend return is deliberately outside this target.
  - **leakage_guard**: Subsequent agreements, partial and final CSDC cancellations and any dividend-return information remain label-side only. Controller, management or obligor continuity is an analysis feature, never a criterion.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_csdc_cancellation_completion
    - **title**: 兴源环境关于业绩承诺补偿股份剩余部分回购注销完成的公告
    - **published_at**: 2021-06-26
    - **url**: https://static.cninfo.com.cn/finalpage/2021-06-26/1210341092.PDF
    - **result**: 公告列明应补偿股份总数10,623,743股、首批五名义务人的股份已完成注销，并确认剩余七名义务人合计4,861,425股于2021-06-24在中国结算深圳分公司完成回购注销，故快照范围全部股份已注销。公告仅称现金分红返还已达成一致，并未证明收到；现金分红因此明确不属于本题label。
    - **extraction**:
      - **tool**: run-llama/liteparse
      - **version**: 2.11.1
      - **git_commit**: 5109b46e7f960a52ea9833704c9484c835c6ef4f
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: ae03019acad15a618eb304ccd769401a3f4d32c64a41f9eb5f09150f33b5e76d

</details>

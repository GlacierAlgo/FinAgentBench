# cn-a-2019-governance-share-compensation-600666

## Question

你处在2019-10-25收盘后的信息环境。*ST瑞德披露业绩未达标和减值合计应赔偿约40,277.21万股，已向各义务人发送通知但补偿超期；第一顺位义务人左洪波、褚淑霞持股全部冻结，上市公司同时存在债务违约和破产清算风险。请使用冻结搜索材料，预测未来24个自然月内是否达到target定义的全部补偿股份回购注销。综合义务规模、股份冻结、控制人资源、诉讼债权网络和治理执行力；不能把催告、锁定、拍卖或控制权变化当成注销。现金分红返还不属于本题target，控制人或管理层连续性只作分析。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: *ST瑞德 (600666, SSE)
- 信息截止 / As of: 2019-10-25
- 预测窗口结束 / Window end: 2021-10-25
- 目标事件 / Target: `full_scoped_share_performance_compensation_repurchase_cancellation_24m`
- 判定定义 / Definition: 快照日公告量化的全部业绩补偿股份，在24个自然月内均完成回购并在中国结算或其他官方登记中注销。达成一致、董事会或股东大会批准、监管催告、诉讼、判决、司法拍卖、重整方案、锁定期延长或仅部分回购注销均不计；窗口后完成不计。

#### 判定条件 / Criteria

- `full_scoped_share_compensation_repurchase_cancellation_count_24m >= 1` — 窗口内快照范围全部业绩补偿股份完成回购并在官方登记中注销，完整履约事件至少一次

<details>
<summary>冻结资料 / Frozen evidence (1)</summary>

### *ST瑞德2019年三季报：约4.0277亿股业绩及减值补偿超期未履行

- Evidence ID: `snapshot-q3-overdue-share-compensation`
- 发布日期 / Published: 2019-10-25
- 来源 / Source: 巨潮资讯法定季度报告
- URL: https://static.cninfo.com.cn/finalpage/2019-10-25/1207014294.PDF

三季报披露，按重大资产重组盈利预测补偿协议，业绩承诺方因承诺未完成需履行37,971.64万股业绩补偿，因注入资产期末减值需履行2,305.57万股估值补偿，合计约40,277.21万股；公司已于2019年9月24日向各义务人发送通知，但补偿超期未完成。第一顺位义务人兼实际控制人左洪波、褚淑霞所持233,223,515股和157,483,093股全部被冻结，个人资产权利受限；两人及一致行动人仍控制关键补偿股份。同期公司及子公司账户、资产和股权存在多轮司法冻结并已出现债务违约和破产清算风险，使得股份可执行性、控制权风险和上市公司治理执行相互纠缠。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `full_scoped_share_performance_compensation_repurchase_cancellation_24m`
- 结果日期 / Resolved at: 2021-10-25
- 可观察日期 / Observed at: 2022-04-23

### 实际结果 / Realized outcome

- **observations**:
  - **full_scoped_share_compensation_repurchase_cancellation_count_24m**: 0
  - **snapshot_scoped_compensation_shares_rounded**: 402772100
  - **performance_compensation_unperformed_flag_at_observation**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `snapshot-q3-overdue-share-compensation`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_governance_obligation_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600666.XSHG
  - **ticker**: 600666
  - **name_as_of**: *ST瑞德
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-10-25
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_basic_info.parquet
    - symbol_change.parquet
    - special_treatment_info.parquet
  - **row_policy**: 600666.XSHG identity and contemporaneous risk-warning name were checked point-in-time; official issuer and registration filings remain label authority
  - **matching_group**: governance-share-performance-compensation-cancellation-24m-v1
  - **matching_role**: no_event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **snapshot_2019_q3_report**: 9da83d7143cf7117ae514d566f5a68e6472a157184ce3829b6615cff98822d6d
  - **outcome_contract**: Every snapshot-scoped compensation share must be repurchased and cancelled in official registration by 2021-10-25; cash-dividend return is deliberately outside this target.
  - **leakage_guard**: Subsequent auctions, restructuring, control changes and later confirmations of nonperformance remain label-side only. Controller or management continuity is an analysis feature, never a criterion.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_2021_annual_report
    - **title**: 奥瑞德光电股份有限公司2021年年度报告
    - **published_at**: 2022-04-23
    - **url**: https://static.cninfo.com.cn/finalpage/2022-04-23/1213057592.PDF
    - **result**: 年报在窗口结束后明确披露公司存在业绩承诺超期未履行，因第一顺位赔付义务人所持股份被冻结、个人资产受限而无法实施赔付，并称截至报告披露日业绩赔付尚未履行；因此快照范围不可能已于2021-10-25前全部回购注销。
    - **extraction**:
      - **tool**: run-llama/liteparse
      - **version**: 2.11.1
      - **git_commit**: 5109b46e7f960a52ea9833704c9484c835c6ef4f
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 3799c625ebea1f2a98b31d341bca5a17afa3c1b86ebb0c1b345a49dd79c6c1af

</details>

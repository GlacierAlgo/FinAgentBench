# cn-a-2024-pig-restructuring-603363

## Question

你处在2024-04-30收盘后的信息环境。傲农生物已进入法院决定的预重整，2023年末归母净资产为负、货币资金相对短债极低，且存在逾期贷款、账户冻结和持续经营重大不确定性；但经营现金流仍为正，预重整也不等于正式受理。请使用下方冻结资料，预测未来24个自然月内是否会发生target严格定义的法院正式受理上市公司重整事件。请区分经营现金流改善与偿债存量缺口、猪周期与资不抵债、预重整可行性与正式法律门槛；不能因已预重整便把结果当作确定事件。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 傲农生物 (603363, SSE)
- 信息截止 / As of: 2024-04-30
- 预测窗口结束 / Window end: 2026-04-30
- 目标事件 / Target: `listed_issuer_formal_judicial_restructuring_acceptance_24m`
- 判定定义 / Definition: 快照日后24个自然月内，有管辖权的人民法院以民事裁定正式受理针对上市公司本身的破产重整申请。法院决定启动或延长预重整、公司或债权人提出申请、签署投资协议、子公司或控股股东重整、法院仅登记审查，以及公司被实施ST或*ST均不计；只有法院正式裁定受理上市公司重整至少一次才计入。

#### 判定条件 / Criteria

- `formal_judicial_restructuring_acceptance_count_24m >= 1` — 窗口内法院正式裁定受理上市公司本身的破产重整至少一次

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 傲农生物收到预重整决定：法院明确预重整不代表最终受理重整

- Evidence ID: `court-starts-pre-reorganization-not-formal-acceptance`
- 发布日期 / Published: 2024-02-06
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2024-02-06/1219098050.PDF

漳州中院于2024年2月5日决定对傲农生物启动预重整并指定临时管理人。公告逐字提示：启动预重整不代表法院会最终受理公司的重整申请，公司后续是否进入重整程序存在不确定性。若未来正式受理，股票将叠加退市风险警示；若重整失败并宣告破产，则可能终止上市。

### 傲农生物2023年年度报告：资不抵债、现金短债比0.036，但经营现金流为正

- Evidence ID: `fy2023-negative-equity-overdue-debt-and-positive-cfo`
- 发布日期 / Published: 2024-04-30
- 来源 / Source: 巨潮资讯法定定期报告
- URL: https://static.cninfo.com.cn/finalpage/2024-04-30/1219925622.PDF

2023年营业收入194.5764亿元、归母净利润-36.5082亿元，期末归母权益-9.6297亿元、资产负债率103.69%。货币资金2.0766亿元，其中0.5691亿元受限；短期借款38.3539亿元、一年内到期非流动负债18.7169亿元，现金/两项短债约0.036，另有1.1962亿元逾期短期借款。经营活动现金流净额却为正9.8401亿元，主要因出售上年存货；审计师出具无保留意见但单列持续经营重大不确定性，指出账户冻结、无法支付到期债务与预重整结果不确定。正CFO必须与存量偿债缺口共同判断。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `listed_issuer_formal_judicial_restructuring_acceptance_24m`
- 结果日期 / Resolved at: 2024-11-05
- 可观察日期 / Observed at: 2024-11-06

### 实际结果 / Realized outcome

- **observations**:
  - **formal_judicial_restructuring_acceptance_count_24m**: 1
  - **days_from_as_of_to_first_formal_acceptance**: 189
- **derivations**:


### 对应的题内资料 / Expected evidence

- `court-starts-pre-reorganization-not-formal-acceptance`
- `fy2023-negative-equity-overdue-debt-and-positive-cfo`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_pig_restructuring_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 603363.XSHG
  - **ticker**: 603363
  - **name_as_of**: 傲农生物
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2024-04-30
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: /Users/yanghh/Documents/code/quant/download_rqdata/data/db
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=603363.XSHG; quarter=2023q4; selected earliest info_date=2024-04-30; if_adjusted=0
  - **matching_group**: pig-cycle-formal-issuer-restructuring-24m-2023-distress-v1
  - **matching_role**: event/pre_reorganization_negative_equity
  - **pdf_text_tool**: run-llama/liteparse 2.12.0 git 2fd644a9e10ceeee7379949a55fa77aaf26d4b9b
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **pre_reorganization_notice**: adcb908a8ac1a804e3f9d68e1a7fc35f87ab88b1f252193833940a6e9fb22d50
    - **fy2023_annual_report**: 387c913d1850cc293b6fa1dfd5c65928fa0e9b83c71865f4d528b2faf0611d0d
  - **rqdata_sha256**:
    - **balance_2023q4**: 5f27719ecb2c1931347687d0654d204f8ca38a4693a354f772f0e213c5b52125
    - **income_2023q4**: 7133f8d47e1ebca02354c705a8b29bc75754c8706d295d601bde84cdcf8fcba7
    - **cash_flow_2023q4**: 52117623f5042bcf05cc731c600c42e983db56bfa19546a8e34d619d58f6008f
  - **outcome_contract**: Only the date of a competent court's civil ruling formally accepting reorganization of the listed issuer counts; pre-reorganization and filing milestones never count.
  - **leakage_guard**: Only documents published no later than as_of enter the corpus; later court rulings, risk warnings and restructuring outcomes are label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_court_acceptance_notice
    - **title**: 福建傲农生物科技集团股份有限公司关于法院裁定受理公司重整及指定管理人暨公司股票被叠加实施退市风险警示的公告
    - **published_at**: 2024-11-06
    - **url**: https://static.cninfo.com.cn/finalpage/2024-11-06/1221637676.PDF
    - **sha256**: 12ac36a046c996311bc15d526e0e2da7fcbd9c989afc94c19ccfafa9d7f5d538
    - **ruling_date**: 2024-11-05
    - **court**: 福建省漳州市中级人民法院
    - **civil_ruling_number**: （2024）闽06破申59号
    - **result**: 漳州中院以民事裁定正式受理债权人对上市公司傲农生物的重整申请

</details>

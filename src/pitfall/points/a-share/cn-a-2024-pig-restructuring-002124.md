# cn-a-2024-pig-restructuring-002124

## Question

你处在2024-04-30收盘后的信息环境。天邦食品2023年再次巨亏、现金短债覆盖偏低、流动负债超过流动资产，股东大会已经同意公司申请重整及预重整；但此时法院是否启动预重整、是否最终正式受理以及具体时间均不确定。请使用下方冻结资料，预测未来24个自然月内是否会发生target严格定义的法院正式受理上市公司重整事件。请把公司决议、法院预重整、子公司重整、投资协议和上市公司正式受理逐层分开，结合现金流、短债、净资产与外部融资判断；不得看到‘重整’二字便计为事件。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 天邦食品 (002124, SZSE)
- 信息截止 / As of: 2024-04-30
- 预测窗口结束 / Window end: 2026-04-30
- 目标事件 / Target: `listed_issuer_formal_judicial_restructuring_acceptance_24m`
- 判定定义 / Definition: 快照日后24个自然月内，有管辖权的人民法院以民事裁定正式受理针对上市公司本身的破产重整申请。法院决定启动或延长预重整、公司或债权人提出申请、签署投资协议、子公司或控股股东重整、法院仅登记审查，以及公司被实施ST或*ST均不计；只有法院正式裁定受理上市公司重整至少一次才计入。

#### 判定条件 / Criteria

- `formal_judicial_restructuring_acceptance_count_24m >= 1` — 窗口内法院正式裁定受理上市公司本身的破产重整至少一次

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 天邦食品董事会拟申请重整及预重整：正式受理仍是未来条件

- Evidence ID: `board-proposes-reorganization-and-pre-reorganization`
- 发布日期 / Published: 2024-03-26
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2024-03-26/1219404399.PDF

董事会拟以无法清偿到期债务、明显缺乏清偿能力但具有重整价值为由，向法院申请重整及预重整，尚需股东大会审议。公告使用条件式表述：若未来法院正式裁定受理，相关诉讼、保全和执行将依法中止或解除。公司内部决议、提交申请和法院正式受理是不同法律节点。

### 天邦食品2023年年度报告：拟重整、短债承压，但法院入口和时间不确定

- Evidence ID: `fy2023-distress-with-uncertain-court-entry`
- 发布日期 / Published: 2024-04-30
- 来源 / Source: 巨潮资讯法定定期报告
- URL: https://static.cninfo.com.cn/finalpage/2024-04-30/1219920450.PDF

2023年营业收入102.3193亿元、归母净利润-28.8341亿元，经营活动现金流净额为正2.6441亿元；期末归母权益22.1684亿元、资产负债率86.73%。货币资金12.5450亿元，短期借款27.0831亿元、一年内到期非流动负债14.0820亿元，现金/两项短债约0.305；流动负债124.12亿元高于流动资产87.87亿元。股东大会已于4月8日批准申请重整及预重整，但年报明确：法院能否决定预重整、重整申请能否被裁定受理及具体时间均不确定。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `listed_issuer_formal_judicial_restructuring_acceptance_24m`
- 结果日期 / Resolved at: 2026-04-30
- 可观察日期 / Observed at: 2026-05-22

### 实际结果 / Realized outcome

- **observations**:
  - **formal_judicial_restructuring_acceptance_count_24m**: 0
  - **formal_acceptance_not_received_at_first_official_observation_after_window**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `board-proposes-reorganization-and-pre-reorganization`
- `fy2023-distress-with-uncertain-court-entry`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_pig_restructuring_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002124.XSHE
  - **ticker**: 002124
  - **name_as_of**: 天邦食品
  - **exchange**: SZSE
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
  - **row_policy**: stock_code=002124.XSHE; quarter=2023q4; selected earliest info_date=2024-04-30; if_adjusted=0
  - **matching_group**: pig-cycle-formal-issuer-restructuring-24m-2023-distress-v1
  - **matching_role**: no_event/reorganization_application_temporal_hard_control
  - **pdf_text_tool**: run-llama/liteparse 2.12.0 git 2fd644a9e10ceeee7379949a55fa77aaf26d4b9b
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **reorganization_application_plan**: b080e8e8f3f0ee34fc63e2591f98e1d0a0bdfe3d3f0f5fb3ae080331a42e1fa7
    - **fy2023_annual_report**: 98286ddf1ad9e24e8f3908782c7d87d51ba86fbd77384dd3facc25853bcf8735
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
    - **type**: official_investor_relations_negative_crosscheck
    - **title**: 天邦食品股份有限公司投资者关系活动记录表
    - **published_at**: 2026-05-22
    - **url**: https://static.cninfo.com.cn/finalpage/2026-05-22/1225324701.PDF
    - **sha256**: d97c54349b9d7a6e981cbafe9165c00e10ea9c3ca9db2241fd42923f05cc988b
    - **window**: 2024-05-01/2026-04-30
    - **official_acceptance_ruling_dates_inside_window**:

    - **status_at_first_official_observation_after_window**: pre_reorganization_extended; formal_acceptance_not_received
    - **result**: 公司在窗口结束后的首次充分官方核验中披露预重整期限延长至2026-11-09，并明确尚未收到法院受理公司重整申请的文书

</details>

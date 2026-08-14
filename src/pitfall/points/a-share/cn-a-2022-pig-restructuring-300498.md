# cn-a-2022-pig-restructuring-300498

## Question

你处在2022-04-16收盘后的信息环境。温氏股份同样遭遇猪价下行并形成134亿元归母亏损，但披露的货币资金、流动比率、经营现金流和股东权益缓冲与高杠杆猪企不同。请使用下方冻结资料，预测未来24个自然月内是否会发生target严格定义的法院正式受理上市公司重整事件。请判断行业亏损与公司级偿债失速之间是否存在足够传导，比较现金短债覆盖、经营造血、资本结构和治理风险；不能把亏损规模本身直接翻译为重整。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 温氏股份 (300498, SZSE)
- 信息截止 / As of: 2022-04-16
- 预测窗口结束 / Window end: 2024-04-16
- 目标事件 / Target: `listed_issuer_formal_judicial_restructuring_acceptance_24m`
- 判定定义 / Definition: 快照日后24个自然月内，有管辖权的人民法院以民事裁定正式受理针对上市公司本身的破产重整申请。法院决定启动或延长预重整、公司或债权人提出申请、签署投资协议、子公司或控股股东重整、法院仅登记审查，以及公司被实施ST或*ST均不计；只有法院正式裁定受理上市公司重整至少一次才计入。

#### 判定条件 / Criteria

- `formal_judicial_restructuring_acceptance_count_24m >= 1` — 窗口内法院正式裁定受理上市公司本身的破产重整至少一次

<details>
<summary>冻结资料 / Frozen evidence (1)</summary>

### 温氏股份2021年年度报告：同为猪周期巨亏，但现金短债覆盖与权益缓冲明显不同

- Evidence ID: `fy2021-large-loss-with-liquidity-buffer`
- 发布日期 / Published: 2022-04-16
- 来源 / Source: 巨潮资讯法定定期报告
- URL: https://static.cninfo.com.cn/finalpage/2022-04-16/1212943189.PDF

2021年营业收入649.5406亿元，归母净利润-134.0436亿元，经营活动现金流净额仍为正7.6616亿元；期末归母权益324.4768亿元、资产负债率64.10%。货币资金76.3277亿元，短期借款17.5690亿元、一年内到期非流动负债27.3248亿元，现金/两项短债约1.70。公司称流动比率1.81、速动比率1.01，货币资金充足；年报还勾选控股股东及一致行动人质押未达到其持股80%，报告期未发生破产重整事项。公司自述仍需结合报表核验，但巨亏不等同于现金链已断裂。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `listed_issuer_formal_judicial_restructuring_acceptance_24m`
- 结果日期 / Resolved at: 2024-04-16
- 可观察日期 / Observed at: 2025-04-24

### 实际结果 / Realized outcome

- **observations**:
  - **formal_judicial_restructuring_acceptance_count_24m**: 0
  - **annual_periods_reporting_no_bankruptcy_reorganization_matter**: 3
- **derivations**:


### 对应的题内资料 / Expected evidence

- `fy2021-large-loss-with-liquidity-buffer`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_pig_restructuring_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 300498.XSHE
  - **ticker**: 300498
  - **name_as_of**: 温氏股份
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2022-04-16
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: /Users/yanghh/Documents/code/quant/download_rqdata/data/db
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=300498.XSHE; quarter=2021q4; selected earliest info_date=2022-04-16; if_adjusted=0
  - **matching_group**: pig-cycle-formal-issuer-restructuring-24m-2021-v1
  - **matching_role**: no_event/large_loss_with_liquidity_buffer
  - **pdf_text_tool**: run-llama/liteparse 2.12.0 git 2fd644a9e10ceeee7379949a55fa77aaf26d4b9b
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **fy2021_annual_report**: 31e74c289fa927432237f4419ad12dcdbc6352d51aa1ecdc6be96e80541d8f8b
  - **rqdata_sha256**:
    - **balance_2021q4**: 95031057e95656fd75ae2972db3f4be2865284fe28d12378fc546558f096cb12
    - **income_2021q4**: eaf6c791f8b8f1265be420d5bdabbfe28629acfeaaf0e07351236929def91dc6
    - **cash_flow_2021q4**: 6f555a2cce3ce21eaa5b5ad5e7876d72151f40c856e230a92935e20b2e7453bb
  - **outcome_contract**: Only the date of a competent court's civil ruling formally accepting reorganization of the listed issuer counts; pre-reorganization and filing milestones never count.
  - **leakage_guard**: Only documents published no later than as_of enter the corpus; later court rulings, risk warnings and restructuring outcomes are label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_annual_report_negative_crosscheck_sequence
    - **title**: 温氏食品集团股份有限公司2022、2023及2024年年度报告
    - **published_at**: 2025-04-24
    - **urls**:
      - https://static.cninfo.com.cn/finalpage/2023-04-26/1216584900.PDF
      - https://static.cninfo.com.cn/finalpage/2024-04-29/1219866693.PDF
      - https://static.cninfo.com.cn/finalpage/2025-04-24/1223241291.PDF
    - **source_sha256**:
      - **fy2022_annual_report**: 2ba213734ddec2b9af7f8dabd9b77c834b84aa8a14251faa76311e5c5461d8ad
      - **fy2023_annual_report**: 42a9257bb61916b76ec70b1ab3c21c9db3c635a1aaae12a9bc886e23b71df6b5
      - **fy2024_annual_report**: db6e09f22c59612f37fd731a63ff5435670ffa696f88af01badc5b90eb6825a3
    - **window**: 2022-04-17/2024-04-16
    - **official_acceptance_ruling_dates_inside_window**:

    - **result**: 覆盖窗口的连续三份年报均在破产重整相关事项栏勾选不适用并披露报告期未发生破产重整相关事项；窗口内不存在上市公司正式受理公告

</details>

# cn-a-2020-acquisition-commitment-validation-000004

## Question

你处在2020-01-18收盘后的信息环境。国农科技以发行股份方式收购智游网安100%股权，过户和新增股份登记已经完成，业绩承诺期为2019至2021年。请使用下方冻结资料，预测智游网安2021年度能否达到target定义的末年承诺验证。请综合交易估值与增值率、历史财务质量、客户和应收账款、移动应用安全行业竞争、承诺增速、整合与会计确认风险；不得把完成收购或后续更名本身当作业绩兑现。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 国农科技 (000004, SZSE)
- 信息截止 / As of: 2020-01-18
- 预测窗口结束 / Window end: 2023-01-18
- 目标事件 / Target: `acquisition_terminal_commitment_validated_at_registered_outcome_within_36_month_window`
- 判定定义 / Definition: 以重组文件约定的承诺口径，在预先登记的业绩承诺末年，标的资产实际扣非归母净利润不低于当年承诺值；更名、股价和事后补偿是否完成不作为判定条件

#### 判定条件 / Criteria

- `terminal_commitment_completion_ratio >= 1.0` — 承诺末年标的资产实际扣非归母净利润除以当年承诺净利润不低于1

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 国农科技发行股份购买智游网安100%股权暨关联交易报告书（草案）

- Evidence ID: `zhiyou-acquisition-draft`
- 发布日期 / Published: 2019-07-09
- 来源 / Source: 国农科技法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2019-07-09/1206432898.PDF

草案披露发行股份购买智游网安100%股权的交易结构、移动应用安全业务、历史财务和客户情况，并约定2019、2020、2021年度扣非后归属于母公司所有者的净利润分别不低于9,000万元、11,700万元、15,210万元。材料同时列示收益法估值、应收账款考核、股份补偿和减值测试安排，为判断承诺增速与实现质量提供基线。

### 国农科技发行股份购买资产实施情况暨新增股份上市公告书

- Evidence ID: `zhiyou-acquisition-implemented`
- 发布日期 / Published: 2020-01-18
- 来源 / Source: 国农科技法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2020-01-18/1207262468.PDF

公告书确认智游网安100%股权已过户，新增股份登记完成并于2020年1月20日上市。以2018年末为评估基准日，智游网安收益法评估值128,196.01万元，较账面净资产增值849.94%，交易作价128,100万元；文件重申2019至2021年承诺期及9,000万元、11,700万元、15,210万元的逐年扣非归母净利润指标。高估值和递增承诺既可能反映成长性，也提高末年兑现压力。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `acquisition_terminal_commitment_validated_at_registered_outcome_within_36_month_window`
- 结果日期 / Resolved at: 2021-12-31
- 可观察日期 / Observed at: 2022-04-30

### 实际结果 / Realized outcome

- **observations**:
  - **terminal_actual_adjusted_profit**: 49542242.07
  - **terminal_committed_adjusted_profit**: 152100000.0
- **derivations**:
  - **item 1**:
    - **metric**: terminal_commitment_completion_ratio
    - **operation**: ratio
    - **inputs**:
      - terminal_actual_adjusted_profit
      - terminal_committed_adjusted_profit
    - **value**: 0.32572151262327415

### 对应的题内资料 / Expected evidence

- `zhiyou-acquisition-draft`
- `zhiyou-acquisition-implemented`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_name_business_transition_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000004.XSHE
  - **ticker**: 000004
  - **name_as_of**: 国农科技
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-01-18
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
  - **row_policy**: stock_code=000004.XSHE; if_adjusted=0; earliest info_date used only for issuer-level cross-check; official commitment audit is label authority
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **news_evidence_policy**: Frozen evidence is limited to contemporaneous issuer filings.
  - **causal_guardrail**: The label evaluates the terminal annual commitment at the acquired target, not the wisdom of the acquisition under a counterfactual.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **zhiyou-acquisition-draft**: c20d2b5adbcb01dc4d551de08e3d41cb349c8abfd6b602f7b526fdd759c6a13e
    - **zhiyou-acquisition-implemented**: 327eddb2673d0f7d48da4d06c7e80d3be5d5e9b8fcddb17c916cc1fc9e74ff6f
- **label_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **outcome_source_sha256**:
    - **1213274239.PDF**: 087ad9f5f084197bbe58c369dddb3064e549663ce2669193e62325c7674014f1
- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 国华网安关于收购智游网安业绩承诺实现情况及业绩补偿方案的公告
    - **published_at**: 2022-04-30
    - **url**: https://static.cninfo.com.cn/finalpage/2022-04-30/1213274239.PDF
    - **fields**:
      - 2021年度承诺净利润
      - 2021年度实现扣非归母净利润
      - 业绩完成情况

</details>

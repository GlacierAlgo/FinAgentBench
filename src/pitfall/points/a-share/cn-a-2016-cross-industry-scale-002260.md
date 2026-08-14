# cn-a-2016-cross-industry-scale-002260

## Question

你处在2016-03-05收盘后的信息环境。德奥通航从传统厨房小家电向通用航空跨行业布局，年报将两者称为双主业，但通航业务仍处孵化期，2015年收入仅约占公司营业收入2.61%。请使用下方冻结资料，预测通用航空新主业能否在2016年度达到target定义的商业规模。请综合海外技术和资产收购、适航认证、研发与资本投入、订单和产能、现金流与融资能力，以及原有小家电业务的韧性；不得把改名、双主业表述或股价直接当作规模兑现。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 德奥通航 (002260, SZSE)
- 信息截止 / As of: 2016-03-05
- 预测窗口结束 / Window end: 2018-09-05
- 目标事件 / Target: `cross_industry_new_principal_business_scaled_at_registered_outcome_within_30_month_window`
- 判定定义 / Definition: 在预先登记的结果年度，跨行业布局所指向的新主业收入占公司营业收入至少50%，且上市公司扣非归母净利润为正；更名、股价和公告措辞不作为判定条件

#### 判定条件 / Criteria

- `new_principal_business_revenue_share_outcome >= 0.5` — 结果年度跨行业新主业收入除以公司营业收入不低于50%
- `issuer_adjusted_profit_outcome > 0` — 结果年度上市公司扣非归母净利润为正

<details>
<summary>冻结资料 / Frozen evidence (1)</summary>

### 德奥通用航空股份有限公司2015年年度报告

- Evidence ID: `fy2015-general-aviation-transition`
- 发布日期 / Published: 2016-03-05
- 来源 / Source: 德奥通航法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2016-03-05/1202023564.PDF

年报将电器设备和通用航空描述为双主业，但明确通航业务仍处孵化阶段、尚未形成规模。2015年公司营业收入654,425,778.81元，其中电器设备收入637,331,818.04元，通用航空收入17,093,960.77元，占比约2.61%。报告还披露海外技术及资产布局、研发和适航认证进度，以及资本投入、整合、市场和项目回报风险。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `cross_industry_new_principal_business_scaled_at_registered_outcome_within_30_month_window`
- 结果日期 / Resolved at: 2016-12-31
- 可观察日期 / Observed at: 2017-04-28

### 实际结果 / Realized outcome

- **observations**:
  - **total_revenue_outcome**: 717211958.23
  - **new_principal_business_revenue_outcome**: 32135645.58
  - **issuer_adjusted_profit_outcome**: -10034810.94
- **derivations**:
  - **item 1**:
    - **metric**: new_principal_business_revenue_share_outcome
    - **operation**: ratio
    - **inputs**:
      - new_principal_business_revenue_outcome
      - total_revenue_outcome
    - **value**: 0.044806343802893674

### 对应的题内资料 / Expected evidence

- `fy2015-general-aviation-transition`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_name_business_transition_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002260.XSHE
  - **ticker**: 002260
  - **name_as_of**: 德奥通航
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2016-03-05
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
  - **row_policy**: stock_code=002260.XSHE; quarter=2016q4; if_adjusted=0; selected earliest info_date=2017-04-28; official issuer filing defines general-aviation revenue
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **news_evidence_policy**: Frozen evidence is limited to contemporaneous issuer filings.
  - **causal_guardrail**: The benchmark tests audited cross-industry scale and adjusted earnings, not the issuer's name or management narrative.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **fy2015-general-aviation-transition**: 16439bd12fa1bea6557fdace5604cb50131186cd6c01d4a30021cd9df21abde7
- **label_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **outcome_source_sha256**:
    - **1203415376.PDF**: f94f61c7f79a583f595123298e0b647400496e83635cd402c0f6750fe98bba58
- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 德奥通用航空股份有限公司2016年年度报告
    - **published_at**: 2017-04-28
    - **url**: https://static.cninfo.com.cn/finalpage/2017-04-28/1203415376.PDF
    - **fields**:
      - 2016年度营业收入
      - 2016年度通用航空业务营业收入
      - 扣除非经常性损益后的净利润
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: f94f61c7f79a583f595123298e0b647400496e83635cd402c0f6750fe98bba58
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2016q4/data.parquet
    - **fields**:
      - revenue
      - net_profit_deduct_non_recurring_pnl
    - **row_policy**: stock_code=002260.XSHE; quarter=2016q4; if_adjusted=0; selected earliest info_date=2017-04-28

</details>

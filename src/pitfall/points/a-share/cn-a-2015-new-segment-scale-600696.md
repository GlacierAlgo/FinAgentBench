# cn-a-2015-new-segment-scale-600696

## Question

你处在2015-05-15收盘后的信息环境。多伦股份拟将公司名称变更为匹凸匹金融信息服务（上海）股份有限公司、变更经营范围，并设立金融信息服务子公司，宣称逐步转向互联网金融。请使用下方冻结资料，预测其融资租赁与商业保理新分部能否在2017年度达到target定义的商业规模。重点区分名称和经营范围变化与真实收入兑现，评估既有业务基础、资本和人才、监管可行性、客户与风险定价、资金来源及信息披露质量。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 多伦股份 (600696, SSE)
- 信息截止 / As of: 2015-05-15
- 预测窗口结束 / Window end: 2018-05-15
- 目标事件 / Target: `announced_new_segment_scaled_at_registered_outcome_within_36_month_window`
- 判定定义 / Definition: 在预先登记的结果年度，新业务分部收入占公司营业收入至少50%，且该分部毛利润为正；名称变更、公告措辞和股价表现均不作为判定条件

#### 判定条件 / Criteria

- `new_segment_revenue_share_outcome >= 0.5` — 结果年度新业务分部收入除以公司营业收入不低于50%
- `new_segment_gross_profit_outcome > 0` — 结果年度新业务分部收入减营业成本为正

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 多伦股份2014年度股东大会资料：金融信息子公司、公司名称及经营范围变更

- Evidence ID: `rename-and-finance-plan`
- 发布日期 / Published: 2015-05-15
- 来源 / Source: 多伦股份法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2015-05-15/1201016724.PDF

股东大会资料提出设立金融信息服务子公司，经营范围包括金融软件、经济与企业管理咨询、金融外包和网上贸易代理，并称公司将逐步向金融信息服务行业转向。资料同时提出把公司名称由上海多伦实业股份有限公司变更为匹凸匹金融信息服务（上海）股份有限公司、相应变更经营范围；2014年度利润拟不分配，用于房地产及互联网金融项目。材料还披露，此前拟设基金管理公司因交易所对业务合法性的质疑而拟转让给实际控制人，说明新业务面临监管核准与执行不确定性。

### 上海证券交易所第五期新闻发布会：多伦股份更名事项的监管说明

- Evidence ID: `sse-rename-risk-review`
- 发布日期 / Published: 2015-05-15
- 来源 / Source: 上海证券交易所
- URL: https://www.sse.com.cn/aboutus/mediacenter/conference/c/c_20150912_3987022.shtml

上交所说明，公司名称具有行业标示性、会影响投资者价值判断，因此已要求公司解释更名对经营业务的影响并提示风险。交易所指出更名公告后股价连续涨停、交易带有热点炒作特征，并要求公司进一步说明现有经营状况与更名的实质影响。该监管材料不预判新业务失败，但要求把名称、股价反应与可验证经营兑现分开。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `announced_new_segment_scaled_at_registered_outcome_within_36_month_window`
- 结果日期 / Resolved at: 2017-12-31
- 可观察日期 / Observed at: 2018-01-31

### 实际结果 / Realized outcome

- **observations**:
  - **total_revenue_outcome**: 175089263.7
  - **new_segment_revenue_outcome**: 21085853.04
  - **new_segment_cost_outcome**: 6513972.38
- **derivations**:
  - **item 1**:
    - **metric**: new_segment_revenue_share_outcome
    - **operation**: ratio
    - **inputs**:
      - new_segment_revenue_outcome
      - total_revenue_outcome
    - **value**: 0.12042916050026202
  - **item 2**:
    - **metric**: new_segment_gross_profit_outcome
    - **operation**: difference
    - **inputs**:
      - new_segment_revenue_outcome
      - new_segment_cost_outcome
    - **value**: 14571880.66

### 对应的题内资料 / Expected evidence

- `rename-and-finance-plan`
- `sse-rename-risk-review`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_name_business_transition_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600696.XSHG
  - **ticker**: 600696
  - **name_as_of**: 多伦股份
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2015-05-15
  - **allowed_domains**:
    - cninfo.com.cn
    - sse.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
  - **row_policy**: stock_code=600696.XSHG; quarter=2017q4; if_adjusted=0; selected earliest info_date=2018-01-31; official annual-report segment table defines target revenue and cost
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **news_evidence_policy**: Frozen evidence is limited to contemporaneous issuer filings and the exchange's same-day regulatory explanation.
  - **causal_guardrail**: The benchmark tests commercial scaling of the named new segment, not whether a rename itself is good or bad.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **rename-and-finance-plan**: db2dfc673ec85e3b0b6468a4439cbd4d7dd912b5e335c4776ed75b153787df6f
    - **sse-rename-risk-review**: 9622f7c342c6f3b88ceb3d0ed68665d8e48aa1e6cf1a5f7fdda188d5dae043a5
- **label_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **outcome_source_sha256**:
    - **1204376270.PDF**: ca1d60abd1c5fc66fbc0f43fd27cfe6aec83c7c27d173a7abf07ba97a6a626f6
- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 上海岩石企业发展股份有限公司2017年年度报告
    - **published_at**: 2018-01-31
    - **url**: https://static.cninfo.com.cn/finalpage/2018-01-31/1204376270.PDF
    - **fields**:
      - 营业收入
      - 融资租赁营业收入与营业成本
      - 商业保理营业收入与营业成本
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2017q4/data.parquet
    - **fields**:
      - revenue
      - gross_profit
    - **row_policy**: stock_code=600696.XSHG; quarter=2017q4; if_adjusted=0; selected earliest info_date=2018-01-31

</details>

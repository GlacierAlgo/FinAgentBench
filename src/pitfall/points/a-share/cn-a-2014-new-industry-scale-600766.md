# cn-a-2014-new-industry-scale-600766

## Question

你处在2014-08-28收盘后的信息环境。园城黄金已把黄金矿业写入公司名称和经营范围，并通过托管乳山金海矿业等方式进入矿业，合同提出扩产、勘探和利润目标。请使用下方冻结资料，预测黄金产品新行业能否在2015年度达到target定义的商业规模。请区分矿权所有、托管费、矿产品销售与真实矿业规模，分析证照与储量、建设资金、产权安排、合同期限、金价、关联和执行风险；不得将公司名称中的“黄金”直接当作经营兑现。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 园城黄金 (600766, SSE)
- 信息截止 / As of: 2014-08-28
- 预测窗口结束 / Window end: 2017-08-28
- 目标事件 / Target: `new_industry_scaled_at_registered_outcome_within_36_month_window`
- 判定定义 / Definition: 在预先登记的结果年度，目标新行业收入占公司营业收入至少30%，且目标新行业毛利润为正；名称变更及公告措辞均不作为判定条件

#### 判定条件 / Criteria

- `target_industry_revenue_share_outcome >= 0.3` — 结果年度目标新行业收入除以公司营业收入不低于30%
- `target_industry_gross_profit_outcome > 0` — 结果年度目标新行业收入减营业成本为正

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 园城黄金签订乳山市金海矿业委托经营管理合同的公告

- Evidence ID: `jinhai-mining-management-contract`
- 发布日期 / Published: 2013-09-23
- 来源 / Source: 园城黄金法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2013-09-23/63100134.PDF

公告披露公司受托管理乳山金海矿业，但明确该安排不构成重大资产重组，托管期间矿业公司产权仍归原股东。材料称矿山设计年产能6万吨、日处理能力400多吨，并提出扩建至日处理约1,000吨、建设竖井及年利润不低于3,000万元的目标；初始托管期限为一年，托管费2,000万元/年。产权、证照、投资另议和短合同期均是规模兑现的关键约束。

### 园城黄金2014年半年度报告：名称变更、经营范围与矿业基线

- Evidence ID: `fy2014h1-gold-transition-base`
- 发布日期 / Published: 2014-08-28
- 来源 / Source: 园城黄金法定半年度报告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2014-08-28/1200177414.PDF

半年度报告记载，公司于2013年3月经董事会和股东大会决议更名为烟台园城黄金股份有限公司，经营范围加入黄金及矿产品销售。报告同时披露公司仍有房地产开发、物业及租赁等业务，并说明矿业板块主要通过托管、勘探和项目推进形成；判断新行业规模应核对矿产品销售收入和成本，而不能把托管收入或名称变化等同为黄金产品商业化。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `new_industry_scaled_at_registered_outcome_within_36_month_window`
- 结果日期 / Resolved at: 2015-12-31
- 可观察日期 / Observed at: 2016-03-31

### 实际结果 / Realized outcome

- **observations**:
  - **total_revenue_outcome**: 16897964.73
  - **target_industry_revenue_outcome**: 0.0
  - **target_industry_cost_outcome**: 0.0
- **derivations**:
  - **item 1**:
    - **metric**: target_industry_revenue_share_outcome
    - **operation**: ratio
    - **inputs**:
      - target_industry_revenue_outcome
      - total_revenue_outcome
    - **value**: 0.0
  - **item 2**:
    - **metric**: target_industry_gross_profit_outcome
    - **operation**: difference
    - **inputs**:
      - target_industry_revenue_outcome
      - target_industry_cost_outcome
    - **value**: 0.0

### 对应的题内资料 / Expected evidence

- `jinhai-mining-management-contract`
- `fy2014h1-gold-transition-base`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_name_business_transition_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600766.XSHG
  - **ticker**: 600766
  - **name_as_of**: 园城黄金
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2014-08-28
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
  - **row_policy**: stock_code=600766.XSHG; quarter=2015q4; if_adjusted=0; selected earliest info_date=2016-03-31; official annual-report industry table defines target revenue and cost
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **news_evidence_policy**: Frozen evidence is limited to contemporaneous issuer filings.
  - **causal_guardrail**: The benchmark tests audited new-industry scale and does not infer quality from the issuer's name.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **jinhai-mining-management-contract**: 4d3351e72fce328c6d2aae9c8a60e9586d1577075c2292c0eee33ec2ebb98412
    - **fy2014h1-gold-transition-base**: 43ad97de18e92210d2ac0493af9046e9f83bc513caf87c1871fde1a2ef418093
- **label_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **outcome_source_sha256**:
    - **1202114703.PDF**: 56b396bbe071f0def2a107ff09f3a0f3f074dd75f274c4cd30f518939a711a03
- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 烟台园城黄金股份有限公司2015年年度报告
    - **published_at**: 2016-03-31
    - **url**: https://static.cninfo.com.cn/finalpage/2016-03-31/1202114703.PDF
    - **fields**:
      - 营业收入
      - 黄金产品销售营业收入
      - 黄金产品销售营业成本
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2015q4/data.parquet
    - **fields**:
      - revenue
      - gross_profit
    - **row_policy**: stock_code=600766.XSHG; quarter=2015q4; if_adjusted=0; selected earliest info_date=2016-03-31

</details>

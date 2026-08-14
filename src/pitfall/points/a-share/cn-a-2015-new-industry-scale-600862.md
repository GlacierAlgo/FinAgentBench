# cn-a-2015-new-industry-scale-600862

## Question

你处在2015-12-19收盘后的信息环境。南通科技已完成重大资产出售，并以发行股份方式注入中航复材、优材京航和优材百慕100%股权，控制权转入航空工业体系。请使用下方冻结资料，预测注入的新材料行业能否在2017年度达到target定义的商业规模。请综合注入资产既有收入与盈利、复合材料市场和客户、军民品结构、关联交易、技术与产能、估值及整合风险；不得把控制权变更、资产过户或之后更名直接当作规模兑现。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 南通科技 (600862, SSE)
- 信息截止 / As of: 2015-12-19
- 预测窗口结束 / Window end: 2018-12-19
- 目标事件 / Target: `new_industry_scaled_at_registered_outcome_within_36_month_window`
- 判定定义 / Definition: 在预先登记的结果年度，目标新行业收入占公司营业收入至少30%，且目标新行业毛利润为正；名称变更及公告措辞均不作为判定条件

#### 判定条件 / Criteria

- `target_industry_revenue_share_outcome >= 0.3` — 结果年度目标新行业收入除以公司营业收入不低于30%
- `target_industry_gross_profit_outcome > 0` — 结果年度目标新行业收入减营业成本为正

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 南通科技重大资产出售及发行股份购买资产并募集配套资金报告书

- Evidence ID: `avic-material-assets-restructure`
- 发布日期 / Published: 2015-11-04
- 来源 / Source: 南通科技法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2015-11-04/1201750933.PDF

报告书披露出售通能精机100%股权，并注入中航复材、优材京航、优材百慕各100%股权。中航复材从事航空复合材料等新材料业务，另外两家覆盖人工关节和航空器材。材料提供拟注入资产历史财务、备考报表、评估和配套融资用途，并提示评估增值、政策、市场、生产经营、财务和整合管理风险。

### 南通科技重大资产重组实施情况报告书

- Evidence ID: `avic-material-assets-implemented`
- 发布日期 / Published: 2015-12-19
- 来源 / Source: 南通科技法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2015-12-19/1201845540.PDF

实施报告确认本次交易相关股权划转、标的资产过户和非公开发行均已办理完毕，实施情况与此前披露不存在差异。交易完成只证明资产和控制权进入上市公司，不自动证明其在未来合并收入中达到足够占比；结果仍需以后续年度分行业收入与成本检验。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `new_industry_scaled_at_registered_outcome_within_36_month_window`
- 结果日期 / Resolved at: 2017-12-31
- 可观察日期 / Observed at: 2018-03-17

### 实际结果 / Realized outcome

- **observations**:
  - **total_revenue_outcome**: 3044152398.07
  - **target_industry_revenue_outcome**: 1397975771.79
  - **target_industry_cost_outcome**: 1005122343.93
- **derivations**:
  - **item 1**:
    - **metric**: target_industry_revenue_share_outcome
    - **operation**: ratio
    - **inputs**:
      - target_industry_revenue_outcome
      - total_revenue_outcome
    - **value**: 0.45923317527608665
  - **item 2**:
    - **metric**: target_industry_gross_profit_outcome
    - **operation**: difference
    - **inputs**:
      - target_industry_revenue_outcome
      - target_industry_cost_outcome
    - **value**: 392853427.86

### 对应的题内资料 / Expected evidence

- `avic-material-assets-restructure`
- `avic-material-assets-implemented`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_name_business_transition_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600862.XSHG
  - **ticker**: 600862
  - **name_as_of**: 南通科技
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2015-12-19
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
  - **row_policy**: stock_code=600862.XSHG; quarter=2017q4; if_adjusted=0; selected earliest info_date=2018-03-17; official annual-report industry table defines target revenue and cost
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **news_evidence_policy**: Frozen evidence is limited to contemporaneous issuer filings.
  - **causal_guardrail**: The benchmark tests audited new-industry scale and does not infer quality from the issuer's name.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **avic-material-assets-restructure**: 451e7393a9fc25b6748a3cc803606da07a7b4bd81c63891adf2d23b180dabb8b
    - **avic-material-assets-implemented**: b4291c67e4eed679134d84d54e126e5b6548db90909edceca25dd0c569624674
- **label_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **outcome_source_sha256**:
    - **1204484742.PDF**: 436fe8bb60b94d40814ea087c7f0e30ddd4d7b3d8825d6202d466d7510c40e4a
- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 中航航空高科技股份有限公司2017年年度报告
    - **published_at**: 2018-03-17
    - **url**: https://static.cninfo.com.cn/finalpage/2018-03-17/1204484742.PDF
    - **fields**:
      - 营业收入
      - 新材料行业营业收入
      - 新材料行业营业成本
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2017q4/data.parquet
    - **fields**:
      - revenue
      - gross_profit
    - **row_policy**: stock_code=600862.XSHG; quarter=2017q4; if_adjusted=0; selected earliest info_date=2018-03-17

</details>

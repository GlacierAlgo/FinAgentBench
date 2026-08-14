# cn-a-2015-cross-industry-scale-002027

## Question

你处在2015-12-28收盘后的信息环境。七喜控股已通过重大资产置换、发行股份购买资产及募集配套资金取得分众传媒100%股权，原有IT资产和负债已置出，交易明确构成借壳上市且实际控制人变更。请使用下方冻结资料，预测跨行业进入的媒体新主业能否在2017年度达到target定义的商业规模。请综合分众传媒历史收入与扣非盈利、楼宇和影院媒体网络、客户与广告周期、现金流、估值、业绩承诺、关联交易及整合风险；不得把资产过户、控制权变化、公司名称或股价直接当作商业兑现。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 七喜控股 (002027, SZSE)
- 信息截止 / As of: 2015-12-28
- 预测窗口结束 / Window end: 2018-06-28
- 目标事件 / Target: `cross_industry_new_principal_business_scaled_at_registered_outcome_within_30_month_window`
- 判定定义 / Definition: 在预先登记的结果年度，跨行业布局所指向的新主业收入占公司营业收入至少50%，且上市公司扣非归母净利润为正；更名、股价和公告措辞不作为判定条件

#### 判定条件 / Criteria

- `new_principal_business_revenue_share_outcome >= 0.5` — 结果年度跨行业新主业收入除以公司营业收入不低于50%
- `issuer_adjusted_profit_outcome > 0` — 结果年度上市公司扣非归母净利润为正

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 七喜控股重大资产置换及发行股份购买资产并募集配套资金暨关联交易报告书（草案）

- Evidence ID: `focus-media-backdoor-report`
- 发布日期 / Published: 2015-09-02
- 来源 / Source: 七喜控股法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2015-09-02/1201538117.PDF

报告书披露拟置出上市公司原有全部资产和负债，并置入分众传媒100%股权。材料给出分众传媒楼宇媒体、影院媒体等业务的历史收入、盈利、客户、网络资源、现金流、业绩承诺、估值与风险，并明确交易构成借壳上市。

### 七喜控股重大资产重组实施情况报告书

- Evidence ID: `focus-media-backdoor-implemented`
- 发布日期 / Published: 2015-12-28
- 来源 / Source: 七喜控股法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2015-12-28/1201863184.PDF

实施报告确认分众传媒100%股权于2015年12月17日过户，原有全部资产负债已置出，新增股份随后登记，实际控制人变更为江南春。交易价格相对原上市公司资产总额比例极高并构成借壳上市；但交割完成只能确认业务进入上市公司，未来商业规模仍须按结果年度收入占比与扣非净利润检验。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `cross_industry_new_principal_business_scaled_at_registered_outcome_within_30_month_window`
- 结果日期 / Resolved at: 2017-12-31
- 可观察日期 / Observed at: 2018-04-25

### 实际结果 / Realized outcome

- **observations**:
  - **total_revenue_outcome**: 12013553185.42
  - **new_principal_business_revenue_outcome**: 12013553185.42
  - **issuer_adjusted_profit_outcome**: 4851996085.18
- **derivations**:
  - **item 1**:
    - **metric**: new_principal_business_revenue_share_outcome
    - **operation**: ratio
    - **inputs**:
      - new_principal_business_revenue_outcome
      - total_revenue_outcome
    - **value**: 1.0

### 对应的题内资料 / Expected evidence

- `focus-media-backdoor-report`
- `focus-media-backdoor-implemented`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_name_business_transition_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002027.XSHE
  - **ticker**: 002027
  - **name_as_of**: 七喜控股
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2015-12-28
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
  - **row_policy**: stock_code=002027.XSHE; quarter=2017q4; if_adjusted=0; selected earliest info_date=2018-04-25; official annual-report media segment disclosure defines new-business revenue
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **news_evidence_policy**: Frozen evidence is limited to contemporaneous issuer filings.
  - **causal_guardrail**: The benchmark tests audited cross-industry scale and adjusted earnings, not the issuer's name or management narrative.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **focus-media-backdoor-report**: c9a3148c338d82d52968a3e48b65dcfb0bd2ed55b462d035f22aeb8f2d2802b8
    - **focus-media-backdoor-implemented**: 2c79b1560f7a5635bbdc85f62071d0d18abadfb7363e650e08f238f85d94c9b2
- **label_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **outcome_source_sha256**:
    - **1204733591.PDF**: 07b40b50849a23a661d6fe910d72fc2ea5fb267eb399b59f6c41dfa0b7eae55f
- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 分众传媒信息技术股份有限公司2017年年度报告
    - **published_at**: 2018-04-25
    - **url**: https://static.cninfo.com.cn/finalpage/2018-04-25/1204733591.PDF
    - **fields**:
      - 营业收入
      - 媒体业务营业收入
      - 扣除非经常性损益后的归属于上市公司股东的净利润
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2017q4/data.parquet
    - **fields**:
      - revenue
      - net_profit_deduct_non_recurring_pnl
    - **row_policy**: stock_code=002027.XSHE; quarter=2017q4; if_adjusted=0; selected earliest info_date=2018-04-25

</details>

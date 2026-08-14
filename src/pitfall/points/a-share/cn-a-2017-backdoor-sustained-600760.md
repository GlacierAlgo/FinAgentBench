# cn-a-2017-backdoor-sustained-600760

## Question

你处在2017-12-23收盘后的信息环境。中航黑豹已出售原有汽车等业务资产，并以发行股份方式注入沈飞集团100%股权；标的过户、股份登记与配套融资均已完成。请使用下方冻结资料，预测借壳置入的航空制造新主业能否在2019年度达到target定义的持续经营结果。请综合沈飞集团历史收入与盈利、客户和产品集中度、军品定价与回款、资本开支、配套融资项目、关联交易及整合风险；不得把资产过户、控制权变化、公司名称或股价直接当作商业兑现。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 中航黑豹 (600760, SSE)
- 信息截止 / As of: 2017-12-23
- 预测窗口结束 / Window end: 2020-06-23
- 目标事件 / Target: `backdoor_new_principal_business_sustained_at_registered_outcome_within_30_month_window`
- 判定定义 / Definition: 在预先登记的结果年度，借壳置入的新主业收入占公司营业收入至少80%，且上市公司扣非归母净利润为正；更名、股价及非经常损益不作为判定条件

#### 判定条件 / Criteria

- `new_principal_business_revenue_share_outcome >= 0.8` — 结果年度借壳置入的新主业收入除以公司营业收入不低于80%
- `issuer_adjusted_profit_outcome > 0` — 结果年度上市公司扣非归母净利润为正

<details>
<summary>冻结资料 / Frozen evidence (1)</summary>

### 中航黑豹重大资产出售及发行股份购买资产并募集配套资金暨关联交易实施情况报告书

- Evidence ID: `shenyang-aircraft-backdoor-implemented`
- 发布日期 / Published: 2017-12-23
- 来源 / Source: 中航黑豹法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2017-12-23/1204251588.PDF

实施报告确认沈飞集团100%股权于2017年11月20日过户，原有业务资产已实质交割，新股登记和配套融资完成。募集资金拟投入新机研制生产能力建设等项目。报告同时披露置入资产历史财务、关联交易、客户与军品业务特点及实施风险；交易完成不等于以后年度收入规模和扣非盈利自动达标。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `backdoor_new_principal_business_sustained_at_registered_outcome_within_30_month_window`
- 结果日期 / Resolved at: 2019-12-31
- 可观察日期 / Observed at: 2020-04-25

### 实际结果 / Realized outcome

- **observations**:
  - **total_revenue_outcome**: 23760860873.2
  - **new_principal_business_revenue_outcome**: 23354768571.02
  - **issuer_adjusted_profit_outcome**: 843803894.11
- **derivations**:
  - **item 1**:
    - **metric**: new_principal_business_revenue_share_outcome
    - **operation**: ratio
    - **inputs**:
      - new_principal_business_revenue_outcome
      - total_revenue_outcome
    - **value**: 0.9829091923753472

### 对应的题内资料 / Expected evidence

- `shenyang-aircraft-backdoor-implemented`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_name_business_transition_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600760.XSHG
  - **ticker**: 600760
  - **name_as_of**: 中航黑豹
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2017-12-23
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
  - **row_policy**: stock_code=600760.XSHG; quarter=2019q4; if_adjusted=0; selected earliest info_date=2020-04-25; official annual-report principal-business disclosure defines aviation-manufacturing revenue
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **news_evidence_policy**: Frozen evidence is limited to contemporaneous issuer filings.
  - **causal_guardrail**: The benchmark tests audited post-backdoor business scale and earnings, not the issuer's name or transaction completion alone.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **shenyang-aircraft-backdoor-implemented**: 8d320092cb64edda88334d20ad49f1af073805480004bf09be4ff36a812811e3
- **label_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **outcome_source_sha256**:
    - **1207610489.PDF**: 9c342e2a92eb9b1ecc1ed35519ea194d3e5a1fc26cdd6bcc038f71bb517f7d74
- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 中航沈飞股份有限公司2019年年度报告
    - **published_at**: 2020-04-25
    - **url**: https://static.cninfo.com.cn/finalpage/2020-04-25/1207610489.PDF
    - **fields**:
      - 营业收入
      - 航空制造业营业收入
      - 扣除非经常性损益后的归属于上市公司股东的净利润
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2019q4/data.parquet
    - **fields**:
      - revenue
      - net_profit_deduct_non_recurring_pnl
    - **row_policy**: stock_code=600760.XSHG; quarter=2019q4; if_adjusted=0; selected earliest info_date=2020-04-25

</details>

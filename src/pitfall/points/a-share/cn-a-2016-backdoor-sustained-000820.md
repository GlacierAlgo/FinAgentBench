# cn-a-2016-backdoor-sustained-000820

## Question

你处在2016-10-31收盘后的信息环境。金城股份已通过重大资产出售、置换及发行股份购买江苏省冶金设计院100%股权，原造纸资产基本退出，冶金工程与节能环保业务成为拟置入的新主业。请使用下方冻结资料，预测该借壳置入业务能否在2018年度达到target定义的持续经营结果。请综合工程总承包和合同执行、客户集中度、应收款与经营现金流、关联交易、技术能力、在手项目、业绩承诺及整合风险；不得把资产过户、控制权变化、公司名称或股价直接当作商业兑现。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 金城股份 (000820, SZSE)
- 信息截止 / As of: 2016-10-31
- 预测窗口结束 / Window end: 2019-04-30
- 目标事件 / Target: `backdoor_new_principal_business_sustained_at_registered_outcome_within_30_month_window`
- 判定定义 / Definition: 在预先登记的结果年度，借壳置入的新主业收入占公司营业收入至少80%，且上市公司扣非归母净利润为正；更名、股价及非经常损益不作为判定条件

#### 判定条件 / Criteria

- `new_principal_business_revenue_share_outcome >= 0.8` — 结果年度借壳置入的新主业收入除以公司营业收入不低于80%
- `issuer_adjusted_profit_outcome > 0` — 结果年度上市公司扣非归母净利润为正

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 金城造纸重大资产出售、置换及发行股份购买资产并募集配套资金暨关联交易报告书（草案）

- Evidence ID: `metallurgical-institute-backdoor-draft`
- 发布日期 / Published: 2015-08-28
- 来源 / Source: 金城股份法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2015-08-28/1201509075.PDF

草案披露拟出售原有造纸资产，并置入江苏省冶金设计院100%股权。江苏院以工程设计、咨询和工程总承包为主，交易材料披露其客户、历史财务、应收款、合同、盈利预测、关联交易以及行业和项目执行风险。重组安排本身不能证明置入业务以后可持续盈利。

### 金城股份重大资产重组实施进展公告

- Evidence ID: `metallurgical-institute-assets-transferred`
- 发布日期 / Published: 2016-10-10
- 来源 / Source: 金城股份法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2016-10-10/1202741524.PDF

公告称江苏院100%股权已于2016年8月17日过户，原有资产和负债已大部分交割；过渡期江苏院实现的净利润归上市公司享有，同时仍有少量拟出售资产尚待完成权属转移。过户和过渡期收益只是时点事实，不能替代未来年度收入占比与扣非净利润验证。

### 金城股份2016年第三季度报告全文

- Evidence ID: `metallurgical-institute-post-restructure-q3`
- 发布日期 / Published: 2016-10-31
- 来源 / Source: 金城股份法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2016-10-31/1202804741.PDF

三季报呈现重组后合并资产负债表和经营结果，披露重大资产重组、江苏院纳入上市公司以及相关风险。投资者可以据此区分一次性交割影响与新主业的现金回款、工程执行和持续盈利能力。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `backdoor_new_principal_business_sustained_at_registered_outcome_within_30_month_window`
- 结果日期 / Resolved at: 2018-12-31
- 可观察日期 / Observed at: 2019-04-30

### 实际结果 / Realized outcome

- **observations**:
  - **total_revenue_outcome**: 12895545.71
  - **new_principal_business_revenue_outcome**: 12895545.71
  - **issuer_adjusted_profit_outcome**: -700881732.22
- **derivations**:
  - **item 1**:
    - **metric**: new_principal_business_revenue_share_outcome
    - **operation**: ratio
    - **inputs**:
      - new_principal_business_revenue_outcome
      - total_revenue_outcome
    - **value**: 1.0

### 对应的题内资料 / Expected evidence

- `metallurgical-institute-backdoor-draft`
- `metallurgical-institute-assets-transferred`
- `metallurgical-institute-post-restructure-q3`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_name_business_transition_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000820.XSHE
  - **ticker**: 000820
  - **name_as_of**: 金城股份
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2016-10-31
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
  - **row_policy**: stock_code=000820.XSHE; quarter=2018q4; if_adjusted=0; selected earliest info_date=2019-04-30; official annual-report principal-business disclosure defines new-business revenue
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **news_evidence_policy**: Frozen evidence is limited to contemporaneous issuer filings.
  - **causal_guardrail**: The benchmark tests audited post-backdoor business scale and earnings, not the issuer's name or transaction completion alone.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **metallurgical-institute-backdoor-draft**: ed756ecf425070b4750971847f656671f8a0778192f6fa2b50b395871a320189
    - **metallurgical-institute-assets-transferred**: dde836ef87654d3b068f341eff3cbdb29cd4520c3273f93f936aee9c3bccfe54
    - **metallurgical-institute-post-restructure-q3**: 33fbb869b6cea05f8e6784dc2839c569a67b9e654b4c95f8866755ba15acc404
- **label_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **outcome_source_sha256**:
    - **1206164845.PDF**: 21a151284a65c6d55ce33540647bbf17c2a19dd7dd6ce161ef451214b2a96818
- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 神雾节能股份有限公司2018年年度报告
    - **published_at**: 2019-04-30
    - **url**: https://static.cninfo.com.cn/finalpage/2019-04-30/1206164845.PDF
    - **fields**:
      - 营业收入
      - 冶金工程及相关新主业营业收入
      - 扣除非经常性损益后的归属于上市公司股东的净利润
  - **item 2**:
    - **type**: rqdata_pit
    - **paths**:
      - data/db/rq_income_statement_pit/quarter=2018q4/data.parquet
    - **fields**:
      - revenue
      - net_profit_deduct_non_recurring_pnl
    - **row_policy**: stock_code=000820.XSHE; quarter=2018q4; if_adjusted=0; selected earliest info_date=2019-04-30

</details>

# cn-a-2020-audit-opinion-star-st-000408

## Question

你处在2020-04-30收盘后的信息环境。藏格控股已经披露2019年度财务报表及审计报告，as-of时证券简称尚未冠以*ST。请只使用下方冻结资料，依据当时有效的深交所规则，判断该财务报表审计意见是否会在2020-05-31前导致首次实施退市风险警示*ST。必须区分无法表示意见、否定意见、保留意见，也必须区分财务报表审计意见、内部控制意见、ST和*ST。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 藏格控股 (000408, SZSE)
- 信息截止 / As of: 2020-04-30
- 预测窗口结束 / Window end: 2020-05-31
- 目标事件 / Target: `new_star_st_from_latest_annual_financial_audit_opinion`
- 判定定义 / Definition: 公司在as-of时尚未被实施退市风险警示，并因截至as-of已披露的最近年度财务会计报告所载审计意见触及当时适用的财务类退市风险警示条款，于预测窗口内首次被实施退市风险警示（证券简称冠以“*ST”）。保留意见、仅实施其他风险警示“ST”及非财务报表审计意见均不计入

#### 判定条件 / Criteria

- `new_financial_audit_opinion_star_st_effective_count >= 1` — 预测窗口内因最近年度财务报表审计意见首次生效的*ST次数至少为1

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 深交所股票上市规则（2018年11月修订）第13.2.1条：审计意见触发边界

- Evidence ID: `szse-2018-audit-opinion-rule`
- 发布日期 / Published: 2018-11-16
- 来源 / Source: 深圳证券交易所
- URL: https://docs.static.szse.cn/www/disclosure/notice/W020181116826736012513.pdf

第13.2.1条规定，最近一个会计年度的财务会计报告被出具无法表示意见或者否定意见的审计报告，深交所有权对公司股票交易实行退市风险警示。第13.2.3条规定，触及第13.2.1条第（一）项至第（四）项的，公司在披露年度报告当日停牌一天，自复牌之日起实行退市风险警示。条文明列无法表示意见和否定意见，没有把保留意见列为这一初次*ST触发项。

### 藏格控股2019年度审计报告：财务报表被出具无法表示意见

- Evidence ID: `000408-fy2019-audit-report`
- 发布日期 / Published: 2020-04-30
- 来源 / Source: 巨潮资讯（深交所法定信息披露）
- URL: https://static.cninfo.com.cn/finalpage/2020-04-30/1207687966.PDF

中审众环会计师事务所对藏格控股2019年度财务报表出具无法表示意见。形成无法表示意见的事项包括贸易收入及关联方资金往来的商业实质与审计证据限制等，审计师认为无法取得充分、适当的审计证据以形成审计意见。目标事件看的是年度财务会计报告审计意见，不是内部控制审计意见。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `new_star_st_from_latest_annual_financial_audit_opinion`
- 结果日期 / Resolved at: 2020-05-06
- 可观察日期 / Observed at: 2020-05-06

### 实际结果 / Realized outcome

- **observations**:
  - **new_financial_audit_opinion_star_st_effective_count**: 1
  - **financial_statement_disclaimer_opinion_count**: 1
  - **financial_statement_qualified_opinion_count**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `szse-2018-audit-opinion-rule`
- `000408-fy2019-audit-report`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_rule_regime_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000408.XSHE
  - **ticker**: 000408
  - **name_as_of**: 藏格控股
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-04-30
  - **allowed_domains**:
    - cninfo.com.cn
    - szse.cn
- **scenario_authoring**:
  - **dataset**: official_exchange_and_issuer_filings
  - **access**: read_only
  - **matching_group**: annual-audit-opinion-star-st-regime-v1
  - **matching_role**: event
  - **matching_axes**:
    - annual_report_disclosed
    - nonstandard_financial_statement_opinion
    - pre_event_not_star_st
    - opinion_type_contrast
  - **rule_snapshot_id**: szse-main-2018-11-13.2.1-4
  - **exact_contract**: new_star_st_from_latest_annual_financial_audit_opinion-v1
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **1207687966.PDF**: 1048a3e2adbd166c9dd05ea810d5bb0afb3adaaf949d38a454f180856b69ac69
    - **szse_2018_listing_rules.pdf**: 8cb4eaa97f77f8ff9a88bd25484f2d5c3692a875800134b72d055fbccd4ded00
  - **leakage_guard**: Corpus contains the as-of audit report and contemporaneous rule only; the later effective *ST state remains label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_risk_warning_notice
    - **title**: 藏格控股关于公司股票交易被实行退市风险警示暨停牌的公告
    - **published_at**: 2020-04-30
    - **url**: https://static.cninfo.com.cn/finalpage/2020-04-30/1207687963.PDF
    - **effective_at**: 2020-05-06
    - **fields**:
      - 2019年度财务会计报告无法表示意见
      - *ST藏格
      - 退市风险警示起始日

</details>

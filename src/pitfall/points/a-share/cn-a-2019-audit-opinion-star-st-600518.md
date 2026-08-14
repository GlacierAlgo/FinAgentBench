# cn-a-2019-audit-opinion-star-st-600518

## Question

你处在2019-04-30收盘后的信息环境。康美药业已经披露2018年度财务报表及审计报告，as-of时证券简称尚未冠以*ST。请只使用下方冻结资料，依据当时有效的上交所规则，判断该财务报表审计意见是否会在2019-05-31前导致首次实施退市风险警示*ST。必须区分无法表示意见、否定意见、保留意见，也必须区分财务报表审计意见、内部控制意见、ST和*ST；公司风险严重不等于目标事件自动成立。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 康美药业 (600518, SSE)
- 信息截止 / As of: 2019-04-30
- 预测窗口结束 / Window end: 2019-05-31
- 目标事件 / Target: `new_star_st_from_latest_annual_financial_audit_opinion`
- 判定定义 / Definition: 公司在as-of时尚未被实施退市风险警示，并因截至as-of已披露的最近年度财务会计报告所载审计意见触及当时适用的财务类退市风险警示条款，于预测窗口内首次被实施退市风险警示（证券简称冠以“*ST”）。保留意见、仅实施其他风险警示“ST”及非财务报表审计意见均不计入

#### 判定条件 / Criteria

- `new_financial_audit_opinion_star_st_effective_count >= 1` — 预测窗口内因最近年度财务报表审计意见首次生效的*ST次数至少为1

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 上交所股票上市规则（2018年11月修订）：年度财务报表审计意见的*ST边界

- Evidence ID: `sse-2018-audit-opinion-rule`
- 发布日期 / Published: 2018-11-16
- 来源 / Source: 上海证券交易所
- URL: https://www.sse.com.cn/lawandrules/sselawsrules2025/repeal/rules/c/c_20181116_10784930.shtml

上证发〔2018〕97号发布并施行《上海证券交易所股票上市规则（2018年11月修订）》。同期第13.2.1条财务类退市风险警示条款将最近一个会计年度财务会计报告被出具无法表示意见或者否定意见列为初次实施退市风险警示的情形；保留意见不在该项之列。风险严重、内部控制否定意见或其他风险警示ST，不能替代目标要求的因年度财务报表审计意见首次实施*ST。

### 康美药业2018年年度报告：财务报表为保留意见，内部控制为否定意见

- Evidence ID: `600518-fy2018-audit-report`
- 发布日期 / Published: 2019-04-30
- 来源 / Source: 巨潮资讯（上交所法定信息披露）
- URL: https://static.cninfo.com.cn/finalpage/2019-04-30/1206168292.PDF

广东正中珠江会计师事务所对康美药业2018年度财务报表出具保留意见，明确认为相关事项影响重大但不具有广泛性；审计意见段称，除保留意见基础所述事项影响外，财务报表在所有重大方面公允反映公司财务状况和经营成果。年度报告同时披露，2018年度内部控制审计报告为否定意见。判断目标事件必须以财务报表的保留意见为准，不能把内部控制否定意见误当成财务报表否定意见。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `new_star_st_from_latest_annual_financial_audit_opinion`
- 结果日期 / Resolved at: 2019-05-31
- 可观察日期 / Observed at: 2019-05-31

### 实际结果 / Realized outcome

- **observations**:
  - **new_financial_audit_opinion_star_st_effective_count**: 0
  - **financial_statement_disclaimer_opinion_count**: 0
  - **financial_statement_qualified_opinion_count**: 1
  - **other_risk_warning_st_effective_count**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `sse-2018-audit-opinion-rule`
- `600518-fy2018-audit-report`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_rule_regime_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600518.XSHG
  - **ticker**: 600518
  - **name_as_of**: 康美药业
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2019-04-30
  - **allowed_domains**:
    - cninfo.com.cn
    - sse.com.cn
- **scenario_authoring**:
  - **dataset**: official_exchange_and_issuer_filings
  - **access**: read_only
  - **matching_group**: annual-audit-opinion-star-st-regime-v1
  - **matching_role**: no_event
  - **matching_axes**:
    - annual_report_disclosed
    - nonstandard_financial_statement_opinion
    - pre_event_not_star_st
    - opinion_type_contrast
  - **rule_snapshot_id**: sse-main-2018-11-13.2.1-4
  - **exact_contract**: new_star_st_from_latest_annual_financial_audit_opinion-v1
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **1206168292.PDF**: 9f47aa0dc0a8838ffd21e600d7eca194052d91cf867d8e22a4ba56dee2b9f60a
  - **leakage_guard**: Corpus contains the as-of annual report and contemporaneous rule only; later other-risk-warning ST status remains label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_other_risk_warning_notice
    - **title**: 康美药业关于公司股票交易实施其他风险警示暨停牌的提示性公告
    - **published_at**: 2019-05-18
    - **url**: https://static.cninfo.com.cn/finalpage/2019-05-18/1206283586.PDF
    - **effective_at**: 2019-05-21
    - **fields**:
      - ST康美
      - 其他风险警示
      - 关联方资金往来
  - **item 2**:
    - **type**: official_exchange_security_name_snapshot
    - **title**: 上交所2019年5月31日指数样本调整公告仍列示ST康美
    - **published_at**: 2019-05-31
    - **url**: https://www.sse.com.cn/market/sseindex/diclosure/c/c_20190531_4830732.shtml
    - **fields**:
      - 600518
      - ST康美

</details>

# cn-a-2020-occupation-star-st-regime-600702

## Question

你处在2020-09-21收盘后的信息环境。舍得酒业已确认间接控股股东及关联方未按承诺归还大额非经营性资金占用，公司公告次日起将按当时上交所规则实施其他风险警示ST。请只使用下方冻结资料，判断公司是否会在固定70个自然日窗口内因该资金占用首次被实施退市风险警示*ST。必须按2020年有效规则区分ST和*ST，不能倒套2024年新增的责令改正—停牌—*ST规范类退市链条。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 舍得酒业 (600702, SSE)
- 信息截止 / As of: 2020-09-21
- 预测窗口结束 / Window end: 2020-11-30
- 目标事件 / Target: `new_star_st_from_nonoperating_fund_occupation_70d`
- 判定定义 / Definition: 公司在as-of后70个自然日内，因控股股东或其关联方非经营性资金占用触及当时适用的规范类强制退市风险警示条款而首次被实施退市风险警示（证券简称冠以“*ST”）。仅实施其他风险警示“ST”、因其他原因实施*ST、停牌或窗口外事件均不计入

#### 判定条件 / Criteria

- `new_occupation_normative_star_st_effective_count_70d >= 1` — 固定70个自然日窗口内因非经营性资金占用首次生效的规范类*ST次数至少为1

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 上交所股票上市规则（2018年11月修订）：严重资金占用对应其他风险警示ST

- Evidence ID: `sse-2018-occupation-other-risk-rule`
- 发布日期 / Published: 2018-11-16
- 来源 / Source: 上海证券交易所
- URL: https://www.sse.com.cn/lawandrules/sselawsrules2025/repeal/rules/c/c_20181116_10784930.shtml

上证发〔2018〕97号发布并施行《上海证券交易所股票上市规则（2018年11月修订）》。第13.4.1条第（五）项规定，公司被控股股东及其关联方非经营性占用资金或违反规定决策程序对外提供担保，情形严重的，交易所对股票实施其他风险警示。该风险警示对应证券简称冠以ST，而不是退市风险警示*ST；不得以2024年以后新增的规范类强制退市链条追溯改写2020年的规则结果。

### 舍得酒业资金占用公告：4.4亿元本金及3486万元利息逾期，次日起实施ST

- Evidence ID: `600702-2020-occupation-risk-notice`
- 发布日期 / Published: 2020-09-21
- 来源 / Source: 上海证券交易所法定披露
- URL: https://static.sse.com.cn/disclosure/listedinfo/announcement/c/2020-09-21/600702_20200921_1.pdf

截至2020年8月19日，间接控股股东天洋控股及其关联方非经营性占用本金44,000万元、利息3,486万元，合计47,486万元；截至公告日仍未在9月19日承诺期限前归还。公司明确援引当时《股票上市规则》第13.4.1条第（五）项，触发的是其他风险警示，股票自2020年9月22日起简称由舍得酒业变更为ST舍得。公告没有把该资金占用归入退市风险警示*ST。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `new_star_st_from_nonoperating_fund_occupation_70d`
- 结果日期 / Resolved at: 2020-11-30
- 可观察日期 / Observed at: 2020-12-10

### 实际结果 / Realized outcome

- **observations**:
  - **new_occupation_normative_star_st_effective_count_70d**: 0
  - **occupation_other_risk_st_effective_count_70d**: 1
  - **security_name_at_first_post_cutoff_official_filing_is_st_not_star_st**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `sse-2018-occupation-other-risk-rule`
- `600702-2020-occupation-risk-notice`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_rule_regime_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 600702.XSHG
  - **ticker**: 600702
  - **name_as_of**: 舍得酒业
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2020-09-21
  - **allowed_domains**:
    - sse.com.cn
- **scenario_authoring**:
  - **dataset**: official_exchange_and_issuer_filings
  - **access**: read_only
  - **matching_group**: occupation-star-st-historical-regime-v1
  - **matching_role**: no_event
  - **matching_axes**:
    - large_nonoperating_fund_occupation
    - official_rule_trigger_disclosed
    - fixed_70_calendar_day_window
    - st_versus_star_st_boundary
  - **rule_snapshot_id**: sse-main-2018-13.4.1-5
  - **exact_contract**: new_star_st_from_nonoperating_fund_occupation_70d-v1
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **600702_20200921_1.pdf**: 6a964e0c45d9afc2f6b1f2a360c820253ebb51f5d69e6a90bfc69031b665e16d
  - **leakage_guard**: Corpus includes only the as-of occupation facts and the contemporaneous rule classification; status after the prediction cutoff remains label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_post_cutoff_issuer_filing
    - **title**: 舍得酒业关于天洋控股所持公司控股股东股权冻结事项的公告
    - **published_at**: 2020-12-10
    - **url**: https://static.cninfo.com.cn/finalpage/2020-12-10/1208876319.PDF
    - **fields**:
      - 证券代码600702
      - 证券简称ST舍得
      - 未冠以*ST

</details>

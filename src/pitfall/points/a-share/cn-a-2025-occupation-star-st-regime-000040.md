# cn-a-2025-occupation-star-st-regime-000040

## Question

你处在2025-01-05的信息环境。ST旭蓝因控股股东非经营性资金占用已被深圳证监局责令六个月内改正；截至最新官方公告，75.27亿元仍未偿还、无明确计划，整改期在as-of届满。请只使用下方冻结资料，按2024年修订规则推演期限届满后的停牌与两个月整改链条，判断公司是否会在固定70个自然日窗口内因该资金占用首次被实施退市风险警示*ST。不要把as-of时已经存在的其他风险警示ST计作目标事件。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: ST旭蓝 (000040, SZSE)
- 信息截止 / As of: 2025-01-05
- 预测窗口结束 / Window end: 2025-03-16
- 目标事件 / Target: `new_star_st_from_nonoperating_fund_occupation_70d`
- 判定定义 / Definition: 公司在as-of后70个自然日内，因控股股东或其关联方非经营性资金占用触及当时适用的规范类强制退市风险警示条款而首次被实施退市风险警示（证券简称冠以“*ST”）。仅实施其他风险警示“ST”、因其他原因实施*ST、停牌或窗口外事件均不计入

#### 判定条件 / Criteria

- `new_occupation_normative_star_st_effective_count_70d >= 1` — 固定70个自然日窗口内因非经营性资金占用首次生效的规范类*ST次数至少为1

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 深交所股票上市规则（2024年修订）：大额资金占用责令改正、停牌两个月与*ST

- Evidence ID: `szse-2024-occupation-normative-delisting-rule`
- 发布日期 / Published: 2024-04-30
- 来源 / Source: 深圳证券交易所
- URL: https://docs.static.szse.cn/www/lawrules/rule/repeal/rules/W020240430677262007864.pdf

2024年修订规则第8.6条规定，控股股东或其关联人非经营性占用资金余额达到2亿元以上或者最近一期经审计净资产绝对值30%以上，被证监会责令改正但未在要求期限内完成整改的，自期限届满后次一交易日起停牌，停牌不超过两个月。第9.4.1条第（五）项规定，前述情形在停牌两个月内仍未完成整改的，实施退市风险警示；第9.4.7条规定公司在停牌两个月届满后继续停牌一日，自复牌日起实施退市风险警示，简称冠以*ST。

### 东旭蓝天收到深圳证监局责令改正决定：77.96亿元占用须六个月内归还

- Evidence ID: `000040-2024-csrc-correction-order`
- 发布日期 / Published: 2024-07-05
- 来源 / Source: 深圳证监局决定及深交所法定披露
- URL: https://static.cninfo.com.cn/finalpage/2024-07-05/1220543586.PDF

深圳证监局查明东旭蓝天控股股东东旭集团长期、大额非经营性占用上市公司资金，决定对东旭蓝天、东旭集团采取责令改正措施，要求所有占用资金在收到决定书之日起六个月内归还。公司公告明确被占用金额为77.96亿元；若六个月内未清收，规则链条为先停牌，停牌后两个月仍未完成整改则实施退市风险警示。

### ST旭蓝整改期届满前最后风险公告：75.27亿元未偿还且无明确计划

- Evidence ID: `000040-2025-predeadline-progress`
- 发布日期 / Published: 2025-01-03
- 来源 / Source: 深交所法定信息披露
- URL: https://static.cninfo.com.cn/finalpage/2025-01-03/1222207746.PDF

公司披露，2024年9月26日仅收到控股股东归还2.69亿元；截至2025年1月3日，非经营性占用余额75.27亿元仍未偿还，也未提出明确偿还计划，清收无实质性进展。六个月责令整改期限将于2025年1月5日届满，预计难以按期完成；依据第8.6条，公司可能自1月6日起停牌，停牌期限不超过两个月，停牌后两个月仍未整改则实施退市风险警示。as-of时已有的ST来自其他风险警示，不等于目标*ST。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `new_star_st_from_nonoperating_fund_occupation_70d`
- 结果日期 / Resolved at: 2025-03-07
- 可观察日期 / Observed at: 2025-03-07

### 实际结果 / Realized outcome

- **observations**:
  - **new_occupation_normative_star_st_effective_count_70d**: 1
  - **nonoperating_fund_occupation_balance_at_suspension_end_yuan**: 7527000000
  - **occupation_remediation_completed_by_suspension_end**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `szse-2024-occupation-normative-delisting-rule`
- `000040-2024-csrc-correction-order`
- `000040-2025-predeadline-progress`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_rule_regime_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000040.XSHE
  - **ticker**: 000040
  - **name_as_of**: ST旭蓝
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2025-01-05
  - **allowed_domains**:
    - cninfo.com.cn
    - szse.cn
    - csrc.gov.cn
- **scenario_authoring**:
  - **dataset**: official_regulator_exchange_and_issuer_filings
  - **access**: read_only
  - **matching_group**: occupation-star-st-historical-regime-v1
  - **matching_role**: event
  - **matching_axes**:
    - large_nonoperating_fund_occupation
    - official_rule_trigger_disclosed
    - fixed_70_calendar_day_window
    - st_versus_star_st_boundary
  - **rule_snapshot_id**: szse-main-2024-8.6-9.4.1-5-9.4.7
  - **exact_contract**: new_star_st_from_nonoperating_fund_occupation_70d-v1
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **szse_2024_listing_rules.pdf**: df0ea12983df0d577fd1f0154d3bf1a1aea2378b0631d6ef2d4c04b0a96bfeea
    - **1222207746.PDF**: 85fdb575dd6d1367eadd8527e0e67fcf681f21dce9e5fa7d101b3b691f48f370
    - **1220543586.PDF**: 2d287f52a5fb22e749acd25718d295b8bf0ec047cc2163a01cd7636e7a3bf91e
  - **leakage_guard**: Corpus stops at the final pre-deadline risk announcement and contains no post-as-of suspension or *ST outcome notice.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_risk_warning_notice
    - **title**: 东旭蓝天关于公司股票将被实施退市风险警示及继续被实施其他风险警示暨停复牌安排的公告
    - **published_at**: 2025-03-06
    - **url**: https://static.cninfo.com.cn/finalpage/2025-03-06/1222722328.PDF
    - **effective_at**: 2025-03-07
    - **fields**:
      - 75.27亿元未清收
      - 停牌两个月仍未完成整改
      - *ST旭蓝
      - 退市风险警示起始日2025年3月7日

</details>

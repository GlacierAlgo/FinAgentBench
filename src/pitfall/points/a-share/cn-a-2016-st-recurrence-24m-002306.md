# cn-a-2016-st-recurrence-24m-002306

## Question

你处在2016-05-16收盘后的信息环境。中科云网刚刚完整撤销退市风险警示。请使用冻结材料，预测未来24个自然月内股票是否会再次被实施ST或*ST。区分2015年利润与净资产转正是持续经营修复，还是资产处置、债务处置与业务收缩形成的一次性跨线；同时评估仅保留团膳后的收入规模、现金创造、审计质量和历史治理压力。不要把公司改名次数或管理层好坏直接当作标签，也不要使用2016-05-16之后的年报或风险警示结果。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 中科云网 (002306, SZSE)
- 信息截止 / As of: 2016-05-16
- 预测窗口结束 / Window end: 2018-05-16
- 目标事件 / Target: `risk_warning_recurrence_after_full_removal_24m`
- 判定定义 / Definition: 公司股票在2016-05-16完整撤销全部风险警示后24个自然月内，再次被交易所实施任一种ST或*ST风险警示并实际生效。董事会提示风险、年报触及财务指标但尚未生效、债券被标ST、仅停牌或监管问询均不计入；同一实控人延续只是可用的预测证据，不是标签条件

#### 判定条件 / Criteria

- `risk_warning_recurrence_count_after_full_removal_24m >= 1` — 完整摘帽生效后的24个月内，股票再次实际进入ST或*ST状态至少一次

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 中科云网2014年年报：巨额亏损、负净资产与无法表示意见

- Evidence ID: `annual-2014-loss-audit-and-negative-equity`
- 发布日期 / Published: 2015-04-29
- 来源 / Source: 巨潮资讯法定年度报告
- URL: https://static.cninfo.com.cn/finalpage/2015-04-29/1200935444.PDF

公司2014年营业收入约6.2121亿元、归母净利润约-6.8374亿元、年末归母净资产约-0.8642亿元，资产减值损失约4.3756亿元；年审机构对财务报表出具无法表示意见。该历史基线说明上一轮风险警示同时包含经营亏损、净资产与报告可靠性压力，不能因下一年跨过摘帽门槛就机械认定风险永久消失。

### 2015年重大资产出售问询回复：剥离酒楼等资产并收缩至团膳业务

- Evidence ID: `restructuring-2015-retains-group-meals`
- 发布日期 / Published: 2015-12-18
- 来源 / Source: 巨潮资讯交易所问询回复
- URL: https://static.cninfo.com.cn/finalpage/2015-12-18/1201844479.PDF

公司重大资产出售方案剥离酒楼、食品加工和快餐等亏损业务，并保留团膳业务。此举能够减少亏损资产并释放处置收益，但也显著收缩经营边界；判断后续是否再次触发风险警示，应把持续主营盈利与处置交易带来的报表改善分开。

### 中科云网撤销退市风险警示公告：2015年盈利转正但净资产缓冲较薄

- Evidence ID: `full-removal-2016-thin-equity-cushion`
- 发布日期 / Published: 2016-05-13
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2016-05-13/1202319588.PDF

深交所同意自2016年5月16日起撤销股票交易退市风险警示，简称恢复为中科云网。经审计的2015年营业收入376,635,854.89元、归母净利润65,574,042.66元、归母净资产19,363,156.92元；公司也已于2016年3月完成ST湘鄂债兑付。摘帽是交易所状态的完整撤销，但不足0.2亿元的期末归母净资产意味着下一年度亏损对净资产的容错空间仍然有限。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `risk_warning_recurrence_after_full_removal_24m`
- 结果日期 / Resolved at: 2017-04-27
- 可观察日期 / Observed at: 2017-04-26

### 实际结果 / Realized outcome

- **observations**:
  - **risk_warning_recurrence_count_after_full_removal_24m**: 1
  - **calendar_days_from_full_removal_to_recurrence**: 346
  - **full_removal_effective_before_window**: 1
  - **same_controller_at_recurrence**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `annual-2014-loss-audit-and-negative-equity`
- `restructuring-2015-retains-group-meals`
- `full-removal-2016-thin-equity-cushion`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_st_recurrence_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002306.XSHE
  - **ticker**: 002306
  - **name_as_of**: 中科云网
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2016-05-16
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - symbol_change
    - is_st
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=002306.XSHE; if_adjusted=0; 2014q4 and 2015q4 earliest point-in-time rows available by as_of; risk-warning transitions checked on effective dates
  - **matching_group**: full-removal-risk-warning-recurrence-24m-v1
  - **matching_role**: event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2014_annual_report**: d322ee06d9ebe8967129b0a29192a659af11f4786c400d1ea99c6581f04e125e
    - **2015_restructuring_inquiry_response**: caf67e2a89bf2d5ccd910c3552a5fe2c1d3fb24cfa7cb8dd94e3b419e03d2c1a
    - **2016_full_removal_notice**: 7fe8062688237f8c96b61d9257330762b3012d72e50e128792fc4c169fa1543a
    - **2017_recurrence_notice**: 65cb95ae32d75815de75352a3313131dc051d3feeb74f01d1e8cb76bda9fcd47
  - **outcome_contract**: Only a stock-level ST/*ST status that becomes effective after full removal and no later than 24 calendar months counts.
  - **leakage_guard**: The 2016 annual loss, 2017 renewed *ST status, later controller change and subsequent warning removals remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_risk_warning_notice
    - **title**: 关于公司股票交易被实行退市风险警示暨停牌的公告
    - **published_at**: 2017-04-26
    - **url**: https://static.cninfo.com.cn/finalpage/2017-04-26/1203386418.PDF
    - **effective_at**: 2017-04-27
    - **result**: 公告明确股票自2017-04-27起被实行退市风险警示，简称变更为*ST云网
  - **item 2**:
    - **type**: official_annual_report
    - **title**: 中科云网科技集团股份有限公司2016年年度报告
    - **published_at**: 2017-04-26
    - **url**: https://static.cninfo.com.cn/finalpage/2017-04-26/1203386420.PDF
    - **fields**:
      - **revenue_rmb**: 100286000
      - **net_profit_parent_rmb**: -54078000
      - **equity_parent_rmb**: -32094700
    - **result**: 2016年经审计归母净资产为负，触发再次实施退市风险警示
  - **item 3**:
    - **type**: rqdata_point_in_time_status
    - **paths**:
      - data/db/symbol_change.parquet
      - data/db/is_st.parquet
    - **source**: aliyun:/dev/data1/download_rqdata
    - **access**: read_only
    - **effective_at**: 2017-04-27
    - **symbol**: *ST云网
    - **is_st**: true

</details>

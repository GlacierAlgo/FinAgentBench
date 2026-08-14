# cn-a-2015-acquisition-commitment-validation-000547

## Question

你处在2015-07-23收盘后的信息环境。神州学人收购南京长峰100%股权的资产交割、新增股份登记和配套融资主要事项已经完成，承诺期延伸至2017年度。请使用下方冻结资料，预测南京长峰2017年度能否达到target定义的末年承诺验证。请综合军工仿真与电子对抗业务基础、历史利润、订单和客户集中、关联交易、保密与政策、研发投入、配套募资项目及承诺增速；不得把国资背景、完成过户或之后的公司更名直接当作兑现。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 神州学人 (000547, SZSE)
- 信息截止 / As of: 2015-07-23
- 预测窗口结束 / Window end: 2018-07-23
- 目标事件 / Target: `acquisition_terminal_commitment_validated_at_registered_outcome_within_36_month_window`
- 判定定义 / Definition: 以重组文件约定的承诺口径，在预先登记的业绩承诺末年，标的资产实际扣非归母净利润不低于当年承诺值；更名、股价和事后补偿是否完成不作为判定条件

#### 判定条件 / Criteria

- `terminal_commitment_completion_ratio >= 1.0` — 承诺末年标的资产实际扣非归母净利润除以当年承诺净利润不低于1

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 神州学人发行股份购买南京长峰100%股权并募集配套资金报告书

- Evidence ID: `nanjing-changfeng-restructure-plan`
- 发布日期 / Published: 2014-09-20
- 来源 / Source: 神州学人法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2014-09-20/1200250610.PDF

重组报告书披露收购南京长峰100%股权的方案、室内射频仿真试验系统、有源靶标模拟和仿真雷达业务、历史财务及主要客户。盈利补偿安排给出2014至2017年度扣非归母净利润预测值，其中2017年度为15,035.88万元；材料也提示军品定价、客户集中、关联交易、研发和保密等风险。

### 神州学人发行股份购买资产实施情况暨新增股份上市报告书摘要

- Evidence ID: `nanjing-changfeng-acquisition-implemented`
- 发布日期 / Published: 2015-07-23
- 来源 / Source: 神州学人法定公告（巨潮资讯）
- URL: https://static.cninfo.com.cn/finalpage/2015-07-23/1201334500.PDF

实施报告确认南京长峰100%股权已于2015年6月18日过户，资产交割和新增股份登记等主要事项完成，南京长峰成为上市公司全资子公司。报告称新业务将扩大公司主营范围，并披露配套融资约5.405亿元主要投向南京长峰的境外研发、飞行训练模拟器、靶标和半实物仿真项目；同时说明重组后将增加与航天科工体系的经常性关联交易。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `acquisition_terminal_commitment_validated_at_registered_outcome_within_36_month_window`
- 结果日期 / Resolved at: 2017-12-31
- 可观察日期 / Observed at: 2018-04-04

### 实际结果 / Realized outcome

- **observations**:
  - **terminal_actual_adjusted_profit**: 155966800.0
  - **terminal_committed_adjusted_profit**: 150358800.0
- **derivations**:
  - **item 1**:
    - **metric**: terminal_commitment_completion_ratio
    - **operation**: ratio
    - **inputs**:
      - terminal_actual_adjusted_profit
      - terminal_committed_adjusted_profit
    - **value**: 1.0372974511634836

### 对应的题内资料 / Expected evidence

- `nanjing-changfeng-restructure-plan`
- `nanjing-changfeng-acquisition-implemented`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_name_business_transition_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 000547.XSHE
  - **ticker**: 000547
  - **name_as_of**: 神州学人
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2015-07-23
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
  - **row_policy**: stock_code=000547.XSHE; if_adjusted=0; earliest info_date used only for issuer-level cross-check; official commitment audit is label authority
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **news_evidence_policy**: Frozen evidence is limited to contemporaneous issuer filings.
  - **causal_guardrail**: The label evaluates the terminal annual commitment at the acquired target, not the wisdom of the acquisition under a counterfactual.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **nanjing-changfeng-restructure-plan**: dc9df8c35b58125a8521916591262669c0cde0bc44222f399042d3108faa2412
    - **nanjing-changfeng-acquisition-implemented**: 10b3704dab6801bb495fff088df5417e40ae842a5ce83954edf2d2c9704cf32d
- **label_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **outcome_source_sha256**:
    - **1204587552.PDF**: 37b906ddaa93d4003110c7c18fc51fdfb5bb1c9360eebae79df2970744d3a8f4
- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 关于南京长峰航天电子科技有限公司盈利预测实现情况的专项审核报告
    - **published_at**: 2018-04-04
    - **url**: https://static.cninfo.com.cn/finalpage/2018-04-04/1204587552.PDF
    - **fields**:
      - 2017年度预测扣非归母净利润
      - 2017年度实际扣非归母净利润
      - 完成率

</details>

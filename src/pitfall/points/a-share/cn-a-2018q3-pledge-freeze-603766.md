# cn-a-2018q3-pledge-freeze-603766

## Question

你处在2018-10-31收盘后的信息环境。请使用下方冻结资料，预测隆鑫通用原控股股东隆鑫控股未来12个月内所持上市公司股份是否会发生target定义的重大司法冻结。请核对季度股东表与10月补充质押公告的不同统计时点，综合接近满仓且反复补充质押的轨迹、质押用途、上市公司经营现金流与债务缓冲，并严格区分上市公司财务和控股股东偿债能力。不要把高质押机械等同于冻结，也不要把公司关于风险可控或不影响控制权的陈述当作外部验证。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 隆鑫通用 (603766, SSE)
- 信息截止 / As of: 2018-10-31
- 预测窗口结束 / Window end: 2019-10-31
- 目标事件 / Target: `material_controller_share_judicial_freeze`
- 判定定义 / Definition: as-of后12个月内，原控股股东所持上市公司股份被新增司法冻结，且冻结股份数占其as-of持股数不低于10%；普通质押状态不等于司法冻结，本规则不声称接近满仓质押必然导致冻结

#### 判定条件 / Criteria

- `controller_judicial_freeze_to_as_of_holding >= 0.1` — 预测窗口内新增司法冻结股份数除以原控股股东as-of持股数不低于10%

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 隆鑫通用关于控股股东部分股份补充质押的公告：累计98.42%

- Evidence ID: `2018-repeated-supplemental-pledge`
- 发布日期 / Published: 2018-10-18
- 来源 / Source: 新浪财经法定公告镜像
- URL: https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=4805069&stockid=603766

公告披露，隆鑫控股针对2017年10月25日的一笔质押，继2018年6月补充质押585万股后，于10月16日再补充质押536万股；本次不涉及新增融资，并被称为降低预警线和平仓线。截至公告时隆鑫控股持有1,045,591,564股，累计质押1,029,024,083股，占其持股98.42%。公司称不会导致控制权变更、如有平仓风险将提前购回；反复补充质押和接近满仓质押是压力信号，但仍不能直接推出司法冻结。

### 隆鑫通用2018年第三季度报告：盈利现金流与季度末质押快照

- Evidence ID: `2018-q3-listed-company-buffer`
- 发布日期 / Published: 2018-10-31
- 来源 / Source: 巨潮资讯法定报告
- URL: https://static.cninfo.com.cn/finalpage/2018-10-31/1205560284.PDF

截至2018年9月30日的股东表显示隆鑫控股持有1,045,591,564股，其中1,023,664,083股质押，约占其持股97.90%；10月18日公告提供了更新的98.42%口径。前三季度营业收入79.81亿元、归母净利润6.10亿元、经营现金流5.77亿元；期末货币资金18.19亿元、短期借款4.40亿元、归母净资产61.70亿元。上市公司仍盈利且现金为正，是反向证据，但其财务报表不能覆盖控股股东自身股票质押债务，必须避免主体混同。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `material_controller_share_judicial_freeze`
- 结果日期 / Resolved at: 2019-10-21

### 实际结果 / Realized outcome

- **observations**:
  - **newly_judicially_frozen_shares**: 382947481
  - **as_of_controller_holding**: 1045591564
- **derivations**:
  - **item 1**:
    - **metric**: controller_judicial_freeze_to_as_of_holding
    - **operation**: ratio
    - **inputs**:
      - newly_judicially_frozen_shares
      - as_of_controller_holding
    - **value**: 0.36624958940468266

### 对应的题内资料 / Expected evidence

- `2018-repeated-supplemental-pledge`
- `2018-q3-listed-company-buffer`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_traps_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 603766.XSHG
  - **ticker**: 603766
  - **name_as_of**: 隆鑫通用
  - **exchange**: SSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2018-10-31
  - **allowed_domains**:
    - cninfo.com.cn
    - sina.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_cash_flow_pit
    - rq_balance_sheet_pit
  - **row_policy**: stock_code=603766.XSHG; if_adjusted=0; 2018q3 first visible row; official notices are authority for pledge/freeze state
  - **data_lake_gap**: The local RQData snapshot has no populated share_pledge/share_freeze values for this period; official notices and reports are authority.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0; Rust CLI; PDFium native text; --no-ocr
  - **source_sha256**:
    - **2018_q3_report**: ca8d85ac4a46904a0b2e7ac54f0dc9846cd6f48357f6bd99e39d190c077f6890
    - **2019_q3_outcome**: ae1ddf9c97d7b5c8ff77213c3daba1101b6bcdfd9e21fdba61b2a3c21dfde8f3
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 隆鑫通用2019年第三季度报告
    - **published_at**: 2019-10-29
    - **url**: https://static.cninfo.com.cn/finalpage/2019-10-29/1207030036.PDF
    - **outcome**: 公司披露隆鑫控股因股票质押违约被司法冻结382,947,481股，冻结期三年；占其持股36.62%、占公司总股本18.65%
    - **fields**:
      - 司法冻结股份数
      - 冻结原因
      - 控股股东持股数

</details>

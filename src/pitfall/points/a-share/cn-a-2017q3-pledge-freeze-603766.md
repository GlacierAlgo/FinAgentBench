# cn-a-2017q3-pledge-freeze-603766

## Question

你处在2017-10-26收盘后的信息环境。请使用下方冻结资料，预测隆鑫通用原控股股东隆鑫控股未来12个月内所持上市公司股份是否会发生target定义的重大司法冻结。请核对季度股东表与同日质押公告的不同统计时点，综合质押用途与比例、是否反复补充质押、上市公司经营现金流与债务缓冲，并严格区分上市公司财务和控股股东偿债能力。不要把接近满仓质押机械等同于必然冻结，也不要把公司自述的风险可控当作外部验证。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 隆鑫通用 (603766, SSE)
- 信息截止 / As of: 2017-10-26
- 预测窗口结束 / Window end: 2018-10-26
- 目标事件 / Target: `material_controller_share_judicial_freeze`
- 判定定义 / Definition: as-of后12个月内，原控股股东所持上市公司股份被新增司法冻结，且冻结股份数占其as-of持股数不低于10%；普通质押状态不等于司法冻结，本规则不声称接近满仓质押必然导致冻结

#### 判定条件 / Criteria

- `controller_judicial_freeze_to_as_of_holding >= 0.1` — 预测窗口内新增司法冻结股份数除以原控股股东as-of持股数不低于10%

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 隆鑫通用关于控股股东股份质押的公告：同日更新至97.65%

- Evidence ID: `2017-same-day-pledge-liquidity`
- 发布日期 / Published: 2017-10-26
- 来源 / Source: 中国证券报法定信息披露版
- URL: https://epaper.cs.com.cn/zgzqb/images/2017-10/26/B035/ZQBXP0351026C.pdf

公告披露，隆鑫控股将2,376.7083万股质押给中国国际金融股份有限公司，期限一年，主要用于补充流动资金。公告时隆鑫控股持有1,034,440,128股，累计质押1,010,097,083股，占其持股97.65%。发行人称隆鑫控股具备偿还能力、不存在由此产生的质押风险；这是管理层陈述而非债权人或现金流证据。该同日公告晚于三季报的9月30日股东表，应以97.65%作为as-of最新质押比例。

### 隆鑫通用2017年第三季度报告：上市公司现金缓冲与较早质押快照

- Evidence ID: `2017-q3-listed-company-buffer`
- 发布日期 / Published: 2017-10-26
- 来源 / Source: 巨潮资讯法定报告
- URL: https://static.cninfo.com.cn/finalpage/2017-10-26/1204069859.PDF

截至2017年9月30日的股东表显示隆鑫控股持有1,034,440,128股，其中916,330,000股处于质押状态；这是季度末快照，不包含10月25日新增质押。前三季度营业收入72.68亿元、归母净利润6.91亿元、经营现金流4.81亿元；期末货币资金14.21亿元、短期借款0.41亿元、归母净资产63.43亿元。上市公司经营和流动性仍有缓冲，是重大冻结的反向证据，但不能直接证明控股股东层面的债务与偿付能力。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `material_controller_share_judicial_freeze`
- 结果日期 / Resolved at: 2018-10-26

### 实际结果 / Realized outcome

- **observations**:
  - **newly_judicially_frozen_shares**: 0
  - **as_of_controller_holding**: 1034440128
- **derivations**:
  - **item 1**:
    - **metric**: controller_judicial_freeze_to_as_of_holding
    - **operation**: ratio
    - **inputs**:
      - newly_judicially_frozen_shares
      - as_of_controller_holding
    - **value**: 0.0

### 对应的题内资料 / Expected evidence

- `2017-same-day-pledge-liquidity`
- `2017-q3-listed-company-buffer`

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
  - **latest_published_at**: 2017-10-26
  - **allowed_domains**:
    - cninfo.com.cn
    - cs.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_cash_flow_pit
    - rq_balance_sheet_pit
  - **row_policy**: stock_code=603766.XSHG; if_adjusted=0; 2017q3 first visible row; official notices are authority for pledge/freeze state
  - **data_lake_gap**: The local RQData snapshot has no populated share_pledge/share_freeze values for this period; official notices and reports are authority.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0; Rust CLI; PDFium native text; --no-ocr
  - **source_sha256**:
    - **2017_q3_report**: 4081b5aaf6412ca88fe2b558534c4d38ea631637ff4a28ef7fb0ad78904cb028
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_notice_mirror
    - **title**: 隆鑫通用关于控股股东部分股份补充质押的公告
    - **published_at**: 2018-10-18
    - **url**: https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=4805069&stockid=603766
    - **outcome**: 窗口末前最新质押公告仍披露为补充质押，累计质押98.42%；经上市公司法定公告历史核对，2017-10-27至2018-10-26未披露控股股东股份司法冻结
  - **item 2**:
    - **type**: official_filing
    - **title**: 隆鑫通用2018年第三季度报告
    - **published_at**: 2018-10-31
    - **url**: https://static.cninfo.com.cn/finalpage/2018-10-31/1205560284.PDF
    - **fields**:
      - 控股股东持股数
      - 质押或冻结情况

</details>

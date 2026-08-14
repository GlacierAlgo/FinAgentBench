# cn-a-2025-micron-cleanroom-transmission-688376

## Question

你处在2025-12-18 A股开盘前。美光刚披露超预期的FY2026第一财季结果，同时在电话会配套材料中指出HBM相对DDR5消耗更多晶圆、额外洁净室空间是扩产所需，而全球各地洁净室建设周期正在拉长。请不要把它简化成‘半导体都利好’：先区分财报/需求的行业基线与洁净室约束这条边际信息，再用截至快照日的主营业务判断美埃科技出售的是瓶颈解决方案、瓶颈的使用品，还是仅有关键词关联。预测未来五个A股交易日是否出现target严格定义的双门槛相对市场路径。给出概率、二元判断、证据ID和简短可审计推理；不得声称已知未来订单或已证明因果。

### 任务边界 / Task boundary

- 标的 / Security: 美埃科技 (688376, SSE STAR)
- 信息截止 / As of: 2025-12-18
- 预测窗口结束 / Window end: 2025-12-24
- 目标事件 / Target: `cross_market_cleanroom_bottleneck_repricing_5_sessions`
- 判定定义 / Definition: 以2025-12-17（快照前最后一个A股交易日）标的与半导体ETF 512480.XSHG的前复权收盘价为共同基准，观察2025-12-18、19、22、23、24五个交易日。若窗口内任一收盘时点，标的累计前复权收盘收益减去ETF同期累计前复权收盘收益达到或超过10个百分点，且截至该时点标的至少有一次收盘价等于RQData当日limit_up，则在两个门槛首次同时成立日记为event；两个门槛可以在不同日期先后出现。盘中触及、超额不足10个百分点、只有涨停或只有超额均不计。标签只描述固定市场路径，不认定美光言论造成股价变化，也不推导订单金额。

#### 判定条件 / Criteria

- `semiconductor_etf_excess_return_10pp_crossed_by_resolution == 1` — 截至裁决日，窗口内至少一个收盘时点相对512480累计超额收益达到10个百分点
- `official_limit_up_close_observed_by_resolution == 1` — 截至同一裁决日，窗口内至少一次收盘价等于RQData当日limit_up

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 美光FY2026第一财季结果：业绩与下一季指引构成行业需求基线

- Evidence ID: `micron-fq1-results-demand-baseline`
- 发布日期 / Published: 2025-12-17
- 来源 / Source: Micron Technology官方投资者关系公告
- URL: https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-results-first-quarter-fiscal-2026

美光FY2026第一财季收入136.4亿美元，上一季给出的指引中点为125亿美元、上沿128亿美元；非GAAP摊薄每股收益4.78美元，高于此前指引上沿3.90美元。公司称AI需求加速并披露创纪录季度，同时给出下一季187亿美元收入中点。这里首先提供的是存储需求与盈利超预期的行业基线，不能单独推出所有A股半导体公司的同等收益路径。

### 美光电话会配套材料：洁净室建设周期是区别于财报超预期的新增约束

- Evidence ID: `micron-cleanroom-marginal-constraint`
- 发布日期 / Published: 2025-12-17
- 来源 / Source: Micron Technology FY2026 Q1 earnings deck
- URL: https://investors.micron.com/static-files/530bd7ed-a8c8-4687-af4a-8c129f740e09

美光说明HBM相对DDR5存在约3比1的晶圆消耗比，后续HBM代际的比例还会上升；满足新增需求需要额外洁净室空间，而不同地区的洁净室建设交付周期正在拉长。公司因此预计DRAM与NAND供给紧张延续至2026年及以后。相对于一般的业绩超预期，这条信息把可检验的边际瓶颈指向洁净室空间及其建设能力；它仍是前瞻判断，不等于任何A股公司已经取得订单。

### 美埃科技2025年半年度报告：风机过滤单元与过滤器是洁净室关键设备

- Evidence ID: `issuer-business-exposure-688376`
- 发布日期 / Published: 2025-08-30
- 来源 / Source: 上交所法定半年度报告（巨潮镜像）
- URL: https://static.cninfo.com.cn/finalpage/2025-08-30/1224623632.PDF

公司长期从事半导体、生物制药等领域工业级超洁净技术，称自身为国内电子半导体洁净室设备企业。主要产品包括风机过滤单元、各类过滤器、空气净化设备以及洁净室墙壁和天花板系统；其中风机过滤单元被披露为半导体等洁净室空气净化的关键设备。公司出售的是洁净室关键设备及解决方案，不是存储芯片本身。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `cross_market_cleanroom_bottleneck_repricing_5_sessions`
- 结果日期 / Resolved at: 2025-12-23
- 可观察日期 / Observed at: 2025-12-23

### 实际结果 / Realized outcome

- **observations**:
  - **baseline_stock_adjusted_close**: 51.6
  - **stock_adjusted_close_on_max_excess_date_by_resolution**: 64.2
  - **baseline_semiconductor_etf_adjusted_close**: 1.412
  - **semiconductor_etf_adjusted_close_on_max_excess_date_by_resolution**: 1.45
  - **semiconductor_etf_excess_return_10pp_crossed_by_resolution**: 1
  - **official_limit_up_close_observed_by_resolution**: 1
  - **limit_up_close_session_count_by_resolution**: 1
  - **aligned_prediction_sessions_by_resolution**: 4
- **derivations**:
  - **item 1**:
    - **metric**: stock_adjusted_close_return_on_max_excess_date_by_resolution
    - **operation**: pct_change
    - **inputs**:
      - baseline_stock_adjusted_close
      - stock_adjusted_close_on_max_excess_date_by_resolution
    - **value**: 0.2441860465116279
  - **item 2**:
    - **metric**: semiconductor_etf_adjusted_close_return_on_max_excess_date_by_resolution
    - **operation**: pct_change
    - **inputs**:
      - baseline_semiconductor_etf_adjusted_close
      - semiconductor_etf_adjusted_close_on_max_excess_date_by_resolution
    - **value**: 0.026912181303116123
  - **item 3**:
    - **metric**: maximum_adjusted_close_excess_return_by_resolution
    - **operation**: difference
    - **inputs**:
      - stock_adjusted_close_return_on_max_excess_date_by_resolution
      - semiconductor_etf_adjusted_close_return_on_max_excess_date_by_resolution
    - **value**: 0.21727386520851177

### 对应的题内资料 / Expected evidence

- `micron-fq1-results-demand-baseline`
- `micron-cleanroom-marginal-constraint`
- `issuer-business-exposure-688376`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_cross_market_bottleneck_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 688376.XSHG
  - **ticker**: 688376
  - **name_as_of**: 美埃科技
  - **exchange**: SSE STAR
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2025-12-18
  - **allowed_domains**:
    - micron.com
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: /Users/yanghh/Documents/code/quant/download_rqdata/data/db
  - **access**: read_only
  - **tables**:
    - rq_adj_fwd_price_daily
    - etf_adj_fwd_price_daily
  - **row_policy**: stock_code=688376.XSHG; benchmark=512480.XSHG; baseline=2025-12-17; prediction sessions=2025-12-18,19,22,23,24; closing prices only
  - **matching_group**: micron-cleanroom-direct-exposure-vs-semantic-neighbors-2025q4-v1
  - **matching_role**: event/direct_cleanroom_equipment_supplier
  - **matched_control**: 688525.XSHG
  - **pdf_text_tool**: run-llama/liteparse 2.12.0 git 2fd644a9e10ceeee7379949a55fa77aaf26d4b9b
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **issuer_h1_report**: ce2df36202647f8abe409a35612f65ab5a6c647b17c16554c5fda1960bc7bb1a
  - **micron_pdf_retrieval_note**: The official Micron IR deck was verified on the issuer event page and indexed official PDF text, but its edge returned HTTP 403 to automated binary retrieval; no local SHA-256 or LiteParse claim is made for that document.
  - **outcome_contract**: Both a >=10 percentage-point adjusted-close excess-return crossing versus 512480 and at least one limit-up close must be observed by the same resolution date.
  - **leakage_guard**: Only Micron materials and issuer reports visible before the 2025-12-18 A-share open enter the corpus; later price rows and the 2025-12-23 market article are label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: rqdata_adjusted_daily_close_and_limit_price
    - **paths**:
      - data/db/rq_adj_fwd_price_daily/trade_date=YYYY-MM-DD/data.parquet
      - data/db/etf_adj_fwd_price_daily/trade_date=YYYY-MM-DD/data.parquet
    - **stock_code**: 688376.XSHG
    - **benchmark**: 512480.XSHG
    - **baseline_date**: 2025-12-17
    - **resolution_date**: 2025-12-23
    - **max_excess_date_by_resolution**: 2025-12-23
    - **limit_up_close_dates_by_resolution**:
      - 2025-12-23
    - **formula**: stock_return=stock_close_t/stock_close_2025_12_17-1; etf_return=etf_close_t/etf_close_2025_12_17-1; excess=stock_return-etf_return; limit_up_close=(stock_close_t==limit_up_t)
    - **stock_partition_sha256**:
      - **2025-12-17**: ab1464bf727f4ba8eb0403fe29ed6f6a69b025200ca861cb08d3df20a2988070
      - **2025-12-18**: 7db51ff646eaae94704e20974371c6dd1c3f53d1735e41005e4a60709727e70e
      - **2025-12-19**: 4b583b2af54f0b9983b3c0009de3afd5772600a9428a83a3defad2907ca1da03
      - **2025-12-22**: 9de4c52bd47d4a313265d2208bb0eb47fa6b6d964dc5af64a1cf5293321d9537
      - **2025-12-23**: 28db283f3e32ccd078c0a8452dc9cd4a2791b6dec0a93e27188f1db1969f4631
    - **etf_partition_sha256**:
      - **2025-12-17**: 4c1ec8ee1dcc26ddfe5b9ae85ee02a77cbaa0e8a563a2d6b36b9b4ca7bbaf262
      - **2025-12-18**: d09f0b6af44714733c3e4483c75bd8aad29a0cca13ae8df1577cbc555583c3bc
      - **2025-12-19**: be4f640078ef1f48b87d5cc72fb397615d575af691c79fbaec9acd954238b31c
      - **2025-12-22**: 11dbc68c820106ba05ae7b006dee6ef369c677b9578fd5191da7c9e8fd6c418d
      - **2025-12-23**: 067d27edf7d1272a232b3b2073ffc1a292292ffd6bf1ab12a422c3ce5bf37815
  - **item 2**:
    - **type**: contemporaneous_market_report_crosscheck_not_label_authority
    - **title**: 卡了存储的脖子？这一基建成巨头扩产瓶颈 A股投下信任票
    - **published_at**: 2025-12-23
    - **url**: https://www.cls.cn/detail/2237626
    - **result**: 报道列示美埃科技、亚翔集成、圣晖集成、柏诚股份当日均涨停；数值标签仍以RQData收盘与limit_up字段为准

</details>

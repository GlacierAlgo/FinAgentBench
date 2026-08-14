# cn-a-2014-new-media-shutdown-12m-002306

## Question

你处在2014-08-25收盘后的信息环境。公司刚由湘鄂情更名为中科云网，并把新媒体、大数据和云服务作为转型方向，家庭智能有线电视云终端项目初步估算投资15亿至25亿元。请使用冻结材料，预测未来12个月内其三处主要新媒体运营实体是否会达到target定义的整体停运。重点评估项目从框架到商业收入的距离、巨额计划与公司资本和现金能力的匹配、内容与渠道依赖、组织扩张速度以及传统餐饮经营压力；更名和宏大叙事不是成功或失败标签。不要使用2014-08-25之后的季报、债务违约、员工解除或年报结果。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 中科云网 (002306, SZSE)
- 信息截止 / As of: 2014-08-25
- 预测窗口结束 / Window end: 2015-08-25
- 目标事件 / Target: `principal_new_media_operating_entities_shutdown_12m`
- 判定定义 / Definition: 未来12个月内，公司正式披露承载新媒体业务的深圳、北京和上海主要运营实体已全部解除核心员工劳动关系、不再具备业务发展能力，或通过清算、注销、出售等同等方式完成实质性整体停运。单个团队裁员、项目延期、业务亏损、未产生收入或战略收缩但仍保留主要运营能力均不计

#### 判定条件 / Criteria

- `principal_new_media_operating_entities_shutdown_count_12m >= 3` — 深圳、北京、上海三处主要新媒体运营实体均在窗口内被正式确认实质停运

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 家庭智能有线电视云终端项目：初步估算投资15亿至25亿元

- Evidence ID: `data-cloud-project-15bn-plan`
- 发布日期 / Published: 2014-07-29
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2014-07-29/1200084698.PDF

公司公告家庭智能有线电视云终端项目，初步估算投资总额约15亿至25亿元，作为新媒体和大数据转型的一部分。公告给出了庞大的用户入口、内容和数据运营构想，同时明确拟通过定向募集资金和自有资金解决资金来源，无法达到融资目标可能不利于现金流；宣布投资规模不等于已形成商业闭环。

### 公司及证券简称变更：湘鄂情更名中科云网

- Evidence ID: `rename-to-zhongke-cloud-2014`
- 发布日期 / Published: 2014-08-25
- 来源 / Source: 证券时报刊载的发行人法定公告
- URL: https://epaper.stcn.com/paper/zqsb/page/1/2014-08/25/B039/20140825B039_pdf.pdf

公司名称由北京湘鄂情集团股份有限公司变更为中科云网科技集团股份有限公司，证券简称由湘鄂情变更为中科云网，证券代码仍为002306。更名反映战略表达和身份切换，但没有提供新媒体收入、用户留存、渠道落地或现金回收的独立验证，因此必须从项目融资与执行能力预测运营实体能否存续。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `principal_new_media_operating_entities_shutdown_12m`
- 结果日期 / Resolved at: 2015-04-16
- 可观察日期 / Observed at: 2015-04-18

### 实际结果 / Realized outcome

- **observations**:
  - **principal_new_media_operating_entities_shutdown_count_12m**: 3
  - **principal_new_media_entity_count**: 3
  - **new_media_income_contribution_confirmed**: 0
  - **business_development_capability_retained**: 0
- **derivations**:


### 对应的题内资料 / Expected evidence

- `data-cloud-project-15bn-plan`
- `rename-to-zhongke-cloud-2014`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_segment_shutdown_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002306.XSHE
  - **ticker**: 002306
  - **name_as_of**: 中科云网
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2014-08-25
  - **allowed_domains**:
    - cninfo.com.cn
    - stcn.com
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - symbol_change
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=002306.XSHE; if_adjusted=0; identity and financial facts limited to info_date<=2014-08-25; shutdown adjudicated only from later issuer disclosure
  - **matching_group**: new-segment-principal-entities-shutdown-12m-v1
  - **matching_role**: event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2014_data_cloud_notice**: a51b984842005172d04da40d95055bacf6636b5e27fb8c544e184b6c2e57573c
    - **2014_rename_notice**: 309bbc25bf1dc91fccaa4c2c821e52bc9402c74eabcdb30049799bb99f78959a
    - **2015_new_media_shutdown_notice**: b64dc1bb17c67dd59ad5058ea17f920b1ce882005d7bc152e961673d3cb65ef9
  - **outcome_contract**: All three principal new-media operating entities must be officially confirmed as operationally incapable or equivalently closed within 12 calendar months.
  - **leakage_guard**: The subsequent quarterly loss, public-bond default, employment terminations, failure to generate revenue, annual audit result and *ST status remain label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_risk_notice
    - **title**: 中科云网科技集团股份有限公司第二十次风险提示公告
    - **published_at**: 2015-04-18
    - **url**: https://static.cninfo.com.cn/finalpage/2015-04-18/1200864366.PDF
    - **sha256**: 7ec10612c538bd87fae680fe4f5655574c7fe4754867d10d451ce0d99d535130
    - **effective_dates**:
      - **深圳中科云智**: 2015-04-08
      - **北京爱猫**: 2015-04-10
      - **上海爱猫**: 2015-04-16
    - **result**: 三地新媒体实体员工劳动关系先后解除，公司确认已不再具备业务发展能力且未形成收入贡献

</details>

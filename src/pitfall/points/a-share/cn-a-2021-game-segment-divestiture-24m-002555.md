# cn-a-2021-game-segment-divestiture-24m-002555

## Question

你处在2021-08-31收盘后的信息环境。三七互娱营业收入全部来自网络游戏，移动游戏占比逾九成；广州三七网络是公司全资控制、承载移动游戏发行和运营的核心子公司。请使用冻结材料，预测未来24个月内是否会发生target定义的重大游戏板块剥离。评估板块与公司战略及收入的绑定程度、子公司盈利与业绩承诺、现金和融资能力、监管与产品周期风险、对渠道和爆款的依赖，以及出售核心资产的机会成本。不得因为游戏行业监管收紧或一般子公司增减就直接给出标签，也不得把少数股权交易、内部重组或非核心子公司处置误判为广州三七网络100%出售。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 三七互娱 (002555, SZSE)
- 信息截止 / As of: 2021-08-31
- 预测窗口结束 / Window end: 2023-08-31
- 目标事件 / Target: `material_game_segment_divestiture_24m`
- 判定定义 / Definition: 未来24个月内，公司将截至快照日贡献至少50%合并收入的核心游戏运营子公司全部股权转让给非合并范围主体并完成控制权交割，使该子公司退出合并报表范围。只披露转让意向、董事会预案、少数股权出售、业务自然萎缩或仍受公司控制的内部重组不计

#### 判定条件 / Criteria

- `material_game_segment_divestiture_count_24m >= 1` — 窗口内至少一次完成100%游戏子公司控制权转让并退出合并范围

<details>
<summary>冻结资料 / Frozen evidence (3)</summary>

### 三七互娱2021年半年报：网络游戏收入占比100%

- Evidence ID: `h1-2021-game-revenue-concentration`
- 发布日期 / Published: 2021-08-31
- 来源 / Source: 巨潮资讯法定半年度报告
- URL: https://static.cninfo.com.cn/finalpage/2021-08-31/1210922096.PDF

2021年上半年营业收入7,538,949,378.53元，其中网络游戏行业收入占100%；移动游戏收入7,067,163,703.89元、占93.74%，网页游戏收入460,286,420.34元、占6.11%。因此，预测核心游戏子公司是否整体出售不能只看行业监管或产品周期，还必须衡量公司几乎全部收入与游戏经营能力的绑定，以及剥离后的业务承接问题。

### 广州三七网络：全资控制的移动游戏发行运营主体

- Evidence ID: `guangzhou-sanqi-controlled-core-subsidiary`
- 发布日期 / Published: 2021-08-31
- 来源 / Source: 巨潮资讯法定半年度报告
- URL: https://static.cninfo.com.cn/finalpage/2021-08-31/1210922096.PDF

半年报在合并范围内列示广州三七网络科技有限公司为持股100%的三级子公司，业务性质为软件和信息技术服务业；主要控股参股公司表将其主要业务明确为移动游戏发行和运营，期末总资产4,692,808,416.27元、净资产2,221,050,907.43元，上半年营业收入3,836,134,123.00元、净利润628,293,962.64元。报告期还披露公司支付收购广州三七网络少数股权款项。该子公司的规模、利润和全资控制状态共同构成出售机会成本，也不能单独保证未来不会重组。

### 三七互娱2021年上半年PIT财务链：经营现金与短债能力

- Evidence ID: `h1-2021-pit-financial-capacity`
- 发布日期 / Published: 2021-08-31
- 来源 / Source: 三七互娱法定半年度报告及只读RQData点时记录
- URL: https://static.cninfo.com.cn/finalpage/2021-08-31/1210922096.PDF

2021年上半年营业收入7,538,949,378.53元、归母净利润853,717,855.65元、经营活动现金流净额1,253,919,152.46元；期末货币资金3,927,610,090.55元、应收账款净额1,361,016,422.73元、短期借款247,063,500.00元、总负债4,504,039,837.22元、总权益9,472,091,294.26元。点时口径为002555.XSHE、2021q2、if_adjusted=0、info_date=2021-08-31。较强的现金和盈利能力意味着公司并无显见的被迫出售动机，但模型仍需结合监管、产品和资本配置风险作出概率判断。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `material_game_segment_divestiture_24m`
- 结果日期 / Resolved at: 2023-08-31
- 可观察日期 / Observed at: 2024-04-20

### 实际结果 / Realized outcome

- **observations**:
  - **material_game_segment_divestiture_count_24m**: 0
  - **ownership_interest_sold**: 0
  - **subsidiary_exited_consolidation**: 0
  - **game_revenue_share_as_of**: 1.0
  - **core_game_subsidiary_still_controlled_after_window**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `h1-2021-game-revenue-concentration`
- `guangzhou-sanqi-controlled-core-subsidiary`
- `h1-2021-pit-financial-capacity`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_segment_exit_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002555.XSHE
  - **ticker**: 002555
  - **name_as_of**: 三七互娱
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2021-08-31
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: aliyun:/dev/data1/download_rqdata
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=002555.XSHE; if_adjusted=0; quarter=2021q2; select the latest row with info_date<=2021-08-31, which is info_date=2021-08-31; subsidiary ownership and deconsolidation adjudicated from issuer filings
  - **matching_group**: material-controlled-segment-divestiture-24m-v1
  - **matching_role**: no_event
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f; Rust CLI; --no-ocr
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **2021_half_year_report**: c92fb1bb5166433f9dddcfa79134692fbdc9b7a5396ec2eac126f281da4e4dac
    - **2021_annual_report**: 1b60d1ee03d4b1dd569164610f2316b25b46ef20181382ffba4df09b141cc290
    - **2022_annual_report**: fadd80f3fd0f9ac2cf5ac28197c2ef17a799c9a66ba62a461a68d31d82082cf5
    - **2023_annual_report**: ae82a8d90504da6a7f5649a907b8e3c01ad6fde4fc9437c9cb3d7d70088ef495
  - **rqdata_file_sha256**:
    - **rq_balance_sheet_pit_2021q2**: 60221ddab91503f1fe04832c56c216c69a9299d517f9289a66986987355d0974
    - **rq_income_statement_pit_2021q2**: 0def586a9467e16ff878cd2e3fa3ade4afca6b9bd74d77d7883898dcb126cb84
    - **rq_cash_flow_pit_2021q2**: d83b8d5fd4bdbaf18c891d897612a95131786fafa98d04e2b3b5168c323220f3
  - **outcome_contract**: A divestiture counts only if 100% of the named controlled game subsidiary transfers outside the group and the issuer confirms that it leaves consolidation within 24 calendar months.
  - **leakage_guard**: The 2021, 2022 and 2023 annual-report continuity checks and later group-scope evidence remain label-side only.
- **corpus_authoring**:
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **1210922096.PDF**: c92fb1bb5166433f9dddcfa79134692fbdc9b7a5396ec2eac126f281da4e4dac
- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_annual_report
    - **title**: 三七互娱网络科技集团股份有限公司2021年年度报告
    - **published_at**: 2022-04-26
    - **url**: https://static.cninfo.com.cn/finalpage/2022-04-26/1213106525.PDF
    - **period_end**: 2021-12-31
    - **result**: 年报继续将广州三七网络列入合并范围并确认其移动游戏发行运营业务及2021年度业绩
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: 1b60d1ee03d4b1dd569164610f2316b25b46ef20181382ffba4df09b141cc290
  - **item 2**:
    - **type**: official_annual_report
    - **title**: 三七互娱网络科技集团股份有限公司2022年年度报告
    - **published_at**: 2023-04-28
    - **url**: https://static.cninfo.com.cn/finalpage/2023-04-28/1216644837.PDF
    - **period_end**: 2022-12-31
    - **result**: 年报明确当年不存在丧失子公司控制权的处置，并继续列示广州三七网络直接19.80%、间接80.20%的合计100%持股
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: fadd80f3fd0f9ac2cf5ac28197c2ef17a799c9a66ba62a461a68d31d82082cf5
  - **item 3**:
    - **type**: official_annual_report
    - **title**: 三七互娱网络科技集团股份有限公司2023年年度报告
    - **published_at**: 2024-04-20
    - **url**: https://static.cninfo.com.cn/finalpage/2024-04-20/1219692344.PDF
    - **period_end**: 2023-12-31
    - **result**: 年报覆盖窗口最后八个月；合并范围变动仅列示其他主体，广州三七网络仍以直接19.80%、间接80.20%的合计100%持股列入企业集团构成，故窗口内未发生目标出售
    - **extraction**:
      - **tool**: run-llama/liteparse 2.11.1 git 5109b46e7f960a52ea9833704c9484c835c6ef4f
      - **mode**: native PDFium text extraction (--no-ocr)
      - **sha256**: ae82a8d90504da6a7f5649a907b8e3c01ad6fde4fc9437c9cb3d7d70088ef495

</details>

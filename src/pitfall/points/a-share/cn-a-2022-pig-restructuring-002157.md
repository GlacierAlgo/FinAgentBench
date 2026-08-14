# cn-a-2022-pig-restructuring-002157

## Question

你处在2022-04-30收盘后的信息环境。正邦科技刚披露巨额猪周期亏损、高负债和控股股东高比例质押，同时公司仍披露大额货币资金、经营安排以及‘目前不存在平仓风险’。请使用下方冻结资料，预测未来24个自然月内是否会发生target严格定义的法院正式受理上市公司重整事件。请拆分猪价与养殖成本、现金和受限资金、短债缺口、经营现金流、股东质押与上市公司偿债能力；不能把跌破估算平仓线、预重整、申请重整、*ST或管理层‘风险可控’表述替代正式法律事件。给出概率、二元判断、证据ID和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 正邦科技 (002157, SZSE)
- 信息截止 / As of: 2022-04-30
- 预测窗口结束 / Window end: 2024-04-30
- 目标事件 / Target: `listed_issuer_formal_judicial_restructuring_acceptance_24m`
- 判定定义 / Definition: 快照日后24个自然月内，有管辖权的人民法院以民事裁定正式受理针对上市公司本身的破产重整申请。法院决定启动或延长预重整、公司或债权人提出申请、签署投资协议、子公司或控股股东重整、法院仅登记审查，以及公司被实施ST或*ST均不计；只有法院正式裁定受理上市公司重整至少一次才计入。

#### 判定条件 / Criteria

- `formal_judicial_restructuring_acceptance_count_24m >= 1` — 窗口内法院正式裁定受理上市公司本身的破产重整至少一次

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 正邦科技2021年年度报告：巨亏、短债陡升且大部分货币资金受限

- Evidence ID: `fy2021-loss-liquidity-and-restricted-cash`
- 发布日期 / Published: 2022-04-30
- 来源 / Source: 巨潮资讯法定定期报告
- URL: https://static.cninfo.com.cn/finalpage/2022-04-30/1213251585.PDF

2021年营业收入476.7022亿元，归母净利润-188.1882亿元，经营活动现金流净额-22.0429亿元；期末归母权益20.3825亿元，资产负债率92.60%。货币资金51.3280亿元，短期借款138.5095亿元、一年内到期非流动负债41.1023亿元，现金/两项短债仅0.286；其中32.9828亿元货币资金因票据保证金、履约保证金等受限。报告同时披露猪价下行、养殖成本和产能调整，但行业周期不能解释存量债务能否续接。

### 正邦科技控股股东质押公告：一致行动体系质押83.91%，公司称不存在平仓风险

- Evidence ID: `controller-pledge-over-80-and-controllable-claim`
- 发布日期 / Published: 2022-02-25
- 来源 / Source: 巨潮资讯法定临时公告
- URL: https://static.cninfo.com.cn/finalpage/2022-02-25/1212453163.PDF

控股股东正邦集团及一致行动人合计持股15.9185亿股、占公司50.59%，质押后13.3569亿股，占其持股83.91%、占总股本42.45%。公司提示质押比例超过80%，并解释高质押形成于参与定增、支付融资本息和多次补充质押；同时称目前不存在平仓风险、质押风险可控，若有风险将补充质押或提前清偿。该表述是当时管理层陈述，不是质权合同平仓线或上市公司流动性的独立证明。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `listed_issuer_formal_judicial_restructuring_acceptance_24m`
- 结果日期 / Resolved at: 2023-07-20
- 可观察日期 / Observed at: 2023-07-21

### 实际结果 / Realized outcome

- **observations**:
  - **formal_judicial_restructuring_acceptance_count_24m**: 1
  - **days_from_as_of_to_first_formal_acceptance**: 446
- **derivations**:


### 对应的题内资料 / Expected evidence

- `fy2021-loss-liquidity-and-restricted-cash`
- `controller-pledge-over-80-and-controllable-claim`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_pig_restructuring_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002157.XSHE
  - **ticker**: 002157
  - **name_as_of**: 正邦科技
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2022-04-30
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: /Users/yanghh/Documents/code/quant/download_rqdata/data/db
  - **access**: read_only
  - **tables**:
    - rq_income_statement_pit
    - rq_balance_sheet_pit
    - rq_cash_flow_pit
  - **row_policy**: stock_code=002157.XSHE; quarter=2021q4; selected earliest info_date=2022-04-30; if_adjusted=0
  - **matching_group**: pig-cycle-formal-issuer-restructuring-24m-2021-v1
  - **matching_role**: event/high_pledge_low_cash_coverage
  - **pdf_text_tool**: run-llama/liteparse 2.12.0 git 2fd644a9e10ceeee7379949a55fa77aaf26d4b9b
  - **pdf_text_mode**: native PDFium text extraction (--no-ocr)
  - **source_sha256**:
    - **fy2021_annual_report**: fa00ecfdcf4bf16e91ea3a7876c60df246c251a0d97e0e928422285376695a8f
    - **pledge_notice**: 9922078f92c08371dd2957420546a12d81bf303cb560e11530c8c4e48f531fec
  - **rqdata_sha256**:
    - **balance_2021q4**: 95031057e95656fd75ae2972db3f4be2865284fe28d12378fc546558f096cb12
    - **income_2021q4**: eaf6c791f8b8f1265be420d5bdabbfe28629acfeaaf0e07351236929def91dc6
    - **cash_flow_2021q4**: 6f555a2cce3ce21eaa5b5ad5e7876d72151f40c856e230a92935e20b2e7453bb
  - **outcome_contract**: Only the date of a competent court's civil ruling formally accepting reorganization of the listed issuer counts; pre-reorganization and filing milestones never count.
  - **leakage_guard**: Only documents published no later than as_of enter the corpus; later court rulings, risk warnings and restructuring outcomes are label-side only.
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_issuer_court_acceptance_notice
    - **title**: 江西正邦科技股份有限公司关于法院裁定受理公司重整并指定管理人暨公司股票交易将被叠加实施退市风险警示的公告
    - **published_at**: 2023-07-21
    - **url**: https://static.cninfo.com.cn/finalpage/2023-07-21/1217348496.PDF
    - **sha256**: a0a2f7528d5e5fada3435324b4ccb4618dff3f083bfb1ceb9e4e35dcc8f36e64
    - **ruling_date**: 2023-07-20
    - **court**: 江西省南昌市中级人民法院
    - **civil_ruling_number**: （2022）赣01破申49号
    - **result**: 南昌中院以民事裁定正式受理债权人对上市公司正邦科技的重整申请

</details>

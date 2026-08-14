# cn-a-2017q3-pledge-control-002310

## Question

你处在2017-10-27收盘后的信息环境。请使用下方冻结资料，预测东方园林未来约12个月内是否会通过股份转让、表决权委托、司法处置或其他安排发生控股股东/实际控制人变更。重点综合实际控制人质押比例、经营现金流、融资需求、股权结构和高速增长基本面；不要把高质押机械等同于控制权必然变化，也不要把相关性写成因果。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 东方园林 (002310, SZSE)
- 信息截止 / As of: 2017-10-27
- 预测窗口结束 / Window end: 2018-10-31
- 目标事件 / Target: `control_transfer_after_high_pledge_risk`
- 判定定义 / Definition: as-of后约12个月内，原实际控制人通过股份转让、表决权委托、司法处置或其他安排使上市公司控股股东或实际控制人发生变更；该规则不声称高质押是唯一原因

#### 判定条件 / Criteria

- `control_transfer_flag >= 1` — 预测窗口内控股股东或实际控制人变更记为1，否则记为0

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 东方园林关于控股股东质押及解除质押的公告

- Evidence ID: `2017-high-pledge`
- 发布日期 / Published: 2017-10-27
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2017-10-27/1204078418.PDF

何巧女持有公司11.14亿股，占总股本41.54%。截至公告日，其累计质押7.63亿股，占个人持股68.55%、占公司总股本28.48%。本次同时发生新增质押和到期解除，公告用途为个人融资。质押比例已经很高，但尚未出现补充质押、冻结或控制权安排。

### 东方园林2017年第三季度报告：高速增长与强现金流

- Evidence ID: `2017-q3-growth-and-cash`
- 发布日期 / Published: 2017-10-21
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2017-10-21/1204056363.PDF

前三季度营业收入86.35亿元，同比增长72.29%；归母净利润8.66亿元，同比增长67.64%；经营活动现金流净额7.23亿元，同比增长236.27%。何巧女仍为持股41.54%的控股股东并与唐凯共同控制公司。强增长、强回款和较大的控制权持股缓冲构成高质押之外的关键反向证据。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件未发生 / no event**
- 目标事件 / Target: `control_transfer_after_high_pledge_risk`
- 结果日期 / Resolved at: 2018-10-31

### 实际结果 / Realized outcome

- **observations**:
  - **control_transfer_flag**: 0
  - **original_controller_still_controls_flag**: 1
- **derivations**:


### 对应的题内资料 / Expected evidence

- `2017-high-pledge`
- `2017-q3-growth-and-cash`

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

- **point_type**: historical_a_share
- **suite**: a_share_traps_v1
- **mode**: historical_frozen_web
- **security**:
  - **order_book_id**: 002310.XSHE
  - **ticker**: 002310
  - **name_as_of**: 东方园林
  - **exchange**: SZSE
- **search_policy**:
  - **mode**: frozen_corpus_only
  - **latest_published_at**: 2017-10-27
  - **allowed_domains**:
    - cninfo.com.cn
- **scenario_authoring**:
  - **dataset**: official CNINFO filings
  - **access**: read_only
  - **data_lake_gap**: main_shareholder.parquet in the local RQData snapshot has no populated share_pledge/share_freeze values for the screened period; official notices are authority.
  - **pdf_text_tool**: run-llama/liteparse 2.11.1 git 53e4fc813d35f76d0169923d2c451b3c8700edb0; Rust CLI; PDFium native text
- **corpus_authoring**:

- **label_authoring**:

- **outcome_sources**:
  - **item 1**:
    - **type**: official_filing
    - **title**: 东方园林2018年第三季度报告
    - **published_at**: 2018-10-31
    - **url**: https://static.cninfo.com.cn/finalpage/2018-10-31/1205562661.PDF
    - **outcome**: 报告仍列示何巧女、唐凯为夫妻并共同作为公司实际控制人，观察窗口内未发生控股股东或实际控制人变更

</details>

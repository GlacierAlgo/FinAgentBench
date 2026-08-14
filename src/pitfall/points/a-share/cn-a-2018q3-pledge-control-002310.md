# cn-a-2018q3-pledge-control-002310

## Question

你处在2018-10-31收盘后的信息环境。请使用下方冻结资料，预测东方园林未来12个月内是否会通过股份转让、表决权委托、司法处置或其他安排发生控股股东/实际控制人变更。重点综合实际控制人质押比例、补充质押、经营现金流、融资环境、股权结构和经营基本面；不要把高质押机械等同于控制权必然变化，也不要把相关性写成因果。给出概率、二元判断、关键证据引用和简短可审计推理。

### 任务边界 / Task boundary

- 标的 / Security: 东方园林 (002310, SZSE)
- 信息截止 / As of: 2018-10-31
- 预测窗口结束 / Window end: 2019-10-31
- 目标事件 / Target: `control_transfer_after_high_pledge_risk`
- 判定定义 / Definition: as-of后12个月内，原实际控制人通过股份转让、表决权委托、司法处置或其他安排使上市公司控股股东或实际控制人发生变更；该规则不声称高质押是唯一原因

#### 判定条件 / Criteria

- `control_transfer_flag >= 1` — 预测窗口内控股股东或实际控制人变更记为1，否则记为0

<details>
<summary>冻结资料 / Frozen evidence (2)</summary>

### 东方园林关于实际控制人质押及解除质押的公告

- Evidence ID: `2018-pledge-supplements`
- 发布日期 / Published: 2018-08-30
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2018-08-30/1205357595.PDF

公告显示何巧女和唐凯多笔新增质押用途为补充质押。截至披露日，何巧女累计质押8.014亿股，占其持股71.95%、占公司总股本29.87%；两位实际控制人及一致行动人累计质押占其合计持股63.70%。补充质押比单纯融资质押提供了更强的价格与流动性压力信号。

### 东方园林2018年第三季度报告：质押集中与现金流骤降

- Evidence ID: `2018-q3-cash-and-pledge`
- 发布日期 / Published: 2018-10-31
- 来源 / Source: 巨潮资讯（深交所法定信息披露平台）
- URL: https://static.cninfo.com.cn/finalpage/2018-10-31/1205562661.PDF

截至2018-09-30，何巧女持有公司41.52%股份，其中质押10.096亿股，约占其持股90.65%；唐凯持股7.65%，质押6,063.21万股。前三季度营业收入96.49亿元、归母净利润9.75亿元，但经营现金流净额仅4,272.65万元，同比下降94.09%。利润仍为正且公司预计全年盈利，是重要反向证据；质押集中和现金转弱则指向融资与控制权压力。

</details>

请直接给出最终答案和必要依据；回答格式自由。

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

- 正确结论 / Outcome: **事件发生 / event**
- 目标事件 / Target: `control_transfer_after_high_pledge_risk`
- 结果日期 / Resolved at: 2019-10-09

### 实际结果 / Realized outcome

- **observations**:
  - **control_transfer_flag**: 1
  - **shares_transferred_to_new_controller_ratio**: 0.05
  - **voting_rights_delegated_ratio**: 0.168
- **derivations**:


### 对应的题内资料 / Expected evidence

- `2018-pledge-supplements`
- `2018-q3-cash-and-pledge`

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
  - **latest_published_at**: 2018-10-31
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
    - **type**: official_control_change_notice
    - **title**: 关于实际控制人协议转让公司股份完成过户登记暨公司控股股东、实际控制人变更完成的公告
    - **published_at**: 2019-10-09
    - **url**: https://static.cninfo.com.cn/finalpage/2019-10-09/1206966985.PDF
    - **outcome**: 何巧女、唐凯向朝汇鑫转让总股本5%并委托总股本16.8%的表决权；朝汇鑫成为控股股东，北京市朝阳区国资委成为实际控制人

</details>

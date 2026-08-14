# PITFALL

*Point-in-time, pointwise evaluation for agentic financial reasoning.*

PITFALL 是一个面向 agent 的金融推理评测库。它只关心一个端到端结果：agent
拿到一个问题后，可以自行使用 Web search、代码、文件或其他工具，最终答案与
Ground Truth 相差多少。

评测单位是独立的 **point**。每个 point 都是一个自包含 Markdown 文件，不依赖
JSON schema，也不要求统一的金融字段、工具流程或回答结构，因此可以持续扩展到
任意领域与任意数量的案例。

**[查看历史 A 股公开雷达 / Open the historical A-share radar](https://glacieralgo.github.io/PITFALL/)**

## Point 合同 / Point contract

唯一规范模板是
[`src/pitfall/points/META.md`](src/pitfall/points/META.md)：

```markdown
# {{id}}

## Question

{{question}}

## Ground Truth

<details>
<summary>评测时隐藏 / Hidden during evaluation</summary>

{{ground_truth}}

</details>

## Provenance

<details>
<summary>按需展开 / Expand for audit</summary>

{{provenance}}

</details>
```

固定的只有文件 ID、三个二级标题及其顺序：

- `Question`：agent 唯一可见的 point 内容；可以自由包含任务边界、资料、链接或工具说明。
- `Ground Truth`：评测时隐藏；以自然语言记录足以判断答案对错的事实与结论。
- `Provenance`：评测时隐藏；记录来源、时间、构造方法和可审计信息。

三个 section 内可以自由使用段落、列表、表格、链接、三级标题和折叠块。不要增加
新的二级标题，也不要在具体 point 中保留 `{{placeholder}}`。这种约束只固定读取
边界，不固定内容本身。

## 六类评分 / Six-class evaluation

评分是六选一的分类，不是从好到坏的六档分数。每个 Answer 必须且只能得到一个
primary class。

| Class | 中文定义 | English boundary |
| --- | --- | --- |
| `completely_correct` | 完全正确：最终答案及所有影响结论的关键主张与 Ground Truth 一致，没有实质错误。 | The answer and every material claim agree with the Ground Truth. |
| `numeric_factual_error` | 事实错误（数值类）：金额、比例、数量、价格、日期差、概率或其他可量化事实错误。直接读错数值归此类。 | A material stated quantity is wrong. |
| `non_numeric_factual_error` | 事实错误（非数值类）：实体、事件、日期本身、状态、方向、制度、来源内容等非数值事实错误。 | A material non-quantitative fact is wrong. |
| `analysis_assumption_error` | 分析假设错误：已知事实可以成立，但答案依赖无依据的前提、代理变量、因果假设、外推或边界设定。 | The conclusion depends on an unsupported analytical premise. |
| `analysis_logic_error` | 分析逻辑错误：事实与假设可接受，但计算、比较、条件组合、因果推导或从证据到结论的映射无效。使用正确数字却算错归此类。 | The reasoning operation from accepted inputs to conclusion is invalid. |
| `other_error` | 其他错误：空答、拒答、严重跑题、不可解析、缺失关键输出，或确实无法归入以上类别的错误。 | The response is unusable or does not fit another error class. |

分类边界：

- “读错数字”是 `numeric_factual_error`；“数字都对但计算错”是 `analysis_logic_error`。
- “说错发生了什么”是 `non_numeric_factual_error`；“事实对但擅自假设为什么发生”是 `analysis_assumption_error`。
- 同一答案出现多种错误时，选择可见推理链中最早导致最终结论失效的决定性错误。
- 只有完全正确才计入 accuracy；另外报告五种错误各自的分布，不把类别压成一个伪精确总分。

Judge 的最小输出合同：

```markdown
Class: {{evaluation_class}}

{{decisive_reason}}
```

`decisive_reason` 只需指出决定分类的最短充分理由，不要求或收集模型的私有思维链。

## 端到端边界 / End-to-end boundary

一个正式 run 的实验对象是完整配置：

`agent/model × harness × instructions × tools × evidence snapshot`

PITFALL 不单独奖励搜索次数、工具调用数或某种固定步骤。Web search 和其他工具属于
agent 完成 Question 的运行环境；评分只比较最终 Answer 与隐藏 Ground Truth。工具
轨迹、耗时、token 与成本可以写入 run artifact，用于复现和诊断，但不进入 point
文件，也不改变六类语义判定。

尚未固定的是 judge 的具体模型、版本和运行策略。这不会阻塞 datapoint authoring：
judge 无论如何都只能接收 `Question + Answer + Ground Truth`，并返回上面的六类之一。
正式比较时必须把 judge 配置与重复评测策略写入 run artifact。

## 数据组织 / Data layout

```text
src/pitfall/points/
├── META.md                 # 唯一模板与标题合同
├── synthetic/              # 12 个合成 smoke points
└── a-share/                # 162 个历史 A 股 points
```

现有 174 个已解析案例已经迁移为 pointwise Markdown。A 股案例把当时可见的冻结资料
放在 Question 内，把事后结果与来源放在隐藏 section 中；每个文件可以独立阅读、复制
和审计。`live_shadow`、issuer dossier、历史 run results 与 radar 是运行或展示资产，
不是 datapoint，因此继续使用各自最合适的存储格式。

## 使用 / Usage

需要 Python 3.11+ 与 [uv](https://docs.astral.sh/uv/)：

```bash
uv sync --dev
uv run pitfall validate
uv run pitfall list
uv run pitfall render goodwill-impairment-risk
uv run pitfall show cn-a-2014-new-industry-scale-600766
```

- `validate`：验证模板、标题顺序、折叠边界、ID 与唯一性。
- `list`：每行输出一个 point ID。
- `render`：只输出 agent 可见的 Question。
- `show`：输出完整自包含 Markdown，供作者审计；不要把它直接交给被评测 agent。

新增 point 时，复制 `META.md`，把四个 `{{value}}` 替换为真实内容，并确保文件名与
`# id` 相同。通常不需要修改 Python、注册 suite 或新增测试；通用验证器会自动发现
子目录中的所有 `.md` 文件。

## English summary

PITFALL stores each evaluation unit as a self-contained Markdown point with
exactly three sections: the agent-visible Question, hidden Ground Truth, and
hidden Provenance. Agents may use any configured tools and answer freely. A
judge compares the final Answer with Ground Truth and assigns exactly one of six
mutually exclusive classes. The data contract is stable; the concrete judge
runtime remains an experiment-level choice.

## Status

PITFALL is pre-alpha. The 174 public points are development and authoring data,
not a contamination-resistant leaderboard. Historical result artifacts remain
available for audit, while formal rankings should use pre-registered future
cohorts with hidden labels.

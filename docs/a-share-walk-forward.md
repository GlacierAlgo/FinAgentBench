# A-share walk-forward protocol

The objective is zero-shot generalization to future financial events. Historical
examples are development tests, not the end product and not a claim of investable
performance.

## Three evaluation layers

1. **Synthetic smoke** checks response contracts, basic accounting logic, and
   harness plumbing.
2. **Historical frozen-web replay** starts from a real past as-of date. Search is
   restricted to a frozen corpus whose documents were published no later than
   that date. The future outcome is stored separately.
3. **Live shadow evaluation** creates an unresolved case today, permits real web
   search, seals the prediction, and attaches a label only after the horizon
   closes. This is the strongest defense against hindsight leakage and public
   case memorization.

Historical cases must not use today's unrestricted search results: a result
title, snippet, revised filing, company rename, or retrospective article can
reveal the later event even when the agent never opens the page.

## Version 1 impairment target

The first slice asks whether the asset-impairment loss confirmed in the 2019
annual report exceeds 10% of equity attributable to the parent at 2019Q3. It has
three positives and three high-goodwill negatives:

| Ticker | As-of name | Outcome |
| --- | --- | --- |
| 002739 | 万达电影 | event |
| 002681 | 奋达科技 | event |
| 300467 | 迅游科技 | event |
| 300058 | 蓝色光标 | no event |
| 002425 | 凯撒文化 | no event |
| 300276 | 三丰智能 | no event |

The public outcome table is documentation for the development set. A scored
agent receives only the scenario payload and results returned by the frozen
search interface.

## Data and row policy

Candidate discovery and labels were built with read-only access to
`aliyun:/dev/data1/download_rqdata`. Only small, auditable facts needed for a
case are checked in; the source data lake is not copied or modified.

For this slice:

- 2019Q3 balance sheet, income statement, and cash-flow rows form the as-of
  snapshot;
- 2019Q4 income statement rows provide the future impairment outcome;
- rows use `if_adjusted = 0` and the earliest `info_date` for each stock and
  quarter, preventing a later restatement from entering an earlier snapshot;
- official CNINFO filings independently anchor both the frozen documents and
  the outcome;
- a positive label requires `abs(asset_impairment_loss) / 2019Q3 parent equity
  > 0.10`.

The `scenarios/`, `corpora/`, and `labels/` directories are intentionally
separate. Validation rejects future-dated corpus documents, non-allowlisted
domains, label dates outside the prediction window, mismatched scenario IDs,
and outcome ratios that do not recompute from the stored numerator and
denominator.

## Version 2 generic outcome target

Business decisions rarely resolve to one accounting line. Schema version 2
therefore declares one or more numeric criteria and whether `all` or `any` must
hold. Labels preserve raw observations and machine-checkable derivations such
as ratios, margins, differences, percentage changes, and CAGR. Validation
recomputes every derived metric and then recomputes the event label from the
scenario's published criteria.

The first case starts from 海光信息 on 2022-08-11. It asks whether the company's
pre-listing R&D and CPU/DCU product roadmap will receive commercial validation
by FY2024. The event requires all of:

- 2021-2024 revenue CAGR of at least 30%;
- FY2024 gross margin of at least 50%;
- positive FY2024 operating cash flow.

The frozen evidence includes the official IPO inquiry replies and listing
announcement plus contemporaneous news available by the as-of date. It exposes
competing evidence: product generations, customer certification and orders on
one side; market share, R&D capitalization, customer/related-party
concentration, export-control and supply-chain risks on the other. News supplies
an independently selected market framing, but the later annual report and
RQData PIT rows remain the label authority and label-only.

This rule is intentionally called **commercial validation**, not R&D causal
impact. Observational financial outcomes cannot establish that R&D was the sole
cause. For a Fabless designer such as 海光信息, the relevant allocation choices
are product generations, IP/licensing, tape-out and validation, and software
ecosystem investment—not factory construction.

## Version 3 matched A-share trap families

The next slice adds seven event families with one realized event and one
non-event control each. A benchmark that contains only later blow-ups rewards a
trivial always-distressed policy; matched controls force the agent to use the
strength, timing, and counterevidence in the frozen filings.

| Family | Event case | Control case | Observable target |
| --- | --- | --- | --- |
| ST transition | 600375 汉马科技, 2023Q3 | 002786 银宝山新, 2023Q3 | first new ST or *ST treatment by 2024-06-30 |
| Receivables / cash conversion | 300461 田中精机, 2019Q3 | 300455 康拓红外, 2019Q3 | incremental Q4 credit impairment greater than 20% of Q3 parent equity |
| Inventory | 300278 华昌达, 2019Q3 | 300442 普丽盛, 2019Q3 | FY inventory write-down greater than 10% of Q3 parent equity |
| Audit opinion | 000506 中润资源, 2023Q3 | the same issuer, 2022Q3 | qualified, adverse, or disclaimer opinion on the annual financial statements |
| Performance commitment | 300467 迅游科技, 2019Q3 | 300276 三丰智能, 2019Q3 | audited acquisition-target profit shortfall greater than 20% |
| Pledge / control | 002310 东方园林, 2018Q3 | the same issuer, 2017Q3 | controller change within about 12 months |
| Pledge / judicial freeze | 603766 隆鑫通用, 2018Q3 | the same issuer, 2017Q3 | newly frozen controller shares greater than 10% of its as-of holding within 12 months |

The receivables target is deliberately an **incremental** annual-minus-Q3
credit-impairment amount, preventing a model from being rewarded for predicting
an expense that was already public. The audit target excludes an unmodified
opinion merely because it contains an emphasis or material-uncertainty
paragraph. The pledge/control target records the later governance outcome and
does not encode a claim that pledge risk was its sole cause. The judicial-freeze
pair is an especially strict anti-shortcut control: both same-company slices
had roughly 98% of the controller's holding pledged at the latest as-of update,
but only the later slice crossed the predeclared freeze threshold. The agent
must reconcile report and announcement dates, repeated supplemental pledges,
entity boundaries, and counterevidence instead of treating a high ratio as a
deterministic rule.

Official signed reports are the outcome authority when the local read-only
RQData snapshot does not contain a populated family-specific announcement
table. RQData remains the source for PIT financial cross-checks and ST metadata;
the checked-in label preserves raw observations and recomputable derivations.

## Version 4 matched business-decision controls

Business-decision cases now contain an event and a non-event example for each
decision family. This prevents a policy such as “high R&D is always good” or
“announced capacity in a growing industry is always validated” from succeeding.
Every decision corpus contains both issuer disclosures and contemporaneous
news/industry evidence. News is point-in-time context, never the outcome label.

| Decision family | Event case | Control case | Predeclared joint outcome |
| --- | --- | --- | --- |
| Pre-listing R&D/product route | 688041 海光信息, 2022 | 688256 寒武纪, 2020 | at least 30% revenue CAGR, at least 50% gross margin, positive operating cash flow |
| Factory allocation | 300750 宁德时代湖西扩建, 2019 | 300769 德方纳米前驱体项目, 2021 | disclosed schedule milestone, at least 20% revenue CAGR, at least 10% gross margin, positive operating cash flow, at least 75% utilization |

The R&D pair uses company-specific baseline and outcome years but the same
economic thresholds. The factory pair uses an identical machine-readable
criterion contract. 宁德时代's 2022 annual report records the 湖西 project as
having reached its planned usable state and discloses realized project benefits.
德方纳米's September 2023 official inquiry response still classifies the named
20万吨 precursor project as a long-range plan without a construction timetable;
its FY2024 company-wide gross margin was also negative even though revenue,
operating cash flow, and reported utilization crossed their individual gates.

“Commercial validation” is intentionally narrower than “this investment caused
the outcome” and broader than stock return. It is also not a causal answer to
whether management's choice was counterfactually optimal. The benchmark asks
whether an agent could identify, from the frozen evidence, which announced
allocation was more likely to clear a fixed, auditable operating hurdle.

## PDF-to-text authoring

PDF extraction is standardized on the latest tested Rust-based
[`run-llama/liteparse`](https://github.com/run-llama/liteparse) revision:
version 2.11.1 at
`53e4fc813d35f76d0169923d2c451b3c8700edb0`. Text-layer filings use LiteParse's
PDFium path. Scanned audit and performance-commitment reports use its Tesseract
OCR path with `chi_sim` and `eng` data. Every new scenario records the exact
version, revision, and extraction mode in `authoring_provenance` so later
authors can reproduce the evidence preparation. Parser output never overrides
the signed filing or the numeric label derivation.

## Scoring

The agent returns an event probability, a thresholded decision, cited frozen
document IDs, and a short analysis summary. Per-case Brier loss is the primary
metric; log loss and classification accuracy are diagnostics. The current
public composite is 85% Brier score and 15% evidence-selection F1.

An actual leaderboard should aggregate Brier and log loss across many event
families and time periods, report calibration curves, preserve the full search
and tool trace, and keep final labels server-side. Further cases should add
abrupt earnings-guidance revisions, matched capital-allocation decisions, and
more live-shadow predictions whose outcomes were not knowable at seal time.

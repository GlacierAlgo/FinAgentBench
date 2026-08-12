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

## Version 5 ST, scandal, and market-path cohorts

Version 0.12 expands the real development set to 90 cases, balanced at 45 event
and 45 no-event. Seven new cohorts contain 66 cases; each cohort is balanced
independently so a generic “distressed” or “ST will recover” policy cannot win.

| Cohort | Cases | Balance | Observable target |
| --- | ---: | ---: | --- |
| Cash-payment reality | 2 | 1 / 1 | failure to complete at least RMB 50m of an already announced dividend on its fixed payment schedule |
| Public debt default | 4 | 2 / 2 | officially disclosed failure to pay at least RMB 50m of public debt within 120 calendar days |
| Final enforcement | 6 | 3 / 3 | final CSRC decision within 30 months confirming at least RMB 100m of misstatement, occupation, or illegal guarantee |
| Next annual audit | 12 | 6 / 6 | whether the strictly first annual financial-statement audit disclosed after the snapshot is nonstandard within 18 months |
| Full ST remediation | 12 | 6 / 6 | exchange-approved removal of every ST/*ST warning within 24 months |
| Forced delisting | 12 | 6 / 6 | final exchange decision to forcibly terminate listing within 60 months |
| Post-ST market path | 18 | 9 / 9 | at least 100% adjusted-close return and at least 80 percentage points of excess return versus 510300 within 365 days |

The ST cohorts deliberately separate four questions that are often collapsed
in casual reasoning: what caused the warning, whether the next audit remains
nonstandard, whether every warning is eventually removed, and what tradeable
price path occurs in a fixed window. A company can remediate yet fail the market
path, remain ST yet rally, or avoid forced delisting without receiving a clean
audit. Reusing the identical frozen corpus across those targets makes this
cross-target consistency directly testable.

### ST cause is a feature, not a label

`st_cause_taxonomy` distinguishes non-operating governance failures (fund
occupation, illegal guarantees, internal-control opinions), operating/financial
failures, mixed cases, court restructuring, and major-illegality/terminal risk.
The taxonomy guides matched analysis but never determines the outcome. In the
18-case market-path slice, non-operating governance cases contain both realized
run-ups (for example ST舍得、ST红太阳、ST华钰、ST德威) and controls (for example
ST华仪、ST康美、ST辅仁、ST加加、ST摩登、ST维维). Catastrophic operating or
major-illegality controls such as *ST凯迪、ST长生 and *ST雏鹰 prevent the suite
from teaching the opposite shortcut that every distressed company eventually
becomes a speculative winner.

The sample is curated and balanced, so its event proportions are not estimates
of A-share base rates. Its purpose is conditional reasoning: given an exact
snapshot, can the agent distinguish cash/debt survival, governance credibility,
resource or restructuring optionality, trading continuity, and already-priced
speculation without claiming any one factor caused the later path?

### Fixed-window market labels

The post-ST label uses the first trading day of the current warning episode, not
necessarily the first ST episode in the issuer's entire history. Stock closes
come from read-only backward-adjusted RQData prices; 510300 uses raw closes.
Observations are aligned by trade date, use closing prices only, and stop at the
fixed calendar endpoint. No price is synthesized across a suspension or after
delisting. This leaves *ST雏鹰 with only 113 aligned sessions, which is part of
the real tradeable path rather than missing data to be filled.

Both event gates must pass. ST加加 is the deliberate threshold control: its
maximum adjusted-close return was 100.74%, but the same-window maximum excess
return was 79.07 percentage points, below the 80-point gate. Risk-warning
removal is stored as a diagnostic only and cannot change the event label.

### Full replay diagnostics

The 2026-08-13 matrix contains 270 completed frozen-search runs with no failures:
90 cases each for GPT-5.6 Sol, Terra, and Luna at low reasoning effort. Overall
Brier loss was 0.1405, 0.1529, and 0.1729 respectively. The strict post-ST
market-path family remained difficult: Sol/Terra/Luna accuracy was
61.1%/66.7%/77.8%, and their mean probability on realized event cases was only
0.414/0.399/0.488. The next-annual-audit family was also hard
(58.3%/66.7%/58.3% accuracy), exposing a tendency to extrapolate a current
audit problem mechanically into the next annual report.

These numbers are public one-repeat diagnostics. They validate task difficulty
and expose failure modes; they do not qualify as a sealed leaderboard or model
stability claim.

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

All version 0.12 ST/scandal source PDFs selected for the checked-in corpora had
a usable text layer and were extracted with LiteParse `--no-ocr`. Source
validation checks the PDF container, issuer name, security code, publication
date, document title, and SHA-256. This caught and rejected both exchange
anti-bot HTML masquerading as a PDF response and an initially located quarterly
report belonging to a different issuer.

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

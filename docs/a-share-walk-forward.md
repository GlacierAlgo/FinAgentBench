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
announcement available by the as-of date. It exposes competing evidence:
product generations, customer certification and orders on one side; market
share, R&D capitalization, customer/related-party concentration, export-control
and supply-chain risks on the other. The later annual report and RQData PIT rows
remain label-only.

This rule is intentionally called **commercial validation**, not R&D causal
impact. Observational financial outcomes cannot establish that R&D was the sole
cause. For a Fabless designer such as 海光信息, the relevant allocation choices
are product generations, IP/licensing, tape-out and validation, and software
ecosystem investment—not factory construction.

## Scoring

The agent returns an event probability, a thresholded decision, cited frozen
document IDs, and a short analysis summary. Per-case Brier loss is the primary
metric; log loss and classification accuracy are diagnostics. The current
public composite is 85% Brier score and 15% evidence-selection F1.

An actual leaderboard should aggregate Brier and log loss across many event
families and time periods, report calibration curves, preserve the full search
and tool trace, and keep final labels server-side. The next A-share families
should include ST transitions, modified audit opinions, receivable/cash-flow
divergence, inventory write-downs, performance-commitment failures, pledges and
freezes, and abrupt earnings-guidance revisions.

# EVIDENCE - Arbitrary Finite-Prefix One-Use Charging

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | STRICT startup and task isolation | authoritative memory and Git | pass |
| EV-002 | exact theorem | Arbitrary finite-\(k\) one-use charging | `research/FIXED_ORDER_CYCLE_RATIO.md` | proved |
| EV-003 | exact computation | Six-prefix local-history oracle | `literal_oracle.py` | 332,640 pass |
| EV-004 | static / regression | Lint, tests, artifacts, and proof structure | commands / source | pass after corrections |
| EV-005 | audit / scope | Synchronization and final diff audit | source / Git | pass |

## EV-001 - Startup And Isolation

- **Date:** 2026-07-17
- **Method or command:** read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the relevant
  proof sections and prior dossier; run `git status --short --branch`,
  `git rev-parse HEAD`, and `git log -1 --oneline`.
- **Relevant output:** clean `main` tracking `origin/main` at
  `2897fa52af8e40808f3483647183b25e76eb04f9`.
- **Interpretation:** verified task isolation; the five-prefix theorem and
  local floor lemmas are the exact prior inputs.
- **Limitations:** startup inspection does not prove the generalization.
- **Linked log entry:** `TASK_LOG.md#2026-07-17---strict-startup-and-expected-delta`.

## EV-002 - Exact Arbitrary Finite-Prefix Theorem

- **Date:** 2026-07-17
- **Method or command:** direct symbolic derivation from CR28ax--CR28bd and
  the literal-history invariant, recorded in CR28dr--CR28dw.
- **Relevant output:** for any finite \(k\ge1\), the \(k+1\) convex
  coefficients telescope to \(k\) disjoint segments; selected base splits
  inject into original edges; the canonical charged/unused partition uses
  every original slack exactly once; descending insertion induction contains
  no frontier count. Therefore
  \[
  \gamma^{(r)}_{1,n}\ge
  P_{r,n}+\sum_{i=1}^k(s_{i-1}-s_i)G_{n,\lambda_i}(s_i).
  \]
- **Interpretation:** exact finite method-specific theorem for every finite
  admissible \(k\).
- **Limitations:** no uniform growing-\(k\) estimates, coefficient
  optimization, rounding, limiting-prefix passage, or geometric claim.
- **Linked log entry:** `TASK_LOG.md#2026-07-17---exact-arbitrary-finite-prefix-derivation`.

## EV-003 - Bounded Exact Six-Prefix Oracle

- **Date:** 2026-07-17
- **Method or command:**
  `python -B ops\TASK-20260717__arbitrary_finite_prefix_charging\literal_oracle.py`.
- **Relevant output:** 332,640 histories; base splits
  \((6,30,180,1260,10080,90720)\); recursive splits
  \((0,12,156,1764,20160,241920)\); inserted-pair splits
  \((0,0,12,252,4032,60480)\); used-base histogram
  \(\{1:4320,2:54000,3:144000,4:108000,5:21600,6:720\}\). The local floors
  sum to \(1973481/5720\), and the checked bound is \(12383881/5720\).
- **Interpretation:** verified bounded exact computation. It exercises six
  simultaneous original-edge charges and deeply nested sixth splits.
- **Limitations:** finite corroboration, not the arbitrary-\(k\) proof; no
  project, production, or test helper is imported.
- **Linked log entry:** `TASK_LOG.md#2026-07-17---standalone-exact-six-prefix-oracle`.

## EV-004 - Static, Structural, And Repository Regression

- **Date:** 2026-07-17
- **Method or command:** Ruff check/format; focused and full pytest; checked
  artifact verifier; schema regression; exact counts of equation tags,
  standalone display delimiters, `aligned`, and `array` environments;
  UTF-8/BOM/newline inspection.
- **Relevant output:** Ruff passes; the focused cycle-ratio module and all 283
  local tests pass; the verifier reports 4 certificates and 76 local
  brackets; 4 schema tests pass. The proof note has 321 unique equation tags,
  576 balanced standalone display pairs, 34 balanced `aligned` pairs,
  and 7 balanced `array` pairs. All ten changed/new files are UTF-8
  without BOM, LF-only, and LF-terminated.
- **Corrected failed checks:** the first Ruff format check returned
  `Would reformat`; the formatter was applied and both lint and format
  reruns pass. The first anti-refuso regex matched the root `quad` in
  words such as `quadratic`; a second still matched `\qquad`.
  Restricting the check to a standalone bare `quad(` token gives zero.
- **Interpretation:** repository regressions, artifact semantics, source
  structure, formatting, and encoding pass. The failed checks were diagnostic
  defects, not mathematical or source failures.
- **Limitations:** hosted GitHub Actions were not inspected; static and
  regression checks do not replace the written proof.
- **Linked log entry:** `TASK_LOG.md#2026-07-17---synchronization-and-regression`.

## EV-005 - Independent Audits And Final Scope

- **Date:** 2026-07-17
- **Method or command:** independent read-only proof, synchronization, and
  oracle audits; stale-claim search; complete tracked and untracked diff
  inspection; `git status --short` and `git diff --check`.
- **Relevant output:** proof quantifiers, selected-height indexing, convex
  telescope, canonical partition, recursive induction, local floors,
  \(k=1,5\) specializations, and non-uniformity caveat all pass. Requested
  summaries agree, the six-prefix open question is removed, and no coefficient
  or geometric claim was added. The sole executable is the dossier-local
  \(k=6\) oracle; no production path or enumeration limit changed.
- **Interpretation:** mathematical, computational, synchronization, scope,
  formatting, and final-diff audits pass.
- **Limitations:** manual user review and commit decision remain.
- **Linked log entry:** `TASK_LOG.md#2026-07-17---independent-audits-and-handoff`.

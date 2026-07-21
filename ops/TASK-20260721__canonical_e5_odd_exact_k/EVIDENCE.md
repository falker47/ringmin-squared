# EVIDENCE - TASK-20260721 / Canonical Odd-v E5 Exact K

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git / definition | Startup, clean scope, accepted PGE5ODD base | repository sources | VERIFIED |
| EV-002 | exact theorem | Support, argmax, score, K825, fixed-order closure | fixed-order proof | PROVED |
| EV-003 | bounded exact computation | Sole max-plus/all-arcs diagnostic | `exact_diagnostic.py` | PASS |
| EV-004 | verification / review | Static, repository, source, scope, diff hygiene | repository commands | PASS |

## EV-001 - Startup Scope And Provenance

- **Date:** 2026-07-21
- **Method or command:** read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`,
  (PGE5ODD-1)--(PGE5ODD-26), the accepted PGE5ODD dossier,
  (K825-1)--(K825-9), CR12p/CR22/CR27/CR28a, and the analogous exact-\(K\)
  precedents; inspect `git status --short --branch` and recent history.
- **Relevant output:** clean `main...origin/main` at commit `7abd3d6`, whose
  accepted theorem supplies exactly the required odd-\(v\) support base.
- **Interpretation:** verified provenance and bounded scope, not a new
  \(K\)-theorem.
- **Limitations:** no score or argmax claim followed at this checkpoint.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---strict-startup-and-scope`

## EV-002 - Exact Symbolic Theorem

- **Date:** 2026-07-21
- **Method:** literal image partition and PGE5ODD support check; exact cyclic
  expansion; isolated-hole identity (K825-6)--(K825-9); seven exhaustive
  gain classes; every endpoint, two-edge role, three-edge, longer, and cyclic
  shortcut class; separate finite \(m=1\) proof; exact block summation;
  K825 specialization and subtraction; CR12p/CR22/CR27/CR28a audit.
- **Relevant output:** (KRPGE5ODD-1)--(KRPGE5ODD-40) prove support and
  \(W=W_n\), the complete induced-subset argmax, \(K_1=2175\), the requested
  formula for all \(m\ge2\), coefficient \(857/3000\), strict all-row K825
  comparison, and only the legitimate fixed-order/global consequences.
- **Boundary evidence:** the singleton range is empty at \(m=1\), there is no
  doubleton, the stable tail has score \(2164\) at \(m=1\), deleting \(7\)
  gains \(11\), the sharp shortcut minimum is \(8\) at \(m=1\), \(9\) at
  \(m=2\), and \(4m+4\) from \(m\ge3\); K825 has its independent
  \(-13\) symbolic-boundary correction.
- **Interpretation:** **exact fixed-core theorem** for every \(m\ge1\).
- **Limitations:** it optimizes no other supported map and proves no global
  minimizer, matching global lower bound, all-\(n\) limsup, convergence, or
  exact geometric leading constant.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---exact-all-domain-derivation`

## EV-003 - Sole Bounded Independent Diagnostic

- **Date:** 2026-07-21
- **Command:**
  `python -B ops/TASK-20260721__canonical_e5_odd_exact_k/exact_diagnostic.py`
- **Declared limits:** max-plus, every proper oriented arc, every hole gain,
  and label-one elimination check for \(m=1,\ldots,30\); exact support,
  formula, residue, boundary, K825, and coefficient checks through
  \(m=1000\).
- **Relevant output:** PASS through 39,970,045 max-plus transitions, 1,891
  isolated-hole gains, 1,016,930 proper oriented arcs, 1,010,149 nontrivial
  compressed shortcuts, 4,890 label-one insertion gaps, 508,465 neighbor-pair
  inequalities, 5,013,000 literal core entries, and 1,002,000 assigned
  support incidences.
- **Independent mechanism:** the script imports only the standard library,
  constructs only the prescribed map, supplies no candidate to the max-plus
  DP, and separately checks the exact raw-arc plus internal-hole-budget
  identity on every proper oriented arc. It enumerates no assignment, matching,
  subset, permanent, or alternative order family.
- **Interpretation:** **bounded exact computation** corroborating EV-002.
- **Limitations:** finite rows do not prove the all-domain theorem; the script
  intentionally performs no floating approximation of \(\pi\) and does not
  verify the real-arithmetic angular sandwich.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---sole-independent-diagnostic`

## EV-004 - Final Verification And Handoff

- **Date:** 2026-07-21
- **Environment:** Python 3.14.3; pytest 9.0.2; Ruff 0.11.12.
- **Methods or commands:** standalone diagnostic; `python -m ruff check` and
  `python -m ruff format --check` on the sole script;
  `python -m pytest -p no:cacheprovider`; focused schema and Arb pytest;
  checked-artifact verification with `PYTHONPATH=src`; exact KRPGE5ODD
  tag/display/environment/control-character audit; cross-file link/reference
  and authorized-path audits; three independent read-only reviews; read-only
  Git status/stat/diff inspection; `git diff --check`.
- **Relevant output:** diagnostic PASS with the EV-003 counts; Ruff PASS;
  283 tests passed in 67.02 seconds; 4 focused schema tests and 3 focused Arb
  tests passed; checked-artifact verifier confirmed four certificates, 76
  local brackets, and summary rows \(n=3,4,5,6\); source audit found exactly
  40 sequential unique KRPGE5ODD tags, 56 balanced display pairs, 10 balanced
  environments, and no control characters; scope and final diff hygiene PASS.
- **Independent review:** separate read-only audits rederived the symbolic
  proof, checked every diagnostic counter and coverage invariant, and audited
  the CR12p/CR22/CR27/CR28a implication boundary plus cross-file roles. All
  three returned PASS after corrections.
- **Corrected-check evidence:** the first Ruff format check reported that the
  new script would be reformatted; the formatter was applied to that file and
  both Ruff checks plus the full diagnostic then passed. Independent proof
  reviews found two missing backslashes before `qquad`; both TeX typos were
  corrected and the complete source audit and reviews then passed. No
  mathematical formula, test, schema, artifact, or production check failed.
- **Scope result:** modified tracked files are exactly `CURRENT_STATUS.md`,
  `PROJECT_KNOWLEDGE.md`, `research/FIXED_ORDER_CYCLE_RATIO.md`, and
  `research/NEXT_RESEARCH_STEPS.md`; the only untracked paths are the four
  files in this dossier. Production, public tests, schemas, artifacts,
  workflows, prior dossiers, and the PGE5ODD support proof are unchanged.
- **Interpretation:** the theorem, diagnostic, synchronization, and repository
  checks pass; the task is `READY_FOR_REVIEW`.
- **Limitations:** verification is local rather than hosted; bounded exact
  computation remains corroboration, while all-domain validity comes from
  EV-002. The user must review and decide whether to commit.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---final-verification-and-handoff`

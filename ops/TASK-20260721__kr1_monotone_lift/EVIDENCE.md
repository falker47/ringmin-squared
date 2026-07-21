# EVIDENCE - TASK-20260721 / KR1 Monotone All-Index Lift

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | Startup, source, and scope audit | repository sources and Git | PASS |
| EV-002 | exact theorem | Label cancellation and KR1 all-index lift | `research/FIXED_ORDER_CYCLE_RATIO.md` | PASS |
| EV-003 | bounded exact computation | Residue coverage and KR1 formulas | `exact_diagnostic.py` | PASS |
| EV-004 | tests / checks / review | Repository verification and final diff audit | commands and Git diff | PASS |

## EV-001 - Startup, Source, And Scope Audit

- **Date:** 2026-07-21
- **Method or command:** read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, the relevant KR1
  proof and prior dossier, and the production order/scorer definitions; ran
  `git status --short --branch`; commissioned three independent read-only
  audits.
- **Relevant output:** clean `main...origin/main`; no uncommitted files.
  Independent audits agreed on the proof, source corrections, diagnostic
  design, and exact initial domain.
- **Interpretation:** safe STRICT startup. Historical dossiers remain
  unchanged; the new result belongs in this dossier and the authoritative
  current sources.
- **Limitations:** source and scope audit only.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---strict-startup-and-source-audit`.

## EV-002 - Exact Cancellation Lift

- **Date:** 2026-07-21
- **Method or command:** exact proof from the induced-subset identity (CR12h),
  KR1 formulas (KR1-3)--(KR1-4), fixed-order elimination (KR1-29), and the
  strict global sandwich (CR27), independently rederived and audited.
- **Relevant output:** for every \(3\le n\le N\), cancelling labels above
  \(n\) preserves all retained subset scores and proves
  \(\Lambda_n\le\Lambda_N\). For
  \(N(n)=5\lceil(n-1)/5\rceil+1\), every \(n\ge7\) satisfies
  \(0\le N(n)-n\le4\) and
  \[
  \Lambda_n\le K_{\rm R1}(N(n)),\qquad
  R_2^*(n)<{K_{\rm R1}(N(n))\over\pi}.
  \]
  Hence the all-index limsup coefficients are at most \(857/3000\) and
  \(857/(3000\pi)\).
- **Interpretation:** this is an **exact theorem**, not finite extrapolation.
  It uses restriction of the existing KR1 order only.
- **Limitations:** no equality, lower-bound transfer, optimality,
  minimizing-order classification, normalized monotonicity, convergence, or
  exact leading constant follows. The formula at \(k=1\) is outside the
  proved KR1 domain and is not used.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---exact-cancellation-lift-and-source-synchronization`.

## EV-003 - Bounded Exact-Integer Diagnostic

- **Date:** 2026-07-21
- **Method or command:**
  `python -B ops/TASK-20260721__kr1_monotone_lift/exact_diagnostic.py`;
  `python -m ruff check
  ops/TASK-20260721__kr1_monotone_lift/exact_diagnostic.py`;
  `python -m ruff format --check
  ops/TASK-20260721__kr1_monotone_lift/exact_diagnostic.py`.
- **Relevant output:** PASS on 1,000 consecutive rows \(7\le n\le1006\);
  ten residue classes times 100; offsets \(0,1,2,3,4\) each 200 times;
  KR1 branches \(N\equiv1,6\pmod {10}\) each 500 times; 200 distinct
  lifted rows; 970 third finite differences all equal to \(1714\); exact
  coefficient \(857/3000\). Ruff check and final format check pass.
- **Interpretation:** this is a **bounded exact computation** using only
  integers and `Fraction`. It checks both KR1 formula forms, exact
  divisibility, the first licensed boundary rows, all residue offsets, and
  the common cubic coefficient. It constructs no order or finite-prefix
  object.
- **Failed-check record:** the first Ruff format check reported that the new
  script would be reformatted. `python -m ruff format` was applied; the final
  Ruff check and format check both pass.
- **Limitations:** bounded computation; it corroborates only arithmetic and
  does not replace EV-002.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---bounded-exact-integer-diagnostic`.

## EV-004 - Repository Verification And Final Audit

- **Date:** 2026-07-21
- **Method or command:** `python -m pytest -p no:cacheprovider`;
  `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`;
  `python -m pytest -p no:cacheprovider
  tests/test_checked_artifact_schema_validation.py`; EV-003 commands;
  exact in-file equation-tag uniqueness and KR1/UC24 coverage check; local
  Markdown-target check; authoritative stale-claim scan; independent
  proof/source/diagnostic reviews; `git status --short --branch`, complete
  tracked and untracked diff inspection, and `git diff --check`.
- **Relevant output:** pytest `283 passed in 65.86s`; checked artifacts
  `certificates=4 local_brackets=76` with summary values `3,4,5,6`; focused
  schema tests `4 passed in 0.98s`; 1,449 in-file-unique research equation
  tag occurrences, including all 40 KR1 tags and the complete
  `UC24`--`UC24g` sequence; 21 local Markdown targets exist; authoritative
  stale-claim scan has no false current-best or KR1 non-globalization hit;
  final diff check has no output.
- **Interpretation:** all relevant regression, artifact, structural,
  arithmetic, source-synchronization, and repository-hygiene checks pass.
  Final scope is six tracked authoritative/status Markdown files plus the
  four-file dossier. No production, public test, schema, artifact, order
  family, or finite-prefix extension changed.
- **Failed-check record:** an initial equation-tag checker incorrectly
  required numeric tags to be unique across separate research documents;
  existing document-local numeric tags `1`--`19` correctly recur. The fixed
  checker tests uniqueness within each file and passes. The Git commands
  also emit only the environment warning that the user-level Git ignore file
  is unreadable; repository status and diff checks still complete normally.
- **Limitations:** local verification does not establish hosted CI status.
  The exact all-index conclusion depends on EV-002, not on finite tests.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---repository-verification-and-ready-for-review`.

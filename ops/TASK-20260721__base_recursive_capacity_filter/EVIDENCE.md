# EVIDENCE - TASK-20260721 / Base-Recursive Capacity Filter

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source audit | Scope and source disambiguation | roadmap, proof, Git history | VERIFIED |
| EV-002 | exact theorem | Finite base-capacity inequality | CR28dw40--CR28dw41 | PROVED |
| EV-003 | exact optimization | Compact normalized no-go | CR28dw42--CR28dw49 | PROVED |
| EV-004 | bounded exact computation | Independent literal and normalized diagnostic | `exact_diagnostic.py` | PASS |
| EV-005 | regression / hygiene | Repository verification and final diff | repository root | VERIFIED |

## EV-001 - Scope And Source Audit

- **Date:** 2026-07-21
- **Method or command:** inspected `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, the roadmap, CR28dw, KPGZERO-23--KPGZERO-24, the
  prior two-block dossier, read-only Git history, and clean Git status; used
  three independent read-only derivation/context reviews.
- **Relevant output:** the roadmap phrase "filtered cubic-convergent" was
  inherited from the PG49/KPGZERO problem, where cubic means an algebraic
  cubic root.  The user's explicit CR28dw and \(C_{\mathrm{AF}}\) criteria
  instead select a base-capacity refinement.  The prior two-block theorem is
  already complete and is not duplicated.
- **Interpretation:** the bounded class is declared explicitly: one selected
  prefix, base/recursive type, and original-edge capacity only.
- **Limitations:** no claim is made that this is the unique possible
  structural filter beyond the declared class.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---strict-startup-and-scope-resolution`.

## EV-002 - Exact Finite Capacity Filter

- **Date:** 2026-07-21
- **Method or command:** exact edge-count injection plus
  CR28ax--CR28bf, without numerical computation.
- **Relevant output:** a base cycle has \(q=n-r+1\) edges, so at least
  \([2r-s-n-1]_+\) selected splits are recursive.  Their stronger floor gives
  \[
  \gamma^{(r)}_{1,n}
  \ge P_{r,n}+(r-s)G_{n,\lambda}(s)
  +[2r-s-n-1]_+(J_{n,\lambda}(s)-G_{n,\lambda}(s)).
  \]
- **Interpretation:** exact all-order theorem; pointwise strict improvement
  over one-prefix CR28dw when the filter is active and \(\lambda>0\).
- **Limitations:** it is a lower-bound method, not an upper bound or exact
  evaluation of \(\Lambda_n\).
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---finite-capacity-theorem`.

## EV-003 - Exact Compact No-Go

- **Date:** 2026-07-21
- **Method or command:** exact normalization, positive-part side split,
  inherited complete one-prefix compact classification, active-side
  inequalities, derivative signs, and rational radical separators.
- **Relevant output:** the active-side compact closure has unique maximum
  \(13/48\) at its filter-off hinge.  The full compact domain has unique
  maximum
  \[
  C_{1,*}={4+2\sqrt3\over27}
  <{434+4\sqrt2\over1587}=C_{\mathrm{AF}}
  \]
  at the old inactive one-prefix optimizer.  All density/weight endpoints,
  \(\beta=\alpha\), \(\beta=0\), \(\lambda=0,1\), \(\alpha=0,1\), and the
  hinge \(\beta=2\alpha-1\) are included.
- **Interpretation:** exact method-specific no-go for this binary capacity
  filter; improvements with \(2\alpha-\beta-1>0\) and \(\lambda>0\) cannot
  move the compact optimum.
- **Limitations:** broader multi-prefix or structural filters are not
  classified.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---compact-optimization-and-no-go`.

## EV-004 - Independent Exact Diagnostic

- **Date:** 2026-07-21
- **Method or command:**
  `python -B ops/TASK-20260721__base_recursive_capacity_filter/exact_diagnostic.py`.
- **Relevant output:** PASS; 3,300 exhaustive selected-prefix histories
  across a capacity-saturated control, the first active row, a positive-floor
  active row, and a row with two forced recursive splits.  Every history
  checks linkage, contraction, score corrections, the base/recursive
  invariant, one-use slack, local floors, capacity, and the filtered
  inequality.  A denominator-24 grid checks 8,125 exact compact-domain
  points and both sides of the hinge.  Exact radical arithmetic verifies
  \(13/48<C_{1,*}<C_{\mathrm{AF}}\).
- **Interpretation:** bounded independent corroboration with no project,
  production, test, enumerator, or artifact imports.
- **Limitations:** finite selected-prefix histories and rational grids do not
  replace the written all-history and all-real proofs.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---independent-diagnostic-and-synchronization`.

## EV-005 - Repository Verification And Final Diff

- **Date:** 2026-07-21
- **Method or command:** reran the standalone diagnostic and Ruff lint/format
  checks; ran `python -m pytest -p no:cacheprovider`, the focused checked-
  artifact schema test, and
  `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`;
  audited equation tags, display delimiters, control characters, protected
  paths, task-local generated caches, `git status`, the complete diff, and
  `git diff --check`.
- **Relevant output:** diagnostic PASS on 3,300 selected-prefix histories and
  8,125 grid points; Ruff PASS; full suite `283 passed`; schema suite
  `4 passed`; checked-artifact verifier PASS for 4 certificates and 76 local
  brackets; 914 equation tags are unique and CR28dw40--CR28dw49 are present;
  source, scope, task-local generated-file, diff-review, and whitespace audits
  PASS.
- **Interpretation:** the exact proof, independent diagnostic, and repository
  integration are ready for human review.  No enumerator, production source,
  schema, test module, checked artifact, or geometric artifact changed.
- **Limitations:** hosted CI cannot inspect an uncommitted diff.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---final-verification-and-handoff`.

# EVIDENCE - TASK-20260723 / PG49 KPGZERO Filtered Cardinality

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / exact reduction | Startup and exact filtered problem | authoritative research notes | VERIFIED |
| EV-002 | exact theorem | Filtered cardinality and support-only no-go | fixed-order proof | PROVED |
| EV-003 | bounded exact computation | Independent discriminating diagnostic | `exact_diagnostic.py` | VERIFIED |
| EV-004 | regression / hygiene | Repository verification and final diff audit | repository root | VERIFIED |

## EV-001 - Startup And Exact Problem

- **Date:** 2026-07-23
- **Method or command:** clean `git status`; read `AGENTS.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`,
  `research/NEXT_RESEARCH_STEPS.md`, PG37--PG49, PG61--PG63,
  PG100--PG114, KPGMIN, KPGZERO-1--KPGZERO-30, KPGSTAR, and the predecessor
  task dossier.
- **Relevant output:** KPGZERO-23 bijects zero holes with convergent/scale
  pairs passing congruence, domain, side, and scale filters. PG104 and PG49
  already support the descending-min bijection for every \(m\).
- **Interpretation:** the requested cardinality concerns induced \(K\) on a
  fixed supported family; it is not a support-edge count, the Ferrers
  permanent, or a geometric quantity.
- **Limitations:** source inspection alone does not choose finite versus
  infinite.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---strict-startup-and-exact-scope`.

## EV-002 - Filtered Cardinality And No-Go

- **Date:** 2026-07-23
- **Method or command:** primitive uniqueness and fibre counting from
  KPGZERO-2--KPGZERO-23; finite positive-leading quadratic scale windows;
  exact substitution at the left witness; PG49/KPGSTAR same-board
  comparison; symbolic substitution
  \((\delta,u,w,g)=(1,13,9,20t+1)\).
- **Relevant output:** the per-row filtered fibre has cardinality
  \(|\mathcal Z_m|\), so the descending-min argmax count is its power of two.
  An infinite filtered family requires infinitely many distinct convergents.
  At the same giant-\(m\) PG49 board, descending-min has a zero and at least
  two induced-\(K\) maximizers, whereas PG49-star has one. The affine
  support-only ray has a right local zero for every \(t\ge0\), but its two
  ceiling residuals are
  \(-757536t^2-64548t-1335\) and
  \(-757536t^2-69992t-1606\), so no member is KPGZERO-filtered.
- **Interpretation:** exact no-go for support-only inference and for
  fixed-direction rescaling. PG49 compatibility and common \(W=W_n\)
  neither force nor forbid induced-\(K\) maximizer degeneracy for a
  supported bijection.
- **Limitations:** this does not prove the absolute filtered set finite.
  KPGZERO-24 remains the exact arithmetic obstruction.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---support-only-and-fixed-direction-no-go`.

## EV-003 - Independent Exact Diagnostic

- **Date:** 2026-07-23
- **Method or command:**
  `python ops/TASK-20260723__pg49_kpgzero_filtered_cardinality/exact_diagnostic.py`;
  `python -m ruff check
  ops/TASK-20260723__pg49_kpgzero_filtered_cardinality/exact_diagnostic.py`.
- **Relevant output:** `PG49/KPGZERO filtered-cardinality diagnostic: PASS`;
  two PG49 interval-shift witnesses, one on the literal equality boundary;
  one direct all-pairs \(W\) row; affine-ray rows \(t=0,1,17\); three
  accepted filtered branch/sign cases; two rejected congruent scales; the
  same-board discriminator; zero matching, subset, or permutation-family
  enumerations. Ruff reports `All checks passed!`.
- **Interpretation:** exact discriminating instances independently separate
  PG49 support, the literal KPGZERO filter, and supported-bijection
  induced-\(K\) maximizer cardinality.
- **Limitations:** finite discriminating instances corroborate but do not
  replace the symbolic theorem or decide KPGZERO-24.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---independent-exact-diagnostic`.

## EV-004 - Regression And Hygiene

- **Date:** 2026-07-23
- **Method or command:** `python -m pytest`;
  `python -m pytest tests\test_finite_results.py::test_deterministic_generation -vv`;
  `python -m pytest tests\test_checked_artifact_schema_validation.py`;
  `$env:PYTHONPATH='src'; python -m
  power_ringmin.verify_checked_artifacts`; `git status --short`;
  `git diff`; `git diff --check`.
- **Relevant output:** an initial concurrent full-suite run reported 282
  passes and one deterministic-generation mismatch because a concurrent
  best-effort Git subprocess returned `git_commit=null`; the isolated test
  then passed, direct provenance detection returned the exact baseline SHA,
  and the sequential full suite passed all 283 tests. The schema test passed
  all four cases. The verifier accepted four certificates, 76 local
  brackets, and the \(n=3,4,5,6\) summary. Final status contains only the
  intended documentation and dossier changes; `git diff --check` is clean.
- **Interpretation:** the final repository state passes all regression,
  artifact, static, and diff-hygiene checks. The transient concurrent
  provenance read did not reproduce sequentially and required no source or
  artifact change.
- **Limitations:** repository tests validate existing software/artifact
  contracts; the new all-parameter claims rest on the symbolic proof, with
  the diagnostic as finite corroboration.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---verification-and-ready-for-review`.

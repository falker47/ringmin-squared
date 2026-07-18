# EVIDENCE - Global Finite-Prefix Envelope

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / exact derivation | Startup and clipped reduction | CR28bw / CR28cr / CR28dr | pass |
| EV-002 | exact theorem | Global finite-prefix classification | CR28dw13--CR28dw29 | proved |
| EV-003 | exact computation | Independent clipped-envelope diagnostic | exact_diagnostic.py | pass |
| EV-004 | source | Authoritative synchronization | pertinent Markdown | pass |
| EV-005 | regression / audit | Proportional verification and final diff | commands / Git | pass |

## EV-001 - Startup And Exact Reduction

- **Date:** 2026-07-18
- **Method or command:** read AGENTS.md, start.md, PROJECT_KNOWLEDGE.md,
  CURRENT_STATUS.md, the relevant primary proof sections and task dossiers;
  inspect Git status and HEAD.
- **Relevant output:** clean main at
  807d79eca25249b404ce9b3374472e19c67e5adf. Coordinatewise clipping gives
  the exact arbitrary-\(k\) compact reduction and Bellman recurrence.
- **Interpretation:** the task started isolated and requires proof/status
  documentation plus at most one dossier-local diagnostic.
- **Limitations:** source inspection alone does not prove global optimality.
- **Linked log entry:** TASK_LOG.md#2026-07-18---strict-startup-and-full-clipped-reduction.

## EV-002 - Exact Global Envelope Theorem

- **Date:** 2026-07-18
- **Method or command:** exact Darboux-sum domination, piecewise integration,
  outer-region comparison, normalized-simplex equality, and one-variable
  strict-concavity analysis.
- **Relevant output:** for every finite \(k\), the compact template has a
  unique strict all-middle maximizer with density \(\alpha_{k,*}\), and
  \[
  C_{k,*}\nearrow
  {434+4\sqrt2\over1587}=C_{\mathrm{AF}}.
  \]
  The full finite-prefix family has exactly this unattained supremum.
- **Interpretation:** exact method-specific theorem; no counterexample
  exists.
- **Limitations:** this classifies the continuous coefficient family. It
  gives no uniform finite rounding, growing-\(k\) charging theorem,
  convergence, or exact geometric leading constant.
- **Linked log entry:** TASK_LOG.md#2026-07-18---exact-global-classification.

## EV-003 - Standalone Exact Diagnostic

- **Date:** 2026-07-18
- **Method or command:**
  `python -B ops\TASK-20260718__global_finite_prefix_envelope\exact_diagnostic.py`;
  `python -m ruff check` and `python -m ruff format --check` on that file.
- **Relevant output:** `PASS: exact global finite-prefix clipped-envelope
  diagnostic`, `bellman_states=300`, and `fixed_k_rows=12`; both final Ruff
  checks pass. The script independently reconstructs clipping, \(\phi\), its
  antiderivative, the discrete Bellman recurrence, normalized rows, critical
  brackets, and exact quadratic-surd comparisons.
- **Corrected failures:** three preliminary runs failed because of
  diagnostic-only assertion defects: two singleton \(k=1\) checks treated the
  first and last tuple entries as distinct, and one adjacent-slice
  `zip(strict=True)` required unequal slices to have equal length. The first
  Ruff format check also requested mechanical formatting. All were corrected;
  no theorem or production defect was involved.
- **Interpretation:** verified bounded exact computation, independent of
  project source and test helpers.
- **Limitations:** the rational grids and first 12 rows corroborate but do not
  prove the arbitrary-\(k\), all-real theorem.
- **Linked log entry:** TASK_LOG.md#2026-07-18---exact-diagnostic-and-authoritative-synchronization.

## EV-004 - Authoritative Synchronization

- **Date:** 2026-07-18
- **Method or command:** edit and read back the primary proof,
  `research/ALL_N_LOWER_BOUND.md`, `start.md`, `PROJECT_KNOWLEDGE.md`,
  `research/NEXT_RESEARCH_STEPS.md`, `CURRENT_STATUS.md`, and this dossier;
  run targeted repository-wide `rg` audits.
- **Relevant output:** every pertinent current source records the compact
  clipped Bellman envelope, unique finite-\(k\) strict all-middle optimizer,
  exact unattained supremum \(C_{\mathrm{AF}}\), and the distinction from the
  loose formal endpoint \(E_\infty(1)=1/3\).
- **Interpretation:** authoritative state is consistent and preserves the
  existing lower coefficient while upgrading its method-specific optimality
  classification.
- **Limitations:** historical append-only dossiers are not rewritten.
- **Linked log entry:** TASK_LOG.md#2026-07-18---exact-diagnostic-and-authoritative-synchronization.

## EV-005 - Repository Verification And Final Diff

- **Date:** 2026-07-18
- **Method or command:** rerun the three pertinent historical exact
  diagnostics; `python -m pytest`; checked-artifact verifier; focused schema
  pytest; strict UTF-8/LF/final-newline/trailing-whitespace,
  display/fence/environment, and equation-tag checks; three independent
  read-only audits; `git status --short --untracked-files=all`, complete diff
  inspection, and `git diff --check`.
- **Relevant output:** historical diagnostics PASS with 203,489 normalized
  grid states, 332,640 charging histories, and all 21 five-prefix regimes;
  full pytest PASS 283; four certificates and 76 brackets PASS; schema PASS 4;
  source structure PASS over 10 intended paths with 395 unique primary tags;
  final scope and diff hygiene PASS.
- **Corrected audit findings:** independent reviewers identified a false
  uniqueness implication at the harmless endpoint \(\alpha=1/3\), ambiguous
  formal-versus-clipped wording, an inaccurate fixed-density label, and an
  overbroad diagnostic description. Each was corrected and rechecked.
- **Interpretation:** the exact theorem, synchronization, independent bounded
  corroboration, and requested protected-path scope are READY_FOR_REVIEW.
- **Limitations:** hosted CI is outside local verification; the user reviews
  and commits manually.
- **Linked log entry:** TASK_LOG.md#2026-07-18---regressions-audits-and-handoff.

# EVIDENCE - TASK-20260715__optimize_linear_block_certificate / Optimize Linear-Block Certificate

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | Git / test / exact derivation | Clean startup, focused baseline, and three independent audits | repository and CR28ax--CR28bg | PASS |
| EV-002 | Exact proof | Parameter regions, local floors, charging, finite bounds, and symbolic maximin | `research/FIXED_ORDER_CYCLE_RATIO.md` | PASS |
| EV-003 | Independent bounded diagnostics | Exact local histories, optimizer identities, and finite scan | `tests/test_fixed_order_cycle_ratio.py` | PASS |
| EV-004 | Verification / scope / review | Full tests, artifact checks, lint, reviews, and final diff audits | repository | PASS |

## EV-001 - Startup And Independent Derivation

- **Date:** 2026-07-15
- **Method or command:** Read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the prior task dossier, the
  authoritative proof and tests; inspected `git status`; ran
  `python -m pytest tests/test_fixed_order_cycle_ratio.py -q`; commissioned
  three independent read-only derivations covering symbolic maximin algebra,
  literal linkage/local floors, and bounded diagnostic design.
- **Relevant output:** startup tree clean on `main` at `f0ad789`; focused
  baseline 57 passed. All audits independently obtained

  \[
  \beta_*={3\sqrt2\over4}-{2\over3},\qquad
  \lambda_*={88-48\sqrt2\over49},\qquad
  c_*={99\sqrt2-140\over27}.
  \]

  They also recovered the exact finite recursive/base floor dominance and the
  strict coefficient improvement over the old specialization.
- **Interpretation:** the task starts from a clean verified baseline, and the
  candidate proof has independent exact agreement before editing.
- **Limitations:** read-only derivation and baseline tests do not verify the
  forthcoming documentation or test changes.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---startup-and-exact-read-only-audits`.

## EV-002 - Exact Proof And Symbolic Maximin

- **Date:** 2026-07-15
- **Method or command:** Exact hand derivation, followed by independent
  symbolic audits of the generalized CR28 block and its resultants.
- **Relevant output:** The proof establishes the full region
  \(0<\beta<\sqrt2-1\), \(0\le\lambda\le1\), the exact fixed-\(n\) cutoff
  condition, the smaller positive-cubic region, and the literal floors
  \[
  G_{n,\lambda}(t)=
  {\lambda(4(n+r_n)t-(n+r_n)^2-2\lambda t^2)\over2(2-\lambda)},
  \qquad
  J_{n,\lambda}(t)=
  \lambda\bigl((n+r_n-1)t-n(r_n-1)\bigr).
  \]
  The exact identity
  \[
  J-G={\lambda\bigl((n-r_n)^2+4(n-t)
  +2\lambda(r_n-1-t)(n-t)\bigr)\over2(2-\lambda)}
  \]
  proves base-floor dominance on the recursive range. The stationary
  equations and their factored resultants isolate
  \(\beta_*=(9\sqrt2-8)/12\) and
  \(\lambda_*=(88-48\sqrt2)/49\) as the unique global maximizer, with
  \(c_*=(99\sqrt2-140)/27\). Exact integer comparisons prove the strict gain
  over the old coefficient and the finite thresholds \(n\ge99\) and
  \(n\ge572\).
- **Interpretation:** This is an exact theorem about the admissible
  parameterized proof template and its certified lower coefficient.
- **Limitations:** It is not an exact formula for the residual, an exact
  geometric leading coefficient, a geometric limit, or a convergence proof.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---exact-parameterized-certificate-and-maximin`.

## EV-003 - Bounded Independent Diagnostics

- **Date:** 2026-07-15
- **Method or command:**
  `python -m pytest tests/test_fixed_order_cycle_ratio.py -q` plus a focused
  selection of the new linear-block and slack-identity diagnostics; exact
  test-local \(\mathbb Q(\sqrt2)\) arithmetic is independent of production.
- **Relevant output:** focused selection 19 passed; complete file 66 passed.
  The exhaustive \(n=141\) case covers all \(84\cdot85=7140\) literal
  depth-two histories, including 168 recursive second splits. Deterministic
  cases at \(n=99,141,200,500,1000\) cover intact and forced-recursive
  histories. The exact scan covers every \(99\le n\le1000\).
- **Interpretation:** The tests independently corroborate completion of the
  square, both local floors, their dominance identity, literal child linkage,
  base-edge charging multiplicity, weighted decomposition, prefix step,
  optimizer equations, exact residual inequality, and finite floor/ceil
  estimates.
- **Limitations:** These are bounded diagnostics, not a finite substitute for
  the all-\(n\) proof or an exhaustive geometric search.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---independent-diagnostics-and-memory-synchronization`.

## EV-004 - Complete Verification, Scope, And Review

- **Date:** 2026-07-15
- **Method or command:**
  - `python -m pytest`
  - `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
  - `python -m pytest tests/test_checked_artifact_schema_validation.py -q`
  - `python -m ruff check tests/test_fixed_order_cycle_ratio.py`
  - `python -m ruff check .`
  - `git status --short`, `git diff`, `git diff --check`, and protected-path
    diff inspection
  - three independent proof, test, and synchronization reviews
- **Relevant output:** full suite 242 passed; all four checked certificates,
  76 local brackets, and the \(n=3,4,5,6\) summary verified; schema tests 4
  passed; changed-test Ruff check passed. Repository-wide Ruff reports only
  four known pre-existing findings in untouched files. Independent reviews
  found no blocking algebra, linkage, test, synchronization, or scope defect.
  Final whitespace and protected-path audits pass.
- **Interpretation:** Task-relevant implementation, documentation, and
  reproducibility checks pass, and the diff remains within the requested
  research/test/memory scope.
- **Limitations:** The final user review and manual commit remain outside
  Codex's authority. Pytest reports a non-failing cache warning under the
  restricted workspace permissions.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---complete-verification-and-review-handoff`.

# TASK STATUS - TASK-20260804 / KR1G Fixed Recursive Count

Last update: 2026-08-04

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** repair the committed fixed-\(p\) integration by restoring
  and generalizing the completion Bellman recurrence and exact finite
  minimum, while preserving KR1G-92--KR1G-101 and the unchanged all-middle
  bound for every fixed integer \(p\ge0\).
- **Expected output:** the prefix count through
  \(A^{(q)}_{\ell,\ell-p}\), exact labelled-cycle Bellman and finite-minimum
  formulas, an explicit recovery of the historical \(p=1\) formulation, a
  \(p=2\) fixture with at least two completion labels, corrected dates and
  historical references, and durable-memory updates.

## Scope

- **In scope:** fixed \(p\), fixed \(k\), exactly \(p\) selected recursive
  splits of arbitrary parentage and depth, \(\ell-p\) selected base splits
  on distinct original edges, arbitrary compatible completion below
  \(s_k\), exact finite completion optimization, the iterated order
  \(n\to\infty\) before \(k\to\infty\), and provenance correction for the
  legacy one-recursive dossier.
- **Out of scope:** \(p=p(n)\), \(k=k(n)\), closed-form evaluation of the
  history minimum or equality with KR1G-98/KR1G-99, minimizing-order claims,
  geometry, production code, public tests, schemas, and artifacts.

## Plan And Expected Delta

- [x] Verify the clean accepted baseline and inspect KR1G-1--KR1G-101.
- [x] Prove the exact finite fixed-\(p\) formulation and cubic theorem.
- [x] Implement and run the independent exact \(p=2\) checker.
- [x] Update proof, stable memory, roadmap, current status, and dossier.
- [x] Run repository verification and inspect the final diff.
- [x] Restore the completion Bellman recurrence and exact finite minimum.
- [x] Prove explicitly that \(p=1\) recovers the historical formulation.
- [x] Add and run a focused two-completion-label \(p=2\) fixture.
- [x] Rerun full local verification and record hosted CI separately.

## Verification

- **Checks:** two independent mathematical audits; exact \(p=2\) checker;
  preceding \(p=1\) checker; Ruff; symbolic identities; full repository
  tests; checked-artifact and schema verification; equation-tag, display,
  link, encoding, whitespace, status, and complete-diff audits.
- **Observed result:** KR1G-91a/KR1G-91b restore the exact completion
  recurrence and finite minimum, and KR1G-92--KR1G-101 remain unchanged.
  The fixed-\(p\) checker passes 15,120 selected histories and 151,200
  completions, the focused 42-prefix/4,620-completion two-label Bellman
  fixture, and the 1,296-history position sweep. The one-recursive checker,
  Ruff, 283 repository tests, three focused Arb tests, four checked
  artifacts, four schema tests, symbolic identities, and final source/diff
  checks pass. Hosted CI is separately green on baseline `0240613` for
  Python 3.11--3.13; it does not cover the uncommitted repair.
- **Limitations:** the exact checker uses bounded rational fixtures and does
  not replace the symbolic all-\(q\) proof. KR1G-91b is an exact finite
  optimization formula, not a closed-form evaluation. The theorem fixes
  \(p\) before both limits and makes no \(p=p(n)\), exact asymptotic
  infimum, or geometric claim.

## Blockers / Risks

- No current blocker.
- Residual risk is final human review of the Bellman induction and its
  integration with the already audited dynamic prefix count and
  simultaneous-Cauchy bound.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** the exact fixed-\(p\) Bellman/minimum layer,
  explicit \(p=1\) recovery, preserved universal lower-bound coefficient,
  two-label \(p=2\) fixture, repository regressions, and final source/diff
  audits all pass.
- **Files changed:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `PROJECT_KNOWLEDGE.md`, `research/NEXT_RESEARCH_STEPS.md`,
  `CURRENT_STATUS.md`, this task dossier and checker, and the legacy
  one-recursive dossier's provenance correction; no production module,
  public test, schema, artifact, or workflow.
- **Files to read first:** KR1G-89--KR1G-91b and the unchanged
  KR1G-92--KR1G-101 in `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `exact_checker.py`, and EV-005--EV-007 in `EVIDENCE.md`.

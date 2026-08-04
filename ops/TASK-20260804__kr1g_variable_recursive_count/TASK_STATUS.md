# TASK STATUS - TASK-20260804 / KR1G Variable Recursive Count

Last update: 2026-08-04

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** extend KR1G-98 from a fixed recursive count to variable
  counts whose selected window retains a positive lower density of base
  splits, with an exact finite order-statistic bound and the correctly
  quantified iterated coefficient.
- **Expected output:** authoritative proof, a small independent exact checker,
  aligned durable memory/roadmap/status, and complete verification evidence.

## Scope

- **In scope:** variable integers \(p_{k,n}\); the exact sum of the
  \(b^{\rm base}_{k,n}=\ell_{k,n}-p_{k,n}\) smallest \(d_t\); rounding and
  order-statistic asymptotics at each fixed \(k\); the subsequent
  \(k\to\infty\) limit; recovery of fixed \(p\) and \(p=o(n)\).
- **Out of scope:** geometry, a growing \(k=k(n)\), discrete attainment of
  the residual envelope, minimizing orders, and a closed-form exact residual
  infimum.

## Verified Facts

- Startup baseline `6e5ea239ae06277a836b64253a07f36379bf7a7d` is clean.
- KR1G-98 already permits arbitrary recursive position, parentage, and depth;
  fixedness of \(p\) enters only in the later \(pD_{k,n}=O(n)\) estimate.
- KR1G-102--KR1G-113 prove the exact finite order-statistic replacement,
  fixed-\(k\) rounded limit, and iterated \(\sigma^4C_{\rm dist}\) bound.
- Fixed \(p\) and every \(p=o(n)\) have base density one; only zero lower
  base density remains outside the positive-coefficient theorem.

## Assumptions / Inferences

- The requested \(\sigma^4\) coefficient is a proved lower coefficient for
  the displayed order-statistic numerator and uniform \(Q+2m\) denominator
  relaxation. It is not classified as the strongest correlated KR1G-98
  envelope or an exact residual coefficient.

## Decisions And Rationale

- Preserve KR1G-89--KR1G-101 as the fixed-\(p\) specialization and append a
  separate variable-count theorem.
- Keep the checker independent and task-local because it audits a proof lemma,
  not production behavior.
- State the variable count as a triangular family \(p_{k,n}\) so the nested
  quantifiers and prohibition on \(k=k(n)\) are explicit.

## Plan And Expected Delta

- [x] Derive the finite order-statistic replacement directly from KR1G-98.
- [x] Prove the fixed-\(k\) rounded Riemann/order-statistic limit and then the
  refining-mesh limit.
- [x] Add and run the focused exact checker.
- [x] Align authoritative proof, stable memory, and roadmap.
- [x] Run full tests, artifact checks, and prior KR1G regressions.
- [x] Complete final source/diff audits and set `READY_FOR_REVIEW`.

## Verification

- **Checks:** new checker and Ruff; full pytest; focused Arb and schema tests;
  checked artifacts; prior fixed-count and one-recursive checkers; equation
  tags, local targets/anchors, encoding, line endings, display balance,
  whitespace, full diff, status, and `git diff --check`.
- **Observed result:** every substantive command run so far passes: 283 full
  tests, 3 Arb tests, 4 schema tests, 4 artifacts/76 brackets, the focused
  order-statistic checker, and both historical recursive checkers.
- **Limitations:** finite exact enumeration corroborates but does not replace
  the symbolic theorem. No hosted CI covers the uncommitted working tree.

## Blockers / Risks

- No blocker. Residual risk is final human review of the lower-rearrangement
  proof and its quantifiers.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** the exact checker, full suite, artifact checks,
  and both prior recursive-history checkers pass.
- **Files changed:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `PROJECT_KNOWLEDGE.md`, `research/NEXT_RESEARCH_STEPS.md`,
  `CURRENT_STATUS.md`, and this task dossier/checker; no production module,
  public test, schema, checked artifact, or workflow.
- **Files to read first:** KR1G-102--KR1G-113 in
  `research/FIXED_ORDER_CYCLE_RATIO.md`, `exact_checker.py`, and EV-002--EV-005
  in `EVIDENCE.md`.

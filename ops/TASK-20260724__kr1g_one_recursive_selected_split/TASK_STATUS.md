# TASK STATUS - TASK-20260724 / KR1G One Recursive Selected Split

Last update: 2026-07-24

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** decide the complete KR1G residual for the all-middle class
  with exactly one selected recursive split and all other selected splits on
  distinct original edges.
- **Expected output:** an exact finite formulation, a rigorous fixed-\(k\)
  cubic lower bound or an explicit counterfamily, an independent exact
  small-\(q\) checker, and the required durable-memory updates.

## Scope

- **In scope:** exact domain and rounding; recursive position and direct
  parent; arbitrary completion below \(s_k\); fixed \(k\), then
  \(n\to\infty\), and only afterward an optional \(k\to\infty\) limit.
- **Out of scope:** geometry, growing \(k\), production code, public tests,
  schemas, artifacts, and more than one selected recursive split.

## Plan And Expected Delta

- [x] Verify the accepted clean baseline and inspect KR1G-1--KR1G-88.
- [x] Prove and independently audit the exact finite formulation.
- [x] Run the exact one-recursive checker.
- [x] Update authoritative proof, stable memory, roadmap, and status.
- [x] Run repository verification and inspect the final diff.

## Verification

- **Checks:** three independent mathematical/code audits; exact exhaustive
  checker; Ruff; exact symbolic identities; full repository tests; checked
  artifact and schema verification; equation-tag, display, link, encoding,
  whitespace, status, and diff audits.
- **Observed result:** KR1G-89--KR1G-101 pass every audit after minor
  precision fixes. The checker passes 96,600 broad selected histories and
  6,720 arbitrary completions. Ruff, 283 repository tests, four checked
  artifacts, four schema tests, symbolic identities, and final source/diff
  checks pass.
- **Limitations:** bounded rational fixtures corroborate the finite algebra
  but do not replace the symbolic all-\(q\) theorem. The theorem covers
  exactly one selected recursive split, not two or more.

## Blockers / Risks

- No current blocker.
- Residual risk is final human review of the new finite parametrization,
  completion DP, and combined-Cauchy argument.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact finite formulation, uniform fixed-\(k\)
  cubic theorem, iterated coefficient, checker, repository regressions, and
  final audits all pass.
- **Files changed:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `PROJECT_KNOWLEDGE.md`, `research/NEXT_RESEARCH_STEPS.md`,
  `CURRENT_STATUS.md`, and this task dossier; no production or public test
  file.
- **Files to read first:** KR1G-89--KR1G-101 in
  `research/FIXED_ORDER_CYCLE_RATIO.md` and `EVIDENCE.md`.

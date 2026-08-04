# TASK STATUS - TASK-20260724 / KR1G One Recursive Selected Split

Last update: 2026-08-04

**Historical-date correction:** `TASK-20260724` is a retained legacy slug.
This task was actually performed on 2026-08-04 and recorded by commits
`ce33177d75a596b6b2e9e17f5af351083fd1d84e` and
`069cb677278fc149e2f8fac49b43d3346949c19e`. The earlier 2026-07-24 log
headings are preserved only because `TASK_LOG.md` is append-only; its final
correction entry controls.

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
- **Observed result:** the one-recursive theorem, numbered KR1G-89--KR1G-101
  at historical baseline `069cb677`, passed every audit after minor
  precision fixes. The current proof retains that result inside the
  fixed-\(p\) formulation as KR1G-89--KR1G-91b and KR1G-92--KR1G-101. The
  checker passes 96,600 broad selected histories and 6,720 arbitrary
  completions. Ruff, 283 repository tests, four checked artifacts, four
  schema tests, symbolic identities, and final source/diff checks pass.
- **Post-review correction:** the final audit had verified roadmap links and
  anchors but missed that `Next Atomic Task` still named the preceding
  distinct-original-edge theorem. The handoff now names the current
  all-middle theorem with exactly one selected recursive split; the targeted
  link/anchor, UTF-8/LF, whitespace, scope, full-diff, and
  `git diff --check` controls were repeated and pass.
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
- **Post-review correction files:** only
  `research/NEXT_RESEARCH_STEPS.md` and this task dossier; the proof, stable
  memory, checker, production code, and tests are unchanged.
- **Files to read first:** the fixed-\(p\) KR1G-89--KR1G-101 section in
  `research/FIXED_ORDER_CYCLE_RATIO.md`, this dossier's date-correction log
  entry, and `EVIDENCE.md`.

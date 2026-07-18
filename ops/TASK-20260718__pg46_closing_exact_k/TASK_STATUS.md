# TASK_STATUS - TASK-20260718 / Closing PG46 Exact K

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** determine exactly the induced objective \(K\) for the PG46
  shift placing \(P_m\) in the closing gap on \(n=10m+3\), \(m\ge3\), and
  classify every maximizing subset.
- **Expected output:** an all-\(m\) symbolic theorem, exact comparison with
  K825, one bounded independent diagnostic, and synchronized authoritative
  memory without any geometric or global optimality inference.

## Scope

- **In scope:** the prescribed closing PG46 bijection, its one explicit core
  order, induced-cycle subset optimization, shortcut-budget proof, exact
  block sum, minimum and boundary ranges, K825 comparison, and the coefficient
  \(143/500\).
- **Out of scope:** other PG46 witnesses, permutation or matching search,
  geometric realizability, angular ordering, global minimization, and any
  change to production code or checked artifacts.

## Verified Facts

- Startup found a clean tree at commit
  `963aa533e254cc94e17c1d5e7cd81284df13d552`.
- The prescribed PG46 shift is already proved relation-compatible and
  full-optimal for \(W\); those facts are inputs, not conclusions about \(K\).
- Exact symbolic derivation gives the unique maximizing subset
  \(S_m=\{4m+1,\ldots,10m+3\}\) and
  \(K=(572m^3+631m^2+223m+22)/2\).
- Relative to K825 the exact difference is \(m^2-6m-4\): improvement only
  for \(m=3,4,5,6\), no integer tie, and strict worsening for \(m\ge7\).
- Both families retain leading coefficient \(143/500\).

## Assumptions / Inferences

- None beyond the declared symbolic domain \(m\ge3\) and the previously
  proved PG46 construction facts.
- Bounded computation is corroborative and is not used as the infinite proof.

## Decisions And Rationale

- Use the isolated holes \(H_m=\{2,\ldots,4m\}\), an exhaustive local-gain
  table, and a complete compressed-arc shortcut audit to prove uniqueness.
- Use one dossier-local standard-library diagnostic with a max-plus
  increasing-path DP; it neither enumerates permutations nor matchings.
- Synchronize only the three pertinent research sources, the three root
  memory files, and this task dossier.

## Plan And Expected Delta

- Exact proof and authoritative synchronization are complete.
- Independent diagnostic, regressions, source-structure checks, and final
  audits are complete.
- No production, test, schema, artifact, certificate, or upstream file
  changed.

## Verification

- **Checks:** diagnostic, Ruff, 150 focused tests, 283 full-suite tests, four
  schema tests, checked-artifact verification, source structure,
  `git diff --check`, and three independent read-only audits.
- **Observed result:** all checks pass. The reviewers' sole preliminary
  finding, a missing comparison in the claimed exact shortcut minimum, was
  closed symbolically and re-audited.
- **Limitations:** no hosted CI, geometry, or global-order search is in scope.

## Blockers / Risks

- No blocker or known residual defect. User review and commit remain manual.

## Next Atomic Action

- User manual review and commit decision.

## Handoff

- **Last verified result:** exact formulas, unique subset, all shortcut and
  block boundaries, crossover, coefficient decision, diagnostic, regressions,
  and cross-source wording all pass independent review.
- **Files changed:** six authoritative Markdown sources and this four-file
  dossier.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`, then
  `EVIDENCE.md` in this directory.

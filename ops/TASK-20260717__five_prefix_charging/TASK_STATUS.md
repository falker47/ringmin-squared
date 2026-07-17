# TASK STATUS - Five-Prefix One-Use Charging

Last update: 2026-07-17

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** prove or refute the direct five-prefix extension of the
  one-use charging theorem in `research/FIXED_ORDER_CYCLE_RATIO.md`.
- **Expected output:** either an exact five-segment finite theorem with a
  canonical one-use original-edge partition and a recursive invariant through
  four boundaries, or the minimum literal counterexample and exact failure
  point; in either case, one standalone exact local-history oracle.

## Scope

- **In scope:** the direct four-prefix theorem CR28de--CR28dk, its STRICT
  dossier and literal oracle, the normalized fixed-`k` simplex, exact finite
  five-segment charging, and local five-split histories on one small base.
- **Out of scope:** coefficient optimization, finite rounding, any
  `k -> infinity` passage, new geometric claims, production code, tests,
  artifacts, schemas, backends, certificates, and enumeration limits.

## Verified Facts

- Startup used a clean `main` worktree at
  `1116b1274949475da8462994f296ebd22d0a7bf3`.
- The four-prefix theorem gives a canonical charged/unused partition of the
  original base edges and a recursive invariant through three boundaries.
- The normalized simplex is proved for every fixed `k`, but before this task
  it supplied no charging theorem for `k >= 5`.
- The five-prefix extension is true. The six convex coefficients telescope to
  five disjoint weighted split segments.
- Every literal history induces one canonical charged/unused partition of the
  original edges, and the recursive endpoint invariant survives all four
  boundaries and arbitrary nesting.
- The exact finite inequality is
  \[
  \begin{aligned}
  \gamma^{(r)}_{1,n}\ge{}&P_{r,n}
  +(r-s_1)F_{1,n}+(s_1-s_2)F_{2,n}+(s_2-s_3)F_{3,n}\\
  &+(s_3-s_4)F_{4,n}+(s_4-s_5)F_{5,n}.
  \end{aligned}
  \]
- The standalone exact oracle passes all 15,120 histories of a five-edge
  base, including 120 histories charging all five original edges and 2,520
  fifth splits whose endpoints were both inserted earlier.

## Assumptions / Inferences

- The normalized simplex remains independent context; the five-prefix result
  rests on direct literal-history bookkeeping.

## Decisions And Rationale

- Use the same combined-height-before-charging architecture as the direct
  four-prefix theorem, then audit the fourth boundary independently.
- Keep the sole new oracle dossier-local and standard-library-only.

## Plan And Expected Delta

- Derive or falsify the six-coefficient height inequality.
- Determine whether telescoping yields five disjoint weighted segments.
- Prove or falsify injectivity of original-edge charging and the recursive
  endpoint invariant after the fifth selected split.
- Add one exact bounded oracle covering every local history of five splits.
- Synchronize the requested proof note, dossier, stable memory, current
  status, and roadmap, plus the authoritative project brief, then verify and
  inspect the complete diff.

## Verification

- **Checks:** standalone oracle, Ruff lint/format, focused and complete pytest,
  checked-artifact verifier, schema regression, equation/Markdown structure,
  UTF-8/newline checks, three independent audits, scope inspection, and final
  diff checks.
- **Observed result:** 15,120 histories, 101 focused tests, all 283 local
  tests, 4 certificates with 76 local brackets, and 4 schema tests pass. All
  321 equation tags are unique; source structure, line endings, scope, and
  final diff checks pass.
- **Limitations:** bounded computation corroborates, but does not prove, the
  all-history statement. Hosted GitHub Actions were not inspected.

## Blockers / Risks

- No blocker. Residual limitations are the deliberately excluded coefficient,
  rounding, six-prefix, limiting-prefix, and geometric questions.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact theorem, oracle, all regressions, three
  independent audits, synchronization, and final diff inspection pass.
- **Files changed:** proof note, project brief, stable knowledge, roadmap,
  current status, and this dossier.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md` and
  this dossier.
- **Suggested manual commit message:**
  `Prove exact five-prefix one-use charging`.

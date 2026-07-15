# TASK_STATUS - TASK-20260715__three_nested_tail_obstruction / Three Nested-Tail Obstruction

Last update: 2026-07-15

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** define the exact obstruction from
  \(S_m,S_{m+1},S_{m+2}\), reduce it to a simple base cycle plus two
  compatible insertions, audit every split interaction and cycle condition,
  and determine the optimized cubic coefficient.
- **Expected output:** exact method-specific proof, bounded exact test-local
  checks, synchronized durable memory, and no production or enumeration-limit
  change.

## Scope

- **In scope:** base-cycle/double-split bijection; prefix-sum score; nested,
  distinct-incident, and distinct-disjoint interactions; linked simple-cycle
  signatures; uniform \(O(n^2)\) comparison; optimization in \(m\); focused
  exact verification.
- **Out of scope:** production source or API changes; larger enumeration
  limits; geometric certificate generation; an exact asymptotic claim for
  \(\Lambda_n\) or \(R_2^*(n)\); Git writes.

## Verified Facts

- Startup files and the preceding two-tail dossier were read; the initial
  worktree was clean at c99c9b8b00ba.
- For \(n\ge5\), \(1\le m\le n-4\), the base tail has
  \(q=n-m-1\ge3\) labels, so no two-label double-edge exception occurs.
- Deleting \(m\), then \(m+1\), gives a bijection between outer cycles and a
  simple base cycle with two compatible edge splits.
- The exact correction is \(P(C)+\max(0,A,A+B)\); replacing it by a sum of
  positive parts is only an upper bound.
- Every signature must be one connected loopless degree-two spanning cycle
  with no repeated edge, and consecutive signatures must satisfy the literal
  split identities.
- Uniformly,
  \[
  0\le\gamma^*_{m,n}-P^*_{m+2,n}<2n^2,
  \qquad
  P_{m+2,n}\le\gamma^*_{m,n}<P_{m+2,n}+2n^2.
  \]
- The optimized obstruction satisfies
  \[
  \Gamma_n^{(3)}
  ={2(\sqrt2-1)\over3}n^3+O(n^2).
  \]
  This is method-specific and not an asymptotic evaluation of
  \(\Lambda_n\) or \(R_2^*(n)\).

## Assumptions / Inferences

- \(P^*_{\ell,n}\) denotes the exact minimum simple-cycle score, while
  \(P_{\ell,n}\) remains the established duplicated-pairing floor.
- Finite tests verify arithmetic, linkage, and bounded coverage only; the
  all-\(n\) theorem rests on the written proof.

## Decisions And Rationale

- Retain nested splits in the bijective parametrization even though an exact
  dominance argument permits their removal from the minimum; they can tie on
  the prefix-maximum plateau.
- Keep every new computational path inside the test module and in exact
  integer arithmetic.
- Preserve the production cyclic-ratio boundary \(n\le8\) and all source,
  artifact, schema, and verifier contracts.

## Plan And Expected Delta

- Completed: exact reduction, interaction taxonomy, and signature audit.
- Completed: uniform comparison with both \(P^*\) and \(P\), followed by
  rigorous optimization.
- Completed: bounded exact test-local checks and durable synchronization.
- Completed: proportional regression, independent audits, and diff review.

## Verification

- **Checks:** focused new tests, complete cyclic-ratio and induced-subset
  modules, full local suite, checked-artifact verifier, schema suite, Ruff,
  independent proof/test/scope audits, Git/diff inspection, and production
  boundary audit.
- **Observed result:** 3 focused tests pass; cyclic-ratio module 40 passed;
  induced-subset module 7 passed; full suite 216 passed; all 4 certificates
  and 76 local brackets verified; schema suite 4 passed; Ruff and hygiene
  checks pass.
- **Limitations:** hosted GitHub Actions were not run for this worktree.

## Blockers / Risks

- No current blocker.
- The theorem covers one optimized block of exactly three tails. It does not
  cover a block length growing with \(n\).

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact three-tail theorem, bounded exact checks,
  complete local regression, and independent audits pass.
- **Files changed:** cyclic-ratio proof note, one test module, project brief,
  stable knowledge, roadmap, current status, and this dossier; no production
  source changed.
- **Files to read first:** research/FIXED_ORDER_CYCLE_RATIO.md,
  tests/test_fixed_order_cycle_ratio.py, and this file.

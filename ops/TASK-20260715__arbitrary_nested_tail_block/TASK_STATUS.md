# TASK_STATUS - TASK-20260715__arbitrary_nested_tail_block / Arbitrary Nested-Tail Block

Last update: 2026-07-15

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** generalize the exact consecutive-tail obstruction to a block
  of \(r=r(n)\ge2\) tails, including the compatible split history, every
  correction prefix, a uniform comparison with the inner-cycle minimum, and
  the first growth scale not excluded from changing the cubic coefficient.
- **Expected output:** exact method-specific proof, bounded exact test-local
  oracle covering \(r=4\), synchronized durable memory, and no production,
  enumeration-limit, artifact, schema, verifier, or certificate change.

## Scope

- **In scope:** descending insertion histories; literal split linkage;
  prefix-score identity; admissible nested domino histories; uniform
  \(O(rn^2)\) error; \(r=o(n)\) optimization; bounded exact verification;
  proof, tests, roadmap, and dossier synchronization.
- **Out of scope:** production source or API changes; larger enumeration
  limits; artifact or certificate generation; an exact asymptotic value for
  \(\Lambda_n\) or \(R_2^*(n)\); Git writes.

## Verified Facts

- Startup memory and the preceding three-tail dossier were read; the initial
  worktree was clean on main at 006aa61c71ad.
- For \(2\le r\le n-2\), \(1\le m\le n-r-1\), and
  \(\ell=m+r-1\), cycles on \(S_m\) are in bijection with a simple base
  cycle on \(S_\ell\) and \(r-1\) compatible descending edge splits.
- The exact objective is the base score plus the maximum of every signed
  correction prefix. Every intermediate signature and literal linkage is
  required.
- Recursively nested child-edge dominoes are admissible and can attain the
  history envelope \(\sum_{t=m}^{\ell-1}[t^2-2]_+\). They cannot generally
  be replaced by distinct base edges.
- Uniformly,
  \[
  0\le\gamma^{(r)}_{m,n}-P^*_{\ell,n}
  \le\sum_{t=m}^{\ell-1}[t^2-2]_+<(r-1)n^2,
  \]
  and
  \[
  P_{\ell,n}\le\gamma^{(r)}_{m,n}<P_{\ell,n}+rn^2.
  \]
- Every fixed \(r\), and every \(r=o(n)\), preserves the method coefficient
  \(2(\sqrt2-1)/3\). Linear \(r=\Theta(n)\) is the first scale not excluded,
  not a proved improvement.
- At \((m,n,r)=(2,7,4)\), the exact test-local oracle maps all 60 compatible
  histories to all 60 direct outer cycles and gives
  \((P_{5,7},P^*_{5,7},\gamma^{(4)}_{2,7})=(106,107,118)\).

## Assumptions / Inferences

- The theorem deliberately keeps the inner tail at cardinality at least
  three. The two-label double-edge convention is outside its domain.
- Finite tests verify exact arithmetic, linkage, and bounded coverage only;
  the all-\(n\) theorem rests on the written proof.

## Decisions And Rationale

- Keep all computational additions test-local and exact.
- Preserve every recursive child-edge split instead of generalizing the
  special three-tail distinct-base-edge reduction.
- Keep \(\Gamma_n^{(r)}=\max_m\min_\sigma\) as a separately optimized
  one-block obstruction; do not exchange max and min.
- Classify the sublinear result as method-specific and leave the linear scale
  open.

## Plan And Expected Delta

- Completed: exact history bijection, prefix formula, compatibility audit,
  domino construction, uniform comparison, and sublinear optimization.
- Completed: bounded \(r=2,3,4\) oracle with direct signature-map agreement.
- Completed: proof, tests, roadmap, stable memory, current status, and dossier
  synchronization.
- Completed: proportional regression, independent audits, and diff review.

## Verification

- **Checks:** seven focused new cases; complete cyclic-ratio module; complete
  local suite; checked-artifact verifier; schema suite; focused Ruff; full
  repository Ruff; independent proof/test/scope audits; Git/diff hygiene; and
  production-boundary inspection.
- **Observed result:** 7 focused cases pass; cyclic-ratio module 47 passed;
  full suite 223 tests passed; all 4 checked certificates and 76 local
  brackets verified; schema suite 4 passed; focused Ruff and independent
  audits pass; no production/source path changed.
- **Recorded failed check:** repository-wide Ruff reports four existing
  findings in untouched files: two in src/power_ringmin/critical_structure.py,
  one in src/power_ringmin/fixed_order_artifact.py, and one in
  tests/test_finite_results.py. The modified Python file passes Ruff.
- **Limitations:** hosted GitHub Actions were not run for this worktree.

## Blockers / Risks

- No current blocker.
- Linear-size block optimization remains open, and no exact asymptotic
  coefficient or convergence theorem for \(\Lambda_n\) or \(R_2^*(n)\) is
  claimed.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact arbitrary-block theorem, bounded exact
  oracle, full local regression, and independent audits pass.
- **Files changed:** cyclic-ratio proof note, one test module, project brief,
  stable knowledge, roadmap, current status, and this STRICT dossier; no
  production source changed.
- **Files to read first:** research/FIXED_ORDER_CYCLE_RATIO.md,
  tests/test_fixed_order_cycle_ratio.py, and this file.

# TASK_STATUS - TASK-20260715__first_linear_tail_block / First Linear Tail Block

Last update: 2026-07-15

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** correct the prior first-linear-block handoff by deriving the
  global corollary already implied by CR28ap and CR28bg, explicitly preserving
  max--min order, and deduce the resulting lower coefficients for
  \(\Lambda_n\) and \(R_2^*(n)\).
- **Expected output:** exact finite global chain and asymptotic lower bounds,
  exact test-local coefficient algebra, synchronized proof note, lower-bound
  note, brief, stable memory, roadmap, current status, and dossier, with no
  production, artifact, or enumeration-limit change.

## Scope

- **In scope:** the exact split-history/prefix formula; literal recursive
  compatibility; the maximum over every prefix; explicit floor/ceiling
  conventions; the pointwise-to-global quantifier passage; lower coefficients
  for \(\Lambda_n\) and \(R_2^*(n)\); exact test-local algebra; durable proof,
  roadmap, and dossier updates.
- **Out of scope:** exchanging a global max and min; proving convergence or an
  exact leading/residual coefficient; classifying other linear densities;
  production source or limits; artifact, schema, verifier, or certificate
  changes; Git writes.

## Verified Facts

- The startup tree was clean on main at
  9c39f6a621c1eca41277b2ae72a60c634aa59fe4.
- The block is in the ordinary arbitrary-history domain for every \(n\ge5\).
- For \(s_n=\lceil2n/5\rceil\), the selected prefix is certainly nonempty
  for every \(n\ge141\).
- Every base cycle \(C\) on \(S_{r_n}\) has the exact slack identity
  \[
  P(C)-P_{r_n,n}
  =
  {1\over2}\sum_{\{u,v\}\in E(C)}
  (u+v-n-r_n)^2.
  \]
- Charging an intact base split once against its edge slack and treating
  every recursive split separately gives an exact finite lower bound for
  every compatible history.
- The direct CR28bg form is
  \[
  \gamma^{(r_n)}_{1,n}
  \ge P_{r_n,n}+(r_n-s_n)L_n.
  \]
  The pairing floor here is nonstarred; comparison with \(P^*_{r_n,n}\)
  separately incurs the alternating-cycle correction.
- The resulting residual obeys
  \[
  \gamma^{(r_n)}_{1,n}-P^*_{r_n,n}
  \ge c_0n^3-C_0n^2
  \qquad(n\ge141),
  \]
  where
  \[
  c_0={389-275\sqrt2\over375}>0,
  \qquad
  C_0={2(20\sqrt2-27)\over75}+{1\over8}.
  \]
  Thus the second requested alternative holds for this block.
- For each admissible \(m\), the pointwise inequality
  \(\Lambda(\sigma)\ge\max_jP_\sigma(S_{m+j})\) is minimized first. Taking
  the maximum of the resulting lower bounds therefore proves, without a
  max--min exchange,
  \[
  \Lambda_n
  \ge\Gamma_n^{(r_n)}
  \ge\gamma^{(r_n)}_{1,n}
  \ge P_{r_n,n}+(r_n-s_n)L_n
  \qquad(n\ge141).
  \]
- Exact floor expansion and the existing local estimates give
  \[
  \Lambda_n
  \ge {139-25\sqrt2\over375}n^3
  -{40\sqrt2-54\over75}n^2
  \qquad(n\ge141),
  \]
  and CR27 gives the same cubic coefficient divided by \(\pi\) for
  \(R_2^*(n)\), with its explicit quadratic subtraction.
- Nine focused bounded test-local cases pass: the slack identity is checked
  exhaustively on tail sizes three through six, and deterministic
  intact-base/recursive histories are checked at
  \(n=141,200,500,1000\).

## Assumptions / Inferences

- The finite right-hand side need not be positive at \(n=141\); the displayed
  quantitative bound becomes positive for every \(n\ge655\).
- Bounded diagnostics corroborate arithmetic and linkage only. The all-\(n\)
  result rests on the exact written proof.

## Decisions And Rationale

- Use the prefix ending at \(s_n=\lceil2n/5\rceil\) and the elementary
  inequality \(\max(0,H)\ge H/2\).
- Preserve recursive splits rather than replacing them by base-edge choices.
- Compare with \(P^*_{r_n,n}\) only through the proved alternating-cycle
  upper excess; do not assume equality with the pairing floor.
- Apply CR28bg directly to the nonstarred pairing floor for the global
  corollary; do not route that chain through \(P^*_{r_n,n}\).
- Classify the new numbers as exact coefficients of proved lower bounds, not
  as exact residual or asymptotic leading coefficients.

## Plan And Expected Delta

- Completed: correction audit, independent quantifier/algebra reviews, proof
  note, exact coefficient test, project brief, and stable memory updates.
- Completed: lower-bound note, roadmap, current status, dossier, complete
  regression, final scope/diff audits, and corrected handoff.

## Verification

- **Checks completed:** pre-change cyclic-ratio baseline (47 passed);
  corrected focused selection (9 passed); complete cyclic-ratio module
  (57 passed); complete local suite (233 passed); checked-artifact verifier (4
  certificates and 76 local brackets); schema suite (4 passed); focused
  Ruff; independent proof, rounding, and synchronization audits; diff hygiene;
  and no-production-diff audit.
- **Recorded unrelated check:** repository-wide Ruff retains four existing
  findings in untouched files: two in `critical_structure.py`, one in
  `fixed_order_artifact.py`, and one in `test_finite_results.py`.
- **Limitations:** hosted GitHub Actions have not run these worktree changes.

## Blockers / Risks

- No current blocker.
- The constant \(c_0\) is a certified residual lower constant, not claimed
  optimal. The global coefficient \((139-25\sqrt2)/375\) is likewise a
  certified lower coefficient, not the exact leading coefficient.

## Next Atomic Action

- User review and manual commit decision; do not begin the proposed next task
  in this chat.

## Handoff

- **Last verified result:** the exact global corollary, coefficient algebra,
  complete local regression, artifact/schema checks, documentation
  synchronization, and final scope/diff audits pass.
- **Files to read first:** research/FIXED_ORDER_CYCLE_RATIO.md,
  tests/test_fixed_order_cycle_ratio.py, and this file.

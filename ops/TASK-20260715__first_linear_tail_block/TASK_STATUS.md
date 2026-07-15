# TASK_STATUS - TASK-20260715__first_linear_tail_block / First Linear Tail Block

Last update: 2026-07-15

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** correct only the notation collision introduced by the first
  linear block, reserving the established full-distance symbol and assigning
  an unambiguous superscripted symbol to the block-local floor.
- **Expected output:** synchronized notation in the proof and handoff sources,
  repository-wide ambiguity audit, focused and complete tests, diff hygiene,
  and a new review handoff without mathematical or production changes.

## Scope

- **In scope:** rename the local floor
  \(\min\{G_n(s_n),J_n(s_n)\}\) as \(F_n^{\mathrm{blk}}\) in the named
  synchronized sources and dossier; preserve \(L_n\) for the full-distance
  obstruction; audit every repository occurrence; update the handoff.
- **Out of scope:** formula, tag, coefficient, domain, theorem, proof,
  mathematical-test, production, artifact, schema, verifier, certificate, or
  enumeration-limit changes; Git writes.

## Verified Facts

- The notation-correction startup tree was clean on main at
  e47dfe0e8ee56158b20fc6475bb38c35219c5eaf.
- The authoritative local definition is now
  \[
  F_n^{\mathrm{blk}}=\min\{G_n(s),J_n(s)\},
  \]
  with tag CR28bd unchanged. The full-distance obstruction retains \(L_n\).
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
  \ge P_{r_n,n}+(r_n-s_n)F_n^{\mathrm{blk}}.
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
  \ge P_{r_n,n}+(r_n-s_n)F_n^{\mathrm{blk}}
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

- Use the superscripted \(F_n^{\mathrm{blk}}\), because bare \(F_n\) is
  already used elsewhere for a feasible set and would create a new collision.
- Preserve all full-distance uses of \(L_n\); do not perform a global blind
  replacement.
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

- Completed: classify every repository-wide use of \(L_n\), rename only the
  28 block-local references, and synchronize the named sources and dossier.
- Completed: focused preservation checks, complete regression, final
  scope/diff audits, durable evidence, and notation-only handoff.

## Verification

- **Checks completed:** first-linear-block focused selection (9 passed),
  full-distance-obstruction focused preservation check (1 passed), complete
  local suite (233 passed), repository-wide primary and alternate-spelling
  notation searches, diff hygiene, and no-production/no-test-diff audit.
- **Notation result:** every residual \(L_n\) is the established full-distance
  obstruction or an explicit statement reserving that name; all 28 prior
  block-local references use \(F_n^{\mathrm{blk}}\).
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

- **Last verified result:** the notation collision is removed in every named
  source and dossier file; focused and complete tests, repository-wide
  ambiguity search, scope audit, and diff hygiene pass without code changes.
- **Files to read first:** research/FIXED_ORDER_CYCLE_RATIO.md,
  research/PRODUCT_DISTANCE_SURROGATE.md, and this file.

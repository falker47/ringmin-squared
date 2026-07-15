# TASK_STATUS - TASK-20260715__first_linear_tail_block / First Linear Tail Block

Last update: 2026-07-15

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** for
  \(\alpha=\sqrt2-1\), \(m=1\), and
  \(r_n=\lfloor\alpha n\rfloor\), prove either an \(o(n^3)\) compatible
  split-history excess or a positive cubic residual above
  \(P^*_{r_n,n}\), with explicit domain and rounding.
- **Expected output:** exact block-local proof, bounded exact test-local
  diagnostics, synchronized proof note and roadmap, and no claim or change
  involving \(\Lambda_n\), geometry, production enumeration, artifacts, or
  certificates.

## Scope

- **In scope:** the exact split-history/prefix formula; literal recursive
  compatibility; the maximum over every prefix; explicit floor/ceiling
  conventions; one linear block; bounded exact diagnostics; durable proof,
  roadmap, and dossier updates.
- **Out of scope:** exchanging a global max and min; an asymptotic evaluation
  of \(\Lambda_n\); geometric consequences; production source or limits;
  artifact, schema, verifier, or certificate changes; Git writes.

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
- Classify the result as an exact method-specific cubic residual for one
  block, not as an exact coefficient or global consequence.

## Plan And Expected Delta

- Completed: startup, exact lower proof, independent audits, and focused
  bounded diagnostics.
- Completed: proof note, project brief, stable memory, roadmap, and current
  status updates.
- Completed: complete regression, final diff/scope audits, and
  READY_FOR_REVIEW handoff.

## Verification

- **Checks completed:** pre-change cyclic-ratio baseline (47 passed); focused
  new diagnostics (9 passed); complete cyclic-ratio module (56 passed);
  complete local suite (232 passed); checked-artifact verifier (4
  certificates and 76 local brackets); schema suite (4 passed); focused
  Ruff; independent proof and rounding audits; diff hygiene; and
  no-production-diff audit.
- **Recorded unrelated check:** repository-wide Ruff retains four existing
  findings in untouched files: two in `critical_structure.py`, one in
  `fixed_order_artifact.py`, and one in `test_finite_results.py`.
- **Limitations:** hosted GitHub Actions have not run these worktree changes.

## Blockers / Risks

- No current blocker.
- The constant \(c_0\) is a certified lower constant, not claimed optimal.

## Next Atomic Action

- User review and manual commit decision; do not begin the proposed next task
  in this chat.

## Handoff

- **Last verified result:** exact positive cubic residual, complete local
  regression, artifact/schema checks, and final scope/diff audits pass.
- **Files to read first:** research/FIXED_ORDER_CYCLE_RATIO.md,
  tests/test_fixed_order_cycle_ratio.py, and this file.

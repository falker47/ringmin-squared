# CURRENT_STATUS - power-ringmin

Last update: 2026-07-15

- **Current phase:** first explicit linear-block analysis for the exact
  consecutive-tail obstruction.
- **Current task:** decide the subcubic-history versus positive-cubic-residual
  alternative for \(m=1\) and
  \(r_n=\lfloor(\sqrt2-1)n\rfloor\).
- **Task dossier:**
  `ops/TASK-20260715__first_linear_tail_block/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Implemented Scope

- The ordinary exact split-history formula is specialized to
  \[
  \alpha=\sqrt2-1,
  \qquad
  m=1,
  \qquad
  r_n=\lfloor\alpha n\rfloor
  =\lfloor\sqrt{2n^2}\rfloor-n.
  \]
  Its block domain holds for every integer \(n\ge5\).
- The proof keeps every literal current-edge split, including recursively
  nested child-edge splits, and retains the maximum over all correction
  prefixes.
- With \(s_n=\lceil2n/5\rceil\), the selected prefix is nonempty throughout
  the explicit sufficient domain \(n\ge141\).
- No production source, API, scorer, canonicalizer, enumerator, ceiling,
  schema, artifact, example, verifier, backend, or certificate contract
  changed.

## Exact Method Result

- EXACT THEOREM: every simple base cycle \(C\) on \(S_{r_n}\) satisfies
  \[
  P(C)-P_{r_n,n}
  =
  {1\over2}\sum_{\{u,v\}\in E(C)}
  (u+v-n-r_n)^2.
  \]
- EXACT METHOD-SPECIFIC THEOREM: charging an intact base edge at most once
  against this slack, and bounding recursive splits separately, gives the
  exact finite comparison
  \[
  \gamma^{(r_n)}_{1,n}-P^*_{r_n,n}
  \ge
  (r_n-s_n)L_n-e(n-r_n+1)
  \qquad(n\ge141),
  \]
  with \(L_n\), \(e\), and all rounding conventions defined in
  `research/FIXED_ORDER_CYCLE_RATIO.md`.
- EXACT METHOD-SPECIFIC CUBIC RESIDUAL: for every \(n\ge141\),
  \[
  \gamma^{(r_n)}_{1,n}-P^*_{r_n,n}
  \ge c_0n^3-C_0n^2,
  \]
  where
  \[
  c_0={389-275\sqrt2\over375}>0,
  \qquad
  C_0={2(20\sqrt2-27)\over75}+{1\over8}.
  \]
  The displayed finite lower bound is positive for every \(n\ge655\).
  Hence the second requested alternative holds: no compatible history for
  this block has \(o(n^3)\) excess over \(P^*_{r_n,n}\).

## Bounded Exact Diagnostics

- VERIFIED FACT (FINITE EXACT TEST-ONLY COMPUTATION): the base-slack identity
  is checked exhaustively on all dihedral cycles of tail sizes three through
  six.
- At \(n=141,200,500,1000\), deterministic policies preferring intact base
  edges or forcing recursive child edges check floor/ceiling arithmetic,
  literal linkage, every local bound, prefix averaging, and the finite
  comparison.
- A fixed-seed read-only diagnostic additionally checked 200 compatible
  prefix histories across those four sizes with exact arithmetic.
- These bounded diagnostics call no production scorer, canonicalizer, or
  enumerator and are not the all-\(n\) proof.

## Verification

- New focused selection: 9 passed.
- Complete cyclic-ratio module: 56 passed.
- Complete local suite: 232 passed.
- Checked-artifact verifier: all 4 certificates and 76 local brackets
  verified; schema suite: 4 passed.
- Focused Ruff on the modified Python test passes.
- Repository-wide Ruff reports four existing findings in untouched files:
  two in `src/power_ringmin/critical_structure.py`, one in
  `src/power_ringmin/fixed_order_artifact.py`, and one in
  `tests/test_finite_results.py`. They are recorded but not mixed into this
  task.
- Independent proof, rounding, compatibility, and synchronization audits
  found no flaw.
- Git diff hygiene and the no-production-diff audit pass.
- CURRENT HOSTED STATUS: GitHub Actions has not run these worktree changes.

## Files Changed

- `research/FIXED_ORDER_CYCLE_RATIO.md` adds the authoritative block-local
  theorem, finite constants, compatibility audit, and limitations.
- `tests/test_fixed_order_cycle_ratio.py` adds bounded independent exact
  diagnostics only.
- `start.md`, `PROJECT_KNOWLEDGE.md`, and
  `research/NEXT_RESEARCH_STEPS.md` synchronize stable knowledge and the
  research boundary.
- `CURRENT_STATUS.md` and the STRICT task dossier record durable handoff.

## Residual Limitations

- The constant \(c_0\) is a certified lower constant, not the exact residual
  coefficient and not claimed optimal.
- Other linear densities and starting indices remain unclassified.
- The result concerns one separately optimized block and its exact
  inner-cycle reference. It does not exchange any global max and min.
- No asymptotic evaluation of \(\Lambda_n\), exact angular-geometric result,
  or production-computation claim follows.
- Finite tests verify arithmetic and bounded compatible histories only; they
  are not the all-\(n\) proof.
- Hosted GitHub Actions remain unverified.

## Proposed Next Task

In a fresh chat, optimize the same block-local slack/prefix certificate over
its cutoff and averaging weight, determining the best rigorously certified
cubic lower constant available from that template or proving the current
parameters optimal within it.

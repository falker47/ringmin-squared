# CURRENT_STATUS - power-ringmin

Last update: 2026-07-15

- **Current phase:** notation hygiene for the first explicit linear-block
  lower obstruction.
- **Current task:** remove the collision between the block-local floor and the
  already defined full-distance obstruction, with no mathematical change.
- **Task dossier:**
  `ops/TASK-20260715__first_linear_tail_block/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Implemented Scope

- The block-local floor is now denoted
  \(F_n^{\mathrm{blk}}=\min\{G_n(s_n),J_n(s_n)\}\). The symbol \(L_n\)
  remains reserved for the full-distance obstruction defined in
  `research/PRODUCT_DISTANCE_SURROGATE.md`.
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
- The pointwise full-score domination is minimized separately for each block
  start before those scalar lower bounds are maximized. No max--min exchange
  is used.
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
  (r_n-s_n)F_n^{\mathrm{blk}}-e(n-r_n+1)
  \qquad(n\ge141),
  \]
  with \(F_n^{\mathrm{blk}}\), \(e\), and all rounding conventions defined in
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
- EXACT GLOBAL COROLLARY: CR28bg uses the nonstarred duplicated-pairing floor
  and proves, for every \(n\ge141\),
  \[
  \Lambda_n
  \ge\Gamma_n^{(r_n)}
  \ge\gamma^{(r_n)}_{1,n}
  \ge P_{r_n,n}+(r_n-s_n)F_n^{\mathrm{blk}}.
  \]
  The first inequality is obtained by minimizing pointwise domination for
  each fixed \(m\), then taking the maximum of the resulting scalar bounds.
- EXACT FINITE GLOBAL LOWER BOUNDS: exact floor expansion gives
  \[
  \Lambda_n
  \ge {139-25\sqrt2\over375}n^3
  -{40\sqrt2-54\over75}n^2,
  \]
  while CR27 gives
  \[
  R_2^*(n)
  >{139-25\sqrt2\over375\pi}n^3
  -\left(1+{40\sqrt2-54\over75\pi}\right)n^2
  \qquad(n\ge141).
  \]
  Thus the corresponding liminf lower coefficients are
  \((139-25\sqrt2)/375\) and that number divided by \(\pi\).

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
- A new test-local \(\mathbb Q(\sqrt2)\) calculation checks exactly the
  pairing-floor coefficient, residual coefficient, their sum
  \((139-25\sqrt2)/375\), the quadratic remainder, and positivity.
- These bounded diagnostics call no production scorer, canonicalizer, or
  enumerator and are not the all-\(n\) proof.

## Verification

- First-linear-block focused selection: 9 passed.
- Full-distance-obstruction focused preservation check: 1 passed.
- Complete local suite: 233 passed.
- Repository-wide notation search classifies every residual \(L_n\) as the
  full-distance obstruction or as an explicit statement reserving that name;
  no block-local use remains.
- All 28 pre-existing block-local references are synchronized to
  \(F_n^{\mathrm{blk}}\); alternate spellings of the old symbol are absent.
- Git diff hygiene and the no-production/no-test-diff audit pass.
- CURRENT HOSTED STATUS: GitHub Actions has not run these worktree changes.

## Files Changed

- `research/FIXED_ORDER_CYCLE_RATIO.md` introduces only the unambiguous
  block-local notation and explicitly preserves the full-distance name.
- `research/ALL_N_LOWER_BOUND.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and
  `research/NEXT_RESEARCH_STEPS.md` synchronize that notation.
- `CURRENT_STATUS.md` and the existing STRICT task dossier record the new
  notation-only handoff.
- No production source, test, artifact, schema, example, or verifier changed.

## Residual Limitations

- The constant \(c_0\) is a certified lower constant, not the exact residual
  coefficient and not claimed optimal.
- Other linear densities and starting indices remain unclassified.
- The global and geometric coefficients are certified lower coefficients,
  not exact leading coefficients. Neither normalized sequence is proved to
  converge.
- The proof does not identify exact minimizing orders, exact angular optima,
  or a matching upper coefficient.
- No production-computation, artifact, schema, verifier, backend, or
  enumeration-limit claim follows.
- Finite tests verify arithmetic and bounded compatible histories only; they
  are not the all-\(n\) proof.
- Hosted GitHub Actions remain unverified.

## Proposed Next Task

After user review in a fresh chat, optimize the same block-local slack/prefix
certificate over its cutoff and averaging weight, determining the best
rigorously certified cubic lower constant available from that template or
proving the current parameters optimal within it.

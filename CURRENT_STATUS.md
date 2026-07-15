# CURRENT_STATUS - power-ringmin

Last update: 2026-07-15

- **Current phase:** exact one-wrap saturation of the fixed-order cyclic
  ratio.
- **Current task:** identify the one-wrap score with induced-subset cyclic
  product sums, decide saturation for every complete order, and add an exact
  Karp-independent bounded oracle.
- **Task dossier:**
  ops/TASK-20260715__one_wrap_cycle_ratio_saturation/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Exact Results

- DEFINITION: for a complete order \(\sigma\),
  \[
  \Lambda^{(1)}(\sigma)=\max\{S(C):q(C)=1\}.
  \]
  For a nonempty position subset
  \(T=\{i_0<\cdots<i_{m-1}\}\), let
  \[
  P_\sigma(T)=
  \sum_{r=0}^{m-1}\sigma_{i_r}\sigma_{i_{r+1\bmod m}}.
  \]
  A singleton contributes its square; a two-element subset contributes the
  same unordered product twice.
- EXACT THEOREM: a one-wrap closed walk is exactly the reverse orientation of
  an induced subset order of cardinality at least two. Since singleton scores
  cannot maximize for `n>=3`,
  \[
  \Lambda^{(1)}(\sigma)
  =\max_{|T|\ge2}P_\sigma(T)
  =\max_{T\ne\varnothing}P_\sigma(T).
  \]
- EXACT THEOREM (ALL-ORDER ONE-WRAP SATURATION): for every complete order and
  `n>=3`,
  \[
  \Lambda(\sigma)=\Lambda^{(1)}(\sigma).
  \]
  The complete induced cycle has score at least
  \(n(n+1)(n+2)/6\). Every vertex-simple cycle with `q>=2` has ratio at most
  \[
  {1\over2}\sum_{i=1}^n i^2
  ={n(n+1)(n+2)\over6}-{n(n+1)\over4},
  \]
  which is strictly smaller. Thus \(\Lambda(\sigma)\) and \(\Lambda_n\) are
  integers.
- LIMITATION: saturation concerns separable product weights. It does not
  reduce exact angular-STN feasibility or critical-cycle analysis to
  one-wrap cycles.

## Finite Exact Verification

- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): a test-only exact
  subset/path dynamic program computes the full simple-cycle ratio without
  using production descending closure, macro compression, or Karp's
  maximum-cycle-mean recurrence. It agrees with literal induced-subset
  maximization and production on all 2,956 canonical complete orders for
  `n=3..8`.
- VERIFIED FACT: the bounded values remain
  \[
  (\Lambda_3,\dots,\Lambda_8)=(12,26,47,77,118,172),
  \]
  with canonical minimizer counts `(1,3,4,15,24,84)`.
- VERIFIED FACT: production remains hard-bounded to `3<=n<=8` and at most
  2,520 canonical orders in one row. The oracle exists only in tests.
- INTERPRETATION: the finite sweep verifies the implementation; it is not the
  proof of all-order saturation, an all-`n` formula for \(\Lambda_n\), or a
  geometric result.

## Changes

- `research/FIXED_ORDER_CYCLE_RATIO.md` now contains the authoritative
  induced-subset equivalence, saturation proof, integer consequence,
  independent-oracle description, and exact-angular non-consequence.
- `tests/test_fixed_order_cycle_ratio.py` adds literal subset and independent
  subset/path oracles, exhaustive `n=3..8` agreement, and explicit
  two-element multiplicity coverage.
- The production scorer implementation and enumeration limits are unchanged;
  only its docstrings record the proved integer result.
- Project brief, durable knowledge, fixed-order source note, research roadmap,
  current status, and this task dossier are synchronized.
- No interval backend, verifier, certificate, checked artifact, example,
  schema, CLI, product-distance implementation, or production enumeration
  limit changed.

## Verification

- CURRENT LOCAL VERIFIED FACT: the focused cycle-ratio module passes all 23
  tests, including the exhaustive independent oracle over 2,956 orders.
- CURRENT LOCAL VERIFIED FACT: the complete repository suite passes all 196
  tests on local Python 3.14.3.
- CURRENT LOCAL VERIFIED FACT: checked-artifact semantic verification accepts
  4 certificates, 76 local brackets, and the `n=3..6` summary.
- CURRENT LOCAL VERIFIED FACT: targeted Ruff, Python compilation, and Git diff
  whitespace checks pass.
- CURRENT LOCAL VERIFIED FACT: independent mathematical, oracle,
  implementation, and classification reviews accept the proof, tests,
  bounded-domain guard, and finite/all-order separation after correcting two
  notation collisions and one closed-walk wording ambiguity.
- CURRENT HOSTED STATUS: GitHub Actions on Python 3.11-3.13 has not been run
  for this worktree.

## Residual Limitations

- Local execution used Python 3.14.3; Python 3.11 compatibility of the new
  test-only syntax was inspected but not locally executed.
- Repository-wide Ruff retains four known pre-existing F401/F841 findings in
  three untouched files; task-scoped Ruff is clean.
- The theorem gives no formula for \(\Lambda_n\), exact geometric optimum,
  improvement of the additive-\(n^2\) sandwich, new geometric coefficient, or
  asymptotic convergence result.
- The production Karp scorer remains useful as the independently cross-checked
  full-ratio implementation; no production rewrite was attempted.

## Proposed Next Task

In a fresh chat, design a bounded independent interval-backend
cross-verification path for the existing checked artifacts, without generating
a larger finite certificate or changing current certified claims.

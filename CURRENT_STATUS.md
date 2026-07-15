# CURRENT_STATUS - power-ringmin

Last update: 2026-07-15

- **Current phase:** exact elimination of index `1` from the cyclic-ratio
  objective.
- **Current task:** prove the insertion-independent core reduction, derive its
  global, product-distance, and geometric consequences, and verify every
  bounded core order and insertion.
- **Task dossier:**
  ops/TASK-20260715__index_one_elimination/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Exact Results

- DEFINITION: for a cyclic core order \(\tau\) of \(\{2,\ldots,n\}\),
  \[
  K(\tau)=
  \max_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P_\tau(U),
  \]
  where a singleton contributes \(j^2\) and a two-element subset contributes
  \(2ij\).
- EXACT THEOREM (INDEX-ONE ELIMINATION): if deleting label \(1\) from a
  complete order \(\sigma\) gives \(\tau\), then
  \[
  \Lambda(\sigma)=K(\tau),
  \]
  independently of the insertion gap. Subsets avoiding \(1\) retain their
  score; \(\{1\}\) gives \(1<4\); \(\{1,j\}\) gives \(2j\le j^2\); and
  deleting \(1\) from a subset with distinct core neighbors \(a,b\) raises
  its score by \(ab-a-b\ge1\). No maximizing subset contains \(1\).
- EXACT THEOREM: deletion/insertion is surjective on cyclic-order spaces, so
  \[
  \Lambda_n=\min_\tau K(\tau).
  \]
  The same-order comparison gives
  \[
  K(\tau)\le\Lambda_{\rm same}(\tau)\le(n-1)W(\tau),
  \qquad
  \Lambda_n\le(n-1)W_n.
  \]
- EXACT THEOREM (GEOMETRIC CONSEQUENCE): for every `n>=3`,
  \[
  R_2^*(n)<{\Lambda_n\over\pi}
  \le{(n-1)W_n\over\pi}.
  \]
  This proof does not use radius-one insertion or a regular-direction
  construction. It gives an upper bound, not an exact optimum.
- LIMITATION: insertion independence concerns \(\Lambda\), not
  \(\rho_\sigma\), exact fixed-order feasibility, or feasible-radius sets.

## Finite Exact Verification

- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): for `n=3..8`, every
  canonical core order and every cyclic insertion gap satisfies the reduction
  under literal subset scoring and the production scorer.
- The exact row counts are:

  | `n` | Core classes | Insertions | Complete classes | Minimum | Core minimizers | Complete minimizers |
  |---:|---:|---:|---:|---:|---:|---:|
  | 3 | 1 | 2 | 1 | 12 | 1 | 1 |
  | 4 | 1 | 3 | 3 | 26 | 1 | 3 |
  | 5 | 3 | 12 | 12 | 47 | 1 | 4 |
  | 6 | 12 | 60 | 60 | 77 | 3 | 15 |
  | 7 | 60 | 360 | 360 | 118 | 4 | 24 |
  | 8 | 360 | 2,520 | 2,520 | 172 | 12 | 84 |

- Totals are 437 core classes, 2,957 insertion trials, and 2,956 distinct
  complete classes. At `n=3`, insertions `(3,1,2)` and `(3,2,1)` are
  reflections and canonicalize to the same class; both have value `12`.
- INTERPRETATION: the finite sweep verifies the implementation and counts. It
  is not the proof of the all-order reduction or a geometric certificate.

## Changes

- `research/FIXED_ORDER_CYCLE_RATIO.md` now contains the exact three-case
  elimination proof, reduced minimum, same-order comparison, all-`n`
  geometric upper bound, explicit `n=3` treatment, and bounded table.
- `tests/test_fixed_order_cycle_ratio.py` adds test-only core insertion and
  canonical-coverage checks; production code and limits are unchanged.
- Project brief, durable knowledge, roadmap, current status, and this task
  dossier are synchronized.
- No backend, verifier, certificate, checked artifact, schema, example, CLI,
  product-distance implementation, production scorer, or certification claim
  changed.

## Verification

- CURRENT LOCAL VERIFIED FACT: the focused cycle-ratio module passes all 25
  tests, including 437 core classes and 2,957 insertion trials.
- CURRENT LOCAL VERIFIED FACT: the complete repository suite passes all 198
  tests on local Python 3.14.3.
- CURRENT LOCAL VERIFIED FACT: checked-artifact semantic verification accepts
  4 certificates, 76 local brackets, and the `n=3..6` summary; no backend,
  artifact, or certification claim changed.
- CURRENT LOCAL VERIFIED FACT: targeted Ruff, Python compilation, final Git
  diff inspection, and whitespace hygiene pass.
- CURRENT LOCAL VERIFIED FACT: independent mathematical, test, and
  documentation audits accept the theorem, strictness boundaries, exact
  values, minimizer counts, bounded-domain guard, and evidence
  classifications after five wording/status refinements.
- CURRENT HOSTED STATUS: GitHub Actions on Python 3.11-3.13 has not been run
  for this worktree.

## Residual Limitations

- The reduction gives an exact core optimization, not a closed form for
  \(\Lambda_n\) or a structural classification of its minimizers.
- The pointwise/global comparison with \(W\) is one-sided and non-strict;
  equality holds at `n=3`, and no all-`n` strictness is claimed.
- The geometric consequence recovers the known \(8/(25\pi)\) limsup
  coefficient; it does not prove convergence or a matching lower coefficient.
- Existing interval-backend trust limitations and certified finite claims are
  unchanged.
- Local execution used Python 3.14.3; Python 3.11 compatibility of the new
  test-only code was independently source-inspected but not locally executed.

## Proposed Next Task

In a fresh chat, design a bounded independent interval-backend
cross-verification path for the existing checked artifacts, without generating
a larger finite certificate or changing current certified claims.

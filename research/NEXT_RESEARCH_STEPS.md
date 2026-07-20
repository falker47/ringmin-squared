# Next Research Steps

Last reviewed: 2026-07-20

This file is the roadmap and priority source only. Stable result summaries
belong in [PROJECT_KNOWLEDGE.md](../PROJECT_KNOWLEDGE.md), detailed proofs in
the other research notes, and task evidence in ops/.

## Completed Milestones

- **COMPLETED -- PGE5 support:** on the canonical even-\(v\), \(e=5\)
  scaffold \(n=10m+4\), \(m\ge2\), the exact local relation, extendible
  support, Ferrers reduction, and equivalence between local compatibility and
  \(W=W_n\) are closed by PGE5-1--PGE5-26. The result evaluates \(W\), not
  \(K\) or the geometry. See the
  [authoritative proof](PRODUCT_DISTANCE_SURROGATE.md#the-canonical-even-v-e5-path-to-gap-support)
  and the [stable synopsis](../PROJECT_KNOWLEDGE.md#product-distance-surrogate).

The superficially similar Ferrers count and monotone threshold-closing
\(K\)-theorem already in the repository concern the earlier
\(n=10m+3\), \(e=4\) scaffold; they were not used as the PGE5 theorem.

- **COMPLETED -- fixed PGE5 interval-shift \(K\):** on the distinct
  \(n=10m+4\), \(m\ge2\) scaffold, (KPGE5-1)--(KPGE5-30) evaluate only
  \(\alpha_{q,2m-1}\), \(q=\lfloor(4m+3)/5\rfloor\). The sole maximizing
  subset is \(\{4m+1,\ldots,10m+4\}\), all five residue branches and the
  literal \(m=2\) row are exact, and the score is strictly below canonical
  K825 on every same-subsequence row while retaining cubic coefficient
  \(143/500\). The theorem makes no statement about another supported
  bijection, the permanent, geometry, or global optimality. See the
  [authoritative proof](FIXED_ORDER_CYCLE_RATIO.md#20-exact-k-for-the-fixed-pge5-interval-shift)
  and the [stable synopsis](../PROJECT_KNOWLEDGE.md#product-distance-surrogate).

- **COMPLETED -- PGE5 singleton-reversal \(K\):** on the same
  \(n=10m+4\), \(m\ge2\) scaffold, (KRPGE5-1)--(KRPGE5-36) evaluate only
  the map that keeps the interval shift through the doubleton, reverses the
  complete singleton block, and puts \(P_q\) in the closing gap. The map is
  supported and has \(W=W_n\); its sole induced-\(K\) maximizing subset is
  \(\{4m+1,\ldots,10m+4\}\). Exact cancellation confirms
  \(K_\uparrow-K_*=(m-1)(m-2)(m-3)/3\), the fixed-family coefficient
  \(857/3000\), and strict pointwise improvement over K825. This milestone
  changes no production or test file. Exact label-one elimination and the
  fixed-order sandwich give \(\Lambda=K_*\) and strict bounds on \(\rho\)
  for every insertion gap, plus
  \(R_2^*(10m+4)<K_*/\pi\) and the subsequential upper coefficient
  \(857/(3000\pi)\). It proves no optimality, matching global lower bound,
  all-\(n\) limsup bound, or exact leading constant for the global optimum
  \(R_2^*\). See the
  [authoritative proof](FIXED_ORDER_CYCLE_RATIO.md#21-exact-k-for-the-pge5-singleton-reversal-shift)
  and the [stable synopsis](../PROJECT_KNOWLEDGE.md#product-distance-surrogate).

## Completed Post-Review Closure

- **COMPLETED -- KRPGE5 state and provenance:** commit
  `a15a4d34cc034b669f02382e2e4f27b4822ed382` is the accepted
  KRPGE5-1--KRPGE5-36 baseline. On its clean tree, the standalone diagnostic,
  full pytest, checked-artifact verifier, focused schema suite, and repository
  hygiene checks passed. GitHub Actions `Verification` run `29777676234`
  succeeded for that exact SHA on Python 3.11--3.13. The earlier successful
  run on `bce6e4d8a935bd9d8509e59b760cf78c345779b6` was not reused. This
  closure changes no proof, construction, production code, test, artifact,
  or mathematical classification.

## Next Atomic Task

No mathematical successor is selected by this state/provenance closure.
Choose exactly one item from the deferred directions below in a fresh task
before developing further mathematics.

## Deferred, Not Prioritized

All open directions remain deferred until one is selected as a fresh bounded
task. They include the filtered cubic-convergent obstruction,
finer Ferrers-count residuals, the asymptotic coefficient gap, tighter finite
brackets at \(n=5,6\), the radius-one threshold below \(12\), and later
minimizer-set restrictions for \(n\ge94\). Their mathematical context remains
in the relevant proof notes and stable knowledge; this roadmap does not repeat
it.

Large exhaustive certificates, production enumeration-limit increases, and
claims of an exact geometric asymptotic constant remain deliberately
deferred.

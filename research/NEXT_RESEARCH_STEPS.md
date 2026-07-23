# Next Research Steps

Last reviewed: 2026-07-23

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

- **COMPLETED -- odd-\(v\) PGE5 support:** on the canonical \(e=5\)
  scaffold \(n=10m+9\), \(m\ge1\), PGE5ODD-1--PGE5ODD-26 close the exact
  path decomposition, literal local relation including the genuine cyclic
  column, Hall-extendible and full-threshold supports, four distance classes,
  and equivalence between local compatibility and \(W=W_n\).  There is no
  odd-parity completion obstruction; only the unreduced full support is
  non-Ferrers.  The result evaluates \(W\), not \(K\) or geometry.  See the
  [authoritative proof](PRODUCT_DISTANCE_SURROGATE.md#the-canonical-odd-v-e5-path-to-gap-support)
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

- **COMPLETED -- canonical odd-\(v\), \(e=5\) exact \(K\):** on the
  \(n=10m+9\), \(m\ge1\) scaffold, (KRPGE5ODD-1)--(KRPGE5ODD-40)
  evaluate only the fixed map that shifts the remaining triples, reverses
  the singleton block, and places \(P_q\),
  \(q=\lfloor(4m+5)/5\rfloor\), in the genuine closing gap. The map belongs
  to the exact PGE5ODD support and has \(W=W_n\). Its unique induced-subset
  maximizer is \(\{8,\ldots,19\}\) at \(m=1\), with \(K=2175\), and
  \(\{4m+3,\ldots,10m+9\}\) for every \(m\ge2\), with the exact requested
  polynomial. The stable polynomial misses the minimum row by precisely
  \(11\), because deleting \(7\) is strictly profitable there. Canonical
  K825 is strictly larger on every row, and the fixed-family coefficient is
  \(857/3000\). Exact label-one elimination supplies the fixed-order
  \(\Lambda\) value and angular sandwich; globally only the one-sided
  subsequential upper bounds for \(\Lambda_n\) and \(R_2^*(n)\) follow.
  Production, public tests, schemas, and artifacts are unchanged. See the
  [authoritative proof](FIXED_ORDER_CYCLE_RATIO.md#22-exact-k-for-the-canonical-odd-v-e5-map)
  and the [stable synopsis](../PROJECT_KNOWLEDGE.md#product-distance-surrogate).

- **COMPLETED -- monotone all-index KR1 lift:** for
  \[
  N(n)=5\left\lceil{n-1\over5}\right\rceil+1,
  \qquad 0\le N(n)-n\le4,
  \]
  cancelling labels above \(n\) from a complete KR1 order at \(N(n)\)
  preserves every remaining induced-subset score. The original KR1 domain
  therefore gives, for every \(n\ge7\),
  \(\Lambda_n\le K_{\rm R1}(N(n))\) and
  \(R_2^*(n)<K_{\rm R1}(N(n))/\pi\). Consequently the all-index limsup
  upper coefficients are \(857/3000\) and \(857/(3000\pi)\). The result
  introduces no new order family or finite-prefix extension and proves no
  optimality, convergence, or exact leading constant. See the
  [authoritative proof](FIXED_ORDER_CYCLE_RATIO.md#monotone-cancellation-lift-to-every-sufficiently-large-index)
  and the
  [task evidence](../ops/TASK-20260721__kr1_monotone_lift/EVIDENCE.md).

- **COMPLETED -- two-contiguous-block charging ansatz:** the separator-density
  construction, convex bridge, two history-relative disjoint original-edge
  slack pools, and global recursive child-edge invariant give the exact
  finite inequality (CR28dw34). Its normalized objective (CR28dw35)
  concatenates with one ordinary finite-prefix row of the same total length;
  the inverse holds on strict rows and the compact closures coincide.
  Consequently its fixed-length optimum is \(C_{K,*}\), and
  the exact unattained supremum over all finite nonempty two-block rows is
  \(C_{\mathrm{AF}}=(434+4\sqrt2)/1587\). Thus this ansatz cannot improve the
  current lower coefficient. See the
  [authoritative proof](FIXED_ORDER_CYCLE_RATIO.md#two-contiguous-blocks-separated-by-one-density)
  and the
  [task evidence](../ops/TASK-20260721__two_block_finite_prefix/EVIDENCE.md).

- **COMPLETED -- one-prefix base-capacity filter:** retaining only the
  base/recursive split type and the capacity \(n-r+1\) of the original base
  cycle forces at least \([2r-s-n-1]_+\) selected recursive splits.  This
  gives the new exact all-order inequality (CR28dw41) and normalized compact
  objective (CR28dw43).  The active-side compact closure has exact maximum
  \(13/48\) at its filter-off hinge; after every boundary and the hinge
  \(\beta=2\alpha-1\) are included, the whole class has the old one-prefix
  maximum
  \[
  {4+2\sqrt3\over27}
  <{434+4\sqrt2\over1587}=C_{\mathrm{AF}}.
  \]
  Thus this binary filter is an exact no-go for improving the current lower
  coefficient within the declared one-prefix class.  It does not classify
  broader structural filters or upper-bound \(\Lambda_n\).  See the
  [authoritative proof](FIXED_ORDER_CYCLE_RATIO.md#one-prefix-base-capacity-filter)
  and the
  [task evidence](../ops/TASK-20260721__base_recursive_capacity_filter/EVIDENCE.md).

- **COMPLETED -- one-prefix label-aware capacity refinement:** retaining
  every selected-label base floor gives
  \(\sum_{t=s}^{r-1}G(t)\), and the capacity count adds the \(\nu\) smallest
  exact advantages \(J(t)-G(t)\).  This is the strongest bound from the
  cardinality datum alone.  Literal binary histories are stronger by one
  label shift because the first selected split is necessarily base; the two
  bounds differ by \(O(n^2)\) and share one exact cubic limit.  Complete
  compact optimization, including the positive-part hinge and all
  collisions, gives a unique inactive maximizer with
  \[
  0.2768854<C_{\rm LA,*}<0.2768855
  <{434+4\sqrt2\over1587}=C_{\rm AF}.
  \]
  It strictly improves the old one-prefix coefficient but does not exceed
  the all-fixed-prefix coefficient.  This is a method-specific limitation,
  not a global or geometric upper bound.  See the
  [authoritative proof](FIXED_ORDER_CYCLE_RATIO.md#one-prefix-label-aware-base-capacity)
  and the
  [task evidence](../ops/TASK-20260722__one_prefix_label_aware_capacity/EVIDENCE.md).

- **COMPLETED -- PG49/KPGZERO filtered-cardinality support no-go:** the
  per-row filtered convergent/scale fibre is now defined literally and proved
  bijective with the descending-min zero set, giving the exact
  power-of-two induced-\(K\) argmax count. The corresponding PG49-supported
  family is infinite exactly when the filtered cubic-convergent set is
  infinite. Every primitive direction has only finitely many admitted
  scales, and two supported bijections on the same exact PG49 board have
  different induced-\(K\) maximizer cardinalities. Hence fixed-direction
  rescaling cannot produce an infinite filtered family, and the bare
  supportedness predicate with \(W=T\) cannot replace the induced-\(K\)
  filter. An infinite conic/support ray is proved to fail both literal
  plateau residuals. This is an exact support-only no-go, not a proof that
  the remaining arithmetic set is finite, and it makes no geometric claim.
  See the
  [authoritative proof](FIXED_ORDER_CYCLE_RATIO.md#filtered-cardinality-on-the-pg49-support)
  and the
  [task evidence](../ops/TASK-20260723__pg49_kpgzero_filtered_cardinality/EVIDENCE.md).

## Completed Post-Review Audit

- **COMPLETED -- independent KRPGE5 audit:** KRPGE5-1--KRPGE5-36 at
  accepted baseline `a15a4d34cc034b669f02382e2e4f27b4822ed382` were
  rederived against the PGE5 scaffold and CR12p/CR22/CR27/CR28a, without
  using dossier formulas as oracle values. Support, every deletion and
  shortcut class including the cyclic cut, the block sum, all five residue
  classes, the singleton cancellation, the K825 subtraction, and the exact
  closure all passed. Fresh local diagnostics and repository suites passed,
  and the available GitHub Actions matrix was inspected at that exact SHA
  without reusing an ancestor run. No audit criterion remains open, and no
  proof, construction, production code, test, schema, artifact, or workflow
  changed. See
  [EV-001](../ops/TASK-20260721__krpge5_post_review_audit/EVIDENCE.md#ev-001---independent-krpge5-post-review-audit).

## Next Atomic Task

User review and manual commit decision for the PG49/KPGZERO
filtered-cardinality support no-go. Afterward, choose exactly one item from
the deferred directions below in a fresh task before developing further
mathematics.

## Deferred, Not Prioritized

All open directions remain deferred until one is selected as a fresh bounded
task. They include the absolute finiteness/infinitude of the PG49/KPGZERO
filtered cubic-convergent set after the support-only no-go,
finer Ferrers-count residuals, the asymptotic coefficient gap, tighter finite
brackets at \(n=5,6\), the radius-one threshold below \(12\), and later
minimizer-set restrictions for \(n\ge94\). Their mathematical context remains
in the relevant proof notes and stable knowledge; this roadmap does not repeat
it.

Large exhaustive certificates, production enumeration-limit increases, and
claims of an exact geometric asymptotic constant remain deliberately
deferred.

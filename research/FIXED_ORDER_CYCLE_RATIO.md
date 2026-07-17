# Fixed-Order Maximum Cyclic Ratio

Date: 2026-07-14

Last updated: 2026-07-17

## Scope And Classification

This note formalizes the exact combinatorial cycle ratio associated with the
complete fixed-order angular STN. It uses the real-arithmetic semantics proved
in `research/FIXED_ORDER_ANGULAR_STN.md` and the two angular comparisons proved
in `research/ALL_N_LOWER_BOUND.md`.

- **DEFINITION:** for a complete cyclic order \(\sigma\) of
  \(\{1,\ldots,n\}\), \(q(C)\) counts `wrap_upper` edge occurrences and
  \(S(C)\) sums endpoint-index products over all directed edge occurrences,
  with multiplicity.
- **EXACT THEOREM:** the one-wrap score
  \(\Lambda^{(1)}(\sigma)=\max_{q(C)=1}S(C)\) is exactly the maximum cyclic
  adjacent-product sum over orders induced on subsets of at least two
  positions. For two positions, the same unordered product occurs twice.
- **EXACT THEOREM:** every complete order is one-wrap saturated:
  \(\Lambda(\sigma)=\Lambda^{(1)}(\sigma)\). In fact, every vertex-simple
  cycle with at least two wraps has strictly smaller ratio. Thus the fixed-
  order and global scores are integers, although the implementation retains
  its exact `Fraction` return type.
- **EXACT THEOREM:** if \(\tau\) is obtained from \(\sigma\) by deleting
  label \(1\), and \(K(\tau)\) is the maximum induced cyclic product sum over
  nonempty core subsets, then
  \(\Lambda(\sigma)=K(\tau)\), independently of the insertion gap of label
  \(1\). Consequently \(\Lambda_n=\min_\tau K(\tau)\).
- **EXACT THEOREM:** the accepted same-order comparison gives
  \(\Lambda_n\le(n-1)W_n\). Combined with the strict cyclic-ratio sandwich,
  this yields
  \[
  R_2^*(n)<{\Lambda_n\over\pi}
  \le{(n-1)W_n\over\pi}
  \qquad(n\ge3).
  \]
- **EXACT THEOREM:** the maximum ratio \(\Lambda(\sigma)\) gives the requested
  fixed-order sandwich
  \[
  {\Lambda(\sigma)\over\pi}-n^2
  \le \rho_\sigma
  \le {\Lambda(\sigma)\over\pi}.
  \]
  On the stated domain, both inequalities are in fact strict.
- **EXACT THEOREM:** minimizing over the finite complete-order space gives the
  analogous global sandwich for \(\Lambda_n\) and \(R_2^*(n)\).
- **EXACT THEOREM (TWO NESTED TAILS):** for \(n\ge4\),
  \(1\le m\le n-3\), and \(S_m=\{m,\ldots,n\}\), deleting \(m\) from the
  induced cycle gives a
  simple cycle \(C\) on \(S_{m+1}\) and a distinguished edge
  \(\{a,b\}\), with exact correction
  \(m(a+b)-ab=m^2-(a-m)(b-m)\). The resulting quantity
  \(\beta_{m,n}\) defined below is the strongest universal lower obstruction
  that uses only the two scores on \(S_m,S_{m+1}\).
- **EXACT METHOD-SPECIFIC LIMITATION:** after imposing the full simple-cycle
  conditions on duplicated-pairing signatures and optimizing over \(m\),
  \[
  \beta_n^{(2)}
  ={2(\sqrt2-1)\over3}n^3+O(n^2).
  \]
  Thus the two-tail refinement can strengthen finite terms but does not
  improve the leading coefficient \(2(\sqrt2-1)/3\). This does not determine
  the leading behavior of \(\Lambda_n\) or exclude arguments coupling many
  tails simultaneously.
- **EXACT THEOREM (THREE NESTED TAILS):** for \(n\ge5\) and
  \(1\le m\le n-4\), deleting \(m\) and then \(m+1\) identifies a simple
  base cycle on \(S_{m+2}\) and two compatible edge splits. If their exact
  corrections are \(A\) and \(B\), the three-tail maximum is the base score
  plus \(\max(0,A,A+B)\). The second split is either nested in the first
  split edge or uses a distinct incident/disjoint base edge; these are all
  possibilities.
- **EXACT METHOD-SPECIFIC LIMITATION (THREE TAILS):** writing
  \(P^*_{m+2,n}\) for the minimum simple-cycle score on \(S_{m+2}\), the
  exact obstruction satisfies, uniformly,
  \[
  0\le\gamma^*_{m,n}-P^*_{m+2,n}<2n^2.
  \]
  The same comparison holds with the established duplicated-pairing floor
  \(P_{m+2,n}\). Consequently the optimized three-tail obstruction still has
  cubic coefficient \(2(\sqrt2-1)/3\). This is not an asymptotic evaluation
  of \(\Lambda_n\) or \(R_2^*(n)\).
- **VERIFIED FACT (FINITE EXACT TEST-ONLY CHECK):** compatible double splits
  give every outer simple cycle at \((m,n)=(2,7)\), with exact interaction
  counts 24 nested, 24 distinct-incident, and 12 distinct-disjoint. Four
  bounded rows check the pairing floor, exact base minimum, and three-tail
  obstruction without calling production scoring or enumeration.
- **EXACT THEOREM (ARBITRARY NESTED-TAIL BLOCK):** for
  \(2\le r\le n-2\) and \(1\le m\le n-r-1\), every cycle on
  \(S_m\) is uniquely a simple base cycle on \(S_{m+r-1}\) followed by
  \(r-1\) compatible descending edge splits. If the successive exact
  corrections are \(A_1,\ldots,A_{r-1}\), the block maximum is the base
  score plus
  \[
  \max_{0\le j\le r-1}\sum_{i=1}^j A_i.
  \]
  Every intermediate signature and every literal split linkage is part of
  the parametrization. Recursively nested child-edge splits cannot in
  general be replaced by distinct base edges.
- **EXACT METHOD-SPECIFIC LIMITATION (ARBITRARY BLOCK):** if
  \(P^*_{m+r-1,n}\) is the exact minimum inner simple-cycle score, then
  uniformly in all three parameters,
  \[
  0\le\gamma^{(r)}_{m,n}-P^*_{m+r-1,n}
  \le\sum_{t=m}^{m+r-2}[t^2-2]_+
  <(r-1)n^2.
  \]
  Including the alternating-cycle excess gives the pairing-floor comparison
  \(P_{m+r-1,n}\le\gamma^{(r)}_{m,n}<P_{m+r-1,n}+rn^2\).
  Consequently every fixed \(r\), and more generally every
  \(r=r(n)=o(n)\), preserves the coefficient
  \(2(\sqrt2-1)/3\) for this separately optimized one-block obstruction.
  Linear \(r=\Theta(n)\) is the first scale this error bound does not
  exclude from changing the coefficient; that is not evidence that it does.
- **EXACT METHOD-SPECIFIC THEOREM (JOINTLY OPTIMIZED ONE-PREFIX LINEAR
  BLOCK):** for
  \(m=1\), \(r_n=\lfloor\alpha n\rfloor\),
  \(s_n=\lceil\beta n\rceil\), and prefix weight \(\lambda\), the exact
  proof-valid region is
  \[
  0<\alpha<1,
  \qquad 0<\beta<\alpha,
  \qquad 0\le\lambda\le1.
  \]
  The pairing floor plus certified residual has cubic coefficient
  \[
  \mathcal C(\alpha,\beta,\lambda)
  ={(1-\alpha)(\alpha^2+4\alpha+1)\over6}
  +(\alpha-\beta)
  {\lambda\left(4(1+\alpha)\beta-(1+\alpha)^2
  -2\lambda\beta^2\right)\over2(2-\lambda)}.
  \]
  Complete exact boundary analysis proves the unique global maximizer
  \[
  \alpha_*=1-{\sqrt3\over3},
  \qquad
  \beta_*={5\over6}-{\sqrt3\over4},
  \qquad
  \lambda_*={88-32\sqrt3\over73},
  \]
  with associated residual contribution \((26-15\sqrt3)/54\) and total coefficient
  \[
  \mathcal C_*={4+2\sqrt3\over27}.
  \]
  The exact floor/ceiling certificate is uniformly admissible for
  \(n\ge86\). For \(n\ge90\), it gives
  \[
  \gamma^{(r_n^*)}_{1,n}-P^*_{r_n^*,n}
  \ge {26-15\sqrt3\over54}n^3
  -{233-128\sqrt3\over72}n^2
  \]
  and
  \[
  \Lambda_n\ge {4+2\sqrt3\over27}n^3,
  \qquad
  R_2^*(n)>{4+2\sqrt3\over27\pi}n^3-n^2.
  \]
  These are rigorous method-specific lower coefficients, not exact residual
  or leading coefficients; neither convergence nor production computation
  follows. The one-tail and sublinear-block coefficient
  \(2(\sqrt2-1)/3\) remains unchanged and logically separate.
- **EXACT METHOD-SPECIFIC THEOREM (TWO SELECTED PREFIXES):** for
  \(0<\beta_2<\beta_1<\alpha<1\) and
  \(0\le\lambda_{\rm lo}\le\lambda_{\rm hi}\le1\), combining the two
  prefix heights before charging proves
  \[
  C_2=p(\alpha)
  +(\alpha-\beta_1)g(\alpha,\beta_1,\lambda_{\rm hi})
  +(\beta_1-\beta_2)g(\alpha,\beta_2,\lambda_{\rm lo}).
  \]
  Every original base edge is charged at most once across both segments, and
  every recursively nested child edge retains the local recursive floor.
  Exact reduction of the ordered weights and complete branch/boundary
  analysis give the unique global maximizer
  \[
  \alpha_*={629-23\sqrt{143}\over829},
  \quad
  \beta_{1,*}={2286-77\sqrt{143}\over3316},
  \quad
  \beta_{2,*}={2010-59\sqrt{143}\over3316},
  \]
  \[
  \lambda_{{\rm hi},*}={6264-288\sqrt{143}\over5281},
  \qquad
  \lambda_{{\rm lo},*}={3888-192\sqrt{143}\over4273},
  \]
  with exact coefficient
  \[
  C_{2,*}={491596+6578\sqrt{143}\over2061723}.
  \]
  Consequently
  \[
  \liminf{\Lambda_n\over n^3}\ge C_{2,*},
  \qquad
  \liminf{R_2^*(n)\over n^3}\ge{C_{2,*}\over\pi}.
  \]
  Separately, the exact rational witness
  \[
  (\alpha,\beta_1,\beta_2,\lambda_{\rm hi},\lambda_{\rm lo})
  =(3/7,2/5,3/8,1/2,1/4)
  \]
  gives
  \[
  C_2={72825421\over263424000}>{4+2\sqrt3\over27}.
  \]
  Its floor/ceiling theorem is uniformly admissible from the minimal threshold
  \(n=59\), and
  \[
  \Lambda_n\ge {72825421\over263424000}n^3,
  \qquad
  R_2^*(n)>{72825421\over263424000\pi}n^3-n^2
  \quad(n\ge59).
  \]
  This rational specialization remains the previous explicit finite
  two-prefix theorem; no finite rounding of the irrational *two-prefix*
  optimizer is asserted. The optimized number is still a method-specific
  lower coefficient, not an exact leading coefficient, convergence theorem,
  or production result.
- **EXACT FINITE METHOD-SPECIFIC THEOREM (THREE SELECTED PREFIXES):** the
  unique irrational three-prefix optimizer admits exact integer cutoffs
  \(r_n=\lfloor\alpha_*n\rfloor\) and
  \(s_{i,n}=\lceil\beta_{i,*}n\rceil\). From the minimal uniform threshold
  \(n=159\), they are strictly ordered, all three segments are nonempty, and
  every cutoff lies in its finite middle clipped branch. The finite clipped
  weights give the literal charging expression \(\mathcal B_{3,n}\) in
  (CR28cq7). Its integer closure
  \(\mathcal I_{3,n}=\lceil\mathcal B_{3,n}\rceil\) satisfies
  \[
  \Lambda_n\ge\mathcal I_{3,n}\ge\mathcal B_{3,n}>C_{3,*}n^3,
  \qquad
  R_2^*(n)>{\mathcal I_{3,n}\over\pi}-n^2
  \quad(n\ge159).
  \]
  The controlled polynomial remainder is (CR28cq12)--(CR28cq13). The
  threshold is minimal because the first segment is empty at \(n=158\).
  This finite theorem does not identify an exact residual or leading
  coefficient and does not extend charging to four prefixes.
- **EXACT METHOD-SPECIFIC THEOREM (FOUR SELECTED PREFIXES):** for strictly
  ordered cutoffs and ordered weights
  \(0\le\lambda_4\le\lambda_3\le\lambda_2\le\lambda_1\le1\), the five
  coefficients
  \(1-\lambda_1,\lambda_1-\lambda_2,\lambda_2-\lambda_3,
  \lambda_3-\lambda_4,\lambda_4\) combine the four selected heights before
  any slack is assigned. The resulting four split segments use one canonical
  partition of the original-edge slack, while the recursive invariant covers
  every child edge through all three boundaries. Equations
  (CR28de)--(CR28dk) give the exact finite lower bound. The continuous
  coefficient is now optimized on the full compact closure in
  (CR28dl)--(CR28dq13). The ordered weights reduce independently, all fifteen
  clipping regimes and every transition/collision/facet are classified, and
  the unique strict `MMMM` maximizer gives
  \[
  C_{4,*}
  ={597580022071777213687318156
   +21288970076515705538\sqrt{2903456040383}
   \over2290468477489828247376833403}
  >C_{3,*}.
  \]
  Consequently
  \(\liminf\Lambda_n/n^3\ge C_{4,*}\) and
  \(\liminf R_2^*(n)/n^3\ge C_{4,*}/\pi\). No finite rounding theorem is
  asserted.
- **EXACT FINITE METHOD-SPECIFIC THEOREM (ARBITRARILY MANY FINITE SELECTED
  PREFIXES):** fix any integer \(k\ge1\), strictly ordered finite cutoffs, and
  \(0\le\lambda_k\le\cdots\le\lambda_1\le1\). With
  \(\lambda_{k+1}=0\), the \(k+1\) convex coefficients
  \(1-\lambda_1,\lambda_1-\lambda_2,\ldots,\lambda_k\) combine
  \(0,H_1,\ldots,H_k\) before any slack is assigned and telescope to \(k\)
  disjoint weighted segments. Every literal history canonically partitions
  the original edges into injectively charged and unused edges. A descending
  insertion induction, containing no frontier count, covers arbitrary nesting
  through every finite number of boundaries. Equations (CR28dr)--(CR28dw)
  prove
  \[
  \gamma^{(r)}_{1,n}\ge
  P_{r,n}+\sum_{i=1}^k(s_{i-1}-s_i)G_{n,\lambda_i}(s_i).
  \]
  This pointwise finite theorem gives no uniform asymptotic control for
  \(k=k(n)\), coefficient optimization, limiting-prefix passage, or geometric
  consequence.
- **EXACT THEOREM (NORMALIZED \(k\)-PREFIX SIMPLEX):** for every \(k\ge1\),
  the compact normalized polynomial (CR28cr) has one strictly interior
  maximizer. Its ratios satisfy
  \[
  r_k={2\over3},
  \qquad r_i={2\over3-r_{i+1}^2},
  \]
  and its exact values satisfy
  \[
  M_0=0,
  \qquad M_k={4\over27(1-M_{k-1})^2}.
  \]
  The sequence is strictly increasing and converges to \(1/3\). A global
  nonnegative telescoping certificate proves uniqueness, rather than only
  stationarity. The cases \(k=1,2,3,4\) recover exactly the optimized
  one- through four-prefix simplex data.
- **EXACT NORMALIZED-ENVELOPE CLASSIFICATION:** the formal limiting envelope
  \(p(\alpha)+(3\alpha-1)^3/24\) has unique compact-closure maximum
  \(1/3\) at the degenerate endpoint \(\alpha=1\); on \(\alpha<1\) this is
  only a supremum. Restricted to the limiting all-middle closure
  \([1/3,1/2]\), its unique maximum is
  \((434+4\sqrt2)/1587\) at
  \((13-2\sqrt2)/23\).
- **EXACT METHOD-SPECIFIC ASYMPTOTIC COROLLARY (EXPLICIT FIVE-PREFIX
  WITNESS):** specialize the exact \(k=5\) simplex at
  \(\alpha=13/30\), then use the separate arbitrary finite-prefix charging
  theorem. The resulting five cutoffs and weights are rational, strictly
  ordered, and all middle-clipped. Their complete coefficient is
  \[
  C_{5,\mathrm{rat}}
  ={2263404122555368590593580404287
   \over8177706222298165502582585481000}
  >C_{4,*}.
  \]
  Hence
  \(\liminf\Lambda_n/n^3\ge C_{5,\mathrm{rat}}\) and
  \(\liminf R_2^*(n)/n^3\ge C_{5,\mathrm{rat}}/\pi\). This is one explicit
  fixed-parameter witness, not the global \(k=5\) optimum.
- **EXACT FINITE METHOD-SPECIFIC THEOREM (FIXED RATIONAL FIVE-PREFIX
  WITNESS):** retain the same \(\alpha,x_i,\beta_i,\lambda_i\), put
  \(r_n=\lfloor13n/30\rfloor\) and
  \(s_{i,n}=\lceil\beta_i n\rceil\), and use the fixed-weight floors
  \(G_{n,\lambda_i}(s_{i,n})\). The minimal uniform threshold for complete
  block admissibility, five nonempty segments, strict cutoff order, and all
  five finite middle branches is \(n=234\); the first segment is empty at
  \(n=233\). Equations (CR28dz4)--(CR28dz19) define the literal
  \(\mathcal B_{5,n}\), its integer closure
  \(\mathcal I_{5,n}=\lceil\mathcal B_{5,n}\rceil\), and the exact rounded
  remainder. They prove
  \[
  \Lambda_n\ge\mathcal I_{5,n}\ge\mathcal B_{5,n}
  >C_{5,\mathrm{rat}}n^3
  \qquad(n\ge234).
  \]
  This keeps the fixed rational weights; it does not substitute the finite
  reoptimized clipped weights.
- **LIMITATION:** the normalized theorem by itself proves no charging
  statement. A separate direct argument proves one-use charging for every
  finite admissible \(k\), but supplies no threshold or error estimate uniform
  in a growing \(k=k(n)\), no interchange of \(k\) and \(n\), and no finite
  rounding at the optimized four-prefix point.
- **VERIFIED FACT (BOUNDED EXACT FOUR-PREFIX ORACLE):** a standalone
  Fraction oracle literally checks all 840 four-split histories from the
  bounded base \(C_0=(11,14,12,13)\). It imports no project or test helper and
  verifies the convex telescoping identity, canonical original-edge slack
  partition, recursive invariant, local floors, and four-segment lower bound,
  including 120 fourth splits whose two endpoints were inserted earlier.
  This bounded computation corroborates but does not replace the all-history
  proof.
- **VERIFIED FACT (BOUNDED EXACT FIVE-PREFIX ORACLE):** the standalone
  dossier oracle uses only standard-library `Fraction` arithmetic and
  exhausts all 15,120 literal five-split histories of the five-edge base
  \(C_0=(13,17,14,16,15)\), the minimum edge cardinality permitting five
  simultaneous original-edge charges. It includes 120 such all-five-base
  histories and 2,520 fifth splits between two earlier inserted labels, and
  checks exact linkage, the convex identity, canonical one-use slack, the
  recursive invariant, every local floor, and (CR28dw). This finite
  computation corroborates but does not replace the all-history proof.
- **VERIFIED FACT (BOUNDED EXACT SIX-PREFIX ORACLE):** the sole new
  dossier-local oracle exhausts all 332,640 six-split histories of
  \(C_0=(15,20,16,19,17,18)\). It includes 720 histories charging all six
  original edges and 60,480 sixth splits between two previously inserted
  labels. Exact standard-library arithmetic checks the indexed convex
  telescope, canonical one-use partition, recursive invariant, every local
  floor, and the \(k=6\) instance of (CR28dw). This finite corroboration
  introduces no production enumeration and is not the proof for arbitrary
  finite \(k\).
- **VERIFIED FACT (INDEPENDENT EXACT FOUR-PREFIX OPTIMIZATION DIAGNOSTIC):**
  a separate standard-library script checks the three exact clipping-gap
  factorizations on rational grids, both \(C^1\) joins, all fifteen regimes,
  exact transition weights and collision reductions, the specialized
  \(k=4\) simplex certificate, end-to-end evaluation of the original
  objective at the quadratic-surd optimizer, its primitive irreducible
  polynomial, isolating interval, and strict separator from \(C_{3,*}\). It
  imports no project, production, or test helper and does not replace the
  all-real compact proof.
- **VERIFIED FACT (INDEPENDENT EXACT FIVE-PREFIX RATIONAL DIAGNOSTIC):** the
  sole new standalone script uses only fractions.Fraction. It checks the
  \(q_5,M_5\) recurrences, direct simplex objective and stationarity, every
  reduced \(\beta_i,\lambda_i\), strict all-middle admissibility, equality of
  the direct and normalized coefficient formulas, and the two positive exact
  margins proving \(C_{5,\mathrm{rat}}>75/271>C_{4,*}\). It corroborates but
  does not replace the written algebra.
- **VERIFIED FACT (FINITE EXACT FIVE-PREFIX FLOOR/CEILING DIAGNOSTIC):** the
  sole new dossier script for the finite specialization uses only
  standard-library `Fraction` arithmetic. It checks the exact rows
  \(233\) through \(246\), every predicate's last boundary failure, the
  symbolic-tail margins, fixed-weight literal floors, integer closure,
  stationarity cancellations, exact remainder, and strict comparison. It
  imports no project or test helper and does not replace the written proof.
- **VERIFIED FACT (FINITE EXACT TEST-ONLY CHECK):** a recursive oracle at
  \((m,n,r)=(2,7,4)\) identifies all 60 compatible triple-split histories
  with all 60 outer dihedral cycles and obtains
  \((P_{5,7},P^*_{5,7},\gamma^{(4)}_{2,7})=(106,107,118)\).
  Separate bounded checks retain fully nested domino histories and verify the
  exact prefix envelope. No production scorer, canonicalizer, enumerator, or
  limit is changed.
- **VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION):** bounded canonical
  enumeration for \(n=3,\ldots,8\) gives
  \((12,26,47,77,118,172)\), with no counterexample to the supplied
  prediction.
- **VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION):** a test-only exact
  subset/path oracle, independent of the production macro graph and Karp
  recurrence, agrees with literal induced-subset maximization on all 2,956
  canonical orders for \(n=3,\ldots,8\). This regression is not the proof of
  the all-\(n\) theorem.
- **VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION):** a separate
  all-core/all-insertion regression checks 437 canonical core orders and all
  2,957 insertion gaps for \(n=3,\ldots,8\). It covers the same 2,956
  complete rotation/reflection classes; the extra trial is the explicit
  two-arc degeneracy at \(n=3\).
- **EXACT THEOREM (FINITE SIX-LABEL LEMMA):** for every cyclic order
  \(\omega\) on \(S_6=\{4,\ldots,9\}\), with
  \(S_5=\{5,\ldots,9\}\),
  \[
  \max\{P_\omega(S_6),P_\omega(S_5)\}\ge239.
  \]
  The proof uses a general rearrangement lower bound and only twelve explicit
  exceptional cyclic sums, rather than enumerating the 60 classes.
- **VERIFIED FACT (FINITE EXACT COMBINATORIAL RESULT):** the accepted core
  reduction, the six-label lemma, and the exact witness
  \(\tau=(9,2,3,5,8,6,7,4)\) give
  \(\Lambda_9=239\). The witness has the unique maximizing subset
  \(\{4,5,6,7,8,9\}\). This is a finite combinatorial value, not an exact
  geometric value or an all-\(n\) formula.
- **EXACT THEOREM (FINITE CORE MINIMIZER CLASSIFICATION):** equality in the
  six-label lemma forces the induced cycle `(9,5,8,6,7,4)` up to dihedral
  symmetry. Label `3` may be inserted in exactly the four gaps not incident
  to label `4`, after which label `2` may be inserted in any of the seven
  gaps. These are exactly 28 dihedral core minimizers. Exact label-one
  insertion gives exactly \(28\cdot8=224\) complete minimizer classes.
- **VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION):** an independent
  test-only oracle checks all \(7!/2=2{,}520\) dihedral core classes and all
  255 nonempty subsets of each, recording every maximizing subset. It finds
  exactly the 28 proved classes. A separate oracle checks the six-label lemma
  on all 60 dihedral classes. Neither check calls a repository canonicalizer,
  the public enumerator, or the production Karp scorer.
- **EXACT THEOREM (FINITE SEVEN-LABEL LEMMA):** for every cyclic order
  \(\omega\) on \(\{4,\ldots,10\}\),
  \[
  \max\{P_\omega(\{4,\ldots,10\}),P_\omega(\{5,\ldots,10\})\}\ge323.
  \]
  The proof applies the duplicated-multiset pairing relaxation to
  \(\{5,\ldots,10\}\), classifies exactly the eight pairing signatures at
  the only relevant integer levels 320--322, and then applies the exact
  correction for inserting label \(4\).
- **EXACT THEOREM (FINITE SEVEN-LABEL EQUALITY CLASSIFICATION):** equality in
  the preceding lemma holds in exactly two dihedral classes, represented by
  `(10,4,7,8,6,9,5)` and `(10,5,9,4,7,8,6)`. The proof treats separately
  tail scores 323 and 322. In the 323 branch, the insertion correction leaves
  four possible tail edges; fixed-edge pairing bounds eliminate two, and the
  exact residual equality signatures eliminate a third. Exactly one insertion
  gap survives in each score branch.
- **EXACT THEOREM (FINITE LABEL-THREE INSERTION-GAP CLASSIFICATION):** write
  \(K_{\ge3}\) for the maximum induced-subset score of a partial cycle on
  labels \(3,\ldots,10\). Inserting label \(3\) into
  `(10,4,7,8,6,9,5)` gives \(K_{\ge3}=323\) in every gap except
  \(\{4,7\}\), where it gives 326. Inserting label \(3\) into
  `(10,5,9,4,7,8,6)` gives \(K_{\ge3}=323\) except on
  \(\{4,9\}\) and \(\{4,7\}\), where it gives 326 and 328. The proof uses
  the exact insertion correction and a complete shortcut-gain certificate,
  not subset enumeration.
- **EXACT THEOREM (FINITE \(n=10\) CORE MINIMIZER CLASSIFICATION):** the
  eleven surviving label-three cycles have 88 labelled gaps for label \(2\).
  Using \(2(a+b)-ab=4-(a-2)(b-2)\), the recorded argmaxes, and the
  shortcut-gain pruning certificates, exactly 87 insertions have \(K=323\).
  The sole exception is (10,3,2,4,7,8,6,9,5), obtained by splitting the
  \(\{3,4\}\) gap of (10,3,4,7,8,6,9,5); it has \(K=325\). The 88
  candidates are distinct dihedral core classes, so there are exactly 87
  core minimizer classes. Exact label-one insertion then gives exactly
  \(87\cdot9=783\) complete minimizer classes.
- **VERIFIED FACT (FINITE EXACT COMBINATORIAL RESULT):** the seven-label
  lemma and the exact shortcut-gain witness
  \(\tau=(10,2,3,4,7,8,6,9,5)\) give
  \(\Lambda_{10}=323\). Exactly two witness subsets maximize: the six-label
  tail \(\{5,\ldots,10\}\) and the eight-label tail
  \(\{3,\ldots,10\}\).
- **VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION):** independent
  test-only code checks the lemma on all \(6!/2=360\) seven-label dihedral
  classes, literally scores all \(2^9-1=511\) nonempty witness subsets, and
  separately checks all 14 label-three insertions and all 255 nonempty
  subsets of each. A further independent oracle checks all 88 label-two
  insertions and all 511 nonempty subsets of each, recording every argmax and
  confirming 88 distinct core classes and 783 distinct label-one insertions.
  None of these paths calls a repository canonicalizer, the public enumerator,
  or the production scorer.
- **VERIFIED FACT:** `src/power_ringmin/fixed_order_cycle_ratio.py` implements
  a float-free exact scorer using descending-path compression and Karp's
  maximum-cycle-mean dynamic program. Direct simple-cycle enumeration is not
  used in production and exists only as an independent small-test oracle.
- **LIMITATION:** the exact `n=9` and `n=10` classifications are
  not a closed-form all-\(n\) evaluation or evidence for convergence to a
  new asymptotic constant. They are finite combinatorial classifications, not
  exact values or minimizer classifications for \(R_2^*(9)\) or
  \(R_2^*(10)\). No interval backend, verifier, interval-certificate artifact,
  checked artifact, schema, or example is changed by this work.

## 1. Complete Fixed-Order STN

Fix an integer \(n\ge3\) and a complete order
\[
\sigma=(\sigma_0,\ldots,\sigma_{n-1}),
\qquad
\{\sigma_0,\ldots,\sigma_{n-1}\}=\{1,\ldots,n\}.
\tag{CR1}
\]
The vertices of the STN are the positions \(0,\ldots,n-1\). For distinct
positions \(u,v\), define
\[
\varepsilon(u,v)=\mathbf 1_{\{u<v\}},
\qquad
s_\sigma(u,v)=\sigma_u\sigma_v.
\tag{CR2}
\]
The exact directed-edge weight at central radius \(R>0\) is
\[
w_R(u,v)
=
2\pi\varepsilon(u,v)
-\theta_R(\sigma_u^2,\sigma_v^2).
\tag{CR3}
\]
Indeed, when \(u<v\), this is the `wrap_upper` edge
\(u\to v\) of weight \(2\pi-\theta\). When \(u>v\), it is the
`forward_lower` edge \(u\to v\) of weight \(-\theta\). Thus (CR3) is just
the edge convention already proved in the fixed-order STN note, written
without splitting into two cases.

The domain is deliberately the complete Power-Ringmin instance and
\(n\ge3\). The cases \(n=1,2\) are outside the fixed-order threshold semantics
used here. Peripheral tangency is allowed, so exact STN feasibility permits
zero cycle weight.

## 2. Edge Multiplicity, \(q(C)\), And \(S(C)\)

Let \(C\) be a nonempty directed closed walk
\[
C=(v_0,v_1,\ldots,v_{\ell-1},v_\ell=v_0),
\qquad \ell\ge2,
\tag{CR4}
\]
with no self-loop step. Vertices and directed edges may repeat. Write
\(m_C(u,v)\) for the number of traversals of the directed edge \(u\to v\).
Define
\[
q(C)
=
\sum_{u\ne v}m_C(u,v)\varepsilon(u,v),
\tag{CR5}
\]
and
\[
S(C)
=
\sum_{u\ne v}m_C(u,v)\sigma_u\sigma_v.
\tag{CR6}
\]
Every occurrence is counted. In particular, a directed two-cycle
\(u\to v\to u\) traverses the same unordered pair in both directions and
satisfies
\[
q(C)=1,
\qquad
S(C)=2\sigma_u\sigma_v.
\tag{CR7}
\]
This convention is essential: the two-cycle on labels \(2,3\) supplies the
value \(12\) in the \(n=3\) computation.

Every nonempty closed walk satisfies
\[
q(C)\ge1.
\tag{CR8}
\]
If \(q(C)=0\), every traversed edge would have \(u>v\), so the position would
strictly decrease at every step and could not return to its start.

The exact cycle weight obtained by summing (CR3) is
\[
\omega_R(C)
=
2\pi q(C)
-
\sum_{u\ne v}
m_C(u,v)\theta_R(\sigma_u^2,\sigma_v^2).
\tag{CR9}
\]
Angles have the same traversal multiplicity as products. The fixed-order STN
is feasible exactly when every simple directed cycle has nonnegative weight.

Any directed closed walk decomposes into simple directed cycles. Both \(S\)
and \(q\) are additive under this decomposition, and every component has
positive \(q\) by (CR8). Hence
\[
{S(C)\over q(C)}
=
{\sum_r q(C_r)\,S(C_r)/q(C_r)\over\sum_r q(C_r)}
\le
\max_r {S(C_r)\over q(C_r)}.
\tag{CR10}
\]
It follows that repeated walks do not enlarge the optimum and that the finite
simple-cycle maximum exists. Define
\[
\boxed{
\Lambda(\sigma)
=
\max_C {S(C)\over q(C)},
}
\tag{CR11}
\]
where the maximum may equivalently be taken over all nonempty directed closed
walks or only over vertex-simple directed cycles of lengths \(2,\ldots,n\).
The value is a positive rational number at this stage; the one-wrap theorem
below strengthens this to an integer for complete Power-Ringmin orders.

### Cyclic-order symmetry

Changing the linear cut of \(\sigma\) preserves \(\Lambda\). Moving one
position through the cut changes the edge indicator by a vertex coboundary,
\[
\varepsilon'(u,v)
=
\varepsilon(u,v)+h(v)-h(u),
\tag{CR12}
\]
for the indicator \(h\) of the moved vertex. The extra terms telescope on
every closed walk, so \(q(C)\) is unchanged. Reflection also preserves the
maximum: reflect the positions and reverse each directed cycle; this preserves
both \(S\) and \(q\). Therefore minimization over the repository's canonical
rotation/reflection representatives covers the complete cyclic-order space.

### One-wrap cycles and induced subset orders

Define the one-wrap score by
\[
\Lambda^{(1)}(\sigma)
=
\max\{S(C): C\text{ is a nonempty directed closed walk and }q(C)=1\}.
\tag{CR12a}
\]
The denominator is absent because it equals one on this class.

Let \(T=\{i_0<\cdots<i_{m-1}\}\) be a nonempty subset of positions, and
let \(\sigma|_T\) denote the cyclic order induced by
\(\sigma\). Put
\[
P_\sigma(T)
=
\sum_{r=0}^{m-1}
\sigma_{i_r}\sigma_{i_{r+1\bmod m}}.
\tag{CR12b}
\]
When \(m=1\), this convention gives
\(P_\sigma(\{i_0\})=\sigma_{i_0}^2\). When \(m=2\), it gives
\(\sigma_{i_0}\sigma_{i_1}+\sigma_{i_1}\sigma_{i_0}\): the same unordered
pair contributes twice, exactly as in (CR7).

A closed walk with \(q=1\) cannot repeat a vertex. Rotate it so that its
unique ascending edge occurs first. Every later edge strictly decreases its
position until the walk closes, so repetition is impossible. If its selected
positions are \(i_0<\cdots<i_{m-1}\), the unique ascent must leave the least
position and enter the greatest one; all later positions are then forced into
strictly decreasing order. The cycle is therefore
\[
i_0\longrightarrow i_{m-1}\longrightarrow i_{m-2}
\longrightarrow\cdots\longrightarrow i_1\longrightarrow i_0.
\tag{CR12c}
\]
Its product sum is \(P_\sigma(T)\), since reversing a cyclic order does not
change its undirected adjacent-product sum. Conversely, (CR12c) gives a
one-wrap cycle for every \(T\) of cardinality at least two. Hence
\[
\boxed{
\Lambda^{(1)}(\sigma)
=
\max_{\substack{T\subseteq\{0,\ldots,n-1\}\\|T|\ge2}}
P_\sigma(T)
=
\max_{\varnothing\ne T\subseteq\{0,\ldots,n-1\}}
P_\sigma(T).
}
\tag{CR12d}
\]
The second equality holds because, for \(n\ge3\), every singleton score is at
most \(n^2\), while the subset carrying labels \(n-1,n\) has score
\(2n(n-1)>n^2\). Cardinality at least two is the cycle-faithful convention.

### Exact one-wrap saturation

The duplicated-multiset pairing lemma from
`research/ALL_N_LOWER_BOUND.md`, applied to the complete induced order, gives
\[
P_\sigma(\{0,\ldots,n-1\})
\ge
{n(n+1)(n+2)\over6}.
\tag{CR12e}
\]
For completeness, the cycle edges pair the multiset containing two copies of
each label. Oppositely pairing its sorted entries is the rearrangement lower
bound, and its value is
\(\sum_{k=1}^n k(n+1-k)=n(n+1)(n+2)/6\). Thus
\(\Lambda^{(1)}(\sigma)\ge n(n+1)(n+2)/6\).

Now let \(C\) be a vertex-simple directed cycle with selected label set
\(U\). The inequality \(2ij\le i^2+j^2\), summed over its edge occurrences,
and degree two at every selected vertex give
\[
S(C)
\le
\sum_{i\in U}i^2
\le
\sum_{i=1}^n i^2
={n(n+1)(2n+1)\over6}.
\tag{CR12f}
\]
If \(q(C)\ge2\), then
\[
{S(C)\over q(C)}
\le {1\over2}\sum_{i=1}^n i^2
={n(n+1)(n+2)\over6}-{n(n+1)\over4}
<{n(n+1)(n+2)\over6}
\le\Lambda^{(1)}(\sigma).
\tag{CR12g}
\]
By (CR10), only vertex-simple cycles are needed for the full maximum. The
cycles with \(q=1\) give (CR12d), while (CR12g) strictly excludes every
vertex-simple cycle with more wraps. Therefore
\[
\boxed{
\Lambda(\sigma)=\Lambda^{(1)}(\sigma)
=
\max_{\substack{T\subseteq\{0,\ldots,n-1\}\\|T|\ge2}}
P_\sigma(T)
=
\max_{\varnothing\ne T\subseteq\{0,\ldots,n-1\}}
P_\sigma(T)
\qquad(n\ge3).
}
\tag{CR12h}
\]
This is an **EXACT THEOREM for every complete order**, not an inference from
the bounded experiment. It also proves that \(\Lambda(\sigma)\), and hence
\(\Lambda_n\), is an integer. A general closed walk with \(q>1\) can still
attain the same ratio, for example by repeating a maximizing one-wrap simple
cycle. Equality in the weighted average (CR10) requires every simple
component to be one-wrap and maximizing. The strict separation in (CR12g) is
specifically a statement about vertex-simple multi-wrap cycles.

### Exact elimination of label \(1\)

Let
\[
\tau=(a_0,\ldots,a_{n-2})
\tag{CR12i}
\]
be the cyclic core order obtained from \(\sigma\) by deleting label \(1\).
For a nonempty subset \(U\subseteq\{2,\ldots,n\}\), write
\(P_\tau(U)\) for the cyclic adjacent-product sum in the order induced by
\(\tau\), with the same conventions
\[
P_\tau(\{j\})=j^2,
\qquad
P_\tau(\{i,j\})=2ij.
\tag{CR12j}
\]
Define
\[
\boxed{
K(\tau)
=
\max_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P_\tau(U).
}
\tag{CR12k}
\]
Because every label occurs once, label subsets and their position subsets
will be identified below.

Every subset avoiding label \(1\) has exactly the same induced cyclic order
before and after deletion, so
\[
P_\sigma(U)=P_\tau(U)
\qquad
(\varnothing\ne U\subseteq\{2,\ldots,n\}).
\tag{CR12l}
\]
In particular, a core subset attaining \(K(\tau)\) supplies the same score
inside \(\sigma\).

It remains to classify the subsets containing label \(1\).

1. The singleton has
   \[
   P_\sigma(\{1\})=1<4=P_\tau(\{2\})\le K(\tau).
   \tag{CR12m}
   \]
2. For \(j\ge2\), the two-element convention gives
   \[
   P_\sigma(\{1,j\})=2j\le j^2=P_\tau(\{j\})\le K(\tau).
   \tag{CR12n}
   \]
   The first inequality is an equality only at \(j=2\).
3. Suppose \(T\) contains label \(1\) and at least two core labels, and put
   \(U=T\setminus\{1\}\). Let \(a,b\) be the two distinct core neighbors
   of \(1\) in the cyclic order induced by \(T\). Deleting \(1\) replaces
   the two contributions \(a\cdot1+1\cdot b\) by one contribution \(ab\).
   Hence
   \[
   P_\tau(U)-P_\sigma(T)
   =ab-a-b
   =(a-1)(b-1)-1
   \ge1,
   \tag{CR12o}
   \]
   because \(a,b\) are distinct integers at least two. This calculation also
   covers \(|U|=2\): in that case \(P_\tau(U)=2ab\), and only the occurrence
   on the arc through label \(1\) is replaced.

Thus every subset containing label \(1\) is bounded by a core subset, while
(CR12l) realizes the core maximum unchanged. Combining this classification
with (CR12h) proves
\[
\boxed{
\Lambda(\sigma)=K(\tau).
}
\tag{CR12p}
\]
The right side contains no insertion-gap data: the cyclic-ratio score is
therefore independent of where label \(1\) is inserted into a fixed core
order. Equation (CR12o) makes the third case strictly smaller than its core
deletion. The first two cases have score at most \(n^2\), while
\[
K(\tau)\ge P_\tau(\{n-1,n\})=2n(n-1)>n^2.
\tag{CR12q}
\]
Hence no maximizing subset contains label \(1\).
This independence concerns the separable product score \(\Lambda\), not the
exact angular threshold \(\rho_\sigma\) or fixed-order feasibility.

The smallest case is explicit. For \(n=3\), the unique core class is
\(\tau=(3,2)\), and its nonempty-subset scores are \(9,4,12\), so
\[
K(3,2)=12.
\tag{CR12r}
\]
Insertion into its two cyclic arcs gives \((3,1,2)\) and \((3,2,1)\).
They are reflections, represent one complete canonical class, and both have
\(\Lambda=12\).

## 3. Exact Fixed-Order Sandwich

For distinct \(1\le i,j\le n\) and \(R>0\), the two angular estimates needed
here are
\[
\boxed{
{2ij\over R+n^2}
<
\theta_R(i^2,j^2)
<
{2ij\over R}.
}
\tag{CR13}
\]
The right inequality is the strict general angular majorant proved in
`research/ALL_N_LOWER_BOUND.md`. For the left inequality, that note records
the valid weak estimate. Its one-line strict refinement follows because its
argument has \(0<x<1\), so \(\arcsin x>x\), while
\(\sqrt{(R+i^2)(R+j^2)}\le R+n^2\).

Let \(F_\sigma\) be the feasible positive-radius set and
\(\rho_\sigma=\inf F_\sigma\). The fixed-order STN theorem proves
\[
F_\sigma=[\rho_\sigma,\infty),
\qquad
\rho_\sigma>0.
\tag{CR14}
\]

### Lower side

Let \(C_*\) attain (CR11). If \(R\in F_\sigma\), then (CR9), feasibility,
and the strict left estimate in (CR13) give
\[
0
\le \omega_R(C_*)
<
2\pi q(C_*)-{2S(C_*)\over R+n^2}.
\tag{CR15}
\]
Therefore
\[
R
>
{S(C_*)\over\pi q(C_*)}-n^2
=
{\Lambda(\sigma)\over\pi}-n^2.
\tag{CR16}
\]
Applying (CR16) at the attained threshold \(R=\rho_\sigma\) yields
\[
\rho_\sigma
>
{\Lambda(\sigma)\over\pi}-n^2.
\tag{CR17}
\]
Without using threshold attainment, taking the infimum would give only the
requested non-strict inequality. If the expression on the right is
nonpositive, it remains a valid algebraic lower bound but is not a claim about
negative central radii.

### Upper side

Put
\[
R_0={\Lambda(\sigma)\over\pi}>0.
\tag{CR18}
\]
For every simple directed cycle \(C\), the strict right estimate in (CR13)
gives
\[
\omega_{R_0}(C)
>
2\pi q(C)-{2S(C)\over R_0}
\ge0.
\tag{CR19}
\]
All simple cycle weights are strictly positive, so the negative-cycle theorem
makes the STN feasible at \(R_0\). Since there are only finitely many simple
cycles and their weights are continuous, their strict positivity persists on
some left neighborhood of \(R_0\). Hence
\[
\rho_\sigma<R_0={\Lambda(\sigma)\over\pi}.
\tag{CR20}
\]

Combining the two sides proves the requested exact sandwich
\[
\boxed{
{\Lambda(\sigma)\over\pi}-n^2
\le \rho_\sigma
\le {\Lambda(\sigma)\over\pi}
}
\tag{CR21}
\]
and the sharper endpoint statement valid on the present domain,
\[
\boxed{
{\Lambda(\sigma)\over\pi}-n^2
< \rho_\sigma
< {\Lambda(\sigma)\over\pi}
\qquad(n\ge3).
}
\tag{CR22}
\]
Equivalently,
\[
0<\Lambda(\sigma)-\pi\rho_\sigma<\pi n^2.
\tag{CR23}
\]

## 4. Global Version

Let \(\Omega_n\) be the finite space of complete cyclic orders, with or
without quotienting by rotation and reflection, and define
\[
\Lambda_n
=
\min_{\sigma\in\Omega_n}\Lambda(\sigma).
\tag{CR24}
\]
Every feasible full configuration has one complete cyclic order, and the
fixed-order feasible sets are closed upper intervals. Finiteness therefore
gives
\[
R_2^*(n)=\min_{\sigma\in\Omega_n}\rho_\sigma.
\tag{CR25}
\]

For the lower side, apply (CR17) to an order minimizing \(\rho_\sigma\). For
the upper side, apply (CR20) to an order minimizing \(\Lambda(\sigma)\). This
proves
\[
\boxed{
{\Lambda_n\over\pi}-n^2
\le R_2^*(n)
\le {\Lambda_n\over\pi}
}
\tag{CR26}
\]
and, more sharply,
\[
\boxed{
{\Lambda_n\over\pi}-n^2
< R_2^*(n)
< {\Lambda_n\over\pi}
\qquad(n\ge3).
}
\tag{CR27}
\]
Thus the exact global additive relation is
\[
\boxed{
0<\Lambda_n-\pi R_2^*(n)<\pi n^2.
}
\tag{CR28}
\]

Let \(\mathcal T_n\) be the finite cyclic-order space of the core labels
\(\{2,\ldots,n\}\). Deleting label \(1\) maps every complete cyclic order
to one member of \(\mathcal T_n\), and inserting label \(1\) into any core
gap supplies a complete preimage. Equation (CR12p) is constant over all such
preimages. Therefore the global objective has the exact reduced form
\[
\boxed{
\Lambda_n
=
\min_{\tau\in\mathcal T_n}K(\tau).
}
\tag{CR28a}
\]
By itself this is a reduction from complete to core orders, not a closed-form
evaluation or a general classification of the minimizing core orders. The
separate finite `n=9` classification below uses additional equality and
shortcut-gain arguments.

### Exact obstruction from two nested tails

Fix \(n\ge4\) and \(1\le m\le n-3\), and put
\[
S_m=\{m,m+1,\ldots,n\},
\qquad
T=S_{m+1},
\qquad
q=|T|=n-m\ge3.
\tag{CR28b}
\]
Let \(C\) be the simple cyclic order induced on \(T\). In the cyclic order
induced on \(S_m\), label \(m\) splits one edge \(e=\{a,b\}\) of \(C\).
Writing \(P(C)\) for the adjacent-product sum of the inner cycle, deletion
and insertion give the exact identity
\[
P_\sigma(S_m)
=P(C)+\delta_m(a,b),
\qquad
\delta_m(a,b)
=m(a+b)-ab
=m^2-(a-m)(b-m).
\tag{CR28c}
\]
Consequently
\[
\max\{P_\sigma(S_m),P_\sigma(T)\}
=P(C)+[\delta_m(a,b)]_+,
\qquad [x]_+=\max(0,x).
\tag{CR28d}
\]

Let \(\mathcal C(T)\) be the finite set of undirected simple spanning cycles
on \(T\), and define
\[
\boxed{
\beta_{m,n}
=
\min_{\substack{C\in\mathcal C(T)\\e=\{a,b\}\in E(C)}}
\left(P(C)+[\delta_m(a,b)]_+\right).
}
\tag{CR28e}
\]
This is not merely a convenient lower bound. Every complete order produces a
pair \((C,e)\) in (CR28e). Conversely, every such pair is realized by
inserting \(m\) into \(e\), then inserting labels
\(1,\ldots,m-1\) arbitrarily; those later insertions do not alter either
induced tail order. Hence
\[
\beta_{m,n}
=
\min_{\sigma\in\Omega_n}
\max\{P_\sigma(S_m),P_\sigma(S_{m+1})\}.
\tag{CR28f}
\]
By one-wrap saturation, both subset scores are bounded above by
\(\Lambda(\sigma)\). Therefore, with
\[
\beta_n^{(2)}
=\max_{1\le m\le n-3}\beta_{m,n},
\]
one has the exact method lower bound
\[
\boxed{\Lambda_n\ge\beta_n^{(2)}.}
\tag{CR28g}
\]

The pairing signatures used to estimate (CR28e) require a connectivity audit.
Pairing the duplicated multiset
\[
M_T=\{x,x:x\in T\}
\]
produces a multigraph on \(T\) in which every vertex automatically has degree
two, with a loop counted twice. For \(q\ge3\), such a signature is the edge
signature of one simple spanning cycle if and only if the multigraph is
loopless and connected. Equivalently, an explicit audit may require: exactly
\(q\) edges using both copies of every label, degree two at each label, no
loops, no repeated unordered edge, and connectedness. The last condition
cannot be omitted: a disjoint union of two or more cycles passes the local
degree test. For \(q=2\), outside the present domain, the induced-subset
convention instead uses the exceptional double edge and score \(2ab\).

The fixed-edge pairing form makes the finite refinement explicit. For
\(e=\{a,b\}\), remove one copy of each endpoint and write
\[
N_e=M_T\setminus\{a,b\},
\qquad
F_e=ab+A(N_e),
\tag{CR28h}
\]
where \(A(N_e)\) is the anti-sorted rearrangement sum of the residual
multiset. If
\[
H_e=\min\{P(C):C\in\mathcal C(T),\ e\in E(C)\},
\]
then the residual edges pair \(N_e\), so
\[
H_e\ge F_e,
\qquad
\beta_{m,n}
=\min_e\bigl(H_e+[\delta_m(e)]_+\bigr)
\ge\min_e\bigl(F_e+[\delta_m(e)]_+\bigr).
\tag{CR28i}
\]
If a signature attaining \(F_e\) is used for equality or pruning, the *full*
signature obtained after restoring \(e\) must satisfy all the simple-cycle
conditions above. The `n=10` equality proof below illustrates the distinction:
the fixed-edge floor for \(\{8,9\}\) is not cycle-realizable, whereas the
floor for \(\{7,10\}\) is.

For the consecutive inner tail, the unrestricted pairing floor is
\[
A(T)=P_{m+1,n}
=\sum_{k=m+1}^n k(m+n+1-k)
=
{(n-m)(m^2+4mn+n^2+3m+3n+2)\over6}.
\tag{CR28j}
\]
Since \(a-m,b-m\) are distinct elements of \(\{1,\ldots,q\}\),
\[
m^2-q(q-1)
\le\delta_m(a,b)\le m^2-2.
\]
Thus pairing plus the insertion correction already gives the explicit bound
\[
\beta_{m,n}
\ge
P_{m+1,n}+[m^2-q(q-1)]_+
\ge P_{m+1,n}.
\tag{CR28k}
\]

It remains possible a priori that enforcing one connected simple cycle raises
the pairing floor by order \(n^3\). An explicit cycle rules this out. Write
\(x_i=m+i\), \(1\le i\le q\). If \(q=2t\), take
\[
Z=(x_1,x_{2t},x_2,x_{2t-1},\ldots,x_t,x_{t+1}).
\]
If \(q=2t+1\), take
\[
Z=(x_{t+1},x_1,x_{2t+1},x_2,x_{2t},\ldots,x_t,x_{t+2}).
\]
These are literal simple spanning cycles. In the even case, putting
\(L_i=x_i\), \(H_i=x_{2t+1-i}\) gives
\[
P(Z)-P_{m+1,n}
=\sum_{i=1}^{t-1}(H_i-H_t)
={t(t-1)\over2}.
\]
In the odd case, with \(c=x_{t+1}\) and
\(H_i=x_{2t+2-i}\), direct subtraction gives
\[
P(Z)-P_{m+1,n}
=\sum_{i=1}^t(H_i-c)
={t(t+1)\over2}.
\]
Denote these two exact excesses by \(g(q)\). Then
\(0\le g(q)\le q^2/8\), while (CR28c) gives
\([\delta_m(e)]_+\le m^2\) on every edge. Choosing any edge of \(Z\) in
(CR28e), and using
\[
n^2-m^2-{q^2\over8}=2mq+{7q^2\over8}>0,
\]
yields the uniform exact squeeze
\[
\boxed{
P_{m+1,n}
\le\beta_{m,n}
\le P_{m+1,n}+g(n-m)+m^2
\le P_{m+1,n}+n^2.
}
\tag{CR28l}
\]

This squeeze determines the strongest leading coefficient available from the
two-tail schema. If \(m=\alpha n+O(1)\), then
\[
P_{m+1,n}
=\phi(\alpha)n^3+O(n^2),
\qquad
\phi(\alpha)
={(1-\alpha)(\alpha^2+4\alpha+1)\over6}.
\tag{CR28m}
\]
Moreover,
\[
\phi'(\alpha)={1-2\alpha-\alpha^2\over2},
\qquad
\phi''(\alpha)=-(1+\alpha)<0.
\]
The unique maximizer is \(\alpha_0=\sqrt2-1\), and
\[
\phi(\alpha_0)={2(\sqrt2-1)\over3}.
\]
The old exact tail optimization has an interior maximizer at least two, so the
shift from \(P_{m,n}\) to \(P_{m+1,n}\) and the restriction
\(1\le m\le n-3\) do not remove its discrete maximum. Taking maxima in
(CR28l) gives, exactly,
\[
\max_{1\le \ell\le n-2}P_{\ell,n}
\le\beta_n^{(2)}
\le\max_{1\le \ell\le n-2}P_{\ell,n}+n^2.
\]
The established discrete tail asymptotics therefore prove
\[
\boxed{
\beta_n^{(2)}
={2(\sqrt2-1)\over3}n^3+O(n^2),
\qquad
\lim_{n\to\infty}{\beta_n^{(2)}\over n^3}
={2(\sqrt2-1)\over3}.
}
\tag{CR28n}
\]

Thus this refinement can improve finite lower terms--at \((m,n)=(4,10)\),
for example, the inner pairing floor is 320 while
\(\beta_{4,10}=323\)--but it **cannot improve the cubic coefficient**
\(2(\sqrt2-1)/3\). This is an exact limitation of the single-\(m\),
two-consecutive-tail schema (CR28e)--(CR28g), not an upper bound on
\(\Lambda_n\). It does not exclude a gain from coupling a number of tails
that grows with \(n\), from nonconsecutive subsets, or from additional global
structure.

### Exact obstruction from three nested tails

Fix \(n\ge5\) and \(1\le m\le n-4\), and put
\[
y=m,
\qquad x=m+1,
\qquad T=S_{m+2},
\qquad q=|T|=n-m-1\ge3.
\tag{CR28o}
\]
For a simple cycle \(C\) on a vertex set \(V\), an edge
\(e=\{a,b\}\in E(C)\), and a new label \(z\notin V\), write
\(C\mathbin\oplus_e z\) for the edge split
\[
E(C\mathbin\oplus_e z)
=
\bigl(E(C)\setminus\{\{a,b\}\}\bigr)
\cup\{\{a,z\},\{z,b\}\}.
\tag{CR28p}
\]
This is again a simple spanning cycle. Also put
\[
\delta_t(u,v)
=t(u+v)-uv
=t^2-(u-t)(v-t).
\tag{CR28q}
\]

For later comparison, define the exact one-tail cycle minimum
\[
P^*_{\ell,n}
=
\min_{C\in\mathcal C(S_\ell)}P(C)
\qquad(1\le\ell\le n-2).
\tag{CR28r}
\]
This is distinct from the established duplicated-pairing floor
\(P_{\ell,n}\), although the alternating cycle in the preceding proof puts
them within \(O(n^2)\) of one another.

Delete \(y=m\) and then \(x=m+1\) from the cycle induced by a complete order
on \(S_m\). The result is uniquely a triple
\[
C\in\mathcal C(T),
\qquad e=\{a,b\}\in E(C),
\qquad
f=\{u,v\}\in E(C\mathbin\oplus_e x).
\tag{CR28s}
\]
Conversely, splitting \(e\) with \(x\), then \(f\) with \(y\), reconstructs
a unique cycle on \(S_m\); inserting \(1,\ldots,m-1\) arbitrarily extends it
to a complete order without changing the three tail scores. Thus this is a
bijection, not a relaxation. Indeed, modulo dihedral symmetry, its cardinality
is
\[
{(q-1)!\over2}\,q(q+1)={(q+1)!\over2},
\]
the number of simple cycles on the \(q+2\) labels of \(S_m\).

Let
\[
A=\delta_x(a,b),
\qquad B=\delta_y(u,v).
\]
Literal deletion and insertion give
\[
\begin{aligned}
P_\sigma(S_{m+2})&=P(C),\\
P_\sigma(S_{m+1})&=P(C)+A,\\
P_\sigma(S_m)&=P(C)+A+B.
\end{aligned}
\tag{CR28t}
\]
Consequently, for
\[
\gamma^*_{m,n}
=
\min_{\sigma\in\Omega_n}
\max\{P_\sigma(S_m),P_\sigma(S_{m+1}),P_\sigma(S_{m+2})\},
\]
one has the exact reduction
\[
\boxed{
\gamma^*_{m,n}
=
\min_{\substack{C\in\mathcal C(T),\ e=\{a,b\}\in E(C)\\
                  f=\{u,v\}\in E(C\mathbin\oplus_e x)}}
\left(
P(C)+\max\{0,A,A+B\}
\right).
}
\tag{CR28u}
\]
The prefix maximum is essential. If
\(h(A,B)=\max(0,A,A+B)\), then
\[
h(A,B)=
\begin{cases}
A+[B]_+,&A\ge0,\\
[A+B]_+,&A<0,
\end{cases}
\qquad
h(A,B)\le[A]_++[B]_+,
\tag{CR28v}
\]
but the upper bound is not an exact replacement in general.

The simple-cycle and compatibility conditions in (CR28u) cannot be reduced
to three independently optimized pairing signatures. On a vertex set of at
least three labels, a duplicated-label pairing signature represents one
simple spanning cycle exactly when it has the following properties: it has
one unordered edge per vertex, every endpoint lies in the vertex set, every
vertex has degree two, there are no loops or repeated unordered edges, and
the resulting graph is connected. Degree two alone permits a disjoint union
of proper subcycles. Starting from a valid \(C\), each genuine split in
(CR28p) preserves every condition automatically. Starting from proposed
signatures instead, one must also verify the two exact linkage identities
\[
E(C_1)=
\bigl(E(C)\setminus\{e\}\bigr)\cup\{\{a,x\},\{x,b\}\},
\]
\[
E(C_0)=
\bigl(E(C_1)\setminus\{f\}\bigr)\cup\{\{u,y\},\{y,v\}\},
\tag{CR28w}
\]
and audit the connected simple cycle after restoring \(f\), then \(e\), in
that order. Separate fixed-edge pairing floors need not satisfy this audit.
The exceptional two-label double edge never occurs because \(q\ge3\).

For fixed \(C\) and \(e=\{a,b\}\), the \(q+1\) possible choices of \(f\)
are exhaustive:

1. \(f=\{a,x\}\) or \(f=\{x,b\}\). These are the two nested splits of the
   same base edge and replace the local arc \(a-b\) by, respectively,
   \(a-y-x-b\) or \(a-x-y-b\).
2. \(f\in E(C)\setminus\{e\}\) shares one endpoint with \(e\). There are
   exactly two such surviving base edges.
3. \(f\in E(C)\setminus\{e\}\) is disjoint from \(e\). There are \(q-3\)
   such edges, none when \(q=3\).

There is no fourth case: \(e\) itself was removed by the first split. In the
last two cases the two splits use distinct base edges and commute, including
when the edges share one endpoint. In the nested cases the second corrections
are explicitly
\[
\delta_y(a,x)=m^2+m-a,
\qquad
\delta_y(x,b)=m^2+m-b.
\tag{CR28x}
\]
They can be positive, so the three-tail obstruction does not collapse to the
two-tail obstruction.

Nested splits remain part of the bijection and can tie at the minimum, but
they are weakly dominated for purposes of minimizing (CR28u). For example,
if \(f=\{a,x\}\) and \(\{a,a'\}\ne e\) is the other base edge incident to
\(a\), then
\[
\delta_y(a,a')-\delta_y(a,x)
=(a'-x)(y-a)<0.
\]
The function \(h(A,B)\) is nondecreasing in \(B\), so replacing the nested
split by the surviving edge \(\{a,a'\}\) cannot increase the objective. The
case \(f=\{x,b\}\) is identical. Hence the minimum also has the simpler exact
form
\[
\boxed{
\gamma^*_{m,n}
=
\min_{\substack{C\in\mathcal C(T)\\e,g\in E(C),\ e\ne g}}
\left(
P(C)+h\bigl(\delta_{m+1}(e),\delta_m(g)\bigr)
\right).
}
\tag{CR28y}
\]

We can now prove the requested uniform comparison. Since \(h\ge0\), every
candidate in (CR28u) is at least \(P(C)\), and therefore
\(\gamma^*_{m,n}\ge P^*_{m+2,n}\). Conversely, choose a cycle attaining
\(P^*_{m+2,n}\) and two distinct base edges as in (CR28y). The endpoints of
the first edge are distinct labels greater than \(x\), while those of the
second are distinct labels at least \(y+2\). Thus
\[
\delta_x(e)\le (m+1)^2-2,
\qquad
\delta_y(g)\le m^2-6.
\]
Using (CR28v) gives the explicit uniform bound
\[
\boxed{
0\le
\gamma^*_{m,n}-P^*_{m+2,n}
\le (m+1)^2-2+[m^2-6]_+
<2n^2.
}
\tag{CR28z}
\]
Thus the proposed \(P^*_{m+2,n}+O(n^2)\) statement is true, uniformly over
the full stated two-parameter domain.

It is also true with the duplicated-pairing floor \(P_{m+2,n}\). The exact
alternating cycle on \(q=n-m-1\) consecutive labels satisfies
\[
P_{m+2,n}\le P^*_{m+2,n}\le P_{m+2,n}+g(q),
\qquad
0\le g(q)\le {q^2\over8}.
\]
Combining this with the preceding construction and
\[
2n^2-\left((m+1)^2+m^2+{q^2\over8}\right)
=4mq+2m+{15q^2\over8}+4q+1>0
\]
proves the second uniform squeeze
\[
\boxed{
P_{m+2,n}
\le\gamma^*_{m,n}
<P_{m+2,n}+2n^2.
}
\tag{CR28aa}
\]

Finally define the strongest obstruction obtained by optimizing one block of
three consecutive tails,
\[
\Gamma_n^{(3)}
=\max_{1\le m\le n-4}\gamma^*_{m,n}.
\]
Each of the three subset scores is at most \(\Lambda(\sigma)\), so
\(\Lambda_n\ge\Gamma_n^{(3)}\); this is only a one-sided method bound. From
(CR28aa),
\[
M_n^{(3)}
:=\max_{3\le\ell\le n-2}P_{\ell,n}
\le\Gamma_n^{(3)}
<M_n^{(3)}+2n^2.
\tag{CR28ab}
\]
For \(\alpha=\ell/n\), the exact tail polynomial can be written
\[
P_{\ell,n}
=n^3\phi(\alpha)+\alpha n^2+{\alpha-1\over6}n,
\qquad
\phi(\alpha)
={(1-\alpha)(\alpha^2+4\alpha+1)\over6}.
\tag{CR28ac}
\]
The lower-order terms are uniform for \(0\le\alpha\le1\). As already used in
the two-tail proof, \(\phi\) is strictly concave, has unique maximizer
\(\alpha_0=\sqrt2-1\), and
\(\phi(\alpha_0)=2(\sqrt2-1)/3\). An integer within one of
\(\alpha_0n\) lies in \(3\le\ell\le n-2\) for all sufficiently large \(n\),
so the discrete restriction does not remove the leading maximizer. Therefore
\[
M_n^{(3)}
={2(\sqrt2-1)\over3}n^3+O(n^2),
\]
and (CR28ab) proves
\[
\boxed{
\Gamma_n^{(3)}
={2(\sqrt2-1)\over3}n^3+O(n^2),
\qquad
\lim_{n\to\infty}{\Gamma_n^{(3)}\over n^3}
={2(\sqrt2-1)\over3}.
}
\tag{CR28ad}
\]
This is an exact limitation of the obstruction formed from one optimized
block of three consecutive tails. It is not an asymptotic formula, upper
bound, or convergence result for \(\Lambda_n\), and it makes no exact
asymptotic claim about \(R_2^*(n)\).

Independent exact test-local checks exercise the full reduction without
production scoring or enumeration. For \((m,n)=(2,7)\), the 60 compatible
double splits are exactly all 60 dihedral cycles on \(S_2\), with interaction
counts 24 nested, 24 distinct-incident, and 12 distinct-disjoint. The exact
rows
\[
\bigl(P_{m+2,n},P^*_{m+2,n},\gamma^*_{m,n}\bigr)
\]
are
\[
(46,47,47),\quad
(116,117,118),\quad
(235,237,239),\quad
(320,322,323)
\]
for \((m,n)=(1,5),(2,7),(3,9),(3,10)\), respectively. A separate bounded
grid checks the alternating-cycle excess and the uniform quadratic
construction. These finite computations verify arithmetic and compatibility;
they are not the all-\(n\) proof.

### Exact obstruction from an arbitrary block of nested tails

The preceding two constructions have one uniform form. Fix
\[
2\le r\le n-2,
\qquad
1\le m\le n-r-1,
\qquad
\ell=m+r-1,
\qquad
q=n-\ell+1\ge3.
\tag{CR28ae}
\]
Thus the block is
\(S_m,S_{m+1},\ldots,S_\ell\), and the innermost tail \(S_\ell\)
has at least three labels. The ordinary simple-cycle convention therefore
applies at every level; the two-label double-edge exception lies outside this
domain.

Let \(C_0\in\mathcal C(S_\ell)\). For
\(j=1,\ldots,r-1\), define
\[
z_j=\ell-j,
\qquad
e_j=\{u_j,v_j\}\in E(C_{j-1}),
\qquad
C_j=C_{j-1}\mathbin\oplus_{e_j}z_j.
\tag{CR28af}
\]
Equivalently, the literal edge linkage at level \(j\) is
\[
E(C_j)
=
\bigl(E(C_{j-1})\setminus\{e_j\}\bigr)
\cup
\{\{u_j,z_j\},\{z_j,v_j\}\}.
\tag{CR28ag}
\]
Put
\[
A_j
=\delta_{z_j}(u_j,v_j)
=z_j(u_j+v_j)-u_jv_j
=z_j^2-(u_j-z_j)(v_j-z_j),
\tag{CR28ah}
\]
and define the correction prefixes
\[
H_0=0,
\qquad
H_j=\sum_{i=1}^j A_i
\quad(1\le j\le r-1).
\tag{CR28ai}
\]
Every current endpoint is larger than the newly inserted label. Literal
insertion therefore gives, at every level,
\[
P(C_j)=P(C_{j-1})+A_j=P(C_0)+H_j,
\qquad
C_j\text{ is the cycle induced on }S_{\ell-j}.
\tag{CR28aj}
\]

Deleting \(m,m+1,\ldots,\ell-1\), in that order, from a cycle on
\(S_m\) records a unique history (CR28af). Inserting the labels in the
reverse order reconstructs the original cycle. Hence deletion and insertion
are inverse bijections. The count supplies a useful independent audit:
\[
{(q-1)!\over2}\,q(q+1)\cdots(q+r-2)
={(q+r-2)!\over2},
\tag{CR28ak}
\]
which is exactly the number of undirected simple cycles on the
\(q+r-1\) labels of \(S_m\), modulo dihedral symmetry.
Every such cycle extends to a complete order by inserting
\(1,\ldots,m-1\) arbitrarily, without changing any score in the stated
tail block.

Define the strongest separately optimized obstruction using precisely this
one block by
\[
\gamma^{(r)}_{m,n}
=
\min_{\sigma\in\Omega_n}
\max_{0\le j\le r-1}P_\sigma(S_{m+j}).
\]
The bijection and (CR28aj) give the exact parametrization
\[
\boxed{
\gamma^{(r)}_{m,n}
=
\min_{\substack{C_0\in\mathcal C(S_\ell)\\
                  e_j\in E(C_{j-1}),\ 1\le j\le r-1}}
\left[
P(C_0)+\max_{0\le j\le r-1}H_j
\right].
}
\tag{CR28al}
\]
Here \(\gamma^{(2)}_{m,n}=\beta_{m,n}\), while
\(\gamma^{(3)}_{m,n}=\gamma^*_{m,n}\). The displayed maximum is a
maximum of signed prefixes. Replacing it by
\(\sum_j[A_j]_+\) is only an upper bound, not an exact formula.

If the history is specified through pairing signatures rather than literal
cycles, compatibility must be audited at every level. Each \(C_j\) must be
one connected, loopless, degree-two spanning graph with no repeated
unordered edge, and (CR28ag) must hold literally. Reverse contraction must
restore \(C_{r-2},C_{r-3},\ldots,C_0\) in that order. Independently valid
signatures, degree conditions alone, or independently chosen insertion edges
do not encode the same object.

In particular, the distinct-base-edge simplification proved for three tails
does not extend automatically. A fully nested admissible domino starts from
any base cycle containing \(\{\ell,\ell+1\}\) and, for
\(t=\ell-1,\ldots,m\), splits the surviving child edge
\(\{t+1,t+2\}\) with label \(t\). Its corrections are exactly
\[
\delta_t(t+1,t+2)=t^2-2.
\tag{CR28am}
\]
Thus the positive-prefix envelope below is attained by a compatible history
whenever \(m\ge2\). This is a statement about admissible histories, not a
lower bound on the minimized excess. It shows both that compatibility does
not force the corrections to cancel and that a bound independent of \(r\)
cannot be justified merely by dismissing nested splits. Moreover, when
\(r-1>q\), using distinct base edges for every insertion is combinatorially
impossible even though the exact histories continue to exist.

We now prove the uniform comparison. At the insertion of \(t\), the two
endpoints are distinct elements of \(S_{t+1}\). Hence their positive
differences from \(t\) are distinct, their product is at least two, and
\[
A_j\le z_j^2-2.
\]
For every signed sequence,
\(\max_j H_j\le\sum_j[A_j]_+\). Therefore, with
\[
E_{m,\ell}
=\sum_{t=m}^{\ell-1}[t^2-2]_+,
\]
choosing a base cycle attaining \(P^*_{\ell,n}\) and any compatible
history proves
\[
\boxed{
0\le
\gamma^{(r)}_{m,n}-P^*_{\ell,n}
\le E_{m,\ell}
<(r-1)n^2.
}
\tag{CR28an}
\]
The positive part is essential when \(t=1\). This proves the requested
uniform \(O(rn^2)\) bound relative to the exact inner-cycle minimum; for
fixed \(r\) it is \(O_r(n^2)\).

The comparison with the duplicated-pairing floor is equally uniform. The
alternating cycle from (CR28l), now on the \(q\) labels of \(S_\ell\),
gives
\[
P_{\ell,n}
\le P^*_{\ell,n}
\le P_{\ell,n}+g(q),
\qquad
0\le g(q)\le {q^2\over8}.
\]
Combining this with (CR28an) yields the explicit squeeze
\[
\boxed{
P_{\ell,n}
\le\gamma^{(r)}_{m,n}
\le P_{\ell,n}+g(q)+E_{m,\ell}
<P_{\ell,n}+rn^2.
}
\tag{CR28ao}
\]

Now put
\[
\Gamma_n^{(r)}
=\max_{1\le m\le n-r-1}\gamma^{(r)}_{m,n},
\qquad
M_{n,r}=\max_{r\le\ell\le n-2}P_{\ell,n}.
\tag{CR28ap}
\]
Every score in a block is at most \(\Lambda(\sigma)\), so
\(\Lambda_n\ge\Gamma_n^{(r)}\). This is a maximum of separately
optimized one-block obstructions; it does not exchange the maximum over
\(m\) with the minimum over complete orders. From (CR28ao),
\[
M_{n,r}
\le\Gamma_n^{(r)}
<M_{n,r}+rn^2.
\tag{CR28aq}
\]
There is also a useful lower audit for long blocks. Every
\(t\in\{1,\ldots,n-2\}\) belongs to at least one admissible block of
length \(r\), and every induced cycle on \(S_t\) has score at least
\(P^*_{t,n}\). Consequently
\[
\Gamma_n^{(r)}
\ge\max_{1\le t\le n-2}P^*_{t,n}
\ge\max_{1\le t\le n-2}P_{t,n}.
\tag{CR28ar}
\]
Thus truncating the *inner-reference* range to \(\ell\ge r\) never proves
that the full block obstruction has a smaller coefficient.

Let \(r=r(n)\) be any integer sequence satisfying the domain above and
\(r=o(n)\). The exact maximizing tail index is
\((\sqrt2-1)n+O(1)\), so it lies in \([r,n-2]\) for all sufficiently
large \(n\). Hence \(M_{n,r}\) is then the unrestricted one-tail maximum.
Using (CR28ac), (CR28aq), and \(rn^2=o(n^3)\) gives
\[
\boxed{
\Gamma_n^{(r(n))}
={2(\sqrt2-1)\over3}n^3+O(r(n)n^2)
={2(\sqrt2-1)\over3}n^3+o(n^3).
}
\tag{CR28as}
\]
In particular, every fixed \(r\) has remainder \(O_r(n^2)\), and every
sublinear block length preserves the one-tail cubic coefficient for this
method.

The normalized error in (CR28aq) is bounded by \(r/n\). It vanishes for
every sublinear block and first becomes potentially order one when
\(r=\Theta(n)\), the largest possible growth scale in the present domain.
At that linear scale the admissible domino (CR28am) can accumulate
\(\Theta(rn^2)=\Theta(n^3)\) correction along one history, so recursive
compatibility alone supplies no hidden subcubic cancellation. This does
**not** prove that the minimized obstruction improves, or even changes, its
coefficient. It proves only that linear-size blocks are the first scale not
excluded by this uniform comparison. The next section treats one explicit
linear sequence and proves a cubic residual by an additional argument; it
does not classify every linear density or determine an exact coefficient.

A bounded exact test-local oracle checks the first new case without touching
production code. At \((m,n,r)=(2,7,4)\), the base has three labels. The
\(3\cdot4\cdot5=60\) compatible triple-split histories have distinct final
signatures and equal all 60 directly generated outer dihedral cycles,
signature by signature. Literal prefix scoring gives
\[
\bigl(P_{5,7},P^*_{5,7},\gamma^{(4)}_{2,7}\bigr)
=(106,107,118).
\]
The same bounded checks retain the 12 fully child-edge-nested histories and
verify a domino attaining \(E_{2,5}=23\). These are finite exact arithmetic
and coverage checks, not the proof of (CR28al)--(CR28as).

### Joint optimization of the first linear-density certificate

The first scale left open by (CR28as) can be separated from the inner-cycle
reference for an arbitrary constant density. Put
\[
0<\alpha<1,
\qquad
r=r_n=\lfloor\alpha n\rfloor.
\tag{CR28at}
\]
Whenever
\[
2\le r_n\le n-2,
\]
equations (CR28ae)--(CR28al) apply with \(m=1\), block length \(r_n\), and
\(\ell=r_n\). In particular, the exact object under study is
\[
\gamma^{(r_n)}_{1,n}
=
\min_{\text{compatible histories}}
\left[
P(C_0)+\max_{0\le j\le r_n-1}H_j
\right],
\tag{CR28au}
\]
where \(C_0\) is a simple cycle on \(S_{r_n}\), every split uses a literal
current edge, and every intermediate signature remains a connected simple
spanning cycle.

Introduce constant cutoff and prefix-weight parameters
\[
0<\beta<\alpha,
\qquad
0\le\lambda\le1,
\qquad
s=s_n(\beta)=\lceil\beta n\rceil,
\qquad
S=n+r,
\qquad
q=n-r+1,
\qquad
k=r-s.
\tag{CR28av}
\]
Thus the exact eventually proof-valid region is
\[
\mathcal A
=\{(\alpha,\beta,\lambda):
0<\alpha<1,\ 0<\beta<\alpha,\ 0\le\lambda\le1\}.
\]
At a fixed \(n\), the complete finite conditions are
\[
2\le\lfloor\alpha n\rfloor\le n-2,
\qquad
1\le\lceil\beta n\rceil\le\lfloor\alpha n\rfloor-1.
\]
The elementary weighted-prefix step used below is valid for every real \(H\)
if and only if
\[
\max(0,H)\ge\lambda H
\quad\hbox{for every }H\in\mathbb R
\quad\Longleftrightarrow\quad
0\le\lambda\le1;
\]
the reverse implications are witnessed by \(H=-1\) and \(H=1\). The
rounding estimate
\[
k\ge(\alpha-\beta)n-2
\tag{CR28aw}
\]
gives a uniform finite domain for every fixed admissible triple.

The base pairing floor has an exact quadratic slack decomposition. For every
simple cycle \(C\) on \(S_r\),
\[
\boxed{
P(C)-P_{r,n}
=
{1\over2}
\sum_{\{u,v\}\in E(C)}
(u+v-S)^2.
}
\tag{CR28ax}
\]
To verify it, use degree two and
\(\sum_{x=r}^n x=qS/2\). Expanding the right-hand side gives
\[
P(C)+\sum_{x=r}^n x^2-{qS^2\over2},
\]
while
\[
P_{r,n}
=
\sum_{x=r}^n x(S-x)
={qS^2\over2}-\sum_{x=r}^n x^2.
\]
Thus (CR28ax) is an identity, not a stability heuristic, and it is independent
of the density \(\alpha\).

Fix an arbitrary compatible history in (CR28au), and retain only its first
\(k\) insertions, namely \(t=r-1,r-2,\ldots,s\). Write
\[
H_k=\sum_{t=s}^{r-1}A_t.
\]
Call the split at \(t\) a **base split** when it uses an edge of the original
\(C_0\) that is still present, and a **recursive split** otherwise. Every
base edge can be used at most once. Once split, it is replaced by two edges
incident to a label below \(r\), and later operations never recreate an edge
whose two endpoints both belong to the original \(S_r\). Inductively, every
current non-base edge contains at least one previously inserted label
\(z\in\{t+1,\ldots,r-1\}\). This dichotomy includes all recursive child-edge
dominoes.

For a base split, write
\[
w=u+v,
\qquad
p=uv,
\qquad
A_t=tw-p.
\]
The elementary inequality \(p\le w^2/4\), followed by completing the square,
gives the \(\lambda\)-weighted local bound
\[
\begin{aligned}
{(w-S)^2\over2}+\lambda A_t
&\ge
{(w-S)^2\over2}+\lambda tw-{\lambda w^2\over4}\\
&=
{2-\lambda\over4}
\left(w-{2(S-\lambda t)\over2-\lambda}\right)^2
+G_{n,\lambda}(t),
\end{aligned}
\tag{CR28ay}
\]
where
\[
G_{n,\lambda}(t)
={\lambda(4St-S^2-2\lambda t^2)\over2(2-\lambda)}.
\tag{CR28az}
\]
For a recursive split, choose an inserted endpoint
\(z\in\{t+1,\ldots,r-1\}\); the other endpoint is at most \(n\). The exact
correction formula therefore gives
\[
\begin{aligned}
A_t
&=t^2-(u-t)(v-t)\\
&\ge
t^2-(r-1-t)(n-t)\\
&=(S-1)t-n(r-1).
\end{aligned}
\tag{CR28ba}
\]
Put
\[
J_{n,\lambda}(t)
=\lambda\bigl((S-1)t-n(r-1)\bigr).
\tag{CR28bb}
\]
Both local floors increase throughout the selected prefix:
\[
G_{n,\lambda}(t+1)-G_{n,\lambda}(t)
={\lambda[2S-\lambda(2t+1)]\over2-\lambda}\ge0,
\qquad
J_{n,\lambda}(t+1)-J_{n,\lambda}(t)=\lambda(S-1)\ge0.
\tag{CR28bc}
\]
The inequalities are strict when \(\lambda>0\). More strongly, direct
subtraction gives the finite identity
\[
J_{n,\lambda}(t)-G_{n,\lambda}(t)
=
{\lambda\bigl((n-r)^2+4(n-t)
+2\lambda(r-1-t)(n-t)\bigr)\over2(2-\lambda)}.
\]
It is positive for \(\lambda>0\) and \(t\le r-1\), while both floors vanish
for \(\lambda=0\). Consequently the exact local floor is
\[
F_n^{\mathrm{blk}}(\alpha,\beta,\lambda)
=\min\{G_{n,\lambda}(s),J_{n,\lambda}(s)\}
=G_{n,\lambda}(s),
\tag{CR28bd}
\]
where \(r=\lfloor\alpha n\rfloor\). Every selected split contributes at
least this floor after assigning the full quadratic slack plus
\(\lambda A_t\) to a base split, or \(\lambda A_t\) to a recursive split.

This assignment respects compatibility and uses each base slack at most
once. Discarding the nonnegative slack of unused base edges in (CR28ax)
therefore yields
\[
\begin{aligned}
P(C_0)+\lambda H_k-P_{r,n}
&\ge
\sum_{\substack{t:\ \text{base}\\\text{split}}}
\left[
{(u_t+v_t-S)^2\over2}+\lambda A_t
\right]
+
\sum_{\substack{t:\ \text{recursive}\\\text{split}}}
\lambda A_t\\
&\ge kF_n^{\mathrm{blk}}(\alpha,\beta,\lambda).
\end{aligned}
\tag{CR28be}
\]
The exact objective retains the maximum over *all* prefixes. In particular,
it retains both \(H_0=0\) and the selected \(H_k\), so
\[
\max_{0\le j\le r-1}H_j
\ge\max\{0,H_k\}
\ge\lambda H_k.
\tag{CR28bf}
\]
Equations (CR28be)--(CR28bf) hold for every compatible history, including
histories that repeatedly split recursive child edges. Minimizing therefore
proves the finite lower bound
\[
\boxed{
\gamma^{(r)}_{1,n}
\ge P_{r,n}+kF_n^{\mathrm{blk}}(\alpha,\beta,\lambda).
}
\tag{CR28bg}
\]

#### Exact coefficient and positive region

For fixed proof-admissible parameters,
\[
{G_{n,\lambda}(s)\over n^2}\longrightarrow
g(\alpha,\beta,\lambda)
=
{\lambda\bigl(4(1+\alpha)\beta-(1+\alpha)^2
-2\lambda\beta^2\bigr)\over2(2-\lambda)},
\]
\[
{J_{n,\lambda}(s)\over n^2}\longrightarrow
j(\alpha,\beta,\lambda)
=\lambda\bigl((1+\alpha)\beta-\alpha\bigr),
\qquad
{k\over n}\longrightarrow\alpha-\beta.
\]
The recursive branch is never active when \(\lambda>0\), because
\[
j-g
=
{\lambda\bigl((1-\alpha)^2
+2\lambda(\alpha-\beta)(1-\beta)\bigr)\over2(2-\lambda)}>0.
\]
The residual coefficient certified by (CR28bg) and the total coefficient
after adding the pairing floor are therefore
\[
c_{\rm res}(\alpha,\beta,\lambda)
=(\alpha-\beta)g(\alpha,\beta,\lambda),
\]
\[
\boxed{
\mathcal C(\alpha,\beta,\lambda)
=p(\alpha)+c_{\rm res}(\alpha,\beta,\lambda),
\qquad
p(\alpha)={(1-\alpha)(\alpha^2+4\alpha+1)\over6}.
}
\]
Here \(p(\alpha)\) is exactly the cubic coefficient of
\(P_{\lfloor\alpha n\rfloor,n}\).

The template produces a strictly positive cubic residual exactly on
\[
\boxed{
\begin{aligned}
\mathcal A_+
=\{(\alpha,\beta,\lambda):{}&
{1\over3}<\alpha<1,
\quad {1+\alpha\over4}<\beta<\alpha,
\quad 0<\lambda\le1,\\
&2\lambda\beta^2
<4(1+\alpha)\beta-(1+\alpha)^2\}.
\end{aligned}
}
\]
For fixed \(0<\lambda\le1\), this is equivalently
\[
\alpha>{1\over1+\sqrt{4-2\lambda}},
\qquad
{1+\alpha\over2+\sqrt{4-2\lambda}}<\beta<\alpha.
\]
This description includes the admissible part of the boundary \(\lambda=1\).
The condition \(\alpha>1/3\) is necessary and sufficient for some positive
choice to exist.

#### Complete maximin and boundary analysis

Optimize on the compact closure
\(0\le\beta\le\alpha\le1\), \(0\le\lambda\le1\). Direct differentiation
factors as
\[
{\partial\mathcal C\over\partial\lambda}
=
{(\alpha-\beta)(1+\alpha-\lambda\beta)
(4\beta-1-\alpha-\lambda\beta)\over(2-\lambda)^2}.
\]
The two numerator factors preceding the last parenthesis are nonnegative and
are strictly positive in the interior; the denominator is positive. Thus the
maximum in \(\lambda\), for fixed
\((\alpha,\beta)\), is
\[
\lambda_{\max}=
\begin{cases}
0,&0\le\beta\le(1+\alpha)/4,\\
4-(1+\alpha)/\beta,
  &(1+\alpha)/4<\beta<(1+\alpha)/3,\\
1,&(1+\alpha)/3\le\beta\le\alpha.
\end{cases}
\]
The last interval is nonempty only for \(\alpha\ge1/2\).

On the interior branch,
\[
\widehat{\mathcal C}(\alpha,\beta)
=p(\alpha)+{(\alpha-\beta)(1+\alpha-4\beta)^2\over2},
\]
and
\[
{\partial\widehat{\mathcal C}\over\partial\beta}
=-{(1+\alpha-4\beta)(9\alpha+1-12\beta)\over2}.
\]
Its unique maximizing point is
\[
\beta_0(\alpha)={9\alpha+1\over12},
\qquad
\lambda_0(\alpha)={8(3\alpha-1)\over9\alpha+1},
\]
and it belongs to this branch exactly when
\(1/3<\alpha<3/5\). At that point
\[
g_0(\alpha)={2(3\alpha-1)^2\over9},
\qquad
c_{{\rm res},0}(\alpha)={(3\alpha-1)^3\over54},
\]
so the one-variable envelope is
\[
\overline{\mathcal C}(\alpha)
={9\alpha^3-27\alpha^2+18\alpha+4\over27},
\qquad
\overline{\mathcal C}'(\alpha)
={3\alpha^2-6\alpha+2\over3},
\qquad
\overline{\mathcal C}''(\alpha)=2(\alpha-1)<0.
\]
It has the unique critical point
\[
\boxed{
\alpha_*=1-{\sqrt3\over3}.
}
\]
Substitution gives
\[
\boxed{
\beta_*={5\over6}-{\sqrt3\over4},
\qquad
\lambda_*={88-32\sqrt3\over73},
\qquad
\mathcal C_*={4+2\sqrt3\over27}.
}
\]
The corresponding local and residual coefficients are
\[
g_*={14-8\sqrt3\over9},
\qquad
c_{{\rm res},*}={26-15\sqrt3\over54},
\qquad
p(\alpha_*)={19\sqrt3-18\over54}.
\]
The optimization target here is the total \(\mathcal C=p+c_{\rm res}\), not
the residual summand by itself. For example, the admissible rational triple
\[
(\alpha,\beta,\lambda)=\left({4\over5},{3\over5},1\right)
\]
has
\[
g={9\over50},\qquad c_{\rm res}={9\over250}>
{26-15\sqrt3\over54},
\qquad
\mathcal C={74\over375}<\mathcal C_*.
\]
Thus \(c_{{\rm res},*}\) means the residual contribution at the unique
total-coefficient optimizer; it is not a claim of separate residual
optimality.

It remains to audit every boundary rather than infer globality from the
stationary equations. For \(0\le\alpha\le1/3\), no positive branch exists;
the envelope is \(p(\alpha)\), increasing to
\(p(1/3)=22/81\). On the \(\lambda=1\) branch,
\[
{\partial^2\mathcal C\over\partial\beta^2}
=-2(3\alpha-3\beta+2)<0,
\]
and the endpoint derivatives are
\[
\left.{\partial\mathcal C\over\partial\beta}\right|_
 {\beta=(1+\alpha)/3,\lambda=1}
={(1+\alpha)(5\alpha-3)\over6},
\qquad
\left.{\partial\mathcal C\over\partial\beta}\right|_
 {\beta=\alpha,\lambda=1}
=-{\,\alpha^2+2\alpha-1\,\over2}.
\]
Thus for \(1/2\le\alpha\le3/5\) this face is maximized at its lower
endpoint, already included in the closure of the interior branch. For
\(\alpha\ge3/5\), the endpoint signs and strict concavity put the unique
maximizing cutoff at
\[
\beta_1(\alpha)
=\alpha+{2\over3}-{\sqrt{6\alpha^2+12\alpha+10}\over6}.
\]
Along this envelope, the envelope theorem and direct differentiation give
\[
{d\mathcal C(\alpha,\beta_1(\alpha),1)\over d\alpha}
=-(\alpha-\beta_1)(2\alpha-3\beta_1+3)<0.
\]
It therefore decreases from
\(\overline{\mathcal C}(3/5)=878/3375\).

The remaining exterior faces introduce no hidden maximum. On
\(\lambda=0\), \(\beta=0\), \(\beta=\alpha\), or the frontier \(g=0\), the
value is at most
\[
p_{\max}={2(\sqrt2-1)\over3}.
\]
On the entire face \(\lambda=1\), holding \(\beta\) fixed gives
\[
{\partial\mathcal C\over\partial\alpha}
=-(\alpha-\beta)(2\alpha-3\beta+3)\le0,
\]
with strict inequality when \(\alpha>\beta\). Thus its value is below
\(p(\beta)\le p_{\max}\) unless
\(\alpha=\beta\). The endpoint envelopes give \(1/6\) at \(\alpha=0\) and
\((-34+14\sqrt7)/27\) at \(\alpha=1\). Finally,
\[
\mathcal C_*-p_{\max}
={2(11+\sqrt3-9\sqrt2)\over27}>0:
\]
indeed \(11+\sqrt3>9\sqrt2\) is equivalent after two positive squarings to
\(363>361\). Also
\[
\mathcal C_*-{22\over81}={6\sqrt3-10\over81}>0,
\qquad
\mathcal C_*-{878\over3375}={250\sqrt3-378\over3375}>0.
\]
This exhausts the compact boundary and proves that
\((\alpha_*,\beta_*,\lambda_*)\) is the unique global maximizer of the
generalized CR28ax--CR28bg template.

#### Explicit finite floor/ceiling form

For comparison with the exact inner-cycle reference, recall the alternating
cycle excess
\[
e(q)=
\begin{cases}
q(q-2)/8,&q\text{ even},\\
(q^2-1)/8,&q\text{ odd},
\end{cases}
\qquad
0\le e(q)\le{q^2\over8}.
\tag{CR28bh}
\]
Only the proved upper comparison
\(P^*_{r,n}\le P_{r,n}+e(q)\) is used; equality is not assumed. Hence
(CR28bg) gives the exact finite statement
\[
\boxed{
\gamma^{(r)}_{1,n}-P^*_{r,n}
\ge kF_n^{\mathrm{blk}}(\alpha,\beta,\lambda)-e(q).
}
\tag{CR28bi}
\]

At the unique optimizer, put
\[
r_n^*=\left\lfloor
\left(1-{\sqrt3\over3}\right)n
\right\rfloor,
\qquad
s_n^*=\left\lceil
\left({5\over6}-{\sqrt3\over4}\right)n
\right\rceil,
\qquad
k_n^*=r_n^*-s_n^*.
\tag{CR28bj}
\]
Define \(S_n^*=n+r_n^*\), \(q_n^*=n-r_n^*+1\), and
\[
F_n^*
=
{\lambda_*\left(
4S_n^*s_n^*-(S_n^*)^2-2\lambda_*(s_n^*)^2
\right)\over2(2-\lambda_*)}.
\]
The recursive floor
\[
\lambda_*\bigl((S_n^*-1)s_n^*-n(r_n^*-1)\bigr)
\]
exceeds \(F_n^*\) by the exact positive identity following (CR28bc).

The exact minimal uniform admissibility threshold is \(n\ge86\). Direct
evaluation gives
\[
\begin{array}{c|ccccc}
n&85&86&87&88&89\\ \hline
r_n^*&35&36&36&37&37\\
s_n^*&35&35&35&36&36,
\end{array}
\]
so \(n=85\) fails and \(86\le n\le89\) are admissible. For \(n\ge90\),
\[
k_n^*\ge(\alpha_*-\beta_*)n-2,
\qquad
\alpha_*-\beta_*={2-\sqrt3\over12},
\tag{CR28bk}
\]
and
\[
90(\alpha_*-\beta_*)-2={26-15\sqrt3\over2}>0,
\qquad
26^2-3\cdot15^2=1.
\]
Thus \(k_n^*\ge1\); the other block conditions are immediate. Equivalently,
the exact roundings can be evaluated without floating point as
\[
r_n^*=n-1-\left\lfloor{n\over\sqrt3}\right\rfloor,
\qquad
s_n^*=\left\lceil{10n-\lfloor3\sqrt3\,n\rfloor\over12}\right\rceil.
\]

For every \(n\ge86\), equations (CR28bg) and (CR28bi) now read
\[
\boxed{
\Lambda_n\ge\Gamma_n^{(r_n^*)}
\ge\gamma^{(r_n^*)}_{1,n}
\ge P_{r_n^*,n}+k_n^*F_n^*,
}
\]
\[
\boxed{
\gamma^{(r_n^*)}_{1,n}-P^*_{r_n^*,n}
\ge k_n^*F_n^*-e(q_n^*).
}
\]
These are literal floor/ceiling inequalities, not asymptotic shorthand and
not an identity for the residual.

There is also a clean polynomial consequence. Since \(\beta_*<1/2\),
\(G_{n,\lambda_*}(t)\) increases with \(t\) and decreases with \(S\) between
the actual \((S_n^*,s_n^*)\) and
\(((1+\alpha_*)n,\beta_*n)\). Hence
\[
F_n^*\ge g_*n^2.
\]
Combining this with (CR28bk) and \(e(q_n^*)\le n^2/8\) proves, for every
\(n\ge90\),
\[
\boxed{
\gamma^{(r_n^*)}_{1,n}-P^*_{r_n^*,n}
\ge
{26-15\sqrt3\over54}n^3
-{233-128\sqrt3\over72}n^2.
}
\tag{CR28bl}
\]
The displayed lower polynomial is positive for every \(n\ge441\), because
\[
441{26-15\sqrt3\over54}-{233-128\sqrt3\over72}
={15055-8692\sqrt3\over72}>0,
\]
and \(15055^2-3\cdot8692^2=433\). It is negative at \(n=440\), so 441 is
the exact positivity threshold of this coarse cubic--quadratic expression.

This proves a genuinely cubic *certified lower residual* for the selected
block. It does not identify the exact residual coefficient. It also does not
prove convergence, an exact leading coefficient, a production-enumeration
result, or a finite certificate artifact.

### Global corollary of the jointly optimized linear block

The passage to the global minimum does not exchange a maximum and a minimum.
For every admissible \(m\), define
\[
B_m(\sigma)
=\max_{0\le j\le r-1}P_\sigma(S_{m+j}).
\]
The induced tails in this block are among the subsets defining
\(\Lambda(\sigma)\), so pointwise in \(\sigma\),
\(\Lambda(\sigma)\ge B_m(\sigma)\). Minimizing this already ordered
inequality and then taking the maximum of the separately proved lower bounds
gives, on the exact finite domain \(n\ge86\),
\[
\boxed{
\Lambda_n
\ge\Gamma_n^{(r_n^*)}
\ge\gamma^{(r_n^*)}_{1,n}
\ge P_{r_n^*,n}+k_n^*F_n^*.
}
\tag{CR28bm}
\]
Here \(P_{r_n^*,n}\) is the duplicated-pairing floor, not the exact
simple-cycle minimum \(P^*_{r_n^*,n}\); the latter requires the separate
correction in (CR28bi).

The rounding of the pairing floor can be retained exactly. Put
\[
\eta_n=\alpha_*n-r_n^*\in[0,1).
\]
Then
\[
\begin{aligned}
P_{r_n^*,n}
={}&{19\sqrt3-18\over54}n^3\\
&+\left(\alpha_*+{7-4\sqrt3\over6}\eta_n\right)n^2\\
&-\left(
\left(1-{\sqrt3\over6}\right)\eta_n^2
+\eta_n+{\sqrt3\over18}
\right)n
+{\eta_n^3-\eta_n\over6}.
\end{aligned}
\tag{CR28bn}
\]
Since \(7-4\sqrt3>0\), the bracket multiplying \(-n\) is less than
two, and \((\eta_n^3-\eta_n)/6\ge-1/6\), this implies
\[
P_{r_n^*,n}
\ge {19\sqrt3-18\over54}n^3
+\alpha_*n^2-2n-{1\over6}.
\]
Together with \(k_n^*F_n^*\ge c_{{\rm res},*}n^3-2g_*n^2\), this proves
\[
\boxed{
\Lambda_n
\ge {4+2\sqrt3\over27}n^3
+{13\sqrt3-19\over9}n^2-2n-{1\over6}
\ge {4+2\sqrt3\over27}n^3
\quad(n\ge90).
}
\tag{CR28bo}
\]
The final inequality follows already from
\((13\sqrt3-19)/9>1/3\) and \(n\ge90\).

The strict global sandwich (CR27) therefore gives
\[
\boxed{
\begin{aligned}
R_2^*(n)
>{}&{4+2\sqrt3\over27\pi}n^3
+\left({13\sqrt3-19\over9\pi}-1\right)n^2\\
&-{2\over\pi}n-{1\over6\pi}
>{4+2\sqrt3\over27\pi}n^3-n^2
\qquad(n\ge90).
\end{aligned}
}
\tag{CR28bp}
\]
In particular,
\[
\boxed{
\liminf_{n\to\infty}{\Lambda_n\over n^3}
\ge {4+2\sqrt3\over27},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\ge {4+2\sqrt3\over27\pi}.
}
\tag{CR28bq}
\]
These are method-specific lower coefficients. They do not prove that either
normalized sequence converges, that either lower coefficient is exact, or
that the geometric leading constant exists.

Bounded exact test-local diagnostics check the algebra without entering the
proof. The quadratic identity (CR28ax) is checked on every dihedral cycle of
tail sizes three through six. At
\(n=86,90,141,200,500,1000\), deterministic histories that prefer intact
base edges and histories that force recursive child edges check the optimized
floor/ceiling arithmetic, every local contribution, the one-use base linkage,
the weighted-prefix step, and (CR28bi). At \(n=141\), a separate exhaustive
depth-two oracle checks all \(83\cdot84=6972\) literal histories from one
base cycle, including all 166 recursive child-edge second splits. A bounded
scan over every \(86\le n\le1000\) checks the exact finite formulas and the
uniform-domain boundary. These paths use only integer, rational, and exact
test-local \(\mathbb Q(\sqrt3)\) pair arithmetic and call no production
scorer, canonicalizer, or enumerator. The same arithmetic checks the optimizer
identities, coefficient decompositions, a bounded rational maximin grid, and
all decisive signs without floating point. In particular, it finds the exact
floor/ceil residual expression negative at \(n=175\) and positive throughout
\(176\le n\le440\); (CR28bl) then proves positivity for every \(n\ge441\).

### Two selected prefixes in one linear block

The same base-slack pool can support two selected prefixes, but it must be
charged only after the two prefix heights have been combined. Fix
\[
0<\beta_2<\beta_1<\alpha<1,
\qquad
0\le\lambda_{\rm lo}\le\lambda_{\rm hi}\le1,
\]
and put
\[
r=\lfloor\alpha n\rfloor,
\qquad
s_1=\lceil\beta_1n\rceil,
\qquad
s_2=\lceil\beta_2n\rceil.
\tag{CR28br}
\]
At fixed \(n\), require
\[
2\le r\le n-2,
\qquad
1\le s_2<s_1\le r-1.
\]
For one arbitrary compatible history in (CR28au), denote the two selected
prefix heights by
\[
H_1=\sum_{t=s_1}^{r-1}A_t,
\qquad
H_2=\sum_{t=s_2}^{r-1}A_t.
\]
The exact objective retains \(0,H_1,H_2\). Since
\(1-\lambda_{\rm hi}\),
\(\lambda_{\rm hi}-\lambda_{\rm lo}\), and
\(\lambda_{\rm lo}\) are nonnegative and sum to one, use exactly
\[
\boxed{
\max(0,H_1,H_2)\ge
(\lambda_{\rm hi}-\lambda_{\rm lo})H_1
+\lambda_{\rm lo}H_2.
}
\tag{CR28bs}
\]
Expanding the right-hand side *before charging any edge* gives
\[
(\lambda_{\rm hi}-\lambda_{\rm lo})H_1
+\lambda_{\rm lo}H_2
=
\lambda_{\rm hi}\sum_{t=s_1}^{r-1}A_t
+\lambda_{\rm lo}\sum_{t=s_2}^{s_1-1}A_t.
\]
Thus the first segment uses weight \(\lambda_{\rm hi}\), and the second
uses weight \(\lambda_{\rm lo}\).

For \(i=1,2\), set
\[
(\lambda_1,b_1)=(\lambda_{\rm hi},s_1),
\qquad
(\lambda_2,b_2)=(\lambda_{\rm lo},s_2),
\qquad
F_{i,n}=G_{n,\lambda_i}(b_i),
\]
where \(G\) is (CR28az). On either segment, (CR28ay)--(CR28bc)
apply with that segment's weight. Hence an intact original-base split at
label \(t\) contributes at least
\(G_{n,\lambda_i}(t)\ge F_{i,n}\) after receiving its edge slack, while a
recursive split contributes at least
\(J_{n,\lambda_i}(t)\ge G_{n,\lambda_i}(t)\ge F_{i,n}\).

Here is the charging audit across the segment boundary. Let
\(\Delta_e=(u+v-n-r)^2/2\) for an original base edge
\(e=\{u,v\}\). Every selected split is either the first split of an intact
original edge or a recursive current-edge split. The map from base splits to
original edges is injective across *both* segments: after splitting \(e\),
its two children contain the inserted label and no later operation recreates
an edge with the same two original endpoints. Conversely, every recursive
edge contains a previously inserted endpoint in
\(\{t+1,\ldots,r-1\}\), even when a low-segment split recursively follows a
high-segment split. Therefore the endpoint argument in (CR28ba) covers every
recursive child edge. With \(\lambda_t\) denoting the weight of the segment
containing \(t\), the exact partition is
\[
\begin{aligned}
P(C_0)-P_{r,n}+\sum_{t=s_2}^{r-1}\lambda_tA_t
={}&
\sum_{\substack{t:\ \text{base}\\\text{split}}}
  (\Delta_{e_t}+\lambda_tA_t)
+\sum_{\substack{t:\ \text{recursive}\\\text{split}}}
  \lambda_tA_t
+\sum_{e\text{ unused by the selected prefixes}}\Delta_e.
\end{aligned}
\tag{CR28bt}
\]
Every original base slack occurs exactly once on the right: either beside
its unique split or in the unused sum. This is the promised one-use result.
Applying two separately slack-charged copies of (CR28be) would instead reuse
the same base-slack pool and is invalid.

Discarding only the nonnegative unused sum in (CR28bt), then using (CR28bs),
proves for every compatible history
\[
\boxed{
\gamma^{(r)}_{1,n}
\ge
P_{r,n}+(r-s_1)F_{1,n}+(s_1-s_2)F_{2,n}.
}
\tag{CR28bu}
\]
The exact inner-cycle comparison remains separate:
\[
\boxed{
\gamma^{(r)}_{1,n}-P^*_{r,n}
\ge
(r-s_1)F_{1,n}+(s_1-s_2)F_{2,n}-e(n-r+1).
}
\tag{CR28bv}
\]
No recursive split has been replaced by a base-edge choice in either formula.

Let
\[
g(\alpha,\beta,\lambda)
=
{\lambda\left(4(1+\alpha)\beta-(1+\alpha)^2
-2\lambda\beta^2\right)\over2(2-\lambda)}
\]
as above. Dividing (CR28bu) by \(n^3\) and taking the fixed-parameter
limit gives the certified total coefficient
\[
\boxed{
C_2
=p(\alpha)
+(\alpha-\beta_1)g(\alpha,\beta_1,\lambda_{\rm hi})
+(\beta_1-\beta_2)g(\alpha,\beta_2,\lambda_{\rm lo}).
}
\tag{CR28bw}
\]
The charging derivation itself does not optimize the five parameters.  That
optimization can nevertheless be completed exactly without changing any
part of the charging proof.

#### Exact ordered-weight reduction

Put \(s=1+\alpha\), \(L=s/4\), and \(U=s/3\).  For fixed
\((\alpha,\beta)\), write
\(g_\beta(\lambda)=g(\alpha,\beta,\lambda)\).
Direct differentiation gives
\[
g_\beta'(\lambda)
=
{(s-\lambda\beta)(4\beta-s-\lambda\beta)
 \over(2-\lambda)^2},
\qquad
g_\beta''(\lambda)
=-{2(s-2\beta)^2\over(2-\lambda)^3}<0.
\tag{CR28bw1}
\]
The last inequality is strict on the density domain because
\(s-2\beta>1-\alpha>0\).  Hence the unique maximum on \([0,1]\) is
\[
\psi_s(\beta)
=
\begin{cases}
0,&0\le\beta\le L,\\
4-s/\beta,&L<\beta<U,\\
1,&U\le\beta.
\end{cases}
\tag{CR28bw2}
\]
This function is nondecreasing.  Therefore
\(\beta_2<\beta_1\) implies
\(\psi_s(\beta_2)\le\psi_s(\beta_1)\): the two separate maxima already
satisfy the prescribed order
\(\lambda_{\rm lo}\le\lambda_{\rm hi}\).  Strict concavity shows that no
pooled KKT branch on the open diagonal has been lost.

Substitution gives the exact reduced floor
\[
\Phi_s(\beta)
:=\max_{0\le\lambda\le1}g_\beta(\lambda)
=
\begin{cases}
0,&0\le\beta\le L,\\[2mm]
(4\beta-s)^2/2,&L\le\beta\le U,\\[2mm]
(4s\beta-s^2-2\beta^2)/2,&U\le\beta.
\end{cases}
\tag{CR28bw3}
\]
The values and first derivatives agree at \(L\) and \(U\).  Thus the ordered
weight optimization reduces CR28bw exactly to
\[
\overline C_2
=p(\alpha)+(\alpha-\beta_1)\Phi_s(\beta_1)
 +(\beta_1-\beta_2)\Phi_s(\beta_2).
\tag{CR28bw4}
\]

There are exactly six ordered weight branches.  In the table, \(M\) means
the middle expression in (CR28bw2), while \(H\) means the saturated value
one.

| branch | density region | \((\lambda_{\rm hi},\lambda_{\rm lo})\) |
|---|---|---|
| `00` | \(\beta_1\le L\) | \((0,0)\) |
| `M0` | \(\beta_2\le L<\beta_1<U\) | \((4-s/\beta_1,0)\) |
| `H0` | \(\beta_2\le L\), \(U\le\beta_1\) | \((1,0)\) |
| `MM` | \(L<\beta_2<\beta_1<U\) | \((4-s/\beta_1,4-s/\beta_2)\) |
| `HM` | \(L<\beta_2<U\le\beta_1\) | \((1,4-s/\beta_2)\) |
| `HH` | \(U\le\beta_2\) | \((1,1)\) |

Consequently the three vertices of the ordered weight triangle are exactly
`00`, `H0`, and `HH`; its two non-diagonal open edges are `M0` and `HM`;
and `MM` is its interior.  There is no optimizer with
\(0<\lambda_{\rm lo}=\lambda_{\rm hi}<1\).  The only diagonal optima for
positive segment lengths are the clipped vertices \((0,0)\) and \((1,1)\).
Indeed the two feasible one-sided normal directions on an open diagonal
would require
\[
g_{\beta_1}'(\lambda)\le0,
\qquad
g_{\beta_2}'(\lambda)\ge0,
\]
hence
\(\lambda\ge\psi_s(\beta_1)>\psi_s(\beta_2)\ge\lambda\) unless both
individual optima are clipped to the same endpoint.  A stationary point of
the *restricted* diagonal can therefore exist, but it always has an
improving direction in the full ordered triangle and is not a KKT branch of
CR28bw.
The transition faces are
\(\beta_i=L\), where the corresponding weight is zero, and
\(\beta_i=U\), where it is one.

#### All remaining density branches and transitions

The density classification is cleanest after the normalization
\[
\tau={\alpha\over1+\alpha},
\qquad
x_i={\beta_i\over1+\alpha},
\qquad
0\le x_2\le x_1\le\tau\le{1\over2}.
\]
Then the residual part of (CR28bw4) is
\[
(1+\alpha)^3V_\tau(x_1,x_2),
\qquad
V_\tau=(\tau-x_1)\phi(x_1)+(x_1-x_2)\phi(x_2),
\tag{CR28bw5}
\]
where
\[
\phi(x)=
\begin{cases}
0,&x\le1/4,\\
(4x-1)^2/2,&1/4\le x\le1/3,\\
-x^2+2x-1/2,&x\ge1/3.
\end{cases}
\]

For fixed \(x_1\), first maximize
\((x_1-x_2)\phi(x_2)\).  Its unique positive optimizer is
\[
z(x_1)=
\begin{cases}
(8x_1+1)/12,&1/4<x_1<3/8,\\[1mm]
\displaystyle
{2x_1+4-\sqrt{4x_1^2-8x_1+10}\over6},
&3/8\le x_1\le1/2.
\end{cases}
\tag{CR28bw6}
\]
At \(x_1=3/8\), both formulas give \(z=1/3\).  This follows by solving
\((x_1-z)\phi'(z)=\phi(z)\).  On the middle piece its derivative has one
zero; on the high piece it is strictly decreasing, so no second maximum is
hidden.

Substitute \(x_2=z(x_1)\) and optimize in \(x_1\).  On the `MM` branch the
outer derivative factors as
\[
{(4x_1-1)(72\tau+5-92x_1)\over18}.
\]
On the `HM` branch its zero is equivalently
\[
\tau
={-118x_1^2+104x_1-13\over36(1-x_1)},
\qquad
x_2={8x_1+1\over12}.
\tag{CR28bw7}
\]
The right-hand side is strictly increasing on
\(1/3<x_1<3/8\).  The endpoint values are \(77/216\) and \(301/720\).
If \(F(x_1)\) denotes that right-hand side, the outer derivative is
\[
2(1-x_1)\bigl(\tau-F(x_1)\bigr).
\]
It therefore changes sign from positive to negative at the unique zero, so
the `HM` stationary point is the regional maximum.

On `HH`, put
\[
u=1-x_1,
\qquad v=1-x_2,
\qquad h=1-\tau.
\]
The two stationary equations are exactly
\[
6v^2-4uv-1=0,
\qquad
3u^2-2hu-v^2=0.
\tag{CR28bw8}
\]
The positive first root is
\[
v(u)={u+\sqrt{u^2+3/2}\over3}.
\]
The function
\[
H(u)={3u^2-v(u)^2\over2u}
\]
is strictly increasing on \(1/2<u<5/8\), because
\[
H'(u)
=
{(50u^2+3)\sqrt{2u^2+3}-4\sqrt2\,u^3
 \over36u^2\sqrt{2u^2+3}}>0.
\]
Indeed \(\sqrt{2u^2+3}>\sqrt2\,u\) and
\(50u^2+3>4u^2\).  Moreover,
\[
H(1/2)={19\over36}-{\sqrt7\over18}<{1\over2},
\qquad
H(5/8)={419\over720}.
\]
Hence \(H(u)=h\) gives exactly one `HH` stationary point for every
\(301/720<\tau<1/2\).  Equations (CR28bw6)--(CR28bw8),
not a numerical solver, classify that entire later branch.  On the inner
best response, the outer derivative is
\[
2u\bigl(H(u)-h\bigr).
\]
As \(x_1\) increases, \(u=1-x_1\) and hence \(H(u)\) decrease.  The sign
again changes from positive to negative, so this unique point is the
regional maximum.

The complete fixed-\(\alpha\) maximizing-branch sequence is therefore
\[
\begin{array}{c|c|c}
\text{range of }\alpha&\text{range of }\tau&\text{branch}\\ \hline
0\le\alpha\le1/3&0\le\tau\le1/4&00\\
1/3<\alpha<77/139&1/4<\tau<77/216&MM\\
77/139<\alpha<301/419&77/216<\tau<301/720&HM\\
301/419<\alpha<1&301/720<\tau<1/2&HH.
\end{array}
\tag{CR28bw9}
\]
For \(\tau\le1/4\), the value is unique but the density pair is not: the
whole triangle \(0\le x_2\le x_1\le\tau\) has zero residual.  For
\(\tau>1/4\), the maximizing density pair is unique, including at both
branch junctions.
At the first transition,
\((x_1,x_2)=(1/3,11/36)\); at the second,
\((x_1,x_2)=(3/8,1/3)\).  The adjacent formulas join there.  At
\(\alpha=1/3\), the positive branch is born at the closure collision
\(x_1=x_2=\tau=1/4\).
In the original variables, the two nontrivial junctions are
\[
\left(
{\alpha},{\beta_1},{\beta_2},
{\lambda_{\rm hi}},{\lambda_{\rm lo}}
\right)
=
\left({77\over139},{72\over139},{66\over139},1,{8\over11}\right)
\]
and
\[
\left(
{\alpha},{\beta_1},{\beta_2},
{\lambda_{\rm hi}},{\lambda_{\rm lo}}
\right)
=
\left({301\over419},{270\over419},{240\over419},1,1\right).
\]
The `MM`, `HM`, and `HH` interior stationary families exist exactly on the
three open intervals shown in (CR28bw9); outside those intervals, the
corresponding regional maximum lies on the adjacent transition face.

For completeness, the nonwinning active strata `M0` and `H0` are precisely
the old one-prefix stationary branches.  In the interior of `M0`,
\[
\beta_1={9\alpha+1\over12},
\qquad
\lambda_{\rm hi}={8(3\alpha-1)\over9\alpha+1},
\qquad {1\over3}<\alpha<{3\over5};
\]
for \(\alpha\ge3/5\), its regional maximum is on the closure
\(\beta_1=U\).  On `H0`, that same closure is active for
\(1/2\le\alpha\le3/5\), while its interior stationary family for
\(\alpha>3/5\) is
\[
\beta_1
=\alpha+{2\over3}
-{\sqrt{6\alpha^2+12\alpha+10}\over6},
\qquad
\lambda_{\rm hi}=1,
\qquad {3\over5}<\alpha<1.
\]
They join at \(\alpha=3/5\), \(\beta_1=U\).  The low cutoff is flat on
these strata, but they are never the fixed-\(\alpha\) two-prefix maximum:
as soon as \(x_1>1/4\), (CR28bw6) has \(z(x_1)>1/4\) and adds a strictly
positive second contribution.  Together with `00`, `MM`, `HM`, and `HH`,
this exhausts every smooth density branch.

#### Global upper envelope and exact maximizer

The preceding branch classification can be compared globally without
solving the radicals on `HM` or `HH`.  If \(\alpha\le1/3\), every allowed
cutoff is at most \(L\), so the reduced coefficient is just \(p(\alpha)\).
Here \(p'(\alpha)=(1-2\alpha-\alpha^2)/2>0\), so
\(p(\alpha)\le p(1/3)=22/81<C_{2,*}\).
Suppose \(\alpha>1/3\), and put \(A=3\alpha-1>0\).  For every active cutoff,
\[
\Phi_s(\beta)\le{(4\beta-s)^2\over2},
\tag{CR28bw10}
\]
Indeed the middle expression minus the high expression is
\((3\beta-s)^2\).  Thus (CR28bw10) has equality on the middle branch and
strict inequality above \(U\).
For two active cutoffs set
\(X=4\beta_1-s\) and \(Y=4\beta_2-s\).  If the second cutoff is inactive,
set \(Y=0\) and omit its zero term; if both are inactive, the residual is
zero.  In either active case,
\[
0\le Y\le X\le A,
\]
and the total residual is at most
\[
{(A-X)X^2+(X-Y)Y^2\over8}.
\tag{CR28bw11}
\]
Writing \(r=X/A\) and \(q=Y/A\), first maximize in \(q\):
\[
\max_{0\le q\le r}(r-q)q^2={4r^3\over27},
\qquad q={2r\over3}.
\]
The remaining function is
\(r^2(1-23r/27)\), whose unique maximum on \([0,1]\) is
\[
{108\over529}
\quad\text{at}\quad
(r,q)=\left({18\over23},{12\over23}\right).
\]
Consequently every point in the compact density closure satisfies
\[
\overline C_2\le
E(\alpha)
:=p(\alpha)+{27(3\alpha-1)^3\over1058}
={829\alpha^3-1887\alpha^2+1158\alpha+224\over1587}
\tag{CR28bw12}
\]
when \(\alpha\ge1/3\).  Moreover,
\[
E'(\alpha)={829\alpha^2-1258\alpha+386\over529}.
\]
Its roots are
\[
{629\mathbin\pm23\sqrt{143}\over829}.
\]
The plus root exceeds one.  The minus root lies strictly between \(1/3\)
and \(1/2\), hence inside the `MM` validity interval
\((1/3,77/139)\).  Thus the relaxation is attained there rather than merely
bounding the true piecewise envelope.

The exact global maximizer is
\[
\boxed{
\begin{aligned}
\alpha_*&={629-23\sqrt{143}\over829},\\
\beta_{1,*}&={2286-77\sqrt{143}\over3316},\\
\beta_{2,*}&={2010-59\sqrt{143}\over3316},\\
\lambda_{{\rm hi},*}&={6264-288\sqrt{143}\over5281},\\
\lambda_{{\rm lo},*}&={3888-192\sqrt{143}\over4273}.
\end{aligned}
}
\tag{CR28bw13}
\]
Equivalently, along the full `MM` stationary family,
\[
\beta_1={5+77\alpha\over92},
\qquad
\beta_2={11+59\alpha\over92},
\]
\[
\lambda_{\rm hi}={72(3\alpha-1)\over77\alpha+5},
\qquad
\lambda_{\rm lo}={48(3\alpha-1)\over59\alpha+11}.
\]
The simplex maximum, the relevant root of \(E'\), and both strictly concave
weight maxima are unique.  Hence (CR28bw13) is the only maximizer in the
original strict domain.

The exact optimized coefficient is
\[
\boxed{
C_{2,*}
={491596+6578\sqrt{143}\over2061723}
=0.276592655350947\ldots
}
\tag{CR28bw14}
\]
and it satisfies the independent quadratic equation
\[
6185169C_{2,*}^2-2949576C_{2,*}+342644=0.
\]
The five decimal coordinates are
\[
(0.426972259238\ldots,
 0.411705043058\ldots,
 0.393384383642\ldots,
 0.533993733381\ldots,
 0.372575225211\ldots),
\]
so the proposed numerical point is recovered rather than assumed.

#### Boundary and collision audit

It remains to make explicit why the compact closure introduces no additional
maximizer.

- On \(\alpha=0\), all densities collide and the value is \(p(0)=1/6\).
  On \(\alpha=1\), the unique maximizing density pair is the `HH` solution
  of (CR28bw8) with \(h=1/2\).  Equivalently, \(u\) is the unique root in
  \((1/2,5/8)\) of
  \[
  276u^4-200u^3+12u+1=0,
  \]
  after which \(v=v(u)\), \(x_1=1-u\), and \(x_2=1-v\).  In particular,
  the coarser bound (CR28bw12) gives \(C_2\le108/529\) on this face.
- Each density face
  \(\beta_1=\alpha\), \(\beta_2=\beta_1\), or \(\beta_2=0\) deletes one
  residual term and reduces exactly to the already optimized one-prefix
  coefficient.  Its maximum is \((4+2\sqrt3)/27<C_{2,*}\).  Intersections
  of these faces reduce further to the pairing term.
- On \(\beta_1=\alpha\), the maximizing low weight is
  \(\psi_s(\beta_2)\), while the unused high weight may be any value in
  \([\lambda_{\rm lo},1]\).  On \(\beta_2=\beta_1\), the maximizing high
  weight is \(\psi_s(\beta_1)\), while the unused low weight may be any
  value in \([0,\lambda_{\rm hi}]\).  If all three densities collide, every
  ordered weight pair is irrelevant.  These are nonunique parametrizations
  of strictly smaller collision-face values, not extra global maximizers.
- On \(\beta_2=0\) with positive second-segment length, the unique low
  weight is zero.  The remaining high weight is the one-prefix optimum.
- The internal transition faces \(\beta_i=L,U\) are already included because
  both \(\Phi_s\) and its first derivative join there.  The ordered-weight
  table above classifies every pointwise unrestricted weight optimum.  The
  restricted order-diagonal face is treated separately below.

The exact closure maxima of the six reduced branches are
\[
\begin{array}{c|cccccc}
\text{branch}&00&M0&H0&MM&HM&HH\\ \hline
\max C_2&
{2(\sqrt2-1)\over3}&
{4+2\sqrt3\over27}&
{13\over48}&
C_{2,*}&
{59\over216}&
{13\over48}.
\end{array}
\tag{CR28bw15}
\]
For `00` and `M0`, these are respectively the pairing and one-prefix
envelopes already differentiated above.  Direct differentiation on the high
pieces gives the remaining three non-`MM` values: `H0` decreases from its
\(\alpha=1/2\) collision value; along `HM`,
\[
{dC_2\over d\alpha}
\le {5\alpha^2-17\alpha+5\over27}<0,
\]
and along `HH`,
\[
{dC_2\over d\alpha}
\le {\alpha^2-4\alpha+1\over6}<0.
\]
Thus `HM` and `HH` decrease from their respective closure values
\(59/216\) and \(13/48\).  The transition surfaces themselves have maxima
\[
\begin{array}{c|cccc}
\text{surface}&\beta_1=L&\beta_2=L&\beta_1=U&\beta_2=U\\ \hline
\max C_2&
{2(\sqrt2-1)\over3}&
{4+2\sqrt3\over27}&
{59\over216}&
{13\over48}.
\end{array}
\tag{CR28bw16}
\]
All five non-`MM` values are separated from the global coefficient by the
single rational number \(553/2000\).  The comparisons use only integers:
\[
C_{2,*}>{553\over2000},
\qquad
143(13156000)^2-(156940819)^2
=120067379609239>0,
\]
\[
{4+2\sqrt3\over27}<{553\over2000},
\qquad
6931^2-3(4000)^2=38761>0,
\]
\[
{2(\sqrt2-1)\over3}<{553\over2000},
\qquad
5659^2-2(4000)^2=24281>0.
\]
The rational comparisons
\(59/216<553/2000\) and \(13/48<553/2000\) are immediate.

The three boundary faces of the ordered weight triangle require one final
distinction from the pointwise optimal-branch table.  On
\(\lambda_{\rm lo}=0\), the low term vanishes and the exact face maximum is
the one-prefix value \((4+2\sqrt3)/27\).  On
\(\lambda_{\rm hi}=1\), direct differentiation gives
\[
{\partial C_2\over\partial\alpha}
=-(\alpha-\beta_1)(2\alpha-3\beta_1+3)
+(\beta_1-\beta_2)
 {\lambda_{\rm lo}(2\beta_2-1-\alpha)\over2-\lambda_{\rm lo}}
\le0.
\]
Lowering \(\alpha\) to the collision \(\alpha=\beta_1\) therefore reduces
this closure face again to the one-prefix maximum.  On the order face
\(\lambda_{\rm lo}=\lambda_{\rm hi}\), equality with \(C_{2,*}\) would
force the unique densities in (CR28bw13), but termwise equality in
(CR28bw3) would then require the one common weight to equal two distinct
middle optima.  Hence the compact diagonal face is strictly below
\(C_{2,*}\).  Its endpoint intersections \((0,0)\) and \((1,1)\) have the
pairing maximum \(2(\sqrt2-1)/3\).

For an entirely exact comparison with the prior rational witness,
\[
C_{2,*}-{72825421\over263424000}
={-6882553585461+577601024000\sqrt{143}
  \over181035773184000}>0,
\]
because
\[
143(577601024000)^2-(6882553585461)^2
=338536981654279737417479>0.
\]
Thus every boundary and collision face is strictly below the unique interior
point.  This completes the global optimization of CR28bw itself.  It does
not identify an exact block residual, prove convergence, or determine the
geometric leading coefficient.

Because the optimizer (CR28bw13) lies strictly in the proof-valid domain,
the fixed-parameter limit of (CR28bu) gives the sharpened asymptotic
corollary
\[
\boxed{
\liminf_{n\to\infty}{\Lambda_n\over n^3}
\ge C_{2,*},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\ge {C_{2,*}\over\pi}.
}
\tag{CR28bw17}
\]
No finite floor/ceiling rounding of the irrational two-prefix optimizer is
asserted here. The rational specialization below remains the explicit finite
theorem within the two-prefix branch.

#### Exact rational witness and finite threshold

Take the proposed witness
\[
(\alpha,\beta_1,\beta_2,
  \lambda_{\rm hi},\lambda_{\rm lo})
=\left({3\over7},{2\over5},{3\over8},{1\over2},{1\over4}\right).
\]
It lies strictly in the required density region and satisfies the weight
ordering. Exact substitution gives
\[
p(3/7)={284\over1029},
\qquad
g(3/7,2/5,1/2)={52\over3675},
\qquad
g(3/7,3/8,1/4)={199\over87808}.
\]
The corresponding recursive limits are \(1/14\) and \(3/112\), exceeding
the two base floors by \(421/7350\) and \(2153/87808\), respectively.
Therefore
\[
\boxed{
C_2={72825421\over263424000}.
}
\tag{CR28bx}
\]
The comparison with the previous one-prefix optimum is exact. Put
\[
x={27C_2-4\over2}={304196789\over175616000}>0.
\]
Then
\[
x^2-3
={12748069910521\over30840979456000000}>0,
\]
so \(x>\sqrt3\) and hence
\[
C_2>{4+2\sqrt3\over27}.
\]

For the finite theorem, define
\[
r_n=\left\lfloor{3n\over7}\right\rfloor,
\qquad
s_{1,n}=\left\lceil{2n\over5}\right\rceil,
\qquad
s_{2,n}=\left\lceil{3n\over8}\right\rceil,
\qquad
S_n=n+r_n,
\]
and
\[
F_{1,n}={4S_ns_{1,n}-S_n^2-s_{1,n}^2\over6},
\qquad
F_{2,n}={8S_ns_{2,n}-2S_n^2-s_{2,n}^2\over28}.
\tag{CR28by}
\]
The uniform admissibility threshold is exactly \(n\ge59\). Indeed, the
rational denominators give
\[
r_n-s_{1,n}\ge{n-58\over35},
\qquad
s_{1,n}-s_{2,n}\ge{n-35\over40}.
\]
Both left sides are integers and are therefore at least one for \(n\ge59\);
the other block conditions are immediate. At \(n=58\), however,
\((r_n,s_{1,n},s_{2,n})=(24,24,22)\), so the first selected segment is
empty. Thus 59 is minimal for a uniform two-nonempty-prefix statement.

For every \(n\ge59\), (CR28bu) and the pointwise global comparison give
\[
\boxed{
\Lambda_n
\ge\Gamma_n^{(r_n)}
\ge\gamma^{(r_n)}_{1,n}
\ge P_{r_n,n}
 +(r_n-s_{1,n})F_{1,n}
 +(s_{1,n}-s_{2,n})F_{2,n}.
}
\tag{CR28bz}
\]
This is the requested literal floor/ceiling theorem.

For completeness, the rounding can be retained in a simple polynomial. On
this domain \(2s_{i,n}<S_n\). Since \(G_{n,\lambda}(t)\) increases in
\(t\), decreases in \(S\) there, \(S_n\le10n/7\), and
\(s_{i,n}\ge\beta_i n\),
\[
F_{1,n}\ge{52\over3675}n^2,
\qquad
F_{2,n}\ge{199\over87808}n^2.
\]
Together with the two exact length estimates this yields
\[
(r_n-s_{1,n})F_{1,n}
+(s_{1,n}-s_{2,n})F_{2,n}
\ge
{121421\over263424000}n^3
-{6699143\over263424000}n^2.
\]
If \(\eta_n=3n/7-r_n\), then
\(\eta_n\in\{0,1/7,\ldots,6/7\}\), and exact expansion gives
\[
\begin{aligned}
P_{r_n,n}
={}&{284\over1029}n^3
+\left({3\over7}+{\eta_n\over49}\right)n^2\\
&-\left({5\eta_n^2\over7}+\eta_n+{2\over21}\right)n
+{\eta_n^3-\eta_n\over6}.
\end{aligned}
\]
The linear bracket is at most \(1520/1029\), and the seven exact constant
values are at least \(-22/343\). Consequently
\[
\boxed{
\Lambda_n
\ge
{72825421\over263424000}n^3
+{106196857\over263424000}n^2
-{1520\over1029}n-{22\over343}
\ge
{72825421\over263424000}n^3
\quad(n\ge59).
}
\tag{CR28ca}
\]
For the last inequality, the quadratic coefficient exceeds \(2/5\), while
\(1520/1029<3/2\) and \(22/343<1\); the remaining correction is already
positive for every integer \(n\ge5\).

The residual comparison (CR28bv) and \(e(q)\le n^2/8\) also give
\[
\gamma^{(r_n)}_{1,n}-P^*_{r_n,n}
\ge
{121421\over263424000}n^3
-{39627143\over263424000}n^2,
\]
whose right-hand side is positive for \(n\ge327\). This is a certified
residual lower bound, not the exact residual or its exact coefficient.

Finally, the strict cyclic-ratio sandwich turns (CR28ca) into
\[
\boxed{
R_2^*(n)
>{72825421\over263424000\pi}n^3-n^2
\qquad(n\ge59),
}
\tag{CR28cb}
\]
and therefore
\[
\boxed{
\liminf_{n\to\infty}{\Lambda_n\over n^3}
\ge{72825421\over263424000},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\ge{72825421\over263424000\pi}.
}
\tag{CR28cc}
\]
These remain the explicit finite-\(n\) improvement over the one-prefix
theorem. The optimized two-prefix asymptotic coefficient is (CR28bw14), while
(CR28bw17) supersedes these two liminf inequalities within that template.
Neither statement
asserts convergence, an exact leading coefficient, or a matching upper bound.

Independent test-local `Fraction` diagnostics exercise both the valid and
invalid charging routes. At \(n=59\), all
\(35\cdot36=1{,}260\) literal depth-two histories from one base cycle are
checked; exactly 70 have a recursive second split. Every history passes the
literal edge update, one-use base-edge map, two local floors, combined
weighted identity, and selected-prefix maximum. A separate \(n=100\) domino
splits \(\{t+1,t+2\}\) through the high/low boundary, including low-segment
edges whose two endpoints were both inserted earlier. Deterministic all-base
and recursive policies are also checked at \(n=59,100,200,1000\). An
explicit negative regression shows that two separately charged prefix
inequalities overdraw one base edge by exactly its slack. Finally, exact
rational scans through \(n=1000\) check the floor/ceiling threshold,
coefficient, finite polynomial, and the coarse residual sign change between
326 and 327. These bounded computations corroborate the bookkeeping and
arithmetic; the all-\(n\) statements rest on the written proof and use no
production scorer, canonicalizer, or enumerator.

### Three selected prefixes in one linear block

The preceding one-use argument extends to three selected prefixes, provided
that all three heights are combined before any base slack is assigned. Fix

\[
0<\beta_3<\beta_2<\beta_1<\alpha<1,
\qquad
0\le\lambda_3\le\lambda_2\le\lambda_1\le1,
\]

and put

\[
r=\lfloor\alpha n\rfloor,
\qquad
s_i=\lceil\beta_i n\rceil\quad(i=1,2,3).
\tag{CR28cd}
\]

At fixed \(n\), require

\[
2\le r\le n-2,
\qquad
1\le s_3<s_2<s_1\le r-1.
\]

For one arbitrary compatible split history, let

\[
H_i=\sum_{t=s_i}^{r-1}A_t\quad(i=1,2,3).
\]

The four numbers

\[
1-\lambda_1,
\quad\lambda_1-\lambda_2,
\quad\lambda_2-\lambda_3,
\quad\lambda_3
\]

are nonnegative and sum to one. Therefore the exact prefix objective gives

\[
\boxed{
\max(0,H_1,H_2,H_3)
\ge
(\lambda_1-\lambda_2)H_1
+(\lambda_2-\lambda_3)H_2
+\lambda_3H_3.
}
\tag{CR28ce}
\]

Expanding this linear form before charging gives

\[
\lambda_1\sum_{t=s_1}^{r-1}A_t
+\lambda_2\sum_{t=s_2}^{s_1-1}A_t
+\lambda_3\sum_{t=s_3}^{s_2-1}A_t.
\]

Thus the three disjoint split segments carry the three ordered weights. Put

\[
F_{i,n}=G_{n,\lambda_i}(s_i)\quad(i=1,2,3),
\]

with \(G\) as in (CR28az). On segment \(i\), an intact original-base
split at \(t\) receives its unique slack and contributes at least
\(G_{n,\lambda_i}(t)\ge F_{i,n}\). A recursive split contributes at least
\(J_{n,\lambda_i}(t)\ge G_{n,\lambda_i}(t)\ge F_{i,n}\).

The recursive invariant used here is independent of the number of segment
boundaries crossed. At the moment label \(t\) is inserted, every current
edge is either an untouched original base edge or contains a previously
inserted label in \(\{t+1,\ldots,r-1\}\). Splitting an edge preserves that
dichotomy for every later label. Hence (CR28ba) covers arbitrarily nested
child edges, including edges whose two endpoints were inserted earlier and
histories crossing both selected-prefix boundaries.

Let \(\lambda_t\) be the weight of the segment containing \(t\), and retain
\(\Delta_e=(u+v-n-r)^2/2\) for an original edge \(e=\{u,v\}\). The single
exact base-slack partition is

\[
\begin{aligned}
P(C_0)-P_{r,n}+\sum_{t=s_3}^{r-1}\lambda_tA_t
={}&
\sum_{\substack{t:\ \mathrm{base}\\\mathrm{split}}}
  (\Delta_{e_t}+\lambda_tA_t)
+\sum_{\substack{t:\ \mathrm{recursive}\\\mathrm{split}}}
  \lambda_tA_t
+\sum_{e\text{ unused by the selected prefixes}}\Delta_e.
\end{aligned}
\tag{CR28cf}
\]

Every original slack occurs exactly once, either beside its unique selected
split or in the sum over edges unused by the three selected prefixes. In
contrast, adding three separately slack-charged copies
of the one-prefix inequality would count early-segment slack three times and
middle-segment slack twice.

Discarding only the nonnegative unused sum in (CR28cf), and then applying
(CR28ce), proves

\[
\boxed{
\gamma^{(r)}_{1,n}
\ge P_{r,n}
+(r-s_1)F_{1,n}
+(s_1-s_2)F_{2,n}
+(s_2-s_3)F_{3,n}.
}
\tag{CR28cg}
\]

The exact comparison with the inner simple-cycle minimum remains

\[
\boxed{
\gamma^{(r)}_{1,n}-P^*_{r,n}
\ge
(r-s_1)F_{1,n}
+(s_1-s_2)F_{2,n}
+(s_2-s_3)F_{3,n}
-e(n-r+1).
}
\tag{CR28ch}
\]

No recursive edge has been replaced by a base-edge choice. Taking the
fixed-parameter limit in (CR28cg) gives the certified total coefficient

\[
\boxed{
\begin{aligned}
C_3={}&p(\alpha)
+(\alpha-\beta_1)g(\alpha,\beta_1,\lambda_1)\\
&+(\beta_1-\beta_2)g(\alpha,\beta_2,\lambda_2)
+(\beta_2-\beta_3)g(\alpha,\beta_3,\lambda_3).
\end{aligned}
}
\tag{CR28ci}
\]

#### Exact reduction of the three ordered weights

For fixed densities, each positive-length summand in (CR28ci) has the same
strictly concave weight factor \(g_\beta\) as in (CR28bw1). Its unique
clipped optimum is \(\psi_s(\beta)\) from (CR28bw2), where \(s=1+\alpha\).
Because \(\psi_s\) is nondecreasing,

\[
\psi_s(\beta_3)\le\psi_s(\beta_2)\le\psi_s(\beta_1),
\]

so the three individual optima already satisfy the prescribed weight order.
Termwise maximization gives an upper bound, and this ordered triple attains
it. Hence the reduction is exact on the full compact closure:

\[
\boxed{
\begin{aligned}
\overline C_3={}&p(\alpha)
+(\alpha-\beta_1)\Phi_s(\beta_1)\\
&+(\beta_1-\beta_2)\Phi_s(\beta_2)
+(\beta_2-\beta_3)\Phi_s(\beta_3),
\end{aligned}
}
\tag{CR28cj}
\]

where \(\Phi_s\) is (CR28bw3). Thus there is no pooled interior KKT branch.
The ten possible clipped regimes are

\[
000,\ M00,\ H00,\ MM0,\ HM0,\ HH0,
\quad MMM,\ HMM,\ HHM,\ HHH.
\]

They include every transition \(\beta_i=s/4,s/3\). On a density-collision
face, a zero-length segment makes its weight irrelevant and possibly
nonunique, but the value reduction (CR28cj) remains exact. The only closure
point at which (CR28bw1) loses strictness is
\((\alpha,\beta)=(1,1)\), where the incident segment has zero length; it
cannot affect uniqueness at the strict global point below.

#### Compact-closure maximum

For \(0\le\alpha\le1/3\), every cutoff satisfies
\(\beta_i\le\alpha\le(1+\alpha)/4\), so all three residual terms vanish and
\(\overline C_3=p(\alpha)\). Since
\(p'(\alpha)=(1-2\alpha-\alpha^2)/2>0\) on this interval, its maximum there
is \(p(1/3)=22/81\).

Now suppose \(\alpha>1/3\), and put

\[
A=3\alpha-1>0.
\]

The active cutoffs form an initial prefix because the densities are ordered.
For each active cutoff set
\(X_i=4\beta_i-(1+\alpha)\); replace an inactive suffix by \(X_i=0\) and
omit its zero terms. Then

\[
0\le X_3\le X_2\le X_1\le A.
\]

Using (CR28bw10) on every active term gives

\[
\overline C_3-p(\alpha)
\le
{(A-X_1)X_1^2+(X_1-X_2)X_2^2+(X_2-X_3)X_3^2\over8}.
\tag{CR28ck}
\]

Set \(x=X_1/A\), \(y=X_2/A\), and \(z=X_3/A\). On the entire compact
simplex \(0\le z\le y\le x\le1\), put

\[
f(x,y,z)
=(1-x)x^2+(x-y)y^2+(y-z)z^2.
\]

The following exact identity proves the global maximum directly:

\[
\begin{aligned}
{1119364\over4785507}-f(x,y,z)
={}&{(1263x-1058)^2(1263x+529)\over2531533203}\\
&+{(23y-18x)^2(23y+9x)\over14283}
+{(3z-2y)^2(3z+y)\over27}.
\end{aligned}
\tag{CR28cl}
\]

Every term on the right is nonnegative. Equality is possible only at

\[
\boxed{
(x,y,z)
=\left({1058\over1263},{276\over421},{184\over421}\right).
}
\tag{CR28cm}
\]

Thus the supplied normalized point is derived rather than assumed, and

\[
\max f={1119364\over4785507}
={4\cdot529^2\over27\cdot421^2}.
\]

Equations (CR28ck)--(CR28cm) give the one-variable compact envelope

\[
\begin{aligned}
E_3(\alpha)
&=p(\alpha)+{529^2\over54\cdot421^2}(3\alpha-1)^3\\
&={2980269\alpha^3-6170607\alpha^2
       +3652038\alpha+657664\over4785507},
\end{aligned}
\tag{CR28cn}
\]

whose derivative is

\[
E_3'(\alpha)
={993423\alpha^2-1371246\alpha+405782\over531723}.
\]

The two roots are

\[
\alpha_\pm
={685623\mathbin\pm421\sqrt{377823}\over993423}.
\]

Writing \(Q\) for the derivative numerator,

\[
Q(1/3)={177241\over3}>0,
\qquad
Q(1/2)=-{125941\over4}<0,
\qquad
Q(1)=27959>0.
\]

Hence \(\alpha_-\in(1/3,1/2)\) is the first local maximum and
\(\alpha_+\in(1/2,1)\) is a later local minimum. The latter cannot hide a
larger endpoint value, because

\[
E_3(1/3)={22\over81},
\qquad
E_3(1)={1119364\over4785507},
\qquad
E_3(1/3)-E_3(1)={541210\over14356521}>0.
\]

Together with the derivative signs, this proves that the unique global
maximizing density is

\[
\boxed{
\alpha_*={685623-421\sqrt{377823}\over993423}.
}
\tag{CR28co}
\]

Let \(A_*=3\alpha_*-1\) and let \(x_i\) be the three coordinates in
(CR28cm). Equality in the compact bound requires

\[
\beta_{i,*}={1+\alpha_*+x_iA_*\over4},
\qquad
\lambda_{i,*}=4-{1+\alpha_*\over\beta_{i,*}}
={x_iA_*\over\beta_{i,*}}.
\]

Equivalently,

\[
\begin{aligned}
\beta_{1,*}&={205+4437\alpha_*\over5052},&
\lambda_{1,*}&={4232A_*\over205+4437\alpha_*},\\
\beta_{2,*}&={145+1249\alpha_*\over1684},&
\lambda_{2,*}&={1104A_*\over145+1249\alpha_*},\\
\beta_{3,*}&={237+973\alpha_*\over1684},&
\lambda_{3,*}&={736A_*\over237+973\alpha_*}.
\end{aligned}
\]

Because \(1/3<\alpha_*<1/2\), one has
\(0<X_3<X_2<X_1<A_*<(1+\alpha_*)/3\). Therefore

\[
{1+\alpha_*\over4}
<\beta_{3,*}<\beta_{2,*}<\beta_{1,*}
<\alpha_*<{1+\alpha_*\over3}.
\]

All three densities lie strictly in the middle clipped branch, all three
segments are positive, and
\(0<\lambda_{3,*}<\lambda_{2,*}<\lambda_{1,*}<1\). Consequently every
inequality used in the envelope is an equality at this point. Conversely,
equality in (CR28cl), in (CR28bw10), and in the one-variable envelope forces
exactly these data. This also audits the full compact closure: inactive
suffixes, density collisions, high branches, and weight-tetrahedron faces
cannot tie the strict point; unused weights on zero-length faces merely give
nonunique parametrizations of smaller values.

The exact three-prefix template optimum is

\[
\boxed{
C_{3,*}
={753972193324+106042322\sqrt{377823}\over2960667770787}
=0.2766786474619455709\ldots .
}
\tag{CR28cp}
\]

It satisfies

\[
79938029811249C_{3,*}^2
-40714498439496C_{3,*}+5145490327924=0
\]

and the exact isolation

\[
{276678647461\over10^{12}}
<C_{3,*}
<{276678647462\over10^{12}}.
\]

The improvement over the two-prefix optimum is strict without comparing two
different quadratic fields. Write the strict data in (CR28bw13) as
\(\alpha_{2,*},\beta_{1,2,*},\beta_{2,2,*}\). Choose any
\(\widetilde\beta_3\) with
\[
{1+\alpha_{2,*}\over4}
<\widetilde\beta_3<\beta_{2,2,*}.
\]
Keeping the other two-prefix data, the ordered clipped choice adds the
strictly positive term
\((\beta_{2,2,*}-\widetilde\beta_3)
\Phi_{1+\alpha_{2,*}}(\widetilde\beta_3)\). Thus
\(C_{3,*}>C_{2,*}\). As an independent exact separator,

\[
C_{2,*}<{27663\over100000}<C_{3,*};
\]

after clearing the positive denominators, the two squared comparisons have
respective positive differences

\[
121188964591535801,
\qquad
187552646082113657670204830039.
\]

Finally, the optimizer is strictly proof-valid, so the pointwise global
comparison followed by the fixed-parameter limit in (CR28cg) gives

\[
\boxed{
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{3,*},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{3,*}\over\pi}.
}
\tag{CR28cq}
\]

The derivation through (CR28cq) is the asymptotic optimization of the
documented three-prefix template. The finite floor/ceiling specialization is
proved below. Neither result identifies an exact block residual, proves
convergence or an exact geometric leading coefficient, or makes a
production-computation claim.

Independent test-local exact arithmetic checks this proof without entering
it. A bounded oracle exhausts all
\(35\cdot36\cdot37=46{,}620\) literal depth-three histories from one
\(n=59\) base cycle. It includes 70 distinct recursive second-step prefixes,
occurring in 2,590 complete histories, plus 4,970 recursive third splits and
all 70 fully nested third splits of the edge formed by the two earlier labels.
Every history checks literal linkage, the one-use base
map, every local floor, the combined weighted identity, the unused-slack
partition, and the selected-prefix maximum. Further Fraction grids check
the exact ordered-weight reduction, all ten clipped regimes, the compact
density closure, and the factorization (CR28cl). Test-local
\(\mathbb Q(\sqrt{377823})\) arithmetic verifies the optimizer, strict domain,
coefficient, minimal polynomial, isolating interval, and strict comparison
with \(C_{2,*}\), without calling production scorers, canonicalizers, or
enumerators.

#### Finite theorem at the irrational three-prefix optimizer

The exact optimizer can be rounded without replacing its three-prefix
charging argument. Write

\[
d=377823,
\qquad
a=\alpha_*={685623-421\sqrt d\over993423},
\qquad
A=3a-1,
\]

\[
(x_1,x_2,x_3)
=\left({1058\over1263},{276\over421},{184\over421}\right),
\qquad
b_i={1+a+x_iA\over4}.
\tag{CR28cq1}
\]

Thus \(b_i=\beta_{i,*}\) from the strict middle-branch optimizer above. For
an integer \(n\ge1\), define

\[
r_n=\lfloor an\rfloor,
\qquad
s_{i,n}=\lceil b_i n\rceil\quad(i=1,2,3),
\qquad
S_n=n+r_n.
\tag{CR28cq2}
\]

Whenever the three cutoffs lie in the finite middle clipped branch, put

\[
\widehat\lambda_{i,n}=4-{S_n\over s_{i,n}},
\qquad
\widehat F_{i,n}
=G_{n,\widehat\lambda_{i,n}}(s_{i,n})
={\left(4s_{i,n}-S_n\right)^2\over2}.
\tag{CR28cq3}
\]

These are the exact finite clipped optima, not the fixed irrational weights
\(\lambda_{i,*}\). If
\(S_n/4<s_{3,n}<s_{2,n}<s_{1,n}<S_n/3\), then

\[
0<\widehat\lambda_{3,n}
<\widehat\lambda_{2,n}
<\widehat\lambda_{1,n}<1.
\]

Consequently the ordered-weight hypothesis in (CR28cd)--(CR28cg) holds
pointwise at this finite \(n\).

We next prove the exact uniform domain. The derivative polynomial in
(CR28cn) takes the exact values \(27959/49>0\) at \(3/7\) and
\(-1021633/256<0\) at \(7/16\). Because \(a\) is its first root in
\((1/3,1/2)\), this proves

\[
{3\over7}<a<{7\over16}.
\]

The consecutive density gaps simplify to

\[
a-b_1={205A\over5052},
\qquad
b_1-b_2={230A\over5052},
\qquad
b_2-b_3={276A\over5052}.
\tag{CR28cq4}
\]

For \(n\ge171\), the first and smallest segment satisfies

\[
r_n-s_{1,n}>(a-b_1)n-2>0,
\]

because

\[
171(a-b_1)-2
={21568926-35055\sqrt d\over3973692}>0,
\qquad
21568926^2-d\,35055^2=929632328901>0.
\tag{CR28cq5}
\]

The other two gaps in (CR28cq4) are larger, while their floor/ceiling losses
are only one, so they are positive as well. The remaining block conditions
\(2\le r_n\le n-2\) and \(s_{3,n}\ge1\) follow immediately from
\(3/7<a<7/16\) and \(0<b_3<a\).

The middle clipped conditions also hold uniformly. Put
\(\eta_n=an-r_n\in[0,1)\) and
\(\varepsilon_{i,n}=s_{i,n}-b_i n\in[0,1)\). Then

\[
4s_{i,n}-S_n=x_iAn+4\varepsilon_{i,n}+\eta_n>0.
\]

Since \(b_i\le b_1\), the smallest upper-clip density gap is
\(u_1=(1+a)-3b_1\). Exact arithmetic gives

\[
23u_1-4
={-38744394+63319\sqrt d\over3973692}>0,
\qquad
d\,63319^2-38744394^2=13676085881067>0.
\]

Hence

\[
S_n-3s_{i,n}
>((1+a)-3b_i)n-4\ge u_1n-4>0
\qquad(n\ge23).
\tag{CR28cq6}
\]

At \(n=22\), the last coarse expression is negative, so \(23\) is the exact
threshold of this uniform upper-clip rounding estimate. The actual cutoffs
are checked separately below where needed.

Only the finite gap before the symbolic tail remains. The exact rational
isolation

\[
{614673083842134\over10^{12}}
<\sqrt d<
{614673083842135\over10^{12}}
\]

follows by squaring integers; the two positive gaps are respectively
\(906132566326044\) and \(323213601358225\) after the common scaling.
It gives the following exact cutoffs.

| \(n\) | \(r_n\) | \(s_{1,n}\) | \(s_{2,n}\) | \(s_{3,n}\) |
|---:|---:|---:|---:|---:|
| 158 | 67 | 67 | 64 | 62 |
| 159 | 68 | 67 | 65 | 62 |
| 160 | 68 | 67 | 65 | 63 |
| 161 | 69 | 68 | 66 | 63 |
| 162 | 69 | 68 | 66 | 64 |
| 163 | 70 | 69 | 66 | 64 |
| 164 | 70 | 69 | 67 | 64 |
| 165 | 70 | 69 | 67 | 65 |
| 166 | 71 | 70 | 68 | 65 |
| 167 | 71 | 70 | 68 | 65 |
| 168 | 72 | 71 | 69 | 66 |
| 169 | 72 | 71 | 69 | 66 |
| 170 | 73 | 72 | 69 | 67 |

Thus every required order, non-vacuity, block, and clipped-branch condition
holds for \(159\le n\le170\), and the symbolic argument covers every
\(n\ge171\). At \(n=158\), however, the first segment is empty because
\(r_{158}=s_{1,158}=67\). Therefore

\[
\boxed{n=159}
\]

is the minimal uniform threshold for this three-nonempty-prefix rounded
specialization.

Define the literal finite lower expression

\[
\begin{aligned}
\mathcal B_{3,n}:={}&P_{r_n,n}
 +(r_n-s_{1,n})\widehat F_{1,n}\\
&+(s_{1,n}-s_{2,n})\widehat F_{2,n}
 +(s_{2,n}-s_{3,n})\widehat F_{3,n}.
\end{aligned}
\tag{CR28cq7}
\]

Since \(P_{r_n,n}\) is an integer and the three added terms are
half-integers, define the explicit integer closure

\[
\mathcal I_{3,n}:=\left\lceil\mathcal B_{3,n}\right\rceil
=P_{r_n,n}
+\left\lceil
{1\over2}\sum_{i=1}^3
L_{i,n}(4s_{i,n}-S_n)^2
\right\rceil,
\tag{CR28cq7a}
\]

where
\(L_{1,n}=r_n-s_{1,n}\),
\(L_{2,n}=s_{1,n}-s_{2,n}\), and
\(L_{3,n}=s_{2,n}-s_{3,n}\).
The closure can be strict; for example,
\[
\mathcal B_{3,162}={2374661\over2},
\qquad
\mathcal I_{3,162}=1187331.
\]

The one-use charging theorem (CR28cf)--(CR28cg), applied with the finite
ordered weights (CR28cq3), proves the first chain below. Since \(\Lambda_n\)
is an integer by (CR12h), it also proves the stronger integer conclusion

\[
\boxed{
\Lambda_n
\ge\Gamma_n^{(r_n)}
\ge\gamma^{(r_n)}_{1,n}
\ge\mathcal B_{3,n},
\qquad
\Lambda_n\ge\mathcal I_{3,n}\ge\mathcal B_{3,n}
}
\qquad(n\ge159).
\tag{CR28cq8}
\]

The inner simple-cycle comparison remains a distinct statement:

\[
\gamma^{(r_n)}_{1,n}-P^*_{r_n,n}
\ge
\mathcal B_{3,n}-P_{r_n,n}-e(n-r_n+1).
\tag{CR28cq9}
\]

In particular, (CR28cq8) does not silently replace \(P_{r_n,n}\) by
\(P^*_{r_n,n}\).

There is a controlled polynomial consequence with the same exact cubic
coefficient. Put

\[
g_i={x_i^2A^2\over2},
\qquad
c_{{\rm res},3,*}
=(a-b_1)g_1+(b_1-b_2)g_2+(b_2-b_3)g_3.
\]

The identity \(4s_{i,n}-S_n=x_iAn+4\varepsilon_{i,n}+\eta_n\) gives
\(\widehat F_{i,n}\ge g_i n^2\). The exact segment lengths are

\[
\begin{aligned}
r_n-s_{1,n}&=(a-b_1)n-\eta_n-\varepsilon_{1,n},\\
s_{1,n}-s_{2,n}&=(b_1-b_2)n
 +\varepsilon_{1,n}-\varepsilon_{2,n},\\
s_{2,n}-s_{3,n}&=(b_2-b_3)n
 +\varepsilon_{2,n}-\varepsilon_{3,n}.
\end{aligned}
\]

Together with \(g_1>g_2>g_3>0\), they give the rounding telescope

\[
\begin{aligned}
&-g_1\eta_n+(g_2-g_1)\varepsilon_{1,n}
 +(g_3-g_2)\varepsilon_{2,n}-g_3\varepsilon_{3,n}\\
&\hspace{35mm}>-2g_1.
\end{aligned}
\]

Consequently

\[
\mathcal B_{3,n}-P_{r_n,n}
>c_{{\rm res},3,*}n^3-2g_1n^2.
\tag{CR28cq10}
\]

For the pairing term, direct substitution of
\(r_n=an-\eta_n\) gives the identity

\[
\begin{aligned}
P_{r_n,n}={}&p(a)n^3
+\left[a+{a^2+2a-1\over2}\eta_n\right]n^2\\
&-\left[{1+a\over2}\eta_n^2+\eta_n+{1-a\over6}\right]n
+{\eta_n^3-\eta_n\over6}.
\end{aligned}
\tag{CR28cq11}
\]

Since \(3/7<a<7/16\), one has
\((a^2+2a-1)/2>0\), while the bracket multiplying \(-n\) is less than
\((a+5)/3\), and elementary one-variable maximization gives
\[
{\eta_n^3-\eta_n\over6}
\ge-{1\over9\sqrt3}>-{1\over15},
\]
where the last comparison is \(25<27\). Combining
(CR28cq10)--(CR28cq11), and using
\(C_{3,*}=p(a)+c_{{\rm res},3,*}\), yields

\[
\boxed{
\mathcal B_{3,n}
>
C_{3,*}n^3+\kappa_*n^2-\ell_*n-{1\over15}
}
\qquad(n\ge159),
\tag{CR28cq12}
\]

where

\[
\kappa_*=a-2g_1
=a-x_1^2A^2
={-535396585939+1466777893\sqrt d\over986889256929},
\qquad
\ell_*={a+5\over3}.
\tag{CR28cq13}
\]

It remains to check rather than assume the sign of this remainder. Since

\[
\kappa_*-{1\over3}
=A\left({1\over3}-x_1^2A\right)>0,
\qquad
\ell_*<{11\over6},
\]

where \(0<A<5/16<1/3\) and \(0<x_1<1\), one has

\[
\kappa_*n^2-\ell_*n-{1\over15}
>{10n^2-55n-2\over30}>0
\qquad(n\ge6).
\]

Thus the rounded finite theorem does imply the bare optimized cubic bound,
and does so on its whole minimal uniform domain:

\[
\boxed{
\Lambda_n\ge\mathcal I_{3,n}
\ge\mathcal B_{3,n}>C_{3,*}n^3
\qquad(n\ge159).
}
\tag{CR28cq14}
\]

The integer expression \(\mathcal I_{3,n}\) is the strongest explicit
cutoff-only consequence of this rounded bound established here;
\(\mathcal B_{3,n}\) is the underlying literal charging expression. The
strict global cyclic-ratio sandwich also gives

\[
\boxed{
R_2^*(n)
>{\mathcal I_{3,n}\over\pi}-n^2
\ge{\mathcal B_{3,n}\over\pi}-n^2
>{C_{3,*}\over\pi}n^3-n^2
\qquad(n\ge159).
}
\tag{CR28cq15}
\]

This is an exact finite method-specific theorem obtained from the established
three-prefix charging identity. It is not an exact value of \(\Lambda_n\)
or \(R_2^*(n)\), an exact residual, a convergence theorem, a matching upper
bound, or an extension of charging to four prefixes. The standalone dossier
diagnostic independently evaluates \(\mathbb Q(\sqrt{377823})\), checks the
boundary table and the finite region before the symbolic tail, and verifies
the literal and polynomial inequalities through \(n=1000\), without importing
production code or changing any enumeration limit.

### Four selected prefixes with one slack partition

The next direct charging case also closes, without using the normalized
simplex lemma and without optimizing any parameter. Fix

\[
0<\beta_4<\beta_3<\beta_2<\beta_1<\alpha<1,
\qquad
0\le\lambda_4\le\lambda_3\le\lambda_2\le\lambda_1\le1,
\]

and put

\[
r=\lfloor\alpha n\rfloor,
\qquad
s_i=\lceil\beta_i n\rceil\quad(i=1,2,3,4),
\qquad
s_0=r.
\tag{CR28de}
\]

At fixed \(n\), require exactly the finite admissibility conditions

\[
2\le r\le n-2,
\qquad
1\le s_4<s_3<s_2<s_1\le r-1.
\]

Strict ordering of the real densities guarantees these integer conditions
eventually, not at every finite \(n\). For an arbitrary compatible literal
split history, define the four selected heights

\[
H_i=\sum_{t=s_i}^{r-1}A_t\quad(i=1,2,3,4).
\]

The five numbers

\[
1-\lambda_1,\quad
\lambda_1-\lambda_2,\quad
\lambda_2-\lambda_3,\quad
\lambda_3-\lambda_4,\quad
\lambda_4
\]

are nonnegative and sum to one. Hence

\[
\boxed{
\begin{aligned}
\max(0,H_1,H_2,H_3,H_4)
\ge{}&
(\lambda_1-\lambda_2)H_1
+(\lambda_2-\lambda_3)H_2\\
&+(\lambda_3-\lambda_4)H_3+\lambda_4H_4.
\end{aligned}
}
\tag{CR28df}
\]

This ordered region is exact for an inequality required to hold for all real
height quadruples. Indeed, a linear form is bounded by
\(\max(0,H_1,H_2,H_3,H_4)\) for every quadruple exactly when its four
coefficients are nonnegative and have sum at most one. Negative coefficients
are excluded by sending the corresponding height to \(-\infty\), and a sum
larger than one is excluded by taking all heights equal and positive.

Expanding the right side of (CR28df) before assigning any edge slack
telescopes to

\[
\lambda_1\sum_{t=s_1}^{s_0-1}A_t
+\lambda_2\sum_{t=s_2}^{s_1-1}A_t
+\lambda_3\sum_{t=s_3}^{s_2-1}A_t
+\lambda_4\sum_{t=s_4}^{s_3-1}A_t.
\]

Thus the four disjoint segments
\(I_i=\{s_i,\ldots,s_{i-1}-1\}\) carry the four weights. Write
\(\lambda_t=\lambda_i\) on \(I_i\), retain

\[
\Delta_e={(u+v-n-r)^2\over2}
\qquad(e=\{u,v\}\in E(C_0)),
\]

and define

\[
F_{i,n}=G_{n,\lambda_i}(s_i)\quad(i=1,2,3,4).
\]

There is one canonical partition of the original-edge slack for each literal
history. If \(B\) is the set of selected labels whose split uses an untouched
edge \(e_t\in E(C_0)\), then \(t\mapsto e_t\) is injective. A removed original
edge is never recreated, because later splits insert a label below \(r\) and
never join two original endpoints. Consequently

\[
\begin{aligned}
P(C_0)-P_{r,n}+\sum_{t=s_4}^{r-1}\lambda_tA_t
={}&
\sum_{\substack{t:\ \mathrm{base}\\\mathrm{split}}}
  (\Delta_{e_t}+\lambda_tA_t)
+\sum_{\substack{t:\ \mathrm{recursive}\\\mathrm{split}}}
  \lambda_tA_t\\
&+\sum_{e\in E(C_0)\setminus\{e_t:t\in B\}}\Delta_e.
\end{aligned}
\tag{CR28dg}
\]

The word canonical here is combinatorial: the original edge set is uniquely
partitioned into the injectively charged edges and the unused edges. It does
not assert uniqueness among arbitrary numerical decompositions when some
\(\Delta_e=0\).

The recursive invariant is unchanged by any of the three segment boundaries.
Immediately before label \(t\) is inserted, every current edge is either an
untouched original edge or has an endpoint in
\(\{t+1,\ldots,r-1\}\). This holds initially. Splitting either kind of edge
creates two children incident to \(t\); for every later label \(t'<t\), that
endpoint belongs to \(\{t'+1,\ldots,r-1\}\). Induction therefore covers every
recursive child, including arbitrarily nested edges and edges whose two
endpoints were inserted earlier.

On segment \(I_i\), the base estimate (CR28ay), monotonicity (CR28bc), and the
recursive estimate (CR28ba)--(CR28bd) give respectively

\[
\Delta_{e_t}+\lambda_iA_t
\ge G_{n,\lambda_i}(t)\ge F_{i,n},
\]

and

\[
\lambda_iA_t
\ge J_{n,\lambda_i}(t)
\ge G_{n,\lambda_i}(t)
\ge F_{i,n}.
\]

These inequalities include \(\lambda_i=0\), when all displayed local floors
vanish. Discarding only the nonnegative unused slack in (CR28dg), and then
using (CR28df), proves the exact four-segment lower bound

\[
\boxed{
\begin{aligned}
\gamma^{(r)}_{1,n}\ge{}& P_{r,n}
+(r-s_1)F_{1,n}
+(s_1-s_2)F_{2,n}\\
&+(s_2-s_3)F_{3,n}
+(s_3-s_4)F_{4,n}.
\end{aligned}
}
\tag{CR28dh}
\]

No positivity of the individual \(F_{i,n}\) is assumed. The comparison with
the inner simple-cycle minimum is, exactly as before,

\[
\boxed{
\begin{aligned}
\gamma^{(r)}_{1,n}-P^*_{r,n}\ge{}
&(r-s_1)F_{1,n}
+(s_1-s_2)F_{2,n}\\
&+(s_2-s_3)F_{3,n}
+(s_3-s_4)F_{4,n}
-e(n-r+1).
\end{aligned}
}
\tag{CR28di}
\]

For fixed admissible real parameters, taking only the usual \(n\to\infty\)
limit in (CR28dh) gives the unoptimized coefficient

\[
\boxed{
\begin{aligned}
C_4={}&p(\alpha)
+(\alpha-\beta_1)g(\alpha,\beta_1,\lambda_1)\\
&+(\beta_1-\beta_2)g(\alpha,\beta_2,\lambda_2)\\
&+(\beta_2-\beta_3)g(\alpha,\beta_3,\lambda_3)\\
&+(\beta_3-\beta_4)g(\alpha,\beta_4,\lambda_4).
\end{aligned}
}
\tag{CR28dj}
\]

Equations (CR28ap) and (CR28) therefore imply, without any parameter
optimization or finite rounding theorem,

\[
\boxed{
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_4,
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge {C_4\over\pi}.
}
\tag{CR28dk}
\]

Equation (CR28dk) is still the fixed-parameter consequence; the global
comparison with \(C_{3,*}\) is proved in the optimization below. No
\(k\ge5\) charging statement, uniform \(k\)-to-\(n\) interchange, exact
residual, convergence result, or geometric leading coefficient follows.

The standalone dossier oracle uses
\[
(n,r,C_0)=(14,11,(11,14,12,13)),
\quad
(s_1,s_2,s_3,s_4)=(10,9,8,7),
\quad
(\lambda_1,\lambda_2,\lambda_3,\lambda_4)=(4/5,3/5,2/5,1/5).
\]
It checks all \(4\cdot5\cdot6\cdot7=840\) current-edge histories in exact
standard-library Fraction arithmetic, with 840 distinct final cycles. The
recursive search-tree split counts by depth are \((0,8,72,600)\); 120 fourth
splits have two previously inserted endpoints. The four local floors sum to \(9239/72\),
and every history satisfies the literal partition (CR28dg) and bound
(CR28dh). This bounded computation is independent corroboration, not the
all-history proof.

#### Global optimization of the four-prefix coefficient

The charging proof is complete before this optimization begins. Put

\[
s=1+\alpha,
\quad L={s\over4},
\quad U={s\over3},
\quad \beta_0=\alpha,
\quad d_i=\beta_{i-1}-\beta_i.
\]

The strict proof-valid domain is dense in the compact closure

\[
\boxed{
0\le\beta_4\le\beta_3\le\beta_2\le\beta_1\le\alpha\le1,
\qquad
0\le\lambda_4\le\lambda_3\le\lambda_2\le\lambda_1\le1.
}
\tag{CR28dl}
\]

For fixed densities, every positive-length summand has the strictly concave
weight factor (CR28bw1). Its unique clipped optimum is
\(\psi_s(\beta_i)\) from (CR28bw2). Since \(\psi_s\) is nondecreasing, the
four individual optima already obey the weight order. If \(d_i=0\), that
weight is unused, while the clipped choice still attains the termwise upper
bound. Hence there is no pooled KKT branch and the exact compact reduction is

\[
\boxed{
\overline C_4(\alpha,\boldsymbol\beta)
=p(\alpha)+\sum_{i=1}^4d_i\Phi_s(\beta_i),
}
\tag{CR28dm}
\]

where \(\Phi_s\) is (CR28bw3). On a positive segment,

\[
\lambda_i=
\begin{cases}
0,&\beta_i\le L,\\
4-s/\beta_i,&L<\beta_i<U,\\
1,&U\le\beta_i.
\end{cases}
\]

There are exactly fifteen ordered clipping regimes, namely all words
\(H^hM^m0^z\) with \(h+m+z=4\):

\[
\begin{gathered}
0000;\qquad M000,\ H000;\qquad
MM00,\ HM00,\ HH00;\\
MMM0,\ HMM0,\ HHM0,\ HHH0;\qquad
MMMM,\ HMMM,\ HHMM,\ HHHM,\ HHHH.
\end{gathered}
\tag{CR28dn}
\]

The clipping surfaces are exactly
\(\beta_i=L\), where \(\lambda_i=0\), and \(\beta_i=U\), where
\(\lambda_i=1\). Both \(\Phi_s\) and \(\Phi_s'\) join there, and each surface
belongs to both adjacent branch closures. The five words without an \(M\)
are the vertices of the ordered-weight 4-simplex; with distinct densities, a
word with \(m\) middle entries is in the relative interior of the
corresponding \(m\)-face. With strict densities, \(\psi_s\) is strictly
increasing on the middle piece. Thus no face
\(0<\lambda_{i+1}=\lambda_i<1\) is KKT: a feasible separating direction
moves at least one weight toward its distinct individual optimum. Equal
optimal weights arise only from a clipped 0- or 1-plateau, a density
collision, or an unused segment.

The winning branch at every fixed \(\alpha\) can also be classified exactly.
Normalize

\[
\tau={\alpha\over1+\alpha},
\qquad \rho_i={\beta_i\over1+\alpha},
\]

and put

\[
\phi(x)=
\begin{cases}
0,&x\le1/4,\\
(4x-1)^2/2,&1/4\le x\le1/3,\\
-x^2+2x-1/2,&x\ge1/3.
\end{cases}
\]

The residual in (CR28dm) is
\((1+\alpha)^3\mathcal V_\tau(\rho_1,\ldots,\rho_4)\), where

\[
\mathcal V_\tau(\rho_1,\ldots,\rho_4)
=(\tau-\rho_1)\phi(\rho_1)+(\rho_1-\rho_2)\phi(\rho_2)
+(\rho_2-\rho_3)\phi(\rho_3)+(\rho_3-\rho_4)\phi(\rho_4).
\tag{CR28do}
\]

For \(\tau\le1/4\), it vanishes. For \(\tau>1/4\), an inactive suffix
cannot maximize: appending a cutoff strictly between \(1/4\) and the last
active cutoff adds a positive term. Hence the ten words with a trailing zero
are nonwinning.

The Bellman recursion

\[
V_0(t)=0,
\qquad
V_m(t)=\max_{1/4\le x\le t}\bigl((t-x)\phi(x)+V_{m-1}(x)\bigr),
\qquad
V_4(\tau)=
\max_{\tau\ge\rho_1\ge\cdots\ge\rho_4\ge1/4}
\mathcal V_\tau(\rho_1,\ldots,\rho_4),
\]

has the interior equations

\[
0=-\phi(\rho_i)+(\rho_{i-1}-\rho_i)\phi'(\rho_i)+\phi(\rho_{i+1}),
\quad \rho_0=\tau,
\quad\phi(\rho_5)=0.
\tag{CR28dp}
\]

Writing \(y_i=4\rho_i-1\), the four required predecessor maps are

\[
\begin{aligned}
P_{MM}(y,z)&={3y^2-z^2\over2y},&
P_{HM}(y,z)&={-3y^2+12y-8z^2-1\over2(3-y)},\\
P_{HH}(y,z)&={-3y^2+12y+z^2-6z\over2(3-y)},&
P_{H0}(y)&={-3y^2+12y-1\over2(3-y)}.
\end{aligned}
\tag{CR28dq}
\]

Strict monotonicity must treat the mixed base before the high--high
induction. Put

\[
(q_1,q_2,q_3,q_4)=\left({2\over3},{18\over23},{1058\over1263},
 {3190338\over3666143}\right).
\]

On an all-middle suffix, homogeneity gives the child relation \(z=q_my\),
and

\[
P_{MM}(y,q_my)={3-q_m^2\over2}y={y\over q_{m+1}},
\qquad P_{MM}(y,0)={3y\over2}={y\over q_1}.
\]

Thus every all-middle predecessor has derivative greater than one. Now let
one high coordinate be followed by an optimized middle tail of length
\(m\in\{1,2,3\}\). Its first child has \(z=q_my\), so

\[
T_m(y):=P_{HM}(y,q_my)
={-(3+8q_m^2)y^2+12y-1\over2(3-y)}.
\]

The tail remains middle exactly on

\[
{1\over3}\le y\le{1\over3q_m},
\]

whose right endpoints for \(m=1,2,3\) are respectively
\(1/2,23/54,421/1058\). Direct differentiation gives

\[
T_m'(y)-1
={17-(1+8q_m^2)y(6-y)\over2(3-y)^2}.
\]

Since \(y(6-y)\) is increasing on these intervals, the numerator is bounded
below by its right-endpoint value. For \(m=1,2,3\) those exact values are

\[
{161\over36},\qquad {200735\over67068},\qquad
{9571263245\over4241270196},
\]

so \(T_m'(y)>1\) throughout every relevant `HM` base. For a terminal high
coordinate,

\[
T_0(y):=P_{H0}(y),
\qquad
T_0'(y)-1={y^2-6y+17\over2(3-y)^2}
={(y-3)^2+8\over2(3-y)^2}>0.
\]

It remains only to propagate outward through high--high links. When both
\(\rho_i\) and \(\rho_{i+1}\) are high, put \(u_j=1-\rho_j\). Then, and only then,
(CR28dp) gives

\[
u_{i-1}={3u_i^2-u_{i+1}^2\over2u_i}.
\]

If the already constructed suffix has
\(0<du_{i+1}/du_i<1\), and \(z=u_{i+1}/u_i\ge1\), then

\[
{du_{i-1}\over du_i}
={3\over2}+{z^2\over2}-z{du_{i+1}\over du_i}
>1+{(z-1)^2\over2}\ge1.
\]

Hence its inverse again has derivative in \((0,1)\), closing the `HH`
induction. In each Bellman region the derivative has the sign of
\(\phi'(x)(t-T(x))\). Every active regional maximum for \(\tau>1/4\) is
therefore unique; starting at \(\tau=1/4\), the \(C^1\) joins give the
complete sequence

\[
\begin{array}{c|c}
\alpha\text{ interval}&\text{winning regime}\\ \hline
0\le\alpha\le1/3&0000\\
1/3<\alpha<\alpha_1&MMMM\\
\alpha_1<\alpha<\alpha_2&HMMM\\
\alpha_2<\alpha<\alpha_3&HHMM\\
\alpha_3<\alpha\le1&HHHM,
\end{array}
\tag{CR28dq1}
\]

where

\[
\alpha_1={13237157\over25046899},
\qquad
\alpha_2={76718581\over132993947},
\qquad
\alpha_3={1806469369\over2664344423}.
\tag{CR28dq2}
\]

The three transition points are

\[
\begin{array}{c|c|c}
\tau&(\rho_1,\rho_2,\rho_3,\rho_4)&(\lambda_1,\lambda_2,\lambda_3,\lambda_4)\\ \hline
{13237157\over38284056}
 &(1/3,4847/15156,513/1684,1447/5052)
 &(1,4232/4847,368/513,736/1447)\\[1mm]
{76718581\over209712528}
 &(1479/4232,1/3,29/92,27/92)
 &(1,1,24/29,16/27)\\[1mm]
{1806469369\over4470813792}
 &(7607/20016,77/216,1/3,11/36)
 &(1,1,1,8/11).
\end{array}
\tag{CR28dq3}
\]

On the first row of (CR28dq1) the residual is identically zero, so `0000`
records the winning clipped regime but the maximizing parametrization need
not be unique. At each transition in (CR28dq3), the point is the unique
maximum and belongs to both adjacent branch closures.

The formal `HHHM`--`HHHH` transition would be

\[
\tau_4={199200916177\over391198109760}>{1\over2},
\qquad
\alpha_4={199200916177\over191997193583}>1,
\]

at normalized densities
\((93059/201120,301/720,3/8,1/3)\). Thus `HHHH` never wins on the
admissible compact domain.

The collision and face audit is as follows. Each density facet

\[
\beta_1=\alpha,\quad \beta_2=\beta_1,\quad
\beta_3=\beta_2,\quad \beta_4=\beta_3,\quad \beta_4=0
\tag{CR28dq4}
\]

deletes one summand of (CR28dm), so its exact maximum is \(C_{3,*}\).
Multiple collisions reduce to at most two effective prefixes. An unused
weight on a zero-length segment may be filled arbitrarily between its ordered
neighbors; a consecutive unused block permits any ordered filling between
the active neighboring weights. This is boundary nonuniqueness below the
global value.

The outer weight facets also have exact maximum \(C_{3,*}\). On
\(\lambda_4=0\), the last term vanishes. On \(\lambda_1=1\), differentiation
at fixed remaining parameters gives

\[
{\partial C_4\over\partial\alpha}
=-(\alpha-\beta_1)(2\alpha-3\beta_1+3)
+\sum_{i=2}^4d_i{\lambda_i(2\beta_i-1-\alpha)\over2-\lambda_i}
\le0.
\]

Moving to \(\alpha=\beta_1\) deletes the first term. On an internal diagonal
\(\lambda_i=\lambda_{i+1}\), strict densities and positive segments admit
the separating improvement already described; plateau, collision, and unused
cases are covered above. Thus no internal weight face contains a global
maximizer. The face \(\alpha=0\) collapses to \(\beta_i=0\), has value
\(p(0)=1/6\), and leaves every ordered weight unused. The face \(\alpha=1\)
has the unique `HHHM` point determined by (CR28dp)--(CR28dq) and satisfies
\(C_4\le M_4<22/81\). This exhausts the facets of both compact simplices.

It remains to determine the global value. For \(\alpha>1/3\), put
\(A=3\alpha-1\). On active cutoffs set \(X_i=4\beta_i-s\); replace an
inactive suffix by \(X_i=0\). Then
\(0\le X_4\le\cdots\le X_1\le A\). Since

\[
\Phi_s(\beta)\le{(4\beta-s)^2\over2},
\]

with equality on the middle branch and exact high-branch loss
\((3\beta-s)^2\),

\[
\overline C_4-p(\alpha)
\le{(A-X_1)X_1^2+(X_1-X_2)X_2^2
 +(X_2-X_3)X_3^2+(X_3-X_4)X_4^2\over8}.
\tag{CR28dq5}
\]

Set \(x_i=X_i/A\). The specialized nonnegative certificate (CR28cu) is

\[
\begin{aligned}
M_4-F_4(x)={}&(1-M_3)(x_1-q_4)^2(x_1+q_4/2)\\
&+(1-M_2)(x_2-q_3x_1)^2(x_2+q_3x_1/2)\\
&+(1-M_1)(x_3-q_2x_2)^2(x_3+q_2x_2/2)\\
&+(x_4-q_1x_3)^2(x_4+q_1x_3/2),
\end{aligned}
\tag{CR28dq6}
\]

where

\[
(q_4,q_3,q_2,q_1)
=\left({3190338\over3666143},{1058\over1263},{18\over23},{2\over3}\right),
\qquad
M_4={3392752184748\over13440604496449}.
\]

Every summand is nonnegative. Equality uniquely forces

\[
\boxed{
(x_1,x_2,x_3,x_4)
={1\over3666143}(3190338,2672508,2091528,1394352).
}
\tag{CR28dq7}
\]

Thus the compact objective is bounded by

\[
\begin{aligned}
E_4(\alpha)
&=p(\alpha)+{M_4\over8}(3\alpha-1)^3\\
&={27631313622349\alpha^3-54512522615247\alpha^2
 +31611445368198\alpha+5448020178944
 \over40321813489347}.
\end{aligned}
\tag{CR28dq8}
\]

Its derivative is \(Q(\alpha)/13440604496449\), where

\[
Q(\alpha)=27631313622349\alpha^2
-36341681743498\alpha+10537148456066.
\]

The signs

\[
Q(1/3)={13440604496449\over9}>0,
\quad Q(1/2)=-{2903456040383\over4}<0,
\quad Q(1)=1826780334917>0
\]

make the smaller root a local maximum and the larger root a later local
minimum. Also

\[
E_4(1/3)-E_4(1)
={22\over81}-M_4
={20880371957290\over1088688964212369}>0.
\]

Hence the unique global envelope maximum is at

\[
\boxed{
\alpha_*={18170840871749-3666143\sqrt{2903456040383}
 \over27631313622349}
=0.4315359537746474955\ldots .
}
\tag{CR28dq9}
\]

Since \(1/3<\alpha_*<1/2<\alpha_1\), it is strictly in `MMMM`. Put
\(A_*=3\alpha_*-1\) and use the four coordinates in (CR28dq7). Equality is
attained at

\[
\boxed{
\beta_{i,*}={1+\alpha_*+x_iA_*\over4},
\qquad
\lambda_{i,*}={x_iA_*\over\beta_{i,*}}
\quad(1\le i\le4).
}
\tag{CR28dq10}
\]

Equivalently,

\[
\begin{aligned}
\beta_{1,*}&={475805+13237157\alpha_*\over14664572},&
\lambda_{1,*}&={12761352A_*\over475805+13237157\alpha_*},\\
\beta_{2,*}&={993635+11683667\alpha_*\over14664572},&
\lambda_{2,*}&={10690032A_*\over993635+11683667\alpha_*},\\
\beta_{3,*}&={1574615+9940727\alpha_*\over14664572},&
\lambda_{3,*}&={8366112A_*\over1574615+9940727\alpha_*},\\
\beta_{4,*}&={2271791+7849199\alpha_*\over14664572},&
\lambda_{4,*}&={5577408A_*\over2271791+7849199\alpha_*}.
\end{aligned}
\]

Numerically,

\[
\boldsymbol\beta_*
=(0.421977141321,0.411574056333,0.399902302444,0.385896197777)\ldots,
\]

\[
\boldsymbol\lambda_*
=(0.607550946261,0.521802257099,0.420285792242,0.290360044955)\ldots .
\]

All density and weight inequalities are strict, and every cutoff is strictly
middle-clipped. Conversely, equality in (CR28dq5), (CR28dq6), and (CR28dq8)
forces exactly these data. Therefore the maximizing nine-tuple is unique on
the whole compact closure; the lower-value boundary weight freedom does not
produce another maximum.

The exact optimum is

\[
\boxed{
C_{4,*}
={597580022071777213687318156
 +21288970076515705538\sqrt{2903456040383}
 \over2290468477489828247376833403}
=0.2767361498609895101\ldots .
}
\tag{CR28dq11}
\]

It is the root in

\[
{276736149860\over10^{12}}<C_{4,*}
<{276736149861\over10^{12}}
\]

of

\[
6871405432469484742130500209z^2
-3585480132430663282123908936z
+465999835246384276537748084=0.
\]

The improvement over three prefixes is strict in two independent exact
ways. Let \(\alpha_*^{(3)}\) and \(\beta_{3,*}^{(3)}\) denote respectively
the density (CR28co) and the last cutoff of the strict three-prefix
optimizer. Retain that point and choose
\((1+\alpha_*^{(3)})/4<\beta_4<\beta_{3,*}^{(3)}\), with its middle clipped weight.
The added term
\((\beta_{3,*}^{(3)}-\beta_4)
\Phi_{1+\alpha_*^{(3)}}(\beta_4)\) is positive. Also,

\[
\boxed{C_{3,*}<{2767\over10000}<C_{4,*}.}
\tag{CR28dq12}
\]

After clearing positive denominators and squaring positive quantities, the
two differences are respectively

\[
824523723482111238496361641
\]

and

\[
600035982853463093354803882519517840276863691635717857799,
\]

both positive. The point (CR28dq10) is strict, so the direct four-prefix
theorem gives

\[
\boxed{
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{4,*},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{4,*}\over\pi}.
}
\tag{CR28dq13}
\]

This is an optimized asymptotic template theorem, not finite rounding in
\(n\), an exact residual, a convergence result, a geometric leading
constant, or a five-prefix charging statement.

The standalone standard-library diagnostic at
`ops/TASK-20260717__global_four_prefix_optimization/exact_diagnostic.py`
checks the exact clipping-gap factorizations on rational grids, both \(C^1\)
joins, all fifteen regimes, exact transition weights and collision reductions,
the specialized simplex identity, end-to-end original-objective evaluation at
the quadratic-surd optimizer, its primitive irreducible polynomial, isolating
interval, and both squared comparisons in (CR28dq12). Its denominator-12,
-24, and -48 simplex grids have maxima \(1/4\), \(871/3456\), and
\(27907/110592\), all below \(M_4\). This exact computation corroborates but
does not replace the all-real proof.

### Normalized \(k\)-prefix simplex lemma

The compact polynomial behind the one- through four-prefix optimizations
has an exact all-\(k\) solution which is independent of the charging
argument. For \(k\ge1\), put

\[
F_k(x_1,\ldots,x_k)
=\sum_{i=1}^k(x_{i-1}-x_i)x_i^2,
\qquad x_0=1,
\]
\[
M_k=\max_{1\ge x_1\ge\cdots\ge x_k\ge0}F_k(x_1,\ldots,x_k),
\qquad M_0=0.
\tag{CR28cr}
\]

The feasible simplex is compact and \(F_k\) is continuous, so a maximizer
exists. More is true. Homogeneity of degree three in the tail gives the
exact Bellman reduction

\[
M_m
=\max_{0\le y\le1}
\left((1-y)y^2+y^3M_{m-1}\right)
=\max_{0\le y\le1}y^2\left(1-(1-M_{m-1})y\right).
\tag{CR28cs}
\]

Assume inductively that \(0\le M_{m-1}<1/3\), and define

\[
q_m={2\over3(1-M_{m-1})}.
\]

Then \(0<q_m<1\), and for every \(a,b\ge0\) the following exact identity
holds:

\[
\begin{aligned}
a^3M_m-(a-b)b^2-b^3M_{m-1}
={}&(1-M_{m-1})(b-q_ma)^2
\left(b+{q_ma\over2}\right),\\
M_m={q_m^2\over3}
={4\over27(1-M_{m-1})^2}.
\end{aligned}
\tag{CR28ct}
\]

The second line follows either by substituting \(b=q_ma\), or by the unique
positive interior critical point in (CR28cs). The derivative is positive on
\((0,q_m)\) and negative on \((q_m,1]\), so this point is the unique global
maximum. Since \(q_m<1\), it also proves \(M_m<1/3\), closing the induction.
Summing the first line of (CR28ct) for
\((a,b)=(x_{i-1},x_i)\) and remaining lengths \(m=k-i+1\) telescopes to the
global certificate

\[
\boxed{
M_k-F_k(x_1,\ldots,x_k)
=\sum_{i=1}^k(1-M_{k-i})
 (x_i-q_{k-i+1}x_{i-1})^2
 \left(x_i+{q_{k-i+1}x_{i-1}\over2}\right).
}
\tag{CR28cu}
\]

Every summand is nonnegative. Equality forces, successively,

\[
x_i=q_{k-i+1}x_{i-1}
\qquad(1\le i\le k).
\tag{CR28cv}
\]

Thus the maximizer is unique. Moreover \(q_1=2/3\), while
\(2/3<q_m<1\) for \(m\ge2\). Consequently the unique point is strictly
interior:

\[
1>x_1>x_2>\cdots>x_k>0.
\]

For its consecutive ratios \(r_i=x_i/x_{i-1}\), equations
(CR28ct)--(CR28cv) give

\[
r_i=q_{k-i+1},
\qquad
q_1={2\over3},
\qquad
q_{m+1}={2\over3-q_m^2}.
\]

Hence the proposed backward recurrence is confirmed exactly, without a
correction:

\[
\boxed{
r_k={2\over3},
\qquad
r_i={2\over3-r_{i+1}^2}
\quad(1\le i<k).
}
\tag{CR28cw}
\]

The scalar recurrence in (CR28ct) is an exact recursive formula for every
\(M_k\). If

\[
T(u)={4\over27(1-u)^2},
\]

then, for \(0\le u<1/3\),

\[
T(u)-u
={(1-3u)^2(4-3u)\over27(1-u)^2}>0.
\tag{CR28cx}
\]

Therefore \(M_k=T(M_{k-1})\) is strictly increasing and bounded above by
\(1/3\). Its limit \(L\) satisfies \(T(L)=L\). Equivalently,
\((1-3L)^2(4-3L)=0\); since \(L\le1/3\),

\[
\boxed{M_k\nearrow{1\over3}.}
\tag{CR28cy}
\]

The first four rows recover, exactly and in the same normalization, all
documented optimized prefix-simplex values:

| \(k\) | unique maximizer \((x_1,\ldots,x_k)\) | ratios \((r_1,\ldots,r_k)\) | \(M_k\) | \(M_k/8\) |
|---:|---|---|---:|---:|
| 1 | \((2/3)\) | \((2/3)\) | \(4/27\) | \(1/54\) |
| 2 | \((18/23,12/23)\) | \((18/23,2/3)\) | \(108/529\) | \(27/1058\) |
| 3 | \((1058/1263,276/421,184/421)\) | \((1058/1263,18/23,2/3)\) | \(1119364/4785507\) | \(279841/9571014\) |
| 4 | \((3190338,2672508,2091528,1394352)/3666143\) | \((3190338/3666143,1058/1263,18/23,2/3)\) | \(3392752184748/13440604496449\) | \(848188046187/26881208992898\) |

The last column is the scale appearing after
\(X_i=(3\alpha-1)x_i\): it reproduces respectively the one-prefix residual
coefficient, (CR28bw12), (CR28cn), and the four-prefix envelope (CR28dq8).

Purely at the normalized-polynomial level, define on
\(1/3\le\alpha\le1\)

\[
E_k(\alpha)
=p(\alpha)+{M_k\over8}(3\alpha-1)^3.
\tag{CR28cz}
\]

Then (CR28cy) gives uniform monotone convergence on this compact interval:

\[
E_k(\alpha)\nearrow E_\infty(\alpha)
=p(\alpha)+{(3\alpha-1)^3\over24}
={23\alpha^3-39\alpha^2+21\alpha+3\over24}.
\tag{CR28da}
\]

The full formal envelope has the exact factorization

\[
{1\over3}-E_\infty(\alpha)
={(1-\alpha)(23\alpha^2-16\alpha+5)\over24}.
\tag{CR28db}
\]

The quadratic factor is strictly positive because its discriminant is
\(-204\). Thus on the compact closure \([1/3,1]\), the unique global maximum
is

\[
\boxed{\alpha=1,\qquad E_\infty(1)={1\over3}.}
\tag{CR28dc}
\]

On the strict density domain \(\alpha\in[1/3,1)\), this is only a supremum
and is not attained. This endpoint statement must also be separated from the
branch on which the quadratic relaxation (CR28bw10) is an equality. For finite
\(k\), \(x_1=q_k\) is the largest normalized coordinate, so all cutoffs
remain in the middle-branch closure if and only if
\((3\alpha-1)q_k\le(1+\alpha)/3\). Its exact density interval is
\[
{1\over3}\le\alpha\le{3q_k+1\over9q_k-1}.
\]
Since \(q_k\to1\), these intervals converge to
\(1/3\le\alpha\le1/2\). On that limiting interval,

\[
E_\infty'(\alpha)={23\alpha^2-26\alpha+7\over8}
\]

has the unique maximizing root

\[
\boxed{
\alpha_{\rm mid}={13-2\sqrt2\over23},
\qquad
E_\infty(\alpha_{\rm mid})={434+4\sqrt2\over1587}.
}
\tag{CR28dd}
\]

The other root \((13+2\sqrt2)/23\) is a local minimum of the full cubic.
In particular, (CR28dd) is a middle-branch normalized candidate, whereas
(CR28dc) is the global maximum of the displayed formal compact envelope.

The normalized-simplex argument itself proves no charging theorem. The
separate direct argument below supplies charging for every finite admissible
number of selected prefixes. It does not follow from the recurrence or the
limit \(M_k\to1/3\), and it supplies no control uniform in a growing
\(k=k(n)\). Both envelope optimizations remain statements about the normalized
compact polynomial only; they do not promote either value in (CR28dc) or
(CR28dd) to a lower bound for \(\Lambda_n\) or change any established
statement about \(R_2^*(n)\).

### Arbitrarily many finite selected prefixes with one slack partition

The preceding cases are instances of one finite theorem whose proof does not
depend on the number of selected frontiers. The normalized simplex
(CR28cr)--(CR28dd) is independent of this charging statement, so the proof
returns directly to literal split histories. No coefficient optimization,
finite-rounding specialization, growing-prefix limit, or geometric deduction
is made.

Fix an arbitrary integer \(k\ge1\), together with

\[
0<\beta_k<\cdots<\beta_1<\alpha<1,
\qquad
0\le\lambda_k\le\cdots\le\lambda_1\le1,
\]

and put

\[
r=\lfloor\alpha n\rfloor,
\qquad
s_i=\lceil\beta_i n\rceil\quad(1\le i\le k),
\qquad
s_0=r,
\qquad
\lambda_{k+1}=0.
\tag{CR28dr}
\]

At the given finite \(n\), assume the complete admissibility conditions

\[
2\le r\le n-2,
\qquad
1\le s_k<\cdots<s_1\le r-1.
\]

They imply \(k\le r-1\le n-3\). Conversely, for every fixed finite
parameter tuple above,
\[
\delta
=\min\bigl(
\{\beta_k,\alpha-\beta_1,1-\alpha\}
\cup\{\beta_i-\beta_{i+1}:1\le i<k\}
\bigr)>0,
\]
where the second set is empty when \(k=1\). This makes the integer conditions
valid for all sufficiently large \(n\), with a threshold that may depend on
the whole tuple.

For an arbitrary compatible literal history, let
\(\mathcal H_j\) denote the chronological correction prefixes from (CR28ai),
and retain the selected heights

\[
H_0=0,
\qquad
H_i=\sum_{t=s_i}^{r-1}A_t
=\mathcal H_{r-s_i}\quad(1\le i\le k).
\]

Thus the exact history objective
\(\max_{0\le j\le r-1}\mathcal H_j\) contains
\(0,H_1,\ldots,H_k\). Define

\[
c_0=1-\lambda_1,
\qquad
c_i=\lambda_i-\lambda_{i+1}\quad(1\le i\le k).
\]

These \(k+1\) coefficients are nonnegative and sum to one. Their convex
combination of \((0,H_1,\ldots,H_k)\) therefore gives

\[
\boxed{
\max_{0\le j\le r-1}\mathcal H_j
\ge\max(0,H_1,\ldots,H_k)
\ge\sum_{i=1}^k(\lambda_i-\lambda_{i+1})H_i.
}
\tag{CR28ds}
\]

For a universal inequality over arbitrary real selected heights, this is
exactly the convex region: negative height coefficients fail on a single
coordinate tending to \(-\infty\), and total height coefficient greater than
one fails when all heights are equal and positive. The ordered
\(\lambda_i\) parameterize that region by
\(\lambda_i=\sum_{j=i}^k c_j\).

Set

\[
I_i=\{s_i,\ldots,s_{i-1}-1\}\quad(1\le i\le k).
\]

The segments are pairwise disjoint and nonempty. Summation by parts, before
any edge slack is assigned, gives the explicit \(k\)-segment telescope

\[
\begin{aligned}
\sum_{i=1}^k(\lambda_i-\lambda_{i+1})H_i
&=\lambda_1H_1+\sum_{i=2}^k\lambda_i(H_i-H_{i-1})\\
&=\sum_{i=1}^k\lambda_i\sum_{t=s_i}^{s_{i-1}-1}A_t.
\end{aligned}
\tag{CR28dt}
\]

Write \(\lambda_t=\lambda_i\) for \(t\in I_i\), retain

\[
\Delta_e={(u+v-n-r)^2\over2}
\qquad(e=\{u,v\}\in E(C_0)),
\]

and define

\[
F_{i,n}=G_{n,\lambda_i}(s_i)\quad(1\le i\le k),
\tag{CR28du}
\]

with \(G\) as in (CR28az).

There is one canonical one-use partition of the original-edge slack for each
literal history. Let \(E_0=E(C_0)\), and let \(B\) be the set of selected
labels whose split uses an untouched original edge \(e_t\in E_0\). The map
\(t\mapsto e_t\) is injective: splitting an original edge removes it, and
every newly created edge contains the inserted label below \(r\), so later
subdivisions cannot recreate an edge joining the same two original endpoints.
The base-slack identity (CR28ax) therefore has the exact history-relative
partition

\[
\begin{aligned}
P(C_0)-P_{r,n}+\sum_{i=1}^k\lambda_i
 \sum_{t\in I_i}A_t
={}&
\sum_{t\in B}(\Delta_{e_t}+\lambda_tA_t)
+\sum_{\substack{s_k\le t\le r-1\\t\notin B}}\lambda_tA_t\\
&+\sum_{e\in E_0\setminus\{e_t:t\in B\}}\Delta_e.
\end{aligned}
\tag{CR28dv}
\]

Every original slack thus occurs exactly once: beside its unique selected
base split, or in the unused sum. Here ``unused'' means uncharged over the
selected range \(s_k\le t\le r-1\); the edge may be split later below that
range. The partition is canonical relative to the literal history, not a
claim of uniqueness among arbitrary numerical decompositions when some
\(\Delta_e\) vanishes.

The recursive invariant is independent of both \(k\) and the number of
frontiers already crossed. Immediately before inserting \(t\), let
\(\mathcal Q(t)\) be the assertion that every current edge is either an
untouched edge of \(E_0\), or has an endpoint in
\(\{t+1,\ldots,r-1\}\). At \(t=r-1\), every edge is original. If
\(\mathcal Q(t)\) holds, every unsplit edge retains its class, while the two
children of the split edge are incident to \(t\); immediately before the next
insertion \(t-1\), that endpoint belongs to
\(\{t,\ldots,r-1\}\). Descending induction proves \(\mathcal Q(t)\) through
\(t=s_k\). Segment boundaries change only \(\lambda_t\), never the edge
update, so the induction covers any finite number of them, arbitrary nesting,
and edges whose two endpoints were inserted earlier.

For \(t\in I_i\), equations (CR28ay) and (CR28bc) give, on a base split,

\[
\Delta_{e_t}+\lambda_iA_t
\ge G_{n,\lambda_i}(t)\ge F_{i,n}.
\]

On a recursive split, \(\mathcal Q(t)\) permits (CR28ba)--(CR28bd), and
hence

\[
\lambda_iA_t
\ge J_{n,\lambda_i}(t)
\ge G_{n,\lambda_i}(t)
\ge F_{i,n}.
\]

These inequalities include \(\lambda_i=0\), when both local floors vanish.
Discarding only the nonnegative unused sum in (CR28dv), applying (CR28ds),
and minimizing over compatible histories proves, without any sign assumption
on the individual \(F_{i,n}\), the exact finite theorem

\[
\boxed{
\gamma^{(r)}_{1,n}
\ge
P_{r,n}
+\sum_{i=1}^k(s_{i-1}-s_i)F_{i,n}
=
P_{r,n}
+\sum_{i=1}^k(s_{i-1}-s_i)G_{n,\lambda_i}(s_i).
}
\tag{CR28dw}
\]

The case \(k=1\) has the two coefficients
\(1-\lambda_1,\lambda_1\), one segment, and no frontier; it recovers
(CR28bg). The case \(k=5\) recovers the former five-segment statement
(CR28dw). Equal adjacent weights merely make one convex coefficient zero,
and zero weights remain valid. Since \(k\) was arbitrary and the induction
contains no frontier count, the same proof establishes the bound for every
finite admissible \(k\), rather than repeatedly reusing the base-slack pool.

This pointwise finite theorem can be instantiated on any individual
admissible row, even if its finite \(k\) was selected as a function of that
row. It supplies no cutoff threshold, rounding estimate, or parameter control
uniform in a growing family \(k=k(n)\), and therefore justifies no exchange
of \(n\to\infty\) with \(k\to\infty\), no infinite-prefix passage, no
coefficient optimization, and no asymptotic or geometric consequence.

The earlier five-prefix dossier oracle uses
\[
(n,r,C_0)=(17,13,(13,17,14,16,15)),
\quad
(s_1,s_2,s_3,s_4,s_5)=(12,11,10,9,8),
\]
\[
(\lambda_1,\lambda_2,\lambda_3,\lambda_4,\lambda_5)
=(5/6,2/3,1/2,1/3,1/6).
\]
The five-edge base is the smallest edge cardinality that permits a history
with five distinct original-edge charges. Exact standard-library `Fraction`
arithmetic checks all
\(5\cdot6\cdot7\cdot8\cdot9=15{,}120\) local histories, all with distinct
final cycles. Among them, 120 charge all five original edges and 2,520 use an
edge with two previously inserted endpoints at the fifth split. Every history
satisfies the specialized convex identity, canonical partition (CR28dv),
recursive invariant, local floors, and \(k=5\) instance of (CR28dw). This
bounded computation is historical independent corroboration, not the
all-history proof.

The sole new dossier-local corroboration specializes the theorem to
\[
(n,r,C_0)=(20,15,(15,20,16,19,17,18)),
\quad
(s_1,\ldots,s_6)=(14,13,12,11,10,9),
\]
\[
(\lambda_1,\ldots,\lambda_6)
=(6/7,5/7,4/7,3/7,2/7,1/7).
\]
The six-edge base is the minimum cardinality permitting six simultaneous
original-edge charges. Exact standard-library arithmetic checks all
\(6\cdot7\cdot8\cdot9\cdot10\cdot11=332{,}640\) literal histories.
They include 720 histories charging all six original edges and 60,480 sixth
splits between two previously inserted labels. Every history passes the
convex telescope, canonical partition, recursive invariant, local floors, and
the \(k=6\) instance of (CR28dw). This bounded oracle is not production
enumeration and does not replace the indexed proof.

### Explicit five-prefix rational asymptotic witness

The two preceding theorems can now be combined at one fixed finite value
\(k=5\). This is not a use of the limit \(M_k\to1/3\), and no global
optimization of the five-prefix parameters is needed. From (CR28ct)--(CR28cw),

\[
q_5={26881208992898\over30143556935103},
\qquad
M_5={722599396919860307414438404
 \over2725902074099388500860861827}.
\]

Put

\[
D=30143556935103,
\]

and

\[
\begin{aligned}
(N_1,N_2,N_3,N_4,N_5)=({}&26881208992898,23392470652668,
19595592993288,\\
&15335681473008,10223787648672).
\end{aligned}
\]

The consecutive simplex ratios are

\[
\left(q_5,{3190338\over3666143},{1058\over1263},{18\over23},{2\over3}\right),
\]

so the unique \(k=5\) point and its exact value are

\[
\boxed{
(x_1,x_2,x_3,x_4,x_5)={1\over D}(N_1,N_2,N_3,N_4,N_5),
\qquad F_5(x)=M_5.
}
\tag{CR28dx}
\]

Choose, as a fixed rational density,

\[
\alpha={13\over30},
\qquad
s=1+\alpha={43\over30},
\qquad
A=3\alpha-1={3\over10}.
\]

For \(X_i=Ax_i\), take the middle-clipped parameters

\[
\boxed{
\beta_i={s+X_i\over4}={43D+9N_i\over120D},
\qquad
\lambda_i=4-{s\over\beta_i}
={X_i\over\beta_i}={36N_i\over43D+9N_i}.
}
\tag{CR28dy}
\]

In reduced form they are

\[
\begin{array}{c|c|c}
i&\beta_i&\lambda_i\\ \hline
1&512701276381837/1205742277404120
 &322574507914776/512701276381837\\
2&502235061361147/1205742277404120
 &280709647832016/502235061361147\\
3&21341062103609/52423577278440
 &10223787648672/21341062103609\\
4&20785421470529/52423577278440
 &8001225116352/20785421470529\\
5&20118652710833/52423577278440
 &5334150077568/20118652710833.
\end{array}
\]

The ordering and branch claims are exact. The displayed integers satisfy

\[
D>N_1>N_2>N_3>N_4>N_5>0,
\]

hence \(1>x_1>\cdots>x_5>0\) and
\(A>X_1>\cdots>X_5>0\). With
\(L=s/4=43/120\) and \(U=s/3=43/90\), one has

\[
\beta_i-L={X_i\over4}>0,
\qquad
\alpha-\beta_i={A-X_i\over4}>0,
\]

and

\[
U-\beta_i={s-3X_i\over12}
>{s-3A\over12}={2\over45}>0.
\]

Thus all five cutoffs are strictly middle and

\[
0<\beta_5<\beta_4<\beta_3<\beta_2<\beta_1<\alpha<1.
\]

Moreover \(h(X)=4X/(s+X)\) is strictly increasing for \(X>0\), while
\(3X_i<s\). Consequently

\[
\boxed{
0<\lambda_5<\lambda_4<\lambda_3<\lambda_2<\lambda_1<1.
}
\tag{CR28dz}
\]

This proves the complete continuous parameter admissibility. Since every
inequality is strict, the integer conditions in (CR28dr) hold for all
sufficiently large \(n\), with a threshold depending on this fixed tuple. No
threshold, finite rounding estimate, or rounded finite theorem is derived
here.

On the middle branch, (CR28bw3) gives

\[
g(\alpha,\beta_i,\lambda_i)={X_i^2\over2},
\qquad
\beta_{i-1}-\beta_i={X_{i-1}-X_i\over4},
\]

where \(X_0=A\) and \(\beta_0=\alpha\). Therefore the fixed-parameter
coefficient obtained from (CR28dw) is

\[
\begin{aligned}
C_{5,\mathrm{rat}}
&=p(\alpha)+\sum_{i=1}^5
  (\beta_{i-1}-\beta_i)g(\alpha,\beta_i,\lambda_i)\\
&=p\!\left({13\over30}\right)+{A^3\over8}F_5(x)
 ={44693\over162000}+{27M_5\over8000}\\
&=\boxed{
{2263404122555368590593580404287
 \over8177706222298165502582585481000}}.
\end{aligned}
\tag{CR28dz1}
\]

The subscript “rat” is deliberate: no claim is made that this point is the
global five-prefix optimizer. To compare it exactly with (CR28dq11), write

\[
C_{4,*}={a+b\sqrt d\over c}
\]

with

\[
\begin{aligned}
a&=597580022071777213687318156,
&b&=21288970076515705538,\\
d&=2903456040383,
&c&=2290468477489828247376833403.
\end{aligned}
\]

If \(C_{5,\mathrm{rat}}=N/Q\), then

\[
271N-75Q=54550540142475357166378486777>0,
\]

so \(C_{5,\mathrm{rat}}>75/271\). In the other direction, put

\[
G=75c-271a=9840949830285493643999284949>0.
\]

Exact integer arithmetic gives

\[
G^2-d(271b)^2
=202909790739538065073835756341295480167322654096276669>0.
\]

All quantities being positive, \(G>271b\sqrt d\), and hence

\[
\boxed{
C_{5,\mathrm{rat}}>{75\over271}>C_{4,*}.
}
\tag{CR28dz2}
\]

Finally apply the exact \(k=5\) instance of (CR28dw), use the pointwise global
comparison (CR28ap), divide by \(n^3\), and take the usual fixed-parameter
limit. The exact additive relation (CR28) transfers the same coefficient
with its \(O(n^2)\) additive error removed after normalization. Thus

\[
\boxed{
\liminf_{n\to\infty}{\Lambda_n\over n^3}
\ge C_{5,\mathrm{rat}}>C_{4,*},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\ge{C_{5,\mathrm{rat}}\over\pi}>{C_{4,*}\over\pi}.
}
\tag{CR28dz3}
\]

This is an exact method-specific asymptotic corollary at one fixed rational
five-prefix point. The finite theorem below retains exactly the same tuple; it
does not change the fact that the point is a witness rather than a global
\(k=5\) optimizer. The standalone script in
ops/TASK-20260717__five_prefix_explicit_asymptotic_witness/fraction_diagnostic.py
uses only fractions.Fraction and checks the recurrence, simplex identities,
stationarity, reduced parameters, strict branch conditions, both coefficient
evaluations, and the two exact comparison margins. It corroborates but does
not replace this derivation.

#### Finite floor/ceiling theorem for the same rational witness

Retain without change \(\alpha\), every \(x_i\), every \(\beta_i\), and
every \(\lambda_i\) from (CR28dx)--(CR28dz). For an integer \(n\ge1\), put

\[
r_n=\left\lfloor{13n\over30}\right\rfloor,
\qquad
s_{i,n}=\lceil\beta_i n\rceil\quad(1\le i\le5),
\qquad
s_{0,n}=r_n,
\qquad
S_n=n+r_n.
\tag{CR28dz4}
\]

We first determine the complete uniform domain. The smallest top density gap
is

\[
\alpha-\beta_1
={652469588441\over80382818493608}.
\]

Since

\[
r_n-s_{1,n}>(\alpha-\beta_1)n-2,
\qquad
247(\alpha-\beta_1)-2
={394351357711\over80382818493608}>0,
\tag{CR28dz5}
\]

the first segment is nonempty for every \(n\ge247\). The four internal
density gaps are increasing; the smallest is

\[
\beta_1-\beta_2={348873834023\over40191409246804},
\qquad
234(\beta_1-\beta_2)-1
={20722533957289\over20095704623402}>0.
\]

Thus
\(s_{1,n}>s_{2,n}>s_{3,n}>s_{4,n}>s_{5,n}\) for every
\(n\ge234\), because each ceiling-error difference is greater than \(-1\).

The finite middle branches require

\[
{S_n\over4}<s_{i,n}<{S_n\over3}\quad(1\le i\le5).
\]

Write

\[
\eta_n=\alpha n-r_n\in[0,1),
\qquad
\varepsilon_{i,n}=s_{i,n}-\beta_i n\in[0,1).
\]

With \(X_i=Ax_i\), the lower inequalities are automatic:

\[
4s_{i,n}-S_n
=X_i n+4\varepsilon_{i,n}+\eta_n>0.
\]

For the upper inequalities the smallest density gap occurs at \(i=1\):

\[
u_1=(1+\alpha)-3\beta_1
={190126768467061\over1205742277404120},
\qquad
26u_1-4
={60163435263553\over602871138702060}>0.
\]

Hence

\[
S_n-3s_{i,n}
>\bigl((1+\alpha)-3\beta_i\bigr)n-4
\ge u_1n-4>0
\qquad(n\ge26).
\tag{CR28dz6}
\]

The remaining block conditions \(2\le r_n\le n-2\) and
\(s_{5,n}\ge1\) are immediate on the range below. Exact rational
floor/ceiling evaluation closes the only gap between (CR28dz5) and the
candidate threshold:

| \(n\) | \(r_n\) | \(s_{1,n}\) | \(s_{2,n}\) | \(s_{3,n}\) | \(s_{4,n}\) | \(s_{5,n}\) |
|---:|---:|---:|---:|---:|---:|---:|
| 233 | 100 | 100 | 98 | 95 | 93 | 90 |
| 234 | 101 | 100 | 98 | 96 | 93 | 90 |
| 235 | 101 | 100 | 98 | 96 | 94 | 91 |
| 236 | 102 | 101 | 99 | 97 | 94 | 91 |
| 237 | 102 | 101 | 99 | 97 | 94 | 91 |
| 238 | 103 | 102 | 100 | 97 | 95 | 92 |
| 239 | 103 | 102 | 100 | 98 | 95 | 92 |
| 240 | 104 | 103 | 100 | 98 | 96 | 93 |
| 241 | 104 | 103 | 101 | 99 | 96 | 93 |
| 242 | 104 | 103 | 101 | 99 | 96 | 93 |
| 243 | 105 | 104 | 102 | 99 | 97 | 94 |
| 244 | 105 | 104 | 102 | 100 | 97 | 94 |
| 245 | 106 | 105 | 103 | 100 | 98 | 95 |
| 246 | 106 | 105 | 103 | 101 | 98 | 95 |

Every row from \(234\) through \(246\) is admissible, has five nonempty
segments, and lies in all five finite middle branches. At \(n=233\), however,
\(r_n=s_{1,n}=100\), so the first segment is empty. Therefore

\[
\boxed{n=234}
\tag{CR28dz7}
\]

is the minimal uniform threshold for all requested conditions. For reference,
at the first valid row the segment lengths are \((1,2,2,3,3)\), the five
lower-middle gaps \(4s_{i,n}-S_n\) are \((65,57,49,37,25)\), and the five
upper-middle gaps \(S_n-3s_{i,n}\) are \((35,41,47,56,65)\).

The fixed weights are important. Define

\[
F_{i,n}:=G_{n,\lambda_i}(s_{i,n})
={\lambda_i\left(4S_ns_{i,n}-S_n^2
 -2\lambda_i s_{i,n}^2\right)\over2(2-\lambda_i)}.
\tag{CR28dz8}
\]

Although the rounded cutoffs remain in the middle density branches, the
fixed \(\lambda_i\) generally do not equal the finite clipped optima
\(4-S_n/s_{i,n}\). Thus (CR28dz8), rather than
\((4s_{i,n}-S_n)^2/2\), is the required literal floor. Put

\[
\boxed{
\mathcal B_{5,n}:=P_{r_n,n}
+\sum_{i=1}^5(s_{i-1,n}-s_{i,n})F_{i,n},
}
\tag{CR28dz9}
\]

where

\[
P_{r_n,n}
={(n-r_n+1)(r_n^2+4r_n n+r_n+n^2-n)\over6}\in\mathbb Z.
\]

Since the fixed-weight terms in (CR28dz8) need not be half-integers, the
exact integer closure is

\[
\boxed{
\begin{aligned}
\mathcal I_{5,n}
&:=\left\lceil\mathcal B_{5,n}\right\rceil\\
&=P_{r_n,n}
+\left\lceil\sum_{i=1}^5
(s_{i-1,n}-s_{i,n})F_{i,n}\right\rceil.
\end{aligned}
}
\tag{CR28dz10}
\]

The exact \(k=5\) instance of (CR28dw), followed by (CR28ap), gives the
literal chain. Integrality from (CR12h) gives its stronger closure:

\[
\boxed{
\Lambda_n
\ge\Gamma_n^{(r_n)}
\ge\gamma^{(r_n)}_{1,n}
\ge\mathcal B_{5,n},
\qquad
\Lambda_n\ge\mathcal I_{5,n}\ge\mathcal B_{5,n}
}
\qquad(n\ge234).
\tag{CR28dz11}
\]

It remains to compare the literal rounded expression, not the unknown true
block residual, with its cubic coefficient. Set

\[
x_0=1,
\quad x_6=0,
\quad X_i=Ax_i,
\quad X_0=A,
\quad X_6=0,
\quad \beta_0=\alpha,
\quad g_i={X_i^2\over2},
\quad g_6=0,
\]

and, for \(1\le i\le5\), define

\[
d_i=\beta_{i-1}-\beta_i={X_{i-1}-X_i\over4},
\qquad
e_{0,n}=-\eta_n,
\qquad
e_{i,n}=\varepsilon_{i,n},
\qquad
\delta_{i,n}=e_{i-1,n}-e_{i,n}.
\]

Then

\[
s_{i-1,n}-s_{i,n}=d_i n+\delta_{i,n}.
\]

Define the exact lower-order terms

\[
h_{i,n}=X_i(4\varepsilon_{i,n}+\eta_n),
\qquad
k_{i,n}=-{X_i\over(1+\alpha)-X_i}
\left(\eta_n^2+4\eta_n\varepsilon_{i,n}
 +2\lambda_i\varepsilon_{i,n}^2\right).
\]

Direct substitution in (CR28az), using the fixed relation (CR28dy), gives

\[
\boxed{
F_{i,n}=g_i n^2+h_{i,n}n+k_{i,n}.
}
\tag{CR28dz12}
\]

The pairing floor has the exact expansion

\[
\begin{aligned}
P_{r_n,n}={}&p(\alpha)n^3
+\left({13\over30}+{49\over1800}\eta_n\right)n^2\\
&-\left({43\over60}\eta_n^2+\eta_n+{17\over180}\right)n
+{\eta_n^3-\eta_n\over6}.
\end{aligned}
\tag{CR28dz13}
\]

Now use
\(C_{5,\mathrm{rat}}=p(\alpha)+\sum_i d_i g_i\). The coefficient of
\(\varepsilon_{j,n}n^2\) in the exact subtraction is

\[
4d_jX_j-g_j+g_{j+1}
={A^2\over2}
\left(2x_{j-1}x_j-3x_j^2+x_{j+1}^2\right)=0
\]

by the five stationarity equations obtained by differentiating (CR28cr) at
the strict point (CR28dx). Also
\(\sum_i d_iX_i=g_1/4\). Consequently the complete exact remainder is

\[
\boxed{
\mathcal B_{5,n}-C_{5,\mathrm{rat}}n^3
=\left({13\over30}+K\eta_n\right)n^2+Q_n n+T_n,
}
\tag{CR28dz14}
\]

where

\[
\begin{aligned}
Q_n={}&-\left({43\over60}\eta_n^2+\eta_n+{17\over180}\right)
+\sum_{i=1}^5\left(d_i k_{i,n}+\delta_{i,n}h_{i,n}\right),\\
T_n={}&{\eta_n^3-\eta_n\over6}
+\sum_{i=1}^5\delta_{i,n}k_{i,n},
\end{aligned}
\tag{CR28dz15}
\]

and

\[
\begin{aligned}
K
&={49\over1800}+\sum_{i=1}^5d_iX_i-g_1
={49\over1800}-{3g_1\over4}\\
&={34730769300472139183348711
 \over90863402469979616695362060900}>0.
\end{aligned}
\tag{CR28dz16}
\]

The sign can be controlled uniformly without inspecting residue classes.
Indeed \((1+\alpha)-X_i>17/15>1\),
\(0<X_i<3/10\), and \(0<\lambda_i<1\), so

\[
0\le h_{i,n}<{3\over2},
\qquad
-3<k_{i,n}\le0,
\qquad
\sum_{i=1}^5d_i=\alpha-\beta_5<{1\over2}.
\]

For the middle estimate,
\(lvert k_{i,n}\rvert<(3/10)\,7/(17/15)=63/34<3\).

Moreover
\(\delta_{1,n}\in(-2,0]\) and
\(\delta_{i,n}\in(-1,1)\) for \(i\ge2\). The first bracket in \(Q_n\)
is less than \(2\). Termwise use of these rational bounds in (CR28dz15)
gives

\[
Q_n>-{25\over2},
\qquad
T_n>-{109\over6}.
\]

Since \(K\eta_n\ge0\), the exact remainder therefore satisfies

\[
\boxed{
\mathcal B_{5,n}-C_{5,\mathrm{rat}}n^3
>{13\over30}n^2-{25\over2}n-{109\over6}.
}
\tag{CR28dz17}
\]

The right side equals \(623533/30>0\) at \(n=234\). Its forward
difference there is \(2861/15>0\) and increases with \(n\). Hence there are
no failures on the minimal uniform domain:

\[
\boxed{
\Lambda_n\ge\mathcal I_{5,n}\ge\mathcal B_{5,n}
>C_{5,\mathrm{rat}}n^3
\qquad(n\ge234).
}
\tag{CR28dz18}
\]

Finally, the existing strict additive cyclic-ratio relation gives the finite
geometric consequence

\[
\boxed{
R_2^*(n)
>{\mathcal I_{5,n}\over\pi}-n^2
\ge{\mathcal B_{5,n}\over\pi}-n^2
>{C_{5,\mathrm{rat}}\over\pi}n^3-n^2
\qquad(n\ge234).
}
\tag{CR28dz19}
\]

This is an exact finite method-specific theorem for the already fixed
rational witness. It neither optimizes \(k=5\) nor identifies the true block
residual, an exact value of \(\Lambda_n\) or \(R_2^*(n)\), a limiting
coefficient, or a new geometric lemma. The sole new dossier diagnostic uses
only standard-library `Fraction` arithmetic, checks the exact boundary rows,
minimality, symbolic-tail margins, literal expression, integer closure, and
remainder identities, and changes no production path or enumeration limit.

## 5. Exact Scorer Without Cycle Enumeration

The proof that simple cycles suffice does not make their enumeration the
production algorithm. The implemented scorer exploits the special resource
structure of the fixed-order graph.

### Descending-path closure

Edges with \(q\)-contribution zero strictly decrease their position, so they
form a directed acyclic graph. For positions \(h\ge v\), let \(D_{h,v}\) be
the maximum product sum along a descending path from \(h\) to \(v\), allowing
the empty path when \(h=v\). Then
\[
D_{v,v}=0,
\qquad
D_{h,v}
=
\max_{v\le z<h}
\bigl(\sigma_h\sigma_z+D_{z,v}\bigr)
\quad(h>v).
\tag{CR29}
\]
Increasing \(h\) gives an exact acyclic dynamic program.

### One-wrap macro graph

Every closed walk can be split at its \(q(C)\) ascending `wrap_upper` edges.
Each block consists of one ascending edge \(u\to h\), followed by a possibly
empty descending path ending at the tail \(v\) of the next ascending edge.
Position \(n-1\) cannot be such a tail, so the macro vertices are
\(0,\ldots,n-2\). Define the complete macro-edge weights
\[
M_{u,v}
=
\max_{h\ge\max(u+1,v)}
\bigl(\sigma_u\sigma_h+D_{h,v}\bigr).
\tag{CR30}
\]
The macro graph retains the cases \(u=v\) as self-loops; these encode
legitimate original closed walks with one `wrap_upper` occurrence. Every macro
edge has resource one. Compressing an original closed walk gives a macro closed
walk of length \(q(C)\) and at least its product sum. Conversely, expanding
the maximizing witness for every macro edge gives an original closed walk
whose \(q\)-value equals the macro-walk length and whose product sum equals the
macro-walk weight. Its ordinary directed-edge length may be larger. Closed-walk
decomposition then proves that \(\Lambda(\sigma)\) is exactly the maximum cycle
mean of \(M\).

### Karp dynamic program

Put \(N=n-1\). The macro graph is complete and hence strongly connected.
Choose macro vertex zero as a source, set
\[
F_0(0)=0,
\qquad
F_0(v)=-\infty\quad(v\ne0),
\tag{CR31}
\]
and compute
\[
F_k(v)=\max_u\bigl(F_{k-1}(u)+M_{u,v}\bigr)
\qquad(1\le k\le N).
\tag{CR32}
\]
Karp's exact maximum-cycle-mean formula is
\[
\Lambda(\sigma)
=
\max_v
\min_{\substack{0\le k<N\\F_k(v)>-\infty}}
{F_N(v)-F_k(v)\over N-k}.
\tag{CR33}
\]
The implementation represents unreachable states by `None`, not a floating
sentinel. All \(D\), \(M\), and \(F\) values are integers; only the ratios in
(CR33) are constructed and compared as `Fraction`. The descending closure,
macro graph, and Karp recurrence each take \(O(n^3)\) exact integer operations,
and the memory bound is \(O(n^2)\).

The public scorer accepts any complete permutation, not only a canonical one.
The separate global enumerator rejects values outside \(3\le n\le8\), checks
the explicit canonical-order ceiling before generating permutations, and has
no CLI or serialized artifact contract.

The one-wrap theorem proves that every public score has denominator one. The
production implementation deliberately retains its full-ratio Karp algorithm
and `Fraction` result: the new induced-subset and subset/path implementations
remain test-only independent oracles, and the hard production enumeration
domain is unchanged.

## 6. Finite Exact Results

### Public bounded enumeration, \(n=3,\ldots,8\)

The production scorer was minimized over every canonical complete order using
the repository convention: put \(n\) first and retain the reflection with
second label smaller than the last. The direct simple-cycle oracle independently
checked every canonical order through \(n=6\). A separate exact subset/path
dynamic program anchors each simple cycle at its least position and retains
states `(visited subset, last position, wrap count)`; it shares neither the
descending closure, macro graph, nor Karp recurrence with production. That
oracle and literal induced-subset maximization agree order by order for every
canonical order through \(n=8\).

For the comparison columns only, recall the separate core definition
\[
W_n
=
\min_\tau
\max_{0\le u<v\le n-2}
{\tau_u\tau_v\over d_\tau(u,v)},
\tag{CR33a}
\]
where \(\tau\) ranges over cyclic orders of \(\{2,\ldots,n\}\) and
\(d_\tau(u,v)=\min(v-u,n-1-(v-u))\) is smaller circular positional distance.

| \(n\) | Canonical complete orders | \(\Lambda_n\) | Canonical minimizers | Lexicographically least representative | \(W_n\) | \((n-1)W_n\) |
|---:|---:|---:|---:|---|---:|---:|
| 3 | 1 | 12 | 1 | `(3,1,2)` | 6 | 12 |
| 4 | 3 | 26 | 3 | `(4,1,2,3)` | 12 | 36 |
| 5 | 12 | 47 | 4 | `(5,1,2,4,3)` | 15 | 60 |
| 6 | 60 | 77 | 15 | `(6,1,2,3,5,4)` | 20 | 100 |
| 7 | 360 | 118 | 24 | `(7,1,2,3,5,6,4)` | 24 | 144 |
| 8 | 2520 | 172 | 84 | `(8,1,2,3,5,6,7,4)` | 30 | 210 |

This is a **VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION)** over 2,956
canonical orders. The supplied prediction
\[
(\Lambda_3,\ldots,\Lambda_8)=(12,26,47,77,118,172)
\tag{CR34}
\]
is reproduced exactly, so there is no counterexample to preserve in this
bounded domain. The counts and representative orders are additional finite
data, not a closed-form evaluation or conjecture. The independent oracle also
verifies \(\Lambda=\Lambda^{(1)}\) on every one of these bounded orders, but
the all-order equality is the exact proof (CR12a)--(CR12h), not this finite
regression. The production ceiling remains 2,520 canonical orders at
\(n=8\); no larger production enumeration was enabled.

The elimination theorem has a separate test-only regression over every
canonical core order and every cyclic insertion gap. The exact counts are:

| \(n\) | Canonical core orders | Insertion trials | Distinct complete classes | \(\min K=\Lambda_n\) | Core \(K\)-minimizers | Complete \(\Lambda\)-minimizers |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 1 | 2 | 1 | 12 | 1 | 1 |
| 4 | 1 | 3 | 3 | 26 | 1 | 3 |
| 5 | 3 | 12 | 12 | 47 | 1 | 4 |
| 6 | 12 | 60 | 60 | 77 | 3 | 15 |
| 7 | 60 | 360 | 360 | 118 | 4 | 24 |
| 8 | 360 | 2,520 | 2,520 | 172 | 12 | 84 |

In total, 437 core classes and 2,957 insertion trials cover all 2,956
complete classes. The sole duplicate is the explicit \(n=3\) reflection in
(CR12r). For \(n\ge4\), every core class has \(n-1\) distinct labeled cyclic
gaps, so the complete minimizer count is \((n-1)\) times the core minimizer
count. Each insertion is checked both by literal exact subset maximization and
by the production scorer. This is a **VERIFIED FACT (FINITE EXHAUSTIVE EXACT
COMPUTATION)**, not the proof of (CR12p), and it does not extend the production
domain beyond \(n=8\).

### Reduced exact evaluation at \(n=9\), without public enumeration

Put
\[
S_6=\{4,5,6,7,8,9\},
\qquad
S_5=\{5,6,7,8,9\}.
\tag{L9-1}
\]
For a cyclic order \(\omega\) on \(S_6\), write \(P_\omega(S)\) for the
cyclic adjacent-product sum in the order induced on \(S\). Let \(a,b\) be
the two neighbors of label \(4\) in \(\omega\). Deleting \(4\) replaces
the contributions \(4a+4b\) by \(ab\), so
\[
P_\omega(S_6)
=P_\omega(S_5)+4(a+b)-ab
=P_\omega(S_5)+16-(a-4)(b-4).
\tag{L9-2}
\]

The duplicated-multiset rearrangement bound, applied to any cyclic order on
\(S_5\), gives the human-checkable baseline
\[
P_\omega(S_5)
\ge5\cdot9+6\cdot8+7^2+8\cdot6+9\cdot5
=235.
\tag{L9-3}
\]
If \(\{a,b\}\) is neither \(\{7,9\}\) nor \(\{8,9\}\), then the distinct
integers \(a-4,b-4\in\{1,\ldots,5\}\) have product at most \(12\).
Equations (L9-2)--(L9-3) therefore give
\(P_\omega(S_6)\ge235+4=239\).

Only two neighbor pairs remain. Name them so that \(a<b\), and reflect the
cycle if necessary so that the new edge created by deleting label \(4\) is
oriented \(a\to b\). The induced five-cycle can then be written
\((a,b,x,y,z)\). The following table lists all six possibilities for the
three remaining labels, in lexicographic order. Every entry is a direct sum
of five integer products.

| \(\{a,b\}\) | Permutations \((x,y,z)\) | Corresponding values of \(P_\omega(S_5)\) | Minimum |
|---|---|---|---:|
| \(\{7,9\}\) | `568, 586, 658, 685, 856, 865` | `242, 238, 243, 240, 247, 248` | 238 |
| \(\{8,9\}\) | `567, 576, 657, 675, 756, 765` | `245, 242, 247, 243, 248, 247` | 242 |

For \(\{a,b\}=\{7,9\}\), the correction in (L9-2) is \(1\), so
\(P_\omega(S_6)\ge239\). For \(\{a,b\}=\{8,9\}\), the table already gives
\(P_\omega(S_5)\ge242\). This proves the finite exact lemma
\[
\boxed{
\max\{P_\omega(S_6),P_\omega(S_5)\}\ge239
\quad\text{for every cyclic order \(\omega\) on \(S_6\)}.
}
\tag{L9-4}
\]
The argument is a proof, not a conclusion drawn from the 60-class test.

The equality case is equally rigid. In the nonexceptional branch,
simultaneously having both displayed scores at most 239 would force equality
in (L9-3) and correction \(4\) in (L9-2). Equality in the duplicated-multiset
pairing bound would require the five edge pairs

\[
(5,9),(5,9),(6,8),(6,8),(7,7).
\tag{L9-4a}
\]

The loop \((7,7)\) cannot be an edge of a cyclic order on five distinct
labels, so in that branch \(P_\omega(S_5)\ge236\) and
\(P_\omega(S_6)\ge240\). The exceptional pair \(\{8,9\}\) is excluded by
the lower value 242 already displayed in the table. For \(\{7,9\}\), the
correction is \(1\), so both scores are at most 239 only when
\(P_\omega(S_5)\le238\). The table has exactly one such row: `586`, with
value 238. Reinserting label \(4\) between \(7\) and \(9\) gives, up to
rotation and reflection, the unique equality cycle

\[
\Omega=(9,5,8,6,7,4),
\qquad
P_\Omega(S_6)=239,
\qquad
P_\Omega(S_5)=238.
\tag{L9-4b}
\]

Consequently,

\[
\max\{P_\omega(S_6),P_\omega(S_5)\}=239
\quad\Longleftrightarrow\quad
\omega\sim_{\rm dihedral}\Omega.
\tag{L9-4c}
\]

For any core order \(\tau\) of \(\{2,\ldots,9\}\), both \(S_6\) and
\(S_5\) are admitted in the definition of \(K(\tau)\). Applying (L9-4) to
the order induced by \(\tau\) gives
\[
K(\tau)
\ge\max\{P_\tau(S_6),P_\tau(S_5)\}
\ge239.
\tag{L9-5}
\]

For the reverse inequality, consider the supplied core order
\[
\tau_*=(9,2,3,5,8,6,7,4).
\tag{L9-6}
\]
Its complete-core cyclic sum is \(233\). For an oriented arc from \(i\) to
\(j\) in this order, define its shortcut gain by
\[
g(i,j)
=ij-
\sum_{xy\text{ an edge on the oriented arc from }i\text{ to }j}xy.
\tag{L9-7}
\]
Adjacent endpoints have gain zero. The following table gives every
nontrivial gain; \(r\) is the number of skipped internal vertices, and each
cell has the form `endpoint:gain`.

| Start | \(r=1\) | \(r=2\) | \(r=3\) | \(r=4\) | \(r=5\) | \(r=6\) |
|---:|---:|---:|---:|---:|---:|---:|
| 9 | `3:+3` | `5:+6` | `8:-7` | `6:-73` | `7:-106` | `4:-161` |
| 2 | `5:-11` | `8:-45` | `6:-97` | `7:-137` | `4:-171` | `9:-197` |
| 3 | `8:-31` | `6:-85` | `7:-124` | `4:-161` | `9:-182` | `2:-221` |
| 5 | `6:-58` | `7:-95` | `4:-138` | `9:-149` | `2:-202` | `3:-203` |
| 8 | `7:-34` | `4:-86` | `9:-82` | `2:-156` | `3:-154` | `5:-153` |
| 6 | `4:-46` | `9:-52` | `2:-112` | `3:-112` | `5:-115` | `8:-137` |
| 7 | `9:-1` | `2:-68` | `3:-67` | `5:-68` | `8:-87` | `6:-149` |
| 4 | `2:-46` | `3:-48` | `5:-55` | `8:-83` | `6:-139` | `7:-177` |

Let \(U\) be an induced subset with \(|U|\ge2\). The oriented arcs from
each selected label to the next selected label partition the eight edges of
the complete core cycle. Consequently
\[
P_{\tau_*}(U)-233
=\sum_{(i,j)\text{ a selected gap}}g(i,j).
\tag{L9-8}
\]
For \(|U|=2\), the two complementary arcs contribute the two shortcuts
\(ij+ji=2ij\), exactly matching the adopted two-element convention.

The only positive nontrivial gains in the table are \(g(9,3)=3\) and
\(g(9,5)=6\). Exactly one selected gap can leave label \(9\), so (L9-8) is
at most \(6\). Equality forces the gap \(9\to5\), skipping labels \(2,3\),
and every other gap to be adjacent because there is no nontrivial zero gain.
Thus equality forces
\[
U=S_6,
\qquad
\tau_*|_{S_6}=(9,5,8,6,7,4),
\tag{L9-9}
\]
whose score is
\[
9\cdot5+5\cdot8+8\cdot6+6\cdot7+7\cdot4+4\cdot9=239.
\tag{L9-10}
\]
Singleton scores are at most \(9^2=81\). Therefore
\[
K(\tau_*)=239,
\qquad
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,9\}}
P_{\tau_*}(U)=\{S_6\}.
\tag{L9-11}
\]

Combining (L9-5), (L9-11), and the accepted reduction (CR28a) proves the
requested value
\[
\boxed{\Lambda_9=239.}
\tag{L9-12}
\]
This is a **VERIFIED FACT (FINITE EXACT COMBINATORIAL RESULT)**. It neither
extends the production enumeration past \(n=8\) nor gives an exact value of
\(R_2^*(9)\), a geometric statement, an all-\(n\) formula, an asymptotic
claim, or any conclusion about exact angular minimizers.

#### Complete core classification at \(n=9\)

It remains to insert labels \(3\) and \(2\) into the forced six-label cycle
\(\Omega\). Fix the displayed orientation in (L9-4b) and name its gaps

\[
\begin{array}{lll}
h_0:9\to5,&h_1:5\to8,&h_2:8\to6,\\
h_3:6\to7,&h_4:7\to4,&h_5:4\to9.
\end{array}
\tag{L9-13}
\]

Insert label \(3\) into one gap and call the resulting seven-cycle \(C_h\).
The six complete sums are direct one-edge replacement calculations:

| Gap containing `3` | \(C_h\) | \(P(C_h)\) | Status if \(K\le239\) |
|---|---|---:|---|
| \(h_0\) | `(9,3,5,8,6,7,4)` | 236 | possible |
| \(h_1\) | `(9,5,3,8,6,7,4)` | 238 | possible |
| \(h_2\) | `(9,5,8,3,6,7,4)` | 233 | possible |
| \(h_3\) | `(9,5,8,6,3,7,4)` | 236 | possible |
| \(h_4\) | `(9,5,8,6,7,3,4)` | 244 | impossible |
| \(h_5\) | `(9,5,8,6,7,4,3)` | 242 | impossible |

Thus label \(3\) cannot lie in either gap incident to label \(4\). For the
other four rows, apply the shortcut definition (L9-7) to \(C_h\). The exact
certificate compresses to

| \(h\) | Full sum | Sole positive nontrivial shortcut | Gain | Largest other nontrivial gain |
|---:|---:|---|---:|---:|
| 0 | 236 | \(9\to5\), deleting `3` | \(+3\) | \(-1\) |
| 1 | 238 | \(5\to8\), deleting `3` | \(+1\) | \(-1\) |
| 2 | 233 | \(8\to6\), deleting `3` | \(+6\) | \(-1\) |
| 3 | 236 | \(6\to7\), deleting `3` | \(+3\) | \(-1\) |

In every row the unique \(-1\) entry is \(7\to9\), deleting label \(4\);
direct evaluation of the remaining oriented arcs gives still smaller integer
gains. Singletons have score at most \(9^2=81\). For subsets of at least two
labels, selected gaps partition the full cycle as in (L9-8). The sole positive
gap cannot occur in a subset that retains label \(3\), because that shortcut
skips \(3\). Therefore every subset retaining \(3\) has score at most the
displayed full sum. Deleting \(3\) through the sole positive shortcut gives
exactly \(\Omega\) and score 239, and equality forces every other selected gap
to be adjacent. Hence each of the four \(C_h\) has \(K=239\), with \(S_6\)
as its unique maximizing subset before label \(2\) is inserted.

Now insert label \(2\) into an arbitrary gap of one of these four cycles.
For a selected subset \(U\) containing \(2\), put \(V=U\setminus\{2\}\).
When \(|V|\ge2\), let \(a,b\) be the two distinct neighbors of label \(2\)
in the order induced on \(U\). Deleting \(2\) gives the exact change

\[
P(U)-P(V)
=2(a+b)-ab
=4-(a-2)(b-2).
\tag{L9-14}
\]

If \(3\notin V\), then \(a,b\ge4\) and the change is at most \(-2\). If
\(3\in V\), its maximum is \(2\), attained only for
\(\{a,b\}=\{3,4\}\); the only other positive case is
\(\{a,b\}=\{3,5\}\), with change \(1\). The rows \(h=0,2,3\) have full
sum at most 236, so even the change \(2\) stays below 239. In the remaining
row \(h=1\), the pair \(\{3,5\}\) gives at most \(238+1=239\). If the
neighbors are \(\{3,4\}\), those labels are not adjacent in \(C_1\), so
making them adjacent in \(V\) forces a nontrivial shortcut. It cannot be the
positive shortcut that deletes the selected label \(3\), or the unique
\(-1\) shortcut that deletes the selected label \(4\). Every remaining gain
is an integer below \(-1\), so \(P(V)\le236\) and \(P(U)\le238\). In the
\(\{3,5\}\) branch, equality \(P(U)=239\) forces \(P(V)=238\). Because
\(V\) retains \(3\), this in turn forces \(V=C_1\) with no nontrivial
shortcut, and label \(2\) must occupy the gap \(5\to3\). The cases
\(|V|\le1\) have score at most \(4\cdot9=36\). Thus label \(2\) may occupy
every gap, and the only new equality is the one just identified.

This gives the promised human-checkable parametrization:

1. orient the forced six-cycle as \(\Omega=(9,5,8,6,7,4)\);
2. insert `3` in one of \(h_0,h_1,h_2,h_3\), the four gaps not incident to
   label `4`;
3. insert `2` immediately after any one of the seven displayed labels of the
   resulting \(C_h\).

Equivalently, after choosing the gap of `3`, label `2` may occupy any of the
other five original gaps, or the same original gap in either internal order.
The count is therefore

\[
4\cdot7=4(5+2)=28.
\tag{L9-15}
\]

These are 28 distinct dihedral classes: after fixing the displayed orientation
of the induced labelled cycle \(\Omega\), a rotation is fixed by label \(9\),
while a reflection reverses that orientation, so no two different placements
in the parametrization are identified. Conversely, (L9-4c) forces every
minimizer into this list, and the preceding bounds admit every listed order.
This proves the **EXACT THEOREM (FINITE CORE MINIMIZER CLASSIFICATION)**

\[
K(\tau)=239
\quad\Longleftrightarrow\quad
\tau\text{ is one of the 28 classes in (L9-15).}
\tag{L9-16}
\]

All 28 classes maximize on \(S_6\). In 27 classes this is the unique
maximizing subset. The sole exception is represented in the chosen orientation
by

\[
(9,5,2,3,8,6,7,4),
\tag{L9-17}
\]

whose canonical reflected representative is
`(9,4,7,6,8,3,2,5)`: both \(S_6\) and the full core
\(\{2,3,4,5,6,7,8,9\}\) have score 239. Indeed, this is the unique equality
case \(238+1\) in the \(h=1\), \(\{3,5\}\)-neighbor branch above.

Finally, (CR12p)--(CR12q) show that inserting label \(1\) into a core gap
preserves the score and introduces no maximizing subset containing \(1\).
For \(n=9\), the eight labelled gaps of each core class give eight distinct
complete dihedral classes. Indeed, a dihedral equivalence between two
insertions would restrict, after deleting label \(1\), to a label-preserving
dihedral automorphism of the same eight-cycle. Its distinct labels force that
automorphism to be the identity, so the two gaps coincide. Deletion of label
\(1\) also prevents insertions from different core classes from merging.
Hence

\[
\#\{\text{complete dihedral minimizers at }n=9\}
=28\cdot8
=224.
\tag{L9-18}
\]

Of these, 216 have \(S_6\) as their sole maximizing subset, while the eight
insertions into (L9-17) retain the two core maximizing subsets. This count is
a consequence of the exact elimination/insertion theorem, not an enlargement
of the public complete-order enumerator.

#### Independent finite oracles

The independent test-only lower-bound oracle fixes label \(9\) to remove
rotations, generates the \(5!\) remaining permutations directly, and keeps
the orientation whose second label is smaller than its last. It therefore
checks exactly \(5!/2=60\) dihedral classes without calling repository
canonicalizers, the public enumerator, or the production scorer. Its minimum
of \(\max\{P(S_6),P(S_5)\}\) is 239. A separate literal enumeration of all
\(2^8-1=255\) nonempty subsets of \(\tau_*\) verifies (L9-11), records
\(S_6\) as the sole global maximizer, and gives the following independently
reproducible per-cardinality audit:

| \(|U|\) | Maximum score | Unique maximizing subset |
|---:|---:|---|
| 1 | 81 | \(\{9\}\) |
| 2 | 144 | \(\{8,9\}\) |
| 3 | 191 | \(\{7,8,9\}\) |
| 4 | 225 | \(\{6,7,8,9\}\) |
| 5 | 238 | \(S_5\) |
| 6 | 239 | \(S_6\) |
| 7 | 236 | \(\{3,4,5,6,7,8,9\}\) |
| 8 | 233 | \(\{2,3,4,5,6,7,8,9\}\) |

A third, classification-level oracle directly generates

\[
(9,\pi_2,\ldots,\pi_8),
\qquad
(\pi_2,\ldots,\pi_8)\in\operatorname{Perm}(2,\ldots,8),
\qquad
\pi_2<\pi_8.
\tag{L9-19}
\]

It therefore covers exactly \(7!/2=2{,}520\) core dihedral classes, without
calling `canonical_core_orders`, any repository canonicalizer, the public
enumerator, or the production Karp scorer. For every row it literally scores
all 255 nonempty subsets and records every maximizing subset: 642,600 exact
integer subset evaluations in total. The deterministic 84,395-byte
serialization of `(order, score, all maximizing subsets)` has SHA-256
`557226668a82f6489274571148572076e373d49baefaa61e6d1f5a458bb857a2`.
It finds minimum 239, exactly the 28 canonical representatives hard-coded in
the test, 27 unique \(S_6\) argmax records, and the single two-argmax record
(L9-17).

These sweeps are **VERIFIED FACTS (FINITE EXHAUSTIVE EXACT COMPUTATION)** and
independently audit the finite proofs; they are not their source. The number
2,520 here is the `n=9` **core** space and only happens to equal the production
ceiling at `n=8`. Production still hard-rejects `n=9`, and no public
enumeration limit changed.

### Reduced exact evaluation and core classification at \(n=10\), without public enumeration

Put
\[
T_7=\{4,5,6,7,8,9,10\},
\qquad
T_6=\{5,6,7,8,9,10\}.
\tag{L10-1}
\]
Let \(\omega\) be a cyclic order on \(T_7\), and let \(a,b\) be the two
neighbors of label \(4\). Deleting \(4\) replaces the two contributions
\(4a+4b\) by \(ab\), so
\[
P_\omega(T_7)
=P_\omega(T_6)+4(a+b)-ab
=P_\omega(T_6)+16-(a-4)(b-4).
\tag{L10-2}
\]

The six edges of the cycle induced on \(T_6\) pair the duplicated multiset
\[
M=(5,5,6,6,7,7,8,8,9,9,10,10).
\tag{L10-3}
\]
The duplicated-multiset rearrangement bound gives
\[
P_\omega(T_6)
\ge2(5\mathbin\cdot10+6\mathbin\cdot9+7\mathbin\cdot8)
=320.
\tag{L10-4}
\]
Because every cyclic sum is an integer, only the pairing levels 320, 321,
and 322 can require work before the target 323 is automatic. The following
small recurrence classifies them without enumerating cyclic orders.

For an even sorted multiset
\(N=(x_1\le\cdots\le x_{2r})\), define
\[
A(N)=\sum_{i=1}^r x_i x_{2r+1-i},
\qquad A(\varnothing)=0.
\tag{L10-5}
\]
The same rearrangement lemma says that \(A(N)\) is a lower bound for every
pairing of \(N\). A state consists of the remaining multiset \(N\), a
partial cost \(s\), and the multiset \(E\) of pairs already chosen. Take
\(x=\min N\), try each distinct possible mate \(y\), and form
\[
N'=N\setminus\{x,y\},
\qquad
s'=s+xy,
\qquad
E'=E\mathbin\uplus\{(x,y)\}.
\tag{L10-6}
\]
Retain the branch exactly when
\[
s'+A(N')\le322,
\tag{L10-7}
\]
identifying states that differ only by exchanging equal copies. Every
pairing of cost at most 322 survives by following the actual mate of the
least remaining entry; conversely, every leaf is a pairing. Thus the
recurrence is exhaustive.

At the first step, the lower totals for pairing the first copy of \(5\) with
\(y=5,6,7,8,9,10\) are respectively
\[
335, 330, 326, 323, 321, 320,
\tag{L10-8}
\]
so only \(y=9,10\) survive. Continuing the same test leaves, after
\(0,1,\ldots,6\) chosen pairs,
\[
1, 2, 3, 6, 6, 10, 8
\tag{L10-9}
\]
distinct states. The eight leaves are listed below; \((i,j)^2\) denotes a
pair with multiplicity two.

| Value | Multiset of six unordered pairs | Simple six-cycle? |
|---:|---|---|
| 320 | \((5,10)^2,(6,9)^2,(7,8)^2\) | no: repeated pairs |
| 321 | \((5,9),(5,10),(6,9),(6,10),(7,8)^2\) | no: \((7,8)\) repeats |
| 321 | \((5,10)^2,(6,8),(6,9),(7,8),(7,9)\) | no: \((5,10)\) repeats |
| 321 | \((5,10)^2,(6,9)^2,(7,7),(8,8)\) | no: loops |
| 322 | \((5,9)^2,(6,10)^2,(7,8)^2\) | no: repeated pairs |
| 322 | \((5,9),(5,10),(6,8),(6,10),(7,8),(7,9)\) | yes |
| 322 | \((5,9),(5,10),(6,9),(6,10),(7,7),(8,8)\) | no: loops |
| 322 | \((5,10)^2,(6,8)^2,(7,9)^2\) | no: repeated pairs |

A simple cycle on six distinct labels has neither a loop nor a repeated
unordered edge. Hence 320 and 321 are impossible, while 322 forces, up to
rotation and reflection,
\[
C_*=(10,5,9,7,8,6),
\tag{L10-10}
\]
with
\[
P_{C_*}(T_6)
=10\mathbin\cdot5+5\mathbin\cdot9+9\mathbin\cdot7
 +7\mathbin\cdot8+8\mathbin\cdot6+6\mathbin\cdot10
=322.
\tag{L10-11}
\]

It remains to insert label \(4\). On the six edges of \(C_*\), the exact
correction \(\delta(a,b)=4(a+b)-ab\) in (L10-2) is

| Edge \(\{a,b\}\) | \(\delta(a,b)\) |
|---|---:|
| \(\{5,10\}\) | 10 |
| \(\{5,9\}\) | 11 |
| \(\{7,9\}\) | 1 |
| \(\{7,8\}\) | 4 |
| \(\{6,8\}\) | 8 |
| \(\{6,10\}\) | 4 |

Every correction is at least one. If \(P_\omega(T_6)\ge323\), the desired
maximum is already at least 323. Otherwise (L10-4) and the complete
classification force \(P_\omega(T_6)=322\) and the induced cycle to be
\(C_*\), so (L10-2) gives \(P_\omega(T_7)\ge323\). This proves the exact
finite lemma
\[
\boxed{
\max\{P_\omega(\{4,\ldots,10\}),
      P_\omega(\{5,\ldots,10\})\}\ge323
}
\tag{L10-12}
\]
for every cyclic order \(\omega\) on \(\{4,\ldots,10\}\). The pairing
recurrence and insertion table are the proof; the finite oracle below is an
independent check, not its source.

For any core order \(\tau\) of \(\{2,\ldots,10\}\), the order induced on
\(T_7\) satisfies (L10-12), and both displayed subsets occur in the
definition of \(K\). Therefore
\[
K(\tau)
\ge\max\{P_\tau(T_7),P_\tau(T_6)\}
\ge323.
\tag{L10-13}
\]

For the reverse inequality, take the supplied core order
\[
\tau_*=(10,2,3,4,7,8,6,9,5).
\tag{L10-14}
\]
Its nine cyclic edge products are
\[
20,6,12,28,56,48,54,45,50,
\]
and hence its complete-core sum is
\[
B=P_{\tau_*}(\{2,\ldots,10\})=319.
\tag{L10-15}
\]
For an oriented arc from \(i\) to \(j\) in \(\tau_*\), define the exact
shortcut gain
\[
g(i,j)
=ij-
\sum_{xy\text{ an edge on the oriented arc from }i\text{ to }j}xy.
\tag{L10-16}
\]
Adjacent endpoints have gain zero. The following table records every
nontrivial gain; \(r\) is the number of skipped internal labels, and each
entry has the form `endpoint:gain`.

| Start | \(r=1\) | \(r=2\) | \(r=3\) | \(r=4\) | \(r=5\) | \(r=6\) | \(r=7\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | `3:+4` | `4:+2` | `7:+4` | `8:-42` | `6:-110` | `9:-134` | `5:-219` |
| 2 | `4:-10` | `7:-32` | `8:-86` | `6:-138` | `9:-186` | `5:-239` | `10:-279` |
| 3 | `7:-19` | `8:-72` | `6:-126` | `9:-171` | `5:-228` | `10:-263` | `2:-307` |
| 4 | `8:-52` | `6:-108` | `9:-150` | `5:-211` | `10:-241` | `2:-293` | `3:-295` |
| 7 | `6:-62` | `9:-95` | `5:-168` | `10:-183` | `2:-259` | `3:-258` | `4:-263` |
| 8 | `9:-30` | `5:-107` | `10:-117` | `2:-201` | `3:-199` | `4:-203` | `7:-207` |
| 6 | `5:-69` | `10:-89` | `2:-157` | `3:-157` | `4:-163` | `7:-173` | `8:-223` |
| 9 | `10:-5` | `2:-97` | `3:-94` | `4:-97` | `7:-98` | `8:-145` | `6:-211` |
| 5 | `2:-60` | `3:-61` | `4:-68` | `7:-81` | `8:-132` | `6:-190` | `9:-229` |

Every entry is an integer subtraction from the displayed edge products.
Complementary arcs give the additional audit identity
\[
g(i,j)+g(j,i)=2ij-B=2ij-319.
\tag{L10-17}
\]

Let \(U\) be an induced subset with \(|U|\ge2\). The oriented arcs from
each selected label to the next selected label partition the nine edges of
the complete core cycle. Consequently,
\[
P_{\tau_*}(U)-319
=\sum_{(i,j)\text{ a selected gap}}g(i,j).
\tag{L10-18}
\]
For \(|U|=2\), the two complementary arcs supply both occurrences of the
same unordered product, as required by the two-element convention.

The only positive nontrivial gains are
\[
g(10,3)=4,
\qquad
g(10,4)=2,
\qquad
g(10,7)=4.
\tag{L10-19}
\]
All three leave label \(10\), and exactly one selected gap can leave a given
selected label. Thus the sum in (L10-18) is at most four. There is no
nontrivial zero gain, so equality requires either the shortcut \(10\to3\)
or \(10\to7\), with every other selected gap adjacent. These two cases give
exactly
\[
U_8=\{3,4,5,6,7,8,9,10\},
\qquad
U_6=\{5,6,7,8,9,10\}.
\tag{L10-20}
\]
Their sums are, respectively,
\[
10\mathbin\cdot3+3\mathbin\cdot4+4\mathbin\cdot7
+7\mathbin\cdot8+8\mathbin\cdot6+6\mathbin\cdot9
+9\mathbin\cdot5+5\mathbin\cdot10
=323
\tag{L10-21}
\]
and
\[
10\mathbin\cdot7+7\mathbin\cdot8+8\mathbin\cdot6
+6\mathbin\cdot9+9\mathbin\cdot5+5\mathbin\cdot10
=323.
\tag{L10-22}
\]
Singleton scores are at most \(10^2=100\). Therefore the shortcut table is
an exact certificate that
\[
K(10,2,3,4,7,8,6,9,5)=323,
\tag{L10-23}
\]
with precisely \(U_6\) and \(U_8\) as its maximizing subsets.

Combining (L10-13), (L10-23), and the accepted reduction (CR28a) proves
\[
\boxed{\Lambda_{10}=323.}
\tag{L10-24}
\]
This is a **VERIFIED FACT (FINITE EXACT COMBINATORIAL RESULT)**. It does not
give an exact value of \(R_2^*(10)\), change the production scorer, enlarge
the public enumeration domain, classify the `n=10` core minimizers, or imply
a geometric, all-\(n\), or asymptotic statement.

#### Structural equality classification for the seven-label lemma

The equality cases of (L10-12) can be classified without enumerating cyclic
orders. Write
\[
s=P_\omega(T_6),
\qquad
q=P_\omega(T_7),
\qquad
q=s+\delta(a,b),
\tag{L10-25}
\]
where \(\{a,b\}\) is the edge of the induced tail cycle split by label \(4\)
and
\[
\delta(a,b)=4(a+b)-ab=16-(a-4)(b-4).
\tag{L10-26}
\]
Suppose \(\max\{q,s\}=323\). Then \(s\le323\). The pairing lower bound
(L10-4) and the complete 320--322 signature table show that a simple tail
cycle cannot have score 320 or 321. Hence only the two branches
\[
s=322
\qquad\hbox{or}\qquad
s=323
\tag{L10-27}
\]
remain.

In the branch \(s=322\), the same table forces the unique dihedral tail class
\[
C_*=(10,5,9,7,8,6).
\tag{L10-28}
\]
All six corrections were computed in the insertion table above. Since
\[
\max\{322,322+\delta(a,b)\}=323
\quad\Longleftrightarrow\quad
\delta(a,b)=1,
\tag{L10-29}
\]
only the edge \(\{7,9\}\) survives. Inserting label \(4\) there gives
\[
\omega_{322}=(10,5,9,4,7,8,6),
\qquad
(q,s)=(323,322).
\tag{L10-30}
\]

It remains to treat the genuinely different branch \(s=323\). Here equality
requires \(q\le323\), or equivalently \(\delta(a,b)\le0\). For completeness,
the correction on every one of the 15 possible unordered pairs of distinct
tail labels is

| \(a\backslash b\) | 6 | 7 | 8 | 9 | 10 |
|---:|---:|---:|---:|---:|---:|
| 5 | 14 | 13 | 12 | 11 | 10 |
| 6 | -- | 10 | 8 | 6 | 4 |
| 7 | -- | -- | 4 | 1 | -2 |
| 8 | -- | -- | -- | -4 | -8 |
| 9 | -- | -- | -- | -- | -14 |

Thus exactly four candidate edges have nonpositive correction:
\[
\{7,10\},\quad \{8,9\},\quad \{8,10\},\quad \{9,10\}.
\tag{L10-31}
\]
Fix one such edge \(e=\{a,b\}\). The other five edges pair the residual
multiset \(N_e=M\setminus\{a,b\}\), with one copy of each endpoint removed.
The rearrangement bound therefore sharpens to
\[
s\ge ab+A(N_e).
\tag{L10-32}
\]
The four exact residual calculations are:

| Fixed edge \(e\) | \(A(N_e)\) | \(ab+A(N_e)\) | Anti-sorted residual signature |
|---|---:|---:|---|
| \(\{7,10\}\) | 253 | 323 | \((5,9),(5,10),(6,8),(6,9),(7,8)\) |
| \(\{8,9\}\) | 251 | 323 | \((5,10)^2,(6,8),(6,9),(7,7)\) |
| \(\{8,10\}\) | 246 | 326 | \((5,9),(5,10),(6,8),(6,9),(7,7)\) |
| \(\{9,10\}\) | 240 | 330 | \((5,9),(5,10),(6,8)^2,(7,7)\) |

The last two edges are impossible because their fixed-edge lower bounds
already exceed 323. For each of the first two, apply the exact least-entry
recurrence (L10-6)--(L10-7) to \(N_e\), with residual cutoff \(A(N_e)\).
At depths zero through five its surviving-state counts are, respectively,
\[
(1,2,1,2,1,1)
\qquad\hbox{and}\qquad
(1,1,1,2,1,1),
\tag{L10-33}
\]
and in each case the displayed anti-sorted residual signature is the unique
leaf. This is the same exhaustive pairing recurrence used for the 320--322
classification, now restricted by the candidate insertion edge; no cyclic-
order enumeration enters the argument.

Adding back \(\{8,9\}\) to its unique residual signature produces both the
loop \((7,7)\) and the repeated edge \((5,10)^2\), so it cannot be a simple
tail cycle. Adding back \(\{7,10\}\), on the other hand, gives the simple
cycle
\[
D_*=(10,5,9,6,8,7).
\tag{L10-34}
\]
Its six exact corrections are

| Edge \(\{a,b\}\) | \(\delta(a,b)\) |
|---|---:|
| \(\{5,10\}\) | 10 |
| \(\{5,9\}\) | 11 |
| \(\{6,9\}\) | 6 |
| \(\{6,8\}\) | 8 |
| \(\{7,8\}\) | 4 |
| \(\{7,10\}\) | -2 |

Thus its only admissible insertion gap is the already fixed edge
\(\{7,10\}\). Inserting label \(4\) there gives
\((10,5,9,6,8,7,4)\); reflecting while fixing label \(10\) gives the chosen
representative
\[
\omega_{323}=(10,4,7,8,6,9,5),
\qquad
(q,s)=(321,323).
\tag{L10-35}
\]

Conversely, the literal scores in (L10-30) and (L10-35) show that both
classes attain equality. Their tail scores differ, so the classes are
distinct. We have therefore proved the exact finite structural theorem
\[
\boxed{
\max\{P_\omega(T_7),P_\omega(T_6)\}=323
\quad\Longleftrightarrow\quad
\omega\sim_{\rm dihedral}(10,4,7,8,6,9,5)
\qquad\hbox{or}\qquad
\omega\sim_{\rm dihedral}(10,5,9,4,7,8,6).
}
\tag{L10-36}
\]
The theorem (L10-36) by itself classifies equality in the seven-label lemma
only. It places neither label \(2\) nor label \(3\), and it does not classify
the minimizing `n=10` core orders.

#### Exact label-three insertion gaps over the equality cycles

The next partial step can be classified without placing label \(2\). Set
\[
T_8=\{3,\ldots,10\},
\qquad
K_{\ge3}(\nu)
=\max_{\varnothing\ne U\subseteq T_8}P_\nu(U)
\tag{L10-37}
\]
for a cyclic order \(\nu\) on \(T_8\). This is deliberately distinct from
the full-core score \(K\), whose domain also contains label \(2\). If a later
full-core order \(\tau\) induces \(\nu\) after deleting label \(2\), then
\[
K(\tau)\ge K_{\ge3}(\nu).
\tag{L10-38}
\]
Thus a value above 323 is a definitive obstruction, whereas a value equal to
323 only leaves the gap available for a later label-two analysis.

Write
\[
\omega_A=(10,4,7,8,6,9,5),
\qquad
\omega_B=(10,5,9,4,7,8,6).
\tag{L10-39}
\]
Their complete seven-label sums are 321 and 323, respectively. For an edge
\(h=\{a,b\}\) of one of these displayed cycles, let \(\iota_h(\omega)\)
insert label \(3\) between its endpoints in the displayed orientation. The
full eight-label sum changes by the exact one-edge replacement
\[
\begin{aligned}
B_h
&=P_{\iota_h(\omega)}(T_8)
=P_\omega(T_7)+\Delta_3(a,b),\\
\Delta_3(a,b)
&=3(a+b)-ab
=9-(a-3)(b-3).
\end{aligned}
\tag{L10-40}
\]

It remains to control all proper induced subsets. Use the shortcut gain from
(L10-16), now computed in the inserted eight-cycle. For \(|U|\ge2\), the
same partition of the full cycle into selected gaps gives
\[
P_{\iota_h(\omega)}(U)-B_h
=\sum_{(i,j)\text{ a selected gap}}g_{\iota_h(\omega)}(i,j).
\tag{L10-41}
\]
There is a compact exact audit of every gain that can be nonnegative. For old
endpoints \(i,j\), splitting \(h\) changes the forward-arc sum only when that
arc contains \(h\), so
\[
g_{\iota_h(\omega)}(i,j)
=
\begin{cases}
g_\omega(i,j)-\Delta_3(a,b),&
   \text{if the forward arc from \(i\) to \(j\) contains \(h\)},\\
g_\omega(i,j),&\text{otherwise}.
\end{cases}
\tag{L10-42}
\]
The new shortcut that deletes only label \(3\) has gain
\(-\Delta_3(a,b)\). Every nontrivial shortcut having label \(3\) as an
endpoint is strictly negative: its arc contains a product \(3x\ge12\) and
an old--old product \(yz\ge20\), while its endpoint product is at most 30.

For \(\omega_A\), the edge products are
\[
40,28,56,48,54,45,50,
\tag{L10-43}
\]
and its one-internal-label shortcut gains, in the displayed starting-label
order, are
\[
2,-52,-62,-30,-69,-5,-70.
\tag{L10-44}
\]
The only two requiring separate attention are
\(g_A(10,7)=2\) on \(10\to4\to7\) and
\(g_A(9,10)=-5\) on \(9\to5\to10\). Every longer base arc uses at least
three edges and hence has gain at most
\[
90-(28+40+45)=-23.
\tag{L10-45}
\]
Since \(-\Delta_3(a,b)\le12\) in all 14 rows, (L10-42) keeps these longer
gains and every other one-internal gain strictly negative. The gain
\(g_A(10,7)\) becomes zero for \(h=\{4,10\}\), becomes \(-3\) for
\(h=\{4,7\}\), and otherwise remains 2. The gain \(g_A(9,10)\) becomes
\(-2\) for \(h=\{5,9\}\), becomes zero for \(h=\{5,10\}\), and
otherwise remains \(-5\).

For \(\omega_B\), the edge products and one-internal-label gains are
\[
50,45,36,28,56,48,60
\tag{L10-46}
\]
and
\[
-5,-61,-1,-52,-62,-28,-80.
\tag{L10-47}
\]
Here the only relevant gains are \(g_B(10,9)=-5\) on
\(10\to5\to9\) and \(g_B(9,7)=-1\) on \(9\to4\to7\). Every longer
base arc has gain at most
\[
90-(28+36+45)=-19,
\tag{L10-48}
\]
so it remains negative after (L10-42), as do the other one-internal gains.
The gain \(g_B(10,9)\) becomes zero only for \(h=\{5,10\}\); the gain
\(g_B(9,7)\) remains negative in every row.

The following tables are therefore complete shortcut-gain certificates.
In a bracket after a gain, the listed labels are exactly those skipped by
that shortcut. A dash means that there is no nontrivial gain of the indicated
sign. The argmax column records every maximizing label subset.

| Cycle | Gap \(h\) | \(\Delta_3\) | \(B_h\) | Positive nontrivial gains | Zero nontrivial gains | \(K_{\ge3}\) | Argmax subsets |
|---|---|---:|---:|---|---|---:|---|
| \(\omega_A\) | \(\{4,10\}\) | 2 | 323 | -- | \(10\to7:0\ [3,4]\) | 323 | \(T_6,T_8\) |
| \(\omega_A\) | \(\{4,7\}\) | 5 | 326 | -- | -- | 326 | \(T_8\) |
| \(\omega_A\) | \(\{7,8\}\) | -11 | 310 | \(10\to7:+2\ [4]\); \(7\to8:+11\ [3]\) | -- | 323 | \(T_6\) |
| \(\omega_A\) | \(\{6,8\}\) | -6 | 315 | \(10\to7:+2\ [4]\); \(8\to6:+6\ [3]\) | -- | 323 | \(T_6\) |
| \(\omega_A\) | \(\{6,9\}\) | -9 | 312 | \(10\to7:+2\ [4]\); \(6\to9:+9\ [3]\) | -- | 323 | \(T_6\) |
| \(\omega_A\) | \(\{5,9\}\) | -3 | 318 | \(10\to7:+2\ [4]\); \(9\to5:+3\ [3]\) | -- | 323 | \(T_6\) |
| \(\omega_A\) | \(\{5,10\}\) | -5 | 316 | \(10\to7:+2\ [4]\); \(5\to10:+5\ [3]\) | \(9\to10:0\ [5,3]\) | 323 | \(T_6\) |
| \(\omega_B\) | \(\{5,10\}\) | -5 | 318 | \(10\to5:+5\ [3]\) | \(10\to9:0\ [3,5]\) | 323 | \(T_7\) |
| \(\omega_B\) | \(\{5,9\}\) | -3 | 320 | \(5\to9:+3\ [3]\) | -- | 323 | \(T_7\) |
| \(\omega_B\) | \(\{4,9\}\) | 3 | 326 | -- | -- | 326 | \(T_8\) |
| \(\omega_B\) | \(\{4,7\}\) | 5 | 328 | -- | -- | 328 | \(T_8\) |
| \(\omega_B\) | \(\{7,8\}\) | -11 | 312 | \(7\to8:+11\ [3]\) | -- | 323 | \(T_7\) |
| \(\omega_B\) | \(\{6,8\}\) | -6 | 317 | \(8\to6:+6\ [3]\) | -- | 323 | \(T_7\) |
| \(\omega_B\) | \(\{6,10\}\) | -12 | 311 | \(6\to10:+12\ [3]\) | -- | 323 | \(T_7\) |

Indeed, (L10-41) bounds every score with at least two labels by \(B_h\) plus
the sum of all positive gains in its row. The displayed lower witnesses attain
that bound, and singletons score at most \(10^2=100\). The argmax list is
also exact. In the first row, either every selected gap is adjacent, giving
\(T_8\), or the sole zero shortcut is used, giving \(T_6\). In each of the
other admissible \(\omega_A\) rows, equality requires both positive shortcuts
and gives \(T_6\); in the \(\{5,10\}\) row its zero shortcut cannot coexist
with the positive \(5\to10\) shortcut because both enter label 10. In every
admissible \(\omega_B\) row, equality requires the shortcut deleting label
3 and gives \(T_7\); in its \(\{5,10\}\) row the zero and positive
shortcuts cannot coexist because both leave label 10. With no nontrivial
nonnegative gain, each excluded row is uniquely maximized by \(T_8\).

Consequently the exact partial classification is
\[
\boxed{
K_{\ge3}(\iota_h(\omega_A))
=
\begin{cases}
326,&h=\{4,7\},\\
323,&\text{for every other edge of \(\omega_A\)},
\end{cases}
}
\tag{L10-49}
\]
and
\[
\boxed{
K_{\ge3}(\iota_h(\omega_B))
=
\begin{cases}
326,&h=\{4,9\},\\
328,&h=\{4,7\},\\
323,&\text{for every other edge of \(\omega_B\)}.
\end{cases}
}
\tag{L10-50}
\]
Thus exactly \(\{4,7\}\) is excluded in the first equality cycle, while
exactly \(\{4,9\}\) and \(\{4,7\}\) are excluded in the second. This is
an **EXACT THEOREM (FINITE LABEL-THREE INSERTION-GAP CLASSIFICATION)**. It
makes no placement claim for label \(2\) and is not a classification or count
of the full `n=10` core minimizers.

#### Exact label-two insertion and complete core classification

The preceding result leaves six insertions in \(\omega_A\) and five in
\(\omega_B\). Denote them by \(A0,\ldots,A5,B0,\ldots,B4\) in the gap order
shown below, put
\[
T_9=\{2,\ldots,10\},
\qquad
M_3(\nu)=
\max_{\substack{\varnothing\ne V\subseteq T_8\\3\in V}}P_\nu(V),
\tag{L10-51}
\]
and retain the names \(T_6,T_7,T_8\) from (L10-1) and (L10-37). The complete
shortcut-gain certificates above give the following exact constrained
maxima:

| ID | Parent | Gap containing \(3\) | \(B_\nu=P_\nu(T_8)\) | \(M_3(\nu)\) | Constrained argmax |
|---|---|---|---:|---:|---|
| \(A0\) | \(\omega_A\) | \(\{4,10\}\) | 323 | 323 | \(T_8\) |
| \(A1\) | \(\omega_A\) | \(\{7,8\}\) | 310 | 312 | \(T_8\setminus\{4\}\) |
| \(A2\) | \(\omega_A\) | \(\{6,8\}\) | 315 | 317 | \(T_8\setminus\{4\}\) |
| \(A3\) | \(\omega_A\) | \(\{6,9\}\) | 312 | 314 | \(T_8\setminus\{4\}\) |
| \(A4\) | \(\omega_A\) | \(\{5,9\}\) | 318 | 320 | \(T_8\setminus\{4\}\) |
| \(A5\) | \(\omega_A\) | \(\{5,10\}\) | 316 | 318 | \(T_8\setminus\{4\}\) |
| \(B0\) | \(\omega_B\) | \(\{5,10\}\) | 318 | 318 | \(T_8\) |
| \(B1\) | \(\omega_B\) | \(\{5,9\}\) | 320 | 320 | \(T_8\) |
| \(B2\) | \(\omega_B\) | \(\{7,8\}\) | 312 | 312 | \(T_8\) |
| \(B3\) | \(\omega_B\) | \(\{6,8\}\) | 317 | 317 | \(T_8\) |
| \(B4\) | \(\omega_B\) | \(\{6,10\}\) | 311 | 311 | \(T_8\) |

Here is the pruning argument behind the table, using no subset sweep. In rows
\(A1,\ldots,A5\), the only positive shortcut compatible with retaining label
\(3\) is \(10\to7\), of gain \(2\), which deletes label \(4\). Every other
positive shortcut in those rows deletes label \(3\), as does the zero
shortcut in \(A5\). Thus the exact constrained maximum is \(B_\nu+2\),
attained uniquely on \(T_8\setminus\{4\}\). In every \(B\)-row, each
nontrivial nonnegative shortcut deletes label \(3\), so retaining \(3\)
leaves the full set \(T_8\) as the unique constrained maximizer. In row
\(A0\), \(T_8\) has score 323. Its zero shortcut \(10\to7\) deletes labels
\(3,4\), while \(g(10,4)=-2\) deletes label \(3\); every other nontrivial
gain is at most \(-5\). The compatible shortcut \(9\to10\), which deletes
label \(5\), has gain \(-5\). The complete gain audit in
(L10-42)--(L10-48) therefore gives the sharper fact
\[
\max_{\substack{3\in V\subsetneq T_8}}P_{A0}(V)=318.
\tag{L10-52}
\]

Now insert label \(2\) into one of the eight labelled gaps of a surviving
cycle \(\nu\), obtaining a core order \(\tau\). Let \(U\subseteq T_9\)
contain \(2\), and put \(V=U\setminus\{2\}\). If \(|V|\ge2\), let \(a,b\)
be the two distinct neighbors of \(2\) in the order induced on \(U\).
Deleting \(2\) gives the exact variation
\[
P_\tau(U)-P_\nu(V)
=2(a+b)-ab
=4-(a-2)(b-2)
\le2.
\tag{L10-53}
\]
If \(3\notin V\), then \(a,b\ge4\), so the variation is at most \(-2\) and
\(P_\tau(U)\le321\). The cases \(|V|\le1\) have score at most
\(2\cdot2\cdot10=40\). If \(3\in V\) and \(\nu\ne A0\), the table gives
\[
P_\tau(U)\le M_3(\nu)+2\le322.
\tag{L10-54}
\]

It remains only to inspect \(A0=(10,3,4,7,8,6,9,5)\). Every proper
\(V\) containing \(3\) gives at most \(318+2=320\). For \(V=T_8\), the
neighbors \(a,b\) are the endpoints of the actual insertion gap of label
\(2\), and (L10-53) gives:

| Gap containing \(2\) | \(\{3,10\}\) | \(\{3,4\}\) | \(\{4,7\}\) | \(\{7,8\}\) | \(\{6,8\}\) | \(\{6,9\}\) | \(\{5,9\}\) | \(\{5,10\}\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Variation | -4 | 2 | -6 | -26 | -20 | -24 | -17 | -20 |

Consequently the sole insertion above 323 among the 88 candidates is
\[
\tau_{\rm exc}=(10,3,2,4,7,8,6,9,5),
\qquad
K(\tau_{\rm exc})=P_{\tau_{\rm exc}}(T_9)=325.
\tag{L10-55}
\]
Its full sum is
\[
30+6+8+28+56+48+54+45+50=325.
\]
Equality at 325 requires both \(V=T_8\) and the \(\{3,4\}\) variation, so
\(T_9\) is its unique maximizing subset. For every other insertion, all
subsets containing label \(2\) score strictly below 323. The score is
therefore 323 and the complete argmax list is inherited unchanged from its
partial parent:

| Core family | Number of classes | Exact argmax subsets |
|---|---:|---|
| \(A0\), gap of \(2\ne\{3,4\}\) | 7 | \(T_6,T_8\) |
| \(A1,\ldots,A5\), every gap of \(2\) | 40 | \(T_6\) only |
| \(B0,\ldots,B4\), every gap of \(2\) | 40 | \(T_7\) only |
| Exceptional \(A0,\{3,4\}\) insertion | 1 | \(T_9\) only |

It remains to prove completeness and count dihedral classes, rather than
counting displayed rows. The eleven partial parents are pairwise
dihedrally inequivalent. Deleting label \(3\) from a hypothetical equivalence
would either identify \(\omega_A\) with \(\omega_B\), impossible because
their induced \(T_6\) scores are respectively 323 and 322, or give a
label-preserving dihedral automorphism of one seven-cycle carrying one gap
to another. All seven labels are distinct, so that automorphism is the
identity and the gaps coincide.

The same deletion argument for label \(2\) proves that the \(11\cdot8=88\)
insertions are 88 distinct dihedral core classes. Conversely, if a core
order has \(K=323\), equality is forced in the seven-label lemma (L10-12);
(L10-36) then forces \(\omega_A\) or \(\omega_B\), and
(L10-49)--(L10-50) force one of the eleven partial parents. The label-two
classification above excludes exactly \(\tau_{\rm exc}\). Hence
\[
\boxed{
K(\tau)=323
\quad\Longleftrightarrow\quad
\tau\text{ belongs to one of exactly 87 dihedral core classes.}
}
\tag{L10-56}
\]

Only now may the complete-order count be derived. Exact index-one elimination
(CR12p)--(CR12q) preserves the score, introduces no maximizing subset
containing label \(1\), and is surjective from complete orders to core
orders. Each nine-label core has nine labelled insertion gaps. As above, a
dihedral equivalence between two insertions restricts after deleting \(1\)
to a label-preserving automorphism of the core, which is trivial; deleting
\(1\) also prevents different core classes from merging. Therefore
\[
\boxed{
\#\{\text{complete dihedral minimizer classes at }n=10\}
=87\cdot9
=783.
}
\tag{L10-57}
\]
Among these complete classes, 63 retain argmaxes \(T_6,T_8\), 360 have sole
argmax \(T_6\), and 360 have sole argmax \(T_7\). This is an **EXACT THEOREM
(FINITE \(n=10\) CORE AND COMPLETE MINIMIZER CLASSIFICATION)**. It is not a
classification of geometric minimizers or an exact evaluation of
\(R_2^*(10)\). The exceptional class is unique only among the 88 candidates
forced by the preceding equality classifications; many unrelated core
orders can of course have score above 323.

#### Independent finite oracles for \(n=10\)

The independent test-only lemma oracle fixes label \(10\) to remove
rotations, directly permutes labels \(4,\ldots,9\), and retains the
orientation whose second label is smaller than its last. It therefore checks
exactly \(6!/2=360\) dihedral classes. Literal cyclic sums give minimum 323
and exactly two equality rows:

| Canonical test-local order | \(P(T_7)\) | \(P(T_6)\) |
|---|---:|---:|
| `(10,4,7,8,6,9,5)` | 321 | 323 |
| `(10,5,9,4,7,8,6)` | 323 | 322 |

This exhaustive **computational** equality list agrees with the structural
theorem (L10-36). It remains an independent test-only oracle and is not the
source of that theorem.

The same test independently enumerates duplicated-label pairing signatures
through 322, recovers exactly the eight rows above, recognizes only the
displayed 322 signature as a simple spanning cycle, and checks the exact
correction and fixed-edge pairing data used in both equality branches.

A separate structural regression constructs all seven label-three insertions
in each equality cycle and directly audits all 48 nontrivial oriented
shortcuts of each inserted order. It reproduces the complete nonnegative-gain
columns in the table above and the exact bound obtained from (L10-41). This
checks the certificate data but is not the source of (L10-49)--(L10-50).

An independent literal subset oracle then treats the two equality cycles as
fixed test-local tuples, splices label \(3\) into each of their seven labelled
gaps, and scores all \(2^8-1=255\) nonempty induced subsets of every resulting
order. It performs exactly
\[
14\cdot255=3{,}570
\tag{L10-58}
\]
integer subset evaluations, without using the insertion formula, shortcut
gains, a repository canonicalizer, the public enumerator, or the production
scorer. It independently returns the score rows
\[
\begin{aligned}
\omega_A:&\quad(323,326,323,323,323,323,323),\\
\omega_B:&\quad(323,323,326,328,323,323,323),
\end{aligned}
\tag{L10-59}
\]
in the gap order of the certificate table. It also recovers every displayed
argmax: \(T_6,T_8\) in the first \(\omega_A\) row; only \(T_8\) in each
excluded row; only \(T_6\) in the other five admissible \(\omega_A\) rows;
and only \(T_7\) in all five admissible \(\omega_B\) rows.

A further independent literal oracle constructs the eleven surviving
label-three cycles directly from the two fixed parent tuples, inserts label
\(2\) in every one of their eight labelled gaps, and scores all 511 nonempty
subsets of every resulting core. It performs
\[
88\cdot511=44{,}968
\tag{L10-60}
\]
exact integer subset evaluations. It finds 87 rows of score 323 and the sole
score-325 row \((10,3,2,4,7,8,6,9,5)\), and it recovers every argmax in the
four-row family table above. A test-local dihedral key roots each labelled
cycle at its unique largest label and compares the two orientations directly;
it obtains 88 distinct core keys without calling a repository canonicalizer.
After the mathematical classification has selected the 87 minimizing cores,
the same local key checks all nine label-one insertions of each and obtains
783 distinct complete classes. This finite oracle audits (L10-56)--(L10-57);
it is not their source.

A separate literal computation scores all \(2^9-1=511\) nonempty subsets
of \(\tau_*\). It records every maximizing subset and supplies the following
per-cardinality audit; each row has a unique maximizer.

| \(|U|\) | Maximum | Unique maximizing subset |
|---:|---:|---|
| 1 | 100 | \(\{10\}\) |
| 2 | 180 | \(\{9,10\}\) |
| 3 | 242 | \(\{8,9,10\}\) |
| 4 | 288 | \(\{7,8,9,10\}\) |
| 5 | 318 | \(\{6,7,8,9,10\}\) |
| 6 | 323 | \(\{5,6,7,8,9,10\}\) |
| 7 | 321 | \(\{4,5,6,7,8,9,10\}\) |
| 8 | 323 | \(\{3,4,5,6,7,8,9,10\}\) |
| 9 | 319 | \(\{2,3,4,5,6,7,8,9,10\}\) |

These are **VERIFIED FACTS (FINITE EXHAUSTIVE EXACT COMPUTATION)** and audit
the proof without supplying it. The helpers call no repository canonicalizer,
public enumerator, or production Karp scorer. Production source is unchanged,
and the public complete-order enumeration domain remains `n<=8`.

## 7. Comparison With \(W\)

The native definitions of the two symbols describe different combinatorial
relaxations.

- \(\Lambda(\sigma)\) uses a **complete** order of
  \(\{1,\ldots,n\}\), sums products around directed STN cycles, and divides
  by the number of `wrap_upper` occurrences. It represents variable angular
  spacings through the difference-constraint cycle criterion.
- The repository's \(W(\tau)\) uses a **core** order of
  \(\{2,\ldots,n\}\), maximizes one pair ratio
  \(ij/d_\tau(i,j)\), and controls a construction on equally spaced regular
  directions.

Exact label-one elimination bridges the order domains through the core
objective \(K\), but it does not identify \(K\) with the scalar pair objective
\(W\). In particular, the last two columns of the bounded table compare
separate exact objectives; they do not establish
\(\Lambda_n=(n-1)W_n\) or equality of minimizing order sets.

There is one useful exact comparison after first putting both quantities on
the **same** order. Let
\(\tau=(a_0,\ldots,a_{m-1})\) be a cyclic order of \(m\ge2\) distinct
positive labels. Extend the purely combinatorial definitions (CR5)--(CR11) to
these labels by using \(s(u,v)=a_u a_v\), and call the resulting maximum
\(\Lambda_{\rm same}(\tau)\). For positions \(u\ne v\), put
\[
d_\tau(u,v)=\min(|u-v|,m-|u-v|)
\tag{CR34a}
\]
and define
\[
W_{\rm same}(\tau)=\max_{0\le u<v<m}{a_u a_v\over d_\tau(u,v)}.
\tag{CR35}
\]
For an edge \(u\to v\), its smaller circular distance satisfies
\[
d_\tau(u,v)
\le
\begin{cases}
m-(v-u),&u<v,\\
u-v,&u>v.
\end{cases}
\tag{CR36}
\]
On a closed walk, the total positive position increase equals the total
absolute negative decrease. Summing (CR36) therefore gives
\[
\sum_{e\in C}d_\tau(e)\le m q(C).
\tag{CR37}
\]
Since each edge product is at most
\(W_{\rm same}(\tau)d_\tau(e)\),
\[
\boxed{
\Lambda_{\rm same}(\tau)\le mW_{\rm same}(\tau).
}
\tag{CR38}
\]
This need not be equality: on the core order \(\tau=(4,2,3)\),
\(\Lambda_{\rm same}(\tau)=26\), while \(3W(\tau)=36\).

For a Power-Ringmin core order, singleton scores do not attain \(K\), because
the pair \(\{n-1,n\}\) has score \(2n(n-1)>n^2\). Every relevant subset in
the definition of \(K(\tau)\) is therefore a one-wrap cycle admitted by
\(\Lambda_{\rm same}(\tau)\). Applying (CR38) with \(m=n-1\) gives the
pointwise comparison
\[
\boxed{
K(\tau)
\le\Lambda_{\rm same}(\tau)
\le(n-1)W(\tau).
}
\tag{CR38a}
\]
Using the exact reduction (CR28a) and choosing an order minimizing \(W\),
\[
\boxed{
\Lambda_n\le(n-1)W_n.
}
\tag{CR38b}
\]
The inequality is intentionally non-strict; equality holds at \(n=3\).
Combining it with (CR27) yields the geometric upper bound
\[
\boxed{
R_2^*(n)
< {\Lambda_n\over\pi}
\le {(n-1)W_n\over\pi}
\qquad(n\ge3).
}
\tag{CR38c}
\]
Unlike the regular-direction construction followed by radius-one insertion,
this deduction is valid for every \(n\ge3\) and uses neither construction.
It is an upper bound, not an exact geometric optimum or a certificate claim.
Since the separately proved product-distance theorem gives
\(W_n/n^2\to8/25\), it also recovers
\[
\limsup_{n\to\infty}{\Lambda_n\over n^3}\le{8\over25},
\qquad
\limsup_{n\to\infty}{R_2^*(n)\over n^3}\le{8\over25\pi}.
\tag{CR38d}
\]

Deleting label \(1\) makes the full \(\Lambda\) score a function of the
entire induced core order through \(K\), but not a function of the single
number \(W(\tau)\). Exact finite examples at \(n=6\) are:

- `(6,1,2,4,5,3)` and `(6,3,5,2,1,4)` both have \(\Lambda=77\), while
  their induced-core \(W\) scores are respectively \(20\) and \(24\);
- `(6,1,2,4,5,3)` and `(6,2,5,4,1,3)` both induce \(W=20\), while their
  full scores are respectively \(77\) and \(80\).

These examples disprove identification of \(K\) with \(W\); they are
consistent with the global one-sided comparison (CR38b).

## 8. Asymptotic Consequences And Non-Consequences

Dividing (CR28) by \(\pi n^3\) gives the exact vanishing-error comparison
\[
0
<
{\Lambda_n\over\pi n^3}
-{R_2^*(n)\over n^3}
<
{1\over n}.
\tag{CR39}
\]
Consequently, normalized liminf, limsup, and all subsequential limits agree
after the factor \(\pi\). Combining this relation with the already-proved
geometric bounds gives
\[
\Lambda_n=\pi R_2^*(n)+O(n^2),
\qquad
\Lambda_n=\Theta(n^3),
\tag{CR40}
\]
\[
{\Lambda_n\over\pi R_2^*(n)}\longrightarrow1,
\tag{CR41}
\]
and
\[
C_{5,\mathrm{rat}}
\le
\liminf_{n\to\infty}{\Lambda_n\over n^3}
\le
\limsup_{n\to\infty}{\Lambda_n\over n^3}
\le
{8\over25}.
\tag{CR42}
\]

None of these statements proves that either normalized sequence converges, or
identifies an exact leading constant. In particular, the bounded values in
(CR34) do not give a closed-form evaluation of (CR28a); \(8/25\) remains an
upper coefficient, not an exact constant.

Further non-consequences are important.

- The two-nested-tail obstruction (CR28g) may improve finite lower terms, but
  (CR28n) proves only that this specific proof schema has the same leading
  coefficient as the one-tail pairing bound. It neither evaluates
  \(\Lambda_n\) asymptotically nor excludes methods coupling many tails.
- The three-nested-tail obstruction (CR28u) has the complete compatible-split
  reduction (CR28w)--(CR28y). Its uniform squeeze (CR28z)--(CR28aa) and
  optimized result (CR28ad) again preserve the one-tail cubic coefficient.
  This is a method-specific limitation for one block of three tails, not an
  asymptotic evaluation of \(\Lambda_n\) or \(R_2^*(n)\). By itself it does
  not settle growing blocks; the following general result settles every
  sublinear length, and the later special result treats one linear sequence.
- The arbitrary-block reduction (CR28al) retains every compatible recursive
  split and every signed correction prefix. Its uniform squeeze
  (CR28an)--(CR28ao) proves that all fixed blocks and, more generally, every
  sublinear length \(r=o(n)\) preserve the one-tail coefficient for this
  separately optimized obstruction. The first scale not excluded is linear
  \(r=\Theta(n)\); neither the error estimate nor the admissible-domino audit
  alone proves improvement there.
- For the jointly optimized one-prefix linear block
  \(m=1\), \(r_n=\lfloor(1-\sqrt3/3)n\rfloor\), the independent
  slack/prefix argument (CR28ax)--(CR28bl) proves a positive cubic certified
  residual over \(P^*_{r_n,n}\). The complete three-parameter optimization
  proves that \((4+2\sqrt3)/27\) is the largest *total* pairing-plus-residual
  coefficient certified by the one-prefix specialization. Combined directly
  with (CR28ap)
  and (CR28bg), without a max--min exchange, it yields the global lower
  bounds (CR28bo)--(CR28bq). It gives neither the exact residual coefficient
  nor the exact asymptotic leading coefficient, and it does not prove
  convergence.
- The two-prefix extension (CR28br)--(CR28cc) combines the selected heights
  before drawing from the unique base-slack pool. It therefore charges each
  original edge at most once and covers every recursive child edge. The exact
  ordered-weight reduction, six-branch density classification, compact-face
  audit, and cubic relaxation prove the unique optimizer (CR28bw13) and the
  coefficient \(C_{2,*}\) in (CR28bw14). The older rational witness retains
  the explicit \(n\ge59\) two-prefix theorem; finite rounding of the
  irrational two-prefix optimizer remains open. Neither number is an exact
  residual, limit, or geometric leading constant.
- The three-prefix extension (CR28cd)--(CR28cq15) combines all three heights
  before charging and retains the same one-use base-slack partition through
  every nested child edge. The clipped individual weights are automatically
  ordered. The exact compact-simplex factorization proves the predicted
  normalized point uniquely, and the complete closure audit gives
  \[
  C_{3,*}
  ={753972193324+106042322\sqrt{377823}\over2960667770787}
  >C_{2,*}.
  \]
  The finite clipped specialization (CR28cq1)--(CR28cq15) has minimal uniform
  threshold \(159\), gives the literal expression \(\mathcal B_{3,n}\) and
  its stronger integer closure \(\mathcal I_{3,n}\), controls the polynomial
  remainder, and proves
  \(\Lambda_n>C_{3,*}n^3\) throughout that domain. It makes no exact
  residual, convergence, production, or geometric-leading-constant claim.
- The four-prefix extension (CR28de)--(CR28dq13) combines the four heights
  before any slack assignment. The five convex coefficients telescope to
  four disjoint weighted segments, the literal history canonically partitions
  every original edge into one charged or one unused edge, and the recursive
  invariant survives all three boundaries at arbitrary depth. This proves the
  exact finite bound (CR28dh). The subsequent compact optimization reduces
  the four ordered weights exactly, classifies all fifteen clipping regimes,
  their three winning transitions, every density collision and every compact
  facet, and proves the unique strict `MMMM` optimum
  \[
  C_{4,*}
  ={597580022071777213687318156
   +21288970076515705538\sqrt{2903456040383}
   \over2290468477489828247376833403}
  >C_{3,*}.
  \]
  It yields the asymptotic lower bounds (CR28dq13), but no finite rounding,
  exact residual, convergence theorem, or geometric leading constant.
- The arbitrary finite-prefix extension (CR28dr)--(CR28dw) fixes any
  \(k\ge1\), combines \(0,H_1,\ldots,H_k\) before charging, and telescopes
  its \(k+1\) convex coefficients to \(k\) disjoint segments. Its canonical
  original-edge partition uses each slack once or leaves it unused. The
  descending recursive invariant contains no frontier count and therefore
  survives every finite number of boundaries and every nested history. This
  proves the exact finite indexed inequality by itself. It gives no uniform
  growing-\(k\) control, coefficient optimization, rounding, limiting-prefix
  passage, asymptotic coefficient, or geometric claim.
- The normalized simplex theorem (CR28cr)--(CR28dd) solves the compact
  polynomial for every fixed \(k\), proves its unique interior maximizer and
  the exact recurrence \(M_k\nearrow1/3\), and generates the first five
  rational simplex points used here. It does not imply the separate direct finite-\(k\)
  charging theorem or make that theorem uniform in growing \(k\). In
  particular, neither the formal endpoint value \(1/3\) nor the all-middle
  value \((434+4\sqrt2)/1587\) is a new coefficient bound for \(\Lambda_n\)
  or \(R_2^*(n)\).
- Combining those two separate theorems only at fixed \(k=5\), with
  \(\alpha=13/30\), gives the explicit rational all-middle point
  (CR28dx)--(CR28dz), the exact coefficient
  \[
  C_{5,\mathrm{rat}}
  ={2263404122555368590593580404287
   \over8177706222298165502582585481000},
  \]
  and the exact comparison and liminf bounds (CR28dz2)--(CR28dz3). This
  fixed-parameter consequence is not a global five-prefix optimization.
  The exact finite specialization (CR28dz4)--(CR28dz19) retains all four
  parameter families unchanged. Its minimal uniform threshold is \(234\),
  its literal and integer-closed bounds are \(\mathcal B_{5,n}\) and
  \(\mathcal I_{5,n}\), and its exact rounded remainder proves
  \(\Lambda_n>C_{5,\mathrm{rat}}n^3\) throughout the domain. This supplies
  no growing-\(k\) passage, true residual, convergence theorem, or geometric
  leading constant.
- The theorem does not assert \(\rho_\sigma=\Lambda(\sigma)/\pi\), equality
  of minimizing order sets, or \(\Lambda_n=(n-1)W_n\). The exact global
  relation proved here is the one-sided inequality (CR38b).
- Insertion-gap independence applies to \(\Lambda(\sigma)\), not to the exact
  angular threshold \(\rho_\sigma\) or to fixed-order feasible-radius sets.
- One-wrap saturation concerns the separable product weights
  \(\sigma_u\sigma_v\). It does not show that checking only one-wrap cycles
  suffices for the exact angular STN weights
  \(2\pi\varepsilon(u,v)-\theta_R(\sigma_u^2,\sigma_v^2)\), or that an exact
  angular critical/negative cycle must have one wrap.
- A cycle attaining \(\Lambda(\sigma)\) is a witness for the product-angle
  comparison, not necessarily a critical or negative exact-STN cycle at
  \(\rho_\sigma\). For \(n=3\), the two-cycle on labels \(2,3\) attains
  \(\Lambda=12\), but its exact weight
  \(2\pi-2\theta_R(4,9)\) is positive for every \(R>0\).
- The exact real-arithmetic theorem supplies no new interval-backend audit,
  certificate, exact geometric finite optimum value, or checked-artifact
  conclusion.

# Fixed-Order Maximum Cyclic Ratio

Date: 2026-07-14

Last updated: 2026-07-20

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
- **EXACT THEOREM (CANONICAL EIGHT-TWENTY-FIFTHS CORE):** for every public
  construction row \(n\ge9\), Section 8 gives the unique maximizing subset
  and exact value of \(K(\tau_n)\): (K825-2)--(K825-4) cover the symbolic
  rows and the fourteen-row table covers the explicit initial orders. On
  symbolic rows the maximizer is the tail from \(2v+1\), with \(2v+2\)
  additionally deleted exactly for \(e=6,7,8\), and
  \[
  K(\tau_n)={143\over500}n^3+O(n^2).
  \]
  Hence the current upper coefficients are \(143/500\) for \(\Lambda_n\)
  and \(143/(500\pi)\) geometrically. This is an upper construction, not a
  global minimizing-order or convergence theorem.
- **EXACT THEOREM (EXACT-THRESHOLD RESIDUE-ONE CORE):** for
  \(n=5k+1\), \(k\ge2\), Section 9 proves that the order returned by
  `residue_one_product_distance_order(n)` has the unique maximizing subset
  \(\{2k+1,\ldots,n\}\) and an exact parity quasipolynomial with leading
  coefficient \(857/3000\). It is strictly smaller than the canonical
  K825 value on every row in this residue class. The improvement gives a
  sharper residue-one subsequential upper coefficient, not a new all-residue
  limsup theorem.
- **EXACT THEOREM (EXACT-THRESHOLD RESIDUE-TWO CORE):** for
  \(n=5k+2\), \(k\ge2\), Section 10 proves that the order returned by
  `residue_two_product_distance_order(n)` also has the unique maximizing
  subset \(\{2k+1,\ldots,n\}\). Its exact period-two formula is strictly
  smaller than K825 on every row, with no crossover, but the two families
  have the same cubic coefficient \(143/500\); their difference is only
  \(21n^2/100+O(n)\).
- **EXACT THEOREM (CLOSING PG46 CORE):** on \(n=10m+3\), \(m\ge3\),
  Section 11 proves that the PG46 order placing \(P_m\) in \(G_{2m-1}\)
  has the sole maximizing subset \(\{4m+1,\ldots,n\}\) and
  \[
  K={572m^3+631m^2+223m+22\over2}.
  \]
  Its exact K825 difference is \(m^2-6m-4\): it improves K825 exactly for
  \(m=3,4,5,6\), is worse for \(m\ge7\), and never ties. It retains cubic
  coefficient \(143/500\), so it gives no coefficient improvement. This is
  a construction-specific core-order theorem, not a geometric or global
  optimality result.
- **EXACT THEOREM (PRECLOSING PG46 CORE):** on the same rows, Section 12
  proves that the other sharp PG46 order, placing \(P_m\) in
  \(G_{2m-2}\), has the same sole maximizing tail and
  \[
  K={572m^3+631m^2+235m+22\over2}.
  \]
  It exceeds the closing value by \(6m\) and K825 by \(m^2-4\), so it is
  strictly worse than both on every admitted row. It retains coefficient
  \(143/500\) and has no geometric or global-optimality consequence.
- **EXACT THEOREM (DESCENDING-MIN PG49 CORE):** on \(n=10m+3\),
  \(m\ge3\), Section 13 evaluates the deterministic Ferrers representative
  (PG104) by the exact floor/positive-part formula (KPGMIN-9). Its maximizing
  subsets are precisely
  \(B_m\cup\mathcal P_m\cup Z'\), \(Z'\subseteq\mathcal Z_m\), so their
  number is \(2^{|\mathcal Z_m|}\). The zero set is genuinely nonempty on
  at least one explicit, very large row; universal uniqueness is false. The
  value is smaller than K825 and preclosing PG46 only at \(m=4\), is never
  smaller than closing PG46, and has cubic coefficient
  \(0.2881683105370884612\ldots>143/500\). Its exact formula is neither
  polynomial nor eventual quasipolynomial. These are core-order statements,
  with no geometric or global-optimality consequence.
- **EXACT THEOREM (EXPLICIT PG49-STAR CORE):** on \(n=10m+3\),
  \(m\ge3\), Section 15 evaluates the piecewise Ferrers bijection (PG110).
  Its sole maximizing subset is \(B_m=\{4m+1,\ldots,n\}\), and
  \[
  K={1714m^3+1863m^2+24mq+617m+12q^2+48q+66\over6},
  \qquad q=\left\lfloor{4m+3\over5}\right\rfloor.
  \]
  The five \(m\bmod5\) branches have cubic coefficient \(857/3000\) in
  \(n\). This value is strictly below K825 and both PG46 values for every
  \(m\ge3\). The theorem concerns one explicit fixed core-order family and
  has no geometric or global-optimality consequence.
- **EXACT THEOREM (ODD-\(v\) PG49-STAR PARITY CORE):** on
  \(n=10m+8\), \(m\ge1\), Section 17 evaluates the core order fixed earlier
  by (PGODD-6), without changing the candidate. Its sole maximizing subset
  is \(B_m=\{4m+3,\ldots,10m+8\}\), and, with
  \(q=\lfloor(4m+5)/5\rfloor\),
  \[
  K={1714m^3+4467m^2+24mq+3749m+12q^2+60q+1032\over6}.
  \]
  The five \(m\bmod5\) branches have coefficient \(857/3000\) in \(n\)
  and are strictly below canonical K825 on every row. There is no argmax or
  formula exception at \(m=1,2\); only the unique minimum compressed
  shortcut changes from the stable triple connector to the retained cyclic
  closing label. No geometric or global-optimality consequence follows.
- **EXACT THEOREM (EVEN-\(v\) RESIDUE-TWO PG49-STAR CORE):** on
  \(n=10m+2\), \(m\ge1\), Section 18 evaluates the unchanged core fixed by
  (PGE2-6). Its sole maximizing subset is
  \(B_m=\{4m+1,\ldots,10m+2\}\), and
  \[
  K={1714m^3+1353m^2+24mq+281m+12q^2+36q+30\over6},
  \qquad
  q=\left\lceil{(m-1)(4m+1)\over5m+1}\right\rceil.
  \]
  The five regular residue branches have coefficient \(857/3000\) in
  \(n\), with \(m=1\) the sole residual of that branch expansion and the
  all-row formula still exact. The fixed
  core is strictly below both the known residue-two order and canonical K825
  on every same-subsequence row. The only shortcut-minimum transition is from
  the retained cyclic closing label at \(m=1,2,3\) to the triple connector
  at \(m\ge4\). No angular, geometric, global-minimizer, or global-optimality
  consequence follows.
- **EXACT THEOREM (ODD-\(v\) RESIDUE-TWO PG49-STAR CORE):** on
  \(n=10m+7\), \(m\ge1\), Section 19 evaluates the unchanged core fixed by
  (PGE2ODD-6). Its sole maximizing subset is
  \(B_m=\{4m+3,\ldots,10m+7\}\), and
  \[
  K={1714m^3+3891m^2+24mq+2921m+12q^2+48q+732\over6},
  \qquad q=\left\lfloor{4m+3\over5}\right\rfloor.
  \]
  All five residue branches, including \(m=1,2,3\), are regular and have
  coefficient \(857/3000\) in \(n\); there is no residual correction. The
  fixed core is strictly below both the known residue-two order and canonical
  K825 on every same-subsequence row. The shifted-triple interval is empty
  exactly at \(m=1,2,3\), the scaffold has no doubleton, and the shortcut
  minimum lies on the retained cyclic closing label only at \(m=1,2\), then
  on \(c_0\). No construction, production, angular, geometric,
  global-minimizer, or global-optimality conclusion follows.
- **EXACT THEOREM (MONOTONE THRESHOLD-CLOSING PG46 CORE):** on the same
  rows, Section 16 evaluates the interval shift \(\alpha_{q,2m-1}\), where
  \(q=\lfloor(4m+3)/5\rfloor\), that keeps every residual path increasing.
  Its sole maximizing subset is again \(B_m=\{4m+1,\ldots,n\}\), and
  \[
  K={572m^3+619m^2+8mq+207m+4q^2+16q+22\over2}.
  \]
  It is strictly below K825 and preclosing PG46 on every row, below closing
  PG46 except for equality at \(m=3\), and strictly above PG49-star. The
  exact difference from PG49-star is \(m(m-1)(m-2)/3\), proving that the
  reversed singleton block supplies the entire cubic coefficient reduction
  from \(143/500\) to \(857/3000\). No angular, geometric, or global
  minimizing-order conclusion follows.
- **EXACT THEOREM (FIXED PGE5 INTERVAL-SHIFT CORE):** on the distinct
  \(e=5\), \(n=10m+4\), \(m\ge2\) scaffold, Section 20 evaluates only
  \(\alpha_{q,2m-1}\), where \(q=\lfloor(4m+3)/5\rfloor\). Its sole
  maximizing subset is \(\{4m+1,\ldots,10m+4\}\), and
  \[
  K={572m^3+809m^2+8mq+329m+4q^2+20q+36\over2}.
  \]
  All five residue branches are regular, including \(m=2\). The fixed
  shift is strictly below canonical K825 on every same-subsequence row by
  \(13n^2/2500+O(n)\), while both retain cubic coefficient \(143/500\).
  The only boundary change is the minimum compressed-shortcut role at
  \(m=2\); there is no argmax or score exception. This fixed-core theorem
  has no angular, geometric, global-minimizer, or global-optimality
  consequence.
- **EXACT THEOREM (PGE5 SINGLETON-REVERSAL CORE):** on that same scaffold,
  Section 21 keeps the interval shift through the doubleton, reverses the
  entire singleton block, and puts \(P_q\) in the closing gap. The map is a
  supported bijection with \(W=W_n\), its sole induced-\(K\) maximizer is
  \(B_m=\{4m+1,\ldots,10m+4\}\), and
  \[
  K_*={1714m^3+2439m^2+24mq+965m+12q^2+60q+120\over6}.
  \]
  Every deletion gain and compressed shortcut is strict. The exact identity
  \(K_\uparrow-K_*=(m-1)(m-2)(m-3)/3\) proves the fixed-subsequence
  coefficient \(857/3000\). Canonical K825 is strictly larger on every
  row. These are one-map combinatorial statements with no production,
  permanent, angular, geometric, global-minimizer, or global-optimality
  consequence.
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
  By itself this pointwise finite theorem gives no uniform asymptotic control
  for \(k=k(n)\). It can, however, be combined separately with the normalized
  optimizer at each fixed finite \(k\), as in the all-fixed-\(k\) corollary
  below.
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
  stationarity. The cases \(k=1,2,3,4,5\) recover exactly the optimized
  one- through five-prefix simplex data.
- **EXACT NORMALIZED-ENVELOPE CLASSIFICATION:** the formal limiting envelope
  \(p(\alpha)+(3\alpha-1)^3/24\) has unique compact-closure maximum
  \(1/3\) at the degenerate endpoint \(\alpha=1\); on \(\alpha<1\) this is
  only a supremum. Restricted to the limiting all-middle closure
  \([1/3,1/2]\), its unique maximum is
  \((434+4\sqrt2)/1587\) at
  \((13-2\sqrt2)/23\).
- **EXACT GLOBAL CLIPPED FINITE-PREFIX CLASSIFICATION:** for arbitrary
  \(k\), coordinatewise weight clipping gives (CR28dw14), with
  \((k+1)(k+2)/2\) regimes \(H^hM^m0^z\), and the exact compact Bellman
  envelope is (CR28dw16)--(CR28dw17). Its normalized summands are lower
  Darboux sums for the increasing clipped floor \(\phi\). Their uniform
  finite-prefix supremum is the explicit three-piece polynomial
  (CR28dw20), whose unique global maximum is
  \[
  C_{\mathrm{AF}}={434+4\sqrt2\over1587}
  \]
  at \((13-2\sqrt2)/23\). For every finite \(k\), the complete compact
  template has one strict all-middle maximizer (CR28dw24)--(CR28dw25);
  its value \(C_{k,*}\) increases strictly to \(C_{\mathrm{AF}}\). Thus no
  high-clipped counterexample exists, and the supremum is not attained at
  finite \(k\).
- **EXACT METHOD-SPECIFIC ASYMPTOTIC COROLLARY (ALL FIXED \(k\)):** put
  \[
  \alpha_\infty={13-2\sqrt2\over23}.
  \]
  For every fixed finite \(k\), use the unique normalized maximizer
  \(x^{(k)}\) and define
  \[
  \beta_i={1+\alpha_\infty+(3\alpha_\infty-1)x_i^{(k)}\over4},
  \qquad
  \lambda_i={(3\alpha_\infty-1)x_i^{(k)}\over\beta_i}.
  \]
  These cutoffs and weights are strictly ordered and strictly all-middle.
  Applying (CR28dw) at each fixed \(k\) and then taking the supremum of the
  resulting scalar inequalities gives
  \[
  \liminf_{n\to\infty}{\Lambda_n\over n^3}
  \ge {434+4\sqrt2\over1587},
  \qquad
  \liminf_{n\to\infty}{R_2^*(n)\over n^3}
  \ge {434+4\sqrt2\over1587\pi}.
  \]
  The quantifiers are \(\forall k\,\exists N_k\): no \(k=k(n)\) is used,
  no threshold uniform in \(k\) is needed, and no limits are interchanged.
  The global clipped classification proves that this is the exact supremum
  of the entire continuous finite-prefix template family. It is strictly
  larger than \(C_{5,*}\), which remains the exact optimum of the fixed
  \(k=5\) template only.
- **EXACT METHOD-SPECIFIC THEOREM (GLOBALLY OPTIMIZED FIVE PREFIXES):**
  the full eleven-parameter compact closure reduces coordinatewise to the
  clipped density objective (CR28dz22). All 21 regimes \(H^hM^m0^z\), the
  four in-domain transitions, the formal transition beyond \(\alpha=1\),
  every density collision, every ordered-weight face, and both outer density
  faces are classified in (CR28dz23)--(CR28dz31). The unique global point is
  strictly all-middle, with
  \[
  \alpha_{5,*}
  ={422413777961580309772684503
   -10047852311701\sqrt{183342238504950468196395903}
   \over661485317418210151348973103},
  \]
  and the five exact cutoff/weight pairs are (CR28dz37)--(CR28dz38). Its
  coefficient is
  \[
  C_{5,*}
  ={346693217780244687187063490332457027500975566238012204
   +1228130489996268437333105902690103574002
    \sqrt{183342238504950468196395903}
   \over1312688475479610714750859896048564873968757997852345827},
  \]
  with
  \[
  C_{5,*}>C_{5,\mathrm{rat}}>C_{4,*}.
  \]
  Consequently
  \(\liminf\Lambda_n/n^3\ge C_{5,*}\) and
  \(\liminf R_2^*(n)/n^3\ge C_{5,*}/\pi\). No finite rounding at this
  irrational optimizer is asserted.
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
  \(\liminf R_2^*(n)/n^3\ge C_{5,\mathrm{rat}}/\pi\). Its original
  derivation is one explicit fixed-parameter specialization without a global
  optimization; the exact theorem above now proves it is strictly
  suboptimal.
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
  rounding at the optimized four- or five-prefix points. None of those
  uniform statements is needed for the all-fixed-\(k\) supremum corollary.
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
- **VERIFIED FACT (INDEPENDENT GLOBAL FIVE-PREFIX OPTIMIZATION
  DIAGNOSTIC):** one standalone standard-library script checks the 21 clipped
  words, all five transition rows, collision identities, the primitive
  optimizer and coefficient polynomials, rational isolating intervals,
  strict all-middle density/weight inequalities, end-to-end coefficient
  identities, and the exact margins proving
  \(C_{5,*}>C_{5,\mathrm{rat}}>C_{4,*}\). It imports no project,
  production, test, artifact, backend, certificate, or enumeration helper and
  corroborates rather than replaces the compact proof.
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

The first five rows recover, exactly and in the same normalization, all
documented optimized prefix-simplex values:

| \(k\) | unique maximizer \((x_1,\ldots,x_k)\) | ratios \((r_1,\ldots,r_k)\) | \(M_k\) | \(M_k/8\) |
|---:|---|---|---:|---:|
| 1 | \((2/3)\) | \((2/3)\) | \(4/27\) | \(1/54\) |
| 2 | \((18/23,12/23)\) | \((18/23,2/3)\) | \(108/529\) | \(27/1058\) |
| 3 | \((1058/1263,276/421,184/421)\) | \((1058/1263,18/23,2/3)\) | \(1119364/4785507\) | \(279841/9571014\) |
| 4 | \((3190338,2672508,2091528,1394352)/3666143\) | \((3190338/3666143,1058/1263,18/23,2/3)\) | \(3392752184748/13440604496449\) | \(848188046187/26881208992898\) |
| 5 | \((26881208992898,23392470652668,19595592993288,15335681473008,10223787648672)/30143556935103\) | \((26881208992898/30143556935103,3190338/3666143,1058/1263,18/23,2/3)\) | \(722599396919860307414438404/2725902074099388500860861827\) | \(180649849229965076853609601/5451804148198777001721723654\) |

The last column is the scale appearing after
\(X_i=(3\alpha-1)x_i\): it reproduces respectively the one-prefix residual
coefficient, (CR28bw12), (CR28cn), the four-prefix envelope (CR28dq8), and
the five-prefix envelope (CR28dz34).

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
\(k=k(n)\). The degenerate endpoint value (CR28dc) is not promoted to a
lower bound. The all-middle value (CR28dd), however, *is* promoted below by
applying the two separate theorems at every fixed finite \(k\) and then taking
the supremum of the resulting scalar lower bounds. That argument uses no
growing prefix count and no interchange of limits.

### Arbitrarily many finite selected prefixes with one slack partition

The preceding cases are instances of one finite theorem whose proof does not
depend on the number of selected frontiers. The normalized simplex
(CR28cr)--(CR28dd) is independent of this charging statement, so the proof
returns directly to literal split histories. No coefficient optimization,
finite-rounding specialization, growing-prefix limit, or geometric deduction
is made *inside the finite theorem*. The subsequent corollary combines its
fixed-\(k\) instances with the independent normalized optimizers.

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
of \(n\to\infty\) with \(k\to\infty\) and no infinite-prefix theorem. Those
limitations do not prevent applying it separately at every fixed \(k\),
taking the ordinary fixed-parameter \(n\to\infty\) liminf each time, and
then taking the supremum of the already-established scalar inequalities.

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

### All-fixed-\(k\) asymptotic corollary

The normalized simplex and the direct charging theorem can now be combined
for *every fixed finite* \(k\). Put

\[
\boxed{
\alpha_\infty={13-2\sqrt2\over23},
\qquad
S_\infty=1+\alpha_\infty,
\qquad
A_\infty=3\alpha_\infty-1.
}
\tag{CR28dw1}
\]

Exact squaring of positive quantities gives
\(1/3<\alpha_\infty<1/2\), and hence \(A_\infty>0\). For a fixed
integer \(k\ge1\), let
\(x^{(k)}=(x_1^{(k)},\ldots,x_k^{(k)})\) be the unique normalized maximizer
from (CR28cu)--(CR28cv), with \(x_0^{(k)}=1\), and define

\[
\boxed{
\beta_i={S_\infty+A_\infty x_i^{(k)}\over4},
\qquad
\lambda_i={A_\infty x_i^{(k)}\over\beta_i}
\quad(1\le i\le k).
}
\tag{CR28dw2}
\]

The strict interiority already proved in (CR28cv) says

\[
1=x_0^{(k)}>x_1^{(k)}>\cdots>x_k^{(k)}>0.
\]

Let \(L_\infty=S_\infty/4\) and \(U_\infty=S_\infty/3\), the two
clipping boundaries in (CR28bw2). For every \(i\),

\[
\begin{aligned}
\beta_i-L_\infty
&={A_\infty x_i^{(k)}\over4}>0,\\
\alpha_\infty-\beta_i
&={A_\infty(1-x_i^{(k)})\over4}>0,\\
U_\infty-\beta_i
&={S_\infty-3A_\infty x_i^{(k)}\over12}
>{S_\infty-3A_\infty\over12}
={1-2\alpha_\infty\over3}>0.
\end{aligned}
\tag{CR28dw3}
\]

Thus all cutoffs are strictly in the middle branch and are strictly ordered.
Moreover

\[
\lambda_i
={4A_\infty x_i^{(k)}\over S_\infty+A_\infty x_i^{(k)}},
\qquad
{d\over dx}{4A_\infty x\over S_\infty+A_\infty x}
={4A_\infty S_\infty\over(S_\infty+A_\infty x)^2}>0,
\tag{CR28dw4}
\]

while \(3A_\infty x_i^{(k)}<S_\infty\) by (CR28dw3). Consequently

\[
\boxed{
0<\beta_k<\cdots<\beta_1<\alpha_\infty<1,
\qquad
0<\lambda_k<\cdots<\lambda_1<1.
}
\tag{CR28dw5}
\]

For this fixed \(k\), all continuous margins are strict. The elementary
floor/ceiling convergence used after (CR28dr) therefore supplies a finite
threshold \(N_k\), allowed to depend on the complete \(k\)-tuple, such that
\(r_n=\lfloor\alpha_\infty n\rfloor\) and
\(s_{i,n}=\lceil\beta_i n\rceil\) satisfy every integer admissibility
condition for \(n\ge N_k\). Apply (CR28dw), then (CR28ap), divide by
\(n^3\), and take the ordinary fixed-parameter liminf. Since the sum has the
fixed finite length \(k\), (CR28az) gives

\[
\begin{aligned}
L_\Lambda
:={}&\liminf_{n\to\infty}{\Lambda_n\over n^3}\\
\ge{}&p(\alpha_\infty)
+\sum_{i=1}^k(\beta_{i-1}-\beta_i)
g(\alpha_\infty,\beta_i,\lambda_i),
\qquad \beta_0=\alpha_\infty.
\end{aligned}
\tag{CR28dw6}
\]

Equation (CR28dw2) gives
\(\lambda_i=4-S_\infty/\beta_i\), exactly the middle clipped weight in
(CR28bw2). Hence (CR28bw3), with \(x_0^{(k)}=1\), yields

\[
g(\alpha_\infty,\beta_i,\lambda_i)
={A_\infty^2(x_i^{(k)})^2\over2},
\qquad
\beta_{i-1}-\beta_i
={A_\infty(x_{i-1}^{(k)}-x_i^{(k)})\over4}.
\tag{CR28dw7}
\]

Since \(F_k(x^{(k)})=M_k\), the right-hand side of (CR28dw6) is

\[
C_k(\alpha_\infty)
:=p(\alpha_\infty)+{A_\infty^3M_k\over8}.
\tag{CR28dw8}
\]

This proves the scalar inequality
\(L_\Lambda\ge C_k(\alpha_\infty)\) for every fixed finite \(k\).
Taking the supremum of these already-proved inequalities and using
\(M_k\nearrow1/3\) from (CR28cy) gives

\[
\boxed{
L_\Lambda
\ge\sup_{k\ge1}C_k(\alpha_\infty)
=p(\alpha_\infty)+{A_\infty^3\over24}
={434+4\sqrt2\over1587}
=:C_{\mathrm{AF}}.
}
\tag{CR28dw9}
\]

The last evaluation is (CR28dd). The exact comparison with the former
current coefficient is strict:

\[
p(\alpha_\infty)={9038+722\sqrt2\over36501},
\qquad
{A_\infty^3\over24}={944-630\sqrt2\over36501};
\]

their sum is
\((9982+92\sqrt2)/36501=(434+4\sqrt2)/1587\), giving a direct
simplification independent of merely quoting the earlier envelope value.

\[
C_{5,*}
<{276777463862377\over10^{15}}
<{277\over1000}
<C_{\mathrm{AF}}.
\tag{CR28dw10}
\]

The first inequality is (CR28dz40). For the last one, clearing positive
denominators reduces it to \(4000\sqrt2>5599\), whose square margin is
\(32{,}000{,}000-31{,}348{,}801>0\). Thus \(C_{5,*}\) remains the exact
global optimum of the *fixed \(k=5\) template*, but it is not the strongest
coefficient obtained by using all fixed finite \(k\).

Finally, the additive cyclic-ratio relation (CR28), equivalently (CR39),
has normalized error below \(1/n\). Therefore

\[
\boxed{
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\ge {C_{\mathrm{AF}}\over\pi}
={434+4\sqrt2\over1587\pi}.
}
\tag{CR28dw11}
\]

The quantifier order is essential and elementary:

\[
\forall k\ge1:\
\left[
{\Lambda_n\over n^3}\ge B_{k,n}\ \hbox{ eventually},
\quad B_{k,n}\longrightarrow C_k(\alpha_\infty)
\right]
\quad\Longrightarrow\quad
\forall k\ge1:\ L_\Lambda\ge C_k(\alpha_\infty)
\quad\Longrightarrow\quad
L_\Lambda\ge\sup_{k\ge1}C_k(\alpha_\infty).
\tag{CR28dw12}
\]

Here \(B_{k,n}\) is the normalized right-hand side of (CR28dw), and its
eventual validity begins at the tuple-dependent \(N_k\).
No value \(k=k(n)\) is selected. No common threshold
\(\sup_kN_k<\infty\) is asserted or needed. No \(n\)-limit is interchanged
with a \(k\)-limit: \(M_k\to1/3\) is used only to evaluate the supremum of
the scalar coefficients *after* every fixed-\(k\) liminf inequality has been
established. Because \(M_k<1/3\) for every finite \(k\), this argument also
does not produce a finite rounded theorem of the form
\(\Lambda_n\ge C_{\mathrm{AF}}n^3\) beyond some common threshold.

### Global compact clipped envelope for every finite prefix count

The preceding corollary used one all-middle point for each fixed \(k\). It
remains to decide whether a clipped high-weight regime can do better when the
*entire* continuous finite-prefix family is optimized. The answer is no.

Fix \(k\ge1\), put \(\beta_0=\alpha\), and take the full ordered compact
closure

\[
\mathcal D_k=
\left\{
\begin{aligned}
&0\le\beta_k\le\cdots\le\beta_1\le\alpha\le1,\\
&0\le\lambda_k\le\cdots\le\lambda_1\le1
\end{aligned}
\right\}.
\]

The continuous coefficient on this closure is

\[
C_k(\alpha,\boldsymbol\beta,\boldsymbol\lambda)
=p(\alpha)+\sum_{i=1}^k
(\beta_{i-1}-\beta_i)g(\alpha,\beta_i,\lambda_i).
\tag{CR28dw13}
\]

Let \(s=1+\alpha\). For fixed densities, (CR28bw1)--(CR28bw3) give
the unique clipped optimum \(\psi_s(\beta_i)\) on every positive segment.
The map \(\psi_s\) is nondecreasing, so these coordinatewise optima already
satisfy the ordered-weight constraints. Zero-length segments leave their
weights unused but do not change the value. Hence the exact compact density
reduction for arbitrary finite \(k\) is

\[
\boxed{
\overline C_k(\alpha,\boldsymbol\beta)
=p(\alpha)+\sum_{i=1}^k
(\beta_{i-1}-\beta_i)\Phi_s(\beta_i),
}
\tag{CR28dw14}
\]

where \(\Phi_s\) is (CR28bw3). Density order leaves exactly

\[
H^hM^m0^z,
\qquad h,m,z\ge0,
\qquad h+m+z=k,
\]

so the full clipped problem has \((k+1)(k+2)/2\) regimes. This includes all
clipping surfaces, density collisions, and unused weight faces without a
fixed-\(k\) regime enumeration.

Normalize

\[
\tau={\alpha\over1+\alpha},
\qquad
\rho_i={\beta_i\over1+\alpha},
\qquad
\rho_0=\tau,
\]

and define the continuous increasing function

\[
\phi(x)=
\begin{cases}
0,&0\le x\le1/4,\\[1mm]
(4x-1)^2/2,&1/4\le x\le1/3,\\[1mm]
-x^2+2x-1/2,&1/3\le x\le1/2.
\end{cases}
\tag{CR28dw15}
\]

Thus \(\Phi_s(sx)=s^2\phi(x)\). The exact density-optimized clipped envelope
at fixed \(\alpha\) is

\[
\boxed{
\mathscr H_k(\alpha)
=p(\alpha)+(1+\alpha)^3V_k\!\left({\alpha\over1+\alpha}\right),
}
\tag{CR28dw16}
\]

where either of the equivalent compact definitions may be used:

\[
\begin{aligned}
V_k(t)
&=\max_{0\le\rho_k\le\cdots\le\rho_1\le t}
\sum_{i=1}^k(\rho_{i-1}-\rho_i)\phi(\rho_i),
\qquad \rho_0=t,\\
V_0(t)&=0,
\qquad
V_m(t)=\max_{0\le x\le t}
\bigl((t-x)\phi(x)+V_{m-1}(x)\bigr).
\end{aligned}
\tag{CR28dw17}
\]

This is the requested compact clipped envelope for arbitrary \(k\). It is
different from the formal polynomial relaxation \(E_k\) in (CR28cz) whenever
a high coordinate is present.

There is a short global comparison that keeps the clipping. On
\([1/4,1/2]\), \(\phi\) is strictly increasing and has Lipschitz constant
\(4/3\). Every finite chain in (CR28dw17) is a lower Darboux sum, possibly
with an omitted initial interval. Therefore, with

\[
I(t)=
\begin{cases}
0,&0\le t\le1/4,\\[1mm]
(4t-1)^3/24,&1/4\le t\le1/3,\\[1mm]
-t^3/3+t^2-t/2+5/72,&1/3\le t\le1/2,
\end{cases}
\tag{CR28dw18}
\]

one has

\[
V_k(t)<I(t)\quad(t>1/4).
\]

Conversely, divide \([1/4,t]\) into \(k\) equal intervals and use their
lower endpoints as the cutoffs. The resulting admissible sum gives

\[
0\le I(t)-V_k(t)
\le {2(t-1/4)^2\over3k}
\le {1\over24k}.
\tag{CR28dw19}
\]

Duplicating the last cutoff of any maximizing chain shows
\(V_{k+1}(t)\ge V_k(t)\). Hence the displayed error bound gives the claimed
monotone convergence, not merely convergence along a selected sequence.
Consequently \(V_k\nearrow I\) uniformly, and the pointwise supremum of the
full clipped envelopes over all finite prefix counts is

\[
\boxed{
\mathscr H_{\mathrm{fin}}(\alpha)
:=\sup_{k<\infty}\mathscr H_k(\alpha)
=
\begin{cases}
p(\alpha),&0\le\alpha\le1/3,\\[1mm]
\dfrac{23\alpha^3-39\alpha^2+21\alpha+3}{24},
 &1/3\le\alpha\le1/2,\\[3mm]
\dfrac{5\alpha^3-21\alpha^2+15\alpha+17}{72},
 &1/2\le\alpha\le1.
\end{cases}
}
\tag{CR28dw20}
\]

The notation \(\mathscr H_{\mathrm{fin}}\) denotes a pointwise supremum of
finite templates, not an admissible infinite-prefix charging statement.

The outer density regions cannot contain a finite-\(k\) global maximizer.
For \(0\le\alpha\le1/3\), the residual vanishes and
\(p(\alpha)\le22/81\). On \([1/2,1]\), the last polynomial in
(CR28dw20) has derivative

\[
{5\alpha^2-14\alpha+5\over24}<0,
\]

so it is at most \(53/192\). Both bounds are strictly below the feasible
one-prefix all-middle optimum

\[
C_{1,*}={4+2\sqrt3\over27},
\qquad
C_{1,*}-{22\over81}={6\sqrt3-10\over81}>0,
\qquad
C_{1,*}-{53\over192}={128\sqrt3-221\over1728}>0.
\tag{CR28dw21}
\]

The last sign follows from the positive square margin
\(128^2\cdot3-221^2=311\). For every \(k\), a strict \(k\)-prefix
all-middle point at the one-prefix optimizing density has value at least
\(C_{1,*}\), because \(M_k\ge M_1\). Hence every global compact maximizer
has

\[
{1\over3}<\alpha<{1\over2}.
\]

On this interval no cutoff can be high, because
\(\beta_i\le\alpha<(1+\alpha)/3\). Put

\[
A=3\alpha-1,
\qquad
X_i=4\beta_i-(1+\alpha)
\]

on the active middle prefix, and replace an inactive suffix by \(X_i=0\).
Then \(X_0=A\), and (CR28dw14) reduces exactly to the normalized simplex:

\[
\boxed{
\mathscr H_k(\alpha)
=E_k(\alpha)
=p(\alpha)+{M_k\over8}(3\alpha-1)^3
\qquad(1/3\le\alpha\le1/2).
}
\tag{CR28dw22}
\]

For \(1/3<\alpha\le1/2\), equality is unique in the density variables by
(CR28cu)--(CR28cv), and its normalized coordinates are \(x^{(k)}\). In
particular, the unique simplex point has no inactive suffix. At
\(\alpha=1/3\), the residual is identically zero and density uniqueness is
neither true nor needed; the global maximizer has already been localized to
the open interval.

The one-variable envelope is strictly concave on this interval. Indeed,

\[
E_k''(\alpha)
=-1-\alpha+{27M_k\over4}(3\alpha-1),
\]

which is affine and is negative at both endpoints, while

\[
E_k'(1/3)={1\over9}>0,
\qquad
E_k'(1/2)={9M_k-4\over32}<-{1\over32}.
\tag{CR28dw23}
\]

Thus its unique maximum is the smaller root in \((1/3,1/2)\) of

\[
(81M_k-4)\alpha^2-(54M_k+8)\alpha+(9M_k+4)=0,
\]

namely

\[
\boxed{
\alpha_{k,*}
={27M_k+4-2\sqrt{2(4-9M_k)}\over81M_k-4}.
}
\tag{CR28dw24}
\]

The unique full compact maximizing tuple is

\[
\boxed{
\begin{aligned}
\beta_{i,*}
&={1+\alpha_{k,*}+(3\alpha_{k,*}-1)x_i^{(k)}\over4},\\
\lambda_{i,*}
&={4(3\alpha_{k,*}-1)x_i^{(k)}
 \over1+\alpha_{k,*}+(3\alpha_{k,*}-1)x_i^{(k)}}
\qquad(1\le i\le k).
\end{aligned}
}
\tag{CR28dw25}
\]

All density and weight inequalities are strict. More explicitly,
\(x_1^{(k)}=q_k<1\), and the first all-middle-to-high transition of the
normalized equality point is

\[
\alpha_{\mathrm{tr},k}
={3q_k+1\over9q_k-1}>{1\over2}.
\tag{CR28dw26}
\]

Thus every global maximizer is not merely representable by an all-middle
tuple: for every finite \(k\), it is the single strict all-middle tuple
(CR28dw24)--(CR28dw25). No clipped counterexample regime exists.

Define the exact fixed-template optimum

\[
C_{k,*}:=E_k(\alpha_{k,*}).
\]

Because \(M_{k+1}>M_k\), evaluating \(E_{k+1}\) at \(\alpha_{k,*}\)
shows \(C_{k+1,*}>C_{k,*}\). Uniform convergence on
\([1/3,1/2]\) and the unique limiting maximum (CR28dd) give

\[
\boxed{
\alpha_{k,*}\longrightarrow{13-2\sqrt2\over23},
\qquad
C_{k,*}\nearrow{434+4\sqrt2\over1587}=C_{\mathrm{AF}}.
}
\tag{CR28dw27}
\]

Since \(M_k<1/3\), every finite value \(C_{k,*}\) is strictly below
\(C_{\mathrm{AF}}\). Combining (CR28dw20)--(CR28dw27) proves the exact
classification of the whole family:

\[
\boxed{
\sup_{\substack{k<\infty\\
 (\alpha,\boldsymbol\beta,\boldsymbol\lambda)\in\mathcal D_k}}
C_k(\alpha,\boldsymbol\beta,\boldsymbol\lambda)
=\max_{0\le\alpha\le1}\mathscr H_{\mathrm{fin}}(\alpha)
=C_{\mathrm{AF}}.
}
\tag{CR28dw28}
\]

The supremum is not attained at any finite \(k\); its unique limiting density
is \((13-2\sqrt2)/23\). For each fixed \(k\), the strict tuple
(CR28dw25) has its own eventual integer-admissibility threshold, so (CR28dw)
also gives

\[
L_\Lambda\ge C_{k,*}\quad(k<\infty),
\qquad
L_\Lambda\ge\sup_k C_{k,*}=C_{\mathrm{AF}}.
\tag{CR28dw29}
\]

This recovers (CR28dw9) with the globally optimized member at each finite
\(k\), but it does not change the numerical lower coefficient. It introduces
no \(k=k(n)\), uniform threshold, finite rounding, production computation,
or interchange with the \(n\to\infty\) liminf.

The dossier-local standard-library exact diagnostic independently checks the
clipped formulas, the three-piece integral on a rational grid, discrete
Bellman lower sums, the first twelve exact simplex rows and critical-point
brackets, the surd comparisons in (CR28dw21), bounded sampled comparisons
supporting (CR28dw28), and the adversarial fact \(M_7>C_{\mathrm{AF}}\). The
last check confirms that the valid but loose formal upper relaxation
\(E_7(1)=M_7\) cannot by itself prove the sharp clipped bound
\(C_{\mathrm{AF}}\).

### Explicit five-prefix rational asymptotic witness

The normalized-simplex and direct charging theorems can also be combined at
one fixed finite value
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

The subscript “rat” is deliberate: this fixed point is not the global
five-prefix optimizer, as the optimization below proves. To compare it
exactly with (CR28dq11), write

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
five-prefix point. The finite theorem below retains exactly the same tuple;
the subsequent compact optimization proves that this point is a strict
suboptimal witness. The standalone script in
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

#### Global optimization of the continuous five-prefix coefficient

The finite theorem above remains attached to its fixed rational tuple. We now
return to the unrounded continuous problem and optimize all eleven parameters
at fixed \(k=5\). This uses only the already proved charging theorem
(CR28dr)--(CR28dw) and the normalized simplex (CR28cr)--(CR28cw); it adds no
finite rounding or growing-\(k\) passage.

For fixed strictly admissible real parameters, the coefficient obtained by
taking the usual fixed-parameter limit in (CR28dw) is

\[
\boxed{
C_5=p(\alpha)+\sum_{i=1}^5
 (\beta_{i-1}-\beta_i)g(\alpha,\beta_i,\lambda_i),
\qquad \beta_0=\alpha.
}
\tag{CR28dz20}
\]

The strict proof-valid domain is dense in the compact ordered closure

\[
\boxed{
0\le\beta_5\le\beta_4\le\beta_3\le\beta_2\le\beta_1\le\alpha\le1,
\qquad
0\le\lambda_5\le\lambda_4\le\lambda_3\le\lambda_2\le\lambda_1\le1.
}
\tag{CR28dz21}
\]

Put \(s=1+\alpha\), \(L=s/4\), \(U=s/3\), and
\(d_i=\beta_{i-1}-\beta_i\). Every positive-length summand is strictly
concave in its weight. The only compact point where the second derivative
vanishes is \((\alpha,\beta)=(1,1)\), whose segment necessarily has zero
length. The unique clipped optimum is the nondecreasing map

\[
\psi_s(\beta)=
\begin{cases}
0,&\beta\le L,\\
4-s/\beta,&L<\beta<U,\\
1,&U\le\beta.
\end{cases}
\]

Thus the five coordinatewise optima already obey the weight order. If a
segment has zero length, its unused weight can be filled between its ordered
neighbors without changing the value. There is no pooled KKT branch, and the
exact compact reduction is

\[
\boxed{
\overline C_5(\alpha,\boldsymbol\beta)
=p(\alpha)+\sum_{i=1}^5d_i\Phi_s(\beta_i).
}
\tag{CR28dz22}
\]

Strict concavity and the clipped reduction (CR28bw1)--(CR28bw4) show term by
term that no other ordered weight tuple can tie unless its positive-length
coordinates equal their clipped optima.

The density order leaves exactly the 21 clipping regimes
\(H^hM^m0^z\), \(h+m+z=5\):

\[
\begin{gathered}
00000;\\
M0000,\ H0000;\\
MM000,\ HM000,\ HH000;\\
MMM00,\ HMM00,\ HHM00,\ HHH00;\\
MMMM0,\ HMMM0,\ HHMM0,\ HHHM0,\ HHHH0;\\
MMMMM,\ HMMMM,\ HHMMM,\ HHHMM,\ HHHHM,\ HHHHH.
\end{gathered}
\tag{CR28dz23}
\]

The clipping surfaces are precisely \(\beta_i=L\), where
\(\lambda_i=0\), and \(\beta_i=U\), where \(\lambda_i=1\). Both
\(\Phi_s\) and \(\Phi_s'\) agree across each join. On an internal face
\(0<\lambda_{i+1}=\lambda_i<1\) with two positive segment lengths, distinct
clipped optima admit a feasible separating improvement. If both optima are
the same endpoint, moving both common weights toward that endpoint improves
instead. A common middle optimum forces a density collision. Zero-length
segments are unused. Thus every internal weight collision is either excluded
by one of these directions or belongs to a plateau, join, density-collision,
or unused subface already represented in (CR28dz23). Consecutive unused
blocks may be filled arbitrarily between their active neighbors.

For the complete fixed-density classification, normalize

\[
\tau={\alpha\over1+\alpha},
\qquad
\rho_i={\beta_i\over1+\alpha},
\]

and retain the function \(\phi\) from (CR28do). The residual in (CR28dz22)
is \((1+\alpha)^3\mathcal V^{(5)}_\tau\), where

\[
\mathcal V^{(5)}_\tau
=(\tau-\rho_1)\phi(\rho_1)
+\sum_{i=2}^5(\rho_{i-1}-\rho_i)\phi(\rho_i).
\tag{CR28dz24}
\]

For \(\tau\le1/4\) the residual vanishes. If \(\tau>1/4\), none of the 15
words with a trailing zero can maximize. If all coordinates are inactive,
choosing \(\rho_1\in(1/4,\tau)\) adds a positive term. Otherwise, appending a
cutoff strictly between \(1/4\) and the last active cutoff does the same.

The Bellman recursion and stationarity equations are (CR28dp) with five
coordinates; the four predecessor maps (CR28dq) are unchanged. The only new
mixed-base estimate beyond the four-prefix audit is a high coordinate
followed by an optimized middle tail of length four. With

\[
q_4={3190338\over3666143},
\]

the relevant interval is
\(1/3\le y\le1/(3q_4)=3666143/9571014\), and

\[
T_4'(y)-1
={17-(1+8q_4^2)y(6-y)\over2(3-y)^2}.
\]

The numerator decreases on this interval and at the right endpoint equals

\[
{609160555391902550135\over335834496166911848028}>0.
\tag{CR28dz25}
\]

The corresponding \(m=1,2,3\) margins are already recorded after (CR28dq),
and the terminal H0 derivative is positive there as well. Outward
propagation uses the HH identity only when both adjacent coordinates are
high; it is not used across an HM interface. The same inverse-derivative
induction then makes every active regional maximum unique. Direct exact
substitution in the predecessor maps gives the complete winner sequence

\[
\begin{array}{c|c}
\alpha\text{ interval}&\text{winning regime}\\ \hline
0\le\alpha\le1/3&00000\\
1/3<\alpha<\alpha_1&MMMMM\\
\alpha_1<\alpha<\alpha_2&HMMMM\\
\alpha_2<\alpha<\alpha_3&HHMMM\\
\alpha_3<\alpha<\alpha_4&HHHMM\\
\alpha_4<\alpha\le1&HHHHM,
\end{array}
\tag{CR28dz26}
\]

where

\[
\boxed{
\begin{aligned}
\alpha_1&={36929061304599\over70595774666993},&
\alpha_2&={229053579602567\over410211009692329},\\
\alpha_3&={309127972999621\over499292225089307},&
\alpha_4&={3403232546992614203\over4537959314998507141}.
\end{aligned}
}
\tag{CR28dz27}
\]

At each transition the point is unique and belongs to both adjacent branch
closures. The exact normalized densities and weights are

\[
\begin{array}{c|c|c}
\tau&(\rho_1,\rho_2,\rho_3,\rho_4,\rho_5)
 &(\lambda_1,\lambda_2,\lambda_3,\lambda_4,\lambda_5)\\ \hline
{36929061304599\over107524835971592}
 &(1/3,4729589/14664572,4556979/14664572,
   4363319/14664572,4130927/14664572)
 &(1,4253784/4729589,3563344/4556979,
   2788704/4363319,1859136/4130927)\\[1mm]
{229053579602567\over639264589294896}
 &(13237157/38284056,1/3,4847/15156,513/1684,1447/5052)
 &(1,1,4232/4847,368/513,736/1447)\\[1mm]
{309127972999621\over808420198088928}
 &(76718581/209712528,1479/4232,1/3,29/92,27/92)
 &(1,1,1,24/29,16/27)\\[1mm]
{3403232546992614203\over7941191861991121344}
 &(1806469369/4470813792,7607/20016,77/216,1/3,11/36)
 &(1,1,1,1,8/11).
\end{array}
\tag{CR28dz28}
\]

The formal HHHHM--HHHHH transition is

\[
\tau_5={27936208629060590955659\over50072626139262934446720}>{1\over2},
\qquad
\alpha_5={27936208629060590955659\over22136417510202343491061}>1,
\tag{CR28dz29}
\]

at

\[
\boldsymbol\rho
=\left({199200916177\over391198109760},{93059\over201120},
 {301\over720},{3\over8},{1\over3}\right),
\qquad
\boldsymbol\lambda=(1,1,1,1,1).
\]

Thus HHHHH never wins on the admissible compact domain. Equations
(CR28dz23), (CR28dz26), and (CR28dz28)--(CR28dz29) audit every clipping
regime and every transition, not only the branch containing the global point.

The compact-face audit is also exact. Each density facet

\[
\beta_1=\alpha,\quad
\beta_2=\beta_1,\quad
\beta_3=\beta_2,\quad
\beta_4=\beta_3,\quad
\beta_5=\beta_4,\quad
\beta_5=0
\tag{CR28dz30}
\]

deletes one summand of the clipped objective (CR28dz22), so its exact maximum
is \(C_{4,*}\). Further collisions leave at most three effective prefixes.
On the outer weight facet \(\lambda_5=0\), the last term vanishes. On
\(\lambda_1=1\), differentiation at fixed remaining parameters gives

\[
{\partial C_5\over\partial\alpha}
=-(\alpha-\beta_1)(2\alpha-3\beta_1+3)
+\sum_{i=2}^5d_i
 {\lambda_i(2\beta_i-1-\alpha)\over2-\lambda_i}
\le0.
\tag{CR28dz31}
\]

Moving to \(\alpha=\beta_1\) deletes the first term, so this facet also has
exact maximum \(C_{4,*}\). The directional argument above excludes every
remaining internal weight diagonal from the later strict all-middle equality
case; collision and unused subfaces reduce, while plateau and join subfaces
are covered by the branch audit. The six deletion facets in (CR28dz30)
together with \(\alpha=1\) are all seven facets of the ordered density
simplex. At its collapsed vertex \(\alpha=0\), all densities vanish and the
value is \(p(0)=1/6\). At \(\alpha=1\), the envelope below gives
\(C_5\le M_5<22/81<C_{5,\mathrm{rat}}\). Their intersections inherit the
corresponding reductions or exclusions. This completes the density,
weight-collision, and compact-face audit.

It remains to locate the global value. For \(\alpha>1/3\), put
\(A=3\alpha-1\). On active cutoffs set
\(X_i=4\beta_i-(1+\alpha)\), and replace an inactive suffix by zeros. Then

\[
0\le X_5\le X_4\le X_3\le X_2\le X_1\le A.
\]

For every active coordinate,

\[
\Phi_{1+\alpha}(\beta_i)\le {X_i^2\over2},
\]

with equality on the middle branch and exact high-branch loss
\((3\beta_i-1-\alpha)^2\). Hence, with \(X_0=A\),

\[
\overline C_5-p(\alpha)
\le {1\over8}\sum_{i=1}^5(X_{i-1}-X_i)X_i^2.
\tag{CR28dz32}
\]

Set \(x_i=X_i/A\). The nonnegative certificate (CR28cu) at \(k=5\) gives

\[
F_5(x_1,\ldots,x_5)\le M_5
={722599396919860307414438404
 \over2725902074099388500860861827},
\]

with equality uniquely at

\[
\boxed{
(x_1,x_2,x_3,x_4,x_5)
={1\over30143556935103}
(26881208992898,23392470652668,19595592993288,
 15335681473008,10223787648672).
}
\tag{CR28dz33}
\]

Therefore the exact all-middle envelope is

\[
\begin{aligned}
E_5(\alpha)
&=p(\alpha)+{M_5\over8}(3\alpha-1)^3\\
&={1984455952254630454046919309\alpha^3
 -3801724001654222787954160527\alpha^2
 +2175875358584537096271674118\alpha
 +363992087734915545050005504
 \over2725902074099388500860861827}.
\end{aligned}
\tag{CR28dz34}
\]

Its derivative is \(Q_5(\alpha)/302878008233265388984540203\), where

\[
Q_5(a)=661485317418210151348973103a^2
-844827555923160619545369006a
+241763928731615232919074902.
\tag{CR28dz35}
\]

This polynomial is primitive. Its discriminant is

\[
(20095704623402)^2\cdot183342238504950468196395903,
\]

and the last factor is \(3\bmod5\), hence is not a square.

The exact signs

\[
Q_5(1/3)={100959336077755129661513401\over3}>0,
\quad
Q_5(1/2)=-{61114079501650156065465301\over4}<0,
\quad
Q_5(1)=58421690226664764722678999>0
\]

make the smaller root a local maximum and the larger root a later local
minimum. Moreover

\[
E_5(1/3)-E_5(1)
={22\over81}-M_5
={53307202951031930309979610
 \over8177706222298165502582585481}>0.
\]

On \(0\le\alpha\le1/3\), the residual vanishes and \(p(\alpha)\) is
strictly increasing. It follows that the unique global envelope maximum is
the smaller root

\[
\boxed{
\alpha_{5,*}
={422413777961580309772684503
 -10047852311701\sqrt{183342238504950468196395903}
 \over661485317418210151348973103}.
}
\tag{CR28dz36}
\]

It is the root in

\[
{432907432458521\over10^{15}}
<\alpha_{5,*}<
{432907432458522\over10^{15}}.
\]

In particular,
\(1/3<\alpha_{5,*}<1/2<\alpha_1\); the last inequality has exact numerator
\(2(36929061304599)-70595774666993=3262347942205>0\). Thus the envelope
equality point lies strictly in MMMMM, so (CR28dz32) is an equality there.

Let

\[
D=30143556935103,
\qquad
(N_1,\ldots,N_5)
=(26881208992898,23392470652668,19595592993288,
 15335681473008,10223787648672),
\]

and put \(A_*=3\alpha_{5,*}-1\). The unique maximizing cutoffs and weights
are the five exact pairs

\[
\boxed{
\beta_{i,*}
={(D-N_i)+(D+3N_i)\alpha_{5,*}\over4D},
\qquad
\lambda_{i,*}
={4N_iA_*\over(D-N_i)+(D+3N_i)\alpha_{5,*}}
\quad(1\le i\le5).
}
\tag{CR28dz37}
\]

In individually reduced form they are

\[
\begin{array}{c|c|c}
i&\beta_{i,*}&\lambda_{i,*}\\ \hline
1&{3262347942205+110787183913797\alpha_{5,*}\over120574227740412}
 &{107524835971592A_*\over3262347942205+110787183913797\alpha_{5,*}}\\[1mm]
2&{2250362094145+33440322964369\alpha_{5,*}\over40191409246804}
 &{31189960870224A_*\over2250362094145+33440322964369\alpha_{5,*}}\\[1mm]
3&{152869042635+1288845448043\alpha_{5,*}\over1747452575948}
 &{1135976405408A_*\over152869042635+1288845448043\alpha_{5,*}}\\[1mm]
4&{214606890755+1103631903683\alpha_{5,*}\over1747452575948}
 &{889025012928A_*\over214606890755+1103631903683\alpha_{5,*}}\\[1mm]
5&{288692308499+881375650451\alpha_{5,*}\over1747452575948}
 &{592683341952A_*\over288692308499+881375650451\alpha_{5,*}}.
\end{array}
\tag{CR28dz38}
\]

Numerically,

\[
\boldsymbol\beta_*
=(0.424824974952,0.416181635894,0.406774882573,
  0.396220964212,0.383556262180)\ldots,
\]

\[
\boldsymbol\lambda_*
=(0.627064045325,0.557014272436,0.477394515131,
  0.383564823970,0.264153205804)\ldots .
\]

Their strict branch inequalities are exact. Since
\(D>N_1>\cdots>N_5>0\), the \(x_i=N_i/D\) are strictly ordered. With
\(L=(1+\alpha_{5,*})/4\), \(U=(1+\alpha_{5,*})/3\),

\[
\beta_{i,*}-L={A_*x_i\over4}>0,
\quad
\alpha_{5,*}-\beta_{i,*}={A_*(1-x_i)\over4}>0,
\]

and

\[
U-\beta_{i,*}
={1+\alpha_{5,*}-3A_*x_i\over12}
>{1-2\alpha_{5,*}\over3}>0.
\]

The map \(x\mapsto4A_*x/(1+\alpha_{5,*}+A_*x)\) is strictly increasing,
so

\[
0<\lambda_{5,*}<\cdots<\lambda_{1,*}<1.
\]

Conversely, equality in the high-branch loss, the simplex certificate, and
the scalar envelope forces exactly these data. Hence this is the unique
maximizing eleven-tuple on the whole compact closure.

Substitution gives the exact optimum

\[
\boxed{
C_{5,*}
={346693217780244687187063490332457027500975566238012204
 +1228130489996268437333105902690103574002
  \sqrt{183342238504950468196395903}
 \over1312688475479610714750859896048564873968757997852345827}.
}
\tag{CR28dz39}
\]

Equivalently,

\[
C_{5,*}
={2(903249246149825384268048005
 -183342238504950468196395903\alpha_{5,*})
 \over5953367856763891362140757927}.
\]

It is the root in

\[
{276777463862376\over10^{15}}
<C_{5,*}<
{276777463862377\over10^{15}}
\]

of the primitive irreducible polynomial

\[
\begin{aligned}
{}&35442588837949489298273217193311251597156465942013337329z^2\\
&\quad-18721433760133213108101428477952679485052680576852659016z\\
&\quad+2466564342132814822688647712444341404477077569119884404=0.
\end{aligned}
\tag{CR28dz40}
\]

Its discriminant is

\[
(66319046459798495615987718745265592996108)^2
\cdot183342238504950468196395903,
\]

so the same nonsquare factor proves irreducibility.

The improvement chain is exact. First,

\[
{276777463862376\over10^{15}}
>{1383887\over5000000}>C_{5,\mathrm{rat}},
\]

because the first cleared numerator is \(319311880000000>0\), while the
second is

\[
1383887Q-5000000N
=718080698409904604452109647000>0
\]

for \(C_{5,\mathrm{rat}}=N/Q\). Independently, the rational witness equals
\(E_5(13/30)\), and

\[
E_5'(13/30)
=-{34730769300472139183348711
 \over90863402469979616695362060900}<0,
\]

so uniqueness of the envelope maximum also gives the first strict
comparison without decimal reasoning. The exact margins from (CR28dz2) give

\[
271N-75Q=54550540142475357166378486777>0
\]

and, for \(C_{4,*}=(a+b\sqrt d)/c\),

\[
G=75c-271a=9840949830285493643999284949>0,
\]

\[
G^2-d(271b)^2
=202909790739538065073835756341295480167322654096276669>0.
\]

Therefore

\[
\boxed{
C_{5,*}>C_{5,\mathrm{rat}}>{75\over271}>C_{4,*}.
}
\tag{CR28dz41}
\]

Finally fix the strict tuple (CR28dz36)--(CR28dz38), apply the \(k=5\)
instance of (CR28dw), use (CR28ap), and take only the usual
fixed-parameter \(n\to\infty\) limit. The additive relation (CR28) gives

\[
\boxed{
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{5,*},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{5,*}\over\pi}.
}
\tag{CR28dz42}
\]

This is an exact globally optimized fixed-\(k=5\) template theorem. It does
not round the irrational optimizer at finite \(n\), alter the rational
\(n\ge234\) theorem, identify an exact residual or leading constant, prove
convergence, justify \(k=k(n)\), or change any production, artifact, schema,
backend, test-module, certificate, or enumeration path. The sole new
standalone script in
ops/TASK-20260717__global_five_prefix_optimization/exact_diagnostic.py
uses only standard-library exact arithmetic and checks all 21 clipped words,
the five transition rows, collision identities, the optimizer polynomial and
isolating interval, strict branch inequalities, coefficient identity and
polynomial, and every comparison margin. It corroborates but does not replace
the compact all-real proof.

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

## 8. Exact \(K\) For The Canonical Eight-Twenty-Fifths Core Order

Let \(\tau_n\) denote the cyclic core order called \(\sigma_n\) in the
matching construction (UC11) of research/PRODUCT_DISTANCE_SURROGATE.md, or
equivalently the order returned by eight_twenty_fifths_order(n). This section
determines \(K(\tau_n)\) on the whole public domain \(n\ge9\). The argument
uses the shortcut identity (L9-8)/(L10-18) and the symbolic block structure;
it does not enumerate subsets or cyclic orders.

### Exact statement on the symbolic domain

Retain the construction parameters
\[
d=4v+e,\qquad n=5v+e-1,\qquad 4\le e\le8,
\]
\[
t=\left\lfloor{v+e-2\over2}\right\rfloor,\qquad
\varepsilon=v+e-2-2t,\qquad r=v-t-\varepsilon.
\tag{K825-1}
\]
The symbolic domain is \(v\ge e-2\). Put \(L=2v+1\). Then the unique
maximizing subset is
\[
\boxed{
U_n^*=
\begin{cases}
\{L,L+1,\ldots,n\},&e=4,5,\\
\{L,L+1,\ldots,n\}\setminus\{L+1\},&e=6,7,8.
\end{cases}}
\tag{K825-2}
\]
Thus its cardinality is \(3v+e-1\) in the first two rows and
\(3v+e-2\) in the last three. The residue parameter \(e\) is fixed by
\(n\bmod5\) as in (UC3)--(UC4); no further residue split is needed.

Define
\[
\begin{aligned}
\mathcal Q(v,e,\varepsilon)={1\over8}\bigg[{}
&286v^3+(180e-91+10\varepsilon)v^2\\
&+(38e^2-34e-2-8(e+2)\varepsilon)v\\
&+{e(8e^2-9e-2)\over3}
 +(-2e^2-10e+21)\varepsilon\bigg],\\
\Gamma(v,e)&=(4e-22)v+e^2-7e+8,
\qquad
\chi=\mathbf1_{\{v=e-2\}}.
\end{aligned}
\tag{K825-3}
\]
The expression inside the square brackets is an integer multiple of \(8\) on
the admissible rows, and the exact value is
\[
\boxed{
K(\tau_n)
=\mathcal Q(v,e,\varepsilon)
 -(4e-7)\chi+\max\{0,\Gamma(v,e)\}.
}
\tag{K825-4}
\]
This is a period-ten integer quasipolynomial in \(n\), apart from the five
explicit boundary corrections \(v=e-2\). Those boundary values are
\[
\bigl(K(\tau_{13}),K(\tau_{19}),K(\tau_{25}),K(\tau_{31}),K(\tau_{37})\bigr)
=(724,2186,4898,9248,15608).
\tag{K825-5}
\]

### Shortcut-budget lemma

The following general lemma isolates the reason that no subset search is
needed. Let \(\tau\) be a cyclic order on \(V\), let \(S\subseteq V\) have
at least two elements, and suppose every member \(x\) of \(H=V\setminus S\)
is isolated in \(\tau\), between two members \(a_x,b_x\) of \(S\). Set
\[
h_x=a_xb_x-x(a_x+b_x).
\tag{K825-6}
\]
For an oriented arc \(A:i\to j\), delete only its internal members of \(H\)
and call the resulting path \(C(A)\). If
\[
h_x>0\quad(x\in H),\qquad
\sum_{ab\in E(C(A))}ab>ij
\tag{K825-7}
\]
whenever \(C(A)\) has at least two edges, then \(S\) is the unique subset
attaining \(K(\tau)\).

Indeed, if \(B=P_\tau(V)\), deletion of all isolated holes gives
\(P_\tau(S)=B+\sum_{x\in H}h_x\). For every subset \(U\) with
\(|U|\ge2\), its selected gaps partition the original cycle, and the exact
arc identity is
\[
\begin{aligned}
g(i,j)
&=ij-\sum_{ab\in E(A)}ab\\
&=ij-\sum_{ab\in E(C(A))}ab
  +\sum_{x\in H\cap\operatorname{int}(A)}h_x.
\end{aligned}
\tag{K825-8}
\]
Summing (K825-8) over the selected gaps gives
\[
P_\tau(U)-B
\le\sum_{x\in H\setminus U}h_x
\le\sum_{x\in H}h_x
=P_\tau(S)-B.
\tag{K825-9}
\]
Equality in the second inequality omits every hole. Equality in the first
then forces every selected gap to be one edge in the compressed backbone,
which forces \(U=S\). Finally \(S\) contains \(n-1,n\), so applying the
same inequality to that pair gives
\(P_\tau(S)\ge2n(n-1)>n^2\); no singleton can tie it. This proves the
lemma, including the adopted two-element convention.

### Positive deletion gains

For \(\tau_n\), first retain the tail
\(S_0=\{L,L+1,\ldots,n\}\). Its omitted labels \(2,\ldots,2v\) are
isolated by the block word (UC11). If \(e\ge6\), also omit the connector
\(c_0=L+1\) inside \(P_0\); it too is isolated. This gives exactly
\(S=U_n^*\).

It remains to verify the two hypotheses of the lemma. The ten symbolic rows
with \(r=0\) are recorded by finite exact shortcut certificates below. On
the remaining infinite tail \(v\ge e\), put
\[
E_j=d+j,\quad A_j=d-1-2j,\quad c_j=2v+2+j,\quad B_j=d-2-2j.
\]
The low holes on the two sides of a triple have gains
\[
\begin{aligned}
h_{\lambda,j}
={}&e^2+3ej+4ev-e-4j^2+14jv-3j-2v,\\
h_{\rho,j}
={}&e^2+3ej+4ev+e-4j^2+14jv-7j+6v-3.
\end{aligned}
\tag{K825-10}
\]
Both are concave in \(j\), and
\(h_{\rho,j}-h_{\lambda,j}=2e-4j+8v-3>0\). At the two endpoints,
\[
h_{\lambda,0}=(4e-2)v+e(e-1)>0,
\]
\[
2h_{\lambda,t-1}
=3e^2+e\varepsilon+21ev-e-2\varepsilon^2
 -10\varepsilon v-13\varepsilon+12v^2-47v-20>0.
\tag{K825-11}
\]
For the last inequality the right side increases for \(v\ge e\); at \(v=e\)
it is \(36e^2-48e-20\) when \(\varepsilon=0\), and
\(36e^2-57e-35\) when \(\varepsilon=1\), both positive for
\(4\le e\le8\).

For a singleton path \(x_j=2v+j+2+\varepsilon\), the left-hole gain
increases with \(j\), the right-hole gain exceeds it by
\(e+5j+2\varepsilon+6v+5\), and at the first singleton
\(j=t+\varepsilon\) four times the left gain is
\[
17v^2+(44e+52\varepsilon-48)v+11e^2+26e\varepsilon
 -12e-9\varepsilon-4>0.
\tag{K825-12}
\]
When the doubleton exists, four times its left and right low-hole gains are
\[
\begin{aligned}
&17v^2+(44e-86)v+11e^2-28e+9,\\
&17v^2+(44e-38)v+11e^2-4e-11,
\end{aligned}
\tag{K825-13}
\]
again positive for \(v\ge e\). These formulas cover every low hole. The
only additional candidate hole has exact gain
\[
(d-1)(d-2)-(2v+2)(2d-3)=\Gamma(v,e).
\tag{K825-14}
\]
It equals \(-6v-4,-2v-2,2v+2,6v+8,10v+16\) for
\(e=4,5,6,7,8\), respectively. This proves both why \(c_0\) is retained
in the first two cases and why it is uniquely deleted in the last three.

### Negative non-atomic shortcut gains

Delete the holes from an arbitrary oriented arc and let \(q\) be the number
of edges of its compressed path. All internal backbone labels are at least
\(L=2v+1\). The terminal and outer-triple labels are at least
\(H=3v+2+\varepsilon\).

If an endpoint is a hole, it is at most \(L+1\), and the direct bounds for
\(q=2,3\), starting with \(L(a+b)-ab\), are strictly positive. If both
endpoints are in the backbone and the middle label of a two-edge path is
greater than \(n/2\), positivity is automatic. The remaining two-edge
roles are finite block types:

- for a retained triple connector,
  \[
  M_j=c_j(A_j+B_j)-A_jB_j
  =-e^2+6ej-4ev+7e-8j^2+16jv-17j+22v-8;
  \tag{K825-15}
  \]
  this is concave. Its first retained values for \(e=4,\ldots,8\) are
  \(6v+4,2v+2,14v+9,10v+9,6v+7\), and its other endpoint satisfies
  \[
  2M_{t-1}=2e\varepsilon+6ev+5e-4\varepsilon^2
  -8\varepsilon v-15\varepsilon+12v^2-5v-12>0;
  \]
- singleton margins increase with \(j\), and four times the first one is
  \[
  -3e^2+14e\varepsilon-6ev+16e+5\varepsilon^2
  +46\varepsilon v+9v^2+44v-4>0;
  \]
- the two doubleton margins, multiplied by four, are
  \[
  25v^2+(10e+2)v+e^2-2e+9,\qquad
  25v^2+(10e+38)v+e^2+10e+1;
  \]
- the closing middle label \(L\) has margin
  \[
  2v^2+(5-e)v+1+\varepsilon(1-e-2v)>0.
  \]

For a three-edge path, the presence of an internal high label gives the
lower bound
\[
HL+n(H+L-n)
=6v^2+(27-5e+7\varepsilon)v-e^2+e\varepsilon+5e-2>0;
\tag{K825-16}
\]
the expression increases for \(v\ge e\), and its value at \(v=e\) is
\(2(4e\varepsilon+16e-1)\). Only the doubleton window and the closing
window can have two internal non-high labels. Their exact margins are
\[
{17v^2+(2e+36)v-e^2+12e-3\over2}>0
\]
and
\[
9v^2+(15-4e+7\varepsilon)v-e^2+e\varepsilon+3e>0,
\]
respectively.

For \(q=4\), distinct endpoints and the lower bound \(L\) on internal
labels give the uniform margin
\[
3v^2+(27-6e)v-e^2+5e-3.
\tag{K825-17}
\]
It is positive for \(v\ge e\), except at \((e,v)=(8,8)\), or \(n=47\).
At that one row direct block substitution gives minimum four-edge margin
\(1446\) over all endpoint types, minimum nontrivial compressed-path margin
\(55\), and minimum hole gain \(96\). For every \(q\ge5\), it is enough to use
\[
2Ln+3L^2-n^2=(e+7v)(v+4-e)>0.
\tag{K825-18}
\]
This completes the all-\(v\ge e\) shortcut hypothesis without enumerating a
subset.

The omitted \(r=0\) rows have the following exact finite certificates. The
last two columns are the minimum nontrivial compressed-path margin and the
minimum hole gain. They are obtained by direct integer substitution in the
fixed block word, not by subset maximization.

| \(n\) | \(K(\tau_n)\) | min path margin | min hole gain |
|---:|---:|---:|---:|
| 13 | 724 | 4 | 40 |
| 18 | 1851 | 13 | 54 |
| 19 | 2186 | 8 | 74 |
| 24 | 4309 | 10 | 92 |
| 25 | 4898 | 16 | 10 |
| 30 | 8333 | 31 | 12 |
| 31 | 9248 | 25 | 38 |
| 36 | 14311 | 43 | 44 |
| 37 | 15608 | 36 | 76 |
| 42 | 22613 | 49 | 86 |

Together with the \(n=47\) substitution, these positive margins complete the
backbone proof on the symbolic domain.

### Exact score evaluation

For a nonempty path \(P=(p_1,\ldots,p_s)\), write
\[
\mathcal C(x,P,y)=xp_1+\sum_{i=1}^{s-1}p_ip_{i+1}+p_sy.
\]
Before the optional deletion of \(c_0\), the tail score is exactly
\[
Ld+\sum_{j=0}^{v-2}\mathcal C(E_j,P_j,E_{j+1})
 +\mathcal C(E_{v-1},P_{v-1},L).
\tag{K825-19}
\]
For example, a triple summand is
\[
2(e^2+10ev+e-4j^2-4jv-8j+24v^2+v-4).
\]
Splitting (K825-19) into triple, optional-doubleton, and singleton ranges and
using the standard sums of \(j\) and \(j^2\) gives
\(\mathcal Q(v,e,\varepsilon)-(4e-7)\chi\). Deleting \(c_0\) changes the
score by (K825-14), so choosing the positive part of that change gives
(K825-4). This derives the formula directly from the blocks and also proves
its integrality.

### The fourteen explicit orders

The public construction uses the fourteen fixed rows in (UC21) where the
symbolic inequality \(v\ge e-2\) fails. For each row, the unique maximizing
subset is a tail \(\{m,\ldots,n\}\). The same shortcut-budget lemma is
certified by the two positive local margins shown here.

| \(n\) | \(m\) | \(K(\tau_n)\) | min path margin | min hole gain |
|---:|---:|---:|---:|---:|
| 9 | 4 | 256 | 8 | 15 |
| 10 | 4 | 346 | 1 | 26 |
| 11 | 5 | 459 | 17 | 8 |
| 12 | 5 | 593 | 10 | 19 |
| 14 | 6 | 917 | 18 | 20 |
| 15 | 6 | 1125 | 8 | 35 |
| 16 | 7 | 1346 | 28 | 9 |
| 17 | 7 | 1609 | 9 | 18 |
| 20 | 9 | 2554 | 57 | 13 |
| 21 | 9 | 2976 | 45 | 14 |
| 22 | 9 | 3431 | 21 | 20 |
| 26 | 10 | 5516 | 1 | 95 |
| 27 | 11 | 6204 | 37 | 30 |
| 32 | 13 | 10299 | 13 | 18 |

These are finite exact certificates for already displayed fixed orders, not
an enumeration of their subsets or of alternative permutations. Thus
(K825-2)--(K825-4), together with this table, determine \(K(\tau_n)\) for
every \(n\ge9\).

### Asymptotic and geometric consequences

Since \(e\) is bounded and \(v=(n-e+1)/5\), (K825-4) gives the rigorous
asymptotic theorem
\[
\boxed{
K(\tau_n)={143\over4}v^3+O(v^2)
          ={143\over500}n^3+O(n^2).
}
\tag{K825-20}
\]
In particular,
\[
{143\over500}<{8\over25},\qquad
{8\over25}-{143\over500}={17\over500}.
\tag{K825-21}
\]
The regular-direction pair score of this core still has coefficient \(8/25\);
the improvement comes from optimizing the induced-subset shortcut objective
\(K\), hence from the variable-spacing angular construction.

Insert label \(1\) into any gap \(g\) of \(\tau_n\), and call the resulting
complete order \(\sigma_{n,g}\). Exact label-one elimination and (CR22) give
\[
\Lambda(\sigma_{n,g})=K(\tau_n),\qquad
{K(\tau_n)\over\pi}-n^2
<\rho_{\sigma_{n,g}}<{K(\tau_n)\over\pi}.
\tag{K825-22}
\]
Consequently every such insertion family satisfies
\[
{\rho_{\sigma_{n,g}}\over n^3}\longrightarrow{143\over500\pi}.
\tag{K825-23}
\]
At the global level only the one-sided substitution is valid:
\[
\boxed{
\Lambda_n\le K(\tau_n),\qquad
R_2^*(n)<{\Lambda_n\over\pi}\le{K(\tau_n)\over\pi}.
}
\tag{K825-24}
\]
In particular, \(K(\tau_n)/\pi-n^2<R_2^*(n)\) is **not** inferred. Combining
the new upper coefficient with the current all-fixed-prefix lower coefficient
\(C_{\rm AF}=(434+4\sqrt2)/1587\) yields
\[
\boxed{
C_{\rm AF}
\le\liminf_{n\to\infty}{\Lambda_n\over n^3}
\le\limsup_{n\to\infty}{\Lambda_n\over n^3}
\le{143\over500}.
}
\tag{K825-25}
\]
\[
\boxed{
{C_{\rm AF}\over\pi}
\le\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\le\limsup_{n\to\infty}{R_2^*(n)\over n^3}
\le{143\over500\pi}.
}
\tag{K825-26}
\]
The remaining coefficient gap is
\((9941-2000\sqrt2)/793500>0\). No convergence, exact global leading
constant, equality \(\Lambda_n=K(\tau_n)\), or minimizing-order
classification follows.

## 9. Exact \(K\) For The Exact-Threshold Residue-One Core Order

Let \(\tau_n^{(1)}\) be the cyclic core order returned by
`residue_one_product_distance_order(n)`. Retain the block notation from
(R1C1)--(R1C9):
\[
n=5k+1,\qquad k\ge2,\qquad
D=4k+2,\qquad L=2k+1={D\over2},
\]
\[
t=\left\lfloor{k\over2}\right\rfloor,
\qquad \varepsilon=k-2t\in\{0,1\},
\]
\[
E_j=D+j,\qquad
\lambda_j=2k-2j,\qquad
\rho_j=2k+1-2j,
\]
and
\[
\tau_n^{(1)}
=\bigoplus_{j=0}^{k-1}(E_j,\lambda_j,P_j,\rho_{j+1}),
\tag{KR1-1}
\]
where the subscript on \(\rho\) is cyclic and the paths \(P_j\) are those
in (R1C5)--(R1C8).

### Exact theorem and all maximizing subsets

The unique maximizing subset is
\[
\boxed{
S_k=\{L,L+1,\ldots,n\}=\{2k+1,\ldots,5k+1\}.
}
\tag{KR1-2}
\]
It has cardinality \(3k+1\). The exact value is
\[
\boxed{
K(\tau_n^{(1)})
={857k^3+891k^2+214k
 +\varepsilon(27k^2-51k-18)\over24}.
}
\tag{KR1-3}
\]
Equivalently, as a period-ten quasipolynomial in \(n\),
\[
\boxed{
K(\tau_n^{(1)})=
\begin{cases}
\dfrac{857n^3+1884n^2-989n-1752}{3000},
 &n\equiv1\pmod {10},\\[6pt]
\dfrac{857n^3+2019n^2-2534n-2592}{3000},
 &n\equiv6\pmod {10}.
\end{cases}}
\tag{KR1-4}
\]
Parity changes the lower-order coefficients but not the maximizing subset.
There are no ties or exceptional argmaxes.

### Positive isolated-hole gains

Apply the shortcut-budget lemma (K825-6)--(K825-9) with
\[
H_k=\{2,\ldots,2k\},\qquad V\setminus H_k=S_k.
\tag{KR1-5}
\]
The set \(H_k\) has \(2k-1\) labels: the closing label
\(\rho_0=L\) is retained. Every member of \(H_k\) is isolated in the
block word. After deleting them, the compressed backbone is
\[
(L,E_0,P_0,E_1,P_1,\ldots,E_{k-1},P_{k-1})
\tag{KR1-6}
\]
cyclically.

For a left hole \(\lambda_j\), let \(F_j\) be the first label of \(P_j\);
for a right hole \(\rho_{j+1}\), let \(G_j\) be its last label. The deletion
gains are
\[
h_j^{\rm L}=E_jF_j-\lambda_j(E_j+F_j),
\qquad
h_j^{\rm R}=G_jE_{j+1}-\rho_{j+1}(G_j+E_{j+1}).
\tag{KR1-7}
\]
The right gain is needed only for \(0\le j\le k-2\), because the last
right label is the retained \(\rho_0=L\). Around \(P_0\),
\[
h_0^{\rm L}=6k+2,
\qquad
h_0^{\rm R}=16k+7.
\tag{KR1-8}
\]
For a triple path, \(1\le j\le t\), direct substitution gives
\[
\begin{aligned}
h_j^{\rm L}&=8k+4+(14k+6)j-4j^2,\\
h_j^{\rm R}&=16k+7+(14k+2)j-4j^2.
\end{aligned}
\tag{KR1-9}
\]
Both are positive because \(j\le k/2\); again only actual right holes are
included.

For a residual singleton path, its label is at least \((5k+4)/2\), each
adjacent hole is at most \(k-1\), and that hole's other neighbor is a terminal
label between \(D\) and \(n\). Hence each actual hole gain is at least
\[
{D(5k+4)\over2}-2n(k-1)=21k+6>0.
\tag{KR1-10}
\]
If \(k=2t+1\), the final doubleton has only the left hole
\(\lambda_{k-1}=2\), whose gain is
\[
2(5t+1)(5t+4)=50t^2+50t+8>0.
\tag{KR1-11}
\]
Thus every actual hole gain is positive; in fact the minimum is the value
\(6k+2\) in (KR1-8).

### Strict compressed-path margins

Consider any oriented arc and delete only its internal holes. Let the
resulting compressed path have endpoints \(a,b\) and \(q\ge2\) edges. Every
internal backbone label is at least \(L\). If \(q=2\) and an endpoint, say
\(a\), is a hole, then its internal label \(x\) satisfies \(x\ge L>a\), so
\[
ax+xb-ab=ax+b(x-a)>0.
\tag{KR1-12}
\]
Suppose instead that both endpoints are in the backbone. A middle label
strictly larger than \(n/2\) gives a positive two-edge margin immediately
from \(ab/(a+b)\le n/2\). The only remaining middle roles are a triple
connector \(c_j=L+j\) and the closing label \(L\). For
\(A_j=D-2j\), \(B_j=D-2j-1\),
\[
c_j(A_j+B_j)-A_jB_j
=8j(2k-j)+2k+5j+1>0.
\tag{KR1-13}
\]
If \(z\) is the last label of \(P_{k-1}\), then
\[
L(z+D)-zD=L(D-z)>0,
\tag{KR1-14}
\]
where \(z=5t+2\) for \(k=2t\) and \(z=5t+4\) for
\(k=2t+1\).

Every adjacent pair of backbone labels contains one label at least
\[
M={n+1\over2}
\tag{KR1-15}
\]
and one label at least \(L\). This follows directly from the path roles:
the only backbone labels not strictly above \(n/2\) are \(L\) and the
triple connectors. Each connector is flanked by outer labels; \(L\) is
adjacent to \(E_0\) and to \(z\ge M\). Therefore a
three-edge path has margin at least, up to reversing the path,
\[
Ma+ML+Lb-ab.
\]
This is bilinear in \((a,b)\); checking the four corners of
\([2,n]^2\) gives
\[
Ma+ML+Lb-ab\ge{5k^2+18k+4\over2}>0.
\tag{KR1-16}
\]

For \(q\ge4\), the internal-label bound gives
\[
\begin{aligned}
\sum_{xy\in E(C)}xy-ab
&\ge L(a+b)+(q-2)L^2-ab\\
&\ge2Ln+2L^2-n^2+(q-4)L^2\\
&=3(k^2+4k+1)+(q-4)L^2>0.
\end{aligned}
\tag{KR1-17}
\]
The second line is again the four-corner minimum. Equations
(KR1-12)--(KR1-17) prove the strict non-atomic shortcut condition for every
oriented arc, including arcs whose endpoints are holes.

All hypotheses of the shortcut-budget lemma now hold. Equality forces every
hole to be omitted and every backbone label to be selected, so (KR1-2) is
the unique maximizer among subsets of cardinality at least two. It also
dominates the subset \(\{n-1,n\}\), whose score is \(2n(n-1)>n^2\), so no
singleton can tie. This proves the complete argmax classification without
enumerating a subset.

### Direct block sum and boundary cases

For a nonempty path \(P=(p_1,\ldots,p_s)\), retain
\[
\mathcal C(x,P,y)=xp_1+
\sum_{i=1}^{s-1}p_ip_{i+1}+p_sy.
\]
When \(k=2t\ge4\), the backbone score is the sum of \(LD\), the \(P_0\)
term, the triple terms for \(1\le j\le t\), the nonfinal singleton terms for
\(t+1\le j\le2t-2\), and the final singleton term. Direct expansion gives
\[
\begin{array}{rcl}
LD&=&32t^2+16t+2,\\
\mathcal C(E_0,P_0,E_1)&=&128t^2+56t+5,\\
T_j&=&192t^2+92t+10-(16t+8)j-8j^2,\\
Q_j&=&112t^2+51t+5-(2t+3)j-2j^2,\\
F_{\rm even}&=&70t^2+38t+4.
\end{array}
\tag{KR1-18}
\]
Using the standard sums of \(j\) and \(j^2\),
\[
K(\tau_n^{(1)})
={1714t^3+891t^2+107t\over6}
\qquad(k=2t).
\tag{KR1-19}
\]
At \(k=2\), the residual-singleton range is empty and the final path is a
triple rather than the generic final singleton. The direct decomposition is
\[
LD+\mathcal C(E_0,P_0,E_1)+\mathcal C(E_1,P_1,L)
=50+189+213=452,
\tag{KR1-20}
\]
which agrees with (KR1-19).

When \(k=2t+1\), the corresponding terms are
\[
\begin{array}{rcl}
LD&=&32t^2+48t+18,\\
\mathcal C(E_0,P_0,E_1)&=&128t^2+184t+65,\\
T_j&=&192t^2+284t+104-(16t+16)j-8j^2,\\
Q_j&=&112t^2+171t+65-(2t+3)j-2j^2,\\
F_{\rm odd}&=&95t^2+156t+62,
\end{array}
\tag{KR1-21}
\]
with \(1\le j\le t\) in the triple sum and
\(t+1\le j\le2t-1\) in the singleton sum. Thus
\[
K(\tau_n^{(1)})
={1714t^3+3489t^2+2285t+480\over6}
\qquad(k=2t+1).
\tag{KR1-22}
\]
For \(k=3\), the singleton range is empty; (KR1-22) gives \(1328\)
directly. The connector \(c_t\) is exactly \(n/2\) in every odd row, so its
strict margin comes from (KR1-13), not from the automatic
middle-label argument. These are the only boundary/parity qualifications;
neither changes the unique argmax, and there is no boundary correction in
(KR1-3).

### Pointwise and asymptotic comparison with (K825-4)

Write \(K_{\rm R1}(n)=K(\tau_n^{(1)})\), and use
\(K_{\rm R1}(k)=K_{\rm R1}(5k+1)\) when \(k\) is the row parameter. Let
\(K_{825}(k)\) be the score of `eight_twenty_fifths_order(5k+1)`. On the
symbolic K825 domain, \(k\ge6\), the parameters specialize to
\[
e=7,\qquad v=k-1,\qquad
\varepsilon=k\bmod2,\qquad
\Gamma=6k+2,
\qquad \chi=\mathbf1_{\{k=6\}}.
\]
Consequently (K825-4) becomes
\[
K_{825}(k)
={858k^3+(933+30\varepsilon)k^2
 +(570-276\varepsilon)k+120-195\varepsilon\over24}
-21\mathbf1_{\{k=6\}},
\tag{KR1-23}
\]
and exact subtraction gives
\[
\boxed{
K_{825}(k)-K_{\rm R1}(k)
={k^3+(42+3\varepsilon)k^2
 +(356-225\varepsilon)k+120-177\varepsilon\over24}
-21\mathbf1_{\{k=6\}}.
}
\tag{KR1-24}
\]
At \(k=6\) the difference is \(145\). For even \(k\ge8\), every term in
the relevant numerator is positive; for odd \(k\ge7\), it is
\((k^3+45k^2+131k-57)/24>0\). The four earlier canonical orders are
explicit rather than symbolic:

| \(k\) | \(n\) | \(K_{\rm R1}\) | \(K_{825}\) | \(K_{825}-K_{\rm R1}\) |
|---:|---:|---:|---:|---:|
| 2 | 11 | 452 | 459 | 7 |
| 3 | 16 | 1328 | 1346 | 18 |
| 4 | 21 | 2915 | 2976 | 61 |
| 5 | 26 | 5453 | 5516 | 63 |
| 6 | 31 | 9103 | 9248 | 145 |
| 7 | 36 | 14169 | 14311 | 142 |

Thus the exact-threshold residue-one order is strictly better on every
admissible row \(k\ge2\); there is no crossover. The gap need not be
monotone across the two parity branches.

For the generic symbolic rows, the two K825 branches in terms of \(n\) are
\[
K_{825}(n)=
\begin{cases}
\dfrac{286n^3+697n^2+2498n+1519}{1000},
 &n\equiv1\pmod {10},\\[6pt]
\dfrac{286n^3+747n^2+98n-4256}{1000},
 &n\equiv6\pmod {10},
\end{cases}
\tag{KR1-25}
\]
with an additional subtraction of \(21\) at the boundary \(n=31\). Hence
the cubic coefficients and their exact difference are
\[
{857\over3000}
< {143\over500}={858\over3000},
\qquad
{143\over500}-{857\over3000}={1\over3000}.
\tag{KR1-26}
\]
The quadratic coefficients improve from \(697/1000\) to \(157/250\) on
\(n\equiv1\pmod {10}\), and from \(747/1000\) to \(673/1000\) on
\(n\equiv6\pmod {10}\). More precisely, on the generic rows,
\[
K_{825}(n)-K_{\rm R1}(n)=
\begin{cases}
\dfrac{n^3+207n^2+8483n+6309}{3000},
 &n\equiv1\pmod {10},\\[6pt]
\dfrac{n^3+222n^2+2828n-10176}{3000},
 &n\equiv6\pmod {10},
\end{cases}
\tag{KR1-27}
\]
again subtracting \(21\) from the first branch at \(n=31\). In particular,
\[
K_{\rm R1}(n)={857\over3000}n^3+O(n^2),
\qquad
K_{825}(n)-K_{\rm R1}(n)={n^3\over3000}+O(n^2).
\tag{KR1-28}
\]

### Permitted cyclic-ratio and geometric consequences

Insert label \(1\) in any gap \(g\) of \(\tau_n^{(1)}\), and call the
complete order \(\sigma_{n,g}^{(1)}\). Exact label-one elimination and the
fixed-order sandwich give exactly
\[
\boxed{
\Lambda(\sigma_{n,g}^{(1)})=K_{\rm R1}(n),
\qquad
{K_{\rm R1}(n)\over\pi}-n^2
<\rho_{\sigma_{n,g}^{(1)}}
<{K_{\rm R1}(n)\over\pi}.
}
\tag{KR1-29}
\]
Therefore every choice of insertion gaps along this family satisfies
\[
{\rho_{\sigma_{n,g}^{(1)}}\over n^3}
\longrightarrow {857\over3000\pi}
\qquad(n=5k+1\to\infty).
\tag{KR1-30}
\]
At the global level only the one-sided substitution is valid:
\[
\boxed{
\Lambda_n\le K_{\rm R1}(n),
\qquad
R_2^*(n)<{\Lambda_n\over\pi}
\le{K_{\rm R1}(n)\over\pi}
\qquad(n=5k+1,\ k\ge2).
}
\tag{KR1-31}
\]
Consequently,
\[
\limsup_{k\to\infty}{\Lambda_{5k+1}\over(5k+1)^3}
\le{857\over3000},
\qquad
\limsup_{k\to\infty}{R_2^*(5k+1)\over(5k+1)^3}
\le{857\over3000\pi}.
\tag{KR1-32}
\]

No equality \(\Lambda_n=K_{\rm R1}(n)\), global lower bound
\(K_{\rm R1}(n)/\pi-n^2<R_2^*(n)\), or global minimizing-order
classification follows. The strict inequality
\(K_{\rm R1}<K_{825}\) compares the exact \(\Lambda\) scores of the two
constructed complete-order families after label-one insertion, but does not
order their exact angular thresholds \(\rho\). The fixed-order sandwich has
width \(n^2\), so the quadratic terms of (KR1-4) are not exact geometric
coefficients. Finally, a strict improvement in only one residue class does
not improve the existing all-\(n\) limsup coefficient \(143/500\); it gives
only (KR1-32).

## 10. Exact \(K\) For The Exact-Threshold Residue-Two Core Order

Let \(\tau_n^{(2)}\) be the cyclic core order returned by
`residue_two_product_distance_order(n)`. Retain the block notation from
(R2C1)--(R2C8):
\[
n=5k+2,\qquad k\ge2,\qquad
D=4k+3,\qquad L=2k+1,
\]
\[
\varepsilon=k\bmod2,\qquad
t=\left\lceil{k\over2}\right\rceil={k+\varepsilon\over2},
\qquad E_j=D+j,
\]
\[
\lambda_j=2k-2j,\qquad \rho_j=2k+1-2j,
\qquad
\tau_n^{(2)}
=\bigoplus_{j=0}^{k-1}(E_j,\lambda_j,P_j,\rho_{j+1}),
\tag{KR2-1}
\]
where the subscript on \(\rho\) is cyclic. The first \(t\) paths are
\[
P_j=(A_j,c_j,B_j)
=(D-1-2j,\ 2k+2+j,\ D-2-2j),
\qquad 0\le j<t,
\]
and the residual paths are the parity branches (R2C5)--(R2C6).

### Exact theorem and all maximizing subsets

For every \(k\ge2\), the unique maximizing subset is
\[
\boxed{
S_k=\{L,L+1,\ldots,n\}=\{2k+1,\ldots,5k+2\}.
}
\tag{KR2-2}
\]
It has cardinality \(3k+2\). The exact value is
\[
\boxed{
K_{\rm R2}(k):=K(\tau_n^{(2)})
={286k^3+459k^2+198k+16
 +\varepsilon(-10k^2+40k+27)\over8}.
}
\tag{KR2-3}
\]
Equivalently,
\[
\boxed{
K_{\rm R2}(n)=
\begin{cases}
\dfrac{286n^3+579n^2-798n-1008}{1000},
 &n\equiv2\pmod {10},\\[6pt]
\dfrac{286n^3+529n^2+402n+167}{1000},
 &n\equiv7\pmod {10}.
\end{cases}}
\tag{KR2-4}
\]
Parity changes only the lower-order terms and the internal path types. There
are no parity-dependent ties or exceptional maximizing subsets.

### Positive isolated-hole gains

Apply the shortcut-budget lemma (K825-6)--(K825-9) with
\[
H_k=\{2,\ldots,2k\},\qquad V\setminus H_k=S_k.
\tag{KR2-5}
\]
Every member of \(H_k\) is isolated in (KR2-1). The closing label
\(\rho_0=L\) is retained, and deleting all holes gives the cyclic backbone
\[
(L,E_0,P_0,E_1,P_1,\ldots,E_{k-1},P_{k-1}).
\tag{KR2-6}
\]
If \(F_j\) and \(G_j\) are the first and last labels of \(P_j\), the
actual left and right deletion gains are
\[
h_j^{\rm L}=E_jF_j-\lambda_j(E_j+F_j),\qquad
h_j^{\rm R}=G_jE_{j+1}-\rho_{j+1}(G_j+E_{j+1}).
\tag{KR2-7}
\]
The right gain is required only for \(j\le k-2\), since the last right
label is the retained \(\rho_0\).

On a triple path, \(0\le j<t\), direct substitution gives
\[
\begin{aligned}
h_j^{\rm L}&=10k+6+(14k+6)j-4j^2,\\
h_j^{\rm R}&=18k+9+(14k+2)j-4j^2.
\end{aligned}
\tag{KR2-8}
\]
The left sequence is strictly increasing on its range, and
\(h_j^{\rm R}-h_j^{\rm L}=8k+3-4j>0\). Thus every actual triple-hole
gain is at least \(10k+6\).

If \(k=2m+1\), then \(t=m+1\) and the residual singleton at index
\(m+1\le j\le2m\) is \(P_j=(2k+j+2)\). Its gains are
\[
\begin{aligned}
h_j^{\rm L}
 &=5j^2+(14k+15)j-4k^2+4k+6,\\
h_j^{\rm R}
 &=5j^2+(14k+20)j-4k^2+10k+14.
\end{aligned}
\tag{KR2-9}
\]
Here the right formula is an actual hole gain only for \(j\le2m-1\); at
\(j=2m\), the right label is the retained \(\rho_0=L\).
The left expression increases with \(j\), the right exceeds it by
\(5j+6k+8\), and at the first residual index
\[
h_{m+1}^{\rm L}=17m^2+59m+40>0.
\tag{KR2-10}
\]

If \(k=2m\), then \(P_m=(5m+2,5m+3)\). The two possible gains there are
\[
h_m^{\rm L}=(m+1)(17m+6),\qquad
h_m^{\rm R}=17m^2+47m+19,
\tag{KR2-11}
\]
where the right hole exists only when \(m\ge2\) and its gain exceeds the
left one by \(24m+13\). For the residual
singletons \(P_j=(2k+j+3)\), \(m+1\le j\le2m-1\),
\[
\begin{aligned}
h_j^{\rm L}
 &=5j^2+(14k+18)j-4k^2+6k+9,\\
h_j^{\rm R}
 &=5j^2+(14k+23)j-4k^2+12k+19,
\end{aligned}
\qquad
h_{m+1}^{\rm L}=17m^2+68m+32.
\tag{KR2-12}
\]
The right formula is required only for \(j\le2m-2\); the final singleton
again ends at the retained \(\rho_0=L\).
Again the left gains increase, and the right exceeds the left by
\(5j+6k+10\). These formulas include every actual hole and prove
the claimed exact minimum: after subtracting \(10k+6\), the first odd
residual gain leaves \(17m^2+39m+24\), the even-doubleton left gain leaves
\(17m^2+3m\), and the first even-singleton gain leaves
\(17m^2+48m+26\), all positive on their stated ranges. Hence
\[
\boxed{
\min_{x\in H_k}h_x=10k+6>0,
}
\tag{KR2-13}
\]
with equality at \(\lambda_0\).

### Strict compressed-path margins

Take an arbitrary oriented arc, delete only its internal holes, and let its
compressed path have endpoints \(a,b\) and \(q\ge2\) edges. If \(q=2\)
and, say, \(a\) is a hole, the middle label \(x\) lies in the backbone and
\(x\ge L>a\), so
\[
ax+xb-ab=ax+b(x-a)>0.
\tag{KR2-14}
\]
Suppose both endpoints are in the backbone. A middle label greater than
\(n/2\) gives a positive margin because \(ab/(a+b)\le n/2\). The only
remaining middle roles are a triple connector \(c_j\) and the closing label
\(L\). Their exact margins are
\[
c_j(A_j+B_j)-A_jB_j
=10k+4+(16k+1)j-8j^2
=8j(2k-j)+10k+j+4>0
\tag{KR2-15}
\]
and, with \(z=\operatorname{last}(P_{k-1})\),
\[
L(z+D)-zD=
\begin{cases}
2k^2-1,&k\text{ even},\\
2k^2+2k+1,&k\text{ odd}.
\end{cases}
\tag{KR2-16}
\]
In particular, the even connector that can equal \(n/2\) is covered by
(KR2-15), while the smallest closing margin is \(7\) at \(k=2\).

Put
\[
M=\left\lfloor{n\over2}\right\rfloor+1
 ={5k+4-\varepsilon\over2}.
\tag{KR2-17}
\]
Every compressed-backbone edge has one endpoint at least \(M\) and the
other at least \(L\). Indeed, terminal and outer-triple labels provide the
high endpoint around each connector, all residual-path labels are at least
\(M\), and the two edges at \(L\) have high endpoints \(z,D\). Therefore,
up to reversing a three-edge path, its margin is at least
\[
Ma+ML+Lb-ab
\ge {5k^2+21k+8-\varepsilon(7k+3)\over2}>0.
\tag{KR2-18}
\]
The second inequality is the minimum over the four corners of
\([2,n]^2\), attained by the lower-bound expression at \(a=b=n\).

For \(q\ge4\), every internal label is at least \(L\), so another
four-corner check gives
\[
\begin{aligned}
\sum_{xy\in E(C)}xy-ab
&\ge L(a+b)+(q-2)L^2-ab\\
&\ge3k^2+6k+2+(q-4)L^2>0.
\end{aligned}
\tag{KR2-19}
\]
Equations (KR2-14)--(KR2-19) cover every oriented arc, including arcs with
hole endpoints. Together with (KR2-13), they establish both strict
hypotheses of the shortcut-budget lemma. Equality therefore forces every
hole to be omitted and every backbone label to be selected. Hence (KR2-2)
is the unique maximizer among subsets of cardinality at least two. It
dominates the two-element subset \(\{n-1,n\}\), whose score is
\(2n(n-1)>n^2\), so no singleton ties it. This completes the all-subset
argument without enumerating a subset or a cyclic order.

### Direct block sum, parity, and boundary rows

For a nonempty path \(P=(p_1,\ldots,p_s)\), write
\[
\mathcal C(x,P,y)=xp_1+
\sum_{i=1}^{s-1}p_ip_{i+1}+p_sy.
\]
The backbone score obtained directly from (KR2-6) is
\[
LD+\sum_{j=0}^{k-2}\mathcal C(E_j,P_j,E_{j+1})
 +\mathcal C(E_{k-1},P_{k-1},L).
\tag{KR2-20}
\]

Let first \(k=2m\) with \(m\ge2\). The closure, triple, doubleton,
nonfinal-singleton, and final-singleton terms are respectively
\[
\begin{array}{rcl}
LD&=&32m^2+20m+3,\\
T_j&=&192m^2+124m+16-(16m+16)j-8j^2,
       \quad0\le j\le m-1,\\
Q_{\rm d}&=&115m^2+105m+24,\\
Q_j&=&64m^2+76m+21+(24m+13)j+2j^2,
       \quad m+1\le j\le2m-2,\\
F_{\rm even}&=&84m^2+46m+6.
\end{array}
\tag{KR2-21}
\]
The standard sums of \(j\) and \(j^2\) give
\[
K_{\rm R2}(2m)
={572m^3+459m^2+99m+4\over2}.
\tag{KR2-22}
\]
At the smallest even row, \(k=2\), the doubleton is final and both
singleton ranges are empty. Directly,
\[
LD+T_0+F_{\rm double}=55+332+180=567,
\tag{KR2-23}
\]
which agrees with (KR2-22). At \(k=4\), the nonfinal-singleton range in
(KR2-21) is empty, but the displayed sum remains valid.

For \(k=2m+1\), \(m\ge1\), the corresponding terms are
\[
\begin{array}{rcl}
LD&=&32m^2+52m+21,\\
T_j&=&192m^2+316m+126-(16m+24)j-8j^2,
       \quad0\le j\le m,\\
Q_j&=&64m^2+124m+60+(24m+23)j+2j^2,
       \quad m+1\le j\le2m-1,\\
F_{\rm odd}&=&84m^2+116m+40.
\end{array}
\tag{KR2-24}
\]
Thus
\[
K_{\rm R2}(2m+1)
={572m^3+1307m^2+997m+254\over2}.
\tag{KR2-25}
\]
At \(k=3\), the nonfinal-singleton range is empty and the four remaining
parts give \(1565\). Equations (KR2-22)--(KR2-25) are exactly the two
branches of (KR2-3), including all smallest parity and path-range
boundaries; there is no score correction.

### Pointwise and asymptotic comparison with K825

Let \(K_{825}(k)\) denote the score of
`eight_twenty_fifths_order(5k+2)`. On its symbolic domain \(k\ge7\), the
parameters in (K825-1)--(K825-4) specialize to
\[
e=8,\qquad v=k-1,\qquad
\varepsilon_{825}=1-\varepsilon,\qquad
\Gamma=10k+6,\qquad
\chi=\mathbf1_{\{k=7\}}.
\tag{KR2-26}
\]
Consequently,
\[
K_{825}(k)
={286k^3+(501-10\varepsilon)k^2
 +(298+100\varepsilon)k+24+97\varepsilon\over8}
 -25\mathbf1_{\{k=7\}},
\tag{KR2-27}
\]
and exact subtraction gives
\[
\boxed{
K_{825}(k)-K_{\rm R2}(k)
={21k^2+(50+30\varepsilon)k+4+35\varepsilon\over4}
 -25\mathbf1_{\{k=7\}}.
}
\tag{KR2-28}
\]
The five earlier K825 orders are explicit, \(k=7\) is the symbolic boundary
correction, and \(k=8\) is the first uncorrected even symbolic-domain row:

| \(k\) | \(n\) | \(K_{\rm R2}\) | \(K_{825}\) | \(K_{825}-K_{\rm R2}\) |
|---:|---:|---:|---:|---:|
| 2 | 12 | 567 | 593 | 26 |
| 3 | 17 | 1565 | 1609 | 44 |
| 4 | 22 | 3307 | 3431 | 124 |
| 5 | 27 | 6026 | 6204 | 178 |
| 6 | 32 | 9938 | 10299 | 361 |
| 7 | 37 | 15226 | 15608 | 382 |
| 8 | 42 | 22176 | 22613 | 437 |

All displayed gaps are positive. For even \(k\ge8\), (KR2-28) is
\((21k^2+50k+4)/4>0\); for odd \(k\ge9\), it is
\((21k^2+80k+39)/4>0\). Thus
\[
\boxed{K_{\rm R2}(k)<K_{825}(k)\qquad(k\ge2),}
\tag{KR2-29}
\]
and there is no crossover.

On the symbolic-domain rows, the exact K825 branches in terms of \(n\) are
\[
K_{825}(n)=
\begin{cases}
\dfrac{286n^3+789n^2+862n-4168}{1000},
 &n\equiv2\pmod {10},\\[6pt]
\dfrac{286n^3+739n^2+3562n+2757}{1000},
 &n\equiv7\pmod {10},
\end{cases}
-25\mathbf1_{\{n=37\}}.
\tag{KR2-30}
\]
Together with (KR2-4), this gives the rowwise gaps
\[
K_{825}(n)-K_{\rm R2}(n)=
\begin{cases}
\dfrac{21n^2+166n-316}{100},
 &n\equiv2\pmod {10},\\[6pt]
\dfrac{21n^2+316n+259}{100},
 &n\equiv7\pmod {10},
\end{cases}
-25\mathbf1_{\{n=37\}}.
\tag{KR2-31}
\]
In particular, the new order improves the quadratic terms in both parity
rows but not the cubic coefficient:
\[
\boxed{
K_{\rm R2}(n)={143\over500}n^3+O(n^2),\qquad
K_{825}(n)-K_{\rm R2}(n)={21\over100}n^2+O(n).
}
\tag{KR2-32}
\]
Equivalently,
\(K_{\rm R2}(n)/K_{825}(n)
=1-105/(143n)+O(n^{-2})\) on this subsequence.

### Permitted cyclic-ratio and geometric consequences

Insert label \(1\) into any gap \(g\) of \(\tau_n^{(2)}\), and call the
complete order \(\sigma_{n,g}^{(2)}\). Exact label-one elimination and the
fixed-order sandwich give precisely
\[
\boxed{
\Lambda(\sigma_{n,g}^{(2)})=K_{\rm R2}(n),\qquad
{K_{\rm R2}(n)\over\pi}-n^2
<\rho_{\sigma_{n,g}^{(2)}}
<{K_{\rm R2}(n)\over\pi}.
}
\tag{KR2-33}
\]
Equations (CR12l) and (CR12q) also transfer the argmax classification:
no \(\Lambda\)-maximizing subset contains label \(1\), and every core-subset
score is unchanged by insertion. Thus \(S_k\) in (KR2-2) is the unique
label subset attaining \(\Lambda(\sigma_{n,g}^{(2)})\) for every gap \(g\).
Hence every sequence of insertion gaps along this family satisfies
\[
{\rho_{\sigma_{n,g}^{(2)}}\over n^3}
\longrightarrow{143\over500\pi}
\qquad(n=5k+2\to\infty).
\tag{KR2-34}
\]
At the global level only the one-sided substitution is licensed:
\[
\boxed{
\Lambda_n\le K_{\rm R2}(n),\qquad
R_2^*(n)<{\Lambda_n\over\pi}
\le{K_{\rm R2}(n)\over\pi}
\qquad(n=5k+2,\ k\ge2).
}
\tag{KR2-35}
\]
Consequently,
\[
\limsup_{k\to\infty}{\Lambda_{5k+2}\over(5k+2)^3}
\le{143\over500},\qquad
\limsup_{k\to\infty}{R_2^*(5k+2)\over(5k+2)^3}
\le{143\over500\pi}.
\tag{KR2-36}
\]

These deductions do not prove \(\Lambda_n=K_{\rm R2}(n)\), a global lower
bound \(K_{\rm R2}(n)/\pi-n^2<R_2^*(n)\), a minimizing-order
classification, or an identity between \(K\) and \(W\). The unique argmax
classification for \(K\) does transfer to the complete-order subset
objective as stated above, but it does not classify active geometric or STN
constraints at the exact angular threshold. The strict comparison (KR2-29)
orders the exact \(\Lambda\) scores of the two inserted construction
families. However, the rowwise formulas give
\(0<(K_{825}-K_{\rm R2})/\pi<n^2\), so the two fixed-order sandwiches
overlap and do not order the exact angular thresholds or identify an exact
quadratic geometric term. Finally, the coefficient in (KR2-36) is the
existing canonical coefficient, not an improved all-residue limsup or a
convergence theorem.

## 11. Exact \(K\) For The Closing PG46 Core Order

The extendibility construction (PG46) in
`research/PRODUCT_DISTANCE_SURROGATE.md` contains a distinguished closing
shift. On
\[
n=10m+3,\qquad m\ge3,\qquad d=8m+4,\qquad v=2m,
\]
retain the scaffold notation
\[
E_j=d+j,\qquad
\lambda_j=4m-2j,\qquad
\rho_j=4m+1-2j,
\tag{KPG46-1}
\]
and the paths
\[
P_k=(A_k,c_k,B_k)
=(d-1-2k,\ 4m+2+k,\ d-2-2k)
\quad(0\le k\le m),
\]
\[
P_k=(x_k)=(4m+2+k)
\quad(m+1\le k\le2m-1).
\tag{KPG46-2}
\]
Specialize (PG46) to the target edge \((m,2m-1)\):
\[
\alpha_m(j)=
\begin{cases}
j,&0\le j<m,\\
j+1,&m\le j<2m-1,\\
m,&j=2m-1.
\end{cases}
\tag{KPG46-3}
\]
Thus \(P_m\) occupies the closing gap \(G_{2m-1}\), while the singleton
paths shift one gap to the left. Let \(\tau_m^{\rm cl}=\sigma_{\alpha_m}\)
be the resulting cyclic core order. This section evaluates \(K\) on this one
order family. Relation-compatibility and full optimality for \(W\), already
proved by (PG46) and (PG62), are inputs; they do not determine \(K\).

### Exact statement and compressed backbone

Put
\[
L=4m+1,\qquad
S_m=\{L,L+1,\ldots,n\},\qquad
H_m=\{2,3,\ldots,4m\}.
\tag{KPG46-4}
\]
Every member of \(H_m\) is isolated between two members of \(S_m\). After
deleting these holes, the cyclic backbone is
\[
\begin{aligned}
(&L,E_0,P_0,E_1,P_1,\ldots,E_{m-1},P_{m-1},E_m,
 x_{m+1},E_{m+1},\ldots,\\
 &E_{2m-2},x_{2m-1},E_{2m-1},P_m).
\end{aligned}
\tag{KPG46-5}
\]
Here every displayed triple path is expanded in its retained orientation.
The exact result is
\[
\boxed{
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}
P_{\tau_m^{\rm cl}}(U)=\{S_m\},
}
\tag{KPG46-6}
\]
and
\[
\boxed{
K(\tau_m^{\rm cl})
={572m^3+631m^2+223m+22\over2}
}
\qquad(m\ge3).
\tag{KPG46-7}
\]
Thus every row has exactly one maximizing subset; there is no parity branch
or boundary correction.

### Positive hole gains

We apply the isolated-hole shortcut-budget lemma (K825-6)--(K825-9). If a
hole \(h\) lies between its two backbone neighbors \(a,b\), its deletion gain
is \(ab-h(a+b)\). Direct substitution in the five exhaustive position
ranges gives
\[
\begin{array}{c|c|c}
\text{hole position}&\text{range}&\text{deletion gain}\\ \hline
\lambda_j&0\le j\le m-1&
-4j^2+(28m+9)j+28m+12\\
\rho_{j+1}&0\le j\le m-1&
-4j^2+(28m+5)j+44m+17\\
\lambda_j&m\le j\le2m-2&
5j^2+(28m+21)j-16m^2+12m+12\\
\rho_{j+1}&m\le j\le2m-2&
5j^2+(28m+26)j-16m^2+24m+23\\
\lambda_{2m-1}=2&j=2m-1&60m^2+16m-3
\end{array}
\tag{KPG46-8}
\]
Each polynomial in a displayed interval is increasing there. Its left-end
value is, respectively,
\[
28m+12,\quad44m+17,\quad
17m^2+33m+12,\quad17m^2+50m+23,
\tag{KPG46-9}
\]
while the closing value is already positive. Hence
\[
\boxed{\min_{h\in H_m}\bigl(ab-h(a+b)\bigr)=28m+12>0.}
\tag{KPG46-10}
\]
The ranges in (KPG46-8) include the last unshifted triple, the first and last
shifted singletons, and the closing triple separately.

### Complete shortcut audit

Consider an oriented arc of \(\tau_m^{\rm cl}\), delete its internal holes,
and write the compressed path as
\((z_0,z_1,\ldots,z_q)\), with \(q\ge2\). Every internal label is at least
\(L\).

If an endpoint \(a\) is a hole, then \(a\le L-1\). The two boundary edges
alone give
\[
L(a+b)-ab\ge4L-4=16m>12m+4
\qquad(2\le a\le L-1,\ 2\le b\le n),
\tag{KPG46-11}
\]
because \(L(a+b)-ab=La+(L-a)b\): first allowing the smallest \(b=2\),
then the smallest \(a=2\), gives a valid lower bound on the whole rectangle.
Thus endpoint-hole arcs cannot attain the global compressed-path minimum, and
only arcs whose two endpoints lie in \(S_m\) remain.

For \(q=2\), a middle label \(y>n/2\) has
\(y(a+b)-ab>0\), since \(ab/(a+b)\le n/2\). The only backbone labels not
covered by this observation are
\[
L,\qquad c_j=4m+2+j\quad(0\le j\le m-1);
\]
the moved connector \(c_m=5m+2\) is already strictly above \(n/2\). Their
exact margins are
\[
\begin{aligned}
c_j(A_j+B_j)-A_jB_j
&=-8j^2+(32m+7)j+12m+4\ge12m+4,\\
L(B_m+E_0)-B_mE_0&=8m^2-2m-2>12m+4.
\end{aligned}
\tag{KPG46-12}
\]
It remains to compare the generic high-middle roles with the displayed
minimum. Since \(n\) is odd and the three labels of a two-edge path are
distinct, \(y\ge(n+1)/2=5m+2\). The identity
\[
y(a+b)-ab=y^2-(a-y)(b-y)
\]
splits the endpoint ranges exactly. If \(a,b>y\), then distinctness and
monotonicity give
\[
y^2-(a-y)(b-y)
\ge y^2-(n-y)(n-1-y)
\ge {3n-1\over2}=15m+4.
\]
If \(a,b<y\), the analogous lower corner \(L,L+1\) gives at least
\[
(2L+1){n+1\over2}-L(L+1)=24m^2+19m+4,
\]
and if the endpoints straddle \(y\), the margin is at least \(y^2\).
All three bounds exceed \(12m+4\). The first expression in (KPG46-12) is
increasing on \(0\le j\le m-1\), and the second displayed strict inequality
uses \(8m^2-14m-6>0\) for \(m\ge3\). This checks every two-edge role, including
both path-type joins and the cyclic closure, and proves that the exact
two-edge minimum is \(12m+4\) at \(c_0\).

For \(q=3\), every pair of consecutive internal backbone labels contains
one label at least
\[
R=6m+2.
\]
Indeed, the labels below \(R\) are \(L\), the connectors \(c_0,\ldots,c_m\),
and the shifted singletons; each is flanked in (KPG46-5) by a terminal or an
outer triple label at least \(R\). Therefore, for endpoints \(a,b\in S_m\),
orienting the two internal labels so the first is at least \(R\) gives
\[
aR+RL+Lb-ab
\ge RL
=24m^2+14m+2>12m+4.
\tag{KPG46-13}
\]
The reversed internal orientation is identical after exchanging \(a,b\).
For the displayed inequality, the bilinear remainder \(aR+Lb-ab\) is
nonnegative at all four corners of \([L,n]^2\), using \(R+L=n\).
For \(q\ge4\), discarding any excess above \(L\) gives
\[
\begin{aligned}
\sum_{i=0}^{q-1}z_i z_{i+1}-z_0z_q
&\ge L(a+b)+(q-2)L^2-ab\\
&\ge2Ln+2L^2-n^2
=12m^2-1>12m+4.
\end{aligned}
\tag{KPG46-14}
\]
The last bilinear expression attains its minimum on the corners of
\([L,n]^2\); allowing the potentially smallest corner \((n,n)\) gives the
displayed bound. The final strict inequality holds for every \(m\ge3\).

Equations (KPG46-10)--(KPG46-14) verify both hypotheses of the shortcut
lemma for every \(m\ge3\). Hence \(S_m\) is the unique maximizer among
subsets of cardinality at least two. It contains \(n-1,n\), so its score is
at least \(2n(n-1)>n^2\); no singleton can tie it. This proves
(KPG46-6), including every boundary range.
Together with (KPG46-11)--(KPG46-14), the role \(c_0\) proves the exact
global nontrivial compressed-path margin \(12m+4\).

### Exact block sum

For a nonempty path \(P=(p_1,\ldots,p_s)\), retain
\[
\mathcal C(x,P,y)=xp_1+\sum_{i=1}^{s-1}p_ip_{i+1}+p_sy.
\]
The backbone score is
\[
\begin{aligned}
P_{\tau_m^{\rm cl}}(S_m)={}&LE_0
+\sum_{j=0}^{m-1}\mathcal C(E_j,P_j,E_{j+1})\\
&+\sum_{j=m}^{2m-2}
  \bigl(E_jx_{j+1}+x_{j+1}E_{j+1}\bigr)
+\mathcal C(E_{2m-1},P_m,L).
\end{aligned}
\tag{KPG46-15}
\]
The two repeated block summands and the combined closing contribution are
\[
\begin{aligned}
\mathcal C(E_j,P_j,E_{j+1})
&=-8j^2-16mj-16j+192m^2+164m+32,\\
E_jx_{j+1}+x_{j+1}E_{j+1}
&=2j^2+24mj+15j+64m^2+84m+27,\\
LE_0+\mathcal C(E_{2m-1},P_m,L)
&=176m^2+135m+25.
\end{aligned}
\tag{KPG46-16}
\]
Summing \(j\), \(j^2\) on the exact ranges in (KPG46-15) gives
(KPG46-7) directly and proves its integrality.

### Minimum row and exact comparison with K825

At \(m=3\),
\[
\alpha_3=(0,1,2,4,5,3),
\]
and the expanded order is
\[
\begin{aligned}
(&28,12,27,14,26,11,29,10,25,15,24,9,30,8,23,16,22,7,\\
 &31,6,18,5,32,4,19,3,33,2,21,17,20,13).
\end{aligned}
\tag{KPG46-17}
\]
Its sole maximizing subset is \(\{13,\ldots,33\}\), its exact score is
\[
K(\tau_3^{\rm cl})=10907,
\]
and the minimum hole and nontrivial compressed-path margins are \(96\) and
\(40\). Thus the smallest admitted row is not an exceptional branch.

For the canonical K825 order on the same indices, (K825-1)--(K825-4)
specialize to
\[
e=4,\qquad v=2m,\qquad\varepsilon=0,qquad
\chi=0,\qquad\Gamma=-12m-4<0.
\]
Its unique maximizer is the same label set \(S_m\), and
\[
K_{825}(m)
={572m^3+629m^2+235m+30\over2}.
\tag{KPG46-18}
\]
Exact subtraction gives the pointwise comparison
\[
\boxed{
K(\tau_m^{\rm cl})-K_{825}(m)=m^2-6m-4.
}
\tag{KPG46-19}
\]
The crossover audit is complete:

| \(m\) | \(K(\tau_m^{\rm cl})\) | \(K_{825}(m)\) | PG46 minus K825 |
|---:|---:|---:|---:|
| 3 | 10907 | 10920 | -13 |
| 4 | 23809 | 23821 | -12 |
| 5 | 44206 | 44215 | -9 |
| 6 | 73814 | 73818 | -4 |
| 7 | 114349 | 114346 | 3 |

The difference in (KPG46-19) is strictly positive and increasing for every
integer \(m\ge7\). Its real roots are \(3\pm\sqrt{13}\), so no admitted
integer row is tied. Consequently the closing PG46 shift improves K825
exactly for \(m=3,4,5,6\), and is strictly worse for every \(m\ge7\).

In terms of \(n=10m+3\), the two exact formulas are
\[
K(\tau_m^{\rm cl})
={286n^3+581n^2-58n-1777\over1000},
\]
\[
K_{825}(n)
={286n^3+571n^2+602n+333\over1000},
\tag{KPG46-20}
\]
and their difference is
\[
{n^2-66n-211\over100}.
\]
Therefore
\[
\boxed{
K(\tau_m^{\rm cl})={143\over500}n^3+O(n^2),
\qquad
K(\tau_m^{\rm cl})-K_{825}(n)={1\over100}n^2+O(n).
}
\tag{KPG46-21}
\]
The closing PG46 family does not improve the coefficient \(143/500\); it is
eventually worse already at quadratic order. These are exact statements
about \(K\) on two explicit core-order families. They imply no geometric or
global optimality, no identity with \(W\), no angular-threshold ordering, and
no minimizing-order classification.

## 12. Exact \(K\) For The Preclosing PG46 Core Order

We now evaluate the other sharp interval-shift witness from (PG46). Retain
all notation (KPG46-1)--(KPG46-2) and specialize (PG46) to the target edge
\((m,2m-2)\):
\[
\alpha_m^{\rm pre}(j)=
\begin{cases}
j,&0\le j<m,\\
j+1,&m\le j<2m-2,\\
m,&j=2m-2,\\
2m-1,&j=2m-1.
\end{cases}
\tag{KPG46P-1}
\]
Thus \(P_m\) occupies \(G_{2m-2}\), while the terminal singleton
\(P_{2m-1}\) remains in the closing gap. Let
\(\tau_m^{\rm pre}=\sigma_{\alpha_m^{\rm pre}}\). Its relation-compatibility
and full optimality for \(W\) follow from (PG46) and (PG62); those prior facts
are inputs and do not evaluate \(K\).

### Exact statement and compressed backbone

Keep \(L=4m+1\), \(S_m=\{L,L+1,\ldots,n\}\), and
\(H_m=\{2,3,\ldots,4m\}\). Every member of \(H_m\) is isolated. Deleting
them gives the cyclic backbone
\[
\bigl(
L,E_0,P_0,E_1,P_1,\ldots,E_{m-1},P_{m-1},E_m,
\bigl(x_{j+1},E_{j+1}\bigr)_{j=m}^{2m-3},
P_m,E_{2m-1},x_{2m-1}
\bigr).
\tag{KPG46P-2}
\]
The indexed block is concatenated in increasing \(j\); its range is nonempty
because \(m\ge3\). Every displayed triple is expanded in its retained
orientation. The exact
classification and score are
\[
\boxed{
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}
P_{\tau_m^{\rm pre}}(U)=\{S_m\}
}
\tag{KPG46P-3}
\]
and
\[
\boxed{
K(\tau_m^{\rm pre})
={572m^3+631m^2+235m+22\over2}
}
\qquad(m\ge3).
\tag{KPG46P-4}
\]
There is no parity branch, second maximizer, or boundary correction.

### Exhaustive positive hole gains

For a hole \(h\) between retained neighbors \(a,b\), use the deletion gain
\(ab-h(a+b)\). Direct substitution in every position of (KPG46P-2) gives
\[
\begin{array}{c|c|c}
\text{hole position}&\text{range}&\text{deletion gain}\\ \hline
\lambda_j&0\le j\le m-1&
-4j^2+(28m+9)j+28m+12\\
\rho_{j+1}&0\le j\le m-1&
-4j^2+(28m+5)j+44m+17\\
\lambda_j&m\le j\le2m-3&
5j^2+(28m+21)j-16m^2+12m+12\\
\rho_{j+1}&m\le j\le2m-3&
5j^2+(28m+26)j-16m^2+24m+23\\
\lambda_{2m-2}=4&&60m^2-22m-14\\
\rho_{2m-1}=3&&60m^2-10m-9\\
\lambda_{2m-1}=2&&60m^2-4m-5
\end{array}
\tag{KPG46P-5}
\]
The forward differences in the first four rows are respectively
\[
28m+5-8j,\quad28m+1-8j,\quad
10j+28m+26,\quad10j+28m+31,
\]
so all four rows increase on their displayed ranges. Their left-end values
are
\[
28m+12,\quad44m+17,\quad
17m^2+33m+12,\quad17m^2+50m+23.
\]
The excesses of the three terminal values over \(28m+12\) are
\[
60m^2-50m-26,\quad60m^2-38m-21,\quad60m^2-32m-17,
\]
all positive from \(m=3\) onward. Hence the exact global result is
\[
\boxed{
\min_{h\in H_m}\bigl(ab-h(a+b)\bigr)=28m+12>0,
}
\tag{KPG46P-6}
\]
attained at \(\lambda_0=4m\). The shortened singleton range, the moved
triple, and both sides of the cyclic cut are all separate rows of
(KPG46P-5).

### Complete shortcut audit and cyclic closure

Apply the shortcut-budget lemma (K825-6)--(K825-9). For any oriented arc,
delete its internal holes and write the compressed path as
\((z_0,z_1,\ldots,z_q)\), \(q\ge2\). Every internal label is at least
\(L\).

If one endpoint \(a\) is a hole, the two boundary edges already give
\[
L(a+b)-ab\ge4L-4=16m>12m+4
\qquad(2\le a\le L-1,\ 2\le b\le n).
\tag{KPG46P-7}
\]
Thus it remains to take both endpoints in \(S_m\).

For \(q=2\), the internal labels below
\((n+1)/2=5m+2\) are exactly \(L,c_0,\ldots,c_{m-1}\). The connector
roles and the changed cyclic \(L\)-role have exact margins
\[
\begin{aligned}
c_j(A_j+B_j)-A_jB_j
&=-8j^2+(32m+7)j+12m+4,\\
L(x_{2m-1}+E_0)-x_{2m-1}E_0
&=8m^2+2m+1.
\end{aligned}
\tag{KPG46P-8}
\]
The first expression increases for \(0\le j\le m-1\), and the second
exceeds \(12m+4\) because \(8m^2-10m-3>0\) for \(m\ge3\). For every
remaining middle label \(y\ge(n+1)/2\), distinctness and
\[
y(a+b)-ab=y^2-(a-y)(b-y)
\]
give, according as both endpoints are above \(y\), below \(y\), or on
opposite sides, the lower bounds
\[
{3n-1\over2}=15m+4,\qquad
(2L+1){n+1\over2}-L(L+1)=24m^2+19m+4,\qquad y^2.
\tag{KPG46P-9}
\]
They all exceed \(12m+4\). Therefore the exact two-edge minimum is
\(12m+4\), attained at \((A_0,c_0,B_0)\).

For \(q=3\), every consecutive internal pair in (KPG46P-2) contains a
label at least
\(R'=6m+1\), and its other label is at least \(L\). Orienting the two
internal labels so the first is at least \(R'\), or exchanging the endpoints,
gives
\[
aR'+R'L+Lb-ab\ge R'L-n=24m^2-2>12m+4.
\tag{KPG46P-10}
\]
The first inequality follows by checking the four corners of
\([L,n]^2\), using \(R'+L=n-1\). The only pair that prevents reuse of the
stronger closing bound \(R=6m+2\) is the literal cyclic pair
\((x_{2m-1},L)\). Its complete path and exact margin are
\[
\begin{aligned}
(E_{2m-1},x_{2m-1},L,E_0)&=(n,6m+1,4m+1,d),\\
nx_{2m-1}+x_{2m-1}L+Ld-nd&=36m^2-2m-4>12m+4.
\end{aligned}
\tag{KPG46P-11}
\]
Thus (KPG46P-10) is exhaustive and the changed closure is also checked
directly.

For \(q\ge4\), only the uniform internal lower bound \(L\) is needed:
\[
\begin{aligned}
\sum_{i=0}^{q-1}z_i z_{i+1}-z_0z_q
&\ge L(a+b)+(q-2)L^2-ab\\
&\ge2Ln+2L^2-n^2
=12m^2-1>12m+4.
\end{aligned}
\tag{KPG46P-12}
\]
The bilinear minimum is checked at the four corners of \([L,n]^2\). Hence
(KPG46P-6)--(KPG46P-12) verify every hypothesis of the shortcut-budget
lemma. The exact global nontrivial compressed-path margin is \(12m+4\), at
\(c_0\), so \(S_m\) is the unique maximizer among subsets of cardinality at
least two. Comparing with the two-element subset \(\{n-1,n\}\) gives
\(P(S_m)\ge2n(n-1)>n^2\), excluding every singleton and proving
(KPG46P-3).

### Exact block sum

Using \(\mathcal C\) from (KPG46-15), the retained score is
\[
\begin{aligned}
P_{\tau_m^{\rm pre}}(S_m)={}&LE_0
+\sum_{j=0}^{m-1}\mathcal C(E_j,P_j,E_{j+1})\\
&+\sum_{j=m}^{2m-3}
  \bigl(E_jx_{j+1}+x_{j+1}E_{j+1}\bigr)\\
&+\mathcal C(E_{2m-2},P_m,E_{2m-1})
 +E_{2m-1}x_{2m-1}+x_{2m-1}L.
\end{aligned}
\tag{KPG46P-13}
\]
The two repeated summands are the first two expressions in (KPG46-16), while
the combined terminal contribution in (KPG46P-13) is
\[
LE_0+\mathcal C(E_{2m-2},P_m,E_{2m-1})
 +E_{2m-1}x_{2m-1}+x_{2m-1}L
=296m^2+191m+30.
\tag{KPG46P-14}
\]
Summing \(j\) and \(j^2\) on the displayed ranges gives (KPG46P-4)
directly. Equivalently, the closing and preclosing backbones differ only by
\[
(E_{2m-2},x_{2m-1},E_{2m-1},P_m,L)
\longmapsto
(E_{2m-2},P_m,E_{2m-1},x_{2m-1},L).
\]
Writing \(A_m=6m+3\), \(B_m=6m+2\), and \(x_{2m-1}=6m+1\), cancellation
of every common edge gives the independent local check
\[
\begin{aligned}
K(\tau_m^{\rm pre})-K(\tau_m^{\rm cl})
={}&E_{2m-2}(A_m-x_{2m-1})
 +E_{2m-1}(B_m-A_m)\\
&+L(x_{2m-1}-B_m)
=2(10m+2)-(10m+3)-(4m+1)=6m.
\end{aligned}
\tag{KPG46P-15}
\]

### Minimum row and exact comparisons

At \(m=3\),
\[
\alpha_3^{\rm pre}=(0,1,2,4,3,5),
\]
and the expanded order is
\[
\begin{aligned}
(&28,12,27,14,26,11,29,10,25,15,24,9,30,8,23,16,22,7,\\
 &31,6,18,5,32,4,21,17,20,3,33,2,19,13).
\end{aligned}
\tag{KPG46P-16}
\]
Its only maximizing subset is \(\{13,\ldots,33\}\), and
\[
K(\tau_3^{\rm pre})=10925,\qquad
\min h=96,\qquad
\min\text{ nontrivial shortcut margin}=40.
\tag{KPG46P-17}
\]
The three terminal hole gains are \(460,501,523\). Hence the minimum row
obeys the same theorem and hides no empty range or closure exception.

Combining (KPG46P-15) with (KPG46-18)--(KPG46-19) gives
\[
\boxed{
K(\tau_m^{\rm pre})-K(\tau_m^{\rm cl})=6m>0,
\qquad
K(\tau_m^{\rm pre})-K_{825}(m)=m^2-4>0
}
\quad(m\ge3).
\tag{KPG46P-18}
\]
Thus no admitted row ties. The complete pointwise ordering is
\[
\begin{cases}
K(\tau_m^{\rm cl})<K_{825}(m)<K(\tau_m^{\rm pre}),&3\le m\le6,\\
K_{825}(m)<K(\tau_m^{\rm cl})<K(\tau_m^{\rm pre}),&m\ge7.
\end{cases}
\]
The boundary values are
\[
\begin{array}{c|r|r|r}
m&K(\tau_m^{\rm pre})&K(\tau_m^{\rm cl})&K_{825}(m)\\ \hline
3&10925&10907&10920\\
4&23833&23809&23821\\
5&44236&44206&44215\\
6&73850&73814&73818\\
7&114391&114349&114346
\end{array}
\]

In terms of \(n=10m+3\),
\[
K(\tau_m^{\rm pre})
={286n^3+581n^2+542n-3577\over1000},
\]
\[
K(\tau_m^{\rm pre})-K(\tau_m^{\rm cl})={3(n-3)\over5},
\qquad
K(\tau_m^{\rm pre})-K_{825}(n)={n^2-6n-391\over100}.
\tag{KPG46P-19}
\]
Consequently
\[
\boxed{
K(\tau_m^{\rm pre})={143\over500}n^3+{581\over1000}n^2+O(n),
}
\tag{KPG46P-20}
\]
so both PG46 witnesses share their cubic and quadratic coefficients and the
preclosing witness is worse by a linear term. K825 has quadratic coefficient
\(571/1000\), making the preclosing witness worse by
\(n^2/100+O(n)\). These comparisons concern \(K\) on three explicit core
orders. They do not compare exact angular thresholds, prove geometric
feasibility or optimality, identify a global \(K\)-minimizer, or improve an
all-residue coefficient.

## 13. Exact \(K\) For The Descending-Min PG49 Core Order

We now evaluate the deterministic PG49 representative constructed in
(PG100)--(PG109). This section concerns the induced-subset objective \(K\),
not the product-distance score \(W\). Retain

\[
v=2m,\qquad d=8m+4,\qquad n=10m+3,\qquad
q=\kappa_{v-1}=\left\lfloor{4m+3\over5}\right\rfloor,
\]

and write \(\alpha=\alpha_{\min}\). The resulting core order, rooted at its
largest label, is

\[
\begin{aligned}
\tau_m^{\min}={}&(
E_{v-1},\lambda_{v-1},P_q,\rho_0,
E_0,\lambda_0,P_0,\rho_1,\ldots,\\
&\hspace{8em}
E_{v-2},\lambda_{v-2},P_{\alpha(v-2)},\rho_{v-1}).
\end{aligned}
\tag{KPGMIN-1}
\]

The ellipsis follows increasing gap index and expands every retained path in
its prescribed orientation. Let

\[
B_m=\{4m+1,4m+2,\ldots,n\}
\tag{KPGMIN-2}
\]

be the high backbone obtained by deleting the isolated labels
\(2,\ldots,4m\).

### Exact finite-sum formula

For a path \(P_k\), denote its first and last labels by \(f_k,l_k\), with
the same label used twice for a singleton, and put

\[
r_k=f_k+l_k=
\begin{cases}
16m+5-4k,&0\le k\le m,\\
8m+4+2k,&m<k<v.
\end{cases}
\tag{KPGMIN-3}
\]

Define

\[
\boxed{
D_m=
\sum_{j=0}^{v-1}j\bigl(r_{\alpha(j)}-r_j\bigr)
-(6m+3)(2m+1-2q).
}
\tag{KPGMIN-4}
\]

This is the exact change of the high-backbone score from the identity
assignment. To see the cancellation, in a nonclosing block write

\[
E_jf_k+P(P_k)+l_kE_{j+1}
={2E_j+1\over2}r_k+
\left(P(P_k)+{l_k-f_k\over2}\right),
\tag{KPGMIN-5}
\]

where \(P(P_k)\) is the sum of the internal path-edge products. The
parenthesized term depends only on \(k\), so its sum is unchanged by a path
permutation; the constant part of \((2E_j+1)/2=d+j+1/2\) also cancels.
At the cyclic block, replacing the fictitious next terminal \(n+1\) by
\(\rho_0=4m+1,E_0=d\) contributes

\[
-(6m+3)(l_q-l_{v-1})
=-(6m+3)(2m+1-2q),
\]

which is the last term of (KPGMIN-4). Direct substitution for the identity
assignment gives the already established branch value

\[
K_{825}(m)={572m^3+629m^2+235m+30\over2}.
\tag{KPGMIN-6}
\]

It remains to decide which isolated low labels should be inserted into the
backbone. Put \([x]_+=\max(x,0)\). For
\(1\le j<m\) with \(\Delta_j=0\), let \(r=\kappa_j\) and define the two
exact insertion gains

\[
\begin{aligned}
L_{m,j}={}&j^2-26jm-3jr-7j+8m^2
            -4mr-12m-4r-4,\\
R_{m,j}={}&L_{m,j}-j-16m-2r-7,
\end{aligned}
\tag{KPGMIN-7}
\]

corresponding respectively to \(\lambda_j\) and \(\rho_{j+1}\). Finally put

\[
G_m=
\sum_{\substack{1\le j<m\\\Delta_j=0}}
\bigl([L_{m,j}]_+ +[R_{m,j}]_+\bigr).
\tag{KPGMIN-8}
\]

Then the exact answer for every integer \(m\ge3\) is

\[
\boxed{
K(\tau_m^{\min})=K_{825}(m)+D_m+G_m.
}
\tag{KPGMIN-9}
\]

Thus (KPGMIN-3)--(KPGMIN-9), together with the ceiling formula for
\(\kappa_j\) and (PG104), are an exact \(O(m)\) integer evaluation. They do
not enumerate a path permutation, matching, or subset.

### Exhaustive low-gain classification

For completeness, we prove that (KPGMIN-7) contains every low label whose
insertion can be nonnegative. If \(P_k\) is a triple in \(G_j\), direct
substitution gives the insertion gains

\[
\begin{aligned}
g_{\lambda}(j,k)
&=-2j^2+6jk-36jm-17j+8km+8k-28m-12,\\
g_{\rho}(j,k)
&=g_{\lambda}(j,k)+4k-16m-5.
\end{aligned}
\tag{KPGMIN-10}
\]

Every triple selected by the descending-min rule satisfies \(k\le j\):
this follows from (PG40) on a jump column, from
\(k=\kappa_j+2m-1-j\le m\) on a plateau triple, where
\(\kappa_j\ge1\) also forces \(j\ge m\) and therefore \(k\le m\le j\),
and from \(q<2m-1\) at the closing column. Hence, for \(j\ge1\),

\[
g_{\lambda}(j,k)
\le-20jm-9j-28m-12<0,
\qquad
g_{\rho}(j,k)\le g_{\lambda}(j,k)-12m-5<0.
\tag{KPGMIN-11}
\]

At \(j=0,k=0\), the two values are \(-28m-12\) and \(-44m-17\).
There is no closing \(\rho\)-hole because \(\rho_0\in B_m\).

A singleton can occur only on a nonclosing plateau, where
\(k=\kappa_j+2m-1-j\). Substitution gives exactly \(L_{m,j},R_{m,j}\).
If \(j\ge m\), all omitted terms have the favorable sign for the bound

\[
L_{m,j}\le j^2-26jm+8m^2\le-17m^2<0,
\qquad R_{m,j}<L_{m,j}.
\tag{KPGMIN-12}
\]

If \(j<m\), the same plateau formula automatically has \(k>m\), and these
are precisely the positions retained in (KPGMIN-7). This proves exhaustion.

Define the positive- and zero-gain low sets by

\[
\begin{aligned}
\mathcal P_m={}&
\{\lambda_j:1\le j<m,\ \Delta_j=0,\ L_{m,j}>0\}\\
&\mathbin\cup
\{\rho_{j+1}:1\le j<m,\ \Delta_j=0,\ R_{m,j}>0\},\\
\mathcal Z_m={}&
\{\lambda_j:1\le j<m,\ \Delta_j=0,\ L_{m,j}=0\}\\
&\mathbin\cup
\{\rho_{j+1}:1\le j<m,\ \Delta_j=0,\ R_{m,j}=0\}.
\end{aligned}
\tag{KPGMIN-13}
\]

The complete maximizing-subset classification is

\[
\boxed{
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}
P_{\tau_m^{\min}}(U)
=\{B_m\mathbin\cup\mathcal P_m\mathbin\cup Z':
Z'\subseteq\mathcal Z_m\}.
}
\tag{KPGMIN-14}
\]

In particular, there are exactly

\[
\boxed{2^{|\mathcal Z_m|}}
\tag{KPGMIN-15}
\]

maximizers. This formula includes, rather than assumes away, every possible
zero-gain boundary.

### Strict shortcut audit and equality cases

We prove (KPGMIN-14) with the signed version of the shortcut identity
(K825-8), not by searching subsets. Compress all low labels to the high
backbone \(B_m\). Put \(L_0=4m+1\) and \(H_0=6m+2\). Every two-edge
backbone path is strict. The only possible internal labels below \(H_0\)
have the following exhaustive roles:

\[
\begin{aligned}
c_k(A_k+B_k)-A_kB_k
&=12m+4+k(32m+7-8k)\ge12m+4,\\
x_k(E_j+E_{j+1})-E_jE_{j+1}
&\ge35m+9,\\
\rho_0(B_q+E_0)-B_qE_0
&=2\bigl((4m+3)q-4m-1\bigr)\ge16m+16.
\end{aligned}
\tag{KPGMIN-16}
\]

The singleton minimum in the second line is attained in the wider endpoint
box at \((j,k)=(2m-2,m+1)\), so it is valid for every singleton actually
assigned by \(\alpha\). Every other internal backbone label \(z\) is at
least \(H_0\); since \(2H_0>n\),
\(z(a+b)-ab=ab(z/a+z/b-1)>0\) for all possible endpoints.

In the backbone, every label below \(H_0\) is isolated between labels at
least \(H_0\). Consequently, for compressed paths having
three, four, or at least five edges, respectively, the direct endpoint-box
bounds are

\[
\sum z_i z_{i+1}-z_0z_s\ge
\begin{cases}
4m^2-2m-1,&s=3,\\
28m^2+12m+1,&s=4,\\
28m^2+8m,&s\ge5,
\end{cases}
\tag{KPGMIN-17}
\]

all strictly positive for \(m\ge3\). If an arc endpoint is itself a selected
low label \(x<L_0\), the reduced boundary contribution is already

\[
xL_0+yL_0+(s-2)L_0^2-xy
=xL_0+y(L_0-x)+(s-2)L_0^2>0;
\tag{KPGMIN-18}
\]

two low endpoints only strengthen this conclusion.

Reinserting an internal label of \(\mathcal P_m\cup\mathcal Z_m\) changes
the corresponding arc sum by its nonnegative insertion gain. Hence the only
zero shortcut is the atomic two-edge path through one member of
\(\mathcal Z_m\); every shortcut omitting a backbone label or a positive-
gain low label is strict. The exact arc identity (K825-8) now forces all
members of \(B_m\cup\mathcal P_m\), forbids every negative-gain low label,
and leaves precisely the independent choices \(Z'\subseteq\mathcal Z_m\).
The candidate is obtained from \(B_m\) by nonnegative-gain insertions, so its
score is at least
\[
P(B_m)\ge(6m+3)(4m+1)^2>n^2;
\]
the last margin is \(96m^3-4m^2-30m-6>0\) for \(m\ge3\). Hence no
singleton can tie. This proves
(KPGMIN-14)--(KPGMIN-15) for all subset cardinalities.

The zero set is not always empty. The contrary statement, suggested by all
small rows, is exactly disproved as follows. Take

\[
\begin{aligned}
m&=101805057120180546870,\\
j&=29025982843749082380,\\
\kappa_j=\kappa_{j+1}
&=14013559766810587979.
\end{aligned}
\tag{KPGMIN-19}
\]

The two exact ceiling residuals are

\[
\begin{aligned}
2\kappa_j(d+j)-j(d-1)
 &=912801999149094883612,\\
2\kappa_j(d+j+1)-(j+1)(d-1)
 &=126388661721271684607,
\end{aligned}
\]

and direct comparison with their respective denominators puts both values
in the required half-open ceiling intervals. Thus \(\Delta_j=0\). The
assigned singleton index and gains are

\[
\begin{aligned}
k&=188597691163422599338>m,\\
L_{m,j}&=0,\\
R_{m,j}&=-1685934016300259008265.
\end{aligned}
\tag{KPGMIN-20}
\]

This is an exact, not numerical, zero. One derivation starts from
\(x(a+b)=ab\), or \((a-x)(b-x)=x^2\), for
\(x=\lambda_j\), \(a=E_j\), and the adjacent singleton \(b=x_k\).
Writing

\[
a-x=gu^2,\qquad b-x=gw^2,\qquad x=guw
\]

gives

\[
j={gu(u-w)-4\over5},\qquad
m={gu(2u+3w)-8\over20},\qquad
\kappa_j={g(10w^2-4u^2-uw)+6\over10}.
\tag{KPGMIN-21}
\]

The choice
\((g,u,w)=(4,11116408784,7852541895)\) yields (KPGMIN-19)--(KPGMIN-20).
It follows that the maximizer is not universally unique; at this row at
least the inclusion or omission of \(\lambda_j\) gives two maximizers.

### Exact Diophantine classification of the zero-gain set

We now classify both equations defining \(\mathcal Z_m\), including the
plateau and its half-open endpoints.  The classification is exact, but it
also exposes a residual cubic-continued-fraction question which the present
argument does not decide.  In particular, neither finiteness nor infinitude
of the union over all \(m\) will be inferred from a finite sweep.

Retain \(1\le j<m\), put \(r=\kappa_j=\kappa_{j+1}\), and use
\(\delta=0\) for the left hole \(\lambda_j\) and \(\delta=1\) for the
right hole \(\rho_{j+1}\).  Define

\[
x_\delta=4m-2j-\delta,
\qquad
a_\delta=8m+4+j+\delta,
\qquad
b=6m+1+r-j.
\]

Thus \(b\) is the assigned singleton, while \(a_0=E_j\) and
\(a_1=E_{j+1}\).  Direct expansion, with the two equations kept distinct,
gives

\[
\begin{aligned}
L_{m,j}
 &=x_0(a_0+b)-a_0b
  =x_0^2-(a_0-x_0)(b-x_0),\\
R_{m,j}
 &=x_1(a_1+b)-a_1b
  =x_1^2-(a_1-x_1)(b-x_1).
\end{aligned}
\tag{KPGZERO-1}
\]

All factors in (KPGZERO-1) are positive on the stated domain.  If either
gain is zero, take

\[
g=\gcd(a_\delta-x_\delta,b-x_\delta).
\]

The standard coprime square-factor argument is reversible and unique:

\[
\boxed{
a_\delta-x_\delta=gu^2,\qquad
b-x_\delta=gw^2,\qquad
x_\delta=guw,\qquad
g>0,\quad \gcd(u,w)=1.
}
\tag{KPGZERO-2}
\]

Moreover \(u>w>0\).  Indeed the plateau gives \(r\le j\), and hence
\(a_\delta-x_\delta>b-x_\delta\).  Solving (KPGZERO-2) gives the unified
formulas

\[
\boxed{
\begin{aligned}
j_\delta&={gu(u-w)-(4+3\delta)\over5},\\
m_\delta&={gu(2u+3w)-(8+\delta)\over20},\\
r_\delta&={g(10w^2-4u^2-uw)+(6-3\delta)\over10}.
\end{aligned}}
\tag{KPGZERO-3}
\]

For \(\delta=0\), these are exactly (KPGMIN-21).  For \(\delta=1\), the
previously missing right-hole formulas are

\[
j={gu(u-w)-7\over5},\qquad
m={gu(2u+3w)-9\over20},\qquad
r={g(10w^2-4u^2-uw)+3\over10}.
\tag{KPGZERO-4}
\]

The three quantities in (KPGZERO-3) are integers if and only if

\[
\boxed{gu(2u+3w)\equiv8+\delta\pmod {20}.}
\tag{KPGZERO-5}
\]

Modulo five, this congruence is equivalent to
\(gu(u-w)\equiv4+3\delta\pmod5\), and it then supplies the required
modulo-five condition for \(r\).  The parity of \(gu(2u+3w)\) is \(guw\),
so (KPGZERO-5) also supplies the remaining parity condition for \(r\).
In particular, the right branch
forces \(g,u,w\) all odd; it also forces \(j\) odd and \(r\) even.  On the
left, (KPGZERO-5) is equivalently

\[
gu(u-w)\equiv4\pmod5,\qquad 4\mid gu(2u+3w).
\]

The four domain conditions are exactly

\[
\boxed{
\begin{aligned}
gu(u-w)&\ge9+3\delta,\\
gu(2u+3w)&\ge68+\delta,\\
gu(7w-2u)&\ge12-11\delta,\\
g(10w^2-4u^2-uw)&\ge4+3\delta.
\end{aligned}}
\tag{KPGZERO-6}
\]

They are respectively \(j\ge1\), \(m\ge3\), \(j<m\), and \(r\ge1\).
Thus (KPGZERO-2)--(KPGZERO-6) are an exact, unique parametrization of the
two gain equations before the plateau inequalities are imposed.

We now impose those inequalities integrally.  Put

\[
d=8m+4,\qquad
c_t=2r(d+t)-t(d-1).
\]

The literal ceiling convention is

\[
\boxed{
\kappa_t=r
\quad\Longleftrightarrow\quad
0\le c_t<2(d+t).
}
\tag{KPGZERO-7}
\]

Consequently the plateau requires (KPGZERO-7) at both \(t=j\) and
\(t=j+1\).  The difference is
\(c_j-c_{j+1}=d-1-2r>0\).  In the parametrization,

\[
5(d-1-2r)=
g(8u^2+7uw-10w^2)-(7-\delta)>0,
\]

because, for \(u=w+s\), \(s\ge1\), the quadratic is
\(5w^2+23ws+8s^2\ge36\).  Hence all four half-open inequalities are
equivalent to

\[
c_{j+1}\ge0,\qquad c_j<2(d+j).
\tag{KPGZERO-8}
\]

Define the common cubic form

\[
\Phi(u,w)=50w^3+51uw^2-27u^2w-24u^3.
\tag{KPGZERO-9}
\]

For the **left equation** \(L_{m,j}=0\), direct substitution gives

\[
\begin{aligned}
N_L:=25c_{j+1}
 &=g^2u\Phi+g(7u^2+18uw+50w^2)+31,\\
Q_L:=25\bigl(c_j-2(d+j)\bigr)
 &=g^2u\Phi-3gu(u-w)-4.
\end{aligned}
\tag{KPGZERO-10}
\]

Thus the complete left plateau is

\[
\boxed{N_L\ge0,\qquad Q_L<0.}
\tag{KPGZERO-11}
\]

The equality \(N_L=0\), namely the allowed endpoint
\(h_{j+1}=r\), must be retained.  It can occur only in the residual
subcase \(g\mid31\); parity and (KPGZERO-5) further force
\(g\in\{1,31\}\), \(u\) odd, and \(w\) even.  We neither discard nor
assert existence of this boundary subcase.  The equality \(Q_L=0\), namely
the excluded endpoint \(h_j=r-1\), cannot occur in the admitted domain:
it would force \(gu\mid4\), and the finitely many possibilities contradict
either (KPGZERO-5) or the first inequality in (KPGZERO-6).  Since both
residuals are multiples of \(25\), every admitted left row has
\(N_L=0\) or \(N_L\ge25\), and always \(Q_L\le-25\).

For the **right equation** \(R_{m,j}=0\), the corresponding exact residuals
are

\[
\begin{aligned}
N_R:=25c_{j+1}
 &=g^2u\Phi+2gu(13u+12w)-6,\\
Q_R:=25\bigl(c_j-2(d+j)\bigr)
 &=g^2u\Phi+g(16u^2+9uw-50w^2)+14.
\end{aligned}
\tag{KPGZERO-12}
\]

Thus the complete right plateau is, separately,

\[
\boxed{N_R\ge0,\qquad Q_R<0.}
\tag{KPGZERO-13}
\]

Here both endpoints are automatically strict.  If \(N_R=0\), then
\(gu\mid6\); the oddness forced by (KPGZERO-5) and the first domain bound
leave no possibility.  The number \(Q_R\) is odd before using its
divisibility by \(25\), so \(Q_R=0\) is impossible.  Therefore every
admitted right row satisfies

\[
\boxed{N_R\ge25,\qquad Q_R\le-25.}
\tag{KPGZERO-14}
\]

Equations (KPGZERO-2)--(KPGZERO-6), (KPGZERO-10)--(KPGZERO-11), and
(KPGZERO-12)--(KPGZERO-13) are a necessary-and-sufficient polynomial and
congruential classification, with no ceiling or floor left implicit.  In
particular, if \(\mathfrak P_\delta\) denotes the resulting parameter set,
then

\[
\boxed{
\begin{aligned}
\mathcal Z_m={}&
\{\lambda_{j_0(g,u,w)}:(g,u,w)\in\mathfrak P_0,
                         m_0(g,u,w)=m\}\\
&\mathbin\cup
\{\rho_{j_1(g,u,w)+1}:(g,u,w)\in\mathfrak P_1,
                              m_1(g,u,w)=m\}.
\end{aligned}}
\tag{KPGZERO-15}
\]

For each fixed \(m\), this already gives
\(|\mathcal Z_m|\le2(m-1)\), so \(\mathcal Z_m\) is finite.  The
nontrivial cardinality question below concerns the union over all \(m\).

The union is disjoint at each plateau, since

\[
R_{m,j}=L_{m,j}-(j+16m+2r+7)<L_{m,j}.
\tag{KPGZERO-16}
\]

There are no omitted boundary columns.  If a plateau has \(r=1\), then
\(\kappa_{j+1}=1\) gives
\((j+1)(d-3)\le2d\); since \(d\ge28\), this forces \(j=1\).
At \(j=r=1\), both gains are odd and cannot vanish.  At \(j=m-1\),

\[
L_{m,m-1}=-17m^2+5m+4-(7m+1)r<0,
\qquad R_{m,m-1}<L_{m,m-1}.
\tag{KPGZERO-17}
\]

Every jump column \(\Delta_j=1\) carries a triple and both of its insertion
gains are strictly negative by (KPGMIN-11).  Column \(j=0\) is likewise a
triple, with gains \(-28m-12\) and \(-44m-17\).  All singleton columns
\(j\ge m\) have \(R_{m,j}<L_{m,j}\le-17m^2\) by (KPGMIN-12), and there is
no closing \(\rho\)-hole because \(\rho_0\in B_m\).  This exhausts the
outer and jump-column cases independently of the Diophantine
parametrization.  For reference, the gain equation alone also has the conic
normal form

\[
X_\delta^2-Y_\delta^2=8J_\delta^2,
\tag{KPGZERO-18}
\]

where

\[
\begin{aligned}
J_\delta&=5j+4+3\delta=gu(u-w),\\
X_\delta&=2r+19j+14+12\delta
 =g(3u^2-4uw+2w^2),\\
Y_\delta&=8m-13j-2r-6-8\delta
 =g(-u^2+4uw-2w^2).
\end{aligned}
\]

This conic parametrizes the zero equation, not the plateau.  For example,
the right parameters \((g,u,w)=(1,13,9)\) give the integral gain-zero point
\((m,j,r)=(34,9,2)\), while
\(\kappa_9=\kappa_{10}=5\ne2\).  Therefore a Pell-style argument applied
only to (KPGZERO-18) does not prove a zero-gain family.

We next make the remaining cardinality obstruction exact.  Let

\[
\phi(t)=50+51t-27t^2-24t^3.
\]

It is strictly decreasing for \(t>1\), with

\[
\phi(7/5)={328\over125}>0,
\qquad
\phi(10/7)=-{760\over343}<0.
\]

Hence it has a unique root in \((1,\infty)\), denoted
\(\xi\in(7/5,10/7)\).  Modulo seven,
\(\phi(t)=4t^3+t^2+2t+1\) has no root, so \(\phi\) is irreducible and
\(\xi\) is genuinely cubic.  Also

\[
\Phi(u,w)=w^3\phi(u/w)\ne0.
\tag{KPGZERO-19}
\]

Each primitive fraction supports only finitely many values of \(g\), and the
finite windows can be written without a hidden ceiling.  Put

\[
\begin{aligned}
S_L&=7u^2+18uw+50w^2,\\
S_R&=2u(13u+12w),\\
B_L&=3u(u-w),\\
T_R&=50w^2-16u^2-9uw.
\end{aligned}
\]

The right domain bound in (KPGZERO-6) gives
\(T_R>4u(u-w)>0\).  If \(\Phi=-H<0\), the exact active quadratic
windows are

\[
\boxed{
uHg^2-S_Lg-31\le0\quad(L),
\qquad
uHg^2-S_Rg+31\le0\quad(R).
}
\tag{KPGZERO-20}
\]

Indeed \(Q_L<0\) is immediate, while
\(Q_R=-g^2uH-gT_R+14<0\) follows from
\(gT_R>4gu(u-w)\ge48\).  If \(\Phi>0\), the exact active windows are

\[
\boxed{
u\Phi g^2-3u(u-w)g+21\le0\quad(L),
\qquad
u\Phi g^2-T_Rg+39\le0\quad(R).
}
\tag{KPGZERO-21}
\]

Here \(N_L>0\), and \(N_R=g^2u\Phi+S_Rg-6>0\), so the other residual is
automatic.  The constants \(21,31,39\) use divisibility by \(25\) and the
endpoint audit in (KPGZERO-11)--(KPGZERO-14); on parameters satisfying
(KPGZERO-5), these closed inequalities are equivalent to the original
half-open ones.  Intersecting (KPGZERO-20) or (KPGZERO-21) with the
congruence (KPGZERO-5), the domain (KPGZERO-6), and positive integers gives
the complete finite set of scales \(g\).  Explicitly, for \(\Phi=-H<0\),

\[
\begin{aligned}
L:\quad&
0<g\le {S_L+\sqrt{S_L^2+124uH}\over2uH},\\
R:\quad&
{S_R-\sqrt{S_R^2-124uH}\over2uH}
\le g\le
{S_R+\sqrt{S_R^2-124uH}\over2uH},
\qquad S_R^2\ge124uH;
\end{aligned}
\]

for \(\Phi>0\),

\[
\begin{aligned}
L:\quad&
{B_L-\sqrt{B_L^2-84u\Phi}\over2u\Phi}
\le g\le
{B_L+\sqrt{B_L^2-84u\Phi}\over2u\Phi},
\qquad B_L^2\ge84u\Phi,\\
R:\quad&
{T_R-\sqrt{T_R^2-156u\Phi}\over2u\Phi}
\le g\le
{T_R+\sqrt{T_R^2-156u\Phi}\over2u\Phi},
\qquad T_R^2\ge156u\Phi.
\end{aligned}
\]

In every line \(g\) is restricted further to
\(\mathbb Z_{>0}\) and (KPGZERO-5)--(KPGZERO-6).  These closed radical
intervals are therefore an exact finite parametrization, not merely an
asymptotic bound.

More sharply, every admitted primitive ratio is a regular continued-fraction
convergent of \(\xi\).  The residual windows and the mean-value theorem
give

\[
\boxed{
\left|{u\over w}-\xi\right|<{1\over2w^2}.
}
\tag{KPGZERO-22}
\]

On \(t>7/5\), one has
\(-\phi'(t)=72t^2+54t-51>165\); on \(t>1\), the same quantity is
strictly greater than \(75\).  Here are uniform bounds retaining both
sides.  For a left solution above
\(\xi\), (KPGZERO-20), \(w\ge7\), and
\(7t+18+50/t<64\) give
\(w^2(t-\xi)<65/165\).  The assertion \(w\ge7\) has no finite
exception: \(r\ge1\) gives
\(t<(\sqrt{161}-1)/8<3/2\), while \(\xi>7/5\), and none of the open
intervals \((7w/5,3w/2)\), \(1\le w\le6\), contains an integer \(u\).
Below \(\xi\), one has \(w\ge2\); (KPGZERO-21) first forces
\(t>7/5\) (otherwise the lower bound
\(\Phi\ge(328/125)w^3\) contradicts that window), and then gives
\(w^2(\xi-t)<5/165\).  For a right solution
above \(\xi\), (KPGZERO-20) gives
\(w^2(t-\xi)<63/165\); below \(\xi\), (KPGZERO-21) gives the bound
\(25/75\).  Each is strictly below \(1/2\).  Legendre's criterion now
proves (KPGZERO-22).

Let \(p_\nu/q_\nu\) be the regular convergents of \(\xi\), and let
\(\mathcal G_\delta(p_\nu,q_\nu)\) be the finite set of positive integers
\(g\) satisfying (KPGZERO-5)--(KPGZERO-6) and the corresponding separate
plateau window (KPGZERO-11) or (KPGZERO-13).  The exact global
classification is the bijection

\[
\boxed{
\mathfrak P_\delta
\longleftrightarrow
\{(\nu,g):g\in\mathcal G_\delta(p_\nu,q_\nu)\},
\qquad \delta=0,1,
}
\tag{KPGZERO-23}
\]

followed by (KPGZERO-3) and (KPGZERO-15).  Necessity is
(KPGZERO-22); sufficiency is direct substitution into the congruences,
domain bounds, and exact plateau residuals.

This is also the sharp obstruction to the requested finite/infinite
dichotomy.  The global left or right set is infinite exactly when infinitely
many one-sided convergents of this particular cubic root pass both a fixed
congruence filter and the displayed finite \(g\)-window.  Infinitely many
convergents by itself is insufficient: side, approximation coefficient, and
residue class all matter.  No theorem established in this repository decides
that filtered cubic subsequence.  The general scarcity of information about
partial quotients of algebraic numbers of degree at least three is documented
by Adamczewski and Bugeaud, *Acta Mathematica* 195 (2005), 1--20
([preprint](https://arxiv.org/abs/math/0511677)).  Accordingly,

\[
\boxed{
\text{finiteness versus infinitude of }
\bigcup_{m\ge3}\mathcal Z_m
\text{ remains an unresolved Diophantine claim.}
}
\tag{KPGZERO-24}
\]

Equation (KPGZERO-24) is not a guess from a sweep: it records the exact point
at which the proof stops.  Proving either alternative requires an additional
theorem about the filtered convergents in (KPGZERO-23).

The large left witness (KPGMIN-19) is recovered primitively by

\[
(g,u,w)=(4,11116408784,7852541895),\qquad \gcd(u,w)=1.
\]

It gives

\[
\begin{aligned}
a_0-x_0&=494298177011969434624=4u^2,\\
b-x_0&=246649656850920764100=4w^2,\\
x_0&=349168262793224022720=4uw,
\end{aligned}
\tag{KPGZERO-25}
\]

and reconstructs exactly the \((m,j,r,k)\) of
(KPGMIN-19)--(KPGMIN-20).  Its plateau chain is

\[
0<126388661721271684607
<912801999149094883612
<1686932879610386914688=2(d+j),
\tag{KPGZERO-26}
\]

where the first two numbers are \(c_{j+1}\) and \(c_j\).  Thus neither
half-open boundary is hidden, and

\[
L_{m,j}=0,\qquad
R_{m,j}=-1685934016300259008265.
\]

The right branch is also genuinely nonempty.  One primitive exact witness is

\[
\begin{aligned}
g={}&19,\\
u={}&7473073805813661315256495159240494740302603139227,\\
w={}&5278919324111360426689943587091134465306838560333.
\end{aligned}
\tag{KPGZERO-27}
\]

These integers satisfy \(\gcd(u,w)=1\) and
\(gu(2u+3w)\equiv9\pmod {20}\), namely (KPGZERO-5).
Formula (KPGZERO-4) gives

\[
\begin{aligned}
m={}&218540779117020202383060408199944193641213755526502466925065296490539746241930204347394895037374689,\\
j={}&62308897855848837760124442915698598519487605320218795625218461754986470706211023818397029209164763,\\
r={}&30082339289161262936522647650311907662203655554834208483736149273057046182033506346960514256432748.
\end{aligned}
\tag{KPGZERO-28}
\]

At this row the zero label and assigned singleton-path index are respectively

\[
\begin{aligned}
\rho_{j+1}={}&749545320756383134011992746968379577525879811465572276449824262452186043555298769752785521731169229,\\
k={}&404854999667352829942519021134501696425143561287620346708648280499150067959682891223353275122017362.
\end{aligned}
\]

The exact plateau residuals and denominators are

\[
\begin{aligned}
c_j={}&2557444511371761079345392522862588370572067010168649625564320432471158263160903904496874695905261439,\\
c_{j+1}={}&869282957013921986153954552563658636766764277066298307131270359092954385589529282411636564119129420,\\
2(d+j)={}&3621270261584020913649215417030504295298395299064477062051481667358608881283305317195112379016324558,\\
2(d+j+1)={}&3621270261584020913649215417030504295298395299064477062051481667358608881283305317195112379016324560.
\end{aligned}
\tag{KPGZERO-29}
\]

They lie strictly in their respective half-open intervals, and direct gain
evaluation gives

\[
\boxed{
R_{m,j}=0,\qquad
L_{m,j}=3619126042306494601762136269415429512103315004853926683393735504149736502941161306070636378320025290.
}
\tag{KPGZERO-30}
\]

Thus a universal right-hole obstruction is false.  What remains unresolved
is an infinite right-hole family, not right-hole existence.

The sole bounded diagnostic for this subsection is the standalone
standard-library script in
`ops/TASK-20260719__pg49_zero_gain_classification/`.  It checks literal rows
through \(m=500\), a direct near-root denominator range through \(10^5\),
and finitely many proposed convergents with denominator at most \(10^{200}\)
and \(g\le200\).  Decimal arithmetic is used only to propose convergents;
every reported zero is then reconstructed and accepted by exact integer
formulas, both literal ceilings, and the appropriate literal gain.  The run
finds 56 left parameter triples and eight right parameter triples, including
(KPGZERO-25) and (KPGZERO-27).  These counts are **bounded exact diagnostic
evidence**, not an exhaustive all-\(m\) result and not evidence sufficient to
choose either side of (KPGZERO-24).

### Exact comparison with K825 and both PG46 witnesses

Let \(\beta=\alpha^{-1}\),
\(d_k=\beta(k)-k\), and
\(C_t=\sum_{k=1}^t d_k\). Since \(\beta\) permutes the positive
positions, \(C_{v-1}=0\). Abel summation and (KPGMIN-3) give

\[
S_m:=\sum_{j=0}^{v-1}j(r_{\alpha(j)}-r_j)
=4\sum_{t=1}^{m-1}C_t+(2m-1)C_m
-2\sum_{t=m+1}^{2m-2}C_t.
\tag{KPGMIN-22}
\]

For \(m\ge5\), \(q\le m-1\). If \(k<q\), (PG106) gives
\(\beta(k)=\ell_k\ge2k\), because \(h_{2k}<k\); also
\(\beta(q)=v-1\ge2q\). Hence

\[
C_t\ge{t(t+1)\over2}\quad(t\le q),
\qquad
C_t\ge{q(q+1)\over2}\quad(q<t\le m).
\tag{KPGMIN-23}
\]

For \(q<k\le m\), the path lies on a plateau and
\(\beta(k)=v-1+\kappa_{\beta(k)}-k\ge v-k\ge k\), which proves the
second bound. For \(k=m+s>m\), the same identity and
\(\kappa_{\beta(k)}\le m\) give

\[
C_{m+u}\le C_m+u(m-u-2)
\qquad(1\le u\le m-2).
\tag{KPGMIN-24}
\]

Put

\[
\mathcal A=
\sum_{t=1}^{q}{t(t+1)\over2}
+(m-1-q){q(q+1)\over2},\qquad
\mathcal B={(m-2)(m-1)(m-3)\over6}.
\]

Equations (KPGMIN-22)--(KPGMIN-24), with the negative sign on the final
sum retained, yield

\[
S_m\ge4\mathcal A+{3q(q+1)\over2}-2\mathcal B.
\tag{KPGMIN-25}
\]

Substitute \(q=\lfloor(4m+3)/5\rfloor\) and write \(m=5u+r\). The lower
bound for \(D_m-(m^2-4)\), for \(r=0,1,2,3,4\), is respectively

\[
\begin{array}{c|l}
r&\text{lower margin}\\ \hline
0&3(11u^3-u^2-17u+1)\\
1&33u^3+20u^2-34u-3\\
2&33u^3+43u^2-7u-2\\
3&33u^3+66u^2+30u+8\\
4&33u^3+73u^2-11u-37.
\end{array}
\tag{KPGMIN-26}
\]

On the admitted ranges \(m\ge6\), these become, after shifting \(u\) to
a nonnegative variable where necessary,

\[
\begin{gathered}
33x^3+195x^2+333x+153,
\quad33x^3+119x^2+105x+16,\\
33x^3+142x^2+178x+67,
\quad33x^3+66x^2+30x+8,\\
33x^3+172x^2+234x+58,
\end{gathered}
\]

so every margin is positive. The omitted row \(m=5\) is a direct exact
evaluation, \(D_5=56>21=m^2-4\). Therefore

\[
\boxed{D_m>m^2-4\qquad(m\ge5).}
\tag{KPGMIN-27}
\]

Since \(G_m\ge0\), write \(H_m=D_m+G_m\). The exact three differences are

\[
\begin{aligned}
K(\tau_m^{\min})-K_{825}(m)&=H_m,\\
K(\tau_m^{\min})-K(\tau_m^{\rm cl})
 &=H_m-(m^2-6m-4),\\
K(\tau_m^{\min})-K(\tau_m^{\rm pre})
 &=H_m-(m^2-4).
\end{aligned}
\tag{KPGMIN-28}
\]

The only initial values needed in addition to (KPGMIN-27) are

\[
(D_3,G_3)=(12,0),\qquad
(D_4,G_4)=(-4,0),\qquad
(D_5,G_5)=(56,0).
\tag{KPGMIN-29}
\]

Consequently the descending-min order is smaller than K825 and the
preclosing PG46 value exactly at \(m=4\), and is larger at \(m=3\) and
every \(m\ge5\). It is larger than the closing PG46 value for every
\(m\ge3\). No equality occurs. The first three rows make every sign visible:

\[
\begin{array}{c|r|r|r|r}
m&K(\tau_m^{\rm cl})&K_{825}&K(\tau_m^{\rm pre})
 &K(\tau_m^{\min})\\ \hline
3&10907&10920&10925&10932\\
4&23809&23821&23833&23817\\
5&44206&44215&44236&44271.
\end{array}
\tag{KPGMIN-30}
\]

At \(m=3\), the canonical rooted order itself is

\[
\begin{aligned}
(&33,2,21,17,20,13,28,12,27,14,26,11,29,10,19,9,\\
 &30,8,25,15,24,7,31,6,18,5,32,4,23,16,22,3).
\end{aligned}
\tag{KPGMIN-31}
\]

Its sole maximizing subset is \(B_3=\{13,\ldots,33\}\), its score is
10932, its minimum nontrivial compressed-path margin is 40, and its minimum
positive deletion gain is 71. Thus the minimum row has no hidden empty
range or cyclic exception.

### Cubic coefficient and failure of quasipolynomiality

The exact positive-part sum (KPGMIN-9) is not a polynomial or an eventual
quasipolynomial. We first compute its cubic coefficient. Put

\[
f(x)={4x\over8+x},\qquad
f'(x)={32\over(8+x)^2},\qquad
g(x)=2-x+f(x),\qquad
b={\sqrt{41}-3\over2}.
\tag{KPGMIN-32}
\]

Uniformly, \(\kappa_j/m=f(j/m)+O(m^{-1})\). A jump column has asymptotic
path index \(f(x)m\), while a plateau column has index \(g(x)m\); the
jump and plateau densities are respectively \(f'(x)\) and \(1-f'(x)\).
The jump path is always a triple, while the plateau path changes from a
singleton to a triple at the unique point \(g(b)=1\). For a terminal block
with scaled gap index \(x\) and scaled path index \(y\), its leading
contributions are

\[
C_{\rm tr}(x,y)=2(8-2y)(12+x+y),\qquad
C_{\rm si}(x,y)=2(8+x)(4+y).
\tag{KPGMIN-33}
\]

Here is the uniform error control needed below. If \(\Phi\) is Lipschitz on
\([0,2]\), discrete summation by parts and
\(\kappa_j=mf(j/m)+O(1)\) give

\[
\sum_{j=0}^{v-2}\Delta_j\Phi(j/m)
=m\int_0^2 f'(x)\Phi(x)\,dx+O(1),
\qquad
\sum_{j=0}^{v-2}(1-\Delta_j)\Phi(j/m)
=m\int_0^2(1-f'(x))\Phi(x)\,dx+O(1),
\]

where changing the finitely many endpoints only changes the \(O(1)\) term.
On jump and plateau columns respectively,
\(\alpha(j)/m=f(j/m)+O(m^{-1})\) and
\(\alpha(j)/m=g(j/m)+O(m^{-1})\). Each exact block contribution is therefore
\(m^2C_{\rm tr}(x,y)+O(m)\) or
\(m^2C_{\rm si}(x,y)+O(m)\), uniformly. Moreover
\(g'(x)=f'(x)-1\) is bounded away from zero on \([0,2]\), so the discrete
triple/singleton transition differs by only \(O(1)\) columns from the unique
solution \(g(b)=1\). Thus the accumulated error is \(O(m^2)\).

Applying these summation estimates, followed by the ordinary Riemann sum on
the plateaus, gives the high-backbone coefficient

\[
\begin{aligned}
C_0={}&\int_0^b
 \bigl[f'C_{\rm tr}(x,f)+(1-f')C_{\rm si}(x,g)\bigr],dx\\
&+\int_b^2
 \bigl[f'C_{\rm tr}(x,f)+(1-f')C_{\rm tr}(x,g)\bigr],dx\\
={}&206\sqrt{41}-{2546\over3}
+128\bigl(56\log2+10\log5-19\log(13+\sqrt{41})\bigr).
\end{aligned}
\tag{KPGMIN-34}
\]

For an early plateau, both low insertion gains have the same leading scaled
form

\[
I(x)={x^3-30x^2-216x+64\over x+8}.
\tag{KPGMIN-35}
\]

The numerator is strictly decreasing on \([0,2]\), is positive at zero,
and is negative at one. Let \(a\in(0,1)\) be its unique root. The two low
positions and the plateau density give

\[
\begin{aligned}
C_{\rm ins}
&=2\int_0^a(1-f'(x))I(x)\,dx\\
&={24\over5}a^2-{3212\over5}a+{1616\over15}
 +2176\log{a+8\over8}.
\end{aligned}
\tag{KPGMIN-36}
\]

The zero boundary has measure zero, so the positive part introduces no
additional leading term. More precisely, uniformly on the relevant early
plateaus,
\[
L_{m,j}=m^2I(j/m)+O(m),
\qquad
R_{m,j}=m^2I(j/m)+O(m).
\]
Because \(x\mapsto[x]_+\) is \(1\)-Lipschitz, the same summation estimate
applied to the Lipschitz function \([I]_+\) shows that replacing the exact
positive parts by the integral in (KPGMIN-36) costs \(O(m^2)\). Hence

\[
\boxed{
K(\tau_m^{\min})=Cm^3+O(m^2),\qquad
C=C_0+C_{\rm ins}
=288.1683105370884612135111915\ldots
}
\tag{KPGMIN-37}
\]

and, because \(n=10m+3\),

\[
\boxed{
K(\tau_m^{\min})
=0.2881683105370884612135112\ldots\,n^3+O(n^2).
}
\tag{KPGMIN-38}
\]

This coefficient is strictly larger than \(143/500\), not merely
numerically so. Indeed (KPGMIN-27) and the existence of the limit imply
\(C_0\ge286\), while the integral in (KPGMIN-36) is strictly positive.
Thus \(C>286\), and division by \(10^3\) gives
\(C/1000>286/1000=143/500\). The descending-min choice is therefore
asymptotically worse than K825 and both PG46 witnesses at cubic order.

Finally combine the logarithms in (KPGMIN-34)--(KPGMIN-36):

\[
C=206\sqrt{41}+{24\over5}a^2-{3212\over5}a-{11114\over15}
+128\log Q,
\]

\[
Q={2^5 5^{10}(a+8)^{17}\over(13+\sqrt{41})^{19}}.
\tag{KPGMIN-39}
\]

The cubic defining \(a\) takes the nonzero values
\(1,1,3,6,2,4,4\) at the seven residues modulo seven. Hence it is
irreducible and
\([\mathbb Q(a):\mathbb Q]=3\). Therefore
\(\mathbb Q(a)\cap\mathbb Q(\sqrt{41})=\mathbb Q\). If \(Q=1\), then
\((a+8)^{17}=2^{-5}5^{-10}(13+\sqrt{41})^{19}\) would belong to this
intersection. The right side is not rational, because its positive quadratic
conjugate replaces \(13+\sqrt{41}\) by the distinct
\(13-\sqrt{41}\). Thus \(Q\ne1\).

Hermite--Lindemann now implies that \(\log Q\) is transcendental: if it were
a nonzero algebraic number, its exponential \(Q\) would be transcendental.
Consequently \(C\) is transcendental. An integer-valued eventual
quasipolynomial bounded by \(O(m^3)\) restricts on each residue class to an
integer-valued polynomial of degree at most three, whose leading coefficient
is rational by finite differences. The common limit in (KPGMIN-37) would
force that rational coefficient to equal the transcendental number \(C\), a
contradiction. Hence the exact floor/positive-part sum (KPGMIN-9) is the
required replacement: no polynomial or quasipolynomial formula exists.

All conclusions in this section concern one explicit combinatorial core
order. Its relation compatibility gives \(W=T\) by the separate PG62
theorem, but no geometric feasibility, angular-threshold identity, global
\(K\)-minimality, or geometric consequence follows from the present
calculation.

## 14. Asymptotic Consequences And Non-Consequences

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
{434+4\sqrt2\over1587}
\le
\liminf_{n\to\infty}{\Lambda_n\over n^3}
\le
\limsup_{n\to\infty}{\Lambda_n\over n^3}
\le
{143\over500}.
\tag{CR42}
\]

None of these statements proves that either normalized sequence converges, or
identifies an exact leading constant. In particular, the bounded values in
(CR34) do not give a closed-form evaluation of (CR28a); \(143/500\) is the
current upper coefficient, not an exact constant. The older \(8/25\)
coefficient remains the exact product-distance asymptotic but is superseded
for \(\Lambda_n\) and the geometric sandwich by (K825-25)--(K825-26).

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
  growing-\(k\) control, rounding, or infinite-prefix theorem. Its separate
  fixed-\(k\) instances are used in (CR28dw1)--(CR28dw12) and
  (CR28dw29).
- The normalized simplex theorem (CR28cr)--(CR28dd) solves the compact
  polynomial for every fixed \(k\), proves its unique interior maximizer and
  the exact recurrence \(M_k\nearrow1/3\), and generates the first five
  rational simplex points used here. It does not imply the separate direct finite-\(k\)
  charging theorem or make that theorem uniform in growing \(k\). The formal
  endpoint value \(1/3\) is not a bound. At the strict all-middle density
  \(\alpha_\infty=(13-2\sqrt2)/23\), however, the normalized optimizer is
  strictly admissible for every fixed finite \(k\). Applying charging at each
  fixed \(k\) gives \(L_\Lambda\ge C_k(\alpha_\infty)\); taking the supremum
  of those scalar inequalities gives
  \[
  L_\Lambda\ge{434+4\sqrt2\over1587},
  \qquad
  \liminf_{n\to\infty}{R_2^*(n)\over n^3}
  \ge{434+4\sqrt2\over1587\pi}.
  \]
  This uses no \(k=k(n)\), uniform threshold, or interchange of limits.
- The global clipped classification (CR28dw13)--(CR28dw29) solves the full
  compact continuous template for arbitrary finite \(k\), not only its
  all-middle restriction. Coordinatewise clipping gives
  \((k+1)(k+2)/2\) regimes and the exact Bellman envelope. Its values are
  finite lower Darboux sums for the increasing clipped floor; the limiting
  integral excludes every high regime from global optimality. For each
  finite \(k\), the unique global tuple is strict all-middle, with density
  \(\alpha_{k,*}\) from (CR28dw24) and value \(C_{k,*}\). These values
  increase strictly to
  \[
  \sup_{k<\infty}C_{k,*}=C_{\mathrm{AF}},
  \]
  so the existing all-fixed-\(k\) lower coefficient is exactly the supremum
  of the entire finite-prefix template family and is not attained at finite
  \(k\).
- Combining those two separate theorems only at fixed \(k=5\), with
  \(\alpha=13/30\), gives the explicit rational all-middle point
  (CR28dx)--(CR28dz), the exact coefficient
  \[
  C_{5,\mathrm{rat}}
  ={2263404122555368590593580404287
   \over8177706222298165502582585481000},
  \]
  and the exact comparison and liminf bounds (CR28dz2)--(CR28dz3). Its
  original derivation is a fixed-parameter consequence rather than a global
  optimization. The later compact theorem (CR28dz20)--(CR28dz42) optimizes
  all eleven continuous parameters, audits all 21 clipping regimes and every
  compact face, and proves the unique strict all-middle coefficient
  \(C_{5,*}>C_{5,\mathrm{rat}}>C_{4,*}\). Thus \(C_{5,*}\) remains the
  exact optimum of the fixed \(k=5\) template, while (CR28dw9) is the stronger
  all-fixed-\(k\) lower coefficient.
  The exact finite specialization (CR28dz4)--(CR28dz19) retains all four
  parameter families unchanged. Its minimal uniform threshold is \(234\),
  its literal and integer-closed bounds are \(\mathcal B_{5,n}\) and
  \(\mathcal I_{5,n}\), and its exact rounded remainder proves
  \(\Lambda_n>C_{5,\mathrm{rat}}n^3\) throughout the domain. This supplies
  no finite rounding at the irrational optimizer, growing-\(k\) passage,
  true residual, convergence theorem, or geometric leading constant.
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

## 15. Exact \(K\) For The Explicit PG49-Star Core Order

Retain the symbolic scaffold on

\[
n=10m+3,\qquad m\ge3,\qquad d=8m+4,\qquad v=2m,
\]

with terminals, low labels, and oriented paths

\[
E_j=d+j,\qquad
\lambda_j=4m-2j,\qquad
\rho_j=4m+1-2j,
\tag{KPGSTAR-1}
\]

\[
P_k=(A_k,c_k,b_k)
=(8m+3-2k,\ 4m+2+k,\ 8m+2-2k)
\quad(0\le k\le m),
\]

\[
P_k=(x_k)=(4m+2+k)
\quad(m+1\le k\le2m-1).
\tag{KPGSTAR-2}
\]

Let \(\alpha_*\) be the relation-compatible bijection (PG110), put

\[
q=\left\lfloor{4m+3\over5}\right\rfloor,
\qquad
\tau_m^*=\sigma_{\alpha_*},
\]

and define the proposed backbone and its low complement by

\[
B_m=\{4m+1,\ldots,10m+3\},
\qquad
H_m=\{2,\ldots,4m\}.
\]

The exact theorem is

\[
\boxed{
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}
P_{\tau_m^*}(U)=\{B_m\}.
}
\tag{KPGSTAR-3}
\]

Thus the maximizer is unique on every admitted row. Its value is

\[
\boxed{
K(\tau_m^*)=P_{\tau_m^*}(B_m)
={1714m^3+1863m^2+24mq+617m+12q^2+48q+66\over6}.
}
\tag{KPGSTAR-4}
\]

We prove the maximizer classification first, without using (KPGSTAR-4) as a
surrogate for the shortcut audit.

### Complete deletion-gain audit

Every member of \(H_m\) is isolated between two members of \(B_m\). After
deleting those low labels, the cyclic backbone is

\[
\boxed{
\left(
L,
(E_j,P_j)_{j=0}^{q-1},
(E_j,P_{j+1})_{j=q}^{m-1},
(E_j,x_{3m-1-j})_{j=m}^{2m-2},
E_{2m-1},P_q
\right),
\qquad L=4m+1.
}
\tag{KPGSTAR-5}
\]

Each indexed block is concatenated in increasing \(j\), every path is
expanded in its displayed orientation, and an empty range contributes
nothing. In particular, (KPGSTAR-5) remains literal when \(m=3\) and
\(q=m\).

For a low label \(z\) between backbone neighbors \(a,b\), use the deletion
gain

\[
h_z=ab-z(a+b).
\tag{KPGSTAR-6}
\]

There are exactly seven position classes. The first six are the left and
right holes in the three nonclosing assignment blocks; the last is the sole
closing hole \(\lambda_{2m-1}=2\):

\[
\begin{array}{c|c|c}
\text{hole}&\text{gap range}&h_z\\ \hline
\lambda_j&0\le j<q&
-4j^2+(28m+9)j+28m+12\\
\rho_{j+1}&0\le j<q&
-4j^2+(28m+5)j+44m+17\\
\lambda_j&q\le j\le m-1&
-4j^2+(28m+3)j+20m+4\\
\rho_{j+1}&q\le j\le m-1&
-4j^2+(28m-1)j+36m+5\\
\lambda_j&m\le j\le2m-2&
-j^2+(29m+7)j-4m^2+16m+4\\
\rho_{j+1}&m\le j\le2m-2&
-j^2+(29m+8)j-4m^2+34m+11\\
\lambda_{2m-1}=2&&
80m^2-(20m+2)q+18m-3.
\end{array}
\tag{KPGSTAR-7}
\]

The four triple expressions and the two singleton expressions have forward
differences, in the same order,

\[
28m+5-8j,\quad28m+1-8j,\quad
28m-1-8j,\quad28m-5-8j,\quad
29m+6-2j,\quad29m+7-2j.
\tag{KPGSTAR-8}
\]

Each is positive throughout its displayed range. The first two classes have
respective minima \(28m+12\) and \(44m+17\) at \(j=0\). If the shifted
triple range is nonempty, then \(m\ge4\), \(q\ge3\), and its two left-end
values exceed \(28m+12\). Indeed, subtracting that value from the shifted
left gain gives at least \(64m+1\), while the shifted right gain gives at
least \(79m-7\), using \(-4q^2\ge-4mq\), \(q\ge3\), and \(q\le m\).
The singleton classes begin at

\[
24m^2+23m+4,\qquad24m^2+42m+11.
\]

Finally, the closing value exceeds \(28m+12\), since

\[
80m^2-(20m+2)q+18m-3-(28m+12)
\ge60m^2-12m-15>0.
\]

Consequently every low deletion is strictly profitable, and the complete
minimum is

\[
\boxed{
\min_{z\in H_m}h_z=28m+12>0,
}
\tag{KPGSTAR-9}
\]

attained only at \(\lambda_0=4m\). Equation (KPGSTAR-7) treats the cyclic
closing hole separately; no nonclosing right-hole formula has been extended
through the cut.

### Complete compressed-shortcut audit

Apply the exact arc identity (K825-8). After deleting only the internal
members of \(H_m\) from an oriented arc, write its compressed path as

\[
C=(z_0,z_1,\ldots,z_s),\qquad s\ge2,
\]

and put

\[
M(C)=\sum_{i=0}^{s-1}z_i z_{i+1}-z_0z_s.
\tag{KPGSTAR-10}
\]

We prove \(M(C)>0\) in every endpoint and length class.

If an endpoint, say \(a\), is a low label, every internal vertex is in
\(B_m\) and is therefore at least \(L\). Writing the other endpoint as
\(b\), the two boundary edges already give

\[
M(C)\ge L(a+b)-ab=La+(L-a)b
\ge4L-4=16m>12m+4.
\tag{KPGSTAR-11}
\]

The rectangle is \(2\le a\le L-1\), \(2\le b\le n\); checking its four
corners gives the displayed minimum. The argument also covers two low
endpoints and every orientation.

It remains to take both endpoints \(a,b\) in \([L,n]\). First suppose
\(s=2\), with middle label \(y\). Every possible middle role is one of the
following.

For a triple connector \(c_k\), \(0\le k\le m\), its neighbors remain
\(A_k,b_k\), and

\[
c_k(A_k+b_k)-A_kb_k
=12m+4+(32m+7)k-8k^2.
\tag{KPGSTAR-12}
\]

Its forward difference is \(32m-16k-1>0\) on the displayed range, so its
minimum is \(12m+4\) at \(c_0\). For a reversed singleton gap, write
\(j=m+t\), \(0\le t\le m-2\). Then
\(x_{3m-1-j}=6m+1-t\), and its exact terminal-to-terminal margin is

\[
\begin{aligned}
&x_{3m-1-j}(E_j+E_{j+1})-E_jE_{j+1}\\
&\qquad={}
27m^2-24mt-9m-3t^2-16t-11
\ge35m+9.
\end{aligned}
\tag{KPGSTAR-13}
\]

The polynomial decreases in \(t\), so the last value \(t=m-2\) gives the
displayed minimum. The closing backbone label \(L=\rho_0\) lies literally
between \(b_q\) and \(E_0\). Its exact margin is

\[
L(b_q+E_0)-b_qE_0
=2\bigl((4m+3)q-4m-1\bigr)
\ge16m+16,
\tag{KPGSTAR-14}
\]

using \(q\ge3\). This is the second, distinct role of the cyclic closure;
the closing low gain was already (KPGSTAR-7).

The remaining two-edge middle roles are outer triple labels and terminals;
they satisfy \(y\ge(n+1)/2=5m+2\). More generally, for any such integer
middle label,

\[
y(a+b)-ab=y^2-(a-y)(b-y)
\ge
\begin{cases}
(3n-1)/2=15m+4,&a,b>y,\\
(2L+1)(n+1)/2-L(L+1)=24m^2+19m+4,&a,b<y,\\
y^2,&a<y<b\text{ or }b<y<a.
\end{cases}
\tag{KPGSTAR-15}
\]

Distinctness of the two endpoints gives the first two corner bounds. Every
entry is strictly larger than \(12m+4\). Equations
(KPGSTAR-12)--(KPGSTAR-15) therefore exhaust all two-edge middle labels and
prove that their exact global minimum is \(12m+4\), attained at
\((A_0,c_0,b_0)\).

For \(s=3\), every adjacent pair of internal backbone labels contains one
label at least

\[
R=6m+2,
\qquad R+L=n,
\tag{KPGSTAR-16}
\]

while the other is at least \(L\). This follows block by block: a terminal
is larger than \(R\); each internal triple edge contains \(A_k\ge6m+3\) or
\(b_k\ge6m+2\); a singleton is flanked by terminals; and the two cyclic
edges are \(b_qL\) and \(LE_0\), with
\(b_q=8m+2-2q\ge R\). Orienting the internal pair so the first label is at
least \(R\), or reversing the path, gives

\[
M(C)\ge aR+RL+Lb-ab\ge RL
=24m^2+14m+2>12m+4.
\tag{KPGSTAR-17}
\]

The second inequality is the four-corner minimum of
\(aR+Lb-ab\) on \([L,n]^2\), using \(R+L=n\).

Finally, for every \(s\ge4\), all internal labels are at least \(L\), so

\[
\begin{aligned}
M(C)
&\ge L(a+b)+(s-2)L^2-ab\\
&\ge2Ln+2L^2-n^2+(s-4)L^2\\
&=12m^2-1+(s-4)L^2>12m+4.
\end{aligned}
\tag{KPGSTAR-18}
\]

Again the bilinear minimum is at the corners of \([L,n]^2\). The cyclic
backbone in (KPGSTAR-5), including both edges through \(L\), is used in
(KPGSTAR-16); hence (KPGSTAR-11)--(KPGSTAR-18) cover every oriented arc,
not only arcs inside the displayed linear cut. We have proved

\[
\boxed{
\min_{C:\,s\ge2}M(C)=12m+4>0,
}
\tag{KPGSTAR-19}
\]

with equality exactly on the forward compressed arc
\((A_0,c_0,b_0)\) in the displayed cyclic orientation. Its reversal appears
only after reflecting the entire cyclic representative; it is not a second
forward arc of the fixed presentation.

The positive gains (KPGSTAR-9), strict shortcuts (KPGSTAR-19), and exact
identity (K825-8)--(K825-9) now apply without subset enumeration. Equality
forces every member of \(H_m\) to be omitted and every selected gap to be a
single backbone edge. Thus \(B_m\) is the unique maximizer among subsets of
cardinality at least two. It dominates the two-label subset
\(\{n-1,n\}\), whose score is \(2n(n-1)>n^2\), so no singleton can tie.
This proves (KPGSTAR-3), including all equality cases.

### Exact block sum and the five residue classes

For a nonempty path \(P=(p_1,\ldots,p_s)\), put

\[
\mathcal C(x,P,y)=xp_1+
\sum_{i=1}^{s-1}p_ip_{i+1}+p_sy.
\]

Reading (KPGSTAR-5) from \(L\), its score is

\[
\begin{aligned}
P_{\tau_m^*}(B_m)={}&LE_0
+\sum_{j=0}^{q-1}\mathcal C(E_j,P_j,E_{j+1})\\
&+\sum_{j=q}^{m-1}\mathcal C(E_j,P_{j+1},E_{j+1})\\
&+\sum_{j=m}^{2m-2}
  x_{3m-1-j}(E_j+E_{j+1})
+\mathcal C(E_{2m-1},P_q,L).
\end{aligned}
\tag{KPGSTAR-20}
\]

The three repeated summands and the closing term are

\[
\begin{aligned}
\mathcal C(E_j,P_j,E_{j+1})
&=-8j^2-16mj-16j+192m^2+164m+32,\\
\mathcal C(E_j,P_{j+1},E_{j+1})
&=-8j^2-16mj-28j+192m^2+132m+7,\\
x_{3m-1-j}(E_j+E_{j+1})
&=-2j^2-2mj-7j+112m^2+79m+9,\\
\mathcal C(E_{2m-1},P_q,L)
&=176m^2-28mq+122m-4q^2-11q+21.
\end{aligned}
\tag{KPGSTAR-21}
\]

Using the standard sums of \(j\) and \(j^2\) on the exact ranges in
(KPGSTAR-20) gives (KPGSTAR-4). This also covers the empty shifted range at
\(m=3\); there is no boundary correction.

For the requested five branches, retain \(c_r\) from (PG111). Direct
substitution of \(q=(4m+c_r)/5\) gives

\[
K(\tau_m^*)
={42850m^3+47247m^2+(16385+216c_r)m
  +1650+240c_r+12c_r^2\over150}.
\tag{KPGSTAR-22}
\]

Equivalently,

\[
\begin{array}{c|c|c}
r=m\bmod5&q&150K(\tau_m^*)\\ \hline
0&4m/5&42850m^3+47247m^2+16385m+1650\\
1&(4m+1)/5&42850m^3+47247m^2+16601m+1902\\
2&(4m+2)/5&42850m^3+47247m^2+16817m+2178\\
3&(4m+3)/5&42850m^3+47247m^2+17033m+2478\\
4&(4m-1)/5&42850m^3+47247m^2+16169m+1422.
\end{array}
\tag{KPGSTAR-23}
\]

Every displayed numerator is divisible by \(150\) on its stated residue
class because it equals the integer score in (KPGSTAR-20). Since
\(n=10m+3\), all five branches have the exact fixed-order coefficient

\[
\boxed{
K(\tau_m^*)={857\over3}m^3+O(m^2)
={857\over3000}n^3+O(n^2).
}
\tag{KPGSTAR-24}
\]

This proves the proposed coefficient for this family; it is not imported
from the different residue-one construction (KR1-1).

### Exact comparison with K825 and both PG46 orders

On the same \(n=10m+3\) rows, the retained exact values are

\[
\begin{aligned}
K_{825}(m)&={572m^3+629m^2+235m+30\over2},\\
K_{\rm cl}(m)&={572m^3+631m^2+223m+22\over2},\\
K_{\rm pre}(m)&={572m^3+631m^2+235m+22\over2}.
\end{aligned}
\tag{KPGSTAR-25}
\]

Subtracting them from (KPGSTAR-4) gives

\[
\begin{aligned}
K(\tau_m^*)-K_{825}(m)
&={-m^3-12m^2+12mq-44m+6q^2+24q-12\over3},\\
K(\tau_m^*)-K_{\rm cl}(m)
&={-m^3-15m^2+12mq-26m+6q^2+24q\over3},\\
K(\tau_m^*)-K_{\rm pre}(m)
&={-m^3-15m^2+12mq-44m+6q^2+24q\over3}.
\end{aligned}
\tag{KPGSTAR-26}
\]

The comparison has no hidden crossover. Since \(q\le m\), three times the
respective differences are at most

\[
\begin{aligned}
&-m^3+6m^2-20m-12<0,\\
&-m^3+3m^2-2m=-m(m-1)(m-2)<0,\\
&-m^3+3m^2-20m=-m(m^2-3m+20)<0.
\end{aligned}
\tag{KPGSTAR-27}
\]

For the first line, its negative is
\((m-3)^3+3(m-3)^2+11(m-3)+45>0\). Therefore the PG49-star value is
strictly below all three comparators for every \(m\ge3\), with no tie. At
the minimum row,

\[
\alpha_*=(0,1,2,5,4,3),
\qquad
\boxed{10905<10907<10920<10925},
\tag{KPGSTAR-28}
\]

where the four values are respectively PG49-star, closing PG46, K825, and
preclosing PG46. Combining (KPG46-19) and (KPG46P-18), the complete ordering
is PG49-star \(<\) closing PG46 \(<\) K825 \(<\) preclosing PG46 for
\(3\le m\le6\), and PG49-star \(<\) K825 \(<\) closing PG46 \(<\)
preclosing PG46 for \(m\ge7\). Relative to each comparator, the leading
difference is \(-n^3/3000+O(n^2)\).

The sole diagnostic for (PG110)--(PG114) and
(KPGSTAR-1)--(KPGSTAR-28) is the standalone standard-library script
`ops/TASK-20260719__explicit_pg49_star_exact_k/exact_diagnostic.py`. It
constructs only the displayed assignment. On \(m=3,\ldots,30\), its direct
increasing-path max-plus scorer checks uniqueness and every proper oriented
arc, hence every nontrivial compressed shortcut, including paths crossing
the cyclic cut; lighter exact formula and Ferrers checks extend through
\(m=1000\). It enumerates no subset, path permutation, or matching. These
bounded rows corroborate the symbolic proof and do not extend its scope.

All results in this section concern \(K\) on one explicit cyclic core-order
family. They give no exact angular threshold, geometric feasibility or
optimality statement, global \(K\)-minimizer classification, or equality
with \(\Lambda_n\). In particular, the coefficient in (KPGSTAR-24) is a
fixed-family subsequential coefficient only.

## 16. Exact \(K\) For The Monotone Threshold-Closing PG46 Shift

Retain the scaffold (KPGSTAR-1)--(KPGSTAR-2) on

\[
n=10m+3,\qquad m\ge3,\qquad d=8m+4,\qquad v=2m,
\]

and put

\[
q=\left\lfloor{4m+3\over5}\right\rfloor
=\kappa_{2m-1}.
\]

Specialize the interval shift (PG46) to the closing target
\((q,2m-1)\). Explicitly,

\[
\boxed{
\alpha_m^\uparrow(j)=
\begin{cases}
j,&0\le j<q,\\
j+1,&q\le j\le2m-2,\\
q,&j=2m-1.
\end{cases}}
\tag{KPG46Q-1}
\]

Thus \(P_q\) occupies the cyclic closing gap and all other paths occur in
increasing path-index order. Since the target is exactly the final Ferrers
threshold, (PG46)--(PG49) already prove that this is a relation-compatible
bijection. Let \(\tau_m^\uparrow=\sigma_{\alpha_m^\uparrow}\). The present
section evaluates the distinct induced-subset objective \(K\); it does not
infer that evaluation from Ferrers compatibility or from \(W\).

Put

\[
L=4m+1,\qquad
B_m=\{L,L+1,\ldots,n\},\qquad
H_m=\{2,3,\ldots,4m\}.
\]

Every member of \(H_m\) is isolated between two members of \(B_m\).
Deleting those holes gives the cyclic backbone

\[
\boxed{
\left(
L,
(E_j,P_j)_{j=0}^{q-1},
(E_j,P_{j+1})_{j=q}^{m-1},
(E_j,x_{j+1})_{j=m}^{2m-2},
E_{2m-1},P_q
\right).
}
\tag{KPG46Q-2}
\]

Every indexed block is concatenated in increasing \(j\), every triple is
expanded in its retained orientation, and an empty range contributes
nothing. The exact maximizing-subset classification is

\[
\boxed{
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}
P_{\tau_m^\uparrow}(U)=\{B_m\}.
}
\tag{KPG46Q-3}
\]

In particular, the displayed singleton is the complete list of maximizing
subsets. Its value is

\[
\boxed{
K(\tau_m^\uparrow)
={572m^3+619m^2+8mq+207m+4q^2+16q+22\over2}.
}
\tag{KPG46Q-4}
\]

We first prove (KPG46Q-3), independently of the block sum.

### Exhaustive deletion gains

For a hole \(z\) between its two backbone neighbors \(a,b\), write

\[
h_z=ab-z(a+b).
\tag{KPG46Q-5}
\]

Direct substitution in (KPG46Q-2) gives exactly seven position classes:

\[
\begin{array}{c|c|c}
\text{hole}&\text{gap range}&h_z\\ \hline
\lambda_j&0\le j<q&
-4j^2+(28m+9)j+28m+12\\
\rho_{j+1}&0\le j<q&
-4j^2+(28m+5)j+44m+17\\
\lambda_j&q\le j\le m-1&
-4j^2+(28m+3)j+20m+4\\
\rho_{j+1}&q\le j\le m-1&
-4j^2+(28m-1)j+36m+5\\
\lambda_j&m\le j\le2m-2&
5j^2+(28m+21)j-16m^2+12m+12\\
\rho_{j+1}&m\le j\le2m-2&
5j^2+(28m+26)j-16m^2+24m+23\\
\lambda_{2m-1}=2&&
80m^2-(20m+2)q+18m-3.
\end{array}
\tag{KPG46Q-6}
\]

The six ranged classes contain
\(2q+2(m-q)+2(m-1)=4m-2\) holes; the closing row supplies the last one,
so (KPG46Q-6) accounts for all \(|H_m|=4m-1\) holes. In particular,
\(\rho_0=L\) is correctly retained and is not counted as a hole.

The forward differences of the six polynomials, in table order, are

\[
28m+5-8j,\quad28m+1-8j,\quad
28m-1-8j,\quad28m-5-8j,\quad
10j+28m+26,\quad10j+28m+31.
\tag{KPG46Q-7}
\]

They are positive on their displayed ranges. The first two left-end values
are \(28m+12\) and \(44m+17\). If the shifted-triple range is nonempty,
then \(m\ge4\), \(q\ge3\), and \(q\le m\); subtracting \(28m+12\) from
its two left-end values gives the respective lower bounds
\(64m+1\) and \(80m-10\). The two singleton ranges begin at

\[
17m^2+33m+12,\qquad17m^2+50m+23.
\]

Finally, the closing excess satisfies

\[
h_{\lambda_{2m-1}}-(28m+12)
=80m^2-(20m+2)q-10m-15
\ge60m^2-12m-15>0.
\tag{KPG46Q-8}
\]

Consequently every low deletion is strictly profitable and

\[
\boxed{
\min_{z\in H_m}h_z=28m+12>0,
}
\tag{KPG46Q-9}
\]

with equality only at \(\lambda_0=4m\). The last row of (KPG46Q-6) is the
literal cyclic closing gain; no nonclosing right-hole formula has been
continued through the cut.

### Complete compressed-shortcut audit

Apply the shortcut-budget identity (K825-6)--(K825-9). After deleting only
the internal holes from an oriented arc, write the resulting compressed path
as

\[
C=(z_0,z_1,\ldots,z_s),\qquad s\ge2,
\]

and put

\[
M(C)=\sum_{i=0}^{s-1}z_i z_{i+1}-z_0z_s.
\tag{KPG46Q-10}
\]

If an endpoint \(a\) is a hole, every internal vertex is at least \(L\).
For the other endpoint \(b\), the two boundary edges give

\[
M(C)\ge L(a+b)-ab=La+(L-a)b
\ge4L-4=16m>12m+4.
\tag{KPG46Q-11}
\]

This covers one or two low endpoints in either orientation. It remains to
take both endpoints in \([L,n]\).

For \(s=2\), all possible middle roles split as follows. A triple connector
\(c_k\), \(0\le k\le m\), remains between \(A_k,b_k\), and has margin

\[
c_k(A_k+b_k)-A_kb_k
=12m+4+(32m+7)k-8k^2.
\tag{KPG46Q-12}
\]

Its forward difference is \(32m-16k-1>0\), so the minimum is
\(12m+4\), uniquely at \(c_0\). A monotone singleton \(x_{j+1}\),
\(m\le j\le2m-2\), lies between \(E_j,E_{j+1}\), with exact margin

\[
x_{j+1}(E_j+E_{j+1})-E_jE_{j+1}
=j^2+(8m+6)j+12m+7
\ge9m^2+18m+7.
\tag{KPG46Q-13}
\]

The retained closing label \(L=\rho_0\) lies literally between
\(b_q,E_0\), and its distinct margin is

\[
L(b_q+E_0)-b_qE_0
=2\bigl((4m+3)q-4m-1\bigr)
\ge16m+16,
\tag{KPG46Q-14}
\]

using \(q\ge3\).

The remaining middle roles are outer triple labels and terminals; together
with the singletons, they all satisfy \(y\ge(n+1)/2=5m+2\). For any such
integer middle label, distinct endpoints and

\[
y(a+b)-ab=y^2-(a-y)(b-y)
\]

give, according as both endpoints are above \(y\), below \(y\), or on
opposite sides, the respective lower bounds

\[
{3n-1\over2}=15m+4,\qquad
(2L+1){n+1\over2}-L(L+1)=24m^2+19m+4,\qquad y^2.
\tag{KPG46Q-15}
\]

The connectors, \(L\), outer triple labels, terminals, and singletons count
\((m+1)+1+2(m+1)+2m+(m-1)=6m+3=|B_m|\) middle roles, so no two-edge role
is omitted. Equations (KPG46Q-12)--(KPG46Q-15) prove that the exact
two-edge minimum is \(12m+4\), uniquely on the forward compressed path
\((A_0,c_0,b_0)\).

For \(s=3\), every consecutive pair of internal backbone labels contains a
label at least

\[
R=6m+2,\qquad R+L=n,
\]

and its other label is at least \(L\). Inside each triple one member of
every adjacent pair is an outer label at least \(R\); every ordinary block
join contains a terminal
\(E_j\ge d>R\); every monotone singleton is flanked by terminals; and the
cyclic edges are \(b_qL\) and \(LE_0\), where \(b_q\ge R\) and
\(E_0\ge R\). Orienting
the internal pair with the \(R\)-bounded label first, or exchanging the two
endpoints, gives

\[
M(C)\ge aR+RL+Lb-ab\ge RL
=24m^2+14m+2>12m+4.
\tag{KPG46Q-16}
\]

The second inequality is the four-corner minimum on \([L,n]^2\). For every
\(s\ge4\), the uniform internal lower bound \(L\) instead gives

\[
\begin{aligned}
M(C)
&\ge L(a+b)+(s-2)L^2-ab\\
&\ge2Ln+2L^2-n^2+(s-4)L^2\\
&=12m^2-1+(s-4)L^2>12m+4.
\end{aligned}
\tag{KPG46Q-17}
\]

The full compressed closing word is
\(E_{2m-1},A_q,c_q,b_q,L,E_0\). Thus (KPG46Q-14) separately checks the
two-edge role through \(L\), (KPG46Q-16) checks both closing backbone
edges, and (KPG46Q-17) covers every longer arc across the cyclic cut.
Together with the distinct closing-hole gain (KPG46Q-8), this exhausts
cyclic closure. We have proved

\[
\boxed{
\min_{C:\,s\ge2}M(C)=12m+4>0,
}
\tag{KPG46Q-18}
\]

with equality only on \((A_0,c_0,b_0)\) in the fixed forward cyclic
orientation.

The strict deletion gains (KPG46Q-9), strict shortcut audit
(KPG46Q-18), and exact lemma (K825-6)--(K825-9) prove that \(B_m\) is the
unique maximizer among subsets of cardinality at least two. The same lemma
compared with \(\{n-1,n\}\) gives
\(P_{\tau_m^\uparrow}(B_m)\ge2n(n-1)>n^2\), so no singleton can tie. This
proves (KPG46Q-3), including every equality case.

### Exact block sum and five residue classes

Using \(\mathcal C\) from (KPG46-15), the backbone score is

\[
\begin{aligned}
P_{\tau_m^\uparrow}(B_m)={}&LE_0
+\sum_{j=0}^{q-1}\mathcal C(E_j,P_j,E_{j+1})\\
&+\sum_{j=q}^{m-1}\mathcal C(E_j,P_{j+1},E_{j+1})\\
&+\sum_{j=m}^{2m-2}x_{j+1}(E_j+E_{j+1})
+\mathcal C(E_{2m-1},P_q,L).
\end{aligned}
\tag{KPG46Q-19}
\]

The four repeated summands are

\[
\begin{aligned}
\mathcal C(E_j,P_j,E_{j+1})
&=-8j^2-16mj-16j+192m^2+164m+32,\\
\mathcal C(E_j,P_{j+1},E_{j+1})
&=-8j^2-16mj-28j+192m^2+132m+7,\\
x_{j+1}(E_j+E_{j+1})
&=2j^2+24mj+15j+64m^2+84m+27,\\
\mathcal C(E_{2m-1},P_q,L)
&=176m^2-28mq+122m-4q^2-11q+21.
\end{aligned}
\tag{KPG46Q-20}
\]

Summing \(j\) and \(j^2\) on the exact ranges in (KPG46Q-19) gives
(KPG46Q-4) directly. Put

\[
q={4m+c_r\over5},
\qquad(c_0,c_1,c_2,c_3,c_4)=(0,1,2,3,-1),
\qquad r=m\bmod5.
\]

Then the exact five-branch expression is

\[
K(\tau_m^\uparrow)
={14300m^3+15699m^2+(5495+72c_r)m
  +550+80c_r+4c_r^2\over50},
\tag{KPG46Q-21}
\]

or, explicitly,

\[
\begin{array}{c|c|c}
r&q&50K(\tau_m^\uparrow)\\ \hline
0&4m/5&14300m^3+15699m^2+5495m+550\\
1&(4m+1)/5&14300m^3+15699m^2+5567m+634\\
2&(4m+2)/5&14300m^3+15699m^2+5639m+726\\
3&(4m+3)/5&14300m^3+15699m^2+5711m+826\\
4&(4m-1)/5&14300m^3+15699m^2+5423m+474.
\end{array}
\tag{KPG46Q-22}
\]

Each numerator is divisible by \(50\) on its stated residue class because
it equals the integer block score (KPG46Q-19). Since \(n=10m+3\),

\[
\boxed{
K(\tau_m^\uparrow)=286m^3+O(m^2)
={143\over500}n^3+O(n^2).
}
\tag{KPG46Q-23}
\]

### Exact comparisons and the singleton-inversion contribution

The PG49-star order (PG110) and the monotone order (KPG46Q-1) agree in
every block except the singleton gaps \(m\le j\le2m-2\). The monotone
assignment uses \(x_{j+1}=4m+j+3\), while PG49-star uses
\(x_{3m-1-j}=7m+1-j\). Therefore direct edge cancellation gives

\[
\begin{aligned}
K(\tau_m^\uparrow)-K(\tau_m^*)
&=\sum_{j=m}^{2m-2}
 (2j-3m+2)(16m+9+2j)\\
&={m(m-1)(m-2)\over3}
={ (n-3)(n-13)(n-23)\over3000}>0.
\end{aligned}
\tag{KPG46Q-24}
\]

The individual summands in (KPG46Q-24) have mixed signs; it is their exact
aggregate, not a gapwise improvement, that is positive. At \(m=3\) the
gain is already \(2\).

Against the three retained coefficient-\(143/500\) comparators, exact
subtraction gives

\[
\begin{aligned}
K(\tau_m^\uparrow)-K_{825}(m)
&=2q^2+4mq+8q-5m^2-14m-4,\\
K(\tau_m^\uparrow)-K_{\rm cl}(m)
&=-2(m-q)(3m+q+4),\\
K(\tau_m^\uparrow)-K_{\rm pre}(m)
&=-2(m-q)(3m+q+4)-6m.
\end{aligned}
\tag{KPG46Q-25}
\]

The first expression is increasing in \(q\), and
\(q\le(4m+3)/5\), so

\[
K(\tau_m^\uparrow)-K_{825}(m)
\le{-13m^2-82m+38\over25}<0.
\tag{KPG46Q-26}
\]

Also \(q\le m\), with equality exactly at \(m=3\): for \(m>3\), the
unfloored quotient \((4m+3)/5\) is already smaller than \(m\). Hence the
second line of (KPG46Q-25) is zero only at \(m=3\) and is otherwise
negative; the third is always negative. Combining these signs with
(KPG46-19) and (KPG46P-18) yields the complete ordering

\[
K_\uparrow:=K(\tau_m^\uparrow),
\qquad
K_*:=K(\tau_m^*),
\]

where every comparator below is evaluated on the same row \(m\):

\[
\boxed{
\begin{array}{ll}
m=3:&K_*<K_\uparrow=K_{\rm cl}<K_{825}<K_{\rm pre},\\
4\le m\le6:&K_*<K_\uparrow<K_{\rm cl}<K_{825}<K_{\rm pre},\\
m\ge7:&K_*<K_\uparrow<K_{825}<K_{\rm cl}<K_{\rm pre}.
\end{array}}
\tag{KPG46Q-27}
\]

At the minimum row, \(q=m=3\), the shifted-triple range in
(KPG46Q-2) is empty but the two-element singleton block is not. Here

\[
\alpha_3^\uparrow=(0,1,2,4,5,3),
\qquad
\boxed{
K_*=10905<K_\uparrow=K_{\rm cl}=10907<K_{825}=10920<K_{\rm pre}=10925
},
\tag{KPG46Q-28}
\]

Thus the monotone order literally coincides with closing PG46 only on this
row. Its unique maximizer is
\(B_3=\{13,\ldots,33\}\), and its minimum deletion and shortcut margins
are \(96\) and \(40\), so no minimum-row exception is hidden.

Finally, for each comparator
\(C\in\{K_{825},K_{\rm cl},K_{\rm pre}\}\), with \(C(m)\) denoting its
value on the current row, (KPG46Q-24) gives the exact decomposition

\[
C(m)-K(\tau_m^*)
=\bigl(C(m)-K(\tau_m^\uparrow)\bigr)
+{m(m-1)(m-2)\over3}.
\tag{KPG46Q-29}
\]

The monotone threshold-closing order already weakly improves all three
comparators: strictly for K825 and preclosing on every row, strictly for
closing when \(m\ge4\), and with equality to closing at \(m=3\). These
gains are only \(O(n^2)\), as (KPG46Q-25) shows. The reversed singleton
block contributes exactly

\[
{(n-3)(n-13)(n-23)\over3000}
={n^3\over3000}+O(n^2),
\]

and therefore accounts for the entire cubic improvement from
\(858/3000=143/500\) to the PG49-star coefficient \(857/3000\). This is an
aggregate statement about the two fixed induced-\(K\) scores, not a claim
that each reversed singleton gap improves separately.

The sole diagnostic for (KPG46Q-1)--(KPG46Q-29) is the standalone
standard-library script
`ops/TASK-20260719__pg46_threshold_closing_exact_k/exact_diagnostic.py`.
It constructs only (KPG46Q-1). On \(m=3,\ldots,30\), an independent
increasing-path max-plus recurrence checks the unique maximizing subset, and
an all-oriented-arc scan checks every isolated-hole gain and every
nontrivial compressed shortcut, including cyclic-cut arcs. Lighter exact
formula, Ferrers, residue, inversion, and comparator checks continue through
\(m=1000\). It enumerates no subset, path permutation, matching, or family
of cyclic orders. The bounded computation corroborates the symbolic proof
and does not extend its scope.

All results in this section concern \(K\) on one prescribed cyclic core
order. They imply no exact angular-threshold comparison, geometric result,
global \(K\)-minimality, or minimizing-order classification.

## 17. Exact \(K\) For The Odd-\(v\) PG49-Star Parity Core Order

Retain exactly the scaffold, paths, and a-priori map (PGODD-1)--(PGODD-6):

\[
n=10m+8,\qquad m\ge1,\qquad d=8m+8,\qquad
q=\left\lfloor{4m+5\over5}\right\rfloor.
\]

With \(j^+=j+1\pmod{2m+1}\), reconstruct the fixed cyclic core order as

\[
\boxed{
\tau_m^\circ
=\mathop{\bigcirc}_{j=0}^{2m}
 (E_j,\lambda_j,P_{\alpha^\circ(j)},\rho_{j^+}) .}
\tag{KPGODD-1}
\]

The concatenation starts at \(E_0\), each path is expanded in its orientation
from (PGODD-3), and the final \(\rho_0\) closes back to \(E_0\). Thus
(KPGODD-1), rather than a reordered surrogate, is the core whose induced
subsets are evaluated below. Put

\[
L=4m+3,\qquad
H_m=\{2,\ldots,4m+2\},\qquad
B_m=\{L,\ldots,10m+8\}.
\tag{KPGODD-2}
\]

The exact all-domain theorem is

\[
\boxed{
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}
 P_{\tau_m^\circ}(U)=\{B_m\}.}
\tag{KPGODD-3}
\]

In particular, the maximizer is unique for every \(m\ge1\). Its score is

\[
\boxed{
K(\tau_m^\circ)
={1714m^3+4467m^2+24mq+3749m+12q^2+60q+1032\over6}.}
\tag{KPGODD-4}
\]

We first prove (KPGODD-3), including all equality and boundary cases, without
using the value (KPGODD-4) as a substitute for the shortcut audit.

### Exact compressed backbone

Every label in \(H_m\) is isolated between two members of \(B_m\). Deleting
all of them from (KPGODD-1) gives, starting at \(L=\rho_0\), the cyclic word

\[
\boxed{
\left(
L,
(E_j,P_j)_{j=0}^{q-1},
(E_j,P_{j+1})_{j=q}^{m-1},
E_m,a,b,
(E_j,x_{3m+1-j})_{j=m+1}^{2m-1},
E_{2m},P_q
\right).}
\tag{KPGODD-5}
\]

All indexed blocks are concatenated in increasing \(j\), and every displayed
path is expanded. Empty ranges are literal: the shifted-triple block is
empty exactly when \(q=m\), hence for \(1\le m\le5\); the singleton block is
empty at \(m=1\) and has one member at \(m=2\). The doubleton
\((a,b)=(5m+5,5m+6)\) is always present and retains its orientation.

### Complete elimination-gain audit

For a hole \(z\in H_m\) between backbone neighbors \(u,w\), let

\[
h_z=uw-z(u+w).
\tag{KPGODD-6}
\]

The nine exhaustive position classes are

\[
\begin{array}{c|c|c}
\text{hole}&\text{gap range}&h_z\\ \hline
\lambda_j&0\le j<q&
-4j^2+(28m+23)j+28m+26\\
\rho_{j+1}&0\le j<q&
-4j^2+(28m+19)j+44m+39\\
\lambda_j&q\le j\le m-1&
-4j^2+(28m+17)j+20m+14\\
\rho_{j+1}&q\le j\le m-1&
-4j^2+(28m+13)j+36m+23\\
\lambda_m&&17m^2+31m+14\\
\rho_{m+1}&&17m^2+55m+39\\
\lambda_j&m+1\le j\le2m-1&
-j^2+(29m+26)j-4m^2+18m+20\\
\rho_{j+1}&m+1\le j\le2m-1&
-j^2+(29m+27)j-4m^2+36m+39\\
\lambda_{2m}=2&&80m^2-20mq+98m-12q+26.
\end{array}
\tag{KPGODD-7}
\]

The middle two rows are precisely the left and right holes of the doubleton.
The last row is the genuine closing hole between \(E_{2m}=n\) and \(A_q\);
no off-cut right-hole formula has been extended through the cyclic cut.
Their class cardinalities sum to
\[
2q+2(m-q)+2+2(m-1)+1=4m+1=|H_m|,
\]
with empty ranges interpreted literally, so no hole class is missing.

The forward differences of the four triple and two singleton polynomials,
in their displayed order, are

\[
\begin{gathered}
28m+19-8j,\quad28m+15-8j,\quad
28m+13-8j,\quad28m+9-8j,\\
29m+25-2j,\quad29m+26-2j.
\end{gathered}
\tag{KPGODD-8}
\]

They are positive on their exact ranges. The first left class therefore has
minimum \(28m+26\) at \(j=0\), while the first right class starts at
\(44m+39\). If the shifted range is nonempty, then \(m\ge6\), \(q\ge5\),
and its two left-end excesses over \(28m+26\) are bounded below by

\[
(24m+17)q-8m-12>0,\qquad
(24m+13)q+8m-3>0.
\tag{KPGODD-9}
\]

The doubleton left excess is \(17m^2+3m-12>0\), already at \(m=1\),
and its right excess is \(17m^2+27m+13>0\). When the singleton range is
nonempty, its two initial excesses factor as

\[
(m+1)(24m+19),\qquad(2m+3)(12m+13).
\tag{KPGODD-10}
\]

Finally, using \(q\le m\), the closing excess is at least

\[
80m^2-20mq+70m-12q
\ge2m(30m+29)>0.
\tag{KPGODD-11}
\]

Consequently every elimination is strictly profitable and

\[
\boxed{
\min_{z\in H_m}h_z=28m+26,}
\tag{KPGODD-12}
\]

with equality only for \(z=\lambda_0=4m+2\), between \(E_0=d\) and
\(A_0=d-1\). This includes both doubleton holes, every singleton hole, and
the literal cyclic closing hole.

### Complete compressed-shortcut audit

Apply the exact identity (K825-8). After deleting only the internal members
of \(H_m\) from an oriented arc, write the compressed path as

\[
C=(z_0,z_1,\ldots,z_s),\qquad s\ge2,\qquad
M(C)=\sum_{i=0}^{s-1}z_i z_{i+1}-z_0z_s.
\tag{KPGODD-13}
\]

We prove \(M(C)>0\) and record every case of equality in the exact minimum.
If an endpoint \(a\) is a hole, the boundary-adjacent internal vertices,
which coincide when \(s=2\), are at least \(L\). With the other endpoint
\(b\), the four corners of
\(2\le a\le L-1\), \(2\le b\le n\) give

\[
M(C)\ge L(a+b)-ab\ge4L-4=16m+8.
\tag{KPGODD-14}
\]

This also covers two low endpoints and both orientations. It remains to
take both endpoints in \(B_m=[L,n]\).

For \(s=2\), first consider a triple connector \(c_k\), \(0\le k\le m\).
Its neighbors are \(A_k,B_k\), independently of the assigned gap, and

\[
c_k(A_k+B_k)-A_kB_k
=-8k^2+(32m+23)k+12m+10.
\tag{KPGODD-15}
\]

Its forward difference is \(32m+15-16k>0\), so the unique connector minimum
is \(12m+10\) at \(c_0\).

For a reversed singleton, write \(j=m+1+t\),
\(0\le t\le m-2\). Its exact terminal-to-terminal margin is

\[
27m^2-24mt+33m-3t^2-28t+5\ge65m+49.
\tag{KPGODD-16}
\]

The expression decreases in \(t\), so equality in this class occurs only at
the final singleton. The range is empty at \(m=1\) and contains only that
endpoint at \(m=2\).

The two doubleton labels give the separate two-edge margins

\[
\begin{aligned}
a(E_m+b)-E_mb&=25m^2+46m+22,\\
b(a+E_{m+1})-aE_{m+1}&=25m^2+64m+39.
\end{aligned}
\tag{KPGODD-17}
\]

The retained closing label \(L=\rho_0\), which lies between \(B_q\) and
\(E_0\), has margin

\[
M(B_q,L,E_0)=8mq-8m+10q-6.
\tag{KPGODD-18}
\]

It equals \(4\) at \(m=1\) and \(30\) at \(m=2\). For \(m\ge3\), \(q\ge3\),
and its excess over \(12m+10\) is at least \(4m+14>0\).

The remaining possible middle roles are outer triple labels and terminals,
all at least \(6m+6\). For distinct neighbors \(a,b\in[L,n]\), the identity

\[
y(a+b)-ab=y^2-(a-y)(b-y)
\]

and the three relative-order cases give

\[
y(a+b)-ab\ge
\begin{cases}
20m^2+60m+34,&a,b>y,\\
32m^2+62m+30,&a,b<y,\\
(6m+6)^2,&\text{the endpoints straddle }y.
\end{cases}
\tag{KPGODD-19}
\]

Each bound is strictly above \(12m+10\). Equations
(KPGODD-15)--(KPGODD-19) exhaust every two-edge middle role, including both
members of the doubleton and the cyclic closing label. Indeed their counts
are
\[
(m+1)+2+(m-1)+1+2(m+1)+(2m+1)=6m+6=|B_m|
\]
for connectors, doubleton members, singletons, \(L\), outer triple labels,
and terminals, respectively.

For \(s=3\), every adjacent pair of internal backbone labels has one member
at least

\[
R=5m+6
\tag{KPGODD-20}
\]

and the other at least \(L\). This is literal on the doubleton edge because
\(b=R\); a triple edge contains an outer label at least \(6m+6\), a
singleton is flanked by terminals, and the two closing edges contain
\(B_q\ge6m+6\) or \(E_0\). The exact doubleton three-edge window is, more
strongly,

\[
M(E_m,a,b,E_{m+1})=2(m+1)(17m+26)>0.
\tag{KPGODD-21}
\]

Since \(M(C)=M(C^{\rm rev})\), reverse \(C\) if necessary so that the
\(R\)-bounded internal member comes first. The four corners of \([L,n]^2\)
then yield

\[
M(C)\ge z_0R+RL+Lz_3-z_0z_3
\ge10m^2+41m+26.
\tag{KPGODD-22}
\]

For every \(s\ge4\), all internal labels are at least \(L\), so another
four-corner calculation gives

\[
\begin{aligned}
M(C)
&\ge L(z_0+z_s)+(s-2)L^2-z_0z_s\\
&\ge12m^2+12m+2+(s-4)L^2.
\end{aligned}
\tag{KPGODD-23}
\]

The full compressed closing word is

\[
E_{2m},A_q,c_q,B_q,L,E_0.
\]

Thus (KPGODD-18) treats the retained two-edge closing role,
(KPGODD-20) and (KPGODD-22) treat both adjacent closing pairs, while
(KPGODD-23) treats every longer arc across the cut. The distinct closing
hole was already handled in the last row of (KPGODD-7). Combining all
lengths proves the exact equality classification

\[
\boxed{
\min_{C:\,s\ge2}M(C)=
\begin{cases}
4,&m=1,\quad C=(12,7,16),\\
30,&m=2,\quad C=(18,11,24),\\
12m+10,&m\ge3,\quad C=(A_0,c_0,B_0).
\end{cases}}
\tag{KPGODD-24}
\]

In each row the displayed forward arc is the unique equality arc in the
fixed cyclic presentation. Therefore the boundary change is real but affects
only the shortcut-minimum witness, not the sign needed by the proof.

The strict hole gains (KPGODD-12), strict shortcuts (KPGODD-24), and exact
identity (K825-8)--(K825-9) now force equality as follows. Every hole must be
omitted, and every selected gap must be one edge of the compressed backbone;
hence the selected subset is exactly \(B_m\). Conversely \(B_m\) attains its
backbone score. Applying the same inequality to the two-element subset
\(\{n-1,n\}\), with its product counted twice, gives
\(P_{\tau_m^\circ}(B_m)\ge2n(n-1)>n^2\), so no singleton can tie. This proves
(KPGODD-3), including the doubleton case, singleton subsets, cyclic closure,
and every equality case.

### Exact block sum and five residue classes

For a nonempty path \(P=(p_1,\ldots,p_s)\), retain

\[
\mathcal C(x,P,y)=xp_1+\sum_{i=1}^{s-1}p_ip_{i+1}+p_sy.
\]

Reading (KPGODD-5) from \(L\), the exact score is

\[
\begin{aligned}
P_{\tau_m^\circ}(B_m)={}&LE_0
+\sum_{j=0}^{q-1}\mathcal C(E_j,P_j,E_{j+1})\\
&+\sum_{j=q}^{m-1}\mathcal C(E_j,P_{j+1},E_{j+1})
+\mathcal C(E_m,(a,b),E_{m+1})\\
&+\sum_{j=m+1}^{2m-1}x_{3m+1-j}(E_j+E_{j+1})
+\mathcal C(E_{2m},P_q,L).
\end{aligned}
\tag{KPGODD-25}
\]

The shifted-triple sum is empty for \(1\le m\le5\); the singleton sum is
empty only at \(m=1\) and has one term at \(m=2\). The repeated summands,
doubleton, and closing term are

\[
\begin{aligned}
\mathcal C(E_j,P_j,E_{j+1})
&=-8j^2-16mj-24j+192m^2+356m+162,\\
\mathcal C(E_j,P_{j+1},E_{j+1})
&=-8j^2-16mj-36j+192m^2+324m+121,\\
\mathcal C(E_m,(a,b),E_{m+1})
&=115m^2+239m+124,\\
x_{3m+1-j}(E_j+E_{j+1})
&=-2j^2-2mj-5j+112m^2+215m+102,\\
\mathcal C(E_{2m},P_q,L)
&=176m^2-28mq+298m-4q^2-25q+126,
\end{aligned}
\tag{KPGODD-26}
\]

while \(LE_0=32m^2+56m+24\). Standard sums of \(j\) and \(j^2\) on the
exact ranges in (KPGODD-25) give (KPGODD-4), with no boundary correction.

Only five residue classes are needed. If \(r=m\bmod5\), put

\[
q={4m+c_r\over5},\qquad
(c_0,c_1,c_2,c_3,c_4)=(5,1,2,3,4).
\tag{KPGODD-27}
\]

Then

\[
K(\tau_m^\circ)
={42850m^3+112347m^2+(94925+216c_r)m
 +25800+300c_r+12c_r^2\over150},
\tag{KPGODD-28}
\]

or explicitly

\[
\begin{array}{c|c|c|c}
r&q&n\bmod50&150K(\tau_m^\circ)\\ \hline
0&(4m+5)/5&8&42850m^3+112347m^2+96005m+27600\\
1&(4m+1)/5&18&42850m^3+112347m^2+95141m+26112\\
2&(4m+2)/5&28&42850m^3+112347m^2+95357m+26448\\
3&(4m+3)/5&38&42850m^3+112347m^2+95573m+26808\\
4&(4m+4)/5&48&42850m^3+112347m^2+95789m+27192.
\end{array}
\tag{KPGODD-29}
\]

The \(r=0\) row begins at \(m=5\); the other rows begin at their smallest
positive representatives. Every numerator is divisible by \(150\) on its
stated class because it equals the integer block score (KPGODD-25). There is
no additional parity split. Equivalently, with
\(q=\lfloor(2n+9)/25\rfloor\),

\[
K(\tau_m^\circ)
={857n^3+1767n^2+1200nq-5366n
 +6000q^2+20400q+7056\over3000},
\tag{KPGODD-30}
\]

and hence this fixed subsequence has coefficient \(857/3000\).

### Exact same-row comparison with canonical K825

On \(n=10m+8\), the K825 parameters are
\(e=4\), \(v=2m+1\), \(\varepsilon=1\), and \(\Gamma=-12m-10<0\).
Its unique maximizing subset is the same set \(B_m\), but its cyclic order
is the canonical unshifted order, not (KPGODD-1). Specializing (K825-4)
gives

\[
K_{825}(m)={572m^3+1497m^2+1279m+354\over2}.
\tag{KPGODD-31}
\]

Exact subtraction, performed only after both scores have been evaluated,
gives

\[
K(\tau_m^\circ)-K_{825}(m)
={-m^3-12m^2+12mq-44m+6q^2+30q-15\over3}.
\tag{KPGODD-32}
\]

The numerator is increasing in \(q\ge0\). Since \(q\le m\), with equality
exactly for \(1\le m\le5\),

\[
3\bigl(K(\tau_m^\circ)-K_{825}(m)\bigr)
\le-m^3+6m^2-14m-15
=-\bigl((m-2)^3+2m+23\bigr)<0.
\tag{KPGODD-33}
\]

Thus there is no comparison tie or crossover: the fixed PGODD order is
strictly lower on every row. Only after this exact comparison may one state

\[
K(\tau_m^\circ)={857\over3000}n^3+O(n^2),\qquad
K_{825}(m)={858\over3000}n^3+O(n^2),
\tag{KPGODD-34}
\]

so their fixed-core score difference has leading term
\(-n^3/3000\). This is not a global coefficient improvement or a minimizing-
order theorem.

### Literal boundary rows and verification boundary

At \(m=1\), the singleton range is empty and

\[
\begin{aligned}
\alpha^\circ&=(0,2,1),\\
\tau_1^\circ&=(16,6,15,8,14,5,17,4,10,11,3,18,2,13,9,12,7),\\
B_1&=\{7,\ldots,18\},\qquad
K(\tau_1^\circ)=1843<1851=K_{825}(1).
\end{aligned}
\tag{KPGODD-35}
\]

At \(m=2\), singleton reversal is order-neutral because the block has one
member, and

\[
\begin{aligned}
\alpha^\circ&=(0,1,3,4,2),\\
\tau_2^\circ&=(24,10,23,12,22,9,25,8,21,13,20,7,26,6,15,16,5,\\
&\qquad 27,4,17,3,28,2,19,14,18,11),\\
B_2&=\{11,\ldots,28\},\qquad
K(\tau_2^\circ)=6729<6738=K_{825}(2).
\end{aligned}
\tag{KPGODD-36}
\]

Neither row is an exception to the formula or unique argmax. Their only
exception is the shortcut-minimum role recorded in (KPGODD-24).

The sole diagnostic for (KPGODD-1)--(KPGODD-36) is the standalone
standard-library script
ops/TASK-20260719__pgodd_exact_k/exact_diagnostic.py. It constructs only
(PGODD-6). On \(m=1,\ldots,30\), an independent least-selected-position
max-plus recurrence checks the exact score and unique backbone through
39,461,580 transitions, while a separate scan checks all 1,007,210 proper
oriented arcs, including 1,000,460 nontrivial compressed shortcuts and every
cyclic-cut arc. Literal formula, residue, boundary, and K825 comparisons
continue through \(m=1000\). It enumerates no subset, path permutation,
matching, or family of cyclic orders. These bounded checks corroborate but do
not prove the symbolic theorem.

All claims in this section concern \(K\) on the one core order fixed by
(PGODD-6). They imply no exact angular statement, geometry, global
\(K\)-minimality, minimizing-order classification, or global optimality.

## 18. Exact \(K\) For The Even-\(v\) Residue-Two PG49-Star Core

Retain exactly (PGE2-1)--(PGE2-6), without changing the candidate after its
construction and \(W\) score were proved:

\[
n=10m+2,\qquad m\ge1,\qquad D=8m+3,\qquad
q=\left\lceil{(m-1)(4m+1)\over5m+1}\right\rceil .
\]

With \(j^+=j+1\pmod {2m}\), the literal cyclic core order is

\[
\boxed{
\tau_m^{(2,*)}
=\mathop{\bigcirc}_{j=0}^{2m-1}
 (E_j,\lambda_j,P_{\alpha^{(2)}_*(j)},\rho_{j^+}) .}
\tag{KPGE2-1}
\]

The concatenation starts at \(E_0=D\), expands every path in the orientation
of (PGE2-3), and closes from the final \(\rho_0=4m+1\) back to \(E_0\).
Thus (KPGE2-1), rather than a reordered block surrogate, is the only core
evaluated here. Put

\[
L=4m+1,\qquad
H_m=\{2,\ldots,4m\},\qquad
B_m=\{L,\ldots,10m+2\}.
\tag{KPGE2-2}
\]

The exact all-domain classification is

\[
\boxed{
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}
 P_{\tau_m^{(2,*)}}(U)=\{B_m\}.}
\tag{KPGE2-3}
\]

In particular, the maximizer is unique for every \(m\ge1\). Its exact score
is

\[
\boxed{
K(\tau_m^{(2,*)})
={1714m^3+1353m^2+24mq+281m+12q^2+36q+30\over6}.}
\tag{KPGE2-4}
\]

We first prove uniqueness directly from the literal order. The score formula
is used only afterwards.

### Exact compressed backbone and empty ranges

Every member of \(H_m\) is isolated between two members of \(B_m\). Deleting
all holes from (KPGE2-1) and starting at \(L=\rho_0\) gives

\[
\boxed{
\left(
L,
(E_j,P_j)_{j=0}^{q-1},
(E_j,P_{j+1})_{j=q}^{m-2},
E_{m-1},a,b,
(E_j,x_{3m-1-j})_{j=m}^{2m-2},
E_{2m-1},P_q
\right).}
\tag{KPGE2-5}
\]

Every indexed block is concatenated in increasing \(j\), and every displayed
path is expanded. All ranges are literal. The first triple block is empty
only at \(m=1\). The shifted-triple block is empty exactly for
\(1\le m\le6\), and first consists of one term at \(m=7,q=5\). The
singleton block is empty at \(m=1\) and consists of one member at \(m=2\).
The doubleton \((a,b)=(5m+2,5m+3)\) is always present and keeps its
orientation.

### Complete deletion-gain audit

For a hole \(z\in H_m\) between backbone neighbors \(u,w\), define

\[
h_z=uw-z(u+w).
\tag{KPGE2-6}
\]

The following nine classes are exhaustive:

\[
\begin{array}{c|c|c}
\text{hole}&\text{gap range}&h_z\\ \hline
\lambda_j&0\le j<q&
-4j^2+(28m+6)j+20m+6\\
\rho_{j+1}&0\le j<q&
-4j^2+(28m+2)j+36m+9\\
\lambda_j&q\le j\le m-2&
-4j^2+28mj+12m\\
\rho_{j+1}&q\le j\le m-2&
-4j^2+(28m-4)j+28m-1\\
\lambda_{m-1}&&17m^2-8m-4\\
\rho_m&&17m^2+16m+3\\
\lambda_j&m\le j\le2m-2&
-j^2+(29m+9)j-4m^2+17m+6\\
\rho_{j+1}&m\le j\le2m-2&
-j^2+(29m+10)j-4m^2+35m+14\\
\lambda_{2m-1}=2&&80m^2-20mq-4.
\end{array}
\tag{KPGE2-7}
\]

The two unindexed middle rows are precisely the left and right holes of the
doubleton. The final row is the genuine closing hole between
\(E_{2m-1}=n\) and \(A_q\); the off-cut right-hole formula is not extended
through the cyclic cut. The class cardinalities are

\[
2q+2(m-1-q)+2+2(m-1)+1=4m-1=|H_m|.
\tag{KPGE2-8}
\]

Thus empty ranges introduce no missing class. The forward differences of the
four triple and two singleton polynomials, in table order, are

\[
28m+2-8j,\quad28m-2-8j,\quad
28m-4-8j,\quad28m-8-8j,
\quad29m+8-2j,\quad29m+9-2j.
\tag{KPGE2-9}
\]

They are positive on their exact ranges. For \(m\ge2\), the first left class
therefore has minimum \(20m+6\) at \(j=0\), while the first right class
starts \(16m+3\) higher. If the shifted range is nonempty, then
\(m\ge7,q\ge5\), and its two left-end excesses over \(20m+6\) are

\[
4q(7m-q)-8m-6>0,\qquad
4q(7m-q-1)+8m-7>0.
\tag{KPGE2-10}
\]

The doubleton left and right excesses are

\[
17m^2-28m-10>0,\qquad17m^2-4m-3>0
\qquad(m\ge2).
\tag{KPGE2-11}
\]

When the singleton range is nonempty, its two initial excesses are

\[
6m(4m+1),\qquad24m^2+25m+8.
\tag{KPGE2-12}
\]

Finally \(q\le m-1\) gives the closing excess

\[
80m^2-20mq-4-(20m+6)\ge60m^2-10>0.
\tag{KPGE2-13}
\]

At \(m=1\), all triple and singleton ranges in (KPGE2-7) are empty. The
three remaining gains, in doubleton-left, doubleton-right, and closing order,
are \(5,36,76\). Consequently

\[
\boxed{
\min_{z\in H_m}h_z=
\begin{cases}
5,&m=1,\quad z=\lambda_0=4,\\
20m+6,&m\ge2,\quad z=\lambda_0=4m,
\end{cases}}
\tag{KPGE2-14}
\]

and the displayed minimizer is unique on every row.

### Complete compressed-shortcut audit

For an arbitrary proper oriented arc whose compressed path has at least two
edges, delete only its internal holes and write

\[
C=(z_0,z_1,\ldots,z_s),\qquad s\ge2,\qquad
M(C)=\sum_{i=0}^{s-1}z_iz_{i+1}-z_0z_s.
\tag{KPGE2-15}
\]

First suppose an endpoint is a hole. Every backbone neighbor of a hole is at
least \(R_0=5m+2\). If both endpoints \(u,v\) are holes, they are distinct,
and

\[
M(C)\ge R_0(u+v)-uv>4R_0-4=20m+4.
\tag{KPGE2-16}
\]

If exactly \(u\) is a hole and \(v\in B_m\), the backbone label adjacent to
the other boundary is at least \(L\). A four-corner check on
\(2\le u\le4m\), \(L\le v\le n\) gives

\[
M(C)\ge uR_0+vL-uv\ge16m^2+10m+3>20m+4.
\tag{KPGE2-17}
\]

These bounds apply in both orientations and for every length; all omitted
internal products are positive.

It remains to take both endpoints in \(B_m\). For \(s=2\), a triple
connector \(c_k\), \(0\le k\le m-1\), has exact margin

\[
c_k(A_k+B_k)-A_kB_k
=-8k^2+(32m+1)k+20m+4.
\tag{KPGE2-18}
\]

Its forward difference \(32m-16k-7\) is positive on the exact range, so the
unique connector minimum is \(20m+4\) at \(c_0\). For a reversed singleton,
write its gap as \(j=m+t\), \(0\le t\le m-2\). Its terminal-to-terminal
margin is

\[
27m^2-24mt+15m-3t^2-10t+2\ge65m+10,
\tag{KPGE2-19}
\]

with equality only at \(t=m-2\). This range is empty at \(m=1\) and has one
member at \(m=2\). The two doubleton labels give

\[
25m^2+16m+4,\qquad25m^2+34m+9,
\tag{KPGE2-20}
\]

and the complete three-edge doubleton window has margin

\[
M(E_{m-1},a,b,E_m)=34m^2+50m+13.
\tag{KPGE2-21}
\]

The retained closing label \(L=\rho_0\), between \(B_q\) and \(E_0\), has
the exact two-edge margin

\[
M(B_q,L,E_0)=(8m+4)q+1.
\tag{KPGE2-22}
\]

The remaining two-edge middle roles are outer triple labels and terminals,
all at least \(6m+3\). For such a middle label \(y\), use
\[
y(a+b)-ab=y^2-(a-y)(b-y).
\]
When both endpoints exceed \(y\), both lie below \(y\), or they straddle
\(y\), respectively, the margin is at least

\[
20m^2+44m+8,\qquad
32m^2+28m+5,\qquad
(6m+3)^2.
\tag{KPGE2-23}
\]

Every bound is strictly above \(20m+4\). The two-edge roles are exhaustive
because their counts are

\[
m+(m-1)+2+1+2m+2m=6m+2=|B_m|
\tag{KPGE2-24}
\]

for connectors, singletons, doubleton members, \(L\), outer triple labels,
and terminals.

For \(s=3\), every adjacent pair of internal backbone labels has one member
at least \(R=5m+3\) and the other at least \(L\). This is literal on the
doubleton edge; triple edges contain an outer label at least \(6m+3\);
singletons are flanked by terminals; and both edges at \(L\) have a high
neighbor. Reversing the path if needed and checking the four endpoint
corners gives

\[
M(C)\ge z_0R+RL+Lz_3-z_0z_3
\ge10m^2+35m+7>20m+4.
\tag{KPGE2-25}
\]

For every \(s\ge4\), all internal labels are at least \(L\), so

\[
\begin{aligned}
M(C)
&\ge L(z_0+z_s)+(s-2)L^2-z_0z_s\\
&\ge12m^2+12m+2+(s-4)L^2>20m+4.
\end{aligned}
\tag{KPGE2-26}
\]

The full compressed closing word is

\[
E_{2m-1},A_q,c_q,B_q,L,E_0.
\tag{KPGE2-27}
\]

Thus (KPGE2-22) treats its retained two-edge closing role,
(KPGE2-25) treats both adjacent closing pairs, and (KPGE2-26) treats every
longer cut-crossing arc. The distinct closing hole was already the final row
of (KPGE2-7). Since \(q=0,1,2\) at \(m=1,2,3\), while \(q\ge3\) at
\(m\ge4\), the exact equality classification is

\[
\boxed{
\min_{C:\,s\ge2}M(C)=
\begin{cases}
1,&m=1,\quad C=(9,5,11),\\
21,&m=2,\quad C=(15,9,19),\\
57,&m=3,\quad C=(21,13,27),\\
20m+4,&m\ge4,\quad C=(A_0,c_0,B_0).
\end{cases}}
\tag{KPGE2-28}
\]

Indeed, for \(m\ge4\),
\[
(8m+4)q+1-(20m+4)\ge4m+9>0.
\]
Every displayed forward arc is the unique equality arc in the fixed cyclic
presentation.

The strict gains (KPGE2-14), strict shortcuts (KPGE2-28), and exact identity
(K825-8)--(K825-9) now force equality as follows. Every hole must be omitted,
and every selected gap must be one edge of the compressed backbone. Hence the
selected subset is exactly \(B_m\). Conversely \(B_m\) attains its backbone
score. The same inequality applied to \(\{n-1,n\}\) gives
\(P_{\tau_m^{(2,*)}}(B_m)\ge2n(n-1)>n^2\), so no singleton can tie. This
proves (KPGE2-3), including the two-element convention, doubleton, singleton
block, every empty range, and the cyclic closure.

### Exact block sum and residual branches

For a nonempty path \(P=(p_1,\ldots,p_s)\), put
\[
\mathcal C(x,P,y)=xp_1+\sum_{i=1}^{s-1}p_ip_{i+1}+p_sy.
\]
Reading (KPGE2-5) from \(L\), the exact backbone score is

\[
\begin{aligned}
P_{\tau_m^{(2,*)}}(B_m)={}&LE_0
+\sum_{j=0}^{q-1}\mathcal C(E_j,P_j,E_{j+1})\\
&+\sum_{j=q}^{m-2}\mathcal C(E_j,P_{j+1},E_{j+1})
+\mathcal C(E_{m-1},(a,b),E_m)\\
&+\sum_{j=m}^{2m-2}x_{3m-1-j}(E_j+E_{j+1})
+\mathcal C(E_{2m-1},P_q,L).
\end{aligned}
\tag{KPGE2-29}
\]

The repeated summands, doubleton, singleton, closing term, and initial edge
are

\[
\begin{aligned}
\mathcal C(E_j,P_j,E_{j+1})
&=-8j^2-16mj-16j+192m^2+124m+16,\\
\mathcal C(E_j,P_{j+1},E_{j+1})
&=-8j^2-16mj-28j+192m^2+92m-7,\\
\mathcal C(E_{m-1},(a,b),E_m)
&=115m^2+95m+19,\\
x_{3m-1-j}(E_j+E_{j+1})
&=-2j^2-2mj-3j+112m^2+81m+14,\\
\mathcal C(E_{2m-1},P_q,L)
&=176m^2-28mq+92m-4q^2-11q+11,\\
LE_0&=32m^2+20m+3.
\end{aligned}
\tag{KPGE2-30}
\]

Standard sums of \(j\) and \(j^2\) on the literal ranges in (KPGE2-29)
give (KPGE2-4), with no hidden empty-range correction.

For \(m\ge2\), let \(r=m\bmod5\) and write

\[
q={4m+c_r\over5},\qquad
(c_0,c_1,c_2,c_3,c_4)=(0,1,-3,-2,-1).
\tag{KPGE2-31}
\]

The \(r=1\) regular branch begins at \(m=6\); \(m=1\) is handled separately.
Then

\[
150K
=42850m^3+34497m^2+(7745+216c_r)m
+12c_r^2+180c_r+750.
\tag{KPGE2-32}
\]

Equivalently,

\[
\begin{array}{c|c|c|c}
r&q&n\bmod50&150K\\ \hline
0&4m/5&2&42850m^3+34497m^2+7745m+750\\
1&(4m+1)/5&12&42850m^3+34497m^2+7961m+942\\
2&(4m-3)/5&22&42850m^3+34497m^2+7097m+318\\
3&(4m-2)/5&32&42850m^3+34497m^2+7313m+438\\
4&(4m-1)/5&42&42850m^3+34497m^2+7529m+582.
\end{array}
\tag{KPGE2-33}
\]

The first row begins at \(m=5\), the regular second row at \(m=6\), and the
last three at \(m=2,3,4\). At the sole residual row \(m=1\),
\[
q=0,\qquad K=563;
\]
the formal \(r=1\) expression would instead give \(575\). This is a formula
residual only: neither the argmax nor the score (KPGE2-4) is exceptional.
In terms of \(n=10m+2\), with the same literal \(q\),

\[
K
={857n^3+1623n^2+1200nq-2726n
 +6000q^2+15600q+7104\over3000},
\tag{KPGE2-34}
\]

so this fixed family has cubic coefficient \(857/3000\).

### Exact comparison with the known residue-two order

On the same subsequence, put \(k=2m\) in Section 10. The known residue-two
order uses the same paths with the identity assignment:

\[
\tau_{\rm R2}(2m)
=\mathop{\bigcirc}_{j=0}^{2m-1}
 (E_j,\lambda_j,P_j,\rho_{j^+}).
\tag{KPGE2-35}
\]

Its unique maximizer is the same label set \(B_m\), but its cyclic order is
different. Specializing (KR2-22) gives

\[
K_{\rm R2}(2m)={572m^3+459m^2+99m+4\over2}.
\tag{KPGE2-36}
\]

Exact subtraction yields

\[
\boxed{
K_{\rm R2}(2m)-K(\tau_m^{(2,*)})
={m^3+12m^2-12mq+8m-6q^2-18q-9\over3}.}
\tag{KPGE2-37}
\]

The numerator decreases with \(q\ge0\). Since \(q\le m-1\),

\[
3(K_{\rm R2}-K)
\ge m^3-6m^2+14m+3
=(m-2)^3+2m+11>0.
\tag{KPGE2-38}
\]

Thus the fixed PGE2 order is strictly lower on every row, with no tie or
crossover. The first four exact gaps are \(4,5,6,9\).

### Exact comparison with canonical K825

For \(m\ge4\), the symbolic K825 parameters on \(n=10m+2\) are

\[
e=8,\qquad v=2m-1,\qquad\varepsilon=1,\qquad
\Gamma=20m+6,\qquad\chi=0.
\]

Consequently

\[
K_{825}(m)={572m^3+501m^2+149m+6\over2}
\qquad(m\ge4).
\tag{KPGE2-39}
\]

The first three rows are explicit; the table also includes the first
symbolic row:

\[
\begin{array}{c|c|c|c}
m&K(\tau_m^{(2,*)})&K_{\rm R2}(2m)&K_{825}(m)\\ \hline
1&563&567&593\\
2&3302&3307&3431\\
3&9932&9938&10299\\
4&22167&22176&22613.
\end{array}
\tag{KPGE2-40}
\]

For \(m=1,2,3\), the explicit K825 maximizer is \(B_m\). From \(m\ge4\),
the symbolic K825 maximizer is instead
\[
\{4m-1,\ldots,n\}\setminus\{4m\}=\{4m-1\}\cup B_m,
\]
in the distinct canonical order. For \(m\ge4\), exact subtraction gives

\[
\boxed{
K_{825}(m)-K(\tau_m^{(2,*)})
={m^3+75m^2-12mq+83m-6q^2-18q-6\over3}.}
\tag{KPGE2-41}
\]

Again the numerator decreases with \(q\), and \(q\le m-1\) gives

\[
3(K_{825}-K)\ge m^3+57m^2+89m+6>0.
\tag{KPGE2-42}
\]

Together with (KPGE2-40), this proves strict improvement on every row. There
is no tie or crossover.

Only after both exact comparisons may one state

\[
\boxed{
K(\tau_m^{(2,*)})={857\over3000}n^3+O(n^2),\qquad
K_{\rm R2}(2m)={858\over3000}n^3+O(n^2),\qquad
K_{825}(m)={858\over3000}n^3+O(n^2).}
\tag{KPGE2-43}
\]

Both same-row gaps have leading term \(n^3/3000\). By contrast, the prior
gap between the known residue-two order and K825 was only quadratic.

### Literal boundary rows and verification boundary

At \(m=1\), both triple-index ranges and the singleton range in (KPGE2-5)
are empty:

\[
\begin{aligned}
\alpha^{(2)}_*&=(1,0),\\
\tau_1^{(2,*)}&=(11,4,7,8,3,12,2,10,6,9,5),\\
B_1&=\{5,\ldots,12\},\qquad
K(\tau_1^{(2,*)})=563<567<593.
\end{aligned}
\tag{KPGE2-44}
\]

At \(m=2\), the shifted-triple range is empty and singleton reversal is
order-neutral because the block has one member:

\[
\begin{aligned}
\alpha^{(2)}_*&=(0,2,3,1),\\
\tau_2^{(2,*)}
&=(19,8,18,10,17,7,20,6,12,13,5,21,4,14,3,22,2,\\
&\qquad16,11,15,9),\\
B_2&=\{9,\ldots,22\},\qquad
K(\tau_2^{(2,*)})=3302<3307<3431.
\end{aligned}
\tag{KPGE2-45}
\]

Neither row is an exception to the exact formula (KPGE2-4) or unique
argmax. The only boundary transitions are the deletion-gain branch in
(KPGE2-14), the residual residue formula at \(m=1\), and the shortcut
minimum in (KPGE2-28).

The sole diagnostic for (KPGE2-1)--(KPGE2-45) is the standalone
standard-library script
ops/TASK-20260720__residue_two_pg49_star_k/exact_diagnostic.py. It constructs
only (PGE2-6). On \(m=1,\ldots,30\), an independent
least-selected-position max-plus recurrence checks the score and unique
backbone through 36,511,800 transitions. A separate audit checks 1,830
deletion gains and all 950,150 proper oriented arcs, including 943,640
nontrivial compressed shortcuts and every cyclic-cut arc. It also checks the
exact raw-arc plus hole-budget identity on every arc. Literal formulas,
residue branches, boundary rows, and both exact comparisons continue through
\(m=1000\). It enumerates no subset, matching, path permutation, or family of
orders. These bounded checks corroborate but do not prove the symbolic
theorem.

All claims in this section concern induced \(K\) on the one unchanged core
fixed by (PGE2-6). They do not change production, infer an exact angular or
geometric statement, classify a global minimizing order, or assert global
optimality.

## 19. Exact \(K\) For The Odd-\(v\) Residue-Two PG49-Star Core

Retain exactly (PGE2ODD-1)--(PGE2ODD-6), without changing the candidate
after its construction and \(W\) score were proved:

\[
n=10m+7,\qquad m\ge1,\qquad D=8m+7,\qquad
q=\left\lfloor{4m+3\over5}\right\rfloor .
\]

With \(j^+=j+1\pmod {2m+1}\), the literal cyclic core order is

\[
\boxed{
\tau_m^{(2,\mathrm{odd},*)}
=\mathop{\bigcirc}_{j=0}^{2m}
 (E_j,\lambda_j,P_{\alpha^{(2,\mathrm{odd})}_*(j)},\rho_{j^+}) .}
\tag{KPGE2ODD-1}
\]

The concatenation starts at \(E_0=D\), expands every triple in the
orientation of (PGE2ODD-3), and closes from the retained
\(\rho_0=4m+3\) back to \(E_0\). Thus (KPGE2ODD-1), rather than a reordered
block surrogate, is the only core evaluated here. Put

\[
L=4m+3,\qquad
H_m=\{2,\ldots,4m+2\},\qquad
B_m=\{L,\ldots,10m+7\}.
\tag{KPGE2ODD-2}
\]

The exact all-domain classification is

\[
\boxed{
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}
 P_{\tau_m^{(2,\mathrm{odd},*)}}(U)=\{B_m\}.}
\tag{KPGE2ODD-3}
\]

In particular, the maximizer is unique for every \(m\ge1\). Its exact score
is

\[
\boxed{
K(\tau_m^{(2,\mathrm{odd},*)})
={1714m^3+3891m^2+24mq+2921m+12q^2+48q+732\over6}.}
\tag{KPGE2ODD-4}
\]

We first prove uniqueness directly from the literal order. The score formula
is used only afterwards.

### Exact compressed backbone and all empty ranges

Every member of \(H_m\) is isolated between two members of \(B_m\). Deleting
all holes from (KPGE2ODD-1) and starting at \(L=\rho_0\) gives

\[
\boxed{
\left(
L,
(E_j,P_j)_{j=0}^{q-1},
(E_j,P_{j+1})_{j=q}^{m-1},
(E_j,x_{3m-j})_{j=m}^{2m-1},
E_{2m},P_q
\right).}
\tag{KPGE2ODD-5}
\]

Every indexed block is concatenated in increasing \(j\), and every displayed
path is expanded. All ranges are literal. The first triple block is always
nonempty. The shifted-triple block is empty exactly for \(m=1,2,3\), because
these are exactly the rows with \(q=m\); it first consists of one term at
\(m=4,q=3\). The singleton block always has \(m\) members, so at \(m=1\)
it is a literal singleton block of length one. There is no doubleton path or
doubleton index range on any row. The final displayed path is always the
retained closing triple \(P_q\).

### Complete cancellation-gain audit

For a hole \(z\in H_m\) between backbone neighbors \(u,w\), define

\[
h_z=uw-z(u+w).
\tag{KPGE2ODD-6}
\]

The following seven classes are exhaustive:

\[
\begin{array}{c|c|c}
\text{hole}&\text{gap range}&h_z\\ \hline
\lambda_j&0\le j<q&
-4j^2+(28m+20)j+20m+16\\
\rho_{j+1}&0\le j<q&
-4j^2+(28m+16)j+36m+27\\
\lambda_j&q\le j\le m-1&
-4j^2+(28m+14)j+12m+6\\
\rho_{j+1}&q\le j\le m-1&
-4j^2+(28m+10)j+28m+13\\
\lambda_j&m\le j\le2m-1&
-j^2+(29m+19)j-4m^2+7m+6\\
\rho_{j+1}&m\le j\le2m-1&
-j^2+(29m+20)j-4m^2+25m+20\\
\lambda_{2m}=2&&
80m^2-20mq+80m-10q+16.
\end{array}
\tag{KPGE2ODD-7}
\]

The final row is the genuine closing hole between \(E_{2m}=n\) and \(A_q\);
the off-cut right-hole formula is not extended through the cyclic cut. The
class cardinalities are

\[
2q+2(m-q)+2m+1=4m+1=|H_m|.
\tag{KPGE2ODD-8}
\]

Thus the empty shifted range introduces no missing class, and the absent
doubleton contributes no synthetic class. The forward differences of the
six indexed polynomials, in table order, are

\[
28m+16-8j,\quad28m+12-8j,\quad
28m+10-8j,\quad28m+6-8j,\quad
29m+18-2j,\quad29m+19-2j.
\tag{KPGE2ODD-9}
\]

They are positive on their exact ranges. The first left class therefore has
unique minimum \(20m+16\) at \(j=0\), while the first right class starts
\(16m+11\) higher. If the shifted range is nonempty, then \(m\ge4\),
\(q\ge3\), and its two left-end excesses over \(20m+16\) are

\[
4q(7m-q)+14q-8m-10>0,\qquad
4q(7m-q)+10q+8m-3>0.
\tag{KPGE2ODD-10}
\]

The two singleton classes start at \(j=m\), with excesses

\[
24m^2+6m-10>0,\qquad24m^2+25m+4>0.
\tag{KPGE2ODD-11}
\]

Finally \(q\le m\) gives the closing excess

\[
80m^2-20mq+60m-10q
\ge60m^2+50m>0.
\tag{KPGE2ODD-12}
\]

Consequently

\[
\boxed{
\min_{z\in H_m}h_z=20m+16,
\qquad z=\lambda_0=4m+2,}
\tag{KPGE2ODD-13}
\]

and the displayed minimizing hole, between \(E_0=8m+7\) and
\(A_0=8m+6\), is unique on every row.

### Complete compressed-shortcut audit

For an arbitrary proper oriented arc whose compressed path has at least two
edges, delete only its internal holes and write

\[
C=(z_0,z_1,\ldots,z_s),\qquad s\ge2,\qquad
M(C)=\sum_{i=0}^{s-1}z_iz_{i+1}-z_0z_s.
\tag{KPGE2ODD-14}
\]

First suppose an endpoint is a hole. Every backbone neighbor of a hole is at
least \(R_0=5m+5\). If both endpoints \(u,v\) are holes, they are distinct,
and

\[
M(C)\ge R_0(u+v)-uv\ge5R_0-6=25m+19>0.
\tag{KPGE2ODD-15}
\]

If exactly \(u\) is a hole and \(v\in B_m\), the backbone label adjacent to
the other boundary is at least \(L\). A four-corner check on
\(2\le u\le4m+2\), \(L\le v\le n\) gives

\[
M(C)\ge uR_0+vL-uv\ge16m^2+26m+13>0.
\tag{KPGE2ODD-16}
\]

These bounds apply in both orientations and for every length; omitted
internal products are positive.

It remains to take both endpoints in \(B_m\). For \(s=2\), a triple
connector \(c_k\), \(0\le k\le m\), has exact margin

\[
c_k(A_k+B_k)-A_kB_k
=-8k^2+(32m+17)k+20m+14.
\tag{KPGE2ODD-17}
\]

Its forward difference is \(32m+9-16k>0\) on the exact range, so the unique
connector minimum is \(20m+14\) at \(c_0\). For a reversed singleton, write
its gap as \(j=m+t\), \(0\le t\le m-1\). Its terminal-to-terminal margin is

\[
27m^2-24mt+27m-3t^2-22t+4\ge35m+23,
\tag{KPGE2ODD-18}
\]

with equality only at \(t=m-1\). The retained closing label \(L=\rho_0\),
between \(B_q\) and \(E_0\), has the exact two-edge margin

\[
M(B_q,L,E_0)=(8m+8)q+1.
\tag{KPGE2ODD-19}
\]

The remaining two-edge middle roles are outer triple labels and terminals,
all at least \(6m+5\). Relaxing both endpoints to \([L,n]\) and checking
the four corners gives

\[
y(a+b)-ab\ge20m^2+44m+21>0.
\tag{KPGE2ODD-20}
\]

These roles are exhaustive because their counts are

\[
(m+1)+m+1+2(m+1)+(2m+1)=6m+5=|B_m|
\tag{KPGE2ODD-21}
\]

for connectors, singletons, \(L\), outer triple labels, and terminals.
There is no doubleton middle role.

For \(s=3\), every adjacent pair of internal backbone labels has one member
at least \(R=6m+5\) and the other at least \(L\). This uses exactly the
triple, singleton, and closing edges of (KPGE2ODD-5); no absent doubleton is
silently inserted. Reversing the path if needed and checking the four
endpoint corners gives

\[
M(C)\ge z_0R+RL+Lz_3-z_0z_3
\ge24m^2+48m+22>0.
\tag{KPGE2ODD-22}
\]

For every \(s\ge4\), all internal labels are at least \(L\), so

\[
\begin{aligned}
M(C)
&\ge L(z_0+z_s)+(s-2)L^2-z_0z_s\\
&\ge12m^2+24m+11+(s-4)L^2>0.
\end{aligned}
\tag{KPGE2ODD-23}
\]

The full compressed closing word is

\[
E_{2m},A_q,c_q,B_q,L,E_0.
\tag{KPGE2ODD-24}
\]

Thus (KPGE2ODD-19) treats its retained two-edge closing role,
(KPGE2ODD-22) treats both adjacent closing pairs, and (KPGE2ODD-23) treats
every longer cut-crossing arc. The distinct closing hole was already the
final row of (KPGE2ODD-7). Relative to the connector value \(20m+14\), the
lower bounds for two hole endpoints, one hole endpoint, a singleton middle,
an outer-label or terminal middle, three edges, and at least four edges leave
respectively
\[
5m+5,\quad16m^2+6m-1,\quad15m+9,\quad20m^2+24m+7,
\quad24m^2+28m+8,\quad
12m^2+4m-3+(s-4)L^2,
\]
all strictly positive. Hence these classes also exceed the smaller closing
values at \(m=1,2\). Since \(q=1,2\) at \(m=1,2\), while \(q\ge3\) at
\(m\ge3\), the exact equality classification is

\[
\boxed{
\min_{C:\,s\ge2}M(C)=
\begin{cases}
17,&m=1,\quad C=(11,7,15),\\
49,&m=2,\quad C=(17,11,23),\\
20m+14,&m\ge3,\quad C=(A_0,c_0,B_0).
\end{cases}}
\tag{KPGE2ODD-25}
\]

Indeed, for \(m\ge3\),
\((8m+8)q+1-(20m+14)\ge4m+11>0\). Every displayed forward arc is the unique
equality arc in the fixed cyclic presentation.

The strict gains (KPGE2ODD-13), strict shortcuts (KPGE2ODD-25), and exact
identity (K825-8)--(K825-9) now force equality as follows. Every hole must be
omitted, and every selected gap must be one edge of the compressed backbone.
Hence the selected subset is exactly \(B_m\). Conversely \(B_m\) attains its
backbone score. The same inequality applied to \(\{n-1,n\}\) gives
\(P_{\tau_m^{(2,\mathrm{odd},*)}}(B_m)\ge2n(n-1)>n^2\), so no singleton can
tie. This proves (KPGE2ODD-3), including the adopted two-element convention,
the singleton block, absence of a doubleton path, every empty range, and the
cyclic closure.

### Exact block sum and all residue branches

For a nonempty path \(P=(p_1,\ldots,p_s)\), put
\[
\mathcal C(x,P,y)=xp_1+\sum_{i=1}^{s-1}p_ip_{i+1}+p_sy.
\]
Reading (KPGE2ODD-5) from \(L\), the exact backbone score is

\[
\begin{aligned}
P_{\tau_m^{(2,\mathrm{odd},*)}}(B_m)={}&LE_0
+\sum_{j=0}^{q-1}\mathcal C(E_j,P_j,E_{j+1})\\
&+\sum_{j=q}^{m-1}\mathcal C(E_j,P_{j+1},E_{j+1})
+\sum_{j=m}^{2m-1}x_{3m-j}(E_j+E_{j+1})\\
&+\mathcal C(E_{2m},P_q,L).
\end{aligned}
\tag{KPGE2ODD-26}
\]

The repeated summands, closing term, and initial edge are

\[
\begin{aligned}
\mathcal C(E_j,P_j,E_{j+1})
&=-8j^2-16mj-24j+192m^2+316m+126,\\
\mathcal C(E_j,P_{j+1},E_{j+1})
&=-8j^2-16mj-36j+192m^2+284m+87,\\
x_{3m-j}(E_j+E_{j+1})
&=-2j^2-2mj-7j+112m^2+169m+60,\\
\mathcal C(E_{2m},P_q,L)
&=176m^2-28mq+268m-4q^2-25q+101,\\
LE_0&=32m^2+52m+21.
\end{aligned}
\tag{KPGE2ODD-27}
\]

Standard sums of \(j\) and \(j^2\) on the literal ranges in
(KPGE2ODD-26) give (KPGE2ODD-4), with no hidden empty-range correction.

Let \(r=m\bmod5\) and write

\[
q={4m+c_r\over5},\qquad
(c_0,c_1,c_2,c_3,c_4)=(0,1,2,3,-1).
\tag{KPGE2ODD-28}
\]

Then every row, including \(m=1,2,3\), is covered by

\[
150K=42850m^3+97947m^2+(73985+216c_r)m
+18300+240c_r+12c_r^2.
\tag{KPGE2ODD-29}
\]

Equivalently,

\[
\begin{array}{c|c|c|c}
r&q&n\bmod50&150K\\ \hline
0&4m/5&7&42850m^3+97947m^2+73985m+18300\\
1&(4m+1)/5&17&42850m^3+97947m^2+74201m+18552\\
2&(4m+2)/5&27&42850m^3+97947m^2+74417m+18828\\
3&(4m+3)/5&37&42850m^3+97947m^2+74633m+19128\\
4&(4m-1)/5&47&42850m^3+97947m^2+73769m+18072.
\end{array}
\tag{KPGE2ODD-30}
\]

The five branches begin at \(m=5,1,2,3,4\), respectively. There is no
residual row and no correction to the score or argmax. In terms of
\(n=10m+7\),

\[
q=\left\lfloor{2n+1\over25}\right\rfloor,
\qquad
K={857n^3+1458n^2+1200nq-341n
+6000q^2+15600q+2994\over3000}.
\tag{KPGE2ODD-31}
\]

Thus this fixed family has cubic coefficient \(857/3000\).

### Exact comparison with the known residue-two order

On the same subsequence, put \(k=2m+1\) in Section 10. The known residue-two
order uses the same paths with the identity assignment:

\[
\tau_{\rm R2}(2m+1)
=\mathop{\bigcirc}_{j=0}^{2m}
 (E_j,\lambda_j,P_j,\rho_{j^+}).
\tag{KPGE2ODD-32}
\]

Its unique maximizer is the same label set \(B_m\), but its cyclic order is
different. Specializing (KR2-25) gives

\[
K_{\rm R2}(2m+1)
={572m^3+1307m^2+997m+254\over2}.
\tag{KPGE2ODD-33}
\]

Exact subtraction yields

\[
\boxed{
K_{\rm R2}(2m+1)-K(\tau_m^{(2,\mathrm{odd},*)})
={m^3+15m^2-12mq+35m-6q^2-24q+15\over3}.}
\tag{KPGE2ODD-34}
\]

The numerator decreases with \(q\ge0\). Since \(q\le m\),

\[
3(K_{\rm R2}-K)
\ge m^3-3m^2+11m+15
=(m-1)^3+8m+16>0.
\tag{KPGE2ODD-35}
\]

Thus the fixed PGE2ODD order is strictly lower on every row, with no tie or
crossover. The first three exact gaps are \(8,11,16\).

### Exact comparison with canonical K825

For \(m\ge3\), the symbolic K825 parameters on \(n=10m+7\) are

\[
e=8,\qquad v=2m,\qquad\varepsilon=0,\qquad
\Gamma=20m+16,\qquad\chi=\mathbf1_{\{m=3\}}.
\]

Consequently

\[
K_{825}(m)
={572m^3+1349m^2+1119m+324\over2}
-25\mathbf1_{\{m=3\}}
\qquad(m\ge3).
\tag{KPGE2ODD-36}
\]

The first two rows are explicit; the table also includes the corrected
symbolic boundary row:

\[
\begin{array}{c|c|c|c}
m&K(\tau_m^{(2,\mathrm{odd},*)})&K_{\rm R2}(2m+1)&K_{825}(m)\\ \hline
1&1557&1565&1609\\
2&6015&6026&6204\\
3&15210&15226&15608.
\end{array}
\tag{KPGE2ODD-37}
\]

For \(m=1,2\), the explicit K825 maximizer is \(B_m\). From \(m\ge3\), the
symbolic K825 maximizer is instead
\[
\{4m+1,\ldots,n\}\setminus\{4m+2\}
=\{4m+1\}\cup B_m
\]
in the distinct canonical order. For \(m\ge3\), exact subtraction gives

\[
\boxed{
K_{825}(m)-K(\tau_m^{(2,\mathrm{odd},*)})
={m^3+78m^2-12mq+218m-6q^2-24q+120\over3}
-25\mathbf1_{\{m=3\}}.}
\tag{KPGE2ODD-38}
\]

Using \(q\le m\),

\[
K_{825}-K
\ge {m^3+60m^2+194m+120\over3}
-25\mathbf1_{\{m=3\}}>0
\qquad(m\ge3).
\tag{KPGE2ODD-39}
\]

Together with (KPGE2ODD-37), this proves strict improvement on every row.
There is no tie or crossover. Only after both exact comparisons may one state

\[
\boxed{
\begin{aligned}
K(\tau_m^{(2,\mathrm{odd},*)})&={857\over3000}n^3+O(n^2),\\
K_{\rm R2}(2m+1)&={858\over3000}n^3+O(n^2),\qquad
K_{825}(m)={858\over3000}n^3+O(n^2).
\end{aligned}}
\tag{KPGE2ODD-40}
\]

Both same-row gaps have leading term \(n^3/3000\). By contrast, the prior
gap between the known residue-two order and K825 was only quadratic.

### Literal boundary rows and verification boundary

At \(m=1\), the shifted-triple block is empty, the singleton block has one
member, and

\[
\begin{aligned}
\alpha^{(2,\mathrm{odd})}_*&=(0,2,1),\\
\tau_1^{(2,\mathrm{odd},*)}
&=(15,6,14,8,13,5,16,4,10,3,17,2,12,9,11,7),\\
B_1&=\{7,\ldots,17\},\qquad K=1557<1565<1609.
\end{aligned}
\tag{KPGE2ODD-41}
\]

At \(m=2\), the shifted-triple block is again empty and the two singleton
paths are reversed nontrivially:

\[
\begin{aligned}
\alpha^{(2,\mathrm{odd})}_*&=(0,1,4,3,2),\\
\tau_2^{(2,\mathrm{odd},*)}
&=(23,10,22,12,21,9,24,8,20,13,19,7,25,6,16,5,\\
&\qquad26,4,15,3,27,2,18,14,17,11),\\
B_2&=\{11,\ldots,27\},\qquad K=6015<6026<6204.
\end{aligned}
\tag{KPGE2ODD-42}
\]

At \(m=3\), the shifted-triple block is still empty, all three singleton
paths are reversed, and the K825 boundary correction is active:

\[
\begin{aligned}
\alpha^{(2,\mathrm{odd})}_*&=(0,1,2,6,5,4,3),\\
\tau_3^{(2,\mathrm{odd},*)}
&=(31,14,30,16,29,13,32,12,28,17,27,11,33,10,26,18,\\
&\qquad25,9,34,8,22,7,35,6,21,5,36,4,20,3,37,2,\\
&\qquad24,19,23,15),\\
B_3&=\{15,\ldots,37\},\qquad K=15210<15226<15608.
\end{aligned}
\tag{KPGE2ODD-43}
\]

There is no doubleton on any of these rows or elsewhere in the domain.
None of \(m=1,2,3\) is an exception to the all-row score (KPGE2ODD-4), the
five residue branches, or the unique argmax. Their only boundary transitions
are the empty shifted-triple range, the cardinality of the singleton block,
the shortcut-minimum branch in (KPGE2ODD-25), and the canonical K825
symbolic-domain/maximizer transition and boundary correction at \(m=3\).

The sole diagnostic for (KPGE2ODD-1)--(KPGE2ODD-43) is the standalone
standard-library script
ops/TASK-20260720__residue_two_odd_v_pg49_star_k/exact_diagnostic.py. It
constructs only (PGE2ODD-6). Its least-selected-position max-plus recurrence
checks the exact score and complete argmax classification, while a separate
scan checks every deletion gain, every proper oriented arc, the raw-arc plus
hole-budget identity, and every cyclic-cut arc. It enumerates no subset,
matching, path assignment, path permutation, or family of cyclic orders.
The declared finite limits and exact counts are recorded by the diagnostic
and its task evidence. These bounded checks corroborate but do not prove the
symbolic theorem.

All claims in this section concern induced \(K\) on the one unchanged core
fixed by (PGE2ODD-6). They do not modify the construction or production,
infer an angular or geometric conclusion, classify a global minimizing
order, or assert global optimality.

## 20. Exact \(K\) For The Fixed PGE5 Interval Shift

Retain exactly the \(e=5\) scaffold (PGE5-1)--(PGE5-4), with

\[
d=8m+5,\qquad n=10m+4,\qquad m\ge2,
\]

and fix

\[
q=\left\lfloor{4m+3\over5}\right\rfloor
=\kappa_{2m-1}.
\]

This section uses no other supported bijection.  Specializing (PGE5-22) to
the target \((q,2m-1)\) gives

\[
\boxed{
\alpha_m^{(5,\uparrow)}(j)=
\begin{cases}
j,&0\le j<q,\\
j+1,&q\le j\le2m-2,\\
q,&j=2m-1.
\end{cases}}
\tag{KPGE5-1}
\]

Thus \(P_q\) occupies the genuine closing gap and every residual path keeps
increasing path-index order.  With \(j^+=j+1\pmod {2m}\), reconstruct the
literal fixed core as

\[
\boxed{
\tau_m^{(5,\uparrow)}
=\mathop{\bigcirc}_{j=0}^{2m-1}
 (E_j,\lambda_j,P_{\alpha_m^{(5,\uparrow)}(j)},\rho_{j^+}).}
\tag{KPGE5-2}
\]

Every path is expanded in its unchanged orientation from (PGE5-4), and the
final \(\rho_0\) closes back to \(E_0\).  Put

\[
L=4m+1,\qquad
H_m=\{2,\ldots,4m\},\qquad
B_m=\{L,\ldots,10m+4\}.
\]

The exact maximizing-subset classification is

\[
\boxed{
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}
P_{\tau_m^{(5,\uparrow)}}(U)=\{B_m\}.}
\tag{KPGE5-3}
\]

In particular, this displayed singleton is the complete list of maximizing
subsets.  Its exact value is

\[
\boxed{
K(\tau_m^{(5,\uparrow)})
={572m^3+809m^2+8mq+329m+4q^2+20q+36\over2}.}
\tag{KPGE5-4}
\]

We prove the classification before using the block sum.

### Exact compressed backbone

Every member of \(H_m\) is isolated between two members of \(B_m\).  Deleting
all of them from (KPGE5-2), and starting at \(L=\rho_0\), gives

\[
\boxed{
\left(
L,
(E_j,P_j)_{j=0}^{q-1},
(E_j,P_{j+1})_{j=q}^{m-1},
E_m,a,b,
(E_j,x_{j+1})_{j=m+1}^{2m-2},
E_{2m-1},P_q
\right).}
\tag{KPGE5-5}
\]

All ranges are literal.  The shifted-triple range is empty exactly when
\(q=m\), hence at \(m=2,3\); the singleton range is empty exactly at
\(m=2\).  The doubleton

\[
(a,b)=(5m+3,5m+4)
\]

is present on every row and retains its orientation.

### Complete deletion-gain audit

For a hole \(z\in H_m\) between its two backbone neighbors \(u,w\), write

\[
h_z=uw-z(u+w).
\tag{KPGE5-6}
\]

Direct substitution in (KPGE5-5) gives exactly nine position classes:

\[
\begin{array}{c|c|c}
\text{hole}&\text{gap range}&h_z\\ \hline
\lambda_j&0\le j<q&
-4j^2+(28m+12)j+36m+20\\
\rho_{j+1}&0\le j<q&
-4j^2+(28m+8)j+52m+27\\
\lambda_j&q\le j\le m-1&
-4j^2+(28m+6)j+28m+10\\
\rho_{j+1}&q\le j\le m-1&
-4j^2+(28m+2)j+44m+13\\
\lambda_m&&17m^2+36m+15\\
\rho_{m+1}&&17m^2+60m+34\\
\lambda_j&m+1\le j\le2m-2&
5j^2+(28m+27)j-16m^2+16m+20\\
\rho_{j+1}&m+1\le j\le2m-2&
5j^2+(28m+32)j-16m^2+28m+34\\
\lambda_{2m-1}=2&&80m^2-20mq+36m-4q.
\end{array}
\tag{KPGE5-7}
\]

The middle two rows are precisely the doubleton holes.  The last row is the
literal cyclic closing hole between \(E_{2m-1}=n\) and \(A_q\); no
nonclosing right-hole formula has been continued across the cut.  The class
cardinalities sum to

\[
2q+2(m-q)+2+2(m-2)+1=4m-1=|H_m|,
\]

so every hole is present exactly once and \(\rho_0=L\) is correctly retained.

The forward differences of the six ranged classes, in table order, are

\[
\begin{gathered}
28m+8-8j,\quad28m+4-8j,\quad
28m+2-8j,\quad28m-2-8j,\\
10j+28m+32,\qquad10j+28m+37.
\end{gathered}
\tag{KPGE5-8}
\]

They are positive on their exact ranges.  The first left class has minimum
\(36m+20\) at \(j=0\), while the first right class starts at \(52m+27\).
If the shifted range is nonempty, then \(m\ge4\), \(q\ge3\), and \(q\le m\);
its two left-end excesses over \(36m+20\) satisfy

\[
h_{\lambda_q}-(36m+20)\ge64m+8,
\qquad
h_{\rho_{q+1}}-(36m+20)\ge80m-1.
\]

The doubleton excesses are \(17m^2-5\) and
\(17m^2+24m+14\).  When the singleton range is nonempty, its two initial
excesses at \(j=m+1\) are

\[
17m^2+45m+32,
\qquad
17m^2+62m+51.
\]

Finally, using \(q\le m\), the closing excess obeys

\[
h_{\lambda_{2m-1}}-(36m+20)
\ge60m^2-4m-20>0.
\]

Consequently every deletion is strictly profitable and

\[
\boxed{
\min_{z\in H_m}h_z=36m+20>0,}
\tag{KPGE5-9}
\]

with equality only for \(z=\lambda_0=4m\).

### Complete compressed-shortcut audit

Apply the exact identity (K825-8).  After deleting only the internal members
of \(H_m\) from an oriented arc, write its compressed path as

\[
C=(z_0,z_1,\ldots,z_s),\qquad s\ge2,
\qquad
M(C)=\sum_{i=0}^{s-1}z_i z_{i+1}-z_0z_s.
\tag{KPGE5-10}
\]

If an endpoint \(a\) is a hole, every boundary-adjacent internal vertex is
at least \(L\).  For the other endpoint \(b\), the four corners give

\[
M(C)\ge L(a+b)-ab\ge4L-4=16m.
\tag{KPGE5-11}
\]

This covers one or two low endpoints in both orientations.  It is strictly
larger than \(9\) at \(m=2\) and than \(4m+2\) for \(m\ge3\).

Now take both endpoints in \(B_m=[L,n]\).  For \(s=2\), a triple connector
\(c_k\), \(0\le k\le m\), has margin

\[
M(A_k,c_k,B_k)
=-8k^2+(32m+13)k+4m+2.
\tag{KPGE5-12}
\]

Its forward difference is \(32m+5-16k>0\), so the connector minimum is
\(4m+2\), uniquely at \(c_0\).  The two doubleton roles and every singleton
role have the exact margins

\[
\begin{aligned}
M(E_m,a,b)&=25m^2+26m+7,\\
M(a,b,E_{m+1})&=25m^2+44m+18,\\
M(E_j,x_{j+1},E_{j+1})
&=j^2+(8m+8)j+20m+14\\
&\ge9m^2+38m+23
\qquad(m+1\le j\le2m-2).
\end{aligned}
\tag{KPGE5-13}
\]

The singleton range is empty at \(m=2\).  The retained closing label
\(L=\rho_0\) lies literally between \(B_q\) and \(E_0\), with

\[
M(B_q,L,E_0)=8mq-16m+8q-7.
\tag{KPGE5-14}
\]

This equals \(9\) when \((m,q)=(2,2)\).  For \(m\ge3\), one has \(q\ge3\),
and its excess over \(4m+2\) is at least \(4m+15\).

The remaining two-edge middle roles are outer triple labels and terminals;
all are at least \(R=6m+3\).  For distinct endpoints \(u,w\in[L,n]\),

\[
y(u+w)-uw=y^2-(u-y)(w-y)
\]

gives, according as both endpoints are above \(y\), below \(y\), or on
opposite sides,

\[
M(C)\ge
\begin{cases}
20m^2+32m+9,&u,w>y,\\
32m^2+30m+7,&u,w<y,\\
(6m+3)^2,&u<y<w.
\end{cases}
\tag{KPGE5-15}
\]

The middle-role count is complete:

\[
(m+1)+2+(m-2)+1+2(m+1)+2m=6m+4=|B_m|,
\]

for connectors, doubleton members, singletons, \(L\), outer triple labels,
and terminals, respectively.

For \(s=3\), every adjacent pair of internal backbone labels contains one
member at least \(R=6m+3\) and the other at least \(L\), except for the
single doubleton pair \((a,b)\).  Since \(R+L=n\), reversing the path if
needed and taking the four corners of \([L,n]^2\) gives

\[
M(C)\ge z_0R+RL+Lz_3-z_0z_3\ge RL
=24m^2+18m+3.
\tag{KPGE5-16}
\]

The exceptional literal window is also strict:

\[
M(E_m,a,b,E_{m+1})=34m^2+54m+21.
\]

For every \(s\ge4\), all internal labels are at least \(L\), and another
four-corner calculation yields

\[
\begin{aligned}
M(C)
&\ge L(z_0+z_s)+(s-2)L^2-z_0z_s\\
&\ge12m^2-12m-6+(s-4)L^2.
\end{aligned}
\tag{KPGE5-17}
\]

Already at \(s=4\), this exceeds \(4m+2\) for every \(m\ge2\).  The full
compressed closing word is

\[
E_{2m-1},A_q,c_q,B_q,L,E_0.
\]

Thus (KPGE5-14) treats the retained closing middle role,
(KPGE5-16) treats both adjacent closing pairs, and (KPGE5-17) treats every
longer arc through the cut.  The distinct closing hole was already the last
row of (KPGE5-7).  Combining all lengths proves the exact equality
classification

\[
\boxed{
\min_{C:\,s\ge2}M(C)=
\begin{cases}
9,&m=2,\quad C=(15,9,21)=(B_q,L,E_0),\\
4m+2,&m\ge3,\quad C=(A_0,c_0,B_0).
\end{cases}}
\tag{KPGE5-18}
\]

In each branch the displayed forward arc is the unique equality arc in the
fixed cyclic presentation.

The strict gains (KPGE5-9), strict shortcuts (KPGE5-18), and the exact lemma
(K825-6)--(K825-9) now force every maximizing subset of cardinality at least
two to omit every hole and retain every backbone edge.  Hence it is exactly
\(B_m\).  Applying the same inequality to \(\{n-1,n\}\), with the product
counted twice, gives

\[
P_{\tau_m^{(5,\uparrow)}}(B_m)\ge2n(n-1)>n^2,
\]

so no singleton can tie.  This proves (KPGE5-3), including all equality
cases.

### Exact block sum and five residue classes

For a nonempty path \(P=(p_1,\ldots,p_s)\), put

\[
\mathcal C(x,P,y)=xp_1+\sum_{i=1}^{s-1}p_ip_{i+1}+p_sy.
\]

Reading (KPGE5-5) from \(L\), its score is

\[
\begin{aligned}
P_{\tau_m^{(5,\uparrow)}}(B_m)={}&LE_0
+\sum_{j=0}^{q-1}\mathcal C(E_j,P_j,E_{j+1})\\
&+\sum_{j=q}^{m-1}\mathcal C(E_j,P_{j+1},E_{j+1})
+\mathcal C(E_m,(a,b),E_{m+1})\\
&+\sum_{j=m+1}^{2m-2}x_{j+1}(E_j+E_{j+1})
+\mathcal C(E_{2m-1},P_q,L).
\end{aligned}
\tag{KPGE5-19}
\]

The repeated summands and boundary terms are

\[
\begin{aligned}
\mathcal C(E_j,P_j,E_{j+1})
&=-8j^2-16mj-16j+192m^2+204m+52,\\
\mathcal C(E_j,P_{j+1},E_{j+1})
&=-8j^2-16mj-28j+192m^2+172m+25,\\
\mathcal C(E_m,(a,b),E_{m+1})
&=115m^2+153m+51,\\
x_{j+1}(E_j+E_{j+1})
&=2j^2+(24m+19)j+64m^2+108m+44,\\
\mathcal C(E_{2m-1},P_q,L)
&=176m^2-28mq+152m-4q^2-11q+33,\\
LE_0&=32m^2+28m+5.
\end{aligned}
\tag{KPGE5-20}
\]

Standard sums of \(j\) and \(j^2\) on the exact ranges in (KPGE5-19) give
(KPGE5-4), including the empty singleton range at \(m=2\) and the empty
shifted-triple ranges at \(m=2,3\).

If \(r=m\bmod5\), write

\[
q={4m+c_r\over5},
\qquad
(c_0,c_1,c_2,c_3,c_4)=(0,1,2,3,-1).
\]

Then the five-branch expression is

\[
\boxed{
K(\tau_m^{(5,\uparrow)})
={14300m^3+20449m^2+(8625+72c_r)m
  +900+100c_r+4c_r^2\over50}.}
\tag{KPGE5-21}
\]

Explicitly,

\[
\begin{array}{c|c|c|c}
r&q&n\bmod50&50K(\tau_m^{(5,\uparrow)})\\ \hline
0&4m/5&4&14300m^3+20449m^2+8625m+900\\
1&(4m+1)/5&14&14300m^3+20449m^2+8697m+1004\\
2&(4m+2)/5&24&14300m^3+20449m^2+8769m+1116\\
3&(4m+3)/5&34&14300m^3+20449m^2+8841m+1236\\
4&(4m-1)/5&44&14300m^3+20449m^2+8553m+804.
\end{array}
\tag{KPGE5-22}
\]

The five rows begin respectively at \(m=5,6,2,3,4\).  Every numerator is
divisible by \(50\) on its stated class because it is the integer block score
(KPGE5-19); there is no residual correction.

### Minimum row

At \(m=2\), there is no singleton, the shifted-triple range is empty, and

\[
q=2,\qquad
\alpha_2^{(5,\uparrow)}=(0,1,3,2).
\]

The literal core is

\[
\begin{aligned}
\tau_2^{(5,\uparrow)}=(
&21,8,20,10,19,7,
22,6,18,11,17,5,\\
&23,4,13,14,3,
24,2,16,12,15,9).
\end{aligned}
\tag{KPGE5-23}
\]

Here the doubleton occupies \(G_2\), \(P_2\) closes, and

\[
\boxed{
B_2=\{9,\ldots,24\},\qquad
K(\tau_2^{(5,\uparrow)})=4297.}
\tag{KPGE5-24}
\]

The unique minimum deletion gain is \(92\) at \(\lambda_0=8\).  The stable
connector margin is \(10\), but the genuine closing shortcut
\((15,9,21)\) has the unique minimum \(9\).  At \(m=3\), one still has
\(q=m\) and an empty shifted-triple range, but both the doubleton and one
singleton are present; (KPGE5-3)--(KPGE5-4) remain unchanged and give
\(K=11958\).

### Pointwise and asymptotic comparison with canonical K825

On the same subsequence \(n=10m+4\), the parameters in (K825-1)--(K825-4)
are

\[
(e,v,\varepsilon,\chi,\Gamma)=(5,2m,1,0,-4m-2).
\]

The canonical order has the same unique maximizing label set \(B_m\), and

\[
\boxed{
K_{825}(m)={572m^3+819m^2+361m+44\over2}.}
\tag{KPGE5-25}
\]

This is a comparison of two different cyclic orders on the same labels.
Exact subtraction, performed after evaluating both scores, gives

\[
\boxed{
K(\tau_m^{(5,\uparrow)})-K_{825}(m)
=2q^2+4mq+10q-5m^2-16m-4.}
\tag{KPGE5-26}
\]

The right side is increasing in \(q\ge0\).  Since
\(q\le(4m+3)/5\),

\[
K(\tau_m^{(5,\uparrow)})-K_{825}(m)
\le{-13m^2-92m+68\over25}<0
\qquad(m\ge2).
\tag{KPGE5-27}
\]

Thus the fixed PGE5 shift is strictly smaller on every row, with no tie or
crossover.  The exact five pointwise gaps are

\[
\begin{array}{c|c}
m\bmod5&25\bigl(K_{825}-K(\tau_m^{(5,\uparrow)})\bigr)\\ \hline
0&13m^2+200m+100\\
1&13m^2+164m+48\\
2&13m^2+128m-8\\
3&13m^2+92m-68\\
4&13m^2+236m+148.
\end{array}
\tag{KPGE5-28}
\]

The first representative of each admitted residue class gives

\[
\begin{array}{c|c|c|c|c|c}
m&m\bmod5&q&K(\tau_m^{(5,\uparrow)})&K_{825}&K_{825}-K\\ \hline
2&2&2&4297&4309&12\\
3&3&3&11958&11971&13\\
4&4&3&25548&25600&52\\
5&0&4&46855&46912&57\\
6&1&5&77563&77623&60.
\end{array}
\]

For an exact asymptotic comparison, retain the same \(c_r\) as in
(KPGE5-21).  Substituting \(m=(n-4)/10\) gives

\[
\begin{aligned}
K(\tau_m^{(5,\uparrow)})
={}&{143\over500}n^3+{3289\over5000}n^2
+{360c_r-4351\over2500}n\\
&+{50c_r^2+890c_r-2417\over625},\\
K_{825}(m)
={}&{143\over500}n^3+{663\over1000}n^2
-{491\over500}n-{373\over125}.
\end{aligned}
\tag{KPGE5-29}
\]

Therefore

\[
\boxed{
K_{825}(m)-K(\tau_m^{(5,\uparrow)})
={13\over2500}n^2+O(n),
\qquad
{K(\tau_m^{(5,\uparrow)})\over K_{825}(m)}
=1-{1\over55n}+O(n^{-2}).}
\tag{KPGE5-30}
\]

Both fixed families retain cubic coefficient \(143/500\); this shift gives
a strict pointwise and quadratic-term improvement, not a new cubic
coefficient.

### Independent bounded verification and scope

The sole diagnostic for (KPGE5-1)--(KPGE5-30) is the standalone
standard-library script
`ops/TASK-20260720__pge5_interval_shift_exact_k/exact_diagnostic.py`.
It constructs only (KPGE5-1).  On \(m=2,\ldots,30\), a candidate-free
least-selected-position max-plus recurrence checks the exact score and the
complete argmax classification through 37,475,656 transitions.  A separate
all-oriented-arc traversal checks every hole gain, the exact raw-arc plus
hole-budget identity, and all 968,774 proper cyclic arcs, including every
arc through the displayed cut.  Formula, support, residue, and K825
comparisons continue through \(m=1000\).  The diagnostic enumerates no
subset, path assignment, path permutation, matching, supported-bijection
family, or permanent and imports no project or test helper.  These bounded
checks corroborate but do not prove the all-\(m\) theorem.

All claims in this section concern induced \(K\) on the one fixed core
(KPGE5-2).  They do not optimize over another PGE5 bijection, count the
Ferrers permanent, modify a construction or production code, infer an exact
angular or geometric statement, classify a global \(K\)-minimizer, or assert
global optimality.

## 21. Exact \(K\) For The PGE5 Singleton-Reversal Shift

Retain only the PGE5 scaffold (PGE5-1)--(PGE5-4), so

\[
d=8m+5,\qquad n=10m+4,\qquad m\ge2,
\qquad
q=\left\lfloor{4m+3\over5}\right\rfloor
=\kappa_{2m-1}.
\]

Starting from the accepted monotone interval shift (KPGE5-1), keep the
shift through the doubleton, reverse the entire actual singleton block, and
leave \(P_q\) in the genuine closing gap.  Explicitly, define just the one
map

\[
\boxed{
\alpha_m^{(5,*)}(j)=
\begin{cases}
j,&0\le j<q,\\
j+1,&q\le j\le m-1,\\
m+1,&j=m,\\
3m-j,&m+1\le j\le2m-2,\\
q,&j=2m-1.
\end{cases}}
\tag{KRPGE5-1}
\]

The five image blocks are

\[
[0,q-1],\qquad [q+1,m],\qquad\{m+1\},\qquad
[m+2,2m-1],\qquad\{q\}.
\tag{KRPGE5-2}
\]

They are disjoint and partition \(\{0,\ldots,2m-1\}\), with every empty
range interpreted literally.  Thus (KRPGE5-1) is a bijection.  It is also
supported by the exact PGE5 theorem.  The edge at \(j=0\) is the forced
edge \((0,0)\).  For \(1\le j<q\), (PGE5-15)--(PGE5-16) give
\(j\ge\kappa_j\); for \(q\le j\le m-1\), one has
\(j+1\ge\kappa_j\).  The image at \(j=m\) is the universal doubleton,
every image for \(m+1\le j\le2m-2\) is a universal singleton, and the
closing image is exactly \(q=\kappa_{2m-1}\).  Hence every positive-column
edge lies in (PGE5-23), and (PGE5-26) proves the exact fixed-construction
statement

\[
\boxed{
\alpha_m^{(5,*)}\text{ is a supported bijection},\qquad
W(\sigma_{\alpha_m^{(5,*)}})=W_n={d(d-1)\over2}.}
\tag{KRPGE5-3}
\]

This conclusion uses the complete all-distance PGE5 theorem; it is not an
adjacent-only inference.

With \(j^+=j+1\pmod{2m}\), reconstruct the literal core as

\[
\boxed{
\tau_m^{(5,*)}
=\mathop{\bigcirc}_{j=0}^{2m-1}
 (E_j,\lambda_j,P_{\alpha_m^{(5,*)}(j)},\rho_{j^+}).}
\tag{KRPGE5-4}
\]

Every path retains its orientation from (PGE5-4), and the final \(\rho_0\)
closes back to \(E_0\).  Put

\[
L=4m+1,\qquad H_m=\{2,\ldots,4m\},\qquad
B_m=\{L,\ldots,10m+4\}.
\tag{KRPGE5-5}
\]

The exact maximizing-subset classification is

\[
\boxed{
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}
P_{\tau_m^{(5,*)}}(U)=\{B_m\}.}
\tag{KRPGE5-6}
\]

Thus the displayed singleton is the complete argmax list.  Its value is

\[
\boxed{
K_*:=K(\tau_m^{(5,*)})
={1714m^3+2439m^2+24mq+965m+12q^2+60q+120\over6}.}
\tag{KRPGE5-7}
\]

We first prove (KRPGE5-6), without using the block sum as a substitute for
the shortcut audit.

### Exact compressed backbone

Every member of \(H_m\) is isolated between two members of \(B_m\).
Deleting all of them and starting at \(L=\rho_0\) gives the cyclic word

\[
\boxed{
\left(
L,
(E_j,P_j)_{j=0}^{q-1},
(E_j,P_{j+1})_{j=q}^{m-1},
E_m,a,b,
(E_j,x_{3m-j})_{j=m+1}^{2m-2},
E_{2m-1},P_q
\right).}
\tag{KRPGE5-8}
\]

Every indexed block is concatenated in increasing \(j\), while the path
indices in the singleton block decrease.  The shifted-triple range is empty
exactly at \(m=2,3\), because exactly there \(q=m\).  The singleton range
is empty exactly at \(m=2\), has one member at \(m=3\), and is first
reversed nontrivially at \(m=4\).  The doubleton
\((a,b)=(5m+3,5m+4)\) occurs on every row and keeps its orientation.

### Complete deletion-gain audit

For a hole \(z\in H_m\) between its backbone neighbors \(u,w\), put

\[
h_z=uw-z(u+w).
\tag{KRPGE5-9}
\]

Literal substitution in (KRPGE5-8) gives all nine position classes:

\[
\begin{array}{c|c|c}
\text{hole}&\text{gap range}&h_z\\ \hline
\lambda_j&0\le j<q&
-4j^2+(28m+12)j+36m+20\\
\rho_{j+1}&0\le j<q&
-4j^2+(28m+8)j+52m+27\\
\lambda_j&q\le j\le m-1&
-4j^2+(28m+6)j+28m+10\\
\rho_{j+1}&q\le j\le m-1&
-4j^2+(28m+2)j+44m+13\\
\lambda_m&&17m^2+36m+15\\
\rho_{m+1}&&17m^2+60m+34\\
\lambda_j&m+1\le j\le2m-2&
-j^2+(29m+14)j-4m^2+27m+15\\
\rho_{j+1}&m+1\le j\le2m-2&
-j^2+(29m+15)j-4m^2+45m+27\\
\lambda_{2m-1}=2&&80m^2-20mq+36m-4q.
\end{array}
\tag{KRPGE5-10}
\]

The middle two singleton rows are absent at \(m=2\).  The two unindexed
rows are exactly the doubleton holes.  The last row is the cyclic closing
hole between \(E_{2m-1}=n\) and \(A_q\); no nonclosing right-hole formula
has been continued across the cut.  The class cardinalities sum to

\[
2q+2(m-q)+2+2(m-2)+1=4m-1=|H_m|,
\]

so every hole occurs once and \(\rho_0=L\) is retained.

The forward differences of the six ranged classes, in table order, are

\[
\begin{gathered}
28m+8-8j,\quad28m+4-8j,\quad
28m+2-8j,\quad28m-2-8j,\\
29m+13-2j,\qquad29m+14-2j.
\end{gathered}
\tag{KRPGE5-11}
\]

They are positive on their literal ranges.  The first left class begins at
\(36m+20\), and the first right class begins at \(52m+27\).  If the
shifted-triple range is nonempty, its two left-end excesses over
\(36m+20\) are at least \(64m+8\) and \(80m-1\).  The two doubleton
excesses are

\[
17m^2-5,\qquad17m^2+24m+14.
\]

When the singleton range is nonempty, its two initial excesses are

\[
8(m+1)(3m+1),\qquad3(8m^2+17m+7).
\]

Finally, using \(q\le m\), the closing excess is at least
\(60m^2-4m-20>0\).  Therefore every deletion is strictly profitable and

\[
\boxed{
\min_{z\in H_m}h_z=36m+20>0,}
\tag{KRPGE5-12}
\]

with equality only for \(z=\lambda_0=4m\).

### Complete compressed-shortcut audit

Apply the exact identity (K825-8).  After deleting only the internal holes
from an oriented arc, write its compressed path as

\[
C=(z_0,z_1,\ldots,z_s),\qquad s\ge2,\qquad
M(C)=\sum_{i=0}^{s-1}z_i z_{i+1}-z_0z_s.
\tag{KRPGE5-13}
\]

If an endpoint \(a\) is a hole, each boundary-adjacent internal vertex is
at least \(L\).  For the other endpoint \(b\), the four corners give

\[
M(C)\ge L(a+b)-ab\ge4L-4=16m.
\tag{KRPGE5-14}
\]

This covers one or two low endpoints in both orientations and is strictly
above the final minimum below.

Now take both endpoints in \(B_m=[L,n]\).  For \(s=2\), a triple connector
has the assignment-independent margin

\[
M(A_k,c_k,B_k)
=-8k^2+(32m+13)k+4m+2,
\qquad0\le k\le m.
\tag{KRPGE5-15}
\]

Its forward difference is \(32m+5-16k>0\), so this class has the unique
minimum \(4m+2\) at \(c_0\).  The two separate doubleton roles are

\[
\begin{aligned}
M(E_m,a,b)&=25m^2+26m+7,\\
M(a,b,E_{m+1})&=25m^2+44m+18.
\end{aligned}
\tag{KRPGE5-16}
\]

For a reversed singleton put \(j=m+1+t\), where
\(0\le t\le m-3\).  Its exact terminal-to-terminal margin is

\[
\begin{aligned}
M(E_j,x_{3m-j},E_{j+1})
&=27m^2-24mt-3m-3t^2-22t-16\\
&\ge65m+23.
\end{aligned}
\tag{KRPGE5-17}
\]

The expression strictly decreases with \(t\), so the final singleton is
the unique minimum in this class.  The range is empty at \(m=2\) and has
one member at \(m=3\).

The retained closing label \(L=\rho_0\) lies between \(B_q\) and \(E_0\),
with

\[
M(B_q,L,E_0)=8mq-16m+8q-7.
\tag{KRPGE5-18}
\]

This is \(9\) at \((m,q)=(2,2)\).  For \(m\ge3\), one has \(q\ge3\),
and its excess over \(4m+2\) is at least \(4m+15\).

The remaining two-edge middle roles are outer triple labels and terminals,
all at least \(R=6m+3\).  For distinct endpoints \(u,w\in[L,n]\), the
identity

\[
y(u+w)-uw=y^2-(u-y)(w-y)
\]

gives, according as both endpoints are above \(y\), below \(y\), or on
opposite sides,

\[
M(C)\ge
\begin{cases}
20m^2+32m+9,&u,w>y,\\
32m^2+30m+7,&u,w<y,\\
(6m+3)^2,&u<y<w\text{ or }w<y<u.
\end{cases}
\tag{KRPGE5-19}
\]

The middle-role count

\[
(m+1)+2+(m-2)+1+2(m+1)+2m=6m+4=|B_m|
\]

accounts respectively for connectors, doubleton members, singletons,
\(L\), outer triple labels, and terminals.  Thus no two-edge role is
missing.

For \(s=3\), every adjacent pair of internal backbone labels contains one
member at least \(R\) and the other at least \(L\), except for the literal
doubleton pair.  Reversing the path if needed and checking the four endpoint
corners gives

\[
M(C)\ge RL=24m^2+18m+3.
\tag{KRPGE5-20}
\]

The reversed singleton blocks satisfy this property because every singleton
is flanked by terminals.  The exceptional doubleton window is also strict:

\[
M(E_m,a,b,E_{m+1})=34m^2+54m+21.
\]

For every \(s\ge4\), all internal labels are at least \(L\), and the four
corners give

\[
M(C)\ge
12m^2-12m-6+(s-4)L^2>4m+2.
\tag{KRPGE5-21}
\]

The full compressed closing word remains

\[
E_{2m-1},A_q,c_q,B_q,L,E_0.
\]

Thus (KRPGE5-18) treats the retained closing middle role,
(KRPGE5-20) treats both adjacent pairs through the cut, and
(KRPGE5-21) treats every longer cut-crossing arc.  The distinct closing
hole was already the final row of (KRPGE5-10).  Combining every endpoint,
length, middle-role, doubleton, and cyclic class proves

\[
\boxed{
\min_{C:\,s\ge2}M(C)=
\begin{cases}
9,&m=2,\quad C=(15,9,21)=(B_q,L,E_0),\\
4m+2,&m\ge3,\quad C=(A_0,c_0,B_0).
\end{cases}}
\tag{KRPGE5-22}
\]

In each row the displayed forward arc is the unique equality arc in the
fixed cyclic presentation.  The strict gains (KRPGE5-12), strict shortcuts
(KRPGE5-22), and exact lemma (K825-6)--(K825-9) force every maximizing
subset of cardinality at least two to omit every hole and retain every
backbone edge.  It is therefore exactly \(B_m\).  The same lemma applied to
\(\{n-1,n\}\), with its product counted twice, gives
\(P_{\tau_m^{(5,*)}}(B_m)\ge2n(n-1)>n^2\), so no singleton can tie.
This proves (KRPGE5-6), including every equality case.

### Exact block sum and five residue classes

For a nonempty path \(P=(p_1,\ldots,p_s)\), retain

\[
\mathcal C(x,P,y)=xp_1+\sum_{i=1}^{s-1}p_ip_{i+1}+p_sy.
\]

Reading (KRPGE5-8) from \(L\), the exact score is

\[
\begin{aligned}
K_*={}&LE_0
+\sum_{j=0}^{q-1}\mathcal C(E_j,P_j,E_{j+1})
+\sum_{j=q}^{m-1}\mathcal C(E_j,P_{j+1},E_{j+1})\\
&+\mathcal C(E_m,(a,b),E_{m+1})
+\sum_{j=m+1}^{2m-2}x_{3m-j}(E_j+E_{j+1})
+\mathcal C(E_{2m-1},P_q,L).
\end{aligned}
\tag{KRPGE5-23}
\]

The repeated summands and boundary terms are

\[
\begin{aligned}
\mathcal C(E_j,P_j,E_{j+1})
&=-8j^2-16mj-16j+192m^2+204m+52,\\
\mathcal C(E_j,P_{j+1},E_{j+1})
&=-8j^2-16mj-28j+192m^2+172m+25,\\
\mathcal C(E_m,(a,b),E_{m+1})
&=115m^2+153m+51,\\
x_{3m-j}(E_j+E_{j+1})
&=-2j^2-2mj-5j+112m^2+125m+33,\\
\mathcal C(E_{2m-1},P_q,L)
&=176m^2-28mq+152m-4q^2-11q+33,\\
LE_0&=32m^2+28m+5.
\end{aligned}
\tag{KRPGE5-24}
\]

Standard sums of \(j\) and \(j^2\) on the literal ranges of
(KRPGE5-23) give (KRPGE5-7), including both empty ranges.

If \(r=m\bmod5\), write

\[
q={4m+c_r\over5},\qquad
(c_0,c_1,c_2,c_3,c_4)=(0,1,2,3,-1).
\]

Then

\[
\boxed{
K_*={42850m^3+61647m^2+(25325+216c_r)m
 +3000+300c_r+12c_r^2\over150}.}
\tag{KRPGE5-25}
\]

Equivalently,

\[
\begin{array}{c|c|c|c}
r&q&n\bmod50&150K_*\\ \hline
0&4m/5&4&42850m^3+61647m^2+25325m+3000\\
1&(4m+1)/5&14&42850m^3+61647m^2+25541m+3312\\
2&(4m+2)/5&24&42850m^3+61647m^2+25757m+3648\\
3&(4m+3)/5&34&42850m^3+61647m^2+25973m+4008\\
4&(4m-1)/5&44&42850m^3+61647m^2+25109m+2712.
\end{array}
\tag{KRPGE5-26}
\]

The five rows begin at \(m=5,6,2,3,4\), respectively.  Every numerator
is divisible by \(150\) on its stated class because it is the integer block
score (KRPGE5-23); there is no residual correction.

### Boundary rows and the singleton-reversal target

At \(m=2\), both the shifted-triple and singleton ranges are empty,
\(q=2\), and

\[
\alpha_2^{(5,*)}=(0,1,3,2),\qquad
B_2=\{9,\ldots,24\},\qquad K_*=4297.
\]

The doubleton occupies \(G_2\), \(P_2\) closes, and the literal core is
exactly the one displayed in (KPGE5-23).  Its unique deletion and shortcut
minima are \(92\) at \(\lambda_0\) and \(9\) on the genuine closing arc.
At \(m=3\), the shifted-triple range is still empty and the singleton block
has one member, so reversal is order-neutral:

\[
\alpha_3^{(5,*)}=(0,1,2,4,5,3),\qquad K_*=11958.
\]

At \(m=4\), the first nontrivial reversal is

\[
\alpha_4^{(5,*)}=(0,1,2,4,5,7,6,3),\qquad K_*=25546.
\tag{KRPGE5-27}
\]

Let \(K_\uparrow=K(\tau_m^{(5,\uparrow)})\) be the accepted score from
Section 20.  The two backbones agree outside the singleton gaps.  In gap
\(j\), the monotone singleton is \(x_{j+1}\), while the new singleton is
\(x_{3m-j}\).  Direct edge cancellation therefore gives

\[
\begin{aligned}
K_\uparrow-K_*
&=\sum_{j=m+1}^{2m-2}
 (x_{j+1}-x_{3m-j})(E_j+E_{j+1})\\
&=\sum_{j=m+1}^{2m-2}
 (2j-3m+1)(16m+11+2j)\\
&=\boxed{{(m-1)(m-2)(m-3)\over3}}\\
&={ (n-14)(n-24)(n-34)\over3000}.
\end{aligned}
\tag{KRPGE5-28}
\]

Thus the proposed target is **proved**, including the empty sum at \(m=2\)
and the zero singleton contribution at \(m=3\).  The gain is strictly
positive exactly for \(m\ge4\).  The individual summands can have mixed
signs; (KRPGE5-28) is an aggregate cyclic-score identity, not a gapwise
dominance statement.

### Pointwise comparison with canonical K825

On the same \(n=10m+4\) row, retain (KPGE5-25):

\[
K_{825}(m)={572m^3+819m^2+361m+44\over2}.
\]

Exact subtraction from (KRPGE5-7) gives

\[
\boxed{
K_{825}(m)-K_*
={m^3+9m^2-12mq+59m-6q^2-30q+6\over3}.}
\tag{KRPGE5-29}
\]

The numerator decreases with \(q\ge0\).  Since \(q\le m\), for \(m\ge3\)
it is at least

\[
m^3-9m^2+29m+6=(m-3)^3+2m+33>0.
\]

At \(m=2\), its literal value is \(36\).  Hence K825 is strictly larger
on every row, with no tie or crossover.  The exact five pointwise branches
are

\[
\begin{array}{c|c}
m\bmod5&75(K_{825}-K_*)\\ \hline
0&25m^3-111m^2+875m+150\\
1&25m^3-111m^2+767m-6\\
2&25m^3-111m^2+659m-174\\
3&25m^3-111m^2+551m-354\\
4&25m^3-111m^2+983m+294.
\end{array}
\tag{KRPGE5-30}
\]

The first representative of every admitted residue class gives

\[
\begin{array}{c|c|c|c|c|c}
m&m\bmod5&q&K_*&K_\uparrow&K_{825}\\ \hline
2&2&2&4297&4297&4309\\
3&3&3&11958&11958&11971\\
4&4&3&25546&25548&25600\\
5&0&4&46847&46855&46912\\
6&1&5&77543&77563&77623.
\end{array}
\]

Finally, \(q=\lfloor(2n+7)/25\rfloor\), and direct substitution gives

\[
\boxed{
3000K_*=857n^3+1911n^2+1200nq-8174n
 +6000q^2+25200q+7272.}
\tag{KRPGE5-31}
\]

Consequently

\[
\boxed{
K_*={857\over3000}n^3+O(n^2),\qquad
K_{825}-K_*={1\over3000}n^3+O(n^2).}
\tag{KRPGE5-32}
\]

Equivalently, (KRPGE5-28) supplies the full reduction from the monotone
coefficient \(143/500=858/3000\) to \(857/3000\).  This is a coefficient
for one fixed PGE5 subsequence and one fixed supported order, not a global
minimizing-order or geometric coefficient theorem.

### Independent bounded verification and scope

The sole diagnostic for (KRPGE5-1)--(KRPGE5-32) is the standalone
standard-library script
`ops/TASK-20260720__pge5_singleton_reversal_exact_k/exact_diagnostic.py`.
On \(m=2,\ldots,30\), a candidate-free least-selected-position max-plus
recurrence checks the exact score and complete argmax classification.  A
separate all-oriented-arc traversal checks every deletion budget, the exact
raw-arc plus hole-budget identity, and every proper cyclic arc, including all
arcs through the displayed cut.  Formula, support, five-residue, target, and
K825 checks continue through \(m=1000\).  The accepted monotone order is
reconstructed only for the pointwise cancellation check.  The script imports
no project or test helper and searches no path assignment, matching,
supported-bijection family, subset, cyclic-order family, or permanent.  These
bounded computations corroborate but do not prove the all-\(m\) theorem.

All claims in this section concern \(W\) and induced \(K\) for the one map
(KRPGE5-1).  They change no production or test file, optimize no other PGE5
bijection, count no permanent, infer no angular or geometric result, and
assert no global \(K\)-minimality or global optimality.

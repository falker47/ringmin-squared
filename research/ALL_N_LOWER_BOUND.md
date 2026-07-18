# All-n Bounds And Radius-One Insertion

Date: 2026-07-13

Last updated: 2026-07-18

## Classification

- EXACT THEOREM: for every integer \(n\ge 3\),
  \[
  R_2^*(n)\ge {n(n+1)(n+2)\over 6\pi}-n^2.
  \]
- EXACT THEOREM: if \(n\ge 4\) and \(1\le m\le n-2\), then
  \[
  R_2^*(n)\ge {P_{m,n}\over \pi}-n^2,
  \]
  where
  \[
  P_{m,n}
  =
  \sum_{k=m}^n k(m+n-k)
  =
  {(n-m+1)(m^2+4mn+m+n^2-n)\over 6}.
  \]
- EXACT THEOREM: within the specific relaxation "induced subset plus
  duplicated-multiset pairing plus
  \(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\)", the best bound over all subsets of
  fixed cardinality \(q\) is achieved uniquely by the tail
  \(\{n-q+1,\dots,n\}\). Therefore no nonconsecutive subset improves the
  corresponding \(P_{m,n}\) bound inside this method.
- EXACT THEOREM: the discrete maximum of \(P_{m,n}\) over
  \(1\le m\le n-2\) is characterized exactly by
  \[
  \rho_n={\sqrt{8n^2+8n+1}-(2n+1)\over 2}.
  \]
  For \(n\ge 4\), if \(\rho_n\notin\mathbb Z\) the unique maximizer is
  \(m=\lfloor\rho_n\rfloor+1\); if \(\rho_n\in\mathbb Z\), the two maximizers
  are \(m=\rho_n\) and \(m=\rho_n+1\). For \(n=3\), the admissible set is the
  singleton \(m=1\).
- EXACT THEOREM (single-subset consequence):
  \[
  \liminf_{n\to\infty}{6\pi R_2^*(n)\over n^3}
  \ge
  4(\sqrt2-1)>1.
  \]
- EXACT THEOREM (two-nested-tail geometric refinement): let
  \(\beta_n^{(2)}\) be the exact two-tail obstruction defined in
  `research/FIXED_ORDER_CYCLE_RATIO.md`. Then, for \(n\ge4\),
  \[
  R_2^*(n)>{\beta_n^{(2)}\over\pi}-n^2,
  \qquad
  \beta_n^{(2)}
  ={2(\sqrt2-1)\over3}n^3+O(n^2).
  \]
  The refinement can improve finite lower terms but provably leaves this
  schema's leading lower coefficient unchanged.
- EXACT THEOREM (jointly optimized one-prefix linear-block refinement): put
  \[
  r_n^*=\left\lfloor\left(1-{\sqrt3\over3}\right)n\right\rfloor,
  \qquad
  s_n^*=\left\lceil
  \left({5\over6}-{\sqrt3\over4}\right)n
  \right\rceil,
  \qquad
  \lambda_*={88-32\sqrt3\over73}.
  \]
  With the consecutive-tail quantities defined in
  `research/FIXED_ORDER_CYCLE_RATIO.md`, the literal floor/ceiling statement
  holds for every \(n\ge86\):
  \[
  \Lambda_n
  \ge\Gamma_n^{(r_n^*)}
  \ge\gamma^{(r_n^*)}_{1,n}
  \ge P_{r_n^*,n}+(r_n^*-s_n^*)F_n^*.
  \]
  No maximum and minimum are exchanged: for each fixed \(m\), pointwise
  domination by \(\Lambda(\sigma)\) is minimized first, and only the resulting
  scalar lower bounds are maximized over \(m\). Consequently, for
  \(n\ge90\), one has the explicit finite bounds
  \[
  \Lambda_n\ge {4+2\sqrt3\over27}n^3,
  \qquad
  R_2^*(n)>{4+2\sqrt3\over27\pi}n^3-n^2,
  \]
  and hence
  \[
  \liminf_{n\to\infty}{\Lambda_n\over n^3}
  \ge {4+2\sqrt3\over27},
  \qquad
  \liminf_{n\to\infty}{R_2^*(n)\over n^3}
  \ge {4+2\sqrt3\over27\pi}.
  \]
  These are lower coefficients, not exact asymptotic coefficients or a
  convergence theorem.
- EXACT THEOREM (globally optimized two-prefix linear-block refinement): for
  arbitrary constants
  \(0<\beta_2<\beta_1<\alpha<1\) and
  \(0\le\lambda_{\rm lo}\le\lambda_{\rm hi}\le1\), the exact two-prefix
  theorem in `research/FIXED_ORDER_CYCLE_RATIO.md` charges every original
  base-edge slack at most once and covers all recursive child-edge splits.
  Exact reduction of the ordered weights, all six density branches, both
  nontrivial transitions, and every compact boundary/collision face gives
  the unique global optimizer
  \[
  \left(
  {629-23\sqrt{143}\over829},
  {2286-77\sqrt{143}\over3316},
  {2010-59\sqrt{143}\over3316},
  {6264-288\sqrt{143}\over5281},
  {3888-192\sqrt{143}\over4273}
  \right),
  \]
  in the order
  \((\alpha,\beta_1,\beta_2,\lambda_{\rm hi},\lambda_{\rm lo})\). Its
  exact template-optimal coefficient is
  \[
  C_{2,*}={491596+6578\sqrt{143}\over2061723}.
  \]
  Hence
  \[
  \liminf{\Lambda_n\over n^3}\ge C_{2,*},
  \qquad
  \liminf{R_2^*(n)\over n^3}\ge{C_{2,*}\over\pi}.
  \]
  No finite rounding theorem for this irrational two-prefix optimizer is
  asserted.
- EXACT THEOREM (globally optimized three-prefix linear-block refinement):
  combine the three selected heights before assigning any edge slack, with
  \[
  0<\beta_3<\beta_2<\beta_1<\alpha<1,
  \qquad
  0\le\lambda_3\le\lambda_2\le\lambda_1\le1.
  \]
  One global partition then uses every original base-edge slack at most once
  and covers every recursive child edge, including fully nested histories
  across both segment boundaries. The three clipped individual weight optima
  are automatically ordered. Exact optimization on the full compact closure
  gives
  \[
  {X_1\over A}={1058\over1263},
  \qquad
  {X_2\over A}={276\over421},
  \qquad
  {X_3\over A}={184\over421},
  \]
  where \(A=3\alpha-1\) and \(X_i=4\beta_i-(1+\alpha)\), and the unique
  template-optimal coefficient is
  \[
  C_{3,*}
  ={753972193324+106042322\sqrt{377823}\over2960667770787}
  =0.276678647461945\ldots>C_{2,*}.
  \]
  Hence
  \[
  \liminf{\Lambda_n\over n^3}\ge C_{3,*},
  \qquad
  \liminf{R_2^*(n)\over n^3}\ge{C_{3,*}\over\pi}.
  \]
  Its exact floor/ceiling specialization has minimal uniform threshold
  \(n=159\). With \(r_n=\lfloor\alpha_*n\rfloor\),
  \(s_{i,n}=\lceil\beta_{i,*}n\rceil\), \(S_n=n+r_n\), and finite
  middle-clipped floors \(\widehat F_{i,n}=(4s_{i,n}-S_n)^2/2\), the literal
  expression \(\mathcal B_{3,n}\) and integer closure
  \(\mathcal I_{3,n}=\lceil\mathcal B_{3,n}\rceil\) satisfy
  \[
  \Lambda_n\ge\mathcal I_{3,n}\ge\mathcal B_{3,n}>C_{3,*}n^3,
  \qquad
  R_2^*(n)>{\mathcal I_{3,n}\over\pi}-n^2
  \quad(n\ge159).
  \]
- EXACT THEOREM (globally optimized four-prefix linear-block refinement): for
  \[
  0<\beta_4<\beta_3<\beta_2<\beta_1<\alpha<1,
  \qquad
  0\le\lambda_4\le\lambda_3\le\lambda_2\le\lambda_1\le1,
  \]
  combine all four selected heights before assigning slack. The five convex
  coefficients telescope to four disjoint split segments; one canonical
  original-edge partition uses each base slack once or leaves it unused, and
  the recursive invariant covers every nested child edge through all three
  boundaries. For every finite \(n\) satisfying the full admissibility
  conditions
  \[
  2\le r\le n-2,
  \qquad
  1\le s_4<s_3<s_2<s_1\le r-1,
  \]
  the exact bound is
  \[
  \begin{aligned}
  \gamma^{(r)}_{1,n}\ge{}& P_{r,n}
  +(r-s_1)F_{1,n}
  +(s_1-s_2)F_{2,n}\\
  &+(s_2-s_3)F_{3,n}
  +(s_3-s_4)F_{4,n}.
  \end{aligned}
  \]
  Its fixed-parameter coefficient \(C_4\) is recorded below. On the compact
  closure of the ordered densities and weights, the weight problem reduces
  exactly to four clipped individual optima. All fifteen clipping regimes,
  every transition, density collision, and compact facet are classified in
  `research/FIXED_ORDER_CYCLE_RATIO.md`. The unique global point is strict,
  lies in `MMMM`, and has
  \[
  \alpha_*={18170840871749-3666143\sqrt{2903456040383}
   \over27631313622349}.
  \]
  With \(A_*=3\alpha_*-1\) and
  \[
  (x_1,x_2,x_3,x_4)
  ={(3190338,2672508,2091528,1394352)\over3666143},
  \]
  the remaining unique coordinates are
  \[
  \beta_{i,*}={1+\alpha_*+x_iA_*\over4},
  \qquad
  \lambda_{i,*}={x_iA_*\over\beta_{i,*}}.
  \]
  The exact optimum is
  \[
  C_{4,*}
  ={597580022071777213687318156
   +21288970076515705538\sqrt{2903456040383}
   \over2290468477489828247376833403}
  =0.276736149860989\ldots>C_{3,*}.
  \]
  Hence
  \[
  \liminf{\Lambda_n\over n^3}\ge C_{4,*},
  \qquad
  \liminf{R_2^*(n)\over n^3}\ge{C_{4,*}\over\pi}.
  \]
  No finite rounding theorem is asserted. This four-prefix optimization does
  not itself supply the separate arbitrary finite-prefix charging theorem
  below.
- EXACT FINITE METHOD-SPECIFIC THEOREM (ARBITRARILY MANY FINITE PREFIXES):
  for every fixed integer \(k\ge1\), let
  \[
  0<\beta_k<\cdots<\beta_1<\alpha<1,
  \qquad
  0\le\lambda_k\le\cdots\le\lambda_1\le1,
  \]
  put \(r=\lfloor\alpha n\rfloor\),
  \(s_i=\lceil\beta_i n\rceil\), and \(s_0=r\). Whenever
  \[
  2\le r\le n-2,
  \qquad
  1\le s_k<\cdots<s_1\le r-1,
  \]
  the exact combined-height one-use theorem gives
  \[
  \gamma^{(r)}_{1,n}\ge
  P_{r,n}+\sum_{i=1}^k(s_{i-1}-s_i)G_{n,\lambda_i}(s_i).
  \]
  The convex telescope, canonical original-edge slack partition, and
  descending recursive induction are independent of the finite frontier
  count. By itself this pointwise theorem supplies no uniform asymptotic
  control for \(k=k(n)\), but its separate fixed-\(k\) instances can be
  combined with the normalized simplex as follows.
- EXACT METHOD-SPECIFIC ASYMPTOTIC COROLLARY (ALL FIXED \(k\)): fix
  \[
  \alpha_\infty={13-2\sqrt2\over23}.
  \]
  For each finite \(k\), let \(x^{(k)}\) be the unique normalized simplex
  maximizer and set
  \[
  \beta_i={1+\alpha_\infty+(3\alpha_\infty-1)x_i^{(k)}\over4},
  \qquad
  \lambda_i={(3\alpha_\infty-1)x_i^{(k)}\over\beta_i}.
  \]
  The parameters are strictly ordered and all-middle. Applying the charging
  theorem separately at each fixed \(k\), taking the fixed-parameter liminf,
  and then taking the supremum of the resulting scalar inequalities gives
  \[
  \liminf_{n\to\infty}{\Lambda_n\over n^3}
  \ge {434+4\sqrt2\over1587},
  \qquad
  \liminf_{n\to\infty}{R_2^*(n)\over n^3}
  \ge {434+4\sqrt2\over1587\pi}.
  \]
  No \(k=k(n)\), threshold uniform in \(k\), or interchange of limits is
  used. The full clipped arbitrary-\(k\) optimization proves in addition
  that this coefficient is the exact, unattained supremum of the entire
  continuous finite-prefix template family, not only of its all-middle
  subfamily. It is strictly larger than \(C_{5,*}\).
- EXACT THEOREM (globally optimized five-prefix linear-block refinement):
  optimizing the \(k=5\) specialization on the complete eleven-parameter
  compact closure reduces the ordered weights coordinatewise. All 21 clipping
  regimes, every transition, density and weight collision, and every compact
  face are classified in research/FIXED_ORDER_CYCLE_RATIO.md. The unique
  point is strictly all-middle, with
  \[
  \alpha_{5,*}
  ={422413777961580309772684503
   -10047852311701\sqrt{183342238504950468196395903}
   \over661485317418210151348973103}.
  \]
  Its five exact cutoff/weight pairs are (CR28dz37)--(CR28dz38), and
  \[
  C_{5,*}
  ={346693217780244687187063490332457027500975566238012204
   +1228130489996268437333105902690103574002
    \sqrt{183342238504950468196395903}
   \over1312688475479610714750859896048564873968757997852345827}
  >C_{5,\mathrm{rat}}>C_{4,*}.
  \]
  Hence
  \[
  \liminf{\Lambda_n\over n^3}\ge C_{5,*},
  \qquad
  \liminf{R_2^*(n)\over n^3}\ge{C_{5,*}\over\pi}.
  \]
  No finite rounding theorem at this irrational optimizer is asserted.
  This remains the exact global optimum of the fixed \(k=5\) template, not
  the strongest coefficient obtained from all fixed finite \(k\).
- EXACT METHOD-SPECIFIC ASYMPTOTIC COROLLARY (EXPLICIT FIVE-PREFIX WITNESS):
  combine the preceding theorem at fixed \(k=5\) with the exact fifth
  normalized-simplex row and choose \(\alpha=13/30\). The resulting rational
  parameters are strictly ordered and all middle-clipped. Their coefficient is
  \[
  C_{5,\mathrm{rat}}
  ={2263404122555368590593580404287
   \over8177706222298165502582585481000}
  >{75\over271}>C_{4,*}.
  \]
  Therefore
  \[
  \liminf{\Lambda_n\over n^3}\ge C_{5,\mathrm{rat}},
  \qquad
  \liminf{R_2^*(n)\over n^3}\ge{C_{5,\mathrm{rat}}\over\pi}.
  \]
  This fixed rational specialization is strictly suboptimal by the preceding
  global theorem.
  Keeping exactly those rational weights, the finite floor/ceiling theorem has
  minimal uniform threshold \(234\). Its literal expression
  \(\mathcal B_{5,n}\) and integer closure
  \(\mathcal I_{5,n}=\lceil\mathcal B_{5,n}\rceil\) satisfy
  \[
  \Lambda_n\ge\mathcal I_{5,n}\ge\mathcal B_{5,n}
  >C_{5,\mathrm{rat}}n^3
  \qquad(n\ge234).
  \]
- EXACT FINITE THEOREM (two-prefix rational specialization): with
  \[
  r_n=\left\lfloor{3n\over7}\right\rfloor,
  \qquad
  s_{1,n}=\left\lceil{2n\over5}\right\rceil,
  \qquad
  s_{2,n}=\left\lceil{3n\over8}\right\rceil,
  \]
  and weights
  \((\lambda_{\rm hi},\lambda_{\rm lo})=(1/2,1/4)\), the exact two-prefix
  theorem has a uniform floor/ceiling domain starting at the minimal
  threshold \(n=59\), and
  \[
  \Lambda_n\ge {72825421\over263424000}n^3,
  \qquad
  R_2^*(n)>{72825421\over263424000\pi}n^3-n^2
  \quad(n\ge59).
  \]
  The rational coefficient is strictly larger than
  \((4+2\sqrt3)/27\) and strictly smaller than \(C_{2,*}\). It remains the
  earlier explicit rational two-prefix finite-\(n\) witness, not an exact
  asymptotic coefficient.
- EXACT THEOREM: if a configuration of the core radii
  \(2^2,\dots,n^2\) is feasible at central radius \(R>0\), then a circle of
  radius \(1\) can be inserted at the same central radius whenever
  \[
  \sum_{j=2}^n\theta_R(1,j^2)<\pi.
  \]
  The proof uses the measure of the union of all forbidden angular arcs and
  checks every new pairwise constraint.
- EXACT THEOREM: define \(R^*_{2:n}\) as the infimum feasible central radius
  for the core radii \(2^2,\dots,n^2\). Then
  \[
  R_2^*(n)=R^*_{2:n}\qquad(n\ge 12).
  \]
  In fact, for every \(n\ge12\), the full problem and the core problem have
  exactly the same set of feasible positive central radii. The threshold
  \(12\) is sufficient; no minimal-threshold claim is made.
- EXACT THEOREM: for every \(n\ge12\), the regular \((n-1)\)-gon construction
  for the core radii gives
  \[
  R_2^*(n)\le U_n,
  \]
  where
  \[
  U_n
  =
  \sqrt{
  n^2(n-1)^2\csc^2\!\left({\pi\over n-1}\right)
  +{(2n-1)^2\over4}}
  -{n^2+(n-1)^2\over2}.
  \]
  The construction verifies every core pair, including non-adjacent
  regular-polygon directions, and then uses the exact radius-one insertion
  theorem.
- EXACT THEOREM: define
  \[
  M_n=n\left(\left\lfloor{n\over2}\right\rfloor+1\right),
  \qquad
  V_n={(n-1)M_n\over\pi}.
  \]
  Assigning the core indices to the same regular-polygon directions in the
  zigzag order
  \[
  z_n=(n,2,n-1,3,\dots)
  \]
  is all-pairs feasible at \(V_n\). Hence
  \[
  R_2^*(n)\le V_n\qquad(n\ge12).
  \]
- EXACT THEOREM:
  \[
  \limsup_{n\to\infty}{R_2^*(n)\over n^3}\le {1\over2\pi},
  \qquad
  R_2^*(n)=\Theta(n^3).
  \]
  The \(\Theta(n^3)\) conclusion combines this construction with the
  induced-subset lower bound; it does not identify an exact leading constant.
- EXACT THEOREM (later product-distance refinement): the explicit orders in
  `research/PRODUCT_DISTANCE_SURROGATE.md` satisfy
  \(W(\sigma_n)\le d_n(d_n-1)/2\), where
  \(d_n=\lceil(4n+8)/5\rceil\). The core construction and insertion theorem
  therefore give the regular-direction geometric upper coefficient
  \[
  \limsup_{n\to\infty}{R_2^*(n)\over n^3}\le {8\over25\pi}.
  \]
- EXACT THEOREM (later shortcut refinement): evaluating the induced-subset
  objective \(K\) exactly on the same canonical core order gives
  \[
  K(\tau_n)={143\over500}n^3+O(n^2).
  \]
  Exact label-one elimination and the fixed-order angular sandwich therefore
  sharpen the current geometric upper coefficient to
  \[
  \limsup_{n\to\infty}{R_2^*(n)\over n^3}\le {143\over500\pi}.
  \]
- DISPROVED CLAIM:
  \[
  R_2^*(n)= {n^3\over 6\pi}(1+o(1)).
  \]
- DISPROVED CLAIM:
  \[
  R_2^*(n)= {n^3\over 6\pi}+O(n^2).
  \]

The lower-bound proof uses only necessary consequences of all-pairs feasibility.
The coefficient \(2(\sqrt2-1)/(3\pi)\) remains optimal for the
single-subset pairing relaxation analyzed directly here. The relational
extension using two consecutive tails is a distinct, stronger finite schema;
its separate exact analysis proves the same leading coefficient. The jointly
optimized one-prefix linear block first improves the global lower coefficient
to \((4+2\sqrt3)/(27\pi)\), and the globally optimized two-prefix CR28bw
template improves it again to
\((491596+6578\sqrt{143})/(2061723\pi)\). The globally optimized
three-prefix template raises it further to
\[
{753972193324+106042322\sqrt{377823}\over2960667770787\pi}.
\]
The globally optimized four-prefix template raises it again to
\[
{597580022071777213687318156
 +21288970076515705538\sqrt{2903456040383}
 \over2290468477489828247376833403\pi}.
\]
The explicit rational five-prefix witness at \(\alpha=13/30\) first raises
the coefficient to
\[
{2263404122555368590593580404287
 \over8177706222298165502582585481000\pi}.
\]
The full global five-prefix optimization raises the fixed-\(k=5\) template
coefficient further to
\[
{346693217780244687187063490332457027500975566238012204
 +1228130489996268437333105902690103574002
  \sqrt{183342238504950468196395903}
 \over1312688475479610714750859896048564873968757997852345827\pi}.
\]
It remains the exact optimum of that five-prefix template. Combining the
arbitrary finite-prefix charging theorem with the normalized optimizer at
every fixed finite \(k\), all at the single strict density
\(\alpha_\infty=(13-2\sqrt2)/23\), raises the current lower coefficient to
\[
\boxed{{434+4\sqrt2\over1587\pi}}.
\]
This is a supremum of fixed-\(k\) scalar inequalities, not a growing-\(k\)
certificate.
None of these lower-bound results is an upper
bound on the true problem. The order-independent regular-core baseline has
upper coefficient \(1/\pi\), the zigzag refinement gives \(1/(2\pi)\), and
the later product-distance construction gives \(8/(25\pi)\) on regular
directions. Exact shortcut evaluation of the same core order sharpens the
current variable-spacing upper coefficient to \(143/(500\pi)\). This still
does not match the current lower coefficient. Thus no exact leading constant,
limiting coefficient, or leading-term asymptotic formula is proved.

## Domain And Definitions

Fix \(n\ge 3\). The Power-Ringmin radii are
\[
r_i=i^2,\qquad i=1,\dots,n.
\]

Let
\[
\mathcal F_n
=
\{R>0:\text{the radii }1^2,\dots,n^2\text{ are feasible at }R\}
\]
and
\[
\mathcal C_n
=
\{R>0:\text{the core radii }2^2,\dots,n^2\text{ are feasible at }R\}.
\]
In this note the optimum symbols mean infima:
\[
R_2^*(n)=\inf\mathcal F_n,
\qquad
R^*_{2:n}=\inf\mathcal C_n.
\]
No attainment assumption is used below.

For a central radius \(R>0\), the minimum central angle needed between two
peripheral circles of radii \(a,b>0\), both externally tangent to the central
circle, is
\[
\theta_R(a,b)
=
2\arcsin\sqrt{ab\over (R+a)(R+b)}.
\]
Thus for quadratic radii,
\[
\theta_R(i^2,j^2)
=
2\arcsin\left({ij\over \sqrt{(R+i^2)(R+j^2)}}\right).
\]

For \(n\ge 3\), a feasible configuration cannot have \(R=0\): at \(R=0\),
every center lies on a ray from the origin at distance \(i^2\), and two
peripheral circles of radii \(i^2,j^2\) are disjoint only when their rays are
opposite; three or more distinct peripheral circles cannot all be pairwise
opposite. Hence every feasible configuration relevant to \(R_2^*(n)\) has
\(R>0\), and the displayed angular formula applies.

## Combinatorial Pairing Lemma

Lemma. Let
\[
S=\{s_1<s_2<\cdots<s_q\}
\]
be a set of \(q\ge 3\) positive indices. Let
\[
M_S=\{s_1,s_1,s_2,s_2,\dots,s_q,s_q\}
\]
be sorted as
\[
x_1\le x_2\le \cdots\le x_{2q}.
\]
For every cyclic order \(\tau=(\tau_1,\dots,\tau_q)\) of \(S\),
\[
\sum_{\ell=1}^q \tau_\ell\tau_{\ell+1}
\ge
\sum_{\ell=1}^q x_\ell x_{2q+1-\ell},
\]
with \(\tau_{q+1}=\tau_1\).

Proof. First recall the standard rearrangement pairing form. Let
\[
x_1\le x_2\le \cdots \le x_{2q}
\]
be nonnegative real numbers. Among all partitions of these \(2q\) entries into
\(q\) unordered pairs, the sum of pair-products is minimized by pairing the
smallest entry with the largest, the second-smallest with the second-largest,
and so on:
\[
\sum_{\{p,r\}}x_px_r
\ge
\sum_{\ell=1}^q x_\ell x_{2q+1-\ell}.
\]
Indeed, in a minimizing pairing, if \(x_1\) is paired with \(x_j\) and
\(x_{2q}\) is paired with \(x_k\), where \(j<2q\), replacing those two pairs by
\(\{x_1,x_{2q}\}\) and \(\{x_j,x_k\}\) changes the product sum by
\[
\bigl(x_1x_j+x_kx_{2q}\bigr)
-
\bigl(x_1x_{2q}+x_kx_j\bigr)
=
(x_k-x_1)(x_{2q}-x_j)\ge 0.
\]
Thus some minimum has \(x_1\) paired with \(x_{2q}\), and induction gives the
claim.

The \(q\) adjacent edges of the cycle \(\tau\) use exactly two copies of every
index in \(S\), so they define a partition of \(M_S\) into \(q\) pairs, with
product sum \(\sum_\ell\tau_\ell\tau_{\ell+1}\). The rearrangement pairing
bound applies to that partition. The argument is a relaxation: it allows
pairings that need not be realizable as a Hamiltonian cycle, so equality is not
asserted.

For \(S=\{1,\dots,n\}\), this gives the older full-index bound
\[
\sum_{k=1}^n \sigma_k\sigma_{k+1}
\ge
{n(n+1)(n+2)\over 6}
\]
for every cyclic order \(\sigma\) of \(\{1,\dots,n\}\).

## Geometry To Induced Subset Gaps

Consider any feasible Power-Ringmin configuration for \(n\ge 3\) with central
radius \(R\). Let \(S\subseteq\{1,\dots,n\}\) have cardinality \(q\ge 3\).
Order only the centers whose indices lie in \(S\) by their polar angles around
the central center:
\[
\tau_1,\dots,\tau_q.
\]
Coincident polar angles cannot occur in a feasible configuration, since two
distinct peripheral centers on the same ray have distance
\(|i^2-j^2|<i^2+j^2\). Therefore the induced cyclic order is well-defined.

Let
\[
\Delta_\ell\in(0,2\pi),\qquad \ell=1,\dots,q,
\]
be the positive oriented angular gaps between consecutive \(S\)-centers in
this induced cyclic order. Each \(\Delta_\ell\) may contain centers whose
indices are not in \(S\), but the induced gaps still partition the full turn:
\[
\sum_{\ell=1}^q \Delta_\ell=2\pi.
\]

For the induced adjacent pair \(i=\tau_\ell\), \(j=\tau_{\ell+1}\), all-pairs
feasibility of the original configuration includes the non-overlap condition
for this pair. Their center distance must be at least \(i^2+j^2\). By the law
of cosines, with oriented central gap \(\Delta_\ell\), this condition is
equivalent to
\[
\sin^2{\Delta_\ell\over 2}
\ge
{i^2j^2\over (R+i^2)(R+j^2)}.
\]
Since \(R>0\), the right side is in \((0,1)\). With
\[
\theta_R(i^2,j^2)
=
2\arcsin\left({ij\over \sqrt{(R+i^2)(R+j^2)}}\right)
\in(0,\pi),
\]
the sine inequality and \(\Delta_\ell\in(0,2\pi)\) imply
\[
\Delta_\ell\in[\theta_R(i^2,j^2),\,2\pi-\theta_R(i^2,j^2)],
\]
and in particular
\[
\Delta_\ell\ge \theta_R(i^2,j^2).
\]
Summing over induced adjacent gaps gives
\[
2\pi
=
\sum_{\ell=1}^q\Delta_\ell
\ge
\sum_{\ell=1}^q\theta_R(\tau_\ell^2,\tau_{\ell+1}^2).
\]

This is the key strengthening over the full-cycle argument: the same adjacent
gap inequality applies to every induced subset \(S\), not only to
\(\{1,\dots,n\}\).

## Angular Inequality

For \(1\le i,j\le n\) and \(R>0\),
\[
\theta_R(i^2,j^2)
\ge
{2ij\over R+n^2}.
\]
Indeed, \(\arcsin x\ge x\) for \(x\in[0,1]\), and
\[
\sqrt{(R+i^2)(R+j^2)}\le R+n^2.
\]
Therefore
\[
2\arcsin\left({ij\over \sqrt{(R+i^2)(R+j^2)}}\right)
\ge
{2ij\over \sqrt{(R+i^2)(R+j^2)}}
\ge
{2ij\over R+n^2}.
\]

## Lower Bound From An Arbitrary Subset

Let \(S\subseteq\{1,\dots,n\}\) have \(q\ge 3\) indices, and let
\[
A(S)=\sum_{\ell=1}^q x_\ell x_{2q+1-\ell}
\]
be the anti-sorted pairing sum for the duplicated sorted multiset
\(M_S=\{x_1,\dots,x_{2q}\}\). Combining the induced-gap inequality, the angular
inequality, and the pairing lemma gives
\[
2\pi
\ge
\sum_{\ell=1}^q\theta_R(\tau_\ell^2,\tau_{\ell+1}^2)
\ge
{2\over R+n^2}
\sum_{\ell=1}^q\tau_\ell\tau_{\ell+1}
\ge
{2A(S)\over R+n^2}.
\]
Hence every feasible central radius \(R\) satisfies
\[
R\ge {A(S)\over\pi}-n^2.
\]
Taking the infimum over feasible \(R\) gives the same bound for \(R_2^*(n)\).

The pairing bound has the following explicit form. Write
\[
S=\{s_1<s_2<\cdots<s_q\}.
\]
If \(q=2t\) is even, then
\[
A(S)=2\sum_{a=1}^t s_a s_{2t+1-a}.
\]
If \(q=2t+1\) is odd, then
\[
A(S)=2\sum_{a=1}^t s_a s_{2t+2-a}+s_{t+1}^2.
\]
Indeed, in the duplicated sorted multiset, the two copies of each of the first
\(t\) indices are paired anti-sortingly with the two copies of the
corresponding last \(t\) indices. In the odd case one additional middle copy is
paired with the other middle copy, producing \(s_{t+1}^2\).

For \(S=\{1,\dots,n\}\), \(A(S)=n(n+1)(n+2)/6\), recovering
\[
R_2^*(n)\ge {n(n+1)(n+2)\over 6\pi}-n^2
\qquad(n\ge 3),
\]
and therefore the older consequence
\[
\liminf_{n\to\infty}{6\pi R_2^*(n)\over n^3}\ge 1.
\]

## Optimal Fixed-Cardinality Subsets In This Relaxation

Fix \(q\) with \(3\le q\le n\), and let
\[
T_q=\{n-q+1,n-q+2,\dots,n\}
\]
be the tail subset of cardinality \(q\). If
\[
S=\{s_1<s_2<\cdots<s_q\}\subseteq\{1,\dots,n\},
\]
then
\[
s_a\le n-q+a
\qquad(a=1,\dots,q).
\]
The explicit even and odd formulas for \(A(S)\) show that \(A\) is
coordinatewise nondecreasing for positive coordinates: each coordinate appears
in exactly one positive product, except for the odd middle coordinate, where it
appears as a positive square. Therefore
\[
A(S)\le A(T_q).
\]
The inequality is strict unless \(S=T_q\), because if \(S\ne T_q\) at least one
coordinate is strictly smaller than the corresponding tail coordinate and all
partner coordinates are positive.

Thus, among all subsets of a fixed cardinality \(q\), the method's best lower
bound is obtained uniquely by the consecutive tail. Writing
\[
m=n-q+1,
\]
this best fixed-cardinality pairing value is
\[
A(T_q)=A(\{m,m+1,\dots,n\})=P_{m,n}.
\]
Consequently, no nonconsecutive subset of \(\{1,\dots,n\}\) can improve on the
corresponding tail bound within the specific relaxation used here.

## Consecutive Large-Index Subsets

Now specialize to
\[
S=\{m,m+1,\dots,n\},
\qquad
1\le m\le n-2.
\]
The anti-sorted pairing of
\[
\{m,m,m+1,m+1,\dots,n,n\}
\]
pairs \(k\) with \(m+n-k\), counting both copies through the sum over
\(k=m,\dots,n\). Thus
\[
P_{m,n}
=
A(\{m,\dots,n\})
=
\sum_{k=m}^n k(m+n-k).
\]

Let \(q=n-m+1\). Since
\[
\sum_{k=m}^n k = {q(m+n)\over 2},
\]
and
\[
\sum_{k=m}^n k^2
=
{n(n+1)(2n+1)-(m-1)m(2m-1)\over 6},
\]
we get
\[
\begin{aligned}
P_{m,n}
&=
(m+n)\sum_{k=m}^n k-\sum_{k=m}^n k^2\\
&=
{(n-m+1)(m^2+4mn+m+n^2-n)\over 6}.
\end{aligned}
\]
Therefore, for \(n\ge 4\) and \(1\le m\le n-2\),
\[
R_2^*(n)\ge {P_{m,n}\over \pi}-n^2.
\]

## Exact Discrete Optimization Over Tails

For fixed \(n\), the best lower bound obtainable from this relaxation is
\[
{1\over\pi}\max_{1\le m\le n-2}P_{m,n}-n^2,
\]
with the trivial singleton domain \(m=1\) when \(n=3\). For \(n\ge 4\), the
discrete maximizers can be characterized exactly.

From the closed form, or directly by subtracting the tail sums,
\[
P_{m+1,n}-P_{m,n}
=
{n^2+n-m^2-(2n+1)m\over 2}.
\]
Denote this difference by \(D_{m,n}\). It is strictly decreasing in \(m\), since
\[
D_{m+1,n}-D_{m,n}=-(m+n+1)<0.
\]
Thus \(P_{m,n}\) is a discrete concave, unimodal sequence in \(m\).

The positive real root of \(D_{m,n}=0\) is
\[
\rho_n={\sqrt{8n^2+8n+1}-(2n+1)\over 2}.
\]
For \(n\ge 4\), one has \(1<\rho_n<n-2\), so the root lies inside the
admissible interval. The two inequalities follow by squaring the equivalent
positive comparisons
\[
\sqrt{8n^2+8n+1}>2n+3
\]
and
\[
\sqrt{8n^2+8n+1}<4n-3.
\]
They reduce respectively to \(4(n-2)(n+1)>0\) and
\(8(n^2-4n+1)>0\), both valid for \(n\ge 4\). Since \(D_{m,n}\ge 0\) exactly
when \(m\le\rho_n\), the maximizers are:

- if \(\rho_n\notin\mathbb Z\), the unique maximizer is
  \[
  m=\lfloor\rho_n\rfloor+1=\lceil\rho_n\rceil;
  \]
- if \(\rho_n\in\mathbb Z\), then \(D_{\rho_n,n}=0\), so
  \[
  P_{\rho_n,n}=P_{\rho_n+1,n},
  \]
  and the two maximizers are \(m=\rho_n\) and \(m=\rho_n+1\).

The tie cases are exactly those for which \(8n^2+8n+1\) is a square,
equivalently the Pell-type condition
\[
y^2-8r^2=1,\qquad r=\rho_n,\qquad n={2r-1+y\over 2}.
\]
No tie occurs otherwise.

## Asymptotic Optimization

Let
\[
m=\alpha n+O(1),
\qquad 0\le \alpha<1.
\]
Using the closed form for \(P_{m,n}\),
\[
P_{m,n}
=
{(1-\alpha)(\alpha^2+4\alpha+1)\over 6}\,n^3
+O(n^2).
\]
Define
\[
\phi(\alpha)
=
{(1-\alpha)(\alpha^2+4\alpha+1)\over 6}.
\]
Then
\[
\phi'(\alpha)
=
{1-2\alpha-\alpha^2\over 2},
\qquad
\phi''(\alpha)=-(1+\alpha)<0.
\]
The unique maximum on \([0,1]\) is therefore
\[
\alpha_0=\sqrt2-1.
\]
At this value,
\[
\alpha_0^2+4\alpha_0+1=2\sqrt2,
\qquad
1-\alpha_0=2-\sqrt2,
\]
so
\[
\phi(\alpha_0)
=
{2(\sqrt2-1)\over 3}.
\]

The rounding is harmless and explicit. Choose
\[
m_n=\lceil(\sqrt2-1)n\rceil
=(\sqrt2-1)n+\varepsilon_n,
\qquad 0\le\varepsilon_n<1.
\]
For \(n\ge 4\), this gives \(1\le m_n\le n-2\). Substituting
\(m_n=(\sqrt2-1)n+\varepsilon_n\) into the exact formula gives
\[
P_{m_n,n}
=
{2(\sqrt2-1)\over 3}n^3
+(\sqrt2-1)n^2
+{ -3\sqrt2\,\varepsilon_n^2+6\varepsilon_n+\sqrt2-2\over 6}\,n
+{(1-\varepsilon_n)(\varepsilon_n^2+\varepsilon_n)\over 6}.
\]
Because \(0\le\varepsilon_n<1\), the last two terms are \(O(n)\), uniformly in
\(n\). Hence
\[
P_{m_n,n}
=
{2(\sqrt2-1)\over 3}n^3+O(n^2),
\]
and the induced-subset lower bound gives
\[
R_2^*(n)
\ge
{2(\sqrt2-1)\over 3\pi}n^3
-O(n^2).
\]
Consequently,
\[
\liminf_{n\to\infty}{6\pi R_2^*(n)\over n^3}
\ge
4(\sqrt2-1)>1.
\]

The preceding fixed-cardinality and discrete-optimization results show a
method-specific optimality statement: the coefficient
\[
{2(\sqrt2-1)\over 3\pi}
\]
is the largest leading coefficient obtainable from the relaxation consisting
only of induced subsets, duplicated-multiset pairing, and
\(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\). This is not an upper bound and does not
assert that the same coefficient is the exact asymptotic leading constant for
Power-Ringmin.

This contradicts any asymptotic formula whose normalized ratio
\(6\pi R_2^*(n)/n^3\) tends to \(1\). Therefore
\[
R_2^*(n)= {n^3\over 6\pi}(1+o(1))
\]
is a disproved claim. The stronger target
\[
R_2^*(n)= {n^3\over 6\pi}+O(n^2)
\]
is also a disproved claim, since it would also force the normalized ratio to
tend to \(1\).

## Geometric Consequence Of Two Nested Tails

The preceding single-subset optimization does not use relations between
different induced tails. The exact cyclic-ratio theorem permits the first such
refinement to be transferred back to geometry.

For \(n\ge4\), let \(\beta_{m,n}\) and
\(\beta_n^{(2)}=\max_{1\le m\le n-3}\beta_{m,n}\) be defined by
(CR28e)--(CR28g) in `research/FIXED_ORDER_CYCLE_RATIO.md`. Thus
\(\beta_{m,n}\) is the minimum, over a simple cycle \(C\) on
\(S_{m+1}\) and an edge \(\{a,b\}\) split by \(m\), of
\[
P(C)+[m(a+b)-ab]_+.
\]
That note proves both
\[
\Lambda_n\ge\beta_n^{(2)}
\]
and the exact method-specific asymptotic squeeze
\[
\beta_n^{(2)}
={2(\sqrt2-1)\over3}n^3+O(n^2).
\]
Combining the first inequality with the strict global cyclic-ratio sandwich
\[
R_2^*(n)>{\Lambda_n\over\pi}-n^2
\]
gives the geometric consequence
\[
\boxed{
R_2^*(n)>{\beta_n^{(2)}\over\pi}-n^2
\qquad(n\ge4).
}
\]

This can be a finite strengthening: for example,
\(\beta_{4,10}=323\), while the inner-tail pairing floor is
\(P_{5,10}=320\). Nevertheless, the correction from inserting one label and
the cost of enforcing a connected simple pairing signature are uniformly
subcubic. Hence this two-tail geometric refinement reproduces, but does not
exceed, the coefficient \(2(\sqrt2-1)/(3\pi)\) at first order. The negative
conclusion is specific to a single optimized pair of consecutive tails; it
does not cover simultaneous coupling of a number of tails growing with
\(n\), nonconsecutive subsets, or other information about \(\Lambda_n\).

## Global Consequence Of The Jointly Optimized One-Prefix Linear Block

The generalized linear block in `research/FIXED_ORDER_CYCLE_RATIO.md` yields
a stronger global lower bound. Its exact proof-valid region is
\[
0<\alpha<1,
\qquad
0<\beta<\alpha,
\qquad
0\le\lambda\le1.
\]
For fixed parameters, the pairing-floor and residual coefficients are
\[
p(\alpha)={(1-\alpha)(\alpha^2+4\alpha+1)\over6},
\]
\[
c_{\rm res}(\alpha,\beta,\lambda)
=(\alpha-\beta)
{\lambda\left(4(1+\alpha)\beta-(1+\alpha)^2
-2\lambda\beta^2\right)\over2(2-\lambda)}.
\]
Complete optimization, including every boundary face, gives the unique triple
\[
\alpha_*=1-{\sqrt3\over3},
\qquad
\beta_*={5\over6}-{\sqrt3\over4},
\qquad
\lambda_*={88-32\sqrt3\over73}.
\]
Put
\[
r=r_n^*=\lfloor\alpha_*n\rfloor,
\qquad
s=s_n^*=\lceil\beta_*n\rceil.
\]
For a fixed admissible starting index \(m\), define
\[
B_m(\sigma)=\max_{0\le j\le r-1}P_\sigma(S_{m+j}).
\]
Every score in this block is among the induced-subset scores defining
\(\Lambda(\sigma)\). Therefore, for each fixed \(m\),
\[
\Lambda_n
=\min_\sigma\Lambda(\sigma)
\ge\min_\sigma B_m(\sigma)
=\gamma^{(r)}_{m,n}.
\]
This inequality is proved separately for every \(m\). Taking the maximum of
these already-minimized scalar lower bounds gives
\[
\Lambda_n\ge
\max_{1\le m\le n-r-1}\gamma^{(r)}_{m,n}
=\Gamma_n^{(r)}.
\]
Thus no maximum is interchanged with a minimum. The floor/ceiling conditions
are uniformly valid for \(n\ge86\), and this threshold is sharp:
\((r_{85}^*,s_{85}^*)=(35,35)\), whereas the selected prefix is nonempty for
every \(n\ge86\). Since \(m=1\) is then admissible, CR28bg gives
\[
\boxed{
\Lambda_n
\ge\Gamma_n^{(r_n^*)}
\ge\gamma^{(r_n^*)}_{1,n}
\ge P_{r_n^*,n}+(r_n^*-s_n^*)F_n^*.
}
\]
The last term uses the duplicated-pairing floor \(P_{r_n^*,n}\), not the exact
inner-cycle minimum \(P^*_{r_n^*,n}\). The latter belongs to the separate
residual comparison CR28bi.

The strictly positive-cubic region of the generalized certificate is exactly
\[
\begin{aligned}
{1\over3}<\alpha<1,
\qquad {1+\alpha\over4}<\beta<\alpha,
\qquad 0<\lambda\le1,\\
2\lambda\beta^2<4(1+\alpha)\beta-(1+\alpha)^2.
\end{aligned}
\]
At the optimizer, the local, residual, pairing, and total coefficients are
\[
g_*={14-8\sqrt3\over9},
\qquad
c_{{\rm res},*}={26-15\sqrt3\over54},
\]
\[
p(\alpha_*)={19\sqrt3-18\over54},
\qquad
p(\alpha_*)+c_{{\rm res},*}={4+2\sqrt3\over27}.
\]
The total-coefficient optimality is template-specific. The displayed
\(c_{{\rm res},*}\) is its residual contribution at that optimizer, not the
separate maximum of \(c_{\rm res}\), and neither value is an exact residual
or geometric asymptotic coefficient. The density \(\alpha_*\) differs from the one-tail
maximizer \(\sqrt2-1\): its slightly smaller pairing contribution is more
than offset by the certified block residual.

The finite coefficient can be read without losing the floor information.
Write
\[
\eta_n=\alpha_*n-r_n^*,
\qquad 0\le\eta_n<1.
\]
Substitution in the exact formula for \(P_{r_n^*,n}\) gives
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
\]
In particular,
\[
P_{r_n^*,n}
\ge {19\sqrt3-18\over54}n^3
+\alpha_*n^2-2n-{1\over6}.
\]
The optimized floor estimate and CR28bk give, for \(n\ge90\),
\[
(r_n^*-s_n^*)F_n^*
\ge
{26-15\sqrt3\over54}n^3
-{28-16\sqrt3\over9}n^2.
\]
Adding the two bounds proves
\[
\boxed{
\Lambda_n
\ge
{4+2\sqrt3\over27}n^3
+{13\sqrt3-19\over9}n^2-2n-{1\over6}
\ge {4+2\sqrt3\over27}n^3
\qquad(n\ge90).
}
\]
Finally, the strict global cyclic-ratio sandwich gives the finite geometric
consequence
\[
\boxed{
R_2^*(n)
>
{4+2\sqrt3\over27\pi}n^3-n^2
\qquad(n\ge90).
}
\]
In particular,
\[
\liminf_{n\to\infty}{\Lambda_n\over n^3}
\ge {4+2\sqrt3\over27},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\ge {4+2\sqrt3\over27\pi}.
\]
These are exact lower bounds with a rigorously certified lower coefficient.
They do not prove that either normalized sequence converges or that the
displayed coefficient is its exact leading coefficient. The total coefficient
\((4+2\sqrt3)/27\) is optimal only inside the parameterized one-prefix
specialization of CR28ax--CR28bg. Its associated residual contribution is
\((26-15\sqrt3)/54\), which is neither separately maximized nor the exact
residual coefficient of the selected block; the total is not an exact
geometric constant.

## Global Consequence And Optimization Of Two Selected Prefixes

The two-prefix extension in `research/FIXED_ORDER_CYCLE_RATIO.md` uses
\[
\max(0,H_1,H_2)
\ge(\lambda_{\rm hi}-\lambda_{\rm lo})H_1
+\lambda_{\rm lo}H_2
\]
before drawing from the base-slack identity. This order matters: the expanded
linear form assigns weight \(\lambda_{\rm hi}\) to splits in the first
segment and \(\lambda_{\rm lo}\) to splits in the second, while each original
base edge receives its quadratic slack only at its unique split. Every
non-base current edge contains a previously inserted endpoint, so recursive
and fully nested child-edge splits remain covered by the same local recursive
floor.

For \(s=1+\alpha\), the exact optimizer of one weight is
\[
\psi_s(\beta)=
\begin{cases}
0,&\beta\le s/4,\\
4-s/\beta,&s/4<\beta<s/3,\\
1,&\beta\ge s/3.
\end{cases}
\]
It is nondecreasing in \(\beta\), so the two independent weight optima
automatically satisfy the order constraint. The reduced density envelope has
exactly the six branches `00`, `M0`, `H0`, `MM`, `HM`, and `HH`, with global
fixed-\(\alpha\) transitions at
\[
\alpha={1\over3},\qquad {77\over139},\qquad {301\over419}.
\]
The complete derivation in `research/FIXED_ORDER_CYCLE_RATIO.md` proves that
the unique global point is
\[
\left(
\alpha_*,\beta_{1,*},\beta_{2,*},
\lambda_{{\rm hi},*},\lambda_{{\rm lo},*}
\right)
=
\left(
{629-23\sqrt{143}\over829},
{2286-77\sqrt{143}\over3316},
{2010-59\sqrt{143}\over3316},
{6264-288\sqrt{143}\over5281},
{3888-192\sqrt{143}\over4273}
\right),
\]
and
\[
\boxed{
C_{2,*}={491596+6578\sqrt{143}\over2061723}.
}
\]
Therefore
\[
\boxed{
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\ge {491596+6578\sqrt{143}\over2061723\pi}.
}
\]
This is the globally optimized CR28bw coefficient, not an exact geometric
leading constant. No finite rounding theorem for these irrational two-prefix
densities is asserted here.

### Global Consequence And Optimization Of Three Selected Prefixes

For three heights \(H_1,H_2,H_3\), the exact ordered-weight step is
\[
\max(0,H_1,H_2,H_3)
\ge
(\lambda_1-\lambda_2)H_1
+(\lambda_2-\lambda_3)H_2+\lambda_3H_3.
\]
Expanding this expression before charging assigns one weight to each of the
three disjoint split segments. The proof in
research/FIXED_ORDER_CYCLE_RATIO.md then partitions the original
base-slack pool once across all three segments. Every recursive edge retains
a previously inserted endpoint, even after crossing both boundaries or when
both endpoints were inserted earlier.

The three clipped individual weight optima are automatically ordered, so the
exact reduced coefficient is
\[
\overline C_3
=p(\alpha)+(\alpha-\beta_1)\Phi_s(\beta_1)
+(\beta_1-\beta_2)\Phi_s(\beta_2)
+(\beta_2-\beta_3)\Phi_s(\beta_3).
\]
For \(A=3\alpha-1\) and \(X_i=4\beta_i-(1+\alpha)\), the exact compact
simplex factorization has its unique equality point at
\[
\left({X_1\over A},{X_2\over A},{X_3\over A}\right)
=
\left({1058\over1263},{276\over421},{184\over421}\right).
\]
The resulting one-variable envelope is
\[
E_3(\alpha)
=p(\alpha)+{279841\over9571014}(3\alpha-1)^3,
\]
and its unique global maximum occurs at
\[
\alpha_*={685623-421\sqrt{377823}\over993423}.
\]
Every density and weight is strictly ordered and lies in the middle clipped
branch at this point. Therefore the compact upper bound is attained and
\[
\boxed{
C_{3,*}
={753972193324+106042322\sqrt{377823}\over2960667770787}
>C_{2,*}.
}
\]
Consequently
\[
\boxed{
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\ge
{753972193324+106042322\sqrt{377823}
 \over2960667770787\pi}.
}
\]
This is the three-prefix template optimum. It is not an exact block residual,
a convergence theorem, or an exact geometric leading constant.

The optimizer also has an exact finite specialization. Put
\[
a=\alpha_*,
\qquad A=3a-1,
\qquad
(x_1,x_2,x_3)
=\left({1058\over1263},{276\over421},{184\over421}\right),
\]
\[
b_i={1+a+x_iA\over4},
\qquad
r_n=\lfloor an\rfloor,
\qquad
s_{i,n}=\lceil b_i n\rceil,
\qquad
S_n=n+r_n.
\]
For every \(n\ge159\), the cutoffs obey
\[
1\le s_{3,n}<s_{2,n}<s_{1,n}\le r_n-1,
\qquad
{S_n\over4}<s_{i,n}<{S_n\over3}.
\]
The finite clipped weights
\(\widehat\lambda_{i,n}=4-S_n/s_{i,n}\) are therefore strictly ordered and
give
\[
\widehat F_{i,n}={(4s_{i,n}-S_n)^2\over2}.
\]
Define
\[
\begin{aligned}
\mathcal B_{3,n}={}&P_{r_n,n}
 +(r_n-s_{1,n})\widehat F_{1,n}\\
&+(s_{1,n}-s_{2,n})\widehat F_{2,n}
 +(s_{2,n}-s_{3,n})\widehat F_{3,n}.
\end{aligned}
\]
and put
\[
\mathcal I_{3,n}=\lceil\mathcal B_{3,n}\rceil.
\]
Then the exact one-use charging theorem gives
\[
\Lambda_n\ge\mathcal I_{3,n}\ge\mathcal B_{3,n}
\qquad(n\ge159).
\]
The threshold is minimal uniformly: at \(n=158\),
\((r_n,s_{1,n},s_{2,n},s_{3,n})=(67,67,64,62)\), so the first segment is
empty; exact evaluation covers \(159\le n\le170\), and the symbolic tail
starts at \(171\).

The rounding remainder is controlled explicitly. With
\[
\kappa_*
={-535396585939+1466777893\sqrt{377823}\over986889256929},
\qquad
\ell_*={a+5\over3},
\]
one has
\[
\mathcal B_{3,n}
>C_{3,*}n^3+\kappa_*n^2-\ell_*n-{1\over15}.
\]
Exact comparison gives \(\kappa_*>1/3\) and \(\ell_*<11/6\), so the
remainder is positive already for \(n\ge6\). Hence, throughout the finite
theorem's domain,
\[
\boxed{
\Lambda_n\ge\mathcal I_{3,n}\ge\mathcal B_{3,n}>C_{3,*}n^3,
\qquad
R_2^*(n)>{\mathcal I_{3,n}\over\pi}-n^2
>{C_{3,*}\over\pi}n^3-n^2
\quad(n\ge159).
}
\]
The integer closure \(\mathcal I_{3,n}\) is the strongest explicit cutoff-only
consequence of this rounded bound; \(\mathcal B_{3,n}\) is the underlying
literal charging expression. No charging statement beyond three selected
prefixes is used.

For
\[
r_n=\left\lfloor{3n\over7}\right\rfloor,
\qquad
s_{1,n}=\left\lceil{2n\over5}\right\rceil,
\qquad
s_{2,n}=\left\lceil{3n\over8}\right\rceil,
\]
define \(S_n=n+r_n\) and
\[
F_{1,n}={4S_ns_{1,n}-S_n^2-s_{1,n}^2\over6},
\qquad
F_{2,n}={8S_ns_{2,n}-2S_n^2-s_{2,n}^2\over28}.
\]
The two segment lengths satisfy
\[
r_n-s_{1,n}\ge{n-58\over35},
\qquad
s_{1,n}-s_{2,n}\ge{n-35\over40}.
\]
Thus both are positive integers for every \(n\ge59\), while \(n=58\)
has \((r_n,s_{1,n},s_{2,n})=(24,24,22)\). Hence 59 is the minimal uniform
two-nonempty-prefix threshold. The pointwise block comparison gives
\[
\Lambda_n
\ge\Gamma_n^{(r_n)}
\ge\gamma^{(r_n)}_{1,n}
\ge P_{r_n,n}
+(r_n-s_{1,n})F_{1,n}
+(s_{1,n}-s_{2,n})F_{2,n}.
\]

The exact limiting ingredients are
\[
p(3/7)={284\over1029},
\qquad
g(3/7,2/5,1/2)={52\over3675},
\qquad
g(3/7,3/8,1/4)={199\over87808},
\]
so the total coefficient is
\[
C_2={72825421\over263424000}>{4+2\sqrt3\over27}.
\]
Exact rounding strengthens the literal floor theorem to
\[
\Lambda_n
\ge C_2n^3
+{106196857\over263424000}n^2
-{1520\over1029}n-{22\over343}
\ge C_2n^3
\qquad(n\ge59).
\]
The strict cyclic-ratio sandwich therefore gives
\[
\boxed{
R_2^*(n)>{72825421\over263424000\pi}n^3-n^2
\qquad(n\ge59).
}
\]
This remains the earlier exact rational two-prefix specialization. Its
coefficient is below both \(C_{2,*}\) and \(C_{3,*}\); the finite
three-prefix theorem above is stronger from \(n=159\). No exact residual,
convergence, exact leading coefficient, or matching upper bound follows.

### Four selected prefixes and global optimization

The direct theorem (CR28de)--(CR28dk) of
research/FIXED_ORDER_CYCLE_RATIO.md closes the next charging case without
using the normalized-simplex recurrence. Put

\[
r=\lfloor\alpha n\rfloor,\qquad
s_i=\lceil\beta_i n\rceil,\qquad
s_0=r,
\]

under

\[
0<\beta_4<\beta_3<\beta_2<\beta_1<\alpha<1,
\qquad
0\le\lambda_4\le\lambda_3\le\lambda_2\le\lambda_1\le1.
\]

Whenever

\[
2\le r\le n-2,\qquad
1\le s_4<s_3<s_2<s_1\le r-1,
\]

define \(F_{i,n}=G_{n,\lambda_i}(s_i)\). Combining the four heights first,
partitioning the original-edge slack once, and retaining every recursive
child edge gives

\[
\boxed{
\begin{aligned}
\Lambda_n\ge\Gamma_n^{(r)}
\ge\gamma^{(r)}_{1,n}\ge{}& P_{r,n}
+(r-s_1)F_{1,n}
+(s_1-s_2)F_{2,n}\\
&+(s_2-s_3)F_{3,n}
+(s_3-s_4)F_{4,n}.
\end{aligned}
}
\]

For fixed admissible real parameters the integer conditions hold eventually,
and division by \(n^3\) yields

\[
\begin{aligned}
C_4={}&p(\alpha)
+(\alpha-\beta_1)g(\alpha,\beta_1,\lambda_1)\\
&+(\beta_1-\beta_2)g(\alpha,\beta_2,\lambda_2)\\
&+(\beta_2-\beta_3)g(\alpha,\beta_3,\lambda_3)\\
&+(\beta_3-\beta_4)g(\alpha,\beta_4,\lambda_4),
\end{aligned}
\]

\[
\boxed{
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_4,
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_4\over\pi}.
}
\]

The continuous parameter problem is optimized on

\[
0\le\beta_4\le\beta_3\le\beta_2\le\beta_1\le\alpha\le1,
\qquad
0\le\lambda_4\le\lambda_3\le\lambda_2\le\lambda_1\le1.
\]

For \(s=1+\alpha\), the four ordered weights reduce exactly to the clipped
individual optima at the thresholds \(s/4,s/3\). The fifteen regimes are

\[
0000;\ M000,H000;\ MM00,HM00,HH00;\
MMM0,HMM0,HHM0,HHH0;\ MMMM,HMMM,HHMM,HHHM,HHHH.
\]

The fixed-\(\alpha\) winner moves through
\(0000,MMMM,HMMM,HHMM,HHHM\); the `HHHH` transition lies beyond
\(\alpha=1\). Density collisions and the two outer weight facets reduce
exactly to the three-prefix problem, while internal weight diagonals admit a
strict separating improvement unless they are already clipped or unused.

The normalized four-prefix simplex has unique point

\[
(x_1,x_2,x_3,x_4)
={1\over3666143}(3190338,2672508,2091528,1394352)
\]

and value
\(M_4=3392752184748/13440604496449\). Its one-variable envelope has the
unique maximizing density

\[
\alpha_*={18170840871749-3666143\sqrt{2903456040383}
 \over27631313622349}.
\]

Putting \(A_*=3\alpha_*-1\), the unique original parameters are

\[
\beta_{i,*}={1+\alpha_*+x_iA_*\over4},
\qquad
\lambda_{i,*}={x_iA_*\over\beta_{i,*}},
\]

and the exact global coefficient is

\[
\boxed{
C_{4,*}
={597580022071777213687318156
 +21288970076515705538\sqrt{2903456040383}
 \over2290468477489828247376833403}
>C_{3,*}.
}
\]

Thus

\[
\boxed{
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{4,*},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{4,*}\over\pi}.
}
\]

The exact separator \(C_{3,*}<2767/10000<C_{4,*}\) corroborates the strict
improvement. No finite rounding, \(k\to\infty\) passage, or claim for five
selected prefixes is used. The standalone exact oracle at
ops/TASK-20260716__four_prefix_charging/literal_oracle.py checks all 840
literal four-split histories of one bounded base, including 120 fourth splits
with two previously inserted endpoints. That computation corroborates the
bookkeeping but is not the all-history proof. Separately,
ops/TASK-20260717__global_four_prefix_optimization/exact_diagnostic.py uses
only standard-library exact arithmetic to check clipping-gap factorizations,
joins, branches, transition weights, collision reductions, the simplex
identity, end-to-end surd objective, irreducible polynomial, and comparison;
it corroborates but does not replace the all-real optimization proof.

### Arbitrarily many finite selected prefixes

The direct charging theorem in
research/FIXED_ORDER_CYCLE_RATIO.md is not limited to the optimized
four-prefix case. Fix any finite \(k\ge1\), set
\[
s_0=r,
\qquad
\lambda_{k+1}=0,
\qquad
I_i=\{s_i,\ldots,s_{i-1}-1\}.
\]
The coefficients
\[
1-\lambda_1,\quad
\lambda_1-\lambda_2,\quad\ldots,\quad
\lambda_{k-1}-\lambda_k,\quad\lambda_k
\]
form a convex combination of \(0,H_1,\ldots,H_k\). Before any original-edge
slack is assigned, they telescope exactly to
\[
\sum_{i=1}^k\lambda_i\sum_{t\in I_i}A_t.
\]
Each selected split of an untouched original edge is injectively paired with
that edge's quadratic slack; every other original slack appears once in the
unused sum. Immediately before inserting \(t\), every recursive edge has an
endpoint in \(\{t+1,\ldots,r-1\}\). Descending induction on \(t\) preserves
this property, and the induction does not mention \(k\) or a segment
boundary. Thus it covers arbitrary nesting through every finite number of
frontiers.

For
\[
2\le r\le n-2,
\qquad
1\le s_k<\cdots<s_1\le r-1,
\]
the local base and recursive floors therefore give
\[
\boxed{
\Lambda_n\ge\Gamma_n^{(r)}
\ge\gamma^{(r)}_{1,n}
\ge
P_{r,n}+\sum_{i=1}^k(s_{i-1}-s_i)G_{n,\lambda_i}(s_i).
}
\]
This includes \(k=1\), with no frontier, and the earlier \(k=5\) theorem. No
sign assumption on an individual \(G_{n,\lambda_i}(s_i)\) is needed.

The sole new bounded corroboration is dossier-local and limited to \(k=6\).
At
\[
(n,r,C_0)=(20,15,(15,20,16,19,17,18)),
\]
with consecutive cutoffs \(14,\ldots,9\) and weights
\((6/7,\ldots,1/7)\), exact standard-library arithmetic checks all
332,640 literal histories, including 720 histories charging all six original
edges and 60,480 sixth splits between inserted endpoints. This is not
production enumeration and does not replace the arbitrary-\(k\) proof.

The displayed finite inequality may be instantiated on each individual
admissible row. It provides no cutoff threshold, rounding estimate, error
bound, or parameter control uniform in a growing family \(k=k(n)\).
Consequently it yields no interchange of \(n\to\infty\) with
\(k\to\infty\) and no infinite-prefix theorem. This does not preclude taking
the supremum of separate scalar consequences proved at every fixed \(k\).

### Full clipped continuous envelope at arbitrary finite \(k\)

For the complete compact continuous template, coordinatewise weight
optimization is exact because the clipped optimizer is nondecreasing in its
cutoff. With \(s=1+\alpha\), \(\beta_0=\alpha\), and the clipped floor
\(\Phi_s\) from (CR28bw3), the value is therefore

\[
\mathscr H_k(\alpha)
=p(\alpha)+
\max_{0\le\beta_k\le\cdots\le\beta_1\le\alpha}
\sum_{i=1}^k(\beta_{i-1}-\beta_i)\Phi_s(\beta_i).
\]

Equivalently, with \(t=\alpha/(1+\alpha)\) and the increasing clipped
function \(\phi\) in (CR28dw15),

\[
\mathscr H_k(\alpha)=p(\alpha)+(1+\alpha)^3V_k(t),
\qquad
V_m(t)=\max_{0\le x\le t}
\bigl((t-x)\phi(x)+V_{m-1}(x)\bigr),
\quad V_0=0.
\]

This compact Bellman envelope contains exactly
\((k+1)(k+2)/2\) ordered clipping regimes \(H^hM^m0^z\). Its finite
chains are lower Darboux sums for \(\phi\), and they converge monotonically
and uniformly to its integral. The resulting pointwise finite-prefix
supremum is

\[
\mathscr H_{\rm fin}(\alpha)=
\begin{cases}
p(\alpha),&0\le\alpha\le1/3,\\[1mm]
(23\alpha^3-39\alpha^2+21\alpha+3)/24,
 &1/3\le\alpha\le1/2,\\[1mm]
(5\alpha^3-21\alpha^2+15\alpha+17)/72,
 &1/2\le\alpha\le1.
\end{cases}
\]

The two outer intervals are strictly below the feasible one-prefix
all-middle optimum. Hence, for every finite \(k\), the unique global compact
maximizer lies in \(1/3<\alpha<1/2\), where no high coordinate is feasible
and the exact envelope is

\[
E_k(\alpha)=p(\alpha)+{M_k\over8}(3\alpha-1)^3.
\]

It follows that the unique full optimizer is strict all-middle, with
\(\alpha_{k,*}\) and the original cutoff/weight tuple given in
(CR28dw24)--(CR28dw25), and

\[
C_{k,*}\nearrow
{434+4\sqrt2\over1587}=C_{\mathrm{AF}}.
\]

Thus \(C_{\mathrm{AF}}\) is the exact supremum of the whole continuous
finite-prefix family and is not attained at finite \(k\). This is a
continuous template classification; it introduces no finite rounding,
uniform threshold, or growing-prefix charging assertion.

### All-fixed-\(k\) corollary

Fix

\[
\alpha_\infty={13-2\sqrt2\over23},
\qquad
A_\infty=3\alpha_\infty-1,
\qquad
S_\infty=1+\alpha_\infty.
\]

For each finite \(k\), let
\(1=x_0^{(k)}>x_1^{(k)}>\cdots>x_k^{(k)}>0\) be the unique normalized
simplex optimizer and define

\[
\beta_i={S_\infty+A_\infty x_i^{(k)}\over4},
\qquad
\lambda_i={A_\infty x_i^{(k)}\over\beta_i}.
\]

Since \(1/3<\alpha_\infty<1/2\), one has

\[
\beta_i-{S_\infty\over4}={A_\infty x_i^{(k)}\over4}>0,
\qquad
\alpha_\infty-\beta_i
={A_\infty(1-x_i^{(k)})\over4}>0,
\]

and

\[
{S_\infty\over3}-\beta_i
={S_\infty-3A_\infty x_i^{(k)}\over12}
>{1-2\alpha_\infty\over3}>0.
\]

Thus the cutoffs are strictly ordered and all-middle. The map
\(x\mapsto4A_\infty x/(S_\infty+A_\infty x)\) is strictly increasing,
and the last displayed margin also gives \(\lambda_i<1\). Hence

\[
0<\beta_k<\cdots<\beta_1<\alpha_\infty<1,
\qquad
0<\lambda_k<\cdots<\lambda_1<1.
\]

For each fixed \(k\), these strict margins give some tuple-dependent
threshold \(N_k\). Applying the finite theorem for \(n\ge N_k\), dividing by
\(n^3\), and taking the fixed-parameter liminf gives

\[
L_\Lambda:=\liminf_{n\to\infty}{\Lambda_n\over n^3}
\ge p(\alpha_\infty)+{A_\infty^3M_k\over8}.
\]

Indeed, on the middle branch,
\(g(\alpha_\infty,\beta_i,\lambda_i)
=A_\infty^2(x_i^{(k)})^2/2\), while
\(\beta_{i-1}-\beta_i
=A_\infty(x_{i-1}^{(k)}-x_i^{(k)})/4\).
The inequality holds for every fixed finite \(k\), so \(M_k\nearrow1/3\)
implies

\[
\boxed{
L_\Lambda
\ge\sup_{k\ge1}
\left[p(\alpha_\infty)+{A_\infty^3M_k\over8}\right]
={434+4\sqrt2\over1587}.
}
\]

Here
\(p(\alpha_\infty)=(9038+722\sqrt2)/36501\) and
\(A_\infty^3/24=(944-630\sqrt2)/36501\), which sum to the displayed
coefficient. The normalized cyclic-ratio sandwich then gives

\[
\boxed{
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\ge{434+4\sqrt2\over1587\pi}.
}
\]

The quantifiers are \(\forall k\,\exists N_k\). There is no choice
\(k=k(n)\), no common threshold, and no interchange of limits: the
\(k\)-supremum is taken only after every fixed-\(k\) liminf inequality has
been established. Since no finite \(k\) attains \(M_k=1/3\), this is not a
new uniformly rounded finite-\(n\) theorem.

### Globally optimized five-prefix coefficient

At fixed \(k=5\), the preceding one-use theorem gives the continuous
coefficient

\[
C_5=p(\alpha)+\sum_{i=1}^5
(\beta_{i-1}-\beta_i)g(\alpha,\beta_i,\lambda_i),
\qquad \beta_0=\alpha.
\]

On the full ordered compact closure, the weights clip independently to
\(0\), \(4-(1+\alpha)/\beta_i\), or \(1\). Their optima are already ordered,
so the exact density reduction has 21 regimes \(H^hM^m0^z\),
\(h+m+z=5\). The Bellman audit in
research/FIXED_ORDER_CYCLE_RATIO.md classifies all 15 trailing-zero
nonwinners, the active sequence

\[
MMMMM,\quad HMMMM,\quad HHMMM,\quad HHHMM,\quad HHHHM,
\]

and the formal HHHHH transition beyond \(\alpha=1\). The same proof audits
all clipping joins, density collisions, ordered-weight diagonals, unused
segments, and compact faces.

For \(A=3\alpha-1\), the normalized-simplex certificate gives the sharp
envelope

\[
E_5(\alpha)
=p(\alpha)+{M_5\over8}(3\alpha-1)^3.
\]

Its unique global maximizer is

\[
\boxed{
\alpha_{5,*}
={422413777961580309772684503
 -10047852311701\sqrt{183342238504950468196395903}
 \over661485317418210151348973103}.
}
\]

It lies strictly between \(1/3\) and \(1/2\), before the first high-clipping
transition. With the \(D,N_i\) above and \(A_*=3\alpha_{5,*}-1\), the five
unique exact pairs are

\[
\boxed{
\beta_{i,*}
={(D-N_i)+(D+3N_i)\alpha_{5,*}\over4D},
\qquad
\lambda_{i,*}
={4N_iA_*\over(D-N_i)+(D+3N_i)\alpha_{5,*}}
\quad(1\le i\le5).
}
\]

All five cutoffs and weights are strictly ordered and middle-clipped. The
exact optimum is

\[
\boxed{
C_{5,*}
={346693217780244687187063490332457027500975566238012204
 +1228130489996268437333105902690103574002
  \sqrt{183342238504950468196395903}
 \over1312688475479610714750859896048564873968757997852345827}.
}
\]

The optimizer and coefficient have the primitive quadratic polynomials and
rational isolating intervals recorded in (CR28dz35)--(CR28dz40). Exact
integer and squared-radical margins give

\[
\boxed{C_{5,*}>C_{5,\mathrm{rat}}>C_{4,*}.}
\]

Consequently

\[
\boxed{
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{5,*},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{5,*}\over\pi}.
}
\]

The standalone standard-library diagnostic checks all 21 clipped words, the
five transition rows, collision identities, optimizer and coefficient
polynomials, isolating intervals, strict branch inequalities, coefficient
identity, and comparison margins. This is a fixed-\(k=5\) asymptotic
optimization, not finite rounding at the irrational point, a growing-\(k\)
passage, an exact residual, convergence, or a geometric leading constant.
It remains the exact optimum of the five-prefix template. The all-fixed-\(k\)
corollary is strictly stronger, since
\[
C_{5,*}<{277\over1000}<{434+4\sqrt2\over1587}.
\]

### Explicit fixed five-prefix witness: asymptotic and finite forms

For one fixed specialization, the finite theorem may be combined with the
exact normalized simplex without any growing-\(k\) passage. The fifth row is

\[
M_5={722599396919860307414438404
 \over2725902074099388500860861827},
\]

and, with \(D=30143556935103\),

\[
(x_1,\ldots,x_5)
={1\over D}(26881208992898,23392470652668,19595592993288,
15335681473008,10223787648672).
\]

Choose

\[
\alpha={13\over30},
\qquad
s={43\over30},
\qquad
A={3\over10}.
\]

The exact all-middle parameters are

\[
\beta_i={s+Ax_i\over4},
\qquad
\lambda_i={Ax_i\over\beta_i}=4-{s\over\beta_i}.
\]

Because \(1>x_1>\cdots>x_5>0\), these satisfy

\[
0<\beta_5<\cdots<\beta_1<\alpha<1,
\qquad
{s\over4}<\beta_i<{s\over3},
\qquad
0<\lambda_5<\cdots<\lambda_1<1.
\]

All inequalities are strict, so the integer cutoffs are admissible for every
sufficiently large \(n\). The exact threshold and rounded bound are given
below. In the limiting middle regime,

\[
g(\alpha,\beta_i,\lambda_i)={(Ax_i)^2\over2}.
\]

Consequently the five-segment coefficient is exactly

\[
\boxed{
C_{5,\mathrm{rat}}
=p\!\left({13\over30}\right)+{(3/10)^3M_5\over8}
={2263404122555368590593580404287
 \over8177706222298165502582585481000}.
}
\]

The exact separator calculation in
research/FIXED_ORDER_CYCLE_RATIO.md proves

\[
C_{5,\mathrm{rat}}>{75\over271}>C_{4,*}.
\]

The fixed-parameter limit of the five-prefix inequality and the established
additive cyclic-ratio relation therefore give

\[
\boxed{
\liminf_{n\to\infty}{\Lambda_n\over n^3}
\ge C_{5,\mathrm{rat}},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\ge{C_{5,\mathrm{rat}}\over\pi}.
}
\]

The second inequality uses no new geometric lemma: it is only the normalized
consequence of the existing \(O(n^2)\) additive sandwich. The standalone
Fraction diagnostic in the task dossier checks every rational identity and
both comparison margins. This rational specialization is strictly below the
global coefficient above. Its derivation itself uses no global optimization,
and it remains the point with the exact finite theorem below.

For the finite form, retain the same fixed rational weights and define

\[
r_n=\left\lfloor{13n\over30}\right\rfloor,
\qquad
s_{i,n}=\lceil\beta_i n\rceil,
\qquad
s_{0,n}=r_n,
\qquad
S_n=n+r_n,
\]

\[
F_{i,n}
=G_{n,\lambda_i}(s_{i,n})
={\lambda_i(4S_ns_{i,n}-S_n^2-2\lambda_i s_{i,n}^2)
 \over2(2-\lambda_i)}.
\]

The exact boundary and symbolic-tail audit in
research/FIXED_ORDER_CYCLE_RATIO.md proves that \(n=234\) is the minimal
uniform threshold for

\[
2\le r_n\le n-2,
\qquad
1\le s_{5,n}<\cdots<s_{1,n}\le r_n-1,
\qquad
{S_n\over4}<s_{i,n}<{S_n\over3}.
\]

Indeed \(r_{233}=s_{1,233}=100\), while the rows \(234\) through \(246\)
close the finite bridge and a direct rounding inequality covers every
\(n\ge247\). The middle inequalities classify the rounded cutoffs; they do
not replace the fixed \(\lambda_i\) by the finite clipped optima
\(4-S_n/s_{i,n}\).

Define

\[
\mathcal B_{5,n}
=P_{r_n,n}+\sum_{i=1}^5(s_{i-1,n}-s_{i,n})F_{i,n},
\qquad
\mathcal I_{5,n}=\left\lceil\mathcal B_{5,n}\right\rceil.
\]

The exact floor/ceiling-error expansion cancels every ceiling error from the
quadratic coefficient by the five simplex stationarity equations. In
particular,

\[
\mathcal B_{5,n}-C_{5,\mathrm{rat}}n^3
>{13\over30}n^2-{25\over2}n-{109\over6}>0
\qquad(n\ge234).
\]

Therefore the finite theorem and its existing geometric transfer are

\[
\boxed{
\Lambda_n\ge\mathcal I_{5,n}\ge\mathcal B_{5,n}
>C_{5,\mathrm{rat}}n^3
\qquad(n\ge234),
}
\]

\[
\boxed{
R_2^*(n)>{\mathcal I_{5,n}\over\pi}-n^2
>{C_{5,\mathrm{rat}}\over\pi}n^3-n^2
\qquad(n\ge234).
}
\]

The sole finite diagnostic uses standard-library exact arithmetic for the
boundary rows, minimality, literal expression, integer closure, and exact
remainder identities. The written symbolic tail, not the bounded diagnostic,
proves the uniform theorem.

## Exact Radius-One Insertion

The following result turns the finite reduced-core observation into an exact
eventual theorem. Its proof does not use the checked cases \(n=5,6\).

### Forbidden-arc lemma

Consider a feasible configuration of the core radii \(2^2,\dots,n^2\) at
central radius \(R>0\). Let \(\phi_j\) be the polar angle of the center of the
circle of radius \(j^2\). On the angular circle
\(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), let
\(d_{\mathbb T}\in[0,\pi]\) denote circular distance and define
\[
B_j
=
\{\alpha\in\mathbb T:
d_{\mathbb T}(\alpha,\phi_j)<\theta_R(1,j^2)\}.
\]
Because \(0<\theta_R(1,j^2)<\pi\), the set \(B_j\) is an open arc of angular
measure \(2\theta_R(1,j^2)\). Hence
\[
\mu\!\left(\bigcup_{j=2}^n B_j\right)
\le
\sum_{j=2}^n\mu(B_j)
=
2\sum_{j=2}^n\theta_R(1,j^2).
\]
If the angular sum is less than \(\pi\), the union has measure less than
\(2\pi\). Choose \(\alpha\) outside that union and place the new center at
polar coordinates \((R+1,\alpha)\).

This construction checks all constraints introduced by the new circle.

1. Its center is at distance \(R+1\) from the central center, so the new circle
   is externally tangent to the central circle.
2. For every \(j=2,\dots,n\), put
   \(\delta_j=d_{\mathbb T}(\alpha,\phi_j)\). Since
   \(\alpha\notin B_j\), one has
   \(\delta_j\ge\theta_R(1,j^2)\). The squared distance to the \(j\)-th
   center is
   \[
   d_j^2
   =
   (j^2-1)^2
   +4(R+1)(R+j^2)\sin^2(\delta_j/2).
   \]
   Because \(0\le\delta_j\le\pi\), the sine is increasing on the relevant
   half-angle interval. By the definition of \(\theta_R\),
   \[
   d_j^2
   \ge
   (j^2-1)^2+4j^2
   =
   (j^2+1)^2.
   \]
   Thus every one of the \(n-1\) new peripheral pairwise constraints
   \((1,j^2)\) holds; equality is permitted because tangent peripheral
   circles have disjoint interiors.
3. Every core-core pairwise constraint is unchanged.

There are no other new constraints. This proves the insertion criterion.

### Angular majorant

For \(R>0\) and \(j\ge2\), set
\[
x={j\over\sqrt{(R+1)(R+j^2)}}
\quad\text{and}\quad
y=\arcsin x.
\]
Since \(0<y<\pi/2\), one has \(y<\tan y\). Also
\[
(R+1)(R+j^2)-j^2=R(R+j^2+1).
\]
Therefore
\[
\theta_R(1,j^2)
=2\arcsin x
< {2x\over\sqrt{1-x^2}}
= {2j\over\sqrt{R(R+j^2+1)}}
< {2j\over R}.
\tag{1}
\]
In particular, with
\[
S_n=2\sum_{j=2}^n j=n(n+1)-2,
\]
equation (1) gives
\[
\sum_{j=2}^n\theta_R(1,j^2)<{S_n\over R}.
\tag{2}
\]

We use the elementary rational bounds
\[
{31\over10}<\pi<{22\over7}.
\tag{3}
\]
For completeness, the upper bound follows from the positive integral identity
\[
{22\over7}-\pi
=
\int_0^1{x^4(1-x)^4\over1+x^2}\,dx>0.
\]
For the lower bound, the perimeter of the regular dodecagon inscribed in the
unit circle gives
\[
\pi>3(\sqrt6-\sqrt2)>{31\over10}.
\]
The last comparison is purely algebraic; after two squarings of positive
quantities its strict margin is
\(6239^2-3\cdot3600^2=45121>0\).

### Configuration-level core lower bound

The induced-subset theorem above must be reapplied to a core configuration;
the scalar lower bound for the full optimum alone would not imply a lower
bound for the smaller core optimum. If \(R\in\mathcal C_n\) and
\(2\le m\le n-2\), apply the already-proved induced-gap and pairing argument
to the tail \(\{m,m+1,\dots,n\}\), which is present in the core. It gives
\[
R\ge {P_{m,n}\over\pi}-n^2,
\qquad
P_{m,n}=\sum_{k=m}^n k(m+n-k).
\tag{4}
\]
This is a statement about every feasible core configuration, not about an
unattained infimum.

### The boundary case \(n=12\)

For \(m=6\), one has \(P_{6,12}=539\). Equations (3)--(4) give, for every
\(R\in\mathcal C_{12}\),
\[
R\ge{539\over\pi}-144>{7\cdot539\over22}-144={55\over2}.
\]
Put \(R_0=55/2\). For \(j=2,\dots,12\), equation (1) is bounded at \(R_0\)
by \(k_j/1000\), using the following exact integer checks. The first
majorant in (1) is strictly decreasing in \(R\), so an upper bound at \(R_0\)
also bounds every feasible \(R>R_0\).

| \(j\) | \(k_j\) | \(k_j^2\,55(57+2j^2)-16{,}000{,}000j^2\) |
|---:|---:|---:|
| 2 | 134 | 192700 |
| 3 | 187 | 247125 |
| 4 | 229 | 698695 |
| 5 | 261 | 892085 |
| 6 | 285 | 291375 |
| 7 | 304 | 3846400 |
| 8 | 318 | 4936700 |
| 9 | 329 | 7762845 |
| 10 | 337 | 5297815 |
| 11 | 344 | 10035520 |
| 12 | 349 | 7173975 |

Every margin is positive, which after squaring positive quantities proves
\[
{2j\over\sqrt{R_0(R_0+j^2+1)}}<{k_j\over1000}.
\]
Since \(\sum_{j=2}^{12}k_j=3077\),
\[
\sum_{j=2}^{12}\theta_R(1,j^2)
<{3077\over1000}
<{31\over10}
<\pi.
\tag{5}
\]

### The boundary case \(n=13\)

Here \(P_{6,13}=680\), so every \(R\in\mathcal C_{13}\) satisfies
\[
R\ge{680\over\pi}-169>{521\over11}>47.
\]
For
\[
f_R(x)={x\over\sqrt{R+x^2+1}},
\]
one has \(f_R'(x)>0\). Hence the right-interval integral bound gives
\[
\sum_{j=2}^{13}f_R(j)
\le
\int_2^{14}f_R(x)\,dx
=
\sqrt{R+197}-\sqrt{R+5}.
\]
Combining this with (1) and rationalizing yields
\[
\sum_{j=2}^{13}\theta_R(1,j^2)
<
{384\over
\sqrt{R(R+197)}+\sqrt{R(R+5)}}.
\]
For \(R>47\), the denominator is greater than
\[
\sqrt{47\cdot244}+\sqrt{47\cdot52}
>107+49=156,
\]
because \(107^2<47\cdot244\) and \(49^2<47\cdot52\). Consequently
\[
\sum_{j=2}^{13}\theta_R(1,j^2)
<{384\over156}
={32\over13}
<3
<\pi.
\tag{6}
\]

### Uniform estimate for \(n\ge14\)

Let \(m=\lfloor n/2\rfloor\). If \(n=2t\), then
\[
P_{m,n}={t(t+1)(13t-1)\over6};
\]
if \(n=2t+1\), then
\[
P_{m,n}={t(t+2)(13t+7)\over6}.
\]
For \(t\ge7\), both cases satisfy
\[
P_{m,n}\ge {29\over7}n^2+n-2.
\tag{7}
\]
Indeed, after multiplying the difference in (7) by \(42\) and putting
\(u=t-7\ge0\), the even and odd cases respectively become
\[
91u^3+1299u^2+4718u+672>0
\]
and
\[
91u^3+1446u^2+6185u+3522>0.
\]
Using (3), (4), and (7), every \(R\in\mathcal C_n\) satisfies
\[
R
\ge {P_{m,n}\over\pi}-n^2
={P_{m,n}-\pi n^2\over\pi}
>{S_n\over\pi}.
\]
Equation (2) therefore gives
\[
\sum_{j=2}^n\theta_R(1,j^2)<{S_n\over R}<\pi
\qquad(n\ge14).
\tag{8}
\]

### Equality of feasible-radius sets and infima

Restriction of a full configuration to its core always gives
\(\mathcal F_n\subseteq\mathcal C_n\). Conversely, equations (5), (6), and
(8), followed by the forbidden-arc lemma, show that every
\(R\in\mathcal C_n\) also belongs to \(\mathcal F_n\) when \(n\ge12\).
Thus
\[
\mathcal F_n=\mathcal C_n\qquad(n\ge12).
\]
Taking infima of equal sets proves
\[
\boxed{R_2^*(n)=R^*_{2:n}\qquad(n\ge12)}.
\]
No core minimizer, full minimizer, or limiting configuration was assumed. The
argument does not prove that \(12\) is the least possible threshold. The same
chain of lower and upper bounds does not close \(n=11\), which is a limitation
of this proof and not a counterexample to equality at \(n=11\).

## Regular-Direction Core Cubic Upper Bounds

We first record an order-independent regular-direction baseline, and then
sharpen it by assigning the core indices in zigzag order. Both constructions
check every pairwise constraint directly; checking only neighboring directions
would not be sufficient.

### Worst pair at fixed radius

Fix \(n\ge12\) and \(R>0\), and define
\[
h_R(x)={x\over\sqrt{R+x^2}}\qquad(x>0).
\]
Then
\[
h_R'(x)={R\over(R+x^2)^{3/2}}>0.
\]
For distinct core indices \(2\le i<j\le n\),
\[
\theta_R(i^2,j^2)
=2\arcsin\bigl(h_R(i)h_R(j)\bigr).
\]
Both \(h_R\) and \(\arcsin\) are strictly increasing on the relevant
domains. Therefore the unique largest required angular separation among
distinct core radii is
\[
\theta_R((n-1)^2,n^2).
\tag{9}
\]
This is an exact fixed-\(R\) monotonicity statement, not a finite numerical
observation.

### Solving for a sufficient radius

Put
\[
\gamma_n={\pi\over n-1},\qquad A=(n-1)^2,\qquad B=n^2.
\]
For \(n\ge12\), one has \(0<\gamma_n<\pi/2\). Hence
\[
\theta_R(A,B)\le {2\pi\over n-1}
\]
is equivalent to
\[
{n(n-1)\over\sqrt{(R+A)(R+B)}}\le\sin\gamma_n,
\]
or
\[
(R+A)(R+B)\ge AB\csc^2\gamma_n.
\tag{10}
\]
Completing the square in (10) gives
\[
\left(R+{A+B\over2}\right)^2
\ge
AB\csc^2\gamma_n+{(B-A)^2\over4}.
\]
The left side is strictly increasing for \(R\ge0\). Since
\(\csc^2\gamma_n>1\), the unique nonnegative threshold is positive and equals
\[
\boxed{
U_n
=
\sqrt{
n^2(n-1)^2\csc^2\!\left({\pi\over n-1}\right)
+{(2n-1)^2\over4}}
-{n^2+(n-1)^2\over2}
}.
\tag{11}
\]
At \(R=U_n\), equality holds in (10), so
\[
\theta_{U_n}((n-1)^2,n^2)={2\pi\over n-1}.
\tag{12}
\]

### All-pairs feasibility of the regular core

Use the vertex directions of a regular \((n-1)\)-gon centered at the central
center. Explicitly, in one bijective assignment put
\[
\phi_i={2\pi(i-2)\over n-1}
\qquad(i=2,\dots,n)
\]
and place the center of the radius-\(i^2\) circle at
\[
(U_n+i^2)(\cos\phi_i,\sin\phi_i).
\]
Thus all polar angles are equally spaced, while the differing radial distances
correctly enforce external tangency to the central circle. Any permutation of
the radii among these directions has the same argument below.

Let two distinct vertices be separated by the smaller circular step \(q\),
where
\[
1\le q\le\left\lfloor{n-1\over2}\right\rfloor.
\]
Their smaller central angle is
\[
\delta={2\pi q\over n-1}\in(0,\pi],
\]
and therefore
\[
\delta\ge {2\pi\over n-1}.
\tag{13}
\]
For peripheral radii \(a,b>0\), central radius \(R>0\), and smaller central
angle \(\delta\in[0,\pi]\), the squared center distance is
\[
d^2
=(a-b)^2+4(R+a)(R+b)\sin^2(\delta/2).
\]
Consequently,
\[
d^2\ge(a+b)^2
\quad\Longleftrightarrow\quad
\sin^2(\delta/2)
\ge {ab\over(R+a)(R+b)}
\quad\Longleftrightarrow\quad
\delta\ge\theta_R(a,b).
\tag{14}
\]
By (9), (12), and (13), every pair \(2\le i<j\le n\) satisfies
\[
\delta
\ge {2\pi\over n-1}
=\theta_{U_n}((n-1)^2,n^2)
\ge\theta_{U_n}(i^2,j^2).
\]
Equation (14) proves non-overlap for all \(\binom{n-1}{2}\) core pairs.
This explicitly includes non-adjacent vertex pairs \(q>1\); they have more
available angular separation than an edge pair. Equality is allowed because
external tangency gives disjoint interiors. Hence \(U_n\in\mathcal C_n\).

For \(n\ge12\), the already-proved equality
\(\mathcal C_n=\mathcal F_n\) therefore also gives
\[
R_2^*(n)\le U_n.
\]
For reference, this baseline has \(U_n/n^3\to1/\pi\). Indeed, if
\[
X_n=n(n-1)\csc\!\left({\pi\over n-1}\right),
\quad
Y_n={2n-1\over2},
\quad
Z_n={n^2+(n-1)^2\over2},
\]
then \(U_n=\sqrt{X_n^2+Y_n^2}-Z_n\), while
\[
{X_n\over n^3}
=
{(n-1)^2\over n^2}
{1\over(n-1)\sin(\pi/(n-1))}
\longrightarrow{1\over\pi},
\]
and \(Y_n/n^3,Z_n/n^3\to0\). The next construction improves this
coefficient by exploiting the order of the indices.

### General angular upper bound

The zigzag refinement starts from an upper bound valid for every \(R>0\) and
all positive indices \(i,j\):
\[
\boxed{
\theta_R(i^2,j^2)<{2ij\over R}
}.
\tag{15}
\]
Indeed, put
\[
x={ij\over\sqrt{(R+i^2)(R+j^2)}},
\qquad
y=\arcsin x.
\]
Here \(0<x<1\) and \(0<y<\pi/2\). The strict inequality \(y<\tan y\) gives
\[
\begin{aligned}
\theta_R(i^2,j^2)
&=2y
< {2x\over\sqrt{1-x^2}}\\
&={2ij\over\sqrt{(R+i^2)(R+j^2)-i^2j^2}}
={2ij\over\sqrt{R(R+i^2+j^2)}}
<{2ij\over R}.
\end{aligned}
\]
The hypothesis \(R>0\) is essential to this formula and to both strict
inequalities.

### Zigzag product lemma

For \(n\ge3\), let
\[
N=n-1,
\qquad
h=\left\lfloor{n\over2}\right\rfloor,
\qquad
M_n=n(h+1),
\tag{16}
\]
and place the core indices \(2,\dots,n\) in the cyclic zigzag order
\[
z_n=(z_0,\dots,z_{N-1})=(n,2,n-1,3,\dots).
\]
This is exactly the order returned by `patterns.zigzag(range(2, n + 1))`.

Lemma. If distinct indices \(i,j\) have smaller circular positional distance
\[
q\in\left\{1,\dots,\left\lfloor{N\over2}\right\rfloor\right\}
\]
in \(z_n\), then
\[
ij\le qM_n.
\tag{17}
\]

Proof. The first entry of \(z_n\) is \(n\), and its last entry is always
\(h+1\). Thus the closing arc has product
\[
z_{N-1}z_0=n(h+1)=M_n.
\]
This is the maximum adjacent product. To check all other adjacent arcs
explicitly, separate the two parities.

If \(n=2h\), then
\[
z_{2t}=2h-t\quad(0\le t\le h-1),
\qquad
z_{2t+1}=t+2\quad(0\le t\le h-2).
\]
Every non-closing adjacent arc therefore contains a low entry at most \(h\)
and an entry at most \(n\), so its product is at most
\(nh<M_n\).

If \(n=2h+1\ge5\), then
\[
z_{2t}=2h+1-t,
\qquad
z_{2t+1}=t+2
\quad(0\le t\le h-1).
\]
Every non-closing adjacent arc joins a low entry at most \(h+1\) to a high
entry at most \(n\), so its product is at most \(M_n\). Equality would require
the pair \(\{h+1,n\}\), but these are the last and first entries and hence form
the closing arc, not a non-closing one. Thus all other adjacent products are
strictly smaller. For \(n=3\), the two directions determine the same unordered
pair on both sides of the two-vertex cycle; its product is still \(M_3\).

This proves (17) when \(q=1\), including the closing arc. For every \(q\ge2\),
distinctness of the indices gives the exact elementary chain
\[
ij\le n(n-1)<2n(h+1)=2M_n\le qM_n.
\]
This covers every remaining pair and proves the lemma.

### All-pairs feasibility of the zigzag core

Define
\[
\boxed{
V_n={(n-1)M_n\over\pi}
=
{n(n-1)(\lfloor n/2\rfloor+1)\over\pi}
}.
\tag{18}
\]
Assign \(z_k\) to polar direction \(2\pi k/N\), and place its center at
radial distance \(V_n+z_k^2\). These are the directions of a regular
\((n-1)\)-gon; the centers themselves have different radial distances because
the peripheral radii differ.

Take any two distinct core indices \(i,j\), and let \(q\) be their smaller
circular positional distance in the zigzag order. Their smaller central angle
is
\[
\delta_q={2\pi q\over n-1}\in(0,\pi].
\]
By (15), the product lemma, and (18),
\[
\theta_{V_n}(i^2,j^2)
<{2ij\over V_n}
\le {2qM_n\over V_n}
={2\pi q\over n-1}
=\delta_q.
\tag{19}
\]
The pairwise distance equivalence (14) therefore gives strict non-overlap for
this pair. Since the choice was arbitrary, all \(\binom{n-1}{2}\) core pairs
are feasible at once. This argument includes the maximal adjacent product, the
closing arc, and every non-adjacent pair \(q\ge2\). Hence
\[
V_n\in\mathcal C_n.
\]

### Insertion and improved asymptotic consequences

For \(n\ge12\), the exact radius-one theorem above proves
\(\mathcal C_n=\mathcal F_n\). Since the zigzag core is actually feasible at
\(V_n\), it follows directly that \(V_n\in\mathcal F_n\), and thus
\[
\boxed{R_2^*(n)\le V_n\qquad(n\ge12)}.
\tag{20}
\]
This implication uses equality of feasible-radius sets and does not assume
that either infimum is attained.

From the exact formula (18),
\[
{V_n\over n^3}
=
{n-1\over n}
{\lfloor n/2\rfloor+1\over n}
{1\over\pi}
\longrightarrow {1\over2\pi}.
\]
Therefore
\[
\limsup_{n\to\infty}{R_2^*(n)\over n^3}\le {1\over2\pi}.
\tag{21}
\]
Combining (21) with the all-fixed-\(k\) lower bound proved in this note yields
\[
{434+4\sqrt2\over1587\pi}
\le
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\le
\limsup_{n\to\infty}{R_2^*(n)\over n^3}
\le {1\over2\pi}.
\tag{22}
\]
In particular,
\[
\boxed{R_2^*(n)=\Theta(n^3)}.
\]
The later exact shortcut evaluation of the canonical eight-twenty-fifths
core order sharpens the right endpoint to

\[
{434+4\sqrt2\over1587\pi}
\le
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\le
\limsup_{n\to\infty}{R_2^*(n)\over n^3}
\le {143\over500\pi}.
\tag{23}
\]

The coefficient gap in (23) remains open. The value \(1/(2\pi)\) is the
limsup coefficient of the zigzag construction, and \(8/(25\pi)\) is the
older regular-direction product-distance coefficient; neither is the current
best bound. Neither the improved upper bound nor the lower bound proves that
\(R_2^*(n)/n^3\) has a limit, and no exact leading constant is claimed.

## Gap And Counterexample Audit

- The induced gaps are valid even when skipped non-\(S\) centers lie inside
  them: they are positive oriented arcs between consecutive \(S\)-centers and
  still sum to \(2\pi\).
- The induced adjacent endpoints need not be adjacent in the full order. This
  is not a gap, because all-pairs feasibility applies directly to every pair of
  endpoints in the original configuration.
- The sine condition gives both
  \(\Delta_\ell\ge\theta_R(i^2,j^2)\) and
  \(\Delta_\ell\le2\pi-\theta_R(i^2,j^2)\). The lower-bound proof uses only
  the first inequality.
- The pairing lemma is a relaxation over all pair partitions of the duplicated
  subset multiset. Relaxing the cyclic-order constraint can only lower the
  product sum used in a necessary lower bound, so it cannot invalidate the
  lower bound.
- The angular inequality uses \(R+n^2\), the largest radius scale in the full
  \(n\)-circle instance. This is weaker than using the maximum index in a
  smaller subset, but it is valid for all \(i,j\le n\) and is exactly what is
  needed for \(S=\{m,\dots,n\}\).
- The fixed-cardinality extremal result is a theorem about the pairing
  relaxation \(A(S)\), not about cyclic orders themselves. It proves that no
  nonconsecutive subset improves this method's bound, but it does not rule out
  stronger lower-bound methods.
- The two-tail corollary is a distinct relational refinement. Its proof does
  not treat an arbitrary pairing signature as a cycle: after restoring the
  distinguished insertion edge, the complete degree-two multigraph must be
  loopless and connected. The alternating-cycle upper squeeze shows that even
  this exact filter can change the optimized bound only by \(O(n^2)\); the
  resulting no-improvement conclusion is specific to one pair of consecutive
  tails.
- The asymptotic optimization uses an integer choice
  \(m_n=\lceil(\sqrt2-1)n\rceil\) with an explicit bounded rounding parameter
  \(\varepsilon_n\). The exact finite maximizers are characterized separately
  by \(\rho_n\), so no real-valued \(m\) is used as an index.
- The order-independent radius \(U_n\) remains a valid regular-direction
  baseline. The zigzag radius \(V_n\) improves its asymptotic upper coefficient
  from \(1/\pi\) to \(1/(2\pi)\); the later product-distance construction
  improves the regular-direction value again to \(8/(25\pi)\). The exact
  shortcut theorem for the same core improves the variable-spacing upper
  coefficient to \(143/(500\pi)\), which still does not match the current
  all-fixed-\(k\) lower coefficient
  \[
  {434+4\sqrt2\over1587\pi}.
  \]
  None may be described as the exact asymptotic leading constant for
  Power-Ringmin. The smaller coefficient
  \(2(\sqrt2-1)/(3\pi)\) remains optimal only inside the single-subset
  lower-bound relaxation explicitly analyzed above.
- The jointly optimized one-prefix total coefficient
  \((4+2\sqrt3)/27\) is maximal only in the one-prefix specialization of
  CR28ax--CR28bg. The value \((26-15\sqrt3)/54\) is its residual contribution
  at that optimizer, not the separate maximum of the residual coefficient.
  This does not make it the exact residual of the block or the total an exact
  geometric leading coefficient, and it proves no convergence theorem.
- The two-prefix rational coefficient \(72825421/263424000\) remains the
  earlier explicit \(n\ge59\) two-prefix specialization. The globally
  optimized CR28bw coefficient is
  \((491596+6578\sqrt{143})/2061723\), attained uniquely at the exact
  five-parameter point recorded above. No finite rounding theorem for that
  irrational point has been derived, and the optimized coefficient is not an
  exact block residual, leading coefficient, limit, or geometric constant.
- The globally optimized three-prefix coefficient is
  \[
  C_{3,*}
  ={753972193324+106042322\sqrt{377823}\over2960667770787}
  >C_{2,*}.
  \]
  Its proof uses one slack pool, every recursive split, automatic clipped
  weight ordering, and the complete compact closure. The rounded finite
  clipped theorem has minimal uniform threshold \(159\), literal expression
  \(\mathcal B_{3,n}\), integer closure \(\mathcal I_{3,n}\), and a
  controlled cubic--quadratic--linear remainder. It proves
  \(\Lambda_n>C_{3,*}n^3\) on that domain. It is not an exact
  residual, limit, or geometric leading coefficient. That rounded
  three-prefix derivation itself supplies no four-prefix theorem.
- The separate direct four-prefix theorem combines all four heights before
  assigning slack, gives the canonical one-use original-edge partition, and
  retains every recursive split through all three boundaries. Its
  four-segment lower bound is exact. The full compact optimization then
  reduces all four weights, classifies all fifteen regimes and every
  transition/collision/facet, and proves the unique strict coefficient
  \[
  C_{4,*}
  ={597580022071777213687318156
   +21288970076515705538\sqrt{2903456040383}
   \over2290468477489828247376833403}
  >C_{3,*}.
  \]
  That four-prefix optimization itself claims no finite rounding theorem,
  \(k\to\infty\) passage, or general charging result.
- The separate direct combined-height theorem does establish the exact
  indexed finite bound for every finite admissible \(k\). Its proof is
  independent of the normalized simplex and its insertion induction contains
  no frontier count. This pointwise statement by itself gives no control
  uniform in \(k=k(n)\) and no limiting-prefix interchange.
- Combining the two independent theorems at
  \(\alpha_\infty=(13-2\sqrt2)/23\) gives strictly ordered, all-middle
  parameters for every fixed finite \(k\). For each \(k\), a possibly
  different threshold \(N_k\) gives
  \(L_\Lambda\ge p(\alpha_\infty)+A_\infty^3M_k/8\). Taking the supremum of
  these scalar inequalities gives the lower endpoints
  \[
  {434+4\sqrt2\over1587},
  \qquad
  {434+4\sqrt2\over1587\pi}
  \]
  for \(\Lambda_n\) and the geometry. This is not a use of \(k=k(n)\), a
  uniform threshold, or an interchange of limits.
- The full compact clipped envelope at arbitrary finite \(k\) is the Bellman
  lower-sum problem above, with \((k+1)(k+2)/2\) regimes. Exact integration
  excludes all outer-density and high-clipped regimes from global
  optimality. Every finite-\(k\) global maximizer is uniquely strict
  all-middle, its value is \(C_{k,*}\), and
  \(C_{k,*}\nearrow C_{\mathrm{AF}}\). Hence the existing coefficient is the
  exact unattained supremum of the entire continuous finite-prefix template
  family, not merely an all-middle lower construction.
- At fixed \(k=5\), combining that theorem with the exact fifth simplex row
  and \(\alpha=13/30\) gives
  \[
  C_{5,\mathrm{rat}}
  ={2263404122555368590593580404287
   \over8177706222298165502582585481000}
  >{75\over271}>C_{4,*}.
  \]
  This is one explicit rational all-middle witness. Its exact finite
  specialization keeps the same weights, has
  minimal uniform threshold \(234\), and proves
  \(\Lambda_n>C_{5,\mathrm{rat}}n^3\) throughout that domain via the literal
  bound \(\mathcal B_{5,n}\) and integer closure \(\mathcal I_{5,n}\).
  The full compact optimization instead proves the unique strict all-middle
  coefficient \(C_{5,*}>C_{5,\mathrm{rat}}\), the exact optimum of the fixed
  \(k=5\) template, after auditing all 21 branches, transitions, collisions,
  and compact faces. It is strictly below the all-fixed-\(k\) endpoint in
  (22)--(23). No finite rounding theorem is attached to that irrational
  point. Neither fixed-five result is a growing-\(k\) argument, true residual,
  convergence theorem, new geometric lemma, or exact leading constant.
- The radius-one theorem reapplies the configuration-level induced-subset
  argument to a subset already present in the core. Inferring a core lower
  bound only from the scalar full-problem lower bound would reverse the useful
  implication and would be invalid.
- The forbidden arcs are open and each has measure \(2\theta_R(1,j^2)\), not
  \(\theta_R(1,j^2)\). Their union may overlap; subadditivity is all that is
  needed.
- The equality for \(n\ge12\) is an exact all-configuration theorem, not an
  extrapolation from the checked cases \(n=5,6\).
- The threshold \(12\) is sufficient and explicit, not claimed minimal. No
  conclusion for \(n\le11\) follows from the failure of this proof chain.
- The worst-pair reduction assumes \(R>0\), as does the angular formulation.
  At \(R=0\), the strict monotonicity used in (9) would fail.
- The regular-core proof uses the smaller circular separation for every
  unordered vertex pair. Non-adjacent pairs are not inferred from neighboring
  constraints; they are checked directly through (13)--(14).
- The formula \(U_n\) is a feasible radius, not a claim that the regular core
  is optimal or that the full infimum is attained there.
- The angular upper bound (15) is strict and assumes \(R>0\). Its stronger
  intermediate denominator \(\sqrt{R(R+i^2+j^2)}\) is what makes the strict
  inequality valid even when the product lemma is tight on the closing arc.
- The zigzag product lemma checks three distinct regimes: the maximum adjacent
  product is \(M_n\), attained on the closing arc; all other adjacent products
  are smaller (apart from the duplicate two-vertex description at \(n=3\));
  and every pair with \(q\ge2\) follows from
  \(ij\le n(n-1)<2M_n\le qM_n\).
- The zigzag construction assigns unequal-radius centers to regular-polygon
  directions, not to a common circumcircle. Equation (19) checks every pair at
  its own smaller circular distance. The formula \(V_n\) is a feasible radius,
  not a claim that the zigzag core is optimal or that \(1/(2\pi)\) is exact.

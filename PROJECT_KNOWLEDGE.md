# PROJECT_KNOWLEDGE - power-ringmin

Last reviewed: 2026-07-15

This file is stable durable project memory. Chronology, command transcripts, failed attempts, and task-local evidence belong in `ops/`.

## Project Identity

- VERIFIED FACT: working repository name is `power-ringmin`.
- VERIFIED FACT: project title is Power-Ringmin: Quadratic Radii.
- VERIFIED FACT: author is Maurizio Falconi.
- VERIFIED FACT: repository status is an independent research project, not a Ringmin worktree or branch.
- VERIFIED FACT: the authoritative project brief is `start.md`.
- VERIFIED FACT: upstream Ringmin local path is `C:\Users\Falker\Desktop\Code\circle\ringmin`.
- VERIFIED FACT: upstream public repository URL is `https://github.com/falker47/ringmin.git`.
- VERIFIED FACT: upstream inspected commit is `cc0327400819fe06b230d967cdcbafffe1648317`.
- RULE: Ringmin is prior work and a read-only upstream reference. No Ringmin theorem, implementation assumption, or structural pattern automatically transfers to quadratic radii.

## Definitions And Disproved Targets

- DEFINITION: peripheral radii are \(r_k=k^2\), for \(k=1,\dots,n\).
- DEFINITION: \(R_2^*(n)\) is the infimum feasible central radius for externally tangent peripheral circles with pairwise disjoint interiors.
- DEFINITION: optimum-radius symbols are treated as infima unless attainment
  has been proved. In particular, \(R^*_{2:n}\) is the infimum feasible
  central radius for only the core radii \(2^2,\dots,n^2\).
- DEFINITION: for peripheral radii \(r_i,r_j\) and central radius \(R\),
  \[
  \theta_R(r_i,r_j)
  =
  2\arcsin
  \sqrt{
  \frac{r_i r_j}
  {(R+r_i)(R+r_j)}
  }.
  \]
- DEFINITION: for quadratic radii,
  \[
  \theta_R(i^2,j^2)
  =
  2\arcsin
  \left(
  \frac{ij}
  {\sqrt{(R+i^2)(R+j^2)}}
  \right).
  \]
- DISPROVED CLAIM: the former principal research target
  \[
  R_2^*(n)=\frac{n^3}{6\pi}(1+o(1)).
  \]
- DISPROVED CLAIM: the former stronger target
  \[
  R_2^*(n)=\frac{n^3}{6\pi}+O(n^2).
  \]
- HEURISTIC: in the expected regime \(R\asymp n^3\), \(\theta_R(i^2,j^2)\approx 2ij/R\).
- WARNING: any heuristic leading to the former \(n^3/(6\pi)\) scale is insufficient as an asymptotic target because the induced-subset lower bound proves \(\liminf 6\pi R_2^*(n)/n^3\ge 4(\sqrt2-1)>1\).
- RULE: all-pairs non-overlap constraints are part of the problem, not merely adjacent-pair constraints.

## Fixed-Order Angular And STN Semantics

- EXACT THEOREM: for a fixed labelled cyclic order
  \((r_0,\dots,r_{m-1})\), \(m\ge3\), with \(p_0=0\), exact all-pairs
  geometric feasibility at \(R>0\) is equivalent to
  \[
  \theta_R(r_i,r_j)
  \le p_j-p_i
  \le2\pi-\theta_R(r_i,r_j)
  \qquad(0\le i<j<m).
  \]
  These inequalities automatically realize the prescribed strict cyclic
  order.
- EXACT THEOREM: with an edge \(u\to v\) encoding
  \(p_v-p_u\le w\), the implemented edges are \(j\to i\) of weight
  \(-\theta_{ij}\), named `forward_lower`, and \(i\to j\) of weight
  \(2\pi-\theta_{ij}\), named `wrap_upper`.
- EXACT THEOREM: the fixed-order STN is feasible if and only if it has no
  negative directed cycle. When it is feasible, shortest-path distances give
  a potential \(p_k=\operatorname{dist}(0,k)\); subtracting the value at node
  zero supplies the general anchored construction.
- EXACT THEOREM: for positive radii, \(\theta_R(a,b)\) is continuous and
  strictly decreasing in \(R>0\). Both STN edge weights and every directed
  cycle weight are continuous and strictly increasing. The fixed-order
  feasible-radius set has the form \([\rho_\sigma,\infty)\), with
  \(\rho_\sigma>0\).
- EXACT THEOREM (ABSTRACT ENCLOSURE IMPLICATION): if genuine oracle
  enclosures are given, a lower cycle whose relaxed weight upper bound is
  strictly negative excludes \(L\) and a right neighborhood, while an
  all-pairs upper witness whose slack lower bounds are nonnegative includes
  \(U\). Therefore
  \[
  \rho_\sigma\in(L_\sigma,U_\sigma].
  \]
  Zero lower cycle sum is undecided and rejected; zero upper witness slack is
  valid because tangency is allowed.
- EXACT THEOREM (FINITE ABSTRACT AGGREGATION): exhaustive coverage of the
  finite canonical order space gives the same half-open global meaning
  \(R_2^*(n)\in(L_{\mathrm{glob}},U_{\mathrm{glob}}]\). The current
  candidate convention
  \(\{\sigma:L_\sigma\le U_{\mathrm{glob}}\}\) is a conservative v1
  superset and is not changed by this theorem.
- CONDITIONAL COMPUTER-CERTIFIED RESULT: the checked \(n=3,4,5,6\)
  artifacts instantiate these abstract implications only under the documented
  guarded `mpmath.iv` enclosure contract.
- VERIFIED FACT: `research/FIXED_ORDER_ANGULAR_STN.md` is the authoritative
  proof; `docs/INTERVAL_BACKEND_TRUST.md` records the separate guarded
  `mpmath.iv` trust premise.
- LIMITATION: the exact real-arithmetic theorems do not prove `mpmath.iv`, its
  interval `atan2` formulation, endpoint extraction, decimal parsing, scalar
  `mp.mpf` bound arithmetic, or guard adequacy correct. Checked artifacts
  remain computer-certified finite results under that documented contract.

## Fixed-Order Maximum Cyclic Ratio

- DEFINITION: for `n>=3` and a complete order
  \(\sigma=(\sigma_0,\dots,\sigma_{n-1})\) of \(\{1,\dots,n\}\), a directed
  STN edge \(u\to v\) contributes
  \(\varepsilon(u,v)=\mathbf1_{\{u<v\}}\) to its wrap count and
  \(s_\sigma(u,v)=\sigma_u\sigma_v\) to its product sum.
- DEFINITION: for a nonempty directed closed walk \(C\), with every edge
  occurrence counted,
  \[
  q(C)=\sum_{e\in C}\varepsilon(e),
  \qquad
  S(C)=\sum_{e\in C}s_\sigma(e).
  \]
  In particular, a two-cycle on labels \(i,j\) has \(q=1\) and \(S=2ij\).
- EXACT THEOREM: every nonempty directed closed walk has \(q(C)\ge1\), because
  edges with zero wrap count strictly decrease position. Closed-walk
  decomposition makes \(S/q\) a \(q\)-weighted average of simple-cycle
  ratios. Therefore
  \[
  \Lambda(\sigma)=\max_C{S(C)\over q(C)}
  \]
  exists, is rational, and may be maximized over the finite simple-cycle set.
- DEFINITION / EXACT THEOREM: put
  \[
  \Lambda^{(1)}(\sigma)=\max\{S(C):q(C)=1\}.
  \]
  For a nonempty position subset
  \(T=\{i_0<\cdots<i_{m-1}\}\), define
  \[
  P_\sigma(T)=
  \sum_{r=0}^{m-1}\sigma_{i_r}\sigma_{i_{r+1\bmod m}}.
  \]
  Cardinality one gives \(\sigma_{i_0}^2\), while cardinality two counts the
  same unordered product twice. A one-wrap closed walk is forced to be the
  reverse orientation of exactly one induced subset order of cardinality at
  least two, so
  \[
  \Lambda^{(1)}(\sigma)
  =\max_{|T|\ge2}P_\sigma(T)
  =\max_{T\ne\varnothing}P_\sigma(T).
  \]
  The last equality holds because singleton scores are at most \(n^2\), while
  the two labels \(n-1,n\) give \(2n(n-1)>n^2\).
- EXACT THEOREM (ONE-WRAP SATURATION): for every complete order and `n>=3`,
  \[
  \Lambda(\sigma)=\Lambda^{(1)}(\sigma).
  \]
  The complete induced order has score at least
  \(n(n+1)(n+2)/6\). For every vertex-simple cycle with `q>=2`,
  \[
  {S(C)\over q(C)}
  \le {1\over2}\sum_{i=1}^n i^2
  ={n(n+1)(n+2)\over6}-{n(n+1)\over4}
  <{n(n+1)(n+2)\over6}.
  \]
  Thus every vertex-simple multi-wrap cycle is strictly dominated. General
  closed walks may repeat maximizing one-wrap components. This product-weight
  theorem does not reduce the nonlinear exact angular STN to one-wrap cycle
  checks. In particular, \(\Lambda(\sigma)\) and \(\Lambda_n\) are integers.
- EXACT THEOREM: for every complete order and `n>=3`,
  \[
  {\Lambda(\sigma)\over\pi}-n^2
  \le\rho_\sigma
  \le{\Lambda(\sigma)\over\pi}.
  \]
  Both inequalities are actually strict. The lower strictness uses
  \(\arcsin x>x\) and fixed-order threshold attainment; the upper strictness
  uses the strict angular majorant, finite simple-cycle set, and continuity.
- EXACT THEOREM: \(\Lambda\) is invariant under rotation and reflection of
  the complete cyclic order. With
  \(\Lambda_n=\min_\sigma\Lambda(\sigma)\),
  \[
  {\Lambda_n\over\pi}-n^2
  <R_2^*(n)
  <{\Lambda_n\over\pi},
  \qquad
  0<\Lambda_n-\pi R_2^*(n)<\pi n^2.
  \]
- EXACT THEOREM: the additive relation transfers normalized asymptotics:
  \(\Lambda_n=\pi R_2^*(n)+O(n^2)=\Theta(n^3)\),
  \(\Lambda_n/(\pi R_2^*(n))\to1\), and
  \[
  {2(\sqrt2-1)\over3}
  \le\liminf{\Lambda_n\over n^3}
  \le\limsup{\Lambda_n\over n^3}
  \le{8\over25}.
  \]
  This proves neither convergence nor an exact leading constant.
- EXACT THEOREM / DISTINCTION: \(\Lambda\) is a complete-order directed-cycle
  objective, while repository \(W\) is a core-order single-pair objective for
  equal regular directions. On the same cyclic order of `m` labels one has
  only \(\Lambda_{\rm same}\le mW_{\rm same}\), not equality. The global
  complete/core minima and their minimizing order sets must not be identified.
- VERIFIED FACT: `src/power_ringmin/fixed_order_cycle_ratio.py` implements the
  exact scorer by maximum descending-path closure, a one-wrap macro graph, and
  Karp maximum-cycle-mean dynamic programming in integer/`Fraction`
  arithmetic. Production code does not enumerate cycles. Its global enumerator
  has the hard domain `3<=n<=8` and a preflight ceiling of 2,520 canonical
  orders.
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): exact enumeration gives
  \[
  (\Lambda_3,\dots,\Lambda_8)=(12,26,47,77,118,172),
  \]
  canonical minimizer counts `(1,3,4,15,24,84)`, and no counterexample to the
  supplied prediction. A test-only independent simple-cycle oracle agrees on
  every canonical complete order through `n=6`. A separate exact subset/path
  oracle and literal induced-subset maximization agree on every one of the
  2,956 canonical complete orders through `n=8`, independently of production
  descending closure, macro compression, and Karp scoring. This finite result
  verifies the implementation but is not the all-order saturation proof, an
  all-`n` formula for \(\Lambda_n\), an exact geometric optimum, or an
  asymptotic theorem. The production bound remains `n<=8`.
- VERIFIED FACT: `research/FIXED_ORDER_CYCLE_RATIO.md` is the authoritative
  proof, algorithm, bounded-experiment, \(W\)-comparison, and limitations
  note.

## All-n Lower Bound

- EXACT THEOREM: for every finite index set \(S\) with \(|S|\ge 3\), every cyclic order \(\tau\) of \(S\), and the sorted duplicated multiset \(M_S=\{x_1\le\cdots\le x_{2|S|}\}\),
  \[
  \sum_\ell \tau_\ell\tau_{\ell+1}
  \ge
  \sum_{\ell=1}^{|S|}x_\ell x_{2|S|+1-\ell}.
  \]
  The proof is the rearrangement pairing lower bound applied to the duplicated multiset of indices.
- EXACT THEOREM: for every all-pairs feasible Power-Ringmin configuration and every subset \(S\) of at least three indices, the induced cyclic order on \(S\) has positive gaps summing to \(2\pi\), and each induced adjacent gap is at least the corresponding \(\theta_R(i^2,j^2)\).
- EXACT THEOREM: for every cyclic order \(\sigma\) of \(\{1,\dots,n\}\),
  \[
  \sum_{k=1}^n \sigma_k\sigma_{k+1}
  \ge
  \frac{n(n+1)(n+2)}{6},
  \]
  with indices read cyclically. The proof is the rearrangement pairing lower bound applied to the multiset with two copies of each index.
- EXACT THEOREM: for every \(n\ge 3\),
  \[
  R_2^*(n)\ge \frac{n(n+1)(n+2)}{6\pi}-n^2.
  \]
- EXACT THEOREM: for every \(n\ge 4\) and \(1\le m\le n-2\),
  \[
  R_2^*(n)\ge \frac{P_{m,n}}{\pi}-n^2,
  \qquad
  P_{m,n}
  =
  \sum_{k=m}^n k(m+n-k)
  =
  \frac{(n-m+1)(m^2+4mn+m+n^2-n)}{6}.
  \]
- EXACT THEOREM: for \(S=\{s_1<\cdots<s_q\}\), the duplicated-multiset
  pairing bound has the explicit form
  \[
  A(S)=2\sum_{a=1}^t s_a s_{2t+1-a}\quad(q=2t),
  \]
  and
  \[
  A(S)=2\sum_{a=1}^t s_a s_{2t+2-a}+s_{t+1}^2\quad(q=2t+1).
  \]
- EXACT THEOREM: at fixed cardinality \(q\), \(A(S)\) is uniquely maximized
  over \(S\subseteq\{1,\dots,n\}\) by the tail \(\{n-q+1,\dots,n\}\). Hence no
  nonconsecutive subset improves \(P_{m,n}\) inside the induced-subset plus
  duplicated-pairing plus \(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\) relaxation.
- EXACT THEOREM: the discrete maximizers of \(P_{m,n}\) over
  \(1\le m\le n-2\) are characterized by
  \[
  \rho_n=\frac{\sqrt{8n^2+8n+1}-(2n+1)}2.
  \]
  For \(n\ge4\), the unique maximizer is \(\lfloor\rho_n\rfloor+1\) unless
  \(\rho_n\in\mathbb Z\), in which case the two maximizers are
  \(\rho_n,\rho_n+1\). For \(n=3\), the domain is the singleton \(m=1\).
- EXACT THEOREM:
  \[
  \liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}\ge 4(\sqrt2-1)>1.
  \]
- VERIFIED FACT: `research/ALL_N_LOWER_BOUND.md` records the self-contained proof, including the subset-induced cyclic-gap passage, the explicit \(A(S)\) formula, the tail optimality theorem, the consecutive-subset formula \(P_{m,n}\), the exact discrete maximizer characterization by \(\rho_n\), the rounded asymptotic choice \(m=\lceil(\sqrt2-1)n\rceil\), the angular inequality \(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\), and a gap/counterexample audit.
- INTERPRETATION: the induced-subset lower bound uses only necessary consequences of all-pairs feasibility; it does not require constructing a feasible order or controlling all non-adjacent constraints for an upper bound.
- INTERPRETATION: this proves a strict lower obstruction above the former \(n^3/(6\pi)\) target; it does not prove exact optima, a matching upper bound, or an exact asymptotic constant.
- INTERPRETATION: the coefficient \(2(\sqrt2-1)/(3\pi)\) is optimal only
  within the specific relaxation named above, not necessarily for
  Power-Ringmin.
- DISPROVED CLAIM: \(R_2^*(n)=n^3/(6\pi)(1+o(1))\).
- DISPROVED CLAIM: \(R_2^*(n)=n^3/(6\pi)+O(n^2)\).

## Exact Radius-One Insertion

- EXACT THEOREM: for a feasible core configuration at central radius \(R>0\),
  the circle of radius \(1\) can be inserted at the same radius whenever
  \[
  \sum_{j=2}^n\theta_R(1,j^2)<\pi.
  \]
  Each core circle forbids an open angular arc of measure
  \(2\theta_R(1,j^2)\); subadditivity leaves an allowed angle, and the proof
  explicitly verifies every new pair \((1,j^2)\), central tangency, and
  preservation of all core-core constraints.
- EXACT THEOREM: for \(R>0\) and \(j\ge2\),
  \[
  \theta_R(1,j^2)
  <{2j\over\sqrt{R(R+j^2+1)}}
  <{2j\over R}.
  \]
- EXACT THEOREM: the full and core feasible-radius sets are equal for every
  \(n\ge12\). Consequently,
  \[
  R_2^*(n)=R^*_{2:n}\qquad(n\ge12),
  \]
  without assuming either infimum is attained.
- VERIFIED FACT: `research/ALL_N_LOWER_BOUND.md` records the self-contained
  insertion proof, exact rational boundary estimates for `n=12,13`, uniform
  symbolic estimates for `n>=14`, the configuration-level core lower-bound
  reuse, and the infimum audit.
- INTERPRETATION: `12` is a sufficient explicit threshold, not a proved
  minimal threshold. The argument gives no conclusion for `n<=11`.
- INTERPRETATION: this exact theorem is independent of the checked `n=5,6`
  candidate structures and does not turn lower negative cycles into exact
  contact graphs.

## Regular-Direction Core Cubic Upper Bounds

- EXACT THEOREM: for every \(n\ge12\) and fixed \(R>0\), the largest value of
  \(\theta_R(i^2,j^2)\) over distinct core indices \(2\le i<j\le n\) is
  attained uniquely by \((i,j)=(n-1,n)\).
- EXACT THEOREM: for every \(n\ge12\), assigning the core centers to the
  equally spaced polar directions of a regular \((n-1)\)-gon is all-pairs
  feasible at
  \[
  U_n
  =
  \sqrt{
  n^2(n-1)^2\csc^2\!\left({\pi\over n-1}\right)
  +{(2n-1)^2\over4}}
  -{n^2+(n-1)^2\over2}.
  \]
  Every non-adjacent pair is checked through its smaller regular-polygon
  separation, which is at least one edge angle.
- EXACT THEOREM: the radius-one insertion theorem gives
  \[
  R_2^*(n)\le U_n\qquad(n\ge12),
  \]
  without an attainment assumption.
- EXACT THEOREM: for every \(R>0\) and positive indices \(i,j\),
  \[
  \theta_R(i^2,j^2)<{2ij\over R}.
  \]
- EXACT THEOREM: let
  \[
  M_n=n\left(\left\lfloor{n\over2}\right\rfloor+1\right).
  \]
  In the zigzag core order \((n,2,n-1,3,\dots)\), every pair at smaller
  circular positional distance \(q\) satisfies \(ij\le qM_n\). The closing
  arc has the maximum adjacent product, exactly \(M_n\), and all pairs with
  \(q\ge2\) are covered by \(ij\le n(n-1)<2M_n\le qM_n\).
- EXACT THEOREM: assigning that zigzag order to regular \((n-1)\)-gon polar
  directions is all-pairs feasible at
  \[
  V_n={(n-1)M_n\over\pi}.
  \]
  The radius-one insertion theorem gives
  \[
  R_2^*(n)\le V_n\qquad(n\ge12),
  \]
  without an attainment assumption.
- EXACT THEOREM:
  \[
  \limsup_{n\to\infty}{R_2^*(n)\over n^3}\le{1\over2\pi},
  \qquad
  R_2^*(n)=\Theta(n^3).
  \]
- VERIFIED FACT: `research/ALL_N_LOWER_BOUND.md` records the self-contained
  proof of the order-independent baseline, general angular upper bound,
  zigzag product lemma, all-pairs feasibility, insertion step, and improved
  asymptotic conclusion.
- INTERPRETATION: the known lower and upper leading coefficients do not match.
  The value \(1/(2\pi)\) is the proved zigzag coefficient, while the later
  matching product-distance construction improves the current limsup upper
  coefficient to \(8/(25\pi)\). No geometric limit has been proved.

## Product-Distance Surrogate

- DEFINITION: for `n>=3`, put \(N=n-1\). For a cyclic order \(\sigma\) of
  the core \(\{2,\dots,n\}\), let \(d_\sigma(i,j)\) be smaller circular
  positional distance and define
  \[
  W(\sigma)=\max_{2\le i<j\le n}{ij\over d_\sigma(i,j)},
  \qquad W_n=\min_\sigma W(\sigma).
  \]
- DEFINITION: for integer \(q\ge1\),
  \[
  W_n^{(\le q)}
  =
  \min_\sigma
  \max_{\substack{i<j\\d_\sigma(i,j)\le q}}
  {ij\over d_\sigma(i,j)}.
  \]
  The adjacent relaxation is
  \(A_n=W_n^{(\le1)}=\min_\sigma\max_k\sigma_k\sigma_{k+1}\).
- EXACT THEOREM:
  \[
  A_3=6,
  \qquad
  A_n=
  \left(\left\lfloor{n\over2}\right\rfloor+1\right)
  \left(\left\lceil{n\over2}\right\rceil+2\right)
  \quad(n\ge4).
  \]
  The lower bound follows by counting forced internal cycle edges in high and
  low index blocks. The existing `patterns.interleave` construction attains the
  bound for every \(n\): its cycle edges have endpoint sums among
  \(n+1,n+2,n+3\).
- EXACT THEOREM: the equality cases are parity-specific. If `n=2t`, the
  unique high-high edge is \(\{t+1,t+2\}\); if `n=2t+1`, the two high-high
  edges are \(\{t+1,t+2\}\) and \(\{t+1,t+3\}\). There is no low-low edge,
  and removing the forced edge or high segment leaves an alternating active
  high path. Conversely, this structure is sufficient exactly when every
  crossing product is at most \(A_n\).
- EXACT THEOREM: defining \(B_n=W_n^{(\le2)}\),
  \[
  B_n=A_n\quad(3\le n\le8),
  \qquad
  B_n>A_n\quad(n\ge9).
  \]
  The proof counts incidences from a terminal high block to compatible lows;
  `n=12` is covered by a separate exact degree obstruction. Therefore
  \(W_n>A_n\) for every \(n\ge9\), without cyclic-order enumeration beyond
  `n=11`.
- DEFINITION: for exact \(T\ge0\), let \(a_T\) and \(b_T\) be the least
  integers at least two satisfying \(a_T(a_T+1)>T\) and
  \(b_T(b_T+1)>2T\). Put
  \(U_T=\{a_T,\dots,n\}\cap\{2,\dots,n\}\) and
  \(V_T=\{b_T,\dots,n\}\cap\{2,\dots,n\}\); their sizes are
  \(u=\max(0,n-a_T+1)\) and \(v=\max(0,n-b_T+1)\).
- DEFINITION: put
  \[
  \delta_n(T)
  =
  \mathbf1_{\{a_T<b_T\le n-1,\ 2T<b_T^2-1\}}.
  \]
- EXACT THEOREM: the graph on \(U_T\) with compatible edges \(xy\le2T\)
  is a split threshold graph with nested prefix neighborhoods, and its exact
  minimum number of incompatible cyclic adjacencies is
  \[
  \eta_n(T)=\max(0,2v-u+\delta_n(T)).
  \]
  For \(u=0,1\), \(\eta_n(T)=0\); for \(u=2\), the two oriented arcs are
  counted separately. At equality \(2T=b_T^2-1\), the skip-one pair is
  compatible and the correction turns off. Consequently, if a cyclic core
  order has distance-at-most-two score at most \(T\), its induced
  \(U_T\)-gaps give
  \[
  n-1\ge2u+\eta_n(T).
  \]
  The exact correction improves the clique count by zero or one. It is
  genuinely active, for example at `n=5,T=6`.
- DEFINITION / EXACT FINITE OBSTRUCTION: let \(Q_n\) be the least
  nonnegative half-integer \(T\) for which the displayed packing requirement
  is at most \(n-1\). It is computed exactly from the finite event set
  \[
  \{0\}\cup
  \{k(k+1)/2,k(k+1),(k^2-1)/2:2\le k\le n\},
  \]
  and
  \[
  B_n\ge Q_n,
  \qquad
  B_n\ge\max(A_n,Q_n).
  \]
- EXACT THEOREM: for every \(n\ge9\),
  \[
  B_n\ge Q_n\ge
  {36-16\sqrt2\over49}\left(n+{1\over2}\right)^2,
  \]
  so
  \[
  \liminf_{n\to\infty}{B_n\over n^2}
  \ge {36-16\sqrt2\over49}>{1\over4}.
  \]
  The inversion is asymptotically sharp for this subproblem:
  \[
  Q_n={36-16\sqrt2\over49}n^2+O(n).
  \]
  Hence the exact nested-neighborhood correction does not improve the leading
  coefficient furnished by this necessary condition.
  This \(Q_n\) tail-cycle coefficient is strictly below the full-distance tail
  coefficient \(2(\sqrt2-1)/3\); \(L_n\le W_n\) does not imply
  \(L_n\le B_n\).
- DEFINITION: for the same exact threshold data, put
  \[
  C_n(T)
  =
  \#\{\ell\in\{2,\dots,a_T-1\}:\ell b_T\le T\}
  =
  \max\left(0,\left\lfloor{T\over b_T}\right\rfloor-1\right).
  \]
- EXACT THEOREM: every cyclic core order with distance-at-most-two score at
  most \(T\) satisfies
  \[
  2v\le C_n(T).
  \]
  For \(n\ge4\), the two neighbors of each \(V_T\)-vertex are distinct and
  outside \(U_T\); no low can neighbor two distinct \(V_T\)-vertices because
  those highs would lie at distance at most two but have product greater than
  \(2T\). For \(n=3\), score at most \(T\) forces \(T\ge6\) and hence \(v=0\).
  The theorem also covers \(v=0\), \(v=1\), singleton and empty tails, strict
  tail equalities, non-strict compatible-low equality, and the exact floor.
- DEFINITION / EXACT FINITE OBSTRUCTION: preserve \(Q_n\) unchanged and let
  \[
  H_n
  =
  \min\left\{
  {q\over2}:q\in\mathbb Z_{\ge0},\quad
  \Psi_n(q/2)\le n-1,\quad
  2v(q/2)\le C_n(q/2)
  \right\}.
  \]
  Its exhaustive finite event set is
  \[
  \widehat E_n
  \cup
  \{k^2/2:4\le k\le n,\ k\text{ even}\},
  \]
  where \(\widehat E_n\) is the unchanged event set for \(Q_n\). Then
  \[
  B_n\ge H_n\ge Q_n,
  \qquad
  B_n\ge\max(A_n,H_n).
  \]
- EXACT THEOREM:
  \[
  H_n={8\over25}n^2+O(n),
  \qquad
  \lim_{n\to\infty}{H_n\over n^2}={8\over25},
  \qquad
  \liminf_{n\to\infty}{B_n\over n^2}\ge{8\over25}.
  \]
  The coefficient is proved by matching exact lower and upper inequalities.
  At that scale the two branches of \(\Psi_n(T)/n\) are strictly below one;
  the incidence constraint is the active asymptotic obstruction. By itself
  this does not prove convergence; the explicit matching construction below
  supplies the reverse asymptotic inequality.
- EXACT THEOREM: let
  \[
  d_n=\left\lceil{4n+8\over5}\right\rceil,
  \qquad
  T_n={d_n(d_n-1)\over2}.
  \]
  For every \(n\ge9\), the explicit cyclic order \(\sigma_n\) in
  `research/PRODUCT_DISTANCE_SURROGATE.md` satisfies
  \(W(\sigma_n)\le T_n\). The symbolic five-residue family covers every
  \(n\ge33\) and ten earlier indices; fourteen explicit initial witnesses
  cover the rest. Its proof separately checks adjacent products, distances
  two and three, closing arcs, and automatic distances at least four.
- EXACT THEOREM: for every \(n\ge9\), the terminal-high obstruction has the
  closed residue-class formula
  \[
  H_n=
  \begin{cases}
  d_n(d_n-1)/2,&n\equiv0,3,4\pmod5,\\
  (d_n-1)^2/2,&n\equiv1\pmod5,\\
  (d_n-1)(d_n-2)/2,&n\equiv2\pmod5,\ n\ge17,
  \end{cases}
  \qquad H_{12}=56.
  \]
  The uniform upper construction and separate search-free residue-one and
  residue-two constructions give
  \[
  B_n=W_n
  =
  \begin{cases}
  d_n(d_n-1)/2,&n\equiv0,3,4\pmod5,\\
  (d_n-1)^2/2,&n\equiv1\pmod5,\\
  d_n(d_n-2)/2,&n\equiv2\pmod5
  \end{cases}
  \qquad(n\ge9).
  \]
  In residue one, writing \(n=5k+1\), \(D=d_n-1=4k+2\), the explicit order
  has score exactly \(D^2/2=H_n\) for every \(k\ge2\). Its proof separately
  checks adjacent products, distances two and three, the displayed closing
  cut, and automatic distances at least four.
- EXACT THEOREM: in residue two, define
  \[
  J_n={d_n(d_n-2)\over2}.
  \]
  For every \(n=5k+2\) with \(k\ge3\), saturation of the terminal-high
  incidence injection throughout \(H_n\le T<J_n\) forces a
  low--\((d_n-2)\)--low component whose two distinct distance-two terminals
  would both have to equal \(d_n-1\). The separate exact arithmetic
  \(H_{12}=56\), \(J_{12}=60\) gives the same contradiction. Hence
  \[
  B_{12}\ge60,
  \qquad
  B_n\ge J_n
  \quad(n\equiv2\pmod5,\ n\ge17).
  \]
  A separate parity-aware order \(\sigma_n^{(2)}\), generated without search
  for every \(n=5k+2\), \(k\ge2\), is a permutation and satisfies
  \[
  W(\sigma_n^{(2)})=J_n.
  \]
  Its symbolic proof checks adjacency, distances two and three, the closing
  cut, and all distances at least four through
  \(4J_n-n(n-1)=7k^2+33k+14>0\). Therefore
  \[
  B_n=W_n=J_n
  \]
  at \(n=12\) and for every \(n\equiv2\pmod5\), \(n\ge17\). The case \(n=7\)
  remains covered by the bounded exact table. The older uniform threshold has
  slack \(T_n-J_n=d_n/2\), which is not an objective gap.
- EXACT THEOREM: the matching lower and upper bounds give
  \[
  \lim_{n\to\infty}{B_n\over n^2}
  =\lim_{n\to\infty}{W_n\over n^2}
  ={8\over25}.
  \]
  For `n>=12`, exact core feasibility and radius-one insertion give
  \[
  R_2^*(n)\le{(n-1)T_n\over\pi},
  \qquad
  \limsup_{n\to\infty}{R_2^*(n)\over n^3}\le{8\over25\pi}.
  \]
  The geometric conclusion is an upper coefficient, not an exact leading
  constant or a convergence theorem.
- EXACT THEOREM: assigning \(\sigma\) to equally spaced polar directions
  makes the core strictly all-pairs feasible at
  \[
  R={N W(\sigma)\over\pi}.
  \]
  For `n=3`, the two core directions are treated explicitly as antipodal.
  The proof checks every pair using
  \(\theta_R(i^2,j^2)<2ij/R\).
- EXACT THEOREM: for `n>=12`, equality of the full and core feasible-radius
  sets transfers the construction and gives
  \[
  R_2^*(n)\le {N W(\sigma)\over\pi},
  \qquad
  R_2^*(n)\le {N W_n\over\pi}.
  \]
- EXACT THEOREM: for every `2<=m<=n-2`, the induced oriented positional gaps
  of the tail \(\{m,\dots,n\}\) are positive, sum to \(N\), and dominate the
  corresponding smaller circular distances. Combined with the
  duplicated-multiset pairing lemma, this proves
  \[
  W(\sigma)\ge {P_{m,n}\over N}.
  \]
- EXACT THEOREM:
  \[
  \lim_{n\to\infty}{A_n\over n^2}={1\over4}
  <
  {2(\sqrt2-1)\over3}
  =
  \lim_{n\to\infty}{L_n\over n^2},
  \qquad
  L_n=\max_{2\le m\le n-2}{P_{m,n}\over n-1}.
  \]
  The explicit tail \(m=\lceil2n/5\rceil\), checked symbolically by residue
  class modulo \(10\), proves \(L_n>A_n\) for every \(n\ge33\).
- VERIFIED FACT (FINITE EXACT COMPUTATION): exact rational evaluation of the
  proved tail formula gives \(L_n\le A_n\) for every \(4\le n\le32\).
  Therefore \(33\) is the first index at which this tail obstruction alone
  proves that non-adjacent constraints are essential.
- EXACT THEOREM: the zigzag score is exactly
  \(W(z_n)=M_n=n(\lfloor n/2\rfloor+1)\), because the general zigzag lemma
  gives the upper bound and the closing pair attains it.
- VERIFIED FACT: `src/power_ringmin/product_distance.py` provides exact
  all-pairs `Fraction` scoring, core-cycle canonicalization, explicit `n=3`
  handling, the exact adjacent formula, a direct parity-specific adjacent
  equality classifier, the exact nested-neighborhood tail-cycle
  incompatibility, compatible-low capacity, unchanged finite two-threshold
  obstruction, joint terminal-high incidence obstruction, its constant-time
  exact residue-class formula, the explicit eight-twenty-fifths order and
  threshold, the exact-threshold residue-one and residue-two orders,
  full-distance tail obstructions,
  and deterministic full and truncated enumeration with the hard domain
  `3<=n<=11` and a preflight canonical-order ceiling. The explicit upper
  generators perform no search or enumeration. The module creates no CLI or
  serialized artifact.
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): enumeration of all
  `204557` canonical rotation/reflection classes for `n=3..11` gives
  \[
  (W_3,\dots,W_{11})=(6,12,15,20,24,30,36,45,50)
  \]
  and canonical minimizer counts
  \((1,1,1,2,2,4,12,72,24)\). Exact representatives, zigzag comparisons,
  and tail lower obstructions are recorded in
  `research/PRODUCT_DISTANCE_SURROGATE.md`.
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION):
  \[
  (W_3^{(\le1)},\dots,W_{11}^{(\le1)})
  =(6,12,15,20,24,30,35,42,48),
  \]
  while \(W_n^{(\le2)}=W_n\) for every enumerated \(3\le n\le11\).
  The first gap from the adjacent relaxation is
  \(A_9=35<36=W_9^{(\le2)}=W_9\). The distance-two and full canonical
  minimizer sets also coincide throughout this bounded range.
- VERIFIED FACT (FINITE EXACT FORMULA EVALUATION): the new finite obstruction
  gives
  \[
  (Q_3,\dots,Q_{11})=(6,12,12,20,21,30,63/2,42,45).
  \]
  Thus \(\max(A_n,Q_n)=A_n\) throughout this bounded table. This formula
  evaluation is not cyclic-order enumeration and does not weaken the all-\(n\)
  asymptotic improvement over \(A_n\).
- VERIFIED FACT (FINITE EXACT FORMULA EVALUATION): the joint obstruction gives
  \[
  (H_3,\dots,H_{11})=(6,12,15,20,21,30,36,45,50).
  \]
  Hence \(\max(A_n,H_n)=B_n\) throughout the existing bounded exact table.
  This comparison does not assert an all-\(n\) formula and does not extend
  cyclic-order enumeration beyond \(n=11\).
- INTERPRETATION: zigzag is surrogate-optimal for `n=3,4,5` and strictly
  suboptimal for every enumerated `n=6..11`; the best tail obstruction is
  strict for every enumerated case where it is defined.
- INTERPRETATION: the finite table is not an all-`n` formula, a geometric
  certificate, or proof that the surrogate radius is geometrically optimal
  for a fixed order. No conjecture is promoted from these nine cases.
- EXACT THEOREM (FINITE-EXHAUSTIVE PLUS SYMBOLIC): the exact table proves
  \(B_n=W_n\) for \(3\le n\le11\), while the residue-class theorem proves it
  for every \(n\ge9\). These domains cover every \(n\ge3\), so
  \[
  W_n^{(\le2)}=B_n=W_n\qquad(n\ge3).
  \]
  Consequently \(W_n^{(\le q)}=W_n\) for every integer \(q\ge2\); positional
  distances at least three never change the optimum value.
- EXACT THEOREM: if \(\mathcal M_n\) and
  \(\mathcal M_n^{(\le2)}\) denote the full and distance-two minimizer sets,
  then
  \(\mathcal M_n\subseteq\mathcal M_n^{(\le2)}\) for every \(n\ge3\).
  More sharply, every omitted pair has score at most \(n(n-1)/3\), so
  \(n(n-1)/3\le B_n\) implies equality of the two sets.
- EXACT THEOREM: exact residue-class evaluation of the preceding criterion,
  together with the bounded exact values for \(3\le n\le8\), proves
  \[
  \mathcal M_n=\mathcal M_n^{(\le2)}
  \qquad(3\le n\le92).
  \]
  At \(n=93\), move label \(54\) in
  \(\operatorname{eight\_twenty\_fifths\_order}(93)\) from between \(4,3\)
  to between \(16,48\). Exact all-pairs scoring gives
  \(W^{(\le2)}=2850=B_{93}\) and \(W=2852\), with \((92,93)\) at distance
  three. Hence
  \[
  \mathcal M_{93}\subsetneq\mathcal M_{93}^{(\le2)},
  \]
  and \(93\) is the first index where distances at least three restrict the
  minimizer set. This uses no canonical enumeration beyond \(n=11\) and has
  no geometric implication.
- OPEN QUESTION: for which \(n\ge94\) is the minimizer inclusion strict? No
  persistence from \(n=93\) onward is claimed; the sufficient equality
  criterion already holds again at \(n=94\).
- OPEN QUESTION: structural characterizations of minimizing orders remain
  open in every residue class.

## Verified Computational Machinery

- VERIFIED FACT: the Python package import name is `power_ringmin`; package source is under `src/power_ringmin/`; tests are under `tests/`.
- VERIFIED FACT: substantial imported/adapted code is licensed under MIT and records upstream Ringmin commit `cc0327400819fe06b230d967cdcbafffe1648317` in module docstrings.
- VERIFIED FACT: `src/power_ringmin/geometry.py` provides positive-radius validation, `quadratic_radii(n)`, `theta(R,a,b)`, cyclic adjacent pairs, and cycle-equivalence helpers.
- VERIFIED FACT: `src/power_ringmin/evaluator.py` provides a float64 fixed-order evaluator using all-pairs STN feasibility, radius bracketing, recovered positions, Cartesian validation, essential tight-pair detection, and floating-radius detection.
- VERIFIED FACT: `src/power_ringmin/highprec.py` provides an independent `mpmath` fixed-order feasibility verifier, high-precision full-radius bisection, position recovery, and pair slack checks.
- VERIFIED FACT: `src/power_ringmin/crosscheck.py` provides a radius-sequence-aware fixed-order SLSQP cross-check using all-pairs Cartesian non-overlap constraints and explicit fixed-order angle variables.
- VERIFIED FACT: `src/power_ringmin/patterns.py` provides selected generic order constructors: sequential, zigzag, interleave, Supnick maximum-tour form, Supnick minimum-tour form, and JSON order loading.
- VERIFIED FACT: root `verify.py` is a standalone high-precision fixed-order verifier scaffold that imports only the Python standard library and `mpmath`.
- VERIFIED FACT: `schemas/fixed_order_result.schema.json` defines the v1 JSON artifact schema for one fixed-order numerical result.
- VERIFIED FACT: `src/power_ringmin/fixed_order_artifact.py`, `src/power_ringmin/export_fixed_order_cli.py`, `src/power_ringmin/export_fixed_order_batch_cli.py`, and `src/power_ringmin/verify_fixed_order_artifacts_cli.py` provide fixed-order artifact construction, export, batch export, and standalone-verifier checking.
- VERIFIED FACT: `src/power_ringmin/search_small_n.py` provides canonical quadratic index-order enumeration modulo rotation and reflection, canonicalization, quadratic index-to-radius conversion, exhaustive float64 small-`n` search, and v1 small-`n` search JSON helpers.
- VERIFIED FACT: `ops/TASK-20260711__interval_verifier_semantics/DESIGN.md` records the design semantics for finite small-`n` interval certification.
- VERIFIED FACT: `research/FIXED_ORDER_ANGULAR_STN.md` discharges the
  historical fixed-order proof obligations, including the exact angular/STN
  equivalence, negative-cycle criterion, potential recovery, radius
  monotonicity and continuity, half-open endpoint semantics, and finite global
  aggregation.
- VERIFIED FACT: `src/power_ringmin/interval_verifier.py` implements local fixed-order interval bracket verifier semantics for one canonical quadratic index order.
- VERIFIED FACT: the local interval bracket verifier checks the radius order against the index-order squares, rejects noncanonical index orders, requires exact local `artifact_type`, requires exact backend metadata matching for every field declared by the oracle including `rounding_policy`, rejects tolerance-based interval metadata, checks a lower endpoint by an explicit negative cycle using relaxed interval edge upper weights, and checks an upper endpoint by explicit all-pairs witness slacks using theta upper bounds.
- VERIFIED FACT: `MPMathIntervalAngularOracle` provides a guarded `mpmath.iv` angular interval backend using `atan2(x, sqrt(1-x^2))` for the inverse-sine step and records backend precision, guard, rounding policy, outward-enclosure, certification-capability, and no-tolerance metadata.
- VERIFIED FACT: `src/power_ringmin/interval_bracket_exporter.py` provides a fixed-order interval bracket generator/exporter for records consumed by the local interval verifier.
- VERIFIED FACT: generated fixed-order interval bracket records are local fixed-order certificate building blocks only; they do not certify a global small-`n` optimum unless a global verifier covers every canonical order.
- VERIFIED FACT: `src/power_ringmin/small_n_interval_certificate.py` provides a finite small-`n` interval certificate aggregator that embeds local fixed-order interval bracket records, independently regenerates the canonical cyclic index-order space, verifies exactly one local bracket per canonical order, and computes a finite global radius bracket from verified local endpoints.
- VERIFIED FACT: `schemas/small_n_interval_certificate.schema.json` defines the v1 structural JSON Schema for finite small-`n` interval certificate artifacts.
- VERIFIED FACT: `power-ringmin-export-small-n-interval-certificate` is a bounded general finite small-`n` certificate CLI that requires an explicit `--max-canonical-orders` ceiling and supports `--dry-run` preflight.
- VERIFIED FACT: small-`n` certificate generation is currently work-count bounded by canonical-order count and local retry count, not wall-clock bounded.
- VERIFIED FACT: `schemas/finite_results_summary.schema.json` defines the v1 structural JSON Schema for a separate derived finite-results summary artifact, `power-ringmin.finite_results_summary.v1`.
- VERIFIED FACT: `src/power_ringmin/finite_results.py` provides the derived finite-results summary builder, dump/load helpers, CLI, and semantic validator for checked source certificates.
- VERIFIED FACT: finite-results summary validation reloads every source small-`n` interval certificate through the semantic certificate loader, recomputes source `content_sha256` values, rederives candidate sets and exclusion gaps, and rejects stale summaries when source content or derived content no longer match.
- VERIFIED FACT: finite-results `content_sha256` is a cross-platform source-content SHA-256 digest: the source certificate byte stream is hashed after normalizing every CRLF sequence and every lone CR byte to one LF byte, with no character decoding or other byte normalization.
- VERIFIED FACT: JSON Schema validation is structural only; semantic Python validators remain authoritative for interval verification, checked-artifact source freshness, and derived summary consistency.
- VERIFIED FACT: `src/power_ringmin/verify_checked_artifacts.py` provides `power-ringmin-verify-checked-artifacts`, a deterministic checked-artifact verification command that discovers checked finite certificates, validates JSON Schema structure, reloads semantic validators, explicitly re-verifies embedded local interval brackets, validates the finite-results summary, and rejects summary source mismatches.
- VERIFIED FACT: `docs/INTERVAL_BACKEND_TRUST.md` documents the current guarded `mpmath.iv` backend trust contract, guards, tested coverage, unproved/audited gaps, classification implications, and possible stronger future trust paths.
- VERIFIED FACT (WORKFLOW CONFIGURATION): `.github/workflows/verification.yml` defines a GitHub Actions workflow for Python `3.11`, `3.12`, and `3.13` that installs package test and crosscheck extras, runs the full test suite, runs checked-artifact semantic verification, runs schema validation tests, and runs diff/trailing-whitespace hygiene checks.
- VERIFIED FACT: `pyproject.toml` registers console scripts for fixed-order export, batch fixed-order export, fixed-order interval bracket export, checked `n=3`/`n=4` interval certificate export, general small-`n` interval certificate export, fixed-order artifact verification, small-`n` float64 search, derived finite-results summary generation, critical-structure analysis, and checked-artifact verification.
- LOCAL VERIFIED FACT: successful local tests, checked-artifact verification,
  workflow inspection, and hygiene checks are recorded in
  `ops/TASK-20260712__verification_trust_layer_ci/` and
  `ops/TASK-20260712__cross_platform_finite_hash_ci/`; these checks do not
  establish hosted GitHub Actions status.
- HISTORICAL USER-REPORTED STATUS: the 2026-07-12 research-roadmap task
  recorded a green hosted run after the cross-platform fix, but no commit SHA,
  run identifier, URL, or independently inspected result was recorded. It
  establishes no hosted status for a specific commit.
- CURRENT HOSTED STATUS: GitHub Actions for the current `HEAD` has not been
  independently verified.
- INTERPRETATION: float64 and high-precision numerical search/recheck artifacts are numerical observations unless interval evidence covers the relevant finite order space.

## Certified Finite Results

The following checked artifacts are classified as COMPUTER-CERTIFIED RESULT under the repository's documented local interval-verifier semantics and guarded `mpmath.iv` interval-backend contract.

| `n` | Canonical order count | Certified global lower endpoint | Certified global upper endpoint | Checked artifact path | Certification limitation |
|---:|---:|---|---|---|---|
| 3 | 1 | `0.3832870361393696523322205393924377858638763427734375` | `0.383487036139369685816546962087159045040607452392578125` | `examples/small_n_interval_certificate_n3.json` | finite `n` only; no exact optimum, all-`n` theorem, or asymptotic claim; guarded `mpmath.iv` backend provenance remains a limitation |
| 4 | 3 | `1.4955284118749971877804227915476076304912567138671875` | `1.4957284118749971657535979829845018684864044189453125` | `examples/small_n_interval_certificate_n4.json` | finite `n` only; no exact optimum, all-`n` theorem, or asymptotic claim; guarded `mpmath.iv` backend provenance remains a limitation |
| 5 | 12 | `3.934227717145796443531935437931679189205169677734375` | `3.9344277171457964215051106293685734272003173828125` | `examples/small_n_interval_certificate_n5.json` | finite `n` only; no exact optimum, all-`n` theorem, or asymptotic claim; guarded `mpmath.iv` backend provenance remains a limitation |
| 6 | 60 | `8.4678350760883720482752323732711374759674072265625` | `8.4680350760883715821591977146454155445098876953125` | `examples/small_n_interval_certificate_n6.json` | finite `n` only; no exact optimum, all-`n` theorem, or asymptotic claim; guarded `mpmath.iv` backend provenance remains a limitation |

- INTERPRETATION: these finite brackets do not prove exact threshold values;
  each strict lower endpoint is excluded, each upper endpoint is certified
  feasible, and the threshold infimum lies in the displayed half-open interval
  \((L,U]\) under the guarded backend contract.
- INTERPRETATION: these finite brackets do not prove exact values or
  asymptotic claims; the disproof of the former \(n^3/(6\pi)\) target comes
  from the all-\(n\) induced-subset theorem, not from finite certificates.

Candidate-set extraction uses the following finite-certificate semantics.

- DEFINITION: for one finite certificate with verified local brackets, \(U\) is the minimum verified upper endpoint across all canonical orders, and the certified candidate set is \(C=\{\sigma:L_\sigma\le U\}\), where \(L_\sigma\) is the verified strict lower endpoint for order \(\sigma\).
- DEFINITION: an order with \(L_\sigma>U\) is certified not to be globally optimal under the checked artifact semantics.
- DEFINITION: when at least one order is excluded, the exclusion gap is \(\Delta=\min_{\sigma\notin C}(L_\sigma-U)\).
- COMPUTER-CERTIFIED RESULT: derived from the checked `n=3..6` artifacts, current candidate-set sizes and exclusion gaps are:

| `n` | Candidate-set size | Excluded-order count | Exclusion gap |
|---:|---:|---:|---|
| 3 | 1 | 0 | undefined |
| 4 | 1 | 2 | `0.1171644705802874497635457373689860105514526367187500` |
| 5 | 2 | 10 | `0.1137866156209259571596703608520328998565673828125` |
| 6 | 5 | 55 | `0.0488707956703002821541304001584649085998535156250` |

- INTERPRETATION: candidate-set size `1` means there is a unique certified candidate order modulo the current rotation/reflection convention.
- WARNING: candidate-set size greater than `1` does not prove an exact tie between the candidate orders.
- WARNING: identical serialized local brackets must not be described as exact
  equality of the corresponding fixed-order threshold infima.
- VERIFIED FACT: the checked derived summary artifact `examples/finite_results_summary_n3_n6.json` records the `n=3..6` certified finite brackets, candidate sets, exclusion gaps, identical serialized bracket groups, source certificate line-ending-normalized `content_sha256` values, and finite-`n` ratios under `power-ringmin.finite_results_summary.v1`.
- INTERPRETATION: `examples/finite_results_summary_n3_n6.json` is derived analysis over checked source certificates. It does not replace the primary certificate artifacts and does not change `power-ringmin.small_n_interval_certificate.v1`.

## Empirical Structural Questions

- OPEN QUESTION: can tighter brackets or independent methods reduce the multiple certified candidate sets for `n=5` and `n=6`?
- OPEN QUESTION: how do the checked finite brackets compare numerically with the induced-subset lower obstruction at small `n`?
- OPEN QUESTION: do the checked finite cases suggest stable optimal-order representatives, floating-circle regimes, or contact structures that can be formulated as conjectures?

## Candidate Critical-Structure Analysis

- VERIFIED FACT: `src/power_ringmin/critical_structure.py` provides deterministic structural analysis for checked finite candidate orders, including lower negative-cycle normalization, stable index/radius-pair labels, interval-lower upper-witness slack rankings, candidate common-core intersections, candidate differences, weak-constraint proxy labels, and identical-bracket diagnostics.
- VERIFIED FACT: `ops/TASK-20260712__critical_constraints_order_structure/critical_structure_n3_n6.json` records the checked `n=3..6` candidate-order structural analysis under `power-ringmin.critical_structure_analysis.v1`.
- VERIFIED FACT: `research/FINITE_RESULTS.md` summarizes the checked finite results and structural diagnostics with separate evidence labels for computer-certified finite facts, verified structural data, numerical observations, empirical patterns, heuristics, conjectures, open questions, and warnings.
- VERIFIED FACT: for the checked certified candidate orders at `n=5`, both candidates share the same lower negative-cycle pair set `{2-4, 2-5, 3-4, 3-5}` after stable index/radius-pair normalization.
- VERIFIED FACT: for the checked certified candidate orders at `n=6`, all five candidates share the same lower negative-cycle pair set `{2-5, 2-6, 3-4, 3-6, 4-5}` after stable index/radius-pair normalization.
- EMPIRICAL PATTERN: in the checked multiple-candidate cases `n=5` and `n=6`, the repeated serialized candidate brackets align with a shared lower-cycle pair core on indices `2..n`, while directed cycle signatures and upper-witness minimum-slack pair sets are not common across all candidates.
- HEURISTIC: under the recorded finite proxy rule, index `1` is a possible weakly constrained index for the checked multiple-candidate cases `n=5` and `n=6`; this is not a certified floating-circle or active-constraint non-incidence statement.
- WARNING: lower negative cycles are lower-endpoint infeasibility certificates, not exact active contact graphs; upper-witness slack rankings are finite numerical diagnostics at certified upper endpoints.
- OPEN QUESTION: can the shared lower-cycle core on indices `2..n` be formulated as a smaller exact reduced subsystem, or is it an artifact of the current bracket generator and resolution?
- OPEN QUESTION: can tighter brackets or independent fixed-order analysis determine whether repeated serialized brackets at `n=5` and `n=6` reflect exact ties, hidden symmetry, or numerical coincidence?

## Current Research Roadmap

- VERIFIED FACT: `research/NEXT_RESEARCH_STEPS.md` is the current concise
  roadmap synthesizing checked `n=3..6` certificates, candidate-set and
  critical-structure diagnostics, verifier limitations, workflow provenance,
  the induced-subset lower bound, exact insertion theorem, regular-direction
  bounds, bounded product-distance enumeration through \(n=11\), the all-\(n\)
  matching construction, the exact residue-class formulas, and their global
  consequence \(W_n^{(\le2)}=B_n=W_n\) for every \(n\ge3\), together with
  minimizer-set equality through \(n=92\) and its first strict inclusion at
  \(n=93\), plus the exact one-wrap induced-subset characterization and
  saturation of \(\Lambda(\sigma)\) for every complete order.
- INTERPRETATION: the cubic order is settled; after the zigzag improvement
  from \(1/\pi\) to \(1/(2\pi)\), the matching product-distance construction
  improves the current regular-direction upper coefficient to
  \(8/(25\pi)\). Further narrowing the geometric coefficient gap is more
  valuable than automatic `n=7` enumeration.
- COMPLETED PRIORITY: `research/FIXED_ORDER_ANGULAR_STN.md` now proves the
  fixed-order angular/STN equivalence, negative-cycle and potential theorems,
  radius dependence, half-open endpoint semantics, and explicit interval
  trust boundary.
- RECOMMENDED NEXT TASK: design a bounded independent interval-backend
  cross-verification path for the existing checked artifacts, without
  generating a larger finite certificate or changing current claims.
- EXACT THEOREM: the reduced-core insertion question has an all-configuration
  answer at the level of feasible radii for `n>=12`: index `1` can be inserted
  without increasing the central radius. This does not assert a fixed-order
  active-subsystem description or settle `n<=11`.
- OPEN QUESTION: can the upper coefficient \(8/(25\pi)\) be lowered toward
  the induced-subset coefficient \(2(\sqrt2-1)/(3\pi)\), while retaining a
  symbolic all-pairs proof?
- RULE: an `n=7` exhaustive certificate should be considered only after structural analysis produces a precise discriminator such as competing order-family predictions, a predicted candidate-set cardinality, a predicted critical-cycle transition, or a predicted first floating-index pattern.

## Proof Obligations And Limitations

- CLOSED PROOF OBLIGATION: the fixed-order angular/STN equivalence and
  endpoint semantics are proved in `research/FIXED_ORDER_ANGULAR_STN.md`.
- LIMITATION: the current certified finite results depend on the documented guarded `mpmath.iv` interval-backend contract; backend trust/provenance remains a production-review item.
- LIMITATION: finite computation for `n=3..6` is not proof for all `n`.
- LIMITATION: no exact geometric optimum value \(R_2^*(n)\) has been proved
  in this repository; the exact all-\(n\) classification of the combinatorial
  surrogate \(W_n\) is a different statement.
- LIMITATION: no upper bound matching the induced-subset leading coefficient
  has been proved in this repository.
- LIMITATION: the later indices \(n\ge94\) with strict distance-two/full
  minimizer inclusion have not been classified.
- LIMITATION: neither existence of \(\lim R_2^*(n)/n^3\) nor a leading-term
  asymptotic formula has been proved in this repository.
- LIMITATION: no Ringmin result should be silently generalized to quadratic radii.
- LIMITATION: the sufficient radius-one threshold `12` is not known to be
  minimal, and the exact equality question remains open for `n<=11`.

## Evidence Classification Rules

Every material mathematical or computational claim must be classified where relevant as one of:

- definition;
- verified fact;
- exact theorem;
- computer-certified result;
- numerical observation;
- empirical pattern;
- heuristic;
- conjecture;
- unresolved claim;
- disproved claim.

Rules:

- finite computation is not proof for all `n`;
- a conjecture must not be used as an established lemma;
- conditional arguments must be labeled conditional;
- all-pairs constraints must be checked, not only adjacent pairs;
- numerical precision, parameters, solver, seeds, environment, and code version must be recorded when relevant;
- contradictory evidence must be preserved and investigated;
- task chronology and detailed command evidence belong in `ops/`, not in this file.

## Canonical Commands

- `python -m pytest`
- `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
- `python -m pytest tests\test_checked_artifact_schema_validation.py`

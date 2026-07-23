# PROJECT_KNOWLEDGE - power-ringmin

Last reviewed: 2026-07-23

This file is compact stable project memory. Detailed proofs live in
`research/*.md`; roadmap, chronology, command transcripts, failed attempts,
and task-local evidence belong respectively in `research/NEXT_RESEARCH_STEPS.md`
and `ops/`.

## Project Identity

- VERIFIED FACT: working repository name is `power-ringmin`.
- VERIFIED FACT: project title is Power-Ringmin: Quadratic Radii.
- VERIFIED FACT: author is Maurizio Falconi.
- VERIFIED FACT: repository status is an independent research project, not a Ringmin worktree or branch.
- VERIFIED FACT: document roles and precedence are defined by `AGENTS.md`;
  `start.md` is only a deprecated compatibility pointer.
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
- LOCAL VERIFIED FACT (FINITE TEST-ONLY INDEPENDENT BACKEND CROSS-CHECK):
  `tests/test_n3_arb_interval_crosscheck.py` reads the checked `n=3` artifact
  directly and, at 384-bit precision with python-flint 0.9.0 / FLINT 3.6.0,
  independently recomputes each required theta with Arb `sqrt` and direct
  `asin`, recomputes `2*pi`, checks all three lower-cycle edge occurrences,
  and checks both directional slacks for all three upper-witness pairs. The
  recomputed cycle upper bound is strictly negative and all six slack lower
  bounds are nonnegative.
- INTERPRETATION: the bounded Arb result corroborates the decisive endpoint
  signs for checked `n=3` only. It neither audits Arb/FLINT nor covers
  `n=4,5,6`, and it changes no artifact, schema, bracket, supported production
  backend, classification, or certified claim.
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
- DEFINITION: for a cyclic core order \(\tau\) of \(\{2,\ldots,n\}\), let
  \[
  K(\tau)
  =
  \max_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P_\tau(U),
  \]
  where the cyclic order is induced by \(\tau\), a singleton contributes
  \(j^2\), and a two-element subset contributes \(2ij\).
- EXACT THEOREM (INDEX-ONE ELIMINATION): if \(\tau\) is obtained from a
  complete order \(\sigma\) by deleting label \(1\), then
  \[
  \Lambda(\sigma)=K(\tau),
  \]
  independently of the insertion gap of label \(1\). Subsets avoiding
  \(1\) retain their score. The remaining cases are: \(\{1\}\) has score
  \(1<4\); \(\{1,j\}\) has score \(2j\le j^2\); and if a subset has at
  least two core labels with distinct core neighbors \(a,b\) around \(1\),
  deleting \(1\) increases its score by
  \(ab-a-b=(a-1)(b-1)-1\ge1\). Thus no maximizing subset contains label
  \(1\). This theorem concerns \(\Lambda\), not \(\rho_\sigma\) or exact
  fixed-order feasibility.
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
- EXACT THEOREM: deletion is surjective from complete cyclic orders to core
  cyclic orders, and every insertion has the same score, so
  \[
  \Lambda_n=\min_\tau K(\tau).
  \]
  Singleton terms do not attain \(K\), hence the accepted same-order
  comparison gives
  \[
  K(\tau)\le\Lambda_{\rm same}(\tau)\le(n-1)W(\tau),
  \qquad
  \Lambda_n\le(n-1)W_n.
  \]
  Consequently the geometric infimum satisfies the all-\(n\) upper bound
  \[
  R_2^*(n)<{\Lambda_n\over\pi}
  \le{(n-1)W_n\over\pi}
  \qquad(n\ge3).
  \]
  This route neither uses radius-one insertion nor constructs regular
  directions; it supplies an upper bound, not an exact optimum.
- EXACT THEOREM (LABEL-CANCELLATION MONOTONICITY): if \(3\le n\le N\),
  cancelling labels \(n+1,\ldots,N\) from a complete order preserves the
  induced cyclic order and product score of every nonempty subset of
  \(\{1,\ldots,n\}\). One-wrap saturation therefore gives
  \[
  \Lambda(\sigma|_n)\le\Lambda(\sigma),
  \qquad \Lambda_n\le\Lambda_N.
  \]
  This is monotonicity of the unnormalized global combinatorial score. It is
  not monotonicity of \(\Lambda_n/n^3\), an equality statement, or a
  minimizing-order classification.
- DEFINITION / EXACT THEOREM (TWO NESTED TAILS): for `n>=4` and
  `1<=m<=n-3`, put \(S_m=\{m,\ldots,n\}\) and define
  \[
  \beta_{m,n}
  =\min_{\substack{C\text{ simple on }S_{m+1}\\
                    e=\{a,b\}\in E(C)}}
  \left(P(C)+[m(a+b)-ab]_+\right).
  \]
  Deleting \(m\) gives the exact correction
  \(m(a+b)-ab=m^2-(a-m)(b-m)\). Every cycle/edge pair extends to a
  complete order, so
  \[
  \beta_{m,n}
  =\min_\sigma\max\{P_\sigma(S_m),P_\sigma(S_{m+1})\},
  \qquad
  \Lambda_n\ge\beta_n^{(2)}:=\max_m\beta_{m,n}.
  \]
- EXACT THEOREM (PAIRING-SIGNATURE VALIDITY): a pairing of the duplicated
  labels of \(S_{m+1}\) is automatically degree two. On at least three
  labels it represents one simple spanning cycle exactly when the associated
  multigraph is loopless and connected; an explicit equivalent audit also
  rejects repeated unordered edges. Degree two, or only the local
  loop/repetition checks, does not exclude disjoint subcycles. For a fixed
  insertion edge, the full signature after restoring that edge must pass the
  audit. The two-label convention is the exceptional double edge.
- EXACT METHOD-SPECIFIC THEOREM: the inner-tail pairing floor and an explicit
  alternating simple cycle give the uniform squeeze
  \[
  P_{m+1,n}\le\beta_{m,n}\le P_{m+1,n}+n^2.
  \]
  Therefore
  \[
  \beta_n^{(2)}
  ={2(\sqrt2-1)\over3}n^3+O(n^2),
  \qquad
  \lim_{n\to\infty}{\beta_n^{(2)}\over n^3}
  ={2(\sqrt2-1)\over3}.
  \]
  The two-tail refinement may improve finite terms--for example
  \(\beta_{4,10}=323>P_{5,10}=320\)--but cannot improve the cubic
  coefficient. This limitation is specific to one optimized pair of
  consecutive tails; it is not an asymptotic evaluation of \(\Lambda_n\)
  and does not cover coupling a number of tails growing with \(n\).
- DEFINITION / EXACT THEOREM (THREE NESTED TAILS): for \(n\ge5\) and
  \(1\le m\le n-4\), put \(x=m+1\), \(y=m\), \(T=S_{m+2}\), and define
  \[
  P^*_{m+2,n}
  =\min_{C\in\mathcal C(T)}P(C).
  \]
  Deleting \(y\), then \(x\), gives a bijection between cycles on \(S_m\)
  and triples consisting of a simple base cycle \(C\) on \(T\), a first edge
  \(e\in E(C)\), and a second edge
  \(f\in E(C\mathbin\oplus_e x)\). With
  \(\delta_t(u,v)=t(u+v)-uv\), the exact obstruction is
  \[
  \gamma^*_{m,n}
  =
  \min_{C,e,f}
  \left[
  P(C)+
  \max\{0,\delta_x(e),\delta_x(e)+\delta_y(f)\}
  \right].
  \]
  The second split is either one of the two children of \(e\), one of the
  two surviving base edges incident to \(e\), or one of the \(q-3\) disjoint
  base edges. Nested splits can tie but are weakly dominated in the minimum,
  so an equivalent formula minimizes over two distinct base edges.
- EXACT THEOREM (THREE-TAIL COMPATIBILITY): every base, intermediate, and
  final pairing signature must be one connected loopless degree-two spanning
  graph with no repeated unordered edge, and consecutive signatures must be
  linked by the literal split identities. Independently valid signatures or
  degree conditions alone do not suffice; contraction restores the second
  split edge first and the first split edge second.
- EXACT METHOD-SPECIFIC THEOREM: uniformly over the full domain,
  \[
  0\le\gamma^*_{m,n}-P^*_{m+2,n}<2n^2,
  \qquad
  P_{m+2,n}\le\gamma^*_{m,n}<P_{m+2,n}+2n^2.
  \]
  Hence, for
  \(\Gamma_n^{(3)}=\max_{1\le m\le n-4}\gamma^*_{m,n}\),
  \[
  \Gamma_n^{(3)}
  ={2(\sqrt2-1)\over3}n^3+O(n^2),
  \qquad
  \lim_{n\to\infty}{\Gamma_n^{(3)}\over n^3}
  ={2(\sqrt2-1)\over3}.
  \]
  This preserves the one-tail coefficient only for the optimized three-tail
  obstruction. Although \(\Lambda_n\ge\Gamma_n^{(3)}\), it is not an
  asymptotic evaluation of \(\Lambda_n\) or \(R_2^*(n)\).
- DEFINITION / EXACT THEOREM (ARBITRARY NESTED-TAIL BLOCK): for
  \(2\le r\le n-2\), \(1\le m\le n-r-1\), put
  \(\ell=m+r-1\) and \(q=n-\ell+1\ge3\). Start with a simple cycle
  \(C_0\) on \(S_\ell\). For \(j=1,\ldots,r-1\), set
  \[
  z_j=\ell-j,
  \qquad
  e_j=\{u_j,v_j\}\in E(C_{j-1}),
  \qquad
  C_j=C_{j-1}\mathbin\oplus_{e_j}z_j,
  \]
  and
  \[
  A_j=z_j(u_j+v_j)-u_jv_j,
  \qquad
  H_0=0,
  \qquad
  H_j=\sum_{i=1}^jA_i.
  \]
  Deletion and reverse insertion are inverse bijections, and
  \[
  \gamma^{(r)}_{m,n}
  :=\min_\sigma\max_{0\le j\le r-1}P_\sigma(S_{m+j})
  =\min_{C_0,e_1,\ldots,e_{r-1}}
  \left[P(C_0)+\max_{0\le j\le r-1}H_j\right].
  \]
  The history count is
  \((q-1)!q(q+1)\cdots(q+r-2)/2=(q+r-2)!/2\), exactly the number of outer
  dihedral cycles. The specializations are
  \(\gamma^{(2)}_{m,n}=\beta_{m,n}\) and
  \(\gamma^{(3)}_{m,n}=\gamma^*_{m,n}\).
- EXACT THEOREM (GENERAL BLOCK COMPATIBILITY): every intermediate signature
  must be one connected loopless degree-two spanning cycle with no repeated
  unordered edge, and successive signatures must satisfy the literal split
  identities. Recursively nested child-edge splits are admissible. Starting
  from an edge \(\{\ell,\ell+1\}\) and repeatedly splitting
  \(\{t+1,t+2\}\) gives the exact domino corrections \(t^2-2\).
  Therefore the three-tail distinct-base-edge reduction cannot be assumed for
  general \(r\); it is impossible once \(r-1>q\).
- EXACT METHOD-SPECIFIC THEOREM: define
  \[
  E_{m,\ell}=\sum_{t=m}^{\ell-1}[t^2-2]_+.
  \]
  Then uniformly over the full domain,
  \[
  0\le\gamma^{(r)}_{m,n}-P^*_{\ell,n}
  \le E_{m,\ell}<(r-1)n^2,
  \]
  while the alternating-cycle excess \(g(q)\le q^2/8\) gives
  \[
  P_{\ell,n}\le\gamma^{(r)}_{m,n}
  \le P_{\ell,n}+g(q)+E_{m,\ell}
  <P_{\ell,n}+rn^2.
  \]
  For
  \(\Gamma_n^{(r)}=\max_m\gamma^{(r)}_{m,n}\), every fixed \(r\) has
  \[
  \Gamma_n^{(r)}
  ={2(\sqrt2-1)\over3}n^3+O_r(n^2),
  \]
  and every integer sequence \(r=r(n)=o(n)\) has
  \[
  \Gamma_n^{(r(n))}
  ={2(\sqrt2-1)\over3}n^3+O(r(n)n^2)
  ={2(\sqrt2-1)\over3}n^3+o(n^3).
  \]
  Linear \(r=\Theta(n)\) is the first scale not excluded by this error
  estimate. This is not proof of a changed coefficient, an asymptotic
  evaluation of \(\Lambda_n\), or a geometric asymptotic theorem.
- EXACT METHOD-SPECIFIC LOWER AUDIT: every tail index belongs to an admissible
  block, so for every allowed \(r\),
  \[
  \Gamma_n^{(r)}
  \ge\max_{1\le t\le n-2}P^*_{t,n}
  \ge\max_{1\le t\le n-2}P_{t,n}.
  \]
  Thus a linear block's truncated *inner-cycle reference* cannot be used to
  infer a drop below the one-tail coefficient. Also,
  \(\Gamma_n^{(r)}\) is a maximum of separately minimized one-block
  obstructions; no exchange of max and min is asserted.
- EXACT METHOD-SPECIFIC THEOREM (GENERAL LINEAR BLOCK): with \(m=1\),
  \(r_n=\lfloor\alpha n\rfloor\), \(s_n=\lceil\beta n\rceil\),
  \(S_n=n+r_n\), \(q_n=n-r_n+1\), and \(k_n=r_n-s_n\), the exact eventually
  proof-valid region is
  \[
  0<\alpha<1,
  \qquad 0<\beta<\alpha,
  \qquad 0\le\lambda\le1.
  \]
  At fixed \(n\), the complete conditions are
  \(2\le r_n\le n-2\) and \(1\le s_n\le r_n-1\). Define
  \[
  G_{n,\lambda}(t)
  ={\lambda(4S_nt-S_n^2-2\lambda t^2)\over2(2-\lambda)},
  \qquad
  J_{n,\lambda}(t)
  =\lambda((S_n-1)t-n(r_n-1)),
  \qquad
  F_n^{\mathrm{blk}}(\alpha,\beta,\lambda)
  =\min\{G_{n,\lambda}(s_n),J_{n,\lambda}(s_n)\}.
  \]
  Exact subtraction proves
  \[
  J_{n,\lambda}(t)-G_{n,\lambda}(t)
  ={\lambda\bigl((n-r_n)^2+4(n-t)
  +2\lambda(r_n-1-t)(n-t)\bigr)\over2(2-\lambda)}>0
  \]
  for \(\lambda>0\) and \(t\le r_n-1\), so the base floor is always active
  on the selected prefix; both floors vanish at \(\lambda=0\).
  If
  \[
  e(q)=
  \begin{cases}
  q(q-2)/8,&q\text{ even},\\
  (q^2-1)/8,&q\text{ odd},
  \end{cases}
  \]
  then, whenever \(s_n\le r_n-1\),
  \[
  \gamma^{(r_n)}_{1,n}
  \ge P_{r_n,n}+k_nF_n^{\mathrm{blk}}(\alpha,\beta,\lambda).
  \]
  Comparing separately with the exact inner simple-cycle minimum gives
  \[
  \gamma^{(r_n)}_{1,n}-P^*_{r_n,n}
  \ge
  k_nF_n^{\mathrm{blk}}(\alpha,\beta,\lambda)-e(q_n).
  \]
- EXACT THEOREM (BASE-SLACK IDENTITY): every simple cycle \(C\) on
  \(S_{r_n}\) satisfies
  \[
  P(C)-P_{r_n,n}
  =
  {1\over2}
  \sum_{\{u,v\}\in E(C)}
  (u+v-n-r_n)^2.
  \]
  On the selected prefix \(t=r_n-1,\ldots,s_n\), an intact base split can
  be charged against its unique edge slack and contributes at least
  \(G_{n,\lambda}(t)\); a recursive split contains a previously inserted
  endpoint and contributes at least \(J_{n,\lambda}(t)\). Both floors increase
  in \(t\), no base edge can be recreated, and
  \(\max\{0,H_{k_n}\}\ge\lambda H_{k_n}\). Thus the proof retains literal
  recursive compatibility and the maximum over all prefixes.
- EXACT TEMPLATE OPTIMIZATION (JOINT ONE-PREFIX LINEAR BLOCK): the limiting base and
  recursive floors are
  \[
  g(\alpha,\beta,\lambda)
  ={\lambda\left(4(1+\alpha)\beta-(1+\alpha)^2
  -2\lambda\beta^2\right)\over2(2-\lambda)},
  \qquad
  j(\alpha,\beta,\lambda)=\lambda((1+\alpha)\beta-\alpha),
  \]
  and
  \[
  j-g={\lambda\left((1-\alpha)^2
  +2\lambda(\alpha-\beta)(1-\beta)\right)\over2(2-\lambda)}>0.
  \]
  Thus the total pairing-plus-residual coefficient is
  \[
  \mathcal C(\alpha,\beta,\lambda)
  ={(1-\alpha)(\alpha^2+4\alpha+1)\over6}
  +(\alpha-\beta)g(\alpha,\beta,\lambda).
  \]
  The strictly positive-cubic region is exactly
  \[
  {1\over3}<\alpha<1,
  \quad {1+\alpha\over4}<\beta<\alpha,
  \quad 0<\lambda\le1,
  \quad
  2\lambda\beta^2<4(1+\alpha)\beta-(1+\alpha)^2.
  \]
  Complete exact boundary analysis proves the unique global maximizer
  \[
  \alpha_*=1-{\sqrt3\over3},
  \qquad
  \beta_*={5\over6}-{\sqrt3\over4},
  \qquad
  \lambda_*={88-32\sqrt3\over73}.
  \]
  It gives
  \[
  g_*={14-8\sqrt3\over9},
  \qquad
  c_{{\rm res},*}={26-15\sqrt3\over54},
  \qquad
  \mathcal C_*={4+2\sqrt3\over27}.
  \]
  The total coefficient is optimal only within the one-prefix specialization
  of CR28ax--CR28bg. The displayed
  residual coefficient is its contribution at that total-coefficient
  optimizer, not the separate maximum of \(c_{\rm res}\). Neither quantity
  is an exact residual or geometric leading coefficient.
- EXACT METHOD-SPECIFIC CUBIC RESIDUAL: put
  \(r_n^*=\lfloor\alpha_*n\rfloor\),
  \(s_n^*=\lceil\beta_*n\rceil\), and let \(F_n^*\) be the explicit optimized
  base floor. The exact floor/ceiling domain is uniformly \(n\ge86\). For
  \(n\ge90\),
  \[
  \gamma^{(r_n^*)}_{1,n}-P^*_{r_n^*,n}
  \ge
  c_{{\rm res},*}n^3-Q_*n^2,
  \]
  where
  \[
  c_{{\rm res},*}={26-15\sqrt3\over54}>0,
  \qquad
  Q_*={233-128\sqrt3\over72}.
  \]
  The displayed lower polynomial is positive for \(n\ge441\). Hence no
  compatible history for this selected block has \(o(n^3)\) excess. This
  proves no exact residual coefficient.
- EXACT GLOBAL LOWER COROLLARY (JOINTLY OPTIMIZED ONE-PREFIX LINEAR BLOCK): for each
  admissible
  \(m\), the pointwise inequality between the full subset maximum and the
  block maximum may first be minimized over \(\sigma\). Taking the maximum
  of the resulting separately proved lower bounds does not exchange max and
  min. Therefore, for every \(n\ge86\),
  \[
  \Lambda_n
  \ge\Gamma_n^{(r_n^*)}
  \ge\gamma^{(r_n^*)}_{1,n}
  \ge P_{r_n^*,n}+(r_n^*-s_n^*)F_n^*.
  \]
  Exact floor expansion and the residual contribution at the optimized
  triple prove
  \[
  \Lambda_n
  \ge {4+2\sqrt3\over27}n^3
  +{13\sqrt3-19\over9}n^2-2n-{1\over6}
  \ge {4+2\sqrt3\over27}n^3
  \qquad(n\ge90),
  \]
  and the strict global cyclic-ratio sandwich proves
  \[
  R_2^*(n)
  >{4+2\sqrt3\over27\pi}n^3-n^2.
  \]
  Hence the corresponding liminf lower coefficients are
  \((4+2\sqrt3)/27\) and that value divided by \(\pi\). These are
  certified lower coefficients, not exact leading coefficients; no limit,
  convergence, production, artifact, or certificate claim follows.
- EXACT METHOD-SPECIFIC THEOREM (TWO SELECTED PREFIXES): let
  \(0<\beta_2<\beta_1<\alpha<1\) and
  \(0\le\lambda_{\rm lo}\le\lambda_{\rm hi}\le1\). With the two selected
  prefix heights \(H_1,H_2\), the exact step
  \[
  \max(0,H_1,H_2)
  \ge(\lambda_{\rm hi}-\lambda_{\rm lo})H_1
    +\lambda_{\rm lo}H_2
  \]
  assigns weight \(\lambda_{\rm hi}\) to the first split segment and
  \(\lambda_{\rm lo}\) to the second. Combining the heights before charging
  gives one partition of the quadratic base-slack pool: every original edge
  is charged at most once, and every recursive current edge contains a
  previously inserted endpoint and retains the CR28ba floor. Therefore
  \[
  C_2=p(\alpha)
  +(\alpha-\beta_1)g(\alpha,\beta_1,\lambda_{\rm hi})
  +(\beta_1-\beta_2)g(\alpha,\beta_2,\lambda_{\rm lo}).
  \]
- EXACT TEMPLATE OPTIMIZATION (GLOBAL TWO-PREFIX CR28bw): for fixed
  densities the two weight summands are strictly concave. Their clipped
  individual optima are nondecreasing in the cutoff, so
  \(\beta_2<\beta_1\) automatically enforces
  \(\lambda_{\rm lo}\le\lambda_{\rm hi}\) and creates no pooled KKT branch.
  The six reduced branches are `00`, `M0`, `H0`, `MM`, `HM`, and `HH`.
  Their exact fixed-\(\alpha\) transition values are
  \[
  \alpha={1\over3},\qquad {77\over139},\qquad {301\over419}.
  \]
  Complete transition, compact-face, and collision analysis proves the
  unique global optimizer
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
  \right).
  \]
  The exact template-optimal coefficient is
  \[
  C_{2,*}
  ={491596+6578\sqrt{143}\over2061723}
  =0.276592655350947\ldots .
  \]
  It is the root satisfying
  \[
  {276592655350\over10^{12}}<C_{2,*}
  <{276592655352\over10^{12}}
  \]
  of \(6185169z^2-2949576z+342644\). The global proof uses the exact relaxation
  \[
  C_2\le
  p(\alpha)+{27(3\alpha-1)^3\over1058},
  \]
  whose unique equality point is the optimizer above.
- EXACT ASYMPTOTIC LOWER COROLLARY (GLOBAL TWO-PREFIX CR28bw):
  \[
  \liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{2,*},
  \qquad
  \liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{2,*}\over\pi}.
  \]
  No finite floor/ceiling theorem is currently proved for the irrational
  two-prefix optimizer.
- EXACT METHOD-SPECIFIC THEOREM (THREE SELECTED PREFIXES): let
  \(0<\beta_3<\beta_2<\beta_1<\alpha<1\) and
  \(0\le\lambda_3\le\lambda_2\le\lambda_1\le1\). Combining the three
  selected heights before assigning slack gives one weight on each disjoint
  split segment. A single partition of the quadratic base-slack pool charges
  every original edge at most once. Every recursive current edge retains a
  previously inserted endpoint, including fully nested histories crossing
  both segment boundaries. Therefore
  \[
  C_3=p(\alpha)
  +(\alpha-\beta_1)g(\alpha,\beta_1,\lambda_1)
  +(\beta_1-\beta_2)g(\alpha,\beta_2,\lambda_2)
  +(\beta_2-\beta_3)g(\alpha,\beta_3,\lambda_3).
  \]
- EXACT TEMPLATE OPTIMIZATION (GLOBAL THREE-PREFIX COMPACT CLOSURE): the
  three clipped individual weight optima are automatically ordered, so no
  pooled KKT branch occurs. The ten clipped regimes, all transition faces,
  density collisions, and weight faces are covered by the exact reduction.
  For \(A=3\alpha-1\) and \(X_i=4\beta_i-(1+\alpha)\), the normalized
  compact-simplex maximum is unique at
  \[
  \left({X_1\over A},{X_2\over A},{X_3\over A}\right)
  =
  \left({1058\over1263},{276\over421},{184\over421}\right).
  \]
  The remaining envelope has the unique global maximizing density
  \[
  \alpha_*={685623-421\sqrt{377823}\over993423},
  \]
  and all three densities and weights are strictly ordered in the middle
  clipped branch. The exact template-optimal coefficient is
  \[
  C_{3,*}
  ={753972193324+106042322\sqrt{377823}\over2960667770787}
  =0.276678647461945\ldots .
  \]
  It is the root in
  \[
  {276678647461\over10^{12}}
  <C_{3,*}
  <{276678647462\over10^{12}}
  \]
  of
  \(79938029811249z^2-40714498439496z+5145490327924\).
  Exact extension of the strict two-prefix optimizer by one active cutoff
  proves \(C_{3,*}>C_{2,*}\).
- EXACT ASYMPTOTIC LOWER COROLLARY (GLOBAL THREE-PREFIX TEMPLATE):
  \[
  \liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{3,*},
  \qquad
  \liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{3,*}\over\pi}.
  \]
  The coefficient is not an exact residual, limit, or geometric leading
  coefficient.
- EXACT FINITE METHOD-SPECIFIC THEOREM (IRRATIONAL THREE-PREFIX OPTIMIZER):
  put
  \[
  a=\alpha_*,\quad A=3a-1,
  \quad
  (x_1,x_2,x_3)
  =\left({1058\over1263},{276\over421},{184\over421}\right),
  \quad
  b_i={1+a+x_iA\over4}.
  \]
  Define
  \[
  r_n=\lfloor an\rfloor,
  \qquad
  s_{i,n}=\lceil b_i n\rceil,
  \qquad
  S_n=n+r_n,
  \qquad
  \widehat F_{i,n}={(4s_{i,n}-S_n)^2\over2}.
  \]
  The exact order, non-vacuity, block, and finite middle-clipped conditions
  hold uniformly from the minimal threshold \(n=159\). The failure at
  \(n=158\) is \((r_n,s_{1,n},s_{2,n},s_{3,n})=(67,67,64,62)\); exact
  arithmetic covers \(159\le n\le170\), and the symbolic tail begins at
  \(171\). Define
  \[
  \begin{aligned}
  \mathcal B_{3,n}={}&P_{r_n,n}
   +(r_n-s_{1,n})\widehat F_{1,n}\\
  &+(s_{1,n}-s_{2,n})\widehat F_{2,n}
   +(s_{2,n}-s_{3,n})\widehat F_{3,n},
  \end{aligned}
  \]
  and its integer closure
  \[
  \mathcal I_{3,n}=\lceil\mathcal B_{3,n}\rceil.
  \]
  Then the exact one-use charging theorem gives
  \[
  \Lambda_n\ge\mathcal I_{3,n}\ge\mathcal B_{3,n}>C_{3,*}n^3,
  \qquad
  R_2^*(n)>{\mathcal I_{3,n}\over\pi}-n^2
  \quad(n\ge159).
  \]
  More precisely,
  \[
  \mathcal B_{3,n}
  >C_{3,*}n^3+\kappa_*n^2-{a+5\over3}n-{1\over15},
  \]
  where
  \[
  \kappa_*
  ={-535396585939+1466777893\sqrt{377823}\over986889256929}
  >{1\over3}.
  \]
  The integer closure \(\mathcal I_{3,n}\) is the strongest explicit
  cutoff-only consequence of this rounded bound; \(\mathcal B_{3,n}\) is the
  literal charging expression. This theorem proves no exact residual,
  convergence, exact leading coefficient, production computation, or charging
  beyond three prefixes.
- EXACT METHOD-SPECIFIC THEOREM (FOUR SELECTED PREFIXES): let
  \[
  0<\beta_4<\beta_3<\beta_2<\beta_1<\alpha<1,
  \qquad
  0\le\lambda_4\le\lambda_3\le\lambda_2\le\lambda_1\le1.
  \]
  With \(r=\lfloor\alpha n\rfloor\), \(s_i=\lceil\beta_i n\rceil\), and
  \(s_0=r\), the five numbers
  \[
  1-\lambda_1,\quad\lambda_1-\lambda_2,\quad
  \lambda_2-\lambda_3,\quad\lambda_3-\lambda_4,\quad\lambda_4
  \]
  form the exact convex weight region for the four selected heights. Their
  linear form telescopes to weight \(\lambda_i\) on the disjoint segment
  \(\{s_i,\ldots,s_{i-1}-1\}\). Each literal history canonically partitions
  the original edges into injectively charged and unused edges. Immediately
  before inserting \(t\), every recursive edge contains an endpoint in
  \(\{t+1,\ldots,r-1\}\); splitting preserves this invariant through all
  three boundaries and at arbitrary nesting depth. Therefore, whenever the
  full finite admissibility conditions
  \[
  2\le r\le n-2,
  \qquad
  1\le s_4<s_3<s_2<s_1\le r-1
  \]
  hold,
  \[
  \begin{aligned}
  \gamma^{(r)}_{1,n}\ge{}& P_{r,n}
  +(r-s_1)F_{1,n}
  +(s_1-s_2)F_{2,n}\\
  &+(s_2-s_3)F_{3,n}
  +(s_3-s_4)F_{4,n},
  \qquad
  F_{i,n}=G_{n,\lambda_i}(s_i).
  \end{aligned}
  \]
  For fixed admissible real parameters,
  \[
  \begin{aligned}
  C_4={}&p(\alpha)
  +(\alpha-\beta_1)g(\alpha,\beta_1,\lambda_1)\\
  &+(\beta_1-\beta_2)g(\alpha,\beta_2,\lambda_2)\\
  &+(\beta_2-\beta_3)g(\alpha,\beta_3,\lambda_3)\\
  &+(\beta_3-\beta_4)g(\alpha,\beta_4,\lambda_4),
  \end{aligned}
  \]
  and
  \[
  \liminf{\Lambda_n\over n^3}\ge C_4,
  \qquad
  \liminf{R_2^*(n)\over n^3}\ge{C_4\over\pi}.
  \]
  The continuous parameter problem is globally optimized on the full compact
  ordered closure. The weights reduce to their clipped individual optima;
  there are exactly fifteen regimes \(H^hM^m0^{4-h-m}\). The fixed-\(\alpha\)
  winner moves through \(0000,MMMM,HMMM,HHMM,HHHM\), with the `HHHH`
  transition beyond \(\alpha=1\). Every transition, density collision, and
  compact facet is classified. The unique strict `MMMM` point has
  \[
  \alpha_*={18170840871749-3666143\sqrt{2903456040383}
   \over27631313622349},
  \]
  \[
  (x_1,x_2,x_3,x_4)
  ={(3190338,2672508,2091528,1394352)\over3666143},
  \]
  \[
  \beta_{i,*}={1+\alpha_*+x_i(3\alpha_*-1)\over4},
  \qquad
  \lambda_{i,*}={x_i(3\alpha_*-1)\over\beta_{i,*}},
  \]
  and exact coefficient
  \[
  C_{4,*}
  ={597580022071777213687318156
   +21288970076515705538\sqrt{2903456040383}
   \over2290468477489828247376833403}
  =0.276736149860989\ldots>C_{3,*}.
  \]
  Therefore
  \[
  \liminf{\Lambda_n\over n^3}\ge C_{4,*},
  \qquad
  \liminf{R_2^*(n)\over n^3}\ge{C_{4,*}\over\pi}.
  \]
  No finite rounding theorem or \(k\to\infty\) passage follows. This
  optimized four-prefix result does not itself supply the separate direct
  arbitrary finite-prefix theorem below.
- EXACT FINITE METHOD-SPECIFIC THEOREM (ARBITRARILY MANY FINITE SELECTED
  PREFIXES): fix any integer \(k\ge1\) and
  \[
  0<\beta_k<\cdots<\beta_1<\alpha<1,
  \qquad
  0\le\lambda_k\le\cdots\le\lambda_1\le1.
  \]
  With \(r=\lfloor\alpha n\rfloor\),
  \(s_i=\lceil\beta_i n\rceil\), \(s_0=r\), and
  \(\lambda_{k+1}=0\), the nonnegative convex coefficients
  \[
  1-\lambda_1,\quad
  \lambda_1-\lambda_2,\quad\ldots,\quad
  \lambda_{k-1}-\lambda_k,\quad\lambda_k
  \]
  combine \(0,H_1,\ldots,H_k\) before any edge slack is assigned and
  telescope to weight \(\lambda_i\) on the disjoint segment
  \(\{s_i,\ldots,s_{i-1}-1\}\). For every literal history, selected base
  splits inject into the original edge set, giving one canonical
  charged/unused slack partition. Descending induction on the inserted label
  shows that every recursive edge contains an endpoint in
  \(\{t+1,\ldots,r-1\}\). The induction contains no segment count and hence
  covers arbitrary nesting through any finite number of boundaries. Whenever
  \[
  2\le r\le n-2,
  \qquad
  1\le s_k<\cdots<s_1\le r-1,
  \]
  one has the exact finite inequality
  \[
  \gamma^{(r)}_{1,n}\ge
  P_{r,n}+\sum_{i=1}^k(s_{i-1}-s_i)G_{n,\lambda_i}(s_i).
  \]
  The cases \(k=1\) and \(k=5\) recover the one-prefix and former
  five-prefix statements. No positivity of the individual floors is
  required. The pointwise theorem gives no uniform threshold, rounding, or
  parameter control for \(k=k(n)\) and no \(k\to\infty\) passage. Its
  separate fixed-\(k\) instances combine with the normalized optimizer in the
  exact corollary below.
- EXACT METHOD-SPECIFIC ASYMPTOTIC COROLLARY (ALL FIXED \(k\)): set
  \[
  \alpha_\infty={13-2\sqrt2\over23}.
  \]
  For every fixed finite \(k\), let \(x^{(k)}\) be the unique normalized
  maximizer and define
  \[
  \beta_i={1+\alpha_\infty+(3\alpha_\infty-1)x_i^{(k)}\over4},
  \qquad
  \lambda_i={(3\alpha_\infty-1)x_i^{(k)}\over\beta_i}.
  \]
  The cutoffs and weights are strictly ordered and strictly all-middle. For
  each \(k\), a tuple-dependent threshold \(N_k\) permits the fixed-parameter
  charging limit
  \[
  L_\Lambda:=\liminf_{n\to\infty}{\Lambda_n\over n^3}
  \ge p(\alpha_\infty)
  +{(3\alpha_\infty-1)^3M_k\over8}.
  \]
  Taking the supremum of these scalar inequalities, after they have all been
  proved at fixed \(k\), gives
  \[
  \boxed{
  L_\Lambda\ge{434+4\sqrt2\over1587},
  \qquad
  \liminf_{n\to\infty}{R_2^*(n)\over n^3}
  \ge{434+4\sqrt2\over1587\pi}.
  }
  \]
  No \(k=k(n)\), uniform threshold, or interchange of limits is used. The
  separate full clipped arbitrary-\(k\) classification proves that the scalar
  coefficient is also the exact unattained supremum of the entire continuous
  finite-prefix template family and that every finite-\(k\) global maximizer
  is uniquely strict all-middle.
- EXACT METHOD-SPECIFIC THEOREM (GLOBALLY OPTIMIZED FIVE PREFIXES): the
  \(k=5\) coefficient on its full eleven-parameter compact closure clips
  coordinatewise to 21 ordered regimes \(H^hM^m0^z\). Every transition,
  density and weight collision, unused face, and compact boundary is
  classified. The unique point is strictly all-middle, with
  \[
  \alpha_{5,*}
  ={422413777961580309772684503
   -10047852311701\sqrt{183342238504950468196395903}
   \over661485317418210151348973103},
  \]
  the five exact pairs (CR28dz37)--(CR28dz38), and
  \[
  C_{5,*}
  ={346693217780244687187063490332457027500975566238012204
   +1228130489996268437333105902690103574002
    \sqrt{183342238504950468196395903}
   \over1312688475479610714750859896048564873968757997852345827}.
  \]
  Exact polynomial isolation and integer/squared-radical margins prove
  \[
  C_{5,*}>C_{5,\mathrm{rat}}>C_{4,*}.
  \]
  Therefore the liminf bounds hold with \(C_{5,*}\) and
  \(C_{5,*}/\pi\). There is no finite rounding theorem at the irrational
  optimizer and no growing-\(k\) passage. This is the exact optimum of the
  fixed \(k=5\) template only; it is strictly below the all-fixed-\(k\)
  coefficient above.
- EXACT METHOD-SPECIFIC ASYMPTOTIC COROLLARY (EXPLICIT FIVE-PREFIX WITNESS):
  let
  \[
  D=30143556935103,
  \]
  \[
  (N_1,\ldots,N_5)
  =(26881208992898,23392470652668,19595592993288,
  15335681473008,10223787648672).
  \]
  The exact fifth simplex point is \(x_i=N_i/D\), with
  \[
  M_5={722599396919860307414438404
   \over2725902074099388500860861827}.
  \]
  At \(\alpha=13/30\), put \(s=43/30\), \(A=3/10\), and
  \[
  \beta_i={s+Ax_i\over4},
  \qquad
  \lambda_i={Ax_i\over\beta_i}.
  \]
  Exact order and branch algebra gives
  \[
  0<\beta_5<\cdots<\beta_1<\alpha<1,
  \quad
  {s\over4}<\beta_i<{s\over3},
  \quad
  0<\lambda_5<\cdots<\lambda_1<1.
  \]
  Hence the fixed rational tuple is strictly all-middle and eventually
  integer-admissible. Its complete coefficient is
  \[
  C_{5,\mathrm{rat}}
  ={2263404122555368590593580404287
   \over8177706222298165502582585481000}.
  \]
  Exact positive integer margins prove
  \[
  C_{5,\mathrm{rat}}>{75\over271}>C_{4,*}.
  \]
  The fixed-parameter limit of the separate charging theorem and the existing
  additive cyclic-ratio relation give
  \[
  \liminf{\Lambda_n\over n^3}\ge C_{5,\mathrm{rat}},
  \qquad
  \liminf{R_2^*(n)\over n^3}\ge{C_{5,\mathrm{rat}}\over\pi}.
  \]
  The preceding theorem proves this rational specialization is strictly
  suboptimal. It remains the tuple with the exact finite theorem below.
- EXACT FINITE METHOD-SPECIFIC THEOREM (FIXED RATIONAL FIVE-PREFIX WITNESS):
  retain the preceding \(\alpha,x_i,\beta_i,\lambda_i\) and put
  \[
  r_n=\left\lfloor{13n\over30}\right\rfloor,
  \qquad
  s_{i,n}=\lceil\beta_i n\rceil,
  \qquad
  s_{0,n}=r_n,
  \qquad
  S_n=n+r_n.
  \]
  The minimal uniform threshold for complete block admissibility, strict
  cutoff order, five nonempty segments, and
  \(S_n/4<s_{i,n}<S_n/3\) is \(234\). At \(n=233\),
  \((r_n,s_{1,n})=(100,100)\), so the first segment is empty. Keep the
  fixed-weight floors
  \[
  F_{i,n}=G_{n,\lambda_i}(s_{i,n})
  ={\lambda_i(4S_ns_{i,n}-S_n^2-2\lambda_i s_{i,n}^2)
   \over2(2-\lambda_i)}
  \]
  and define
  \[
  \mathcal B_{5,n}
  =P_{r_n,n}+\sum_{i=1}^5(s_{i-1,n}-s_{i,n})F_{i,n},
  \qquad
  \mathcal I_{5,n}=\lceil\mathcal B_{5,n}\rceil.
  \]
  Exact floor/ceiling-error algebra gives
  \[
  \mathcal B_{5,n}-C_{5,\mathrm{rat}}n^3
  >{13\over30}n^2-{25\over2}n-{109\over6}>0
  \qquad(n\ge234),
  \]
  and therefore
  \[
  \Lambda_n\ge\mathcal I_{5,n}\ge\mathcal B_{5,n}
  >C_{5,\mathrm{rat}}n^3,
  \qquad
  R_2^*(n)>{\mathcal I_{5,n}\over\pi}-n^2
  \quad(n\ge234).
  \]
  The middle inequalities classify the rounded cutoffs; the fixed weights are
  not finite reoptimized clipped weights. The exact remainder concerns the
  literal lower bound, not the unknown true block residual.
- VERIFIED FACT (FINITE EXACT FOUR-PREFIX DOSSIER ORACLE): the standalone
  ops/TASK-20260716__four_prefix_charging/literal_oracle.py imports no
  production or test helper and exhausts all 840 current-edge histories from
  \(C_0=(11,14,12,13)\) for insertions \(10,9,8,7\). All 840 final cycles
  are distinct. Recursive search-tree splits by depth are
  \((0,8,72,600)\), including 120 fourth splits with two previously inserted
  endpoints. Every history
  satisfies the convex telescoping identity, exact canonical slack partition,
  recursive floor, and four-segment bound. This bounded result corroborates
  but does not replace the proof.
- VERIFIED FACT (FINITE EXACT FIVE-PREFIX DOSSIER ORACLE): the standalone
  `ops/TASK-20260717__five_prefix_charging/literal_oracle.py` imports only
  `collections.Counter` and `fractions.Fraction`. From the five-edge base
  \(C_0=(13,17,14,16,15)\), it exhausts all 15,120 five-split histories for
  insertions \(12,11,10,9,8\), with 15,120 distinct final cycles. The
  base/recursive split counts are
  \((5,20,100,600,4200)\) and
  \((0,10,110,1080,10920)\); 2,520 fifth splits have two previously inserted
  endpoints, and 120 histories charge five distinct original edges. Every
  linkage, convex-height identity, canonical one-use partition, recursive
  invariant, exact local floor, and five-segment inequality passes. This
  bounded computation corroborates but does not prove the all-history theorem.
- VERIFIED FACT (FINITE EXACT SIX-PREFIX DOSSIER ORACLE): the sole new
  dossier-local script uses standard-library exact arithmetic and exhausts
  all 332,640 six-split histories from
  \(C_0=(15,20,16,19,17,18)\), with cutoffs
  \((14,13,12,11,10,9)\) and weights
  \((6/7,5/7,4/7,3/7,2/7,1/7)\). The base/recursive split counts are
  \((6,30,180,1260,10080,90720)\) and
  \((0,12,156,1764,20160,241920)\); 720 histories charge all six original
  edges and 60,480 sixth splits join two inserted labels. Every indexed
  convex, partition, invariant, local-floor, and finite-bound assertion
  passes. This bounded corroboration changes no production enumeration and
  does not prove arbitrary finite \(k\).
- VERIFIED FACT (INDEPENDENT EXACT FOUR-PREFIX OPTIMIZATION DIAGNOSTIC): the
  standalone standard-library script at
  ops/TASK-20260717__global_four_prefix_optimization/exact_diagnostic.py
  verifies exact clipping-gap factorizations on rational grids, both \(C^1\)
  joins, all fifteen regimes, exact transition weights and collision
  reductions, the specialized \(k=4\) simplex certificate, the end-to-end
  original objective at the quadratic-surd optimizer, its primitive
  irreducible polynomial and isolating interval, and the exact separator
  \(C_{3,*}<2767/10000<C_{4,*}\). It imports no project, production, or test
  helper and corroborates rather than replaces the all-real proof.
- VERIFIED FACT (INDEPENDENT EXACT FIVE-PREFIX RATIONAL DIAGNOSTIC): the
  standalone script at
  ops/TASK-20260717__five_prefix_explicit_asymptotic_witness/fraction_diagnostic.py
  imports only fractions.Fraction. It checks the fifth scalar and ratio
  recurrences, direct simplex objective, all stationarity equations, every
  reduced \(\beta_i,\lambda_i\), strict all-middle admissibility, equality of
  the direct and normalized coefficient evaluations, and both positive exact
  comparison margins. It corroborates rather than replaces the written
  derivation.
- VERIFIED FACT (INDEPENDENT GLOBAL FIVE-PREFIX OPTIMIZATION DIAGNOSTIC):
  the standalone standard-library script at
  ops/TASK-20260717__global_five_prefix_optimization/exact_diagnostic.py
  checks all 21 clipped words, five transition rows, collision identities,
  primitive optimizer and coefficient polynomials, rational isolating
  intervals, strict all-middle inequalities, end-to-end coefficient
  identities, and every exact comparison margin. It imports no project,
  production, test, artifact, backend, certificate, or enumeration helper.
- VERIFIED FACT (FINITE EXACT FIVE-PREFIX FLOOR/CEILING DIAGNOSTIC): the
  standalone script at
  `ops/TASK-20260717__five_prefix_finite_theorem/exact_diagnostic.py` imports
  only `fractions.Fraction`. It checks exact rows \(233\) through \(246\),
  every predicate's last boundary failure, the symbolic-tail margins,
  fixed-weight local-floor expansion, integer closure, simplex-stationarity
  cancellation, exact remainder, and uniform sign. It corroborates but does
  not replace the written finite bridge and symbolic tail.
- EXACT THEOREM (NORMALIZED PREFIX SIMPLEX): for every fixed \(k\ge1\), put
  \[
  F_k(x_1,\ldots,x_k)
  =\sum_{i=1}^k(x_{i-1}-x_i)x_i^2,
  \qquad x_0=1,
  \]
  and
  \[
  M_k=\max_{1\ge x_1\ge\cdots\ge x_k\ge0}F_k(x_1,\ldots,x_k),
  \qquad M_0=0.
  \]
  The maximum exists and its unique maximizer satisfies
  \(1>x_1>\cdots>x_k>0\). Defining
  \[
  q_k={2\over3(1-M_{k-1})},
  \]
  gives the exact value and forward-ratio recurrences
  \[
  M_k={q_k^2\over3}
  ={4\over27(1-M_{k-1})^2},
  \qquad
  q_1={2\over3},
  \qquad
  q_{m+1}={2\over3-q_m^2}.
  \]
  At the maximizer,
  \[
  r_i={x_i\over x_{i-1}}=q_{k-i+1},
  \qquad
  r_k={2\over3},
  \qquad
  r_i={2\over3-r_{i+1}^2}.
  \]
  The sequence \(M_k\) is strictly increasing and
  \(M_k\nearrow1/3\).
- VERIFIED FACT (EXACT SOURCE AGREEMENT): the normalized theorem recovers
  \[
  \begin{array}{c|c|c|c}
  k&(x_1,\ldots,x_k)&M_k&M_k/8\\ \hline
  1&(2/3)&4/27&1/54\\
  2&(18/23,12/23)&108/529&27/1058\\
  3&(1058/1263,276/421,184/421)&1119364/4785507&279841/9571014\\
  4&(3190338,2672508,2091528,1394352)/3666143
    &3392752184748/13440604496449&848188046187/26881208992898\\
  5&(26881208992898,23392470652668,19595592993288,
     15335681473008,10223787648672)/30143556935103
    &722599396919860307414438404/2725902074099388500860861827
    &180649849229965076853609601/5451804148198777001721723654
  \end{array}
  \]
  exactly. The first five are the optimized one- through five-prefix simplex
  points; the fifth is also the rational simplex point used in the explicit
  witness above.
- EXACT NORMALIZED-ENVELOPE CLASSIFICATION: with
  \[
  p(\alpha)={(1-\alpha)(\alpha^2+4\alpha+1)\over6},
  \qquad
  E_k(\alpha)=p(\alpha)+{M_k\over8}(3\alpha-1)^3,
  \]
  one has uniform monotone convergence on \([1/3,1]\) to
  \[
  E_\infty(\alpha)
  =p(\alpha)+{(3\alpha-1)^3\over24}.
  \]
  The formal normalized-polynomial envelope has the unique maximum
  \(E_\infty(1)=1/3\); on \([1/3,1)\) that value is only a nonattained
  supremum. The limiting all-middle closure is \([1/3,1/2]\), where the
  unique maximum is
  \[
  \alpha_{\rm mid}={13-2\sqrt2\over23},
  \qquad
  E_\infty(\alpha_{\rm mid})={434+4\sqrt2\over1587}.
  \]
- EXACT GLOBAL CLIPPED FINITE-PREFIX CLASSIFICATION: for the complete compact
  continuous \(k\)-prefix template, coordinatewise weight clipping is exact
  and leaves \((k+1)(k+2)/2\) ordered regimes \(H^hM^m0^z\). With \(\phi\)
  from (CR28dw15), the exact compact envelope is
  \[
  \mathscr H_k(\alpha)
  =p(\alpha)+(1+\alpha)^3V_k\!\left({\alpha\over1+\alpha}\right),
  \quad
  V_m(t)=\max_{0\le x\le t}
  \bigl((t-x)\phi(x)+V_{m-1}(x)\bigr).
  \]
  These Bellman values are finite lower Darboux sums. Their monotone uniform
  limit gives the exact three-piece clipped envelope (CR28dw20). Its outer
  density pieces are strictly below a feasible one-prefix value, so for every
  finite \(k\) the unique global compact maximizer is strict all-middle,
  with density and tuple (CR28dw24)--(CR28dw25). Its value satisfies
  \[
  C_{k,*}\nearrow{434+4\sqrt2\over1587}=C_{\mathrm{AF}}.
  \]
  Hence \(C_{\mathrm{AF}}\) is the exact unattained supremum of the entire
  continuous finite-prefix family. The formal value \(E_\infty(1)=1/3\) is
  not a clipped-family coefficient.
- EXACT METHOD-SPECIFIC LIMITATION (TWO CONTIGUOUS BLOCKS): split the
  insertion labels at a density \(\eta\) into two disjoint contiguous blocks.
  Mixing the upper absolute-prefix maximum with the lower maximum anchored at
  the separator by \(h\in[0,1]\) forces effective weights
  \[
  \lambda_i^+=h+(1-h)a_i,\qquad \lambda_j^-=hb_j,
  \]
  and therefore
  \[
  1\ge\lambda_1^+\ge\cdots\ge\lambda_{k_+}^+
  \ge h\ge\lambda_1^-\ge\cdots\ge\lambda_{k_-}^-\ge0.
  \]
  Original edges first split above and below the separator form two
  history-relative disjoint slack pools; a split edge is never recreated,
  and the global recursive child-edge invariant crosses the separator.
  The exact finite inequality is (CR28dw34), and the normalized objective is
  (CR28dw35). Concatenation identifies every valid two-block tuple with one
  \(K=k_++k_-\) finite-prefix tuple, while (CR28dw36) gives the converse on
  the strict density domain and identifies the full compact closures by
  continuity. Hence
  \[
  \max C^{\mathrm{2B}}_{k_+,k_-}=C_{K,*}<C_{\mathrm{AF}},
  \qquad
  \sup_{k_+,k_-\ge1}C^{\mathrm{2B}}_{k_+,k_-}=C_{\mathrm{AF}}.
  \]
  Thus this ansatz has no rational witness strictly above
  \(C_{\mathrm{AF}}\); this is not an upper bound on \(\Lambda_n\).
- EXACT METHOD-SPECIFIC LIMITATION (ONE-PREFIX BASE CAPACITY): the coarsest
  nonconstant filter in the declared one-prefix class retains the existing
  base/recursive dichotomy and records its capacity count: the \(r-s\)
  selected splits can use at most \(n-r+1\) original base edges.
  Hence at least \([2r-s-n-1]_+\) selected splits receive the stronger
  recursive floor.  The exact all-order inequality is (CR28dw41), and its
  normalized compact objective is (CR28dw43).  The positive-part collision
  is \(\beta=2\alpha-1\).  Exact optimization of both closed sides and all
  boundary faces gives
  \[
  \max C^{\mathrm{cap}}={4+2\sqrt3\over27}
  <{434+4\sqrt2\over1587}=C_{\mathrm{AF}}.
  \]
  The active-side compact closure has exact maximum \(13/48\), uniquely at
  its filter-off hinge \((\alpha,\beta,\lambda)=(1/2,0,0)\); the unique
  global optimizer is the old inactive one-prefix point.  Thus the filter is
  strictly stronger when \(2\alpha-\beta-1>0\) and \(\lambda>0\), but cannot
  improve the current coefficient.  This is a no-go for the declared binary
  capacity-filter class only, not an upper bound on \(\Lambda_n\) or a claim
  about arbitrary structural filters.
- EXACT METHOD-SPECIFIC LIMITATION (ONE-PREFIX LABEL-AWARE CAPACITY): retain
  the individual selected-label floors in the preceding binary filter.
  With \(\Delta(t)=J(t)-G(t)\), (CR28dw50) proves that \(\Delta\) decreases
  with \(t\).  Therefore the strongest bound implied by the capacity
  cardinality alone is
  \(P_{r,n}+\sum_{t=s}^{r-1}G(t)+\sum_{t=r-\nu}^{r-1}\Delta(t)\).
  Literal histories give the stronger shifted block
  \(\sum_{t=r-\nu-1}^{r-2}\Delta(t)\), because the first selected split is
  necessarily base; every other admissible binary type word is realizable.
  Their finite difference is \(O(n^2)\), so both have the exact common cubic
  objective (CR28dw57).  Its active compact side has maximum \(13/48\), and
  its unique global maximizer is inactive with
  \[
  0.2768854<C_{\rm LA,*}<0.2768855,\qquad
  (\alpha_*,\beta_*,\lambda_*)
  \in(0.4365889,0.4365890)\times(0.3850802,0.3850803)
     \times(0.5024738,0.5024739).
  \]
  Exact Sturm and Bernstein certificates prove
  \[
  {4+2\sqrt3\over27}<C_{\rm LA,*}
  <{434+4\sqrt2\over1587}=C_{\rm AF}.
  \]
  Hence label awareness strictly improves the old one-prefix compact
  coefficient but cannot exceed \(C_{\rm AF}\); the capacity advantage is
  off at the optimizer.  This is a limitation only of the declared floor
  model, not an upper bound on \(\Lambda_n\), a geometric conclusion, or a
  classification of richer filters.  See
  [the authoritative proof](research/FIXED_ORDER_CYCLE_RATIO.md#one-prefix-label-aware-base-capacity).
- EXACT METHOD-SPECIFIC NO-GO (TWO-PREFIX LABEL-AWARE NESTED CAPACITY):
  retain simultaneously the upper-prefix capacity
  \(|\mathcal R_1|\ge\nu_1\) and total-prefix capacity
  \(|\mathcal R_1|+|\mathcal R_2|\ge\nu_2\) in the accepted \(k=2\)
  height telescope.  One common history-relative original-edge partition
  proves (CR28dw72), so no slack is reset or double charged at the inner
  cutoff.  The exact finite allocation over \(q=|\mathcal R_1|\) has
  increasing quadratic first difference (CR28dw73); its discriminant
  includes lower/upper endpoint minima, an interior minimum, equal-weight
  linear degeneration, and adjacent ties.  The normalized objective
  (CR28dw75) is continuous on
  \[
  \{0\le c\le b\le a\le1,\ 0\le v\le u\le1\},
  \]
  with both positive-part hinges, all cutoff collisions, all weight faces,
  and allocation collisions included.  The raw active closure is strictly
  below \(69/250\).  On the inactive closure, comparison with the exact
  clipped arbitrary-prefix envelope is strict at \(C_{\rm AF}\), because
  two constant weights cannot equal its strictly varying pointwise optimizer.
  The rational inactive witness
  \[
  (a,b,c,u,v)
  =\left({11\over25},{49\over120},{47\over125},
          {3\over5},{1\over3}\right)
  \]
  has value \(588926561981/2126250000000>2769/10000\).  Therefore
  \[
  C_{\rm LA,*}
  <{2769\over10000}
  <C_{\rm 2LA,*}
  <{434+4\sqrt2\over1587}=C_{\rm AF}.
  \]
  This is an exact strict improvement over the one-prefix floor model and an
  exact no-go against the arbitrary-finite-prefix coefficient, not an upper
  bound on \(\Lambda_n\), a geometric claim, or a concatenation of two reset
  blocks.  See
  [the authoritative proof](research/FIXED_ORDER_CYCLE_RATIO.md#two-prefix-label-aware-nested-capacity).
- LIMITATION AND COROLLARY: the \(M_k,E_k\) statements are exact
  normalized-polynomial theorems, and \(\mathscr H_k\) is the separate full
  clipped continuous classification. Both are independent of the charging
  argument. A third direct proof establishes charging for every finite
  admissible \(k\). None supplies uniform control for growing \(k=k(n)\) or
  an interchange of limits. Those are unnecessary for the all-fixed-\(k\)
  corollary: at the strict all-middle density \(\alpha_\infty\), apply the
  normalized and charging theorems separately at each fixed \(k\), then take
  the supremum of the resulting scalar liminf inequalities to obtain
  \((434+4\sqrt2)/1587\) and its geometric value divided by \(\pi\).
- EXACT GLOBAL LOWER COROLLARY (TWO-PREFIX RATIONAL WITNESS): at
  \[
  (\alpha,\beta_1,\beta_2,\lambda_{\rm hi},\lambda_{\rm lo})
  =(3/7,2/5,3/8,1/2,1/4),
  \]
  \[
  p={284\over1029},\qquad
  g_{\rm hi}={52\over3675},\qquad
  g_{\rm lo}={199\over87808},
  \]
  and
  \[
  C_2={72825421\over263424000}>{4+2\sqrt3\over27}.
  \]
  With \(r_n=\lfloor3n/7\rfloor\),
  \(s_{1,n}=\lceil2n/5\rceil\), and
  \(s_{2,n}=\lceil3n/8\rceil\), the minimal uniform two-nonempty-prefix
  threshold is \(n=59\); \(n=58\) has \(r_n=s_{1,n}=24\). Exact rounding
  proves
  \[
  \Lambda_n
  \ge C_2n^3+{106196857\over263424000}n^2
       -{1520\over1029}n-{22\over343}
  \ge C_2n^3
  \quad(n\ge59),
  \]
  \[
  R_2^*(n)>{C_2\over\pi}n^3-n^2
  \quad(n\ge59).
  \]
  The separate residual lower polynomial is positive for \(n\ge327\).
  This remains the earlier exact rational two-prefix specialization. It is
  below \(C_{2,*}<C_{3,*}\); the rounded three-prefix theorem is stronger
  from \(n=159\). No exact residual, convergence, exact leading coefficient,
  production, artifact, or certificate claim follows.
- EXACT GEOMETRIC COROLLARY: the strict global cyclic-ratio sandwich gives
  \[
  R_2^*(n)>{\beta_n^{(2)}\over\pi}-n^2
  \qquad(n\ge4).
  \]
  This is a finite refinement with the same leading geometric coefficient
  \(2(\sqrt2-1)/(3\pi)\), not a new asymptotic constant.
- VERIFIED FACT (FINITE EXACT TEST-ONLY CHECK): independent helpers enumerate
  all distinct duplicated-label pairing signatures and all dihedral simple
  cycles for tail sizes three through six. They recover total signature
  counts `(5,17,73,388)`, simple-cycle counts `(1,3,12,60)`, and exact
  \((P_{m+1,n},\min P(C),\beta_{m,n})\) rows
  `(25,26,26)`, `(76,77,77)`, `(170,172,172)`, and `(320,322,323)` for
  `(m,n)=(1,4),(2,6),(3,8),(4,10)`. A separate exact check verifies the
  alternating-cycle excess formula. These tests call no production scorer,
  canonicalizer, or enumerator and are not the all-`n` proof.
- VERIFIED FACT (FINITE EXACT TEST-ONLY CHECK): compatible double insertion
  is checked literally on small tails. At \((m,n)=(2,7)\), the 60 triples
  (base cycle, first edge, second edge) give exactly all 60 dihedral cycles
  on \(S_2\), split into 24 nested, 24 distinct-incident, and 12
  distinct-disjoint interactions. Exact rows
  \((P_{m+2,n},P^*_{m+2,n},\gamma^*_{m,n})\) are
  \((46,47,47)\), \((116,117,118)\), \((235,237,239)\), and
  \((320,322,323)\) for
  \((m,n)=(1,5),(2,7),(3,9),(3,10)\). A separate exact grid checks the
  alternating-cycle quadratic squeeze. The new paths call no production
  scorer, canonicalizer, or enumerator and are not the all-\(n\) proof.
- VERIFIED FACT (FINITE EXACT TEST-ONLY CHECK): a recursive general-block
  oracle specializes correctly to \(r=2,3\) and checks \(r=4\) at three
  bounded rows. At \((m,n,r)=(2,7,4)\), all 60 compatible histories agree
  signature by signature with all 60 direct outer cycles and
  \[
  (P_{5,7},P^*_{5,7},\gamma^{(4)}_{2,7})=(106,107,118).
  \]
  At \((2,8,4)\), three base classes expand to all 360 outer classes and
  give \((164,165,172)\). The oracle audits every prefix, edge-set linkage,
  and intermediate connected cycle; a separate exact check realizes the
  admissible-domino envelope \(E_{2,5}=23\). All paths are test-local and
  call no production scorer, canonicalizer, or enumerator.
- VERIFIED FACT (BOUNDED EXACT TEST-LOCAL DIAGNOSTIC): the jointly optimized
  linear-block
  checks verify the base-slack identity on every dihedral cycle of tail sizes
  three through six. At \(n=86,90,141,200,500,1000\), two deterministic history
  policies exercise intact-base and recursive child-edge splits and verify
  exact floor/ceiling rounding, one-use base linkage, every local floor, the
  weighted-prefix step, and the finite lower inequality. At \(n=141\), a
  separate oracle checks all 6,972 depth-two literal histories from one base,
  including all 166 recursive second splits. An exact bounded scan covers
  every \(86\le n\le1000\). The checks use integer, rational, and test-local
  \(\mathbb Q(\sqrt3)\) coefficient-pair arithmetic and call no production
  scorer, canonicalizer, or enumerator. They also verify the stationary
  branch identities, candidate equations, a bounded rational grid, finite
  constants, and decisive signs without floating point. They corroborate the
  algebra but are not the all-\(n\) proof.
- VERIFIED FACT (BOUNDED EXACT TEST-LOCAL DIAGNOSTIC): rational two-prefix
  checks exhaust all 1,260 literal depth-two histories from one \(n=59\)
  base, including all 70 recursive second splits. A separate \(n=100\)
  domino crosses the high/low boundary and splits edges whose two endpoints
  were inserted earlier. Deterministic base/recursive policies at four sizes,
  an explicit invalid double-charge regression, exact coefficient and surd
  arithmetic, and a \(59\le n\le1000\) rounding scan all pass without using
  production scorers, canonicalizers, or enumerators. These computations
  corroborate the proof but do not replace it.
- VERIFIED FACT (BOUNDED EXACT TEST-LOCAL DIAGNOSTIC): independent
  \(\mathbb Q(\sqrt{143})\) arithmetic verifies every optimizer coordinate,
  all five coordinate minimal polynomials, the coefficient polynomial
  \(6185169z^2-2949576z+342644\), exact rational isolating intervals, and
  the strict parameter order. A separate rational oracle checks the ordered
  weight reduction and all six branches, the exact fixed-\(\alpha\) transitions
  at \(77/139\) and \(301/419\), the unique simplex maximum
  \((18/23,12/23)\), and every point of a denominator-32 compact-closure
  grid. These checks use no production scorer, canonicalizer, enumerator,
  floating-point premise, or enumeration-limit change.
- VERIFIED FACT (BOUNDED EXACT TEST-LOCAL DIAGNOSTIC): a test-local rational
  oracle exhausts all \(35\cdot36\cdot37=46{,}620\) literal depth-three
  histories from one \(n=59\) base cycle, including 70 distinct recursive
  second-step prefixes (2,590 full-history occurrences), 4,970 recursive
  third splits, and 70 fully nested third splits of
  the edge formed by the two earlier labels. It verifies one-use slack,
  literal linkage, every local floor, the combined weighted identity, and
  the selected-prefix maximum. Separate exact grids check the ordered-weight
  reduction, all ten clipped regimes, the compact closure, and the unique
  simplex factorization. Test-local \(\mathbb Q(\sqrt{377823})\) arithmetic
  verifies the optimizer, strict domain, coefficient polynomial, rational
  isolation, and \(C_{3,*}>C_{2,*}\). These paths use no production scorer,
  canonicalizer, enumerator, floating-point premise, or limit change.
- VERIFIED FACT (FINITE EXACT DOSSIER DIAGNOSTIC):
  `ops/TASK-20260716__three_prefix_finite_theorem/exact_diagnostic.py`
  imports no project or test helper and implements
  \(\mathbb Q(\sqrt{377823})\), exact signs, and exact surd floor/ceil
  independently. It reconstructs the optimizer and coefficient, scans
  \(1\le n\le170\), checks the boundary rows \(158,159,170,171\), verifies
  the symbolic segment thresholds \((171,77,64)\) and symbolic upper-clip
  estimate threshold \(23\), and checks the literal and polynomial theorem
  through \(n=1000\).
  This bounded exact computation corroborates the arithmetic; the written
  finite table and symbolic tail prove the uniform all-\(n\ge159\) theorem.
- VERIFIED FACT (FINITE EXACT DOSSIER DIAGNOSTIC): the standalone
  `ops/TASK-20260716__normalized_prefix_simplex/fraction_diagnostic.py` uses
  only integer and `Fraction` arithmetic. For \(k=1,\ldots,8\), it checks the
  scalar and ratio recurrences, direct objective values, all stationarity
  equations, strict feasibility, monotonicity, and the exact \(k=1,2,3,4\)
  rows. Literal denominator-12 enumeration and an independent discrete
  Bellman calculation agree over 203,489 grid tuples, and no grid value
  exceeds its exact \(M_k\). This bounded computation corroborates but does
  not replace the all-real proof.
- EXACT THEOREM: the additive relation transfers normalized asymptotics:
  \(\Lambda_n=\pi R_2^*(n)+O(n^2)=\Theta(n^3)\),
  \(\Lambda_n/(\pi R_2^*(n))\to1\), and
  \[
  {434+4\sqrt2\over1587}
  \le\liminf{\Lambda_n\over n^3}
  \le\limsup{\Lambda_n\over n^3}
  \le{857\over3000}.
  \]
  This proves neither convergence nor an exact leading constant.
- EXACT THEOREM / DISTINCTION: \(\Lambda\) is natively a complete-order
  directed-cycle objective, while repository \(W\) is a core-order
  single-pair objective for equal regular directions. Elimination factors
  \(\Lambda\) through the full core order via \(K\), but \(K\ne W\) in
  general. Only the one-sided comparison
  \(\Lambda_n\le(n-1)W_n\) is proved; equality and equality of minimizing
  order sets are not claimed.
- EXACT THEOREM (CANONICAL EIGHT-TWENTY-FIFTHS \(K\)): let \(\tau_n\) be the
  core order returned by `eight_twenty_fifths_order(n)`. On the symbolic
  domain write
  \[
  d=4v+e,\qquad n=5v+e-1,\qquad 4\le e\le8,
  \]
  and put \(L=2v+1\). The unique maximizing subset is
  \[
  U_n^*=
  \begin{cases}
  \{L,\ldots,n\},&e=4,5,\\
  \{L,\ldots,n\}\setminus\{L+1\},&e=6,7,8.
  \end{cases}
  \]
  With
  \(t=\lfloor(v+e-2)/2\rfloor\),
  \(\varepsilon=v+e-2-2t\), and
  \(\chi=\mathbf1_{\{v=e-2\}}\), define
  \[
  \begin{aligned}
  \mathcal Q(v,e,\varepsilon)={1\over8}\bigg[{}
  &286v^3+(180e-91+10\varepsilon)v^2\\
  &+(38e^2-34e-2-8(e+2)\varepsilon)v\\
  &+{e(8e^2-9e-2)\over3}
   +(-2e^2-10e+21)\varepsilon\bigg],\\
  \Gamma(v,e)&=(4e-22)v+e^2-7e+8.
  \end{aligned}
  \]
  Then
  \[
  K(\tau_n)=\mathcal Q(v,e,\varepsilon)
  -(4e-7)\chi+\max\{0,\Gamma(v,e)\}.
  \]
  The fourteen nonsymbolic public rows also have unique maximizing tails:
  \[
  \begin{array}{c|rrrrrrrrrrrrrr}
  n&9&10&11&12&14&15&16&17&20&21&22&26&27&32\\
  m&4&4&5&5&6&6&7&7&9&9&9&10&11&13\\
  K&256&346&459&593&917&1125&1346&1609&2554&2976&3431&5516&6204&10299
  \end{array}
  \]
  where the maximizer is \(\{m,\ldots,n\}\). The proof is an exact
  shortcut-budget/backbone argument, not finite subset enumeration.
- EXACT ASYMPTOTIC CONSEQUENCE:
  \[
  K(\tau_n)={143\over500}n^3+O(n^2),
  \qquad {143\over500}={8\over25}-{17\over500}.
  \]
  Any insertion of label \(1\) has
  \(\Lambda(\sigma_{n,g})=K(\tau_n)\) and fixed-order threshold
  \[
  {K(\tau_n)\over\pi}-n^2
  <\rho_{\sigma_{n,g}}<{K(\tau_n)\over\pi}.
  \]
  Globally, only \(\Lambda_n\le K(\tau_n)\) and
  \(R_2^*(n)<\Lambda_n/\pi\le K(\tau_n)/\pi\) follow. This historically
  gave
  \[
  {434+4\sqrt2\over1587}
  \le\liminf{\Lambda_n\over n^3}
  \le\limsup{\Lambda_n\over n^3}
  \le{143\over500},
  \]
  with the same bracket divided by \(\pi\) for \(R_2^*(n)/n^3\). The later
  KR1 monotone cancellation lift supersedes the two upper endpoints by
  \(857/3000\) and \(857/(3000\pi)\). No convergence, exact leading
  constant, or global minimizing-order theorem is proved.
- VERIFIED FACT (BOUNDED EXACT DOSSIER DIAGNOSTIC): the standalone
  `ops/TASK-20260718__canonical_eight_twenty_fifths_k/exact_diagnostic.py`
  reconstructs the block order without production imports, checks
  \(9\le n\le120\) by an increasing-path max-plus dynamic program, and
  audits every oriented shortcut budget; it also compares the direct block
  score with the formula through \(n=1000\). It checks 8,495,284 DP
  transitions and 561,568 oriented arcs, obtains one optimizer on all 112
  full-certificate rows, and uses neither subset nor permutation enumeration.
  This corroborates but does not replace the symbolic proof.
- EXACT THEOREM (EXACT-THRESHOLD RESIDUE-ONE \(K\)): let
  \(\tau_n^{(1)}\) be the core order returned by
  `residue_one_product_distance_order(n)` for \(n=5k+1\), \(k\ge2\), and
  put \(\varepsilon=k\bmod2\). Its unique maximizing subset is
  \[
  \{2k+1,2k+2,\ldots,5k+1\},
  \]
  and
  \[
  K(\tau_n^{(1)})
  ={857k^3+891k^2+214k
   +\varepsilon(27k^2-51k-18)\over24}.
  \]
  Equivalently,
  \[
  K(\tau_n^{(1)})=
  \begin{cases}
  (857n^3+1884n^2-989n-1752)/3000,&n\equiv1\pmod {10},\\
  (857n^3+2019n^2-2534n-2592)/3000,&n\equiv6\pmod {10}.
  \end{cases}
  \]
  The proof deletes exactly the isolated holes \(\{2,\ldots,2k\}\), proves
  every deletion gain and every non-atomic compressed-path margin strictly
  positive, and then sums the parity-specific block word. There is no tie or
  argmax exception; \(k=2\) has a final triple and \(k=3\) has an empty
  singleton range, but the same theorem and formula hold.
- EXACT POINTWISE AND ASYMPTOTIC COMPARISON: on \(n=5k+1\), the canonical
  symbolic parameters are \(e=7\), \(v=k-1\), with the boundary correction
  at \(k=6\). For \(k\ge6\),
  \[
  K_{825}-K(\tau_n^{(1)})
  ={k^3+(42+3\varepsilon)k^2
    +(356-225\varepsilon)k+120-177\varepsilon\over24}
  -21\mathbf1_{\{k=6\}}.
  \]
  The explicit differences at \(k=2,3,4,5\) are \(7,18,61,63\), and the
  boundary difference at \(k=6\) is \(145\). The difference is positive on
  every row, so there is no crossover. The cubic coefficient improves from
  \(143/500=858/3000\) to \(857/3000\), exactly \(1/3000\) lower.
- EXACT RESIDUE-ONE CYCLIC-RATIO CONSEQUENCE: inserting label \(1\) in any
  gap gives
  \[
  \Lambda(\sigma_{n,g}^{(1)})=K(\tau_n^{(1)}),
  \qquad
  {K(\tau_n^{(1)})\over\pi}-n^2
  <\rho_{\sigma_{n,g}^{(1)}}
  <{K(\tau_n^{(1)})\over\pi}.
  \]
  On the original residue-one rows, globally only
  \[
  \Lambda_n\le K(\tau_n^{(1)}),
  \qquad
  R_2^*(n)<{\Lambda_n\over\pi}
  \le{K(\tau_n^{(1)})\over\pi}
  \]
  follows directly. More generally, define
  \[
  N(n)=5\left\lceil{n-1\over5}\right\rceil+1.
  \]
  For every \(n\ge7\), this lies in the original KR1 domain and
  \(0\le N(n)-n\le4\). Cancelling the labels above \(n\) from a complete
  KR1 order at \(N(n)\) preserves every induced-subset score on the remaining
  labels. Hence
  \[
  \Lambda_n\le\Lambda_{N(n)}\le K_{\rm R1}(N(n)),
  \qquad
  R_2^*(n)<{\Lambda_n\over\pi}
  \le{K_{\rm R1}(N(n))\over\pi}.
  \]
  Since \(K_{\rm R1}(N)=857N^3/3000+O(N^2)\), the full-sequence limsup
  coefficients are at most \(857/3000\) and \(857/(3000\pi)\). This does
  not globalize the lower side of the fixed-order sandwich, order exact
  angular thresholds, transfer quadratic terms to geometry, prove equality
  or a minimizing-order theorem, establish convergence, or identify an exact
  leading constant. For the prescribed \(N(n)\), the sharp initial domain is
  \(n\ge7\): \(N(6)=6\) is outside the proved KR1 domain, while \(N(7)=11\)
  is its first usable row.
- EXACT THEOREM (KR1 / ARBITRARY-FINITE-PREFIX GAP DECOMPOSITION): on the
  existing \(n=5k+1\) KR1 family, specialize the accepted finite-prefix
  charging chain at
  \[
  a={13-2\sqrt2\over23},\qquad b={1+a\over4}.
  \]
  In the active window \(bn\le t\le an\), every KR1 insertion splits a
  distinct original edge of the base tail cycle. Hence child-edge coverage
  and both recursive-floor terms are identically absent. The height telescope
  and original-slack partition are exact, while the coefficient gap has the
  exact nonnegative decomposition
  \[
  {857\over3000}-C_{\rm AF}
  =\mathcal U+\mathcal H+\mathcal P+\mathcal Q.
  \]
  Here \(\mathcal U\) is discarded slack on unused original edges,
  \(\mathcal H\) is the convex-height loss, \(\mathcal P\) is the local
  product relaxation, and \(\mathcal Q\) is the square-center mismatch. The
  explicit structural term
  \[
  \mathcal U
  ={4614125\sqrt2-5527598\over146004000}
  =0.006833786426979789\ldots>0
  \]
  proves that the current lower functional is not cubically tight when
  evaluated on KR1. The other coefficients are respectively
  \(0.001136949526183062\ldots\),
  \(0.000001205971985529712\ldots\), and
  \(0.0006582696378683922\ldots\). Within-segment floor loss vanishes only
  after the all-fixed-prefix supremum; no new growing-prefix theorem is used.
  This pointwise KR1 audit does not classify the minimum over histories,
  prove that KR1 minimizes \(K\), improve either global coefficient, or make
  a geometric claim. The detailed proof is in
  `research/FIXED_ORDER_CYCLE_RATIO.md`.
- EXACT THEOREM (RELAXED UNUSED-ORIGINAL-EDGE SLACK): put
  \[
  a={13-2\sqrt2\over23},\qquad b={1+a\over4},\qquad
  r=\lfloor an\rfloor,\qquad s=\lceil bn\rceil.
  \]
  For every \(n\ge25\), the exact relaxed minimum over a simple cycle \(C\)
  on \(S_r\) and at most \(r-s\) deleted original edges is
  \[
  \begin{aligned}
  &\min_{\substack{C\text{ simple cycle on }S_r\\
                   E'\subseteq E(C),\ |E'|\le r-s}}
    \sum_{e\in E(C)\setminus E'}\Delta_e\\
  &\qquad={1\over2}
  \left(
  \left\lceil{\,n-\lfloor an\rfloor+1\over2}\right\rceil
  -\lfloor an\rfloor+\lceil bn\rceil
  \right)\\
  &\qquad={2+5\sqrt2\over92}n+O(1).
  \end{aligned}
  \]
  The lower bound counts at most
  \(\lfloor(n-r+1)/2\rfloor\) zero-slack complementary edges. The matching
  zigzag cycle has every other connector at slack \(1/2\) except one closing
  edge, which is deleted together with \(r-s-1\) connectors. The selected
  original edges can be split successively, so the same value is the exact
  minimum of \(E_{\rm unused}\) over compatible histories for that term
  alone. Hence \(E_{\rm unused}\) has a sharp uniform linear lower bound but
  its \(n^3\)-normalized minimum tends to zero. This does not make the full
  KR1G residual subcubic: the lifted history may have cubic height and local-
  floor terms. It neither transfers the positive KR1-specific
  \(\mathcal U\), changes \(C_{\rm AF}\), nor implies a geometric result.
  The detailed proof is in `research/FIXED_ORDER_CYCLE_RATIO.md`.
- EXACT THEOREM (FULL KR1G RESIDUAL ON THE ZIGZAG-WITNESS CLASS): for every
  fixed \(k\), retain without modification
  \[
  a={13-2\sqrt2\over23},\qquad
  \beta_i^{(k)}
  ={1+a+(3a-1)x_i^{(k)}\over4},\qquad
  \lambda_i^{(k)}
  ={(3a-1)x_i^{(k)}\over\beta_i^{(k)}}.
  \]
  Put \(r=\lfloor an\rfloor\), \(s_k=\lceil\beta_k^{(k)}n\rceil\),
  take the translated zigzag \(Z_{n-r+1}\) as \(C_0\), split its closing
  edge and any \(r-s_k-1\) slack-\(1/2\) connectors with the selected
  labels in arbitrary bijection, and complete below \(s_k\) arbitrarily.
  For every history in the union of these classes, the maximum endpoint sum
  never exceeds \(\mathsf{U}_n=n+r+1\). Hence every correction satisfies
  \(A_t\ge\mathsf{U}_n\,t-\mathsf{U}_n^2/4\), forcing a cubic positive
  prefix down to \(d_n=\lceil\mathsf{U}_n/4\rceil\). With \(M_k\) the
  exact normalized-simplex value,
  \[
  \liminf_{n\to\infty}
  {\min_h(P(C_0)+M_h-B_{h,n})\over n^3}
  \ge
  \delta_k
  ={(3a-1)^2\over32}
   \bigl(1+a-4(3a-1)M_k\bigr).
  \]
  The quantifiers are fixed \(k\), then \(n\to\infty\), and only afterward
  \(k\to\infty\). Since \(M_k\uparrow1/3\),
  \[
  \liminf_{k\to\infty}\liminf_{n\to\infty}
  {\min_h(P(C_0)+M_h-B_{h,n})\over n^3}
  \ge {470-159\sqrt2\over73002}>0.
  \]
  Thus the zero alternative is excluded for this whole zigzag-witness
  history class. The theorem is a lower bound, not an exact residual
  coefficient or an outer-limit existence theorem, and it makes no claim
  about arbitrary base cycles, all histories, minimizing orders, or
  geometry. The detailed proof is in
  `research/FIXED_ORDER_CYCLE_RATIO.md`.
- VERIFIED FACT (BOUNDED EXACT DOSSIER DIAGNOSTIC): the standalone
  `ops/TASK-20260718__residue_one_exact_k/exact_diagnostic.py` imports only
  standard-library modules and no project or test helper. It reconstructs
  both block orders, runs independent increasing-path max-plus DPs, and
  audits every residue-one oriented shortcut arc on \(2\le k\le30\). Each
  DP checks 4,504,280 transitions, all 234,030 shortcut arcs pass, and every
  residue-one row has exactly the predicted sole argmax. Direct formula and
  pointwise comparison checks continue through \(k=1000\). No subset or
  permutation is enumerated; the bounded computation corroborates rather
  than replaces the all-\(k\) proof.
- VERIFIED FACT (BOUNDED EXACT KR1 LIFT DIAGNOSTIC): the standalone
  standard-library script in `ops/TASK-20260721__kr1_monotone_lift/` checks
  exactly 1,000 consecutive indices \(7\le n\le1006\). It covers every
  class modulo ten 100 times, every offset \(N(n)-n\in\{0,1,2,3,4\}\)
  200 times, both KR1 parity branches 500 times, and 200 distinct lifted
  KR1 rows. The \(k\)- and \(N\)-formulas agree with exact divisibility, and
  970 third finite differences equal \(1714\), giving the coefficient
  \(857/3000\) exactly. It constructs no order and does not replace the
  all-index cancellation proof.
- VERIFIED FACT (BOUNDED EXACT KR1 GAP DIAGNOSTIC): the standalone
  standard-library script in
  `ops/TASK-20260723__kr1_af_gap_decomposition/` independently reconstructs
  six KR1 rows on both parity branches through \(n=100006\), records all
  deletion endpoints, and checks the exact finite nonnegative decomposition
  with one active cutoff per integer label. The largest row has 8,168
  distinct selected original edges and zero recursive splits. Its six
  normalized components converge to the exact coefficients above. The dense
  cutoff is only a discriminating Riemann-sum audit, not a uniform \(k(n)\)
  theorem or a new fixed-prefix optimization.
- VERIFIED FACT (BOUNDED EXACT RELAXED-SLACK ORACLE): the standalone
  standard-library script in
  `ops/TASK-20260723__kr1g_relaxed_unused_slack/` imports no project helper.
  It exhausts 204,556 Hamiltonian cycles modulo rotation and reversal for
  \(3\le q\le10\), checks all 52 pairs \(1\le\ell\le q\), and independently
  verifies the full deletion profile of every explicit zigzag witness.
  Every exact minimum equals
  \(\frac12[\lceil q/2\rceil-\ell]_+\). This finite oracle corroborates but
  does not replace the all-\(q\) matching proof.
- VERIFIED FACT (BOUNDED EXACT ZIGZAG-HISTORY CHECKER): the standalone
  standard-library script in
  `ops/TASK-20260723__kr1g_zigzag_full_residual/` imports no project helper.
  On four synthetic rational fixtures it exhausts 18,468 literal histories,
  including every permitted connector subset, every selected-label
  assignment, and every completion. Exact `Fraction` arithmetic checks the
  completion DP, full KR1G decomposition, edge-sum invariant, pointwise
  correction bound, finite cubic barrier, and two golden minima. A separate
  exact \(\mathbb Q(\sqrt2)\) implementation checks the first twelve
  fixed-\(k\) scalar bounds and
  \((470-159\sqrt2)/73002>0\). The synthetic fixtures corroborate structure;
  they do not realize the eventual irrational cutoff rows or replace the
  proof.
- EXACT THEOREM (EXACT-THRESHOLD RESIDUE-TWO \(K\)): let
  \(\tau_n^{(2)}\) be the core order returned by
  `residue_two_product_distance_order(n)` for \(n=5k+2\), \(k\ge2\), and
  put \(\varepsilon=k\bmod2\). Its unique maximizing subset is
  \[
  \{2k+1,2k+2,\ldots,5k+2\},
  \]
  and
  \[
  K(\tau_n^{(2)})
  ={286k^3+459k^2+198k+16
   +\varepsilon(-10k^2+40k+27)\over8}.
  \]
  Equivalently,
  \[
  K(\tau_n^{(2)})=
  \begin{cases}
  (286n^3+579n^2-798n-1008)/1000,&n\equiv2\pmod {10},\\
  (286n^3+529n^2+402n+167)/1000,&n\equiv7\pmod {10}.
  \end{cases}
  \]
  The proof deletes precisely the isolated holes \(\{2,\ldots,2k\}\),
  proves every hole gain and every non-atomic compressed-path margin strictly
  positive, and sums the parity-specific block word. There is no tie or
  score correction. At \(k=2\) the doubleton is final, at \(k=3\) the odd
  nonfinal-singleton range is empty, and at \(k=4\) the corresponding even
  range is empty; the theorem remains unchanged.
- EXACT POINTWISE AND ASYMPTOTIC RESIDUE-TWO COMPARISON: on the symbolic K825
  domain, \(e=8\), \(v=k-1\), and the boundary correction is \(-25\) at
  \(k=7\). Thus
  \[
  K_{825}-K(\tau_n^{(2)})
  ={21k^2+(50+30\varepsilon)k+4+35\varepsilon\over4}
  -25\mathbf1_{\{k=7\}}.
  \]
  The explicit differences at \(k=2,3,4,5,6\) are
  \(26,44,124,178,361\), and the boundary difference at \(k=7\) is
  \(382\). Every gap is positive, so there is no crossover. Both cubic
  coefficients equal \(143/500\), and
  \[
  K_{825}(n)-K(\tau_n^{(2)})={21\over100}n^2+O(n).
  \]
- EXACT RESIDUE-TWO CYCLIC-RATIO CONSEQUENCE: inserting label \(1\) in any
  gap gives
  \[
  \Lambda(\sigma_{n,g}^{(2)})=K(\tau_n^{(2)}),
  \qquad
  {K(\tau_n^{(2)})\over\pi}-n^2
  <\rho_{\sigma_{n,g}^{(2)}}
  <{K(\tau_n^{(2)})\over\pi}.
  \]
  No maximizing subset contains label \(1\), so the same unique core subset
  is the unique subset attaining \(\Lambda\) after every insertion.
  Globally, only
  \[
  \Lambda_n\le K(\tau_n^{(2)}),
  \qquad
  R_2^*(n)<{\Lambda_n\over\pi}
  \le{K(\tau_n^{(2)})\over\pi}
  \]
  follows on this residue class. The subsequential limsup coefficients are
  therefore at most \(143/500\) and \(143/(500\pi)\), which are weaker than
  the all-index KR1 coefficients. No global equality, lower sandwich transfer,
  minimizing-order theorem, active geometric/STN classification at the exact
  threshold, exact angular ordering, quadratic geometric coefficient, or
  improvement of the KR1 all-index bound follows.
- VERIFIED FACT (BOUNDED EXACT DOSSIER DIAGNOSTIC): the standalone
  `ops/TASK-20260718__residue_two_exact_k/exact_diagnostic.py` imports only
  standard-library modules and no project or test helper. It independently
  reconstructs both block orders, runs increasing-path max-plus DPs, and
  audits every residue-two oriented shortcut arc for \(2\le k\le30\). Each
  DP checks 4,623,615 transitions, all 238,670 arcs pass, every row has the
  predicted sole argmax, and the bounded minimum hole and path margins are
  respectively \(26\) and \(7\). Direct formula and K825 comparison checks
  continue through
  \(k=1000\), with no crossover. This finite computation enumerates neither
  subsets nor cyclic orders and corroborates rather than replaces the
  all-\(k\) proof.
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
  descending closure, macro compression, and Karp scoring. A further exact
  test checks all 437 canonical core orders and all 2,957 insertion gaps,
  covering the same 2,956 complete classes. Core minimizer counts are
  `(1,1,1,3,4,12)` and complete minimizer counts remain
  `(1,3,4,15,24,84)`. At `n=3`, the two insertion arcs are reflections and
  collapse to one complete class. This finite result verifies the
  implementation but is not the all-order proof, a closed-form evaluation of
  the reduced minimum, an exact geometric optimum, or an asymptotic theorem.
  The production bound remains `n<=8`.
- EXACT THEOREM (FINITE \(n=9\) CORE MINIMIZER CLASSIFICATION): equality in
  the accepted \(S_6/S_5\) lemma forces the induced six-label cycle
  \(\Omega=(9,5,8,6,7,4)\) up to dihedral symmetry. A core order has
  \(K=239\) exactly when label \(3\) is inserted in one of the four gaps of
  \(\Omega\) not incident to label \(4\), and label \(2\) is then inserted
  in any of the seven resulting gaps. Thus
  \[
  \Lambda_9=239,
  \qquad
  \#\{\text{dihedral core minimizers}\}=28.
  \]
  Exact index-one elimination/insertion gives 224 complete dihedral minimizer
  classes. All 28 core classes maximize on
  \(S_6=\{4,5,6,7,8,9\}\); 27 do so uniquely, while the canonical class
  `(9,4,7,6,8,3,2,5)` also maximizes on the full core.
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): an independent
  test-only oracle directly generates all \(7!/2=2{,}520\) dihedral core
  classes on \(\{2,\ldots,9\}\), literally scores all 255 nonempty subsets of
  every class, records every maximizing subset, and recovers exactly the
  proved minimum, 28 minimizers, and \(27+1\) minimizer-argmax pattern. The
  oracle calls no repository canonicalizer, public enumerator, or production
  Karp scorer. Its 2,520-row deterministic record has SHA-256
  `557226668a82f6489274571148572076e373d49baefaa61e6d1f5a458bb857a2`.
  This core count only happens to equal the production \(n=8\) complete-order
  ceiling; production still hard-rejects \(n=9\).
- INTERPRETATION: the \(n=9\) theorem and oracle are finite exact
  combinatorial results. They do not give an exact value of \(R_2^*(9)\), a
  geometric minimizer classification, an all-\(n\) formula, or an asymptotic
  claim.
- EXACT THEOREM (FINITE \(n=10\) SEVEN-LABEL LEMMA): for every cyclic order
  \(\omega\) on \(\{4,\ldots,10\}\),
  \[
  \max\{P_\omega(\{4,\ldots,10\}),
        P_\omega(\{5,\ldots,10\})\}\ge323.
  \]
  The duplicated-multiset pairing relaxation on \(\{5,\ldots,10\}\) has
  baseline 320. An exact least-entry recurrence classifies all pairing
  signatures at the only relevant values 320, 321, and 322: one, three, and
  four signatures respectively. Only one 322 signature is a simple spanning
  cycle, and inserting label \(4\) in any of its six edges raises the score by
  at least one.
- EXACT THEOREM (FINITE \(n=10\) SEVEN-LABEL EQUALITY CLASSIFICATION):
  equality in the preceding lemma holds in exactly two dihedral classes,
  represented by
  `(10,4,7,8,6,9,5)` and `(10,5,9,4,7,8,6)`, with score pairs
  \((P(T_7),P(T_6))=(321,323)\) and \((323,322)\), respectively. In the
  tail-322 branch the unique cyclic signature and its six exact corrections
  force insertion on \(\{7,9\}\). In the tail-323 branch, the only possible
  nonpositive-correction edges are
  \(\{7,10\},\{8,9\},\{8,10\},\{9,10\}\); their fixed-edge pairing floors
  are 323, 323, 326, and 330. The unique equality signature for \(\{8,9\}\)
  is not a simple cycle, while \(\{7,10\}\) gives the sole surviving class.
  This proof does not use cyclic-order enumeration.
- EXACT THEOREM (FINITE \(n=10\) LABEL-THREE INSERTION-GAP CLASSIFICATION):
  for a partial cycle \(\nu\) on \(\{3,\ldots,10\}\), define
  \[
  K_{\ge3}(\nu)=
  \max_{\varnothing\ne U\subseteq\{3,\ldots,10\}}P_\nu(U).
  \]
  Inserting label \(3\) into `(10,4,7,8,6,9,5)` gives
  \(K_{\ge3}=326\) on \(\{4,7\}\) and 323 on every other gap. Inserting
  it into `(10,5,9,4,7,8,6)` gives 326 on \(\{4,9\}\), 328 on
  \(\{4,7\}\), and 323 on every other gap. The proof uses
  \(\Delta_3(a,b)=3(a+b)-ab=9-(a-3)(b-3)\), the exact shortcut
  transformation under insertion, and complete nonnegative-gain
  certificates. The first cycle has argmaxes \(\{5,\ldots,10\}\) and the
  full partial set on gap \(\{4,10\}\), and only \(\{5,\ldots,10\}\) on
  its other five admissible gaps. Every admissible gap of the second cycle
  has sole argmax \(\{4,\ldots,10\}\). Each excluded row has the full
  partial set as its sole argmax.
- EXACT THEOREM (FINITE \(n=10\) CORE MINIMIZER CLASSIFICATION): inserting
  label \(2\) in the eight gaps of each of the eleven surviving partial
  cycles gives 88 pairwise distinct dihedral core classes. The exact
  variation \(\Delta_2(a,b)=2(a+b)-ab=4-(a-2)(b-2)\), together with the
  preceding argmax and shortcut-gain certificates, proves that exactly 87
  classes have \(K=323\). The sole exception is
  `(10,3,2,4,7,8,6,9,5)`, which has \(K=325\) and sole argmax
  \(\{2,\ldots,10\}\). Of the 87 core minimizers, seven have exactly
  the argmaxes \(\{5,\ldots,10\}\) and \(\{3,\ldots,10\}\), 40
  have sole argmax \(\{5,\ldots,10\}\), and 40 have sole argmax
  \(\{4,\ldots,10\}\). Exact index-one elimination/insertion gives
  exactly \(87\cdot9=783\) complete dihedral minimizer classes, distributed
  as 63 with two argmaxes and 360 in each sole-argmax family.
- VERIFIED FACT (FINITE EXACT COMBINATORIAL RESULT): the core witness
  \(\tau=(10,2,3,4,7,8,6,9,5)\) has complete sum 319. Its exact shortcut
  table has only the positive nontrivial gains
  \(g(10,3)=4\), \(g(10,4)=2\), and \(g(10,7)=4\), with no nontrivial zero.
  Hence
  \[
  K(\tau)=323,
  \qquad
  \operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,10\}}
  P_\tau(U)
  =\bigl\{\{5,\ldots,10\},\{3,\ldots,10\}\bigr\}.
  \]
  Together with the accepted reduction, this proves
  \(\Lambda_{10}=323\).
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): independent test-only
  helpers directly generate all \(6!/2=360\) dihedral classes in the
  seven-label lemma, recover the exact low-pairing and fixed-edge branch data,
  audit every required insertion correction, confirm exactly the two proved
  equality classes, and literally score all \(2^9-1=511\) nonempty witness
  subsets. Separate oracles construct the 14 label-three insertions and score
  all \(14(2^8-1)=3{,}570\) corresponding nonempty subsets, then construct
  the 88 label-two insertions and score all
  \(88(2^9-1)=44{,}968\) corresponding nonempty subsets. They record every
  argmax; a test-local dihedral key confirms 88 distinct core classes and
  783 distinct label-one insertions. These paths call no repository
  canonicalizer, public enumerator, or production Karp scorer. Production
  source and the public complete-order `n<=8` boundary are unchanged.
- INTERPRETATION: the \(n=10\) theorem and oracles are finite exact
  combinatorial results. They do not give an exact value of \(R_2^*(10)\),
  a geometric minimizer statement, an all-\(n\) formula, or an asymptotic
  claim. The score-325 exception is unique among the 88 candidates forced by
  the earlier equality classifications, not among every nonminimizing core
  order.
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
  within the single-subset relaxation named above. The exact consecutive-tail
  block extension has the same leading coefficient for every fixed \(r\)
  and every \(r=o(n)\). None of these statements is an exact asymptotic
  result for Power-Ringmin. Joint optimization of the one-prefix linear block has a
  positive method-specific certified cubic residual over its inner-cycle
  reference and yields the one-prefix global lower coefficient
  \((4+2\sqrt3)/(27\pi)\). Its total coefficient
  \((4+2\sqrt3)/27\) is optimal only within the one-prefix specialization of
  CR28ax--CR28bg; the associated
  residual contribution at that optimizer is \((26-15\sqrt3)/54\), not a
  separately maximized residual. The globally optimized two-prefix CR28bw
  template raises the lower coefficient to
  \[
  {491596+6578\sqrt{143}\over2061723\pi}.
  \]
  The globally optimized three-prefix template raises it again to
  \[
  {753972193324+106042322\sqrt{377823}
   \over2960667770787\pi}.
  \]
  The globally optimized four-prefix template raises it further to
  \[
  {597580022071777213687318156
   +21288970076515705538\sqrt{2903456040383}
   \over2290468477489828247376833403\pi}.
  \]
  The explicit rational five-prefix witness at \(\alpha=13/30\) first raises
  the established lower coefficient to
  \[
  {2263404122555368590593580404287
   \over8177706222298165502582585481000\pi}.
  \]
  The globally optimized five-prefix template raises its fixed-\(k=5\)
  optimum further to
  \[
  {346693217780244687187063490332457027500975566238012204
   +1228130489996268437333105902690103574002
    \sqrt{183342238504950468196395903}
   \over1312688475479610714750859896048564873968757997852345827\pi}.
  \]
  The all-fixed-\(k\) supremum corollary then raises the current lower
  coefficient to
  \[
  {434+4\sqrt2\over1587\pi}.
  \]
  It applies charging at every fixed finite \(k\), with a threshold that may
  depend on \(k\), and only afterward takes the supremum of the resulting
  scalar inequalities. It uses no \(k=k(n)\) and no interchange of limits.
  All four multi-prefix optimizers are exact and unique inside their
  respective templates. The
  older rational witness remains the finite two-prefix theorem from \(n=59\),
  while the irrational three-prefix optimizer has the stronger finite theorem
  \(\Lambda_n>C_{3,*}n^3\) from the minimal uniform threshold \(159\). The
  optimized four-prefix theorem has no finite rounding specialization. The
  five-prefix rational point remains the strict suboptimal witness with an
  exact finite theorem from the minimal uniform threshold \(234\); the
  irrational global five-prefix optimizer has no finite rounding theorem.
  The exact block residual, finite rounding at the irrational two-, four-,
  and five-prefix optimizers, convergence, and the exact global leading
  coefficient remain unresolved.
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
  matching product-distance construction gives the regular-direction
  coefficient \(8/(25\pi)\). The exact K825 theorem for the same core order
  historically improved the variable-spacing limsup upper coefficient to
  \(143/(500\pi)\); the KR1 cancellation lift improves the current all-index
  coefficient to \(857/(3000\pi)\). No geometric limit has been proved.

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
  This remains the exact regular-direction product-distance coefficient; its
  geometric conclusion is a valid historical upper bound, not an exact
  leading constant or a convergence theorem. The later K825 theorem
  historically sharpens the variable-spacing upper coefficient to
  \(143/(500\pi)\), and the KR1 cancellation lift sharpens the current
  all-index coefficient further to \(857/(3000\pi)\).
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
- EXACT THEOREM (ONE-TRIPLE REVERSAL OBSTRUCTION): restrict the symbolic
  eight-twenty-fifths order to
  \[
  n=10m+3,
  \qquad m\ge3,
  \qquad d=8m+4,
  \qquad T={d(d-1)\over2}.
  \]
  Its triple paths are
  \(P_s=(d-1-2s,4m+2+s,d-2-2s)\), \(0\le s\le m\). If
  \(\tau_{m,s}\) reverses only the two outer entries of \(P_s\), then
  \[
  W(\tau_{m,s})=
  \begin{cases}
  (d^2-1)/2=T+(d-1)/2,&s=0,\\
  T,&1\le s\le m.
  \end{cases}
  \]
  The exact distance classes are
  \(M_1=T\), the displayed piecewise \(M_2\),
  \(M_3=(5m+2)(9m+5)/3<T\), and
  \(M_{\ge4}=n(n-1)/4<T\). With the canonical cut,
  \[
  C_1=(4m+1)d,
  \quad C_2={(6m+1)d\over2},
  \quad C_3={(4m+1)(d-1-\mathbf1_{\{s=0\}})\over3},
  \]
  all strictly below \(T\). Hence every parameter choice has coefficient
  \(8/25\); the persistent adjacent saturation is an exact family-specific
  obstruction. The smallest admitted non-neutral row is
  \((m,s)=(3,0)\), where \(T=378\) and \(W=783/2\).
- INTERPRETATION: this obstruction concerns the surrogate on one explicit
  subsequence and one local perturbation. Its regular-direction transfer is
  only an upper bound; it neither lower-bounds \(R_2^*(n)\) nor excludes a
  different order family, unequal directions, or a non-regular geometric
  construction.
- EXACT THEOREM (NONLOCAL ONE-GAP PATH-ROTATION OBSTRUCTION): for
  \(n=10m+3\), \(m\ge3\), \(d=8m+4\), and
  \(T=d(d-1)/2\), keep the terminal/low scaffold and every path orientation
  fixed, but assign the whole path \(P_{j+1\bmod2m}\) to terminal gap
  \(G_j\). The resulting \(\widehat\sigma_m\) is a permutation. Its exact
  distance-class maxima and unique unordered class maximizers are
  \[
  \begin{array}{c|c|c}
  1&T&\{d-1,4m+2\}\\
  2&n(d-1)/2&\{n,d-1\}\\
  3&(5m+2)(9m+4)/3&\{5m+2,9m+4\}\\
  \ge4&n(n-1)/4&\{n-1,n\}.
  \end{array}
  \]
  At the canonical cut, the exact class maxima are
  \[
  C_1=(4m+1)d,\qquad
  C_2={d(d-2)\over2},\qquad
  C_3={d^2\over6},\qquad
  C_{\ge4}={T\over2},
  \]
  with unique maximizers
  \(\{\rho_0,E_0\}\), \(\{B_0,E_0\}\),
  \(\{c_0,E_0\}\), and \(\{A_0,E_0\}\), respectively. Therefore
  \[
  W(\widehat\sigma_m)
  ={n(d-1)\over2}
  ={(10m+3)(8m+3)\over2},
  \]
  uniquely saturated by \(\{n,d-1\}\) at distance two, and
  \[
  {W(\widehat\sigma_m)\over n^2}\longrightarrow{2\over5}>{8\over25}.
  \]
  The exact obstacle is the word \(n,2,d-1\) produced when \(P_0\) moves to
  the closing gap. This single reassignment worsens the coefficient by
  \(2/25\).
- VERIFIED FACT (FINITE EXACT DOSSIER DIAGNOSTIC): the standalone
  standard-library script in
  ops/TASK-20260717__nonlocal_middle_path_rotation/ reconstructs only the
  a-priori fixed family and independently scores every unordered pair at
  \(m=3,4,9,25\). It confirms the four distance classes, four canonical-cut
  classes, all unique class maximizers, and the unique full-score saturator.
  It imports no project or test helper and performs no cyclic-order search or
  enumeration.
- INTERPRETATION: this theorem concerns one deterministic whole-path
  reassignment only. Its already proved regular-direction transfer is a
  weaker upper bound with coefficient \(2/(5\pi)\); it gives no geometric
  lower bound, no obstruction to another order or direction assignment, and
  no consequence beyond the existing regular-direction upper-bound method.
- EXACT NECESSARY PLACEMENT THEOREM (DISTINGUISHED PATH): retain the
  \(n=10m+3\), \(m\ge3\), scaffold, all path definitions and orientations,
  and \(T=d(d-1)/2\), but allow an arbitrary bijection \(\alpha\) from
  terminal gaps to whole paths. If \(P_0=(d-1,4m+2,d-2)\) occupies \(G_j\),
  then the exact local maxima among its distance-one and distance-two pairs
  are
  \[
  M^{\rm loc}_1(j)=T,
  \qquad
  M^{\rm loc}_2(j)=T+{j(d-1)\over2},
  \]
  uniquely on \(\{d-1,4m+2\}\) and \(\{E_j,d-1\}\), respectively. The
  right terminal score is
  \[
  R_j=
  \begin{cases}
  T+[j(d-2)-2]/2,&0\le j\le2m-2,\\
  T-d/2,&j=2m-1.
  \end{cases}
  \]
  Thus its own right inequality allows \(j\in\{0,2m-1\}\), but the left
  inequality allows only \(j=0\). Every full reassignment with
  \(W^{(\le2)}\le T\), hence every one with \(W\le T\), must satisfy
  \(\alpha(0)=0\). Consequently \(G_1,\ldots,G_{2m-1}\) are locally
  excluded for \(P_0\), while \(G_0\) is uniquely locally non-excluded.
  The closing word is exactly
  \((n,2,d-1,4m+2,d-2,4m+1,d)\), so its safe right side does not remove
  the left obstruction. Because \((d-1)(4m+2)=T\), every reassignment with
  \(W^{(\le2)}\le T\) has truncated score exactly \(T\); if it also satisfies
  \(W\le T\), then its full score is exactly \(T\).
- INTERPRETATION: local non-exclusion of \(G_0\) is not a completion theorem.
  The identity assignment from the established construction is a separate
  known witness, but the placement lemma neither constructs nor proves the
  existence of a nonidentity reassignment and does not analyze the remaining
  path assignments.
- VERIFIED FACT (FINITE EXACT LOCAL-GAP DIAGNOSTIC): the standalone
  standard-library script in
  ops/TASK-20260717__p0_terminal_gap_classification/ scans only the terminal
  gap indices at \(m=3,4,9,25\). It checks the seven-label local word, exact
  one- and two-step scores, unique maxima, one-sided allowed sets, and cyclic
  closure, returning \(j=0\) as the sole locally non-excluded index in every
  row. It builds no complete order, assigns no other path, imports no project
  or test helper, and enumerates no path permutation. The finite check
  corroborates rather than proves the all-\(m\) theorem.
- EXACT LOCAL RELATION THEOREM (GENERIC PATHS): in the same
  \(n=10m+3\), \(m\ge3\), scaffold, a triple
  \(P_k=(d-1-2k,4m+2+k,d-2-2k)\), \(0\le k\le m\), placed in
  \(G_j\) has all adjacent pairs at most \(T\) and unique local
  distance-two maximum
  \[
  M^{\rm tr}_2(k,j)={(d+j)(d-1-2k)\over2}.
  \]
  Therefore its exact locally non-excluded row is
  \[
  0\le j\le
  \ell_k:=
  \min\!\left\{2m-1,
  \left\lfloor{2kd\over d-1-2k}\right\rfloor\right\}.
  \]
  Equivalently, the triple indices locally permitted by \(G_j\) are
  \[
  k\ge\kappa_j:=
  \left\lceil{j(d-1)\over2(d+j)}\right\rceil.
  \]
  Every singleton \(P_k=(4m+2+k)\), \(m+1\le k\le2m-1\), is strictly
  locally non-excluded in every gap. Its exact distance-two maximum is
  \(x_k(d+j+1)/2\) for \(j\le2m-2\) and \(x_kn/2\) at cyclic closure.
  The last nonclosing and closing triple thresholds are
  \(\lfloor(4m+1)/5\rfloor\) and
  \(\lfloor(4m+3)/5\rfloor\).
- EXACT FERRERS/HALL STRUCTURE: for a given path-to-gap bijection
  \(\alpha\), the distance-at-most-two condition is equivalent to
  \((\alpha(j),j)\in\mathcal R_{\rm loc}\) for every \(j\). With
  \(v=2m\), the column neighborhoods are the nested suffixes
  \[
  N(G_j)=\{P_{\kappa_j},\ldots,P_{v-1}\},
  \qquad
  \kappa_j=\left\lceil{j(d-1)\over2(d+j)}\right\rceil.
  \]
  The thresholds are nondecreasing and satisfy
  \(\kappa_0=0\), \(\kappa_1=1\), and
  \(1\le\kappa_r\le r-1\) for \(2\le r\le v-1\). After fixing a local edge
  \((k,j)\), residual Hall is equivalent to
  \[
  \kappa_r+\mathbf1_{\{k\ge\kappa_r\}}
  \le r+\mathbf1_{\{j>r\}}
  \qquad(r\ne j).
  \]
- EXACT EDGE-EXTENDIBILITY THEOREM: the support of relation-compatible
  bijections is
  \[
  \mathcal R_{\rm ext}
  =\{(0,0)\}\cup
  \{(k,j)\in\mathcal R_{\rm loc}:j\ge1\}.
  \]
  Thus every positive-column local edge is extendible, while none of the
  \((k,0)\), \(k>0\), is. The latter fail Hall because, after the prescribed
  path is removed, the \(v-1\) gaps \(G_1,\ldots,G_{v-1}\) have only
  \(v-2\) available neighbors. For existence, rotating the integer interval
  between \(j\) and \(k\) gives explicit bijections in the three cases
  \(j<k\), \(j=k\), and \(j>k\). The shifts preserve \((0,0)\) and cover
  the triple/singleton boundary, terminal singleton, closing column, and
  \(m=3\) without wrapping the canonical cut.
- EXACT ARBITRARY-BIJECTION COLLAPSE THEOREM: for every path-to-gap bijection
  \(\alpha\) in the symbolic \(n=10m+3\), \(m\ge3\), scaffold, the complete
  six-form triple and four-form singleton classification gives
  \[
  W^{(=3)}(\sigma_\alpha)
  \le{n(5m+2)\over3}<T.
  \]
  This bound does not require relation-compatibility. It is sharp exactly
  when \(\alpha(2m-2)=m\) or \(\alpha(2m-1)=m\), and both alternatives have
  relation-compatible PG46 witnesses. Every distance at least four has score
  at most \(n(n-1)/4<T\), while the internal pair \(A_0c_0=T\) persists.
  Therefore
  \[
  W(\sigma_\alpha)=W^{(\le2)}(\sigma_\alpha)
  \]
  for every bijection.
- EXACT FULL-OPTIMAL EQUIVALENCE AND SUPPORT THEOREM: on this branch,
  \[
  \alpha\text{ relation-compatible}
  \quad\Longleftrightarrow\quad
  W(\sigma_\alpha)=T=W_n.
  \]
  Hence every compatible bijection is a global full-distance minimizer of the
  product-distance surrogate, and every incompatible scaffold bijection has
  score strictly above \(T\). If \(\mathcal R_{\rm full}\) is the edge
  support of full-optimal scaffold bijections, then
  \[
  \mathcal R_{\rm full}=\mathcal R_{\rm ext}
  =\{(0,0)\}\cup
  \{(k,j)\in\mathcal R_{\rm loc}:j\ge1\}.
  \]
  This theorem classifies their score and edge support; the separate Ferrers
  theorem below supplies their count without enumerating them. Neither has a
  geometric consequence.
- EXACT THEOREM (PGE5-1--PGE5-26): on the canonical even-\(v\), \(e=5\)
  scaffold \(n=10m+4\), \(m\ge2\), the literal local relation is the suffix
  board \(\mathcal R_{\rm loc}=\{(k,j):k\ge\kappa_j\}\). Its exact
  full-threshold support is
  \(\mathcal R_{\rm full}=\mathcal R_{\rm ext}=\{(0,0)\}\cup
  \{(k,j):j\ge1,\ k\ge\kappa_j\}\). Every scaffold bijection satisfies
  \(W=W^{(\le2)}\), and local compatibility is equivalent to \(W=W_n\).
  The local board is Ferrers; the full support is not, while deleting the
  forced pair \((P_0,G_0)\) leaves a matching-covered Ferrers board. This is
  exact \(W\)-minimality only for the supported scaffold bijections: it does
  not classify outside-scaffold \(W\)-minimizers or by itself evaluate
  \(K\), and it implies no angular or geometric result. Definitions,
  boundary cases, and the complete support proof are authoritative in
  [`research/PRODUCT_DISTANCE_SURROGATE.md`](research/PRODUCT_DISTANCE_SURROGATE.md#the-canonical-even-v-e5-path-to-gap-support).
- EXACT THEOREM (PGE5ODD-1--PGE5ODD-26): on the canonical odd-\(v\),
  \(e=5\) scaffold \(n=10m+9\), \(m\ge1\), there are \(m+2\) triples,
  no doubleton, and \(m-1\) singletons.  With \(d=8m+9\),
  \(T=W_n=d(d-1)/2\), and
  \[
  \kappa_j=\left\lceil{j(d-1)\over2(d+j)}\right\rceil,
  \]
  the exact local relation is
  \(\mathcal R^{\rm odd}_{\rm loc}=\{(k,j):k\ge\kappa_j\}\), with true
  terminal thresholds
  \[
  \kappa_{2m-1}=\left\lfloor{4m+3\over5}\right\rfloor,
  \qquad
  \kappa_{2m}=\left\lfloor{4m+5\over5}\right\rfloor.
  \]
  Its Hall-extendible and full-threshold supports coincide and equal
  \[
  \mathcal R^{\rm odd}_{\rm full}=\mathcal R^{\rm odd}_{\rm ext}
  =\{(0,0)\}\cup
  \{(k,j):1\le j\le2m,\ k\ge\kappa_j\}.
  \]
  Every scaffold bijection satisfies \(W=W^{(\le2)}\), and local
  compatibility is equivalent to \(W=W_n\).  The proof treats distances
  \(1,2,3,\ge4\) and the genuine closing word separately.  There is no
  odd-parity completion obstruction; the unreduced full support alone is
  non-Ferrers, while deleting forced \((P_0,G_0)\) leaves a
  matching-covered Ferrers board.  This theorem evaluates neither \(K\) nor
  geometry and does not classify outside-scaffold \(W\)-minimizers.  The
  authoritative proof is
  [`research/PRODUCT_DISTANCE_SURROGATE.md`](research/PRODUCT_DISTANCE_SURROGATE.md#the-canonical-odd-v-e5-path-to-gap-support).
- EXACT FIXED PGE5 INTERVAL-SHIFT CORE THEOREM (KPGE5-1--KPGE5-30): on
  the even-\(v\), \(n=10m+4\), \(m\ge2\) scaffold, fix only (PGE5-22) at
  \((q,2m-1)\), where \(q=\lfloor(4m+3)/5\rfloor\). The resulting core has
  the sole induced-subset maximizer
  \[
  B_m=\{4m+1,\ldots,10m+4\}
  \]
  and
  \[
  K={572m^3+809m^2+8mq+329m+4q^2+20q+36\over2}.
  \]
  Its nine deletion classes have unique minimum \(36m+20\) at
  \(\lambda_0\). Every compressed shortcut is strict; its unique minimum is
  the genuine closing margin \(9\) at \(m=2\), and \(4m+2\) at the stable
  connector \(c_0\) for \(m\ge3\). All five \(m\bmod5\) branches are
  regular. The literal minimum row has \(\alpha=(0,1,3,2)\) and \(K=4297\).
  On the same subsequence, canonical K825 has the same maximizing label set
  and
  \[
  K_{825}={572m^3+819m^2+361m+44\over2}.
  \]
  The fixed shift is strictly smaller on every row, with
  \(K_{825}-K=13n^2/2500+O(n)\), while both have cubic coefficient
  \(143/500\). This is one fixed-core combinatorial theorem: it optimizes no
  other supported bijection, counts no permanent, and gives no angular,
  geometric, global-minimizer, or global-optimality conclusion. The detailed
  proof is authoritative in
  [`research/FIXED_ORDER_CYCLE_RATIO.md`](research/FIXED_ORDER_CYCLE_RATIO.md#20-exact-k-for-the-fixed-pge5-interval-shift).
- VERIFIED FACT (FINITE EXACT FIXED-PGE5-K DIAGNOSTIC): the standalone
  standard-library script in
  `ops/TASK-20260720__pge5_interval_shift_exact_k/` constructs only the
  prescribed shift. A candidate-free max-plus recurrence checks the exact
  score and complete argmax classification on \(m=2,\ldots,30\) through
  37,475,656 transitions; a separate traversal checks every deletion budget
  and all 968,774 proper oriented arcs, including the cyclic cut. Formula,
  support, five-residue, boundary, and K825 checks continue through
  \(m=1000\). It imports no project/test helper and enumerates no subset,
  matching, path assignment, path permutation, supported-bijection family,
  or permanent. The finite computation corroborates rather than proves the
  all-\(m\) theorem.
- EXACT PGE5 SINGLETON-REVERSAL THEOREM (KRPGE5-1--KRPGE5-36): on the same
  \(n=10m+4\), \(m\ge2\) scaffold, put
  \(q=\lfloor(4m+3)/5\rfloor\), retain the interval shift through the
  doubleton, reverse precisely the complete singleton block, and assign
  \(P_q\) to the genuine closing gap. The five image blocks partition all
  path indices, and every image belongs to (PGE5-23), including the forced
  edge, doubleton, empty singleton range at \(m=2\), and exact cyclic
  threshold. Hence the map is a supported bijection and has \(W=W_n\).
  Its complete induced-subset classification is
  \[
  \operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P(U)
  =\bigl\{\{4m+1,\ldots,10m+4\}\bigr\},
  \]
  and
  \[
  K_*={1714m^3+2439m^2+24mq+965m+12q^2+60q+120\over6}.
  \]
  The nine exhaustive deletion classes have unique minimum \(36m+20\) at
  \(\lambda_0\). Every compressed shortcut is strict; the unique minimum is
  the genuine closing margin \(9\) at \(m=2\), and \(4m+2\) at \(c_0\)
  for \(m\ge3\). Exact singleton-block cancellation proves
  \[
  K_\uparrow-K_*={(m-1)(m-2)(m-3)\over3},
  \]
  including equality at \(m=2,3\); therefore the new fixed-subsequence
  coefficient is \(857/3000\). Canonical K825 is strictly larger pointwise,
  with the five exact gap branches in (KRPGE5-30). For every cyclic gap
  \(g\), inserting label \(1\) into the fixed core gives a complete order
  \(\sigma_{m,g}^{(5,*)}\) satisfying
  \[
  \Lambda\bigl(\sigma_{m,g}^{(5,*)}\bigr)=K_*,
  \qquad
  {K_*\over\pi}-(10m+4)^2
  <\rho_{\sigma_{m,g}^{(5,*)}}
  <{K_*\over\pi}.
  \]
  Globally, only
  \[
  R_2^*(10m+4)<{\Lambda_{10m+4}\over\pi}\le {K_*\over\pi}
  \]
  follows, and hence
  \[
  \limsup_{m\to\infty}
  {R_2^*(10m+4)\over(10m+4)^3}
  \le {857\over3000\pi}.
  \]
  This proves no minimizing-order or geometric optimality, no matching
  global lower bound, no all-\(n\) limsup bound, and no exact leading
  constant for the global optimum \(R_2^*\). The detailed proof is
  authoritative in
  [`research/FIXED_ORDER_CYCLE_RATIO.md`](research/FIXED_ORDER_CYCLE_RATIO.md#21-exact-k-for-the-pge5-singleton-reversal-shift).
- VERIFIED FACT (FINITE EXACT PGE5 SINGLETON-REVERSAL DIAGNOSTIC): the sole
  standalone standard-library script in
  `ops/TASK-20260720__pge5_singleton_reversal_exact_k/` constructs the one
  prescribed map and the accepted monotone comparator only for direct score
  cancellation. On \(m=2,\ldots,30\), a candidate-free max-plus recurrence
  checks the unique backbone through 37,475,656 transitions, while a separate
  all-arcs traversal checks every deletion budget and all 968,774 proper
  oriented arcs, including the cyclic cut. Every label-one insertion gap and
  the exact elimination inequalities are checked on those bounded rows,
  totaling 4,727 gaps and 484,387 distinct neighbor pairs. The \(n\)-form
  identity is checked coefficientwise in the independent symbols \(m,q\);
  formula, support, empty-range, target, residue, and K825 checks continue
  through \(m=1000\). It imports no project/test helper and searches no
  subset, matching, path assignment, supported-bijection family, alternative
  core-order family, or permanent. The finite computation corroborates
  rather than proves the all-\(m\) theorem and does not verify the
  real-arithmetic angular sandwich.
- EXACT CANONICAL ODD-\(v\), \(e=5\) CORE THEOREM
  (KRPGE5ODD-1--KRPGE5ODD-40): on \(n=10m+9\), \(m\ge1\), put
  \(q=\lfloor(4m+5)/5\rfloor\) and fix the map that is the identity below
  \(q\), shifts triples through \(P_{m+1}\), reverses the complete singleton
  block, and places \(P_q\) in the genuine closing gap. Its four image
  blocks partition all path indices, every incidence belongs to the exact
  PGE5ODD support, and hence the map is a supported bijection with
  \(W=W_n\). Its complete induced-subset argmax is
  \[
  \begin{cases}
  \bigl\{\{8,\ldots,19\}\bigr\},&m=1,\\
  \bigl\{\{4m+3,\ldots,10m+9\}\bigr\},&m\ge2.
  \end{cases}
  \]
  With
  \[
  F_m={1714m^3+4977m^2+24mq+4721m+12q^2+72q+1464\over6},
  \]
  the exact score is \(K_m=F_m+11\mathbf1_{\{m=1\}}\). The minimum row has
  \(K_1=2175\): the stable tail containing \(7\) has score \(2164\), and
  deleting \(7\) supplies the real \(+11\) correction. For \(m\ge2\), the
  unique deletion-gain minimum is \(36m+38\) at \(\lambda_0\); the unique
  shortcut minimum is the genuine closing margin \(9\) at \(m=2\), then
  \(4m+4\) at \(c_0\). Canonical K825 is strictly larger on every row,
  including gap \(11\) at \(m=1\), and the fixed-family coefficient is
  \(857/3000\). For every insertion gap of label \(1\), exact elimination
  gives \(\Lambda=K_m\) and the strict fixed-order sandwich. Globally, only
  \(\Lambda_{10m+9}\le K_m\) and
  \(R_2^*(10m+9)<\Lambda_{10m+9}/\pi\le K_m/\pi\) follow, with their
  subsequential upper coefficients. There is no minimizing-order theorem,
  matching global lower bound, all-\(n\) limsup, convergence, or exact
  leading constant for \(R_2^*\). The detailed proof is authoritative in
  [`research/FIXED_ORDER_CYCLE_RATIO.md`](research/FIXED_ORDER_CYCLE_RATIO.md#22-exact-k-for-the-canonical-odd-v-e5-map).
- VERIFIED FACT (FINITE EXACT CANONICAL ODD-\(v\), \(e=5\) \(K\)
  DIAGNOSTIC): the sole standalone standard-library script in
  `ops/TASK-20260721__canonical_e5_odd_exact_k/` constructs only the fixed
  KRPGE5ODD map. On \(m=1,\ldots,30\), a candidate-free max-plus recurrence
  checks the exact score and unique induced-subset argmax through
  39,970,045 transitions. A separate traversal checks 1,891 isolated-hole
  gains, all 1,016,930 proper oriented arcs, the exact raw-arc plus
  hole-budget identity, and 1,010,149 nontrivial shortcuts, including the
  cyclic cut. It also checks all 4,890 label-one insertion gaps and 508,465
  elimination neighbor pairs on those rows. Formula, support, residue,
  minimum-row residual, K825, and coefficient identities continue through
  \(m=1000\). It imports no project/test helper and enumerates no assignment,
  matching, subset, permanent, or alternative order family. The bounded
  computation corroborates rather than proves the all-domain theorem and
  does not verify the real-arithmetic angular sandwich.
- EXACT \(n=10m+3\), \(e=4\) FERRERS COUNT THEOREM: put
  \(v=2m\), \(d=8m+4\), and
  \[
  \kappa_j=
  \left\lceil{j(d-1)\over2(d+j)}\right\rceil.
  \]
  PG49 forces \((0,0)\). On the reduced board, assigning the nested columns
  in the order \(G_{v-1},\ldots,G_1\) leaves exactly
  \(j+1-\kappa_j\) choices at \(G_j\), independently of the narrower-column
  choices. Therefore the exact labelled count is
  \[
  \boxed{
  \mathsf F_m^{\rm lab}
  =\prod_{j=1}^{2m-1}(j+1-\kappa_j)
  }
  \qquad(m\ge3).
  \]
  The dual row form is
  \[
  \mathsf F_m^{\rm lab}
  =(m-1)!\prod_{k=1}^{m}(\ell_k-k+1),
  \]
  with the inclusive PG26 cutoffs \(\ell_k\). PG36 and PG62 prove that the
  perfect matchings counted are exactly all relation-compatible,
  equivalently full-optimal, bijections in the fixed scaffold. The formula
  is labelled: indexed gaps and oriented paths are not quotiented by any
  symmetry. Distinct assignments yield distinct canonical dihedral core
  orders rooted at \(n\) with neighbors \(2<3\), so the same value also
  counts the represented dihedral classes by injectivity. The forced zero
  edge, first positive column, both terminal columns, universal-row threshold,
  triple/singleton transition, terminal singleton, cutoff equalities, and
  \(m=3\) are explicit; \(\mathsf F_3^{\rm lab}=36\). This is a
  combinatorial count with no geometric or alternative-scaffold consequence.
- EXACT FERRERS LOG-ASYMPTOTIC THEOREM: define
  \[
  C_{\rm F}=14\log2+6\log3-10\log5-2.
  \]
  The exact PG69 factors satisfy, for every integer \(m\ge3\),
  \[
  1+\log{5\over6}-\log m
  <\log\mathsf F_m^{\rm lab}-(2m\log m+C_{\rm F}m)
  <{9\over4}+\log\bigl(2m(2m+1)\bigr).
  \]
  Consequently
  \[
  \log\mathsf F_m^{\rm lab}
  =2m\log m+C_{\rm F}m+{3\over4}\log m+O(1).
  \]
  The proof first writes each integer factor as an exact floor of the literal
  no-ceiling factor, then compares with
  \(r_{m,j}=j(j+4m)/(j+8m)\). Its product is exactly
  \[
  {(2m-1)!(6m-1)!(8m)!\over(4m)!(10m-1)!},
  \]
  which isolates the \(j/m\to0\) singularity. Monotone integral bounds give
  the displayed all-\(m\) envelope. Stirling gives logarithmic coefficient
  \(-1/2\) for the factorial product, the smooth perturbation converges with
  coefficient zero, and an exact parity reduction plus a jump-inclusive
  dyadic sawtooth estimate gives \(5/4\) for
  \(\sum_j\log(a_{m,j}/c_{m,j})\). The signed direct
  ceiling/no-ceiling delta is instead
  \(-\tfrac34\log m+O(1)\). The ranges \(j\le\sqrt m\),
  \(\sqrt m<j\le m/2\), and \(j>m/2\), exact cutoff hits, the forced and
  first positive factors, both terminal columns, every class modulo five,
  the universal-row threshold, triple/singleton transition, and terminal
  singleton are explicit. This theorem concerns the labelled count. The
  equal cardinality of the represented canonical image is only a corollary
  of prior injectivity, not a quotient; convergence of the bounded remainder
  and every geometric conclusion remain unproved.
- EXACT CLOSING-PG46 CORE-ORDER THEOREM: on \(n=10m+3\), \(m\ge3\), let
  \(\alpha(j)=j\) for \(j<m\), \(\alpha(j)=j+1\) for
  \(m\le j<2m-1\), and \(\alpha(2m-1)=m\). For the corresponding core
  order, the complete maximizing-subset classification is

  \[
  \operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}
  P(U)=\bigl\{\{4m+1,\ldots,10m+3\}\bigr\},
  \]

  and

  \[
  K={572m^3+631m^2+223m+22\over2}.
  \]

  An exhaustive isolated-hole table and compressed-path shortcut budget prove
  uniqueness, and direct block summation proves the score. The exact
  canonical comparison is
  \(K-K_{825}=m^2-6m-4\): improvement exactly for \(m=3,4,5,6\), strict
  worsening for every \(m\ge7\), and no integer equality. In terms of \(n\),
  the difference is \((n^2-66n-211)/100\), so the family retains cubic
  coefficient \(143/500\) and is eventually worse at quadratic order. This
  theorem concerns one explicit order only and has no geometric or global
  optimality consequence.
- EXACT PRECLOSING-PG46 CORE-ORDER THEOREM: on \(n=10m+3\), \(m\ge3\), let
  \(\alpha(j)=j\) for \(j<m\), \(\alpha(j)=j+1\) for
  \(m\le j<2m-2\), \(\alpha(2m-2)=m\), and
  \(\alpha(2m-1)=2m-1\). For the corresponding core order,

  \[
  \operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}
  P(U)=\bigl\{\{4m+1,\ldots,10m+3\}\bigr\},
  \]

  and

  \[
  K={572m^3+631m^2+235m+22\over2}.
  \]

  Seven exhaustive isolated-hole classes and a complete compressed-path
  audit prove uniqueness, including the changed cyclic pair
  \((x_{2m-1},4m+1)\). The exact comparisons are
  \(K-K_{\rm closing}=6m\) and \(K-K_{825}=m^2-4\), so this witness is
  strictly worse than both on every admitted row. It shares cubic and
  quadratic coefficients with closing PG46, retains cubic coefficient
  \(143/500\), and has no geometric or global-optimality consequence.
- EXACT DESCENDING-MIN PG49 THEOREM: retain
  \(\kappa_j=\lceil j(8m+3)/(2(8m+4+j))\rceil\), put
  \(\Delta_j=\kappa_{j+1}-\kappa_j\), and assign the least unused
  admissible path while reading \(j=2m-1,\ldots,1\), with
  \(\alpha_{\min}(0)=0\). The exact invariant is
  \[
  \{\alpha_{\min}(t):j\le t\le2m-1\}
  =[\kappa_j,\kappa_j+2m-1-j],
  \]
  and hence
  \[
  \alpha_{\min}(j)
  =\kappa_j+(1-\Delta_j)(2m-1-j)\quad(1\le j<2m-1),
  \qquad
  \alpha_{\min}(2m-1)=\kappa_{2m-1}.
  \]
  Thus the rule is well defined, bijective, and relation-compatible for every
  \(m\ge3\), without matching enumeration.
- EXACT DESCENDING-MIN CORE-ORDER THEOREM: for this one representative,
  (KPGMIN-9) gives the exact integer floor/positive-part formula
  \[
  K(\tau_m^{\min})=K_{825}(m)+D_m+G_m,
  \]
  where \(D_m\) is the explicit path-connection sum (KPGMIN-4), and \(G_m\)
  is the positive part of the two early-plateau singleton insertion gains
  (KPGMIN-7)--(KPGMIN-8). With
  \(B_m=\{4m+1,\ldots,10m+3\}\), \(\mathcal P_m\) the positive-gain low
  labels, and \(\mathcal Z_m\) the zero-gain low labels, all and only the
  maximizing subsets are
  \[
  B_m\cup\mathcal P_m\cup Z',\qquad Z'\subseteq\mathcal Z_m,
  \]
  so their exact number is \(2^{|\mathcal Z_m|}\). A signed shortcut audit,
  not subset enumeration, proves this equality classification.
- DISPROVED CLAIM: the descending-min PG49 core order does not always have a
  unique maximizing subset. At
  \[
  m=101805057120180546870,\qquad
  j=29025982843749082380,\qquad
  \kappa_j=\kappa_{j+1}=14013559766810587979,
  \]
  the assigned singleton index is \(188597691163422599338\) and the
  \(\lambda_j\) insertion gain is exactly zero. The general
  \(2^{|\mathcal Z_m|}\) formula is therefore essential; bounded zero-free
  ranges do not imply universal uniqueness.
- EXACT DIOPHANTINE CLASSIFICATION AND FILTERED CARDINALITY: for each
  descending-min plateau \(1\le j<m\), the separate equations
  \(L_{m,j}=0\) and \(R_{m,j}=0\) have the unique primitive parametrization
  (KPGZERO-2)--(KPGZERO-6).  Their two literal half-open ceilings are exactly
  the distinct residual windows (KPGZERO-10)--(KPGZERO-14), including the
  allowed left upper endpoint and the three proved-impossible endpoints.
  The finite scale windows are the explicit quadratics
  (KPGZERO-20)--(KPGZERO-21).  Every admitted \(u/w\) is a regular
  convergent of the irreducible cubic root
  \(\xi\in(7/5,10/7)\) of
  \(50+51t-27t^2-24t^3\).  For its convergent \(p_\nu/q_\nu\), with next
  complete quotient \(\alpha_{\nu+1}\),
  (KPGZERO-24a)--(KPGZERO-24b) give exactly
  \[
  \xi-{p_\nu\over q_\nu}
  ={(-1)^\nu\over
    q_\nu^2(\alpha_{\nu+1}+q_{\nu-1}/q_\nu)}
  \]
  and the corresponding signed integer cubic form.  The four distinct
  branch/sign windows in (KPGZERO-24c), the domain and congruence reduction,
  and the rounded radical interval (KPGZERO-24d)--(KPGZERO-24f) give the
  complete arithmetic progression of admitted scales without scanning
  \(m\).  The residue-aware integer discriminant
  \[
  \mathfrak D_{\delta,\nu}
  =\Delta_{\delta,\nu}-(2A_\nu g_*-b_{\delta,\nu})^2
  \]
  is nonnegative exactly when that single convergent is admitted on branch
  \(\delta\), after the stated domain and congruence compatibility checks;
  the ordinary quadratic discriminant alone is insufficient.
  Equation (KPGZERO-23) is an exact bijection after these congruence, domain,
  side, and scale filters.  The giant left witness is reconstructed exactly.
  The primitive \(g=19\) witness
  (KPGZERO-27)--(KPGZERO-30) proves that right holes also exist.
  The filtered convergent fibre \(\mathcal C_m\) in (KPGZERO-31) is
  bijective with \(\mathcal Z_m\), so
  \[
  |\mathcal Z_m|=|\mathcal C_m|,
  \qquad
  \#\operatorname {argmax}P_{\tau_m^{\min}}=2^{|\mathcal C_m|}.
  \]
  The canonical supported family consists exactly of the rows with
  \(\mathcal C_m\ne\varnothing\); it is infinite exactly when the tagged
  convergent/scale set, and equivalently the numerical union of zero labels,
  is infinite. Every fixed primitive direction has only finitely many
  admitted scales, so no finite set of convergent directions can generate an
  infinite filtered family. On the giant left-witness board,
  \(\alpha_{\min}\) has at least two induced-\(K\) maximizers while the
  PG49-star bijection has exactly one, although both are PG49-supported and
  have \(W=T=W_n\). Thus support does not determine induced-\(K\) maximizer
  cardinality. The infinite right conic ray
  \((u,w,g)=(13,9,20t+1)\) is an exact support-only false positive: both
  literal plateau residuals are negative for every \(t\ge0\).
  These are the support-only and fixed-direction no-go theorems
  (KPGZERO-31)--(KPGZERO-41); they use no geometry. For every fixed \(m\),
  \(\mathcal Z_m\) is finite; whether
  \(\bigcup_{m\ge3}\mathcal Z_m\) is finite or infinite remains the explicit
  frequency question for the exact local discriminants in (KPGZERO-24).
  Neither the local criterion nor bounded data decides that alternative.
- EXACT DESCENDING-MIN COMPARISON AND ASYMPTOTIC THEOREM: the value is below
  K825 and preclosing PG46 exactly at \(m=4\), above both at \(m=3\) and every
  \(m\ge5\), above closing PG46 for every \(m\ge3\), and never tied. Its
  cubic coefficient is
  \[
  0.2881683105370884612135112\ldots
  \]
  in \(n^3\), strictly larger than \(143/500\). The exact radical,
  algebraic-root, and logarithmic expression (KPGMIN-34)--(KPGMIN-39) is
  transcendental by Hermite--Lindemann. Therefore the exact score function is
  neither polynomial nor eventual quasipolynomial. These facts concern one
  combinatorial core order and imply no geometric or global optimum.
- EXACT EXPLICIT PG49-STAR FERRERS AND CORE-ORDER THEOREM: on
  \(n=10m+3\), \(m\ge3\), put
  \(q=\lfloor(4m+3)/5\rfloor\) and use the piecewise map (PG110). Its image
  blocks partition every path index, its positive values meet the exact
  Ferrers thresholds, and the cyclic closing value is
  \(q=\kappa_{2m-1}\). For the resulting core order,
  \[
  \operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P(U)
  =\bigl\{B_m\bigr\},
  \qquad B_m=\{4m+1,\ldots,10m+3\},
  \]
  and
  \[
  K={1714m^3+1863m^2+24mq+617m+12q^2+48q+66\over6}.
  \]
  The complete low-gain audit has unique minimum \(28m+12\), and the
  complete compressed-shortcut audit has exact minimum \(12m+4\); both
  roles of the cyclic closure are separate. The five \(m\bmod5\) formulas
  all have coefficient \(857/3000\) in \(n\). This value is strictly below
  K825 and both PG46 values for every \(m\ge3\), with no tie. The theorem is
  fixed-order and combinatorial; it implies no geometric or global optimum.
- EXACT ODD-\(v\) PG49-STAR PARITY THEOREMS: on the distinct
  \(n=10m+8\), \(m\ge1\), branch, put
  \[
  q=\left\lfloor{4m+5\over5}\right\rfloor=\kappa_{2m}
  \]
  and use the a-priori map (PGODD-6). It shifts the residual triples and
  doubleton, reverses only the actual singleton block, and assigns \(P_q\)
  to the genuine closing gap. The five image blocks partition all
  \(2m+1\) path indices. The exact odd local relation is
  \(k\ge\kappa_j\); its extendible support consists of \((0,0)\) and all
  positive-column local edges. Every image of (PGODD-6) is supported,
  including the exact closing equality and the minimum row
  \(\alpha^\circ=(0,2,1)\). Hence the map is a search-free
  Ferrers/PG49-compatible bijection on the whole domain, and
  \[
  W(\sigma_{\alpha^\circ})
  ={(8m+8)(8m+7)\over2}.
  \]
  The unchanged core order has the exact induced-subset classification
  \[
  \operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P(U)
  =\bigl\{\{4m+3,\ldots,10m+8\}\bigr\},
  \]
  and
  \[
  K={1714m^3+4467m^2+24mq+3749m+12q^2+60q+1032\over6}.
  \]
  Nine exhaustive hole classes have unique minimum \(28m+26\). The exact
  shortcut minimum is uniquely \(4\) at \(m=1\), \(30\) at \(m=2\), and
  \(12m+10\) for \(m\ge3\); this is the only boundary exception. The five
  residue branches have coefficient \(857/3000\), and exact subtraction
  proves a strict all-row improvement over same-subsequence K825. These are
  fixed-order combinatorial theorems and imply no angular, geometric, global
  \(K\)-minimality, or global optimum.
- EXACT EVEN-\(v\) RESIDUE-TWO PG49-STAR THEOREM: on the existing
  \(e=2\) scaffold with \(n=10m+2\), \(m\ge1\), put
  \[
  q=\kappa_{2m-1}
  =\left\lceil{(m-1)(4m+1)\over5m+1}\right\rceil
  =\begin{cases}
  0,&m=1,\\
  \lfloor(4m+1)/5\rfloor,&m\ge2,
  \end{cases}
  \]
  and use the pre-score map (PGE2-6). It preserves every non-singleton
  orientation, reverses exactly the complete singleton block, and assigns
  \(P_q\) to the genuine closing gap. Its four image blocks partition all
  \(2m\) path indices. The exact local relation is
  \(k\ge\kappa_j\), and its Hall-extendible support equals the entire local
  board because \(\kappa_0=\kappa_1=0\). Every image is supported, including
  the exact closing equality; at \(m=1\), both relevant ranges are empty and
  \(\alpha^{(2)}_*=(1,0)\). Hence the construction is compatible for every
  \(m\ge1\), and the complete cyclic distance audit gives
  \[
  W(\sigma_{\alpha^{(2)}_*})
  ={(8m+4)(8m+2)\over2}=32m^2+24m+4.
  \]
  This construction theorem itself stops at \(W\). The separate unchanged-
  core theorem (KPGE2-1)--(KPGE2-45) gives the unique induced-subset
  maximizer
  \[
  B_m=\{4m+1,\ldots,10m+2\}
  \]
  and
  \[
  K={1714m^3+1353m^2+24mq+281m+12q^2+36q+30\over6}.
  \]
  Nine exhaustive deletion-gain classes have unique minimum \(5\) at
  \(m=1\) and \(20m+6\) thereafter. Every compressed shortcut is strict;
  the unique minimum is \(1,21,57\) at \(m=1,2,3\) and \(20m+4\) for
  \(m\ge4\). The five regular residue branches have coefficient
  \(857/3000\), with \(m=1\) the sole residual of that branch expansion and
  the all-row formula still exact. Exact subtraction
  proves a strict all-row improvement over both the known residue-two order
  and K825. Neither theorem evaluates an alternative candidate, changes
  production, or infers angular, geometric, global-minimizer, or global-
  optimality conclusions.
- EXACT ODD-\(v\) RESIDUE-TWO PG49-STAR THEOREM: on the other parity branch
  of the same \(e=2\) scaffold, \(n=10m+7\), \(m\ge1\), put
  \[
  q=\kappa_{2m}=\left\lfloor{4m+3\over5}\right\rfloor
  \]
  and use the pre-score map (PGE2ODD-6).  It preserves all \(m+1\) triple
  orientations, reverses the complete block of \(m\) singleton paths, and
  assigns the threshold triple \(P_q\) to the genuine closing gap.  This
  branch has no doubleton.  Its four image blocks partition all \(2m+1\)
  path indices.  The exact local relation is \(k\ge\kappa_j\), and its
  Hall-extendible support equals the full local board because
  \(\kappa_0=\kappa_1=0\).  Every image is supported.  The shifted-triple
  range is empty exactly for \(m=1,2,3\); at \(m=1\),
  \(\alpha^{(2,\mathrm{odd})}_*=(0,2,1)\).  The complete cyclic-distance
  audit gives
  \[
  W(\sigma_{\alpha^{(2,\mathrm{odd})}_*})
  ={(8m+8)(8m+6)\over2}=32m^2+56m+24.
  \]
  This construction theorem itself stops at \(W\). The separate unchanged-
  core theorem (KPGE2ODD-1)--(KPGE2ODD-43) gives the unique induced-subset
  maximizer
  \[
  B_m=\{4m+3,\ldots,10m+7\}
  \]
  and
  \[
  K={1714m^3+3891m^2+24mq+2921m+12q^2+48q+732\over6}.
  \]
  Seven exhaustive deletion-gain classes have unique minimum \(20m+16\),
  and every compressed shortcut is strict; its unique minimum is \(17,49\)
  at \(m=1,2\) and \(20m+14\) for \(m\ge3\). All five residue branches,
  including \(m=1,2,3\), are regular and have coefficient \(857/3000\).
  Exact subtraction proves a strict all-row improvement over both the known
  residue-two order and K825. Neither theorem evaluates an alternative,
  changes construction or production, or implies an angular, geometric,
  global-minimizer, or global-optimality conclusion.
- EXACT MONOTONE THRESHOLD-CLOSING PG46 CORE-ORDER THEOREM: on the same
  \(n=10m+3\), \(m\ge3\), rows, put
  \(q=\lfloor(4m+3)/5\rfloor=\kappa_{2m-1}\) and specialize (PG46) to
  \((q,2m-1)\). The resulting bijection places \(P_q\) in the closing gap
  and leaves every residual path increasing. Its complete maximizer set is
  \[
  \operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P(U)
  =\bigl\{B_m\bigr\},
  \qquad B_m=\{4m+1,\ldots,10m+3\},
  \]
  and
  \[
  K={572m^3+619m^2+8mq+207m+4q^2+16q+22\over2}.
  \]
  The seven deletion-gain classes have unique minimum \(28m+12\), while
  the exhaustive compressed-shortcut audit has unique minimum \(12m+4\).
  The closing low \(\lambda_{2m-1}=2\), retained role \(b_q-L-E_0\), every
  longer cut-crossing arc, and \(m=3\) are separate. All five
  \(m\bmod5\) branches retain coefficient \(143/500\). The exact
  comparisons are
  \[
  K_\uparrow-K_*={m(m-1)(m-2)\over3}>0,
  \]
  \[
  K_\uparrow-K_{825}<0,\qquad
  K_\uparrow-K_{\rm cl}\le0,\qquad
  K_\uparrow-K_{\rm pre}<0,
  \]
  with equality only in the middle comparison at \(m=3\). Since the
  PG49-star and monotone orders differ only on the singleton block, its
  reversal supplies exactly the complete cubic gain
  \((n-3)(n-13)(n-23)/3000\); individual gap deltas have mixed signs. These
  are fixed-order combinatorial results, with no angular, geometric, or
  global-minimizer consequence.
- VERIFIED FACT (FINITE EXACT GENERIC-PATH DIAGNOSTIC): the standalone
  standard-library script in
  ops/TASK-20260717__generic_path_terminal_gap_classification/ scans only
  \((m,k,j)\) at \(m=3,4,9,34\). It directly checks every local one- and
  two-step pair against both exact cutoff formulas, including cyclic
  endpoints, the path-type transition, the complete \(m=3\) relation, and
  the nontrivial equality \((34,11,24)\). It constructs no complete order
  or bijection, imports no project/test helper, and enumerates no path
  permutation. The finite check corroborates rather than proves the all-\(m\)
  theorem.
- VERIFIED FACT (FINITE EXACT EDGE-EXTENDIBILITY DIAGNOSTIC): the sole
  standalone standard-library script in
  ops/TASK-20260717__local_edge_extendibility_classification/ scans only the
  established local edges for \(m=3,4,9,34\). It evaluates the residual Hall
  inequalities, directly constructs exactly one prescribed interval shift
  for each extendible edge, and checks permutation, target, forced zero edge,
  and every resulting Ferrers edge. It also checks the deficient suffix and
  all stated boundary cases. It searches no matching, enumerates no path
  permutation, constructs no cyclic core order, and scores no positional
  pair. The finite check corroborates rather than proves the theorem.
- VERIFIED FACT (FINITE EXACT FULL-SCORE DIAGNOSTIC): the sole standalone
  standard-library script in
  ops/TASK-20260717__relation_compatible_full_score_classification/ scans the
  polynomial local state \((j,k,h)\) for \(m=3,4,9,34\), directly compares
  the symbolic distance-three lists with local words, covers all four path
  transitions and the compatible cyclic closure, and constructs only the two
  sharp PG46 witnesses per row. It enumerates no path permutation or matching
  and imports no project or test helper. The finite check corroborates rather
  than proves the theorem.
- VERIFIED FACT (FINITE EXACT FERRERS-COUNT DIAGNOSTIC): the sole standalone
  standard-library script in
  ops/TASK-20260718__ferrers_bijection_count/ builds the PG49 matrix directly
  from integer cross-multiplied inequalities for \(m=3,\ldots,8\), then
  evaluates its reduced permanent by Ryser inclusion--exclusion over column
  subsets. It independently agrees with both Ferrers products and the fixed
  exact counts \(36,720,21600,725760,46448640,3292047360\). It enumerates no
  path permutation or matching, constructs no cyclic order, scores no pair,
  and imports no project or test helper. The finite check corroborates rather
  than proves the all-\(m\) theorem.
- VERIFIED FACT (FINITE EXACT CLOSING-PG46 K DIAGNOSTIC): the sole standalone
  standard-library script in
  ops/TASK-20260718__pg46_closing_exact_k/ reconstructs only the prescribed
  PG46 order. For \(m=3,\ldots,30\), it independently checks the exact score,
  unique maximizing subset through a max-plus increasing-path DP, every
  isolated-hole gain, and every oriented compressed shortcut arc. Direct
  score/formula comparisons continue through \(m=1000\). It imports no
  project or test helper and enumerates no subsets, permutations, or
  matchings. The bounded computation corroborates rather than proves the
  symbolic theorem.
- VERIFIED FACT (FINITE EXACT PRECLOSING-PG46 K DIAGNOSTIC): the sole
  standalone standard-library script in
  ops/TASK-20260718__pg46_preclosing_exact_k/ reconstructs only the specified
  order. For \(m=3,\ldots,30\), an increasing-path max-plus DP checks the
  exact score, unique tail, every isolated-hole gain, and every oriented
  shortcut arc. Direct score and comparison checks continue through
  \(m=1000\). It enumerates no subsets, permutations, or matchings and imports
  no project or test helper. The finite check corroborates rather than proves
  the symbolic theorem.
- VERIFIED FACT (FINITE EXACT DESCENDING-MIN PG49 K DIAGNOSTIC): the sole
  standalone standard-library script in
  ops/TASK-20260719__ferrers_greedy_exact_k/ compares the literal recursion
  with its closed formula, checks the exact Ferrers suffix invariant, and
  reconstructs only the prescribed core. For \(m=3,\ldots,30\), a max-plus
  increasing-path DP and every oriented shortcut arc check the exact score
  and bounded optimizer; formula and comparison checks continue through
  \(m=1000\). It enumerates no subset, permutation, or matching. Its
  zero-free observation is confined to the checked rows and does not
  contradict the exact much larger zero-gain example.
- VERIFIED FACT (BOUNDED EXACT PG49 ZERO-GAIN DIAGNOSTIC): the sole
  standard-library script in
  ops/TASK-20260719__pg49_zero_gain_classification/ checks literal rows only
  through \(m=500\), direct near-root denominators only through \(10^5\),
  and proposed convergents only through denominator \(10^{200}\) and
  \(g\le200\).  Every reported candidate is accepted by exact integer
  reconstruction, both literal ceilings, and the corresponding literal
  gain.  It reconstructs the giant left witness and finds exact right
  witnesses, reporting 56 left and eight right parameter triples in its
  bounded proposal set.  These counts prove neither absence outside the
  bounds nor global finiteness or infinitude.
- VERIFIED FACT (EXACT PG49/KPGZERO CARDINALITY DISCRIMINANTS): the
  standalone standard-library script in
  ops/TASK-20260723__pg49_kpgzero_filtered_cardinality/exact_diagnostic.py
  uses only exact integers and rational cubic signs. It checks an inclusive
  PG49 boundary, directly scores every unordered pair of one supported
  \(m=34\) core, checks discriminating rows of the infinite unfiltered conic
  ray, accepts both filtered branches and both one-sided signs on the left
  branch, rejects adjacent congruent scales, and distinguishes
  \(\alpha_{\min}\) from PG49-star on the same giant board. It enumerates no
  matching, subset, path assignment, or permutation family. The finite
  discriminants corroborate the exact support/filter separation; they do not
  decide (KPGZERO-24).
- VERIFIED FACT (FIXED LOCAL-CF FORMULA FALSIFICATION): the standalone
  standard-library script in
  ops/TASK-20260723__kpgzero_local_cf_criterion/exact_diagnostic.py uses only
  exact integer and rational arithmetic. It generates no convergent and
  scans neither \(m\) nor \(g\). Five fixed convergents check the generic
  complete-tail identity, sign parity, all four branch/sign quadratics,
  three singleton scale fibres, an exact residue-class miss, and a positive
  ordinary discriminant with no positive integer scale. Literal ceiling
  residuals \(-1,0,D-1,D\) check both half-open boundaries. These finite
  checks can falsify the formulas but do not prove them or decide the global
  alternative (KPGZERO-24).
- VERIFIED FACT (FINITE EXACT PG49-STAR K DIAGNOSTIC): the sole standalone
  standard-library script in
  ops/TASK-20260719__explicit_pg49_star_exact_k/ directly constructs only
  the prescribed assignment. On \(m=3,\ldots,30\), its increasing-path
  max-plus DP checks the exact score and unique backbone, while an
  all-oriented-arc audit checks every hole and shortcut, including the cyclic
  cut. It performs 36,989,498 max-plus transitions and checks all 958,916
  proper oriented arcs, including every nontrivial shortcut. Ferrers,
  formula, and comparator checks continue through \(m=1000\). It enumerates
  no subset, path permutation, or matching. The finite check corroborates
  rather than proves the symbolic theorem.
- VERIFIED FACT (BOUNDED EXACT ODD-\(v\) PG49-STAR \(W\) DIAGNOSTIC): the
  sole standalone integer script in
  ops/TASK-20260719__pg49_star_parity_w/ constructs only the prescribed map
  (PGODD-6). Formula, image, and Ferrers checks cover
  \(m=1,\ldots,1000\); direct local-word and residual-Hall checks cover
  \(m=1,\ldots,40\); and exact all-pairs cyclic scoring covers
  \(m=1,\ldots,80\). It checks 8,906,280 unordered pairs and enumerates no
  alternative order, matching, path permutation, or subset. The bounded
  computation corroborates rather than proves the all-domain theorem.
- VERIFIED FACT (BOUNDED EXACT EVEN-\(v\) RESIDUE-TWO PG49-STAR \(W\)
  DIAGNOSTIC): the sole standalone standard-library script in
  ops/TASK-20260720__residue_two_pg49_star_w/ constructs only (PGE2-6).
  Formula, image, threshold, and Ferrers checks cover
  \(m=1,\ldots,1000\); literal local-word and residual-Hall checks cover
  \(m=1,\ldots,40\); and exact all-pairs cyclic scoring covers
  \(m=1,\ldots,80\). It checks 8,710,200 unordered pairs and searches no
  candidate, matching, path permutation, order family, or subset. It
  computes no \(K\) and imports no project or test helper. The bounded
  computation corroborates rather than proves the all-domain theorem.
- VERIFIED FACT (BOUNDED EXACT ODD-\(v\) RESIDUE-TWO PG49-STAR \(W\)
  DIAGNOSTIC): the sole standalone standard-library script in
  ops/TASK-20260720__residue_two_odd_v_pg49_star_w/ constructs only
  (PGE2ODD-6). Formula, image, orientation, empty-range, and Ferrers checks
  cover \(m=1,\ldots,1000\); literal local-word and residual-Hall checks
  cover \(m=1,\ldots,40\); and exact all-pairs cyclic scoring covers
  \(m=1,\ldots,80\). It checks 8,873,400 unordered pairs and searches no
  candidate, matching, path assignment, order family, or subset. It computes
  no \(K\) and imports no project or test helper. The bounded computation
  corroborates rather than proves the all-domain theorem.
- VERIFIED FACT (BOUNDED EXACT CANONICAL EVEN-\(v\), \(e=5\) PATH/GAP
  SUPPORT DIAGNOSTIC): the sole standalone standard-library script in
  ops/TASK-20260720__canonical_e5_even_path_gap_support/ reconstructs the
  literal scaffold directly on \(m=2,\ldots,40\). It checks 88,556 local
  path/gap incidences, 69,124 local Ferrers edges, 4,132,070 residual suffix
  Hall inequalities, 67,525 extendible edges, and all 1,599 zero-column
  obstructions. It verifies the minimum row, empty singleton range, genuine
  cyclic word, inclusive cutoff equality, global induced \(2K_2\), and
  reduced Ferrers nesting. It constructs no complete path assignment,
  searches no matching or permutation, computes no \(K\), and imports no
  project or test helper. The bounded computation corroborates rather than
  proves the all-domain theorem.
- VERIFIED FACT (BOUNDED EXACT CANONICAL ODD-\(v\), \(e=5\) PATH/GAP
  SUPPORT DIAGNOSTIC): the sole standalone standard-library script in
  ops/TASK-20260721__canonical_e5_odd_path_gap_support/ reconstructs the
  literal scaffold directly on \(m=1,\ldots,30\). It checks 39,710 local
  path/gap incidences, 30,948 local Ferrers edges, 1,408,738 residual suffix
  Hall inequalities, 30,018 extendible edges, and all 930 zero-column
  obstructions. It also checks the minimum row, empty singleton range,
  genuine cyclic threshold split, four exact distance classes, induced
  \(2K_2\), and reduced Ferrers nesting. Independently, exhaustive scoring
  of all 5,166 scaffold bijections for \(m=1,2,3\) finds exactly 158 with
  \(W=W_n\), precisely the locally compatible ones, and recovers the full
  support. It computes no \(K\), imports no project/test helper, and is
  bounded corroboration rather than an all-domain proof.
- VERIFIED FACT (FINITE EXACT ODD-\(v\) PG49-STAR \(K\) DIAGNOSTIC): the
  sole standalone standard-library script in
  ops/TASK-20260719__pgodd_exact_k/ constructs only (PGODD-6). On
  \(m=1,\ldots,30\), its independent max-plus DP checks the exact score and
  unique backbone through 39,461,580 transitions. A separate all-arcs audit
  checks 1,007,210 proper oriented arcs, including 1,000,460 nontrivial
  compressed shortcuts and every cyclic-cut arc. Formula, residue, boundary,
  and K825 checks continue through \(m=1000\). It enumerates no subset, path
  permutation, matching, or order family. The bounded computation
  corroborates rather than proves the symbolic theorem.
- VERIFIED FACT (FINITE EXACT EVEN-\(v\) RESIDUE-TWO PG49-STAR \(K\)
  DIAGNOSTIC): the sole standalone standard-library script in
  ops/TASK-20260720__residue_two_pg49_star_k/ constructs only (PGE2-6).
  On \(m=1,\ldots,30\), its independent max-plus DP checks the exact score
  and unique backbone through 36,511,800 transitions. A separate audit
  checks 1,830 deletion gains and all 950,150 proper oriented arcs, including
  943,640 nontrivial compressed shortcuts, the exact arc-budget identity,
  and the cyclic cut. Formula, residual, boundary, residue-two, and K825
  checks continue through \(m=1000\). It enumerates no subset, matching,
  path permutation, or order family. The bounded computation corroborates
  rather than proves the symbolic theorem.
- VERIFIED FACT (FINITE EXACT ODD-\(v\) RESIDUE-TWO PG49-STAR \(K\)
  DIAGNOSTIC): the sole standalone standard-library script in
  ops/TASK-20260720__residue_two_odd_v_pg49_star_k/ constructs only
  (PGE2ODD-6). On \(m=1,\ldots,30\), its independent max-plus DP checks the
  exact score and unique backbone through 38,957,975 transitions. A separate
  audit checks 1,890 cancellation gains and all 997,550 proper oriented arcs,
  including 990,830 nontrivial compressed shortcuts, the exact arc-budget
  identity, and the cyclic cut. Formula, all five regular residue branches,
  \(m=1,2,3\), residue-two, and K825 checks continue through \(m=1000\). It
  enumerates no subset, matching, path assignment, path permutation, or order
  family. The bounded computation corroborates rather than proves the
  symbolic theorem.
- VERIFIED FACT (FINITE EXACT MONOTONE THRESHOLD-CLOSING K DIAGNOSTIC): the
  sole standalone standard-library script in
  ops/TASK-20260719__pg46_threshold_closing_exact_k/ directly constructs
  only \(\alpha_{q,2m-1}\). For \(m=3,\ldots,30\), its increasing-path
  max-plus DP checks the exact score and unique backbone, while its
  all-oriented-arc audit checks every low gain and compressed shortcut,
  including the cyclic cut. It performs 36,989,498 DP transitions and checks
  958,916 proper oriented arcs. Formula, residue, Ferrers, inversion, and
  comparator checks continue through \(m=1000\). It enumerates no subset,
  path permutation, matching, or order family. This finite result
  corroborates rather than proves the all-\(m\) theorem.
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
- VERIFIED FACT: `python-flint==0.9.0` is an optional test dependency, not a
  runtime dependency or supported production verifier backend. The checked
  `n=3` Arb cross-check uses a fixed 384-bit working precision and skips only
  when that optional top-level module is absent; native import failures remain
  failures.
- VERIFIED FACT (WORKFLOW CONFIGURATION): `.github/workflows/verification.yml` defines a GitHub Actions workflow for Python `3.11`, `3.12`, and `3.13` that installs package test and crosscheck extras, runs the full test suite, runs checked-artifact semantic verification, runs schema validation tests, and scans tracked text files for trailing whitespace.
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
- HISTORICAL HOSTED VERIFIED FACT (PRE-CORRECTION KRPGE5 BASELINE): GitHub Actions
  `Verification` run
  [`29771633257`](https://github.com/falker47/ringmin-squared/actions/runs/29771633257)
  completed successfully for push commit
  `bce6e4d8a935bd9d8509e59b760cf78c345779b6`; its Python 3.11, 3.12, and
  3.13 jobs and all recorded workflow steps succeeded. This hosted result
  covers exactly that KRPGE5-1--KRPGE5-32 baseline commit and is not evidence
  for any later commit.
- HOSTED VERIFIED FACT (ACCEPTED KRPGE5 BASELINE): GitHub Actions
  `Verification` run
  [`29777676234`](https://github.com/falker47/ringmin-squared/actions/runs/29777676234)
  completed successfully for push commit
  `a15a4d34cc034b669f02382e2e4f27b4822ed382`; its Python 3.11, 3.12, and
  3.13 jobs all completed successfully, including full pytest,
  checked-artifact verification, focused schema validation, and tracked-text
  trailing-whitespace checks. The run is associated exactly with the accepted
  KRPGE5-1--KRPGE5-36 baseline; no result from `bce6e4d8...` is reused for
  that provenance claim.
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

## Roadmap Pointer

Current priorities live only in `research/NEXT_RESEARCH_STEPS.md`; this stable-memory file does not rank tasks.

## Proof Obligations And Limitations

- CLOSED PROOF OBLIGATION: the fixed-order angular/STN equivalence and
  endpoint semantics are proved in `research/FIXED_ORDER_ANGULAR_STN.md`.
- LIMITATION: the current certified finite results depend on the documented
  guarded `mpmath.iv` interval-backend contract; backend trust/provenance
  remains a production-review item. The test-only Arb cross-check covers
  checked `n=3` only and is not a full independent backend audit.
- LIMITATION: finite computation for `n=3..6` is not proof for all `n`.
- LIMITATION: no exact geometric optimum value \(R_2^*(n)\) has been proved
  in this repository; the exact all-\(n\) classification of the combinatorial
  surrogate \(W_n\) is a different statement.
- LIMITATION: no upper bound for the original geometric problem matching the
  current all-fixed-\(k\) lower coefficient has been proved in this
  repository. This does not contradict the exact supremum classification of
  the continuous finite-prefix template family.
- LIMITATION: the later indices \(n\ge94\) with strict distance-two/full
  minimizer inclusion have not been classified.
- LIMITATION: neither existence of \(\lim R_2^*(n)/n^3\) nor a leading-term
  asymptotic formula has been proved in this repository.
- LIMITATION: the uniform consecutive-tail comparison classifies every
  sublinear block length. The one-prefix CR28ax--CR28bg specialization is
  jointly optimized over all constant densities, and CR28bw is now globally
  optimized over all five two-prefix parameters. The three-, four-, and
  five-prefix extensions remain individually globally optimized, while the
  new clipped Bellman theorem globally classifies every finite-prefix compact
  closure at once.
  The rational five-prefix point remains the separate finite witness. Finite
  rounding at the irrational two-, four-, and five-prefix optimizers, the exact
  residual and exact leading coefficient of the selected block, and
  linear-density methods outside these templates remain unclassified. The
  irrational three-prefix optimizer has the exact finite theorem recorded
  above.
- LIMITATION: both the normalized simplex and the separate combined-height
  one-use theorem are proved for every fixed finite \(k\). Their pointwise
  validity gives no threshold, rounding, error, or parameter control uniform
  in a growing \(k=k(n)\) and no interchange between \(k\) and \(n\). The
  all-fixed-\(k\) corollary needs neither: it takes the supremum only after
  proving the liminf inequality separately at each fixed \(k\). It gives no
  common finite rounding threshold at the unattained supremum coefficient.
- LIMITATION: no Ringmin result should be silently generalized to quadratic radii.
- LIMITATION: the sufficient radius-one threshold `12` is not known to be
  minimal, and the exact equality question remains open for `n<=11`.

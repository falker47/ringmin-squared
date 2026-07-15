# Fixed-Order Angular Feasibility And STN Certificate Semantics

Date: 2026-07-14

## Scope And Evidence Classification

This is the authoritative proof note for the fixed-order angular and simple
temporal network (STN) semantics used by Power-Ringmin. It discharges the
mathematical proof obligations left open in
ops/TASK-20260711__interval_verifier_semantics/DESIGN.md.

- **DEFINITION:** the exact statements below concern real arithmetic, positive
  peripheral radii, a positive central radius, and one fixed labelled cyclic
  order of at least three peripheral circles.
- **EXACT THEOREM:** the geometric all-pairs non-overlap constraints are
  equivalent to the difference constraints and directed STN edges used by the
  repository.
- **EXACT THEOREM:** STN feasibility is equivalent to the absence of a
  negative directed cycle, and shortest-path distances recover a feasible
  potential.
- **EXACT THEOREM:** the angular constraints, STN edge weights, cycle weights,
  and fixed-witness slacks have the radius dependence proved below.
- **CONDITIONAL COMPUTER-CERTIFIED RESULT:** applying these exact implications
  to a serialized interval record is conditional on the angular oracle and its
  subsequent bound arithmetic providing the claimed outward enclosures.
- **LIMITATION:** this note proves no exact numerical threshold, creates no
  certificate, and does not independently audit mpmath.iv.

The proofs are independent of upstream Ringmin results. The present source
inspection confirms that the formulas and edge orientation match the current
Power-Ringmin implementation; source inspection is not a proof that a numeric
backend rounds outward.

## 1. Exact Two-Circle Angular Constraint

Let the central circle have radius \(R>0\), and let two peripheral circles
have radii \(a,b>0\). Their centers lie at distances \(R+a\) and \(R+b\) from
the central center. If their oriented angular difference is
\(\delta\in[0,\tau]\), where \(\tau=2\pi\), then their squared center distance
is

\[
d^2
=(a-b)^2+4(R+a)(R+b)\sin^2(\delta/2).
\tag{AS1}
\]

Since

\[
(a+b)^2=(a-b)^2+4ab,
\tag{AS2}
\]

the two closed disks have disjoint interiors, equivalently \(d\ge a+b\), if
and only if

\[
\sin^2(\delta/2)
\ge {ab\over(R+a)(R+b)}.
\tag{AS3}
\]

Put

\[
x_R(a,b)
=\sqrt{{ab\over(R+a)(R+b)}}.
\tag{AS4}
\]

Because \(R,a,b>0\), one has \(0<x_R(a,b)<1\). On
\(\delta\in[0,\tau]\), the exact solution set of (AS3) is therefore

\[
\theta_R(a,b)\le\delta\le\tau-\theta_R(a,b),
\qquad
\theta_R(a,b)=2\arcsin x_R(a,b),
\tag{AS5}
\]

with \(0<\theta_R(a,b)<\pi\). Equality is permitted: it means external
tangency of the two peripheral circles. For quadratic radii \(a=i^2\) and
\(b=j^2\), this becomes

\[
\theta_R(i^2,j^2)
=2\arcsin\!\left(
{ij\over\sqrt{(R+i^2)(R+j^2)}}
\right).
\tag{AS6}
\]

Thus (AS5) is an exact geometric equivalence, not a small-angle
approximation.

## 2. A Fixed Cyclic Order

Fix \(m\ge3\) labelled positive radii in counterclockwise cyclic order,

\[
\sigma=(r_0,r_1,\ldots,r_{m-1}).
\tag{AS7}
\]

Rotation of the whole configuration is immaterial, so choose lifted angular
coordinates with \(p_0=0\). For every \(0\le i<j<m\), write

\[
\Delta_{ij}=p_j-p_i.
\tag{AS8}
\]

The exact fixed-order all-pairs system is

\[
\theta_{ij}(R)
\le p_j-p_i
\le \tau-\theta_{ij}(R),
\qquad
\theta_{ij}(R)=\theta_R(r_i,r_j),
\tag{AS9}
\]

for every \(i<j\). These constraints include non-adjacent pairs.

The pairs \((0,j)\) in (AS9) give \(0<p_j<\tau\), and all remaining lower
bounds give \(p_i<p_j\) whenever \(i<j\). Hence any solution of (AS9)
automatically satisfies

\[
0=p_0<p_1<\cdots<p_{m-1}<\tau
\tag{AS10}
\]

and realizes the prescribed cyclic order. Conversely, any geometric
configuration in that order has a unique lift satisfying (AS10), after a
rotation, and (AS5) gives every inequality in (AS9).

**Exact fixed-order geometry theorem.** A vector \(p\) with
\(0=p_0<p_1<\cdots<p_{m-1}<\tau\) satisfies (AS9) if and only if placing the
center of circle \(i\) at

\[
(R+r_i)(\cos p_i,\sin p_i)
\tag{AS11}
\]

makes every peripheral pair have disjoint interiors while every peripheral
circle remains externally tangent to the central circle.

The condition \(m\ge3\) is the scope enforced by the local interval verifier.
For \(m=1\) or \(m=2\), the positive-radius threshold behavior at \(R=0\)
is different and is not part of the certificate format.

## 3. Difference Constraints And Directed Edges

Use the standard convention that a directed edge \(u\to v\) of weight \(w\)
encodes

\[
p_v-p_u\le w.
\tag{AS12}
\]

For each \(i<j\), (AS9) is exactly the following pair of edges:

\[
\begin{array}{lll}
j\longrightarrow i,
&w^-_{ji}(R)=-\theta_{ij}(R),
&\texttt{forward\_lower},\\[2mm]
i\longrightarrow j,
&w^+_{ij}(R)=\tau-\theta_{ij}(R),
&\texttt{wrap\_upper}.
\end{array}
\tag{AS13}
\]

Indeed, the first edge is \(p_i-p_j\le-\theta_{ij}\), while the second is
\(p_j-p_i\le\tau-\theta_{ij}\). This is precisely the orientation used by
evaluator.py, highprec.py, interval_verifier.py, and
interval_bracket_exporter.py.

### Negative-cycle criterion

Let \(G_R(\sigma)\) be the graph in (AS13). If a potential \(p\) satisfies
all edges, summing (AS12) around any directed cycle \(C\) telescopes to

\[
0\le W_C(R),
\qquad
W_C(R)=\sum_{e\in C}w_e(R).
\tag{AS14}
\]

Thus a negative directed cycle makes the STN infeasible.

Conversely, suppose there is no negative directed cycle. Add a super-source
with zero-weight edges to every vertex, and let \(d(v)\) be the shortest-path
distance to \(v\). Shortest paths are finite and satisfy, for every edge
\(u\to v\),

\[
d(v)\le d(u)+w_{uv}.
\tag{AS15}
\]

Therefore \(p_v=d(v)-d(0)\) is anchored by \(p_0=0\) and satisfies every
difference constraint. This proves

\[
G_R(\sigma)\text{ is feasible}
\quad\Longleftrightarrow\quad
G_R(\sigma)\text{ has no negative directed cycle}.
\tag{AS16}
\]

The graph in (AS13) is already strongly connected. Consequently one may use
shortest distances from vertex \(0\) directly:

\[
p_k=\operatorname{dist}(0,k).
\tag{AS17}
\]

This is the potential-recovery rule used after Floyd--Warshall closure in the
current float64 and high-precision proposal code. A closed distance matrix has
a negative diagonal entry exactly when a negative cycle is present in exact
arithmetic. The tolerances in evaluator.py and highprec.py make those modules
numerical proposal and cross-check paths; they are not interval certifiers.

## 4. Dependence On The Central Radius

From (AS4),

\[
{x_R'(a,b)\over x_R(a,b)}
=-{1\over2}\left({1\over R+a}+{1\over R+b}\right).
\tag{AS18}
\]

Differentiating (AS5) gives

\[
{d\over dR}\theta_R(a,b)
=-{x_R(a,b)\over\sqrt{1-x_R(a,b)^2}}
\left({1\over R+a}+{1\over R+b}\right)<0.
\tag{AS19}
\]

Hence \(\theta_R(a,b)\) is continuous, indeed real analytic, and strictly
decreasing on \(R>0\). Its endpoint limits are

\[
\lim_{R\downarrow0}\theta_R(a,b)=\pi,
\qquad
\lim_{R\to\infty}\theta_R(a,b)=0.
\tag{AS20}
\]

Both edge weights in (AS13) are consequently continuous and strictly
increasing in \(R\). The constraints loosen as \(R\) increases. In
particular:

- if one potential is feasible at \(R\), the same potential is feasible at
  every \(R'\ge R\);
- if one directed cycle is negative at \(R\), the same cycle is negative at
  every \(0<R'\le R\).

More explicitly, if \(C\) has \(q(C)\) wrap-upper edges, then

\[
W_C(R)
=q(C)\tau-\sum_{e\in C}\theta_e(R),
\tag{AS21}
\]

where pair angles are counted with their cycle multiplicities. Every directed
cycle has \(q(C)\ge1\), because lower edges strictly decrease the vertex index
and cannot close a cycle by themselves. Thus each fixed cycle weight is
continuous and strictly increasing.

### Fixed-order feasible-radius set

Define, without assuming a minimizer,

\[
F_\sigma
=\{R>0:G_R(\sigma)\text{ is feasible}\},
\qquad
\rho_\sigma=\inf F_\sigma.
\tag{AS22}
\]

The set is nonempty: for sufficiently large \(R\), every pair angle is less
than \(2\pi/m\), and the equally spaced potential \(p_i=2\pi i/m\) satisfies
all pairs. It is upper-closed by monotonicity.

For completeness, fixed-order attainment need not be assumed either. It
follows from the same finite STN. A negative closed walk contains a negative
simple cycle, so feasibility is equivalent to nonnegativity of the finite set
of simple directed-cycle weights. Define

\[
\gamma_\sigma(R)=\min_C W_C(R),
\tag{AS23}
\]

where \(C\) ranges over the nontrivial simple directed cycles. This is the
minimum of finitely many continuous, strictly increasing functions. It is
itself continuous and strictly increasing: for \(R_2>R_1\), the minimum over
the finite cycle set of \(W_C(R_2)-W_C(R_1)\) is positive.

Near \(R=0\), the cycle

\[
0\longrightarrow m-1\longrightarrow m-2
\longrightarrow\cdots\longrightarrow1\longrightarrow0
\tag{AS24}
\]

has one wrap edge and \(m-1\) lower edges, and its weight tends to
\((2-m)\pi<0\). Every simple cycle tends at \(R\to\infty\) to
\(q(C)\tau>0\). Therefore \(\gamma_\sigma\) has a unique zero
\(\rho_\sigma>0\), and

\[
F_\sigma=[\rho_\sigma,\infty).
\tag{AS25}
\]

The bracket implications below are nevertheless proved directly from the
infimum definition in (AS22); they do not rely on an unproved optimum or on
knowing \(\rho_\sigma\) exactly.

## 5. Interval Enclosures

Assume an angular oracle supplies real enclosures

\[
\underline\theta_{ij}(R)
\le\theta_{ij}(R)
\le\overline\theta_{ij}(R),
\qquad
\underline\tau\le\tau\le\overline\tau.
\tag{AS26}
\]

Everything in Sections 1--4 is unconditional real mathematics. Everything in
this section is a valid implication **provided (AS26) is true**.

### 5.1 Strict lower-endpoint certificate

At a proposed lower endpoint \(L>0\), replace each true edge weight by the
following upper bound:

\[
\overline w^-_{ji}(L)
=-\underline\theta_{ij}(L),
\qquad
\overline w^+_{ij}(L)
=\overline\tau-\underline\theta_{ij}(L).
\tag{AS27}
\]

The inequalities in (AS26) give

\[
w_e(L)\le\overline w_e(L)
\tag{AS28}
\]

for both edge kinds. Thus (AS27) defines a deliberately relaxed STN. For an
explicit connected directed cycle \(C\), let

\[
S_C^{\mathrm{up}}(L)
=\sum_{e\in C}\overline w_e(L).
\tag{AS29}
\]

The decisive lower sign condition required by the verifier is

\[
S_C^{\mathrm{up}}(L)<0.
\tag{AS30}
\]

If (AS30) is established and the remaining record checks pass, the true cycle
satisfies \(W_C(L)\le S_C^{\mathrm{up}}(L)<0\). Hence

\[
L\notin F_\sigma,
\qquad
(0,L]\cap F_\sigma=\varnothing.
\tag{AS31}
\]

Because \(W_C\) is continuous and strictly negative at \(L\), the same true
cycle remains negative on some right neighborhood of \(L\). Consequently

\[
\rho_\sigma>L.
\tag{AS32}
\]

A computed sum upper bound equal to zero, or an interval sum containing zero,
does not prove a negative cycle and must be rejected. The strictness belongs
only to the lower certificate. A lower negative cycle is an infeasibility
witness at and below the endpoint; it is not an exact active-contact graph at
the unknown threshold.

### 5.2 Closed upper-endpoint witness

At a proposed upper endpoint \(U>0\), the current artifact contains exact
decimal-string positions \(p_i\), anchored by \(p_0=0\). For every \(i<j\),
the verifier computes the conservative slack lower bounds

\[
\underline s^-_{ij}(U)
=(p_j-p_i)-\overline\theta_{ij}(U),
\tag{AS33}
\]

and

\[
\underline s^+_{ij}(U)
=\underline\tau-\overline\theta_{ij}(U)-(p_j-p_i).
\tag{AS34}
\]

If

\[
\min_{i<j}
\min\{\underline s^-_{ij}(U),\underline s^+_{ij}(U)\}
\ge0,
\tag{AS35}
\]

then every true slack is nonnegative. By the geometric equivalence, the
stored positions give an all-pairs feasible configuration at \(U\). Therefore

\[
U\in F_\sigma,
\qquad
[U,\infty)\subseteq F_\sigma,
\qquad
\rho_\sigma\le U.
\tag{AS36}
\]

Zero is accepted in (AS35) because peripheral tangency is allowed and the
geometric constraints are closed. A positive lower bound is operationally
more robust and, by continuity, proves that the same witness remains feasible
on some left neighborhood of \(U\), hence \(\rho_\sigma<U\). With a merely
nonnegative lower bound, one must retain the possibility
\(\rho_\sigma=U\).

### 5.3 Exact local bracket meaning

Combining (AS32) and (AS36), a verified local record proves

\[
\boxed{\rho_\sigma\in(L,U]}.
\tag{AS37}
\]

Equivalently, \(L\) is excluded and \(U\) is included in the feasible-radius
semantics. The open/closed statement is about what is proved at the two
endpoints; it is not an exact threshold claim. It also implies that a sound
verified record cannot have \(L=U\).

The verifier recomputes the cycle sum and witness slacks. The serialized
lower_negative_cycle_sum_upper may not understate the recomputed upper bound,
and the serialized min_upper_witness_slack_lower may not overstate the
recomputed lower bound. More precisely, if \(C,c\) are the recomputed and
serialized cycle-sum upper bounds, and \(S,s\) are the recomputed and
serialized minimum-slack lower bounds, accepted summary fields satisfy

\[
C\le c<0,
\qquad
0\le s\le S.
\tag{AS37a}
\]

Those reported fields are conservative summaries, not substitutes for
recomputation.

### 5.4 Finite global aggregation

Let \(\Omega_n\) be the finite canonical order space, and suppose every order
\(\sigma\in\Omega_n\) has a verified local record
\((L_\sigma,U_\sigma]\). Define

\[
L_{\mathrm{glob}}
=\min_{\sigma\in\Omega_n}L_\sigma,
\qquad
U_{\mathrm{glob}}
=\min_{\sigma\in\Omega_n}U_\sigma.
\tag{AS38}
\]

The global feasible-radius set and its threshold infimum are

\[
F_n=\bigcup_{\sigma\in\Omega_n}F_\sigma,
\qquad
R_2^*(n)=\inf F_n
=\min_{\sigma\in\Omega_n}\rho_\sigma,
\tag{AS38a}
\]

where the last equality uses the finiteness of \(\Omega_n\). Every order is
infeasible for \(R\le L_{\mathrm{glob}}\), while the order attaining the
finite minimum \(U_{\mathrm{glob}}\) has an explicit feasible witness there.
For every order,
\(\rho_\sigma>L_\sigma\ge L_{\mathrm{glob}}\); finiteness of
\(\Omega_n\) preserves the strict global inequality. Thus

\[
\boxed{R_2^*(n)\in(L_{\mathrm{glob}},U_{\mathrm{glob}}]}
\tag{AS39}
\]

under verified order-space coverage and the interval-backend contract. The
checked small-\(n\) artifacts already encode the lower endpoint with
included: false and the upper endpoint with included: true. Writing a closed
numerical enclosure \([L_{\mathrm{glob}},U_{\mathrm{glob}}]\) is conservative
shorthand only; it must not be read as feasibility of
\(L_{\mathrm{glob}}\).

The current v1 candidate-set convention

\[
\{\sigma:L_\sigma\le U_{\mathrm{glob}}\}
\tag{AS40}
\]

is also deliberately conservative. The strict-continuity theorem would allow
equality \(L_\sigma=U_{\mathrm{glob}}\) to be excluded: then
\(\rho_\sigma>U_{\mathrm{glob}}\ge R_2^*(n)\), so that order cannot minimize
the fixed-order thresholds. This note does not change the v1 algorithm,
checked artifacts, or their derived summaries.

## 6. Correspondence With Current Code

The exact semantics map to the repository as follows.

| Mathematical role | Current implementation | Evidence meaning |
|---|---|---|
| Formula (AS5) | geometry.theta, highprec.theta_mp | float64/high-precision point evaluation |
| Edges (AS13) | evaluator._closed_stn_distances, highprec.closed_stn_mp, exporter _stn_edges | numerical feasibility/proposal paths |
| Potential (AS17) | evaluator.recover_positions, highprec.recover_positions_mp, exporter padded recovery | candidate witness generation |
| Strict lower check (AS30) | interval_verifier._negative_cycle_sum_upper | interval-certified implication under the backend contract |
| Closed upper check (AS35) | interval_verifier._min_witness_slack_lower | interval-certified implication under the backend contract |
| Proposal/verification separation | interval_bracket_exporter then interval_verifier | generator output is not trusted without verifier acceptance |
| Structural diagnostics | critical_structure | lower cycles are endpoint certificates; upper slack rankings are numerical diagnostics |

Floyd--Warshall and Bellman--Ford are used to propose or diagnose the exact
objects proved above. Float64 tolerances and ordinary mpmath precision do not
establish the strict signs required for computer certification.

## 7. Guarded mpmath.iv Trust Boundary

The checked records use MPMathIntervalAngularOracle, recorded as
mpmath_iv_guarded_atan2_v1. Because the local environment does not expose
mpmath.iv.asin, it evaluates

\[
\arcsin x=\operatorname{atan2}(x,\sqrt{1-x^2})
\tag{AS41}
\]

on interval inputs and widens the extracted endpoints by guard_decimal.

The exact theorems prove that genuine enclosures satisfying (AS26), combined
as in (AS27), (AS33), and (AS34), imply the endpoint claims. They do **not**
prove that the current backend actually supplies those enclosures. The present
certificate interpretation assumes all of the following implementation
boundary is conservative:

- mpmath.iv arithmetic and directed endpoint behavior for the operations used
  by the oracle;
- the interval atan2 inverse-sine formulation on the complete certificate
  domain;
- interval endpoint extraction and conversion to mp.mpf;
- decimal parsing at the recorded precision;
- endpoint widening, subsequent scalar mp.mpf sums and differences, and the
  final strict/non-strict comparisons.

guard_decimal supplies an explicit widening margin; it is not a proof of
backend correctness and cannot generally repair an unsound backend. Likewise,
metadata values such as outward_enclosure: true and certification_capable:
true state the contract but do not audit it.

Repository tests exercise sampled containment, metadata refusal, artifact
tampering, strict lower signs, and closed upper signs. A separate bounded
test-only cross-check now reads the checked `n=3` JSON directly and recomputes
its three-edge cycle upper bound and all six witness-slack lower bounds with
384-bit Arb through python-flint, using direct `asin` rather than the
production `atan2` path. It calls neither `MPMathIntervalAngularOracle` nor
its enclosures and obtains a strictly negative cycle upper bound and
nonnegative slack lower bounds with complete one-record coverage.

That bounded cross-check is independent implementation evidence for the
`n=3` endpoint signs, not an audit or proof of Arb/FLINT, its bindings, decimal
conversion, or the test code. It does not cover `n=4,5,6`, provide a machine
proof of rounding, or make the full checked set publication-grade.
Accordingly, the checked \(n=3,4,5,6\) results remain
**computer-certified finite results under the documented guarded mpmath.iv
contract**, with no artifact, schema, bracket, supported production backend,
or certified claim changed.

## 8. Consequences And Non-Consequences

- **EXACT THEOREM:** fixed-order geometric feasibility and the implemented
  all-pairs STN are equivalent.
- **EXACT THEOREM:** negative cycles and feasible shortest-path potentials are
  exact dual feasibility alternatives for this finite difference-constraint
  system.
- **EXACT THEOREM:** strict lower evidence excludes \(L\) and a right
  neighborhood; closed upper evidence includes \(U\).
- **CONDITIONAL COMPUTER-CERTIFIED RESULT:** a verifier-accepted local record
  proves (AS37), and exhaustive finite order coverage proves (AS39), under the
  stated backend contract.
- **WARNING:** a lower negative cycle is not an active contact graph at the
  unknown threshold.
- **WARNING:** upper-witness slack rankings at a finite endpoint are not exact
  active-contact certificates.
- **WARNING:** a bracket proves neither an exact threshold value nor equality
  of thresholds for orders with identical serialized brackets.
- **LIMITATION:** no result here is an all-\(n\) asymptotic theorem, a new
  finite certificate, or a publication-grade independent interval-backend
  audit of the full checked artifact set. The bounded `n=3` Arb cross-check is
  test-only corroborating evidence.
- **EXACT DERIVED THEOREM:**
  `research/FIXED_ORDER_CYCLE_RATIO.md` combines the cycle-weight semantics
  proved here with the accepted angular lower and upper comparisons to define
  \(\Lambda(\sigma)\), prove its strict \(n^2\)-width sandwich around
  \(\rho_\sigma\), and derive the finite-order global version. It now also
  proves that the product ratio is exactly one-wrap saturated and equals an
  induced-subset cyclic product maximum. This does not reduce the exact
  angular STN itself to one-wrap cycle checks and does not change the interval
  endpoint or backend-trust semantics above.

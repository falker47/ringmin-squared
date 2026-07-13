# Next Research Steps

This roadmap synthesizes the checked `n=3..6` certificates, candidate-set
diagnostics, critical-structure analysis, checked-artifact verification tooling
and workflow configuration, the induced-subset all-\(n\) lower bound, and the
exact eventual radius-one insertion theorem, the regular-direction baseline
and zigzag cubic upper bound, and the exact bounded product-distance surrogate
analysis through `n=11`.

As of 2026-07-13, the former asymptotic target
\[
R_2^*(n)=\frac{n^3}{6\pi}(1+o(1))
\]
is a DISPROVED CLAIM. The stronger former target
\[
R_2^*(n)=\frac{n^3}{6\pi}+O(n^2)
\]
is also a DISPROVED CLAIM.

The best leading coefficient obtainable from the specific relaxation
"induced subset plus duplicated-multiset pairing plus
\(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\)" is exactly
\[
\frac{2(\sqrt2-1)}{3\pi}.
\]
This is a method-specific optimality statement, not a matching upper bound and
not a proved exact asymptotic constant for Power-Ringmin.

The zigzag regular-direction construction improves the proved upper coefficient
from \(1/\pi\) to \(1/(2\pi)\), but it still does not match the induced-subset
leading coefficient. That zigzag theorem itself generated no leading-order LP,
new finite certificate, `n=7` certificate, preflight artifact, permutation
optimization, or exhaustive enumeration.

The product-distance surrogate now optimizes the regular-direction sufficient
radius combinatorially. Exact canonical enumeration, deliberately bounded to
`n=3..11`, gives
\[
(W_3,\dots,W_{11})=(6,12,15,20,24,30,36,45,50).
\]
This finite exact result improves on zigzag for every enumerated `n=6..11`,
but it is not an all-`n` formula, a geometric certificate, or a new asymptotic
upper bound without a symbolic order family.

## Evidence Basis

- COMPUTER-CERTIFIED RESULT: checked finite interval certificates exist for
  `n=3,4,5,6` under the documented local interval-verifier semantics and
  guarded `mpmath.iv` backend contract.
- EXACT THEOREM: `research/ALL_N_LOWER_BOUND.md` proves the induced-subset
  lower-bound theorem. In particular, for every `n>=4` and `1<=m<=n-2`,
  \[
  R_2^*(n)\ge \frac{P_{m,n}}{\pi}-n^2,
  \qquad
  P_{m,n}
  =
  \sum_{k=m}^n k(m+n-k)
  =
  \frac{(n-m+1)(m^2+4mn+m+n^2-n)}{6}.
  \]
- EXACT THEOREM: choosing \(m=\lceil(\sqrt2-1)n\rceil\) gives
  \[
  R_2^*(n)
  \ge
  \frac{2(\sqrt2-1)}{3\pi}n^3-O(n^2),
  \]
  and hence
  \[
  \liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}
  \ge
  4(\sqrt2-1)>1.
  \]
- EXACT THEOREM: for \(S=\{s_1<\cdots<s_q\}\), the duplicated-multiset pairing
  bound is
  \[
  A(S)=2\sum_{a=1}^t s_a s_{2t+1-a}
  \quad(q=2t),
  \]
  and
  \[
  A(S)=2\sum_{a=1}^t s_a s_{2t+2-a}+s_{t+1}^2
  \quad(q=2t+1).
  \]
  At fixed \(q\), this is uniquely maximized by the tail
  \(\{n-q+1,\dots,n\}\), so nonconsecutive subsets do not improve this
  relaxation.
- EXACT THEOREM: the discrete maximizers of \(P_{m,n}\) over
  \(1\le m\le n-2\) are characterized by
  \[
  \rho_n=\frac{\sqrt{8n^2+8n+1}-(2n+1)}2.
  \]
  For \(n\ge4\), the unique maximizer is \(\lfloor\rho_n\rfloor+1\) unless
  \(\rho_n\) is an integer, in which case the two maximizers are
  \(\rho_n\) and \(\rho_n+1\).
- EXACT THEOREM: writing \(R^*_{2:n}\) for the infimum central radius of the
  core radii \(2^2,\dots,n^2\),
  \[
  R_2^*(n)=R^*_{2:n}\qquad(n\ge12).
  \]
  The proof uses the exact forbidden-arc insertion criterion
  \(\sum_{j=2}^n\theta_R(1,j^2)<\pi\), rigorous angular majorants, and the
  configuration-level induced-subset lower bound. It proves equality of the
  full and core feasible-radius sets and does not assume a minimizer.
- EXACT THEOREM: for every \(n\ge12\), `research/ALL_N_LOWER_BOUND.md` proves
  the order-independent baseline in which the core uses regular
  \((n-1)\)-gon polar directions and is all-pairs feasible at
  \[
  U_n
  =
  \sqrt{
  n^2(n-1)^2\csc^2\!\left({\pi\over n-1}\right)
  +{(2n-1)^2\over4}}
  -{n^2+(n-1)^2\over2}.
  \]
  The accepted insertion theorem gives \(R_2^*(n)\le U_n\) for \(n\ge12\),
  with \(U_n/n^3\to1/\pi\).
- EXACT THEOREM: for every \(R>0\) and positive \(i,j\),
  \(\theta_R(i^2,j^2)<2ij/R\). For
  \[
  M_n=n\left(\left\lfloor{n\over2}\right\rfloor+1\right),
  \qquad
  V_n={(n-1)M_n\over\pi},
  \]
  the core indices in zigzag order \((n,2,n-1,3,\dots)\) satisfy
  \(ij\le qM_n\) at circular distance \(q\). Thus all core pairs are feasible
  at \(V_n\), the insertion theorem gives \(R_2^*(n)\le V_n\) for \(n\ge12\),
  and
  \[
  \limsup_{n\to\infty}{R_2^*(n)\over n^3}\le {1\over2\pi},
  \qquad
  R_2^*(n)=\Theta(n^3).
  \]
- EXACT THEOREM: `research/PRODUCT_DISTANCE_SURROGATE.md` defines
  \(W(\sigma)=\max ij/d_\sigma(i,j)\), proves strict all-pairs core
  feasibility at \((n-1)W(\sigma)/\pi\), transfers it to the full problem for
  `n>=12`, and proves the tail obstruction
  \[
  W(\sigma)\ge {P_{m,n}\over n-1}
  \qquad(2\le m\le n-2)
  \]
  using induced oriented positional gaps that sum to `n-1`.
- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): exact canonical
  enumeration of `204557` rotation/reflection classes for `n=3..11` gives
  the displayed \(W_n\) values and minimizer counts
  \((1,1,1,2,2,4,12,72,24)\), with representatives and comparisons recorded
  in `research/PRODUCT_DISTANCE_SURROGATE.md`. No floating point, serialized
  artifact, schema, CLI, or geometric certificate is involved.
- VERIFIED FACT: `examples/finite_results_summary_n3_n6.json` derives
  candidate sets, exclusion gaps, repeated serialized bracket groups, and
  small-`n` ratios from the checked finite certificates.
- VERIFIED FACT: `ops/TASK-20260712__critical_constraints_order_structure/critical_structure_n3_n6.json`
  records deterministic critical-structure diagnostics for certified candidate
  orders only.
- LOCAL VERIFIED FACT: successful local tests, checked-artifact verification,
  workflow inspection, and hygiene checks are recorded in
  `ops/TASK-20260712__verification_trust_layer_ci/` and
  `ops/TASK-20260712__cross_platform_finite_hash_ci/`; they do not establish
  hosted GitHub Actions status.
- HISTORICAL USER-REPORTED STATUS: the 2026-07-12 roadmap task recorded a green
  hosted run after the cross-platform fix, but no commit SHA, run identifier,
  URL, or independently inspected result was recorded; it establishes no
  hosted status for a specific commit.
- CURRENT HOSTED STATUS: GitHub Actions for the current `HEAD` has not been
  independently verified.
- LIMITATION: none of the finite certificates proves an exact optimum, a
  coefficient-matching upper bound, or a leading-term asymptotic formula.

## Consequences

1. The induced-subset lower bound supersedes the older full-cycle lower bound
   \(\liminf 6\pi R_2^*(n)/n^3\ge 1\). The older statement remains true but is
   no longer sharp enough to describe the current obstruction.

2. Any future asymptotic upper-bound target must be compatible with
   \[
   \liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}
   \ge
   4(\sqrt2-1)>1.
   \]
   This roadmap deliberately does not propose a new exact constant.

3. The proof uses induced cyclic orders on subsets, not only adjacent pairs in
   the full cyclic order. For any subset \(S\) of at least three indices, the
   induced gaps sum to \(2\pi\), all-pairs feasibility applies to each induced
   adjacent endpoint pair, and the duplicated-multiset pairing lemma supplies
   the product lower bound.

4. The finite tests added with the proof are diagnostic checks only: they
   verify the formula for \(P_{m,n}\), the explicit formula for \(A(S)\), the
   fixed-cardinality optimality of tails by exhaustive small-`n` subset
   enumeration, the integer characterization of the discrete maximizers, the
   zigzag product lemma on a substantial finite interval, and sampled
   geometric all-pairs feasibility. They are not the all-\(n\) proofs.

5. The former reduced-core observation now has an exact eventual consequence:
   for \(n\ge12\), adding radius \(1\) does not change any feasible central
   radius. This does not validate the finite lower-cycle proxy as an exact
   contact graph, does not settle \(n\le11\), and is not based on the checked
   cases \(n=5,6\).

6. The zigzag regular-direction construction sharpens the prior baseline and
   gives the rigorous liminf/limsup bracket
   \[
   {2(\sqrt2-1)\over3\pi}
   \le
   \liminf_{n\to\infty}{R_2^*(n)\over n^3}
   \le
   \limsup_{n\to\infty}{R_2^*(n)\over n^3}
   \le {1\over2\pi}.
   \]
   The upper value is a limsup coefficient, not an exact leading constant; the
   construction does not prove convergence.

7. The product-distance surrogate isolates exactly what the angular majorant
   needs from a regular-direction order. Zigzag has exact surrogate score
   \(M_n\), but bounded enumeration finds strictly smaller scores for every
   `n=6..11`. The best tail obstruction remains strict in all enumerated cases
   where it is defined, so neither comparison identifies an all-`n` optimum.

## Updated Research Questions

- OPEN QUESTION: what upper-bound construction, if any, matches the new
  induced-subset lower obstruction up to lower-order terms?
- OPEN QUESTION: can the previous reduced-core observations at checked
  `n=5,6` be related to the exact feasible-radius-set equality for
  \(n\ge12\), or are their lower-cycle proxies a separate finite phenomenon?
- OPEN QUESTION: is \(12\) the least threshold for
  \(R_2^*(n)=R^*_{2:n}\), or can the remaining \(n\le11\) cases be settled by
  stronger exact estimates or counterexamples?
- OPEN QUESTION: what is the asymptotic behavior of \(W_n/n^2\), and can a
  symbolic regular-direction order family improve the zigzag coefficient?
- OPEN QUESTION: what stronger combinatorial obstruction can narrow the gap
  between the best tail lower obstruction and \(W_n\)?
- OPEN QUESTION: can the fixed-order STN/geometric equivalence, endpoint
  semantics, and negative-cycle proof obligations be recorded independently of
  any particular asymptotic constant?

## Ranked Work

Immediate:

- Document fixed-order angular/STN equivalence and certificate endpoint
  semantics, including monotonicity in `R`, negative-cycle infeasibility,
  upper-witness meaning, and the interval-backend trust boundary.

Next:

- Seek a symbolic order family or stronger obstruction for the
  product-distance surrogate; do not extrapolate a formula from `n<=11`.
- Keep the exact radius-one theorem separate from finite critical-cycle proxy
  claims and from any assumption that an optimum is attained.

Later:

- Replace or independently audit the guarded `mpmath.iv` backend before making
  public production-grade certificate claims.
- Reduce bracket widths or add independent fixed-order analysis for the
  multiple candidates at `n=5,6` if exact tie questions become important.
- Consider larger finite certificates only after a structural prediction gives
  a precise discriminator.
- Revisit whether the sufficient radius-one threshold can be lowered below
  \(12\), using exact inequalities or a genuine counterexample rather than
  finite-certificate extrapolation.

Deliberately deferred:

- `n=7` exhaustive certificate generation.
- Larger exhaustive enumeration without a precise discriminator.
- Product-distance enumeration beyond the explicit `n=11` boundary.
- Leading-order LP work in the induced-subset proof task.
- Any claim that the new lower-bound coefficient is the exact asymptotic
  constant.
- Any claim that the radius-one threshold \(12\) is minimal.

## Recommended Next Atomic Task

Task: document fixed-order angular/STN equivalence and endpoint semantics.

Acceptance criteria:

- state the fixed-order angular constraints and monotonicity in `R` precisely;
- prove the equivalence between geometric feasibility and the STN formulation
  used by the current code;
- document strict lower-endpoint negative-cycle infeasibility and upper-witness
  semantics without overstating endpoint inclusion;
- preserve the local interval-backend trust boundary and evidence
  classifications;
- do not generate new certificates, artifacts, or surrogate enumerations.

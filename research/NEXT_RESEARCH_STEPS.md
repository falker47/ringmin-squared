# Next Research Steps

This roadmap synthesizes the checked `n=3..6` certificates, candidate-set
diagnostics, critical-structure analysis, the checked-artifact verification
pipeline, and the target conjecture

\[
R_2^*(n)=\frac{n^3}{6\pi}(1+o(1)).
\]

As of 2026-07-12, the lower-bound half of the leading constant is proved:
\[
R_2^*(n)\ge \frac{n(n+1)(n+2)}{6\pi}-n^2
\quad(n\ge 3),
\]
and therefore
\[
\liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}\ge 1.
\]
The matching upper-bound direction remains open.

No `n=7` certificate, preflight artifact, or exhaustive enumeration was
generated for this roadmap.

## Evidence Basis

- COMPUTER-CERTIFIED RESULT: checked finite interval certificates exist for
  `n=3,4,5,6` under the documented local interval-verifier semantics and
  guarded `mpmath.iv` backend contract.
- EXACT THEOREM: `research/ALL_N_LOWER_BOUND.md` proves the all-`n`
  adjacent-product lower bound and its consequence
  \(\liminf 6\pi R_2^*(n)/n^3\ge 1\).
- VERIFIED FACT: `examples/finite_results_summary_n3_n6.json` derives
  candidate sets, exclusion gaps, repeated serialized bracket groups, and
  small-`n` ratios from those checked certificates.
- VERIFIED FACT: `ops/TASK-20260712__critical_constraints_order_structure/critical_structure_n3_n6.json`
  records deterministic critical-structure diagnostics for certified candidate
  orders only.
- USER-REPORTED STATUS: after the cross-platform CI fix, hosted GitHub Actions
  is green. This roadmap did not independently query GitHub.
- LIMITATION: none of the finite certificates proves an exact optimum, a
  matching upper bound, or the asymptotic conjecture.

## Answers

1. Mathematical facts now established.

   The all-`n` exact theorem now established is:
   \[
   R_2^*(n)\ge \frac{n(n+1)(n+2)}{6\pi}-n^2
   \quad(n\ge 3),
   \qquad
   \liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}\ge 1.
   \]
   It follows from a rearrangement-pairing bound
   \(\sum_k\sigma_k\sigma_{k+1}\ge n(n+1)(n+2)/6\), the adjacent-gap
   consequence of all-pairs feasibility, and
   \(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\).

   The finite checked facts are:

   | `n` | canonical orders | certified global bracket `(L, U]` | candidate count | excluded count | exclusion gap |
   |---:|---:|---|---:|---:|---|
   | 3 | 1 | `(0.3832870361393696523322205393924377858638763427734375, 0.383487036139369685816546962087159045040607452392578125]` | 1 | 0 | undefined |
   | 4 | 3 | `(1.4955284118749971877804227915476076304912567138671875, 1.4957284118749971657535979829845018684864044189453125]` | 1 | 2 | `0.1171644705802874497635457373689860105514526367187500` |
   | 5 | 12 | `(3.934227717145796443531935437931679189205169677734375, 3.9344277171457964215051106293685734272003173828125]` | 2 | 10 | `0.1137866156209259571596703608520328998565673828125` |
   | 6 | 60 | `(8.4678350760883720482752323732711374759674072265625, 8.4680350760883715821591977146454155445098876953125]` | 5 | 55 | `0.0488707956703002821541304001584649085998535156250` |

   The checked-artifact pipeline now verifies the checked finite certificates,
   embedded local brackets, schema structure, summary freshness, and whitespace
   hygiene in CI. The interval-backend trust limitation remains.

2. Empirical order patterns visible.

   Candidate orders are `[3,1,2]`; `[4,1,3,2]`;
   `[5,1,3,4,2]`, `[5,2,4,1,3]`; and
   `[6,1,2,5,4,3]`, `[6,1,3,4,5,2]`, `[6,2,1,5,4,3]`,
   `[6,2,5,1,4,3]`, `[6,2,5,4,1,3]`.

   The visible pattern is not a single stable full cyclic order. It is a
   recurring reduced lower-cycle core. For `n=5`, both candidates share
   `{2-4, 2-5, 3-4, 3-5}`. For `n=6`, all five candidates share
   `{2-5, 2-6, 3-4, 3-6, 4-5}`. In both multiple-candidate cases, index `1`
   is absent from the lower-cycle core but appears in some upper-witness
   near-critical diagnostics.

   Numerical midpoint ratios to `n^3/(6*pi)` increase from about `0.268` to
   `0.739` over `n=3..6`; this is a small-`n` numerical observation only.

3. Most promising candidate structural lemma.

   The most promising lemma is a reduced-core insertion lemma:

   CONJECTURE: for the relevant large-`n` order family, the leading obstruction
   is a fixed-order all-pairs subsystem supported by indices `2..n`; index `1`
   can be inserted into one of several gaps without changing the leading radius,
   while all constraints incident to index `1` remain either slack or lower-order
   corrections.

   This is stronger and more useful than another finite enumeration because it
   would explain the repeated candidate brackets at `n=5,6`, predict when weakly
   constrained indices appear, and give a proof target tied to the asymptotic
   constant.

4. What is required to prove fixed-order feasibility equivalence.

   A rigorous proof must define, for one cyclic order and radius `R`, angular
   variables around the central circle and all-pairs constraints
   \[
   t_j-t_i \ge \theta_R(r_i,r_j),\qquad
   t_j-t_i \le 2\pi-\theta_R(r_i,r_j)
   \]
   for every pair in the fixed cyclic order, with a normalization such as
   `t_0=0`.

   The proof obligations are:

   - geometric placement implies the STN/difference-constraint system;
   - a feasible STN solution gives a valid geometric placement with the same
     cyclic order and all peripheral interiors disjoint;
   - strict and closed endpoint semantics match the certificate convention;
   - negative cycles are exactly the finite infeasibility certificates for the
     fixed-order STN;
   - monotonicity of every \(\theta_R(r_i,r_j)\) in `R` justifies bisection and
     interval bracketing.

5. What is required to control non-adjacent constraints.

   Adjacent-chain feasibility is not enough. For a proposed structured order,
   every non-adjacent pair `i,j` needs a domination inequality: the available
   angular arc between them, or its complement, must be at least
   \(\theta_R(i^2,j^2)\). In the asymptotic regime this becomes a family of
   weighted interval inequalities with leading weights `ij`.

   The next proof layer should isolate a candidate gap allocation, then prove
   all interval sums dominate the corresponding pair weights with uniform
   error terms. A verifier can test the exact finite inequalities, but the proof
   needs a symbolic or monotone family argument rather than checking one `n` at
   a time.

6. What is required to derive the `n^3/(6*pi)` leading term.

   The lower-bound half is now complete. A plausible route to the full
   asymptotic equality has the remaining pieces:

   - identify a structured order family and adjacent gap allocation whose
     leading adjacent product weight is \(n^3/6+O(n^2)\);
   - convert the angular formula to
     \(\theta_R(i^2,j^2)=2ij/R+O((ij/R)^3+n^2ij/R^2)\) uniformly in the regime
     \(R\asymp n^3\);
   - prove an upper construction whose all-pairs constraints, not just adjacent
     constraints, fit inside \(2\pi\) at
     \(R=n^3/(6\pi)+O(n^2)\) or at least
     \(R=(1+o(1))n^3/(6\pi)\).

   The lower bound does not require separate non-adjacent control because it
   relaxes the full feasible set to adjacent constraints. Non-adjacent control
   is required for the matching upper-bound direction, where a proposed
   placement or fixed-order angle assignment must satisfy every pair.

7. Realistic role for Supnick or anti-Monge reasoning.

   The lower-bound product inequality no longer needs upstream Supnick input:
   it follows locally from a rearrangement pairing relaxation on two copies of
   each index. Supnick/anti-Monge reasoning may still help identify an
   upper-bound order family and prove interval domination inequalities for
   structured arcs.

   It should not be treated as a complete proof of the quadratic-radii problem
   unless it yields a local all-pairs upper-bound construction. Existing
   upstream claims remain proof assets to review, not Power-Ringmin theorems.

8. Evidence for floating or weakly constrained circles.

   The current evidence supports only weakly constrained or candidate-floating
   language. In the checked multiple-candidate cases, index `1` has zero lower
   critical-cycle incidence and minimum combined proxy incidence, so it is
   marked as a possible weakly constrained index for `n=5,6`. This does not
   certify true non-incidence with the exact active constraint set.

   The strongest useful next question is whether index `1` can be removed,
   solved as a reduced subsystem on `2..n`, and reinserted with positive
   all-pairs slack under independently recovered positions.

9. Highest information-gain next experiment.

   Run a reduced-subsystem fixed-order experiment on the existing `n=5,6`
   candidate orders only. Remove index `1`, solve or verify the induced
   subsystem on `2..n`, reinsert index `1` in every candidate gap, and compare:

   - fixed-order lower-cycle cores;
   - full all-pairs feasibility radii;
   - upper-witness slack margins for constraints incident to index `1`;
   - whether repeated serialized brackets persist after isolating the reduced
     subsystem.

   This uses existing checked cases and directly tests the structural lemma.
   It has higher research value than automatic enumeration because it can
   explain why the current certificates have multiple candidates and can produce
   a reusable proof target.

10. When an `n=7` exhaustive certificate is worth its cost.

   An `n=7` exhaustive certificate is worth considering only after the reduced
   analysis produces a precise discriminator. Acceptable triggers include:

   - two explicit order-family conjectures make different `n=7` candidate-order
     predictions;
   - the reduced-core lemma predicts a specific `n=7` candidate-set cardinality;
   - the critical-cycle theory predicts a specific transition in the shared
     lower-cycle core;
   - the weakly constrained index analysis predicts the first appearance of a
     new floating-index pattern that cannot be tested with `n=5,6`.

   The local canonical-order count for `n=7` is `360`, compared with `60` for
   `n=6`, so enumeration is a nontrivial cost. "Because `n=7` is next" is not a
   sufficient reason.

## Ranked Work

Immediate:

- Prove and document the fixed-order STN/geometric equivalence with certificate
  endpoint semantics.
- Run the reduced-subsystem experiment on checked `n=5,6` candidate orders,
  including reinsertion of index `1` and all-pairs slack reporting.
- Formulate a symbolic all-pairs domination target for a candidate
  upper-bound order family at radius \(n^3/(6\pi)+O(n^2)\) or
  \((1+o(1))n^3/(6\pi)\).

Next:

- Turn the reduced-core experiment into a conjecture or disproof with exact
  hypotheses, not just a pattern note.
- Derive symbolic non-adjacent domination inequalities for the leading
  alternating order family.
- Review the upstream Supnick/anti-Monge proof assets only if they are needed
  for a candidate upper-bound family; the all-`n` lower bound is already local.

Later:

- Replace or independently audit the guarded `mpmath.iv` backend before making
  public production-grade certificate claims.
- Reduce bracket widths or add independent fixed-order analysis for the
  multiple candidates at `n=5,6` if exact tie questions become important.
- Build an asymptotic proof scaffold combining product-tour bounds, angular
  error estimates, and non-adjacent domination.

Deliberately deferred:

- `n=7` exhaustive certificate generation.
- Larger exhaustive enumeration without a precise discriminator.
- Exact optimum claims or exact tie claims for `n=5,6`.
- Treating any Ringmin theorem as automatically valid for quadratic radii.

## Recommended Next Atomic Task

Task: formulate and test a candidate all-pairs upper-bound inequality family
for one explicit structured cyclic order.

Why this beats automatic enumeration: the lower-bound constant is now proved,
so the proof bottleneck is whether a concrete order and gap allocation can
satisfy every non-adjacent pair at the same leading radius. Enumeration would
mostly add another finite row unless it is tied to a specific upper-bound
prediction.

Acceptance criteria:

- one explicit order family and gap-allocation rule is stated;
- adjacent gap sums are shown to fit the target radius to leading order;
- every non-adjacent pair is translated into a symbolic interval-sum inequality;
- finite checks are used only as diagnostics, not as an all-`n` proof;
- the result explicitly says whether the candidate upper-bound family is
  supported, falsified, or unresolved;
- durable memory and task evidence are updated without generating `n=7`.

Stopping conditions:

- the fixed-order STN equivalence proof has an unresolved endpoint or wrap
  semantics gap;
- the proposed non-adjacent interval inequalities fail for small symbolic
  subfamilies or checked finite diagnostics;
- angular error terms cannot be made uniform in the target radius regime;
- the only proposed reason to continue is that `n=7` is the next integer.

Remaining risks:

- finite `n=5,6` behavior may not persist asymptotically;
- upper-witness slack proxies may not match exact active constraints;
- the adjacent leading constant may be attainable by a tour but insufficient for
  all-pairs feasibility;
- interval-backend provenance remains a trust limitation for public
  certification claims.

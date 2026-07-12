# Next Research Steps

This roadmap synthesizes the checked `n=3..6` certificates, candidate-set
diagnostics, critical-structure analysis, the checked-artifact verification
pipeline, and the induced-subset all-\(n\) lower bound.

As of 2026-07-12, the former asymptotic target
\[
R_2^*(n)=\frac{n^3}{6\pi}(1+o(1))
\]
is a DISPROVED CLAIM. The stronger former target
\[
R_2^*(n)=\frac{n^3}{6\pi}+O(n^2)
\]
is also a DISPROVED CLAIM.

No upper-bound construction, leading-order LP, new finite certificate, `n=7`
certificate, preflight artifact, or exhaustive enumeration was generated for
this roadmap update.

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
- VERIFIED FACT: `examples/finite_results_summary_n3_n6.json` derives
  candidate sets, exclusion gaps, repeated serialized bracket groups, and
  small-`n` ratios from the checked finite certificates.
- VERIFIED FACT: `ops/TASK-20260712__critical_constraints_order_structure/critical_structure_n3_n6.json`
  records deterministic critical-structure diagnostics for certified candidate
  orders only.
- USER-REPORTED STATUS: after the cross-platform CI fix, hosted GitHub Actions
  was green. This roadmap update did not independently query GitHub.
- LIMITATION: none of the finite certificates proves an exact optimum, a
  matching upper bound, or an asymptotic equality theorem.

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
   verify the formula for \(P_{m,n}\), the moderate-`n` discrete maximizer over
   \(m\), and pairing bounds on some nonconsecutive subsets. They are not the
   all-\(n\) proof.

## Updated Research Questions

- OPEN QUESTION: what upper-bound construction, if any, matches the new
  induced-subset lower obstruction up to lower-order terms?
- OPEN QUESTION: can the previous reduced-core observations at checked
  `n=5,6` be reinterpreted under the induced-subset obstruction, or were they
  artifacts of pursuing the former \(n^3/(6\pi)\) scale?
- OPEN QUESTION: can one identify a structured order family and gap allocation
  whose all-pairs constraints are feasible at a radius scale consistent with
  the new lower bound?
- OPEN QUESTION: do the checked finite brackets for `n=3..6` contain useful
  diagnostics when compared to the best finite induced-subset lower bound
  \(\max_m(P_{m,n}/\pi-n^2)\)?
- OPEN QUESTION: can the fixed-order STN/geometric equivalence, endpoint
  semantics, and negative-cycle proof obligations be recorded independently of
  any particular asymptotic constant?

## Ranked Work

Immediate:

- Compare the checked finite `n=3..6` brackets against the best finite
  induced-subset lower bound as a diagnostic table, without changing their
  certificate classification.
- Revisit the reduced-core fixed-order observations only as structural
  diagnostics, no longer as evidence for the disproved \(n^3/(6\pi)\) target.
- Prove and document the fixed-order STN/geometric equivalence with certificate
  endpoint semantics.

Next:

- Formulate one structured upper-bound order family and gap-allocation rule at
  a radius scale compatible with the induced-subset obstruction.
- Translate every non-adjacent pair for that family into symbolic interval-sum
  inequalities.
- Use finite checks only as diagnostics for those symbolic inequalities, not as
  all-\(n\) proof.

Later:

- Replace or independently audit the guarded `mpmath.iv` backend before making
  public production-grade certificate claims.
- Reduce bracket widths or add independent fixed-order analysis for the
  multiple candidates at `n=5,6` if exact tie questions become important.
- Consider larger finite certificates only after a structural prediction gives
  a precise discriminator.

Deliberately deferred:

- `n=7` exhaustive certificate generation.
- Larger exhaustive enumeration without a precise discriminator.
- Upper-bound construction work in the induced-subset proof task.
- Leading-order LP work in the induced-subset proof task.
- Any claim that the new lower-bound coefficient is the exact asymptotic
  constant.

## Recommended Next Atomic Task

Task: build a small diagnostic comparison between the checked finite `n=3..6`
brackets and the best finite induced-subset lower bound
\(\max_{1\le m\le n-2}(P_{m,n}/\pi-n^2)\).

Acceptance criteria:

- compute the best induced-subset lower bound for `n=3..6` using exact integer
  \(P_{m,n}\) arithmetic and high-precision decimal output;
- compare it with the checked finite lower and upper endpoints without changing
  any finite-certificate classification;
- state clearly that the table is a finite diagnostic, not an all-\(n\) proof
  or an upper-bound construction;
- update durable memory and task evidence without generating new certificates.

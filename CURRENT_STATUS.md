# CURRENT_STATUS - power-ringmin

Last update: 2026-07-14

- **Current phase:** exact minimizer-set boundary for the product-distance
  surrogate.
- **Current task:** prove the first index at which positional distances at
  least three restrict distance-two minimizers.
- **Task dossier:**
  ops/TASK-20260714__first_long_distance_minimizer_restriction/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Exact Result

Let \(\mathcal M_n\) and \(\mathcal M_n^{(\le2)}\) denote the full and
distance-two minimizer sets. The accepted global value theorem remains

\[
W_n^{(\le2)}=B_n=W_n\qquad(n\ge3).
\]

For any cyclic core order, every pair omitted from the distance-two objective
has score

\[
{ij\over q}\le {n(n-1)\over3}
\qquad(q\ge3).
\]

Therefore \(n(n-1)/3\le B_n\) implies
\(\mathcal M_n=\mathcal M_n^{(\le2)}\). Exact evaluation of the bounded
values for \(3\le n\le8\) and the five residue-class formulas for
\(9\le n\le92\) proves

\[
\boxed{
\mathcal M_n=\mathcal M_n^{(\le2)}
\qquad(3\le n\le92)
}.
\]

At \(n=93\), the exact formula gives

\[
d_{93}=76,
\qquad
B_{93}=W_{93}=2850,
\qquad
{93\cdot92\over3}=2852.
\]

Starting from \(\operatorname{eight\_twenty\_fifths\_order}(93)\), delete
label \(54\) from the segment \((92,4,54,3,93)\) and insert it between the
consecutive labels \(16,48\). Exact scoring of the resulting order
\(\tau_{93}\) gives

\[
W^{(\le2)}(\tau_{93})=2850,
\qquad
W(\tau_{93})=2852,
\]

with the full maximum uniquely attained by \((92,93)\) at circular distance
three. Consequently,

\[
\boxed{\mathcal M_{93}\subsetneq\mathcal M_{93}^{(\le2)}}.
\]

EXACT THEOREM: \(93\) is the first index at which distances at least three
restrict the minimizers of the product-distance surrogate. No assertion is
made that strict inclusion persists for every later index; the sufficient
equality criterion holds again at \(n=94\).

## Verification

- CURRENT LOCAL VERIFIED FACT: the two new targeted exact tests pass 2/2.
- CURRENT LOCAL VERIFIED FACT: the focused product-distance suite passes all
  43 tests.
- CURRENT LOCAL VERIFIED FACT: the complete suite passes all 171 tests
  outside the filesystem sandbox. The first sandboxed full-suite attempt
  reached collection and produced 31 setup errors only because pytest could
  not create the requested temporary directory; no test body failed.
- CURRENT LOCAL VERIFIED FACT: checked-artifact semantic verification accepts
  4 certificates, 76 local brackets, and the \(n=3,\dots,6\) summary.
- CURRENT LOCAL VERIFIED FACT: Ruff reports "All checks passed!" on
  tests/test_product_distance.py, and Python compilation succeeds.
- CURRENT LOCAL VERIFIED FACT: independent mathematical and implementation
  audits reconstruct the five residue calculations, the moved-label order,
  all \(\binom{92}{2}=4186\) exact pair scores, scorer independence, and the
  unchanged enumeration boundary.
- CURRENT LOCAL VERIFIED FACT: no production source, generator, canonical
  enumerator, artifact, schema, CLI, certificate, or geometric proof changed.
- CURRENT LOCAL VERIFIED FACT: the final cross-document audit, strict UTF-8
  scan, whitespace checks, 163-tag uniqueness check, stale-claim scan,
  complete-diff inspection, changed-path audit, and Git diff check pass.
- CURRENT HOSTED STATUS: GitHub Actions for the current worktree has not been
  independently verified.

## Residual Limitations

- This is an exact combinatorial surrogate theorem, not an exact value or new
  bound for the geometric optimum \(R_2^*(n)\).
- Subsequent indices \(n\ge94\) with strict minimizer inclusion have not been
  classified; no monotone persistence is claimed.
- Canonical cyclic-order enumeration remains bounded to \(n=3,\dots,11\).
- The existing fixed-order interval-backend trust boundary is unchanged.

## Proposed Next Task

In a fresh chat, document the fixed-order angular/STN equivalence and endpoint
semantics, as already prioritized in research/NEXT_RESEARCH_STEPS.md. This
task did not begin or add that documentation.

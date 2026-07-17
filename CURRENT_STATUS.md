# CURRENT_STATUS - power-ringmin

Last update: 2026-07-17

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** arbitrary relation-compatible full-score classification on
  the symbolic \(n=10m+3\), \(m\ge3\), scaffold.
- **Repository state at startup:** clean `main` worktree at commit
  \(9664e342964e27c36b8e203f0dc646c811c66409\), aligned with `origin/main`.
- **Implementation state:** the symbolic theorem, sole polynomial diagnostic,
  proof note, stable memory, roadmap, dossier, independent audits, and final
  diff inspection are complete and synchronized.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

For
\[
n=10m+3,
\qquad m\ge3,
\qquad d=8m+4,
\qquad v=2m,
\qquad T={d(d-1)\over2},
\]
treat the path-to-gap bijection \(\alpha\) as arbitrary and determine whether
every relation-compatible bijection for the Ferrers relation (PG31)/(PG36)
satisfies \(W(\sigma_\alpha)=T\).

The task classifies every positional-distance-three pair, all four ordered
triple/singleton transitions, and cyclic closure. Production code, tests,
APIs, enumeration limits, artifacts, schemas, interval backends,
certificates, CLIs, and configuration remain unchanged.

## Complete Distance-Three Classification

Put \(k_j=\alpha(j)\), \(j^+=j+1\pmod v\), and let \(F_k\) be the first
label of \(P_k\). If \(P_{k_j}=(A_{k_j},c_{k_j},B_{k_j})\) is a triple, the
six forward pairs are
\[
\begin{gathered}
\{E_j,c_{k_j}\},\quad
\{\lambda_j,B_{k_j}\},\quad
\{A_{k_j},\rho_{j^+}\},\quad
\{c_{k_j},E_{j^+}\},\\
\{B_{k_j},\lambda_{j^+}\},\quad
\{\rho_{j^+},F_{k_{j^+}}\}.
\end{gathered}
\]
If \(P_{k_j}=(x_{k_j})\) is a singleton, the four are
\[
\{E_j,\rho_{j^+}\},\quad
\{\lambda_j,E_{j^+}\},\quad
\{x_{k_j},\lambda_{j^+}\},\quad
\{\rho_{j^+},F_{k_{j^+}}\}.
\]

The two transition pairs are respectively last\((P_{k_j})\)--\(\lambda_{j^+}\)
and \(\rho_{j^+}\)--first\((P_{k_{j^+}})\), giving all four ordered type
combinations. The lists have
\[
6(m+1)+4(m-1)=10m+2=|\sigma_\alpha|
\]
starts. Since the core length is greater than six, they contain every
unordered distance-three pair exactly once.

For a compatible bijection, \(\alpha(0)=0\). Thus the closing list is
\[
\{n,c_k\},\{2,B_k\},\{A_k,4m+1\},\{c_k,d\},
\{B_k,4m\},\{4m+1,A_0\}
\]
when \(k=\alpha(v-1)\) is triple, and
\[
\{n,4m+1\},\{2,d\},\{x_k,4m\},\{4m+1,A_0\}
\]
when it is singleton.

## Sharp Bound And Arbitrary-Bijection Collapse

Every terminal--connector product is at most \(n(5m+2)\). Every
terminal--low product is strictly smaller, and every low--middle product is at
most \((4m+1)(d-1)\), with
\[
n(5m+2)-(4m+1)(d-1)=18m^2+15m+3>0.
\]
Therefore, for every bijection, even without relation-compatibility,
\[
\boxed{
W^{(=3)}(\sigma_\alpha)
\le {n(5m+2)\over3}<T,
\qquad
3T-n(5m+2)=46m^2+49m+12>0.
}
\]
The bound is sharp exactly when
\(\alpha(v-2)=m\) or \(\alpha(v-1)=m\). Both alternatives occur in
relation-compatible PG46 witnesses.

Universally for positional distance \(q\ge4\),
\[
{ij\over q}\le {n(n-1)\over4}<T,
\qquad
4T-n(n-1)=28m^2+62m+18>0.
\]
Every reassignment retains the adjacent internal pair
\(A_0c_0=(d-1)(4m+2)=T\). Hence the stronger exact theorem is
\[
\boxed{
W(\sigma_\alpha)=W^{(\le2)}(\sigma_\alpha)
\quad\text{for every bijection }\alpha.
}
\]

## Full-Optimal Equivalence And PG49

Combining the collapse theorem with PG36 gives
\[
\boxed{
\alpha\text{ relation-compatible}
\quad\Longleftrightarrow\quad
W^{(\le2)}(\sigma_\alpha)\le T
\quad\Longleftrightarrow\quad
W(\sigma_\alpha)=T.
}
\]
The residue-three formula and global saturation theorem give \(W_n=T\), so
these are global full-distance minimizers of the product-distance surrogate.
Every incompatible scaffold bijection has score strictly above \(T\).

If \(\mathcal R_{\rm full}\) is the edge support of scaffold bijections with
full score \(T\), then
\[
\boxed{
\mathcal R_{\rm full}=\mathcal R_{\rm ext}
=\{(0,0)\}\cup
\{(k,j)\in\mathcal R_{\rm loc}:j\ge1\}.
}
\]
Thus PG49 is exactly the support of full-optimal scaffold bijections. It does
not enumerate those bijections, and this surrogate theorem gives no new
geometric optimum or bound.

## Diagnostic And Verification

- The sole new diagnostic is standalone, standard-library-only, and
  polynomial. It scans local states \((j,k,h)\), not bijections or matchings.
- At \(m=3,4,9,34\), it checks respectively 180, 448, 5,508, and 309,808
  local words, all four transition types, 3, 5, 11, and 41 compatible closing
  cases, and exactly two sharp PG46 full-order witnesses per row.
- The diagnostic, in-memory compilation, and Ruff lint/format checks pass
  after one retained initial format-check failure and mechanical reformat.
- The focused product-distance regression passes 49 tests; the serial complete
  suite passes all 283 tests; the schema regression passes 4 tests.
- The checked-artifact semantic verifier confirms 4 certificates and 76 local
  brackets.
- Three independent proof/code/scope audits pass. Exact nine-file scope,
  PG50--PG63 uniqueness, UTF-8/no-BOM, final newlines, no trailing whitespace,
  no generated cache, complete diff inspection, and `git diff --check` pass.

## Evidence Classification And Limitations

- The all-\(m\) distance-three classification, arbitrary-bijection collapse,
  full-optimal equivalence, and support identity are **exact theorems** proved
  symbolically.
- Sharpness uses two exact constructive PG46 witnesses.
- The four-row script is a **finite exact diagnostic** that corroborates but
  does not prove the theorem.
- No path permutation, matching, production result, artifact, certificate,
  schema, backend, limit, or geometric statement is added.

## Files In Scope

- research/PRODUCT_DISTANCE_SURROGATE.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260717__relation_compatible_full_score_classification/

## Proposed Next Task

In a fresh STRICT task, derive an exact symbolic count of
relation-compatible, equivalently full-optimal, scaffold bijections from the
nested Ferrers thresholds, without enumerating path permutations.

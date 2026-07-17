# CURRENT_STATUS - power-ringmin

Last update: 2026-07-17

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** exact generic path-to-terminal-gap classification at
  distances one and two in the symbolic \(n=10m+3\) construction.
- **Repository state at startup:** clean main worktree at commit
  \(d8107ef\), aligned with origin/main.
- **Implementation state:** proof, standalone diagnostic, stable memory,
  state, roadmap, and dossier are synchronized; all requested verification
  has completed.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

Keep the established terminal/low scaffold, every path, and every orientation
fixed. For
\[
n=10m+3,\qquad m\ge3,\qquad d=8m+4,\qquad
T={d(d-1)\over2},
\]
classify exactly when the unchanged oriented path \(P_k\) is locally
non-excluded from terminal gap \(G_j\) by every distance-one and distance-two
pair.

No complete reassignment is selected, scored, or experimentally probed. No
path permutations are enumerated. Production code, tests, APIs, artifacts,
schemas, interval backends, certificates, and enumeration limits remain out
of scope.

## Exact Result

Let \(j^+=j+1\pmod{2m}\), with
\[
E_j=d+j,\qquad
\lambda_j=4m-2j,\qquad
\rho_j=4m+1-2j.
\]
The local word is
\[
Q_{k,j}=(E_j,\lambda_j,P_k,\rho_{j^+},E_{j^+}).
\]
The fixed terminal/low scaffold is strictly below \(T\) at both requested
distances.

### Triple Paths

For \(0\le k\le m\), write
\[
P_k=(A_k,c_k,B_k)
=(d-1-2k,\,4m+2+k,\,d-2-2k).
\]

- Every adjacent pair is at most \(T\). The path-bearing adjacent maximum is
  \[
  A_kc_k=T-k(2k+1).
  \]
- The unique distance-two local maximum is
  \[
  M^{\rm tr}_2(k,j)
  ={E_jA_k\over2}
  =T+{jA_k-2kd\over2}.
  \]
- Hence the exact local condition is
  \[
  (k,j)\text{ locally non-excluded}
  \quad\Longleftrightarrow\quad
  j(d-1-2k)\le2kd.
  \]

Equivalently, define
\[
\ell_k=
\min\!\left\{2m-1,
\left\lfloor{2kd\over d-1-2k}\right\rfloor\right\},
\qquad
\kappa_j=
\left\lceil{j(d-1)\over2(d+j)}\right\rceil.
\]
Then the row of \(P_k\) is exactly \(0\le j\le\ell_k\), while the
triple indices admitted by \(G_j\) are exactly \(\kappa_j\le k\le m\).
If \(j>\ell_k\), the pair \(\{E_j,A_k\}\) is an explicit distance-two
violation.

The right terminal pair is less restrictive. For \(j\le2m-2\), it is safe
exactly when
\[
(j+1)B_k\le d(2k+1);
\]
at cyclic closure it is always safe. The left terminal pair remains the
unique maximum in both branches.

### Singleton Paths

For \(m+1\le k\le2m-1\), write
\[
P_k=(x_k),\qquad x_k=4m+2+k.
\]
Every adjacent pair is strictly below \(T\), and the unique distance-two
maximum is
\[
M^{\rm sing}_2(k,j)=
\begin{cases}
x_k(d+j+1)/2,&0\le j\le2m-2,\\
x_kn/2,&j=2m-1.
\end{cases}
\]
It is uniformly strict because
\[
d(d-1)-n(6m+1)=4m^2+28m+9>0.
\]
Thus every singleton is locally non-excluded in every gap.

### Complete Local Relation

\[
\mathcal R_{\rm loc}
=
\{(k,j):0\le k\le m,\ 0\le j\le\ell_k\}
\cup
\{(k,j):m+1\le k\le2m-1,\ 0\le j\le2m-1\}.
\]

## Cyclic Closure, Transitions, And Extremes

- \(G_0\) locally permits every path, while \(P_0\) locally permits only
  \(G_0\), recovering (PG15).
- The last nonclosing triple word is
  \[
  (n-1,4,A_k,c_k,B_k,3,n),
  \]
  and it permits exactly
  \[
  k\ge\kappa_{2m-2}=\left\lfloor{4m+1\over5}\right\rfloor.
  \]
- The cyclic closing triple word is
  \[
  (n,2,A_k,c_k,B_k,4m+1,d),
  \]
  and it permits exactly
  \[
  k\ge\kappa_{2m-1}=\left\lfloor{4m+3\over5}\right\rfloor.
  \]
  This is also the first triple index locally permitted in every gap.
- The same column formula applies at \(j=m-1,m,m+1\); there is no hidden
  branch at the canonical triple/singleton gap transition.
- The path-type transition is
  \[
  P_m=(6m+3,5m+2,6m+2),
  \qquad
  P_{m+1}=(5m+3).
  \]
  Both paths, as well as the terminal singleton \(P_{2m-1}=(6m+1)\), are
  locally non-excluded in every gap.

At \(m=3\), \(d=28\), \(T=378\), the exact rows are
\[
\begin{array}{c|c}
k&\text{locally non-excluded gap indices}\\ \hline
0&\{0\}\\
1&\{0,1,2\}\\
2&\{0,1,2,3,4\}\\
3&\{0,1,2,3,4,5\}\\
4,5&\{0,1,2,3,4,5\}.
\end{array}
\]
In particular, \(P_2\) passes \(G_4\) with score \(368\), but is excluded
from cyclic \(G_5\) by the exact score \(759/2=T+3/2\).

## Logical Classification

- **Locally excluded:** \((k,j)\notin\mathcal R_{\rm loc}\); this occurs
  only for a triple with \(j>\ell_k\), and \(\{E_j,A_k\}\) is the explicit
  violating pair.
- **Locally non-excluded:** \((k,j)\in\mathcal R_{\rm loc}\); every
  distance-one and distance-two pair determined by that one placement is
  safe. This is not an edge-extendibility claim.
- **Relation-compatible bijection:** for a bijection \(\alpha\) already
  given, one has
  \[
  W^{(\le2)}(\sigma_\alpha)\le T
  \quad\Longleftrightarrow\quad
  (\alpha(j),j)\in\mathcal R_{\rm loc}\quad\text{for every }j.
  \]
  An individual local edge need not extend: every \((k,0)\) is local, but
  \(P_0\) has only \((0,0)\), so no \((k,0)\) with \(k>0\) can belong to a
  relation-compatible bijection.
- **Existence:** the previously proved canonical identity construction
  separately supplies one relation-compatible bijection. No new bijection is
  selected, no nonidentity bijection is classified, and no complete
  reassignment is evaluated here.
- **Full threshold:** even a relation-compatible bijection must separately
  pass every distance-at-least-three pair to prove \(W\le T\).

## Diagnostic And Verification

- The sole new standalone diagnostic uses only the Python standard library
  and exact Fraction arithmetic.
- It scans only \((m,k,j)\) at the fixed values \(m=3,4,9,34\), constructs
  only constant-size local words, and compares every direct pair with both
  symbolic cutoff forms.
- The row \(m=34\) includes the nontrivial exact boundary equality
  \((m,k,j)=(34,11,24)\).
- The diagnostic passes on all four rows; Python compilation and Ruff
  lint/format pass.
- The focused product-distance regression passes 49 tests, the schema
  regression passes 4 tests, and the complete suite passes all 283 tests.
- The checked-artifact semantic verifier confirms 4 certificates and 76
  local brackets.
- Three independent read-only audits pass after correcting one false prose
  ordering before (PG19) from \(A_k>c_k>B_k\) to
  \(A_k>B_k>c_k\); no formula or conclusion changed.
- Expected-file scope, sole-diagnostic structure, generated-cache cleanup,
  UTF-8/delimiter delta, PG16--PG36 uniqueness, complete diff inspection, and
  final whitespace checks pass.
- The first Ruff format check required one mechanical correction. A later
  redirected-cache compile attempt failed with WinError 5; ordinary
  compilation passed and its generated task-local cache was removed.

## Evidence Classification And Limitations

- The all-\(m\) classification is an **exact theorem** proved symbolically.
- The four-row script is a **finite exact diagnostic** that corroborates but
  does not prove the theorem.
- No geometric claim, new upper bound, nonidentity matching, full
  reassignment, artifact, certificate, or production result follows.

## Files In Scope

- research/PRODUCT_DISTANCE_SURROGATE.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260717__generic_path_terminal_gap_classification/

## Proposed Next Task

In a fresh STRICT task, use the monotone relation \(\mathcal R_{\rm loc}\) to
classify symbolically which locally non-excluded edges extend to a
relation-compatible bijection, without enumerating path permutations or
scoring distances at least three.

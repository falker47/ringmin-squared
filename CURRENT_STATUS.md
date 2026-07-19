# CURRENT_STATUS - power-ringmin

Last update: 2026-07-19

## State

- **Mode:** STRICT
- **Status:** BLOCKED
- **Active task:** classify the descending-min PG49 zero-gain set on
  \(n=10m+3\), starting from (KPGMIN-19)--(KPGMIN-21).
- **Repository state at startup:** clean main worktree at commit
  78e0007ee1ca7967a787b60c072f167b3b8a2abe.
- **Implementation state:** the separate left/right gain equations, unique
  primitive parameters, integrality, domain, literal plateau inequalities,
  every endpoint and outer column, explicit quadratic scale windows,
  continued-fraction reduction, giant left witness, and a new exact right
  witness are proved and synchronized.  The sole bounded standard-library
  diagnostic and all repository-proportional checks pass.
- **Current blocker:** no theorem available in the repository or identified
  primary literature decides whether the exact congruence-filtered,
  one-sided convergent set for the specified cubic root is finite or
  infinite.  Therefore the requested global cardinality dichotomy remains
  an unresolved Diophantine claim.
- **Current next atomic action:** user review; in a fresh STRICT task, attack
  the filtered-convergent obstruction (KPGZERO-23)--(KPGZERO-24).
- **Awaiting user review:** yes.

## Objective And Scope

For the fixed descending-min PG49 order, classify

\[
\mathcal Z_m=
\{\lambda_j:L_{m,j}=0\}\mathbin\cup
\{\rho_{j+1}:R_{m,j}=0\}
\]

with \(m\ge3\), \(1\le j<m\), and
\(\kappa_j=\kappa_{j+1}\).  The two equations and their two literal
half-open ceiling inequalities must remain separate.  Geometry, angular
thresholds, global \(K\)-minimality, minimizing-order classification, and
all-row deductions from a finite sweep are excluded.

## Exact Branchwise Classification

Use \(\delta=0\) for \(L=0\) and \(\delta=1\) for \(R=0\).  Every gain-zero
equation has unique parameters

\[
g>0,\qquad \gcd(u,w)=1,\qquad u>w>0,
\]

with

\[
\begin{aligned}
j_\delta&={gu(u-w)-(4+3\delta)\over5},\\
m_\delta&={gu(2u+3w)-(8+\delta)\over20},\\
r_\delta&={g(10w^2-4u^2-uw)+(6-3\delta)\over10}.
\end{aligned}
\]

Integrality is equivalent to

\[
gu(2u+3w)\equiv8+\delta\pmod {20},
\]

and (KPGZERO-6) gives the four exact inequalities for
\(j\ge1\), \(m\ge3\), \(j<m\), and \(r\ge1\).  The distinct residual pairs
(KPGZERO-10) and (KPGZERO-12) are exactly equivalent to both literal
ceilings.  The allowed left upper endpoint is retained; the left lower
endpoint and both right endpoints are impossible.  Jump columns, \(j=0\),
\(r=1\), \(j=m-1\), all \(j\ge m\), and the cyclic closing position are
audited symbolically.

The common cubic form is

\[
\Phi(u,w)=50w^3+51uw^2-27u^2w-24u^3.
\]

Its sign gives the four explicit radical intervals in \(g\) recorded in
(KPGZERO-20)--(KPGZERO-21).  Intersecting the appropriate interval with the
integrality congruence and domain is a necessary-and-sufficient finite
parameter set for each primitive fraction.

## Exact Cardinality Obstruction

Let \(\xi\in(7/5,10/7)\) be the unique root in \((1,\infty)\) of

\[
50+51t-27t^2-24t^3=0.
\]

The polynomial is irreducible modulo seven.  Every admitted primitive ratio
satisfies

\[
\left|{u\over w}-\xi\right|<{1\over2w^2},
\]

so it is a regular continued-fraction convergent.  Conversely, a convergent
produces a zero exactly when it passes the side, congruence, domain, and
finite scale-window tests.  This is the exact bijection (KPGZERO-23).

Consequences:

- every fixed \(\mathcal Z_m\) is finite, already from \(1\le j<m\);
- both the left and right global branches are nonempty;
- no fixed primitive ratio supports infinitely many scales \(g\);
- the global union is infinite exactly if infinitely many filtered
  one-sided convergents pass one of the four scale windows;
- neither finiteness nor infinitude of that filtered subsequence is proved.

The conic \(X^2-Y^2=8J^2\) describes the gain equation alone and cannot
replace the plateau filters; (KPGZERO-18) includes explicit integral points
that fail both ceilings.

## Exact Witnesses

- **Left:** \((g,u,w)=(4,11116408784,7852541895)\) reconstructs the
  giant row (KPGMIN-19)--(KPGMIN-20), both literal ceiling residuals,
  \(L_{m,j}=0\), and the stated negative \(R_{m,j}\).
- **Right:** the primitive \(g=19\) triple (KPGZERO-27) reconstructs the
  full \((m,j,r)\), right label, singleton path index, strict plateau
  residuals, \(R_{m,j}=0\), and positive \(L_{m,j}\) in
  (KPGZERO-28)--(KPGZERO-30).  Universal right-hole nonexistence is therefore
  disproved; an infinite right-hole family is not proved.

## Verification

- The sole standard-library diagnostic passes.  Its declared finite bounds
  are literal rows \(m=3,\ldots,500\), direct denominators \(w\le10^5\),
  proposed convergents with denominator at most \(10^{200}\), and
  \(g\le200\).
- Every proposed positive witness is rechecked with exact integer formulas,
  both literal ceilings, the appropriate literal gain, and the exact
  sign-dependent scale window.  The bounded proposal set contains 56 left
  and eight right parameter triples.
- Full pytest passes: 283 passed.
- The focused checked-artifact schema suite passes: 4 passed.
- The standalone checked-artifact verifier passes:
  certificates=4, local_brackets=76, n=3,4,5,6.
- Scoped Ruff lint and format checks pass for the sole new Python file.
- The KPGZERO source audit passes with 30 sequential unique primary tags,
  balanced displays and aligned environments, no cubic-root notation
  collision, and exactly one dossier diagnostic.
- An independent formula audit reports no remaining mathematical or material
  defect in (KPGZERO-1)--(KPGZERO-30).
- Complete diff inspection and final whitespace hygiene pass.

## Evidence Classification And Limitations

- (KPGZERO-1)--(KPGZERO-23) and both witnesses are **exact
  combinatorial/Diophantine results**.
- The finite diagnostic output is **bounded exact computation** used for
  falsification and initial corroboration only.
- (KPGZERO-24) is an **unresolved Diophantine claim**, not a finiteness or
  infinitude theorem.
- No geometric result, angular result, global \(K\)-minimality result,
  minimizing-order classification, or Ringmin generalization is asserted.

## Files In Scope

- research/FIXED_ORDER_CYCLE_RATIO.md
- research/PRODUCT_DISTANCE_SURROGATE.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260719__pg49_zero_gain_classification/

## Proposed Next Task

In a fresh STRICT task, attack the exact filtered-convergent obstruction.
Prove an infinite congruence-compatible one-sided subsequence entering a
left or right scale window, prove eventual exclusion, or record a strictly
sharper literature-backed obstruction.  Further bounded expansion alone is
not an acceptance criterion.

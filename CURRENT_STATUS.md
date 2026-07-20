# CURRENT_STATUS - power-ringmin

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** exact induced-subset objective \(K\) of the unchanged
  odd-\(v\) residue-two PG49-star core fixed by (PGE2ODD-6),
  \(n=10m+7\), \(m\ge1\).
- **Repository state at startup:** clean `main` worktree at commit
  be6420c4f5f2dbd68c552accdd44a8d4ded91b71.
- **Implementation state:** exact symbolic theorem, five residue branches,
  same-row comparisons, sole bounded diagnostic, authoritative
  synchronization, independent audits, repository verification, and diff
  hygiene are complete.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Unchanged Fixed Core

Retain exactly the construction already proved in (PGE2ODD-1)--
(PGE2ODD-29):

\[
n=10m+7,\qquad m\ge1,\qquad D=8m+7,
\qquad q=\left\lfloor{4m+3\over5}\right\rfloor,
\]

\[
\alpha^{(2,\mathrm{odd})}_*(j)=
\begin{cases}
j,&0\le j<q,\\
j+1,&q\le j\le m-1,\\
3m-j,&m\le j\le2m-1,\\
q,&j=2m.
\end{cases}
\]

No path assignment or orientation is changed. The branch has \(m+1\)
oriented triples, \(m\) singleton paths, and no doubleton.

## Exact Induced-Subset Theorem

Put

\[
L=4m+3,\qquad H_m=\{2,\ldots,4m+2\},
\qquad B_m=\{L,\ldots,10m+7\}.
\]

For every \(m\ge1\), (KPGE2ODD-1)--(KPGE2ODD-43) prove

\[
\boxed{
\operatorname*{argmax}_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P(U)
=\{B_m\},}
\]

\[
\boxed{
K={1714m^3+3891m^2+24mq+2921m+12q^2+48q+732\over6}.}
\]

The compressed backbone is

\[
\left(
L,
(E_j,P_j)_{j=0}^{q-1},
(E_j,P_{j+1})_{j=q}^{m-1},
(E_j,x_{3m-j})_{j=m}^{2m-1},
E_{2m},P_q
\right).
\]

The first triple interval is always nonempty. The shifted-triple interval is
empty exactly for \(m=1,2,3\). The singleton block always has cardinality
\(m\), including its one-member boundary at \(m=1\). The doubleton type and
range are identically absent. The true compressed closure is

\[
E_{2m},A_q,c_q,B_q,L,E_0.
\]

## Cancellation And Shortcut Proof

- The seven exhaustive cancellation-gain classes cover exactly
  \(4m+1=|H_m|\) holes.
- Their unique minimum is
  \[
  \min h_z=20m+16
  \]
  at \(\lambda_0=4m+2\), between \(E_0=8m+7\) and \(A_0=8m+6\).
- Every nontrivial compressed shortcut is strict. Its exact unique minimum is
  \[
  \begin{cases}
  17,&m=1,\quad(11,7,15),\\
  49,&m=2,\quad(17,11,23),\\
  20m+14,&m\ge3,\quad(A_0,c_0,B_0).
  \end{cases}
  \]
- The exact raw-arc plus cancellation-budget identity forces every hole to
  be omitted and every backbone label to be retained. The backbone score is
  at least \(2n(n-1)>n^2\), so no singleton ties; the adopted two-element
  convention is included.

Thus \(B_m\) is the only maximizing subset. This is an exact all-domain
combinatorial theorem, not a finite-computation inference.

## Five Regular Residue Branches

For \(r=m\bmod5\),

\[
q={4m+c_r\over5},\qquad(c_0,c_1,c_2,c_3,c_4)=(0,1,2,3,-1),
\]

and

\[
150K=42850m^3+97947m^2+(73985+216c_r)m
+18300+240c_r+12c_r^2.
\]

The five branches begin at \(m=5,1,2,3,4\), respectively. There is no
residual row, score correction, or argmax exception. Equivalently,

\[
q=\left\lfloor{2n+1\over25}\right\rfloor,\qquad
K={857n^3+1458n^2+1200nq-341n
+6000q^2+15600q+2994\over3000},
\]

so the cubic coefficient is \(857/3000\).

## Exact Same-Subsequence Comparisons

For the known residue-two order on \(k=2m+1\),

\[
K_{\rm R2}={572m^3+1307m^2+997m+254\over2},
\]

\[
K_{\rm R2}-K
={m^3+15m^2-12mq+35m-6q^2-24q+15\over3}>0.
\]

For canonical K825, the rows \(m=1,2\) are explicit, while for \(m\ge3\),

\[
K_{825}={572m^3+1349m^2+1119m+324\over2}
-25\mathbf1_{\{m=3\}},
\]

\[
K_{825}-K
={m^3+78m^2-12mq+218m-6q^2-24q+120\over3}
-25\mathbf1_{\{m=3\}}>0.
\]

Hence the unchanged PGE2ODD core is strictly below both named orders on
every same-subsequence row, with no tie or crossover. Both gaps have leading
term \(n^3/3000\).

## Literal Boundary Rows

\[
\begin{array}{c|c|c|c|c|c}
m&q&\alpha^{(2,\mathrm{odd})}_*&K&K_{\rm R2}&K_{825}\\ \hline
1&1&(0,2,1)&1557&1565&1609\\
2&2&(0,1,4,3,2)&6015&6026&6204\\
3&3&(0,1,2,6,5,4,3)&15210&15226&15608.
\end{array}
\]

All three shifted-triple intervals are empty. Their singleton blocks have
sizes one, two, and three; none has a doubleton. At \(m=3\), the shortcut
minimum has already moved to \(c_0\), and the canonical K825 boundary
correction is active. None is an exception to the exact formula or unique
argmax.

## Bounded Diagnostic

The task's sole standalone standard-library diagnostic constructs only
(PGE2ODD-6). It passes on:

- formula, residue, boundary, closure, and comparator rows
  \(m=1,\ldots,1000\), totaling 5,011,000 literal core entries;
- max-plus score and complete argmax counts for \(m=1,\ldots,30\), totaling
  38,957,975 transitions;
- every cancellation gain and every proper oriented arc on those 30 rows:
  1,890 gains, 997,550 arcs, and 990,830 nontrivial compressed shortcuts.

It verifies the exact raw-arc plus internal-hole-budget identity, the cyclic
cut, all empty intervals, singleton boundaries, absent doubleton, and both
comparisons. It imports no project or test helper and performs no subset,
matching, path-assignment, path-permutation, or order-family search.

## Verification

- The standalone diagnostic passes with the exact bounded counts above.
- Scoped Ruff lint and format checks pass.
- The KPGE2ODD source audit passes with 43 sequential unique tags, 48
  balanced display pairs, balanced environments, and no control characters.
- Four independent mathematical, comparator, proof/code, and synchronization
  audits pass.
- Full pytest passes: 283 tests.
- The focused checked-artifact schema suite passes: 4 tests.
- The standalone checked-artifact verifier passes for four certificates,
  76 local brackets, and \(n=3,4,5,6\).
- Final Git status, complete tracked and untracked scope inspection, source
  structure, and whitespace hygiene pass.
- Two initial `rg` synchronization wrappers had malformed regular
  expressions and exited before completing their searches. Corrected fixed-
  string searches and the independent source audit pass; no mathematical,
  code, or repository check failed.

## Evidence Classification And Scope

- (KPGE2ODD-1)--(KPGE2ODD-43) are an **exact all-domain fixed-core
  combinatorial theorem**.
- The standalone diagnostic is **bounded exact computation** corroborating,
  not replacing, the symbolic proof.
- Construction, compatibility, and \(W\) remain the separate theorem
  (PGE2ODD-1)--(PGE2ODD-29); this task does not alter them.
- No production or test file is changed. No angular, geometric, global-
  minimizer, or global-optimality conclusion is inferred.

## Files In Scope

- research/FIXED_ORDER_CYCLE_RATIO.md
- research/PRODUCT_DISTANCE_SURROGATE.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260720__residue_two_odd_v_pg49_star_k/

## Proposed Next Task

In a fresh STRICT task, attack the exact filtered cubic-convergent obstruction
(KPGZERO-23)--(KPGZERO-24): construct an infinite congruence-compatible
subsequence entering its quadratic window, prove eventual exclusion, or
record a sharper rigorous obstruction.

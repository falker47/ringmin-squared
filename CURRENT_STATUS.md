# CURRENT_STATUS - power-ringmin

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** determine exactly the induced-subset objective \(K\) for
  `residue_two_product_distance_order(n)` on \(n=5k+2\), \(k\ge2\), and
  compare it pointwise and asymptotically with (K825-4).
- **Repository state at startup:** clean `main` worktree at commit
  `6edc37325200dec1826173b2506dd0893219b28b`, tracking `origin/main`.
- **Implementation state:** the exact score, unique-maximizer classification,
  all-\(k\) shortcut-budget proof, parity/boundary treatment, K825 comparison,
  sole bounded diagnostic, authorized consequences, authoritative
  synchronization, independent audits, and final verification are complete.
- **Current blocker:** none.
- **Current next atomic action:** user manual review and commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

For the exact-threshold residue-two cyclic core order \(\tau_n^{(2)}\)
returned by `residue_two_product_distance_order(n)`, determine
\[
K(\tau_n^{(2)})
=\max_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P_{\tau_n^{(2)}}(U)
\]
for every \(n=5k+2\), \(k\ge2\), without enumerating subsets or cyclic
orders. Classify every maximizer, treat both parities and every smallest path
boundary, compare exactly and asymptotically with K825, and transfer only
consequences licensed by label-one elimination and the fixed-order sandwich.
Production, tests, artifacts, schemas, certificates, and enumeration limits
remain unchanged because no defect was found.

## Exact Theorem And Argmax Classification

Put \(\varepsilon=k\bmod2\). For every \(k\ge2\), the sole maximizing
subset is
\[
\boxed{S_k=\{2k+1,\ldots,5k+2\}.}
\]
There are no ties, parity-dependent argmaxes, or exceptional boundary
maximizers. The exact score is
\[
\boxed{
K(\tau_n^{(2)})
={286k^3+459k^2+198k+16
 +\varepsilon(-10k^2+40k+27)\over8}.
}
\]
Equivalently,
\[
K(\tau_n^{(2)})=
\begin{cases}
\dfrac{286n^3+579n^2-798n-1008}{1000},
 &n\equiv2\pmod {10},\\[6pt]
\dfrac{286n^3+529n^2+402n+167}{1000},
 &n\equiv7\pmod {10}.
\end{cases}
\]

## Proof Architecture And Boundary Cases

- Delete exactly the isolated holes \(\{2,\ldots,2k\}\), retaining the
  closing label \(L=2k+1\). Every deletion gain is positive, with exact
  minimum \(10k+6\).
- Every compressed path with at least two edges has strict positive shortcut
  margin. The proof treats hole endpoints, connector and closing middle
  labels, every three-edge path, and all longer paths separately.
- Equality in the shortcut budget therefore forces exactly \(S_k\).
- Direct even/odd block summation gives the displayed quasipolynomial. At
  \(k=2\) the doubleton is final and gives \(K=567\); at \(k=3\) the odd
  nonfinal-singleton range is empty and gives \(K=1565\); at \(k=4\) the
  even nonfinal-singleton range is empty. The same theorem holds without a
  boundary correction. The smallest shortcut margin is \(7\) at \(k=2\).

## Exact K825 Comparison

On the symbolic canonical domain \(k\ge7\), the parameters are
\(e=8\), \(v=k-1\), and the K825 parity is \(1-\varepsilon\). Exact
subtraction gives
\[
K_{825}(k)-K(\tau_n^{(2)})
={21k^2+(50+30\varepsilon)k+4+35\varepsilon\over4}
-25\mathbf1_{\{k=7\}}.
\]
The explicit gaps at \(k=2,\ldots,6\) are
\(26,44,124,178,361\), and the K825 boundary gap at \(k=7\) is \(382\).
Every gap is positive; there is no crossover. Rowwise in \(n\),
\[
K_{825}(n)-K(\tau_n^{(2)})=
\begin{cases}
\dfrac{21n^2+166n-316}{100},&n\equiv2\pmod {10},\\[6pt]
\dfrac{21n^2+316n+259}{100},&n\equiv7\pmod {10},
\end{cases}
-25\mathbf1_{\{n=37\}}
\]
on the symbolic rows. Both families have cubic coefficient \(143/500\), and
\[
K_{825}(n)-K(\tau_n^{(2)})={21\over100}n^2+O(n).
\]
Thus the improvement is pointwise and quadratic, not cubic.

## Permitted Cyclic-Ratio And Geometric Consequences

For every insertion gap \(g\), exact label-one elimination and the fixed-
order sandwich give
\[
\Lambda(\sigma_{n,g}^{(2)})=K(\tau_n^{(2)}),
\qquad
{K(\tau_n^{(2)})\over\pi}-n^2
<\rho_{\sigma_{n,g}^{(2)}}
<{K(\tau_n^{(2)})\over\pi}.
\]
No maximizing subset contains label \(1\), so the same
\(S_k=\{2k+1,\ldots,5k+2\}\) is the unique subset attaining
\(\Lambda(\sigma_{n,g}^{(2)})\) for every insertion gap.
At the global level, only
\[
\Lambda_n\le K(\tau_n^{(2)}),
\qquad
R_2^*(n)<{\Lambda_n\over\pi}
\le{K(\tau_n^{(2)})\over\pi}
\]
is licensed on \(n=5k+2\). Consequently,
\[
\limsup_{k\to\infty}{\Lambda_{5k+2}\over(5k+2)^3}
\le{143\over500},
\qquad
\limsup_{k\to\infty}{R_2^*(5k+2)\over(5k+2)^3}
\le{143\over500\pi}.
\]
These are the existing canonical cubic coefficients, not an improved
all-residue or subsequential cubic bound.

## Verification

- The sole standard-library diagnostic independently reconstructs both block
  orders. For \(2\le k\le30\), each increasing-path max-plus DP checks
  4,623,615 transitions and the residue-two audit checks all 238,670 oriented
  shortcut arcs. Every row has the predicted sole argmax; minimum bounded
  hole and path margins are respectively \(26\) and \(7\). Direct formulas
  and comparison continue through \(k=1000\), with no crossover.
- Ruff lint/format and `py_compile` pass for the sole diagnostic.
- The full repository suite passes 283 tests. The checked-artifact verifier
  accepts four certificates, 76 local brackets, and summary rows
  \(n=3,4,5,6\); the focused schema suite passes four tests.
- Three independent read-only audits pass the mathematics, K825 comparison,
  diagnostic semantics, and authoritative scope. Their one logical wording
  correction and three editorial clarifications were incorporated.
- Strict UTF-8/LF/final-newline/trailing-whitespace, display/fence, LaTeX
  environment, and equation-tag checks pass on all ten intended source paths.
  All 489 primary tags are unique, including KR2-1 through KR2-36.
- Final Git status contains only the six intended tracked Markdown files and
  the four-file dossier. Complete diff inspection and `git diff --check`
  pass; no production, test, artifact, or cache path changed.

## Evidence Classification And Limitations

- The exact score, unique argmax, shortcut-budget proof, parity formulas,
  pointwise K825 comparison, and permitted sandwich consequences are
  **exact theorems**.
- The diagnostic is a **bounded exact computation** that corroborates but
  does not replace the infinite symbolic proof.
- The result is construction-specific. It proves no equality
  \(\Lambda_n=K(\tau_n^{(2)})\), global lower bound
  \(K/\pi-n^2<R_2^*(n)\), global minimizing-order classification,
  classification of active geometric/STN constraints at the exact threshold,
  exact ordering of the two angular thresholds, exact quadratic geometric
  term, convergence, or improved cubic coefficient.

## Files In Scope

- `research/FIXED_ORDER_CYCLE_RATIO.md`
- `research/PRODUCT_DISTANCE_SURROGATE.md`
- `research/NEXT_RESEARCH_STEPS.md`
- `start.md`
- `PROJECT_KNOWLEDGE.md`
- `CURRENT_STATUS.md`
- `ops/TASK-20260718__residue_two_exact_k/`

## Proposed Next Task

After manual review and in a fresh STRICT chat, derive an exact symbolic
count of relation-compatible, equivalently full-optimal, scaffold bijections
from the nested Ferrers support (PG49), without enumerating path permutations.

# CURRENT_STATUS - power-ringmin

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** determine exactly the induced-subset objective \(K\) for
  `residue_one_product_distance_order(n)` on \(n=5k+1\), \(k\ge2\), and
  compare it with the canonical formula (K825-4).
- **Repository state at startup:** clean `main` worktree at commit
  `aca4a7b3544fa015b21774be2413296321f47ed3`, tracking `origin/main`.
- **Implementation state:** the exact formula, unique-maximizer
  classification, all-\(k\) shortcut-budget proof, boundary/parity analysis,
  K825 comparison, permitted consequences, sole bounded diagnostic,
  independent audits, source checks, and complete diff inspection are done.
- **Current blocker:** none.
- **Current next atomic action:** user manual review and commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

For the exact-threshold residue-one cyclic core order
\(\tau_n^{(1)}\) returned by `residue_one_product_distance_order(n)`,
determine

\[
K(\tau_n^{(1)})
=\max_{\varnothing\ne U\subseteq\{2,\ldots,n\}}
P_{\tau_n^{(1)}}(U)
\]

for every \(n=5k+1\), \(k\ge2\), without enumerating subsets or
permutations. Classify every maximizer, compare exactly and asymptotically
with K825, and transfer only consequences licensed by label-one elimination
and the fixed-order sandwich. Residue two, production/test changes, artifacts,
schemas, certificates, and global minimizing-order claims remain out of scope.

## Exact Theorem And Argmax Classification

Put \(\varepsilon=k\bmod2\). For every \(k\ge2\), the sole maximizing
subset is

\[
\boxed{S_k=\{2k+1,\ldots,5k+1\}.}
\]

There are no ties, parity-dependent argmaxes, or exceptional boundary
maximizers. The exact score is

\[
\boxed{
K(\tau_n^{(1)})
={857k^3+891k^2+214k
 +\varepsilon(27k^2-51k-18)\over24}.
}
\]

Equivalently,

\[
K(\tau_n^{(1)})=
\begin{cases}
\dfrac{857n^3+1884n^2-989n-1752}{3000},
 &n\equiv1\pmod {10},\\[6pt]
\dfrac{857n^3+2019n^2-2534n-2592}{3000},
 &n\equiv6\pmod {10}.
\end{cases}
\]

## Proof Architecture And Boundary Cases

- Delete the isolated holes \(\{2,\ldots,2k\}\) while retaining the closing
  label \(2k+1\). Every exact deletion gain is positive.
- The compressed backbone satisfies a strict shortcut margin for every
  oriented path with at least two edges, including paths whose endpoints are
  holes. Equality in the shortcut budget therefore forces precisely \(S_k\).
- Direct even/odd block summation yields the displayed quasipolynomial.
  At \(k=2\), the final path is a triple and gives \(K=452\); at \(k=3\),
  the singleton range is empty and \(K=1328\). In odd rows the final triple
  connector equals \(n/2\), and its separate exact margin remains strict.

## Exact K825 Comparison

On the symbolic canonical domain \(k\ge6\), (K825-4) specializes to

\[
K_{825}(k)
={858k^3+(933+30\varepsilon)k^2
 +(570-276\varepsilon)k+120-195\varepsilon\over24}
-21\mathbf1_{\{k=6\}}.
\]

Exact subtraction, together with the four earlier explicit canonical rows,
proves

\[
K(\tau_n^{(1)})<K_{825}(k)
\qquad(k\ge2).
\]

There is no crossover. The gaps for \(k=2,\ldots,7\) are respectively
\(7,18,61,63,145,142\); parity means the gap need not be monotone. The cubic
coefficient improves from \(143/500=858/3000\) to \(857/3000\), while the
quadratic coefficients improve from \(697/1000\) to \(157/250\) on
\(n\equiv1\pmod {10}\), and from \(747/1000\) to \(673/1000\) on
\(n\equiv6\pmod {10}\). Thus

\[
K_{825}(n)-K(\tau_n^{(1)})={n^3\over3000}+O(n^2).
\]

## Permitted Cyclic-Ratio And Geometric Consequences

For every insertion gap \(g\), exact label-one elimination and the
fixed-order sandwich give

\[
\Lambda(\sigma_{n,g}^{(1)})=K(\tau_n^{(1)}),
\qquad
{K(\tau_n^{(1)})\over\pi}-n^2
<\rho_{\sigma_{n,g}^{(1)}}
<{K(\tau_n^{(1)})\over\pi}.
\]

At the global level, only

\[
\Lambda_n\le K(\tau_n^{(1)}),
\qquad
R_2^*(n)<{\Lambda_n\over\pi}
\le{K(\tau_n^{(1)})\over\pi}
\]

is licensed on \(n=5k+1\). Consequently,

\[
\limsup_{k\to\infty}{\Lambda_{5k+1}\over(5k+1)^3}
\le{857\over3000},
\qquad
\limsup_{k\to\infty}{R_2^*(5k+1)\over(5k+1)^3}
\le{857\over3000\pi}.
\]

These are residue-one subsequence bounds, not an improved all-\(n\) limsup.

## Verification

- The sole standard-library diagnostic independently reconstructs both block
  orders. For \(2\le k\le30\), each increasing-path max-plus DP checks
  4,504,280 transitions and the residue-one audit checks all 234,030 oriented
  shortcut arcs. Every row has the predicted sole argmax; minimum bounded
  hole/path margins are 14/15. Direct formulas and the comparison continue
  through \(k=1000\), with no crossover.
- The full repository suite passes 283 tests.
- The checked-artifact verifier accepts four certificates, 76 local brackets,
  and summary rows \(n=3,4,5,6\); the focused schema suite passes four tests.
- Ruff lint/format and `py_compile` pass for the sole diagnostic.
- Three independent read-only audits pass the mathematics, diagnostic
  semantics, and authoritative scope. Two non-substantive wording ambiguities
  were corrected.
- Strict UTF-8/LF/final-newline/trailing-whitespace, display/fence, LaTeX
  environment, and equation-tag checks pass on all nine intended Markdown
  paths. All 453 primary tags are unique, including KR1-1 through KR1-32.
- Final Git status contains only the six intended tracked Markdown files and
  the four-file dossier; complete diff inspection and `git diff --check` pass.

## Evidence Classification And Limitations

- The exact score, unique argmax, shortcut-budget proof, parity formulas,
  pointwise K825 comparison, and permitted sandwich consequences are
  **exact theorems**.
- The diagnostic is a **bounded exact computation** that corroborates but
  does not replace the infinite symbolic proof.
- The result is construction-specific. It proves no equality
  \(\Lambda_n=K(\tau_n^{(1)})\), global lower bound
  \(K/\pi-n^2<R_2^*(n)\), exact ordering of the two families' angular
  thresholds, exact quadratic geometric term, all-\(n\) coefficient
  improvement, or residue-two result.

## Files In Scope

- `research/FIXED_ORDER_CYCLE_RATIO.md`
- `research/PRODUCT_DISTANCE_SURROGATE.md`
- `research/NEXT_RESEARCH_STEPS.md`
- `start.md`
- `PROJECT_KNOWLEDGE.md`
- `CURRENT_STATUS.md`
- `ops/TASK-20260718__residue_one_exact_k/`

## Proposed Next Task

After manual review and in a fresh STRICT chat, determine the analogous exact
\(K\) theorem for the residue-two product-distance core order. No residue-two
mathematics is included in the current task.

# CURRENT_STATUS - power-ringmin

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** determine exactly the induced-subset objective K for the
  canonical core order of the symbolic eight-twenty-fifths construction on
  its complete public domain.
- **Repository state at startup:** clean `main` worktree at commit
  `1ec6e0b7fca85b9ed1bb81636c87934564994e97`, tracking `origin/main`.
- **Implementation state:** the exact formula, maximizing-subset
  classification, shortcut-budget proof, consequences, authoritative
  synchronization, sole dossier-local diagnostic, regressions, independent
  audits, source checks, and final diff inspection are complete.
- **Current blocker:** none.
- **Current next atomic action:** user manual review and commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

For the canonical cyclic core order `tau_n` returned by
`eight_twenty_fifths_order(n)`, determine

\[
K(\tau_n)
=\max_{\varnothing\ne U\subseteq\{2,\ldots,n\}}P_{\tau_n}(U)
\]

for every public row `n>=9`, without enumerating subsets or permutations.
Classify every maximizing subset and transfer the result through exact
label-one elimination and the angular sandwich. Production, test modules,
artifacts, schemas, backends, certificates, and enumeration limits remain
unchanged.

## Exact Symbolic Theorem

On the symbolic domain write

\[
d=4v+e,\qquad n=5v+e-1,\qquad 4\le e\le8,
\]

and put `L=2v+1`. The unique maximizing subset is

\[
\boxed{
U_n^*=
\begin{cases}
\{L,L+1,\ldots,n\},&e=4,5,\\
\{L,L+1,\ldots,n\}\setminus\{L+1\},&e=6,7,8.
\end{cases}}
\]

With

\[
t=\left\lfloor{v+e-2\over2}\right\rfloor,
\qquad
\varepsilon=v+e-2-2t,
\qquad
\chi=\mathbf1_{\{v=e-2\}},
\]

define

\[
\begin{aligned}
\mathcal Q(v,e,\varepsilon)={1\over8}\bigg[{}
&286v^3+(180e-91+10\varepsilon)v^2\\
&+(38e^2-34e-2-8(e+2)\varepsilon)v\\
&+{e(8e^2-9e-2)\over3}
 +(-2e^2-10e+21)\varepsilon\bigg],\\
\Gamma(v,e)&=(4e-22)v+e^2-7e+8.
\end{aligned}
\]

Then

\[
\boxed{
K(\tau_n)=\mathcal Q(v,e,\varepsilon)
 -(4e-7)\chi+\max\{0,\Gamma(v,e)\}.
}
\]

The fourteen nonsymbolic public orders have the exact unique maximizing
tails and K values recorded in the K825 theorem. Thus the full public domain
is classified.

## Proof Architecture

- Delete isolated holes from the core cycle. Each deletion has exact gain
  `ab-x(a+b)`.
- The shortcut-budget lemma rewrites every selected gap as its compressed
  backbone path plus the gains of its internal holes.
- All hole gains are positive for the stated candidate. Every compressed
  path with at least two edges has product sum strictly larger than its
  endpoint product.
- Exact block formulas prove those inequalities for all `v>=e`. Ten `r=0`
  rows and the sole generic four-edge inequality exception `n=47` use exact
  bounded local margins. The fourteen explicit orders use the same finite
  local certificate.
- Equality in the budget forces every hole omitted and every backbone label
  selected, proving uniqueness without subset enumeration.
- Direct block summation gives the exact formula.

## Asymptotic And Geometric Consequences

The exact formula gives

\[
K(\tau_n)={143\over4}v^3+O(v^2)
          ={143\over500}n^3+O(n^2),
\]

so the shortcut construction improves the regular-direction coefficient by

\[
{8\over25}-{143\over500}={17\over500}.
\]

For every insertion gap `g`, exact label-one elimination and the fixed-order
sandwich give

\[
\Lambda(\sigma_{n,g})=K(\tau_n),
\qquad
{K(\tau_n)\over\pi}-n^2
<\rho_{\sigma_{n,g}}<{K(\tau_n)\over\pi}.
\]

Globally, only

\[
\Lambda_n\le K(\tau_n),
\qquad
R_2^*(n)<{\Lambda_n\over\pi}\le{K(\tau_n)\over\pi}
\]

is valid. Combining this upper construction with
`C_AF=(434+4 sqrt(2))/1587` yields

\[
C_{\rm AF}
\le\liminf{\Lambda_n\over n^3}
\le\limsup{\Lambda_n\over n^3}
\le{143\over500},
\]

with the same bracket divided by `pi` for the geometric optimum.

## Verification

- The standard-library diagnostic independently reconstructs every order.
  Its increasing-path max-plus DP and shortcut audit pass all 112 rows
  `n=9..120`, with 8,495,284 transitions and 561,568 oriented arcs; a direct
  formula-only tail continues through `n=1000`.
- The full repository suite passes 283 tests.
- The checked-artifact verifier accepts four certificates, 76 local brackets,
  and summary rows `n=3,4,5,6`; the focused schema suite passes four tests.
- Ruff lint and format checks pass for the sole new diagnostic.
- Strict UTF-8/LF/final-newline/trailing-whitespace, display/fence, and primary
  equation-tag checks pass on the current intended Markdown paths, including
  all 26 unique K825 tags.
- Three independent read-only audits confirm the proof, diagnostic, and
  authoritative consistency. They found and prompted correction of one
  n=47 four-edge-margin transcription and one symbolic/explicit scope phrase.
- Final Git status shows only the seven intended authoritative Markdown files
  and the four-file dossier; complete diff inspection and `git diff --check`
  pass.

## Evidence Classification And Limitations

- The K formula, maximizing subsets, shortcut-budget lemma, asymptotic leading
  term, and sandwich consequences are **exact theorems**.
- The diagnostic is a **verified bounded exact computation** that corroborates
  but does not replace the infinite symbolic proof.
- The fourteen explicit rows and eleven symbolic boundary/exception rows use
  finite local shortcut certificates, not subset or permutation enumeration.
- The result is construction-specific. It proves no equality
  `Lambda_n=K(tau_n)`, global minimizing-order classification, convergence,
  exact global leading constant, or exact geometric finite optimum.

## Files In Scope

- research/FIXED_ORDER_CYCLE_RATIO.md
- research/PRODUCT_DISTANCE_SURROGATE.md
- research/ALL_N_LOWER_BOUND.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260718__canonical_eight_twenty_fifths_k/

## Proposed Next Task

In a fresh STRICT task, evaluate K exactly for the sharper residue-one and
residue-two product-distance core orders and compare them pointwise and
asymptotically with the canonical 143/500 family using shortcut budgets rather
than subset enumeration.

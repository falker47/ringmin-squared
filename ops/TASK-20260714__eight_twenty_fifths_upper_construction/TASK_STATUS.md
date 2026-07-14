# TASK_STATUS - TASK-20260714__eight_twenty_fifths_upper_construction / Eight-Twenty-Fifths Upper Construction

Last update: 2026-07-14

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** determine whether every `n>=9` admits an explicit cyclic core
  order with product-distance score at most
  `T_n=d_n(d_n-1)/2`, where `d_n=ceil((4n+8)/5)`, and derive only the
  rigorously justified asymptotic consequences.
- **Outcome:** the construction exists. A symbolic five-residue family plus
  fourteen explicit initial witnesses covers every `n>=9`.
- **Current blocker:** none.

## Scope

- **In scope:** a uniform or residue-class construction; exact exceptional
  witnesses; adjacent, distance-two, distance-three, closing, and automatic
  distance-at-least-four checks; consequences for `B_n`, `W_n`, and the
  insertion upper coefficient.
- **Out of scope:** canonical factorial enumeration beyond `n=11`; geometric
  optimality or a geometric limiting constant; new certificate schemas or
  serialized research artifacts; Git writes; upstream Ringmin changes.

## Exact Result

Put

\[
d=d_n=\left\lceil{4n+8\over5}\right\rceil,
\qquad
T_n={d(d-1)\over2},
\qquad
v=n-d+1,
\qquad
e=d-4v.
\]

For residues `n mod 5 = 0,1,2,3,4`, respectively,
`e=6,7,8,4,5`. The symbolic construction uses

\[
t=\left\lfloor{v+e-2\over2}\right\rfloor,
\qquad
\varepsilon=v+e-2-2t,
\qquad
r=v-t-\varepsilon,
\]

and is valid exactly when `r>=0`, equivalently `v>=e-2`. It covers every
`n>=33` and the ten earlier values

```text
13,18,19,23,24,25,28,29,30,31.
```

The remaining fourteen values

```text
9,10,11,12,14,15,16,17,20,21,22,26,27,32
```

have explicit exactly checked witnesses. No witness is asserted to be a
minimizer.

EXACT THEOREM: for every `n>=9`, the resulting cyclic order `sigma_n` is a
permutation of `{2,...,n}` and satisfies

\[
W(\sigma_n)\le T_n.
\]

The proof separately checks:

- all adjacent products;
- all positional-distance-two products, including the cyclic all-triple
  endpoint case;
- all positional-distance-three products;
- every pair crossing the displayed cut;
- every distance `q>=4` via
  `n(n-1)<2d(d-1)=4T_n<=qT_n`.

In the symbolic family, `(d,d-1)` occurs at distance two and has product
`2T_n`, so in fact `W(sigma_n)=T_n` there. Only the required upper inequality
is used asymptotically.

## Consequences

The exact chain

\[
H_n\le B_n\le W_n\le W(\sigma_n)\le T_n
\]

and the two endpoint limits give

\[
\boxed{{B_n\over n^2}\longrightarrow{8\over25}},
\qquad
\boxed{{W_n\over n^2}\longrightarrow{8\over25}}.
\]

For `n>=12`, regular-direction core feasibility and the exact insertion theorem
give

\[
R_2^*(n)\le{(n-1)T_n\over\pi},
\qquad
\boxed{
\limsup_{n\to\infty}{R_2^*(n)\over n^3}
\le{8\over25\pi}
}.
\]

This is an upper coefficient, not a proved geometric limit or exact geometric
leading constant. The cases `n=9,10,11` are combinatorial witnesses only;
insertion is not invoked there.

## Verification

- Source and tests compile.
- Focused product-distance tests pass `27/27`.
- Integrated product-distance/zigzag/tail/insertion tests pass `42/42`.
- Full pytest passes `155/155` when run outside the filesystem sandbox so
  pytest can use its system temporary directory.
- Checked-artifact semantic verification accepts 4 certificates, 76 local
  brackets, and the `n=3..6` summary.
- Independent exact checks cover all symbolic local constraints through
  `n=5000`, with additional large-index spot checks; the repository regression
  checks every `9<=n<=1000` and selected full all-pairs scores.
- Independent mathematical and implementation audits both pass without a
  residual finding.
- Two sandboxed full-pytest attempts failed only because pytest could not
  create a temporary directory; both failures are preserved in `EVIDENCE.md`.
- Ruff, strict UTF-8, trailing-whitespace, 88 unique equation-tag, 171
  balanced display-pair, complete-diff, exact 11-path scope, and
  `git diff --check` checks pass.

## Decisions And Limitations

- The production generator performs no search or enumeration.
- The canonical factorial enumerator remains hard-bounded to `n<=11`.
- Finite exact search was used only to falsify candidates and identify the
  construction and exceptional witnesses; it is not the all-`n` proof.
- Exact finite formulas and second-order asymptotics for `B_n` and `W_n`
  remain open.
- The geometric lower and upper coefficients still do not match.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** compile, focused, integrated, full-suite,
  checked-artifact, independent exact, two-agent audit, documentation, and
  final diff/hygiene checks pass.
- **Files changed:** `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`,
  `start.md`, `research/ALL_N_LOWER_BOUND.md`,
  `research/NEXT_RESEARCH_STEPS.md`,
  `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `src/power_ringmin/product_distance.py`,
  `tests/test_product_distance.py`, and this three-file task dossier.
- **Files to read first:** `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `src/power_ringmin/product_distance.py`,
  `tests/test_product_distance.py`, and this dossier.

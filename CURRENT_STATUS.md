# CURRENT_STATUS - power-ringmin

Last update: 2026-07-14

- **Current phase:** matching product-distance upper construction.
- **Current task:** prove or refute an explicit cyclic order with threshold
  `T_n=d_n(d_n-1)/2` for every `n>=9`, and derive the exact justified
  asymptotic consequences.
- **Task dossier:**
  `ops/TASK-20260714__eight_twenty_fifths_upper_construction/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Exact Construction Theorem

For `n>=9`, put

\[
d_n=\left\lceil{4n+8\over5}\right\rceil,
\qquad
T_n={d_n(d_n-1)\over2}.
\]

EXACT THEOREM: there is an explicit cyclic order `sigma_n` of the core
`{2,...,n}` satisfying

\[
W(\sigma_n)\le T_n.
\]

Write `v=n-d_n+1` and `e=d_n-4v`. According to `n mod 5`, the value of `e`
is `6,7,8,4,5` for residues `0,1,2,3,4`. The symbolic block construction is
valid exactly when `v>=e-2`. It covers every `n>=33` and

```text
13,18,19,23,24,25,28,29,30,31.
```

The complementary values

```text
9,10,11,12,14,15,16,17,20,21,22,26,27,32
```

are covered by fourteen explicit exactly checked orders. They are witnesses,
not asserted minimizers. The production generator performs no search or
enumeration, and the canonical factorial enumerator remains hard-bounded to
`n<=11`.

The proof treats separately:

- adjacent products;
- positional-distance-two products;
- positional-distance-three products;
- every closing pair across the displayed cut;
- automatic distances `q>=4` via
  `n(n-1)<2d_n(d_n-1)=4T_n<=qT_n`.

In the symbolic family, `(d_n,d_n-1)` occurs at distance two and realizes
score `T_n` exactly.

## Exact Asymptotic Consequences

The established lower obstruction and the new construction give

\[
H_n\le B_n\le W_n\le W(\sigma_n)\le T_n.
\]

Because both endpoint sequences divided by `n^2` tend to `8/25`, the squeeze
theorem proves

\[
\boxed{
{B_n\over n^2}\longrightarrow{8\over25},
\qquad
{W_n\over n^2}\longrightarrow{8\over25}
}.
\]

For `n>=12`, regular-direction core feasibility and the exact radius-one
insertion theorem give

\[
R_2^*(n)\le{(n-1)T_n\over\pi},
\qquad
\boxed{
\limsup_{n\to\infty}{R_2^*(n)\over n^3}
\le{8\over25\pi}
}.
\]

This is a geometric upper coefficient only. No convergence or exact geometric
leading constant is claimed, and insertion is not invoked for `n=9,10,11`.

## Verification And Provenance

- CURRENT LOCAL VERIFIED FACT: changed source and tests compile.
- CURRENT LOCAL VERIFIED FACT: focused product-distance tests pass `27/27`.
- CURRENT LOCAL VERIFIED FACT: integrated product-distance, zigzag,
  induced-subset, and insertion tests pass `42/42`.
- CURRENT LOCAL VERIFIED FACT: full pytest passes `155/155` outside the
  filesystem sandbox. Two prior sandboxed attempts reached 31 setup errors
  only because pytest could not create a temporary directory; no test body
  failed, and the failures are preserved in the task evidence.
- CURRENT LOCAL VERIFIED FACT: checked-artifact semantic verification accepts
  4 certificates, 76 local brackets, and the `n=3..6` summary.
- CURRENT LOCAL VERIFIED FACT: independent exact checks cover every symbolic
  local constraint through `n=5000`, exceptional all-pairs and closing scores,
  and additional large-index spots through at least `n=1,000,001`.
- CURRENT LOCAL VERIFIED FACT: independent mathematical and implementation
  audits pass with no residual finding.
- CURRENT LOCAL VERIFIED FACT: Ruff, strict UTF-8, trailing-whitespace, 88
  unique equation-tag, 171 balanced display-pair, complete-diff, exact
  11-path scope, and `git diff --check` checks pass.
- CURRENT HOSTED STATUS: GitHub Actions for the current worktree has not been
  independently verified.

## Residual Limitations

- Exact finite formulas, second-order asymptotics, and optimal-order
  classifications for `B_n` and `W_n` remain open.
- The upper coefficient `8/(25*pi)` does not match the induced-subset lower
  coefficient and is not proved geometrically exact.
- The fourteen initial witnesses are not claimed to minimize `W`.
- Finite canonical core-order enumeration remains bounded to `n=3..11`.

## Proposed Next Task

Document the fixed-order angular/STN equivalence and endpoint semantics, as
already prioritized in the research roadmap. Do not begin that task in this
chat.

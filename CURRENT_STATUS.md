# CURRENT_STATUS - power-ringmin

Last update: 2026-07-13

- **Current phase:** positional-distance-two constraints are proved to make the adjacent product-distance relaxation strict exactly from `n=9` onward.
- **Current task:** Characterize adjacent equality cycles and decide `B_n=W_n^(<=2)` versus `A_n` for all `n>=9`.
- **Task dossier:** `ops/TASK-20260713__distance_two_adjacent_strictness/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Current Exact Result

For
\[
A_n=\min_\sigma\max_k\sigma_k\sigma_{k+1},
\qquad
B_n=W_n^{(\le2)},
\]
the adjacent optimum remains
\[
A_3=6,
\qquad
A_n=
\left(\left\lfloor{n\over2}\right\rfloor+1\right)
\left(\left\lceil{n\over2}\right\rceil+2\right)
\quad(n\ge4).
\]

The equality cases are now necessary and sufficient.

- For even `n=2t`, an `A_n`-optimal cycle has no low-low edge and its unique
  high-high edge is `{t+1,t+2}`. Removing that edge leaves an alternating
  Hamilton path on highs `{t+1,...,2t}` and lows `{2,...,t}`, with endpoints
  `t+1,t+2`; every crossing product is at most `A_n`.
- For odd `n=2t+1`, an `A_n`-optimal cycle has no low-low edge and its only
  high-high edges are `{t+1,t+2}` and `{t+1,t+3}`. Removing the middle high
  `t+1` from the forced segment leaves an alternating Hamilton path on highs
  `{t+2,...,2t+1}` and lows `{2,...,t}`, with endpoints `t+2,t+3`; every
  crossing product is at most `A_n`.

EXACT THEOREM:
\[
\boxed{
B_n=A_n\quad(3\le n\le8),
\qquad
B_n>A_n\quad(n\ge9).
}
\]

The equality side uses explicit `patterns.interleave` witnesses. For
strictness, each low labels an active-high path edge `xy` and distance two
would require `xy<=2A_n`. A terminal block of mutually incompatible highs
requires more distinct compatible lows than exist. The only incidence-count
exception is `n=12`; there, the degree budget of `{7,8,9}` is exhausted by
the two edges to high `12` and the edge labelled by low `6`, disconnecting
`{10,11}`.

No cyclic-order enumeration beyond `n=11` is used in this theorem.

## Consequences For The Full Surrogate And Power-Ringmin

Because `W_n>=B_n`,
\[
W_n>A_n\qquad(n\ge9).
\]
This resolves the former strictness gap `n=12..32`; the tail obstruction is no
longer needed to prove strictness there. It remains useful as a quantitative
lower bound and still first exceeds `A_n` at `n=33`.

The theorem does not give a formula for `B_n` or `W_n`, does not prove
`B_n=W_n` beyond `n=11`, and does not determine when positional distances at
least three first become essential.

For regular-direction constructions, the accepted implications remain
\[
R_2^*(n)\le{(n-1)W_n\over\pi}\qquad(n\ge12),
\]
and the zigzag construction retains coefficient `1/(2*pi)`. Strictness of a
lower relaxation does not by itself sharpen this feasible-radius upper bound
or prove any exact geometric optimum.

## Finite Exact Regression

VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): the bounded canonical,
no-floating-point enumeration remains restricted to `n=3..11`. Its
distance-one objectives are
\[
(6,12,15,20,24,30,35,42,48),
\]
and its distance-two objectives are
\[
(6,12,15,20,24,30,36,45,50).
\]
The latter equal the full `W_n` values and minimizer sets throughout this
bounded range. This is regression evidence only; the all-`n` strictness proof
is the high/low incidence theorem above.

The full bounded values remain
\[
(W_3,\dots,W_{11})=(6,12,15,20,24,30,36,45,50)
\]
with canonical minimizer counts
\[
(1,1,1,2,2,4,12,72,24).
\]

## Other Stable Context

The induced-subset lower bound and zigzag upper construction still give
\[
{2(\sqrt2-1)\over3\pi}
\le
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\le
\limsup_{n\to\infty}{R_2^*(n)\over n^3}
\le{1\over2\pi}.
\]
The exact leading coefficient and existence of a limit remain open. The full
and core feasible-radius sets remain equal for every `n>=12`; the threshold
is sufficient, not known minimal. The former `n^3/(6*pi)` asymptotic targets
remain disproved.

## Verification And CI Provenance

- CURRENT LOCAL VERIFIED FACT: Python compilation passes for the changed
  source and test files.
- CURRENT LOCAL VERIFIED FACT: focused product-distance tests pass `16/16`,
  and integrated product-distance/zigzag/tail/insertion tests pass `31/31`.
- CURRENT LOCAL VERIFIED FACT: the adjacent equality classifier accepts the
  `patterns.interleave` construction for `n=4..1000`.
- CURRENT LOCAL VERIFIED FACT: exact parameter-only incidence checks pass for
  `199991` values in `n=9..200000`, excluding the separately proved `n=12`;
  this is diagnostic formula verification, not cyclic-order enumeration or
  the all-`n` proof.
- CURRENT LOCAL VERIFIED FACT: the bounded equality classifier was checked
  against every canonical adjacent score for `n=4..11`; no order enumeration
  beyond `n=11` was run.
- CURRENT LOCAL VERIFIED FACT: full pytest passes `144/144`.
- CURRENT LOCAL VERIFIED FACT: checked-artifact semantic verification accepts
  4 certificates, 76 local brackets, and the `n=3..6` summary.
- CURRENT LOCAL VERIFIED FACT: exact ten-path scope, strict UTF-8, trailing
  whitespace, 32 unique equation tags, complete diff, and `git diff --check`
  inspections pass.
- CURRENT HOSTED STATUS: GitHub Actions for the current `HEAD` has not been
  independently verified.

## Proposed Next Task

Document the fixed-order angular/STN equivalence and endpoint semantics, as
already prioritized in the research roadmap. Do not begin that task in this
chat.

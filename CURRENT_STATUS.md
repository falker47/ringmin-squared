# CURRENT_STATUS - power-ringmin

Last update: 2026-07-17

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** global continuous five-prefix coefficient optimization.
- **Repository state at startup:** clean main worktree at commit
  9fc4b2caeb385a7cd34c62fc494fd91182935f06, tracking origin/main.
- **Implementation state:** the full compact proof, exact optimizer,
  coefficient comparison, sole standalone diagnostic, authoritative research
  synchronization, regression checks, independent audits, and final diff
  inspection are complete.
- **Current blocker:** none.
- **Current next atomic action:** user manual review and commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

Starting from CR28cr--CR28dd and CR28dr--CR28dw, optimize globally the fixed
\(k=5\) continuous coefficient over its complete ordered compact closure.
Classify every clipping regime and transition, audit density/weight
collisions and every compact face, determine the exact optimizer and
coefficient, prove

\[
C_{5,*}>C_{5,\mathrm{rat}}>C_{4,*},
\]

and add one standalone exact diagnostic.

Finite rounding at the irrational optimizer, growing-\(k\) claims, and
production, artifact, schema, backend, test-module, certificate, or
enumeration changes are excluded. The existing rational \(n\ge234\) theorem
is retained without alteration.

## Exact Compact Classification

Coordinatewise clipping reduces the full eleven-parameter problem to

\[
\overline C_5
=p(\alpha)+\sum_{i=1}^5
(\beta_{i-1}-\beta_i)\Phi_{1+\alpha}(\beta_i).
\]

There are exactly 21 ordered regimes \(H^hM^m0^z\),
\(h+m+z=5\). The 15 words with a trailing zero are nonwinning for
\(\alpha>1/3\). The exact active winner sequence is

\[
MMMMM,\ HMMMM,\ HHMMM,\ HHHMM,\ HHHHM,
\]

with the formal HHHHH transition beyond \(\alpha=1\). The new \(m=4\)
mixed predecessor margin is positive. Every clipping join, density
collision, internal and outer weight face, unused segment, and compact
density face is classified.

## Exact Optimizer

Let

\[
d_5=183342238504950468196395903.
\]

The unique global density is

\[
\boxed{
\alpha_{5,*}
={422413777961580309772684503
 -10047852311701\sqrt{d_5}
 \over661485317418210151348973103}.
}
\]

It is the smaller root of

\[
661485317418210151348973103a^2
-844827555923160619545369006a
+241763928731615232919074902=0
\]

and lies in

\[
{432907432458521\over10^{15}}
<\alpha_{5,*}<
{432907432458522\over10^{15}}.
\]

With

\[
D=30143556935103,
\quad
(N_1,\ldots,N_5)
=(26881208992898,23392470652668,19595592993288,
15335681473008,10223787648672),
\]

and \(A_*=3\alpha_{5,*}-1\), the five exact pairs are

\[
\boxed{
\beta_{i,*}
={(D-N_i)+(D+3N_i)\alpha_{5,*}\over4D},
\qquad
\lambda_{i,*}
={4N_iA_*\over(D-N_i)+(D+3N_i)\alpha_{5,*}}.
}
\]

All cutoff, weight, and middle-branch inequalities are strict. Equality in
the clipping loss, normalized-simplex certificate, and scalar envelope forces
this unique eleven-tuple.

## Exact Coefficient And Comparisons

\[
\boxed{
C_{5,*}
={346693217780244687187063490332457027500975566238012204
 +1228130489996268437333105902690103574002\sqrt{d_5}
 \over1312688475479610714750859896048564873968757997852345827}.
}
\]

It lies in

\[
{276777463862376\over10^{15}}
<C_{5,*}<
{276777463862377\over10^{15}}
\]

and satisfies its recorded primitive quadratic. Rational separators and
positive squared-radical margins prove

\[
\boxed{
C_{5,*}>C_{5,\mathrm{rat}}>{75\over271}>C_{4,*}.
}
\]

The fixed-parameter charging theorem and additive cyclic-ratio relation give

\[
\liminf_{n\to\infty}{\Lambda_n\over n^3}\ge C_{5,*},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}\ge{C_{5,*}\over\pi}.
\]

## Verification

- The sole new standalone standard-library diagnostic passes its clipping,
  transition, collision, polynomial, isolation, branch, coefficient, and
  comparison assertions.
- Independent mathematical audits agree on all exact transition, optimizer,
  pair, coefficient, and comparison data; their wording corrections have
  been applied to the compact-face proof.
- Ruff check and format check pass for the sole new diagnostic.
- The focused fixed-order suite passes 101 tests; the full suite passes 283
  tests.
- Schema checks, four artifact certificates with 76 local brackets, and the
  four historical exact diagnostics all pass.
- The source audit finds 366 unique equation tags, balanced delimiters and
  LaTeX environments, valid UTF-8, synchronized theorem statements, no
  prohibited scope changes, and a clean `git diff --check`.
- Three independent audits agree on the optimizer algebra, branch/face audit,
  coefficient comparisons, and final source synchronization; all concrete
  wording corrections found during review are applied.

## Evidence Classification And Limitations

- The compact reduction, branch and face classification, optimizer,
  coefficient, strict comparisons, and liminf consequences are **exact
  method-specific theorems**.
- The standalone script is a **verified bounded exact computation** that
  corroborates but does not replace the all-real proof.
- \(C_{5,*}\) is the global optimum of this fixed five-prefix template, not
  an exact residual, limit, or geometric leading constant.
- The finite \(n\ge234\) theorem remains specific to
  \(C_{5,\mathrm{rat}}\); no finite rounding is claimed at \(C_{5,*}\).
- No growing-\(k\), convergence, production, artifact, schema, backend,
  test-module, certificate, or enumeration conclusion is added.

## Files In Scope

- research/FIXED_ORDER_CYCLE_RATIO.md
- research/ALL_N_LOWER_BOUND.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260717__global_five_prefix_optimization/

## Proposed Next Task

In a fresh STRICT task, derive an exact symbolic count of
relation-compatible, equivalently full-optimal, scaffold bijections from the
nested Ferrers thresholds, without enumerating path permutations.

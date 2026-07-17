# CURRENT_STATUS - power-ringmin

Last update: 2026-07-17

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** explicit rational five-prefix asymptotic witness at
  \(\alpha=13/30\).
- **Repository state at startup:** clean main worktree at commit
  \(8dc7d2313349136c5c1fc21e098829dcffb2b742\), tracking origin/main.
- **Implementation state:** exact derivation, sole standalone Fraction
  diagnostic, authoritative synchronization, focused/full regressions, three
  independent audits, and final diff inspection are complete.
- **Current blocker:** none.
- **Current next atomic action:** user review and, if accepted, manual commit.
- **Awaiting user review:** yes.

## Objective And Scope

Specialize the exact normalized prefix simplex at \(k=5\), fix
\(\alpha=13/30\), derive exact all-middle cutoffs and weights, and combine
this fixed tuple with the already proved arbitrary finite-prefix charging
theorem. The requested output is one explicit rational asymptotic coefficient
strictly larger than \(C_{4,*}\), with the corresponding liminf consequences.

Finite rounding, global \(k=5\) optimization, growing-\(k\) uniformity,
production code, tests, artifacts, schemas, interval backends, serialized
certificates, enumeration, and new geometric input are excluded.

## Exact Five-Prefix Witness

Put

\[
D=30143556935103,
\]

\[
(N_1,\ldots,N_5)
=(26881208992898,23392470652668,19595592993288,
15335681473008,10223787648672).
\]

The exact fifth simplex point is \(x_i=N_i/D\), with

\[
M_5={722599396919860307414438404
 \over2725902074099388500860861827}.
\]

At

\[
\alpha={13\over30},\qquad s={43\over30},\qquad A={3\over10},
\]

take

\[
\beta_i={s+Ax_i\over4},
\qquad
\lambda_i={Ax_i\over\beta_i}.
\]

Exact algebra proves

\[
0<\beta_5<\cdots<\beta_1<\alpha<1,
\qquad
{s\over4}<\beta_i<{s\over3},
\qquad
0<\lambda_5<\cdots<\lambda_1<1.
\]

Thus the tuple is strictly all-middle and its integer cutoffs are admissible
for every sufficiently large \(n\), without a finite threshold claim.

## Coefficient And Comparison

The exact coefficient is

\[
\boxed{
C_{5,\mathrm{rat}}
={2263404122555368590593580404287
 \over8177706222298165502582585481000}.
}
\]

Using the rational separator \(75/271\), exact positive integer margins prove

\[
\boxed{
C_{5,\mathrm{rat}}>{75\over271}>C_{4,*}.
}
\]

Consequently

\[
\boxed{
\liminf_{n\to\infty}{\Lambda_n\over n^3}
\ge C_{5,\mathrm{rat}},
\qquad
\liminf_{n\to\infty}{R_2^*(n)\over n^3}
\ge{C_{5,\mathrm{rat}}\over\pi}.
}
\]

The second statement is only the normalized consequence of the existing
exact additive cyclic-ratio relation; it adds no new geometric lemma.

## Verification

- The standalone diagnostic passes every recurrence, simplex, stationarity,
  parameter, branch, coefficient, and exact-comparison assertion.
- Ruff lint and format checks pass after one recorded mechanical format fix.
- All 101 fixed-order cycle-ratio tests and all 283 local tests pass.
- The independent artifact verifier accepts 4 certificates and 76 local
  brackets; all 4 schema-validation tests pass.
- The primary proof has 327 unique equation tags. Display and LaTeX
  environments balance across every changed Markdown source.
- All intended changed/new files are UTF-8 without BOM, LF-only, and
  LF-terminated after the dossier control-character correction.
- Three independent read-only audits pass. Complete tracked and untracked
  diff inspection, protected-scope checks, encoding checks, and
  `git diff --check` pass.

## Evidence Classification And Limitations

- The fifth simplex row, rational parameter identities, strict all-middle
  ordering, coefficient identity, separator comparison, and liminf
  consequences are **exact method-specific theorems**.
- The standalone script is a **verified exact computation** that corroborates
  but does not replace the written proof.
- \(C_{5,\mathrm{rat}}\) is an explicit witness, not \(C_{5,*}\); no global
  five-prefix optimum is claimed.
- No finite rounding, growing-\(k\) passage, exact residual, convergence
  theorem, exact leading constant, production computation, serialized
  certificate, or new geometric claim is added.

## Files In Scope

- research/FIXED_ORDER_CYCLE_RATIO.md
- research/ALL_N_LOWER_BOUND.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260717__five_prefix_explicit_asymptotic_witness/

## Proposed Next Task

In a fresh STRICT task, derive the exact finite floor/ceiling theorem for this
fixed rational five-prefix tuple, including the minimal uniform admissibility
threshold and any exact comparison with \(C_{5,\mathrm{rat}}n^3\), without
globally optimizing the \(k=5\) parameters.

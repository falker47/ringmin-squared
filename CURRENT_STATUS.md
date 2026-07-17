# CURRENT_STATUS - power-ringmin

Last update: 2026-07-17

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** exact finite floor/ceiling theorem for the fixed rational
  five-prefix witness of CR28dx--CR28dz3.
- **Repository state at startup:** clean `main` worktree at commit
  `941d0b6f5a7be00f71552bfd3771a841a7c05782`, tracking `origin/main`.
- **Implementation state:** exact threshold, literal and integer-closed
  bounds, exact rounded remainder, uniform comparison, sole standalone
  diagnostic, authoritative research/project synchronization, focused/full
  regressions, three independent audits, and final diff inspection are
  complete.
- **Current blocker:** none.
- **Current next atomic action:** user review and, if accepted, manual commit.
- **Awaiting user review:** yes.

## Objective And Scope

Keep exactly

\[
\alpha={13\over30},
\qquad
x_i={N_i\over30143556935103},
\qquad
\beta_i={43/30+(3/10)x_i\over4},
\qquad
\lambda_i={(3/10)x_i\over\beta_i},
\]

and derive the exact finite specialization of CR28dw: minimal uniform
admissibility/middle-branch threshold, literal
\(\mathcal B_{5,n}\), integer closure \(\mathcal I_{5,n}\), exact
floor/ceiling-error remainder, and a uniform comparison with
\(C_{5,\mathrm{rat}}n^3\).

Global \(k=5\) optimization, growing-\(k\) limits, and changes to production
code, tests, artifacts, schemas, interval backends, serialized certificates,
enumerators, or enumeration limits are excluded.

## Exact Uniform Domain

Define

\[
r_n=\left\lfloor{13n\over30}\right\rfloor,
\qquad
s_{i,n}=\lceil\beta_i n\rceil,
\qquad
s_{0,n}=r_n,
\qquad
S_n=n+r_n.
\]

The minimal uniform threshold for

\[
2\le r_n\le n-2,
\qquad
1\le s_{5,n}<\cdots<s_{1,n}\le r_n-1,
\qquad
{S_n\over4}<s_{i,n}<{S_n\over3}
\]

is

\[
\boxed{n=234}.
\]

At \(n=233\),

\[
(r_n;s_{1,n},\ldots,s_{5,n})=(100;100,98,95,93,90),
\]

so the first segment is empty. Exact rows \(234\) through \(246\) close the
finite bridge; the symbolic tail starts at \(247\). At \(n=234\), the
segment lengths are \((1,2,2,3,3)\), and all five lower/upper middle gaps
are strictly positive.

## Literal Bound And Integer Closure

The user-fixed weights are retained in

\[
F_{i,n}
=G_{n,\lambda_i}(s_{i,n})
={\lambda_i(4S_ns_{i,n}-S_n^2-2\lambda_i s_{i,n}^2)
 \over2(2-\lambda_i)}.
\]

They are not replaced by the finite clipped optima
\(4-S_n/s_{i,n}\). Define

\[
\boxed{
\mathcal B_{5,n}
=P_{r_n,n}+\sum_{i=1}^5(s_{i-1,n}-s_{i,n})F_{i,n},
}
\]

\[
\boxed{
\mathcal I_{5,n}
=\left\lceil\mathcal B_{5,n}\right\rceil
=P_{r_n,n}
+\left\lceil\sum_{i=1}^5(s_{i-1,n}-s_{i,n})F_{i,n}\right\rceil.
}
\]

CR28dw, CR28ap, and integrality of \(\Lambda_n\) give

\[
\Lambda_n\ge\mathcal I_{5,n}\ge\mathcal B_{5,n}
\qquad(n\ge234).
\]

## Exact Remainder And Uniform Sign

With the exact floor/ceiling errors \(\eta_n,\varepsilon_{i,n}\), the
literal rounded-bound remainder has the form

\[
\mathcal B_{5,n}-C_{5,\mathrm{rat}}n^3
=\left({13\over30}+K\eta_n\right)n^2+Q_n n+T_n,
\]

where

\[
K={34730769300472139183348711
 \over90863402469979616695362060900}>0.
\]

The simplex stationarity equations cancel every ceiling error from the
quadratic coefficient. Exact rational estimates give

\[
Q_n>-{25\over2},
\qquad
T_n>-{109\over6},
\]

and therefore

\[
\mathcal B_{5,n}-C_{5,\mathrm{rat}}n^3
>{13\over30}n^2-{25\over2}n-{109\over6}>0
\qquad(n\ge234).
\]

There are no failure rows on the minimal uniform domain. Consequently

\[
\boxed{
\Lambda_n\ge\mathcal I_{5,n}\ge\mathcal B_{5,n}
>C_{5,\mathrm{rat}}n^3
\qquad(n\ge234),
}
\]

\[
\boxed{
R_2^*(n)>{\mathcal I_{5,n}\over\pi}-n^2
>{C_{5,\mathrm{rat}}\over\pi}n^3-n^2
\qquad(n\ge234).
}
\]

## Verification

- The sole new standalone `Fraction` diagnostic passes every parameter,
  boundary-row, predicate-failure, symbolic-margin, literal-floor, integer
  closure, stationarity, exact-remainder, and uniform-sign assertion.
- Ruff lint and format checks pass after the recorded mechanical formatting
  corrections.
- All 101 fixed-order cycle-ratio tests and all 283 local tests pass.
- The independent artifact verifier accepts 4 certificates and 76 local
  brackets; all 4 schema-validation tests pass.
- The primary proof has 343 unique equation tags. Display math and aligned
  environments balance across every changed Markdown source.
- Three independent read-only audits pass. Exactly the ten intended files are
  present; encodings, whitespace, protected-path scope, complete diff, and
  `git diff --check` pass.

## Evidence Classification And Limitations

- The threshold \(234\), literal and integer-closed bounds, exact rounded
  remainder, uniform strict comparison, and finite geometric consequence are
  **exact finite method-specific theorems**.
- The standalone script is a **verified bounded exact computation** that
  corroborates but does not replace the finite bridge and symbolic tail.
- \(C_{5,\mathrm{rat}}\) remains one fixed rational witness, not the global
  \(k=5\) optimum.
- The exact remainder belongs to \(\mathcal B_{5,n}\); it is not the true
  residual of the block, \(\Lambda_n\), or the geometric problem.
- No growing-\(k\) result, convergence theorem, exact leading coefficient,
  production computation, serialized certificate, or new geometric lemma is
  added.

## Files In Scope

- research/FIXED_ORDER_CYCLE_RATIO.md
- research/ALL_N_LOWER_BOUND.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260717__five_prefix_finite_theorem/

## Proposed Next Task

In a fresh STRICT task, derive an exact symbolic count of
relation-compatible, equivalently full-optimal, scaffold bijections from the
nested Ferrers thresholds, without enumerating path permutations.

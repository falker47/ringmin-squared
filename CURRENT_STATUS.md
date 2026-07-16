# CURRENT_STATUS - power-ringmin

Last update: 2026-07-16

- **Current phase:** corrective synchronization of the exact normalized
  prefix-simplex theorem.
- **Current task:** synchronize the normalized-prefix result across
  authoritative project memory and correct the task dossier's obsolete
  file-scope claims.
- **Task dossier:** `ops/TASK-20260716__normalized_prefix_simplex/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Corrective Scope

- Synchronized `start.md`, `PROJECT_KNOWLEDGE.md`, and this status with the
  exact fixed-\(k\) normalized simplex lemma already proved in
  `research/FIXED_ORDER_CYCLE_RATIO.md`.
- Corrected the normalized-prefix dossier so it no longer claims that the
  authoritative project-memory files were intentionally excluded.
- Preserved the later exact three-prefix charging theorem and its coefficient
  \(C_{3,*}\); this correction does not supersede or weaken those results.
- Inspected the mathematical proof and dossier-local `Fraction` diagnostic;
  no real defect was found, so neither is modified.
- Kept production code, tests, artifacts, schemas, backends, certificates,
  enumerators, and enumeration limits unchanged.

## Exact Normalized Prefix-Simplex Theorem

For every fixed \(k\ge1\), define

\[
F_k(x_1,\ldots,x_k)
=\sum_{i=1}^k(x_{i-1}-x_i)x_i^2,
\qquad x_0=1,
\]

and

\[
M_k=\max_{1\ge x_1\ge\cdots\ge x_k\ge0}F_k(x_1,\ldots,x_k),
\qquad M_0=0.
\]

The compact maximum exists and has a unique strictly interior maximizer:

\[
1>x_1>x_2>\cdots>x_k>0.
\]

Writing

\[
q_k={2\over3(1-M_{k-1})},
\]

the value and forward-ratio recurrences are

\[
M_k={q_k^2\over3}
={4\over27(1-M_{k-1})^2},
\qquad
q_1={2\over3},
\qquad
q_{m+1}={2\over3-q_m^2}.
\]

At the maximizer, the consecutive ratios \(r_i=x_i/x_{i-1}\) satisfy

\[
r_i=q_{k-i+1},
\qquad
r_k={2\over3},
\qquad
r_i={2\over3-r_{i+1}^2}
\quad(1\le i<k).
\]

Moreover, \(M_k\) is strictly increasing and

\[
M_k\nearrow{1\over3}.
\]

## Exact Agreement With \(k=1,2,3\)

The all-\(k\) theorem recovers exactly:

| \(k\) | unique maximizer \((x_1,\ldots,x_k)\) | \(M_k\) | \(M_k/8\) |
|---:|---|---:|---:|
| 1 | \((2/3)\) | \(4/27\) | \(1/54\) |
| 2 | \((18/23,12/23)\) | \(108/529\) | \(27/1058\) |
| 3 | \((1058/1263,276/421,184/421)\) | \(1119364/4785507\) | \(279841/9571014\) |

These are the previously documented one-, two-, and three-prefix simplex
points and residual scale factors.

## Exact Normalized-Envelope Classification

For

\[
p(\alpha)={(1-\alpha)(\alpha^2+4\alpha+1)\over6},
\qquad
E_k(\alpha)=p(\alpha)+{M_k\over8}(3\alpha-1)^3,
\]

one has uniform monotone convergence on \([1/3,1]\):

\[
E_k(\alpha)\nearrow
E_\infty(\alpha)
=p(\alpha)+{(3\alpha-1)^3\over24}.
\]

On the full compact interval, the unique maximum is the degenerate endpoint

\[
\alpha=1,
\qquad
E_\infty(1)={1\over3}.
\]

On the strict domain \([1/3,1)\), this value is only a nonattained supremum.
On the limiting all-middle closure \([1/3,1/2]\), the unique maximum is

\[
\alpha_{\rm mid}={13-2\sqrt2\over23},
\qquad
E_\infty(\alpha_{\rm mid})={434+4\sqrt2\over1587}.
\]

## Protected Limitations

- The theorem concerns the normalized compact polynomial for each fixed
  \(k\).
- No combined-height or one-use charging theorem has been proved beyond three
  selected prefixes.
- No uniform interchange between \(k\) and \(n\) has been justified.
- Neither \(M_k\to1/3\) nor either envelope value gives a new bound for
  \(\Lambda_n\) or \(R_2^*(n)\).
- No production path or established three-prefix bound is changed.

## Verification

- `python -B ops\TASK-20260716__normalized_prefix_simplex\fraction_diagnostic.py`:
  all exact checks passed for \(k=1,\ldots,8\), including 203,489 literal
  denominator-12 grid tuples.
- Focused historical/simplex pytest selection: 8 passed.
- Ruff on the unchanged standalone diagnostic: passed.
- Anchored display delimiters, inline delimiters, LaTeX environments, code
  fences, and trailing whitespace are balanced or clean in all synchronized
  sources and the canonical proof/roadmap.
- The cyclic-ratio proof note retains 273 unique equation tags with no
  duplicate.
- Cross-source theorem values, domains, evidence classifications, and
  protected limitations agree.
- The corrective diff contains only the six documentation files listed below;
  the proof, diagnostic, tests, production, and protected paths have no diff.
- `git diff --check` and final changed-path inspection pass.
- Independent read-only audits found no residual mathematical,
  diagnostic, synchronization, Markdown, equation, or scope defect after the
  corrective findings were applied.

## Files In Corrective Diff

- `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md`: synchronized
  authoritative project memory.
- `ops/TASK-20260716__normalized_prefix_simplex/TASK_STATUS.md`,
  `TASK_LOG.md`, and `EVIDENCE.md`: corrected durable task handoff.
- The proof and `fraction_diagnostic.py` remain unmodified after inspection.

## Proposed Next Task

In a fresh STRICT task, derive an explicit finite floor/ceiling theorem for
the exact irrational three-prefix optimizer, including a minimal or
rigorously sufficient uniform threshold, without changing production,
artifacts, schemas, backends, certificates, or enumeration limits.

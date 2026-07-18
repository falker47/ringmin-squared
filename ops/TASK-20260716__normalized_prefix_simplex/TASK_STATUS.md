# TASK STATUS - Normalized Prefix Simplex

- Task ID: `TASK-20260716__normalized_prefix_simplex`
- Mode: STRICT
- Status: READY_FOR_REVIEW
- Last updated: 2026-07-18
- Blocker: none

## Objective

Solve exactly, for every fixed \(k\ge1\),
\[
M_k=\max_{1\ge x_1\ge\cdots\ge x_k\ge0}
\sum_{i=1}^k(x_{i-1}-x_i)x_i^2,
\qquad x_0=1,
\]
including existence, strict interiority, uniqueness, the proposed ratio
recurrence, an exact recurrence for \(M_k\), monotonicity, the limit, the
limiting polynomial envelope, exact agreement with the documented
\(k=1,2,3\) cases, and independent small-\(k\) `Fraction` diagnostics.

## Scope Guard

- In scope: the normalized compact polynomial lemma, its formal envelope,
  proof-note and roadmap updates, synchronized authoritative project memory,
  and a dossier-local exact diagnostic.
- Out of scope: charging with four or more selected prefixes, any interchange
  of \(k\) and \(n\), finite rounding of prefix certificates, and any new
  bound for \(\Lambda_n\) or \(R_2^*(n)\).
- No production source, test module, API, artifact, schema, example, verifier,
  backend, certificate, enumerator, or enumeration limit is changed.
- `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` record the exact
  lemma and its limitations. The all-\(n\) lower-bound proof note remains
  unchanged because the normalized result supplies no new original-problem
  bound.

## Current Truth

- The proposed ratio recurrence is confirmed exactly.
- The compact maximum exists and is uniquely attained in the strict interior.
- With \(M_0=0\),
  \[
  q_k={2\over3(1-M_{k-1})},
  \qquad
  M_k={4\over27(1-M_{k-1})^2},
  \qquad M_k\nearrow{1\over3}.
  \]
- At the maximizer,
  \[
  r_i=q_{k-i+1},
  \qquad
  r_k={2\over3},
  \qquad
  r_i={2\over3-r_{i+1}^2}.
  \]
- The \(k=1,2,3\) rows agree exactly with the three documented simplex
  values and scale factors.
- The full formal limiting envelope has compact maximum \(1/3\) at the
  degenerate endpoint \(\alpha=1\). On the limiting all-middle closure its
  unique maximum is \((434+4\sqrt2)/1587\) at
  \((13-2\sqrt2)/23\).
- The normalized theorem alone supplies no charging and therefore no
  original-problem coefficient by itself. A later correction combines it with
  the independent arbitrary finite-prefix charging theorem at every fixed
  finite \(k\), obtaining the all-fixed-\(k\) coefficient
  \((434+4\sqrt2)/1587\). See
  `ops/TASK-20260718__all_fixed_k_corollary/`.

## Subsequent Correction - 2026-07-18

The earlier task correctly excluded a new bound from the normalized-simplex
theorem *in isolation*, but its absolute project-wide wording became stale
after arbitrary finite-\(k\) charging was proved. For each fixed \(k\), the
two independent theorems now give a scalar liminf inequality; taking their
supremum requires no \(k=k(n)\), uniform threshold, or interchange of limits.
The append-only chronology is preserved in `TASK_LOG.md`.

## Completion Checklist

- [x] Complete repository startup and inspect the three prior STRICT tasks.
- [x] Derive the Bellman recurrence and global nonnegative certificate.
- [x] Prove existence, strict interiority, uniqueness, ratio recurrence,
  monotonicity, and limit.
- [x] Compare \(k=1,2,3\) exactly with the proof note.
- [x] Classify the full formal and all-middle limiting envelopes.
- [x] Add and run an independent dossier-local `Fraction` diagnostic.
- [x] Synchronize `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`,
  the proof note, roadmap, and task dossier.
- [x] Complete corrective verification, diff inspection, and
  READY_FOR_REVIEW handoff.

## Corrective Verification

- The standalone `Fraction` diagnostic passed for \(k=1,\ldots,8\), including
  all 203,489 denominator-12 grid tuples.
- The focused historical/simplex pytest selection passed all 8 tests.
- Ruff on the unchanged diagnostic passed.
- Cross-source theorem, envelope, case-table, limitation, Markdown, equation,
  changed-path, and protected-scope checks passed.
- `git diff --check` passed.

## Handoff

The bounded task, authoritative synchronization, corrective dossier update,
verification, and independent reviews are complete. No defect was found in
the proof or diagnostic, so both remain unmodified. The worktree is ready for
user review and a manual commit decision.

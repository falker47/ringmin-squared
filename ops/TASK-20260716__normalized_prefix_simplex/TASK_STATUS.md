# TASK STATUS - Normalized Prefix Simplex

- Task ID: `TASK-20260716__normalized_prefix_simplex`
- Mode: STRICT
- Status: READY_FOR_REVIEW
- Last updated: 2026-07-16
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
  proof-note and roadmap updates, and a dossier-local exact diagnostic.
- Out of scope: charging with four or more selected prefixes, any interchange
  of \(k\) and \(n\), finite rounding of prefix certificates, and any new
  bound for \(\Lambda_n\) or \(R_2^*(n)\).
- No production source, test module, API, artifact, schema, example, verifier,
  backend, certificate, enumerator, or enumeration limit is changed.
- `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and the all-\(n\)
  proof note remain unchanged under the user's narrower task-specific
  synchronization instruction.

## Current Truth

- The proposed ratio recurrence is confirmed exactly.
- The compact maximum exists and is uniquely attained in the strict interior.
- With \(M_0=0\),
  \[
  M_k={4\over27(1-M_{k-1})^2},
  \qquad M_k\nearrow{1\over3}.
  \]
- The \(k=1,2,3\) rows agree exactly with the three documented simplex
  values and scale factors.
- The full formal limiting envelope has compact maximum \(1/3\) at the
  degenerate endpoint \(\alpha=1\). On the limiting all-middle closure its
  unique maximum is \((434+4\sqrt2)/1587\) at
  \((13-2\sqrt2)/23\).
- Neither envelope value is a new coefficient bound.

## Completion Checklist

- [x] Complete repository startup and inspect the three prior STRICT tasks.
- [x] Derive the Bellman recurrence and global nonnegative certificate.
- [x] Prove existence, strict interiority, uniqueness, ratio recurrence,
  monotonicity, and limit.
- [x] Compare \(k=1,2,3\) exactly with the proof note.
- [x] Classify the full formal and all-middle limiting envelopes.
- [x] Add and run an independent dossier-local `Fraction` diagnostic.
- [x] Update only the pertinent proof note, roadmap, and task dossier.
- [x] Complete final verification, diff inspection, and READY_FOR_REVIEW
  handoff.

## Handoff

The bounded task, verification, synchronization, and independent reviews are
complete. `CURRENT_STATUS.md` is intentionally unchanged under the explicit
file-scope instruction. The worktree is ready for user review and a manual
commit decision.

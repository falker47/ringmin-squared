# TASK_LOG - TASK-20260718__ferrers_log_asymptotics / Ferrers Log Asymptotics

Append-only. Add a new entry to correct previous information.

## 2026-07-18 - STRICT startup and independent derivation

- **Action:** Read the operating contract, authoritative project memory,
  PG64--PG73, the predecessor Ferrers-count dossier, roadmap, templates, and
  clean Git state; derive the asymptotic locally and commission three
  independent read-only analyses.
- **Result:** The clean `main` worktree was at
  `3472b47e2f10e721b44c504ce3db9355e89ceac6`. Every derivation confirmed
  the proposed linear coefficient and an all-\(m\), \(O(\log m)\) envelope.
- **Interpretation:** The ceiling contributes at most harmonic scale and must
  be kept distinct from the positive lower-comparator correction. The
  singular endpoint is isolated exactly by the factorial component.
- **Evidence:** `EVIDENCE.md#ev-001---startup-scope-and-symbolic-derivation`.
- **Next step:** write PG74--PG85 and the independent residual diagnostic.

## 2026-07-18 - Proof written

- **Action:** Added the exact rounding identity, literal ceiling/no-ceiling
  bound, homogeneous comparator, factorial identity, monotone integral
  estimate, explicit all-\(m\) residual envelope, and complete boundary and
  interpretation audit to the proof note.
- **Result:** The coefficient is
  \(14\log2+6\log3-10\log5-2\), with a quantitative remainder bounded below
  by \(1+\log(5/6)-\log m\) and above by
  \(9/4+\log(2m(2m+1))\) for every \(m\ge3\).
- **Interpretation:** The requested asymptotic theorem follows without a
  nonuniform endpoint estimate, permutation enumeration, matching
  enumeration, or geometric inference.
- **Evidence:** `EVIDENCE.md#ev-001---startup-scope-and-symbolic-derivation`.
- **Next step:** implement and run the standalone residual diagnostic.

## 2026-07-18 - Growing-row diagnostic implemented

- **Action:** Added one standalone standard-library script that builds the
  PG69 factors by integer ceiling arithmetic, sums their logarithms directly,
  and audits the literal no-ceiling, lower-comparator, homogeneous, and dual
  row quantities on thirteen increasing rows.
- **Result:** Rows \(m=3,4,5,6,7,16,\ldots,262144\) satisfy every explicit
  theorem envelope. The residual increases from `2.38777979993` to
  `10.7381128464`; the estimated linear coefficient reaches
  `-1.79860390184`. Exact integer assertions cover both terminal thresholds,
  the first universal row, the factors \(m,m-1,1\), and equality of the row
  and column factor multisets.
- **Interpretation:** These are bounded numerical observations that
  corroborate but neither prove nor sharpen PG84--PG85. No permutation or
  matching is enumerated.
- **Evidence:** `EVIDENCE.md#ev-002---growing-row-residual-diagnostic`.
- **Next step:** run repository verification and independent audits.

## 2026-07-18 - Verification and audit corrections

- **Action:** Ran the predecessor Ryser oracle, compile and Ruff checks, 49
  focused tests, the complete suite, four schema tests, and checked-artifact
  verification; commissioned independent proof, diagnostic, and cross-file
  audits and incorporated their clarity and finite-scope findings.
- **Result:** All final checks pass. Two Ruff format checks requested only
  mechanical formatting. The first complete-suite run retained 252 passes
  but had 31 setup errors because the sandbox denied its isolated `C:\tmp`
  basetemp; the approved rerun passed all 283 tests. Audits found no
  mathematical error. Wording now states the finite diagnostic scope,
  identifies the always-triple universal row, names the signed ceiling column
  unambiguously, and checks the full dual factor multiset exactly.
- **Interpretation:** The retained failures were environmental or formatting,
  not mathematical, production, schema, or artifact regressions.
- **Evidence:** `EVIDENCE.md#ev-003---static-checks-and-repository-regressions`;
  `EVIDENCE.md#ev-004---synchronization-scope-and-final-diff`.
- **Next step:** finalize durable status and inspect the complete diff.

## 2026-07-18 - Final handoff

- **Action:** Synchronized `READY_FOR_REVIEW` across current status and the
  dossier; inspected every tracked diff and all four new dossier files; ran
  exact nine-path scope, UTF-8/BOM, final-newline, trailing-whitespace,
  display, fence, generated-cache, `git status`, and `git diff --check`
  hygiene.
- **Result:** Exactly five pertinent authoritative project files and four new
  dossier files are changed. All final hygiene checks pass; no production,
  test, schema, artifact, certificate, alternative-scaffold, or geometric
  file is in the diff.
- **Interpretation:** The STRICT task is complete and awaits user review and
  a manual commit decision. No Git staging or commit action was taken.
- **Evidence:** `EVIDENCE.md#ev-004---synchronization-scope-and-final-diff`.
- **Next step:** user review and manual commit decision.

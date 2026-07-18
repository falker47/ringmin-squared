# TASK STATUS - All-Fixed-k Corollary

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** correct the project by combining CR28cr--CR28dd with
  CR28dr--CR28dw at every fixed finite \(k\), proving the all-fixed-\(k\)
  liminf coefficient and synchronizing every authoritative source.
- **Expected output:** exact strict admissibility proof, fixed-\(k\) charging
  passage, supremum argument with explicit quantifier audit, geometric
  corollary, corrected status of \(C_{5,*}\), one small exact diagnostic, and
  complete verification.

## Scope

- **In scope:** proof and documentation, authoritative-memory correction,
  roadmap, relevant dossier errata, and one dossier-local exact diagnostic.
- **Out of scope:** production source, test modules, artifacts, schemas,
  backends, certificates, enumeration code, and enumeration limits.
- No \(k=k(n)\), threshold uniform in \(k\), limit interchange, or finite
  rounded theorem at the unattained supremum is claimed.

## Verified Facts

- Startup used a clean `main` worktree at
  `6c5eb5b49e40f763a88580656f04a4143b2b4852`, tracking `origin/main`.
- For
  \(\alpha_\infty=(13-2\sqrt2)/23\), every unique normalized optimizer
  \(x^{(k)}\) gives strictly ordered, strictly all-middle cutoffs and weights
  through the formulas required by the task.
- For every fixed finite \(k\), a tuple-dependent threshold \(N_k\) permits
  CR28dw and gives
  \[
  \liminf_{n\to\infty}{\Lambda_n\over n^3}
  \ge p(\alpha_\infty)
  +{(3\alpha_\infty-1)^3M_k\over8}.
  \]
- Taking the supremum of these scalar inequalities gives
  \[
  \liminf_{n\to\infty}{\Lambda_n\over n^3}
  \ge{434+4\sqrt2\over1587},
  \qquad
  \liminf_{n\to\infty}{R_2^*(n)\over n^3}
  \ge{434+4\sqrt2\over1587\pi}.
  \]
- The exact separator
  \[
  C_{5,*}<{277\over1000}<{434+4\sqrt2\over1587}
  \]
  leaves \(C_{5,*}\) as the exact optimum of the fixed \(k=5\) template only.

## Assumptions / Inferences

- None beyond the exact prior theorems cited above.
- The sequence \(M_k\to1/3\) evaluates a supremum of coefficient numbers
  after the fixed-\(k\) liminf inequalities; it is not an interchange with
  \(n\to\infty\).

## Decisions And Rationale

- Use the notation \(C_{\mathrm{AF}}=(434+4\sqrt2)/1587\) for the
  all-fixed-\(k\) coefficient.
- Preserve all fixed-five optimization and finite-rounding results, but label
  their exact template scope.
- Add correction notes to the two historical input dossiers without rewriting
  their append-only chronology.
- Use one small standalone \(\mathbb Q(\sqrt2)\) diagnostic for exact algebra
  and bounded \(k\le8\) corroboration.

## Plan And Expected Delta

- [x] Complete STRICT startup and inspect the two input theorems and prior
  dossiers.
- [x] Prove strict order, all-middle admissibility, and fixed-\(k\) passage.
- [x] Prove the supremum coefficient, geometric transfer, and strict
  comparison with \(C_{5,*}\).
- [x] Synchronize the primary proof, all-\(n\) note, project brief, durable
  knowledge, roadmap, and current status draft.
- [x] Add the sole exact diagnostic.
- [x] Complete regressions, source audits, final diff inspection, and
  READY_FOR_REVIEW handoff.

## Verification

- **Checks completed:** the new exact diagnostic passes for \(k=1,\ldots,8\);
  Ruff check and final format check pass; normalized-simplex,
  arbitrary-charging, and global-five historical diagnostics pass; focused
  pytest passes 101 tests and full pytest passes 283; artifact verification
  passes four certificates and 76 local brackets; schema pytest passes four;
  source structure, stale-claim synchronization, three independent audits,
  protected-scope inspection, complete diff inspection, and `git diff
  --check` pass.
- **Corrected check failures:** the diagnostic initially needed Ruff's
  mechanical formatting. Three preliminary PowerShell source-audit commands
  had audit-command defects (variable parsing, a trailing-space regex that
  treated `t` literally, and missing spaces in compact `foreach` syntax);
  corrected commands pass and found no source defect.
- **Limitations:** bounded exact computation corroborates but does not replace
  the all-real proof for every fixed finite \(k\); hosted CI has not run this
  uncommitted diff.

## Blockers / Risks

- No blocker.
- Residual risk is limited to manual review of a large documentation diff and
  hosted CI not yet running the uncommitted changes.

## Next Atomic Action

- User manual review and commit decision; do not begin the proposed next task
  in this chat.

## Handoff

- **Last verified result:** exact derivation, proportional regressions,
  structural/source/scope checks, three independent audits, and final Git
  checks pass.
- **Files changed:** authoritative research/status Markdown, relevant dossier
  corrections, and this dossier-local diagnostic only.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`, then this
  dossier.

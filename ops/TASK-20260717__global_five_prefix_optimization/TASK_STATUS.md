# TASK STATUS - Global Five-Prefix Optimization

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** globally optimize the continuous five-prefix coefficient
  supplied by CR28cr--CR28dd and CR28dr--CR28dw.
- **Expected output:** exact compact reduction, complete clipping/transition/
  collision/face audit, the unique optimizer and coefficient, exact strict
  comparisons with the rational five-prefix witness and \(C_{4,*}\), one
  standalone exact diagnostic, and synchronized authoritative memory.

## Scope

- **In scope:** the fixed \(k=5\) continuous coefficient; its compact ordered
  density/weight closure; all 21 clipping regimes; every winning transition;
  density and weight faces; exact quadratic-surd algebra; one dossier-local
  standard-library diagnostic; research and status synchronization.
- **Out of scope:** finite rounding at the irrational optimizer, growing-
  \(k\) claims, production code, artifacts, schemas, backends, test modules,
  certificates, enumerators, and enumeration limits.

## Verified Facts

- Startup used a clean `main` worktree at
  `9fc4b2caeb385a7cd34c62fc494fd91182935f06`.
- CR28dw already proves the required one-use charging theorem for every fixed
  finite admissible \(k\); this task changes only the continuous \(k=5\)
  optimization and its consequences.
- The compact density/weight problem clips coordinatewise and has exactly 21
  ordered regimes \(H^hM^m0^z\), \(h+m+z=5\).
- The candidate envelope maximizer lies strictly in `MMMMM` and is distinct
  from the fixed rational witness at \(\alpha=13/30\).

## Assumptions / Inferences

- The eventual integer admissibility of a strict fixed continuous optimizer
  is used only for the usual fixed-parameter asymptotic passage. No uniform
  threshold or finite rounded theorem is inferred.
- The existing finite theorem from \(n=234\) remains specific to the rational
  witness and its fixed rational weights.

## Decisions And Rationale

- Use the exact clipped compact objective before invoking the normalized
  simplex envelope, so weight ordering and every clipping face are audited.
- Classify the fixed-density envelope through the same Bellman predecessor
  maps used for four prefixes, with the new \(m=4\) mixed-base margin checked
  explicitly.
- Use rational separators and positive integer square margins for the strict
  coefficient comparisons.

## Plan And Expected Delta

- [x] Complete STRICT startup and reconstruct the cited exact inputs.
- [x] Prove the compact reduction and complete regime/face audit.
- [x] Derive the exact optimizer, coefficient, and comparison chain.
- [x] Add and run the sole standalone diagnostic.
- [x] Synchronize authoritative research/project/status files.
- [x] Run proportional verification, independent audits, and final diff
  inspection; set `READY_FOR_REVIEW` if all pass.

## Verification

- **Checks:** exact diagnostic; Ruff check and format check; focused and full
  pytest regressions; schema and artifact verifiers; historical normalized-
  simplex, global-four-prefix, rational-five-prefix, and finite-five-prefix
  diagnostics; source-tag, delimiter, environment, encoding, synchronization,
  scope, and Git-diff audits; three independent mathematical/source reviews.
- **Observed result:** all checks pass. The full suite reports 283 passing
  tests, the focused fixed-order suite reports 101 passing tests, all four
  historical diagnostics pass, and `git diff --check` is clean.
- **Limitations:** hosted CI is outside the local verification scope.

## Blockers / Risks

- No blocker. The formal all-middle envelope is used for equality only on its
  audited branch. No finite theorem is claimed at the irrational optimizer.

## Subsequent Scope Clarification - 2026-07-18

The optimizer and coefficient in this dossier remain exact, unique, and
unchanged for the fixed \(k=5\) template. A later all-fixed-\(k\) corollary
proves
\[
C_{5,*}<{277\over1000}<{434+4\sqrt2\over1587},
\]
so \(C_{5,*}\) is no longer the current cross-\(k\) lower coefficient. See
`ops/TASK-20260718__all_fixed_k_corollary/`.

## Next Atomic Action

- User manual review and commit decision.

## Handoff

- **Last verified result:** exact global five-prefix theorem, diagnostic,
  authoritative synchronization, and all local verification pass.
- **Files changed:** the six authoritative research/status files listed in
  `CURRENT_STATUS.md` and this four-file task dossier only.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md`, then this
  dossier.

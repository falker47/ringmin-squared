# TASK_STATUS - TASK-20260719 / Monotone Threshold-Closing PG46 Exact K

Last update: 2026-07-19

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** evaluate the one PG46 interval shift
  `alpha_{q,2m-1}` on `n=10m+3`, `m>=3`, determine exact `K`, every
  maximizing subset, all five residue formulas, and exact comparisons with
  PG49-star, K825, closing PG46, and preclosing PG46.
- **Expected output:** a complete symbolic deletion-gain, compressed-shortcut,
  and cyclic-closure proof; one bounded independent standard-library
  diagnostic; synchronized durable research memory.

## Scope

- **In scope:** the one fixed monotone interval shift, its exact induced-
  subset score, the singleton-inversion decomposition, all equality and
  minimum-row cases, and the four named fixed-order comparators.
- **Out of scope:** any other Ferrers matching, subset/path-permutation/
  matching search, exact angular thresholds, geometric claims, global
  `K`-minimality, or minimizing-order classification.

## Verified Facts

- The startup worktree was clean at
  `e4dae3ee5c44587c4a93fd04ca68c486a1505b70`.
- The shift is exactly (PG46) with closing target
  `q=kappa_{2m-1}=floor((4m+3)/5)`; all residual paths remain increasing.
- The retained shortcut-budget lemma is (K825-6)--(K825-9), and the paired
  PG49-star theorem is (KPGSTAR-1)--(KPGSTAR-28).
- Symbolic deletion gains and compressed shortcuts prove that
  `B_m={4m+1,...,10m+3}` is the sole maximizing subset. The exact minima are
  `28m+12` for holes and `12m+4` for nontrivial shortcuts.
- The exact score, five residue branches, all comparator signs, and the
  singleton-inversion contribution `m(m-1)(m-2)/3` are proved for every
  `m>=3`.

## Assumptions / Inferences

- Previously proved scaffold, Ferrers, and shortcut lemmas are exact inputs.
  No geometric or Ringmin statement is generalized.
- The symbolic theorem, not bounded computation, must establish all-`m`
  uniqueness and every comparison.

## Decisions And Rationale

- Use the same isolated-hole compression framework as the retained PG46 and
  PG49-star proofs so that every equality case and both cyclic-closing roles
  remain explicit.
- Keep exactly one dossier-local diagnostic. It constructs only the fixed
  shift, uses a max-plus increasing-position DAG and an all-oriented-arc
  audit, and imports no project helper.

## Completed Delta

- Added Section 16, (KPG46Q-1)--(KPG46Q-29), to the fixed-order research
  note.
- Added the sole standalone bounded diagnostic and this task dossier.
- Synchronized only the pertinent research summary, project brief, stable
  knowledge, next-task list, and current status; production, tests, schemas,
  and checked artifacts are unchanged.

## Verification

- **Checks:** standalone diagnostic; scoped Ruff/compile; full pytest suite;
  focused schema suite; checked-artifact verifier; equation-tag, delimiter,
  UTF-8/BOM, control-character, one-diagnostic, source-sync, mathematical,
  and diff audits.
- **Observed result:** diagnostic PASS on 28 max-plus/shortcut rows and 998
  formula rows; 283 tests pass with a workspace-local `--basetemp`; 4 focused
  schema tests pass; 4 certificates and 76 local brackets verify; scoped
  lint/format/compile, source audits, complete diff inspection, and whitespace
  hygiene pass.
- **Limitations:** bounded computation is corroborative only. The first two
  full-suite attempts recorded 252 passes and 31 `tmp_path` setup errors
  because both the default Windows temp directory and `C:\tmp` were denied;
  the identical suite passed once `--basetemp` used the writable workspace.
  Whole-repository Ruff also reports four pre-existing lint errors and 39
  pre-existing formatting candidates outside the changed Python file; the
  sole new Python file passes both scoped checks.

## Blockers / Risks

- No task blocker. The inherited whole-repository Ruff baseline is recorded
  and was not modified because every reported file is outside this task.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact theorem, sole diagnostic, full tests,
  checked artifacts, scoped lint, independent audits, complete diff review,
  and final whitespace/status hygiene pass.
- **Files changed:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `research/NEXT_RESEARCH_STEPS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, and this dossier.
- **Files to read first:** the new Section 16, this status, and `EVIDENCE.md`.

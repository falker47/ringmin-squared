# EVIDENCE - TASK-20260719 / Explicit PG49-Star Exact K

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git | Startup and source reconstruction | repository root and retained research notes | VERIFIED |
| EV-002 | exact theorem | Ferrers, `K`, argmax, formulas, coefficient, comparisons | pertinent research notes | PROVED |
| EV-003 | bounded exact computation | Direct max-plus and all-oriented-shortcut diagnostic | `exact_diagnostic.py` | VERIFIED |
| EV-004 | regression / hygiene | Full tests, artifact checks, source and diff audit | repository root | VERIFIED |

## EV-001 - Startup And Source Reconstruction

- **Date:** 2026-07-19
- **Method or command:** read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, relevant task dossiers,
  (PG1)--(PG49), (CR12j)--(CR12k), (K825-1)--(K825-9), and both PG46
  evaluations; ran read-only Git status and revision checks.
- **Relevant output:** clean worktree at
  `fded0cc29029b5d2e725f1609f71ea17b4468e38`; no unrelated modifications.
- **Interpretation:** the task could proceed without mixing work, and all
  reused facts have exact repository provenance.
- **Limitations:** source reconstruction does not itself prove the new order.
- **Linked log entry:** `TASK_LOG.md#2026-07-19---startup-and-exact-derivation`.

## EV-002 - Exact Symbolic Theorem

- **Date:** 2026-07-19
- **Method or command:** direct integer/Ferrers proof; exhaustive symbolic
  deletion-gain classification; strict compressed-shortcut lemma by endpoint
  and edge-count classes; direct block summation; exact polynomial sign
  comparisons.
- **Relevant output:** the proposed map is compatible for every `m>=3`;
  `B_m={4m+1,...,10m+3}` is the unique maximizer; its score is
  `(1714m^3+1863m^2+24mq+617m+12q^2+48q+66)/6`, with
  `q=floor((4m+3)/5)`; the five residue formulas have coefficient
  `857/3000` in `n`; every requested comparator is strictly larger.
- **Interpretation:** all three supplied conjectures are exact fixed-order
  combinatorial theorems. No first counterexample exists.
- **Limitations:** no exact angular, geometric, or global minimizing-order
  conclusion is inferred.
- **Linked log entry:** `TASK_LOG.md#2026-07-19---startup-and-exact-derivation`.

## EV-003 - Direct Max-Plus And Shortcut Diagnostic

- **Date:** 2026-07-19
- **Method or command:**
  `python ops/TASK-20260719__explicit_pg49_star_exact_k/exact_diagnostic.py`.
  The script constructs only the prescribed order, fixes the least selected
  backbone position, solves the resulting increasing DAG by direct max-plus,
  closes the cycle, counts ties, and scans every proper oriented arc.
- **Relevant output:** PASS; 28 max-plus/shortcut rows (`m=3,...,30`),
  36,989,498 max-plus transitions, 958,916 proper oriented-arc checks, and
  998 formula/Ferrers rows (`m=3,...,1000`). Every max-plus row has unique
  argmax `B_m`; cyclic closure and all three comparator inequalities pass.
- **Interpretation:** a structurally independent scorer corroborates every
  requested conclusion on its declared finite range without enumerating
  subsets, matchings, path permutations, or general orders.
- **Limitations:** bounded exact computation corroborates, but does not
  replace, EV-002. The all-`m` result rests on the symbolic proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---diagnostic-and-source-synchronization`.

## EV-004 - Regression And Diff Hygiene

- **Date:** 2026-07-19
- **Method or command:** `python -m pytest -p no:cacheprovider`;
  `python -m pytest -p no:cacheprovider tests/test_checked_artifact_schema_validation.py`;
  `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`;
  Ruff lint/format, Python compile, scoped equation-tag/delimiter and control
  character audits, three independent proof/diagnostic/source reviews,
  `git status --short`, complete diff inspection, and `git diff --check`.
- **Relevant output:** 283 tests passed; 4 focused tests passed; verifier
  confirms `certificates=4`, `local_brackets=76`, summary `n=3,4,5,6`;
  lint, format, compile, scoped source audits, all independent audits, and
  whitespace checks pass.
- **Interpretation:** the new theorem, diagnostic, and pertinent source
  synchronization introduce no observed regression and are internally
  consistent. No production, test, schema, or checked-artifact file changed.
- **Limitations:** a generic whole-file display-delimiter count reports the
  same inherited two surplus openers in
  `research/PRODUCT_DISTANCE_SURROGATE.md` in `HEAD` and the working copy;
  the newly added PG110--PG114 section is balanced. Regression tests do not
  independently prove the mathematical theorem.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---final-verification-and-handoff`.

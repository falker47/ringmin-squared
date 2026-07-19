# EVIDENCE - TASK-20260719 / Monotone Threshold-Closing PG46 Exact K

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git | Startup and source reconstruction | repository root and retained research notes | VERIFIED |
| EV-002 | exact theorem | Maximizers, score, residues, shortcuts, closure, comparisons | `research/FIXED_ORDER_CYCLE_RATIO.md` | PROVED |
| EV-003 | bounded exact computation | Direct max-plus and all-oriented-arc diagnostic | `exact_diagnostic.py` | VERIFIED |
| EV-004 | regression / hygiene | Full tests, artifact checks, source and diff audit | repository root | VERIFIED |

## EV-001 - Startup And Source Reconstruction

- **Date:** 2026-07-19
- **Method or command:** read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, relevant task dossiers,
  (PG1)--(PG49), (CR12j)--(CR12k), (K825-6)--(K825-9), both prior PG46
  evaluations, and (PG110)--(PG114)/(KPGSTAR-1)--(KPGSTAR-28); ran
  read-only Git status and revision checks.
- **Relevant output:** clean `main` worktree at
  `e4dae3ee5c44587c4a93fd04ca68c486a1505b70`; no unrelated modifications.
- **Interpretation:** the task could proceed without mixing work, and every
  reused claim has exact repository provenance.
- **Limitations:** reconstruction alone does not prove the new fixed-order
  theorem.
- **Linked log entry:** `TASK_LOG.md#2026-07-19---startup-and-exact-derivation`.

## EV-002 - Exact Symbolic Theorem

- **Date:** 2026-07-19
- **Method or command:** exact expansion of the prescribed interval shift;
  exhaustive seven-class deletion-gain calculation; compressed shortcuts by
  endpoint type and edge count; literal cyclic-closure audit; block summation;
  exact polynomial/floor comparison.
- **Relevant output:** Section 16 proves that
  `B_m={4m+1,...,10m+3}` is the sole maximizing subset, with score
  `(572m^3+619m^2+8mq+207m+4q^2+16q+22)/2`; the exact gain over PG49-star
  is `m(m-1)(m-2)/3`; all five residue formulas and comparator signs are
  explicit.
- **Interpretation:** the singleton reversal supplies the entire cubic
  `n^3/3000+O(n^2)` PG49-star advantage, while the monotone shift's gains
  against the coefficient-`143/500` comparators are only quadratic.
- **Limitations:** this is one combinatorial fixed-order theorem. It gives no
  angular, geometric, or global minimizing-order result.
- **Linked log entry:** `TASK_LOG.md#2026-07-19---startup-and-exact-derivation`.

## EV-003 - Direct Max-Plus And Shortcut Diagnostic

- **Date:** 2026-07-19
- **Method or command:**
  `python ops/TASK-20260719__pg46_threshold_closing_exact_k/exact_diagnostic.py`.
  The script constructs only the fixed shift, solves the increasing-position
  DAG by max-plus with tie counting, and scans every proper oriented arc.
- **Relevant output:** PASS; 28 max-plus/shortcut rows (`m=3,...,30`),
  36,989,498 max-plus transitions, 958,916 proper oriented-arc checks, and
  998 Ferrers/formula/residue/inversion/comparator rows (`m=3,...,1000`).
  Every max-plus row has unique argmax `B_m`; the minimum hole and shortcut
  margins are exactly `28m+12` and `12m+4`.
- **Interpretation:** an independent standard-library scorer corroborates
  every requested fixed-order conclusion on its declared finite range. It
  enumerates no subset, path permutation, matching, or cyclic-order family.
- **Limitations:** bounded exact computation corroborates, but does not
  replace, EV-002.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---diagnostic-and-source-synchronization`.

## EV-004 - Regression And Diff Hygiene

- **Date:** 2026-07-19
- **Method or command:** `python -m pytest -p no:cacheprovider`; two retries
  with explicit temp roots; successful
  `python -m pytest -p no:cacheprovider --basetemp <workspace-local-path>`;
  focused schema pytest with its own workspace-local `--basetemp`;
  `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`;
  scoped and whole-tree Ruff checks; Python compile; PowerShell audits for
  primary tags, delimiters, controls, UTF-8 BOMs, and diagnostic count;
  independent proof/diagnostic/source reviews; generated-file cleanup;
  `git status`, `git diff`, and `git diff --check`.
- **Relevant output:** the first run and the `C:\tmp` retry each produced
  252 passes plus 31 identical `tmp_path` setup errors (`WinError 5`); the
  same suite then passed all 283 tests under a writable workspace-local
  `--basetemp`. The focused suite passes 4 tests. The artifact verifier
  confirms `certificates=4`, `local_brackets=76`, `n=3,4,5,6`. The sole new
  Python file passes Ruff lint/format and compile. Whole-tree Ruff reports
  four lint findings and 39 formatting candidates, all in pre-existing,
  unchanged files. The source audit finds 29 sequential unique KPG46Q tags,
  balanced scoped displays/environments, no duplicate primary tag, no bad
  control/BOM, and exactly one dossier diagnostic. Generated files are
  removed; complete diff inspection, final status, scoped Ruff/tag/display
  reruns, and `git diff --check` pass.
- **Interpretation:** all task-proportional checks pass, and no observed
  regression is attributable to the new theorem or diagnostic. Environment-
  only failures and inherited whole-tree lint debt are explicitly retained.
- **Limitations:** tests and bounded diagnostics do not independently prove
  EV-002; unrelated Ruff debt remains outside this task.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---regression-and-pre-handoff-audit`.

# EVIDENCE - TASK-20260712__promote_n5_interval_certificate_example / Promote n=5 Interval Certificate Example

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source | Startup and prior artifact review | startup files, prior n=5 task dossier, initial Git status | PASS |
| EV-002 | command/artifact | Clean-provenance n=5 example export | `examples/small_n_interval_certificate_n5.json` | PASS |
| EV-003 | test | Focused and full tests | `tests/test_small_n_interval_certificate.py`; full suite | PASS |
| EV-004 | command | Final status and diff hygiene | `git status --short`; `git diff`; `git diff --check`; trailing-whitespace scan | PASS |

## EV-001 - Startup And Prior Artifact Review

- **Date:** 2026-07-12
- **Method or command:** Read `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and `ops/TASK-20260712__bounded_n5_interval_certificate_attempt/`.
- **Method or command:** `git status --short`.
- **Relevant output:** Initial `git status --short` produced no entries.
- **Interpretation:** The repository was clean, so a regenerated example artifact could honestly record clean-tree provenance before any new task files were written.
- **Limitations:** Startup inspection does not by itself validate the artifact.

## EV-002 - Clean-Provenance n=5 Example Export

- **Date:** 2026-07-12
- **Method or command:** `python -c "import sys; sys.path.insert(0, 'src'); from power_ringmin.small_n_interval_certificate import main_small_n; raise SystemExit(main_small_n(['--n','5','--max-canonical-orders','12','--output','examples/small_n_interval_certificate_n5.json','--digits','80','--guard-decimal','1e-70','--radius-eta','1e-4','--local-max-attempts','8','--created-at-utc','2026-07-12T00:00:00Z']))"`.
- **Relevant output:** `wrote examples\small_n_interval_certificate_n5.json n=5 bracket=(3.934227717145796443531935437931679189205169677734375, 3.9344277171457964215051106293685734272003173828125] classification=computer_certified_result covered=12`.
- **Method or command:** Inspected the artifact provenance and aggregate result with PowerShell `ConvertFrom-Json`.
- **Relevant output:** `git_commit` was `1b013793eafe03661d12e0c1ae5aec3e9173d151`; `git_dirty` was `False`; `covered_canonical_count` was `12`; both global bound source orders were `[5, 1, 3, 4, 2]`.
- **Interpretation:** The promoted example has clean-tree provenance and matches the finite bracket found by the prior task-scoped attempt.
- **Limitations:** This is finite `n=5` evidence only and depends on the documented guarded `mpmath.iv` interval backend contract.

## EV-003 - Focused And Full Tests

- **Date:** 2026-07-12
- **Method or command:** `python -m pytest tests\test_small_n_interval_certificate.py`.
- **Relevant output:** `18 passed in 1.83s`.
- **Method or command:** `python -m pytest`.
- **Relevant output:** `67 passed in 10.27s`.
- **Interpretation:** The checked `n=5` example loads and validates through the existing small-n interval certificate verifier path, and the full suite passes after promotion.
- **Limitations:** Passing tests do not prove any all-`n` theorem or remove the interval-backend provenance limitation.

## EV-004 - Final Status And Diff Hygiene

- **Date:** 2026-07-12
- **Method or command:** `git status --short`.
- **Relevant output:** Modified tracked files: `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, `tests/test_small_n_interval_certificate.py`. New untracked paths: `examples/small_n_interval_certificate_n5.json` and `ops/TASK-20260712__promote_n5_interval_certificate_example/`.
- **Method or command:** `git diff`.
- **Relevant output:** Inspected tracked documentation and test changes. New artifact and task dossier were inspected through the commands recorded above.
- **Method or command:** `git diff --check`.
- **Relevant output:** No output.
- **Method or command:** `rg -n "[ \t]+$" CURRENT_STATUS.md PROJECT_KNOWLEDGE.md tests\test_small_n_interval_certificate.py examples\small_n_interval_certificate_n5.json ops\TASK-20260712__promote_n5_interval_certificate_example`.
- **Relevant output:** No matches.
- **Interpretation:** Final diff and whitespace hygiene checks passed.
- **Limitations:** `git diff --check` does not inspect untracked files until staged, so the separate trailing-whitespace scan included the new artifact and task dossier.

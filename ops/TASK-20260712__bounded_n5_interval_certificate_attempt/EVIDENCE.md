# EVIDENCE - TASK-20260712__bounded_n5_interval_certificate_attempt / Bounded n=5 Interval Certificate Attempt

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | review/test | Startup, hardening review, and focused tests | `HEAD` hardening commit; focused interval tests | PASS |
| EV-002 | command | Initial source-layout dry-run attempt | `python -c ... main_small_n(...)` | FAILED ENVIRONMENT SETUP |
| EV-003 | command | Bounded n=5 preflight | `main_small_n --n 5 --max-canonical-orders 12 --dry-run` | PASS |
| EV-004 | command/artifact | Bounded n=5 certificate export | `small_n_interval_certificate_n5_attempt.json` | PASS |
| EV-005 | validation/test | Artifact validation and final full tests | package artifact loader; `python -m pytest` | PASS |
| EV-006 | command | Final status and diff hygiene | `git status --short`; `git diff`; `git diff --check`; trailing whitespace scan | PASS |

## EV-001 - Startup Hardening Review And Focused Tests

- **Date:** 2026-07-12
- **Method or command:** Read startup files, inspected `git status`, `git log --oneline -5`, `git show --stat --oneline --decorate --no-renames HEAD`, hardening task memory, and selected hardening source/test hunks.
- **Relevant output:** Working tree was clean. `HEAD` was `b462d523d65d56313a5eda2cd31d79ab7a6f9e1f` (`Harden small-n interval certificate production path`).
- **Method or command:** `python -m pytest tests\test_interval_verifier.py tests\test_small_n_interval_certificate.py`.
- **Relevant output:** `24 passed in 2.49s`.
- **Review notes:** No blocking issue was found in the checked-in hardening path before the bounded `n=5` attempt. The generic small-n CLI requires an explicit `--max-canonical-orders` ceiling and has test coverage for the `n=5`, `12`-order dry run.
- **Interpretation:** The bounded `n=5` attempt can proceed under the current hardening code.
- **Limitations:** This review was scoped to the hardening path needed for this run; it was not a full formal audit of the interval arithmetic backend.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---startup-and-hardening-review`

## EV-002 - Initial Source-Layout Dry-Run Attempt

- **Date:** 2026-07-12
- **Method or command:** `python -c "from power_ringmin.small_n_interval_certificate import main_small_n; raise SystemExit(main_small_n(['--n','5','--max-canonical-orders','12','--dry-run']))"`.
- **Relevant output:** Failed with `ModuleNotFoundError: No module named 'power_ringmin'`.
- **Interpretation:** This was an environment/source-layout issue because the checkout uses `src/` layout and was not importable through plain `python -c`.
- **Limitations:** This is not evidence about the certificate logic or the mathematical result. Subsequent commands should set `PYTHONPATH=src` or use an installed console script.

## EV-003 - Bounded n=5 Preflight

- **Date:** 2026-07-12
- **Method or command:** `python -c "import sys; sys.path.insert(0, 'src'); from power_ringmin.small_n_interval_certificate import main_small_n; raise SystemExit(main_small_n(['--n','5','--max-canonical-orders','12','--dry-run']))"`.
- **Relevant output:** `preflight n=5 canonical_orders=12 max_canonical_orders=12 generation_allowed=true`.
- **Interpretation:** The regenerated canonical order count exactly matched the requested explicit ceiling, so bounded generation was allowed.
- **Limitations:** Preflight checks only order-space cardinality and the explicit ceiling; it does not generate or verify local brackets.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---bounded-n5-preflight-and-export`

## EV-004 - Bounded n=5 Certificate Export

- **Date:** 2026-07-12
- **Method or command:** `python -c "import sys; sys.path.insert(0, 'src'); from power_ringmin.small_n_interval_certificate import main_small_n; raise SystemExit(main_small_n(['--n','5','--max-canonical-orders','12','--output','ops/TASK-20260712__bounded_n5_interval_certificate_attempt/small_n_interval_certificate_n5_attempt.json']))"`.
- **Relevant output:** `wrote ops\TASK-20260712__bounded_n5_interval_certificate_attempt\small_n_interval_certificate_n5_attempt.json n=5 bracket=(3.934227717145796443531935437931679189205169677734375, 3.9344277171457964215051106293685734272003173828125] classification=computer_certified_result covered=12`.
- **Artifact:** `ops/TASK-20260712__bounded_n5_interval_certificate_attempt/small_n_interval_certificate_n5_attempt.json`.
- **Interpretation:** The bounded export generated and wrote a finite `n=5` interval certificate artifact covering all 12 canonical cyclic orders.
- **Limitations:** This result is finite n=5 evidence only and depends on the repository's documented guarded `mpmath.iv` interval backend contract.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---bounded-n5-preflight-and-export`

## EV-005 - Artifact Validation And Final Tests

- **Date:** 2026-07-12
- **Method or command:** Loaded `small_n_interval_certificate_n5_attempt.json` with `load_small_n_interval_certificate_artifact`.
- **Relevant output:** `n 5`; `covered 12`; `expected_count 12`; lower endpoint `3.934227717145796443531935437931679189205169677734375`; upper endpoint `3.9344277171457964215051106293685734272003173828125`; lower and upper source order `[5, 1, 3, 4, 2]`; source commit `b462d523d65d56313a5eda2cd31d79ab7a6f9e1f`; `git_dirty True`; `created_at_utc 2026-07-12T01:05:30Z`.
- **Method or command:** `python -m pytest`.
- **Relevant output:** `66 passed in 11.90s`.
- **Interpretation:** Package semantic validation accepts the generated artifact, and the full repository test suite still passes after the task-scoped artifact generation.
- **Limitations:** The artifact provenance records `git_dirty=true` because the task dossier had already been created before generation. Startup evidence records the source tree was clean before this task's generated files.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---validation-and-handoff`

## EV-006 - Final Status And Diff Hygiene

- **Date:** 2026-07-12
- **Method or command:** `git status --short`.
- **Relevant output:** Modified tracked files: `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`. New untracked path: `ops/TASK-20260712__bounded_n5_interval_certificate_attempt/`.
- **Method or command:** `git diff --stat`.
- **Relevant output:** Tracked diff showed `CURRENT_STATUS.md` and `PROJECT_KNOWLEDGE.md` changed with 12 insertions and 7 deletions.
- **Method or command:** `git diff -- PROJECT_KNOWLEDGE.md CURRENT_STATUS.md`.
- **Relevant output:** Inspected tracked status/knowledge updates documenting the `n=5` attempt and next action.
- **Method or command:** `git diff --check`.
- **Relevant output:** No output.
- **Method or command:** `rg -n "[ \t]+$" PROJECT_KNOWLEDGE.md CURRENT_STATUS.md ops\TASK-20260712__bounded_n5_interval_certificate_attempt`.
- **Relevant output:** No matches.
- **Interpretation:** Final tracked diff and task dossier hygiene checks passed. The remaining working-tree changes are the intended task evidence and status updates.
- **Limitations:** `git diff --check` does not inspect untracked files, so the separate trailing-whitespace scan covered the new task dossier.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---validation-and-handoff`

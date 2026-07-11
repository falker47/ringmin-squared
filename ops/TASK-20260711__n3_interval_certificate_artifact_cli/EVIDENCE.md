# EVIDENCE - TASK-20260711__n3_interval_certificate_artifact_cli / N=3 Interval Certificate Artifact CLI

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source | Startup and source inspection | `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, prior task files, source files | PASS |
| EV-002 | file | N=3 certificate artifact CLI implementation | `src/power_ringmin/small_n_interval_certificate.py`, `pyproject.toml`, `src/power_ringmin/__init__.py`, `tests/test_small_n_interval_certificate.py` | PASS |
| EV-003 | command | Checked n=3 artifact generation | `examples/small_n_interval_certificate_n3.json` | PASS |
| EV-004 | test | Focused and full test verification | `python -m pytest tests\test_small_n_interval_certificate.py`; `python -m pytest` | PASS |
| EV-005 | command | Final status and diff checks | `git status --short`; `git diff --stat`; `git diff`; `git diff --check`; trailing-whitespace scan | PASS |

## EV-001 - Startup And Source Inspection

- **Date:** 2026-07-11
- **Method or command:** Read project startup files, previous n=3 fixture task files, relevant source/test files, and inspected the initial working tree with `git status --short`.
- **Relevant output:** Initial `git status --short` produced no entries. `CURRENT_STATUS.md` proposed promoting the n=3 interval certificate fixture into a checked reproducible artifact or CLI command.
- **Interpretation:** The repository was ready for this bounded finite certificate promotion task.
- **Limitations:** Inspection establishes context only.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---startup-and-implementation`

## EV-002 - Implementation

- **Date:** 2026-07-11
- **Method or command:** File edits using `apply_patch`.
- **Relevant output:** Added `export_n3_interval_certificate_artifact`, `build_parser`, and `main` to `src/power_ringmin/small_n_interval_certificate.py`; registered `power-ringmin-export-n3-interval-certificate`; exported the helper from `src/power_ringmin/__init__.py`; added focused tests.
- **Interpretation:** The n=3 fixture can now be reproduced through a checked command path and loaded through the existing semantic validator.
- **Limitations:** The command intentionally supports only the known complete n=3 fixture.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---startup-and-implementation`

## EV-003 - Checked Artifact Generation

- **Date:** 2026-07-11
- **Method or command:** `python -c "import sys; sys.path.insert(0, 'src'); from power_ringmin.small_n_interval_certificate import main; raise SystemExit(main(['--output', 'examples/small_n_interval_certificate_n3.json', '--digits', '80', '--guard-decimal', '1e-70', '--radius-eta', '1e-4', '--created-at-utc', '2026-07-11T00:00:00Z']))"`
- **Relevant output:** `wrote examples\small_n_interval_certificate_n3.json n=3 bracket=(0.3832870361393696523322205393924377858638763427734375, 0.383487036139369685816546962087159045040607452392578125] classification=computer_certified_result covered=1`
- **Interpretation:** The checked artifact records a finite n=3 global interval bracket with one verified local bracket covering the complete canonical n=3 order space.
- **Limitations:** The artifact is finite n=3 evidence only and carries the documented guarded `mpmath.iv` interval-backend provenance limitation.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---artifact-generation-and-tests`

## EV-004 - Focused And Full Test Verification

- **Date:** 2026-07-11
- **Method or command:** `python -m pytest tests\test_small_n_interval_certificate.py`.
- **Relevant output:** `7 passed in 0.76s`.
- **Method or command:** `python -m pytest`.
- **Relevant output:** `55 passed in 9.97s`.
- **Interpretation:** Focused tests validate the fixture, CLI export path, checked artifact loading, and console script registration; the full repository suite still passes.
- **Limitations:** Passing tests do not establish an all-n theorem or production-grade interval-backend provenance.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---artifact-generation-and-tests`

## EV-005 - Final Diff Checks

- **Date:** 2026-07-11
- **Method or command:** `git status --short`.
- **Relevant output:** Modified tracked files include `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, `pyproject.toml`, `src/power_ringmin/__init__.py`, `src/power_ringmin/small_n_interval_certificate.py`, and `tests/test_small_n_interval_certificate.py`; new untracked paths include `examples/small_n_interval_certificate_n3.json` and `ops/TASK-20260711__n3_interval_certificate_artifact_cli/`.
- **Method or command:** `git diff --stat`; `git diff`.
- **Relevant output:** Diff inspection showed tracked changes for the CLI, script registration, tests, and durable memory. The checked artifact and task dossier are untracked and were inspected separately.
- **Method or command:** `git diff --check`.
- **Relevant output:** No output.
- **Method or command:** `rg -n "[ \t]+$" PROJECT_KNOWLEDGE.md CURRENT_STATUS.md pyproject.toml src\power_ringmin\__init__.py src\power_ringmin\small_n_interval_certificate.py tests\test_small_n_interval_certificate.py examples\small_n_interval_certificate_n3.json ops\TASK-20260711__n3_interval_certificate_artifact_cli`.
- **Relevant output:** No matches.
- **Interpretation:** Final diff and whitespace checks passed.
- **Limitations:** `git diff --check` does not inspect untracked files until staged, so the separate trailing-whitespace scan included the checked artifact and new task dossier.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---final-diff-checks-and-handoff`

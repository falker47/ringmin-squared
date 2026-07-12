# EVIDENCE - TASK-20260712__bounded_n6_interval_certificate_export / Bounded n=6 Interval Certificate Export

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source | Startup, prior memory, and exporter review | startup files; prior `n=6` preflight; exporter source | PASS |
| EV-002 | command/artifact | Bounded n=6 certificate export | `small_n_interval_certificate_n6_attempt.json` | PASS |
| EV-003 | validation/test | Artifact validation and tests | package loader; focused/full pytest | PASS |
| EV-004 | command | Final status and diff hygiene | `git status --short`; `git diff`; `git diff --check`; trailing-whitespace scan | PASS |

## EV-001 - Startup Prior Memory And Exporter Review

- **Date:** 2026-07-12
- **Method or command:** Read `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `ops/TASK-20260712__bounded_n6_preflight/`, and relevant small-n certificate exporter source.
- **Method or command:** `git status --short`.
- **Relevant output:** Initial `git status --short` produced no entries.
- **Relevant output:** Prior preflight recorded `canonical_index_order_count(6) == 60` and bounded dry-run admission at `--max-canonical-orders 60`.
- **Interpretation:** The requested bounded export is the next atomic action described by the repository handoff.
- **Limitations:** Startup review does not by itself validate a generated artifact.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---startup-and-prior-preflight-review`

## EV-002 - Bounded n6 Certificate Export

- **Date:** 2026-07-12
- **Method or command:** `New-Item -ItemType Directory -Path ops\TASK-20260712__bounded_n6_interval_certificate_export -Force`.
- **Relevant output:** Created the empty task dossier directory.
- **Method or command:** `git status --short`.
- **Relevant output:** No entries after empty directory creation.
- **Method or command:** `python -c "import sys; sys.path.insert(0, 'src'); from power_ringmin.small_n_interval_certificate import main_small_n; raise SystemExit(main_small_n(['--n','6','--max-canonical-orders','60','--output','ops/TASK-20260712__bounded_n6_interval_certificate_export/small_n_interval_certificate_n6_attempt.json']))"`.
- **Relevant output:** `wrote ops\TASK-20260712__bounded_n6_interval_certificate_export\small_n_interval_certificate_n6_attempt.json n=6 bracket=(8.4678350760883720482752323732711374759674072265625, 8.4680350760883715821591977146454155445098876953125] classification=computer_certified_result covered=60`.
- **Artifact:** `ops/TASK-20260712__bounded_n6_interval_certificate_export/small_n_interval_certificate_n6_attempt.json`.
- **Interpretation:** The bounded export generated and wrote a finite `n=6` interval certificate artifact covering all 60 canonical cyclic index orders.
- **Limitations:** This result is finite n=6 evidence only and depends on the repository's documented guarded `mpmath.iv` interval backend contract.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---bounded-n6-export`

## EV-003 - Artifact Validation And Tests

- **Date:** 2026-07-12
- **Method or command:** Loaded `small_n_interval_certificate_n6_attempt.json` with `load_small_n_interval_certificate_artifact`.
- **Relevant output:** `n 6`; `covered 60`; `expected_count 60`; lower endpoint `8.4678350760883720482752323732711374759674072265625`; upper endpoint `8.4680350760883715821591977146454155445098876953125`; lower and upper source order `[6, 1, 2, 5, 4, 3]`; source commit `8dbdd8c90d07347a57f962260b00b6d5b2c55109`; `git_dirty False`; `created_at_utc 2026-07-12T01:30:29Z`.
- **Method or command:** `Get-Item ops\TASK-20260712__bounded_n6_interval_certificate_export\small_n_interval_certificate_n6_attempt.json`.
- **Relevant output:** File size was `378959` bytes.
- **Method or command:** `python -m pytest tests\test_small_n_interval_certificate.py`.
- **Relevant output:** `18 passed in 2.66s`.
- **Method or command:** `python -m pytest`.
- **Relevant output:** `67 passed in 12.91s`.
- **Interpretation:** Package semantic validation accepts the generated artifact, the focused small-n certificate tests pass, and the full repository test suite passes after artifact generation.
- **Limitations:** Passing tests do not prove any all-`n` theorem or remove the interval-backend provenance limitation.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---validation-and-tests`

## EV-004 - Final Status And Diff Hygiene

- **Date:** 2026-07-12
- **Method or command:** `git status --short`.
- **Relevant output:** Modified tracked files: `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`. New untracked path: `ops/TASK-20260712__bounded_n6_interval_certificate_export/`.
- **Method or command:** `git diff --stat`.
- **Relevant output:** Tracked diff showed `CURRENT_STATUS.md` and `PROJECT_KNOWLEDGE.md` changed.
- **Method or command:** `git diff -- PROJECT_KNOWLEDGE.md CURRENT_STATUS.md`.
- **Relevant output:** Inspected tracked status/knowledge updates documenting the `n=6` export and handoff.
- **Method or command:** `git diff --check`.
- **Relevant output:** No output.
- **Method or command:** `rg -n "[ \t]+$" PROJECT_KNOWLEDGE.md CURRENT_STATUS.md ops\TASK-20260712__bounded_n6_interval_certificate_export`.
- **Relevant output:** No matches.
- **Interpretation:** Final tracked diff and task dossier hygiene checks passed.
- **Limitations:** `git diff --check` does not inspect untracked files until staged, so the separate trailing-whitespace scan covered the new task dossier and artifact.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---final-handoff`

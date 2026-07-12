# EVIDENCE - TASK-20260712__promote_n6_interval_certificate_example / Promote n=6 Interval Certificate Example

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source | Startup and prior artifact review | startup files; prior `n=6` task dossier and artifact | PASS |
| EV-002 | command/artifact | Checked n=6 example regeneration | `examples/small_n_interval_certificate_n6.json` | PASS |
| EV-003 | validation/test | Artifact validation, comparison, and tests | package loader; comparison scripts; focused/full pytest | PASS |
| EV-004 | command | Final status and diff hygiene | `git status --short`; `git diff`; `git diff --check`; trailing-whitespace scan | PASS |

## EV-001 - Startup And Prior Artifact Review

- **Date:** 2026-07-12
- **Method or command:** Read `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and `ops/TASK-20260712__bounded_n6_interval_certificate_export/`.
- **Method or command:** `git status --short`.
- **Relevant output:** Initial `git status --short` produced no entries.
- **Relevant output:** Prior task evidence recorded `small_n_interval_certificate_n6_attempt.json` with 60 covered canonical orders and bracket `(8.4678350760883720482752323732711374759674072265625, 8.4680350760883715821591977146454155445098876953125]`.
- **Interpretation:** The task-scoped artifact was ready to promote or regenerate as a checked example.
- **Limitations:** Review of prior evidence does not by itself create checked `examples/` coverage.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---startup-and-artifact-review`

## EV-002 - Checked n6 Example Regeneration

- **Date:** 2026-07-12
- **Method or command:** `python -c "import sys; sys.path.insert(0, 'src'); from power_ringmin.small_n_interval_certificate import main_small_n; raise SystemExit(main_small_n(['--n','6','--max-canonical-orders','60','--output','examples/small_n_interval_certificate_n6.json','--digits','80','--guard-decimal','1e-70','--radius-eta','1e-4','--local-max-attempts','8','--created-at-utc','2026-07-12T00:00:00Z']))"`.
- **Relevant output:** `wrote examples\small_n_interval_certificate_n6.json n=6 bracket=(8.4678350760883720482752323732711374759674072265625, 8.4680350760883715821591977146454155445098876953125] classification=computer_certified_result covered=60`.
- **Artifact:** `examples/small_n_interval_certificate_n6.json`.
- **Interpretation:** The exporter generated a checked finite `n=6` interval certificate artifact covering all 60 canonical cyclic index orders.
- **Limitations:** This result is finite n=6 evidence only and depends on the repository's documented guarded `mpmath.iv` interval backend contract.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---checked-example-regeneration`

## EV-003 - Artifact Validation Comparison And Tests

- **Date:** 2026-07-12
- **Method or command:** Loaded `examples/small_n_interval_certificate_n6.json` with `load_small_n_interval_certificate_artifact`.
- **Relevant output:** `n 6`; `covered 60`; `expected 60`; lower endpoint `8.4678350760883720482752323732711374759674072265625`; upper endpoint `8.4680350760883715821591977146454155445098876953125`; source order `[6, 1, 2, 5, 4, 3]`; source commit `32743f7f791c8a1550689e39f56347a194d4520a`; `git_dirty False`; `created_at_utc 2026-07-12T00:00:00Z`.
- **Method or command:** `Get-Item examples\small_n_interval_certificate_n6.json`.
- **Relevant output:** File size was `379015` bytes.
- **Method or command:** Compared the checked example against `ops/TASK-20260712__bounded_n6_interval_certificate_export/small_n_interval_certificate_n6_attempt.json`.
- **Relevant output:** Top-level differences were `local_brackets` and `provenance`; `result_same True`; `local_summaries_same True`; `evidence_diff False`; the first embedded local bracket differed only in `provenance`.
- **Method or command:** `python -m pytest tests\test_small_n_interval_certificate.py`.
- **Relevant output:** `19 passed in 2.88s`.
- **Method or command:** `python -m pytest`.
- **Relevant output:** `68 passed in 13.69s`.
- **Interpretation:** Package semantic validation accepts the checked artifact. Its mathematical result and summary evidence match the task-scoped artifact, while provenance was regenerated for the checked example and current source commit. Focused and full tests pass.
- **Limitations:** Passing tests do not prove any all-`n` theorem or remove the interval-backend provenance limitation.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---validation-comparison-and-tests`

## EV-004 - Final Status And Diff Hygiene

- **Date:** 2026-07-12
- **Method or command:** `git status --short`.
- **Relevant output:** Modified tracked files: `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, `tests/test_small_n_interval_certificate.py`. New untracked paths: `examples/small_n_interval_certificate_n6.json`, `ops/TASK-20260712__promote_n6_interval_certificate_example/`.
- **Method or command:** `git diff --stat`.
- **Relevant output:** Tracked diff showed updates to `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, and `tests/test_small_n_interval_certificate.py`.
- **Method or command:** `git diff -- PROJECT_KNOWLEDGE.md CURRENT_STATUS.md tests/test_small_n_interval_certificate.py`.
- **Relevant output:** Inspected tracked status/knowledge/test updates documenting the checked `n=6` example artifact and loader regression test.
- **Method or command:** `git diff --check`.
- **Relevant output:** No output.
- **Method or command:** `rg -n "[ \t]+$" PROJECT_KNOWLEDGE.md CURRENT_STATUS.md tests\test_small_n_interval_certificate.py examples\small_n_interval_certificate_n6.json ops\TASK-20260712__promote_n6_interval_certificate_example`.
- **Relevant output:** No matches.
- **Interpretation:** Final tracked diff and new artifact/task dossier hygiene checks passed.
- **Limitations:** `git diff --check` does not inspect untracked files until staged, so the separate trailing-whitespace scan covered the new example artifact and task dossier.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---final-handoff`

# EVIDENCE - TASK-20260711__n4_highprec_export_rejection / n=4 High-Precision Export Rejection

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | computation | Startup reproduction and root cause | `src/power_ringmin/export_fixed_order_cli.py`, `src/power_ringmin/highprec.py` | PASS |
| EV-002 | file | Exporter stabilization and regression test | `src/power_ringmin/export_fixed_order_cli.py`, `tests/test_fixed_order_artifact_cli.py` | PASS |
| EV-003 | test | Focused, full, and temporary manual verification | `tests/`, `examples/fixed_order_batch_end_to_end/` | PASS |
| EV-004 | command | Final diff and whitespace check | `git status --short`; `git diff --stat`; `git diff`; `git diff --check` | PASS |

## EV-001 - Startup Reproduction And Root Cause

- **Date:** 2026-07-11
- **Method or command:** Read startup files and relevant source/tests. Ran `python -c "... power_ringmin.export_fixed_order_cli.main([... '--index-order','4,1,3,2','--backend','mpmath','--digits','80','--local-radius-eta','1e-12', ...])"` and a diagnostic `python -c` that compared the raw `full_radius_mp((16,1,9,4), digits=80)` value with `mp.nstr(R, n=80)`.
- **Relevant output:** Exporter error: `exported fixed-order radius is not feasible at the requested precision; increase --digits`. Diagnostic values: raw radius `1.49562841187499713143355762255872002290331802621242622455694034422615424392067573535622920042538278`; 80-digit text `1.4956284118749971314335576225587200229033180262124262245569403442261542439206757`; raw minus text about `3.58e-80`; tolerance `1e-40`; raw margin about `-9.9999999999999999999999999999999999999993e-41`; text margin about `-1.0000000000000000000000000000000000000012e-40`; raw feasibility `True`; text feasibility `False`.
- **Interpretation:** The fixed-order radius computed by the high-precision bisection is accepted within the requested STN tolerance, but the artifact decimal representation can round slightly downward and fail the export guard. This is a finite numerical robustness issue in the exporter path.
- **Limitations:** This evidence covers the explicit n=4 fixed cyclic order `(4,1,3,2)` only. It is not a global optimum certificate or theorem.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---startup-and-reproduction`

## EV-002 - Exporter Stabilization

- **Date:** 2026-07-11
- **Method or command:** File edits using `apply_patch`.
- **Relevant output:** `src/power_ringmin/export_fixed_order_cli.py` now converts the mpmath radius to the exact decimal that will be written, checks that decimal with `is_feasible_mp`, and adaptively increases near-boundary values until the serialized decimal is feasible. The high-precision CLI path recovers positions and constructs the artifact from that stabilized decimal string. `tests/test_fixed_order_artifact_cli.py` now includes the formerly rejected n=4 index order `(4,1,3,2)`.
- **Interpretation:** The exporter path is robust to tiny downward decimal serialization at the feasibility tolerance boundary without weakening `export_highprec_artifact` validation.
- **Limitations:** The stabilization is covered for the known n=4 failure and uses bounded adaptive search; unusual future cases may still require larger precision or manual eta review.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---exporter-stabilized`

## EV-003 - Focused Full And Manual Verification

- **Date:** 2026-07-11
- **Method or command:** `python -m pytest tests/test_fixed_order_artifact_cli.py tests/test_fixed_order_artifact_batch_cli.py tests/test_examples_fixed_order_batch_e2e.py tests/test_verify_fixed_order_artifacts_cli.py`; `python -m pytest`; temporary source-checkout batch export plus `power_ringmin.verify_fixed_order_artifacts_cli` inside a workspace temporary directory.
- **Relevant output:** Focused tests: `16 passed in 2.36s`. Full suite: `30 passed in 8.36s`. Temporary export wrote `fixed_order_0001_n3.json` and `fixed_order_0002_n4.json`; standalone batch verification reported `batch standalone verification complete count=2 passed=2 failed=0`. An attempted extra output directory under `C:\tmp\power-ringmin-n4-highprec-export` failed with Windows `Accesso negato`, so the extra manual verification used a workspace temporary directory that was cleaned up.
- **Interpretation:** The restored n=4 high-precision batch example exports and verifies successfully through the same module entry-point path used by the checked example test.
- **Limitations:** Tests cover finite explicit orders only. Passing tests do not establish a global optimum, certified quadratic-radii result, or theorem.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---verification-passed`

## EV-004 - Final Diff And Whitespace Check

- **Date:** 2026-07-11
- **Method or command:** `git status --short`; `git diff --stat`; `git diff`; `git diff --check`.
- **Relevant output:** `git status --short` showed modified `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, `examples/fixed_order_batch_end_to_end/README.md`, `examples/fixed_order_batch_end_to_end/index_orders.json`, `src/power_ringmin/export_fixed_order_cli.py`, `tests/test_examples_fixed_order_batch_e2e.py`, and `tests/test_fixed_order_artifact_cli.py`, plus untracked `ops/TASK-20260711__n4_highprec_export_rejection/`. `git diff --stat` reported 7 tracked files changed with 119 insertions and 20 deletions. `git diff --check` produced no output.
- **Interpretation:** The tracked diff is scoped to the exporter robustness fix, n=4 example restoration, regression tests, and durable global status/knowledge. The untracked task dossier is the expected operational memory for this task.
- **Limitations:** `git diff --check` does not include untracked files until the user stages them for manual review; the new task dossier files were manually inspected.
- **Linked log entry:** `TASK_LOG.md#2026-07-11---ready-for-review`

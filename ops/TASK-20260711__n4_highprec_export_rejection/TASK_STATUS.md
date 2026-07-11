# TASK_STATUS - TASK-20260711__n4_highprec_export_rejection / n=4 High-Precision Export Rejection

Last update: 2026-07-11

## State

- **Mode:** STANDARD
- **Status:** READY_FOR_REVIEW
- **Objective:** Investigate why the n=4 high-precision batch example for index order `(4,1,3,2)` was rejected as infeasible at 80 digits, then either document the limitation or fix the exporter path if it is a robustness issue.
- **Expected output:** Root-cause evidence, a narrow exporter fix or documented limitation, focused regression coverage, updated example if fixed, verification evidence, and updated durable project memory.

## Scope

- **In scope:** mpmath fixed-order exporter path; decimal serialization feasibility guard; index order `(4,1,3,2)` / radius order `(16,1,9,4)`; the fixed-order batch end-to-end example; focused tests and verification.
- **Out of scope:** Global cyclic-order search; certified global optimum claims; changing the artifact schema; changing the mathematical definition of feasibility; importing new Ringmin pipeline code.

## Verified Facts

- Repository root is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- `CURRENT_STATUS.md` proposed this exact task as the next atomic action.
- The previous end-to-end example task recorded that an attempted n=4 high-precision order was rejected by the exporter as infeasible at the requested precision.
- The rejection reproduces through `power_ringmin.export_fixed_order_cli` for `--index-order 4,1,3,2 --backend mpmath --digits 80 --local-radius-eta 1e-12`.
- At 80 digits, `full_radius_mp((16,1,9,4))` returns a raw mpmath radius whose STN margin is within the default tolerance, while its 80-significant-digit decimal serialization rounds slightly downward and fails the same tolerance check.
- The fixed exporter path exports and verifies the n=4 order `(4,1,3,2)` at 80 digits with `--local-radius-eta 1e-12`.
- `examples/fixed_order_batch_end_to_end/index_orders.json` now includes the n=4 index order `(4,1,3,2)`.

## Assumptions / Inferences

- Because the raw radius is accepted by the high-precision feasibility oracle and the serialized decimal fails by a tiny amount, the observed rejection is a numerical export robustness issue, not evidence that the fixed cyclic order is mathematically infeasible.
- A safe exporter fix should only increase the exported high-precision radius by the minimum amount needed for the artifact's own decimal radius to pass the requested feasibility tolerance.

## Decisions And Rationale

- Fix the mpmath exporter path instead of merely documenting a limitation, because the failure is caused by decimal serialization of a near-boundary numerical radius.
- Keep `export_highprec_artifact` strict: it should continue to mark infeasible decimals as infeasible rather than silently changing arbitrary API inputs.
- Stabilize the CLI-computed mpmath radius before position recovery and artifact construction.

## Plan And Expected Delta

- Create task dossier and record the reproduced root cause. COMPLETE.
- Add exporter-side stable mpmath radius selection. COMPLETE.
- Add focused regression coverage for the n=4 mpmath export path. COMPLETE.
- Restore the n=4 order to the batch end-to-end example and test it. COMPLETE.
- Run focused and full verification. COMPLETE.
- Update durable memory and final task status. COMPLETE.

## Verification

- **Checks:** Initial reproduction and diagnostic command; `python -m pytest tests/test_fixed_order_artifact_cli.py tests/test_fixed_order_artifact_batch_cli.py tests/test_examples_fixed_order_batch_e2e.py tests/test_verify_fixed_order_artifacts_cli.py`; `python -m pytest`; temporary source-checkout batch export plus batch standalone verification; `git status --short`; `git diff --stat`; `git diff`; `git diff --check`.
- **Observed result:** Initial exporter rejected the serialized 80-digit n=4 radius; raw radius margin was accepted, serialized decimal margin was rejected. After the fix, focused tests reported `16 passed`, full tests reported `30 passed`, and temporary source-checkout export/verify reported two passing artifacts including `fixed_order_0002_n4.json`.
- **Limitations:** The n=4 result is finite fixed-order numerical evidence only. It is not a global optimum certificate or theorem.

## Blockers / Risks

- No current blocker.
- Residual risk: the stabilization step is intentionally conservative and covered for the known n=4 failure; future much larger or tighter examples may still require precision/eta review.

## Next Atomic Action

- User reviews the n=4 high-precision export robustness diff and decides whether to commit manually.

## Handoff

- **Last verified result:** `python -m pytest` passed 30 tests and temporary source-checkout batch export/verification passed for n=3 and n=4 artifacts.
- **Files changed:** `src/power_ringmin/export_fixed_order_cli.py`, `tests/test_fixed_order_artifact_cli.py`, `examples/fixed_order_batch_end_to_end/index_orders.json`, `examples/fixed_order_batch_end_to_end/README.md`, `tests/test_examples_fixed_order_batch_e2e.py`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `src/power_ringmin/export_fixed_order_cli.py`, `src/power_ringmin/highprec.py`, `tests/test_fixed_order_artifact_cli.py`, `tests/test_examples_fixed_order_batch_e2e.py`.

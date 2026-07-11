# TASK_LOG - TASK-20260711__n4_highprec_export_rejection / n=4 High-Precision Export Rejection

Append-only. Add a new entry to correct previous information.

## 2026-07-11 - Startup And Reproduction

- **Action:** Read startup files, previous fixed-order batch example dossier, exporter and verifier code paths, relevant tests, and the end-to-end example. Reproduced the n=4 mpmath exporter rejection and inspected the raw high-precision radius versus its exported decimal.
- **Result:** The single-order exporter rejected `--index-order 4,1,3,2 --backend mpmath --digits 80 --local-radius-eta 1e-12`. The raw `full_radius_mp` value had STN margin just above the default `-1e-40` tolerance, while its 80-digit decimal text rounded downward and had STN margin just below `-1e-40`.
- **Interpretation:** The rejected n=4 example is an exporter robustness issue caused by near-boundary decimal serialization, not evidence of fixed-order infeasibility.
- **Evidence:** `EVIDENCE.md#ev-001---startup-reproduction-and-root-cause`
- **Next step:** Add exporter-side stabilization for mpmath radii and regression coverage.

## 2026-07-11 - Exporter Stabilized

- **Action:** Added exporter-side mpmath radius stabilization before high-precision position recovery and artifact construction. Added a focused regression for `--index-order 4,1,3,2 --backend mpmath --digits 80 --local-radius-eta 1e-12`.
- **Result:** The exporter now checks the exact decimal radius it will write and adaptively nudges near-boundary radii upward until that serialized value is feasible under the requested STN tolerance.
- **Interpretation:** The artifact guard remains strict, while CLI-computed high-precision artifacts avoid false rejection from downward decimal rounding.
- **Evidence:** `EVIDENCE.md#ev-002---exporter-stabilization`
- **Next step:** Restore the n=4 order to the batch end-to-end example and verify.

## 2026-07-11 - Verification Passed

- **Action:** Restored the n=4 order to `examples/fixed_order_batch_end_to_end/index_orders.json`, updated the example README and test expectation, then ran focused tests, full tests, and a temporary source-checkout export plus standalone batch verification.
- **Result:** Focused exporter/batch/verifier/example tests reported `16 passed`; full repository tests reported `30 passed`; temporary source-checkout export/verify produced passing n=3 and n=4 artifacts.
- **Interpretation:** The original n=4 high-precision batch example now works through the exporter and standalone verifier path.
- **Evidence:** `EVIDENCE.md#ev-003---focused-full-and-manual-verification`
- **Next step:** Update durable memory, inspect final diff, and run whitespace checks.

## 2026-07-11 - Ready For Review

- **Action:** Updated `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, task status, task log, and evidence; inspected final status and diff; ran whitespace check.
- **Result:** Task status is `READY_FOR_REVIEW`; `git diff --check` produced no output.
- **Interpretation:** The bounded n=4 high-precision export rejection task is fixed, verified, recorded, and ready for user review.
- **Evidence:** `EVIDENCE.md#ev-004---final-diff-and-whitespace-check`
- **Next step:** User reviews the diff and decides whether to commit manually.

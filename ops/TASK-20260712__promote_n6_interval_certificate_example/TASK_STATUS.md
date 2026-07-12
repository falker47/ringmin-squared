# TASK_STATUS - TASK-20260712__promote_n6_interval_certificate_example / Promote n=6 Interval Certificate Example

Last update: 2026-07-12

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** Review the task-scoped finite `n=6` interval certificate artifact and promote it as a checked `examples/` artifact when appropriate.
- **Expected output:** A checked `examples/small_n_interval_certificate_n6.json` artifact, loader regression coverage, verification evidence, and updated durable project memory.

## Scope

- **In scope:** Startup inspection, prior task-artifact review, checked example regeneration, semantic artifact validation, comparison against the task-scoped artifact, focused/full tests, and durable handoff updates.
- **Out of scope:** Changing interval-verifier semantics, optimizing exporter runtime, attempting `n=7`, claiming an exact optimum, claiming an all-`n` theorem, or making Git commits.

## Verified Facts

- Repository root is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- The prior task-scoped artifact `ops/TASK-20260712__bounded_n6_interval_certificate_export/small_n_interval_certificate_n6_attempt.json` was reviewed through its task status, log, evidence, and JSON header.
- The task-scoped artifact covered 60 canonical `n=6` orders and recorded global bracket `(8.4678350760883720482752323732711374759674072265625, 8.4680350760883715821591977146454155445098876953125]`.
- The checked example was regenerated before any task-memory edits, so its repository provenance recorded source commit `32743f7f791c8a1550689e39f56347a194d4520a` and `git_dirty=false`.
- `examples/small_n_interval_certificate_n6.json` covers 60 canonical orders and records the same global bracket as the task-scoped artifact.
- Relative to the task-scoped artifact, the regenerated example has the same result, evidence record, and local bracket summaries. The top-level provenance changed, and each embedded local bracket differs only in nested provenance.
- Focused small-n interval certificate tests passed with `19 passed in 2.88s`.
- Full tests passed with `68 passed in 13.69s`.

## Assumptions / Inferences

- Regeneration is preferable to copying because the checked artifact should record the `examples/` output path in its provenance command.
- The changed source commit in the checked artifact is expected because the prior bounded `n=6` export task appears to have been committed before this task began.

## Decisions And Rationale

- **Decision:** Regenerate `examples/small_n_interval_certificate_n6.json` from the clean worktree rather than copying the task-scoped JSON.
- **Rationale:** Regeneration preserves clean source provenance while embedding the checked example output path and explicit production parameters in the artifact command.
- **Evidence classification:** The generated example artifact is classified as `computer_certified_result` under the repository's documented local interval-verifier semantics and guarded `mpmath.iv` interval backend contract.

## Plan And Expected Delta

- Read startup memory and inspect working tree. COMPLETE.
- Review the task-scoped `n=6` artifact and prior evidence. COMPLETE.
- Regenerate the checked `examples/` artifact from the clean worktree. COMPLETE.
- Validate the artifact and compare it against the task-scoped artifact. COMPLETE.
- Add loader regression coverage for the checked `n=6` example. COMPLETE.
- Run focused and full tests. COMPLETE.
- Update durable memory and final status/diff checks. COMPLETE.

## Verification

- **Checks:** Startup/status review; prior artifact review; checked example regeneration; package artifact load/validation; task-artifact comparison; focused small-n certificate tests; full test suite; final status/diff hygiene checks.
- **Observed result:** The checked `n=6` example artifact was generated, validated, and covered by a focused regression test. Focused and full tests passed.
- **Limitations:** This is finite n=6 evidence only. It is not an exact optimum value, not a theorem for all `n`, not an asymptotic result, and it depends on the documented guarded `mpmath.iv` interval backend contract.

## Blockers / Risks

- No current blocker.
- Residual risk: the `n=6` artifact is larger than prior checked examples because it embeds 60 local brackets; this is expected for the current self-contained certificate format.

## Next Atomic Action

- User reviews the promoted checked `n=6` example artifact and decides whether to run a bounded `n=7` dry-run/order-count preflight in a fresh task.

## Handoff

- **Last verified result:** `python -m pytest` passed with `68 passed in 13.69s`.
- **Generated artifact:** `examples/small_n_interval_certificate_n6.json`.
- **Files changed:** `examples/small_n_interval_certificate_n6.json`, `tests/test_small_n_interval_certificate.py`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `ops/TASK-20260712__promote_n6_interval_certificate_example/EVIDENCE.md`, then `examples/small_n_interval_certificate_n6.json` if deeper artifact audit is needed.
- **Suggested manual commit message:** `Promote checked n6 interval certificate example`.

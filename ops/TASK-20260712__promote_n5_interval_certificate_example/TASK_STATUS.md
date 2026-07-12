# TASK_STATUS - TASK-20260712__promote_n5_interval_certificate_example / Promote n=5 Interval Certificate Example

Last update: 2026-07-12

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** Decide whether the finite `n=5` interval certificate should be promoted to `examples/` with clean-tree provenance or kept only as task-scoped evidence.
- **Decision:** Promote it to `examples/small_n_interval_certificate_n5.json` by regenerating from the clean repository state, while keeping the prior dirty-provenance task artifact as historical task evidence.
- **Expected output:** Checked `n=5` example artifact, focused test coverage for loading it, durable memory updates, and verification evidence.

## Scope

- **In scope:** Inspect the prior `n=5` task artifact and provenance, regenerate a clean-provenance example artifact, add checked-artifact tests, update durable memory, and verify.
- **Out of scope:** Changing interval-verifier semantics, optimizing certificate generation, deleting prior task evidence, attempting `n=6`, claiming an exact optimum, or claiming any all-`n` theorem.

## Verified Facts

- Repository root is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- The prior `n=5` task artifact validated and recorded the finite bracket `(3.934227717145796443531935437931679189205169677734375, 3.9344277171457964215051106293685734272003173828125]`, but its artifact provenance recorded `git_dirty=true`.
- `examples/small_n_interval_certificate_n5.json` was regenerated before any task files were created in this chat, and records source commit `1b013793eafe03661d12e0c1ae5aec3e9173d151` with `git_dirty=false`.
- The promoted artifact covers all 12 canonical `n=5` cyclic index orders and records the same finite bracket as the task-scoped attempt.
- Focused small-n interval certificate tests passed with `18 passed in 1.83s`.
- Final full tests passed with `67 passed in 10.27s`.

## Assumptions / Inferences

- A checked `n=5` example is appropriate because it extends the already checked finite `n=3` and `n=4` interval certificate example family without changing artifact semantics.
- The main reason to avoid promotion was dirty provenance; regenerating from the clean tree removed that concern.
- The prior task-scoped artifact should remain as evidence for the original attempt rather than being moved or deleted.

## Plan And Expected Delta

- Read startup memory and inspect the relevant prior task dossier. COMPLETE.
- Decide promotion versus task-scoped retention. COMPLETE: promote.
- Regenerate `examples/small_n_interval_certificate_n5.json` from the clean tree. COMPLETE.
- Add tests that load and validate the checked `n=5` artifact. COMPLETE.
- Run focused and full verification. COMPLETE.
- Inspect final status, diff, and whitespace hygiene. COMPLETE.

## Verification

- **Checks:** clean initial `git status --short`; artifact regeneration; provenance inspection; focused small-n interval certificate tests; full test suite; final `git status --short`; final `git diff`; final `git diff --check`; trailing-whitespace scan over changed files.
- **Observed result:** The promoted artifact records `git_dirty=false`; focused tests passed with `18 passed in 1.83s`; full tests passed with `67 passed in 10.27s`; final diff hygiene checks passed.
- **Evidence classification:** The promoted artifact is classified as `computer_certified_result` under the repository's documented local interval-verifier semantics and guarded `mpmath.iv` interval backend contract.
- **Limitations:** The result is finite `n=5` evidence only, not an exact optimum value, not a theorem for all `n`, and not an asymptotic claim. It still depends on the documented guarded `mpmath.iv` interval backend contract.

## Blockers / Risks

- No current blocker.
- Residual risk: the artifact is larger than the `n=3` and `n=4` examples and embeds 12 local brackets, so user review should focus on whether this example size is acceptable in the repository.

## Next Atomic Action

- User reviews the promoted `n=5` example artifact and decides whether to commit manually.

## Handoff

- **Last verified result:** `python -m pytest` passed with `67 passed in 10.27s`.
- **Promoted artifact:** `examples/small_n_interval_certificate_n5.json`.
- **Prior task artifact retained:** `ops/TASK-20260712__bounded_n5_interval_certificate_attempt/small_n_interval_certificate_n5_attempt.json`.
- **Files changed:** `examples/small_n_interval_certificate_n5.json`, `tests/test_small_n_interval_certificate.py`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Suggested manual commit message:** `Promote n5 interval certificate example`

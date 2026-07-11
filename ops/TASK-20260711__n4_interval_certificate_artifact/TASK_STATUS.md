# TASK_STATUS - TASK-20260711__n4_interval_certificate_artifact / N=4 Interval Certificate Artifact

Last update: 2026-07-11

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** Implement a bounded `n=4` interval certificate artifact/export path and add `examples/small_n_interval_certificate_n4.json` only if validation passes.
- **Expected output:** Source/tests for the bounded `n=4` exporter, a validated checked example artifact, updated durable memory, and final `READY_FOR_REVIEW` handoff.

## Scope

- **In scope:** Add a bounded `n=4` small-n interval certificate export path; generate exactly the three canonical `n=4` local brackets; validate and check in the `n=4` example JSON only after validation; add focused tests; run verification; update project memory.
- **Out of scope:** Larger-`n` certificate generation; broad interval-backend hardening; schema redesign; Git staging or commits.

## Verified Facts

- Repository root is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- The prior `n=4` design task selected a runtime-bounded certificate artifact/export attempt as the next atomic task.
- `n=4` has exactly three canonical cyclic index orders under the repository convention: `(4, 1, 2, 3)`, `(4, 1, 3, 2)`, and `(4, 2, 1, 3)`.
- `build_bounded_small_n_interval_certificate_fixture` enforces an explicit `max_canonical_orders` ceiling before generating local brackets.
- `build_n4_interval_certificate_fixture`, `export_n4_interval_certificate_artifact`, and `main_n4` implement the bounded n=4 artifact/export path.
- `pyproject.toml` registers `power-ringmin-export-n4-interval-certificate`.
- `examples/small_n_interval_certificate_n4.json` was written by the n=4 exporter and reloads through `load_small_n_interval_certificate_artifact`.
- The checked n=4 artifact covers exactly three canonical orders and records global bracket `(1.4955284118749971877804227915476076304912567138671875, 1.4957284118749971657535979829845018684864044189453125]`.

## Assumptions / Inferences

- The requested phrase "check in" means create the repository artifact file for user review, not run forbidden Git staging or commit commands.
- The `n=4` artifact remains finite `n=4` evidence under the documented local interval-verifier semantics, not an exact all-`n` theorem.

## Decisions And Rationale

- Use `STRICT` mode because this task creates a `computer_certified_result` artifact.
- Keep the new path bounded to `n=4` with explicit canonical-order and local-attempt bounds.
- Reuse the existing aggregate validator and local bracket verifier rather than changing certificate semantics.

## Plan And Expected Delta

- Create this task dossier. COMPLETE.
- Add bounded `n=4` builder/exporter and CLI entry point. COMPLETE.
- Add focused `n=4` tests and console script registration. COMPLETE.
- Generate `examples/small_n_interval_certificate_n4.json` through the exporter and reload/validate it. COMPLETE.
- Run focused and full verification, inspect diffs, and update durable memory. COMPLETE.

## Verification

- **Checks:** `python -m pytest tests\test_small_n_interval_certificate.py::test_n4_interval_certificate_fixture_covers_every_canonical_order -q`; n=4 exporter invocation; checked artifact reload/summary command; `python -m pytest tests\test_small_n_interval_certificate.py -q`; `python -m pytest`; `git status --short`; `git diff --stat`; tracked `git diff` inspection; `git diff --check`; trailing-whitespace scan.
- **Observed result:** The n=4 fixture test passed; exporter wrote the checked n=4 artifact with `covered=3`; reload/summary reported n=4, covered 3, classification `computer_certified_result`, and bracket `(1.4955284118749971877804227915476076304912567138671875, 1.4957284118749971657535979829845018684864044189453125]`; focused tests passed with `12 passed`; full suite passed with `60 passed in 11.89s`; `git diff --check` produced no output; trailing-whitespace scan produced no matches.
- **Limitations:** The artifact is finite n=4 evidence only. It is not an exact optimum value, not an asymptotic result, and not a theorem for all `n`; it still depends on the documented guarded `mpmath.iv` interval backend contract.

## Blockers / Risks

- No current blocker.
- Residual risk: the checked artifact still depends on the documented guarded `mpmath.iv` interval backend contract pending future production hardening.

## Next Atomic Action

- User reviews the bounded n=4 certificate artifact/export changes and decides whether to commit manually.

## Handoff

- **Last verified result:** `python -m pytest` passed with `60 passed in 11.89s`; `git diff --check` produced no output after the final diff inspection.
- **Files changed:** `src/power_ringmin/small_n_interval_certificate.py`, `tests/test_small_n_interval_certificate.py`, `pyproject.toml`, `examples/small_n_interval_certificate_n4.json`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Files to read first:** `src/power_ringmin/small_n_interval_certificate.py`, `tests/test_small_n_interval_certificate.py`, `examples/small_n_interval_certificate_n4.json`.

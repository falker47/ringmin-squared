# TASK_STATUS - TASK-20260711__n4_finite_certificate_next_step_design / N=4 Finite-Certificate Next-Step Design

Last update: 2026-07-11

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** Design the next finite-certificate step for `n=4`, choosing between a runtime-bounded interval certificate attempt and verifier/format hardening before larger certificates.
- **Expected output:** A recorded design decision, supporting evidence, updated project knowledge, and updated current status.

## Scope

- **In scope:** Inspect current certificate code and task memory; run a bounded in-memory `n=4` feasibility probe; choose the next atomic certificate task; record evidence and handoff.
- **Out of scope:** Implementing the `n=4` certificate artifact/exporter; checking in an `n=4` certificate artifact; broad verifier/format hardening; larger-`n` certificate generation; Git staging or commits.

## Verified Facts

- Repository root is `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- Startup files `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md` were read.
- Initial `git status --short` produced no entries.
- The current small-n aggregate validator is implemented in `src/power_ringmin/small_n_interval_certificate.py`.
- The current fixed-order interval bracket generator/exporter is implemented in `src/power_ringmin/interval_bracket_exporter.py`.
- The current local interval bracket verifier is implemented in `src/power_ringmin/interval_verifier.py`.
- `n=4` has exactly three canonical cyclic index orders: `(4, 1, 2, 3)`, `(4, 1, 3, 2)`, and `(4, 2, 1, 3)`.
- An in-memory design probe generated and validated one local interval bracket per canonical `n=4` order and accepted the aggregate certificate validator in `0.8` seconds.

## Assumptions / Inferences

- The user requested a design choice, not implementation of the chosen next task in this chat.
- A checked `n=4` artifact should still be treated as finite evidence only under the documented local interval-verifier semantics, not as an exact optimum theorem or an all-`n` result.
- Because the n=4 order space has only three canonical orders and the probe passed quickly, broad hardening before the n=4 attempt would be premature.

## Decisions And Rationale

- Use `STRICT` mode because this task affects the finite-certificate path and evidence classification.
- Choose a runtime-bounded `n=4` interval certificate attempt as the next task.
- Defer broader verifier/format hardening until after a checked `n=4` artifact exists, so hardening is guided by a nontrivial artifact rather than by speculation.
- Keep the next task bounded to `n=4`; do not begin larger certificates in the same step.

## Plan And Expected Delta

- Create this task dossier and `DESIGN.md`. COMPLETE.
- Record the in-memory `n=4` probe evidence. COMPLETE.
- Update `PROJECT_KNOWLEDGE.md` with the design decision and readiness evidence. COMPLETE.
- Update `CURRENT_STATUS.md` with the chosen next atomic action. COMPLETE.
- Run final verification and diff checks. COMPLETE.

## Verification

- **Checks:** Startup/source inspection; `python -c` canonical `n=4` enumeration; in-memory `n=4` local-bracket and aggregate-certificate validation probe; `python -m pytest`; `git status --short`; `git diff --stat`; `git diff`; `git diff --check`.
- **Observed result:** The `n=4` probe covered three canonical orders and accepted the aggregate bracket `(1.4955284118749971877804227915476076304912567138671875, 1.4957284118749971657535979829845018684864044189453125]`; `python -m pytest` passed with `55 passed in 6.97s`; `git diff --check` produced no output; trailing-whitespace scan found no matches.
- **Limitations:** The probe did not write a checked `n=4` artifact and does not establish any theorem for all `n`. It is readiness evidence for the next task.

## Blockers / Risks

- No current blocker.
- Residual risk: a checked `n=4` artifact will still depend on the documented guarded `mpmath.iv` interval backend contract until a later production-certification hardening task audits or replaces it.

## Next Atomic Action

- Implement the runtime-bounded `n=4` interval certificate artifact/export path and check in the resulting artifact only if validation passes.

## Handoff

- **Last verified result:** `python -m pytest` passed with `55 passed in 6.97s`; final diff checks passed.
- **Files changed:** `ops/TASK-20260711__n4_finite_certificate_next_step_design/`, `PROJECT_KNOWLEDGE.md`, and `CURRENT_STATUS.md`.
- **Files to read first:** `ops/TASK-20260711__n4_finite_certificate_next_step_design/DESIGN.md`, `src/power_ringmin/small_n_interval_certificate.py`, `src/power_ringmin/interval_bracket_exporter.py`, `src/power_ringmin/interval_verifier.py`.

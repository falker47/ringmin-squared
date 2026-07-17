# EVIDENCE - TASK-20260717__relation_compatible_full_score_classification / Relation-Compatible Full-Score Classification

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / confirmation | Startup, scope, and independent symbolic audits | retained PG material and clean repository state | PASS |
| EV-002 | computation | Polynomial local/transition diagnostic | exact_diagnostic.py | PASS |
| EV-003 | test / command | Static checks, regressions, suite, and artifacts | repository commands | PASS |
| EV-004 | inspection | Proof, scope, synchronization, and final diff | project files and Git inspection | PASS |

## EV-001 - Startup, Scope, And Independent Derivation

- **Date:** 2026-07-17
- **Method or command:** Read AGENTS.md, start.md, PROJECT_KNOWLEDGE.md,
  CURRENT_STATUS.md, predecessor task memory,
  research/PRODUCT_DISTANCE_SURROGATE.md, and
  research/NEXT_RESEARCH_STEPS.md; inspect `git status`, `git rev-parse HEAD`,
  and the retained scaffold/Ferrers formulas; compare three independent
  read-only derivations.
- **Relevant output:** clean `main...origin/main` worktree at
  `9664e342964e27c36b8e203f0dc646c811c66409`; unanimous agreement that the
  six triple and four singleton forms are exhaustive, the candidate bound is
  true and sharp, and relation-compatibility is equivalent to full score
  \(T\).
- **Interpretation:** The task began from synchronized predecessor results,
  and the theorem was independently reproducible before editing.
- **Limitations:** Independent agreement does not replace the written proof.
- **Linked log entry:** TASK_LOG.md, STRICT startup and independent derivation.

## EV-002 - Polynomial Local And Transition Diagnostic

- **Date:** 2026-07-17
- **Method or command:**
  `python ops\TASK-20260717__relation_compatible_full_score_classification\exact_diagnostic.py`
- **Relevant output:**
  \[
  \begin{array}{c|r|r|r|r}
  m&\text{local words}&\text{compatible closing cases}&
  \text{transition types}&\text{sharp witnesses}\\ \hline
  3&180&3&4&2\\
  4&448&5&4&2\\
  9&5508&11&4&2\\
  34&309808&41&4&2.
  \end{array}
  \]
- **Interpretation:** For every scanned \((j,k,h)\) with distinct adjacent
  paths, the script compares PG50--PG51 with pairs read directly from the
  corresponding local word and checks the product bound. It verifies all
  four ordered type transitions, the exact two equality placements, every
  locally possible compatible closing path, and two explicit PG46 full-order
  witnesses per row. Those witnesses independently attain the sharp
  distance-three bound and have full score \(T\).
- **Limitations:** The fixed rows corroborate rather than prove the symbolic
  theorem. The local scan is a polynomial over-approximation and performs no
  path-permutation or matching enumeration.
- **Linked log entry:** TASK_LOG.md, proof and diagnostic implementation.

## EV-003 - Static Checks, Regressions, Suite, And Artifacts

- **Date:** 2026-07-17
- **Method or commands:** in-memory `compile(...)`; `python -m ruff check`;
  `python -m ruff format --check`; focused product-distance pytest with
  `-p no:cacheprovider` and a task-specific `C:\tmp` basetemp; complete
  pytest suite serially with the same cache isolation; checked-artifact schema
  regression; set `PYTHONPATH=src` and run
  `python -m power_ringmin.verify_checked_artifacts`.
- **Relevant output:** compile PASS; Ruff lint and final format check PASS;
  focused product-distance regression 49 PASS; complete suite 283 PASS;
  schema regression 4 PASS; checked artifacts verified with 4 certificates
  and 76 local brackets.
- **Retained failed check:** the first Ruff format check reported that the
  diagnostic would be reformatted. `python -m ruff format` changed that sole
  file mechanically; the repeated format check then passed.
- **Interpretation:** No production, schema, artifact, or repository
  regression was detected. The single failed check was a source-format issue,
  not a mathematical or runtime failure, and remains recorded.
- **Limitations:** Existing repository tests do not prove the new all-\(m\)
  theorem.
- **Linked log entry:** TASK_LOG.md, diagnostic execution and repository
  verification.

## EV-004 - Proof, Scope, Synchronization, And Final Diff

- **Date:** 2026-07-17
- **Method or command:** three independent read-only proof, diagnostic-code,
  and synchronization/scope audits; complete per-file diff inspection;
  expected-path, sole-diagnostic, PG-tag, stale-claim, UTF-8/BOM, final-newline,
  trailing-whitespace, and cache checks; `git status` and
  `git diff --check`.
- **Relevant output:** all mathematical formulas, equality cases, PG46
  witnesses, circular-distance quantifiers, code paths, and geometric caveats
  pass independent review. One proof audit identified that ownership of the
  shared terminal start was ambiguous; the final proof introduces the
  half-open block \(H_j\), after which the audit passed. The scope is exactly
  five synchronized project Markdown files plus four dossier files, with one
  diagnostic, unique PG50--PG63 tags, valid UTF-8/no BOM, final newlines, no
  trailing whitespace, no generated cache, and a clean whitespace diff.
- **Interpretation:** The exact theorem, diagnostic, durable state, and
  repository scope agree and are ready for user review.
- **Limitations:** Inspection cannot replace user review.
- **Linked log entry:** TASK_LOG.md, independent audits and final handoff.

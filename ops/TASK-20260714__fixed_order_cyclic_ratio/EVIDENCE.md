# EVIDENCE - TASK-20260714__fixed_order_cyclic_ratio / Fixed-Order Cyclic Ratio

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / computation / review | Clean startup, proof-source inspection, and exact prototype | authoritative sources and read-only Python probes | PASS |
| EV-002 | proof / code / test | Exact theorem, scorer, and independent simple-cycle oracle | proof note, source module, test module | PASS |
| EV-003 | computation / test / lint / review | Bounded experiment and complete local verification | production API, pytest, Ruff, artifact verifier, independent audits | PASS with recorded pre-existing global lint findings |
| EV-004 | review / hygiene | Final changed-path, text, temporary-path, and diff audit | complete worktree diff and intended files | PASS |

## EV-001 - Startup And Prototype

- **Date:** 2026-07-14
- **Method or command:** Read all mandatory startup files, relevant prior task
  memory, the complete fixed-order STN and all-`n` bound notes, current exact
  surrogate/order-enumeration source and tests, and read-only Git status. Ran
  in-memory Python probes for the proposed compression/dynamic program and an
  independently written direct simple-cycle oracle.
- **Relevant output:** Git reported `main...origin/main` with no changed paths.
  Production-algorithm prototype and oracle agreed for every canonical full
  order at `n=3,4,5,6`. Exhaustive prototype enumeration returned
  `(12,26,47,77,118,172)` for `n=3..8`, over canonical order counts
  `(1,3,12,60,360,2520)`.
- **Interpretation:** The requested prediction is reproduced exactly at the
  exploratory stage; no counterexample was found. The scorer design has an
  independent small-instance check before repository implementation.
- **Limitations:** These were exploratory in-memory probes, not the final
  checked implementation. Finite enumeration does not prove an all-`n`
  formula or asymptotic behavior.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---startup-scope-and-prototype`

## EV-002 - Proof, Implementation, And Independent Oracle

- **Date:** 2026-07-14
- **Method:** Derived the exact cycle weight from the accepted fixed-order STN
  signs; defined edge-occurrence multiplicities, `q`, `S`, and `Lambda`;
  applied both strict angular comparisons; implemented descending-path
  closure, the one-wrap macro graph, and Karp's formula; wrote a separate
  subset/permutation simple-cycle oracle in the tests.
- **Relevant result:** Every closed walk has positive `q`; decomposition
  reduces its ratio to a weighted average of simple-cycle ratios. Both
  fixed-order and global sandwiches are strict on `n>=3`. Production code uses
  no cycle enumeration. The oracle includes two-cycles and counts both directed
  occurrences of their unordered pair.
- **Classification:** The real-arithmetic statements are EXACT THEOREMS. Code
  behavior and oracle agreement are VERIFIED FACTS. No interval premise is
  used by the scorer.
- **Independent review:** mathematical and algorithm audits recovered the same
  definitions, signs, strictness, global inequalities, compression, Karp
  recurrence, and domain. A later implementation review found no actionable
  defect and matched Karp to direct cycle means on 1,200 random complete
  matrices and all 870 full permutations through `n=6`.
- **Limitations:** A maximizing product-ratio cycle need not be critical for
  the exact angular STN. The scorer proves no exact geometric threshold.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-14---proof-scorer-oracle-and-authoritative-sources`

## EV-003 - Bounded Experiment And Local Verification

- **Date:** 2026-07-14
- **Environment:** local Windows host, Python 3.14.3.
- **Production experiment:** exact enumeration returned rows
  `(n, canonical_count, Lambda_n, minimizer_count, representative)`:
  `(3,1,12,1,(3,1,2))`, `(4,3,26,3,(4,1,2,3))`,
  `(5,12,47,4,(5,1,2,4,3))`, `(6,60,77,15,(6,1,2,3,5,4))`,
  `(7,360,118,24,(7,1,2,3,5,6,4))`, and
  `(8,2520,172,84,(8,1,2,3,5,6,7,4))`; total 2,956 orders.
- **Tests:** the final focused module has 21 passing tests; the integrated
  cycle-ratio/product-distance/search/lower-bound/zigzag selection has 82
  passing tests; the complete suite has `194 passed in 45.70s`.
- **Independent exact checks:** the test oracle agrees on all 76 canonical
  orders through `n=6`. A separate audit compared production Karp against an
  independently implemented exact ratio iteration on all 2,956 bounded
  canonical orders, checked 46,230 rotations/reflections, and found no
  discrepancy.
- **Other checks:** Python compilation passes; Ruff passes on the two new
  Python files; checked-artifact verification accepts 4 certificates, 76 local
  brackets, and the `n=3..6` summary; all 4 schema tests pass.
- **Global lint finding retained:** `python -m ruff check .` was executed and
  reports four pre-existing F401/F841 findings in untouched
  `critical_structure.py`, `fixed_order_artifact.py`, and
  `tests/test_finite_results.py`. They were not changed or suppressed.
- **Failed check preserved:** the first integrated run reported one setup error
  after the sandbox denied `C:\tmp` to a `tmp_path` fixture. No test body
  failed. The workspace-local basetemp rerun passed all 82 tests.
- **Interpretation:** The exact bounded prediction is reproduced and all
  task-scoped implementation checks pass. Existing checked artifacts remain
  unchanged and valid under their prior trust contract.
- **Limitations:** hosted Python 3.11-3.13 CI was not run; finite computation is
  not an all-`n` theorem.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-14---bounded-experiment-and-local-verification`

## EV-004 - Final Hygiene And Diff Review

- **Date:** 2026-07-14
- **Method:** Inspected every intended path and the complete worktree diff;
  scanned task text files with strict UTF-8 decoding; checked forbidden control
  characters, lone carriage returns, trailing whitespace, final newlines,
  display-math balance, uniqueness of `CR` equation tags, temporary-path
  cleanup, and Git diff whitespace.
- **Relevant output:** All task-scoped hygiene checks pass. Git status contains
  only the intended authoritative documentation, proof note, source module,
  test module, current status, and task dossier. No interval, certificate,
  artifact, schema, example, CLI, or temporary path changed.
- **Failed checks preserved:** an initial text-hygiene probe incorrectly
  treated existing valid CRLF line endings as forbidden carriage returns. A
  later naive delimiter count mistook the LaTeX row break `\\[2mm]` for a
  Markdown display-math opener. The corrected probe normalizes CRLF, rejects
  only lone carriage returns, and counts only standalone display delimiters;
  it passes all task text paths.
- **Interpretation:** The final diff is scoped, internally consistent, and
  ready for manual review.
- **Limitations:** local hygiene does not establish hosted CI status or remove
  unrelated committed lint findings.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-14---final-hygiene-and-handoff`

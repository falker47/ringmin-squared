# EVIDENCE - TASK-20260715__lambda10_label3_insertion_gap_classification / Lambda_10 Label-Three Insertion-Gap Classification

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git inspection / exact probe | Clean startup and partial-score reduction | authoritative files and exact integer arithmetic | PASS |
| EV-002 | exact proof | Fourteen insertion gaps and shortcut certificates | proof note | PASS |
| EV-003 | exact computation / test | Independent 14-by-255 subset oracle | focused test module | PASS |
| EV-004 | verification / audit | Full suite and artifact regressions | repository checks | PASS |
| EV-005 | hygiene | Final diff, whitespace, scope, and temp paths | Git/worktree | PASS |

## EV-001 - Startup And Reduction

- **Date:** 2026-07-15
- **Method or command:** Read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the two prior `n=10`
  dossiers, the cyclic-ratio proof and tests, roadmap, and templates; ran
  read-only Git inspection and exact integer-only exploratory probes.
- **Relevant output:** Git reports clean `main...origin/main` at
  `db881793a438`. The current question has exactly 14 insertion trials and
  `2^8-1=255` nonempty induced subsets per resulting order.
- **Interpretation:** A structural proof plus independent test-local
  arithmetic can complete the task without placing label `2` or changing
  production.
- **Limitations:** Exploratory arithmetic is design evidence, not the recorded
  proof or regression.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---startup-and-partial-score-reduction`.

## EV-002 - Structural Gap Classification

- **Date:** 2026-07-15
- **Method:** Defined \(K_{\ge3}\) on labels `3..10`, used
  \(\Delta_3(a,b)=3(a+b)-ab\), related every old shortcut gain before and
  after splitting one edge, bounded all shortcuts with endpoint `3`, audited
  the one-internal-label gains, and bounded every longer base arc.
- **Relevant output:** The first cycle has exact scores 326 on `{4,7}` and
  323 elsewhere. The second has 326 on `{4,9}`, 328 on `{4,7}`, and
  323 elsewhere. The proof records every positive and zero nontrivial gain and
  every argmax subset.
- **Independent review:** a separate mathematical audit reconstructed every
  insertion correction, full sum, one-internal and long-arc bound, positive
  and zero gain, skipped-label annotation, upper witness, argmax uniqueness
  condition, and scope statement.
- **Classification:** EXACT THEOREM (FINITE LABEL-THREE INSERTION-GAP
  CLASSIFICATION).
- **Limitations:** \(K_{\ge3}=323\) is necessary but not sufficient for a
  later full-core extension. Label `2` remains unplaced.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---structural-gap-classification`.

## EV-003 - Independent Test-Only Checks

- **Date:** 2026-07-15
- **Environment:** Windows, Python 3.14.3; exact integer arithmetic only in
  the new paths.
- **Oracle design:** One structural test reconstructs all 48 nontrivial
  oriented shortcuts per insertion without enumerating label subsets. A
  separate literal oracle splices label `3` into all 14 labelled gaps and
  scores all 255 nonempty induced subsets of every resulting order without
  using the insertion formula or shortcut certificate.
- **Relevant output:** The tests cover 14 distinct orders and 3,570 literal
  subset evaluations, recover the three and only three excluded rows, give
  323 on every other row, and record every exact argmax.
- **Commands and output:** focused `-k label_three` reports
  `2 passed, 31 deselected in 0.17s`; the complete cyclic-ratio module reports
  `33 passed in 16.63s`.
- **Independent review:** a separate test audit reproduced all rows and
  argmaxes with a bitmask oracle, checked exact coverage, certificate/oracle
  separation, absence of new production dependencies, and Python 3.11 API
  compatibility.
- **Classification:** VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION).
- **Limitations:** The finite oracle audits the theorem; it is not the source
  of the proof or a public `n=10` enumeration.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---independent-test-only-checks`.

## EV-004 - Complete Verification

- **Date:** 2026-07-15
- **Environment:** Windows, Python 3.14.3. Python 3.11 compatibility was
  audited statically; hosted GitHub Actions was not run or inspected.
- **Commands and relevant output:**
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_fixed_order_cycle_ratio.py -k label_three --basetemp C:\tmp\ringmin_squared_label3_focused`
    -> `2 passed, 31 deselected in 0.17s`.
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_fixed_order_cycle_ratio.py --basetemp C:\tmp\ringmin_squared_label3_module`
    -> `33 passed in 16.63s`.
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider --basetemp C:\tmp\ringmin_squared_label3_full`
    under the initial sandbox restriction -> `178 passed, 31 errors`; every
    error was `PermissionError` while creating the requested pytest base
    directory, before the affected test bodies ran.
  - The same full-suite command rerun with the temporary-directory permission
    restriction removed -> `209 passed in 76.87s`.
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_checked_artifact_schema_validation.py --basetemp .tmp_pytest_label3_schema`
    -> `4 passed in 0.97s`.
  - `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
    -> accepted 4 certificates, 76 local brackets, and the checked summary.
  - `$env:PYTHONPATH='src'; python -m ruff check tests/test_fixed_order_cycle_ratio.py`
    -> `All checks passed!`.
  - `python -m compileall -q tests/test_fixed_order_cycle_ratio.py`
    -> exit code 0 with no output.
- **Independent audits:** mathematical, test, and proof-note scope audits
  found no remaining correctness, coverage, independence, compatibility, or
  classification defect.
- **Interpretation:** The successful rerun and the remaining checks verify the
  implementation and documentation. The failed first run is retained as
  environmental evidence rather than hidden.
- **Limitations:** Local success does not establish hosted CI status.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---complete-verification`.

## EV-005 - Final Diff And Hygiene

- **Date:** 2026-07-15
- **Method or command:** Inspected `git status --short`, the complete per-file
  diff, diff statistics, and every new dossier file; ran `git diff --check`, a
  trailing-whitespace scan over all changed paths, `git diff --name-only --
  src`, `git diff --cached --name-only`, a production-boundary source check,
  and workspace/`C:\tmp` task-directory searches.
- **Relevant output:** Diff and whitespace checks are empty; the `src/` diff,
  staged path list, and task-temp searches are empty; production still records
  the hard `n<=8` boundary; status contains only the six intended tracked
  files and the three-file task dossier. The staged-state command emitted a
  non-fatal sandbox warning while reading the user's global Git ignore, but
  exited zero and reported no staged path.
- **Failed setup evidence:** an initial bundled parallel hygiene invocation
  failed before any check ran because the sandbox setup helper exited nonzero.
  The same checks were then run individually and produced the results above.
- **Independent review:** the final documentation audit found one missing
  command transcription in EV-004; it was corrected before the final rerun of
  hygiene checks. No other scope, classification, count, argmax, evidence, or
  roadmap defect was found.
- **Interpretation:** Durable memory, proof, tests, and worktree scope are
  internally consistent and ready for user review and a manual commit
  decision.
- **Limitations:** Read-only local diff inspection does not establish hosted
  CI status or perform a Git commit.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---final-hygiene-and-handoff`.

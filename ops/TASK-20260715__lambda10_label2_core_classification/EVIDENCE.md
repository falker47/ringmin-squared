# EVIDENCE - TASK-20260715__lambda10_label2_core_classification / Lambda_10 Label-Two And Core Classification

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git inspection / exact probe | Clean startup and 88-case reduction | authoritative files and exact arithmetic | PASS |
| EV-002 | exact proof | Label-two, argmax, dihedral, and count classification | proof note | PASS |
| EV-003 | exact computation / test | Independent 88-by-511 subset oracle | focused test module | PASS |
| EV-004 | verification / audit | Full suite and artifact regressions | repository checks | PASS |
| EV-005 | hygiene | Final diff, whitespace, scope, and temp paths | Git/worktree | PASS |

## EV-001 - Startup And Reduction

- **Date:** 2026-07-15
- **Method or command:** Read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, all accepted `n=10` dossiers,
  the proof note, production scorer, focused tests, roadmap, and templates;
  ran read-only Git inspection and three independent exact analyses.
- **Relevant output:** Git reported a clean `main...origin/main` worktree.
  The accepted label-three theorem leaves eleven cycles and exactly
  `11*8=88` labelled insertions for label `2`.
- **Interpretation:** The task can be completed without a production change
  or public-domain extension.
- **Limitations:** Startup arithmetic scopes the task; it is not the final
  proof or regression.
- **Linked log entry:** `TASK_LOG.md#2026-07-15---startup-and-reduction`.

## EV-002 - Structural Classification And Counts

- **Date:** 2026-07-15
- **Method:** For a subset containing label `2`, delete it and apply the exact
  variation `2(a+b)-ab=4-(a-2)(b-2)`. Use the recorded nonnegative shortcut
  gains to compute the exact maximum constrained to retain label `3`; inspect
  all eight variations only in the sole parent attaining 323 under that
  constraint. Resolve equivalences by deleting the inserted label and using
  the trivial label-preserving dihedral stabilizer of a distinctly labelled
  cycle.
- **Relevant output:** Ten parents have constrained maximum at most 320. In
  `(10,3,4,7,8,6,9,5)`, the full partial set has score 323 and every proper
  subset retaining `3` has score at most 318. Splitting `{3,4}` gives the sole
  score 325; all other insertions inherit score 323 and their parent argmaxes.
  The 88 candidate cores are distinct; exactly 87 minimize. Only afterward,
  nine label-one gaps per core give `87*9=783` complete classes.
- **Independent review:** three separate analyses reconstructed the 87/1
  result, every argmax, the dihedral proof, and the complete-class count.
- **Classification:** EXACT THEOREM (FINITE `n=10` CORE AND COMPLETE
  MINIMIZER CLASSIFICATION).
- **Limitations:** No exact `R_2^*(10)`, geometric minimizer, all-`n`, or
  asymptotic conclusion follows. The exception is unique only in the forced
  88-candidate family.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---structural-classification-and-counts`.

## EV-003 - Independent Test-Only Oracle

- **Date:** 2026-07-15
- **Environment:** Windows; exact integer arithmetic only in the new path.
- **Oracle design:** Construct the two fixed seven-label parents locally,
  splice label `3` in their admissible gaps, splice label `2` in all eight
  gaps of each survivor, and literally score every nonempty position subset.
  Root each distinctly labelled cycle at its unique maximum and compare its
  two orientations to obtain a test-local dihedral key.
- **Relevant output:** `88*(2^9-1)=44,968` subset evaluations; score
  distribution `{323: 87, 325: 1}`; seven rows with two argmaxes, 81 with one;
  88 distinct core keys and 783 distinct minimizing complete keys.
- **Commands and output:** focused and module commands passed during
  implementation; final command transcripts are recorded in EV-004.
- **Classification:** VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION).
- **Limitations:** The oracle audits but does not prove the theorem. It calls
  no production scorer, enumerator, or canonicalizer.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---independent-test-only-oracle`.

## EV-004 - Repository Verification And Audits

- **Date:** 2026-07-15
- **Environment:** Windows, Python 3.14.3. Hosted Ubuntu/Python 3.11--3.13 was
  not available in this worktree.
- **Commands:**
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_fixed_order_cycle_ratio.py -k label_two --basetemp C:\tmp\ringmin_squared_label2_focused`
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_fixed_order_cycle_ratio.py --basetemp C:\tmp\ringmin_squared_label2_module`
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider --basetemp C:\tmp\ringmin_squared_label2_full`
  - `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests/test_checked_artifact_schema_validation.py --basetemp C:\tmp\ringmin_squared_label2_schema`
  - `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
  - `$env:PYTHONPATH='src'; python -m ruff check tests/test_fixed_order_cycle_ratio.py`
  - `python -m compileall -q tests/test_fixed_order_cycle_ratio.py`
- **Relevant output:** focused `1 passed, 33 deselected in 0.24s`; module
  `34 passed in 16.39s`; unrestricted full suite `210 passed in 67.04s`;
  schema `4 passed in 0.87s`; semantic verifier `certificates=4`,
  `local_brackets=76`; Ruff reported `All checks passed!`; compilation was
  silent and successful.
- **Failed check retained:** the first sandboxed full-suite attempt reported
  `1 failed, 178 passed, 31 errors in 66.10s`. All 31 setup errors were denied
  temporary-path access and the one assertion was a hidden-Git-provenance
  mismatch. The required unrestricted rerun of the identical suite passed all
  210 tests.
- **Independent audits:** separate mathematical, test-independence/scope, and
  documentation audits all returned PASS. The test audit additionally parsed
  the changed module with the Python 3.11 grammar; an actual Python 3.11
  runtime was unavailable locally.
- **Interpretation:** All locally available implementation and repository
  regressions pass; the failed first run is classified as an environmental
  sandbox event, not suppressed evidence.
- **Limitations:** Hosted GitHub Actions and its Python 3.11--3.13 matrix have
  not been run or inspected for this worktree.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---complete-repository-verification`.

## EV-005 - Final Diff And Scope Hygiene

- **Date:** 2026-07-15
- **Commands:** `git status --short`, `git diff --stat`,
  `git diff --numstat`, `git diff --check`,
  `git diff --name-only -- src`, `git diff --cached --name-only`, a trailing
  whitespace search over the new dossier, and an exact task-temporary-path
  inspection.
- **Relevant output:** `git diff --check` was silent; `src/` and cached diff
  lists were empty; the dossier whitespace search found no match. Status lists
  only the six intended tracked files plus the new STRICT dossier. The exact
  `C:\tmp\ringmin_squared_label2_full` pytest directory was removed after
  its path was resolved and verified.
- **Scope result:** no production source, public API, enumerator,
  canonicalizer, schema, artifact, example, or public `n<=8` limit changed.
- **Interpretation:** The worktree contains one coherent uncommitted task and
  is ready for manual review.
- **Limitations:** GitHub Actions remains uninspected; the user must review and
  decide whether to commit.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-15---final-hygiene-and-handoff`.

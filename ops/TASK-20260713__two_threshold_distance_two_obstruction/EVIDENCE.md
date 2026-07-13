# EVIDENCE - TASK-20260713__two_threshold_distance_two_obstruction / Two-Threshold Distance-Two Obstruction

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / derivation | Startup and symbolic proof | project memory, primary proof, relevant source/tests | PASS |
| EV-002 | file / command / test | Exact finite support and focused verification | product-distance source/tests | PASS |
| EV-003 | command / review | Integrated and full verification | pytest, formula audit, artifact verifier, proof review | PASS |
| EV-004 | command / review | Final scope and diff inspection | intended paths and Git diff | PASS after checker correction |

## EV-001 - Startup And Symbolic Proof

- **Date:** 2026-07-13
- **Method or command:** Read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, relevant prior dossiers,
  `research/PRODUCT_DISTANCE_SURROGATE.md`, source/tests, and roadmap; ran
  `git status --short --branch`; derived the cyclic gap and marked-word count,
  then checked strict equality and cardinalities zero and one separately.
- **Relevant output:** Initial tree clean. For `u>=2`, every induced `U_T`
  gap costs at least two positions and every `V_T-V_T` gap costs at least
  three. A cyclic word with `u` positions and `v` marked has exactly minimum
  `max(0,2v-u)` marked-marked adjacencies. If `u=1`, exact threshold intervals
  force `v=0` for `n>=3`.
- **Interpretation:** The candidate lemma is an exact all-`n` theorem with no
  exceptional `u=2` failure and no reliance on finite computation.
- **Limitations:** The lemma is necessary only; it does not construct an order
  or determine exact `B_n`.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---startup-and-exact-derivation`

## EV-002 - Exact Support And Focused Verification

- **Date:** 2026-07-13
- **Method or command:** Edited with `apply_patch`; ran
  `python -m py_compile src\power_ringmin\product_distance.py tests\test_product_distance.py`;
  ran `python -m pytest -p no:cacheprovider tests\test_product_distance.py -q`.
- **Relevant output:** Compilation passed; pytest reported `18 passed`. The
  exact finite values are
  `(6,12,12,20,21,30,30,42,45)` for `n=3..11`; every value passes the packing
  inequality while the preceding half-integer is excluded, and every value is
  at most the existing exact `B_n` row.
- **Interpretation:** Strict floors, event-set inversion, empty/singleton
  tails, and the bounded comparison are implemented exactly with integers and
  `Fraction`.
- **Limitations:** The bounded table does not prove the all-`n` quadratic
  inequality; that conclusion is the symbolic proof in the research note.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---exact-support-and-focused-tests`

## EV-003 - Integrated And Full Verification

- **Date:** 2026-07-13
- **Method or command:** Ran integrated pytest over product-distance, zigzag,
  induced-subset, and insertion tests; evaluated exact threshold, predecessor,
  capacity, and squared-radical inequalities for `n=9..1000`; ran
  `python -m pytest -p no:cacheprovider`; ran
  `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`;
  reviewed the self-contained proof and all exact domains.
- **Relevant output:** Integrated tests passed `33/33`; `992` exact formula
  diagnostics passed; full pytest passed `146/146`; checked-artifact
  verification accepted 4 certificates, 76 local brackets, and the `n=3..6`
  summary.
- **Interpretation:** Symbolic proof, exact implementation, bounded regression,
  repository integration, and existing checked artifacts are consistent.
- **Limitations:** The 992-case diagnostic is formula evaluation, not cyclic
  order enumeration and not a replacement for the all-`n` proof. Local Python
  is the repository's current runtime; hosted CI for current `HEAD` was not
  inspected.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---integrated-and-full-verification`

## EV-004 - Final Scope And Diff Inspection

- **Date:** 2026-07-13
- **Method or command:** Compared exact expected and observed Git paths;
  strictly decoded all changed files as UTF-8; scanned trailing whitespace;
  checked equation-tag uniqueness; inspected source/test, proof, memory, and
  dossier diffs; ran `git diff --check` and final `git status`.
- **Relevant output:** Exact scope contains 10 intended paths; strict UTF-8
  failures are zero; corrected trailing-whitespace count is zero; all 51
  equation tags are unique; `git diff --check` produced no output. The first
  whitespace scan used an incorrectly escaped PowerShell line split and
  reported 172 false positives; rerunning with the literal regex `\r?\n`
  corrected the checker input.
- **Interpretation:** The final change set is limited to exact source/tests,
  the primary proof, essential project memory/roadmap, and one STRICT dossier,
  with no artifact, CLI, schema, certificate, or infrastructure addition.
- **Limitations:** Git warnings about the inaccessible user-global ignore file
  are environmental and do not affect repository status or diff content.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---final-hygiene-and-handoff`

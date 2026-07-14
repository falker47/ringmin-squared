# EVIDENCE - TASK-20260714__terminal_high_incidence / Terminal-High Incidence Obstruction

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / derivation / computation | Startup, independent derivation, and exact probe | project memory, predecessor dossiers, proof/source/tests, three read-only audits | PASS |
| EV-002 | file / command / test | Exact support and independent focused verification | product-distance source/tests | PASS after verifier-range correction |
| EV-003 | proof / computation / memory | Proof, exact event inversion, and asymptotic diagnostics | proof note, exact source, project memory | PASS |
| EV-004 | command / test / independent review | Integrated, full, artifact, and review verification | full repository and three independent audits | PASS |
| EV-005 | source / proof / repository hygiene | Final scope, proof, and diff inspection | exact 10-path worktree diff | PASS |

## EV-001 - Startup, Independent Derivation, And Exact Probe

- **Date:** 2026-07-14
- **Method or command:** Read all required startup state and relevant predecessor task memory; inspected `research/PRODUCT_DISTANCE_SURROGATE.md`, `src/power_ringmin/product_distance.py`, and `tests/test_product_distance.py`; ran `git status --short --branch`; obtained three independent read-only derivations; evaluated the proposed joint event set with exact `Fraction` arithmetic.
- **Relevant output:** Initial tree clean. All derivations prove the same incidence injection and event set. Exact probing gives `(6,12,15,20,21,30,36,45,50)` for `H_3,...,H_11`, and the symbolic lower/upper arguments both yield coefficient `8/25`.
- **Interpretation:** The proposed theorem, finite inversion, and asymptotic target have independent pre-implementation support.
- **Limitations:** The probe and bounded checks do not replace the all-`n` proof or establish an exact formula or limit for `B_n`.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---startup-and-independent-derivation`

## EV-002 - Exact Support And Independent Focused Verification

- **Date:** 2026-07-14
- **Method or command:** Edited with `apply_patch`; ran `python -m py_compile src\power_ringmin\product_distance.py tests\test_product_distance.py`; ran `python -m pytest -p no:cacheprovider tests\test_product_distance.py -q` twice, before and after correcting the intended independent-verifier range.
- **Relevant output:** The first run reported `1 failed, 23 passed`: all visited incidence assertions passed, but the hard expected count was 34,160 while the scan ending at `n(n-1)` visited 10,520 states. Changing only the independent scan endpoint to `n(n+1)` included the intended empty-tail states; the second run reported `24 passed`. The verifier covers all 872 permutations for `n=3..7`, 34,160 qualifying half-integer states, and a separate `n=11,T=50` case with two terminal highs and four distinct lows.
- **Interpretation:** Exact `Fraction` support, the unchanged `Q_n`, new `H_n`, floors, tail starts, strict and non-strict equalities, empty/singleton tails, independent incidence injection, bounded finite values, and the symbolic upper-witness arithmetic agree.
- **Limitations:** The small-order verifier is finite evidence and does not replace the all-`n` proof. Existing exhaustive core enumeration remains bounded to `n=3..11`.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---exact-support-and-independent-focused-verification`

## EV-003 - Proof, Event Inversion, And Asymptotic Diagnostics

- **Date:** 2026-07-14
- **Method or command:** Inspected the proof line by line against the exact `Fraction` implementation; evaluated `H_n` on its finite event set for `n=3..1000`; checked the explicit upper witness `d_n=ceil((4*n+8)/5)`, `T_n^*=d_n(d_n-1)/2` for `n=11..1000`; aligned `research/PRODUCT_DISTANCE_SURROGATE.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `research/NEXT_RESEARCH_STEPS.md`, and `CURRENT_STATUS.md`.
- **Relevant output:** `H_3,...,H_11=(6,12,15,20,21,30,36,45,50)`; 998 exact formula checks and 990 upper-witness checks pass. The lower estimate is `T>(8/25)n^2+(2/5)n`; the witness is below `(8/25)n^2+(42/25)n+52/25`.
- **Interpretation:** The finite event inversion is exact and the matching bounds prove `H_n=(8/25)n^2+O(n)`. The value `8/25` was verified rather than assumed.
- **Limitations:** The diagnostics above `n=11` evaluate formulas only and do not enumerate cyclic orders. The conclusion for `B_n` is a lower bound, not an exact coefficient or convergence theorem.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---proof-event-inversion-and-durable-memory`

## EV-004 - Integrated, Full, Artifact, And Review Verification

- **Date:** 2026-07-14
- **Method or command:** Ran `python -m pytest -p no:cacheprovider tests\test_product_distance.py tests\test_zigzag_core_upper_bound.py tests\test_induced_subset_lower_bound.py tests\test_radius_one_insertion.py -q`; ran `python -m pytest -p no:cacheprovider`; ran `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`; obtained independent mathematical, implementation, and documentation reviews.
- **Relevant output:** Integrated suite `39 passed`; full suite `152 passed`; semantic verifier accepts 4 certificates, 76 local brackets, and the `n=3..6` summary. Review diagnostics independently match event inversion through at least `n=150` and the all-`n` witness through at least `n=1000`; final reviewers report PASS with no residual finding.
- **Interpretation:** The change is compatible with the existing bounded research pipeline, and the proof/source/tests agree independently.
- **Limitations:** Hosted GitHub Actions for the current `HEAD` was not independently checked. Documentation clarifications were applied after the full suite; they did not alter executable source or tests.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---integrated-verification-and-independent-reviews`

## EV-005 - Final Scope, Proof, And Diff Inspection

- **Date:** 2026-07-14
- **Method or command:** Inspected every changed source, test, proof, memory, status, and dossier file; ran `python -m py_compile src\power_ringmin\product_distance.py tests\test_product_distance.py`; reran `python -m pytest -p no:cacheprovider tests\test_product_distance.py -q`; checked strict UTF-8 and trailing whitespace on all changed paths; checked equation-tag uniqueness and display-delimiter balance; ran `git status --short --untracked-files=all`, `git diff --stat`, and `git diff --check`.
- **Relevant output:** Targeted review of the explicit `a_{T_n^*}<=n` justification PASS; focused tests `24 passed`; exactly 10 intended paths; strict UTF-8 PASS; trailing whitespace PASS; 64 unique equation tags; 143 opening and 143 closing display delimiters; diff check clean.
- **Interpretation:** The final worktree scope is coherent, the proof has no hidden use of a negative tail-cardinality formula, and the task satisfies the repository handoff contract.
- **Limitations:** The worktree is intentionally modified and uncommitted for manual review. Hosted CI remains unchecked.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---final-inspection-and-handoff`

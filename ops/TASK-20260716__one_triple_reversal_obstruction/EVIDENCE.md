# EVIDENCE - TASK-20260716__one_triple_reversal_obstruction / One-Triple Reversal Obstruction

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / proof / review | Startup and exact family obstruction | project memory, prior construction, proof/source/tests, independent audits | PASS |
| EV-002 | exact computation / test | Small reproducible corroboration | dossier diagnostic and focused test | PASS |
| EV-003 | command / review | Complete verification and final hygiene | test suite, artifacts, documents, Git diff | PASS after environment rerun and formatter-scope correction |

## EV-001 - Startup And Exact Family Obstruction

- **Date:** 2026-07-16
- **Method or command:** Read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the prior upper-construction
  dossier, `research/PRODUCT_DISTANCE_SURROGATE.md`, source, and tests; ran
  read-only Git status; obtained independent read-only audits; derived the
  local triple-reversal formulas directly.
- **Relevant output:** Initial tree clean. For `n=10*m+3`, `d=8*m+4`, and
  `0<=s<=m`, the exact maxima are `M_1=T`, piecewise `M_2` as in (PT6),
  `M_3=(5*m+2)*(9*m+5)/3<T`, and
  `M_{>=4}=n(n-1)/4<T`; the three closing maxima are (PT11).
  Hence (PT13) gives `W=T` for `s>=1` and `W=(d^2-1)/2` for `s=0`.
- **Interpretation:** EXACT FAMILY-SPECIFIC OBSTRUCTION: the persistent
  adjacent saturation prevents a strict finite or asymptotic improvement.
- **Limitations:** This theorem concerns one selected perturbation family and
  the surrogate `W`; it is not a classification of all perturbations or an
  obstruction to non-regular geometric constructions.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-16---startup-family-selection-and-exact-derivation`

## EV-002 - Small Reproducible Corroboration

- **Date:** 2026-07-16
- **Method or command:** Ran
  `python ops\TASK-20260716__one_triple_reversal_obstruction\exact_diagnostic.py`
  and
  `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider
  tests\test_product_distance.py -k one_triple_reversal -q`.
- **Relevant output:** The independent diagnostic passes six rows:
  `(m,s)=(3,0),(3,1),(3,3),(4,2),(9,0),(9,9)`. The targeted pytest run
  passes 6/6. At `(3,0)`, it records
  `(M_1,M_2,M_3,M_{>=4})=(378,783/2,544/3,264)` and
  `(C_1,C_2,C_3)=(364,266,338/3)`; at `(9,0)`, it records
  `W=5775/2`, while `(9,9)` has `W=2850`.
- **Interpretation:** The standalone path independently reconstructs the
  family, while the test path compares two independent scorers and production
  scoring. Both corroborate every class used in the proof.
- **Limitations:** finite direct scoring does not prove the all-parameter
  theorem and does not enumerate cyclic orders.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-16---reproducible-exact-controls`.

## EV-003 - Complete Verification And Final Hygiene

- **Date:** 2026-07-16
- **Method or command:** Ran complete product-distance and repository pytest,
  the checked-artifact semantic verifier, schema-selection pytest, Ruff,
  pytest collection counting, equation-tag/display/UTF-8 checks, read-only
  Git status/diff/diff-check, protected-source and changed-path checks, and
  three independent read-only final audits.
- **Relevant output:** Product-distance 49/49; complete suite 283/283 outside
  the sandbox; 4 certificates and 76 local brackets verified; schema 4/4;
  Ruff PASS; 179 unique tags, 309 balanced display pairs, balanced aligned
  environments, strict UTF-8, exact intended path scope, no `src` diff,
  `MAX_ENUMERATION_N=11`, and `git diff --check` PASS.
- **Failed checks retained:** the sandboxed full suite produced 31 setup
  errors because pytest could not access
  `C:\Users\Falker\AppData\Local\Temp\pytest-of-Falker`; no test body
  failed. The outside-sandbox rerun passed all 283 tests. A combined Ruff
  check/format-check command returned exit 1 because the formatter proposed
  reformatting legacy test code. The mechanical formatter was applied, every
  unrelated test hunk was then reverted with `apply_patch`, and the final test
  diff contains only the intended 53-line addition; final Ruff check passes.
- **Interpretation:** Executable behavior, authoritative memory, protected
  scope, and repository hygiene all support `READY_FOR_REVIEW`.
- **Limitations:** hosted CI will not be inferred from local checks.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-16---complete-verification-and-final-handoff`.

# EVIDENCE - TASK-20260714__eight_twenty_fifths_upper_construction / Eight-Twenty-Fifths Upper Construction

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / derivation / computation | Startup, reduction, and candidate family | project memory, predecessor proof/source/tests, independent audits, exact probes | PRELIMINARY PASS |
| EV-002 | proof / source / test | Construction, proof, and implementation | proof note, generator, tests | PASS |
| EV-003 | independent exact computation / review | Falsification and final audits | bounded constraint search, independent formula and proof reviews | PASS |
| EV-004 | command / test | Automated verification | compile, pytest, checked-artifact verifier | PASS after environment rerun |
| EV-005 | documentation / hygiene | Durable memory and final diff audit | project memory, task status, Git diff checks | PASS |

## EV-001 - Startup, Reduction, And Candidate Family

- **Date:** 2026-07-14
- **Method or command:** Inspected all required startup files and relevant
  product-distance/insertion memory, proof, source, and tests; ran read-only
  Git status; commissioned three independent read-only audits; ran exact
  integer diagnostics for candidate cyclic orders without extending canonical
  factorial enumeration beyond `n=11`.
- **Relevant output:** Initial worktree clean. The implication chain is
  `H_n<=B_n<=W_n<=T_n`. The preliminary symbolic parameter range, later
  identified exactly as `v>=e-2`, includes every `n>=33`, and exact
  local-distance diagnostics passed through `n=5000`. Independent exact
  constraint search finds witnesses through at least `n=48`.
- **Interpretation:** There is strong independent support for a valid upper
  construction, but the all-`n` result remains pending the written proof,
  exceptional witness audit, and repository tests.
- **Limitations:** These finite diagnostics do not prove the symbolic family
  or any asymptotic result; no canonical factorial enumeration was performed
  beyond `n=11`.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---startup-reduction-and-candidate-construction`

## EV-002 - Construction, Proof, And Implementation

- **Date:** 2026-07-14
- **Method or command:** Added
  `eight_twenty_fifths_threshold(n)` and `eight_twenty_fifths_order(n)` to
  `src/power_ringmin/product_distance.py`; added independent exact scoring and
  closing checks to `tests/test_product_distance.py`; recorded the all-`n`
  proof in `research/PRODUCT_DISTANCE_SURROGATE.md`.
- **Relevant output:** The generator partitions `{2,...,n}` exactly and uses
  no search. For `v=n-d+1` and `e=d-4v`, its symbolic domain is
  `v>=e-2`, covering every `n>=33` plus ten earlier values. Fourteen displayed
  initial orders cover the complement in `n>=9`. The proof checks distance
  classes one, two, three, closing, and at least four separately.
- **Interpretation:** EXACT THEOREM: every `n>=9` has an explicit cyclic core
  order `sigma_n` with `W(sigma_n)<=T_n`. The resulting squeeze proves exact
  leading coefficients for `B_n` and `W_n`, and insertion gives the geometric
  limsup upper coefficient `8/(25*pi)`.
- **Limitations:** The construction does not prove exact finite optima,
  second-order terms, or a matching geometric lower coefficient.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-14---exact-construction-proof-and-implementation`

## EV-003 - Independent Falsification And Audits

- **Date:** 2026-07-14
- **Method or command:** Used an exact non-factorial positional constraint
  model with Boolean position-label assignments and forbidden pairs at
  distances one through three to falsify candidate forms and identify small
  witnesses; independently recomputed every exceptional score and closing
  score; commissioned separate final mathematical and implementation reviews.
- **Relevant output:** Z3 `4.16.0` under Python `3.14.3` found exact witnesses
  for `n=9..48`. No canonical factorial enumeration was extended beyond
  `n=11`. Independent integer checks of the final family covered every
  eligible index through `n=5000`, plus large-index spot checks through at
  least `n=1,000,001`. The final proof audit checked every residue class,
  block partition, distance class, closing case, exception, squeeze, and
  insertion implication; the implementation audit independently reconstructed
  the formula and checked exports and validation. Both audits report PASS with
  no residual finding.
- **Interpretation:** This supplies independent falsification and regression
  evidence for the exact symbolic proof. It does not replace that proof.
- **Limitations:** The bounded constraint search establishes no all-`n`
  statement and the exceptional witnesses are not claimed optimal.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-14---independent-audits-and-automated-verification`

## EV-005 - Durable Memory And Final Diff Audit

- **Date:** 2026-07-14
- **Method or command:** Aligned `start.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, the two research notes, the roadmap, and this dossier;
  inspected the complete source, test, proof, memory, status, and dossier
  changes; ran `python -m ruff check --ignore F841
  src\power_ringmin\product_distance.py tests\test_product_distance.py`;
  ran strict UTF-8, trailing-whitespace, equation-tag, and display-delimiter
  checks; ran `git status --short --untracked-files=all`,
  `git diff --stat`, and `git diff --check`.
- **Relevant output:** Ruff reported `All checks passed!`; all 11 changed
  paths decode as strict UTF-8; no trailing whitespace was found; the proof
  note has 88 unique equation tags and 171 balanced display-math pairs; the
  changed-path scope is exactly the 11 intended files; complete diff
  inspection found no residual issue; `git diff --check` produced no output.
- **Interpretation:** Durable memory and the final worktree consistently state
  the exact theorem, its verification basis, and its limitations. The task is
  ready for user review.
- **Limitations:** The worktree has not been staged, committed, pushed, or
  checked on hosted CI; those actions remain outside Codex authority.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-14---final-handoff`

## EV-004 - Automated Verification

- **Date:** 2026-07-14
- **Method or command:** Ran:
  `python -m py_compile src\power_ringmin\product_distance.py tests\test_product_distance.py`;
  `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests\test_product_distance.py -q`;
  `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider tests\test_product_distance.py tests\test_zigzag_core_upper_bound.py tests\test_induced_subset_lower_bound.py tests\test_radius_one_insertion.py -q`;
  `$env:PYTHONPATH='src'; python -m pytest -p no:cacheprovider -q`;
  `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`.
- **Relevant output:** Compilation passed. Focused tests passed `27/27`;
  integrated tests passed `42/42`; the complete suite passed `155/155` outside
  the filesystem sandbox. The semantic verifier reported
  `certificates=4 local_brackets=76 summary_n_values=3,4,5,6`.
- **Failed checks retained:** The first sandboxed full-suite run failed with
  31 setup errors because pytest could not access
  `C:\Users\Falker\AppData\Local\Temp\pytest-of-Falker`. A second sandboxed
  run with `--basetemp C:\tmp\power-ringmin-pytest-eight-twenty-fifths`
  failed for the same permission reason at `C:\tmp`. The identical suite then
  passed outside the filesystem sandbox. No test body failed in either
  sandboxed attempt.
- **Interpretation:** All code and artifact checks pass. The two failed runs
  isolate a sandbox temporary-directory restriction and are not evidence of a
  product defect.
- **Limitations:** Hosted GitHub Actions for the current worktree was not
  inspected.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-14---independent-audits-and-automated-verification`

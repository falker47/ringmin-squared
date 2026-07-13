# EVIDENCE - TASK-20260713__distance_two_adjacent_strictness / Distance-Two Adjacent Strictness

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / derivation | Startup and all-n parity/incidence derivation | project memory, prior dossiers, relevant source and research note | PASS |
| EV-002 | file / test | Structural implementation and focused verification | source, focused tests | PASS after correction |
| EV-003 | derivation / command / test | All-n proof record and full verification | research/memory, exact probes, pytest, artifact verifier | PASS |
| EV-004 | command / review | Final scope, encoding, whitespace, and diff review | 10 intended paths and Git diff | PASS |

## EV-001 - Startup And All-n Derivation

- **Date:** 2026-07-13
- **Method or command:** Read the required startup files, preceding adjacent/full-surrogate dossiers, relevant code/tests/research, and `git status --short --branch`; derive forced high-high equality edges, alternating active high paths, the terminal-high incidence count, and the exceptional `n=12` degree obstruction.
- **Relevant output:** Initial tree clean. Even equality cycles have only `{t+1,t+2}` high-high; odd equality cycles have only `{t+1,t+2}` and `{t+1,t+3}`. For the terminal block starting at the least `r` with `r(r+1)>2A_n`, the required `2|V|` distinct compatible lows exceed the available count except at `n=12`; there, the degree budget of `{7,8,9}` is exhausted by vertex `12` and low `6`.
- **Interpretation:** This is an exact all-`n` proof route, independent of cyclic-order enumeration beyond the permitted `n=3..11` regression.
- **Limitations:** The theorem decides strictness of the distance-two relaxation but gives no closed formula for `B_n` or `W_n`.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---startup-and-exact-derivation`

## EV-002 - Structural Implementation And Focused Verification

- **Date:** 2026-07-13
- **Method or command:** Edit with `apply_patch`; `python -m py_compile src\power_ringmin\product_distance.py tests\test_product_distance.py`; `python -m pytest -p no:cacheprovider tests\test_product_distance.py -q`; integrated focused pytest over product-distance, zigzag, induced-subset, and insertion tests.
- **Relevant output:** Python compilation passed. The first focused run failed because the even path extractor rejected its legitimate final blocked-neighbor endpoint. After the interior-only correction, product-distance tests passed `16/16`; integrated focused tests passed `31/31`.
- **Interpretation:** Exact source support now implements the parity classification independently of the adjacent scorer and agrees with every bounded canonical equality case through `n=11`.
- **Limitations:** The classifier regression is finite and bounded. The all-`n` theorem is the symbolic proof in the research note; no order enumeration beyond `n=11` was performed.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---structural-implementation-and-focused-verification`

## EV-003 - All-n Proof Record And Full Verification

- **Date:** 2026-07-13
- **Method or command:** Direct `patterns.interleave` structural checks for `n=4..1000`; exact parameter-only incidence checks for `n=9..200000` excluding the separately proved `n=12`; equation-tag inspection; `python -m pytest -p no:cacheprovider`; `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`.
- **Relevant output:** `interleave_structures=997`; `incidence_parameter_checks 199991`; boundary polynomials passed; full pytest reported `144 passed in 34.68s`; artifact verification accepted 4 certificates, 76 local brackets, and the `n=3..6` summary.
- **Interpretation:** The exact proof, implementation, tests, and existing checked artifacts are mutually consistent. The former `n=12..32` strictness gap is resolved without extending cyclic-order enumeration.
- **Limitations:** The large parameter check is diagnostic formula evaluation, not a substitute for the all-`n` inequalities. No formula for `B_n` or `W_n`, no beyond-`n=11` equality `B_n=W_n`, and no geometric optimum claim follows.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---all-n-proof-record-and-full-verification`

## EV-004 - Final Scope, Encoding, Whitespace, And Diff Review

- **Date:** 2026-07-13
- **Method or command:** Exact expected/observed path comparison from `git status --short --untracked-files=all`; strict .NET UTF-8 decoding; trailing-whitespace scan; equation-tag extraction/uniqueness check; complete tracked and untracked diff inspection; `git diff --check`.
- **Relevant output:** The first whitespace checker used an incorrectly escaped PowerShell line-split expression and reported 126 false positives. The corrected checker reported `scope_paths=10 utf8_bad=0 trailing_whitespace=0 equation_tags=32 duplicate_tags=0`; final `git diff --check` produced no output.
- **Interpretation:** The change set is confined to exact source/tests, research/project memory, and one task dossier, with clean text hygiene and no unintended file class.
- **Limitations:** Git warnings about the inaccessible user-global ignore file are environmental and do not affect repository status or diff content.
- **Linked log entry:** `TASK_LOG.md#2026-07-13---final-hygiene-and-handoff`

# EVIDENCE - TASK-20260713__adjacent_product_distance_relaxation / Adjacent Product-Distance Relaxation

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / derivation / computation | Startup, symbolic adjacent proof, tail comparison | project memory, prior dossier, source, exact formulas | PASS |
| EV-002 | computation / file / test | Truncated tables, implementation, focused tests | source, tests, exact probes | PASS |
| EV-003 | command / test | Full verification and command audit | pytest, AST parser, artifact verifier, residue check | PASS |
| EV-004 | command / review | Final scope, encoding, whitespace, and diff review | 11 intended paths and Git diff | PASS |

## EV-001 - Startup And Symbolic Derivation

- **Date:** 2026-07-13
- **Method or command:** Read required startup files, the previous product-distance dossier, implementation, patterns, tests, and research note; ran git status --short --branch; derived the high/low edge count, sum-matching interleave cycle, asymptotic limits, and residue-class tail witness.
- **Relevant output:** Initial tree clean. For even n, at least one high-high edge is forced; for odd n, at least two are forced and only one can lie below the target. The interleave edge set uses endpoint sums n+1, n+2, n+3. For n>=33, every residue polynomial for D=P-(n-1)A has positive coefficients after the least allowed quotient shift.
- **Interpretation:** The target adjacent formula and the n>=33 tail strictness are exact all-n theorems.
- **Limitations:** Exact evaluation for n=4..32 is finite formula computation. It is not order enumeration and does not determine W_n in the unresolved n=12..32 interval.
- **Linked log entry:** TASK_LOG.md#2026-07-13---startup-and-exact-derivation

## EV-002 - Truncated Table, Implementation, And Focused Tests

- **Date:** 2026-07-13
- **Method or command:** Exact Python probes with PYTHONPATH=src; edit source/tests with apply_patch; python -m pytest -p no:cacheprovider tests/test_product_distance.py -q.
- **Relevant output:** A first allocation-heavy probe timed out at 30.4 seconds without output. The optimized exact probe completed in 4 seconds and gave distance-one values (6,12,15,20,24,30,35,42,48); distance-two values equal W_n for all n=3..11. Focused pytest reported 12 passed.
- **Interpretation:** Non-adjacent constraints first change the bounded exact objective at n=9, and distance two accounts for the full objective and minimizer set through n=11.
- **Limitations:** This is finite exhaustive exact computation only. No cyclic-order enumeration beyond n=11 was run.
- **Linked log entry:** TASK_LOG.md#2026-07-13---exact-truncated-implementation-and-focused-tests

## EV-003 - Full Verification And Command Audit

- **Date:** 2026-07-13
- **Method or command:** Python AST parse of the changed Python files; focused
  product-distance/zigzag/tail pytest; full pytest; checked-artifact semantic
  verifier; direct comparison of the ten displayed residue polynomials at 80
  residue/quotient points.
- **Relevant output:** Python AST parsed 2 files; focused pytest reported 22
  passed; full pytest reported 140 passed; checked-artifact verification
  accepted 4 certificates, 76 local brackets, and the n=3..6 summary;
  residue_polynomials_verified=80.
- **Interpretation:** Source syntax, focused behavior, repository integration,
  existing checked artifacts, and the symbolic table all agree.
- **Limitations:** An attempted `node --check` on the Python source failed
  because Node rejects the .py extension. This was a command-selection error,
  not a source failure; the correct Python AST check passed immediately.
- **Linked log entry:** TASK_LOG.md#2026-07-13---research-memory-and-full-verification

## EV-004 - Final Scope, Encoding, Whitespace, And Diff Review

- **Date:** 2026-07-13
- **Method or command:** Exact intended-path PowerShell check; strict UTF-8 and
  trailing-whitespace scan; equation-tag uniqueness check; Git status;
  complete tracked/untracked review; `git diff --check`.
- **Relevant output:** scope_paths=11, bad_utf8=0, trailing_whitespace=0,
  equation_tags=19, unique_tags=19; `git diff --check` produced no output.
- **Interpretation:** The final change set is confined to source, tests,
  research/project memory, and the task dossier, with clean text hygiene.
- **Limitations:** Git warnings about the inaccessible user-global ignore file
  are environmental and do not affect repository status or diff content.
- **Linked log entry:** TASK_LOG.md#2026-07-13---final-hygiene-and-handoff

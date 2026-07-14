# EVIDENCE - TASK-20260714__first_long_distance_minimizer_restriction / First Long-Distance Minimizer Restriction

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / proof / independent exact computation | Startup and independent derivation | authoritative memory, proof/source/tests, two independent audits | PASS |
| EV-002 | proof / test / documentation | Theorem, witness, and bounded delta | primary proof, test module, authoritative memory, roadmap | PASS |
| EV-003 | command / test / review | Executable verification and independent audits | focused/full suites, checked artifacts, Ruff, three audits | PASS after environment rerun |
| EV-004 | review / hygiene | Final cross-document and complete-diff audit | nine intended paths and complete worktree delta | PASS after checker correction |

## EV-001 - Startup And Independent Derivation

- **Date:** 2026-07-14
- **Method or command:** Inspected all required startup files, relevant
  predecessor task memory, the exact residue theorem, production generator,
  existing independent scorers, roadmap, and read-only Git status; obtained
  separate read-only audits of the finite-range proof and \(n=93\) witness.
- **Relevant output:** For every omitted pair,
  \(ij/d\le n(n-1)/3\). Exact residue arithmetic gives
  \(3B_n-n(n-1)>0\) for every \(3\le n\le92\). At \(n=93\),
  \(B_{93}=2850\) while \(93\cdot92/3=2852\); the requested relocation of
  label \(54\) leaves the distance-two score at \(2850\) and makes
  \((92,93)\) the unique full-score maximizer at distance three with value
  \(2852\).
- **Interpretation:** The result has an exact combinatorial proof, with one
  finite exact witness check at the boundary.
- **Limitations:** This establishes no geometric consequence and performs no
  canonical cyclic-order enumeration beyond \(n=11\).
- **Linked log entry:**
  TASK_LOG.md#2026-07-14---startup-and-independent-exact-derivation

## EV-002 - Proof, Witness, And Bounded Delta

- **Date:** 2026-07-14
- **Method or command:** Added (MS1)--(MS7) to
  research/PRODUCT_DISTANCE_SURROGATE.md; added independent exact residue and
  all-pairs witness regressions to tests/test_product_distance.py; synchronized
  start.md, PROJECT_KNOWLEDGE.md, CURRENT_STATUS.md, and
  research/NEXT_RESEARCH_STEPS.md.
- **Relevant output:** The five concave residue polynomials have positive
  endpoint values throughout \(9\le n\le92\); the exact \(n=3,\dots,8\)
  values also satisfy the criterion. The moved-label order has exactly two
  retained-score maximizers at \(2850\), the unique score above \(2850\) is
  \((92,93,3,2852)\), and the maximum for distances at least four is \(2093\).
- **Interpretation:** EXACT THEOREM:
  \[
  \mathcal M_n=\mathcal M_n^{(\le2)}\quad(3\le n\le92),
  \qquad
  \mathcal M_{93}\subsetneq\mathcal M_{93}^{(\le2)}.
  \]
  Thus \(93\) is the first minimizer-restriction index.
- **Limitations:** No strict-inclusion persistence is claimed for every later
  index; the sufficient equality criterion holds again at \(n=94\). No
  production source or geometric statement changed.
- **Linked log entry:**
  TASK_LOG.md#2026-07-14---exact-theorem-witness-and-independent-tests

## EV-003 - Verification And Independent Audits

- **Date:** 2026-07-14
- **Method or command:** Targeted exact tests:
  python -m pytest -p no:cacheprovider tests/test_product_distance.py
  -k long_distance -q.
- **Relevant output:** 2 passed.
- **Interpretation:** The residue boundary and moved-label witness regressions
  pass independently.
- **Limitations:** Targeted tests do not replace the symbolic proof.
- **Linked log entry:**
  TASK_LOG.md#2026-07-14---executable-verification-and-independent-audits

- **Date:** 2026-07-14
- **Method or command:** Focused exact suite:
  python -m pytest -p no:cacheprovider tests/test_product_distance.py -q.
- **Relevant output:** 43 passed.
- **Interpretation:** The complete product-distance regression passes.
- **Limitations:** This is a focused suite only.
- **Linked log entry:**
  TASK_LOG.md#2026-07-14---executable-verification-and-independent-audits

- **Date:** 2026-07-14
- **Method or command:** Complete repository suite:
  python -m pytest -p no:cacheprovider -q with an explicit temporary
  directory, followed by the required outside-sandbox rerun after the first
  environment failure.
- **Relevant output:** First run: 31 setup errors because pytest could not
  create the requested temporary directory; no test body failed. Outside-
  sandbox rerun: all 171 tests passed with exit code 0.
- **Interpretation:** The retained failure is a filesystem-sandbox restriction,
  not a test defect; the complete suite is green.
- **Limitations:** Hosted CI was not inspected.
- **Linked log entry:**
  TASK_LOG.md#2026-07-14---executable-verification-and-independent-audits

- **Date:** 2026-07-14
- **Method or command:** Checked-artifact semantic verifier, Ruff on
  tests/test_product_distance.py, and Python compilation of that test module.
- **Relevant output:** Artifact verification accepts 4 certificates, 76 local
  brackets, and summary values \(3,4,5,6\); Ruff reports
  "All checks passed!"; compilation exits 0 without output.
- **Interpretation:** Existing checked artifacts remain semantically valid,
  and the changed Python file passes static checks.
- **Limitations:** The existing guarded interval-backend trust boundary is
  unchanged.
- **Linked log entry:**
  TASK_LOG.md#2026-07-14---executable-verification-and-independent-audits

- **Date:** 2026-07-14
- **Method or command:** Independent mathematical, implementation/test, and
  cross-document audits.
- **Relevant output:** Mathematical and implementation audits report PASS
  after reconstructing all residue formulas, the complete local pair-set
  delta, all 4186 exact pair scores, independent scorer paths, unique equation
  tags, unchanged production source, and the hard \(n\le11\) enumeration
  boundary. The first documentation audit correctly identified that current
  status and task memory still needed synchronization; those files were then
  updated for a final rerun.
- **Interpretation:** Independent review confirms the theorem and executable
  boundary; documentation requires one final post-update audit.
- **Limitations:** Independent review does not establish hosted CI status.
- **Linked log entry:**
  TASK_LOG.md#2026-07-14---executable-verification-and-independent-audits

## EV-004 - Final Cross-Document And Complete-Diff Audit

- **Date:** 2026-07-14
- **Method or command:** Reran the independent cross-document audit after
  synchronizing CURRENT_STATUS.md and all dossier files; scanned all nine
  intended paths for strict UTF-8, lone CR, tabs, trailing whitespace,
  mojibake, balanced display math, duplicate proof tags, stale minimizer
  claims, changed-path scope, production-source changes, forbidden \(n=93\)
  enumerator calls, complete tracked/untracked content, and Git diff hygiene.
- **Relevant output:** Documentation audit PASS; text_hygiene=PASS paths=9
  tags=163; stale_claim_scan=PASS; source diff empty;
  MAX_ENUMERATION_N remains 11; no \(n=93\) enumerator call; exactly nine
  intended changed paths; complete diff inspection and git diff --check PASS.
- **Retained failed check:** the first PowerShell hygiene command placed a
  colon immediately after an interpolated variable name, causing a parser
  error. Delimiting the variable names explicitly produced the valid PASS
  above.
- **Interpretation:** The theorem, tests, authoritative memory, roadmap,
  current status, and task evidence are mutually consistent and ready for
  manual review.
- **Limitations:** The worktree is intentionally unstaged and uncommitted;
  hosted CI was not inspected.
- **Linked log entry:**
  TASK_LOG.md#2026-07-14---final-cross-document-and-complete-diff-audit

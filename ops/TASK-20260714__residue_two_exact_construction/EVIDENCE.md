# EVIDENCE - TASK-20260714__residue_two_exact_construction / Residue-Two Exact Construction

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / derivation / exact computation | Startup and symbolic candidate | project memory, witnesses, independent audits | PRELIMINARY PASS |
| EV-002 | source / proof / test / independent review | Exact construction, proof, and tests | product-distance source/tests/proof | PASS |
| EV-003 | command / test / artifact / rendering | Automated verification and TeX repair | local verification commands and byte audit | PASS after repair |
| EV-004 | documentation / hygiene | Durable memory and final diff audit | intended ten-path delta | PASS |

## EV-001 - Startup And Symbolic Candidate

- **Date:** 2026-07-14
- **Method or command:** Inspected all mandatory startup and relevant task
  state, exact proof/source/tests, and the clean Git tree; assigned three
  independent read-only audits; evaluated candidate formulas with exact
  integer and rational all-pairs scoring without extending canonical cyclic
  enumeration.
- **Relevant output:** With `D=d-1`, all three analyses validate the same
  parity-aware block family. It is a permutation in every checked case,
  attains `J_n` on the edge `(D-1,2k+2)`, and passes exact all-pairs checks.
- **Interpretation:** This is candidate-identification and falsification
  evidence only; the all-`k` classification will rest on the pending symbolic
  proof plus the already accepted lower obstruction.
- **Limitations:** No finite sweep proves the symbolic family, and no
  geometric or new asymptotic claim follows.
- **Linked log entry:** `TASK_LOG.md#2026-07-14---startup-and-symbolic-candidate`

## EV-002 - Exact Construction, Proof, And Tests

- **Date:** 2026-07-14
- **Method or command:** Added `residue_two_product_distance_order(n)`; added
  a second independent label-first all-pairs scorer beside the position-first
  oracle; added exact parity, local-distance, closing, all-pairs, and strict
  domain tests; wrote R2C1--R2C25; obtained independent mathematical and
  implementation audits.
- **Relevant output:** The generator exactly partitions the core in both
  parity branches, uses no search, and has score \(J_n\), attained on the
  edge \((D-1,2k+2)\). Independent reconstruction matches every generated
  tuple for \(2\le k\le5000\). Both independent scorers return \(J_n\) on
  selected parity-balanced cases.
- **Interpretation:** EXACT THEOREM: \(B_n=W_n=J_n\) at \(n=12\) and for
  every \(n\equiv2\pmod5\), \(n\ge17\). The finite checks support but do not
  replace the symbolic proof.
- **Limitations:** The theorem is combinatorial; no geometric optimum or new
  asymptotic coefficient is asserted. The \(n=7\) value remains a bounded
  finite-table fact outside the generator domain.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-14---exact-generator-proof-and-independent-scorers`

## EV-003 - Automated Verification And Rendering Repair

- **Date:** 2026-07-14
- **Method or command:** Ran targeted, focused, integrated, and full pytest;
  py_compile; Ruff; checked-artifact semantic verification; independent AST
  and formula audits; byte-level line-ending and TeX-delimiter inspection.
- **Relevant output:** New tests \(6/6\); focused \(41/41\); integrated
  \(56/56\); full suite \(169/169\); compile and Ruff PASS; checked artifacts
  report 4 certificates, 76 local brackets, and summary values \(3,4,5,6\).
  The implementation audit confirms linear search-free code and two scorer
  call graphs independent of production support.
- **Retained correction:** The first proof patch interpreted some inline TeX
  backslashes as escape characters, creating missing markup and lone carriage
  returns. Independent audit found the defect. After repair, R2C has balanced
  inline delimiters, no doubled delimiters, and no lone carriage return.
- **Interpretation:** No mathematical or executable check fails; the retained
  issue was a corrected serialization defect.
- **Limitations:** Full pytest used unsandboxed system temporary-directory
  access already known to be required by this repository; hosted CI was not
  inspected.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-14---automated-verification-and-tex-repair`

## EV-004 - Durable Memory And Final Diff Audit

- **Date:** 2026-07-14
- **Method or command:** Synchronized all durable project state; inspected the
  complete intended delta; checked all ten paths as strict UTF-8 with no lone
  carriage returns, control characters, tabs, or trailing whitespace; checked
  proof delimiters and equation-tag uniqueness; ran `git status --short`,
  `git diff`, and `git diff --check` without modifying Git state.
- **Relevant output:** The ten intended paths are the only worktree delta.
  Text and proof hygiene pass, all equation tags are unique, and
  `git diff --check` exits successfully with no output.
- **Interpretation:** Durable state matches the implementation and exact
  theorem; the task satisfies the repository's `READY_FOR_REVIEW` contract.
- **Limitations:** Hosted CI remains uninspected, and the user must perform
  any staging or commit manually.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-14---durable-handoff-and-final-audit`

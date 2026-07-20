# EVIDENCE - TASK-20260719 / PGODD Exact K

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git | Startup and independent reconstruction | repository root and retained research notes | VERIFIED |
| EV-002 | exact theorem | Backbone, argmax, score, residues, and K825 comparison | `research/FIXED_ORDER_CYCLE_RATIO.md` | PROVED |
| EV-003 | bounded exact computation | Independent max-plus and all-arcs diagnostic | `exact_diagnostic.py` | VERIFIED |
| EV-004 | regression / hygiene | Repository checks and final diff audit | repository root | VERIFIED |

## EV-001 - Startup And Source Reconstruction

- **Date:** 2026-07-19
- **Method or command:** read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the PGODD construction, the
  fixed-order `K` definition, K825, and the prior shortcut proofs; inspect
  read-only Git status and recent history; obtain three independent
  read-only derivations.
- **Relevant output:** clean main worktree at
  `513f294d6c7e79e899d953f8b197ae3e23cded73`; all derivations agree on the
  same core word, unique tail, exact score, residue split, boundary margins,
  and strict same-row K825 comparison.
- **Interpretation:** the bounded task can proceed without mixing unrelated
  work, and no candidate search or modification is needed.
- **Limitations:** agreement of derivations is not a substitute for the
  recorded symbolic proof or final verification.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---startup-and-independent-derivations`.

## EV-002 - Exact Symbolic Theorem

- **Date:** 2026-07-19
- **Method or command:** direct reconstruction of (PGODD-6); exact
  isolated-hole identity; nine-class elimination-gain audit; all-length
  compressed-shortcut proof with separate doubleton, singleton, and cyclic
  roles; exact block summation; five residue substitutions; exact K825
  specialization and subtraction.
- **Relevant output:** (KPGODD-1)--(KPGODD-36) prove the sole maximizer
  \(B_m=\{4m+3,\ldots,10m+8\}\), score (KPGODD-4), exact hole minimum
  \(28m+26\), exact shortcut minima \(4,30,12m+10\), five residue branches,
  coefficient \(857/3000\), and strict same-row improvement over K825 for
  every \(m\ge1\).
- **Interpretation:** this is an exact all-domain fixed-core combinatorial
  theorem. There is no obstruction and no hidden boundary correction.
- **Limitations:** the theorem does not identify a global minimizing order or
  imply an angular, geometric, or global-optimality result.
- **Linked log entry:**
  EVIDENCE.md is linked from the exact-theorem task-log entry.

## EV-003 - Independent Max-Plus And All-Arcs Diagnostic

- **Date:** 2026-07-19
- **Method or command:**
  python ops/TASK-20260719__pgodd_exact_k/exact_diagnostic.py.
- **Relevant output:** PASS; 1,000 formula/residue rows and 5,012,000 literal
  core entries; 30 max-plus rows and 39,461,580 transitions; 1,007,210
  proper oriented arcs, including 1,000,460 nontrivial compressed shortcuts;
  unique backbone and exact \(m=1,2\) witnesses; strict K825 comparison.
- **Interpretation:** an independent recurrence and a separate all-arcs scan
  corroborate the symbolic score, uniqueness, hole/shortcut minima, residue
  formulas, closure, and boundaries.
- **Limitations:** the finite limits are explicit; the diagnostic cannot
  prove the all-\(m\) theorem and searches no alternative order.
- **Linked log entry:**
  EVIDENCE.md is linked from the exact-theorem task-log entry.

## EV-004 - Regression, Source, And Diff Hygiene

- **Date:** 2026-07-19
- **Method or command:** `python -m py_compile` and scoped Ruff checks on the
  diagnostic; `python -m pytest -p no:cacheprovider`; the focused
  checked-artifact schema suite; `python -m power_ringmin.verify_checked_artifacts`
  with `PYTHONPATH=src`; a Section 17 tag/display/environment audit; two
  independent mathematical audits and one independent diagnostic audit;
  `git status --short --branch`, complete tracked/untracked source inspection,
  `git diff`, and `git diff --check`.
- **Relevant output:** syntax and Ruff pass; 283 pytest tests pass; 4 focused
  schema tests pass; the independent verifier passes for four certificates,
  76 local brackets, and `n=3,4,5,6`; the scoped source audit finds 36
  sequential unique KPGODD tags, 42 balanced displays, balanced
  `aligned`/`array`/`cases`/`gathered` environments, and no control characters
  or unescaped `qquad`; all three independent reviews report no remaining
  defect; final diff hygiene exits zero.
- **Corrections preserved:** the first Ruff format check found one mechanical
  formatting delta, after which formatting and the repeat check passed. The
  first TeX audit was incorrectly scoped to the entire long historical file
  and therefore reported pre-existing global counts; the corrected audit is
  restricted to the new Section 17 and passes.
- **Interpretation:** the task's exact proof, sole bounded diagnostic, and
  authoritative-memory synchronization are internally consistent and
  regression-safe. Status is `READY_FOR_REVIEW`.
- **Limitations:** Git could not read the user-level exclude file outside the
  sandbox, but repository-local status/diff commands completed with exit code
  zero. Manual review of the long symbolic proof remains appropriate; no
  commit was created.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---verification-and-handoff`.

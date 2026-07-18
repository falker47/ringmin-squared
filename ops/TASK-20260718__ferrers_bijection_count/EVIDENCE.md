# EVIDENCE - TASK-20260718__ferrers_bijection_count / Ferrers Bijection Count

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / confirmation | Startup, scope, and independent symbolic derivations | retained PG material and clean repository state | PASS |
| EV-002 | computation | Bounded independent Ryser permanent diagnostic | exact_diagnostic.py | PASS |
| EV-003 | test / command | Static checks, regressions, suite, schemas, and artifacts | repository commands | PASS |
| EV-004 | inspection | Proof, code, synchronization, scope, hygiene, and final diff | intended nine-file scope | PASS |

## EV-001 - Startup, Scope, And Independent Derivation

- **Date:** 2026-07-18
- **Method or command:** Read AGENTS.md, start.md, PROJECT_KNOWLEDGE.md,
  CURRENT_STATUS.md, research/PRODUCT_DISTANCE_SURROGATE.md,
  research/NEXT_RESEARCH_STEPS.md, the PG37--PG49 and PG50--PG63 predecessor
  dossiers, templates, and `git status`; compare three independent read-only
  count, symmetry, and diagnostic derivations.
- **Relevant output:** clean `main...origin/main` worktree at
  `b1a4054d1fac75443cf1929921dddb38f9750a5f`; unanimous formula
  \[
  \mathsf F_m^{\rm lab}
  =\prod_{j=1}^{2m-1}(j+1-\kappa_j),
  \qquad
  \kappa_j=
  \left\lceil{j(8m+3)\over2(8m+4+j)}\right\rceil,
  \]
  with the dual row product, every requested boundary, the exact PG36/PG62
  class identity, and the labelled convention.
- **Interpretation:** The retained support and full-score theorems were stable,
  and the missing result was exactly a Ferrers perfect-matching count. The
  nested-neighborhood recurrence is independent of any permutation
  enumeration.
- **Limitations:** Independent agreement does not replace the written
  all-\(m\) proof.
- **Linked log entry:** TASK_LOG.md, STRICT startup and scope; independent
  symbolic derivation.

## EV-002 - Bounded Independent Ryser Diagnostic

- **Date:** 2026-07-18
- **Method or command:**
  `python ops\TASK-20260718__ferrers_bijection_count\exact_diagnostic.py`
- **Relevant output:**

  | \(m\) | reduced size | penultimate \(\kappa\) | closing \(\kappa\) | Ferrers / Ryser count | nonempty subsets |
  |---:|---:|---:|---:|---:|---:|
  | 3 | 5 | 2 | 3 | 36 | 31 |
  | 4 | 7 | 3 | 3 | 720 | 127 |
  | 5 | 9 | 4 | 4 | 21,600 | 511 |
  | 6 | 11 | 5 | 5 | 725,760 | 2,047 |
  | 7 | 13 | 5 | 6 | 46,448,640 | 8,191 |
  | 8 | 15 | 6 | 7 | 3,292,047,360 | 32,767 |

  Final line:
  `PASS: exact Ryser subset check; no path-permutation enumeration`.
- **Interpretation:** The script constructs PG49 directly from
  \(2k(d+j)\ge j(d-1)\), without calling either threshold product, then
  computes the reduced permanent by exact Ryser inclusion--exclusion. Both
  symbolic products and fixed expected integers agree. The 43,674 examined
  objects are column subsets, not path permutations or matchings. The rows
  cover the minimum parameter and all five residue classes of the terminal
  thresholds.
- **Limitations:** The fixed rows corroborate rather than prove the symbolic
  theorem. No cyclic order is built and no product-distance score is checked.
- **Linked log entry:** TASK_LOG.md, proof and sole bounded diagnostic.

## EV-003 - Static Checks, Regressions, Suite, Schemas, And Artifacts

- **Date:** 2026-07-18
- **Method or commands:**
  - run the exact diagnostic before and after the matrix-orientation wording
    correction;
  - in-memory `compile(...)` of the diagnostic source;
  - `python -m ruff check` and `python -m ruff format --check` on the
    diagnostic;
  - focused product-distance pytest with `-p no:cacheprovider` and a
    task-specific `C:\tmp` basetemp;
  - serial complete pytest suite with the same cache isolation;
  - checked-artifact schema regression with a separate task-specific basetemp;
  - set `PYTHONPATH=src` and run
    `python -m power_ringmin.verify_checked_artifacts`.
- **Relevant output:** diagnostic PASS on \(m=3,\ldots,8\); compile PASS;
  Ruff lint and final format check PASS; 49 focused tests PASS; all 283
  repository tests PASS; four schema tests PASS; checked artifacts verified
  with four certificates and 76 local brackets.
- **Retained failed check:** the first Ruff format check reported that the
  sole diagnostic would be reformatted. `python -m ruff format` changed that
  file mechanically; lint, format, and the diagnostic then passed. No
  mathematical or runtime failure occurred.
- **Interpretation:** No production, test, schema, artifact, or repository
  regression was detected. The final diagnostic orientation agrees with the
  proof convention of path rows and gap columns.
- **Limitations:** Existing tests do not prove the new all-\(m\) theorem.
- **Linked log entry:** TASK_LOG.md, proof and sole bounded diagnostic; final
  verification and handoff.

## EV-004 - Proof, Code, Synchronization, Scope, Hygiene, And Final Diff

- **Date:** 2026-07-18
- **Method or command:** three independent read-only audits of the PG64--PG73
  proof, diagnostic code, and cross-file synchronization; code re-audit after
  the orientation correction; equation-tag uniqueness, expected-path,
  sole-diagnostic, UTF-8/BOM, final-newline, trailing-whitespace, generated-
  cache, display/fence, complete-diff, `git status`, and `git diff --check`
  inspection.
- **Relevant output:** the proof audit passed the recurrence, both products,
  every endpoint and transition boundary, PG36/PG49/PG62/PG63 equivalence,
  and labelled/dihedral injectivity. The code audit passed Ryser signs,
  support construction, independence, bounds, and non-enumerative scope. The
  synchronization audit found one row/column wording mismatch: PG65 named gap
  rows while the surrounding convention called gaps columns. PG65 and the
  diagnostic construction were transposed consistently to path rows and gap
  columns; synchronization and code re-audits then passed. PG64--PG73 are
  unique, and final hygiene and whitespace checks pass on exactly five
  synchronized project Markdown files plus four dossier files.
- **Retained hygiene corrections:** the first final harness found one trailing
  space in this evidence file and an audit-generated `__pycache__`; both were
  removed. It also reported 459 opening versus 457 closing display tokens in
  the full proof note. The unchanged `HEAD` file has 445 versus 443, so the
  task delta is balanced at 14 versus 14. The corrected check compares the
  edited state with `HEAD` rather than attributing the retained global
  difference to this task. A second version required equal display deltas and
  rejected CURRENT_STATUS.md because replacing it removed the inherited
  imbalance instead of preserving it. The final check requires that a tracked
  file not worsen its `HEAD` imbalance; it accepts this improvement and passed
  the exact nine-path scope.
- **Interpretation:** The exact theorem, bounded oracle, durable state, and
  scope agree. No production, test, artifact, cache, geometric, or
  alternative-scaffold path changed.
- **Limitations:** Inspection cannot replace user review.
- **Linked log entry:** TASK_LOG.md, authoritative synchronization in
  progress; final verification and handoff.

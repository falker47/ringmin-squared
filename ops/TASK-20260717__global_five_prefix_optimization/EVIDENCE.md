# EVIDENCE - Global Five-Prefix Optimization

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | STRICT startup and isolation | authoritative memory / Git | pass |
| EV-002 | exact derivation | Compact envelope and exact candidate | CR28 inputs / independent algebra | pass |
| EV-003 | exact computation | Standalone optimizer diagnostic | `exact_diagnostic.py` | pass |
| EV-004 | regression / static | Repository and source verification | commands / source | pass |
| EV-005 | audit / scope | Independent proof and final-diff audits | source / Git | pass |

## EV-001 - Startup And Isolation

- **Date:** 2026-07-17
- **Method or command:** read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, relevant proof sections and
  prior dossiers; run `git status --short --branch` and `git rev-parse HEAD`.
- **Relevant output:** clean `main` tracking `origin/main` at
  `9fc4b2caeb385a7cd34c62fc494fd91182935f06`.
- **Interpretation:** task isolation and the exact prior inputs are verified.
- **Limitations:** source inspection is not evidence for the new optimizer.
- **Linked log entry:** `TASK_LOG.md#2026-07-17---strict-startup-and-isolation`.

## EV-002 - Compact Envelope And Exact Candidate

- **Date:** 2026-07-17
- **Method or command:** independent exact algebra from CR28cr--CR28dd and
  CR28dr--CR28dw, cross-checked against the four-prefix compact proof.
- **Relevant output:** coordinatewise clipping leaves 21 ordered regimes; the
  new \(m=4\) predecessor margin is positive; the unique envelope candidate
  lies strictly in `MMMMM` before the first high-clipping transition.
- **Interpretation:** CR28dz20--CR28dz42 prove the compact global optimum,
  uniqueness, coefficient identity, and strict comparison chain.
- **Limitations:** this is a fixed-template theorem; it supplies neither
  finite irrational rounding nor a growing-\(k\) conclusion.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-17---exact-candidate-and-branch-reconstruction`.

## EV-003 - Standalone Exact Diagnostic

- **Date:** 2026-07-17
- **Method or command:**
  `python -B ops\TASK-20260717__global_five_prefix_optimization\exact_diagnostic.py`.
- **Relevant output:** `PASS`; 21 clipping regimes; exact optimizer and
  coefficient isolating intervals; all polynomial, branch, pair/coefficient
  identity, transition, collision, and comparison-margin assertions pass.
- **Interpretation:** one dossier-local, standard-library exact computation
  independently corroborates every requested algebraic diagnostic.
- **Limitations:** bounded executable corroboration does not replace the
  written all-real compact proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-17---verification-and-independent-audit`.

## EV-004 - Repository And Source Verification

- **Date:** 2026-07-17
- **Methods or commands:** Ruff check and format check on the sole new Python
  file; `python -m pytest tests\test_fixed_order_cycle_ratio.py -q -p
  no:cacheprovider`; `python -m pytest -q -p no:cacheprovider`; existing
  schema/artifact verifiers and four historical exact diagnostics; equation-
  tag, delimiter, LaTeX-environment, UTF-8/control-byte, synchronization, Git
  status/diff, and `git diff --check` inspections.
- **Relevant output:** Ruff passes; 101 focused and 283 full-suite tests pass;
  schema tests pass; 4 certificates and 76 local brackets verify; normalized
  simplex through \(k=8\), global \(k=4\), rational \(k=5\), and finite
  rational \(k=5\) diagnostics pass; 366 equation tags are unique; all
  delimiters/environments balance; encodings and diff check are clean.
- **Preliminary check corrections:** the first Ruff format check requested
  reformatting, so the diagnostic was formatted and both Ruff checks were
  rerun successfully. A later occurrence-based delimiter probe falsely
  counted 12 LaTeX table-spacing tokens such as `\\[1mm]` as display
  openings; the standalone-line delimiter audit gives the correct
  `684/684` balance for the primary proof and passes on every changed
  Markdown file.
- **Interpretation:** the documentation-only theorem and standalone diagnostic
  preserve existing verified behavior and source integrity.
- **Limitations:** hosted CI was not run locally.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-17---verification-and-independent-audit`.

## EV-005 - Independent And Scope Audits

- **Date:** 2026-07-17
- **Method:** three independent agents audited the exact optimizer algebra and
  comparison margins, all clipping/transition/collision/face branches, and the
  final authoritative synchronization and bounded diff.
- **Relevant output:** exact data agree. Five concrete proof-wording/citation
  issues were corrected; the final re-audit reports no remaining mathematical,
  synchronization, or scope defect.
- **Interpretation:** the conclusion does not depend on a single derivation or
  a single source representation.
- **Limitations:** independent reviews inspect the same repository and are not
  an external peer review.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-17---verification-and-independent-audit`.

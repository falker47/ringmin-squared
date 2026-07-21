# EVIDENCE - TASK-20260721 / Canonical Odd-v E5 Path-Gap Support

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git | Startup and scaffold reconstruction | authoritative repository sources | VERIFIED |
| EV-002 | exact theorem | Local relation, Hall support, four distance classes, full support | PGE5ODD-1--PGE5ODD-26 | PROVED |
| EV-003 | bounded exact computation | Sole standalone small-row diagnostic | `exact_diagnostic.py` | PASS |
| EV-004 | independent review | Algebra, cyclic closure, Hall, diagnostic, scope, document roles | three read-only audits | PASS |
| EV-005 | regression / structure | Tests, artifacts, Ruff, source audit | repository root | PASS |
| EV-006 | final inspection | Durable state, exact scope, caches, diff, whitespace | repository root | PASS |

## EV-001 - Startup And Source Reconstruction

- **Date:** 2026-07-21
- **Method or command:** read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, UC1--UC20,
  PGE5-1--PGE5-26, the prior even-PGE5 dossier/diagnostic, relevant
  odd-parity scaffold sources, and read-only Git status/HEAD.
- **Relevant output:** clean `main...origin/main` worktree at
  `f4cd81b1342ec356c5baa35eeb3338ddcdc8f1c8`; no unrelated modifications.
  The exact specialization is `v=2m+1`, `d=8m+9`, `n=10m+9`,
  `t=m+2`, `epsilon=0`, `r=m-1`.
- **Interpretation:** the exact structural domain is `m>=1`. The branch has
  `m+2` triples, no doubleton, and `m-1` singletons, and it was not already
  classified by the even-PGE5 or odd-`e=4` results.
- **Limitations:** source reconstruction alone proves neither local support
  nor the full score.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---strict-startup-and-odd-branch-reconstruction`.

## EV-002 - Exact All-Domain Support Theorem

- **Date:** 2026-07-21
- **Method:** exact integer comparison of every literal distance-one and
  distance-two form, including the true cyclic closure; monotone inversion
  to row/column thresholds; residual suffix Hall; and separate universal
  bounds for distances three and at least four.
- **Relevant result:** PGE5ODD-1--PGE5ODD-26 prove, for every `m>=1`,
  `R_loc={(k,j):k>=kappa_j}` and
  `R_full=R_ext={(0,0)} union {(k,j):j>0,k>=kappa_j}`. Every scaffold
  bijection has `W=W^(<=2)`, and local compatibility is equivalent to
  `W=W_n`.
- **Boundary evidence:** the proof explicitly treats the empty singleton
  range at `m=1`, the absence of every doubleton, `m=2`, both terminal
  thresholds, the actual closing word, and the first false-closure
  discriminator at `m=4`.
- **Interpretation:** **exact all-domain combinatorial support theorem**.
  There is no odd-parity completion obstruction. The local board is Ferrers;
  the full support has an induced `2K2`; its forced-edge reduction is
  matching-covered Ferrers.
- **Limitations:** the theorem evaluates no `K`, chooses no assignment,
  classifies no outside-scaffold minimizer, and implies no angular or
  geometric conclusion.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---exact-support-theorem-and-sole-diagnostic`.

## EV-003 - Sole Bounded Standard-Library Diagnostic

- **Date:** 2026-07-21
- **Command:**
  `python -B ops/TASK-20260721__canonical_e5_odd_path_gap_support/exact_diagnostic.py`.
- **Declared direct interval:** `m=1..30`.
- **Relevant output:** PASS; 39,710 literal local incidences, 30,948 local
  Ferrers edges, 1,408,738 residual suffix Hall inequalities, 30,018
  Hall-extendible edges, and 930 exact zero-column obstructions. The script
  also exhausts all 5,166 scaffold bijections for `m=1..3`, scores every
  unordered core pair by true smaller cyclic distance, and finds exactly
  158 compatible/full-threshold bijections with the predicted edge support.
- **Interpretation:** **bounded exact computation**. Direct symbolic-margin
  assertions and exhaustive all-pairs scoring independently cover distances
  `1`, `2`, `3`, and `>=4`, the minimum row, the empty singleton range, the
  genuine closure split, local/full support, and Ferrers reduction.
- **Limitations:** the script imports no project/test helper and computes no
  `K`, but finite computation corroborates rather than proves EV-002.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---exact-support-theorem-and-sole-diagnostic`.

## EV-004 - Independent Audits And Corrections

- **Date:** 2026-07-21
- **Method:** three independent read-only reviews: exact algebra and all four
  distance classes; literal diagnostic, exhaustive cyclic scorer, and count
  reproduction; source/tag/link/document-role and scope audit.
- **Relevant output:** all reviews reproduce PGE5ODD-1--PGE5ODD-26 and the
  diagnostic counts. They identified one terminal-low maximum that lacked
  its global `j` quantifier, a locally undefined `W^(=1)` abbreviation, and
  two ambiguous antecedents caused by inserting the odd theorem before an
  even-PGE5 follow-up. The text now quantifies the maximum, defines the
  notation, and names the even scaffold explicitly. The diagnostic now
  retains and checks separate cyclic maxima for distances `1`, `2`, `3`, and
  `>=4`, asserts `W>=T`, and rejects `m=0`.
- **Source audit:** PASS with 26 unique sequential tags, 32/32 displays,
  4/4 environments, 118/118 braces, and no control characters.
- **Interpretation:** all retained corrections harden notation or diagnostic
  coverage; none changes a mathematical conclusion.
- **Limitations:** independent review supports but does not replace the
  authoritative proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---independent-audits-and-retained-corrections`.

## EV-005 - Repository Verification

- **Date:** 2026-07-21
- **Methods or commands:** final diagnostic; in-memory syntax compile;
  `python -m ruff check --no-cache` and
  `python -m ruff format --check --no-cache` on the diagnostic; PGE5ODD
  source-structure audit; `python -m pytest -p no:cacheprovider`; focused
  checked-artifact schema pytest; `n=3` Arb interval cross-check; and
  `python -m power_ringmin.verify_checked_artifacts` with `PYTHONPATH=src`.
- **Relevant output:** diagnostic PASS with EV-003 counts; syntax PASS; Ruff
  lint/format PASS; source audit PASS; full pytest `283 passed`; schema
  pytest `4 passed`; Arb cross-check `3 passed`; checked artifacts verified
  for four certificates, 76 local brackets, and `n=3,4,5,6`.
- **Retained failed check:** the first Ruff format check reported that the
  diagnostic would be reformatted. Ruff applied one mechanical formatting
  pass; the repeated lint, format, and diagnostic checks pass with unchanged
  counts.
- **Interpretation:** no regression remains in the repository, source
  structure, schemas, finite artifacts, or the task-local diagnostic.
- **Limitations:** tests and bounded checks do not independently prove
  EV-002; hosted CI was not run or claimed.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---repository-verification`.

## EV-006 - Final Inspection

- **Date:** 2026-07-21
- **Method or command:** complete tracked-diff and untracked-file inspection;
  `git status --short --branch`; `git diff --stat`; `git diff --numstat`;
  dossier cache/bytecode scan; and final `git diff --check` after all durable
  state updates.
- **Relevant output:** exactly four tracked project-memory/proof files and
  the four expected new dossier files are in scope. No cache or bytecode file
  is present. The complete diff is confined to proof, compact stable memory,
  roadmap, current status, diagnostic, and task-local evidence. Final
  whitespace validation passes.
- **Interpretation:** the bounded task is internally consistent, verified,
  and `READY_FOR_REVIEW`; the protected upstream and Git history remain
  untouched.
- **Limitations:** user review and manual commit remain required.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---final-inspection-and-handoff`.

# EVIDENCE - TASK-20260720 / Canonical Even-v E5 Path-Gap Support

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / Git | Startup and scaffold reconstruction | authoritative repository memory and proof sources | VERIFIED |
| EV-002 | exact theorem | Local relation, Hall/Ferrers, and full support | PGE5-1--PGE5-26 | PROVED |
| EV-003 | bounded exact computation | Sole direct standalone diagnostic | `exact_diagnostic.py` | PASS |
| EV-004 | independent review | Algebra, Hall/Ferrers, scope, and diagnostic audits | three read-only audits | PASS |
| EV-005 | regression / structure | Repository tests, artifacts, Ruff, and source audit | repository root | PASS |
| EV-006 | final inspection | Durable state, scope, diff, and whitespace | repository root | PASS |

## EV-001 - Startup And Source Reconstruction

- **Date:** 2026-07-20
- **Method or command:** read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, UC1--UC20, PG16--PG49,
  pertinent recent task dossiers, and read-only Git status/HEAD.
- **Relevant output:** clean `main...origin/main` worktree at
  `d69178766f61a22875ea9f29fc99121db6e2fddf`; no unrelated modifications.
- **Interpretation:** `e=5`, even `v` was a distinct unresolved path/gap
  branch. The canonical specialization has `m>=2`, `m+1` triples, one
  doubleton, and `m-2` singletons.
- **Limitations:** source reconstruction alone proves neither the local
  relation nor completion support.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---strict-startup-and-scaffold-reconstruction`.

## EV-002 - Exact All-Domain Support Theorem

- **Date:** 2026-07-20
- **Method:** direct integer comparison of every local one- and two-step form;
  monotone cutoff inversion; nested-suffix residual Hall; deterministic
  interval shifts used only as edge-existence witnesses; and universal
  distance-three and long-distance bounds.
- **Relevant result:** PGE5-1--PGE5-26 prove, for every `m>=2`,
  `R_loc={(k,j): k>=kappa_j}` and
  `R_full=R_ext={(0,0)} union {(k,j): j>0, k>=kappa_j}`. The global support
  is non-Ferrers by an induced `2K2`; its forced-edge reduction is Ferrers
  and matching-covered. Every compatible scaffold reassignment has
  `W=W_n`.
- **Boundary evidence:** all triple/doubleton/singleton and
  nonclosing/closing forms, terminal thresholds, `m=2`, `m=3`, empty
  singleton range, doubleton closure, singleton closure, and inclusive cutoff
  equality are explicit.
- **Interpretation:** **exact all-domain combinatorial support theorem**. It
  gives global product-distance minimality to the supported scaffold
  bijections but does not classify minimizers outside the scaffold.
- **Limitations:** no selected construction, `K`, angular/geometric theorem,
  production change, or global `K`/geometric-optimality conclusion.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---exact-local-hall-ferrers-and-full-support-theorem`.

## EV-003 - Sole Bounded Direct Diagnostic

- **Date:** 2026-07-20
- **Command:**
  `python -B ops/TASK-20260720__canonical_e5_even_path_gap_support/exact_diagnostic.py`.
- **Declared interval:** `m=2..40` (39 rows).
- **Relevant output:** PASS; 88,556 literal path/gap relation checks, 69,124
  local Ferrers edges, 4,132,070 residual suffix Hall inequalities, 67,525
  Hall-extendible edges, and 1,599 exact zero-column obstructions. Minimum
  row, empty singleton range, cyclic closure, inclusive boundary equality,
  global/reduced Ferrers distinction, and full-distance symbolic margins
  pass.
- **Retained failed run:** the first direct-set implementation through
  `m=60` timed out after 60.4 seconds. Exact bit masks replaced costly set
  unions, and the declared bounded interval became `m=2..40`; final runs pass
  in roughly 14--16 seconds.
- **Interpretation:** **bounded exact computation** corroborating EV-002,
  not replacing it.
- **Limitations:** the script imports no project or test helper, builds no
  complete assignment, searches no matching/path permutation/order family,
  enumerates no subset, and computes no `K`.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---bounded-diagnostic-and-retained-corrections`.

## EV-004 - Independent Audits And Corrections

- **Date:** 2026-07-20
- **Method:** three independent read-only audits: exact local algebra and
  full-distance collapse; residual Hall, shift directions, Ferrers status,
  and boundaries; and diagnostic implementation/scope/counts.
- **Relevant output:** all audits reproduce the theorem. They identified two
  documentation defects: `start.md` had one missing backslash before
  `\left`, and the first scope disclaimer appeared to deny any global
  minimizer conclusion despite `W=W_n`. Both were corrected; the text now
  states exact global `W`-minimality for supported scaffold bijections while
  excluding only distinct `K`/geometric claims and outside-scaffold
  classification.
- **Interpretation:** independent review corroborates EV-002 and hardened its
  logical scope. Neither correction changes an equation or diagnostic result.
- **Limitations:** read-only audits support but do not replace the durable
  proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---independent-audits-and-repository-verification`.

## EV-005 - Repository Verification

- **Date:** 2026-07-20
- **Methods or commands:** final standalone diagnostic; in-memory syntax
  compile; scoped `python -m ruff check --no-cache`; scoped
  `python -m ruff format --check --no-cache`; line-anchored PGE5 tag,
  delimiter, environment, brace, and control-character audit;
  `python -m pytest -p no:cacheprovider`; focused checked-artifact schema
  pytest; and `python -m power_ringmin.verify_checked_artifacts` with
  `PYTHONPATH=src`.
- **Relevant output:** diagnostic PASS with EV-003 counts; syntax PASS; Ruff
  lint/format PASS; source audit PASS with 26 sequential tags, 42 balanced
  displays, 139/139 braces, balanced environments, and no control characters;
  full pytest 283 passed; focused schema pytest 4 passed; checked artifacts
  verified for four certificates, 76 local brackets, and `n=3,4,5,6`.
- **Retained failed checks:** the first Ruff format check requested one
  mechanical reformat. The first source wrapper reported 44 opening versus
  42 closing displays because it counted the two `\\[5pt]` row-spacing
  tokens; a line-anchored audit reports the correct 42/42 balance.
- **Interpretation:** no repository, static, source-structure, schema, or
  artifact regression remains.
- **Limitations:** repository tests and bounded checks do not independently
  prove EV-002.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---independent-audits-and-repository-verification`.

## EV-006 - Final Inspection

- **Date:** 2026-07-20
- **Method or command:** final `git status --short --branch`, complete
  tracked diff and untracked-file inspection, exact path and cache audit,
  `git diff --stat`, and repeated `git diff --check` after all durable-state
  updates.
- **Relevant output:** exactly five tracked files and the four expected
  dossier files are modified or new; no cache or bytecode file is present;
  the complete diff is confined to proof, durable memory, status, roadmap,
  and diagnostic evidence. The first whitespace check found one new blank
  line at EOF in `CURRENT_STATUS.md`; it was removed, and the final check
  passes.
- **Interpretation:** the bounded task is internally consistent, verified,
  and `READY_FOR_REVIEW`; the protected upstream and Git history remain
  untouched.
- **Limitations:** user review remains required.

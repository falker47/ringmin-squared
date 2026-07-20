# EVIDENCE - TASK-20260720 / PGE5 Singleton-Reversal Exact K

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | Git / source | Startup and source boundary | repository root / authoritative notes | VERIFIED |
| EV-002 | exact proof | Supported-map and exact induced-\(K\) theorem | `research/FIXED_ORDER_CYCLE_RATIO.md` | PROVED |
| EV-003 | bounded exact computation | Candidate-free max-plus and all-arcs audit | `exact_diagnostic.py` | PASS |
| EV-004 | documentation | Source roles, links, tags, and scope | project memory/status/roadmap | PASS |
| EV-005 | local verification | Dynamic and static repository checks | repository root | PASS |
| EV-006 | final inspection | Diff, status, whitespace, and cache hygiene | repository root | PASS |

## EV-001 - Startup And Source Boundary

- **Date:** 2026-07-20
- **Method or command:** `git status --short --branch`; `git rev-parse HEAD`;
  direct inspection of `AGENTS.md`, stable memory/status/roadmap,
  PGE5-1--PGE5-26, K825-6--K825-9, and KPGE5-1--KPGE5-30.
- **Relevant output:** clean `main` at
  `15ba9f9c58e8c7783ec2ad39d8eaa44b1be50318`; the requested singleton
  reversal is not the accepted monotone interval shift.
- **Interpretation:** the task starts from the requested reviewed baseline and
  is bounded to one new supported-map candidate.
- **Limitations:** source inspection alone proves neither support nor the
  induced-\(K\) formula.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---strict-startup-and-scope-isolation`.

## EV-002 - Symbolic Fixed-Core Theorem

- **Date:** 2026-07-20
- **Method:** literal image partition and PGE5 support check; exact
  isolated-hole identity; exhaustive nine-class deletion audit; compressed
  shortcuts by endpoint, length, middle role, doubleton, empty ranges, and
  cyclic cut; direct block sums and exact residue/comparator subtraction.
- **Relevant result:** KRPGE5-1--KRPGE5-32 prove that the map is supported,
  has \(W=W_n\), has sole argmax \(B_m\), and has
  \[
  K_*={1714m^3+2439m^2+24mq+965m+12q^2+60q+120\over6}.
  \]
  Exact cancellation proves
  \(K_\uparrow-K_*=(m-1)(m-2)(m-3)/3\), coefficient \(857/3000\), and a
  strict all-row K825 improvement.
- **Interpretation:** exact theorem for one prescribed supported cyclic core.
- **Limitations:** no statement about another bijection, permanent,
  production, angular threshold, geometry, global \(K\)-minimum, or global
  optimum.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---exact-support-argmax-and-score-theorem`.

## EV-003 - Independent Bounded Diagnostic

- **Date:** 2026-07-20
- **Command:**
  `python -B ops/TASK-20260720__pge5_singleton_reversal_exact_k/exact_diagnostic.py`.
- **Relevant output:** PASS; 29 max-plus/all-arcs rows
  (\(m=2,\ldots,30\)); 37,475,656 max-plus transitions; 968,774 proper
  oriented arcs; 999 formula/support rows through \(m=1000\); unique argmax
  \(B_m\); exact deletion and shortcut minima; target, residue, and K825
  checks all pass.
- **Method:** the optimizer fixes each possible least selected position and
  solves an increasing-position DAG without receiving \(B_m\). A separate
  modular traversal checks every raw arc, internal-hole budget, compressed
  shortcut, and cyclic-cut arc.
- **Interpretation:** independent bounded exact corroboration of the symbolic
  theorem and complete bounded argmax classification.
- **Limitations:** internal finite computation, not an all-\(m\) proof,
  external audit, artifact certificate, production path, or hosted CI. The
  accepted monotone comparator is reconstructed only for direct score
  cancellation.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---standalone-max-plus-and-all-arcs-diagnostic`.

## EV-004 - Document And Scope Synchronization

- **Date:** 2026-07-20
- **Method:** synchronized only the authoritative fixed-order proof note,
  compact stable memory, current status, roadmap, and this STRICT dossier;
  then scanned theorem tags, local links, next-task language, and prohibited
  scope claims.
- **Relevant result:** KRPGE5-1--KRPGE5-32 occur sequentially and exactly
  once; the stable-memory proof link and diagnostic path resolve; the roadmap
  contains one post-review audit; and no production, test, permanent,
  geometric, or global-optimality delta is claimed.
- **Interpretation:** document roles and task scope remain consistent with
  `AGENTS.md`.
- **Limitations:** document consistency alone proves no mathematical formula.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---durable-memory-and-document-audit`.

## EV-005 - Local Repository Verification

- **Date:** 2026-07-20
- **Methods or commands:** standalone diagnostic; scoped `ruff check` and
  `ruff format --check`; `python -m pytest -p no:cacheprovider`; focused
  checked-artifact schema pytest; `PYTHONPATH=src` checked-artifact verifier;
  KRPGE5 tag/link/scope audit; and `git diff --check`.
- **Relevant output:** diagnostic PASS; scoped Ruff PASS; full pytest
  `283 passed in 75.40s`; focused schema pytest `4 passed in 0.88s`; artifact
  verifier PASS for four certificates, 76 local brackets, and summary rows
  \(n=3,4,5,6\); document audit PASS; `git diff --check` emits no finding.
- **Interpretation:** the new standalone diagnostic is formatted and clean,
  all dynamic checks pass, and no tested or checked-artifact regression is
  present.
- **Limitations:** local execution is not the hosted Python 3.11--3.13 matrix;
  the task changes no production or test file.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---local-verification`.

## EV-006 - Final Inspection

- **Date:** 2026-07-20
- **Methods or commands:** `git status --short --branch`; `git diff
  --name-only`; `git diff --numstat`; `git diff --check`; task-directory
  listing; explicit untracked-file trailing-whitespace and cache scan; and
  `git rev-parse HEAD`.
- **Relevant output:** exactly four tracked role documents and the one
  four-file STRICT dossier are in scope; no production or test file changed;
  `git diff --check` emits no finding; task-file whitespace/cache scan PASS;
  HEAD remains the requested baseline
  `15ba9f9c58e8c7783ec2ad39d8eaa44b1be50318`.
- **Interpretation:** the complete delta is bounded, verified, hygienic, and
  ready for manual review.
- **Limitations:** no staging, commit, push, or hosted CI run was performed.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---final-inspection-and-handoff`.

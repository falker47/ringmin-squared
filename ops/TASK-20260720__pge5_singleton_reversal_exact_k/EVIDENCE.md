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
| EV-007 | exact proof | Label-one elimination and angular/geometric closure | `research/FIXED_ORDER_CYCLE_RATIO.md` | PROVED |
| EV-008 | bounded exact computation | Updated elimination and identity diagnostic | `exact_diagnostic.py` | PASS |
| EV-009 | local verification | Corrected working-tree repository checks | repository root | PASS |
| EV-010 | historical hosted CI | Pre-correction baseline Python 3.11--3.13 matrix | GitHub Actions run `29771633257` | PASS (HISTORICAL SHA ONLY) |
| EV-011 | historical final inspection | Pre-acceptance corrected-delta scope and hygiene | repository root | PASS (HISTORICAL) |
| EV-012 | accepted-baseline verification | Clean local reruns, exact-SHA hosted CI, and hygiene | repository root / GitHub Actions run `29777676234` | PASS |

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
- **Limitations:** this baseline item checked the fixed-core theorem only;
  it did not analyze the already available label-one/angular transfer. That
  omission is corrected, without altering this historical method, by EV-007.
  No statement about another bijection or permanent and no production change
  belongs to either delta.
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
- **Relevant result:** at the baseline checkpoint, KRPGE5-1--KRPGE5-32
  occurred sequentially and exactly once; the stable-memory proof link and
  diagnostic path resolved; and no production, test, or permanent delta was
  present. The later KRPGE5-33--KRPGE5-36 synchronization is audited
  separately in EV-011.
- **Interpretation:** this preserves the method and chronology of the
  original 32-tag document audit; it is not evidence for the later closure.
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

## EV-007 - Exact KRPGE5 Closure

- **Date:** 2026-07-20
- **Method:** direct application of the already proved exact label-one
  elimination (CR12p), strict fixed-order sandwich (CR22), strict global
  sandwich (CR27), and reduced global objective (CR28a) to the fixed core
  evaluated in (KRPGE5-1)--(KRPGE5-32). Two independent read-only
  mathematical audits rederived the chain.
- **Relevant result:** for every cyclic insertion gap \(g\),
  \[
  \Lambda\bigl(\sigma_{m,g}^{(5,*)}\bigr)=K_*,
  \qquad
  {K_*\over\pi}-(10m+4)^2
  <\rho_{\sigma_{m,g}^{(5,*)}}
  <{K_*\over\pi}.
  \]
  Therefore
  \[
  R_2^*(10m+4)<{\Lambda_{10m+4}\over\pi}\le {K_*\over\pi}
  \]
  and
  \[
  \limsup_{m\to\infty}
  {R_2^*(10m+4)\over(10m+4)^3}
  \le {857\over3000\pi}.
  \]
- **Classification:** exact theorem and exact geometric subsequence upper
  corollary, recorded as (KRPGE5-33)--(KRPGE5-36).
- **Limitations:** no equality \(\Lambda_{10m+4}=K_*\), minimizing-order or
  geometric-optimality theorem, matching global lower bound, all-\(n\)
  limsup bound, or exact leading constant for the global optimum \(R_2^*\).
  The exact \(\rho\) may depend on the insertion gap.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---correction-of-the-overbroad-non-consequence`.

## EV-008 - Updated Exact Diagnostic

- **Date:** 2026-07-20
- **Command:**
  `python -B ops/TASK-20260720__pge5_singleton_reversal_exact_k/exact_diagnostic.py`.
- **Relevant output:** PASS; 29 max-plus/all-arcs rows
  \(m=2,\ldots,30\); 37,475,656 max-plus transitions; 968,774 proper
  oriented arcs; all 4,727 label-one insertion gaps; all 484,387 possible
  distinct core-neighbor inequalities; and 999 formula/support rows through
  \(m=1000\). The coefficientwise \(n\)-form identity has exact tuple
  `(857000, 1219500, 12000, 482500, 6000, 30000, 60000)` on both sides.
- **Method:** the existing candidate-free core max-plus and independent
  all-arcs traversal are retained. New standard-library integer checks verify
  \(q=\lfloor(2n+7)/25\rfloor\), (KRPGE5-31) coefficientwise in \(m,q\),
  every literal insertion/deletion, the unchanged core-maximizer score, and
  all three cases (CR12m)--(CR12o).
- **Interpretation:** exact bounded corroboration of the label-one
  elimination hypotheses and an unbounded coefficientwise identity check.
- **Limitations:** the bounded insertion checks are not an all-\(m\) proof;
  the script intentionally performs no floating approximation of \(\pi\) and
  does not numerically certify CR22 or CR27.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---exact-closure-and-symbolic-checks`.

## EV-009 - Corrected Working-Tree Local Verification

- **Date:** 2026-07-20
- **Environment:** Python 3.14.3; pytest 9.0.2; Ruff 0.11.12;
  python-flint 0.9.0.
- **Initial sandbox attempt:**
  `$env:PYTHONDONTWRITEBYTECODE='1'; python -m pytest -p no:cacheprovider`
  exited 1 with `252 passed, 31 errors in 62.63s`. Every error was a setup
  `PermissionError` for pytest's `tmp_path` under
  `AppData\Local\Temp\pytest-of-Falker`.
- **Sandbox basetemp retry:**
  `$env:PYTHONDONTWRITEBYTECODE='1'; python -m pytest -p no:cacheprovider
  --basetemp=C:\tmp\ringmin-squared-krpge5-pytest-019f8117` exited 1 with
  `252 passed, 31 errors in 68.25s`; creation of the requested basetemp was
  likewise denied. These are retained environmental failures, not test
  failures in the repository.
- **Approved local rerun:**
  `$env:PYTHONDONTWRITEBYTECODE='1'; python -m pytest -p no:cacheprovider`
  outside the restrictive sandbox completed with `283 passed in 71.94s`.
- **Focused checks:**
  `$env:PYTHONDONTWRITEBYTECODE='1'; python -m pytest -p no:cacheprovider
  tests\test_checked_artifact_schema_validation.py` gave `4 passed in
  0.92s`; `$env:PYTHONDONTWRITEBYTECODE='1'; python -m pytest -p
  no:cacheprovider tests\test_n3_arb_interval_crosscheck.py` gave `3 passed
  in 0.08s`.
- **Checked-artifact verifier:**
  `$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='src'; python -m
  power_ringmin.verify_checked_artifacts` verified four certificates, 76
  local brackets, and the summary rows \(n=3,4,5,6\).
- **Static task-local checks:** `python -m ruff check` and `python -m ruff
  format --check` on `exact_diagnostic.py` both passed; the final standalone
  diagnostic rerun also passed after the coefficientwise check was added.
- **Interpretation:** the corrected local working tree passes the full
  repository suite and all canonical focused verification. No production or
  test file changed.
- **Limitations:** this is local Python 3.14.3 verification, not hosted CI.

## EV-010 - Hosted CI On The Pre-Correction Baseline (Historical)

- **Date:** 2026-07-20
- **Method:** independent inspection of GitHub Actions run metadata, jobs,
  and recorded step conclusions through the connected GitHub data and REST
  result.
- **Run:** [Verification `29771633257`](https://github.com/falker47/ringmin-squared/actions/runs/29771633257),
  event `push`, commit
  `bce6e4d8a935bd9d8509e59b760cf78c345779b6`, started
  `2026-07-20T19:21:17Z`, completed `2026-07-20T19:22:52Z`, conclusion
  `success`.
- **Relevant result:** the Python 3.11, 3.12, and 3.13 jobs all succeeded;
  each recorded full pytest, checked-artifact verification, schema pytest,
  and trailing-whitespace steps as successful.
- **Interpretation:** hosted CI independently verifies the reviewed
  KRPGE5-1--KRPGE5-32 baseline commit.
- **Limitation:** the run covers only `bce6e4d8...`; it does not cover the
  KRPGE5-33--KRPGE5-36 correction later accepted in `a15a4d34...`.
- **Current-status note:** this was the correct limitation when recorded.
  EV-012 now supplies separate hosted provenance for the later accepted
  commit; this run remains tied only to `bce6e4d8...` and is not reused.

## EV-011 - Corrected-Delta Final Inspection (Historical)

- **Date:** 2026-07-20
- **Methods or commands:** independent read-only final-diff audit; exact
  KRPGE5 tag-sequence and document-scope Python audit; changed-file scope
  assertion; `git status --short --branch`; `git diff --name-only`; complete
  diff inspection; and `git diff --check`.
- **Relevant output:** (KRPGE5-1)--(KRPGE5-36) are unique and sequential;
  the proof section no longer contains the superseded categorical
  angular/geometric negation; proof, stable memory, status, roadmap, and
  dossier references agree. Exactly eight authorized documentation/dossier
  files are modified, including the task-local diagnostic; no `src/` or
  `tests/` path changed. The independent final audit found no mathematical,
  document-role, diagnostic, or provenance defect. `git diff --check` emits
  no finding.
- **Failed audit formulations retained as evidence:** the first tag command
  used an overescaped regular expression and returned an empty tag list; a
  later composite command incorrectly required the literal range string in
  every evidence file. Both commands failed by assertion because of their
  audit predicates. Corrected patterns then passed and required no project-
  content repair.
- **Interpretation:** the task delta is coherent, hygienic, locally verified,
  and `READY_FOR_REVIEW`; the user retains manual commit authority.
- **Limitations:** the Git status commands emitted a permission warning for
  the user's global ignore file, without preventing tracked-diff inspection.
  That hosted baseline result remained separate and did not cover the
  correction later accepted in `a15a4d34...`.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---corrected-delta-final-inspection-and-handoff`.

## EV-012 - Accepted-Commit Post-Review Verification

- **Date:** 2026-07-20
- **Accepted baseline:** commit
  `a15a4d34cc034b669f02382e2e4f27b4822ed382`, title
  `Correct the KRPGE5 geometric closure`; `HEAD`, `main`, and `origin/main`
  agreed before verification. Its tree object is
  `2543f29f79968d8b09144acf20d1f7e0339c1685`.
- **Clean-state methods:** `git rev-parse HEAD`; `git rev-parse origin/main`;
  `git status --porcelain=v1 --untracked-files=all`; and `git status
  --short --branch` before and after the requested checks.
- **Clean-state result:** exact accepted SHA, branch `main...origin/main`, and
  empty porcelain status throughout the baseline run.
- **KRPGE5 command:**
  `python -B ops/TASK-20260720__pge5_singleton_reversal_exact_k/exact_diagnostic.py`.
- **KRPGE5 result:** exit 0, PASS in about 17.18 seconds; 29 max-plus/all-arcs
  rows \(m=2,\ldots,30\); 37,475,656 transitions; 968,774 proper arcs;
  4,727 insertion gaps; 484,387 distinct neighbor-pair inequalities; and
  999 formula/support rows through \(m=1000\). The exact coefficient tuple
  was `(857000, 1219500, 12000, 482500, 6000, 30000, 60000)` and no
  floating-\(\pi\) check was performed.
- **Repository commands and results:** `python -m pytest` exited 0 with
  `283 passed in 73.82s`; `$env:PYTHONPATH='src'; python -m
  power_ringmin.verify_checked_artifacts` exited 0 after verifying four
  certificates, 76 local brackets, and summary rows \(n=3,4,5,6\);
  `python -m pytest tests\test_checked_artifact_schema_validation.py`
  exited 0 with `4 passed in 0.80s`.
- **Local environment:** Python 3.14.3 and pytest 9.0.2.
- **Clean-commit hygiene:** `git diff --check` and `git diff --check
  a15a4d34cc034b669f02382e2e4f27b4822ed382^
  a15a4d34cc034b669f02382e2e4f27b4822ed382` emitted no finding;
  `git grep -n -I -E '[[:blank:]]+$' -- .` returned the expected no-match
  exit 1; the tracked cache/bytecode path scan was empty; post-check porcelain
  status remained empty.
- **Retained command-construction failure:** the first unquoted PowerShell
  invocation of `git rev-parse a15a4d3...^{tree}` treated `{tree}` as shell
  syntax and exited 1. Quoting the complete revision corrected the query and
  returned the tree object above; this was a command parsing error, not a
  repository failure.
- **Hosted method:** exact-SHA-filtered GitHub Actions REST inspection, then
  direct run and latest-jobs inspection for run `29777676234`. No run for
  `bce6e4d8a935bd9d8509e59b760cf78c345779b6` was queried or reused.
- **Hosted run:** [Verification `29777676234`](https://github.com/falker47/ringmin-squared/actions/runs/29777676234),
  workflow `.github/workflows/verification.yml`, run number 90, event
  `push`, branch `main`, attempt 1, exact `head_sha`
  `a15a4d34cc034b669f02382e2e4f27b4822ed382`, created and started
  `2026-07-20T20:48:56Z`, updated `2026-07-20T20:50:36Z`, status
  `completed`, conclusion `success`.
- **Hosted jobs:** Python 3.11 job `88470931481`, Python 3.12 job
  `88470931399`, and Python 3.13 job `88470931382` all completed with
  conclusion `success`. In every job, full pytest, checked-artifact semantic
  verification, focused schema pytest, and tracked-text trailing-whitespace
  steps completed successfully.
- **Classification:** the diagnostic is bounded exact corroboration; the
  local repository checks and clean-commit hygiene are verified facts; the
  exact-SHA hosted run is a hosted verified fact. No new theorem,
  construction, or mathematical classification is inferred.
- **Interpretation:** the accepted KRPGE5 baseline has fresh local verification
  and independent hosted Python 3.11--3.13 verification with exact commit
  provenance. EV-010 remains historical and is not promoted to this SHA.
- **Limitations:** the hosted result does not independently audit GitHub or
  its runners, and the bounded diagnostic is not an all-\(m\) proof. The
  later documentation-only recording delta is outside the accepted commit
  and is checked separately by final diff and hygiene inspection.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-20---accepted-commit-post-review-state-and-provenance-closure`.

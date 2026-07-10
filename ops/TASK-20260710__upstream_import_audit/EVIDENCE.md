# EVIDENCE - TASK-20260710 / Upstream Import Audit

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | command/source | Startup and local state | project root | Startup files read; local tree clean |
| EV-002 | command | Upstream identity and file map | upstream Ringmin | Valid clean Git repo; tracked asset map inspected |
| EV-003 | source | Source and test audit | upstream `src/`, `tests/`, `verify.py` | Reusable core and hard-coded original-radii assumptions identified |
| EV-004 | source | Scripts, results, and math assets | upstream scripts/results/docs/paper | Certification pipeline and reference-only assets classified |
| EV-005 | file | Local documentation updates | Power-Ringmin docs/dossier | Import recommendation recorded |
| EV-006 | command | Final verification | project root and upstream | Upstream clean; local diff inspected; whitespace checks passed |

## EV-001 - Startup And Local State

- **Date:** 2026-07-10
- **Method or command:** `Get-Location`
- **Relevant output:** `C:\Users\Falker\Desktop\Code\circle\ringmin-squared`.
- **Method or command:** `git status --short`
- **Relevant output:** no output.
- **Method or command:** `Get-Content -LiteralPath AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `UPSTREAM_RINGMIN.md`, and prior bootstrap task files.
- **Relevant output:** required startup and relevant memory files were read.
- **Interpretation:** The audit began from the intended repository root with no unrelated uncommitted local changes.
- **Limitations:** This does not inspect upstream content beyond previously recorded provenance.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---startup-and-dossier-creation`

## EV-002 - Upstream Identity And File Map

- **Date:** 2026-07-10
- **Method or command:** `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin -c core.excludesfile= rev-parse --show-toplevel`
- **Relevant output:** `C:/Users/Falker/Desktop/Code/circle/ringmin`.
- **Method or command:** `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin -c core.excludesfile= rev-parse HEAD`
- **Relevant output:** `cc0327400819fe06b230d967cdcbafffe1648317`.
- **Method or command:** `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin -c core.excludesfile= remote -v`
- **Relevant output:** `origin https://github.com/falker47/ringmin.git (fetch)` and `(push)`.
- **Method or command:** `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin -c core.excludesfile= status --short`
- **Relevant output:** no output.
- **Method or command:** `rg --files`; `git ... ls-files results paper_assets figures scripts tests src verify.py pyproject.toml README.md REPORT.md LICENSE CITATION.cff requirements.txt`
- **Relevant output:** tracked files include `src/ringmin/*.py`, `tests/*.py`, `scripts/*.py`, `verify.py`, certified `results/`, `paper_assets/`, `README.md`, `REPORT.md`, `LICENSE`, `CITATION.cff`, `pyproject.toml`, and `requirements.txt`.
- **Interpretation:** Upstream Ringmin is a valid clean Git repository and its tracked asset classes were inspected read-only.
- **Limitations:** File-map inspection does not prove correctness of any mathematical or computational claim.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---upstream-structure-and-source-audit`

## EV-003 - Source And Test Audit

- **Date:** 2026-07-10
- **Method or command:** `Get-Content` on upstream `src/ringmin/geometry.py`, `evaluator.py`, `search.py`, `crosscheck.py`, `highprec.py`, `patterns.py`, `artifacts.py`, `cli.py`, `plots.py`, `tests/test_m0.py`, `tests/test_m1.py`, `tests/conftest.py`, `verify.py`, `pyproject.toml`, `requirements.txt`, and `LICENSE`.
- **Relevant output:** `geometry.py` defines `theta`, radius validation, cyclic pairs, and cycle-equivalence. `evaluator.py` implements all-pairs STN feasibility, full fixed-order radius bisection, witness recovery, Cartesian validation, essential tight pairs, and floating-circle detection. `highprec.py` implements mpmath STN checks. `patterns.py` provides generic order constructors including Supnick helpers. `search.py` has generic `*_values` entry points but also default `range(1,n+1)` wrappers and `lb3` removals of `1` and `2`. `crosscheck.py` has a fixed-order generic SLSQP helper and a global helper hard-coded to `range(1,n+1)`.
- **Method or command:** `rg -n "range\\(1, n \\+ 1\\)|tuple\\(range\\(1|without_1|without_1_2|\\{1, 2\\}|results/n|n\\{n:02d\\}" src tests scripts verify.py README.md REPORT.md paper_assets\\ringmin_paper.tex`
- **Relevant output:** found original-radii assumptions in tests, search wrappers, search lower-bound components, verifier paths/bounds, scripts, docs, and paper assets.
- **Interpretation:** The code foundation is partially reusable for arbitrary radius values, but a trustworthy quadratic import requires explicit sequence-aware refactors and tests.
- **Limitations:** No tests were run in upstream because running tests could update caches in the read-only upstream repository.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---upstream-structure-and-source-audit`

## EV-004 - Scripts, Results, And Math Assets

- **Date:** 2026-07-10
- **Method or command:** `Get-Content` and `rg -n` on upstream scripts, `results/n03/optimum.json`, `results/n14/certificate.txt`, `results/frontiers/n14_frontier.json`, `results/heuristic/schema.json`, `results/highprec.csv`, `results/patterns_table.csv`, `README.md`, `REPORT.md`, and `paper_assets/ringmin_paper.tex`.
- **Relevant output:** `sweep_certified.py`, `highprec_verify.py`, `extract_frontiers.py`, `calibrate_float64.py`, and `verify.py` form the original certification/regeneration pipeline. Result artifacts store original-radii optima, witness positions, high-precision radii, essential pairs, floating circles, frontier metadata, and provenance fields. Paper source contains the angular reformulation, STN feasibility description, Supnick/anti-Monge chain theorem stated for arbitrary distinct radii, floating/pocket definitions, certificate semantics, original certified finite results, original heuristics, and bibliography.
- **Interpretation:** The pipeline pattern is valuable, but original result artifacts are prior-work references, not quadratic-radii results. Mathematical assets should be imported with classification and local review before becoming Power-Ringmin claims.
- **Limitations:** This was a source/document audit; no independent recomputation of upstream certificates was performed.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---upstream-structure-and-source-audit`

## EV-005 - Local Documentation Updates

- **Date:** 2026-07-10
- **Method or command:** local file edits through patch.
- **Relevant output:** updated `UPSTREAM_RINGMIN.md` with the import audit, minimum coherent import set, exclusions, required adaptations, and priority order; updated `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, and this task dossier.
- **Interpretation:** The audit output is stored in durable project files.
- **Limitations:** Final Git and whitespace checks are recorded separately after edits.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---import-recommendation-recorded`

## EV-006 - Final Verification

- **Date:** 2026-07-10
- **Method or command:** `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin -c core.excludesfile= status --short`
- **Relevant output:** no output.
- **Method or command:** `git status --short`
- **Relevant output:** modified local files: `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, `UPSTREAM_RINGMIN.md`; new local dossier: `ops/TASK-20260710__upstream_import_audit/`.
- **Method or command:** `git diff --stat`
- **Relevant output:** tracked-file diff shows updates to `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, and `UPSTREAM_RINGMIN.md`.
- **Method or command:** `git diff`
- **Relevant output:** inspected tracked diff for status, knowledge, and upstream provenance updates.
- **Method or command:** `git diff --check`
- **Relevant output:** no output.
- **Method or command:** `rg -n "[ \\t]+$" UPSTREAM_RINGMIN.md PROJECT_KNOWLEDGE.md CURRENT_STATUS.md ops\TASK-20260710__upstream_import_audit\TASK_STATUS.md ops\TASK-20260710__upstream_import_audit\TASK_LOG.md ops\TASK-20260710__upstream_import_audit\EVIDENCE.md`
- **Relevant output:** no matches; command returned exit code 1, which is ripgrep's no-match status.
- **Interpretation:** Upstream remained unmodified; local changes are scoped to audit documentation and task memory; whitespace checks passed.
- **Limitations:** No code tests were run because this task imported no code and changed no executable behavior.
- **Linked log entry:** `TASK_LOG.md#2026-07-10---final-verification`

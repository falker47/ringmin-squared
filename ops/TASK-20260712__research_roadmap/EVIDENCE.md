# EVIDENCE - TASK-20260712__research_roadmap / Research Roadmap

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | file / command | Startup and source review | startup files, prior dossiers, checked summaries, workflow, Git status | PASS |
| EV-002 | file | Roadmap and durable-memory updates | `research/NEXT_RESEARCH_STEPS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md` | PASS |
| EV-003 | command | Markdown and repository hygiene | Markdown checks, whitespace scan, checked-artifact verifier, Git diff checks | PASS |

## EV-001 - Startup And Source Review

- **Date:** 2026-07-12
- **Method or command:** `Get-Content -Raw AGENTS.md`; `Get-Content -Raw start.md`; `Get-Content -Raw PROJECT_KNOWLEDGE.md`; `Get-Content -Raw CURRENT_STATUS.md`.
- **Relevant output:** Required startup files were read.
- **Method or command:** `git status --short`.
- **Relevant output:** Initial command produced no entries.
- **Method or command:** `git rev-parse HEAD`; `git log -3 --oneline`.
- **Relevant output:** Current `HEAD` was `4da593e5751850be3eb7e9ed7e4c3d8182aeecb8`; recent commits were `4da593e Fix generic template trailing whitespace`, `953b609 Normalize finite-results source digests`, and `92d6017 Harden checked-artifact verification trust layer and add CI`.
- **Method or command:** Read `research/FINITE_RESULTS.md`, `ops/TASK-20260712__critical_constraints_order_structure/EVIDENCE.md`, `ops/TASK-20260712__cross_platform_finite_hash_ci/EVIDENCE.md`, `.github/workflows/verification.yml`, and the machine-readable finite-results and critical-structure artifacts.
- **Relevant output:** Candidate counts for `n=3..6` are `1,1,2,5`; exclusion gaps are undefined, `0.1171644705802874497635457373689860105514526367187500`, `0.1137866156209259571596703608520328998565673828125`, and `0.0488707956703002821541304001584649085998535156250`; shared lower cores for multiple-candidate cases are supported on indices `2..n`.
- **Method or command:** `$env:PYTHONPATH='src'; python -c "from power_ringmin.search_small_n import canonical_index_order_count; print({n: canonical_index_order_count(n) for n in range(3,8)})"`.
- **Relevant output:** `{3: 1, 4: 3, 5: 12, 6: 60, 7: 360}`.
- **Interpretation:** Existing evidence supports a structural roadmap and shows `n=7` is a larger enumeration step requiring a precise discriminator.
- **Limitations:** Hosted GitHub Actions green status was user-provided context and was not independently queried. The `n=7` count probe generated no certificate or output artifact.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---startup-and-evidence-review`

## EV-002 - Roadmap And Memory Updates

- **Date:** 2026-07-12
- **Method or command:** File edits using `apply_patch`.
- **Relevant output:** Added `research/NEXT_RESEARCH_STEPS.md`.
- **Relevant output:** Updated `start.md` to mention the checked-artifact verification pipeline and user-reported green hosted workflow context.
- **Relevant output:** Updated `PROJECT_KNOWLEDGE.md` to replace the stale hosted-CI limitation, add the roadmap as current stable research memory, and record the conditions under which `n=7` would be worth considering.
- **Relevant output:** Updated `CURRENT_STATUS.md` to point to the reduced-core insertion task and explicitly defer `n=7` generation/preflight.
- **Interpretation:** Durable project memory now aligns with the post-CI-fix research-planning state and does not recommend automatic enumeration.
- **Limitations:** The roadmap is a planning artifact; it proves no exact optimum, exact tie, all-`n` theorem, or asymptotic theorem.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---roadmap-draft-and-memory-alignment`

## EV-003 - Markdown And Repository Hygiene

- **Date:** 2026-07-12
- **Method or command:** Custom Markdown required-section check over `research/NEXT_RESEARCH_STEPS.md`, `CURRENT_STATUS.md`, `PROJECT_KNOWLEDGE.md`, `start.md`, and the task dossier files.
- **Relevant output:** `markdown required-section check passed: 17 items; utf8 files: 7`.
- **Method or command:** Custom Markdown path-reference check over the same files.
- **Relevant output:** `markdown path-reference check passed: 60 refs`.
- **Method or command:** `rg -n "[ \t]+$" start.md PROJECT_KNOWLEDGE.md CURRENT_STATUS.md research\NEXT_RESEARCH_STEPS.md ops\TASK-20260712__research_roadmap`.
- **Relevant output:** `no trailing whitespace`.
- **Method or command:** `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`.
- **Relevant output:** `verified checked artifacts certificates=4 local_brackets=76 summary=examples/finite_results_summary_n3_n6.json summary_n_values=3,4,5,6`.
- **Method or command:** `git diff --check`.
- **Relevant output:** Produced no output.
- **Method or command:** `git status --short`; `git diff --stat`; tracked diff inspection.
- **Relevant output:** Final status and diff were inspected.
- **Interpretation:** Markdown coverage, local path references, checked finite artifact verification, and repository hygiene checks passed.
- **Limitations:** Two initial Markdown checker attempts failed because PowerShell interpreted backticks and command-like inline code; corrected checks passed. Full `pytest` was not run because this task changed documentation and task memory only.
- **Linked log entry:** `TASK_LOG.md#2026-07-12---verification-and-handoff`

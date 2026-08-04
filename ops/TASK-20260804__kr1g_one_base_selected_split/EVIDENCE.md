# EVIDENCE - TASK-20260804 / KR1G One Base Selected Split

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | Startup and source isolation | repository sources; Git | PASS |
| EV-002 | proof / audit | Exact one-base theorem and fixed-\(k\) cubic decision | authoritative proof | PASS |
| EV-003 | code / computation | Independent exact recursive-topology checker | `exact_checker.py` | PASS |
| EV-004 | test / regression | Repository and prior KR1G regressions | repository commands | PASS |
| EV-005 | source / diff audit | Final proof, documentation, and diff verification | changed files; Git | PASS |

## EV-001 - Startup and source isolation

- **Date:** 2026-08-04
- **Method or command:** read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, the relevant KR1G
  proof context, and the fixed-count and variable-count dossiers; inspect
  `git rev-parse HEAD` and `git status --short --branch` before task edits.
- **Relevant output:** baseline
  `943a841d46424cf2c22fe3d80be2e88438b32262` was clean. Later status output
  may contain only the active task's parallel, task-scoped edits.
- **Interpretation:** the STRICT task began without unrelated uncommitted
  changes and is bounded to the exactly-one-base selected class.
- **Limitations:** this establishes source isolation, not the new theorem or
  any computational check.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---strict-startup-and-one-base-class-isolation`.

## EV-002 - Exact one-base theorem and fixed-k cubic decision

- **Date:** 2026-08-04
- **Method or command:** direct exact specialization of KR1G-89--KR1G-98;
  independent read-only mathematical audit of the prefix count, Bellman
  quantifiers, recursive-energy identity, floor/ceiling errors, finite
  denominator, and fixed-\(k\) limit.
- **Relevant output:** KR1G-114--KR1G-123 force the unique base label
  \(t=r-1\), prove
  \(A^{(q)}_{\ell,1}=q\ell!\) and
  \(|\Pi^{(1{\rm B})}_{q,\ell}|=q!\ell!/2\), and retain KR1G-91b as the
  exact finite minimum over arbitrary completions. The recursive terms obey
  \[
  \mathcal E_{\mathcal R}(h)
  =\sum_{\rho=s}^{r-2}E_{{\rm cov},\rho}(h)
   +K^{(1{\rm B})}_{k,n},
  \]
  and KR1G-98 gives the finite bound KR1G-120. Exact floor/ceiling limits
  prove
  \[
  {K^{(1{\rm B})}_{k,n}\over n^3}\to\Theta^{(1{\rm B})}_k
  \ge{(a-\beta_k)\lambda_k(1-a)^2\over2(2-\lambda_k)}>0.
  \]
- **Interpretation:** for every fixed \(k\), the minimum complete residual
  normalized by \(n^3\) has positive liminf. Hence no compatible subcubic
  family exists in the exactly-one-base class.
- **Limitations:** \(\Theta_k^{(1{\rm B})}\) is the exact limit of the
  retained deterministic lower bound, not an exact coefficient of the
  unknown residual minimum. The theorem excludes generic
  \(2\le b^{\rm base}_{k,n}=o(n)\), \(k=k(n)\), and geometry.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---one-base-theorem-and-independent-proof-audit`.

## EV-003 - Independent exact recursive-topology checker

- **Date:** 2026-08-04
- **Method or command:** `python -B
  ops\TASK-20260804__kr1g_one_base_selected_split\exact_checker.py`;
  `python -m ruff check
  ops\TASK-20260804__kr1g_one_base_selected_split\exact_checker.py`;
  `python -m ruff format --check
  ops\TASK-20260804__kr1g_one_base_selected_split\exact_checker.py`.
- **Relevant output:** the checker reports 216 `BRRR` prefixes, the exact
  global formula \(q!\ell!/2=4{,}354{,}560\), 39,312 completions, recursive
  depth histogram \((324,252,72)\), 72 sibling histories, 108 balanced
  histories, and 180 inserted--inserted targets. It obtains
  \(K_{\rm det}=8333/140\), uniform bound \(17191/280\),
  topology-sensitive minimum bound \(18591/280\), and matching literal and
  Bellman residual minimum \(3464/35\). The checker prints `PASS`; Ruff
  reports `All checks passed!` and `1 file already formatted`.
- **Interpretation:** fresh exact arithmetic corroborates the global count,
  KR1G-91b, every KR1G-93 component, the KR1G-118/119 deterministic sum,
  KR1G-94, and the recursive-term-preserving one-base KR1G-98 bound across
  nontrivial recursive topologies and arbitrary two-label completion.
- **Limitations:** bounded finite enumeration cannot replace the symbolic
  all-\(q\) or asymptotic proof. The synthetic rational fixture enumerates
  one of 20,160 base cycles and is not a rounded irrational all-middle row.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---independent-one-base-recursive-topology-checker`.

## EV-004 - Repository and prior KR1G regressions

- **Date:** 2026-08-04
- **Method or command:** `python -m pytest -p no:cacheprovider`;
  `python -m pytest tests\test_n3_arb_interval_crosscheck.py -p
  no:cacheprovider`; `python -m pytest
  tests\test_checked_artifact_schema_validation.py -p no:cacheprovider`;
  `$env:PYTHONPATH='src'; python -m
  power_ringmin.verify_checked_artifacts`; and the standalone fixed-count,
  variable-count, and historical one-recursive KR1G checker commands.
- **Relevant output:** 283 repository tests pass in 65.95 seconds; 3 focused
  Arb tests and 4 focused schema tests pass; all 4 checked artifacts and 76
  local brackets verify with summary rows \(3,4,5,6\). The fixed-count
  checker passes 15,120 selected prefixes, 151,200 completions, its
  42-prefix/4,620-completion Bellman fixture, and 1,296 position-sweep
  histories. The variable-count order-statistic checker and the historical
  one-recursive checker, covering 96,600 broad histories plus 6,720
  completions, also pass.
- **Interpretation:** the proof/checker/documentation extension preserves the
  production, certification, schema, and preceding KR1G verification layers.
- **Limitations:** local regression success would not replace the new
  mathematical proof or hosted verification of a later committed revision.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---repository-and-prior-kr1g-regressions`.

## EV-005 - Final proof, documentation, and diff verification

- **Date:** 2026-08-04
- **Method or command:** exact equation-tag uniqueness audit; local target
  and heading-anchor checks; strict UTF-8, BOM, CR/LF, final-LF,
  trailing-whitespace, display, `aligned`, and `array` balance audits over all
  eight task files; direct inspection of every tracked diff and untracked
  dossier file; `git status --short --branch`; `git diff --stat`; complete
  `git diff --color=never`; and `git diff --check`.
- **Relevant output:** all 1,090 equation tags are unique. All eight files
  are strict UTF-8 without BOM or CR, end in LF, contain no trailing
  whitespace, and have balanced math delimiters. Both new local targets and
  the unique proof heading resolve. The complete proof, memory, roadmap,
  current-status, checker, and dossier contents were inspected; final
  `git diff --check` passes. One preliminary combined balance command exited
  with code 1 solely because bare `rg` uses that code for a successful
  no-match trailing-whitespace result; the corrected wrapper explicitly
  accepted exit 1 as zero matches and passed with `trailing_matches=0`.
- **Interpretation:** proof, stable memory, roadmap, current truth, task
  chronology, verification evidence, and exact checker agree. The task is
  `READY_FOR_REVIEW` for the user's manual commit decision.
- **Limitations:** untracked dossier files require direct inspection in
  addition to ordinary Git diff output; hosted CI cannot cover an
  uncommitted working tree.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---final-documentation-and-review-handoff`.

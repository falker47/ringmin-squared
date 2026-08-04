# EVIDENCE - TASK-20260804 / KR1G Fixed Recursive Count

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | Startup and source isolation | repository sources; Git | PASS |
| EV-002 | proof / computation | Fixed-\(p\) finite theorem | authoritative proof | PASS |
| EV-003 | code / computation | Independent exact \(p=2\) checker | `exact_checker.py` | PASS |
| EV-004 | test / audit | Repository and final-diff verification | repository commands | PASS |

## EV-001 - Startup and source isolation

- **Date:** 2026-08-04
- **Method or command:** read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, the relevant
  KR1G proof sections, and the preceding dossier; run `git status
  --short --branch` and `git rev-parse HEAD`.
- **Relevant output:** the accepted baseline is
  `069cb677278fc149e2f8fac49b43d3346949c19e`; the startup worktree was
  clean.
- **Interpretation:** no unrelated uncommitted work is mixed into this
  STRICT task.
- **Limitations:** this establishes local source state, not hosted CI state.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---strict-startup-and-fixed-count-isolation`.

## EV-002 - Fixed-p finite theorem

- **Date:** 2026-08-04
- **Method or command:** exact derivation from KR1G-5--KR1G-6; dynamic
  selected-prefix count; original-cycle deviation partition; simultaneous
  weighted Cauchy; two independent read-only proof audits; direct Python
  check of the \((q,\ell,p)=(7,3,2)\) recurrence and completion count.
- **Relevant output:** with \(|\mathcal R|=p\),
  \(m_p=q-\ell+p\),
  \(T^{(-\mathcal R)}=T-\sum_{\rho\in\mathcal R}d_\rho\), and
  \(Q^{(-\mathcal R)}=Q-\sum_{\rho\in\mathcal R}4/(2-\lambda_\rho)\),
  KR1G-98 gives
  \[
  \mathscr R_{k,n}(h)
  \ge\mathcal E_{\mathcal R}(h)
  +{(T^{(-\mathcal R)}_{k,n})^2\over
  Q^{(-\mathcal R)}_{k,n}+2m_p}.
  \]
  Every recursive term is nonnegative at arbitrary depth. The exact
  denominator identity yields KR1G-99, and fixed \((p,k)\) gives
  \(\tau_k^2/(\chi_k+2\mu_k)>0\) after \(n\to\infty\). The direct count
  check returned `42 15120 151200`: 42 target histories per canonical
  \(q=7\) cycle, 15,120 selected prefixes, and 151,200 one-label
  completions.
- **Interpretation:** the same universal lower-bound coefficient as the
  all-base theorem survives for every fixed \(p\), before the later
  \(k\to\infty\) limit.
- **Limitations:** there is no uniform threshold in \(p\) or \(k\), no
  theorem for \(p=p(n)\) or \(k=k(n)\), no exact residual-infimum claim,
  and no geometric or minimizing-order consequence.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---fixed-p-finite-theorem-and-cubic-bound`.

## EV-003 - Independent exact p=2 checker

- **Date:** 2026-08-04
- **Method or command:**
  `python ops\TASK-20260804__kr1g_fixed_recursive_count\exact_checker.py`;
  `python -m ruff check
  ops\TASK-20260804__kr1g_fixed_recursive_count\exact_checker.py`;
  `python -m ruff format --check
  ops\TASK-20260804__kr1g_fixed_recursive_count\exact_checker.py`.
- **Relevant output:** the two-segment fixture reports 360 cycles, 181,440
  raw selected histories, 15,120 retained \(p=2\) prefixes, and 151,200
  completions. Its three topology classes have 5,040 histories each;
  5,040 selected targets and 30,240 completion targets have two inserted
  endpoints. Exact locked values are residual \(823/14\),
  position-sensitive bound \(21148/665\), and uniform bound \(81/5110\).
  The position sweep reports 2,520 raw and 1,296 retained histories with
  BBRR/BRBR/BRRB counts 720/360/216, relation counts 288 sibling, 576
  nested, and 432 different-root, plus 288 two-inserted targets. Its locked
  values are \(260/3\), \(589/21\), and \(25/24\). The checker prints PASS;
  Ruff lint and format checks pass.
- **Interpretation:** exact rational enumeration independently corroborates
  the generalized local identities, full KR1G-6 decomposition,
  nonnegativity, \(m_p\) partition, \(T,Q\) coordinate removal, radical and
  combined Cauchy, uniform positive-part bound, and arbitrary-completion
  recursion.
- **Limitations:** the fixtures are bounded and rational; they are not
  rounded irrational all-middle rows and do not prove the all-\(q\) or
  asymptotic theorem. Their locked residual minima are fixture diagnostics,
  not exact infimum claims for the theorem's history classes.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---independent-exact-p2-checker`.

## EV-004 - Repository and final-diff verification

- **Date:** 2026-08-04
- **Method or command:** `python -m pytest -p no:cacheprovider`;
  `$env:PYTHONPATH='src'; python -m
  power_ringmin.verify_checked_artifacts`; `python -m pytest
  tests\test_checked_artifact_schema_validation.py -p no:cacheprovider`;
  both recursive checker commands; Ruff commands from EV-003; exact
  recurrence and SymPy denominator identities; final equation-tag, display,
  roadmap/dossier-link, UTF-8/LF, trailing-whitespace, Git status, complete
  diff, and `git diff --check` audits.
- **Relevant output:** 283 tests pass in 65.79 seconds; all four checked
  artifacts pass with 76 local brackets and summary rows \(3,4,5,6\); all
  four focused schema tests pass. The new \(p=2\) and preceding \(p=1\)
  checkers pass, and Ruff reports no lint or format issue. Exact checks pass
  for the KR1G-89 \(p=0,p=1\) reductions and the \(p=2\) denominator
  identity. All 1,066 equation tags are unique; 40 Markdown links resolve,
  including 25 anchors; all eight changed text/code files are strict UTF-8
  without BOM or CR, end in LF, have balanced display/aligned delimiters,
  and contain no trailing whitespace. Final Git diff checks pass.
- **Interpretation:** the proof, stable memory, roadmap, status, independent
  checker, and unchanged production verification layer are consistent.
- **Limitations:** the first display-balance invocation counted every inline
  `\[`/`\]` occurrence in the long pre-existing proof and produced a false
  failure. The corrected audit counts exact display-delimiter lines and
  passes; the invocation defect did not expose a source defect. All checks
  are local rather than hosted CI, and bounded checker enumeration does not
  replace the symbolic theorem.
- **Linked log entry:**
  `TASK_LOG.md#2026-08-04---repository-verification-and-handoff`.

# EVIDENCE - TASK-20260724 / KR1G One Recursive Selected Split

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | Startup and source isolation | repository sources; Git | PASS |
| EV-002 | proof / computation | One-recursive finite theorem | authoritative proof | PASS |
| EV-003 | code / computation | Independent exact checker | `exact_checker.py` | PASS |
| EV-004 | test / audit | Repository and final diff verification | repository commands | PASS |

## EV-001 - Startup and source isolation

- **Date:** 2026-07-24
- **Method or command:** read the operating contract and all required memory,
  proof, roadmap, and prior-dossier sources; run `git rev-parse HEAD` and
  `git status --short`.
- **Relevant output:** HEAD is the user-accepted baseline
  `7665e31a51a051669f73b32fda41e9e06a1cebd6`; the startup working tree was
  clean.
- **Interpretation:** no unrelated uncommitted work was mixed into the task.
- **Limitations:** this establishes local source state, not hosted CI state.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-24---strict-startup-and-class-isolation`.

## EV-002 - One-recursive finite theorem and cubic bound

- **Date:** 2026-07-24
- **Method or command:** exact derivation from KR1G-5--KR1G-6 and the
  original cycle-sum identity; finite parent/side parametrization; Bellman
  completion recursion; simultaneous weighted Cauchy; three independent
  read-only audits; exact SymPy checks of the coverage, \(J-G\),
  denominator, and scalar-square identities.
- **Relevant output:** KR1G-89--KR1G-91 give the exact finite formulation.
  With \(m_1=q-\ell+1\),
  \(T^{(-\rho)}=T_{k,n}-d_\rho\), and
  \(Q^{(-\rho)}=Q_{k,n}-4/(2-\lambda_\rho)\), KR1G-98 gives
  \[
  \mathscr R_{k,n}(h)\ge
  \mathcal E_\rho+
  {(T^{(-\rho)})^2\over Q^{(-\rho)}+2m_1}.
  \]
  KR1G-99 makes the bound uniform in position, parent, and side. For every
  fixed \(k\), the normalized lower coefficient is
  \(\tau_k^2/(\chi_k+2\mu_k)>0\); only afterward does \(k\to\infty\) yield
  \(C_{\rm dist}\).
- **Interpretation:** no subcubic counterfamily exists in the declared
  class. The recursive loss may vanish in its coverage component, but the
  remaining base/unused energy still forces the cubic bound.
- **Limitations:** the theorem makes no claim for two or more selected
  recursive splits, a diagonal \(k=k(n)\), an exact residual infimum, or
  geometry.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-24---exact-finite-theorem-and-cubic-decision`.

## EV-003 - Independent exact checker

- **Date:** 2026-07-24
- **Method or command:**
  `python ops\TASK-20260724__kr1g_one_recursive_selected_split\exact_checker.py`;
  `python -m ruff check
  ops\TASK-20260724__kr1g_one_recursive_selected_split\exact_checker.py`;
  `python -m ruff format --check
  ops\TASK-20260724__kr1g_one_recursive_selected_split\exact_checker.py`.
- **Relevant output:** `PASS: 432 canonical cycles, 96600 broad genuinely
  recursive histories, plus 6720 arbitrary-completion histories; direct
  residual, KR1G-6 decomposition, parentage, radical envelope, optimized
  bound, uniform bound, and completion DP agree`. The two recursive
  positions at \((q,\ell)=(7,3)\) occur 30,240 and 60,480 times. There are
  9,504 broad zero-coverage cases. The deep fixture has 1,344
  zero-coverage completions and 1,920 completions using an edge with two
  inserted endpoints. Its exact minimum residual and optimized bound are
  \(1137/140\) and \(148/35\). Ruff lint and format checks pass.
- **Interpretation:** standard-library `Fraction` arithmetic independently
  checks every finite identity used by the theorem on genuinely recursive
  selected histories and arbitrary deeper completions.
- **Limitations:** the one-segment fixtures use \(s=1,\lambda=1/2\), and the
  separate two-segment fixture uses rational weights. They are synthetic
  structural checks, not rounded irrational all-middle rows and not a proof
  of the all-\(q\) theorem.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-24---independent-exact-recursive-checker`.

## EV-004 - Repository and final diff verification

- **Date:** 2026-07-24
- **Method or command:** `python -m pytest -p no:cacheprovider`;
  `$env:PYTHONPATH='src'; python -m
  power_ringmin.verify_checked_artifacts`; `python -m pytest
  tests\test_checked_artifact_schema_validation.py -p no:cacheprovider`;
  checker and Ruff commands from EV-003; exact SymPy identities; final
  equation-tag, display, aligned-environment, roadmap-link, UTF-8/LF,
  trailing-whitespace, Git status, complete diff, and `git diff --check`
  audits.
- **Relevant output:** 283 tests pass in 68.65 seconds; all four checked
  artifacts pass with 76 local brackets and summary rows \(3,4,5,6\); all
  four focused schema tests pass. The symbolic coverage, \(J-G\),
  denominator, and scalar-square identities simplify to zero. All 1,066
  equation tags are unique, proof displays and aligned environments are
  balanced, the new roadmap targets resolve, every changed text/code file
  is strict UTF-8 without BOM or CR and ends in LF, no changed line has
  trailing whitespace, and final Git diff checks pass.
- **Interpretation:** the proof, stable memory, roadmap, status, checker,
  and unchanged production verification layer are consistent.
- **Limitations:** the first SymPy invocation failed before evaluation
  because of PowerShell quote transport, and the first roadmap-anchor audit
  used an incorrect PowerShell truth test for a silent external command.
  Both invocation defects were retained here, corrected, and the substantive
  checks passed. Repository regressions and bounded enumeration do not
  replace the symbolic all-\(q\) proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-24---repository-verification-and-handoff`.

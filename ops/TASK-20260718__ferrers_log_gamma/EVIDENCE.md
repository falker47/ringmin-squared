# EVIDENCE - TASK-20260718__ferrers_log_gamma / Ferrers Logarithmic Coefficient

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / confirmation | Startup and symbolic separation | PG69, PG74--PG99, three independent derivations | PASS |
| EV-002 | computation | Formula-only component diagnostic | `component_diagnostic.py` | PASS |
| EV-003 | test / command | Static checks and repository regressions | repository commands | PASS |
| EV-004 | inspection | Independent audits, synchronization, and final diff | intended nine-file scope | PASS |

## EV-001 - Startup And Symbolic Separation

- **Date:** 2026-07-18
- **Method or command:** Read `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, PG69/PG74--PG85, the
  predecessor dossier, roadmap, templates, `git status`, and `git log`;
  compare three independent read-only derivations focused on the smooth
  components, the floor/ceiling sum, and possible logarithmic obstruction.
- **Relevant output:** clean startup at
  `6e7a1b6e241899883d4432d670ef8c261b3ca02d`; unanimous expansions
  \[
  \log Z_m=2m\log m+C_{\rm F}m-\tfrac12\log m
  +\tfrac12\log(10\pi/3)+O(m^{-1}),
  \]
  \[
  \Delta_m=\tfrac52\log(3/2)-4\log(5/4)+O(m^{-1}),
  \qquad
  \Theta_m=\tfrac54\log m+O(1).
  \]
- **Interpretation:** The logarithmic coefficient exists and is
  \(\gamma=-1/2+0+5/4=3/4\). PG93--PG95 prove the central uniform estimate;
  exact jumps, residue classes, and endpoints contribute only \(O(1)\).
- **Limitations:** independent agreement and later finite diagnostics do not
  replace the written all-\(m\) asymptotic proof. No convergence of the
  bounded remainder is asserted.
- **Linked log entry:** `TASK_LOG.md`, STRICT startup and independent
  derivations; sharp coefficient proof written.

## EV-002 - Formula-Only Component Diagnostic

- **Date:** 2026-07-18
- **Method or command:**
  `python -B ops\TASK-20260718__ferrers_log_gamma\component_diagnostic.py`.
- **Relevant output:** 25 rows pass, comprising \(m=3,4,5,6,7\) and every
  class modulo five in the four blocks beginning at
  \(125,2045,32765,262140\). Exact integer assertions check
  \(a=1+\lfloor c\rfloor\), \(0<a-c\le1\), and every PG97 endpoint
  branch. The factorial gamma quotient and the separately accumulated
  \(c/r\), \(a/c\), and \(a/s\) logarithmic sums agree within the declared
  floating tolerance. Selected centered columns are:

  | \(m\) | \(m\bmod5\) | total after \((3/4)\log m\) | factorial after \(-(1/2)\log m\) | \(\Delta_m\) | rounding after \((5/4)\log m\) | direct ceiling after \(-(3/4)\log m\) |
  |---:|---:|---:|---:|---:|---:|---:|
  | 3 | 3 | 1.56382058343 | 1.18660813401 | 0.0843132175959 | 0.292899231824 | -0.326080832938 |
  | 125 | 0 | 1.40896055740 | 1.17464578937 | 0.120043301811 | 0.114271466216 | -0.188803535329 |
  | 32768 | 3 | 1.37954123563 | 1.17435246837 | 0.121084559651 | 0.0841042076006 | -0.203679046941 |
  | 262140 | 0 | 1.38112123003 | 1.17435148687 | 0.121088064328 | 0.0856816790342 | -0.202015024471 |
  | 262144 | 4 | 1.38062590883 | 1.17435148600 | 0.121088064336 | 0.0851863582992 | -0.202510344997 |

  Final line:
  `PASS: listed rows satisfy the formula-only component checks`.
- **Interpretation:** The three numerical columns move toward the symbolic
  component scales and the total centered residual stays bounded on the
  listed rows. The script is standalone and iterates only the explicit
  formula index \(j\).
- **Limitations:** these are bounded floating observations, not a certificate
  for PG98 and not evidence that the bounded remainder converges.
- **Linked log entry:** `TASK_LOG.md`, formula-only component diagnostic
  implemented.

## EV-003 - Static Checks And Repository Regressions

- **Date:** 2026-07-18
- **Method or command:** run the new component diagnostic, predecessor PG84
  residual diagnostic, and predecessor exact Ferrers diagnostic with
  `python -B`; focused `python -m ruff check`,
  `python -m ruff format --check`, and `python -m py_compile` on the new
  script; focused product-distance pytest with cache disabled; complete
  pytest with an isolated `C:\tmp` basetemp; and a read-only broad Ruff
  probe.
- **Relevant output:** all three diagnostics PASS; the new script's lint,
  format, and compile checks PASS; 49 focused tests PASS. The initial
  sandboxed complete suite reported 252 passed and 31 setup errors, all
  `PermissionError` failures creating
  `C:\tmp\ringmin_squared_ferrers_gamma_full`. The approved identical rerun
  outside the sandbox passed all 283 tests. The broad Ruff probe retained
  four lint findings and 39 format findings in unrelated pre-existing
  production/test paths; the startup tree was clean, no such path is in this
  task diff, and the focused new script checks pass.
- **Interpretation:** The theorem-facing diagnostics and all tests pass. The
  failed sandbox setup was environmental, and the broad Ruff baseline is
  outside the changed scope; neither was hidden or modified around.
- **Limitations:** tests and floating diagnostics do not replace the proof.
  Whole-repository Ruff cleanliness is not claimed.
- **Linked log entry:** `TASK_LOG.md`, repository verification.

## EV-004 - Independent Audits, Synchronization, And Final Diff

- **Date:** 2026-07-18
- **Method or command:** three independent read-only derivations followed by
  separate smooth-proof, sawtooth-proof, diagnostic, TeX/tag, and cross-file
  audits; inspect current formulas, claims, generated files, Git status, and
  whitespace; inspect all five tracked diffs and all four new dossier files;
  run final `git diff --check`, scope, status, tag, cache, and basetemp checks.
- **Relevant output:** no P0--P2 mathematical finding. Audit suggestions now
  incorporated: explicit trapezoidal/Riemann formulas for `-21/160`,
  semi-open jump cells, the hit bound `q<m/5`, independently accumulated
  diagnostic components, calibrated floating PASS wording, and attribution
  of proof to the written argument rather than the audits. PG86--PG99 tags
  are globally unique and display/cases/array environments balance. The
  generated dossier `__pycache__` and isolated test basetemp were removed;
  final focused diagnostic confirms neither remains. Exactly the five
  pertinent authoritative files and four new dossier files are changed/new;
  final complete diff, whitespace, status, and scope checks pass.
- **Interpretation:** The proof, diagnostic, authoritative files, roadmap,
  and dossier agree on \(\gamma=3/4\), the three component coefficients,
  scope, limitations, and proposed next task. The task is ready for manual
  review.
- **Limitations:** inspection cannot replace user review. The unrelated broad
  Ruff baseline recorded in EV-003 remains outside this task diff.
- **Linked log entry:** `TASK_LOG.md`, proof audits and authoritative
  synchronization; repository verification.

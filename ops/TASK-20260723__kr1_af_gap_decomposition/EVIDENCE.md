# EVIDENCE - TASK-20260723 / KR1 Finite-Prefix Gap Decomposition

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / command | Startup and source isolation | repository sources / Git | PASS |
| EV-002 | exact theorem | KR1 finite-prefix gap decomposition | `research/FIXED_ORDER_CYCLE_RATIO.md` | PROVED |
| EV-003 | bounded exact computation | Independent dense-cutoff diagnostic | `exact_diagnostic.py` | PASS |
| EV-004 | regression / audit | Repository and final diff verification | commands / Git | PASS |

## EV-001 - Startup And Source Isolation

- **Date:** 2026-07-23
- **Method or command:** read `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, the authoritative
  arbitrary-finite-prefix and KR1 proof sections, their dossiers, the
  production KR1 generator, and relevant tests; run
  `git status --short --branch`, `git log -1 --oneline`, and
  `git rev-parse HEAD`.
- **Relevant output:** clean `main...origin/main` at
  `d5e3ea3b9e379989a04740978a432d4e92594686`.
- **Interpretation:** STRICT startup and bounded-task isolation pass.
- **Limitations:** source inspection alone does not prove the decomposition.
- **Linked log entry:** `TASK_LOG.md#2026-07-23---strict-startup-and-task-isolation`.

## EV-002 - Exact KR1 Gap Theorem

- **Date:** 2026-07-23
- **Method or command:** exact derivation from CR28ax--CR28dw, the KR1 block
  word R1C4--R1C10, and the unique maximizing tail KR1-2.
- **Relevant output:** KR1G-2--KR1G-6 decompose the finite slack into
  nonnegative terms. KR1G-7--KR1G-10 prove that every relevant KR1 split is a
  distinct original-edge split and give the two uniform profiles. Exact
  integration then proves
  \[
  {857\over3000}-C_{\rm AF}
  =\mathcal U+\mathcal H+\mathcal P+\mathcal Q,
  \]
  with
  \[
  \mathcal U
  ={4614125\sqrt2-5527598\over146004000}>0.
  \]
- **Interpretation:** exact theorem. The current arbitrary-finite-prefix lower
  functional is not cubically tight when evaluated on KR1. The concrete
  missing datum is a uniform way to retain slack on original edges that the
  selected history does not split.
- **Limitations:** pointwise KR1 audit only. It does not solve the minimum over
  all histories, prove that KR1 minimizes \(K\), improve a global coefficient,
  or imply a geometric claim.
- **Linked log entry:** `TASK_LOG.md#2026-07-23---exact-cubic-coefficients`.

## EV-003 - Bounded Exact Diagnostic

- **Date:** 2026-07-23
- **Method or command:**
  `python -B ops\TASK-20260723__kr1_af_gap_decomposition\exact_diagnostic.py`;
  `python -m ruff check
  ops\TASK-20260723__kr1_af_gap_decomposition\exact_diagnostic.py`;
  `python -m ruff format --check
  ops\TASK-20260723__kr1_af_gap_decomposition\exact_diagnostic.py`.
- **Relevant output:** exact finite identities pass on
  \(n=1001,1006,5001,5006,100001,100006\), covering both KR1 parity
  branches. Selected-edge counts are \(81,81,408,408,8167,8168\), with zero
  recursive splits on every row. At the largest row the normalized values
  \[
  \begin{array}{c|c}
  \text{term}&\text{observed coefficient}\\ \hline
  \text{total gap}&0.008632785848305\\
  \text{unused original slack}&0.006836345491143\\
  \text{height combination}&0.001137067196540\\
  \text{local floor}&0.000659373160622\\
  \text{product relaxation}&0.000001294716178\\
  \text{square center}&0.000658078444444
  \end{array}
  \]
  and each is within \(2\cdot10^{-5}\) of its proved limit.
- **Interpretation:** bounded exact computation with `Fraction` and an
  integer-square comparison for the irrational cutoff; independent order
  reconstruction and endpoint deletion corroborate the decisive
  classifications and coefficients.
- **Failed-check record:** the first Ruff format check requested mechanical
  reformatting. `python -m ruff format` was applied; final lint and format
  checks are rerun in EV-004.
- **Limitations:** using every integer cutoff is a discriminating Riemann-sum
  audit only. It is not a uniform growing-prefix theorem and does not replace
  EV-002.
- **Linked log entry:** `TASK_LOG.md#2026-07-23---independent-exact-dense-cutoff-diagnostic`.

## EV-004 - Repository And Final Diff Verification

- **Date:** 2026-07-23
- **Method or command:** `python -m pytest -p no:cacheprovider`;
  `$env:PYTHONPATH='src'; python -m
  power_ringmin.verify_checked_artifacts`; `python -m pytest
  tests\test_checked_artifact_schema_validation.py -p no:cacheprovider`;
  final diagnostic and Ruff checks from EV-003; exact equation-tag,
  Markdown-display, aligned-environment, UTF-8/LF, local-link, Git status,
  complete-diff, and whitespace audits.
- **Relevant output:** 283 tests pass in 67.65 seconds; all four checked
  artifacts pass with summary rows \(3,4,5,6\); all four focused schema tests
  pass; Ruff lint and format pass; all 22 new `KR1G` tags are unique;
  standalone displays balance \(1507/1507\), aligned environments balance
  \(184/184\), every changed text file is UTF-8 without BOM or CR and ends in
  LF, all new local links resolve, the complete final diff was inspected, and
  `git diff --check` passes.
- **Failed-check record:** two preliminary source-structure probes were
  over-broad. Counting every `\[` substring also counted `\left[` and
  reported \(1600/1576\); counting only exact-line `\end{aligned}` missed
  `\end{aligned}}` and reported \(184/174\). The corrected standalone-line
  and token audits give the balanced counts above. The initial Ruff format
  check in EV-003 also requested the recorded mechanical reformat.
- **Interpretation:** the proof, bounded diagnostic, durable memory, and
  repository regressions are consistent. The bounded task is
  `READY_FOR_REVIEW`.
- **Limitations:** regression and bounded checks do not replace the symbolic
  theorem and do not establish a growing-prefix result, a global minimizing
  history, or any geometric claim.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-23---final-verification-and-handoff`.

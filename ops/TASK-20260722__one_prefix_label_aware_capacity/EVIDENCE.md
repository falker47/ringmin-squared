# EVIDENCE - TASK-20260722 / One-Prefix Label-Aware Capacity

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source audit | Scope and source inspection | contract, proof, prior dossier, Git status | VERIFIED |
| EV-002 | exact theorem | Labelwise finite history bounds | CR28dw50--CR28dw55 | PROVED |
| EV-003 | exact optimization | Common cubic closure and global comparison | CR28dw56--CR28dw68 | PROVED |
| EV-004 | bounded exact computation | Independent histories and algebra diagnostic | `exact_diagnostic.py` | PASS |
| EV-005 | regression / hygiene | Repository verification and final diff | repository root | VERIFIED |

## EV-001 - Scope And Source Audit

- **Date:** 2026-07-22
- **Method or command:** inspected `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, the roadmap, CR28ax--CR28dw49, the preceding
  base-capacity proof and dossier, actual repository code and evidence, and
  clean `git status`; used three independent read-only derivations.
- **Relevant output:** the bounded task is the one-prefix label-aware
  refinement: preserve \(G(t)\) or \(J(t)\) at every selected label while
  retaining only base/recursive type and original-edge capacity.
- **Interpretation:** the task is distinct from richer endpoint filters and
  changes no production, test, artifact, schema, or geometric claim.
- **Limitations:** no optimality beyond the declared floor model is claimed.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-22---strict-startup-and-scope`.

## EV-002 - Exact Labelwise Finite Bounds

- **Date:** 2026-07-22
- **Method or command:** exact labelwise slack decomposition, monotonicity of
  \(\Delta(t)=J(t)-G(t)\), order statistics, and constructive classification
  of realizable base/recursive type words.
- **Relevant output:** with \(\nu=[2r-s-n-1]_+\), (CR28dw52) adds the
  \(\nu\) smallest advantages to \(\sum_{t=s}^{r-1}G(t)\).  Since the first
  selected insertion is necessarily base, literal histories satisfy the
  stronger shifted bound (CR28dw53).  Equations (CR28dw54)--(CR28dw55) give
  exact closed sums and their strictly positive difference when
  \(\nu>0\) and \(\lambda>0\).
- **Interpretation:** (CR28dw52) is strongest from cardinality alone;
  (CR28dw53) is strongest for the complete realizable binary type data.
  Already (CR28dw52) strictly dominates CR28dw41 for \(\lambda>0\) and at
  least two selected labels.
- **Limitations:** type-word realizability does not assert simultaneous
  equality of every geometric floor.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-22---labelwise-finite-bounds`.

## EV-003 - Exact Continuous Optimization

- **Date:** 2026-07-22
- **Method or command:** exact Riemann normalization; closed inactive/active
  formulas; Bernstein sign certificate; boundary localization; resultant and
  subresultant elimination; Sturm root counts; exact interval arithmetic;
  rational and radical comparison.
- **Relevant output:** both finite bounds have objective (CR28dw57).  Its
  active side has unique maximum \(13/48\).  The inactive stationary system
  has one feasible root, giving
  \[
  (\alpha_*,\beta_*,\lambda_*)
  \in(0.4365889,0.4365890)\times(0.3850802,0.3850803)
     \times(0.5024738,0.5024739)
  \]
  and the unique global value
  \[
  {4+2\sqrt3\over27}<0.2768854<C_{\rm LA,*}<0.2768855
  <{434+4\sqrt2\over1587}=C_{\rm AF}.
  \]
- **Interpretation:** exact method-specific improvement over the old
  one-prefix bound, but an exact failure to exceed \(C_{\mathrm{AF}}\).  The
  optimum is capacity-inactive.
- **Limitations:** this is not an upper bound on \(\Lambda_n\), a
  classification of richer filters, or a geometric leading-coefficient
  claim.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-22---exact-compact-optimization`.

## EV-004 - Independent Exact Diagnostic

- **Date:** 2026-07-22
- **Method or command:**
  `python -B ops/TASK-20260722__one_prefix_label_aware_capacity/exact_diagnostic.py`.
- **Relevant output:** PASS; 3,300 literal selected-prefix histories across
  four triangle-base rows.  Every history checks the requested cardinality
  floor and the forced-first-base refinement, exact closed sums, and positive
  margins.  Exact `Fraction` polynomial arithmetic checks the active
  identities and Bernstein rows, 729 compact active points, two degree-ten
  Sturm isolations, the algebraic-value identity modulo \(\mathcal Q\),
  direct optimizer-coordinate and value enclosures, and all decisive
  comparisons.
- **Interpretation:** standalone bounded corroboration importing only the
  Python standard library and no project, production, test, enumerator,
  artifact, or certificate helper.
- **Limitations:** finite histories and a finite grid do not replace the
  all-history and all-real exact proofs.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-22---independent-diagnostic-and-synchronization`.

## EV-005 - Repository Verification And Final Diff

- **Date:** 2026-07-22
- **Method or command:** reran
  `python -B ops/TASK-20260722__one_prefix_label_aware_capacity/exact_diagnostic.py`;
  ran Ruff lint and format checks, `python -m pytest -p no:cacheprovider`,
  `python -m pytest -p no:cacheprovider tests/test_checked_artifact_schema_validation.py`,
  and
  `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`;
  audited tags, standalone display delimiters, control characters, generated
  files, protected scope, Git status, the complete diff, and
  `git diff --check`; used two independent final read-only reviews.
- **Relevant output:** diagnostic PASS on 3,300 literal histories and 729
  active points, with optimizer/value Sturm chains of length 11, direct
  coordinate and value enclosures, and exact comparisons passing; Ruff PASS;
  full suite `283 passed`; focused schema suite `4 passed`; verifier PASS for
  4 certificates and 76 local brackets; 933 equation tags are unique;
  standalone display delimiters balance 1,483/1,483; zero forbidden control
  characters; exactly the 8 authorized files changed; no generated file;
  diff review and whitespace PASS.  Both independent reviews found no
  remaining mathematical, diagnostic, or synchronization issue.
- **Failed checks and resolution:** the first Ruff format check requested a
  mechanical reformat, after which E731 exposed two assigned lambdas; both
  became nested functions and all Ruff checks passed.  A newly added interval
  assertion on a fully expanded rational expression failed because dependency
  widening crossed zero; exact interval evaluation of the factored objective
  now directly encloses the claimed value and passes.  The first delimiter
  regex counted inline bracket commands rather than only display delimiters;
  the corrected standalone-line audit passes.  Final review found a missing
  backslash before `qquad` in the stable synopsis; it was corrected and
  re-audited.
- **Interpretation:** the exact proof, independent diagnostic, and repository
  integration are ready for human review.  No production source, test,
  schema, checked artifact, enumerator, or geometric artifact changed.
- **Limitations:** hosted CI cannot inspect an uncommitted diff.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-22---final-verification-and-handoff`.

# PROJECT_KNOWLEDGE - power-ringmin

Last reviewed: 2026-07-13

This file is stable durable project memory. Chronology, command transcripts, failed attempts, and task-local evidence belong in `ops/`.

## Project Identity

- VERIFIED FACT: working repository name is `power-ringmin`.
- VERIFIED FACT: project title is Power-Ringmin: Quadratic Radii.
- VERIFIED FACT: author is Maurizio Falconi.
- VERIFIED FACT: repository status is an independent research project, not a Ringmin worktree or branch.
- VERIFIED FACT: the authoritative project brief is `start.md`.
- VERIFIED FACT: upstream Ringmin local path is `C:\Users\Falker\Desktop\Code\circle\ringmin`.
- VERIFIED FACT: upstream public repository URL is `https://github.com/falker47/ringmin.git`.
- VERIFIED FACT: upstream inspected commit is `cc0327400819fe06b230d967cdcbafffe1648317`.
- RULE: Ringmin is prior work and a read-only upstream reference. No Ringmin theorem, implementation assumption, or structural pattern automatically transfers to quadratic radii.

## Definitions And Disproved Targets

- DEFINITION: peripheral radii are \(r_k=k^2\), for \(k=1,\dots,n\).
- DEFINITION: \(R_2^*(n)\) is the infimum feasible central radius for externally tangent peripheral circles with pairwise disjoint interiors.
- DEFINITION: optimum-radius symbols are treated as infima unless attainment
  has been proved. In particular, \(R^*_{2:n}\) is the infimum feasible
  central radius for only the core radii \(2^2,\dots,n^2\).
- DEFINITION: for peripheral radii \(r_i,r_j\) and central radius \(R\),
  \[
  \theta_R(r_i,r_j)
  =
  2\arcsin
  \sqrt{
  \frac{r_i r_j}
  {(R+r_i)(R+r_j)}
  }.
  \]
- DEFINITION: for quadratic radii,
  \[
  \theta_R(i^2,j^2)
  =
  2\arcsin
  \left(
  \frac{ij}
  {\sqrt{(R+i^2)(R+j^2)}}
  \right).
  \]
- DISPROVED CLAIM: the former principal research target
  \[
  R_2^*(n)=\frac{n^3}{6\pi}(1+o(1)).
  \]
- DISPROVED CLAIM: the former stronger target
  \[
  R_2^*(n)=\frac{n^3}{6\pi}+O(n^2).
  \]
- HEURISTIC: in the expected regime \(R\asymp n^3\), \(\theta_R(i^2,j^2)\approx 2ij/R\).
- WARNING: any heuristic leading to the former \(n^3/(6\pi)\) scale is insufficient as an asymptotic target because the induced-subset lower bound proves \(\liminf 6\pi R_2^*(n)/n^3\ge 4(\sqrt2-1)>1\).
- RULE: all-pairs non-overlap constraints are part of the problem, not merely adjacent-pair constraints.

## All-n Lower Bound

- EXACT THEOREM: for every finite index set \(S\) with \(|S|\ge 3\), every cyclic order \(\tau\) of \(S\), and the sorted duplicated multiset \(M_S=\{x_1\le\cdots\le x_{2|S|}\}\),
  \[
  \sum_\ell \tau_\ell\tau_{\ell+1}
  \ge
  \sum_{\ell=1}^{|S|}x_\ell x_{2|S|+1-\ell}.
  \]
  The proof is the rearrangement pairing lower bound applied to the duplicated multiset of indices.
- EXACT THEOREM: for every all-pairs feasible Power-Ringmin configuration and every subset \(S\) of at least three indices, the induced cyclic order on \(S\) has positive gaps summing to \(2\pi\), and each induced adjacent gap is at least the corresponding \(\theta_R(i^2,j^2)\).
- EXACT THEOREM: for every cyclic order \(\sigma\) of \(\{1,\dots,n\}\),
  \[
  \sum_{k=1}^n \sigma_k\sigma_{k+1}
  \ge
  \frac{n(n+1)(n+2)}{6},
  \]
  with indices read cyclically. The proof is the rearrangement pairing lower bound applied to the multiset with two copies of each index.
- EXACT THEOREM: for every \(n\ge 3\),
  \[
  R_2^*(n)\ge \frac{n(n+1)(n+2)}{6\pi}-n^2.
  \]
- EXACT THEOREM: for every \(n\ge 4\) and \(1\le m\le n-2\),
  \[
  R_2^*(n)\ge \frac{P_{m,n}}{\pi}-n^2,
  \qquad
  P_{m,n}
  =
  \sum_{k=m}^n k(m+n-k)
  =
  \frac{(n-m+1)(m^2+4mn+m+n^2-n)}{6}.
  \]
- EXACT THEOREM: for \(S=\{s_1<\cdots<s_q\}\), the duplicated-multiset
  pairing bound has the explicit form
  \[
  A(S)=2\sum_{a=1}^t s_a s_{2t+1-a}\quad(q=2t),
  \]
  and
  \[
  A(S)=2\sum_{a=1}^t s_a s_{2t+2-a}+s_{t+1}^2\quad(q=2t+1).
  \]
- EXACT THEOREM: at fixed cardinality \(q\), \(A(S)\) is uniquely maximized
  over \(S\subseteq\{1,\dots,n\}\) by the tail \(\{n-q+1,\dots,n\}\). Hence no
  nonconsecutive subset improves \(P_{m,n}\) inside the induced-subset plus
  duplicated-pairing plus \(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\) relaxation.
- EXACT THEOREM: the discrete maximizers of \(P_{m,n}\) over
  \(1\le m\le n-2\) are characterized by
  \[
  \rho_n=\frac{\sqrt{8n^2+8n+1}-(2n+1)}2.
  \]
  For \(n\ge4\), the unique maximizer is \(\lfloor\rho_n\rfloor+1\) unless
  \(\rho_n\in\mathbb Z\), in which case the two maximizers are
  \(\rho_n,\rho_n+1\). For \(n=3\), the domain is the singleton \(m=1\).
- EXACT THEOREM:
  \[
  \liminf_{n\to\infty}\frac{6\pi R_2^*(n)}{n^3}\ge 4(\sqrt2-1)>1.
  \]
- VERIFIED FACT: `research/ALL_N_LOWER_BOUND.md` records the self-contained proof, including the subset-induced cyclic-gap passage, the explicit \(A(S)\) formula, the tail optimality theorem, the consecutive-subset formula \(P_{m,n}\), the exact discrete maximizer characterization by \(\rho_n\), the rounded asymptotic choice \(m=\lceil(\sqrt2-1)n\rceil\), the angular inequality \(\theta_R(i^2,j^2)\ge 2ij/(R+n^2)\), and a gap/counterexample audit.
- INTERPRETATION: the induced-subset lower bound uses only necessary consequences of all-pairs feasibility; it does not require constructing a feasible order or controlling all non-adjacent constraints for an upper bound.
- INTERPRETATION: this proves a strict lower obstruction above the former \(n^3/(6\pi)\) target; it does not prove exact optima, a matching upper bound, or an exact asymptotic constant.
- INTERPRETATION: the coefficient \(2(\sqrt2-1)/(3\pi)\) is optimal only
  within the specific relaxation named above, not necessarily for
  Power-Ringmin.
- DISPROVED CLAIM: \(R_2^*(n)=n^3/(6\pi)(1+o(1))\).
- DISPROVED CLAIM: \(R_2^*(n)=n^3/(6\pi)+O(n^2)\).

## Exact Radius-One Insertion

- EXACT THEOREM: for a feasible core configuration at central radius \(R>0\),
  the circle of radius \(1\) can be inserted at the same radius whenever
  \[
  \sum_{j=2}^n\theta_R(1,j^2)<\pi.
  \]
  Each core circle forbids an open angular arc of measure
  \(2\theta_R(1,j^2)\); subadditivity leaves an allowed angle, and the proof
  explicitly verifies every new pair \((1,j^2)\), central tangency, and
  preservation of all core-core constraints.
- EXACT THEOREM: for \(R>0\) and \(j\ge2\),
  \[
  \theta_R(1,j^2)
  <{2j\over\sqrt{R(R+j^2+1)}}
  <{2j\over R}.
  \]
- EXACT THEOREM: the full and core feasible-radius sets are equal for every
  \(n\ge12\). Consequently,
  \[
  R_2^*(n)=R^*_{2:n}\qquad(n\ge12),
  \]
  without assuming either infimum is attained.
- VERIFIED FACT: `research/ALL_N_LOWER_BOUND.md` records the self-contained
  insertion proof, exact rational boundary estimates for `n=12,13`, uniform
  symbolic estimates for `n>=14`, the configuration-level core lower-bound
  reuse, and the infimum audit.
- INTERPRETATION: `12` is a sufficient explicit threshold, not a proved
  minimal threshold. The argument gives no conclusion for `n<=11`.
- INTERPRETATION: this exact theorem is independent of the checked `n=5,6`
  candidate structures and does not turn lower negative cycles into exact
  contact graphs.

## Regular-Core Cubic Upper Bound

- EXACT THEOREM: for every \(n\ge12\) and fixed \(R>0\), the largest value of
  \(\theta_R(i^2,j^2)\) over distinct core indices \(2\le i<j\le n\) is
  attained uniquely by \((i,j)=(n-1,n)\).
- EXACT THEOREM: for every \(n\ge12\), assigning the core centers to the
  equally spaced polar directions of a regular \((n-1)\)-gon is all-pairs
  feasible at
  \[
  U_n
  =
  \sqrt{
  n^2(n-1)^2\csc^2\!\left({\pi\over n-1}\right)
  +{(2n-1)^2\over4}}
  -{n^2+(n-1)^2\over2}.
  \]
  Every non-adjacent pair is checked through its smaller regular-polygon
  separation, which is at least one edge angle.
- EXACT THEOREM: the radius-one insertion theorem gives
  \[
  R_2^*(n)\le U_n\qquad(n\ge12),
  \]
  without an attainment assumption.
- EXACT THEOREM:
  \[
  \limsup_{n\to\infty}{R_2^*(n)\over n^3}\le{1\over\pi},
  \qquad
  R_2^*(n)=\Theta(n^3).
  \]
- VERIFIED FACT: `research/ALL_N_LOWER_BOUND.md` records the self-contained
  proof of the worst-pair reduction, closed formula, all-pairs feasibility,
  insertion step, and asymptotic conclusions.
- INTERPRETATION: the known lower and upper leading coefficients do not match.
  No limit or exact leading constant has been proved.

## Verified Computational Machinery

- VERIFIED FACT: the Python package import name is `power_ringmin`; package source is under `src/power_ringmin/`; tests are under `tests/`.
- VERIFIED FACT: substantial imported/adapted code is licensed under MIT and records upstream Ringmin commit `cc0327400819fe06b230d967cdcbafffe1648317` in module docstrings.
- VERIFIED FACT: `src/power_ringmin/geometry.py` provides positive-radius validation, `quadratic_radii(n)`, `theta(R,a,b)`, cyclic adjacent pairs, and cycle-equivalence helpers.
- VERIFIED FACT: `src/power_ringmin/evaluator.py` provides a float64 fixed-order evaluator using all-pairs STN feasibility, radius bracketing, recovered positions, Cartesian validation, essential tight-pair detection, and floating-radius detection.
- VERIFIED FACT: `src/power_ringmin/highprec.py` provides an independent `mpmath` fixed-order feasibility verifier, high-precision full-radius bisection, position recovery, and pair slack checks.
- VERIFIED FACT: `src/power_ringmin/crosscheck.py` provides a radius-sequence-aware fixed-order SLSQP cross-check using all-pairs Cartesian non-overlap constraints and explicit fixed-order angle variables.
- VERIFIED FACT: `src/power_ringmin/patterns.py` provides selected generic order constructors: sequential, zigzag, interleave, Supnick maximum-tour form, Supnick minimum-tour form, and JSON order loading.
- VERIFIED FACT: root `verify.py` is a standalone high-precision fixed-order verifier scaffold that imports only the Python standard library and `mpmath`.
- VERIFIED FACT: `schemas/fixed_order_result.schema.json` defines the v1 JSON artifact schema for one fixed-order numerical result.
- VERIFIED FACT: `src/power_ringmin/fixed_order_artifact.py`, `src/power_ringmin/export_fixed_order_cli.py`, `src/power_ringmin/export_fixed_order_batch_cli.py`, and `src/power_ringmin/verify_fixed_order_artifacts_cli.py` provide fixed-order artifact construction, export, batch export, and standalone-verifier checking.
- VERIFIED FACT: `src/power_ringmin/search_small_n.py` provides canonical quadratic index-order enumeration modulo rotation and reflection, canonicalization, quadratic index-to-radius conversion, exhaustive float64 small-`n` search, and v1 small-`n` search JSON helpers.
- VERIFIED FACT: `ops/TASK-20260711__interval_verifier_semantics/DESIGN.md` records the design semantics for finite small-`n` interval certification.
- VERIFIED FACT: `src/power_ringmin/interval_verifier.py` implements local fixed-order interval bracket verifier semantics for one canonical quadratic index order.
- VERIFIED FACT: the local interval bracket verifier checks the radius order against the index-order squares, rejects noncanonical index orders, requires exact local `artifact_type`, requires exact backend metadata matching for every field declared by the oracle including `rounding_policy`, rejects tolerance-based interval metadata, checks a lower endpoint by an explicit negative cycle using relaxed interval edge upper weights, and checks an upper endpoint by explicit all-pairs witness slacks using theta upper bounds.
- VERIFIED FACT: `MPMathIntervalAngularOracle` provides a guarded `mpmath.iv` angular interval backend using `atan2(x, sqrt(1-x^2))` for the inverse-sine step and records backend precision, guard, rounding policy, outward-enclosure, certification-capability, and no-tolerance metadata.
- VERIFIED FACT: `src/power_ringmin/interval_bracket_exporter.py` provides a fixed-order interval bracket generator/exporter for records consumed by the local interval verifier.
- VERIFIED FACT: generated fixed-order interval bracket records are local fixed-order certificate building blocks only; they do not certify a global small-`n` optimum unless a global verifier covers every canonical order.
- VERIFIED FACT: `src/power_ringmin/small_n_interval_certificate.py` provides a finite small-`n` interval certificate aggregator that embeds local fixed-order interval bracket records, independently regenerates the canonical cyclic index-order space, verifies exactly one local bracket per canonical order, and computes a finite global radius bracket from verified local endpoints.
- VERIFIED FACT: `schemas/small_n_interval_certificate.schema.json` defines the v1 structural JSON Schema for finite small-`n` interval certificate artifacts.
- VERIFIED FACT: `power-ringmin-export-small-n-interval-certificate` is a bounded general finite small-`n` certificate CLI that requires an explicit `--max-canonical-orders` ceiling and supports `--dry-run` preflight.
- VERIFIED FACT: small-`n` certificate generation is currently work-count bounded by canonical-order count and local retry count, not wall-clock bounded.
- VERIFIED FACT: `schemas/finite_results_summary.schema.json` defines the v1 structural JSON Schema for a separate derived finite-results summary artifact, `power-ringmin.finite_results_summary.v1`.
- VERIFIED FACT: `src/power_ringmin/finite_results.py` provides the derived finite-results summary builder, dump/load helpers, CLI, and semantic validator for checked source certificates.
- VERIFIED FACT: finite-results summary validation reloads every source small-`n` interval certificate through the semantic certificate loader, recomputes source `content_sha256` values, rederives candidate sets and exclusion gaps, and rejects stale summaries when source content or derived content no longer match.
- VERIFIED FACT: finite-results `content_sha256` is a cross-platform source-content SHA-256 digest: the source certificate byte stream is hashed after normalizing every CRLF sequence and every lone CR byte to one LF byte, with no character decoding or other byte normalization.
- VERIFIED FACT: JSON Schema validation is structural only; semantic Python validators remain authoritative for interval verification, checked-artifact source freshness, and derived summary consistency.
- VERIFIED FACT: `src/power_ringmin/verify_checked_artifacts.py` provides `power-ringmin-verify-checked-artifacts`, a deterministic checked-artifact verification command that discovers checked finite certificates, validates JSON Schema structure, reloads semantic validators, explicitly re-verifies embedded local interval brackets, validates the finite-results summary, and rejects summary source mismatches.
- VERIFIED FACT: `docs/INTERVAL_BACKEND_TRUST.md` documents the current guarded `mpmath.iv` backend trust contract, guards, tested coverage, unproved/audited gaps, classification implications, and possible stronger future trust paths.
- VERIFIED FACT: `.github/workflows/verification.yml` defines a GitHub Actions workflow for Python `3.11`, `3.12`, and `3.13` that installs package test and crosscheck extras, runs the full test suite, runs checked-artifact semantic verification, runs schema validation tests, and runs diff/trailing-whitespace hygiene checks.
- VERIFIED FACT: `pyproject.toml` registers console scripts for fixed-order export, batch fixed-order export, fixed-order interval bracket export, checked `n=3`/`n=4` interval certificate export, general small-`n` interval certificate export, fixed-order artifact verification, small-`n` float64 search, derived finite-results summary generation, critical-structure analysis, and checked-artifact verification.
- USER-REPORTED STATUS: the 2026-07-12 research-roadmap task started from a successful CI fix and green hosted GitHub Actions run. Codex did not independently query GitHub during that task.
- INTERPRETATION: float64 and high-precision numerical search/recheck artifacts are numerical observations unless interval evidence covers the relevant finite order space.

## Certified Finite Results

The following checked artifacts are classified as COMPUTER-CERTIFIED RESULT under the repository's documented local interval-verifier semantics and guarded `mpmath.iv` interval-backend contract.

| `n` | Canonical order count | Certified global lower endpoint | Certified global upper endpoint | Checked artifact path | Certification limitation |
|---:|---:|---|---|---|---|
| 3 | 1 | `0.3832870361393696523322205393924377858638763427734375` | `0.383487036139369685816546962087159045040607452392578125` | `examples/small_n_interval_certificate_n3.json` | finite `n` only; no exact optimum, all-`n` theorem, or asymptotic claim; guarded `mpmath.iv` backend provenance remains a limitation |
| 4 | 3 | `1.4955284118749971877804227915476076304912567138671875` | `1.4957284118749971657535979829845018684864044189453125` | `examples/small_n_interval_certificate_n4.json` | finite `n` only; no exact optimum, all-`n` theorem, or asymptotic claim; guarded `mpmath.iv` backend provenance remains a limitation |
| 5 | 12 | `3.934227717145796443531935437931679189205169677734375` | `3.9344277171457964215051106293685734272003173828125` | `examples/small_n_interval_certificate_n5.json` | finite `n` only; no exact optimum, all-`n` theorem, or asymptotic claim; guarded `mpmath.iv` backend provenance remains a limitation |
| 6 | 60 | `8.4678350760883720482752323732711374759674072265625` | `8.4680350760883715821591977146454155445098876953125` | `examples/small_n_interval_certificate_n6.json` | finite `n` only; no exact optimum, all-`n` theorem, or asymptotic claim; guarded `mpmath.iv` backend provenance remains a limitation |

- INTERPRETATION: these finite brackets do not prove exact optimum values; each strict lower endpoint is excluded and each upper endpoint is certified feasible under the artifact semantics.
- INTERPRETATION: these finite brackets do not prove exact optima or asymptotic claims; the disproof of the former \(n^3/(6\pi)\) target comes from the all-\(n\) induced-subset theorem, not from finite certificates.

Candidate-set extraction uses the following finite-certificate semantics.

- DEFINITION: for one finite certificate with verified local brackets, \(U\) is the minimum verified upper endpoint across all canonical orders, and the certified candidate set is \(C=\{\sigma:L_\sigma\le U\}\), where \(L_\sigma\) is the verified strict lower endpoint for order \(\sigma\).
- DEFINITION: an order with \(L_\sigma>U\) is certified not to be globally optimal under the checked artifact semantics.
- DEFINITION: when at least one order is excluded, the exclusion gap is \(\Delta=\min_{\sigma\notin C}(L_\sigma-U)\).
- COMPUTER-CERTIFIED RESULT: derived from the checked `n=3..6` artifacts, current candidate-set sizes and exclusion gaps are:

| `n` | Candidate-set size | Excluded-order count | Exclusion gap |
|---:|---:|---:|---|
| 3 | 1 | 0 | undefined |
| 4 | 1 | 2 | `0.1171644705802874497635457373689860105514526367187500` |
| 5 | 2 | 10 | `0.1137866156209259571596703608520328998565673828125` |
| 6 | 5 | 55 | `0.0488707956703002821541304001584649085998535156250` |

- INTERPRETATION: candidate-set size `1` means there is a unique certified candidate order modulo the current rotation/reflection convention.
- WARNING: candidate-set size greater than `1` does not prove an exact tie between the candidate orders.
- WARNING: identical serialized local brackets must not be described as exact equality of the corresponding fixed-order optima.
- VERIFIED FACT: the checked derived summary artifact `examples/finite_results_summary_n3_n6.json` records the `n=3..6` certified finite brackets, candidate sets, exclusion gaps, identical serialized bracket groups, source certificate line-ending-normalized `content_sha256` values, and finite-`n` ratios under `power-ringmin.finite_results_summary.v1`.
- INTERPRETATION: `examples/finite_results_summary_n3_n6.json` is derived analysis over checked source certificates. It does not replace the primary certificate artifacts and does not change `power-ringmin.small_n_interval_certificate.v1`.

## Empirical Structural Questions

- OPEN QUESTION: can tighter brackets or independent methods reduce the multiple certified candidate sets for `n=5` and `n=6`?
- OPEN QUESTION: how do the checked finite brackets compare numerically with the induced-subset lower obstruction at small `n`?
- OPEN QUESTION: do the checked finite cases suggest stable optimal-order representatives, floating-circle regimes, or contact structures that can be formulated as conjectures?

## Candidate Critical-Structure Analysis

- VERIFIED FACT: `src/power_ringmin/critical_structure.py` provides deterministic structural analysis for checked finite candidate orders, including lower negative-cycle normalization, stable index/radius-pair labels, interval-lower upper-witness slack rankings, candidate common-core intersections, candidate differences, weak-constraint proxy labels, and identical-bracket diagnostics.
- VERIFIED FACT: `ops/TASK-20260712__critical_constraints_order_structure/critical_structure_n3_n6.json` records the checked `n=3..6` candidate-order structural analysis under `power-ringmin.critical_structure_analysis.v1`.
- VERIFIED FACT: `research/FINITE_RESULTS.md` summarizes the checked finite results and structural diagnostics with separate evidence labels for computer-certified finite facts, verified structural data, numerical observations, empirical patterns, heuristics, conjectures, open questions, and warnings.
- VERIFIED FACT: for the checked certified candidate orders at `n=5`, both candidates share the same lower negative-cycle pair set `{2-4, 2-5, 3-4, 3-5}` after stable index/radius-pair normalization.
- VERIFIED FACT: for the checked certified candidate orders at `n=6`, all five candidates share the same lower negative-cycle pair set `{2-5, 2-6, 3-4, 3-6, 4-5}` after stable index/radius-pair normalization.
- EMPIRICAL PATTERN: in the checked multiple-candidate cases `n=5` and `n=6`, the repeated serialized candidate brackets align with a shared lower-cycle pair core on indices `2..n`, while directed cycle signatures and upper-witness minimum-slack pair sets are not common across all candidates.
- HEURISTIC: under the recorded finite proxy rule, index `1` is a possible weakly constrained index for the checked multiple-candidate cases `n=5` and `n=6`; this is not a certified floating-circle or active-constraint non-incidence statement.
- WARNING: lower negative cycles are lower-endpoint infeasibility certificates, not exact active contact graphs; upper-witness slack rankings are finite numerical diagnostics at certified upper endpoints.
- OPEN QUESTION: can the shared lower-cycle core on indices `2..n` be formulated as a smaller exact reduced subsystem, or is it an artifact of the current bracket generator and resolution?
- OPEN QUESTION: can tighter brackets or independent fixed-order analysis determine whether repeated serialized brackets at `n=5` and `n=6` reflect exact ties, hidden symmetry, or numerical coincidence?

## Current Research Roadmap

- VERIFIED FACT: `research/NEXT_RESEARCH_STEPS.md` is the current concise roadmap synthesizing checked `n=3..6` certificates, candidate sets and exclusion gaps, critical-cycle diagnostics, weak-constraint observations, verifier limitations, CI status, combinatorial growth, the induced-subset lower-bound disproof of the former \(n^3/(6\pi)\) target, the exact eventual radius-one insertion theorem, and the regular-core cubic upper bound.
- INTERPRETATION: the cubic order is settled; improving the regular-core
  coefficient or finding a different construction that narrows the exact
  coefficient gap is now more valuable than automatic `n=7` enumeration.
- EXACT THEOREM: the reduced-core insertion question has an all-configuration
  answer at the level of feasible radii for `n>=12`: index `1` can be inserted
  without increasing the central radius. This does not assert a fixed-order
  active-subsystem description or settle `n<=11`.
- OPEN QUESTION: can the regular-core coefficient \(1/\pi\) be lowered toward
  the induced-subset coefficient \(2(\sqrt2-1)/(3\pi)\), while retaining a
  symbolic all-pairs proof?
- RULE: an `n=7` exhaustive certificate should be considered only after structural analysis produces a precise discriminator such as competing order-family predictions, a predicted candidate-set cardinality, a predicted critical-cycle transition, or a predicted first floating-index pattern.

## Open Proof Obligations And Limitations

- PROOF OBLIGATION: locally record or prove the angular formula, monotonicity of \(\theta_R(a,b)\) in `R`, fixed-order angular/STN equivalence, and negative-cycle infeasibility.
- LIMITATION: the current certified finite results depend on the documented guarded `mpmath.iv` interval-backend contract; backend trust/provenance remains a production-review item.
- LIMITATION: finite computation for `n=3..6` is not proof for all `n`.
- LIMITATION: no exact optimum value has been proved in this repository.
- LIMITATION: no upper bound matching the induced-subset leading coefficient
  has been proved in this repository.
- LIMITATION: neither existence of \(\lim R_2^*(n)/n^3\) nor a leading-term
  asymptotic formula has been proved in this repository.
- LIMITATION: no Ringmin result should be silently generalized to quadratic radii.
- LIMITATION: the sufficient radius-one threshold `12` is not known to be
  minimal, and the exact equality question remains open for `n<=11`.

## Evidence Classification Rules

Every material mathematical or computational claim must be classified where relevant as one of:

- definition;
- verified fact;
- exact theorem;
- computer-certified result;
- numerical observation;
- empirical pattern;
- heuristic;
- conjecture;
- unresolved claim;
- disproved claim.

Rules:

- finite computation is not proof for all `n`;
- a conjecture must not be used as an established lemma;
- conditional arguments must be labeled conditional;
- all-pairs constraints must be checked, not only adjacent pairs;
- numerical precision, parameters, solver, seeds, environment, and code version must be recorded when relevant;
- contradictory evidence must be preserved and investigated;
- task chronology and detailed command evidence belong in `ops/`, not in this file.

## Canonical Commands

- `python -m pytest`
- `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`
- `python -m pytest tests\test_checked_artifact_schema_validation.py`

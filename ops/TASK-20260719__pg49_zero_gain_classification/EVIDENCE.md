# EVIDENCE - TASK-20260719 / PG49 Zero-Gain Classification

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | exact algebra | Primitive left/right parametrization | fixed-order note | PROVED |
| EV-002 | exact theorem | Plateau and boundary audit | fixed-order note | PROVED |
| EV-003 | exact reduction | Cubic continued-fraction obstruction | fixed-order note | PROVED |
| EV-004 | bounded computation | Sole falsification diagnostic | bounded_diagnostic.py | PASS |
| EV-005 | exact witnesses | Giant left and first bounded right witness | integer substitution | VERIFIED |
| EV-006 | regression / hygiene | Tests, artifacts, source, review, and diff audit | repository root | VERIFIED |

## EV-001 - Startup And Primitive Parameterization

- **Date:** 2026-07-19
- **Method or command:** inspected `AGENTS.md`, `start.md`,
  `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, KPGMIN-1--KPGMIN-39,
  PG37--PG40, PG100--PG109, and the prior descending-min task dossier at a
  clean `main` worktree, commit `78e0007ee1ca7967a787b60c072f167b3b8a2abe`.
- **Relevant output:** the identities
  `gain=x^2-(a-x)(b-x)` give a unique primitive factorization
  `a-x=gu^2`, `b-x=gw^2`, `x=guw`.  Solving yields the separate constants
  `(4,8,6)` for left holes and `(7,9,3)` for right holes.
- **Interpretation:** exact necessary-and-sufficient parametrization of each
  gain equation before plateau constraints.
- **Limitations:** the gain conic alone does not imply that the assigned path
  lies on a plateau.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---strict-startup-and-exact-reduction`.

## EV-002 - Exact Plateau And Boundary Audit

- **Date:** 2026-07-19
- **Method or command:** direct substitution into
  `0<=2r(d+t)-t(d-1)<2(d+t)` for `t=j,j+1`, separately for each branch.
- **Relevant output:** KPGZERO-10--KPGZERO-14 give the four exact polynomial
  residuals.  The allowed left equality `h_{j+1}=r` remains; the excluded
  left lower endpoint is impossible; both right endpoints are strict.
  Minimum/terminal plateau columns and the absence of a closing right hole
  are explicit.
- **Interpretation:** complete plateau classification with no floating point,
  hidden ceiling, or omitted endpoint.
- **Limitations:** it classifies membership but does not yet decide how many
  parameter triples occur globally.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---plateau-boundaries-and-cubic-obstruction`.

## EV-003 - Continued-Fraction Obstruction

- **Date:** 2026-07-19
- **Method or command:** irreducibility modulo seven, exact sign brackets for
  the cubic root, mean-value bounds in all four branch/sign cases, and
  Legendre's criterion.
- **Relevant output:** every accepted primitive `u/w` is a regular convergent
  of the unique root of `50+51t-27t^2-24t^3`; every convergent has a finite,
  explicitly tested arithmetic-progression segment of possible `g`.
- **Additional audit:** KPGZERO-20--KPGZERO-21 give all four exact
  sign-dependent quadratic scale windows; the sole diagnostic checks their
  equivalence to the separate branch residuals on every integral in-domain
  proposal.
- **Interpretation:** KPGZERO-23 is an exact bijection.  Global infinitude is
  equivalent to infinitely many one-sided convergents meeting simultaneous
  approximation, congruence, and scale windows.
- **Limitations:** neither general continued-fraction theory cited in the
  task nor any repository theorem decides this filtered subsequence.  The
  finite/infinite dichotomy remains an unresolved claim, not a proved
  theorem.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---plateau-boundaries-and-cubic-obstruction`.

## EV-004 - Sole Bounded Diagnostic

- **Date:** 2026-07-19
- **Method or command:**
  `python ops/TASK-20260719__pg49_zero_gain_classification/bounded_diagnostic.py`.
- **Relevant output:** PASS; literal rows `m=3..500` have no zero; direct
  near-root denominators are scanned through `10^5`; finitely proposed
  convergents have denominator at most `10^200`, with `g<=200`; 56 left and
  eight right parameter triples are individually accepted by exact integer
  reconstruction, both ceilings, and literal gain evaluation.
- **Interpretation:** exact positive witnesses falsify universal right-hole
  nonexistence and corroborate both parametrizations.
- **Limitations:** decimal arithmetic only proposes bounded convergents and
  certifies no absence statement.  The finite run neither proves finiteness
  nor infinitude and is not used in the all-parameter proof.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---bounded-diagnostic-and-right-hole-discovery`.

## EV-005 - Exact Left And Right Witnesses

- **Date:** 2026-07-19
- **Method or command:** exact integer substitution into KPGZERO-2--KPGZERO-14
  and the literal KPGMIN-7 gains.
- **Relevant output:** the primitive left triple `(g,u,w)=(4,11116408784,
  7852541895)` reconstructs KPGMIN-19 with strict ceiling residuals,
  `L=0`, and negative `R`.  The primitive right triple beginning with
  `g=19` in KPGZERO-27 reconstructs KPGZERO-28--KPGZERO-30 with both ceilings
  strict, positive `L`, and `R=0`.
- **Interpretation:** both branches are nonempty exact sets; an all-right
  obstruction is disproved.
- **Limitations:** two witnesses, or the larger bounded list, do not constitute
  an infinite family.
- **Linked log entry:**
  `TASK_LOG.md#2026-07-19---bounded-diagnostic-and-right-hole-discovery`.

## EV-006 - Regression, Source, And Review Audit

- **Date:** 2026-07-19
- **Method or command:** reran the sole bounded diagnostic; full pytest with
  a workspace-local basetemp; focused checked-artifact schema pytest;
  standalone checked-artifact verification; scoped Ruff lint and format;
  PowerShell KPGZERO tag/display/notation/diagnostic-count audit; independent
  formula review; Git status, complete diff inspection, and whitespace
  checks.
- **Relevant output:** the diagnostic passes; full pytest reports 283 passed;
  focused schema pytest reports 4 passed; the artifact verifier reports 4
  certificates and 76 local brackets for n=3,4,5,6; Ruff passes; the source
  audit reports sequential tags 1--30, 44 balanced displays, 15 balanced
  aligned environments, no root-name collision, and one diagnostic.
  Independent review reports no mathematical or material defect in
  KPGZERO-1--KPGZERO-30.
- **Failed check retained:** after focused pytest, a cleanup probe attempted
  to resolve its basetemp and failed because pytest had already removed the
  directory; no generated path remained and no cleanup action was needed.
- **Interpretation:** all task-proportional regression and exact-source
  checks pass.  The symbolic theorem does not depend on the bounded run.
- **Limitations:** these checks do not decide the filtered-convergent
  cardinality obstruction.
- **Linked log entry:** the final regression and handoff entry in TASK_LOG.md.

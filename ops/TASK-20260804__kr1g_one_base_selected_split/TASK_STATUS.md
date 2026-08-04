# TASK STATUS - TASK-20260804 / KR1G One Base Selected Split

Last update: 2026-08-04

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** decide the complete KR1G residual on the unchanged
  all-middle tuple, at each fixed \(k\), for histories with exactly one
  selected base split and \(p=\ell-1\) selected recursive splits of
  arbitrary parentage and depth, followed by arbitrary compatible
  completion below \(s_k\).
- **Expected output:** an exact finite formulation from KR1G-91b, a rigorous
  positive cubic liminf or a compatible subcubic family, a small independent
  exact checker with nontrivial recursive topologies, and aligned proof,
  stable memory, roadmap, current status, and task evidence.

## Scope

- **In scope:** the specialization \(p=\ell-1\) with one selected base
  split; the forced base label; the exact finite prefix count and Bellman
  minimum; all recursive terms in KR1G-93--KR1G-98; arbitrary recursive
  parentage, depth, and compatible completion; fixed \(k\), followed by
  \(n\to\infty\).
- **Out of scope:** the generic \(b=o(n)\) regime, any diagonal
  \(k=k(n)\), geometry, minimizing-order consequences, production code,
  public tests, schemas, and checked artifacts.

## Verified Facts

- The task began from clean baseline
  `943a841d46424cf2c22fe3d80be2e88438b32262` before task-scoped edits.
- KR1G-91b supplies the exact finite prefix/Bellman optimization for every
  finite admissible \(p\), including \(p=\ell-1\); the fixed-\(p\)
  asymptotic theorem does not apply when \(p\) grows with \(\ell\).
- The preceding positive-base-density theorem deliberately leaves the
  density-zero regime outside its conclusion, and its checker does not
  enumerate compatible recursive histories.
- KR1G-114--KR1G-123 give the exact one-base count and Bellman minimum,
  preserve every KR1G-93 recursive addend, and prove a positive cubic liminf
  separately for every fixed \(k\).
- The standalone exact checker passes 216 nontrivial BRRR prefixes and all
  39,312 two-label completions, including recursive depth three and
  inserted--inserted targets.
- The full suite, focused Arb/schema suites, checked artifacts, Ruff, and all
  preceding recursive-history checker regressions pass.

## Assumptions / Inferences

- The proved finite lower quantity \(K_{k,n}^{1\mathrm B}\) satisfies
  \[
  {K_{k,n}^{1\mathrm B}\over n^3}
  \longrightarrow \Theta_k^{1\mathrm B}>0
  \]
  for every fixed \(k\). The coefficient is the exact limit of that retained
  deterministic lower bound, not an exact coefficient of the unknown
  residual minimum.

## Decisions And Rationale

- Specialize the exact finite KR1G-91b domain before taking asymptotics, so
  the forced base label and the full compatible completion layer remain
  explicit.
- Start from KR1G-93--KR1G-98 and preserve every recursive energy term; the
  earlier lower-order-statistic relaxation discards precisely the structure
  needed when only one base coordinate remains.
- Keep the checker standalone and task-local because it audits finite proof
  structure rather than production behavior.

## Plan And Expected Delta

- [x] Isolate the one-base class and record the clean startup baseline.
- [x] Complete and independently audit the exact finite specialization and
  fixed-\(k\) cubic argument.
- [x] Implement and run the focused independent exact checker.
- [x] Run repository, artifact, schema, and prior KR1G regressions.
- [x] Align authoritative proof, stable memory, roadmap, and current status.
- [x] Inspect the final diff, run `git diff --check`, and set
  `READY_FOR_REVIEW` if every required check passes.

## Verification

- **Checks:** startup source isolation; independent proof audit; exact
  task-local checker and Ruff; full repository and certification
  regressions; prior recursive-history checkers; equation-tag, link,
  encoding, whitespace, status, and complete-diff audits.
- **Observed result:** the new checker and Ruff pass; 283 full tests, 3 Arb
  tests, 4 schema tests, all 4 checked artifacts and 76 local brackets, and
  all three prior KR1G checkers pass. The proof, equation tags, links,
  encoding, line endings, display balance, whitespace, full diff, status,
  and `git diff --check` audits pass.
- **Limitations:** no pending item is treated as evidence. The bounded exact
  checker will corroborate finite identities and topology coverage but will
  not replace the symbolic all-\(q\) or asymptotic proof.

## Blockers / Risks

- No current blocker.
- Residual risk is human review of the retained recursive-energy lower bound
  and its fixed-\(k\) quantifiers.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** the exact checker, full suite, artifact checks,
  prior KR1G regressions, and final source/diff audits all pass.
- **Files changed:** `research/FIXED_ORDER_CYCLE_RATIO.md`,
  `PROJECT_KNOWLEDGE.md`, `research/NEXT_RESEARCH_STEPS.md`,
  `CURRENT_STATUS.md`, and this task dossier/checker; no production module,
  public test, schema, checked artifact, or workflow.
- **Files to read first:** KR1G-114--KR1G-123 in
  `research/FIXED_ORDER_CYCLE_RATIO.md`, `exact_checker.py`, and EV-002--EV-005
  in `EVIDENCE.md`.

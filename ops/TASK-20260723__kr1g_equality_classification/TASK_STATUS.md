# TASK STATUS - TASK-20260723 / KR1G Equality Classification

Last update: 2026-07-23

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** classify symbolically every equality pair in the positive
  branch of the relaxed KR1G minimum and decide whether arbitrary equality
  families can avoid a cubically positive correction prefix after the
  selected KR1G labels are assigned and split.
- **Expected output:** an all-\(q\) iff classification, an exact structural
  block parametrization, one symbolic theorem or counterexample for the
  selected-prefix barrier, and one independent bounded classification oracle.

## Scope

- **In scope:** \(q\ge3\),
  \(1\le\ell<\lceil q/2\rceil\); all simple cycles and all
  \(E'\subseteq E(C)\) with \(|E'|\le\ell\); every bijection from the selected
  labels to \(E'\); the unchanged all-middle KR1G cutoff sequence; exact
  finite inequalities and separated fixed-\(k\), \(n\), and \(k\) limits.
- **Out of scope:** production code, public tests, schemas, artifacts,
  enumeration-limit changes, non-equality histories, an exact full-residual
  coefficient, minimizing-order claims, or geometric consequences.

## Verified Facts

- Equality in the positive branch holds if and only if exactly \(\ell\)
  noncomplementary edges are deleted, every complementary edge is retained,
  and every other retained edge has deviation \(\pm1\).
- Contracting the complementary matching gives exactly \(\ell\) signed
  interval components; the deleted edges join their free stubs in one cycle.
- Every assignment of the selected labels satisfies the exact finite
  weighted-slot bound KR1G-57.
- At each fixed all-middle cutoff the selected-prefix coefficient is
  \(I(D_k)>0\), and
  \[
  \liminf_{k\to\infty}\liminf_{n\to\infty}
  {\min M_h\over n^3}
  \ge I(E)
  \ge {787-551\sqrt2\over73002}>0.
  \]
- The independent \(q\le10\) oracle passes all 1,066 equality pairs.

## Assumptions / Inferences

- The finite equality and prefix statements require no computational
  assumption.
- Integer admissibility at the irrational all-middle cutoffs is eventual for
  each fixed \(k\); no uniform threshold in \(k\) is asserted.

## Decisions And Rationale

- Use simultaneous equality in the retained-edge count, complementary
  matching count, and integer deviation-square bound.
- Contract the forced complementary matching to expose interval components
  of a signed block path.
- Use an auxiliary decreasing convex weighting of the selected chronological
  prefixes, followed by connector-slot majorization.
- Keep the oracle task-local, standard-library-only, and limited to
  \(q\le10\) classification checks.

## Plan And Expected Delta

- [x] Complete STRICT startup on a clean worktree.
- [x] Derive the all-\(q\) equality classification.
- [x] Derive the finite selected-prefix lower bound and limiting coefficient.
- [x] Run and harden the independent bounded oracle.
- [x] Update the authoritative proof, stable memory, roadmap, and status.
- [x] Complete repository verification and final diff review.
- [x] Set all task memory to `READY_FOR_REVIEW`.

## Verification

- **Checks:** independent exhaustive oracle; Ruff lint and format; exact
  symbolic algebra; two independent mathematical reviews and one independent
  oracle review; full repository tests; checked-artifact and schema
  verification; equation-tag, Markdown-display, encoding, link, Git diff,
  and whitespace audits.
- **Observed result:** 204,556 canonical cycles and all 1,066 equality pairs
  pass; exact algebra and all three independent reviews pass; 283 repository
  tests, all four checked artifacts, and four focused schema tests pass; all
  final source and diff audits pass.
- **Limitations:** the bounded oracle verifies only the classification for
  \(q\le10\). The all-\(q\) and asymptotic conclusions rest on the symbolic
  proof.

## Blockers / Risks

- No blocker.
- Residual risk is human review of the weighted slot-majorization argument,
  the block-stub converse, and the strict order of the fixed-\(k\), \(n\),
  and \(k\) limits.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** exact all-\(q\) equality classification, exact
  finite selected-prefix bound, positive all-middle cubic theorem, passing
  \(q\le10\) oracle, repository regressions, and final source/diff audits.
- **Files changed:** authoritative proof, stable memory, roadmap, current
  status, and this task dossier; no production or public test file.
- **Files to read first:** the new equality-classification subsection in
  `research/FIXED_ORDER_CYCLE_RATIO.md` and `EVIDENCE.md`.

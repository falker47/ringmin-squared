# TASK LOG - Four-Prefix One-Use Charging

Append-only. Add a new entry to correct previous information.

## 2026-07-16 - Startup And Expected Delta

- Read the operating contract, project brief, stable knowledge, current
  status, CR28ax--CR28cg, the three-prefix STRICT dossier, and the relevant
  bounded-history diagnostics.
- Confirmed a clean `main` worktree at
  `59d152ee0308702fef1a2dfdafaafb6af3f6ebe0`.
- Classified the task as STRICT and fixed the protected scope: no parameter
  optimization, finite rounding, limiting-prefix passage, or protected
  production/certification/enumeration change.
- Defined the expected result as either the exact four-prefix one-use theorem
  plus an independent bounded oracle, or one exact reproducible obstruction.

## 2026-07-16 - Exact Four-Prefix Derivation

- The five coefficients
  \(1-\lambda_1,\lambda_1-\lambda_2,\lambda_2-\lambda_3,
  \lambda_3-\lambda_4,\lambda_4\) give the exact uniform convex-height
  region and telescope to four disjoint split segments.
- Proved that each literal history canonically partitions the original edge
  set into injectively charged edges and unused edges. Clarified that this is
  combinatorial uniqueness, not uniqueness of a numerical decomposition when
  some slack vanishes.
- Proved the recursive invariant through all three boundaries and arbitrary
  nesting depth, then derived the four local segment floors, finite lower
  bound, inner-cycle comparison, and unoptimized fixed-parameter \(C_4\).
- No parameter optimization, finite rounding, \(k\to\infty\) passage, or
  claim for \(k\ge5\) was made.

## 2026-07-16 - Independent Literal Oracle

- Added a standalone standard-library Fraction oracle with no project or
  test-helper imports.
- Exhausted all 840 current-edge histories from
  \(C_0=(11,14,12,13)\) with insertions \(10,9,8,7\). All 840 final cycles
  are distinct.
- Verified base/recursive search-tree split counts \((4,12,48,240)\) and
  \((0,8,72,600)\), 120 fourth splits with two inserted endpoints, exact local
  floor sum \(9239/72\), and four-segment lower bound \(53879/72\).
- The first format check requested one mechanical rewrite. After formatting,
  the oracle, Ruff check, and format check all passed.

## 2026-07-16 - Authoritative Synchronization

- Added the primary proof as CR28de--CR28dk.
- Synchronized only the project brief, stable knowledge, current status,
  all-\(n\) note, and research roadmap. Historical task dossiers remain
  unchanged because their scope statements are still accurate.
- Preserved the best optimized numerical lower coefficient \(C_{3,*}\);
  the new \(C_4\) theorem is deliberately parametric and unoptimized.

## 2026-07-16 - Verification, Audits, And Handoff

- Fixed-order-cycle-ratio module: 101 passed. Complete local suite: 277
  passed.
- Checked-artifact verifier passed 4 certificates and 76 local brackets;
  schema selection passed 4 tests.
- The oracle passes execution, Ruff check, and Ruff format check. Equation-tag
  audit found 296 unique tags; all changed Markdown display and environment
  delimiters are balanced.
- Three independent read-only audits checked the proof, oracle, synchronized
  sources, Markdown, and scope. They identified one omitted \(r\le n-2\)
  condition in two summaries, ambiguity between search-tree split counts and
  leaf-weighted occurrences, and one transient status wording inconsistency.
  All were corrected; stable reaudit found no remaining defect.
- Final changed-path and protected-scope inspection, git diff --check, and
  final diff review passed.
- Set the task and project status to READY_FOR_REVIEW for user inspection and
  a manual commit decision.

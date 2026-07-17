# TASK STATUS - Five-Prefix Explicit Asymptotic Witness

Last update: 2026-07-17

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** specialize the exact normalized simplex at \(k=5\) and
  \(\alpha=13/30\), combine it with arbitrary finite-prefix one-use charging,
  and derive an explicit rational asymptotic lower witness strictly stronger
  than \(C_{4,*}\).
- **Expected output:** exact \(\beta_i,\lambda_i\), proof of strict all-middle
  admissibility, complete rational coefficient, exact comparison with
  \(C_{4,*}\), both liminf corollaries, and one standalone Fraction diagnostic.

## Scope

- **In scope:** the fixed \(k=5\) normalized-simplex row, the already proved
  arbitrary finite-\(k\) charging theorem, one rational density, exact
  algebra, fixed-parameter asymptotics, authoritative synchronization, and one
  dossier-local diagnostic.
- **Out of scope:** finite rounding, global \(k=5\) parameter optimization,
  uniformity in growing \(k\), production code, tests, artifacts, schemas,
  backends, serialized certificates, enumeration, and new geometric input.

## Verified Facts

- Startup used a clean main worktree at
  \(8dc7d2313349136c5c1fc21e098829dcffb2b742\).
- The exact \(k=5\) simplex and finite-\(k\) charging theorem are separate
  established inputs.
- The fifth simplex row is
  \[
  M_5={722599396919860307414438404
   \over2725902074099388500860861827}.
  \]
- At \(\alpha=13/30\), all five rational cutoffs and weights are strictly
  ordered and middle-clipped.
- The resulting rational coefficient is
  \[
  C_{5,\mathrm{rat}}
  ={2263404122555368590593580404287
   \over8177706222298165502582585481000}.
  \]
- Exact algebra gives
  \(C_{5,\mathrm{rat}}>75/271>C_{4,*}\).
- The corresponding liminf bounds for \(\Lambda_n\) and \(R_2^*(n)\) follow
  from the fixed-parameter charging limit and existing additive sandwich.

## Assumptions / Inferences

- Strict continuous admissibility gives integer cutoff admissibility for all
  sufficiently large \(n\); no threshold or finite rounding claim is made.
- The geometric liminf is a corollary of existing geometry, not a new
  geometric theorem.

## Decisions And Rationale

- Use the exact \(k=5\) simplex maximizer at the user-selected rational
  \(\alpha\), without optimizing \(\alpha\) or the full parameter tuple.
- Use \(75/271\) as a rational separator so both strict comparisons reduce to
  explicit positive integers.
- Add no executable beyond the requested standalone Fraction diagnostic.

## Plan And Expected Delta

- Record the exact derivation in the primary proof note.
- Add the standalone diagnostic and synchronize all authoritative summaries.
- Run proportional mathematical, repository, source-hygiene, and final-diff
  checks.

## Verification

- **Checks:** standalone diagnostic; Ruff lint/format; focused and full
  pytest; checked-artifact and schema verification; equation/Markdown,
  encoding, protected-scope, independent-proof, synchronization, and final
  diff audits.
- **Observed result:** diagnostic PASS; Ruff PASS after one mechanical format
  correction; 101 focused and 283 full tests PASS; 4 certificates with 76
  local brackets and 4 schema tests PASS; 327 equation tags are unique and
  all changed-source environments balance. All three independent audits,
  protected-scope inspection, encoding checks, complete diff inspection, and
  `git diff --check` PASS.
- **Limitations:** the exact computation corroborates but does not replace
  the proof; hosted GitHub Actions were not inspected.

## Blockers / Risks

- No blocker. Exactly the ten intended files changed, and the corrected
  status/dossier files contain no control characters.

## Next Atomic Action

- User review and, if accepted, manual commit.

## Handoff

- **Last verified result:** proof, diagnostic, exact comparison, regressions,
  source structure, all independent audits, and final diff checks pass.
- **Files changed:** five authoritative research/project sources,
  CURRENT_STATUS.md, and this four-file dossier.
- **Files to read first:** research/FIXED_ORDER_CYCLE_RATIO.md and this
  dossier.
- **Suggested manual commit message:**
  Add explicit five-prefix asymptotic witness.

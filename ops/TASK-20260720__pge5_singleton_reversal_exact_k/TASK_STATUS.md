# TASK_STATUS - TASK-20260720 / PGE5 Singleton-Reversal Exact K

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** evaluate exactly the one prescribed PGE5 singleton-reversal
  bijection on \(n=10m+4\), \(m\ge2\); prove its support and \(W=W_n\);
  classify every induced-\(K\) maximizer; prove or refute the proposed score
  reduction and coefficient; and compare it pointwise with canonical K825.
- **Expected output:** one symbolic fixed-core proof, one standalone bounded
  max-plus/all-arcs diagnostic, synchronized durable memory, and no result
  outside the one-map combinatorial scope.

## Scope

- **In scope:** only PGE5-1--PGE5-26, the map (KRPGE5-1), its exact support,
  literal doubleton and empty ranges, all deletion gains and compressed
  shortcuts including the cyclic cut, exact block score, target identity,
  five residue branches, and same-row K825 comparison.
- **Out of scope:** every other new bijection, Ferrers permanent, production
  or test changes, angular or geometric evaluation, global \(K\)-minimization,
  and global optimality.

## Verified Facts

- Startup found a clean `main` worktree at the user-accepted baseline
  `15ba9f9c58e8c7783ec2ad39d8eaa44b1be50318`.
- The accepted KPGE5 map shifts every path after \(q\) monotonically; the new
  map instead keeps that shift only through the doubleton and reverses the
  complete singleton block.
- KRPGE5-1--KRPGE5-32 prove that the new map is supported, has \(W=W_n\),
  has sole argmax \(B_m=\{4m+1,\ldots,10m+4\}\), and has exact score
  \[
  K_*={1714m^3+2439m^2+24mq+965m+12q^2+60q+120\over6}.
  \]
- The target is true:
  \(K_\uparrow-K_*=(m-1)(m-2)(m-3)/3\). Hence the fixed-family cubic
  coefficient is \(857/3000\), and K825 is strictly larger on every row.
- The unique deletion minimum is \(36m+20\). The unique shortcut minimum is
  \(9\) at the genuine closing arc for \(m=2\), and \(4m+2\) at \(c_0\)
  for \(m\ge3\).

## Assumptions / Inferences

- None. The all-\(m\) statements are exact symbolic theorems; bounded
  computation is classified only as corroboration.

## Decisions And Rationale

- Reuse only the exact general shortcut identity (K825-6)--(K825-9) and the
  accepted PGE5 support theorem; derive every map-specific gain, shortcut,
  score, and comparison explicitly.
- Keep the diagnostic task-local and standard-library-only, with a
  candidate-free optimization layer and a separate all-arcs traversal.

## Implemented Delta

- Added Section 21 to `research/FIXED_ORDER_CYCLE_RATIO.md` and synchronized
  its compact theorem in stable memory and the roadmap.
- Added one standalone diagnostic and this STRICT dossier.
- Changed no production file or test.

## Verification

- **Checks:** symbolic derivation and independent algebra review; standalone
  max-plus/all-arcs diagnostic; document/tag/link audit; scoped static checks;
  repository tests and final diff inspection.
- **Observed result:** diagnostic PASS on \(m=2,\ldots,30\) and formulas
  through \(m=1000\); scoped Ruff PASS; full pytest `283 passed`; focused
  schema pytest `4 passed`; all four certificates and 76 local brackets
  verify; tag/link/scope, diff, whitespace, and cache audits PASS.
- **Limitations:** bounded computation corroborates rather than proves the
  all-\(m\) theorem; local execution is not hosted CI.

## Blockers / Risks

- No blocker.
- Residual risk is transcription or external-review error in the long
  symbolic proof; independent derivations, bounded computation, and targeted
  audits found none.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** implementation, symbolic theorem, bounded
  diagnostic, repository verification, durable memory, and final hygiene are
  complete.
- **Files changed:** proof note, stable memory, status/roadmap, and the one
  new task dossier; no production or test file.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md` Section 21,
  `exact_diagnostic.py`, and `EVIDENCE.md`.
- **Suggested manual commit message:**
  `Prove exact K for the PGE5 singleton reversal`.
- **Proposed next fresh task:** post-review audit of KRPGE5-1--KRPGE5-32 and
  the standalone diagnostic at the reviewed commit.

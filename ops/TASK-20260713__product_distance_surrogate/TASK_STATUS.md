# TASK_STATUS - TASK-20260713__product_distance_surrogate / Product-Distance Surrogate

Last update: 2026-07-13

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** formalize the exact product-distance surrogate for regular-direction core constructions and determine its finite optima for `n=3..11`.
- **Expected output:** all-`n` proofs, exact bounded enumeration code, focused tests, a concise research note, aligned durable memory, and complete verification without certificates, schemas, artifacts, or a CLI.

## Scope

- **In scope:** exact surrogate definitions and implications; tail obstruction via oriented positional gaps; the accepted `n>=12` insertion transfer; exact all-pairs scoring; canonical rotation/reflection enumeration through `n=11`; zigzag and tail comparisons; tests and documentation.
- **Out of scope:** enumeration beyond `n=11`; geometric certificates; JSON artifacts or schemas; CLI work; exact geometric optimality claims; commits, pushes, and upstream changes.

## Verified Facts

- Required startup files and relevant lower-bound, insertion, regular-core, zigzag, code, test, and dossier sources were inspected; the initial Git tree was clean.
- Independent mathematical and computational audits agree that the rendered fractions mean \(W(\sigma)=\max ij/d_\sigma(i,j)\), \(R=NW(\sigma)/\pi\), and \(W(\sigma)\ge P_{m,n}/N\).
- The existing full-order canonicalizer cannot be called directly for the core labels `2..n`; its largest-first and second-less-than-last convention can be adapted.
- The implementation and exact table now agree with an independent full
  `n=3..11` enumeration that does not import the new module or use its cutoff.
- Focused tests, the full repository suite, and checked-artifact semantic
  verification pass.

## Assumptions / Inferences

- Exact finite enumeration is distinct from an all-`n` proof and from a geometric certificate.
- No all-`n` formula for \(W_n\) is inferred solely from the `n=3..11` table.

## Decisions And Rationale

- Use a dedicated source module with `Fraction` outputs and integer cross-product comparisons.
- Enforce both `n<=11` and a deterministic canonical-order work ceiling before generating permutations.
- Treat the two-element core at `n=3` explicitly; use the adapted dihedral convention for `n>=4`.
- Add a new concise research note because this surrogate is a distinct bounded task, while citing rather than duplicating accepted proofs.

## Plan And Expected Delta

- Implement exact scorer, pair diagnostics, canonization, tail obstruction, and bounded enumeration. COMPLETE.
- Add focused tests and reproduce the independently checked table. COMPLETE.
- Record theorems, finite results, limitations, and the absence of a justified extrapolative conjecture. COMPLETE.
- Update stable memory and run focused, full, artifact, and diff verification. COMPLETE.

## Verification

- **Checks:** exact table probe; focused surrogate/zigzag/tail/insertion tests;
  full pytest; checked-artifact semantic verifier; independent mathematical,
  code, table, and documentation reviews; UTF-8/path/whitespace checks; final
  Git status, diff, and `git diff --check`.
- **Observed result:** exact table reproduced; focused tests passed `24/24`;
  full suite passed `137/137`; checked-artifact verifier accepted 4
  certificates, 76 local brackets, and the `n=3..6` summary; independent
  mathematical and code reviews found no defect; ten-path scope, strict UTF-8,
  trailing-whitespace, complete diff, and `git diff --check` checks passed.
- **Limitations:** finite tests and enumeration do not prove an all-`n` formula
  or exact geometric optima; Python 3.11 compatibility was checked statically,
  while the local runtime was Python 3.14.3.

## Blockers / Risks

- No current blocker.
- Audited risks were a reversed fraction from rendered notation, missing
  non-adjacent pairs, mishandling `n=3`, losing exact ties at a cutoff, and
  overstating finite enumeration; tests and independent reviews found none of
  these defects.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** focused/full tests, checked-artifact verification,
  independent mathematical/code/table reviews, and final scope/UTF-8/diff
  hygiene all pass.
- **Files changed:** exact source module, focused tests, concise research note,
  project brief/knowledge/status/roadmap, and this task dossier.
- **Files to read first:** `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `src/power_ringmin/product_distance.py`, `tests/test_product_distance.py`,
  and `EVIDENCE.md`.

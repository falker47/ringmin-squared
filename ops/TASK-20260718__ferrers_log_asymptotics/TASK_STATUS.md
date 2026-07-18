# TASK_STATUS - TASK-20260718__ferrers_log_asymptotics / Ferrers Log Asymptotics

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** derive a rigorous all-\(m\) asymptotic theorem for
  \(\log\mathsf F_m^{\rm lab}\) directly from the exact PG69 product.
- **Expected output:** an explicit \(O(\log m)\) remainder bound, complete
  ceiling and boundary audit, one independent growing-row residual
  diagnostic, and synchronization of only the pertinent authoritative
  sources.

## Scope

- **In scope:** the PG69 labelled Ferrers product for \(m\ge3\), the exact
  ceiling, the singular range \(j/m\to0\), both column endpoints, the dual
  triple/singleton row transition, and canonical injectivity only as a
  downstream interpretation.
- **Out of scope:** permutation or matching enumeration, production or test
  code, schemas, artifacts, certificates, alternative scaffolds, global
  optimization, and every geometric conclusion.

## Verified Facts

- PG69 gives the exact labelled count and PG70 its dual row product.
- The proposed coefficient
  \(14\log2+6\log3-10\log5-2\) has been recovered independently from the
  homogeneous comparison product.
- Three independent read-only derivations agree on the ceiling, singular,
  endpoint, and triple/singleton controls.
- PG84 proves the explicit residual envelope for every \(m\ge3\), and PG85
  proves the requested asymptotic with the proposed coefficient unchanged.
- The final diagnostic, static checks, focused and full regressions, schema
  tests, checked-artifact verifier, and independent audits pass.

## Assumptions / Inferences

- No new mathematical assumption is used. All logarithms are natural.
- Finite diagnostic rows will be classified as bounded numerical
  observations, not as the proof of the all-\(m\) theorem.

## Decisions And Rationale

- Use an exact integer-rounding identity before any asymptotic comparison, so
  equality at a ceiling cutoff is retained.
- Separate the literal no-ceiling factor from the lower comparator used in
  the proof, because their logarithmic corrections have opposite signs.
- Isolate \(\log(j/m)\) by an exact factorial product and monotone integral
  bounds, avoiding a nonuniform Euler--Maclaurin step at zero.

## Plan And Expected Delta

- Add PG74--PG85 to `research/PRODUCT_DISTANCE_SURROGATE.md`.
- Add one standalone dossier-local residual diagnostic and record its bounded
  output.
- Synchronize only `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`,
  `research/NEXT_RESEARCH_STEPS.md`, and this dossier.
- Run focused and repository verification, independent audits, and final diff
  hygiene before setting `READY_FOR_REVIEW`.

## Verification

- **Checks:** standalone residual diagnostic and predecessor Ryser oracle;
  Ruff lint and format; compile; 49 focused tests; complete 283-test suite;
  four schema tests; checked-artifact verifier; three independent proof,
  code, and synchronization audits; Git status, complete diff, whitespace,
  cache, and scope inspection.
- **Observed result:** thirteen growing rows through \(m=262144\) satisfy all
  asserted envelopes and exact endpoint/row identities; every final static,
  test, artifact, audit, and hygiene check passes. The first two Ruff format
  checks required mechanical formatting. The first full-suite run retained
  252 passes and 31 setup errors caused solely by sandbox denial of the
  isolated `C:\tmp` directory; the approved rerun passed all 283 tests.
- **Limitations:** the error bound is \(O(\log m)\) and does not determine a
  finer logarithmic coefficient.

## Blockers / Risks

- No blocker.
- Main proof risk is confusing the direct ceiling/no-ceiling delta with the
  positive comparison against the lower auxiliary factor; the notation keeps
  them separate.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** PG84--PG85, the independent diagnostic, complete
  regressions, artifact checks, audits, and final hygiene pass.
- **Files changed:** `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `research/NEXT_RESEARCH_STEPS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, and the four files in this dossier.
- **Files to read first:** `research/PRODUCT_DISTANCE_SURROGATE.md`, PG74--PG85.

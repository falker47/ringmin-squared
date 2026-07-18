# TASK STATUS - Global Finite-Prefix Envelope

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** determine whether \(C_{\mathrm{AF}}\) is the supremum of
  the complete continuous finite-prefix template family, including every
  clipped regime, rather than only the all-middle subfamily.
- **Expected output:** an exact arbitrary-\(k\) compact clipped envelope,
  classification of every finite-\(k\) global maximizer or a minimal exact
  counterexample, the resulting family supremum, one small independent exact
  diagnostic, authoritative synchronization, and proportional verification.

## Scope

- **In scope:** exact continuous coefficient optimization for every fixed
  finite \(k\); clipped \(0/M/H\) regimes; one dossier-local standard-library
  diagnostic; pertinent mathematical and status sources.
- **Out of scope:** finite rounding, production source, test modules,
  artifacts, schemas, backends, certificates, enumerators, and enumeration
  limits.

## Verified Facts

- Startup used a clean main worktree at
  807d79eca25249b404ce9b3374472e19c67e5adf.
- Coordinatewise clipping is exact for arbitrary finite \(k\), and the
  normalized compact problem has a Bellman/Darboux-sum formulation.
- The limiting clipped integral excludes the high and low density regions
  from global optimality.
- For every finite \(k\), the unique compact global maximizer is strict
  all-middle; no counterexample exists.
- The exact full-family supremum is \(C_{\mathrm{AF}}\), and no finite
  \(k\) attains it.

## Assumptions / Inferences

- None beyond the previously proved clipping, normalized-simplex, and
  finite-prefix charging theorems.

## Decisions And Rationale

- Use the true piecewise clipped floor before taking any \(k\)-supremum.
- Distinguish the full clipped envelope from the formal polynomial
  relaxation, which is not sharp in high regimes.
- Add only one independent Fraction diagnostic and change no protected
  implementation path.

## Plan And Expected Delta

- [x] Complete STRICT startup and inspect the relevant compact proofs.
- [x] Derive the arbitrary-\(k\) clipped Bellman envelope.
- [x] Prove the global all-middle classification and exact supremum.
- [x] Run the sole exact diagnostic.
- [x] Synchronize the pertinent authoritative sources.
- [x] Complete proportional verification and final diff review.

## Verification

- **Checks:** the new diagnostic and Ruff checks; three pertinent historical
  exact diagnostics; full pytest; checked-artifact and schema verification;
  strict source structure, stale-claim, scope, Git diff, and three independent
  read-only audits.
- **Observed result:** new diagnostic PASS with 300 Bellman states and 12
  fixed-\(k\) rows; historical diagnostics PASS with 203,489 grid states,
  332,640 histories, and 21 five-prefix regimes; full pytest PASS 283;
  artifact verifier PASS for four certificates and 76 brackets; schema suite
  PASS 4; strict source structure PASS for 10 paths and 395 unique equation
  tags; final scope and diff checks PASS.
- **Limitations:** the bounded diagnostics corroborate but do not replace the
  all-real proof; hosted CI remains outside local verification.

## Blockers / Risks

- No blocker.
- Main proof risk addressed: the formal \(E_k\) is not used as a high-regime
  upper envelope.

## Next Atomic Action

- User manual review and commit decision.

## Handoff

- **Last verified result:** exact full-family proof, synchronization,
  diagnostics, regression suite, independent audits, and final diff hygiene
  all pass.
- **Files changed:** six pertinent authoritative Markdown files plus this
  task dossier and its sole standalone exact diagnostic.
- **Files to read first:** research/FIXED_ORDER_CYCLE_RATIO.md, then this
  dossier.

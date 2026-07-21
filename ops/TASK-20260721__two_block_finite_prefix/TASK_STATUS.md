# TASK STATUS - Two-Block Finite-Prefix Charging

Last update: 2026-07-21

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** analyze one separator-density extension of
  CR28dr--CR28dw29 with two disjoint contiguous insertion blocks, two
  nonoverlapping original-edge slack pools, and the global recursive
  child-edge invariant.
- **Expected output:** an exact finite charging inequality, exact normalized
  objective, explicit no-double-charge proof, and either a rational
  coefficient above \(C_{\mathrm{AF}}\) with a finite theorem or an exact
  ansatz upper bound at most \(C_{\mathrm{AF}}\).

## Scope

- **In scope:** CR28ax--CR28dw29, one density separator, the convex bridge,
  two history-relative original-edge pools, exact continuous optimization,
  one dossier-local exact oracle on a small instance, and synchronization of
  authoritative research and memory files.
- **Out of scope:** production source, test modules, schemas, artifacts,
  finite certificates, verifier backends, production enumeration limits,
  unrelated constructions, a global upper bound on \(\Lambda_n\), and any
  claim of an exact geometric leading constant.

## Verified Facts

- Startup used a clean `main` worktree at
  `3390215b751c3b67fed1fd8d7f37a00ec1df275d`.
- A valid two-block construction requires the lower block to remain anchored
  at the absolute separator height. Mixing the two block maxima by \(h\)
  forces
  \[
  \lambda_i^+=h+(1-h)a_i,\qquad \lambda_j^-=hb_j.
  \]
- Original edges first split above and below the separator form two
  history-relative disjoint pools. Splitting an original edge removes it
  permanently, so no original edge is charged twice.
- The descending child-edge invariant crosses the separator without a reset;
  lower descendants of upper splits remain recursive and receive no new
  original slack.
- Concatenating the effective rows gives exactly one ordinary finite-prefix
  row. Conversely, every strictly density-ordered finite-prefix row with at
  least two coordinates has a two-block factorization, and the compact
  closures coincide after allowing weak orders.
- Therefore, at fixed \(K=k_++k_-\), the compact optimum is \(C_{K,*}\), and
  \[
  \sup_{k_+,k_-\ge1}C^{\mathrm{2B}}_{k_+,k_-}
  =C_{\mathrm{AF}}={434+4\sqrt2\over1587}.
  \]
  This sharp supremum is not attained at finite \(K\).
- The sole oracle passes all 840 four-split histories, including 504 using
  both slack pools and 64 deep cross-separator descendants without a direct
  upper-label endpoint.

## Assumptions / Inferences

- The pool partition must be history-relative; the separator density alone
  cannot preassign a fixed subset of original edges for every literal
  history.
- The exact upper bound classifies this ansatz only. It is not an upper bound
  on the true \(\Lambda_n\).

## Decisions And Rationale

- Mix the upper absolute-prefix maximum with the lower maximum anchored at
  the separator before assigning any slack.
- Keep the original \(r\) in the recursive lower bound across both blocks.
- Classify the resulting ansatz through both an explicit Darboux-integral
  bound and an exact inverse factorization to the known finite-prefix family.
- Use exactly one standalone standard-library oracle, with no production or
  test imports.

## Plan And Expected Delta

- [x] Complete STRICT startup and inspect CR28dr--CR28dw29.
- [x] Prove the bridge, two-pool partition, recursive invariant, and finite
  inequality.
- [x] Derive and classify the exact normalized objective.
- [x] Add and run the one bounded exact oracle.
- [x] Synchronize the primary proof, all-\(n\) note, stable knowledge,
  roadmap, and current status.
- [x] Complete proportional regressions, structural audits, and final diff
  inspection.

## Verification

- **Checks completed:** oracle and Ruff; focused and full pytest;
  checked-artifact verifier; schema regression; three pertinent historical
  exact diagnostics; equation/environment and encoding audits; three
  independent read-only reviews; protected-scope, complete diff, and Git
  whitespace checks.
- **Observed result:** oracle PASS on 840 histories; focused pytest PASS 101;
  full pytest PASS 283; four checked certificates and 76 local brackets PASS;
  schema PASS 4; arbitrary-charging, global-clipped-envelope, and
  all-fixed-\(k\) diagnostics PASS; all 856 primary equation tags are unique,
  the ten new tags occur once, and all 1,353 standalone display pairs and
  relevant environments balance. All nine intended files are UTF-8 without
  BOM, LF-only, and LF-terminated. Independent audits and final Git checks
  pass.
- **Limitations:** the oracle is bounded corroboration, not the all-history
  proof; hosted CI has not run this uncommitted diff.

## Blockers / Risks

- No blocker.
- Residual risk is limited to user review and hosted CI not yet running the
  uncommitted changes.

## Next Atomic Action

- User review and manual commit decision. Do not begin another research task
  in this chat.

## Handoff

- **Last verified result:** exact theorem, bounded oracle, regressions,
  structural checks, three independent audits, and final diff inspection all
  pass.
- **Files changed:** authoritative proof/summary/status Markdown plus one new
  dossier and its oracle.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md` and
  `EVIDENCE.md`.
- **Suggested manual commit message:**
  `Classify two-block finite-prefix charging`.

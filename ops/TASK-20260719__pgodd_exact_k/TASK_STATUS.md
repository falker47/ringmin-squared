# TASK_STATUS - TASK-20260719 / PGODD Exact K

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** evaluate exactly the induced-subset objective `K` for the
  already fixed odd-\(v\) map (PGODD-6) on `n=10m+8`, `m>=1`, without
  changing the candidate.
- **Expected output:** an all-\(m\) theorem or an exact qualified obstruction,
  including the core order, every maximizing subset, boundary rows, complete
  deletion-gain and compressed-shortcut proof, exact residue formulas, and
  same-row comparison with K825.

## Scope

- **In scope:** the single fixed PGODD-6 order; induced cyclic product sums;
  max-plus and all-oriented-arc corroboration; doubleton, singleton block,
  cyclic closure, equality cases, and `m=1,2`.
- **Out of scope:** changing or searching the candidate; order-family or
  matching enumeration; exact angular thresholds; geometry; global
  `K`-minimality; and global optimality.

## Verified Facts

- Startup found a clean main worktree at
  `513f294d6c7e79e899d953f8b197ae3e23cded73`.
- The prior task fixed (PGODD-6) before scoring and proved its construction,
  Ferrers compatibility, cyclic boundaries, and exact `W` score.
- Three independent read-only derivations agree on a unique tail backbone,
  one exact floor-polynomial score, and boundary changes only in the minimum
  shortcut witness.
- The complete symbolic proof is now (KPGODD-1)--(KPGODD-36). It proves
  uniqueness, all nine elimination-gain classes, every shortcut length and
  equality case, the doubleton, singleton block, cyclic closure, five residue
  branches, and strict same-row K825 comparison.
- The sole independent diagnostic passes on all declared finite domains.

## Decisions And Rationale

- Retain (PGODD-6) literally and reconstruct its cyclic core word directly.
- Use the isolated-hole identity (K825-6)--(K825-9) only after auditing every
  deletion gain and every compressed shortcut class.
- Add one standalone standard-library diagnostic that constructs no other
  order and keeps all finite limits explicit.

## Plan And Expected Delta

- Prove the exact backbone and all maximizing subsets.
- Derive the block sum, five `m mod 5` branches, and strict K825 comparison.
- Run the independent diagnostic and repository-proportional verification.
- Synchronize only the pertinent research, roadmap, durable-memory, and task
  sources; finish as `READY_FOR_REVIEW`.

## Verification

- **Checks:** exact diagnostic, syntax, Ruff lint and formatting, scoped
  source audit, full pytest, checked-artifact schema tests, independent
  checked-artifact verification, two mathematical reviews, one diagnostic
  review, complete tracked/untracked diff inspection, and whitespace hygiene
  all pass. Ruff formatting was applied after its first check found one
  mechanical delta. An initially overbroad audit of the entire historical
  research file was replaced by the correctly scoped Section 17 audit.
- **Observed result:** the diagnostic checks 1,000 formula rows, 30 max-plus
  rows with 39,461,580 transitions, and 1,007,210 proper oriented arcs,
  including 1,000,460 nontrivial shortcuts. Full pytest reports 283 passed;
  the focused schema suite reports 4 passed; the checked-artifact verifier
  reports four certificates and 76 local brackets; the source audit finds 36
  sequential unique tags and 42 balanced displays.
- **Limitations:** finite computation will corroborate, not prove, the
  symbolic all-\(m\) theorem.

## Blockers / Risks

- No blocker. Residual risk is manual review of a long symbolic proof.

## Next Atomic Action

- User review and manual commit decision. Do not begin the proposed research
  task in this chat.

## Handoff

- **Last verified result:** exact all-\(m\) theorem plus passing sole
  diagnostic.
- **Files changed:** fixed-order proof, pertinent product-distance/roadmap and
  durable-memory sources, and this task dossier with one diagnostic.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md` and this
  dossier's `EVIDENCE.md`.
- **Suggested manual commit message:** `Prove exact odd-v PG49-star induced K`.

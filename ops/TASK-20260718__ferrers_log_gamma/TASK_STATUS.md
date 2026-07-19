# TASK_STATUS - TASK-20260718__ferrers_log_gamma / Ferrers Logarithmic Coefficient

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** decide rigorously whether the exact PG69 labelled count has
  a logarithmic coefficient with bounded remainder, starting from PG74--PG85.
- **Expected output:** a proof or explicit obstruction, with separate
  factorial, smooth-perturbation, and floor/ceiling-rounding contributions;
  uniform treatment of the singular range, bulk, residue classes, and
  endpoints; and one formula-only standalone diagnostic.

## Scope

- **In scope:** the exact PG69 product; the PG74--PG85 decomposition;
  asymptotics of \(Z_m\), \(c_{m,j}/r_{m,j}\), and
  \(a_{m,j}/c_{m,j}\); exact cutoff hits; both endpoints; all five terminal
  residue classes.
- **Out of scope:** permutation or matching enumeration, production source,
  test modules, schemas, artifacts, alternative scaffolds, global
  optimization, and every geometric conclusion.

## Verified Facts

- The startup worktree was clean at commit
  `6e7a1b6e241899883d4432d670ef8c261b3ca02d`.
- PG80 isolates the exact factorial product and the only nonsmooth term is
  \(\Theta_m=\sum_j\log(a_{m,j}/c_{m,j})\).
- The written PG86--PG99 proof establishes \(\gamma=3/4\); three independent
  derivations and three post-write audits agree and find no mathematical
  issue.

## Assumptions / Inferences

- All logarithms are natural.
- Finite diagnostic rows are bounded numerical observations and do not prove
  the asymptotic theorem.

## Decisions And Rationale

- Use the exact identity
  \(c_{m,j}=j/2+j(j+1)/(2(j+8m+4))\) before estimating the rounding.
- Split at \(j\asymp\sqrt m\), where the parity bias changes to a
  mean-one-half sawtooth regime.
- Prove the sawtooth estimate by a jump-inclusive sum--integral lemma and
  dyadic Abel summation, so exact cutoff equalities and lattice subclasses
  remain in the argument.

## Plan And Expected Delta

- Add PG86--PG99 to `research/PRODUCT_DISTANCE_SURROGATE.md`.
- Add and run a standalone formula-only component diagnostic.
- Synchronize the pertinent authoritative memory and roadmap only.
- Run mathematical audits, focused static checks, relevant regressions, and
  final diff hygiene before setting `READY_FOR_REVIEW`.

## Verification

- **Checks:** formula-only component diagnostic and both predecessors; script
  Ruff lint/format and compile; 49 focused and 283 complete tests; three
  independent proof/diagnostic audits; complete diff, whitespace, tags,
  generated-cache, and scope hygiene.
- **Observed result:** 25 diagnostic rows through \(m=262144\) PASS; all five
  residue classes pass on four growing blocks; script static checks PASS;
  49 focused and 283 complete tests PASS; audits find no P0--P2 issue and all
  P3 clarity findings are incorporated. The initial full-suite sandbox run
  retained 252 passes plus 31 basetemp setup errors before the approved rerun.
  A broad Ruff probe retains unrelated pre-existing findings; scoped Ruff is
  clean. Exactly nine intended files are changed/new and final hygiene passes.
- **Limitations:** the theorem targets an \(O(1)\) remainder, not convergence
  of that bounded remainder.

## Blockers / Risks

- No blocker.
- Main proof risk is a nonuniform treatment of the sawtooth near its
  \(\sqrt m\) transition or silently discarding exact phase hits.

## Next Atomic Action

- User review and manual commit decision.

## Handoff

- **Last verified result:** PG86--PG99 and the formula-only diagnostic pass
  independent audits, all 283 repository tests, and final diff hygiene.
- **Files changed:** `research/PRODUCT_DISTANCE_SURROGATE.md`,
  `research/NEXT_RESEARCH_STEPS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`,
  `CURRENT_STATUS.md`, and the four files in this task dossier.
- **Files to read first:** `research/PRODUCT_DISTANCE_SURROGATE.md`,
  PG86--PG99.

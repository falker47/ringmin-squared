# TASK STATUS - Arbitrary Finite-Prefix One-Use Charging

Last update: 2026-07-17

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Objective:** generalize the five-prefix one-use combined-height charging
  theorem in `research/FIXED_ORDER_CYCLE_RATIO.md` to every finite
  admissible \(k\ge1\).
- **Expected output:** one exact indexed finite theorem with a convex
  \(k+1\)-term height combination, \(k\)-segment telescope, canonical one-use
  original-edge partition, boundary-count-independent recursive induction,
  and the requested finite bound.

## Scope

- **In scope:** CR28ax--CR28bd, CR28dr--CR28dw, every finite admissible
  prefix count, one optional dossier-local exact oracle limited to \(k=6\),
  and synchronization of the requested research and memory files.
- **Out of scope:** coefficient optimization, finite rounding, uniform
  growing-\(k\) asymptotics, \(k\to\infty\), exact residuals, geometric
  consequences, production code, tests, artifacts, schemas, backends,
  certificates, and production enumeration limits.

## Verified Facts

- Startup used a clean `main` worktree at
  `2897fa52af8e40808f3483647183b25e76eb04f9`.
- The five-prefix theorem already had the correct one-use partition and
  recursive endpoint invariant, but its quantifiers stopped at \(k=5\).
- For arbitrary finite \(k\), the ordered weights give one convex
  combination of \(0,H_1,\ldots,H_k\), which telescopes to \(k\) disjoint
  weighted segments.
- Selected base splits inject into the original edge set, so every original
  slack is canonically charged once or left unused over the selected range.
- Descending induction on inserted labels contains no segment-boundary count
  and covers arbitrary nesting through every finite number of frontiers.
- The exact finite inequality is
  \[
  \gamma^{(r)}_{1,n}\ge
  P_{r,n}+\sum_{i=1}^k(s_{i-1}-s_i)G_{n,\lambda_i}(s_i).
  \]
- The sole new dossier-local \(k=6\) oracle passes all 332,640 histories,
  including 720 histories charging all six original edges and 60,480 sixth
  splits between inserted endpoints.

## Assumptions / Inferences

- The normalized simplex remains independent context and is not used to
  prove charging.
- Pointwise validity for every finite admissible row does not supply
  thresholds, rounding, errors, or parameter control uniform in \(k=k(n)\).

## Decisions And Rationale

- Distinguish chronological prefixes \(\mathcal H_j\) from selected heights
  \(H_i\) to avoid an index collision.
- Prove the recursive invariant by descending insertion time, not by induction
  on \(k\), so the original slack pool is never reused.
- Use exactly one new oracle, limited to \(k=6\), as bounded corroboration.

## Plan And Expected Delta

- Replace the five-prefix proof section by an indexed finite theorem.
- Add the bounded \(k=6\) oracle and record its exact arithmetic.
- Synchronize the project brief, stable knowledge, status, roadmap,
  all-\(n\) summary, and this dossier.
- Run proportional regressions and inspect the final diff.

## Verification

- **Checks:** \(k=6\) oracle; Ruff lint and format; focused and full pytest;
  checked-artifact verifier; schema regression; equation tags and Markdown
  environments; stale-scope search; UTF-8/BOM/newline audit; three independent
  read-only audits; complete diff and whitespace checks.
- **Observed result:** all 332,640 oracle histories, the focused module, all
  283 local tests, 4 checked certificates with 76 local brackets, and 4 schema
  tests pass. Ruff passes. All 321 equation tags are unique; 576 standalone
  display pairs, 34 `aligned` pairs, and 7 `array` pairs balance.
  All ten changed/new files are UTF-8 without BOM, LF-only, and
  LF-terminated.
- **Corrected diagnostic failures:** the first Ruff format check requested
  mechanical reformatting and passed after applying the formatter. Two
  anti-refuso regexes were too broad and matched `quadratic`, then
  `\qquad`; the corrected token-level check reports zero bare
  `quad(` occurrences. These were command defects, not source failures.
- **Limitations:** bounded computation corroborates but does not prove the
  arbitrary finite-\(k\) statement. Hosted GitHub Actions were not inspected.

## Blockers / Risks

- No blocker. Three final read-only audits confirm that pointwise finite
  applicability is not confused with uniform asymptotic control for growing
  \(k(n)\).

## Next Atomic Action

- User review and, if accepted, manual commit. Do not begin the proposed next
  research task in this chat.

## Handoff

- **Last verified result:** indexed proof, bounded \(k=6\) oracle, all
  regressions, structure/encoding checks, and proof/synchronization audits
  pass.
- **Files changed:** proof note, project brief, stable knowledge, roadmap,
  all-\(n\) summary, current status, and this new dossier.
- **Files to read first:** `research/FIXED_ORDER_CYCLE_RATIO.md` and
  this dossier.
- **Suggested manual commit message:**
  `Prove arbitrary finite-prefix one-use charging`.

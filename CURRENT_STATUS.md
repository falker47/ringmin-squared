# CURRENT_STATUS - power-ringmin

Last update: 2026-07-14

- **Current phase:** exact fixed-order maximum cyclic ratio.
- **Current task:** formalize the complete-order STN cycle ratio, prove its
  fixed/global geometric sandwich, implement an exact scorer, and reproduce
  the bounded `n=3..8` prediction.
- **Task dossier:**
  ops/TASK-20260714__fixed_order_cyclic_ratio/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Exact Results

- DEFINITION: for a complete order \(\sigma\) of \(\{1,\dots,n\}\),
  \(q(C)\) counts `wrap_upper` edge occurrences and \(S(C)\) sums
  endpoint-index products over every directed edge occurrence, with
  multiplicity. Every directed closed walk has \(q(C)\ge1\).
- EXACT THEOREM: closed-walk decomposition reduces the maximum to simple
  directed cycles and defines the rational score
  \[
  \Lambda(\sigma)=\max_C{S(C)\over q(C)}.
  \]
- EXACT THEOREM: for every complete order and `n>=3`, the requested sandwich
  holds, with both endpoints actually strict:
  \[
  {\Lambda(\sigma)\over\pi}-n^2
  <\rho_\sigma
  <{\Lambda(\sigma)\over\pi}.
  \]
- EXACT THEOREM: with
  \(\Lambda_n=\min_\sigma\Lambda(\sigma)\),
  \[
  {\Lambda_n\over\pi}-n^2
  <R_2^*(n)
  <{\Lambda_n\over\pi},
  \qquad
  0<\Lambda_n-\pi R_2^*(n)<\pi n^2.
  \]
- EXACT THEOREM: the additive relation transfers normalized asymptotics but
  does not prove convergence or an exact constant. In particular,
  \[
  {2(\sqrt2-1)\over3}
  \le\liminf{\Lambda_n\over n^3}
  \le\limsup{\Lambda_n\over n^3}
  \le{8\over25}.
  \]
- DEFINITION / LIMITATION: \(\Lambda\) is a full-order directed-cycle objective;
  repository \(W\) is a core-order single-pair regular-direction objective.
  They and their minimizers are not identified.

## Finite Exact Computation

- VERIFIED FACT (FINITE EXHAUSTIVE EXACT COMPUTATION): exact canonical
  enumeration over `n=3..8` covers `(1,3,12,60,360,2520)` orders and gives
  \[
  (\Lambda_3,\dots,\Lambda_8)=(12,26,47,77,118,172).
  \]
  The canonical minimizer counts are `(1,3,4,15,24,84)`.
- VERIFIED FACT: the production scorer uses integer descending-path closure,
  a one-wrap macro graph, and Karp maximum-cycle-mean dynamic programming,
  constructing exact `Fraction` ratios only. It does not enumerate cycles.
- VERIFIED FACT: a direct simple-cycle oracle confined to tests agrees for
  every canonical complete order through `n=6`. Independent audits also
  compared the production scorer with a separate exact ratio algorithm on all
  2,956 bounded orders and found no discrepancy.
- INTERPRETATION: the bounded table is not an all-`n` formula, a geometric
  exact optimum, or an asymptotic theorem.

## Changes

- `research/FIXED_ORDER_CYCLE_RATIO.md` is the authoritative definition,
  proof, algorithm, bounded-experiment, \(W\)-comparison, and limitations
  note.
- `src/power_ringmin/fixed_order_cycle_ratio.py` provides the exact scorer and
  hard-bounded `3<=n<=8` canonical enumerator.
- `tests/test_fixed_order_cycle_ratio.py` provides the independent
  simple-cycle oracle, exhaustive prediction regression, symmetry, validation,
  preflight, multiplicity, and \(W\)-separation tests.
- Project brief, durable knowledge, fixed-order source note, roadmap, current
  status, and task dossier are synchronized.
- No interval backend, interval verifier, certificate, checked artifact,
  example, schema, or CLI changed.

## Verification

- CURRENT LOCAL VERIFIED FACT: the focused cycle-ratio suite passes all 21
  tests; an integrated exact-math/search suite passes all 82 tests.
- CURRENT LOCAL VERIFIED FACT: the complete repository suite passes all 194
  tests on local Python 3.14.3.
- CURRENT LOCAL VERIFIED FACT: checked-artifact semantic verification accepts
  4 certificates, 76 local brackets, and the `n=3..6` summary; all 4 schema
  tests pass.
- CURRENT LOCAL VERIFIED FACT: compilation and Ruff pass on both new Python
  files. Repository-wide Ruff was also executed and reports four pre-existing
  F401/F841 findings in three untouched files; they were not mixed into this
  bounded task.
- CURRENT LOCAL VERIFIED FACT: independent mathematical, implementation,
  algorithm, finite-experiment, and documentation reviews accept the theorem,
  code, tests, classifications, and bounded-domain guard.
- CURRENT LOCAL VERIFIED FACT: the final 11-path scope, strict-text, temporary-
  path, and diff-hygiene audit passes; no task-created temporary directory
  remains.
- ENVIRONMENT NOTE: one initial integrated run completed all but one setup;
  the sandbox denied `C:\tmp` for a `tmp_path` fixture. No test body failed.
  The workspace-local `--basetemp` rerun passed.
- CURRENT HOSTED STATUS: GitHub Actions on Python 3.11-3.13 has not been run
  for this worktree.

## Residual Limitations

- The four global Ruff findings predate and lie outside this task's diff:
  unused `defaultdict` and local `n` in `critical_structure.py`, unused `sys`
  in `fixed_order_artifact.py`, and an unused import in
  `tests/test_finite_results.py`.
- The exact cycle-ratio theorem changes no guarded `mpmath.iv` trust premise
  and certifies no new geometric finite optimum.
- No order enumeration beyond `n=8`, all-`n` formula for \(\Lambda_n\),
  convergence theorem, or exact leading constant is claimed.
- Local execution used Python 3.14.3, outside the hosted Python 3.11-3.13
  matrix.

## Proposed Next Task

In a fresh chat, perform a bounded repository-lint cleanup of the four
pre-existing F401/F841 findings and establish a clean global Ruff baseline,
without changing mathematical behavior.

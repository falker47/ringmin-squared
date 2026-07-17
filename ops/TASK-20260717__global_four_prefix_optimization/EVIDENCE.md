# EVIDENCE - Global Four-Prefix Optimization

## EV-01 - Baseline And Isolation

- Classification: verified fact.
- Check: STRICT startup source inspection and Git state.
- Result: clean `main` worktree at
  `24bea121d96906bfb884c57e3e97f189351d8791` before task edits.
- Limitation: this establishes isolation only; it is not evidence for the new
  optimization theorem.

## EV-02 - Compact Reduction And Exhaustive Branch Audit

- Classification: exact theorem.
- Check: direct algebra from the proved four-prefix coefficient followed by
  Bellman/KKT analysis on the compact ordered closure.
- Result: every weight clips independently to \(0\),
  \(4-(1+\alpha)/\beta_i\), or \(1\); the clipping map is ordered. Exactly
  fifteen regimes \(H^hM^m0^{4-h-m}\) remain.
- Result: exact predecessor-map derivatives prove the fixed-\(\alpha\) winning
  sequence `0000`, `MMMM`, `HMMM`, `HHMM`, `HHHM`; the `HHHH` transition has
  \(\alpha_4>1\). Every transition point and weight is rational and recorded
  in (CR28dq1)--(CR28dq3).
- Result: all five density facets, outer weight facets, internal diagonals,
  collisions, unused segments, and \(\alpha=0,1\) faces are classified.
  Effective three-prefix faces have maximum \(C_{3,*}\); none attains the
  global value.
- Corrective evidence: the first proof draft used an `HH` derivative formula
  at an `HM` interface. A read-only audit supplied a counterexample. The final
  proof now treats all `HM` and `H0` bases directly and reserves the formula
  for `HH`; the audit rechecked and accepted the correction.
- Limitation: this is an optimization of the already proved asymptotic
  four-prefix template, not a finite-\(n\) rounding theorem or a charging
  theorem for five prefixes.

## EV-03 - Exact Global Maximum And Three-Prefix Comparison

- Classification: exact theorem.
- Check: specialized nonnegative four-variable simplex certificate plus exact
  one-variable envelope differentiation and endpoint signs.
- Result: the normalized simplex maximum is
  \(M_4=3392752184748/13440604496449\), uniquely at
  \((3190338,2672508,2091528,1394352)/3666143\).
- Result: the unique global density is
  \[
  \alpha_*={18170840871749-3666143\sqrt{2903456040383}
   \over27631313622349},
  \]
  and the induced four cutoffs and weights are strict, ordered, and all in the
  `MMMM` branch. Hence the full nine-parameter maximum is unique.
- Result: the exact value is
  \[
  C_{4,*}
  ={597580022071777213687318156
   +21288970076515705538\sqrt{2903456040383}
   \over2290468477489828247376833403}
  =0.2767361498609895101\ldots .
  \]
- Result: a structural strict extension of the three-prefix optimizer and
  exact positive squared differences independently prove
  \(C_{3,*}<2767/10000<C_{4,*}\).

## EV-04 - Independent Exact Diagnostic

- Classification: computer-checked exact arithmetic, corroborating the proof.
- Command:
  `python -B ops\TASK-20260717__global_four_prefix_optimization\exact_diagnostic.py`.
- Result: `global four-prefix exact diagnostic: PASS`.
- Coverage: exact clipping-gap factorizations on rational grids, both \(C^1\)
  joins, all fifteen branch witnesses, transition coordinates and weights,
  collision reductions, the specialized nonnegative simplex identity,
  derivation of the cubic envelope from \(p+M_4(3\alpha-1)^3/8\), end-to-end
  original and reduced objective evaluation at the surd point, primitive
  irreducible polynomial, conjugate exclusion, isolating interval, and both
  exact separator inequalities.
- Bounded checks: normalized simplex grids at denominators 12, 24, and 48 have
  exact maxima \(1/4\), \(871/3456\), and \(27907/110592\), all below
  \(M_4\).
- Failed check retained: the first run stopped at an unequal-length
  `zip(..., strict=True)` in an adjacency assertion. The corrected adjacency
  pairing passes. A later audit found missing end-to-end assertions; the
  strengthened version now includes them and passes.
- Limitation: rational grids are bounded corroboration. The all-real result is
  the written exact proof, not the computation.

## EV-05 - Regression And Historical Cross-Checks

- Classification: verified fact.
- Command: `python -m pytest tests\test_fixed_order_cycle_ratio.py -q`.
- Result: 101 tests passed.
- Command: `python -m pytest -q`.
- Result: complete 283-test suite passed again in 67.9 seconds (the earlier
  full run passed in 64.6 seconds).
- Command:
  `$env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`.
- Result: 4 certificates and 76 local brackets verified.
- Command:
  `python -m pytest tests\test_checked_artifact_schema_validation.py -q`.
- Result: 4 tests passed. Pytest reported a non-failing cache-directory
  warning (`WinError 183`); no test body failed.
- Command:
  `python -B ops\TASK-20260716__four_prefix_charging\literal_oracle.py`.
- Result: PASS over all 840 literal histories.
- Command:
  `python -B ops\TASK-20260716__normalized_prefix_simplex\fraction_diagnostic.py`.
- Result: exact checks through \(k=8\) and 203,489 grid states passed.
- Interpretation: no regression or contradiction with either independent
  historical diagnostic was found.

## EV-06 - Static, Source, Scope, And Final-Diff Checks

- Classification: verified fact.
- Commands:
  `python -m ruff check ops\TASK-20260717__global_four_prefix_optimization\exact_diagnostic.py`
  and
  `python -m ruff format --check ops\TASK-20260717__global_four_prefix_optimization\exact_diagnostic.py`.
- Result: lint and format checks pass. The first format check requested one
  mechanical rewrite; the formatted file subsequently passes.
- Result: Markdown audit found balanced display delimiters and aligned/array
  environments, 315 unique equation tags, and no duplicate tag.
- Result: three independent read-only audits checked proof completeness,
  diagnostic algebra, and cross-source consistency. All actionable findings
  were corrected; the mathematical auditor found no remaining substantive
  defect after the `HM`/`H0` repair.
- Result: changed-path review shows only six authoritative Markdown sources
  and this task dossier. No production, test, artifact, schema, certificate,
  backend, enumerator, or limit file changed.
- Result: full diff inspection and `git diff --check` pass.
- Limitation: the user must still review the diff and decide whether to commit;
  Codex did not stage or commit anything.

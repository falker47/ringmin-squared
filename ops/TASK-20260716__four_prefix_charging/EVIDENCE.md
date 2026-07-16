# EVIDENCE - Four-Prefix One-Use Charging

## EV-01 - Baseline And Isolation

- Classification: verified fact.
- Check: STRICT startup source inspection and Git state.
- Result: clean `main` worktree at
  `59d152ee0308702fef1a2dfdafaafb6af3f6ebe0` before task edits.
- Focused regression: six historical three-prefix tests passed.
- Limitation: this is isolation and regression evidence, not the new theorem.

## EV-02 - Exact Four-Prefix One-Use Theorem

- Classification: exact method-specific theorem.
- Result: the exact convex height region telescopes to four disjoint weighted
  split segments; the literal history gives one canonical original-edge
  charged/unused partition; the recursive invariant covers every child edge
  through all three boundaries.
- Finite conclusion:
  \[
  \begin{aligned}
  \gamma^{(r)}_{1,n}\ge{}&P_{r,n}
  +(r-s_1)F_{1,n}
  +(s_1-s_2)F_{2,n}\\
  &+(s_2-s_3)F_{3,n}
  +(s_3-s_4)F_{4,n}.
  \end{aligned}
  \]
- Fixed-parameter conclusion: the exact unoptimized \(C_4\) gives the
  corresponding liminf bounds for \(\Lambda_n\) and \(R_2^*(n)\).
- Limitations: no optimization, finite rounding, \(k\to\infty\) passage,
  exact residual, convergence, or \(k\ge5\) result.

## EV-03 - Independent Bounded Exact Oracle

- Classification: verified bounded exact computation.
- Command:
  python -B ops\TASK-20260716__four_prefix_charging\literal_oracle.py.
- Result: 840 histories passed; 840 final cycles were distinct; recursive
  search-tree split counts were \((0,8,72,600)\); 120 fourth splits used an
  edge with two inserted endpoints; floor sum \(9239/72\); checked lower bound
  \(53879/72\).
- Independence: standard library only; no project, production, or test helper
  import.
- Limitation: bounded computation corroborates but does not replace the
  all-history proof.

## EV-04 - Oracle Static Checks

- Classification: verified computation.
- Initial result: Ruff format check requested one mechanical rewrite.
- Commands:
  python -m ruff check
  ops\TASK-20260716__four_prefix_charging\literal_oracle.py;
  python -m ruff format --check
  ops\TASK-20260716__four_prefix_charging\literal_oracle.py.
- Final result: the reformatted oracle passes execution, Ruff check, and Ruff
  format check.
- Interpretation: the failed initial format check is preserved as evidence;
  no mathematical assertion failed.

## EV-05 - Regression And Repository Verification

- Classification: verified computation.
- Commands and results:
  - python -m pytest tests\test_fixed_order_cycle_ratio.py -q: 101 passed.
  - python -m pytest -q: 277 passed.
  - $env:PYTHONPATH='src'; python -m
    power_ringmin.verify_checked_artifacts: 4 certificates and 76 local
    brackets passed.
  - python -m pytest tests\test_checked_artifact_schema_validation.py -q:
    4 passed.
- Structural checks: 296 equation tags are unique; display-math,
  aligned, and array delimiters are balanced in all changed Markdown files.
- Limitation: hosted GitHub Actions were not inspected.

## EV-06 - Independent Audits And Final Scope

- Classification: verified source inspection.
- Three independent read-only audits covered the all-history proof, oracle,
  synchronized claims, Markdown, and changed-path scope.
- Corrections: restored the full finite condition \(2\le r\le n-2\) in two
  summaries; clarified search-tree split counts; corrected a transient status
  phrase.
- Final result: no remaining mathematical, computational, synchronization,
  formatting, or scope defect.
- Protected scope: no production, test, artifact, schema, backend,
  certificate, enumerator, or enumeration-limit file changed.
- Final checks: changed paths inspected, git diff --check passed, and the
  complete diff was reviewed.

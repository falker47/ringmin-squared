# TASK LOG - Normalized Prefix Simplex

## 2026-07-16 - Startup And Scope

- Read `AGENTS.md`, `start.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`,
  the one-, two-, and three-prefix STRICT dossiers, the pertinent proof-note
  sections, and the roadmap.
- Confirmed a clean initial worktree on `main` at `726c8f0`.
- Classified the task as STRICT and retained the explicit prohibition on a
  general \(k\)-prefix charging theorem or new \(\Lambda_n\)/\(R_2^*(n)\)
  bounds.
- The focused pre-change command
  `python -m pytest tests\\test_fixed_order_cycle_ratio.py -q -k "two_prefix_global or three_prefix_global_simplex or three_prefix_global_compact or first_linear_density_parameter_optimization"`
  passed 8 tests.

## 2026-07-16 - Exact Compact Lemma

- Used degree-three tail homogeneity to derive the exact Bellman recurrence.
- Derived a telescoping nonnegative certificate for the full objective. Its
  equality conditions force every consecutive ratio and prove global
  uniqueness and strict interiority.
- Confirmed the proposed backward recurrence without correction and obtained
  \(M_k=4/[27(1-M_{k-1})^2]\).
- Factored \(T(u)-u\) exactly, proving strict monotonicity and
  \(M_k\to1/3\).

## 2026-07-16 - Documented Cases And Envelope

- Recovered exactly the existing one-prefix value \(4/27\), two-prefix value
  \(108/529\), and three-prefix value \(1119364/4785507\), including their
  documented maximizers and scale factors \(M_k/8\).
- Classified the displayed formal limit envelope on the whole compact closure:
  its unique maximum is \(1/3\) at \(\alpha=1\), while the strict domain has
  only that supremum.
- Separated this degenerate endpoint from the limiting all-middle equality
  branch. On \([1/3,1/2]\), the unique maximum is
  \((434+4\sqrt2)/1587\) at \((13-2\sqrt2)/23\).
- Recorded explicitly that neither result supplies charging or a new original-
  problem bound.

## 2026-07-16 - Independent Exact Diagnostic

- Added the dossier-local `fraction_diagnostic.py`, using no production or
  test helper.
- For \(k=1,\ldots,8\), it compares the scalar Bellman recurrence with the
  independent backward ratio recurrence, evaluates the objective directly,
  checks all exact stationarity equations, verifies strict feasibility and
  monotonicity, and recovers the three documented rows.
- A separate denominator-12 oracle compares literal rational-grid enumeration
  with a discrete Bellman computation over 203,489 literal grid tuples. Both
  return the same eight exact grid maxima, each no larger than \(M_k\).
- The diagnostic completed successfully under local Python 3.14.3. Static
  inspection confirms that its syntax and APIs remain compatible with the
  project's Python 3.11+ contract; no local Python 3.11 run is claimed.

## 2026-07-16 - Verification, Review, And Handoff

- `python -B ops\\TASK-20260716__normalized_prefix_simplex\\fraction_diagnostic.py`:
  all exact checks passed for \(k=1,\ldots,8\), including 203,489 literal
  denominator-12 grid tuples.
- Focused historical comparison: 8 passed. Complete
  `tests\\test_fixed_order_cycle_ratio.py`: 101 passed. Complete local suite:
  277 passed.
- Checked-artifact verification accepted all 4 certificates, 76 local
  brackets, and the \(n=3,4,5,6\) summary; schema selection passed 4 tests.
- Ruff and `py_compile` passed on the standalone diagnostic.
- Proof hygiene found 273 unique equation tags, no duplicate tags, 429/429
  balanced proof-note displays, 59/59 balanced roadmap displays, and no
  trailing whitespace; `git diff --check` passed.
- Three independent read-only audits checked the all-real proof, envelope
  domains, Fraction code, exact grid, documentation synchronization, and
  file scope. Their minor wording and evidence findings were applied; final
  reruns reported no defect.
- Confirmed that only the proof note, roadmap, and new task dossier changed.
  No charging extension, new original-problem bound, protected path, or
  broader project-memory file entered the diff.
- Set the task to READY_FOR_REVIEW for user inspection and a manual commit
  decision.

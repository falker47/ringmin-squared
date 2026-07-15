# CURRENT_STATUS - power-ringmin

Last update: 2026-07-15

- **Current phase:** all-`n` method analysis for lower bounds on the exact
  cyclic-ratio objective.
- **Current task:** classify the two-consecutive-tail refinement for
  \(\Lambda_n\), including cycle-compatible pairing signatures and exact
  insertion corrections.
- **Task dossier:**
  `ops/TASK-20260715__nested_tail_cyclic_ratio_lower_bound/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Implemented Scope

- `research/FIXED_ORDER_CYCLE_RATIO.md` defines the sharp obstruction
  \[
  \beta_{m,n}
  =\min_{\substack{C\text{ simple on }S_{m+1}\\
                    \{a,b\}\in E(C)}}
  \left(P(C)+[m(a+b)-ab]_+\right)
  \]
  and proves that it is the strongest universal bound using only
  \(S_m,S_{m+1}\).
- The proof includes the exact identity
  \(m(a+b)-ab=m^2-(a-m)(b-m)\), fixed-edge residual pairing floors, and the
  requirement that the restored full pairing signature form one connected
  loopless degree-two spanning graph.
- An explicit alternating simple cycle gives the uniform squeeze
  \[
  P_{m+1,n}\le\beta_{m,n}\le P_{m+1,n}+n^2.
  \]
- `tests/test_fixed_order_cycle_ratio.py` adds exact test-local checks only.
  No production source, scorer, API, canonicalizer, or enumerator changed;
  the public complete-order domain remains `n<=8`.

## Exact Method Result

- EXACT THEOREM: with
  \(\beta_n^{(2)}=\max_{1\le m\le n-3}\beta_{m,n}\),
  \[
  \Lambda_n\ge\beta_n^{(2)}
  ={2(\sqrt2-1)\over3}n^3+O(n^2).
  \]
- EXACT METHOD-SPECIFIC LIMITATION: the two-tail refinement may strengthen
  finite terms but cannot improve the leading coefficient
  \(2(\sqrt2-1)/3\). This is not an upper bound or an asymptotic evaluation
  of \(\Lambda_n\), and it does not cover coupling a number of tails growing
  with \(n\).
- EXACT GEOMETRIC COROLLARY:
  \[
  R_2^*(n)>{\beta_n^{(2)}\over\pi}-n^2
  \qquad(n\ge4),
  \]
  with the same leading lower coefficient
  \(2(\sqrt2-1)/(3\pi)\).
- VERIFIED FACT (FINITE EXACT TEST-ONLY EXAMPLE): \(\beta_{4,10}=323\),
  compared with the inner-tail pairing floor \(P_{5,10}=320\).

## Verification

- Final focused new-test selection: `3 passed, 34 deselected`.
- Complete cyclic-ratio module: `37 passed`.
- Induced-subset lower-bound module: `7 passed`.
- Complete local suite: `213 passed`.
- Checked-artifact verifier: all 4 certificates and 76 local brackets
  verified; schema suite: `4 passed`.
- Ruff, test-file compilation, `git diff --check`, temporary-output cleanup,
  and the no-`src/`-diff boundary all pass.
- Independent proof, test, and documentation/scope audits pass after adding
  the explicit \(n\ge4\), \(1\le m\le n-3\) domain to the summary theorem.
- CURRENT HOSTED STATUS: GitHub Actions has not run these uncommitted
  worktree changes.

## Files Changed

- `research/FIXED_ORDER_CYCLE_RATIO.md` adds the authoritative theorem and
  proof.
- `research/ALL_N_LOWER_BOUND.md` adds only the resulting geometric
  consequence and its method-specific limitation.
- `tests/test_fixed_order_cycle_ratio.py` adds independent exact bounded
  checks.
- `start.md`, `PROJECT_KNOWLEDGE.md`, and
  `research/NEXT_RESEARCH_STEPS.md` synchronize stable knowledge and the
  research boundary.
- `CURRENT_STATUS.md` and the STRICT task dossier record durable handoff.

## Residual Limitations

- No exact leading constant, nor convergence of \(\Lambda_n/n^3\) or
  \(R_2^*(n)/n^3\), is proved.
- The theorem concerns one optimized pair of consecutive tails; simultaneous
  coupling of many tails remains open.
- Finite tests verify arithmetic and signature recognition only; they are not
  the all-`n` proof.
- Hosted GitHub Actions remain unverified.

## Proposed Next Task

In a fresh chat, generalize the no-first-order-improvement theorem from two
tails to a fixed symbolic block of \(r\) consecutive nested tails and identify
the first growth scale of \(r=r(n)\) not excluded by the resulting error
bound, without changing production enumeration.

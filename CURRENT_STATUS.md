# CURRENT_STATUS - power-ringmin

Last update: 2026-07-15

- **Current phase:** sublinear-block method analysis for lower bounds on the
  exact cyclic-ratio objective.
- **Current task:** arbitrary block of \(r=r(n)\ge2\) consecutive nested
  tails, including compatible histories, uniform error, and growth scale.
- **Task dossier:**
  ops/TASK-20260715__arbitrary_nested_tail_block/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Implemented Scope

- research/FIXED_ORDER_CYCLE_RATIO.md now defines, for
  \[
  2\le r\le n-2,\qquad
  1\le m\le n-r-1,\qquad
  \ell=m+r-1,
  \]
  the exact obstruction from
  \(S_m,S_{m+1},\ldots,S_\ell\).
- Deleting \(m,m+1,\ldots,\ell-1\), then reinserting them in reverse order,
  gives a bijection between outer cycles and a simple base cycle on
  \(S_\ell\) followed by \(r-1\) compatible descending edge splits.
- If \(A_i\) are the exact split corrections and
  \(H_j=\sum_{i=1}^jA_i\), then
  \[
  \gamma^{(r)}_{m,n}
  =
  \min_{\text{compatible histories}}
  \left[P(C)+\max_{0\le j\le r-1}H_j\right].
  \]
- Every intermediate signature must be one connected loopless degree-two
  spanning cycle with no repeated edge and must satisfy the literal split
  linkage. Recursive child-edge dominoes remain admissible.

## Exact Method Result

- EXACT THEOREM: with
  \[
  E_{m,\ell}=\sum_{t=m}^{\ell-1}[t^2-2]_+,
  \]
  the exact inner-cycle comparison is
  \[
  0\le\gamma^{(r)}_{m,n}-P^*_{\ell,n}
  \le E_{m,\ell}<(r-1)n^2.
  \]
- EXACT THEOREM: the alternating-cycle comparison gives
  \[
  P_{\ell,n}\le\gamma^{(r)}_{m,n}
  \le P_{\ell,n}+g(n-\ell+1)+E_{m,\ell}
  <P_{\ell,n}+rn^2.
  \]
- EXACT METHOD-SPECIFIC LIMITATION: for every integer sequence
  \(r=r(n)=o(n)\),
  \[
  \Gamma_n^{(r(n))}
  ={2(\sqrt2-1)\over3}n^3+O(r(n)n^2)
  ={2(\sqrt2-1)\over3}n^3+o(n^3).
  \]
  Thus every fixed or sublinear block preserves the one-tail coefficient.
- EXACT METHOD-SPECIFIC BOUNDARY: linear \(r=\Theta(n)\) is the first scale
  not excluded by the error estimate. An admissible nested domino attains the
  history-level envelope, but this does not prove that the minimized
  obstruction improves or changes coefficient.

## Bounded Exact Oracle

- VERIFIED FACT (FINITE EXACT TEST-ONLY COMPUTATION): the recursive oracle
  audits every correction, prefix, edge-set linkage, intermediate cycle, and
  final signature without production scoring or enumeration.
- At \((m,n,r)=(2,7,4)\), 60 compatible histories equal all 60 direct outer
  dihedral cycles signature by signature, with
  \[
  (P_{5,7},P^*_{5,7},\gamma^{(4)}_{2,7})=(106,107,118).
  \]
- At \((2,8,4)\), three base classes expand to all 360 outer classes and give
  \((164,165,172)\). A separate fully nested history attains
  \(E_{2,5}=23\).
- No production source, API, scorer, canonicalizer, public enumerator,
  enumeration ceiling, schema, artifact, example, verifier, backend, or
  certificate contract changed. The production complete-order domain remains
  \(3\le n\le8\), with ceiling 2,520.

## Verification

- New focused selection: 7 passed.
- Complete cyclic-ratio module: 47 passed.
- Complete local suite: 223 collected tests passed.
- Checked-artifact verifier: all 4 certificates and 76 local brackets
  verified; schema suite: 4 passed.
- Focused Ruff on the modified Python test passes.
- Repository-wide Ruff reports four existing findings in untouched files:
  two in src/power_ringmin/critical_structure.py, one in
  src/power_ringmin/fixed_order_artifact.py, and one in
  tests/test_finite_results.py. They are recorded but not mixed into this
  task.
- Independent proof, oracle, and synchronization audits pass after extending
  the \(P^*_{\ell,n}\) definition to \(1\le\ell\le n-2\) and making the
  complete-order extension explicit.
- Git diff hygiene and the no-production-diff audit pass.
- CURRENT HOSTED STATUS: GitHub Actions has not run these worktree changes.

## Files Changed

- research/FIXED_ORDER_CYCLE_RATIO.md adds the authoritative general theorem,
  uniform bound, sublinear result, domino audit, and limitations.
- tests/test_fixed_order_cycle_ratio.py adds the independent recursive exact
  oracle and bounded \(r=4\) checks.
- start.md, PROJECT_KNOWLEDGE.md, and
  research/NEXT_RESEARCH_STEPS.md synchronize stable knowledge and the
  research boundary.
- CURRENT_STATUS.md and the STRICT task dossier record durable handoff.

## Residual Limitations

- The ordinary split theorem requires an inner tail of at least three labels;
  the two-label double-edge case is outside the stated domain.
- The result concerns a maximum of separately optimized one-block
  obstructions. It does not exchange \(\max_m\) and \(\min_\sigma\).
- Linear-size block optimization remains open.
- No exact leading constant, convergence theorem, or matching geometric bound
  for \(\Lambda_n/n^3\) or \(R_2^*(n)/n^3\) is claimed.
- Finite tests verify arithmetic, compatibility, and bounded coverage only;
  they are not the all-\(n\) proof.
- Hosted GitHub Actions remain unverified.

## Proposed Next Task

In a fresh chat, formulate one linear-density block, for example
\(r_n=\lfloor(\sqrt2-1)n\rfloor\), and determine whether a compatible-history
strategy has \(o(n^3)\) excess or a genuinely cubic residual obstruction,
without changing production enumeration.

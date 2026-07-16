# EVIDENCE - Two-Prefix Linear Block

## EV-01 - Baseline And Isolation

- Classification: verified fact.
- Check: clean startup state and focused pre-change regression.
- Evidence: `git status --short --branch` showed only the clean `main`
  tracking line; `python -m pytest tests\test_fixed_order_cycle_ratio.py -q`
  passed all 69 tests.
- Interpretation: the STRICT task starts from an isolated verified state.

## EV-02 - Single-Use Charging And Recursive Coverage

- Classification: exact method-specific theorem.
- Check: partition selected splits into original-base and recursive current
  edges only after expanding the prescribed two-prefix linear form.
- Result: original base-edge slack has multiplicity at most one
  across both segments; recursive child-edge histories remain in the local
  endpoint range used by CR28ba.
- Invalid route excluded: summing two independently slack-charged CR28be
  inequalities would double count the same base slack.
- Independent audits and literal history diagnostics found no obstruction.

## EV-03 - Exact Coefficient And Witness

- Classification: exact method-specific theorem.
- Result:
  \[
  C_2=p(\alpha)
  +(\alpha-\beta_1)g(\alpha,\beta_1,\lambda_{\rm hi})
  +(\beta_1-\beta_2)g(\alpha,\beta_2,\lambda_{\rm lo}).
  \]
- Witness values:
  \[
  p={284\over1029},\quad
  g_{\rm hi}={52\over3675},\quad
  g_{\rm lo}={199\over87808},\quad
  C_2={72825421\over263424000}.
  \]
- Exact comparison: with
  \(x=(27C_2-4)/2=304196789/175616000\),
  \[
  x^2-3={12748069910521\over30840979456000000}>0.
  \]
  Hence \(C_2>(4+2\sqrt3)/27\) without floating point.

## EV-04 - Finite And Global Theorem

- Classification: exact finite and global lower-bound theorem.
- The two selected segments are uniformly nonempty from the minimal threshold
  \(n=59\); \(n=58\) fails with \((r,s_1,s_2)=(24,24,22)\).
- Exact result for every \(n\ge59\):
  \[
  \Lambda_n
  \ge C_2n^3+{106196857\over263424000}n^2
       -{1520\over1029}n-{22\over343}
  \ge C_2n^3,
  \]
  \[
  R_2^*(n)>{C_2\over\pi}n^3-n^2.
  \]
- Limitation: \(C_2\) is one witness, not a five-parameter optimum or exact
  leading coefficient.

## EV-05 - Independent Split Diagnostics

- Classification: verified bounded exact test-local computation.
- All 1,260 depth-two histories at \(n=59\) pass literal linkage, one-use
  charging, both local floors, and the prescribed weighted maximum; 70 have a
  recursive second split.
- A fully nested \(n=100\) history crosses the high/low boundary and splits
  child edges with two inserted endpoints. Deterministic base and recursive
  policies pass at \(n=59,100,200,1000\).
- The invalid two-copy route is tested separately and overdraws one edge by
  exactly its slack. Exact rational finite scans pass through \(n=1000\).
- Limitation: bounded diagnostics corroborate the all-\(n\) written proof but
  do not replace it.

## EV-06 - Complete Verification And Scope

- Classification: verified computation and source inspection.
- Results: two-prefix selection 20 passed; fixed-cycle module 89 passed; full
  suite 265 passed; checked-artifact verifier passed 4 certificates and 76
  local brackets; schema selection 4 passed; changed-test Ruff passed.
- Repository-wide Ruff reports the same four known findings in untouched
  files. Final `git diff --check` and protected-scope inspection pass.
- No production, artifact, schema, example, verifier, backend, certificate,
  enumerator, or enumeration-limit path changed.
- Hosted GitHub Actions remain unverified; the user retains all staging and
  commit authority.

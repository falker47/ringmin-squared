# CURRENT_STATUS - power-ringmin

Last update: 2026-07-20

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** evaluate exactly the induced-subset objective \(K\) for
  the unchanged even-\(v\), residue-two core \(\sigma_{\alpha^{(2)}_*}\)
  fixed by (PGE2-1)--(PGE2-6), on \(n=10m+2\), \(m\ge1\).
- **Repository state at startup:** clean main worktree at commit
  8052c99d0c9c6c058cf8246a261619d6bcc00d09.
- **Implementation state:** the exact fixed-core theorem, comparisons, sole
  bounded diagnostic, source synchronization, and final diff hygiene are
  complete.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

Evaluate only the order already fixed by (PGE2-1)--(PGE2-6). Reconstruct its
literal cyclic word, classify every maximizing subset, derive the exact score
with all residual branches, and prove the deletion-gain and compressed-arc
conditions including the doubleton, singleton block, cyclic closure, empty
ranges, and \(m=1,2\). Compare the result exactly with the already known
residue-two order and K825 on \(n=10m+2\).

The task excludes changes to the fixed core, searches over subsets,
matchings, permutations, path assignments, or alternative orders, production
changes, and all angular, geometric, global-minimizer, or global-optimality
conclusions.

## Literal Fixed Order

With

\[
D=8m+3,\qquad L=4m+1,\qquad E_j=D+j,
\]

\[
\lambda_j=4m-2j,\qquad \rho_j=4m+1-2j,
\]

and the path words \(P_k\) and map \(\alpha^{(2)}_*\) of
(PGE2-1)--(PGE2-6), the literal cyclic order is

\[
\tau_m^{(2,*)}
=\mathop{\bigcirc}_{j=0}^{2m-1}
\left(E_j,\lambda_j,P_{\alpha^{(2)}_*(j)},
\rho_{j+1\bmod 2m}\right).
\]

It starts at \(E_0\); the final retained label is \(\rho_0=L\), which closes
to \(E_0\). After deleting \(H_m=\{2,\ldots,4m\}\), its compressed backbone
is exactly (KPGE2-5), including the closing segment
\((E_{2m-1},A_q,c_q,B_q,L,E_0)\).

## Exact Fixed-Core Theorem

For every \(m\ge1\), the unique maximizing subset is

\[
B_m=\{4m+1,\ldots,10m+2\}.
\]

Its exact score is

\[
\boxed{
K(\sigma_{\alpha^{(2)}_*})
=\frac{
1714m^3+1353m^2+24mq+281m+12q^2+36q+30
}{6}},
\]

where

\[
q=\left\lceil\frac{(m-1)(4m+1)}{5m+1}\right\rceil.
\]

For \(m\ge2\), write \(r=m\bmod5\) and
\(q=(4m+c_r)/5\), with
\((c_0,c_1,c_2,c_3,c_4)=(0,1,-3,-2,-1)\). Then

\[
150K
=42850m^3+34497m^2+(7745+216c_r)m
+12c_r^2+180c_r+750.
\]

The only residual of this five-branch expansion is \(m=1\):
\(q=0\) and \(K=563\). The boxed all-row formula remains exact there.

The nine deletion-gain classes cover all \(4m-1\) deleted labels and are
strictly positive. Their unique minimum is \(5\) at \(m=1\), and
\(20m+6\) for every \(m\ge2\). Every proper compressed shortcut is strictly
positive. Its unique minimum is \(1,21,57\) for \(m=1,2,3\), respectively,
and \(20m+4\) for \(m\ge4\). These strict inequalities prove uniqueness,
including endpoint holes, every two-edge middle role, three-edge and longer
arcs, and the genuine cyclic cut.

The boundary rows are

\[
\tau_1^{(2,*)}
=(11,4,7,8,3,12,2,10,6,9,5),\qquad K=563,
\]

\[
\tau_2^{(2,*)}
=(19,8,18,10,17,7,20,6,12,13,5,21,4,14,3,22,2,16,11,15,9),
\qquad K=3302.
\]

## Exact Same-Subsequence Comparisons

For the known residue-two order,

\[
K_{\mathrm{R2}}(2m)
=\frac{572m^3+459m^2+99m+4}{2},
\]

and

\[
K_{\mathrm{R2}}(2m)-K(\sigma_{\alpha^{(2)}_*})
=\frac{
m^3+12m^2-12mq+8m-6q^2-18q-9
}{3}>0.
\]

For K825, the first three values on this subsequence are
\(593,3431,10299\), while for \(m\ge4\)

\[
K_{825}(m)
=\frac{572m^3+501m^2+149m+6}{2},
\]

\[
K_{825}(m)-K(\sigma_{\alpha^{(2)}_*})
=\frac{
m^3+75m^2-12mq+83m-6q^2-18q-6
}{3}>0.
\]

Thus the fixed PGE2 core is strictly lower than both named combinatorial
orders on every row of the same subsequence. This is only a comparison of
three fixed orders. The fixed-core cubic coefficient is \(857/3000\) in \(n\);
both comparators have coefficient \(858/3000=143/500\).

## Verification

- The sole dossier-local standard-library diagnostic constructs only
  (PGE2-6), uses a max-plus recurrence without subset enumeration, and audits
  every proper oriented arc without enumerating matchings, permutations, path
  assignments, or alternative orders.
- It passes through \(m=1000\) for formulas, residuals, boundary rows, and
  exact comparisons, and through \(m=30\) for literal max-plus and all-arcs
  checks: 5,006,000 literal entries, 36,511,800 transitions, 1,830 deletion
  gains, 950,150 proper arcs, and 943,640 compressed shortcuts.
- Scoped Ruff lint and format checks pass. The first format check found one
  mechanical delta; Ruff formatted the diagnostic, whose post-format rerun
  passes.
- Full pytest passes: 283 passed.
- The focused checked-artifact schema suite passes: 4 passed.
- The standalone checked-artifact verifier passes for four certificates,
  76 local brackets, and \(n=3,4,5,6\).
- The proof-source structural audit, three focused independent audits, and a
  separate final synchronization audit pass; all actionable notation,
  editorial, and synchronization findings were corrected.
- One final source-audit wrapper invocation failed on a PowerShell
  interpolation typo before inspecting the source; the corrected audit
  passes with 45 sequential unique tags, 52 balanced displays, balanced math
  environments, and no control characters.
- Final Git status, complete tracked and untracked inspection, and
  diff-whitespace hygiene pass. Only the intended six authoritative files
  and this one task dossier are in scope.

## Evidence Classification And Limitations

- (KPGE2-1)--(KPGE2-45) are an **exact all-domain fixed-order combinatorial
  theorem**.
- The standalone diagnostic is **bounded exact computation** corroborating,
  not replacing, that proof.
- The comparisons with the known residue-two order and K825 are **exact
  same-subsequence fixed-order comparisons**.
- No production, angular, geometric, global-minimizer, global-optimality, or
  upstream Ringmin conclusion is asserted or inferred.

## Files In Scope

- research/FIXED_ORDER_CYCLE_RATIO.md
- research/PRODUCT_DISTANCE_SURROGATE.md
- research/NEXT_RESEARCH_STEPS.md
- start.md
- PROJECT_KNOWLEDGE.md
- CURRENT_STATUS.md
- ops/TASK-20260720__residue_two_pg49_star_k/

## Proposed Next Task

In a fresh STRICT task, analyze the filtered cubic-convergent obstruction
(KPGZERO-23)--(KPGZERO-24), without beginning any search or inferring a
geometric or global optimum.

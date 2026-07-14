# CURRENT_STATUS - power-ringmin

Last update: 2026-07-14

- **Current phase:** exact residue-class consequences of the matching
  product-distance construction.
- **Current task:** derive the closed formula for \(H_n\), including the
  separate value at \(n=12\), and combine it with the existing uniform upper
  construction.
- **Task dossier:**
  ops/TASK-20260714__residue_class_matching_consequences/.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Exact Residue-Class Formula

For \(n\ge9\), put

\[
d_n=\left\lceil{4n+8\over5}\right\rceil,
\qquad
T_n={d_n(d_n-1)\over2}.
\]

EXACT THEOREM:

\[
H_n=
\begin{cases}
d_n(d_n-1)/2,&n\equiv0,3,4\pmod5,\\
(d_n-1)^2/2,&n\equiv1\pmod5,\\
(d_n-1)(d_n-2)/2,&n\equiv2\pmod5,\ n\ge17,\\
56,&n=12.
\end{cases}
\]

The exceptional value is caused by the unchanged tail-packing condition:
at \(n=12\), both \(55\) and \(111/2\) have \(a=7,u=6\), so
\(\Psi_{12}=12>11\); at \(56\), one has \(a=8,u=5,b=11,v=2,C=4\) and
\(\Psi_{12}=10\).

## Exact Matching Consequences

The established chain

\[
H_n\le B_n\le W_n\le W(\sigma_n)\le T_n
\]

has equal endpoints in residues zero, three, and four. Therefore

\[
\boxed{
B_n=W_n=T_n={d_n(d_n-1)\over2}
}
\qquad(n\ge9,\ n\equiv0,3,4\pmod5).
\]

In the two unresolved classes, the exact widths to the uniform theorem
threshold are

\[
T_n-H_n=
\begin{cases}
(d_n-1)/2=(2n+3)/5,&n\equiv1\pmod5,\\
d_n-1=(4n+7)/5,&n\equiv2\pmod5,\ n\ge17,\\
10,&n=12.
\end{cases}
\]

These are bound widths, not optimality gaps and not necessarily gaps to the
scores of individual exceptional witnesses. No replacement construction is
proposed, and no all-\(n\) formula or new exact value beyond the bounded
\(n\le11\) table is claimed in residues one and two.

## Exact Support And Verification

- CURRENT LOCAL VERIFIED FACT: the event-set inversion for \(H_n\) remains
  unchanged, and a separate constant-time exact residue formula is exported
  from power_ringmin.product_distance.
- CURRENT LOCAL VERIFIED FACT: source and tests compile; Ruff passes.
- CURRENT LOCAL VERIFIED FACT: focused product-distance tests pass 28/28.
- CURRENT LOCAL VERIFIED FACT: integrated product-distance, zigzag,
  induced-subset, and insertion tests pass 43/43.
- CURRENT LOCAL VERIFIED FACT: the full suite passes 156/156 outside the
  filesystem sandbox.
- RETAINED FAILED CHECK: the sandboxed full suite produced 31 temporary-path
  setup errors and one Git-provenance mismatch because the sandbox denied the
  required system-temp and Git metadata access. The identical suite passed
  outside the sandbox; no changed product-distance test failed.
- CURRENT LOCAL VERIFIED FACT: checked-artifact semantic verification accepts
  4 certificates, 76 local brackets, and the n=3..6 summary.
- CURRENT LOCAL VERIFIED FACT: the closed form matches both an independent
  five-polynomial oracle and the unchanged exact event inversion for every
  9<=n<=200; exact formula/gap checks cover every 9<=n<=5000.
- CURRENT LOCAL VERIFIED FACT: independent mathematical and implementation
  audits pass without a finding; the documentation audit's stale-memory
  findings were applied.
- CURRENT LOCAL VERIFIED FACT: all 9 changed paths pass strict UTF-8 and
  trailing-whitespace checks; the proof note has 94 unique equation tags and
  195 balanced display pairs; path scope, complete-diff inspection, and
  git diff --check pass.
- CURRENT HOSTED STATUS: GitHub Actions for the current worktree has not been
  independently verified.

## Residual Limitations

- Exact values of \(B_n\) and \(W_n\) beyond the bounded table remain open in
  residue classes one and two.
- Structural classifications of optimal orders remain open in every class.
- The widths above are relative to the uniform threshold \(T_n\), not to a
  proved best upper construction in each exceptional finite case.
- Finite canonical core-order enumeration remains bounded to n=3..11.
- The geometric lower and upper coefficients remain different.

## Proposed Next Task

Document the fixed-order angular/STN equivalence and endpoint semantics, as
already prioritized in the research roadmap. Do not begin that task in this
chat.

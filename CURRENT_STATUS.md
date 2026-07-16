# CURRENT_STATUS - power-ringmin

Last update: 2026-07-16

- **Current phase:** exact finite three-prefix theorem completed.
- **Current task:** round the exact irrational \(C_{3,*}\) optimizer and prove
  one reproducible finite lower theorem.
- **Task dossier:** `ops/TASK-20260716__three_prefix_finite_theorem/`.
- **Task status:** READY_FOR_REVIEW.
- **Current blocker:** none.
- **Current next atomic action:** user review and manual commit decision.
- **Awaiting user review:** yes.

## Exact Finite Three-Prefix Theorem

Put
\[
d=377823,
\qquad
a=\alpha_*={685623-421\sqrt d\over993423},
\qquad
A=3a-1,
\]
\[
(x_1,x_2,x_3)
=\left({1058\over1263},{276\over421},{184\over421}\right),
\qquad
b_i={1+a+x_iA\over4}.
\]
For integer \(n\), define
\[
r_n=\lfloor an\rfloor,
\qquad
s_{i,n}=\lceil b_i n\rceil,
\qquad
S_n=n+r_n.
\]
From the minimal uniform threshold \(n=159\), all block, order,
non-vacuity, and finite middle-clipped conditions hold. The finite weights
\[
\widehat\lambda_{i,n}=4-{S_n\over s_{i,n}}
\]
are strictly ordered and give
\[
\widehat F_{i,n}={(4s_{i,n}-S_n)^2\over2}.
\]
The literal lower expression is
\[
\begin{aligned}
\mathcal B_{3,n}={}&P_{r_n,n}
 +(r_n-s_{1,n})\widehat F_{1,n}\\
&+(s_{1,n}-s_{2,n})\widehat F_{2,n}
 +(s_{2,n}-s_{3,n})\widehat F_{3,n}.
\end{aligned}
\]
Define the integer closure
\[
\mathcal I_{3,n}=\lceil\mathcal B_{3,n}\rceil.
\]
The established one-use charging theorem gives
\[
\boxed{
\Lambda_n\ge\mathcal I_{3,n}\ge\mathcal B_{3,n}
\qquad(n\ge159).
}
\]

## Threshold And Boundary Region

- At \(n=158\),
  \((r_n,s_{1,n},s_{2,n},s_{3,n})=(67,67,64,62)\), so the first segment is
  empty.
- Exact floor/ceil arithmetic checks every case \(159\le n\le170\).
- The symbolic non-vacuity tail starts at \(n=171\).
- Therefore \(159\) is the minimal uniform threshold for three nonempty
  selected segments.
- The symbolic middle-clipping estimate is uniform by \(n=23\); it is not the active
  threshold.

## Controlled Polynomial Remainder

The literal bound satisfies
\[
\mathcal B_{3,n}
>C_{3,*}n^3+\kappa_*n^2-\ell_*n-{1\over15},
\]
where
\[
C_{3,*}
={753972193324+106042322\sqrt{377823}\over2960667770787},
\]
\[
\kappa_*
={-535396585939+1466777893\sqrt{377823}\over986889256929}
>{1\over3},
\qquad
\ell_*={a+5\over3}<{11\over6}.
\]
Hence the remainder is larger than
\((10n^2-55n-2)/30>0\) for every \(n\ge6\). In particular, the finite
theorem does imply the bare optimized cubic bound on its entire domain:
\[
\boxed{
\Lambda_n\ge\mathcal I_{3,n}\ge\mathcal B_{3,n}>C_{3,*}n^3,
\qquad
R_2^*(n)>{\mathcal I_{3,n}\over\pi}-n^2
\ge{\mathcal B_{3,n}\over\pi}-n^2
>{C_{3,*}\over\pi}n^3-n^2
\quad(n\ge159).
}
\]
The integer \(\mathcal I_{3,n}\) inequality is the strongest explicit
cutoff-only consequence of this rounded bound; \(\mathcal B_{3,n}\) is the
literal charging expression.

## Evidence Classification

- EXACT FINITE METHOD-SPECIFIC THEOREM: cutoff admissibility, minimal uniform
  threshold, finite clipped weights, literal charging expression, integer
  closure, controlled polynomial remainder, and strict \(C_{3,*}n^3\)
  consequence.
- VERIFIED BOUNDED EXACT COMPUTATION: the standalone dossier diagnostic
  implements \(\mathbb Q(\sqrt{377823})\) independently, scans through the
  finite bridge, and checks all finite formulas through \(n=1000\).
- LIMITATION: the theorem does not give an exact value of \(\Lambda_n\) or
  \(R_2^*(n)\), an exact residual, convergence, a matching upper bound, or an
  exact geometric leading coefficient.
- SCOPE: no four-prefix charging, production code, test, artifact, schema,
  backend, certificate, enumerator, or enumeration-limit change.

## Verification

- Independent exact diagnostic: passed through \(n=1000\).
- Focused three-/two-/one-prefix selection: 12 passed.
- Complete fixed-order-cycle-ratio module: 101 passed.
- Complete local suite: 277 passed.
- Checked-artifact semantic verification: 4 certificates and 76 local
  brackets passed.
- Schema selection: 4 passed.
- Ruff check and format check on the standalone diagnostic: passed.
- Equation-tag audit: 289 tags, all unique.
- Changed-source delimiter deltas and LaTeX environments: balanced.
- Three independent read-only audits found no remaining mathematical,
  diagnostic, synchronization, Markdown, or scope defect after the
  integer-closure and wording corrections were applied.
- Protected-path inspection, final changed-path inspection,
  `git diff --check`, and final diff review passed.

## Files Changed

- `research/FIXED_ORDER_CYCLE_RATIO.md`: primary exact proof and finite
  theorem; also corrects CR42 from the obsolete \(C_{2,*}\) lower endpoint to
  the already-proved \(C_{3,*}\) endpoint.
- `research/ALL_N_LOWER_BOUND.md` and `research/NEXT_RESEARCH_STEPS.md`:
  synchronized all-\(n\) note and roadmap.
- `start.md`, `PROJECT_KNOWLEDGE.md`, and this file: synchronized authoritative
  project memory.
- `ops/TASK-20260716__three_prefix_finite_theorem/`: STRICT task status, log,
  evidence, and independent exact diagnostic.

## Protected Limitations

- No charging theorem beyond three selected prefixes is inferred from the
  normalized simplex.
- Finite rounding of the irrational two-prefix optimizer remains unresolved.
- Neither normalized sequence is proved to converge.
- No upper bound matching \(C_{3,*}/\pi\) is known.
- Production, artifacts, schemas, interval backends, certificates, tests,
  enumerators, and enumeration limits remain unchanged.

## Proposed Next Task

In a fresh STRICT task, analyze one explicit parametric perturbation of the
current \(8/25\) product-distance upper construction and prove either a strict
symbolic improvement or a precise obstruction, without extending cyclic-order
enumeration.

# CURRENT_STATUS - power-ringmin

Last update: 2026-07-18

## State

- **Mode:** STRICT
- **Status:** READY_FOR_REVIEW
- **Active task:** derive the exact symbolic count of relation-compatible,
  equivalently full-optimal, path-to-gap scaffold bijections on
  \(n=10m+3\), \(m\ge3\), from the PG49 Ferrers support without enumerating
  path permutations.
- **Repository state at startup:** clean `main` worktree at commit
  `b1a4054d1fac75443cf1929921dddb38f9750a5f`, tracking `origin/main`.
- **Implementation state:** the permanent recurrence, exact column and row
  products, complete boundary treatment, PG50--PG63 class identity,
  labelled/dihedral convention, sole bounded independent diagnostic,
  authoritative synchronization, independent audits, and repository
  verification are complete.
- **Current blocker:** none.
- **Current next atomic action:** user manual review and commit decision.
- **Awaiting user review:** yes.

## Objective And Scope

For the fixed indexed paths \(P_0,\ldots,P_{2m-1}\) and oriented terminal
gaps \(G_0,\ldots,G_{2m-1}\), count exactly every relation-compatible
bijection using the nested PG49 support. Prove that the counted set is exactly
the full-optimal scaffold class from PG50--PG63, cover every endpoint and
path-type boundary, and specify the symmetry convention. Use no permutation
enumeration. Add only one small standard-library diagnostic and make no
geometric inference or alternative-scaffold study.

## Exact Ferrers Formula And Recurrence

Put

\[
v=2m,
\qquad
d=8m+4,
\qquad
\kappa_j=
\left\lceil{j(d-1)\over2(d+j)}\right\rceil.
\]

PG49 forces \((P_0,G_0)\). On the reduced board
\(1\le j,k<v\), gap \(G_j\) has the nested suffix neighborhood
\[
N(G_j)=\{P_{\kappa_j},\ldots,P_{v-1}\}.
\]
After assigning the narrower gaps \(G_{v-1},\ldots,G_{j+1}\), exactly
\(v-1-j\) used paths lie in \(N(G_j)\). Therefore every partial assignment
has precisely
\[
(v-\kappa_j)-(v-1-j)=j+1-\kappa_j
\]
extensions at \(G_j\). Thus
\[
C_{m,v}=1,
\qquad
C_{m,j}=(j+1-\kappa_j)C_{m,j+1},
\qquad
\mathsf F_m^{\rm lab}=C_{m,1},
\]
and the exact labelled count is
\[
\boxed{
\mathsf F_m^{\rm lab}
=\prod_{j=1}^{2m-1}
\left(
j+1-
\left\lceil{j(8m+3)\over2(8m+4+j)}\right\rceil
\right)
}
\qquad(m\ge3).
\]

The equivalent row formula is
\[
\boxed{
\mathsf F_m^{\rm lab}
=(m-1)!\prod_{k=1}^{m}(\ell_k-k+1)
=(2m-q_m)!\prod_{k=1}^{q_m-1}(\ell_k-k+1),
}
\]
where
\[
\ell_k=
\min\!\left\{2m-1,
\left\lfloor{2k(8m+4)\over8m+3-2k}\right\rfloor\right\},
\qquad
q_m=\left\lfloor{4m+3\over5}\right\rfloor.
\]

## Exact Class Identity

Let \(\mathfrak F_m\) be the perfect matchings of the PG49 support. Since
\(\mathcal R_{\rm ext}\subseteq\mathcal R_{\rm loc}\), PG36 makes every such
matching relation-compatible. Conversely, every relation-compatible
bijection witnesses the extendibility of each of its own edges. PG62 then
gives the exact set identity
\[
\boxed{
\mathfrak F_m
=\{\alpha:\alpha\text{ is relation-compatible}\}
=\{\alpha:W(\sigma_\alpha)=T=W_n\}.
}
\]
Hence the product counts all and only the full-optimal scaffold bijections
classified by PG50--PG63, not support edges or partial assignments.

## Boundaries And Symmetry Convention

- PG49 forces \(\alpha(0)=0\); \(\kappa_1=1\) gives the first positive
  factor one.
- For \(2\le j<2m\), \(\kappa_j\le j-1\), so every remaining factor is at
  least two.
- The last nonclosing and closing thresholds are
  \(\lfloor(4m+1)/5\rfloor\) and \(\lfloor(4m+3)/5\rfloor\), covering every
  residue class of \(m\).
- Rows from \(P_{q_m}\) onward are universal on positive gaps. In particular,
  the last triple, first singleton, and terminal singleton contribute
  \(m\), \(m-1\), and \(1\), respectively.
- Floor/ceiling cutoff equalities are included.
- At \(m=3\),
  \((\kappa_0,\ldots,\kappa_5)=(0,1,1,2,2,3)\) and
  \(\mathsf F_3^{\rm lab}=36\); there is no exceptional minimum branch.
- The formula is primarily a **labelled** count of indexed gaps and retained
  oriented paths. No rotation, reflection, or Ferrers-board automorphism is
  quotiented out. Distinct assignments nevertheless yield distinct canonical
  dihedral core-order representatives: the unique label \(n\) fixes rotation,
  its oriented neighbors are \(2<3\), and the gap words recover \(\alpha\).
  Thus the same integer also counts the dihedral classes represented by this
  fixed scaffold, by injectivity rather than division by a symmetry factor.

## Verification

- The sole standard-library diagnostic independently builds the PG49 matrix
  by cross-multiplied integer inequalities and applies Ryser
  inclusion--exclusion to its reduced permanent. For \(m=3,\ldots,8\), it
  agrees with both Ferrers products at
  \[
  36,\ 720,\ 21600,\ 725760,\ 46448640,\ 3292047360.
  \]
  It enumerates 43,674 nonempty column subsets in total, not path
  permutations or matchings.
- The diagnostic passes after an orientation-consistency correction; in-memory
  compilation and Ruff lint/format pass. One initial Ruff format-check failure
  was retained and resolved by mechanical formatting.
- The focused product-distance suite passes 49 tests; the complete repository
  suite passes 283 tests; the schema suite passes four tests; checked-artifact
  verification accepts four certificates and 76 local brackets.
- Three independent read-only audits pass the mathematics, diagnostic, and
  cross-file synchronization. The synchronization audit found one row/column
  wording mismatch; PG65 and the diagnostic were transposed consistently,
  after which proof and code re-audits passed.
- Final encoding, equation-tag, whitespace, complete-diff, and Git checks pass
  on the intended nine-file scope.

## Evidence Classification And Limitations

- The permanent recurrence, both product formulas, boundary treatment,
  full-optimal class identity, and labelled/dihedral injectivity statement are
  **exact theorems**.
- The diagnostic is a **bounded exact computation** that corroborates but
  does not prove the all-\(m\) theorem.
- The result is confined to the fixed retained scaffold and its path
  orientations. It proves no geometric feasibility, exact value of
  \(R_2^*(n)\), classification of alternative scaffolds, or asymptotic formula
  for the new count. Production, tests, artifacts, schemas, backends,
  certificates, and enumeration limits are unchanged.

## Files In Scope

- `research/PRODUCT_DISTANCE_SURROGATE.md`
- `research/NEXT_RESEARCH_STEPS.md`
- `start.md`
- `PROJECT_KNOWLEDGE.md`
- `CURRENT_STATUS.md`
- `ops/TASK-20260718__ferrers_bijection_count/`

## Proposed Next Task

After manual review and in a fresh STRICT chat, derive the leading asymptotics
of \(\log \mathsf F_m^{\rm lab}\) from the exact Ferrers product, with a
rigorous error term and without permutation enumeration, alternative
scaffolds, or geometric claims.

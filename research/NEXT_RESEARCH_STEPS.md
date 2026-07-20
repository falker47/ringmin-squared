# Next Research Steps

Last reviewed: 2026-07-20

This file is the roadmap and priority source only. Stable result summaries
belong in [PROJECT_KNOWLEDGE.md](../PROJECT_KNOWLEDGE.md), detailed proofs in
the other research notes, and task evidence in ops/.

## Completed Milestone

- **COMPLETED -- PGE5 support:** on the canonical even-\(v\), \(e=5\)
  scaffold \(n=10m+4\), \(m\ge2\), the exact local relation, extendible
  support, Ferrers reduction, and equivalence between local compatibility and
  \(W=W_n\) are closed by PGE5-1--PGE5-26. The result evaluates \(W\), not
  \(K\) or the geometry. See the
  [authoritative proof](PRODUCT_DISTANCE_SURROGATE.md#the-canonical-even-v-e5-path-to-gap-support)
  and the [stable synopsis](../PROJECT_KNOWLEDGE.md#product-distance-surrogate).

The superficially similar Ferrers count and monotone threshold-closing
\(K\)-theorem already in the repository concern the earlier
\(n=10m+3\), \(e=4\) scaffold. They do not close the \(e=5\) question below.

## Sole Next Atomic Task

Run one fresh STRICT task to evaluate exactly \(K\) for the canonical PGE5
interval-shift bijection

\[
\alpha_{q,2m-1},\qquad
q=\left\lfloor{4m+3\over5}\right\rfloor,\qquad
n=10m+4,\quad m\ge2.
\]

Acceptance criteria:

- construct only this fixed \(e=5\) core order from the PGE5 scaffold;
- determine the exact maximizing induced subset or subsets and the exact
  value of \(K\), including the minimum row and every residue branch;
- audit every deletion/shortcut and the genuine cyclic closing role with an
  independent bounded diagnostic that does not replace the proof;
- distinguish the result throughout from the already closed
  \(n=10m+3\), \(e=4\) theorem for the identically named shift; and
- infer no angular, geometric, global-\(K\)-minimizer, or global-optimality
  conclusion without a separate proof.

This task is recorded here but is not executed by the present consolidation.
No Ferrers-permanent count is a competing priority.

## Deferred, Not Prioritized

All other open directions remain deferred until the sole task above is
reviewed. They include the filtered cubic-convergent obstruction, finer
Ferrers-count residuals, the asymptotic coefficient gap, tighter finite
brackets at \(n=5,6\), the radius-one threshold below \(12\), and later
minimizer-set restrictions for \(n\ge94\). Their mathematical context remains
in the relevant proof notes and stable knowledge; this roadmap does not repeat
it.

Large exhaustive certificates, production enumeration-limit increases, and
claims of an exact geometric asymptotic constant remain deliberately
deferred.

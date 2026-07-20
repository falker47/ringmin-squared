# Next Research Steps

Last reviewed: 2026-07-20

This file is the roadmap and priority source only. Stable result summaries
belong in [PROJECT_KNOWLEDGE.md](../PROJECT_KNOWLEDGE.md), detailed proofs in
the other research notes, and task evidence in ops/.

## Completed Milestones

- **COMPLETED -- PGE5 support:** on the canonical even-\(v\), \(e=5\)
  scaffold \(n=10m+4\), \(m\ge2\), the exact local relation, extendible
  support, Ferrers reduction, and equivalence between local compatibility and
  \(W=W_n\) are closed by PGE5-1--PGE5-26. The result evaluates \(W\), not
  \(K\) or the geometry. See the
  [authoritative proof](PRODUCT_DISTANCE_SURROGATE.md#the-canonical-even-v-e5-path-to-gap-support)
  and the [stable synopsis](../PROJECT_KNOWLEDGE.md#product-distance-surrogate).

The superficially similar Ferrers count and monotone threshold-closing
\(K\)-theorem already in the repository concern the earlier
\(n=10m+3\), \(e=4\) scaffold; they were not used as the PGE5 theorem.

- **COMPLETED -- fixed PGE5 interval-shift \(K\):** on the distinct
  \(n=10m+4\), \(m\ge2\) scaffold, (KPGE5-1)--(KPGE5-30) evaluate only
  \(\alpha_{q,2m-1}\), \(q=\lfloor(4m+3)/5\rfloor\). The sole maximizing
  subset is \(\{4m+1,\ldots,10m+4\}\), all five residue branches and the
  literal \(m=2\) row are exact, and the score is strictly below canonical
  K825 on every same-subsequence row while retaining cubic coefficient
  \(143/500\). The theorem makes no statement about another supported
  bijection, the permanent, geometry, or global optimality. See the
  [authoritative proof](FIXED_ORDER_CYCLE_RATIO.md#20-exact-k-for-the-fixed-pge5-interval-shift)
  and the [stable synopsis](../PROJECT_KNOWLEDGE.md#product-distance-surrogate).

## Sole Next Atomic Task

After manual review, run one fresh STRICT post-review audit of the new
KPGE5 theorem and its diagnostic at the reviewed commit.

Acceptance criteria:

- audit KPGE5-1--KPGE5-30 line by line against the literal PGE5 scaffold;
- independently rederive the block sum, five residue branches, minimum row,
  and exact K825 subtraction without importing the task formula as an
  oracle criterion;
- rerun the standalone bounded oracle and repository verification at the
  reviewed commit, recording exact provenance and any contradictory result;
- check document roles, links, tags, and all scope/non-consequence language;
  and
- introduce no new bijection, permanent count, or mathematical extension.

This audit is not executed by the present theorem-development task. No
Ferrers-permanent count is a competing priority.

## Deferred, Not Prioritized

All other open directions remain deferred until the new KPGE5 theorem is
reviewed and audited. They include the filtered cubic-convergent obstruction,
finer Ferrers-count residuals, the asymptotic coefficient gap, tighter finite
brackets at \(n=5,6\), the radius-one threshold below \(12\), and later
minimizer-set restrictions for \(n\ge94\). Their mathematical context remains
in the relevant proof notes and stable knowledge; this roadmap does not repeat
it.

Large exhaustive certificates, production enumeration-limit increases, and
claims of an exact geometric asymptotic constant remain deliberately
deferred.

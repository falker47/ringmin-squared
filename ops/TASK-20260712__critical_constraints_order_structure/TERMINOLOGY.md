# Terminology Note - Floating And Weak Constraint Labels

This task analyzes finite checked certificate artifacts for `n=3..6`. The labels below are local to this analysis and do not prove behavior for unlisted `n`.

## Rigorously Certified Non-Incidence With Active Constraints

Classification: unresolved claim for this task unless a later proof or certificate explicitly establishes it.

An index would have rigorously certified non-incidence with all active constraints only if there is a defined active-constraint set and a certificate or exact argument proving that no constraint in that active set is incident to the index. A heuristic slack threshold, a candidate lower negative cycle, or a witness slack ranking is not enough.

This task does not currently have such a certificate format. Therefore the research note must not call an index "floating" in this rigorous sense.

## Candidate Floating Index

Classification: heuristic unless independently certified.

A candidate floating index is an index that appears absent from the current empirical proxies for active constraints, such as normalized lower critical-cycle pair labels and the tightest upper-witness slack pairs, across one or more candidate orders.

This is only a prompt for further investigation. It is not a certified geometric statement.

## Weakly Constrained Index

Classification: numerical observation or empirical pattern, depending on scope.

A weakly constrained index is an index with comparatively low incidence in the machine-readable structural data used in this task. The applicable proxies are:

- lower critical-cycle pair-incidence counts;
- membership in minimum-slack and near-minimum upper-witness pairs;
- membership in candidate common-core intersections.

The threshold must be recorded with the output field using it. A weakly constrained label is never a theorem and never a certified non-incidence claim.

## Empirical Non-Critical Index

Classification: empirical pattern.

An empirical non-critical index is an index absent from a specified finite set of extracted critical proxies for a specified finite candidate set. The statement must name the proxy set, candidate orders, `n` values, and thresholds used.

Absence from these proxies does not prove absence from the true active contact graph.

## Rule For This Task

Use the strongest supported term only:

- use "computer-certified result" for checked bracket and candidate-membership facts inherited from verified certificates;
- use "verified fact" for deterministic structural data exactly read or recomputed from checked artifacts;
- use "numerical observation" for finite slack magnitudes and ratios;
- use "empirical pattern" for recurring finite patterns across candidate orders or `n` values;
- use "heuristic" for threshold-based weak-constraint labels;
- use "conjecture" only for explicit falsifiable structural predictions.

Do not convert a tightness threshold into a certified statement.

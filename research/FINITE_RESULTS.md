# Finite Results And Critical Structure Notes

This note summarizes checked finite artifacts for `n=3..6` and structural diagnostics derived from certified candidate orders. It is not an operational log.

Primary machine-readable inputs:

- `examples/small_n_interval_certificate_n3.json` through `examples/small_n_interval_certificate_n6.json`
- `examples/finite_results_summary_n3_n6.json`
- `ops/TASK-20260712__critical_constraints_order_structure/critical_structure_n3_n6.json`

Terminology guardrail: see `ops/TASK-20260712__critical_constraints_order_structure/TERMINOLOGY.md`. This note does not use "floating" as a certified geometric statement.

## Computer-Certified Finite Facts

The following facts are certified only under the repository's documented finite interval-verifier semantics and guarded `mpmath.iv` backend contract.

| `n` | canonical orders | certified global bracket `(L, U]` | candidates | excluded | exclusion gap | midpoint ratio to `n^3/(6*pi)` |
|---:|---:|---|---:|---:|---:|---:|
| 3 | 1 | `(0.3832870361393696523322205393924377858638763427734375, 0.383487036139369685816546962087159045040607452392578125]` | 1 | 0 | undefined | 0.26765464360377962623207969638536051054269711953714 |
| 4 | 3 | `(1.4955284118749971877804227915476076304912567138671875, 1.4957284118749971657535979829845018684864044189453125]` | 1 | 2 | 0.1171644705802874497635457373689860105514526367187500 | 0.44049892792937443214095096407513696627716047627377 |
| 5 | 12 | `(3.934227717145796443531935437931679189205169677734375, 3.9344277171457964215051106293685734272003173828125]` | 2 | 10 | 0.1137866156209259571596703608520328998565673828125 | 0.59328264254399693220972289588517333219782366820764 |
| 6 | 60 | `(8.4678350760883720482752323732711374759674072265625, 8.4680350760883715821591977146454155445098876953125]` | 5 | 55 | 0.0488707956703002821541304001584649085998535156250 | 0.73896673961429321458434021392383309660393607393622 |

Certified candidate orders, modulo the current rotation/reflection convention:

| `n` | candidate orders |
|---:|---|
| 3 | `[3,1,2]` |
| 4 | `[4,1,3,2]` |
| 5 | `[5,1,3,4,2]`; `[5,2,4,1,3]` |
| 6 | `[6,1,2,5,4,3]`; `[6,1,3,4,5,2]`; `[6,2,1,5,4,3]`; `[6,2,5,1,4,3]`; `[6,2,5,4,1,3]` |

Interpretation: candidate membership and exclusion gaps are computer-certified finite facts. Multiple candidates and identical serialized brackets are not exact tie claims.

## Verified Structural Data

The structural analysis translates lower negative-cycle edges from positional nodes to stable index/radius-pair labels and normalizes cyclic edge signatures by rotation.

| `n` | lower critical-cycle pair core across candidate orders |
|---:|---|
| 3 | `{1-2, 1-3, 2-3}` |
| 4 | `{1-3, 1-4, 2-3, 2-4}` |
| 5 | `{2-4, 2-5, 3-4, 3-5}` |
| 6 | `{2-5, 2-6, 3-4, 3-6, 4-5}` |

For `n=5` and `n=6`, every certified candidate order has the same lower-cycle pair set. This is a verified fact about the extracted certificate records. It is not a proof that these are the true active contact pairs at the exact optimum.

## Numerical Observations

Upper witnesses were analyzed by recomputing interval-lower all-pairs slack rankings at the certified upper endpoints.

| `n` | recurring top-ranked upper-witness pairs among candidates |
|---:|---|
| 3 | none recurring because there is one candidate |
| 4 | none recurring because there is one candidate |
| 5 | `1-3`, `2-4`, `2-5`, `3-4`, `3-5` each appears in both candidate top-ranked lists |
| 6 | `2-5`, `3-4`, `4-5` appear in all 5 candidate top-ranked lists; `3-6` appears in 4; `1-3` appears in 2 |

Minimum-slack pairs do not form a single common set across the multiple candidates:

- `n=5`: interval-lower minimum pairs are `2-4` for `[5,1,3,4,2]` and `1-3` for `[5,2,4,1,3]`.
- `n=6`: interval-lower minimum pairs vary among `3-4`, `2-5`, `1-5`, and `1-4`.

Interpretation: identical candidate bracket values are not explained by a common upper-witness minimum-slack pair set.

## Empirical Patterns

For the identical serialized candidate-bracket groups at `n=5` and `n=6`:

| `n` | all share lower pair set | all share pair-kind signature | all share directed cycle signature | all share upper minimum-slack set | common reduced lower-core indices | indices absent from lower core |
|---:|---|---|---|---|---|---|
| 5 | yes | no | no | no | `{2,3,4,5}` | `{1}` |
| 6 | yes | no | no | no | `{2,3,4,5,6}` | `{1}` |

Empirical pattern: repeated serialized candidate brackets in the checked artifacts align with a shared lower-cycle pair core and a common reduced subconfiguration on indices `2..n`. The pattern is not explained by exact directed-cycle equality or by a common upper minimum-slack set.

## Weak Constraint Labels

Heuristic rule used in the machine-readable output: an index is listed as possible weakly constrained only when it has zero lower critical-cycle pair incidence and minimum combined incidence across lower-cycle, minimum-slack, and top-ranked slack-pair proxies.

| `n` | possible weakly constrained indices | empirical non-critical for lower-cycle proxy |
|---:|---|---|
| 3 | none | none |
| 4 | none | none |
| 5 | `{1}` | `{1}` |
| 6 | `{1}` | `{1}` |

These are heuristic or empirical labels only. They do not certify that circle `1` is non-incident with all active constraints, and they do not certify a floating circle.

## Conjectures

CONJECTURE 1: For the next checked multiple-candidate cases, at least one certified candidate group with identical or near-identical brackets will share a lower-cycle pair core supported entirely on indices `2..n`, with index `1` absent from that lower-cycle proxy.

Falsification: a checked candidate group for a later `n` has repeated brackets but no such shared lower-cycle core, or every lower-cycle core necessarily includes index `1`.

CONJECTURE 2: Repeated serialized candidate brackets in `n=5` and `n=6` are primarily caused by a common reduced lower infeasibility subsystem, not by a common upper minimum-slack pair set.

Falsification: tighter certificates or independent fixed-order analysis split the candidate values while preserving the same lower subsystem, or identify a common upper active subsystem that explains the repetition.

CONJECTURE 3: The lower-cycle core size in the first multiple-candidate cases is `n-1`, supported on indices `2..n`; this reduced-core phenomenon persists at least through the next feasible checked case.

Falsification: a later checked multiple-candidate case has lower-cycle core size different from `n-1`, or a core including index `1`.

CONJECTURE 4: Upper-witness near-critical pairs will include some pairs incident to index `1` even when index `1` is absent from the lower-cycle core.

Falsification: a later checked case has index `1` absent from the lower core and also absent from all near-minimum upper slack rankings under the recorded rank rule.

## Open Questions

- Can tighter brackets separate the multiple `n=5` or `n=6` candidates, or do independent methods support a genuine tie?
- Is the shared lower-cycle pair core an artifact of the current bracket generator, or an intrinsic fixed-order obstruction?
- Is there a symmetry or transformation between candidate orders not captured by the current rotation/reflection convention?
- Can the reduced subsystem on indices `2..n` be expressed as a smaller exact geometric or STN problem?
- Which slack proxy, if any, predicts exact active contacts after bracket widths are reduced?

## Warnings

- No exact optimum value has been proved for any `n`.
- No exact tie has been proved between candidate orders.
- No theorem for all `n` or asymptotic theorem has been proved.
- Lower negative cycles certify lower-endpoint infeasibility; they are not exact active contact graphs.
- Upper-witness slacks are diagnostics at certified upper endpoints; positive slack is expected at finite bracket width.
- The word "floating" is deliberately avoided as a certified claim.

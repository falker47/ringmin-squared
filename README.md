# Power-Ringmin: Quadratic Radii

**Power-Ringmin** is an independent research project studying the minimum-central-circle problem for peripheral radii

[
1^2,2^2,ldots,n^2.
]

Given one circle of each radius (k^2), every peripheral circle must be externally tangent to a central circle of radius (R), while all peripheral interiors remain pairwise disjoint. The quantity of interest is the infimum feasible central radius, denoted (R_2^*(n)).

This repository extends the geometric framework of [ringmin](https://github.com/falker47/ringmin), which studies radii (1,2,ldots,n). It is a separate project: results from Ringmin are not assumed to transfer automatically to quadratic radii.

## Current research status

The project currently contains:

- an exact fixed-order formulation using a circular system of difference constraints / Simple Temporal Network over **all pairwise** angular non-overlap constraints;
- checked finite interval-certificate artifacts for (n=3,4,5,6), interpreted as computer-certified results under the documented guarded `mpmath.iv` enclosure contract;
- an independent, bounded Arb/python-flint cross-check of the decisive endpoint signs for the checked (n=3) certificate;
- exact combinatorial results for the maximum cyclic-ratio surrogate (Lambda), together with rigorous links between (Lambda), fixed-order thresholds, and (R_2^*(n));
- an active program of structural and asymptotic work on product-distance surrogates and KR1/KR1G order families.

A former target,
[
R_2^*(n)=rac{n^3}{6pi}(1+o(1)),
]
has been disproved. **This repository does not currently claim an exact global asymptotic constant for (R_2^*(n)).**

For the authoritative classification of established results, conjectures, limitations, and disproved claims, see [PROJECT_KNOWLEDGE.md](PROJECT_KNOWLEDGE.md).

## Geometry and fixed-order feasibility

For peripheral radii (r_i,r_j) and central radius (R), the required angular separation is

[
	heta_R(r_i,r_j)
=
2arcsin
sqrt{
rac{r_i r_j}
{(R+r_i)(R+r_j)}
}.
]

For quadratic radii (r_k=k^2),

[
	heta_R(i^2,j^2)
=
2arcsin
left(
rac{ij}
{sqrt{(R+i^2)(R+j^2)}}
ight).
]

For a fixed cyclic order, the repository enforces the full all-pairs geometry through difference constraints. Feasibility is equivalent to the absence of a negative directed cycle in the corresponding STN; see [research/FIXED_ORDER_ANGULAR_STN.md](research/FIXED_ORDER_ANGULAR_STN.md) for the detailed proof.

## Reproducibility

Python 3.11+ is required.

```bash
python -m pip install -e ".[test,crosscheck]"
python -m pytest
python -m power_ringmin.verify_checked_artifacts
```

The checked finite artifacts live in [examples/](examples/), including the (n=3,ldots,6) interval certificates and their derived summary.

The certification boundary is explicit: the exact real-arithmetic implication is proved separately from the numerical interval backend. See [docs/INTERVAL_BACKEND_TRUST.md](docs/INTERVAL_BACKEND_TRUST.md) before treating the finite artifacts as computer-certified evidence.

## Repository map

| Path | Role |
| --- | --- |
| `src/power_ringmin/` | computational library, fixed-order evaluation, interval verification, finite-result analysis |
| `verify.py` | standalone high-precision fixed-order verifier scaffold |
| `examples/` | checked finite artifacts and reproducible example outputs |
| `research/` | authoritative detailed mathematical proofs and research roadmap |
| `PROJECT_KNOWLEDGE.md` | compact stable research knowledge and claim classification |
| `docs/INTERVAL_BACKEND_TRUST.md` | interval-backend trust boundary and independent cross-check scope |
| `CURRENT_STATUS.md` | current bounded research task / handoff state |
| `ops/` | task-local evidence, exact checkers, and verification dossiers |
| `UPSTREAM_RINGMIN.md` | provenance and controlled import history from Ringmin |

The main research roadmap is [research/NEXT_RESEARCH_STEPS.md](research/NEXT_RESEARCH_STEPS.md).

## Relationship to Ringmin

[Ringmin](https://github.com/falker47/ringmin) studies the original radius sequence (1,2,ldots,n). Power-Ringmin reuses selected computational ideas with explicit provenance, but quadratic radii change the scale and the mathematics substantially.

In particular:

- upstream finite optima are not evidence for quadratic-radii optima;
- upstream asymptotic theorems are not silently generalized here;
- imported code is adapted and retested against the quadratic sequence;
- mathematical claims are classified explicitly as exact theorems, computer-certified finite results, numerical observations, heuristics, conjectures, or open questions.

See [UPSTREAM_RINGMIN.md](UPSTREAM_RINGMIN.md) for the import audit and provenance record.

## License

MIT. See [LICENSE](LICENSE).

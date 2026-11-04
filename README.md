# Power-Ringmin: Quadratic Radii

Power-Ringmin investigates a geometric packing problem: **how small can a central circle be if it must touch one circle of each radius \(1^2,2^2,\ldots,n^2\), without any two peripheral circles overlapping?**

Each peripheral circle is externally tangent to the central circle. Peripheral circles may also touch one another, but their interiors must remain disjoint. Their cyclic arrangement is not prescribed.

We write \(R_2^*(n)\) for the infimum of all feasible central radii.

This is a separate research project from [Ringmin](https://github.com/falker47/ringmin), which studies peripheral radii \(1,2,\ldots,n\). Power-Ringmin adapts parts of the computational framework, but its mathematical results and certification claims are established independently.

## Mathematical formulation

Let the central circle have radius \(R>0\). The center of a peripheral circle of radius \(i^2\) must lie at distance \(R+i^2\) from the central center.

For two peripheral circles with radii \(i^2\) and \(j^2\), the minimum angular separation of their centers is

$$
\theta_R(i^2,j^2)
=
2\arcsin\left(
\frac{ij}{\sqrt{(R+i^2)(R+j^2)}}
\right).
$$

This expression is an exact geometric constraint, not a small-angle approximation.

For a fixed cyclic order, choose lifted angular positions

$$
0=p_0<p_1<\cdots<p_{n-1}<2\pi.
$$

Every pair of positions \(i<j\) must satisfy

$$
\theta_{ij}(R)
\le p_j-p_i
\le 2\pi-\theta_{ij}(R),
$$

where \(\theta_{ij}(R)\) is evaluated using the peripheral radii assigned to those positions.

Both inequalities matter. Checking only neighboring circles in a proposed cyclic order is insufficient to establish geometric feasibility.

The full system can be represented as a **Simple Temporal Network (STN)**, or system of difference constraints. In exact arithmetic, a fixed order is feasible precisely when its directed constraint graph has no negative cycle. A feasible angular placement can then be recovered from shortest-path potentials.

The proof of this equivalence, together with the monotonicity and fixed-order threshold results, is in [Fixed-Order Angular Feasibility and STN Certificate Semantics](research/FIXED_ORDER_ANGULAR_STN.md).

## Established mathematical results

### Cubic growth and asymptotic bounds

The central radius grows on the cubic scale:

$$
R_2^*(n)=\Theta(n^3).
$$

More precisely, the current proved global bounds are

$$
\frac{434+4\sqrt{2}}{1587\pi}
\le
\liminf_{n\to\infty}\frac{R_2^*(n)}{n^3}
\le
\limsup_{n\to\infty}\frac{R_2^*(n)}{n^3}
\le
\frac{857}{3000\pi}.
$$

The lower coefficient follows from an all-fixed-\(k\) family of combinatorial lower-bound arguments. Each finite \(k\) is handled before taking the asymptotic limit, and the supremum over \(k\) is taken afterward. It is not a theorem permitting \(k\) to grow with \(n\).

The upper coefficient comes from explicit cyclic-order constructions and a monotone cancellation argument that extends the bound to every sufficiently large index, rather than only a subsequence.

**These coefficients do not match.** The inequalities establish cubic growth and a bounded range for possible asymptotic behavior, but they do not prove that \(R_2^*(n)/n^3\) converges or identify an exact leading constant.

Detailed arguments are available in:

- [All-\(n\) Bounds and Radius-One Insertion](research/ALL_N_LOWER_BOUND.md)
- [Fixed-Order Cycle Ratio](research/FIXED_ORDER_CYCLE_RATIO.md)

### An exact combinatorial surrogate

The project studies a maximum cyclic-ratio quantity \(\Lambda(\sigma)\), determined by products of peripheral indices along directed cycles or, equivalently, by cyclic product sums over induced subsets of an order.

Let

$$
\Lambda_n=\min_\sigma\Lambda(\sigma),
$$

with the minimum over all complete cyclic orders. The repository proves the strict geometric comparison

$$
\frac{\Lambda_n}{\pi}-n^2
<
R_2^*(n)
<
\frac{\Lambda_n}{\pi}.
$$

This provides a rigorous connection between exact combinatorial optimization and the original geometry. It does not make the two optimization problems identical.

Several exact classifications, finite enumerations and structural theorems concern \(\Lambda\) or related product-distance objectives. Their scope is specified in [Fixed-Order Cycle Ratio](research/FIXED_ORDER_CYCLE_RATIO.md) and [Product-Distance Surrogate](research/PRODUCT_DISTANCE_SURROGATE.md). An exact result for a surrogate must not be read as an exact geometric optimum.

### Eventual insertion of the unit-radius circle

A separate geometric theorem shows that, for every \(n\ge12\), any feasible arrangement of the core circles with radii

$$
2^2,3^2,\ldots,n^2
$$

admits insertion of the remaining circle of radius \(1\) without increasing the central radius.

Consequently, the full and core feasible-radius sets coincide for \(n\ge12\), and

$$
R_2^*(n)=R_{2:n}^*
\qquad(n\ge12),
$$

where \(R_{2:n}^*\) denotes the infimum for the core alone.

The threshold \(12\) is sufficient; it is not known to be minimal. This theorem does not establish that the unit-radius circle is free of active contacts in every optimal arrangement.

See [All-\(n\) Bounds and Radius-One Insertion](research/ALL_N_LOWER_BOUND.md).

### A disproved asymptotic proposal

An earlier research target was

$$
R_2^*(n)=\frac{n^3}{6\pi}(1+o(1)).
$$

It is **disproved** by the rigorous lower bounds. The stronger proposed expansion with an \(O(n^2)\) remainder is also false.

Neither expression is an accepted asymptotic formula for Power-Ringmin.

The distinction between established results, conditional statements, numerical observations, conjectures and disproved claims is maintained in [PROJECT_KNOWLEDGE.md](PROJECT_KNOWLEDGE.md).

## Checked finite results

The repository contains exhaustive small-\(n\) interval-certificate artifacts for \(n=3,4,5,6\). Each covers all canonical cyclic orders modulo rotation and reflection.

Under the documented interval-backend assumptions, the certificates establish the following global brackets.

| \(n\) | Canonical orders checked | Remaining candidate orders | Enclosure for \(R_2^*(n)\) |
| ---: | ---: | ---: | --- |
| 3 | 1 | 1 | \((0.3832870361,\ 0.3834870362]\) |
| 4 | 3 | 1 | \((1.4955284118,\ 1.4957284119]\) |
| 5 | 12 | 2 | \((3.9342277171,\ 3.9344277172]\) |
| 6 | 60 | 5 | \((8.4678350760,\ 8.4680350761]\) |

The displayed decimal endpoints have been rounded outward for readability. The JSON artifacts contain the full certified decimal strings.

For each fixed order, verification combines two different witnesses:

1. **Lower endpoint:** an explicitly checked negative cycle excludes the proposed lower radius and a right neighborhood of it.
2. **Upper endpoint:** an explicitly checked angular placement satisfies every pairwise constraint, establishing feasibility at the upper radius.

The interval is therefore **open at the lower endpoint and closed at the upper endpoint**.

A remaining candidate order has not been excluded by these certificates. Multiple candidates, including those for \(n=5\) and \(n=6\), do not establish exact ties. No exact numerical value of \(R_2^*(n)\) is claimed.

Primary certificate files:

- [\(n=3\)](examples/small_n_interval_certificate_n3.json)
- [\(n=4\)](examples/small_n_interval_certificate_n4.json)
- [\(n=5\)](examples/small_n_interval_certificate_n5.json)
- [\(n=6\)](examples/small_n_interval_certificate_n6.json)

The [derived finite-results summary](examples/finite_results_summary_n3_n6.json) records candidate sets, exclusion gaps and source digests. [Finite Results and Critical Structure Notes](research/FINITE_RESULTS.md) explains the mathematical interpretation and separates certified statements from structural diagnostics and empirical patterns.

### Certification boundary

The finite certificates use a guarded `mpmath.iv` interval backend identified as `mpmath_iv_guarded_atan2_v1`.

The exact mathematical implication from genuine interval enclosures to valid lower and upper bounds is proved separately. Applying that implication to the stored artifacts depends on the backend, endpoint conversion and subsequent bound arithmetic providing conservative enclosures.

Those implementation-level assumptions have **not** been completely independently audited or formally proved. The decimal guard is an explicit safety margin, not a proof of the underlying interval arithmetic.

An additional test-only check uses Arb through `python-flint` to independently recompute the decisive endpoint signs for the checked \(n=3\) record. It covers the three lower-cycle edge occurrences and all six directional upper-witness slacks. It does not independently verify the \(n=4,5,6\) artifacts or audit Arb itself.

Accordingly, the finite brackets are described as **computer-certified under the documented guarded-backend contract**, not as independently audited, exact optimum values or machine-checked proofs of the entire numerical stack.

Read [Interval Backend Trust](docs/INTERVAL_BACKEND_TRUST.md) for the precise assumptions, coverage and outstanding verification work.

## Installation and verification

The project requires **Python 3.11 or newer**. The core package uses `mpmath`; numerical cross-checks use NumPy and SciPy. The test dependencies include `pytest`, `jsonschema` and the pinned `python-flint` test backend.

From a terminal:

```bash
git clone https://github.com/falker47/ringmin-squared.git
cd ringmin-squared
python -m pip install -e ".[test,crosscheck]"
```

Run the test suite from the repository root:

```bash
python -m pytest
```

Revalidate the committed finite certificates and their derived summary:

```bash
python -m power_ringmin.verify_checked_artifacts
```

The equivalent installed command is:

```bash
power-ringmin-verify-checked-artifacts
```

The checked-artifact command validates JSON Schema structure, reloads the semantic certificate validators, rechecks embedded local interval brackets and verifies consistency with the derived summary. For the currently checked files it processes four certificates containing 76 local order brackets.

To run the bounded independent Arb cross-check separately:

```bash
python -m pytest tests/test_n3_arb_interval_crosscheck.py
```

A standalone high-precision numerical fixed-order check is also available:

```bash
python verify.py --order 9,1,4 --radius 0.384 --digits 80
```

Here `--order` supplies the **actual peripheral radii**, rather than their indices. This verifier evaluates a supplied order and radius numerically. It is not an exhaustive global certificate generator or a replacement for the interval-certificate validator.

For batch export and verification examples, see [Fixed-Order Batch End-to-End Example](examples/fixed_order_batch_end_to_end/README.md). Certificate generation has explicit work-count and retry limits; generating a new artifact is not equivalent to having independently certified it.

The [GitHub Actions verification workflow](.github/workflows/verification.yml) runs the Python test suite, checked-artifact verification, focused schema tests and text-file hygiene checks on Python 3.11, 3.12 and 3.13.

For reproducible scientific comparisons, record the repository commit, Python version, dependency versions, artifact metadata and verification environment. A successful CI run establishes that the configured checks completed on its tested revision; it is not a general mathematical proof.

## Repository guide

| Location | Contents |
| --- | --- |
| [`src/power_ringmin/`](src/power_ringmin/) | Geometry, fixed-order evaluators, numerical cross-checks, exact combinatorial tools, search, exporters and interval verification |
| [`tests/`](tests/) | Unit, regression, mathematical consistency, artifact-validation and independent cross-check tests |
| [`schemas/`](schemas/) | JSON schemas for recorded results and certificates |
| [`examples/`](examples/) | Checked finite certificates, derived summaries and reproducible examples |
| [`research/FIXED_ORDER_ANGULAR_STN.md`](research/FIXED_ORDER_ANGULAR_STN.md) | Exact geometric/STN equivalence and certificate implications |
| [`research/ALL_N_LOWER_BOUND.md`](research/ALL_N_LOWER_BOUND.md) | Global bounds, radius-one insertion and constructive upper bounds |
| [`research/FIXED_ORDER_CYCLE_RATIO.md`](research/FIXED_ORDER_CYCLE_RATIO.md) | Exact cycle-ratio theory, finite combinatorics and asymptotic constructions |
| [`research/PRODUCT_DISTANCE_SURROGATE.md`](research/PRODUCT_DISTANCE_SURROGATE.md) | Product-distance optimization and its distinct mathematical scope |
| [`research/FINITE_RESULTS.md`](research/FINITE_RESULTS.md) | Interpretation of checked small cases and structural diagnostics |
| [`PROJECT_KNOWLEDGE.md`](PROJECT_KNOWLEDGE.md) | Stable results and explicit classification of claims |
| [`docs/INTERVAL_BACKEND_TRUST.md`](docs/INTERVAL_BACKEND_TRUST.md) | Numerical certification assumptions and limitations |
| [`research/NEXT_RESEARCH_STEPS.md`](research/NEXT_RESEARCH_STEPS.md) | Research roadmap |
| [`CURRENT_STATUS.md`](CURRENT_STATUS.md) | Dated task handoff; not a live CI or repository-status dashboard |
| [`ops/`](ops/) | Task-specific evidence, experimental records and proof audits |

## Open research questions

The principal unresolved geometric question is the exact asymptotic behavior of \(R_2^*(n)\). Cubic growth is established, but the available lower and upper coefficients remain separated.

Other questions include whether tighter finite certificates can distinguish the remaining candidate orders for \(n=5,6\), whether the sufficient radius-one insertion threshold can be improved, and which structural insights from cyclic-ratio and product-distance surrogates can be turned into stronger geometric bounds.

The repository also investigates order families such as KR1 and KR1G. Results for a particular family, relaxation or conditional construction retain their stated scope; they are not general optimal-order theorems unless separately proved.

See the [research roadmap](research/NEXT_RESEARCH_STEPS.md) for the detailed programme. Research task states and mathematical conclusions should be read with their dated evidence and proof references, rather than inferred from an individual test result.

## Relationship to Ringmin

[Ringmin](https://github.com/falker47/ringmin) studies the original sequence \(1,2,\ldots,n\). Power-Ringmin shares geometric motivation and adapts selected computational components under the applicable MIT licensing terms.

The [upstream provenance record](UPSTREAM_RINGMIN.md) identifies imported or adapted components, their source revision and their local verification history.

Ringmin's numerical certificates, theorems, structural conjectures and publication record are not automatically valid for the quadratic-radii problem. The two projects must be cited and evaluated separately.

## Authorship, citation and license

**Author:** Maurizio Falconi.

The project has used AI-assisted research and development workflows, with task evidence and operating practices recorded in the repository. AI-generated reasoning or code is not treated as independent mathematical verification; claims depend on their stated proofs, algorithms, tests and certification assumptions.

When citing this repository, identify *Power-Ringmin: Quadratic Radii*, Maurizio Falconi, the [GitHub repository](https://github.com/falker47/ringmin-squared) and the relevant commit or version. No separate DOI or published Power-Ringmin paper is asserted here.

The repository is distributed under the **MIT License**. See [LICENSE](LICENSE) and [UPSTREAM_RINGMIN.md](UPSTREAM_RINGMIN.md) for the license text and imported-code provenance.

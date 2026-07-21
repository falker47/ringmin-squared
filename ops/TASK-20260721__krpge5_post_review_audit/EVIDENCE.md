# EVIDENCE - TASK-20260721 / KRPGE5 Post-Review Audit

## Index

| ID | Type | Description | Source/path | Result |
|---|---|---|---|---|
| EV-001 | source / exact derivation / computation / test / hosted CI | Independent audit of KRPGE5-1--KRPGE5-36 at the accepted baseline | authoritative proofs, local commands, GitHub Actions run `29777676234` | PASS |

## EV-001 - Independent KRPGE5 Post-Review Audit

- **Date:** 2026-07-21
- **Mode:** STRICT
- **Classification:** the symbolic conclusions below are an independent
  verification of existing exact theorems; the finite enumerations are
  bounded exact corroboration; local test results and exact-SHA CI metadata
  are verified computational facts. No new theorem or construction is
  asserted.

### Baseline And Source Integrity

- The audited commit is
  [`a15a4d34cc034b669f02382e2e4f27b4822ed382`](https://github.com/falker47/ringmin-squared/commit/a15a4d34cc034b669f02382e2e4f27b4822ed382),
  titled `Correct the KRPGE5 geometric closure`, with tree object
  `2543f29f79968d8b09144acf20d1f7e0339c1685`.
- The baseline was read directly with `git show <SHA>:<path>`. The source
  hierarchy used for the derivation was:

  - PGE5-1--PGE5-26 in
    `research/PRODUCT_DISTANCE_SURROGATE.md`;
  - CR12p, CR22, CR27, CR28a, K825-1--K825-9, and
    KRPGE5-1--KRPGE5-36 in
    `research/FIXED_ORDER_CYCLE_RATIO.md`.

- Startup `HEAD` was
  `92bbb857d1b9ce4b67b8ca8dd125564c0ac52f28`. A path-limited
  `git diff --exit-code <baseline>..HEAD` was empty for both authoritative
  proofs, the KRPGE5 diagnostic, workflow, `src/`, `tests/`, `schemas/`,
  `examples/`, `verify.py`, and `pyproject.toml`. The complete name-only
  diff contained only six status, knowledge, roadmap, and dossier documents.
- Matching baseline/current blob IDs independently confirmed:

  - KRPGE5 proof: `454ea1c09d461567ca33a760b1a520b05540dfc8`;
  - KRPGE5 diagnostic: `f83651ab542f9b225ca0d304d6e94f5a7c7886f2`;
  - verification workflow:
    `53e7315f3ec8f4eb513c2215e473896963e414cb`.

This distinguishes two operations: symbolic reading was tied directly to
the accepted SHA; fresh executions used current files only after their
relevant blobs were proved identical to that SHA.

### Oracle Separation And Audit Method

- The prior dossier was inspected to recover scope and chronology required by
  the operating contract. Its displayed formulas and recorded expected
  values were not used as pass/fail oracles.
- Expected expressions were regenerated from the literal PGE5 label
  definitions and cyclic word. Manual exact algebra established the case
  partitions and inequalities. A separate read-only SymPy 1.14 expansion
  recomputed raw neighbors, block sums, residue substitutions, cancellation,
  K825 specialization, and the `n`-form before comparison with KRPGE5.
- Independent standard-library reconstruction checked the literal word,
  label partition, all-pairs `W`, deletion gains, proper cyclic arcs, and
  max-plus subset optimum on bounded rows. It neither imported nor invoked
  the task diagnostic.
- Only after those derivations were fixed were their results compared with
  KRPGE5-1--KRPGE5-36. The repository's canonical diagnostics were then run
  as a separate regression layer.

### Support And Complete-Score Rederivation

Starting from `d=8m+5`, `n=10m+4`, and
`T=d(d-1)/2`, direct comparison of the five path-bearing distance-two
products for a triple `P_k`, `0<=k<=m`, in gap `G_j` gives

`P_k is local in G_j iff j(d-1-2k) <= 2kd iff k >= kappa_j`.

The genuine closing word is `(n,2,P_k,4m+1,d)`, not a continuation of a
nonclosing formula. It gives

`kappa_(2m-1) = ceil((4m^2-1)/(5m+2)) = floor((4m+3)/5) = q`,

with `P_q` strictly local and `P_(q-1)` strictly nonlocal. The doubleton
and every actual singleton are local in every gap. The extendible relation is
exactly the forced edge `(0,0)` plus every local edge in a positive column;
explicit interval-shift matchings witness each such edge.

The five image blocks of KRPGE5-1 are
`[0,q-1]`, `[q+1,m]`, `{m+1}`, `[m+2,2m-1]`, and `{q}`.
They are disjoint and exhaustive. The second block is empty exactly for
`m=2,3`; the fourth is empty exactly for `m=2` and is a singleton for
`m=3`. Every assigned edge lies in the exact support. The
all-distance PGE5 bounds cover distances three and at least four, while the
forced pair `(d,d-1)` at distance two attains `T`. Therefore
`W=T=W_n`; this is not an adjacent-only check.

### Nine Deletion Classes

Deleting the isolated holes `H_m={2,...,4m}` from the literal cyclic core
leaves exactly the backbone

    (L,(E_j,P_j)_(j<q),(E_j,P_(j+1))_(q<=j<m),E_m,a,b,
     (E_j,x_(3m-j))_(m<j<=2m-2),E_(2m-1),P_q),

where `L=4m+1`. Substituting the two literal backbone neighbors into
`h_z=uw-z(u+w)` regenerates these nine classes:

| Hole and range | Independently expanded deletion gain |
|---|---|
| `lambda_j`, `0<=j<q` | `-4j^2+(28m+12)j+36m+20` |
| `rho_(j+1)`, `0<=j<q` | `-4j^2+(28m+8)j+52m+27` |
| `lambda_j`, `q<=j<=m-1` | `-4j^2+(28m+6)j+28m+10` |
| `rho_(j+1)`, `q<=j<=m-1` | `-4j^2+(28m+2)j+44m+13` |
| `lambda_m` | `17m^2+36m+15` |
| `rho_(m+1)` | `17m^2+60m+34` |
| `lambda_j`, `m+1<=j<=2m-2` | `-j^2+(29m+14)j-4m^2+27m+15` |
| `rho_(j+1)`, `m+1<=j<=2m-2` | `-j^2+(29m+15)j-4m^2+45m+27` |
| closing `lambda_(2m-1)=2` | `80m^2-20mq+36m-4q` |

Their cardinalities sum to
`2q+2(m-q)+2+2(m-2)+1=4m-1=|H_m|`; thus no hole is omitted or counted
twice. The six ranged classes have positive forward differences on their
literal ranges. Direct boundary comparisons put every class strictly above
`36m+20` except the first value of the first class. Hence the deletion
minimum is uniquely `36m+20` at `lambda_0=4m`.

### Exhaustive Shortcut Audit

For a compressed arc `C=(z_0,...,z_s)`, `s>=2`, the independently used
margin was `M(C)=sum(z_i z_(i+1))-z_0 z_s`.

- A low endpoint gives `M>=L(a+b)-ab>=4L-4=16m`, covering either
  orientation and one or two low endpoints.
- For `s=2`, all `6m+4=|B_m|` middle roles are partitioned as
  `(m+1)+2+(m-2)+1+2(m+1)+2m`: triple connectors, two doubleton roles,
  actual singletons, `L`, outer-triple labels, and terminals.
- The connector margin
  `-8k^2+(32m+13)k+4m+2` increases on `0<=k<=m`, so its unique
  minimum is `4m+2` at `c_0`.
- The closing middle role is
  `M(B_q,L,E_0)=8mq-16m+8q-7`: it equals `9` at `m=2` and exceeds
  `4m+2` for `m>=3`.
- Both doubleton roles, all reversed-singleton roles, outer labels, and
  terminals are strictly larger. The singleton class is treated literally
  when empty at `m=2`.
- For `s=3`, every internal adjacent pair contains a label at least
  `R=6m+3` and one at least `L`, except the separately checked
  doubleton. This proves `M>=RL` for both ordinary and cut-crossing pairs;
  the doubleton window gives `34m^2+54m+21`.
- For `s>=4`, the four endpoint corners give
  `M>=12m^2-12m-6+(s-4)L^2>4m+2`.
- The literal closing segment
  `E_(2m-1),A_q,c_q,B_q,L,E_0` was used throughout. Thus the retained
  closing middle, both adjacent pairs through the cut, and every longer
  cut-crossing arc are covered.

Consequently the unique shortcut minimum is `9` on
`(B_q,L,E_0)=(15,9,21)` when `m=2`, and `4m+2` on
`(A_0,c_0,B_0)` for `m>=3`. Strict deletion and shortcut gains plus
K825-6--K825-9 force every maximizing subset of size at least two to be
exactly `B_m`; the lower bound `P(B_m)>=2n(n-1)>n^2` excludes a
singleton tie.

### Block Sum, Residues, Cancellation, And K825

Expanding the six literal block types and summing their actual ranges gives

`K_*=(1714m^3+2439m^2+24mq+965m+12q^2+60q+120)/6`.

Substitution of `q=(4m+c_r)/5` with
`(c_0,c_1,c_2,c_3,c_4)=(0,1,2,3,-1)` independently yields:

| `m mod 5` | `150 K_*` |
|---|---|
| 0 | `42850m^3+61647m^2+25325m+3000` |
| 1 | `42850m^3+61647m^2+25541m+3312` |
| 2 | `42850m^3+61647m^2+25757m+3648` |
| 3 | `42850m^3+61647m^2+25973m+4008` |
| 4 | `42850m^3+61647m^2+25109m+2712` |

The branches begin at `m=5,6,2,3,4`, respectively. Direct cancellation
of only the changed singleton gaps gives
`K_up-K_*=(m-1)(m-2)(m-3)/3`, including the empty/neutral rows
`m=2,3`.

Specializing K825 from its general parameters
`(e,v,epsilon,chi,Gamma)=(5,2m,1,0,-4m-2)` gives
`K_825=(572m^3+819m^2+361m+44)/2`. Independent subtraction gives

`K_825-K_*=(m^3+9m^2-12mq+59m-6q^2-30q+6)/3`.

It is strictly positive: at `m=2` its numerator is 36, while for
`m>=3` the bound `q<=m` gives at least
`(m-3)^3+2m+33`. Substitution into all five residue classes reproduces
KRPGE5-30. Finally, replacing `m=(n-4)/10` gives coefficientwise

`3000K_*=857n^3+1911n^2+1200nq-8174n+6000q^2+25200q+7272`,

so the fixed-family cubic coefficient is exactly `857/3000`.

### CR Closure And Limits

For any insertion gap, deleting label one recovers the same core. CR12p
therefore gives `Lambda(sigma_(m,g))=K_*`; CR22 gives the two strict
fixed-order bounds `K_*/pi-n^2 < rho_(sigma_(m,g)) < K_*/pi`.
CR28a supplies only `Lambda_n<=K_*`, and CR27 supplies
`R_2^*<Lambda_n/pi`. Their directions yield exactly the one-sided chain
in KRPGE5-35. Since `q=O(n)`, the exact `n`-form yields the stated
subsequential limsup in KRPGE5-36.

The derivation does not assert `Lambda_n=K_*`, a matching global lower
bound, an all-`n` limsup, geometric optimality, an exact global leading
constant, or insertion-gap independence of the angular threshold.

### Independent Finite Corroboration

- A fresh literal reconstruction, separate from the dossier diagnostic,
  checked structure, all-pairs `W=W_n`, all deletion gains, and all
  backbone arcs for `m=2,...,100`; every original-word proper arc at
  `m=2,3`; candidate-free max-plus over all induced subsets for
  `m=2,...,30`; and score, cancellation, `n`-form, and K825 gap through
  `m=1000`. Every check passed and every computed argmax count was one.
- Command:
  `python -B ops/TASK-20260720__pge5_post_review_consolidation/pge5_independent_oracle.py`.
  Result: PASS for 11,476 literal cells, 8,914 forced decisions, 8,515
  supported cells, and 399 rejected cells over `m=2,...,20`; exhaustive
  `m=2,3,4` enumeration covered 41,064 bijections, 760 compatible and
  40,304 incompatible assignments, and 36,795,192 all-pairs comparisons.
  It found local compatibility exactly equivalent to `W=W_n`.
- Boundary rows were reconstructed literally:
  `m=2,q=2,K_*=4297`, deletion minimum 92, shortcut minimum 9; and
  `m=3,q=3,K_*=11958`, deletion minimum 128, shortcut minimum 14, with
  order-neutral singleton reversal.

These finite checks are corroboration and do not replace the symbolic
all-`m` case exhaustion.

### Requested Local Regression

- Fresh local environment: Python 3.14.3, pytest 9.0.2, and SymPy 1.14.0.

- Command:
  `python -B ops/TASK-20260720__pge5_singleton_reversal_exact_k/exact_diagnostic.py`.
  Result: PASS over 29 max-plus/all-arcs rows `m=2,...,30`, 37,475,656
  transitions, 968,774 proper arcs including the cyclic cut, 4,727
  label-one insertion gaps, 484,387 neighbor-pair inequalities, and 999
  formula/support rows through `m=1000`. The exact `n`-form coefficient
  tuple was
  `(857000,1219500,12000,482500,6000,30000,60000)`.
- First full-suite attempt: an explicitly sandboxed temporary directory
  produced `252 passed, 31 errors`; all 31 errors occurred during
  `tmp_path` setup with `PermissionError`, not in project assertions.
  This failed environmental attempt is retained rather than hidden.
- Approved ordinary-environment rerun:
  `$env:PYTHONDONTWRITEBYTECODE='1'; python -m pytest -p no:cacheprovider`.
  Result: `283 passed in 65.82s`.
- Command:
  `$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='src'; python -m power_ringmin.verify_checked_artifacts`.
  Result: four certificates, 76 local brackets, and summary rows
  `n=3,4,5,6` verified.
- Command:
  `$env:PYTHONDONTWRITEBYTECODE='1'; python -m pytest -p no:cacheprovider tests/test_checked_artifact_schema_validation.py`.
  Result: `4 passed in 0.88s`.

### Exact-SHA Hosted CI Inspection

- Method: queried GitHub Actions by the exact
  `head_sha=a15a4d34cc034b669f02382e2e4f27b4822ed382`, obtaining one
  available run. Then independently fetched that run's current job list and
  decoded logs through the connected GitHub app. No run for an ancestor SHA
  was queried or reused.
- Run:
  [Verification `29777676234`](https://github.com/falker47/ringmin-squared/actions/runs/29777676234),
  run 90, attempt 1, event `push`, branch `main`, status `completed`,
  conclusion `success`; created `2026-07-20T20:48:56Z` and completed
  `2026-07-20T20:50:36Z`.
- Each decoded job log explicitly shows checkout and
  `git log -1 --format=%H` resolving to the exact accepted SHA:

  - [Python 3.11, job `88470931481`](https://github.com/falker47/ringmin-squared/actions/runs/29777676234/job/88470931481):
    CPython 3.11.15, `283 passed in 71.80s`, four certificates, 76 local
    brackets, and `4 passed in 0.79s` for schema validation.
  - [Python 3.12, job `88470931399`](https://github.com/falker47/ringmin-squared/actions/runs/29777676234/job/88470931399):
    CPython 3.12.13, `283 passed in 69.53s`, the same artifact counts, and
    `4 passed in 0.76s`.
  - [Python 3.13, job `88470931382`](https://github.com/falker47/ringmin-squared/actions/runs/29777676234/job/88470931382):
    CPython 3.13.14, `283 passed in 73.05s`, the same artifact counts, and
    `4 passed in 0.88s`.

- The
  [exact-SHA workflow](https://github.com/falker47/ringmin-squared/blob/a15a4d34cc034b669f02382e2e4f27b4822ed382/.github/workflows/verification.yml)
  has the same blob `53e7315f3ec8f4eb513c2215e473896963e414cb`
  as the locally inspected workflow. It runs full pytest, checked-artifact
  verification, focused schema validation, and tracked-text whitespace on
  Python 3.11--3.13.
- Important limit: that workflow does not run the task-local
  `exact_diagnostic.py`. Its PASS is therefore separate local evidence,
  not attributed to hosted CI. The hosted result also does not independently
  validate GitHub, runner images, actions, or dependency supply chains.

### Result And Limits

Every requested audit criterion is satisfied. The roadmap may close this
post-review audit. The task changes no mathematical source, construction,
diagnostic, workflow, production code, test, schema, or checked artifact.
The exact theorem classifications and their existing geometric limitations
remain unchanged.

Final documentary inspection enumerated exactly these five changed files:
`CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`, and the three
files in this dossier. The tracked diff and all untracked contents were read.
The following checks passed:

- KRPGE5 tags 1--36 are sequential and unique at the baseline, and CR12p,
  CR22, CR27, and CR28a each have one defining tag;
- every new relative file target and heading anchor resolves;
- `git diff --check` reports no tracked-diff error;
- an explicit scan reports no trailing whitespace in either tracked or
  untracked changed files;
- no changed cache or bytecode path exists; and
- the audited mathematical, diagnostic, workflow, production, test, schema,
  and artifact inputs remain byte-identical between the baseline and startup
  `HEAD`.

Read-only Git status emitted a permission warning for
`C:/Users/Falker/.config/git/ignore`; it nevertheless returned the complete
expected changed-file set, so this environmental warning did not limit scope
inspection.

- **Linked log entry:**
  `TASK_LOG.md#2026-07-21---final-documentary-inspection-and-handoff`.

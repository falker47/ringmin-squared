# EVIDENCE - Finite Three-Prefix Theorem

## EV-01 - Baseline And Isolation

- Classification: verified fact.
- Check: STRICT startup, Git state, focused historical tests, and prior exact
  diagnostic.
- Result: clean `main` worktree at `fe4a316`; six focused three-prefix tests
  passed; the normalized-simplex diagnostic passed all 203,489 grid states.
- Limitation: these checks are regression evidence, not the new finite proof.

## EV-02 - Exact Uniform Domain

- Classification: exact finite-exhaustive plus symbolic theorem.
- Result: the integer cutoffs satisfy every block, order, non-vacuity, and
  middle-clipped condition for all \(n\ge159\). Exact finite arithmetic covers
  \(159\le n\le170\); the symbolic inequalities cover \(n\ge171\).
- Minimality: at \(n=158\),
  \((r_n,s_{1,n},s_{2,n},s_{3,n})=(67,67,64,62)\), so the first segment is
  empty.

## EV-03 - Literal Finite Lower Theorem

- Classification: exact finite method-specific theorem.
- Result: finite clipped weights
  \(\widehat\lambda_{i,n}=4-(n+r_n)/s_{i,n}\) are strictly ordered and give
  \(\widehat F_{i,n}=(4s_{i,n}-n-r_n)^2/2\). The established one-use charging
  identity proves
  \[
  \Lambda_n\ge\mathcal I_{3,n}\ge\mathcal B_{3,n},
  \qquad
  \mathcal I_{3,n}=\lceil\mathcal B_{3,n}\rceil
  \qquad(n\ge159).
  \]
- Scope: no four-prefix charging or production path is used.

## EV-04 - Controlled Remainder And Decisive Sign

- Classification: exact theorem.
- Result:
  \[
  \mathcal B_{3,n}
  >C_{3,*}n^3+\kappa_*n^2-{\alpha_*+5\over3}n-{1\over15},
  \]
  where
  \[
  \kappa_*
  ={-535396585939+1466777893\sqrt{377823}\over986889256929}
  >{1\over3}.
  \]
  Since \((\alpha_*+5)/3<11/6\), the remainder is positive for every
  \(n\ge6\). Therefore
  \[
  \Lambda_n\ge\mathcal I_{3,n}\ge\mathcal B_{3,n}>C_{3,*}n^3,
  \qquad
  R_2^*(n)>{\mathcal I_{3,n}\over\pi}-n^2
  >{C_{3,*}\over\pi}n^3-n^2
  \quad(n\ge159).
  \]
- Interpretation: the integer closure \(\mathcal I_{3,n}\) is the strongest
  explicit cutoff-only consequence of this rounded bound;
  \(\mathcal B_{3,n}\) is the underlying literal charging expression. No exact
  residual or leading coefficient is inferred.

## EV-05 - Independent Exact Arithmetic

- Classification: verified bounded exact computation.
- Method:
  `python -B ops\TASK-20260716__three_prefix_finite_theorem\exact_diagnostic.py`.
- Result: independently reconstructed optimizer and coefficient; exact scan
  through \(170\); boundary rows \(158,159,170,171\); segment thresholds
  \((171,77,64)\); symbolic upper-clip estimate threshold \(23\); literal,
  integer-closure, polynomial, and bare cubic checks for every
  \(159\le n\le1000\), including
  \(\mathcal B_{3,162}=2374661/2\) and
  \(\mathcal I_{3,162}=1187331\); all checks passed.
- Independence: the script imports no project, production, or test helper.
- Limitation: the bounded scan corroborates the arithmetic but does not replace
  the written charging proof or symbolic tail.

## EV-06 - Failed Checks Preserved

- Classification: verified workflow evidence.
- Result: one scratch prototype raised a transient `TypeError` before the
  pairing-expansion line was corrected; the first format check requested
  mechanical reformatting; and the first monolithic proof patch missed its
  context and made no change. Stable reruns pass. No mathematical assertion,
  theorem comparison, or final-source check failed.

## EV-07 - Final Verification

- Classification: verified computation and source inspection.
- Results: exact diagnostic passed through \(n=1000\); focused selection 12
  passed; fixed-order-cycle-ratio module 101 passed; complete suite 277 passed;
  checked-artifact verification passed 4 certificates and 76 local brackets;
  schema selection passed 4 tests; diagnostic Ruff check and format check
  passed.
- Equation tags: the corrected final audit found 289 unique tags and no
  duplicate.
  An earlier over-escaped pattern found zero tags and was discarded rather
  than misclassified as a pass.
- Source audits: all synchronized theorem values and domains agree; 289 tags
  are unique; delimiter, environment, code-fence, trailing-whitespace,
  protected-path, and changed-path checks pass.
- Independent audits: no mathematical, diagnostic, synchronization, Markdown,
  or scope defect remains after the integer-closure and wording corrections.
- Final state: `git diff --check` and final diff inspection pass; task is
  READY_FOR_REVIEW. Hosted GitHub Actions remain unverified, and the user
  retains all staging and commit authority.

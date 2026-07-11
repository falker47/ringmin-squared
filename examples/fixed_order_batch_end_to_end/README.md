# Fixed-Order Batch End-To-End Example

This example exports two high-precision v1 fixed-order artifacts from explicit
n=3 and n=4 quadratic index orders, then verifies the generated artifact
directory with `power-ringmin-verify-fixed-order-artifacts`.

The result is finite fixed-order numerical evidence only. It is not a global
optimum certificate and does not prove any theorem for all `n`.

## Artifact Status And Local Eta

Generated artifacts from this example record one supplied cyclic order, the
all-pairs fixed-order feasibility check at the exported radius, witness data,
and a local radius bracket when `--local-radius-eta` is used. They are
classified as finite numerical observations unless stronger evidence is added.
They do not certify global optimality over cyclic orders.

For small high-precision examples, choose `--local-radius-eta` as an absolute
radius offset that is much larger than the recorded STN tolerance and decimal
serialization noise, but small relative to the radius scale being reported. A
useful bracket should make the standalone verifier accept `R` and `R + eta`,
and reject `R - eta` when `R > eta`; the batch verifier enforces this when it
uses the artifact-recorded eta. The `1e-12` value below is an illustrative local
bracket for these n=3 and n=4 examples at 80 digits. For new examples, rerun the
verifier after changing eta, and increase `--digits` before tightening eta if
the bracket is unstable.

From the repository root, with the package console scripts available:

```powershell
$output = "C:\tmp\power-ringmin-fixed-order-batch-example"
New-Item -ItemType Directory -Force $output | Out-Null

power-ringmin-export-fixed-order-batch `
  examples/fixed_order_batch_end_to_end/index_orders.json `
  --order-kind index `
  --backend mpmath `
  --digits 80 `
  --local-radius-eta 1e-12 `
  --output-dir $output `
  --created-at-utc 2026-07-11T00:00:00Z `
  --overwrite

power-ringmin-verify-fixed-order-artifacts $output --digits 80
```

The export step should finish with:

```text
batch complete count=2 output_dir=C:\tmp\power-ringmin-fixed-order-batch-example backend=mpmath
```

The verification step should finish with:

```text
batch standalone verification complete count=2 passed=2 failed=0
```

From a source checkout without installed console scripts, set `PYTHONPATH` and
run the same entry points as modules:

```powershell
$env:PYTHONPATH = "src"
$output = "C:\tmp\power-ringmin-fixed-order-batch-example"
New-Item -ItemType Directory -Force $output | Out-Null

python -m power_ringmin.export_fixed_order_batch_cli `
  examples/fixed_order_batch_end_to_end/index_orders.json `
  --order-kind index `
  --backend mpmath `
  --digits 80 `
  --local-radius-eta 1e-12 `
  --output-dir $output `
  --created-at-utc 2026-07-11T00:00:00Z `
  --overwrite

python -m power_ringmin.verify_fixed_order_artifacts_cli $output --digits 80
```

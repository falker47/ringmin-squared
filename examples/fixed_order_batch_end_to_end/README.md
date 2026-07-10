# Fixed-Order Batch End-To-End Example

This example exports two high-precision v1 fixed-order artifacts from explicit
quadratic index orders, then verifies the generated artifact directory with
`power-ringmin-verify-fixed-order-artifacts`.

The result is finite fixed-order numerical evidence only. It is not a global
optimum certificate and does not prove any theorem for all `n`.

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
  --created-at-utc 2026-07-10T00:00:00Z `
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
  --created-at-utc 2026-07-10T00:00:00Z `
  --overwrite

python -m power_ringmin.verify_fixed_order_artifacts_cli $output --digits 80
```

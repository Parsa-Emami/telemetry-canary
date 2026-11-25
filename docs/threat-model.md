# Threat model

**Asset** Integrity of the evidence processed by TelemetryCanary and confidentiality of any input retained by the operator.

| Boundary | Failure mode | Current control |
| --- | --- | --- |
| File to CLI | Oversized, malformed or ambiguous JSON | Size limit, rejects duplicate keys and handles invalid input without echoing raw input |
| Evaluator to report | Identifiers or evidence accidentally disclosed | Use synthetic fixtures, inspect output before sharing and keep results outside Git |
| GitHub Actions | Untrusted contributions or dependency drift | Read-only PR jobs, full-SHA action pins and no mandatory product secrets |
| Build to release | Substituted or incomplete artifacts | SHA-256 manifest, signed provenance and signed SBOM attestations in release workflow |

Run with synthetic data and ordinary user permissions. The prototype assumes the local fixture directory is controlled by its operator. Inputs provide observations and can omit evidence or misstate what happened; validation results do not establish provenance of input records. Real data connectors require a separate boundary review.

[R11 and the release checklist](../ROADMAP.md) track acceptance beyond these controls.

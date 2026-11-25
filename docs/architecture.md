# Architecture

The CLI parses one local JSON document and delegates to a deterministic project-specific evaluator. Findings are serialized as structured JSON on stdout. Exit status allows local scripts and CI to distinguish pass, findings and invalid input.

The repository uses synthetic fixtures at two boundaries. Unit tests call the evaluator, while process tests run the checked-in CLI. No product server or cloud service is required for these paths.

The first integration planned for the product is described in [R07](../ROADMAP.md). Planned stack includes Go, OpenTelemetry Collector and optional Presidio. [ADR 0001](adr/0001-local-evidence.md) records the offline boundary for the proof of concept.

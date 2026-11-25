# TelemetryCanary roadmap

Privacy and platform teams need to verify that telemetry filters prevent configured synthetic identifiers from reaching sinks.

Comparison candidates include OpenTelemetry Collector, Presidio and Gitleaks. Planned product stack includes Go, OpenTelemetry Collector and optional Presidio.

The proof of concept uses Python's standard library and runs locally on synthetic evidence. Validate the engine before investing in a UI. The flagship order is RecoverInvariant, SchemaRehearsal, and AgentActionProof. Advance remaining projects as user discovery and maintenance capacity justify them.

## Research and development

| Phase | Deliverable | State | Acceptance evidence |
| --- | --- | --- | --- |
| R01 | Problem research | Draft | Document baseline workarounds, candidate users and the evidence they need. |
| R02 | Competitive analysis | Planned | Compare one reproducible workflow across the reference tools. Record versions and trade-offs. |
| R03 | User discovery | Planned | Interview three candidate users and validate the proposed workflow and evidence format. |
| R04 | Product specification | Draft | Define the MVP input, output, acceptance fixtures, compatibility and exit behavior. |
| R05 | Architecture | Draft | Review trust boundaries, isolation and failure behavior. Record decisions as ADRs. |
| R06 | Proof of concept | Implemented | Run the local CLI against passing, failing and invalid fixtures. |
| R07 | Core engine | Planned | Send labeled synthetic signals through a local OpenTelemetry Collector. Cover nested attributes and separate log and trace sinks. Retain finding counts and marker positions only and test that fixture values never enter reports. |
| R08 | CLI / API | Partial | Version the fixture and output contracts. Add upgrade and invalid-input coverage. |
| R09 | Web workspace | Planned | Ship a local UI only if pilot feedback shows that it improves the evidence triage workflow. |
| R10 | Integrations | Planned | Add a local adapter around one reference tool with reproducible fixtures and no mandatory paid credentials. |
| R11 | Security hardening | Partial | Run input-boundary tests and security checks. Confirm active main protection and private reporting on GitHub. |
| R12 | Benchmark | Partial | Run the included microbenchmark as a baseline. Add a representative corpus and report median, p95 and machine configuration. |
| R13 | Independent testing | Planned | Have external users repeat the demo and confirm failure evidence from a clean checkout. |
| R14 | Documentation | Partial | Publish setup, architecture, troubleshooting and versioned CLI documentation. Verify the Pages build and links. |
| R15 | Public beta | Planned | Publish an explicitly marked pre-stable release after reviewing CI, SBOM, signing verification and known limitations. |
| R16 | Stable release | Planned | Close acceptance gaps, verify reproducible release artifacts and publish compatibility and maintenance policies. |
| R17 | Community development | Planned | Triage public feedback and publish independently reproducible contribution tasks. |
| R18 | Continuous maintenance | Planned | Review dependencies and CI on a recurring basis. Publish changelogs and document supported versions. |

## Open-source release checklist

| Priority | Requirement | Evidence and remaining work |
| --- | --- | --- |
| P0 | Working software | R06 CLI present; R07 MVP planned |
| P0 | OSI license | LICENSE |
| P0 | Free core and local operation | Standard-library runtime; RULES.md |
| P0 | Installation and English README | README.md |
| P0 | Unit tests | Direct engine assertions in tests/ |
| P0 | Integration tests | CLI with synthetic fixtures; external adapters planned |
| P0 | End-to-end tests | Process-level proof-of-concept checks; product E2E planned |
| P0 | CI/CD | Workflows committed; hosted run and release unverified |
| P0 | Branch protection | Desired ruleset committed; activation requires repository settings |
| P0 | Required checks | CI job names declared in ruleset; enforcement requires activation |
| P0 | Security policy and threat model | SECURITY.md and docs/threat-model.md |
| P0 | Dependency scanning | Stdlib inventory and manifest/action pin guard; lockfile advisory scan required when dependencies land |
| P0 | Secret scanning | Pinned Gitleaks CI and local command in RULES.md; hosted run unverified |
| P1 | Signed artifacts, SBOM and provenance | Draft release workflow and local artifacts; signing and delivery unverified |
| P1 | Reproducible benchmark | Local microbenchmark; representative validation planned |
| P1 | Architecture and ADRs | docs/architecture.md and docs/adr/ |
| P1 | Contribution, conduct and issue/PR templates | Repository templates committed |
| P1 | Documentation site | Static Pages-ready entry point in docs/; hosted publication unverified |
| P1 | Synthetic demo and API documentation | examples/ and docs/cli.md; network API planned only if needed |
| P1 | Changelog, semantic versioning and maintenance | CHANGELOG.md and CONTRIBUTING.md; release pending |

R15 and R16 require a green hosted CI run, active rules, signed-artifact verification, documented installation and a product demo that satisfies R07. Record an evidence link and commit for each completed release gate.

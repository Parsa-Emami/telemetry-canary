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
| R11 | Security hardening | Partial | Run input-boundary tests and security checks. Exercise pull-request protection and extend the model for live integrations. |
| R12 | Benchmark | Partial | Run the included microbenchmark as a baseline. Add a representative corpus and report median, p95 and machine configuration. |
| R13 | Independent testing | Planned | Have external users repeat the demo and confirm failure evidence from a clean checkout. |
| R14 | Documentation | Partial | Publish setup, architecture, troubleshooting and versioned CLI documentation. Extend product documentation as R07 integrations land. |
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
| P0 | CI/CD | [Initial hosted CI passed](https://github.com/Parsa-Emami/telemetry-canary/actions/runs/45611457781); draft-release workflow committed |
| P0 | Branch protection | [Active Protect main ruleset](https://github.com/Parsa-Emami/telemetry-canary/rules/28073889) and .github/rulesets/main.json |
| P0 | Required checks | Local tests and Dependency and secret checks required on main |
| P0 | Security policy and threat model | SECURITY.md and docs/threat-model.md; private vulnerability reporting enabled |
| P0 | Dependency scanning | Stdlib inventory and manifest/action pin guard; lockfile advisory scan required when dependencies land |
| P0 | Secret scanning | Pinned Gitleaks ran successfully in hosted CI; local command in RULES.md |
| P1 | Signed artifacts, SBOM and provenance | Draft release workflow and local artifacts; signing and delivery unverified |
| P1 | Reproducible benchmark | Local microbenchmark; representative validation planned |
| P1 | Architecture and ADRs | docs/architecture.md and docs/adr/ |
| P1 | Contribution, conduct and issue/PR templates | Repository templates committed |
| P1 | Documentation site | [Published documentation](https://parsa-emami.github.io/telemetry-canary/) from main:/docs |
| P1 | Synthetic demo and API documentation | examples/ and docs/cli.md; network API planned only if needed |
| P1 | Changelog, semantic versioning and maintenance | CHANGELOG.md and CONTRIBUTING.md; release pending |

R15 and R16 require a green hosted CI run, active rules, signed-artifact verification, documented installation and a product demo that satisfies R07. Record an evidence link and commit for each completed release gate.

The bootstrap CI run and repository settings above were verified on 2026-11-25.
The [baseline commit](https://github.com/Parsa-Emami/telemetry-canary/commit/cee36eea93098a6a94325fbf62260af6d4385cd8) contains the offline prototype.

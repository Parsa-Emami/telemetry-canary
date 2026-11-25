# Open source engineering rules

1. Keep every mandatory runtime feature self-hostable and usable without account creation, payment, billing-enabled cloud or proprietary APIs. Use local machines, fixtures and community toolchains for required workflows. Document licenses, quotas and substitutes for optional integrations before adoption.
2. Use Apache-2.0 for original project code. Review licenses and notices of fixtures, assets, build tools and transitive packages before incorporating them. Keep employer data, customer information, credentials and identifiable telemetry outside Git, reports and CI artifacts.
3. Use synthetic fixtures and read-only evidence for automated checks. Keep operational integrations opt-in, confined to owned test environments, and governed by a versioned data boundary.
4. Land changes through a pull request after the initial repository bootstrap. Protect `main` against force-push and deletion. Require passing **Local tests** and **Dependency and secret checks**. The solo-maintainer baseline requires zero approvals; stable release requires independent acceptance evidence under R13.
5. Keep workflow actions pinned by full SHA and use read-only workflow tokens by default. Give write permission only to the trusted release job. Review a dependency before adding it and wire in a free lockfile advisory scanner for that ecosystem in the same change.
6. Provide unit and CLI integration tests for behavior changes. Add product-level end-to-end acceptance checks when live integrations land. Report limitations and publish only measured benchmark results.
7. Use semantic versioning and maintain an English changelog. Before publishing a draft release, verify its archive, CycloneDX SBOM, Sigstore build provenance and signed SBOM attestation. Record security support and compatibility.
8. Use GitHub-hosted standard runners on the public repository or run the local fallback. Use GitHub Pages from `main:/docs` for optional publication of the static entry point. Paid features, premium runners, billing-enabled services and paid add-ons are outside the supported baseline.

## Local fallback

Run `python3 -m unittest discover -s tests -v`, `python3 scripts/check_dependencies.py`, and `git diff --check main`. With Go and outbound access to the public module service, run `GOTOOLCHAIN=go1.25.4 go install github.com/zricethezav/gitleaks/v8@v8.30.0` followed by `"$(go env GOPATH)/bin/gitleaks" git --redact --log-opts="--all" .`. Review CI-tool licenses and pins when upgrading them. The scanner and attestation services are release tooling.

## GitHub setup

`.github/rulesets/main.json` is an importable ruleset. Activate it after the first CI run succeeds. The check contexts use the two job names above. Enable private vulnerability reporting, review the resulting rule summary, and verify that a PR with a failing check cannot merge. For documentation, configure Pages to deploy from the `main` branch and `/docs` folder. These repository settings require maintainer access.

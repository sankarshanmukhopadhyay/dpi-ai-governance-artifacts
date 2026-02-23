# Normative language

This repository uses RFC 2119-style keywords to express conformance expectations:

- **MUST / MUST NOT / REQUIRED / SHALL / SHALL NOT**: mandatory requirements.
- **SHOULD / SHOULD NOT / RECOMMENDED**: strong recommendations with explicit rationale when deviating.
- **MAY / OPTIONAL**: permitted options.

Guidelines:

1. **One normative statement per bullet** where possible.
2. Avoid using RFC keywords in purely informative text.
3. Prefer unique identifiers for requirements in controlled docs that are expected to be audited or tested.
4. When a requirement could be machine-testable, express it as:
   - a schema constraint, and/or
   - a test vector, and/or
   - a ruleset (future).

These conventions are inspired by the discipline of ToIP Governance Metamodel policy drafting guidance, adapted to this repository’s artifact-first approach.

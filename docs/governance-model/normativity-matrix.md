# Normativity matrix

This matrix is a quick guide to what is normative.

| Area | Typical files | Normativity |
|---|---|---|
| Governance spine | `governance/primary.md` | Mixed (definitions + process requirements) |
| Controlled documents | `controlled/**` | Normative where stated |
| Schemas | `schemas/**` | Machine-testable constraints |
| Templates | `templates/**` | Informative structure; may embed normative fields |
| Test vectors | `rulebook-test-vectors/**` | Machine-testable examples |
| Playbooks | `playbooks/**` | Informative; may include normative operational commitments |
| Guides | `docs/guides/**` | Informative |

Rule of thumb: if it uses RFC 2119 keywords in uppercase and is intended for conformance, it is normative.

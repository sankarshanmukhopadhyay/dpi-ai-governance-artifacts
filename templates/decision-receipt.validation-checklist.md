# Decision Receipt Validation Checklist

Use this checklist when assessing whether an implementation produces decision receipts that are fit for audit and contestability.

## Structure
- Receipt has a stable `receipt_id` and `issued_at` timestamp
- Receipt identifies an accountable `authority` suitable for lookup in an authority directory
- Receipt identifies the `rulebook_id` and `version` used
- Receipt includes at least one `input_refs` entry
- Receipt includes `outcome` and one or more `reason_codes`

## Cryptographic integrity
- Signature is present and verifiable (`signature.alg`, `signature.kid`, `signature.value`)
- Key identifier resolves to a valid public key in the authority directory
- Signature covers the full receipt payload (excluding transport wrappers)

## Minimization and privacy
- Inputs are referenced by durable pointers or hashes, not raw personal data
- Reason codes do not leak sensitive attributes beyond what is required for remedy
- Evidence pointers are access-controlled and purpose-limited

## Contestability
- Receipt provides an appeals hook when outcomes are consequential
- Reason codes are mapped to a published vocabulary and have remedy guidance
- There is a defined path from receipt to correction and recompute workflows

## Operational readiness
- Receipts are generated deterministically for equivalent inputs and rulebook versions
- Receipts are retained under an explicit retention policy
- Receipt issuance is monitored (error budgets, latency, failed signature rates)

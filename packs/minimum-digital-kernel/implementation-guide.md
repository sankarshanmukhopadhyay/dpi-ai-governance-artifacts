# Minimum Digital Kernel — Implementation Guide

This pack operationalizes the **Minimum Digital Kernel** (MDK): the minimum governance surface area required for legitimate action in AI-enabled DPI systems.

## What you implement

1. **Authority Directory** (who can decide what)
2. **Decision Receipts** (what happened, why, under what authority)
3. **Rulebook Manifest + Change Control** (rules as controlled objects)
4. **Tier Profile** (tier-conditional governance requirements)
5. **Evidence Bundle** (audit-friendly packaging)

## Integration steps (practical)

1. Adopt the schemas in this repo for Authority Directory, Decision Receipt, and Rulebook Manifest.
2. Stand up an Authority Directory register (even a Git repo + JSON store is fine).
3. Emit Decision Receipts for governed decisions (start with high-impact tiers).
4. Put the Rulebook Manifest under change control using the change-control template.
5. Use the evidence bundle guide to package proof for reviews and audits.

## Evidence checklist

Use `artifact-checklist.md` in this pack and the control mappings in `controls-mapping.md` to confirm completeness.

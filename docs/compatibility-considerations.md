
# Compatibility considerations

The new conformance artifacts are designed to sit between the Lab and this repository rather than replace either one.

Compatibility expectations:

- the Lab produces review bundles and evidence logs,
- this repository adds control mappings, declarations, and audit trail expectations,
- downstream adopters can swap pack-level artifacts without rewriting the review method.

This keeps the boundary crisp: method on one side, implementation-ready governance bundles on the other.

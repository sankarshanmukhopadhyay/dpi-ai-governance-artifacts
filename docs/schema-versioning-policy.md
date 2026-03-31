
# Schema versioning policy

New machine-readable artifacts should follow a conservative versioning rule:

- additive, backward-compatible field additions: minor increment,
- required-field additions or semantic breaking changes: major increment,
- typo and documentation-only corrections: patch increment.

Where possible, example instances should be updated in the same change that updates the schema.

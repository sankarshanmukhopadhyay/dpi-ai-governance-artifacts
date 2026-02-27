# Practitioner FAQ

## What is this repo, in one line?
A **portable governance kit**: schemas, templates, controlled docs, and conformance guidance to operationalize risk, redress, transparency, and assurance for AI-enabled systems.

## Is this a policy framework or an engineering toolkit?
Both — intentionally.
- **Controlled docs** express commitments and expectations.
- **Schemas/templates** turn those commitments into operational artifacts.
- **Conformance** provides the proof layer.

## Where should I start?
Start with `docs/guides/how-to-use-this-repo.md` and pick one adoption pathway in `docs/guides/adoption-pathways.md`.

## Do I need to adopt everything?
No. Treat the repo as modular. Start with one workflow end-to-end, then expand.

## What’s the difference between templates and controlled docs?
- **Templates** are editable starting points for teams.
- **Controlled docs** are governance commitments that should change only through explicit review.

## Can we use this without writing software?
Yes. You can start with templates and disciplined document management. Schemas become valuable as you scale or automate.

## How does this relate to audits?
Conformance and evidence bundle guidance are designed to reduce audit friction by making governance artifacts *repeatable and reviewable*.

## How do we avoid this becoming paperwork theater?
Bind artifacts to operational events:
- launches
- incidents
- quarterly reviews
- procurement gates

Evidence should be a byproduct of running the system, not a scramble.

## Does this prescribe specific laws or regulations?
No. It’s a *governance operations layer* that can be mapped to local legal/regulatory requirements.

## How do we contribute changes safely?
- Use pull requests
- Treat `controlled/` changes as higher scrutiny
- Prefer additive schema changes; document breaking changes with migrations

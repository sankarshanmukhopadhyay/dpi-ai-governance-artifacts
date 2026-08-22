---
layout: default
title: Pages rendering
nav_order: 7
---

# Pages rendering

The site uses **Just the Docs on Jekyll 4**, built and deployed through GitHub Actions.

The template is selected for operator utility: persistent hierarchical navigation, full-site search, breadcrumbs, heading anchors, callouts, and Mermaid support are more valuable here than a marketing-oriented landing-page theme.

Pull requests build the site as a validation gate. Pushes to `main` build and deploy the Pages artifact. Dependencies are pinned through `Gemfile` so the repository does not depend on GitHub's limited built-in Jekyll theme set.

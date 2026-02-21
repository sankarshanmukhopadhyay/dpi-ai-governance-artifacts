<!--
SPDX-License-Identifier: CC-BY-SA-4.0
SPDX-FileCopyrightText: 2026 Sankarshan Mukhopadhyay
SPDX-FileContributor: Sankarshan Mukhopadhyay <sankarshan@qbfconsulting.digital>
-->

# DPI–AI Risk Scoring Matrix

Author: Sankarshan Mukhopadhyay  
Author Contact: sankarshan@qbfconsulting.digital  
License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)

---

# Risk-to-Tier-to-Governance Binding Model

## Step 1: Risk Priority Thresholds

* Priority 12–15 → Tier 1 (Advisory with Human Oversight)
* Priority 16–19 → Tier 2 (Conditional Automation)
* Priority ≥ 20  → Tier 3 (High Impact Determination)


## Step 2: Tier-Driven Governance Requirements

| Tier | Risk Level | Mandatory Controls | Governance Escalation |
|------|------------|-------------------|----------------------|
| Tier 0 | Minimal | Logging, traceability | Internal review only |
| Tier 1 | Moderate | Explanation artifacts, override logging | Agency-level oversight |
| Tier 2 | High | Binding safeguards, delegation tokens, audit bundle | Cross-agency reporting |
| Tier 3 | Critical | Human-in-loop confirmation, formal appeals, independent audit | Ecosystem governor review |


# DPI–AI Risk Scoring Matrix

* Scoring:
* Likelihood (L): 1–5
* Impact (I): 1–5
* Priority = L × I

| # | Risk | Failure Mode | L | I | Priority |
|---|------|-------------|---|---|----------|
| 1 | Mandate ambiguity | Agent executes action without legally valid authority chain | 4 | 5 | 20 |
| 2 | Workflow inconsistency | Different ministries implement divergent orchestration logic | 4 | 4 | 16 |
| 3 | Data access overreach | Authorized access expands beyond original purpose | 4 | 5 | 20 |
| 4 | Training data legitimacy gap | Public data reused for training without durable rights basis | 3 | 5 | 15 |
| 5 | AI Block supply-chain compromise | Vendor swap or dependency injection risk | 3 | 5 | 15 |
| 6 | Safeguard bypass | Safeguards exist but are overridden by default | 4 | 5 | 20 |
| 7 | Contestability failure | Citizen cannot meaningfully appeal decision | 4 | 5 | 20 |
| 8 | Identity-authority misbinding | Correct identity, wrong authority assumed | 3 | 5 | 15 |
| 9 | Cross-agency accountability gap | Harm occurs, responsibility diffuses | 4 | 4 | 16 |
|10 | Interoperability lock-in | Nominal standards mask practical vendor lock-in | 3 | 4 | 12 |
|11 | Compute cost escalation | Inference and scaling costs become structural burden | 4 | 3 | 12 |
|12 | DPI maturity mismatch | AI layered onto weak registries and APIs | 4 | 4 | 16 |

# DPI–AI Components and Agentic Control Surface

| Framework Element | What It Represents in Agentic Terms | Primary Risk Surface | Required Control Primitive |
|------------------|---------------------------------------|----------------------|---------------------------|
| AI Blocks | Callable tools the agent can invoke | Tool misuse or substitution | Signed artifacts, allowlists, capability-based access |
| DPI Workflows | Runtime policy orchestration | Policy drift, inconsistent execution | Versioned policies, conformance tests, runtime enforcement |
| Public Agents | Acting interface layer | Authority confusion, social engineering | Identity binding, disclosure, escalation pathways |


# Public-Agent Identity and Accountability Model

| Role | System Actor | Control Domain | Accountability Focus |
|------|--------------|---------------|----------------------|
| Issuer | Credential or entitlement authority | Right-to-act tokens | Correct issuance and revocation semantics |
| Verifier | Service validating claims | Acceptance criteria | False accept/reject, auditability |
| Controller | Ministry or agency | Purpose and workflow intent | Lawful basis, minimization, contestability |
| Governor | Ecosystem oversight body | Participation and certification rules | Conformance enforcement, incident arbitration |
| Beneficiary | Citizen or business | Rights and outcomes | Appeal access, transparency, remedy |

---

## Licensing

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0).

You are free to share and adapt this material provided appropriate attribution is given and derivative works are distributed under the same license.

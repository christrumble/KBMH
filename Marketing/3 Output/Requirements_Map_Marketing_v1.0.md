# Requirements Map - Marketing
**Version**: 1.0  
**Date**: 2025-10-02  
**Process Area**: Marketing

## Change Log
- **Date**: 2025-10-02
- **Version**: 1.0
- **Sources**: Marketing/2 Input/MRK & CRM Outline & Questionnaire; Marketing/2 Input/Transcript MRK&CRM
- **Summary**: Scaffold created; pending REQ extraction from questionnaire responses.

## Implementation Approach Classifications

**ALIGNS**: The way the dealer is executing a business process in their current business system aligns with how they will do it in Orion. It might not be an exact one-to-one alignment, but it doesn't require any customizations for them to do what they are currently doing now in Orion.

**ADAPT**: They do need to modify their business process to use Orion. Adaptation is on a spectrum so it could be major or minor - but still no customization required.

**ACCOMMODATE**: WE will accommodate their business process by customization, personalization, new configuration - something we need to do to accommodate their needs.

## Requirements Map

| ID | Requirement | Type (F/NF) | Functionality | Decision | SolutionDesign? | Approach (ALIGNS/ADAPT/ACCOMMODATE/FUTURE) | Risks |
|----|-------------|-------------|--------------|----------|-----------------|---------------------------------------------|-------|
| REQ-001 | Limit Phase 1 email marketing scope | NF | NetSuite Email Marketing | Minimal config now | No | ALIGNS | Underutilization risk/over-investment risk |
| REQ-002 | Targeted segmentation by role/sector/location | F | CRM Groups/Segments | Needed to enable targeting | No | ADAPT | Data quality dependency |
| REQ-003 | Manage opt-in/unsubscribe and transactional emails | NF | Email Subscription Status | Standard handling | No | ALIGNS | Compliance risk if misused |
| REQ-004 | Curated broker/PM lists for value emails | F | Saved Searches/Lists | Periodic comms | No | ADAPT | List governance risk |
| REQ-005 | Showroom event tracking/invitations | F | Campaign/Event Mgmt | Use if/when needed | No | ALIGNS | Low adoption risk |
| REQ-006 | Marketing visibility into leads/sectors | F | Saved searches/dashboards | Proactive content planning | Yes | ACCOMMODATE | Requires design and access control |
| REQ-008 | Internal vs external project status reports | F | Custom Reports/Dashboards | Publish vs acknowledge date | Yes | ACCOMMODATE | Version control, misuse risk |
| REQ-009 | Customer/project statement grouped by order | F | Custom Statement | Progress billing clarity | Yes | ACCOMMODATE | Client confusion if misaligned |
| REQ-010 | Import/tag Zendesk historical data | NF | Data Import/CSV | Tagging for history | No | ALIGNS | Mapping/duplicate risks |

## Notes
- Link decisions to transcript quotes where possible
- Include references back to questionnaire sections
- Keep one requirement per row; split if multiple decisions/approaches apply
- Use precise definitions above for consistent ALIGNS/ADAPT/ACCOMMODATE classification



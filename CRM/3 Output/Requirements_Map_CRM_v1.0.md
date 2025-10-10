# Requirements Map - CRM
**Version**: 1.0  
**Date**: 2025-10-02  
**Process Area**: CRM

## Change Log
- **Date**: 2025-10-02
- **Version**: 1.0
- **Sources**: Marketing/2 Input/Transcript MRK&CRM
- **Summary**: Scaffold created; pending REQ extraction from CRM questionnaire responses.

## Implementation Approach Classifications

**ALIGNS**: The way the dealer is executing a business process in their current business system aligns with how they will do it in Orion. It might not be an exact one-to-one alignment, but it doesn't require any customizations for them to do what they are currently doing now in Orion.

**ADAPT**: They do need to modify their business process to use Orion. Adaptation is on a spectrum so it could be major or minor - but still no customization required.

**ACCOMMODATE**: WE will accommodate their business process by customization, personalization, new configuration - something we need to do to accommodate their needs.

## Requirements Map

| ID | Requirement | Type (F/NF) | Functionality | Decision | SolutionDesign? | Approach (ALIGNS/ADAPT/ACCOMMODATE/FUTURE) | Risks |
|----|-------------|-------------|--------------|----------|-----------------|---------------------------------------------|-------|
| CRM-REQ-001 | Kanban Boards for opportunity pipeline | F | Orion Boards | Adopt boards for pipeline | No | ALIGNS | Adoption/training |
| CRM-REQ-002 | Restrict opportunity visibility to assigned users | NF | Role/Permission Config | Assigned-only policy | No | ADAPT | Discovery limitations |
| CRM-REQ-003 | Forecast only opportunities at ≥70% probability | NF | Forecast Rules | Inclusion threshold | No | ADAPT | Missed early signals |
| CRM-REQ-004 | Sales Goals dashboard in NetSuite | F | Dashboards/Reports | Replace Excel | Yes | ACCOMMODATE | Data integrity alignment |
| CRM-REQ-005 | Default GP target 22%; customer override | F | Opportunity/Customer Fields | Source & override | No | ADAPT | Misuse/override control |
| CRM-REQ-006 | Mobile Quick Add Lead for reps | F | NetSuite Mobile | Quick capture | No | ALIGNS | Minimal |
| CRM-REQ-007 | Import/tag Zendesk history | NF | Data Import/CSV | Historical tagging | No | ALIGNS | Mapping/duplicates |
| CRM-REQ-008 | Customer Portal for quotes/invoices | F | Customer Center | Basic access | No | ALIGNS | Low adoption |
| CRM-REQ-009 | Commission split support | F | Opportunity/Commission Config | Team splits | Future | FUTURE | Complexity of rules |
| CRM-REQ-010 | CRM KPIs & accuracy/win-loss trend tracking | F | Reports/Dashboards | KPI definitions | No | ADAPT | Data quality |

## Notes
- Link decisions to transcript quotes where possible
- Include references back to questionnaire sections
- Keep one requirement per row; split if multiple decisions/approaches apply
- Use precise definitions above for consistent ALIGNS/ADAPT/ACCOMMODATE classification



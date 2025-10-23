# Requirements Map - Order Management
**Version**: 1.0  
**Date**: 2025-10-16  
**Process Area**: Order Management

## Change Log
- **Date**: 2025-10-23
- **Version**: 1.0 (Pending v1.1 Update)
- **Sources**: Master_Transcript_Order_Management.md (July 2025), GapAnalysis_OrderManagement.md (2025-10-23)
- **Summary**: Initial requirements map created from Order Management discovery questionnaire, capturing 43 requirements across transaction management, approvals, customer PO tracking, tax management, templates, order types, commission, and integrations.
- **Pending Updates**: Gap analysis completed on 2025-10-23 identifying 4 critical gaps requiring follow-up sessions. Requirements map will be updated to v1.1 after completion of Sessions 1-4 (estimated +5-9 new requirements from draft PO workflow, quote versioning, customer hierarchy, SO fields, and e-portal specifications).

## Implementation Approach Classifications

**ALIGNS**: The way the dealer is executing a business process in their current business system aligns with how they will do it in Orion. It might not be an exact one-to-one alignment, but it doesn't require any customizations for them to do what they are currently doing now in Orion.

**ADAPT**: They do need to modify their business process to use Orion. Adaptation is on a spectrum so it could be major or minor - but still no customization required.

**ACCOMMODATE**: WE will accommodate their business process by customization, personalization, new configuration - something we need to do to accommodate their needs.

## Requirements Map

| ID | Requirement | Type | Functionality | Decision | SolutionDesign? | Approach | Risks |
|----|-------------|------|---------------|----------|-----------------|----------|-------|
| REQ-001 | Separate transactions for Opportunity → Proposal → Sales Order workflow | F | NetSuite CRM, Quote/Proposal Management, Sales Orders | Use separate linked transactions vs. single transaction with status changes | No | ADAPT | Change management - team memorizes single order number currently; "Kleenex may be required" |
| REQ-002 | Consistent project numbers across all transactions as primary reference | F | NetSuite Project Records | Project number stays consistent, becomes primary search/reference key | No | ALIGNS | None - standard NetSuite capability |
| REQ-003 | Transaction-specific prefixes: OP/PROP/SO/DPO/VPO/INV | F | NetSuite Transaction Numbering | Team added "P" to proposal for clarity | No | ADAPT | Training required on new numbering; email subject lines need updating |
| REQ-004 | One-click conversion between transaction types with automatic data transfer | F | NetSuite Transaction Conversion | Standard NetSuite one-click conversion capability | No | ALIGNS | None - standard feature |
| REQ-005 | Hyperlinked relationships between all related transactions | F | NetSuite Transaction Linking | Standard hyperlink functionality | No | ALIGNS | None - standard feature |
| REQ-006 | SIF import with 60-column data mapping to Smart Table | F | Orion Smart Table, BOM Import Tool | Import SIF files without data loss or concatenation | No | ALIGNS | None - standard Orion capability |
| REQ-007 | XML import with JSON conversion capability | F | NetSuite Data Import, Custom Conversion | Convert XML to JSON for import; Matt to provide template | Yes | ACCOMMODATE | Template dependency; rarely used feature |
| REQ-008 | Smart Table grouping for PO planning and installation strategies | F | Orion Smart Table | Group quote lines by ship-to, date, floor, vendor, product type, WHIPs | No | ALIGNS | None - standard Orion Smart Table |
| REQ-009 | Create static proposals after all upfront work complete (collapsed workflow) | NF | NetSuite Quote/Proposal | Team philosophy: all work done in Google Docs before proposal | No | ADAPT | Requires change management - team must understand proposal still static |
| REQ-010 | No separate SO approval workflow beyond proposal approval | NF | NetSuite Approval Workflows | "Sales order means donezo" - approval done at proposal stage | No | ADAPT | None - simpler than typical workflow |
| REQ-011 | SuiteTax with automated tax calculation for 48 states | F | SuiteTax | Automatic tax calculation based on ship-to address, nexus management | No | ALIGNS | None - standard SuiteTax |
| REQ-012 | Tax exemption certificate management with expiration tracking and auto-application | F | SuiteTax Certificate Management | Upload certificates, track expiration, automatically apply to future quotes | No | ALIGNS | None - standard SuiteTax feature |
| REQ-013 | Tax override capability for government/direct bill orders | F | SuiteTax Override | Manual tax override for Miller Knoll warehouse tax requirement | No | ALIGNS | Government customer dissatisfaction with incorrect tax approach; reputational risk |
| REQ-014 | Finance charges on/off switch (not actively enforced) | F | NetSuite Finance Charges | "Never actually implemented in 13 years" - deterrent only | No | ALIGNS | None - standard capability, not used |
| REQ-015 | Storage fees always commissionable, billed back to client | F | NetSuite Line Items, Commission | Storage fee lines marked commissionable; add to SO or create separate SO | No | ADAPT | None - clear business rule |
| REQ-016 | Custom transaction/record for customer PO tracking | F | NetSuite Custom Record/Transaction | Track customer PO documents and values | Yes | ACCOMMODATE | Manual data entry required; separate design session needed |
| REQ-017 | Customer PO value tracking aggregated at project level | F | NetSuite Custom Record, Saved Searches | Aggregate PO values across multiple orders on same project | Yes | ACCOMMODATE | Complex scenarios: multiple POs, change orders, PO adjustments |
| REQ-018 | KPI dashboard showing customer PO utilization and remaining balance | F | NetSuite Dashboards, Saved Searches | Display: Total PO value, Amount billed, Remaining balance, Alerts when approaching limit | Yes | ACCOMMODATE | Dashboard design and alert threshold configuration required |
| REQ-019 | Display customer PO number on invoices and proposals | F | NetSuite PDF Templates | Customer PO number field flows from proposal to SO to invoice | No | ALIGNS | None - standard field placement |
| REQ-020 | Orders over $25,000 require Shannon approval | F | NetSuite Business Rule Engine | Automatic routing to Shannon for completeness check | No | ADAPT | Approval time monitoring needed |
| REQ-021 | Missing requirements (deposit/signed proposal/drawings/lookbook) route to Matt | F | NetSuite Business Rule Engine | If ANY of 4 required items missing, route to Matt for exception | No | ADAPT | Requires clear definition of "missing" vs. "pending" |
| REQ-022 | Cumulative erosion over $1,500 requires Matt approval | F | NetSuite Business Rule Engine | Track cumulative erosion; trigger approval at $1,500 threshold | No | ADAPT | Erosion calculation logic must be defined; cumulative tracking |
| REQ-023 | Configure up to 10 approval rules for quotes and sales orders | F | NetSuite Business Rule Engine | Flexible approval rule configuration for current and future needs | Yes | ACCOMMODATE | Rule management and maintenance; approval time monitoring |
| REQ-024 | Approval time tracking and reporting | F | NetSuite Saved Searches, Dashboards | Track approval times (average and individual); dashboard visibility | No | ALIGNS | Risk: "People are slow on approving" - must monitor |
| REQ-025 | Double order detection query (same $ amount in 30 days) | F | NetSuite Saved Search | Flag orders with same dollar amount within 30-day window for manual review | Yes | ACCOMMODATE | False positives possible (legitimate bulk orders, similar projects) |
| REQ-026 | Vendor credit limit warnings at threshold (e.g., 90%) | F | NetSuite Vendor Records, Workflow | Warning at threshold; prevent PO creation if over limit | Yes | ACCOMMODATE | Credit limit maintenance required; vendor notification process |
| REQ-027 | Self-service template management without vendor billable hours | F | NetSuite PDF Composer, Advanced PDF/HTML Templates | Kipp and team can modify templates without GSI involvement | No | ALIGNS | None - standard NetSuite capability; major benefit |
| REQ-028 | Template version control and change documentation process | NF | NetSuite + Process | Document why changing, maintain version history, controlled changes | No | ADAPT | Process adherence required; Kipp to define standards |
| REQ-029 | Recreate all customer-facing templates (proposals, invoices, order confirmations) | F | NetSuite PDF Templates | Kipp's designs to be recreated in NetSuite | Yes | ACCOMMODATE | Template design time; Kipp approval required |
| REQ-030 | Redesign vendor-facing templates (purchase orders) | F | NetSuite PDF Templates | "POs are a shitstorm of information" - better organization needed | Yes | ACCOMMODATE | Template design time; Kipp ownership; vendor feedback |
| REQ-031 | Direct Bill order type configuration (~$1M/year) | F | NetSuite Order Types | Gross up for commission; tracked separately for reporting | No | ALIGNS | Accounting treatment must be configured correctly |
| REQ-032 | Intermarket order type configuration (inbound ~40/yr, outbound thousands) | F | NetSuite Order Types | ServiceTime integration for Shannon's high-volume work | No | ALIGNS | Shannon bottleneck risk with thousands of orders |
| REQ-033 | "Intuit Work from Home" order type for reporting | F | NetSuite Order Types | Rename from "e-commerce"; separate reporting visibility | No | ADAPT | Reporting changes required |
| REQ-034 | Government order type configuration (20% of business) | F | NetSuite Order Types | Special tax handling; significant revenue stream | No | ALIGNS | Tax override complexity (see REQ-013) |
| REQ-035 | Header-level commission assignment with split capability | F | NetSuite Commission | Assign sales person, percentage, split between multiple people | No | ALIGNS | None - standard NetSuite commission |
| REQ-036 | Line-level commissionable flag | F | NetSuite Commission | Mark individual lines as commissionable or not | No | ALIGNS | Clear business rules needed (storage fees, accommodations) |
| REQ-037 | Track both Project GP and Commissionable GP separately | F | NetSuite Saved Searches, Dashboards | Project GP (total) vs. Commissionable GP (subset for commission calc) | No | ALIGNS | Reporting must clearly distinguish the two |
| REQ-038 | 15% labor markup via formula lines | F | NetSuite Formula Lines | Automatic 15% markup calculation on external labor | No | ALIGNS | None - standard formula line capability |
| REQ-039 | Miller Knoll ServiceNet integration with Orion | F | Order Manager Integration, ServiceNet | Link ServiceNet to Orion for intermarket orders | Yes | ALIGNS | Integration technical specifications pending |
| REQ-040 | Evaluate Coupa email parsing automation for order creation | F | Email Parsing, NetSuite Workflow | Parse Coupa emails to create orders automatically; bi-directional invoicing | Yes | ACCOMMODATE | Email format consistency; decision on ROI pending; Shannon's volume justifies |
| REQ-041 | ServiceTime integration for intermarket orders | F | ServiceTime Integration | Maintain current integration for thousands of intermarket orders | No | ALIGNS | Critical for Shannon's workflow |
| REQ-042 | Miller Knoll Quote Tool integration at proposal and PO level | F | Vendor Quote Tool | Price validation; vendor response utility | No | ALIGNS | Standard Orion capability with Miller Knoll |
| REQ-043 | Escalate to Miller Knoll (Dustin) for project-level tiered pricing recognition | NF | External - Miller Knoll Policy | Request project number + contract number acceptance for tiered pricing | N/A | FUTURE | Major business impact if not resolved; split orders lose discounts; affects installation strategy vs. pricing optimization trade-off |

## Notes

### Transaction Structure & Numbering (REQ-001 through REQ-005)
- **Change Management Critical**: "This is like the one thing during discovery that people get tripped up on"
- **Mitigation**: Project number stays consistent; global search; hyperlinked records; recent transactions dialog
- **Training Focus**: Search by project, not order number; email subject lines reference project
- **Timeline**: "Kleenex may be required, but we should be able to wipe our tears pretty quickly"

### Customer PO Tracking (REQ-016, REQ-017, REQ-018)
- **Business Driver**: Bank reporting requirement; payment delay risk mitigation
- **Complexity**: Multiple POs per project; change orders; blanket POs
- **Follow-Up**: Separate design session scheduled
- **Competitive Advantage**: "Anything that we can do to make us look like we're easy to do business with"

### Approval Workflows (REQ-020 through REQ-026)
- **Current Rules Well-Defined**: Clear thresholds and routing
- **Key Approvers**: Shannon ($25K, missing requirements); Matt (missing requirements, erosion)
- **Purpose Beyond Control**: Training opportunity; problem-solving expertise
- **Budget**: Up to 10 rules configured
- **Action Item**: Shannon to document approval workflow flowchart

### Tax Management (REQ-011, REQ-012, REQ-013)
- **Government Orders**: 20% of business
- **Miller Knoll Policy Conflict**: Warehouse tax vs. final destination tax
- **Pain Point**: "Every tax person we've ever talked to in the entire 80 years of our existence in business, we have taxed to final destination"
- **Reputational Risk**: "Government frustrated with KBM Hoag but 'we have no control over anything'"
- **Volume**: ~$1M direct bill annually (1% of revenue)

### Template Management (REQ-027 through REQ-030)
- **Major Benefit**: Self-service eliminates vendor billable hours
- **Kipp Ownership**: Strong design owner; pride in 5-year-old templates
- **Current Pain**: "That's insane" - paying for simple changes
- **Vendor POs**: "Shitstorm of information" - redesign opportunity
- **Action Items**: Kipp to provide all templates; GSI to recreate

### Order Types & Volume (REQ-031 through REQ-034)
- **Intermarket Outbound**: Thousands annually; Shannon's primary workload (8-10/day)
- **Government**: 20% of business
- **Direct Bill**: ~$1M annually (1% of revenue)
- **Intermarket Pain Point**: Setting up dealers as both vendor AND customer first time

### Integrations (REQ-039 through REQ-042)
- **ServiceNet**: Confirmed integration plan
- **ServiceTime**: Critical for Shannon's thousands of intermarket orders
- **Coupa**: Optional automation; Shannon's volume may justify
- **Quote Tool**: Standard Miller Knoll integration

### Tiered Pricing Challenge (REQ-043)
- **Major Business Issue**: Installation strategy conflicts with pricing optimization
- **Current Problem**: Split POs lose tiered discounts despite qualifying at project level
- **Impact**: GP erosion on large multi-order projects
- **Solution Path**: Escalation to Dustin (Miller Knoll product owner)
- **Industry Impact**: "Other manufacturers and dealers that have the same challenge"
- **Status**: FUTURE - pending Miller Knoll decision

## Traceability Matrix

All requirements traced to:
- **Questionnaire Sections**: Each REQ-### appears in questionnaire with full context, evidence, user stories
- **Transcript Quotes**: Direct quotes support each decision and requirement
- **Stakeholders**: Primary users, approvers, and impacted parties identified
- **Confidence Ratings**: 80%+ confidence on all requirements except those marked for further investigation

## Risk Summary

**High Risk:**
- REQ-043: Tiered pricing - significant GP impact if not resolved
- REQ-032: Intermarket volume - Shannon bottleneck if not streamlined
- REQ-016/017/018: Customer PO tracking - bank requirement; payment delays if not implemented

**Medium Risk:**
- REQ-001: Transaction number change management - user adoption challenge
- REQ-013: Tax override - government customer dissatisfaction (existing, not new)
- REQ-023: Approval rules - risk of slow approvals if not monitored

**Low Risk:**
- Most ALIGNS requirements - standard NetSuite capabilities
- REQ-027: Template self-service - high value, low risk

## Action Items from Requirements

1. **Shannon**: Document approval workflow flowchart (REQ-020, 021, 022)
2. **Kipp**: Provide all templates for recreation (REQ-029, 030)
3. **Matt**: Provide XML import template example (REQ-007)
4. **Team**: Provide complete order type list (REQ-031-034)
5. **Marcus/Team**: Schedule customer PO tracking design session (REQ-016, 017, 018)
6. **Marcus/Team**: Follow up with Dustin on tiered pricing (REQ-043)

## Follow-Up Sessions Required

1. **Customer PO Tracking Solution Design** - Detailed workflow and field design (REQ-016, 017, 018)
2. **Draft PO Concept & Vendor PO Management** - Session ended before completion
3. **Template Design Review & Approval** - Kipp to approve recreated templates (REQ-029, 030)
4. **E-Portals Discussion** - Coupa and other portal requirements (REQ-040)

**See GapAnalysis_OrderManagement.md for detailed session plans, pre-work requirements, and expected outcomes.**

---

## Gap Analysis Reference

**Completeness Assessment** (as of 2025-10-23):
- **Overall Completeness**: 84% of questions fully answered (21 of 25 questions)
- **Requirements Coverage**: 43 requirements mapped, estimated +5-9 additional requirements from follow-up sessions
- **Critical Gaps Identified**: 4 (Draft PO workflow, Customer PO tracking design, E-portals/Coupa integration, Complete order type list)
- **Follow-Up Sessions**: 4 targeted sessions (6.5 hours total)
- **Timeline to 100% Complete**: 3-4 weeks

**Next Version**: v1.1 will incorporate all findings from the 4 follow-up sessions and add newly identified requirements. Expected completion: November 20, 2025.

For complete gap analysis including:
- Comprehensive question status matrix
- Information gaps analysis with priorities
- Stakeholder engagement assessment
- Detailed session plans with agendas and pre-work
- Consultant action plan with timelines
- Success metrics and completion targets

**Reference Document**: `Order Management/3 Output/GapAnalysis_OrderManagement.md`

---

**Requirements Map Version 1.0 Complete**

*This requirements map will be updated to v1.1 as additional discovery sessions occur and requirements are refined during the design phase.*







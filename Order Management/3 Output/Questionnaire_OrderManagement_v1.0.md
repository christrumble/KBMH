# Questionnaire - Order Management
**Version**: 1.0  
**Date**: 2025-10-16  
**Process Area**: Order Management

## Change Log
- **Date**: 2025-10-16
- **Version**: 1.0
- **Sources**: Master_Transcript_Order_Management.md (July 2025)
- **Summary**: Initial discovery questionnaire created from Order Management workshop transcripts covering transaction structure, quote/proposal management, sales orders, customer PO tracking, approval workflows, tiered pricing challenges, tax management, and template ownership.

## PROCESSED FILES
- Order Management/2 Input/Master_Transcript_Order_Management.md
  - 07-30 Meeting: NetSuite Workflow & Transaction Management.txt (July 30, 2025)
  - Relevant portions from Marketing.txt and 07-29 Business Process Review

## Decision Log

### Transaction Structure & Numbering Decisions
- **REQ-001**: Use separate transactions for Opportunity → Proposal → Sales Order workflow (ADAPT) - "This is like the one thing during discovery that people get tripped up on"
- **REQ-002**: Implement consistent project numbers across all transactions as primary reference (ALIGNS) - "Project number stays consistent... Always one click away from the project record"
- **REQ-003**: Use transaction-specific prefixes: OP/PROP/SO/DPO/VPO/INV (ADAPT) - "Team decided to add 'P' for clarity" for proposals
- **REQ-004**: Enable one-click conversion between transaction types (ALIGNS) - "One-click conversion between transaction types. Automatic data transfer"
- **REQ-005**: Maintain hyperlinked relationships between all related transactions (ALIGNS) - "Hyperlinks between all related records"

### Quote/Proposal Management Decisions
- **REQ-006**: Support SIF import with 60-column data mapping (ALIGNS) - "60 columns of data imported. Smart table display with quick views"
- **REQ-007**: Implement XML import with JSON conversion capability (ACCOMMODATE) - "Convert any format to JSON. Need example template from Matt"
- **REQ-008**: Enable Smart Table grouping for PO planning strategies (ALIGNS) - "Group items by how POs should be split. Installation strategy drives grouping"
- **REQ-009**: Create static proposals after all upfront work complete (ADAPT) - "By the time we get to quote, it's dead at that point. Where it's static"
- **REQ-010**: No separate SO approval workflow needed beyond proposal approval (ADAPT) - "By the time it gets there, we've already done all the other stuff, like the spec check"

### Customer & Tax Management Decisions
- **REQ-011**: Implement SuiteTax with automated tax calculation for 48 states (ALIGNS) - "Automatic tax calculation based on ship-to address"
- **REQ-012**: Enable tax exemption certificate management with expiration tracking (ALIGNS) - "Dashboard shows expiring certificates. Automatic application on future quotes"
- **REQ-013**: Support tax override capability for government/direct bill orders (ALIGNS) - "Tax override capability available. Not elegant but workable"
- **REQ-014**: Finance charges on/off switch but not actively enforced (ALIGNS) - "Never actually implemented in 13 years... Most dealers want to threaten"
- **REQ-015**: Storage fees always commissionable, billed back to client (ADAPT) - "Always commissionable per team"

### Customer PO Tracking Solution
- **REQ-016**: Create custom transaction/record for customer PO tracking (ACCOMMODATE) - "Custom record/transaction for PO tracking. Attach customer PO document"
- **REQ-017**: Enable customer PO value tracking aggregated at project level (ACCOMMODATE) - "Track PO value. Aggregate at project level"
- **REQ-018**: Build KPI dashboard showing PO utilization and remaining balance (ACCOMMODATE) - "Total PO value, Amount billed to date, Remaining balance, Alert when approaching limit"
- **REQ-019**: Display customer PO number on invoices and proposals (ALIGNS) - "Customer PO number appears on invoice... Shows on invoice"

### Approval Workflow Decisions
- **REQ-020**: Orders over $25,000 require Shannon approval (ADAPT) - "Shannon verifies completeness"
- **REQ-021**: Missing requirements (deposit/signed proposal/drawings/lookbook) route to Matt (ADAPT) - "If ANY missing → goes to Matt for approval"
- **REQ-022**: Cumulative erosion over $1,500 requires Matt email approval (ADAPT) - "$500 erosion + $1,000 more = $1,500 triggers"
- **REQ-023**: Configure up to 10 approval rules for quotes and sales orders (ACCOMMODATE) - "Budget for up to 10 approval rules"
- **REQ-024**: Enable approval time tracking and reporting (ALIGNS) - "Report on approval times (average, individual)"
- **REQ-025**: Implement double order detection query (same $ in 30 days) (ACCOMMODATE) - "Query: Same total dollar amount within past 30 days. Flag for manual review"
- **REQ-026**: Configure vendor credit limit warnings at threshold (ACCOMMODATE) - "Warning threshold (e.g., 90% of limit). Prevent PO creation if over limit"

### Template & Document Management Decisions
- **REQ-027**: Enable self-service template management without vendor billable hours (ALIGNS) - "You can do it yourself. No vendor billable hours for changes"
- **REQ-028**: Implement version control and change documentation for templates (ADAPT) - "Communication record of changes. Document why changing. Version history"
- **REQ-029**: Recreate all customer-facing templates (proposals, invoices, order confirmations) (ACCOMMODATE) - "Provide ALL templates (customer and vendor-facing)"
- **REQ-030**: Redesign vendor-facing templates (purchase orders) (ACCOMMODATE) - "I would like to reevaluate the design of vendor facing... Our current POs are a shitstorm of information"

### Order Types & Special Billing
- **REQ-031**: Configure Direct Bill order type (~$1M annually, 1% revenue) (ALIGNS) - "Gross up for commission. Full sales amount to Miller Knoll. Commission kicked back"
- **REQ-032**: Configure Intermarket order types (Inbound ~40/yr, Outbound thousands) (ALIGNS) - "Shannon handles for all Intuit work-from-home... thousands of transactions"
- **REQ-033**: Create "Intuit Work from Home" order type for reporting (ADAPT) - "Want separate order type for reporting. Currently 'e-commerce' in Core"
- **REQ-034**: Configure Government order type (20% of business) (ALIGNS) - "20% of business. Special tax handling"

### Commission Management
- **REQ-035**: Support header-level commission assignment with split capability (ALIGNS) - "Who gets commission (sales person). Percentage (100% or split)"
- **REQ-036**: Enable line-level commissionable flag (ALIGNS) - "Mark individual lines as commissionable or not"
- **REQ-037**: Track both Project GP and Commissionable GP separately (ALIGNS) - "Project GP: Total gross profit. Commissionable GP: Subset used for commission calculation"
- **REQ-038**: Apply 15% labor markup via formula lines (ALIGNS) - "External labor marked up 15%. Formula-based calculation"

### Integrations
- **REQ-039**: Integrate Miller Knoll ServiceNet with Orion (ALIGNS) - "Did you talk about Miller linking ServiceNet into Orion at some point? Yes. Yep. Absolutely"
- **REQ-040**: Evaluate Coupa email parsing automation for order creation (ACCOMMODATE) - "Email parsing to create orders. Automated processing. Bi-directional: Invoice back to Coupa portal"
- **REQ-041**: Maintain ServiceTime integration for intermarket orders (ALIGNS) - "All through ServiceTime integration"
- **REQ-042**: Support Miller Knoll Quote Tool integration at proposal level (ALIGNS) - "Price validation. Vendor response utility"

### Tiered Pricing Challenge (Pending Resolution)
- **REQ-043**: Escalate to Miller Knoll (Dustin) for project-level tiered pricing recognition (FUTURE) - "We're gonna talk to Dustin about this... Should accept that project number along with the contract number"

## Action Items

ACTION: Provide complete list of order types with descriptions  
ASSIGNED TO: Team (Matt, Shannon, Kipp mentioned)  
DUE: Early implementation phase  
RELATED TO: REQ-031, REQ-032, REQ-033, REQ-034

ACTION: Provide all current templates (customer and vendor-facing)  
ASSIGNED TO: Kipp  
DUE: Early implementation phase  
RELATED TO: REQ-029, REQ-030

ACTION: Provide XML import template example  
ASSIGNED TO: Matt  
DUE: Early implementation phase  
RELATED TO: REQ-007

ACTION: Document current approval workflow flowchart  
ASSIGNED TO: Shannon  
DUE: Early implementation phase  
RELATED TO: REQ-020, REQ-021, REQ-022

ACTION: Schedule separate working session for customer PO tracking solution design  
ASSIGNED TO: Marcus/GSI Team with KBM Hoag stakeholders  
DUE: During implementation phase  
RELATED TO: REQ-016, REQ-017, REQ-018

ACTION: Follow up with Dustin (Miller Knoll product owner) on tiered pricing project-level recognition  
ASSIGNED TO: Marcus/Team  
DUE: Before design phase  
RELATED TO: REQ-043

ACTION: Define transaction numbering formats and starting sequences  
ASSIGNED TO: TBD - Suggest: IT Admin with Process Owners  
DUE: Pre-configuration phase  
RELATED TO: REQ-003

ACTION: Define vendor credit limits and warning thresholds  
ASSIGNED TO: TBD - Suggest: Finance/AP Team  
DUE: Before go-live  
RELATED TO: REQ-026

ACTION: Define double order detection parameters and alert recipients  
ASSIGNED TO: Shannon with Operations/Finance  
DUE: Before go-live  
RELATED TO: REQ-025

ACTION: Gather current Google Docs budget templates for reference  
ASSIGNED TO: TBD - Suggest: Sales/Project Coordinators  
DUE: Early implementation phase  
RELATED TO: Current state documentation

## Additional Sessions Needed

### Session: Customer PO Tracking Solution Design
- **Participants Needed**: Matt, Shannon, Marcus (GSI), Finance Lead, potential bank liaison
- **Questions to Address**: 
  • Exact field structure for PO tracking record?
  • Custom transaction or custom record approach?
  • Workflow for manual PO updates?
  • Dashboard KPIs and alert thresholds?
  • How to handle change orders and PO adjustments?
  • Multiple PO scenarios per project?
  • Reporting requirements for bank?
- **Priority**: High
- **Suggested Duration**: 2 hours
- **Dependencies**: REQ-016, REQ-017, REQ-018
- **Evidence**: "Action Item: Separate working session to design PO tracking solution"

### Session: Draft Purchase Order & Vendor PO Management
- **Participants Needed**: Kipp, Shannon, Operations team, Marcus (GSI)
- **Questions to Address**: 
  • What is the draft PO concept and workflow?
  • How should PO information be better organized?
  • What specific improvements needed to current PO format?
  • PO splitting strategies by installation plan?
  • Pre-sold inventory vs ship-to-site PO differences?
- **Priority**: High
- **Suggested Duration**: 2 hours
- **Dependencies**: Transaction management, installation strategy
- **Evidence**: "Here's some big ideas I'm going to introduce. The first one is the concept of the draft PO... Our current POs are a shitstorm of information. I'd like them to be more organized"

### Session: Template Design Review & Approval
- **Participants Needed**: Kipp (design owner), Marcus (GSI), customer-facing teams
- **Questions to Address**: 
  • Review all recreated templates (customer and vendor-facing)?
  • Approve designs and layouts?
  • Define template change control process?
  • Who can authorize template changes post go-live?
  • Version control standards?
- **Priority**: Medium
- **Suggested Duration**: 1.5 hours
- **Dependencies**: REQ-027, REQ-028, REQ-029, REQ-030
- **Evidence**: "Kipp to provide ALL templates (customer and vendor-facing)" and "Communication record of changes. Version history"

### Session: E-Portals Discussion (Deferred Topic)
- **Participants Needed**: Shannon, Marcus (GSI), IT Lead
- **Questions to Address**: 
  • What are the e-portal requirements?
  • Coupa portal integration specifics?
  • Other portal needs?
  • Email parsing automation scope?
- **Priority**: Medium
- **Suggested Duration**: 1 hour
- **Dependencies**: REQ-040
- **Evidence**: "That's what I was going to talk about later today as well, our e-portals"

## New Questions Identified

### Proposed New Question: How do you handle spec creation and catalog management?
- **Asked By**: Kipp and team discussion
- **Context**: Current Core system has catalogs loaded; can search part numbers and build specs. NetSuite/Orion doesn't have this capability currently
- **Suggested Placement**: Quote Management section
- **Evidence**: "All the catalogs are there, so I can go search a part number and then I can pick all the options... Old timers use Core to write our specs"

### Proposed New Question: What is your upfront budgeting and specification workflow before creating quotes?
- **Asked By**: Marcus and team discussion
- **Context**: Team uses Google Docs for live collaborative budgeting before creating static proposals
- **Suggested Placement**: Quote Management section
- **Evidence**: "We really live in a world of collapsed. So part of us using Google Docs, it's like we have a shared budget that we're working through"

---

## QUESTIONNAIRE RESPONSES

### SECTION A: CURRENT STATE ASSESSMENT

#### Customer Management

### i. How do you currently manage customer records and configuration?

**Answer:**
KBM Hoag currently manages customer records in their Core system. Key aspects include:

- **Tax Management**: Currently registered in 48 states for nexus. Tax exemption certificates are tracked, though the system is manual
- **Customer PO Tracking**: Currently no systematic way to track customer PO values against amount billed. This creates risk of exceeding PO limits and payment delays
- **Government Customers**: 20% of business. Require special tax handling due to Miller Knoll direct bill requirements
- **Bank Reporting**: Bank has requested visibility into total project value, POs against project, and open balances - currently unable to provide this data

**Custom Data Fields Critical:**
- Customer PO numbers and values (not currently tracked systematically)
- Tax exemption status and certificate expiration dates
- Government vs. commercial customer designation
- Direct bill customer flagging

**Different Customer Types:**
- Government customers (20% of business) with special tax requirements
- Direct bill customers (~$1M annually, 1% of revenue)
- Intermarket dealers (both inbound and outbound)
- Standard commercial customers

**User Stories:**
- As a Finance Manager, I need to track customer PO utilization so that I avoid exceeding PO limits and payment delays
- As a Tax Manager, I need to track tax exemption certificates with expiration dates so that I can maintain compliance and renew certificates proactively
- As a CFO, I need to provide bank reporting on project values and PO status so that I can meet lending requirements

**Current State Process:**
**PROCESS**: Customer PO Management  
**TRIGGER**: Client provides purchase order  
**STEPS**:
1. Sales/PM receives customer PO → enters PO number manually on order
2. No tracking of PO value vs. billed amount → risk of exceeding
3. Discovery of PO exhaustion → at time of invoice rejection
4. Payment delay → scramble to resolve with customer

**SYSTEMS INVOLVED**: Core (limited PO number field only), Email, Manual tracking  
**PAIN POINTS**: 
- No visibility to when approaching PO limit
- Risk of exceeding PO value
- Payment delays when PO exceeded
- Cannot provide bank reporting on PO status
- Blanket POs with no running balance tracking

**BRD Requirements:**
- [REQUIREMENT] Customer PO tracking with value and utilization monitoring (ID: REQ-016, REQ-017, REQ-018, Type: Functional)
- [REQUIREMENT] Tax exemption certificate management with expiration tracking (ID: REQ-012, Type: Functional)
- [REQUIREMENT] Customer type configuration for government/direct bill/intermarket (ID: REQ-034, Type: Functional)
- [PRIORITY] Must-Have - Customer PO tracking for bank requirements and payment risk mitigation
- [CONSTRAINT] Manual data entry required - team willing to manage PO updates

**Stakeholder Impact:**
- **Primary Users**: Finance team, Shannon (Project Coordinator Manager), Project Coordinators
- **Secondary Users**: Sales team, Matt (executive approval)
- **Approvers**: Bank (external stakeholder requiring reporting)
- **Impacted Parties**: Customers (better PO management), Accounting/AR

**Evidence:**
- "Blanket POs received frequently. No way to track PO value vs. amount billed" - Transcript
- "That's something we just talked about that our bank has asked us" - Regarding project value and PO reporting
- "Then client says 'we can't pay this' → payment delays" - Pain point when POs exceeded
- "20% of business" - Government customer volume

**Confidence Rating**: 95% - Direct quotes with extensive context from transcript covering current state, pain points, and requirements

**Outstanding Items:**
- Specific fields needed on customer record beyond standard NetSuite fields
- Customer hierarchy requirements (parent-child relationships) not discussed in detail
- Credit limit tracking requirements

---

### ii. How do you handle customer deposit requirements and terms setup?

**Answer:**
The transcript indicates deposits are part of the approval requirements but does not provide extensive detail on deposit management processes.

**Deposit Requirements:**
- Signed proposal required
- Deposit required (amount/percentage not specified in transcript)
- Part of Shannon's $25K+ order approval check
- Missing deposit triggers routing to Matt for approval

**Payment Terms:**
- Customer-specific payment terms exist but details not discussed
- Finance charges available as deterrent but "never actually implemented in 13 years" per Lorraine
- Finance charge functionality: "Global on/off switch. Deterrent/threat mechanism"

**User Stories:**
- As a Project Coordinator, I need to verify deposit received before booking order so that orders meet company policy requirements
- As a Finance Manager, I need to track which customers have paid deposits so that I can manage cash flow

**BRD Requirements:**
- [REQUIREMENT] Deposit tracking from quote through sales order (ID: TBD, Type: Functional)
- [REQUIREMENT] Approval workflow triggered by missing deposit (ID: REQ-021, Type: Functional)
- [REQUIREMENT] Finance charge capability (on/off switch, not actively enforced) (ID: REQ-014, Type: Functional)
- [PRIORITY] Must-Have - Deposit verification in approval workflow

**Stakeholder Impact:**
- **Primary Users**: Shannon (Project Coordinator Manager), Finance team
- **Approvers**: Matt (when deposit missing)

**Evidence:**
- "Must have ALL of: Deposit, Signed proposal, Signed drawings, Signed lookbook. If ANY missing → goes to Matt for approval"
- "Never actually implemented in 13 years... Most dealers want to threaten. They don't actually follow through" - Lorraine on finance charges
- "90-day old invoice would automatically add finance charge line. Can be manually added as line item if needed"

**Confidence Rating**: 80% - Limited evidence on deposit management details beyond approval workflow requirements. More investigation needed on:
- Deposit percentages or amounts (standard vs. custom)
- Deposit application process
- Proforma invoice process
- Milestone-based deposit/invoicing scenarios

**Outstanding Items:**
- Standard deposit percentages or amounts
- Process for applying deposits to final invoices
- Proforma invoice requirements
- Milestone-based payment requirements
- Customer-specific deposit terms

---

### iii. What customer-specific approval requirements do you have?

**Answer:**
KBM Hoag has specific, well-defined approval workflows with clear thresholds and rules:

**Current Approval Rules:**

**Rule 1: Orders Over $25,000**
- Goes to Shannon (Project Coordinator Manager) for completeness approval
- Shannon verifies all requirements met
- Designed to prevent double orders (biggest financial losses)

**Rule 2: Missing Requirements Check**
- Must have ALL of: Deposit, Signed proposal, Signed drawings, Signed lookbook
- If ANY missing → routes to Matt for approval
- Team "do all day unabashedly, could care less" about missing requirements
- Matt is "so good and quick about responding"
- Mark is backup for Matt

**Rule 3: Cumulative Erosion Over $1,500**
- Example: $500 erosion + $1,000 more = $1,500 cumulative triggers approval
- Email approval from Matt required
- "Sounds like a lot, but it's not that much"

**Purpose of Erosion Approval:**
- Training opportunity for new team members who made mistakes
- Problem-solving with experienced leadership
- Finding cheaper solutions (Matt's crane story: $10K crane vs. $1.2K elevator technician solution)
- "If we're going to spend the money, let's spend it this way"

**Process:**
- "Usually make the PCs do it" (Project Coordinators submit requests)
- Matt very accessible and responsive
- Not punitive - focused on training and problem-solving

**No Credit Limits Mentioned:**
- No discussion of customer credit limit approvals
- No pre-approved limit arrangements discussed

**User Stories:**
- As a Project Coordinator Manager - Shannon, I need to review all orders over $25K so that I can catch double orders and verify completeness
- As an Executive - Matt, I need to approve orders with missing requirements or significant erosion so that I can maintain quality control and provide problem-solving expertise
- As a Project Coordinator, I need clear approval routing rules so that I know when to escalate orders for approval

**Current State Process:**
**PROCESS**: Order Approval Workflow  
**TRIGGER**: Order ready for booking  
**STEPS**:
1. PC creates order → System checks if over $25K → Yes: routes to Shannon
2. Shannon reviews completeness → checks for deposit, signed proposal, drawings, lookbook
3. If anything missing → routes to Matt for exception approval
4. System checks cumulative erosion → if over $1,500 → routes to Matt
5. Matt reviews and approves/rejects → provides problem-solving guidance if needed
6. Approved order → proceeds to booking

**SYSTEMS INVOLVED**: Core (manual approval tracking), Email notifications  
**PAIN POINTS**: 
- Manual approval tracking
- Need for automated routing based on rules
- Approval time visibility needed for management

**BRD Requirements:**
- [REQUIREMENT] Order over $25K approval workflow to Shannon (ID: REQ-020, Type: Functional)
- [REQUIREMENT] Missing requirements approval workflow to Matt (ID: REQ-021, Type: Functional)
- [REQUIREMENT] Cumulative erosion over $1,500 approval workflow to Matt (ID: REQ-022, Type: Functional)
- [REQUIREMENT] Configure up to 10 approval rules with flexibility (ID: REQ-023, Type: Functional)
- [REQUIREMENT] Approval time tracking and reporting (ID: REQ-024, Type: Functional)
- [REQUIREMENT] Approval dashboard for pending approvals (ID: REQ-024, Type: Functional)
- [FUNCTIONALITY] NetSuite Business Rule Engine
- [SOLUTIONDESIGN] Yes - Custom approval rule configuration
- [PRIORITY] Must-Have - Core business process controls
- [RISK] "Unintended consequence: People are slow on approving" - Need to monitor approval times

**Stakeholder Impact:**
- **Primary Users**: Shannon (Project Coordinator Manager), Matt (Executive), Mark (backup approver), Project Coordinators
- **Approvers**: Shannon ($25K threshold), Matt (missing requirements and erosion)
- **Impacted Parties**: Sales team, Operations team (delayed orders if approvals slow)

**Evidence:**
- "Orders Over $25,000 goes to Shannon (Project Coordinator Manager) for approval. Shannon verifies completeness"
- "Must have ALL of: Deposit, Signed proposal, Signed drawings, Signed lookbook. If ANY missing → goes to Matt for approval"
- "Erosion > $1,500 Cumulative. Example: $500 erosion + $1,000 more = $1,500 triggers. Email approval from Matt required"
- "Matt's Erosion Story: Clay (dramatic employee) runs in: 'We need to rent a crane!' ... Matt's solution: Float table on top of elevator with technician on-site. Cost: $1,200" vs. crane at $6K-$10K
- "If we're going to spend the money, let's spend it this way"
- "Budget for up to 10 approval rules. Should cover quotes and sales orders"

**Confidence Rating**: 98% - Extensive direct quotes with specific details, dollar thresholds, named individuals, and even story examples

**Outstanding Items:**
- Formal approval workflow flowchart (Shannon to provide)
- Backup approver designation beyond Mark
- Approval SLAs or expected response times
- Holiday/vacation approval coverage process

---

### iv. How do you manage customer compliance and tax configuration?

**Answer:**
KBM Hoag has complex tax management requirements spanning 48 states with particular challenges around government orders and Miller Knoll direct bill requirements.

**Tax Management - SuiteTax:**

**Automated Capabilities:**
- Registered in 48 states (nexus)
- Automatic tax calculation based on ship-to address
- Tax exemption certificate management:
  - Upload certificates with effective dates
  - Dashboard shows expiring certificates
  - Automatic application on future quotes for that customer
  - No manual selection needed
- Tax compliance reporting: "You get a beautiful report"

**Government Orders - Tax Complexity (Major Pain Point):**

**The Challenge:**
- Miller Knoll direct bill orders: Client pays Miller Knoll directly for product
- KBM Hoag issues proposal but doesn't collect payment on product
- **Miller Knoll policy**: Tax to warehouse (where shipped), not final destination
- **Standard tax practice**: Tax to final destination
- Conflict: "Every tax person we've ever talked to in the entire 80 years of our existence in business, we have taxed to final destination"
- Miller Knoll's perspective: "Miller Knoll insists, because you know they're the experts on selling to clients, not the hundreds of dealers that do this every day" (sarcastic tone)

**Current Core Workaround:**
1. Change ship-to address in Core to warehouse
2. Get tax calculation
3. Get tax number
4. Change address back
5. Do tax override
6. "It's a pain in the butt"

**NetSuite Solution:**
- Tax override capability available
- "Not elegant" but workable
- Manual process still required
- Warehouse tax percentage always higher than final destination
- Government frustrated with KBM Hoag but "we have no control over anything"

**Direct Bill Volume:**
- ~$1M annually
- 1% of $100M total revenue
- Gross up for commission (full sales amount to Miller Knoll, commission kicked back)

**Multi-State Requirements:**
- 48-state nexus registration
- Automated tax calculation by jurisdiction
- Certificate management across all states

**User Stories:**
- As a Tax Manager, I need automated tax calculation across 48 states so that I ensure compliance without manual lookups
- As a Project Coordinator, I need tax exemption certificates to automatically apply so that I don't have to remember which customers are exempt
- As a Finance Manager, I need tax exemption certificate expiration tracking so that I can proactively request renewals
- As an Order Manager, I need tax override capability for government orders so that I can accommodate Miller Knoll's warehouse tax requirement

**Current State Process:**
**PROCESS**: Government Order Tax Calculation  
**TRIGGER**: Government order with Miller Knoll direct bill  
**STEPS**:
1. Create proposal in Core → needs tax calculation
2. Change ship-to address to warehouse → temporary change
3. System calculates warehouse tax → capture tax amount and tax number
4. Change ship-to address back to final destination → restore correct address
5. Override tax with warehouse calculation → manual override
6. Complete proposal → with incorrect (per standard practice) but Miller Knoll-required tax

**SYSTEMS INVOLVED**: Core, Miller Knoll systems  
**PAIN POINTS**: 
- Manual address changing and override process
- Time-consuming workaround
- Government customer frustration with incorrect tax approach
- KBM Hoag has no control over Miller Knoll policy
- Higher tax burden on government customers due to warehouse rates

**BRD Requirements:**
- [REQUIREMENT] SuiteTax implementation with 48-state nexus configuration (ID: REQ-011, Type: Functional)
- [REQUIREMENT] Tax exemption certificate management with document upload and expiration tracking (ID: REQ-012, Type: Functional)
- [REQUIREMENT] Automated tax certificate application on future quotes (ID: REQ-012, Type: Functional)
- [REQUIREMENT] Tax override capability for government/direct bill scenarios (ID: REQ-013, Type: Functional)
- [REQUIREMENT] Tax compliance reporting (ID: REQ-011, Type: Functional)
- [FUNCTIONALITY] SuiteTax, Tax Exemption Certificate Management
- [PRIORITY] Must-Have - Tax compliance is regulatory requirement
- [CONSTRAINT] Miller Knoll policy requires warehouse tax on direct bill orders (cannot be changed)
- [RISK] Government customer dissatisfaction with tax approach; KBM Hoag bears reputational impact of manufacturer policy

**Stakeholder Impact:**
- **Primary Users**: Finance/Tax team, Project Coordinators creating proposals
- **Secondary Users**: Sales team (customer communication)
- **Approvers**: Tax Manager (certificate approval)
- **Impacted Parties**: Government customers (affected by tax complexity), Miller Knoll (policy owner)

**Evidence:**
- "KBM Hoag registered in 48 states (nexus). Automatic tax calculation based on ship-to address"
- "Upload certificates with effective dates. Dashboard shows expiring certificates. Automatic application on future quotes for that customer. No manual selection needed"
- "Miller Knoll insists, because you know they're the experts on selling to clients, not the hundreds of dealers that do this every day"
- "Every tax person we've ever talked to in the entire 80 years of our existence in business, we have taxed to final destination"
- "Tax override capability available. Not elegant but workable. Manual process still required"
- "~$1M annually. 1% of $100M total revenue" - Direct bill volume
- "Government frustrated with KBM Hoag but 'we have no control over anything'"

**Confidence Rating**: 97% - Extensive direct quotes detailing current process, pain points, workarounds, and requirements with specific dollar volumes

**Outstanding Items:**
- International tax requirements (not mentioned - appears to be US-only currently)
- Sales tax vs. use tax scenarios
- Tax reporting frequency and submission process
- Avalara vs. SuiteTax decision (transcript shows SuiteTax)

---

### v. Do you have customer hierarchy and relationship management needs?

**Answer:**
The transcript does not provide detailed information about customer hierarchy or parent-child relationship requirements.

**Limited Information:**
- No discussion of parent-child customer relationships
- No mention of consolidated billing requirements
- Customer types discussed (government, direct bill, intermarket) but not hierarchical structures

**Inference from Context:**
- Large government projects suggest potential for multiple agencies under same parent entity
- Intermarket orders with other dealers might benefit from dealer network relationship tracking
- No explicit requirement stated for hierarchical customer management

**User Stories:**
- As a Sales Manager, I need to track customer relationships so that I can see all entities related to a parent organization (POTENTIAL - not confirmed)

**BRD Requirements:**
- [ASSUMPTION] Standard NetSuite customer hierarchy may be sufficient
- [PRIORITY] Should-Have - Further investigation needed to determine if critical

**Evidence:**
- No direct evidence in transcript

**Confidence Rating**: Below 80% - Insufficient evidence. Requires more investigation in follow-up sessions.

**Outstanding Items:**
- Do any customers have parent-child relationships requiring consolidated billing?
- Do government entities need to be grouped under agencies or departments?
- Do intermarket dealers need relationship tracking?
- Are there any corporate customers with multiple subsidiaries or locations?

---

#### Quote Management

### vi. How do you currently manage quote creation from opportunities?

**Answer:**
KBM Hoag has a unique "collapsed" workflow where they complete all work upfront before creating a static proposal. They don't use a traditional quote phase.

**Current Process (Core):**

**Single Transaction Model:**
- Proposal and Sales Order are the same record in Core
- Status changes from "Proposal" to "Sales Order" (booked)
- No separate quote phase: "Quote phase for us is basically we did a ROM before we ever got to a proposal"
- ROM (Rough Order of Magnitude) done before proposal
- Order number assigned at proposal creation
- No CRM module used in Core
- Opportunity tracking in Zendesk (if entered)

**Current Workflow:**
1. Opportunity identified (tracked in Zendesk if entered)
2. ROM/rough budgeting in Google Docs (live document, collaborative)
3. Specification work completed
4. Budget finalized
5. Create Proposal in Core (static from this point forward)
6. Client approval
7. Change status to Sales Order (booked)
8. Generate Purchase Orders

**"Collapsed World" Philosophy:**
"We really live in a world of collapsed. So part of us using Google Docs, it's like we have a shared budget that we're working through. And so we have to expect that budget to be met. Like, everything is live. So by the time we get to quote, it's dead at that point. Where it's static. It's not moving any longer. But everything up to that is static. So we don't put anything in there. We don't put anything in the system until we're ready to be static."

**Key Implications:**
- All specification complete before proposal
- Budget finalized before proposal
- Spec check done before proposal
- Everything ready before creating proposal
- No changes expected after proposal created
- High confidence in accuracy
- "Proposal and sales order mean the same thing to us"

**Future State (NetSuite/Orion):**

**Separate Transaction Model:**
- Opportunity (CRM record for pipeline tracking)
- Proposal/Quote (pricing, terms, client approval)
- Sales Order (booked order, ready for fulfillment)
- Each with unique transaction numbers and prefixes
- Still working "collapsed" but in separate transactions

**Transaction Linking:**
- One-click conversion between transaction types
- Automatic data transfer
- Linked together via Project Number/Name
- Project Number and Name consistent across all transactions
- Hyperlinks between all related records

**Benefits of Separation:**
- Compare proposal to sales order (change tracking)
- Better audit trail
- Multiple quotes from single opportunity (capability, though not typical workflow)
- Different fields/data at different stages
- Revenue recognition separation

**User Stories:**
- As a Sales Person, I need to create ROM budgets collaboratively in Google Docs so that I can work with team members in real-time before creating a static proposal
- As a Project Coordinator, I need to convert proposals to sales orders with one click so that no re-keying is required
- As a Sales Manager, I need to track opportunities before they become proposals so that I can forecast pipeline

**Current State Process:**
**PROCESS**: Quote/Proposal Creation  
**TRIGGER**: Client expresses interest in project  
**STEPS**:
1. Sales creates opportunity record (in Zendesk if tracked)
2. Team creates ROM in Google Docs → live collaborative budget with all stakeholders
3. Specification work occurs → complete all spec details
4. Budget finalized → all pricing confirmed
5. Spec check completed → verify all details correct
6. Create Proposal in Core → static snapshot, assigned order number
7. Client reviews and approves → signed proposal obtained
8. Change status to Sales Order → booking
9. Generate POs → fulfillment begins

**SYSTEMS INVOLVED**: Zendesk (opportunity tracking), Google Docs (collaborative budgeting), Core (proposal/SO), Email (client communication)  
**PAIN POINTS**: 
- No CRM integration with Core
- Opportunity tracking inconsistent (if entered in Zendesk)
- Google Docs separate from system of record
- No audit trail of budget evolution
- Can't track multiple quote scenarios from one opportunity

**BRD Requirements:**
- [REQUIREMENT] Opportunity → Proposal → Sales Order workflow with one-click conversion (ID: REQ-001, REQ-004, Type: Functional)
- [REQUIREMENT] Consistent project number across all transaction types (ID: REQ-002, Type: Functional)
- [REQUIREMENT] Hyperlinked relationships between opportunity, proposal, and SO (ID: REQ-005, Type: Functional)
- [REQUIREMENT] Support for creating proposal directly without opportunity if desired (ID: REQ-004, Type: Functional)
- [REQUIREMENT] No additional SO approval beyond proposal approval (ID: REQ-010, Type: Functional)
- [FUNCTIONALITY] NetSuite CRM (Opportunities), Quote/Proposal Management, Sales Order Management, Project Records
- [PRIORITY] Must-Have - Core transaction workflow
- [CONSTRAINT] Team works in "collapsed" model - all work done before creating static proposal
- [RISK] Change management challenge with separate transaction numbers vs. single order number

**Stakeholder Impact:**
- **Primary Users**: Sales team, Project Coordinators, Shannon
- **Secondary Users**: Finance (booking), Operations (PO generation)
- **Impacted Parties**: Entire organization (workflow change)

**Evidence:**
- "Proposal and Sales Order are the same record. Status changes from 'Proposal' to 'Sales Order' (booked)"
- "Quote phase for us is basically we did a ROM before we ever got to a proposal"
- "We really live in a world of collapsed... everything is live... by the time we get to quote, it's dead at that point. Where it's static"
- "Sales order means donezo. Ready for sales."
- "One-click conversion between transaction types. Automatic data transfer"
- "Project number stays consistent... Always one click away from the project record"

**Confidence Rating**: 98% - Extensive direct quotes detailing current process, philosophy, and future state approach

**Outstanding Items:**
- How will Google Docs budgeting integrate or connect to NetSuite records?
- Will opportunity tracking become mandatory or remain optional?
- Pipeline forecasting methodology (discussed briefly - forecast from opportunity level to prevent over-forecasting)

---

### vii. How do you handle complex quote line editing?

**Answer:**
KBM Hoag handles complex BOM imports and quote line editing through several specialized tools:

**SIF Import Tool (Orion Capability):**
- Import SIF files to quote/proposal
- 60 columns of data imported
- Smart table display with quick views
- Custom grouping capabilities
- Drag and drop organization
- All SIF columns map to their own fields (no concatenation required)

**Smart Table Grouping Capabilities:**
- Ship-to location
- Ship date
- Floor/area (installation strategy)
- Vendor
- Product type (standard vs. specials/customs)
- WHIPs (Work Hold In Progress - expedited items)
- Custom groups for PO planning

**Option Code Changes:**
- Can change option codes in popup window
- Shows: Part number, option code, option description
- **No validation** - must be careful
- Risk of entering invalid options
- Users need to be cautious

**XML Import (Rare but Used):**
- Sometimes build spec in Excel, export as XML, upload
- "Very rare, but we have used that feature"
- Vendors send XMLs as quotes (Jack sends XML for accessories)
- Orion supports XML import with JSON conversion
- Need example template from Matt to build conversion schema

**Vendor Quote Tool Integration:**
- Miller Knoll Quote Tool engaged at proposal level
- Price validation
- Vendor response utility
- Accept pricing or create issue
- Same tool used for POs

**Core Comparison:**
- Core has popup asking to concatenate SIF fields
- Core limits: "SIF file has more fields than core will accept"
- Core combines/concatenates fields
- NetSuite: All SIF columns map to their own fields - "No having to tell it what to do"

**Tag Handling:**
- Tags (floor, room, chair tag, etc.) each get their own field
- No confusion about tag1, tag2, tag3, tag4
- No automatic combining
- Cleaner data structure

**User Stories:**
- As a Project Coordinator, I need to import SIF files with 60 columns so that I don't lose any specification data
- As a Sales Person, I need to group quote lines by installation strategy so that I can plan PO splits effectively
- As a Specifier, I need to import XML quotes from vendors so that I can quickly add accessories to proposals

**BRD Requirements:**
- [REQUIREMENT] SIF import with 60-column data mapping to Smart Table (ID: REQ-006, Type: Functional)
- [REQUIREMENT] XML import with JSON conversion capability (ID: REQ-007, Type: Functional)
- [REQUIREMENT] Smart Table grouping for PO planning and installation strategies (ID: REQ-008, Type: Functional)
- [REQUIREMENT] Option code editing capability (with user caution for validation) (Type: Functional)
- [REQUIREMENT] Vendor Quote Tool integration for price validation (ID: REQ-042, Type: Functional)
- [FUNCTIONALITY] Orion Smart Table, BOM Import Tool, Vendor Quote Tool
- [SOLUTIONDESIGN] Yes - XML conversion schema development
- [PRIORITY] Must-Have for SIF import; Should-Have for XML import
- [RISK] Option code editing without validation could result in invalid configurations

**Stakeholder Impact:**
- **Primary Users**: Project Coordinators, Sales team, Specifiers
- **Secondary Users**: Operations team (PO planning visibility)

**Evidence:**
- "60 columns of data imported. Smart table display with quick views"
- "Group items by how POs should be split. Installation strategy drives grouping"
- "Core limits: 'SIF file has more fields than core will accept'. Core combines/concatenates fields"
- "NetSuite: All SIF columns map to their own fields. No having to tell it what to do"
- "Sometimes build spec in Excel, export as XML, upload. Very rare, but we have used that feature"
- "Can change option codes in popup window... No validation - must be careful"

**Confidence Rating**: 95% - Extensive direct quotes with detailed functionality descriptions

**Outstanding Items:**
- XML import template examples (Matt to provide)
- Specific tag field requirements
- Line-level detail modification frequency
- Most common grouping strategies used

---

### viii. What quote approval workflows do you currently have?

**Answer:**
Quote/proposal approval workflows are covered under customer-specific approval requirements (see question iii above). Key approval rules apply to both quotes and sales orders:

- Orders over $25,000 → Shannon approval
- Missing requirements (deposit, signed proposal, drawings, lookbook) → Matt approval
- Cumulative erosion over $1,500 → Matt approval

**NetSuite Capability:**
- Business Rule Engine with sophisticated criteria
- Automatic routing to approvers
- Approvers see on dashboard
- Approve/reject/exception handling
- Timestamp and audit trail
- Report on approval times (average, individual)
- "As sophisticated or as simple as you want"

**Multiple Approval Workflows:**
- Yes - different workflows for different scenarios
- Budget for up to 10 approval rules
- Can have multiple complex rules

**Evidence:**
See question iii for detailed evidence

**Confidence Rating**: 98% - Covered extensively in approval requirements section

---

### ix. How do you handle alternative billing options?

**Answer:**
KBM Hoag processes several specialized billing models beyond standard orders:

**1. Direct Bill (~$1M/year, 1% of revenue):**
- Client pays Miller Knoll directly for product
- KBM Hoag gross up for commission:
  - Give full sales amount to Miller Knoll
  - Miller Knoll kicks back commission to KBM Hoag
- Tracked separately for reporting
- Hits financials as normal income/COGS (no DB items needed)
- Auditor-approved approach
- Often combined with government orders

**2. Intermarket Orders:**

**Inbound (~40/year):**
- "39 more than we're used to"
- Other dealers sending orders to KBM Hoag territory
- All through ServiceTime platform

**Outbound (Thousands annually):**
- Shannon handles for all Intuit work-from-home
- "Literally" thousands of transactions
- 8-10/day average per Shannon
- 100+/month
- 20-30/week minimum
- Shannon's primary workload
- All through ServiceTime integration

**Pain Point:** "Biggest pain they ask is setting up that dealer if we haven't done it with them before" - must set up other dealer as both vendor AND customer

**3. Intuit Work from Home (Subset of Intermarket):**
- Massive volume (Shannon's primary work)
- Want separate order type for reporting
- Currently "e-commerce" in Core (Shopify legacy)
- Should rename to "Intuit Work from Home"

**4. Government Orders (20% of business):**
- Special tax handling (see question iv)
- Sometimes direct bill to Miller Knoll
- Tax complexity (warehouse vs. final destination)

**Purpose of Order Types in Orion:**
- Primarily informational for reporting
- Can drive business process/automation
- Default order functionality (auto-import lines)

**Challenges:**
- Intermarket: Setting up dealers as both vendor AND customer first time
- Direct bill: Tax override complexity with government orders
- Volume management: Shannon processing thousands of intermarket orders

**User Stories:**
- As a Project Coordinator - Shannon, I need streamlined intermarket order processing so that I can handle thousands of transactions efficiently
- As a Finance Manager, I need to track direct bill orders separately so that I can report on this revenue stream accurately
- As an Operations Manager, I need government order visibility so that I can ensure proper tax handling

**BRD Requirements:**
- [REQUIREMENT] Direct Bill order type configuration (~$1M/year) (ID: REQ-031, Type: Functional)
- [REQUIREMENT] Intermarket order type configuration (inbound and outbound) (ID: REQ-032, Type: Functional)
- [REQUIREMENT] "Intuit Work from Home" order type for reporting (ID: REQ-033, Type: Functional)
- [REQUIREMENT] Government order type configuration (20% of business) (ID: REQ-034, Type: Functional)
- [REQUIREMENT] ServiceTime integration for intermarket orders (ID: REQ-041, Type: Functional)
- [REQUIREMENT] Vendor/customer setup for intermarket dealers (Type: Functional)
- [FUNCTIONALITY] NetSuite Order Types, Default Orders, ServiceTime Integration
- [PRIORITY] Must-Have - Core revenue streams
- [CONSTRAINT] Direct bill orders require gross-up accounting treatment
- [RISK] High intermarket volume requires efficient processing to avoid Shannon bottleneck

**Stakeholder Impact:**
- **Primary Users**: Shannon (intermarket specialist), Project Coordinators, Finance team
- **Secondary Users**: Sales team, Operations team
- **Impacted Parties**: Intermarket dealer partners, Government clients

**Evidence:**
- "~$1M annually. 1% of $100M total revenue" - Direct bill volume
- "Shannon handles for all Intuit work-from-home. Literally thousands of transactions"
- "I average probably about 8 to 10 a day" - Shannon on daily intermarket volume
- "It's at least 20 or 30 a week. At least." - Shannon
- "I'm probably doing 100 a month, if not more" - Shannon
- "20% of business" - Government orders
- "Biggest pain they ask is setting up that dealer if we haven't done it with them before"
- "All through ServiceTime integration"

**Confidence Rating**: 96% - Multiple direct quotes with specific volumes and pain points from Shannon

**Outstanding Items:**
- Complete list of all order types with descriptions (action item assigned)
- Accounting treatment details for direct bill gross-up process
- ServiceTime integration technical specifications
- Default order line configurations by order type

---

### x. What are your quote PDF and document requirements?

**Answer:**
KBM Hoag has specific template and document management requirements with a strong emphasis on self-service control.

**Current Challenge with Core:**
- Any template change requires Core vendor billable hours
- Example: "Change verbiage on the footer of our invoice"
- Have to contact Core support, wait for changes, pay per change
- "That's insane"

**Kipp's Template Redesign (5 years ago):**
- Redesigned all templates 5 years ago
- "No one has said anything to me about anything on this proposal"
- Happy with current designs
- "Are you saying there's a problem?" (Kipp to team - defensive of his designs)
- Got rid of "core beige envelope"

**NetSuite Solution - Template Ownership:**
- "You can do it yourself"
- "Are these templates things that we can own and manage ourselves? Yes, sir."
- No vendor billable hours for changes
- Self-service modifications
- Kipp's requirements: Communication record of changes, document why changing, version history, lock down process

**Types of Templates Needed:**

**Customer-Facing:**
- Proposals
- Invoices
- Order confirmations
- Quotes
- Other client documents

**Vendor-Facing (New Focus):**
- Purchase orders
- "We never touch vendor facing"
- "I would like to reevaluate the design of vendor facing"
- Opportunity to improve during implementation
- Current issue: "Our current POs are a shitstorm of information" - Kipp

**Template Format Features:**
- Little table in top right corner (invoices)
- Multiple data points
- Can add proposal/quote number to invoice
- Reference original order number
- Customer PO number
- All cross-referenced for client AP matching

**PDF Generation:**
- Custom templates (Kipp's designs)
- "We're going to give you templates, you're going to get yours, so we can recreate them"
- Ability to modify without vendor involvement
- Not using automated client approval workflow - traditional PDF signature approach

**User Stories:**
- As a Design Manager - Kipp, I need to modify invoice templates myself so that I don't pay vendor billable hours for simple changes
- As a Finance Manager, I need to include all reference numbers on invoices so that clients can match to their POs and approve payment quickly
- As an Operations Manager, I need better-organized PO templates so that vendors receive clear, professional documents

**BRD Requirements:**
- [REQUIREMENT] Self-service template management without vendor billable hours (ID: REQ-027, Type: Functional)
- [REQUIREMENT] Template version control and change documentation process (ID: REQ-028, Type: Functional)
- [REQUIREMENT] Recreate all customer-facing templates (proposals, invoices, order confirmations) (ID: REQ-029, Type: Functional)
- [REQUIREMENT] Redesign vendor-facing templates (purchase orders) (ID: REQ-030, Type: Functional)
- [REQUIREMENT] Cross-reference numbers on invoices (invoice #, customer PO #, original quote/proposal #) (ID: REQ-019, Type: Functional)
- [FUNCTIONALITY] NetSuite PDF Composer, Advanced PDF/HTML Templates
- [SOLUTIONDESIGN] Yes - Custom template designs recreated
- [PRIORITY] Must-Have - Customer and vendor communication documents
- [CONSTRAINT] Kipp owns template design approval; requires version control process

**Stakeholder Impact:**
- **Primary Users**: Kipp (template owner), Finance team (invoices), Sales team (proposals), Operations (POs)
- **Approvers**: Kipp (template changes)
- **Impacted Parties**: Customers (receiving proposals/invoices), Vendors (receiving POs)

**Evidence:**
- "I have to go to Core and they have billable hours for that. That's insane."
- "Are these templates things that we can own and manage ourselves? Yes, sir."
- "Communication record of changes. Document why changing. Version history"
- "Our current POs are a shitstorm of information. I'd like them to be more organized in their format"
- "We're going to give you templates, you're going to get yours, so we can recreate them"
- "Can add proposal/quote number to invoice. Reference original order number. Customer PO number"

**Confidence Rating**: 97% - Extensive direct quotes covering pain points, requirements, and Kipp's ownership

**Outstanding Items:**
- All current templates to be provided by Kipp (action item)
- Specific template change control process workflow
- Who besides Kipp can authorize template changes post go-live
- Template testing and approval process during implementation

---

### xi. How do you manage quote versioning and revisions?

**Answer:**
The transcript provides limited direct information about quote versioning, but context suggests an approach based on their "static proposal" philosophy.

**Implied from Context:**

**Current Approach:**
- Proposals are created as static documents after all upfront work complete
- "By the time we get to quote, it's dead at that point. Where it's static"
- Changes not expected after proposal created
- If changes needed, likely create new proposal

**NetSuite Capability:**
- Can compare proposal to sales order (change tracking)
- Better audit trail with separate transactions
- Multiple quotes from single opportunity (capability exists)
- Opportunity to track quote versions if needed

**Change Management:**
- No mention of tracking quote revisions or versions systematically
- Order change management discussed at SO level (erosion tracking and approval)

**User Stories:**
- As a Project Coordinator, I need to track if proposals change after being issued so that I have an audit trail (POTENTIAL)

**BRD Requirements:**
- [ASSUMPTION] Standard NetSuite quote revision tracking may be sufficient
- [REQUIREMENT] Compare proposal to sales order for change tracking (ID: REQ-001, Type: Functional)
- [PRIORITY] Should-Have - Further investigation needed

**Confidence Rating**: Below 80% - Insufficient evidence on quote versioning practices

**Outstanding Items:**
- How do you handle client-requested changes to proposals?
- Do you create new proposal versions or modify existing?
- Do you need to track and compare multiple proposal versions?
- How do you ensure team works from latest proposal version?
- What triggers a new proposal version vs. modification?

---

#### Sales Order Management

### xii. How do you handle sales order creation and processing?

**Answer:**
Sales order creation follows KBM Hoag's "collapsed" workflow where all work is complete before the proposal, making SO creation straightforward.

**From Proposal to Sales Order:**

**One-Click Conversion:**
- Click "Sales Order" button on proposal
- Generates new SO record
- All information transfers automatically
- No re-keying required
- Different SO form has different/additional fields

**Different Fields at SO Stage:**
- Proposal form ≠ Sales Order form
- SO form has additional fields
- Opportunity to gather more information
- "Moved one more step in the process, now we need to get more information in order to take the next step"
- Typically ask for more dates at SO stage

**KBM Hoag Approach - No Additional SO Approval:**
- Don't need additional SO approval workflow
- Already done everything upfront
- "By the time it gets there, we've already done all the other stuff, like the spec check"
- "Sales order means donezo. Ready for sales."
- Proposal approval is sufficient

**Why No Additional SO Approval:**
- Doing more upfront to get proposal right
- Spec check complete before proposal
- All validation done
- Proposal approval sufficient
- "We don't issue a quote until we're [ready]"

**NetSuite Capability (Not Needed by KBM Hoag):**
- Could add SO approval workflow if wanted
- After proposal approved, before SO booked
- Before generating POs
- KBM Hoag doesn't need this

**Live Budget → Static Proposal → Sales Order:**
Philosophy carried through: "We really live in a world of collapsed... everything is live. So by the time we get to quote, it's dead at that point. Where it's static... we don't put anything in the system until we're ready to be static."

**Information Captured:**
- All specification data
- Pricing
- Terms
- Customer PO number
- Signed documents (proposal, drawings, lookbook)
- Deposit
- Additional dates at SO stage

**User Stories:**
- As a Project Coordinator, I need to convert approved proposals to sales orders with one click so that booking is fast and error-free
- As an Operations Manager, I need sales orders to have all required information so that I can immediately begin PO generation

**BRD Requirements:**
- [REQUIREMENT] One-click proposal to sales order conversion (ID: REQ-004, Type: Functional)
- [REQUIREMENT] Automatic data transfer from proposal to SO (ID: REQ-004, Type: Functional)
- [REQUIREMENT] Different SO form with additional fields (especially dates) (Type: Functional)
- [REQUIREMENT] No additional SO approval workflow beyond proposal approval (ID: REQ-010, Type: Functional)
- [FUNCTIONALITY] NetSuite Sales Order Management, Transaction Conversion
- [PRIORITY] Must-Have - Core transaction process
- [CONSTRAINT] Team philosophy: All work done upfront, SO is final booking step only

**Stakeholder Impact:**
- **Primary Users**: Project Coordinators, Shannon, Sales team
- **Secondary Users**: Operations (PO generation), Finance (booking)

**Evidence:**
- "Click 'Sales Order' button on proposal. Generates new SO record. All information transfers automatically. No re-keying"
- "SO form has different/additional fields... typically ask for more dates at SO stage"
- "By the time it gets there, we've already done all the other stuff, like the spec check"
- "Sales order means donezo. Ready for sales"
- "We don't put anything in the system until we're ready to be static"

**Confidence Rating**: 95% - Clear direct quotes on process and philosophy

**Outstanding Items:**
- Specific additional fields needed on SO form vs. proposal form
- What dates are captured at SO stage
- Sales order status workflow after booking

---

### xiii. What order types do you process?

**Answer:**
See question ix above for detailed coverage of order types. Summary:

**Identified Order Types:**
1. Direct Bill (~$1M/year, 1% of revenue)
2. Intermarket Inbound (~40/year)
3. Intermarket Outbound (thousands/year)
4. Intuit Work from Home (subset of intermarket, want separate type)
5. Government Orders (20% of business)

**Purpose:**
- Primarily informational for reporting
- Can drive business process/automation
- Default order functionality (auto-import lines)

**Evidence:**
See question ix for detailed evidence

**Confidence Rating**: 96% - See question ix

**Outstanding Items:**
- Complete list of all order types with descriptions (action item assigned to team)

---

### xv. Do you have multi-order project management needs?

**Answer:**
Yes, KBM Hoag frequently splits large projects into multiple orders based on installation strategy and client requirements.

**Project Strategy - Multiple Orders:**
- Large projects broken into multiple orders for installation strategy
  - By floor
  - By area
  - By halls (example: hall chairs separate)
- Or broken by client request (different cost centers)
- Each order becomes separate sales order
- Each SO becomes separate PO

**Project Number Consistency:**
- Same project number across ALL related orders
- Project number primary linking mechanism
- "Always one click away from the project record"
- First view shows all associated transactions

**PO Splitting Strategies:**
- Installation strategy drives splits
- Group by floor or area
- Separate standard from specials/customs (avoid delay)
- Miller Knoll: Separate to avoid holding entire order for custom items

**Smart Table Grouping for PO Planning:**
- Can group quote lines by intended PO split
- Visual planning: "Group items by how POs should be split"
- "This was a conversation at a project level where our PO ordering strategies for a big project would be part of our install strategy"

**Reporting Needs:**
- Project-level GP aggregation
- Customer PO utilization across multiple orders
- Total project value for bank reporting
- Backlog by project
- Invoice status across project orders

**User Stories:**
- As a Project Manager, I need to split large projects into multiple orders by floor so that installation can proceed in phases
- As a Finance Manager, I need to see project-level GP across all related orders so that I understand true project profitability
- As an Operations Manager, I need to see all orders for a project so that I can coordinate installation strategy

**Current State Process:**
**PROCESS**: Multi-Order Project Setup  
**TRIGGER**: Large project with phased installation  
**STEPS**:
1. Complete upfront budgeting for entire project → Google Docs collaborative budget
2. Determine installation strategy → by floor, area, or phase
3. Create first order/proposal → Phase 1 or Floor 1
4. Create subsequent orders → Phase 2, Floor 2, etc.
5. Link via project number → manual tracking
6. Coordinate PO generation → by installation phase
7. Track GP by order → difficulty aggregating to project level

**SYSTEMS INVOLVED**: Core (limited project linking), Google Docs (planning), Manual tracking  
**PAIN POINTS**: 
- Difficult to see project-level aggregated data
- Customer PO tracking across multiple orders
- GP roll-up to project level

**BRD Requirements:**
- [REQUIREMENT] Consistent project number across multiple related orders (ID: REQ-002, Type: Functional)
- [REQUIREMENT] Project Navigator showing all related transactions (Type: Functional)
- [REQUIREMENT] Smart Table grouping for PO planning by installation strategy (ID: REQ-008, Type: Functional)
- [REQUIREMENT] Project-level GP reporting across all orders (ID: REQ-037, Type: Functional)
- [REQUIREMENT] Customer PO tracking aggregated at project level (ID: REQ-017, REQ-018, Type: Functional)
- [FUNCTIONALITY] NetSuite Project Management, Project Navigator, Smart Table
- [PRIORITY] Must-Have - Common business scenario
- [RISK] Tiered pricing challenge (REQ-043) - splitting orders can result in lost discounts

**Stakeholder Impact:**
- **Primary Users**: Project Coordinators, Operations team, Finance team
- **Secondary Users**: Sales team, Executive leadership (project visibility)

**Evidence:**
- "Large projects broken into multiple orders for installation strategy (by floor, by area, etc.)"
- "Or broken by client request (different cost centers)"
- "Group items by how POs should be split. Installation strategy drives grouping"
- "This was a conversation at a project level where our PO ordering strategies for a big project would be part of our install strategy"
- "Project number stays consistent... Always one click away from the project record"
- "First view shows all associated transactions"

**Confidence Rating**: 93% - Strong evidence on multi-order approach and project linking needs

**Outstanding Items:**
- How many projects typically have multiple orders (percentage)
- Average number of orders per multi-order project
- Project-level reporting requirements beyond GP
- How to handle project-level customer communications

---

### xxv. How do you handle purchase order splitting and creation?

**Answer:**
PO splitting is driven by installation strategy and vendor requirements, with a "Draft PO" concept mentioned but not fully explained in the session.

**PO Creation Approaches:**

**Strategic Splitting:**
- Split by installation strategy (floor, area, phase)
- Split by product type (standard vs. specials/customs)
- Miller Knoll: Separate standard from specials to avoid delay
- WHIPs (Work Hold In Progress) - expedited items may be separate

**From Quote to PO:**
- Smart Table grouping shows intended PO splits
- Can group by how POs should be generated
- Installation strategy drives grouping decisions
- One sales order might generate multiple POs

**Draft PO Concept (Session Ended Before Full Discussion):**
- "Here's some big ideas I'm going to introduce. The first one is the concept of the draft PO"
- "Inside NetSuite and actually inside most enterprise..."
- Session break for lunch - topic not completed

**Current PO Issues:**
- Kipp: "Our current POs are a shitstorm of information"
- "I'd like them to be more organized in their format"
- "Deal. We'll make it happen"
- Better organization desired
- More structured presentation needed

**Transaction Types:**
- DPO-#### = Draft Purchase Order
- VPO-#### or PO-#### = Vendor Purchase Order
- Distinction indicates draft vs. finalized PO workflow

**Vendor Quote Tool:**
- Same tool used for proposals and POs
- Price validation at PO level
- Vendor response utility
- Accept pricing or create issue

**User Stories:**
- As an Operations Manager, I need to create draft POs for review before sending to vendors so that I can verify details and get internal approval
- As a Purchaser, I need to split POs by installation strategy so that vendors ship according to our project plan
- As a Project Coordinator, I need better-organized PO templates so that vendors receive clear instructions

**BRD Requirements:**
- [REQUIREMENT] Draft PO creation and management workflow (Type: Functional)
- [REQUIREMENT] PO splitting capability based on Smart Table grouping (ID: REQ-008, Type: Functional)
- [REQUIREMENT] Redesigned PO templates with better organization (ID: REQ-030, Type: Functional)
- [REQUIREMENT] Vendor Quote Tool integration for PO price validation (ID: REQ-042, Type: Functional)
- [FUNCTIONALITY] Orion Draft PO, PO Management, PDF Templates
- [SOLUTIONDESIGN] Yes - PO template redesign
- [PRIORITY] Must-Have - Core fulfillment process
- [CONSTRAINT] Installation strategy drives PO splitting logic

**Stakeholder Impact:**
- **Primary Users**: Operations team, Purchasing, Project Coordinators
- **Secondary Users**: Finance (PO approval if needed), Vendors (receiving POs)

**Evidence:**
- "Here's some big ideas I'm going to introduce. The first one is the concept of the draft PO"
- "Our current POs are a shitstorm of information. I'd like them to be more organized in their format"
- "Group items by how POs should be split. Installation strategy drives grouping"
- "Miller Knoll: Separate standard from specials/customs (avoid delay)"
- "DPO-#### = Draft Purchase Order. VPO-#### or PO-#### = Vendor Purchase Order"

**Confidence Rating**: 85% - Topic mentioned but session ended before full discussion; requires follow-up

**Outstanding Items:**
- Complete explanation of Draft PO concept and workflow (follow-up session needed)
- Draft PO approval requirements
- When does draft PO become vendor PO
- PO transmission methods
- PO change order process

---

### xxxii. How do you monitor margin erosion from acknowledgment changes?

**Answer:**
Margin erosion is monitored through approval workflows rather than automated reporting.

**Erosion Approval Workflow:**
- Cumulative erosion over $1,500 triggers approval
- Routes to Matt for email approval
- Tracks cumulative erosion across changes

**Purpose:**
- Training opportunity: "New person who's the reason for the erosion, like they made a mistake"
- Problem-solving with experience: Finding cheaper solutions
- Matt's expertise in cost-effective alternatives

**Matt's Crane Story (Example):**
- Problem: Table doesn't fit in elevator or stairs
- Clay's solution: Rent crane ($6K-$10K plus permit plus traffic control)
- Matt's solution: Float table on top of elevator with technician on-site
- Cost: $1,200 vs. $6K-$10K
- Lesson: Experience finds cheaper solutions
- "If we're going to spend the money, let's spend it this way"

**Reporting Needs:**
- Erosion by project
- Erosion by person (training identification)
- Cumulative erosion tracking
- GP impact visibility

**User Stories:**
- As an Executive - Matt, I need to review significant erosion so that I can provide cost-effective alternatives and train team members
- As a Finance Manager, I need to track erosion by project so that I can see which projects are impacting margins
- As a Project Coordinator Manager - Shannon, I need to see erosion patterns by team member so that I can identify training needs

**BRD Requirements:**
- [REQUIREMENT] Cumulative erosion approval workflow over $1,500 (ID: REQ-022, Type: Functional)
- [REQUIREMENT] Erosion tracking and reporting by project (Type: Functional)
- [REQUIREMENT] Erosion tracking by team member for training purposes (Type: Functional)
- [FUNCTIONALITY] NetSuite Business Rule Engine, Saved Searches for Erosion Reporting
- [PRIORITY] Must-Have - Margin protection and training tool
- [CONSTRAINT] Approval threshold at $1,500 cumulative

**Stakeholder Impact:**
- **Primary Users**: Matt (approver), Project Coordinators, Shannon
- **Secondary Users**: Finance team (margin reporting)

**Evidence:**
- "Erosion > $1,500 Cumulative. Example: $500 erosion + $1,000 more = $1,500 triggers"
- "Training insight: 'New person who's the reason for the erosion, like they made a mistake'"
- "Matt's Erosion Story: Clay runs in: 'We need to rent a crane!'... Matt's solution: Float table on top of elevator... Cost: $1,200" vs. $6K-$10K crane
- "If we're going to spend the money, let's spend it this way"

**Confidence Rating**: 94% - Clear approval workflow with specific example story

**Outstanding Items:**
- How is erosion calculated and tracked currently
- Definition of erosion (cost increases? pricing decreases? both?)
- Erosion reporting requirements beyond approval workflow
- How vendor acknowledgment price changes trigger erosion calculation

---

### xxxiii. What manufacturer integrations do you currently have?

**Answer:**
KBM Hoag has existing and planned integrations with Miller Knoll systems.

**Miller Knoll ServiceNet Integration:**
- Plan to link ServiceNet to Orion
- "Did you talk about Miller linking ServiceNet into Orion at some point? Yes. Yep. Absolutely."
- Used for intermarket orders (thousands annually)
- Already integrated with Core currently

**Miller Knoll Quote Tool:**
- Currently integrated
- Used at proposal level and PO level
- Price validation
- Vendor response utility
- Accept pricing or create issue

**Order Manager Integration (Standard Orion):**
- Aligned Manufacturer Integration capability
- Automated acknowledgment retrieval potential
- Vendor bill automation and creation capability
- Order status monitoring and alerts
- Draft vs. live order transmission

**Potential Coupa Integration:**
- Email parsing for order creation (Shannon's intermarket work)
- "As long as the emails have order information that's pretty consistent, it's pretty easy to do"
- Email parsing to create orders automatically
- Automated processing
- Bi-directional: Invoice back to Coupa portal
- Currently manual process

**User Stories:**
- As an Operations Manager, I need ServiceNet integration so that intermarket orders flow automatically
- As a Purchaser, I need Miller Knoll Quote Tool integration so that I can validate pricing before ordering
- As a Project Coordinator - Shannon, I need Coupa email parsing so that I can process thousands of intermarket orders efficiently

**BRD Requirements:**
- [REQUIREMENT] Miller Knoll ServiceNet integration with Orion (ID: REQ-039, Type: Functional)
- [REQUIREMENT] Miller Knoll Quote Tool integration at proposal and PO level (ID: REQ-042, Type: Functional)
- [REQUIREMENT] Evaluate Coupa email parsing automation for order creation (ID: REQ-040, Type: Functional)
- [REQUIREMENT] ServiceTime integration for intermarket orders (ID: REQ-041, Type: Functional)
- [FUNCTIONALITY] Order Manager Integration, ServiceNet, ServiceTime
- [SOLUTIONDESIGN] Yes - Email parsing automation for Coupa (if approved)
- [PRIORITY] Must-Have for ServiceNet/ServiceTime; Should-Have for Coupa automation
- [RISK] High intermarket volume makes automation critical for Shannon's workload

**Stakeholder Impact:**
- **Primary Users**: Shannon (intermarket), Operations team, Purchasing
- **Secondary Users**: Finance team
- **Impacted Parties**: Miller Knoll (integration partner)

**Evidence:**
- "Did you talk about Miller linking ServiceNet into Orion at some point? Yes. Yep. Absolutely."
- "Price validation. Vendor response utility. Accept pricing or create issue. Same tool as for POs"
- "As long as the emails have order information that's pretty consistent, it's pretty easy to do"
- "Email parsing to create orders. Automated processing. Bi-directional: Invoice back to Coupa portal"
- "All through ServiceTime integration" - for intermarket orders

**Confidence Rating**: 90% - Clear integration requirements stated, though technical details pending

**Outstanding Items:**
- ServiceNet integration technical specifications
- Coupa email format consistency and reliability
- Decision on whether to proceed with Coupa automation
- Other manufacturer integrations beyond Miller Knoll
- Order Manager integration scope for acknowledgments and vendor bills

---

### xxxvii. What are your current challenges with order management?

**Answer:**
The transcript reveals several significant pain points and challenges:

**1. Transaction Number Confusion:**
- "There's still a lot of confusion around is it a quote, is it a proposal, is it a sales order?"
- Different numbers for each transaction type feels overwhelming
- Currently reference single order number; need to shift to project-based thinking
- "This is like the one thing during discovery that people get tripped up on"
- Change management challenge: "Kleenex may be required, but we should be able to wipe our tears pretty quickly"

**2. Miller Knoll Tiered Pricing Problem (Major Issue):**
- Large projects split into multiple POs lose tiered discount eligibility
- Manufacturer looks at PO level, not project level
- Lose deeper discounts despite qualifying based on project total
- "Nightmare to get them to put these different POs together and give us a deeper discount"
- Installation strategy conflicts with pricing optimization
- GP tracking issues if keep on one PO to preserve discount
- Potential solution: Escalate to Dustin (Miller Knoll) for project-level recognition

**3. Government Order Tax Complexity:**
- Miller Knoll requires warehouse tax, not final destination tax
- Conflicts with standard tax practice
- Manual workaround: Change address, calculate, change back, override
- "It's a pain in the butt"
- "Not elegant" in NetSuite either
- Government customer frustration
- KBM Hoag bears reputational impact but has no control

**4. Customer PO Tracking:**
- No visibility to PO exhaustion
- Risk of exceeding PO limits
- Payment delays when limits exceeded
- Cannot provide bank reporting requirements
- Blanket POs with no running balance

**5. Template Management Costs:**
- Vendor billable hours for every template change
- Slow turnaround for simple changes
- "That's insane"
- No ownership or control

**6. Double Orders (Biggest Financial Losses):**
- "The two that have hurt us the hardest are both the double orders"
- Example: 150 workstations ordered and owned unintentionally
- Not discovered until shipment notice
- Shannon's $25K approval designed to catch these
- Need better automated detection

**7. Vendor Credit Limits:**
- Unexpected hits to credit limits
- "Mad scramble at that nth hour because our order won't go through because we hit it"
- Order rejections
- No proactive visibility

**8. Intermarket Dealer Setup:**
- "Biggest pain they ask is setting up that dealer if we haven't done it with them before"
- Must set up as both vendor AND customer
- Time-consuming for first-time dealers
- Shannon processing thousands of orders

**9. Spec Creation Without Catalogs:**
- "Old timers use Core to write our specs"
- NetSuite doesn't have catalog integration currently
- Must use external tools (Project Spec, CET, CAP)
- Some resistance: "I refuse to learn project spec"
- Impact on small orders, showroom orders, employee orders
- "It's faster for me to just write a proposal than send an email and ask for it"

**10. PO Organization:**
- "Our current POs are a shitstorm of information"
- Need better structure and organization
- Vendor-facing documents never redesigned

**11. Information Accessibility:**
- "Information is going to be presented to us differently than it is in Core"
- Currently difficult to find information
- "Core is impossible to find something without that data"
- Reliance on specific data formats

**User Stories:**
- As a Project Coordinator, I need to search by project number instead of order number so that I can find all related transactions easily
- As a Finance Manager, I need tiered pricing to recognize project-level volumes so that we don't lose margin on split orders
- As an Operations Manager, I need proactive credit limit warnings so that POs aren't rejected at the last minute

**BRD Requirements:**
See requirements throughout questionnaire addressing these pain points

**Evidence:**
- Multiple direct quotes throughout (see individual pain point sections above)

**Confidence Rating**: 98% - Extensive evidence throughout transcript

---

### xxxviii. What manual processes need automation?

**Answer:**
Several manual processes were identified for automation:

**1. Approval Routing:**
- Currently manual approval tracking
- Need automated routing based on business rules
- Automatic dashboard visibility for approvers
- Approval time tracking

**2. Tax Exemption Certificate Application:**
- Currently manual selection
- NetSuite: Automatic application on future quotes

**3. Tax Certificate Expiration Monitoring:**
- Need dashboard showing expiring certificates
- Proactive renewal reminders

**4. Customer PO Utilization Tracking:**
- Currently no tracking
- Need automated calculation: PO value - billed amount = remaining
- Alert when approaching limit

**5. Vendor Credit Limit Monitoring:**
- Currently discover at time of rejection
- Need threshold warnings (e.g., 90% of limit)
- Prevent PO creation if over limit

**6. Double Order Detection:**
- Currently relies on Shannon's manual review
- Need query: Same $ amount in last 30 days
- Automatic flagging for review

**7. Template Generation:**
- Self-service template modifications
- No vendor involvement needed

**8. Transaction Linking:**
- Currently manual project number tracking
- NetSuite: Automatic hyperlinks between related records
- One-click navigation

**9. Intermarket Order Processing (Potential):**
- Coupa email parsing to create orders automatically
- Bi-directional invoice transmission
- Reduce Shannon's manual processing of thousands of orders

**10. Tiered Pricing Optimization (Pending):**
- If Miller Knoll accepts project-level pricing
- Automatic recognition of related POs
- Preserve discounts while enabling installation strategy splits

**11. Transaction Conversions:**
- One-click opportunity → proposal → sales order
- Automatic data transfer
- No re-keying

**12. SIF/XML Import:**
- Automatic field mapping (no manual concatenation)
- All 60 columns preserved

**13. Commission Calculation:**
- Header-level and line-level rules
- Automatic commissionable GP calculation
- Formula-based labor markup

**User Stories:**
- As a Project Coordinator, I need automated approval routing so that I don't have to manually email approvers
- As a Finance Manager, I need automated PO tracking calculations so that I always know remaining balance
- As Shannon, I need Coupa email parsing so that thousands of intermarket orders don't require manual entry

**BRD Requirements:**
See requirements throughout questionnaire

**Confidence Rating**: 95% - Clear automation opportunities identified throughout transcript

---

## SECTION B: OBJECTIVES & STRATEGY

### Overall Goals for Order Management Improvement

**Primary Goals:**
1. Maintain current "collapsed" workflow efficiency while gaining audit trail benefits
2. Eliminate vendor dependency for template changes
3. Improve visibility: Customer PO tracking, vendor credit limits, erosion
4. Automate approval workflows
5. Resolve Miller Knoll tiered pricing challenge
6. Streamline high-volume intermarket processing
7. Improve PO organization and clarity

**Success Definition:**
- Zero disruption to business during implementation
- Faster order processing with better controls
- Self-service template management
- Reduced risk (double orders, PO limits, credit limits)
- Better reporting and visibility
- Competitive advantage through customer PO management

**Critical Business Processes:**
- Quote to sales order conversion (must be seamless)
- Approval workflows (must be automated and fast)
- Customer PO tracking (bank requirement)
- Multi-order project management
- Template ownership

---

## Outstanding Items Summary

**High Priority Items Requiring Follow-Up Sessions:**
1. **Draft PO Concept & Workflow** - Session ended before completion (follow-up session scheduled)
2. **Customer PO Tracking Solution Design** - Separate working session needed (scheduled)
3. **Template Design Review** - Kipp to provide templates, GSI to recreate (action item)
4. **E-Portals Discussion** - Deferred topic, follow-up needed

**High Priority Items Requiring Decisions:**
1. **Miller Knoll Tiered Pricing** - Escalation to Dustin required
2. **Coupa Email Parsing** - Decision on automation investment
3. **Complete Order Type List** - Team to provide

**Medium Priority Items Requiring Investigation:**
1. Customer hierarchy requirements (parent-child relationships)
2. Quote versioning practices
3. Deposit management details (percentages, application process)
4. Milestone-based invoicing requirements
5. Spec creation tool integration (Configura/CET timeline)

**Documentation Needed:**
1. Shannon: Approval workflow flowchart
2. Kipp: All current templates (customer and vendor-facing)
3. Matt: XML import template example
4. Team: Complete order type list with descriptions

---

## Change Management Considerations

**Behavior Changes Required:**
1. **Reference by Project, Not Order Number** - Biggest adjustment
2. **Static Proposal Mindset Maintained** - Team philosophy preserved
3. **Template Self-Service** - Kipp gains control
4. **Customer PO Manual Management** - Team willing to manage

**Resistance Points:**
1. Transaction number changes ("Kleenex may be required")
2. Catalog loss for spec creation (workaround with external tools)
3. Separate transactions feel like more work initially

**Success Factors:**
1. Project number emphasis in training
2. Demonstrate global search and navigation
3. Template self-service (immediate win)
4. Customer PO tracking (bank requirement met)
5. Better audit trail and reporting

---

**END OF QUESTIONNAIRE**


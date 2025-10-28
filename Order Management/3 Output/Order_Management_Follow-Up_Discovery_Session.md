
# Order Management Comprehensive Follow-Up Discovery Session
## KBMH NetSuite/Orion Implementation

**Date:** October 2025  
**Session Duration:** Comprehensive single session covering all 8 interconnected topics  
**Priority:** High - Core transaction processing, approval workflows, and custom solutions  
**Participants Needed:**
- Shannon (Order Manager/Approvals) - Primary
- Matt (Leadership/Operations) - For strategic decisions
- Kipp (IT/Process) - For systems integration decisions
- Product Coordinators - For workflow details
- Finance/AR Representative - For customer and credit limit tracking
- Dustin (Miller Knoll) - For tiered pricing coordination (if available)

---

## OVERVIEW

This comprehensive follow-up session will address critical gaps between what was discovered and what's needed for successful NetSuite/Orion configuration. The session covers 8 interconnected topic areas covering transaction structure, approval workflows, custom solutions, tax management, templates, order types, tiered pricing, and specification/BOM management.

**Session Agenda:**
1. Transaction Structure & Numbering
2. Approval Workflow Automation & Rules
3. Customer PO Tracking Solution Design
4. Tax Management & Government Orders
5. Template Management & Document Redesign
6. Order Types, Integrations & Special Processing
7. Tiered Pricing with Miller Knoll
8. Specification & BOM Management
9. Decisions & Next Steps

---

## PART 1: CURRENT STATE KNOWLEDGE SUMMARY

### What We Know About Your Order Management

Based on our comprehensive discovery sessions, we have documented a strong understanding of your order management operations:

#### **Your Order Management Team & Operations**
- **Shannon** - Primary order approver and manager, handles approval workflow ($25K threshold, completeness verification)
- **Matt** - Leadership, final approver for missing items and margin erosion over $1,500
- **Product Coordinators** - Specification and BOM management
- **Kipp** - Systems integration and technical process design
- **Operations** - Managing thousands of intermarket transactions annually

#### **Current Order Processing**
- **Single Transaction Model in Core** - Proposal and Sales Order are same record with status changes
- **Upfront "Collapsed" Workflow** - All specification work done in Google Docs before proposal created
- **ROM (Rough Order of Magnitude)** - Budget estimation before formal proposal
- **Static Proposals** - No changes expected after proposal created ("by the time we get to quote, it's dead at that point")
- **Transaction Numbering** - Single order number memorized, assigned at proposal creation

#### **Order Types & Special Handling**
- **Direct Bill Orders** (~$1M annually, 1% of revenue) - Miller Knoll direct payment with commission kickback
- **Intermarket Orders** (inbound ~40/year, outbound thousands) - Dealers as both vendor AND customer, ServiceTime integration
- **Intuit Work from Home Orders** - E-commerce type, high volume, separate reporting
- **Government Orders** (20% of business) - Special tax handling with warehouse complexity

#### **Tax Management**
- **48 states with nexus registration** - SuiteTax for automatic tax calculation by ship-to address
- **Tax exemption certificates** - Dashboard tracking expiration dates, automatic application
- **Government Order Complexity** - Miller Knoll insists on warehouse tax vs. industry standard final destination tax
- **Current Workaround** - Manual address swapping in Core to calculate, then override (described as "a pain in the butt")

#### **Customer Financial Management**
- **Customer PO Tracking** - Critical pain point: blanket POs with no tracking of utilization
- **Storage Fees** - Variable by warehouse (30-90 day free periods), billed back to client, always commissionable
- **Finance Charges** - Never implemented in 13 years (deterrent only)
- **Direct Bill Commission** - Gross up entire Miller Knoll amount with commission kickback

#### **Current Approval Workflows**
- **Orders over $25,000** - Require Shannon approval (completeness verification)
- **Missing Requirements** - Any missing deposit/proposal/drawings/lookbook routes to Matt
- **Margin Erosion** - Cumulative $500 + $1,000 more = $1,500 triggers Matt email approval
- **Manual Process** - No system-enforced workflows currently
- **No Double Order Detection** - Risk of accidentally creating duplicate orders

#### **Proposal & Quote Management**
- **Quote/Proposal Features** - Smart Table with 60-column SIF import, drag-and-drop grouping
- **PO Planning** - Group items by installation strategy, split strategy, vendor, floor/area
- **Specification Method** - External tools (Project Spec, CET/Configura, CAP Worksheets) - Core catalogs not available in NetSuite yet
- **Miller Knoll Integration** - ServiceNet quote tool for price validation at proposal level
- **XML Import** - Rare but used for Excel specs exported as XML

#### **Commission & Margin Management**
- **Project GP vs. Commissionable GP** - Two separate KPI sets
- **Line-Level Commission Marking** - Individual lines flagged as commissionable or not
- **15% Labor Markup** - External labor costs marked up 15% (continuation pending decision)
- **Commission Assignment** - Header-level (who gets commission, percentage/split) and line-level flagging

#### **Templates & Documents**
- **Current Templates** - All customer-facing (proposals, invoices, confirmations) and vendor-facing (POs) need recreation
- **Self-Service Management** - Can be changed without vendor billable hours in NetSuite
- **Vendor-Facing POs** - Current design described as "a shitstorm of information" - needs redesign
- **Version Control** - Need communication record of changes and why

#### **Key Business Practices We Understand**
- **Tiered Pricing Challenge** - Miller Knoll multi-tier contracts recognized by contract number, not project number (escalation to Dustin needed)
- **Intermarket Setup** - Dealers must be set up as both vendor AND customer
- **Pipeline Forecasting** - Should forecast from Opportunity level to prevent over-forecasting with multiple quotes
- **Manual PO Syncing** - Pipeline accuracy requires manual update of opportunity amounts when quotes change
- **Competitive Advantage Focus** - "Anything that can make us look like we're easy to do business with" (emphasis on customer experience)

---

## PART 2: COMPREHENSIVE DISCUSSION TOPICS

### TOPIC 1: TRANSACTION STRUCTURE & NUMBERING CONVENTION

**Context:** NetSuite uses Opportunity → Proposal → Sales Order → PO workflow (separate transactions), fundamentally different from your current Core single-transaction model. This is "like the one thing during discovery that people get tripped up on."

**What We Know:**
- NetSuite uses Opportunity → Proposal → Sales Order → PO workflow (separate transactions)
- Transaction prefixes decided: OP-/PROP-/SO-/DPO-/VPO-/INV-
- Project number stays consistent across all transactions
- One-click conversion between transaction types planned
- Global search works across all transaction types

**Discussion Points:**

1. **Project Number Format & Sequence**
   - What format for project numbers? (e.g., "KBMH-2025-####" or simpler?)
   - Starting sequence for 2025 and beyond?
   - How many projects anticipated annually? (sizing consideration)
   - Alphanumeric, numeric only, or with special characters?

2. **Transaction Number Sequences**
   - Starting numbers for each transaction type (suggest 1001+)?
   - Number length preference (5-digit, 6-digit, 8-digit)?
   - Combined sequence vs. separate sequences?
   - Gap management if sequences run together?

3. **User Communication & Training**
   - How to educate team on multiple transaction numbers?
   - Email/communication standards for referencing orders (use project number?)
   - Old habits: Memorizing single order number vs. new: Project number focus
   - Training timeline and approach?

4. **Navigation & Search Strategy**
   - How often will team search vs. receive links?
   - Preference: Global search vs. transaction navigation vs. recent items list?
   - Need for custom dashboards showing related transactions?
   - Saved searches for common queries?

5. **Customer Communication**
   - What number shown on quotes/proposals? (Transaction or Project?)
   - What number on invoices?
   - What number on order confirmations?
   - Customer expectations and communication strategy?

6. **CRM & Pipeline Management**
   - Will CRM (Opportunity) be actively used or just for linking?
   - Pipeline forecasting approach (forecast from Opportunity level)?
   - Manual update of opportunity amounts when quotes change?
   - Accuracy vs. effort trade-off decisions?

---

### TOPIC 2: APPROVAL WORKFLOW AUTOMATION & RULES ENGINE

**Context:** Currently manual approval workflows. NetSuite can automate based on configurable rules. Need to document exact rules and configure up to 10 approval rules for quotes and sales orders.

**What We Know:**
- Orders over $25K → Shannon approval
- Missing requirements (deposit/proposal/drawings/lookbook) → Matt approval
- Cumulative erosion >$1,500 → Matt email approval
- Shannon verifies order completeness
- All approvals currently manual
- No double order detection currently

**Discussion Points:**

1. **Approval Rule Details**
   - Exact order amount threshold for Shannon? ($25,000 confirmed?)
   - What constitutes "missing requirements"? (Specific list?)
   - Erosion calculation: Cumulative within what period? (Year-to-date? Rolling 12 months?)
   - Separate rules for Quotes vs. Sales Orders?

2. **Double Order Detection**
   - How to define "duplicate"? (Same $ within 30 days to same customer?)
   - Time window for duplicate detection? (30 days is that right?)
   - Alert recipients? (Shannon? Matt?)
   - Alert only or hard block?
   - False positive tolerance?

3. **Approval Routing & Escalation**
   - Current approval path: Proposal → Shannon → Matt?
   - Automatic escalation if no response? (Timeout period?)
   - Can approver approve or must escalate?
   - Email notifications for pending approvals?
   - Approval history tracking required?

4. **Vendor Credit Limit Warnings**
   - Warning threshold % (90%? 80%?)
   - Hard block if over limit or just warning?
   - Who receives alert? (Shannon? AP team? Matt?)
   - Alert method? (Email? Dashboard widget?)
   - How credit limits will be maintained (manual updates)?

5. **Approval Time Tracking & Reporting**
   - Report on average approval time by rule?
   - Individual approval time tracking needed?
   - Bottleneck identification?
   - SLA tracking (e.g., approval within 24 hours)?

6. **Margin Erosion Logic**
   - Is cumulative erosion calculation correct? ($500 + $1,000 more = $1,500 triggers?)
   - Erosion period? (Per quote? Year-to-date?)
   - Other margin thresholds beyond $1,500?
   - Different rules by order type or customer type?

7. **Special Approval Cases**
   - Government orders special approval rules?
   - Direct Bill orders special rules?
   - Large complex projects special handling?
   - Are there other approval scenarios we haven't documented?

---

### TOPIC 3: CUSTOMER PO TRACKING SOLUTION DESIGN

**Context:** HIGH PRIORITY custom solution. Identified as pain point causing payment delays. Bank requesting data. Solution is KBM-specific (won't go into standard Orion).

**What We Know:**
- Blanket POs received frequently
- No current tracking of PO utilization
- Risk of exceeding customer PO limits
- Causes payment delays and customer friction
- Bank requests: Total project value, POs against project, open balance
- Custom transaction planned with document attachment
- KPI dashboard needed with utilization tracking

**Discussion Points:**

1. **PO Tracking Record Structure**
   - Custom transaction or custom record?
   - Required fields: PO number, PO amount, PO date, customer, project, effective date?
   - Customer-provided document attachment capability?
   - Multiple currency support or USD only?
   - Status field (active, expired, full)?

2. **PO Value Tracking Calculation**
   - How to calculate utilization? (Sum of invoiced amounts / PO amount?)
   - Include only invoiced or also pending invoices?
   - Include change orders? (Yes/no?)
   - How to handle PO adjustments (customer increases PO amount)?
   - Automatic calculation or manual entry?

3. **Multiple PO Scenarios**
   - Can one project have multiple POs?
   - Can one PO cover multiple projects/orders?
   - What happens when customer adds money to existing PO?
   - How to track which PO applies to which invoice?
   - Priority when multiple POs exist (first-in-first-out)?

4. **Change Order Handling**
   - Are change orders on original PO or separate PO?
   - If not on PO: Include in utilization calculation or exclude?
   - If excluded: How tracked and reported?
   - Customer notification when approaching limit with change orders pending?

5. **Dashboard & Alert Requirements**
   - KPI dashboard displaying: Total PO value, Invoiced amount, Remaining balance, % utilized
   - Alert thresholds: 90% utilized? 100%? Custom?
   - Who receives alerts? (AR person? Matt? Finance?)
   - Frequency of alerts? (Real-time? Daily?)
   - How to prevent over-billing when PO approaching limit?

6. **User Workflow**
   - Who enters PO information? (AR person? Project coordinator?)
   - When is PO entered (upfront or as needed)?
   - How often updated? (Monthly? As invoiced?)
   - Can users override or adjust calculations?
   - Validation rules to prevent data errors?

7. **Bank Reporting**
   - Specific format required by bank?
   - Data elements needed: Project value, PO value, invoiced amount, balance?
   - Reporting frequency? (Monthly? Quarterly?)
   - Drill-down capability for bank review?

8. **Integration Points**
   - Link PO tracking record to Quote?
   - Link to Sales Order?
   - Link to Invoice?
   - Automatic calculations from invoices or manual?

---

### TOPIC 4: TAX MANAGEMENT & GOVERNMENT ORDER COMPLEXITY

**Context:** Tax management is complex with Miller Knoll direct bill orders requiring special handling. SuiteTax handles most cases, but government/direct bill orders need manual override. Government orders are 20% of business. Bank requesting proper documentation.

**What We Know:**
- 48 states with nexus
- SuiteTax automatic calculation by ship-to address
- Tax exemption certificate management with expiration tracking
- Government/Direct Bill orders: Tax to warehouse (Miller Knoll requirement) vs. final destination (standard practice)
- Current Core workaround: Manual address swap, calculation, override
- NetSuite tax override available but manual
- ~$1M direct bill revenue annually

**Discussion Points:**

1. **SuiteTax Configuration**
   - Tax profiles by state confirmed?
   - Tax rates updated annually or as needed?
   - Multi-state transactions handled correctly?
   - Tax exemption certificate configuration working as expected?

2. **Government Order Identification**
   - How to flag government orders in system?
   - Is Miller Knoll identified as specific customer type or order type?
   - Other government customers besides Miller Knoll?
   - Should system auto-flag for manual override?

3. **Tax Override Rules**
   - Trigger for override: Specific customer? Order type? Manual flag?
   - When is override decision made? (Proposal stage? SO stage?)
   - Who has authority to approve override? (Shannon? Matt? Finance?)
   - Audit trail for override decisions required?

4. **Warehouse vs. Final Destination**
   - Multiple warehouses with different tax rates?
   - Default warehouse for each region?
   - Can tax person determine warehouse vs. final destination?
   - Impact on total order cost (is warehouse tax materially higher)?

5. **Documentation & Audit Trail**
   - How to document why override was necessary?
   - Approval sign-off requirements?
   - Reporting for tax compliance audits?
   - Historical override tracking?

6. **Reporting & Compliance**
   - Gross receipts tax reporting by ship-to location?
   - Use tax reporting for IL/MO?
   - State-specific tax compliance requirements?
   - Annual tax return documentation needs?

---

### TOPIC 5: TEMPLATE MANAGEMENT & DOCUMENT REDESIGN

**Context:** All customer-facing and vendor-facing templates must be recreated in NetSuite. Current templates not provided. Vendor POs described as poor quality. Self-service template management without vendor billable hours required.

**What We Know:**
- All templates need recreation in NetSuite
- Self-service management (no vendor billable hours for changes)
- Version control and change documentation needed
- Vendor POs need redesign (currently "shitstorm of information")
- Templates not yet provided by Kipp
- Customer-facing templates project company image

**Discussion Points:**

1. **Current Templates & Issues**
   - What are main issues with current PO template?
   - Are there quote/proposal templates issues?
   - Invoice template issues?
   - Order confirmation/pick list issues?
   - Customer communication templates?

2. **Template Data Requirements**
   - What information appears on each template?
   - Mandatory vs. optional fields?
   - Formatting/calculation requirements?
   - Multi-page requirements?
   - Print vs. digital distribution?

3. **Template Customization by Type**
   - Separate templates for order types? (Direct Bill, Intermarket, Government, Intuit?)
   - Separate templates by customer? (Specific customer formatting needs?)
   - Separate templates by region or warehouse?
   - Template versioning strategy?

4. **Vendor-Facing Template (PO) Redesign**
   - What information makes current PO a "shitstorm"?
   - What information is critical for vendors?
   - What can be eliminated?
   - Miller Knoll specific requirements?
   - Other vendor requirements?

5. **Branding & Professional Appearance**
   - Company logo and branding standards?
   - Color scheme preferences?
   - Professional appearance requirements?
   - Customer messaging/language preferences?
   - Corporate identity guidelines?

6. **Self-Service Management**
   - How will users manage template changes?
   - Version control and approval process?
   - Documentation of change reasons?
   - Training on template management?

---

### TOPIC 6: ORDER TYPES, INTEGRATIONS & SPECIAL PROCESSING

**Context:** Multiple order types with special handling (Direct Bill, Intermarket, Government, Intuit), plus integration points (Miller Knoll ServiceNet, ServiceTime, Coupa email parsing). Need complete list and handling requirements.

**What We Know:**
- Direct Bill Orders (~$1M/year, 1% revenue) - Miller Knoll direct payment, commission kickback
- Intermarket Orders (outbound thousands/year, inbound ~40/year) - Dealers as vendor/customer, ServiceTime integration
- Government Orders (20% of business) - Special tax handling
- Intuit Work from Home Orders (high volume, separate reporting needed)
- Miller Knoll integration (ServiceNet, quote tool)
- ServiceTime integration for intermarket

**Discussion Points:**

1. **Complete Order Type List**
   - Are there other order types beyond Direct Bill, Intermarket, Government, Intuit?
   - Do these map to Orion order types or need customization?
   - Detailed requirements for each order type?
   - How to identify/flag each order type in system?

2. **Direct Bill Order Handling**
   - Order creation process (Opportunity → Quote → SO)?
   - Commission calculation: Gross up entire Miller Knoll amount with kickback?
   - Pricing: How to handle multi-tier pricing?
   - PO tracking for these orders?
   - Invoice generation and delivery process?

3. **Intermarket Order Handling**
   - Dealer setup as both vendor AND customer?
   - ServiceTime integration: How does it work?
   - What data flows through ServiceTime?
   - Bi-directional (order out and invoice back)?
   - Thousands/year volume: System performance considerations?

4. **Government Order Handling**
   - Tax override process? (See Topic 4)
   - Any other special handling beyond tax?
   - Margin requirements or constraints?
   - Approval workflow differences?
   - Reporting requirements?

5. **Intuit Work from Home Order Handling**
   - Currently coded as "e-commerce"?
   - Why separate reporting needed?
   - Order creation process?
   - Frequency and volume?
   - Integration with Intuit systems?

6. **Miller Knoll ServiceNet Integration**
   - Current status: Used today? Will be used?
   - What data integration needed?
   - Order creation from ServiceNet?
   - Invoice transmission back to ServiceNet?
   - Timing: Phase 1 or later phase?

7. **Coupa Email Parsing Evaluation**
   - Current status: Under evaluation?
   - What would email parsing automate?
   - Which order types?
   - Bi-directional integration needed?
   - ROI vs. effort?

8. **Integration Timeline & Phasing**
   - Phase 1 implementation scope?
   - What integrations in Phase 1?
   - What integrations in Phase 2+?
   - Dependencies between integrations?
   - Risk mitigation for complex integrations?

---

### TOPIC 7: TIERED PRICING CHALLENGE & MILLER KNOLL RESOLUTION

**Context:** Miller Knoll has multi-tier contracts recognized by contract number, not project number. This is escalation item with Dustin (Miller Knoll product owner). Need confirmation that NetSuite/Orion can link project numbers to tiered pricing contracts.

**What We Know:**
- Miller Knoll tiered pricing by contract number
- Project number may not align with contract number
- Current system recognizes pricing by contract
- Need to confirm NetSuite approach
- Escalation to Dustin (Miller Knoll) needed
- This is pre-design phase dependency

**Discussion Points:**

1. **Tiered Pricing Structure**
   - How many tier levels? (2? 3? More?)
   - What determines tier? (Annual volume? Customer class? Duration?)
   - Tier pricing updates frequency?
   - Retroactive tier application or prospective?

2. **Contract Number to Project Number Linking**
   - How are contracts identified in current system?
   - Can project number be linked to contract number?
   - Will Dustin/Miller Knoll support this linkage?
   - Data integration needed between systems?

3. **Pricing Inheritance**
   - How does tiered pricing apply to project orders?
   - Automatic pricing lookup or manual selection?
   - Can pricing be overridden at project level?
   - Audit trail for pricing decisions?

4. **Dustin Coordination**
   - Has Miller Knoll been briefed on this requirement?
   - What questions does Dustin need answered?
   - Timeline for Miller Knoll confirmation?
   - ServiceNet integration dependency?

5. **System Configuration Approach**
   - Custom fields to link contracts to projects?
   - Standard NetSuite tiered pricing features?
   - Orion-specific tiered pricing capability?
   - Configuration options and trade-offs?

6. **Fallback If Not Supported**
   - Is manual pricing entry acceptable?
   - Workaround if automatic pricing not available?
   - Risk mitigation strategy?

---

### TOPIC 8: SPECIFICATION & BOM MANAGEMENT STRATEGY

**Context:** SIF import with 60-column mapping already planned. XML import capability for vendor specs needed. Catalogs not yet available in NetSuite (will be addressed in future phase). Need to finalize current state approach and plan for catalog availability.

**What We Know:**
- SIF import with 60-column mapping (Smart Table)
- XML import rare but used for vendor specs
- Specification external tools (Project Spec, CET/Configura, CAP Worksheets)
- Catalogs not available in NetSuite yet
- Tag handling (floor, room, chair tag, etc.) as separate fields
- Specification complete before proposal created

**Discussion Points:**

1. **SIF Import Configuration**
   - SIF import already tested in Orion?
   - 60-column mapping correct and complete?
   - Column mapping: Any custom or specialized mappings?
   - Data validation during import?
   - Error handling for bad data?

2. **XML Import Requirements**
   - Example XML templates available from vendors?
   - Can Matt provide sample Excel export as XML?
   - Frequency of XML imports?
   - Which vendors provide XML quotes?
   - Custom mapping requirements?

3. **Custom Tag Handling**
   - Current tags beyond standard fields?
   - How many custom tags?
   - Examples: Floor, Room, Chair tag, etc.?
   - Add more custom fields or use standard structure?

4. **Specification Tools Integration**
   - Are external tools (Project Spec, CET, CAP Worksheets) used in all projects or sometimes?
   - Data flow from tools to NetSuite/Orion?
   - Export format from tools (SIF? XML? Other)?
   - Users comfortable with current tools?

5. **Catalog Availability Timeline**
   - When will catalogs be available in NetSuite?
   - Phase 1 or later?
   - Interim workaround strategy (external tools)?
   - What needs to happen before catalogs available?

6. **BOM Validation**
   - Data validation rules during import?
   - Error messages and handling?
   - Duplicate detection?
   - Out-of-stock or unavailable item handling?

7. **User Training**
   - Are users comfortable with SIF import process?
   - XML import training needed?
   - Error resolution process?
   - Best practices documentation?

---

## PART 3: OUTSTANDING DECISIONS REQUIRED

The following strategic decisions are pending and need to be made during this session to proceed with configuration:

### DECISION 1: Tiered Pricing Miller Knoll Confirmation
**Decision Maker:** Marcus/GSI with Dustin (Miller Knoll)  
**Impact:** High - Affects pricing accuracy and margin calculations  
**Status:** Escalation required to Dustin for confirmation of project-level recognition

**Options:**
1. **Miller Knoll supports project-level tiered pricing** - Automatic pricing lookup possible
2. **Manual pricing entry required** - Workaround approach needed

---

### DECISION 2: Customer PO Tracking Solution - Custom Transaction vs. Record
**Decision Maker:** Matt/Shannon/Finance Lead  
**Impact:** Medium - Affects workflow and reporting  
**Status:** Design session required to finalize structure

**Options:**
1. **Custom Transaction** - More integrated, appears in transaction list
2. **Custom Record** - More flexible, separate from transaction processing

---

### DECISION 3: Coupa Email Parsing Automation
**Decision Maker:** Matt/Operations  
**Impact:** Medium - User experience and efficiency  
**Status:** Under evaluation

**Options:**
1. **Implement email parsing automation** - Automate order creation from emails
2. **Skip automation** - Manual order entry continues

---

### DECISION 4: Intuit Work from Home Order Type Configuration
**Decision Maker:** Operations/Matt  
**Impact:** Low-Medium - Reporting and process separation  
**Status:** Requires detailed requirements gathering

**Options:**
1. **Separate order type** - Distinct reporting and handling
2. **Continue as e-commerce** - Use existing order type

---

## PART 4: PRE-WORK & PREPARATION

To make the most of this comprehensive session, please prepare the following:

### Transaction Structure Topic:
- [ ] Confirm project number format and starting sequence preference
- [ ] Confirm transaction number starting sequences
- [ ] Identify any other transaction types beyond OP/PROP/SO/DPO/VPO/INV
- [ ] Gather examples of how orders are currently referenced in emails/documents

### Approval Workflow Topic:
- [ ] Confirm exact approval thresholds ($25K for Shannon?)
- [ ] List specific "missing requirements" that trigger Matt approval
- [ ] Clarify erosion calculation details ($500 + $1,000 = $1,500 trigger?)
- [ ] Define any other approval scenarios beyond documented rules
- [ ] Identify approval rule recipients and notification preferences

### Customer PO Tracking Topic:
- [ ] Examples of recent PO tracking issues
- [ ] Sample customer POs to understand structure
- [ ] Bank requirements for PO reporting
- [ ] Current workarounds and pain points
- [ ] Multi-PO scenario examples

### Tax Management Topic:
- [ ] Current tax override examples
- [ ] Miller Knoll tax handling documentation
- [ ] Government order customer list
- [ ] Regional tax requirements and variations
- [ ] Tax compliance reporting needs

### Template Topic:
- [ ] All current templates (proposals, quotes, POs, invoices, confirmations)
- [ ] Customer/vendor feedback on current templates
- [ ] Specific issues with vendor PO template
- [ ] Branding and logo standards
- [ ] Any industry-specific template requirements

### Order Types Topic:
- [ ] Complete list of order types
- [ ] Current order type volumes and frequencies
- [ ] Special handling requirements for each type
- [ ] Integration points and timelines
- [ ] Reporting requirements by order type

### Tiered Pricing Topic:
- [ ] Current tiered pricing structure and examples
- [ ] Contract number samples
- [ ] Pricing tier matrix
- [ ] Confirm Dustin (Miller Knoll) availability

### Specification/BOM Topic:
- [ ] Sample SIF files with column mappings
- [ ] Sample XML imports from vendors
- [ ] Catalog structure understanding
- [ ] Custom tag list and examples
- [ ] Specification workflow examples

---

## PART 5: SESSION DELIVERABLES & SUCCESS CRITERIA

At the completion of this comprehensive follow-up session, we will have:

### Documentation Deliverables:
1. **Transaction Structure & Numbering Document** - Format specifications, sequences, navigation guidelines
2. **Approval Workflow Rules Documentation** - All approval rules, thresholds, and logic configured
3. **Customer PO Tracking Solution Design** - Complete specification for custom solution
4. **Tax Management Procedures** - Override rules, compliance, and documentation approach
5. **Template Specifications** - All templates designed, reviewed, and ready for implementation
6. **Order Type Configuration Guide** - All order types documented with special handling
7. **Tiered Pricing Implementation Plan** - Dustin confirmation and NetSuite configuration approach
8. **Specification/BOM Import Procedures** - SIF and XML import processes documented

### Decisions Finalized:
- [ ] Tiered pricing approach confirmed with Miller Knoll (Dustin)
- [ ] PO tracking solution structure selected (custom transaction vs. record)
- [ ] Coupa email parsing automation decision made
- [ ] Intuit Work from Home order type configuration approach determined

### Requirements Confirmed:
- [ ] Transaction numbering and project number format approved
- [ ] All approval rule thresholds validated
- [ ] PO tracking requirements and workflow approved
- [ ] Tax override rules and procedures confirmed
- [ ] All templates reviewed and redesign approach approved
- [ ] Order type handling procedures confirmed
- [ ] Specification/BOM import requirements finalized

### Implementation Impact Assessed:
- [ ] Custom development scope identified (PO tracking, approval rules, integrations)
- [ ] User training requirements identified by topic
- [ ] Change management plan for new transaction structure
- [ ] Data migration impact (if any) assessed
- [ ] Integration timeline and phasing confirmed

---

## PART 6: NEXT STEPS AFTER SESSION

Once this comprehensive follow-up session is complete:

1. **Update Business Requirements Document (BRD)** - Incorporate all clarifications and decisions
2. **Finalize Requirements Map** - Confirm ALIGNS/ADAPT/ACCOMMODATE classifications
3. **Solution Design Phase** - Begin detailed design for ACCOMMODATE requirements (custom development)
4. **Template Design & Approval** - Finalize template designs with stakeholders
5. **Approval Workflow Configuration** - Configure up to 10 approval rules in NetSuite
6. **PO Tracking Solution Development** - Begin custom development for PO tracking
7. **Integration Planning** - Detailed planning for Miller Knoll, ServiceTime, Coupa integrations
8. **User Training Plan Development** - Identify training needs based on requirements
9. **Go-Live Planning** - Incorporate all decisions into go-live approach and timeline

---

## APPENDIX: REFERENCE MATERIALS

### Related Documents:
- **Questionnaire_OrderManagement_v1.0.md** - Comprehensive questionnaire with 43 requirements
- **Requirements_Map_OrderManagement_v1.0.md** - Requirements classified by implementation approach
- **Master_Transcript_OrderManagement.md** - Full transcript from discovery sessions
- **GapAnalysis_OrderManagement.md** - Gap analysis from discovery

### Key Requirements Requiring Follow-Up:
- **REQ-001:** Separate transactions workflow (ADAPT) - Topic 1
- **REQ-016-018:** Customer PO tracking (ACCOMMODATE) - Topic 3
- **REQ-020-026:** Approval workflow rules (ACCOMMODATE) - Topic 2
- **REQ-029-030:** Template recreation/redesign (ACCOMMODATE) - Topic 5
- **REQ-043:** Tiered pricing escalation (FUTURE) - Topic 7

### Contact Information:
- **Primary Contact:** Shannon (Order Manager/Approvals)
- **Strategic Contact:** Matt (Leadership/Operations)
- **Technical Contact:** Kipp (IT/Integration)
- **GSI Lead:** Marcus (Implementation Lead)
- **Miller Knoll Liaison:** Dustin (for tiered pricing coordination)

---

**Document Version:** 2.0  
**Created:** October 2025  
**Updated:** After consolidation decision  
**Status:** Ready for comprehensive single session scheduling

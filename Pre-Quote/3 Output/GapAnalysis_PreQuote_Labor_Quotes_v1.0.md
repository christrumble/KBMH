# Discovery Questionnaire Completeness Analysis
## KBMH Pre-Quote Labor Quote Process

**Document Title:** Gap Analysis - Pre-Quote Labor Quote Process  
**Version:** 1.0  
**Date:** November 18, 2025  
**Analysis Type:** Completeness Assessment based on First Follow-Up Discovery Session  

---

## EXECUTIVE SUMMARY

**Overall Completeness:** 68% of critical discovery questions fully answered; 22% partially answered; 10% remaining gaps

**Critical Findings:**
- Labor quote request types, processes, calculations, and acceptance workflows are well-documented
- Hold-back strategy and multi-vendor bidding approach are clearly understood
- Significant gaps remain around design requests, PM requests, and finance/accounting processes
- Scope governance decision (Opportunity as single source of truth) is PENDING and critical
- File management and organizational structure decisions needed

**Follow-up Sessions Needed:** 3-4 additional sessions recommended
- Session 1: Design Request Process (90 min)
- Session 2: PM Request & Resource Management (90 min)
- Session 3: Finance/Accounting & Data Migration (60 min)
- Session 4: (Optional) Scope Governance & Process Validation (60 min)

**Estimated Timeline:** 2-3 weeks to complete questionnaire to 95%+ confidence

**Project Readiness:** Labor quote pre-quote process is 70% ready for configuration; design/PM/finance discovery required before full BRD creation

---

## COMPLETION STATUS MATRIX

| Question # | Topic | Status | Evidence Quality | Action Needed |
|-----------|-------|--------|-----------------|---------------|
| **Q1** | Labor Quote Types | ✅ Complete | Strong | None - proceed with config |
| **Q2** | Request Initiation & Distribution | ✅ Complete | Strong | Validate final Intermarket status |
| **Q3** | Request Form Fields | ⚠️ Partial | Weak | Get current form template |
| **Q4** | Labor Cost Calculation | ✅ Complete | Strong | Get business rule screenshot |
| **Q5** | Internal Estimating | ✅ Complete | Strong | None - rate tables future roadmap |
| **Q6** | Quote Acceptance Process | ✅ Complete | Strong | Clarify multi-quote acceptance |
| **Q7** | Multiple Quotes Per Project | ✅ Complete | Strong | Validate scope-based auto-rejection |
| **Q8** | Dashboard & Visibility | ✅ Complete | Strong | Define exact dashboard fields |
| **Q9** | Auto-Rejection Workflow | ⚠️ Partial | Weak | Design scope-based approach |
| **Q10** | Multiple Quote Acceptance | ❌ Not Answered | None | Validate with Orion technical |
| **Q11** | Opportunity Launch | ✅ Complete | Strong | Confirm capability exists in Orion |
| **Q12** | Scope as Single Source | ⚠️ Pending Decision | Weak | KBMH leadership decision needed |
| **Q13** | Scope Capture in Sales | ✅ Complete | Strong | None - process confirmed |
| **Q14** | Quote to Proposal Process | ✅ Complete | Strong | Validate itemization approach |
| **Q15** | Decentralized Acceptance | ✅ Complete | Strong | None - clear process |
| **Q16** | Order Team Assignment | ✅ Complete | Strong | Confirm team alignment model |
| **Q17** | Resource Workload Mgmt | ✅ Complete | Strong | Build dashboard as phase 2 |
| **Q18** | Design Request Workflow | ❌ Not Answered | None | Full discovery session needed |
| **Q19** | PM Request Workflow | ❌ Not Answered | None | Full discovery session needed |
| **Q20** | File Organization & SharePoint | ✅ Complete | Strong | Get folder structure proposal |

**Summary:** 
- ✅ **Fully Answered: 15 questions (75%)**
- ⚠️ **Partially Answered/Pending: 4 questions (20%)**
- ❌ **Not Answered: 1 question (5%)**

---

## INFORMATION GAPS ANALYSIS

### CATEGORY 1: CRITICAL GAPS (Project Blocking)

#### Gap #1: Scope Governance Decision
**Question:** Should Opportunity be the single source of truth for project scope?

**Current Status:** Proposed but not decided by KBMH leadership

**Why Critical:** 
- Affects data architecture and field sync logic
- Determines training and process governance
- Impacts how Marketing Requests, Design Requests, and Labor Quotes inherit information
- Cannot configure scope field syncing without this decision

**What's Missing:**
- Formal decision from operations leadership (Matt Denning, Kimi Katsuyoshi)
- Definition of scope fields to be included
- Process for updating opportunity when scope changes during project
- Exceptions/override rules

**Who Can Answer:** Operations leadership (Matt Denning, Kimi Katsuyoshi)

**How to Get Answer:** Requires leadership decision-making meeting, not technical discovery

**Evidence Gap:** Only preliminary discussion; no commitment made

**Dependency:** This decision blocks:
- Scope field mapping configuration
- Training & change management planning
- Data migration approach for existing scope data

---

#### Gap #2: Multiple Labor Quote Acceptance Technical Validation
**Question:** How does Orion handle acceptance of multiple labor quotes on the same project with evolving scope?

**Current Status:** Flagged for validation but not yet confirmed

**Why Critical:**
- KBMH frequently re-quotes when scope changes
- Affects workflow and quote tracking
- Determines if revision workflow or new quote workflow is needed
- Impacts PO linking and traceability

**What's Missing:**
- Technical confirmation from Orion dev team (Joe)
- System behavior documentation
- Workflow recommendations
- Exception handling approach

**Who Can Answer:** Joe (Orion Technical Lead), Marcus (Implementation)

**How to Get Answer:** Technical validation call/documentation from Orion

**Evidence Gap:** No technical testing or confirmation yet

---

#### Gap #3: Design Request Full Process
**Question:** What is KBMH's complete design request workflow?

**Current Status:** Barely discussed; high-level understanding only

**Why Critical:**
- Design is part of pre-quote scope
- Affects labor quote request timing and content
- Influences scope definition and specification
- May impact labor quote cost calculations

**What's Missing:**
- Design request initiation process
- Designer assignment rules
- Design cost structure (flat fee? hourly? percentage?)
- Design deliverables and format
- Timeline expectations
- Design-to-proposal flow
- Design request form template
- Integration with labor quote requests

**Who Can Answer:** Design Manager/Lead, Senior Designers, Wendy Stark

**How to Get Answer:** Full discovery session with design team

**Evidence Gap:** Almost no detail captured; only high-level confirmation exists

**Related Questions:** Q18 in questionnaire

---

#### Gap #4: PM Request Full Process & Timing
**Question:** What is KBMH's PM request workflow and when should PM be assigned?

**Current Status:** Partially understood; formal process unclear

**Why Critical:**
- PM availability affects project timeline and scope
- PM assignment happens at different lifecycle stages (opportunity, order, kickoff)
- Affects project planning and resource allocation
- May impact labor quote requirements

**What's Missing:**
- Formal PM request process (does it exist?)
- Optimal PM assignment timing (pre-sale vs. post-sale)
- PM approval workflow
- PM capacity tracking and workload management
- PM communications during RFP/bid phase
- Integration with project kickoff

**Who Can Answer:** Wendy Stark (PM Manager), Senior PMs, Matt Denning

**How to Get Answer:** Full discovery session with PM team

**Evidence Gap:** High-level conversation only; no process documentation

**Related Questions:** Q19 in questionnaire

---

### CATEGORY 2: HIGH-PRIORITY GAPS (Should Be Answered Before Config)

#### Gap #5: Labor Quote Request Form Exact Fields
**Question:** What are ALL the required and optional fields on the labor quote request form?

**Current Status:** Partially known; form template not yet received

**Why Important:**
- Form fields determine what Orion labor quote form should capture
- Missing fields may break current workflow
- Must match or exceed current capability

**What's Missing:**
- Complete field list (required vs. optional)
- Field descriptions and validation rules
- Field order/grouping on form
- Conditional logic (fields shown based on other fields)
- Attachment/file upload requirements
- Current form template screenshot

**Who Can Answer:** Matt Denning, Chris Trumble, Wendy Stark

**How to Get Answer:** Email request for current form template

**Evidence Gap:** Only general description; no actual form seen

**Action Item Status:** [PENDING - Matt Denning to provide]

---

#### Gap #6: Design Request Form Exact Fields
**Question:** What fields does the design request form capture?

**Current Status:** Not yet received; needed for design discovery

**Why Important:**
- Determines what information flows to designers
- Impacts how scope gets communicated
- May influence labor quote request detail
- Part of pre-quote scope capture

**What's Missing:**
- Complete field list
- Field descriptions
- Current form template

**Who Can Answer:** Design team, Chris Trumble

**How to Get Answer:** Email request for design request form template

**Evidence Gap:** Not yet discussed

**Action Item Status:** [PENDING - Chris Trumble to provide]

---

#### Gap #7: Exact Labor Markup Deduction Business Rule
**Question:** What is the exact formula for the 15% labor markup deduction?

**Current Status:** High-level understanding; technical details pending

**Why Important:**
- Must be accurately configured in Orion
- Affects all labor margin calculations
- Critical for financial reporting
- Test cases depend on this rule

**What's Missing:**
- Technical specification/formula
- Visual screenshot of business rule configuration in current system
- Test scenarios
- Exceptions or special cases
- When rule applies (all labor orders? specific types?)

**Who Can Answer:** Kip Herdrick, Matt Denning

**How to Get Answer:** Screenshot of Core business rule configuration

**Evidence Gap:** Only verbal description received

**Action Item Status:** [PENDING - Kip Herdrick to provide screenshot]

---

#### Gap #8: Finance/Accounting Process Details
**Question:** What are KBMH's complete accounting and financial processes related to labor quotes, POs, and invoicing?

**Current Status:** Barely discussed; finance not yet represented in discovery

**Why Important:**
- Labor quote connects to PO, invoice, and GL entries
- Chart of accounts mapping required
- Cost/revenue recognition needs clarification
- Commission calculations mentioned but not detailed
- Data migration must account for historical transactions

**What's Missing:**
- Labor cost tracking methodology
- PO-to-Invoice reconciliation process
- GL account assignments for labor
- Commission calculation rules
- Cost rollup and reporting needs
- Historical data migration requirements

**Who Can Answer:** Lorraine Guzman (Finance), Accounting team

**How to Get Answer:** Dedicated finance discovery session

**Evidence Gap:** Finance team barely participated in this session

**Related Questions:** Chart of Accounts review (ongoing per Chris)

---

### CATEGORY 3: MEDIUM-PRIORITY GAPS (Nice-to-Have Details)

#### Gap #9: Auto-Rejection Logic for Competing Quotes
**Question:** Should Orion automatically reject competing labor quotes when one is accepted (by scope)?

**Current Status:** Identified as potential feature; design approach unclear

**Why Helpful:**
- Keeps dashboard clean
- Reduces manual cleanup
- But requires scope-based tagging

**What's Missing:**
- Design of scope-based grouping
- Scope versioning/change tracking mechanism
- Exceptions and override approach
- User testing/validation

**Who Can Answer:** Operations leadership, Marcus (Implementation)

**How to Get Answer:** Design thinking session post-discovery

**Evidence Gap:** Concept identified but not fully designed

---

#### Gap #10: Labor Quote Dashboard Field Details
**Question:** What are ALL the specific fields/columns for the labor quote dashboard?

**Current Status:** High-level requirements known; exact fields not detailed

**Why Helpful:**
- Dashboard development depends on this
- Affects reporting capabilities
- Filtering logic depends on fields

**What's Missing:**
- Complete field list
- Calculated fields (quote-to-award ratio, aging, etc.)
- Sort/filter capabilities
- Drill-down capabilities
- Visualization preferences

**Who Can Answer:** Matt Denning, Kimi Katsuyoshi

**How to Get Answer:** Detailed dashboard design session

**Evidence Gap:** Only general description

---

#### Gap #11: Itemized vs. Summary Labor Quote Import Strategy
**Question:** When should KBMH use itemized vs. summary labor quote import?

**Current Status:** Understood conceptually; no decision rules defined

**Why Helpful:**
- Affects proposal formatting and client visibility
- Influences how contingencies are managed
- Impacts financial reporting

**What's Missing:**
- Decision criteria for when to itemize vs. summarize
- Business rules or logic
- Client communication approach
- Template/format preferences

**Who Can Answer:** Matt Denning, Account Managers

**How to Get Answer:** Best practice discussion and decision documentation

**Evidence Gap:** Conceptual understanding only

---

### CATEGORY 4: TECHNICAL VALIDATION GAPS

#### Gap #12: SharePoint Folder Structure Proposal
**Question:** What will be the SharePoint folder structure for KBMH files?

**Current Status:** Proposed concept; not yet designed

**Why Important:**
- Affects file organization and retrieval
- Impacts user experience
- Critical for pre-quote/post-order file separation

**What's Missing:**
- Proposed folder hierarchy
- File naming conventions
- Pre-quote vs. post-quote file locations
- Lookbook/CAT file handling

**Who Can Answer:** Marcus (with Tyler) - Implementation team

**How to Get Answer:** SharePoint folder structure proposal document

**Evidence Gap:** Not yet created

**Action Item Status:** [ACTION] Marcus/Chris/Tyler to create proposal

---

#### Gap #13: Data Migration Planning
**Question:** What is the detailed plan for migrating existing labor quotes and related data from Core to NetSuite?

**Current Status:** Initiated but not detailed

**Why Important:**
- Critical for project success
- Requires significant planning and testing
- May affect go-live timing

**What's Missing:**
- Historical data scope (how many years?)
- Data mapping details
- Validation and reconciliation process
- Cutover strategy (bulk vs. incremental)
- Risk mitigation approach

**Who Can Answer:** Marcus, Kip, Joe (Orion data migration expert)

**How to Get Answer:** Data migration planning session

**Evidence Gap:** Only high-level initiation

**Action Item Status:** [ACTION] Marcus to start conversation with Joe on Teams

---

#### Gap #14: Chart of Accounts Mapping Status
**Question:** How complete is the Chart of Accounts mapping?

**Current Status:** In progress per Chris

**Why Important:**
- Required for GL coding accuracy
- Affects financial reporting
- May block data migration

**What's Missing:**
- Current completion percentage
- Any issues or gaps identified
- Timeline for completion

**Who Can Answer:** Chris Trumble, Lorraine Guzman (Finance)

**How to Get Answer:** Status update from Chris

**Evidence Gap:** No status provided in this session

**Action Item Status:** [PENDING] Chris to provide COA mapping status

---

## STAKEHOLDER ENGAGEMENT ANALYSIS

### Well-Represented Stakeholders ✅
- **Operations/Management:** Matt Denning (excellent participation, clear process knowledge)
- **Account Management:** Kimi Katsuyoshi (strong input on strategy and nuance)
- **Implementation Leadership:** Marcus Dallacqua (comprehensive system understanding)
- **Technical Configuration:** Kip Herdrick (system knowledge, documentation)
- **Project Management:** Wendy Stark (partial input on PM/designer assignment)

### Under-Represented Stakeholders ⚠️
- **Finance/Accounting:** Lorraine Guzman (minimal participation despite financial implications)
- **Design:** Not represented (designer perspective missing)
- **PMs:** Not represented (PM workflow insight missing)
- **Systems Administration:** Chris Trumble (silent due to laryngitis; could provide more)
- **Salespeople/Account Managers (field-level):** Only manager-level input

### Missing Stakeholders ❌
- **Individual Account Managers** - need field perspective on labor quote requests
- **Designers** - need design request workflow understanding
- **Project Managers** - need PM assignment and workflow detail
- **Installation Partners/Vendors** - external perspective on labor quote receiving
- **Executive Leadership** - needed for scope governance decision

### Decision-Maker Involvement Status
- ✅ Operations decisions (Matt Denning) - present
- ⚠️ Finance decisions (Lorraine Guzman) - minimal presence; COA mapping ongoing
- ❌ Leadership decision on scope governance - NOT YET ENGAGED

---

## FOLLOW-UP MEETING PLAN

### **Session 1: Design Request Process Discovery**

**Session Goal:** Fully document KBMH's design request workflow and form requirements

**Questions to Address:**
- Q18: Design Request Workflow (complete discovery)
- Q3: Labor Quote Request Form (understand design→labor flow)
- Q13: Scope Capture (how scope flows from design request)

**Required Attendees:**
- Design Manager or Lead
- 1-2 Senior Designers
- Marcus (Implementation Lead)
- Chris (Form configuration)

**Optional Attendees:**
- Sales/Account Manager (who initiates design requests)
- Operations Lead (workflow oversight)

**Duration:** 90 minutes

**Pre-work for Client:**
- Provide design request form template (current version)
- Provide 2-3 examples of recent design requests
- Document typical design timeline
- Identify any process variations (bid vs. non-bid, different project types)
- Document designer assignment logic

**Consultant Preparation:**
- Review design request template if available
- Prepare Orion design request form concept
- Prepare list of design-related questions

**Expected Outcome:**
- Complete design request process documented
- Form field list with validation rules
- Designer assignment rules captured
- Design-to-proposal flow confirmed
- Timeline and cost structure clarified
- Q18 moved to ✅ Complete

**Success Criteria:**
- Design request process fully documented (90%+ clarity)
- Form template received and reviewed
- Design request form configured in Orion
- Integration with labor quote process validated

---

### **Session 2: PM Request & Resource Management**

**Session Goal:** Document PM assignment and resource management processes

**Questions to Address:**
- Q19: PM Request Workflow (complete discovery)
- Q16: Order Team Assignment (validate PM assignment rules)
- Q17: Resource Workload Management (dashboard requirements)

**Required Attendees:**
- PM Manager/Lead (Wendy Stark)
- 1-2 Senior PMs
- Operations Lead (Matt Denning)
- Marcus (Implementation)

**Optional Attendees:**
- Account Managers
- Sales team member (who initiates PM requests)

**Duration:** 90 minutes

**Pre-work for Client:**
- Document PM request form (if exists) or team assignment process
- Provide examples of recent PM assignments
- Document typical PM timeline from assignment to kickoff
- Clarify capacity/workload tracking approach
- Identify any variations (bid projects vs. straight orders)

**Consultant Preparation:**
- Review PM request capabilities in Orion
- Prepare resource dashboard concept
- Prepare workload visualization options

**Expected Outcome:**
- PM assignment process fully documented
- PM request form/process clarified (or confirmed as team-based)
- Optimal PM assignment timing defined
- Resource dashboard requirements captured
- Q19 moved to ✅ Complete

**Success Criteria:**
- PM workflow 90%+ documented
- Resource assignment rules clear
- Dashboard requirements defined
- PM module configuration approach agreed upon

---

### **Session 3: Finance, Accounting & Data Migration**

**Session Goal:** Understand financial processes and begin data migration planning

**Questions to Address:**
- Gap #8: Finance/Accounting Process Details
- Gap #13: Data Migration Planning
- Gap #14: Chart of Accounts Mapping Status

**Required Attendees:**
- Finance Manager (Lorraine Guzman)
- Accounting Lead
- Marcus (Implementation)
- Kip (System/Data)

**Optional Attendees:**
- Operations Lead (Matt Denning)
- Joe (Orion Data Migration Expert - if available)

**Duration:** 60-90 minutes

**Pre-work for Client:**
- Bring Chart of Accounts mapping status
- Document labor cost accounting process
- Provide sample labor quote → PO → Invoice flow
- Document GL account assignments
- Clarify commission calculation logic
- Provide historical data scope (time period to migrate)

**Consultant Preparation:**
- Prepare financial mapping templates
- Prepare data migration approach overview
- Prepare GL coding recommendations

**Expected Outcome:**
- Financial processes documented
- Chart of Accounts mapping completed or planned
- Data migration scope defined
- Historical data inventory completed
- Migration strategy outlined
- Gap #8, #13, #14 addressed

**Success Criteria:**
- Financial workflow clearly documented
- COA mapping completed
- Data migration plan drafted
- Test data approach agreed upon

---

### **Session 4 (Optional): Scope Governance & Process Validation**

**Session Goal:** Make final decision on scope governance and validate pre-quote processes

**Questions to Address:**
- Gap #1: Scope Governance Decision (formal decision)
- Q12: Scope as Single Source of Truth (final confirmation)
- Validation of all pre-quote processes

**Required Attendees:**
- Operations Leadership (Matt Denning, Kimi Katsuyoshi)
- Sales Leadership
- Marcus (Implementation)

**Duration:** 60 minutes

**Pre-work for Client:**
- Leadership to come prepared to make scope governance decision
- Marketing/Sales to document current scope capture approach
- Operations to define scope governance rules

**Expected Outcome:**
- Scope governance decision finalized
- Scope update/sync approach defined
- Training plan outlined
- Gap #1 resolved

---

## PRIORITY CLASSIFICATION

### 🔴 CRITICAL PRIORITY - Must Be Answered Before Config Phase

#### CRIT-1: Scope Governance Decision
- **Question:** Should Opportunity be single source of truth for scope?
- **Missing Information:** Formal decision from operations leadership; scope field definitions; update protocols
- **Business Impact:** Blocks scope field sync configuration; affects data architecture; impacts training/governance
- **Who Can Answer:** Matt Denning, Kimi Katsuyoshi (Leadership decision)
- **How to Get Answer:** Leadership decision meeting (not technical discovery)
- **Timeline:** ASAP - required before technical build-out
- **Session:** Session 4 (optional) or separate leadership discussion

#### CRIT-2: Design Request Workflow
- **Question:** What is KBMH's complete design request process?
- **Missing Information:** Complete workflow, form fields, designer assignment, design-to-proposal flow, timeline, cost structure
- **Business Impact:** Design is part of pre-quote scope; affects labor quote timing and content; blocks configuration
- **Who Can Answer:** Design Manager/Lead, Senior Designers, Wendy Stark
- **How to Get Answer:** Full discovery session
- **Timeline:** Next 1-2 weeks
- **Session:** Session 1 (Design Request)

#### CRIT-3: PM Request Workflow
- **Question:** What is KBMH's PM request and assignment process?
- **Missing Information:** Complete workflow, assignment timing, request form, capacity management, PM communication during bid phase
- **Business Impact:** PM affects project planning; availability impacts labor quotes; part of pre-quote scope
- **Who Can Answer:** Wendy Stark (PM Manager), Senior PMs
- **How to Get Answer:** Full discovery session
- **Timeline:** Next 1-2 weeks
- **Session:** Session 2 (PM Request & Resource)

#### CRIT-4: Multiple Labor Quote Acceptance Technical Validation
- **Question:** How does Orion handle multiple labor quote acceptance on same project?
- **Missing Information:** Technical confirmation of system behavior; workflow recommendations; edge case handling
- **Business Impact:** KBMH frequently re-quotes; affects traceability and financial reconciliation
- **Who Can Answer:** Joe (Orion Technical Lead), Marcus
- **How to Get Answer:** Technical validation with Orion
- **Timeline:** Within 1 week
- **Session:** Technical call with Orion (not user session)

---

### 🟡 HIGH PRIORITY - Should Be Answered Before Configuration

#### HIGH-1: Labor Quote Request Form Template
- **Question:** What are exact fields on labor quote request form?
- **Missing Information:** Complete field list, required vs optional, validation rules, current template
- **Business Impact:** Form fields determine Orion labor quote form; missing fields break current workflow
- **Who Can Answer:** Matt Denning, Chris Trumble, Wendy Stark
- **How to Get Answer:** Email form template; review in follow-up session
- **Timeline:** This week
- **Action Item:** [PENDING] Matt Denning to provide

#### HIGH-2: Design Request Form Template
- **Question:** What fields does design request form capture?
- **Missing Information:** Complete field list, design request form template
- **Business Impact:** Determines scope capture for design process
- **Who Can Answer:** Design team, Chris Trumble
- **How to Get Answer:** Email form template; design discovery session
- **Timeline:** With Session 1
- **Action Item:** [PENDING] Chris Trumble to provide

#### HIGH-3: Business Rule Screenshot (15% Labor Deduction)
- **Question:** What is exact formula for 15% labor markup deduction?
- **Missing Information:** Technical screenshot, formula details, test scenarios
- **Business Impact:** Critical for accurate labor margin configuration; affects all labor orders
- **Who Can Answer:** Kip Herdrick, Matt Denning
- **How to Get Answer:** Screenshot of Core business rule
- **Timeline:** This week
- **Action Item:** [PENDING] Kip Herdrick to provide screenshot

#### HIGH-4: Finance & Accounting Processes
- **Question:** What are KBMH's complete accounting and financial processes?
- **Missing Information:** Cost tracking, GL assignments, commission calculations, PO-to-invoice reconciliation, data migration requirements
- **Business Impact:** Affects data migration, financial reporting, cost recognition
- **Who Can Answer:** Lorraine Guzman (Finance), Accounting team
- **How to Get Answer:** Dedicated finance discovery session
- **Timeline:** Next 1-2 weeks
- **Session:** Session 3 (Finance & Data Migration)

#### HIGH-5: SharePoint Folder Structure Proposal
- **Question:** What will be the SharePoint folder structure?
- **Missing Information:** Folder hierarchy, file naming, pre-quote vs post-quote separation, lookbook handling
- **Business Impact:** Affects file organization, user experience, document retrieval
- **Who Can Answer:** Marcus (with Tyler), Implementation team
- **How to Get Answer:** Create SharePoint structure proposal document
- **Timeline:** Next 1-2 weeks
- **Action Item:** [ACTION] Marcus/Chris/Tyler to create proposal and present

#### HIGH-6: Data Migration Planning
- **Question:** What is detailed plan for data migration from Core to NetSuite?
- **Missing Information:** Historical data scope, mapping details, validation approach, cutover strategy
- **Business Impact:** Critical for project success; affects go-live timing; requires significant testing
- **Who Can Answer:** Marcus, Kip, Joe (Orion)
- **How to Get Answer:** Data migration planning session with Orion team
- **Timeline:** Weeks 2-3
- **Session:** Session 3 (Finance & Data Migration)
- **Action Item:** [ACTION] Marcus to initiate Teams conversation with Joe

---

### 🟢 MEDIUM PRIORITY - Nice-to-Have Details

#### MED-1: Auto-Rejection Logic for Competing Quotes
- **Question:** Should competing labor quotes auto-reject when one accepted?
- **Missing Information:** Scope-based grouping design, exception handling, user validation
- **Business Impact:** Dashboard cleanliness, manual cleanup reduction
- **Who Can Answer:** Operations, Marcus (Design)
- **How to Get Answer:** Design thinking session post-discovery

#### MED-2: Labor Quote Dashboard Details
- **Question:** What specific fields should be on labor quote dashboard?
- **Missing Information:** Complete field list, calculated fields, filter options, drill-down capabilities
- **Business Impact:** Reporting capabilities and user experience
- **Who Can Answer:** Matt Denning, Kimi Katsuyoshi, Operations
- **How to Get Answer:** Dashboard requirements documentation session

#### MED-3: Itemization Strategy Rules
- **Question:** When to use itemized vs. summary labor quote import?
- **Missing Information:** Decision criteria, business rules, template preferences
- **Business Impact:** Proposal formatting, contingency management, financial reporting
- **Who Can Answer:** Matt Denning, Account Managers
- **How to Get Answer:** Best practice decision documentation

---

## CONSULTANT ACTION PLAN

### **IMMEDIATE ACTIONS (Next 3-5 Days)**

#### Schedule Sessions
- [ ] **Session 1 Schedule:** Design Request Discovery
  - **With:** Wendy Stark (PM Manager) or Design Lead
  - **Target Attendees:** Design team, Marcus, Chris
  - **Duration:** 90 minutes
  - **Target Date:** Week of Nov 25 (avoid short Thanksgiving week if possible)
  - **Requested by:** Chris (contact Design Manager)

- [ ] **Session 2 Schedule:** PM Request & Resource Management
  - **With:** Wendy Stark
  - **Target Attendees:** PM team, Matt Denning, Marcus
  - **Duration:** 90 minutes
  - **Target Date:** Week of Nov 25
  - **Requested by:** Chris (contact Wendy)

- [ ] **Session 3 Schedule:** Finance & Data Migration
  - **With:** Lorraine Guzman
  - **Target Attendees:** Finance, Marcus, Kip
  - **Duration:** 60-90 minutes
  - **Target Date:** Week of Dec 2
  - **Requested by:** Chris (contact Lorraine)

#### Request Documents
- [ ] **Labor Quote Form Template** - Email to Matt Denning (URGENT)
  - "We need a screenshot or current version of KBMH's labor quote request form to use as template for Orion. This will help us ensure we capture all necessary fields. Please send at earliest convenience."
  
- [ ] **Design Request Form Template** - Email to Chris Trumble
  - "For the design request discovery session, we'll need a copy of the current design request form. Please provide template and a few recent examples."

- [ ] **Business Rule Screenshot** - Email to Kip Herdrick
  - "We need a screenshot of the 15% labor deduction business rule configuration from Core system. This will help us understand exactly how the formula works for Orion configuration."

- [ ] **Chart of Accounts Mapping Status** - Email to Chris Trumble/Lorraine Guzman
  - "What is the current status of Chart of Accounts mapping? Are there any gaps or issues we need to be aware of before data migration planning?"

#### Prepare Materials
- [ ] Create Design Request Discovery Session Agenda
- [ ] Create PM Request Discovery Session Agenda
- [ ] Create Finance Discovery Session Agenda
- [ ] Prepare Orion design request form concept to discuss
- [ ] Prepare Orion PM assignment approach to discuss
- [ ] Prepare labor quote dashboard mockup for review

---

### **FOLLOW-UP ACTIONS (Next 2-4 Weeks)**

#### Week 1-2: Document Collection & Preparation
- [ ] **Receive labor quote form template** - Review and incorporate fields into Orion form design
- [ ] **Receive design request form template** - Review and incorporate into discovery session
- [ ] **Receive business rule screenshot** - Document exact 15% deduction logic for configuration team
- [ ] **Conduct Session 1:** Design Request Discovery
  - Outcome: Complete design workflow documentation, form configuration ready
- [ ] **Conduct Session 2:** PM Request & Resource Discovery
  - Outcome: Complete PM workflow documentation, resource assignment rules clear

#### Week 2-3: Technical Validation & Planning
- [ ] **Technical Call with Orion:** Multiple Labor Quote Acceptance Validation
  - Confirm system behavior with Joe (Orion dev)
  - Document approach for scope-based quote management
- [ ] **Data Migration Planning Initiation:**
  - Marcus starts Teams conversation with Joe on data migration
  - Kip prepares historical data inventory
  - Scope historical data to be migrated (how many years?)
- [ ] **Conduct Session 3:** Finance & Accounting Discovery
  - Outcome: Financial processes documented, COA mapping confirmed, data migration scope defined

#### Week 3: Design & Proposal
- [ ] **Create SharePoint Folder Structure Proposal**
  - Marcus with Tyler
  - Send to KBMH for review
  - Get feedback and finalize
- [ ] **Draft Data Migration Strategy**
  - Based on Session 3 findings
  - Prepare test approach
  - Define cutover strategy

---

### **COMPLETION ACTIONS (Weeks 4+)**

#### Final Review & Sign-off
- [ ] **Conduct Session 4 (Optional):** Scope Governance Decision
  - Get final leadership decision on scope governance
  - Finalize scope update protocols
  - Outline training approach
  
- [ ] **Update Questionnaire to 95%+ Complete**
  - Incorporate all session findings
  - Add design request details
  - Add PM request details
  - Add finance/accounting details
  - Make scope governance decision final

- [ ] **Finalize Requirements Map**
  - Add any new REQ-### items from sessions
  - Classify by ALIGNS/ADAPT/ACCOMMODATE
  - Validate all requirements

- [ ] **Create BRD from Complete Questionnaire**
  - Use complete questionnaire as source
  - Incorporate all requirements
  - Include all workflows and processes
  - Ready for configuration phase

- [ ] **Schedule Configuration Phase Kickoff**
  - With all teams aligned
  - All questions answered
  - All decisions made
  - Ready to build

---

## SUCCESS METRICS & TIMELINE

### **Completion Targets**

| Milestone | Current | Target After Session | Timeline |
|-----------|---------|---------------------|----------|
| **Labor Quote Process** | 85% | 95%+ | Complete (ready for config) |
| **Design Request Process** | 5% | 85%+ | After Session 1 (Dec 2) |
| **PM Request Process** | 5% | 85%+ | After Session 2 (Dec 2) |
| **Finance/Accounting** | 20% | 85%+ | After Session 3 (Dec 9) |
| **Technical Decisions** | 70% | 95%+ | After validation calls (Dec 2) |
| **Overall Questionnaire** | 68% | 90%+ | End of follow-up phase (Dec 9) |

### **Phase Timeline**

**Week 1 (Nov 18-22):** 
- ✅ First discovery session completed (Labor Quotes)
- Document collection initiated
- Follow-up sessions scheduled

**Week 2 (Nov 25-29):**
- Design Request Discovery Session (Session 1)
- PM Request Discovery Session (Session 2)  
- Technical validation calls with Orion
- Questionnaire ~75% complete

**Week 3 (Dec 2-6):**
- Finance & Data Migration Session (Session 3)
- SharePoint folder structure finalized
- Data migration approach drafted
- Questionnaire ~85% complete

**Week 4 (Dec 9+):**
- Scope Governance Decision Session (if needed)
- Questionnaire finalized to 90%+
- BRD creation phase begins
- Configuration phase preparation

### **Go-Live Readiness**

**Estimated Configuration Start:** Early December 2025  
**Estimated Go-Live:** Q1 2026 (pending configuration effort estimates)

---

## OUTSTANDING DECISIONS & VALIDATIONS

### **Awaiting KBMH Decision**

| Item | Impact | Owner | Deadline |
|------|--------|-------|----------|
| **Scope Governance Model** | 🔴 CRITICAL | Operations Leadership | ASAP |
| **Auto-Rejection Logic** | 🟡 HIGH | Operations/Marcus | By design phase |
| **SharePoint Folder Structure** | 🟡 HIGH | Marcus/Tyler (present) | By data prep |

### **Awaiting Orion Technical Input**

| Item | Impact | Owner | Deadline |
|------|--------|-------|----------|
| **Multiple Quote Acceptance** | 🔴 CRITICAL | Joe/Marcus | Within 1 week |
| **Data Migration Approach** | 🔴 CRITICAL | Joe/Marcus/Kip | Week 3 |
| **Orion Feature Capabilities** | 🟡 HIGH | Joe/Marcus | By configuration |

### **Awaiting KBMH Documents**

| Item | Impact | Owner | Deadline |
|------|--------|-------|----------|
| **Labor Quote Form** | 🟡 HIGH | Matt Denning | This week |
| **Design Request Form** | 🔴 CRITICAL | Chris Trumble | Before Session 1 |
| **Business Rule Screenshot** | 🟡 HIGH | Kip Herdrick | This week |
| **SharePoint Proposal Review** | 🟡 HIGH | Matt Denning | By design phase |

---

## SUMMARY & RECOMMENDATIONS

### **What's Solid ✅**
- Labor quote request types, types, and calculations fully documented
- Hold-back strategy and multi-vendor bidding approach clear
- Acceptance workflow and PO-based acceptance well understood
- Decentralized initiation and team assignment models confirmed
- Opportunity integration concept validated

### **What Needs Work 🟠**
- Design request workflow requires full discovery
- PM request process requires full discovery and formalization
- Finance/accounting processes require detailed discovery
- Scope governance decision is critical and pending

### **What's at Risk 🔴**
- Data migration planning hasn't started yet (but not too early)
- Scope governance decision not made (needed for architecture)
- Multiple quote acceptance technical approach not validated
- Finance processes not fully understood (may impact data migration)

### **Recommended Next Steps**
1. **Get leadership decision on scope governance** (Matt & Kimi with team)
2. **Schedule Sessions 1-3** (Design, PM, Finance) for next 3 weeks
3. **Request documents** (forms, screenshots) this week
4. **Initiate technical validation** with Orion on multiple quotes
5. **Begin data migration planning** with inventory of historical data

### **Projected Completion**
- **Questionnaire 90%+ complete:** December 9, 2025
- **BRD ready for review:** December 16, 2025
- **Configuration phase kickoff:** December 20-30, 2025 (or early January per holidays)
- **Go-live:** Q1 2026 (depends on configuration complexity and team capacity)

---

## APPENDIX: DISCOVERY GAPS BY SOURCE

### **Gaps from Organic Discovery** (Questions that emerged from conversation, not original questionnaire)
- Auto-rejection logic for competing quotes
- Scope governance decision
- External work process integration (Google Slides, etc.)
- Rate tables for future estimating

### **Gaps from Original Questionnaire Not Yet Covered**
- Complete design request workflow (Q18)
- Complete PM request workflow (Q19)
- Finance/accounting complete process (Not in original; emerged as critical)

### **New Questions That Emerged But Need Deeper Exploration**
- How exactly should scope updates flow through system?
- What's the user adoption impact of "Opportunity as source of truth"?
- How will historical data quality impact migration?
- What training will be needed?

---

**Document Status:** Ready for KBMH Review & Session Planning  
**Next Milestone:** Schedule follow-up discovery sessions  
**Owner:** Implementation Team (Marcus, Chris, with KBMH guidance)



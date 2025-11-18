# Pre-Quote Follow-Up Discovery Sessions - KBMH ONLY
## KBMH NetSuite/Orion Implementation
**Document Version:** 3.0 (KBMH Ground Truth - COR References Removed, Assumptions Eliminated)  
**Date:** November 2025  
**Status:** Ready for KBMH Discovery Sessions

---

## EXECUTIVE SUMMARY

**Purpose:** Discover and document KBMH's pre-quote processes to configure accurately in NetSuite/Orion

**Scope:** 4 focused discovery sessions addressing:
1. Labor quote request types and processes
2. Vendor management and filtering
3. Design request workflow (if applicable)
4. PM request workflow (if applicable)

**Session Format:** Open-ended discovery focused on understanding KBMH's actual current processes - not assumptions from other companies

**Total Estimated Time:** ~6-8 hours of combined sessions across 4 topics

**Critical Outcome:** Fully documented KBMH pre-quote processes with clear decisions on Orion configuration approach

---

## CRITICAL NOTE: STARTING FROM KBMH GROUND TRUTH

This document was previously based on COR (Creative Office Resources) source material and contained COR-specific concepts (LTS, CAM, CAP, Bridge system). 

**We are starting fresh with KBMH:**
- No assumptions about labor quote types
- No assumptions about vendor management structure
- No assumptions about design/PM workflows
- No assumptions about systems or integrations
- Everything to be discovered directly from KBMH stakeholders

---

# SESSION 1: LABOR QUOTE REQUEST PROCESSES
**Priority:** CRITICAL  
**Duration:** 90 minutes  
**Objective:** Fully understand KBMH's labor quote request workflow

## Why This Discovery is Needed

We need to understand:
- What labor quote request types KBMH actually uses
- How they're currently initiated and managed
- Who's involved in the process
- What information needs to be captured
- How calculations are done
- How acceptance/rejection works
- What dashboards or reporting is needed

## Who Should Attend

**Must Have:**
- Senior Quoting Team Member(s) (2+) - Day-to-day users of labor quote process
- Operations Manager or Process Owner - Overall process authority
- Marcus (Implementation Team) - Orion configuration expert

**Should Have:**
- Chris Trumble (Implementation Team) - Form and configuration details
- Sales Representative - User and initiator perspective
- Finance/Accounting - Costing and margin perspective

**Optional:**
- Subcontractor/Vendor representative - External perspective

## Questions to Ask - OPEN-ENDED DISCOVERY

### 1. LABOR QUOTE REQUEST OVERVIEW (20 minutes)

**Q1.1:** What Labor Quote Request Types Exist?
- How many different types of labor quote requests does KBMH use?
- What are they? (Please describe each)
- What makes each type different from the others?
- Are there any other categories or variations?

**Q1.2:** How Often Are They Used?
- Which types are most common?
- Which are rare or seasonal?
- Rough volume per month for each type?

**Q1.3:** Who Uses Labor Quotes?
- Who initiates labor quote requests?
- Who receives/responds to them?
- Who approves or accepts them?
- Who uses the information from labor quotes?

### 2. CURRENT LABOR QUOTE WORKFLOW (20 minutes)

**Q2.1:** How is a Labor Quote Request Started?
- Where does the user go to start a labor quote request? (What system/screen/form?)
- What triggers the need for a labor quote?
- Is there a formal decision process for when to request labor quotes?

**Q2.2:** What Information is Captured on the Request?
- What fields/data must be on a labor quote request form?
- What's required vs. optional?
- What's unique to each request type?
- How much detail is needed?

**Q2.3:** Who Gets the Request?
- How are labor quote recipients selected/identified?
- Can users select multiple recipients?
- Is there filtering involved? (By location, skill, availability, etc.)
- How is the request transmitted? (Email, system portal, other?)

**Q2.4:** Response and Acceptance Process
- How do recipients respond with quotes?
- What format are responses in? (Email, system, spreadsheet, etc.)
- Who reviews the responses?
- How is a response accepted or rejected?
- What happens after acceptance?

### 3. LABOR CALCULATION METHODOLOGY (20 minutes)

**Q3.1:** How Are Labor Costs Calculated?
- Are calculations done in the system or outside (Excel, etc.)?
- If outside the system, who does the calculations?
- What information goes into calculations? (Hours, rates, markups, other?)
- Are there standard formulas or does it vary by situation?

**Q3.2:** Are There Different Calculation Approaches?
- Different by labor type?
- Different by customer type?
- Different by vendor/subcontractor?
- Different by project complexity?
- Seasonal variations?

**Q3.3:** Documentation of Calculations
- Are calculation rules documented anywhere?
- Who knows HOW calculations are done? (Institutional knowledge?)
- Is there a notes field or documentation area for calculation rationale?

**Q3.4:** Future Automation
- Would KBMH want automated calculations in Orion?
- What would that require? (Rate tables, formula storage, other?)
- Is that a nice-to-have or must-have?

### 4. LABOR QUOTE ACCEPTANCE & STATUS (15 minutes)

**Q4.1:** Acceptance Workflow
- What happens when a labor quote is "accepted"?
- Who makes the acceptance decision?
- Does acceptance automatically update anything? (Proposal, order, project?)
- Can an accepted quote be changed or rejected later?

**Q4.2:** Rejection or Send-Back Process
- If a labor quote is inadequate, what happens?
- Can it be sent back for revision?
- How many iterations/revisions are typical?
- Who decides if a quote is acceptable?

**Q4.3:** Status Tracking & Reporting
- How do users track pending labor quote requests?
- Is there a dashboard or report showing:
  - Which quotes were sent out?
  - To whom?
  - Current status?
  - How long they've been pending?
- Who needs access to this information?

### 5. FILE & DOCUMENTATION HANDLING (10 minutes)

**Q5.1:** Attachments and Specifications
- Are specification documents attached to labor quote requests?
- What formats? (PDF, Word, CAD files, other?)
- How are they shared with recipients? (Email, system, link, other?)

**Q5.2:** Project Scope Documentation
- How is project scope currently documented?
- Where is this information stored?
- Is it on the labor quote request or elsewhere?
- What details are included?

### 6. PROCESS INITIATION POINT (10 minutes)

**Q6.1:** Where Are Requests Started?
- Are labor quote requests initiated from Project records?
- Or from Opportunity/Quote records?
- Or from somewhere else?
- Can they be initiated from multiple places?

**Q6.2:** Process Change Impact
- If moving to a different starting point (e.g., Opportunity vs. Project), how would that affect users?
- What training would be needed?
- Are there any concerns about the change?

### 7. SITE CONDITIONS & PROJECT DETAILS (10 minutes)

**Q7.1:** Site/Location Information
- Is site condition information part of labor quote requests?
- How detailed? (Simple notes or structured data?)
- Is there a separate system record for site conditions?

**Q7.2:** Project Scope on Labor Quote Form
- What project information is needed on labor quote request?
- Is scope documented on the labor quote form itself?
- Or does it reference a separate project scope document?
- Could scope be better captured on the labor quote form?

---

## Pre-Work Required (Due One Week Before Session)

**Senior Quoting Team Members:**
- [ ] Document or describe EACH labor quote request type used
  - Name
  - When used
  - Who initiates
  - Who receives
  - Typical volume
- [ ] Bring 2-3 actual examples of labor quote requests
- [ ] Document any calculation rules or formulas currently used
- [ ] Identify pain points with current labor quote process

**Operations Manager:**
- [ ] Provide end-to-end workflow overview
- [ ] Document current approval/acceptance process
- [ ] List all stakeholders involved in labor quote process
- [ ] Identify any bottlenecks or inefficiencies

**Marcus (Implementation Team):**
- [ ] Confirm Orion capabilities for:
  - Multiple request types
  - Acceptance workflows
  - Rejection/send-back workflows
  - Status tracking and dashboards
- [ ] Prepare description of Orion request engine architecture

**All Participants:**
- [ ] Be prepared to discuss KBMH's specific business model and requirements (not comparative to other companies)

---

## Expected Outcomes

**Documentation to be Delivered:**
1. **KBMH Labor Quote Request Types Specification** - All types with business rules and workflows
2. **Labor Quote Process Flow Diagram** - Step-by-step current process
3. **Labor Quote Form Requirements** - All fields needed with purposes
4. **Calculation Methodology Documentation** - How labor costs are determined
5. **Acceptance & Rejection Procedures** - Decision criteria and workflow
6. **Status Tracking Approach** - Dashboard/report requirements
7. **Recommendation Document** - Orion configuration approach

**Outcomes:**
- Clear understanding of KBMH's labor quote request types (actual count and details)
- Documented calculation methodology
- Defined acceptance/rejection workflows
- Status tracking requirements documented
- Technical recommendation for Orion configuration

---

---

# SESSION 2: VENDOR MANAGEMENT & FILTERING
**Priority:** CRITICAL  
**Duration:** 60-75 minutes  
**Objective:** Discover how KBMH manages and selects vendors

## Why This Discovery is Needed

We need to understand:
- How KBMH classifies vendors
- What criteria are used to select vendors for labor quotes
- Whether there are multi-location vendors
- How vendor data is maintained
- What filters are applied when sending labor quote requests

## Who Should Attend

**Must Have:**
- Vendor Manager or Procurement Lead - Vendor data owner and selection authority
- Operations Manager - Process owner for vendor selection
- Marcus (Implementation Team) - Vendor record customization in Orion

**Should Have:**
- Joe (Implementation Team) - Technical questions on multi-location structures
- Sample Quoting Team Member - User perspective on vendor filtering
- Finance/AP - Vendor data maintenance

---

## Questions to Ask - OPEN-ENDED DISCOVERY

### 1. VENDOR CLASSIFICATION (20 minutes)

**Q1.1:** How Are Vendors Classified?
- What categories or classifications exist for vendors at KBMH?
- Are there unions involved? How are those tracked?
- Are there location-based categories?
- Are there preferred/approved vendor lists?
- Are there other vendor tiers or types?

**Q1.2:** What Information is Tracked on Vendor Records?
- What data does KBMH currently maintain on each vendor?
- Which fields are most important for labor quote selection?
- Are there certifications or qualifications tracked?
- Is there performance data tracked?

**Q1.3:** Dropdown Values and Definitions
- For each vendor classification:
  - What are the exact values or categories?
  - What's the business definition for each?
  - Can vendors have multiple values (e.g., both union AND non-union)?

### 2. MULTI-LOCATION VENDORS (20 minutes)

**Q2.1:** KBMH Location Structure
- How many KBMH locations exist?
- What are they?
- Do vendors service one location or multiple locations?

**Q2.2:** Multi-Location Vendor Approach
- How many vendors service multiple KBMH locations?
- Do these vendors have the same contacts/rates at each location?
- Or different contacts/rates per location?
- Are there location-specific certifications or requirements?

**Q2.3:** Technical Approach: How Should This Be Structured in Orion?
- Option A: One vendor record with multi-select location field
  - Pros: Simpler to maintain
  - Cons: Can't have different rates/contacts per location
- Option B: Parent vendor record with child records per location
  - Pros: Can have location-specific rates/contacts
  - Cons: More records to manage
- **Which approach makes sense for KBMH's business?**

### 3. VENDOR FILTERING LOGIC (15 minutes)

**Q3.1:** How Are Vendors Selected for Labor Quotes?
- Current process: How do users choose which vendors to send labor quote requests to?
- What filters or criteria are applied?
- Are there standard filters or is it manual selection?
- Can users apply multiple filters at once?

**Q3.2:** Filtering Criteria
- By location?
- By vendor classification/type?
- By specialty or skill?
- By performance history?
- By availability/capacity?
- Other criteria?

**Q3.3:** Multi-Vendor Quotes
- Can one labor quote request go to multiple vendors simultaneously?
- Or single vendor per request?
- How are multiple bids compared?

### 4. VENDOR DATA MAINTENANCE (10 minutes)

**Q4.1:** How Often Do Vendor Records Change?
- How frequently are vendor classifications updated?
- Who maintains vendor data?
- What triggers vendor data changes?
- Is there a review/audit process?

**Q4.2:** Current Vendor Data Status
- Is vendor classification data well-maintained currently?
- Are there data quality issues?
- Would cleaning up vendor data be needed before Orion implementation?

---

## Pre-Work Required (Due One Week Before Session)

**Vendor Manager/Procurement Lead:**
- [ ] Export complete vendor list with all current data/classifications
- [ ] Document each vendor classification type and its exact values
- [ ] Identify multi-location vendors (count and examples)
- [ ] Describe how vendor data is currently maintained

**Operations Manager:**
- [ ] Provide KBMH location list (all locations)
- [ ] Confirm vendor selection process and workflow
- [ ] Describe any vendor filtering logic currently used

**Marcus (Implementation Team):**
- [ ] Prepare technical recommendations for multi-location vendor structure
- [ ] Prepare options for vendor classification field structure

---

## Expected Outcomes

**Documentation to be Delivered:**
1. **KBMH Vendor Classification Specification** - All categories and values
2. **Vendor Record Structure Recommendation** - Multi-location approach decision
3. **Vendor Filtering Logic Document** - How vendors are selected for labor quotes
4. **Vendor Data Maintenance Process** - Who updates what and how often
5. **Recommended Orion Vendor Configuration** - Fields and structure

**Outcomes:**
- Clear definition of all vendor classifications needed
- Decision on multi-location vendor structure
- Documented vendor filtering workflow
- Vendor data maintenance process confirmed
- Technical configuration approach agreed upon

---

---

# SESSION 3: DESIGN REQUEST PROCESS
**Priority:** CRITICAL (if design requests are part of KBMH pre-quote)  
**Duration:** 90 minutes  
**Objective:** Discover design request workflow (if applicable)

## CRITICAL PRE-DISCOVERY QUESTION

**Does KBMH have a design request process as part of Pre-Quote?**

This session should only occur if KBMH confirms they have design requests that need to be configured in Orion. This is NOT assumed.

---

## If Design Requests Are Applicable

## Who Should Attend

**Must Have:**
- Design Manager or Lead - Process owner
- 1-2 Senior Designers - Hands-on workflow experts
- Marcus (Implementation Team) - Form configuration

**Should Have:**
- Sales Representative - Who requests design services
- Operations Lead - Handoff process
- Chris (Implementation Team) - Form development

---

## Questions to Ask - OPEN-ENDED DISCOVERY

### 1. DESIGN REQUEST TRIGGERS & INITIATION (15 minutes)

**Q1.1:** When Does KBMH Do Design Requests?
- What percentage of projects require design work?
- What triggers the need for design?
- Who decides if design is needed?
- When in the project lifecycle are design requests initiated?

**Q1.2:** Design Request Types
- Are there different types of design requests?
- Different complexity levels?
- Rush vs. standard timelines?

### 2. DESIGN REQUEST WORKFLOW (20 minutes)

**Q2.1:** What's Captured on a Design Request?
- What information must be on the design request form?
- What's required vs. optional?
- What's the level of detail?

**Q2.2:** Designer Assignment
- How are designers assigned to design requests?
- Can customers request specific designers?
- How does capacity/workload affect assignment?

**Q2.3:** Design Deliverables
- What outputs does a designer produce?
- What formats?
- What's the approval/sign-off process?

### 3. DESIGN-TO-QUOTE INTEGRATION (15 minutes)

**Q3.1:** How Does Design Feed Into Quoting?
- After design is complete, how does that information get to the proposal/quote?
- Are there design costs included in the quote?
- Can design specs be attached to labor quote requests?

**Q3.2:** Timeline
- How long does typical design take?
- Are there rush options?
- Capacity constraints?

### 4. DESIGN COST & BILLING (10 minutes)

**Q4.1:** How is Design Priced?
- Flat fee, hourly, percentage of project, complexity-based, or free?
- Is design cost visible to customer?
- Is design always billed or sometimes included?

---

## Expected Outcomes

**Documentation to be Delivered:**
1. **KBMH Design Request Process Workflow**
2. **Design Request Form Specification**
3. **Designer Assignment Rules**
4. **Design-to-Quote Integration Process**
5. **Design Costing & Billing Rules**

---

---

# SESSION 4: PM REQUEST PROCESS
**Priority:** CRITICAL (if PM requests are part of KBMH pre-quote)  
**Duration:** 90 minutes  
**Objective:** Discover PM request workflow (if applicable)

## CRITICAL PRE-DISCOVERY QUESTION

**Does KBMH have a PM (Project Manager) request process as part of Pre-Quote?**

This session should only occur if KBMH confirms they have PM requests that need to be configured in Orion. This is NOT assumed.

---

## If PM Requests Are Applicable

## Who Should Attend

**Must Have:**
- PM Manager or Lead - Process owner
- 1-2 Senior PMs - Hands-on workflow experts
- Marcus (Implementation Team) - Form configuration

**Should Have:**
- Sales Representative - Who requests PM services
- Operations Lead - Resource allocation and planning
- Chris (Implementation Team) - Form development

---

## Questions to Ask - OPEN-ENDED DISCOVERY

### 1. PM INVOLVEMENT TRIGGERS & TIMING (15 minutes)

**Q1.1:** When Does KBMH Request PM Involvement?
- What percentage of projects have PM assigned?
- What triggers the need for PM involvement?
- Who decides if PM is needed?
- When in project lifecycle is PM involved? (Pre-sale, post-sale, at kickoff?)

**Q1.2:** PM Types
- Are there different types of PM involvement?
- Different project types requiring different PM approaches?

### 2. PM REQUEST WORKFLOW (20 minutes)

**Q2.1:** What's Captured on PM Request?
- What information must be on the PM request form?
- What's required vs. optional?

**Q2.2:** PM Assignment
- How are PMs assigned to projects?
- Can customers request specific PMs?
- Can PMs decline projects?
- How many projects can one PM juggle?

**Q2.3:** Sales-to-PM Handoff
- How does information flow from sales to PM?
- Is there a formal kickoff or handoff meeting?
- What information does PM need?

### 3. PM IMPACT ON QUOTE/PROJECT (15 minutes)

**Q3.1:** Does PM Involvement Affect the Quote?
- Is PM cost included in proposal?
- Does PM assignment change project timeline?
- Can customers see who their PM will be?

**Q3.2:** PM Authority & Responsibilities
- What decisions can PM make?
- Who approves PM decisions?
- Escalation process?

### 4. PM WORKLOAD & RESOURCE MANAGEMENT (10 minutes)

**Q4.1:** PM Capacity & Tracking
- How many PMs available?
- Typical workload?
- How is PM workload currently tracked?
- Capacity constraints?

---

## Expected Outcomes

**Documentation to be Delivered:**
1. **KBMH PM Request Process Workflow**
2. **PM Request Form Specification**
3. **PM Assignment Rules & Logic**
4. **Sales-to-PM Handoff Process**
5. **PM Workload Management Approach**

---

---

## APPENDIX: SESSION SCHEDULING & LOGISTICS

### Recommended Sequencing
1. **Session 1: Labor Quote Requests** - Week 1 (Foundational)
2. **Session 2: Vendor Management** - Week 1 (Can parallel with Session 1)
3. **Session 3: Design Requests** - Week 2 (Only if KBMH confirms design is pre-quote)
4. **Session 4: PM Requests** - Week 2 (Only if KBMH confirms PM is pre-quote)

### Session Outcomes
Each session should result in:
- ✅ Clear understanding of KBMH's actual process (not assumptions)
- ✅ Documented business requirements
- ✅ Technical configuration recommendations
- ✅ Stakeholder sign-off on approach

### Post-Session Process
- Implementation team documents findings within 3 business days
- KBMH stakeholders review and approve documentation
- Clarifications gathered within 5 business days
- Final approval before Orion configuration begins

---

**Document Version:** 3.0 (KBMH Ground Truth Only)  
**Status:** Ready for KBMH Discovery Sessions  
**Date:** November 2025  
**Note:** This document assumes NO prior process knowledge and asks open-ended discovery questions focused entirely on KBMH's actual business requirements.

# Gap Analysis - Pre-Quote Discovery
**Version**: 1.0  
**Date**: October 23, 2025  
**Process Area**: Pre-Quote (Labor Quote Requests, Design Requests, Estimating, Project Requests)  
**Analysis Type**: Discovery Questionnaire Completeness Assessment

## Change Log
- **Date**: October 23, 2025
- **Version**: 1.0
- **Sources**: Questionnaire_PreQuote_v1.0.md, Requirements_Map_PreQuote_v1.0.md, Master_Transcript_Pre-Quote.md
- **Summary**: Comprehensive gap analysis completed identifying 2 critical documentation gaps (Design and PM requests), 4 technical confirmations needed, and 6 discovery clarifications required before configuration can proceed.

## PROCESSED FILES
- Pre-Quote/3 Output/Questionnaire_PreQuote_v1.0.md (1138 lines)
- Pre-Quote/3 Output/Requirements_Map_PreQuote_v1.0.md (234 lines)
- Pre-Quote/2 Input/Master_Transcript_Pre-Quote.md (273 lines)
- Pre-Quote/2 Input/Discovery Workflow Specification.md (87 lines)

---

## 1. EXECUTIVE SUMMARY

**Overall Completeness**: 74% of questions fully answered for documented processes

**Critical Gaps**: 
1. Design Request Process - Complete workflow undocumented (High Priority)
2. PM Request Process - Complete workflow undocumented (High Priority)
3. Vendor classification values undefined (Medium Priority)
4. CAP/SIF file handling process unclear (Medium Priority)

**Follow-up Sessions Needed**: 4 discovery sessions (2 high priority, 2 medium priority)

**Estimated Timeline**: 3-4 weeks to achieve 95%+ completeness across all Pre-Quote request types

**Key Strengths**: Labor quote request process (Internal, External, Intermarket, LTS) is well-documented with 92% confidence. Strong understanding of vendor management requirements, union compliance, and Orion implementation approach.

**Key Risks**: Missing Design and PM request documentation could delay configuration phase; vendor classification values needed before vendor record customization can proceed.

---

## 2. COMPREHENSIVE QUESTION ANALYSIS

### 2.1 Complete Status Matrix

| Question # | Question Source | Question Topic | Status | Evidence Quality | Action Needed |
|------------|----------------|----------------|--------|------------------|---------------|
| 1.1 | Original | Current systems for pre-quote | ✅ Complete | Strong | None |
| 1.2 | Original | Labor quote request types | ✅ Complete | Strong | None |
| 2.1 | Original | Union labor requirements | ✅ Complete | Strong | Technical confirmation on vendor field |
| 2.2 | Original | Vendor selection & filtering | ⚠️ Partial | Strong | Define dropdown values |
| 2.3 | Original | Labor quote calculations | ✅ Complete | Strong | Document institutional knowledge formulas |
| 2.4 | Organic | Labor quote acceptance workflow | ✅ Complete | Strong | None (Orion feature confirmed) |
| 2.5 | Organic | Pending quote tracking | ⚠️ Partial | Moderate | Confirm Orion functionality exists |
| 3.1 | Original | Project request form workflow | ✅ Complete | Strong | Obtain Design & PM documentation |
| 3.2 | Original | Project scope capture | ✅ Complete | Strong | None |
| 4.1 | Original | CAM reservation integration | ✅ Complete | Strong | None |
| 4.2 | Original | CAP/SIF file handling | ⚠️ Partial | Moderate | Clarify PDF vs SIF import process |
| 4.3 | Original | RFQ form and branding | ✅ Complete | Strong | Confirm design preferences |
| 5.1 | Original | Estimating process | ⚠️ Partial | Moderate | Covered in Operations sessions |
| 5.2 | Organic | Job site analysis record | ✅ Complete | Strong | None (Orion feature confirmed) |
| 6.1 | Original | Long term storage process | ⚠️ Partial | Moderate | Covered in Order Management sessions |
| 7.1 | Organic | Process adaptations for Orion | ✅ Complete | Strong | Change management planning |
| 7.2 | Organic | Form development requirements | ✅ Complete | Strong | None |
| 8.1 | Follow-up | Missing documentation identified | ✅ Complete | Strong | Schedule Design & PM sessions |
| 8.2 | Follow-up | Technical confirmations needed | ⚠️ Partial | Moderate | Query implementation team |
| NEW-1 | Missing | Design request complete workflow | ❌ Missing | None | HIGH PRIORITY - Discovery session |
| NEW-2 | Missing | PM request complete workflow | ❌ Missing | None | HIGH PRIORITY - Discovery session |
| NEW-3 | Clarification | Institutional knowledge formulas | ⚠️ Partial | Weak | Document calculation formulas |
| NEW-4 | Clarification | Vendor dropdown values | ⚠️ Partial | Weak | Define with COR team |
| NEW-5 | Clarification | LTS calculation methodology | ⚠️ Partial | Weak | Reference Order Management docs |
| NEW-6 | Clarification | Vendor location multi-select approach | ⚠️ Partial | Moderate | Technical design decision |

### 2.2 Categorized Results

**✅ Fully Answered** (13 questions): 
- Current system identification (Bridge)
- Labor quote request types (4 types confirmed)
- Union requirements and compliance
- CAM reservation (manual entry)
- Labor quote acceptance workflow (Orion feature)
- Project request form structure
- Project scope capture location (adaptation required)
- Job site analysis record (Orion feature)
- Process adaptations identified (ADAPT requirements)
- Form development scope
- Missing documentation identified
- RFQ form requirements
- Request initiation point change (ADAPT requirement)

**⚠️ Partially Answered** (9 questions):
- Vendor filtering dropdown values (concept understood, values undefined)
- Pending quote dashboard (requirement understood, Orion capability needs confirmation)
- CAP/SIF file handling (general approach understood, specific process unclear)
- Estimating detailed workflow (high-level understood, detailed in Operations sessions)
- Long term storage details (high-level understood, detailed in Order Management sessions)
- Technical confirmations from implementation team (questions identified, confirmations pending)
- Institutional knowledge calculation formulas (examples given, complete documentation needed)
- Vendor location field approach (need identified, single vs multi-select decision pending)
- Request rejection workflow (need identified, Orion capability needs confirmation)

**❌ Not Answered** (2 questions):
- Design request complete workflow (documentation missing)
- PM request complete workflow (documentation missing)

---

## 3. INFORMATION GAPS ANALYSIS

### 3.1 Critical Gaps (Must Be Resolved Before Configuration)

#### GAP-001: Design Request Process Documentation
**Related REQ**: REQ-014 (partial implementation blocked)

**What specific information is missing?**
- What triggers a design request? (Customer-initiated vs Sales-identified need)
- What information is captured on the design request form?
- How are designers assigned? (By location, specialty, workload)
- What deliverables are produced? (CAD drawings, floor plans, renderings)
- How does design integrate with quote process? (Design cost billing, timeline impact)
- What is the approval/review workflow?
- Who are the stakeholders? (Design Manager Rafina mentioned, designer roles)

**Why is this information important?**
- Project request form includes "Design needed" checkbox that triggers design workflow
- Without design request configuration, project request form is incomplete
- Design deliverables likely impact quote pricing and project timeline
- Integration between Design (COR Studio) and Quote process is critical

**Who would have this information?**
- **Design Manager** (Rafina - mentioned in Operations transcript)
- **COR Studio team members**
- **Sales team** (who request design services)
- **Operations team** (who coordinate design-to-quote handoff)

**What's the best way to get this information?**
- **Discovery session** (60-90 minutes) with Design Manager and 1-2 senior designers
- **Pre-work**: Obtain any existing design request forms/documentation from SharePoint
- **Walkthrough**: Review sample design projects from request through deliverable
- **Demo**: If available, screen-share Bridge design request workflow

**Current Approach**: FUTURE (not yet analyzed; likely ALIGNS or ACCOMMODATE)

---

#### GAP-002: PM Request Process Documentation
**Related REQ**: REQ-014 (partial implementation blocked)

**What specific information is missing?**
- What triggers a PM request? (Project complexity, size, customer requirement)
- What information is captured on the PM request form?
- How are PMs assigned? (By location, expertise, availability)
- What is the handoff process from Sales to PM?
- How does PM involvement impact the quote? (PM time billing, resource allocation)
- What is the PM acceptance/review workflow?
- Who are the stakeholders? (PM Manager Wendy extensively involved in Operations)

**Why is this information important?**
- Project request form includes "PM needed" checkbox that triggers PM workflow
- Without PM request configuration, project request form is incomplete
- PM assignment timing impacts project planning and resource allocation
- PM involvement may affect quote pricing and project timeline

**Who would have this information?**
- **PM Manager** (Wendy - extensively involved in Operations discussions)
- **Senior PMs**
- **Sales team** (who determine when PM involvement is needed)
- **Operations team** (who coordinate PM assignment)

**What's the best way to get this information?**
- **Discovery session** (60-90 minutes) with PM Manager and 1-2 senior PMs
- **Pre-work**: Obtain any existing PM request forms/documentation from SharePoint
- **Walkthrough**: Review sample projects from PM request through assignment
- **Demo**: If available, screen-share Bridge PM request workflow

**Current Approach**: FUTURE (not yet analyzed; likely ALIGNS or ACCOMMODATE)

---

### 3.2 High-Priority Gaps (Needed for Configuration Completion)

#### GAP-003: Vendor Classification Dropdown Values
**Related REQ**: REQ-003, REQ-017

**What specific information is missing?**
- Complete list of union status values (Union, Non-union, Both?)
- Complete list of intermarket classification values
- COR location list for vendor assignment
- Business rules for vendor classification (Can a vendor be both union and non-union? How is this managed?)

**Why is this information important?**
- Custom fields on vendor record require dropdown value lists
- Vendor filtering logic depends on accurate classification
- Union compliance requirements are legally binding
- Incorrect vendor selection could result in compliance violations

**Who would have this information?**
- **Vendor Manager** or **Procurement lead**
- **Operations Manager**
- **Legal/Compliance** (for union requirements)
- **Finance** (for vendor record management)

**What's the best way to get this information?**
- **Targeted Q&A session** (30 minutes) or asynchronous document request
- **Pre-work**: Export current vendor list from Bridge with classifications
- **Deliverable**: Documented dropdown values and business rules

**Current Approach**: ACCOMMODATE (REQ-003, REQ-017)

---

#### GAP-004: CAP/SIF File Handling Process
**Related REQ**: REQ-015

**What specific information is missing?**
- Does COR export CAP specifications as PDF or SIF file?
- Are SIF files attached to labor quote requests as-is, or imported/processed?
- What format do subcontractors need/expect? (PDF table vs SIF text file)
- Are there any integrations between CAP and NetSuite/Orion expected?

**Why is this information important?**
- Document attachment approach depends on file format
- PDF attachment is straightforward; SIF import might require custom development
- Subcontractor requirements drive file format decision
- SharePoint integration approach may vary based on file type

**Who would have this information?**
- **Quoting Team** (who generate and attach CAP specifications)
- **Sales Team** (who use CAP to create specifications)
- **Subcontractors** (who receive and process specifications) - via COR team feedback

**What's the best way to get this information?**
- **Targeted Q&A session** (30 minutes) with Quoting Team lead
- **Pre-work**: COR provides sample CAP export files (both PDF and SIF if available)
- **Demonstration**: Show how specifications are currently exported and attached in Bridge

**Current Approach**: ALIGNS (REQ-015 - assuming PDF attachment)

---

#### GAP-005: Institutional Knowledge Calculation Formulas
**Related REQ**: REQ-007

**What specific information is missing?**
- Complete list of labor calculation formulas used by quoting team
- Rationale/business rules for each formula (e.g., "X times 1.52 rounded to nearest 50")
- When each formula is applied (by labor type, project type, location)
- Source of formula constants (industry standard, company policy, negotiated rates)
- How formulas are updated (rate changes, policy changes)

**Why is this information important?**
- Institutional knowledge needs to be documented for continuity
- Notes field design should accommodate formula documentation
- Future rate table functionality will require these formulas
- Training materials need formula explanations

**Who would have this information?**
- **Senior Quoting Team members** (who know the formulas)
- **Operations Manager** (who approves formula usage)
- **Finance** (who may validate or source rate information)

**What's the best way to get this information?**
- **Documentation request** with asynchronous completion
- **Follow-up Q&A** (30 minutes) to clarify formulas and rationale
- **Deliverable**: Formula documentation with examples

**Current Approach**: ADAPT (REQ-007 - manual calculation with notes)

---

#### GAP-006: Vendor Location Multi-Select Approach
**Related REQ**: REQ-004, REQ-005

**What specific information is missing?**
- How many vendors service multiple COR locations?
- Should multi-location vendors be handled with parent-child structure or multi-select location field?
- Are there different contacts/rates for the same vendor at different locations?
- How do users currently select vendors across locations?

**Why is this information important?**
- Design decision impacts vendor record structure
- Parent-child structure provides separate records per location
- Multi-select field keeps single vendor record with multiple locations
- Decision affects filtering logic and user workflow

**Who would have this information?**
- **Implementation Team** (Marcus, Joe - technical design decision)
- **Vendor Manager** (business process input)
- **Quoting Team** (user workflow preference)

**What's the best way to get this information?**
- **Technical design session** (45 minutes) with implementation team and COR stakeholders
- **Pre-work**: Analyze vendor list to identify multi-location vendors
- **Decision**: Document approach and rationale

**Current Approach**: ACCOMMODATE (REQ-004, REQ-005)

---

### 3.3 Medium-Priority Gaps (Needed for Optimization)

#### GAP-007: Pending Quote Dashboard Confirmation
**Related REQ**: REQ-013

**What specific information is missing?**
- Does Orion labor quote module include pending status dashboard?
- If not, what fields/data are available for saved search creation?
- What specific status values need to be displayed?
- Who are the primary users and what is their workflow?

**Who would have this information?**
- **Implementation Team** (Luke, Chris - Orion labor quote functionality experts)

**What's the best way to get this information?**
- **Internal confirmation** with implementation team
- **Demo**: If functionality exists, demonstrate to COR
- **Design**: If saved search needed, document requirements

**Current Approach**: ACCOMMODATE (REQ-013)

---

#### GAP-008: Request Rejection Workflow Confirmation
**Related REQ**: REQ-009

**What specific information is missing?**
- Does Orion request engine support "send back for more information" workflow?
- How is rejection/send-back different from mandatory fields preventing submission?
- What status changes occur when request is sent back?
- What notifications are triggered?

**Who would have this information?**
- **Implementation Team** (Joe - request engine architect)

**What's the best way to get this information?**
- **Internal confirmation** with Joe
- **Demo**: If functionality exists, demonstrate to COR
- **Design**: If customization needed, document requirements

**Current Approach**: ACCOMMODATE (REQ-009)

---

### 3.4 Categorization of Missing Information

**Current State Gaps** (Understanding existing processes):
- Design request workflow (GAP-001)
- PM request workflow (GAP-002)
- Institutional knowledge formulas (GAP-005)
- CAP/SIF file handling process (GAP-004)

**Requirements Gaps** (Unclear functional requirements):
- Vendor classification dropdown values (GAP-003)
- Vendor location multi-select approach (GAP-006)

**Technical Gaps** (System capabilities and integration):
- Pending quote dashboard exists in Orion? (GAP-007)
- Request rejection workflow exists in Orion? (GAP-008)
- Union status field exists on vendor record? (Related to GAP-003)

**Stakeholder Gaps** (Areas needing more input):
- Design Manager and COR Studio team (GAP-001)
- PM Manager and PM team (GAP-002)
- Vendor Manager/Procurement (GAP-003)

**Organic Discovery Gaps** (Important questions emerged but not fully explored):
- Labor quote acceptance feature benefits and user training approach
- Form development detailed specifications
- Change management strategy for process adaptations (REQ-010, REQ-011)

---

## 4. STAKEHOLDER ENGAGEMENT ANALYSIS

### 4.1 Well-Represented Roles (Good Input Received)

**✅ Implementation Team (Marcus Dallacqua, Chris Trumble, Gary Strickland)**
- **Coverage**: Excellent understanding of Orion capabilities and limitations
- **Evidence**: Detailed technical discussion throughout transcript
- **Contribution**: Identified ALIGN/ADAPT/ACCOMMODATE classifications, technical confirmations needed
- **Quality**: High - Clear articulation of implementation approach

**✅ Quoting Team (Implicit via Bridge documentation)**
- **Coverage**: Good understanding of labor quote workflows via Bridge documentation review
- **Evidence**: Current process well-documented in Labor Quote documents
- **Contribution**: Current state process flows, form fields, calculations
- **Quality**: Good - Need follow-up for formulas and CAP/SIF clarification

**✅ Operations Team (Referenced extensively)**
- **Coverage**: High-level process flows understood
- **Evidence**: References to Operations Manager, workflow handoffs
- **Contribution**: Process triggers, assignments, handoffs
- **Quality**: Moderate - Need deeper dive on estimating workflow

---

### 4.2 Under-Represented Roles (Need More Involvement)

**⚠️ Design Manager (Rafina)**
- **Current Involvement**: Mentioned in transcript but not directly engaged
- **Needed Involvement**: Full design request workflow documentation
- **Priority**: High
- **Action**: Schedule dedicated design request discovery session

**⚠️ PM Manager (Wendy)**
- **Current Involvement**: Mentioned as extensively involved in Operations but not in Pre-Quote session
- **Needed Involvement**: Full PM request workflow documentation
- **Priority**: High
- **Action**: Schedule dedicated PM request discovery session

**⚠️ Vendor Manager / Procurement Lead**
- **Current Involvement**: Not directly engaged
- **Needed Involvement**: Vendor classification values, multi-location vendor approach
- **Priority**: Medium-High
- **Action**: 30-minute targeted Q&A or document request

**⚠️ Senior Estimator(s)**
- **Current Involvement**: Process documented at high level
- **Needed Involvement**: Institutional knowledge formulas, detailed estimating workflow
- **Priority**: Medium
- **Action**: 30-minute targeted Q&A session

---

### 4.3 Missing Stakeholders (Haven't Been Engaged Yet)

**❌ Design Team Members (COR Studio)**
- **Why Needed**: Design request workflow, deliverables, tools, timeline
- **Impact**: Cannot configure design request functionality without their input
- **Priority**: High
- **Action**: Include 1-2 senior designers in design discovery session

**❌ Subcontractors (External Stakeholders)**
- **Why Needed**: RFQ form requirements, CAP/SIF file format preferences (via COR feedback)
- **Impact**: RFQ effectiveness, subcontractor responsiveness
- **Priority**: Low-Medium (COR can represent subcontractor needs)
- **Action**: Ask COR team about subcontractor feedback on current RFQ process

---

### 4.4 Decision-Maker Involvement

**✅ Operations Leadership**
- **Evidence**: Operations Manager referenced; Wendy (PM Manager) involved in Operations sessions
- **Needed**: Sign-off on process adaptations (REQ-010, REQ-011)

**⚠️ Sales Leadership**
- **Current Involvement**: Minimal direct engagement
- **Needed**: Validation of quote-to-sales handoff process, RFQ form approval
- **Priority**: Medium
- **Action**: Sales Manager review and sign-off on project request form and RFQ design

**⚠️ Finance Leadership**
- **Current Involvement**: None apparent
- **Needed**: Review of institutional knowledge formulas, vendor classification validation
- **Priority**: Low-Medium
- **Action**: Finance review during UAT phase

---

## 5. FOLLOW-UP MEETING PLAN

### 5.1 Required Follow-Up Sessions

---

#### Session 1: Design Request Process Deep Dive

**Purpose**: Document complete design request workflow to enable configuration of design request functionality tied to project request form (REQ-014)

**Questions to Address**:
1. What triggers a design request? (Customer requirement, Sales identification, project type)
2. What information is captured on the design request form? (Space planning, furniture specs, customer preferences, budget)
3. How are designers assigned? (Location, specialty, workload, customer relationship)
4. What tools do designers use? (CAD, rendering software, integration with CAP)
5. What deliverables are produced? (Floor plans, renderings, specifications, presentations)
6. What is the review/approval workflow? (Internal review, customer approval, revision cycles)
7. How does design integrate with quote? (Design fee billing, timeline impact, spec-to-quote handoff)
8. What is the timeline for typical design requests? (Rush vs standard)
9. How do designers communicate with Sales and customers? (Email, meetings, design presentations)
10. Are there different design request types? (New space, reconfiguration, furniture selection only)

**Required Attendees**:
- **Design Manager** (Rafina) - Primary stakeholder
- **1-2 Senior Designers** - Hands-on workflow experts
- **Sales Representative** - Design request initiator perspective
- **Operations Team Member** - Cross-functional coordination
- **Implementation Team** (Marcus/Chris) - Technical requirements capture

**Optional Attendees**:
- CAD/Design tools administrator (if relevant)

**Duration**: 90 minutes
- 10 min: Introductions and session objectives
- 30 min: Design request form and workflow walkthrough
- 20 min: Designer assignment and deliverables
- 20 min: Integration points (Sales, Quote, Customer)
- 10 min: Action items and follow-up

**Pre-work for Client**:
1. Locate and share any existing design request form templates or documentation from SharePoint
2. Prepare 2-3 sample design projects (simple, moderate, complex) for walkthrough
3. If available, prepare Bridge screen-share demo of design request process
4. Identify any design-specific fields or requirements not captured in project request form

**Consultant Preparation**:
1. Review existing project request form structure (REQ-014)
2. Review Orion request engine capabilities for design-specific fields
3. Prepare questions list based on gaps identified
4. Prepare screen-share of Orion request forms for comparison

**Expected Outcome**:
- Complete design request workflow documented
- Design request form fields defined
- New REQ-### items added to requirements map (estimated 5-8 requirements)
- ALIGN/ADAPT/ACCOMMODATE classification for design workflow
- Design request configuration ready to begin

**Success Criteria**:
- ✅ All 10 questions above answered with evidence
- ✅ Sample projects walked through
- ✅ Form fields documented
- ✅ Integration points identified
- ✅ Confidence rating ≥ 90% for design request process

---

#### Session 2: PM Request Process Deep Dive

**Purpose**: Document complete PM request workflow to enable configuration of PM request functionality tied to project request form (REQ-014)

**Questions to Address**:
1. What triggers a PM request? (Project size, complexity, customer requirement, contract type)
2. What information is captured on the PM request form? (Project details, timeline, resource needs, customer expectations)
3. How are PMs assigned? (Location, expertise, availability, customer relationship, project type)
4. What is the handoff process from Sales to PM? (Kickoff meeting, documentation transfer, system access)
5. How does PM involvement impact the quote? (PM time billing, resource allocation, timeline assumptions)
6. What is the PM acceptance/review workflow? (PM reviews request, accepts or requests more info, begins project planning)
7. When does PM get involved in project lifecycle? (Pre-sale, post-sale, at project kickoff)
8. What information does PM need from Sales? (SOW, customer contacts, site information, budget, constraints)
9. How do PMs track project requests in Bridge? (Dashboard, notifications, status updates)
10. Are there different PM request types? (Install PM, Project PM, Account PM)

**Required Attendees**:
- **PM Manager** (Wendy) - Primary stakeholder
- **1-2 Senior PMs** - Hands-on workflow experts
- **Sales Representative** - PM request initiator perspective
- **Operations Team Member** - Cross-functional coordination
- **Implementation Team** (Marcus/Chris) - Technical requirements capture

**Optional Attendees**:
- Scheduler or Resource Manager (if separate role)

**Duration**: 90 minutes
- 10 min: Introductions and session objectives
- 30 min: PM request form and workflow walkthrough
- 20 min: PM assignment and handoff process
- 20 min: Integration points (Sales, Quote, Project, Operations)
- 10 min: Action items and follow-up

**Pre-work for Client**:
1. Locate and share any existing PM request form templates or documentation from SharePoint
2. Prepare 2-3 sample PM requests (different project types) for walkthrough
3. If available, prepare Bridge screen-share demo of PM request process
4. Identify PM assignment criteria and business rules

**Consultant Preparation**:
1. Review existing project request form structure (REQ-014)
2. Review Orion request engine capabilities for PM-specific fields
3. Review project record capabilities in Orion (since PM may interact with project record differently)
4. Prepare questions list based on gaps identified

**Expected Outcome**:
- Complete PM request workflow documented
- PM request form fields defined
- New REQ-### items added to requirements map (estimated 5-8 requirements)
- ALIGN/ADAPT/ACCOMMODATE classification for PM workflow
- PM assignment business rules documented
- PM request configuration ready to begin

**Success Criteria**:
- ✅ All 10 questions above answered with evidence
- ✅ Sample projects walked through
- ✅ Form fields documented
- ✅ Integration points identified
- ✅ Confidence rating ≥ 90% for PM request process

---

#### Session 3: Vendor Management and Classification

**Purpose**: Define vendor classification dropdown values and finalize vendor record customization approach for union requirements and location-based filtering (REQ-003, REQ-004, REQ-005, REQ-017)

**Questions to Address**:
1. What are the complete values for union classification dropdown? (Union, Non-union, Both, N/A)
2. What are the complete values for intermarket classification dropdown?
3. How many COR locations exist and need vendor assignments?
4. What vendors currently service multiple locations?
5. For multi-location vendors, are contacts and rates the same or different per location?
6. How do users currently select vendors for RFQs? (Filter by multiple criteria simultaneously)
7. What are the criteria for "preferred vendors" vs all qualified vendors?
8. Are there pre-approved vendor lists by location or project type?
9. How often do vendor classifications change? (Union status changes, new locations served)
10. Who maintains vendor records and keeps classifications up-to-date?

**Required Attendees**:
- **Vendor Manager or Procurement Lead** - Primary stakeholder
- **Quoting Team Lead** - Vendor selection user
- **Operations Manager** - Process oversight and compliance
- **Implementation Team** (Marcus, Joe) - Technical design and NetSuite configuration

**Optional Attendees**:
- Finance representative (vendor record data management)
- Legal/Compliance (union requirement validation)

**Duration**: 75 minutes
- 10 min: Introductions and session objectives
- 20 min: Vendor classification values definition
- 20 min: Multi-location vendor approach (parent-child vs multi-select)
- 15 min: Vendor filtering workflow and business rules
- 10 min: Technical confirmation and design decisions

**Pre-work for Client**:
1. Export vendor list from Bridge with current classifications (union status, locations served)
2. Identify multi-location vendors and note if they have different contacts/rates per location
3. Document complete COR location list
4. Prepare business rules for vendor selection and filtering

**Consultant Preparation**:
1. Review NetSuite vendor record standard fields and customization options
2. Prepare recommendation for parent-child vs multi-select approach with pros/cons
3. Review filtering logic requirements (REQ-017)
4. Prepare screen-share of vendor record configuration options

**Expected Outcome**:
- Vendor classification dropdown values finalized and documented
- Decision made on parent-child vs multi-select location approach
- Vendor filtering business rules documented
- REQ-003, REQ-004, REQ-005, REQ-017 marked as CONFIRMED and ready for configuration
- Technical specifications prepared for Joe/implementation team

**Success Criteria**:
- ✅ Dropdown values documented and approved
- ✅ Multi-location approach decided with rationale
- ✅ Filtering logic confirmed
- ✅ Vendor record customization specifications ready
- ✅ Data migration/cleanup approach identified (if needed)

---

#### Session 4: Quoting Team Q&A - Formulas, CAP/SIF, Pending Dashboard

**Purpose**: Clarify institutional knowledge calculation formulas, CAP/SIF file handling process, and pending quote dashboard requirements (GAP-004, GAP-005, GAP-007)

**Questions to Address**:
1. What are all the calculation formulas used for labor quotes? (Document each formula with example)
2. What is the rationale for each formula? (Business rules, industry standards, negotiated rates)
3. When is each formula applied? (By labor type, location, project type, customer)
4. How are formulas updated? (Rate changes, frequency, approval process)
5. Does COR export CAP specifications as PDF or SIF file?
6. How are CAP exports attached to labor quote requests in Bridge?
7. What format do subcontractors need/prefer? (Feedback on current process)
8. What information needs to be visible on pending quote dashboard?
9. How do quoting team members currently use the pending quote dashboard?
10. What actions do they take from the dashboard? (Follow-up, status updates, closing quotes)

**Required Attendees**:
- **Quoting Team Lead** - Primary user and subject matter expert
- **1-2 Senior Quoting Team Members** - Hands-on workflow and formula experts
- **Operations Manager** - Process oversight and formula approval authority
- **Implementation Team** (Chris, Luke) - Orion labor quote functionality and saved search design

**Optional Attendees**:
- Sales representative (CAP/SIF file usage perspective)

**Duration**: 60 minutes
- 10 min: Introductions and session objectives
- 20 min: Institutional knowledge calculation formulas documentation
- 15 min: CAP/SIF file handling process clarification
- 10 min: Pending quote dashboard requirements and Orion capabilities
- 5 min: Action items and follow-up

**Pre-work for Client**:
1. Document all labor calculation formulas currently used with examples
2. Prepare sample CAP export files (PDF and SIF if both are used)
3. Screen-capture pending quote dashboard from Bridge showing desired information
4. Note any pain points with current CAP/SIF or dashboard processes

**Consultant Preparation**:
1. Review labor quote form field design (REQ-007 notes field)
2. Confirm Orion labor quote pending status tracking capabilities (internal check)
3. Prepare saved search design approach if dashboard doesn't exist
4. Review SharePoint integration capabilities for CAP/SIF attachments

**Expected Outcome**:
- Complete calculation formulas documented with examples and rationale
- CAP/SIF file handling process clarified (PDF vs SIF, attachment workflow)
- Pending quote dashboard requirements finalized
- Confirmation of Orion capabilities or saved search specifications
- REQ-007, REQ-013, REQ-015 marked as CONFIRMED and ready for configuration

**Success Criteria**:
- ✅ All formulas documented with examples
- ✅ CAP/SIF process clearly understood
- ✅ Pending dashboard requirements specified
- ✅ Technical approach confirmed (existing feature vs custom saved search)
- ✅ Notes field design validated for formula capture

---

### 5.2 Client Preparation Summary

**Documents Needed**:
1. Design request form templates or documentation (Session 1)
2. PM request form templates or documentation (Session 2)
3. Vendor list export with classifications (Session 3)
4. Labor calculation formulas documentation (Session 4)
5. Sample CAP export files (Session 4)
6. Bridge dashboard screenshots (pending quotes) (Session 4)

**People to Involve**:
- Design Manager (Rafina) + 1-2 senior designers (Session 1)
- PM Manager (Wendy) + 1-2 senior PMs (Session 2)
- Vendor Manager/Procurement Lead + Operations Manager (Session 3)
- Quoting Team Lead + 1-2 senior quoting team members (Session 4)
- Sales Representative (Sessions 1, 2 - request initiator perspective)
- Implementation Team (All sessions - Marcus, Chris, Joe, Luke as appropriate)

**Examples to Prepare**:
- 2-3 sample design projects (simple, moderate, complex)
- 2-3 sample PM requests (different project types)
- Sample labor quotes showing calculation formulas
- Sample CAP/SIF files attached to labor quotes

---

## 6. PRIORITY CLASSIFICATION

### 6.1 Critical Priority Gaps (🔴 Must Be Answered to Proceed)

---

**🔴 GAP-001: Design Request Process Documentation**

**Question**: What is the complete design request workflow from initiation through deliverable completion?

**Missing Information**: 
- Design request form fields and structure
- Designer assignment workflow and criteria
- Design deliverables and quality standards
- Design-to-quote integration points
- Timeline and communication processes

**Business Impact**: 
- **Configuration Blocker**: Cannot configure design request functionality without this information
- **Incomplete Project Request Form**: "Design needed" checkbox cannot be fully implemented
- **Integration Risk**: Unknown integration points between Design (COR Studio) and Quote process
- **Timeline Risk**: Design request process may impact overall quote-to-project timeline

**Who Can Answer**: 
- Design Manager (Rafina) - PRIMARY
- Senior Designers (1-2) - REQUIRED
- Sales Representative - SUPPORTING

**How to Get Answer**: 
- 90-minute discovery session (Session 1 above)
- Pre-work: Obtain existing design documentation from SharePoint
- Deliverable: Documented workflow, form fields, 5-8 new REQ-### items

**Related Requirements**: REQ-014 (Project request form - partial)

---

**🔴 GAP-002: PM Request Process Documentation**

**Question**: What is the complete PM request workflow from initiation through PM assignment and handoff?

**Missing Information**: 
- PM request form fields and structure
- PM assignment workflow and criteria
- Sales-to-PM handoff process and documentation
- PM request impact on quote and project
- PM acceptance/review workflow

**Business Impact**: 
- **Configuration Blocker**: Cannot configure PM request functionality without this information
- **Incomplete Project Request Form**: "PM needed" checkbox cannot be fully implemented
- **Resource Allocation Risk**: Unknown PM assignment and resource planning impacts
- **Handoff Risk**: Critical Sales-to-PM handoff process undefined

**Who Can Answer**: 
- PM Manager (Wendy) - PRIMARY
- Senior PMs (1-2) - REQUIRED
- Sales Representative - SUPPORTING

**How to Get Answer**: 
- 90-minute discovery session (Session 2 above)
- Pre-work: Obtain existing PM documentation from SharePoint
- Deliverable: Documented workflow, form fields, 5-8 new REQ-### items

**Related Requirements**: REQ-014 (Project request form - partial)

---

**🔴 GAP-003: Vendor Classification Dropdown Values**

**Question**: What are the complete and accurate dropdown values for vendor classification fields (union status, intermarket, location)?

**Missing Information**: 
- Union classification dropdown values (Union, Non-union, Both, N/A?)
- Intermarket classification dropdown values
- Complete COR location list for vendor assignment
- Business rules for vendor classification management

**Business Impact**: 
- **Configuration Blocker**: Cannot create custom vendor fields without dropdown values
- **Compliance Risk**: Incorrect union classification could lead to legal/contract violations
- **Filtering Risk**: Incomplete classification values will cause vendor filtering to fail
- **Data Quality Risk**: Unclear values will cause inconsistent data entry

**Who Can Answer**: 
- Vendor Manager/Procurement Lead - PRIMARY
- Operations Manager - SUPPORTING
- Implementation Team (Joe) - Technical input

**How to Get Answer**: 
- 75-minute discovery session (Session 3 above)
- Pre-work: Export vendor list from Bridge with current classifications
- Deliverable: Finalized dropdown values, business rules documented

**Related Requirements**: REQ-003, REQ-017

---

### 6.2 High Priority Gaps (🟡 Important for Project Success)

---

**🟡 GAP-004: CAP/SIF File Handling Process**

**Question**: How does COR export and attach CAP specifications to labor quote requests?

**Missing Information**: 
- CAP export format used (PDF vs SIF)
- Attachment workflow in Bridge
- Subcontractor format preferences/requirements
- Any expected CAP-to-NetSuite integrations

**Business Impact**: 
- **Configuration Impact**: Document attachment approach depends on file format
- **User Workflow**: SharePoint integration approach may vary by file type
- **Subcontractor Effectiveness**: Incorrect format could reduce RFQ response quality/speed
- **Development Risk**: If SIF import/integration is expected, significant custom development required

**Who Can Answer**: 
- Quoting Team Lead - PRIMARY
- Sales Representative - SUPPORTING (CAP usage)
- Subcontractors - via COR team feedback

**How to Get Answer**: 
- 60-minute Q&A session (Session 4 above, 15 minutes dedicated)
- Pre-work: COR provides sample CAP export files (PDF and SIF)
- Deliverable: Confirmed file format and attachment workflow

**Related Requirements**: REQ-015

**Current Assumption**: PDF attachment (low-risk assumption, easily corrected if needed)

---

**🟡 GAP-005: Institutional Knowledge Calculation Formulas**

**Question**: What are all the labor calculation formulas used by the quoting team, and what is the business rationale for each?

**Missing Information**: 
- Complete list of formulas with examples (e.g., "X times 1.52 rounded to nearest 50")
- Business rules for when each formula applies
- Source of formula constants (negotiated rates, industry standards, company policy)
- Formula update process and frequency

**Business Impact**: 
- **Continuity Risk**: Undocumented institutional knowledge creates dependency on specific individuals
- **Training Impact**: New quoting team members cannot learn formulas from system
- **Data Quality**: Inconsistent formula application without documentation
- **Future Enhancement**: Rate table functionality (future phase) will require these formulas

**Who Can Answer**: 
- Senior Quoting Team Members - PRIMARY
- Operations Manager - SUPPORTING (approval authority)
- Finance - SUPPORTING (rate validation)

**How to Get Answer**: 
- 60-minute Q&A session (Session 4 above, 20 minutes dedicated)
- Pre-work: Quoting team documents all formulas with examples
- Deliverable: Formula documentation, notes field design validated

**Related Requirements**: REQ-007

**Current Approach**: ADAPT (manual calculation with notes field for formulas)

---

**🟡 GAP-006: Vendor Location Multi-Select Approach**

**Question**: Should multi-location vendors be handled with parent-child structure or multi-select location field?

**Missing Information**: 
- Number of multi-location vendors
- Whether contacts and rates differ by location for the same vendor
- User workflow preference for vendor selection
- Technical pros/cons of each approach

**Business Impact**: 
- **Design Decision**: Impacts vendor record structure and configuration approach
- **User Workflow**: Different user experience with parent-child vs multi-select
- **Data Migration**: May affect vendor data cleanup/migration from Bridge
- **Filtering Logic**: Different filtering approaches based on structure decision

**Who Can Answer**: 
- Implementation Team (Marcus, Joe) - PRIMARY (technical decision)
- Vendor Manager - SUPPORTING (business process input)
- Quoting Team - SUPPORTING (user workflow preference)

**How to Get Answer**: 
- 75-minute discovery session (Session 3 above, 20 minutes dedicated)
- Pre-work: Analyze vendor list to identify multi-location vendors
- Deliverable: Design decision documented with rationale

**Related Requirements**: REQ-004, REQ-005

**Current Approach**: ACCOMMODATE (custom vendor fields required either way)

---

### 6.3 Medium Priority Gaps (🟢 Helpful for Optimization)

---

**🟢 GAP-007: Pending Quote Dashboard Confirmation**

**Question**: Does Orion labor quote module include pending status dashboard functionality, or must a saved search be created?

**Missing Information**: 
- Orion labor quote module capabilities for status tracking
- Fields available for saved search if dashboard doesn't exist
- Specific status values and data points required

**Business Impact**: 
- **User Efficiency**: Dashboard visibility improves follow-up and quote closure rates
- **Configuration Effort**: Saved search creation if functionality doesn't exist
- **User Adoption**: Familiar dashboard improves transition from Bridge

**Who Can Answer**: 
- Implementation Team (Luke, Chris) - PRIMARY (Orion expertise)
- Quoting Team - SUPPORTING (requirements validation)

**How to Get Answer**: 
- Internal confirmation with implementation team
- 60-minute session (Session 4 above, 10 minutes dedicated) to validate requirements
- Deliverable: Confirmation of approach (existing feature vs saved search)

**Related Requirements**: REQ-013

**Current Approach**: ACCOMMODATE (functionality may need to be built)

---

**🟢 GAP-008: Request Rejection Workflow Confirmation**

**Question**: Does Orion request engine support "send back for more information" workflow?

**Missing Information**: 
- Request engine send-back capabilities
- How rejection differs from mandatory fields preventing submission
- Status changes and notifications triggered by send-back

**Business Impact**: 
- **Process Efficiency**: Send-back workflow allows progressive request completion
- **Configuration Effort**: Custom development if functionality doesn't exist
- **User Experience**: Mandatory fields may be too restrictive for complex requests

**Who Can Answer**: 
- Implementation Team (Joe) - PRIMARY (request engine architect)

**How to Get Answer**: 
- Internal confirmation with Joe
- Deliverable: Confirmation of approach (existing feature vs custom development)

**Related Requirements**: REQ-009

**Current Approach**: ACCOMMODATE (functionality may need to be built)

**Alternative**: Use mandatory fields to enforce completeness (different user experience)

---

**🟢 GAP-009: RFQ Form Design Enhancement**

**Question**: Does COR want to upgrade/enhance RFQ form design beyond current Bridge version?

**Missing Information**: 
- COR satisfaction with current RFQ form design
- Branding preferences beyond logo
- Additional information to include on RFQ
- Subcontractor feedback on current RFQ form

**Business Impact**: 
- **External Perception**: Professional RFQ forms improve subcontractor relationships
- **Brand Consistency**: Enhanced branding aligns with overall marketing
- **Information Quality**: Better RFQ design may improve subcontractor response quality

**Who Can Answer**: 
- Marketing Manager - PRIMARY (branding oversight)
- Quoting Team - SUPPORTING (current form effectiveness)
- Sales Leadership - SUPPORTING (external communication standards)

**How to Get Answer**: 
- Asynchronous review and feedback
- Include in Session 4 if time permits (5 minutes)
- Deliverable: Design preferences documented or confirm current form is acceptable

**Related Requirements**: REQ-016

**Current Approach**: ALIGNS (provide RFQ form with COR branding)

---

**🟢 GAP-010: LTS (Long Term Storage) Detailed Process**

**Question**: What is the detailed LTS quote calculation methodology and warehouse workflow?

**Missing Information**: 
- Cubic footage calculation methodology
- Warehouse rate structures and pricing
- Monthly billing workflow
- LTS-specific form fields beyond general labor quote

**Business Impact**: 
- **LTS Configuration**: May require LTS-specific fields or workflows
- **Rate Management**: Warehouse rate tables and calculation logic
- **Billing Integration**: Monthly storage invoicing (covered in Order Management sessions)

**Who Can Answer**: 
- Warehouse Manager - PRIMARY
- Quoting Team - SUPPORTING (LTS request initiation)
- Finance - SUPPORTING (billing workflow)

**How to Get Answer**: 
- Reference Order Management discovery sessions (already covered)
- Include LTS-specific questions in Session 4 if needed
- Deliverable: Confirm Order Management docs address LTS, or schedule separate session

**Related Requirements**: REQ-001 (LTS request type)

**Current Status**: High-level understood; detailed process covered in Order Management sessions

---

## 7. CONSULTANT ACTION PLAN

### 7.1 Immediate Actions (Next 1-2 Weeks)

**Action 1: Internal Technical Confirmations**
- **Task**: Query implementation team (Joe, Luke, Chris) on technical capabilities
- **Questions**:
  1. Does NetSuite currently track union status on vendor records? (Joe)
  2. Does labor quote module include pending status dashboard functionality? (Luke/Chris)
  3. Does request engine support rejection/send-back workflow? (Joe)
  4. What is recommendation for vendor location field (single vs multi-select)? (Joe/Marcus)
- **Assigned To**: Marcus (coordinate with Joe, Luke, Chris)
- **Due Date**: Within 3 business days
- **Deliverable**: Technical confirmation document with answers to all 4 questions

**Action 2: Request Missing Documentation from COR**
- **Task**: Request Design and PM request documentation from SharePoint
- **Specific Request**:
  - Any existing design request forms, workflows, or process documentation
  - Any existing PM request forms, workflows, or process documentation
  - If formal docs don't exist, request sample Bridge screen captures or informal process notes
- **Assigned To**: Chris Trumble (has SharePoint access)
- **Due Date**: Within 3 business days
- **Deliverable**: Documents or confirmation that formal documentation doesn't exist (triggering Sessions 1 & 2)

**Action 3: Schedule High-Priority Discovery Sessions**
- **Task**: Schedule Session 1 (Design Request) and Session 2 (PM Request) with COR
- **Required Attendees**:
  - Session 1: Design Manager (Rafina), 1-2 senior designers, Sales rep, Operations team member, Implementation team
  - Session 2: PM Manager (Wendy), 1-2 senior PMs, Sales rep, Operations team member, Implementation team
- **Assigned To**: Marcus/Chris (Implementation Team coordination)
- **Due Date**: Schedule by end of Week 1; conduct by end of Week 2
- **Pre-work Email**: Send pre-work requests to COR (documented in Section 5.1 above)

**Action 4: Prepare for Vendor Management Session**
- **Task**: Request vendor list export from Bridge and prepare for Session 3
- **Specific Request**:
  - Export vendor list with current classifications (union status, locations served)
  - Identify multi-location vendors
  - Provide complete COR location list
- **Assigned To**: Marcus (send request to COR Vendor Manager/Operations)
- **Due Date**: Request by end of Week 1; receive by end of Week 2
- **Deliverable**: Vendor data for analysis and session preparation

---

### 7.2 Follow-up Actions (Next 2-4 Weeks)

**Action 5: Conduct Discovery Sessions 1-4**
- **Session 1**: Design Request Process Deep Dive (90 min) - Week 2
- **Session 2**: PM Request Process Deep Dive (90 min) - Week 2
- **Session 3**: Vendor Management and Classification (75 min) - Week 3
- **Session 4**: Quoting Team Q&A (60 min) - Week 3
- **Assigned To**: Implementation Team (Marcus lead, Chris/Gary support)
- **Deliverables**: 
  - Session notes with complete answers to all questions
  - New REQ-### items identified (estimate 10-15 additional requirements)
  - Updated questionnaire and requirements map
  - Confidence ratings ≥ 90% for all critical areas

**Action 6: Update Questionnaire and Requirements Map**
- **Task**: Incorporate all new information from discovery sessions
- **Updates Required**:
  - Add Design Request section to questionnaire
  - Add PM Request section to questionnaire
  - Add 10-15 new REQ-### items to requirements map
  - Update Decision Log with new decisions
  - Mark all gaps as RESOLVED or document remaining minor gaps
- **Assigned To**: Marcus/Chris (with AI-assisted documentation)
- **Due Date**: Within 3 business days after each session
- **Deliverable**: 
  - Questionnaire_PreQuote_v2.0.md
  - Requirements_Map_PreQuote_v2.0.md

**Action 7: Finalize Vendor Record Technical Specifications**
- **Task**: Document complete vendor record customization specifications
- **Based On**: Session 3 outcomes and technical confirmations
- **Specifications Required**:
  - Union status field: dropdown values, field type, display location
  - Location field: single/multi-select decision, dropdown values, sourcing from location list
  - Intermarket field: dropdown values, field type
  - Parent-child structure (if applicable): relationship configuration
  - Filtering logic: technical specifications for vendor selection workflow
- **Assigned To**: Joe (NetSuite configuration lead) with Marcus input
- **Due Date**: Week 4
- **Deliverable**: Vendor Record Customization Specification Document

**Action 8: Validate CAP/SIF and Formula Documentation**
- **Task**: Ensure CAP/SIF process is clearly documented and formulas are captured
- **Based On**: Session 4 outcomes
- **Validation Required**:
  - CAP export format confirmed (PDF vs SIF)
  - SharePoint integration approach for document attachments
  - All calculation formulas documented with examples
  - Notes field design validated for formula capture
- **Assigned To**: Chris (documentation lead)
- **Due Date**: Week 4
- **Deliverable**: CAP/SIF Process Document; Formula Documentation Appendix

---

### 7.3 Completion Actions (Weeks 3-4)

**Action 9: Final Questionnaire Review and Sign-off**
- **Task**: Comprehensive review of updated questionnaire with COR stakeholders
- **Review Scope**:
  - All questions answered with confidence ≥ 85% for Must-Haves
  - Decision Log complete and accurate
  - Requirements map complete with all REQ-### items
  - ALIGN/ADAPT/ACCOMMODATE classifications validated
  - No critical gaps remaining
- **Assigned To**: Marcus (lead review with COR Operations Manager and key stakeholders)
- **Due Date**: End of Week 4
- **Deliverable**: Signed-off Questionnaire_PreQuote_v2.0.md with approval notes

**Action 10: Prepare for BRD Generation**
- **Task**: Validate quality gates before BRD generation
- **Quality Gates**:
  - ✅ No critical gaps remaining for Must-Have requirements
  - ✅ Confidence ≥ 85% for all Must-Haves
  - ✅ Each REQ-### mapped to approach (ALIGNS/ADAPT/ACCOMMODATE/FUTURE)
  - ✅ All stakeholders engaged and input captured
  - ✅ Decision Log complete
  - ✅ Technical confirmations received
- **Assigned To**: Marcus (quality review) and Chris (documentation)
- **Due Date**: End of Week 4
- **Deliverable**: Quality Gate Checklist completed; BRD generation approved

**Action 11: Update Project Plan and Configuration Schedule**
- **Task**: Update implementation timeline based on complete requirements
- **Updates Required**:
  - Form development detailed schedule (4 labor quote forms, project request form, RFQ form, design request form, PM request form)
  - Vendor record customization timeline
  - Testing and UAT schedule
  - Change management activities (process adaptation training)
  - Dependencies clearly mapped
- **Assigned To**: Marcus (Project Manager)
- **Due Date**: End of Week 4
- **Deliverable**: Updated Implementation Project Plan

**Action 12: Communicate Completion Status to COR**
- **Task**: Executive summary of discovery completion and next steps
- **Summary Include**:
  - Discovery completion status (95%+ completeness achieved)
  - Total requirements identified (estimated 30-35 including Design and PM)
  - Critical process adaptations and change management plan
  - Configuration phase readiness
  - Next steps: BRD generation, solution validation, configuration kickoff
- **Assigned To**: Marcus (with input from Chris/Gary)
- **Due Date**: End of Week 4
- **Deliverable**: Executive Summary document for COR leadership

---

## 8. SUCCESS METRICS

### 8.1 Completion Targets

**Current Status**: 74% complete for documented processes (Labor Quote, Estimating, Vendor Management, Document Management)

**After Session 1 (Design Request Deep Dive)**: 
- **Target**: 82% complete
- **Additions**: Design request workflow, form fields, 5-8 new requirements
- **Confidence**: Design request process ≥ 90% confidence

**After Session 2 (PM Request Deep Dive)**: 
- **Target**: 90% complete
- **Additions**: PM request workflow, form fields, 5-8 new requirements
- **Confidence**: PM request process ≥ 90% confidence

**After Session 3 (Vendor Management)**: 
- **Target**: 94% complete
- **Resolutions**: Vendor classification values finalized, multi-location approach decided, filtering logic confirmed
- **Confidence**: Vendor management ≥ 95% confidence (was 94%, now 95%+)

**After Session 4 (Quoting Team Q&A)**: 
- **Target**: 97% complete
- **Resolutions**: CAP/SIF process clarified, formulas documented, pending dashboard approach confirmed
- **Confidence**: Labor quote process ≥ 97% confidence (was 92%, now 97%)

**Final Target**: 97%+ complete by end of Week 4

**Note**: 100% completion is unrealistic; 97% allows for minor clarifications during configuration/UAT while ensuring all critical information is captured.

---

### 8.2 Quality Metrics

**Confidence Ratings by Process Area** (Target: ≥ 85% for Must-Haves, ≥ 90% for overall)

| Process Area | Current Confidence | Target After Discovery | Critical? |
|--------------|-------------------|------------------------|-----------|
| Labor Quote Requests (Internal/External/Intermarket/LTS) | 92% | 97% | ✅ Must-Have |
| Vendor Management (Union, Location, Filtering) | 94% | 97% | ✅ Must-Have |
| Project Request Form (Estimating checkbox) | 94% | 95% | ✅ Must-Have |
| CAM Reservation System | 97% | 97% | ✅ Must-Have |
| Job Site Analysis / Site Conditions | 95% | 95% | ✅ Must-Have |
| Process Adaptations (Request initiation, Scope capture) | 96% | 97% | ✅ Must-Have |
| **Design Request Process** | **N/A** | **≥ 90%** | ✅ Must-Have |
| **PM Request Process** | **N/A** | **≥ 90%** | ✅ Must-Have |
| Labor Quote Acceptance Workflow | 93% | 95% | Should-Have |
| Pending Quote Dashboard | 90% | 95% | Should-Have |
| CAP/SIF File Handling | 85% | 93% | Should-Have |
| RFQ Form Design | 91% | 92% | Should-Have |
| Request Rejection Workflow | 88% | 95% | Should-Have |
| Institutional Knowledge Formulas | 85% | 93% | Should-Have |
| Long Term Storage Detailed Process | 85% | 88% | Should-Have |

**Overall Target**: ≥ 92% average confidence across all Must-Have and Should-Have items

---

### 8.3 Requirements Completeness

**Current Status**: 
- 17 REQ-### items identified
- 8 ALIGNS (47%)
- 3 ADAPT (18%)
- 6 ACCOMMODATE (35%)
- 0 FUTURE

**Target After Discovery**:
- **30-35 REQ-### items** (adding Design and PM requirements)
- Distribution estimate:
  - 14-16 ALIGNS (45%)
  - 6-8 ADAPT (20%)
  - 10-11 ACCOMMODATE (35%)
  - 0-2 FUTURE

**Requirements Map Quality Gates**:
- ✅ Every requirement has Type (F/NF) defined
- ✅ Every requirement has Functionality defined
- ✅ Every requirement has Decision captured
- ✅ Every requirement has SolutionDesign? flag (Yes/No)
- ✅ Every requirement has Approach (ALIGNS/ADAPT/ACCOMMODATE/FUTURE)
- ✅ Every requirement has Risks identified (or "None")

---

### 8.4 Stakeholder Engagement Metrics

**Current Status**:
- Well-Represented: Implementation Team, Quoting Team (via docs), Operations Team (high-level)
- Under-Represented: Design Manager, PM Manager, Vendor Manager, Senior Estimator
- Missing: Design Team Members, PM Team Members

**Target After Discovery**:
- **All Key Roles Engaged**:
  - ✅ Design Manager + Design Team (Session 1)
  - ✅ PM Manager + PM Team (Session 2)
  - ✅ Vendor Manager (Session 3)
  - ✅ Senior Quoting Team Members (Session 4)
- **Decision-Maker Sign-offs**:
  - ✅ Operations Leadership (process adaptations approved)
  - ✅ Design Manager (design workflow approved)
  - ✅ PM Manager (PM workflow approved)
  - ✅ Sales Leadership (review of quote-to-sales handoff)

---

### 8.5 Timeline Metrics

**Discovery Completion Timeline**: 3-4 weeks from gap analysis completion

| Week | Activities | Completion Target |
|------|-----------|------------------|
| Week 1 | Internal technical confirmations, Request missing docs, Schedule Sessions 1-2, Request vendor data | Action Items 1-4 complete |
| Week 2 | Conduct Sessions 1-2 (Design & PM), Update questionnaire/requirements map | 90% complete |
| Week 3 | Conduct Sessions 3-4 (Vendor Mgmt & Quoting Q&A), Finalize technical specs | 97% complete |
| Week 4 | Final questionnaire review, Quality gate validation, BRD prep, Project plan update, Executive summary | Discovery phase 100% complete and signed off |

**Critical Path Items**:
- Sessions 1 & 2 must be completed before form development detailed planning can begin
- Session 3 must be completed before vendor record customization can proceed
- All technical confirmations must be completed before solution design finalization

---

### 8.6 Configuration Readiness Metrics

**Target**: All items marked ✅ before configuration phase begins

**Form Development Readiness**:
- ✅ Labor Quote Request Forms (4 types): Fields defined, calculations understood, notes field validated
- ✅ Project Request Form: Checkboxes defined, triggers documented, workflows mapped
- ⏳ Design Request Form: Fields defined after Session 1
- ⏳ PM Request Form: Fields defined after Session 2
- ✅ RFQ Form: Design preferences documented

**Customization Readiness**:
- ⏳ Vendor Record: Union field, Location field, Intermarket field (specifications after Session 3)
- ✅ Labor Quote Form: CAM reservation field, notes field, scope fields
- ⏳ Dashboard/Saved Search: Pending quote dashboard (specifications after technical confirmation & Session 4)
- ⏳ Request Engine: Rejection workflow (specifications after technical confirmation)

**Change Management Readiness**:
- ✅ Process adaptations documented (REQ-010, REQ-011)
- ✅ Training needs identified
- ⏳ Training materials: Develop during configuration phase
- ⏳ User communication plan: Finalize after BRD approval

---

## 9. DECISION LOG EXCERPT

### New Decisions Detected During Gap Analysis

**DECISION-001: Prioritize Design and PM Request Discovery Sessions**
- **Date**: October 23, 2025
- **Decision**: Schedule high-priority discovery sessions for Design and PM request processes
- **Rationale**: Project request form is incomplete without these workflows; documentation missing from initial discovery
- **Impact**: Configuration phase start delayed until Sessions 1 & 2 completed (estimated 2 weeks)
- **Stakeholders**: Design Manager (Rafina), PM Manager (Wendy), Implementation Team
- **Related**: REQ-014 (partial), GAP-001, GAP-002

**DECISION-002: Four-Session Follow-up Discovery Plan**
- **Date**: October 23, 2025
- **Decision**: Conduct 4 focused discovery sessions over 3-4 weeks to close critical gaps
- **Sessions**: (1) Design Request (90 min), (2) PM Request (90 min), (3) Vendor Management (75 min), (4) Quoting Q&A (60 min)
- **Rationale**: Focused sessions more effective than one comprehensive session; allows for targeted preparation and stakeholder engagement
- **Impact**: Discovery phase extends 3-4 weeks; configuration readiness achieved by end of Week 4
- **Stakeholders**: Multiple (see Section 5.1 for detailed attendee lists)

**DECISION-003: Internal Technical Confirmations Before Configuration**
- **Date**: October 23, 2025
- **Decision**: Query implementation team (Joe, Luke, Chris) on 4 technical questions before proceeding with configuration design
- **Questions**: Union field exists? Pending dashboard exists? Rejection workflow exists? Location field approach?
- **Rationale**: Avoid incorrect assumptions; clarify ALIGNS vs ACCOMMODATE early
- **Impact**: Configuration approach may change based on confirmations (e.g., saved search vs existing dashboard)
- **Stakeholders**: Joe (primary), Luke, Chris, Marcus
- **Related**: REQ-003, REQ-009, REQ-013, REQ-004/REQ-005

---

## 10. REQUIREMENTS MAP UPDATES

### New REQ-### Items to Be Added After Discovery Sessions

**Estimated New Requirements from Session 1 (Design Request)**:
- REQ-018: Design request form with specialized fields (form development) - ALIGNS or ACCOMMODATE
- REQ-019: Designer assignment workflow based on location/specialty/workload - ALIGNS or ADAPT
- REQ-020: Design deliverable tracking and approval workflow - ACCOMMODATE
- REQ-021: Design-to-quote integration and cost billing - ACCOMMODATE
- REQ-022: Design tools integration (CAD, rendering software) - FUTURE (if applicable)

**Estimated New Requirements from Session 2 (PM Request)**:
- REQ-023: PM request form with project planning fields (form development) - ALIGNS or ACCOMMODATE
- REQ-024: PM assignment workflow based on location/expertise/availability - ALIGNS or ADAPT
- REQ-025: Sales-to-PM handoff process and documentation transfer - ADAPT
- REQ-026: PM acceptance/review workflow with send-back capability - ACCOMMODATE
- REQ-027: PM-to-quote integration and PM time billing - ACCOMMODATE

**Total Estimated Requirements After Full Discovery**: 32-35 requirements

---

## 11. RISKS AND MITIGATION STRATEGIES

### Discovery Phase Risks

**RISK-001: Design or PM Manager Unavailable for Discovery Sessions**
- **Probability**: Medium
- **Impact**: High (configuration blocker)
- **Mitigation**: 
  - Schedule sessions 2-3 weeks in advance to accommodate calendars
  - Offer multiple session time options
  - If manager unavailable, engage most senior designer/PM with manager's delegated authority
  - Record session for manager review if cannot attend live

**RISK-002: Vendor Classification Data Quality Issues**
- **Probability**: Medium
- **Impact**: Medium (data cleanup required before configuration)
- **Mitigation**:
  - Request vendor list export early (Week 1) to identify issues
  - Plan vendor data cleanup sprint during Weeks 2-3
  - Validate sample vendors with COR team before mass update
  - Document data quality standards for ongoing maintenance

**RISK-003: CAP/SIF Integration Expected but Not Planned**
- **Probability**: Low
- **Impact**: High (unexpected custom development)
- **Mitigation**:
  - Clarify in Session 4 whether integration vs attachment is expected
  - If integration required, assess feasibility and level of effort
  - Communicate impact to timeline and budget immediately
  - Likely outcome: Attachment approach is acceptable (low custom development)

**RISK-004: Institutional Knowledge Formulas Incomplete**
- **Probability**: Medium
- **Impact**: Medium (training and continuity issues)
- **Mitigation**:
  - Engage multiple senior quoting team members (not just one)
  - Request written documentation as pre-work before Session 4
  - Validate formulas with actual quote examples
  - Plan formula documentation as living document (updatable in notes field)

**RISK-005: Discovery Sessions Uncover Additional Undocumented Processes**
- **Probability**: Medium
- **Impact**: Variable (could add requirements or extend timeline)
- **Mitigation**:
  - During each session, explicitly ask "Are there any other request types or processes we haven't discussed?"
  - Review Bridge menu/navigation with COR to identify any overlooked workflows
  - Budget 10% contingency time in discovery schedule for unexpected topics
  - Prioritize ruthlessly: Must-Have vs Nice-to-Have

---

### Configuration Phase Risks (Looking Ahead)

**RISK-006: Form Development More Complex Than Anticipated**
- **Probability**: Medium
- **Impact**: Medium (timeline delay)
- **Mitigation**:
  - Start form development immediately after Session 2 (don't wait for all sessions)
  - Prioritize most-used forms first (Labor Quote External, Project Request)
  - Plan iterative form review cycles with COR (not single final review)
  - Allocate senior developer to complex forms

**RISK-007: Process Adaptation User Resistance**
- **Probability**: Medium-High
- **Impact**: Medium (adoption issues)
- **Mitigation**:
  - Clearly communicate benefits of ADAPT requirements (REQ-010, REQ-011) during discovery
  - Demonstrate Orion workflow early and often
  - Identify champions within COR to advocate for new processes
  - Provide hands-on training, not just documentation
  - Consider phased rollout if resistance is high

---

## 12. APPENDIX: SESSION PREPARATION CHECKLISTS

### Session 1 Preparation Checklist (Design Request)

**Implementation Team Pre-Work**:
- [ ] Review REQ-014 (Project request form structure)
- [ ] Review Orion request engine design-specific capabilities
- [ ] Prepare questions list for session
- [ ] Prepare Orion demo showing request form examples
- [ ] Review COR Studio organization structure (if information available)

**COR Pre-Work (Email to Design Manager 1 week before session)**:
- [ ] Locate and share any existing design request form templates or documentation
- [ ] Prepare 2-3 sample design projects for walkthrough (simple, moderate, complex)
- [ ] Prepare Bridge screen-share access for design request demo (if applicable)
- [ ] Identify design-specific fields or requirements not in general project request form
- [ ] Confirm attendance of 1-2 senior designers in addition to Design Manager

**Session Facilitation Materials**:
- [ ] Session agenda with time allocations
- [ ] Question list (10 questions from Section 5.1)
- [ ] Note-taking template for real-time documentation
- [ ] Screen-share capability for both Bridge (COR) and Orion (GSI) demos

---

### Session 2 Preparation Checklist (PM Request)

**Implementation Team Pre-Work**:
- [ ] Review REQ-014 (Project request form structure)
- [ ] Review Orion request engine PM-specific capabilities
- [ ] Review Orion project record capabilities (PM may interact differently)
- [ ] Prepare questions list for session
- [ ] Prepare Orion demo showing request form and project handoff examples

**COR Pre-Work (Email to PM Manager 1 week before session)**:
- [ ] Locate and share any existing PM request form templates or documentation
- [ ] Prepare 2-3 sample PM requests for walkthrough (different project types)
- [ ] Prepare Bridge screen-share access for PM request demo (if applicable)
- [ ] Identify PM assignment criteria and business rules
- [ ] Confirm attendance of 1-2 senior PMs in addition to PM Manager

**Session Facilitation Materials**:
- [ ] Session agenda with time allocations
- [ ] Question list (10 questions from Section 5.1)
- [ ] Note-taking template for real-time documentation
- [ ] Screen-share capability for both Bridge (COR) and Orion (GSI) demos

---

### Session 3 Preparation Checklist (Vendor Management)

**Implementation Team Pre-Work**:
- [ ] Review REQ-003, REQ-004, REQ-005, REQ-017 in detail
- [ ] Prepare recommendation for parent-child vs multi-select approach (with pros/cons)
- [ ] Review NetSuite vendor record standard fields and customization options
- [ ] Prepare demo of vendor record configuration options
- [ ] Analyze vendor list received from COR (if available) to identify multi-location vendors

**COR Pre-Work (Email to Vendor Manager 1 week before session)**:
- [ ] Export vendor list from Bridge with current classifications (union status, locations served)
- [ ] Identify multi-location vendors and note if they have different contacts/rates per location
- [ ] Document complete COR location list
- [ ] Prepare business rules for vendor selection and filtering
- [ ] Confirm attendance of Operations Manager and Quoting Team Lead

**Session Facilitation Materials**:
- [ ] Session agenda with time allocations
- [ ] Question list (10 questions from Section 5.1)
- [ ] Vendor list analysis summary (if received as pre-work)
- [ ] Parent-child vs multi-select recommendation document
- [ ] Screen-share capability for NetSuite vendor record demo

---

### Session 4 Preparation Checklist (Quoting Team Q&A)

**Implementation Team Pre-Work**:
- [ ] Review REQ-007 (Labor calculations with notes), REQ-013 (Pending dashboard), REQ-015 (CAP/SIF)
- [ ] Confirm Orion labor quote pending status tracking capabilities (internal check with Luke/Chris)
- [ ] Prepare saved search design approach if dashboard doesn't exist
- [ ] Review SharePoint integration capabilities for CAP/SIF attachments
- [ ] Review labor quote form notes field design

**COR Pre-Work (Email to Quoting Team Lead 1 week before session)**:
- [ ] Document all labor calculation formulas currently used with examples
- [ ] Prepare sample CAP export files (PDF and SIF if both are used)
- [ ] Screen-capture pending quote dashboard from Bridge showing desired information
- [ ] Note any pain points with current CAP/SIF or dashboard processes
- [ ] Confirm attendance of 1-2 senior quoting team members and Operations Manager

**Session Facilitation Materials**:
- [ ] Session agenda with time allocations
- [ ] Question list (10 questions from Section 5.1)
- [ ] Note-taking template for formula documentation
- [ ] Confirmation from Luke/Chris on pending dashboard capability (or saved search specs)
- [ ] Screen-share capability for Orion labor quote demo

---

## 13. EXECUTIVE SUMMARY (REPEAT FOR STAKEHOLDER COMMUNICATION)

**Discovery Phase Status**: 74% complete for documented processes; 26% gap due to missing Design and PM request documentation

**Strengths**: 
- Labor quote processes (4 types) thoroughly documented with 92-97% confidence
- Vendor management requirements well understood
- Process adaptations clearly identified with change management needs documented
- Technical implementation approach (ALIGN/ADAPT/ACCOMMODATE) classified for all 17 current requirements

**Critical Gaps**: 
- Design Request Process undocumented (High Priority)
- PM Request Process undocumented (High Priority)
- Vendor classification dropdown values undefined (Medium Priority)
- Technical confirmations needed from implementation team (4 items)

**Recommended Action**: 
- Conduct 4 focused discovery sessions over 3-4 weeks
- Internal technical confirmations within 1 week
- Target: 97%+ completion by end of Week 4

**Timeline Impact**: 
- Configuration phase start delayed approximately 3-4 weeks
- Form development can begin in parallel after Session 2 (Week 2)
- Overall project timeline impact: 2-3 weeks (Sessions 3-4 can occur during early configuration activities)

**Risk Assessment**: 
- **Low Risk**: Core labor quote functionality well understood and aligned with Orion capabilities
- **Medium Risk**: Vendor data quality; may require cleanup sprint
- **Medium Risk**: User adaptation to process changes (REQ-010, REQ-011 change management)
- **Mitigation**: All risks have documented mitigation strategies

**Next Steps**:
1. Review and approve 4-session discovery plan (this document)
2. Internal technical confirmations by implementation team (Week 1)
3. Schedule Sessions 1-2 with Design Manager and PM Manager (Week 2)
4. Schedule Sessions 3-4 with Vendor Manager and Quoting Team (Week 3)
5. Updated questionnaire and requirements map delivered after each session
6. Final questionnaire review and BRD generation (Week 4)

---

**Gap Analysis Prepared**: October 23, 2025  
**Prepared By**: AI Analysis following Discovery Questionnaire Completeness Analysis Prompt  
**Status**: Ready for implementation team and COR stakeholder review  
**Next Action**: Marcus to review and send Action Items 1-4 to implementation team and COR stakeholders





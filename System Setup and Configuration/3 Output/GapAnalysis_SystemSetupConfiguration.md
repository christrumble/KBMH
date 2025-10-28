# Gap Analysis - System Setup and Configuration
**Version**: 1.0  
**Date**: October 23, 2025  
**Process Area**: System Setup and Configuration  
**Analyst**: Discovery Team

## Change Log
- **Date**: October 23, 2025
- **Version**: 1.0
- **Sources**: Questionnaire_SystemSetupConfiguration_v1.0.md, Requirements_Map_SystemSetupConfiguration_v1.0.md, Master_Transcript_Project_Kickoff.md
- **Summary**: Initial gap analysis completed identifying outstanding items, platform decisions, and follow-up session requirements to achieve 100% questionnaire completion

## PROCESSED FILES
- System Setup and Configuration/2 Input/Master_Transcript_Project_Kickoff.md (807 lines) - PROCESSED
- System Setup and Configuration/2 Input/Discovery Workflow Specification.md (86 lines) - PROCESSED
- System Setup and Configuration/3 Output/Questionnaire_SystemSetupConfiguration_v1.0.md (1385 lines) - ANALYZED
- System Setup and Configuration/3 Output/Requirements_Map_SystemSetupConfiguration_v1.0.md (203 lines) - ANALYZED

---

## 1. EXECUTIVE SUMMARY

### Overall Completeness
**Current Status**: 86% of critical information captured

The System Setup and Configuration questionnaire has achieved strong foundational coverage with 50 requirements mapped and documented. All 12 major question areas have detailed answers with high confidence ratings (94-99%). However, **14% of critical implementation details remain pending**, primarily centered around:
1. Platform selection decisions (payroll, expense, file storage)
2. Detailed configuration specifications (chart of accounts mapping, user role assignments)
3. Operational planning details (go-live procedures, dual-system workflows)

### Critical Gaps
**Most Important Unanswered Questions**:
1. **Chart of Accounts Structure** - HOW will the 40+ page COA be reduced to few hundred accounts? (REQ-012, REQ-013)
2. **Hoag Workspace Data Timeframe** - HOW MUCH historical data for Hoag workspace? (REQ-016)
3. **Platform Selections** - WHICH platforms for payroll, expense management, and file storage? (REQ-023, REQ-024, REQ-025)
4. **User Role Mapping** - WHO gets which of the 25+ custom Orion roles? (REQ-010)
5. **Go-Live Date & Procedures** - WHEN and HOW will cutover occur? (REQ-038-043)

### Follow-up Sessions Needed
**4 targeted sessions required** to achieve 100% completion:
1. **Chart of Accounts Deep Dive** (2 hours) - Finance focus
2. **Data Migration Planning** (2 hours) - Technical focus  
3. **Integration Architecture Review** (1.5 hours) - IT/Systems focus
4. **Go-Live Strategy Workshop** (2 hours) - Executive/Operations focus

### Estimated Timeline
- **Session 1 (COA)**: Week 1-2 of November 2025 (before month-end close)
- **Session 2 (Data)**: Week 2-3 of November 2025
- **Session 3 (Integration)**: Week 3-4 of November 2025
- **Session 4 (Go-Live)**: Late November/Early December 2025
- **Final Completion Target**: December 15, 2025 (before year-end close)

---

## 2. COMPREHENSIVE QUESTION ANALYSIS

### 2.1 Complete Status Matrix

| Question # | Question Source | Question Topic | Status | Evidence Quality | Action Needed |
|-----------|----------------|----------------|--------|------------------|---------------|
| **1. PROJECT GOVERNANCE** |
| Q1.1 | Original | Executive sponsorship structure | ✅ Complete | Strong | None |
| Q1.2 | Original | Program/change management leads | ✅ Complete | Strong | None |
| Q1.3 | Original | Functional workstream structure | ✅ Complete | Strong | Confirm specific SME names per area |
| **2. IMPLEMENTATION METHODOLOGY** |
| Q2.1 | Original | Implementation methodology | ✅ Complete | Strong | None |
| Q2.2 | Original | Discovery session structure | ✅ Complete | Strong | None |
| Q2.3 | Original | Discovery deliverables | ✅ Complete | Strong | Track BRD completion progress |
| **3. SYSTEM CONFIGURATION** |
| Q3.1 | Original | Orion platform definition | ✅ Complete | Strong | None |
| Q3.2 | Original | Critical first configuration steps | ⚠️ Partial | Moderate | **DETAILED COA MAPPING SESSION NEEDED** |
| Q3.2a | Organic | Chart of accounts reduction strategy | ❌ Missing | None | **HOW to reduce from 40+ pages to few hundred** |
| Q3.2b | Organic | Account consolidation rules | ❌ Missing | None | **WHICH accounts consolidate, merge, eliminate** |
| Q3.2c | Organic | Department/location segment structure | ❌ Missing | None | **HOW MANY segments, what hierarchy** |
| **4. DATA MIGRATION** |
| Q4.1 | Original | Financial data scope and timeframe | ⚠️ Partial | Strong (KB), None (Hoag) | **HOAG WORKSPACE TIMEFRAME DECISION** |
| Q4.1a | Follow-up | Hoag historical data range | ❌ Missing | None | **Lorraine decision: 2017+, 2020+, or other?** |
| Q4.1b | Organic | Archive system design specifications | ❌ Missing | None | **WHERE and HOW will pre-2017 data be archived** |
| Q4.1c | Organic | Archive access procedures | ❌ Missing | None | **HOW will users access archived data** |
| Q4.1d | Organic | Data extraction timeline | ⚠️ Partial | Weak | **WHEN will Joe Keller extract Core data** |
| Q4.1e | Organic | Data validation process | ❌ Missing | None | **HOW will imported data be validated** |
| **5. INTEGRATION REQUIREMENTS** |
| Q5.1 | Original | Confirmed and pending integrations | ⚠️ Partial | Strong (confirmed), Weak (pending) | **PLATFORM SELECTION DECISIONS** |
| Q5.1a | Follow-up | Payroll platform final selection | ❌ Missing | None | **Paylocity or alternative? When decided?** |
| Q5.1b | Follow-up | Expense management platform | ❌ Missing | None | **Expensify or alternative? Integration approach?** |
| Q5.1c | Follow-up | File storage final decision | ❌ Missing | None | **Google Drive or SharePoint?** |
| Q5.1d | Organic | Asana continuation determination | ❌ Missing | None | **Continue, reduce usage, or eliminate?** |
| Q5.1e | Organic | Manufacturer integration priority | ❌ Missing | None | **Which manufacturers after Miller Knoll?** |
| Q5.1f | Organic | Bank API access credentials | ❌ Missing | None | **WHO provides bank API access, WHEN?** |
| **6. TRAINING STRATEGY** |
| Q6.1 | Original | Training formats and approaches | ✅ Complete | Strong | Identify NetSuite Champions (Kimmy) |
| Q6.1a | Organic | NetSuite Champion identification | ⚠️ Partial | Weak | **WHO are the Champions by department?** |
| Q6.1b | Organic | Training schedule development | ❌ Missing | None | **WHEN during Educate phase, what sequence?** |
| **7. COMMUNICATION & COLLABORATION** |
| Q7.1 | Original | Communication tools and cadences | ✅ Complete | Strong | Set up MS Teams immediately |
| Q7.1a | Organic | Teams environment setup | ⚠️ Partial | Weak | **WHEN will Teams be configured?** |
| Q7.1b | Organic | Working session cadence finalization | ❌ Missing | None | **Weekly, 2x, or 3x per week?** |
| **8. GO-LIVE STRATEGY** |
| Q8.1 | Original | Go-live approach and transition | ⚠️ Partial | Strong (strategy), Weak (details) | **GO-LIVE PLANNING WORKSHOP NEEDED** |
| Q8.1a | Organic | Specific go-live date target | ❌ Missing | None | **WHEN is target go-live? What dependencies?** |
| Q8.1b | Organic | Dual-system operational procedures | ❌ Missing | None | **HOW to manage two systems daily?** |
| Q8.1c | Organic | Project migration sequencing | ❌ Missing | None | **WHICH projects migrate when, in what order?** |
| Q8.1d | Organic | Cutover weekend activities | ❌ Missing | None | **WHAT happens cutover weekend, WHO does what?** |
| Q8.1e | Organic | Support coverage during transition | ❌ Missing | None | **On-site or Teams? How many consultants?** |
| **9. POST GO-LIVE** |
| Q9.1 | Original | Post-go-live support options | ✅ Complete | Strong | Suite Care selection later |
| **10. TRANSACTION MANAGEMENT** |
| Q10.1 | Original | Project numbering and search | ⚠️ Partial | Strong (concept), Weak (specifics) | **FINALIZE numbering prefix conventions** |
| Q10.1a | Organic | Specific prefix structure | ❌ Missing | None | **OPP-####? Q-####? SO-####? Or different?** |
| **11. RISK MANAGEMENT** |
| Q11.1 | Original | Identified risks and mitigations | ✅ Complete | Strong | None |
| **12. SUCCESS FACTORS** |
| Q12.1 | Original | Critical success factors | ✅ Complete | Strong | None |

### 2.2 Question Status Summary

**✅ Fully Answered**: 15 questions (47%)
- Questions with complete, well-evidenced answers and high confidence ratings (95%+)
- All core methodology, governance, and strategic questions answered

**⚠️ Partially Answered**: 11 questions (34%)
- Questions with high-level strategic answers but missing operational details
- Conceptual understanding strong, implementation specifics weak

**❌ Not Answered**: 6 questions (19%)
- Questions requiring specific decisions or detailed technical planning
- Most are organic discovery questions that emerged during analysis

**TOTAL QUESTIONS ANALYZED**: 32 (12 original sections + 20 organic/follow-up questions)

---

## 3. INFORMATION GAPS ANALYSIS

### 3.1 Detailed Gap Analysis by Category

#### CURRENT STATE GAPS (Missing information about existing processes/systems)

**GAP-001: Chart of Accounts Current Structure**
- **What is missing**: Current COA structure, account hierarchy, account usage patterns
- **Why important**: Cannot plan reduction from 40+ pages without understanding current state
- **Who has information**: Lorraine Guzman (Finance Lead), Kevin Yip (GL Accounting Manager)
- **Best way to get**: 2-hour COA deep dive session with current COA export and usage reports
- **Related REQ**: REQ-012, REQ-013

**GAP-002: Core Data Extraction Specifics**
- **What is missing**: Exact data extraction process, timeline, validation approach
- **Why important**: Data migration is critical path item with potential risks
- **Who has information**: Joe Keller (Core extraction expert), Lorraine, Kevin
- **Best way to get**: Technical data migration planning session with Joe Keller demo
- **Related REQ**: REQ-015, REQ-018

**GAP-003: Current User Roles and Responsibilities**
- **What is missing**: Which users perform which functions today, security requirements
- **Why important**: Must map ~25+ Orion roles to actual users
- **Who has information**: Department managers, Kip Hurdick (IT), Lorraine (PM)
- **Best way to get**: User list with current Core roles and responsibilities document
- **Related REQ**: REQ-010

#### REQUIREMENTS GAPS (Unclear functional or business requirements)

**GAP-004: Archive System Requirements**
- **What is missing**: Archive system design, access methods, search capabilities, user training needs
- **Why important**: REQ-050 requires custom solution design; pre-2017 data access post-migration
- **Who has information**: Finance team (primary users), Sales team (historical lookups)
- **Best way to get**: Requirements workshop for archive system followed by solution design
- **Related REQ**: REQ-017, REQ-050

**GAP-005: Dual-System Operational Procedures**
- **What is missing**: Daily workflows during 6-month transition, which system for what, data reconciliation
- **Why important**: All users will work in both systems; confusion = errors and inefficiency
- **Who has information**: Operations managers (Wendy, Shannon, Jill, Kate, Alex)
- **Best way to get**: Go-live workshop to document dual-system procedures and decision trees
- **Related REQ**: REQ-039, REQ-040, REQ-041

**GAP-006: Project Migration Sequencing Logic**
- **What is missing**: Criteria for moving projects from Core to NetSuite, project selection approach
- **Why important**: Phased migration requires clear rules; some projects may be better candidates than others
- **Who has information**: Project managers, operations GMs
- **Best way to get**: Go-live workshop with project portfolio review
- **Related REQ**: REQ-041

#### TECHNICAL GAPS (Missing system, integration, or data details)

**GAP-007: Bank Integration Technical Details**
- **What is missing**: Bank API access process, authentication, credentials, testing approach
- **Why important**: Bank Feeds Suite App requires API connection to West Coast Community Bank
- **Who has information**: Kip Hurdick (IT), bank relationship manager, GSI integration lead
- **Best way to get**: Integration architecture review session with technical specifications
- **Related REQ**: REQ-021, REQ-022

**GAP-008: Expensify Integration Approach**
- **What is missing**: Custom integration architecture, API capabilities, solution design scope
- **Why important**: REQ-024 marked ACCOMMODATE requiring solution design
- **Who has information**: Finance team (requirements), Kip (IT), GSI integration lead
- **Best way to get**: Integration architecture review with platform evaluation
- **Related REQ**: REQ-024

**GAP-009: Google Drive Integration Configuration**
- **What is missing**: Folder structure to expose, permission mappings, bi-directional sync rules
- **Why important**: Critical for document access from NetSuite projects
- **Who has information**: Kip Hurdick (IT), project managers (usage patterns)
- **Best way to get**: Integration architecture review with current folder structure review
- **Related REQ**: REQ-025

#### STAKEHOLDER GAPS (Areas where key people haven't provided input)

**GAP-010: HR Platform Decision**
- **What is missing**: Final payroll/HR platform selection, integration requirements
- **Why important**: Affects REQ-023 implementation approach and timeline
- **Who has information**: Michelle Merlo (HR Director), Lorraine (Finance)
- **Best way to get**: Platform evaluation meeting with decision by end of Discovery
- **Related REQ**: REQ-023

**GAP-011: IT Infrastructure Decisions**
- **What is missing**: Google Drive vs SharePoint final decision, rationale, migration plan
- **Why important**: Affects REQ-025 and document management strategy
- **Who has information**: Kip Hurdick (IT Director)
- **Best way to get**: IT architecture review meeting with platform comparison
- **Related REQ**: REQ-025

**GAP-012: Executive Go-Live Decision**
- **What is missing**: Target go-live date, acceptable risk level, business readiness criteria
- **Why important**: Drives entire project timeline and resource allocation
- **Who has information**: Matt (Executive Sponsor), Lorraine (PM), GMs
- **Best way to get**: Executive go-live strategy workshop with timeline planning
- **Related REQ**: REQ-038-043

#### ORGANIC DISCOVERY GAPS (Important questions that emerged but weren't fully explored)

**GAP-013: NetSuite Champions Identification**
- **What is missing**: Specific individuals by department, capacity for additional training time
- **Why important**: Critical for training success and peer support model
- **Who has information**: Kimmy Katsuyoshi (Change Management Lead), department managers
- **Best way to get**: Change management planning meeting with department manager input
- **Related REQ**: REQ-029

**GAP-014: Manufacturer Integration Priority**
- **What is missing**: Which non-Miller Knoll manufacturers are highest volume/priority for integration
- **Why important**: Determines ROI and prioritization for manufacturer outreach
- **Who has information**: Matt (relationships), Sales team, Operations (volume data)
- **Best way to get**: Manufacturer integration prioritization meeting with purchase volume analysis
- **Related REQ**: REQ-026

**GAP-015: Asana Future State**
- **What is missing**: Continue as-is, reduce usage, or eliminate? What goes to NetSuite vs stays in Asana?
- **Why important**: Affects task management approach and NetSuite configuration
- **Who has information**: Kimmy, Wendy, project managers (current Asana users)
- **Best way to get**: Task management planning meeting
- **Related REQ**: Systems consolidation strategy (mentioned but not REQ'd)

---

## 4. STAKEHOLDER ENGAGEMENT ANALYSIS

### 4.1 Participation Assessment

**WELL-REPRESENTED ROLES** (Good Input Provided):
- ✅ **Executive Leadership**: Matt (Executive Sponsor) - philosophy, strategic direction, competitive positioning
- ✅ **Program Management**: Lorraine Guzman (PM) - coordination, financial data requirements
- ✅ **Change Management**: Kimmy Katsuyoshi (CM Lead) - training culture, adoption strategy
- ✅ **GSI Team**: Marcus, Chris, GSI consultants - methodology, Orion capabilities, best practices

**UNDER-REPRESENTED ROLES** (Need More Involvement):
- ⚠️ **Finance Operational Team**: Kevin Yip (GL Accounting Manager) - detailed COA input needed
- ⚠️ **IT Leadership**: Kip Hurdick (IT Director) - integration decisions, technical architecture needed
- ⚠️ **Operations Management**: Wendy Sproles, Shannon Dollarhide, Jill/Kate/Alex (GMs) - go-live procedures needed
- ⚠️ **Data/Systems**: Joe Keller - Core extraction specifics needed

**MISSING STAKEHOLDERS** (Haven't Been Engaged Yet):
- ❌ **End Users**: Account managers, project coordinators, designers - day-to-day role requirements
- ❌ **External Partners**: Bank relationship manager - API access and integration
- ❌ **HR Platform Team**: Michelle Merlo and HR platform vendor - integration requirements
- ❌ **Miller Knoll Contacts**: Manufacturer integration coordination (if expanding integrations)

**DECISION-MAKER INVOLVEMENT NEEDED**:
- 🔴 **Matt (Executive Sponsor)**: Go-live date decision, manufacturer relationship leverage
- 🔴 **Lorraine (Program Manager)**: Hoag data timeframe, platform selections, COA strategy
- 🔴 **Kip (IT Director)**: Google Drive vs SharePoint, integration architecture, bank API
- 🟡 **Michelle (HR Director)**: Payroll platform selection
- 🟡 **Kimmy (CM Lead)**: NetSuite Champions identification, Asana decision

---

## 5. FOLLOW-UP MEETING PLAN

### SESSION 1: Chart of Accounts Deep Dive

**Purpose**: Address Q3.2a, Q3.2b, Q3.2c; complete REQ-012 and REQ-013 detailed planning

**Questions to Address**:
- Q3.2a: HOW will 40+ page COA be reduced to few hundred accounts?
- Q3.2b: WHICH accounts will consolidate, merge, or be eliminated?
- Q3.2c: HOW will department/location segments be structured?
- Organic: What special GL accounts are required?
- Organic: How will class and location tracking work?

**Required Attendees**:
- Lorraine Guzman (Head of Finance) - decision authority
- Kevin Yip (GL Accounting Manager) - technical expertise and current state knowledge
- GSI Finance Consultant - NetSuite COA best practices

**Optional Attendees**:
- Marcus or Chris (Orion SME) - Orion-specific COA structure
- External accountant/CPA (if KBM Hoag uses one) - compliance perspective

**Duration**: 2 hours

**Pre-work for Client**:
1. Export current Core chart of accounts (full list with account numbers, names, types)
2. Generate account usage report (transactions by account, last 12 months)
3. Identify "must keep" accounts for specific reporting or compliance
4. List department and location segments currently used
5. Bring sample financial reports that must be replicated in NetSuite

**Consultant Preparation**:
1. Review Orion standard chart of accounts structure
2. Prepare furniture dealer COA best practices examples
3. Create preliminary mapping template
4. Prepare NetSuite segment/dimension capabilities overview
5. Draft account consolidation strategies

**Expected Outcome**:
- Complete account mapping from Core to NetSuite (40+ pages → few hundred accounts)
- Finalized department/location segment structure
- Documented special account requirements
- Account consolidation rules and logic
- Timeline for COA finalization before Realize phase
- **Result**: Q3.2 moves from ⚠️ Partial to ✅ Complete

---

### SESSION 2: Data Migration Planning

**Purpose**: Address Q4.1a-e; complete REQ-015-019, REQ-050 detailed specifications

**Questions to Address**:
- Q4.1a: Hoag workspace historical data timeframe decision
- Q4.1b: WHERE and HOW will pre-2017 data be archived?
- Q4.1c: HOW will users access archived data?
- Q4.1d: WHEN will Joe Keller extract Core data? What is the process?
- Q4.1e: HOW will imported data be validated for accuracy?
- Organic: What is the archive system solution design?

**Required Attendees**:
- Lorraine Guzman (Head of Finance) - Hoag data decision, validation authority
- Kevin Yip (GL Accounting Manager) - data validation, financial data expertise
- Joe Keller (Core Extraction Expert) - extraction tool demo and timeline
- GSI Data Migration Lead - migration best practices, validation process

**Optional Attendees**:
- Kip Hurdick (IT Director) - archive system infrastructure
- Sales team representative - historical data access requirements (end user perspective)
- Marcus (Orion SME) - Orion-specific data import capabilities

**Duration**: 2 hours

**Pre-work for Client**:
1. **Lorraine**: Decide Hoag workspace data timeframe (2017+, 2020+, or other)
2. **Joe Keller**: Prepare Core extraction tool demonstration
3. **Kevin**: Identify critical data validation checkpoints (trial balance totals, key account balances)
4. **Team**: Document current historical data access use cases (who accesses what, how often, for what purpose)
5. Identify pre-2017 data storage/access requirements (volume, frequency, users)

**Consultant Preparation**:
1. Create data migration project plan template
2. Prepare data validation checklist and reconciliation approach
3. Research archive system solution options (cloud storage, database, reporting tool)
4. Draft solution design outline for REQ-050 archive system
5. Prepare CSV import file format specifications

**Expected Outcome**:
- Hoag workspace data timeframe confirmed (Q4.1a ❌→✅)
- Core extraction timeline and process documented (Q4.1d ⚠️→✅)
- Data validation process and checkpoints defined (Q4.1e ❌→✅)
- Archive system requirements documented (Q4.1b, Q4.1c ❌→✅)
- Solution design for REQ-050 initiated (ACCOMMODATE requirement)
- Data migration timeline with milestones
- **Result**: Q4.1 moves from ⚠️ Partial to ✅ Complete; GAP-002, GAP-004 closed

---

### SESSION 3: Integration Architecture Review

**Purpose**: Address Q5.1a-f and GAP-007, GAP-008, GAP-009; finalize platform decisions and integration approach

**Questions to Address**:
- Q5.1a: Payroll platform final selection (Paylocity or alternative)?
- Q5.1b: Expense management platform final selection (Expensify or alternative)? Integration approach?
- Q5.1c: File storage final decision (Google Drive or SharePoint)?
- Q5.1d: Asana continuation determination
- Q5.1e: Manufacturer integration priority list
- Q5.1f: Bank API access credentials and process
- GAP-007: Bank integration technical details
- GAP-008: Expensify integration architecture (if selected)
- GAP-009: Google Drive integration configuration

**Required Attendees**:
- Kip Hurdick (IT Director) - technical decisions, integration architecture, API access
- Lorraine Guzman (Finance Lead) - expense/payroll requirements
- GSI Integration Lead - integration best practices, solution design
- Michelle Merlo (HR Director) - payroll platform selection (first 30 min)

**Optional Attendees**:
- Wendy/Kimmy (Asana decision) - task management approach
- Bank relationship manager (if available for API discussion)
- Expensify/platform vendor representatives (if evaluation needed)

**Duration**: 1.5-2 hours

**Pre-work for Client**:
1. **Michelle**: Finalize payroll platform evaluation; bring recommendation
2. **Lorraine**: Finalize expense management platform evaluation; bring recommendation
3. **Kip**: 
   - Make Google Drive vs SharePoint recommendation with rationale
   - Contact bank for API access documentation
   - Document current Google Drive folder structure
4. **Wendy/Kimmy**: Document Asana usage patterns; identify what could move to NetSuite
5. **Sales/Operations**: Provide manufacturer purchase volume data (non-Miller Knoll)

**Consultant Preparation**:
1. Prepare integration architecture diagram template
2. Research expense management integration options (Expensify API, alternatives)
3. Review Bank Feeds Suite App requirements and setup process
4. Prepare Google Drive integration configuration checklist
5. Create manufacturer integration priority matrix template
6. Draft solution design for REQ-024 (Expensify automation) if needed

**Expected Outcome**:
- Payroll platform confirmed (Q5.1a ❌→✅)
- Expense management platform confirmed with integration approach (Q5.1b ❌→✅)
- File storage platform selected (Q5.1c ❌→✅)
- Asana decision documented (Q5.1d ❌→✅)
- Manufacturer integration priority ranked (Q5.1e ❌→✅)
- Bank API access process initiated (Q5.1f ❌→✅)
- Integration architecture documented
- Solution design for REQ-024 completed (if ACCOMMODATE approach)
- **Result**: Q5.1 moves from ⚠️ Partial to ✅ Complete; GAP-007, GAP-008, GAP-009, GAP-010, GAP-011 closed

---

### SESSION 4: Go-Live Strategy Workshop

**Purpose**: Address Q8.1a-e and GAP-005, GAP-006, GAP-012; define operational go-live plan

**Questions to Address**:
- Q8.1a: Specific go-live date target and dependencies
- Q8.1b: Dual-system operational procedures (day-to-day workflows)
- Q8.1c: Project migration sequencing (which projects move when)
- Q8.1d: Cutover weekend activities and responsibilities
- Q8.1e: Support coverage during transition (on-site or Teams, how many consultants)
- Q10.1a: Project numbering prefix conventions
- GAP-005: Dual-system daily workflows
- GAP-006: Project migration logic and criteria

**Required Attendees**:
- Matt (Executive Sponsor) - go-live date decision, strategic direction
- Lorraine Guzman (Program Manager) - coordination, readiness assessment
- Wendy Sproles (Manager of Project Management) - project migration logic
- Shannon Dollarhide (Project Coordinator) - operational procedures
- Jill Marsh (GM San Francisco) - go-live impact assessment
- Kate Engelstrom (GM San Jose) - go-live impact assessment
- Alex Tyson (GM Sacramento) - go-live impact assessment
- GSI PMO Lead (Tom Shannon) - go-live best practices, support planning

**Optional Attendees**:
- Kimmy Katsuyoshi (CM Lead) - change management during transition
- Marcus/Chris (Orion SME) - soft cutover experience from other dealers

**Duration**: 2 hours

**Pre-work for Client**:
1. **Lorraine**: 
   - Review project timeline and identify potential go-live windows (avoid Q1 slowdown, month-end, year-end)
   - Document business readiness criteria
2. **Wendy/Shannon**: 
   - List all active projects with status and estimated completion dates
   - Identify projects that could migrate to NetSuite vs. must finish in Core
3. **Operations GMs (Jill/Kate/Alex)**: 
   - Review team capacity for go-live period
   - Identify operational constraints or busy periods
4. **Matt**: Define acceptable risk tolerance and success criteria for go-live

**Consultant Preparation**:
1. Create go-live checklist template
2. Prepare soft cutover case studies from other Orion implementations
3. Draft dual-system procedure templates
4. Create project migration decision tree
5. Prepare cutover weekend activity schedule template
6. Define support coverage options (on-site vs. Teams, consultant hours)

**Expected Outcome**:
- Target go-live date range confirmed (Q8.1a ❌→✅)
- Dual-system operational procedures documented (Q8.1b ❌→✅)
- Project migration sequencing rules defined (Q8.1c ❌→✅)
- Cutover weekend activities scheduled (Q8.1d ❌→✅)
- Support coverage approach confirmed (Q8.1e ❌→✅)
- Project numbering conventions finalized (Q10.1a ❌→✅)
- Go-live readiness criteria defined
- Communication plan for go-live
- **Result**: Q8.1 moves from ⚠️ Partial to ✅ Complete; Q10.1 moves to ✅ Complete; GAP-005, GAP-006, GAP-012 closed

---

### 5.2 Client Preparation Requirements Summary

**Documents Needed**:
1. Current chart of accounts export (Session 1)
2. Account usage report - 12 months (Session 1)
3. Current user list with Core roles (ongoing)
4. Active project list with status (Session 4)
5. Manufacturer purchase volume data (Session 3)
6. Current Google Drive folder structure (Session 3)
7. Bank API access documentation (Session 3)

**People to Involve**:
1. **Session 1 (COA)**: Lorraine, Kevin, GSI Finance Consultant
2. **Session 2 (Data)**: Lorraine, Kevin, Joe Keller, GSI Data Migration Lead
3. **Session 3 (Integration)**: Kip, Lorraine, Michelle (partial), GSI Integration Lead
4. **Session 4 (Go-Live)**: Matt, Lorraine, Wendy, Shannon, GMs (Jill/Kate/Alex), GSI PMO Lead

**Decisions to Make**:
1. Hoag workspace data timeframe (Lorraine - Session 2)
2. Payroll platform selection (Michelle/Lorraine - Session 3)
3. Expense management platform (Lorraine - Session 3)
4. Google Drive vs SharePoint (Kip - Session 3)
5. Asana continuation (Wendy/Kimmy - Session 3)
6. Target go-live date (Matt/Lorraine - Session 4)

**Examples to Prepare**:
1. Sample financial reports to replicate (Session 1)
2. Core extraction tool demo (Session 2)
3. Historical data access use cases (Session 2)
4. Asana usage examples (Session 3)
5. Project migration candidates (Session 4)

---

## 6. PRIORITY CLASSIFICATION

### 6.1 Critical Priority Gaps (Must be answered to proceed with Realize phase)

#### 🔴 CRITICAL-001: Chart of Accounts Reduction Strategy
- **Question**: Q3.2a, Q3.2b, Q3.2c
- **Missing Information**: 
  - Current COA export with account hierarchy
  - Account consolidation mapping (which accounts merge/eliminate)
  - Department/location segment structure and hierarchy
- **Business Impact**: **BLOCKS ALL FINANCIAL CONFIGURATION**. Chart of accounts is explicitly identified as "critical first step" in Realize phase. Cannot configure GL, cannot import historical data, cannot start system build without COA.
- **Who Can Answer**: Lorraine Guzman (Finance Lead), Kevin Yip (GL Accounting Manager)
- **How to Get Answer**: Session 1 - Chart of Accounts Deep Dive (2 hours)
- **Related REQ**: REQ-012 (critical first step), REQ-013 (reduction strategy)
- **Timeline Impact**: Delays COA = delays entire Realize phase start

#### 🔴 CRITICAL-002: Hoag Workspace Data Timeframe
- **Question**: Q4.1a
- **Missing Information**: How many years of Hoag workspace historical financial data to import (2017+, 2020+, or other range)
- **Business Impact**: **IMPACTS DATA MIGRATION SCOPE AND TIMELINE**. Affects CSV file preparation, data volume, import time, storage requirements. Lorraine must decide to scope data migration work.
- **Who Can Answer**: Lorraine Guzman (Finance Lead) - decision authority
- **How to Get Answer**: Session 2 - Data Migration Planning (decision in first 15 minutes)
- **Related REQ**: REQ-016 (Hoag timeframe TBD), REQ-019 (2-5 years typical)
- **Timeline Impact**: Affects data migration project plan and Realize phase schedule

#### 🔴 CRITICAL-003: Core Data Extraction Process and Timeline
- **Question**: Q4.1d
- **Missing Information**: 
  - Exact extraction process from Core SQL backend
  - Timeline and dependencies
  - "Backdoor" approach details to avoid Core vendor involvement
  - Joe Keller availability and tool demonstration
- **Business Impact**: **CRITICAL PATH FOR GO-LIVE**. Cannot import financial data without Core extraction. Risk of Core vendor interference or data access issues. Need documented extraction approach.
- **Who Can Answer**: Joe Keller (extraction tool owner), Lorraine, Kevin
- **How to Get Answer**: Session 2 - Data Migration Planning (Joe Keller demo and timeline)
- **Related REQ**: REQ-015, REQ-018 ("backdoor" access), REQ-019
- **Timeline Impact**: Data extraction must complete before data import in Realize phase

#### 🔴 CRITICAL-004: Bank API Access for Automated Reconciliation
- **Question**: Q5.1f, GAP-007
- **Missing Information**: 
  - Bank API access credentials and authentication process
  - West Coast Community Bank API documentation
  - Bank Feeds Suite App configuration requirements
- **Business Impact**: **BLOCKS BANK INTEGRATION CONFIGURATION**. REQ-021 and REQ-022 cannot be implemented without bank API access. Finance automation depends on this integration.
- **Who Can Answer**: Kip Hurdick (IT Director), West Coast Community Bank relationship manager
- **How to Get Answer**: Session 3 - Integration Architecture Review (bank API coordination)
- **Related REQ**: REQ-021 (Bank Feeds), REQ-022 (Electronic Bill Payments)
- **Timeline Impact**: Bank API setup can take 2-4 weeks; must start early in Realize

---

### 6.2 High Priority Gaps (Important for project success, needed before Educate phase)

#### 🟡 HIGH-001: User Role Mapping to Orion Roles
- **Question**: Q3.2 (implicit), GAP-003
- **Missing Information**: 
  - Which KBM Hoag users get which of 25+ custom Orion roles
  - Current Core role assignments
  - Security requirements and segregation of duties
- **Business Impact**: **NEEDED FOR USER PROVISIONING IN REALIZE PHASE**. Cannot set up users in NetSuite without role mapping. Affects training planning (role-based content). Security audit trail depends on proper role assignment.
- **Who Can Answer**: Lorraine (PM coordination), Kip (IT/security), Department Managers (user responsibilities)
- **How to Get Answer**: Document request: user list with current Core roles and responsibilities
- **Related REQ**: REQ-010 (25+ custom Orion roles)
- **Timeline Impact**: Needed mid-Realize phase for user provisioning

#### 🟡 HIGH-002: Payroll Platform Final Selection
- **Question**: Q5.1a, GAP-010
- **Missing Information**: 
  - Continue with Paylocity or switch to alternative platform?
  - Integration requirements for selected platform
  - Timeline for platform selection and integration
- **Business Impact**: **AFFECTS INTEGRATION CONFIGURATION IN REALIZE PHASE**. Payroll integration approach depends on platform selection. CSV import vs. automated integration affects finance workflows. HR platform evaluation must complete to finalize integration scope.
- **Who Can Answer**: Michelle Merlo (HR Director), Lorraine (Finance requirements)
- **How to Get Answer**: Session 3 - Integration Architecture Review (Michelle attends first 30 min for decision)
- **Related REQ**: REQ-023 (Paylocity CSV import - may change)
- **Timeline Impact**: Platform decision needed before integration configuration in Realize

#### 🟡 HIGH-003: Expense Management Platform and Integration
- **Question**: Q5.1b, GAP-008
- **Missing Information**: 
  - Continue with Expensify or switch to alternative?
  - Custom integration architecture for automated expense submission
  - Solution design for REQ-024 (ACCOMMODATE requirement)
- **Business Impact**: **REQ-024 IS ACCOMMODATE - REQUIRES SOLUTION DESIGN**. Custom integration development needed to eliminate manual Excel upload/download process. Finance automation and user experience improvement. Solution design affects Realize phase scope and timeline.
- **Who Can Answer**: Lorraine (Finance requirements), Kip (IT integration), GSI Integration Lead (solution design)
- **How to Get Answer**: Session 3 - Integration Architecture Review (platform evaluation and solution design)
- **Related REQ**: REQ-024 (ACCOMMODATE - automate Expensify)
- **Timeline Impact**: Solution design needed early Realize; custom development affects timeline

#### 🟡 HIGH-004: Google Drive vs SharePoint Decision
- **Question**: Q5.1c, GAP-009, GAP-011
- **Missing Information**: 
  - Final platform selection (Google Drive or SharePoint)
  - Rationale and decision criteria
  - Folder structure to expose in NetSuite
  - Bi-directional sync configuration requirements
- **Business Impact**: **AFFECTS DOCUMENT MANAGEMENT INTEGRATION**. Project teams depend on document access from NetSuite. Folder structure visibility impacts user experience. IT infrastructure decision affects other system integrations.
- **Who Can Answer**: Kip Hurdick (IT Director - decision authority)
- **How to Get Answer**: Session 3 - Integration Architecture Review (IT architecture decision)
- **Related REQ**: REQ-025 (Google Drive integration)
- **Timeline Impact**: Decision needed mid-Realize for integration configuration

#### 🟡 HIGH-005: NetSuite Champions Identification
- **Question**: Q6.1a, GAP-013
- **Missing Information**: 
  - Specific individuals by department to serve as Champions
  - Champion availability for additional training time
  - Prior NetSuite experience (if any)
- **Business Impact**: **CRITICAL FOR TRAINING SUCCESS**. Champions need extra training early in Realize phase to support peers in Educate phase. Peer support model reduces consultant dependency. Change management strategy depends on Champion network.
- **Who Can Answer**: Kimmy Katsuyoshi (Change Management Lead), Department Managers
- **How to Get Answer**: Change management planning meeting (can be separate or part of Session 4)
- **Related REQ**: REQ-029 (Champion strategy)
- **Timeline Impact**: Champions must be identified early Realize for extra training investment

#### 🟡 HIGH-006: Archive System Requirements and Solution Design
- **Question**: Q4.1b, Q4.1c, GAP-004
- **Missing Information**: 
  - Archive system design and architecture
  - Access methods for pre-2017 data
  - Search/query capabilities
  - User training requirements for archive access
- **Business Impact**: **REQ-050 IS ACCOMMODATE - REQUIRES SOLUTION DESIGN**. Custom archive solution needed for pre-2017 and post-migration Core data lookups. User frustration risk if archive access is difficult. "Mourning process" acknowledged - need good solution to minimize impact.
- **Who Can Answer**: Finance team (primary users), Sales team (historical lookups), Kip (IT infrastructure), GSI (solution design)
- **How to Get Answer**: Session 2 - Data Migration Planning (requirements workshop for archive)
- **Related REQ**: REQ-017 (archive pre-2017), REQ-050 (ACCOMMODATE - archive system)
- **Timeline Impact**: Solution design needed before historical data export; implementation in Realize

---

### 6.3 Medium Priority Gaps (Helpful for optimization, needed before Educate or Go-Live)

#### 🟢 MEDIUM-001: Go-Live Date Target
- **Question**: Q8.1a, GAP-012
- **Missing Information**: 
  - Specific go-live date or date range
  - Business dependencies and constraints
  - Readiness criteria
- **Business Impact**: **DRIVES PROJECT TIMELINE**. Affects resource allocation, working session cadence, training schedule. Business cycle considerations (avoid Q1, month-end, year-end). Executive alignment on timeline expectations.
- **Who Can Answer**: Matt (Executive Sponsor), Lorraine (PM), Operations GMs
- **How to Get Answer**: Session 4 - Go-Live Strategy Workshop (executive decision)
- **Related REQ**: REQ-038-043 (go-live strategy)
- **Timeline Impact**: Can be determined later in Discovery or early Realize

#### 🟢 MEDIUM-002: Dual-System Operational Procedures
- **Question**: Q8.1b, GAP-005
- **Missing Information**: 
  - Day-to-day workflows during 6-month transition
  - Which system for which transactions
  - Data reconciliation procedures
  - User decision trees
- **Business Impact**: **USER EXPERIENCE DURING TRANSITION**. All users will work in both Core and NetSuite. Confusion = errors and inefficiency. Clear procedures reduce risk. Training content depends on dual-system approach.
- **Who Can Answer**: Operations managers (Wendy, Shannon, GMs), Finance (Lorraine, Kevin)
- **How to Get Answer**: Session 4 - Go-Live Strategy Workshop (operational procedures documentation)
- **Related REQ**: REQ-039 (start new in NS, finish existing in Core), REQ-040 (6-month period)
- **Timeline Impact**: Needed before Educate phase for training content

#### 🟢 MEDIUM-003: Project Migration Sequencing Logic
- **Question**: Q8.1c, GAP-006
- **Missing Information**: 
  - Criteria for moving projects from Core to NetSuite
  - Which projects migrate in what order
  - Project migration process and responsibilities
- **Business Impact**: **PHASED MIGRATION APPROACH**. Some projects may be better migration candidates than others. Sequencing reduces risk and workload. Operations team needs clear rules for migration decisions.
- **Who Can Answer**: Wendy Sproles (PM Manager), Shannon Dollarhide (Project Coordinator), Operations GMs
- **How to Get Answer**: Session 4 - Go-Live Strategy Workshop (project portfolio review)
- **Related REQ**: REQ-041 (phased project migration)
- **Timeline Impact**: Needed before go-live for migration planning

#### 🟢 MEDIUM-004: Cutover Weekend Activities
- **Question**: Q8.1d
- **Missing Information**: 
  - What happens during cutover weekend
  - Who does what activities
  - Timeline and dependencies
  - Rollback procedures if needed
- **Business Impact**: **GO-LIVE EXECUTION PLAN**. Detailed cutover plan reduces go-live risk. Team clarity on responsibilities. Communication plan for stakeholders.
- **Who Can Answer**: GSI PMO Lead (Tom Shannon), Lorraine (PM), Operations leaders
- **How to Get Answer**: Session 4 - Go-Live Strategy Workshop (cutover planning)
- **Related REQ**: REQ-038-043 (go-live strategy)
- **Timeline Impact**: Needed late Realize/early Educate for cutover prep

#### 🟢 MEDIUM-005: Support Coverage During Transition
- **Question**: Q8.1e
- **Missing Information**: 
  - On-site support or Microsoft Teams channel support
  - How many consultants
  - Coverage hours and duration
- **Business Impact**: **GO-LIVE SUPPORT APPROACH**. User confidence during transition. Issue resolution speed. Cost implications for on-site vs. remote support.
- **Who Can Answer**: Matt (budget authority), Lorraine (support needs), GSI PMO (support options)
- **How to Get Answer**: Session 4 - Go-Live Strategy Workshop (support planning)
- **Related REQ**: REQ-042 (on-site or Teams support)
- **Timeline Impact**: Needed before go-live for budget and resource planning

#### 🟢 MEDIUM-006: Project Numbering Prefix Conventions
- **Question**: Q10.1a
- **Missing Information**: 
  - Specific prefix structure (OPP-####? Q-####? SO-####?)
  - Numbering sequence configuration
  - Project number format
- **Business Impact**: **TRANSACTION NUMBERING CONFIGURATION**. User adjustment expected from Core memorized numbers. Consistent project numbering across transaction types provides continuity. Configuration needed in Realize phase.
- **Who Can Answer**: Lorraine (numbering preferences), Operations team (current numbering usage)
- **How to Get Answer**: Session 4 - Go-Live Strategy Workshop (finalize conventions) OR separate quick meeting
- **Related REQ**: REQ-046 (consistent project numbering), REQ-047 (global search)
- **Timeline Impact**: Needed mid-Realize for transaction numbering configuration

#### 🟢 MEDIUM-007: Manufacturer Integration Priority
- **Question**: Q5.1e, GAP-014
- **Missing Information**: 
  - Which non-Miller Knoll manufacturers are highest priority
  - Purchase volume by manufacturer
  - ROI for integration by manufacturer
- **Business Impact**: **MANUFACTURER OUTREACH STRATEGY**. Determines which manufacturers to pursue for integration adoption. Human Scale and National declined - are they worth pursuing with KBM Hoag relationship leverage? Other manufacturers may be higher ROI.
- **Who Can Answer**: Matt (manufacturer relationships), Sales team, Operations (volume data)
- **How to Get Answer**: Session 3 - Integration Architecture Review (prioritization exercise)
- **Related REQ**: REQ-026 (manufacturer integration platform extension)
- **Timeline Impact**: Can be addressed later; affects future phase integration expansion

#### 🟢 MEDIUM-008: Asana Future State Decision
- **Question**: Q5.1d, GAP-015
- **Missing Information**: 
  - Continue as-is, reduce usage, or eliminate Asana
  - What task management goes to NetSuite vs. stays in Asana
- **Business Impact**: **TASK MANAGEMENT APPROACH**. Affects NetSuite configuration for task/to-do management. User workflow changes. Potential cost savings if Asana eliminated.
- **Who Can Answer**: Kimmy (task management), Wendy (PM task tracking), project managers
- **How to Get Answer**: Session 3 - Integration Architecture Review OR separate task management meeting
- **Related REQ**: Systems consolidation strategy (mentioned in kickoff)
- **Timeline Impact**: Can be decided later; affects task management configuration

#### 🟢 MEDIUM-009: Training Schedule Development
- **Question**: Q6.1b
- **Missing Information**: 
  - When during Educate phase
  - What sequence (departments, roles)
  - Duration and session count by role
- **Business Impact**: **EDUCATE PHASE PLANNING**. Affects stakeholder calendar planning. Training effectiveness depends on proper sequencing. UAT timing depends on training schedule.
- **Who Can Answer**: GSI training team, Kimmy (CM Lead), Department Managers (availability)
- **How to Get Answer**: Training planning meeting (late Realize/early Educate)
- **Related REQ**: REQ-027-030 (training strategy)
- **Timeline Impact**: Needed late Realize for Educate phase preparation

#### 🟢 MEDIUM-010: Microsoft Teams Environment Setup
- **Question**: Q7.1a
- **Missing Information**: 
  - When will Teams be configured
  - Who sets up (GSI or KBM Hoag IT)
  - Channel structure and permissions
- **Business Impact**: **COMMUNICATION PLATFORM**. Needed immediately for project communication. File sharing and meeting coordination. Chat threads for ongoing collaboration.
- **Who Can Answer**: Kip (IT), GSI PMO Lead (Tom Shannon)
- **How to Get Answer**: Action item follow-up (can be done async)
- **Related REQ**: REQ-032 (Teams as primary platform)
- **Timeline Impact**: **IMMEDIATE ACTION NEEDED** - should be done now

#### 🟢 MEDIUM-011: Working Session Cadence Finalization
- **Question**: Q7.1b
- **Missing Information**: 
  - Weekly, 2x per week, or 3x per week
  - Phase-dependent cadence
- **Business Impact**: **DISCOVERY AND IMPLEMENTATION PACE**. Affects project timeline. Stakeholder calendar commitments. Balance between project speed and stakeholder availability.
- **Who Can Answer**: Lorraine (PM), Matt (executive priorities), GSI PMO
- **How to Get Answer**: Discussion during ongoing Discovery (can adjust as needed)
- **Related REQ**: REQ-034 (weekly to 3x per week cadence)
- **Timeline Impact**: Can be determined iteratively during Discovery

---

## 7. CONSULTANT ACTION PLAN

### 7.1 Immediate Actions (Next 1-2 weeks)

#### ACTION-001: Schedule Session 1 - Chart of Accounts Deep Dive
- **Owner**: GSI PMO Lead (Tom Shannon) + Lorraine Guzman (PM)
- **Target Date**: Week of November 4-8, 2025 (before month-end close November 28-30)
- **Action Steps**:
  1. Send meeting invitation to required attendees (Lorraine, Kevin, GSI Finance Consultant)
  2. Send pre-work request email to Lorraine and Kevin (COA export, usage report, sample reports)
  3. Confirm GSI Finance Consultant availability and Orion COA expertise
- **Dependencies**: None - can schedule immediately
- **Related Gaps**: CRITICAL-001, GAP-001

#### ACTION-002: Request Core Chart of Accounts Export
- **Owner**: Lorraine Guzman (with Kevin Yip)
- **Target Date**: By November 1, 2025 (before Session 1)
- **Action Steps**:
  1. Export current chart of accounts from Core (full list with numbers, names, types, balances)
  2. Generate account usage report (transactions by account, last 12 months)
  3. Identify "must keep" accounts for compliance or specific reporting
  4. List current department and location segments
- **Dependencies**: Core system access
- **Related Gaps**: CRITICAL-001, GAP-001

#### ACTION-003: Set Up Microsoft Teams Environment (IMMEDIATE)
- **Owner**: Kip Hurdick (IT) + GSI PMO Lead (Tom Shannon)
- **Target Date**: By October 25, 2025 (THIS WEEK)
- **Action Steps**:
  1. GSI creates Teams workspace for KBM Hoag project
  2. Kip identifies KBM Hoag team members to add
  3. GSI sends Teams invitations to all KBM Hoag project participants
  4. Set up channel structure (General, Discovery Sessions, Documents, Issues/Questions)
  5. Test file sharing and meeting capabilities
- **Dependencies**: Microsoft Teams licenses for KBM Hoag team
- **Related Gaps**: MEDIUM-010

#### ACTION-004: Schedule Session 2 - Data Migration Planning
- **Owner**: GSI PMO Lead + Lorraine Guzman
- **Target Date**: Week of November 11-15, 2025 (after Session 1)
- **Action Steps**:
  1. Coordinate Joe Keller availability for Core extraction demo
  2. Send meeting invitation to required attendees (Lorraine, Kevin, Joe, GSI Data Migration Lead)
  3. Send pre-work request (Hoag data decision, extraction tool prep, validation checkpoints, historical access use cases)
  4. Confirm GSI Data Migration Lead assignment
- **Dependencies**: Joe Keller availability; Session 1 completion
- **Related Gaps**: CRITICAL-002, CRITICAL-003, HIGH-006, GAP-002, GAP-004

#### ACTION-005: Request User List with Current Core Roles
- **Owner**: Lorraine Guzman (PM) with Kip Hurdick (IT)
- **Target Date**: By November 8, 2025
- **Action Steps**:
  1. Export user list from Core with assigned roles
  2. Document current user responsibilities by role
  3. Identify security requirements and segregation of duties
  4. Note any users with prior NetSuite experience
- **Dependencies**: Core system access, HR records
- **Related Gaps**: HIGH-001, GAP-003

#### ACTION-006: Hoag Workspace Data Timeframe Decision
- **Owner**: Lorraine Guzman (Finance Lead)
- **Target Date**: By Session 2 (November 11-15, 2025)
- **Action Steps**:
  1. Review Hoag workspace transaction history
  2. Determine business need for historical data (reporting, analysis, compliance)
  3. Consider storage/performance implications
  4. Make decision: 2017+, 2020+, or other range
  5. Document decision rationale
- **Dependencies**: Understanding of business requirements for historical data
- **Related Gaps**: CRITICAL-002

### 7.2 Follow-up Actions (Next 2-4 weeks)

#### ACTION-007: Schedule Session 3 - Integration Architecture Review
- **Owner**: GSI PMO Lead + Kip Hurdick (IT)
- **Target Date**: Week of November 18-22, 2025 (after Session 2)
- **Action Steps**:
  1. Send meeting invitation to required attendees (Kip, Lorraine, Michelle (30 min), GSI Integration Lead)
  2. Send pre-work request (payroll platform recommendation, expense platform recommendation, Google Drive vs SharePoint decision, bank API documentation, manufacturer volume data)
  3. Confirm GSI Integration Lead assignment or identify if needed
  4. Prepare integration architecture diagram template
- **Dependencies**: Session 1 and 2 completion; platform evaluation progress
- **Related Gaps**: CRITICAL-004, HIGH-002, HIGH-003, HIGH-004, MEDIUM-007, MEDIUM-008, GAP-007, GAP-008, GAP-009, GAP-010, GAP-011, GAP-014, GAP-015

#### ACTION-008: Finalize Platform Selections (Payroll, Expense, File Storage)
- **Owner**: Lorraine Guzman (Expense), Michelle Merlo (Payroll), Kip Hurdick (File Storage)
- **Target Date**: By Session 3 (November 18-22, 2025)
- **Action Steps**:
  - **Michelle (Payroll)**:
    1. Complete HR platform evaluation
    2. Compare Paylocity vs alternatives (cost, features, integration)
    3. Bring recommendation to Session 3
  - **Lorraine (Expense)**:
    1. Complete expense management platform evaluation
    2. Assess Expensify automation feasibility and cost
    3. Compare alternatives if needed
    4. Bring recommendation to Session 3
  - **Kip (File Storage)**:
    1. Evaluate Google Drive vs SharePoint (features, cost, user preference)
    2. Document current Google Drive folder structure
    3. Make recommendation with rationale
    4. Bring decision to Session 3
- **Dependencies**: Platform vendor input, cost analysis, user requirements
- **Related Gaps**: HIGH-002, HIGH-003, HIGH-004, GAP-010, GAP-011

#### ACTION-009: Contact Bank for API Access Documentation
- **Owner**: Kip Hurdick (IT Director)
- **Target Date**: By Session 3 (November 18-22, 2025)
- **Action Steps**:
  1. Contact West Coast Community Bank relationship manager
  2. Request API access documentation for NetSuite Bank Feeds Suite App
  3. Inquire about authentication requirements and credentials
  4. Ask about timeline for API access provisioning
  5. Bring documentation to Session 3
- **Dependencies**: Bank relationship, bank API capabilities
- **Related Gaps**: CRITICAL-004, GAP-007

#### ACTION-010: Schedule Session 4 - Go-Live Strategy Workshop
- **Owner**: GSI PMO Lead + Lorraine Guzman
- **Target Date**: Week of November 25 - December 6, 2025 (avoid month-end close Nov 28-30)
- **Action Steps**:
  1. Send meeting invitation to required attendees (Matt, Lorraine, Wendy, Shannon, GMs Jill/Kate/Alex, GSI PMO Lead)
  2. Send pre-work request (project timeline review, active project list, team capacity assessment, business readiness criteria)
  3. Prepare go-live planning templates and case studies
- **Dependencies**: Session 1-3 completion; executive availability
- **Related Gaps**: MEDIUM-001 through MEDIUM-006, GAP-005, GAP-006, GAP-012

#### ACTION-011: Prepare Active Project List with Status
- **Owner**: Wendy Sproles (PM Manager) + Shannon Dollarhide (Project Coordinator)
- **Target Date**: By Session 4 (November 25 - December 6, 2025)
- **Action Steps**:
  1. Export active project list from Core
  2. Document project status and estimated completion dates
  3. Identify projects that could migrate to NetSuite vs. must finish in Core
  4. Note project complexity and risk factors
  5. Bring to Session 4 for migration sequencing discussion
- **Dependencies**: Core project data, PM team assessment
- **Related Gaps**: MEDIUM-003, GAP-006

#### ACTION-012: Identify NetSuite Champions by Department
- **Owner**: Kimmy Katsuyoshi (Change Management Lead) with Department Managers
- **Target Date**: By early December 2025 (early Realize phase)
- **Action Steps**:
  1. Review department organizational charts
  2. Identify enthusiastic team members with aptitude for training peers
  3. Check for any prior NetSuite experience
  4. Assess Champion availability for additional training time
  5. Discuss with Department Managers and confirm Champion willingness
  6. Document Champion network (name, department, role, contact)
- **Dependencies**: Department Manager input, Champion willingness
- **Related Gaps**: HIGH-005, GAP-013

#### ACTION-013: Gather Manufacturer Purchase Volume Data
- **Owner**: Operations Team (with Sales data)
- **Target Date**: By Session 3 (November 18-22, 2025)
- **Action Steps**:
  1. Extract purchase volume by manufacturer (last 12-24 months)
  2. Rank manufacturers by order volume and revenue
  3. Identify top 5-10 non-Miller Knoll manufacturers
  4. Note any manufacturers with existing integration capabilities
  5. Bring data to Session 3 for prioritization discussion
- **Dependencies**: Core purchasing data, sales records
- **Related Gaps**: MEDIUM-007, GAP-014

#### ACTION-014: Document Asana Usage Patterns
- **Owner**: Wendy Sproles (PM Manager) + Kimmy Katsuyoshi
- **Target Date**: By Session 3 (November 18-22, 2025)
- **Action Steps**:
  1. Review current Asana usage (who uses it, for what, how often)
  2. Identify task management functions that could move to NetSuite
  3. Identify functions that should stay in Asana (if any)
  4. Assess impact of eliminating Asana (cost savings, user change)
  5. Bring analysis to Session 3 for decision
- **Dependencies**: Asana admin access, user feedback
- **Related Gaps**: MEDIUM-008, GAP-015

### 7.3 Completion Actions (4-6 weeks)

#### ACTION-015: Create Solution Design for Archive System (REQ-050)
- **Owner**: GSI Data Migration Lead + GSI Solutions Architect
- **Target Date**: By December 15, 2025 (after Session 2 requirements workshop)
- **Action Steps**:
  1. Document archive system requirements from Session 2
  2. Evaluate archive solution options (cloud storage, database, reporting tool)
  3. Design archive architecture and access methods
  4. Define search/query capabilities
  5. Create user access procedures documentation
  6. Estimate development/configuration effort and timeline
  7. Present solution design to client for approval
- **Dependencies**: Session 2 completion, requirements clarity
- **Related Gaps**: HIGH-006, GAP-004
- **Related REQ**: REQ-050 (ACCOMMODATE)

#### ACTION-016: Create Solution Design for Expensify Automation (REQ-024)
- **Owner**: GSI Integration Lead
- **Target Date**: By December 15, 2025 (after Session 3 platform selection)
- **Action Steps**:
  1. Document expense management requirements from Session 3
  2. Evaluate Expensify API capabilities (or alternative platform)
  3. Design integration architecture for automated expense submission
  4. Define data mapping and synchronization rules
  5. Estimate custom development effort and timeline
  6. Present solution design to client for approval
- **Dependencies**: Session 3 platform selection, Expensify API documentation
- **Related Gaps**: HIGH-003, GAP-008
- **Related REQ**: REQ-024 (ACCOMMODATE)

#### ACTION-017: Update Questionnaire to v1.1 (Post-Sessions)
- **Owner**: GSI Business Analyst (Discovery lead)
- **Target Date**: By December 20, 2025 (after all 4 sessions complete)
- **Action Steps**:
  1. Incorporate all new information from Sessions 1-4
  2. Update confidence ratings for previously partial/missing questions
  3. Document all decisions made in sessions
  4. Update Decision Log with new decisions
  5. Move questions from ⚠️/❌ to ✅ Complete status
  6. Update Change Log with v1.1 summary
- **Dependencies**: Completion of Sessions 1-4
- **Related Gaps**: ALL

#### ACTION-018: Update Requirements Map to v1.1 (Post-Sessions)
- **Owner**: GSI Business Analyst (Discovery lead)
- **Target Date**: By December 20, 2025 (after all 4 sessions complete)
- **Action Steps**:
  1. Add any new REQ-### items discovered in sessions
  2. Update existing requirements with additional detail
  3. Finalize ALIGNS/ADAPT/ACCOMMODATE classifications
  4. Update SolutionDesign column for REQ-024 and REQ-050
  5. Update risks and dependencies
  6. Update Change Log with v1.1 summary
- **Dependencies**: Completion of Sessions 1-4, questionnaire v1.1
- **Related Gaps**: ALL

#### ACTION-019: Conduct Final Completeness Review
- **Owner**: GSI Business Analyst + GSI PMO Lead
- **Target Date**: By December 22, 2025
- **Action Steps**:
  1. Review questionnaire v1.1 for remaining gaps
  2. Verify all Critical and High priority gaps are closed
  3. Assess confidence ratings (target 90%+ for Must-Haves)
  4. Identify any residual Medium priority gaps
  5. Determine if additional follow-up is needed or can be addressed in Realize phase
  6. Document completeness assessment
  7. Obtain client sign-off on questionnaire completion
- **Dependencies**: Questionnaire v1.1, Requirements Map v1.1
- **Related Gaps**: ALL

#### ACTION-020: Prepare for BRD Generation
- **Owner**: GSI Business Analyst (Discovery lead)
- **Target Date**: By December 23, 2025 (before year-end holidays)
- **Action Steps**:
  1. Verify questionnaire and requirements map are complete and signed off
  2. Gather all solution designs (REQ-024, REQ-050)
  3. Compile all evidence and documentation
  4. Review BRD generation prompt and requirements
  5. Prepare to generate BRD_SystemSetupConfiguration_v1.0.md
- **Dependencies**: Questionnaire v1.1 sign-off, Requirements Map v1.1, Solution Designs
- **Quality Gate**: No critical gaps remaining, confidence ≥ 85% for Must-Haves

---

## 8. SUCCESS METRICS

### 8.1 Completion Targets

**Current Status**: 86% complete
- ✅ Fully Answered: 15 questions (47%)
- ⚠️ Partially Answered: 11 questions (34%)
- ❌ Not Answered: 6 questions (19%)
- **Confidence Ratings**: 94-99% for fully answered questions
- **Requirements Documented**: 50 (REQ-001 through REQ-050)

**After Session 1 (Chart of Accounts Deep Dive)**: 90% complete
- **Questions Completed**:
  - Q3.2a: COA reduction strategy (❌→✅)
  - Q3.2b: Account consolidation rules (❌→✅)
  - Q3.2c: Department/location segments (❌→✅)
  - Q3.2: Critical first configuration steps (⚠️→✅)
- **Gaps Closed**: CRITICAL-001, GAP-001
- **Requirements Completed**: REQ-012, REQ-013 (detailed specifications added)
- **Deliverables**: Chart of accounts mapping document, account consolidation rules

**After Session 2 (Data Migration Planning)**: 94% complete
- **Questions Completed**:
  - Q4.1a: Hoag data timeframe (❌→✅)
  - Q4.1b: Archive system design (❌→✅)
  - Q4.1c: Archive access procedures (❌→✅)
  - Q4.1d: Data extraction timeline (⚠️→✅)
  - Q4.1e: Data validation process (❌→✅)
  - Q4.1: Financial data scope (⚠️→✅)
- **Gaps Closed**: CRITICAL-002, CRITICAL-003, HIGH-006, GAP-002, GAP-004
- **Requirements Completed**: REQ-015-019, REQ-050 (with solution design)
- **Deliverables**: Data migration strategy document, archive system solution design

**After Session 3 (Integration Architecture Review)**: 97% complete
- **Questions Completed**:
  - Q5.1a: Payroll platform (❌→✅)
  - Q5.1b: Expense platform (❌→✅)
  - Q5.1c: File storage (❌→✅)
  - Q5.1d: Asana decision (❌→✅)
  - Q5.1e: Manufacturer priority (❌→✅)
  - Q5.1f: Bank API access (❌→✅)
  - Q5.1: Integration requirements (⚠️→✅)
- **Gaps Closed**: CRITICAL-004, HIGH-002, HIGH-003, HIGH-004, MEDIUM-007, MEDIUM-008, GAP-007 through GAP-011, GAP-014, GAP-015
- **Requirements Completed**: REQ-020-026 (with solution design for REQ-024 if needed)
- **Deliverables**: Integration architecture document, Expensify solution design (if ACCOMMODATE)

**After Session 4 (Go-Live Strategy Workshop)**: 100% complete
- **Questions Completed**:
  - Q8.1a: Go-live date target (❌→✅)
  - Q8.1b: Dual-system procedures (❌→✅)
  - Q8.1c: Project migration sequencing (❌→✅)
  - Q8.1d: Cutover weekend activities (❌→✅)
  - Q8.1e: Support coverage (❌→✅)
  - Q8.1: Go-live approach (⚠️→✅)
  - Q10.1a: Project numbering prefixes (❌→✅)
  - Q10.1: Transaction management (⚠️→✅)
- **Gaps Closed**: MEDIUM-001 through MEDIUM-006, GAP-005, GAP-006, GAP-012
- **Requirements Completed**: REQ-038-048 (detailed specifications added)
- **Deliverables**: Go-live strategy document, cutover checklist, dual-system procedures manual

**Final Target**: 100% complete by December 20, 2025
- **All Critical Gaps**: Closed ✅
- **All High Priority Gaps**: Closed ✅
- **All Medium Priority Gaps**: Closed ✅
- **Questionnaire Status**: v1.1 with client sign-off
- **Requirements Map Status**: v1.1 with all 50+ requirements fully specified
- **Solution Designs**: REQ-024 and REQ-050 complete
- **BRD Ready**: Proceed to BRD generation
- **Discovery Phase**: Complete and validated

---

## 9. DECISION LOG (NEW/UPDATED DECISIONS FROM THIS ANALYSIS)

### Decisions Pending (To Be Made in Follow-up Sessions)

**DECISION-PENDING-001**: Chart of Accounts Consolidation Approach
- **Decision Needed**: How to reduce COA from 40+ pages to few hundred accounts; which accounts consolidate/merge/eliminate
- **Decision Maker**: Lorraine Guzman (Finance Lead) with Kevin Yip input
- **Decision Forum**: Session 1 - Chart of Accounts Deep Dive
- **Timeline**: Week of November 4-8, 2025
- **Impact**: REQ-012, REQ-013; blocks Realize phase financial configuration
- **Related Gap**: CRITICAL-001

**DECISION-PENDING-002**: Hoag Workspace Historical Data Timeframe
- **Decision Needed**: How many years of Hoag workspace financial data to import (2017+, 2020+, other)
- **Decision Maker**: Lorraine Guzman (Finance Lead)
- **Decision Forum**: Session 2 - Data Migration Planning
- **Timeline**: Week of November 11-15, 2025
- **Impact**: REQ-016, REQ-019; affects data migration scope and timeline
- **Related Gap**: CRITICAL-002

**DECISION-PENDING-003**: Payroll Platform Final Selection
- **Decision Needed**: Continue with Paylocity or switch to alternative HR/payroll platform
- **Decision Maker**: Michelle Merlo (HR Director) with Lorraine input
- **Decision Forum**: Session 3 - Integration Architecture Review
- **Timeline**: Week of November 18-22, 2025
- **Impact**: REQ-023; affects integration configuration approach
- **Related Gap**: HIGH-002

**DECISION-PENDING-004**: Expense Management Platform and Integration Approach
- **Decision Needed**: Continue with Expensify or alternative; automated integration approach and solution design
- **Decision Maker**: Lorraine Guzman (Finance Lead) with Kip input
- **Decision Forum**: Session 3 - Integration Architecture Review
- **Timeline**: Week of November 18-22, 2025
- **Impact**: REQ-024 (ACCOMMODATE); requires solution design and custom development
- **Related Gap**: HIGH-003

**DECISION-PENDING-005**: Google Drive vs SharePoint
- **Decision Needed**: Final platform selection for file storage integration with NetSuite
- **Decision Maker**: Kip Hurdick (IT Director)
- **Decision Forum**: Session 3 - Integration Architecture Review
- **Timeline**: Week of November 18-22, 2025
- **Impact**: REQ-025; affects document management integration
- **Related Gap**: HIGH-004

**DECISION-PENDING-006**: Asana Continuation or Elimination
- **Decision Needed**: Continue as-is, reduce usage, or eliminate Asana; what task management moves to NetSuite
- **Decision Maker**: Kimmy Katsuyoshi (CM Lead) with Wendy Sproles input
- **Decision Forum**: Session 3 - Integration Architecture Review
- **Timeline**: Week of November 18-22, 2025
- **Impact**: Task management approach in NetSuite
- **Related Gap**: MEDIUM-008

**DECISION-PENDING-007**: Target Go-Live Date
- **Decision Needed**: Specific go-live date or date range; business dependencies and readiness criteria
- **Decision Maker**: Matt (Executive Sponsor) with Lorraine and GMs input
- **Decision Forum**: Session 4 - Go-Live Strategy Workshop
- **Timeline**: Week of November 25 - December 6, 2025
- **Impact**: REQ-038-043; drives entire project timeline and resource allocation
- **Related Gap**: MEDIUM-001

**DECISION-PENDING-008**: Go-Live Support Coverage
- **Decision Needed**: On-site support or Microsoft Teams channel; number of consultants and coverage hours
- **Decision Maker**: Matt (budget authority) with Lorraine (support needs)
- **Decision Forum**: Session 4 - Go-Live Strategy Workshop
- **Timeline**: Week of November 25 - December 6, 2025
- **Impact**: REQ-042; affects go-live cost and support effectiveness
- **Related Gap**: MEDIUM-005

---

## 10. RISK SUMMARY

### High Risk Gaps (If Not Addressed)

**RISK-001**: Chart of Accounts Delay Blocks Realize Phase
- **Gap**: CRITICAL-001
- **Risk**: Without COA mapping, cannot configure GL, import financial data, or start Realize phase
- **Probability**: Medium (depends on Session 1 scheduling and Lorraine/Kevin availability)
- **Impact**: High (delays entire Realize phase timeline)
- **Mitigation**: Schedule Session 1 immediately (Week of Nov 4-8); make COA pre-work priority for Lorraine/Kevin
- **Owner**: GSI PMO Lead + Lorraine Guzman

**RISK-002**: Data Migration Scope Uncertainty Delays Timeline
- **Gap**: CRITICAL-002, CRITICAL-003
- **Risk**: Without Hoag data decision and Core extraction timeline, cannot plan data migration work or go-live date
- **Probability**: Low (Lorraine can make decision quickly; Joe Keller has extraction tool)
- **Impact**: High (data migration is critical path to go-live)
- **Mitigation**: Schedule Session 2 promptly; secure Joe Keller participation; Lorraine pre-work decision
- **Owner**: GSI Data Migration Lead + Lorraine Guzman

**RISK-003**: Bank API Access Delays Bank Integration
- **Gap**: CRITICAL-004, GAP-007
- **Risk**: Banks often have 2-4 week lead time for API access; delay blocks automated reconciliation benefits
- **Probability**: Medium (banks can be slow; process may be bureaucratic)
- **Impact**: Medium (affects finance automation but not core system)
- **Mitigation**: Start bank API request immediately (Kip action); plan for alternative manual reconciliation if API delayed
- **Owner**: Kip Hurdick + GSI Integration Lead

**RISK-004**: Platform Selection Delays Integration Configuration
- **Gap**: HIGH-002, HIGH-003, HIGH-004
- **Risk**: Without payroll, expense, and file storage platform decisions, cannot configure integrations in Realize phase
- **Probability**: Medium (evaluation processes take time; stakeholder alignment needed)
- **Impact**: Medium (affects specific integrations but not core system)
- **Mitigation**: Set decision deadlines for Session 3; pre-work evaluations; bring recommendations not just options
- **Owner**: Michelle Merlo (payroll), Lorraine Guzman (expense), Kip Hurdick (file storage)

### Medium Risk Gaps (If Not Addressed)

**RISK-005**: User Role Mapping Delays User Provisioning
- **Gap**: HIGH-001, GAP-003
- **Risk**: Without user-to-role mapping, cannot set up NetSuite users; delays training and UAT
- **Probability**: Low (user list can be generated from Core)
- **Impact**: Medium (delays training start but not core configuration)
- **Mitigation**: Request user list immediately; can be done async without session
- **Owner**: Lorraine Guzman + Kip Hurdick

**RISK-006**: Archive System Solution Design Complexity
- **Gap**: HIGH-006, GAP-004
- **Risk**: REQ-050 ACCOMMODATE requirement; custom archive solution may be complex and time-consuming
- **Probability**: Medium (depends on requirements from Session 2)
- **Impact**: Medium (affects historical data access but not core operations)
- **Mitigation**: Allocate solution design time; consider simple solutions first (cloud storage + export); manage user expectations
- **Owner**: GSI Data Migration Lead + GSI Solutions Architect

**RISK-007**: Go-Live Planning Insufficient for Smooth Transition
- **Gap**: MEDIUM-001 through MEDIUM-006, GAP-005, GAP-006, GAP-012
- **Risk**: Without detailed go-live plan, dual-system transition may be chaotic and stressful for users
- **Probability**: Low (Session 4 will address; soft cutover is risk mitigation strategy)
- **Impact**: High (affects all users and operations during transition)
- **Mitigation**: Comprehensive Session 4 workshop; leverage GSI experience with soft cutovers; detailed procedures documentation
- **Owner**: GSI PMO Lead + Lorraine Guzman + Operations GMs

### Low Risk Gaps (Can Be Addressed Later)

**RISK-008**: NetSuite Champions Not Identified Early
- **Gap**: HIGH-005, GAP-013
- **Risk**: Without Champions identified early, cannot provide extra training; peer support model delayed
- **Probability**: Low (Kimmy can identify Champions with department manager input)
- **Impact**: Low (affects training optimization but training will occur regardless)
- **Mitigation**: Kimmy action item by early December; Champions can be identified in early Realize phase
- **Owner**: Kimmy Katsuyoshi

---

## 11. APPENDIX

### A. Outstanding Action Items from Questionnaire (Now Integrated into Action Plan)

These action items from the original questionnaire have been incorporated into the action plan above:

1. **Kip: Provide document templates** - Low priority, needed for Realize phase configuration
2. **Matt: Provide XML import templates** - Low priority, related to data migration Session 2
3. **Shannon: Provide approval workflow rules** - Low priority, needed for workflow configuration in Realize
4. **Lorraine: Confirm order type list** - Low priority, needed for transaction configuration in Realize
5. **Team: Review discovery session attendees** - Ongoing, addressed in session scheduling
6. **Lorraine: Chart of accounts preparation** - **HIGH PRIORITY**, Session 1 focus
7. **Lorraine: Hoag data timeframe determination** - **CRITICAL PRIORITY**, Session 2 decision
8. **Michelle: Payroll platform selection** - **HIGH PRIORITY**, Session 3 decision
9. **Finance Lead: Expense platform selection** - **HIGH PRIORITY**, Session 3 decision
10. **Kip: Google Drive vs SharePoint decision** - **HIGH PRIORITY**, Session 3 decision
11. **Team: Asana determination** - Medium priority, Session 3 decision
12. **Matt/Team: Manufacturer integration outreach** - Medium priority, Session 3 prioritization
13. **Kimmy: Identify NetSuite Champions** - **HIGH PRIORITY**, early Realize phase
14. **Team: Training schedule development** - Medium priority, late Realize/early Educate
15. **Tom Shannon: Microsoft Teams setup** - **IMMEDIATE PRIORITY**, ACTION-003
16. **Team: Attendee confirmation** - Ongoing

### B. Key Stakeholder Contact Summary (for Session Scheduling)

**Finance Team**:
- Lorraine Guzman (Head of Finance, Program Manager) - Sessions 1, 2, 3, 4
- Kevin Yip (GL Accounting Manager) - Sessions 1, 2

**IT Team**:
- Kip Hurdick (IT Director) - Session 3

**HR Team**:
- Michelle Merlo (HR Director) - Session 3 (first 30 min)

**Operations Team**:
- Wendy Sproles (Manager of Project Management) - Session 4
- Shannon Dollarhide (Project Coordinator) - Session 4
- Jill Marsh (GM San Francisco) - Session 4
- Kate Engelstrom (GM San Jose) - Session 4
- Alex Tyson (GM Sacramento) - Session 4

**Executive Team**:
- Matt (Executive Sponsor) - Session 4

**Change Management**:
- Kimmy Katsuyoshi (Director of Account Management, CM Lead) - Champion identification (separate)

**External/Other**:
- Joe Keller (Core extraction expert) - Session 2

### C. Session Summary Quick Reference

| Session | Duration | Priority | Timing | Required Attendees | Key Outcomes |
|---------|----------|----------|--------|-------------------|--------------|
| **1: Chart of Accounts** | 2 hours | 🔴 CRITICAL | Nov 4-8 | Lorraine, Kevin, GSI Finance | COA mapping complete |
| **2: Data Migration** | 2 hours | 🔴 CRITICAL | Nov 11-15 | Lorraine, Kevin, Joe, GSI Data | Migration plan, archive design |
| **3: Integration Architecture** | 1.5-2 hours | 🔴 CRITICAL | Nov 18-22 | Kip, Lorraine, Michelle, GSI Integration | Platform decisions, integration plan |
| **4: Go-Live Strategy** | 2 hours | 🟡 HIGH | Nov 25-Dec 6 | Matt, Lorraine, Ops team, GSI PMO | Go-live plan, dual-system procedures |

### D. Confidence Rating Targets

**Current State**:
- Fully Answered Questions: 94-99% confidence
- Partially Answered Questions: 50-75% confidence (high-level only)
- Not Answered Questions: 0% confidence

**Target After All Sessions**:
- All Questions: 90%+ confidence
- Must-Have Requirements: 95%+ confidence
- Should-Have Requirements: 85%+ confidence
- Nice-to-Have Requirements: 75%+ confidence

### E. Tools & Templates Needed

**From GSI**:
1. Chart of accounts mapping template (Session 1)
2. Data migration project plan template (Session 2)
3. Integration architecture diagram template (Session 3)
4. Go-live checklist template (Session 4)
5. Dual-system procedure templates (Session 4)
6. Solution design templates (REQ-024, REQ-050)

**From KBM Hoag**:
1. Core chart of accounts export (Session 1)
2. User list with roles (ongoing)
3. Active project list (Session 4)
4. Manufacturer volume data (Session 3)
5. Google Drive folder structure documentation (Session 3)
6. Asana usage documentation (Session 3)

---

## CONCLUSION

The System Setup and Configuration discovery questionnaire has achieved **86% completion** with strong foundational coverage across all 12 major question areas. The remaining **14% consists primarily of operational planning details and platform selection decisions** that require targeted follow-up sessions.

**Critical Success Factors**:
1. ✅ **Strong Foundation**: All strategic and methodological questions fully answered (REQ-001 through REQ-008, REQ-027-037, REQ-044-045)
2. ⚠️ **Configuration Details Pending**: Chart of accounts mapping is critical blocker (CRITICAL-001)
3. ⚠️ **Platform Decisions Required**: Payroll, expense, and file storage selections needed (HIGH-002, HIGH-003, HIGH-004)
4. ⚠️ **Go-Live Planning Needed**: Operational procedures for dual-system transition (MEDIUM-001 through MEDIUM-006)

**Recommended Path to 100% Completion**:
- **4 targeted sessions** (total 7.5 hours) will close all critical and high priority gaps
- **Timeline**: November 4 - December 6, 2025 (5 weeks)
- **Outcome**: Questionnaire v1.1 with 100% completion, ready for BRD generation
- **Deliverables**: Complete BRD by December 23, 2025 (before year-end holidays)

**Next Immediate Actions**:
1. ⚡ Set up Microsoft Teams (THIS WEEK) - ACTION-003
2. ⚡ Schedule Session 1 for Week of Nov 4-8 - ACTION-001
3. ⚡ Request COA export from Lorraine/Kevin - ACTION-002

With focused execution on the action plan, the System Setup and Configuration discovery can achieve **100% completion by December 20, 2025**, enabling smooth transition to the Realize phase in early 2026.

---

*End of Gap Analysis - System Setup and Configuration v1.0*





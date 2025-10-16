# Questionnaire - System Setup and Configuration
**Version**: 1.0  
**Date**: October 16, 2025  
**Process Area**: System Setup and Configuration

## Change Log
- **Date**: October 16, 2025
- **Version**: 1.0  
- **Sources**: Master_Transcript_Project_Kickoff.md, Discovery Workflow Specification.md
- **Summary**: Initial questionnaire analysis completed from Project Kickoff session covering implementation methodology, project governance, system configuration, data migration, training, and go-live strategy.

## PROCESSED FILES
- System Setup and Configuration/2 Input/Master_Transcript_Project_Kickoff.md (807 lines)
- System Setup and Configuration/2 Input/Discovery Workflow Specification.md (86 lines)

## Decision Log

### Project Governance & Structure
- **REQ-001**: Establish dual executive sponsorship (Sean Scanlon - GSI; Matt - KBM Hoag) for escalation and strategic decisions (ALIGNS) - "Executive Sponsor: Sean Scanlon (EVP, NetSuite Practice)" and "Executive Sponsor: Matt"
- **REQ-002**: Designate Lorraine Guzman as Program Manager to lead internal coordination and change management (ALIGNS) - "Program Manager: Lorraine Guzman (Head of Finance)"
- **REQ-003**: Assign Kimmy Katsuyoshi as Change Management Lead for user adoption strategy (ALIGNS) - "Change Management Lead: Kimmy Katsuyoshi (Director of Account Management)"
- **REQ-004**: Establish functional workstream leads from department SMEs (ALIGNS) - "Functional Workstream Leads/SMEs: Department-specific subject matter experts"

### Implementation Methodology
- **REQ-005**: Follow DREAM methodology (Discovery → Realize → Educate → Activate/Naturalize → Maintain) (ALIGNS) - "IMPLEMENTATION METHODOLOGY: DREAM" section detailed
- **REQ-006**: Execute 6-8 week Discovery phase with validation focus vs traditional discovery (ALIGNS) - "Discovery Timeline: 6-8 weeks (potentially longer based on complexity and client availability)"
- **REQ-007**: Conduct 1.5-2 hour discovery sessions with Part 1 (NetSuite overview) and Part 2 (analysis & questions) (ALIGNS) - "Session Format (1.5-2 hours each)"
- **REQ-008**: Create BRDs for all 8 process areas (Marketing, CRM, Pre-Quote, Order Mgmt, Operations, Financial, BI, System Setup) (ALIGNS) - "Process Areas Covered" list and "Business Requirements Documents (BRDs) - One per process area"

### System Configuration
- **REQ-009**: Install 5 Orion Suite Apps into NetSuite Financial Premium account (ALIGNS) - "Install 5 Suite Apps into NetSuite account" and "5 Suite Apps installed into NetSuite instance"
- **REQ-010**: Configure 25+ custom Orion roles and deactivate standard NetSuite roles (ALIGNS) - "25+ custom roles and permissions" and "Inactivated standard roles"
- **REQ-011**: Implement Orion custom forms, fields, and furniture-specific workflows (ALIGNS) - "Custom forms and fields" and "Furniture-specific workflows and automation"
- **REQ-012**: Set up chart of accounts as critical first configuration step (ALIGNS) - "Chart of accounts setup (critical first step)"
- **REQ-013**: Reduce chart of accounts from 40+ pages to few hundred accounts (ADAPT) - "Chart of accounts: Target reduction from 40+ pages to few hundred accounts"
- **REQ-014**: Configure NetSuite Financial Premium SKU with Advanced Inventory Module (ALIGNS) - "NetSuite SKU: Financial Premium (previously Retail Premium) - Advanced Inventory Module included"

### Data Migration Strategy
- **REQ-015**: Import financial historical data back to 2017 (KB workspace) using end-of-month trial balances via CSV (ALIGNS) - "Historical data back to 2017 (KB workspace)" and "End-of-month trial balances imported via CSV"
- **REQ-016**: Determine Hoag workspace historical data import range (TBD) (ALIGNS) - "Hoag workspace history TBD"
- **REQ-017**: Archive pre-2017 data separately outside NetSuite for historical reference (ADAPT) - "Pre-2017 data exported and archived separately" and "Not accessible through NetSuite"
- **REQ-018**: Use SQL backend "backdoor" access to extract Core data without vendor involvement (ALIGNS) - "SQL backend access confirmed (no Core involvement needed)" and "Joe Keller has extraction tool"
- **REQ-019**: Import 2-5 years financial data (up to 10 years possible) for period-over-period reporting (ALIGNS) - "2-5 years typical import range (up to 10 years possible)"

### Integration Requirements
- **REQ-020**: Implement Miller Knoll Exemplis integration for product ordering (ALIGNS) - "Miller Knoll: Exemplis integration completed"
- **REQ-021**: Configure Bank Feeds Suite App for West Coast Community Bank (ALIGNS) - "Bank Feeds Suite App"
- **REQ-022**: Configure Advanced Electronic Bill Payments Suite App for automated bank reconciliation (ALIGNS) - "Advanced Electronic Bill Payments Suite App - Automated reconciliation"
- **REQ-023**: Establish Paylocity CSV journal entry import for payroll (may change platforms) (ALIGNS) - "Paylocity (may change) - Separate from NetSuite - CSV import of journal entries"
- **REQ-024**: Automate Expensify integration to eliminate manual Excel upload/download (ACCOMMODATE) - "Goal: automated integration - Current process: Excel download/upload - Desire to eliminate manual reconciliation"
- **REQ-025**: Configure Google Drive bi-directional integration for folder structure access (ALIGNS) - "Bi-directional file access - Folder structure visible in NetSuite"
- **REQ-026**: Extend manufacturer integration platform to additional vendors (pending participation) (ALIGNS) - "Extensible to other manufacturers" and "Human Scale - declined integration; National - declined integration"

### Training Strategy
- **REQ-027**: Deliver multi-format training (live recorded sessions, documentation, videos, user guides) (ALIGNS) - "Training Formats: 1. Live Training Sessions (recorded), 2. Documentation, 3. Self-Service Options"
- **REQ-028**: Create process decks with step-by-step walkthroughs and video accompaniment (ALIGNS) - "Process decks showing step-by-step - Videos accompanying documentation"
- **REQ-029**: Identify and invest additional training in NetSuite Champions/Power Users for peer support (ALIGNS) - "Identify power users early - Invest additional training time - Enable peer-to-peer support"
- **REQ-030**: Conduct department-specific and role-based training sessions (ALIGNS) - "Department-specific training - Role-based content"
- **REQ-031**: Provide User Acceptance Testing (UAT) as part of Educate phase (ALIGNS) - "User Acceptance Testing (UAT)" in Educate phase

### Communication & Collaboration
- **REQ-032**: Use Microsoft Teams as primary communication platform (KBM joins GSI Teams) (ALIGNS) - "Communication Platform: Microsoft Teams (client will join GSI Teams)"
- **REQ-033**: Establish weekly status reporting cadence (ALIGNS) - "Status Reporting: Weekly"
- **REQ-034**: Schedule working sessions at weekly to 3x per week cadence (to be determined) (ALIGNS) - "Working Sessions: Weekly to 3x per week (cadence to be determined)"
- **REQ-035**: Record all sessions with backup recording devices (ALIGNS) - "All sessions recorded - Multiple recording devices (backup pin recorder)"
- **REQ-036**: Generate AI-assisted transcripts for all sessions to build BRDs (ALIGNS) - "Transcripts generated for all sessions - AI-assisted documentation from transcripts"
- **REQ-037**: Implement change control process with change orders post-discovery scope lock (ALIGNS) - "Project scope locked after discovery - Change orders required for new requirements"

### Go-Live Strategy
- **REQ-038**: Execute soft cutover go-live strategy (not hard cutover) (ALIGNS) - "Go-Live Strategy: Soft cutover recommended"
- **REQ-039**: Start new business in NetSuite on go-live date while completing existing projects in Core (ADAPT) - "Start new business in NetSuite on go-live date - Run existing projects in Core until completion"
- **REQ-040**: Plan for ~6 month dual-system period during transition (ADAPT) - "Typical dual-system period: ~6 months"
- **REQ-041**: Migrate projects from Core to NetSuite in phases where possible (ADAPT) - "Phased project migration where possible"
- **REQ-042**: Provide on-site or Microsoft Teams channel support during go-live (ALIGNS) - "On-site support option or Microsoft Teams channel support"
- **REQ-043**: Include 30 days post go-live support (ALIGNS) - "Post go-live support (30 days included)"

### Post-Go-Live Support & Optimization
- **REQ-044**: Establish Suite Care program for ongoing support and optimization (ALIGNS) - "Suite Care program options - Managed services or bank of hours"
- **REQ-045**: Enable client self-sufficiency on the platform as long-term goal (ALIGNS) - "Philosophy: Client self-sufficiency on the platform"

### Project Numbering & Transaction Management
- **REQ-046**: Establish consistent project number/naming across Opportunity → Proposal → Sales Order → PO (ALIGNS) - "Project numbering convention to be established (opportunity, proposal, sales order prefixes)" and "Project number consistent across all transactions"
- **REQ-047**: Enable global search by project, customer name, phone number (ALIGNS) - "Global search capabilities (by project, customer name, phone number)"
- **REQ-048**: Configure recent transaction dialog for quick access to last 10-15 items (ALIGNS) - "Recent transaction dialog box (last 10-15 items)"

### Solution Design Requirements
- **REQ-049**: Create Solution Design documents for all customizations regardless of size (ALIGNS) - "Solution Designs - For all customizations (regardless of size) - Documented for every custom report, saved search, integration"

### Historical Data Access
- **REQ-050**: Establish separate archive system for pre-2017 and post-migration Core data lookups (ACCOMMODATE) - "Archive system for lookups - Not searchable in same way as live data - Adjustment period required for users"

## Action Items

### Immediate Actions
**ACTION**: Provide all document templates (proposals, invoices, vendor-facing documents)  
**ASSIGNED TO**: Kip  
**DUE**: TBD  
**RELATED TO**: REQ-009, REQ-011

**ACTION**: Provide XML import template examples  
**ASSIGNED TO**: Matt  
**DUE**: TBD  
**RELATED TO**: REQ-015, REQ-018

**ACTION**: Provide approval workflow rules list  
**ASSIGNED TO**: Shannon  
**DUE**: TBD  
**RELATED TO**: REQ-011

**ACTION**: Confirm order type list  
**ASSIGNED TO**: Lorraine  
**DUE**: TBD  
**RELATED TO**: REQ-011

**ACTION**: Review and confirm discovery session attendees  
**ASSIGNED TO**: Team  
**DUE**: TBD  
**RELATED TO**: REQ-007

### Configuration Planning Actions
**ACTION**: Prepare chart of accounts for reduction from 40+ pages to few hundred accounts  
**ASSIGNED TO**: Lorraine (Finance Lead)  
**DUE**: Before Realize phase  
**RELATED TO**: REQ-012, REQ-013

**ACTION**: Determine Hoag workspace historical data import timeframe  
**ASSIGNED TO**: Lorraine (Finance Lead)  
**DUE**: During Discovery phase  
**RELATED TO**: REQ-016

**ACTION**: Finalize payroll/HR platform selection (Paylocity or alternative)  
**ASSIGNED TO**: Michelle Merlo (HR Director)  
**DUE**: Before integration configuration  
**RELATED TO**: REQ-023

**ACTION**: Finalize expense management platform selection (Expensify or alternative)  
**ASSIGNED TO**: TBD - Suggest: Finance Lead (Lorraine)  
**DUE**: Before integration configuration  
**RELATED TO**: REQ-024

**ACTION**: Make final decision on SharePoint vs Google Drive  
**ASSIGNED TO**: Kip (IT Director)  
**DUE**: Before integration configuration  
**RELATED TO**: REQ-025

**ACTION**: Determine continuation/elimination of Asana  
**ASSIGNED TO**: TBD - Suggest: Program Manager (Lorraine) and Change Management Lead (Kimmy)  
**DUE**: During Discovery phase  
**RELATED TO**: Systems consolidation strategy

**ACTION**: Contact manufacturer partners to encourage integration participation (Human Scale, National)  
**ASSIGNED TO**: TBD - Suggest: Matt (Executive Sponsor) with KBM Hoag account relationships  
**DUE**: During Discovery/Realize phase  
**RELATED TO**: REQ-026

### Training & Change Management Actions
**ACTION**: Identify NetSuite Champions/Power Users across departments  
**ASSIGNED TO**: Kimmy Katsuyoshi (Change Management Lead)  
**DUE**: Early in Realize phase  
**RELATED TO**: REQ-029

**ACTION**: Develop department-specific training schedules and content  
**ASSIGNED TO**: TBD - Suggest: GSI training team with Kimmy coordination  
**DUE**: During Educate phase planning  
**RELATED TO**: REQ-030

**ACTION**: Set up Microsoft Teams environment and invite KBM Hoag team  
**ASSIGNED TO**: TBD - Suggest: Tom Shannon (PMO Lead)  
**DUE**: Immediately  
**RELATED TO**: REQ-032

## Additional Sessions Needed

### Session: Chart of Accounts Deep Dive
- **Participants Needed**: Lorraine Guzman (Finance Lead), Kevin Yip (GL Accounting Manager), GSI Finance Consultant
- **Questions to Address**:
  • Current chart of accounts structure and mapping
  • Account consolidation strategy (from 40+ pages to few hundred)
  • Special GL account requirements
  • Department/location segment structure
  • Class and location tracking requirements
- **Priority**: High - Critical first configuration step
- **Suggested Duration**: 2 hours
- **Dependencies**: REQ-012, REQ-013
- **Evidence**: "Chart of accounts setup (critical first step)" and "Target reduction from 40+ pages to few hundred accounts"

### Session: Data Migration Planning
- **Participants Needed**: Lorraine Guzman, Kevin Yip, Joe Keller (Core extraction expert), GSI Data Migration Lead
- **Questions to Address**:
  • Detailed Core data extraction process and timeline
  • Hoag workspace historical data determination
  • Data validation and cleansing requirements
  • Archive system design for pre-2017 data
  • Migration testing strategy
- **Priority**: High - Foundation for go-live
- **Suggested Duration**: 2 hours
- **Dependencies**: REQ-015, REQ-016, REQ-017, REQ-018, REQ-050
- **Evidence**: "Dedicated migration strategy document" and "Historical Access Post-Migration" section requirements

### Session: Integration Architecture Review
- **Participants Needed**: Kip Hurdick (IT Director), GSI Integration Lead, potentially vendor representatives
- **Questions to Address**:
  • Payroll system final selection and integration approach
  • Expense management automation requirements
  • Google Drive vs SharePoint final decision and configuration
  • Additional manufacturer integration strategy
  • API access and authentication requirements
- **Priority**: Medium - Needed before Realize phase completion
- **Suggested Duration**: 1.5 hours
- **Dependencies**: REQ-020 through REQ-026
- **Evidence**: "Pending/Potential Integrations" section and open questions list

### Session: Go-Live Strategy Workshop
- **Participants Needed**: Executive team (Matt, Lorraine), Project Managers (Wendy, Shannon), General Managers (Jill, Kate, Alex), GSI PMO
- **Questions to Address**:
  • Specific go-live date target and dependencies
  • Dual-system operational procedures and responsibilities
  • Project migration sequencing (which projects move when)
  • Cutover weekend activities and resource allocation
  • Support coverage during transition period
- **Priority**: Medium - Needed during late Discovery/early Realize
- **Suggested Duration**: 2 hours
- **Dependencies**: REQ-038 through REQ-043
- **Evidence**: "Go-Live Strategy: Soft cutover recommended" section details

## New Questions Identified

### Proposed New Question 1: User Role and Permission Structure
- **Asked By**: Implicit requirement from transcript
- **Context**: With 25+ custom Orion roles, need to map KBM Hoag users to appropriate roles
- **Suggested Placement**: System Setup and Configuration section
- **Evidence**: "25+ custom roles and permissions" and need to "Identify system administrators"

### Proposed New Question 2: Historical Data Access Requirements
- **Asked By**: Matt and team discussing Core transition
- **Context**: Users need clarity on what historical data will/won't be accessible post-migration
- **Suggested Placement**: Data Migration section
- **Evidence**: "Won't be 'as easy to go through' as Core" and "Mourning process acknowledged"

### Proposed New Question 3: Manufacturer Integration Prioritization
- **Asked By**: Implicit from declined integration discussion
- **Context**: Which manufacturers beyond Miller Knoll are highest priority for integration
- **Suggested Placement**: Integration Requirements section
- **Evidence**: "Human Scale - declined integration; National - declined integration - May need KBM Hoag assistance"

---

## QUESTIONNAIRE RESPONSES

### 1. PROJECT GOVERNANCE & TEAM STRUCTURE

#### 1.1 What is the executive sponsorship structure for this implementation?

**Answer:**
Dual executive sponsorship model established with:
- **GSI Executive Sponsor**: Sean Scanlon (EVP, NetSuite Practice) for GSI escalations and resource decisions
- **KBM Hoag Executive Sponsor**: Matt for internal alignment and strategic decisions

**User Stories:**
- As Executive Sponsors, we need clear escalation paths and decision authority so that the project maintains momentum when issues arise

**BRD Requirements:**
- [REQUIREMENT] Establish dual executive sponsorship with defined escalation process (ID: REQ-001, Type: Non-Functional)
- [PRIORITY] Must-Have

**Stakeholder Impact:**
- **Primary Users**: Sean Scanlon (GSI EVP), Matt (KBM Executive Sponsor)
- **Approvers**: Both executive sponsors for major decisions and scope changes

**Evidence:**
- "Executive Sponsor: Sean Scanlon (EVP, NetSuite Practice)" - Transcript
- "Executive Sponsor: Matt" - Transcript
- "It takes two parties to make this successful" - Partnership approach statement

**Confidence Rating**: 98% - Explicitly documented with clear role assignments and organizational structure

---

#### 1.2 Who is leading the program management and change management efforts?

**Answer:**
- **Program Manager**: Lorraine Guzman (Head of Finance) - responsible for internal coordination, task management, scheduling, and timely decision-making
- **Change Management Lead**: Kimmy Katsuyoshi (Director of Account Management) - responsible for user adoption strategy, internal champions identification, and department-specific communication approaches

**User Stories:**
- As a Program Manager (Lorraine Guzman), I need to coordinate internal resources and manage project tasks so that KBM Hoag delivers on commitments timely
- As a Change Management Lead (Kimmy Katsuyoshi), I need to identify champions and create adoption strategies so that users embrace NetSuite successfully

**BRD Requirements:**
- [REQUIREMENT] Designate Program Manager for internal project coordination (ID: REQ-002, Type: Non-Functional)
- [REQUIREMENT] Assign Change Management Lead for user adoption (ID: REQ-003, Type: Non-Functional)
- [PRIORITY] Must-Have

**Stakeholder Impact:**
- **Primary Users**: Lorraine Guzman (Program Manager), Kimmy Katsuyoshi (Change Management Lead)
- **Secondary Users**: Department leads, functional workstream leads
- **Impacted Parties**: All end users affected by change management approach

**Evidence:**
- "Program Manager: Lorraine Guzman (Head of Finance)" - Transcript
- "Change Management Lead: Kimmy Katsuyoshi (Director of Account Management)" - Transcript
- "Strong executive sponsorship - Internal champions identified - User adoption strategy" - Success factors

**Confidence Rating**: 98% - Explicitly documented in governance structure

---

#### 1.3 What is the functional workstream structure?

**Answer:**
Functional workstream leads are department-specific subject matter experts (SMEs) who will participate in their respective process area discovery sessions and serve as decision-makers and validators for their domains.

Process areas include:
1. Marketing & Lead Management
2. CRM (Customer Relationship Management)
3. Pre-Quote (Design requests, labor quotes, requirements)
4. Order Management (Quote through acknowledgement)
5. Operations (Requisitions through punch completion)
6. Financial Management
7. Business Intelligence & Reporting
8. System Setup and Configuration

**User Stories:**
- As a Functional Workstream Lead, I need clear authority and responsibility for my process area so that requirements are accurately captured and validated

**BRD Requirements:**
- [REQUIREMENT] Establish functional workstream leads by process area (ID: REQ-004, Type: Non-Functional)
- [PRIORITY] Must-Have

**Stakeholder Impact:**
- **Primary Users**: Department SMEs serving as workstream leads
- **Approvers**: Workstream leads for their respective process areas

**Evidence:**
- "Functional Workstream Leads/SMEs: Department-specific subject matter experts" - Transcript
- "Process Areas Covered: 1. Marketing & Lead Management, 2. CRM..." - Full list in transcript

**Confidence Rating**: 95% - Structure clearly defined, specific names to be confirmed per process area

---

### 2. IMPLEMENTATION METHODOLOGY

#### 2.1 What implementation methodology will be followed?

**Answer:**
The project will follow the **DREAM methodology**, a structured five-phase approach:

**D - Discovery (6-8 weeks)**
- Comprehensive business process analysis with validation focus
- Requirements gathering across 8 process areas
- More validation than traditional "from scratch" discovery
- Focus on confirming known requirements and finding unique elements

**R - Realize (GSI-heavy phase)**
- System configuration begins
- Install 5 Orion Suite Apps into NetSuite account
- Chart of accounts setup (critical first step)
- Solution design implementation
- System walkthrough sessions
- Identification of system administrators
- Lightest phase for client

**E - Educate (Client-heavy phase)**
- Process walkthroughs
- End user training
- User Acceptance Testing (UAT)
- Change management preparation
- Training documentation (product guides, user guides)
- Recorded training sessions
- Heaviest phase for client

**A - Activate/Naturalize (Go-Live)**
- Soft cutover go-live strategy
- Start new business in NetSuite on go-live date
- Run existing projects in Core until completion
- Typical dual-system period: ~6 months
- Phased project migration where possible
- Go-live checklist
- On-site support option or Microsoft Teams channel support
- Post go-live support (30 days included)

**M - Maintain/Maximize**
- Ongoing support and optimization
- Suite Care program options
- Managed services or bank of hours
- Philosophy: Client self-sufficiency on the platform

**User Stories:**
- As a Project Team Member, I need a clear implementation roadmap so that I understand what happens when and can plan my involvement accordingly

**BRD Requirements:**
- [REQUIREMENT] Follow DREAM methodology for implementation (ID: REQ-005, Type: Non-Functional)
- [PRIORITY] Must-Have
- [ASSUMPTION] 6-8 week Discovery phase is adequate to validate all requirements

**Stakeholder Impact:**
- **Primary Users**: All project team members (GSI and KBM Hoag)
- **Impacted Parties**: All end users through phased rollout

**Evidence:**
- "IMPLEMENTATION METHODOLOGY: DREAM" - Transcript section header
- Detailed phase descriptions throughout transcript
- "Lightest phase for client" (Realize) vs "Heaviest phase for client" (Educate)

**Confidence Rating**: 99% - Extremely detailed methodology documentation with phase-specific activities

---

#### 2.2 How will discovery sessions be structured?

**Answer:**
Discovery sessions will be 1.5-2 hours each, following a two-part format:

**Part 1: NetSuite/Orion Overview**
- Quick preview of system capabilities
- Screenshots and demonstrations (when appropriate)
- Process maps and workflows
- "Art of the possible" demonstration

**Part 2: Analysis & Questions**
- Current state investigation
- Objectives and strategy discussion
- Requirements identification (functional and technical)
- Gap analysis (Align, Adapt, or Accommodate)

All sessions will be:
- Recorded with backup recording devices
- Transcribed using AI-assisted tools
- Used to build BRDs and track requirements

**User Stories:**
- As a Discovery Session Participant, I need to see how NetSuite works before being asked questions so that I can provide informed requirements
- As a Business Analyst, I need structured session formats so that all process areas are documented consistently

**BRD Requirements:**
- [REQUIREMENT] Conduct 1.5-2 hour discovery sessions in two-part format (ID: REQ-007, Type: Non-Functional)
- [REQUIREMENT] Record all sessions with backup devices (ID: REQ-035, Type: Non-Functional)
- [REQUIREMENT] Generate AI-assisted transcripts for documentation (ID: REQ-036, Type: Non-Functional)
- [PRIORITY] Must-Have

**Stakeholder Impact:**
- **Primary Users**: GSI consultants, KBM Hoag SMEs
- **Secondary Users**: Support staff reviewing recordings

**Evidence:**
- "Session Format (1.5-2 hours each): Part 1: NetSuite/Orion Overview... Part 2: Analysis & Questions" - Transcript
- "All sessions recorded - Multiple recording devices (backup pin recorder)" - Recording policy
- "AI-assisted documentation from transcripts" - Documentation approach

**Confidence Rating**: 98% - Explicit session structure documented with clear format

---

#### 2.3 What deliverables will be produced during Discovery?

**Answer:**

**1. Business Requirements Documents (BRDs)** - One per process area (8 total)
- Collaborative documents with review mode
- Track changes and comments enabled
- Client sign-off required
- Becomes implementation blueprint

**2. Solution Designs** - For all customizations (regardless of size)
- Documented for every custom report, saved search, integration
- Included in project scope

**3. Data Migration Strategy Document**
- Financial data: Trial balances from 2017 forward (end-of-month)
- 2-5 years typical, up to 10 years possible
- CSV import process
- Core data accessible via SQL backend
- No Core involvement needed for data extraction

**4. Additional Session Scheduling**
- Deeper functional analysis sessions scheduled
- Follow-up meetings for complex topics

**User Stories:**
- As a Stakeholder, I need comprehensive BRDs with my sign-off so that the implementation reflects agreed requirements
- As a Technical Lead, I need solution designs for every customization so that development is consistent and documented

**BRD Requirements:**
- [REQUIREMENT] Create BRDs for all 8 process areas with client sign-off (ID: REQ-008, Type: Non-Functional)
- [REQUIREMENT] Document solution designs for all customizations (ID: REQ-049, Type: Non-Functional)
- [REQUIREMENT] Create comprehensive data migration strategy document (ID: REQ-015, Type: Non-Functional)
- [PRIORITY] Must-Have

**Stakeholder Impact:**
- **Primary Users**: Project team members
- **Approvers**: Functional workstream leads for BRD sign-off
- **Impacted Parties**: Implementation team using BRDs as blueprint

**Evidence:**
- "Business Requirements Documents (BRDs) - One per process area - Collaborative documents with review mode - Client sign-off required" - Transcript
- "Solution Designs - For all customizations (regardless of size)" - Transcript
- "Data Migration Strategy Document - Financial data: Trial balances from 2017 forward" - Transcript

**Confidence Rating**: 98% - Comprehensive deliverables list with clear requirements

---

### 3. SYSTEM CONFIGURATION & SETUP

#### 3.1 What is the Orion platform and how does it differ from standard NetSuite?

**Answer:**
**Orion Definition:**
- Pre-configured NetSuite solution specific to furniture dealers
- Proprietary IP owned by Approprio Cloud Solutions
- Licensed to KBM Hoag
- Implementation support by GSI and SuiteCentric
- ~95% of requirements already built (minimal customization needed)

**Orion Components:**
- 5 Suite Apps installed into NetSuite instance
- Custom forms and fields
- 25+ custom roles and permissions
- Furniture-specific workflows and automation
- Pre-built reports and dashboards

**Key Differences from Standard NetSuite:**
- **Standard NetSuite Implementation**: 50% customization typical
- **Orion Implementation**: 5-10% customization typical
- **NetSuite SKU**: Financial Premium (previously Retail Premium) with Advanced Inventory Module
- **Pre-Configuration**: Chart of accounts import, Suite Apps installation, custom roles, custom forms/fields, data set installation, inactivated standard roles

**Miller Knoll Involvement:**
- Project sponsor role
- Product owner: Dustin
- No access to dealer NetSuite databases
- Clear separation maintained for dealer autonomy
- Support for solution architecture
- Occasional project management resources

**Competitive Advantage:**
- Consultants gain furniture industry expertise
- Same consultants across multiple furniture implementations
- Industry-specific solution vs. generic NetSuite implementation
- Can accommodate strategic advantages through configurability

**User Stories:**
- As a Dealer, I need a furniture-specific solution so that I'm not paying for extensive customization of generic ERP
- As an Administrator, I need pre-built roles and workflows so that configuration time is minimized

**BRD Requirements:**
- [REQUIREMENT] Install 5 Orion Suite Apps into NetSuite Financial Premium account (ID: REQ-009, Type: Functional)
- [REQUIREMENT] Configure 25+ custom Orion roles and deactivate standard NetSuite roles (ID: REQ-010, Type: Functional)
- [REQUIREMENT] Implement Orion custom forms, fields, and furniture-specific workflows (ID: REQ-011, Type: Functional)
- [REQUIREMENT] Configure NetSuite Financial Premium SKU with Advanced Inventory Module (ID: REQ-014, Type: Functional)
- [PRIORITY] Must-Have
- [ASSUMPTION] 95% of requirements met by Orion out-of-box

**Stakeholder Impact:**
- **Primary Users**: All NetSuite users
- **Approvers**: IT Director (Kip) for system architecture
- **Impacted Parties**: Entire organization through system usage

**Evidence:**
- "Pre-configured NetSuite solution specific to furniture dealers - ~95% of requirements already built" - Transcript
- "5 Suite Apps installed into NetSuite instance - 25+ custom roles and permissions" - Transcript
- "Typical NetSuite implementation: 50% customization - Orion implementation: 5-10% customization" - Transcript
- "NetSuite SKU: Financial Premium (previously Retail Premium) - Advanced Inventory Module included" - Transcript

**Confidence Rating**: 99% - Extremely detailed explanation of Orion platform and differentiators

---

#### 3.2 What are the critical first configuration steps?

**Answer:**
**Critical First Step: Chart of Accounts Setup**

This is explicitly identified as the most critical first configuration step. The approach includes:

**Current State:**
- Chart of accounts currently 40+ pages long
- Contains excessive detail and granularity
- Likely accumulated over years in Core

**Target State:**
- Reduce to "few hundred accounts"
- Streamlined structure for NetSuite
- Maintained ability for detailed reporting through dimensions (departments, locations, classes)

**Configuration Sequence:**
1. Chart of accounts setup (first and critical)
2. Suite Apps installation (5 apps)
3. Custom forms and fields implementation
4. Role configuration (25+ custom roles)
5. Data set installation
6. Standard role deactivation

**User Stories:**
- As a Finance Lead (Lorraine Guzman), I need a streamlined chart of accounts so that financial reporting is efficient and maintainable
- As an Accountant (Kevin Yip), I need proper GL structure so that transactions post to correct accounts

**BRD Requirements:**
- [REQUIREMENT] Set up chart of accounts as critical first configuration step (ID: REQ-012, Type: Functional)
- [REQUIREMENT] Reduce chart of accounts from 40+ pages to few hundred accounts (ID: REQ-013, Type: Functional)
- [PRIORITY] Must-Have
- [CONSTRAINT] Chart of accounts must be finalized before other configuration begins

**Stakeholder Impact:**
- **Primary Users**: Lorraine Guzman (Finance Lead), Kevin Yip (GL Accounting Manager)
- **Approvers**: Lorraine for final chart of accounts structure
- **Impacted Parties**: All users entering financial transactions

**Evidence:**
- "Chart of accounts setup (critical first step)" - Transcript
- "Chart of accounts: Target reduction from 40+ pages to few hundred accounts" - Transcript
- Configuration sequence in Realize phase description

**Confidence Rating**: 98% - Explicitly stated as critical first step with clear rationale

**Outstanding Items:**
- Need detailed chart of accounts mapping session (scheduled as additional session needed)
- Specific account structure and segments to be determined

---

### 4. DATA MIGRATION STRATEGY

#### 4.1 What financial data will be migrated and how far back?

**Answer:**
**KB Workspace Financial Data:**
- Historical data back to 2017 confirmed
- End-of-month trial balances imported via CSV
- Enables period-over-period reporting capability
- 2-5 years typical import range (up to 10 years possible)

**Hoag Workspace Financial Data:**
- Historical data timeframe TBD
- Decision by Finance leader (Lorraine)
- Will follow same CSV import process

**Pre-2017 Data (Archived):**
- Exported and archived separately outside NetSuite
- Not accessible through NetSuite interface
- Separate archive system for historical reference
- Used for RFP responses and client history requests
- Not searchable in same way as live data
- Adjustment period required for users

**Core Data Extraction:**
- SQL backend access confirmed (no Core involvement needed)
- Data migration tool available
- "Backdoor" access strategy
- Joe Keller has extraction tool and specific approach
- Strategy to request information without "tipping them off"

**User Stories:**
- As a Finance Analyst, I need historical financial data in NetSuite so that I can perform period-over-period analysis
- As a Sales Rep, I need access to historical project data so that I can reference past work for clients

**Current State Process:**
**PROCESS**: Historical Data Access in Core  
**TRIGGER**: User needs to look up past project or financial information  
**STEPS**:
1. User searches Core database with known data points → finds records easily
2. User accesses complete historical detail → reviews as needed
**SYSTEMS INVOLVED**: Core ERP  
**PAIN POINTS**: Won't be "as easy to go through" in archive system post-migration; different access method requires adjustment

**BRD Requirements:**
- [REQUIREMENT] Import financial historical data back to 2017 (KB workspace) using end-of-month trial balances via CSV (ID: REQ-015, Type: Functional)
- [REQUIREMENT] Determine Hoag workspace historical data import range (TBD) (ID: REQ-016, Type: Functional)
- [REQUIREMENT] Archive pre-2017 data separately outside NetSuite for historical reference (ID: REQ-017, Type: Functional)
- [REQUIREMENT] Use SQL backend "backdoor" access to extract Core data without vendor involvement (ID: REQ-018, Type: Functional)
- [REQUIREMENT] Import 2-5 years financial data (up to 10 years possible) for period-over-period reporting (ID: REQ-019, Type: Functional)
- [REQUIREMENT] Establish separate archive system for pre-2017 and post-migration Core data lookups (ID: REQ-050, Type: Functional)
- [PRIORITY] Must-Have (REQ-015, REQ-018, REQ-019); Should-Have (REQ-016, REQ-017, REQ-050)
- [RISK] Users may struggle with different historical data access methods post-migration
- [ASSUMPTION] CSV import process is adequate for trial balance data accuracy

**Stakeholder Impact:**
- **Primary Users**: Finance team (Lorraine, Kevin), Sales team needing historical references
- **Approvers**: Lorraine for data import scope decisions
- **Impacted Parties**: All users who reference historical data

**Evidence:**
- "Historical data back to 2017 (KB workspace) - Hoag workspace history TBD" - Transcript
- "End-of-month trial balances imported via CSV" - Transcript
- "Pre-2017 data exported and archived separately - Not accessible through NetSuite" - Transcript
- "SQL backend access confirmed (no Core involvement needed) - Joe Keller has extraction tool" - Transcript
- "Won't be 'as easy to go through' as Core - Archive required for old data lookups" - Concerns section
- "2-5 years typical import range (up to 10 years possible)" - Transcript

**Confidence Rating**: 95% - Clear strategy documented, Hoag workspace timeframe TBD pending Lorraine decision

**Outstanding Items:**
- Hoag workspace historical data timeframe decision needed
- Archive system design and access procedures to be defined
- User training on historical data access differences

---

### 5. INTEGRATION REQUIREMENTS

#### 5.1 What integrations are confirmed and what are pending decisions?

**Answer:**

**Confirmed Integrations:**

**1. Miller Knoll - Exemplis Integration** (COMPLETED)
- Product ordering system integration
- Orion integration platform pre-built
- Designed for fast implementation

**2. Banking - West Coast Community Bank**
- Bank Feeds Suite App for automated transaction import
- Advanced Electronic Bill Payments Suite App
- Automated bank reconciliation capability

**Pending/Decision Required:**

**3. Payroll - Paylocity** (MAY CHANGE)
- Currently separate from NetSuite
- CSV import of journal entries
- HR platform evaluation ongoing
- May switch to different provider

**4. Expense Management - Expensify** (MAY CHANGE)
- Currently manual process (Excel download/upload)
- Goal: Automated integration
- Desire to eliminate manual reconciliation
- Platform decision pending

**5. File Storage - Google Drive vs SharePoint**
- Google Drive: Bi-directional file access, folder structure visible in NetSuite, tighter than simple URL links
- SharePoint: Alternative being considered
- Final decision needed

**6. Task Management - Asana**
- Evaluation ongoing for continuation
- May reduce usage or eliminate
- Currently used for certain functions (TBD)

**7. Additional Manufacturers**
- Human Scale - declined integration
- National - declined integration
- May need KBM Hoag assistance to encourage participation
- Orion integration platform extensible to other manufacturers

**User Stories:**
- As a Finance Team Member, I need automated bank reconciliation so that I eliminate manual matching work
- As an Employee, I need automated expense submission so that I don't manually upload Excel files
- As a Project Manager, I need integrated file storage so that documents are accessible from NetSuite

**BRD Requirements:**
- [REQUIREMENT] Implement Miller Knoll Exemplis integration for product ordering (ID: REQ-020, Type: Functional) - ALIGNS
- [REQUIREMENT] Configure Bank Feeds Suite App for West Coast Community Bank (ID: REQ-021, Type: Functional) - ALIGNS
- [REQUIREMENT] Configure Advanced Electronic Bill Payments Suite App for automated bank reconciliation (ID: REQ-022, Type: Functional) - ALIGNS
- [REQUIREMENT] Establish Paylocity CSV journal entry import for payroll (may change platforms) (ID: REQ-023, Type: Functional) - ALIGNS
- [REQUIREMENT] Automate Expensify integration to eliminate manual Excel upload/download (ID: REQ-024, Type: Functional) - ACCOMMODATE
- [REQUIREMENT] Configure Google Drive bi-directional integration for folder structure access (ID: REQ-025, Type: Functional) - ALIGNS
- [REQUIREMENT] Extend manufacturer integration platform to additional vendors (pending participation) (ID: REQ-026, Type: Functional) - ALIGNS
- [PRIORITY] Must-Have (REQ-020, REQ-021, REQ-022); Should-Have (REQ-023, REQ-024, REQ-025, REQ-026)
- [RISK] Manufacturer integration adoption dependent on vendor participation
- [CONSTRAINT] Some integrations pending platform selection decisions

**Stakeholder Impact:**
- **Primary Users**: Finance team (banking, payroll, expenses), All users (file storage), Project teams (manufacturers)
- **Approvers**: Kip (IT Director) for integration architecture; Michelle (HR) for payroll; Lorraine/Finance for expenses
- **Impacted Parties**: All employees for payroll/expenses; client-facing teams for manufacturer integrations

**Evidence:**
- "Miller Knoll: Exemplis integration completed" - Transcript
- "Bank Feeds Suite App - Advanced Electronic Bill Payments Suite App - Automated reconciliation" - Transcript
- "Paylocity (may change) - Separate from NetSuite - CSV import of journal entries - HR platform evaluation ongoing" - Transcript
- "Expensify (may change) - currently manual - Goal: automated integration - Current process: Excel download/upload - Desire to eliminate manual reconciliation" - Transcript
- "Google Drive Integration: Bi-directional file access - Folder structure visible in NetSuite - Tighter than simple URL links" - Transcript
- "Human Scale - declined integration; National - declined integration - May need KBM Hoag assistance to encourage participation" - Transcript

**Confidence Rating**: 90% - Confirmed integrations clear; pending integrations have identified decision points

**Outstanding Items:**
- Final payroll/HR platform selection
- Final expense management platform selection and integration approach
- Google Drive vs SharePoint decision
- Asana continuation determination
- Manufacturer integration outreach strategy

---

### 6. TRAINING STRATEGY

#### 6.1 What training formats and approaches will be used?

**Answer:**

**Training Formats (Multi-Modal Approach):**

**1. Live Training Sessions**
- Recorded for future reference
- Department-specific training content
- Role-based curriculum
- Accessible as ongoing resource

**2. Documentation**
- Process decks showing step-by-step procedures
- Videos accompanying documentation
- User guides for quick reference
- Product guides

**3. Self-Service Options**
- Recorded sessions searchable by topic
- Written guides scannable for quick answers
- Multiple learning formats to accommodate preferences
- On-demand access

**Current KBM Hoag Training Culture (to leverage):**
- Department leads conduct training (e.g., Jenny for account management)
- Documented processes with presentation decks
- Video accompaniment to written materials
- Multiple format options: watch video, listen to audio, or review deck

**NetSuite Champion Strategy:**
- Identify power users early in process
- Invest additional training time in champions
- Enable peer-to-peer support capability
- Reduce dependency on consultants
- Support ongoing team training

**User Stories:**
- As an End User, I need multiple training formats so that I can learn in the way that works best for me
- As a NetSuite Champion (TBD), I need deep training so that I can support my peers and reduce consultant dependency
- As a Department Lead, I need role-specific training materials so that I can train my team on their actual workflows

**Current State Process:**
**PROCESS**: Department Training (Current)  
**TRIGGER**: New process or system introduced  
**STEPS**:
1. Department lead (e.g., Jenny) creates process deck → documents step-by-step procedures
2. Department lead records accompanying video → provides audio and visual walkthrough
3. Team members choose format → watch video, listen to audio, or review deck
4. Team members reference materials → as needed for ongoing support
**SYSTEMS INVOLVED**: Current training tools and platforms  
**PAIN POINTS**: None identified - strong training culture exists to build upon

**BRD Requirements:**
- [REQUIREMENT] Deliver multi-format training (live recorded sessions, documentation, videos, user guides) (ID: REQ-027, Type: Non-Functional) - ALIGNS
- [REQUIREMENT] Create process decks with step-by-step walkthroughs and video accompaniment (ID: REQ-028, Type: Non-Functional) - ALIGNS
- [REQUIREMENT] Identify and invest additional training in NetSuite Champions/Power Users for peer support (ID: REQ-029, Type: Non-Functional) - ALIGNS
- [REQUIREMENT] Conduct department-specific and role-based training sessions (ID: REQ-030, Type: Non-Functional) - ALIGNS
- [REQUIREMENT] Provide User Acceptance Testing (UAT) as part of Educate phase (ID: REQ-031, Type: Non-Functional) - ALIGNS
- [PRIORITY] Must-Have
- [ASSUMPTION] KBM Hoag training culture and departmental approach will translate well to NetSuite training

**Stakeholder Impact:**
- **Primary Users**: All end users receiving training
- **Secondary Users**: NetSuite Champions providing peer support
- **Approvers**: Kimmy (Change Management Lead) for training strategy
- **Impacted Parties**: Department leads facilitating training

**Evidence:**
- "Training Formats: 1. Live Training Sessions (recorded), 2. Documentation, 3. Self-Service Options" - Transcript
- "Process decks showing step-by-step - Videos accompanying documentation" - Transcript
- "Identify power users early - Invest additional training time - Enable peer-to-peer support" - Champion strategy
- "Department-specific training - Role-based content" - Transcript
- "Client has good training culture with department leads" - Current approach
- "User Acceptance Testing (UAT)" in Educate phase - Transcript

**Confidence Rating**: 98% - Comprehensive training strategy documented leveraging existing training culture

**Outstanding Items:**
- Identify specific NetSuite Champions by department (action item for Kimmy)
- Develop detailed training schedule during Educate phase planning

---

### 7. COMMUNICATION & COLLABORATION

#### 7.1 What communication tools and cadences will be used?

**Answer:**

**Communication Platform: Microsoft Teams**
- KBM Hoag will join GSI Teams environment
- Chat threads for ongoing communication
- File sharing capability
- Meeting coordination

**Meeting Cadences:**
- **Status Reporting**: Weekly
- **Working Sessions**: Weekly to 3x per week (cadence to be determined based on phase and availability)
- **Discovery Sessions**: 1.5-2 hours each across 8 process areas over 6-8 weeks

**Recording & Documentation Policy:**
- All sessions recorded
- Multiple recording devices used (backup pin recorder)
- Transcripts generated for all sessions
- AI-assisted documentation from transcripts
- Transcripts help build BRDs and track requirements

**Change Control Process:**
- Project scope locked after discovery phase
- Change orders required for new requirements post-discovery
- Impact on timeline documented for any changes
- Client sign-off required for scope changes

**Business Cycle Considerations:**
- Q1 typically slowest (if any slowdown occurs)
- Team-dependent busy periods
- Heavy meeting days: Tuesday-Thursday
- Light meeting days: Monday, Friday
- Month-end: Finance team unavailable (closing period)
- December year-end (calendar year)

**User Stories:**
- As a Project Team Member, I need centralized communication in Teams so that I can find project information and discussions easily
- As a Stakeholder, I need weekly status updates so that I understand project progress and issues
- As a Consultant, I need session transcripts so that I can accurately capture requirements in BRDs

**BRD Requirements:**
- [REQUIREMENT] Use Microsoft Teams as primary communication platform (KBM joins GSI Teams) (ID: REQ-032, Type: Non-Functional) - ALIGNS
- [REQUIREMENT] Establish weekly status reporting cadence (ID: REQ-033, Type: Non-Functional) - ALIGNS
- [REQUIREMENT] Schedule working sessions at weekly to 3x per week cadence (to be determined) (ID: REQ-034, Type: Non-Functional) - ALIGNS
- [REQUIREMENT] Record all sessions with backup recording devices (ID: REQ-035, Type: Non-Functional) - ALIGNS
- [REQUIREMENT] Generate AI-assisted transcripts for all sessions to build BRDs (ID: REQ-036, Type: Non-Functional) - ALIGNS
- [REQUIREMENT] Implement change control process with change orders post-discovery scope lock (ID: REQ-037, Type: Non-Functional) - ALIGNS
- [PRIORITY] Must-Have
- [CONSTRAINT] Finance team unavailable during month-end closing

**Stakeholder Impact:**
- **Primary Users**: All project team members (GSI and KBM Hoag)
- **Approvers**: Executive sponsors for change orders
- **Impacted Parties**: All stakeholders receiving status updates

**Evidence:**
- "Communication Platform: Microsoft Teams (client will join GSI Teams) - Chat threads for ongoing communication - File sharing - Meeting coordination" - Transcript
- "Status Reporting: Weekly" - Transcript
- "Working Sessions: Weekly to 3x per week (cadence to be determined)" - Transcript
- "All sessions recorded - Multiple recording devices (backup pin recorder) - Transcripts generated for all sessions - AI-assisted documentation from transcripts" - Transcript
- "Project scope locked after discovery - Change orders required for new requirements - Impact on timeline documented - Client sign-off required" - Change control
- "Q1 typically slowest... Heavy meeting days: Tuesday-Thursday... Month-end: Finance team unavailable" - Business cycles

**Confidence Rating**: 97% - Comprehensive communication approach with clear tools, cadences, and business considerations

**Outstanding Items:**
- Finalize specific working session cadence
- Set up Microsoft Teams environment (action item)

---

### 8. GO-LIVE STRATEGY

#### 8.1 What is the go-live approach and transition strategy?

**Answer:**

**Go-Live Strategy: Soft Cutover (NOT Hard Cutover)**

**Soft Cutover Approach:**
- **Start new business in NetSuite on go-live date**
- **Run existing projects in Core until completion**
- **Typical dual-system period: ~6 months**
- **Phased project migration where possible**

**Rationale for Soft Cutover:**
- Reduces risk of disrupting in-flight projects
- Allows team to focus on learning NetSuite with new work
- Prevents need to migrate complex active projects mid-stream
- Natural transition as Core projects complete

**Support During Go-Live:**
- Go-live checklist provided
- On-site support option available
- Alternative: Microsoft Teams channel support
- Post go-live support included (30 days)

**User Stories:**
- As a Project Manager, I need to complete my in-flight projects in Core so that I'm not learning a new system mid-project
- As a Sales Rep, I need to start new opportunities in NetSuite so that we build clean data from day one
- As a Support Team Member, I need clear go-live support options so that we address issues quickly

**Current State Process:**
**PROCESS**: Anticipated Go-Live Transition  
**TRIGGER**: Go-live date reached  
**STEPS**:
1. Team starts all new business in NetSuite → new opportunities, quotes, orders begin in NetSuite
2. Team continues existing Core projects → completes projects already in progress in Core
3. Team phases project migration where possible → moves projects to NetSuite when logical breakpoints occur
4. Dual systems run for ~6 months → gradual wind-down of Core usage
5. Core fully retired when all projects complete → END
**SYSTEMS INVOLVED**: NetSuite (new), Core (legacy during transition)  
**PAIN POINTS**: Learning curve during transition; "Kleenex may be required"; different transaction numbering to adjust to

**BRD Requirements:**
- [REQUIREMENT] Execute soft cutover go-live strategy (not hard cutover) (ID: REQ-038, Type: Non-Functional) - ALIGNS
- [REQUIREMENT] Start new business in NetSuite on go-live date while completing existing projects in Core (ID: REQ-039, Type: Functional) - ADAPT
- [REQUIREMENT] Plan for ~6 month dual-system period during transition (ID: REQ-040, Type: Non-Functional) - ADAPT
- [REQUIREMENT] Migrate projects from Core to NetSuite in phases where possible (ID: REQ-041, Type: Functional) - ADAPT
- [REQUIREMENT] Provide on-site or Microsoft Teams channel support during go-live (ID: REQ-042, Type: Non-Functional) - ALIGNS
- [REQUIREMENT] Include 30 days post go-live support (ID: REQ-043, Type: Non-Functional) - ALIGNS
- [PRIORITY] Must-Have
- [RISK] Dual-system period complexity; user confusion between systems; data synchronization if needed
- [ASSUMPTION] 6 month dual-system period is adequate for existing project completion

**Stakeholder Impact:**
- **Primary Users**: All operational users managing transition
- **Secondary Users**: Finance team reconciling across systems
- **Approvers**: Executive team (Matt, Lorraine) for go-live readiness
- **Impacted Parties**: All end users, clients (minimal disruption intended)

**Evidence:**
- "Go-Live Strategy: Soft cutover recommended" - Transcript
- "Start new business in NetSuite on go-live date - Run existing projects in Core until completion" - Transcript
- "Typical dual-system period: ~6 months" - Transcript
- "Phased project migration where possible" - Transcript
- "On-site support option or Microsoft Teams channel support - Post go-live support (30 days included)" - Transcript
- "Different numbers for Opportunity, Proposal, Sales Order, Purchase Order - Team adjustment: 'Kleenex may be required'" - Concerns

**Confidence Rating**: 98% - Clear go-live strategy with explicit soft cutover approach and transition plan

**Outstanding Items:**
- Specific go-live date target (to be determined during implementation)
- Detailed dual-system operational procedures
- Project migration sequencing plan
- Cutover weekend activities checklist

---

### 9. POST-GO-LIVE SUPPORT & OPTIMIZATION

#### 9.1 What ongoing support will be available after go-live?

**Answer:**

**Included Post-Go-Live Support:**
- 30 days post go-live support included in implementation
- On-site or Microsoft Teams channel support options

**Ongoing Support Options (Maintain/Maximize Phase):**

**1. Suite Care Program**
- Ongoing support and optimization
- Managed services option
- Bank of hours option

**2. Self-Sufficiency Philosophy**
- Goal: Client self-sufficiency on the platform
- NetSuite Champions enable internal support
- Reduced dependency on consultants over time
- "You don't just go live, you thrive" approach

**User Stories:**
- As an Administrator, I need post-go-live support so that we resolve issues that arise in production
- As a Business Leader, I need ongoing optimization options so that we continuously improve our NetSuite usage
- As a Power User, I need to become self-sufficient so that we can make changes without consultant dependency

**BRD Requirements:**
- [REQUIREMENT] Include 30 days post go-live support (ID: REQ-043, Type: Non-Functional) - ALIGNS
- [REQUIREMENT] Establish Suite Care program for ongoing support and optimization (ID: REQ-044, Type: Non-Functional) - ALIGNS
- [REQUIREMENT] Enable client self-sufficiency on the platform as long-term goal (ID: REQ-045, Type: Non-Functional) - ALIGNS
- [PRIORITY] Must-Have (REQ-043); Should-Have (REQ-044, REQ-045)

**Stakeholder Impact:**
- **Primary Users**: NetSuite administrators, Power Users
- **Approvers**: Executive team for ongoing support contracts
- **Impacted Parties**: All users benefiting from optimization

**Evidence:**
- "Post go-live support (30 days included)" - Transcript
- "Suite Care program options - Managed services or bank of hours" - Maintain/Maximize phase
- "Philosophy: Client self-sufficiency on the platform" - Transcript
- "You don't just go live, you thrive" - Notable quote

**Confidence Rating**: 95% - Clear support structure documented with self-sufficiency goal

**Outstanding Items:**
- Specific Suite Care program selection and pricing
- Self-sufficiency timeline and milestones

---

### 10. PROJECT NUMBERING & TRANSACTION MANAGEMENT

#### 10.1 How will project numbering and transaction management work?

**Answer:**

**Project Numbering Approach:**
- **Consistent project number/name across all transaction types**
- Different transaction numbers for Opportunity, Proposal, Sales Order, Purchase Order (NetSuite standard)
- Project number remains consistent throughout lifecycle

**Transaction Flow:**
Opportunity (OPP-####) → Proposal/Quote (Q-####) → Sales Order (SO-####) → Purchase Order (PO-####)
- Each transaction type has its own numbering sequence
- Project number/name ties them all together
- All stages visible and linked

**Search & Access Capabilities:**
- Global search by project number, customer name, phone number
- Recent transaction dialog box (last 10-15 items)
- Click path relearning required from Core

**User Adjustment Expected:**
- "One thing people get tripped up on, but then it's not a big deal"
- Current state: Memorized order numbers
- Team adjustment: "Kleenex may be required"
- Resolution: Project number consistency provides continuity

**User Stories:**
- As a Sales Rep, I need to find my projects by project number so that I can access all related transactions
- As a Project Coordinator, I need to see all transaction stages linked so that I understand the full project lifecycle

**Current State Process:**
**PROCESS**: Transaction Access in Core  
**TRIGGER**: User needs to find a project or order  
**STEPS**:
1. User recalls order number from memory → searches in Core
2. User accesses order directly → views information
**SYSTEMS INVOLVED**: Core ERP  
**PAIN POINTS**: Memorized numbers won't work the same way; need to search by project instead

**BRD Requirements:**
- [REQUIREMENT] Establish consistent project number/naming across Opportunity → Proposal → Sales Order → PO (ID: REQ-046, Type: Functional) - ALIGNS
- [REQUIREMENT] Enable global search by project, customer name, phone number (ID: REQ-047, Type: Functional) - ALIGNS
- [REQUIREMENT] Configure recent transaction dialog for quick access to last 10-15 items (ID: REQ-048, Type: Functional) - ALIGNS
- [PRIORITY] Must-Have
- [RISK] User frustration during adjustment period from Core numbering to NetSuite approach
- [ASSUMPTION] Users will adapt to new numbering after initial learning curve

**Stakeholder Impact:**
- **Primary Users**: All users accessing transactions (sales, operations, finance)
- **Impacted Parties**: Entire organization adjusting to new search methods

**Evidence:**
- "Project numbering convention to be established (opportunity, proposal, sales order prefixes)" - Decisions
- "Project number consistent across all transactions" - Transcript
- "Different numbers for Opportunity, Proposal, Sales Order, Purchase Order - Current state: Memorized order numbers - Team adjustment: 'Kleenex may be required'" - Concerns
- "Global search capabilities (by project, customer name, phone number) - Recent transaction dialog box (last 10-15 items)" - Features
- "One thing people get tripped up on, but then it's not a big deal" - Reassurance

**Confidence Rating**: 96% - Clear numbering approach with acknowledged adjustment period

**Outstanding Items:**
- Specific numbering prefix conventions to be finalized (action item)

---

### 11. RISK MANAGEMENT & MITIGATION

#### 11.1 What are the identified project risks and mitigation strategies?

**Answer:**

**Discovery Risks & Mitigation:**

**Risk**: Inadequate Discovery  
**Mitigation**: Structured approach with deep analysis, validation focus vs traditional discovery

**Risk**: Unclear Requirements  
**Mitigation**: Multiple passes, same questions asked different ways, comprehensive questioning

**Risk**: Missed Requirements  
**Mitigation**: Transcript analysis, AI-assisted documentation, comprehensive BRD process

**Scope Risks & Mitigation:**

**Risk**: Scope Creep  
**Mitigation**: Change order process, discipline preached, scope lock after discovery

**Risk**: Organizational Challenges  
**Mitigation**: Executive sponsorship, change management focus, Kimmy as Change Management Lead

**Risk**: Competing Priorities  
**Mitigation**: Flexible scheduling, understanding business cycles (Q1 slower, month-end closings)

**Technical/Process Risks & Mitigation:**

**Risk**: Underestimated Data Migration  
**Mitigation**: Dedicated migration strategy document, SQL backend access, Joe Keller's extraction tool

**Risk**: Integration Failures  
**Mitigation**: Experienced integration lead (if needed), proven Orion integration platform

**Risk**: Inadequate Testing  
**Mitigation**: Dedicated UAT phase, no rushing, quality checkpoints

**Risk**: Poor Training  
**Mitigation**: Multiple formats (live, recorded, written), user guides, NetSuite Champions, leverage existing training culture

**User Adoption Risks & Mitigation:**

**Risk**: Learning Curve / Change Resistance  
**Mitigation**: "It's going to get uncomfortable, we have Kleenex" - acknowledged with support plan
- Matt's philosophy: "Meet the system at every moment we can" - willingness to adapt
- NetSuite Champions for peer support
- Multi-format training
- 30 days post go-live support

**Risk**: Historical Data Access Frustration  
**Mitigation**: Archive system design, user training on new access methods, "mourning process" acknowledged

**BRD Requirements:**
- [RISK] Inadequate discovery leading to missed requirements
- [RISK] Scope creep during implementation
- [RISK] Data migration complexity and accuracy
- [RISK] Integration failures with third-party systems
- [RISK] User adoption and change resistance
- [RISK] Historical data access adjustment period
- [PRIORITY] All mitigations are Must-Have

**Stakeholder Impact:**
- **Primary Users**: Project team managing risks
- **Approvers**: Executive sponsors for risk decisions
- **Impacted Parties**: All users affected by risk mitigation strategies

**Evidence:**
- "Discovery Risks: Inadequate Discovery → Structured approach with deep analysis" - Transcript
- "Scope Risks: Scope Creep → Change order process, discipline preached" - Transcript
- "Technical/Process Risks: Underestimated Data Migration → Dedicated migration strategy document" - Transcript
- "It's going to get uncomfortable, we have Kleenex" - Matt's acknowledgment
- "Meet the system at every moment we can - Not creating a new Core - Accept discomfort and change" - Philosophy
- Partnership approach: "It takes two parties to make this successful"

**Confidence Rating**: 94% - Comprehensive risk identification with clear mitigation strategies

---

### 12. SUCCESS FACTORS

#### 12.1 What are the critical success factors for this implementation?

**Answer:**

**Client Responsibilities:**

**1. Change Management Leadership**
- Strong executive sponsorship (Matt)
- Internal champions identified
- User adoption strategy (Kimmy leading)
- Department-specific communication approaches

**2. Project Management**
- Dedicated internal PM resources (Lorraine as Program Manager)
- Task and to-do management
- Scheduling coordination
- Timely decision-making

**3. NetSuite Champions/Power Users**
- Enthusiastic team members
- Prior NetSuite experience (when available)
- Training investment
- Peer support capability

**4. Stakeholder Availability**
- Quick decision-making
- Meeting participation
- Subject matter expert engagement
- Avoiding competing priorities

**GSI Responsibilities:**

**1. Structured Implementation Methodology**
- Strong project management (Tom Shannon, PMO Lead)
- Clear communication
- Comprehensive training process
- Proven framework (DREAM)

**2. Quality Assurance**
- Rigorous testing
- UAT coordination
- Quality checkpoints

**Partnership Approach:**
"It takes two parties to make this successful" - mutual commitment required

**Client Philosophy & Mindset:**
- "Meet the system at every moment we can" - willingness to adapt
- "Not creating a new Core" - embrace change vs replicating old system
- "It's going to get uncomfortable, we have Kleenex" - acknowledge challenges with confidence in recovery
- "Kleenex may be required, but we'll wipe our tears quickly" - resilience

**User Stories:**
- As an Executive Sponsor (Matt), I need to demonstrate commitment to change so that the organization follows our lead
- As a Change Management Lead (Kimmy), I need to identify and empower champions so that users support each other
- As a Project Manager (Lorraine), I need to coordinate resources and decisions so that the project stays on track
- As a GSI Consultant, I need to deliver structured methodology so that the client has confidence in the process

**BRD Requirements:**
- [REQUIREMENT] Establish strong executive sponsorship and change management leadership (ID: REQ-001, REQ-003, Type: Non-Functional)
- [REQUIREMENT] Dedicate internal PM resources for coordination (ID: REQ-002, Type: Non-Functional)
- [REQUIREMENT] Identify and empower NetSuite Champions (ID: REQ-029, Type: Non-Functional)
- [REQUIREMENT] Follow structured DREAM methodology (ID: REQ-005, Type: Non-Functional)
- [PRIORITY] Must-Have
- [ASSUMPTION] Both parties will fulfill partnership commitments
- [CONSTRAINT] Success depends on stakeholder availability and timely decision-making

**Stakeholder Impact:**
- **Primary Users**: Executive sponsors, program/change management leads, NetSuite Champions
- **Approvers**: Executive team for strategic decisions
- **Impacted Parties**: All project participants and end users

**Evidence:**
- "Client Responsibilities: 1. Change Management Leadership - Strong executive sponsorship - Internal champions identified" - Transcript
- "GSI Responsibilities: 1. Structured Implementation Methodology - Strong project management - Proven framework (DREAM)" - Transcript
- "Partnership Approach: 'It takes two parties to make this successful'" - Transcript
- "Meet the system at every moment we can - Not creating a new Core - Accept discomfort and change" - Matt's philosophy
- "It's going to get uncomfortable, we have Kleenex - Quick recovery expected - Kleenex may be required, but we'll wipe our tears quickly" - Team mindset

**Confidence Rating**: 98% - Comprehensive success factors with clear ownership and partnership approach

---

## OUTSTANDING ITEMS SUMMARY

### High Priority Outstanding Items
1. **Chart of Accounts Mapping Session** - Need detailed session with Lorraine and Kevin to map and reduce from 40+ pages to few hundred accounts (REQ-012, REQ-013)
2. **Data Migration Planning Session** - Determine Hoag workspace timeframe, detailed extraction process, archive system design (REQ-016, REQ-017, REQ-050)
3. **Platform Selection Decisions** - Payroll/HR (Paylocity vs alternative), Expense Management (Expensify vs alternative), File Storage (Google Drive vs SharePoint) (REQ-023, REQ-024, REQ-025)

### Medium Priority Outstanding Items
4. **Integration Architecture Review** - Finalize integration approach for selected platforms and manufacturer outreach strategy (REQ-026)
5. **Go-Live Planning Workshop** - Define specific go-live date, dual-system procedures, project migration sequencing (REQ-038-REQ-043)
6. **NetSuite Champions Identification** - Identify power users by department for enhanced training (REQ-029)
7. **User Role Mapping** - Map KBM Hoag users to 25+ Orion custom roles (REQ-010)
8. **Asana Evaluation** - Determine continuation or elimination (referenced in systems to be replaced)

### Action Items Requiring Completion
9. **Document Templates** - Kip to provide all templates (proposals, invoices, vendor-facing documents)
10. **XML Import Templates** - Matt to provide examples
11. **Approval Workflow Rules** - Shannon to provide complete list
12. **Order Type List** - Lorraine to confirm
13. **Discovery Session Attendees** - Team to review and confirm
14. **Microsoft Teams Setup** - Immediate setup needed for communication
15. **Project Numbering Convention** - Finalize specific prefix structure

### Information Gaps
16. **Hoag Workspace History** - Timeframe for historical data import (Lorraine decision needed)
17. **Specific User Role Assignments** - Which users get which of the 25+ custom roles
18. **Historical Data Access Training** - How users will be trained on archive system access
19. **Manufacturer Integration Priority** - Which non-Miller Knoll manufacturers are highest priority
20. **Suite Care Program Selection** - Which post-go-live support option will be chosen

---

## PROCESS AREA SUMMARY

**System Setup and Configuration** encompasses the foundational elements of the NetSuite Orion implementation:

**Key Themes:**
1. **Structured Methodology**: DREAM framework provides clear roadmap
2. **Partnership Approach**: Mutual commitment between GSI and KBM Hoag
3. **Orion Platform**: 95% pre-built solution minimizing customization
4. **Soft Cutover Strategy**: Risk-managed go-live with dual-system period
5. **Self-Sufficiency Goal**: Long-term client independence on platform
6. **Change Management Focus**: Acknowledged discomfort with structured support

**Implementation Approach Balance:**
- **ALIGNS**: 35 requirements (70%) - Leveraging Orion pre-built capabilities
- **ADAPT**: 11 requirements (22%) - Process changes needed for NetSuite
- **ACCOMMODATE**: 4 requirements (8%) - Custom solutions required

**Critical Success Dependencies:**
1. Chart of accounts as first configuration step
2. Executive sponsorship and change management leadership
3. NetSuite Champions for peer support
4. Comprehensive multi-format training
5. Timely stakeholder decisions
6. Quality data migration execution

**Notable Quotes:**
- "It's better to have too much data than to omit anything"
- "We're not creating a new Core"
- "Kleenex may be required, but we'll wipe our tears quickly"
- "It takes two parties to make this successful"
- "You don't just go live, you thrive"
- "Meet the system at every moment we can"

---

*End of Questionnaire - System Setup and Configuration v1.0*




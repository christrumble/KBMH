# Proposed Follow-Up Discovery Sessions - KBMH Project

## Executive Summary

Based on the comprehensive analysis of questionnaires and requirements maps across all 8 business process areas, this document proposes **29 follow-up discovery sessions** to complete the Discovery phase of the NetSuite/Orion implementation. These sessions address outstanding requirements, clarify implementation approaches, and validate critical decisions before moving to the Realize phase.

**Update:** Financial Management expanded from 3 to 8 sessions based on detailed requirements analysis. High-priority sessions identified for Revenue Recognition, Chart of Accounts Design, and Commission Structure require dedicated focus due to complexity and impact on implementation.

## Session Overview by Business Process Area

### 1. Business Intelligence & Reporting (3 Sessions)

#### Session 1.1: Dashboard Design & KPI Definition
- **Duration**: 2 hours
- **Participants**: Executive team, department heads, GSI BI consultant
- **Topics**:
  - Executive dashboard requirements and KPIs
  - Department-specific dashboard needs
  - Real-time vs. scheduled reporting preferences
  - Data visualization standards and branding
- **Outcomes**: Approved dashboard mockups, KPI definitions, reporting schedules

#### Session 1.2: SuiteQL & Advanced Analytics Requirements
- **Duration**: 1.5 hours
- **Participants**: Power users, department heads, GSI technical team
- **Topics**:
  - SuiteQL query requirements and complexity
  - Workbook Analytics training needs
  - Data export security and access controls
  - Integration with external analytics tools
- **Outcomes**: SuiteQL requirements document, training plan, security matrix

#### Session 1.3: Report Standardization & Change Management
- **Duration**: 1 hour
- **Participants**: All report users, change management team
- **Topics**:
  - Current report inventory and usage patterns
  - Report consolidation opportunities
  - User training and adoption strategy
  - Report ownership and maintenance procedures
- **Outcomes**: Report inventory, consolidation plan, training schedule

### 2. CRM (0 Additional Sessions)
- **Status**: Complete - All requirements captured and mapped
- **Note**: No additional discovery sessions needed based on comprehensive questionnaire analysis

### 3. Financial Management (8 Sessions)

**Note:** Detailed session outline available in `Financial Management\1 Instructions\Financial_Management_Follow-Up_Discovery_Session.md`

#### Session 3.1: Revenue Recognition Rules & Project Accounting (HIGH PRIORITY)
- **Duration**: 90 minutes
- **Participants**: Lorraine (CFO), Kipp, Marcus, Operations team
- **Topics**:
  - Revenue recognition timing for different order types
  - Special recognition scenarios (mockups, direct bill, intermarket, government, e-commerce)
  - Project-based revenue rules and cost recognition alignment
  - Compliance & audit requirements (ASC 606)
  - Reporting requirements for unbilled revenue, deferred revenue, backlog
- **Outcomes**: Detailed revenue recognition rules by order type, white paper review, implementation approach, testing plan
- **Why Critical**: Complex, compliance-critical; errors impact financials; dedicated session identified as high priority

#### Session 3.2: Chart of Accounts Design & Mapping Workshop (HIGH PRIORITY)
- **Duration**: 2 hours
- **Participants**: Lorraine, Celine, Kevin (GL), Implementation team
- **Topics**:
  - Current 40+ page COA analysis and consolidation strategy
  - Target "few hundred accounts" structure design
  - Account numbering scheme and parent/child hierarchy
  - Project vs. G&A cost structure in COA
  - 15% labor markup impact on COA (if continued)
  - Mapping strategy from old to new COA
- **Pre-Work Required**: Export current Core COA, identify top 50 accounts, list duplicates/rarely used
- **Outcomes**: Proposed NetSuite COA structure, mapping document, account numbering scheme, training requirements
- **Why Critical**: Foundational - impacts all transactions and reports; 40+ pages to few hundred is major change

#### Session 3.3: Commission Structure & GP Calculation Deep Dive (HIGH PRIORITY)
- **Duration**: 90 minutes
- **Participants**: Lorraine, Kipp, Matt/Mark (Leadership), Sales Leadership
- **Topics**:
  - **DECISION REQUIRED**: 15% labor markup - continue or eliminate? (Matt/Mark)
  - Commission calculation details (header vs. line level, splits, timing)
  - Project GP vs. Commissionable GP reporting requirements
  - Role-based visibility & security matrix
  - KPI dashboard requirements for both GP metrics
- **Outcomes**: 15% labor markup decision, commission rules documented, GP reporting specs, role permissions matrix
- **Why Critical**: Affects sales compensation; custom development required for dual GP reporting

#### Session 3.4: Period Close Process Optimization
- **Duration**: 60 minutes
- **Participants**: Lorraine, Celine, Kevin, Kipp, GSI consultant
- **Topics**:
  - Current 10-day Excel-based close process walkthrough
  - Reconciliation requirements and tolerances
  - Journal entry requirements during close (recurring, accruals, reversals)
  - NetSuite Period Close Checklist customization
  - Close timeline goals (target: reduce from 10 days)
  - Period locking & controls, AP/AR close vs. GL close
- **Outcomes**: Customized Period Close Checklist, task assignments, target timeline, close procedures
- **Why Important**: Current pain point - 10 days via Excel; goal is efficiency improvement

#### Session 3.5: Bill Payment & Cash Management Workflow Details
- **Duration**: 45 minutes
- **Participants**: Lorraine, Guada, Michael (AP), GSI consultant
- **Topics**:
  - Payment approval workflow details (Lorraine picks and chooses from $3M runs)
  - Remittance process (automatic vs. manual trigger)
  - Wire transfer handling (international wires)
  - Vendor prepayments process
  - Positive pay process with West Coast Community Bank
  - Payment exceptions & error handling
  - Cash flow management with Cache360 Dashboard
- **Outcomes**: Bill payment workflow fully defined, remittance process confirmed, cash flow requirements specified
- **Why Important**: Critical AP process with high dollar amounts; workflow details need clarification

#### Session 3.6: Expense Management System Decision & Project Coding
- **Duration**: 45 minutes
- **Participants**: Lorraine, Kipp, AP team, sample expense submitters, GSI consultant
- **Topics**:
  - **DECISION REQUIRED**: Expensify Suite App OR RAMP integration
  - Current pain points (manual process, user resistance: "Who likes to do expense reports?")
  - Project vs. G&A allocation requirements (COGS vs. G&A expenses)
  - Demo both options - evaluation criteria
  - Integration requirements (auto-sync, receipt flow, project coding fields)
  - Approval workflow and credit card integration
- **Pre-Work**: Schedule demos for both platforms
- **Outcomes**: Platform decision, project coding requirements documented, integration specs
- **Why Important**: Critical requirement for project cost accuracy; user experience affects adoption

#### Session 3.7: Fixed Asset Management Decision
- **Duration**: 30 minutes
- **Participants**: Lorraine, Celine/Kevin, GSI consultant
- **Topics**:
  - **DECISION REQUIRED**: NetSuite Fixed Asset module OR continue Bloomberg
  - Current Bloomberg functionality and costs
  - NetSuite FA module capabilities evaluation
  - Book vs. tax depreciation requirements
  - Migration of existing assets (if NetSuite FA chosen)
  - Cost-benefit analysis
- **Outcomes**: Platform decision, detailed requirements (if NetSuite FA), migration plan
- **Why Important**: Cost savings opportunity; system consolidation vs. functionality risk

#### Session 3.8: Vendor Credit Limit Tracking & Alerts
- **Duration**: 20 minutes
- **Participants**: Lorraine, Purchasing team, Shannon, GSI consultant
- **Topics**:
  - Current pain point: "Mad scramble at that nth hour" when hitting vendor limits
  - Warning threshold definition (suggested 90% of credit limit)
  - Alert recipients and mechanism (email, dashboard, PO blocking?)
  - Credit utilization calculation (open POs + unpaid bills vs. limit)
  - Process when approaching limit (expedite payment, request increase, defer orders)
- **Outcomes**: Threshold defined, alert mechanism specified, custom development requirements documented
- **Why Important**: Prevents unexpected order delays and vendor relationship issues

### 4. Marketing (2 Sessions)

#### Session 4.1: Marketing Automation & Integration Requirements
- **Duration**: 1.5 hours
- **Participants**: Marketing team, IT team, GSI marketing consultant
- **Topics**:
  - Email marketing platform integration
  - Lead scoring and nurturing workflows
  - Marketing analytics and ROI tracking
  - Google Drive integration requirements
- **Outcomes**: Marketing automation requirements, integration specifications

#### Session 4.2: RFP Management & Market Intelligence
- **Duration**: 1 hour
- **Participants**: Marketing team, Sales team, GSI consultant
- **Topics**:
  - RFP response workflow and templates
  - Market intelligence data sources and integration
  - Competitive analysis requirements
  - Event management and tracking
- **Outcomes**: RFP workflow design, market intelligence requirements

### 5. Operations (2 Sessions)

#### Session 5.1: Advanced Receiving & Vendor Center Configuration
- **Duration**: 2 hours
- **Participants**: Operations team, Vendor management, GSI operations consultant
- **Topics**:
  - Advanced receiving workflows and bin management
  - Vendor Center portal requirements and access
  - Contractor direct receiving processes
  - VRA (Vendor Return Authorization) workflows
- **Outcomes**: Receiving configuration, vendor portal design, VRA procedures

#### Session 5.2: Work Order Management & Field Service App
- **Duration**: 1.5 hours
- **Participants**: Operations team, Field service team, GSI consultant
- **Topics**:
  - Work order creation and management workflows
  - Field Service App requirements and customization
  - Time tracking and labor markup processes
  - Punch list and issue management
- **Outcomes**: Work order procedures, field app requirements, time tracking setup

### 6. Order Management (4 Sessions)

#### Session 6.1: Transaction Structure & Multi-Order Project Management
- **Duration**: 2 hours
- **Participants**: Sales team, Project managers, GSI consultant
- **Topics**:
  - Project numbering and transaction linking
  - Multi-order project management workflows
  - Customer PO tracking and management
  - Order splitting and consolidation rules
- **Outcomes**: Transaction structure design, project management procedures

#### Session 6.2: Quote Management & Smart Table Configuration
- **Duration**: 1.5 hours
- **Participants**: Sales team, Estimating team, GSI consultant
- **Topics**:
  - Quote template design and Smart Table configuration
  - SIF/XML import requirements and testing
  - Approval workflow design and routing
  - Commission management and calculation rules
- **Outcomes**: Quote templates, approval workflows, commission setup

#### Session 6.3: Tiered Pricing & Margin Management
- **Duration**: 1.5 hours
- **Participants**: Sales team, Finance team, GSI consultant
- **Topics**:
  - Tiered pricing structure and rules
  - Margin erosion prevention strategies
  - Pricing approval workflows
  - Customer-specific pricing management
- **Outcomes**: Pricing structure, margin controls, approval procedures

#### Session 6.4: Manufacturer Integrations & Tax Management
- **Duration**: 1 hour
- **Participants**: IT team, Sales team, GSI integration specialist
- **Topics**:
  - Miller Knoll integration requirements and testing
  - Coupa integration specifications
  - ServiceTime integration needs
  - Tax calculation and management workflows
- **Outcomes**: Integration requirements, tax configuration, testing procedures

### 7. Pre-Quote (4 Sessions)

#### Session 7.1: Labor Quote Request Engine & Workflow Design
- **Duration**: 2 hours
- **Participants**: Estimating team, Project managers, GSI consultant
- **Topics**:
  - Labor quote request types and categorization
  - Request engine configuration and automation
  - Union requirements and compliance
  - Quote acceptance and rejection workflows
- **Outcomes**: Request engine design, workflow procedures, union compliance

#### Session 7.2: Vendor Management & CAM Reservation System
- **Duration**: 1.5 hours
- **Participants**: Estimating team, Vendor management, GSI consultant
- **Topics**:
  - Vendor filtering and selection criteria
  - CAM reservation system requirements
  - Vendor communication and document management
  - Quote response tracking and management
- **Outcomes**: Vendor management procedures, CAM system requirements

#### Session 7.3: Project Request Form & Document Management
- **Duration**: 1 hour
- **Participants**: Estimating team, Project managers, GSI consultant
- **Topics**:
  - Project request form design and fields
  - Document attachment requirements and organization
  - RFQ form branding and customization
  - Long-term storage and retrieval procedures
- **Outcomes**: Request form design, document management procedures

#### Session 7.4: Estimating Process & Change Management
- **Duration**: 1 hour
- **Participants**: Estimating team, All stakeholders, GSI consultant
- **Topics**:
  - Current estimating process documentation
  - Process adaptation requirements for NetSuite
  - Change management and training needs
  - Missing documentation identification
- **Outcomes**: Process documentation, change management plan, training requirements

### 8. System Setup and Configuration (4 Sessions)

#### Session 8.1: Data Migration Strategy & Historical Data Access
- **Duration**: 2 hours
- **Participants**: IT team, Department heads, GSI data migration specialist
- **Topics**:
  - Historical data migration scope and priorities
  - Core system data extraction and mapping
  - Data validation and testing procedures
  - Historical data access requirements post-migration
- **Outcomes**: Migration strategy, data mapping, validation procedures

#### Session 8.2: Integration Requirements & Technical Architecture
- **Duration**: 1.5 hours
- **Participants**: IT team, Department heads, GSI technical architect
- **Topics**:
  - Third-party system integration requirements
  - API specifications and security requirements
  - Data synchronization and error handling
  - Integration testing and monitoring procedures
- **Outcomes**: Integration specifications, technical architecture, testing plan

#### Session 8.3: Training Strategy & User Adoption Planning
- **Duration**: 1.5 hours
- **Participants**: All department heads, Training team, GSI training specialist
- **Topics**:
  - Role-based training requirements and schedules
  - User adoption strategies and change management
  - Training environment setup and testing
  - Post-training support and optimization
- **Outcomes**: Training plan, adoption strategy, support procedures

#### Session 8.4: Go-Live Strategy & Project Governance
- **Duration**: 1 hour
- **Participants**: Executive team, Project managers, GSI project manager
- **Topics**:
  - Go-live approach and timeline validation
  - Project governance and decision-making processes
  - Risk management and mitigation strategies
  - Success criteria and measurement procedures
- **Outcomes**: Go-live plan, governance procedures, success metrics

## Session Prioritization & Dependencies

### Phase 1: Foundation Sessions (Weeks 1-2)
- System Setup and Configuration sessions (8.1-8.4)
- Data Migration Strategy (8.1)
- Integration Requirements (8.2)

### Phase 2: Core Process Sessions (Weeks 3-5)
- Financial Management HIGH PRIORITY sessions (3.1-3.3): Revenue Recognition, Chart of Accounts, Commission Structure
- Financial Management STANDARD sessions (3.4-3.8): Period Close, Bill Payment, Expense Mgmt, Fixed Assets, Vendor Limits
- Order Management sessions (6.1-6.4)
- Operations sessions (5.1-5.2)

### Phase 3: Specialized Process Sessions (Weeks 5-6)
- Pre-Quote sessions (7.1-7.4)
- Marketing sessions (4.1-4.2)
- Business Intelligence sessions (1.1-1.3)

### Phase 4: Validation & Finalization (Week 7)
- Cross-process integration validation
- Final requirements confirmation
- Solution design initiation

## Resource Requirements

### GSI Team Members Needed:
- Project Manager (all sessions)
- Technical Architect (sessions 8.2, 6.4, 3.2)
- Business Intelligence Consultant (sessions 1.1-1.3)
- Financial Management Consultant (sessions 3.1-3.3)
- Marketing Consultant (sessions 4.1-4.2)
- Operations Consultant (sessions 5.1-5.2)
- Order Management Consultant (sessions 6.1-6.3)
- Pre-Quote Consultant (sessions 7.1-7.4)
- Data Migration Specialist (session 8.1)
- Training Specialist (session 8.3)

### KBMH Team Members:
- Executive team (sessions 1.1, 8.4)
- Department heads (all sessions)
- Power users (sessions 1.2, 3.1-3.3, 6.1-6.4)
- IT team (sessions 8.1-8.2, 6.4, 3.2)

## Success Criteria

### Session Completion Criteria:
- All outstanding requirements identified and documented
- Implementation approaches confirmed (ALIGNS/ADAPT/ACCOMMODATE)
- Solution design requirements identified
- Dependencies and risks documented
- Action items assigned with owners and timelines

### Overall Discovery Phase Completion:
- All 8 Business Requirements Documents (BRDs) completed
- All solution design requirements identified
- Data migration strategy finalized
- Integration requirements documented
- Training and change management plans approved
- Go-live strategy confirmed

## Next Steps

1. **Schedule Sessions**: Coordinate with all stakeholders to schedule sessions according to prioritization
2. **Prepare Materials**: Create session agendas and pre-work materials
3. **Assign Resources**: Confirm GSI team member availability
4. **Set Expectations**: Communicate session objectives and outcomes to all participants
5. **Track Progress**: Monitor session completion and requirement capture
6. **Validate Completion**: Ensure all discovery requirements are met before Realize phase

## Estimated Timeline

- **Total Sessions**: 29 (updated from 24)
- **Estimated Duration**: 7-8 weeks
- **Total Hours**: 48.5 hours of discovery sessions
- **Completion Target**: End of Discovery phase, ready for Realize phase initiation

**Breakdown by Business Process Area:**
- Business Intelligence & Reporting: 3 sessions (4.5 hours)
- CRM: 0 sessions (complete)
- Financial Management: 8 sessions (8.5 hours) - **EXPANDED**
- Marketing: 2 sessions (2.5 hours)
- Operations: 2 sessions (3.5 hours)
- Order Management: 4 sessions (6 hours)
- Pre-Quote: 4 sessions (5.5 hours)
- System Setup and Configuration: 4 sessions (6 hours)
- Cross-Process Integration: 2 sessions (2 hours - from Project Governance)

---

*This document serves as the master plan for completing the Discovery phase of the KBMH NetSuite/Orion implementation project.*


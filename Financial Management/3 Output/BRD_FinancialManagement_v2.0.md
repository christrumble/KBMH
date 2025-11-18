# Business Requirements Document
## Solution Alignment & Validation

**Financial Management - Accounting, GL, AP, AR, Banking, Reporting & Period Close**

---

## Project Information

| Field | Value |
|-------|-------|
| **Implementation Name** | KB+Hoag Orion Implementation - Phase 1 |
| **Customer Name** | KB+Hoag |
| **Solution** | Orion/NetSuite Financial Management Suite |
| **Process Area** | Financial Management |
| **Document Owner** | Implementation Consultant |
| **Document Date** | November 18, 2025 |

### Document Version History

| Revision | Date | Author | Summary |
|----------|------|--------|---------|
| 1.0 | November 13, 2025 | Implementation Team | Initial BRD based on discovery findings, questionnaire v1.0, and requirements map v1.0 |
| 2.0 | November 18, 2025 | Implementation Team | **ENHANCED** - Updated with questionnaire v1.1 and requirements map v1.1 enhancements: added 8-session discovery framework, critical decision points, implementation complexity analysis, risk mitigation strategies, and stakeholder dependencies |

---

## Document Change Summary (v1.0 → v2.0)

### What's New in v2.0

This updated BRD incorporates significant enhancements from the discovery process:

1. **Follow-Up Discovery Framework**: 8 critical discovery sessions identified with specific participants, pre-work requirements, and deliverables
2. **Critical Decision Gates**: Three strategic decisions pending that will impact scope and approach:
   - REQ-023: Continue 15% labor markup or eliminate?
   - REQ-035: Define revenue recognition rules (compliance-critical)
   - REQ-016: Chart of Accounts consolidation (foundational)
3. **Implementation Complexity Matrix**: Each requirement now includes complexity assessment and specific risk mitigation strategies
4. **Stakeholder Role Clarity**: Decision makers, timelines, and approval authorities clearly identified
5. **Integration Dependencies**: Detailed mapping of platform integrations with status and decision points
6. **High-Risk Requirements**: Specific mitigation strategies for critical compliance and operational items

### Key Enhancements by Section

- **Tax Management**: Updated compliance risk mitigation and certificate management workflow
- **Period Close**: Added optimization opportunity analysis with SESSION 4 dependency
- **Expense Management**: Two platform options (Expensify vs. RAMP) with SESSION 6 decision required
- **Project Accounting**: Two GP metrics (Project GP vs. Commissionable GP) with role-based visibility requirements
- **Vendor Management**: New REQ-034 for vendor credit limit alerts with custom development scope
- **Financial Reporting**: Enhanced dashboard requirements with KPI specification

---

## Executive Summary

KB+Hoag, formed through the merger of KB and Hoag operations, requires a modern, integrated financial management solution to replace their current system built on NetSuite Core. The organization currently operates with significant manual processes, a large and unwieldy chart of accounts (40+ pages), and a 10-day accounting close cycle that relies on Excel-based workflows.

The proven Orion/NetSuite Financial Management solution directly addresses these operational challenges by providing:

- **Integrated financial management** across accounting, banking, accounts payable/receivable, and reporting
- **Automated processes** that eliminate manual steps in payment processing, expense management, and financial reporting
- **Real-time visibility** into project profitability, cash flow, and financial metrics through consolidated dashboards
- **Streamlined period close** with guided checklists and automated processes, reducing close time from 10 days to an estimated 5-7 days
- **Proven capabilities** used by similar furniture dealerships to manage complex project-based accounting

**Implementation Status**: The organization has completed comprehensive discovery sessions identifying 38 specific requirements. Of these:
- **26 requirements (68%)** align with standard Orion/NetSuite functionality
- **9 requirements (24%)** require business process adaptation
- **3-5 requirements (16%)** will need custom solution design (pending strategic decisions)

**Critical Path Items**: Eight follow-up discovery sessions have been identified to finalize requirements before configuration. Three strategic decisions must be completed before detailed design can proceed, as they will significantly impact scope, custom development needs, and implementation timeline.

---

## Strategic Overview & Key Decisions

### Three Critical Decision Gates

Before proceeding to detailed design and configuration, three strategic decisions must be finalized by leadership:

#### **DECISION 1: Revenue Recognition Rules (REQ-035) - COMPLIANCE-CRITICAL**
- **Decision Maker**: Lorraine (CFO/Controller), Kipp, Marcus (Implementation Team)
- **Timeline**: BEFORE DETAILED DESIGN PHASE
- **Impact**: HIGH - Compliance risk if not properly documented; affects financial statement accuracy
- **Session Required**: SESSION 1 (1-2 hours) 
- **Pre-Work Needed**:
  - Review revenue recognition white paper (referenced in discovery)
  - Document special order type scenarios (mockup, direct bill, government, E-commerce)
  - Determine ASC 606 compliance requirements
  - Engage external auditor if needed
- **Implementation Complexity**: HIGH - May require custom solution design for special scenarios
- **Outstanding Questions**:
  - When does revenue recognize - at Sales Order creation or Invoice?
  - Do different order types require different recognition rules?
  - What scenarios need special handling?
  - Are unbilled revenue and deferred revenue tracking needed?

#### **DECISION 2: 15% Labor Markup Continuation (REQ-023) - HIGH IMPACT**
- **Decision Maker**: Matt/Mark (Leadership)
- **Timeline**: BEFORE CONFIGURATION PHASE
- **Impact**: HIGH - Affects sales compensation structure, commission calculations, and custom development scope
- **Session Required**: SESSION 3 (1-2 hours)
- **Key Considerations**:
  - If CONTINUE: May require custom script development for automated calculation
  - If ELIMINATE: Must communicate impact to sales team; may affect commission structure
  - Either decision impacts Project GP vs. Commissionable GP reporting (REQ-024/025)
- **Implementation Complexity**: MODERATE-HIGH if continuing; affects REQ-024, REQ-025, REQ-038
- **Dependent Requirements**: REQ-024 (Project GP vs. Commissionable GP), REQ-025 (Role-based permissions), REQ-038 (KPI dashboards)

#### **DECISION 3: Chart of Accounts Consolidation (REQ-016) - FOUNDATIONAL**
- **Decision Maker**: Lorraine (CFO/Controller), Celine, Kevin (GL team)
- **Timeline**: URGENT - BEFORE DATA MIGRATION PLANNING
- **Impact**: CRITICAL - Foundational to all transactions; impacts all reports and user workflows
- **Session Required**: SESSION 2 (2-3 hours)
- **Pre-Work Required**:
  - Export complete Core COA (40+ pages) with GL numbers, descriptions, usage frequency
  - Identify top 50 most-used accounts
  - List any known duplicate accounts
  - Assess user reliance on current account numbers (many memorized?)
- **Implementation Complexity**: CRITICAL - Massive change affecting all transactions
- **Outstanding Questions**:
  - What is realistic target account count? (200? 300? 500?)
  - Can project-level segmentation reduce account proliferation?
  - Are any accounts duplicates across KB and Hoag workspaces?
  - What impact on historical reporting?

### Additional Pending Decisions (Medium Priority)

| Decision | REQ-ID | Decision Maker | Timeline | Impact |
|----------|--------|---|----------|--------|
| Expense Platform: Expensify vs. RAMP | REQ-013/014 | Lorraine | Before configuration | Medium - User adoption impact; platform capabilities differ |
| Fixed Asset Management: NetSuite FA vs. Bloomberg | REQ-026 | Lorraine/Marcus | Before implementation | Medium - Cost/benefit analysis; migration complexity |
| Automated Allocations Implementation | REQ-019 | Matt/Mark | Before configuration | Medium - P&L reporting impact; optional feature |
| Payroll Provider Continuation | REQ-027/028 | Lorraine/HR | Before implementation | Medium - Integration approach remains similar |

---

## Follow-Up Discovery Sessions Required

### CRITICAL/URGENT Sessions (Must Complete Before Configuration)

#### **SESSION 1: Revenue Recognition Rules & Project Accounting** [HIGH PRIORITY]
- **Duration**: 1-2 hours
- **Participants Needed**: Lorraine, Kipp, Marcus, possibly external auditor
- **Decision Authority**: Lorraine, Marcus
- **Key Questions to Address**:
  - When does revenue recognize for different order types?
  - What are the special scenarios requiring different recognition rules? (mockup, direct bill, government, E-commerce)
  - How does project-based revenue recognition work?
  - Review revenue recognition white paper details
  - ASC 606 compliance requirements?
  - Unbilled revenue and deferred revenue tracking needed?
- **Related REQ Items**: REQ-035 (ACCOMMODATE), REQ-036 (ALIGNS)
- **Deliverables**: 
  - Detailed revenue recognition rules by order type
  - Special scenario handling procedures
  - White paper review and validation
  - Implementation approach confirmation
  - Testing and validation plan
- **Outstanding Items**:
  - [ ] Detailed revenue recognition rules documented
  - [ ] Special scenario handling procedures defined
  - [ ] White paper review and validation completed
  - [ ] Implementation approach confirmation
  - [ ] Testing and validation plan for recognition rules

#### **SESSION 2: Chart of Accounts Design & Mapping** [HIGH PRIORITY - FOUNDATIONAL]
- **Duration**: 2-3 hours
- **Participants Needed**: Lorraine, Celine, Kevin, Implementation Team
- **Decision Authority**: Lorraine, Celine, Kevin
- **Key Questions to Address**:
  - What accounts are duplicates or rarely used in current 40+ page COA?
  - How can we use Classes/Departments/Projects instead of account proliferation?
  - Revenue accounts - how many true categories needed?
  - COGS accounts - project vs. general structure?
  - 15% labor markup impact on COA if continuing? (Dependent on REQ-023 decision)
  - Historical data migration impact on trend reporting?
- **Related REQ Items**: REQ-016 (ACCOMMODATE)
- **Pre-Work Required**:
  - Export complete Core COA with GL account numbers, descriptions, usage frequency
  - Identify top 50 most-used accounts
  - List any known duplicates across KB and Hoag workspaces
- **Deliverables**:
  - Current Core COA analyzed
  - Top 50 most-used accounts identified
  - Proposed NetSuite COA structure with account ranges
  - Mapping document from old to new COA
  - Account numbering scheme defined
  - User impact assessment and training plan
- **Timeline**: ASAP - Foundational to implementation

#### **SESSION 3: Commission Structure & GP Calculation** [HIGH PRIORITY - DECISION REQUIRED]
- **Duration**: 1-2 hours
- **Participants Needed**: Lorraine, Kipp, Matt, Mark, Sales Leadership
- **Decision Authority**: Matt/Mark (DECISION REQUIRED)
- **Key Decisions Required**:
  1. **DECISION**: Continue 15% labor markup in NetSuite or eliminate? (REQ-023)
  2. If continuing: Implementation approach (custom script vs. manual process)?
  3. If eliminating: Communication plan to sales team? Commission impact?
- **Key Questions Identified**:
  - Commission calculation details: % of commissionable GP? Header or line-level?
  - Commission splits between sales reps - how allocated?
  - When are commissions paid? (Booking, invoice, payment collection?)
  - Project GP vs. Commissionable GP reporting - who needs to see what?
  - Role-based visibility permissions - define specific access levels
  - Other load factors or markups to consider?
- **Related REQ Items**: REQ-023 (ADAPT), REQ-024 (ACCOMMODATE), REQ-025 (ACCOMMODATE), REQ-038 (ACCOMMODATE)
- **Deliverables**:
  - **DECISION**: 15% labor markup continues or is eliminated
  - Commission calculation rules fully documented
  - GP reporting and dashboard requirements specified
  - Role-based permissions matrix defined
  - KPI definitions for both GP metrics
  - Custom development scope defined if continuing markup
- **Implementation Complexity**: HIGH - Dependent on REQ-023 decision

#### **SESSION 4: Period Close Process Optimization** [HIGH PRIORITY]
- **Duration**: 1-2 hours
- **Participants Needed**: Lorraine, Celine, Kevin, AP Team
- **Decision Authority**: Lorraine, Celine, Kevin
- **Key Questions Identified**:
  - Current 10-day close process - detailed step-by-step walkthrough needed
  - Which steps take longest? (Reconciliations, JEs, reporting?)
  - Reconciliation requirements - frequency and timing?
  - Recurring JEs each period - standard list?
  - Close checklist customization - what specific steps required?
  - Who's responsible for each step? Approval gates?
  - Realistic target timeline for NetSuite? (5-7 days possible?)
- **Related REQ Items**: REQ-020 (ALIGNS), REQ-021 (ALIGNS), REQ-022 (ADAPT)
- **Deliverables**:
  - Detailed current state close process documented
  - NetSuite Period Close Checklist customized to KBM needs
  - Task assignments and approval gates defined
  - Target timeline established (realistic goal)
  - Close procedure documentation created
  - Training requirements identified
- **Optimization Opportunity**: Current 10-day close → target 5-7 days

#### **SESSION 5: Bill Payment & Cash Management Workflow** [HIGH PRIORITY]
- **Duration**: 1 hour
- **Participants Needed**: Lorraine, Guada, Michael, Marcus
- **Decision Authority**: Lorraine, Guada, Michael
- **Key Questions Identified**:
  - Payment approval workflow details - can Lorraine remove items in-system or communicate to AP?
  - Preferred workflow in NetSuite?
  - Remittance process - automatic or manual trigger? (Lorraine's concern: "If it said we sent it and we didn't...")
  - Wire transfer handling - supported in Advanced Electronic Bill Payments or manual?
  - Vendor prepayments - how many vendors require? Approval process?
  - Positive pay process with West Coast Community Bank?
  - Payment exceptions - failed ACH handling, retry process?
- **Related REQ Items**: REQ-008 (ALIGNS), REQ-009 (ALIGNS), REQ-010 (ADAPT), REQ-011 (ALIGNS), REQ-030 (ADAPT)
- **Deliverables**:
  - Bill payment approval workflow fully defined
  - Remittance process confirmed (automatic or manual)
  - Wire transfer handling approach determined
  - Positive pay process documented
  - Payment exception handling procedures defined
  - Cash flow management requirements specified
  - Vendor prepayment handling documented
- **High-Dollar Impact**: Payment runs sometimes reach $3M; approval process critical

### MEDIUM PRIORITY Sessions (Must Complete Before Detailed Design)

#### **SESSION 6: Expense Management System Decision** [MEDIUM PRIORITY - DECISION REQUIRED]
- **Duration**: 1.5-2 hours
- **Participants Needed**: Lorraine, AP Team, sample expense submitters
- **Decision Authority**: Lorraine
- **Key Decisions Required**:
  1. **DECISION REQUIRED**: Expensify Suite App OR RAMP for NetSuite integration?
  2. If RAMP: Change management plan for user transition from Expensify?
- **Key Questions Identified**:
  - Current pain points - how many reports monthly? Primary submitters?
  - Project vs. G&A allocation - how granular? Line-level or report-level coding?
  - Expensify Suite App - pros/cons? Can UX be improved enough?
  - RAMP option - "receipt capture from phone, boom, get assigned" - appeal to users?
  - Integration requirements - automatic sync, receipt attachment, project coding in mobile?
  - Approval workflow - manager approval before AP processing?
  - Credit card integration - corporate card auto-import capability needed?
- **Related REQ Items**: REQ-013 (ALIGNS), REQ-014 (ALIGNS), REQ-015 (ACCOMMODATE)
- **Deliverables**:
  - **DECISION**: Expensify Suite App OR RAMP selected
  - Project coding requirements fully documented
  - Approval workflow defined
  - Credit card reconciliation approach confirmed
  - Integration specifications for chosen platform
  - Change management plan (if switching to RAMP)
  - User training requirements identified
  - Cost comparison completed (Expensify vs. RAMP)

#### **SESSION 7: Fixed Asset Management Decision** [MEDIUM PRIORITY - DECISION REQUIRED]
- **Duration**: 45 minutes - 1 hour
- **Participants Needed**: Lorraine, Marcus, Implementation Team
- **Decision Authority**: Lorraine, Marcus
- **Key Decisions Required**:
  1. **DECISION REQUIRED**: NetSuite Fixed Asset module OR continue Bloomberg?
- **Key Questions Identified**:
  - Current Bloomberg usage - features actually being used?
  - NetSuite FA module capabilities - does it meet all Bloomberg needs?
  - Cost-benefit analysis - Bloomberg annual cost vs. NetSuite FA cost?
  - Migration complexity for existing assets?
  - Depreciation methods - straight-line, declining balance, MACRS, Section 179?
  - Book vs. tax depreciation - separate tracking needed?
  - Physical inventory/asset tagging requirements?
- **Related REQ Items**: REQ-026 (ADAPT)
- **Deliverables**:
  - **DECISION**: NetSuite Fixed Asset module OR continue Bloomberg
  - If NetSuite FA: Detailed requirements for module configuration
  - If NetSuite FA: Migration plan for existing assets
  - If continuing Bloomberg: Integration approach between Bloomberg and NetSuite
  - Cost-benefit analysis documented
  - Depreciation requirements fully specified
  - Implementation timeline confirmed

#### **SESSION 8: Vendor Credit Limit Tracking & Alerts** [MEDIUM PRIORITY - DECISION REQUIRED]
- **Duration**: 30-45 minutes
- **Participants Needed**: Lorraine, Purchasing Team, Shannon
- **Decision Authority**: Lorraine, Purchasing Team
- **Key Questions Identified**:
  - Frequency of hitting limits - how often "mad scramble at nth hour"?
  - Which vendors frequently-reached limits?
  - Impact of hitting limits - order delays, rush payments, vendor relationship issues?
  - Warning threshold preference - 90% of limit? Different for different vendors?
  - Alert mechanism - email, dashboard widget, hard PO block, or combination?
  - Credit utilization calculation - include open POs + unpaid bills vs. limit?
  - Vendor credit limit update process - who maintains? Frequency?
- **Related REQ Items**: REQ-034 (ACCOMMODATE)
- **Deliverables**:
  - Warning threshold defined (recommend: 90% of credit limit)
  - Alert recipients identified
  - Alert mechanism specified (email vs. dashboard vs. hard stop)
  - Credit utilization calculation defined
  - Custom development requirements documented
  - Process for handling warnings established
  - Vendor credit limit management workflow defined

---

## Financial Management Business Requirements

### Overview of Process Area

Financial management at KB+Hoag encompasses the complete accounting lifecycle: from transaction origination through accounts payable and accounts receivable management, to period-end closing, financial reporting, and compliance. The organization manages consolidated operations across merged KB and Hoag entities, requiring a single subsidiary structure with 13 accounting periods per year (non-standard configuration).

KB+Hoag's finance team is lean but highly skilled, including:
- **Lorraine** (CFO/Controller) - Strategic decision maker, process owner, change champion
- **Kipp** (Hybrid Finance/IT) - Technical bridge, systems integration, troubleshooting
- **Celine & Kevin** (GL Specialists) - Chart of accounts structure, period close management
- **Guada & Michael** (AP Team, "Dynamic Duo") - Payment processing, cash management
- **Shannon** (Product Coordinator Manager) - Vendor management, credit limit tracking

This team is **highly motivated for modernization**, having worked through the merger integration and understanding the limitations of their current system. The team has **prior exposure to modern accounting software** (Lorraine has used Blackline/Flowcast in previous roles) and is **realistic about implementation complexity**.

### Current State Challenges

**Current System Limitations:**
- **40+ page Chart of Accounts** - Unwieldy structure with significant redundancy; difficult to manage and report against
- **10-day Manual Period Close** - Excel-based process with manual reconciliations, JEs, and reporting; time-consuming and error-prone
- **Manual Payment Processing** - Requires staff to log into bank portal to upload payment files; extra step in ACH workflow (sometimes $3M payment runs)
- **No Automated Reversal Journal Entries** - Manual tracking of reversals, creating audit issues (abandoned in prior system due to tracking challenges)
- **Workaround Tax Processes** - SuiteTax "trick" workaround for use tax in Illinois/Missouri; non-standard approach
- **Manual Expense Reports** - No integrated expense management platform; data must be manually entered into GL; user resistance to expense submission
- **No Real-Time Reporting** - Financial reports generated manually; period-over-period analysis requires Excel consolidation
- **Third-Party Fixed Assets Tools** - Bloomberg usage for asset management; adds cost and system integration complexity
- **No Automated Vendor Credit Alerts** - Hitting vendor credit limits creates "mad scramble at the nth hour"; ordering delays and vendor relationship risk

**Stakeholder Pain Points:**
- **Lorraine**: "The 40+ page chart is unwieldy and difficult to manage"
- **Kipp**: "We had to create a workaround in Core because it wouldn't handle use tax natively"
- **Finance Team**: "Our 10-day close process is mostly Excel; there's definitely room for optimization"
- **Purchasing Team**: "We hit vendor credit limits unexpectedly and it creates a mad scramble at the nth hour"
- **Guada/Michael**: Processing large payment runs multiple times per week with manual approval workflows

---

## Business Requirements by Functional Area

### 1. Company Structure & Setup (Foundational)

#### Your Business Requirements

**REQ-001:** Configure single NetSuite subsidiary for consolidated KB+Hoag operations (ALIGNS)
- Single subsidiary for merged entity reflects streamlined organizational structure
- Evidence: "Single NetSuite subsidiary... KB + Hoag merged operations... Consolidated financial reporting" - Team
- Implementation Approach: Straightforward configuration; no customization required

**REQ-002:** Implement 13 accounting periods on calendar year basis (ADAPT)
- Non-standard configuration reflecting KB+Hoag's business cycle preference
- Evidence: "I would like 13. 13. Core only does 12. Okay. So it was, like, 13. Yep." - Lorraine
- Implementation Note: Users will need training on 13-period calendar vs. typical 12-period standard; decision made by Lorraine

**REQ-003:** Configure US Dollar as single currency (no multi-currency) (ALIGNS)
- Simplified approach appropriate for US-based operations
- Evidence: "We're all in U.S. dollar" - Team
- Implementation Approach: Standard configuration; no multi-currency complexity

#### Current State Process

KB+Hoag currently operates as a consolidated entity across merged KB and Hoag locations, managed within a single Core subsidiary. The company uses a calendar year with 13 periods (13 four-week periods instead of traditional monthly accounting). All transactions occur in US dollars with no international operations requiring multi-currency handling.

#### Orion/NetSuite Solution

Orion/NetSuite provides robust subsidiary configuration capabilities that align with KB+Hoag's consolidated, single-entity structure. The solution enables straightforward subsidiary setup for merged operations, maintaining clear separation of legal entities where needed while supporting consolidated financial reporting and KPI tracking across the combined organization.

NetSuite fully supports non-standard accounting calendars, including 13-period configurations. While 13 periods represents a departure from NetSuite's default 12-period calendar, this configuration is well-supported by the platform and allows KB+Hoag to continue its established business cycle without requiring workarounds or customization. Period management is centralized, and users access the same period structure across all modules, ensuring consistency.

Currency configuration in NetSuite is straightforward for USD-only operations. By configuring USD as the base currency with no multi-currency processing enabled, KB+Hoag simplifies transaction entry, eliminates currency conversion overhead, and maintains standard reporting processes.

#### Future State Process

At go-live, KB+Hoag's finance team will navigate to a simplified subsidiary structure with consolidated KB+Hoag operations managed within a single subsidiary. The 13-period calendar will be automatically applied across all financial modules—no manual period management required. All new transactions will default to USD, and the system will enforce this standard globally.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Complexity |
|--------|-------------|---------------------------|----------|-----------|
| REQ-001 | Single subsidiary for KB+Hoag | Subsidiary configuration and consolidation | ALIGNS | Low |
| REQ-002 | 13 accounting periods (non-standard) | Custom calendar support | ADAPT | Low |
| REQ-003 | US Dollar only (no multi-currency) | Currency setup and transaction defaults | ALIGNS | Low |

#### Implementation Approach

- Subsidiary configuration will be completed during initial setup phase
- 13-period calendar will be established during system configuration with full documentation
- Currency defaults will be applied globally across all modules
- No customization required for any of these foundational requirements

---

### 2. Tax Management (Compliance-Critical)

#### Your Business Requirements

**REQ-004:** Implement native SuiteTax for 48-state nexus management with automatic calculation (ALIGNS)
- Automatic tax calculation based on ship-to address across all nexus states
- Evidence: "48 states with nexus registration... Automatic calculation based on ship-to address... Native SuiteTax (not Avalara)" - Team
- Implementation Note: Native SuiteTax eliminates third-party Avalara dependency; significant advantage for compliance automation

**REQ-005:** Configure tax exemption certificate management with expiration tracking and dashboard (ALIGNS)
- Proactive certificate expiration monitoring prevents compliance violations
- Evidence: "Tax exemption certificate management... Effective date tracking... Dashboard for expiring certificates... Compliance reporting" - Discovery
- Strategic Benefit: Eliminates manual certificate tracking; reduces compliance risk

**REQ-006:** Configure SuiteTax for use tax handling in Illinois and Missouri (ALIGNS)
- Eliminates current "trick" workaround that has required non-standard Core configuration
- Evidence: "CORE won't do use tax, so we have to kind of trick it" - Kipp
- Strategic Benefit: Removes workaround dependency, improving system reliability and audit compliance

**REQ-007:** Enable gross receipts tax reporting by ship-to location (ALIGNS)
- Standard ship-to location reporting supports revenue aggregation by region
- Evidence: "We need the sales revenue number based on ship to location... standard way of calculating it" - Kipp/Marcus

#### Current State Process

KB+Hoag currently manages tax compliance across 48 states with nexus registration. Tax calculation is complex, requiring manual verification across multiple state jurisdictions. Use tax handling in Illinois and Missouri requires a workaround in Core that was not natively supported. Tax exemption certificates are tracked, but expiration monitoring is manual, creating compliance risk. Gross receipts tax reporting requires manual consolidation by ship-to location.

#### Orion/NetSuite Solution

Orion/NetSuite delivers comprehensive tax management through native SuiteTax integration, which automatically calculates sales tax for all 48 states where KB+Hoag has nexus. SuiteTax determines applicable tax rates and rules based on ship-to addresses, transaction types, and customer tax status—all without manual intervention. This eliminates the need for Avalara or other third-party tax engines and ensures consistency across all transactions.

Use tax handling in Illinois and Missouri is fully supported through SuiteTax, eliminating the workaround currently required in Core. NetSuite's native approach ensures proper tax treatment for these jurisdictions while maintaining audit compliance.

Tax exemption certificates are managed within SuiteTax with automatic expiration tracking and dashboard alerts. When certificates approach expiration, the dashboard flags them for renewal, preventing accidental tax charging on exempt transactions. The system maintains a complete audit trail of certificate updates and renewals for compliance reporting.

Gross receipts tax reporting integrates directly with transaction data, automatically aggregating revenue by ship-to location without manual consolidation. Standard NetSuite reports provide this view natively, supporting both compliance reporting and business intelligence analysis.

#### Future State Process

KB+Hoag's finance team will maintain tax compliance through automated SuiteTax processing. Tax rates are automatically determined by NetSuite based on ship-to addresses and transaction types. Tax exemption certificates are uploaded to the system and tracked automatically with dashboard alerts 30 days before expiration. Finance staff review the expiration dashboard monthly to identify certificates requiring renewal. Use tax for IL/MO is calculated automatically without requiring manual workarounds. At month-end, the team runs standard SuiteTax reports organized by ship-to location for state filings and analysis.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Complexity | Risk |
|--------|-------------|---------------------------|----------|-----------|------|
| REQ-004 | 48-state nexus tax management | Native SuiteTax with automatic calculation | ALIGNS | Low | Low - Well-established feature |
| REQ-005 | Tax exemption certificate management | SuiteTax dashboard with expiration tracking | ALIGNS | Low | Low - Standard feature |
| REQ-006 | Use tax handling (IL/MO) | Native SuiteTax support | ALIGNS | Low | Medium - Compliance validation needed |
| REQ-007 | Gross receipts reporting by ship-to | SuiteTax reporting with location aggregation | ALIGNS | Low | Low - Standard report |

#### Implementation Approach

- SuiteTax will be configured during system setup phase with all 48-state nexus definitions
- Tax rates, rules, and exemption rules will be configured before data migration
- Certificate management dashboard will be set up and tested before go-live
- Finance team will receive training on certificate renewal process and dashboard monitoring
- IL/MO use tax configuration will be validated with external accountant if needed for compliance verification

#### Implementation Considerations

- SuiteTax configuration complexity; ongoing compliance maintenance
- Nexus configuration must be reviewed annually as nexus definitions change
- Certificate upload process requires digital certificates or scanned copies
- TaxConnect dependency (REQ-006) is being eliminated with SuiteTax native support
- Report templates may require customization for state filing requirements

---

### 3. Banking & Cash Management

#### Your Business Requirements

**REQ-008:** Implement bank feeds integration with West Coast Community Bank (ALIGNS)
- Auto-import transactions, auto-matching eliminates manual data entry
- Evidence: "West Coast Community Bank... Confirmed as part of NetSuite Bank Feeds program... Automatic transaction feed into NetSuite" - Team
- Integration Status: CONFIRMED - Bank is part of NetSuite Bank Feeds program
- Session Dependency: SESSION 5 for positive pay process confirmation

**REQ-009:** Enable Advanced Electronic Bill Payments for ACH directly from NetSuite (ALIGNS)
- ACH from NetSuite eliminates manual bank portal upload step
- Evidence: "Advanced Electronic Bill Payments (part of edition)... Pay via ACH directly from NetSuite... Skip manual bank portal upload step" - Marcus
- High-Dollar Impact: Payment runs sometimes reach $3M; process efficiency critical
- Session Dependency: SESSION 5 for workflow confirmation

**REQ-010:** Configure bill payment approval workflow with Lorraine as approver (ADAPT)
- Lorraine reviews Monday payment runs; sometimes $3M in transactions
- Evidence: "Guada or Michael compile proposed payment run... Bring to Lorraine with amounts... Lorraine reviews and approves" - Process description
- Outstanding Questions: Can Lorraine remove items in-system or does she communicate to AP? What's preferred approach?
- Session Dependency: SESSION 5 required for workflow clarification

**REQ-011:** Enable Cash360 Dashboard for cash flow forecasting (ALIGNS)
- Standard dashboard for cash flow forecasting and visibility
- Evidence: "Cache360 Dashboard... Cash flow forecasting functionality... Part of configured system" - Marcus
- Implementation Approach: Standard configuration; enables real-time cash visibility

**REQ-012:** Configure credit card reconciliation as bank account (upload statement, auto-match) (ALIGNS)
- Treats credit card like another bank account for consolidated reconciliation
- Evidence: "Treat credit card like another bank account... Upload statement (likely CSV)... Use same reconciliation process" - Marcus
- Outstanding Question: Statement import - CSV vs. live feed from ARC Bank?

#### Current State Process

KB+Hoag currently manages banking through manual processes. Bank reconciliation requires downloading transactions from West Coast Community Bank, manually entering them into accounting records, and verifying against the GL. Credit card reconciliation is handled separately. Bill payments are prepared by the AP team (Guada/Michael), compiled into payment runs, and brought to Lorraine for approval. Once approved, payment files are manually uploaded to the bank portal for processing. Cash flow visibility requires manual Excel consolidation from multiple bank statements.

#### Orion/NetSuite Solution

Orion/NetSuite provides comprehensive banking and cash management capabilities that automate KB+Hoag's current manual processes. Bank feeds integration with West Coast Community Bank automatically imports transactions into NetSuite, eliminating manual data entry and reducing errors. The system automatically matches downloaded transactions to existing bank deposits and checks, requiring minimal manual intervention.

Advanced Electronic Bill Payments enables KB+Hoag to process ACH payments directly from NetSuite. Payment runs prepared by the AP team are submitted through the system, Lorraine reviews and approves them within the system workflow, and payments are transmitted directly to West Coast Community Bank—eliminating the extra step of uploading files to the bank portal. This streamlines the approval process while maintaining complete audit trails.

Credit card reconciliation integrates seamlessly with bank feeds. By treating the credit card as another bank account, KB+Hoag can upload monthly statements via CSV import and use the same reconciliation workflow applied to bank accounts. Statement reconciliation becomes a standardized process across all bank-type accounts.

Cash360 Dashboard provides real-time visibility into cash flow by consolidating account balances, pending transactions, and forecasted cash positions. KB+Hoag can view cash flow projections at the company level, supporting better cash management decision-making.

#### Future State Process

At go-live, KB+Hoag's banking processes will become largely automated. West Coast Community Bank transactions flow automatically into NetSuite daily. The finance team reviews incoming transactions and applies matching rules; most transactions match automatically without manual intervention. Payment runs prepared by the AP team are submitted in the system for Lorraine's review and approval. Once Lorraine approves, payments transmit directly to the bank without additional manual steps. Monthly credit card statements are uploaded via CSV, reconciled using the same bank account reconciliation workflow, and cleared.

The finance team monitors the Cash360 Dashboard for cash flow forecasting and can run real-time reports on banking activity, eliminating Excel-based cash consolidation.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Complexity | Risk |
|--------|-------------|---------------------------|----------|-----------|------|
| REQ-008 | Bank feeds from West Coast Community Bank | NetSuite Bank Feeds Suite App | ALIGNS | Low | Low - Bank confirmed in program |
| REQ-009 | Advanced Electronic Bill Payments (ACH) | Advanced Electronic Bill Payments module | ALIGNS | Low | Medium - Testing required; vendor relationships |
| REQ-010 | Bill payment approval workflow (Lorraine approver) | Workflow automation | ADAPT | Medium | Medium - Workflow details to be confirmed in SESSION 5 |
| REQ-011 | Cash360 Dashboard for forecasting | Cash360 Dashboard module | ALIGNS | Low | Low - Standard feature |
| REQ-012 | Credit card reconciliation (CSV upload) | Bank reconciliation with CSV import | ALIGNS | Low | Low - Standard process |

#### Implementation Approach

- Bank Feeds will be configured during system setup; West Coast Community Bank will activate the feed
- Advanced Electronic Bill Payments will be configured; Coastal registration will be completed
- Bill payment approval workflow will be designed based on SESSION 5 requirements; workflow automation will be tested
- Cash360 Dashboard will be set up with standard metrics and forecasting parameters
- Credit card reconciliation will be tested with CSV import process; ARC Bank upload process will be confirmed

#### Implementation Considerations

- Bank integration setup; possible security review by IT
- Advanced Electronic Bill Payments requires vendor registration (Coastal) and testing
- Bill payment approval workflow details to be confirmed in SESSION 5; specifically, Lorraine's ability to remove items in-system vs. communicating changes to AP
- Remittance process must be confirmed - automatic vs. manual trigger for sending payment confirmations to vendors; Lorraine's concern: "If it said we sent it and we didn't..."
- Wire transfer handling for international payments needs clarification (REQ-030) - integrated or manual bank portal?
- Positive pay process with West Coast Community Bank must be documented
- Testing plan required for payment reconciliation and exception handling

---

### 4. Expense Management (User Adoption Focus)

#### Your Business Requirements

**REQ-013:** Evaluate and implement Expensify integration via Suite App (ALIGNS)
- Suite App available for automatic data sync from Expensify to NetSuite
- Evidence: "Expensify Integration (Suite App available)... Absolutely talk to each other. You can just sync data... Automated data sync from Expensify to NetSuite" - Discovery
- Session Dependency: SESSION 6 required for platform evaluation (Expensify vs. RAMP decision)
- Outstanding Decision: **PENDING** - Platform selection required

**REQ-014:** Evaluate RAMP as alternative to Expensify with NetSuite integration (ALIGNS)
- RAMP offers alternative to Expensify with improved mobile UX ("receipt capture from phone, boom, get assigned")
- Evidence: "Lorraine interested in moving from Expensify to RAMP... RAMP has NetSuite integration too... Could potentially demo both" - Discovery
- Session Dependency: SESSION 6 required for platform evaluation
- Change Management: If switching, transition plan and user training required
- Outstanding Decision: **PENDING** - Platform selection required

**REQ-015:** Support project vs. G&A allocation for expense reports (ACCOMMODATE)
- Project expenses must be coded to COGS; G&A expenses to general GL accounts
- Evidence: "We have two different... cost structure... create a cost to go into cost of goods sold, specifically identified as a project cost, and then we have general G&A-type stuff" - Lorraine
- Complexity: Requires careful integration with chosen platform (Expensify vs. RAMP); field mapping critical; line-level coding needs clarification
- Session Dependency: SESSION 6 for platform selection impacts this requirement

#### Current State Process

KB+Hoag currently uses Expensify for employee expense submissions. Expensify provides mobile and web interfaces for receipt capture and expense report entry. Reports are submitted to managers for approval. However, the connection to NetSuite is not fully integrated—expense data requires manual entry into the GL with project vs. G&A coding performed during GL entry.

#### Orion/NetSuite Solution

Orion/NetSuite provides integrated expense management through platform partnerships. Two options are available for evaluation in SESSION 6:

**Option A: Expensify Suite App**
Expensify Suite App provides automatic data synchronization between Expensify and NetSuite. Employees submit expense reports in Expensify, which are automatically synced to NetSuite for GL entry. The system maps expense categories to GL accounts, reducing manual entry and coding errors. For project vs. G&A allocation, expenses can be coded at the line level in Expensify or automatically mapped based on expense category during sync.

**Option B: RAMP with NetSuite Integration**
RAMP offers an alternative platform designed specifically for corporate expense management. RAMP's mobile interface emphasizes simplified receipt capture with phone photo submission ("receipt capture from phone, boom, get assigned"). RAMP has native NetSuite integration and can provide the same automatic sync capability as Expensify. RAMP may offer improved user experience compared to Expensify, potentially addressing user resistance to expense submission.

Both platforms support project coding and automatic GL account mapping, ensuring expenses are properly allocated to project COGS or general G&A accounts. The specific coding rules and field mapping will be finalized during SESSION 6 platform evaluation.

#### Future State Process

Once platform selection is finalized in SESSION 6, KB+Hoag's expense process will flow as follows:

Employees will submit expenses through the selected platform (Expensify or RAMP). Expenses will be coded at the time of submission, specifying project (COGS) or G&A (GL account) allocation. Managers will approve reports within the platform. Approved reports will automatically sync to NetSuite, with expenses appearing in the GL with proper account coding and project linkage. Finance team will review the GL entries during the period close process and verify that project expenses have been properly linked to the appropriate project.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Complexity | Status |
|--------|-------------|---------------------------|----------|-----------|--------|
| REQ-013 | Expensify integration | Expensify Suite App (auto-sync) | ALIGNS | Low-Medium | **DECISION PENDING** |
| REQ-014 | RAMP alternative | RAMP NetSuite integration | ALIGNS | Low-Medium | **DECISION PENDING** |
| REQ-015 | Project vs. G&A allocation | Field mapping + category rules | ACCOMMODATE | Medium | **Dependent on REQ-013/014 decision** |

#### Implementation Approach

- SESSION 6 will evaluate both Expensify and RAMP capabilities
- Demos will focus on project coding capability, approval workflow, and user experience
- Cost comparison will be performed (current Expensify cost vs. RAMP cost)
- Once platform selected, integration will be configured during system setup phase
- Field mapping will be finalized to support project vs. G&A coding rules
- Change management plan will be developed if switching from Expensify to RAMP

#### Implementation Considerations - CRITICAL

- **DECISION PENDING**: Expensify vs. RAMP platform selection (SESSION 6)
- User adoption risk: Current user resistance to expense submission may be addressed through improved UX (RAMP advantage)
- Project coding must support line-level detail - confirmation needed on field mapping capability in chosen platform
- If switching to RAMP: Change management plan required; user training on new interface; parallel running possible during transition
- Credit card integration: Does chosen platform support corporate card auto-import? Important for reducing manual expense entry
- Approval workflow: Confirm whether manager approval happens in platform or in NetSuite
- Testing required for auto-sync accuracy and project coding validation

---

### 5. Chart of Accounts & Data Migration (FOUNDATIONAL - CRITICAL PATH)

#### Your Business Requirements

**REQ-016:** Consolidate chart of accounts from 40+ pages to few hundred accounts (ACCOMMODATE)
- Current Core COA is extremely large (40+ pages); target is few hundred accounts
- Evidence: "40+ pages of accounts in Core... Unwieldy and difficult to manage... Target: Few hundred accounts (target reduction)" - Team discussion
- Complexity: **CRITICAL** - Foundational change affecting all transactions, reports, and user workflows
- Session Dependency: **SESSION 2 REQUIRED** - Major design effort needed before data migration planning
- Outstanding Questions:
  - What is realistic target account count? (200? 300? 500?)
  - Can project-level segmentation reduce account proliferation?
  - Are any accounts duplicates across KB and Hoag workspaces?
  - What's the impact on historical reporting?

**REQ-017:** Migrate historical financial data back to 2017 (trial balances, period-over-period) (ALIGNS)
- Historical data back to 2017 supports trend analysis and comparative reporting
- Evidence: "Back to 2017 (Lorraine's decision)... Historical data back to 2017... Older data exported and archived" - Team decision
- Dependent on: REQ-016 must be finalized first (data mapping between old and new COA)
- Outstanding Items: Data quality validation; SQL extraction approach from Core

#### Current State Process

KB+Hoag manages their current chart of accounts with 40+ pages of accounts in NetSuite Core. This unwieldy structure contains many duplicate accounts, rarely-used accounts, and significant redundancy. Users have memorized many account numbers for frequent transactions. Historical financial data is maintained in Core going back to 2017. At period close, finance teams must navigate this large account structure to find appropriate accounts for transactions and reconciliations.

#### Orion/NetSuite Solution

Orion/NetSuite enables KB+Hoag to consolidate and streamline its chart of accounts structure. The platform supports flexible account hierarchies and supplementary dimensions (Classes, Departments, Projects) that can reduce the need for account proliferation. 

Through SESSION 2 (Chart of Accounts Design & Mapping), the finance team will:
1. Analyze the current 40+ page structure to identify most-used vs. rarely-used accounts
2. Identify duplicate and redundant accounts
3. Consolidate the structure to a rationalized set of few hundred accounts
4. Design account hierarchies and supplementary dimensions to support business segmentation (by class, department, project)
5. Create a comprehensive mapping document from old accounts to new accounts
6. Develop a user reference guide showing changes and new structure

NetSuite's Project Record module (part of Orion) supports project-level financial tracking and KPI aggregation, enabling KB+Hoag to use a consolidated GL account structure while maintaining project-level detail through project linkage rather than account proliferation.

Historical financial data migration will occur once the new COA structure is finalized. Data from 2017 forward will be extracted from Core and mapped to the new account structure, preserving historical reporting capability.

#### Future State Process

At go-live, KB+Hoag will navigate a streamlined chart of accounts with few hundred accounts instead of 40+ pages. Accounts will be organized by logical business category (Assets, Liabilities, Revenue, COGS, Expenses, etc.). Project-level detail will be tracked through project linkage and the Project Record module rather than account proliferation. Finance team will have a comprehensive mapping guide showing old account numbers, new account numbers, and business purpose. Historical financial data will be available for period-over-period trend analysis and comparative reporting going back to 2017.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Complexity | Risk |
|--------|-------------|---------------------------|----------|-----------|------|
| REQ-016 | COA consolidation (40+ pages → few hundred) | Chart of accounts redesign + project linkage | ACCOMMODATE | **CRITICAL** | **CRITICAL** - Massive change, impacts all transactions |
| REQ-017 | Historical data migration (back to 2017) | GL data migration with COA mapping | ALIGNS | Medium | Medium - Data quality validation needed |

#### Implementation Approach - CRITICAL PATH

- **SESSION 2 MUST BE COMPLETED FIRST** - Chart of accounts design is foundational to implementation
- Pre-Session 2 work: Export complete Core COA, analyze usage patterns, identify duplicates
- During Session 2: Design new structure, create mapping document, develop user training materials
- Post-Session 2: Data migration approach planning, historical data extraction, mapping validation
- Testing: GL balances, historical reporting accuracy, transaction posting to correct new accounts

#### Implementation Considerations - HIGH IMPACT

- **This is the single biggest structural change in the implementation** - affects every transaction and user
- Users have memorized many account numbers - significant training and change management required
- Historical reporting must be validated to ensure period-over-period comparisons work correctly
- Multiple GL entries may need to be reclassified during transition if old structure is being significantly condensed
- Phase-out plan may be needed if users continue referring to old account numbers
- Impact on user efficiency during transition as users learn new account structure
- Comprehensive mapping reference guide will be essential
- Parallel COA management may be needed during cutover - running old and new structures in parallel for validation

---

### 6. Journal Entries & Allocations

#### Your Business Requirements

**REQ-018:** Enable CSV import of journal entries with automated reversal capability (ALIGNS)
- CSV import eliminates manual JE data entry; automated reversal solves prior tracking issues
- Evidence: "CSV import of journal entries... Payroll entries imported from Paylocity... Automated reversal journal entries" - Team
- Strategic Benefit: Reversal automation addresses known pain point - reversals were abandoned in prior system due to tracking challenges
- Integration: Paylocity integration provides monthly payroll entries via CSV

**REQ-019:** Determine if automated allocation transactions will be implemented (ADAPT)
- Optional feature; decision pending with leadership (Matt/Mark)
- Evidence: "Optional to implement... Decision pending with leadership... I don't know that he knows that he wants to, or doesn't..." - Discussion
- Complexity: If implemented, requires allocation rules definition; affects P&L reporting
- Session Dependency: SESSION 3 - decision on labor markup (REQ-023) may impact allocation requirements

#### Current State Process

KB+Hoag currently imports payroll journal entries from Paylocity via CSV export. These entries are manually entered into the GL. Reversal journal entries are manually created, and tracking of reversals has been problematic—the organization abandoned using reversals in the prior system due to audit tracking issues.

#### Orion/NetSuite Solution

Orion/NetSuite provides CSV import capability for journal entries, enabling direct import of Paylocity payroll data. The system can automatically create reversal journal entries on the first day of the next period, eliminating manual reversal creation and solving the tracking issues that forced KB+Hoag to abandon reversals in the past system.

Automated allocation transactions are available as an optional feature. If implemented, allocation rules can be configured to automatically create journal entries that allocate expenses or revenues according to defined business rules (e.g., allocating shared overhead to departments or projects). However, this is optional and requires a business decision on whether automated allocations are needed.

#### Future State Process

Payroll entries will be exported from Paylocity as CSV on a monthly basis. The file will be imported directly into NetSuite using the CSV import tool. NetSuite will automatically create the journal entry in the GL with the imported data. The system will automatically generate reversal entries on the first day of the following period, with those reversals automatically reversed on the first day of the period after that, creating clean P&L reporting.

If automated allocations are implemented, allocation transactions will run automatically at period end, creating journal entries that allocate expenses according to the configured rules.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Complexity | Status |
|--------|-------------|---------------------------|----------|-----------|--------|
| REQ-018 | CSV import of JEs with auto-reversal | Journal Entry Import + Reversal JE automation | ALIGNS | Low | **Confirmed** |
| REQ-019 | Automated allocation transactions | Allocation rules engine | ADAPT | Medium | **DECISION PENDING** - Leadership decision required |

#### Implementation Approach

- CSV import will be configured for Paylocity payroll entries during system setup
- Automated reversal rules will be configured and tested before go-live
- If allocation transactions are approved in SESSION 3, allocation rules will be designed and tested
- Integration with Paylocity will be tested to ensure CSV exports are properly formatted

#### Implementation Considerations

- CSV import testing required to ensure data integrity
- Payroll entry timing must align with GL close process
- Reversal automation will eliminate prior tracking issues and improve audit compliance
- If automated allocations are implemented, allocation rules must be clearly documented and tested

---

### 7. Period Close Process

#### Your Business Requirements

**REQ-020:** Implement NetSuite Period Close Checklist to replace Excel-based process (ALIGNS)
- System-guided checklist replaces Excel-based close workbook
- Evidence: "10 days to close accounting period... All managed via Excel... NetSuite: Built-in Checklist... Step-by-step process" - Team
- Implementation Advantage: Guided workflow ensures no steps are missed; timestamps and approvals are automatically tracked
- Session Dependency: SESSION 4 for detailed requirements

**REQ-021:** Configure ability to close AP/AR modules separately from GL (ALIGNS)
- Flexible module closing via checklist; AP/AR can close before GL if needed
- Evidence: "Can close AP/AR separately and go through checklist... Flexible closing process... Close modules as ready" - Marcus
- Outstanding Question: Can AP/AR close in parallel with GL or must be sequential?

**REQ-022:** Open all 13 periods at year start, close progressively (ADAPT)
- Best practice: open full year in December, close periods as completed
- Evidence: "Open entire year at once... Set December reminder to open next year... Don't open more than one year ahead" - Marcus best practice
- Process Change: Users must adapt to year-open approach vs. opening periods on-demand

#### Current State Process

KB+Hoag currently operates a 10-day manual period close process primarily managed via Excel. The finance team manually:
1. Reconciles bank accounts and AP
2. Creates and enters journal entries
3. Reconciles GL balances
4. Prepares period close reports
5. Generates financial statements

The process is entirely tracked in Excel, requiring the team to manually navigate each step and validate completion. There is no system-based checklist or automated tracking of close milestones.

#### Orion/NetSuite Solution

Orion/NetSuite provides a comprehensive Period Close Checklist module that guides the finance team through required close steps. The checklist can be customized to KB+Hoag's specific requirements and will include:
- Step-by-step close tasks with due dates and owners
- Automated reconciliation workflows for bank, intercompany, and control account reconciliations
- Approval gates where specified (e.g., GL reconciliation must be approved before JE entry)
- Task completion tracking with timestamps and user attribution
- Pre-configured workflows that prepare data for the next period

Through SESSION 4 (Period Close Process Optimization), the finance team will identify bottlenecks in the current 10-day close and design the NetSuite checklist to streamline the process. The goal is to reduce close time from 10 days to 5-7 days by eliminating manual Excel steps and automating reconciliations.

The platform supports separate closing of AP/AR modules from GL if business processes require this flexibility. The 13-period structure will be fully supported, with all periods opened at year-end and progressively closed as completed.

#### Future State Process

At the end of each accounting period, KB+Hoag's finance team will access the NetSuite Period Close Checklist. The checklist will present a guided workflow of tasks:
1. Reconcile bank accounts (automated matching against cleared items)
2. Reconcile AP aging to subledger
3. Reconcile AR aging to subledger
4. Enter recurring journal entries (from pre-configured list)
5. Complete balance reconciliations (if needed)
6. Prepare financial statements
7. Obtain management review and approval

Finance team members will update task status as completed. Approvals will flow through NetSuite when approval gates are reached. The system will track completion dates and who completed each task. Once all tasks are marked complete, the period is ready to close. Based on SESSION 4 optimization, the target timeline is 5-7 days from period end to closed status.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Complexity | Timeline Impact |
|--------|-------------|---------------------------|----------|-----------|-----------------|
| REQ-020 | Period Close Checklist (replaces Excel) | NetSuite built-in Period Close Checklist | ALIGNS | Medium | **Potential 3-5 day reduction** |
| REQ-021 | Separate AP/AR/GL closing | Flexible module-level close capability | ALIGNS | Low | Depends on current process |
| REQ-022 | Open all periods year-start | Calendar management best practice | ADAPT | Low | Process change for users |

#### Implementation Approach - SESSION 4 REQUIRED

- SESSION 4 will analyze current 10-day close process step-by-step
- Bottleneck identification will drive checklist design
- Recurring JE list will be pre-configured based on current requirements
- Reconciliation workflows will be designed during SESSION 4
- Approval gates will be established based on current governance
- Target timeline reduction (10 days → 5-7 days) will be confirmed as realistic goal

#### Implementation Considerations - CRITICAL FOR TIMELINE IMPROVEMENT

- Current 10-day close offers significant optimization opportunity
- SESSION 4 deep-dive required to identify quick wins (often: automation of reconciliations, pre-configuration of recurring JEs)
- Parallel running: First 2-3 periods may require parallel close (Excel + NetSuite) to validate accuracy
- Training critical: Lorraine and team must understand new workflow vs. Excel process
- User acceptance: New system-guided process will require trust-building during early periods
- Reconciliation accuracy testing: Results must match Excel process before going live
- Documentation: Step-by-step close procedures must be documented for team reference

---

### 8. Labor Markup & Costing (STRATEGIC - DECISION PENDING)

#### Your Business Requirements

**REQ-023:** Determine if 15% labor markup (contingency line) will continue in NetSuite (ADAPT - DECISION PENDING)
- Current practice in Core adds 15% contingency to labor costs
- Evidence: "That may be up for debate as to whether or not we would want to keep that... Matt and Mark decision... Commission is paid on that..." - Kipp
- **CRITICAL DECISION REQUIRED**: Leadership decision impacts commission structure, custom development scope, and financial reporting
- Session Dependency: **SESSION 3 REQUIRED** - Cannot proceed without final decision
- Implementation Impact: If continued, may require custom script development; if eliminated, requires sales communication

**REQ-024:** Maintain separate Project GP vs. Commissionable GP reporting and KPIs (ACCOMMODATE - DECISION DEPENDENT)
- Two distinct GP metrics for different audiences: true project profitability vs. commission-eligible earnings
- Evidence: "That's why we have two... different set of KPIs... So, we have a set of KPIs for project gross profit, and then we have commissionable gross profit" - Kipp
- Complexity: Requires custom reporting, dashboards, and role-based visibility
- Dependent on: REQ-023 (labor markup decision) and REQ-025 (role-based permissions)

**REQ-025:** Configure role-based permissions for different GP visibility (ACCOMMODATE - DECISION DEPENDENT)
- Sales team sees Commissionable GP; Management sees true Project GP
- Evidence: "Permission Control: Different people see different KPIs... Role-based visibility... Sales may see commissionable GP... Management sees true project GP" - Discussion
- Complexity: Permission design must be tested and validated
- Dependent on: REQ-023 and REQ-024 decisions

#### Current State Process

KB+Hoag's current commission structure includes a 15% contingency markup on labor costs. This markup:
- Adds 15% to labor line items before calculating commissions
- Affects commission calculations (commission is paid on the markup as well as base labor)
- Creates a difference between Project GP (actual cost-based) and Commissionable GP (cost + markup)

Sales teams see Commissionable GP (which includes the 15% markup) for commission purposes. Management sees true Project GP (without markup) for actual profitability analysis.

#### Orion/NetSuite Solution

Orion/NetSuite enables both approaches through flexible project accounting and reporting capabilities:

**Option A: Continue 15% Labor Markup**
If leadership decides to continue the 15% markup, custom script development can automate the calculation at order line-item level. The markup would be calculated and added to labor costs automatically. Commission rules would be configured to apply commissions to the total (base labor + markup). Project GP and Commissionable GP would be tracked separately through distinct custom fields and calculated values.

**Option B: Eliminate 15% Labor Markup**
If leadership decides to eliminate the markup, all labor costs would be charged at actual cost. Commissions would be based on actual project costs only. Project GP and Commissionable GP would converge (or the distinction could be eliminated entirely). Sales team would need clear communication about the impact on commission calculations.

Both options require SESSION 3 detailed discussion and final leadership decision before custom development can proceed.

#### Future State Process

**If 15% Markup Continues:**
At order line-item entry, labor costs are entered. The system automatically calculates and applies the 15% markup, creating a total labor line value. Commission calculations apply commissions to this total (base + markup). At project completion, the system generates two reporting views: Project GP (actual cost) and Commissionable GP (cost + markup). Sales teams access dashboards showing Commissionable GP. Management accesses dashboards showing true Project GP for actual profitability analysis.

**If 15% Markup is Eliminated:**
At order line-item entry, labor costs are entered at actual value. No markup is automatically applied. Commission calculations apply commissions to actual costs only. Project GP reflects true profitability without any contingency markup. This requires change communication to sales teams about commission impacts.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Complexity | Status |
|--------|-------------|---------------------------|----------|-----------|--------|
| REQ-023 | 15% labor markup continuation decision | Project costing + custom script (if continuing) | ADAPT | Medium-High | **DECISION PENDING** |
| REQ-024 | Project GP vs. Commissionable GP tracking | Custom calculated fields + reporting | ACCOMMODATE | High | **Dependent on REQ-023** |
| REQ-025 | Role-based permission visibility | Role/Permission setup with field-level visibility | ACCOMMODATE | Medium | **Dependent on REQ-023** |

#### Implementation Approach - SESSION 3 REQUIRED

- **SESSION 3 will present both scenarios** with implementation approaches, custom development scope, and commission impact analysis
- **Final decision required from Matt/Mark** before configuration can proceed
- **If continuing markup**: Custom script will be designed during detailed design phase
- **If eliminating markup**: Sales communication plan will be developed; commission recalculation analysis will be performed

#### Implementation Considerations - CRITICAL DECISION GATE

- This is a **strategic business decision** with major implications
- **Commission impact**: Elimination of markup may reduce commission amounts; continuation increases scope and custom development
- **Custom development scope**: If continuing, requires custom script (moderate complexity); if eliminating, eliminates custom development needs
- **Timeline impact**: Decision delay directly impacts configuration phase timeline
- **Sales alignment**: Sales team must understand and accept the decision; communication plan is critical
- **KPI reporting**: Dual GP metric tracking is more complex than single metric; worth the complexity if markup continues

---

### 9. Fixed Asset Management (EVALUATION PENDING)

#### Your Business Requirements

**REQ-026:** Evaluate NetSuite Fixed Asset module vs. continuing Bloomberg (ADAPT - DECISION PENDING)
- Currently pays for Bloomberg third-party tool for asset management
- Evidence: "I just want to know if NetSuite can meet our needs, and do we need that fixed asset stuff? [Currently] paying for a third party to do that. Bloomberg... I think the fixed asset module's gonna handle what you need" - Lorraine/Marcus
- Session Dependency: SESSION 7 for evaluation and decision
- Outstanding Questions: Current Bloomberg cost? NetSuite FA module cost? Migration effort?
- Cost-Benefit: Potential elimination of third-party tool cost

#### Current State Process

KB+Hoag currently maintains a separate fixed asset management system (Bloomberg) outside NetSuite. Assets are managed in Bloomberg with depreciation calculations, book/tax depreciation tracking, and asset lifecycle management. Financial reporting requires manual consolidation of fixed asset information from Bloomberg with NetSuite GL accounts.

#### Orion/NetSuite Solution

Orion/NetSuite includes a native Fixed Asset module that provides comprehensive asset management capabilities. The module can track:
- Asset acquisition, depreciation, and disposal
- Multiple depreciation methods (straight-line, declining balance, MACRS, Section 179)
- Book vs. tax depreciation tracking
- Asset categorization and reporting

SESSION 7 will evaluate whether the NetSuite Fixed Asset module capabilities meet KB+Hoag's needs, potentially eliminating the Bloomberg tool and consolidating asset management within NetSuite.

#### Future State Process

**If Fixed Asset Module is Selected:**
Assets are entered into the NetSuite Fixed Asset module at acquisition. Depreciation rules are configured based on asset class and required depreciation methods. The system automatically calculates depreciation each period. Fixed asset schedules are generated directly from NetSuite for financial statement reporting.

**If Bloomberg Continues:**
Bloomberg continues as the asset management system; NetSuite includes a GL account for fixed assets. Integration between Bloomberg and NetSuite is managed manually or through periodic reconciliation.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Complexity | Status |
|--------|-------------|---------------------------|----------|-----------|--------|
| REQ-026 | Fixed Asset management evaluation | NetSuite FA module vs. Bloomberg | ADAPT | Medium | **DECISION PENDING** |

#### Implementation Approach - SESSION 7 REQUIRED

- SESSION 7 will review Bloomberg current usage and costs
- NetSuite FA module capabilities will be evaluated against Bloomberg features
- Cost-benefit analysis will be performed
- If module selected, migration plan for existing assets will be developed

#### Implementation Considerations

- **DECISION PENDING**: NetSuite FA vs. Bloomberg
- If migrating to NetSuite: Existing assets must be migrated with historical depreciation data
- Depreciation methods must be fully specified (straight-line, declining balance, MACRS, Section 179)
- Book vs. tax depreciation tracking requirements must be confirmed
- Cost-benefit analysis critical - module may pay for itself quickly if Bloomberg is eliminated

---

### 10. Payroll Integration

#### Your Business Requirements

**REQ-027:** Configure CSV journal entry import from Paylocity (or new payroll provider) (ALIGNS)
- Payroll entries imported as CSV from Paylocity; department allocation done before import
- Evidence: "CSV download from Paylocity... Journal entry import to NetSuite... Department Allocation: Allocations done before import" - Current process
- Implementation Approach: Standard CSV import; flexible for any payroll provider

**REQ-028:** Evaluate new HR platform/payroll provider integration (ADAPT)
- Paylocity is current payroll provider; HR platform evaluation in progress
- Evidence: "Paylocity: Current payroll provider... May change (evaluation ongoing)... HR platform evaluation in progress" - Team
- Outstanding: Provider decision pending; CSV approach remains flexible

#### Current State Process

KB+Hoag currently uses Paylocity for payroll processing. Each month, Paylocity generates a CSV file containing journal entry data with department allocations. This file is imported into the GL. No other integration exists between Paylocity and NetSuite.

#### Orion/NetSuite Solution

Orion/NetSuite supports CSV journal entry import for payroll data. The approach is provider-agnostic - as long as the payroll system can generate CSV output, NetSuite can import it. Department allocations can be included in the CSV, or they can be handled separately during the import process.

If the organization selects a new HR platform/payroll provider, the CSV import approach remains flexible. Most modern payroll providers support CSV export, so the integration approach is unlikely to change regardless of provider.

#### Future State Process

Each month, the payroll provider generates a CSV file containing journal entry data with department allocations. This file is uploaded to NetSuite through the CSV import tool. NetSuite processes the entries and posts them to the GL. No manual data entry or department allocation is required.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Complexity | Status |
|--------|-------------|---------------------------|----------|-----------|--------|
| REQ-027 | CSV import from Paylocity/payroll provider | Journal Entry Import | ALIGNS | Low | Confirmed |
| REQ-028 | New HR platform evaluation | CSV import remains flexible | ADAPT | Low | **Provider decision pending** |

#### Implementation Approach

- CSV import format will be finalized based on current Paylocity export
- If payroll provider changes, CSV format will be validated with new provider
- Import process will be tested during system setup

---

### 11. Payment Processing

#### Your Business Requirements

**REQ-029:** Maintain Stripe integration for credit card payment acceptance (ALIGNS)
- Current Stripe integration works well for incidental use (~$100/year)
- Evidence: "Payment link embedded in invoice hyperlink... Very rare we take a credit card... Stripe: Transaction-based pricing only... Stay with Stripe currently" - Team
- Implementation Approach: Keep current setup; low priority

**REQ-030:** Support wire transfer processing for international payments (ADAPT)
- International wires are expensive but occasionally needed
- Evidence: "Wires restricted to international (expensive)... Module question: ACH only or wire support too?... If not integrated: Manual entry in bank portal" - Discussion
- Outstanding Question: Integrated in Advanced Electronic Bill Payments or manual bank portal required?
- Session Dependency: SESSION 5 for clarification

#### Current State Process

KB+Hoag currently uses Stripe for credit card payment acceptance. Credit cards are charged through an embedded payment link in customer invoices. Transactions are rare (approximately $100/year in fees). For international wire transfers, the team manually processes wires through the bank portal when needed.

#### Orion/NetSuite Solution

Orion/NetSuite maintains Stripe integration for continued credit card acceptance. The embedded payment link approach remains unchanged.

For wire transfers, the solution depends on whether Advanced Electronic Bill Payments supports wire transfer capability (to be confirmed in SESSION 5). If supported, wires can be processed directly from NetSuite. If not supported, international wires continue to be processed manually through the West Coast Community Bank portal.

#### Future State Process

Credit card payments continue to use the Stripe embedded link - no changes to current process. Wire transfers are processed either through NetSuite (if integrated in Advanced Electronic Bill Payments) or through the bank portal if not integrated.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Complexity | Status |
|--------|-------------|---------------------------|----------|-----------|--------|
| REQ-029 | Stripe integration maintenance | Keep current Stripe setup | ALIGNS | Low | Confirmed |
| REQ-030 | Wire transfer processing | Advanced Electronic Bill Payments (TBD) or manual portal | ADAPT | Low-Medium | **Clarification needed in SESSION 5** |

#### Implementation Approach

- Stripe integration will be maintained as-is
- Wire transfer capability will be confirmed during SESSION 5
- If supported in Advanced Electronic Bill Payments, wire processing will be configured
- If not supported, wire processing will continue through bank portal

---

### 12. Customer Financial Management

#### Your Business Requirements

**REQ-031:** Configure finance charge capability (off by default, available as deterrent) (ALIGNS)
- Finance charges available but never used (13 years); kept for potential deterrent effect
- Evidence: "Never implemented in 13 years (Lorraine)... Deterrent/threat only... Most dealers want to threaten. They don't actually follow through" - Lorraine
- Implementation Approach: Standard configuration, turned off by default

**REQ-032:** Implement pro forma invoice for customer deposit management (ALIGNS)
- Deposits collected via pro forma invoices; apply automatically to final invoice
- Evidence: "Not revenue-recognizing transaction... Liability account... Deposit collection... Automatically applies to final invoice when generated" - Discussion
- Implementation Approach: Standard NetSuite functionality

#### Current State Process

KB+Hoag collects customer deposits on projects. Deposits are tracked through manual Excel processes or separate invoicing. At project completion, deposit amounts are manually applied to the final invoice. Finance charges are not used but are available if the organization decides to implement them.

#### Orion/NetSuite Solution

Orion/NetSuite provides standard capabilities for both finance charges and pro forma invoicing. Finance charges are available as a feature and can remain disabled by default. If the organization ever decides to charge late payment penalties, the feature is available and can be enabled without customization.

Pro forma invoices are a standard NetSuite feature designed for deposit collection. A pro forma invoice is issued to collect the deposit, which posts to a liability account (not revenue). When the final invoice is generated, the pro forma deposit is automatically applied, reducing the final amount due.

#### Future State Process

At project initiation, a pro forma invoice is created requesting the customer deposit. The customer remits payment against the pro forma invoice. NetSuite posts the payment to the deposit liability account. At project completion, the final invoice is generated. NetSuite automatically applies the deposit amount to the final invoice, reducing the amount due from the customer.

Finance charges remain off by default. If the organization later decides to charge late fees on overdue invoices, the feature can be enabled in system administration.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Complexity | Status |
|--------|-------------|---------------------------|----------|-----------|--------|
| REQ-031 | Finance charge capability (off by default) | Finance Charges module (disabled) | ALIGNS | Low | Confirmed |
| REQ-032 | Pro forma invoice for deposits | Pro Forma Invoice functionality | ALIGNS | Low | Confirmed |

#### Implementation Approach

- Finance charges will be configured but disabled by default
- Pro forma invoice process will be configured and tested
- Automatic deposit application will be tested to ensure accuracy

---

### 13. Vendor Management

#### Your Business Requirements

**REQ-033:** Configure vendors that are also customers (Intermarket dealers) (ALIGNS)
- Dealers must be set up as both vendor AND customer (hundreds of outbound transactions)
- Evidence: "Dealers must be set up as both vendor AND customer... Pain point for first-time dealer setup... High volume (Shannon: hundreds of outbound transactions)" - Team
- Implementation Approach: Standard NetSuite functionality; setup process to be documented
- Stakeholder: Shannon (Product Coordinator Manager) - vendor management coordination

**REQ-034:** Implement vendor credit limit tracking with warning alerts (ACCOMMODATE - CUSTOM DEVELOPMENT)
- Track KB+Hoag's credit limits with vendors; warn when approaching limits
- Evidence: "Track KBM credit limits with vendors... Hit limits unexpectedly: Mad scramble at that nth hour... Need warnings/alerts" - Team
- Complexity: Custom development required for alert mechanism and warning threshold logic
- Session Dependency: SESSION 8 for detailed requirements (alert mechanism, threshold, custom dev scope)
- Outstanding Questions: Warning threshold (90%)? Alert mechanism (email, dashboard, hard stop)? Credit utilization calculation?

#### Current State Process

KB+Hoag manages vendor relationships with hundreds of suppliers. Many of these supplier relationships also include buying from those same dealers (they are both customers and vendors). When setting up new vendors in NetSuite, they must often also be added as customers for reciprocal transactions. 

KB+Hoag has credit limits with many vendors. When approaching or hitting those limits, there is no system warning—the team discovers the problem when orders are placed. This creates operational delays and sometimes requires rush payment processing to avoid disrupting vendor relationships.

#### Orion/NetSuite Solution

Orion/NetSuite provides standard functionality for dual vendor/customer setup. Vendors can be configured as customers, enabling the same entity to appear in both vendor and customer lists. For vendor-customers with high transaction volume, this is a standard approach.

Vendor credit limit tracking with automated warnings requires custom development. Through SESSION 8, the team will define:
- Warning threshold (e.g., 90% of credit limit)
- Alert recipients (who sees warnings)
- Alert mechanism (email notification, dashboard widget, hard PO block, or combination)
- Credit utilization calculation (include open POs + unpaid bills vs. limit)
- Process for handling warnings (early payment trigger, order defer, etc.)

Custom alert logic will be developed during configuration phase to monitor vendor credit utilization and trigger alerts when usage exceeds the defined threshold.

#### Future State Process

Vendor-customers are set up once with both vendor and customer profiles. Shannon's team maintains the dual setup during ongoing vendor management.

Vendor credit limits are configured in NetSuite with defined warning thresholds. Each month, the system monitors credit utilization for all vendors with configured limits. When utilization approaches the threshold (e.g., 90%), the system triggers alerts to specified recipients via email or dashboard notification. Finance or purchasing team members review alerts and can take action (early payment, order deferral) before hitting actual limits and creating operational disruption.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Complexity | Status |
|--------|-------------|---------------------------|----------|-----------|--------|
| REQ-033 | Vendor-Customer dual setup | Vendor and Customer configuration | ALIGNS | Low | Confirmed |
| REQ-034 | Vendor credit limit alerts | Custom alert system with threshold logic | ACCOMMODATE | Medium | **Detailed requirements needed in SESSION 8** |

#### Implementation Approach

- Vendor-customer setup process will be documented and handled during customer/vendor data migration
- SESSION 8 will define vendor credit limit tracking requirements
- Custom alert logic will be developed based on SESSION 8 specifications
- Alert system will be tested for accuracy and timing

#### Implementation Considerations - SESSION 8 REQUIRED

- **CUSTOM DEVELOPMENT REQUIRED**: Alert system must be designed and tested
- Warning threshold definition critical (90% recommended but must be confirmed)
- Alert recipients and communication mechanism must be clearly defined
- Credit utilization calculation must account for open POs + unpaid bills + existing holds
- Testing required for accuracy - false alerts can overwhelm users; missed alerts defeat the purpose
- Change management: Process for handling warnings must be established (who takes action? escalation path?)

---

### 14. Revenue & Cost Recognition (COMPLIANCE-CRITICAL)

#### Your Business Requirements

**REQ-035:** Define revenue recognition rules and timing (at Sales Order or Invoice) (ACCOMMODATE - DECISION PENDING)
- Complex rules; timing decision pending; special scenarios need documentation
- Evidence: "Decision point: When does revenue recognize?... Typically at sales order or invoice... May need special rules for certain order types... White paper mentioned" - Discussion
- Session Dependency: **SESSION 1 REQUIRED** - Compliance-critical, requires white paper review and potentially auditor input
- Outstanding Questions: Sales order vs. invoice timing? Special scenarios (mockup, direct bill, government, E-commerce)? ASC 606 compliance?

**REQ-036:** Maintain project-level revenue/cost tracking with linked transactions (ALIGNS)
- All transactions linked to project; project-level revenue/cost aggregation; KPI dashboard at project level
- Evidence: "All transactions linked to project... Project-level revenue/cost aggregation... KPI dashboard at project level" - Team
- Implementation Approach: Standard project accounting; dependent on REQ-035 for recognition timing

#### Current State Process

KB+Hoag currently recognizes revenue at order creation in their existing Core system. This approach may not align with ASC 606 compliance requirements or specific industry standards for contract furniture dealerships. Revenue recognition timing for different order types (standard orders, mockups, direct bill, government, E-commerce) may require different rules. These are not currently documented.

#### Orion/NetSuite Solution

Orion/NetSuite provides flexible project-level revenue recognition through its Project Record module. The platform can support different recognition rules based on order type or transaction characteristics. However, specific revenue recognition rules must be defined by the business and possibly validated with external auditors before implementation.

Through SESSION 1, KB+Hoag will:
1. Review the revenue recognition white paper referenced in discovery
2. Determine revenue recognition timing (at sales order or invoice)
3. Document special scenarios requiring different recognition rules
4. Validate ASC 606 compliance
5. Potentially engage external auditor for compliance review

Once revenue recognition rules are finalized, NetSuite can be configured to implement those rules through custom project accounting logic or period-end revenue recognition processes.

#### Future State Process

At project creation, all transactions are linked to the project. As transactions occur (sales orders, invoices, expense entries, time tracking), they are automatically aggregated at the project level. Revenue is recognized based on the defined rules (either at sales order or invoice, depending on decision in SESSION 1). At any point, the Project Record dashboard shows real-time project profitability including revenue, costs, and gross profit. Project-level reporting reflects the defined revenue recognition approach.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Complexity | Status |
|--------|-------------|---------------------------|----------|-----------|--------|
| REQ-035 | Revenue recognition rules & timing | Project accounting with custom logic | ACCOMMODATE | **HIGH** | **DECISION PENDING - SESSION 1 REQUIRED** |
| REQ-036 | Project-level revenue/cost tracking | Project Record module | ALIGNS | Low | Confirmed |

#### Implementation Approach - SESSION 1 CRITICAL

- **SESSION 1 is compliance-critical** and must be completed before detailed design
- White paper review will inform revenue recognition approach
- If revenue recognition rules require custom logic, that will be designed during configuration
- External auditor review may be recommended for compliance validation

#### Implementation Considerations - HIGH RISK

- **COMPLIANCE-CRITICAL**: Improper revenue recognition can result in audit findings or restatement requirements
- **SESSION 1 MANDATORY**: Cannot proceed without clear revenue recognition rules
- **Auditor involvement recommended**: External auditor should review and validate revenue recognition approach
- **White paper review pending**: Referenced white paper must be reviewed and validated
- **Special scenarios must be documented**: Mockup orders, direct bill, government orders, E-commerce orders may require different rules
- **ASC 606 compliance validation required**: Revenue recognition must comply with current accounting standards
- **Custom development may be needed**: If revenue recognition rules are complex, custom project accounting logic may be required

---

### 15. Financial Reporting & Dashboards

#### Your Business Requirements

**REQ-037:** Create real-time financial dashboards to replace manual Excel reports (ALIGNS)
- Real-time reporting with period-over-period analysis and automated report generation
- Evidence: "Real-time reporting... Period-over-period analysis... Custom dashboards... Automated report generation" - Team
- Implementation Approach: Standard NetSuite dashboard and reporting functionality

**REQ-038:** Configure project-level KPI dashboards (real-time GP, revenue/cost tracking, commission reporting) (ACCOMMODATE - CUSTOM DASHBOARDS)
- Project GP, Commissionable GP, revenue/cost tracking, commission reporting
- Evidence: "KPI dashboards... Real-time GP visibility... Revenue/cost tracking... Commission reporting" - Team
- Complexity: Custom dashboard configuration required; role-based visibility needed
- Dependent on: REQ-023 (labor markup), REQ-024 (dual GP metrics), REQ-025 (role-based permissions)

#### Current State Process

KB+Hoag currently generates financial reports manually using Excel. Data is exported from NetSuite Core into Excel files where analysis is performed, comparisons are created, and reports are generated. This process is time-consuming and limits reporting frequency and accessibility. Project profitability dashboards do not exist - project profitability is analyzed through ad hoc Excel analysis.

#### Orion/NetSuite Solution

Orion/NetSuite provides comprehensive reporting and dashboard capabilities. Financial dashboards can be created to display:
- Real-time GL balances and activity
- Period-over-period comparative analysis
- Revenue, cost, and profitability trends
- Project-level financial metrics

The Orion Project Record module consolidates all project data including revenue, costs, GP, time tracking, and communications. Custom dashboards can be built to display project KPIs including:
- Project gross profit (actual profitability)
- Commissionable gross profit (used for commission calculations if REQ-023 continues)
- Revenue vs. budget
- Cost tracking vs. budget
- Commission accruals by sales rep

Role-based visibility can be configured so sales teams see Commissionable GP while management sees true Project GP.

#### Future State Process

Finance team members log into NetSuite and access real-time financial dashboards showing GL activity, balance trends, and period-over-period analysis. Project managers and sales teams access project dashboards showing real-time project profitability and metrics. Dashboards refresh automatically as transactions are entered. No Excel-based reporting is required.

Standard financial reports (income statement, balance sheet, project detail reports) are run directly from NetSuite and exported when needed for management review or distribution.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Complexity | Dependencies |
|--------|-------------|---------------------------|----------|-----------|---|
| REQ-037 | Real-time financial dashboards | NetSuite Dashboards + Reporting | ALIGNS | Medium | None |
| REQ-038 | Project-level KPI dashboards | Orion Project Record + Custom Dashboards | ACCOMMODATE | Medium-High | REQ-023, REQ-024, REQ-025 |

#### Implementation Approach

- Dashboard requirements will be defined during detailed design phase
- Standard financial dashboards will be created first
- Project-level KPI dashboards will be built based on SESSION 3 outcomes (labor markup, GP metrics, role-based visibility)
- Role-based dashboard access will be configured per SESSION 3 specifications
- Testing will validate dashboard accuracy and performance

#### Implementation Considerations

- Dashboard design must reflect actual KPI needs - avoid "pretty dashboards" that aren't used
- Performance testing needed for real-time updates with large transaction volumes
- Custom dashboards for dual GP metrics require careful design for role-based visibility
- Training needed: Users must understand how to interpret new dashboards
- Excel reports may continue temporarily in parallel until users trust system dashboards

---

## Implementation Complexity Summary

### By Complexity Level

**Simple (Low Risk, Standard NetSuite Features) - 15 items:**
- REQ-001, REQ-003, REQ-004, REQ-005, REQ-007, REQ-011, REQ-012, REQ-018, REQ-021, REQ-029, REQ-031, REQ-032, REQ-033, REQ-036, REQ-037

**Moderate (Process Changes, Some Configuration) - 8 items:**
- REQ-002, REQ-006, REQ-008, REQ-009, REQ-017, REQ-027, REQ-028, REQ-030

**Complex (Custom Development, Design Decisions, High Risk) - 15 items:**
- REQ-010, REQ-013/014, REQ-015, REQ-016, REQ-019, REQ-020, REQ-022, REQ-023, REQ-024, REQ-025, REQ-026, REQ-034, REQ-035, REQ-038

---

## High-Risk Requirements & Mitigation Strategies

| REQ-ID | Requirement | Risk | Severity | Mitigation Strategy |
|--------|-------------|------|----------|---|
| **REQ-016** | Chart of Accounts consolidation | Massive change affecting all transactions; high user training burden; impacts all reports | **CRITICAL** | **SESSION 2** required for detailed design; comprehensive mapping documentation; phased user training; extensive testing of GL balances and historical reporting |
| **REQ-035** | Revenue recognition rules | Compliance-critical; errors impact financial statements and audit; white paper needs review | **CRITICAL** | **SESSION 1** with external auditor review recommended; detailed documentation of recognition rules by order type; testing and validation plan for recognition logic |
| **REQ-023** | 15% labor markup decision | If eliminated: major sales compensation change; if continued: custom script development | **HIGH** | **SESSION 3** required; final leadership decision mandatory before configuration; sales communication plan if eliminating |
| **REQ-024/025/038** | Project GP vs. Commissionable GP | Custom calculation logic; role-based visibility complex; commission impact; dependent on REQ-023 | **HIGH** | **SESSION 3** detailed requirements; calculation validation; user acceptance testing; parallel testing first few months |
| **REQ-004** | 48-state nexus tax management | Ongoing compliance; certificate maintenance; audit risk | HIGH | SuiteTax configuration validation; certificate upload process documentation; expiration monitoring dashboard |
| **REQ-009** | Advanced Electronic Bill Payments | Critical AP process; high dollar amounts ($3M runs); vendor impact | HIGH | Thorough testing; parallel run with NACHA fallback; remittance confirmation verification; vendor communication plan |
| **REQ-015** | Project vs. G&A expense allocation | Must work with Expensify/RAMP integration; COGS accuracy critical | Medium | Dependent on **SESSION 6** platform selection; integration testing; project coding validation; user training |
| **REQ-034** | Vendor credit limit tracking | Custom development required; "mad scramble" pain point; operational efficiency | Medium | **SESSION 8** requirements definition; alert mechanism clarification; testing for accuracy; process documentation |

---

## Critical Decision Points & Timeline

### Critical Path (Must Complete Before Proceeding to Configuration)

| Decision | REQ-ID | Decision Maker | Target Date | Impact | Session |
|----------|--------|---|---|---|---|
| **Revenue Recognition Rules** | REQ-035 | Lorraine, Marcus (+ auditor?) | Before detailed design | Compliance-critical; affects financial accuracy | **SESSION 1** |
| **Chart of Accounts Design** | REQ-016 | Lorraine, Celine, Kevin | **URGENT** - ASAP | Foundational; affects all transactions | **SESSION 2** |
| **Commission Structure & Labor Markup** | REQ-023 | Matt/Mark (Leadership) | Before configuration | Impacts sales compensation, custom dev scope | **SESSION 3** |

### Recommended Implementation Timeline

**Phase 0: Pre-Discovery Sessions** (Weeks 1-2)
- [ ] Export Core COA and prepare SESSION 2 pre-work
- [ ] Review revenue recognition white paper; prepare SESSION 1
- [ ] Compile commission/labor markup analysis; prepare SESSION 3
- [ ] Begin vendor credit limit tracking analysis; prepare SESSION 8

**Phase 1: Follow-Up Discovery Sessions** (Weeks 2-4)
- [ ] Complete SESSION 1: Revenue Recognition (Week 2)
- [ ] Complete SESSION 2: Chart of Accounts (Week 2)
- [ ] Complete SESSION 3: Commission Structure (Week 3)
- [ ] Complete Sessions 4-8 (Weeks 3-4)

**Phase 2: Strategic Decisions** (Week 4)
- [ ] Finalize revenue recognition approach
- [ ] Approve COA consolidation design
- [ ] Leadership decision on labor markup
- [ ] Expense platform selection
- [ ] Fixed asset management decision

**Phase 3: Detailed Design & Configuration** (Weeks 5-12)
- [ ] Design and configure Chart of Accounts consolidation
- [ ] Design revenue recognition custom logic (if needed)
- [ ] Design commission and GP tracking (if labor markup continues)
- [ ] Configure all integrations (bank feeds, expense platform, payroll)
- [ ] Design and build custom dashboards
- [ ] Build period close checklist and workflows

**Phase 4: Data Migration & Testing** (Weeks 10-16)
- [ ] Historical data migration (2017-present)
- [ ] COA mapping validation
- [ ] User acceptance testing (UAT)
- [ ] Period close parallel testing (first 2-3 periods)
- [ ] Dashboard accuracy testing

**Phase 5: Training & Go-Live** (Weeks 14-18)
- [ ] Finance team training on new processes
- [ ] Dashboard user training
- [ ] Period close workflow training
- [ ] Go-live cutover planning and execution

---

## Dependencies & Integration Points

### Key Integration Dependencies

| Integration | REQ-IDs | Status | Critical Path Impact |
|---|---|---|---|
| **West Coast Community Bank** | REQ-008, REQ-009, REQ-011 | Confirmed partner | High - Critical for banking automation |
| **Expensify vs. RAMP** | REQ-013, REQ-014, REQ-015 | **Decision pending SESSION 6** | Medium - Affects user adoption |
| **Paylocity / New Payroll Provider** | REQ-027, REQ-028 | Current known; flexible for new | Low - CSV approach flexible |
| **Stripe** | REQ-029 | Current; maintained | Low - No changes needed |
| **Bloomberg / NetSuite FA Module** | REQ-026 | **Decision pending SESSION 7** | Low - Nice-to-have vs. critical |

### Requirement Dependencies

```
REQ-016 (COA Design) [SESSION 2]
  ├─ Foundational for all other requirements
  └─ Required for: REQ-017 (Historical Data Migration)

REQ-035 (Revenue Recognition) [SESSION 1]
  ├─ Compliance-critical
  └─ Related to: REQ-036 (Project-level revenue/cost tracking)

REQ-023 (15% Labor Markup Decision) [SESSION 3] **CRITICAL GATE**
  ├─ Affects: REQ-024 (Project GP vs. Commissionable GP)
  ├─ Affects: REQ-025 (Role-based permissions)
  ├─ Affects: REQ-038 (KPI dashboards)
  └─ Affects: Commission structure and sales compensation

REQ-024/025/038 (GP Metrics & Dashboards) [SESSION 3]
  ├─ Dependent on: REQ-023 decision
  └─ Related to: REQ-015 (Project vs. G&A expense allocation)

REQ-013/014 (Expense Platform) [SESSION 6] **DECISION GATE**
  └─ Affects: REQ-015 (Project coding capability)

REQ-026 (Fixed Assets) [SESSION 7] **DECISION GATE**
  └─ Independent - no other REQ dependencies
```

---

## Outstanding Items & Action Register

### Immediate Actions Required (Before Sessions)

- [ ] **Export current Core COA** - 40+ page chart; analyze for SESSION 2
- [ ] **Review revenue recognition white paper** - prepare for SESSION 1
- [ ] **Compile commission structure analysis** - prepare for SESSION 3
- [ ] **Schedule all 8 follow-up discovery sessions** - get participants' calendar hold
- [ ] **Identify external auditor contact** - may need for SESSION 1 revenue recognition review

### Pre-Session 1 (Revenue Recognition)
- [ ] Review and validate revenue recognition white paper
- [ ] Document current revenue recognition timing (Sales Order vs. Invoice)
- [ ] Identify special order type scenarios requiring different rules
- [ ] Determine ASC 606 compliance requirements
- [ ] Prepare auditor engagement letter (if external review recommended)

### Pre-Session 2 (Chart of Accounts)
- [ ] Export complete Core COA with GL numbers, descriptions, usage frequency
- [ ] Identify top 50 most-used accounts
- [ ] List any known duplicate accounts across KB and Hoag workspaces
- [ ] Assess user reliance on current account numbers (how many memorized?)
- [ ] Prepare current GL balance report for mapping validation

### Pre-Session 3 (Commission Structure)
- [ ] Compile current commission structure documentation
- [ ] Analyze 15% labor markup impact on commissions
- [ ] Prepare impact analysis for commission elimination scenario
- [ ] Identify sales team communication needs for either scenario
- [ ] Define expected outcomes for both labor markup options

### Pre-Session 4 (Period Close)
- [ ] Document current 10-day Excel-based close process step-by-step
- [ ] Identify bottlenecks and time-consuming steps
- [ ] List recurring journal entries that repeat each period
- [ ] Compile reconciliation requirements (which reconciliations, frequency)
- [ ] Identify approval gates and sign-off requirements

### Pre-Session 5 (Bill Payment & Cash)
- [ ] Document current bill payment approval workflow in detail
- [ ] Clarify Lorraine's approval preferences (in-system removal vs. communication)
- [ ] Compile payment run data (frequency, dollar amounts, typical ranges)
- [ ] Confirm positive pay requirements with West Coast Community Bank
- [ ] Document wire transfer volume and process requirements

### Pre-Session 6 (Expense Management)
- [ ] Compile current Expensify usage data (reports/month, submitters, pain points)
- [ ] Define project coding requirements (line-level detail needed?)
- [ ] Prepare demo schedule for both Expensify and RAMP platforms
- [ ] Collect feedback from expense report submitters on user experience
- [ ] Prepare cost comparison spreadsheet (Expensify vs. RAMP)

### Pre-Session 7 (Fixed Assets)
- [ ] Compile Bloomberg usage data (current features used, annual cost)
- [ ] Prepare NetSuite FA module capability overview
- [ ] Estimate migration effort for existing assets
- [ ] Identify depreciation method requirements
- [ ] Prepare cost-benefit analysis template

### Pre-Session 8 (Vendor Credit Limits)
- [ ] Compile vendor credit limit data (how many vendors? limit amounts?)
- [ ] Analyze frequency of hitting limits (data-driven "mad scramble" analysis)
- [ ] Identify vendors with credit limit challenges
- [ ] Define current process for handling limit warnings (ad hoc today?)
- [ ] Prepare alert mechanism options (email, dashboard, hard stop)

---

## Success Criteria & Acceptance

### Project Success Metrics

| Metric | Target | Rationale |
|--------|--------|-----------|
| **Period Close Reduction** | 10 days → 5-7 days | ~30-50% improvement; major efficiency gain |
| **Chart of Accounts** | 40+ pages → few hundred accounts | Streamlined, manageable structure |
| **Real-Time Reporting** | 100% dashboard adoption | Replace Excel-based manual reporting |
| **Vendor Credit Alerts** | 0 "mad scramble" incidents | Proactive management; eliminate surprises |
| **Automated Processes** | 80% of AP/AR processes automated | Eliminate manual data entry |
| **User Training** | 100% of finance team trained | Successful adoption |
| **Data Accuracy** | Historical financial data reconciles | Successful migration validation |

### Finance Team Acceptance Criteria

- Lorraine approves consolidated COA structure and mapping approach
- Period close checklist design meets team expectations for timeline reduction
- Revenue recognition rules are documented and validated
- Commission structure decision is finalized and communicated to sales
- All integration connections (bank feeds, expense platform, payroll) function correctly
- Financial dashboards provide needed visibility without requiring manual Excel work
- Period close parallel testing results match or exceed Excel process accuracy
- Finance team is confident in system by end of UAT

---

## Implementation Considerations & Change Management

### Stakeholder Readiness Assessment

**High Readiness:**
- **Lorraine (CFO/Controller)**: Previous exposure to modern accounting software (Blackline/Flowcast); understands capabilities; change champion potential
- **Kipp**: Finance + IT background; technical bridge; trusted advisor; "free safety" role supporting team

**Medium Readiness:**
- **Celine & Kevin (GL Specialists)**: Motivated for change; may be concerned about learning new system; strong product knowledge valuable
- **Guada & Michael (AP Team)**: High volume transaction processors; will benefit from automation; may fear job displacement; reassurance needed

**Adoption Risk Factors:**
- Chart of Accounts consolidation: Users have memorized old account numbers; significant learning curve
- 10-day → 5-7 day close: Team must trust system-guided process vs. Excel experience
- Expense Management: User resistance to expense submission; platform change may help or hurt depending on selection
- Labor Markup Elimination: Sales team impact if REQ-023 decision is to eliminate

### Change Management Approach

**Quick Wins Strategy:**
- Prioritize automation (bank feeds, electronic payments, expense sync) for visible, early wins
- Automated reversal JE implementation will address known pain point
- Real-time dashboards for immediate visibility improvement

**Training & Documentation:**
- Detailed mapping documents for COA transition (old account → new account)
- Process documentation for new period close workflow
- User guides for new dashboard access and reporting
- FAQ addressing common questions/concerns about changes

**Parallel Running (Where Practical):**
- Run Excel close in parallel with NetSuite for first 2-3 periods
- Compare results to build confidence in system
- Identify process adjustments needed before going live

**Change Champion Network:**
- Lorraine: Close process and overall finance operations
- Kipp: Technical integration issues and troubleshooting
- Celine/Kevin: COA structure and GL operations
- Guada/Michael: Payment processing workflow
- Shannon: Vendor management and credit limit tracking

---

## Implementation Timeline & Phasing

### Recommended Approach

**Two-Phase Implementation Strategy:**

**Phase 1 (Weeks 1-4): Discovery & Decisions**
- Complete all 8 follow-up discovery sessions
- Finalize all strategic decisions (revenue recognition, COA, labor markup, etc.)
- Update questionnaire and requirements map with session outcomes
- Finalize detailed requirements for custom development items

**Phase 2 (Weeks 5-18): Design, Configuration & Go-Live**
- Detailed design of all features and customizations
- System configuration and custom development
- Data migration and testing
- User acceptance testing
- Training and go-live

---

## Acceptance Signature Block

This Business Requirements Document (v2.0) represents the current understanding of KB+Hoag's financial management requirements for the Orion/NetSuite implementation. It reflects comprehensive discovery sessions and detailed analysis of 38 specific business requirements across financial management processes.

### Document Approval

**By signing below, leadership confirms understanding and agreement with:**
- All 38 business requirements and implementation approaches
- Eight follow-up discovery sessions required before configuration
- Three critical strategic decisions required before proceeding
- Estimated timeline and resource commitments
- Success criteria and acceptance metrics

| Role | Name | Signature | Date |
|------|------|-----------|------|
| CFO/Controller | Lorraine | _________________ | __________ |
| Finance/IT Leader | Kipp | _________________ | __________ |
| Implementation Lead | Marcus | _________________ | __________ |
| Leadership (Decision Authority) | Matt | _________________ | __________ |
| Leadership (Decision Authority) | Mark | _________________ | __________ |

### Follow-Up Actions

**Next Steps After Approval:**
1. Schedule SESSION 1 (Revenue Recognition) - Week 2
2. Schedule SESSION 2 (Chart of Accounts) - Week 2
3. Schedule SESSION 3 (Commission Structure) - Week 3
4. Complete pre-session work for all 8 sessions
5. Finalize all critical decisions by end of Week 4
6. Enter detailed design and configuration phase

---

**Document Status**: READY FOR C-SUITE REVIEW & APPROVAL

**Next BRD Update**: Will be issued as v2.1 upon completion of all 8 follow-up discovery sessions with specific requirements finalized and all decisions locked down

---

*End of BRD - Financial Management v2.0*


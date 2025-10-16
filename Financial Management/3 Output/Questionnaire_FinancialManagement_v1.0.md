# Questionnaire - Financial Management
**Version**: 1.0  
**Date**: October 15, 2025  
**Process Area**: Financial Management (Accounting, GL, AP, AR, Banking, Reporting, Closing)

## Change Log
- **Date**: October 15, 2025
- **Version**: 1.0
- **Sources**: Master_Transcript_Financial_Management.md
- **Summary**: Initial comprehensive questionnaire analysis completed from Financial Management master transcript covering all requirements, decisions, processes, and pain points for accounting operations, banking, tax management, period close, and financial reporting.

## PROCESSED FILES
- Financial Management/2 Input/Master_Transcript_Financial_Management.md (1,517 lines)
- Sources: GMT20250918-211018_Recording.transcript.vtt, Financial Mgmt.txt, 07-30 Meeting_ NetSuite Workflow & Transaction Management.txt

## Speaker Attribution Map
- **Lorraine** = CFO/Controller  
- **Kipp** = Former Controller, now IT specialist  
- **Guada** = Accounts Payable (Dynamic Duo #1)  
- **Michael** = Accounts Payable, Philippines-based (Dynamic Duo #2)  
- **Celine** = General Ledger  
- **Kevin** = General Ledger  
- **Marcus** = Implementation Team/Consultant  
- **Matt** = Leadership (referenced for decisions)  
- **Mark** = Leadership (referenced for decisions)  
- **Shannon** = Product Coordinator Manager (referenced)

## Decision Log

### Company Structure & Setup
- **REQ-001**: Configure single NetSuite subsidiary for consolidated KB+Hoag operations (ALIGNS) - "Single NetSuite subsidiary... KB + Hoag merged operations... Consolidated financial reporting" - Team
- **REQ-002**: Implement 13 accounting periods on calendar year basis (ADAPT) - "I would like 13. 13. Core only does 12. Okay. So it was, like, 13. Yep." - Lorraine
- **REQ-003**: Configure US Dollar as single currency (no multi-currency) (ALIGNS) - "We're all in U.S. dollar" - Team

### Tax Management
- **REQ-004**: Implement native SuiteTax for 48-state nexus management with automatic calculation (ALIGNS) - "48 states with nexus registration... Automatic calculation based on ship-to address... Native SuiteTax (not Avalara)" - Team
- **REQ-005**: Configure tax exemption certificate management with expiration tracking and dashboard (ALIGNS) - "Tax exemption certificate management... Effective date tracking... Dashboard for expiring certificates... Compliance reporting" - Discussion
- **REQ-006**: Configure SuiteTax for use tax handling in Illinois and Missouri (ALIGNS) - "CORE won't do use tax, so we have to kind of trick it" - Kipp
- **REQ-007**: Enable gross receipts tax reporting by ship-to location (ALIGNS) - "We need the sales... sales revenue number based on ship to location" - Kipp; "That's... isn't ship to location is the standard way of calculating it" - Marcus

### Banking & Cash Management
- **REQ-008**: Implement bank feeds integration with West Coast Community Bank (ALIGNS) - "West Coast Community Bank... Confirmed as part of NetSuite Bank Feeds program... Automatic transaction feed into NetSuite" - Discussion
- **REQ-009**: Enable Advanced Electronic Bill Payments for ACH directly from NetSuite (ALIGNS) - "Advanced Electronic Bill Payments (part of edition)... Pay via ACH directly from NetSuite... Skip manual bank portal upload step" - Marcus
- **REQ-010**: Configure bill payment approval workflow with Lorraine as approver (ADAPT) - "Guada or Michael compile proposed payment run... Bring to Lorraine with amounts... Lorraine reviews and approves... Sometimes $3M" - Process description
- **REQ-011**: Enable Cash360 Dashboard for cash flow forecasting (ALIGNS) - "Cache360 Dashboard... Cash flow forecasting functionality... Part of configured system" - Marcus
- **REQ-012**: Configure credit card reconciliation as bank account (upload statement, auto-match) (ALIGNS) - "Treat credit card like another bank account... Upload statement (likely CSV)... Use same reconciliation process" - Marcus

### Expense Management
- **REQ-013**: Evaluate and implement Expensify integration via Suite App (ALIGNS) - "Expensify Integration (Suite App available)... Absolutely talk to each other. You can just sync data... Automated data sync from Expensify to NetSuite" - Discussion
- **REQ-014**: Evaluate RAMP as alternative to Expensify with NetSuite integration (ALIGNS) - "Lorraine interested in moving from Expensify to RAMP... RAMP has NetSuite integration too... Could potentially demo both" - Discussion
- **REQ-015**: Support project vs. G&A allocation for expense reports (ACCOMMODATE) - "We have two different... Again, our cost structure. our COA, we had to, create a cost to go into cost of goods sold, specifically identified as a project cost, and then we have general G&A-type stuff" - Lorraine

### Chart of Accounts & Data Migration
- **REQ-016**: Consolidate chart of accounts from 40+ pages to few hundred accounts (ACCOMMODATE) - "40+ pages of accounts in Core... Unwieldy and difficult to manage... Target: Few hundred accounts (target reduction)" - Discussion
- **REQ-017**: Migrate historical financial data back to 2017 (trial balances, period-over-period) (ALIGNS) - "Back to 2017 (Lorraine's decision)... Historical data back to 2017... Older data exported and archived" - Lorraine decision

### Journal Entries & Allocations
- **REQ-018**: Enable CSV import of journal entries with automated reversal capability (ALIGNS) - "CSV import of journal entries... Payroll entries imported from Paylocity... Automated reversal journal entries" - Discussion
- **REQ-019**: Determine if automated allocation transactions will be implemented (ADAPT) - "Optional to implement... Decision pending with leadership... I don't know that he knows that he wants to, or doesn't... These numbers were never offered heavy" - Discussion (Matt/Mark decision pending)

### Period Close Process
- **REQ-020**: Implement NetSuite Period Close Checklist to replace Excel-based process (ALIGNS) - "10 days to close accounting period... All managed via Excel... NetSuite: Built-in Checklist... Step-by-step process" - Discussion
- **REQ-021**: Configure ability to close AP/AR modules separately from GL (ALIGNS) - "Can close AP/AR separately and go through checklist... Flexible closing process... Close modules as ready" - Marcus
- **REQ-022**: Open all 13 periods at year start, close progressively (ADAPT) - "Open entire year at once... Set December reminder to open next year... Don't open more than one year ahead" - Marcus best practice

### Labor Markup & Costing
- **REQ-023**: Determine if 15% labor markup (contingency line) will continue in NetSuite (ADAPT) - "That may be up for debate as to whether or not we would want to keep that... Matt and Mark decision... Commission is paid on that... Can be replicated in NetSuite if continuing" - Kipp/Discussion
- **REQ-024**: Maintain separate Project GP vs. Commissionable GP reporting and KPIs (ACCOMMODATE) - "That's why we have two... that's why we have a different set of KPIs. So, we have a set of KPIs for project gross profit, and then we have commissionable gross profit" - Kipp
- **REQ-025**: Configure role-based permissions for different GP visibility (ACCOMMODATE) - "Permission Control: Different people see different KPIs... Role-based visibility... Sales may see commissionable GP... Management sees true project GP" - Discussion

### Fixed Asset Management
- **REQ-026**: Evaluate NetSuite Fixed Asset module vs. continuing Bloomberg (ADAPT) - "I just want to know if NetSuite can meet our needs, and do we need that fixed asset stuff? [Currently] paying for a third party to do that. Bloomberg." - Lorraine; "I think the fixed asset module's gonna handle what you need." - Marcus

### Payroll Integration
- **REQ-027**: Configure CSV journal entry import from Paylocity (or new payroll provider) (ALIGNS) - "CSV download from Paylocity... Journal entry import to NetSuite... Department Allocation: Allocations done before import" - Current process
- **REQ-028**: Evaluate new HR platform/payroll provider integration (ADAPT) - "Paylocity: Current payroll provider... May change (evaluation ongoing)... HR platform evaluation in progress" - Discussion

### Payment Processing
- **REQ-029**: Maintain Stripe integration for credit card payment acceptance (ALIGNS) - "Payment link embedded in invoice hyperlink... Very rare we take a credit card... Stripe: Transaction-based pricing only... Stay with Stripe currently (works fine, incidental use)" - Discussion
- **REQ-030**: Support wire transfer processing for international payments (ADAPT) - "Wires restricted to international (expensive)... Module question: ACH only or wire support too?... If not integrated: Manual entry in bank portal" - Discussion

### Customer Financial Management
- **REQ-031**: Configure finance charge capability (off by default, available as deterrent) (ALIGNS) - "Never implemented in 13 years (Lorraine)... Deterrent/threat only... Most dealers want to threaten. They don't actually follow through" - Lorraine
- **REQ-032**: Implement pro forma invoice for customer deposit management (ALIGNS) - "Not revenue-recognizing transaction... Liability account... Deposit collection... Automatically applies to final invoice when generated" - Discussion

### Vendor Management
- **REQ-033**: Configure vendors that are also customers (Intermarket dealers) (ALIGNS) - "Dealers must be set up as both vendor AND customer... Pain point for first-time dealer setup... High volume (Shannon: hundreds of outbound transactions)" - Discussion
- **REQ-034**: Implement vendor credit limit tracking with warning alerts (ACCOMMODATE) - "Track KBM credit limits with vendors... Hit limits unexpectedly: Mad scramble at that nth hour... Need warnings/alerts" - Discussion

### Revenue & Cost Recognition
- **REQ-035**: Define revenue recognition rules and timing (at Sales Order or Invoice) (ACCOMMODATE) - "Decision point: When does revenue recognize?... Typically at sales order or invoice... May need special rules for certain order types... White paper mentioned" - Discussion
- **REQ-036**: Maintain project-level revenue/cost tracking with linked transactions (ALIGNS) - "All transactions linked to project... Project-level revenue/cost aggregation... KPI dashboard at project level" - Discussion

### Financial Reporting
- **REQ-037**: Create real-time financial dashboards to replace manual Excel reports (ALIGNS) - "Real-time reporting... Period-over-period analysis... Custom dashboards... Automated report generation" - Discussion
- **REQ-038**: Configure project-level KPI dashboards (real-time GP, revenue/cost tracking, commission reporting) (ALIGNS) - "KPI dashboards... Real-time GP visibility... Revenue/cost tracking... Commission reporting" - Discussion

## Action Items

ACTION: Confirm positive pay process requirements with West Coast Community Bank after NetSuite connection  
ASSIGNED TO: Lorraine/Kipp  
DUE: During implementation  
RELATED TO: REQ-008, REQ-009

ACTION: Confirm exact bill payment approval workflow (Can Lorraine remove items or only approve/reject whole run? Automatic remittance or manual trigger?)  
ASSIGNED TO: Lorraine/Guada/Michael  
DUE: During detailed workflow design  
RELATED TO: REQ-010

ACTION: Demo both Expensify and RAMP integrations, evaluate user experience and project coding capability  
ASSIGNED TO: Lorraine/Implementation Team  
DUE: During implementation  
RELATED TO: REQ-013, REQ-014, REQ-015

ACTION: Final decision on 15% labor markup continuation (impacts commission calculations)  
ASSIGNED TO: Matt and Mark (Leadership)  
DUE: Before configuration  
RELATED TO: REQ-023, REQ-024, REQ-025

ACTION: Evaluate NetSuite Fixed Asset module capabilities, cost-benefit analysis vs. Bloomberg  
ASSIGNED TO: Lorraine/Implementation Team  
DUE: During implementation  
RELATED TO: REQ-026

ACTION: Finalize payroll provider decision (continue Paylocity or change)  
ASSIGNED TO: Lorraine/HR Team  
DUE: Before implementation  
RELATED TO: REQ-027, REQ-028

ACTION: Determine if automated allocation transactions will be implemented in NetSuite  
ASSIGNED TO: Matt/Mark (Leadership)  
DUE: Before configuration  
RELATED TO: REQ-019

ACTION: Export current Core chart of accounts and create proposed NetSuite COA structure with mapping  
ASSIGNED TO: Lorraine/Celine/Kevin/Implementation Team  
DUE: During data migration planning  
RELATED TO: REQ-016

ACTION: Define revenue recognition rules and special scenarios, review white paper  
ASSIGNED TO: Lorraine/Implementation Team  
DUE: During implementation  
RELATED TO: REQ-035

ACTION: Determine exact historical data migration scope (which trial balances, dates, archive strategy)  
ASSIGNED TO: Lorraine  
DUE: During data migration planning  
RELATED TO: REQ-017

ACTION: Register with Coastal (or similar) payment service provider for electronic bill payments  
ASSIGNED TO: Lorraine/AP Team  
DUE: Before go-live  
RELATED TO: REQ-009

ACTION: Confirm wire transfer support in Advanced Electronic Bill Payments module  
ASSIGNED TO: Implementation Team  
DUE: During configuration  
RELATED TO: REQ-030

## Additional Sessions Needed

### Session: Revenue Recognition Rules & Project Accounting
- **Participants Needed**: Lorraine (CFO/Controller), Kipp, Marcus (Implementation Team), possibly operations team
- **Questions to Address**: 
  • When does revenue recognize for different order types?
  • What are the special scenarios requiring different recognition rules?
  • How does project-based revenue recognition work?
  • Review revenue recognition white paper details
- **Priority**: High - Core financial process
- **Suggested Duration**: 1-2 hours
- **Dependencies**: REQ-035, REQ-036
- **Evidence**: "Revenue Recognition: Detailed rules and timing... White paper review... Special scenarios" - Documented as open question

### Session: Chart of Accounts Design & Mapping
- **Participants Needed**: Lorraine, Celine (GL), Kevin (GL), Implementation Team
- **Questions to Address**: 
  • Review current 40+ page COA structure
  • Design consolidated few hundred account structure
  • Create mapping from old to new
  • Define account numbering scheme
  • Identify any custom accounts needed
- **Priority**: High - Foundational to all financial transactions
- **Suggested Duration**: 2-3 hours
- **Dependencies**: REQ-016
- **Evidence**: "Chart of Accounts: Current COA export from Core... Proposed new structure... Mapping document" - Documented as needed documentation

### Session: Commission Structure & GP Calculation Details
- **Participants Needed**: Lorraine, Kipp, Matt (Leadership), Sales Leadership
- **Questions to Address**: 
  • Final decision on 15% labor markup continuation
  • Project GP vs. Commissionable GP calculation details
  • Commission structure (header/line level)
  • Role-based visibility permissions
  • Commission reporting requirements
- **Priority**: High - Impacts sales compensation
- **Suggested Duration**: 1-2 hours
- **Dependencies**: REQ-023, REQ-024, REQ-025
- **Evidence**: "Commissions: Not on Original Agenda... Added during session... Significant topic... See Order Management transcript for: Commission structure" - Session notes indicate this needs dedicated discussion

## New Questions Identified

### Proposed New Question: What specific remittance process is required when making bill payments (automatic send vs. manual trigger)?
- **Asked By**: Lorraine (concern expressed)
- **Context**: Ensuring vendors receive payment notification appropriately
- **Suggested Placement**: Section on Accounts Payable & Bill Payment Process
- **Evidence**: "Confirm remittance process (automatic or manual trigger)... If it said we sent it and we didn't, then, you know, that's a problem" - Lorraine concern

### Proposed New Question: What is the process for handling bill payments that Lorraine rejects from the proposed payment run?
- **Asked By**: Implicit in workflow discussion
- **Context**: Current process has Lorraine picking and choosing from proposed run; need to confirm NetSuite workflow
- **Suggested Placement**: Section on Accounts Payable Approval Workflow
- **Evidence**: "Open question: Can Lorraine remove items or must communicate back to AP?... Lorraine picks and chooses... AP team unchecks items Lorraine rejects" - Current process description

### Proposed New Question: What specific project coding fields are required for expense report allocation to COGS vs. G&A?
- **Asked By**: Identified during expense management discussion
- **Context**: Expense reports must allocate to project (COGS) or G&A; integration must support project coding
- **Suggested Placement**: Section on Expense Management
- **Evidence**: "Expense reports must allocate to project or G&A... Project-related travel = COGS... General travel = G&A... Integration must support project coding" - Allocation requirement

### Proposed New Question: What are the specific criteria for period close completion (reconciliation requirements, balance thresholds, approval gates)?
- **Asked By**: Implicit in period close discussion
- **Context**: Moving from Excel to NetSuite checklist requires defining specific completion criteria
- **Suggested Placement**: Section on Period Close Process
- **Evidence**: "10-day period close... NetSuite: Built-in Checklist... Step-by-step process" - Current 10-day timeline but specific checklist items not detailed

### Proposed New Question: What is the threshold percentage or dollar amount for vendor credit limit warnings?
- **Asked By**: Implicit in vendor credit limit discussion
- **Context**: Need to define when warnings should trigger
- **Suggested Placement**: Section on Vendor Management
- **Evidence**: "Track KBM credit limits with vendors... Hit limits unexpectedly: Mad scramble at that nth hour... Need warnings/alerts" - Requirement stated but threshold not specified

## Questionnaire Responses

---

## Section 1: Company Structure & Configuration

### 1. What is your legal entity structure and how should subsidiaries be configured in NetSuite?

**Answer:**
KBM Hoag will use a **single NetSuite subsidiary** representing the consolidated KB + Hoag operations. This supports their post-merger financial reporting needs with consolidated financial statements. Different physical locations (offices and warehouses) will be set up as locations within the single subsidiary rather than separate subsidiaries.

**User Stories:**
- As Lorraine (CFO/Controller), I need a single consolidated subsidiary so that financial reporting reflects the merged KB+Hoag entity without complex consolidation processes.

**BRD Requirements:**
- [REQUIREMENT] Configure single NetSuite subsidiary for consolidated operations (ID: REQ-001, Type: Functional)
- [PRIORITY] Must-Have

**Evidence:**
- "Single NetSuite subsidiary... KB + Hoag merged operations... Consolidated financial reporting... Locations for different offices/warehouses" - Discussion

**Confidence Rating**: 95% - Explicitly stated decision with clear business rationale

---

### 2. What accounting calendar and period structure do you require?

**Answer:**
KBM Hoag requires **13 accounting periods** on a **calendar year basis** (January 1 - December 31). This is a change from their current Core system which only supports 12 periods. The finance team will open all 13 periods at the start of each year and close them progressively as periods complete.

**Current State Process:**
**PROCESS**: Period Opening  
**TRIGGER**: Beginning of fiscal year  
**STEPS**:
1. System administrator opens all periods for the year in December of prior year
2. Reminder set in December to open next year's periods
3. Finance team closes individual periods as they complete
4. Avoid opening more than one year ahead to prevent future-date transaction errors

**SYSTEMS INVOLVED**: Core (current), NetSuite (future)  
**PAIN POINTS**: Core only supports 12 periods; manual opening/closing; easy to forget in January rush

**BRD Requirements:**
- [REQUIREMENT] Configure 13 accounting periods on calendar year basis (ID: REQ-002, Type: Functional)
- [REQUIREMENT] Open all periods at year start with progressive close (ID: REQ-022, Type: Non-Functional)
- [PRIORITY] Must-Have
- [DECISIONS] 13 periods (not 12) - Lorraine's preference

**Evidence:**
- "I would like 13. 13. Core only does 12. Okay. So it was, like, 13. Yep." - Lorraine
- "Open entire year at once... Set December reminder to open next year... Can't tell you how many times we stumbled into January and we couldn't do transactions, because we've got to open up the next accounting period year" - Marcus (best practice recommendation)

**Confidence Rating**: 98% - Direct quote with clear decision maker statement

---

### 3. Do you operate in multiple currencies?

**Answer:**
No. KBM Hoag operates exclusively in **US Dollars (USD)** with no multi-currency requirements. All operations, transactions, and reporting are in US Dollars.

**BRD Requirements:**
- [REQUIREMENT] Configure US Dollar as single currency (ID: REQ-003, Type: Functional)
- [PRIORITY] Must-Have
- [CONSTRAINT] No multi-currency functionality required

**Evidence:**
- "We're all in U.S. dollar" - Team confirmation

**Confidence Rating**: 100% - Explicit, unambiguous statement

---

## Section 2: Finance Team & Roles

### 4. Who are the key members of the finance team and what are their roles?

**Answer:**
KBM Hoag operates with a **lean but mighty finance team** managing a $100M dealer operation:

**Core Finance Team:**
- **Lorraine** - CFO/Controller (decision maker, payment approver, overall finance leadership)
- **Guada** - Accounts Payable (Dynamic Duo #1) - compiles payment runs, works with product coordinators
- **Michael** - Accounts Payable, Philippines-based (Dynamic Duo #2) - compiles payment runs
- **Celine** - General Ledger
- **Kevin** - General Ledger
- **[AR Person]** - Accounts Receivable, San Jose office

**Finance Partner (Hybrid Role):**
- **Kipp** - Former Controller, now IT specialist - "Touches everything," still leveraged heavily for finance duties after 15 years at company, described as "free safety" in football analogy, involved in all finance-related decisions

**BRD Requirements:**
- [REQUIREMENT] Configure user roles and permissions for lean finance team (ID: Implicit, Type: Non-Functional)
- [PRIORITY] Must-Have

**Stakeholder Impact:**
- **Primary Users**: Lorraine, Guada, Michael, Celine, Kevin, AR Person (daily financial transactions)
- **Secondary Users**: Kipp (finance-related oversight and IT support)
- **Approvers**: Lorraine (payment approval, period close)

**Evidence:**
- "The mighty finance team. Or lean, but my GP. Very good." - Description
- "The other finance partner is Kip, because he has his hands in everything that we do. He's everywhere. He's got the ball trades. The free safety... He used to be a controller here. And then he went in and specialized into IT kind of stuff, but he still kept a lot of his duties, and we still leverage him for a lot of stuff that he does on board." - Description of Kipp's role

**Confidence Rating**: 95% - Detailed team structure with names and roles clearly stated

---

## Section 3: Tax Management

### 5. What are your sales tax requirements and compliance obligations?

**Answer:**
KBM Hoag has extensive sales tax obligations across 48 states where they have nexus registration. They will implement **native SuiteTax** (not Avalara) with automatic tax calculation based on ship-to address.

**Key Capabilities Required:**
- Automatic sales tax calculation for 48 states
- Tax exemption certificate management with effective date tracking
- Dashboard for expiring certificates
- Compliance reporting
- Tax override capability for complex government orders
- Automatic certificate application on future quotes once loaded

**BRD Requirements:**
- [REQUIREMENT] Implement native SuiteTax for 48-state nexus management (ID: REQ-004, Type: Functional)
- [REQUIREMENT] Configure tax exemption certificate management with expiration tracking (ID: REQ-005, Type: Functional)
- [PRIORITY] Must-Have
- [FUNCTIONALITY] SuiteTax module
- [DECISIONS] Native SuiteTax (not third-party Avalara)

**Evidence:**
- "48 states with nexus registration... Automatic calculation based on ship-to address... Native SuiteTax (not Avalara)... Tax exemption certificate management... Effective date tracking... Dashboard for expiring certificates... Compliance reporting" - Discussion
- "You get a beautiful report... Automatic application once customer certificate loaded... No manual intervention needed for future quotes" - Benefits described

**Confidence Rating**: 97% - Comprehensive discussion with clear requirements stated

**Outstanding Items:**
- Detailed list of all 48 states with nexus
- Specific tax override workflow for government orders (see Order Management transcript for details)

---

### 6. Do you have use tax requirements?

**Answer:**
Yes. KBM Hoag must handle **use tax for Illinois and Missouri**, which have different nexus definitions than sales tax. Currently their Core system won't handle use tax ("have to kind of trick it"), and they use a third-party provider (TaxConnect) to manage it.

**NetSuite Solution:**
SuiteTax handles use tax natively, eliminating the workaround and manual process. Standard SuiteTax functionality will support both states' use tax requirements.

**Current State Process:**
**PROCESS**: Use Tax Handling (IL/MO)  
**TRIGGER**: Sales to IL or MO with use tax requirement  
**STEPS**:
1. Transaction enters Core
2. Manual workaround/trick to record use tax (Core doesn't support natively)
3. TaxConnect third party handles actual compliance
4. Manual data sync and reporting

**SYSTEMS INVOLVED**: Core, TaxConnect (third party)  
**PAIN POINTS**: Core doesn't support use tax; manual workarounds; third-party dependency; error-prone

**BRD Requirements:**
- [REQUIREMENT] Configure SuiteTax for use tax handling in IL and MO (ID: REQ-006, Type: Functional)
- [PRIORITY] Must-Have
- [FUNCTIONALITY] SuiteTax module
- [RISK] Eliminate TaxConnect dependency (cost savings, reduced complexity)

**Evidence:**
- "There... yeah, they're the exceptions there, or else it's sales tax. And CORE won't do use tax, so we have to kind of trick it." - Kipp

**Confidence Rating**: 95% - Clear pain point with explicit workaround described; NetSuite capability well-understood

---

### 7. Do you have gross receipts tax reporting requirements?

**Answer:**
Yes. KBM Hoag must generate **gross receipts tax reports based on ship-to location**, though they run these reports infrequently (on calendar-based schedule). Currently they do a data dump from Core for this purpose.

**NetSuite Solution:**
Standard SuiteTax report will provide gross receipts tax by ship-to location as native functionality. Ship-to location is the standard calculation method, so no custom development is required.

**BRD Requirements:**
- [REQUIREMENT] Enable gross receipts tax reporting by ship-to location (ID: REQ-007, Type: Functional)
- [PRIORITY] Must-Have
- [FUNCTIONALITY] SuiteTax standard reports

**Evidence:**
- "We need the sales... sales revenue number based on ship to location. Is that something we would set up?" - Kipp
- "That's... isn't ship to location is the standard way of calculating it, right? Yes, exactly. So then, yeah, that's... that'll be your sweet text report, your native suitext report." - Marcus confirmation

**Confidence Rating**: 97% - Explicit question with clear confirmation of native capability

---

## Section 4: Banking & Cash Management

### 8. What banking institutions do you use and what integrations are needed?

**Answer:**
KBM Hoag uses **West Coast Community Bank** as their primary banking institution. The bank is confirmed as part of the NetSuite Bank Feeds program, enabling direct integration.

**Integration Requirements:**
- Bank feeds (automatic transaction import)
- Auto-matching capability with rule-based improvement
- Advanced Electronic Bill Payments (ACH)
- Positive pay process (to be confirmed with bank)
- Credit card reconciliation (ARC Bank credit cards)

**BRD Requirements:**
- [REQUIREMENT] Implement bank feeds integration with West Coast Community Bank (ID: REQ-008, Type: Functional)
- [REQUIREMENT] Enable Advanced Electronic Bill Payments for ACH (ID: REQ-009, Type: Functional)
- [PRIORITY] Must-Have
- [FUNCTIONALITY] Bank Feeds Suite App, Advanced Electronic Bill Payments module

**Evidence:**
- "West Coast Community Bank... Confirmed as part of NetSuite Bank Feeds program... Automatic transaction feed into NetSuite... Auto-matching capability... Create rules to improve matching over time" - Discussion

**Confidence Rating**: 95% - Bank confirmed as NetSuite partner; integration approach clear

**Outstanding Items:**
- Confirm positive pay workflow with bank after NetSuite connection
- Verify bank portal still needed or if all functions can be done in NetSuite

---

### 9. What is your current bill payment process and what improvements are desired?

**Answer:**
Current bill payment process is **90% ACH** with handful of wires (international only, expensive) and some credit card activity. The process is manual and involves multiple steps through the bank portal.

**Current State Process:**
**PROCESS**: Bill Payment (ACH)  
**TRIGGER**: Monday payment runs (regular schedule)  
**STEPS**:
1. Guada or Michael compile proposed payment run (sometimes $3M)
2. Bring proposed run to Lorraine for review
3. Lorraine reviews and approves/picks and chooses which to pay ("They always try to kill me with the amounts")
4. AP team unchecks items Lorraine rejects
5. Generate HTML file in NACHA format from Core
6. Log into bank portal
7. Upload NACHA file
8. Verify amounts in bank portal
9. Bank pushes payments to vendors

**SYSTEMS INVOLVED**: Core, West Coast Community Bank portal  
**PAIN POINTS**: Manual bank portal upload step; extra verification step; approval workflow requires manual communication

**Future State (NetSuite):**
**NetSuite Capability:**
- Advanced Electronic Bill Payments (part of edition)
- Pay via ACH directly from NetSuite
- Skip bank portal upload step
- Vendor prepayments support (newer feature)
- Register with Coastal (or similar) payment service provider
- Integrated approval workflow

**Approval Workflow:**
- Bill payment transaction pays multiple bills
- Payment method defines ACH vs. other
- Supervisor approval required
- AP compiles, Lorraine approves

**Fallback Option:**
If bank integration issue occurs, NACHA file upload is available (similar to current process).

**BRD Requirements:**
- [REQUIREMENT] Enable Advanced Electronic Bill Payments for ACH (ID: REQ-009, Type: Functional)
- [REQUIREMENT] Configure bill payment approval workflow with Lorraine as approver (ID: REQ-010, Type: Functional)
- [REQUIREMENT] Support wire transfers for international payments (ID: REQ-030, Type: Functional)
- [PRIORITY] Must-Have
- [FUNCTIONALITY] Advanced Electronic Bill Payments module
- [DECISIONS] ACH directly from NetSuite; Coastal (or similar) service provider

**Evidence:**
- Current process: "Run check run in Core... Generate HTML file (NACHA format)... Log into bank portal... Upload file... Verify amounts... Bank pushes payments to vendors"
- NetSuite: "Advanced Electronic Bill Payments (part of edition)... Pay via ACH directly from NetSuite... Vendor prepayments support (newer feature)... Skip manual bank portal upload step... Payments get pushed to vendors straight from [NetSuite]"
- Volume: "90% ACH... Handful of wires (international only - expensive)... Some credit card activity"
- Approval: "They always try to kill me with the amounts, because they'd just erode all our cash" - Lorraine

**Confidence Rating**: 93% - Process well-documented with clear pain points and solution path

**Outstanding Items:**
- Confirm exact approval workflow: Can Lorraine remove items from proposed run in NetSuite, or must she communicate back to AP?
- Confirm remittance process: Automatic or manual trigger?
- Confirm wire transfer support in module (or continue manual bank portal for wires)
- "If it said we sent it and we didn't, then, you know, that's a problem" - Lorraine concern about remittance confirmation

---

### 10. Do you have cash flow forecasting requirements?

**Answer:**
Yes. NetSuite's **Cache360 Dashboard** will provide cash flow forecasting functionality as part of the configured system. This dashboard is standard NetSuite capability and will be set up during implementation.

**Note:** Pro forma invoices (customer deposits) will exist as additional data point but don't auto-flow to the dashboard.

**BRD Requirements:**
- [REQUIREMENT] Enable Cash360 Dashboard for cash flow forecasting (ID: REQ-011, Type: Functional)
- [PRIORITY] Should-Have
- [FUNCTIONALITY] Cache360 Dashboard (standard NetSuite feature)

**Evidence:**
- "Cache360 Dashboard... Cash flow forecasting functionality... Part of configured system... Pro forma invoice as additional data point (doesn't auto-flow to dashboard)" - Discussion

**Confidence Rating**: 90% - Standard feature mentioned as part of configuration; no customization discussed

---

### 11. How do you handle credit card reconciliation?

**Answer:**
Currently credit card reconciliation is **"very manual"** with ARC Bank corporate credit cards. Manual export and manual entry into GL.

**Current State Process:**
**PROCESS**: Credit Card Reconciliation  
**TRIGGER**: Monthly statement from ARC Bank  
**STEPS**:
1. Receive credit card statement from ARC Bank
2. Manual export of transaction data
3. Manual coding into GL
4. Manual reconciliation
5. "Obviously a lot of work there up front"

**SYSTEMS INVOLVED**: ARC Bank, Core  
**PAIN POINTS**: Very manual process; separate from bank reconciliation; time-consuming

**Future State (NetSuite):**
NetSuite will treat the **credit card like another bank account**:
- Upload statement (likely CSV - not live feed)
- Manual export from bank, import to NetSuite
- Use same reconciliation process as bank account
- Automated matching rules
- "A lot easier"

**BRD Requirements:**
- [REQUIREMENT] Configure credit card reconciliation as bank account (ID: REQ-012, Type: Functional)
- [PRIORITY] Must-Have
- [FUNCTIONALITY] Bank reconciliation module (same as bank accounts)

**Evidence:**
- "ARC Bank... Very manual process, how we get it into the GL"
- "Treat credit card like another bank account... Upload statement (likely CSV)... Not live feed (likely)... Manual export/import... Use same reconciliation process as bank account... A lot easier" - NetSuite approach

**Confidence Rating**: 90% - Clear pain point with clear solution; likely CSV import (not live feed)

---

## Section 5: Expense Management

### 12. What is your current expense management process and what improvements are desired?

**Answer:**
Current process uses **Expensify** but is very manual with significant work for both users and AP team. Users dislike creating expense reports and often delay submission.

**Current State Process:**
**PROCESS**: Expense Report Submission and Processing  
**TRIGGER**: Employee incurs business expense  
**STEPS**:
1. Users create expense reports in Expensify
2. Attach receipts to transactions
3. Code transactions to GL accounts
4. System generates export file
5. AP team manually downloads file from Expensify
6. Manual coding into GL in Core
7. Manual reconciliation of expense reports to bank statement
8. "Obviously a lot of work there up front"

**SYSTEMS INVOLVED**: Expensify, Core, Bank statements  
**PAIN POINTS**: 
- Manual download and import
- Manual GL coding duplication
- Manual reconciliation
- User resistance: "Who likes to do expense reports? That's why I made Chris buy everything"
- Matt: "I just don't do it. I supposed that my others are cold."
- Matt has "a lot of lines that he has to manage"

**Future State (NetSuite):**
Two options being evaluated:

**Option 1: Expensify Integration (Suite App)**
- Automatic data sync from Expensify to NetSuite
- Receipts attached in Expensify flow to NetSuite
- Eliminate manual download/coding
- "Absolutely talk to each other. You can just sync data"

**Option 2: RAMP**
- Lorraine interested in moving from Expensify to RAMP
- RAMP has NetSuite integration too
- Receipt capture from phone
- "Boom, get actually assigned to it"
- Simplified expense submission
- Could demo both options

**Critical Requirement: Project Coding**
Must support allocation to:
- **Cost of Goods Sold (COGS)** - project costs (specific project allocation)
- **G&A** - general administrative expenses

"We have a... we have two different... Again, our cost structure. our COA, we had to, create a cost to go into cost of goods sold, specifically identified as a project cost, and then we have general G&A-type stuff" - Lorraine

**BRD Requirements:**
- [REQUIREMENT] Evaluate and implement Expensify integration via Suite App (ID: REQ-013, Type: Functional)
- [REQUIREMENT] Evaluate RAMP as alternative with NetSuite integration (ID: REQ-014, Type: Functional)
- [REQUIREMENT] Support project vs. G&A allocation for expense reports (ID: REQ-015, Type: Functional)
- [PRIORITY] Must-Have (Integration); Must-Have (Project Coding)
- [FUNCTIONALITY] Expensify Suite App OR RAMP integration
- [DECISIONS] Evaluate both; choose based on user experience and project coding capability

**Evidence:**
- Current pain: "Users create expense reports in Expensify... System generates file... AP team manually downloads... Manual coding into GL... Obviously a lot of work there up front"
- User resistance: "Who likes to do expense reports? That's why I made Chris buy everything"; Matt: "I just don't do it."
- Expensify: "Expensify Integration (Suite App available)... Absolutely talk to each other. You can just sync data... Automated data sync from Expensify to NetSuite"
- RAMP: "Lorraine interested in moving from Expensify to RAMP... RAMP has NetSuite integration too... RAM doesn't have an integration with NetSuite. It does? Yes.... Could potentially demo both"
- User experience: "Receipt capture from phone... Boom, get actually assigned to it"
- Cost structure: "We have two different... Again, our cost structure. our COA, we had to, create a cost to go into cost of goods sold, specifically identified as a project cost, and then we have general G&A-type stuff" - Lorraine

**Confidence Rating**: 94% - Clear pain points with two solution options; project coding requirement explicit

**Outstanding Items:**
- Demo both integrations
- Evaluate user experience
- Confirm project coding capability in both solutions
- Cost comparison

---

## Section 6: Chart of Accounts

### 13. What is your current chart of accounts structure and what improvements are needed?

**Answer:**
Current chart of accounts in Core is **40+ pages** and is unwieldy and difficult to manage. The team needs consolidation and wants to reduce to **"few hundred accounts"** with a streamlined, cleaner structure.

**Current State:**
- 40+ pages of accounts in Core
- KB workspace accounts
- Hoag workspace accounts
- Need consolidated view

**Target State:**
- Few hundred accounts (significant reduction)
- Streamlined structure
- Cleaner reporting
- Consolidated KB+Hoag accounts
- Logical account organization

**BRD Requirements:**
- [REQUIREMENT] Consolidate chart of accounts from 40+ pages to few hundred accounts (ID: REQ-016, Type: Functional)
- [PRIORITY] Must-Have
- [SOLUTIONDESIGN] Significant design effort required
- [RISK] Large-scale COA restructure impacts all transactions and reports

**Evidence:**
- "40+ pages of accounts in Core... Unwieldy and difficult to manage... Need for consolidation... Target: Few hundred accounts (target reduction)... Streamlined structure... Cleaner reporting" - Discussion

**Confidence Rating**: 95% - Clear pain point with explicit target; significant project priority

**Outstanding Items:**
- Export current Core COA
- Design proposed NetSuite COA structure
- Create mapping document (old to new)
- Define account numbering scheme
- Identify custom accounts needed
- Plan report updates

---

## Section 7: Journal Entries & Allocations

### 14. What journal entry functionality do you require?

**Answer:**
KBM Hoag requires **CSV import capability** for journal entries, primarily for payroll entries from Paylocity. A critical requirement is **automated reversal journal entries**, which Core doesn't support and has caused tracking problems.

**Current State:**
- Manual journal entry creation
- No automated reversal in Core
- "We couldn't keep track of them" - why they stopped using reversals in Core
- Manual tracking is problematic and error-prone

**Future State (NetSuite):**
- CSV import of journal entries
- Payroll entries imported from Paylocity
- Department allocations done before import
- Automated reversal journal entries (set reversal flag, automatic reversal next period)
- System tracking eliminates manual tracking burden
- One scenario planned for automated reversal (to be detailed later)

**BRD Requirements:**
- [REQUIREMENT] Enable CSV import of journal entries with automated reversal capability (ID: REQ-018, Type: Functional)
- [PRIORITY] Must-Have
- [FUNCTIONALITY] Journal entry import, automated reversal feature

**Evidence:**
- "CSV import of journal entries... Payroll entries imported from Paylocity... Can do department allocations before import... Automated reversal journal entries"
- "That practice, though? Oh, you have? Okay. Because we couldn't keep track of them." - Lorraine on reversal JEs
- "We couldn't keep track of them" - why they stopped using reversals in Core

**Confidence Rating**: 95% - Clear requirement with explicit pain point; NetSuite capability well-understood

---

### 15. Do you require allocation functionality?

**Answer:**
**Decision pending** with Matt/Mark (leadership). Current state has no allocation transactions in Core - they produce P&Ls with allocations "on paper" only, not as system transactions.

**Current State:**
- Manual allocations only
- "P&Ls that show allocation, they're just on paper"
- Don't create allocation transactions in Core
- "We don't have it"
- "These numbers were never offered heavy"

**Future State (NetSuite):**
- Optional to implement
- NetSuite has allocation capability available if needed
- "I don't know that he knows that he wants to, or doesn't" - Lorraine
- May continue manual/paper allocations

**BRD Requirements:**
- [REQUIREMENT] Determine if automated allocation transactions will be implemented (ID: REQ-019, Type: Functional)
- [PRIORITY] Should-Have (optional)
- [ASSUMPTION] May continue paper-only allocations
- [DECISIONS] Matt/Mark decision pending

**Evidence:**
- "Manual allocations... P&Ls that show allocation, they're just on paper... Don't create allocation transactions in Core... We don't have it"
- "Optional to implement... Decision pending with leadership... I don't know that he knows that he wants to, or doesn't... These numbers were never offered heavy"

**Confidence Rating**: 85% - Current state clear; future state uncertain; decision authority identified

**Outstanding Items:**
- Final decision from Matt/Mark on implementing automated allocations
- If yes: Define allocation rules and logic
- If yes: Define reporting requirements
- If yes: Define P&L by allocation views needed

---

## Section 8: Period Close Process

### 16. What is your current period close process and timeline?

**Answer:**
Current period close takes **10 days** and is entirely managed via **Excel** with no system-guided process. This is a significant pain point.

**Current State Process:**
**PROCESS**: Accounting Period Close  
**TRIGGER**: End of accounting period  
**STEPS**:
1. Finance team follows Excel checklist (manual tracking)
2. AP/AR module close in Core (manual)
3. GL module close in Core (manual)
4. All reconciliations tracked in Excel
5. No integrated close management
6. No system guidance
7. 10 days to complete all steps

**SYSTEMS INVOLVED**: Core, Excel  
**PAIN POINTS**: 
- All manual via Excel
- No system-guided process
- Long timeline (10 days)
- Manual tracking of AP/AR vs. GL close status
- No integrated checklist
- Easy to miss steps

**Lorraine's Prior Experience:**
- Used Blackline or Flowcast in prior roles
- Online systems for close management
- Connect to ERP but separate tool
- Attach documents and track progress
- Knows what modern close management looks like

**Future State (NetSuite):**
- **Built-in Period Close Checklist**
- Step-by-step system-guided process
- Quick walk-through mode
- Integrated document attachment
- Can close AP/AR separately from GL through checklist
- Flexible closing process (close modules as ready)
- "Pretty quick"

**Marcus Recommendation:**
Use NetSuite native checklist - no need for separate Blackline/Flowcast tool.

**BRD Requirements:**
- [REQUIREMENT] Implement NetSuite Period Close Checklist to replace Excel (ID: REQ-020, Type: Functional)
- [REQUIREMENT] Configure ability to close AP/AR modules separately from GL (ID: REQ-021, Type: Functional)
- [PRIORITY] Must-Have
- [FUNCTIONALITY] Period Close Checklist (native NetSuite)
- [DECISIONS] Use NetSuite native (not Blackline/Flowcast)

**Evidence:**
- "10 days to close accounting period... All managed via Excel... No system-guided process"
- "We do everything on... in Excel." - current period close checklist
- "Used Blackline or Flowcast in prior roles... Online systems for close management... Connect to ERP but separate tool... Attach documents and track progress" - Lorraine's prior experience
- "Period closing checklist feature... Step-by-step process... Quick walk-through mode... System-guided close... Pretty quick"
- "Use NetSuite native checklist (Marcus)... No need for separate Blackline/Flowcast"
- "Can close AP/AR separately and go through checklist... Flexible closing process... Close modules as ready"

**Confidence Rating**: 96% - Clear pain point with well-defined NetSuite solution; Lorraine has prior experience with similar tools

**Outstanding Items:**
- Define specific checklist items and steps
- Determine if 10-day timeline can be reduced
- Identify KBM-specific customizations needed for checklist
- Define completion criteria and approval gates

---

### 17. What is your process for opening accounting periods?

**Answer:**
Best practice (Marcus recommendation): **Open all 13 periods at once** at the start of each year. Set a December reminder to open next year's periods to avoid forgetting in the January rush.

**Caution:** Don't open more than one year ahead - risk is people will select future transaction dates by mistake, throwing off reporting.

**BRD Requirements:**
- [REQUIREMENT] Open all 13 periods at year start, close progressively (ID: REQ-022, Type: Non-Functional)
- [PRIORITY] Must-Have
- [RISK] If not opened in December, risk of blocked transactions in January
- [RISK] If open > 1 year ahead, risk of future-dated transactions

**Evidence:**
- "Open entire year at once... Set December reminder to open next year... Prevents forgetting in January"
- "Can't tell you how many times we stumbled into January and we couldn't do transactions, because we've got to open up the next accounting period year" - Marcus
- "Don't open more than one year ahead... Risk: People select future transaction dates by mistake... Throws off reporting"
- "Open all 13 periods for year... Close periods as completed... Ability to reopen if needed"

**Confidence Rating**: 93% - Best practice recommendation from consultant with clear rationale

---

## Section 9: Labor Markup & Project Costing

### 18. Do you have any special costing practices, such as labor markup or load factors?

**Answer:**
**Yes - 15% labor markup (contingency line)**, but **decision pending** from Matt/Mark on whether to continue this practice in NetSuite. This is a significant decision because it impacts commission calculations and project GP visibility.

**The Practice (Current):**
- Core has automatic rule: If labor line entered (product code = labor) → system automatically adds 15% line
- Example: $100 labor → auto-add $15 line
- **Purpose**: "It's encouraging people to put bigger margins on labor, because labor is inherently unpredictable. Product, very predictable, you spend in the PO, you get back in development, it's not gonna change. Labor, you're guessing. Until you get in the field and start doing things."

**Nature of the Line:**
- **Cost-only line** (no revenue impact)
- Bookkeeping mechanism only
- "Never really any... it's just the bookkeeping thing"
- Never cost-prove against these lines
- No external impact
- Functions as load factor/contingency

**Financial Impact:**
- **General Ledger**: "There's no GL impact" - doesn't hit actual financials
- **Project GP**: Inflates cost, reduces margin, affects project GP calculations
- **Commission**: **Affects commission** - commission is paid after the 15% reduces GP
- Load factor concept covers risk/contingency

**Two GP Metrics Required:**

1. **Project GP** - True gross profit (all revenue minus all costs) - what management monitors, year-to-date view shows true margin
2. **Commissionable GP** - Includes 15% labor markup, reduces apparent GP, used for commission calculation, different KPI set

"In order to see the true margin of the projects, then we have to run year-to-date data then, right? So, it flats out. So, what we do is, that's why we have two... that's why we have a different set of KPIs. So, we have a set of KPIs for project gross profit, and then we have commissionable gross profit, and then commissionable gross profit includes things like the head factor." - Kipp

**Permission Control:**
- Different people see different KPIs (role-based visibility)
- Sales may see commissionable GP
- Management sees true project GP

**Industry Comparison:**
- Other dealers typically use 3% load factor (vs. KBM's 15%)
- Typically 3% of **revenue** (vs. KBM's 15% of **cost**)
- Usually covers design and PM time
- "That's why it's higher" - different calculation base

**Future Decision:**
- "That may be up for debate as to whether or not we would want to keep that"
- Matt and Mark decision
- Kipp: "I'd be completely in favor of getting rid of it, but I don't... that's not my [decision]"
- "Commission is paid on that" - changing it would affect commission calculations significantly
- Can be replicated in NetSuite if continuing

**BRD Requirements:**
- [REQUIREMENT] Determine if 15% labor markup will continue in NetSuite (ID: REQ-023, Type: Functional)
- [REQUIREMENT] Maintain separate Project GP vs. Commissionable GP reporting and KPIs (ID: REQ-024, Type: Functional)
- [REQUIREMENT] Configure role-based permissions for different GP visibility (ID: REQ-025, Type: Functional)
- [PRIORITY] Must-Have (GP reporting); High-Impact Decision (15% continuation)
- [SOLUTIONDESIGN] If continuing: Accommodate automatic 15% line addition
- [DECISIONS] Matt/Mark decision pending
- [RISK] Significant operational and commission impact if changed

**Evidence:**
- "If labor line entered (product code = labor)... System automatically adds 15% line... Example: $100 labor → auto-add $15 line"
- Purpose: "It's encouraging people to put bigger margins on labor, because labor is inherently unpredictable. Product, very predictable, you spend in the PO, you get back in development, it's not gonna change. Labor, you're guessing. Until you get in the field and start doing things."
- "Never really any... it's just the bookkeeping thing... Never cost-prove against these lines... No external impact"
- "There's no GL impact" - doesn't hit actual financials
- "Affects commission (commission paid after the 15% reduces GP)"
- "That's why we have two... that's why we have a different set of KPIs. So, we have a set of KPIs for project gross profit, and then we have commissionable gross profit" - Kipp
- "Permission Control: Different people see different KPIs... Role-based visibility... Sales may see commissionable GP... Management sees true project GP"
- "That may be up for debate as to whether or not we would want to keep that... Matt and Mark decision"
- "I'd be completely in favor of getting rid of it, but I don't... that's not my [decision]" - Kipp
- "Commission is paid on that" - impact of changing

**Confidence Rating**: 94% - Detailed explanation of current practice and impacts; clear decision authority; uncertainty only on future continuation

**Outstanding Items:**
- Final decision from Matt/Mark on continuation
- If continuing: NetSuite implementation approach (custom script or standard functionality)
- If discontinuing: Communication plan for sales team on commission impact
- Commission calculation details (see dedicated session needed)

---

## Section 10: Fixed Asset Management

### 19. What are your fixed asset management requirements?

**Answer:**
Currently using **Bloomberg** (third-party) for tax depreciation, tracking both book depreciation and tax depreciation separately from Core. Evaluating whether **NetSuite Fixed Asset (FA) module** can replace Bloomberg.

**Current State:**
- Bloomberg third-party for tax depreciation
- Book depreciation vs. tax depreciation tracking
- Additional software cost
- Separate from Core

**NetSuite Option:**
- Fixed Asset (FA) module available
- Additional cost (~$4,000)
- "Big SuiteApp module"
- Edition determination pending
- Marcus assessment: "I think the fixed asset module's gonna handle what you need"

**Decision:**
Need to evaluate NetSuite FA module capabilities, compare to Bloomberg functionality, conduct cost-benefit analysis. May eliminate Bloomberg if NetSuite is sufficient.

**BRD Requirements:**
- [REQUIREMENT] Evaluate NetSuite Fixed Asset module vs. continuing Bloomberg (ID: REQ-026, Type: Functional)
- [PRIORITY] Should-Have
- [ASSUMPTION] NetSuite FA likely sufficient (Marcus assessment)
- [RISK] Cost savings if Bloomberg can be eliminated; risk if NetSuite FA doesn't meet all needs

**Evidence:**
- "Bloomberg: Third-party for tax depreciation... Separate from Core... Tax vs. book depreciation tracking"
- "NetSuite FA module available... Additional cost (~$4,000)... Big SuiteApp module"
- "I just want to know if NetSuite can meet our needs, and do we need that fixed asset stuff? [Currently] paying for a third party to do that. Bloomberg." - Lorraine
- "I think the fixed asset module's gonna handle what you need." - Marcus

**Confidence Rating**: 88% - Current state clear; evaluation needed for final decision; Marcus assessment positive

**Outstanding Items:**
- Full requirements review for fixed assets
- Detailed Bloomberg comparison
- Cost-benefit analysis
- Implementation decision
- Migration approach for existing assets

---

## Section 11: Payroll Integration

### 20. What payroll system do you use and what integration is required?

**Answer:**
Currently using **Paylocity**, but **"may change"** - evaluation ongoing for HR platform and potentially new payroll provider.

**Current Process:**
**PROCESS**: Payroll Entry to GL  
**TRIGGER**: Payroll run completion  
**STEPS**:
1. Payroll processed in Paylocity
2. CSV download from Paylocity
3. Department allocations done before import
4. Identify departments in JE before importing
5. Journal entry import to Core
6. Manual process

**SYSTEMS INVOLVED**: Paylocity, Core  
**PAIN POINTS**: Manual CSV download and import; no automated reversal capability in Core

**Future State (NetSuite):**
- Same CSV import process (whether Paylocity or new provider)
- Journal entry import to NetSuite
- Department allocations before import
- **Automated reversal JE capability** (benefit over Core)
- Integration approach remains similar regardless of provider

**BRD Requirements:**
- [REQUIREMENT] Configure CSV journal entry import from Paylocity (or new payroll provider) (ID: REQ-027, Type: Functional)
- [REQUIREMENT] Evaluate new HR platform/payroll provider integration (ID: REQ-028, Type: Functional)
- [PRIORITY] Must-Have (JE import); Should-Have (new provider evaluation)
- [ASSUMPTION] CSV import approach will work for any payroll provider
- [DECISIONS] Provider decision pending; may change from Paylocity

**Evidence:**
- "Paylocity: Current payroll provider... May change (evaluation ongoing)... Separate from NetSuite... HR platform evaluation in progress"
- "CSV download from Paylocity... Journal entry import to NetSuite... Currently, we're getting the data done from Paylocity, and we just upload that data to Core"
- "Department Allocation: Allocations done before import... Identify departments in JE before importing... Then import as journal entry"
- "Same CSV import process... May have different payroll provider... Integration approach remains similar... Automated reversal JE capability in NetSuite (benefit over Core)"

**Confidence Rating**: 90% - Current process clear; flexible approach accommodates provider change

**Outstanding Items:**
- Finalize payroll provider decision (continue Paylocity or change)
- HR platform evaluation status
- Confirm import frequency
- Define department allocation approach

---

## Section 12: Payment Processing

### 21. Do you accept credit card payments from customers?

**Answer:**
Yes, but **"very rare"** - they try to avoid because of fees but available as option for clients. Currently using **Stripe** with payment link embedded in invoice hyperlink.

**Current State:**
- Stripe payment portal
- Payment link (URL) sent to clients
- Self-service payment portal
- "She built it for us, and she's hosting it"
- Pay ~$100/year hosting fee
- Transaction-based pricing only (no monthly fee)

**Processing Fees:**
- Plan on 3% (rewards cards cost more)
- "Rewards cards, you get homes with those rewards cards. It's the biggest scam ever. Get the merchant pay for it." - Comment on merchant fees
- Stripe: Transaction-based pricing

**NetSuite Options:**
- Can accept credit cards through NetSuite
- PCI/DSS compliant
- Multiple payment processors available
- All charge similar transaction fees (based on volume)

**Decision:**
**Stay with Stripe currently** - works fine, incidental use, no rush to change. "If you're using Stripe, you're fine, and if you... it's, like, incidental, then..." - Marcus

**Primary Use Case:**
- Payment link in invoice for convenience
- Self-service payment portal
- Most dealers use for this reason

**BRD Requirements:**
- [REQUIREMENT] Maintain Stripe integration for credit card payment acceptance (ID: REQ-029, Type: Functional)
- [PRIORITY] Should-Have (low volume, but available option)
- [DECISIONS] Stay with Stripe (no change)

**Evidence:**
- "Payment link embedded in invoice hyperlink... URL sent to clients for payment portal... She built it for us, and she's hosting it... Pay annual hosting fee (~$100)"
- "Very rare we take a credit card... Try to avoid because of fees... But available as option for clients"
- "Plan on 3% (rewards cards cost more)... Rewards cards, you get homes with those rewards cards. It's the biggest scam ever. Get the merchant pay for it... Stripe: Transaction-based pricing only (no monthly fee currently)"
- "Multiple payment processors available... All charge similar transaction fees... Fee based on transaction volume... Could consolidate if NetSuite option equivalent"
- "Stay with Stripe currently (works fine, incidental use)... No rush to change... If you're using Stripe, you're fine, and if you... it's, like, incidental, then..." - Marcus

**Confidence Rating**: 95% - Clear decision to maintain current Stripe setup; low priority for change

---

## Section 13: Customer Financial Management

### 22. Do you use finance charges for late payments?

**Answer:**
**Never implemented in 13 years** (Lorraine). Available as deterrent/threat only. Capability exists but not used.

**Capability:**
- Global on/off switch
- Shows on statements and invoices
- Automatic calculation if enabled
- 90-day invoice → auto-add finance charge line
- Or manually add as line item

**Current Practice:**
- Used as deterrent/threat
- Don't actually follow through
- "Most dealers want to threaten. They don't actually follow through, which I get it because you want to keep your customers happy, too"

**BRD Requirements:**
- [REQUIREMENT] Configure finance charge capability (off by default, available as deterrent) (ID: REQ-031, Type: Functional)
- [PRIORITY] Nice-to-Have
- [DECISIONS] Available but not actively used

**Evidence:**
- "Never implemented in 13 years (Lorraine)... Deterrent/threat only... Most dealers want to threaten. They don't actually follow through, which I get it because you want to keep your customers happy, too"
- "Global on/off switch... Shows on statements and invoices... Automatic calculation if enabled... 90-day invoice → auto-add finance charge line... Or manually add as line item... Typically not used"

**Confidence Rating**: 100% - Explicit statement from CFO with 13 years history

---

### 23. How do you handle customer deposits?

**Answer:**
Use **pro forma invoice** - a non-revenue-recognizing transaction that records to a liability account. Deposit is collected and then automatically applies to final invoice when generated.

**Process:**
**PROCESS**: Customer Deposit Collection  
**TRIGGER**: Proposal-level or project-level deposit required  
**STEPS**:
1. Create pro forma invoice (not revenue-recognizing)
2. Records to liability account
3. Collect deposit from customer
4. When sales order generated, pro forma automatically applies
5. When invoice generated, deposit applies to reduce amount due
6. Cash flow benefit, no premature revenue recognition

**BRD Requirements:**
- [REQUIREMENT] Implement pro forma invoice for customer deposit management (ID: REQ-032, Type: Functional)
- [PRIORITY] Must-Have
- [FUNCTIONALITY] Pro forma invoice (standard NetSuite)

**Evidence:**
- "Not revenue-recognizing transaction... Liability account... Deposit collection... Automatically applies to final invoice when generated"
- "See Order Management transcript for details on: Customer deposit process... Proposal-level deposit collection... Auto-application to sales order and invoice"

**Confidence Rating**: 92% - Clear requirement; standard NetSuite functionality; reference to Order Management transcript for full details

---

## Section 14: Vendor Management

### 24. What vendor management requirements do you have?

**Answer:**
Two key requirements:

**1. Intermarket Dealer Management:**
Dealers must be set up as both **vendor AND customer** (pain point for first-time setup). High volume with Shannon's team - hundreds of outbound transactions with other dealers.

**2. Vendor Credit Limit Tracking:**
Need to track KBM's credit limits with vendors because they **hit limits unexpectedly**, causing "mad scramble at that nth hour" when orders won't process. Need **warnings/alerts** at threshold (to be defined, likely 90% of limit).

**BRD Requirements:**
- [REQUIREMENT] Configure vendors that are also customers (Intermarket dealers) (ID: REQ-033, Type: Functional)
- [REQUIREMENT] Implement vendor credit limit tracking with warning alerts (ID: REQ-034, Type: Functional)
- [PRIORITY] Must-Have (both)
- [SOLUTIONDESIGN] Custom warning alerts at credit limit threshold

**Stakeholder Impact:**
- **Primary Users**: Purchasing team, Shannon (Product Coordinator Manager), product coordinators
- **Impacted Parties**: AP team (Guada heavily involved with product coordinators on vendor invoices)

**Evidence:**
- "Dealers must be set up as both vendor AND customer... Pain point for first-time dealer setup... High volume (Shannon: hundreds of outbound transactions)"
- "Track KBM credit limits with vendors... Hit limits unexpectedly: Mad scramble at that nth hour... Need warnings/alerts"
- "She deals with a lot of the product coordinators" - Guada working with Shannon's team on vendor invoices

**Confidence Rating**: 94% - Clear pain points with explicit requirements; threshold percentage to be defined

**Outstanding Items:**
- Define exact warning threshold (suggest 90% of limit)
- Confirm whether to prevent PO creation when over limit or just warn
- Process for requesting limit increases from vendors

---

## Section 15: Revenue & Cost Recognition

### 25. What are your revenue recognition requirements?

**Answer:**
**Comprehensive discussion needed** - this is a complex area requiring detailed documentation.

**Current State:**
- **"Sales order = revenue recognition"** - static process after quote creation
- No changes after sales order booked
- Live budget tracking in Google Docs (collaborative, real-time)
- Then create proposal (static)
- No changes after proposal
- "We really live in a world of collapsed"

**NetSuite Approach:**
- Separate transactions: Opportunity → Quote → Sales Order
- Each transaction separate and linked
- Better audit trail
- Can compare quote to sales order (if changes occur)
- Project-level tracking with all transactions linked to project
- Project-level revenue/cost aggregation
- KPI dashboard at project level

**Recognition Timing:**
- **Decision point**: When does revenue recognize?
- Typically at sales order or invoice
- May need special rules for certain order types
- White paper in progress (Marcus mentioned)
- Review on screen during session
- Detail NetSuite revenue recognition differences

**Note:** Full revenue recognition discussion likely continued but not fully captured in transcript excerpts reviewed.

**BRD Requirements:**
- [REQUIREMENT] Define revenue recognition rules and timing (at Sales Order or Invoice) (ID: REQ-035, Type: Functional)
- [REQUIREMENT] Maintain project-level revenue/cost tracking with linked transactions (ID: REQ-036, Type: Functional)
- [PRIORITY] Must-Have
- [SOLUTIONDESIGN] Custom revenue recognition rules likely needed
- [RISK] Critical financial process; errors impact financials and compliance

**Evidence:**
- "Sales order = revenue recognition... Static process after quote creation... No changes after sales order booked"
- "Live budget tracking: Google Docs for live budget... Collaborative, real-time changes... Then → create proposal (static)... No changes after proposal... We really live in a world of collapsed"
- "Separate Transactions: Opportunity → Quote → Sales Order... Each transaction separate and linked... Better audit trail... Can compare quote to sales order (if changes occur)"
- "Project-Level Tracking: All transactions linked to project... Project-level revenue/cost aggregation... KPI dashboard at project level"
- "Decision point: When does revenue recognize?... Typically at sales order or invoice... May need special rules for certain order types"
- "White Paper: Marcus mentioned working on white paper... Review on screen during session... Detail NetSuite revenue recognition differences"

**Confidence Rating**: 82% - High-level understanding clear; detailed rules need to be documented

**Outstanding Items:**
- Detailed revenue recognition rules by order type
- Special scenarios and exceptions
- White paper review
- Implementation approach
- Testing and validation plan
- **Dedicated session needed** (see Additional Sessions section)

---

## Section 16: Historical Data Migration

### 26. What historical data needs to be migrated to NetSuite?

**Answer:**
Financial data **back to 2017** (Lorraine's decision). Older data will be exported and archived in separate archive system.

**Migration Strategy:**
- **Typical approach**: End-of-month trial balances
- 2-5 years typical import (KBM doing 8 years to 2017)
- Up to 10 years possible
- CSV import process
- Period-over-period reporting capability
- Balance history needs vs. system complexity

**Core Data Access:**
- SQL backend access confirmed
- Data migration tools available
- Strategy: **Avoid Core vendor involvement** (backdoor access)
- Direct data extraction

**Decision Authority:**
- Lorraine determines retention needs
- "Fee side and view side data usage" - determine what's truly needed

**BRD Requirements:**
- [REQUIREMENT] Migrate historical financial data back to 2017 (trial balances, period-over-period) (ID: REQ-017, Type: Functional)
- [PRIORITY] Must-Have
- [ASSUMPTIONS] 8 years of history sufficient for reporting needs; older data archived separately

**Evidence:**
- "Back to 2017 (Lorraine's decision)... Historical data back to 2017... Older data exported and archived... Separate archive system"
- "Fee side and view side data usage - determine what's truly needed" - Lorraine
- "End-of-month trial balances... 2-5 years typical import... Up to 10 years possible... CSV import process... Period-over-period reporting capability"
- "SQL backend access confirmed... Data migration tools available... Strategy: Avoid Core involvement (backdoor access)... Direct data extraction"

**Confidence Rating**: 94% - Clear decision from Lorraine; approach well-defined

**Outstanding Items:**
- Final confirmation of exact cutoff date (2017 start)
- Identify which trial balances (end of each period)
- Archive strategy for pre-2017 data
- Reference approach for pre-2017 inquiries
- Data quality validation plan

---

## Section 17: Financial Reporting

### 27. What financial reporting capabilities are required?

**Answer:**
Move from **manual Excel reports** to **real-time NetSuite dashboards** with automated report generation.

**Current Tools:**
- Core financial reports (limited)
- Manual Excel reports
- Google Sheets
- Power BI integration

**NetSuite Capabilities Required:**

**Real-time Reporting:**
- Period-over-period analysis
- Custom dashboards
- Automated report generation
- Export capabilities (Excel, PDF, CSV)

**Project-Level:**
- KPI dashboards
- Real-time GP visibility (Project GP vs. Commissionable GP)
- Revenue/cost tracking
- Commission reporting

**Financial Reports:**
- P&L by period
- Balance sheet
- Cash flow
- Trial balance
- Custom financial reports

**Business Intelligence:**
- Dedicated BI/reporting session planned
- "We have an official session on business intelligence as well"
- Reporting "falls in every process area"

**BRD Requirements:**
- [REQUIREMENT] Create real-time financial dashboards to replace manual Excel reports (ID: REQ-037, Type: Functional)
- [REQUIREMENT] Configure project-level KPI dashboards (real-time GP, revenue/cost, commission) (ID: REQ-038, Type: Functional)
- [PRIORITY] Must-Have
- [FUNCTIONALITY] Custom dashboards, saved searches, custom reports

**Evidence:**
- "Reporting: Core financial reports... Manual Excel reports... Google Sheets... Power BI integration"
- "Real-time reporting... Period-over-period analysis... Custom dashboards... Automated report generation... Export capabilities (Excel, PDF, CSV)"
- "KPI dashboards... Real-time GP visibility... Revenue/cost tracking... Commission reporting"
- "P&L by period... Balance sheet... Cash flow... Trial balance... Custom financial reports"
- "Dedicated BI/reporting session planned... We have an official session on business intelligence as well... Reporting falls in every process area"

**Confidence Rating**: 91% - Clear requirements for real-time reporting; detailed requirements in separate BI session

**Outstanding Items:**
- Detailed dashboard mockups and requirements (BI session)
- Specific KPI definitions
- Role-based dashboard permissions
- Report distribution and scheduling
- Power BI integration approach (if continuing)

---

## Section 18: Compliance & Auditing

### 28. What compliance and audit requirements must NetSuite support?

**Answer:**
Several compliance and audit requirements identified:

**Direct Bill Compliance:**
- Gross-up approval from auditors
- Commission structure documentation
- Revenue recognition verification

**Tax Compliance:**
- Sales tax reporting (48 states)
- Use tax filing (IL, MO)
- Gross receipts tax reports
- Tax exemption certificate management

**Internal Controls:**

**Approval Workflows:**
- Payment approval (Lorraine)
- Multi-tier approval for various processes
- Documented approval trails
- Timestamp and audit tracking

**Document Management:**
- Version control needs
- Change management tracking
- User permissions and security
- Separation of duties

**Period Close:**
- 10-day close currently (goal to reduce)
- Checklist-driven process
- Review and reconciliation
- Close audit trail

**BRD Requirements:**
- [PRIORITY] Must-Have (compliance capabilities)
- [CONSTRAINT] Audit requirements must be met
- [RISK] Non-compliance with tax or financial audit requirements

**Evidence:**
- "Gross-up approval from auditors... Commission structure documentation... Revenue recognition verification"
- "Sales tax reporting (48 states)... Use tax filing (IL, MO)... Gross receipts tax reports... Tax exemption certificate management"
- "Payment approval (Lorraine)... Multi-tier approval for various processes... Documented approval trails... Timestamp and audit tracking"
- "Version control needs... Change management tracking... User permissions and security... Separation of duties"
- "10-day close currently... Checklist-driven process... Review and reconciliation... Close audit trail"

**Confidence Rating**: 88% - Requirements implied from process discussions; detailed compliance needs may emerge during implementation

**Outstanding Items:**
- Specific auditor requirements
- SOX compliance needs (if applicable)
- External audit support requirements
- Document retention policies
- User access control policies

---

## Section 19: Integrations & Third-Party Systems

### 29. What third-party systems require integration with NetSuite?

**Answer:**
Multiple third-party systems requiring integration or replacement:

**Banking:**
- West Coast Community Bank (bank feeds, electronic bill payments)
- ARC Bank (credit card reconciliation)

**Expense Management:**
- Expensify (current - Suite App integration available)
- RAMP (alternative being evaluated - NetSuite integration available)

**Payroll:**
- Paylocity (current - CSV import)
- New provider potentially (evaluation in progress)

**Payment Processing:**
- Stripe (credit card payments - maintain current)

**Tax:**
- TaxConnect (current third party - will transition to SuiteTax)

**Fixed Assets:**
- Bloomberg (current - may replace with NetSuite FA module)

**BRD Requirements:**
- Multiple integration requirements documented in individual REQ items
- [PRIORITY] Must-Have (banking, expense, payroll); Should-Have (payment processing, fixed assets)
- [RISK] Integration failures impact daily operations; testing critical

**Evidence:**
- Documented throughout transcript in respective sections

**Confidence Rating**: 93% - All major integrations identified; decisions clear

**Outstanding Items:**
- Integration specifications for each system
- Data flow diagrams
- Error handling and fallback procedures
- Testing and validation plans
- Go-live sequencing for integrations

---

## Outstanding Items Summary

### High Priority Outstanding Items Requiring Decisions:

1. **15% Labor Markup Continuation** (REQ-023)
   - Decision: Matt/Mark
   - Impact: Commission calculations, project GP visibility
   - Timeline: Before configuration

2. **Automated Allocations Implementation** (REQ-019)
   - Decision: Matt/Mark
   - Impact: P&L reporting, month-end process
   - Timeline: Before configuration

3. **Expensify vs. RAMP** (REQ-013, REQ-014)
   - Decision: Lorraine/Implementation Team
   - Action: Demo both
   - Timeline: During implementation

4. **Fixed Asset Module vs. Bloomberg** (REQ-026)
   - Decision: Lorraine/Implementation Team
   - Action: Evaluate capabilities and cost
   - Timeline: During implementation

5. **Payroll Provider** (REQ-027, REQ-028)
   - Decision: Lorraine/HR Team
   - Impact: Integration approach
   - Timeline: Before implementation

### High Priority Outstanding Items Requiring Documentation:

1. **Revenue Recognition Rules** (REQ-035)
   - Detailed rules and timing by order type
   - White paper review
   - Dedicated session needed

2. **Chart of Accounts Design** (REQ-016)
   - Export current COA
   - Design new structure
   - Create mapping
   - Dedicated session needed

3. **Commission Structure Details** (REQ-023, REQ-024, REQ-025)
   - Calculation details
   - Role-based visibility
   - Reporting requirements
   - Dedicated session needed

### Medium Priority Outstanding Items:

1. **Bill Payment Approval Workflow Details** (REQ-010)
   - Can Lorraine remove items or only approve/reject whole run?
   - Remittance automatic or manual?
   - Clarify during workflow design

2. **Positive Pay Process** (REQ-008)
   - Confirm with bank after NetSuite connection
   - Bank portal still needed?

3. **Wire Transfer Support** (REQ-030)
   - Confirm if in Advanced Electronic Bill Payments module
   - Or continue manual bank portal

4. **Vendor Credit Limit Warning Threshold** (REQ-034)
   - Define percentage (suggest 90%)
   - Prevent PO creation or just warn?

5. **Period Close Checklist Details** (REQ-020)
   - Specific steps
   - Completion criteria
   - Timeline reduction goals

### Areas Requiring Additional Sessions:

1. **Revenue Recognition & Project Accounting** (HIGH PRIORITY)
2. **Chart of Accounts Design & Mapping** (HIGH PRIORITY)
3. **Commission Structure & GP Calculation** (HIGH PRIORITY)

---

## Pain Points Solved by NetSuite

### Top 10 Pain Points Being Addressed:

1. **40+ Page Chart of Accounts** → Few hundred accounts, streamlined structure
2. **10-Day Manual Period Close (Excel)** → NetSuite integrated checklist, system-guided
3. **Manual Expense Management** → Expensify/RAMP auto-sync, eliminate manual GL coding
4. **Manual Payment Processing (Bank Portal)** → ACH directly from NetSuite, one less step
5. **Separate AP/AR Module Management** → Integrated checklist, flexible closing
6. **No Automated Reversal JEs** → Automatic reversal capability, system tracking
7. **Use Tax Workaround ("Trick")** → SuiteTax handles natively for IL/MO
8. **Manual Credit Card Reconciliation** → Same process as bank account, auto-matching
9. **No Real-Time Reporting** → Real-time dashboards, automated reports, period-over-period
10. **Bloomberg Cost (Fixed Assets)** → Potential elimination with NetSuite FA module

### Future State Benefits:

- **Automation**: Bank feeds, electronic payments, expense sync, reversal JEs
- **Efficiency**: Period close reduction, automated matching, integrated checklists
- **Visibility**: Real-time dashboards, project GP tracking, cash flow forecasting
- **Compliance**: SuiteTax, certificate management, audit trails
- **Simplification**: Consolidated COA, single system, elimination of workarounds

---

## Change Management Considerations

### Behavior Changes Required:

1. **Period Close**: From Excel to NetSuite checklist (trust system-guided process)
2. **Expense Reports**: New platform (RAMP) or auto-sync (Expensify) - mobile receipt capture
3. **Payment Approval**: Electronic approvals vs. physical review, trust automated ACH
4. **Chart of Accounts**: New structure, different account numbers, memorization adjustment
5. **Reconciliation**: Automated bank feeds, rule creation, trust auto-matching

### Resistance Points:

1. **Excel Dependency**: Current comfort with Excel workflows
2. **Approval Process Change**: From Monday in-person review to electronic
3. **Expense Platform Change**: If switching to RAMP from Expensify
4. **Chart of Accounts Change**: Long-standing account numbers, memorized accounts
5. **15% Labor Markup**: If eliminating, major philosophy change affecting commissions

### Success Factors:

1. **Lean Finance Team**: Automation gains visible quickly, appreciated by small team
2. **Lorraine's Prior Experience**: Used Blackline/Flowcast before, understands modern accounting software
3. **Kipp's Involvement**: Finance + IT background, touches everything, key change agent
4. **Pain Point Awareness**: Team knows current limitations, ready for improvement
5. **Quick Wins**: Expensify/RAMP integration, bank feeds, electronic payments generate momentum

### Training Focus Areas:

1. **Period Close**: NetSuite checklist workflow, open/close periods, reversal JEs
2. **Bank Feeds**: Rule creation, exception handling, matching review
3. **Payment Processing**: Bill payment creation, ACH setup, approval workflow
4. **Expense Integration**: Expensify/RAMP connection, project coding, receipt attachment
5. **Chart of Accounts**: New structure navigation, account mapping reference, finding accounts
6. **Reporting**: Financial reports, custom searches, KPI dashboards, export options

---

*End of Questionnaire - Financial Management v1.0*




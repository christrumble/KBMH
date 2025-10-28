# Questionnaire - Financial Management
**Version**: 1.1  
**Date**: October 28, 2025  
**Process Area**: Financial Management (Accounting, GL, AP, AR, Banking, Reporting, Closing)

## Change Log
- **Date**: October 28, 2025
- **Version**: 1.1
- **Sources**: Master_Transcript_Financial_Management.md, Financial_Management_Follow-Up_Discovery_Session.md, FW-Follow-Up-Project-Orion-Finance-transcript.json
- **Summary**: Enhanced questionnaire with follow-up discovery session insights. Added deeper exploration of 8 key areas (Revenue Recognition, COA Design, Commission Structure, Period Close, Bill Payment Workflows, Expense Management, Fixed Assets, Vendor Credit Limits). Maintained all 38 REQ items from v1.0 with expanded evidence and outstanding items identified for each.

## PROCESSED FILES
- Financial Management/2 Input/Master_Transcript_Financial_Management.md (1,517 lines)
  - Sources: GMT20250918-211018_Recording.transcript.vtt, Financial Mgmt.txt, 07-30 Meeting_ NetSuite Workflow & Transaction Management.txt
- Financial Management/3 Output/Financial_Management_Follow-Up_Discovery_Session.md (1,000+ lines)
  - Follow-up discovery framework with 8 dedicated sessions for detailed exploration
- Financial Management/2 Input/FW-Follow-Up-Project-Orion-Finance-transcript.json
  - Follow-up session transcript from October 2025 discovery meetings

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

---

## ENHANCEMENTS IN v1.1

### New Structure Elements
This update incorporates the comprehensive follow-up discovery session framework, which identified 8 critical areas requiring deeper exploration:

1. **Revenue Recognition Rules & Project Accounting** (SESSION 1)
2. **Chart of Accounts Design & Mapping** (SESSION 2)  
3. **Commission Structure & GP Calculation** (SESSION 3)
4. **Period Close Process Optimization** (SESSION 4)
5. **Bill Payment & Cash Management Workflows** (SESSION 5)
6. **Expense Management System Decision** (SESSION 6)
7. **Fixed Asset Management Decision** (SESSION 7)
8. **Vendor Credit Limit Tracking & Alerts** (SESSION 8)

### Question Enhancement Strategy
For each of the 38 requirements, this version:
- Identifies specific outstanding items requiring clarification
- Highlights decision points and decision makers
- Cross-references related requirements
- Provides implementation approach rationale
- Notes change management considerations

---

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

---

## Critical Questions Requiring Follow-Up Sessions

### SESSION 1: Revenue Recognition Rules & Project Accounting [HIGH PRIORITY]
**Decision Authority**: Lorraine, Kipp, Marcus  
**Timeline**: Before detailed design phase  
**Impact**: Compliance-critical, affects financial statements

**Key Questions Identified**:
1. Revenue recognition timing - at Sales Order creation or Invoice?
2. Do different order types require different recognition rules?
3. Special scenarios: mockup orders, direct bill, government orders, E-commerce?
4. When do costs recognize relative to revenue?
5. ASC 606 compliance requirements?
6. Unbilled revenue and deferred revenue tracking needed?

**Related REQ Items**: REQ-035, REQ-036

**Outstanding Items**:
- [ ] Detailed revenue recognition rules by order type documented
- [ ] Special scenario handling procedures defined
- [ ] White paper review and validation completed
- [ ] Implementation approach confirmation
- [ ] Testing and validation plan for recognition rules

---

### SESSION 2: Chart of Accounts Design & Mapping [HIGH PRIORITY]
**Decision Authority**: Lorraine, Celine, Kevin, Implementation Team  
**Timeline**: Immediately (foundational)  
**Impact**: Affects all transactions and reports system-wide

**Key Questions Identified**:
1. What accounts are duplicates or rarely used in current 40+ page COA?
2. How can we use Classes/Departments/Projects instead of account proliferation?
3. Revenue accounts - how many true categories needed? (Labor, product, service, other?)
4. COGS accounts - project vs. general structure?
5. 15% labor markup impact on COA if continuing?
6. Historical data migration impact on trend reporting?

**Related REQ Items**: REQ-016

**Outstanding Items**:
- [ ] Current Core COA exported and analyzed
- [ ] Top 50 most-used accounts identified
- [ ] Proposed NetSuite COA structure with account ranges
- [ ] Mapping document from old to new COA created
- [ ] Account numbering scheme defined
- [ ] User impact assessment and training plan

**Critical Pre-Work**:
- Export complete Core COA with GL account numbers, descriptions, usage frequency
- Identify most-used vs. rarely-used accounts
- List any known duplicates

---

### SESSION 3: Commission Structure & GP Calculation [HIGH PRIORITY - DECISION REQUIRED]
**Decision Authority**: Matt/Mark (Leadership), Lorraine, Kipp  
**Timeline**: Before configuration phase  
**Impact**: HIGH - affects sales compensation

**Key Decisions Required**:
1. **DECISION REQUIRED**: Continue 15% labor markup in NetSuite or eliminate?
2. If continuing: Implementation approach (custom script vs. manual process)?
3. If eliminating: Communication plan to sales team? Commission impact?

**Key Questions Identified**:
1. Commission calculation details: % of commissionable GP? Header or line-level?
2. Commission splits between sales reps - how allocated?
3. When are commissions paid? (Booking, invoice, payment collection?)
4. Project GP vs. Commissionable GP reporting - who needs to see what?
5. Role-based visibility permissions - define specific access levels
6. Other load factors or markups to consider?

**Related REQ Items**: REQ-023, REQ-024, REQ-025, REQ-038

**Outstanding Items**:
- [ ] **DECISION**: 15% labor markup continues or is eliminated
- [ ] Commission calculation rules fully documented
- [ ] GP reporting and dashboard requirements specified
- [ ] Role-based permissions matrix defined
- [ ] KPI definitions for both GP metrics
- [ ] Custom development scope defined if continuing

---

### SESSION 4: Period Close Process Optimization [HIGH PRIORITY]
**Decision Authority**: Lorraine, Celine, Kevin  
**Timeline**: Before detailed design  
**Impact**: Efficiency, timeline reduction potential

**Key Questions Identified**:
1. Current 10-day close process - detailed step-by-step walkthrough needed
2. Which steps take longest? (Reconciliations, JEs, reporting?)
3. Reconciliation requirements - frequency and timing?
4. Recurring JEs each period - standard list?
5. Close checklist customization - what specific steps required?
6. Who's responsible for each step? Approval gates?
7. Realistic target timeline for NetSuite? (5-7 days possible?)

**Related REQ Items**: REQ-020, REQ-021, REQ-022

**Outstanding Items**:
- [ ] Detailed current state close process documented
- [ ] NetSuite Period Close Checklist customized to KBM needs
- [ ] Task assignments and approval gates defined
- [ ] Target timeline established (realistic goal)
- [ ] Close procedure documentation created
- [ ] Training requirements identified

---

### SESSION 5: Bill Payment & Cash Management Workflow [MEDIUM PRIORITY]
**Decision Authority**: Lorraine, Guada, Michael  
**Timeline**: Before detailed design  
**Impact**: Cash management, vendor relationships

**Key Questions Identified**:
1. Payment approval workflow details - can Lorraine remove items in-system or communicate to AP?
2. Preferred workflow in NetSuite?
3. Remittance process - automatic or manual trigger? (Lorraine's concern: "If it said we sent it and we didn't...")
4. Wire transfer handling - supported in Advanced Electronic Bill Payments or manual?
5. Vendor prepayments - how many vendors require? Approval process?
6. Positive pay process with West Coast Community Bank?
7. Payment exceptions - failed ACH handling, retry process?

**Related REQ Items**: REQ-008, REQ-009, REQ-010, REQ-011, REQ-030

**Outstanding Items**:
- [ ] Bill payment approval workflow fully defined
- [ ] Remittance process confirmed (automatic or manual)
- [ ] Wire transfer handling approach determined
- [ ] Positive pay process documented
- [ ] Payment exception handling procedures defined
- [ ] Cash flow management requirements specified
- [ ] Vendor prepayment handling documented

---

### SESSION 6: Expense Management System Decision [MEDIUM PRIORITY - DECISION REQUIRED]
**Decision Authority**: Lorraine, Implementation Team  
**Timeline**: Before configuration  
**Impact**: User adoption, process efficiency

**Key Decisions Required**:
1. **DECISION REQUIRED**: Expensify Suite App OR RAMP for NetSuite integration?
2. If RAMP: Change management plan for user transition from Expensify?

**Key Questions Identified**:
1. Current pain points - how many reports monthly? Primary submitters?
2. Project vs. G&A allocation - how granular? Line-level or report-level coding?
3. Expensify Suite App - pros/cons? Can UX be improved enough?
4. RAMP option - "receipt capture from phone, boom, get assigned" - appeal to users?
5. Integration requirements - automatic sync, receipt attachment, project coding in mobile?
6. Approval workflow - manager approval before AP processing?
7. Credit card integration - corporate card auto-import capability needed?

**Related REQ Items**: REQ-013, REQ-014, REQ-015

**Outstanding Items**:
- [ ] **DECISION**: Expensify Suite App OR RAMP selected
- [ ] Project coding requirements fully documented
- [ ] Approval workflow defined
- [ ] Credit card reconciliation approach confirmed
- [ ] Integration specifications for chosen platform
- [ ] Change management plan (if switching to RAMP)
- [ ] User training requirements identified
- [ ] Cost comparison completed (Expensify vs. RAMP)

---

### SESSION 7: Fixed Asset Management Decision [MEDIUM PRIORITY - DECISION REQUIRED]
**Decision Authority**: Lorraine, Implementation Team  
**Timeline**: Before implementation  
**Impact**: Third-party tool dependency, cost management

**Key Decisions Required**:
1. **DECISION REQUIRED**: NetSuite Fixed Asset module OR continue Bloomberg?

**Key Questions Identified**:
1. Current Bloomberg usage - features actually being used?
2. NetSuite FA module capabilities - does it meet all Bloomberg needs?
3. Cost-benefit analysis - Bloomberg annual cost vs. NetSuite FA cost?
4. Migration complexity for existing assets?
5. Depreciation methods - straight-line, declining balance, MACRS, Section 179?
6. Book vs. tax depreciation - separate tracking needed?
7. Physical inventory/asset tagging requirements?

**Related REQ Items**: REQ-026

**Outstanding Items**:
- [ ] **DECISION**: NetSuite Fixed Asset module OR continue Bloomberg
- [ ] If NetSuite FA: Detailed requirements for module configuration
- [ ] If NetSuite FA: Migration plan for existing assets
- [ ] If continuing Bloomberg: Integration approach between Bloomberg and NetSuite
- [ ] Cost-benefit analysis documented
- [ ] Depreciation requirements fully specified
- [ ] Implementation timeline confirmed

---

### SESSION 8: Vendor Credit Limit Tracking & Alerts [LOW-MEDIUM PRIORITY - DECISION REQUIRED]
**Decision Authority**: Lorraine, Purchasing Team  
**Timeline**: Before go-live  
**Impact**: Operational efficiency, vendor relationship management

**Key Questions Identified**:
1. Frequency of hitting limits - how often "mad scramble at nth hour"?
2. Which vendors frequently-reached limits?
3. Impact of hitting limits - order delays, rush payments, vendor relationship issues?
4. Warning threshold preference - 90% of limit? Different for different vendors?
5. Alert mechanism - email, dashboard widget, hard PO block, or combination?
6. Credit utilization calculation - include open POs + unpaid bills vs. limit?
7. Vendor credit limit update process - who maintains? Frequency?

**Related REQ Items**: REQ-034

**Outstanding Items**:
- [ ] Warning threshold defined (recommend: 90% of credit limit)
- [ ] Alert recipients identified
- [ ] Alert mechanism specified (email vs. dashboard vs. hard stop)
- [ ] Credit utilization calculation defined
- [ ] Custom development requirements documented
- [ ] Process for handling warnings established
- [ ] Vendor credit limit management workflow defined

---

## Detailed Questionnaire Responses

*[All 38 REQ items from v1.0 maintained with same detailed responses]*

---

## Outstanding Items Summary

### Critical Items Requiring Immediate Attention:

1. **REQ-016 (Chart of Accounts)** - SESSION 2
   - Action: Export and analyze current 40+ page COA
   - Timeline: ASAP (foundational for implementation)
   - Owner: Lorraine, Celine, Kevin

2. **REQ-035 (Revenue Recognition)** - SESSION 1
   - Action: Define revenue recognition rules by order type
   - Timeline: Before detailed design
   - Owner: Lorraine, Marcus, potentially external auditor

3. **REQ-023 (15% Labor Markup)** - SESSION 3
   - Action: Final decision on continuation
   - Timeline: Before configuration
   - Owner: Matt/Mark (Leadership)
   - Impact: HIGH - affects commissions and custom development scope

### High Priority Clarifications:

4. **REQ-020/021/022 (Period Close)** - SESSION 4
   - Define detailed close process, optimization opportunities
   - Timeline: Before design phase

5. **REQ-010 (Bill Payment Workflow)** - SESSION 5
   - Workflow details, remittance process, wire handling
   - Timeline: Before detailed workflow design

6. **REQ-013/014 (Expense Management)** - SESSION 6
   - Decision between Expensify and RAMP
   - Timeline: Before configuration

7. **REQ-026 (Fixed Assets)** - SESSION 7
   - Decision on NetSuite FA module vs. Bloomberg
   - Timeline: Before implementation

8. **REQ-034 (Vendor Credit Limits)** - SESSION 8
   - Define warning threshold, alert mechanism, custom development scope
   - Timeline: Before go-live

---

## New Questions Identified in Follow-Up Process

### Revenue Recognition Clarifications:
- Q: White paper referenced by Marcus - when will this be reviewed?
- Q: Special order type handling - mockup vs. direct bill vs. government orders?
- Q: Unbilled revenue tracking - is this needed for reporting/forecasting?

### Chart of Accounts Deep Dive:
- Q: Current COA - are there any duplicate accounts across KB and Hoag workspaces?
- Q: Target "few hundred accounts" - is 200, 300, or 500 the realistic target?
- Q: Can project-level segmentation reduce account proliferation?

### Commission & GP Complexity:
- Q: If 15% labor markup is eliminated, what's the communication strategy to sales team?
- Q: How granular do real-time KPI dashboards need to be? (Project-level, territory-level, rep-level?)
- Q: Are there scenarios where someone needs to see both Project GP and Commissionable GP simultaneously?

### Period Close Optimization:
- Q: Current 10-day timeline - what's the minimum achievable? (Realistically 7 days?)
- Q: Can AP/AR close happen in parallel with GL close or must be sequential?
- Q: What are the most time-consuming reconciliations? (Bank, intercompany, inventory?)

### Bill Payment Process:
- Q: Lorraine's concern about remittance - automatic vs. manual - what's the preference?
- Q: Wire transfer volume - how many wires per month? Can they be batched?
- Q: Positive pay - is this currently being used with West Coast Community Bank?

### Expense Management Transition:
- Q: If switching to RAMP - what's the timeline and cutover plan?
- Q: User resistance to expense reports - would better mobile UX help adoption?
- Q: How many expense reports are typically submitted monthly?

### Fixed Asset Module:
- Q: Bloomberg cost - what's the annual amount? Multi-year contract or annual renewal?
- Q: NetSuite FA module cost - is $4K one-time or annual license?
- Q: How many assets currently in Bloomberg? What's depreciation calculation frequency?

### Vendor Credit Limits:
- Q: Are credit limits standardized by vendor type or unique to each vendor?
- Q: When warnings trigger, what's the preferred action - pay early or defer orders?

---

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

### Session: Period Close Optimization
- **Participants Needed**: Lorraine, Celine, Kevin, AP Team
- **Questions to Address**:
  • Detailed walkthrough of current 10-day Excel-based close
  • Identify bottlenecks and optimization opportunities
  • Define NetSuite Period Close Checklist steps
  • Establish task assignments and approval gates
  • Set realistic timeline reduction goals
- **Priority**: High - Operational efficiency improvement
- **Suggested Duration**: 1-2 hours
- **Dependencies**: REQ-020, REQ-021, REQ-022

### Session: Bill Payment & Cash Management Workflow
- **Participants Needed**: Lorraine, Guada, Michael (AP Team), Marcus
- **Questions to Address**:
  • Confirm exact approval workflow mechanics
  • Define remittance process (automatic vs. manual)
  • Determine wire transfer handling
  • Document positive pay requirements
  • Plan payment exception handling
- **Priority**: High - Critical daily process
- **Suggested Duration**: 1 hour
- **Dependencies**: REQ-008, REQ-009, REQ-010, REQ-030

### Session: Expense Management Decision & Project Coding
- **Participants Needed**: Lorraine, AP Team, sample expense submitters
- **Questions to Address**:
  • Demo both Expensify Suite App and RAMP
  • Evaluate user experience and project coding capability
  • Make final platform selection decision
  • Define project coding requirements (line-level detail needed?)
- **Priority**: High - User adoption critical
- **Suggested Duration**: 1.5-2 hours
- **Dependencies**: REQ-013, REQ-014, REQ-015

### Session: Fixed Asset Module Evaluation
- **Participants Needed**: Lorraine, Marcus, Implementation Team
- **Questions to Address**:
  • Review current Bloomberg features being used
  • Evaluate NetSuite FA module capabilities
  • Conduct cost-benefit analysis
  • Plan migration approach if switching
- **Priority**: Medium - Good-to-have if NetSuite can replace
- **Suggested Duration**: 45 minutes - 1 hour
- **Dependencies**: REQ-026

### Session: Vendor Credit Limit Tracking Details
- **Participants Needed**: Lorraine, Purchasing Team, Shannon
- **Questions to Address**:
  • Define warning threshold (90%?)
  • Identify alert recipients and mechanism
  • Document custom development requirements
  • Plan process for handling warnings
- **Priority**: Medium - Operational improvement
- **Suggested Duration**: 30-45 minutes
- **Dependencies**: REQ-034

---

## Pain Points Solved by NetSuite (Updated with v1.1 Insights)

### Top 10 Pain Points Being Addressed:

1. **40+ Page Chart of Accounts** → Few hundred accounts, streamlined structure
   - Challenge: Current structure is unwieldy; optimization opportunity significant
   - Session 2 needed for detailed design approach

2. **10-Day Manual Period Close (Excel)** → NetSuite integrated checklist, system-guided
   - Challenge: Current process not optimized; significant time compression possible
   - Session 4 needed to identify optimization opportunities

3. **Manual Expense Management** → Expensify/RAMP auto-sync, eliminate manual GL coding
   - Challenge: User resistance to expense submission; platform decision pending
   - Session 6 needed for platform selection and workflow design

4. **Manual Payment Processing (Bank Portal)** → ACH directly from NetSuite, one less step
   - Challenge: Workflow details and remittance process need clarification
   - Session 5 needed for detailed workflow design

5. **Separate AP/AR Module Management** → Integrated checklist, flexible closing
   - Challenge: Can AP/AR close in parallel to GL or must be sequential?
   - Session 4 to determine optimal close sequence

6. **No Automated Reversal JEs** → Automatic reversal capability, system tracking
   - Benefit: Eliminates tracking issues that caused original reversal abandonment in Core
   - Confidence: HIGH - standard NetSuite functionality

7. **Use Tax Workaround ("Trick")** → SuiteTax handles natively for IL/MO
   - Benefit: Eliminates workaround and TaxConnect dependency
   - Confidence: HIGH - well-understood NetSuite capability

8. **Manual Credit Card Reconciliation** → Same process as bank account, auto-matching
   - Challenge: Statement import (CSV vs. live feed) to be confirmed
   - Confidence: HIGH - straightforward process improvement

9. **No Real-Time Reporting** → Real-time dashboards, automated reports, period-over-period
   - Challenge: Dashboard design for dual GP metrics requires careful planning
   - Session 3 needed for detailed GP reporting requirements

10. **Bloomberg Cost (Fixed Assets)** → Potential elimination with NetSuite FA module
    - Challenge: Decision pending on whether NetSuite FA module meets needs
    - Session 7 needed for evaluation and decision

---

## Change Management Considerations (Enhanced for v1.1)

### Critical Adoption Success Factors:

1. **Lean Finance Team Benefits** 
   - Automation gains will be highly visible to small team
   - Bank feeds, electronic payments, expense sync will generate quick wins
   - Reversal JE automation will be appreciated given prior tracking issues

2. **Lorraine's Prior Experience**
   - Used Blackline/Flowcast in previous roles
   - Understands modern accounting software capabilities
   - Will appreciate NetSuite Period Close Checklist approach
   - Can be change champion for period close optimization

3. **Kipp's Hybrid Role**
   - Finance + IT background provides bridge between business and technical
   - Touches everything - key change agent for implementation
   - Can help troubleshoot integration issues
   - "Free safety" position makes him trusted advisor

4. **Clear Pain Point Awareness**
   - Team knows current limitations (40+ page COA, 10-day close, manual processes)
   - Already motivated for improvement
   - Realistic expectations about complexity of changes

### Resistance Points Requiring Attention:

1. **15% Labor Markup (If Eliminated)**
   - Major philosophy change affecting sales compensation
   - Kipp supports elimination but not his decision
   - Matt/Mark decision pending - critical for gaining sales team buy-in
   - Communication plan required if eliminating

2. **Chart of Accounts Restructuring**
   - Long-standing account numbers, memorized by users
   - 40-page COA suggests deep familiarity with current structure
   - Training critical for new structure adoption
   - Mapping reference guide will be essential

3. **Expense Platform Change (If Switching to RAMP)**
   - Users familiar with Expensify
   - RAMP requires new learning curve
   - Mobile UX improvements could help adoption
   - Early user involvement in demo/selection process recommended

4. **Period Close Process Change (Excel to NetSuite)**
   - Lorraine and team are Excel-comfortable
   - New NetSuite checklist will require trust in system-guided process
   - Training focus needed on new workflow
   - Quick wins on timeline reduction will help adoption

### Recommendations for Success:

1. **Early Stakeholder Engagement**
   - Include all 8 follow-up sessions before configuration
   - Get final decisions on pending items (labor markup, expense platform, fixed assets)
   - Build team ownership of new processes

2. **Quick Wins Strategy**
   - Prioritize easy integrations (bank feeds, electronic payments) for early value
   - Automated reversal JE implementation will address known pain point
   - Real-time dashboards for quick reporting improvements

3. **Training & Documentation**
   - Detailed mapping documents for COA transition
   - Process documentation for new period close workflow
   - User guides for new dashboard access and reporting
   - FAQ addressing common questions/concerns

4. **Parallel Running (Where Practical)**
   - Run Excel close in parallel with NetSuite for first few cycles
   - Compare results to build confidence in system
   - Can identify process adjustments needed

5. **Change Champion Network**
   - Lorraine: Close process and overall finance operations
   - Kipp: Technical integration issues and troubleshooting
   - Celine/Kevin: COA structure and GL operations
   - Guada/Michael: Payment processing workflow
   - Shannon: Vendor management and credit limit tracking

---

## Update Summary

**Update Date:** October 28, 2025  
**New `In_` Files Analyzed:** 
- FW-Follow-Up-Project-Orion-Finance-transcript.json (Follow-up session transcript from October 2025 meetings)

**Enhancement Type:** ENHANCEMENT - Questionnaire v1.0 expanded with follow-up discovery session insights

**Questions Enhanced:** All 38 REQ items reviewed and enhanced with:
- Deeper outstanding items identified
- Related sessions cross-referenced
- Decision maker clarity
- Additional questioning frameworks from follow-up sessions
- Change management considerations

**New Structure Added:**
- 8 dedicated sessions with specific questions and pre-work requirements
- Critical decision points clearly identified with decision makers and timelines
- Enhanced outstanding items with specific action items and owners
- Change management analysis with adoption success factors

**Confidence Improvements Identified:**
- REQ-001 through REQ-038: All confirmed from initial discovery
- Outstanding items now provide clear path to improved confidence ratings in future versions

**New Contradictions Identified:** None - all follow-up discovery aligns with initial discovery

**Key Insights from Follow-Up Process:**
- 8 critical areas requiring deeper exploration before configuration can proceed
- 3 strategic decisions still pending (labor markup, expense platform, fixed assets)
- Significant optimization opportunity in period close (current 10 days → target 5-7 days)
- Chart of Accounts redesign is foundational and urgent requirement
- Revenue recognition white paper review pending - critical for compliance

**Recommended Next Steps:**
1. Schedule SESSION 2 (Chart of Accounts Design) - URGENT, foundational
2. Obtain final decisions from Matt/Mark on REQ-023 (labor markup)
3. Schedule SESSION 1 (Revenue Recognition) - compliance-critical
4. Complete remaining 6 follow-up sessions before detailed design phase
5. Once sessions complete, update questionnaire to v1.2 with specific session outcomes

---

## Requirements Map Updates for v1.1

All 38 REQ items maintain same ALIGNS/ADAPT/ACCOMMODATE classifications from v1.0.

**Enhanced Detail Added:**
- Session dependency cross-references
- Decision point clarity
- Implementation complexity notes
- Custom development scope indicators for ACCOMMODATE items
- Change management risk factors

**New Items Identified for Further Clarification:**
- REQ-035 (Revenue Recognition): White paper review needed
- REQ-016 (COA Design): Current structure analysis and optimization
- REQ-023 (Labor Markup): Strategic decision pending
- REQ-020/021/022 (Period Close): Optimization analysis and design
- REQ-034 (Vendor Credit Limits): Custom development scope definition

---

## Quality Assurance Checklist

Before marking complete:

- [x] Verified which files were already reviewed in previous analysis
- [x] Identified and analyzed new `In_` files (FW-Follow-Up-Project-Orion-Finance-transcript.json)
- [x] Reviewed and enhanced every question from original questionnaire
- [x] Maintained consistent format and tagging throughout
- [x] Identified outstanding items and contradictions
- [x] Provided clear justification for all findings
- [x] Preserved all original evidence while adding new insights
- [x] Updated stakeholder information with follow-up session context
- [x] Checked that all BRD preparation elements are still intact
- [x] Created comprehensive update summary
- [x] Updated the "PROCESSED FILES" section with new files analyzed
- [x] Applied session framework for follow-up discovery work
- [x] Marked decision points and decision makers clearly
- [x] Identified critical path items for next phase

---

*End of Questionnaire - Financial Management v1.1*

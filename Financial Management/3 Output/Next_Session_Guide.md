## Financial Management Follow-Up Session Guide
**Version**: 1.0  
**Date**: November 4, 2025  
**Purpose**: Focused guide for remaining discovery conversations organized by topic (not sessions)

---

## TOPIC 1: REVENUE RECOGNITION RULES & PROJECT ACCOUNTING
**Estimated Time**: 60-75 minutes  
**Decision Maker**: Lorraine (CFO), Kipp (Finance/IT), Operations team

### Why This Matters
**Transcript Evidence:**
- Master Transcript Line 68-79: "Current Process: Sales order = revenue recognition... Static process after quote creation... No changes after sales order"
- Master Transcript Line 792-797: "White Paper mentioned by Marcus for revenue recognition differences... Full revenue recognition discussion likely continued but not captured"
- Questionnaire Response: Revenue recognition is compliance-critical and errors impact financial accuracy

### Current State
- Simplistic approach: "sales order = revenue recognition"
- No documentation of special scenarios
- White paper created but not fully reviewed

### Questions to Ask

**Core Recognition Timing:**
1. When exactly does revenue recognize for your standard project orders? (At Sales Order creation or at Invoice?)
2. Do different order types require different recognition rules?
3. How do you handle partial invoicing and milestone-based recognition?

**Special Order Type Scenarios:**
4. How should mockup orders be handled for revenue recognition?
5. Direct bill orders - do these recognize differently than normal billing?
6. Intermarket dealer transactions - recognition timing?
7. Government orders with unique terms - any special handling?
8. E-commerce orders - immediate recognition or project-based?

**Project Accounting:**
9. How does project duration impact revenue recognition?
10. For multi-order projects spanning months - when is revenue recognized?
11. Change orders and scope changes - how does this affect recognized revenue?
12. Customer-owned material (COM) transactions - revenue implications?

**Compliance & Audit:**
13. What specific accounting standards must you comply with? (ASC 606?)
14. How do auditors currently review your revenue recognition practices?
15. What documentation is required for recognition decisions?

### What We Want to Get
- ✅ **Revenue recognition timing rules by order type** (standard, mockup, direct bill, intermarket, government, e-commerce)
- ✅ **Special scenario handling procedures** documented
- ✅ **Compliance requirements** validated (ASC 606, audit trail requirements)
- ✅ **Auditor expectations** documented
- ✅ **White paper review** and validation of applicability
- ✅ **Implementation approach** confirmed for NetSuite

---

## TOPIC 2: CHART OF ACCOUNTS CONSOLIDATION & MAPPING
**Estimated Time**: 90-120 minutes  
**Decision Maker**: Lorraine (CFO), Celine (GL), Kevin (GL)  
**Pre-Work Required**: ⚠️ **CRITICAL - Export current Core COA**

### Why This Matters
**Transcript Evidence:**
- Master Transcript Line 595-612: "Chart of Accounts - Current State: Volume: 40+ pages of accounts in Core... Unwieldy and difficult to manage... Target State: Few hundred accounts"
- Master Transcript Line 1147-1149: "Pain Points: 40+ Page Chart of Accounts: Unwieldy and hard to manage... Need consolidation... Cleaner reporting structure"
- Questionnaire Note: Listed as "early priority, needed immediately" for data migration

### Current State
- 40+ pages of accounts (extremely unwieldy)
- No documented mapping strategy
- No analysis of which accounts are duplicates/rarely used
- Must consolidate to make system manageable

### Questions to Ask

**Current State Analysis:**
1. Looking at the exported COA, which accounts are used frequently vs. rarely?
2. Which accounts are duplicates or serve the same purpose?
3. What's causing the 40+ page expansion? (Overly specific accounts? Lack of consolidation?)
4. Are there KB-specific vs. Hoag-specific vs. shared accounts?

**Target Structure Design:**
5. What level of detail do you actually need for GL reporting?
6. How can we use Classes, Departments, or Projects instead of account proliferation?
7. What account numbering scheme makes sense? (1000-1999 Assets, etc.?)
8. Do you need parent/child account hierarchies?

**Specific Account Categories:**
9. Revenue accounts: How many revenue categories do you truly need? (Labor, product, service, other?)
10. COGS accounts: Project COGS vs. general COGS structure?
11. G&A Expenses: What categories are essential vs. nice-to-have?
12. Equity accounts: Any special tracking needs?

**Project vs. G&A Structure:**
13. You mentioned needing "cost of goods sold, specifically identified as a project cost, and then general G&A-type stuff" - how many project cost categories? How many G&A categories?
14. Can we use segmentation (Projects, Departments) to reduce account count?

**15% Labor Markup Impact:**
15. If the labor markup continues, does it need separate cost accounts?
16. Currently how is the markup line coded in GL?
17. How do we maintain Project GP vs. Commissionable GP distinction in the COA?

**Mapping & Migration:**
18. Once we propose new structure, how will mapped accounts affect historical trend reporting?
19. What training will users need to adapt to new account structure?

### What We Want to Get
- ✅ **Proposed NetSuite COA structure** with account ranges and categories (target: few hundred accounts)
- ✅ **Account numbering scheme** defined
- ✅ **Mapping document**: Old COA → New COA (for all currently used accounts)
- ✅ **Classification of accounts**: Which ones can consolidate, which need to stay separate
- ✅ **Implementation approach**: How will you handle chart of accounts change (parallel reporting, cutover date, etc.)
- ✅ **Training plan**: Reference guide for users on new account structure
- ✅ **Finance team approval** on proposed structure

---

## TOPIC 3: COMMISSION STRUCTURE & 15% LABOR MARKUP DECISION
**Estimated Time**: 90 minutes  
**Decision Maker**: Matt/Mark (Leadership), Lorraine (CFO), Kipp (Finance/IT)  
**⚠️ CRITICAL ATTENDANCE REQUIRED**: Matt/Mark must participate for 15% markup decision

### Why This Matters
**Transcript Evidence:**
- Master Transcript Line 440-527: Complete section on "15% LABOR MARKUP (CONTINGENCY LINE)" with detailed explanation
- Master Transcript Line 512-522: "Two GP Metrics: Project GP: True gross profit... Commissionable GP: Includes 15% labor markup... Different set of KPIs"
- Master Transcript Line 515-519: "Commission Impact: Commission is paid on that... Changing it would affect commission calculations"
- Master Transcript Line 512-516: "Up for Debate: That may be up for debate as to whether or not we would want to keep that... Matt and Mark decision..."
- Kipp's opinion: "I'd be completely in favor of getting rid of it, but I don't... that's not my [decision]"

### Current State
- Core automatically adds 15% cost line when labor entered
- Purpose: "Encouraging people to put bigger margins on labor"
- Commission is calculated AFTER the 15% reduces GP (so commission is lower)
- Two separate KPI sets exist: Project GP (true profit) vs. Commissionable GP (reduced by markup)
- Decision pending on whether to continue

### Questions to Ask

**THE CRITICAL DECISION (Matt/Mark Only):**
1. Do you want to **continue the 15% labor markup** in NetSuite or **eliminate it**?
2. If continuing: Is automatic addition in Core working well, or do you want a different approach?
3. If eliminating: What's the communication plan to sales team? How much will commissions be impacted?

**If Continuing - Implementation Details:**
4. What triggers the markup line? (Specific product codes = labor?)
5. Is the calculation exactly 15% of labor cost line?
6. Can users override or remove the markup in specific situations?
7. Does the markup apply to ALL labor or only certain types?

**Commission Calculation Details:**
8. How exactly are commissions calculated? (% of commissionable GP?)
9. Is commission assigned at header-level or line-level?
10. How are commission splits handled between multiple sales reps?
11. When are commissions paid? (Order booking, invoice, payment collection?)
12. Do different order types have different commission structures?

**Dual GP Metrics Reporting:**
13. Who needs to see Project GP? (Management, finance, operations?)
14. Who needs to see Commissionable GP? (Sales team, account managers?)
15. What specific reports or dashboards are needed for each metric?
16. Do people need real-time visibility or month-end reporting?
17. How do you currently prevent sales team from seeing Project GP if they shouldn't?

**Role-Based Visibility:**
18. Define specific user roles and what GP metric they see (Sales Manager vs. Sales Rep vs. Finance?)
19. Any situations where someone needs to switch between views?
20. How are dashboard permissions managed?

### What We Want to Get
- ✅ **DECISION**: 15% labor markup continues or is eliminated (from Matt/Mark)
- ✅ **Commission calculation rules** fully documented with exact formulas
- ✅ **If continuing markup**: Implementation approach (manual process, custom script, or auto-add rules)
- ✅ **Dual GP metric definitions**: Project GP vs. Commissionable GP specifications
- ✅ **Role-based permissions matrix**: Who sees what metrics
- ✅ **KPI dashboard requirements**: What metrics for each audience
- ✅ **Sales team input** (optional but helpful): Do they understand and support current approach?

---

## TOPIC 4: PERIOD CLOSE PROCESS OPTIMIZATION
**Estimated Time**: 60 minutes  
**Decision Maker**: Lorraine (CFO), Celine (GL), Kevin (GL)

### Why This Matters
**Transcript Evidence:**
- Master Transcript Line 532-537: "Current Process: Timeline: 10 days to close accounting period... All managed via Excel... No system-guided process"
- Master Transcript Line 1152-1156: "Pain Points: 10-Day Period Close: All manual via Excel... No system guidance... Tracking challenges... Want to reduce timeline"
- Master Transcript Line 544-547: "Lorraine: Used Blackline or Flowcast in prior roles... Online systems for close management"
- Master Transcript Line 562-573: "NetSuite Period Close - Built-in Checklist: Period closing checklist feature... Step-by-step process"

### Current State
- 10-day Excel-based close process (entirely manual)
- All steps tracked in Excel, no system guidance
- Lorraine has prior experience with modern close tools (Blackline/Flowcast)
- Open all 13 periods at year start, close progressively

### Questions to Ask

**Current 10-Day Process:**
1. Walk me through your current Excel checklist - what are the specific steps?
2. Which steps take the longest? (Reconciliations, journal entries, reporting, other?)
3. What causes delays or bottlenecks?
4. Do you ever close faster than 10 days? What enables that?
5. What's the typical breakdown? (AP close: X days, AR close: Y days, GL close: Z days?)

**Reconciliation Requirements:**
6. Bank reconciliation - how often and when in the close process?
7. Credit card reconciliation - manual or can be automated?
8. Do you have intercompany reconciliations?
9. Inventory reconciliation - warehouse physical counts frequency?
10. What reconciliation tolerances are acceptable?

**Journal Entry Requirements:**
11. What recurring JEs do you process each period?
12. Accruals and prepayments - standard list each month?
13. Allocation journal entries - if implemented, when do they post?
14. Reversal JEs - how many scenarios will use automated reversals?
15. Who has authority to post JEs during close? (Lorraine, Celine, Kevin, Kipp?)

**NetSuite Period Close Checklist Customization:**
16. What specific steps must be on your NetSuite checklist?
17. Who's responsible for each step? (Need task assignment)
18. Which steps require approval? (Lorraine sign-off points?)
19. What tasks can happen simultaneously vs. sequentially?
20. What document attachments must be uploaded?

**Timeline & Goals:**
21. What's a realistic target for NetSuite close timeline? (5 days? 7 days?)
22. What's the absolute minimum timeline achievable with full automation?
23. Do you need both soft close and hard close?
24. When do reports need to be ready after period end?

**Period Control & Locking:**
25. After close, who can reopen periods? (Lorraine only?)
26. What circumstances require reopening a closed period?
27. Do you need to audit all period reopening activity?

### What We Want to Get
- ✅ **Detailed current state close process** documented (all 10 days broken down)
- ✅ **NetSuite Period Close Checklist** customized to KBM needs
- ✅ **Task assignments** and approval gates defined
- ✅ **Target timeline** established (realistic goal with automation)
- ✅ **Reconciliation approach** for bank, credit card, inventory
- ✅ **Recurring JE list** identified for automation
- ✅ **Close procedure documentation** for training

---

## TOPIC 5: BILL PAYMENT & CASH MANAGEMENT WORKFLOW
**Estimated Time**: 45-60 minutes  
**Decision Maker**: Lorraine (CFO), Guada & Michael (Accounts Payable)

### Why This Matters
**Transcript Evidence:**
- Master Transcript Line 270-299: Complete section on "Payment Approval Workflow" with Monday payment runs, Lorraine's approval process
- Master Transcript Line 275-278: "Monday Payment Process: Regular Monday payment runs... Sometimes $3M... Lorraine reviews and approves... 'They always try to kill me with the amounts'"
- Master Transcript Line 233-253: "Electronic Bill Payments (ACH) - Current Process: Run check run in Core... Generate HTML file (NACHA format)... Log into bank portal... Upload file"
- Master Transcript Line 243-248: "NetSuite Capability: Advanced Electronic Bill Payments (part of edition)... Pay via ACH directly from NetSuite... Skip manual bank portal upload step"
- Master Transcript Line 299-300: "Action Items: Confirm exact approval workflow steps... Determine if approver can edit payment selection... Confirm remittance process (automatic or manual trigger)... If it said we sent it and we didn't, then you know that's a problem"

### Current State
- Monday payment runs, sometimes $3M
- Guada/Michael compile bills → Lorraine reviews → Lorraine "picks and chooses" → NACHA file generation → Bank portal upload
- 90% ACH, handful of international wires, some credit card activity
- Concern about remittance: "If it said we sent it and we didn't, that's a problem"

### Questions to Ask

**Payment Approval Workflow Details:**
1. Currently Lorraine "picks and chooses" from the proposed payment run - can she remove items in NetSuite system, or must she communicate back to AP to uncheck items?
2. What's your preferred workflow in NetSuite?
3. If Lorraine removes items, what happens to those bills? (Automatically move to next Monday run?)
4. Does Lorraine ever need to change payment amounts, or only approve/reject entire bills?
5. How often does Lorraine actually reject or remove items? (Typical % of payment run?)

**Payment Run Compilation:**
6. Who decides which bills go into the Monday payment run? (Guada/Michael criteria?)
7. Do you pay by due date, take discounts, or other priority?
8. How do you handle rush payments outside Monday schedule?
9. Do you track and take advantage of early payment discounts?
10. Any payment terms optimization strategy?

**Remittance Process:**
11. Current concern was "If it said we sent it and we didn't" - clarify what this risk is?
12. Should remittance to vendors be automatic or manual trigger in NetSuite?
13. What's your preferred approach?
14. Remittance format: Email, portal, mail check stub, or combination?
15. Remittance detail level: Summary or itemized bill details?

**Wire Transfer Handling:**
16. You have "handful of wires (international only)"
17. Are wires supported in Advanced Electronic Bill Payments module?
18. If not: Continue manual bank portal for wires, or find alternative?
19. Wire approval process: Same as ACH (Lorraine) or additional authorization?

**Vendor Prepayments:**
20. Which vendors require prepayments?
21. How do prepayments get approved? (Lorraine approves before full payment run?)
22. Prepayment application against future bills - automatic or manual?

**Positive Pay:**
23. Does West Coast Community Bank require positive pay?
24. Do you currently use positive pay?
25. After NetSuite connection: How will positive pay file be generated and transmitted?

**Payment Exceptions:**
26. What happens if ACH payment fails? (Vendor bank info wrong, account closed, etc.)
27. Failed payment notification - who receives alerts?
28. Retry process - automatic or manual?

### What We Want to Get
- ✅ **Bill payment approval workflow** fully defined (system-based vs. communication-based)
- ✅ **Remittance process** confirmed (automatic or manual trigger)
- ✅ **Wire transfer handling** approach determined (if not supported in ACH module)
- ✅ **Vendor prepayment** procedures documented
- ✅ **Positive pay process** documented with West Coast Community Bank
- ✅ **Payment exception handling** procedures defined
- ✅ **Cash flow management requirements** specified (if using Cache360 dashboard)

---

## TOPIC 6: EXPENSE MANAGEMENT PLATFORM & PROJECT CODING
**Estimated Time**: 45-60 minutes + separate demos  
**Decision Maker**: Lorraine (CFO), Guada & Michael (AP)  
**Optional Attendees**: 2-3 sample expense submitters (Matt, field team members)

### Why This Matters
**Transcript Evidence:**
- Master Transcript Line 341-379: Complete section on "Expense Management - Expensify" with current manual process
- Master Transcript Line 342-350: "Current Process: Users create expense reports in Expensify... AP team manually downloads... Manual coding into GL... Obviously a lot of work there up front"
- Master Transcript Line 352-355: "User Challenge: Matt has a lot of lines that he has to manage... Matt: I just don't do it... Who likes to do expense reports? That's why I made Chris buy everything"
- Master Transcript Line 357-361: "NetSuite Solution: Expensify Integration (Suite App available)... Absolutely talk to each other. You can just sync data"
- Master Transcript Line 363-367: "Alternative: RAMP... Lorraine interested in moving from Expensify to RAMP... Could potentially demo both"
- Master Transcript Line 380-395: "Expense Report Allocation - Cost Structure Question: Two different cost categories... Cost of Goods Sold - project costs... G&A - general administrative expenses"

### Current State
- Expensify with entirely manual process
- Users resist creating expense reports ("who likes to do expense reports?")
- Manual download/upload creates substantial AP work
- Lorraine interested in RAMP as alternative
- Must support project cost (COGS) vs. G&A allocation

### Questions to Ask

**Current Pain Points:**
1. How many expense reports submitted monthly?
2. Who are the primary submitters? (Sales team, field team, executives?)
3. Typical expense report size? (Number of lines, dollar amounts?)
4. What do users complain about most regarding Expensify?
5. What does AP team complain about most?
6. How long does approval and processing typically take?

**Project vs. G&A Allocation Requirements:**
7. You mentioned needing "project cost to go into COGS, and then general G&A-type stuff" - what % of expenses are project-related vs. G&A?
8. What project-related expenses are common? (Travel to job site, client meetings, project meals?)
9. How granular does project coding need to be? (Project number only, or project + phase/task?)
10. Can one expense report have both project and G&A expenses? (Need line-level coding?)

**Expensify Suite App Option:**
11. If we improve Expensify integration: What would need to change for users to actually do their expense reports?
12. Is it the submission process, the approval process, or just user resistance?
13. What must auto-sync do to eliminate manual work?
14. Receipts attached in Expensify must flow to NetSuite automatically?

**RAMP Option:**
15. Lorraine interested in RAMP - what appeals to you? (Receipt capture from phone, simpler UX?)
16. Do you understand RAMP already has NetSuite integration?
17. Change management: How hard would it be to get users to switch from Expensify to RAMP?
18. Cost comparison: Any sense of RAMP vs. Expensify pricing?

**Integration Requirements (Either Option):**
19. Must auto-sync expense data to NetSuite (eliminate manual download/import)?
20. Receipt images must attach to expense transactions in NetSuite?
21. Project coding fields available in mobile app for ease of use?
22. GL account coding: Pre-defined categories or user selects?
23. Department coding: Automatic based on employee or user selects?
24. Corporate card integration: Can ARC Bank transactions auto-import to expense reports?

**Approval Workflow:**
25. Current approval process: Who approves expense reports?
26. Manager approval required before AP processing?
27. Expense policy enforcement: Spending limits, receipt requirements, per diem rates?
28. Out-of-policy expenses: How handled?
29. Reimbursement timing: How quickly do employees get reimbursed?

**Credit Card Integration:**
30. ARC Bank corporate credit card currently "very manual" reconciliation
31. Can Expensify or RAMP pull in corporate card transactions automatically?
32. NetSuite credit card reconciliation: Can you upload statement as CSV, auto-match to reports?
33. Corporate card vs. personal card expenses: Different handling?

### What We Want to Get
- ✅ **DECISION**: Expensify Suite App integration OR switch to RAMP
- ✅ **Project coding requirements** fully documented
- ✅ **Approval workflow** defined
- ✅ **Credit card reconciliation approach** confirmed
- ✅ **Integration specifications** for chosen platform (auto-sync, receipt attachment, project fields)
- ✅ **Change management plan** if switching platforms
- ✅ **User experience assessment**: What would increase adoption?

---

## TOPIC 7: FIXED ASSET MANAGEMENT
**Estimated Time**: 30-45 minutes  
**Decision Maker**: Lorraine (CFO)

### Why This Matters
**Transcript Evidence:**
- Master Transcript Line 829-857: Complete section on "Fixed Asset Management" comparing Bloomberg vs. NetSuite module
- Master Transcript Line 833-836: "Bloomberg: Third party for tax depreciation... Separate from Core... Tax vs. book depreciation tracking"
- Master Transcript Line 840-850: "NetSuite Fixed Asset Module - Option: Additional cost (~$4,000)... Lorraine's Question: I just want to know if NetSuite can meet our needs... Marcus Assessment: I think the fixed asset module's gonna handle what you need"
- Master Transcript Line 852-856: "Decision: Evaluate NetSuite FA module capabilities... Compare to Bloomberg functionality... Cost-benefit analysis"

### Current State
- Currently using Bloomberg (third-party, additional cost)
- Bloomberg tracks tax depreciation, separate from Core
- NetSuite FA module available (~$4,000 cost)
- Marcus believes NetSuite FA should handle needs, but not fully validated

### Questions to Ask

**Current Fixed Asset Management:**
1. How many fixed assets do you currently track?
2. Asset categories: Vehicles, equipment, furniture, leasehold improvements, other?
3. How frequently do you add new assets?
4. How frequently do you dispose of assets?
5. Who manages fixed asset records? (Lorraine, Celine, Kevin?)

**Depreciation Requirements:**
6. Book depreciation methods used: Straight-line, declining balance, other?
7. Tax depreciation: MACRS, Section 179, bonus depreciation?
8. How often do you need book vs. tax depreciation? (Annual, monthly?)
9. Mid-year conventions used: Half-year, mid-quarter, other?
10. What depreciation reports do you need? (Monthly, quarterly, annual?)

**Bloomberg Functionality:**
11. What specific Bloomberg features do you actually use?
12. What do you like about Bloomberg?
13. What are Bloomberg limitations or pain points?
14. What's Bloomberg's annual cost?
15. How does Bloomberg data currently get into Core GL? (Manual entry, export/import?)

**NetSuite FA Module Evaluation:**
16. What Bloomberg features are "must-have" in NetSuite?
17. Depreciation calculations: Should be automatic monthly posting?
18. Asset tagging and physical inventory - important to track?
19. Asset transfers between locations/departments - need this?
20. Asset split and partial disposal capabilities - need this?

**Migration Considerations (If Switching):**
21. How will existing asset records migrate from Bloomberg to NetSuite?
22. Historical depreciation data - how far back? (Just current year?)
23. Asset valuation: Cost, accumulated depreciation, net book value - accurate in Bloomberg?
24. Year-to-date depreciation: Import or recalculate in NetSuite?

**Cost-Benefit Analysis:**
25. Bloomberg annual cost: $X?
26. NetSuite FA module: $4,000 is one-time or annual?
27. What's the payback period?

### What We Want to Get
- ✅ **DECISION**: NetSuite Fixed Asset module OR continue Bloomberg
- ✅ **If NetSuite FA**: Detailed requirements for module configuration
- ✅ **If NetSuite FA**: Migration plan for existing assets from Bloomberg
- ✅ **If continuing Bloomberg**: Integration approach between Bloomberg and NetSuite
- ✅ **Cost-benefit analysis** documented

---

## TOPIC 8: VENDOR CREDIT LIMIT TRACKING & ALERTS
**Estimated Time**: 20-30 minutes  
**Decision Maker**: Lorraine (CFO), Purchasing team  
**Optional**: Shannon (Product Coordinator Manager)

### Why This Matters
**Transcript Evidence:**
- Master Transcript Line 700-703: "Vendor Management - Credit Limits: Track KBM credit limits with vendors... Hit limits unexpectedly: Mad scramble at that nth hour... Need warnings/alerts"
- Master Transcript Line 1194-1197: "Pain Points: [No automated credit limit tracking]... Vendor credit limit issues... How often do you hit vendor credit limits unexpectedly?"
- Requirements Document: "REQ-034: Custom alert/warning required (ACCOMMODATE approach)"

### Current State
- No automated credit limit tracking
- Occasionally hit vendor limits unexpectedly
- Causes "mad scramble at that nth hour"
- Need warnings/alerts when approaching limits

### Questions to Ask

**Current Credit Limit Issues:**
1. How often do you hit vendor credit limits unexpectedly?
2. Which vendors have credit limits that are frequently reached?
3. What's the impact when you hit a limit? (Order delays, rush payments, vendor relationship issues?)
4. Do vendors notify you proactively, or only when you're over?
5. How do you currently track how close you are to limits?

**Vendor Credit Limit Data:**
6. Do you have credit limit amounts documented for all major vendors?
7. How do vendors communicate limits? (Email, portal, contract?)
8. Do credit limits change over time? (Increases based on payment history?)
9. Are limits per location or company-wide?

**Warning Threshold:**
10. At what percentage of limit do you want a warning? (Suggested: 80%, 90%, 95%?)
11. Different thresholds for different vendors? (Critical vendors = earlier warning?)
12. Should there be soft warning vs. hard blocking?

**Alert Recipients & Mechanism:**
13. Who should receive warning alerts? (Purchasing team, Shannon, AP team, Lorraine?)
14. Alert method: Email, dashboard widget, both?
15. Should PO creation be blocked if it would exceed limit? (Hard stop or just warning?)
16. Report needed: "Vendor credit utilization" showing % of limit used for all vendors?

**Credit Utilization Calculation:**
17. Calculate utilization as: Open POs + Unpaid bills vs. credit limit?
18. Include vendor prepayments in available credit calculation?
19. Real-time tracking or end-of-day batch calculation?

**Process When Approaching Limit:**
20. When you receive a 90% warning, what's the ideal process?
21. Expedite payment to free up credit?
22. Request credit limit increase from vendor?
23. Defer non-urgent orders?
24. Who makes the decision on how to respond?

### What We Want to Get
- ✅ **Warning threshold** defined (e.g., 90% of credit limit)
- ✅ **Alert recipients** identified
- ✅ **Alert mechanism** specified (email, dashboard, PO blocking)
- ✅ **Credit utilization calculation** method defined
- ✅ **Custom development requirements** documented
- ✅ **Process for handling warnings** established

---

## SESSION SCHEDULING RECOMMENDATION

### Consolidation Strategy (Realistic 4-5 Hour Approach):

**PRIORITY SESSION 1** (90 min): Revenue Recognition + Chart of Accounts
- Topic 1: Revenue Recognition Rules (60 min)
- Topic 2: Chart of Accounts (starts 30 min, continues to Session 2)

**PRIORITY SESSION 2** (90 min): Chart of Accounts (continued) + Commission Structure
- Topic 2: COA Design (finish - 60 min)
- Topic 3: Commission/Labor Markup Decision (30 min start)
- **REQUIRED**: Matt/Mark attendance

**SESSION 3** (90 min): Commission Structure (finish) + Operational Topics
- Topic 3: Commission/GP/Markup (finish - 30 min)
- Topic 4: Period Close (30 min)
- Topic 5: Bill Payment (30 min)

**SESSION 4** (75 min): Platform & Optimization Decisions
- Topic 6: Expense Management + Demos (45 min, demos scheduled separately)
- Topic 7: Fixed Assets (20 min)
- Topic 8: Vendor Credit Limits (10 min)

**TOTAL TIME**: ~345 minutes (5 hours 45 minutes)

---

*End of Next Session Guide v1.0*

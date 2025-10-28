# Financial Management Follow-Up Discovery Session
## KBMH NetSuite/Orion Implementation

**Date:** October 2025  
**Session Duration:** 2-3 hours  
**Priority:** High - Core financial processes and design decisions  
**Participants Needed:**
- Lorraine (CFO/Controller) - Primary
- Kipp (Former Controller/IT) - Primary
- Celine & Kevin (General Ledger) - As needed for COA design
- Guada & Michael (Accounts Payable) - As needed for payment workflows
- Matt/Mark (Leadership) - For strategic decisions on labor markup and allocations

---

## PART 1: CURRENT STATE KNOWLEDGE SUMMARY

### What We Know About Your Financial Management

Based on our comprehensive discovery sessions, we have documented a strong understanding of your current financial operations:

#### **Your Finance Team & Operations**
You operate with a **lean but mighty finance team** managing a **$100M dealer operation**:
- **Lorraine** (CFO/Controller) provides leadership and payment approval
- **Guada** and **Michael** (Philippines) manage accounts payable as the "Dynamic Duo"
- **Celine** and **Kevin** handle general ledger operations
- **AR Person** manages receivables from San Jose office
- **Kipp** serves as a critical finance partner - former controller turned IT specialist who still "touches everything" and is leveraged heavily for finance duties after 15 years with the company

#### **Company Structure & Configuration**
- **Single NetSuite subsidiary** representing consolidated KB + Hoag operations
- **13 accounting periods** on calendar year basis (your preference vs. Core's 12-period limitation)
- **US Dollar only** - no multi-currency requirements
- Multiple locations/warehouses within single subsidiary

#### **Tax Management**
- **48 states** with nexus registration requiring sales tax compliance
- **SuiteTax** (native NetSuite, not Avalara) for automatic tax calculation based on ship-to address
- **Tax exemption certificate management** with expiration tracking and dashboard
- **Use tax** requirements for Illinois and Missouri (currently using workaround in Core with TaxConnect third party)
- **Gross receipts tax reporting** by ship-to location
- Tax override capability for complex government orders

#### **Banking & Payment Processing**
- **West Coast Community Bank** (confirmed NetSuite Bank Feeds partner)
- **Bank feeds integration** for automatic transaction import and auto-matching
- **Advanced Electronic Bill Payments** for ACH directly from NetSuite (eliminating bank portal upload step)
- **Payment approval workflow** with Lorraine as approver for Monday payment runs (sometimes $3M)
- **90% ACH**, handful of international wires, some credit card activity
- **ARC Bank** corporate credit cards (currently very manual reconciliation process)
- **Stripe** for rare customer credit card payments (~$100/year, incidental use)

#### **Current Pain Points We're Addressing**
- **40+ page chart of accounts** - unwieldy and difficult to manage
- **10-day period close** managed entirely via Excel with no system guidance
- **Manual expense management** - Expensify with manual download, GL coding, and reconciliation
- **Manual credit card reconciliation** - separate from bank reconciliation, time-consuming
- **No automated reversal journal entries** in Core - "couldn't keep track of them"
- **Manual ACH process** - HTML/NACHA file generation, bank portal upload, verification steps
- **Limited real-time reporting** - reliance on manual Excel reports and Google Sheets

#### **What's Working Well**
- **Clear project accounting structure** with project-level revenue/cost tracking
- **Defined approval workflows** - payment approval process with Lorraine
- **Payroll integration** via CSV import from Paylocity (flexible for potential provider change)
- **Customer deposit management** understanding (pro forma invoices)
- **Finance charge capability** (never used in 13 years, but available as deterrent)

#### **Key Business Practices We Understand**
- **Project GP vs. Commissionable GP** - two separate KPI sets for different audiences
- **15% labor markup** (contingency line) - cost-only, affects commission calculations (continuation pending Matt/Mark decision)
- **Role-based permissions** - different people see different GP metrics
- **Intermarket dealers** requiring setup as both vendor AND customer
- **Vendor credit limit tracking** needs with warnings to avoid unexpected limit issues

#### **Historical Data & Migration**
- **Financial data back to 2017** per Lorraine's decision (8 years)
- End-of-month trial balances approach
- SQL backend access to Core confirmed
- Older data to be exported and archived separately

---

## TRANSCRIPT EVIDENCE & JUSTIFICATION FOR FOLLOW-UP QUESTIONS

### SESSION 1: Revenue Recognition Rules & Project Accounting

**Transcript Evidence:**
- **Master Transcript, Line 68-79:** "Current Process: Sales order = revenue recognition... Static process after quote creation... No changes after sales order... NetSuite Approach: Separate transaction types... Opportunity → Quote → Sales Order"
- **Master Transcript, Line 792-797:** "White Paper mentioned by Marcus for revenue recognition differences... Full revenue recognition discussion likely continued but not captured in transcript excerpts reviewed"
- **Transcript_FinancialManagement_20250918.md, Line 125-134:** "White Paper Provided: GSI has detailed white paper on revenue recognition in NetSuite... Different from Core's approach... Review required: Lorraine needs to understand differences"

**Justification:**
The discovery sessions identified that KBM's revenue recognition process is simplistic ("sales order = revenue recognition") but NetSuite offers more sophisticated capabilities through separate transaction types (Opportunity → Quote → Sales Order). A white paper was referenced but not fully discussed. The transcript shows Lorraine explicitly "needs to understand differences" between Core and NetSuite approaches. This session is required to:
1. Explain the white paper findings
2. Clarify when revenue should recognize for different order types
3. Document special scenarios (mockup orders, direct bill, government orders, E-commerce)
4. Establish compliance requirements
5. Define audit documentation needs

---

### SESSION 2: Chart of Accounts Design & Mapping Workshop

**Transcript Evidence:**
- **Master Transcript, Line 595-612:** "Chart of Accounts - Current State: Volume: 40+ pages of accounts in Core... Unwieldy and difficult to manage... Target State: Few hundred accounts"
- **Master Transcript, Line 1147-1149:** "Pain Points: 40+ Page Chart of Accounts: Unwieldy and hard to manage... Need consolidation... Cleaner reporting structure"
- **Transcript_FinancialManagement_20250918.md, Line 234:** "Chart of Accounts - Early priority, needed immediately"
- **Master Transcript, Line 624-638:** "Data Migration Strategy - Core Data Export: SQL backend access confirmed... Data migration tool available"

**Justification:**
The transcripts repeatedly highlight the 40+ page chart of accounts as a major pain point that is "unwieldy and difficult to manage." This was identified as an "early priority, needed immediately" for data migration. However, the current state COA hasn't been exported or analyzed. This session is required to:
1. Export and analyze current Core COA structure
2. Identify redundant/duplicate accounts
3. Define target structure ("few hundred accounts")
4. Create mapping from old to new COA
5. Impact historical reporting and trend analysis
6. Plan user training for new structure

---

### SESSION 3: Commission Structure & GP Calculation Deep Dive

**Transcript Evidence:**
- **Master Transcript, Line 440-527:** Complete section on "15% LABOR MARKUP (CONTINGENCY LINE)" with detailed explanation of the practice, impact, and industry comparison
- **Master Transcript, Line 512-522:** "Two GP Metrics: Project GP: True gross profit... Commissionable GP: Includes 15% labor markup... Kipp: 'That's why we have two... different set of KPIs'"
- **Master Transcript, Line 512-516:** "Up for Debate: That may be up for debate as to whether or not we would want to keep that... Matt and Mark decision... Kipp: I'd be completely in favor of getting rid of it, but I don't... that's not my [decision]"
- **Master Transcript, Line 515-519:** "Commission Impact: Commission is paid on that... Changing it would affect commission calculations"
- **Transcript_FinancialManagement_20250918.md, Line 89-122:** Detailed section on "Labor Margin Contingency - 15% Load Factor"

**Justification:**
The transcripts thoroughly document that KBM uses a 15% labor markup system with significant implications:
- It affects commission calculations (commissions are "paid on that")
- Requires two separate GP metrics (Project GP vs. Commissionable GP)
- Requires role-based visibility (different users see different KPIs)
- Is "up for debate" with pending decision from Matt/Mark
- The implementation approach in NetSuite is unknown

This session is required to:
1. Obtain Matt/Mark's final decision on whether to continue
2. Document exact commission calculation rules
3. Define who needs to see which GP metric
4. Plan custom development if continuing
5. Design role-based permissions for GP visibility
6. Plan communication to sales team regarding any changes

---

### SESSION 4: Period Close Process Optimization

**Transcript Evidence:**
- **Master Transcript, Line 532-537:** "Current Process: Timeline: 10 days to close accounting period... All managed via Excel... No system-guided process"
- **Master Transcript, Line 1152-1156:** "Pain Points: 10-Day Period Close: All manual via Excel... No system guidance... Tracking challenges... Want to reduce timeline"
- **Master Transcript, Line 544-547:** "Previous Experience (Lorraine): Used Blackline or Flowcast in prior roles... Online systems for close management"
- **Master Transcript, Line 562-573:** "NetSuite Period Close - Built-in Checklist: Period closing checklist feature... Step-by-step process"
- **Master Transcript, Line 563-573:** "Module Closing: Can close AP/AR separately and go through checklist... Flexible closing process"

**Justification:**
The discovery sessions identified a 10-day, entirely Excel-based period close process with no system guidance. Lorraine has prior experience with modern close tools (Blackline/Flowcast), suggesting she would appreciate a NetSuite-based solution. However, critical details are missing:
- Current close steps and timeline breakdown
- Reconciliation requirements and frequencies
- Recurring journal entries and accruals
- Close checklist customization needs
- Target timeline for NetSuite close
- AP/AR closing sequence and gates

This session is required to:
1. Document current 10-day Excel-based process in detail
2. Identify bottlenecks and optimization opportunities
3. Define customized NetSuite Period Close Checklist steps
4. Establish task assignments and approval gates
5. Set realistic target timeline (5-7 days goal?)
6. Plan training for new process

---

### SESSION 5: Bill Payment & Cash Management Workflow Details

**Transcript Evidence:**
- **Master Transcript, Line 270-299:** Complete section on "Payment Approval Workflow" detailing Monday payment runs, Lorraine's approval process, and current workflow
- **Master Transcript, Line 275-278:** "Monday Payment Process: Regular Monday payment runs... Sometimes $3M... Lorraine reviews and approves... 'They always try to kill me with the amounts'"
- **Master Transcript, Line 233-253:** "Electronic Bill Payments (ACH) - Current Process: Run check run in Core... Generate HTML file (NACHA format)... Log into bank portal... Upload file"
- **Master Transcript, Line 243-248:** "NetSuite Capability: Advanced Electronic Bill Payments (part of edition)... Pay via ACH directly from NetSuite... Skip manual bank portal upload step"
- **Master Transcript, Line 256-268:** "Wire Transfers: Wires restricted to international (expensive)... ACH is cheap... Module question: ACH only or wire support too?"
- **Master Transcript, Line 299-300:** "Action Items: Confirm exact approval workflow steps... Determine if approver can edit payment selection... Confirm remittance process (automatic or manual trigger)... If it said we sent it and we didn't, then you know that's a problem"

**Justification:**
The discovery sessions identified that KBM's current payment process involves multiple manual steps (NACHA file generation, bank portal upload, verification). NetSuite's Advanced Electronic Bill Payments can eliminate the bank portal step, but several workflow details need clarification:
- Exact approval workflow (Can Lorraine remove items in-system or only communicate back to AP?)
- Remittance process (automatic vs. manual)
- Wire transfer handling (if not supported in ACH module)
- Payment run compilation criteria
- Vendor prepayment handling
- Cash flow management

This session is required to:
1. Confirm exact approval workflow and system-based vs. manual communication
2. Define remittance process (automatic or manual trigger)
3. Determine wire transfer handling approach
4. Document payment exception handling
5. Specify cash flow forecasting requirements
6. Plan training for new approval workflow

---

### SESSION 6: Expense Management System Decision & Project Coding

**Transcript Evidence:**
- **Master Transcript, Line 341-379:** Complete section on "Expense Management - Expensify" with current manual process and NetSuite integration options
- **Master Transcript, Line 342-350:** "Current Process: Users create expense reports in Expensify... AP team manually downloads... Manual coding into GL... Obviously a lot of work there up front"
- **Master Transcript, Line 352-355:** "User Challenge: Matt has a lot of lines that he has to manage... Matt: I just don't do it... Who likes to do expense reports? That's why I made Chris buy everything"
- **Master Transcript, Line 357-361:** "NetSuite Solution: Expensify Integration (Suite App available)... Absolutely talk to each other. You can just sync data"
- **Master Transcript, Line 363-367:** "Alternative: RAMP... Lorraine interested in moving from Expensify to RAMP... Could potentially demo both"
- **Master Transcript, Line 380-395:** "Expense Report Allocation - Cost Structure Question: Two different cost categories... Cost of Goods Sold - project costs... G&A - general administrative expenses"
- **Master Transcript, Line 1213-1218:** "Expensify/RAMP Integration: Auto-sync to NetSuite... Attach receipts automatically... Project coding... Eliminate manual download/upload"

**Justification:**
The discovery sessions identified significant pain points with the current Expensify process:
- Users resist creating expense reports ("who likes to do expense reports?")
- Manual download/upload creates substantial administrative work
- Expense allocation must support both project costs (COGS) and G&A
- Lorraine is interested in exploring RAMP as an alternative
- Both platforms have NetSuite integration available

However, critical requirements are unclear:
- Exact project coding requirements (project number only or project + phase/task?)
- User experience needs (what would make users more willing to submit?)
- Integration specifications for chosen platform
- Approval workflow requirements
- Credit card reconciliation approach

This session is required to:
1. Document project vs. G&A allocation requirements in detail
2. Identify user experience requirements for adoption
3. Demo both Expensify Suite App and RAMP
4. Evaluate project coding capabilities
5. Define approval workflow
6. Plan credit card reconciliation approach
7. Make platform selection decision

---

### SESSION 7: Fixed Asset Management Decision

**Transcript Evidence:**
- **Master Transcript, Line 829-857:** Complete section on "Fixed Asset Management" comparing Bloomberg vs. NetSuite module
- **Master Transcript, Line 833-836:** "Bloomberg: Third party for tax depreciation... Separate from Core... Tax vs. book depreciation tracking"
- **Master Transcript, Line 840-850:** "NetSuite Fixed Asset Module - Option: Additional cost (~$4,000)... Lorraine's Question: I just want to know if NetSuite can meet our needs... Marcus Assessment: I think the fixed asset module's gonna handle what you need"
- **Master Transcript, Line 852-856:** "Decision: Evaluate NetSuite FA module capabilities... Compare to Bloomberg functionality... Cost-benefit analysis"
- **Transcript_FinancialManagement_20250918.md, Line 173-177:** "Asset Management: Fixed asset tracking required... Depreciation calculations... Asset lifecycle management"

**Justification:**
The discovery sessions identified that KBM currently pays for Bloomberg (third-party service) for tax depreciation tracking. NetSuite offers a Fixed Asset module (~$4,000 cost) that Marcus believes "is gonna handle what you need." However, critical requirements haven't been defined:
- Bloomberg functionality actually being used
- NetSuite FA module capabilities vs. Bloomberg
- Cost-benefit analysis (Bloomberg annual cost vs. NetSuite FA cost)
- Migration complexity for existing assets
- Depreciation method requirements

This session is required to:
1. Document current Bloomberg features being used
2. Evaluate NetSuite FA module capabilities
3. Conduct cost-benefit analysis
4. Determine migration approach if switching
5. Make platform selection decision
6. Plan implementation timeline

---

### SESSION 8: Vendor Credit Limit Tracking & Alerts

**Transcript Evidence:**
- **Master Transcript, Line 700-703:** "Vendor Management - Credit Limits: Track KBM credit limits with vendors... Hit limits unexpectedly: Mad scramble at that nth hour... Need warnings/alerts"
- **Master Transcript, Line 1194-1197:** "Pain Points: [No automated credit limit tracking]... Vendor credit limit issues... How often do you hit vendor credit limits unexpectedly?"
- **Financial_Management_Follow-Up_Discovery_Session.md, Line 596:** "REQ-034: Custom alert/warning required (ACCOMMODATE approach)"

**Justification:**
The discovery sessions identified a specific pain point: KBM hits vendor credit limits unexpectedly, causing "mad scramble at that nth hour." This is a documented requirement (REQ-034) that needs custom development to accommodate. However, critical details are missing:
- Which vendors have frequently-reached limits
- Impact of hitting limits
- Warning threshold preference (90%?)
- Alert mechanism (email, dashboard, PO blocking?)
- Credit utilization calculation approach

This session is required to:
1. Quantify frequency and impact of credit limit issues
2. Define warning threshold(s)
3. Identify alert recipients
4. Specify alert mechanism (email vs. dashboard vs. hard stop)
5. Document custom development requirements
6. Plan process for handling warnings

---

## SUMMARY: Why These Sessions Are Required

These follow-up sessions address critical gaps between what was discovered and what's needed for successful configuration:

| Gap | Root Cause | Follow-Up Session |
|-----|-----------|-------------------|
| Simplistic revenue recognition not documented | White paper reviewed but not discussed | SESSION 1 |
| 40+ page COA identified but not analyzed | No COA export/analysis done yet | SESSION 2 |
| 15% labor markup decision pending | Matt/Mark need final input | SESSION 3 |
| 10-day close process not optimized | Excel-based, needs system design | SESSION 4 |
| Payment approval workflow unclear | Lorraine's role not fully specified | SESSION 5 |
| Expense platform not selected | Expensify vs. RAMP comparison needed | SESSION 6 |
| Fixed Asset module not evaluated | Bloomberg capabilities vs. NetSuite unclear | SESSION 7 |
| Vendor credit limit pain point needs solution | Custom development scope not defined | SESSION 8 |

---

## PART 2: AREAS REQUIRING CLARIFICATION & DEEPER EXPLORATION

### SESSION 1: Revenue Recognition Rules & Project Accounting (90 minutes)

**Context:** This is identified as a High Priority session requiring dedicated discussion. Revenue recognition rules and timing are complex, compliance-critical, and errors would impact financials significantly.

**What We Know:**
- Current state: "Sales order = revenue recognition" - static process after quote
- NetSuite approach: Opportunity → Quote → Sales Order with separate, linked transactions
- All transactions linked to project for project-level aggregation
- White paper mentioned by Marcus for revenue recognition differences

**Questions for Discussion:**

1. **Revenue Recognition Timing**
   - When exactly does revenue recognize for your standard project orders? (At Sales Order creation or at Invoice?)
   - Do different order types require different recognition rules?
   - How do you handle partial invoicing and milestone-based recognition?

2. **Special Recognition Scenarios**
   - How should mockup orders be handled for revenue recognition?
   - Direct bill vs. normal billing - any recognition differences?
   - Intermarket dealer transactions - recognition timing?
   - Government orders with unique terms - special handling?
   - E-commerce orders - immediate recognition vs. project-based?

3. **Project-Based Revenue Rules**
   - How does project duration impact recognition?
   - Multi-order projects spanning months - recognition approach?
   - Change orders and scope changes - how does this affect recognized revenue?
   - Customer-owned material (COM) transactions - revenue implications?

4. **Cost Recognition Alignment**
   - When do costs recognize relative to revenue?
   - How do vendor prepayments affect cost recognition timing?
   - Labor costs - recognize when work performed or when invoiced?
   - Storage fees - recognition timing?

5. **Compliance & Audit Requirements**
   - What specific accounting standards must you comply with? (ASC 606, etc.)
   - How do auditors currently review your revenue recognition practices?
   - What documentation is required for recognition decisions?
   - Any industry-specific compliance requirements for dealer operations?

6. **Reporting Requirements**
   - What revenue recognition reports do you need monthly/quarterly?
   - How do you track unbilled revenue?
   - Deferred revenue tracking and reporting?
   - Revenue backlog visibility requirements?

**Expected Outcomes:**
- Detailed revenue recognition rules documentation by order type
- Special scenario handling procedures defined
- White paper review and validation
- Implementation approach confirmation
- Testing and validation plan for recognition rules

---

### SESSION 2: Chart of Accounts Design & Mapping Workshop (2 hours)

**Context:** This is a High Priority foundational requirement. Your current 40+ page COA is unwieldy; consolidating to "few hundred accounts" impacts all transactions and reports system-wide.

**What We Know:**
- Current: 40+ pages of accounts in Core
- Target: Few hundred accounts (significant reduction)
- KB workspace and Hoag workspace accounts need consolidation
- Pain point: Unwieldy and difficult to manage

**Questions for Discussion:**

1. **Current COA Analysis**
   - Review exported current Core COA structure
   - Identify most frequently used accounts
   - Identify rarely used or duplicate accounts
   - Which accounts are KB-specific vs. Hoag-specific vs. shared?
   - What's causing the 40+ page expansion? (Overly specific accounts? Lack of consolidation?)

2. **Target COA Structure Design**
   - What level of detail do you need for GL reporting?
   - How can we use Classes/Departments/Projects instead of account proliferation?
   - Account numbering scheme preferences?
   - Parent/child account hierarchy needs?
   - Statistical accounts requirements for allocations?

3. **Specific Account Categories**
   - **Revenue accounts:** How many revenue categories do you truly need? (Labor, product, service, other?)
   - **COGS accounts:** Project COGS vs. general COGS structure?
   - **Expense accounts:** G&A categories - what's essential vs. nice-to-have?
   - **Asset/Liability accounts:** Current structure working well or needs changes?
   - **Equity accounts:** Any special tracking needs?

4. **Project vs. G&A Cost Structure**
   - You mentioned needing to "create a cost to go into cost of goods sold, specifically identified as a project cost, and then we have general G&A-type stuff"
   - How many project cost categories do you need?
   - How many G&A expense categories are essential?
   - Can we use segmentation (Projects, Departments) to reduce account count?

5. **15% Labor Markup Impact on COA**
   - If labor markup continues, does it need separate cost accounts?
   - How is the markup line currently coded in GL?
   - "There's no GL impact" was mentioned - clarify how this works
   - How do we maintain Project GP vs. Commissionable GP distinction in COA?

6. **Mapping Strategy**
   - Create mapping document from old COA to new COA
   - Identify accounts that can be consolidated
   - Historical data migration impact - how will mapped accounts affect trend reporting?
   - Training plan - how will users adapt to new account structure?

7. **Special Account Needs**
   - 1099 tracking accounts for vendor payments
   - Intercompany accounts (if any)
   - Clearing accounts for specific processes
   - Suspense accounts for reconciliation
   - Stat accounts for allocations (if implemented)

**Pre-Work Required:**
- Export complete current Core COA with GL account numbers, descriptions, and usage frequency
- Identify top 50 most-used accounts
- List any accounts you know are duplicates or rarely used

**Expected Outcomes:**
- Proposed NetSuite COA structure with account ranges and categories
- Mapping document from old COA to new COA
- Account numbering scheme defined
- Implementation plan with user impact assessment
- Training requirements for new account structure

---

### SESSION 3: Commission Structure & GP Calculation Deep Dive (90 minutes)

**Context:** This is a High Priority requirement with significant impact on sales compensation. The 15% labor markup decision affects commission calculations, and maintaining two GP metrics (Project GP vs. Commissionable GP) requires custom reporting.

**What We Know:**
- **15% labor markup** - automatic rule in Core adds 15% line when labor line entered
- **Purpose:** "Encouraging people to put bigger margins on labor, because labor is inherently unpredictable"
- **Nature:** Cost-only line, bookkeeping mechanism, no GL impact, never cost-prove against these lines
- **Commission impact:** "Commission is paid on that" - after the 15% reduces GP
- **Two GP metrics:**
  - **Project GP:** True gross profit (all revenue minus all costs) - management view
  - **Commissionable GP:** Includes 15% markup, reduces apparent GP - sales view
- **Role-based visibility:** Different people see different KPIs
- **Decision pending:** Matt/Mark deciding whether to continue 15% practice
- **Kipp's opinion:** "I'd be completely in favor of getting rid of it" but acknowledges it's not his decision

**Questions for Discussion:**

1. **15% Labor Markup Decision (Matt/Mark Input Critical)**
   - **DECISION REQUIRED:** Continue 15% labor markup in NetSuite or eliminate?
   - If continuing: Implementation approach (custom script vs. manual process)?
   - If eliminating: What's the communication plan to sales team? Commission impact?
   - Timeline for decision: This affects configuration approach

2. **Markup Mechanics (if continuing)**
   - Currently automatic in Core - do you want automatic in NetSuite?
   - What triggers the markup line? (Product code = labor?)
   - Exact calculation: 15% of labor cost line?
   - Can users override or remove the markup line in specific situations?
   - Does the markup apply to ALL labor or only certain types?

3. **Commission Calculation Details**
   - How exactly are commissions calculated? (% of commissionable GP?)
   - Header-level or line-level commission assignment?
   - Commission splits between multiple sales reps - how allocated?
   - When are commissions paid? (Order booking, invoice, payment collection?)
   - Do different order types have different commission structures?

4. **Project GP vs. Commissionable GP Reporting**
   - Who needs to see Project GP? (Management, finance, operations?)
   - Who needs to see Commissionable GP? (Sales team, account managers?)
   - What specific reports or dashboards are needed for each GP metric?
   - Real-time visibility requirements or month-end reporting sufficient?
   - How do you currently prevent sales team from seeing Project GP if they shouldn't?

5. **Role-Based Visibility & Security**
   - Define specific user roles and what GP metric they see
   - Sales Manager vs. Sales Rep - same or different visibility?
   - Finance team visibility - both metrics or just Project GP?
   - Executive team - which dashboards and metrics?
   - Any situations where someone needs to switch views?

6. **Other Load Factors or Markups**
   - Industry standard is 3% load factor of revenue (vs. your 15% of cost) - any other factors to consider?
   - Any other automatic markups or load factors in your pricing?
   - Design time, PM time - how are these factored in?
   - Overhead allocation - separate from labor markup or related?

7. **KPI Dashboard Requirements**
   - What KPIs do you track for Project GP?
   - What KPIs do you track for Commissionable GP?
   - Project-level dashboards - real-time or scheduled?
   - Sales rep performance dashboards - what metrics?
   - Margin erosion monitoring - thresholds and alerts?

**Expected Outcomes:**
- **DECISION:** 15% labor markup continues or is eliminated
- If continuing: Implementation approach defined (custom script requirements)
- Commission calculation rules fully documented
- GP reporting and dashboard requirements specified
- Role-based permissions matrix defined
- KPI definitions for both GP metrics

---

### SESSION 4: Period Close Process Optimization (60 minutes)

**Context:** Current 10-day period close managed entirely via Excel with no system guidance. NetSuite has built-in Period Close Checklist to replace Excel process. Goal is to reduce timeline and improve efficiency.

**What We Know:**
- Current: 10 days to close via Excel checklist, all manual
- Target: NetSuite Period Close Checklist with system guidance
- Can close AP/AR separately from GL
- Open all 13 periods at year start, close progressively
- Lorraine has prior experience with Blackline/Flowcast in previous roles

**Questions for Discussion:**

1. **Current 10-Day Close Process**
   - Walk through your current Excel checklist - what are the specific steps?
   - Which steps take the longest? (Reconciliations, journal entries, reporting?)
   - What causes delays or bottlenecks?
   - Do you ever close faster than 10 days? What enables that?
   - What's the typical breakdown? (AP close: X days, AR close: Y days, GL close: Z days)

2. **Reconciliation Requirements**
   - Bank reconciliation - frequency and timing within close process
   - Credit card reconciliation - manual or can be automated?
   - Intercompany reconciliations - do you have any?
   - Inventory reconciliation - warehouse physical counts frequency?
   - What reconciliation tolerances are acceptable?

3. **Journal Entry Requirements During Close**
   - What recurring JEs do you process each period?
   - Accruals and prepayments - standard list each month?
   - Allocation journal entries - if implemented, timing?
   - Reversal JEs - how many scenarios will use automated reversals?
   - Who has authority to post JEs during close? (Lorraine, Celine, Kevin, Kipp?)

4. **Close Checklist Customization**
   - What specific steps must be on your NetSuite close checklist?
   - Who's responsible for each step? (Need task assignment)
   - Which steps require approval? (Lorraine sign-off points?)
   - Parallel tasks vs. sequential tasks - what can happen simultaneously?
   - Document attachment requirements - what needs to be uploaded?

5. **Close Timeline Goals**
   - What's a realistic target for NetSuite close timeline? (5 days? 7 days? 8 days?)
   - What's the minimum timeline you could achieve with automation?
   - Soft close vs. hard close - do you do both?
   - Reporting deadlines - when do reports need to be ready after period end?

6. **Period Locking & Controls**
   - After close, who can reopen periods? (Lorraine only?)
   - What circumstances require reopening a closed period?
   - GL audit numbering - do you need to track all reopening activity?
   - Date/period mismatch controls - how strict?

7. **AP/AR Close vs. GL Close**
   - Current process: Do you close AP/AR before GL?
   - NetSuite flexibility: Close modules as ready - preferred approach?
   - What gates require AP to close before moving to GL close?
   - AR aging cutoff - timing and process?

**Expected Outcomes:**
- Detailed current state close process documented
- NetSuite Period Close Checklist customized to KBM needs
- Task assignments and approval gates defined
- Target timeline established (realistic goal)
- Close procedure documentation created
- Training requirements identified for close process

---

### SESSION 5: Bill Payment & Cash Management Workflow Details (45 minutes)

**Context:** Current bill payment process is 90% ACH with manual steps. NetSuite Advanced Electronic Bill Payments will eliminate bank portal upload, but specific workflow details need clarification.

**What We Know:**
- Current: Monday payment runs, sometimes $3M
- Process: Guada/Michael compile → Lorraine reviews → "They always try to kill me with the amounts" → Lorraine picks and chooses → Generate NACHA file → Bank portal upload
- Target: ACH directly from NetSuite, skip bank portal step
- Lorraine approval required as supervisor
- Handful of international wires (expensive)
- Need to register with Coastal or similar payment service provider

**Questions for Discussion:**

1. **Payment Approval Workflow Details**
   - Current: "Lorraine picks and chooses" from proposed payment run
   - NetSuite approach: Can Lorraine remove items from payment batch in system, or does she communicate back to AP team to uncheck items?
   - Preferred workflow in NetSuite?
   - If Lorraine removes items, what happens to those bills? (Automatically move to next payment run?)
   - Does Lorraine ever need to change payment amounts, or only approve/reject entire bills?

2. **Payment Run Compilation**
   - Who decides which bills go into the Monday payment run? (Guada/Michael criteria?)
   - Do you pay by due date, take discounts, or other priority?
   - How do you handle rush payments outside Monday schedule?
   - Early payment discounts - do you track and take advantage?
   - Payment terms optimization - any strategy here?

3. **Remittance Process**
   - Current concern: "If it said we sent it and we didn't, then, you know, that's a problem"
   - NetSuite remittance: Automatic send to vendors or manual trigger?
   - Preferred approach?
   - Remittance format: Email, portal, mail check stub?
   - Remittance detail level: Summary or itemized bill details?

4. **Wire Transfer Handling**
   - You have "handful of wires (international only - expensive)"
   - Confirm: Are wires supported in Advanced Electronic Bill Payments module?
   - If not supported: Continue manual bank portal for wires?
   - Wire approval process: Same as ACH (Lorraine) or additional authorization?
   - Wire templates for common international vendors?

5. **Vendor Prepayments**
   - Marcus mentioned "vendor prepayments support (newer feature)"
   - Which vendors require prepayments?
   - How do prepayments get approved? (Lorraine approves before full payment run?)
   - Prepayment application against future bills - automatic or manual?

6. **Positive Pay Process**
   - West Coast Community Bank positive pay requirements?
   - Do you currently use positive pay?
   - After NetSuite connection: How will positive pay file be generated and transmitted?
   - Exception handling - how do you handle positive pay rejects?

7. **Payment Exceptions & Error Handling**
   - What happens if ACH payment fails? (Vendor bank information wrong, account closed, etc.)
   - Failed payment notification - who receives alerts?
   - Retry process - automatic or manual?
   - Vendor payment information updates - how handled?

8. **Cash Flow Management**
   - Cache360 Dashboard - what cash flow metrics do you want to see?
   - Cash flow forecasting horizon - 30 days? 60 days? 90 days?
   - Pro forma invoices (customer deposits) - integration with cash flow forecast?
   - Payment run impact on cash - do you model cash position before approving large runs?

**Expected Outcomes:**
- Bill payment approval workflow fully defined
- Remittance process confirmed (automatic or manual)
- Wire transfer handling approach determined
- Positive pay process documented
- Payment exception handling procedures defined
- Cash flow management requirements specified

---

### SESSION 6: Expense Management System Decision & Project Coding (45 minutes)

**Context:** Current Expensify process is manual with significant work for users and AP team. Evaluating Expensify Suite App integration vs. switching to RAMP. Critical requirement: Must support project vs. G&A allocation.

**What We Know:**
- Current: Expensify with manual download, manual GL coding, manual reconciliation
- Users resist expense reports: "Who likes to do expense reports? That's why I made Chris buy everything"
- Matt: "I just don't do it. I supposed that my others are cold." - has "a lot of lines that he has to manage"
- Options: Expensify Suite App integration OR RAMP (both have NetSuite integration)
- Critical: Must support allocation to COGS (project costs) vs. G&A (general expenses)

**Questions for Discussion:**

1. **Current Expense Management Pain Points**
   - How many expense reports are submitted monthly?
   - Who are the primary expense report submitters? (Sales team, field team, executives, other?)
   - What's the typical expense report size? (Number of lines, dollar amounts?)
   - Biggest user complaints about Expensify?
   - Biggest AP team complaints about current process?
   - How long does approval and processing typically take?

2. **Project vs. G&A Allocation Requirements**
   - "We have two different... our cost structure, our COA, we had to create a cost to go into cost of goods sold, specifically identified as a project cost, and then we have general G&A-type stuff"
   - What project-related expenses are common? (Travel to job site, client meetings, project meals?)
   - What percentage of expenses are project-related vs. G&A?
   - How granular does project coding need to be? (Project number only, or project + phase/task?)
   - Can one expense report have both project and G&A expenses? (Need line-level coding?)

3. **Expensify Suite App Option**
   - Pros: Continue with known system, users already trained, "absolutely talk to each other, you can just sync data"
   - Cons: Users already don't like it, current user experience is poor
   - If we demo Expensify integration: What must it do to win? (Ease of submission? Auto-sync? Project coding?)
   - Receipts attached in Expensify flow to NetSuite automatically

4. **RAMP Option**
   - Pros: Lorraine interested in switching, "receipt capture from phone, boom, get actually assigned to it" - simpler UX
   - RAMP has NetSuite integration: "RAM doesn't have an integration with NetSuite. It does? Yes."
   - If we demo RAMP: What must it do to win?
   - Change management: Users would need to switch from Expensify to RAMP (training required)
   - Cost comparison: Expensify vs. RAMP pricing

5. **Integration Requirements (Both Options)**
   - Automatic sync from expense platform to NetSuite (eliminate manual download/import)
   - Receipt images attached to expense transactions in NetSuite
   - Project coding fields available in mobile app for ease of use
   - GL account coding: Pre-defined categories or user selects?
   - Department coding: Automatic based on employee or user selects?
   - Credit card integration: Corporate card transactions auto-import to expense reports?

6. **Approval Workflow**
   - Current approval process: Who approves expense reports?
   - Manager approval required before AP processing?
   - Expense policy enforcement: Spending limits, receipt requirements, per diem rates?
   - Out-of-policy expenses: How handled?
   - Reimbursement timing: How quickly do employees get reimbursed?

7. **Credit Card Integration**
   - ARC Bank corporate credit cards: Currently "very manual" reconciliation
   - Can Expensify or RAMP pull in corporate card transactions automatically?
   - NetSuite credit card reconciliation: Upload statement as CSV, auto-match to expense reports?
   - Corporate card vs. personal card expenses: Different handling?

8. **Reporting Requirements**
   - What expense reports do you need? (By employee, by department, by project, by GL account?)
   - Project cost reports: Need to see project-allocated expenses in real-time?
   - Budget vs. actual expense tracking?
   - Expense trends and analysis - what matters most?

9. **Decision Timeline & Next Steps**
   - **Action:** Demo both Expensify Suite App and RAMP integrations
   - When do you want to see demos?
   - Who should attend demos? (Lorraine, Kipp, AP team, sample expense report submitters?)
   - Criteria for decision: User experience, project coding capability, cost, implementation ease?
   - Decision timeline: Before configuration phase or can decide during?

**Expected Outcomes:**
- **DECISION:** Expensify Suite App OR RAMP for NetSuite integration
- Project coding requirements fully documented
- Approval workflow defined
- Credit card reconciliation approach confirmed
- Integration specifications for chosen platform
- Change management plan if switching to RAMP

---

### SESSION 7: Fixed Asset Management Decision (30 minutes)

**Context:** Currently using Bloomberg (third party, additional cost) for fixed asset tax depreciation. Evaluating whether NetSuite Fixed Asset module can replace Bloomberg.

**What We Know:**
- Bloomberg: Third party for tax depreciation, tracks book vs. tax depreciation
- NetSuite FA module: Available, additional cost (~$4,000), "Big SuiteApp module"
- Marcus assessment: "I think the fixed asset module's gonna handle what you need"
- Lorraine: "I just want to know if NetSuite can meet our needs"

**Questions for Discussion:**

1. **Current Fixed Asset Management**
   - How many fixed assets do you currently track?
   - Asset categories: Vehicles, equipment, furniture, leasehold improvements, other?
   - Asset acquisition frequency - monthly additions?
   - Asset disposal frequency - how often?
   - Who manages fixed asset records? (Lorraine, Celine, Kevin?)

2. **Depreciation Requirements**
   - Book depreciation methods used: Straight-line, declining balance, other?
   - Tax depreciation: MACRS, Section 179, bonus depreciation?
   - Different depreciation for book vs. tax - common in your assets?
   - Mid-year conventions: Half-year, mid-quarter, other?
   - Depreciation reports needed: Monthly, quarterly, annual?

3. **Bloomberg Functionality Used**
   - What specific Bloomberg features do you use?
   - What do you like about Bloomberg?
   - What are Bloomberg limitations or pain points?
   - Bloomberg cost: Annual subscription amount?
   - Integration with Core: How does Bloomberg data get into Core GL?

4. **NetSuite FA Module Evaluation**
   - Marcus assessment: NetSuite FA module should handle needs
   - What Bloomberg features are "must-have" in NetSuite?
   - Depreciation calculations: Automatic monthly posting?
   - Asset tagging and physical inventory - do you need this?
   - Asset transfers between locations/departments?
   - Asset split and partial disposal capabilities?

5. **Implementation Considerations**
   - Migration of existing asset records from Bloomberg to NetSuite FA
   - Historical depreciation data - how far back?
   - Asset valuation: Cost, accumulated depreciation, net book value - accurate in Bloomberg?
   - Year-to-date depreciation: Need to import or recalculate in NetSuite?
   - Tax reporting: Forms 4562, state depreciation schedules?

6. **Cost-Benefit Analysis**
   - Bloomberg cost: $X annually
   - NetSuite FA module: ~$4,000 (one-time? annual? - clarify pricing)
   - Integration benefit: Eliminate Bloomberg, consolidate into NetSuite
   - Risk: If NetSuite FA doesn't meet all needs, may need to continue Bloomberg

7. **Decision Timeline**
   - When do you need to decide? (Before configuration or can decide during implementation?)
   - Trial period: Can we test NetSuite FA module with sample assets?
   - Fallback: If NetSuite FA doesn't work, continue Bloomberg temporarily?

**Expected Outcomes:**
- **DECISION:** NetSuite Fixed Asset module OR continue Bloomberg
- If NetSuite FA: Detailed requirements for module configuration
- If NetSuite FA: Migration plan for existing assets from Bloomberg
- If continuing Bloomberg: Integration approach between Bloomberg and NetSuite
- Cost-benefit analysis documented

---

### SESSION 8: Vendor Credit Limit Tracking & Alerts (20 minutes)

**Context:** Pain point identified - KBM hits vendor credit limits unexpectedly, causing "mad scramble at that nth hour" when orders won't process. Need warnings/alerts when approaching limits.

**What We Know:**
- Requirement: Track KBM's credit limits with vendors
- Pain point: "Hit limits unexpectedly: Mad scramble at that nth hour"
- Solution needed: Warnings/alerts at threshold
- REQ-034: Custom alert/warning required (ACCOMMODATE approach)

**Questions for Discussion:**

1. **Current Vendor Credit Limit Issues**
   - How often do you hit vendor credit limits unexpectedly?
   - Which vendors have credit limits that are frequently reached?
   - What's the impact when you hit a limit? (Order delays, rush payments, vendor relationship issues?)
   - Do vendors notify you before you hit the limit, or only when you're over?
   - How do you currently track how close you are to limits?

2. **Vendor Credit Limit Data**
   - Do you have credit limit amounts documented for all major vendors?
   - How do vendors communicate credit limits to you? (Email, portal, contract?)
   - Do credit limits change over time? (Increases based on payment history?)
   - Are limits per location or company-wide?

3. **Warning Threshold Requirements**
   - At what percentage of limit do you want a warning? (Suggested: 90%, but your preference?)
   - Different thresholds for different vendors? (Critical vendors: earlier warning?)
   - Who should receive warning alerts? (Purchasing team, Shannon, AP team, Lorraine?)
   - Alert frequency: Daily check, weekly report, real-time when PO would push over limit?

4. **Alert Mechanism**
   - Email alerts to specified users?
   - Dashboard widget showing vendors approaching limits?
   - Block PO creation if it would exceed vendor credit limit? (Hard stop or just warning?)
   - Report: "Vendor credit utilization" - showing % of limit used for all vendors?

5. **Vendor Credit Limit Tracking**
   - Calculate credit utilization: Open POs + Unpaid bills vs. credit limit
   - Include vendor prepayments in available credit calculation?
   - Real-time tracking or end-of-day batch calculation?

6. **Process When Approaching Limit**
   - What's the ideal process when you receive a 90% limit warning?
   - Expedite payment to that vendor to free up credit?
   - Request credit limit increase from vendor?
   - Defer non-urgent orders until credit available?
   - Who makes the decision on how to handle?

7. **Vendor Credit Limit Management**
   - Where should credit limits be stored in NetSuite? (Custom field on vendor record?)
   - Who updates credit limits when vendors communicate changes?
   - Periodic review: Check with vendors to confirm current limits?

**Expected Outcomes:**
- Warning threshold defined (e.g., 90% of credit limit)
- Alert recipients identified
- Alert mechanism specified (email, dashboard, PO blocking)
- Credit utilization calculation defined
- Custom development requirements documented
- Process for handling warnings established

---

## PART 3: OUTSTANDING DECISIONS REQUIRED

The following strategic decisions are pending and need to be made to proceed with configuration:

### DECISION 1: 15% Labor Markup Continuation
**Decision Maker:** Matt/Mark (Leadership)  
**Timeline:** Before configuration phase  
**Impact:** High - affects commission calculations, project GP visibility, custom development scope  
**Context:** Current Core practice automatically adds 15% cost line when labor entered. Purpose is to encourage higher labor margins due to unpredictability. Kipp is "completely in favor of getting rid of it" but acknowledges it affects commissions.

**Options:**
1. **Continue 15% labor markup in NetSuite** - Requires custom script development to replicate automatic line addition
2. **Eliminate 15% labor markup** - Major process change, affects sales compensation, requires communication plan

**Required for Decision:**
- Commission impact analysis if eliminated
- Sales team input on markup usefulness
- Finance team recommendation
- Custom development cost estimate if continuing

---

### DECISION 2: Automated Allocation Transactions Implementation
**Decision Maker:** Matt/Mark (Leadership)  
**Timeline:** Before configuration phase  
**Impact:** Medium - affects P&L reporting, month-end process  
**Context:** Current state has no allocation transactions in Core - P&Ls with allocations "are just on paper." NetSuite can automate allocations if desired, but it's optional. Lorraine noted "I don't know that he knows that he wants to, or doesn't" and "These numbers were never offered heavy."

**Options:**
1. **Implement automated allocations** - Requires defining allocation rules and logic
2. **Continue paper-only allocations** - Maintain current approach

**Required for Decision:**
- Use case: What would be allocated and why?
- Allocation rules definition
- Benefit vs. complexity analysis
- Leadership prioritization

---

### DECISION 3: Expensify vs. RAMP for Expense Management
**Decision Maker:** Lorraine / Implementation Team  
**Timeline:** During implementation (can schedule demos)  
**Impact:** Medium - user experience, training requirements, cost  
**Context:** Current Expensify process is manual and users resist. Lorraine interested in RAMP. Both have NetSuite integration. Critical requirement: Must support project vs. G&A allocation.

**Options:**
1. **Expensify Suite App integration** - Continue with known system, implement auto-sync
2. **RAMP integration** - Better user experience (per Lorraine), requires change management

**Required for Decision:**
- Demo both options
- Evaluate user experience (mobile app, receipt capture, project coding)
- Compare project coding capabilities
- Cost comparison
- Implementation ease and timeline

---

### DECISION 4: NetSuite Fixed Asset Module vs. Bloomberg
**Decision Maker:** Lorraine / Implementation Team  
**Timeline:** During implementation  
**Impact:** Low-Medium - cost savings vs. functionality risk  
**Context:** Currently paying Bloomberg for tax depreciation (third party). NetSuite FA module costs ~$4,000 but consolidates into single system. Marcus thinks NetSuite FA will handle needs.

**Options:**
1. **NetSuite Fixed Asset module** - Eliminate Bloomberg, consolidate systems, potential cost savings
2. **Continue Bloomberg** - Known functionality, lower implementation risk

**Required for Decision:**
- Detailed NetSuite FA module capabilities review
- Bloomberg comparison for critical features
- Cost-benefit analysis (Bloomberg annual cost vs. NetSuite FA cost)
- Migration complexity assessment

---

### DECISION 5: Payroll Provider (Continue Paylocity or Change)
**Decision Maker:** Lorraine / HR Team  
**Timeline:** Before implementation  
**Impact:** Low - CSV import approach flexible regardless of provider  
**Context:** Currently using Paylocity with CSV journal entry import. "May change" - HR platform evaluation ongoing.

**Options:**
1. **Continue Paylocity** - CSV import approach already understood
2. **Change to new payroll provider** - CSV import still works, may have better HR platform features

**Required for Decision:**
- HR platform evaluation status
- New provider options and capabilities
- Integration approach for any provider (CSV import flexible)
- Timeline for provider decision

---

## PART 4: PRE-WORK & PREPARATION

To make the most of our follow-up sessions, please prepare the following:

### For Chart of Accounts Session:
- [ ] Export complete current Core chart of accounts (account numbers, descriptions, types)
- [ ] Identify top 50 most frequently used accounts
- [ ] List accounts you know are duplicates or rarely used
- [ ] Bring any existing COA consolidation ideas or drafts

### For Commission/GP Session:
- [ ] **Matt/Mark availability confirmation** for 15% labor markup decision
- [ ] Sample commission calculations (how it's currently done)
- [ ] Examples of reports showing Project GP vs. Commissionable GP
- [ ] List of who currently sees which GP metric (role-based visibility)

### For Period Close Session:
- [ ] Current Excel close checklist
- [ ] Breakdown of typical close timeline (which steps take how many days)
- [ ] List of recurring journal entries posted each month
- [ ] Reconciliation procedures and timing

### For Bill Payment Session:
- [ ] Sample payment run details (how Guada/Michael compile, how Lorraine approves)
- [ ] List of vendors requiring prepayments
- [ ] West Coast Community Bank positive pay requirements

### For Expense Management Session:
- [ ] Demo scheduling: Expensify Suite App and RAMP (GSI to coordinate)
- [ ] Sample expense reports showing project vs. G&A allocation needs
- [ ] Current Expensify usage metrics (reports/month, users, costs)
- [ ] List of primary expense report submitters to invite to demos

### For Fixed Asset Session:
- [ ] List of fixed assets currently in Bloomberg (categories, quantities)
- [ ] Bloomberg feature list (what you use, what you need)
- [ ] Bloomberg annual cost
- [ ] Sample depreciation report from Bloomberg

### For Vendor Credit Limit Session:
- [ ] List of vendors with credit limits and limit amounts
- [ ] Examples of recent credit limit issues
- [ ] Identify who should receive credit limit warning alerts

---

## PART 5: SESSION DELIVERABLES & SUCCESS CRITERIA

At the completion of these follow-up sessions, we will have:

### Documentation Deliverables:
1. **Revenue Recognition Rules Document** - Detailed rules by order type, special scenarios, compliance requirements
2. **Proposed NetSuite Chart of Accounts** - Structure, numbering scheme, mapping from old to new
3. **Commission Structure Specification** - GP calculation rules, role-based visibility matrix, KPI definitions
4. **Period Close Procedures** - Customized NetSuite checklist, task assignments, target timeline
5. **Bill Payment Workflow Documentation** - Approval process, remittance handling, exception procedures
6. **Expense Management Solution Selection** - Chosen platform, integration specs, implementation plan
7. **Fixed Asset Management Decision** - Module selection, requirements, migration approach
8. **Vendor Credit Limit Alert Specification** - Threshold, alert mechanism, custom development scope

### Decisions Finalized:
- [ ] 15% labor markup: Continue or eliminate (Matt/Mark)
- [ ] Automated allocations: Implement or continue paper-only (Matt/Mark)
- [ ] Expense management platform: Expensify or RAMP (Lorraine)
- [ ] Fixed assets: NetSuite FA module or Bloomberg (Lorraine)
- [ ] Payroll provider: Paylocity or new provider (Lorraine/HR)

### Requirements Confirmed:
- [ ] Revenue recognition rules validated for compliance
- [ ] Chart of accounts structure approved by finance team
- [ ] Commission calculations documented and approved
- [ ] Period close checklist customized and approved
- [ ] Bill payment workflow confirmed
- [ ] Expense management project coding requirements confirmed
- [ ] Vendor credit limit tracking requirements specified

### Implementation Impact Assessed:
- [ ] Custom development scope identified (labor markup, GP reporting, vendor alerts, etc.)
- [ ] Training requirements identified for COA changes
- [ ] Change management plan for expense platform (if changing)
- [ ] Data migration complexity assessed (COA mapping, fixed assets)
- [ ] Timeline impact understood (decisions affect configuration sequencing)

---

## PART 6: NEXT STEPS AFTER FOLLOW-UP SESSIONS

Once these follow-up sessions are complete:

1. **Update Business Requirements Document (BRD)** - Incorporate all clarifications and decisions
2. **Finalize Requirements Map** - Confirm ALIGNS/ADAPT/ACCOMMODATE classifications
3. **Solution Design Phase** - Begin detailed design for ACCOMMODATE requirements (custom development)
4. **Configuration Planning** - Sequence configuration tasks based on dependencies
5. **Data Migration Planning** - Finalize data migration scope and approach
6. **Integration Specifications** - Detail integration requirements for expense platform, banking, etc.
7. **Training Plan Development** - Identify training needs based on requirements
8. **Go-Live Planning** - Incorporate decisions into go-live approach and timeline

---

## APPENDIX: REFERENCE MATERIALS

### Related Documents:
- **Questionnaire_FinancialManagement_v1.0.md** - Comprehensive questionnaire with 38 requirements
- **Requirements_Map_FinancialManagement_v1.0.md** - 38 requirements classified by implementation approach
- **Master_Transcript_FinancialManagement.md** - Full transcript from discovery sessions
- **Discovery_Master_Outline_Answered.md** - Overall project discovery status

### Key Requirements Requiring Follow-Up:
- **REQ-016:** Chart of Accounts consolidation (ACCOMMODATE) - Session 2
- **REQ-019:** Automated allocations decision (ADAPT) - Decision 2
- **REQ-023:** 15% labor markup decision (ADAPT) - Session 3, Decision 1
- **REQ-024:** Project GP vs. Commissionable GP reporting (ACCOMMODATE) - Session 3
- **REQ-025:** Role-based permissions for GP visibility (ACCOMMODATE) - Session 3
- **REQ-026:** Fixed Asset module evaluation (ADAPT) - Session 7, Decision 4
- **REQ-034:** Vendor credit limit tracking (ACCOMMODATE) - Session 8
- **REQ-035:** Revenue recognition rules (ACCOMMODATE) - Session 1
- **REQ-013/014:** Expense management platform (ALIGNS) - Session 6, Decision 3

### Contact Information:
- **Primary Contact:** Lorraine (CFO/Controller)
- **Technical Contact:** Kipp (Former Controller/IT)
- **GSI Lead:** Mark (Implementation Lead)
- **GSI Technical:** Gary (Technical Lead)

---

**Document Version:** 1.0  
**Created:** October 2025  
**Next Review:** After follow-up sessions completed  
**Status:** Ready for scheduling


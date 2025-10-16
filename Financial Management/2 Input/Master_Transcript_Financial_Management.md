# MASTER TRANSCRIPT: FINANCIAL MANAGEMENT
## KBM Hoag NetSuite Orion Implementation

**Sources Combined:**
- GMT20250918-211018_Recording.transcript.vtt (September 18, 2025 - Financial Management Session)
- Financial Mgmt.txt (Compiled notes from July 30, 2025)
- Relevant portions from 07-30 Meeting_ NetSuite Workflow & Transaction Management.txt

**Date Range:** July-September 2025
**Business Process:** Financial Management (Accounting, GL, AP, AR, Banking, Reporting, Closing)

---

## EXECUTIVE SUMMARY

Financial Management at KBM Hoag involves a lean but mighty finance team managing a $100M dealer operation with a complex cost structure, 13-period accounting calendar, multi-workspace consolidation, and sophisticated project accounting. The current Core system has limitations in areas like chart of accounts management (40+ pages), period close process (10 days via Excel), limited labor markup automation (15% contingency line), and manual expense management through Expensify. NetSuite/Orion will enable automation through bank feeds, electronic bill payments, integrated expense management, automated period close checklists, and improved financial reporting with real-time dashboards.

**Key Themes:**
- Lean finance team managing $100M operations
- 15% labor markup (cost-only contingency line)  
- Project GP vs. Commissionable GP distinction
- Chart of accounts simplification (40+ pages → few hundred accounts)
- 10-day period close (Excel-based currently)
- Bank feeds and electronic payments (ACH/wire)
- Expensify integration for expense management
- 13 accounting periods, calendar year
- Fixed asset management (Bloomberg currently, evaluating NetSuite module)

---

## FINANCE TEAM STRUCTURE

### Team Members

**Core Finance Team:**
- **Lorraine** - CFO/Controller ("mighty finance team... lean, but mighty GP")
- **Guada** - Accounts Payable (Dynamic Duo #1)
- **Michael** - Accounts Payable, Philippines-based (Dynamic Duo #2)
- **Celine** - General Ledger  
- **Kevin** - General Ledger
- **[AR Person]** - San Jose office

**Finance Partner:**
- **Kipp** - Former Controller, now IT specialist
  - "He touches everything"
  - "Free safety" (football analogy)
  - Still leveraged heavily for finance duties
  - 15 years at company
  - Involved in all finance-related decisions

**Quote from Speaker:**
"The other finance partner is Kip, because he has his hands in everything that we do. He's everywhere. He's got the ball trades. The free safety... He used to be a controller here. And then he went in and specialized into IT kind of stuff, but he still kept a lot of his duties, and we still leverage him for a lot of stuff that he does on board."

---

## COMPANY STRUCTURE & SETUP

### Subsidiary Structure

**Decision: One Subsidiary**
- Single NetSuite subsidiary
- KB + Hoag merged operations
- Consolidated financial reporting
- Locations for different offices/warehouses

### Accounting Periods

**Current (Core):**
- 12 accounting periods
- Calendar year basis

**Future (NetSuite):**
- **13 accounting periods** (Lorraine's preference)
- Calendar year (January 1 - December 31)
- "I would like 13. 13. Core only does 12. Okay. So it was, like, 13. Yep."

**Period Management:**
- Open whole year at once
- Set December reminder to open next year
- Avoid opening more than one year in advance (prevents future-date transaction errors)
- Can close AP/AR separately from GL through checklist

### Currency

**US Dollar Only:**
- No multi-currency requirements
- All operations in USD
- "We're all in U.S. dollar"

---

## TAX MANAGEMENT

### Sales Tax - SuiteTax

**Implementation:**
- 48 states with nexus registration
- Automatic calculation based on ship-to address
- Native SuiteTax (not Avalara)
- Tax exemption certificate management
- Effective date tracking
- Dashboard for expiring certificates
- Compliance reporting

**Benefits:**
- "You get a beautiful report"
- Automatic application once customer certificate loaded
- No manual intervention needed for future quotes

**Government Orders Tax Complexity:**
- See Order Management transcript for detailed Miller Knoll direct bill tax issues
- Tax override capability available when needed

### Use Tax

**States Requiring Use Tax:**
- Illinois
- Missouri
- Different nexus definitions
- Current: TaxConnect third party handles
- Core won't do use tax: "have to kind of trick it"

**Kipp Quote:**
"There... yeah, they're the exceptions there, or else it's sales tax. And CORE won't do use tax, so we have to kind of trick it."

### Gross Receipts Tax

**Requirement:**
- Generate reports based on ship-to location
- Currently: Data dump from Core
- "Run it so infrequently, I'm sure it's on my calendar"

**NetSuite Solution:**
- Standard SuiteTax report
- Ship-to location is standard calculation method
- Native functionality, no custom development

**Kipp:**
"We need the sales... sales revenue number based on ship to location. Is that something we would set up?"

**Marcus:**
"That's... isn't ship to location is the standard way of calculating it, right? Yes, exactly. So then, yeah, that's... that'll be your sweet text report, your native suitext report."

### Fixed Asset Tax Depreciation

**Current State:**
- Bloomberg (third party) for tax depreciation
- Book depreciation vs. tax depreciation

**NetSuite Option:**
- Fixed Asset (FA) module available
- Additional cost (~$4,000)
- Need to determine if NetSuite can meet all needs
- "I think the fixed asset module's gonna handle what you need"

**Decision Point:**
- Evaluate NetSuite FA module vs. continuing Bloomberg
- Open question during discovery

---

## JOURNAL ENTRIES & ALLOCATIONS

### Journal Entry Functionality

**Import Capability:**
- CSV import of journal entries
- Payroll entries imported from Paylocity
- Can do department allocations before import
- Automated reversal journal entries

**Reversal Entries:**

**Lorraine:**
"That practice, though? Oh, you have? Okay. Because we couldn't keep track of them."

**Current Challenge:**
- Core doesn't have automated reversal
- Tracking reversals manually is problematic

**NetSuite Benefit:**
- Automatic reversal journal entries
- Better tracking
- One scenario planned for automated reversal (to be detailed later)

### Allocations

**Current State:**
- Manual allocations
- "P&Ls that show allocation, they're just on paper"
- Don't create allocation transactions in Core
- "We don't have it"

**Future State (NetSuite):**
- Optional to implement
- Decision pending with leadership
- "I don't know that he knows that he wants to, or doesn't"
- "These numbers were never offered heavy"

**Implication:**
- May continue manual/paper allocations
- NetSuite capability available if needed

---

## BANKING & CASH MANAGEMENT

### Cash Flow Forecasting

**NetSuite Feature:**
- Cache360 Dashboard
- Cash flow forecasting functionality
- Part of configured system
- Pro forma invoice as additional data point (doesn't auto-flow to dashboard)

### Bank Feeds

**Current Bank:**
- West Coast Community Bank
- Confirmed as part of NetSuite Bank Feeds program

**Functionality:**
- Automatic transaction feed into NetSuite
- Auto-matching capability
- Create rules to improve matching over time
- Similar process for both bank and credit card reconciliation

**Benefit:**
- Automated reconciliation
- Reduced manual data entry
- Rule-based matching improves over time

### Electronic Bill Payments (ACH)

**Current Process:**
- Run check run in Core
- Generate HTML file (NACHA format)
- Log into bank portal
- Upload file
- Verify amounts
- Bank pushes payments to vendors

**NetSuite Capability:**
- **Advanced Electronic Bill Payments** (part of edition)
- Pay via ACH directly from NetSuite
- Vendor prepayments support (newer feature)
- Skip manual bank portal upload step
- "Payments get pushed to vendors straight from [NetSuite]"

**Fallback:**
- If bank integration issue: NACHA file upload
- Similar to current process
- "Depends on what template your bank uses"

**Service Provider:**
- Register with Coastal (or similar service)
- Third-party payment processor

**Current Volume:**
- 90% ACH
- Handful of wires (international only - expensive)
- Some credit card activity

**Wire Transfers:**
- Wires restricted to international (expensive)
- ACH is cheap
- Module question: ACH only or wire support too?
- If not integrated: Manual entry in bank portal (current process for wires)

### Payment Approval Workflow

**Current Process:**
- Guada or Michael compile proposed payment run
- Bring to Lorraine with amounts (sometimes $3M)
- "They always try to kill me with the amounts, because they'd just erode all our cash"
- Lorraine reviews and approves
- AP team must click to pay in Core
- Lorraine picks and chooses
- AP team unchecks items Lorraine rejects

**NetSuite Process:**
- Similar approval workflow
- Bill payment transaction pays multiple bills
- Payment method defines ACH vs. other
- Supervisor approval required
- AP compiles, Lorraine approves
- Open question: Can Lorraine remove items or must communicate back to AP?

**Monday Payment Process:**
- Regular Monday payment runs
- Proposed run brought to Lorraine
- Selection/approval process
- Then execution

**Action Items:**
- Confirm exact approval workflow steps
- Determine if approver can edit payment selection
- Confirm remittance process (automatic or manual trigger)
- "If it said we sent it and we didn't, then, you know, that's a problem" (Lorraine concern)

### Positive Pay

**Current Requirement:**
- Must go into bank portal for positive pay review
- Validates transactions

**NetSuite Question:**
- Bank connected to NetSuite
- Validate transactions in NetSuite
- Still need bank portal for positive pay?
- "Haven't talked to the bank about being connected to NetSuite"
- "Our current process requires us to do that, but we don't know if the new process will require us to do"

**Action Item:**
- Confirm with bank: Positive pay process with NetSuite bank feeds
- Determine if bank portal still needed

---

## CREDIT CARD MANAGEMENT

### Corporate Credit Cards

**Current Bank:**
- ARC Bank
- "Very manual process, how we get it into the GL"

**NetSuite Approach:**
- Treat credit card like another bank account
- Upload statement (likely CSV)
  - Not live feed (likely)
  - Manual export/import
- Use same reconciliation process as bank account
- "A lot easier"

**Benefit:**
- Consistent reconciliation process
- Automated matching
- Reduced manual entry

### Expense Management - Expensify

**Current Process:**
1. Users create expense reports in Expensify
2. Attach receipts
3. Code transactions
4. System generates file
5. AP team manually downloads
6. Manual coding into GL
7. "Obviously a lot of work there up front"

**User Challenge:**
- Matt has "a lot of lines that he has to manage"
- Matt: "I just don't do it. I supposed that my others are cold."
- Manual reconciliation of expense reports to bank statement

**NetSuite Solution:**
- **Expensify Integration** (Suite App available)
- "Absolutely talk to each other. You can just sync data"
- Automated data sync from Expensify to NetSuite
- Receipts attached in Expensify flow to NetSuite

**Alternative: RAMP**
- Lorraine interested in moving from Expensify to RAMP
- RAMP has NetSuite integration too
- "RAM doesn't have an integration with NetSuite. It does? Yes."
- Could potentially demo both

**User Experience Benefit:**
- Receipt capture from phone
- "Boom, get actually assigned to it"
- Simplified expense submission
- "Who likes to do expense reports? That's why I made Chris buy everything"

**Action Item:**
- Evaluate Expensify vs. RAMP integration
- Demo both if needed
- Determine which better fits workflow

### Expense Report Allocation

**Cost Structure Question:**
- Travel reimbursement allocation
- Two different cost categories:
  1. **Cost of Goods Sold** - project costs (specific project allocation)
  2. **G&A** - general administrative expenses

**Lorraine:**
"We have a... we have two different... Again, our cost structure. our COA, we had to, create a cost to go into cost of goods sold, specifically identified as a project cost, and then we have general G&A-type stuff"

**Implication:**
- Expense reports must allocate to project or G&A
- Project-related travel = COGS
- General travel = G&A
- Integration must support project coding

### Accepting Credit Card Payments

**NetSuite Capability:**
- Can accept credit cards
- PCI/DSS compliant
- Multiple payment processors available

**Current State: Stripe**
- Payment link embedded in invoice hyperlink
- URL sent to clients for payment portal
- "She built it for us, and she's hosting it"
- Pay annual hosting fee (~$100)

**Frequency:**
- "Very rare we take a credit card"
- Try to avoid because of fees
- But available as option for clients

**Processing Fees:**
- Plan on 3% (rewards cards cost more)
- "Rewards cards, you get homes with those rewards cards. It's the biggest scam ever. Get the merchant pay for it."
- Stripe: Transaction-based pricing only (no monthly fee currently)

**NetSuite Options:**
- Multiple payment processors available
- All charge similar transaction fees
- Fee based on transaction volume
- Could consolidate if NetSuite option equivalent

**Primary Use Case:**
- Payment link in invoice for convenience
- Self-service payment portal
- Most dealers use for this reason

**Decision:**
- Stay with Stripe currently (works fine, incidental use)
- No rush to change
- "If you're using Stripe, you're fine, and if you... it's, like, incidental, then..." (Marcus)

---

## 15% LABOR MARKUP (CONTINGENCY LINE)

### The Practice

**Automatic Calculation:**
- Core rule: If labor line entered (product code = labor)
- System automatically adds 15% line
- Example: $100 labor → auto-add $15 line

**Purpose:**
"It's encouraging people to put bigger margins on labor, because labor is inherently unpredictable. Product, very predictable, you spend in the PO, you get back in development, it's not gonna change. Labor, you're guessing. Until you get in the field and start doing things."

**Nature:**
- Cost-only line (no revenue impact)
- Bookkeeping mechanism
- "Never really any... it's just the bookkeeping thing"
- Never cost-prove against these lines
- No external impact

### Financial Impact

**General Ledger:**
- "There's no GL impact"
- Doesn't hit actual financials

**Project GP:**
- Inflates cost
- Reduces margin
- Affects project GP calculations
- **Affects commission** (commission paid after the 15% reduces GP)

**Load Factor Concept:**
- Functions as load factor
- Covers risk/contingency
- Meant to cover labor unpredictability

### Industry Comparison

**Other Dealers:**
- Common practice, but usually lower percentage
- Typically 3% load factor
- Covers design and PM time
- Usually calculated as 3% of **revenue** (vs. KBM's 15% of **cost**)

**Why KBM's is Higher:**
- 15% of cost vs. others' 3% of revenue
- Different calculation base
- "That's why it's higher"

### Two GP Metrics

**Project GP:**
- True gross profit
- All revenue minus all costs
- What management monitors
- Year-to-date view shows true margin

**Commissionable GP:**
- Includes 15% labor markup
- Reduces apparent GP
- Used for commission calculation
- Different KPI set

**Kipp:**
"In order to see the true margin of the projects, then we have to run year-to-date data then, right? So, it flats out. So, what we do is, that's why we have two... that's why we have a different set of KPIs. So, we have a set of KPIs for project gross profit, and then we have commissionable gross profit, and then commissionable gross profit includes things like the head factor."

**Permission Control:**
- Different people see different KPIs
- Role-based visibility
- Sales may see commissionable GP
- Management sees true project GP

### Future of 15% Rule

**Up for Debate:**
- "That may be up for debate as to whether or not we would want to keep that"
- Matt and Mark decision
- Kipp mentioned Matt was discussing it
- Kipp: "I'd be completely in favor of getting rid of it, but I don't... that's not my [decision]"

**Commission Impact:**
- "Commission is paid on that"
- Changing it would affect commission calculations
- Significant operational change

**Decision:**
- Will ask Matt/Mark for final decision
- May continue or eliminate
- Can be replicated in NetSuite if continuing

---

## PERIOD CLOSE PROCESS

### Current Process

**Timeline:**
- **10 days** to close accounting period
- All managed via Excel
- No system-guided process

**Tools:**
- Excel for tracking
- Manual checklist
- No integrated close management

**Previous Experience (Lorraine):**
- Used Blackline or Flowcast in prior roles
- Online systems for close management
- Connect to ERP but separate tool
- Attach documents and track progress

### NetSuite Period Close

**Built-in Checklist:**
- Period closing checklist feature
- Step-by-step process
- Quick walk-through mode
- System-guided close
- "Pretty quick"

**Recommendation:**
- Use NetSuite native checklist (Marcus)
- No need for separate Blackline/Flowcast

**Module Closing:**

**Current Core:**
- AP/AR module close separately from GL module
- Can open/close individually

**NetSuite:**
- Can close AP/AR separately and go through checklist
- Flexible closing process
- Close modules as ready

### Period Opening

**Best Practice (Marcus):**
- Open entire year at once
- Set December reminder to open next year
- Prevents forgetting in January
- "Can't tell you how many times we stumbled into January and we couldn't do transactions, because we've got to open up the next accounting period year"

**Caution:**
- Don't open more than one year ahead
- Risk: People select future transaction dates by mistake
- Throws off reporting

**13-Period Calendar:**
- Open all 13 periods for year
- Close periods as completed
- Ability to reopen if needed

---

## CHART OF ACCOUNTS

### Current State

**Volume:**
- **40+ pages of accounts** in Core
- Unwieldy and difficult to manage
- Need for consolidation

**Target State:**
- **"Few hundred accounts"** (target reduction)
- Streamlined structure
- Cleaner reporting

**Workspaces:**
- KB workspace accounts
- Hoag workspace accounts  
- Consolidated view needed

### Historical Data

**Retention Decision:**
- Back to **2017** (Lorraine's decision)
- "Historical data back to 2017"
- Older data exported and archived
- Separate archive system

**Lorraine:**
"Fee side and view side data usage" - determine what's truly needed

### Data Migration Strategy

**Typical Approach:**
- End-of-month trial balances
- 2-5 years typical import
- Up to 10 years possible
- CSV import process
- Period-over-period reporting capability

**Core Data Export:**
- SQL backend access confirmed
- Data migration tool available
- Strategy: Avoid Core involvement (backdoor access)
- Direct data extraction

---

## CUSTOMER FINANCIAL MANAGEMENT

### Finance Charges

**Capability:**
- Global on/off switch
- Shows on statements and invoices
- Automatic calculation if enabled

**Current Use:**
- **Never implemented in 13 years** (Lorraine)
- Deterrent/threat only
- "Most dealers want to threaten. They don't actually follow through, which I get it because you want to keep your customers happy, too"

**Functionality:**
- 90-day invoice → auto-add finance charge line
- Or manually add as line item
- Typically not used

### Storage Fees

**See Order Management transcript for full details**

**Summary:**
- Vary by warehouse (30-90 days free)
- Bill back to client (typically)
- Mark up storage costs
- Sometimes absorbed as customer accommodation
- Impact on commission (line-level marking)

### Project Accounting

**Two GP Concepts:**

1. **Project GP** - True gross profit (everyone monitors)
2. **Commissionable GP** - For commission calculation (includes 15% labor markup)

**Line-Level Commission Marking:**
- Individual lines marked commissionable or not
- Header: Who gets commission, percentage/split
- Flexibility for storage fees, accommodations, etc.

**Time Tracking Impact:**
- Internal labor rates affect project GP
- External contractor rates
- Manual reconciliation
- GP impact tracking

---

## ACCOUNTS PAYABLE MANAGEMENT

### Vendor Management

**Intermarket:**
- Dealers must be set up as both vendor AND customer
- Pain point for first-time dealer setup
- High volume (Shannon: hundreds of outbound transactions)

**Credit Limits:**
- Track KBM credit limits with vendors
- Hit limits unexpectedly: "Mad scramble at that nth hour"
- Need warnings/alerts

### Bill Payment Process

**See Banking section for detailed payment workflow**

**Summary:**
- Monday payment runs (Guada/Michael compile)
- Lorraine review and approval
- ACH primary method (90%)
- Wires for international
- Some credit card payments

### Vendor Invoices

**Product Coordinators (Shannon's Team):**
- Work with Guada heavily
- "She deals with a lot of the product coordinators"
- Vendor invoice coordination
- PO reconciliation

---

## ACCOUNTS RECEIVABLE MANAGEMENT

### Customer Deposits

**Pro Forma Invoice:**
- Not revenue-recognizing transaction
- Liability account
- Deposit collection
- Automatically applies to final invoice when generated

**See Order Management transcript for details on:**
- Customer deposit process
- Proposal-level deposit collection
- Auto-application to sales order and invoice

### Collections

**Finance Charges:**
- Available but not used (see Customer Financial Management)

### Customer PO Tracking

**See Order Management transcript for comprehensive details**

**Bank Requirement:**
- Bank requesting PO reporting
- Total project value, POs against project, open balance
- Never able to provide this data historically
- Custom solution planned in NetSuite

---

## REVENUE & COST RECOGNITION

### Current Process

**Sales Order = Revenue Recognition:**
- "Sales order = revenue recognition"
- Static process after quote creation
- No changes after sales order booked

**Live Budget Tracking:**
- Google Docs for live budget
- Collaborative, real-time changes
- Then → create proposal (static)
- No changes after proposal
- "We really live in a world of collapsed"

### NetSuite Approach

**Separate Transactions:**
- Opportunity → Quote → Sales Order
- Each transaction separate and linked
- Better audit trail
- Can compare quote to sales order (if changes occur)

**Project-Level Tracking:**
- All transactions linked to project
- Project-level revenue/cost aggregation
- KPI dashboard at project level

**Recognition Timing:**
- Decision point: When does revenue recognize?
- Typically at sales order or invoice
- May need special rules for certain order types

**White Paper:**
- Marcus mentioned working on white paper
- Review on screen during session
- Detail NetSuite revenue recognition differences

**Note:** Full revenue recognition discussion likely continued but not captured in transcript excerpts reviewed.

---

## PAYROLL INTEGRATION

### Current System

**Paylocity:**
- Current payroll provider
- "May change" (evaluation ongoing)
- Separate from NetSuite
- HR platform evaluation in progress

**Integration Method:**
- CSV download from Paylocity
- Journal entry import to NetSuite
- "Currently, we're getting the data done from Paylocity, and we just upload that data to Core"

**Department Allocation:**
- Allocations done before import
- Identify departments in JE before importing
- Then import as journal entry

**Future State:**
- Same CSV import process
- May have different payroll provider
- Integration approach remains similar
- Automated reversal JE capability in NetSuite (benefit over Core)

---

## FIXED ASSET MANAGEMENT

### Current Solution

**Bloomberg:**
- Third-party for tax depreciation
- Separate from Core
- Tax vs. book depreciation tracking

### NetSuite Fixed Asset Module

**Option:**
- NetSuite FA module available
- Additional cost (~$4,000)
- "Big SuiteApp module"
- Edition determination pending

**Lorraine's Question:**
"I just want to know if NetSuite can meet our needs, and do we need that fixed asset stuff? [Currently] paying for a third party to do that. Bloomberg."

**Marcus Assessment:**
"I think the fixed asset module's gonna handle what you need."

**Decision:**
- Evaluate NetSuite FA module capabilities
- Compare to Bloomberg functionality
- Cost-benefit analysis
- May eliminate Bloomberg if NetSuite sufficient

---

## BUDGETING & PLANNING

**Topic Mentioned:**
- On agenda for financial management session
- No specific details captured in transcript excerpts

**Likely Topics:**
- Project budgeting (Google Docs live budgets currently)
- Annual budgeting process
- Budget vs. actual reporting
- Forecasting

---

## FINANCIAL REPORTING & ANALYTICS

### Current Tools

**Reporting:**
- Core financial reports
- Manual Excel reports
- Google Sheets
- Power BI integration

### NetSuite Capabilities

**Features:**
- Real-time reporting
- Period-over-period analysis
- Custom dashboards
- Automated report generation
- Export capabilities (Excel, PDF, CSV)

**Project-Level:**
- KPI dashboards
- Real-time GP visibility
- Revenue/cost tracking
- Commission reporting

**Financial:**
- P&L by period
- Balance sheet
- Cash flow
- Trial balance
- Custom financial reports

### Business Intelligence

**Separate Session:**
- Dedicated BI/reporting session planned
- "We have an official session on business intelligence as well"
- Reporting "falls in every process area"

---

## COMMISSIONS

**Not on Original Agenda:**
- "Missions is not on there"
- Added during session
- Significant topic

**See Order Management transcript for:**
- Commission structure (header/line level)
- Project GP vs. Commissionable GP
- 15% labor markup impact
- Split commissions
- Non-commissionable lines

---

## INTEGRATIONS & THIRD-PARTY SYSTEMS

### Banking

**West Coast Community Bank:**
- Bank feeds (Suite App)
- Advanced Electronic Bill Payments
- Automated reconciliation
- Positive pay (process TBD)

### Expense Management

**Expensify:**
- Current system
- NetSuite Suite App available
- Auto-sync capability

**RAMP:**
- Alternative being evaluated
- NetSuite integration available
- Mobile receipt capture

### Payroll

**Paylocity:**
- Current provider
- May change
- CSV import of journal entries
- HR platform evaluation in progress

### Payment Processing

**Stripe:**
- Credit card payment processing
- Invoice payment links
- Portal for client payments
- Transaction-based pricing
- ~$100/year hosting fee

### Tax

**TaxConnect:**
- Current third party
- Handles use tax for Illinois/Missouri
- Will transition to SuiteTax in NetSuite

### Fixed Assets

**Bloomberg:**
- Tax depreciation
- May replace with NetSuite FA module

---

## DATA MIGRATION

### Historical Data

**Financial Data:**
- 2017 forward into NetSuite
- Older data: Export and archive
- Separate archive system
- Trial balance imports (end-of-month)

**Decision Authority:**
- Lorraine determines retention needs
- "Fee side and view side data usage"
- Balance history needs vs. system complexity

### Core Data Access

**SQL Backend:**
- Confirmed access to SQL backend
- Data migration tools available
- Strategy: Avoid Core vendor involvement
- Backdoor extraction approach

**Migration Scope:**
- 2-5 years typical
- Up to 10 years possible
- Period-over-period reporting needs drive decision

---

## COMPLIANCE & AUDITING

### Audit Requirements

**Direct Bill:**
- Gross-up approval from auditors
- Commission structure documentation
- Revenue recognition verification

**Tax Compliance:**
- Sales tax reporting (48 states)
- Use tax filing (IL, MO)
- Gross receipts tax reports
- Tax exemption certificate management

### Internal Controls

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
- 10-day close currently
- Checklist-driven process
- Review and reconciliation
- Close audit trail

---

## DECISION POINTS & ACTION ITEMS

### Decisions Made

1. **13 Accounting Periods** - Calendar year
2. **SuiteTax** - For sales tax (not Avalara)
3. **Bank Feeds** - Implement with West Coast Community Bank
4. **Electronic Bill Payments** - Implement ACH (Advanced Electronic Bill Payments module)
5. **Expensify Integration** - Evaluate (may also demo RAMP)
6. **NetSuite Period Close Checklist** - Use native functionality
7. **Open Full Year** - All periods at once, close as go
8. **Chart of Accounts Cleanup** - Reduce from 40+ pages to few hundred accounts

### Open Questions/Action Items

1. **Fixed Asset Module:**
   - Evaluate NetSuite FA module vs. Bloomberg
   - Cost-benefit analysis
   - Determine if meets all needs

2. **15% Labor Markup:**
   - Matt and Mark to decide: Keep or eliminate?
   - Impacts commission calculations
   - Affects project GP visibility

3. **Expensify vs. RAMP:**
   - Demo both integrations
   - Evaluate user experience
   - Determine best fit for workflow
   - Project coding capability

4. **ACH Payment Process:**
   - Confirm exact approval workflow
   - Can Lorraine remove items or only approve/reject whole run?
   - Remittance auto-send or manual trigger?
   - Wire transfer support in module?

5. **Positive Pay:**
   - Confirm process with bank
   - Bank portal still needed with NetSuite integration?
   - Validation workflow

6. **Allocations:**
   - Do they want to implement automated allocations in NetSuite?
   - Or continue manual/paper process?
   - Decision pending

7. **Payroll Provider:**
   - Continue Paylocity or change?
   - HR platform evaluation status
   - Integration requirements

8. **Revenue Recognition:**
   - Detailed rules and timing
   - White paper review
   - Special scenarios

9. **Historical Data Migration:**
   - Final decision on years to import
   - Trial balance dates
   - Archive strategy for older data

### Documentation Needed

1. **Bank Integration Details:**
   - Advanced Electronic Bill Payments process flow
   - Positive pay workflow
   - Bank feeds setup requirements

2. **Expense Management:**
   - Expensify integration guide
   - RAMP integration guide  
   - Project coding requirements

3. **Period Close Checklist:**
   - NetSuite standard checklist
   - KBM-specific customizations needed
   - 10-day timeline goals

4. **Chart of Accounts:**
   - Current COA export from Core
   - Proposed new structure
   - Mapping document

5. **Revenue Recognition White Paper:**
   - NetSuite approach
   - KBM-specific scenarios
   - Implementation plan

---

## PAIN POINTS TO SOLVE

### Current Frustrations

1. **40+ Page Chart of Accounts:**
   - Unwieldy and hard to manage
   - Need consolidation
   - Cleaner reporting structure

2. **10-Day Period Close:**
   - All manual via Excel
   - No system guidance
   - Tracking challenges
   - Want to reduce timeline

3. **Manual Expense Management:**
   - Expensify → manual download → manual GL coding
   - "Obviously a lot of work there up front"
   - Users don't like creating expense reports
   - Reconciliation time-consuming

4. **Manual Payment Processing:**
   - Core report → bank portal → upload NACHA → verify
   - Extra step vs. direct ACH from system
   - "It is not a big-time stuff right now, but... one less step, great"

5. **AP/AR Module Separation:**
   - Manual clicks to open/close
   - Tracking which is open/closed
   - No integrated checklist

6. **No Automated Reversal JEs:**
   - "We couldn't keep track of them" in Core
   - Manual reversal management
   - Error-prone

7. **Use Tax Workaround:**
   - "CORE won't do use tax, so we have to kind of trick it"
   - IL and MO special handling
   - Manual process

8. **Credit Card Reconciliation:**
   - "Very manual process, how we get it into the GL"
   - Separate from bank reconciliation
   - Inefficient

9. **No Real-Time Reporting:**
   - Reliance on Excel
   - Manual report creation
   - Period-over-period comparisons difficult

10. **Bloomberg Cost:**
    - Third-party fixed asset management
    - Additional software cost
    - May be redundant with NetSuite FA module

### Future State Solutions

1. **Chart of Accounts Cleanup:**
   - Few hundred accounts (down from 40+ pages)
   - Logical structure
   - Better reporting
   - Easier maintenance

2. **NetSuite Period Close:**
   - Integrated checklist
   - Step-by-step guidance
   - Automated reminders
   - Goal: Reduce from 10 days

3. **Expensify/RAMP Integration:**
   - Auto-sync to NetSuite
   - Attach receipts automatically
   - Project coding
   - Eliminate manual download/upload
   - "Boom, get actually assigned to it"

4. **Advanced Electronic Bill Payments:**
   - ACH directly from NetSuite
   - Skip bank portal upload
   - Automated process
   - Approval workflow integrated

5. **Bank Feeds:**
   - Auto-import transactions
   - Auto-matching rules
   - Consistent process for bank and credit cards
   - Faster reconciliation

6. **Automated Reversal JEs:**
   - Set reversal flag on entry
   - Automatic reversal next period
   - System tracking
   - No manual tracking needed

7. **SuiteTax:**
   - Use tax handled automatically
   - IL/MO filing simplified
   - Gross receipts tax reports
   - 48-state nexus management
   - No "tricks" needed

8. **Credit Card as Bank Account:**
   - Same reconciliation process
   - Upload statement
   - Auto-matching
   - Integrated workflow

9. **Real-Time Dashboards:**
   - Cache360 for cash flow
   - Project GP KPIs
   - Financial reports on-demand
   - Period-over-period comparisons
   - Export flexibility

10. **Fixed Asset Module:**
    - Potential Bloomberg elimination
    - Integrated tax/book depreciation
    - One system
    - Cost savings

---

## QUOTES & INSIGHTS

**On the Finance Team:**
- "The mighty finance team. Or lean, but my GP. Very good."
- "Kip... he has his hands in everything that we do. He's everywhere."

**On Accounting Periods:**
- "I would like 13. 13. Core only does 12."

**On Period Opening:**
- "I can't tell you how many times we stumbled into January and we couldn't do transactions, because we've got to open up the next accounting period year."

**On Labor Markup:**
- "Product, very predictable, you spend in the PO, you get back in development, it's not gonna change. Labor, you're guessing. Until you get in the field and start doing things."

**On Two GP Metrics:**
- "That's why we have two... that's why we have a different set of KPIs. So, we have a set of KPIs for project gross profit, and then we have commissionable gross profit"

**On Payment Runs:**
- "They always try to kill me with the amounts, because they'd just erode all our cash." (Lorraine on proposed $3M payment runs)

**On Credit Card Fees:**
- "Rewards cards, you get homes with those rewards cards. It's the biggest scam ever. Get the merchant pay for it."

**On Expense Reports:**
- "Who likes to do expense reports? That's why I made Chris buy everything."
- Matt: "I just don't do it. I supposed that my others are cold."

**On Manual Processes:**
- "Obviously a lot of work there up front" (Expensify manual process)
- "It is not a big-time stuff right now, the way we're doing it, so if we had to stick with the way we're doing it, not a big deal, but, you know, one less step, great"

**On Reversal Journal Entries:**
- "We couldn't keep track of them" (why they stopped using reversals in Core)

**On Period Close:**
- "We do everything on... in Excel." (current period close checklist)

**On Fixed Assets:**
- "I just want to know if NetSuite can meet our needs, and do we need that fixed asset stuff? [We're] paying for a third party to do that."

**On Use Tax:**
- "CORE won't do use tax, so we have to kind of trick it."

**On Allocations:**
- "P&Ls that show allocation, they're just on paper."
- "These numbers were never offered heavy."

---

## CHANGE MANAGEMENT CONSIDERATIONS

### Behavior Changes Required

1. **Period Close Process:**
   - From Excel to NetSuite checklist
   - Trust system-guided process
   - Follow step-by-step workflow
   - Communicate status within system

2. **Expense Reports:**
   - If RAMP: New platform entirely
   - Mobile receipt capture
   - Project coding discipline
   - Timely submission

3. **Payment Approval:**
   - New approval workflow in NetSuite
   - Electronic approvals vs. physical review
   - Trust automated ACH process
   - Different remittance communication

4. **Chart of Accounts:**
   - New account structure
   - Different account numbers
   - Memorization adjustment
   - Mapping old to new

5. **Reconciliation:**
   - Automated bank feeds
   - Rule creation for matching
   - Trust auto-matching
   - Exception handling

### Resistance Points

1. **Excel Dependency:**
   - Period close in Excel currently
   - Comfort with Excel workflows
   - May resist system checklist

2. **Approval Process Change:**
   - Current Monday in-person review
   - Shift to electronic approval
   - Less "hands-on" feel
   - Trust in automation

3. **Expense Platform:**
   - If changing from Expensify to RAMP
   - User learning curve
   - New mobile app
   - Change in workflow

4. **Chart of Accounts:**
   - Long-standing account numbers
   - Memorized accounts
   - Reports need updating
   - Significant mapping effort

5. **15% Labor Markup:**
   - If eliminating: Major philosophy change
   - Commission impact
   - Project GP visibility changes
   - Sales team concern

### Success Factors

1. **Lean Finance Team:**
   - Automation will free up time
   - Efficiency gains visible quickly
   - Reduced manual work
   - Appreciated by small team

2. **Lorraine's Prior Experience:**
   - Used Blackline/Flowcast before
   - Understands modern accounting software
   - NetSuite period close similar concept
   - Champions modern approach

3. **Kipp's Involvement:**
   - Finance + IT background
   - Touches everything
   - Can bridge technical and finance
   - Key change agent

4. **Pain Point Awareness:**
   - Team knows current limitations
   - 40+ page COA is problematic
   - Manual processes frustrating
   - Ready for improvement

5. **Integration Opportunities:**
   - Expensify/RAMP integration = major relief
   - Bank feeds = time savings
   - Electronic payments = efficiency
   - Quick wins generate momentum

### Training Focus

1. **Period Close:**
   - NetSuite checklist workflow
   - How to open/close periods
   - Reversal journal entries
   - Best practices

2. **Bank Feeds:**
   - Rule creation
   - Exception handling
   - Matching review
   - Credit card reconciliation

3. **Payment Processing:**
   - Bill payment creation
   - ACH setup
   - Approval workflow
   - Remittance management

4. **Expense Integration:**
   - Expensify or RAMP connection
   - Project coding
   - Receipt attachment
   - Approval routing

5. **Chart of Accounts:**
   - New structure navigation
   - Account mapping reference
   - Report updates
   - Finding accounts quickly

6. **Reporting:**
   - Financial reports
   - Custom searches
   - KPI dashboards
   - Export options

---

## OPEN QUESTIONS FOR FUTURE SESSIONS

1. **Revenue Recognition Details:**
   - Specific recognition rules
   - Timing by order type
   - Project-based recognition
   - White paper review

2. **15% Labor Markup:**
   - Matt/Mark final decision
   - Implementation in NetSuite if continuing
   - Commission calculation impact
   - Communication to sales team

3. **Budgeting Process:**
   - Annual budget workflow
   - Project budgeting beyond Google Docs
   - Budget vs. actual reporting
   - Forecasting approach

4. **Commission Reporting:**
   - Detailed commission structure
   - Reports needed
   - Calculation verification
   - Payment processing

5. **Project Accounting Details:**
   - Project setup workflow
   - Cost allocation
   - Revenue allocation
   - WIP reporting

6. **Payroll Provider:**
   - Final decision on Paylocity vs. new provider
   - HR platform integration
   - Department allocation approach
   - Frequency of imports

7. **Historical Data:**
   - Exact cutoff date
   - Which trial balances
   - Archive process for old data
   - Reference approach for pre-2017

8. **Fixed Asset Module:**
   - Full requirements review
   - Bloomberg comparison
   - Implementation decision
   - Migration of existing assets

9. **Bank Integration Technical:**
   - Coastal registration process
   - Bank feeds technical setup
   - Positive pay workflow confirmation
   - Wire transfer handling

10. **Allocations:**
    - Automate or keep manual?
    - If automate: Rules and logic
    - Reporting requirements
    - P&L by allocation view

---

*End of Master Transcript: Financial Management*


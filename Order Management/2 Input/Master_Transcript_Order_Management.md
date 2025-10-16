# MASTER TRANSCRIPT: ORDER MANAGEMENT
## KBM Hoag NetSuite Orion Implementation

**Sources Combined:**
- 07-30 Meeting_ NetSuite Workflow & Transaction Management.txt (July 30, 2025)
- Relevant portions from Marketing.txt and 07-29 Business Process Review

**Date Range:** July 2025
**Business Process:** Order Management (Quote through Sales Order, Transaction Management, Approvals, Tax, Billing)

---

## EXECUTIVE SUMMARY

Order Management at KBM Hoag encompasses the entire transaction lifecycle from quote/proposal creation through sales order booking, purchase order generation, and invoicing. The current Core system treats proposals and sales orders as a single transaction with status changes, while NetSuite/Orion uses separate, linked transactions. Key challenges include Miller Knoll tiered pricing complexities, tax management for government/direct bill orders, customer PO tracking, approval workflows, and managing split orders for installation strategies. The team emphasizes they operate in a "collapsed" world where all work is done upfront before creating a static proposal.

**Key Themes:**
- Transaction separation (Opportunity → Proposal → Sales Order → PO)
- Upfront specification and budgeting (live Google Docs → static proposal)
- Tiered pricing challenges with Miller Knoll
- Government order tax complexity (warehouse vs. final destination)
- Customer PO value tracking need
- Template ownership and customization control
- Approval workflow automation

---

## TRANSACTION STRUCTURE: CORE VS. NETSUITE

### Current State (Core)

**Single Transaction Model:**
- Proposal and Sales Order are the same record
- Status changes from "Proposal" to "Sales Order" (booked)
- No separate quote phase
- ROM (Rough Order of Magnitude) done before proposal
- Order number assigned at proposal creation
- No CRM module used in Core

**Current Workflow:**
1. Opportunity identified (tracked in Zendesk if entered)
2. ROM/rough budgeting (Google Docs - live document)
3. Specification work completed
4. Budget finalized
5. Create Proposal in Core (static from this point)
6. Client approval
7. Change status to Sales Order (booked)
8. Generate Purchase Orders

### Future State (NetSuite/Orion)

**Separate Transaction Model:**
- **Opportunity** (CRM record for pipeline tracking)
- **Proposal/Quote** (pricing, terms, client approval)
- **Sales Order** (booked order, ready for fulfillment)
- **Purchase Order** (vendor orders)
- **Invoice** (billing)

**Each Transaction:**
- Unique transaction number with prefix
  - OP-#### (Opportunity)
  - PR-#### or PROP-#### (Proposal)
  - SO-#### (Sales Order)
  - PO-#### (Purchase Order)  
  - INV-#### (Invoice)
- Linked together via Project Number/Name
- Project Number and Name consistent across all transactions
- One-click conversion between transaction types
- Automatic data transfer

**Benefits of Separation:**
- Compare proposal to sales order (change tracking)
- Better audit trail
- Multiple quotes from single opportunity
- Different fields/data at different stages
- Revenue recognition separation

**Challenge:**
- "This is like the one thing during discovery that people get tripped up on"
- Different numbers for each transaction (vs. memorizing one order number)
- Adjustment period: "Kleenex may be required, but we should be able to wipe our tears pretty quickly"

**Mitigation:**
- Project number stays consistent
- Global search works (project, customer name, phone number)
- Recent transactions dialog (last 10-15 items)
- Hyperlinks between all related records
- "Always one click away from the project record"
- First view shows all associated transactions

---

## TRANSACTION NUMBERING & NAMING CONVENTIONS

### Confusion During Discovery

**Team Feedback:**
- "There's still a lot of confusion around is it a quote, is it a proposal, is it a sales order?"
- Multiple numbers for one project feels overwhelming
- Current practice: Email subject lines reference specific order number
- Need to shift to project-based referencing

### Decided Naming Convention

**Transaction Prefixes:**
- **OP-####** = Opportunity
- **PR-#### or PROP-####** = Proposal (team decided to add "P" for clarity)
- **SO-####** = Sales Order
- **DPO-####** = Draft Purchase Order
- **VPO-#### or PO-####** = Vendor Purchase Order
- **INV-####** = Invoice

**Project Number:**
- Consistent across ALL transactions
- Appears on every record
- Primary search/reference key
- To be determined: Specific format/prefix

**Sequence Configuration:**
- Each transaction type can have different number lengths (5-digit, 6-digit, etc.)
- Starting numbers to be determined (typically 1001+)
- No prefix required (but recommended for clarity)

### Search & Navigation

**Global Search Capabilities:**
- Project number/name
- Customer name
- Phone number
- Transaction numbers
- Many other fields

**Quote from Team:**
"Information is going to be presented to us differently than it is in Core and be easier to read and find and understand. We rely a lot on that information right now because Core is impossible to find something without that data."

---

## CUSTOMER MANAGEMENT

### Tax Management

**Tax Automation - SuiteTax:**
- KBM Hoag registered in 48 states (nexus)
- Automatic tax calculation based on ship-to address
- Tax exemption certificate management:
  - Upload certificates with effective dates
  - Dashboard shows expiring certificates
  - Automatic application on future quotes for that customer
  - No manual selection needed
- Tax compliance reporting
- "You get a beautiful report"

**Government Orders - Tax Complexity:**

**The Challenge:**
- Miller Knoll direct bill orders: Client pays Miller Knoll directly for product
- KBM Hoag issues proposal but doesn't collect payment on product
- Miller Knoll insists on taxing to warehouse (where shipped), not final destination
- "Miller Knoll insists, because you know they're the experts on selling to clients, not the hundreds of dealers that do this every day"
- Standard tax practice: Tax to final destination
- "Every tax person we've ever talked to in the entire 80 years of our existence in business, we have taxed to final destination"

**Current Core Workaround:**
- Change ship-to address in Core to warehouse
- Get tax calculation
- Get tax number
- Change address back
- Do tax override
- "It's a pain in the butt"

**NetSuite Solution:**
- Tax override capability available
- "Not elegant" but workable
- Manual process still required
- Warehouse tax percentage always higher than final destination
- Government frustrated with KBM Hoag but "we have no control over anything"

**Direct Bill Volume:**
- ~$1M annually
- 1% of $100M total revenue
- Gross up for commission (full sales amount to Miller Knoll, commission kicked back)

### Finance Charges

**Current Approach:**
- Global on/off switch
- Deterrent/threat mechanism
- **Never actually implemented in 13 years** (Lorraine)
- Shows on statements and invoices as warning
- Automatic calculation if enabled

**Quote:**
"Most dealers want to threaten. They don't actually follow through, which I get it because you want to keep your customers happy, too."

**Functionality:**
- 90-day old invoice would automatically add finance charge line
- Can be manually added as line item if needed
- Typically not used

### Storage Fees

**Variability by Warehouse:**
- Some warehouses: 90-day free storage
- Some: 60 days
- Some: 30 days

**Current Process:**
- Bill back to client (most cases)
- Add lines to existing sales order:
  - Cost line
  - Sale line (marked up)
- Sometimes absorbed as customer accommodation
- Situational decision based on cause (construction delay not client's fault vs. client-caused delay)

**Alternative Approach:**
- Create separate, related sales order for storage fees
- Part of same project
- Cleaner than adding to original order
- Team uses both methods currently

**Impact on Commission:**
- Storage fee lines can be marked as non-commissionable at line level
- Decision: "Always" commissionable per team

### Project GP vs. Commissionable GP

**Two GP Concepts:**

1. **Project GP:**
   - Overall gross profit for the project
   - What everyone primarily monitors
   - Includes all revenue and costs

2. **Commissionable GP:**
   - Basis for commission calculation
   - Individual lines marked commissionable or not
   - Header level: Who gets commission, percentage/split
   - Line level: Is this line commissionable?
   - Used only for calculating commission

**Example Non-Commissionable Lines:**
- Storage fees (sometimes)
- Customer accommodations
- Reimbursable expenses
- Other situational items

**Outside of Commission Calculation:**
"Everyone just primarily looking at the project GP like the actual GP"

### Customer PO Tracking

**Current Challenge:**
- Blanket POs received frequently
- No way to track PO value vs. amount billed
- Don't know when approaching PO limit
- Risk of exceeding PO
- Then client says "we can't pay this" → payment delays

**Bank Requirement:**
- Bank asking for: Total project value, POs against project, open balance
- Never been able to provide this data
- "That's something we just talked about that our bank has asked us"

**Proposed Solution:**
- Custom record/transaction for PO tracking
- Attach customer PO document
- Track PO value
- Aggregate at project level
- KPI dashboard showing:
  - Total PO value
  - Amount billed to date
  - Remaining balance
  - Alert when approaching limit

**Complexity:**

*Multiple POs Scenario:*
- If multiple orders on project, might get different PO for each order
- Or client adds money to existing PO (easier than getting new PO approval)
- Need to track which PO applies to which order

*Change Orders:*
- Do they issue new PO for change orders? "Depends on the client"
- If change orders aren't on a PO, math doesn't work
- Potential rule: Change orders excluded from calculation

**Manual Management Required:**
- "Won't just happen on its own"
- Someone needs to enter PO numbers and values
- Update as changes occur
- Decision: Team willing to manage this

**Design Approach:**
- Custom transaction created
- Pull in customer PO information
- Attach PO document to record
- Link to project
- Aggregate data at project level
- "Simple elegant solution"
- "Low-hanging fruit from a customization standpoint"

**Competitive Advantage:**
- "We're in a pretty dealer-heavy market"
- "Four other Miller & Noll Dealers in our markets"
- "Anything that we can do to make us look like we're easy to do business with"

**Proprietary vs. Shared:**
- Matt: Open to sharing with dealers outside market
- Solution will be KBM Hoag-specific customization
- Won't go into standard Orion
- If other dealers want it, GSI will solve differently

**Action Item:** Separate working session to design PO tracking solution

---

## QUOTE/PROPOSAL MANAGEMENT

### Quote Creation Process

**Typical Flow (NetSuite Standard):**
1. Create from opportunity (one-click conversion)
2. Or bypass opportunity and create quote directly
3. Add line items
4. Pricing
5. Terms
6. Client approval
7. Convert to sales order

**KBM Hoag Approach:**
- No separate "quote phase" in current process
- ROM (Rough Order of Magnitude) before proposal
- All work done upfront in Google Docs (live budget)
- Proposal created only when ready to be static
- "Quote phase for us is basically we did a ROM before we ever got to a proposal"

**In NetSuite:**
- Will have opportunity record
- Will have proposal/quote record
- Will have sales order record
- Still working "collapsed" but in separate transactions

### Proposal = Sales Order (Current Mindset)

**Current Core:**
"Proposal and sales order mean the same thing to us"

**Why:**
- Core: Same transaction, status changes
- Don't use quote tool in Core (no Core CRM)
- No quote phase - go straight to proposal

**Quote from Team:**
"Sales order is the number that gets issued when you quote"

### Upfront Work Philosophy

**Team Approach:**
"We really live in a world of collapsed. So part of us using Google Docs, it's like we have a shared budget that we're working through. And so we have to expect that budget to be met. Like, everything is live. So by the time we get to quote, it's dead at that point. Where it's static."

**Implications:**
- All specification complete before proposal
- Budget finalized
- Spec check done
- Everything ready before creating proposal
- No changes expected after proposal created
- "We don't put anything in the system until we're ready to be static"

**Sales Order in NetSuite:**
- "Sales order means donezo. Ready for sales."
- By the time it's a sales order: all upfront work already done
- Spec check complete
- No additional approval needed at SO stage (already approved at proposal)

### Quote/Proposal Features

**Smart Table Functionality:**
- 60 columns displayed
- SIF import data
- Quick views
- Custom groups for PO planning
- Drag and drop organization

**Grouping Capabilities:**
- Ship-to location
- Ship date
- Floor/area (installation strategy)
- Vendor
- Product type (standard vs. specials/customs)
- WHIPs (Work Hold In Progress - expedited items)

**PO Planning from Quote:**
- Group items by how POs should be split
- Installation strategy drives grouping
- "This was a conversation at a project level where our PO ordering strategies for a big project would be part of our install strategy so maybe it's by floor or by area"

**Examples of Splits:**
- One order by floor
- One order by hall chairs
- Or single order but POs split different ways
- Miller Knoll: Separate standard from specials/customs (avoid delay)

### Pipeline Forecasting

**Recommendation:**
- Forecast from **Opportunity** level (not quote/proposal level)
- Prevents over-forecasting with multiple quotes

**Why:**
- One opportunity might have multiple quotes
- If forecasting from quotes, all quotes would add to pipeline
- Result: Over-forecasting

**Challenge:**
- Three quotes with different amounts
- Opportunity doesn't know which amount to use
- Manual management needed if want accuracy

**Manual Sync:**
- Update opportunity amount when quote amount changes
- "Someone's gonna have to manage which quote should go back to the opportunity and update the amount if you want to get that accuracy"
- "Just depends on how accurate it needs to be"

---

## BILL OF MATERIALS (BOM) & IMPORT

### SIF Import Tool

**Orion Capability:**
- Import SIF files to quote/proposal
- 60 columns of data imported
- Smart table display with quick views
- Custom grouping
- Drag and drop

**Core Comparison:**
- Core has popup asking to concatenate SIF fields
- Core limits: "SIF file has more fields than core will accept"
- Core combines/concatenates fields
- NetSuite: All SIF columns map to their own fields
- "No having to tell it what to do"

**Tag Handling:**
- Tags (floor, room, chair tag, etc.) each get their own field
- No confusion about tag1, tag2, tag3, tag4
- No automatic combining
- Cleaner data structure

### XML Import

**Need Identified:**
- Sometimes build spec in Excel, export as XML, upload
- "Very rare, but we have used that feature"
- Vendors send XMLs as quotes (Jack sends XML for accessories)

**Solution:**
- Orion supports XML import
- Convert any format to JSON
- Need example template from Matt
- Build conversion schema
- Matt to provide Excel template

**Action Item:** Matt to provide XML import template example

### Vendor Quote Tool Integration

**Miller Knoll Quote Tool:**
- Engaged at proposal level
- Price validation
- Vendor response utility
- Accept pricing or create issue
- Same tool as for POs

### Option Code Changes

**Smart Table Feature:**
- Can change option codes in popup window
- Shows: Part number, option code, option description
- **No validation** - must be careful
- Risk of entering invalid options
- Users need to be cautious

### Spec Creation Limitation

**Current Core Capability:**
- Catalogs loaded in Core (CAP catalogs on CDs monthly)
- Can search part number
- Pick options
- Build spec directly in Core
- "All the catalogs are there, so I can go search a part number and then I can pick all the options"

**NetSuite/Orion:**
- "Not there yet"
- Cannot build specs directly in NetSuite currently
- Must use external tools:
  - Project Spec (preferred by some)
  - CET (Configura)
  - CAP Worksheets
  - Vendor tools

**Integration Plans:**
- Talked to Configura about integration
- "Said it would be easier to integrate with CET than Project Spec"
- Not in current scope

**Impact:**
- "Old timers use Core to write our specs"
- Will need to use Project Spec or other tools
- Some resistance: "I refuse to learn project spec"
- "CAP is better"

**Workaround for One-Offs:**
- Can manually enter (tedious for long model numbers)
- Can copy/paste from quote
- Cannot search catalogs
- Primarily affects: Small orders, showroom orders, employee friends/family orders
- "Basically what happens is everybody's buddy that wants something for their home usually comes to me"
- "It's faster for me to just write a proposal than send an email and ask for it"

### SIF Validation

**Core Behavior:**
- Doesn't validate SIF files
- "CORE doesn't look at it, right? It just says, ah, here's a CIF"
- Can fix option order manually (paint before finish vs. finish before paint)

**NetSuite/Orion:**
- Also doesn't validate
- Can manually edit
- No validation against catalogs
- "You just, it doesn't validate"

**Benefit of No Validation:**
- Flexibility to fix errors
- Can adjust as needed
- Manual quality control

---

## TIERED PRICING CHALLENGES

### The Problem

**Miller Knoll (and other manufacturers) Tiered Pricing:**
- Contract discount rates based on volume tiers
- Example:
  - $0 - $1M list: Discount X%
  - $1M - $2.5M list: Discount Y% (deeper)
  - Etc.
- Automated system calculates discount based on PO value
- System rejects or adjusts if wrong discount used

**Project Strategy:**
- Large projects broken into multiple orders for installation strategy (by floor, by area, etc.)
- Or broken by client request (different cost centers)
- Each order becomes separate sales order
- Each SO becomes separate PO

**The Issue:**
- Manufacturer pricing looks at **PO level**, not project level
- Multiple POs from same project don't aggregate for tier calculation
- Each PO priced separately at lower tier
- Lose deeper discount despite qualifying based on project total
- "If we put in the wrong discount, their system auto-calculates it and adjusts the discount up or down"

**Attempts to Fix:**
- "Nightmare to get them to put these different POs together and give us a deeper discount"
- Even providing same contract number doesn't help
- System "just rejects it"
- Not smart enough to look at project number

### Consequences of Current Approach

**If Keep on One PO (to get discount):**
- Lose ability to split for installation strategy
- GP tracking issues: "Sell out here on a different sales order and cost on this sales order. If you're looking at just sales order, your GPs are all screwed up"
- Booking timing issues:
  - Friday: Book all costs (tanks that month's P&L)
  - Monday: Book sales (next month)
  - Or reverse: "Book all the sales, then forget to book the tier"

**If Split POs (installation strategy):**
- Correct installation approach
- Clean GP by order
- Proper cost/revenue matching
- But lose tiered discount
- Higher product cost

### Proposed Solution

**Escalation to Dustin (Miller Knoll):**
- "We're gonna talk to Dustin about this"
- Request: Accept project number + contract number
- Project numbers unique to each project
- Should recognize all POs from same project for tier calculation
- "If they know that your project numbers are unique to that project, then they should just accept that project number along with the contract number"

**Scope:**
- Not just Miller Knoll: "Other manufacturers and dealers that have the same challenge"
- Industry-wide issue
- Orion solution could benefit multiple dealers

**Action Item:** Follow up with Dustin (Miller Knoll product owner) on tiered pricing for projects

---

## APPROVAL WORKFLOWS & RULES

### Business Rule Engine (NetSuite/Orion)

**Capabilities:**
- Write business rules with criteria
- Apply to quotes/sales orders
- Automatic routing to approvers
- Approvers see on dashboard
- Approve/reject/exception handling
- Timestamp and audit trail
- Report on approval times (average, individual)

**Example Rules:**
- Customer PO number missing → route to specific person
- Gross margin < 16% → route to CFO
- [KBM Hoag specific rules documented below]

**Sophistication:**
- "As sophisticated or as simple as you want"
- Can have multiple complex rules
- Can override/make exceptions (documented with timestamp)

**Caution:**
- More checks = slower process
- "Unintended consequence: People are slow on approving"
- Must manage approvers
- Need to monitor approval times
- Balance control with speed

### KBM Hoag Current Approval Rules

**Rule 1: Orders Over $25,000**
- Goes to Shannon (Project Coordinator Manager) for approval
- Shannon verifies completeness

**Rule 2: Missing Requirements**
- Must have ALL of:
  - Deposit
  - Signed proposal
  - Signed drawings
  - Signed lookbook
- If ANY missing → goes to Matt for approval
- "They do all day unabashedly, could care less"
- Matt: "So good and quick about responding"
- Mark is backup for Matt

**Rule 3: Erosion > $1,500 Cumulative**
- Example: $500 erosion + $1,000 more = $1,500 triggers
- Email approval from Matt required
- "Sounds like a lot, but it's not that much"

**Purpose of Erosion Review:**
- Training insight: "New person who's the reason for the erosion, like they made a mistake"
- Problem-solving with experience
- Finding cheaper solutions

**Matt's Erosion Story:**
- Clay (dramatic employee) runs in: "We need to rent a crane!"
- Table doesn't fit in elevator or stairs
- Crane cost: $6K-$10K plus permit plus traffic control
- Matt's solution: Float table on top of elevator with technician on-site
- Cost: $1,200
- Lesson: Experience finds cheaper solutions
- "If we're going to spend the money, let's spend it this way"

**Process Notes:**
- "Usually make the PCs do it" (submit erosion approval requests)
- Matt very accessible and responsive
- Not about punishment - about training and problem-solving

### Double Order Prevention

**Biggest Losses:**
- "The two that have hurt us the hardest are both the double orders"
- Someone places same order twice unknowingly
- Example: 150 workstations ordered and owned
- Not discovered until shipment notice received

**Current Prevention:**
- Shannon's approval supposed to catch double orders

**Challenge with Automation:**
- Legitimately order similar items across projects
- Sometimes order in bulk ("ordering by four, so technically it's a double order")
- Don't want constant "Are you sure?" prompts
- Users will click yes without thinking

**Potential Detection:**
- Query: Same total dollar amount within past 30 days
- Flag for manual review
- "Not a hard query"
- Not automatic rejection - just alert

### Vendor Credit Limits

**Need Identified:**
- Track KBM Hoag credit limits with vendors
- Currently hit limits unexpectedly
- "Mad scramble at that nth hour because our order won't go through because we hit it"

**Solution:**
- Vendor record: Credit limit field
- Warning threshold (e.g., 90% of limit)
- Prevent PO creation if over limit
- Dashboard visibility

**Implementation:**
- "Sounds more like just a pretty simple query"
- On vendor record
- Percentage-based threshold

### Approval Rules Configuration

**For BRD:**
- Budget for up to 10 approval rules
- Should cover quotes and sales orders
- Includes current KBM Hoag rules
- Room for additional rules as needed

**Action Item:** Shannon to document current approval flowchart

---

## ORDER TYPES & SPECIAL BILLING

### Order Types (Current)

**Identified Types:**
1. **Direct Bill** (~$1M/year, 1% of revenue)
   - Client pays Miller Knoll directly
   - Gross up for commission
   - Give full sales amount to Miller Knoll
   - Get commission kickback
   - Tracked separately for reporting
   - Hits financials as normal income/COGS (no DB items needed)

2. **Intermarket**
   - **Inbound:** ~40/year ("39 more than we're used to")
   - **Outbound:** Hundreds (possibly thousands)
   - Shannon handles for all Intuit work-from-home
   - "Literally" thousands of transactions
   - 8-10/day average per Shannon
   - 100+/month
   - 20-30/week minimum
   - All through ServiceTime
   - Pain point: Setting up dealer as vendor AND customer

3. **Intuit Work from Home** (subset of intermarket)
   - Massive volume (Shannon's primary work)
   - Want separate order type for reporting
   - Currently "e-commerce" in Core (Shopify legacy)
   - Rename to "Intuit Work from Home"

4. **Government Orders** (20% of business)
   - Special tax handling
   - Direct bill sometimes

**Purpose of Order Types in Orion:**
- Primarily informational for reporting
- Can drive business process/automation
- Default order functionality (auto-import lines)

**Action Item:** Provide complete list of order types with descriptions

### Default Orders

**Functionality:**
- Order type can trigger automatic line imports
- Example: Choose "Order with Dealer Services"
- System automatically adds service lines
- Called "default order" in Orion
- Can "clone transactions" with formula lines

**Current Use:**
- Already using concept in Core
- Will continue in NetSuite

### Alternative Billing

**Third-Party Billing:**
- Direct business (covered above)
- Intermarket (covered above)

**Government:**
- 20% of business
- Some direct bill to Miller Knoll
- Tax complexity (warehouse vs. final destination)

**No Unique Processing Beyond Order Type:**
- Intermarket: Nothing special beyond vendor/customer setup
- Direct bill: Gross up handled, but auditor-approved approach

---

## DOCUMENT TEMPLATES

### Current Challenge

**Core Template Management:**
- Any change requires Core billable hours
- Example: "Change verbiage on the footer of our invoice"
- Have to contact Core support
- Wait for changes
- Pay per change
- "That's insane"

**Kipp's Redesign:**
- Redesigned all templates 5 years ago
- "No one has said anything to me about anything on this proposal"
- Happy with current designs
- "Are you saying there's a problem?" (Kipp to team)
- Got rid of "core beige envelope"

### NetSuite Solution

**Template Ownership:**
- "You can do it yourself"
- "Are these templates things that we can own and manage ourselves? Yes, sir."
- No vendor billable hours for changes
- Self-service modifications

**Kipp's Requirements:**
- Communication record of changes
- Document why changing
- Version history
- Lock down process (controlled changes)

**Types of Templates Needed:**

*Customer-Facing:*
- Proposals
- Invoices
- Order confirmations
- Quotes
- Other client documents

*Vendor-Facing (New Focus):*
- Purchase orders
- "We never touch vendor facing"
- "I would like to reevaluate the design of vendor facing"
- Opportunity to improve during implementation

**Action Item:** Kipp to provide ALL templates (customer and vendor-facing)

**Template Format:**
- Little table in top right corner (invoices)
- Multiple data points
- Can add proposal/quote number to invoice
- Reference original order number
- Customer PO number
- All cross-referenced

---

## CUSTOMER PO HANDLING

### Client PO Numbers on Transactions

**Current Process:**
- Client issues PO
- Mark their order number on PO (for back-reference)
- KBM Hoag enters customer PO number on proposal
- Customer PO number appears on invoice

**NetSuite Process:**
- Enter customer PO on proposal/quote record
- Automatically flows to sales order
- Shows on invoice
- "Their customer PO number show up anywhere you want"

**Invoice Cross-Reference:**
- Invoice number
- Customer PO number
- Original proposal/quote number (can add to template)
- All for client's AP matching

**Client Matching Process:**
- Client references invoice to their PO
- Also references back to original order number
- Now order number changing (transaction numbers different)
- Solution: Add quote/proposal number to invoice template
- Still have all needed reference numbers

---

## COMMISSION MANAGEMENT

### Commission Structure

**Header Level:**
- Who gets commission (sales person)
- Percentage (100% or split)
- Can split commission between multiple people

**Line Level:**
- Mark individual lines as commissionable or not
- Example: Storage fees might not be commissionable
- Customer accommodation lines not commissionable
- Flexibility to exclude specific line items

**GP Impact:**
- Project GP: Total gross profit
- Commissionable GP: Subset used for commission calculation
- Sales team looks at commissionable GP
- Management looks at project GP
- "Outside of calculating the commission, then yes, we're looking at Project GP"

### Storage Fees and Commission

**Decision:**
- Storage fees **always** commissionable
- Even though sometimes absorbed as customer accommodation
- Consistent approach

**15% Labor Markup:**
- External labor marked up 15%
- Affects project GP
- Formula-based calculation

---

## SALES ORDER MANAGEMENT

### Creating Sales Order

**From Proposal:**
- One-click conversion
- Click "Sales Order" button on proposal
- Generates new SO record
- All information transfers automatically
- No re-keying

**Different Fields:**
- Proposal form ≠ Sales Order form
- SO form has different/additional fields
- Opportunity to gather more information
- "Moved one more step in the process, now we need to get more information in order to take the next step"
- Typically ask for more dates at SO stage

**KBM Hoag Approach:**
- Don't need additional SO approval
- Already done everything upfront
- "By the time it gets there, we've already done all the other stuff, like the spec check"
- "Sales order means donezo. Ready for sales."

### No Additional SO Approval

**Why Not Needed:**
- Doing more upfront to get proposal right
- Spec check complete before proposal
- All validation done
- Proposal approval sufficient
- "We don't issue a quote until we're [ready]"

**NetSuite Capability:**
- Could add SO approval workflow if wanted
- After proposal approved, before SO booked
- Before generating POs
- KBM Hoag doesn't need this

### Live Budget → Static Proposal

**Philosophy:**
"We really live in a world of collapsed. So part of us using Google Docs, it's like we have a shared budget that we're working through. And so we have to expect that budget to be met. Like, everything is live. So by the time we get to quote, it's dead at that point. Where it's static. It's not moving any longer. But everything up to that is static. So we don't put anything in there. We don't put anything in the system until we're ready to be static."

**Implications:**
- Google Docs: Live collaborative budgeting
- Multiple stakeholders updating
- Real-time changes
- Dynamic until finalized
- **Then**: Create proposal (static snapshot)
- No changes after proposal created
- High confidence in accuracy

---

## PURCHASE ORDER GENERATION

### Draft PO Concept

**Session Ended Before Discussion:**
- "Here's some big ideas I'm going to introduce. The first one is the concept of the draft PO"
- "Inside NetSuite and actually inside most enterprise..."
- Session break for lunch

**Kipp's Comment:**
- "Our current POs are a shitstorm of information"
- "I'd like them to be more organized in their format"
- "Deal. We'll make it happen"

**Implication:**
- Current PO format needs improvement
- Better organization desired
- More structured presentation
- Topic to be covered in separate session

---

## CLONING & FORMULA FEATURES

### Transaction Cloning

**Capability:**
- Clone entire transactions
- Useful for similar orders
- Repeat orders
- Standard configurations

### Formula Lines

**Capability:**
- Lines with formulas
- Automatic calculations
- Examples:
  - Labor markup (15%)
  - Percentage-based fees
  - Quantity-based calculations
  - Storage fee calculations

**Current Use:**
- Already using in Core
- Will continue in NetSuite

---

## QUOTE PDF GENERATION & CUSTOMIZATION

**Client Quote Approval:**
- Not using automated client approval workflow
- Traditional send PDF for signature approach

**PDF Generation:**
- Custom templates (Kipp's designs)
- "We're going to give you templates, you're going to get yours, so we can recreate them"
- Ability to modify without vendor involvement

---

## SPECIAL CASES & EDGE CASES

### Government Orders

**Volume:**
- 20% of business
- Significant portion of revenue

**Special Handling:**
- Tax to warehouse (Miller Knoll direct bill)
- Tax override capability needed
- Client pays Miller Knoll directly (sometimes)
- Still issue proposal from KBM Hoag

### Miller Knoll Direct Bill

**Annual Volume:**
- ~$1M (1% of $100M revenue)

**Process:**
- Gross up sales amount
- Full amount to Miller Knoll
- Commission kicked back to KBM Hoag
- Auditor-approved process

**Tax Issues:**
- See Government Orders tax complexity above

### Intermarket Outbound (Intuit)

**Massive Volume:**
- Shannon's primary work
- Thousands of transactions
- Work-from-home program
- All through ServiceTime integration

**Pain Point:**
- Setting up other dealers (first time)
- Must be both vendor AND customer
- "Biggest pain they ask is setting up that dealer if we haven't done it with them before"

### One-Off Orders

**Personal Orders:**
- "Everybody's buddy that wants something for their home usually comes to me"
- Faster to write proposal than request through proper channels
- Small orders for showrooms
- Employee friends/family

**Impact of No Catalog:**
- Currently fast in Core (search catalog, pick options)
- Will be slower in NetSuite (manual entry or copy/paste from quote)
- "But that's a me problem" (Kipp)

---

## INTEGRATIONS RELEVANT TO ORDER MANAGEMENT

### Miller Knoll ServiceNet

**Plan:**
- Link ServiceNet to Orion
- Mentioned but not detailed
- "Did you talk about Miller linking ServiceNet into Orion at some point? Yes. Yep. Absolutely."

### Coupa Integration (Potential)

**Current Process:**
- Shannon gets Coupa email notifications
- Order information in email
- Has to log into Coupa to process
- Information in PDF

**Potential Automation:**
- "As long as the emails have order information that's pretty consistent, it's pretty easy to do"
- Email parsing to create orders
- Automated processing
- Bi-directional: Invoice back to Coupa portal
- Currently manual process

**Email Portals:**
- Discussion deferred: "That's what I was going to talk about later today as well, our e-portals"

---

## REQUIREMENTS SUMMARY

### Functional Requirements

1. **Transaction Management:**
   - Opportunity → Proposal → Sales Order workflow
   - One-click conversions
   - Automatic data transfer
   - Transaction linking via project number
   - Audit trail between versions

2. **Approval Workflows:**
   - 10+ approval rules
   - Shannon's $25K threshold
   - Matt's missing requirements rule
   - Erosion approval ($1,500 cumulative)
   - Timestamp and audit trail
   - Approval time tracking
   - Double order detection query

3. **Tax Management:**
   - SuiteTax for 48 states
   - Tax exemption certificate tracking
   - Expiration dashboard
   - Tax override capability (government orders)

4. **Customer PO Tracking:**
   - Custom transaction/record
   - Document attachment
   - Value tracking
   - Project-level aggregation
   - Remaining balance calculation
   - Alert thresholds

5. **BOM/Import:**
   - SIF import (60 columns)
   - XML import (with conversion)
   - Smart table with grouping
   - Quick views
   - Vendor quote integration

6. **Commission:**
   - Header-level assignment
   - Line-level commissionable flag
   - Project GP vs. Commissionable GP
   - Split commission support

7. **Template Management:**
   - Custom PDF templates
   - User-manageable (no vendor billable hours)
   - Customer-facing templates
   - Vendor-facing templates
   - Version control

### Technical Requirements

1. **Customizations:**
   - Customer PO tracking (custom record/transaction)
   - Approval rule configuration (10 rules)
   - Double order detection query
   - Vendor credit limit warnings
   - SIF import mapping
   - XML import conversion

2. **Integrations:**
   - Miller Knoll ServiceNet
   - Coupa (potential email parsing)
   - ServiceTime (intermarket)
   - Google Drive (document linking)

3. **Reports:**
   - Order type reporting
   - Approval time analysis
   - Project GP vs. Commissionable GP
   - Customer PO utilization
   - Intermarket volume
   - Government order tracking
   - Direct bill reporting

4. **Data Migration:**
   - Historical orders
   - Customer POs
   - Project associations
   - Commission data

---

## DECISIONS & ACTION ITEMS

### Decisions Made

1. **Transaction Naming:**
   - OP/PROP/SO/PO/INV prefixes decided
   - Project number primary reference

2. **No SO Approval:**
   - Proposal approval sufficient
   - Upfront work makes SO approval redundant

3. **Customer PO Tracking:**
   - Will implement custom solution
   - Separate working session needed
   - Team willing to manually manage

4. **Storage Fees:**
   - Always commissionable
   - Bill back to client (most cases)
   - Add lines to SO or create separate SO

5. **Finance Charges:**
   - Not implementing (never used in 13 years)

6. **Template Ownership:**
   - All templates to be recreated in NetSuite
   - Self-service management
   - Version control process

### Action Items

1. **Shannon:** Document approval workflow flowchart
2. **Kipp:** Provide all templates (customer and vendor-facing)
3. **Matt:** Provide XML import template example
4. **Team:** Provide complete order type list
5. **Marcus/Team:** Schedule PO tracking design session
6. **Marcus:** Follow up with Dustin on tiered pricing solution
7. **All:** Review transaction numbering and confirm comfortable

---

## PAIN POINTS TO SOLVE

### Current Frustrations

1. **Different Transaction Numbers:**
   - Memorized order numbers won't work
   - Need to shift to project-based thinking
   - Email subject lines currently use order number
   - "Kleenex may be required"

2. **Miller Knoll Tiered Pricing:**
   - Lost discounts on split orders
   - Installation strategy conflicts with pricing
   - GP tracking issues if keep on one PO
   - Timing issues (booking in different months)
   - Manufacturer won't recognize project number

3. **Government Order Taxes:**
   - Warehouse vs. final destination
   - Miller Knoll policy conflicts with tax law
   - Manual override workaround
   - "Not elegant"
   - Client frustration

4. **Customer PO Tracking:**
   - No visibility to PO exhaustion
   - Risk of exceeding and delaying payment
   - Bank reporting requirement unmet

5. **Template Management:**
   - Can't make simple changes
   - Vendor billable hours for every change
   - Slow turnaround
   - No ownership

6. **Double Orders:**
   - Biggest financial losses
   - Current manual prevention (Shannon)
   - Need better detection

7. **Vendor Credit Limits:**
   - Unexpected hits to credit limits
   - "Nth hour mad scramble"
   - Order rejections

8. **Intermarket Setup:**
   - Setting up dealers as vendor AND customer
   - Time-consuming for first-time dealers
   - Pain point for high-volume work

### Future State Solutions

1. **Project Number Consistency:**
   - Search by project instead of order
   - Global search capabilities
   - Recent transactions
   - Hyperlinked records
   - "One click away from project record"

2. **Tiered Pricing (Proposed):**
   - Dustin/Miller Knoll to accept project number + contract
   - Industry-wide benefit
   - Installation strategy preserved
   - Correct discount received

3. **Tax Override:**
   - Available in NetSuite
   - Still manual but functional
   - Document process

4. **Customer PO Tracking:**
   - Custom solution designed
   - Visibility dashboard
   - Alert thresholds
   - Bank reporting capability

5. **Template Ownership:**
   - Self-service modifications
   - No vendor involvement
   - Version control
   - Fast changes

6. **Double Order Detection:**
   - Query: Same $ amount in last 30 days
   - Flag for review
   - Not automatic block

7. **Vendor Credit Limits:**
   - Field on vendor record
   - Threshold warnings
   - Prevent PO creation if over

8. **Intermarket:**
   - Streamlined setup (if possible)
   - ServiceTime integration maintained

---

## QUOTES & INSIGHTS

**On Transaction Numbers:**
- "This is like the one thing during discovery that people get tripped up on. And then it's like also the one thing that when you get into actual using the system, it's like, oh, that wasn't a big deal."
- "Kleenex may be required, but we should be able to wipe our tears pretty quickly"
- "Information is going to be presented to us differently than it is in Core and be easier to read and find and understand"

**On Working Collapsed:**
- "We really live in a world of collapsed... everything is live... by the time we get to quote, it's dead at that point. Where it's static."
- "Sales order means donezo. Ready for sales."

**On Matt's Erosion Review:**
- Story of Clay and the crane: $10K crane vs. $1.2K elevator technician solution
- "If we're going to spend the money, let's spend it this way"
- "He's so good and quick about responding"

**On Tiered Pricing:**
- "Miller Knoll insists, because you know they're the experts on selling to clients, not the hundreds of dealers that do this every day"
- "Every tax person we've ever talked to in the entire 80 years of our existence in business, we have taxed to final destination"
- "It is a nightmare to get them to put these different POs together and give us a deeper discount"

**On Templates:**
- "I have to go to Core and they have billable hours for that. That's insane."
- "Are you saying there's a problem?" (Kipp's pride in 5-year-old designs)

**On Intermarket Volume:**
- Shannon: "I'm probably doing 100 a month, if not more"
- "It's at least 20 or 30 a week. At least."
- "I average probably about 8 to 10 a day"

**On PO Tracking:**
- "We're in a pretty dealer-heavy market"
- "Anything that we can do to make us look like we're easy to do business with"

**On Current POs:**
- Kipp: "Our current POs are a shitstorm of information"

---

## CHANGE MANAGEMENT CONSIDERATIONS

### Behavior Changes Required

1. **Reference by Project Not Order:**
   - Email subject lines use project number
   - Search by project in global search
   - Remember recent transactions
   - Use hyperlinks between records

2. **Static Proposal Mindset:**
   - Proposals in NetSuite still static
   - But separate from sales orders
   - Can compare if SO changes
   - Better audit trail

3. **Template Self-Service:**
   - Team manages own template changes
   - Document change reasons
   - Version control process
   - No more waiting on vendor

4. **Customer PO Management:**
   - Manual entry required
   - Track values and documents
   - Update as changes occur
   - Monitor dashboard alerts

### Resistance Points

1. **Transaction Number Change:**
   - "The one thing people get tripped up on"
   - Deeply ingrained habit
   - Memorization no longer works
   - Temporary frustration expected

2. **Catalog Loss:**
   - "Old timers use Core to write specs"
   - Need to learn Project Spec or other tools
   - Small order inconvenience
   - "That's a me problem" (Kipp)

3. **Process Changes:**
   - Separate transactions feel like more work
   - Different forms at different stages
   - New navigation patterns

### Success Factors

1. **Project Number Emphasis:**
   - Train on project-based reference
   - Demonstrate global search
   - Show hyperlink navigation
   - Practice with recent transactions

2. **Early Wins:**
   - Template self-service (immediate value)
   - Customer PO tracking (bank requirement met)
   - Better audit trail (compare quote to SO)
   - Approval automation

3. **Visual Aids:**
   - Transaction flow diagrams
   - Project number consistency shown
   - Search examples
   - Navigation demonstrations

4. **Support:**
   - NetSuite champions
   - Ongoing training
   - Documentation
   - Quick reference guides

---

## OPEN QUESTIONS FOR FUTURE SESSIONS

1. **Draft PO Concept:**
   - What is draft PO vs. vendor PO?
   - How does it improve organization?
   - Kipp's "shitstorm" comment - what specifically needs fixing?

2. **Tiered Pricing Solution:**
   - Will Dustin/Miller Knoll cooperate?
   - Technical feasibility?
   - Other manufacturers?
   - Orion standard or customization?

3. **Customer PO Tracking Design:**
   - Exact field structure?
   - Custom transaction or record?
   - Workflow for updates?
   - Dashboard KPIs?
   - Change order handling?
   - Multiple PO scenarios?

4. **Coupa Integration:**
   - Worth automating?
   - Email parsing reliable?
   - Volume justify effort?
   - Bi-directional integration?

5. **Catalog Integration:**
   - Configura/CET timeline?
   - Worth pursuing vs. external tools?
   - Impact on spec creation workflow?

6. **ServiceNet Integration:**
   - Scope and functionality?
   - Implementation timeline?
   - Impact on intermarket orders?

7. **E-Portals:**
   - What are e-portals?
   - Separate discussion needed?
   - Integration points?

---

*End of Master Transcript: Order Management*


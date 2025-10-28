
# Operations Comprehensive Follow-Up Discovery Session
## KBMH NetSuite/Orion Implementation

**Date:** October 2025  
**Session Duration:** Comprehensive single session covering all interconnected topics  
**Priority:** High - Field operations, outsourced installation coordination, and PM resource management critical to project success  
**Participants Needed:**
- Wendy (PM Manager/Operations Manager) - Primary
- Kipp (IT/Process) - For technical configuration and business rule logic
- Lorraine (CFO) - For financial/accounting impacts (VRA, labor costs)
- Matt (Leadership) - For strategic decisions on resource management
- PMs (Representatives) - For field perspective
- Receiving Team (Representative) - For warehouse/bin operations
- Rafina (Design Manager/Reconciliation) - For time tracking and contractor reconciliation
- Kimmy (Account Manager/Pre-Quote) - For account manager workload tracking perspective

---

## OVERVIEW

This comprehensive follow-up session will address critical gaps between what was discovered and what's needed for successful Operations configuration in NetSuite/Orion. The session covers 9 interconnected topic areas covering receiving and warehouse management, vendor center contractor portal, VRA and damaged product management, work order strategy, time tracking and rate configuration, labor markup business rules, punch list and field service strategy, scheduling and resource management approach, and training/change management for field adoption.

**Session Agenda:**
1. Receiving & Warehouse Management Strategy (Advanced Receiving, Bins, Vendor Notifications)
2. Vendor Center Contractor Portal Implementation & Adoption
3. VRA & Damaged Product Management Workflow
4. Work Order Management & Soft Scheduling Strategy
5. Time Tracking, Rates & External Contractor Integration
6. 15% Labor Markup Business Rules Configuration
7. Punch List & Field Service App Implementation
8. Scheduling & Resource Management Deep Dive (Additional Session Trigger)
9. Field App Training & Change Management Strategy
10. Decisions & Next Steps

---

## PART 1: CURRENT STATE KNOWLEDGE SUMMARY

### What We Know About Your Operations

Based on comprehensive discovery sessions, we have documented a strong understanding of your operational model and needs:

#### **Your Unique Operational Model**
- **Outsourced Installation**: "Not doing own installation - all work with third-party contractors"
- **Third-Party Warehouses**: Product ships to contractor warehouses, not your own
- **No Direct Warehouse Control**: Can't physically check inventory; rely on contractor communication
- **Email-Based Coordination**: Currently coordinating via email with installation partners
- **PM Oversight Role**: PMs coordinate and oversee but don't perform installation work
- **Multiple Locations**: Various third-party warehouse locations across region
- **High Volume Coordination**: "Thousands of intermarket transactions annually" plus direct customer installations

#### **Current State Challenges**
- **Email Receiving Notifications**: "They're sending it via email over to receiving@KBM" - easy to lose
- **Manual WIP Tracking**: Manually receiving product in system even though third-party warehouses receive physically
- **PlanGrid Subscription Cost**: "$$$$ per month" for punch list management
- **Manual PM Workload Management**: Wendy maintains Google Sheets calendar manually
- **Disconnected Communication**: Contractors don't have visibility into their work orders/POs
- **No Punch Location Memory**: "Four months later you've done 15 jobs. You're like, yeah, I'll remember what room that goes into. And you don't."
- **Contractor Time Reconciliation**: Manual process reconciling time entries vs. invoices
- **Complex Labor Markup Logic**: "KPMG 15%" formula with exceptions by order type

#### **Key Business Processes Discovered**
- **Purchase Requisitions**: Decision made to use for purchasing approval control
- **Advanced Receiving**: Orion custom tool with drag-and-drop for ease (not standard NetSuite)
- **Simple Bin Structure**: One bin per warehouse location (not granular tracking within warehouse)
- **Damaged Product Quarantine**: Separate bins to prevent accidental allocation
- **VRA Process Change**: Use VRA even when 80% of time not shipping back - for credit tracking
- **Work Order Approach**: Decision made (Wendy buy-in) but needs finalization
- **Soft Scheduling**: PM must approve scheduling requests
- **Time Tracking**: Impacts project GP, not GL
- **Field Service App**: Replaces PlanGrid with offline capability, floor plan pinning, geological check-in
- **Vendor Center**: Portal for contractors to see POs, work orders, communicate without email

#### **Financial & Cost Structure Discovered**
- **PM Flat Rates**: Not hourly - flat internal rate and separate client billing rate
- **Design Rates**: Multiple rates (workshop designer lower than standard designer)
- **Negotiated Client Rates**: Some clients have special PM/design rates with fixed internal cost
- **Contractor Time**: External contractors enter time at KBM standard rate (not their invoice rate)
- **15% Labor Markup**: Cost-only line that auto-calculates on every order with labor
- **Design Loses Money**: "We lose money on design. Design does not make money."
- **Storage Fees**: Variable by warehouse (30-90 day free periods), billed back to client

#### **Integration & System Points**
- **ServiceTime**: Intermarket orders integration
- **Paylocity**: Time tracking import (future)
- **Coupa Evaluation**: Email parsing for PO automation
- **Miller Knoll ServiceNet**: Price validation and direct bill coordination
- **Field Service App**: Tablet/mobile for PMs and contractors

#### **Team Structure & Roles**
- **Wendy**: PM Manager, manages workload and resource allocation
- **Kipp**: IT/Process specialist, owns 15% markup logic and business rules
- **Rafina**: Design Manager, reconciles contractor time vs. invoices
- **PMs**: Field coordination, punch list management, client communication
- **Receiving Team**: Process product arrivals, manage bins
- **Installation Contractors**: Field installation, punch walks, equipment delivery
- **Finance (Lorraine)**: VRA and credit tracking, time impact on GP

---

## PART 2: COMPREHENSIVE DISCUSSION TOPICS

### TOPIC 1: RECEIVING & WAREHOUSE MANAGEMENT STRATEGY

**Context:** Advanced Receiving tool is custom Orion innovation for drag-and-drop receiving. Simple bin structure (one per warehouse) matches outsourced model. Vendor center receiving notifications will replace email.

**What We Know:**
- Advanced Receiving: "Utility that sits on top of NetSuite" making receiving "kind of clunky" in standard NetSuite
- Drag-and-drop interface: "Grab items and I can just drag them to the bin and that's it, now they're received"
- Tablet/desktop compatible
- One bin per warehouse: "Only one bin at that location because you don't care where it's being tracked there"
- Damaged bin per location: Prevents accidental allocation
- Duplicate/overage bin per location: Handles excess and duplicate shipments
- Vendor center notification: Contractors notify KBM when product arrives
- Simple approach: Not granular bin tracking within warehouse

**Discussion Points:**

1. **Advanced Receiving Tool Capability & Training**
   - When will tool be demoed? (Full operations suite demo needed)
   - Mobile/tablet optimization: Works well on iPad? Android tablets?
   - Learning curve: How complex is drag-and-drop interface?
   - Performance: Does it work with large POs (50+ lines)? 100+ lines?
   - Connectivity: What happens if warehouse has intermittent WiFi?
   - Barcode scanning: Can items be scanned instead of manually dragged?
   - Training duration: How long to train receiving team?

2. **Bin Structure Finalization**
   - **Complete warehouse location list**: Names and addresses?
   - **Office/showroom bins**: Do we need receiving bin for office location?
   - **Direct-to-site handling**: How tracked if no receiving bin?
   - **Bin naming convention**: Standard naming format across all locations?
   - **Bin capacity limits**: Any limits on items per bin?
   - **Bin transfers**: How do we move items between bins? (Same location or different location?)

3. **Damaged Product Process**
   - **Damage identification**: Who determines if item is damaged? (Contractor or KBM receiving?)
   - **Communication of damage**: Current process for contractor to notify of damage?
   - **Damage documentation**: Photos required? Condition notes?
   - **Damaged bin allocation**: Should we track why damaged? (Shipping damage, impact, defect?)
   - **Damaged item replacement**: When does VRA process start?
   - **Warehouse quarantine**: Can contractors see damaged bin? Should they access replacement item?

4. **Overage/Duplicate Inventory**
   - **Frequency of overages**: How often does this happen?
   - **Duplicate shipment process**: Is it preventable? How does it currently occur?
   - **Resolution**: How does overage get resolved? (Return to vendor? Keep as extra stock?)
   - **Stock availability**: Can overage be re-allocated to other orders?

5. **Receiving Notification via Vendor Center**
   - **Contractor adoption**: How to get contractors to use portal instead of email?
   - **Mobile-friendly**: Can contractors notify from phone while unloading?
   - **Fallback if not adopted**: Email process stays as backup?
   - **Notification workflow**: Does notification go to reminders portlet? Email? Dashboard?
   - **Receiving team action**: What happens after notification received? (Manual check or auto-trigger?)
   - **SLA for receiving**: How long after notification should receiving happen in NetSuite?

6. **Direct Receiving by Contractors (Future)**
   - **Phase 2 consideration**: Should this be pursued eventually?
   - **Current blockers**: Permission creep, mistakes, trust levels
   - **Pain relief if implemented**: What would improve for KBM?
   - **Risk if implemented**: How to prevent accidental receiving of entire PO?
   - **Timing**: After vendor center adoption is solid? Year 2? Never?

7. **Receiving Process Training**
   - **Who needs training**: Receiving team + any PMs who might receive?
   - **Contractors training**: If contractors eventually can receive, training needs?
   - **Frequency**: Is receiving transaction volume high enough to need refresher training?
   - **Documentation**: Quick reference guide for receiving team?

---

### TOPIC 2: VENDOR CENTER CONTRACTOR PORTAL IMPLEMENTATION & ADOPTION

**Context:** NetSuite Vendor Center will provide contractors portal access with no per-user licensing cost. Critical for adoption is helping contractors understand value and making it easy to use.

**What We Know:**
- No additional license cost: "Use one license for everybody"
- Contractor access scope: View POs, work orders, project info, communicate
- Document attachment: Contractors can upload photos, documents
- Communication tools: Notes and comments capability
- Receiving notification feature: Custom Orion development
- Current email coordination: "Sending via email" communication will be eliminated
- Implementation timing: Before or after full system go-live?

**Discussion Points:**

1. **Complete Contractor Access List**
   - How many contractors total? (Estimate for portal access)
   - Are all contractors equal tier or different security levels?
   - Any contractors who shouldn't have portal access?
   - Specialty contractors (HVAC, electrical) vs. general installers?
   - One-time contractors vs. regular partners?
   - Associated companies vs. individual contractors?

2. **Contractor Security & Role Setup**
   - What should contractors see in vendor center?
     - Only their own POs/work orders?
     - Can they see other contractors' work on same project?
     - Can they see financial terms (pricing)?
   - What should contractors NOT see?
     - Pricing/margin information?
     - Other contractors' details?
     - Company operations data?
   - Password management: How will contractor credentials be managed?
   - Multi-user within contractor organization: Can multiple people from same contractor access?

3. **Receiving Notification Workflow**
   - **Step 1**: Product arrives at contractor warehouse
   - **Step 2**: Contractor logs into vendor center
   - **Step 3**: Contractor finds relevant PO
   - **Step 4**: Contractor clicks "Notify of Arrival" (or similar)
   - **Step 5**: KBM receiving notification appears (where? dashboard? reminders? email?)
   - **Step 6**: KBM receiving clerk goes to PO and uses Advanced Receiving tool
   - **Step 7**: Items dragged to appropriate bins
   - Clarification: How does contractor specify damage/quantities if different from PO?

4. **Communication & Document Features**
   - Current use cases for notes/comments:
     - "Product arrived with 2 items damaged"?
     - "Need replacement ASAP for job on Thursday"?
     - Photo attachments for damage documentation?
     - Signed delivery confirmation?
   - Training contractors on how to add notes/attachments?
   - Will Finance/Rafina review? Or just KBM receiving?

5. **Contractor Adoption Strategy**
   - **How to communicate change**: Email? Phone call? In-person meeting?
   - **Why contractors should care**: What's the benefit for them?
     - "No more sending emails" (one-way benefit - KBM benefit)
     - "See all your work and POs in one place" (contractor benefit)
     - "Communication tracked and documented"
   - **Training provided**: Live training session? Recorded video? Written guide?
   - **Support during transition**: Who do contractors call if vendor center not working?
   - **Parallel period**: Run email and vendor center for a while?
   - **Cutover date**: When does email receiving stop being accepted?

6. **Vendor Center Capabilities Exploration**
   - Can contractors create POs themselves? (No - probably not wanted)
   - Can contractors see project schedule/timeline? (Yes - helpful for planning)
   - Can contractors request scheduling changes? (Maybe - through notification system)
   - Can contractors upload delivery signatures? (Yes - good for proof of delivery)
   - Can contractors leave feedback/comments on completed work? (Maybe for quality feedback)

7. **Scaling for Volume**
   - If thousands of intermarket orders annually: How does portal scale?
   - Performance with high volume notifications?
   - Batch notifications vs. real-time?
   - Old notifications: Do they clutter interface or archive automatically?

---

### TOPIC 3: VRA & DAMAGED PRODUCT MANAGEMENT WORKFLOW

**Context:** Critical pain point identified: "People will enter lines for credits that we're expecting. And then they just kind of, there's not really a way to track it." VRA process will provide systematic tracking and follow-up on expected vendor credits.

**What We Know:**
- Current problem: Expected credits entered but never tracked/collected
- Lorraine's frustration: "I just like throwing it out there. I hope we get this. And then no one ever really follows up on it."
- 80/20 rule: 80% of damaged products not shipped back, 20% are
- VRA even if not shipping: Still use VRA for damage documentation and credit tracking
- Zero-cost replacement line: Add to existing PO when requesting replacement
- Vendor pressure tactic: End-of-month report with "TBD" credit numbers gets vendor attention
- Accounting treatment: Need to define for period-end reconciliation

**Discussion Points:**

1. **VRA Process for Each Damage Scenario**
   - **Scenario 1: Damage, Vendor Ships Replacement**
     - Step 1: Receive damaged items to damaged bin
     - Step 2: Notify vendor of damage
     - Step 3: Vendor agrees to send replacement
     - Step 4: Add zero-cost line to existing PO
     - Step 5: Receive replacement to normal bin (now have duplicate? Move damaged to scrap?)
     - Step 6: Create VRA for damaged items
     - Step 7: Receive VRA (no shipment because replacement on PO)
     - Step 8: Vendor issues credit memo
     - Step 9: Enter credit memo in bill credits
   - **Scenario 2: Damage, Vendor Issues Credit**
     - Similar but credit instead of replacement
   - **Scenario 3: Damage, We Handle Scrapping**
     - Damaged item won't be replaced - we'll dispose
     - Still need VRA for credit tracking

2. **Damaged Product Disposition Options**
   - **Replace via PO**: Vendor ships replacement at no cost
   - **Credit Issue**: Vendor issues credit memo for damaged item cost
   - **We Scrap**: We handle disposal, vendor doesn't pay for damage
   - **Warranty Claim**: Is damaged item warranty replacement vs. vendor responsibility?
   - Process: How is decision made for each damaged item?

3. **VRA Approval Workflow**
   - Who approves VRA creation? (Receiving clerk? Wendy? Lorraine?)
   - Is approval automatic or manual review?
   - Time sensitivity: Should VRA be created immediately or batched end of week?
   - Change orders: Can VRA be adjusted if vendor disputes or customer requests change?

4. **End-of-Month Credit Report**
   - **Current process**: Send vendor report with expected credits (Marcus's "TBD" tactic)
   - **Report content**: All expected credits, organized by date/reason?
   - **Format**: Excel? PDF? Email attachment?
   - **Recipients**: Each vendor gets their own report? All in one report?
   - **Timing**: When sent during month? End of month?
   - **Effectiveness**: Does vendor pressure tactic work? How often?
   - **Follow-up**: What if vendor doesn't respond to report?

5. **Bill Credit Application**
   - **Vendor Credit Memo Receipt**: What's the process?
   - **Credit Number**: Vendor provides? We generate?
   - **Amount matching**: Verify credit memo amount matches original damage estimate?
   - **Application**: Apply to next invoice from vendor? Or manual?
   - **Timing**: How long between VRA and credit memo typically?
   - **Discrepancies**: What if credit memo doesn't match? (Vendor lowballs us?)

6. **Accounting Treatment for Period-End**
   - **Accrual**: How do we record expected but not-yet-received credits?
   - **Period-end adjustment**: What happens if credit spans fiscal period boundaries?
   - **Write-off**: If credit never received after 6 months, when do we give up?
   - **Lorraine's challenge**: How to ensure credits don't fall through cracks after initial entry?

7. **VRA Reporting & Tracking**
   - **Dashboard/report**: Should VRA status be visible to PMs?
   - **Replacement status**: Track when replacement received vs. when installed?
   - **Customer communication**: Do we tell customer about damage/replacement or handle transparently?
   - **Project impact**: Does damage delay project? How tracked?

8. **Documentation & Notes**
   - **Reason field**: Document reason for damage (shipping damage, site damage, defect, etc.)
   - **Photos**: Should damage photos be attached to VRA?
   - **Vendor communication**: Should we document vendor conversations in VRA?
   - **Project reference**: Which project was damaged item for?

---

### TOPIC 4: WORK ORDER MANAGEMENT & SOFT SCHEDULING STRATEGY

**Context:** Wendy "signed on for work orders" but decision is soft (not finalized). Work orders needed to organize PM activities, coordinate with contractors, and track event-based workflow. Soft scheduling means request-based with PM approval.

**What We Know:**
- Soft buy-in: "Wendy signed on for work orders just now, so that was good"
- Can be simple or sophisticated: "Can be as easy or sophisticated as you want it to be"
- Generation: Create from sales order without picking specific lines
- Event types: Site verification, delivery/install, site review, PM on-site, design meetings, punch walks
- Assignment: To PM or contractor
- Soft scheduling: Not hard scheduled; PM must approve
- Event-driven: Work order events drive time entry and punch list

**Discussion Points:**

1. **Work Order vs. Current Process**
   - **Current**: Email coordination, Google Sheets calendar, informal scheduling
   - **Future**: Formalized work order events, soft scheduling with approval
   - **Change for PMs**: Will they resist new formal process?
   - **Pain relief**: What improves for Wendy as PM Manager?
     - Better visibility into PM workload?
     - Structured event tracking?
     - Automatic task assignment?

2. **Work Order Event Type Configuration**
   - **Site Verification**: PM pre-install visit (scope confirmation, site assessment)
   - **Delivery and Install**: Main delivery/installation event
   - **Site Review**: Post-installation review before punch walk
   - **PM On-Site Presence**: PM required on-site during delivery (not PM doing install)
   - **Design Meetings**: If design meetings happen on-site as part of project
   - **Punch Walks**: Final punch walk before project completion
   - Are there other event types needed?

3. **Soft Scheduling Approval Workflow**
   - **Current**: No formal scheduling - happens via email/calendar
   - **Future workflow**:
     - Step 1: Operations/scheduling person requests time slot for PM
     - Step 2: Work order event created with soft schedule (proposed date/time)
     - Step 3: Notification goes to PM: "You have a soft-scheduled site verification for Thursday 10am"
     - Step 4: PM approves (confirms they'll do it) or rejects (suggests alternative)
     - Step 5: Once approved, work order goes hard scheduled
   - **Approval timing**: Must PM respond same day? Can they sit on request?
   - **Escalation**: What if PM doesn't respond? Manager override?

4. **Work Order Creation & Generation**
   - **Trigger**: When is work order created? (SO created? After acknowledgement sent? Manual trigger?)
   - **Automatic generation**: Do all SOs auto-generate work orders or manual selection?
   - **Line item selection**: Do we specify which items on SO are related to which event? (No - mentioned not needed)
   - **Quick creation**: Need to be quick process for high volume

5. **Resource Assignment**
   - **PM Assignment**: Work order assigned to which PM? (How selected?)
   - **Contractor Assignment**: If contractor doing delivery, assigned to them?
   - **Multiple resources**: Can multiple PMs be assigned? (Yes for co-install projects)
   - **PM preferences**: Should we consider PM preferences/specialties?

6. **Work Order Complexity Decision**
   - **Simple approach**: Create work orders, assign, schedule - don't over-engineer
   - **Advanced approach**: Task templates, dependencies, phase tracking
   - **Historical resistance**: "Every time we've proposed it to dealers, it was too much"
   - **KBM desire**: Wendy wants task lists but also wants autonomy
   - **Balance**: How many tasks before it feels micromanagement? (10 tasks ok? 300 tasks too many?)

7. **Integration with Field Service App**
   - **Work order events**: Appear on PM's field app?
   - **Check-in**: PM checks in at work order location via app?
   - **Time entry**: Time logged to work order event?
   - **Punch creation**: Punch items tied to work order event?
   - **Status updates**: PM updates status in field (in progress, complete)?

8. **Contractor Work Order Visibility**
   - **Vendor center**: Can contractors see their assigned work orders?
   - **Delivery schedule**: Contractor knows when they need to be available?
   - **Site requirements**: Contractor sees any site requirements/notes?
   - **Communication**: How does contractor confirm they're available?

9. **PM Task List Vision (Wendy)**
   - **Template tasks**: When PM assigned, automatic task list appears?
   - **Standard tasks**: Site verification, delivery, walkthrough, etc.
   - **Accountability**: PM must acknowledge receipt of task?
   - **Completion tracking**: PM marks tasks complete as they happen?
   - **If not completed**: Someone knows it's missing (escalation)?
   - **Difficulty**: Is this too much structure? Or helpful?

---

### TOPIC 5: TIME TRACKING, RATES & EXTERNAL CONTRACTOR INTEGRATION

**Context:** Time tracking impacts project GP (not GL). Multiple rate structures needed: PM flat rates, designer rates (workshop vs. standard), negotiated client rates. External contractors enter time at KBM standard internal rates (not their higher contractor rates).

**What We Know:**
- Time impacts GP only, not GL
- PM rates: Flat rate (not hourly), internal cost rate, external client billing rate
- Design rates: Multiple rates (workshop designer lower rate, standard designer higher rate)
- Client negotiation: Some clients have special PM/design rates
- External contractors: Enter time at KBM standard rate (even if contractor charges more)
- Example: "Contractor charges $95/hour but KBM rate is $85/hour, only $85 impacts project"
- KBM absorbs difference when understaffed
- Rafina reconciles: Time entered vs. invoice received
- Design reality: "We lose money on design. Design does not make money."

**Discussion Points:**

1. **Complete Rate Matrix Documentation**
   - **PM Rates**:
     - Internal PM flat rate (cost to project)?
     - External PM billing rate (to customer)?
     - Any by-client exceptions?
   - **Design Rates**:
     - Workshop designer internal rate?
     - Workshop designer external rate?
     - Standard designer internal rate?
     - Standard designer external rate?
     - Any other designer types (field designers)?
   - **Client-specific rates**:
     - List clients with negotiated rates?
     - How different from standard?
   - **Effective date**: When do rate changes take effect?
   - **Historical rates**: Need to track prior year rates for historical accuracy?

2. **Rate Configuration in NetSuite**
   - **Rate tables**: How many rate types needed?
   - **Time entry interface**: How does PM enter time? Select rate type or auto-populated?
   - **Client-specific**: How to handle client-specific rates? (Override on each entry? Or automatic?)
   - **Rate change dates**: How to handle mid-project rate changes?
   - **Accuracy**: If rate wrong on time entry, how corrected?

3. **External Contractor Time Entry**
   - **Current access**: "Some of our contractors, they have core time-entry access"
   - **Contractor list**: Which contractors need direct system access?
   - **Training**: How do contractors learn time entry process?
   - **Accuracy**: Will contractors enter hours correctly?
   - **Verification**: Rafina reconciles time vs. invoice - what if mismatch?

4. **Contractor Time vs. Invoice Reconciliation**
   - **Rafina's process**: Compare time entered to invoice received
   - **Mismatch scenarios**:
     - Contractor billed $95/hour but only entered 40 hours vs. 45 hours on invoice
     - Contractor billed 50 hours but only entered 40 hours in time entry
   - **Resolution**: How does Rafina handle mismatch?
   - **Communication**: Does Rafina contact contractor? Adjust time entry?
   - **Frequency**: How often is reconciliation done? (Monthly? Weekly? As invoices arrive?)

5. **Special Rate Cases**
   - **Temporary rates**: Short-term contract at different rate?
   - **Learning/junior rates**: Lower rate for less experienced staff?
   - **Overtime premium**: Higher rates for overtime hours?
   - **Travel time**: How billed? (To project? G&A?)
   - **Billable vs. non-billable**: All time billable or some non-billable?

6. **Time Entry Interfaces & Workflows**
   - **Desktop time entry**: Where do PMs/designers enter time?
   - **Field app time entry**: Can contractors enter from tablet in field?
   - **Work order event time**: Time tied to specific work order event? (Yes - understood from field app description)
   - **Approval process**: Does anyone review/approve time entries before GP calculated?
   - **Backdating**: Can time be entered after-the-fact? (How long after?)

7. **Training & Compliance**
   - **"Slapped around" compliance**: Time tracking "is a pain in the butt" - how to improve?
   - **Weekly requirement**: Ideal is weekly time tracking
   - **Reality**: People delay or forget
   - **System enforcement**: Can we require weekly entry? Block other actions if time not entered?
   - **Manager reminders**: Should reminders portlet show incomplete time entries?

8. **Contractor Cost Absorption**
   - **Understanding the reality**: "We're understaffed, and so therefore KBM Hoag takes the hit"
   - **Why this is necessary**: Design doesn't make money anyway
   - **Accounting**: How is $10/hour difference reflected in project? (Nothing? G&A absorption?)
   - **Future decision**: Should policy change? (Cap KBM cost absorption?)

---

### TOPIC 6: 15% LABOR MARKUP BUSINESS RULES CONFIGURATION

**Context:** Complex business rule requiring custom NetSuite configuration. Formula line auto-calculates 15% of external labor cost, decreases project GP. Applied to most orders but has exceptions by order type and possibly by client. Kipp to provide complete exception logic.

**What We Know:**
- Auto-calculates on every order
- Cost-only line (no revenue component)
- Takes 15% of external labor cost
- Decreases project GP (behavioral forcing function)
- No GL impact (GP only)
- Line is "KPMG 15%"
- Currently appears as line 1 (Kipp's complaint)
- Kipp wants: Bottom position, uneditable, non-printing, always dynamic
- Exceptions: "Based off of order type, not based off of client. You could add in additional exceptions by client if you wanted to as well."
- Purpose: Force higher markup on labor, account for unpredictability

**Discussion Points:**

1. **15% Markup Logic Understanding**
   - **How calculated**: Takes 15% of which labor? (External warehouse/install labor only)
   - **Line code identification**: How identified? (Specific line code for external labor?)
   - **Auto-recalculation**: If labor line added after initial order creation, does 15% auto-recalc? (Yes - "always dynamic")
   - **Multiple labor lines**: If two external labor lines, is 15% calculated on total or each line?
   - **Labor-less orders**: What if order has no labor? (Line should not appear?)

2. **Exception Logic by Order Type**
   - **Order types**: Which order types exist?
     - Direct Bill Orders?
     - Intermarket Orders?
     - Government Orders?
     - Intuit Work from Home Orders?
     - Standard orders?
   - **Which have exceptions**: Which order types get 15% markup? Which don't?
   - **Complete logic needed**: "I just need to know, like, that full logical expression" - Kipp must provide
   - **IF statement**: Order Type = X AND Order Type != Y AND...?

3. **Client-Based Exceptions**
   - **Possible per-client exceptions**: Can we add exceptions by client? (Kipp mentioned possibility)
   - **Examples needed**: Any clients that shouldn't have 15% markup?
   - **How implemented**: Custom client field? Lookup table?

4. **Line Positioning Requirements** (Kipp's Wish List)
   1. **Keep the line**: Most important - must be there
   2. **Position at bottom**: Not line 1 (for proposal line numbering)
   3. **Uneditable**: Can't be manually changed by account manager
   4. **Non-printing**: Doesn't show on customer proposals
   5. **Always dynamic**: Auto-recalculates when labor lines change

5. **Commission Impact**
   - **Is this line commissionable?**: Do account managers get commission on 15% markup?
   - **Recommendation**: Probably not (it's a cost reduction, not revenue)
   - **Confirmation needed**: Verify with Matt/Kipp

6. **Testing & Validation**
   - **Test scenarios**: Multiple orders with different labor lines, different order types
   - **Before go-live**: Extensive testing to ensure logic works
   - **Edge cases**: Orders with mix of internal/external labor?
   - **Rate changes**: If labor rates change mid-project, does 15% recalculate correctly?

7. **Training & Communication**
   - **Account managers**: Understand that 15% is forced, not their choice
   - **Behavioral purpose**: Understand why force higher labor markup (unpredictability)
   - **Can't override**: Make clear line is uneditable
   - **Questions**: Who do they call if they want exception?

8. **Historical Data Migration**
   - **Existing orders**: How handle 15% on existing orders in system?
   - **Phase-in date**: When does 15% start applying? (All new orders only?)
   - **Retroactive**: Apply to existing backlog or not?

---

### TOPIC 7: PUNCH LIST & FIELD SERVICE APP IMPLEMENTATION

**Context:** Orion Field Service app replaces PlanGrid with custom punch list functionality including offline mode, floor plan pinning, geological check-in, and status report generation. Critical for field operations since PMs must adopt tablet/mobile workflow.

**What We Know:**
- Replaces PlanGrid: "One last thing to pay for" - eliminates subscription cost
- Tablet primary: iPad primary device, but mobile-responsive for phones
- Offline capability: Download work info, work offline, sync when back online
- Floor plan pinning: "Pin punch to floor plan location" so can remember where issue was months later
- Geological check-in: Confirms PM actually on-site
- Photo attachment: Attach photos to punch items
- Status reports: Generate and send from field app (added during session)
- Punch reasons/issues: Categorize what's wrong

**Discussion Points:**

1. **Floor Plan Upload & Pinning**
   - **File formats supported**: Which file types? (PDF? Images? CAD files?)
   - **File sources**: Where do floor plans come from? (Customer provides? Architect? Project team?)
   - **Upload process**: Who uploads floor plan to work order? (PM? Coordinator?)
   - **Multiple floors**: How handle multi-story projects? (Separate floor plans? Layer?)
   - **Scale/accuracy**: Must floor plan be to scale for pinning to work?
   - **Markup precision**: How precise is pinning? (General room or exact location?)

2. **Punch Item Types & Categorization**
   - **Generic "issues" concept**: NetSuite uses "issues" for multiple purposes
   - **Punch list items**: What's wrong (e.g., "Paint scratch on door frame")
   - **Punch reasons**: Why (e.g., "Installation damage" or "Factory defect")?
   - **Responsible party**: Who fixes (contractor? KBM? Factory warranty?)
   - **Priority**: Urgent vs. minor cosmetic?
   - **Associated line items**: Can punch be tied to specific product/line on order?
   - **Assignment**: Who responsible for fix? (PM? Contractor? Assigned to?

3. **Offline Mode Deep Dive**
   - **Download scope**: What downloads? (Just today's work? Week's work? Everything assigned?)
   - **Data sync timing**: How long to sync when reconnected? (Immediate? Queued?)
   - **Conflict resolution**: If punch added offline and someone else added punch to same item?
   - **Real-time changes**: If schedule changes while offline, how updated? (After sync?)
   - **Connectivity edge cases**: What if intermittent WiFi (connected, disconnected, connected)?

4. **Geological Check-In**
   - **Purpose**: Confirm PM actually at project location (accountability)
   - **GPS accuracy**: How precise? (City block? Exact location?)
   - **Privacy concerns**: Do PMs object to location tracking? (Manager perspective?)
   - **Spoofing prevention**: Can PM check in from office? (Any prevention?)
   - **Time-based**: Does check-in stay active entire event? Or just checkpoint?
   - **Failure handling**: What if GPS unavailable? (Indoor location without signal?)

5. **Photo & Document Attachment**
   - **Photo quality**: Can take photos of punch items/damage?
   - **Storage**: Where stored? (NetSuite? Cloud storage? Device?)
   - **File size limits**: Any limits on photo size or quantity?
   - **Metadata**: Does photo capture timestamp/location automatically?
   - **Other documents**: Can PM attach non-photo files? (Sketches? Notes?)
   - **Signature collection**: Mentioned - customer or contractor signature?

6. **Status Report Generation**
   - **What was originally planned**: Back-end NetSuite generation
   - **What was added**: Generate from field app on tablet
   - **Content**: What's in status report?
     - Summary of work completed?
     - Punch items identified?
     - Photos of issues?
     - Floor plan with pinned items?
     - Next steps/timeline?
   - **Recipients**: Who is report sent to? (Customer? Project file? Email?)
   - **Timing**: Can generate end of shift? End of day? Weekly?
   - **Format**: PDF? Email attachment? Portal?

7. **Multi-Resource Time Entry**
   - **Scenario**: 5 resources working on same event
   - **Current process**: Fill in time once, applies to all
   - **Flexibility**: Can different resources have different hours? (Yes - select individual)
   - **Temporary resources**: Can add resources not originally assigned?
   - **Cleanup**: If wrong resource added, how removed?

8. **Field App Hardware & Device Management**
   - **iPad requirements**: Specific model? OS version? Storage?
   - **Ruggedness**: Will be used in construction environment - durability concerns?
   - **Battery life**: Can operate full day? Need mid-day charging?
   - **Device management**: Who maintains/updates apps?
   - **Training**: How long for PMs to learn app? Learning curve?
   - **Support**: Who handles field app technical issues?

9. **Work Order Event Integration**
   - **Event creation**: Work order events appear on PM's app?
   - **Check-in location**: Check-in to work order event location?
   - **Time tracking**: Time entry to work order event?
   - **Punch association**: Punch items tied to work order event?
   - **Status updates**: Event marked complete in app?

10. **PlanGrid Transition Plan**
    - **Parallel period**: Run both PlanGrid and new app for a while?
    - **Migration of existing**: Can punch items from PlanGrid be imported?
    - **PlanGrid cutoff**: When is PlanGrid access disabled?
    - **Historical data**: After cutoff, how access old punch lists?
    - **Change management**: How to manage PMs comfortable with PlanGrid?

11. **Punch List Workflow Post-Generation**
    - **Review**: Who reviews punch list from field? (PM? Project coordinator? Customer?)
    - **Assignment**: How assigned for fix? (Contractor? KBM? Customer?)
    - **Tracking**: How tracked to completion? (Mark complete in app? Follow-up email?)
    - **Timeline**: How know when punch should be complete?
    - **Punch walk scheduling**: When does final punch walk happen?

---

### TOPIC 8: SCHEDULING & RESOURCE MANAGEMENT (Additional Session Required)

**Context:** Complex topic requiring dedicated additional session. Tension between Asana-style workflow with task dependencies vs. maintaining PM autonomy. Wendy's PM workload calendar currently manual Google Sheets. Account managers need pre-quote workload tracking. No decisions made yet - explicitly deferred to additional session.

**What We Know:**
- Currently manual: Wendy maintains Google Sheets calendar with timelines by PM
- Manual and inaccurate: "Only as accurate as the information... Have they updated it"
- PM assignment timing change: Desired shift to assign PM at same time as designer
- Wendy's vision: "Get a list of tasks... site verification, delivery, walkthrough, all these different things"
- Manager perspective (Kimmy): "I want to know what phase of project they're at, the volume of those projects, and the timeline" - not micro-manage tasks
- Asana inspiration (Kimmy): "When you complete a task, they're going to queue the next thing... workflow where if you're waiting for someone"
- Dealer resistance: "Every time we've proposed it to dealers, it was too much. They wanted more flexibility"
- NetSuite Suite Projects: Native project management available but dealers don't use it
- Sophistication decision: "Do we build 10 phases or 300 things that happen in each one of those phases?"
- Employee pushback concern: "You hired me to do the job. Trust me to do the job. I don't need a list to tell me what my job is."

**This topic requires dedicated follow-up session - not detailed here.**

---

### TOPIC 9: FIELD APP TRAINING & CHANGE MANAGEMENT STRATEGY

**Context:** Significant behavior change required for PMs and contractors. Shift from email/spreadsheet coordination to system-based workflow. Field app adoption critical. Need comprehensive training and change management approach.

**What We Know:**
- New tool adoption: Shift from PlanGrid to Orion Field Service app
- Contractor adoption needed: Vendor center portal instead of email
- PM workload change: Formalized work orders instead of informal scheduling
- Time entry behavior: Weekly compliance important but "people have to be slapped around a little bit"
- Offline capability: New workflow for connectivity-challenged buildings
- Field equipment: Tablet usage may be new for some PMs

**Discussion Points:**

1. **Field App Adoption Strategy**
   - **Who needs training**: All PMs? Only certain PMs? Contractors?
   - **Device rollout**: How many iPads needed? Budget?
   - **Phased rollout**: Pilot with subset of PMs first? Or all at once?
   - **Support period**: How long transition while people still learning?
   - **Old tool parallel**: Run PlanGrid and new app together? How long?

2. **Training Approach & Materials**
   - **Training format**: In-person? Recorded video? Self-paced? Hands-on?
   - **Training duration**: 30 minutes per person? Half-day? Day-long?
   - **Timing**: Before go-live? First week? Ongoing?
   - **Train-the-trainer**: Should KBM staff become trainers?
   - **Materials**: Quick reference guide? Video library? Checklists?
   - **Languages**: Any PMs or contractors non-English speaking?

3. **Change Communication Plan**
   - **"Why" messaging**: Help PMs understand benefits
     - "PlanGrid replacement saves money"
     - "Offline mode works in buildings without WiFi"
     - "Floor plan pinning - remember where issues are"
     - "Check-in confirmation helps with accountability"
   - **Timing**: When communicate? How long before go-live?
   - **Forums**: Team meetings? Email? One-on-one?
   - **FAQ document**: Address common concerns upfront

4. **Resistance Management**
   - **"I like PlanGrid"**: Address comfort with current tool
     - Show new tool features
     - Demonstrate ease of use
     - Highlight cost savings
   - **"This is too complicated"**: Address learning curve concerns
     - Emphasize it's similar to PlanGrid
     - Offer extended training
     - Assign power users as peer support
   - **"I don't want to use a tablet"**: Address technology resistance
     - Show ruggedness/durability
     - Demonstrate battery life
     - Offer training on basic tablet skills

5. **Post-Go-Live Support**
   - **Help desk**: Who handles field app technical issues?
   - **Remote support**: Can field app issues be fixed remotely or on-site?
   - **Critical issues**: Process for urgent issues during live projects?
   - **Enhancement requests**: How do PMs request new features?
   - **SLA for support**: How quickly must issues be resolved?

6. **Performance Monitoring**
   - **Adoption metrics**: Are PMs using app? How frequently?
   - **Punch list quality**: Are punch items complete/useful?
   - **Time accuracy**: Are time entries timely and complete?
   - **Check-in compliance**: Are PMs checking in?
   - **Status report usage**: Are status reports being generated?
   - **Feedback**: What's working? What's broken?

7. **Success Measurement**
   - **60-day check-in**: How is adoption going? Any issues?
   - **90-day review**: Can we retire PlanGrid?
   - **User satisfaction**: Survey on app usability
   - **Efficiency gains**: Are processes faster than PlanGrid?
   - **Cost savings**: How much PlanGrid budget saved?

---

## PART 3: OUTSTANDING DECISIONS REQUIRED

The following strategic decisions are pending and need to be made during this session to proceed with configuration:

### DECISION 1: Work Order Final Confirmation
**Decision Maker:** Wendy (Operations) with Matt (Leadership)  
**Impact:** Medium - Changes how PM coordination works  
**Status:** Soft buy-in from Wendy; final confirmation needed

**Options:**
1. **Implement work orders**: Full formalized system with events and soft scheduling
2. **Skip work orders**: Continue email/calendar coordination (no system change)
3. **Phased approach**: Start simple, expand over time

---

### DECISION 2: Scheduling & Resource Management Sophistication
**Decision Maker:** Wendy (PM Manager), Kimmy (Account Manager Lead), Matt (Leadership)  
**Impact:** High - Affects PM workload management and account manager pre-quote tracking  
**Status:** Complex discussion deferred to additional session

**Options:**
1. **High-touch task management**: 300+ granular tasks per project, dependencies, Asana-style
2. **Medium-level phase management**: 10 phases with key tasks, structured but not overbearing
3. **Lightweight approach**: Just work order events, no formal task list

---

### DECISION 3: Advanced Receiving Vendor Center Rollout Timing
**Decision Maker:** Wendy (Operations) with Kipp (IT)  
**Impact:** Medium - Affects contractor adoption and receiving process  
**Status:** Implementation timing needed

**Options:**
1. **Phase 1 go-live**: Implement vendor center and Advanced Receiving with main system go-live
2. **Phase 2 later**: Wait 2-3 months after go-live, contractors more settled
3. **Gradual rollout**: Email first 1 month, then introduce vendor center in month 2

---

### DECISION 4: 15% Labor Markup Exception Logic
**Decision Maker:** Kipp (IT) with Matt (Leadership) approval  
**Impact:** High - Must be configured correctly or GP calculations wrong  
**Status:** Kipp to provide complete exception logic

**Questions:**
- Which order types have exceptions?
- Are there client-based exceptions?
- What's the complete IF/THEN logic?

---

### DECISION 5: Contractor Direct Receiving (Future)
**Decision Maker:** Wendy (Operations) with Matt (Leadership)  
**Impact:** Medium - Future phase decision  
**Status:** Deferred to Phase 2

**Questions:**
- After vendor center adoption is solid, revisit contractor direct receiving?
- Trust level sufficient after 3-6 months?
- Risk acceptable if implemented later?

---

## PART 4: PRE-WORK & PREPARATION

To make the most of this comprehensive session, please prepare the following:

### Advanced Receiving & Bins Topic:
- [ ] Complete list of third-party warehouse locations with names/addresses
- [ ] Confirm office/showroom bin needs
- [ ] Proposal for bin naming convention
- [ ] Demo schedule for Advanced Receiving tool

### Vendor Center Topic:
- [ ] Complete list of contractors needing portal access
- [ ] Contractor contact information for onboarding
- [ ] Proposed receiving notification workflow
- [ ] Backup plan if contractors don't adopt portal

### VRA & Damaged Product Topic:
- [ ] Confirm damaged product disposition options
- [ ] Accounting treatment for damaged item write-offs
- [ ] Sample VRA from current system for reference
- [ ] Confirm end-of-month credit report format needed

### Work Order Topic:
- [ ] Final confirmation from Wendy on work order usage
- [ ] Sample current process for event scheduling
- [ ] Proposed event types (expand beyond 6 listed if needed)

### Time Tracking & Rates Topic:
- [ ] Complete PM rate matrix (internal and external rates)
- [ ] Complete design rate matrix (all designer types)
- [ ] List of clients with negotiated rates
- [ ] List of external contractors with time entry access

### 15% Labor Markup Topic:
- [ ] Complete exception logic from Kipp (critical)
- [ ] All order types and their exceptions
- [ ] Client-based exceptions if any
- [ ] Confirm line item code for external labor identification

### Punch List Topic:
- [ ] Sample floor plans showing typical project layouts
- [ ] Current PlanGrid report examples (format Wendy wants replicated)
- [ ] List of punch issue types/categories
- [ ] Proposed device management approach

### Scheduling Topic:
- [ ] Pre-work for additional session (defer detailed prep)

### Training Topic:
- [ ] Identify internal PM trainers/power users
- [ ] Identify contractor liaison for training coordination
- [ ] Preferred training timeframe
- [ ] Availability for post-go-live support period

---

## PART 5: SESSION DELIVERABLES & SUCCESS CRITERIA

At the completion of this comprehensive follow-up session, we will have:

### Documentation Deliverables:
1. **Receiving & Warehouse Management Procedure** - Bin structure, Advanced Receiving workflow, vendor notifications
2. **Vendor Center Contractor Portal Guide** - Access setup, communication workflow, adoption plan
3. **VRA & Damaged Product Management Procedure** - Step-by-step for each scenario, credit tracking, reporting
4. **Work Order Configuration Specification** - Event types, soft scheduling, creation process (if decided yes)
5. **Time Tracking & Rate Configuration** - Complete rate matrices, contractor reconciliation workflow
6. **15% Labor Markup Business Rules** - Complete exception logic, testing scenarios, training
7. **Field Service App Implementation Plan** - Floor plan setup, punch workflow, status reports, training
8. **Scheduling & Resource Management Plan** - (From additional session) Approach to PM/account manager workload
9. **Operations Training & Change Management Plan** - Field app adoption, contractor training, support model

### Decisions Finalized:
- [ ] Work order implementation decided
- [ ] Scheduling/resource management sophistication level decided (via additional session)
- [ ] Advanced Receiving and vendor center rollout timing decided
- [ ] 15% labor markup exception logic complete
- [ ] Contractor direct receiving Phase 2 decision made (probably defer)

### Requirements Confirmed:
- [ ] Warehouse location list complete
- [ ] Contractor access list finalized
- [ ] All time tracking rates documented
- [ ] Work order event types defined
- [ ] 15% markup exception logic complete
- [ ] Floor plan and punch item types specified
- [ ] Advanced Receiving demo confirmed

### Implementation Impact Assessed:
- [ ] Custom development scope identified (Advanced Receiving, field service customizations)
- [ ] Orion feature requirements identified
- [ ] User training requirements by role
- [ ] Change management risks identified with mitigation plans
- [ ] Contractor adoption risks and support needs
- [ ] Equipment/infrastructure needs (iPads, etc.)

---

## PART 6: NEXT STEPS AFTER SESSION

Once this comprehensive follow-up session is complete (plus additional scheduling/resource management session):

1. **Update BRD** - Incorporate all clarifications and decisions into Business Requirements Document
2. **Finalize Operational Procedures** - Document complete workflows for all operational processes
3. **Complete 15% Labor Markup Configuration** - Get exception logic from Kipp, configure in NetSuite
4. **Complete Rate Matrix Configuration** - Set up all PM and design rates
5. **Design VRA Reporting** - End-of-month credit reports configured
6. **Configure Work Order Events** - If decided yes, set up all event types
7. **Plan Advanced Receiving Demo** - Schedule full operations suite demo for team
8. **Begin Contractor Outreach** - Start communication about vendor center and changes
9. **Develop Training Materials** - Create guides for field app, work orders, vendor center
10. **Schedule Operations Suite Demo** - Hands-on walkthrough of Advanced Receiving, Field Service, Work Orders
11. **Plan Training Sessions** - Confirm dates and participants for field app and contractor portal training

---

## APPENDIX: REFERENCE MATERIALS

### Related Documents:
- **Questionnaire_Operations_v1.0.md** - Comprehensive questionnaire with 34 requirements
- **Requirements_Map_Operations_v1.0.md** - Requirements classified by implementation approach
- **Master_Transcript_Operations.md** - Full transcript from discovery sessions
- **GapAnalysis_Operations.md** - Gap analysis from discovery

### Key Requirements Requiring Follow-Up:
- **REQ-002**: Advanced Receiving tool implementation - TOPIC 1
- **REQ-006-009**: Vendor Center contractor portal - TOPIC 2
- **REQ-010-012**: VRA and damaged product management - TOPIC 3
- **REQ-013-015**: Work order management - TOPIC 4
- **REQ-016-020**: Time tracking and rates - TOPIC 5
- **REQ-021-023**: 15% labor markup configuration - TOPIC 6
- **REQ-024-031**: Punch list and field service app - TOPIC 7
- **REQ-032-034**: Scheduling and resource management - TOPIC 8

### Contact Information:
- **Primary Contact:** Wendy (PM Manager/Operations Manager)
- **Technical Contact:** Kipp (IT/Business Rules)
- **Financial Contact:** Lorraine (CFO) - VRA, labor impacts
- **Account Manager Perspective:** Kimmy (Pre-Quote/Account Manager Lead)
- **Contractor Coordination:** Rafina (Design Manager)
- **GSI Lead:** Marcus (Implementation Lead)

---

**Document Version:** 1.0  
**Created:** October 2025  
**Status:** Ready for comprehensive single session scheduling + additional session on Scheduling/Resource Management

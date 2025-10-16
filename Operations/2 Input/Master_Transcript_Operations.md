# MASTER TRANSCRIPT: OPERATIONS
## KBM Hoag NetSuite Orion Implementation

**Sources Combined:**
- 07-31 Workshop_ NetSuite Operations Implementation — Advanced Receiving, Vendor Center, VRA, Work Orders, Scheduling, Field Service, Reporting, and Data Migration.txt (July 31, 2025)

**Date Range:** July 2025
**Business Process:** Operations (Receiving, Work Orders, Scheduling, Field Service, VRAs, Time Tracking, Punch List)

---

## EXECUTIVE SUMMARY

Operations at KBM Hoag encompasses purchase requisitions through punch completion, with a unique operational model where most installation work is outsourced to third-party contractors while the company maintains project oversight through PMs. The current challenge is managing operations across multiple third-party warehouses and installation partners without direct control, requiring communication via email and manual tracking. NetSuite/Orion will enable automated receiving workflows through Advanced Receiving tool (drag-and-drop bins), vendor center portal for contractor communication, work order management for installation oversight, field service app for PMs and contractors, punch list management replacing PlanGrid, and time tracking integrated to project GP.

**Key Themes:**
- Outsourced installation model (third-party warehouses and installers)
- Advanced Receiving tool (drag-and-drop to bins)
- Vendor center for contractor access (no additional license cost)
- Work orders (soft scheduling to installation partners)
- Field service app (replaces PlanGrid, works offline)
- VRA process for damaged product tracking
- PM resource scheduling and site verification
- 15% labor markup automation (cost-only line)
- Time tracking impact on project GP

---

## OPERATIONS SCOPE

### Broad Definition

**Marcus:**
"We do kind of consider operations going all the way back to site analysis, labor quote requests, and things like that. It feels like that kind of is part of the thread all the way through."

**Session Focus:**
"For our purposes today, we're really kind of just looking at purchase requisitions through punch completion."

### Process Flow

1. Purchase Requisitions
2. Receiving (third-party warehouses)
3. Scheduling & Resource Management (PM assignments)
4. Work Order Management (installation oversight)
5. Vendor Return Management (VRAs for damaged product)
6. Time Tracking (PM and design hours)
7. Punch List & Issue Management (field app)
8. Field Operations (contractor coordination)
9. Vendor Center (portal access)

---

## PURCHASE REQUISITIONS

### Decision Made

**Quote:**
"We made the decision yesterday we'll be using purchase requisitions."

### Functionality

**NetSuite Native:**
- Employee submits purchase requisition
- Requires supervisor approval
- Once approved: Converts to purchase order automatically
- All information transfers (no re-keying)

**Use Cases:**
- Team members request purchases
- Routes to appropriate approver
- Controlled purchasing process

**Benefits:**
- Approval workflow automation
- Audit trail
- Budget control
- Authorized purchasing only

---

## RECEIVING & WAREHOUSE MANAGEMENT

### Current Challenge

**Outsourced Model:**
- Not doing own installation
- Third-party warehouses receive product
- No direct visibility to receiving status
- Currently: Email communication from contractors
- Must still track receiving for WIP impact

**Why Receiving Still Necessary:**
"Receiving is what impacts your WIP. So we still want to do that."

### Advanced Receiving Tool

**Orion Innovation:**
"Traditionally, in NetSuite, receiving is actually kind of clunky, it's kind of difficult to do, so we built this tool, this utility that sits on top of it."

**Functionality:**
- Drag and drop interface
- "Here's all my items, here's all my bins, and I can grab items and I can just drag them to the bin and that's it, now they're received"
- Tablet/desktop compatible
- Part of Orion (not NetSuite standard)

**Screenshots:**
- Marcus requested Chris pull up Advanced Receiving screenshots
- Wendy requested access to preview
- Links available in Lux1/Lux2

### Bin Structure

**Definition:**
"Bins are really just locations on a shelf, or locations in a warehouse, or you can have one bin for one warehouse."

**Sophistication Range:**
- Simple: One bin per warehouse location
- Complex: Some dealers have 8,000+ bin locations

**KBM Hoag Approach:**
"I think you're probably gonna have, here's our location, that's the warehouse that it's being shipped to, there's only one bin at that location, because you don't care where it's being tracked there."

**Bin Types Needed:**

1. **Normal Receiving Bin** (per third-party warehouse)
   - Standard product receiving
   - One per installation partner location

2. **Damaged Inventory Bin** (per location)
   - Quarantine damaged product
   - Cannot be accidentally allocated to orders
   - Prevents damaged items shipping out
   - Triggers VRA process

3. **Duplicate Inventory / Overages Bin** (per location)
   - Excess product
   - Duplicate shipments
   - Not allocated to specific orders

**Direct-to-Site:**
- No receiving bin needed
- Mark as shipped
- Track shipping timing only
- No WIP impact

**Office/Showroom Deliveries:**
- May need bin for office location
- Showroom may need receiving bin
- Sometimes product ships to Kipp's house (takes to job site)

**Bin Transfers:**
- Can transfer from one bin to another (bin transfer)
- Can transfer from one location to another (transfer order)
- Sophisticated WMS functionality available

**Example Scenario:**
"There's chairs in San Jose that we're paying storage on that were from a client. And the client didn't want them or something now, so they're sitting on 32 chairs."

---

## VENDOR CENTER (CONTRACTOR PORTAL)

### Purpose

**Marcus:**
"The vendor center, which I think is gonna be really important for you guys, that's just a place for your vendors to log in, including your subcontractors."

### Access Scope

**What Contractors Can See:**
- Purchase orders
- Work orders
- Project information
- Communication tools

**No Additional Cost:**
"There's no additional cost for the field service app. Don't tell them that's why we did that. Usually you charge a license for each one. What we did is, we use one license for everybody. So no matter how many reps you have, it's just gonna cost you one license."

### Receiving Notification

**Current Process:**
- Email from contractor to receiving@KBM
- "They're sending it via email over to receiving at KBM call"

**Future Process (Vendor Center):**
"We are putting in a feature that allows your vendor, or your subcontractor, to notify you that they've received it, right from inside the vendor center."

**Workflow:**
1. Contractor logs into vendor center
2. Sees all their work and incoming POs
3. Product arrives at their warehouse
4. Click "Notify of Arrival" on PO
5. Shows up in KBM Hoag dashboard (not email)
6. KBM team goes to PO and receives it
7. Done

**Can Attach Documents:**
- Contractor can attach files to notification
- Photos of product received
- Documentation

**Optional:**
- Can continue email process if preferred
- Vendor center is optional convenience

### Contractor Direct Receiving

**Considered Approach:**
- Give contractors ability to do full receiving in NetSuite
- Mark items received directly

**Concerns:**

**Example Scenario:**
"You have 200 lines on the PO, they receive all 200. And then like, oh, crap, I shouldn't have done all of them. There's a couple that didn't actually come. Now I need to go back and edit that."

**Permission Creep:**
- Edit capability needed to fix mistakes
- Could mess up other POs if not careful
- No oversight on contractor's end
- Trust level varies by contractor

**Current Decision:**
"So I'm not saying it's not doable. It's absolutely doable. It just really comes down to how much trust you have in them. And you're probably still going to need..."

"For now, they can just get as received. Yep. And it'll show up on our report."

**Future Option:**
- Can revisit later
- "If it's not part of it now, it is in the future. We can always look at that later."

### Communication & Notes

**Current Process (Email):**
- Contractor emails issues/punch items
- Easy to get lost
- No centralized tracking

**Vendor Center Solution:**
"We can give them just the ability to communicate notes, and instead of them typing in the email, they can upload the files and have a comment section where they can communicate some of that info."

**Punch/Damage Communication:**
- Concealed damage discovered at receiving
- Box looks good but product inside damaged
- Currently: "That's when we find out that there's [damage]"

**Punch vs. Damage:**
- Team calls it "concealed damage" or "pre-punch"
- It's a non-bill (claim submission needed)
- PC level handles typically
- "It comes into us as a punch"

**Design Decision:**
"We can kind of think about how to handle that, because we have... when it comes time, we can design whether it's going to be an issue that you track or a punch that you track, and we'll just make sure that we give them the ability to communicate it."

**Communication Options:**
- Email (current)
- Through vendor portal (new)

---

## VENDOR RETURN AUTHORIZATIONS (VRAs)

### Current Damage Process

**Scenario:**
- Product arrives damaged
- Must receive it anyway (WIP impact needed)
- Reach out to vendor for replacement/credit

**Quote:**
"So if something comes in damage, do you typically receive it and then ask for a bill credit from your vendor? Correct."

### Replacement Process

**Adding Lines:**
"It generally ends up that we're adding another line to get that replacement. Because they want you to send a new PO? No, because we need a new line to receive a new piece because we've already seen it."

**New Line Details:**
- Zero-cost line for replacement
- Receive replacement on new line
- Original line stays (damaged, in damaged bin)

### Return Shipping

**Frequency:**
- 90% of time: Vendor doesn't want it back
- 10% of time: Must ship back

**Quote:**
"Sometimes, depending on what it is, sometimes they want it back. Probably 90% of the time they do not. It's not worthwhile shipping them."

**Shipping Method (when needed):**
- FedEx or UPS
- "It depends on when the carrier will come and pick it up"
- All case-by-case
- Based on size and carrier availability

### VRA Process (NetSuite)

**Full Process:**
1. Create VRA (Vendor Return Authorization)
2. Create Item Fulfillment (shipping it back)
3. Vendor confirms receipt
4. Vendor issues credit memo number
5. Create Bill Credit in NetSuite (with vendor's number)
6. Full traceability

**Quote:**
"So there's like all that traceability. It's all very streamlined."

### Tracking Challenge (Lorraine)

**Current Problem:**
"One thing that's always kind of nagged me is that people will enter lines for credits that we're expecting. And then they just kind of, there's not really a way to track it. To make sure that we ever get that credit."

**Lack of Follow-Up:**
"So they just kind of go in there and you're just like throwing it out there. I hope we get this. And then no one ever really follows up on it. So if that would facilitate helping us to track this and to know, hey, where's that $5,000 credit... that we were promised three months ago."

### Marcus's Vendor Pressure Tactic

**Proactive Credit Tracking:**
"This is something that I used to do is because vendors are not prioritizing your credits. So whether you're generating the VRA and sending it back or whatever, there were times where I would be like, I'm just going to create this credit and the number on it is TBD."

**End-of-Month Report:**
"And then at the end of the month, I would send a report of all that to the vendor and say, hey, just so you know, here's all the vendor credits and here's the reason why. And we're expecting your number, but if not, we're just going to apply them to invoices in the next month."

**Results:**
- "That gets their attention and then you get the credit memo number"
- "Or you just apply it and then they get pissed off because now you're paying stuff with credit"
- "Then you're like kind of putting the onus on them. Now they have to do all the forensic accounting on their end to figure it all out."

### Modified VRA Process for KBM Hoag

**Decision:**
Use VRA even when not shipping back (80% of cases)

**Benefits:**
- Traceability of why credit deserved
- Notes on VRA explain reason
- Can justify credit with vendor
- Create bill credit from VRA
- Close VRA (indicates not shipping back)
- Track all expected credits
- Follow up systematically

**Quote (Decision):**
"We'll use the VRA item fulfillment bill credit process... Let's say 80% of the time they're not getting shipped back it's an 80-20 rule, but we could still use the VRA to track the reasons."

---

## DAMAGED PRODUCT BINS

### Why Separate Bin

**Marcus:**
"We need to [receive] it somewhere where somebody can't accidentally inside the system allocate it to an item fulfillment so it gets shipped out."

### Bin Strategy

**Per Third-Party Warehouse:**
1. Normal receiving bin
2. Damaged product bin
3. Duplicate/overage bin (if needed)

### Receiving Process with Damage

**Example:**
- 10 items on PO
- 8 items good condition
- 2 items damaged (told by contractor)

**Receiving:**
- Drag/drop 8 items to normal bin
- Drag/drop 2 items to damaged bin
- Now have traceability: What's damaged, where it's at, needs VRA

### Contractor Receiving Benefit

**Marcus:**
"Another reason why it might be good for you guys to do the receiving and not your contractors."

**Why:**
- Contractor tells you which items damaged
- You control bin assignment
- Prevent damaged items from being allocated
- Track VRA needs

### Write-Off Process

**Lorraine's Question:**
"What you do from a write-off perspective, that product that's being damaged?"

**Complexity:**
- Damaged item in bin at cost
- New PO line at zero cost receives replacement
- Replacement has value but zero cost in system
- "This is where it gets a little bit tricky"

**Decision:**
"Let's come back to that, won't put a pin [in] that one."

**Timing Factor:**
- If resolved same accounting period: No big deal
- Product eventually goes out anyway
- Timing reconciliation needed

---

## SCHEDULING & RESOURCE MANAGEMENT

### Current Process

**Resource Assignment Timing:**
- Designer assigned early
- Other resources trickle in
- PM assigned very late in process

**Desired Change:**
- "We're trying to change that, where the PM gets assigned at the same time as the designer gets assigned"

### PM Dashboard Needs (Wendy)

**Current Challenge:**
"I can think about the PM dashboard, like what the workload is for the PMs. Could that be used in that sort? So then we know."

**Current Method:**
- Look at dates in project
- See all PMs and their projects
- Determine who's available by timeframe

**Quote (Wendy):**
"If I need a PM for something, the first thing I do is go into the project and have all the PMs [projects] they're working on, the dates, and I'll see like who's available for that time."

### Scheduling Tool Capabilities

**Work Orders for PM Scheduling:**
Can schedule PM to be on-site during delivery/install

**Current Request Process:**
"Right now, they just threw an email."

**Potential Improvement:**
"If we actually, like, put the information on the [work order]... And we're like, hey, I need a site verification... [PM] wouldn't have to take the email and then go find the files and drive and so on. The location information is all there."

### Soft Scheduling Concept

**Concern:**
"My fear is, is that people will just start slinging stuff on their schedule and they're going to be like, yeah."

**Solution:**
- Request scheduling (not hard schedule)
- PM must approve
- Similar to soft-scheduling installation jobs

**Quote:**
"Could you soft-schedule them the same way you would soft-schedule a job."

### PM Task List Concept (Wendy)

**Vision:**
"What I'm hoping for is on every project, when you get assigned as project manager, you're going to get a list of tasks, which are always going to include site verification, delivery, walkthrough, all these different things."

**Benefit:**
- PM knows what needs to be done
- Can self-schedule tasks
- If task not completed: Someone knows it needs scheduling

### Calendar View Needs

**Current Tool (Google Sheets):**
- Wendy maintains PM workload calendar
- Shows project timelines by PM
- Shows install dates (bars on timeline)
- Scrolls to current week
- Identifies who has open space

**Challenges:**
- Manual updates required
- "It's only as accurate as the information"
- "Have they updated it, or is it standard?"
- Not accurate by time accessed

**Screenshot Shown:**
- Horizontal timeline
- Projects as rows
- PMs as sections
- Install dates highlighted
- Scrollable by week

**Use Cases:**
- Assign last-minute requests
- See who's available
- Manager view of all PM workloads
- One-on-one review tool
  - "I do also pull this up during my one-on-ones with the PMs and just kind of go through each project"

### NetSuite Solutions

**Design Boards (Card System):**
- Visually shows workload
- Move cards through statuses
- Used for designers currently

**For PMs:**
- Similar card system possible
- Don't move through statuses (different workflow)
- Need calendar view of install days

**Manager Visibility:**
"For reporting, you know, for your sake... it's been a historical struggle with us with resources. They're just not great visibility into it."

**PM Resource Reports:**
- Who's assigned to what projects
- Where projects are in process
- Dashboard visibility
- One-on-one review tool

### Account Manager Resource Needs (Kimmy)

**Pre-Quote Phase Tracking:**
"I was envisioning pre-booking, non-financial impact part, like the resource management, using those, perhaps it's the card, same as design, but the account managers need a similar tool."

**Current State:**
"Right now it looks like that, and I don't want it to look like that. Every department is basically in a Google Sheet."

**Integration Need:**
"They're all connected, and we utilize the same resources, it's just ours happens before any of the design, before the PC, before the VM, and it'd be great to track it from the opportunity, all the way to the end."

**Saved Search Solution:**
- Who's assigned to what
- What their role is
- Where project is in process

**Card View Needs:**
- Weighted by volume
- Show project phase
- Timeline visibility

**Challenge:**
- "We haven't run into a dealer who wants to go that far with it"
- Had built resource visualizer tool, but no dealer interest
- Easier with team-based dealers

### Project Management Software Evaluation

**Asana Consideration:**
"I've held off on rolling out a project management software until I fully understand what NetSuite's going to offer. So it's like, is NetSuite going to do it, or do I need to tackle the Asana build simultaneously?"

**Marcus Response:**
"I would hope not. We just haven't run into a dealer who wants to go that far with it."

**Why Dealers Resist:**
"It's easier to identify your resources when they're team-based. Yeah."

**Asana Already in Use:**
- HR and marketing use small version
- Assigns resources to tasks

**Asana Challenge:**
"The hardest part about Asana is actually just building out the task. You have to think of all the things you have to type in. All the little itty-bitty things that happen."

### Task Detail Levels (Matt)

**Question:**
"If they're going to build us something, Kimmy, we have to decide, is it the 10 phases or is it the 300 things that happen in each one of those phases? So 300 times 10."

**Management Perspective:**
"I don't want to manage all of that. That's the account manager's job to manage the individual details."

**Manager Need:**
"From a manager perspective, like Wendy wanting to assign a PM, I want to know what phase of project they're at, the volume of those projects, and the timeline of those projects so that you know when they're breathing from the new programming for another opportunity."

**Challenge:**
- Project might be in phase, but account manager not
- "The order's there, but the person's not. They're behind."
- How to show someone is behind?

**PM Management (Wendy):**
"For PMs, I don't want to micro them, but I also want what the always are. And I want an acknowledgement sign off that they were done."

### Suite Projects (NetSuite Native)

**Functionality:**
- Project record
- Task templates
- Resource assignment
- Skills matrix
- Native NetSuite project management

**Marcus:**
"We're familiar with all of that. We just haven't run into dealers that want to use it."

**Wendy's Reaction:**
"It's so fascinating. I mean, we're literally, industry is project and budget management. And people don't want to use it. I know. What?"

**Why Dealers Don't Use:**
- Ohio dealer example: Lower costs, higher prices, less need for detail
- "Throwing five more bodies onto a project is no big deal because it's on the property"
- Regional differences in margin pressure

### Task Dependencies (Asana-Style)

**Kimmy:**
"At Asana, when you complete a task, they're going to queue the next thing. And if that next thing is assigned to someone else, then they know now it's ready for them to go. Or it can be moved to them."

**Workflow Vision:**
"I just like the idea of like this workflow where if you're waiting for someone, you know that you're waiting for someone else until it's your time to step up to play."

**Task Dependencies & Constraints:**
"So like the task dependencies and all that constraints. So yeah, like we kind of come from that world."

**Dealer Resistance:**
"Every time we've proposed it to dealers, it was a little bit too much. They wanted more flexibility than that type of stringent project management."

### Project Setup Flexibility

**Need:**
- Core task list
- Part of project setup: Does this apply or not?
- Remove tasks that don't apply
- Add additional tasks as needed
- Editable per project

**Marcus:**
"It's like everybody knows exactly what they're supposed to be doing. This is what they're supposed to be doing."

**Challenge with System Tasks:**
"There are things that you do in the system that the system knows that you did. So then what they ended up having was, well, here's a task to tell you to go do it. I went and did it, and now I'm going to go back and tell the same system that I did it."

**Solution:**
"The task can kind of be woven through the process rather than it has to kind of be like... it gets just tedious to keep going back to the same system and say I did that work when the system already knows that you did it."

### Employee Pushback

**Quote:**
"We obviously have non-process-driven people within our organization as well. Their pushback usually is, well, you hired me to do the job. Trust me to do the job. I don't need a list to tell me what my job is."

**Counter-Argument:**
"When we're busy, things can get lost."

### Unlimited PTO

**Side Note:**
"We have unlimited PTO, and they go in the future."

### Action Item

**Decision:**
"We'll definitely come back to that. So scheduling and resourcing... we'll have another session where we go a little bit deeper on this."

**Questions to Answer:**
- Asana-style workflow?
- Task dependencies?
- Level of detail needed?
- Manager vs. individual contributor views?
- Resource visualizer needs?

---

## WORK ORDER MANAGEMENT

### Decision Status

**Not Finalized:**
"I don't think we've made the hard decision that we're going to use them. It keeps coming up."

**Wendy's Buy-In:**
"Wendy signed on for work orders just now, so that was good. That's like mission accomplished."

### Sophistication Levels

**Marcus:**
"The one thing I just want you to know about work order management is it can be as easy or sophisticated as you want it to be."

**Simple Approach:**
- Go to sales order
- Generate work order
- Don't have to pick any lines
- Choose event type
- Save it (soft scheduled)
- Done

### Work Order Events

**Event Types:**
- Site verification
- Delivery and install
- Site review
- PM on-site presence
- Design meetings
- Punch walks

**Resource Assignment:**
- PM can be resource on work order
- PM sees event in Field Service app
- Shows on appropriate calendar day
- Can self-schedule

---

## TIME TRACKING & PROJECT MANAGEMENT

### Confirmation

**GL Impact:**
- "Time tracking has no GL impact" (confirmed)
- Does have GP impact on project
- Affects project profitability

### Rate Structure

**PM Rates:**
- Flat rate (not hourly)
- Internal rate (cost)
- External rate (client billing)

**Design Rates:**
- Flat rate
- Two different internal costs:
  - Workshop designer (lower internal hourly rate)
  - Standard designer
- Field designers different from studio

**Quote (Wendy):**
"So there's a design client rate and a PM client rate, and then there's basically three internal rates."

**Billable vs. Non-Billable:**
- Tracked on time entry
- Determine if billable to project or G&A
- "They're either billable or non-billable. And right now they're on the quarter."

### Contracted Rates

**Negotiated Client Rates:**
- Some clients have negotiated PM/design rates
- Sell rate varies by client contract
- Internal cost stays same regardless
- "The internal doesn't change"

### External Contractors (Blue River)

**Quote:**
"And the Blue River. And the outside contractors. The outside contractors doesn't matter. The internal rate has stayed the same even if their hourly rate is more. That is a, we're understaffed, and so therefore KBM Hoag takes the hit."

**Implication:**
- External contractor may charge $95/hour
- KBM internal rate is $85/hour
- Only bill project at $85
- KBM absorbs difference
- "So that's why I try not to book Kimiko at $95 an hour"

**Billing:**
- External contractor time billed as "consulting"
- Not true job cost in that sense

### Tracking Frequency

**Ideal:**
- Weekly time tracking

**Reality:**
- "They have to be slapped around a little bit"
- "Sometimes. I know. And I get it. The time tracking is a pain in the butt."

### Rate Matrix

**Configuration:**
- Rate matrix to be filled out
- Part of configuration setup
- KBM has only a handful of rates
- "Should be pretty easy"

**Calculation:**
- Time tracked → calculates cost based on rate matrix
- Cost pulled into project
- Affects project GP

### Transcript Statement

**Marcus:**
"I just want to say it out loud, again, for the sake of the transcript, because not all dealers do it this way. We do want that time to impact the GP. Yes."

---

## EXTERNAL VENDOR BILLS & TIME

### Vendor Bill Structure

**Question:**
One bill per project, or one bill with multiple projects itemized?

**Answer:**
- "One-to-one ratio of bills, vendor bills, to POs"
- Don't tag to project from vendor bill

### Contractor Time Entry

**Some Contractors:**
- Have Core time-entry access
- Can log own time into KBM system
- "Some of our contractors, they have core time-entry access, because we can give them access to just time-entry."

**Process:**
1. Contractor logs time directly
2. Rafina (Design Manager) reconciles
3. Compare time entered to invoice received
4. Ensure matching

### Contractors Without Time Entry

**Process:**
- Pay invoice as "consulting" (GL code)
- No job impact from invoice
- Rafina manually enters time at standard rates
- Time (not invoice) impacts GP

**Example:**
- Contractor charges $99/hour
- KBM internal rate is $85/hour
- Only bill job at $85
- "Because it's just a GP"

### Design GP Impact

**Decision:**
"Whatever the cost, the selling cost that was put on the sales order for design, that's what hits the GP."

**Reality Check (Matt):**
"I'll state for the record, we lose money on design. Design does not make money. No matter how much design we bill, our payroll costs more than what we were able to bill to a client at any point."

**Result:**
"So we don't hold them [to GP]. Otherwise, we'd have to put a negative GP on every order."

### External Design Vendors

**PO Issued?**
- No PO for external design

**How Billed:**
- "They just bill us, and it comes through as a... GNA expense, consulting expense"
- Not tagged to project
- No project GP impact

**Exception:**
- "There are times where we will tag something to a project"
- If end up doing [labor/install] and not design
- Then: Line added, new PO issued for that line
- Cost of PO flows back to project and impacts GP

### General Rule (Kipp)

**Quote:**
"In general, everything that is job-costed is going to be tagged to a PO, with the exception of design... Labor, PO. Storage, we issue a PO. Our copy suit, we issue a PO. Everything."

**Benefit:**
"I mean, that just helps us because it's like a one-on-one ratio."

---

## 15% LABOR MARKUP (FORMULA LINE)

### The Practice

**Unique but Not Alone:**
- "That's the weirdest thing that we do that I don't think any other dealer does"
- "You're not the only one doing that"

**How It Works:**
"Every time you start a new order, it automatically pulls in a line that says KPMG 15%. And that line auto-calculates any time there's a labor line. It takes 15% of the GP and adjusts the whole GP."

**Details:**
- Cost-only line (no revenue)
- Auto-calculates 15% of cost of all labor
- No GL impact
- Does decrease GP
- Core has business rule formula

### What Labor Counts

**External Labor Only:**
- Not all labor, just external (warehouse/install) labor
- Line code identifies external labor
- Formula looks at line code: "Oh any line that has that I'm going to calculate"

**NetSuite Solution:**
- Formula lines capability exists
- Can replicate Core business rule
- "There's a way to put this into the code or the native way to do this in NetSuite"

### Line Number Issue (Kipp's OCD)

**Problem:**
"My biggest gripe about that is that it's always line one. So any time you issue a proposal with line numbers it starts at two."

**Impact:**
- Doesn't print on customer proposal
- Messes up line numbers
- Line 1 is blank on proposal (starts at line 2)
- Big bold on internal view

**Can Move Manually:**
- "Now you can move it all the way up until you open that order but nobody does it"
- Requires someone to care enough to click button
- Nobody with OCD awareness does it

**Kipp's Wish List:**
1. Need the line (most important)
2. Always at bottom (not top)
3. Uneditable
4. Not printing
5. Always dynamic

**Marcus:**
"Okay, so there is an override but that's why I'm not..."

### Purpose & History

**Behavioral Change:**
"So this is something really is to guard and ensure that there's some level of profitability on the order."

**Background (Matt):**
- Used to have warehouse
- Forklift incident with drinking
- OSHA environment decided against
- "We decided we didn't want to be in an OSHA environment anymore"

**Goal:**
"To get people to mark up what labor should be, it's supposed to be like stop marking up labor at the same as product. You need to be like marking up product higher. So we forced our markup by taking a hit against it."

**Strategy:**
- "It's a behavioral push"
- Forces higher markup on labor
- Safety margin for labor unpredictability

### Logic & Exceptions

**Applies To:**
- All orders that have labor

**Exceptions:**
- Some clients have exceptions
- Order type based exceptions possible
- Client based exceptions possible

**Business Rule Logic:**
- Can be automated if logic laid out
- Must define full logical expression
- Natural language acceptable

**Action Item:**
Kipp to provide:
- 15% labor markup logic
- All exceptions
- Current Core rules

**Quote (Marcus):**
"But it's based off of order type, not based off of client. You could add in additional exceptions by client if you wanted to as well. So there's a few ways to do it. I just need to know, like, that full logical expression."

### Industry Comparison

**Quote (Marcus):**
"The only unique thing there is you're doing it on labor. A lot of people doing on product. Are they not billing hourly for services? They are. They're doing on time."

---

## PUNCH LIST & ISSUE MANAGEMENT

### Issue Types (Generic Term)

**Quote:**
"We kind of have this generic term called issues and punch lists. Punch is one of the issue types. And there's a bunch of other issue types."

**Examples:**
- Punch list items
- Bill price discrepancies
- Acknowledgement discrepancies
- Warehouse damage
- "Something that's wrong we wanna track"

### Current Tool: PlanGrid

**Quote:**
"So who's doing the punch list? Is that your subcontractors or your PMs?"

**Answer:**
PMs doing punch lists, using PlanGrid currently

### Orion Replacement

**Built into Field Service App:**
"We've built specific functionality into the field service app and into the work order application to replace [PlanGrid], so you don't have to use... Plan grid."

**Goal:**
"One last thing to pay for. That's what we're going for."

**Installation Partners Can Access:**
"And our installation partners can give [access]. Because is it work order driven? It's all work order driven."

### Requirements

**Work Order Driven:**
- Must be resource on work order or work order event
- If PM is resource: Can create punch
- "As long as the PM is a resource on the work order, they will"

**Projects Without Work Orders:**
"There's projects without it."

**Solution:**
"You just have to be a resource on the work order or the work order event"

### Punch Functionality

**How It Works:**
- Take photo
- Punch reasons (what's wrong)
- Punch issues (why it's wrong, who's responsible)
- Associate lines with it (one or multiple)

**Current Process (Core):**
"Right now we can, we enter it through core and we can attach photos, which is nice because then we just go in a line and we don't have to... You only have to do it once."

**Avoiding Double Entry:**
- Currently: Enter in PlanGrid AND Core
- "I still do it in plain grid"

### Floor Plan Marking

**Critical Feature:**
"One of the big things is plain grid is that you can then mark that location on the drawing, correct? Resolving that issue. There's a thing you can do in there."

**Why Important:**
"Four months later you get that punch item and you've done 15 jobs. You're like, yeah, I'll remember what room that goes into. And you don't. We all know the reality there."

**Orion Solution:**
- Floor plan functionality built-in
- Pin punch to location on drawing
- Visual reference months later

### Offline Mode

**Field Service App:**
"The app works in offline mode as well."

**Workflow:**
1. Log in in morning
2. Download all work event information
3. Go into building (no internet)
4. Do all work
5. Take pictures
6. Create punch
7. Sync when back online

**Quote:**
"You download all your work event information, you go into a building with no internet connectivity, you can still do all your work, take pictures, create punch, and then it'll sync when you..."

### Daily/Weekly Status Reports

**Current PlanGrid Feature:**
- Generate report on iPad
- Email from PlanGrid
- PM in field initiates and sends

**Orion Current State:**
- Can generate report in back-end NetSuite
- Reports easier to create in NetSuite desktop
- "We don't have it in the app yet"

**Challenge:**
- "Someone using the app to generate and send that [report]?"
- Would have to log into desktop NetSuite to email report
- "Two different locations"

**Who Creates Report:**
- "Sometimes it's me, and sometimes it's them" (Wendy)

**Decision:**
"Generating it in the app is not going to be a challenge for us to do. We just weren't planning on it, but we can."

**Prioritization:**
- Project to Orion
- Not high priority but doable

### Report Polish

**Consideration:**
- Field notes during punch walk not polished
- "General notes, but it's not going to be, like, a polished report that you want to send out to a client"
- Typing while walking, people interrupting
- Cannot do time entry and punch report simultaneously

### Action Item

**Demo Requested:**
- Show PlanGrid replacement functionality
- Floor plan punch pinning
- Preview of operations suite

---

## FIELD SERVICE APP

### Demo Attempted

**Late Session:**
- Tried to show Field Service app
- Logged in as Dennis (developer)
- Older version in demo account
- Limited functionality shown

**Rescheduled:**
"Let's schedule a session to do a preview of the whole operations suite, especially since it's new... receiving, work order, scheduling, dispatching, and field service."

### Design

**Platform:**
- Tablet primary
- Mobile phone responsive
- Works on both

### Dashboard View

**Cards:**
- Each card = work order event
- Multiple events possible per project
- Filtered by date (today's work)
- PMs/subcontractors see only their assignments

**Example:**
- See 2-3 cards per day
- Subcontractors might have couple per day

**Filters:**
- Status
- Date
- Sort options

### Event Detail

**Information Available:**
- Location address (with map link - can navigate)
- Check-in (geologically stamped, confirms on-site)
- Status updates (in process, complete)
- Site requirements (from job site analysis)
- Contact info
- Resource assignments

**Check-In Feature:**
"Is it geologically confirmed that you're actually on site when you're checking? Yeah, stamp set."

**Complete:**
- Complete all lines on event
- Mark event done

### Items Tab

**Line Item Management:**
- See all products on work order
- Mark items in progress or completed
- May be locked (older version shown)
- Not heavily used by KBM (outsourced installation)

**Possible Use:**
- Installation partners might want line item detail
- Track completion by item

### Time Tracking

**Multi-Resource:**
- If five resources on event: Fill in time once, applies to all
- Add temporary resources
- Time entry tied to work order event

**Limitation:**
- Work order event driven only
- No event = no time tracking in app
- Must use desktop NetSuite for non-event time (like design)

**Question Asked:**
"Can the PM in the field on their iPad enter the time that they were doing?"

**Answer:**
- Only if work order event exists
- Design time: Not work order driven, enter in desktop

### Punch List (See Punch Section Above)

**Access:**
- Create punch from details screen
- Create from floor plan (preferred method)
- Photos
- Tasks

### Additional Features

**Shown:**
- Attach files
- Collect signatures
- Initiate change orders
- Document return of product ("Oh, you might? Oh, okay.")

**Marcus:**
- Keeps making assumptions about KBM not needing features
- Then discovers they do need them
- "I'm silly. I keep making assumptions that I shouldn't"

### Updated Version

**Note:**
"This is an older version... some of this stuff is not going to apply to you... this is for our developer... Like I said, this is an older version"

**Action:**
Get updated links from Lux1/Lux2 for latest version

---

## VENDOR CENTER ADDITIONAL DETAILS

### License Cost

**One License for All:**
"No matter how many reps you have, it's just gonna cost you one license."

**Why:**
- Designed purposely for contractors to use
- Not typical NetSuite licensing (usually per user)
- Shared license model
- "Don't tell them that's why we did that"

### Access Control

**Full License Discussion:**
- Considered giving contractors full NetSuite license
- "That would be a full license, yeah"
- More expensive
- More capabilities (and risks)

---

## DATA MIGRATION (Brief Mention)

### Chart of Accounts

**Marcus:**
"I've been spending a lot of time mapping our chart of accounts."

**Lorraine:**
"We'll definitely be walking through and talking through all of that."

**Starting Point:**
- Baseline mapping
- Changes won't affect anything
- Will walk through in separate session

### Historical Data

**Trial Balance Import:**
"Typically it's end-of-the-month trial balances for the past two, five, seven, ten years, whatever you want."

**Chart of Accounts Simplification:**
"Hopefully it will become like two or three pages [from] 40. Now we're at 40 pages."

**Goal:**
"You should be able to get it down to a few hundred, right? Yeah, I think so."

### Dimensions

**NetSuite Structure:**
- Not same as Core geography structure
- Location, geography, account are different dimensions
- "Dimensions. Yeah. Yep. So we just need a dimension for location."

**Marcus:**
"It makes it so much easier."

---

## BUSINESS INTELLIGENCE & REPORTING (PREVIEW)

### Session Transition

**Quote:**
"Not financial management, business intelligence. So NetSuite has the same geo structure, like location, geo account? No, it's just a different channel. Those are different dimensions."

**Moving On:**
"All right, so we are moving on to business intelligence and reporting."

*(Note: Full BI session covered in separate Business Intelligence transcript)*

### Preview Comments

**Marcus:**
"Just to kind of give you the highlights of what's available to you inside NetSuite. So you have these core NetSuite BI tools. They are very powerful."

**Dashboard Philosophy:**
"Dashboards are a very important part of NetSuite. And so we will be building on dashboards kind of for your departments. We've built out some additional components to make those dashboards a little bit so they look a little bit better. Like how things look is actually important to us. We kind of think of NetSuite as kind of the home that you're living in all day. So it should look good. So you feel good about where you're living."

---

## DECISIONS & ACTION ITEMS

### Decisions Made

1. **Purchase Requisitions:** Will use them
2. **Advanced Receiving:** Will use drag-and-drop tool
3. **Bin Structure:** One bin per warehouse, plus damaged and duplicate bins per location
4. **VRA Process:** Will use even when not shipping back (80/20 rule) for credit tracking
5. **Vendor Center:** Will implement for contractor communication
6. **15% Labor Markup:** Will replicate (Kipp to provide logic and exceptions)
7. **Time Tracking:** Will impact project GP
8. **Field Service App:** Will use to replace PlanGrid

### Action Items

1. **Marcus/Chris:** Pull up Advanced Receiving screenshots/demo
2. **Marcus/Chris:** Schedule preview session for entire operations suite (receiving, work orders, scheduling, dispatching, field service)
3. **Kipp:** Provide 15% labor markup logic with all exceptions
4. **Kipp:** Provide rate matrix for PM and design rates
5. **Marcus/Team:** Determine punch vs. issue categorization for damage communication
6. **Marcus/Team:** Design customer PO tracking solution (from Order Management)
7. **Wendy/Kimmy/Team:** Provide examples of status reports from PlanGrid
8. **All:** Separate session on scheduling/resource management needs (Asana-style workflow, task dependencies, resource visualizer)

### Open Questions

1. **Work Orders:** Final decision on usage (soft yes from Wendy)
2. **Contractor Direct Receiving:** Trust level, oversight concerns, future consideration?
3. **Damaged Product Write-Off:** Process when replacement at zero cost received
4. **PM Scheduling:** Hard schedule vs. request/approve workflow
5. **Project Management Sophistication:** How deep to go with Suite Projects, task dependencies, resource management?
6. **Resource Visualization:** Card views, weighted by volume, timeline views - how much to build?
7. **Status Report Generation:** In-app vs. desktop NetSuite - priority?
8. **Task Detail Level:** 10 phases or 300 granular tasks per phase?

---

## QUOTES & INSIGHTS

**On Work Orders:**
"Wendy signed on for work orders just now, so that was good. That's like mission accomplished."

**On Advanced Receiving:**
"We worked really hard to make this as simple as possible for companies like you that are not doing your own installation."

**On Vendor Center Licensing:**
"There's no additional cost for the field service app. Don't tell them that's why we did that. Usually you charge a license for each one. What we did is, we use one license for everybody."

**On VRA Tracking (Lorraine):**
"One thing that's always kind of nagged me is that people will enter lines for credits that we're expecting... I hope we get this. And then no one ever really follows up on it."

**On Marcus's Vendor Pressure:**
"I'm just going to create this credit and the number on it is TBD. And then at the end of the month, I would send a report of all that to the vendor and say, hey, just so you know, here's all the vendor credits and here's the reason why. And we're expecting your number, but if not, we're just going to apply them to invoices in the next month. That gets their attention."

**On 15% Labor Markup History (Matt):**
"We used to have a warehouse. I wasn't here during all this. I don't understand the whole process. But we used to have a warehouse. I think there was a forklift incident with drinking. It happens."

**On Kipp's OCD:**
"My biggest gripe about that is that it's always line one. So any time you issue a proposal with line numbers it starts at two... It's like big bold on the line one and it doesn't print so it just like messes up the line numbers... Somebody with OCD... I will murder this thing."

**On Design GP (Matt):**
"I'll state for the record, we lose money on design. Design does not make money. No matter how much design we bill, our payroll costs more than what we were able to bill to a client at any point."

**On External Contractors:**
"The outside contractors doesn't matter. The internal rate has stayed the same even if their hourly rate is more. That is a, we're understaffed, and so therefore KBM Hoag takes the hit."

**On Time Tracking:**
"They have to be slapped around a little bit. Sometimes. I know. And I get it. The time tracking is a pain in the butt."

**On PlanGrid Replacement:**
"Four months later you get that punch item and you've done 15 jobs. You're like, yeah, I'll remember what room that goes into. And you don't. We all know the reality there."

**On Project Management Software Resistance (Marcus):**
"It's so fascinating. I mean, we're literally, industry is project and budget management. And people don't want to use it. I know. What? They don't want to use it."

**On Process-Driven People:**
"We obviously have non-process-driven people within our organization as well. Their pushback usually is, well, you hired me to do the job. Trust me to do the job. I don't need a list to tell me what my job is. When we're busy, things can get lost."

**On Unlimited PTO:**
"We have unlimited PTO, and they go in the future."

**On Assumptions (Marcus):**
"You might? Oh, okay. Oh, see, I'm silly. I keep making assumptions that I shouldn't."

---

## CHANGE MANAGEMENT CONSIDERATIONS

### Behavior Changes Required

1. **Receiving Process:**
   - From email confirmation → Vendor center notification
   - Trust contractors to notify accurately
   - Drag-and-drop bin assignments
   - Damaged bin discipline

2. **VRA Discipline:**
   - Create VRA even if not shipping back
   - Track all expected credits
   - Follow-up systematically
   - End-of-month vendor reporting

3. **Work Order Adoption:**
   - Create work orders for installation events
   - Soft schedule vs. hard schedule
   - Resource assignment discipline

4. **Field Service App:**
   - PM adoption of tablet app
   - Replace PlanGrid workflow
   - Check-in discipline (geological stamp)
   - Punch creation in field (not back at desk)

5. **Time Tracking:**
   - Weekly time entry (still needs reminders)
   - Tie to work order events when possible
   - Desktop NetSuite for non-event time

6. **PM Assignment Timing:**
   - Assign PM earlier (with designer)
   - Not late in process
   - Enable better scheduling

### Resistance Points

1. **PlanGrid Replacement:**
   - Established workflow
   - Familiar interface
   - Offline mode concerns (addressed: app works offline)
   - Report generation from field (addressed: can build in app)

2. **Work Order "Bureaucracy":**
   - Feels like extra steps
   - Soft scheduling approval workflow
   - New transaction type to manage

3. **Contractor Portal Adoption:**
   - Getting contractors to use new system
   - Training external parties
   - Change management outside KBM control

4. **Time Tracking:**
   - Already a struggle ("slapped around a little bit")
   - Work order event requirement may add friction
   - Or may help (structured around events)

5. **Project Management Sophistication:**
   - "Hired me to do the job, trust me"
   - Feels like micromanagement
   - Task list tedium
   - Different levels of process adherence across team

### Success Factors

1. **Offline Field Service App:**
   - Critical for field work
   - Download in morning, sync at night
   - No connectivity excuses

2. **Replace Paid Tool (PlanGrid):**
   - Cost savings motivation
   - One less system
   - "One last thing to pay for"

3. **One License for All Contractors:**
   - No per-user cost
   - Easy to give access
   - Removes financial barrier

4. **Vendor Pressure Tool (VRAs):**
   - Lorraine's frustration addressed
   - Follow-up visibility
   - Marcus's "TBD credit" tactic

5. **Kipp's OCD Satisfaction:**
   - 15% line at bottom, not top
   - Uneditable
   - Doesn't print
   - Small wins matter

6. **Visual Floor Plans:**
   - Pin punch to location
   - Future reference
   - Addresses real pain point

### Training Focus

1. **Advanced Receiving:**
   - Drag-and-drop mechanics
   - Bin selection (normal vs. damaged vs. duplicate)
   - When to create VRA

2. **Vendor Center:**
   - Contractor login process
   - Notify of arrival workflow
   - Attach documents/photos
   - Communication notes

3. **Work Order Creation:**
   - From sales order
   - Event types
   - Resource assignment
   - Soft scheduling

4. **Field Service App:**
   - Download work in morning
   - Check-in/check-out
   - Punch creation
   - Floor plan pinning
   - Photo attachment
   - Offline mode
   - Sync when online
   - Change orders
   - Signatures

5. **VRA Process:**
   - When to create
   - VRA → Bill Credit workflow
   - Close without shipping
   - End-of-month vendor reporting

6. **15% Labor Markup:**
   - How it works
   - Why it exists
   - Exceptions
   - Cannot override (most cases)

7. **Time Tracking:**
   - Work order event tied
   - Desktop for non-event
   - Weekly discipline
   - Rate application

---

## OPEN QUESTIONS FOR FUTURE SESSIONS

1. **Scheduling & Resource Management Deep Dive:**
   - Asana-style workflow feasibility
   - Task dependencies implementation
   - Resource visualizer design
   - Card view weighted by volume
   - Manager vs. individual views
   - Account manager pre-quote phase tracking
   - 10 phases vs. 300 tasks decision

2. **Suite Projects Evaluation:**
   - Native NetSuite project management
   - Task templates
   - Resource assignment
   - Skills matrix
   - Worth implementing for KBM?

3. **Advanced Receiving Demo:**
   - Live walkthrough
   - Bin assignment workflow
   - Drag-and-drop demonstration
   - Mobile vs. desktop experience

4. **Field Service App Deep Dive:**
   - Latest version demo
   - Floor plan functionality
   - Punch list workflow
   - Offline mode demonstration
   - Change order process
   - Status report generation

5. **Work Order Workflow:**
   - Soft schedule approval process
   - PM task list automation
   - Site verification scheduling
   - Delivery/install coordination

6. **Damaged Product Write-Off:**
   - Accounting treatment
   - Zero-cost replacement line
   - Period-end reconciliation
   - Financial reporting

7. **Contractor Time Entry:**
   - Which contractors get access?
   - Reconciliation workflow (Rafina)
   - Invoice vs. time entry matching
   - Audit trail

8. **15% Labor Markup:**
   - Complete exception logic
   - Order type rules
   - Client exceptions
   - Line positioning solution

9. **Status Report Design:**
   - In-app vs. desktop generation
   - Report content/format
   - Email workflow
   - Client-facing polish

10. **Data Migration:**
    - Chart of accounts final mapping
    - Historical trial balance dates
    - Dimension structure
    - Location setup

---

*End of Master Transcript: Operations*


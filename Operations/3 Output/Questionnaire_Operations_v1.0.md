# Questionnaire - Operations
**Version**: 1.0  
**Date**: October 16, 2025  
**Process Area**: Operations (Receiving, Work Orders, Scheduling, Field Service, VRAs, Time Tracking, Punch List)

## Change Log
- **Date**: October 16, 2025
- **Version**: 1.0
- **Sources**: Master_Transcript_Operations.md
- **Summary**: Initial comprehensive questionnaire analysis completed from Operations master transcript covering purchase requisitions, receiving, vendor center, work orders, field service, VRAs, time tracking, and punch list management for outsourced installation model.

## PROCESSED FILES
- Operations/2 Input/Master_Transcript_Operations.md (1,607 lines)
- Sources: 07-31 Workshop_ NetSuite Operations Implementation — Advanced Receiving, Vendor Center, VRA, Work Orders, Scheduling, Field Service, Reporting, and Data Migration.txt (July 31, 2025)

## Speaker Attribution Map
- **Marcus** = Implementation Team/Consultant
- **Wendy** = PM Manager/Operations Manager
- **Kipp** = IT Specialist/Former Controller
- **Lorraine** = CFO/Controller
- **Matt** = Leadership
- **Kimmy** = Account Manager/Pre-Quote Manager
- **Chris** = Implementation Team

## Decision Log

### Purchase Requisitions
- **REQ-001**: Implement purchase requisition approval workflow (ALIGNS) - "We made the decision yesterday we'll be using purchase requisitions." - Team

### Receiving & Warehouse Management
- **REQ-002**: Implement Advanced Receiving tool with drag-and-drop bin functionality (ACCOMMODATE) - "Traditionally, in NetSuite, receiving is actually kind of clunky, it's kind of difficult to do, so we built this tool, this utility that sits on top of it." - Marcus
- **REQ-003**: Configure one receiving bin per third-party warehouse location (ALIGNS) - "I think you're probably gonna have, here's our location, that's the warehouse that it's being shipped to, there's only one bin at that location, because you don't care where it's being tracked there." - Marcus
- **REQ-004**: Configure damaged inventory bin per location to quarantine damaged product (ALIGNS) - "We need to [receive] it somewhere where somebody can't accidentally inside the system allocate it to an item fulfillment so it gets shipped out." - Marcus
- **REQ-005**: Configure duplicate/overage inventory bin per location (ALIGNS) - "Duplicate Inventory / Overages Bin (per location) - Excess product - Duplicate shipments - Not allocated to specific orders" - Discussion

### Vendor Center (Contractor Portal)
- **REQ-006**: Implement vendor center portal for contractor access at no additional cost (ALIGNS) - "There's no additional cost for the field service app. Don't tell them that's why we did that. Usually you charge a license for each one. What we did is, we use one license for everybody." - Marcus
- **REQ-007**: Enable receiving notification feature in vendor center (ACCOMMODATE) - "We are putting in a feature that allows your vendor, or your subcontractor, to notify you that they've received it, right from inside the vendor center." - Marcus
- **REQ-008**: Defer contractor direct receiving capability to future phase (ADAPT) - "For now, they can just get as received. Yep. And it'll show up on our report... If it's not part of it now, it is in the future. We can always look at that later." - Decision
- **REQ-009**: Enable document attachment and communication in vendor center (ALIGNS) - "We can give them just the ability to communicate notes, and instead of them typing in the email, they can upload the files and have a comment section where they can communicate some of that info." - Marcus

### Vendor Return Authorizations (VRAs)
- **REQ-010**: Use VRA process even when not shipping product back (80/20 rule) for credit tracking (ADAPT) - "We'll use the VRA item fulfillment bill credit process... Let's say 80% of the time they're not getting shipped back it's an 80-20 rule, but we could still use the VRA to track the reasons." - Decision
- **REQ-011**: Configure damaged product replacement as zero-cost line on existing PO (ALIGNS) - "It generally ends up that we're adding another line to get that replacement... Zero-cost line for replacement - Receive replacement on new line" - Process description
- **REQ-012**: Track expected vendor credits with follow-up reporting (ACCOMMODATE) - "One thing that's always kind of nagged me is that people will enter lines for credits that we're expecting. And then they just kind of, there's not really a way to track it." - Lorraine

### Work Order Management
- **REQ-013**: Implement work orders for installation and PM events (soft decision) (ADAPT) - "Wendy signed on for work orders just now, so that was good. That's like mission accomplished." - Marcus
- **REQ-014**: Configure work order event types (site verification, delivery/install, site review, PM on-site, design meetings, punch walks) (ALIGNS) - "Event Types: Site verification - Delivery and install - Site review - PM on-site presence - Design meetings - Punch walks" - Discussion
- **REQ-015**: Enable soft scheduling with PM approval workflow (not hard schedule) (ADAPT) - "Could you soft-schedule them the same way you would soft-schedule a job... Request scheduling (not hard schedule) - PM must approve" - Discussion

### Time Tracking & Project Management
- **REQ-016**: Configure time tracking to impact project GP (not GL) (ALIGNS) - "I just want to say it out loud, again, for the sake of the transcript, because not all dealers do it this way. We do want that time to impact the GP. Yes." - Marcus
- **REQ-017**: Configure PM flat rate structure (internal cost and external billing) (ALIGNS) - "PM Rates: Flat rate (not hourly) - Internal rate (cost) - External rate (client billing)" - Wendy
- **REQ-018**: Configure design rate matrix with workshop vs. standard designer rates (ALIGNS) - "Two different internal costs: Workshop designer (lower internal hourly rate) - Standard designer" - Wendy
- **REQ-019**: Support negotiated client rates with standard internal costs (ALIGNS) - "Some clients have negotiated PM/design rates - Sell rate varies by client contract - Internal cost stays same regardless" - Discussion
- **REQ-020**: Allow external contractor time entry with reconciliation workflow (ALIGNS) - "Some of our contractors, they have core time-entry access, because we can give them access to just time-entry... Rafina (Design Manager) reconciles" - Process description

### 15% Labor Markup (Formula Line)
- **REQ-021**: Implement 15% labor markup formula line (cost-only, no revenue) (ACCOMMODATE) - "Every time you start a new order, it automatically pulls in a line that says KPMG 15%. And that line auto-calculates any time there's a labor line. It takes 15% of the GP and adjusts the whole GP." - Description
- **REQ-022**: Apply markup only to external labor (not all labor types) (ACCOMMODATE) - "Not all labor, just external (warehouse/install) labor - Line code identifies external labor" - Discussion
- **REQ-023**: Position formula line at bottom (not top), make uneditable and non-printing (ACCOMMODATE) - "My biggest gripe about that is that it's always line one... [Kipp's Wish List:] 1. Need the line (most important) 2. Always at bottom (not top) 3. Uneditable 4. Not printing 5. Always dynamic" - Kipp

### Punch List & Issue Management
- **REQ-024**: Implement punch list functionality in Field Service app to replace PlanGrid (ACCOMMODATE) - "We've built specific functionality into the field service app and into the work order application to replace [PlanGrid], so you don't have to use... Plan grid... One last thing to pay for." - Marcus
- **REQ-025**: Enable floor plan markup with location pinning for punch items (ACCOMMODATE) - "Four months later you get that punch item and you've done 15 jobs. You're like, yeah, I'll remember what room that goes into. And you don't. We all know the reality there." - Discussion
- **REQ-026**: Support offline mode for field app with sync capability (ALIGNS) - "You download all your work event information, you go into a building with no internet connectivity, you can still do all your work, take pictures, create punch, and then it'll sync when you..." - Marcus
- **REQ-027**: Enable status report generation from field app (not just desktop) (ACCOMMODATE) - "Generating it in the app is not going to be a challenge for us to do. We just weren't planning on it, but we can." - Marcus decision

### Field Service App
- **REQ-028**: Deploy Field Service app for PMs and contractors (tablet/mobile) (ALIGNS) - "Platform: Tablet primary - Mobile phone responsive - Works on both" - Description
- **REQ-029**: Enable check-in with geological stamping to confirm on-site presence (ALIGNS) - "Is it geologically confirmed that you're actually on site when you're checking? Yeah, stamp set." - Confirmation
- **REQ-030**: Support photo attachment, signatures, and document collection (ALIGNS) - "Attach files - Collect signatures - Initiate change orders - Document return of product" - Features shown
- **REQ-031**: Enable multi-resource time entry from work order events (ALIGNS) - "If five resources on event: Fill in time once, applies to all - Add temporary resources - Time entry tied to work order event" - Functionality

### Scheduling & Resource Management (Future Session Needed)
- **REQ-032**: Determine PM task list automation approach (ADAPT) - "What I'm hoping for is on every project, when you get assigned as project manager, you're going to get a list of tasks, which are always going to include site verification, delivery, walkthrough, all these different things." - Wendy vision
- **REQ-033**: Evaluate resource visualizer with calendar view of PM workloads (ACCOMMODATE) - "I do also pull this up during my one-on-ones with the PMs and just kind of go through each project... Shows project timelines by PM - Shows install dates (bars on timeline)" - Wendy current process
- **REQ-034**: Determine task management sophistication level (10 phases vs 300 granular tasks) (ADAPT) - "If they're going to build us something, Kimmy, we have to decide, is it the 10 phases or is it the 300 things that happen in each one of those phases?" - Matt

## Action Items

ACTION: Schedule preview session for entire operations suite (Advanced Receiving, work orders, scheduling, dispatching, field service)  
ASSIGNED TO: Marcus/Chris (Implementation Team)  
DUE: Before detailed design phase  
RELATED TO: REQ-002, REQ-013, REQ-024, REQ-028

ACTION: Provide 15% labor markup complete logic with all exceptions (order types, clients)  
ASSIGNED TO: Kipp  
DUE: During configuration phase  
RELATED TO: REQ-021, REQ-022, REQ-023

ACTION: Provide rate matrix for PM and design rates (internal costs and client billing)  
ASSIGNED TO: Kipp/Wendy  
DUE: During configuration phase  
RELATED TO: REQ-017, REQ-018, REQ-019

ACTION: Determine categorization approach for damage communication (issue type vs. punch type)  
ASSIGNED TO: Marcus/Team  
DUE: During workflow design  
RELATED TO: REQ-024

ACTION: Provide examples of current PlanGrid status reports for format reference  
ASSIGNED TO: Wendy/PM Team  
DUE: During field service app configuration  
RELATED TO: REQ-027

ACTION: Final confirmation on work order usage decision  
ASSIGNED TO: Wendy/Operations Team  
DUE: Before configuration  
RELATED TO: REQ-013

ACTION: Define damaged product write-off accounting treatment for zero-cost replacements  
ASSIGNED TO: Lorraine/Kipp  
DUE: During configuration (pinned for later discussion)  
RELATED TO: REQ-011

ACTION: Identify which contractors should receive time entry access  
ASSIGNED TO: Wendy/Rafina  
DUE: During user provisioning  
RELATED TO: REQ-020

## Additional Sessions Needed

### Session: Scheduling & Resource Management Deep Dive
- **Participants Needed**: Wendy (PM Manager), Kimmy (Account Manager), Matt (Leadership), Marcus (Implementation Team)
- **Questions to Address**: 
  • What level of project task management is needed (10 phases vs. 300 tasks)?
  • Should PM task lists be automated with templates?
  • Is Asana-style workflow with task dependencies desired?
  • What resource visualizer/calendar views are needed?
  • How should account manager pre-quote workload tracking integrate?
  • Manager vs. individual contributor view requirements?
- **Priority**: Medium - Impacts PM efficiency and resource allocation
- **Suggested Duration**: 2 hours
- **Dependencies**: REQ-032, REQ-033, REQ-034
- **Evidence**: "We'll definitely come back to that. So scheduling and resourcing... we'll have another session where we go a little bit deeper on this." - Marcus decision

### Session: Operations Suite Demo (Advanced Receiving, Field Service, Work Orders)
- **Participants Needed**: Wendy, PMs, Operations Team, Marcus/Chris (Implementation Team)
- **Questions to Address**: 
  • Live demonstration of Advanced Receiving drag-and-drop functionality
  • Field Service app walkthrough (latest version, not demo version shown)
  • Floor plan punch pinning demonstration
  • Work order creation and soft scheduling workflow
  • Status report generation from field app
  • Offline mode demonstration
- **Priority**: High - Critical for user adoption and training preparation
- **Suggested Duration**: 1.5-2 hours
- **Dependencies**: REQ-002, REQ-013, REQ-024, REQ-025, REQ-026, REQ-027, REQ-028
- **Evidence**: "Let's schedule a session to do a preview of the whole operations suite, especially since it's new... receiving, work order, scheduling, dispatching, and field service." - Marcus

## New Questions Identified

### Proposed New Question: What is the complete exception logic for the 15% labor markup (order types and specific clients)?
- **Asked By**: Marcus (requested from Kipp)
- **Context**: Need full logical expression to replicate business rule in NetSuite
- **Suggested Placement**: Section on Labor Markup and Costing
- **Evidence**: "But it's based off of order type, not based off of client. You could add in additional exceptions by client if you wanted to as well. So there's a few ways to do it. I just need to know, like, that full logical expression." - Marcus

### Proposed New Question: What specific information should be included in PM task lists if automated?
- **Asked By**: Wendy (expressed vision)
- **Context**: Automating PM task assignment requires defining standard tasks
- **Suggested Placement**: Section on PM Scheduling and Task Management
- **Evidence**: "What I'm hoping for is on every project, when you get assigned as project manager, you're going to get a list of tasks, which are always going to include site verification, delivery, walkthrough, all these different things." - Wendy

### Proposed New Question: Which external contractors should receive time entry access and what reconciliation controls are needed?
- **Asked By**: Implicit in contractor time entry discussion
- **Context**: Security and control requirements for external access
- **Suggested Placement**: Section on Time Tracking
- **Evidence**: "Some of our contractors, they have core time-entry access, because we can give them access to just time-entry... Rafina (Design Manager) reconciles - Compare time entered to invoice received" - Process description

### Proposed New Question: What are the complete content and format requirements for field status reports?
- **Asked By**: Implicit when discussing PlanGrid report replacement
- **Context**: Replicating current PlanGrid report functionality in NetSuite
- **Suggested Placement**: Section on Field Service and Reporting
- **Evidence**: "Current PlanGrid Feature: Generate report on iPad - Email from PlanGrid - PM in field initiates and sends... Sometimes it's me, and sometimes it's them" - Wendy

## Questionnaire Responses

---

## Section 1: Operations Scope & Process Flow

### 1. What is the scope of operations processes that need to be managed in NetSuite?

**Answer:**
Operations at KBM Hoag encompasses **purchase requisitions through punch completion**, with a unique operational model where most installation work is outsourced to third-party contractors while the company maintains project oversight through PMs. The company does not do its own installation, instead managing operations across multiple third-party warehouses and installation partners.

**Process Flow:**
1. Purchase Requisitions (approval workflow)
2. Receiving (third-party warehouses)
3. Scheduling & Resource Management (PM assignments)
4. Work Order Management (installation oversight)
5. Vendor Return Management (VRAs for damaged product)
6. Time Tracking (PM and design hours)
7. Punch List & Issue Management (field app)
8. Field Operations (contractor coordination)
9. Vendor Center (portal access for contractors)

**User Stories:**
- As Marcus (Operations Manager), I need to track receiving at third-party warehouses so that WIP is accurately reflected even though we don't control the warehouse
- As Wendy (PM Manager), I need to coordinate installation with outsourced contractors so that projects complete on time without direct installation control

**Current State Process:**
**PROCESS**: Operations Coordination with Third-Party Partners  
**TRIGGER**: Product ships to third-party warehouse  
**STEPS**:
1. Product ships to contractor warehouse
2. Contractor emails receiving@KBM when product arrives
3. KBM team manually tracks in system
4. Coordinate installation scheduling via email
5. PM oversees but doesn't perform installation
6. Punch list tracked in PlanGrid

**SYSTEMS INVOLVED**: Core (current), Email, PlanGrid, Google Sheets (PM scheduling)  
**PAIN POINTS**: Email-based communication easy to lose, no centralized tracking, manual coordination, lack of visibility into contractor status

**BRD Requirements:**
- [REQUIREMENT] Support outsourced installation model with third-party warehouse receiving (ID: REQ-002, Type: Functional)
- [REQUIREMENT] Enable contractor portal for communication without email dependency (ID: REQ-006, Type: Functional)
- [PRIORITY] Must-Have
- [CONSTRAINT] Company does not perform own installation; all solutions must work with external partners

**Stakeholder Impact:**
- **Primary Users**: Wendy (PM Manager), PMs in field, receiving team
- **Secondary Users**: Installation contractors, warehouse partners
- **Approvers**: Operations leadership
- **Impacted Parties**: Design team (time tracking), finance (WIP impact)

**Evidence:**
- "For our purposes today, we're really kind of just looking at purchase requisitions through punch completion." - Session scope
- "Not doing own installation - Third-party warehouses receive product - No direct visibility to receiving status - Currently: Email communication from contractors" - Current challenge
- "Receiving is what impacts your WIP. So we still want to do that." - Why receiving still necessary

**Confidence Rating**: 98% - Explicitly stated scope with clear operational model explained

**Outstanding Items:**
- Need to map all third-party warehouse locations for bin setup
- Confirm all installation partners who need vendor center access

---

## Section 2: Purchase Requisitions

### 2. Will you use purchase requisitions for purchasing approval workflow?

**Answer:**
Yes. KBM Hoag has **decided to implement purchase requisitions** with supervisor approval workflow. This will enable controlled purchasing where employees submit requisitions that route to appropriate approvers, and once approved, automatically convert to purchase orders without re-keying information.

**User Stories:**
- As an Employee, I need to submit purchase requisitions so that I can request needed items through proper approval channels
- As a Supervisor, I need to review and approve purchase requisitions so that I can control department spending and authorize purchases
- As a Finance Manager, I need purchase approval audit trails so that I can ensure all purchases are properly authorized

**BRD Requirements:**
- [REQUIREMENT] Implement purchase requisition approval workflow (ID: REQ-001, Type: Functional)
- [FUNCTIONALITY] NetSuite Purchase Requisition module with supervisor approval routing
- [PRIORITY] Must-Have
- [DECISIONS] Use purchase requisitions for approval control

**Stakeholder Impact:**
- **Primary Users**: Employees requesting purchases, supervisors approving
- **Approvers**: Department supervisors, budget owners
- **Impacted Parties**: AP team (receives approved POs), procurement

**Evidence:**
- "We made the decision yesterday we'll be using purchase requisitions." - Team decision
- "Employee submits purchase requisition - Requires supervisor approval - Once approved: Converts to purchase order automatically - All information transfers (no re-keying)" - Functionality described

**Confidence Rating**: 98% - Explicit decision made and documented

---

## Section 3: Receiving & Warehouse Management

### 3. How does your outsourced installation model affect receiving processes?

**Answer:**
KBM Hoag faces a unique challenge because they don't do their own installation and instead rely on **third-party warehouses** to receive product. This creates visibility challenges as they currently rely on email communication from contractors to know when product arrives. However, receiving must still be tracked in NetSuite because **receiving impacts WIP** (Work in Progress inventory), even though KBM doesn't physically control the warehouses.

**Current State Process:**
**PROCESS**: Third-Party Receiving Notification  
**TRIGGER**: Product delivery to contractor warehouse  
**STEPS**:
1. Product ships to third-party installation partner warehouse
2. Contractor receives product physically
3. Contractor sends email to receiving@KBM
4. KBM team manually receives in system
5. WIP impacted in financial system

**SYSTEMS INVOLVED**: Core (current), Email  
**PAIN POINTS**: Email easy to lose, no automated notification, no direct visibility, delayed WIP updates, manual process

**BRD Requirements:**
- [REQUIREMENT] Implement Advanced Receiving tool with drag-and-drop functionality (ID: REQ-002, Type: Functional)
- [REQUIREMENT] Configure receiving bins per third-party warehouse location (ID: REQ-003, Type: Functional)
- [REQUIREMENT] Enable vendor center receiving notifications to replace email (ID: REQ-007, Type: Functional)
- [FUNCTIONALITY] Orion Advanced Receiving tool, Vendor Center portal
- [PRIORITY] Must-Have
- [CONSTRAINT] No direct physical control over warehouse operations

**Stakeholder Impact:**
- **Primary Users**: Receiving team, installation contractors
- **Secondary Users**: Finance team (WIP tracking), PMs (need to know product availability)
- **Impacted Parties**: Contractors must adopt new notification process

**Evidence:**
- "Not doing own installation - Third-party warehouses receive product - No direct visibility to receiving status - Currently: Email communication from contractors" - Current challenge
- "Receiving is what impacts your WIP. So we still want to do that." - Why receiving necessary
- "They're sending it via email over to receiving at KBM call" - Current process

**Confidence Rating**: 98% - Clear explanation of operational model and pain points

**Outstanding Items:**
- List of all third-party warehouse locations needed for bin setup
- Decision on contractor direct receiving capability (deferred to future)

---

### 4. What is the Advanced Receiving tool and how will it improve your receiving process?

**Answer:**
The **Orion Advanced Receiving tool** is a custom-built utility that sits on top of NetSuite to make receiving significantly easier than standard NetSuite functionality. It features a **drag-and-drop interface** where users can see all items on a purchase order and all available bins, then simply drag items to bins to complete receiving. This works on both tablet and desktop, making it accessible for warehouse or office use.

**User Stories:**
- As a Receiving Clerk, I need a simple drag-and-drop interface so that I can quickly receive items to the correct bins without complex NetSuite navigation
- As a Remote Receiver (office-based), I need to receive items at third-party warehouses based on contractor notification so that WIP updates without visiting the physical location

**BRD Requirements:**
- [REQUIREMENT] Deploy Orion Advanced Receiving tool (ID: REQ-002, Type: Functional)
- [FUNCTIONALITY] Orion Advanced Receiving (custom Orion innovation, not NetSuite standard)
- [SOLUTIONDESIGN] Yes - Custom tool developed by Orion
- [PRIORITY] Must-Have
- [DECISIONS] Use Advanced Receiving to simplify outsourced model

**Evidence:**
- "Traditionally, in NetSuite, receiving is actually kind of clunky, it's kind of difficult to do, so we built this tool, this utility that sits on top of it." - Marcus explaining innovation
- "Here's all my items, here's all my bins, and I can grab items and I can just drag them to the bin and that's it, now they're received" - Functionality description
- "Tablet/desktop compatible - Part of Orion (not NetSuite standard)" - Platform compatibility

**Confidence Rating**: 98% - Detailed explanation with clear benefits stated

---

### 5. What bin structure do you need for inventory management?

**Answer:**
KBM Hoag needs a **simple bin structure** with one primary receiving bin per third-party warehouse location, plus specialized bins for damaged and duplicate inventory. Since they don't control the warehouses and don't need granular location tracking within warehouses, the approach is straightforward: one bin per location for normal receiving, with quarantine bins for exceptions.

**Bin Types Needed:**

1. **Normal Receiving Bin** (one per third-party warehouse)
   - Standard product receiving
   - One bin per installation partner location
   - Simplest approach for outsourced model

2. **Damaged Inventory Bin** (one per location)
   - Quarantine damaged product
   - Cannot be accidentally allocated to orders
   - Prevents damaged items shipping out
   - Triggers VRA process

3. **Duplicate Inventory / Overages Bin** (one per location)
   - Excess product
   - Duplicate shipments
   - Not allocated to specific orders

4. **Office/Showroom Bins** (if needed)
   - May need bin for office location
   - Showroom receiving
   - Sometimes ships to employee homes (e.g., Kipp's house, then to job site)

**Special Cases:**
- **Direct-to-Site**: No receiving bin needed, mark as shipped, track timing only
- **Bin Transfers**: Can move from one bin to another (same location)
- **Transfer Orders**: Can move between locations if needed

**User Stories:**
- As a Receiving Clerk, I need separate bins for damaged inventory so that damaged items cannot accidentally be allocated to customer orders
- As a PM, I need visibility into what's in the damaged bin so that I can track VRA status and replacement needs

**Current State Process:**
**PROCESS**: Receiving with Damage Segregation  
**TRIGGER**: Product arrives with some damaged items  
**STEPS**:
1. Contractor notifies KBM of receipt with damage notation
2. Receiving clerk opens PO in Advanced Receiving tool
3. Drag good items (quantity: 8) to normal receiving bin
4. Drag damaged items (quantity: 2) to damaged bin
5. System prevents allocation of damaged items
6. VRA process initiated for damaged items

**SYSTEMS INVOLVED**: NetSuite, Advanced Receiving tool  
**PAIN POINTS**: Need to ensure contractors clearly communicate which items are damaged

**BRD Requirements:**
- [REQUIREMENT] Configure one receiving bin per third-party warehouse (ID: REQ-003, Type: Functional)
- [REQUIREMENT] Configure damaged inventory bin per location (ID: REQ-004, Type: Functional)
- [REQUIREMENT] Configure duplicate/overage bin per location (ID: REQ-005, Type: Functional)
- [FUNCTIONALITY] NetSuite bin management
- [PRIORITY] Must-Have
- [CONSTRAINT] System must prevent allocation of damaged bin inventory

**Evidence:**
- "I think you're probably gonna have, here's our location, that's the warehouse that it's being shipped to, there's only one bin at that location, because you don't care where it's being tracked there." - Simple bin approach
- "We need to [receive] it somewhere where somebody can't accidentally inside the system allocate it to an item fulfillment so it gets shipped out." - Purpose of damaged bin
- "Drag/drop 8 items to normal bin - Drag/drop 2 items to damaged bin - Now have traceability: What's damaged, where it's at, needs VRA" - Receiving process example

**Confidence Rating**: 95% - Clear bin strategy explained with examples

**Outstanding Items:**
- Complete list of all third-party warehouse locations
- Confirm if office/showroom bins needed
- Define naming convention for bins

---

## Section 4: Vendor Center (Contractor Portal)

### 6. What is the Vendor Center and how will contractors use it?

**Answer:**
The **Vendor Center** is a portal where KBM Hoag's vendors and subcontractors can log in to see their purchase orders, work orders, project information, and communicate with KBM. This is particularly important for KBM's outsourced installation model. The unique advantage is that there is **no additional license cost** - Orion uses one shared license for all vendors regardless of volume.

**Access Scope for Contractors:**
- View purchase orders sent to them
- View work orders and installation schedules
- Access project information relevant to their work
- Communicate via notes and messages
- Attach documents and photos
- Notify KBM of product receipt

**User Stories:**
- As an Installation Contractor, I need to access my work orders and POs in one place so that I don't rely on scattered emails
- As a Receiving Coordinator, I need contractors to notify me of arrivals through the portal so that I don't miss email notifications
- As an Operations Manager, I need centralized contractor communication so that project status updates are tracked in the system

**Future Process (Vendor Center):**
**PROCESS**: Receiving Notification via Vendor Center  
**TRIGGER**: Product arrives at contractor warehouse  
**STEPS**:
1. Contractor logs into vendor center
2. Sees all their work and incoming POs
3. Product arrives at their warehouse
4. Click "Notify of Arrival" on PO
5. Can attach photos/documents
6. Notification shows up in KBM Hoag dashboard (not email)
7. KBM team goes to PO and receives it using Advanced Receiving tool
8. Done

**SYSTEMS INVOLVED**: NetSuite Vendor Center, Advanced Receiving tool  
**PAIN POINTS**: Relies on contractor adoption of new portal (training needed)

**BRD Requirements:**
- [REQUIREMENT] Implement vendor center portal for contractor access (ID: REQ-006, Type: Functional)
- [REQUIREMENT] Enable receiving notification feature (ID: REQ-007, Type: Functional)
- [REQUIREMENT] Enable document attachment and communication (ID: REQ-009, Type: Functional)
- [FUNCTIONALITY] NetSuite Vendor Center with Orion enhancements (receiving notification)
- [SOLUTIONDESIGN] Yes - Receiving notification feature is Orion custom development
- [PRIORITY] Must-Have
- [DECISIONS] Use vendor center for contractor communication, defer direct receiving by contractors

**Stakeholder Impact:**
- **Primary Users**: Installation contractors, subcontractors, receiving team
- **Secondary Users**: PMs viewing contractor status
- **Impacted Parties**: All installation partners must adopt new system

**Evidence:**
- "The vendor center, which I think is gonna be really important for you guys, that's just a place for your vendors to log in, including your subcontractors." - Marcus
- "There's no additional cost for the field service app. Don't tell them that's why we did that. Usually you charge a license for each one. What we did is, we use one license for everybody." - Marcus on no-cost access
- "We are putting in a feature that allows your vendor, or your subcontractor, to notify you that they've received it, right from inside the vendor center." - Receiving notification feature

**Confidence Rating**: 98% - Detailed functionality explanation with clear decision

**Outstanding Items:**
- List of all contractors who need vendor center access
- Training plan for contractor adoption
- Backup process if contractors don't adopt

---

### 7. Should contractors be given the ability to do direct receiving in NetSuite?

**Answer:**
**Not initially** - this has been **deferred to future consideration**. The team discussed giving contractors the ability to mark items as received directly in NetSuite, but there are concerns about permission creep, mistakes, and trust levels varying by contractor. For now, contractors will use the vendor center to **notify KBM of arrival**, and KBM team will perform the actual receiving in NetSuite with oversight.

**Concerns with Direct Contractor Receiving:**
- **Mistakes difficult to undo**: "You have 200 lines on the PO, they receive all 200. And then like, oh, crap, I shouldn't have done all of them."
- **Permission creep**: Edit capability needed to fix mistakes could allow access to other POs
- **Variable trust levels**: Trust level varies by contractor
- **No oversight**: Contractors might not understand WIP impact or bin selection

**Current Decision:**
Contractors can notify KBM via vendor center, and it shows up on KBM's report/dashboard. KBM team does actual receiving.

**Future Option:**
Can be revisited later if trust and process mature.

**User Stories:**
- As a Receiving Manager, I need to control actual receiving transactions so that I can ensure proper bin assignment and WIP accuracy
- As a Contractor, I need an easy way to tell KBM product arrived so that I don't rely on email

**BRD Requirements:**
- [REQUIREMENT] Defer contractor direct receiving to future phase (ID: REQ-008, Type: Non-Functional)
- [ASSUMPTION] Contractors will reliably notify via vendor center
- [RISK] If contractors don't adopt vendor center, falls back to email
- [PRIORITY] Nice-to-Have (future phase)
- [DECISIONS] Use notification model (not direct receiving) initially

**Evidence:**
- "For now, they can just get as received. Yep. And it'll show up on our report." - Current decision
- "If it's not part of it now, it is in the future. We can always look at that later." - Future option
- "So I'm not saying it's not doable. It's absolutely doable. It just really comes down to how much trust you have in them." - Marcus on trust concern

**Confidence Rating**: 95% - Clear decision with rationale, explicitly deferred to future

---

## Section 5: Vendor Return Authorizations (VRAs)

### 8. How do you handle damaged product and vendor credits?

**Answer:**
KBM Hoag will use the **full VRA (Vendor Return Authorization) process** even when product is not being shipped back to the vendor (which is 80% of cases). This decision addresses a critical pain point: **tracking expected vendor credits** that often get lost and never followed up. The VRA provides traceability for why credits are deserved, enables systematic follow-up, and prevents credits from falling through the cracks.

**Modified VRA Process for KBM:**

**When Damage Occurs:**
1. Product arrives damaged at third-party warehouse
2. Must still receive it (impacts WIP)
3. Receive damaged items to damaged bin
4. Reach out to vendor for replacement/credit
5. Create VRA even if not shipping back (new approach)

**Replacement Process:**
6. Add zero-cost line to existing PO for replacement
7. Vendor ships replacement
8. Receive replacement on new zero-cost line
9. Original damaged item stays in damaged bin

**VRA & Credit Process:**
10. Create VRA documenting damage and credit expectation
11. Add notes explaining reason for credit
12. If shipping back (10% of cases): Create item fulfillment
13. If not shipping back (90% of cases): Close VRA without shipment
14. Vendor issues credit memo number
15. Create bill credit in NetSuite with vendor's number
16. Full traceability maintained

**Current Pain Point (Lorraine):**
"One thing that's always kind of nagged me is that people will enter lines for credits that we're expecting. And then they just kind of, there's not really a way to track it. To make sure that we ever get that credit... So they just kind of go in there and you're just like throwing it out there. I hope we get this. And then no one ever really follows up on it."

**Marcus's Vendor Pressure Tactic:**
Create bill credit with number "TBD", send end-of-month report to vendor with all expected credits. "That gets their attention and then you get the credit memo number" or "you just apply it and then they get pissed off because now you're paying stuff with credit."

**User Stories:**
- As Lorraine (CFO), I need systematic tracking of expected vendor credits so that I can follow up and ensure we receive all credits we're entitled to
- As an AP Clerk, I need the VRA to document why we deserve a credit so that I can justify it to the vendor months later
- As a PM, I need to know which items in damaged bins have VRA processing so that I can communicate replacement timelines to clients

**Current State Process:**
**PROCESS**: Damaged Product Credit Request (Current - Problematic)  
**TRIGGER**: Damaged product received  
**STEPS**:
1. Receive damaged product
2. Enter line for expected credit
3. Hope vendor eventually issues credit
4. No systematic follow-up
5. Credits often lost
6. Manual forensic accounting to resolve

**SYSTEMS INVOLVED**: Core (current)  
**PAIN POINTS**: No systematic tracking, no follow-up mechanism, credits lost, manual reconciliation

**BRD Requirements:**
- [REQUIREMENT] Use VRA process even when not shipping back (80/20 rule) (ID: REQ-010, Type: Functional)
- [REQUIREMENT] Configure zero-cost replacement line workflow (ID: REQ-011, Type: Functional)
- [REQUIREMENT] Implement expected credit tracking with follow-up reporting (ID: REQ-012, Type: Functional)
- [FUNCTIONALITY] NetSuite VRA module with bill credit linkage
- [PRIORITY] Must-Have
- [DECISIONS] Use VRA for all damage scenarios to track credits
- [RISK] Requires discipline to create VRA every time (not just when shipping back)

**Stakeholder Impact:**
- **Primary Users**: AP team (Guada, Michael), receiving team
- **Secondary Users**: Lorraine (credit tracking), PMs (replacement status)
- **Approvers**: Lorraine (credit approval)

**Evidence:**
- "We'll use the VRA item fulfillment bill credit process... Let's say 80% of the time they're not getting shipped back it's an 80-20 rule, but we could still use the VRA to track the reasons." - Decision quote
- "Sometimes, depending on what it is, sometimes they want it back. Probably 90% of the time they do not." - Return frequency
- Lorraine's full quote above documenting pain point
- Marcus's tactic quote about TBD credits

**Confidence Rating**: 98% - Explicit decision with strong supporting rationale and pain point evidence

**Outstanding Items:**
- Define damaged product write-off accounting treatment (pinned for later with Lorraine/Kipp)
- Confirm VRA approval workflow
- End-of-month credit report format

---

## Section 6: Work Order Management

### 9. Will you use work orders for managing installation and PM activities?

**Answer:**
**Soft yes** - Wendy signed on for work orders during the session, though it wasn't a finalized hard decision yet. Work orders will be used to manage installation events, PM site visits, and other field activities. The approach will be kept **as simple as needed** - work orders can be generated from sales orders without picking specific lines, assigned event types, soft scheduled (not hard scheduled), and used to coordinate with both internal PMs and external installation contractors.

**Work Order Event Types:**
- Site verification (PM pre-install visit)
- Delivery and install (primary event)
- Site review (post-install)
- PM on-site presence (during delivery)
- Design meetings (if on-site)
- Punch walks (post-completion inspection)

**Simple Work Order Workflow:**
1. Go to sales order
2. Generate work order (don't have to pick specific lines)
3. Choose event type
4. Assign resource (PM or contractor)
5. Save as soft scheduled
6. Done

**Soft Scheduling Approach:**
Someone can request scheduling on a PM, but PM must approve (not hard scheduled without consent). Similar concept to soft-scheduling installation jobs with contractors.

**User Stories:**
- As a PM, I need work orders for my site visits so that all event information (location, contacts, site requirements) is in one place instead of scattered emails
- As Wendy (PM Manager), I need work orders to track PM assignments so that I can see workload distribution and schedule coverage
- As an Installation Coordinator, I need work orders for contractor installations so that we have formal scheduling and tracking

**BRD Requirements:**
- [REQUIREMENT] Implement work orders for installation and PM events (ID: REQ-013, Type: Functional)
- [REQUIREMENT] Configure event types (ID: REQ-014, Type: Functional)
- [REQUIREMENT] Enable soft scheduling with approval workflow (ID: REQ-015, Type: Functional)
- [FUNCTIONALITY] NetSuite Work Order Management
- [PRIORITY] Should-Have (Wendy buy-in but not fully finalized)
- [DECISIONS] Use work orders, keep simple, soft schedule approach

**Evidence:**
- "I don't think we've made the hard decision that we're going to use them. It keeps coming up." - Status pre-session
- "Wendy signed on for work orders just now, so that was good. That's like mission accomplished." - Marcus noting buy-in
- "The one thing I just want you to know about work order management is it can be as easy or sophisticated as you want it to be." - Marcus on flexibility
- "Could you soft-schedule them the same way you would soft-schedule a job." - Soft scheduling approach

**Confidence Rating**: 90% - Wendy buy-in achieved but final leadership confirmation pending

**Outstanding Items:**
- Final confirmation from Wendy/operations leadership
- Define complete list of event types
- Soft scheduling approval workflow details

---

## Section 7: Time Tracking & Project Management

### 10. How should time tracking impact project financials?

**Answer:**
Time tracking will **impact project GP (gross profit) but NOT impact GL (general ledger)**. This is an important distinction that not all dealers make. PMs and designers track time against projects, and that time calculates cost based on a rate matrix, which then impacts the project's gross profit calculations. However, payroll is handled separately through journal entry import from Paylocity (or future payroll provider), so time tracking doesn't directly hit the GL.

**Rate Structure:**

**PM Rates:**
- Flat rate (not hourly)
- Internal rate (cost to project)
- External rate (client billing)
- Some clients have negotiated different rates

**Design Rates:**
- Flat rate
- Workshop designer (lower internal hourly rate)
- Standard designer (standard rate)
- Field designers may differ from studio
- Client billing rate may be negotiated

**External Contractor Time:**
- Some contractors have Core time-entry access
- Log time directly into KBM system
- Rafina (Design Manager) reconciles time entered vs. invoice received
- Time impacts GP at KBM internal rate (not contractor's actual cost)
- If contractor charges $95/hour but KBM rate is $85/hour, only $85 impacts project
- KBM absorbs difference when understaffed

**Reality Check (Matt):**
"I'll state for the record, we lose money on design. Design does not make money. No matter how much design we bill, our payroll costs more than what we were able to bill to a client at any point."

**Tracking Frequency:**
- Ideal: Weekly time tracking
- Reality: "They have to be slapped around a little bit" to comply

**User Stories:**
- As a PM, I need to track my time to projects so that project GP accurately reflects PM resource consumption
- As a Designer, I need to track time so that design costs are properly allocated to projects vs. G&A
- As Wendy (PM Manager), I need time tracking integrated with work orders so that PMs can log time directly from field activities
- As Lorraine (CFO), I need time to impact GP so that project profitability reflects true resource costs

**BRD Requirements:**
- [REQUIREMENT] Configure time tracking to impact project GP (not GL) (ID: REQ-016, Type: Functional)
- [REQUIREMENT] Configure PM flat rate structure (ID: REQ-017, Type: Functional)
- [REQUIREMENT] Configure design rate matrix with multiple internal rates (ID: REQ-018, Type: Functional)
- [REQUIREMENT] Support negotiated client rates with standard internal costs (ID: REQ-019, Type: Functional)
- [REQUIREMENT] Allow external contractor time entry with reconciliation (ID: REQ-020, Type: Functional)
- [FUNCTIONALITY] NetSuite Time Tracking with rate matrix
- [PRIORITY] Must-Have
- [DECISIONS] Time impacts GP, not GL
- [CONSTRAINT] Rate matrix must support multiple internal rates and negotiated client rates

**Stakeholder Impact:**
- **Primary Users**: PMs, designers, external contractors (some)
- **Secondary Users**: Rafina (reconciliation), finance team
- **Approvers**: Wendy (PM time), Rafina (design time)

**Evidence:**
- "I just want to say it out loud, again, for the sake of the transcript, because not all dealers do it this way. We do want that time to impact the GP. Yes." - Marcus making explicit
- "Time tracking has no GL impact (confirmed) - Does have GP impact on project - Affects project profitability" - Confirmation
- "So there's a design client rate and a PM client rate, and then there's basically three internal rates." - Wendy on rate structure
- Matt's quote about design losing money
- "They have to be slapped around a little bit. Sometimes. I know. And I get it. The time tracking is a pain in the butt." - Tracking compliance challenge

**Confidence Rating**: 98% - Explicit confirmation with detailed rate structure discussion

**Outstanding Items:**
- Complete rate matrix (action item for Kipp/Wendy)
- List of external contractors who should have time entry access
- Define reconciliation workflow in detail

---

## Section 8: 15% Labor Markup (Formula Line)

### 11. What is the 15% labor markup and how should it work in NetSuite?

**Answer:**
KBM Hoag has a unique **15% labor markup formula line** that auto-calculates on every sales order that includes labor. This is a **cost-only line** (no revenue) that takes 15% of the cost of external labor and decreases the GP. It's essentially a built-in contingency for labor unpredictability. In Core, this line automatically appears as line 1, which bothers Kipp because it messes up customer proposal line numbering.

**How It Works:**
- Every new order automatically pulls in a line: "KPMG 15%"
- Line is cost-only (no revenue component)
- Auto-calculates based on external labor lines only
- Formula looks at line code to identify external labor
- Takes 15% of those labor costs
- Decreases project GP (behavioral forcing function)
- No GL impact
- Does NOT apply to all labor - only external (warehouse/install) labor

**Purpose & History:**
- Used to have own warehouse
- Forklift incident with drinking → stopped own warehouse operations
- "We decided we didn't want to be in an OSHA environment anymore"
- Goal: Force higher markup on labor to account for unpredictability
- "It's a behavioral push" - Forces account managers to price labor appropriately
- Guards against underpricing labor

**Kipp's Wish List:**
1. Keep the line (most important)
2. Position at **bottom** of order (not line 1)
3. **Uneditable** (can't be manually changed)
4. **Non-printing** (doesn't show on customer proposals)
5. Always dynamic (recalculates automatically)

**Current Problem:**
"My biggest gripe about that is that it's always line one. So any time you issue a proposal with line numbers it starts at two... Somebody with OCD... I will murder this thing."

**Exceptions:**
- Based on order type primarily
- Some client-based exceptions possible
- Business rule logic must be fully defined
- Kipp to provide complete exception logic

**User Stories:**
- As an Account Manager, I need the 15% markup to auto-calculate so that I don't accidentally underprice labor
- As Kipp (IT Specialist), I need the formula line at the bottom and non-printing so that customer proposals have clean line numbering starting at 1
- As Matt (Leadership), I need the markup to enforce margin discipline so that we don't lose money on labor variability

**BRD Requirements:**
- [REQUIREMENT] Implement 15% labor markup formula line (cost-only, no revenue) (ID: REQ-021, Type: Functional)
- [REQUIREMENT] Apply only to external labor (not all labor) (ID: REQ-022, Type: Functional)
- [REQUIREMENT] Position at bottom, make uneditable and non-printing (ID: REQ-023, Type: Functional)
- [FUNCTIONALITY] NetSuite formula line with business rules
- [SOLUTIONDESIGN] Yes - Custom business rule configuration
- [PRIORITY] Must-Have (critical to pricing discipline)
- [DECISIONS] Continue 15% markup in NetSuite
- [CONSTRAINT] Must apply only to orders meeting exception criteria

**Stakeholder Impact:**
- **Primary Users**: Account managers (automatic calculation)
- **Secondary Users**: Finance team (GP impact)
- **Approvers**: Matt/Mark (exception logic)
- **Impacted Parties**: Sales team (affects commissionable GP)

**Evidence:**
- "Every time you start a new order, it automatically pulls in a line that says KPMG 15%. And that line auto-calculates any time there's a labor line. It takes 15% of the GP and adjusts the whole GP." - How it works
- "My biggest gripe about that is that it's always line one." - Kipp's frustration
- "To get people to mark up what labor should be, it's supposed to be like stop marking up labor at the same as product. You need to be like marking up product higher. So we forced our markup by taking a hit against it. It's a behavioral push" - Purpose
- "We decided we didn't want to be in an OSHA environment anymore" - History (Matt)

**Confidence Rating**: 98% - Detailed explanation with clear requirements

**Outstanding Items:**
- Kipp to provide complete exception logic (order types, clients)
- Confirm if commission is paid on this line
- Define exact line code that identifies external labor

---

## Section 9: Punch List & Issue Management

### 12. How do you currently manage punch lists and what needs to change?

**Answer:**
PMs currently use **PlanGrid** for punch list management in the field. Orion has built specific punch list functionality into the **Field Service app** to replace PlanGrid, eliminating one more subscription cost. The critical feature is the ability to **pin punch items to locations on floor plans** so that months later, users can remember exactly which room or area had the issue.

**Current PlanGrid Process:**
- PM goes on punch walk
- Takes photos of issues in PlanGrid
- Marks location on floor plan drawing
- Enters description and details
- Can generate report on iPad
- Emails report directly from PlanGrid

**Pain Point:**
"Four months later you get that punch item and you've done 15 jobs. You're like, yeah, I'll remember what room that goes into. And you don't. We all know the reality there."

**Orion Replacement Functionality:**
- Built into Field Service app
- Must be resource on work order or work order event
- Take photo
- Punch reasons (what's wrong)
- Punch issues (why it's wrong, who's responsible)
- Associate lines with it (one or multiple)
- **Pin to location on floor plan** (critical feature)
- Works in offline mode
- Sync when back online

**Issue Types (Generic):**
NetSuite uses "issues" as generic term:
- Punch list items
- Bill price discrepancies
- Acknowledgement discrepancies
- Warehouse damage
- "Something that's wrong we wanna track"

**Status Report Generation:**
- Currently: Generate in PlanGrid on iPad, email directly
- NetSuite: Can generate in back-end NetSuite easily
- **New requirement**: Generate and send from field app (not originally planned)
- Marcus agreed to build this capability

**Offline Mode (Critical):**
1. Log in in morning
2. Download all work event information
3. Go into building (no internet)
4. Do all work, take pictures, create punch
5. Sync when back online

**User Stories:**
- As a PM, I need to create punch items in the field with photos so that I can document issues during the walk without returning to office
- As a PM, I need to pin punch items to floor plan locations so that months later I can remember exactly where the issue was
- As Wendy (PM Manager), I need to generate status reports from the field so that I can send client updates without waiting to get back to the office
- As a Client, I need visual floor plan reference for punch items so that I can understand exactly what needs to be addressed

**BRD Requirements:**
- [REQUIREMENT] Implement punch list in Field Service app to replace PlanGrid (ID: REQ-024, Type: Functional)
- [REQUIREMENT] Enable floor plan markup with location pinning (ID: REQ-025, Type: Functional)
- [REQUIREMENT] Support offline mode with sync capability (ID: REQ-026, Type: Functional)
- [REQUIREMENT] Enable status report generation from field app (ID: REQ-027, Type: Functional)
- [FUNCTIONALITY] Orion Field Service app with punch list module
- [SOLUTIONDESIGN] Yes - Custom Orion development
- [PRIORITY] Must-Have (replaces paid tool)
- [DECISIONS] Replace PlanGrid with Orion Field Service app
- [RISK] PMs must adopt new tool; training critical

**Stakeholder Impact:**
- **Primary Users**: PMs in field
- **Secondary Users**: Wendy (reports), clients (receiving reports)
- **Approvers**: Wendy (PM Manager)
- **Impacted Parties**: Installation contractors (may also access punch list via vendor center)

**Evidence:**
- "We've built specific functionality into the field service app and into the work order application to replace [PlanGrid], so you don't have to use... Plan grid. One last thing to pay for." - Marcus
- "Four months later you get that punch item..." - Pain point quote above
- "Generating it in the app is not going to be a challenge for us to do. We just weren't planning on it, but we can." - Marcus agreeing to report generation
- "You download all your work event information, you go into a building with no internet connectivity, you can still do all your work, take pictures, create punch, and then it'll sync when you..." - Offline mode description

**Confidence Rating**: 95% - Clear decision with detailed functionality, report generation added during session

**Outstanding Items:**
- Wendy to provide examples of current PlanGrid reports for format reference
- Floor plan file format requirements
- Training plan for PM adoption

---

## Section 10: Field Service App

### 13. What are the key features and requirements for the Field Service app?

**Answer:**
The **Field Service app** is Orion's tablet/mobile application for PMs and contractors to manage field activities. It works offline, integrates with work orders, and consolidates multiple functions: punch list management (PlanGrid replacement), time tracking, event management, document collection, signatures, and change order initiation.

**Platform:**
- Primary: Tablet (iPad)
- Also works on mobile phones (responsive)

**Dashboard View:**
- Each card = one work order event
- Multiple events possible per project
- Filtered by date (show today's work)
- PMs/subcontractors see only their assignments
- Status filters
- Sort options

**Event Detail Features:**
- **Location address** with map link (can navigate)
- **Check-in** (geologically stamped, confirms on-site)
- **Status updates** (in process, complete)
- **Site requirements** from job site analysis
- **Contact info** for project
- **Resource assignments**

**Items Tab:**
- See all products on work order
- Mark items in progress or completed
- Track completion by line item
- Useful for installation partners

**Time Tracking:**
- Multi-resource: If 5 resources on event, fill in once, applies to all
- Add temporary resources
- Time entry tied to work order event
- **Limitation**: Only work order event driven (design time must be entered in desktop)

**Punch List Features:**
- Create from details screen or floor plan
- Attach photos
- Associate with tasks
- Pin to floor plan location
- Works offline

**Additional Features:**
- Attach files
- Collect signatures
- Initiate change orders
- Document product returns

**Offline Mode (Critical Feature):**
Critical for buildings with no internet connectivity
1. Morning: Log in, download all work event info
2. Enter building (no connectivity)
3. Complete all work, take pictures, create punch
4. Exit building
5. Automatically syncs when back online

**Check-In Feature:**
"Is it geologically confirmed that you're actually on site when you're checking? Yeah, stamp set."
Provides accountability that PM/contractor was actually at the location.

**User Stories:**
- As a PM, I need the field app to work offline so that I can document work in buildings with no cell service
- As a PM, I need all event information (address, contacts, site requirements) on my tablet so that I don't need to search emails while in the field
- As Wendy (PM Manager), I need geological check-in stamps so that I can verify PMs were actually on-site at scheduled times
- As an Installation Contractor, I need to access my work order events on my phone so that I know what's scheduled and where

**BRD Requirements:**
- [REQUIREMENT] Deploy Field Service app for PMs and contractors (ID: REQ-028, Type: Functional)
- [REQUIREMENT] Enable geological check-in stamping (ID: REQ-029, Type: Functional)
- [REQUIREMENT] Support photo, signature, and document collection (ID: REQ-030, Type: Functional)
- [REQUIREMENT] Enable multi-resource time entry from events (ID: REQ-031, Type: Functional)
- [FUNCTIONALITY] Orion Field Service app (tablet/mobile)
- [PRIORITY] Must-Have
- [DECISIONS] Use Field Service app for all field operations
- [CONSTRAINT] Requires work order event to exist for time tracking

**Stakeholder Impact:**
- **Primary Users**: PMs, installation contractors
- **Secondary Users**: Wendy (monitoring), clients (receiving reports)
- **Approvers**: Wendy (PM Manager)
- **Impacted Parties**: All field personnel must adopt tablet/mobile app

**Evidence:**
- "The app works in offline mode as well." - Offline capability
- "Is it geologically confirmed that you're actually on site when you're checking? Yeah, stamp set." - Check-in feature
- "Attach files - Collect signatures - Initiate change orders - Document return of product" - Features list
- "You download all your work event information, you go into a building with no internet connectivity, you can still do all your work..." - Offline workflow

**Confidence Rating**: 95% - Comprehensive feature list with demonstrations (though older demo version shown)

**Outstanding Items:**
- Demo of latest version (session showed older version)
- Training materials for PM adoption
- Tablet hardware specifications/recommendations
- Change order workflow details

---

## Section 11: Scheduling & Resource Management

### 14. What are your scheduling and resource management needs?

**Answer:**
This is a **complex area requiring additional dedicated session**. The team has sophisticated needs around PM resource management, account manager workload tracking, and task management that go beyond what most dealers request. The discussion revealed tension between desired Asana-style workflow with task dependencies vs. Orion's experience that dealers resist that level of project management rigor.

**Current State (Wendy's PM Management):**

**Google Sheets Calendar:**
- Wendy maintains manual PM workload calendar
- Horizontal timeline view
- Projects as rows, grouped by PM
- Install dates highlighted as bars
- Scrollable by week
- Shows who has capacity
- Used for assignment decisions and one-on-one reviews

**Pain Point:**
"It's only as accurate as the information... Have they updated it, or is it standard?... Not accurate by time accessed"

**Desired Future State:**

**PM Assignment Timing Change:**
Currently: PM assigned late in process
Desired: "We're trying to change that, where the PM gets assigned at the same time as the designer gets assigned"

**PM Task List Vision (Wendy):**
"What I'm hoping for is on every project, when you get assigned as project manager, you're going to get a list of tasks, which are always going to include site verification, delivery, walkthrough, all these different things."

**Benefits:**
- PM knows what needs to be done
- Can self-schedule tasks
- If task not completed, someone knows it needs scheduling
- Accountability and sign-off

**Account Manager Needs (Kimmy):**

**Pre-Quote Phase Tracking:**
"I was envisioning pre-booking, non-financial impact part, like the resource management, using those, perhaps it's the card, same as design, but the account managers need a similar tool."

**Integration Desire:**
"They're all connected, and we utilize the same resources, it's just ours happens before any of the design, before the PC, before the VM, and it'd be great to track it from the opportunity, all the way to the end."

**Sophistication Level Questions:**

**Matt's Question:**
"If they're going to build us something, Kimmy, we have to decide, is it the 10 phases or is it the 300 things that happen in each one of those phases? So 300 times 10."

**Management Perspective (Kimmy):**
"I don't want to manage all of that. That's the account manager's job to manage the individual details. From a manager perspective, like Wendy wanting to assign a PM, I want to know what phase of project they're at, the volume of those projects, and the timeline of those projects."

**Wendy's PM Perspective:**
"For PMs, I don't want to micro them, but I also want what the always are. And I want an acknowledgement sign off that they were done."

**Task Dependencies (Asana-Style):**

**Kimmy's Vision:**
"At Asana, when you complete a task, they're going to queue the next thing. And if that next thing is assigned to someone else, then they know now it's ready for them to go. Or it can be moved to them. I just like the idea of like this workflow where if you're waiting for someone, you know that you're waiting for someone else until it's your time to step up to play."

**Dealer Resistance (Marcus):**
"Every time we've proposed it to dealers, it was a little bit too much. They wanted more flexibility than that type of stringent project management."

**Suite Projects:**
NetSuite has native project management (Suite Projects) with task templates, resource assignment, skills matrix - but Marcus reports dealers don't want to use it.

**Wendy's Reaction:**
"It's so fascinating. I mean, we're literally, industry is project and budget management. And people don't want to use it. I know. What?"

**Employee Pushback Concern:**
"We obviously have non-process-driven people within our organization as well. Their pushback usually is, well, you hired me to do the job. Trust me to do the job. I don't need a list to tell me what my job is."

**Counter:**
"When we're busy, things can get lost."

**User Stories:**
- As Wendy (PM Manager), I need a real-time calendar view of PM workloads so that I can assign new projects without maintaining a manual Google Sheet
- As a PM, I need an automated task list when assigned to a project so that I know what activities I'm responsible for
- As Kimmy (Account Manager Leader), I need to track account manager workload in pre-quote phase so that I can balance assignments before projects even hit design
- As a Manager, I need to see high-level phases (not 300 tasks) so that I can manage without micromanaging
- As a PM, I need flexibility to manage my own details so that I don't feel micromanaged by excessive task tracking

**BRD Requirements:**
- [REQUIREMENT] Determine PM task list automation approach (ID: REQ-032, Type: Functional)
- [REQUIREMENT] Evaluate resource visualizer with calendar view (ID: REQ-033, Type: Functional)
- [REQUIREMENT] Determine task management sophistication level (ID: REQ-034, Type: Non-Functional)
- [FUNCTIONALITY] TBD - Requires design session
- [PRIORITY] Should-Have (impacts efficiency but requires more discovery)
- [DECISIONS] Additional session needed to design approach
- [RISK] Too much rigor = employee resistance; too little = things fall through cracks

**Stakeholder Impact:**
- **Primary Users**: Wendy (PM Manager), Kimmy (Account Manager Leader), PMs, Account Managers
- **Secondary Users**: All project resources
- **Approvers**: Matt/Mark (leadership)
- **Impacted Parties**: Entire operations and sales teams if full task management implemented

**Evidence:**
- "We'll definitely come back to that. So scheduling and resourcing... we'll have another session where we go a little bit deeper on this." - Marcus explicit decision for additional session
- All quotes above from various speakers
- "I've held off on rolling out a project management software until I fully understand what NetSuite's going to offer. So it's like, is NetSuite going to do it, or do I need to tackle the Asana build simultaneously?" - Wendy

**Confidence Rating**: 85% - Complex topic with clear needs expressed but no decisions made; explicitly deferred to additional session

**Outstanding Items:**
- **Additional session required** - see "Additional Sessions Needed"
- Decision on task management sophistication level
- Resource visualizer design
- Account manager pre-quote tracking approach
- Asana evaluation/comparison
- Task dependency workflow feasibility

---

## Section 12: External Vendor Bills & Time

### 15. How do external design contractors bill and how does their time impact projects?

**Answer:**
External design contractors (like Blue River) present a unique challenge. KBM does not issue POs for external design contractor work - they just bill and it comes through as a **G&A expense (consulting)**. However, their time is manually entered by Rafina (Design Manager) at KBM's standard internal rates, and that time (not the invoice) impacts project GP.

**Process for Contractors WITH Time Entry Access:**
1. Contractor has Core time-entry access
2. Contractor logs time directly into KBM system
3. Rafina reconciles: Compare time entered vs. invoice received
4. Ensure matching
5. Time impacts GP at standard rates
6. Invoice paid as consulting (G&A, no project impact)

**Process for Contractors WITHOUT Time Entry Access:**
1. Contractor works on project
2. Sends invoice (e.g., at $99/hour)
3. Invoice paid as "consulting" (GL code) - G&A expense
4. No job impact from invoice itself
5. Rafina manually enters time at KBM standard internal rate ($85/hour)
6. Only the manually entered time (at $85) impacts project GP
7. Difference ($99 - $85 = $14/hour) absorbed by KBM as G&A

**Why This Happens:**
"The outside contractors doesn't matter. The internal rate has stayed the same even if their hourly rate is more. That is a, we're understaffed, and so therefore KBM Hoag takes the hit."

**Matt's Reality Check:**
"I'll state for the record, we lose money on design. Design does not make money. No matter how much design we bill, our payroll costs more than what we were able to bill to a client at any point."

**Result:**
"So we don't hold them [to GP]. Otherwise, we'd have to put a negative GP on every order."

**Exception:**
"There are times where we will tag something to a project" - If contractor ends up doing labor/install (not design), then: Line added to SO, new PO issued for that line, cost of PO flows to project and impacts GP

**General Rule (Kipp):**
"In general, everything that is job-costed is going to be tagged to a PO, with the exception of design... Labor, PO. Storage, we issue a PO. Our copy suit, we issue a PO. Everything."

**User Stories:**
- As Rafina (Design Manager), I need to reconcile contractor time entry against invoices so that I ensure accuracy and prevent overbilling
- As Lorraine (CFO), I need design contractor costs in G&A (not project) so that project GP isn't artificially deflated by high contractor rates
- As a PM, I need to see design time allocated to my project so that I understand resource consumption even if cost stays in G&A

**BRD Requirements:**
- [REQUIREMENT] Support external contractor time entry with reconciliation workflow (ID: REQ-020, already captured)
- [REQUIREMENT] Configure consulting expense for contractor invoices (G&A, not project-costed)
- [ASSUMPTION] Rafina will continue manual time entry for contractors without system access
- [CONSTRAINT] Design contractor invoices do NOT impact project GP
- [PRIORITY] Must-Have
- [DECISIONS] Continue current process of separating invoice payment (G&A) from time impact (GP at standard rates)

**Stakeholder Impact:**
- **Primary Users**: Rafina (reconciliation), AP team (invoice payment)
- **Secondary Users**: External contractors, project teams
- **Approvers**: Lorraine (expense approval)

**Evidence:**
- "Some of our contractors, they have core time-entry access, because we can give them access to just time-entry." - Access model
- "The outside contractors doesn't matter. The internal rate has stayed the same even if their hourly rate is more. That is a, we're understaffed, and so therefore KBM Hoag takes the hit." - Why difference absorbed
- "They just bill us, and it comes through as a... GNA expense, consulting expense" - Invoice handling
- Matt's quote about design not making money
- Kipp's quote about everything else having POs

**Confidence Rating**: 95% - Clear process description with rationale

**Outstanding Items:**
- List of contractors who should have time entry access
- Reconciliation workflow details for Rafina
- Confirm if any design contractors should be handled differently

---

## Outstanding Items Summary

### High Priority Open Questions
1. **Damaged Product Write-Off Accounting** - How to handle zero-cost replacement lines and period-end reconciliation (Lorraine/Kipp to address)
2. **15% Labor Markup Exception Logic** - Complete rule set needed (Kipp action item)
3. **Rate Matrix** - Complete PM and design rates (Kipp/Wendy action item)
4. **Work Order Final Confirmation** - Wendy buy-in achieved but formal decision pending
5. **Scheduling & Resource Management Approach** - Requires dedicated session (see Additional Sessions)

### Medium Priority Open Questions
1. **Contractor Vendor Center Access List** - Which contractors need portal access
2. **Third-Party Warehouse Locations** - Complete list for bin setup
3. **Bin Naming Conventions** - Standard naming approach
4. **External Contractor Time Entry Access** - Which contractors get system access
5. **Floor Plan File Format** - Requirements for punch list pinning
6. **Report Format Examples** - Current PlanGrid reports for reference (Wendy action item)

### Future Considerations
1. **Contractor Direct Receiving** - Deferred to future phase, may revisit
2. **Suite Projects Evaluation** - NetSuite native project management capabilities
3. **Asana Integration** - Determine if NetSuite replaces need for Asana

### Training & Change Management Needs
1. **PM Field Service App Adoption** - Critical for PlanGrid replacement
2. **Contractor Vendor Center Adoption** - External party training
3. **Advanced Receiving Training** - Drag-and-drop mechanics, bin selection
4. **Work Order Creation Training** - For coordinators and PMs
5. **VRA Discipline** - Creating VRAs even when not shipping back

### Configuration Dependencies
1. **Third-Party Warehouse Location Setup** - Prerequisite for bin configuration
2. **Work Order Event Type Definition** - Complete list needed
3. **15% Markup Business Rules** - Complete logic before configuration
4. **Rate Matrix Setup** - All PM/design rates needed
5. **Contractor Access Provisioning** - List needed before go-live

---

*End of Questionnaire - Operations*





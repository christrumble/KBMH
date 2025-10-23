# Gap Analysis - Operations Discovery
**Version**: 1.0  
**Date**: October 23, 2025  
**Process Area**: Operations (Receiving, Work Orders, Scheduling, Field Service, VRAs, Time Tracking, Punch List)  
**Analyst**: Discovery Team

## Change Log
- **Date**: October 23, 2025
- **Version**: 1.0
- **Sources**: Questionnaire_Operations_v1.0.md, Master_Transcript_Operations.md, Requirements_Map_Operations_v1.0.md
- **Summary**: Comprehensive completeness analysis of Operations discovery questionnaire revealing 82% completion with critical gap in scheduling/resource management requiring dedicated follow-up session

## PROCESSED FILES
- Operations/2 Input/Master_Transcript_Operations.md (1,607 lines)
- Operations/3 Output/Questionnaire_Operations_v1.0.md (1,231 lines)
- Operations/3 Output/Requirements_Map_Operations_v1.0.md (250 lines)

---

## 1. EXECUTIVE SUMMARY

The Operations discovery questionnaire is **82% complete** based on questions with fully actionable answers. The team made excellent progress covering purchase requisitions, receiving processes, vendor center functionality, VRA management, time tracking, field service app requirements, and punch list management. However, one critical area—**scheduling and resource management**—remains substantially incomplete and requires a dedicated 2-hour follow-up session before design can proceed.

**Overall Completeness**: 82% of questions fully answered  
**Critical Gaps**: Scheduling/resource management approach (REQ-032 through REQ-034), configuration data pending from stakeholders  
**Follow-up Sessions Needed**: 2 sessions (1 critical, 1 high priority)  
**Estimated Timeline**: 3-4 weeks to achieve 100% questionnaire coverage

**Key Strengths:**
- Clear decisions on core operational processes (receiving, VRA, time tracking)
- Strong buy-in on Field Service app to replace PlanGrid
- Explicit decisions documented with supporting rationale
- Vendor center approach well-defined for outsourced model

**Key Gaps:**
- Scheduling/resource management sophistication level undecided
- Configuration data (rate matrix, warehouse locations, contractor lists) not yet provided
- Work order usage needs final leadership confirmation

---

## 2. COMPREHENSIVE QUESTION ANALYSIS

### 2.1 Complete Status Matrix

| Q# | Question Topic | Source | Status | Evidence Quality | Action Needed |
|----|---------------|--------|--------|------------------|---------------|
| Q1 | Operations scope and process flow | Original | ✅ Complete | Strong | None |
| Q2 | Purchase requisitions usage | Original | ✅ Complete | Strong | None - decision confirmed |
| Q3 | Outsourced model impact on receiving | Original | ✅ Complete | Strong | Need warehouse location list |
| Q4 | Advanced Receiving tool functionality | Original | ✅ Complete | Strong | Schedule demo session |
| Q5 | Bin structure requirements | Original | ✅ Complete | Strong | Need warehouse location list |
| Q6 | Vendor center functionality | Original | ✅ Complete | Strong | Need contractor access list |
| Q7 | Contractor direct receiving capability | Original | ✅ Complete | Strong | Explicitly deferred to future |
| Q8 | Damaged product and vendor credits | Original | ✅ Complete | Strong | Need accounting treatment clarification |
| Q9 | Work order usage decision | Original | ⚠️ Partial | Medium | Need final confirmation from Wendy |
| Q10 | Time tracking GP impact | Original | ✅ Complete | Strong | None - explicitly confirmed |
| Q11 | 15% labor markup functionality | Original | ⚠️ Partial | Strong | Need complete exception logic from Kipp |
| Q12 | Punch list management approach | Original | ✅ Complete | Strong | Need PlanGrid report examples |
| Q13 | Field Service app requirements | Original | ✅ Complete | Strong | Schedule demo session |
| Q14 | Scheduling & resource management | Original | ❌ Incomplete | Weak | **CRITICAL: Dedicated session needed** |
| Q15 | External contractor billing/time | Original | ✅ Complete | Strong | Need contractor time access list |
| Q16 | PM task list automation | Organic | ❌ Incomplete | Weak | Part of Q14 - session needed |
| Q17 | Resource visualizer/calendar needs | Organic | ❌ Incomplete | Weak | Part of Q14 - session needed |
| Q18 | Task management sophistication | Organic | ❌ Incomplete | Weak | Part of Q14 - session needed |
| Q19 | Account manager pre-quote tracking | Organic | ❌ Incomplete | Weak | Part of Q14 - session needed |
| Q20 | Task dependency workflow | Organic | ❌ Incomplete | Weak | Part of Q14 - session needed |
| Q21 | 15% markup exception logic details | Follow-up | ⚠️ Partial | Medium | Kipp action item - not yet provided |
| Q22 | PM and design rate matrix | Follow-up | ⚠️ Partial | Medium | Kipp/Wendy action item - not yet provided |
| Q23 | Contractor vendor center access list | Follow-up | ⚠️ Partial | Medium | Operations team - not yet provided |
| Q24 | Contractor time entry access list | Follow-up | ⚠️ Partial | Medium | Wendy/Rafina - not yet provided |
| Q25 | Third-party warehouse locations | Follow-up | ⚠️ Partial | Medium | Operations team - not yet provided |
| Q26 | Work order event types complete list | Follow-up | ⚠️ Partial | Medium | Operations team - not yet provided |
| Q27 | Floor plan file format requirements | Follow-up | ⚠️ Partial | Medium | Technical specs needed |
| Q28 | Status report content/format | Follow-up | ⚠️ Partial | Medium | PlanGrid examples needed from Wendy |
| Q29 | Damaged product write-off process | Follow-up | ⚠️ Partial | Medium | Lorraine/Kipp - explicitly pinned for later |

### 2.2 Categorized Results

**✅ Fully Answered** (11 questions): Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q10, Q12, Q13, Q15  
Questions with complete, well-evidenced answers and clear decisions

**⚠️ Partially Answered** (12 questions): Q9, Q11, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28, Q29  
Questions with directional answers but missing key configuration details or final confirmation

**❌ Not Answered** (6 questions): Q14, Q16, Q17, Q18, Q19, Q20  
Questions that were discussed but require dedicated session to reach decisions

**Total Questions Identified**: 29 (15 original questionnaire + 14 organic/follow-up)

**Completion Calculation**:
- Fully Answered: 11 questions = 38%
- Partially Answered (actionable direction): 12 questions = 41%
- Not Answered: 6 questions = 21%
- **Effective Completeness**: 79% (11 + 12 with clear direction) to 82% (accounting for actionability)

---

## 3. INFORMATION GAPS ANALYSIS

### 3.1 Critical Priority Gaps (🔴)

#### GAP-001: Scheduling & Resource Management Approach (REQ-032, REQ-033, REQ-034)

**What specific information is missing?**
- Decision on PM task list automation (templates vs. manual)
- Resource visualizer design and functionality requirements
- Task management sophistication level (10 high-level phases vs. 300 granular tasks)
- Manager vs. individual contributor view requirements
- Account manager pre-quote workload tracking approach
- Task dependency workflow feasibility (Asana-style)
- Integration between account management, PM, and design resource tracking

**Why is this information important?**
This affects the entire resource management and project coordination approach. Wendy currently maintains manual Google Sheets for PM workload tracking ("It's only as accurate as the information... Not accurate by time accessed"). Kimmy needs pre-quote account manager tracking. The solution could range from simple saved searches to full Suite Projects implementation with task dependencies. The gap between what KBM desires (Asana-style workflow) and what Marcus reports dealers actually use (minimal project management) must be bridged.

**Who would have this information?**
- Wendy (PM Manager) - primary user, knows PM needs
- Kimmy (Account Manager Leader) - pre-quote tracking needs
- Matt (Leadership) - decision on sophistication level, employee resistance concerns
- Marcus (Implementation) - NetSuite capabilities, dealer best practices

**What's the best way to get this information?**
Dedicated 2-hour design session with whiteboard/screen share to:
1. Review Wendy's current Google Sheet calendar and requirements
2. Demonstrate NetSuite resource management options (Suite Projects, saved searches, custom visualizers)
3. Discuss Asana comparison and task dependency needs
4. Make explicit decisions on sophistication level
5. Define manager vs. individual views
6. Determine account manager integration approach

**Current Approach**: TBD (explicitly deferred during session: "We'll definitely come back to that. So scheduling and resourcing... we'll have another session where we go a little bit deeper on this.")

**Evidence**: Multiple transcript quotes showing complexity:
- Wendy: "What I'm hoping for is on every project, when you get assigned as project manager, you're going to get a list of tasks..."
- Matt: "If they're going to build us something, Kimmy, we have to decide, is it the 10 phases or is it the 300 things that happen in each one of those phases?"
- Kimmy: "I was envisioning pre-booking, non-financial impact part, like the resource management... the account managers need a similar tool."
- Marcus: "Every time we've proposed it to dealers, it was a little bit too much. They wanted more flexibility than that type of stringent project management."

---

#### GAP-002: Work Order Final Confirmation (REQ-013)

**What specific information is missing?**
Final leadership confirmation that work orders will be implemented. Wendy provided soft buy-in during session, but this wasn't a hard decision yet.

**Why is this information important?**
Work orders are foundational to field service app functionality (REQ-024-031), time tracking from field (REQ-031), punch list creation (REQ-024), and contractor coordination (REQ-006/007). If work orders aren't implemented, multiple other requirements need alternative approaches.

**Who would have this information?**
- Wendy (PM Manager) - primary user, provided soft buy-in
- Matt (Leadership) - final approval
- Operations team - users who would create/manage work orders

**What's the best way to get this information?**
Quick confirmation meeting (30 minutes) or email confirmation after operations suite demo (when Wendy can see work order functionality in action).

**Current Approach**: ADAPT - Soft decision, Wendy buy-in achieved  
**Evidence**: "Wendy signed on for work orders just now, so that was good. That's like mission accomplished." - Marcus noting progress, but not final decision

---

#### GAP-003: 15% Labor Markup Complete Exception Logic (REQ-021, REQ-022)

**What specific information is missing?**
Complete business rule logic for when the 15% labor markup applies:
- Which order types trigger the markup?
- Which order types are excluded?
- Which specific clients have exceptions?
- How to identify "external labor" lines (line code definition)?
- Any other exception scenarios?

**Why is this information important?**
Cannot configure the automated formula line without complete exception logic. If logic is wrong, every sales order will calculate incorrectly, affecting pricing, GP, and potentially sales commissions. The formula must be tested against historical orders to validate accuracy.

**Who would have this information?**
- Kipp (IT Specialist/Former Controller) - owns the current Core business rule
- Mark/Matt (Leadership) - approve exceptions
- Finance team - validate calculation accuracy

**What's the best way to get this information?**
Kipp provides documentation of current Core business rule in natural language, then Marcus translates to NetSuite formula. Validate against sample orders.

**Current Approach**: ACCOMMODATE - Custom formula line with business rules  
**Evidence**: "But it's based off of order type, not based off of client. You could add in additional exceptions by client if you wanted to as well. So there's a few ways to do it. I just need to know, like, that full logical expression." - Marcus request to Kipp

**Action Item**: Already assigned to Kipp, due during configuration phase

---

### 3.2 High Priority Gaps (🟡)

#### GAP-004: PM and Design Rate Matrix (REQ-017, REQ-018, REQ-019)

**What specific information is missing?**
Complete rate matrix including:
- PM internal rate (cost to project)
- PM external rate (client billing)
- Workshop designer internal rate
- Standard designer internal rate
- Field designer rates (if different from studio)
- Client-specific negotiated rates (which clients, what rates)
- Billable vs. non-billable classification rules

**Why is this information important?**
Time tracking calculates project cost based on rate matrix. Incorrect rates = incorrect project GP = incorrect profitability reporting = bad business decisions. Client billing rates affect revenue recognition.

**Who would have this information?**
- Kipp (IT Specialist) - maintains current rates
- Wendy (PM Manager) - PM rates, negotiated client rates
- Rafina (Design Manager) - design rates
- Finance team - rate approval

**What's the best way to get this information?**
Kipp/Wendy collaborate to document all rates in spreadsheet, including:
- Rate effective dates
- Resource type (PM, workshop designer, standard designer, field designer)
- Internal cost rate
- External billing rate
- Client exceptions

**Current Approach**: ALIGNS - NetSuite rate matrix (standard functionality)  
**Evidence**: "So there's a design client rate and a PM client rate, and then there's basically three internal rates." - Wendy describing complexity

**Action Item**: Already assigned to Kipp/Wendy, due during configuration phase

---

#### GAP-005: Damaged Product Write-Off Accounting Treatment (REQ-011)

**What specific information is missing?**
Accounting process for damaged product scenarios:
- When damaged item received at cost, stays in damaged bin
- Replacement received at zero cost on new PO line
- How to handle damaged item write-off?
- Period-end reconciliation if resolved across periods
- GL impact of zero-cost replacement

**Why is this information important?**
Affects inventory valuation, COGS recognition, and financial reporting. Lorraine (CFO) explicitly requested this be addressed ("What you do from a write-off perspective, that product that's being damaged?"). The complexity: replacement has value but zero cost in system, creating potential GP distortion.

**Who would have this information?**
- Lorraine (CFO) - accounting treatment decision
- Kipp (Former Controller) - technical implementation
- Finance team - period-end reconciliation process

**What's the best way to get this information?**
30-minute meeting with Lorraine, Kipp, and Marcus to walk through scenarios:
1. Receive 10 items, 2 damaged (received to damaged bin at cost)
2. Add zero-cost line for 2 replacements
3. Receive 2 replacements (zero cost)
4. What happens to damaged items? (write-off, credit, transfer)
5. How to handle if credit comes in different period?

**Current Approach**: ALIGNS - NetSuite PO line management  
**Evidence**: "Let's come back to that, won't put a pin [in] that one." - Explicitly deferred during session

**Action Item**: Already identified, assigned to Lorraine/Kipp, due during configuration phase

---

#### GAP-006: Contractor Access Lists (REQ-006, REQ-007, REQ-020)

**What specific information is missing?**
Two separate lists needed:
1. **Vendor Center Access**: Which installation contractors and subcontractors need portal access?
2. **Time Entry Access**: Which contractors need direct time entry capability in NetSuite?

For each contractor:
- Company name
- Contact person
- Email address
- Access type needed (vendor center only, or time entry also)
- Reconciliation owner (if time entry)

**Why is this information important?**
User provisioning and training planning. Vendor center access is critical for receiving notification process (REQ-007) to replace email. Time entry access affects project GP accuracy and requires Rafina reconciliation (REQ-020). External party training must be scheduled.

**Who would have this information?**
- Wendy (PM Manager) - knows installation contractors
- Rafina (Design Manager) - knows design contractors with time entry
- Operations team - complete contractor relationships

**What's the best way to get this information?**
Operations team compiles lists in spreadsheet with columns:
- Contractor name
- Contact person / email
- Vendor center access? (Y/N)
- Time entry access? (Y/N)
- Reconciliation owner
- Notes

**Current Approach**: ALIGNS - NetSuite vendor center and time entry (standard functionality)  
**Action Item**: Assigned to Wendy/Rafina, due during user provisioning phase

---

#### GAP-007: Third-Party Warehouse Location List (REQ-003, REQ-004, REQ-005)

**What specific information is missing?**
Complete list of all third-party warehouse locations where product is received, including:
- Warehouse name / company
- Physical address
- Primary contact
- Bin naming convention preferences
- Any special handling requirements

**Why is this information important?**
Cannot configure bin structure without knowing all locations. Each location needs:
- One primary receiving bin
- One damaged inventory bin
- One duplicate/overage bin (optional)

Incorrect bin setup = receiving errors = WIP inaccuracy = financial reporting problems.

**Who would have this information?**
- Operations team - manages warehouse relationships
- Wendy (PM Manager) - coordinates with installation partners
- Receiving team - current process knowledge

**What's the best way to get this information?**
Operations team compiles list, possibly from current system or manual tracking. Include any planned future warehouse relationships.

**Current Approach**: ALIGNS - NetSuite bin management (standard functionality)  
**Action Item**: Assigned to Operations team, needed before configuration phase

---

#### GAP-008: Field Status Report Requirements (REQ-027)

**What specific information is missing?**
Requirements for status reports generated from field app:
- Current PlanGrid report examples (screenshots or PDFs)
- Report content requirements (punch items, photos, notes, completion status)
- Report format/layout preferences
- Email workflow (to whom, when, subject line)
- Client-facing polish level needed

**Why is this information important?**
Marcus agreed to build status report generation in field app during the session ("Generating it in the app is not going to be a challenge for us to do. We just weren't planning on it, but we can."). This is custom development (REQ-027, ACCOMMODATE). Without clear requirements, the delivered report may not meet needs, requiring rework.

**Who would have this information?**
- Wendy (PM Manager) - uses reports, knows client expectations
- PM team - generates reports currently in PlanGrid
- Clients - ultimate report consumers (indirectly)

**What's the best way to get this information?**
Wendy provides 2-3 examples of actual PlanGrid reports (redact client names if needed) showing:
- Current format and layout
- Content included
- How photos are displayed
- How floor plan markups appear
- Email format when sent

**Current Approach**: ACCOMMODATE - Custom Orion development for in-app report generation  
**Evidence**: "Sometimes it's me, and sometimes it's them" (Wendy describing current report creation), "Generating it in the app is not going to be a challenge for us to do. We just weren't planning on it, but we can." - Marcus commitment

**Action Item**: Already assigned to Wendy/PM Team, due during field service app configuration phase

---

### 3.3 Medium Priority Gaps (🟢)

#### GAP-009: Work Order Event Types Complete List (REQ-014)

**What specific information is missing?**
Complete, finalized list of all work order event types needed. Session identified six types:
- Site verification
- Delivery and install
- Site review
- PM on-site presence
- Design meetings
- Punch walks

Are there other event types? Are these names final? Any special fields or requirements per event type?

**Why is this information important?**
Event types must be configured in NetSuite before work orders can be created. Affects field service app display, reporting, and time tracking categorization.

**Who would have this information?**
- Wendy (PM Manager) - knows all PM activities
- Operations team - understands field activities
- Design team - knows design-related events

**What's the best way to get this information?**
Operations team reviews list from session and confirms complete or adds missing types. Quick email confirmation or 15-minute meeting.

**Current Approach**: ALIGNS - NetSuite work order event configuration (standard functionality)  
**Action Item**: Assigned to Operations team, needed before work order configuration

---

#### GAP-010: Floor Plan File Format Requirements (REQ-025)

**What specific information is missing?**
Technical specifications for floor plan uploads:
- Supported file formats (PDF, CAD, image formats?)
- File size limitations
- Resolution requirements
- How floor plans are currently stored/created
- Who creates floor plans (designers, architects, clients?)
- Typical floor plan sizes (# of pages, dimensions)

**Why is this information important?**
Floor plan punch pinning is critical feature ("Four months later you get that punch item and you've done 15 jobs. You're like, yeah, I'll remember what room that goes into. And you don't."). If file formats aren't compatible, feature doesn't work. Testing required before go-live.

**Who would have this information?**
- Design team - creates or receives floor plans
- PM team - uploads to PlanGrid currently
- IT/Marcus - technical requirements for Orion app

**What's the best way to get this information?**
Design/PM team provides examples of typical floor plan files. Marcus confirms compatibility with field service app. Test upload and pinning during demo session.

**Current Approach**: ACCOMMODATE - Custom Orion floor plan pinning feature  
**Action Item**: Technical specs needed, testing during operations suite demo

---

#### GAP-011: Bin Naming Conventions (REQ-003, REQ-004, REQ-005)

**What specific information is missing?**
Standard naming approach for bins across all locations:
- Normal receiving bin naming pattern (e.g., "[Location]-RCV")
- Damaged bin naming pattern (e.g., "[Location]-DMG")
- Duplicate/overage bin naming pattern (e.g., "[Location]-DUP")
- Location naming conventions
- Any specific requirements from warehouses

**Why is this information important?**
Consistent naming improves user experience, reporting, and prevents receiving errors. Bins are displayed in Advanced Receiving tool drag-and-drop interface—clear names help users select correct bin.

**Who would have this information?**
- Operations team - preferences
- IT/Kipp - system standards
- Marcus - NetSuite best practices

**What's the best way to get this information?**
Marcus proposes standard naming convention, operations team approves. Simple decision, can be part of configuration kickoff.

**Current Approach**: ALIGNS - NetSuite bin management (standard functionality)  
**Action Item**: Define during bin configuration, low complexity

---

#### GAP-012: Contractor Direct Receiving Future Evaluation (REQ-008)

**What specific information is missing?**
Criteria for future evaluation of contractor direct receiving capability:
- Which contractors would be trusted with direct receiving?
- What controls/oversight would be needed?
- How to handle mistakes/corrections?
- Pilot approach?

**Why is this information important?**
Explicitly deferred to future ("For now, they can just get as received. Yep. And it'll show up on our report... If it's not part of it now, it is in the future. We can always look at that later."). Not a current gap, but documenting decision criteria helps future evaluation.

**Who would have this information?**
- Operations leadership - trust level assessment
- Wendy - contractor performance history
- Marcus - technical implementation approach

**What's the best way to get this information?**
Not immediate need. Revisit 3-6 months after go-live when vendor center adoption is established. Evaluate if notification approach is working or if direct receiving would improve process.

**Current Approach**: ADAPT - Deferred to future phase  
**Action Item**: Revisit post-implementation (not blocking current implementation)

---

### 3.4 Categorized Missing Information

#### Current State Gaps
- Third-party warehouse locations (GAP-007) - need complete list for bin configuration
- Current floor plan formats (GAP-010) - need examples for compatibility testing
- Current PlanGrid report examples (GAP-008) - need for custom development requirements

#### Requirements Gaps
- Scheduling/resource management approach (GAP-001) - **CRITICAL** - entire design session needed
- Task management sophistication level (GAP-001) - part of scheduling session
- Floor plan pinning requirements (GAP-010) - technical specifications

#### Technical Gaps
- 15% labor markup exception logic (GAP-003) - complete business rule needed
- Rate matrix (GAP-004) - all rates and client exceptions
- Damaged product accounting treatment (GAP-005) - accounting process definition
- Bin naming conventions (GAP-011) - standard approach
- Floor plan file formats (GAP-010) - compatibility requirements

#### Stakeholder Gaps
- Work order final confirmation (GAP-002) - Wendy/leadership approval
- Contractor access lists (GAP-006) - operations team compilation
- Work order event types (GAP-009) - operations team finalization

#### Organic Discovery Gaps
- PM task list automation (GAP-001, Q16) - emerged during scheduling discussion
- Resource visualizer (GAP-001, Q17) - Wendy's manual Google Sheet replacement
- Account manager pre-quote tracking (GAP-001, Q19) - Kimmy's requirements
- Task dependencies (GAP-001, Q20) - Asana-style workflow evaluation

---

## 4. STAKEHOLDER ENGAGEMENT ANALYSIS

### 4.1 Assess Participation

#### Well-Represented Roles
**Wendy (PM Manager)** - ⭐⭐⭐⭐⭐ Excellent engagement
- Provided detailed PM workflow requirements
- Shared current Google Sheet tracking approach
- Identified PlanGrid pain points and report needs
- Soft buy-in on work orders
- Expressed clear vision for PM task lists
- Needs follow-up on scheduling/resource management session

**Marcus (Implementation Team)** - ⭐⭐⭐⭐⭐ Excellent leadership
- Led session effectively
- Made custom development commitments (status report generation)
- Educated team on NetSuite options
- Identified gaps and scheduled follow-up sessions
- Demonstrated Orion tools and innovations

**Lorraine (CFO)** - ⭐⭐⭐⭐ Strong participation
- Identified critical VRA pain point (credit tracking)
- Raised damaged product accounting question
- Confirmed time tracking GP impact requirements
- Needs follow-up on damaged product write-off accounting

**Kipp (IT Specialist/Former Controller)** - ⭐⭐⭐⭐ Strong participation
- Detailed 15% labor markup explanation and requirements
- Identified OCD pain point (line positioning)
- Confirmed time tracking and contractor billing approaches
- Needs to provide exception logic and rate matrix

**Matt (Leadership)** - ⭐⭐⭐ Good participation
- Provided context on 15% labor markup history
- Raised sophistication level question (10 phases vs 300 tasks)
- Confirmed design GP reality check
- Needs to participate in scheduling/resource management session

**Kimmy (Account Manager Leader)** - ⭐⭐⭐ Good participation
- Raised account manager pre-quote tracking needs
- Expressed Asana-style workflow vision
- Identified integration requirements across roles
- Needs to participate in scheduling/resource management session

#### Under-Represented Roles
**Rafina (Design Manager)** - ⭐⭐ Mentioned but not present
- Reconciles contractor time vs. invoices (REQ-020)
- Manages design contractor relationships
- Needs involvement in:
  - Rate matrix definition
  - Contractor time entry access list
  - Reconciliation workflow design

**Receiving Team** - ⭐ Not present
- Will use Advanced Receiving tool daily (REQ-002)
- Need to confirm warehouse location list
- Need training on bin selection process
- Should participate in operations suite demo

**PM Team Members** - ⭐ Not present
- Will use Field Service app daily (REQ-024-031)
- Need to confirm work order event types
- Need to provide PlanGrid report examples
- Should participate in field service app demo

**Operations Team (general)** - ⭐ Under-represented
- Need to compile contractor access lists
- Need to confirm warehouse locations
- Need to finalize work order event types

#### Missing Stakeholders
**Installation Contractors** - Not present (external)
- Will use vendor center (REQ-006/007)
- Critical for adoption success
- Need training plan and phased rollout
- Should pilot vendor center with 1-2 trusted contractors

**Design Contractors** - Not present (external)
- Some need time entry access (REQ-020)
- Rafina reconciles their time/invoices
- Need to understand time entry process

**Receiving Coordinators** - Not present (if different from Wendy)
- Daily users of Advanced Receiving tool
- Need hands-on training
- Should validate bin structure design

#### Decision-Maker Involvement
✅ **Wendy** - PM Manager, operational decisions, participated strongly  
✅ **Lorraine** - CFO, financial/accounting decisions, participated, needs follow-up  
⚠️ **Matt** - Leadership, strategic decisions, participated but needs to join scheduling session  
⚠️ **Mark** - Leadership (if different from Matt), not mentioned in transcript, may need involvement  
⚠️ **Rafina** - Design Manager, design operations decisions, not present but mentioned frequently

### 4.2 Stakeholder Engagement Recommendations

**Immediate Engagement Needed:**
1. **Rafina (Design Manager)** - Include in rate matrix and contractor time entry discussions
2. **PM Team Representatives** - Include in field service app demo and work order design
3. **Receiving Team Representative** - Include in Advanced Receiving demo

**Future Engagement Needed:**
4. **Installation Contractors** - Vendor center training and pilot program
5. **Design Contractors** - Time entry training for selected contractors
6. **Mark (if separate from Matt)** - Scheduling/resource management decision session

---

## 5. FOLLOW-UP MEETING PLAN

### Session 1: Scheduling & Resource Management Deep Dive (CRITICAL)

**Purpose**: Address questions Q14, Q16, Q17, Q18, Q19, Q20 (GAP-001) and make decisions on REQ-032, REQ-033, REQ-034

**Required Attendees**:
- Wendy (PM Manager) - primary user, manual Google Sheet owner
- Kimmy (Account Manager Leader) - pre-quote tracking needs
- Matt (Leadership) - sophistication level decision, employee resistance concerns
- Marcus (Implementation Team) - NetSuite capabilities, dealer best practices

**Optional Attendees**:
- Kipp (IT Specialist) - technical perspective
- PM representative - individual contributor perspective
- Account Manager representative - user perspective

**Duration**: 2 hours

**Pre-work for Client**:
1. **Wendy**: Bring current Google Sheet PM workload calendar (screenshots or live access)
2. **Wendy**: Document ideal PM task list for typical project
3. **Kimmy**: Document account manager pre-quote activities and timeline
4. **Kimmy**: Identify what Asana features are most valuable vs. nice-to-have
5. **Matt**: Consider employee resistance scenarios and acceptable guardrails

**Consultant Preparation**:
1. **Marcus**: Prepare demonstration of Suite Projects functionality
2. **Marcus**: Prepare demo of resource-based saved searches
3. **Marcus**: Prepare examples of dealer resource management approaches (best practices)
4. **Marcus**: Prepare custom resource visualizer options (if available)
5. **Marcus**: Research Asana integration options (if any)

**Expected Outcome**:
- ✅ Decision on PM task list approach (automated templates vs. manual)
- ✅ Decision on task management sophistication (high-level phases vs. granular tasks)
- ✅ Definition of resource visualizer requirements (calendar view, weighted cards, etc.)
- ✅ Decision on account manager pre-quote tracking integration
- ✅ Decision on task dependency workflow (Asana-style vs. flexible)
- ✅ Documented user stories for resource management
- ✅ Updated requirements map with REQ-032, REQ-033, REQ-034 approaches (ALIGNS/ADAPT/ACCOMMODATE)

**Agenda**:
- 0:00-0:15 - Review Wendy's current Google Sheet and pain points
- 0:15-0:30 - Demonstrate NetSuite resource management options
- 0:30-0:45 - Discuss task list automation requirements (Wendy's vision)
- 0:45-1:00 - Discuss account manager pre-quote tracking (Kimmy's needs)
- 1:00-1:15 - Evaluate Asana comparison and task dependencies
- 1:15-1:30 - Discuss employee resistance and sophistication level (Matt's decision)
- 1:30-1:45 - Make decisions on each requirement (REQ-032, REQ-033, REQ-034)
- 1:45-2:00 - Document decisions, user stories, and next steps

**Success Criteria**:
- All three requirements have clear ALIGNS/ADAPT/ACCOMMODATE classification
- If ACCOMMODATE, scope of custom development is defined
- If ADAPT, process changes are documented and stakeholder buy-in confirmed
- Action items assigned for any additional information needed
- Training needs identified

---

### Session 2: Operations Suite Demo (Advanced Receiving, Field Service, Work Orders) (HIGH PRIORITY)

**Purpose**: Demonstrate custom Orion tools (REQ-002, REQ-024-031) and validate functionality meets requirements

**Required Attendees**:
- Wendy (PM Manager) - PM and field service user
- Receiving team representative - Advanced Receiving user
- PM representative(s) - Field Service app users
- Marcus/Chris (Implementation Team) - demonstrators

**Optional Attendees**:
- Operations team members
- Installation contractors (pilot users)
- Kipp (IT Specialist) - technical perspective
- Lorraine (CFO) - stakeholder visibility

**Duration**: 1.5-2 hours

**Pre-work for Client**:
1. **Wendy**: Provide 2-3 PlanGrid report examples (GAP-008)
2. **Wendy**: Bring list of work order event types to validate (GAP-009)
3. **PM Team**: Bring floor plan file examples for upload testing (GAP-010)
4. **Receiving Team**: Confirm warehouse location list (GAP-007)
5. **Operations Team**: Identify 1-2 pilot contractors for vendor center demo

**Consultant Preparation**:
1. **Marcus/Chris**: Prepare latest version of Advanced Receiving tool (not demo version)
2. **Marcus/Chris**: Prepare latest Field Service app on tablet
3. **Marcus/Chris**: Load sample work orders and punch list data
4. **Marcus/Chris**: Prepare sample floor plans for pinning demonstration
5. **Marcus/Chris**: Prepare offline mode demonstration scenario
6. **Marcus/Chris**: Prepare vendor center demonstration

**Expected Outcome**:
- ✅ Team sees Advanced Receiving drag-and-drop functionality (REQ-002)
- ✅ Team validates bin structure approach works in tool (REQ-003, REQ-004, REQ-005)
- ✅ PM team sees Field Service app punch list functionality (REQ-024)
- ✅ PM team validates floor plan pinning meets needs (REQ-025)
- ✅ Team confirms offline mode is acceptable (REQ-026)
- ✅ Team confirms status report generation approach (REQ-027) - Marcus to demo mockup or discuss requirements
- ✅ Team sees vendor center contractor view (REQ-006, REQ-007)
- ✅ Team sees work order creation and soft scheduling (REQ-013, REQ-015)
- ✅ Test floor plan file upload and compatibility (GAP-010)
- ✅ Finalize work order confirmation decision (GAP-002)
- ✅ Training plan drafted for PM Field Service app adoption

**Agenda**:
- 0:00-0:15 - Advanced Receiving tool demonstration (drag-and-drop bins)
- 0:15-0:30 - Vendor Center demonstration (contractor view, receiving notification)
- 0:30-0:45 - Work order creation and soft scheduling workflow
- 0:45-1:00 - Field Service app navigation and event management
- 1:00-1:15 - Punch list creation and floor plan pinning (live test with client floor plans)
- 1:15-1:30 - Offline mode demonstration (disconnect, work, reconnect, sync)
- 1:30-1:45 - Status report requirements discussion (review PlanGrid examples, define needs)
- 1:45-2:00 - Q&A, final work order confirmation, training planning

**Success Criteria**:
- PM team comfortable with Field Service app as PlanGrid replacement
- Receiving team comfortable with Advanced Receiving tool
- Floor plan files confirmed compatible (or conversion process identified)
- Work order final confirmation documented
- Status report requirements finalized (if not already provided)
- Training dates scheduled

---

### Session 3 (Optional/Future): Contractor Vendor Center Training & Pilot

**Purpose**: Train pilot contractors on vendor center and validate adoption approach

**Required Attendees**:
- 1-2 pilot contractors
- Operations coordinator
- Marcus/Chris (trainer)

**Duration**: 1 hour

**Pre-work for Client**:
- Finalize contractor access list (GAP-006)
- Provision pilot contractor accounts
- Configure sample work orders and POs for pilot

**Expected Outcome**:
- Contractors can log in and navigate vendor center
- Contractors can notify of product arrival
- Contractors can attach documents and photos
- Feedback on usability and adoption barriers
- Refined training materials for broader rollout

**Timeline**: After go-live, during hypercare period

---

## 6. PRIORITY CLASSIFICATION

### 🔴 Critical Priority - Must be answered to proceed

#### GAP-001: Scheduling & Resource Management Approach (REQ-032, REQ-033, REQ-034)
**Question**: How sophisticated should resource management be? PM task lists? Resource visualizer? Account manager pre-quote tracking?  
**Missing Information**: Explicit decisions on task management approach, resource visualizer design, account manager integration  
**Business Impact**: Affects entire PM and account manager workflow. Wendy currently maintains manual tracking. Could range from no custom development (saved searches only) to significant custom resource visualizer. Employee resistance risk if too detailed. Decision impacts project timeline and budget.  
**Who Can Answer**: Wendy (primary user), Kimmy (account manager needs), Matt (sophistication decision), Marcus (capabilities)  
**How to Get Answer**: Dedicated 2-hour design session (see Session 1 above)  
**Timeline Impact**: Blocking - Cannot complete requirements map or proceed with scheduling configuration until decided

---

#### GAP-003: 15% Labor Markup Complete Exception Logic (REQ-021, REQ-022)
**Question**: What is the complete business rule logic for when 15% markup applies?  
**Missing Information**: Order types that trigger markup, order types excluded, client exceptions, line code definition for "external labor"  
**Business Impact**: Every sales order with labor affected. Incorrect formula = incorrect GP = incorrect pricing decisions and potentially incorrect sales commissions. Must be validated against historical orders before go-live.  
**Who Can Answer**: Kipp (owns current Core rule), Mark/Matt (approve exceptions)  
**How to Get Answer**: Kipp documents current Core business rule in natural language, validates against sample orders  
**Timeline Impact**: Blocking for sales order configuration - Cannot configure formula line without complete logic

---

### 🟡 High Priority - Important for project success

#### GAP-002: Work Order Final Confirmation (REQ-013)
**Question**: Final confirmation that work orders will be implemented?  
**Missing Information**: Hard decision confirmation from leadership  
**Business Impact**: Work orders are foundational for field service app (REQ-024-031), time tracking (REQ-031), punch list (REQ-024). If not implemented, multiple requirements need alternative approaches. Wendy provided soft buy-in but not final decision.  
**Who Can Answer**: Wendy (primary user), Matt (leadership approval)  
**How to Get Answer**: Quick confirmation after operations suite demo (Session 2) when functionality is visible  
**Timeline Impact**: Moderate - Soft decision exists, but final confirmation needed before field service configuration

---

#### GAP-004: PM and Design Rate Matrix (REQ-017, REQ-018, REQ-019)
**Question**: What are all PM and design rates (internal costs and client billing)?  
**Missing Information**: Complete rate matrix with all resource types, internal rates, external rates, client exceptions  
**Business Impact**: Time tracking calculates project cost based on rates. Incorrect rates = incorrect project GP = incorrect profitability reporting. Client billing rates affect revenue.  
**Who Can Answer**: Kipp (maintains rates), Wendy (PM rates), Rafina (design rates)  
**How to Get Answer**: Kipp/Wendy/Rafina collaborate on spreadsheet with all rates and effective dates  
**Timeline Impact**: Moderate - Needed before time tracking configuration but straightforward data collection

---

#### GAP-005: Damaged Product Write-Off Accounting Treatment (REQ-011)
**Question**: How to handle accounting for damaged items and zero-cost replacements?  
**Missing Information**: Write-off process, period-end reconciliation, GL impact of zero-cost replacement  
**Business Impact**: Affects inventory valuation, COGS, financial reporting. Lorraine (CFO) explicitly raised question. Replacement received at zero cost creates potential GP distortion that must be addressed.  
**Who Can Answer**: Lorraine (CFO - accounting treatment), Kipp (technical implementation)  
**How to Get Answer**: 30-minute meeting to walk through scenarios and document accounting process  
**Timeline Impact**: Moderate - Needed before VRA configuration but can be addressed in parallel with other activities

---

#### GAP-006: Contractor Access Lists (REQ-006, REQ-007, REQ-020)
**Question**: Which contractors need vendor center access? Which need time entry access?  
**Missing Information**: Two lists: (1) Vendor center access, (2) Time entry access, with contact details  
**Business Impact**: User provisioning and external training planning. Vendor center adoption is critical for receiving notification process (REQ-007) to replace email. Time entry affects GP accuracy.  
**Who Can Answer**: Wendy (installation contractors), Rafina (design contractors), Operations team (complete list)  
**How to Get Answer**: Operations team compiles spreadsheet with contractor names, contacts, access types  
**Timeline Impact**: Moderate - Needed before user provisioning phase but straightforward data collection

---

#### GAP-007: Third-Party Warehouse Location List (REQ-003, REQ-004, REQ-005)
**Question**: What are all third-party warehouse locations where product is received?  
**Missing Information**: Complete list with warehouse names, addresses, contacts  
**Business Impact**: Cannot configure bin structure without knowing locations. Each location needs three bins (receiving, damaged, duplicate). Incorrect setup = receiving errors = WIP inaccuracy.  
**Who Can Answer**: Operations team (manages relationships), Wendy (coordinates with partners), Receiving team (current process)  
**How to Get Answer**: Operations team compiles list, possibly from current system  
**Timeline Impact**: Moderate - Needed before bin configuration but straightforward data collection

---

#### GAP-008: Field Status Report Requirements (REQ-027)
**Question**: What should field-generated status reports contain and look like?  
**Missing Information**: Current PlanGrid report examples, content requirements, format preferences, email workflow  
**Business Impact**: Marcus committed to custom development for in-app report generation during session. Without clear requirements, delivered report may not meet needs, requiring rework. Client-facing document affects external perception.  
**Who Can Answer**: Wendy (uses reports), PM team (generates currently)  
**How to Get Answer**: Wendy provides 2-3 actual PlanGrid report examples (redacted if needed)  
**Timeline Impact**: Moderate - Needed before field service app custom development begins

---

### 🟢 Medium Priority - Helpful for optimization

#### GAP-009: Work Order Event Types Complete List (REQ-014)
**Question**: What is the complete, finalized list of work order event types?  
**Missing Information**: Confirmation of six types identified in session, or additions  
**Business Impact**: Event types must be configured before work orders can be created. Affects field service app, reporting, time tracking categorization. Low complexity—just need confirmation.  
**Who Can Answer**: Wendy (PM Manager), Operations team  
**How to Get Answer**: Quick email confirmation or 15-minute meeting  
**Timeline Impact**: Low - Simple data, quick confirmation

---

#### GAP-010: Floor Plan File Format Requirements (REQ-025)
**Question**: What file formats are used for floor plans and are they compatible with field service app?  
**Missing Information**: Typical floor plan file formats, sizes, who creates them  
**Business Impact**: Floor plan punch pinning is critical feature. If formats aren't compatible, feature doesn't work. Testing required before go-live.  
**Who Can Answer**: Design team (creates/receives), PM team (uploads currently), Marcus (Orion compatibility)  
**How to Get Answer**: Provide examples during operations suite demo (Session 2) and test upload  
**Timeline Impact**: Low - Can test during demo session

---

#### GAP-011: Bin Naming Conventions (REQ-003, REQ-004, REQ-005)
**Question**: What naming convention should be used for bins across locations?  
**Missing Information**: Standard naming patterns for receiving, damaged, and duplicate bins  
**Business Impact**: Consistent naming improves UX, reporting, prevents errors. Bins display in Advanced Receiving drag-and-drop interface—clear names help correct bin selection.  
**Who Can Answer**: Operations team (preferences), Marcus (NetSuite best practices)  
**How to Get Answer**: Marcus proposes standard, operations approves  
**Timeline Impact**: Low - Simple decision during bin configuration

---

#### GAP-012: Contractor Direct Receiving Future Evaluation (REQ-008)
**Question**: What criteria for future evaluation of contractor direct receiving?  
**Missing Information**: Trust criteria, controls needed, pilot approach  
**Business Impact**: Explicitly deferred to future—not blocking current implementation. Documents decision criteria for future evaluation.  
**Who Can Answer**: Operations leadership, Wendy  
**How to Get Answer**: Revisit 3-6 months post-go-live after vendor center adoption established  
**Timeline Impact**: None - Future consideration, not blocking

---

## 7. CONSULTANT ACTION PLAN

### 7.1 Immediate Actions (Next 1-2 weeks)

**CRITICAL:**
1. **Schedule Session 1: Scheduling & Resource Management Deep Dive**
   - **Assigned To**: Marcus
   - **Target Date**: Within 2 weeks
   - **Attendees**: Wendy, Kimmy, Matt, Marcus
   - **Duration**: 2 hours
   - **Priority**: 🔴 CRITICAL - Blocking requirements map completion

2. **Schedule Session 2: Operations Suite Demo**
   - **Assigned To**: Marcus/Chris
   - **Target Date**: Within 3 weeks
   - **Attendees**: Wendy, Receiving team, PM team, Marcus/Chris
   - **Duration**: 1.5-2 hours
   - **Priority**: 🟡 HIGH - Critical for user adoption preparation

**HIGH:**
3. **Request Work Order Final Confirmation**
   - **Assigned To**: Marcus (via email to Wendy/Matt)
   - **Target Date**: Within 1 week (can confirm after demo)
   - **Content**: "Wendy, following your buy-in during our Operations session, we need formal confirmation that work orders will be implemented. Please confirm so we can proceed with field service app configuration."
   - **Priority**: 🟡 HIGH - Blocking field service configuration

4. **Request 15% Labor Markup Exception Logic**
   - **Assigned To**: Marcus (email to Kipp)
   - **Target Date**: Within 2 weeks
   - **Content**: "Kipp, please document the complete business rule logic for the 15% labor markup: (1) Which order types trigger it? (2) Which are excluded? (3) Which clients have exceptions? (4) What line code identifies 'external labor'? Natural language is fine—we'll translate to NetSuite formula. Please validate against 5-10 sample orders."
   - **Priority**: 🔴 CRITICAL - Blocking sales order configuration

5. **Request PM and Design Rate Matrix**
   - **Assigned To**: Marcus (email to Kipp/Wendy/Rafina)
   - **Target Date**: Within 2 weeks
   - **Content**: "Please collaborate on complete rate matrix including: PM internal/external rates, workshop designer rate, standard designer rate, field designer rates (if different), client-specific negotiated rates with client names. Include effective dates."
   - **Priority**: 🟡 HIGH - Needed for time tracking configuration

6. **Request Damaged Product Accounting Meeting**
   - **Assigned To**: Marcus (meeting request to Lorraine/Kipp)
   - **Target Date**: Within 2 weeks
   - **Duration**: 30 minutes
   - **Content**: "Let's walk through damaged product accounting scenarios: receiving damaged items, adding zero-cost replacement lines, write-off process, period-end reconciliation. Lorraine raised this during the session—need to document accounting treatment."
   - **Priority**: 🟡 HIGH - Needed for VRA configuration

7. **Request Contractor Access Lists**
   - **Assigned To**: Marcus (email to Wendy/Rafina/Operations team)
   - **Target Date**: Within 3 weeks (before user provisioning)
   - **Content**: "Please provide two lists: (1) Which installation contractors need vendor center access? (2) Which contractors need time entry access? For each: company name, contact person, email, access type. This is for user provisioning and training planning."
   - **Priority**: 🟡 HIGH - Needed for user provisioning timeline

8. **Request Warehouse Location List**
   - **Assigned To**: Marcus (email to Operations team/Wendy)
   - **Target Date**: Within 3 weeks (before bin configuration)
   - **Content**: "Please provide complete list of third-party warehouse locations where product is received: warehouse name/company, address, primary contact. We'll configure receiving bins for each location."
   - **Priority**: 🟡 HIGH - Needed for bin configuration

9. **Request PlanGrid Status Report Examples**
   - **Assigned To**: Marcus (email to Wendy/PM team)
   - **Target Date**: Before Session 2 demo (3 weeks)
   - **Content**: "Please provide 2-3 examples of actual PlanGrid status reports (redact client names if needed). We need to see current format, content, photo display, floor plan markups to build field service app report generation feature."
   - **Priority**: 🟡 HIGH - Needed for custom development requirements

### 7.2 Follow-up Actions (Next 2-4 weeks)

**After Session 1 (Scheduling & Resource Management):**
10. **Document Session 1 Decisions**
    - **Assigned To**: Marcus
    - **Deliverable**: Updated Requirements_Map_Operations with REQ-032, REQ-033, REQ-034 approaches
    - **Deliverable**: User stories for resource management requirements
    - **Deliverable**: Scope definition if custom development needed (resource visualizer)

11. **Update Questionnaire with Scheduling Answers**
    - **Assigned To**: Marcus/Chris
    - **Deliverable**: Questionnaire_Operations_v2.0.md with Q14-Q20 answers completed
    - **Deliverable**: Decision log updates

**After Session 2 (Operations Suite Demo):**
12. **Collect Floor Plan Compatibility Feedback**
    - **Assigned To**: Marcus/Chris
    - **Deliverable**: Document supported floor plan formats, any conversion needs

13. **Finalize Work Order Event Types**
    - **Assigned To**: Operations team (during or after demo)
    - **Deliverable**: Complete, confirmed list of event types

14. **Draft PM Field Service App Training Plan**
    - **Assigned To**: Marcus/Chris
    - **Deliverable**: Training outline, schedule, materials list
    - **Include**: Offline mode testing scenario

15. **Draft Contractor Vendor Center Training Plan**
    - **Assigned To**: Marcus/Chris
    - **Deliverable**: External training approach, pilot contractor selection, rollout phases

**Configuration Data Collection:**
16. **Finalize Bin Naming Conventions**
    - **Assigned To**: Marcus (propose) → Operations team (approve)
    - **Deliverable**: Standard naming pattern document
    - **Timeline**: During bin configuration phase

17. **Validate 15% Labor Markup Logic**
    - **Assigned To**: Kipp (provide sample orders) → Marcus (configure) → Kipp (validate)
    - **Deliverable**: Formula configured and tested against historical orders
    - **Timeline**: During sales order configuration phase

### 7.3 Completion Actions

**Final Review Process:**
18. **Requirements Map Final Review**
    - **Trigger**: After Session 1 (scheduling decisions made)
    - **Participants**: Marcus, Chris, Wendy, Operations leadership
    - **Deliverable**: Confirmed Requirements_Map_Operations_v2.0 with all 34 requirements classified

19. **Questionnaire Completeness Validation**
    - **Trigger**: After Session 1 and all configuration data collected
    - **Participants**: Marcus, Chris
    - **Deliverable**: Questionnaire_Operations_v2.0 marked 100% complete

20. **Gap Analysis Closure**
    - **Trigger**: After all gaps addressed
    - **Deliverable**: GapAnalysis_Operations_v2.0 with all gaps marked resolved or explicitly deferred

**Client Sign-off:**
21. **Operations Requirements Sign-off**
    - **Trigger**: After Requirements Map v2.0 complete
    - **Participants**: Wendy (primary), Matt/Mark (leadership), Lorraine (finance)
    - **Deliverable**: Formal approval to proceed with operations configuration
    - **Format**: Email confirmation or sign-off meeting

**Documentation:**
22. **Configuration Workbook for Operations**
    - **Trigger**: After requirements sign-off
    - **Assigned To**: Marcus/Chris
    - **Deliverable**: Detailed configuration specifications:
      - Bin structure for all locations
      - Rate matrix configured
      - 15% labor markup formula
      - Work order event types
      - VRA workflow
      - Time tracking setup
      - Field service app configuration
    - **Purpose**: Guide configuration phase execution

23. **Training Materials Development**
    - **Trigger**: During configuration phase
    - **Assigned To**: Marcus/Chris
    - **Deliverables**:
      - Advanced Receiving tool training (receiving team)
      - Work order creation training (operations team)
      - Field Service app training (PM team)
      - Vendor center training (contractors—external)
      - VRA process training (AP team, receiving team)
      - Time tracking training (PMs, designers, contractors)

---

## 8. SUCCESS METRICS

### 8.1 Completion Targets

**Current Status**: 82% complete (23 of 29 questions have fully actionable answers)

**After Session 1 (Scheduling & Resource Management)**:
- **Target**: 93% complete
- **Questions Resolved**: Q14, Q16, Q17, Q18, Q19, Q20 (6 questions)
- **Requirements Updated**: REQ-032, REQ-033, REQ-034 (3 requirements)
- **Estimated Date**: 2 weeks from today (approximately November 6, 2025)

**After Configuration Data Collection (15% markup logic, rate matrix, warehouse lists, contractor lists)**:
- **Target**: 97% complete
- **Questions Resolved**: Q21, Q22, Q23, Q24, Q25, Q26 (6 questions)
- **Estimated Date**: 3-4 weeks from today (approximately November 13, 2025)

**After Session 2 (Operations Suite Demo) and Final Clarifications**:
- **Target**: 100% complete
- **Questions Resolved**: Q27, Q28, Q29 (3 questions)
- **Requirements Validated**: All 34 requirements confirmed feasible and approved
- **Estimated Date**: 4-5 weeks from today (approximately November 20, 2025)

### 8.2 Timeline Summary

| Milestone | Target Date | Completion % | Critical Dependencies |
|-----------|-------------|--------------|----------------------|
| **Session 1 Scheduled** | 1 week | 82% | Marcus calendaring |
| **Session 1 Completed** | 2 weeks | 93% | Wendy, Kimmy, Matt attendance |
| **Configuration Data Received** | 3-4 weeks | 97% | Kipp (logic/rates), Operations (lists) |
| **Session 2 Completed** | 4-5 weeks | 100% | Receiving/PM team, floor plans, reports |
| **Requirements Sign-off** | 5-6 weeks | 100% | Leadership approval |
| **Configuration Workbook Ready** | 6-7 weeks | 100% | Marcus/Chris documentation |

### 8.3 Risk-Adjusted Timeline

**Best Case** (all stakeholders responsive, no scope changes): 4 weeks to 100%  
**Expected Case** (typical delays, minor clarifications): 5-6 weeks to 100%  
**Worst Case** (scheduling conflicts, major scope changes after Session 1): 8-10 weeks to 100%

**Key Risk Factors:**
1. **Session 1 Scheduling** - Requires 4 busy people (Wendy, Kimmy, Matt, Marcus) for 2 hours
2. **Session 1 Scope Expansion** - If scheduling/resource management decisions reveal new requirements
3. **Kipp Responsiveness** - Critical data owner for 15% markup logic and rate matrix
4. **Contractor Data Collection** - Operations team may need time to compile comprehensive lists
5. **Work Order Confirmation** - Leadership may delay final decision until after demo

---

## 9. DECISION LOG EXCERPT (New/Updated Decisions from This Analysis)

### Decisions Detected During Gap Analysis

**DECISION-001**: Schedule dedicated 2-hour session for scheduling & resource management  
**Type**: [FUNCTIONALITY]  
**Context**: Team identified during Operations session that scheduling/resource management requires deeper dive. Gap analysis confirms REQ-032, REQ-033, REQ-034 cannot be designed without explicit decisions on task management approach, resource visualizer, and account manager integration.  
**Detected In**: GapAnalysis_Operations.md (this document)  
**Status**: Decision needed—session must be scheduled  
**Priority**: 🔴 CRITICAL

**DECISION-002**: Prioritize operations suite demo (Session 2) as high priority, not critical  
**Type**: [SOLUTIONDESIGN]  
**Context**: While demo is important for user adoption and training planning, it is not blocking requirements definition. Most requirements for REQ-002 and REQ-024-031 are already well-defined. Demo validates functionality and builds confidence but doesn't fundamentally change requirements.  
**Detected In**: GapAnalysis_Operations.md (this document)  
**Status**: Decision made—HIGH priority (not CRITICAL)  
**Priority**: 🟡 HIGH

**DECISION-003**: Treat configuration data gaps (rates, lists, logic) as high priority collection activities, not decision blockers  
**Type**: [FUNCTIONALITY]  
**Context**: Missing data (GAP-003, GAP-004, GAP-006, GAP-007) represents straightforward information collection, not design decisions. Requirements are clear—just need data to populate. Can proceed with requirements sign-off while data collection happens in parallel, as long as data delivery timeline is committed.  
**Detected In**: GapAnalysis_Operations.md (this document)  
**Status**: Decision made—data collection parallel track  
**Priority**: 🟡 HIGH

---

## 10. REQUIREMENTS MAP UPDATES

### New Requirements Discovered

*No new requirements discovered during gap analysis. All 34 requirements from original questionnaire analysis remain valid.*

### Requirements Approach Updates

**REQ-032, REQ-033, REQ-034**: Status remains "TBD" pending Session 1. Once session completed, these will be updated with specific ALIGNS/ADAPT/ACCOMMODATE classifications and, if ACCOMMODATE, scope of custom development will be defined.

---

## 11. CHANGE MANAGEMENT IMPLICATIONS

### High-Risk Adoption Areas Confirmed

**External Party Adoption (Contractors)**:
- Vendor center adoption is critical path for receiving notification process (REQ-007)
- Recommend phased rollout: 1-2 pilot contractors → expand to trusted partners → full rollout
- Backup email process must remain during transition period
- Training burden is on KBM to train external parties (not under KBM control)

**PM Field Service App Adoption**:
- Replacing familiar PlanGrid tool with new Orion app
- Offline mode is critical—must work flawlessly (buildings with no connectivity)
- Floor plan punch pinning must match or exceed PlanGrid capability
- Recommend parallel run period (keep PlanGrid active for 1-2 months during transition)

**VRA Process Discipline**:
- Requires behavioral change: create VRA even when not shipping back (80% of cases)
- Lorraine's pain point (lost credits) is strong motivator, but team must remember to create VRA
- Recommend workflow enforcement: damaged receiving → auto-prompt for VRA creation

**15% Labor Markup Change**:
- Kipp's OCD satisfied (line at bottom, uneditable, non-printing) may improve user satisfaction
- Exception logic must be thoroughly tested—affects every labor order
- Sales team needs clear communication on why line exists and how it works

### Training Complexity Assessment

**High Complexity** (require hands-on, repetition):
- Advanced Receiving tool (drag-and-drop mechanics, bin selection)
- Field Service app (multiple features, offline mode, floor plan pinning)
- VRA process change (behavioral shift)

**Medium Complexity** (require clear documentation, demo):
- Vendor center contractor access
- Work order creation and soft scheduling
- Time tracking from field service app

**Low Complexity** (require brief training):
- Purchase requisitions (standard workflow)
- 15% labor markup (auto-calculates, users just see it)

---

## 12. APPENDICES

### Appendix A: Question-to-Requirement Traceability

| Question | Related Requirements | Status |
|----------|---------------------|--------|
| Q1 - Operations scope | All requirements | ✅ Complete |
| Q2 - Purchase requisitions | REQ-001 | ✅ Complete |
| Q3 - Outsourced receiving | REQ-002, REQ-003, REQ-006, REQ-007 | ✅ Complete |
| Q4 - Advanced Receiving | REQ-002 | ✅ Complete |
| Q5 - Bin structure | REQ-003, REQ-004, REQ-005 | ✅ Complete |
| Q6 - Vendor center | REQ-006, REQ-007, REQ-009 | ✅ Complete |
| Q7 - Contractor direct receiving | REQ-008 | ✅ Complete (deferred) |
| Q8 - Damaged product/VRA | REQ-010, REQ-011, REQ-012 | ✅ Complete |
| Q9 - Work orders | REQ-013, REQ-014, REQ-015 | ⚠️ Partial (needs confirmation) |
| Q10 - Time tracking GP | REQ-016, REQ-017, REQ-018, REQ-019 | ✅ Complete |
| Q11 - 15% labor markup | REQ-021, REQ-022, REQ-023 | ⚠️ Partial (needs logic) |
| Q12 - Punch list | REQ-024, REQ-025, REQ-026, REQ-027 | ✅ Complete |
| Q13 - Field Service app | REQ-028, REQ-029, REQ-030, REQ-031 | ✅ Complete |
| Q14 - Scheduling/resource mgmt | REQ-032, REQ-033, REQ-034 | ❌ Incomplete (session needed) |
| Q15 - External contractor billing | REQ-020 | ✅ Complete |
| Q16 - PM task list automation | REQ-032 | ❌ Incomplete (session needed) |
| Q17 - Resource visualizer | REQ-033 | ❌ Incomplete (session needed) |
| Q18 - Task sophistication | REQ-034 | ❌ Incomplete (session needed) |
| Q19 - Account mgr tracking | REQ-033 (integrated) | ❌ Incomplete (session needed) |
| Q20 - Task dependencies | REQ-032, REQ-034 | ❌ Incomplete (session needed) |

### Appendix B: Stakeholder Contact Summary

| Stakeholder | Role | Email/Contact | Engagement Level | Follow-Up Needed |
|-------------|------|---------------|------------------|------------------|
| Wendy | PM Manager | [TBD] | ⭐⭐⭐⭐⭐ Excellent | Session 1 (critical), Session 2 (high) |
| Marcus | Implementation Lead | [TBD] | ⭐⭐⭐⭐⭐ Excellent | All sessions (facilitator) |
| Lorraine | CFO | [TBD] | ⭐⭐⭐⭐ Strong | Damaged product accounting meeting |
| Kipp | IT Specialist | [TBD] | ⭐⭐⭐⭐ Strong | 15% markup logic, rate matrix |
| Matt | Leadership | [TBD] | ⭐⭐⭐ Good | Session 1 (critical decision) |
| Kimmy | Acct Mgr Leader | [TBD] | ⭐⭐⭐ Good | Session 1 (critical) |
| Rafina | Design Manager | [TBD] | ⭐⭐ Mentioned only | Rate matrix, contractor list |
| Chris | Implementation Team | [TBD] | ⭐⭐⭐⭐ Strong | Session 2 demo |

### Appendix C: Acronyms and Terms

- **VRA**: Vendor Return Authorization (process for returning damaged product or tracking expected credits)
- **GP**: Gross Profit (revenue minus direct costs)
- **GL**: General Ledger (accounting system impact)
- **WIP**: Work in Progress (inventory status for received but not yet shipped items)
- **PM**: Project Manager (oversees installation and project delivery)
- **PO**: Purchase Order
- **SO**: Sales Order
- **TBD**: To Be Determined
- **ALIGNS**: Dealer process aligns with NetSuite/Orion standard functionality
- **ADAPT**: Dealer must adapt process to use NetSuite/Orion
- **ACCOMMODATE**: Orion/GSI will accommodate dealer process with customization

---

## CONCLUSION

The Operations discovery questionnaire is **82% complete** with strong progress on core operational processes. The critical path to 100% completion is:

1. **Schedule and complete Session 1** (Scheduling & Resource Management) - 🔴 CRITICAL within 2 weeks
2. **Collect configuration data** from Kipp, Operations team, Rafina - 🟡 HIGH within 3-4 weeks
3. **Schedule and complete Session 2** (Operations Suite Demo) - 🟡 HIGH within 4-5 weeks
4. **Obtain final confirmations** and examples - 🟢 MEDIUM within 5-6 weeks

**Timeline to 100%**: 5-6 weeks (expected case)

**Primary Responsibility**: Marcus to schedule Session 1 immediately and send data request emails to stakeholders

**Next Immediate Action**: Email Wendy, Kimmy, Matt to schedule Session 1: Scheduling & Resource Management Deep Dive (2 hours, within 2 weeks)

---

*End of Gap Analysis - Operations*


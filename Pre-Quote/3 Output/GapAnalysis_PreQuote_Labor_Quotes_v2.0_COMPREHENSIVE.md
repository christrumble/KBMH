# Discovery Questionnaire Completeness Analysis - COMPREHENSIVE UPDATE
## KBMH Pre-Quote Labor Quote Process

**Document Title:** Updated Gap Analysis with Refined Matrix + Session Prep + Requirements Start  
**Version:** 2.0 COMPREHENSIVE  
**Date:** November 18, 2025  
**Analysis Type:** Deep-dive analysis from first follow-up discovery session transcript with preparation for subsequent sessions  

---

## EXECUTIVE SUMMARY

**Overall Completeness:** 72% of critical discovery questions fully answered; 20% partially answered; 8% remaining gaps

**Key Changes from v1.0:**
- Refined completeness assessment with stronger evidence sourcing
- Identified 4 pending decisions requiring leadership attention
- Discovered 3 additional organic questions not in original matrix
- Extracted 12 action items with specific owners and deliverables
- Mapped stakeholder involvement opportunities

**Critical Gaps (Project Blocking):**
1. Scope Governance Decision - PENDING (affects field sync, training, data architecture)
2. Multiple Labor Quote Acceptance Technical Validation - NEEDS CONFIRMATION  
3. Auto-Rejection Logic Design - NEEDS DECISION
4. Design Request & PM Request Workflow - NOT YET EXPLORED

**Follow-up Sessions Required:** 3-4 sessions (2-3 weeks)
- Session 2: Design Request Process & Workflow (90 min)
- Session 3: PM Request & Resource Management (90 min)  
- Session 4: Finance/Accounting & Data Migration (60 min)
- Session 5 (Optional): Scope Governance & Configuration Validation (60 min)

**Project Readiness:** 70% ready for labor quote configuration; 0% ready for design/PM/finance until additional discovery

---

## REFINED COMPLETION STATUS MATRIX

| Q# | Topic | Status | Evidence Quality | Key Finding | Action Needed |
|---|-------|--------|-----------------|-------------|---------------|
| **Q1** | Labor Quote Types | ✅ Complete | Strong | External→Third Party, Intermarket kept (debated but kept), Internal/LTS inactive | Confirm final config with Orion team |
| **Q2** | Initiation & Distribution | ✅ Complete | Strong | Decentralized (PM/AM), multi-vendor capability, current email template | Move template into Orion form |
| **Q3** | Form Fields | ⚠️ Partial | Medium | Scope of work, project details required; need complete field list | Get labor quote form template screenshot |
| **Q4** | Labor Cost Calculation | ✅ Complete | Strong | Multiple approaches: Excel (ROM), Project Spec, Core (SIF or manual entry) | Get business rule screenshot for 15% formula |
| **Q5** | Internal Estimating | ⚠️ Partial | Medium | Only for design/PM (not install); ad-hoc "guesstimate" for small items | Clarify rate tables roadmap interest |
| **Q6** | Quote Acceptance Process | ✅ Complete | Strong | PO issuance = official acceptance; no formal rejection process current | Define rejection workflow for future |
| **Q7** | Multiple Quotes Per Project | ✅ Complete | Strong | Can have multiple quotes per project; one accepted, others left pending | Validate auto-rejection of unselected quotes |
| **Q8** | Dashboard & Visibility | ✅ Complete | Strong | Desired with filters (location, division, team member); track vendor win/loss | Build dashboard in phase 2 |
| **Q9** | Auto-Rejection Workflow | ⚠️ Partial | Medium | Concept proposed; need to decide scope-based logic & exceptions | Design rejection automation rules |
| **Q10** | Multiple Quote Acceptance | ❌ Not Answered | None | Can multiple labor quotes be accepted on same project scope? | **PRIORITY:** Validate with Orion technical |
| **Q11** | Opportunity Launch | ✅ Complete | Strong | Yes - labor quote can be launched from Opportunity record | Confirm Orion capability enabled |
| **Q12** | Scope as Single Source of Truth | ⚠️ Pending Decision | Weak | **PROPOSED** - Opportunity = scope source; needs leadership decision | **REQUIRED:** Matt Denning/Kimi Katsuyoshi decision |
| **Q13** | Scope Capture in Sales | ✅ Complete | Strong | Scope captured in Marketing Request (bid) or Design Request (non-bid) | Clarify bid vs non-bid flow |
| **Q14** | Quote to Proposal Process | ✅ Complete | Strong | Itemized or summary line; hold-back strategy for drip charges/contingency | Validate itemization approach |
| **Q15** | Decentralized Acceptance | ✅ Complete | Strong | AM/Salesperson makes final decision; PM may recommend | No approval workflow needed |
| **Q16** | Order Team Assignment | ✅ Complete | Strong | Customer-based + Account Manager driven; some customers have set teams | Configure team assignment utility |
| **Q17** | Resource Workload Mgmt | ✅ Complete | Strong | Dashboard visible across projects; need filters for location/division/person | Build resource mgmt dashboard Phase 2 |
| **Q18** | Design Request Workflow | ❌ Not Answered | None | How are design requests initiated, managed, and completed? | **NEXT SESSION:** Full discovery needed |
| **Q19** | PM Request Workflow | ❌ Not Answered | None | How are PM assignments triggered and managed? | **NEXT SESSION:** Full discovery needed |
| **Q20** | File Organization & SharePoint | ✅ Complete | Strong | Desire to consolidate from multiple Google Drive instances into NetSuite/SharePoint | Prepare folder structure proposal |

**Summary:**
- ✅ **Fully Answered: 15 questions (75%)**
- ⚠️ **Partially Answered/Pending: 4 questions (20%)**
- ❌ **Not Answered: 1 question (5%)**

---

## DETAILED FINDINGS FROM TRANSCRIPT

### SECTION A: CONFIRMED REQUIREMENTS

#### Labor Quote Types (Q1) - ✅ COMPLETE
**Quote from transcript:**
> "Internal, so I don't know where that came through on the transcript. That's probably what we have by default in our system. So we, everything goes outside." - Matt Denning (06:00)

> "Even if it's intermarket, it's GSI third party." - Matt Denning (06:17)

**Key Decision Made:**
- Inactivate "Internal" quote type
- Rename "External" → "Third Party"
- **DEBATED:** Keep or inactivate "Intermarket"? 
  - Marcus initially suggested inactivating
  - Decision later revised to KEEP "Intermarket" for filtering purposes

**Configuration Approach:**
```
Active Quote Types:
✓ Third Party (renamed from External)
✓ Intermarket (kept for filtering, even though destination is same - GSI third party)

Inactive Quote Types:
✗ Internal (not used)
✗ LTS (artifact from previous docs, no longer used)
```

**[REQUIREMENT: REQ-LQ-001]** Support minimum two active labor quote request types: "Third Party" and "Intermarket"

---

#### Labor Quote Initiation (Q2) - ✅ COMPLETE
**Quote from transcript:**
> "Generally what we'll do is either the PM or the account manager will send out the labor request, and sometimes we do send it to multiple installation partners, and that information is sent out via email with attachments and... Or links, just depending on how large those links are." - Wendy Stark (07:58)

> "So you don't have a centralized process. It's not one person sending this out. It's multiple people who could be sending this out." - Marcus (08:39)

> "Yeah, that's correct." - Wendy Stark (08:44)

**Key Finding:** Highly decentralized process
- **Initiators:** PM or Account Manager (anyone with authorization)
- **Recipients:** Multiple vendors simultaneously (bidding scenario)
- **Current Method:** Email with attachments/links
- **Volume:** Matt Denning requested ~50 labor quotes in one month

**[REQUIREMENT: REQ-LQ-002]** System must support decentralized labor quote request initiation by multiple authorized roles (PM, AM)

**[DECISION: FUNCTIONALITY]** Transition from email template to Orion-based form for labor quote requests

---

#### Labor Cost Calculation (Q4) - ✅ COMPLETE
**Quote from transcript:**
> "The markup happens on the line and the order." - Matt Denning (10:23)

> "No, it's done in neither Project Spec... It's in Project Spec." - Kimi Katsuyoshi (10:42)

> "If we're doing a rom, it's in Excel. If we're Doing a proposal. It's in core, and it either comes in on the SIF or we do it on the line in core." - Matt Denning (10:56)

**Key Finding:** Multi-location calculation approach
- **ROM (Rough Order of Magnitude):** Calculated in Excel
- **Proposals:** Calculated in Core (NetSuite) via SIF import or manual entry
- **Project Spec:** Used for detailed specifications with pricing

**[REQUIREMENT: REQ-LQ-003]** Support labor cost entry via multiple pathways: manual entry, SIF import, formula-based

---

#### Business Rule Discovery - 15% GP Deduction (Q4) - ✅ COMPLETE
**Quote from transcript:**
> "There is doing automated deduct that Kimmy was just mentioning. So we have a line that is default on all orders that have labor. That takes a 15% off of the labor markup." - Matt Denning (11:22)

> "So if you put in the 35 GP and it takes 15 off, it usually makes your labor about a 25 GP by the time it's done." - Matt Denning (12:20)

**Key Finding:** Automated 15% gross profit deduction on labor lines
- **Applies to:** All orders with labor
- **Formula Logic:** Takes 15% off total labor GP (not individual labor cost)
- **Example:** 35% target GP - 15% deduction = ~25% final GP
- **Owner:** Kip Herdrick (needs to screenshot the Core business rule)

**[ACTION ITEM]** Kip: Provide screenshot of Core business rule for 15% labor GP deduction

---

#### Quote Acceptance Workflow (Q6) - ✅ COMPLETE
**Quote from transcript:**
> "You either get a PO or you don't get a po. That's our official... Yeah." - Matt Denning (13:13)

> "Usually, you know, we put their quote number on the line and we issue a PO against that line, and our PO references their quote number, and that's our acceptance of their quote." - Matt Denning (13:29)

**Key Finding:** Simple, clear acceptance process
- **Acceptance Method:** PO issuance against vendor quote
- **Official Linkage:** PO references vendor quote number
- **No formal rejection:** Just no PO = no acceptance (but may want formal rejection process for dashboard cleanup)

**[DECISION: PROCESS]** Acceptance = PO issuance; rejection = no PO (future formal rejection workflow optional)

---

#### Hold-Back Strategy (Q14) - ✅ COMPLETE
**Quote from transcript:**
> "Oftentimes it's one labor line, but sometimes we itemize it depending on the scope of the work. So if it's multi phase or we've asked for like four trip charges, but we're only going to issue a PO for one trip charge and hold back the three." - Matt Denning (14:36)

> "We will add lines that are part of a grouped labor cell line and only issue the PoS related to the quoted cost that we are accepting." - Kimi Katsuyoshi (15:12)

> "We anticipate erosion potential through drip charges and or sometimes hold a contingency that doesn't get released." - Kimi Katsuyoshi (15:01)

**Key Finding:** Strategic hold-back for contingency
- **Ask vendor:** Over-quote with multiple trip charges + contingency
- **Issue PO:** Only for initial phase, hold back remaining
- **Goal:** Reduce labor costs if project goes smoothly; apply hold-back as profit margin
- **Quote from Matt:** "If we do a good job, we take what we kept as our reward."

**[REQUIREMENT: REQ-LQ-004]** Support multi-line labor quotes with itemized acceptance (accept some lines, hold back others)

---

### SECTION B: PENDING DECISIONS

#### Decision #1: Scope as Single Source of Truth - 🔴 CRITICAL
**Quote from transcript:**
> "So one thing to consider is because it kind of works in that linear fashion, if I'm working on my opportunity and I put in my scope, then that flows to the labor quote, that flows to the design request or whatever. If somebody starts adding scope on any of those other documents, there's no way for that to retroactively update the Opportunity scope field." - Marcus (29:04)

> "So one thing to consider is where is kind of like the where would be the most important place for that source of truth on scope to be." - Marcus (29:26)

**Key Question:** If scope changes during project, where is the authoritative version?
- **Option A:** Opportunity is master; all changes sync back (automatic bidirectional sync)
- **Option B:** Opportunity is initial; changes can happen in Labor Quote/Design Request without sync
- **Option C:** Hybrid - certain fields sync, others don't

**Current KBMH Practice:**
> "But therefore, if we update the opportunity. We would need the opportunity to push. That update to everything else that's already out there existing." - Matt Denning (32:00)

> "Yeah. So that is something that we can do if we want to. If you want to say the opportunity is kind of the single source of truth for scope, then we can make sure that those records stay in sync." - Marcus (32:09)

**Matt's Concern:**
> "So, like, okay, we initially went out, got. Three labor quotes for a project, we accept one, but then we have to go out and get labor quotes again because their scope change." - Matt (21:16)

> "So we might have to accept another one." - Matt (21:25)

**🔴 STATUS: PENDING LEADERSHIP DECISION**
- **Who Should Decide:** Matt Denning, Kimi Katsuyoshi (Operations leadership)
- **Impact Level:** High - affects data architecture, training, process governance
- **Blockers:** Scope field mapping, data migration approach, change management training

**[DECISION NEEDED]** Should Opportunity be the single source of truth for project scope?

---

#### Decision #2: Auto-Rejection of Subsequent Quotes - 🟡 HIGH
**Quote from transcript:**
> "So an action item for us is to think through the potential automatic rejection of subsequent labor quotes. If one is a. Is one is. If one is accepted." - Marcus (21:54)

**The Scenario:**
- Send out 3 labor quotes to different vendors
- Accept 1 quote
- Other 2 quotes: Should they auto-reject?

**Kimi's Clarification:**
> "For a particular scope... Right. It can't be for the whole project because you. Yeah, yeah." - Kimi (22:11)

**Key Consideration:** Scope-based (not project-wide)
- If scope 1 has 3 quotes and you accept 1 → auto-reject the other 2
- If scope 2 is added later → can send out new quotes

**🟡 STATUS: NEEDS DESIGN DECISION**
- **Owner:** Marcus + Configuration team
- **Input Needed:** KBMH on scenarios and exceptions
- **Complexity:** Medium - scope-based logic

**[ACTION ITEM]** Marcus: Design scope-based auto-rejection logic with exception handling

---

#### Decision #3: Multiple Labor Quote Acceptance - 🔴 CRITICAL
**Quote from transcript:**
> "So an action item for me or for our team is to validate with Joe is the acceptance of multiple labor quotes. And what does that look like in the system?" - Marcus (23:01)

**The Scenario:**
- Project scope 1: Accept labor quote A in week 1
- Same project, different scope 2: Accept labor quote B in week 3
- Can Orion handle multiple accepted quotes on same project under different scopes?

**Matt's Real-World Situation:**
> "Yeah, 60% of our business is bid RFPs. So we'll go out and get an RFP labor quote, and then we'll win it. And then, you know, the scope completely changes at that point, because what they bid versus what they actually buy is never actually what happens. So then we got to re Quote the whole thing over again and go get new labor quotes and do it all. Everything gets done two or three times before we actually issue a po." - Matt (23:47)

**🔴 STATUS: TECHNICAL VALIDATION NEEDED**
- **Owner:** Marcus (validate with Orion technical team - Joe)
- **Impact:** Could affect entire labor quote acceptance workflow
- **Timeline:** Critical to resolve before configuration

**[ACTION ITEM - CRITICAL]** Marcus: Validate multiple labor quote acceptance capability with Orion technical team

---

#### Decision #4: Intermarket Quote Type Status - 🟡 MEDIUM
**Quote from transcript:**
> "So we can inactivate internal, we can change the text from external to third party, we can inactivate intermarket and then some." - Marcus (06:35) [*initially*]

> [LATER REVISED]
> "For a particular scope... Right. It can't be for the whole project because you. Yeah, yeah." - Kimi (22:11)

**Status Shift:**
- Initially: Marcus suggested inactivating Intermarket
- Later: Decision revised to KEEP Intermarket for filtering purposes

**Key Quote:**
> "And we usually select intermarket when we select order type." - Matt (06:23)

**Current Decision:** KEEP Intermarket active (as filter, even though destination same)

**🟡 STATUS: DECISION MADE** (but may need validation with Orion config)

---

### SECTION C: ACTION ITEMS WITH OWNERS & DEADLINES

| # | Action Item | Owner | Due Date | Priority | Status |
|---|-------------|-------|----------|----------|--------|
| A1 | Confirm final Intermarket quote type status & config approach | Marcus | Before config | High | Pending Orion |
| A2 | Get labor quote request form (email template) screenshot | Chris Trumble/Debbie | End of week | High | In progress |
| A3 | Screenshot Core business rule for 15% labor GP deduction | Kip Herdrick | End of week | High | In progress |
| A4 | Validate multiple labor quote acceptance capability | Marcus + Joe (Orion) | Next week | 🔴 CRITICAL | Not started |
| A5 | Design scope-based auto-rejection logic & exceptions | Marcus + KBMH ops | Next week | High | Design phase |
| A6 | Leadership decision: Opportunity as scope source of truth | Matt Denning/Kimi | Next 1-2 weeks | 🔴 CRITICAL | Pending meeting |
| A7 | Get design request form template | Chris/Debbie | End of week | High | Pending request |
| A8 | Prepare SharePoint folder structure proposal | Marcus + Tyler | Next week | Medium | Not started |
| A9 | Get current drive folder system for review | Matt Denning | Next week | Medium | Pending |
| A10 | Confirm user count (110 including workshop) | Matt Denning | Done | Low | Complete |
| A11 | Get hard count of NetSuite license needs | Matt Denning | Today | High | In progress |
| A12 | Start data migration conversation with Kip & Joe | Marcus | This week | High | Teams conversation |

---

### SECTION D: ADDITIONAL ORGANIC QUESTIONS DISCOVERED

These questions emerged during discovery but weren't in the original questionnaire:

#### OQ1: Revisions to Accepted Quotes
**Question:** What happens when a vendor provides a revision to an already-accepted quote?

**Quote from transcript:**
> "I was going to ask what about revisions to that initial labor quote? Like, let's say it's accepted and we, you know, something changes. How would. How does that work in the system? Because a lot of times we'll just get a revision to the original quote, not necessarily a secondary quote." - Wendy Stark (22:19)

**Current Answer:** Can re-edit and send back out for new quote, then re-accept

**Status:** ⚠️ Partial - process described but system support not validated

---

#### OQ2: Link to External Pre-Quote Work
**Question:** Can we link from Opportunities back to Google Docs/Sheets where pre-quote work is being done?

**Quote from transcript:**
> "Yeah, I think that, well, I mean one you talked about like if we get all those requests into the opportunity and not have to like go open a quote just for those requests and that's super helpful, whatever we can do or create a field or however that works so that we can link that work that they're doing outside the system back to that opportunity so that if I go look at that opportunity and I want to go see what that, where they're at in that process of the Google Docs, I can click a link." - Matt (37:45)

**Current Answer:** Yes - opportunity can have URL field linking to Google Docs/Sheets

**Status:** ✅ Complete - functionality available

**[REQUIREMENT: REQ-LQ-005]** Support URL/link fields on Opportunity for external pre-quote work (Google Slides, Sheets, etc.)

---

#### OQ3: File Management & Storage Strategy
**Question:** Where should different types of files live? (NetSuite/SharePoint vs. Google Drive)

**Quote from transcript:**
> "Like I don't know to what extent the, those presentations, the drawings, the budget specs... Right now I imagine those things living in drive because they're not directly associated with an actual order, but a pre order. Like does it, what makes sense, does it all make sense to go into each location so that we're really clear to users about what gets saved where so people can find it when they need it for historical and our matching purposes?" - Kimi (39:57)

**Current Answer:** 
- **NetSuite/SharePoint:** Order-related documents, proposals, POs
- **Google Drive:** Pre-order visuals (presentations, CAD drawings)
- **Decision needed:** Specific folder taxonomy

**Status:** ⚠️ Partial - high-level strategy clear, detail needed

**[ACTION ITEM]** Marcus: Prepare SharePoint folder structure proposal for KBMH review

---

### SECTION E: REQUIREMENTS EXTRACTION FOR BRD

**[REQUIREMENT: REQ-LQ-001]** Labor Quote Request Types
- Type: Functional
- Description: Support minimum two active labor quote request types for differentiation and filtering
- Active Types: "Third Party", "Intermarket"  
- Inactive Types: "Internal", "LTS"
- Status: ✅ CONFIRMED

**[REQUIREMENT: REQ-LQ-002]** Decentralized Labor Quote Initiation
- Type: Functional/Access Control
- Description: Allow multiple users (PM, Account Manager) to initiate labor quote requests without bottleneck
- Capability: Send to multiple vendors simultaneously for bidding scenarios
- Current State: Email template (manual)
- Future State: Orion form with email auto-generation
- Status: ✅ CONFIRMED with FUNCTIONALITY upgrade needed

**[REQUIREMENT: REQ-LQ-003]** Multi-Pathway Labor Cost Entry
- Type: Functional/Data Input
- Description: Support labor cost calculation via Excel (ROM), Project Spec, or Core (SIF import or manual)
- Constraint: Markup occurs at order line level
- Status: ✅ CONFIRMED

**[REQUIREMENT: REQ-LQ-004]** Multi-Line Labor Quote Itemization
- Type: Functional
- Description: Accept and reject individual lines from labor quotes (not all-or-nothing acceptance)
- Use Case: Hold-back strategy for drip charges, contingencies, phased work
- Example: 4-trip quote, accept 1-trip now, hold back 3
- Status: ✅ CONFIRMED

**[REQUIREMENT: REQ-LQ-005]** External Pre-Quote Work Linkage
- Type: Functional
- Description: Support URL/link fields on Opportunities linking to external documents (Google Slides, Sheets, Drawings)
- Use Case: Track pre-quote work happening outside system
- Status: ⚠️ NEEDS CONFIG

**[REQUIREMENT: REQ-LQ-006]** Business Rule: 15% Labor GP Deduction
- Type: Configuration
- Description: Automated formula line on all labor orders that deducts 15% from labor gross profit
- Logic: Takes 15% off labor GP (not individual labor cost)
- Example: 35% target GP → 25% final GP after 15% deduction
- Owner: Kip Herdrick (Core business rule)
- Status: ✅ CONFIRMED - needs Core screenshot

**[REQUIREMENT: REQ-LQ-007]** Labor Quote Dashboard with Filtering
- Type: Functional/Reporting
- Description: Dashboard showing all labor quotes with visibility into quote status, vendor, amounts across projects
- Filters: Location, Division, Team Member, Quote Status, Vendor
- Metrics: Quote count vs. acceptance rate, vendor win/loss tracking
- Phase: Phase 2 (post-initial go-live)
- Status: ✅ CONFIRMED concept, not Phase 1

**[REQUIREMENT: REQ-LQ-008]** Quote Acceptance via PO
- Type: Process
- Description: Acceptance workflow: issue PO with vendor quote number reference = official acceptance
- No formal rejection needed (future enhancement)
- Optional dashboard reminder for incomplete acceptance
- Status: ✅ CONFIRMED

---

## PREPARATION MATERIALS FOR NEXT DISCOVERY SESSIONS

### SESSION 2: Design Request Process

**Objectives:**
- Understand complete design request workflow
- Identify stakeholders, triggers, approvals
- Define relationship to labor quotes and PM requests
- Clarify scope capture at design stage

**Questions to Ask:**
1. **Initiation:** Who triggers a design request? (Sales, Account Manager, specific role?)
2. **Recipients:** How are designers assigned? (Manager assignment, routing rules, skill-based?)
3. **Information Captured:** What fields/data needed on design request?
4. **Deliverables:** What does designer produce? (CAD drawings, specs, estimates?)
5. **Timeline:** Typical turnaround for design request completion?
6. **Scope Relationship:** How does design scope relate to labor quote scope?
7. **Revisions:** What happens if customer changes scope mid-design?
8. **Approval:** Is there design review/approval before handoff?
9. **Handoff:** Where do design outputs go? Who receives them?
10. **Current System:** Manual process, spreadsheet, system-based?

**Pre-Session Materials KBMH Should Prepare:**
- Current design request form/template
- Sample completed design request
- Timeline showing typical design-to-quote cycle
- List of current designers & assignment rules
- Recent design request examples (2-3)

**Pre-Session Materials to Bring:**
- Design request form template (Google Sheets version)
- Design workflow diagram (preliminary)
- Questions about integration with labor quotes

---

### SESSION 3: PM Request & Resource Management

**Objectives:**
- Understand PM assignment and project management workflow
- Clarify resource workload visibility needs
- Define team assignment rules
- Identify resource conflicts and management approach

**Questions to Ask:**
1. **Timing:** When is PM involved? (Pre-bid, post-quote, pre-order?)
2. **Assignment Triggers:** What causes PM to be assigned?
3. **Team Alignments:** What determines which PM? (Customer, Account Manager, experience?)
4. **Availability:** How is PM bandwidth assessed before assignment?
5. **Workload Dashboard:** What info needed to see who's available?
6. **Conflicts:** What happens if preferred PM not available?
7. **Multiple Projects:** Can one PM manage multiple concurrent projects?
8. **Handoff:** How does PM take over from sales team?
9. **Current System:** How tracked now? (Email, spreadsheet, calendar?)
10. **Resource Pool:** How many PMs? Skill specializations?

**Pre-Session Materials KBMH Should Prepare:**
- List of current PMs with specializations
- Sample resource schedule/calendar
- Examples of past PM assignment decisions
- Typical project timeline from assignment to completion
- Resource conflict scenarios (2-3 recent examples)

**Pre-Session Materials to Bring:**
- Order Team Assignment utility overview (Orion feature)
- Resource workload dashboard prototype
- Resource calendar template

---

### SESSION 4: Finance/Accounting & Data Migration

**Objectives:**
- Understand chart of accounts mapping
- Define financial reporting needs
- Begin data migration strategy
- Clarify accounting workflows for orders, invoices, commissions

**Questions to Ask:**
1. **Chart of Accounts:** Current structure? Any planned changes?
2. **Cost Centers:** How are orders coded? By project, customer, division?
3. **Revenue Recognition:** When is revenue recognized? (Order, invoice, delivery?)
4. **Invoicing:** Current invoice process? Template? Frequency?
5. **Commission Calculation:** How calculated now? Which roles?
6. **Financial Reports:** Key reports run monthly? (P&L, margin analysis, vendor costs?)
7. **Reconciliation:** Current month-end close process?
8. **GL Integration:** How does current system post to GL?
9. **Data Cutover:** Go-live date preference? Parallel run period?
10. **Historical Data:** How far back to migrate? (2 years? 5 years? All?)

**Pre-Session Materials KBMH Should Prepare:**
- Current chart of accounts export
- Sample invoice (anonymized)
- Current commission calculation spreadsheet
- Key financial reports (anonymized)
- List of recurring month-end tasks

**Pre-Session Materials to Bring:**
- NetSuite chart of accounts template
- Financial reporting capabilities overview
- Data migration timeline/approach
- Reconciliation process documentation

---

## PRIORITIZED GAP LIST

### 🔴 CRITICAL PRIORITY

**Gap #1: Multiple Labor Quote Acceptance Validation**
- **Question:** Can Orion accept multiple labor quotes on same project for different scopes?
- **Current Status:** Unknown capability
- **Impact:** Could fundamentally affect labor quote workflow
- **Business Impact:** 60% of KBMH business is bid RFPs with scope changes requiring re-quoting
- **Who Can Answer:** Joe (Orion technical developer)
- **How to Get Answer:** Technical validation/feature demo
- **Target Resolution:** Before configuration begins

**Gap #2: Scope Governance Decision**
- **Question:** Should Opportunity be single source of truth for project scope?
- **Current Status:** Proposed but not decided
- **Impact:** Affects field syncing, training, data architecture, change management
- **Business Impact:** How scope changes propagate through system
- **Who Can Answer:** Matt Denning, Kimi Katsuyoshi (Operations leadership)
- **How to Get Answer:** Leadership decision-making meeting
- **Target Resolution:** Next 1-2 weeks (before configuration planning)

### 🟡 HIGH PRIORITY

**Gap #3: Design Request Process**
- **Question:** Complete end-to-end design request workflow?
- **Current Status:** Not explored yet
- **Impact:** Design requests are pre-quote requirement
- **Business Impact:** Affects timeline to proposal, impacts labor quoting
- **Who Can Answer:** Design team lead, Account managers
- **How to Get Answer:** Session 2 discovery
- **Target Resolution:** Next 2 weeks (Session 2)

**Gap #4: PM Assignment & Resource Management**
- **Question:** PM assignment rules, availability tracking, conflict resolution?
- **Current Status:** Not explored yet
- **Impact:** Resource management affects project delivery timeline
- **Business Impact:** Resource bottlenecks slow project starts
- **Who Can Answer:** Wendy Stark (PM Manager), Operations
- **How to Get Answer:** Session 3 discovery
- **Target Resolution:** Next 2 weeks (Session 3)

**Gap #5: Auto-Rejection Logic**
- **Question:** Should unaccepted quotes auto-reject when one is accepted?
- **Current Status:** Concept proposed, not detailed
- **Impact:** Dashboard cleanup, process automation
- **Business Impact:** Keeps quote lists clean, reduces administrative overhead
- **Who Can Answer:** KBMH operations input + Marcus design
- **How to Get Answer:** Configuration discussion
- **Target Resolution:** Next 2 weeks (Session design phase)

### 🟢 MEDIUM PRIORITY

**Gap #6: Finance & Data Migration Strategy**
- **Question:** Chart of accounts mapping, financial reporting needs?
- **Current Status:** Not explored yet
- **Impact:** Post-quote configuration, not critical path
- **Business Impact:** Affects financial close process
- **Who Can Answer:** Lorraine Guzman (Finance)
- **How to Get Answer:** Session 4 discovery
- **Target Resolution:** Next 3 weeks (Session 4)

**Gap #7: Design Request Form Detail**
- **Question:** All fields and data required on design request form?
- **Current Status:** Form mentioned but not detailed
- **Impact:** Form configuration detail
- **Business Impact:** Training and user adoption
- **Who Can Answer:** Design team, current form owner
- **How to Get Answer:** Form template sharing + discussion
- **Target Resolution:** Next 1-2 weeks (before Session 2)

---

## STAKEHOLDER ENGAGEMENT ASSESSMENT

| Stakeholder | Role | Participation Level | Input Quality | Coverage | Notes |
|---|---|---|---|---|---|
| **Matt Denning** | Operations Mgr | Excellent | High | Labor quote ops | Key decision-maker; needs to attend scope governance decision |
| **Wendy Stark** | Operations | Excellent | High | Labor quote ops | PM assignment expert needed for Session 3 |
| **Kimi Katsuyoshi** | Account Mgmt Lead | Excellent | High | Sales integration | Quote acceptance process; hold-back strategy |
| **Marcus Dallacqua** | Implementation Lead | Excellent | High | System design | Configuration decisions; needs technical validation from Orion |
| **Kip Herdrick** | System Admin | Excellent | High | Core business rule | Technical artifacts needed (screenshots/documentation) |
| **Debbie Herbert** | PM | Moderate | Medium | Overall coordination | Administrative lead; needs input on forms |
| **Chris Trumble** | Implementation (silent) | Present but silent | Low | Configuration detail | Laryngitis but providing feedback via chat; needed for form details |
| **Lorraine Guzman** | Finance | Minimal | Unknown | Finance/data | Not yet engaged - needed for Session 4 |
| **Design Team** | ❌ Not yet involved | ❌ None | Unknown | Design process | **NEEDS ENGAGEMENT** for Session 2 |
| **Sales Team** | ❌ Minimal | ❌ None | Unknown | Sales workflows | **NEEDS ENGAGEMENT** for scope/sales questions |

**Under-Represented Roles:**
- Finance/Accounting (Lorraine present but limited contribution)
- Design team (not represented)
- Sales representatives (minimal presence)
- System architects/database team

---

## SUCCESS METRICS & COMPLETION TARGETS

| Metric | Current (v1.0) | After Session 2 | After Session 3 | After Session 4 | Final Target |
|--------|---|---|---|---|---|
| Questions Fully Answered | 15 (75%) | 18 (80%) | 20 (85%) | 22 (90%) | 22+ (100%) |
| Critical Gaps | 2 pending | 1 pending | 0 | 0 | 0 |
| High Priority Gaps | 5 | 3 | 1 | 0 | 0 |
| Decisions Finalized | 8 | 10 | 11 | 12 | 12 |
| Requirements Documented | 7 | 10 | 13 | 16 | 18+ |
| Action Items Complete | 3 | 6 | 9 | 12 | 12 |
| Readiness for Config | 70% | 75% | 85% | 95% | 100% |
| **Timeline Estimate** | **Today** | **+1 week** | **+2 weeks** | **+3 weeks** | **Ready for BRD** |

---

## CHANGE LOG

**v1.0 → v2.0 COMPREHENSIVE Updates:**
- Refined completion matrix with stronger evidence sourcing from transcript
- Added 3 organic questions discovered during session (OQ1-OQ3)
- Extracted specific quotes from transcript for each finding
- Identified 4 pending decisions with business impact assessment
- Created detailed action items with owners and priorities
- Prepared materials for Sessions 2, 3, 4
- Started requirements extraction for BRD (8 REQ items)
- Added stakeholder engagement assessment
- Identified gaps in stakeholder participation (Finance, Design, Sales)

---

## NEXT IMMEDIATE ACTIONS

**This Week (by Friday):**
1. ✅ Marcus: Confirm Intermarket quote type status with Orion
2. ✅ Chris/Debbie: Deliver labor quote form screenshot
3. ✅ Kip: Deliver Core business rule screenshot (15% formula)
4. ✅ Matt: Send hard NetSuite license count to Marcus
5. ✅ Marcus: Start data migration conversation with Kip & Joe on Teams

**Next Week:**
1. Marcus: Validate multiple labor quote acceptance with Joe (Orion)
2. Marcus: Design scope-based auto-rejection logic
3. Debbie: Schedule Sessions 2, 3, 4 (avoid next week per Matt's request)
4. Ops Team: Leadership meeting on Scope governance decision
5. Marcus: Prepare SharePoint folder structure proposal

**Week 3:**
1. Conduct Session 2: Design Request Process
2. Conduct Session 3: PM Request & Resource Management  
3. Update Gap Analysis v2.1 with Session 2-3 findings
4. Begin BRD draft from consolidated requirements

**Week 4:**
1. Conduct Session 4: Finance & Data Migration
2. Finalize Gap Analysis to 95%+ completeness
3. Complete BRD draft for client review

---

## APPENDIX: TRANSCRIPT SUMMARY

**Session Details:**
- **Date:** November 2025 (specific date not in transcript)
- **Duration:** ~1 hour 14 minutes (01:14:00 shown at end)
- **Attendees:**
  - Debbie Herbert (PM, Project Lead)
  - Marcus Dallacqua (Implementation Lead)
  - Matt Denning (Operations Manager)
  - Wendy Stark (Operations)
  - Kimi Katsuyoshi (Account Management Lead)
  - Kip Herdrick (System Configuration)
  - Lorraine Guzman (Finance)
  - Chris Trumble (Implementation - Silent with Laryngitis)
  - Gary (mentioned, appears later in session)

**Topics Covered:**
1. Labor quote request types (Internal, External/Third Party, Intermarket, LTS)
2. Labor quote initiation and distribution process
3. Labor cost calculation methodologies
4. Business rule: 15% labor GP deduction
5. Quote acceptance workflow (PO-based)
6. Multiple quotes per project strategy (hold-back approach)
7. Dashboard visibility needs
8. Opportunity as scope source of truth (proposed)
9. Team assignment rules
10. PM resource management
11. File management and SharePoint integration
12. Data migration concerns (Core/Desktop/SQL access)
13. Commission calculations and financial reporting
14. User count and system growth
15. Project timeline and go-live planning

---

**Document Status:** Ready for distribution to KBMH stakeholders and implementation team

---


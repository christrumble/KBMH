# Pre-Quote Questionnaire: Labor Quote Request Process
## KBMH - NetSuite/Orion Implementation

**Document Title:** Pre-Quote Labor Quote Request Questionnaire - Follow-Up Discovery Session  
**Version:** 1.0  
**Date:** November 18, 2025  
**Status:** First Pass - Extracted from Discovery Session Transcript  
**Confidence Level:** 75% - Requires Validation  

**Change Log:**
- **v1.0 (Nov 18)** - Initial questionnaire created from follow-up discovery session transcript (KBM-Hogue-Pre-Quote-Follow-up-5916b07e-0676.json)

---

## PROCESSED FILES

**REVIEWED PROJECT FILES:**
- KBM-Hogue-Pre-Quote-Follow-up-5916b07e-0676.json (November 18, 2025 - Discovery Session Transcript)

---

## EXECUTIVE SUMMARY

This questionnaire documents KBMH's Labor Quote Request process based on the first follow-up discovery session. The session covered labor quote request types, initiation process, vendor communication, calculation methodology, acceptance workflows, and stakeholder involvement.

**Key Participants:**
- Marcus Dallacqua (Implementation Lead)
- Matt Denning (Operations)
- Wendy Stark (Operations)
- Kimi Katsuyoshi (Account Management)
- Kip Herdrick (System Configuration)
- Lorraine Guzman (Finance)
- Debbie Herbert (Project Management)
- Chris Trumble (Implementation - Silent/Laryngitis)

**Key Decisions Captured This Session:**
- REQ-001: Labor quote request types confirmed (not GSI/LTS-based)
- REQ-002: Decentralized labor quote initiation model
- REQ-003: Labor quote markup calculation methodology
- REQ-004: Multiple vendor bid capability
- REQ-005: Labor quote acceptance process via PO issuance

---

# DISCOVERY QUESTIONNAIRE

## Q1: LABOR QUOTE REQUEST TYPES

**Question:** What labor quote request types does KBMH use?

**Answer:** KBMH originally had four labor quote request types, but after review, the relevant types are:

1. **External** (renamed to **Third Party**) - For subcontractor/external labor partners
2. **Intermarket** - For labor requests across different markets/regions (but to GSI third-party partners)

**Previous Assumptions (REMOVED):**
- ~~Internal~~ - Not used; everything goes outside the organization
- ~~LTS~~ - Artifact from previous documentation; no longer referenced

**Key Finding:** Internal labor is NOT an option. All labor is sourced from external vendors/subcontractors.

**[REQUIREMENT: Type: Functional]** - The system must support multiple labor quote request types with at least two active types: "Third Party" and "Intermarket" for scope differentiation.

**User Stories:**
- As a PM, I need to differentiate between Third Party quotes and Intermarket quotes so that I can route them to the appropriate vendor network.
- As Operations, I need to track which quote type was used so that I can analyze vendor performance by market type.

**BRD Requirements:**
- [REQUIREMENT] Support minimum two labor quote request types: "Third Party" and "Intermarket"
- [REQUIREMENT] System allows selection of quote type at labor quote request creation
- [CONSTRAINT] "Internal" and "LTS" quote types should be INACTIVE in the system
- [DECISION] External = Third Party (field text update)
- [DECISION] Intermarket is used for regional labor network requests

**Evidence:**
- "Internal, so I don't know where that came through on the transcript. That's probably what we have by default in our system. So we, everything goes outside." - Matt Denning
- "Even if it's intermarket, it's GSI third party." - Matt Denning
- "So no need to differentiate between intermarket... And we usually select intermarket when we select order type." - Matt Denning
- "So we can inactivate internal, we can change the text from external to third party, we can inactivate intermarket..." - Marcus Dallacqua
- **Note:** Marcus later revised this to keep intermarket as an option for filtering purposes

**Confidence Rating: 85%** - Clear confirmation that Internal/LTS don't apply, External=Third Party confirmed. Slight ambiguity on final intermarket decision but appears to be kept.
- Previous: N/A (First pass)
- Rationale: Direct confirmation from operations team, but need to validate final configuration approach with Orion team

**Outstanding Questions:**
- [ ] Confirm final status of Intermarket quote type (keep active or inactive?)
- [ ] Are there any other quote type variations not discussed?

---

## Q2: LABOR QUOTE REQUEST INITIATION & DISTRIBUTION

**Question:** Who initiates labor quote requests and how are they sent to vendors?

**Answer:** Labor quote requests are initiated by either **Project Managers (PMs)** or **Account Managers (AMs)**, with requests sent to multiple vendors simultaneously when bidding is involved.

**Process Overview:**
1. **Initiation:** PM or AM sends out labor request
2. **Recipients:** Can be multiple installation/labor partners simultaneously
3. **Transmission Method:** Email with attachments or links (depending on file size)
4. **Information Included:** Scope of work description and relevant project details
5. **Decentralized:** Multiple people can initiate (not bottlenecked to one role)

**Current System:** Email template form that PM/AM fills out and sends manually

**Desired Future State:** Move labor quote request email template into Orion system, allowing Orion to issue the email directly (reducing copy/paste and standardizing communication)

**[REQUIREMENT: Type: Functional]** - The system must support decentralized labor quote request initiation by multiple roles (PM, AM) with the ability to send requests to multiple vendors simultaneously.

**User Stories:**
- As a PM, I need to send labor quote requests to multiple vendors so that I can compare bids and negotiate pricing.
- As an AM, I need to quickly send labor quote requests without leaving the system so that I can reduce manual email steps.
- As Operations, I need visibility into who is sending labor quote requests so that I can ensure quality control and consistency.

**BRD Requirements:**
- [REQUIREMENT] Multiple users (PM, AM) can initiate labor quote requests without requiring approval/routing
- [REQUIREMENT] Labor quote request form should be available in Orion (not external email template)
- [REQUIREMENT] Users can select multiple vendors to receive same labor quote request
- [REQUIREMENT] System auto-generates and sends email to selected vendors with attachments/specifications
- [FUNCTIONALITY] Labor quote request form should include scope of work and project details fields
- [CONSTRAINT] Current approach: Manual email with template (to be transitioned to system-based)

**Evidence:**
- "Generally what we'll do is either the PM or the account manager will send out the labor request, and sometimes we do send it to multiple installation partners, and that information is sent out via email with attachments and... Or links, just depending on how large those links are." - Wendy Stark
- "We have a form that we basically have them fill out. It's an email template. If we could move that template into Orion and then Orion issue that email, that would be great." - Matt Denning
- "So you don't have a centralized process. It's not one person sending this out. It's multiple people who could be sending this out." - Marcus Dallacqua
- "Yeah, that's correct." - Wendy Stark

**Confidence Rating: 90%** - Clear confirmation of decentralized process, multiple vendor capability, and desire to move to system-based form.
- Previous: N/A (First pass)
- Rationale: Explicit statements from operations team; only minor detail needed on exact form fields

**[DECISION: FUNCTIONALITY]** - Orion will provide standardized labor quote request form accessible to PM/AM roles, replacing manual email template.

**Outstanding Questions:**
- [ ] What are ALL the required fields on the labor quote request form?
- [ ] What's the timeline for transitioning from email template to Orion form?
- [ ] Are there any approval workflows or authorization requirements for labor quote sending?

---

## Q3: LABOR QUOTE REQUEST FORM REQUIREMENTS

**Question:** What information must be captured on a labor quote request form?

**Answer:** The form captures scope of work, project details, and project specifications. Current form is external (email template); need to move to Orion.

**Information Captured:**
- Scope of work description
- Project specifications (attachments/links)
- Project location/site information
- Timeline/scheduling information
- Any other project details relevant to the labor estimate

**[ACTION ITEM - KBMH TEAM]** - Provide copy of current labor quote request form/email template for comparison and verification

**[REQUIREMENT: Type: Functional]** - Orion labor quote request form must capture all fields currently on email template, plus allow for scope and project detail entry.

**Evidence:**
- "And so obviously that email has a description of, you know, the requests for the scope of work and all of that information." - Wendy Stark
- "So if we can get a copy of that, you might have already sent it... I don't want to ask for it again if you already sent it." - Marcus Dallacqua
- "So an action item for us is to take a screenshot of our labor quote request form and send that off to them so they can compare it against their form." - Marcus Dallacqua

**Confidence Rating: 60%** - High-level understanding that form captures scope; specific fields not yet documented.
- Previous: N/A (First pass)
- Rationale: Need to see actual form to confirm all required fields

**Outstanding Questions:**
- [ ] What are the exact required fields on current labor quote form?
- [ ] Which fields are optional vs. required?
- [ ] Are there attachments/file uploads needed?
- [ ] What data currently exists in Project Spec that could auto-populate?

---

## Q4: LABOR COST CALCULATION METHODOLOGY

**Question:** How are labor costs calculated and what markup is applied?

**Answer:** Labor cost calculations depend on project type:

**For ROM (Rough Order of Magnitude):** Calculations done in Excel (external to system)

**For Proposal/Quote:** Calculations done in either Project Spec or Core system

**Markup Calculation:** There is a standard 15% markup DEDUCTION from labor on all orders with labor

**The 15% Deduction Rule:**
- Applies to: All orders containing labor
- Calculation: 15% off the labor Gross Profit (GP)
- Impact: If PM puts in 35% GP on labor, system automatically reduces to ~25% GP
- Business Logic: Reduces markup to account for internal labor coordination costs
- System Location: Formula line in Core system (business rule)
- Term: "Formula line" is the NetSuite/Core term for this automated adjustment

**[REQUIREMENT: Type: Functional]** - System must apply automated 15% labor margin reduction on all labor-containing orders via formula line

**User Stories:**
- As a PM, I need to understand how the 15% deduction affects my labor markup so that I can calculate accurate proposals.
- As Finance, I need the 15% deduction to be automatically applied so that we maintain consistent margin management across all labor orders.

**BRD Requirements:**
- [REQUIREMENT] Automated "formula line" that deducts 15% from labor Gross Profit
- [REQUIREMENT] This line appears on all orders containing labor charges
- [REQUIREMENT] The 15% deduction reduces overall project GP (not a separate line item)
- [FUNCTIONALITY] PM enters desired GP (e.g., 35%), system calculates final GP after 15% reduction (e.g., ~25%)
- [DECISION] This is a system business rule (formula line) - not manual calculation

**Evidence:**
- "So we have a line that is default on all orders that have labor. That takes a 15% off of the labor markup. That is basically internal cost." - Matt Denning
- "So the formula line. I'm hearing that correct. That's... That's the term in core, I think. Yes, 15%." - Marcus Dallacqua
- "So if you put in 35 GP and it takes 15 off, it usually makes your labor about a 25 GP by the time it's done." - Matt Denning
- "So it's taking it from the GP. So whatever GP you put in, it's lowering your GP." - Matt Denning

**[ACTION ITEM - KIP]** - Take screenshot of the business rule configuration showing the 15% labor deduction formula for documentation

**Confidence Rating: 88%** - Clear explanation of 15% deduction mechanism; need technical screenshot for confirmation.
- Previous: N/A (First pass)
- Rationale: Matt Denning and Marcus confirmed mechanism clearly; slight ambiguity on exact technical implementation resolved

**Outstanding Questions:**
- [ ] Is this 15% applied before or after other adjustments?
- [ ] Are there exceptions to the 15% rule?
- [ ] Does this apply to both external and intermarket labor quotes?

---

## Q5: INTERNAL ESTIMATING & RATE TABLES

**Question:** Does KBMH do internal labor estimating, or solely rely on vendor quotes?

**Answer:** KBMH does NOT perform internal labor estimating for installation work. They ONLY use external vendor quotes. The exception is Design/NPM (which may have internal estimating).

**Current State:**
- Design/NPM: May have internal estimating (not fully explored)
- Installation Labor: 100% vendor-quoted; no internal estimates
- Ad-hoc Small Items: When labor quote is forgotten/not obtained, PMs estimate price (e.g., "I think that's $300") but this is NOT a formal process

**Rate Tables:** KBMH does not currently maintain rate tables in Orion, but expressed interest for future consideration (estimated delivery: end of next year)

**Internal Rate Structures (Future Consideration):**
- Most installers use rate tables based on chair type (e.g., Executive chair = 0.25 hours, Standard chair = 0.5 hours)
- KBMH doesn't track to that level of detail currently (only track minutes)
- Potential future tool for ROM estimates and internal reference

**[REQUIREMENT: Type: Functional - Future]** - Rate tables for internal labor estimation (Low Priority, Roadmap item for end of next year)

**Evidence:**
- "And then do you guys... Are you doing any of your own internal estimating at all? Well, only on design npm." - Marcus Dallacqua / Matt Denning
- "Not on the install." - Matt Denning
- "If you mean that when we forget to get a label quote for something small and we go, I think that's $300, and then we hope we're right about it... Yeah, that happens a lot actually, Marcus." - Matt Denning
- "Right now we have rate tables that we keep based off of hourly rates. But you know, most of our installers have rate tables that are like, knocks it down by like chair... If it's a generation chair, it's 0.25 hours. If it's a sit on a chair, it's 0.5 hours. Like real rate tables. We don't, we don't get that deep. We just go based off of minutes." - Matt Denning

**Confidence Rating: 85%** - Clear that internal estimating is NOT used for installation; rate tables are potential future tool.
- Previous: N/A (First pass)
- Rationale: Explicit confirmation from operations; rate tables are clearly a future consideration

**Outstanding Questions:**
- [ ] Is there any situation where internal estimates ARE used?
- [ ] How often is the "I think it's $300" ad-hoc estimation used?

---

## Q6: LABOR QUOTE ACCEPTANCE & PO ISSUANCE

**Question:** How does KBMH accept labor quotes and what's the formal process?

**Answer:** Labor quote acceptance is INFORMAL. The formal acceptance is the issuance of a Purchase Order (PO).

**Acceptance Process:**
- **Formal Acceptance:** Issuing a PO that references the vendor's quote number = acceptance
- **Communication:** Sometimes PMs/AMs send email communication to vendor confirming acceptance, but NOT required
- **PO Structure:** KBMH puts vendor's quote number on the PO line and issues PO against that quote number; this PO automatically becomes the acceptance

**No Formal Rejection:** 
- There is no formal rejection/send-back workflow currently
- Unaccepted quotes simply don't get a PO
- No official communication that a quote was rejected

**[REQUIREMENT: Type: Functional]** - System must support labor quote acceptance workflow where acceptance is tied to PO issuance and references vendor quote number.

**User Stories:**
- As PM, I need to be able to mark a labor quote as accepted so that the system knows which quote to build the PO from.
- As Finance, I need to see which labor quotes were accepted so that I can reconcile vendor costs against actual PO amounts.

**BRD Requirements:**
- [REQUIREMENT] Labor quote acceptance is documented when PO is issued against the quote
- [REQUIREMENT] PO must link to and reference the original labor quote
- [REQUIREMENT] PO line must include vendor's quote number for traceability
- [FUNCTIONALITY] Orion labor quote acceptance feature should allow users to accept quote and move lines to PO
- [CONSTRAINT] No formal rejection process currently exists; unaccepted quotes simply don't get a PO

**Evidence:**
- "Do you have some type of workflow for accepting those quotes from vendors? Like official acceptance and rejection?" - Marcus Dallacqua
- "You either get a PO or you don't get a po. That's our official." - Matt Denning
- "I mean, sometimes there's an email communication if the PM or the AM decides to... But usually, you know, we put their quote number on the line and we issue a PO against that line, and our PO references their quote number, and that's our acceptance of their quote." - Matt Denning

**Confidence Rating: 90%** - Clear explanation of PO-based acceptance; no formal rejection process.
- Previous: N/A (First pass)
- Rationale: Explicit confirmation from Matt Denning; Marcus expressed this is different from other dealers they work with

**Outstanding Questions:**
- [ ] How often is email confirmation sent vs. just PO?
- [ ] Should a formal rejection process be implemented in future?

---

## Q7: MULTIPLE LABOR QUOTES PER PROJECT SCOPE

**Question:** Can there be multiple labor quotes on a single project, and how does that work?

**Answer:** YES - There can be multiple labor quotes per project scope, particularly when:
1. **Scope Changes During Project:** If scope changes after initial quote, new labor quotes may be requested
2. **Multiple Phases:** Multi-phase projects may have separate labor quotes per phase
3. **Hold-Back Strategy:** Sometimes KBMH requests quote for multiple trip charges but only issues PO for one trip charge and holds back others

**Quote Strategy - Trip Charges Example:**
- Scope: Project will need 4 trip charges
- Labor Quote Request: Quote for all 4 trip charges
- PO Strategy: Only issue PO for 1 trip charge initially
- Business Logic: Hope to only need 1 trip; hold others as contingency
- If Additional Trips Needed: Come back to same accepted quote for additional trip POs
- Margin Benefit: Keep difference between quoted amount and issued PO as project margin if additional trips not needed

**Itemization Approach:**
- Some quotes brought in as ONE total labor line
- Other quotes itemized with multiple lines (for multi-phase or multi-trip visibility)
- Decision depends on project structure and risk management

**[REQUIREMENT: Type: Functional]** - System must support multiple labor quotes per project scope and allow strategic PO issuance that may be less than full quoted scope.

**User Stories:**
- As AM, I need to request a quote for all potential trip charges so that I have contingency labor cost information.
- As Finance, I need to see which labor quote lines have been PO'd and which are being held as contingency.
- As PM, I need to request additional POs against an already-accepted labor quote when scope changes occur.

**BRD Requirements:**
- [REQUIREMENT] Multiple labor quotes can exist on single project
- [REQUIREMENT] Single accepted labor quote can generate multiple POs (for phased releases)
- [REQUIREMENT] Labor quote lines can be itemized (e.g., Trip 1, Trip 2, Trip 3, Trip 4)
- [REQUIREMENT] User can select which quoted lines to include in each PO issuance
- [FUNCTIONALITY] "Labor Quote Acceptance Modal" should allow user to select which lines to move to PO (summary or itemized)
- [CONSTRAINT] Lines not included in PO can remain on quote as contingency

**Evidence:**
- "It depends... Sometimes we're building it in spec, sometimes we're building it in core. Sometimes we're itemizing it depending on the scope of the work. So if it's multi phase or we've asked for like four trip charges, but we're only going to issue a PO for one trip charge and hold back the three." - Matt Denning
- "I was to say that we anticipate erosion potential through drip charges and or sometimes hold a contingency that doesn't get released. So we will add lines that are part of a grouped labor cell line and only issue the PoS related to the quoted cost that we are accepting." - Kimi Katsuyoshi
- "So we might ask them to over quote, but then we'll under issue the po hoping that we don't have to use the difference. And if we do have to use the difference, it's in there. And then we'll issue the PO as it's requested. But... Yeah, but we're hoping... To hold on to that money." - Marcus Dallacqua / Matt Denning

**Confidence Rating: 92%** - Excellent detail provided on multi-quote and hold-back strategy; this is a key part of KBMH's business model.
- Previous: N/A (First pass)
- Rationale: Multiple speakers confirmed this approach; Kimi provided specific terminology

**[DECISION: FUNCTIONALITY]** - Support itemized labor quote line selection during acceptance, allowing strategic PO issuance of subset of quoted lines as contingency management.

**Outstanding Questions:**
- [ ] Typical % of quotes where hold-back strategy is used?
- [ ] What happens to held-back lines after project completion?

---

## Q8: LABOR QUOTE DASHBOARD & VISIBILITY

**Question:** What dashboard or reporting is needed for labor quote visibility?

**Answer:** YES - There is desire for a labor quote dashboard to provide visibility across all pending and accepted quotes.

**Dashboard Purpose:** Understand what labor quotes are out there, who they're with, and what status they're at

**Desired Fields/Information:**
- Which vendors are quoting (and which ones are being used most frequently vs. rarely)
- Quote-to-Award ratio (how often specific vendors are quoted vs. how often they're awarded)
- Status tracking (Pending, Accepted, Rejected, Expired)
- Across all projects (company-wide visibility, not just per-project)
- Filter capability: By location, division, order team member

**Current Situation:** No centralized visibility into pending labor quotes (all ad-hoc tracking)

**[REQUIREMENT: Type: Functional]** - System must provide labor quote dashboard with status visibility across all labor quotes, filterable by project criteria.

**User Stories:**
- As Operations Manager, I need a dashboard showing all pending labor quotes so that I can track turnaround and follow up on slow responses.
- As Finance, I need to see who KBMH is quoting with most frequently vs. who we're actually awarding to so that I can analyze vendor performance.
- As Account Manager, I need filtered views of labor quotes by location so that I can see status for my region.

**BRD Requirements:**
- [REQUIREMENT] Labor Quote Dashboard visible to authorized users
- [REQUIREMENT] Shows all labor quotes across all projects (enterprise view)
- [REQUIREMENT] Displays: Quote status, vendor, date sent, expected response date
- [REQUIREMENT] Filterable by: Location, Division, Account Manager/Order Team Member, Status
- [REQUIREMENT] Shows quote vs. award ratio per vendor
- [FUNCTIONALITY] Ability to drill into specific quote for details

**Evidence:**
- "And in one of our conversations, we talked about... Understanding what labor quotes are out there. And I think we talked about having a dashboard, putting together a dashboard for those labor quotes." - Marcus Dallacqua
- "To be able to see who's with what and what status they are at and what's getting sent out to whom would be helpful." - Matt Denning
- "We look at right now who we're doing labor with. It would be nice to see who's quoting and we could see how often quote versus actual what we're awarding." - Matt Denning

**Confidence Rating: 82%** - Clear need for dashboard; specific fields would benefit from additional discussion.
- Previous: N/A (First pass)
- Rationale: Matt Denning provided specific metrics desired (quote vs. award); may have additional fields

**Outstanding Questions:**
- [ ] What time period should be shown (current only, historical)?
- [ ] Should dashboard show expired quotes?
- [ ] Who should have access to dashboard?

---

## Q9: POTENTIAL AUTOMATIC REJECTION WORKFLOW (Future Consideration)

**Question:** Should there be automatic rejection of labor quotes when one is accepted?

**Answer:** POTENTIAL FEATURE - Worth exploring but complex due to scope changes

**Scenario:** If KBMH sends out 3 labor quotes and accepts 1, should the other 2 be automatically rejected/closed?

**Business Reality:** This could be helpful BUT:
- **Caveat:** Multiple labor quotes can exist for different SCOPES (not just different vendor options for same scope)
- **Scope Changes:** If scope changes, new labor quotes go out even though first quote was accepted
- **Revision Scenario:** Sometimes vendor revises the original quote (not a new quote, same quote updated)
- **Complexity:** Can't auto-reject all other quotes on project because they might be for different scopes

**Potential Solution:** Auto-rejection could work "for a particular scope" but NOT for whole project

**[DECISION: FUNCTIONALITY - FUTURE]** - Explore automatic rejection of competing quotes for same scope, but do NOT auto-reject all quotes on project

**Evidence:**
- "So an action item for us is to think through the potential automatic rejection of subsequent labor quotes. If one is a... If one is accepted... Might just want to think through that and think about what the potential exceptions could be." - Marcus Dallacqua
- "For a particular scope." - Kimi Katsuyoshi
- "Right. It can't be for the whole project because you... Yeah, yeah." - Marcus Dallacqua
- "What about revisions to that initial labor quote? Like, let's say it's accepted and we, you know, something changes. How would... How does that work in the system?" - Wendy Stark

**Confidence Rating: 65%** - Identified as potential feature but needs more design thinking before implementation.
- Previous: N/A (First pass)
- Rationale: Concept introduced but requires clarification on scope-based approach

**Outstanding Questions:**
- [ ] How are scope changes tracked/documented?
- [ ] How does KBMH currently manage multiple quotes across scope changes?
- [ ] Is automatic rejection a high-priority feature or nice-to-have?

---

## Q10: ACCEPTANCE OF MULTIPLE LABOR QUOTES (Validation Needed)

**Question:** Can KBMH accept multiple labor quotes on the same project?

**Answer:** NEEDS VALIDATION - Unclear from discussion

**Situation:** If KBMH initially requests labor quotes for Scope A and accepts Quote A1, but then Scope A changes and they request new quotes (Quote A2), can they accept both A1 and A2?

**Business Logic Question:** 
- Is the first accepted quote (A1) effectively "superseded" by the second accepted quote (A2) for revised Scope A?
- Or do they coexist with different PO amounts?

**[ACTION ITEM - MARCUS/ORION TEAM]** - Validate with Joe (Orion technical lead) how system handles acceptance of multiple labor quotes for same project with evolving scope.

**Evidence:**
- "So an action item for me or for our team is to validate with Joe is the acceptance of multiple labor quotes. And what does that look like in the system?" - Marcus Dallacqua

**Confidence Rating: 40%** - This is identified as needing technical validation.
- Previous: N/A (First pass)
- Rationale: Question raised but not fully resolved in session

**Outstanding Questions:**
- [ ] Can same project have multiple ACCEPTED labor quotes?
- [ ] If scope changes, does first accepted quote remain active or get superseded?

---

## Q11: LAUNCH OF LABOR QUOTES FROM OPPORTUNITY RECORDS

**Question:** How should labor quote requests be initiated - from which record type (Opportunity, Quote, Project)?

**Answer:** YES - Labor quotes CAN be launched from Opportunity record (and Quote record), but this may be a process change for KBMH

**Orion Capability:** 
- Opportunity → Labor Quote Request (button available at opportunity level)
- Quote → Labor Quote Request (button available at quote level)
- Project → Labor Quote Request (button available but less commonly used)

**KBMH Current Process:**
- Labor quotes are typically initiated independently, not always from structured records
- Decentralized initiation by PM/AM with manual email

**Opportunity as Source of Truth:**
- If KBMH captures scope at opportunity level, labor quote request can inherit that scope
- Reduces need for re-entry of scope information
- Creates link between opportunity → labor quote → quote → sales order → project

**Key Benefit:** Scope information flows through entire system from opportunity forward

**[REQUIREMENT: Type: Functional]** - System must allow launch of labor quote request from Opportunity, Quote, and Project records with scope information auto-population where available.

**User Stories:**
- As AM, I need to launch a labor quote request directly from the opportunity so that I don't have to create it separately.
- As PM, I need scope information from the opportunity to auto-populate on the labor quote request so that I don't have to re-type it.

**BRD Requirements:**
- [REQUIREMENT] Labor quote request can be initiated from Opportunity record
- [REQUIREMENT] Labor quote request can be initiated from Quote record
- [REQUIREMENT] Labor quote request can be initiated from Project record
- [REQUIREMENT] Scope fields auto-populate from parent record when available
- [FUNCTIONALITY] Single point of initiation (not multiple redundant entry points)

**Evidence:**
- "And right now our... And then anything. So nothing to differentiate between external and intermarket. So that's fine. So we'll make sure in the BRD we talk about exactly what we'll do. By the way, when we make some of these notate some of these things in the brd that kind of becomes our blueprint for when we get into the configuration phase, which is realize. So we take the information from BRD and that's. We make sure we configure things properly." - Marcus Dallacqua
- "And another thing to consider here is since the whole system is integrated so you have this end to end platform, we typically, well, we allow for you to launch a labor quote from an opportunity." - Marcus Dallacqua

**Confidence Rating: 78%** - Capability confirmed; KBMH process integration not yet finalized.
- Previous: N/A (First pass)
- Rationale: Marcus explained Orion capability clearly; integration approach to be determined

**Outstanding Questions:**
- [ ] Does KBMH want to mandate labor quote requests through Opportunity? Or allow both?
- [ ] How mature is KBMH's opportunity data capture?

---

## Q12: SCOPE AS SINGLE SOURCE OF TRUTH

**Question:** Where should scope information be captured and how should it flow through the system?

**Answer:** KBMH is exploring making Opportunity the "single source of truth" for scope, but this requires organizational discipline.

**Ideal Model:** 
1. Scope captured ONCE at Opportunity level
2. Opportunity flows to multiple child records: Marketing Request, Design Request, PM Request, Labor Quote Request
3. All child records inherit scope from Opportunity
4. If scope changes, Opportunity is updated (once) and all child records see updated scope

**Challenge:** Current KBMH process is more ad-hoc:
- Marketing Request may define scope
- Design Request may define/refine scope
- Labor Quote Request may add additional detail
- No single source of truth currently

**Tradeoff to Consider:**
- Pro: Cleaner data flow, less re-entry, better scope consistency
- Con: Requires discipline; users must update opportunity rather than just add to downstream document
- Risk: If someone adds scope to Labor Quote without updating Opportunity, scope becomes de-sync'd

**[REQUIREMENT: Type: Non-Functional]** - Scope data should have clear ownership and update protocol to maintain single source of truth

**[ASSUMPTION]** - Assuming Opportunity will be primary scope record; may need business process training to enforce

**User Stories:**
- As AM, I need scope in one place (Opportunity) so that all projects have consistent scope information.
- As PM, when scope changes, I need to know whether to update Opportunity or downstream documents so that we don't have conflicting scope information.

**BRD Requirements:**
- [REQUIREMENT] Opportunity is identified as "single source of truth" for project scope
- [ASSUMPTION] Scope fields include: Location, Site Details, Budget, Timeline, Requirements
- [CONSTRAINT] Downstream records should NOT override opportunity scope without documented reason
- [FUNCTIONALITY] System allows scope updates at opportunity level to trigger downstream notification/update
- [DECISION] Training will be needed on scope governance

**Evidence:**
- "So when something goes from an opportunity to a project, does that matter? Like, do you GSI go back to then the opportunity to revise the scope as the project evolves?" - Kimi Katsuyoshi
- "Yeah, so the idea here is. Yeah. The labor quote is this standalone record, and you could have multiple labor quotes because you may have sent multiple out, got multiple back, and now you got to choose which one." - Marcus Dallacqua
- "Where should that be captured? Where would be the most important place for that source of truth on scope to be?" - Marcus Dallacqua
- "The opportunity is where all the information lives. So if the scope changes, we have to go update the opportunity to show that new scope." - Matt Denning

**Confidence Rating: 72%** - Concept identified; KBMH not yet committed to this approach.
- Previous: N/A (First pass)
- Rationale: Good discussion of tradeoff; needs business decision from leadership

**[DECISION - PENDING]** - KBMH to confirm whether Opportunity should be single source of truth for scope

**Outstanding Questions:**
- [ ] Is KBMH willing to commit to Opportunity as single source of truth?
- [ ] What business process changes are needed?
- [ ] How will data migration handle existing projects with scattered scope information?

---

## Q13: SCOPE CAPTURE IN SALES PROCESS

**Question:** Where do salespeople currently capture initial project scope?

**Answer:** Scope is captured in different places depending on bid vs. non-bid:

**For Bid Projects (60% of KBMH business):**
- Initial scope captured in: Marketing Request → Design Request (forms/documents)
- NOT captured in Zendesk CRM currently
- Process: Marketing Request > Design Request > Build out spec > Create proposal

**For Non-Bid Projects:**
- Initial scope captured in: Design Request

**In Zendesk (CRM/Opportunity):**
- Only capturing: Project date, timeline, and budget/amount
- NOT capturing: Detailed scope description
- Rationale: "Not really happening on the CRM" because Zendesk is too lightweight for scope detail

**Desired Future State:**
- Capture detailed scope at Opportunity level (in Zendesk)
- Have that scope flow through Marketing Request, Design Request, PM Request, Labor Quote Request
- Reduce copy/paste of scope information across multiple systems/documents

**[REQUIREMENT: Type: Functional]** - Opportunity scope field(s) must be robust enough to capture detailed project scope and carry that through to related requests

**User Stories:**
- As AM, I need to capture detailed project scope in Zendesk so that I can reference it throughout the project lifecycle.
- As Marketing, I don't want to have to re-type scope information that was already in Zendesk.
- As PM, I need scope information to flow from Opportunity to PM Request so that I can start project without re-entering details.

**BRD Requirements:**
- [REQUIREMENT] Opportunity must have scope capture capability (not just budget/timeline)
- [REQUIREMENT] Scope field should include space for detailed requirements (text area, not just single-line)
- [REQUIREMENT] Scope from Opportunity should auto-populate on related requests
- [CONSTRAINT] Marketing and Design may add detail to scope during their process
- [FUNCTIONALITY] Decision: Does detail added during Marketing/Design flow back to Opportunity, or stays local to those documents?

**Evidence:**
- "So, Kim, I think it basically might be in the marketing request or the design request is the initial scope." - Matt Denning
- "So if it's a bid, that initial scope's going through the marketing request and the design request. If it's a non bid, then that initial scope's getting captured in the design request. Got it. It's usually not getting captured in this. In Zendesk, because Zendesk is only capturing project date and timeline and amount." - Matt Denning
- "So the scope can get... If we capture the scope at the opportunity, and then that opportunity initiates the marketing request, the design request, the PM requests, the labor request, then great, they're all getting the same scope." - Matt Denning

**Confidence Rating: 85%** - Clear understanding of current scope capture locations; opportunity for improvement identified.
- Previous: N/A (First pass)
- Rationale: Matt Denning provided clear explanation of current process

**Outstanding Questions:**
- [ ] What are the specific scope fields needed?
- [ ] Should Marketing/Design edits flow back to Opportunity?
- [ ] How much detail is needed in Opportunity scope vs. Design Request?

---

## Q14: LABOR QUOTE TO PROPOSAL PROCESS

**Question:** How does a labor quote transition into a proposal/quote?

**Answer:** Process depends on how labor quote information is brought into the quote/order:

**Scenario 1: As Single Summary Line**
- Entire labor quote amount becomes one line on proposal
- Simplest approach; less visibility but faster

**Scenario 2: Itemized**
- Labor quote lines are broken out separately
- Maintains detail for multi-phase or multi-trip visibility
- Better for hold-back strategy

**Quote Building Process:**
1. Labor quote comes in from vendor
2. User decides whether to bring it in as summary or itemized
3. Orion has "labor quote acceptance feature" with modal that allows selection:
   - User can choose WHICH lines to accept/bring over
   - User can choose format: Summary vs. Itemized
4. Selected lines move to Quote record
5. Labor Quote remains linked to Quote for traceability

**Benefits of Orion Approach:**
- Less copy/paste (reduces manual entry errors)
- Maintains traceability from labor quote → quote → sales order → invoice
- Can see full cost flow: quote → PO → invoice for reconciliation

**[REQUIREMENT: Type: Functional]** - System must provide labor quote acceptance feature that allows users to select which quote lines to move to proposal, with summary or itemized options.

**User Stories:**
- As PM, I need to accept a labor quote and move lines to the proposal without manually re-typing costs.
- As Finance, I need to see which proposal lines came from which labor quotes so that I can reconcile and catch discrepancies.

**BRD Requirements:**
- [REQUIREMENT] Labor quote acceptance modal/interface provided at quote level
- [REQUIREMENT] User can select subset of labor quote lines (for hold-back scenarios)
- [REQUIREMENT] User can choose summary (one line) or itemized (multiple lines) import
- [REQUIREMENT] Links maintained between labor quote, quote, and eventual sales order
- [FUNCTIONALITY] One-way connection: Quote knows its source labor quote; can see history

**Evidence:**
- "So there's a labor quote acceptance feature and there's like a little modal that says, okay, I'm going to accept this labor quote and I'm going to decide what lines I want to have pass over to the quote record, either summary or itemized." - Marcus Dallacqua
- "And you can kind of fiddle with that a little bit. And then it connects the quote and the labor quote together and it makes labor quote part of the project. So when we're doing all our project reporting later on, you have visibility starting at the labor quote, to the quote, to the sales order, to the invoice." - Marcus Dallacqua

**Confidence Rating: 88%** - Clear explanation of Orion acceptance feature; KBMH will need to decide use approach.
- Previous: N/A (First pass)
- Rationale: Marcus explained feature clearly; KBMH needs to confirm if itemized vs. summary approach fits their model

**Outstanding Questions:**
- [ ] Does KBMH prefer summary or itemized approach (or use both)?
- [ ] How often is hold-back strategy used (affects itemization rate)?

---

## Q15: DECENTRALIZED LABOR QUOTE ACCEPTANCE

**Question:** Who can accept labor quotes - is there a single approval person?

**Answer:** NO - Acceptance is DECENTRALIZED. Multiple people can accept labor quotes.

**Current Acceptance Authority:**
- **Sales/Account Manager OR Salesperson:** Typically decides final labor number
- **PM:** Can also accept if helping account manager
- **No rubber stamp requirement:** No single approval bottleneck

**When Acceptance Occurs:**
- Usually when Account Manager or Sales approves the labor cost
- PMs may submit 2-3 quotes and recommend one; Sales makes final decision

**Volume Example:** Matt Denning requests ~50 labor quotes per month, showing this is very frequent activity

**[REQUIREMENT: Type: Functional]** - System must allow multiple users (AM, Salesperson, PM) to accept labor quotes without requiring centralized approval.

**User Stories:**
- As AM, I need to accept a labor quote without waiting for approval from another person.
- As PM, I need to present multiple quote options to the AM for decision.
- As Salesperson, I need to make the final decision on which labor quote to use.

**BRD Requirements:**
- [REQUIREMENT] No centralized "approval workflow" for labor quote acceptance required
- [REQUIREMENT] Access control via role (don't restrict to specific person)
- [REQUIREMENT] Audit trail shows who accepted and when

**Evidence:**
- "Usually it's the account manager or the salesperson that's going to accept the final labor number or the PM if they get some help." - Matt Denning
- "Marcus, last month I requested like 50 labor quotes. So it's like anybody is available. If you're willing and know how to, you can request a labor quote." - Matt Denning
- "Oftentimes what PMs are doing is they're presenting what they think we should do. So they might go get three quotes and then they make a recommendation. But ultimately it's the sales side that makes the final decision on what labor we're going to use." - Matt Denning

**Confidence Rating: 90%** - Clear confirmation that acceptance is decentralized; sales side makes final decision.
- Previous: N/A (First pass)
- Rationale: Explicit from Matt Denning; multiple examples provided

**Outstanding Questions:**
- [ ] Are there any situations where centralized approval IS needed?
- [ ] Should "required roles" notification be applied (filtered by order type)?

---

## Q16: ORDER TEAM ASSIGNMENT & RESOURCE ALLOCATION

**Question:** How should order team roles (PM, AM, Salesperson, Designer) be assigned and managed?

**Answer:** KBMH has sophisticated resource management approach:

**Team Alignment Model:**
- Pre-defined team alignments exist for some accounts (e.g., Wilson, Stanford schools)
- Same people typically work together on specific customer projects
- Team is usually: Salesperson, Account Manager, PM, Designer (roles vary)

**How Assignment Works:**
1. **Customer-Level Defaults:** Some customers have fixed teams assigned in customer record
2. **Opportunity-Level Assignment:** When opportunity created, can use customer-level defaults or override
3. **Role-Based Assignment:** Some roles move with Account Manager (e.g., if AM is assigned, PM automatically flows from that team)
4. **Flexibility:** Some roles may rotate/change, so left blank at customer level

**Decentralized Responsibility:**
- PM typically makes their own assignments from team
- Not bottlenecked through one manager
- Teams may be fluid based on capacity

**Example Structure:**
- Customer: Wilson → Always has Frankie as AM → Esther is PM assigned to Frankie
- Customer: Stanford → Pre-defined team assignment
- Customer: One-off project → Manual assignment by whoever is managing opportunity

**[REQUIREMENT: Type: Functional]** - System must support team assignment at customer level (defaults) with override capability at opportunity/quote/order level.

**User Stories:**
- As Operations, I need to see pre-defined team alignments for customers so that I don't have to reassign same team every project.
- As Account Manager, I need to override team assignments when standard team isn't available.
- As PM, I need my workload visible so that I can see if I have capacity for new assignment.
- As Resource Manager, I need visibility into who is assigned to what so that I can plan resource allocation.

**BRD Requirements:**
- [REQUIREMENT] Customer record can have default team assignments (Salesperson, AM, PM, Designer)
- [REQUIREMENT] Opportunity can accept team assignments from customer defaults
- [REQUIREMENT] Opportunity team assignments can be overridden at opportunity/quote/order level
- [REQUIREMENT] Some customers have fixed teams; others have variable teams
- [REQUIREMENT] Order Team Assignment Utility allows manual assignment at multiple levels
- [FUNCTIONALITY] Resource dashboard shows PM/Designer workload and availability

**Evidence:**
- "Yeah, that's kind of both, I would say." - Wendy Stark (on whether alignment is by customer or AM)
- "With Wilson, we always know it's going to be the same people." - Matt Denning
- "Or with Stanford, certain schools, we always... So right now we leave it blank if it's not. Or if we do know that customer is always going to be same people." - Matt Denning
- "We always fill out who the salesperson is at the customer level. Okay, great. And then if we do know it's a set team, we'll fill out the resources at the customer level so that the account manager or the PC doesn't have to go in every single time they create a new order and put all those people in there." - Matt Denning

**Confidence Rating: 82%** - Good understanding of team alignment model; may have additional nuances.
- Previous: N/A (First pass)
- Rationale: Matt and Wendy provided good examples; team assignment strategy seems well-developed

**Outstanding Questions:**
- [ ] What % of customers have fixed team alignments vs. variable?
- [ ] How often do team members rotate?
- [ ] What's PM capacity per person?

---

## Q17: RESOURCE MANAGEMENT & WORKLOAD VISIBILITY

**Question:** How should resource workload and capacity be tracked?

**Answer:** KBMH wants visibility into resource workload to support assignment decisions.

**Desired Dashboard:**
- See what every PM/Designer is assigned to
- See count of projects/orders assigned per person
- Quick visibility for determining who has capacity

**Current Challenges:**
- Resources juggling many assignments
- No easy way to see who has capacity
- Manual decision-making on who can take next project

**Orion Capability:** Order Team Assignment Utility with resource dashboard capability

**[REQUIREMENT: Type: Functional]** - System must provide resource dashboard showing workload and availability for capacity planning.

**User Stories:**
- As Operations Manager, I need to see all PM assignments so that I know who has capacity for new projects.
- As Account Manager, I need to know if my assigned PM is available before confirming project timeline.

**BRD Requirements:**
- [REQUIREMENT] Resource dashboard shows all assignments by person
- [REQUIREMENT] Count of projects/orders assigned to each resource
- [REQUIREMENT] Visual indication of workload levels (optional)
- [FUNCTIONALITY] Drill-down to see detail of each person's assignments

**Evidence:**
- "Well, this is where I imagine and presumably there is that resource management component where as opportunities need to be assigned those different resources, we're able to see what's on a current resources plate to be able to see what would be a good match for the things that aren't yet assigned." - Kimi Katsuyoshi
- "Right at the opportunity level you have the order team assignment utility where you can assign resources to the at that point you're assigning it to the opportunity which will eventually become the order. But you're able to do it as early as the opportunity. You could do it at the quote or the sales order, but as early as the opportunity. And then you'll have dashboards where you could see everybody and what they're assigned to and counts of how many orders are assigned to or projects are assigned to and things like that." - Marcus Dallacqua

**Confidence Rating: 78%** - Kimi expressed strong desire for this; Orion capability confirmed.
- Previous: N/A (First pass)
- Rationale: Clear need identified; capability exists in Orion

**Outstanding Questions:**
- [ ] What's the right way to visualize workload/capacity?
- [ ] Should assignment suggestions be automated or manual?

---

## Q18: DESIGN REQUEST WORKFLOW (Conditional)

**Question:** If design requests are part of pre-quote, what is the workflow?

**Answer:** Design requests exist and are part of pre-quote process. Summary provided; detailed discovery needed.

**Current Understanding:**
- Design requests are initiated by Sales/AM
- Designers assigned based on team alignment or manual assignment
- May be simultaneous with labor quote requests OR sequential
- Design is completed before quote/proposal is built

**Current Process:**
- Design request goes to Design Manager/Lead
- Manager assigns to available designer
- Designer completes work and provides deliverables
- Output feeds into proposal/quote

**Outstanding Discovery Needed:**
- Design request form details
- Designer assignment rules
- Design cost/billing approach
- Timeline expectations
- Design deliverables format

**[ACTION ITEM]** - Separate discovery session needed on Design Request workflow

**Confidence Rating: 45%** - High-level understanding only; detailed discovery needed.
- Previous: N/A (First pass)
- Rationale: Design mentioned but not primary focus of this session

**Outstanding Questions:**
- [ ] Detailed design request workflow needed
- [ ] Design cost structure needed
- [ ] Design request form needed

---

## Q19: PM REQUEST WORKFLOW (Conditional)

**Question:** If PM requests are part of pre-quote, what is the workflow?

**Answer:** PM involvement exists but not formal "PM request" process at pre-quote stage.

**Current Understanding:**
- PMs may be assigned to projects at different times:
  - Early: As part of team alignment from opportunity stage
  - Late: At order/kickoff stage
  - Ad-hoc: When project gets complex
- PM assignment is usually based on Account Manager assignment (they're part of same team)
- No formal "request for PM" workflow; more like team-based assignment

**Timing:**
- Ideally: PMs assigned at opportunity stage for early visibility of workload
- Reality: Often assigned at order stage (after quote is accepted)
- Challenge: Dates slip, scope changes, capacity conflicts

**Outstanding Discovery Needed:**
- Is there a formal PM request process?
- When should PM be assigned (pre-sale vs. post-sale)?
- What information does PM need?
- PM capacity/workload management

**[ACTION ITEM]** - Separate discovery session needed on PM request workflow and timing

**Confidence Rating: 50%** - PM assignment happens but formal process unclear.
- Previous: N/A (First pass)
- Rationale: PM workflow discussed but not in detail; needs dedicated session

**Outstanding Questions:**
- [ ] Formal PM request process exists?
- [ ] When is ideal PM assignment time?
- [ ] What information flows to PM at assignment?

---

## Q20: PROJECT FILE ORGANIZATION & SHAREPOINT INTEGRATION

**Question:** Where should project files be stored and how should they be organized?

**Answer:** KBMH is transitioning from Google Drive to SharePoint (via NetSuite integration).

**Current State:**
- Files stored in Google Drive
- Reaching capacity limits (Google Drive has item count limits, not just size)
- Manual file management and folder structure needed maintenance

**Future State (Orion/NetSuite):**
- Primary file storage: SharePoint (integrated with NetSuite)
- Access method: Can access from within NetSuite interface (appears as attached files)
- Drag-and-drop file upload into NetSuite records
- Files physically stored in SharePoint but accessible through NetSuite UI
- Automatic folder structure creation by system

**Exceptions (Remain in Google Drive):**
- Lookbooks
- CAT files (3D drawings)
- Other visual/design assets not directly part of order processing

**Orion to SharePoint Integration:**
- Quotes, POs, Invoices auto-saved to SharePoint via Orion
- Design requests, Labor quotes, etc. auto-save to SharePoint
- User never has to manually move files to SharePoint
- Clean central repository of all order-related documentation

**[REQUIREMENT: Type: Functional]** - System must integrate with SharePoint for file storage with files appearing attached to NetSuite records while physically stored in SharePoint folder structure.

**User Stories:**
- As PM, I need to upload project specifications to the project record so that I have one place to find all project documents.
- As Finance, I don't need to manually export and organize POs because they should automatically file to the right place.

**BRD Requirements:**
- [REQUIREMENT] NetSuite-SharePoint integration enabled
- [REQUIREMENT] Users can drag-and-drop files onto records (e.g., labor quote, design request, quote)
- [REQUIREMENT] Files automatically saved to SharePoint folder structure
- [REQUIREMENT] Folder structure mirrors NetSuite record hierarchy
- [REQUIREMENT] Users can access files from NetSuite interface without going to SharePoint directly
- [FUNCTIONALITY] PDF composer and other system-generated documents auto-save to SharePoint
- [CONSTRAINT] Lookbook and CAT files remain in Google Drive (not migrated to SharePoint)

**Evidence:**
- "So SharePoint, the SharePoint integration does allow you to drag and drop files right onto the NetSuite record. So let's just say at the opportunity level, or maybe it's at the labor quote or it's at the design request, but you can drag and drop a file right there onto that record in NetSuite and it saves it to SharePoint." - Marcus Dallacqua
- "But when you're in NetSuite, it looks like it's attached to that record." - Marcus Dallacqua
- "And there is a folder structure that we have a folder structure paradigm that will work with you on that looks pretty much like how most dealers are doing it in either SharePoint or Drive Now." - Marcus Dallacqua
- "So we'll see yours, Marcos, we'd be interested." - Matt Denning (re: proposed SharePoint folder structure)

**Confidence Rating: 85%** - Approach confirmed; need to see proposed folder structure.
- Previous: N/A (First pass)
- Rationale: Marcus clearly explained NetSuite-SharePoint integration; KBMH wants to review folder structure proposal

**[ACTION ITEM - MARCUS/CHRIS]** - Provide SharePoint folder structure proposal to KBMH for review

**Outstanding Questions:**
- [ ] What is the exact SharePoint folder structure recommendation?
- [ ] Timeline for cutover from Google Drive to SharePoint?
- [ ] What training is needed?

---

## Q21: REQUIREMENTS MAPPING & DECISIONS LOG

### REQ-001: Labor Quote Request Types
- **Type:** Functional
- **Status:** Confirmed
- **Decision:** Support Third Party and Intermarket labor quote types; Inactivate Internal and LTS types
- **Source:** Direct confirmation from Matt Denning
- **Implementation:** Configuration task

### REQ-002: Decentralized Labor Quote Initiation
- **Type:** Functional
- **Status:** Confirmed
- **Decision:** Multiple users (PM, AM) can initiate labor quote requests without centralized approval
- **Source:** Wendy Stark, Matt Denning
- **Implementation:** Role-based access control

### REQ-003: Labor Quote Markup Calculation (15% Formula Line)
- **Type:** Functional
- **Status:** Confirmed
- **Decision:** Automated 15% deduction from labor GP applied via formula line on all labor orders
- **Source:** Matt Denning, Marcus Dallacqua
- **Implementation:** Business rule configuration
- **Pending:** Technical screenshot of business rule

### REQ-004: Multiple Vendor Bidding
- **Type:** Functional
- **Status:** Confirmed
- **Decision:** Can send labor quote request to multiple vendors simultaneously
- **Source:** Wendy Stark, Matt Denning
- **Implementation:** Multi-select vendor feature in labor quote form

### REQ-005: Labor Quote Acceptance via PO Issuance
- **Type:** Functional
- **Status:** Confirmed
- **Decision:** Labor quote is "accepted" when PO is issued referencing the quote; no formal rejection process required
- **Source:** Matt Denning
- **Implementation:** Link between labor quote and PO

### REQ-006: Hold-Back Strategy for Labor Quotes
- **Type:** Functional
- **Status:** Confirmed
- **Decision:** Support itemized labor quote lines with selective PO issuance (e.g., quote 4 trips, issue PO for 1 trip, hold 3 as contingency)
- **Source:** Matt Denning, Kimi Katsuyoshi
- **Implementation:** Line-level selection in labor quote acceptance feature
- **Business Impact:** High - Core part of KBMH margin strategy

### REQ-007: Labor Quote Dashboard
- **Type:** Functional
- **Status:** Confirmed
- **Decision:** Create labor quote dashboard with visibility across all quotes, filterable by location/division/team member
- **Source:** Matt Denning, Marcus Dallacqua
- **Implementation:** Dashboard development task

### REQ-008: Itemized vs. Summary Labor Quote Import
- **Type:** Functional
- **Status:** Confirmed
- **Decision:** Support both itemized (multiple lines) and summary (single line) import of labor quotes to proposal
- **Source:** Matt Denning
- **Implementation:** Labor quote acceptance modal with format selector

### REQ-009: Labor Quote Traceability
- **Type:** Functional
- **Status:** Confirmed
- **Decision:** Maintain links between labor quote → proposal/quote → sales order → invoice for full cost visibility
- **Source:** Marcus Dallacqua
- **Implementation:** Relationship configuration in NetSuite

### REQ-010: Opportunity as Single Source of Truth (Pending Decision)
- **Type:** Non-Functional / Process
- **Status:** Proposed - Requires KBMH Decision
- **Decision Needed:** Confirm whether Opportunity should be single source of truth for scope information
- **Source:** Marcus Dallacqua, Matt Denning, Kimi Katsuyoshi
- **Implementation:** Process documentation and training

### REQ-011: Scope Auto-Population from Opportunity
- **Type:** Functional
- **Status:** Proposed - Dependent on REQ-010
- **Decision Needed:** If Opportunity is source of truth, should scope auto-populate to labor quote requests, design requests, etc.?
- **Source:** Marcus Dallacqua
- **Implementation:** Field mapping configuration

### REQ-012: Team Assignment at Customer Level
- **Type:** Functional
- **Status:** Confirmed
- **Decision:** Support pre-defined team assignments at customer level with override capability at opportunity/order level
- **Source:** Matt Denning
- **Implementation:** Customer record customization

### REQ-013: Resource Workload Dashboard
- **Type:** Functional
- **Status:** Confirmed
- **Decision:** Create resource dashboard showing PM/Designer workload and availability
- **Source:** Kimi Katsuyoshi
- **Implementation:** Dashboard development task

### REQ-014: Labor Quote Form Template Migration
- **Type:** Functional
- **Status:** Pending - Awaiting Current Form
- **Decision Needed:** Move labor quote request from email template to Orion system form
- **Source:** Matt Denning
- **Implementation:** Form development
- **Pending Item:** KBMH to provide current labor quote form template

### REQ-015: NetSuite-SharePoint Integration for Files
- **Type:** Functional
- **Status:** Confirmed
- **Decision:** Integrate SharePoint with NetSuite for project file storage; drag-and-drop files onto records
- **Source:** Marcus Dallacqua
- **Implementation:** SharePoint folder structure proposal needed
- **Pending Item:** [ACTION] Provide SharePoint folder structure recommendation

---

# DECISIONS LOG

| Decision # | Topic | Decision | Status | Confidence | Source |
|-----------|-------|----------|--------|------------|--------|
| D-001 | Labor Quote Types | Remove Internal/LTS; use Third Party + Intermarket | Confirmed | 85% | Matt Denning |
| D-002 | External Field Label | Change "External" to "Third Party" | Confirmed | 90% | Marcus Dallacqua |
| D-003 | 15% Labor Deduction | Implement formula line auto-deducting 15% from labor GP | Confirmed | 88% | Matt Denning |
| D-004 | Acceptance Method | Labor quote accepted when PO issued (not separate acceptance step) | Confirmed | 90% | Matt Denning |
| D-005 | Hold-Back Strategy | Support itemized labor quote lines with selective PO issuance | Confirmed | 92% | Matt Denning / Kimi |
| D-006 | Multi-Vendor Bidding | Allow labor quote to go to multiple vendors simultaneously | Confirmed | 90% | Wendy Stark |
| D-007 | Quote Format | Support both itemized and summary labor quote import to proposal | Confirmed | 88% | Matt Denning |
| D-008 | Decentralized Initiation | No centralized approval needed; PM/AM can initiate independently | Confirmed | 90% | Matt Denning |
| D-009 | Team Assignment | Use customer-level defaults with opportunity-level override | Confirmed | 82% | Matt Denning |
| D-010 | Scope Single Source | PENDING - Need KBMH decision on Opportunity as scope source of truth | Proposed | 72% | Leadership Decision Needed |

---

# OUTSTANDING ITEMS & ACTION ITEMS

## ACTION ITEMS - KBMH TEAM
- [ ] **Provide current labor quote request form/email template** - For form field validation and comparison with Orion template
  - Assigned to: Chris Trumble / Debbie Herbert
  - Due: Before next session

- [ ] **Provide design request form** - If design requests to be included in discovery
  - Assigned to: Chris Trumble / Debbie Herbert  
  - Due: Before design request session

- [ ] **Provide business rule screenshot** - 15% labor deduction formula line screenshot for documentation
  - Assigned to: Kip Herdrick
  - Due: Before next session

- [ ] **Confirm user count for license planning** - Matt to provide hard count of system users
  - Assigned to: Matt Denning
  - Due: End of day (per session)

- [ ] **Confirm Opportunity as single source of truth** - DECISION NEEDED on scope governance approach
  - Assigned to: Operations Leadership / Matt Denning
  - Due: Before next session

- [ ] **Schedule additional discovery sessions** - Design requests, PM requests, Finance topics
  - Assigned to: Debbie Herbert
  - Due: Schedule for December (avoid short Thanksgiving week)

## ACTION ITEMS - IMPLEMENTATION TEAM
- [ ] **Validate multiple labor quote acceptance with Joe (Orion)** - Confirm technical capability for accepting multiple labor quotes on same project
  - Assigned to: Marcus Dallacqua
  - Due: Before configuration phase

- [ ] **Propose automatic rejection logic** - Design potential auto-rejection of competing quotes by scope (not project-wide)
  - Assigned to: Marcus Dallacqua / Joe
  - Due: Before configuration phase

- [ ] **SharePoint folder structure proposal** - Create recommended folder structure for KBMH to review
  - Assigned to: Marcus Dallacqua / Chris Trumble / Tyler
  - Due: Before next session

- [ ] **Data migration planning with Joe** - Start conversation on extracting Core data for NetSuite migration
  - Assigned to: Marcus Dallacqua / Kip Herdrick
  - Due: Immediate (not too early to start)

- [ ] **Chart of Accounts review** - Chris team to continue working through COA mapping
  - Assigned to: Chris Trumble
  - Due: Continue work; report status

---

# NEXT STEPS

1. **KBMH Response to Action Items** - Collect outstanding documents/confirmations
2. **Schedule Follow-Up Sessions:**
   - Design Request Discovery Session (if applicable)
   - PM Request Discovery Session (if applicable)
   - Finance/Accounting Discovery Session
3. **Implementation Team Work:**
   - Validate technical capabilities with Joe (Orion)
   - Prepare SharePoint proposal
   - Begin data migration planning
4. **Review & Approval:** Present this questionnaire to KBMH for feedback and corrections

---

## UPDATE SUMMARY

**Update Date:** November 18, 2025

**New `In_` Files Analyzed:** 
- KBM-Hogue-Pre-Quote-Follow-up-5916b07e-0676.json (First KBMH discovery session transcript)

**Questions Addressed:**
- Q1: Labor Quote Request Types - ENHANCE ✅
- Q2: Labor Quote Request Initiation & Distribution - COMPLETE ✅
- Q3: Labor Quote Request Form Requirements - COMPLETE (Pending Form) 📋
- Q4: Labor Cost Calculation Methodology - COMPLETE ✅
- Q5: Internal Estimating & Rate Tables - COMPLETE ✅
- Q6: Labor Quote Acceptance & PO Issuance - COMPLETE ✅
- Q7: Multiple Labor Quotes Per Project - COMPLETE ✅
- Q8: Labor Quote Dashboard & Visibility - COMPLETE ✅
- Q9: Automatic Rejection Workflow - IDENTIFIED (Future Feature) 🔮
- Q10: Multiple Labor Quote Acceptance - VALIDATION NEEDED ⚠️
- Q11: Launch from Opportunity Records - CONFIRMED ✅
- Q12: Scope as Single Source of Truth - PROPOSED (Decision Pending) ⏳
- Q13: Scope Capture in Sales Process - COMPLETE ✅
- Q14: Labor Quote to Proposal Process - COMPLETE ✅
- Q15: Decentralized Acceptance Authority - COMPLETE ✅
- Q16: Order Team Assignment & Resources - COMPLETE ✅
- Q17: Resource Management & Workload - COMPLETE ✅
- Q18: Design Request Workflow - IDENTIFIED (Separate Discovery Needed) 📋
- Q19: PM Request Workflow - IDENTIFIED (Separate Discovery Needed) 📋
- Q20: Project File Organization & SharePoint - COMPLETE ✅

**Key Decisions Captured:**
1. Remove Internal/LTS labor quote types; use Third Party + Intermarket only
2. Rename "External" to "Third Party"
3. Implement 15% labor margin reduction via formula line (automated)
4. Support itemized labor quote lines with selective PO issuance (hold-back strategy)
5. Allow labor quote acceptance via PO issuance (no separate acceptance step)
6. Support multi-vendor bidding with simultaneous labor quote distribution
7. Decentralized labor quote initiation (no approval bottleneck)
8. Team assignment at customer level with opportunity-level override
9. Resource workload dashboard for capacity planning

**Confidence Improvements:**
- All Q1-Q8 items increased from 0% (no prior questionnaire) to 75-92% confidence
- Items requiring additional discovery maintained at 40-65% confidence pending clarification

**New Contradictions Identified:**
- None major; one clarification needed on Intermarket quote type final status (Marcus initially said inactivate, then reconsidered; appears to stay active)

**Outstanding Items Added:**
- [ ] Current labor quote form template needed
- [ ] Design request form needed (if applicable)
- [ ] Business rule screenshot for 15% deduction
- [ ] User count confirmation
- [ ] Scope governance decision (Opportunity as single source of truth)
- [ ] Multiple labor quote acceptance validation with technical team

**Key Insights from New Session:**
- KBMH is highly decentralized in labor quote management (multiple PMs/AMs initiating independently)
- Hold-back strategy is core to business model (quote high, issue lower PO, keep difference as margin)
- 60% of business is bid-based RFPs (scope changes significantly after initial bid)
- Everything goes to external vendors (no internal labor; removes Internal quote type assumption)
- SharePoint integration desired for file management (moving away from Google Drive limitations)
- Leadership needs to confirm scope governance approach (Opportunity vs. decentralized)

---

**Document Status:** Ready for KBMH Review & Feedback  
**Next Scheduled Activity:** Awaiting KBMH response to outstanding items; schedule design/PM/finance discovery sessions  
**Implementation Readiness:** 70% - Core pre-quote labor flow documented; design/PM/finance discovery needed before full BRD



# Questionnaire - Marketing
**Version**: 1.0  
**Date**: 2025-10-02  
**Process Area**: Marketing (Lead Acquisition & Lead Management interface)

## Change Log
- **Date**: 2025-10-02
- **Version**: 1.0
- **Sources**: Marketing/2 Input/MRK & CRM Outline & Questionnaire; Marketing/2 Input/Transcript MRK&CRM
- **Summary**: Initial questionnaire scaffold created. Pending population from transcript analysis.

## PROCESSED FILES
- Marketing/2 Input/MRK & CRM Outline & Questionnaire
- Marketing/2 Input/Transcript MRK&CRM

## Speaker Attribution Map
- Matt = Speaker 2 (Cornerstone)  
- Jill Marsh = Named in transcript  
- Kip = Speaker 7 (Cornerstone)  
- Alex Blangeres = Named in transcript  
- Kimmy = Speaker 1 (Cornerstone) (high confidence)  
- Marcus = Participant (speaker number not confirmed)  
- Kate = Participant referenced (speaker number not confirmed)  
- Carlos = Participant referenced (speaker number not confirmed)  
- Jillian = Participant referenced (speaker number not confirmed)  
- Others = Unconfirmed; left as generic Speaker N (Cornerstone)

## Decision Log
 - **REQ-001**: Limit Phase 1 scope for Email Marketing (ALIGNS) - "We won't plan for much there [email marketing]"; "It'll probably get underutilized" - Speaker 3 (Cornerstone) & Matt
- **REQ-002**: Enable targeted segmentation by role, sector, and location (ADAPT) - "We want to be able to tailor those markets by location and by what their focus may be"; "I need… to know how it works in terms of segmenting users and groups and the tagging" - Speaker 2 & Speaker 4 (Cornerstone)
 - **REQ-003**: Manage opt-in/unsubscribe natively in NetSuite (ALIGNS) - "NetSuite will manage that for you automatically"; need support for transactional emails outside campaign - Speaker 3 (Cornerstone) / Matt
- **REQ-004**: Support curated broker/PM lists for periodic value emails (ADAPT) - "If we had a curated list… quarterly market rates… I could see us using it [more]" - Kimmy
- **REQ-005**: Provide showroom event tracking and invitations (ALIGNS) - "Do you do any showroom events… you'll have the availability to do the email marketing inside of NetSuite" - Speaker 3 (Cornerstone)
- **REQ-006**: Provide visibility to marketing on leads/sectors to enable proactive content (ACCOMMODATE) - "If marketing had more insight into what some of those leads are… then it would be easier… to proactively create targeted email material" - Speaker 4 (Cornerstone)
 - **REQ-007**: Replace manual MailChimp/Excel uploads with NetSuite communications (ALIGNS) - "MailChimp gets really pissed off when you try to load in Excel… most of it bounces" - Matt
 - **REQ-008**: Implement internal vs external Project Status Reports with publish vs acknowledge dates (ACCOMMODATE) - "I need… a published date… status report showed the published dates… internal version and an external version" - Matt / Speaker 3 (Cornerstone)
 - **REQ-009**: Customized customer/project statement grouped by order with progress billing clarity (ACCOMMODATE) - "I need an accounting statement that shows you what you owed, how much you paid… group by order" - Matt
 - **REQ-010**: Migrate/ingest Zendesk data and tag for history (ALIGNS) - "Export the entire [CSV]… import it and tag it" - Kip / Speaker 3 (Cornerstone)

## Action Items
ACTION: Provide sample of current Project Status Report format (internal/external)  
ASSIGNED TO: Matt  
DUE: TBD  
RELATED TO: REQ-008

ACTION: Provide example of desired customer/project statement grouped by order  
ASSIGNED TO: Matt  
DUE: TBD  
RELATED TO: REQ-009

ACTION: Share inventory of existing reports and identify Phase 1 candidates  
ASSIGNED TO: Cornerstone team (Suggest: Sales Ops/Finance lead)  
DUE: TBD  
RELATED TO: REQ-010

ACTION: Confirm opt-in approach and unsubscribe handling for campaigns vs transactional  
ASSIGNED TO: Marketing lead (Suggest: Jill Marsh)  
DUE: TBD  
RELATED TO: REQ-003

## Additional Sessions Needed
### Session: Segmentation model and data ownership (Marketing x Sales)
- **Participants Needed**: Marketing lead, Sales leadership, CRM Admin
- **Questions to Address**: 
  • Required tags/fields for role, sector, location  
  • Ownership and maintenance responsibilities  
- **Priority**: High
- **Suggested Duration**: 60-90 minutes
- **Dependencies**: REQ-002, data dictionary draft

## New Questions Identified
### Proposed New Question: M-NEW-01. What fields and taxonomy are required to support targeted segmentation across role, sector, and location?
- **Asked By**: Speaker 4 (Cornerstone)
- **Context**: Desire to target campaigns and communications to segments
- **Suggested Placement**: Functional Requirements → Segmentation & Targeting
- **Evidence**: "I need… to know how it works in terms of segmenting users and groups and the tagging"

## Questionnaire Responses

### Scope Confirmation
**Answer:** Marketing-focused analysis based on session kickoff indicating "Marketing and Lead Management" technical focus.  
**Confidence Rating:** 90% - Session introduction explicitly frames marketing/lead management focus.  
**Evidence:** "Marketing. Marketing and Lead Management. So, it's going to be on the technical side of marketing and lead management." - Speaker 2 (Cornerstone)  
**Evidence:** "Marketing. Marketing and Lead Management. So, it's going to be on the technical side of marketing and lead management." - Matt  
**BRD Tags:** [DECISIONS] Scope area = Marketing; [ASSUMPTION] Lead Management intersections with CRM captured only where marketing-owned.

### 1. Current State Assessment (Marketing)
**Answer:**
- Web form leads route to marketing for initial qualification; many are low-value/cleaning quotes; occasional valuable existing-client inquiries.  
- Influencer-driven leads via GMs/business development dominate; RFPs come through relationships and trigger Asana requests to marketing.  
- Opportunities entered variably in Zendesk; data quality and visibility inconsistent; manual email sends and list uploads via MailChimp/Excel common.  
- Marketing report building and RFP time-tracking largely manual (Google Sheets, spreadsheets).  

**Evidence:**
- "Goes web form, lead creation… I qualify… most of the time… cleaning quote… then I delete" - Matt  
- "RFP will come in… relationship… formal project request through Asana to the marketing team" - Speaker 4 (Cornerstone)

**Confidence Rating:** 92% - Multiple direct quotes establish current state.

**BRD Tags:** [CONSTRAINT] Inconsistent data entry/visibility; [RISK] Manual processes; [REQUIREMENT] Improve intake and visibility.

### 2. Objectives & Strategy (Marketing)
**Answer:**
- Shift from mass emails to targeted, role/sector/location-based outreach.  
- Reduce manual tools and consolidate communications and tracking in NetSuite.  
- Provide curated broker/PM lists for periodic value communications (market rates).  

**Evidence:**
- "Targeted campaigns… tailor… by location and… focus" - Speaker 2 (Cornerstone)  
- "One-size-fits-all… no way right now to target" - Speaker 4 (Cornerstone)  

**Confidence Rating:** 90% - Repeated statements about targeting and tool consolidation.

### 3. Functional Requirements (Marketing)
**Answer:**
- Segmentation: tag by role, sector, location; list building; shared ownership with Sales. [REQUIREMENT] (ID: REQ-002, Type: Functional) [ADAPT]  
- Email compliance: opt-in/unsubscribe management; transactional vs campaign handling. [REQUIREMENT] (ID: REQ-003, Type: Non-Functional) [ALIGNS]  
- Events: support showroom event invites/tracking. [REQUIREMENT] (ID: REQ-005, Type: Functional) [ALIGNS]  
- Visibility: marketing view into leads/sectors for proactive content. [REQUIREMENT] (ID: REQ-006, Type: Functional) [ACCOMMODATE]  
- Reporting: internal/external Project Status Reports with publish date; customer/project statements grouped by order. [REQUIREMENT] (ID: REQ-008/REQ-009, Type: Functional) [ACCOMMODATE]

**Evidence:** See Decision Log quotes for each requirement.

**Confidence Rating:** 90% - Direct asks recorded.

### 4. Technical Requirements (Marketing)
**Answer:**
- Data migration: export Zendesk CSV; import to NetSuite with tagging. [REQUIREMENT] (ID: REQ-010, Type: Non-Functional) [ALIGNS]  
- Email: support opt-in status, unsubscribe, and transactional sends outside campaigns. [REQUIREMENT] (ID: REQ-003, Type: Non-Functional) [ALIGNS]  
- Integrations: optional file links to Google Drive in project custom fields; potential SharePoint for NetSuite-linked files. [ASSUMPTION] Marketing artifacts may live externally.  

**Evidence:** "Export… CSV… import it and tag it"; "NetSuite will manage [unsubscribe]"; "Insert links back to Google Drive… custom fields".

**Confidence Rating:** 85% - Some details will need confirmation.

### 5. Implementation Alignment / Decisions
**Answer:**
- Email marketing in Phase 1 minimal use: ALIGNS  
- Segmentation model: ADAPT (process adjustment without customization)  
- Marketing visibility to leads/sectors: ACCOMMODATE (likely needs config/custom views)  
- Status reports and project/customer statements: ACCOMMODATE (solution design required)

**Evidence:** See Decision Log.

**Confidence Rating:** 88% - Classifications consistent with definitions.

## Outstanding Items Summary
- Populate Decision Log with REQ-### and quotes
- Extract Action Items with WHO/WHAT/WHEN
- Identify any explicitly requested follow-up sessions
 - Confirm segmentation data model and ownership
 - Collect sample templates for status report and statement



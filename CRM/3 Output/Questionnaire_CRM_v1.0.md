# Questionnaire - CRM
**Version**: 1.0  
**Date**: 2025-10-02  
**Process Area**: CRM

## Change Log
- **Date**: 2025-10-02
- **Version**: 1.0
- **Sources**: Marketing/2 Input/Transcript MRK&CRM
- **Summary**: Initial scaffold for CRM questionnaire.

## PROCESSED FILES
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
- **CRM-REQ-001**: Use Orion Kanban Boards for opportunity pipeline (ALIGNS) - "Your opportunities have statuses… you can visually move through the status"; "I think it'd be a good tool for us to try and test out" - Speaker 3 (Cornerstone) & Matt
- **CRM-REQ-002**: Restrict opportunity visibility to assigned users (ADAPT) - "Restricted their opportunities to only the ones that they're on. It does that natively" - Speaker 3 (Cornerstone)
- **CRM-REQ-003**: Forecast only opportunities at 70%+ probability (ADAPT) - "We don't forecast anything below 70%… whenever we say forecast, it's 70% or greater" - Speaker 1 (Cornerstone) / Matt
- **CRM-REQ-004**: Create Sales Goals dashboard in NetSuite to replace Excel (ACCOMMODATE) - "You want that to live in NetSuite? — Yes. Yes… a dashboard" - Speaker 3 (Cornerstone) & Matt
- **CRM-REQ-005**: Default GP target 22% with customer overrides on opportunities (ADAPT) - "We have a target GP goal… 22%"; "Field on the customer… sources through the opportunity… user can override" - Matt & Speaker 3 (Cornerstone)
- **CRM-REQ-006**: Enable mobile Quick Add Lead for reps (ALIGNS) - "NetSuite mobile app… a really good one is Quick Add Lead" - Speaker 3 (Cornerstone)
- **CRM-REQ-007**: Import Zendesk history via CSV with tagging (ALIGNS) - "You can export the entire… CSV… import it and tag it" - Kip & Speaker 3 (Cornerstone)
- **CRM-REQ-008**: Provide basic Customer Portal for quotes/invoices (ALIGNS) - "We do have a customer portal… see open quotes… open invoices" - Speaker 3 (Cornerstone)
- **CRM-REQ-009**: Support sales team commission splits (FUTURE) - "Sometimes… start out as a team… historically… even split… bigger conversation" - Speaker 2 (Cornerstone)
- **CRM-REQ-010**: Track KPIs: pipeline, forecast accuracy, win/loss trends (ADAPT) - "Forecasted versus actual… identify trends… reporting is so manual" - Speaker 1/7 (Cornerstone)

## Action Items
ACTION: Provide current Sales Goals Excel and layout for dashboard recreation  
ASSIGNED TO: Speaker 2 / Kip (Cornerstone)  
DUE: TBD  
RELATED TO: CRM-REQ-004

ACTION: Confirm final rule for opportunity visibility (assigned-only vs discovery)  
ASSIGNED TO: Sales leadership (Suggest: GM lead)  
DUE: TBD  
RELATED TO: CRM-REQ-002

ACTION: Provide list of CRM KPIs and definitions (pipeline, accuracy, win/loss)  
ASSIGNED TO: Sales Ops (Suggest: Speaker 1 + Speaker 7)  
DUE: TBD  
RELATED TO: CRM-REQ-010

## Additional Sessions Needed
### Session: Opportunity security and discovery policy
- **Participants Needed**: Sales leadership, CRM Admin
- **Questions to Address**: 
  • Assigned-only visibility vs limited discovery  
  • Access to accounts vs contacts vs activities  
- **Priority**: High
- **Suggested Duration**: 60 minutes
- **Dependencies**: CRM-REQ-002

## New Questions Identified
### Proposed New Question: C-NEW-01. What is the standard probability threshold for inclusion in forecast and dashboards?
- **Asked By**: Speaker 3 (implicit policy confirmation)
- **Context**: Team states 70%+; needs configuration alignment
- **Suggested Placement**: Forecast/Pipeline Management
- **Evidence**: "We don't forecast anything below 70%"

## Questionnaire Responses
### Scope Confirmation
**Answer:** CRM-focused requirements covering leads, opportunities, pipeline, forecasting, security, KPIs, and portals.  
**Confidence Rating:** 90% - CRM discussion sections are explicit.  
**Evidence:** "After this… who will be part of the CRM discussion…" - Speaker 3 (Cornerstone)

### Current State Assessment (CRM)
**Answer:**
- Opportunities entered in Zendesk by sales or account managers; varying data quality and activity logging; global activity feed causes culture/visibility issues.  
- Forecasting managed manually; Excel-based sales goals and KPI tracking distributed weekly; pipeline visibility is fragmented by views.  

**Evidence:**
- "There is a company-wide feed… every change… you can doom-scroll" - Matt  
- "Custom report… dumped into… Excel… pushed out once a week" - Kip

**Confidence Rating:** 92% - Multiple direct quotes.

### Objectives & Strategy (CRM)
**Answer:**
- Standardize pipeline and forecasting in Orion; adopt Kanban boards for opportunity management.  
- Replace manual Excel reports with NetSuite dashboards; improve KPI accuracy and trend analysis.  
- Enforce sensible security: restrict by assignment while enabling necessary discovery.  

**Evidence:**
- "Good tool… to try and test out" [Boards]; "You want that to live in NetSuite? — Yes" [Dashboard].

**Confidence Rating:** 90%.

### Functional Requirements (CRM)
**Answer:**
- Pipeline Boards for opportunities with status drag-and-drop. [REQUIREMENT] (ID: CRM-REQ-001, Type: Functional) [ALIGNS]  
- Opportunity visibility restricted to assigned users; policy confirmation and exceptions. [REQUIREMENT] (ID: CRM-REQ-002, Type: Non-Functional) [ADAPT]  
- Forecast inclusion rule: 70%+ probability. [REQUIREMENT] (ID: CRM-REQ-003, Type: Non-Functional) [ADAPT]  
- Sales team commission splits handling. [REQUIREMENT] (ID: CRM-REQ-009, Type: Functional) [FUTURE]

**Evidence:** See Decision Log.

**Confidence Rating:** 88% - One open policy decision remains (visibility nuances).

### Technical Requirements (CRM)
**Answer:**
- Sales goals dashboard and KPIs in NetSuite to replace Excel (exec vs rep views). [REQUIREMENT] (ID: CRM-REQ-004, Type: Functional) [ACCOMMODATE]  
- Default GP target 22% with customer-level default and opportunity override. [REQUIREMENT] (ID: CRM-REQ-005, Type: Functional) [ADAPT]  
- Mobile app Quick Add Lead. [REQUIREMENT] (ID: CRM-REQ-006, Type: Functional) [ALIGNS]  
- Zendesk CSV import with tagging. [REQUIREMENT] (ID: CRM-REQ-007, Type: Non-Functional) [ALIGNS]  
- Customer portal (quotes/invoices) available; enable as needed. [REQUIREMENT] (ID: CRM-REQ-008, Type: Functional) [ALIGNS]

**Evidence:** Quotes in Decision Log sections.

**Confidence Rating:** 90%.

### Implementation Alignment / Decisions
**Answer:**
- Boards and mobile lead add: ALIGNS.  
- Forecasting 70%+ and visibility policies: ADAPT (configuration, governance).  
- Sales goals dashboard and GP defaults/overrides: ACCOMMODATE/ADAPT (configuration and minor solution design).  
- Customer portal basic: ALIGNS; commission splits: FUTURE.

**Evidence:** See Decision Log.

**Confidence Rating:** 88%.

## Outstanding Items Summary
- Extract CRM decisions with quotes
- Populate requirements and user stories


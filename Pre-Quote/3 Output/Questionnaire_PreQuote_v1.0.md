# Questionnaire - Pre-Quote
**Version**: 1.0  
**Date**: October 16, 2025  
**Process Area**: Pre-Quote (Labor Quote Requests, Design Requests, Estimating, Project Requests)

## Change Log
- **Date**: October 16, 2025
- **Version**: 1.0
- **Sources**: Master_Transcript_Pre-Quote.md, Discovery Workflow Specification.md
- **Summary**: Initial comprehensive questionnaire analysis completed from Pre-Quote master transcript covering labor quote request types, estimating workflows, vendor management, union requirements, CAM reservations, and project request forms.

## PROCESSED FILES
- Pre-Quote/2 Input/Master_Transcript_Pre-Quote.md (273 lines)
- Pre-Quote/2 Input/Discovery Workflow Specification.md (87 lines)
- Sources: Pre-Quote Transcript.txt, Labor Quote documents, Project Request Review documents

## Speaker Attribution Map
- **Marcus Dallacqua** = Implementation Team/Consultant
- **Chris Trumble** = Implementation Team
- **Gary Strickland** = Consultant

## Decision Log

### Labor Quote Request Types
- **REQ-001**: Support multiple labor quote request types (Internal, External, Intermarket, LTS) (ALIGNS) - "Yeah, it's two different request types. So you would create a request type specific for labor quote internal, another one for labor quote external, another one for labor quote internal, intermarket, something like that. Yep. But they're all pretty easy to make." - Marcus Dallacqua

### Request Engine
- **REQ-002**: Use Orion request engine to replace Bridge functionality (ALIGNS) - "We're in good shape because Bridge is very similar to Connect, which Joe built. And then Joe brought a lot of that functionality into Orion. So in fact, I think our request engine is going to better than what they have in Bridge." - Marcus Dallacqua

### Union Requirements
- **REQ-003**: Track union/non-union status on vendor records (ACCOMMODATE) - "So that's a, that's something that we need to find out. Maybe not discovery but just a takeaway for us to do. We do we track vendors and if they're union or not on our vendor record." - Marcus Dallacqua

### Vendor Location Management
- **REQ-004**: Identify service vendors by COR location using custom field (ACCOMMODATE) - "So here's a requirement and it's a pretty easy one for us to do. I know this is kind of early in the process, but just for a note, we'll need a requirement to identify service vendors in NetSuite by COR location." - Marcus Dallacqua

### Vendor Relationships
- **REQ-005**: Support parent-child vendor relationships for multi-location service (ACCOMMODATE) - "If the vendors service multiple or their parent company have divisions, we would probably want to use parent child on the vendor record." - Gary Strickland

### CAM Reservation System
- **REQ-006**: Provide field for CAM reservation number (manual entry, no integration) (ALIGNS) - "No, there's actually no integration. What they're doing here, they're just. They're doing it one system and copying the number over into their current system through Bridge. And we would have them do the same thing. We'll just have a field for a reservation number." - Marcus Dallacqua

### Labor Quote Calculations
- **REQ-007**: Support manual labor calculations with notes field for institutional knowledge (ADAPT) - "The team manually calculates rate in hours and adds the total to the cost column. So, okay, so they're not actually doing the calculations in here, they're doing it outside the system and then manually plugging them in here, which is fine." - Marcus Dallacqua

### Labor Quote Acceptance
- **REQ-008**: Implement labor quote acceptance workflow (standard Orion feature not in Bridge) (ACCOMMODATE) - "So there's all these quotes that come back, especially if you're going external. And then at some point you have to say, okay, for this quote, I'm going to accept for this, sorry, this quote record in netsuite. I'm going to accept this labor quote." - Marcus Dallacqua

### Request Rejection Workflow
- **REQ-009**: Enable request rejection/send back for more information workflow (ACCOMMODATE) - "So they have a process where if you don't give them enough information, they can send it back for more information. Chris, will you just make a note for Joe to make sure that I think we have a process for that on the labor quote request." - Marcus Dallacqua

### Request Initiation Point
- **REQ-010**: Launch labor quote requests from Opportunity/Quote records (not Project record) (ADAPT) - "They initiate these estimating or requests for estimates from the project record in Orion. They'll do it from the opportunity record or the quote record, not necessarily the project record... That's something to make sure that we emphasize during discovery. That'll be a shift in their process, something that they'll have to adapt to." - Marcus Dallacqua

### Project Scope Capture
- **REQ-011**: Capture project scope details on labor quote form (not project record) (ADAPT) - "So this is interesting. Okay, so like they're filling out the project scope details and we would typically do this elsewhere... we would do this on the. On the labor quote form, not on the project form." - Marcus Dallacqua

### Site Conditions Record
- **REQ-012**: Use job site analysis/site conditions record for site information (ALIGNS) - "Just so you know, Gary, our site conditions record is attached to the address... We have all of this on the site conditions record. Or I think. Is it called site conditions or job site analysis?" - Marcus Dallacqua

### Pending Quote Dashboard
- **REQ-013**: Provide pending quote dashboard showing RFQs sent to subcontractors (ACCOMMODATE) - "So then there's a little dashboard pending quote pending from sub so they could see everything they sent out for bid... We need to figure out if we have that on the labor quote. I think that there might be a section on the labor quote that shows everybody that they sent it to and the status." - Marcus Dallacqua

### Project Request Form
- **REQ-014**: Configure project request form with checkboxes (Estimating needed, Design needed, PM needed) (ALIGNS) - "So this kind of follows the same path. Enbridge. They start with the project request and then if estimating is needed, they mark it. Oh, it's interesting here on this project request, do you need estimated. Is the estimated needed. Design needed, PM needed?" - Marcus Dallacqua

### Document Attachments
- **REQ-015**: Support CAP/SIF file attachments and project documentation (ALIGNS) - "Good. They're just. Yeah, they're just attaching documents, which is fine. That's where that SharePoint integration is gonna be really helpful for them." - Marcus Dallacqua

### RFQ Form Branding
- **REQ-016**: Provide request for quote form with COR branding (ALIGNS) - "We have a nice request for quote. So this is their form, I guess, you know, for their request for quote during discovery. We'll ask them if they want to upgrade this." - Marcus Dallacqua

### Vendor Filtering
- **REQ-017**: Support vendor filtering by union status, intermarket, and location (ACCOMMODATE) - "Yeah, yeah. And then union intermarket. Okay. So this is where they differentiate between union, non union, intermarket. Yeah. And then cor. So we'll have to figure out like what that list of drop downs are." - Marcus Dallacqua

## Action Items

ACTION: Determine if NetSuite currently tracks union status on vendor records; if not, create custom field  
ASSIGNED TO: Joe (Implementation Team) - via Chris/Marcus  
DUE: Before vendor configuration  
RELATED TO: REQ-003

ACTION: Define dropdown values for union/non-union/intermarket vendor classification  
ASSIGNED TO: COR Operations Team  
DUE: Discovery session  
RELATED TO: REQ-003, REQ-017

ACTION: Determine if location field on vendor record should be multi-select for multi-location vendors  
ASSIGNED TO: Marcus/Joe  
DUE: During vendor configuration design  
RELATED TO: REQ-004, REQ-005

ACTION: Confirm labor quote pending status tracking functionality exists in request engine  
ASSIGNED TO: Joe/Luke/Chris  
DUE: Before labor quote configuration  
RELATED TO: REQ-013

ACTION: Confirm request rejection workflow capability in request engine  
ASSIGNED TO: Joe  
DUE: Before labor quote configuration  
RELATED TO: REQ-009

ACTION: Clarify CAP/SIF file handling requirements (PDF export vs. SIF import)  
ASSIGNED TO: COR Operations Team  
DUE: Discovery session  
RELATED TO: REQ-015

ACTION: Obtain documentation for Design request and PM request workflows  
ASSIGNED TO: COR Operations Team / SharePoint access  
DUE: Next discovery phase  
RELATED TO: REQ-014

ACTION: Develop labor quote request forms for all request types  
ASSIGNED TO: Implementation Team (Form Development)  
DUE: Configuration phase  
RELATED TO: REQ-001, REQ-007, REQ-011

ACTION: Document institutional knowledge formulas for labor calculations (e.g., X times 1.52 rounded to nearest 50)  
ASSIGNED TO: COR Operations Team  
DUE: Discovery session  
RELATED TO: REQ-007

ACTION: Schedule preview session for request engine and labor quote acceptance workflow  
ASSIGNED TO: Marcus/Chris  
DUE: Before detailed design phase  
RELATED TO: REQ-002, REQ-008

## Additional Sessions Needed

### Session: Design Request Process Deep Dive
- **Participants Needed**: Design Manager (Rafina mentioned in Operations transcript), Sales team, Operations team
- **Questions to Address**: 
  • What triggers a design request?
  • What information is captured on the design request form?
  • How are designers assigned?
  • What deliverables are produced?
  • How does this integrate with the quote process?
- **Priority**: High (mentioned as missing documentation)
- **Suggested Duration**: 60-90 minutes
- **Dependencies**: REQ-014 (Project request form checkboxes)
- **Evidence**: "So one thing we need to look for, and we don't have it in this bucket right now of pre quote, but there should be documentation for design and PM requests. So that should be in this pre quote section as well." - Marcus Dallacqua

### Session: PM Request Process Deep Dive
- **Participants Needed**: PM Manager (Wendy mentioned in Operations transcript), Sales team, Operations team
- **Questions to Address**: 
  • What triggers a PM request?
  • What information is captured on the PM request form?
  • How are PMs assigned?
  • What is the handoff process?
  • How does PM involvement impact the quote?
- **Priority**: High (mentioned as missing documentation)
- **Suggested Duration**: 60-90 minutes
- **Dependencies**: REQ-014 (Project request form checkboxes)
- **Evidence**: "So one thing we need to look for, and we don't have it in this bucket right now of pre quote, but there should be documentation for design and PM requests. So that should be in this pre quote section as well. Chris, do you have access to SharePoint?" - Marcus Dallacqua

### Session: Vendor Management and Subcontractor Selection
- **Participants Needed**: Operations team, Procurement, Vendor managers
- **Questions to Address**: 
  • Complete list of vendor classification values (union, non-union, intermarket)?
  • How many COR locations need vendor assignments?
  • What vendors service multiple locations?
  • How do you select vendors for RFQs?
  • What are the criteria for preferred vendors?
- **Priority**: Medium (needed for configuration)
- **Suggested Duration**: 60 minutes
- **Dependencies**: REQ-003, REQ-004, REQ-005, REQ-017
- **Evidence**: "So we'll have to figure out like what that list of drop downs are. And you know, we might be able to handle that better than how they're doing it now. So we'll definitely dig in during discovery on that." - Marcus Dallacqua

### Session: Long Term Storage (LTS) Quote Process
- **Participants Needed**: Warehouse team, Operations team, Sales team
- **Questions to Address**: 
  • How is cubic footage calculated?
  • What are the warehouse rate structures?
  • How often do rates change?
  • What information needs to flow to warehouse for LTS quotes?
  • How are monthly storage invoices handled?
- **Priority**: Medium (covered briefly in transcript)
- **Suggested Duration**: 45-60 minutes
- **Dependencies**: REQ-001 (LTS request type)
- **Evidence**: "Long term storage quote process, which we've already covered in quoting, but I guess. Or in order management, but I guess it also falls in here too, because you're going to get a quote from the warehouse." - Marcus Dallacqua

## New Questions Identified

### Proposed New Question: 1. What institutional knowledge formulas are used for labor calculations?
- **Asked By**: Chris Trumble (identified during review)
- **Context**: COR has specific calculation formulas (e.g., X times 1.52 rounded to nearest 50) that represent institutional knowledge
- **Suggested Placement**: Labor Quote Calculations section
- **Evidence**: "There's like a little institutional knowledge there where it says like if you go back up it says It's X times 1.52 rounded to the nearest 50. Even if there's like a notes field or somewhere where we can capture that." - Chris Trumble

### Proposed New Question: 2. What is the labor quote acceptance procedure in Bridge?
- **Asked By**: Marcus Dallacqua (identified gap)
- **Context**: Orion has a labor quote acceptance feature that Bridge may not have
- **Suggested Placement**: Labor Quote Workflow section
- **Evidence**: "So they have the ability there to consolidate that or summarize that or itemize it because some might need itemized. That step is called labor quote acceptance. And I don't think they have that. I'm not sure if they have that here in Bridge or not. I haven't seen it yet. But just so you know, something we'll look for in discovery is if they have a labor quote acceptance procedure." - Marcus Dallacqua

### Proposed New Question: 3. How are rate tables currently managed for labor quotes?
- **Asked By**: Marcus Dallacqua (future functionality discussion)
- **Context**: Orion could support rate table calculations in the future
- **Suggested Placement**: Labor Quote Calculations section
- **Evidence**: "Ideally, eventually what we want to do is have the ability for them to do their Calculations right in the system based on rate tables. We have a lot of dealers who want that, but we don't have that currently." - Marcus Dallacqua

## Questionnaire Responses

---

## 1. OVERVIEW AND CURRENT STATE

### 1.1. What systems are currently used for pre-quote processes?

**Answer:**
Creative Office Resources currently uses Bridge for their pre-quote processes, including:
- Labor quote requests (internal, external, intermarket, LTS)
- Project request forms
- Request for quote (RFQ) generation and distribution
- Pending quote tracking
- Estimating workflows

**User Stories:**
- As an Operations Team Member, I need to manage multiple labor quote request types so that I can route work appropriately between internal resources, external subcontractors, intermarket partners, and long-term storage facilities.
- As a Quoting Team Member, I need to track all pending quotes sent to subcontractors so that I can follow up on outstanding requests and ensure timely responses.

**Current State Process:**
**PROCESS**: Labor Quote Request  
**TRIGGER**: Sales Account Manager identifies need for labor quote during opportunity development  
**STEPS**:
1. Sales completes project request form → Form flows to shared email inbox
2. Quoting team reviews request → Determines quote type (Internal, External, Intermarket, LTS)
3. Quoting team creates labor quote request in Bridge → Selects appropriate request type
4. If external, quoting team filters vendors by union status and location → Sends RFQ to subcontractors
5. Quoting team tracks pending quotes in dashboard → Monitors responses
6. Team receives quote responses → Manually calculates totals → Enters into cost columns
7. Quote completed and sent to Sales → Sales team determines next steps

**SYSTEMS INVOLVED**: Bridge (request management), CAM (Customer Asset Management - reservation numbers), CAP (specification software for SIF files), Email (notifications), External calculation tools (Excel for rate calculations)

**PAIN POINTS**: 
- Manual calculations outside system
- No labor quote acceptance workflow visible
- Limited integration between systems (CAM numbers manually copied)
- Institutional knowledge captured in external formulas
- Multiple systems for document management

**BRD Requirements:**
- [REQUIREMENT] Support multiple labor quote request types (Internal, External, Intermarket, LTS) (ID: REQ-001, Type: Functional)
- [REQUIREMENT] Replace Bridge functionality with Orion request engine (ID: REQ-002, Type: Functional)
- [FUNCTIONALITY] Request engine with customizable request types
- [PRIORITY] Must-Have

**Stakeholder Impact:**
- **Primary Users**: Quoting Team, Operations Team
- **Secondary Users**: Sales Account Managers (initiators)
- **Approvers**: Operations Manager

**Evidence:**
- "The quoting team toggles between quoting and intermarket quote requests. Okay. So they have different quote request types." - Marcus Dallacqua
- "Yeah, I did notice that. So they're using Bridge for this, which, you know, again we have. We're in good shape because Bridge is very similar to Connect, which Joe built." - Marcus Dallacqua

**Confidence Rating**: 95% - Direct transcript evidence with clear current system identification and process walkthrough

---

### 1.2. What are the different types of labor quote requests?

**Answer:**
COR uses four distinct labor quote request types:
1. **Internal** - Labor performed by COR's own employees
2. **External** - Labor performed by external subcontractors
3. **Intermarket** - Labor provided by another COR location/market
4. **LTS (Long Term Storage)** - Warehouse storage services with monthly rates

Each request type requires its own configuration in the request engine, with different fields and workflows appropriate to each type.

**User Stories:**
- As a Quoting Team Member, I need to select the appropriate labor quote type so that the request is routed to the correct resources with the appropriate fields and requirements.
- As an Operations Manager, I need to differentiate between labor types so that I can track utilization of internal resources vs. external subcontractors vs. storage services.

**BRD Requirements:**
- [REQUIREMENT] Create separate request types for Internal, External, Intermarket, and LTS labor quotes (ID: REQ-001, Type: Functional)
- [FUNCTIONALITY] Request engine supporting multiple request type configurations
- [PRIORITY] Must-Have

**Stakeholder Impact:**
- **Primary Users**: Quoting Team
- **Secondary Users**: Internal labor resources, Warehouse team, Subcontractors

**Evidence:**
- "So labor quote request types. Which is fine. We support that. That maps over to our request engine that can. Can create different types of labor quotes. Internal, external, intermarket, in. In. That's fine." - Marcus Dallacqua
- "Yeah, it's two different request types. So you would create a request type specific for labor quote internal, another one for labor quote external, another one for labor quote internal, intermarket, something like that." - Marcus Dallacqua
- "Oh, LTS is long term storage." - Chris Trumble

**Confidence Rating**: 97% - Explicitly stated with clear definitions and implementation approach

---

## 2. LABOR QUOTE REQUIREMENTS

### 2.1. What union labor requirements exist?

**Answer:**
COR must comply with union labor requirements that are generally dictated by building owners. Key requirements:
- Building owners may require union workers for specific projects
- If union workers are required, work must be performed by union subcontractors (cannot be quoted internally)
- The labor request becomes an external request when union labor is required
- Vendor records need to track union vs. non-union status for proper subcontractor selection

This is a critical filtering criterion when selecting vendors for external labor quote requests.

**User Stories:**
- As a Quoting Team Member, I need to know which vendors are union-certified so that I can only send RFQs to appropriate subcontractors when the building owner requires union labor.
- As an Operations Manager, I need to track vendor union status so that we remain compliant with building owner requirements and avoid costly mistakes.

**BRD Requirements:**
- [REQUIREMENT] Track union/non-union status on vendor records with custom field (ID: REQ-003, Type: Functional)
- [REQUIREMENT] Support vendor filtering by union status when creating external labor requests (ID: REQ-017, Type: Functional)
- [CONSTRAINT] Building owner requirements dictate union labor necessity
- [RISK] Non-compliance could result in project delays, contract violations, or rework
- [PRIORITY] Must-Have

**Stakeholder Impact:**
- **Primary Users**: Quoting Team (vendor selection)
- **Approvers**: Operations Manager, Legal/Compliance (implicit)
- **Impacted Parties**: Subcontractors, Building owners, Sales team

**Evidence:**
- "They have union. So that's a key call out is they have union requirements generally dictated by the building owners. If union workers are required, the work must come from a union subcontractor." - Marcus Dallacqua
- "So when they say cannot be quoted internally, then that just means that they have to select a contract. The labor request becomes an external request and it has to go to one of the ones that uses union labor." - Chris Trumble

**Confidence Rating**: 96% - Clear requirement with direct quotes and compliance implications

---

### 2.2. How are vendors selected and filtered for labor quotes?

**Answer:**
Vendor selection for external labor quotes requires filtering by three primary criteria:

1. **Union Status**: Union, Non-union, or capability for both
2. **COR Location**: Vendors are associated with specific COR locations/markets
3. **Intermarket Classification**: Whether vendor can work across multiple COR markets

The current Bridge system allows quoting team to filter vendors by these criteria to generate the appropriate vendor list for RFQ distribution. Some vendors may service multiple locations through parent-child relationships (e.g., Marcus Installation with Massachusetts office and New York office).

**User Stories:**
- As a Quoting Team Member, I need to filter vendors by location, union status, and intermarket capability so that I only send RFQs to vendors who can actually perform the work.
- As a Vendor Manager, I need to maintain accurate vendor records with location and union information so that we select the right subcontractors for each project.

**Current State Process:**
**PROCESS**: External Vendor Selection  
**TRIGGER**: Labor quote request determined to be external  
**STEPS**:
1. Quoting team identifies project requirements (location, union status) → Determines filtering criteria
2. Team accesses vendor filtering in Bridge → Selects union/non-union/intermarket dropdown
3. System filters vendors by COR location → Presents qualified vendor list
4. Team selects vendors from filtered list → Generates and sends RFQs
5. Vendors receive RFQs → Submit quote responses

**SYSTEMS INVOLVED**: Bridge (vendor management and filtering)

**BRD Requirements:**
- [REQUIREMENT] Add custom location field to service vendor records sourced from COR locations (ID: REQ-004, Type: Functional)
- [REQUIREMENT] Implement parent-child vendor relationships for multi-location service providers (ID: REQ-005, Type: Functional)
- [REQUIREMENT] Support vendor filtering by union status, intermarket capability, and location (ID: REQ-017, Type: Functional)
- [FUNCTIONALITY] Vendor record customization, Multi-select location field (potential), Filtering logic
- [SOLUTIONDESIGN] Custom fields on vendor record, Filtering interface in labor quote creation
- [PRIORITY] Must-Have

**Stakeholder Impact:**
- **Primary Users**: Quoting Team
- **Secondary Users**: Vendor managers, Procurement
- **Impacted Parties**: Subcontractors

**Evidence:**
- "It looks like this is where they're kind of drilling down where union, non union. But the vendors are set up. So they've got to have something on the vendor record that says it's union or non union." - Gary Strickland
- "Yeah, I think so. But then also they're also dependent on the location, the COR location, which makes sense. So we probably then need to identify our vendors by location. At least the service vendors." - Marcus Dallacqua
- "So here's a requirement and it's a pretty easy one for us to do... we'll need a requirement to identify service vendors in NetSuite by COR location." - Marcus Dallacqua
- "If the vendors service multiple or their parent company have divisions, we would probably want to use parent child on the vendor record." - Gary Strickland

**Confidence Rating**: 94% - Well-supported by discussion with clear implementation approach, though specific dropdown values need to be defined

---

### 2.3. How are labor quote calculations performed?

**Answer:**
Labor quote calculations are currently performed **outside the system** (likely in Excel or similar tools) and then manually entered into Bridge. The process involves:

- Quoting team manually calculates rate × hours
- Team applies institutional knowledge formulas (e.g., "X times 1.52 rounded to nearest 50")
- Total calculated values are entered into the cost column in Bridge
- System does not currently perform calculations based on rate tables

This approach means that institutional knowledge about calculation formulas exists outside the system and needs to be captured in notes or documentation fields. The implementation team noted that while rate table functionality would be ideal for the future, it is not currently available in Orion.

**User Stories:**
- As a Quoting Team Member, I need to enter manually calculated labor costs so that I can include institutional knowledge and company-specific formulas in my calculations.
- As an Operations Manager, I need to capture the rationale behind calculation formulas so that new team members can understand and replicate our quoting methodology.

**BRD Requirements:**
- [REQUIREMENT] Support manual labor calculation entry with notes field for formulas and institutional knowledge (ID: REQ-007, Type: Functional)
- [FUNCTIONALITY] Labor quote form with cost entry fields and notes/comments capability
- [ASSUMPTION] Calculations will continue to be performed externally until rate table functionality is developed
- [CONSTRAINT] Current Orion functionality does not support rate table-based calculations
- [PRIORITY] Must-Have (manual entry), Nice-to-Have (rate table functionality for future)

**Stakeholder Impact:**
- **Primary Users**: Quoting Team
- **Impacted Parties**: Finance (validation), Sales (pricing)

**Evidence:**
- "The team manually calculates rate in hours and adds the total to the cost column. So, okay, so they're not actually doing the calculations in here, they're doing it outside the system and then manually plugging them in here, which is fine." - Marcus Dallacqua
- "Yeah, we could support that. That's not a problem. Ideally, eventually what we want to do is have the ability for them to do their Calculations right in the system based on rate tables. We have a lot of dealers who want that, but we don't have that currently." - Marcus Dallacqua
- "There's like a little institutional knowledge there where it says like if you go back up it says It's X times 1.52 rounded to the nearest 50. Even if there's like a notes field or somewhere where we can capture that." - Chris Trumble

**Confidence Rating**: 95% - Explicit discussion of current process and future capabilities

---

### 2.4. What is the labor quote acceptance workflow?

**Answer:**
Orion includes a **labor quote acceptance feature** that represents an improvement over COR's current Bridge process. This feature was not observed in the Bridge documentation and appears to be a new capability that will be introduced.

The labor quote acceptance workflow in Orion:
1. Multiple external quotes are received from subcontractors
2. User decides which labor quote to accept for a specific quote record in NetSuite
3. User links the selected labor quote to the NetSuite quote record
4. A popup appears allowing the user to determine what information from the labor quote will pass to the quote
5. User can consolidate, summarize, or itemize the labor quote lines (all lines itemized for internal visibility may not need to be shown to customer)

This workflow provides flexibility in how detailed cost information is presented to customers while maintaining full visibility internally.

**User Stories:**
- As a Quoting Team Member, I need to accept a specific labor quote from multiple vendor responses so that I can incorporate the selected vendor's pricing into my customer quote.
- As a Sales Manager, I need to control which labor cost details appear on the customer quote so that I can show appropriate detail without overwhelming the customer or revealing cost structures.

**BRD Requirements:**
- [REQUIREMENT] Implement labor quote acceptance workflow with line selection capability (ID: REQ-008, Type: Functional)
- [FUNCTIONALITY] Labor quote acceptance popup, Line consolidation/summarization options, Link labor quote to NetSuite quote
- [SOLUTIONDESIGN] This is standard Orion functionality that will be enabled
- [PRIORITY] Should-Have (process improvement over current state)

**Stakeholder Impact:**
- **Primary Users**: Quoting Team, Sales Team
- **Secondary Users**: Operations Manager (oversight)

**Evidence:**
- "Yeah, but there's another step that we have that I don't think they have and that's the labor quote acceptance. So there's all these quotes that come back, especially if you're going external. And then at some point you have to say, okay, for this quote, I'm going to accept for this, sorry, this quote record in netsuite." - Marcus Dallacqua
- "So they have the ability there to consolidate that or summarize that or itemize it because some might need itemized. That step is called labor quote acceptance. And I don't think they have that." - Marcus Dallacqua
- "Yeah, so there's no like. So that step of bringing over the quoted information to the actual proposal or netsuite quote, they don't look like they have that. So that. That would be an improvement to their processes." - Marcus Dallacqua

**Confidence Rating**: 93% - Feature is standard Orion functionality; COR's current process needs to be confirmed in discovery

---

### 2.5. What is the pending quote tracking requirement?

**Answer:**
COR currently has a **pending quote dashboard** in Bridge that shows all labor quote requests that have been sent to subcontractors for bid. This dashboard allows the quoting team to:
- View all RFQs sent to external vendors
- Monitor status of each pending quote
- Track which vendors have responded and which are outstanding

The implementation team needs to confirm whether Orion's labor quote functionality includes a similar dashboard or report showing:
- All labor quotes sent to vendors
- Status of each quote (pending, received, accepted, rejected)
- Vendor response tracking

If this functionality doesn't exist in the current labor quote module, a saved search or custom dashboard may need to be created.

**User Stories:**
- As a Quoting Team Member, I need to see all pending quotes I've sent to subcontractors so that I can follow up on late responses and manage my open requests.
- As an Operations Manager, I need visibility into all outstanding external labor quotes so that I can identify bottlenecks and ensure timely project progression.

**BRD Requirements:**
- [REQUIREMENT] Provide pending quote dashboard or report showing RFQs sent to subcontractors with status tracking (ID: REQ-013, Type: Functional)
- [FUNCTIONALITY] Dashboard or saved search showing labor quote status by vendor
- [ASSUMPTION] Functionality may exist in current Orion labor quote module but needs confirmation
- [PRIORITY] Should-Have

**Stakeholder Impact:**
- **Primary Users**: Quoting Team
- **Secondary Users**: Operations Manager

**Evidence:**
- "So then there's a little dashboard pending quote pending from sub so they could see everything they sent out for bid." - Marcus Dallacqua
- "So that's something Luke or Chris. We need to figure out if we have that on the labor quote. I think that there might be a section on the labor quote that shows everybody that they sent it to and the status. We'll need to double check that because if we don't have that, we might just have to create a safe search." - Marcus Dallacqua

**Confidence Rating**: 90% - Current Bridge functionality clearly described; Orion capability needs confirmation

---

## 3. PROJECT REQUEST FORM

### 3.1. How does the project request form work?

**Answer:**
The project request form is the **initiating document** for COR's pre-quote processes. Key characteristics:

**Form Structure:**
- Completed by Sales Account Manager when opportunity requires additional resources
- Contains checkboxes to indicate needs:
  - "Is estimating needed?" ☐
  - "Is design needed?" ☐
  - "Is PM needed?" ☐
- Includes project scope details
- Supports document attachments (CAP/SIF files, project plans, specifications)

**Workflow:**
- Form submission flows to shared email inbox
- Notifications sent to appropriate managers (Estimating Manager, Design Manager, PM Manager)
- Assigned to appropriate resource for review
- Estimator/Designer/PM can request more information if needed (send back workflow)

**COR vs. Orion Difference:**
In Bridge, COR initiates these requests from the Project record. In Orion, requests will be launched from the **Opportunity or Quote record** (not the Project record), representing a process adaptation for COR.

**User Stories:**
- As a Sales Account Manager, I need to complete a project request form with checkboxes for different service types so that the appropriate teams are notified and can begin their work.
- As an Estimating Manager, I need to receive notifications when estimating is requested so that I can assign the work to an estimator promptly.

**Current State Process:**
**PROCESS**: Project Request Submission  
**TRIGGER**: Sales identifies need for estimating, design, or PM services during opportunity development  
**STEPS**:
1. Sales Account Manager completes project request form → Checks appropriate boxes (estimating, design, PM)
2. Form submitted → Flows to shared email inbox → Triggers notifications
3. Notifications sent to relevant managers → Manager reviews request
4. Manager assigns to resource (estimator, designer, PM) → Resource reviews information
5. If information incomplete → Resource sends request back for more information
6. If information sufficient → Resource proceeds with their respective process

**SYSTEMS INVOLVED**: Bridge (form submission and routing), Email (notifications)

**BRD Requirements:**
- [REQUIREMENT] Configure project request form with checkboxes for Estimating needed, Design needed, PM needed (ID: REQ-014, Type: Functional)
- [REQUIREMENT] Launch labor quote/estimating/design/PM requests from Opportunity or Quote records (not Project record) (ID: REQ-010, Type: Functional - Process Change)
- [REQUIREMENT] Support document attachments including CAP/SIF files and project documentation (ID: REQ-015, Type: Functional)
- [REQUIREMENT] Enable request rejection/send back workflow for incomplete information (ID: REQ-009, Type: Functional)
- [FUNCTIONALITY] Request engine customization, Notification workflow, Document management
- [PRIORITY] Must-Have

**Stakeholder Impact:**
- **Primary Users**: Sales Account Managers (initiators), Estimating Manager, Design Manager, PM Manager
- **Secondary Users**: Estimators, Designers, PMs (assignees)

**Evidence:**
- "Request flows to a shared email inbox. So they're using complete project request form. So using that project request form to kick this off, which. That'll map to our project record that's automatically being created." - Marcus Dallacqua
- "So this kind of follows the same path. Enbridge. They start with the project request and then if estimating is needed, they mark it. Oh, it's interesting here on this project request, do you need estimated. Is the estimated needed. Design needed, PM needed?" - Marcus Dallacqua
- "They initiate these estimating or requests for estimates from the project record in Orion. They'll do it from the opportunity record or the quote record, not necessarily the project record... That'll be a shift in their process, something that they'll have to adapt to." - Marcus Dallacqua

**Confidence Rating**: 94% - Clear description with process adaptation identified; design and PM request details need deeper documentation

---

### 3.2. What project scope information is captured?

**Answer:**
Project scope details are currently captured on COR's project request form in Bridge. However, in Orion, this information should be captured on the **labor quote form** rather than the project record itself.

This represents a **process adaptation** for COR, as Orion treats the project record primarily as a reporting and aggregation tool rather than an operational form where detailed scope is entered.

Scope details typically include:
- Project location and site information
- Type of work required
- Timeline and scheduling requirements
- Special requirements (union labor, after-hours work, etc.)
- Related documents and specifications

**User Stories:**
- As a Quoting Team Member, I need to capture detailed project scope on the labor quote form so that vendors have complete information to provide accurate bids.
- As a Sales Manager, I need project scope information connected to my quote record so that I can reference it throughout the sales process.

**BRD Requirements:**
- [REQUIREMENT] Capture project scope details on labor quote form (not project record) (ID: REQ-011, Type: Functional - Process Change)
- [FUNCTIONALITY] Labor quote form field configuration
- [PRIORITY] Must-Have
- **Process Adaptation Note**: This is a change from COR's current Bridge process and will require training and change management

**Stakeholder Impact:**
- **Primary Users**: Quoting Team, Sales Team
- **Impacted Parties**: All users familiar with current Bridge project record workflow

**Evidence:**
- "Project scope. So this is interesting. Okay, so like they're filling out the project scope details and we would typically do this elsewhere, but they're okay, so they're doing it. Yeah, we would do this on the. On the labor quote form, not on the project form." - Marcus Dallacqua

**Confidence Rating**: 92% - Clear direction on where to capture information; specific scope fields need to be defined in discovery

---

## 4. VENDOR AND DOCUMENT MANAGEMENT

### 4.1. How is the CAM reservation system integrated?

**Answer:**
COR uses CAM (Customer Asset Management) software to manage warehouse reservations. The integration is **manual** - there is no system-to-system integration.

Current process:
1. User creates reservation record in CAM system
2. CAM generates a reservation number for that record
3. User manually copies the CAM reservation number
4. User pastes the reservation number into the appropriate field in Bridge

**Orion Implementation:**
The same manual approach will be used in Orion. A field will be provided on the appropriate form (likely labor quote or project record) where users can enter the CAM reservation number manually. No API integration or automated data exchange is required.

**User Stories:**
- As a Warehouse Coordinator, I need to enter the CAM reservation number so that warehouse staff can reference the correct reservation for storage requirements.
- As an Operations Team Member, I need to see the CAM reservation number on the labor quote so that I can coordinate with warehouse staff.

**BRD Requirements:**
- [REQUIREMENT] Provide field for CAM reservation number (manual entry, no system integration) (ID: REQ-006, Type: Functional)
- [FUNCTIONALITY] Custom field on appropriate record (labor quote or project)
- [PRIORITY] Should-Have

**Stakeholder Impact:**
- **Primary Users**: Warehouse Coordinators, Quoting Team
- **Secondary Users**: Operations Team

**Evidence:**
- "What about the CAM reservation number? Where does that come from?" - Gary Strickland
- "So they're using cam. CAM is that piece of software, Customer asset management software that they're using. And so they're going to set it up in cam and then CAM has a number for that record and that's the reservation number and they're just linking it here." - Marcus Dallacqua
- "No, there's actually no integration. What they're doing here, they're just. They're doing it one system and copying the number over into their current system through Bridge. And we would have them do the same thing. We'll just have a field for a reservation number." - Marcus Dallacqua

**Confidence Rating**: 97% - Explicit confirmation of manual approach with clear implementation direction

---

### 4.2. How are CAP/SIF files and documents handled?

**Answer:**
COR uses CAP software to generate project specifications, which can be exported as:
- **SIF file** - Text file with specialized formatting (appears as "wall of text" in PDF)
- **PDF** - Printable table format showing specification details

**Current approach:** Documents are attached to labor quote requests and RFQs. The implementation team noted that SharePoint integration will be particularly helpful for COR's document management.

**Outstanding Question:** The team needs to clarify in discovery whether COR:
1. Exports CAP specifications as PDF and attaches to requests, OR
2. Exports SIF files and expects them to be imported into another system, OR
3. Uses a different approach

The consensus during the walkthrough was that COR likely exports CAP as PDF (which shows a table format) rather than raw SIF files.

**User Stories:**
- As a Quoting Team Member, I need to attach specification documents to labor quote requests so that vendors have complete information to bid accurately.
- As a Subcontractor, I need to access project specifications and documents so that I can provide accurate pricing.

**BRD Requirements:**
- [REQUIREMENT] Support CAP/SIF file attachments and project documentation (ID: REQ-015, Type: Functional)
- [FUNCTIONALITY] Document attachment capability, SharePoint integration for document management
- [ASSUMPTION] Documents are attached as PDFs rather than imported as SIF data
- [PRIORITY] Must-Have
- **Outstanding Item**: Confirm exact CAP/SIF export and attachment process in discovery

**Stakeholder Impact:**
- **Primary Users**: Quoting Team
- **Secondary Users**: Estimators, Subcontractors (external)

**Evidence:**
- "So what I'm curious about is are they using CAP to generate a PDF of the specifications, which is all the transaction lines. They're all the lines. So that's something we need to think we need to call out for discovery is what requirement they have at this point." - Marcus Dallacqua
- "Unless they're printing out the table. Unless it prints out the table, it won't be like in cap they see a table like our smart table. So if they choose PDF, it might just print that table where CIF is that text file. That's all arranged weird. So. Yeah, we'll figure that out." - Marcus Dallacqua
- "Good. They're just. Yeah, they're just attaching documents, which is fine. That's where that SharePoint integration is gonna be really helpful for them." - Marcus Dallacqua

**Confidence Rating**: 85% - General approach understood but specific format and process needs discovery confirmation

---

### 4.3. What RFQ form and branding requirements exist?

**Answer:**
COR currently has a Request for Quote (RFQ) form generated from Bridge that is sent to external subcontractors. Key observations:

- Form includes COR logo
- Minimal branding beyond logo
- May print in COR colors (though document was reviewed in grayscale)
- Form structure and content serve functional purpose
- Implementation team will ask during discovery if COR wants to upgrade or enhance the form design

Orion can generate RFQ forms with customizable branding and formatting.

**User Stories:**
- As a Quoting Team Member, I need to generate professional RFQ forms with our company branding so that subcontractors receive consistent, branded communications.
- As a Marketing Manager, I need RFQ forms to reflect our brand identity so that all external communications maintain brand consistency.

**BRD Requirements:**
- [REQUIREMENT] Provide request for quote form with COR branding and logo (ID: REQ-016, Type: Functional)
- [FUNCTIONALITY] Customizable RFQ form template
- [PRIORITY] Should-Have
- **Discovery Item**: Confirm if COR wants to maintain current form design or upgrade during discovery

**Stakeholder Impact:**
- **Primary Users**: Quoting Team
- **Secondary Users**: Marketing (branding oversight), Subcontractors (recipients)

**Evidence:**
- "Okay, good. They're just. Yeah, they're just attaching documents, which is fine. That's where that SharePoint integration is gonna be really helpful for them. Okay. We have a nice request for quote. So this is their form, I guess, you know, for their request for quote during discovery. We'll ask them if they want to upgrade this." - Marcus Dallacqua
- "There's no. There's not much branding on it, but that's fine. You know, that's how they want it... I mean this is actually their logo. It may print in their colors, but that's actually their logo that they have on their website." - Gary Strickland

**Confidence Rating**: 91% - Current form described; enhancement decisions deferred to discovery

---

## 5. ESTIMATING PROCESS

### 5.1. How does the estimating process work?

**Answer:**
The estimating process for interior construction follows this workflow:

**Trigger:** Sales Account Manager submits project request with "Estimating needed" checkbox selected

**Process Flow:**
1. Notification sent to Estimating Manager
2. Estimating Manager reviews request
3. Estimating Manager assigns request to specific Estimator for review
4. Estimator reviews project request to determine if sufficient information provided
5. If information insufficient → Estimator sends request back to originator for more information
6. If information sufficient → Estimator proceeds with estimate

**Key Components:**
- Project request form serves as initiating document
- Estimator assignment based on location and workload
- Site conditions/job site analysis record provides location-specific information
- Document attachments (specifications, plans) support estimating work

**Missing Documentation:** The transcript notes that detailed estimating workflow documentation was not included in the pre-quote materials reviewed. This falls under operations/order management scope.

**User Stories:**
- As an Estimating Manager, I need to receive project request notifications so that I can assign estimating work to the appropriate estimator based on location and workload.
- As an Estimator, I need complete project information including site conditions and specifications so that I can provide accurate estimates.

**BRD Requirements:**
- [REQUIREMENT] Configure project request form with "Estimating needed" checkbox triggering notification workflow (ID: REQ-014, Type: Functional)
- [REQUIREMENT] Enable request rejection/send back workflow for incomplete estimating requests (ID: REQ-009, Type: Functional)
- [REQUIREMENT] Use job site analysis/site conditions record for site-specific information (ID: REQ-012, Type: Functional)
- [FUNCTIONALITY] Request routing, Notification engine, Site conditions record
- [PRIORITY] Must-Have

**Stakeholder Impact:**
- **Primary Users**: Estimating Manager, Estimators
- **Secondary Users**: Sales Account Managers (request originators)

**Evidence:**
- "Yeah, sorry. Project request review Interior Construction Estimating. Okay. Yeah, this is. This falls under their operations order management. So this falls under operations, which makes sense to me." - Marcus Dallacqua
- "Sales Account Manager submits notifications. Go to. Oh, so the project request, which was an email, I think notifications go to estimating manager. Design Manager wants to sign another email sent to estimator for review." - Marcus Dallacqua
- "So this kind of follows the same path. Enbridge. They start with the project request and then if estimating is needed, they mark it." - Marcus Dallacqua

**Confidence Rating**: 88% - High-level process understood; detailed estimating workflow needs additional documentation and discovery

---

### 5.2. What is the job site analysis / site conditions record?

**Answer:**
Orion includes a **job site analysis** (also called **site conditions**) record that is attached to the address record in NetSuite. This is a standard Orion feature that aligns with COR's current process.

**Key Characteristics:**
- Attached to address record (NetSuite address book)
- Stores site-specific information needed for estimating and operations
- Can be referenced from multiple transactions related to that address
- Supports detailed site condition documentation
- Original naming: "Job Site Analysis" (industry standard: "Site Conditions")

**Terminology Note:** The team discussed whether it's called "site conditions" or "job site analysis" in Orion, concluding that it was originally called "job site analysis" because it provides deeper functionality than typical site condition records.

**User Stories:**
- As an Estimator, I need to access site condition information for the project location so that I can account for site-specific factors in my estimate.
- As a PM, I need to reference job site analysis details so that I can plan resource allocation and identify potential site challenges.

**BRD Requirements:**
- [REQUIREMENT] Use job site analysis/site conditions record attached to address for site-specific information (ID: REQ-012, Type: Functional)
- [FUNCTIONALITY] Site conditions custom record linked to address
- [PRIORITY] Must-Have (standard Orion feature)

**Stakeholder Impact:**
- **Primary Users**: Estimators, PMs, Operations Team
- **Secondary Users**: Field Service team, Installers

**Evidence:**
- "Okay, so here's another thing. The site conditions. So they review the site conditions. So they do have a record for site conditions like we do. Just so you know, Gary, our site conditions record is attached to the address." - Marcus Dallacqua
- "We have all of this on the site conditions record. Or I think. Is it called site conditions or job site analysis? I don't remember, Chris." - Marcus Dallacqua
- "Originally it was called job site analysis... Well, I think the industry term is site conditions, and we change it to job site analysis because it's deeper than what most people are doing." - Chris Trumble

**Confidence Rating**: 95% - Standard Orion functionality confirmed; aligns with COR process

---

## 6. LONG TERM STORAGE (LTS)

### 6.1. How does the Long Term Storage quote process work?

**Answer:**
Long Term Storage (LTS) represents a specific labor quote request type for warehouse storage services. The process was briefly covered in the transcript:

**Key Points:**
- LTS is one of the four labor quote request types
- Requires getting quote from warehouse for storage services
- Warehouse calculates storage requirements (cubic footage or similar metrics)
- Provides monthly storage rate quote
- Quote calculation performed by warehouse team

**Connection to Other Processes:** The transcript notes that LTS was covered more extensively in the order management sessions, as it relates to ongoing warehouse billing and management.

**User Stories:**
- As a Sales Team Member, I need to request a long-term storage quote from the warehouse so that I can include storage costs in my customer proposal.
- As a Warehouse Manager, I need to calculate cubic footage and storage requirements so that I can provide accurate monthly storage rate quotes.

**BRD Requirements:**
- [REQUIREMENT] Create LTS-specific labor quote request type for warehouse storage quotes (ID: REQ-001, Type: Functional)
- [FUNCTIONALITY] Request engine supporting LTS request type with warehouse-specific fields
- [PRIORITY] Must-Have
- **Outstanding Item**: Deep dive on LTS calculation methodology, rate structures, and monthly billing workflow (covered in order management sessions)

**Stakeholder Impact:**
- **Primary Users**: Quoting Team, Warehouse Team
- **Secondary Users**: Sales Team, Finance (billing)

**Evidence:**
- "Oh, LTS is long term storage." - Chris Trumble
- "Long term storage quote process, which we've already covered in quoting, but I guess. Or in order management, but I guess it also falls in here too, because you're going to get a quote from the warehouse. The warehouse, yeah. Or your labor. Your external labor or the warehouse sales rate." - Marcus Dallacqua
- "Yeah. This one says they get a monthly surge quote from the warehouse in the calculation table. In the quote calculation process, they got to figure out thus the cubic footage or whatever it's going to take up and base it on that. And the warehouse calculates that." - Chris Trumble

**Confidence Rating**: 85% - Basic process understood; detailed requirements covered in order management sessions

---

## 7. PROCESS ADAPTATIONS AND CHANGE MANAGEMENT

### 7.1. What are the key process adaptations required for Orion?

**Answer:**
The implementation team identified several areas where COR will need to **adapt** their current processes to align with how Orion operates:

**ADAPT #1: Request Initiation Point**
- **Current (Bridge)**: Labor quote and estimating requests are initiated from the Project record
- **Future (Orion)**: Requests will be launched from the Opportunity or Quote record
- **Rationale**: Orion treats the Project record as a reporting and aggregation tool, not an operational record
- **Impact**: Medium - Training required; represents philosophical shift in how project records are used

**ADAPT #2: Project Scope Capture Location**
- **Current (Bridge)**: Project scope details captured on Project record
- **Future (Orion)**: Project scope captured on Labor Quote form
- **Rationale**: Orion captures operational details on transaction records, not project record
- **Impact**: Medium - Users must adjust where they enter information

**ADAPT #3: Manual Calculation Entry (maintained)**
- **Current (Bridge)**: Manual calculations performed outside system
- **Future (Orion)**: Same approach initially; rate table functionality not available yet
- **Rationale**: Rate table calculations are desired future functionality but not currently in Orion
- **Impact**: Low - No process change, but represents future enhancement opportunity

**User Stories:**
- As a Sales Manager transitioning to Orion, I need training on launching requests from Opportunity records so that I can adapt to the new workflow efficiently.
- As a Quoting Team Member, I need to understand where to capture scope information so that I enter data in the correct forms.

**BRD Requirements:**
- [REQUIREMENT] Launch requests from Opportunity/Quote records (not Project) (ID: REQ-010, Type: Process Change - ADAPT)
- [REQUIREMENT] Capture scope on Labor Quote form (not Project record) (ID: REQ-011, Type: Process Change - ADAPT)
- [CONSTRAINT] Rate table functionality not available in current Orion version
- [PRIORITY] Must-Have (process training and change management)
- [RISK] User resistance to changing familiar workflows; potential for errors during transition period

**Stakeholder Impact:**
- **Primary Users**: All COR users familiar with Bridge workflow (Sales, Quoting, Operations)
- **Training Need**: Moderate - Targeted training on new workflow initiation points
- **Change Management**: Required - Clear communication about why these changes improve overall process

**Evidence:**
- "They initiate these estimating or requests for estimates from the project record in Orion. They'll do it from the opportunity record or the quote record, not necessarily the project record. So again, the way that we treat the project record is it's almost a reporting tool and an aggregation tool." - Marcus Dallacqua
- "That's something to make sure that we emphasize during discovery. That'll be a shift in their process, something that they'll have to adapt to. Now that's a good example of align, adapt or accommodate. It definitely doesn't align. They will need to adapt." - Marcus Dallacqua
- "We could build an accommodation for them to do that, but I don't... I would push back on it. I don't see a reason why to accommodate that." - Marcus Dallacqua

**Confidence Rating**: 96% - Clear identification of process changes with explicit rationale and impact assessment

---

### 7.2. What form development is required?

**Answer:**
Form development is a **critical requirement** for the Pre-Quote implementation, as identified by the implementation team during the transcript review.

**Required Forms:**
1. **Labor Quote Request Forms** (4 types):
   - Internal labor quote request
   - External labor quote request
   - Intermarket labor quote request
   - LTS (Long Term Storage) labor quote request

2. **Project Request Form**:
   - Checkboxes for service types (Estimating, Design, PM)
   - Project scope fields
   - Document attachment capability

3. **RFQ (Request for Quote) Form**:
   - Vendor-facing document
   - COR branding and logo
   - Professional formatting

**Form Requirements:**
- Custom fields appropriate to each request type
- Institutional knowledge capture (notes fields for calculation formulas)
- CAM reservation number field
- Union labor requirements field
- Location selection
- Document attachment areas
- Site condition reference

**User Stories:**
- As an Implementation Team Member, I need to develop custom forms for each labor quote type so that COR users have the appropriate fields and workflows for each scenario.
- As a Quoting Team Member, I need forms that capture all necessary information so that I can process requests efficiently without missing critical details.

**BRD Requirements:**
- [REQUIREMENT] Develop custom labor quote request forms for all four request types (ID: REQ-001, Type: Functional)
- [REQUIREMENT] Configure project request form with required checkboxes and fields (ID: REQ-014, Type: Functional)
- [REQUIREMENT] Design RFQ form with COR branding (ID: REQ-016, Type: Functional)
- [SOLUTIONDESIGN] Required - Custom form development is significant effort
- [FUNCTIONALITY] Request engine form configuration
- [PRIORITY] Must-Have
- **Critical Path**: Form development must occur early in configuration phase to allow user testing

**Stakeholder Impact:**
- **Primary Users**: All Pre-Quote users (will interact with forms daily)
- **Development Team**: Significant configuration and development effort required

**Evidence:**
- "So form development is going to be important." - Chris Trumble
- "Yeah, for sure." - Marcus Dallacqua (in response)
- "Yeah, it's two different request types. So you would create a request type specific for labor quote internal, another one for labor quote external, another one for labor quote internal, intermarket, something like that. Yep. But they're all pretty easy to make." - Marcus Dallacqua

**Confidence Rating**: 94% - Clear requirement identified; specific field requirements will be detailed during configuration

---

## 8. MISSING DOCUMENTATION AND OUTSTANDING ITEMS

### 8.1. What documentation is missing from the Pre-Quote materials?

**Answer:**
The implementation team identified two significant gaps in the Pre-Quote documentation provided:

**1. Design Request Process**
- Project request form includes "Design needed" checkbox
- No documentation provided for the design request workflow
- Design Manager (Rafina) mentioned in Operations transcript
- Likely falls under "COR Studio" organization
- Process details needed: Triggers, form fields, assignment workflow, deliverables

**2. PM Request Process**
- Project request form includes "PM needed" checkbox
- No documentation provided for the PM request workflow
- PM Manager (Wendy) extensively involved in Operations discussions
- Process details needed: Triggers, form fields, assignment workflow, handoff procedures

Both of these processes should be documented as part of the Pre-Quote scope, as they are initiated by the same project request form mechanism as labor quote and estimating requests.

**User Stories:**
- As an Implementation Team Member, I need complete documentation for all request types so that I can configure comprehensive workflows in Orion.
- As a Design Manager, I need my team's request process documented so that our workflow is properly configured in the new system.

**BRD Requirements:**
- [CONSTRAINT] Design request documentation missing from current scope
- [CONSTRAINT] PM request documentation missing from current scope
- [RISK] Incomplete requirements may result in gaps in configured functionality
- [PRIORITY] Must-Have - Documentation needed before configuration can be completed
- **Action Required**: Obtain documentation or schedule discovery sessions for Design and PM request processes

**Stakeholder Impact:**
- **Primary Users**: Design team, PM team (workflows not yet documented)
- **Implementation Team**: Cannot complete configuration without these requirements

**Evidence:**
- "So this kind of follows the same path. Enbridge. They start with the project request and then if estimating is needed, they mark it. Oh, it's interesting here on this project request, do you need estimated. Is the estimated needed. Design needed, PM needed?" - Marcus Dallacqua
- "So one thing we need to look for, and we don't have it in this bucket right now of pre quote, but there should be documentation for design and PM requests. So that should be in this pre quote section as well. Chris, do you have access to SharePoint?" - Marcus Dallacqua
- "There's nothing on design. Let me look for pm... Yeah, design might be under that whole COR studio." - Chris Trumble

**Confidence Rating**: 97% - Explicit identification of missing documentation with clear action items

---

### 8.2. What confirmations are needed from the implementation team?

**Answer:**
The transcript identified several technical questions that need confirmation from the Orion implementation team (Joe and team):

**Confirmation #1: Union Status Tracking**
- **Question**: Does NetSuite/Orion currently track union status on vendor records?
- **Action**: If not, create custom field for union/non-union classification
- **Related**: REQ-003

**Confirmation #2: Vendor Location Field**
- **Question**: Should location field on vendor record be multi-select to support vendors serving multiple COR locations?
- **Action**: Determine best approach for parent-child vendor relationships vs. multi-select field
- **Related**: REQ-004, REQ-005

**Confirmation #3: Pending Quote Dashboard**
- **Question**: Does labor quote module show all vendors who were sent RFQs and their response status?
- **Action**: If not, create saved search for pending quote tracking
- **Related**: REQ-013

**Confirmation #4: Request Rejection Workflow**
- **Question**: Does request engine support "send back for more information" workflow?
- **Action**: Confirm capability; may use mandatory fields vs. rejection workflow
- **Related**: REQ-009

**User Stories:**
- As a Technical Lead, I need to confirm existing Orion capabilities so that we accurately scope custom development vs. configuration work.

**Action Items:**
- Marcus/Chris to query Joe on vendor record fields and capabilities
- Luke/Chris to confirm labor quote dashboard functionality
- Joe to confirm request engine rejection workflow
- Define dropdown values with COR team during discovery

**Evidence:**
- "So that's a, that's something that we need to find out. Maybe not discovery but just a takeaway for us to do. We do we track vendors and if they're union or not on our vendor record." - Marcus Dallacqua
- "Yeah, we might need to make that location field a multi select. Yeah, that could be. They could be Used across multi. Multi locations." - Marcus Dallacqua
- "So that's something Luke or Chris. We need to figure out if we have that on the labor quote." - Marcus Dallacqua
- "Chris, will you just make a note for Joe to make sure that I think we have a process for that on the labor quote request." - Marcus Dallacqua

**Confidence Rating**: 96% - Clear list of technical confirmations needed with specific assignees identified

---

## Outstanding Items Summary

### Critical Gaps (Must Be Addressed Before Configuration)
1. **Design Request Process Documentation** - No documentation provided; needed for complete Pre-Quote configuration
2. **PM Request Process Documentation** - No documentation provided; needed for complete Pre-Quote configuration
3. **Union/Non-Union/Intermarket Dropdown Values** - Specific values need to be defined with COR team
4. **CAP/SIF File Handling Process** - Clarify whether PDF export or SIF import/integration required

### Technical Confirmations Needed (Before Configuration)
1. **Vendor Record - Union Status Field** - Confirm if exists; if not, add custom field
2. **Vendor Record - Location Field** - Determine single-select vs. multi-select approach
3. **Labor Quote - Pending Dashboard** - Confirm existing functionality or create saved search
4. **Request Engine - Rejection Workflow** - Confirm send-back capability

### Discovery Sessions Needed
1. **Design Request Process** - High priority, missing documentation
2. **PM Request Process** - High priority, missing documentation
3. **Vendor Management** - Medium priority, define classifications and selection criteria
4. **Long Term Storage Details** - Medium priority, covered in order management sessions

### Form Development Required (Critical Path)
1. Internal Labor Quote Request Form
2. External Labor Quote Request Form
3. Intermarket Labor Quote Request Form
4. LTS Labor Quote Request Form
5. Project Request Form (with checkboxes)
6. RFQ Form (vendor-facing, branded)

### Change Management Focus Areas
1. **Request Initiation Location** - Train users to launch from Opportunity/Quote instead of Project
2. **Scope Capture Location** - Train users to enter scope on Labor Quote form instead of Project record
3. **Labor Quote Acceptance Workflow** - New feature not in Bridge; train on benefits and usage

### Future Enhancement Opportunities
1. **Rate Table Calculations** - Not available in current Orion but desired by many dealers
2. **Institutional Knowledge Capture** - Formulas and calculation logic documentation and potential automation

---

## Confidence Summary

**Overall Questionnaire Confidence**: 92%

**High Confidence Areas (95%+)**:
- Current system identification (Bridge)
- Labor quote request types
- Union requirements
- Request engine replacement approach
- CAM reservation (manual entry)
- Site conditions/job site analysis record
- Process adaptations required

**Good Confidence Areas (90-94%)**:
- Vendor selection and filtering
- Labor quote acceptance workflow (Orion feature)
- Project request form structure
- RFQ form requirements
- Estimating process (high-level)
- Missing documentation identification

**Moderate Confidence Areas (85-89%)**:
- CAP/SIF file handling specifics
- LTS detailed process (covered elsewhere)
- Pending quote dashboard (needs confirmation)

**Areas Requiring Discovery**:
- Design request complete workflow
- PM request complete workflow
- Vendor classification dropdown values
- Institutional knowledge formulas
- Rate table requirements (future)

---

## Requirements Summary by Implementation Approach

### ALIGNS (Standard Orion Functionality - 8 Requirements)
- REQ-001: Multiple labor quote request types
- REQ-002: Request engine replacing Bridge
- REQ-006: CAM reservation number field
- REQ-012: Job site analysis/site conditions record
- REQ-014: Project request form with checkboxes
- REQ-015: Document attachment support
- REQ-016: RFQ form with branding

### ADAPT (Process Changes Required - 3 Requirements)
- REQ-007: Manual calculation entry with notes
- REQ-010: Launch requests from Opportunity/Quote (not Project)
- REQ-011: Capture scope on Labor Quote form (not Project)

### ACCOMMODATE (Customization Required - 7 Requirements)
- REQ-003: Union status tracking on vendor records
- REQ-004: Vendor location custom field
- REQ-005: Parent-child vendor relationships
- REQ-008: Labor quote acceptance workflow
- REQ-009: Request rejection/send back workflow
- REQ-013: Pending quote dashboard
- REQ-017: Vendor filtering (union, location, intermarket)

**Total Requirements Identified**: 17 (with more to be added from Design and PM request documentation)

---

**Document Prepared**: October 16, 2025  
**Prepared By**: AI Analysis following Discovery Questionnaire Analysis Prompt  
**Next Steps**: 
1. Schedule Design Request and PM Request discovery sessions
2. Confirm technical capabilities with Joe/implementation team
3. Gather vendor classification values from COR
4. Begin form development planning






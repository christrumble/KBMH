# Questionnaire - CRM
**Version**: 2.0  
**Date**: October 15, 2025  
**Process Area**: CRM (Customer Relationship Management)

## Change Log
- **Date**: October 15, 2025
- **Version**: 2.0  
- **Sources**: Master_Transcript_CRM.md, Master_Transcript_Marketing_CRM.md
- **Summary**: Comprehensive questionnaire analysis completed from both CRM master transcripts covering all requirements, decisions, processes, and pain points.

- **Date**: 2025-10-02
- **Version**: 1.0
- **Sources**: Marketing/2 Input/Transcript MRK&CRM
- **Summary**: Initial scaffold for CRM questionnaire.

## PROCESSED FILES
- CRM/2 Input/Master_Transcript_CRM.md (1,258 lines)
- CRM/2 Input/Master_Transcript_Marketing_CRM.md (1,056 lines)

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

### Core CRM Requirements
- **REQ-001**: Migrate from Zendesk to NetSuite CRM with Opportunity → Quote → Sales Order → Project integration (ALIGNS) - "Opportunity → Quote → Sales Order, all stages visible and linked, project number/name consistent across all transactions" - Marcus
- **REQ-002**: Make opportunity entry required (currently optional) to ensure pipeline visibility and data quality (ADAPT) - "Not required - many don't" [current state]; "The data entry part of it has never been clean enough to trust in" - Team
- **REQ-003**: Implement validation rules and required fields on opportunities to prevent incomplete data entry (ACCOMMODATE) - "Some people are actually working, and you have other people that are just licking everything and calling it theirs" - Kimmy
- **REQ-004**: Use Kanban Boards for visual opportunity pipeline management (ALIGNS) - "I think it'd be a good tool for us to try and test out" - Matt
- **REQ-005**: Restrict opportunity visibility to assigned users only (ADAPT) - "Restricted their opportunities to only the ones that they're on. It does that natively" - Team

### Lead Management
- **REQ-006**: Web form integration to automatically create leads in NetSuite (ALIGNS) - "Contact form submission → Lead created automatically in NetSuite"
- **REQ-007**: Implement lead routing rules to assign to Jenny (Admin) for qualification then route to appropriate GM/Account Manager (ALIGNS) - Current process documented with Jenny qualifying leads
- **REQ-008**: Enable mobile Quick Add Lead functionality for BD reps (ALIGNS) - "NetSuite mobile app… a really good one is Quick Add Lead" - Team
- **REQ-009**: Track lead sources (web form, referral, relationship, RFP, event) for conversion analysis (ALIGNS) - Multiple lead source types identified in transcripts

### Contact & Account Management
- **REQ-010**: Implement custom contact role classifications beyond Core limitations (ACCOMMODATE) - "Are they the main contact? Are they finance? Is it procurement? We don't know" - Team on Core limitations
- **REQ-011**: Support multiple contact roles per contact (broker, A&D firm, decision maker, finance, procurement, facilities, PM, influencer) (ALIGNS) - Detailed role types identified in transcripts
- **REQ-012**: Implement market sector/vertical tracking (Healthcare, Tech, Corporate, Government, Education, Legal, Creative, Hospitality) (ALIGNS) - "Healthcare trending up - opportunity to focus" - Team
- **REQ-013**: Implement territory assignment (SF - Jill, San Jose - Kate, Sacramento - Alex) (ALIGNS) - Territory structure documented
- **REQ-014**: Enable duplicate detection and merge capabilities (ALIGNS) - "No duplicate detection" in Core; NetSuite has "AI-enhanced duplicate identification"
- **REQ-015**: Track contact communication preferences and opt-in/opt-out status automatically (ALIGNS) - Requirement for email marketing compliance

### Forecasting & Pipeline Management
- **REQ-016**: Configure opportunity-level forecasting (not quote-level) to prevent over-forecasting (ADAPT) - "Someone's gonna have to manage which quote amount should go back to the opportunity" - Team
- **REQ-017**: Set forecast inclusion threshold at 70%+ probability (ADAPT) - "We don't forecast anything below 70%… whenever we say forecast, it's 70% or greater" - Team
- **REQ-018**: Track forecast accuracy by user over time (ADAPT) - "Forecast accuracy varies by user... No systematic tracking of accuracy... Can't improve without measurement"
- **REQ-019**: Define opportunity stages and probability by stage (ADAPT) - Stages listed but "To Be Finalized": Lead/Prospect, Qualification, Needs Analysis, Proposal/RFP, Negotiation, Closed Won, Closed Lost
- **REQ-020**: Create Sales Goals dashboard in NetSuite to replace Excel tracking (ACCOMMODATE) - "You want that to live in NetSuite? — Yes. Yes… a dashboard" - Matt

### Approval Workflows
- **REQ-021**: Configure order approval for amounts over $25,000 to Shannon (Project Coordinator Manager) (ALIGNS) - Current documented approval rule
- **REQ-022**: Configure approval workflow when missing required documents (deposit, signed proposal, signed drawings, signed lookbook) to Matt (ALIGNS) - "If any missing → approval from Matt required"
- **REQ-023**: Configure erosion approval when cumulative erosion exceeds $1,500 to Matt (ALIGNS) - "$500 erosion + $1,000 more = $1,500 cumulative triggers approval"
- **REQ-024**: Build double-order detection query (same total dollar amount within past 30 days) with flagging for review (ACCOMMODATE) - "Biggest losses from double orders... 150 workstations ordered and owned before discovered"
- **REQ-025**: Track approval time by approver to identify bottlenecks (ALIGNS) - "Average approval time tracking per approver... Bottleneck identification" capability noted

### Win/Loss Analysis
- **REQ-026**: Implement required win/loss reason codes (ADAPT) - "Dies in there if lost... No systematic learning... No competitor intelligence"
- **REQ-027**: Track competitor information on lost opportunities (ADAPT) - "Competitor tracking" identified as future need
- **REQ-028**: Create win/loss analysis reports by sector, size, type, territory (ADAPT) - "Analysis by sector, size, type... Continuous learning"

### Vendor & Customer Management
- **REQ-029**: Add vendor credit limit field and warning threshold (90% of limit) (ACCOMMODATE) - "Mad scramble at that nth hour because our order won't go through because we hit it [credit limit]"
- **REQ-030**: Prevent PO creation when vendor credit limit exceeded (ACCOMMODATE) - "Prevent PO creation if over limit"
- **REQ-031**: Enable basic Customer Portal for quote and invoice visibility (ALIGNS) - "We do have a customer portal… see open quotes… open invoices" - Team
- **REQ-032**: Configure GP target default of 22% at customer level with opportunity override capability (ADAPT) - "We have a target GP goal… 22%"; "Field on the customer… sources through the opportunity… user can override" - Matt

### Activity & Task Management
- **REQ-033**: Enable activity tracking (calls, emails, meetings) on opportunities (ALIGNS) - "Follow-up tasks with due dates... Call logging with notes... Email tracking"
- **REQ-034**: Enable task management with due dates and reminders on opportunities (ALIGNS) - Standard CRM capability
- **REQ-035**: Maintain activity history and team collaboration notes on opportunities (ALIGNS) - "Team collaboration (notes, tasks, assignments)"

### Document Management
- **REQ-036**: Enable document attachment to opportunities/quotes (RFPs, proposals, correspondence) (ALIGNS) - "Document attachment (RFPs, proposals, correspondence)"
- **REQ-037**: Support Google Drive folder linking for project documentation (ALIGNS) - Current practice to be maintained

### Data Migration
- **REQ-038**: Import Zendesk opportunity history via CSV with historical tagging (ALIGNS) - "You can export the entire… CSV… import it and tag it" - Kip
- **REQ-039**: Migrate contact data from Core with deduplication (ALIGNS) - "Deduplication during migration" identified
- **REQ-040**: Migrate and classify contacts by role, sector, and territory during import (ACCOMMODATE) - "Contact classification/segmentation" needed

### Dashboards & Reporting
- **REQ-041**: Create BD/Sales Rep dashboard (my opportunities, pipeline value, forecast, activities, overdue tasks) (ALIGNS) - Detailed dashboard requirements documented
- **REQ-042**: Create Sales Manager dashboard with "Me and My Team" role-based filters (ADAPT) - "That's been one of the frustrations with Core... I've never gotten that [to work]" - Marcus
- **REQ-043**: Create Executive dashboard (company-wide pipeline, forecast summary, pipeline by sector/territory, win rate trends) (ALIGNS) - Executive metrics documented
- **REQ-044**: Enable drill-down capability from dashboard metrics to detail records (ALIGNS) - "Click any metric → see detail"

### Marketing Integration
- **REQ-045**: Configure email marketing capability (120,000 emails/month included) with minimal implementation (ALIGNS) - "Capacity way more than we would ever use... Less than 6 campaigns per year" - Team
- **REQ-046**: Implement automatic subscription management for opt-in/opt-out (ALIGNS) - "Subscription status automatically managed"
- **REQ-047**: Support segmented contact lists by role, sector, geography, custom criteria (ALIGNS) - "Curated lists by role... Market-specific campaigns"
- **REQ-048**: Track campaign performance (opens, clicks, ROI) when email campaigns used (ALIGNS) - Standard email marketing metrics

### Future Phase / Lower Priority
- **REQ-049**: Support sales team commission splits on opportunities (FUTURE) - "Sometimes… start out as a team… historically… even split… bigger conversation" - Team
- **REQ-050**: Event management with invitation tracking and attendance (FUTURE) - "Minimal focus during implementation, evaluate post-go-live if value emerges"

## Action Items

ACTION: Document current approval workflow rules in flowchart format  
ASSIGNED TO: Shannon (Project Coordinator Manager)  
DUE: TBD  
RELATED TO: REQ-021, REQ-022, REQ-023

ACTION: Define final list of contact roles (Primary Contact, Decision Maker, Finance, Procurement, Facilities, PM, Executive Sponsor, Influencer/Broker, A&D, CM, GC, Manufacturer Rep, Vendor Contact)  
ASSIGNED TO: Sales/BD Team (All)  
DUE: TBD  
RELATED TO: REQ-010, REQ-011

ACTION: Define lead sources for tracking (relationship, RFP, web form, referral, event, etc.)  
ASSIGNED TO: Sales/BD Team  
DUE: TBD  
RELATED TO: REQ-009

ACTION: Define sector/market classifications (finalize list: Healthcare, Tech, Corporate, Government, Education, Financial Services, Legal, Creative/Agency, Hospitality, Other)  
ASSIGNED TO: All stakeholders  
DUE: TBD  
RELATED TO: REQ-012

ACTION: Define opportunity stages and probability percentages by stage  
ASSIGNED TO: Sales Leadership, All stakeholders  
DUE: TBD  
RELATED TO: REQ-019

ACTION: Define win/loss reason codes (Price, Competitor, Timing, Requirements not met, Relationship, Other)  
ASSIGNED TO: All stakeholders  
DUE: TBD  
RELATED TO: REQ-026, REQ-027

ACTION: Identify data quality owner/champion for contact database management  
ASSIGNED TO: TBD - Suggest: Sales Operations or CRM Admin  
DUE: TBD  
RELATED TO: REQ-003, REQ-039, REQ-040

ACTION: Build double-order detection query specification  
ASSIGNED TO: Marcus/Implementation Team  
DUE: TBD  
RELATED TO: REQ-024

ACTION: Provide current Sales Goals Excel template and layout for dashboard recreation  
ASSIGNED TO: Matt/Kip  
DUE: TBD  
RELATED TO: REQ-020

ACTION: Document minimum required fields for opportunity creation  
ASSIGNED TO: Sales Leadership  
DUE: TBD  
RELATED TO: REQ-002, REQ-003

ACTION: Define activity logging standards (which activities must be logged vs. optional)  
ASSIGNED TO: Sales Leadership  
DUE: TBD  
RELATED TO: REQ-033, REQ-034

ACTION: Confirm vendor credit limits and warning thresholds  
ASSIGNED TO: Purchasing/Finance Team  
DUE: TBD  
RELATED TO: REQ-029, REQ-030

## Additional Sessions Needed

None explicitly discussed in transcripts. All necessary discovery information was captured across the CRM and Marketing CRM session transcripts. Follow-up clarification may be needed on specific configuration details (opportunity stages, contact role taxonomy finalization, win/loss reason codes) but these are action items rather than full discovery sessions.

## New Questions Identified

### Proposed New Question: What is the standard probability threshold for inclusion in forecast reporting and dashboards?
- **Asked By**: Team (implicit policy confirmation in discussion)
- **Context**: Team states 70%+ threshold; needs configuration alignment in NetSuite
- **Suggested Placement**: Section on Forecasting & Pipeline Management
- **Evidence**: "We don't forecast anything below 70%… whenever we say forecast, it's 70% or greater" - Team

### Proposed New Question: What are the specific criteria for progressing an opportunity through each pipeline stage?
- **Asked By**: Identified gap during analysis
- **Context**: Stages are listed but criteria for moving between stages not defined; needed for consistent pipeline management
- **Suggested Placement**: Section on Opportunity Management Process
- **Evidence**: "Stage Definitions (To Be Finalized)" noted in transcript analysis

### Proposed New Question: How should territory-based opportunities be handled when accounts span multiple territories?
- **Asked By**: Identified gap during analysis  
- **Context**: Three distinct territories (SF, San Jose, Sacramento) but process for shared accounts not discussed
- **Suggested Placement**: Section on Territory Management
- **Evidence**: Territory structure documented but overlap scenarios not addressed

## Questionnaire Responses

---

### 1. CURRENT STATE: CRM System & Process

**1.1. What CRM system(s) are currently in use?**

**Answer:**
KBM Hoag currently uses Zendesk as their CRM system for opportunity tracking, lead management, and forecasting. However, Zendesk usage is **optional** and **not required**, leading to significant data quality issues. Core serves as the master customer database, and Asana is used for RFP project workflow management. These systems are completely disconnected with no automatic data sync.

**Current State Process:**
**PROCESS**: Opportunity Management  
**TRIGGER**: Lead identified through relationship, RFP, or web form  
**STEPS**:
1. BD rep/GM **may** enter opportunity in Zendesk (optional, inconsistent)
2. Opportunity assigned value and probability (if entered)
3. Activities and tasks documented (varies by user - some diligent, some minimal)
4. Forecasting updates supposed to happen regularly (inconsistent)
5. If Closed Won → Manual transfer to Core → Create customer record → Begin order process
6. If Closed Lost → Mark as lost → "Dies in there" (no systematic learning)

**SYSTEMS INVOLVED**: Zendesk (CRM), Core (order management/customer master), Asana (RFP workflow)  
**PAIN POINTS**: 
- Not required = ignored by many users
- "Some people are actually working, and you have other people that are just licking everything and calling it theirs"
- No validation or data quality standards
- Manual transfer between systems when deal closes
- Lost opportunities provide no learning ("dies in there")
- No integrated visibility across teams

**BRD Requirements:**
- [REQUIREMENT] Migrate from Zendesk to integrated NetSuite CRM (ID: REQ-001, Type: Functional)
- [REQUIREMENT] Make opportunity entry required with validation rules (ID: REQ-002, REQ-003, Type: Functional)
- [PRIORITY] Must-Have

**Evidence:**
- "Not required - many don't" [enter opportunities] - Transcript
- "Some people are actually working, and you have other people that are just licking everything and calling it theirs" - Kimmy
- "The data entry part of it has never been clean enough to trust in" - Team
- "Dies in there" if lost (no learning) - Transcript
- "Zendesk → Core manual transfer" - Current process documentation

**Confidence Rating**: 95% - Direct quotes with clear context from multiple transcript sources

---

**1.2. What are your primary lead sources?**

**Answer:**
KBM Hoag's lead generation is **relationship-based**, not marketing-driven. Lead sources in order of importance:

1. **Relationships/Influencers (PRIMARY):**
   - Business Development reps (Jill - SF, Kate - San Jose, Alex - Sacramento) cultivate influencer relationships
   - Types: Brokers, A&D firms, existing clients, manufacturers, PM firms, CM firms
   - General Managers manage their territory relationships
   - Tenant-in-the-market lists

2. **RFPs (Significant Volume):**
   - Always relationship-based: "Never cold RFPs to KBM Hoag"
   - Sources: PM firms, A&D firms, direct clients, manufacturers
   - Come through existing relationships

3. **Web Contact Form (Minimal Viable Leads):**
   - Most submissions non-viable: cleaning quotes, odd requests
   - Quote: "A lot of cleaning quotes or 'I inherited my grandmother's Newell Eames chair and need a pad for it'"
   - Occasional legitimate opportunity (success story: cubicles order)
   - Jenny (Admin) qualifies and routes

4. **Referrals:**
   - Existing client referrals
   - Manufacturer referrals
   - Partner/word-of-mouth

**User Stories:**
- As a BD Rep (Jill, Kate, Alex), I need to track my influencer relationships and associated opportunities so that I can nurture strategic accounts and measure relationship ROI
- As Jenny (Admin), I need web form submissions to automatically create leads in NetSuite so that I can efficiently qualify and route them to the appropriate GM or account manager

**BRD Requirements:**
- [REQUIREMENT] Track lead source types: Relationship/Influencer, RFP, Web Form, Referral, Event (ID: REQ-009, Type: Functional)
- [REQUIREMENT] Web form integration to auto-create leads (ID: REQ-006, Type: Functional)
- [REQUIREMENT] Lead routing rules: Jenny → GM/Account Manager (ID: REQ-007, Type: Functional)
- [FUNCTIONALITY] NetSuite Lead Management & Web-to-Lead
- [PRIORITY] Must-Have

**Evidence:**
- "Never cold RFPs to KBM Hoag" - always relationship-based - Team
- "A lot of cleaning quotes or 'I inherited my grandmother's Newell Eames chair and need a pad for it'" - Team describing web form quality
- Primary lead sources section extensively documented in Master_Transcript_CRM.md lines 65-108

**Confidence Rating**: 95% - Extensive detail with direct quotes

---

**1.3. How do Business Development and Account Manager roles differ?**

**Answer:**
**Business Development Reps (Jill, Kate, Alex):**
- Market-facing customer acquisition focus
- Relationship building with influencers (brokers, A&D firms, clients)
- "Wining and dining" approach
- Lead generation through relationship cultivation
- Territory/market-specific: Jill-SF, Kate-San Jose, Alex-Sacramento
- Different approaches by GM/region and market dynamics

**Account Managers:**
- Role is **"Broad on purpose" - varies by individual**
- Depends on skill set and compensation structure
- Two general approaches:
  1. **BD-Like Account Managers**: Generate own leads, relationship-focused, client acquisition
  2. **Sales Support Account Managers**: Project support after handoff, less lead generation, execution/delivery focus
- All have some PM duties (varies by project complexity)
- Manage client relationship through project completion

**Quote:** "Role execution depends on individual skill set and comp structure" - Team

**BRD Requirements:**
- [REQUIREMENT] Support role-based security and dashboards for BD vs. Account Manager personas (ID: REQ-041, REQ-042, Type: Functional)
- [REQUIREMENT] Territory assignment by BD rep (ID: REQ-013, Type: Functional)
- [ASSUMPTION] Both roles will use CRM but with different primary functions (BD: lead gen/relationships; AM: opportunity execution)
- [PRIORITY] Must-Have

**Stakeholder Impact:**
- **Primary Users**: Jill (BD-SF), Kate (BD-San Jose), Alex (BD-Sacramento), Account Managers (various)
- **Impacted Parties**: General Managers who oversee territory performance

**Evidence:**
- "Broad on purpose" - Account Manager role variability - Team
- Business Development vs. Account Manager roles section in Master_Transcript_CRM.md lines 111-158
- Territory structure documented lines 567-579

**Confidence Rating**: 92% - Multiple supporting statements with clear context

---

**1.4. What are the current data quality challenges?**

**Answer:**
Data quality is a **critical pain point** in the current Zendesk implementation:

**Challenges:**
- **Inconsistent Entry**: CRM entry is optional, so many users don't enter opportunities or enter minimal information
- **Variable Quality**: Some users diligent (activities, tasks, contacts documented); some just "claim the lead"
- **No Validation**: No required fields or validation rules
- **No Standards**: No accountability for data completion or accuracy
- **Can't Trust Data**: Forecasting unreliable; can't segment contacts; reporting meaningless
- **Manual Processes**: No automatic data flow between systems
- **Quote: "Poo in, poo out"** - Team describing data quality issue

**Contact Management Issues:**
- Core contact type options inadequate ("Main contact? Finance? Procurement? We don't know")
- No contact role classification
- Can't segment effectively for targeted communication
- No duplicate detection (multiple records for same contact/company)
- No chain of control for data maintenance

**Forecasting Impact:**
- "The data entry part of it has never been clean enough to trust in" - Team
- Accuracy varies widely by user
- Probability weighting subjective
- Value estimates vary in quality
- Hard to trust for planning; manual validation needed

**BRD Requirements:**
- [REQUIREMENT] Implement validation rules and required fields (ID: REQ-003, Type: Non-Functional) [ACCOMMODATE]
- [REQUIREMENT] Make opportunity entry required (ID: REQ-002, Type: Non-Functional) [ADAPT]
- [REQUIREMENT] Custom contact role classifications (ID: REQ-010, REQ-011, Type: Functional) [ACCOMMODATE]
- [REQUIREMENT] Duplicate detection and merge capabilities (ID: REQ-014, Type: Functional)
- [CONSTRAINT] Cultural change needed - sales team may resist structure
- [RISK] If data quality standards not enforced, same problems will occur in NetSuite
- [PRIORITY] Must-Have

**Evidence:**
- "Poo in, poo out" - Team
- "Some people are actually working, and you have other people that are just licking everything and calling it theirs" - Kimmy
- "The data entry part of it has never been clean enough to trust in" - Team
- Data Quality & Standardization section lines 501-615 in Master_Transcript_CRM.md

**Confidence Rating**: 95% - Extensive direct quotes and multiple supporting statements

---

### 2. FUTURE STATE: NetSuite CRM Requirements

**2.1. Describe the desired integrated transaction flow**

**Answer:**
NetSuite will provide seamless integrated flow: **Lead → Opportunity → Quote/Proposal → Sales Order → Project**

**Key Characteristics:**
- **All stages visible and linked** - no manual transfer between systems
- **Project number/name consistent** across all transactions
- **Different transaction numbers but connected**: OP-#### (Opportunity), PR-#### (Proposal), SO-#### (Sales Order)
- **One-click conversion** at each stage with automatic data transfer
- **Complete audit trail** maintained throughout
- **Cross-functional visibility** for all teams
- **Maintains linkage** from first contact through project completion

**Benefits:**
- Eliminates manual transfer between Zendesk and Core
- Automatic data flow - no re-entry
- Complete customer journey visibility
- Handoff from sales to operations seamless
- Performance tracking (forecast vs. actual)
- No opportunities "dying" in disconnected system

**User Stories:**
- As a Sales Rep, I need to convert an opportunity to a quote with one click so that I don't have to re-enter customer information and can maintain a complete audit trail
- As an Operations Manager, I need to see the complete history from opportunity through quote when a project kicks off so that I understand customer commitments and project context

**BRD Requirements:**
- [REQUIREMENT] Implement integrated Opportunity → Quote → SO → Project flow (ID: REQ-001, Type: Functional) [ALIGNS]
- [FUNCTIONALITY] NetSuite CRM + Quote Management + Order Management + Project Management
- [PRIORITY] Must-Have

**Evidence:**
- "Opportunity → Quote → Sales Order, all stages visible and linked, project number/name consistent across all transactions" - Marcus
- Transaction Flow Integration section lines 238-259 in Master_Transcript_CRM.md

**Confidence Rating**: 95% - Direct quote with clear description of desired state

---

**2.2. What are the opportunity management requirements?**

**Answer:**

**Opportunity Record Capabilities Required:**
- **Pipeline tracking** with visual stage management (Kanban boards)
- **Forecasting** with probability weighting (70%+ threshold for forecast inclusion)
- **Value tracking** (projected revenue)
- **Source attribution** (where did opportunity originate?)
- **Market/sector classification** (Healthcare, Tech, Corporate, Government, Education, etc.)
- **Related contacts** and relationship mapping
- **Activity tracking** (calls, emails, meetings) with history
- **Document attachment** (RFPs, proposals, correspondence)
- **Team collaboration** (notes, tasks, assignments)
- **Territory assignment** (SF, San Jose, Sacramento)

**Required Information (Minimum Fields - To Be Defined via Action Item):**
- Opportunity name/description
- Account/Company
- Primary contact
- Value estimate
- Probability percentage
- Stage
- Expected close date
- Source
- Sector/market
- Territory
- Assigned owner

**Pipeline Stages (To Be Finalized):**
- Lead/Prospect
- Qualification
- Needs Analysis
- Proposal/RFP
- Negotiation
- Closed Won
- Closed Lost

**Forecasting Approach:**
- **Forecast from Opportunity level** (not quote level) to prevent over-forecasting
- **70%+ probability threshold** for forecast inclusion
- If multiple quotes: Manual sync to update opportunity amount
- "Someone's gonna have to manage which quote amount should go back to the opportunity" - Team

**Visibility Rules:**
- Opportunities restricted to assigned users only
- Prevents "doom-scrolling" company-wide activity feed issue from Zendesk

**User Stories:**
- As a BD Rep, I need to create and track opportunities with all relevant context so that my forecast is accurate and my team has visibility into my pipeline
- As a Sales Manager, I need to see my team's opportunities with consistent data quality so that I can coach effectively and forecast accurately to executives

**BRD Requirements:**
- [REQUIREMENT] Opportunity management with all fields listed above (ID: REQ-001, Type: Functional)
- [REQUIREMENT] Kanban board visualization (ID: REQ-004, Type: Functional) [ALIGNS]
- [REQUIREMENT] Opportunity-level forecasting (ID: REQ-016, Type: Functional) [ADAPT]
- [REQUIREMENT] 70%+ probability threshold (ID: REQ-017, Type: Non-Functional) [ADAPT]
- [REQUIREMENT] Required fields and validation (ID: REQ-002, REQ-003, Type: Non-Functional) [ADAPT/ACCOMMODATE]
- [REQUIREMENT] Assigned-user visibility restriction (ID: REQ-005, Type: Non-Functional) [ADAPT]
- [FUNCTIONALITY] NetSuite Opportunity Management, Custom Fields, Validation Rules
- [PRIORITY] Must-Have

**Evidence:**
- Opportunity Record section lines 292-318 in Master_Transcript_CRM.md
- Forecasting Recommendations section lines 304-318
- "I think it'd be a good tool for us to try and test out" - Matt on Kanban boards
- "We don't forecast anything below 70%… whenever we say forecast, it's 70% or greater" - Team

**Confidence Rating**: 90% - Well-supported inferences from context; some specifics marked as "To Be Finalized" via action items

---

**2.3. What contact and account management capabilities are needed?**

**Answer:**

**Contact Record Requirements:**

**Role Classification (Custom, Beyond Core Limitations):**
- Primary Contact
- Decision Maker
- Finance/Accounting
- Procurement
- Facilities
- Project Manager
- Executive Sponsor
- Influencer (Broker)
- A&D (Architect & Design)
- CM (Construction Manager)
- PM (Project Manager firm)
- GC (General Contractor)
- Manufacturer Rep
- Vendor Contact
- **Support multiple roles per contact** if appropriate

**Sector/Market Assignment:**
- Healthcare (trending up - opportunity to focus)
- Technology
- Corporate Office
- Government
- Education
- Financial Services
- Legal
- Creative/Agency
- Hospitality
- Other

**Other Contact Capabilities:**
- **Territory/geography** (SF, San Jose, Sacramento)
- **Relationship type** (Client, Prospect, Influencer, Partner, Vendor)
- **Activity tracking** (all interactions logged with history)
- **Communication preferences**
- **Opt-in/opt-out status** (automatic management for email compliance)
- **Related opportunities and projects** (full history/360° view)

**Segmentation Capabilities:**
- **Unlimited custom criteria** for list building
- **Role-based lists** (all brokers, all A&D firms, all PMs)
- **Sector-based lists** (all healthcare contacts)
- **Geography-based lists** (San Francisco territory)
- **Combined criteria** (Healthcare brokers in SF)
- **Dynamic vs. static lists**
- **Saved segments** for reuse

**Marketing Use Case:**
- "If marketing had more insight into what some of those leads are and could see and track over time the sectors and how the market is changing, then it would be easier for that team to create proactively create content and target it" - Marketing Team

**Duplicate Detection:**
- NetSuite native duplicate detection during entry
- AI-enhanced identification
- Merge capabilities
- Prevention of duplicate creation
- **Critical need** - Core lacks this, causing data quality issues

**User Stories:**
- As a Marketing Manager, I need to segment contacts by role and sector so that I can send targeted communications to specific groups (brokers, healthcare contacts, SF territory)
- As a BD Rep, I need to track all my influencer contacts (brokers, A&D firms) with their sectors and territories so that I can strategically nurture relationships
- As an Admin (Jenny), I need duplicate detection to prevent multiple records for the same contact so that our database stays clean and reliable

**BRD Requirements:**
- [REQUIREMENT] Custom contact roles with multiple role support (ID: REQ-010, REQ-011, Type: Functional) [ACCOMMODATE]
- [REQUIREMENT] Sector/vertical tracking (ID: REQ-012, Type: Functional) [ALIGNS]
- [REQUIREMENT] Territory assignment (ID: REQ-013, Type: Functional) [ALIGNS]
- [REQUIREMENT] Duplicate detection and merge (ID: REQ-014, Type: Functional) [ALIGNS]
- [REQUIREMENT] Opt-in/opt-out tracking (ID: REQ-015, Type: Functional) [ALIGNS]
- [REQUIREMENT] Segmentation engine (ID: REQ-047, Type: Functional) [ALIGNS]
- [FUNCTIONALITY] NetSuite Contact Management, Custom Fields, List Management
- [PRIORITY] Must-Have

**Evidence:**
- Contact & Account Management section lines 319-352 in Master_Transcript_CRM.md
- Contact Role Classification section lines 504-543
- Market Sectors/Verticals section lines 546-565
- "Are they the main contact? Are they finance? Is it procurement? We don't know" - Team on Core limitations
- Marketing insight quote from transcript line 305

**Confidence Rating**: 93% - Multiple supporting statements and detailed requirements documented

---

**2.4. What approval workflows need to be configured?**

**Answer:**

KBM Hoag has specific approval rules that must be migrated to NetSuite:

**Approval Rule 1: Order Value > $25,000**
- **Trigger**: Sales order exceeds $25,000
- **Route To**: Shannon (Project Coordinator Manager)
- **Purpose**: Verify completeness and readiness before processing
- **Classification**: [ALIGNS] - straightforward threshold rule

**Approval Rule 2: Missing Required Documents**
- **Trigger**: Order missing ANY of: Deposit, Signed proposal, Signed drawings, Signed lookbook
- **Route To**: Matt (primary), Mark (backup)
- **Current Behavior**: "They do all day unabashedly, could care less" - frequently request exceptions
- **Matt's Response**: "So good and quick about responding"
- **Classification**: [ALIGNS] - validation rule with approval

**Approval Rule 3: Erosion > $1,500 Cumulative**
- **Trigger**: Cumulative erosion on project exceeds $1,500 (example: $500 + $1,000 = $1,500)
- **Route To**: Matt (email approval)
- **Purpose**: Training insight ("new person often reason for erosion"), problem-solving opportunity
- **Matt's Philosophy**: Not punishment - identifying training needs, finding cheaper alternatives
- **Example**: Clay's crane rental story: $6K-$10K crane vs. $1.2K elevator technician solution
- **Quote**: "If we're going to spend the money, let's spend it this way"
- **Frequency**: "Sounds like a lot, but it's not that much" - happens infrequently
- **Process**: "Usually make the PCs do it" (Project Coordinators submit requests)
- **Classification**: [ALIGNS] - threshold rule with learning component

**Approval Rule 4: Double Order Detection (NEW)**
- **Pain Point**: "Biggest losses from double orders"
- **Example**: 150 workstations ordered and owned before discovered (at shipment notice)
- **Challenge**: Sometimes legitimately ordering similar items or bulk orders ("technically a 'double order' but intentional")
- **Solution**: Query for same total dollar amount within past 30 days → Flag for manual review (not automatic rejection)
- **Quote**: "Not a hard query" to build
- **Don't want**: Constant "Are you sure?" prompts (users will click yes without thinking)
- **Classification**: [ACCOMMODATE] - custom query/alert

**General Approval Capabilities Needed:**
- **Business rule engine** with flexible logic
- **Automatic routing** to approvers
- **Dashboard notifications** for approvers
- **Approval/rejection/exception** handling
- **Timestamp and audit trail**
- **Approval time tracking** by approver (identify bottlenecks)
- **Average time-to-approve** reporting

**Complexity Caution:**
"More checks = slower process. Must manage approvers. Report on time-to-approve. Find balance between control and speed." - Team

**User Stories:**
- As Shannon (Project Coordinator Manager), I need orders over $25K to route to me for approval so that I can verify completeness before processing
- As Matt, I need erosion approvals over $1,500 to come to me so that I can identify training opportunities and help the team problem-solve before spending money
- As a Project Coordinator, I need the system to alert me if I'm creating a potential double order so that I can verify before submitting

**BRD Requirements:**
- [REQUIREMENT] Order approval > $25K to Shannon (ID: REQ-021, Type: Functional) [ALIGNS]
- [REQUIREMENT] Missing documents approval to Matt (ID: REQ-022, Type: Functional) [ALIGNS]
- [REQUIREMENT] Erosion > $1,500 approval to Matt (ID: REQ-023, Type: Functional) [ALIGNS]
- [REQUIREMENT] Double-order detection query (ID: REQ-024, Type: Functional) [ACCOMMODATE]
- [REQUIREMENT] Approval time tracking (ID: REQ-025, Type: Functional) [ALIGNS]
- [FUNCTIONALITY] NetSuite Workflow Engine, Approval Routing, Business Rules (up to 10 rules in BRD budget)
- [PRIORITY] Must-Have
- [ASSUMPTION] Matt is primary approver with Mark as backup

**Stakeholder Impact:**
- **Approvers**: Shannon (Project Coordinator Manager), Matt (primary), Mark (backup)
- **Impacted Parties**: Project Coordinators (submit requests), Sales team (experience approval delays)

**Evidence:**
- Current Approval Process section lines 417-476 in Master_Transcript_CRM.md
- "They do all day unabashedly, could care less" - requesting exceptions from Matt
- "So good and quick about responding" - Matt's approval responsiveness
- Clay's crane rental story (erosion review example) lines 446-452
- "Biggest losses from double orders... 150 workstations ordered and owned" - Double order pain point
- Shannon to document flowchart as action item

**Confidence Rating**: 95% - Direct quotes with clear context and specific dollar thresholds documented

---

**2.5. What are the vendor credit limit requirements?**

**Answer:**

**Need:**
Track KBM Hoag's credit limits with vendors to prevent unexpected order failures. Currently, they hit vendor credit limits without warning, causing "mad scramble at that nth hour because our order won't go through because we hit it."

**Solution Requirements:**
- **Vendor record field**: Credit limit amount
- **Warning threshold**: Alert at percentage threshold (e.g., 90% of limit)
- **Prevent PO creation**: Block PO if over limit (hard stop)
- **Dashboard visibility**: Portlet showing vendors approaching limits
- **Alert system**: Notifications for purchasing team/buyers

**Implementation:**
- "Sounds like just a pretty simple query" - Team assessment
- Field on vendor record
- Business rule for warning
- Dashboard component for visibility

**User Stories:**
- As a Buyer, I need to see which vendors we're approaching credit limits with so that I can proactively manage payment or find alternative vendors before orders are blocked
- As a Purchasing Manager, I need the system to prevent PO creation when we've exceeded a vendor credit limit so that we don't place orders that can't be fulfilled

**BRD Requirements:**
- [REQUIREMENT] Vendor credit limit field (ID: REQ-029, Type: Functional) [ACCOMMODATE]
- [REQUIREMENT] Credit limit warning and PO prevention (ID: REQ-030, Type: Functional) [ACCOMMODATE]
- [FUNCTIONALITY] Vendor Record Customization, Business Rule, Dashboard Portlet
- [SOLUTIONDESIGN] Yes - custom field and validation logic needed
- [PRIORITY] Should-Have

**Stakeholder Impact:**
- **Primary Users**: Purchasing team, Buyers
- **Approvers**: Finance (may need to set/update credit limits)

**Evidence:**
- "Mad scramble at that nth hour because our order won't go through because we hit it" - Team describing pain point
- Vendor Credit Limits section lines 479-498 in Master_Transcript_CRM.md
- "Sounds like just a pretty simple query" - Implementation assessment

**Confidence Rating**: 93% - Clear business need with supporting quotes

---

### 3. FORECASTING & ANALYTICS

**3.1. What are the pipeline and forecasting requirements?**

**Answer:**

**Pipeline Visibility Needs:**
- **Real-time pipeline by stage** - see where opportunities are stuck
- **Pipeline by BD rep / Account Manager** - individual performance
- **Pipeline by sector** - which markets are growing?
- **Pipeline by territory** - SF vs. San Jose vs. Sacramento performance
- **Aging analysis** - opportunities stuck in stage too long
- **Velocity metrics** - time in each stage (sales cycle length)

**Forecasting Requirements:**
- **Opportunity-level forecasting** (not quote-level) to prevent over-forecasting
- **70%+ probability threshold** for forecast inclusion
- **Forecast types**:
  - Commit (high confidence)
  - Best Case (if everything goes well)
  - Pipeline (everything weighted by probability)
  - Historical (actual results for comparison)
- **Forecast accuracy tracking** by user over time
- **Historical accuracy reporting** to identify most accurate forecasters and learn from best practices

**Current Challenge:**
- "Forecast accuracy varies by user"
- "No systematic tracking of accuracy"
- "Can't improve without measurement"
- "Executive confidence in forecast low"

**Probability by Stage (To Be Defined via Action Item):**
- Typically 10% → 90% as opportunities progress through stages
- Consistent application needed
- Training on stage criteria required
- Regular pipeline reviews

**User Stories:**
- As a Sales Manager, I need to see my team's pipeline by stage so that I can identify bottlenecks and coach reps on opportunities that aren't progressing
- As a CFO, I need accurate revenue forecasting by territory and sector so that I can plan resources and set expectations with the board
- As a BD Rep, I need to track my forecast accuracy over time so that I can improve my estimation skills and build credibility

**BRD Requirements:**
- [REQUIREMENT] Pipeline tracking by stage, rep, sector, territory (ID: REQ-016, Type: Functional) [ADAPT]
- [REQUIREMENT] 70%+ probability forecast threshold (ID: REQ-017, Type: Non-Functional) [ADAPT]
- [REQUIREMENT] Forecast accuracy tracking by user (ID: REQ-018, Type: Functional) [ADAPT]
- [REQUIREMENT] Define stages and probability by stage (ID: REQ-019, Type: Non-Functional) [ADAPT]
- [REQUIREMENT] Pipeline reports and dashboards (ID: REQ-041, REQ-042, REQ-043, Type: Functional)
- [FUNCTIONALITY] NetSuite Forecasting, Pipeline Reporting, Custom Dashboards
- [PRIORITY] Must-Have

**Evidence:**
- Pipeline Management section lines 618-645 in Master_Transcript_CRM.md
- Forecasting Accuracy section lines 647-666
- "Forecast accuracy varies by user... No systematic tracking of accuracy... Can't improve without measurement"
- "We don't forecast anything below 70%… whenever we say forecast, it's 70% or greater" - Team

**Confidence Rating**: 92% - Multiple supporting statements; some details (probability by stage) to be finalized

---

**3.2. What win/loss analysis is needed?**

**Answer:**

**Current State:**
- "Dies in there" if lost - no systematic learning
- Minimal loss reason tracking
- No competitor intelligence captured
- No pattern identification
- Can't improve without understanding why deals are won or lost

**Future State Requirements:**
- **Required win/loss reason codes** (mandatory field before closing opportunity)
- **Win reasons tracked** as well as loss reasons
- **Competitor tracking** - who did we lose to? who did we beat?
- **Analysis by sector, size, type, territory** to identify patterns
- **Feedback loop** to improve sales approach
- **Continuous learning** culture

**Loss Reason Examples (To Be Defined via Action Item):**
- Price (lost on cost)
- Competitor (specific competitor name)
- Timing (project delayed/cancelled)
- Requirements not met (couldn't deliver what client needed)
- Relationship (chose incumbent/preferred vendor)
- Other (specify)

**Win Reason Examples:**
- Relationship
- Price
- Quality/reputation
- Timing
- Unique capability
- Other (specify)

**Use Cases:**
- Identify most common loss reasons by sector (e.g., losing healthcare deals on price?)
- Track competitor intelligence (who are we losing to most often?)
- Understand win patterns (what's working in SF vs. Sacramento?)
- Improve estimation (are we pricing too high/low in certain sectors?)
- Sales coaching (help reps understand why deals are won/lost)

**User Stories:**
- As a Sales Manager, I need to analyze win/loss patterns by sector so that I can adjust our approach and coach reps on what's working and what's not
- As a BD Rep, I need to document why I won or lost a deal so that the company can learn from my experience and improve over time
- As an Executive, I need to understand our competitive position by analyzing who we're losing to and why so that I can make strategic decisions about focus areas

**BRD Requirements:**
- [REQUIREMENT] Required win/loss reason codes (ID: REQ-026, Type: Functional) [ADAPT]
- [REQUIREMENT] Competitor tracking (ID: REQ-027, Type: Functional) [ADAPT]
- [REQUIREMENT] Win/loss analysis reports (ID: REQ-028, Type: Functional) [ADAPT]
- [FUNCTIONALITY] NetSuite Opportunity Management, Custom Fields, Reporting
- [PRIORITY] Should-Have

**Evidence:**
- Win/Loss Analysis section lines 667-690 in Master_Transcript_CRM.md
- "Dies in there if lost... No systematic learning... No competitor intelligence" - Current state description
- "Analysis by sector, size, type... Continuous learning" - Future state requirements

**Confidence Rating**: 88% - Well-supported inferences from context; specific reason codes marked as "To Be Defined"

---

### 4. DASHBOARDS & REPORTING

**4.1. What dashboard requirements exist for different user roles?**

**Answer:**

**Sales/BD Rep Dashboard:**

**Key Metrics:**
- My open opportunities
- My pipeline value
- My forecast (by type: Commit, Best Case, Pipeline)
- My activities this week
- My overdue tasks
- My opportunities by stage (visual pipeline)
- Recent wins
- Opportunities needing attention (aging, no activity)

**Filters:**
- By date range
- By stage
- By sector
- By probability
- By value range

**Manager Dashboard:**

**Key Metrics:**
- Team pipeline (rollup)
- Team forecast (by type)
- Individual performance comparison
- Pipeline by stage (team view)
- Aging opportunities (across team)
- Win/loss trends
- Activity metrics (who's logging activities?)
- Forecast accuracy by rep (learning opportunity)

**Filters:**
- **"Me and My Team"** (role-based hierarchy) - Critical requirement
- Individual team members (drill-down)
- Territory
- Sector
- Time period

**Core Limitation (Current Pain Point):**
"That's been one of the frustrations with Core. They do allegedly have this hierarchy of permissions, roles and permissions, and, like, this is the manager. They report to that manager, and that manager is supposed to see everyone, and it doesn't. I've never gotten that." - Marcus

**NetSuite Solution:**
"You have to have the right managers assigned for those filters to work. But if we set that up, if we set it up, it actually works. Good." - Team confirming NetSuite capability

**Executive Dashboard:**

**Key Metrics:**
- Company-wide pipeline (total)
- Forecast summary (all reps combined)
- Pipeline by sector (which markets are strongest?)
- Pipeline by territory (SF vs. San Jose vs. Sacramento)
- Win rate trends (improving or declining?)
- Average deal size
- Sales cycle length (time from opportunity creation to close)
- Conversion rates (lead → opportunity → customer)

**Drill-Down Capability:**
- **Click any metric → see detail records**
- Investigate anomalies
- Identify opportunities
- Spot problems early
- "Drill-down capability from dashboard metrics to detail"

**Additional Dashboard Need: Sales Goals (Replaces Excel)**

**Requirement:**
- "You want that to live in NetSuite? — Yes. Yes… a dashboard" - Matt
- Currently tracked in Excel, distributed weekly
- Need NetSuite dashboard to replace manual process

**Action Item:** Matt/Kip to provide current Sales Goals Excel template and layout for recreation in NetSuite

**User Stories:**
- As a Sales Rep, I need a personal dashboard showing my pipeline and tasks so that I can prioritize my day and stay on top of opportunities
- As a Sales Manager, I need a "Me and My Team" dashboard so that I can see my entire team's pipeline and performance without switching between individual views
- As an Executive, I need a company-wide dashboard with sector and territory breakdowns so that I can understand overall business health and identify strategic opportunities

**BRD Requirements:**
- [REQUIREMENT] BD/Sales Rep dashboard (ID: REQ-041, Type: Functional) [ALIGNS]
- [REQUIREMENT] Sales Manager dashboard with Me and My Team filters (ID: REQ-042, Type: Functional) [ADAPT]
- [REQUIREMENT] Executive dashboard (ID: REQ-043, Type: Functional) [ALIGNS]
- [REQUIREMENT] Drill-down capability (ID: REQ-044, Type: Functional) [ALIGNS]
- [REQUIREMENT] Sales Goals dashboard to replace Excel (ID: REQ-020, Type: Functional) [ACCOMMODATE]
- [FUNCTIONALITY] NetSuite Dashboards, Role-Based Views, Drill-Down Navigation
- [SOLUTIONDESIGN] Yes - Sales Goals dashboard needs custom design
- [PRIORITY] Must-Have

**Stakeholder Impact:**
- **Primary Users**: All sales/BD reps, Sales Managers, Executives
- **Success Metric**: Reduction in manual Excel reporting; increased visibility into pipeline

**Evidence:**
- Sales/BD Dashboard section lines 693-713 in Master_Transcript_CRM.md
- Manager Dashboard section lines 715-738
- Executive Dashboard section lines 740-756
- "That's been one of the frustrations with Core... I've never gotten that" - Marcus on Core limitation
- "You want that to live in NetSuite? — Yes. Yes… a dashboard" - Matt on Sales Goals

**Confidence Rating**: 94% - Detailed requirements with supporting quotes; some customization details to be finalized

---

### 5. MARKETING INTEGRATION

**5.1. What email marketing capabilities are needed?**

**Answer:**

**NetSuite Email Marketing Capability:**
- **Capacity**: 120,000 emails/month included
- **KBM Hoag Assessment**: "Way more than we would ever use"
- **Current Usage**: Less than 6 campaigns per year via MailChimp pay-as-you-go credits
- **Decision**: Minimal implementation during Phase 1; can enable post-go-live if needed

**Current Marketing Approach (Unique):**
- **NOT traditional B2B marketing** (no broad campaigns, mass blasts, content marketing)
- **Relationship-based**: Personal one-to-one communication
- **Targeted sector focus**: Specific people within specific industries
- **Strategic shift last year**: Moved away from mass communications to targeted approach
- **Quote**: "So much of what we do is relationship-based, and so we're being very selective of, like, hey, we want to invite these specific 20 people, and we're sending an email from a real person's email, rather than from info at KBM"

**Historical Context:**
- Discontinued quarterly newsletters (internal and external)
- Discontinued event invitations via mass email
- Shifted to personalized, relationship-based outreach
- **Result**: Better engagement, though lower volume

**Email Marketing Features (If/When Used):**
- **Subscription management**: Automatic opt-in/opt-out tracking (critical for compliance)
- **Templates**: Available but KBM Hoag creates images in Google Slides
- **Campaigns**: Track opens, clicks, ROI
- **Segments**: Target by role, sector, geography, custom criteria

**Communication Types:**

**Transactional (No Opt-In Required):**
- Order confirmations
- Rate changes
- Process changes
- Invoices
- Important business communications
- Can send from info@kbmhoag.com or user email

**Marketing (Opt-In Required):**
- Promotional campaigns
- Event invitations (if mass email)
- Newsletters
- Requires opt-in management

**Current Challenge:**
- Manual list management in MailChimp
- "MailChimp gets really pissed off when you try to load in Excel because they think you're going to spam a bunch of people" - Jenny
- "Then most of it bounces anyways" - Jenny
- Can't segment by role or purpose
- "Click rates aren't great so there's just really no way right now to target" - Team

**Future State with NetSuite:**
- Automated segmentation by role, sector, territory
- Opt-in/opt-out automatically managed
- One-click targeted campaigns (when needed)
- Reduced manual effort
- Better tracking and analytics

**Desired Segmentation Use Cases:**
- Curated lists by role (brokers, PM firms, CM firms)
- Market-specific campaigns (SF market ≠ San Jose market)
- Sector-specific targeting (healthcare trending up → tailored message)
- Quarterly market rate communications to specific groups
- **Quote**: "If marketing had more insight into what some of those leads are and could see and track over time the sectors and how the market is changing, then it would be easier for that team to create proactively create content and target it" - Marketing Team

**User Stories:**
- As a Marketing Manager, I need to send targeted communications to specific contact segments (e.g., all healthcare brokers in SF) so that I can deliver relevant messages without spamming our entire database
- As Jenny (Admin), I need opt-in/opt-out status to be automatically managed so that I don't risk MailChimp complaints or compliance issues
- As a GM, I need to send rate change notifications to all my territory's clients so that they're informed of business changes without requiring manual list creation

**BRD Requirements:**
- [REQUIREMENT] Email marketing capability with minimal implementation (ID: REQ-045, Type: Functional) [ALIGNS]
- [REQUIREMENT] Automatic subscription management (ID: REQ-046, Type: Functional) [ALIGNS]
- [REQUIREMENT] Segmented contact lists (ID: REQ-047, Type: Functional) [ALIGNS]
- [REQUIREMENT] Campaign performance tracking (ID: REQ-048, Type: Functional) [ALIGNS]
- [FUNCTIONALITY] NetSuite Email Marketing, Subscription Management, List Builder
- [PRIORITY] Nice-to-Have (Phase 1); Can enable post-go-live
- [DECISION] Minimal focus during implementation; team comfortable with current low-volume approach

**Stakeholder Impact:**
- **Primary Users**: Marketing Team, Jenny (Admin)
- **Secondary Users**: GMs (for territory-specific communications)

**Evidence:**
- Email Marketing section lines 32-47 in Master_Transcript_Marketing_CRM.md
- "Capacity way more than we would ever use... Less than 6 campaigns per year" - Team
- "So much of what we do is relationship-based..." - Team on marketing approach
- Communication Challenges section lines 232-243
- "MailChimp gets really pissed off..." - Jenny
- Marketing insight quote line 305 in Master_Transcript_Marketing_CRM.md

**Confidence Rating**: 95% - Direct quotes with clear context; explicit decision on minimal implementation

---

**5.2. What is the RFP management process and requirements?**

**Answer:**

**Current RFP Process:**
1. RFP identified/received through relationship
2. **May** be entered in Zendesk (inconsistent)
3. When RFP formally arrives → BD rep or Account Manager submits formal project request in **Asana**
4. Request includes: Background, project links, documentation, **projected volume** (key metric)
5. Marketing PM schedules kickoff call with stakeholders
6. Marketing team develops response
7. Track: Projected vs. Actual volume
   - Identify who over-estimates
   - Improve accuracy over time
   - Better resource allocation

**Pain Points:**
- **Marketing has no visibility until formal request submitted**
- Can't proactively prepare
- Can't track market trends from early-stage RFPs
- Resource allocation challenging without early visibility

**Marketing Role (Unique Aspect):**
- "Your marketing department is actually doing like some sales process really, right? Because you're doing RFPs" - Marcus
- Not traditional demand generation
- RFP response coordination and presentation development
- Client-facing materials and brand management

**Proposed Improved Process in NetSuite:**
1. RFP identified → **Create Opportunity in NetSuite immediately**
2. BD/Account Manager enters preliminary information
3. When RFP formally received → Update opportunity, attach documents
4. **Generate Quote/Proposal record** (linked to opportunity)
5. Assign to Marketing team (workflow/routing)
6. **Marketing PM gains visibility into pipeline**
7. Kickoff meeting scheduled
8. Projected volume documented on quote/project
9. Marketing develops response
10. Track: Projected vs. Actual volume
11. Close Won/Lost with reason codes
12. Analysis and learning

**Benefits:**
- **Early visibility** for marketing team
- **Market trend intelligence** - see which sectors/types of projects coming
- **Proactive resource planning** - marketing capacity management
- **Better volume forecasting** - learn who estimates accurately
- **Historical performance** by estimator
- **Sector/market trend tracking**

**Volume Tracking (Critical Requirement):**

**Current Challenge:**
- People overestimate volume
- Resource allocation difficult
- Actual volume often significantly different from projected

**Solution:**
- **Track projected volume on RFP/Quote**
- **Track actual volume on Sales Order/Project**
- **Report: Projected vs. Actual by user**
- Identify patterns:
  - Who is most accurate?
  - Which sectors have largest variance?
  - Improve estimates over time
- Better resource allocation (marketing team capacity planning)

**Document Management:**
- Attach RFP documentation to opportunity/quote
- Link to Google Drive project folder (current practice to maintain)
- Version control and team access
- Client-provided materials
- Marketing-created presentations and proposals
- Link or attach to quote record for future reference

**User Stories:**
- As a Marketing PM, I need visibility into all RFP opportunities as soon as they're identified so that I can proactively plan resources and prepare for formal requests
- As a Marketing Manager, I need to track projected vs. actual volume by estimator so that I can allocate my team's capacity more accurately and coach people on better estimation
- As a Sales Rep, I need to attach RFP documents to the opportunity so that the marketing team has all the context they need when they begin developing the response

**BRD Requirements:**
- [REQUIREMENT] Early opportunity creation for RFPs (ID: REQ-002, Type: Functional) [ADAPT]
- [REQUIREMENT] Document attachment to opportunities/quotes (ID: REQ-036, Type: Functional) [ALIGNS]
- [REQUIREMENT] Google Drive folder linking (ID: REQ-037, Type: Functional) [ALIGNS]
- [REQUIREMENT] Projected volume tracking field on quote (new custom field) [ACCOMMODATE]
- [REQUIREMENT] Actual volume tracking field on project (new custom field) [ACCOMMODATE]
- [REQUIREMENT] Projected vs. Actual volume report [ACCOMMODATE]
- [FUNCTIONALITY] NetSuite Opportunity/Quote Management, Custom Fields, Document Management, Reporting
- [SOLUTIONDESIGN] Yes - volume tracking fields and report need custom design
- [PRIORITY] Must-Have (RFP process critical to business)
- [ASSUMPTION] Asana may still be used for marketing project execution; NetSuite for RFP tracking and visibility

**Stakeholder Impact:**
- **Primary Users**: Marketing PMs, BD Reps, Account Managers
- **Secondary Users**: Marketing team members (response development)
- **Approvers**: GMs (RFP decision-making)

**Evidence:**
- RFP Management Workflow section lines 197-220 in Master_Transcript_Marketing_CRM.md
- RFP Management in NetSuite section lines 355-412
- Volume Tracking & Accuracy section lines 382-396
- "Your marketing department is actually doing like some sales process really, right? Because you're doing RFPs" - Marcus
- "Marketing has no visibility until formal request submitted" - Current pain point
- "People overestimate volume... Resource allocation difficult" - Challenge description

**Confidence Rating**: 92% - Multiple supporting statements; volume tracking is well-documented need

---

### 6. DATA MIGRATION & CHANGE MANAGEMENT

**6.1. What data migration requirements exist?**

**Answer:**

**Data Sources:**
- **Zendesk**: Opportunity history (current CRM)
- **Core**: Contact data, account data, customer history
- **MailChimp**: Contact lists (though data quality questionable)

**Opportunity History from Zendesk:**
- **Approach**: Export entire history via CSV
- **Import**: Into NetSuite with "historical" tagging
- **Quote**: "You can export the entire… CSV… import it and tag it" - Kip
- **Purpose**: Maintain historical context; learning from past opportunities
- **Classification**: [ALIGNS] - standard CSV import with tagging

**Contact Data from Core:**
- **Challenge**: Poor data quality ("poo in, poo out")
- **Need**: Deduplication during migration
- **NetSuite Capability**: Duplicate detection and merge
- **Classification/Segmentation**: Contacts need to be classified by:
  - Role (Primary Contact, Decision Maker, Finance, etc.)
  - Sector/Market (Healthcare, Tech, Corporate, etc.)
  - Territory (SF, San Jose, Sacramento)
  - Relationship Type (Client, Prospect, Influencer, Partner, Vendor)

**Account/Customer Data from Core:**
- Company information
- Industry/sector
- Territory assignment
- Historical revenue
- Current customer status

**Data Quality Considerations:**
- **Critical**: Clean data from start of migration
- **Deduplication**: Required during import (Core lacks duplicate detection)
- **Classification**: May need manual effort to properly classify contacts by role/sector
- **Validation**: Use migration as opportunity to enforce data standards
- **Owner**: Need to identify data quality champion/owner

**User Stories:**
- As a CRM Administrator, I need to import Zendesk opportunity history with clear tagging so that users can access historical context without confusing old data with active opportunities
- As Jenny (Admin), I need duplicate detection during contact migration so that we start with a clean database in NetSuite
- As a Sales Manager, I need contacts to be properly classified by role and sector during migration so that I can immediately begin using segmentation for targeted outreach

**BRD Requirements:**
- [REQUIREMENT] Import Zendesk opportunity history with historical tagging (ID: REQ-038, Type: Non-Functional) [ALIGNS]
- [REQUIREMENT] Migrate contact data with deduplication (ID: REQ-039, Type: Non-Functional) [ALIGNS]
- [REQUIREMENT] Classify contacts by role, sector, territory during import (ID: REQ-040, Type: Non-Functional) [ACCOMMODATE]
- [FUNCTIONALITY] NetSuite Data Import Tools, Duplicate Detection, CSV Import
- [SOLUTIONDESIGN] Yes - contact classification during migration may require custom mapping
- [PRIORITY] Must-Have
- [CONSTRAINT] Data quality in source systems is poor; expect significant cleanup effort
- [RISK] If contacts not properly classified during migration, data quality issues will persist

**Stakeholder Impact:**
- **Primary Users**: CRM Administrator, Jenny (Admin)
- **Impacted Parties**: All CRM users (benefit from clean data)
- **Owner**: TBD - need to identify data quality champion

**Evidence:**
- Data Migration requirements section lines 824-831 in Master_Transcript_CRM.md
- "You can export the entire… CSV… import it and tag it" - Kip & Team
- "Deduplication during migration" identified as requirement
- "Contact classification/segmentation" needed
- "Poo in, poo out" - Team on current data quality

**Confidence Rating**: 90% - Reasonable assumptions based on limited evidence; migration approach standard

---

**6.2. What are the change management considerations?**

**Answer:**

**Behavior Changes Required:**

**1. Consistent CRM Data Entry:**
- **Current**: Optional, ignored by many
- **Future**: Required with validation rules
- **Quote**: "Not required" → "Required for visibility"
- **Challenge**: "Some people just licking everything and calling it theirs" → Standardization needed

**2. Earlier Opportunity Creation:**
- **Current**: Enter when ready to forecast or at RFP arrival
- **Future**: Create at first knowledge of potential (especially RFPs for marketing visibility)
- **Purpose**: Better pipeline visibility, market intelligence

**3. Activity Logging:**
- **Current**: Minimal or none
- **Future**: Log all significant interactions (calls, meetings, emails tracked)
- **Purpose**: History maintained for team, better collaboration

**4. Data Quality Discipline:**
- Required fields completion
- Contact role classification
- Sector assignment
- Validation rule compliance
- Regular updates

**Resistance Points:**

**1. Sales Team Pushback (Primary Concern):**
- **Quote**: "Matt's philosophy: Sales will be our biggest pushback"
- May resist structure and perceived overhead
- Data entry seen as bureaucracy, not value-add
- "Licking everything" behavior needs to change
- **Need**: Demonstrate value for them (better forecasting, reduced work elsewhere)

**2. Time Investment:**
- Data entry takes time
- Activity logging feels like overhead
- **Counter**: Show ROI - better forecasting, reduced manual work, improved visibility
- **Strategy**: Quick wins essential

**3. Process Changes:**
- Comfortable with current Zendesk + Core + Asana mix
- New system = new learning curve
- Temporary productivity dip expected
- Change fatigue possible

**4. Accountability & Visibility:**
- Data quality becomes visible (good and bad performers apparent)
- Forecast accuracy tracked (performance transparency)
- Activity levels measurable
- May create discomfort for some users

**Success Factors:**

**1. Executive Sponsorship:**
- **Matt's support critical**
- Clear expectations set from top
- Accountability for CRM usage
- Recognition for compliance and data quality
- Consequences for persistent non-compliance

**2. Show Value Fast:**
- **Pipeline visibility** (immediate benefit)
- **Forecast accuracy** (measurable improvement tracking)
- **Win/loss insights** (strategic value for sales approach)
- **Reduced manual work** (time savings in reporting, list building)
- **Better team collaboration** (shared visibility)

**3. Training & Support:**
- **Role-specific training** (BD reps ≠ Account Managers ≠ Managers)
- Sales/BD-focused approach (not generic NetSuite training)
- Quick reference guides
- NetSuite champions identified (power users who can help peers)
- Ongoing support available
- Documentation accessible

**4. Data Quality Campaign:**
- Clean data from start (migration done right)
- Regular hygiene processes (ongoing cleanup)
- Recognition for good practices
- Gamification possible (leaderboard for data quality?)
- Shared ownership culture

**5. Incremental Adoption:**
- Start with core functionality (don't overwhelm)
- Add sophistication over time
- Build confidence gradually
- Celebrate wins publicly
- Learn and adjust approach based on feedback

**User Stories:**
- As a Sales Rep, I need to understand the value CRM data entry provides to me personally so that I'm motivated to maintain data quality rather than seeing it as overhead
- As Matt (Executive Sponsor), I need to set clear expectations and hold people accountable for CRM usage so that we achieve the business benefits we're implementing NetSuite to gain
- As a NetSuite Champion, I need good training materials and support so that I can help my peers adopt the new system successfully

**BRD Requirements:**
- [REQUIREMENT] Role-specific training program (Functional)
- [REQUIREMENT] Quick wins identification and communication plan (Non-Functional)
- [ASSUMPTION] Matt will provide executive sponsorship and enforce accountability
- [CONSTRAINT] Sales team resistance expected - plan for mitigation
- [RISK] If sales team doesn't adopt CRM practices, implementation will fail to achieve benefits
- [PRIORITY] Must-Have (change management as critical as technical implementation)

**Stakeholder Impact:**
- **Primary Users**: All sales/BD reps (most impacted by process changes)
- **Approvers/Sponsors**: Matt, GMs (set expectations and accountability)
- **Support**: CRM Administrator, NetSuite Champions (help with adoption)
- **Trainers**: Implementation team (deliver role-specific training)

**Evidence:**
- Change Management Considerations section lines 924-987 in Master_Transcript_Marketing_CRM.md
- "Matt's philosophy: Sales will be our biggest pushback" - Change resistance expectation
- Behavior Changes Required section lines 996-1021 in Master_Transcript_CRM.md
- Resistance Points section lines 1023-1048
- Success Factors section lines 1050-1087

**Confidence Rating**: 94% - Multiple direct quotes and detailed analysis; Matt identified as executive sponsor

---

### 7. INTEGRATION WITH OTHER PROCESSES

**7.1. How does CRM integrate with other business processes?**

**Answer:**

**Connection to Marketing:**
- Lead capture from web forms → automatic lead creation in NetSuite
- Lead qualification and routing (Jenny process maintained)
- Contact segmentation shared between CRM and Marketing
- Opportunity visibility for market intelligence and trend tracking
- Campaign source attribution (when email campaigns used)
- Event attendee follow-up (if event management implemented post-go-live)
- **Quote**: "If marketing had more insight into what some of those leads are and could see and track over time the sectors and how the market is changing, then it would be easier for that team to create proactively create content and target it"

**Connection to Order Management:**
- **Seamless flow**: Opportunity → Quote conversion (one-click)
- **Quote → Sales Order conversion** (automatic data transfer)
- Customer data sync (no manual re-entry)
- Project assignment from closed-won opportunities
- Commission tracking (if implemented)
- Performance metrics (forecast vs. actual)
- **All stages visible and linked** - complete audit trail

**Connection to Financial:**
- Revenue forecasting from opportunity pipeline
- Opportunity value aggregation for financial planning
- Commission calculations (if implemented - marked as FUTURE)
- Credit checks (customer credit status visibility)
- Financial approvals (erosion, GP thresholds)
- Payment terms and conditions

**Connection to Operations:**
- **Project kickoff from won opportunities** (seamless handoff)
- Customer contact info flows to project team (no manual lookup)
- Resource planning from pipeline visibility (know what's coming)
- Capacity planning (projected volume from RFPs)
- Hand-off workflow (sales → operations transition)
- Continued BD/AM visibility after handoff (customer success monitoring)

**Connection to Business Intelligence:**
- Pipeline reporting (company-wide visibility)
- Forecast accuracy analysis (continuous improvement)
- Win/loss trends (strategic insights)
- Sector performance (where are we winning?)
- Territory performance (SF vs. San Jose vs. Sacramento)
- Conversion metrics (lead → opportunity → customer rates)
- Source attribution (which lead sources convert best?)
- Activity metrics (rep performance)

**User Stories:**
- As an Operations Manager, I need to see the opportunity and quote details when a project kicks off so that I understand the customer's expectations and commitments made during the sale
- As a CFO, I need to see opportunity pipeline data in my financial forecasts so that I can plan resources and set revenue expectations with confidence
- As a Marketing Manager, I need to see which lead sources convert to customers at the highest rate so that I can focus efforts on the most effective channels

**BRD Requirements:**
- [REQUIREMENT] Integrated Opportunity → Quote → SO → Project flow (ID: REQ-001, Type: Functional) [ALIGNS]
- [FUNCTIONALITY] Native NetSuite integration across modules
- [PRIORITY] Must-Have
- [ASSUMPTION] All process areas (Marketing, Order Management, Financial, Operations, BI) will be implemented in NetSuite/Orion for full integration

**Stakeholder Impact:**
- **Impacted Parties**: All departments benefit from integrated CRM
- **Cross-Functional Visibility**: Sales, Marketing, Operations, Finance, Executive teams

**Evidence:**
- Integration with Other Processes section lines 1090-1131 in Master_Transcript_CRM.md
- Connection to Marketing lines 1092-1099
- Connection to Order Management lines 1101-1107
- Connection to Financial lines 1109-1115
- Connection to Operations lines 1117-1122
- Connection to Business Intelligence lines 1124-1131

**Confidence Rating**: 93% - Well-documented integration points across process areas

---

## Outstanding Items Summary

**Configuration Details to Finalize (via Action Items):**
1. **Opportunity Stages & Probability**: Define final stage names, criteria for each stage, and probability percentage by stage (Action Item assigned to Sales Leadership)
2. **Contact Roles Taxonomy**: Finalize complete list of contact roles to be configured (Action Item assigned to Sales/BD Team)
3. **Sector/Market Classifications**: Confirm final list of sectors/verticals (Action Item assigned to All stakeholders)
4. **Lead Sources**: Define complete taxonomy of lead sources for tracking (Action Item assigned to Sales/BD Team)
5. **Win/Loss Reason Codes**: Define final list of win and loss reason codes (Action Item assigned to All stakeholders)
6. **Activity Logging Standards**: Define which activities must be logged vs. optional (Action Item assigned to Sales Leadership)
7. **Minimum Required Fields**: Document minimum fields required for opportunity creation (Action Item assigned to Sales Leadership)
8. **Data Quality Owner**: Identify person/role responsible for ongoing data quality (Action Item assigned to TBD)
9. **Sales Goals Dashboard**: Provide current Excel template for recreation in NetSuite (Action Item assigned to Matt/Kip)
10. **Approval Workflow Flowchart**: Document current approval rules in flowchart format (Action Item assigned to Shannon)

**Areas Requiring More Investigation:**
1. **Territory Overlap**: How to handle opportunities/accounts that span multiple territories (SF, San Jose, Sacramento)
2. **Commission Splits**: Marked as FUTURE - decision deferred on how to handle team-based opportunities with split commissions
3. **Event Management**: Minimal focus during Phase 1; may revisit post-go-live if value identified
4. **Asana Integration**: Unclear if Asana will continue to be used for marketing project execution or if all workflow moves to NetSuite

**No Contradictions Identified** between Master_Transcript_CRM.md and Master_Transcript_Marketing_CRM.md - sources are complementary and consistent.

**Comprehensive Coverage Achieved** across:
- Current state assessment (systems, processes, pain points)
- Lead management requirements
- Opportunity management requirements
- Contact & account management requirements
- Forecasting & pipeline requirements
- Win/loss analysis requirements
- Approval workflows
- Dashboards & reporting
- Marketing integration
- RFP management process
- Data migration approach
- Change management considerations
- Cross-process integrations

**Total Requirements Identified**: 50 requirements (REQ-001 through REQ-050) with proper classification (ALIGNS/ADAPT/ACCOMMODATE/FUTURE), supporting evidence, and stakeholder identification.

---

*End of CRM Questionnaire Responses*


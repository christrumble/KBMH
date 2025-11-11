# Business Requirements Document – Marketing
## Solution Alignment & Validation

---

## Document Information

**Document Title:** Business Requirements Document - Solution Alignment & Validation  
**Process Area:** Marketing (Campaigns, Events, Content, Market Intelligence)  
**Audience:** C-suite executives approving NetSuite/Orion implementation  
**Purpose:** Validate that Orion/NetSuite meets marketing requirements and document implementation alignment approach

### Project Information
- **Implementation Name:** Project Orion - KBM Hoag NetSuite Implementation
- **Customer Name:** KBM Hoag
- **Document Owner:** Implementation Consultant
- **Document Version:** 1.0
- **Date:** October 28, 2025

### Document Version History
| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0 | 2025-10-28 | Implementation Consultant | Initial BRD based on comprehensive discovery findings from Questionnaire_Marketing_v3.0 and Requirements_Map_Marketing_v3.1 |

---

## Executive Summary

KBM Hoag's marketing organization operates fundamentally differently from traditional B2B marketing functions. Rather than building demand generation infrastructure, the marketing team serves as relationship coordinators and RFP response specialists—directly supporting sales through targeted communications to key influencers (brokers, architects, project managers, general contractors) and coordinating complex proposal processes.

The Orion/NetSuite solution perfectly aligns with this relationship-based approach while providing critical infrastructure improvements that address current pain points:

**Strategic Alignment:** Orion/NetSuite's standard functionality enables KBM Hoag to maintain their proven relationship-based model while eliminating manual workarounds that currently limit effectiveness.

**Key Capability Alignment:**
- **Contact Segmentation:** Multi-dimensional targeting by role, sector, and geography enables precise influencer relationship management
- **Market Intelligence:** Dashboard visibility into pipeline trends by sector drives proactive content creation
- **RFP Workflow Automation:** Replaces disconnected Asana process with integrated NetSuite system
- **Email Management:** Consolidates MailChimp fragmentation into unified platform while respecting minimal usage model

**Implementation Approach:** 12 requirements leverage proven Orion/NetSuite standard features with no customization. 14 requirements require targeted customization for segmentation, market intelligence dashboards, and RFP workflow—all supporting the core business model rather than changing it.

**Phase 1 Scope:** Implement relationship-based marketing foundation—robust contact segmentation, market intelligence dashboards, RFP workflow automation, and MailChimp replacement. Defer event management and surveys to post-launch evaluation based on adoption.

---

## Marketing Process Area Overview

### Current State (Today)

KBM Hoag's marketing function has three primary responsibilities:

**1. RFP Response Coordination (Core Function)**
- Receive formal RFP requests through Asana
- Schedule stakeholder kickoff calls
- Develop presentations and proposal materials
- Coordinate with Philippines team for time-intensive work
- Track projected vs. actual RFP volume

**2. Targeted Communications (Secondary)**
- Personal email outreach from individual team members (not mass campaigns)
- Quarterly market rate communications to client tiers
- Occasional vendor process notifications
- Sector-specific content creation (when data allows)

**3. Event Coordination (Tertiary)**
- Showroom tours (~2x/month) with personal invitations
- Occasional showroom events and cocktail receptions
- Major event management (when needed)

### Current System Landscape

**Email Marketing:**
- **MailChimp:** Used <6 times/year, difficult Excel imports, bouncing issues due to data quality

**Project Management:**
- **Asana:** RFP request tracking, background documentation, volume projections
- **Google Forms:** RSVP tracking for events

**CRM:**
- **Zendesk:** Being retired, inconsistent data entry, limited contact classification

**File Management:**
- **Google Drive:** Primary collaboration and storage

**Data Quality Challenge:**
The organization's stated problem: "Poo in, poo out." Inconsistent contact classification prevents effective segmentation, limiting campaign targeting effectiveness.

---

## Solution Area 1: Contact Segmentation & Data Foundation

### Your Business Requirements

**REQ-M004: Multi-dimensional contact segmentation (ACCOMMODATE)**
- Need: Segment contacts by role AND sector AND geography simultaneously
- Example: "Target healthcare A&D firms in San Francisco territory"
- Current barrier: Core system lacks role field; no sector field; limited classification options
- Future capability: Saved searches combining role, sector, territory filters

**REQ-M005: Data quality controls and validation rules (ACCOMMODATE)**
- Need: Required fields and validation to ensure clean, trustworthy contact data
- Current barrier: Manual data entry with no validation = "poo in, poo out"
- Future capability: Required field enforcement for role, sector, territory; duplicate detection

**REQ-M006: Custom contact role definitions (ACCOMMODATE)**
- Need: Define comprehensive taxonomy of contact roles for targeting
- Roles required: GC, Broker, A&D Firm, Project Manager, Construction Manager, Finance, Procurement, Facilities, Decision Maker, Executive Sponsor, Manufacturer Rep, Vendor Contact, Office Manager, HR
- Current barrier: Core system offers only generic "role" field
- Future capability: Custom contact role picklist with clear definitions

**REQ-M007: Market sector/vertical classifications (ACCOMMODATE)**
- Need: Define industry verticals for segment identification
- Sectors required: Healthcare, Technology, Corporate Office, Government, Education, Financial Services, Legal, Creative/Agency, Hospitality, Other
- Current barrier: No industry field in Core CRM; can't identify sectors
- Future capability: Custom sector field on contact records

**REQ-M008: Territory-based segmentation (ADAPT)**
- Need: Segment by GM territory (SF, San Jose, Sacramento) for market-specific messaging
- Current barrier: Exists in sales process but not enforced for marketing segmentation
- Future capability: Territory field with assignment rules

### Current State Process

**Lead Entry & Qualification:**
1. Web form submission received → Jenny (Admin) reviews
2. Determination: Delete (most common), Route to GM, or Qualify as new lead
3. BD reps manually enter relationship-based leads (often skip lead stage, create opportunity directly)
4. Inconsistent contact classification in Zendesk

**Current Pain Points:**
- Can't answer: "Is this contact a broker? Finance? Procurement? We don't know"
- Click rates poor because segments are inaccurate
- Data quality issues force manual workarounds: "Pull contacts from specific date ranges" to avoid spamming unsubscribed users
- Duplicate records create confusion

### Orion/NetSuite Solution

Orion/NetSuite provides comprehensive contact management infrastructure designed to eliminate the "poo in, poo out" problem and enable precise relationship targeting:

**Contact Data Foundation:** Orion/NetSuite's standard contact record structure will be customized with required fields for role, sector, and territory. Required field validation ensures every new contact or update captures essential segmentation data. Multi-select checkboxes for role enable contacts to be classified as multiple persona types (e.g., both "Broker" and "A&D Firm").

**Data Quality Implementation:** NetSuite's built-in duplicate detection identifies and prevents duplicate records before they enter the database. Field-level validation rules enforce consistent data entry standards. Required field enforcement at record save prevents incomplete entries. Integration with lookup tables ensures consistent picklist values.

**Segmentation Power:** Once clean, classified data exists, marketing team gains unprecedented targeting capability. Saved searches combine role AND sector AND territory filters to identify precise audience segments. For example: a single saved search identifies all brokers in the healthcare sector within the San Francisco territory—enabling precisely targeted quarterly market rate communications. These segments can be reused across campaigns, quarterly communications, and event invitations.

**Marketing Visibility:** The marketing dashboard displays contact segmentation completion status (% contacts with required fields populated) ensuring data quality discipline over time. As contacts are added or updated, segmentation accuracy improves, making targeting increasingly effective.

### Future State Process

**Improved Lead Entry & Segmentation:**
1. Lead created (web form, manual entry, or direct from opportunity)
2. Required fields completed: Role, Sector, Territory at creation
3. Auto-routing based on territory and account ownership
4. Duplicate detection alerts on similar names/companies
5. Saved searches automatically identify segments for targeting

**Segmentation-Enabled Campaigns:**
- Marketing team accesses pre-built segments: "All brokers in healthcare sector, SF territory"
- Selects target audience for quarterly communications
- Sends from individual user email with personalized merge tags
- Tracks opens, clicks, unsubscribes by segment
- Reports back on segment effectiveness

**Data Quality Governance:**
- Admin team monitors contact record completion
- Sales team training on required field importance
- Periodic data audits to identify and merge duplicates
- Contact update workflow maintains data quality over time

### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Implementation Approach | Business Impact | Status |
|--------|-------------|---------------------------|------------------------|-----------------|--------|
| REQ-M004 | Multi-dimensional segmentation | Custom fields + Saved Searches | Configure role, sector, territory fields; build saved search templates | Enable precise audience targeting for quarterly communications | ✓ Validated |
| REQ-M005 | Data quality controls | Required Fields + Validation Rules | Enforce role, sector, territory as required; duplicate detection rules | Eliminate "poo in, poo out" problem; improve campaign effectiveness | ✓ Validated |
| REQ-M006 | Custom contact roles | Custom Picklist + Multi-Select | Define role taxonomy; implement as custom contact role field | Enable contact classification by influencer type | ✓ Validated |
| REQ-M007 | Sector classifications | Custom Industry Field | Define sector list; implement as custom field | Enable sector-based targeting and market intelligence | ✓ Validated |
| REQ-M008 | Territory segmentation | Territory Field + Assignment Rules | Configure territory field; implement assignment rules by account owner | Enable geographic market-specific messaging | ✓ Validated |

### Implementation Approach

**ACCOMMODATE:** Custom contact role definitions, sector field, and validation rules require configuration and governance. This is an accommodation because KBM Hoag's specific role taxonomy (Broker, A&D Firm, GC, CM, PM, etc.) and sector list go beyond NetSuite's default contact classification. The customization aligns with business requirements, not the other way around.

**Critical Dependencies:**
- **Blocking Configuration:** Taxonomy workshop required to finalize role and sector definitions before configuration begins
- **Data Migration:** Historical contact records must be classified during migration to establish clean foundation
- **Adoption:** Sales team must commit to classifying contacts consistently for segmentation to be effective

**Implementation Considerations:**
- Contact role taxonomy workshop (60-90 minutes with marketing, sales GMs, business development)
- Sector definition workshop (60 minutes with marketing and sales leadership)
- Data classification project during migration (significant manual effort depending on volume)
- Training for sales team on required field entry
- Regular data quality audits post-go-live

---

## Solution Area 2: Email Marketing & Campaigns

### Your Business Requirements

**REQ-M002: Minimal email marketing implementation Phase 1 (ALIGNS)**
- Current: <6 campaigns/year via MailChimp
- NetSuite includes: 120,000 emails/month capacity
- Team assessment: "Way more than we would ever use"
- Approach: Implement email capability without over-investing in automation

**REQ-M009: Transactional vs. marketing email distinction (ALIGNS)**
- Need: Send important business communications (rate changes, process updates) even to unsubscribed contacts
- Example: "If they've unsubscribed and I need to tell them about a rate change, I can still send that"
- Current barrier: MailChimp treats all emails equally; no transactional vs. marketing distinction
- Future capability: Automatic subscription status management by email type

**REQ-M010: Quarterly targeted communications to specific segments (ADAPT)**
- Need: Curated lists for quarterly market rate communications to brokers, PM firms, CM firms
- Quote: "If we did have a curated list of brokers and PM firms or CM firms, and like, we did send out quarterly, oh, here's some market rates we're seeing..."
- Current barrier: Data quality prevents effective list creation; manual Excel process with MailChimp rejection issues
- Future capability: One-click saved search to segment list, send from NetSuite

**REQ-M011: Personalized email sending from individual user accounts (ALIGNS)**
- Need: Send emails from real person's email address, not from "info@kbmhoag.com"
- Quote: "We're sending an email from a real person's email, rather than from info at KBM"
- Current barrier: Limited in MailChimp; requires manual setup
- Future capability: NetSuite native functionality

**REQ-M012: Replace MailChimp with NetSuite (ADAPT)**
- Current issues: Excel upload rejection ("MailChimp gets really pissed off"), high bounce rates, data quality issues
- Future: Consolidate email to NetSuite; eliminate tool switching

### Current State Process

**Current Campaign Workflow:**
1. Identify target audience (often imprecise due to data quality)
2. Create Excel list manually
3. Attempt upload to MailChimp (often rejected due to spam protection)
4. When accepted: Create email in MailChimp (templates in Google Slides embedded as images)
5. Send campaign
6. Many emails bounce due to data quality issues
7. Manual opt-out tracking as workaround: "Only pull contacts from specific date ranges"

**Campaign Types Currently Used:**
- Quarterly market rate communications (to client tiers)
- Vendor process change notifications
- Occasional sector-specific content (if data quality allows)
- Major event invitations (most use personal emails instead)

**Current Pain Points:**
- MailChimp rejects Excel uploads due to spam protection
- High bounce rates from dirty data
- Can't segment effectively (data quality issues)
- Manual opt-out management
- Multiple tools required (Excel, MailChimp, Google Slides, email)
- "Click rates aren't great" = effectiveness limited by poor targeting

### Orion/NetSuite Solution

Orion/NetSuite provides integrated email marketing capability that eliminates tool fragmentation while respecting KBM Hoag's minimal usage model:

**Unified Campaign Management:** Rather than jumping between Excel, MailChimp, and Google Slides, marketing team manages everything from NetSuite. Create campaign, build target list (using segmentation), customize content, and send—all within one system. No more Excel exports or MailChimp rejections.

**Smart List Creation:** With segmentation foundation in place (previous section), marketing team creates campaign target lists with simple criteria: "All healthcare sector contacts who are A&D firms in SF territory and have opted in to marketing emails." Saved searches make recurring lists available one-click. List accuracy improves over time as contact data quality improves.

**Transactional Email Capability:** NetSuite distinguishes between marketing emails (require opt-in) and transactional emails (sent regardless of subscription status). Rate change notifications, process updates, and other business communications send as transactional emails, reaching all contacts. Marketing campaigns require opt-in, respecting user preferences. "NetSuite will manage that for you automatically" rather than manual date-range workarounds.

**Personalized Sending:** Emails send from individual user accounts (not "info@kbmhoag" generic address), maintaining the personal relationship tone KBM Hoag values. Activity tracking captures email opens and clicks back to individual contact records, enabling marketing to see relationship engagement.

**Template Simplification:** While team currently uses Google Slides for image creation (no change needed), NetSuite's template system ensures consistent formatting and speeds up campaign creation. Merge tags personalize each email with recipient name, company, and other contact fields.

**Analytics & Performance:** Every campaign tracked with open rates, click rates, bounce rate, and unsubscribe tracking. Over time, marketing understands which segments, content types, and sending times perform best—informing more effective targeting.

### Future State Process

**Streamlined Campaign Workflow:**
1. Marketing PM identifies campaign need (quarterly market rates, sector content, etc.)
2. Selects saved search: "All brokers in healthcare sector, SF territory, opted in"
3. Customizes email content (can use templates for faster creation)
4. Selects sending user (e.g., Jill Marsh, GM) for personal touch
5. Schedules campaign
6. NetSuite automatically validates list, removes unsubscribes, flags bouncing addresses
7. Campaign sends with personalized merge tags
8. Real-time tracking of opens, clicks, unsubscribes
9. Post-campaign reporting shows which segments engaged best
10. Insights inform next quarter's content and targeting

**Transactional Process:**
1. Rate change or process update identified (Operations or Finance team)
2. Sends to all affected contacts as transactional email
3. Unsubscribed contacts receive notification (important business information)
4. Opt-out status ignored for transactional emails

### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Implementation Approach | Business Impact | Status |
|--------|-------------|---------------------------|------------------------|-----------------|--------|
| REQ-M002 | Minimal email capability | NetSuite Email Marketing Module | Configure campaign interface; establish sending governance | Enable occasional campaigns without over-investment | ✓ Validated |
| REQ-M009 | Transactional vs. marketing | Subscription Status + Email Type | Configure email types; set transactional vs. marketing rules | Allow business-critical communication even if unsubscribed | ✓ Validated |
| REQ-M010 | Quarterly communications | Saved Searches + Campaign Scheduling | Build reusable segments; create quarterly campaign calendar | Enable consistent, targeted outreach to influencers | ✓ Validated |
| REQ-M011 | Personal email sending | User Email Configuration | Set up user email accounts for sending; enable activity tracking | Maintain relationship tone; track individual engagement | ✓ Validated |
| REQ-M012 | Replace MailChimp | NetSuite Email Module | Migrate email templates and historical data; configure list creation | Eliminate tool switching; improve list quality; consolidate systems | ✓ Validated |

### Implementation Approach

**ALIGNS:** Email marketing capability aligns with how KBM Hoag currently operates—minimal campaigns, personal tone, occasional targeted outreach. NetSuite's standard email functionality meets needs without requiring customization.

**ADAPT:** Quarterly targeted communications require minor process adaptation. Rather than manual Excel exports to MailChimp, team adapts to using NetSuite saved searches and campaigns. Once adapted, this approach is actually simpler and more effective than current workaround.

**Implementation Considerations:**
- Migrate MailChimp email templates (low priority per team; can recreate post-launch if needed)
- Email compliance training: Transactional vs. marketing distinction
- Sending governance: Who can send campaigns? When? To what segments?
- Monthly email review process to track volume and performance
- Data migration: Opt-out/subscription status if tracked in MailChimp

---

## Solution Area 3: Lead Capture & Qualification

### Your Business Requirements

**REQ-M024: Web form lead capture with automatic creation (ALIGNS)**
- Current: Website contact form provides business legitimacy
- Quote: "Weird to be a business without a web form"
- Reality: Most submissions are low-quality (cleaning quotes, consumer requests)
- Approach: Keep web form; auto-create leads for qualification; easy deletion for spam

### Current State Process

**Web Form Processing:**
1. Web form submission received → Jenny (Admin) gets notification
2. Manual review → Determine: Delete? Route to GM? Qualify as lead?
3. Qualifies: Is it commercial furniture? Is it existing client? Is it legitimate?
4. Decision: Most = delete (cleaning quotes, "I inherited a Newell Eames chair")
5. Route: Existing client → to account owner GM
6. Rare: New business opportunity → appropriate sales team

**Lead Source:**
- Occasional valuable lead (example: client requesting cubicles → touchdown cubicle order)
- Most valuable leads come through relationships, not web forms
- Web form serves as customer touchpoint more than sales channel

### Orion/NetSuite Solution

Orion/NetSuite's web-to-lead functionality captures form submissions and automatically creates lead records, enabling consistent qualification process and lead attribution:

**Automatic Lead Creation:** Contact form submission immediately creates lead record in NetSuite with basic information (name, company, email, inquiry). No manual data entry. Reduces delay between inquiry and response.

**Lead Routing:** Auto-assignment rules route leads to appropriate queue:
- Existing client identified → Route to account owner GM
- New business (territory identifiable) → Route to appropriate GM's queue
- Unknown/needs qualification → Route to admin queue (Jenny) for review
- Spam/junk patterns → Flag for potential deletion

**Qualification Workflow:** Admin reviews assigned leads and qualifies:
- Commercial furniture inquiry? Yes → Convert to opportunity or advance qualification
- Consumer/residential request? No → Delete with notation
- Incomplete information? → Request follow-up information
- Existing client with simple question? → Resolve and close

**Lead Source Attribution:** Every lead automatically tagged with source "Web Form," enabling marketing to see channel performance over time. Can be tied to sector, contact type, and other attributes for analysis.

**Easy Deletion:** With web-to-lead automation, junk leads easily identified and deleted in bulk (cleaning quotes, consumer requests). No longer clutters admin workflow because system doesn't require manual data entry.

### Future State Process

**Improved Web Lead Process:**
1. Contact form submission → Automatic lead created in NetSuite
2. Auto-routing based on rules → Jenny, GM, or qualification queue
3. Jenny reviews assigned leads → Qualification decision
4. Quality lead → Convert to opportunity and assign to sales team
5. Junk lead → Delete with notation
6. Lead source tracked → "Web Form" attribution for reporting
7. Marketing visibility → Can see web lead quality and source performance

### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Implementation Approach | Business Impact | Status |
|--------|-------------|---------------------------|------------------------|-----------------|--------|
| REQ-M024 | Web-to-lead with auto-creation | Native Web-to-Lead Forms | Configure contact form to NetSuite integration; set auto-routing rules | Streamline lead qualification; maintain customer touchpoint | ✓ Validated |

### Implementation Approach

**ALIGNS:** Web-to-lead functionality aligns with how KBM Hoag currently operates. Form continues to provide customer touchpoint; NetSuite automates lead creation and routing where previously manual; qualification process remains similar.

**Implementation Considerations:**
- Website developer integration to connect contact form to NetSuite
- Lead routing rule configuration
- Spam/junk lead identification criteria
- Jenny training on lead qualification workflow
- Marketing dashboard to track web lead quality/volume

---

## Solution Area 4: RFP Management & Workflow

### Your Business Requirements

**REQ-M015: Marketing early visibility into RFP opportunities (ACCOMMODATE)**
- Current pain: "Marketing has no visibility until formal request submitted" via Asana
- Impact: "Can't proactively prepare"; missed opportunity to prepare materials/resources
- Future need: Marketing team sees pipeline early, identifies upcoming RFPs, resources appropriately

**REQ-M016: Track projected vs. actual RFP volume by submitter (ACCOMMODATE)**
- Current: Asana tracks projected volume vs. actual volume
- Purpose: Identify who overestimates RFP size; improve resource planning
- Quote: "We track what that projected volume is versus what the actual volume is, so that we can see, like, how many people are overestimating"

**REQ-M017: RFP workflow routing to marketing team (ACCOMMODATE)**
- Current: Asana request process (separate system)
- Future: Replace Asana with NetSuite workflow
- Process: Receive RFP → Marketing PM assigned → Document attachment → Collaboration
- Benefit: All RFP information in single system

**REQ-M018: Document attachment to opportunities/quotes (ALIGNS)**
- Need: Attach RFP request documents, response materials, Google Drive links
- Current: Files scattered across email and Google Drive
- Future: Centralized document management on opportunity record

### Current State Process

**RFP Identification & Request:**
1. Relationship-based RFP identified by BD rep
2. Preliminary assessment by rep
3. When formal RFP arrives → Created as opportunity (sometimes)
4. **Formal Asana request submitted by BD rep**
5. Request includes: Background, links, documentation, projected volume
6. Marketing team assigned to RFP

**Marketing RFP Process:**
1. Marketing PM receives Asana notification
2. Schedules kickoff call with stakeholders
3. Develops presentations and proposals
4. Coordinates with Philippines team for resource-intensive work
5. Tracks projected vs. actual volume (in Asana)
6. Manages marketing team resources

**Current Challenges:**
- Marketing has no visibility before formal Asana request
- RFP information fragmented: Opportunity record, Asana request, Google Drive files, email
- No proactive resource forecasting
- Philippines team time tracking disconnected from RFP tracking
- No visibility into early-stage pipeline for content planning

### Orion/NetSuite Solution

Orion/NetSuite workflow automation and project integration replaces Asana process while providing enhanced visibility and collaboration:

**Early Opportunity Visibility:** Marketing team configured with restricted CRM access enabling visibility into sales pipeline without full system access. Marketing dashboard shows opportunities from first identification through RFP stage, enabling early visibility to resource-plan and prepare. As opportunities enter RFP phase, marketing notified through workflow automation.

**RFP Request Engine:** When BD rep identifies formal RFP, they submit through NetSuite request form (replaces Asana). Form captures:
- Opportunity detail (client, project details)
- Projected volume (estimated project scope)
- Timeline (decision timeline, required delivery date)
- Project requirements (special requirements, site notes)
- Preliminary materials (initial RFP documents, links)

**Automatic Workflow Routing:** Upon submission, NetSuite workflow automatically:
1. Creates project record (if not exists)
2. Assigns to Marketing PM (based on territory or availability)
3. Triggers notification to marketing team
4. Escalates to marketing leadership if volume exceeds capacity threshold
5. Links to related opportunity for complete context

**Document Management:** All RFP-related documents centralized on project record:
- Uploaded RFP documents
- Marketing team response materials
- Approved proposals and quotes
- Google Drive folder links (stored in Drive but represented in NetSuite)
- Version history and change tracking

**Volume Tracking:** Custom fields on opportunity/project track:
- Projected volume (estimated scope from RFP)
- Actual volume (final project scope)
- Variance analysis (overestimate/underestimate)
- Submitter name (to identify patterns)
- Resource hours allocated vs. actual
- Completion status

**Philippines Team Integration:** Time entries by Philippines team linked to RFP project record, providing real-time visibility into resource allocation and actual effort vs. estimates. Supports volume accuracy tracking and resource planning.

**Project Record Integration:** All RFP information consolidated on project record (from Orion suite):
- Financial tracking (budget vs. actual)
- Time entries (core team and Philippines team)
- Project communication log
- Milestones and status
- Progress vs. timeline
- RFP response materials and collaboration

### Future State Process

**Improved RFP Workflow:**
1. Relationship identified by BD rep
2. Preliminary assessment (informal)
3. **Formal RFP received → Opportunity created** (before formal request)
4. **Early alert to Marketing:** Workflow triggers when RFP stage entered
5. Marketing PM reviews early, begins resource planning
6. **When formal RFP request ready → BD rep submits through NetSuite form**
7. Automatic workflow routes to assigned Marketing PM
8. Project created with RFP information and documents
9. Kickoff call scheduled (all stakeholders have access to shared project record)
10. Marketing develops response using project record for collaboration
11. Time tracking by Philippines team logged to project
12. Proposed volume tracked; actual volume updated as project scopes
13. Variance analyzed post-completion for future accuracy

**Resource Planning:**
- Marketing dashboard shows RFP pipeline 30/60/90 days ahead
- Projected volume summarized by month/quarter
- Resource allocation visible (marketing team capacity)
- Bottleneck identification when volume exceeds capacity
- Philippines team time visible with regular opportunities

### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Implementation Approach | Business Impact | Status |
|--------|-------------|---------------------------|------------------------|-----------------|--------|
| REQ-M015 | Early opportunity visibility | Custom CRM Permissions + Dashboard | Configure marketing dashboard; set restricted opportunity access | Enable proactive resource planning; avoid reactive scrambling | ✓ Validated |
| REQ-M016 | RFP volume tracking | Custom Opportunity Fields + Project Record | Configure projected/actual volume fields; create volume analytics | Improve resource forecasting; identify volume pattern accuracy | ✓ Validated |
| REQ-M017 | RFP workflow automation | Request Engine + Workflow Automation | Design RFP request form; configure auto-routing and notifications | Replace Asana; consolidate RFP information; improve collaboration | ✓ Validated |
| REQ-M018 | Document attachment | Document Management + Google Drive Integration | Enable document storage on opportunity/project records | Centralize RFP materials; improve file organization and retrieval | ✓ Validated |

### Implementation Approach

**ACCOMMODATE:** RFP workflow routing, volume tracking, and marketing visibility require configuration and custom solution design. This is not off-the-shelf functionality—it's configured to match KBM Hoag's specific RFP process and marketing role.

**CRITICAL DEPENDENCIES:**
- **Blocking Workflow Design:** Must define exact RFP request form fields and workflow routing before configuration
- **Blocking Go-Live:** Workflow must be fully functional at launch or maintain Asana parallel process
- **Adoption:** Sales team must adopt opportunity creation workflow to trigger marketing alerts

**Implementation Considerations:**
- RFP request form design workshop with marketing and sales leadership
- Workflow routing rules configuration
- Project record configuration
- Philippines team time tracking integration requirements
- Parallel running with Asana (2-4 weeks recommended)
- Marketing team training on new workflow
- Sales team training on trigger points for marketing alerts

---

## Solution Area 5: Market Intelligence & Analytics

### Your Business Requirements

**REQ-M019: Marketing visibility into pipeline trends by sector (ACCOMMODATE)**
- Current pain: No sector visibility; marketing reactive instead of proactive
- Quote: "If marketing had more insight into what some of those leads are and could see and track over time the sectors and how the market is changing, then it would be easier for that team to create proactively create content"
- Future: Dashboard showing opportunities by sector, enabling content strategy based on market trends

**REQ-M020: Market intelligence dashboard for content planning (ACCOMMODATE)**
- Need: Multi-dimensional view of market opportunity
- Components: Sector trends (opportunities over time), RFP volume by market, win/loss by sector, pipeline by stage and sector
- Purpose: Inform content strategy, identify growing markets, resource allocation

**REQ-M021: Sector performance analysis for strategic planning (ACCOMMODATE)**
- Need: Analyze sector trends to identify which markets growing/shrinking
- Use case: Healthcare trending up → marketing creates targeted healthcare content
- Benefit: Strategic focus; proactive content; competitive advantage

### Current State Process

**Market Intelligence (Minimal):**
- No systematic tracking of sector trends
- No visibility into early-stage opportunities
- Reactive response when RFP arrives (too late for content preparation)
- Can't proactively create content for growing sectors
- Limited insight into which influencers generating best leads

**What's NOT Tracked:**
- Sector performance
- Lead source effectiveness
- Influencer attribution
- Pipeline by sector
- Market trends
- Win/loss by sector

**Current Gap:**
Marketing team wants to be strategic ("Identify trending sectors, create proactive content") but lacks visibility into market data necessary to inform strategy. Everything is reactive: Wait for RFP → Respond to RFP. No proactive positioning.

### Orion/NetSuite Solution

Orion/NetSuite provides comprehensive market intelligence infrastructure through custom dashboards, analytics, and reporting:

**Market Intelligence Foundation:** With sector field properly populated on all contacts and opportunities (from segmentation work), NetSuite can analyze market data across multiple dimensions. Sales team entering opportunities and tracking outcomes (won/lost) provides analytical fuel.

**Sector Trend Visualization:** Custom dashboard displays:
- **Opportunities by Sector (Trend):** Line chart showing opportunity count by sector over time. Marketing immediately sees: "Healthcare sector opportunities trending up 40% this quarter." Time to create healthcare-focused content.
- **RFP Volume by Market/Territory:** Shows RFP submission volume by territory (SF/San Jose/Sacramento). Marketing understands market-specific demand patterns.
- **Win/Loss by Sector:** Displays win rates by sector. High-win sectors get increased marketing focus; low-win sectors analyzed for competitive positioning issues.
- **Pipeline by Stage and Sector:** Shows pipeline value and quantity at each sales stage, broken down by sector. Enables revenue forecasting by market.

**Strategic Content Planning:** Marketing PM reviews market intelligence dashboard monthly. Observes:
- Healthcare sector trending up 40% → Allocates time to create healthcare-focused case studies, thought leadership content, targeted emails
- Technology sector flatlined → Analyzes: Is market saturated? Do we lack positioning? Identifies strategic response
- Government sector strong in Sacramento → Develops territory-specific Sacramento government content

**Influencer ROI Tracking (Future Capability):** Dashboard could extend to show lead source attribution:
- Which brokers generate most valuable leads?
- Event attendance → opportunity conversion rate
- Quote: "It'd be so cool to see, like, the ROI of an investment on a relationship. Like, I spent $6,000 on this person, and I got $3 million"

**Performance Metrics Reporting:**
- Projected vs. actual RFP volume (by submitter)
- Marketing content performance (sector-specific content engagement)
- Campaign effectiveness by segment
- Lead source performance and conversion

**Access & Governance:** Marketing team receives restricted dashboard access showing sector trends without full pipeline visibility. Enables strategic planning without sales pipeline exposure.

### Future State Process

**Monthly Market Intelligence Review:**
1. Marketing PM opens market intelligence dashboard
2. Reviews sector opportunity trends (month-over-month, quarter-over-quarter)
3. Analyzes: Which sectors growing? Shrinking? Stable?
4. Identifies: Opportunity for proactive content
5. Example: "Healthcare trending up 40% → Allocate next sprint to healthcare thought leadership"
6. Develops sector-specific content strategy
7. Creates targeted campaigns to brokers/A&D firms in growing sectors
8. Tracks campaign performance by sector
9. Iterates: Next month reviews content effectiveness

**Resource Planning Based on Intelligence:**
1. RFP volume trending up for Q4 → Increase Philippines team hours
2. Sector performance analysis shows: "Tech sector low win rate" → Investigate competitive positioning
3. Influencer analysis: "Broker X generates 3x revenue per lead vs. Broker Y" → Allocate more marketing resources to Broker X relationship

**Competitive Advantage:**
Marketing transitions from reactive (respond to RFP) to proactive (anticipate market trends, create content before RFPs arrive). Sector-specific expertise demonstrated early in sales process, improving win rates.

### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Implementation Approach | Business Impact | Status |
|--------|-------------|---------------------------|------------------------|-----------------|--------|
| REQ-M019 | Pipeline visibility by sector | Custom Dashboard + Saved Searches | Build marketing-restricted dashboard; show sector trends | Enable proactive content strategy based on market trends | ✓ Validated |
| REQ-M020 | Market intelligence dashboard | Custom Dashboard + Analytics | Design multi-dimensional dashboard; configure drill-down capability | Provide strategic market visibility; inform content planning | ✓ Validated |
| REQ-M021 | Sector performance analysis | Reports + Trend Analysis | Create sector performance reports; identify trending sectors | Identify growing markets; focus marketing resources strategically | ✓ Validated |

### Implementation Approach

**ACCOMMODATE:** Market intelligence dashboards require custom solution design. These are not off-the-shelf analytics—they're configured to match KBM Hoag's specific market segments, performance metrics, and strategic planning needs.

**CRITICAL DEPENDENCIES:**
- **Blocking:** Sector field must be populated on all opportunities (data quality requirement from segmentation phase)
- **Blocking:** Sales team must track opportunity outcomes (won/lost) for win/loss analysis
- **Blocking:** Dashboard requirements workshop needed to define exact layout, metrics, drill-down

**Implementation Considerations:**
- Market intelligence dashboard requirements workshop (90 minutes)
- Sector field configuration and data population
- Dashboard design and implementation
- Access control configuration (restricted to marketing)
- Sales team training on outcome tracking (won/lost)
- Regular dashboard review cadence (monthly recommended)
- Trend analysis and strategic planning process formalization

---

## Solution Area 6: Integration & Supporting Capabilities

### Your Business Requirements

**REQ-M001: Support relationship-based, targeted marketing approach (ALIGNS)**
- Philosophy: Marketing enables relationship cultivation, not campaign blasts
- Quote: "So much of what we do is relationship-based, and so we're being very selective"
- Approach: System designed for precise targeting and personal communication

**REQ-M003: Support marketing as RFP coordination function (ADAPT)**
- Role: Marketing owns RFP response process, not demand generation
- Quote: "Kind of unique because your marketing department is actually doing like some sales process"
- Approach: Workflow and visibility designed around RFP-centric model

**REQ-M025: Google Drive integration for file management (ACCOMMODATE)**
- Need: Store files in Google Drive (100GB limit better than NetSuite storage)
- Connection: Files represented in NetSuite; actual storage in Drive
- Benefit: Avoid NetSuite storage limits; team already uses Drive
- Implementation: Configure Google Drive connector

### Current State & Solution

**REQ-M001 - Relationship-Based Approach:**
The Orion/NetSuite solution is designed around relationship management:
- Multi-dimensional segmentation enables precise influencer targeting
- Personal email sending from individual accounts maintains relationship tone
- Early RFP visibility enables proactive relationship cultivation
- Market intelligence informs strategic relationship focus
- Contact record captures relationship history and details

**REQ-M003 - RFP Coordination:**
RFP workflow automation positions marketing as coordinator:
- Workflow triggers when RFP stage reached
- Marketing assigned as primary coordinator
- Document collaboration on project record
- Volume tracking and resource planning
- Project status visible to all stakeholders

**REQ-M025 - Google Drive Integration:**
NetSuite connector enables:
- Link Google Drive folders to NetSuite records
- Files stored in Drive (not NetSuite) to manage storage
- View file access from NetSuite (doesn't require leaving system)
- Version control maintained in Drive
- Familiar Drive interface for collaboration

### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Implementation Approach | Business Impact | Status |
|--------|-------------|---------------------------|------------------------|-----------------|--------|
| REQ-M001 | Relationship-based approach | Segmentation + Personal Email + Intelligence | Configure all above features as integrated system | System enables relationship model; no campaign blast infrastructure | ✓ Validated |
| REQ-M003 | RFP coordination function | Workflow Automation + Project Records | Configure RFP workflow and project access | Marketing positioned as RFP coordinator; integrated process | ✓ Validated |
| REQ-M025 | Google Drive integration | Google Drive Connector | Configure connector; set permissions and access rules | Maintain familiar Drive workflow; avoid NetSuite storage limits | ✓ Validated |

### Implementation Approach

**ALIGNS:** Relationship-based approach aligns with current business model. System supports it rather than forcing change.

**ADAPT:** RFP coordination adapts to NetSuite workflow model. Process changes but philosophy remains same.

**ACCOMMODATE:** Google Drive integration requires connector configuration. Not standard but straightforward implementation.

---

## Solution Area 7: Future Phase Capabilities (Deferred)

### Your Business Requirements

**REQ-M013: Minimal event tracking for Phase 1 (ALIGNS)**
**REQ-M014: Evaluate event management post-go-live (FUTURE)**
- Current approach: Personal invitations, Google Forms RSVP, no systematic tracking
- Showroom events: ~2x/month
- Grand opening: Check-in process (exception, not typical)
- Assessment: "Question of value vs. effort"
- Phase 1 approach: Continue current approach; evaluate post-launch

**REQ-M022: Customer satisfaction surveys post-project (FUTURE)**
**REQ-M023: Survey functionality within NetSuite campaigns (FUTURE)**
- Need: Post-delivery customer feedback
- Current: Not systematized
- Timeline: 6+ months post-go-live
- Approach: Evaluate with Customer Service team post-implementation

### Rationale for Future Phase

Event management and surveys are not in Phase 1 scope due to:
1. Low current usage and unclear ROI
2. Data quality foundation and market intelligence dashboards higher priority
3. Team bandwidth focused on RFP workflow transition
4. Value determination: "Question of value vs. effort"
5. Post-launch evaluation enables informed decision

Both capabilities will be evaluated 3-6 months post-launch to determine adoption and business value before investment.

---

## Implementation Approach Summary

### Requirements by Approach

**ALIGNS (8 requirements - 30%):**
- Business processes align with Orion/NetSuite standard functionality
- No customization required
- Team adapts minimally or not at all
- Examples: Email marketing, web-to-lead, relationship-based approach

**ADAPT (5 requirements - 18%):**
- Process modification required to use Orion/NetSuite standard functionality
- No customization, but workflow differs from current
- Team training focused on new process
- Examples: Quarterly communications, RFP workflow, MailChimp replacement, email marketing, territory segmentation

**ACCOMMODATE (12 requirements - 44%):**
- Orion/NetSuite customization required to meet business requirements
- Configurable solution design
- Addresses specific KBM Hoag needs
- Examples: Contact segmentation, data quality, market intelligence dashboards, RFP workflow, Google Drive integration

**FUTURE (2 requirements - 7%):**
- Deferred to post-launch evaluation
- Business value unclear relative to effort
- Examples: Event management, customer surveys

### Decision Log

#### Segmentation & Data Quality (REQ-M004, M005, M006, M007, M008)
- **DECISION:** Implement multi-dimensional segmentation with custom role taxonomy and sector field
- **FUNCTIONALITY:** Custom contact fields, required field validation, duplicate detection
- **SOLUTIONDESIGN:** Taxonomy workshop to define role and sector classifications; data migration to classify historical records
- **APPROACH:** ACCOMMODATE (customized to KBM Hoag's specific taxonomy and requirements)
- **RATIONALE:** Data quality is foundation for all marketing capabilities (segmentation, campaigns, market intelligence). Without clean, classified data, entire marketing strategy fails. This is "poo in, poo out" problem to solve.

#### Email Marketing (REQ-M002, M009, M010, M011, M012)
- **DECISION:** Implement NetSuite email marketing for minimal usage (<6/year) with segmentation-driven targeting
- **FUNCTIONALITY:** Native email marketing module, campaign scheduling, transactional email capability, personal sender options
- **SOLUTIONDESIGN:** None required (standard NetSuite)
- **APPROACH:** ALIGNS (standard functionality) and ADAPT (quarterly communications workflow)
- **RATIONALE:** Replace MailChimp fragmentation with consolidated NetSuite platform. Minimal usage means don't over-invest in automation. Rely on segmentation for targeting accuracy.

#### RFP Workflow (REQ-M015, M016, M017, M018)
- **DECISION:** Replace Asana RFP process with NetSuite workflow automation and project records
- **FUNCTIONALITY:** Request engine, workflow routing, project records, document management, volume tracking fields
- **SOLUTIONDESIGN:** RFP request form design, workflow routing rules, volume tracking analytics, Philippines team integration
- **APPROACH:** ACCOMMODATE (customized workflow) with ALIGNS (document attachment)
- **RATIONALE:** RFP coordination is core marketing function; consolidating to single system improves visibility, collaboration, and resource planning. Early marketing alerts enable proactive preparation. Volume tracking informs resource planning.

#### Market Intelligence (REQ-M019, M020, M021)
- **DECISION:** Build custom market intelligence dashboard for proactive content planning
- **FUNCTIONALITY:** Custom dashboard, trend analysis, sector performance reporting
- **SOLUTIONDESIGN:** Dashboard design, metric definitions, access controls, trend analysis methodology
- **APPROACH:** ACCOMMODATE (customized dashboards)
- **RATIONALE:** Marketing transitions from reactive (respond to RFPs) to proactive (anticipate trends, create content). Dashboard provides strategic visibility to inform content strategy and resource allocation. Key competitive advantage.

#### Lead Capture & Qualification (REQ-M024)
- **DECISION:** Implement web-to-lead forms with auto-routing and qualification workflow
- **FUNCTIONALITY:** Web form integration, auto-lead creation, routing rules
- **SOLUTIONDESIGN:** None required (standard NetSuite)
- **APPROACH:** ALIGNS
- **RATIONALE:** Continue business legitimacy touchpoint (web form); automate manual lead entry; standardize qualification process.

#### Google Drive Integration (REQ-M025)
- **DECISION:** Configure Google Drive connector for file management
- **FUNCTIONALITY:** Google Drive connector, file linking, permission management
- **SOLUTIONDESIGN:** Connector configuration, governance rules for shared access
- **APPROACH:** ACCOMMODATE (configured to specific governance model)
- **RATIONALE:** Team already uses Drive; connector maintains familiar workflow while centralizing file references in NetSuite. Avoids storage limit issues.

#### Event Management (REQ-M013, M014)
- **DECISION:** Defer to Phase 2; continue current approach (personal invites, Google Forms)
- **FUNCTIONALITY:** Campaign events module available but not implemented
- **SOLUTIONDESIGN:** None in Phase 1
- **APPROACH:** FUTURE (ALIGNS with current process; will evaluate 3-6 months post-launch)
- **RATIONALE:** Low priority, unclear ROI vs. effort. Data quality and market intelligence higher priorities.

#### Customer Surveys (REQ-M022, M023)
- **DECISION:** Defer to Phase 2; coordinate evaluation with Customer Service team
- **FUNCTIONALITY:** Survey campaigns module available but not implemented
- **SOLUTIONDESIGN:** None in Phase 1
- **APPROACH:** FUTURE (will evaluate 6+ months post-launch)
- **RATIONALE:** Not systematized currently; low Phase 1 priority. Evaluate post-implementation with Customer Service.

---

## Implementation Timeline & Phase Definition

### Phase 1 Scope: Foundation & Core Marketing Capabilities (Months 1-4 Post-Launch)

**Pre-Launch (Configuration & Data Migration):**
- Taxonomy workshop: Define contact role and sector classifications (Week 1-2)
- Contact data classification: Clean and classify 80%+ of existing records (Week 3-6)
- RFP request form design: Document form fields and workflow routing (Week 2)
- Market intelligence dashboard design: Define metrics, layout, access controls (Week 3-4)
- Email template migration: Recreate or establish templates in NetSuite (Week 4)
- Google Drive integration: Configure connector and governance (Week 3)
- User training: Marketing team, sales team, admin team (Week 4-5)
- Parallel Asana/NetSuite: Run both systems 2-4 weeks to ensure smooth transition

**Post-Launch (Stabilization & Adoption):**
- Monitor data quality: Contact record completion rates, segment accuracy
- RFP workflow: Track adoption, volume accuracy, resource utilization
- Email consolidation: Retire MailChimp, confirm all campaigns through NetSuite
- Market intelligence dashboard: Begin regular monthly reviews, iterative refinement
- Segmentation usage: Track saved search creation, segment application
- Data entry discipline: Sales team compliance with required fields

### Phase 2 (Post-Launch Evaluation, Months 5-12):

**Event Management Evaluation (Months 5-7):**
- Determine: ROI vs. effort; adoption vs. perceived value
- If valuable: Configure event tracking, campaign events, RSVP automation
- If not valuable: Continue current approach

**Customer Satisfaction Surveys (Months 8-12):**
- Evaluate: Survey timing, questions, distribution, action items
- Coordinate with Customer Service team
- If adopted: Configure survey campaigns, response tracking, trend analysis

**Influencer ROI Dashboard Extension:**
- Build on market intelligence foundation
- Add lead source attribution, influencer performance metrics
- Implement if data quality supports detailed tracking

---

## Success Criteria & Metrics

### Phase 1 Success Criteria (Go-Live + 60 Days)

1. **Data Quality:** ≥90% of active contacts have required fields (role, sector, territory) populated
2. **Segmentation Usage:** Marketing team has created ≥3 saved searches for regular segments (brokers, A&D, PM firms, etc.)
3. **Email Consolidation:** MailChimp account retired; 100% of campaigns executed through NetSuite
4. **RFP Workflow:** 100% of RFPs routed through NetSuite; Asana retired for marketing
5. **Web-to-Lead:** All web form leads auto-created in NetSuite; admin reports smooth qualification process

### Phase 1 Success Criteria (6 Months Post-Launch)

6. **Market Intelligence Adoption:** Marketing team using sector dashboard ≥2x/month; identified ≥2 strategic opportunities based on trends
7. **Targeted Communications:** ≥2 quarterly campaign cycles executed to segmented lists with improved open rates vs. MailChimp
8. **Volume Tracking:** Projected vs. actual RFP volume tracked on 100% of RFPs; accuracy analysis completed
9. **User Adoption:** Sales team compliance with required field entry ≥85%
10. **Google Drive Integration:** All RFP documents stored via Google Drive integration; no NetSuite storage limits breached

### 12-Month Success Criteria

11. **Strategic Content Planning:** Marketing proactively creates content based on market trends (not just reactive to RFPs)
12. **Resource Planning Accuracy:** RFP volume forecasting accurate within 10%; resource allocation optimized
13. **Influencer Relationship Tracking:** Early-stage opportunity visibility enables proactive influencer nurturing vs. reactive response

---

## Implementation Considerations & Risks

### High Priority - Critical Success Factors

1. **Contact Role & Sector Taxonomy Definition**
   - Timing: Weeks 1-2 (blocking configuration)
   - Participants: Marketing team, Sales GMs, Business Development
   - Deliverable: Documented role taxonomy, sector list with definitions
   - Risk: Unclear definitions → poor adoption → segmentation failure

2. **Data Quality Foundation**
   - Timing: Weeks 3-6 (blocking go-live)
   - Activity: Historical contact classification and cleanup
   - Effort: Significant manual work depending on contact volume
   - Risk: Incomplete classification → "poo in, poo out" continues

3. **RFP Workflow Design**
   - Timing: Weeks 2-3 (blocking configuration)
   - Participants: Marketing, Sales, Business Development
   - Deliverable: RFP request form specification, workflow routing rules
   - Risk: Misaligned workflow → team resistance, Asana not retired

### Medium Priority - Important Considerations

4. **Change Management & User Adoption**
   - Sales team required field discipline: Training and change management needed
   - Admin team lead qualification: Clear guidelines and decision framework
   - Marketing team capability building: New tools, new dashboards, new process

5. **Parallel Asana/NetSuite Process**
   - Recommendation: Run both systems 2-4 weeks
   - Ensures smooth transition; catches workflow gaps
   - Allows teams to validate new process before Asana retirement

6. **Market Intelligence Dashboard Requirements**
   - Timing: Weeks 3-4 (blocking configuration)
   - Participants: Marketing team with analyst/BI support
   - Deliverable: Dashboard design, metric definitions, access controls
   - Risk: Unclear requirements → dashboard doesn't drive strategic decisions

### Low Priority - Manageable Items

7. **Email Template Migration**
   - Timing: Week 4 (post-launch if needed)
   - Decision: Recreate MailChimp templates or establish new ones
   - Team assessment: Low priority; can recreate as needed

8. **Google Forms/Event Integration**
   - Timing: Phase 2 evaluation
   - Decision: Formalize event tracking or continue current approach

9. **Philippines Team Integration**
   - Timing: Week 4
   - Requirement: Time entry system connection to RFP project records
   - Assessment: Should be straightforward if system exists

### Risk Mitigation Strategies

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Data quality remains poor | Medium | High | Taxonomy workshop + classification project during migration + validation rules |
| Sales team doesn't adopt required fields | Medium | High | Change management, training, accountability, regular audits |
| RFP workflow misaligned with team | Low | High | Detailed requirements workshop + parallel testing + iterative refinement |
| Market intelligence unused | Low | Medium | Regular dashboard reviews, tie to strategic planning, executive visibility |
| Email marketing over-invested | Low | Medium | Realistic expectations; focus on segmentation-driven targeting; minimal templates |
| Event management becomes burden | Low | Medium | Phase 2 evaluation; clear ROI assessment before investment |

---

## Training & Organizational Change

### Marketing Team Training

**Core Training (Required):**
- Contact segmentation and saved searches (2 hours)
- Email campaign creation and scheduling (1.5 hours)
- RFP workflow and project management (2 hours)
- Market intelligence dashboard navigation (1 hour)
- Data quality standards and maintenance (1 hour)
- Google Drive integration and file management (1 hour)

**Estimated Training Effort:** 8.5 hours per person

### Sales/BD Team Training (Marketing Impact)

**Required Training:**
- Contact role classification (importance and accuracy) (1.5 hours)
- Sector assignment (1 hour)
- Territory assignment (0.5 hours)
- Early opportunity creation (triggers marketing alerts) (1 hour)

**Estimated Training Effort:** 4 hours per person

### Admin Team Training

**Required Training:**
- Lead qualification and routing (2 hours)
- Web form lead management (1.5 hours)
- Data quality standards (1 hour)
- Duplicate detection and merge (1 hour)
- Contact record maintenance (1 hour)

**Estimated Training Effort:** 6.5 hours for admin team

### Change Management Approach

1. **Executive Sponsorship:** C-suite alignment on marketing role and strategic market intelligence value
2. **Communications:** Regular updates on implementation progress, value realization, adoption metrics
3. **Training Cadence:** Initial training + refresher sessions 30/60/90 days post-launch
4. **Support Model:** In-app help, reference guides, office hours for questions
5. **Adoption Metrics:** Track compliance with required fields, segment usage, dashboard engagement

---

## Next Steps & Go-Live Readiness

### Pre-Implementation Checklist

- [ ] Executive stakeholder alignment on marketing scope and phased approach
- [ ] Taxonomy workshop scheduled (Week 1)
- [ ] RFP workflow design workshop scheduled (Week 2)
- [ ] Market intelligence dashboard requirements session scheduled (Week 3)
- [ ] Data migration plan documented (contact classification effort, timeline, ownership)
- [ ] Training schedule established (dates, instructors, participant lists)
- [ ] Parallel Asana/NetSuite process defined (duration, success criteria, go-live decision)
- [ ] Change management communications plan prepared
- [ ] Support model and escalation process documented
- [ ] Success metrics defined and tracking mechanism established

### 90-Day Post-Launch Roadmap

**Weeks 1-2:**
- Monitor data quality; track contact field completion rates
- Gather feedback on RFP workflow; iterate if needed
- Validate market intelligence dashboard usefulness

**Weeks 3-4:**
- First quarterly campaign cycle; track performance vs. MailChimp baseline
- Refine segmentation based on usage patterns
- Sales team compliance review (required fields)

**Month 2:**
- Second campaign cycle; optimize based on learnings
- Dashboard refinement based on usage
- Plan for event management and survey evaluation

**Month 3:**
- Comprehensive success metrics review
- Strategic market intelligence analysis; document proactive content created
- Plan Phase 2 capabilities

---

## Appendix A: Requirements Traceability

All 27 marketing requirements mapped and validated:

| REQ-ID | Requirement Name | Source Document | Implementation Phase | Status |
|--------|-----------------|-----------------|---------------------|--------|
| REQ-M001 | Relationship-based approach | Questionnaire Q2.1 | Phase 1 | Validated |
| REQ-M002 | Minimal email marketing | Questionnaire Q1.3, Q2.2 | Phase 1 | Validated |
| REQ-M003 | RFP coordination function | Questionnaire Q1.5, Q2.1 | Phase 1 | Validated |
| REQ-M004 | Multi-dimensional segmentation | Questionnaire Q1.6, Q2.3 | Phase 1 | Validated |
| REQ-M005 | Data quality controls | Questionnaire Q1.6 | Phase 1 | Validated |
| REQ-M006 | Custom contact roles | Questionnaire Q2.3 | Phase 1 | Validated |
| REQ-M007 | Sector classifications | Questionnaire Q2.3 | Phase 1 | Validated |
| REQ-M008 | Territory segmentation | Questionnaire Q2.3 | Phase 1 | Validated |
| REQ-M009 | Transactional email | Questionnaire Q1.3 | Phase 1 | Validated |
| REQ-M010 | Quarterly communications | Questionnaire Q2.2 | Phase 1 | Validated |
| REQ-M011 | Personal email sending | Questionnaire Q1.2 | Phase 1 | Validated |
| REQ-M012 | Replace MailChimp | Questionnaire Q1.2 | Phase 1 | Validated |
| REQ-M013 | Minimal event tracking | Questionnaire Q1.2 | Phase 1 (Minimal) | Validated |
| REQ-M014 | Evaluate events post-launch | Questionnaire Q1.2 | Phase 2 | Validated |
| REQ-M015 | Early RFP visibility | Questionnaire Q1.6 | Phase 1 | Validated |
| REQ-M016 | Volume tracking | Questionnaire Q1.7 | Phase 1 | Validated |
| REQ-M017 | RFP workflow automation | Questionnaire Q1.2 | Phase 1 | Validated |
| REQ-M018 | Document attachment | Questionnaire Q1.2 | Phase 1 | Validated |
| REQ-M019 | Pipeline visibility by sector | Questionnaire Q4.1 | Phase 1 | Validated |
| REQ-M020 | Market intelligence dashboard | Questionnaire Q4.1 | Phase 1 | Validated |
| REQ-M021 | Sector performance analysis | Questionnaire Q4.1 | Phase 1 | Validated |
| REQ-M022 | Customer surveys | Questionnaire Q1.7 | Phase 2 | Deferred |
| REQ-M023 | Survey functionality | Questionnaire Q1.7 | Phase 2 | Deferred |
| REQ-M024 | Web-to-lead forms | Questionnaire Q3.1 | Phase 1 | Validated |
| REQ-M025 | Google Drive integration | Questionnaire Q1.2 | Phase 1 | Validated |
| REQ-M026 | Content library management | Gap Analysis | Phase 1 | Validated |
| REQ-M027 | Philippines team integration | Gap Analysis | Phase 1 | Validated |

---

## Appendix B: Change Log & Sources

**Document Version 1.0 Sources:**
- Questionnaire_Marketing_v3.0.md (Comprehensive discovery findings)
- Requirements_Map_Marketing_v3.1.md (Structured requirement mapping)
- Orion Whitepaper.md (Orion/NetSuite capabilities)
- Master_Transcript_Marketing.md (Supporting evidence and context)

**Change Log:**
- 2025-10-28: Initial BRD v1.0 created; all 27 marketing requirements validated against Orion/NetSuite capabilities

---

## Approval Sign-Off

This document is ready for C-suite review and approval.

**Implementation Consultant:** _________________ Date: _______

**Marketing Leader (Stakeholder):** _________________ Date: _______

**Sales Leadership (Stakeholder):** _________________ Date: _______

**Project Executive Sponsor:** _________________ Date: _______

---

*End of Business Requirements Document - Marketing v1.0*





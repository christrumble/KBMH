# Questionnaire - Marketing
**Version**: 3.0  
**Date**: 2025-10-15  
**Process Area**: Marketing (Campaigns, Events, Content, Market Intelligence)

## Change Log
- **Date**: 2025-10-15
- **Version**: 3.0
- **Sources**: Marketing/2 Input/Master_Transcript_Marketing.md; Marketing/2 Input/MRK & CRM Outline & Questionnaire
- **Summary**: Complete re-analysis using the comprehensive Master_Transcript_Marketing.md which provides better organization and context than v2.0 sources. Focus on Marketing-specific requirements (separate from CRM).

## PROCESSED FILES
- Marketing/2 Input/Master_Transcript_Marketing.md (Primary source - October 15, 2025)
- Marketing/2 Input/MRK & CRM Outline & Questionnaire (Questionnaire template)

## Decision Log

### Marketing Strategy & Philosophy Decisions
- **REQ-M001**: Continue relationship-based, targeted approach vs. mass marketing (ALIGNS) - "So much of what we do is relationship-based, and so we're being very selective of, like, hey, we want to invite these specific 20 people"

- **REQ-M002**: Minimal email marketing implementation in Phase 1 (ALIGNS) - "the capability is fine, and it's great to know that we can do it"; "Way more than we would ever use" (120,000 emails/month capacity); "Less than 6 campaigns per year"

- **REQ-M003**: Marketing as RFP coordination function, not demand generation (ADAPT) - "Kind of unique because your marketing department is actually doing like some sales process really, right? Because you're doing RFPs" - Marcus

### Contact Segmentation & Data Quality Decisions
- **REQ-M004**: Enable multi-dimensional contact segmentation by role, sector, and geography (ACCOMMODATE) - "We want to be able to tailor those markets by location and by what their focus may be"; Need for custom role classifications beyond Core system limitations

- **REQ-M005**: Implement data quality controls and validation rules (ACCOMMODATE) - "Poo in, poo out"; "The data entry part of it has never been clean enough to trust in"; "Can't segment by role or purpose effectively"

- **REQ-M006**: Define custom contact roles including influencer types (ACCOMMODATE) - Listed roles needed: GC, broker, A&D firm, client, vendor, PM, CM, Finance/Accounting, Procurement, Facilities, Decision Maker, Executive Sponsor, Manufacturer Rep

- **REQ-M007**: Define market sectors/verticals for segmentation (ACCOMMODATE) - Healthcare, Technology, Corporate Office, Government, Education, Financial Services, Legal, Creative/Agency, Hospitality

- **REQ-M008**: Implement territory-based segmentation (SF, San Jose, Sacramento) (ADAPT) - "Alex's market ≠ Jill's market ≠ Kate's market"; Different industry mix and messaging needs by territory

### Communication & Campaign Decisions
- **REQ-M009**: Support transactional vs. marketing email distinction with opt-in management (ALIGNS) - "if they've unsubscribed and I need to tell them about a rate change, I can still send that, even if they've unsubscribed"; "NetSuite will manage that for you automatically"

- **REQ-M010**: Enable quarterly targeted communications to specific segments (ADAPT) - "if we did have a curated list of brokers and PM firms or CM firms, and, like, we did send out quarterly, oh, here's some market rates we're seeing"

- **REQ-M011**: Support personalized sending from individual user emails (ALIGNS) - "we're sending an email from a real person's email, rather than from info at KBM"

- **REQ-M012**: Replace MailChimp with NetSuite for occasional campaigns (ADAPT) - "MailChimp gets really pissed off when you try to load in Excel because they think you're going to spam a bunch of people" - Jenny; "Then most of it bounces anyways"

### Event Management Decisions
- **REQ-M013**: Minimal event tracking for Phase 1; continue current approach (ALIGNS) - "probably doing something maybe twice a month at this point" (showroom tours); "Who manages taking attendance? No one's taking headcount"; Decision: Continue personal invites and Google Forms

- **REQ-M014**: Evaluate event management post-go-live if value identified (FUTURE) - "Question of value vs. effort"; "May revisit post-go-live if value identified"

### RFP Management Decisions
- **REQ-M015**: Provide marketing team early visibility into RFP opportunities (ACCOMMODATE) - "Marketing has no visibility until formal request submitted"; "Can't proactively prepare"; Solution: Marketing team access to opportunity pipeline

- **REQ-M016**: Track projected vs. actual RFP volume by submitter (ACCOMMODATE) - "we track what that projected volume is versus what the actual volume is, so that we can see, like, how many people are overestimating"; Key for marketing resource planning

- **REQ-M017**: Implement RFP workflow routing to marketing team (ACCOMMODATE) - Replace Asana workflow; Generate Quote/Proposal record; Assign to Marketing PM; Track completion

- **REQ-M018**: Enable document attachment to opportunities/quotes (ALIGNS) - RFP documentation, response materials, Google Drive links; Version control; Team access

### Market Intelligence & Analytics Decisions
- **REQ-M019**: Provide marketing visibility into pipeline trends by sector (ACCOMMODATE) - "if marketing had more insight into what some of those leads are and could see and track over time the sectors and how the market is changing, then it would be easier for that team to create proactively create content and target it"

- **REQ-M020**: Create market intelligence dashboard for content planning (ACCOMMODATE) - Opportunities by sector trends; RFP volume by market/territory; Win/loss by sector; Pipeline by stage and sector

- **REQ-M021**: Enable sector performance analysis for strategic planning (ACCOMMODATE) - Identify trending sectors (e.g., healthcare growing); Proactive content creation; Resource forecasting; Strategic focus areas

### Survey & Feedback Decisions (Future Phase)
- **REQ-M022**: Implement customer satisfaction surveys post-project (FUTURE) - "Needed but not systematized"; "Nolan mentioned having customer service survey"; Low priority Phase 1

- **REQ-M023**: Enable survey functionality within NetSuite campaigns (FUTURE) - Track responses in NetSuite; Results visible on customer records; Trend analysis; Action item generation

### Integration Decisions
- **REQ-M024**: Web form lead capture with automatic NetSuite creation (ALIGNS) - Contact form submission → Lead created; Routing rules assign to appropriate team; Lead scoring and qualification

- **REQ-M025**: Google Drive integration for file management (ACCOMMODATE) - "we're going to integrate with Google Drive, and it's just represented in NetSuite"; Avoid 100GB storage limits

## Action Items

ACTION: Define complete taxonomy of contact roles for marketing segmentation  
ASSIGNED TO: Marketing Team (Jenny, Marketing PM)  
DUE: Before configuration phase  
RELATED TO: REQ-M004, REQ-M006

ACTION: Define market sectors/verticals taxonomy  
ASSIGNED TO: Marketing Team with Sales leadership input  
DUE: Before configuration phase  
RELATED TO: REQ-M007

ACTION: Document current MailChimp email templates for potential NetSuite recreation  
ASSIGNED TO: Marketing Team  
DUE: Low priority - post go-live  
RELATED TO: REQ-M012

ACTION: Define RFP request form fields and workflow requirements  
ASSIGNED TO: Marketing PM  
DUE: Before workflow configuration  
RELATED TO: REQ-M017

ACTION: Document desired market intelligence dashboard requirements  
ASSIGNED TO: Marketing Team  
DUE: Before reporting design phase  
RELATED TO: REQ-M020, REQ-M021

ACTION: Clean and validate contact data during migration  
ASSIGNED TO: Data Migration Team with Marketing validation  
DUE: During data migration phase  
RELATED TO: REQ-M005

ACTION: Evaluate post-go-live: Event management ROI and adoption potential  
ASSIGNED TO: Marketing Team  
DUE: 3-6 months post go-live  
RELATED TO: REQ-M014

ACTION: Evaluate post-go-live: Customer satisfaction survey implementation  
ASSIGNED TO: Marketing Team with Customer Service  
DUE: 6+ months post go-live  
RELATED TO: REQ-M022

## Additional Sessions Needed

### Session: Contact Segmentation Taxonomy Workshop
- **Participants Needed**: Marketing Team, Sales GMs (Jill, Alex, Kate), Business Development
- **Questions to Address**:
  • Finalize contact role taxonomy (brokers, A&D, PMs, CMs, GCs, etc.)
  • Define sector/vertical classifications
  • Establish territory assignments and rules
  • Data entry standards and validation rules
  • Ownership and maintenance responsibilities
- **Priority**: High (blocks REQ-M004, REQ-M006, REQ-M007, REQ-M008)
- **Suggested Duration**: 90-120 minutes
- **Dependencies**: Required before configuration phase
- **Evidence**: Multiple references to segmentation needs throughout transcript; "We want to be able to tailor those markets by location and by what their focus may be"

### Session: Market Intelligence Dashboard Requirements
- **Participants Needed**: Marketing Team, Sales Leadership, BI/Reporting Lead
- **Questions to Address**:
  • Specific metrics and KPIs for market intelligence
  • Dashboard layout and visualization preferences
  • Report frequency and distribution
  • Drill-down requirements
  • Access and permissions
- **Priority**: Medium (nice-to-have for Phase 1)
- **Suggested Duration**: 60 minutes
- **Dependencies**: REQ-M019, REQ-M020, REQ-M021
- **Evidence**: "if marketing had more insight into what some of those leads are and could see and track over time the sectors"

## New Questions Identified

### Proposed New Question: MKT-01. What specific content types does marketing create and how should they be organized?
- **Asked By**: Implied from RFP management discussion
- **Context**: Marketing creates presentations, proposals, RFP responses, case studies
- **Suggested Placement**: Functional Requirements → Document Management
- **Evidence**: "Marketing-created presentations"; "Proposals"; "Supporting materials"; "Templates and reusable content library"

### Proposed New Question: MKT-02. What is the relationship between marketing and the Philippines team for RFP work?
- **Asked By**: Implied from volume tracking discussion
- **Context**: Understanding resource allocation and time tracking
- **Suggested Placement**: Current State Assessment → Marketing Team Structure
- **Evidence**: "Track time by project"; References to "Philippines team time entry integration"

### Proposed New Question: MKT-03. How should marketing measure and report campaign ROI?
- **Asked By**: Implied from strategic discussions
- **Context**: Shift to more targeted approach requires ROI measurement
- **Suggested Placement**: Objectives & Strategy → Marketing KPIs
- **Evidence**: References to "Campaign ROI tracking"; "Revenue attribution by source"

---

## QUESTIONNAIRE RESPONSES

### SECTION 1: OVERVIEW & CURRENT STATE

#### 1.1 How do you currently generate and capture leads?

**Answer:**
KBM Hoag has a unique, relationship-driven lead generation model that differs significantly from traditional B2B marketing:

**Primary Lead Sources (in priority order):**
1. **Relationship-based influencer network** (dominant) - Personal relationships with brokers, A&D firms, project managers, general contractors
2. **RFPs through established relationships** - Formal requests arrive through relationship channels
3. **Strategic account management** - Existing client expansion and repeat business
4. **Web contact form** (minimal impact) - Mostly low-value inquiries; occasional valuable existing client requests

**What They Don't Do:**
- No broad demand generation campaigns
- No mass email marketing (except rare occasions, <6/year)
- Minimal content marketing
- No significant social media marketing
- No lead generation advertising

**Strategic Shift (Last Year):**
- Moved away from mass communications (discontinued quarterly newsletters internal and external)
- Focus on specific sectors and industries
- Targeted to specific people within sectors
- Market-specific approaches (SF ≠ San Jose ≠ Sacramento)
- Result: Better engagement with lower volume, more personalized, higher quality

**Current Capture Process:**
- Web form leads → Jenny (Admin) → Qualification → Route to GM or delete
- Relationship-based leads → BD reps enter into Zendesk (inconsistent)
- RFPs → Opportunity created (maybe) → Formal Asana request to marketing

**Evidence:**
- "So much of what we do is relationship-based, and so we're being very selective of, like, hey, we want to invite these specific 20 people, and we're sending an email from a real person's email, rather than from info at KBM"
- "Kind of unique because your marketing department is actually doing like some sales process really, right? Because you're doing RFPs" - Marcus
- Web form: "Most submissions are: cleaning quotes (deleted), one-off requests, occasional legitimate leads"
- "A lot of cleaning quotes or 'I inherited my grandmother's Newell Eames chair and need a pad for it'"
- **Notable Success:** "Client requesting cubicles → order for touchdown cubicles"

**Confidence Rating**: 95% - Comprehensive description with multiple supporting quotes

**BRD Requirements:**
- [REQUIREMENT] REQ-M001: Support relationship-based, targeted marketing approach (ALIGNS)
- [REQUIREMENT] REQ-M024: Web form lead capture with auto-routing (ALIGNS)
- [CONSTRAINT] Low web form lead quality - most will be deleted
- [PRIORITY] Must-Have: Web form integration; Should-Have: Better lead qualification tools

---

#### 1.2 What marketing tools and platforms are you using today?

**Answer:**

**Email Marketing:**
- **MailChimp** - Pay-as-you-go credits, no subscription, used <6 times/year
- Major pain points: "MailChimp gets really pissed off when you try to load in Excel because they think you're going to spam a bunch of people" - Jenny; "Then most of it bounces anyways"
- Manual list creation and upload process
- Can't segment effectively due to data quality issues
- Team creates images in Google Slides, embeds in MailChimp

**Project/Request Management:**
- **Asana** - RFP and marketing request tracking
- Formal project request submission by BD reps
- Includes background, links, documentation, projected volume
- Tracks projected vs. actual volume

**CRM/Sales:**
- **Zendesk** - Current CRM (being retired)
- Inconsistent data entry
- Limited contact type options
- "Are they the main contact? Are they finance? Is it procurement? We don't know"

**Event Management:**
- **Google Forms** - RSVP tracking for major events (when needed)
- **Paperless Post** - Mentioned for certain event invitations
- Personal email invitations (most common approach)
- Internal showroom event coordination form (manual)

**File Management:**
- **Google Drive** - Primary collaboration and storage (preferred)
- Project folders and document organization

**Pain Points:**
- Multiple disconnected systems
- Manual data movement between platforms
- No integrated view of customer interactions
- Data quality issues prevent effective segmentation
- "Poo in, poo out" - can't trust contact classification
- Heavy reliance on manual processes

**Evidence:**
- "MailChimp gets really pissed off when you try to load in Excel, because they think you're going to spam a bunch of people, and then most of it bounces anyways" - Jenny
- "The data entry part of it has never been clean enough to trust in"
- "Click rates aren't great so there's just really no way right now to target"
- "We do everything in slides, so we'll create, like, an image, and then we'll just embed that into MailChimp"

**Confidence Rating**: 95% - Explicit tool names and detailed usage patterns

**BRD Requirements:**
- [REQUIREMENT] REQ-M012: Replace MailChimp with NetSuite (ADAPT)
- [REQUIREMENT] REQ-M017: Replace Asana RFP workflow with NetSuite (ACCOMMODATE)
- [REQUIREMENT] REQ-M025: Google Drive integration (ACCOMMODATE)
- [ASSUMPTION] Will maintain Google Slides for image creation
- [PRIORITY] Must-Have: MailChimp replacement; Should-Have: Asana replacement

---

#### 1.3 How do you manage email marketing campaigns?

**Answer:**

**Current Volume & Frequency:**
- Less than 6 campaigns per year
- Discontinued quarterly newsletters (both internal and external)
- Discontinued event invitations via mass email
- Shifted to personalized, one-to-one outreach

**Current Campaign Types:**
- Quarterly market rate communications (by client tier)
- Occasional vendor process change notifications
- Rare targeted sector campaigns (if data quality allowed)
- Event invitations (only for major events; usually personal emails)

**Current Process:**
1. Identify target audience
2. Manual list creation in Excel
3. Upload to MailChimp (often rejected due to spam protection)
4. Create email content (images in Google Slides)
5. Send campaign
6. Most emails bounce due to data quality issues
7. No systematic opt-in/opt-out tracking

**Major Limitations:**
- Can't segment by role effectively (data quality)
- Can't segment by sector (no field in Core)
- Can't segment by relationship type
- One-size-fits-all messaging
- Manual workaround: "Only pull contacts from specific date ranges" to avoid spamming unsubscribed contacts
- Poor results: "Click rates aren't great"

**Desired Future State:**
- Curated lists by role (brokers, PM firms, CM firms)
- Market-specific campaigns (different for each GM's territory)
- Sector-specific targeting (e.g., healthcare trending up → tailored message)
- Quarterly market rate communications to specific tiers
- Automated subscription management
- Better deliverability through clean data

**Evidence:**
- "Less than 6 campaigns per year"
- "Discontinued quarterly newsletters (internal and external)"
- "if we did have a curated list of brokers and PM firms or CM firms, and, like, we did send out quarterly, oh, here's some market rates we're seeing, or something that we feel like would add value, and it was easier, we didn't have to recreate the wheel every time, I could see us using it" - Kimmy
- "Only pull contacts from specific date ranges" - current workaround for opt-out management
- "NetSuite will handle automatically" - regarding subscription status

**Confidence Rating**: 93% - Clear current state and explicit future needs

**BRD Requirements:**
- [REQUIREMENT] REQ-M002: Minimal email marketing Phase 1 (ALIGNS)
- [REQUIREMENT] REQ-M009: Transactional vs. marketing email distinction (ALIGNS)
- [REQUIREMENT] REQ-M010: Quarterly targeted communications (ADAPT)
- [REQUIREMENT] REQ-M011: Personalized sending from user emails (ALIGNS)
- [PRIORITY] Should-Have: All email capabilities (low initial usage expected)

---

#### 1.4 What is your current lead qualification process?

**Answer:**

**Current Process:**
Web forms → Jenny receives notification → Manual review → Decision:
- **Delete** (most common): Cleaning quotes, consumer requests, spam
- **Route to GM**: Existing client inquiries with clear account ownership
- **Route to appropriate team**: Rare new business inquiries

**Qualification Criteria (Informal):**
- Is this a legitimate business inquiry?
- Is this an existing client? (route to account owner)
- Is this commercial furniture-related?
- Does it meet minimum project criteria?

**Business Development Leads:**
- BD team (GMs) manage relationship-based leads personally
- Enter into Zendesk inconsistently
- "Most of our business development team actually creates it as an opportunity, and there is a lead stage under opportunity" - Kimmy
- Skip formal "lead" stage and go directly to opportunity

**RFP Qualification:**
- RFP identified through relationship → Preliminary assessment by BD rep
- When formal RFP arrives → Asana request to marketing team
- Marketing PM evaluates: Projected volume, timeline, resources needed
- Kickoff call with stakeholders
- Decision to pursue or decline

**Pain Points:**
- No systematic lead scoring
- Inconsistent data entry in Zendesk
- Marketing has no visibility until formal Asana request
- Can't track which influencers generate best leads
- No lead nurturing for opportunities not yet ready

**Future NetSuite Process:**
1. Lead captured (web form, manual entry, or direct opportunity creation)
2. Automatic routing based on rules (existing client → account owner; new → qualification queue)
3. Lead scoring and qualification workflow
4. Convert to opportunity when qualified
5. Marketing visibility into early-stage opportunities
6. Track lead source and influencer attribution

**Evidence:**
- "Goes web form, lead creation… I qualify… most of the time… cleaning quote… then I delete" - Matt
- "Most of our business development team actually creates it as an opportunity, and there is a lead stage under opportunity" - Kimmy
- "Notable Success: Client requesting cubicles → order for touchdown cubicles"
- "Marketing has no visibility until formal request submitted"

**Confidence Rating**: 90% - Process clearly described, some inference on future state

**BRD Requirements:**
- [REQUIREMENT] REQ-M024: Automated lead routing based on rules (ALIGNS)
- [FUNCTIONALITY] Lead scoring capability (available, low priority)
- [CONSTRAINT] Most web leads will be low quality
- [PRIORITY] Should-Have: Automated routing; Nice-to-Have: Lead scoring

---

#### 1.5 Who makes up your marketing team and what are their roles?

**Answer:**

Based on transcript evidence, the marketing team structure includes:

**Marketing Team Members:**
- **Marketing PM/Lead** (referenced multiple times) - RFP coordination, presentation development, resource management
- **Carlos & Jillian** - Mentioned as "Marketing-specific team members"
- **Jenny** - Admin role, handles web form lead qualification and routing

**Key Responsibilities:**
1. **RFP Response Coordination** (primary function)
   - Receive formal RFP requests from BD team via Asana
   - Schedule kickoff calls with stakeholders
   - Develop presentations and proposals
   - Track projected vs. actual volume
   - Manage marketing team resources

2. **Content Creation**
   - Client-facing materials
   - Presentations (Google Slides)
   - Proposals and RFP responses
   - Supporting marketing materials
   - Brand management

3. **Event Coordination**
   - Showroom event planning (~2x/month)
   - Showroom tours coordination
   - Event logistics with showroom manager
   - RSVP management (when needed)

4. **Limited Campaign Management**
   - Occasional email campaigns (<6/year)
   - Targeted communications (when data allows)
   - Event invitations (major events)

**NOT Traditional Marketing Roles:**
- No demand generation manager
- No content marketing specialist
- No social media manager
- No marketing automation specialist
- No campaign manager (traditional sense)

**Supporting Resources:**
- **Philippines Team** - Mentioned for RFP work and time tracking
- **Business Development GMs** (Jill, Alex, Kate) - Own client relationships and influencer network
- **Showroom Manager** - Coordinates physical event logistics

**Evidence:**
- "Kind of unique because your marketing department is actually doing like some sales process really, right? Because you're doing RFPs" - Marcus
- "Marketing PM schedules kickoff call with stakeholders"
- "Carlos & Jillian" - Marketing team members
- "Jenny" - Admin handling web leads
- References to "Philippines team time entry integration"

**Confidence Rating**: 85% - Role descriptions clear, exact team size and structure partially inferred

**BRD Requirements:**
- [REQUIREMENT] REQ-M015: Marketing team visibility into opportunities (ACCOMMODATE)
- [REQUIREMENT] REQ-M016: Volume tracking for resource planning (ACCOMMODATE)
- [REQUIREMENT] REQ-M017: RFP workflow routing to marketing team (ACCOMMODATE)
- [ASSUMPTION] Current team size adequate for minimal email marketing usage
- [PRIORITY] Must-Have: RFP workflow support

---

#### 1.6 What are your biggest challenges with lead acquisition?

**Answer:**

**1. Data Quality & Segmentation (Primary Challenge)**
- Core system has limited, unclear contact type options
- "Are they the main contact? Are they finance? Is it procurement? We don't know"
- Inconsistent data entry with no validation
- "Poo in, poo out" - can't trust contact classification
- Can't segment by role (broker, A&D, PM, CM, GC, etc.)
- Can't segment by sector/vertical effectively
- Result: Can't create targeted campaigns, one-size-fits-all messaging fails
- "Click rates aren't great so there's just really no way right now to target"

**2. Limited Market Intelligence**
- No visibility into early-stage opportunities
- Can't track market trends systematically
- Don't know which sectors are trending until too late
- Can't proactively create content for growing markets
- Reactive instead of strategic approach
- Limited insight into which influencers are most effective

**3. Email Marketing Tool Limitations**
- MailChimp rejects Excel uploads (spam protection)
- High bounce rates due to data quality
- Manual list creation process
- No integration with other systems
- Opt-in/opt-out tracking manual and error-prone
- "Then most of it bounces anyways" - Jenny

**4. RFP Workflow Visibility**
- Marketing has no visibility until formal Asana request submitted
- Can't proactively prepare for incoming RFPs
- Difficult to forecast resource needs
- Projected volumes often inaccurate (people overestimate)
- Can't track which estimators are most accurate
- Resource allocation challenging

**5. Disconnected Systems**
- Multiple tools not integrated (Zendesk, MailChimp, Asana, Google Forms)
- Manual data movement between systems
- No integrated view of customer interactions
- Duplicate effort and data inconsistency
- Time-consuming manual processes

**6. Low-Value Web Form Leads**
- Most web form submissions are cleaning quotes or consumer requests
- Time spent qualifying and deleting low-value leads
- Occasional valuable lead, but low signal-to-noise ratio

**Evidence:**
- "Poo in, poo out" - Data quality prevents targeting
- "The data entry part of it has never been clean enough to trust in"
- "if marketing had more insight into what some of those leads are and could see and track over time the sectors and how the market is changing, then it would be easier for that team to create proactively create content and target it"
- "MailChimp gets really pissed off when you try to load in Excel"
- "Marketing has no visibility until formal request submitted"
- "People overestimate RFP volume"

**Confidence Rating**: 95% - Explicitly stated challenges with detailed examples

**BRD Requirements:**
- [REQUIREMENT] REQ-M005: Data quality controls and validation (ACCOMMODATE)
- [REQUIREMENT] REQ-M004: Multi-dimensional segmentation (ACCOMMODATE)
- [REQUIREMENT] REQ-M019: Pipeline visibility by sector (ACCOMMODATE)
- [REQUIREMENT] REQ-M015: Early RFP visibility (ACCOMMODATE)
- [REQUIREMENT] REQ-M012: Replace MailChimp (ADAPT)
- [PRIORITY] Must-Have: Data quality and segmentation; High: Market intelligence

---

#### 1.7 How do you currently track marketing performance and ROI?

**Answer:**

**Current Tracking (Minimal & Manual):**

**Email Campaign Metrics:**
- MailChimp provides basic open rates and click rates
- "Click rates aren't great" - limited visibility into effectiveness
- No systematic analysis or trend tracking
- No attribution to revenue or opportunities

**RFP Volume Tracking:**
- Asana tracks projected volume vs. actual volume
- Identify who overestimates project size
- Helps with resource allocation over time
- Marketing team capacity planning
- No direct ROI calculation

**Event Tracking:**
- No systematic tracking for most events
- "Who manages taking attendance? No one's taking headcount"
- Exception: Major events like grand openings have check-in process
- No conversion tracking from events to opportunities
- No event ROI analysis

**Lead Source Tracking:**
- Informal tracking of where leads originate
- Know that relationship-based leads are primary source
- No quantified metrics by source
- No lead-to-revenue attribution

**What's NOT Tracked:**
- Campaign ROI (cost vs. revenue generated)
- Lead source performance and conversion rates
- Influencer relationship ROI (spend vs. opportunities generated)
- Content effectiveness
- Channel performance
- Marketing contribution to pipeline
- Cost per opportunity
- Marketing-sourced vs. sales-sourced revenue

**Desired Future State:**
Marketing KPIs mentioned in transcript:
- Campaign performance (open rates, click rates)
- Lead source tracking and conversion metrics (lead → opportunity → customer)
- Opportunity pipeline by source
- Sector performance trends
- Event attendance and ROI (if implemented)
- Influencer engagement and attribution
- Market intelligence metrics (sector trends, RFP volume by market)

**Evidence:**
- "Click rates aren't great so there's just really no way right now to target"
- "we track what that projected volume is versus what the actual volume is, so that we can see, like, how many people are overestimating"
- "Who manages taking attendance? No one's taking headcount"
- "At our grand opening, we had people checking people in" (exception, not typical)
- Desired: "Pipeline visibility by sector"; "Trend dashboards"; "Sector performance reporting"

**Confidence Rating**: 88% - Current limitations clear; future desires inferred from capability discussions

**BRD Requirements:**
- [REQUIREMENT] REQ-M020: Market intelligence dashboard (ACCOMMODATE)
- [REQUIREMENT] REQ-M021: Sector performance analysis (ACCOMMODATE)
- [REQUIREMENT] REQ-M016: RFP volume accuracy tracking (ACCOMMODATE)
- [FUNCTIONALITY] Campaign performance tracking (native NetSuite)
- [PRIORITY] Should-Have: Market intelligence dashboards; Nice-to-Have: Campaign ROI

---

### SECTION 2: OBJECTIVES & STRATEGY

#### 2.1 What is your overall marketing strategy and lead generation goals?

**Answer:**

KBM Hoag's marketing strategy is fundamentally different from traditional B2B marketing:

**Core Strategy: Relationship-Based, Not Demand Generation**

**Strategic Principles:**
1. **Personal Relationship Cultivation** - One-to-one communication and relationship building
2. **Targeted Sector Focus** - Specific industries and markets, not broad campaigns
3. **Influencer Network Management** - Relationships with brokers, A&D firms, PMs drive business
4. **Strategic Account Management** - Deepening existing client relationships
5. **RFP Excellence** - Marketing as RFP response coordinators and presentation specialists

**What They Deliberately Don't Do:**
- No broad campaigns or mass marketing
- No traditional lead generation funnels
- No content marketing at scale
- No social media focus
- No demand generation in traditional sense

**Strategic Shift (Implemented Last Year by GM):**
- **From:** Mass communications, quarterly newsletters to all contacts, broad email blasts
- **To:** Targeted, sector-specific, relationship-based outreach to specific audiences
- **Result:** "Better engagement" even with "lower volume of outreach", "more personalized", "higher quality interactions"

**Marketing Function Definition:**
- Primary: RFP response coordination and presentation development
- Secondary: Targeted communications to specific segments
- Tertiary: Event coordination (showroom tours ~2x/month)
- Not: Traditional demand generation

**Lead Generation Philosophy:**
- Leads are relationship-driven, not campaign-driven
- Business development GMs own influencer relationships
- Quality over quantity
- "We're being very selective of, like, hey, we want to invite these specific 20 people"

**Success Metrics (Implicit):**
- Win rate on RFPs
- Relationship depth with key influencers
- Client satisfaction and repeat business
- Sector penetration in target markets
- Not: Lead volume, MQL/SQL conversion, campaign response rates

**Evidence:**
- "So much of what we do is relationship-based, and so we're being very selective"
- "we're sending an email from a real person's email, rather than from info at KBM"
- "Kind of unique because your marketing department is actually doing like some sales process really, right? Because you're doing RFPs" - Marcus
- **GM's Strategic Shift:** "Move away from mass communications", "Focus on specific sectors and industries", "Targeted to specific people within sectors", "Market-specific approaches (SF ≠ San Jose ≠ Sacramento)"
- **Result:** "Better engagement", "Lower volume of outreach", "More personalized", "Higher quality interactions"

**Confidence Rating**: 95% - Strategy explicitly discussed with clear examples

**BRD Requirements:**
- [REQUIREMENT] REQ-M001: System must support relationship-based approach (ALIGNS)
- [REQUIREMENT] REQ-M003: Support marketing-as-RFP-coordination model (ADAPT)
- [CONSTRAINT] Not building traditional demand generation infrastructure
- [ASSUMPTION] Strategy will continue; system must enable not change this approach
- [PRIORITY] Must-Have: RFP support; Should-Have: Targeted communication capability

---

#### 2.2 What types of campaigns do you run (frequency, seasonality)?

**Answer:**

**Campaign Frequency: Minimal**
- Less than 6 campaigns per year via MailChimp
- Discontinued quarterly newsletters (both internal and external)
- Discontinued mass event invitations
- NetSuite capacity: 120,000 emails/month - "Way more than we would ever use"

**Current Campaign Types:**

**1. Quarterly Market Rate Communications**
- Target: Existing clients, segmented by tier
- Purpose: Rate change notifications, market updates
- Frequency: Quarterly or as-needed
- Approach: Would prefer targeted by client tier, currently one-size-fits-all

**2. Vendor Process Change Notifications**
- Target: Vendor contacts
- Purpose: Process updates, policy changes, new requirements
- Frequency: As-needed (infrequent)
- Approach: Operational communication, sent from info@kbmhoag.com

**3. Sector-Specific Content (Aspirational)**
- Example: Healthcare sector trending up → targeted content to healthcare A&D, brokers, clients
- Current barrier: Can't segment effectively due to data quality
- Future potential with clean data and segmentation

**4. Broker/Influencer Touchpoints (Potential)**
- Target: Curated lists of brokers, PM firms, CM firms
- Purpose: Quarterly value-add content (market rates, insights)
- Quote: "if we did have a curated list of brokers and PM firms or CM firms, and, like, we did send out quarterly, oh, here's some market rates we're seeing, or something that we feel like would add value, and it was easier, we didn't have to recreate the wheel every time, I could see us using it" - Kimmy
- Currently not done due to tool and data limitations

**Event Communications:**
- **Showroom Tours** (~2x/month) - Personal email invitations, not campaigns
- **Showroom Events** (occasional) - Cocktail receptions, product launches
- **Major Events** (rare) - Grand openings with formal RSVP and attendance tracking
- Approach: "Hey, we want to invite these specific 20 people" - personal, not mass email

**Seasonality:**
- No significant seasonal patterns mentioned
- RFP volume may vary but not explicitly seasonal
- Event frequency varies based on product launches and client needs
- Rate communications quarterly but flexible timing

**Historical (Discontinued):**
- Quarterly newsletters to all contacts (internal and external) - stopped
- Mass event invitations via MailChimp - stopped, moved to personal invites
- Reason: Strategic shift to more targeted, relationship-based approach

**Evidence:**
- "Less than 6 campaigns per year"
- "120,000 emails/month included" - "Way more than we would ever use"
- "Discontinued quarterly newsletters (internal and external)"
- "Discontinued event invitations via mass email"
- "probably doing something maybe twice a month at this point" (showroom events) - Jill Marsh
- "we're being very selective of, like, hey, we want to invite these specific 20 people"

**Confidence Rating**: 92% - Campaign types and frequency clearly stated; some future potential inferred

**BRD Requirements:**
- [REQUIREMENT] REQ-M002: Minimal email marketing Phase 1 (ALIGNS)
- [REQUIREMENT] REQ-M010: Quarterly targeted communications capability (ADAPT)
- [REQUIREMENT] REQ-M011: Personal email sending from user accounts (ALIGNS)
- [FUNCTIONALITY] Campaign scheduling and automation (available but low priority)
- [PRIORITY] Nice-to-Have: Email campaign features (low expected usage)

---

#### 2.3 Who are your target markets and buyer personas?

**Answer:**

**Geographic Markets:**
- **San Francisco** - Jill Marsh's territory
- **San Jose** - Kate's territory
- **Sacramento** - Alex Blangeres' territory
- Each market has distinct characteristics: "Alex's market ≠ Jill's market ≠ Kate's market"

**Market Differences:**
- Industry mix varies by geography
- Client types differ (SF corporate tech vs. Sacramento government, etc.)
- Competitive landscape unique to each market
- Rate structures may vary by market
- Messaging needs distinct per territory

**Industry Sectors/Verticals (Segmentation Needed):**
- **Healthcare** (explicitly mentioned as "trending up")
- **Technology/Tech** (implied SF market strength)
- **Corporate Office**
- **Government** (implied Sacramento strength)
- **Education**
- **Financial Services**
- **Legal**
- **Creative/Agency**
- **Hospitality**
- Other

**Buyer Personas & Contact Roles:**

**Decision Makers & Economic Buyers:**
- Primary Contact / Decision Maker
- Executive Sponsor
- Finance/Accounting (budget control)
- Procurement (purchasing authority)
- Facilities Manager

**Influencers (Critical to KBM Hoag's Model):**
- **Brokers** (real estate) - Connect clients to KBM Hoag
- **A&D Firms** (Architects & Designers) - Specify furniture, influence client decisions
- **Project Managers** (PM firms) - Manage project, recommend vendors
- **Construction Managers** (CM firms) - Coordinate vendors
- **General Contractors** (GCs) - Building construction, coordinate FF&E
- **Manufacturer Reps** - Partner relationships

**Client-Side Contacts:**
- Project Manager (client-side)
- Facilities
- Office Manager
- HR (in some cases)

**Vendor/Partner Contacts:**
- Vendor primary contacts
- Manufacturer representatives
- Service providers

**Relationship-Based Model:**
"Most of those are managed by our business development team... the general managers, like, their relationships. So they're the owners of all of that" - Kimmy

The influencer network is THE primary driver of business, not direct marketing to end clients.

**Evidence:**
- Geography: "San Francisco (Jill's territory)"; "San Jose (Kate's territory)"; "Sacramento (Alex's territory)"
- Sectors: "Healthcare (trending up)"; "technology"; "corporate"; "government"; "education" (listed in transcript)
- Influencer types: Extensive discussion of "brokers", "A&D firms", "project managers", "CM firms", "GC", throughout transcript
- Contact roles needed: "Primary Contact, Decision Maker, Finance/Accounting, Procurement, Facilities, Project Manager, Executive Sponsor, Influencer (Broker), A&D, CM, PM, GC, Manufacturer Rep, Vendor Contact"
- "Most of those are managed by our business development team... the general managers"

**Confidence Rating**: 93% - Explicit geography and roles; sectors partially listed with examples

**BRD Requirements:**
- [REQUIREMENT] REQ-M006: Define custom contact roles for all personas (ACCOMMODATE)
- [REQUIREMENT] REQ-M007: Define market sectors/verticals (ACCOMMODATE)
- [REQUIREMENT] REQ-M008: Territory-based segmentation (ADAPT)
- [REQUIREMENT] REQ-M004: Multi-dimensional segmentation (ACCOMMODATE)
- [PRIORITY] Must-Have: Contact role and sector definitions before go-live

---

#### 2.4 What are your key marketing KPIs and success metrics?

**Answer:**

**Current Tracking (Limited):**

Based on the transcript and implied success metrics, KBM Hoag's marketing KPIs would include:

**Primary Metrics (RFP Focus):**
1. **RFP Win Rate** - Percentage of RFPs that convert to won projects
2. **RFP Volume Forecasting Accuracy** - Projected vs. actual volume by submitter
   - "we track what that projected volume is versus what the actual volume is, so that we can see, like, how many people are overestimating"
3. **RFP Response Time** - Marketing team turnaround time
4. **Marketing Resource Utilization** - Capacity planning based on RFP volume

**Relationship/Influencer Metrics (Desired):**
5. **Influencer ROI** - Investment in relationship vs. opportunities generated
   - "it'd be so cool to see, like, the ROI of an investment on a relationship. like, I spent $6,000 on this person, and I got $3 million"
6. **Event Attendance and Conversion** - Attendees who become opportunities
   - Currently not tracked: "Who manages taking attendance? No one's taking headcount"
7. **Influencer Engagement** - Activities logged, touchpoints, relationship depth

**Pipeline & Market Intelligence Metrics:**
8. **Pipeline by Sector** - Trend over time, identify growing markets
   - "if marketing had more insight into what some of those leads are and could see and track over time the sectors"
9. **Sector Performance** - Win rate, average deal size, cycle time by sector
10. **Territory Performance** - Pipeline and revenue by GM territory
11. **Early-Stage Opportunity Visibility** - RFPs in pipeline before formal request

**Campaign Metrics (When Used):**
12. **Email Campaign Performance** - Open rates, click rates (currently poor due to data quality)
13. **Lead Source Performance** - Conversion rates by source (web, referral, event, etc.)
14. **Campaign ROI** - Revenue attribution to campaigns (not currently tracked)

**Data Quality Metrics:**
15. **Contact Segmentation Accuracy** - Percentage properly classified
16. **Data Completeness** - Required fields populated

**What's NOT Currently Measured (But Implied as Gaps):**
- Marketing-sourced revenue vs. sales-sourced
- Lead-to-customer conversion by source
- Cost per opportunity
- Content effectiveness
- Channel attribution
- Customer acquisition cost (CAC)

**NetSuite Capabilities for Future Tracking:**
- "Real-time marketing dashboards and KPIs"
- "Campaign ROI analysis and attribution"
- "Lead source performance tracking"
- "Conversion funnel reporting from lead to customer"
- "Market trend reporting"; "Sector performance analysis"

**Evidence:**
- "we track what that projected volume is versus what the actual volume is"
- "it'd be so cool to see, like, the ROI of an investment on a relationship"
- "if marketing had more insight into what some of those leads are and could see and track over time the sectors and how the market is changing"
- "Click rates aren't great" (current email performance)
- "Pipeline visibility by sector"; "Trend dashboards"; "Sector performance reporting" (desired)

**Confidence Rating**: 85% - Some explicit metrics; many inferred from pain points and desired capabilities

**BRD Requirements:**
- [REQUIREMENT] REQ-M020: Market intelligence dashboard with sector trends (ACCOMMODATE)
- [REQUIREMENT] REQ-M021: Sector performance analysis reporting (ACCOMMODATE)
- [REQUIREMENT] REQ-M016: RFP volume accuracy tracking (ACCOMMODATE)
- [FUNCTIONALITY] Campaign performance tracking (native NetSuite capability)
- [PRIORITY] Should-Have: Market intelligence KPIs; Nice-to-Have: Campaign metrics (low usage)

---

### SECTION 3: FUNCTIONAL REQUIREMENTS

#### 3.1 What specific lead capture methods do you need?

**Answer:**

**1. Web-to-Lead Forms (Current & Continuing)**
- **Website contact form** - Primary current method
- Auto-create lead in NetSuite
- Route to appropriate queue (Jenny for qualification)
- Despite low quality, needed for business legitimacy: "weird to be a business without a web form"

**Form Fields Required:**
- Name, Company, Email, Phone (standard)
- Inquiry type/reason for contact
- Project details (optional)
- How did you hear about us? (lead source)

**2. Manual Lead Entry (Primary Method)**
- BD reps manually create leads/opportunities from relationship interactions
- "Most of our business development team actually creates it as an opportunity, and there is a lead stage under opportunity" - Kimmy
- Quick entry form for speed
- Associate with influencer/referral source

**3. Email-to-Lead (Potential)**
- Create lead from email inquiry
- Outlook/Gmail integration
- Attach email thread to lead record

**4. Event Registration (Low Priority)**
- RSVP forms for major events
- Currently using Google Forms
- Could use NetSuite forms if value identified

**5. Referral Tracking**
- Capture influencer/referral source
- Link to broker, A&D firm, PM, etc.
- Critical for ROI tracking

**Lead Routing Requirements:**
- **Existing client inquiries** → Route to account owner (assigned GM)
- **New business** → Route to Jenny for qualification
- **RFPs** → Create opportunity, notify appropriate GM
- **Junk/spam** → Easy deletion process

**Lead Assignment Rules:**
- By territory (SF/San Jose/Sacramento)
- By existing relationship (account ownership)
- By lead source (if known)
- Default to admin queue for qualification

**Evidence:**
- "We would keep the web forum. Because we have it today, and it serves a purpose, and it'd be weird to be a business without a web form" - Matt
- "Goes web form, lead creation… I qualify… most of the time… cleaning quote… then I delete" - Matt
- "Most of our business development team actually creates it as an opportunity, and there is a lead stage under opportunity" - Kimmy
- Web form integration: "Contact form submission → Lead created in NetSuite automatically"; "Routing rules assign to appropriate team member"

**Confidence Rating**: 90% - Clear current methods; routing logic inferred from process

**BRD Requirements:**
- [REQUIREMENT] REQ-M024: Web-to-lead form integration (ALIGNS)
- [FUNCTIONALITY] Manual lead entry with quick add form (native capability)
- [FUNCTIONALITY] Lead routing and assignment rules (native capability)
- [PRIORITY] Must-Have: Web form integration; Should-Have: Routing automation

---

#### 3.2 What information must be collected from prospects?

**Answer:**

**Basic Contact Information:**
- First Name, Last Name (required)
- Company Name (required)
- Job Title/Role
- Email Address (required)
- Phone Number
- Mobile Number (optional)

**Company/Account Information:**
- Industry/Sector (required for segmentation) - Healthcare, Tech, Corporate, Government, etc.
- Company Size (employees)
- Geographic Location/Territory (SF, San Jose, Sacramento)
- Account Type (Prospect, Client, Influencer, Vendor)

**Contact Classification (CRITICAL for Segmentation):**
- **Primary Role** (required) - One of defined taxonomy:
  - Decision Maker
  - Finance/Accounting
  - Procurement
  - Facilities Manager
  - Project Manager
  - Executive Sponsor
  - Office Manager
  - HR
- **Relationship Type** (required) - Can be multiple:
  - Client Contact
  - Influencer - Broker
  - Influencer - A&D Firm
  - Influencer - PM Firm
  - Influencer - CM Firm
  - Influencer - GC
  - Vendor Contact
  - Manufacturer Rep
  - Partner

**Lead/Opportunity Specific:**
- Lead Source (required) - How did we connect?
  - Web Form
  - Referral (from whom?)
  - Influencer (which one?)
  - RFP
  - Event
  - Existing Client
- Project Type/Need
- Project Timeline
- Estimated Project Value (if known)
- Decision Timeline

**Segmentation Fields (for Marketing):**
- Sector/Vertical (required) - Healthcare, Tech, Corporate, Gov, Education, etc.
- Territory (required) - SF, San Jose, Sacramento
- Opt-in Status (required) - Marketing email subscription
- Communication Preferences

**Influencer Attribution:**
- Referred By (contact link)
- Influencer Relationship
- How introduced

**Data Quality Requirements:**
From transcript pain points, these fields need validation/required rules:
- "Are they the main contact? Are they finance? Is it procurement? We don't know" - Current gap
- Solution: Required role classification with clear definitions
- Validation rules to ensure completeness
- Duplicate detection on name, email, company

**Evidence:**
- Contact roles needed: "Primary Contact, Decision Maker, Finance/Accounting, Procurement, Facilities, Project Manager, Executive Sponsor, Influencer (Broker), A&D, CM, PM, GC, Manufacturer Rep, Vendor Contact"
- Sectors: "Healthcare, Technology, Corporate Office, Government, Education, Financial Services, Legal, Creative/Agency, Hospitality, Other"
- Territory: "San Francisco (Jill's territory)"; "San Jose (Kate's territory)"; "Sacramento (Alex's territory)"
- Data quality: "Poo in, poo out"; "The data entry part of it has never been clean enough to trust in"
- Segmentation critical: "We want to be able to tailor those markets by location and by what their focus may be"

**Confidence Rating**: 92% - Explicit needs from segmentation requirements and pain points

**BRD Requirements:**
- [REQUIREMENT] REQ-M006: Custom contact role definitions (ACCOMMODATE)
- [REQUIREMENT] REQ-M007: Market sector/vertical fields (ACCOMMODATE)
- [REQUIREMENT] REQ-M008: Territory field with validation (ADAPT)
- [REQUIREMENT] REQ-M005: Required fields and validation rules (ACCOMMODATE)
- [PRIORITY] Must-Have: Role, sector, territory fields and validation

---

#### 3.3 What email marketing capabilities are required?

**Answer:**

**Core Requirements (Minimal Usage Expected):**

**1. Segmentation & Targeting**
- Segment by contact role (broker, A&D, PM, etc.)
- Segment by sector/vertical (healthcare, tech, corporate, etc.)
- Segment by territory (SF, San Jose, Sacramento)
- Segment by relationship type (client, influencer, vendor)
- Segment by client tier (for rate communications)
- Combined criteria (e.g., "healthcare A&D firms in SF")

**2. Subscription Management (Critical)**
- Automatic opt-in/opt-out tracking
- **Transactional emails** (no opt-in required):
  - Rate changes to clients
  - Process changes to vendors
  - Important business communications
- **Marketing emails** (opt-in required):
  - Promotional campaigns
  - Event invitations (if mass email)
  - Newsletters (if resumed)
- "if they've unsubscribed and I need to tell them about a rate change, I can still send that" - Speaker 2
- "NetSuite will manage that for you automatically" - Speaker 3

**3. Campaign Creation & Sending**
- Create one-off campaigns
- Schedule campaigns
- Send from individual user email OR info@kbmhoag.com
- Personalization/merge tags (name, company, etc.)
- Template management (low priority - team uses Google Slides)

**4. Analytics & Tracking**
- Open rates
- Click rates
- Bounce tracking
- Unsubscribe tracking
- Link performance
- Conversion tracking (email → opportunity)

**5. List Management**
- Saved searches for recurring segments
- Static groups for one-time campaigns
- Automated list creation from CRM data (vs. manual Excel uploads)
- "if we did have a curated list of brokers and PM firms" - ability to create and maintain

**What's NOT Required (Low Priority):**
- Advanced automation/drip campaigns
- A/B testing (nice to have)
- Complex workflow automation
- Advanced personalization
- Landing page creation
- Form builder (using web-to-lead)

**Volume & Capacity:**
- Current: <6 campaigns/year
- NetSuite includes: 120,000 emails/month
- "Way more than we would ever use" - Matt

**Current Pain Point to Solve:**
- "MailChimp gets really pissed off when you try to load in Excel" - Need seamless list creation from NetSuite data
- "most of it bounces anyways" - Need clean data and subscription management
- Manual opt-out management - "Only pull contacts from specific date ranges" - Need automatic management

**Use Cases:**
1. Quarterly market rate communications to client tiers
2. Vendor process change notifications
3. Sector-specific content (e.g., healthcare trends to healthcare contacts)
4. Periodic value-add content to influencer lists (brokers, PMs)
5. Event invitations for major events (currently using personal emails or Paperless Post)

**Evidence:**
- "120,000 emails/month included" - "Way more than we would ever use"
- "Less than 6 campaigns per year"
- "if we did have a curated list of brokers and PM firms or CM firms, and, like, we did send out quarterly, oh, here's some market rates we're seeing"
- "NetSuite will manage that for you automatically" - subscription status
- "if they've unsubscribed and I need to tell them about a rate change, I can still send that"
- "MailChimp gets really pissed off when you try to load in Excel"

**Confidence Rating**: 95% - Requirements clearly stated with specific use cases

**BRD Requirements:**
- [REQUIREMENT] REQ-M002: Email marketing capability (minimal implementation) (ALIGNS)
- [REQUIREMENT] REQ-M009: Transactional vs. marketing email distinction (ALIGNS)
- [REQUIREMENT] REQ-M010: Quarterly targeted communications (ADAPT)
- [REQUIREMENT] REQ-M011: Personal email sending capability (ALIGNS)
- [REQUIREMENT] REQ-M004: Segmentation by multiple criteria (ACCOMMODATE)
- [PRIORITY] Should-Have: All email capabilities (low expected usage)

---

#### 3.4 How should leads be qualified and scored?

**Answer:**

**Current Qualification Process:**
Simple manual review by Jenny (Admin):
- Review web form submission
- Determine if legitimate business inquiry
- Check if existing client (route to account owner)
- Check if commercial furniture-related
- Decision: Route, qualify, or delete (most common)

**Business Development Approach:**
- BD GMs qualify relationship-based leads personally
- Often skip "lead" stage entirely
- Create opportunity directly with lead stage status
- "Most of our business development team actually creates it as an opportunity, and there is a lead stage under opportunity" - Kimmy

**Qualification Criteria (Implied):**

**Disqualify (Delete):**
- Consumer requests (residential furniture)
- Cleaning quotes
- Spam/junk
- Out of territory (if applicable)
- "A lot of cleaning quotes or 'I inherited my grandmother's Newell Eames chair and need a pad for it'"

**Basic Qualification:**
- Commercial/corporate furniture need
- Legitimate business contact
- Identifiable company

**Routing to Sales:**
- Existing client → Route to account owner
- New business in territory → Route to appropriate GM
- RFP received → Create opportunity

**Lead Scoring (Nice-to-Have, Not Required):**
NetSuite capability available but not emphasized:
- Could score based on:
  - Company size
  - Industry/sector
  - Title/role (decision maker vs. influencer)
  - Engagement (email opens, web activity)
  - Project timeline
  - Estimated value
  - Lead source (influencer referral = high score)

**However:**
Given relationship-based model and low web form volume, automated lead scoring is NOT a priority:
- Most valuable leads come through relationships (already "scored" by human judgment)
- Web leads mostly low value (will be deleted regardless of score)
- BD team prefers personal assessment
- Volume too low to benefit from automation

**Future State (Simple):**
1. Lead created (web or manual)
2. Auto-route based on simple rules:
   - Existing client? → Account owner
   - Territory assignment → Appropriate GM
   - Unknown → Jenny/admin queue
3. Manual review and qualification
4. Convert to opportunity or delete
5. Track lead source for attribution

**Evidence:**
- "Goes web form, lead creation… I qualify… most of the time… cleaning quote… then I delete" - Matt
- "Most of our business development team actually creates it as an opportunity, and there is a lead stage under opportunity" - Kimmy
- "Most of those are managed by our business development team... the general managers, like, their relationships" - Kimmy
- Lead scoring mentioned in questionnaire template capabilities but not discussed in transcript as a priority

**Confidence Rating**: 87% - Current process clear; scoring not emphasized as need

**BRD Requirements:**
- [FUNCTIONALITY] Simple lead qualification workflow (native capability)
- [FUNCTIONALITY] Lead routing based on rules (native capability)
- [FUNCTIONALITY] Lead scoring (available but low priority)
- [PRIORITY] Should-Have: Lead routing; Nice-to-Have: Lead scoring

---

#### 3.5 What campaign types do you need to execute?

**Answer:**

**Email Campaign Types (Minimal):**

**1. Quarterly Business Communications**
- **Target**: Existing clients, segmented by tier
- **Content**: Market rate updates, pricing changes, business updates
- **Frequency**: Quarterly or as-needed
- **Type**: Transactional (can send even if unsubscribed for important business info)
- **Sending**: From appropriate user or info@kbmhoag.com

**2. Vendor Communications**
- **Target**: Vendor contact list
- **Content**: Process changes, policy updates, requirements
- **Frequency**: As-needed (infrequent)
- **Type**: Transactional
- **Sending**: From Operations user or info@kbmhoag.com

**3. Sector-Specific Value Content (Aspirational)**
- **Target**: Specific sector contacts (e.g., healthcare A&D, brokers, clients)
- **Content**: Market trends, case studies, expertise demonstration
- **Frequency**: As-needed when sector trending up
- **Type**: Marketing (requires opt-in)
- **Example**: "Healthcare trending up → tailored message about healthcare expertise"

**4. Influencer Touchpoint Communications**
- **Target**: Curated lists (brokers, PM firms, CM firms)
- **Content**: Market rates, industry insights, value-add information
- **Frequency**: Quarterly
- **Type**: Marketing (requires opt-in)
- **Quote**: "if we did have a curated list of brokers and PM firms or CM firms, and, like, we did send out quarterly, oh, here's some market rates we're seeing, or something that we feel like would add value" - Kimmy

**5. Major Event Invitations (Occasional)**
- **Target**: Selected contact lists by event type
- **Content**: Event details, RSVP link
- **Frequency**: As-needed for major showroom events, product launches
- **Type**: Marketing
- **Note**: Most events use personal email invites, not mass campaigns

**Event Campaign Types (Low Priority):**

**6. Showroom Tours** (~2x/month)
- Current approach: Personal email invitations from GM
- Not mass campaigns
- Targeted 20-person lists
- May continue personal approach vs. campaigns

**7. Showroom Events**
- Cocktail receptions, product launches
- Currently using personal invites or Paperless Post
- Could use NetSuite if value identified

**Campaign Types NOT Needed:**
- Newsletter campaigns (discontinued)
- Content marketing campaigns
- Social media campaigns
- Lead nurturing drip campaigns (not their model)
- Promotional campaigns
- Product launch campaigns (to end users)
- Webinar campaigns

**Approach Philosophy:**
"we're being very selective of, like, hey, we want to invite these specific 20 people, and we're sending an email from a real person's email, rather than from info at KBM"

Low volume, high personalization, targeted segments

**Evidence:**
- "Less than 6 campaigns per year"
- "Discontinued quarterly newsletters (internal and external)"
- "if we did have a curated list of brokers and PM firms or CM firms, and, like, we did send out quarterly, oh, here's some market rates we're seeing"
- "Quarterly market rate communications to specific groups"
- "Vendor process change notifications"
- "probably doing something maybe twice a month at this point" (events)
- "we're being very selective... specific 20 people... email from a real person's email"

**Confidence Rating**: 93% - Campaign types clearly discussed with examples

**BRD Requirements:**
- [REQUIREMENT] REQ-M002: Minimal campaign execution capability (ALIGNS)
- [REQUIREMENT] REQ-M010: Quarterly targeted communications (ADAPT)
- [REQUIREMENT] REQ-M009: Transactional vs. marketing distinction (ALIGNS)
- [REQUIREMENT] REQ-M011: Personal email sending (ALIGNS)
- [PRIORITY] Nice-to-Have: Campaign capabilities (low expected usage)

---

### SECTION 4: MARKET INTELLIGENCE & ANALYTICS

#### 4.1 What market intelligence and analytics capabilities do you need?

**Answer:**

**Primary Need: Proactive Content Planning Based on Market Trends**

Current Gap: "if marketing had more insight into what some of those leads are and could see and track over time the sectors and how the market is changing, then it would be easier for that team to create proactively create content and target it"

**Required Market Intelligence Views:**

**1. Sector/Vertical Trend Analysis**
- Opportunities by sector over time
- Win/loss rates by sector
- Pipeline value by sector
- Sector performance trending up or down
- **Use Case**: "Identify sectors trending up (healthcare growing → create targeted content)"

**2. Territory/Market Performance**
- RFP volume by territory (SF/San Jose/Sacramento)
- Pipeline by GM territory
- Sector mix differences by geography
- Market-specific trends
- **Use Case**: Territory-specific messaging and content

**3. Early-Stage Opportunity Visibility**
- Pipeline from first identification (not just formal RFP)
- Marketing team can see incoming RFPs early
- Resource forecasting based on pipeline
- Proactive preparation vs. reactive
- **Current Pain**: "Marketing has no visibility until formal request submitted"

**4. RFP Performance Metrics**
- Projected volume vs. actual volume by submitter
- Win rates by project type
- Time to complete RFP by project size
- Marketing resource utilization
- **Use Case**: "we track what that projected volume is versus what the actual volume is, so that we can see, like, how many people are overestimating"

**5. Influencer Attribution (Aspirational)**
- Which influencers generating most opportunities?
- ROI by influencer relationship
- Event attendance → opportunity conversion
- Engagement patterns with influencers
- **Quote**: "it'd be so cool to see, like, the ROI of an investment on a relationship. like, I spent $6,000 on this person, and I got $3 million"

**6. Lead Source Analysis**
- Conversion rates by source (web, referral, event, influencer)
- Source performance over time
- Attribution to revenue
- **Current Gap**: No systematic tracking

**Dashboard Requirements:**

**Marketing Intelligence Dashboard:**
- Opportunities by sector (trend chart)
- RFP volume by market/territory
- Win/loss by sector
- Projected vs. actual volume (by estimator)
- Pipeline by stage and sector
- Sector performance YoY comparison

**Content Planning Dashboard:**
- Trending sectors (growing pipeline)
- Territory-specific opportunities
- Seasonal patterns (if any)
- Competitor mentions / loss reasons by sector

**Resource Planning Dashboard:**
- Incoming RFP volume (next 30/60/90 days)
- Marketing team capacity utilization
- Average RFP completion time
- Backlog and queue depth

**Analytics Capabilities Needed:**
- Drill-down from dashboard to opportunity detail
- Time-based trending (monthly, quarterly, YoY)
- Comparison views (territory vs. territory, sector vs. sector)
- Export to Excel for ad-hoc analysis
- Scheduled report delivery

**Value/Purpose:**
- **Proactive vs. Reactive**: Create content for growing sectors before RFPs arrive
- **Resource Allocation**: Staff appropriately based on pipeline visibility
- **Strategic Focus**: Identify which sectors, territories, influencers to prioritize
- **Competitive Intelligence**: Track win/loss patterns to improve approach
- **ROI Measurement**: Understand what's working (events, influencers, content)

**Evidence:**
- "if marketing had more insight into what some of those leads are and could see and track over time the sectors and how the market is changing, then it would be easier for that team to create proactively create content and target it"
- "Marketing has no visibility until formal request submitted"; "Can't proactively prepare"
- "we track what that projected volume is versus what the actual volume is"
- "it'd be so cool to see, like, the ROI of an investment on a relationship"
- Market intelligence dashboard described: "Opportunities by sector (trend over time)"; "RFP volume by market/territory"; "Win/loss by sector"

**Confidence Rating**: 92% - Clear needs stated with specific use cases

**BRD Requirements:**
- [REQUIREMENT] REQ-M019: Marketing pipeline visibility by sector (ACCOMMODATE)
- [REQUIREMENT] REQ-M020: Market intelligence dashboard (ACCOMMODATE)
- [REQUIREMENT] REQ-M021: Sector performance analysis (ACCOMMODATE)
- [REQUIREMENT] REQ-M015: Early RFP opportunity visibility for marketing (ACCOMMODATE)
- [REQUIREMENT] REQ-M016: RFP volume tracking (ACCOMMODATE)
- [PRIORITY] High: Market intelligence dashboards; Should-Have: Influencer ROI

---

## Outstanding Items Summary

**High Priority - Blocking Implementation:**
1. Define complete contact role taxonomy for segmentation (REQ-M006)
2. Define sector/vertical classification list (REQ-M007)
3. Establish territory assignment rules (REQ-M008)
4. Document RFP request form fields to replace Asana (REQ-M017)
5. Define market intelligence dashboard layout and metrics (REQ-M020)

**Medium Priority - Needed Before Go-Live:**
6. Document desired email templates from MailChimp (REQ-M012)
7. Define data quality validation rules (REQ-M005)
8. Clarify marketing team access permissions to opportunity data (REQ-M015)
9. Detail projected vs. actual volume tracking fields (REQ-M016)

**Low Priority - Post Go-Live Evaluation:**
10. Event management adoption and ROI (REQ-M014)
11. Customer satisfaction survey implementation (REQ-M022)
12. Influencer attribution model refinement (REQ-M011 related)

**Questions Requiring Clarification:**
1. What level of opportunity detail should marketing team see (full or summary)?
2. Should marketing team have access to all opportunities or only RFP-stage?
3. Which specific MailChimp templates should be recreated in NetSuite?
4. What is the exact governance for who can send mass emails?
5. Should Google Forms integration be pursued or continue as-is?

**Decisions Pending:**
1. Event management: Implement in Phase 1 or defer to future?
2. Surveys: Phase 1 capability or post-go-live evaluation?
3. Google Drive integration scope: All files or just specific types?
4. Philippines team time tracking integration with RFP records?

---

## Summary

This questionnaire documents KBM Hoag's unique marketing approach—relationship-based and RFP-focused rather than traditional demand generation. The Marketing transcript (Master_Transcript_Marketing.md) reveals a strategic business decision to move away from mass communications toward targeted, sector-specific, influencer-driven marketing.

**Key Themes:**
- **Marketing Philosophy**: Relationship-based, not campaign-driven
- **Core Function**: RFP response coordination, not demand generation
- **Critical Need**: Market intelligence and sector trend visibility for proactive content
- **Foundation Required**: Clean contact data with proper segmentation
- **Volume Reality**: Minimal email campaigns (<6/year); focus on quality over quantity
- **Implementation Approach**: Mostly ALIGNS and ADAPT with targeted ACCOMMODATIONs for segmentation, market intelligence, and RFP workflow

**Phase 1 Scope:**
- Enable (but don't over-invest in) email marketing capability
- Implement robust contact segmentation infrastructure
- Provide marketing visibility into pipeline/sector trends
- Replace Asana RFP workflow with NetSuite
- Replace MailChimp with NetSuite
- Defer event management and surveys to future evaluation

**Version 3.0 reflects comprehensive analysis of Master_Transcript_Marketing.md** with enhanced organization, clearer evidence attribution, and Marketing-specific focus (separate from CRM).

---

*End of Questionnaire v3.0*





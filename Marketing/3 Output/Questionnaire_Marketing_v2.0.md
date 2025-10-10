# Questionnaire - Marketing
**Version**: 2.0  
**Date**: 2025-10-02  
**Process Area**: Marketing & CRM (Lead Acquisition & Lead Management)

## Change Log
- **Date**: 2025-10-02
- **Version**: 2.0
- **Sources**: Marketing/2 Input/MRK & CRM Outline & Questionnaire; Marketing/2 Input/Transcript MRK&CRM
- **Summary**: Complete questionnaire analysis from discovery session with comprehensive requirement extraction, decision documentation, and evidence-based responses. Enhanced from v1.0 scaffold to fully populated analysis.

## PROCESSED FILES
- Marketing/2 Input/MRK & CRM Outline & Questionnaire
- Marketing/2 Input/Transcript MRK&CRM (Complete transcript analysis)

## Speaker Attribution Map
- **Matt** = Speaker 2 (Cornerstone/KBMH)
- **Jill Marsh** = General Manager (San Francisco office)
- **Alex Blangeres** = General Manager
- **Kate** = General Manager  
- **Kimmy** = Speaker 1 (Cornerstone/KBMH - likely leadership)
- **Speaker 3 (Cornerstone)** = Lead consultant/facilitator
- **Speaker 4 (Cornerstone)** = Consultant (Jillian - Marketing team member)
- **Speaker 5, 6, 7 (Cornerstone)** = Kip and other Cornerstone/KBMH team members
- **Carlos & Jillian** = Marketing-specific team members

## Decision Log

### Phase 1 Scope Decisions
- **REQ-001**: Minimal email marketing implementation in Phase 1 (ALIGNS) - "the capability is fine, and it's great to know that we can do it. It'll probably get underutilized compared to other market… other dealers" - Matt; "We won't plan for much there [email marketing]" - Speaker 3 (Cornerstone)

- **REQ-002**: Enable targeted segmentation by role, sector, and location (ADAPT) - "We want to be able to tailor those markets by location and by what their focus may be" - Speaker 2; "I need… to know how it works in terms of segmenting users and groups and the tagging" - Speaker 4 (Cornerstone)

- **REQ-003**: Manage opt-in/unsubscribe status natively in NetSuite (ALIGNS) - "NetSuite will manage that for you automatically" - Speaker 3 (Cornerstone); "if they've unsubscribed and I need to tell them about a rate change, I can still send that, even if they've unsubscribed" - Speaker 2

- **REQ-004**: Support curated broker/PM lists for periodic value communications (ADAPT) - "if we did have a curated list of brokers and PM firms or CM firms, and, like, we did send out quarterly, oh, here's some market rates we're seeing, or something that we feel like would add value, and it was easier, we didn't have to recreate the wheel every time, I could see us using it" - Kimmy

- **REQ-005**: Showroom event tracking and invitations (ALIGNS) - "you'll have the availability to do the email marketing inside of NetSuite" - Speaker 3 (Cornerstone); "we're probably doing something maybe twice a month at this point" - Jill Marsh

- **REQ-006**: Marketing visibility into leads/sectors for proactive content creation (ACCOMMODATE) - "if marketing had more insight into what some of those leads are and could see and track over time the sectors and how the market is changing, then it would be easier for that team to create proactively create targeted email material" - Speaker 4 (Cornerstone)

### Lead & Opportunity Management Decisions  
- **REQ-007**: Web form lead capture with routing (ALIGNS) - "We would keep the web forum. Because we have it today, and it serves a purpose, and it'd be weird to be a business without a web form" - Matt

- **REQ-008**: Lead progression to opportunity with stage tracking (ALIGNS) - "most of our business development team actually creates it as an opportunity, and there is a lead stage under opportunity" - Kimmy

- **REQ-009**: Opportunity stages matching current Zendesk workflow (ADAPT) - "LEAD RFP Awarded Programming Proposal Presented, on hold, order one, unqualified or closed loss" - Kimmy

- **REQ-010**: Restrict opportunity visibility to assigned team members only (ACCOMMODATE) - "people don't want other people to see their stuff... competition" - Jill Marsh; "we can restrict their opportunities to only the ones that they're on. It does that natively" - Speaker 3 (Cornerstone); "Don't create a thread that shows everything that's ever happening in Zend… or in NextWeek" - Matt

### Influencer & Event Tracking Decisions
- **REQ-011**: Track influencers (brokers, A&D firms, PMs) with ROI attribution (ACCOMMODATE) - "it'd be so cool to see, like, the ROI of an investment on a relationship. like, I spent $6,000 on this person, and I got $3 million. Okay, great" - Speaker 4 (Cornerstone); "we invited this person at 9 campaigns, I've never done anything with it, why do I keep inviting them?" - Matt

- **REQ-012**: Event attendance tracking linked to opportunities (ADAPT) - "if there's opportunities that are created and they're assigned as an influencer and the opportunity, you would have visibility into that" - Speaker 3 (Cornerstone)

- **REQ-013**: Expense tracking integration with influencer attribution (ACCOMMODATE) - "we do ask people on their expenses to list the attendees when they submit an expense, so if we can try Expensify or whatever we're using to pull that information to that… there's a matching contact in System, we could log all of them" - Matt

- **REQ-014**: Influencer contribution percentage with default even split (ACCOMMODATE) - "You should just default to an even, and then somebody would manipulate differently if they chose to do so" - Matt

### CRM & Pipeline Management Decisions
- **REQ-015**: Kanban board view for opportunity pipeline management (ALIGNS) - "I think it'd be a good tool for us to try and test out" - Matt

- **REQ-016**: Forecast reporting based on 70%+ probability only (ADAPT) - "we don't forecast anything below 70%. So whenever we say forecast, it's 70% or greater" - Kimmy

- **REQ-017**: Sales goals dashboard with progress bars by person and office (ACCOMMODATE) - "Yes. Yes. Okay, and we want it to be a… just a dashboard" - Matt; "I insisted on the progress bars last year" - Matt

- **REQ-018**: Volume and close date change alerts on dashboard (ACCOMMODATE) - "we'd love to be able to see a volume change, or if there was an order that was supposed to book in… it was going to order in January, and then we pushed it to February" - Jill Marsh

### Data & Reporting Decisions
- **REQ-019**: Import Zendesk historical data with tagging (ALIGNS) - "Export the entire [CSV]… import it and tag it" - Kip / Speaker 7 (Cornerstone)

- **REQ-020**: Eliminate company-wide activity feed to reduce internal competition (ACCOMMODATE) - "There is a company-wide feed, and it will show you every change that is made to every op chain" - Matt; "not having that activity thread visible, though, is for sure helpful" - Jill Marsh

- **REQ-021**: Duplicate detection at lead/opportunity creation (ALIGNS) - "if somebody fills it out similar, but they don't deny it, they just, they give you the option right then to merge it" - Speaker 3 (Cornerstone)

### Email & Communication Decisions
- **REQ-022**: Replace MailChimp manual uploads with NetSuite communications (ADAPT) - "MailChimp gets really pissed off when you try to load in Excel, because they think you're going to spam a bunch of people, and then most of it bounces anyways" - Matt

- **REQ-023**: Outlook/Gmail integration for email tracking to opportunities (ALIGNS) - "attach this to, you know, this email to an opportunity, or start tracking this conversation" - Speaker 3 (Cornerstone); "some of them have actually complained that it doesn't link right now, because they'd like to be able to track that activity within the system" - Matt

- **REQ-024**: Google Drive/SharePoint file integration to avoid storage limits (ACCOMMODATE) - "we're going to integrate with Google Drive, and it's just represented in NetSuite. It's not… it doesn't actually live in NetSuite" - Speaker 7 (Cornerstone); "then that's something we could definitely turn on, if it's just files that live within that trajectory to keep us out of the 100 [gigabytes]" - Matt

### RFP & Marketing Request Management Decisions
- **REQ-025**: RFP tracking with volume forecasting (ADAPT) - "we track what that projected volume is versus what the actual volume is, so that we can see, like, how many people are overestimating" - Speaker 4 (Cornerstone)

- **REQ-026**: Build marketing/RFP request forms in NetSuite tied to clients (ACCOMMODATE) - "Can we build an RFP request, or a marketing request, into NetSuite, Orion, and then also that be tied to the client... So, like, I can see every marketing request ever made for a client" - Matt; "we have the request engine, and it allows you to create any type of request form that you want inside of NetSuite" - Speaker 3 (Cornerstone)

### GP & Financial Tracking Decisions
- **REQ-027**: Global GP target of 22% with customer-level overrides (ACCOMMODATE) - "we have a target GP goal, which is 22%" - Matt; "a global GP percentage, target GP percentage... But then a field on the customer record" - Speaker 3 (Cornerstone)

- **REQ-028**: GP percentage defaults from customer record to opportunity (ACCOMMODATE) - "everything defaults to whatever we set them as a customer. So, like, we know with Google, it's always 12.5%, but they can also go… so any new thing they create will always be at 12.5%" - Matt

- **REQ-029**: Visual GP warning when below company goal (ACCOMMODATE) - "when they override it, if it's less than what our company goal is, it puts their GP in red... at the order level" - Matt

- **REQ-030**: Margin variance tracking with reason codes (ACCOMMODATE) - "if there's a negative and a positive, they're going to combine and then create a new total... we try to get the PCs to code them the same, the pickups the same as the hits, so that they become less of a financial impact" - Matt; "we have codes that go with that variance... is it a design error? Is it a customer accommodation? Vendor issue? Shipping" - Matt

## Action Items

ACTION: Provide current segmentation taxonomy (roles, sectors, locations for targeting)  
ASSIGNED TO: Marketing team (Speaker 4 / Jillian)  
DUE: Before design phase  
RELATED TO: REQ-002

ACTION: Confirm opt-in approach and unsubscribe handling for campaigns vs transactional emails  
ASSIGNED TO: Marketing lead  
DUE: Before Phase 1 implementation  
RELATED TO: REQ-003

ACTION: Provide list of opportunity statuses with probability percentages  
ASSIGNED TO: Matt or Kimmy  
DUE: ASAP  
RELATED TO: REQ-009, REQ-016

ACTION: Share inventory of existing reports and identify Phase 1 candidates  
ASSIGNED TO: Kip and team  
DUE: TBD  
RELATED TO: Multiple requirements

ACTION: Provide sales goals dashboard spreadsheet example  
ASSIGNED TO: Kip  
DUE: Before BRD creation  
RELATED TO: REQ-017

ACTION: Review and finalize variance/erosion reason code list  
ASSIGNED TO: Katie, Kip, Matt  
DUE: Before Phase 1  
RELATED TO: REQ-030

ACTION: Provide RFP request form inputs/requirements  
ASSIGNED TO: Marketing team (Speaker 4)  
DUE: TBD  
RELATED TO: REQ-026

ACTION: Share marketing-specific reports not in Kip's inventory  
ASSIGNED TO: Marketing team  
DUE: TBD  
RELATED TO: General reporting requirements

## Additional Sessions Needed

### Session: Segmentation Data Model & Ownership
- **Participants Needed**: Marketing lead (Jillian/Speaker 4), Sales leadership (Kimmy, GMs), CRM Admin
- **Questions to Address**:
  • Detailed taxonomy for role, sector, location tags
  • Data ownership and maintenance responsibilities
  • Data quality standards and enforcement
  • Integration with sales processes
- **Priority**: High (blocks REQ-002 implementation)
- **Suggested Duration**: 60-90 minutes
- **Dependencies**: REQ-002, REQ-006
- **Evidence**: "I personally need to… and need and want to know how it works in terms of segmenting users and groups and the tagging, and I think that that Would be… fall somewhere between marketing and sales, and be a collaborative effort there to really fine-tune that" - Speaker 4 (Cornerstone)

### Session: Influencer ROI & Attribution Model
- **Participants Needed**: Sales leadership, Finance, CRM Admin
- **Questions to Address**:
  • Attribution model parameters (even split vs weighted)
  • Expense tracking integration requirements
  • ROI reporting requirements
  • Campaign cost tracking methodology
- **Priority**: Medium (nice-to-have for Phase 1)
- **Suggested Duration**: 60 minutes
- **Dependencies**: REQ-011, REQ-013, REQ-014
- **Evidence**: "it'd be so cool to see, like, the ROI of an investment on a relationship" - Speaker 4 (Cornerstone); mentioned multiple times in context of tracking effectiveness

### Session: Reporting Requirements Review
- **Participants Needed**: Kip, Matt, Marketing team, Key report consumers
- **Questions to Address**:
  • Review all 36+ monthly reports
  • Identify Phase 1 critical reports
  • Map to NetSuite native vs custom
  • Prioritize custom report development
- **Priority**: High (impacts scope and timeline)
- **Suggested Duration**: 2 hours
- **Dependencies**: Multiple REQs
- **Evidence**: "We have 3 minutes... we basically started this project last year to talk about Okay, here's every report we're creating, who's looking at what, and are they actually still valid?" - Matt

## New Questions Identified

### Proposed New Question: M-NEW-01. What is the detailed taxonomy for segmenting contacts and leads by role, sector, and location?
- **Asked By**: Speaker 4 (Cornerstone)
- **Context**: Critical for targeted campaign execution
- **Suggested Placement**: Functional Requirements → Segmentation & Targeting
- **Evidence**: "I personally need to… and need and want to know how it works in terms of segmenting users and groups and the tagging"

### Proposed New Question: M-NEW-02. How should influencer contribution be attributed when multiple influencers are involved in a deal?
- **Asked By**: Speaker 3 (Cornerstone), discussed by team
- **Context**: Multiple influencers typically involved in deals
- **Suggested Placement**: Functional Requirements → Influencer Management
- **Evidence**: "it's everybody, because we're just one of many. Like, the influencer can be the PM, could also be the architect, it could also be the real estate broker, it could also be the client, like, it could be 5 people" - Matt

### Proposed New Question: M-NEW-03. What visibility restrictions are needed for opportunity and contact data?
- **Asked By**: Implied by team discussion of internal competition
- **Context**: Sales team competitiveness requires careful access controls
- **Suggested Placement**: Technical Requirements → Security & Access Control
- **Evidence**: "people don't want other people to see their stuff... competition" - Jill Marsh; extensive discussion of activity feed monitoring

### Proposed New Question: M-NEW-04. What are the specific inputs required for RFP/marketing request forms?
- **Asked By**: Matt
- **Context**: Replace Asana workflow with NetSuite request engine
- **Suggested Placement**: Functional Requirements → RFP Management
- **Evidence**: "Can we build an RFP request, or a marketing request, into NetSuite, Orion, and then also that be tied to the client"

## Questionnaire Responses

### Scope Confirmation
**Answer:** This discovery session covered both Marketing (Lead Acquisition & Email Marketing) and CRM (Lead Management, Opportunity Management, Influencer Tracking). The team acknowledged these areas are deeply intertwined for their business model. For BRD purposes, a combined Marketing+CRM document is recommended.

**Evidence:**
- "Marketing. Marketing and Lead Management. So, it's going to be on the technical side of marketing and lead management." - Speaker 2 (Cornerstone)
- "this kind of spills in a little bit into CRM again, but I think for your company, the topic… the two topics are really intertwined. They're the same. Yeah, marketing and CRM" - Speaker 3 (Cornerstone)

**Confidence Rating:** 95% - Explicitly stated and confirmed throughout session

**BRD Tags:** [DECISION] Combined Marketing+CRM scope; [CONSTRAINT] Intertwined processes require integrated solution

---

### 1. Current State Assessment

#### 1.1 Lead Generation & Capture

**Answer:**
Primary lead sources (in order of importance):
1. **Influencer-driven leads** (dominant source) - Relationships with brokers, A&D firms, project managers drive most opportunities
2. **RFPs through relationships** - Formal requests come through established influencer relationships
3. **Web form submissions** (minimal value) - Mostly cleaning quotes and one-off requests, occasional valuable existing client inquiries

**Current Process:**
- Web form leads route to Matt for qualification
- Most web form leads are low-value and deleted (cleaning quotes, one-off consumer requests)
- Influencer leads managed by business development GMs who own relationships
- RFPs trigger formal Asana requests to marketing team with volume projections

**Pain Points:**
- Manual qualification and routing
- No systematic tracking of influencer ROI
- Web form produces mostly noise
- Data entry inconsistency in Zendesk

**User Stories:**
- As Matt (Marketing lead), I need automated lead qualification so that I don't waste time on cleaning quote requests
- As a GM, I need to track which influencers are generating valuable opportunities so that I can focus relationship-building efforts effectively
- As a Marketing team member, I need visibility into lead sectors and trends so that I can create targeted content proactively

**Evidence:**
- "Goes web form, lead creation… I qualify… most of the time… cleaning quote… then I delete" - Matt
- "I did get one last week that was an existing client that just wrote cubicles. And I sent it to Chris, and it resulted in an order" - Matt
- "RFP will come in… relationship… formal project request through Asana to the marketing team" - Speaker 4 (Cornerstone)
- "Most of those are managed by our business development team... the general managers, like, their relationships. So they're the owners of all of that" - Kimmy

**Confidence Rating:** 95% - Multiple explicit statements with clear examples

**BRD Requirements:**
- [REQUIREMENT] Web form lead capture with auto-routing (ID: REQ-007, Type: Functional) [ALIGNS]
- [REQUIREMENT] Lead qualification workflow (ID: REQ-008, Type: Functional) [ALIGNS]
- [REQUIREMENT] Influencer relationship tracking with ROI metrics (ID: REQ-011, Type: Functional) [ACCOMMODATE]
- [CONSTRAINT] Low web form lead quality
- [PRIORITY] Must-Have: Lead capture; Should-Have: Influencer ROI tracking

#### 1.2 Current Tools & Platforms

**Answer:**
- **Zendesk**: Current CRM for opportunities and leads; retiring soon
- **MailChimp**: Email marketing (pay-as-go, used <6 times/year); manual list uploads problematic
- **Asana**: RFP and project request management; tracks volume projections vs actuals
- **Google Sheets**: Various tracking and reporting; RFP metrics; manual data compilation
- **Core**: Financial system; some customer data but not used for CRM
- **Paperless Post**: Event invitations for large events
- **Google Forms**: RSVP tracking when needed
- **Google Drive**: File storage and collaboration (preferred over other tools)

**Pain Points:**
- Multiple disconnected systems
- Manual data movement between systems
- MailChimp rejects Excel uploads (spam protection)
- No integrated view of customer interactions
- Heavy reliance on manual spreadsheet reporting

**Evidence:**
- "I think you guys are using MailChimp currently" - Speaker 3; "We buy credits when we need them. We don't have a monthly or annual subscription" - Matt
- "MailChimp gets really pissed off when you try to load in Excel, because they think you're going to spam a bunch of people, and then most of it bounces anyways" - Matt  
- "Business developer or account manager will put in a formal project request through Asana to the marketing team" - Speaker 4
- "We do everything in slides, so we'll create, like, an image, and then we'll just embed that into MailChimp" - Speaker 4

**Confidence Rating:** 92% - Explicit tool names and usage patterns described

**BRD Requirements:**
- [REQUIREMENT] Replace MailChimp with NetSuite email marketing (ID: REQ-022, Type: Functional) [ADAPT]
- [REQUIREMENT] Migrate Zendesk data to NetSuite (ID: REQ-019, Type: Non-Functional) [ALIGNS]
- [REQUIREMENT] Build RFP request forms in NetSuite to replace Asana (ID: REQ-026, Type: Functional) [ACCOMMODATE]
- [ASSUMPTION] Will maintain Google Drive for file collaboration
- [PRIORITY] Must-Have: Zendesk migration; Should-Have: Asana replacement

#### 1.3 Email Marketing Current State

**Answer:**
- Frequency: Less than 6 times per year
- Approach: Historically mass emails (quarterly newsletters, events); shifting to targeted approach
- Current limitations: One-size-fits-all messaging; no segmentation capability; manual list creation
- Strategy shift: Moving from mass to targeted campaigns by role, sector, location
- Event-based: Showroom events ~2x/month, usually selective invitation from personal emails vs. MailChimp

**Future Vision:**
- Curated broker/PM lists for quarterly market rate updates
- Sector-specific content based on market trends
- Location-specific messaging
- Role-based targeting

**Evidence:**
- "I would say less than 6 times a year, because we don't even have… We have a pay-as-we-go MailChimp" - Matt
- "We used to do a quarterly newsletter, internal and external. We used to do event... the information we got back from it was so little, so we've really refocused" - Matt
- "the GM strategic playlist last year has been all around targeted sectors, industries, and the people within them" - Matt
- "it is so rare that we're doing any sort of, like, email campaign, even for an event, because so much of what we do is relationship-based" - Speaker 4
- "if we did have a curated list of brokers and PM firms or CM firms, and, like, we did send out quarterly, oh, here's some market rates we're seeing... I could see us using it" - Kimmy

**Confidence Rating:** 93% - Clear description of current state and vision

**BRD Requirements:**
- [REQUIREMENT] Minimal Phase 1 email marketing scope (ID: REQ-001, Type: Non-Functional) [ALIGNS]
- [REQUIREMENT] Segmentation capability for future targeted campaigns (ID: REQ-002, Type: Functional) [ADAPT]
- [REQUIREMENT] Curated list management for brokers/PMs (ID: REQ-004, Type: Functional) [ADAPT]
- [RISK] Underutilization of email marketing features
- [PRIORITY] Nice-to-Have: Email marketing in Phase 1

#### 1.4 Lead Qualification Process

**Answer:**
Current process is informal and varies by person:
- Matt qualifies web form leads; mostly deletes (cleaning quotes, consumer requests)
- Existing client inquiries routed to appropriate GM or account manager
- BD team qualifies influencer-driven leads based on relationship context
- Variable data quality in Zendesk - some enter detailed info, others minimal
- Most opportunities created directly as "opportunity with lead stage" rather than separate lead record
- No standardized qualification criteria

**Progression:**
- Lead stage → RFP stage → Programming → Proposal Presented → Awarded/Closed Won or Closed Lost
- Probability assigned manually; not linked to stage in Zendesk

**Evidence:**
- "which comes to me, which then I qualify, and then I give it to one of the GMs, or I, if it's an existing client, give it to that person. But most of the time, it's people asking if they can give us a cleaning quote, which then I delete" - Matt
- "the amount of information that they decide to input on that lead in Zendesk varies widely. Like, some people will put activities or tasks or contacts in their lead in Zendesk, some people will not" - Kimmy
- "most of our business development team actually creates it as an opportunity, and there is a lead stage under opportunity" - Kimmy

**Confidence Rating:** 90% - Detailed description with examples

**BRD Requirements:**
- [REQUIREMENT] Lead to opportunity progression with stage tracking (ID: REQ-008, Type: Functional) [ALIGNS]
- [REQUIREMENT] Opportunity stages matching current workflow (ID: REQ-009, Type: Functional) [ADAPT]
- [CONSTRAINT] Informal qualification criteria; varies by person
- [PRIORITY] Must-Have: Stage progression

#### 1.5 Marketing Team & Roles

**Answer:**
Marketing team structure:
- Matt: Appears to be marketing/operations lead; handles web form leads, email communications
- Carlos & Jillian: Marketing-specific team members (mentioned as "marketing-specific")
- Marketing project manager: Schedules RFP kickoff calls
- Philippine team: Time tracking for RFP projects (6+ months into tracking)

Roles in process:
- Qualify incoming web form leads
- Respond to RFP requests from BD/sales team
- Create RFP materials and proposals
- Track RFP volume projections vs. actuals
- Time tracking by project for ROI analysis
- Create marketing content (use Google Slides for collaboration)

**Evidence:**
- "So everybody but Carlos and Jillian. Okay. They're marketing-specific" - Matt
- "the marketing project manager schedules a kickoff call with the key stakeholders to review" - Speaker 4
- "I get another report from a team that we have in the Philippines, and I'm getting their time entry on each project" - Speaker 4

**Confidence Rating:** 85% - Roles described but not comprehensive org chart

**Stakeholder Impact:**
- **Primary Users**: Marketing team (RFP creation, email campaigns, content)
- **Secondary Users**: BD team (lead entry, influencer tracking)
- **Approvers**: Matt, GMs (lead routing, campaign approval)

#### 1.6 Biggest Challenges with Lead Acquisition

**Answer:**
1. **Lack of segmentation** - Cannot target by role, sector, location; one-size-fits-all messaging
2. **Poor data quality** - Inconsistent Zendesk data entry; "poo in, poo out"
3. **No influencer ROI visibility** - Spending thousands on relationships with no measurable return
4. **Manual processes** - Spreadsheet reporting, manual email list uploads, disconnected systems
5. **Limited marketing visibility** - Marketing can't see lead trends to create proactive targeted content
6. **Internal competition issues** - Salespeople monitor activity feeds and compete for deals; limited information entry due to trust issues

**Pain Points by Stakeholder:**
- Marketing: Can't see sector trends; manual RFP tracking; no content targeting capability
- Sales/BD: Losing time to internal competition; no influencer ROI data; manual opportunity tracking
- Leadership: Can't measure relationship investment ROI; poor forecast accuracy tracking

**Evidence:**
- "right now we have a one-size-fits-all, so when we do send something out, it's the same package, no matter what your role is, or involvement with us... there's just really no way right now to target" - Speaker 2/4
- "if marketing had more insight into what some of those leads are and could see and track over time the sectors... then it would be easier for that team to create proactively create targeted email material" - Speaker 4
- "some of these people we've spent thousands of tens of thousands of dollars on, and they give us zero business" - Matt
- "we're able to create campaigns like you would in Salesforce and have targeted approach. We've just… the data entry part of it has never been clean enough to trust in" - Matt

**Confidence Rating:** 94% - Multiple explicit pain points with examples

**BRD Requirements:**
- [REQUIREMENT] Segmentation by role/sector/location (ID: REQ-002, Type: Functional) [ADAPT]
- [REQUIREMENT] Marketing visibility into leads/sectors (ID: REQ-006, Type: Functional) [ACCOMMODATE]
- [REQUIREMENT] Influencer ROI tracking (ID: REQ-011, Type: Functional) [ACCOMMODATE]
- [PRIORITY] Must-Have: Segmentation; Should-Have: ROI tracking

#### 1.7 Marketing Performance & ROI Tracking

**Answer:**
Current tracking is manual and limited:

**RFP Metrics** (manually tracked in spreadsheets by Jillian/marketing team):
- Projected volume vs. actual volume by salesperson
- Win rates by salesperson
- RFP volume generated by salesperson
- Time tracking by project (Philippines team - 6 months of data)
- Sector-based analysis (tech vs. healthcare vs. other)

**What's NOT tracked:**
- Influencer ROI (event spending vs. resulting opportunities)
- Email campaign effectiveness (limited usage means limited tracking)
- Event attendance to opportunity conversion
- Relationship investment to revenue attribution

**Reporting Challenges:**
- Manual compilation from multiple sources
- Lack of real-time visibility
- Can't correlate expense data to influencer relationships
- Takes months to gather enough data for trend analysis

**Evidence:**
- "we track what that projected volume is versus what the actual volume is, so that we can see, like, how many people are overestimating, what is this really" - Speaker 4
- "I get another report from a team that we have in the Philippines, and I'm getting their time entry on each project, so over time, I can see... here's the ROI that we're getting from their VIN" - Speaker 4
- "Before we even get to that stage, Jillian's doing a ton of data matrix and tracking at the RFP level, like what are individual salespeople's win rates based off the number of RFPs that they're coming in" - Matt
- "that's all being done by Jillian and her team putting that into spreadsheets and tracking that data" - Matt

**Confidence Rating:** 90% - Detailed description of manual tracking with clear gaps

**BRD Requirements:**
- [REQUIREMENT] RFP volume tracking and forecasting (ID: REQ-025, Type: Functional) [ADAPT]
- [REQUIREMENT] Influencer ROI reporting (ID: REQ-011, Type: Functional) [ACCOMMODATE]
- [REQUIREMENT] Win rate reporting by salesperson (ID: REQ-030+, Type: Functional) [ACCOMMODATE]
- [PRIORITY] Should-Have for Phase 1

---

### 2. Objectives & Strategy

#### 2.1 Overall Marketing Strategy & Lead Generation Goals

**Answer:**
Strategic shift from mass marketing to relationship-based, targeted approach:

**Current Strategy:**
- Relationship-driven lead generation (primary)
- Selective event hosting and attendance
- Minimal mass email marketing
- Focus on influencer relationships (brokers, A&D firms, PMs)

**Strategic Direction:**
- Target specific sectors showing growth (healthcare, tech, etc.)
- Location-based messaging (different markets: Alex, Jill, Kate offices)
- Role-based communication (brokers vs. PMs vs. A&D firms)
- Data-driven decision making (track what works)
- Relationship ROI measurement

**Lead Generation Goals:**
- Quality over quantity
- Influencer-driven opportunities (maintain as primary source)
- Better qualification to avoid wasted effort
- Track and optimize relationship investments

**Evidence:**
- "the GM strategic playlist last year has been all around targeted sectors, industries, and the people within them. So, mass emails like, the capability is fine, and it's great to know that we can do it. It'll probably get underutilized" - Matt
- "so much of what we do is relationship-based, and so we're being very selective of, like, hey, we want to invite these specific 20 people, and we're sending an email from a real person's email" - Speaker 4
- "We want to be able to tailor those markets by location and by what their focus may be" - Speaker 2

**Confidence Rating:** 92% - Clear strategic direction stated multiple times

**BRD Requirements:**
- [REQUIREMENT] Support targeted campaigns by segment (ID: REQ-002, Type: Functional) [ADAPT]
- [REQUIREMENT] Influencer relationship tracking (ID: REQ-011, Type: Functional) [ACCOMMODATE]
- [PRIORITY] Must-Have: Segmentation foundation

#### 2.2 Campaign Types & Frequency

**Answer:**
**Email Campaigns** (minimal usage):
- Frequency: <6 times per year currently
- Types: Quarterly newsletters (discontinued), event invitations (rare), operational communications (rate changes, process updates)
- Future potential: Quarterly market rate updates to broker/PM lists

**Event Campaigns** (primary marketing activity):
- Showroom events: ~2x/month
- Types: Showroom tours, finish reviews, client presentations, cocktail events
- Approach: Selective invitation lists; personal outreach preferred over mass invitation

**Operational Communications** (not via MailChimp):
- Rate changes to clients
- Process updates to vendors
- Customer service surveys
- Sent from personal emails (Matt's email) - causing bounce management issues

**Seasonality:**
- No strong seasonal patterns mentioned
- Event-driven rather than calendar-driven

**Evidence:**
- "I would say less than 6 times a year" - Matt
- "we're probably doing something maybe twice a month at this point" - Jill Marsh (re: showroom events)
- "We used to do a quarterly newsletter, internal and external" - Matt
- "if we need to email just clients a change in rates, or if we need to email vendors a change in process" - Matt

**Confidence Rating:** 91% - Clear frequency and types described

**BRD Requirements:**
- [REQUIREMENT] Email marketing for operational + rare campaigns (ID: REQ-001, REQ-022, Type: Functional) [ALIGNS/ADAPT]
- [REQUIREMENT] Event management and tracking (ID: REQ-005, REQ-012, Type: Functional) [ALIGNS/ADAPT]
- [PRIORITY] Nice-to-Have: Event tracking; Must-Have: Operational email capability

#### 2.3 Target Markets & Buyer Personas

**Answer:**
**Industries/Sectors:**
- Technology (significant but volatile)
- Healthcare
- Education
- Contract/Commercial office furniture
- Various other commercial sectors

**Geographic Markets:**
- Multiple office locations with different market focuses
- Alex's market, Jill's market (San Francisco), Kate's market - each different
- California-based with multiple metro areas

**Key Personas:**
1. **Brokers** - Real estate brokers involved in tenant improvements
2. **A&D Firms** - Architects and designers specifying furniture
3. **Project Managers / Construction Managers** - Managing overall projects
4. **Direct Clients** - End customers (existing relationships primarily)
5. **Influencer Contacts** - Junior staff who may become future specifiers

**Relationship Categories:**
- Existing clients (recurring business)
- Influencer network (generates majority of opportunities)
- New prospects (minimal from web form)

**Evidence:**
- "Alex's market is different than Jill's market, which is different from Kate's market, so we want to be able to tailor those markets by location" - Speaker 2
- "If we could see, like, okay, here's all of our contacts in the broker world" - Speaker 4
- "healthcare and contract work is very different than tech. It's just night and day" - Speaker 4
- "Gensler... they send all of their junior non-specifiers, instead of the people that could actually give us business. there's still opportunity there, but the opportunity changes, so then how do we track all those people?" - Matt

**Confidence Rating:** 88% - General sectors clear; specific personas implied more than explicitly defined

**BRD Requirements:**
- [REQUIREMENT] Segmentation by role (broker, A&D, PM, client, etc.) (ID: REQ-002, Type: Functional) [ADAPT]
- [REQUIREMENT] Sector tracking and reporting (ID: REQ-025, Type: Functional) [ADAPT]
- [PRIORITY] Must-Have: Role/sector segmentation capability

#### 2.4 Key Marketing KPIs & Success Metrics

**Answer:**
**Current KPIs (manually tracked):**
- RFP win rate by salesperson
- Projected vs. actual volume on RFPs
- Time investment per RFP/project
- Volume by sector
- Bookings by salesperson (weekly tracking)

**Desired KPIs (not currently tracked):**
- Influencer ROI (spend vs. resulting opportunities)
- Event attendance to opportunity conversion
- Relationship investment effectiveness
- Forecast accuracy by individual
- Campaign effectiveness (when campaigns resume)

**Sales KPIs (from discussion):**
- Revenue volume
- GP percentage (goal: 22% company-wide)
- Margin erosion/variance
- Forecast accuracy (70%+ probability opportunities)
- Quota attainment

**Evidence:**
- Multiple discussions of manual RFP tracking by Jillian
- "we're spending this many hours on each of these stakeholders, and here's the ROI that we're getting from their VIN" - Speaker 4
- "some of these people we've spent thousands of tens of thousands of dollars on, and they give us zero business" - Matt
- Discussion of sales goals dashboard with progress bars

**Confidence Rating:** 87% - Current manual tracking clear; desired metrics strongly implied

**BRD Requirements:**
- [REQUIREMENT] RFP metrics dashboard (ID: REQ-025, Type: Functional) [ADAPT]
- [REQUIREMENT] Influencer ROI reporting (ID: REQ-011, Type: Functional) [ACCOMMODATE]
- [REQUIREMENT] Sales goals tracking with dashboard (ID: REQ-017, Type: Functional) [ACCOMMODATE]
- [PRIORITY] Must-Have: Sales goals; Should-Have: RFP metrics; Nice-to-Have: Influencer ROI

---

### 3. Functional Requirements

#### 3.1 Lead Capture Methods Needed

**Answer:**
1. **Web form integration** - Contact us form embedded on website, creates lead in NetSuite with auto-routing
2. **Manual lead creation** - BD team and account managers create leads/opportunities from relationship discussions
3. **Quick Add Lead (mobile)** - For on-the-go lead capture by sales team
4. **Influencer-sourced leads** - Track lead source as specific influencer contact

**Requirements:**
- Form embedded in website (NetSuite form)
- Auto-route to Matt or appropriate GM based on criteria
- Capture lead source (web form, influencer, RFP, etc.)
- Mobile-friendly lead creation
- Ability to link lead to influencer contact

**Evidence:**
- "you probably have a contact us form on your site. Well, that can actually be our form embedded in your site, and if somebody fills it out, it creates a lead inside of NetStream" - Speaker 3
- "Quick Add Lead, Quick Add Up... On the mobile phone" - Speaker 3
- "We would keep the web forum. Because we have it today, and it serves a purpose" - Matt

**Confidence Rating:** 93% - Explicit requirements stated

**BRD Requirements:**
- [REQUIREMENT] Web form lead capture (ID: REQ-007, Type: Functional) [ALIGNS]
- [REQUIREMENT] Manual lead creation by BD/sales (ID: REQ-008, Type: Functional) [ALIGNS]
- [REQUIREMENT] Mobile quick add capability (ID: New, Type: Functional) [ALIGNS]
- [PRIORITY] Must-Have: Web form and manual creation; Nice-to-Have: Mobile

#### 3.2 Information Collection from Prospects

**Answer:**
**Minimum required (from current Zendesk practice):**
- Company name
- Contact name (though some salespeople only enter first name)
- Contact information (email, phone)
- Lead source
- Basic project description
- Estimated value
- Probability/stage

**Desired but not consistently captured:**
- All influencer contacts involved
- Detailed activities and interactions
- Sector/industry
- Role (broker, A&D, PM, client, etc.)
- Location/market

**Flexibility Needed:**
- High performers allowed more flexibility on data entry
- "if you are productive... rules can look different" - Matt
- Required fields should be minimal to avoid BD resistance

**Evidence:**
- "the amount of information that they decide to input on that lead in Zendesk varies widely" - Kimmy
- "if you're really successful and you're only putting in a first name and not a last name. I'd be okay with that" - Matt
- Discussion of needing role/sector/location for segmentation

**Confidence Rating:** 89% - Current minimal requirements clear; desired fields implied from segmentation needs

**BRD Requirements:**
- [REQUIREMENT] Flexible data capture with minimal required fields (ID: Related to REQ-008, Type: Functional) [ADAPT]
- [REQUIREMENT] Segmentation fields (role, sector, location) (ID: REQ-002, Type: Functional) [ADAPT]
- [PRIORITY] Must-Have: Basic contact/company; Should-Have: Segmentation fields

#### 3.3 Email Marketing Capabilities Required

**Answer:**
**Phase 1 (Minimal):**
- Basic email campaign creation (image-based acceptable)
- Subscription/opt-in status management (automatic)
- Unsubscribe management (automatic)
- Separate transactional email capability (outside campaign function)
- Email to groups/lists from NetSuite
- Ability to send from "info@" address or personal addresses

**Future/Nice-to-Have:**
- Template creation (currently use Google Slides → image → embed)
- Segmented list creation by role/sector/location
- Campaign response tracking
- Email sent from NetSuite tracked back to opportunity

**Not Needed:**
- Advanced email builder
- Complex automation/drip campaigns
- High-volume sending (within 120K/month limit)

**Evidence:**
- "the capability is fine, and it's great to know that we can do it. It'll probably get underutilized compared to other market… other dealers" - Matt
- "NetSuite will manage that for you automatically" - Speaker 3 (re: opt-in/unsubscribe)
- "if they've unsubscribed and I need to tell them about a rate change, I can still send that... You could send it directly to them from inside NetSuite, and not through the email campaign function" - Speaker 3
- "We just need, like, an image with a link that says RSVP" - Speaker 4

**Confidence Rating:** 94% - Very explicit about minimal needs

**BRD Requirements:**
- [REQUIREMENT] Basic email marketing capability (ID: REQ-001, Type: Functional) [ALIGNS]
- [REQUIREMENT] Opt-in/unsubscribe management (ID: REQ-003, Type: Non-Functional) [ALIGNS]
- [REQUIREMENT] Transactional vs. campaign email separation (ID: REQ-003, Type: Functional) [ALIGNS]
- [PRIORITY] Nice-to-Have for Phase 1

#### 3.4 Lead Qualification & Scoring

**Answer:**
**Current Approach (informal):**
- Matt manually qualifies web form leads (mostly deletes)
- BD team qualifies relationship-driven leads based on knowledge/intuition
- No formal scoring system
- Progression based on stage advancement

**Stage-Based Progression:**
- Lead → RFP → Programming → Proposal Presented → Awarded/Closed
- Each stage has implied probability (to be provided in separate action item)
- 70%+ probability = "forecast" stage
- Unqualified leads deleted rather than marked as such

**Not Required:**
- Automated lead scoring
- Complex qualification rules
- Point-based scoring systems

**Preferred:**
- Simple stage-based approach
- Manual qualification decisions
- Ability to quickly disqualify/delete noise

**Evidence:**
- "which comes to me, which then I qualify... most of the time... cleaning quote... then I delete" - Matt
- "we don't forecast anything below 70%" - Kimmy
- Discussion of current stages: "LEAD RFP Awarded Programming Proposal Presented, on hold, order one, unqualified or closed loss"

**Confidence Rating:** 91% - Clear that current informal approach works for them

**BRD Requirements:**
- [REQUIREMENT] Stage-based opportunity progression (ID: REQ-009, Type: Functional) [ADAPT]
- [REQUIREMENT] Probability linked to stages (ID: REQ-016, Type: Functional) [ADAPT]
- [ASSUMPTION] No automated lead scoring needed
- [PRIORITY] Must-Have: Stage progression

#### 3.5 Campaign Types to Execute

**Answer:**
**Required Campaign Types:**
1. **Showroom Events** - Tours, finish reviews, client meetings, cocktail events (~2x/month)
2. **Operational Communications** - Rate changes, process updates, surveys to specific groups
3. **Periodic Value Content** (future) - Quarterly market rate updates to broker/PM lists
4. **Targeted Sector Communications** (future) - Healthcare, tech, education-specific messaging

**Campaign Management Needs:**
- Create invitation lists by criteria (role, sector, relationship level)
- Track invitations sent vs. attendance (when tracking desired)
- Link event attendance to future opportunities
- Manage RSVP if needed (though many events don't track)

**Not Needed:**
- Complex multi-touch drip campaigns
- Automated nurture sequences
- High-frequency campaigns

**Evidence:**
- "showroom events... we're probably doing something maybe twice a month" - Jill Marsh
- "if we did have a curated list of brokers and PM firms... send out quarterly, oh, here's some market rates we're seeing" - Kimmy
- "if we need to email just clients a change in rates, or if we need to email vendors a change in process" - Matt

**Confidence Rating:** 90% - Types clear from current practice and stated desires

**BRD Requirements:**
- [REQUIREMENT] Event invitation and tracking (ID: REQ-005, REQ-012, Type: Functional) [ALIGNS/ADAPT]
- [REQUIREMENT] Operational/transactional email capability (ID: REQ-022, Type: Functional) [ADAPT]
- [REQUIREMENT] List management for curated groups (ID: REQ-004, Type: Functional) [ADAPT]
- [PRIORITY] Should-Have: Event tracking; Must-Have: Email capability

#### 3.6 Lead Assignment to Sales Reps

**Answer:**
**Current Assignment Logic:**
- Web form leads → Matt for qualification → Routes to appropriate GM or account manager
- Existing client inquiries → Route to assigned account manager
- Influencer-driven leads → Stay with the BD rep who owns that relationship
- New opportunities → Created by BD rep, stays with them unless handed to account manager

**Assignment Factors:**
- Existing client relationship (primary)
- Geographic territory (each GM has market)
- Relationship ownership (who brought the lead)
- Account manager vs. BD role (different workloads/specializations)

**Complexity:**
- Not simple round-robin
- Relationship-based, not rule-based
- Manual decision in many cases
- Handoff from BD to account manager when project progresses

**Evidence:**
- "which then I qualify, and then I give it to one of the GMs, or I, if it's an existing client, give it to that person" - Matt
- "Depends on which account manager. There's some that mimic closer to business development, there's some that... bit closer to sales support" - Speaker 2
- Discussion of BD creating opportunity then handing to account manager

**Confidence Rating:** 89% - Process clear but rules are informal/relationship-based

**BRD Requirements:**
- [REQUIREMENT] Manual assignment capability with routing suggestions (ID: Related to REQ-007/008, Type: Functional) [ADAPT]
- [ASSUMPTION] Automated assignment rules not needed initially
- [PRIORITY] Must-Have: Manual assignment; Nice-to-Have: Territory-based suggestions

#### 3.7 Approval Processes for Campaigns

**Answer:**
**Current Approval:**
- Informal approval process
- Marketing team creates materials
- Presumably Matt or GM approves before send
- No formal approval workflow mentioned

**Future Needs (implied):**
- Approval for large expense variances ($1,500+ threshold mentioned for project variances)
- May want approval for mass email sends
- Event budget approvals (likely outside NetSuite)

**Not Discussed in Detail:**
- Specific campaign approval workflow
- Budget approvals within CRM
- Content approval process

**Evidence:**
- Limited direct discussion
- "$1,500" threshold mentioned for variance approval
- General collaborative approach implied

**Confidence Rating:** 70% - Insufficient evidence; requires follow-up

**BRD Requirements:**
- [ASSUMPTION] Formal campaign approval workflow not required Phase 1
- [REQUIREMENT] Potentially variance approval workflow (ID: Related to REQ-030, Type: Functional) [ACCOMMODATE]
- [PRIORITY] Nice-to-Have

#### 3.8 Segmentation & Targeting Capabilities

**Answer:**
**Critical Requirement - High Priority:**

**Segmentation Dimensions Needed:**
1. **Role** - Broker, A&D firm, Project Manager, Client contact, Vendor, etc.
2. **Sector** - Healthcare, Technology, Education, Contract, etc.
3. **Location/Market** - By office territory, by client location
4. **Relationship Level** - Existing client, active prospect, past prospect, influencer
5. **Contact Type** - Decision maker, influencer, junior staff (future potential)

**Usage:**
- Create targeted email lists
- Filter opportunities for analysis
- Track sector trends over time
- Enable marketing to see what sectors are active
- Location-specific messaging

**Data Ownership:**
- Collaborative between sales and marketing
- Sales owns relationship data entry
- Marketing needs visibility to create content

**Critical Challenge:**
- Data quality dependency - "poo in, poo out"
- Need clear taxonomy and enforcement
- Needs to be easy or BD won't use it

**Evidence:**
- "We want to be able to tailor those markets by location and by what their focus may be" - Speaker 2
- "I personally need to… and need and want to know how it works in terms of segmenting users and groups and the tagging, and I think that that Would be… fall somewhere between marketing and sales" - Speaker 4
- "if marketing had more insight into what some of those leads are and could see and track over time the sectors and how the market is changing" - Speaker 4
- "right now we have a one-size-fits-all, so when we do send something out, it's the same package, no matter what your role is" - Speaker 2

**Confidence Rating:** 95% - Extremely clear need stated multiple times

**BRD Requirements:**
- [REQUIREMENT] Multi-dimensional segmentation (role, sector, location) (ID: REQ-002, Type: Functional) [ADAPT]
- [REQUIREMENT] Marketing visibility to segment data (ID: REQ-006, Type: Functional) [ACCOMMODATE]
- [REQUIREMENT] Collaborative sales+marketing data ownership (ID: Related to REQ-002, Type: Process) [ADAPT]
- [CONSTRAINT] Data quality dependent on user adoption
- [RISK] If too complex, BD won't use it
- [PRIORITY] Must-Have - foundational for strategy

---

### 4. Technical Requirements

#### 4.1 System Integration Needs

**Answer:**
**Required Integrations:**
1. **Outlook/Gmail** - Email tracking to opportunities; calendar sync; contact creation from email
2. **Google Drive** - File linking (via hyperlinks in custom fields) to avoid storage limits
3. **SharePoint** (potential) - File storage for NetSuite-linked documents to manage 100GB limit
4. **Expensify** (or expense system) - Pull attendee information to link expenses to influencer contacts
5. **Zendesk** (temporary) - Data export/import for migration

**Nice-to-Have Integrations:**
- DocuSign (mentioned as possibility)
- Request forms for RFP intake (built in NetSuite, replacing Asana)

**Not Needed:**
- Salesforce integration
- MailChimp integration (replacing entirely)

**Evidence:**
- "the Outlook integration, basically... create records within NetSuite... if something comes in, and it is in any way able to be tied directly to NetSuite will update that worker to create new records" - Speaker 5/7
- "there's a SharePoint, and we're double-checking on the Google Drive integration, where you're setting up your entire folder structure there, you drag and drop into it" - Speaker 7
- "we do ask people on their expenses to list the attendees when they submit an expense, so if we can try Expensify or whatever we're using to pull that information" - Matt

**Confidence Rating:** 92% - Explicit integration requirements stated

**BRD Requirements:**
- [REQUIREMENT] Outlook/Gmail email integration (ID: REQ-023, Type: Technical) [ALIGNS]
- [REQUIREMENT] Google Drive file linking (ID: REQ-024, Type: Technical) [ACCOMMODATE]
- [REQUIREMENT] SharePoint integration for document storage (ID: REQ-024, Type: Technical) [ACCOMMODATE]
- [REQUIREMENT] Expense system integration (ID: REQ-013, Type: Technical) [ACCOMMODATE]
- [PRIORITY] Must-Have: Outlook; Should-Have: Google Drive linking; Nice-to-Have: Expense integration

#### 4.2 Data Migration from Current Tools

**Answer:**
**Zendesk Migration:**
- Export entire database as CSV
- Import to NetSuite
- Tag as historical data
- Maintain opportunity history and relationships

**Data Elements to Migrate:**
- Opportunities (all stages, including closed)
- Contacts
- Companies/Accounts
- Influencer relationships (if captured)
- Activity history (if feasible)
- Opportunity stages and probability

**Migration Approach:**
- CSV export from Zendesk
- Import mapping to NetSuite fields
- Tag all migrated records as "Zendesk import"
- Accept that some data cleanup will be needed post-migration

**Not Migrating:**
- MailChimp data (minimal; mostly start fresh)
- Asana RFP data (historical; not CRM data)

**Evidence:**
- "You can export the entire... CSV... import it and tag it" - Kip / Speaker 7
- "Are we able to integrate Zendesk before it retires and save all that data down, or do we have to just give all that up when Zendesk goes away?" - Matt

**Confidence Rating:** 90% - Clear migration plan for Zendesk

**BRD Requirements:**
- [REQUIREMENT] Zendesk CSV import with historical tagging (ID: REQ-019, Type: Non-Functional) [ALIGNS]
- [RISK] Data mapping challenges; duplicate detection
- [PRIORITY] Must-Have

#### 4.3 Email Volume & Deliverability Requirements

**Answer:**
**Volume:**
- Current: <6 email campaigns per year
- 120,000 emails/month limit (NetSuite standard) far exceeds needs
- Typical campaign size: Likely hundreds to low thousands (based on curated lists discussion)
- Operational emails: Occasional, to specific groups (all clients, all vendors, etc.)

**Deliverability:**
- Need to send from recognizable addresses (company domain)
- Option to send from personal addresses for relationship emails
- Need unsubscribe tracking to maintain compliance
- Bounce management
- Avoid spam filters (current MailChimp Excel upload issue)

**Compliance:**
- CAN-SPAM compliance
- Opt-in/unsubscribe management
- Distinction between transactional (no opt-in required) and marketing (opt-in required)

**Evidence:**
- "you get 120,000 emails a month... Way more than we would ever use" - Speaker 3 / Matt
- "I would say less than 6 times a year" - Matt
- "MailChimp gets really pissed off when you try to load in Excel, because they think you're going to spam a bunch of people, and then most of it bounces anyways" - Matt
- "if it's… if it's, like, transactional communication, or informational communication related to orders or anything like that, you don't… they don't have to opt into that" - Speaker 3

**Confidence Rating:** 93% - Clear volume parameters and compliance needs

**BRD Requirements:**
- [REQUIREMENT] Email subscription status management (ID: REQ-003, Type: Non-Functional) [ALIGNS]
- [REQUIREMENT] Transactional vs. campaign email separation (ID: REQ-003, Type: Functional) [ALIGNS]
- [REQUIREMENT] Bounce management (ID: Related to REQ-022, Type: Non-Functional) [ALIGNS]
- [PRIORITY] Must-Have: Compliance management

#### 4.4 Marketing Data Flow to Other Systems

**Answer:**
**Primary Data Flow:**
- Marketing/CRM → Projects → Finance (Core → NetSuite)
- Opportunity won → Sales Order → Project → Billing
- Contact/company data → Shared across all modules
- Activity data → Tied to opportunities and customers

**Key Integration Points:**
- Opportunity closes → Becomes sales order/project in NetSuite
- Customer data created in CRM → Available in finance/project modules
- Email communications → Tracked against customer/opportunity records
- Time tracking → Project records (RFP time from Philippines team)

**Reporting Flows:**
- CRM data → Sales dashboards
- Project data → GP tracking and variance reporting
- Opportunity forecast → Weekly bookings report

**Not Discussed in Detail:**
- Real-time sync requirements
- Batch vs. real-time processing preferences

**Evidence:**
- "if it's closed one, it moves over to core" - Matt (re: current Zendesk to Core flow)
- Discussion of opportunity flowing to project to billing
- Extensive discussion of project GP tracking and variance codes

**Confidence Rating:** 87% - General flow clear; specific technical requirements need more detail

**BRD Requirements:**
- [REQUIREMENT] Opportunity to sales order conversion (ID: Standard NetSuite, Type: Functional) [ALIGNS]
- [REQUIREMENT] Unified customer data across modules (ID: Standard NetSuite, Type: Technical) [ALIGNS]
- [PRIORITY] Must-Have

#### 4.5 Compliance Requirements (CAN-SPAM, GDPR)

**Answer:**
**CAN-SPAM Requirements:**
- Opt-in tracking and management
- Unsubscribe capability (automated)
- Distinction between transactional and marketing emails
- Ability to send transactional emails to unsubscribed contacts
- From address must be company domain

**Current Compliance Approach:**
- Emails to existing business relationships (not purchased lists)
- Manual tracking of unsubscribes in MailChimp
- Incremental list updates to avoid re-emailing unsubscribed contacts

**GDPR:**
- Not explicitly discussed
- Company appears to be US-based with US clients primarily
- May not be primary concern

**Compliance Needs in NetSuite:**
- Automatic subscription status management
- Unsubscribe link in all campaign emails
- Option to exclude unsubscribed from campaigns automatically
- Ability to override for transactional messages

**Evidence:**
- "if it's… if it's, like, transactional communication, or informational communication related to orders or anything like that, you don't… they don't have to opt into that. It's only when you're going to be doing some type of email campaign" - Speaker 3
- "NetSuite will manage that for you automatically" - Speaker 3 (re: unsubscribe)
- "their email addresses from people that we've done business with, so… it's not like we're buying a little…" - Matt

**Confidence Rating:** 88% - CAN-SPAM needs clear; GDPR not discussed

**BRD Requirements:**
- [REQUIREMENT] Automated opt-in/unsubscribe management (ID: REQ-003, Type: Non-Functional) [ALIGNS]
- [REQUIREMENT] Separate transactional email capability (ID: REQ-003, Type: Functional) [ALIGNS]
- [PRIORITY] Must-Have for Phase 1

#### 4.6 API Integrations with External Tools

**Answer:**
**Not Explicitly Required:**
- Most integrations are native NetSuite capabilities (Outlook, SharePoint)
- File linking to Google Drive via hyperlinks (no API needed)
- Expense system integration (Expensify) - approach TBD

**Potential Future APIs:**
- Expense system (pull attendee data)
- Event management tools (if not using NetSuite native)
- DocuSign (mentioned as possibility)

**Current Approach:**
- Prefer native NetSuite functionality
- Use hyperlinks for external file references
- Manual processes acceptable for infrequent activities

**Evidence:**
- Most integration discussion focused on native NetSuite capabilities
- "I could still have somewhere that would allow me to insert links back to Google Drive for easy connection" - Matt

**Confidence Rating:** 75% - Not a primary focus of discussion; needs more exploration

**BRD Requirements:**
- [ASSUMPTION] Native NetSuite integrations sufficient for Phase 1
- [REQUIREMENT] Expense system integration (future) (ID: REQ-013, Type: Technical) [ACCOMMODATE]
- [PRIORITY] Nice-to-Have for future phases

#### 4.7 Performance & Scalability Needs

**Answer:**
**Scale:**
- User count: Approximately 30-50 users (implied from discussion of offices and roles)
- Contact database: Unknown size but manageable (migrate from Zendesk)
- Opportunity volume: Sufficient to require weekly tracking
- Email volume: Very low (<6 campaigns/year)

**Performance Expectations:**
- Real-time dashboard updates for sales goals
- Quick opportunity lookup to check for duplicates
- Fast mobile lead creation
- Responsive Kanban board views

**Not Discussed:**
- Specific response time requirements
- Concurrent user counts
- Growth projections

**Scalability Considerations:**
- 100GB file storage limit will be issue → mitigate with SharePoint/Google Drive linking
- Standard NetSuite performance appears acceptable

**Evidence:**
- Limited direct discussion of performance
- File storage limit concern: "Well, that's not very much... because we could fill that, like, 40 times over the email" - Matt

**Confidence Rating:** 70% - Limited discussion; standard NetSuite performance likely sufficient

**BRD Requirements:**
- [ASSUMPTION] Standard NetSuite performance acceptable
- [REQUIREMENT] File storage strategy (SharePoint/Google Drive) (ID: REQ-024, Type: Technical) [ACCOMMODATE]
- [PRIORITY] Must-Have: File storage strategy

---

### 5. Implementation Alignment / Approach Classification

**Answer:**
Classification of all requirements by implementation approach:

**ALIGNS (12 requirements):** REQ-001, REQ-003, REQ-005, REQ-007, REQ-008, REQ-015, REQ-019, REQ-021, REQ-023, REQ-024 (partial), REQ-022 (partial), plus several technical requirements

**ADAPT (8 requirements):** REQ-002, REQ-004, REQ-009, REQ-012, REQ-016, REQ-022, REQ-025, others related to process changes without customization

**ACCOMMODATE (10 requirements):** REQ-006, REQ-010, REQ-011, REQ-013, REQ-014, REQ-017, REQ-018, REQ-020, REQ-024, REQ-026, REQ-027, REQ-028, REQ-029, REQ-030

**Key Implementation Decisions:**
- Phase 1 marketing focus: Minimal (ALIGNS) - "won't plan for much there"
- Segmentation: Process adaptation required (ADAPT) - need data entry discipline
- Influencer ROI: Custom reporting and tracking (ACCOMMODATE) - solution design needed
- Sales dashboards: Custom development (ACCOMMODATE) - recreate existing reports
- Access controls: Custom permissions (ACCOMMODATE) - unique competitive environment

**Evidence:**
- See Decision Log section for all quotes
- Detailed discussions of each requirement with clear decisions

**Confidence Rating:** 92% - Classifications based on explicit statements about standard vs. custom needs

---

## Outstanding Items Summary

### High Priority Gaps Requiring Follow-up:
1. **Segmentation taxonomy** - Need detailed role, sector, location values and definitions (REQ-002)
2. **Opportunity stages & probabilities** - Need complete list with percentages (REQ-009, REQ-016)
3. **Report inventory** - Need consolidated list of all reports with Phase 1 priorities (multiple REQs)
4. **RFP request form inputs** - Need complete requirements for form fields (REQ-026)
5. **Variance reason codes** - Need reviewed and finalized code list (REQ-030)

### Medium Priority Gaps:
6. **Campaign approval workflow** - Not discussed in detail; may be needed
7. **Email template requirements** - Minimal discussion; may need more design input
8. **Mobile app usage** - Quick Add mentioned but not detailed
9. **Customer portal needs** - Mentioned in outline but not discussed in session

### Assumptions Requiring Validation:
- No automated lead scoring needed
- Standard NetSuite performance acceptable
- Round-robin assignment not needed
- Google Drive remains primary file storage
- GDPR not a primary concern (US business focus)

### Areas of Excellent Coverage:
- Current state process flows ✓
- Pain points and challenges ✓
- Strategic direction ✓
- Email marketing requirements ✓
- Influencer tracking vision ✓
- Access control and security needs ✓
- Integration requirements ✓

---

## Session Notes & Observations

### Key Success Factors Identified:
1. **Data quality dependency** - Segmentation only works if BD team enters data consistently
2. **Ease of use critical** - High performers resist admin burden; keep it simple
3. **Relationship-based culture** - System must support relationship tracking, not just transactions
4. **Internal competition dynamics** - Access controls critical to adoption
5. **Manual report tolerance** - Team comfortable with some manual processes if others automated

### Cultural Considerations:
- Sales team has competitive/territorial dynamics
- Marketing and sales collaboration needed but roles distinct
- High performers given more flexibility
- Trust issues affect data transparency
- Relationship-based vs. transactional approach

### Technical Environment:
- Google Workspace (Gmail, Drive, Docs, Sheets, Slides) - heavy usage
- Moving from Zendesk + Core → NetSuite/Orion
- MailChimp minimal usage
- Asana for project requests
- Paperless Post for event invitations
- Manual Excel/Sheets reporting extensive

### Session Coverage:
- Marketing & CRM topics merged (as appropriate for their business)
- Deep dive on influencer tracking (high interest)
- Extensive discussion of access controls and internal dynamics
- Good coverage of current state pain points
- Solid understanding of strategic direction
- Limited discussion of mobile usage
- Some report requirements need more detail

---

**END OF QUESTIONNAIRE v2.0**


# MASTER TRANSCRIPT: MARKETING
## KBM Hoag NetSuite Orion Implementation

**Sources Combined:**
- Marketing.txt (Plaud AI Recording - Marketing Discovery)
- 07-29 Business Process Review_ Order Approval & Marketing Management.txt
- GMT20250917-200141_Recording.transcript.vtt (September 17, 2025 - Marketing & Lead Management Session)
- Relevant portions from CRM.txt

**Date Range:** July-September 2025
**Business Process:** Marketing (Campaigns, Events, Content, Market Intelligence)

---

## EXECUTIVE SUMMARY

KBM Hoag's marketing approach is unique in the furniture dealer industry - they operate with a highly targeted, relationship-based model rather than traditional mass marketing. The marketing department's primary function is RFP response coordination and presentation development, not demand generation. Email campaigns are minimal (< 6/year), events are targeted and personal (showroom tours ~2x/month), and the team focuses on specific sectors, influencers, and strategic accounts. Current challenges include disconnected systems (MailChimp for occasional emails, Google Forms for RSVPs, Core for contacts) and poor data quality preventing effective segmentation. The shift to NetSuite will enable better market intelligence, contact segmentation for targeted communications, and visibility into pipeline trends to inform content strategy.

**Key Themes:**
- Relationship-based, targeted approach vs. mass marketing
- RFP management as core marketing function  
- Minimal email campaign usage (< 6 times/year)
- Event management (showroom tours, targeted events ~2x/month)
- Need for clean, segmented contact data
- Market intelligence and trend tracking capabilities
- Quarterly communications to specific contact segments

---

## MARKETING PHILOSOPHY & APPROACH

### Not Traditional B2B Marketing

**What KBM Hoag Doesn't Do:**
- No broad campaigns
- No mass email blasts (except rare occasions)
- No content marketing (minimal)
- No social media focus (mentioned in passing)
- No demand generation in traditional sense

**What They Do Instead:**
- Personal relationship cultivation
- One-to-one communication
- Targeted sector focus
- Influencer relationships (brokers, A&D firms)
- Strategic account management
- RFP response coordination

**Quote:**
"So much of what we do is relationship-based, and so we're being very selective of, like, hey, we want to invite these specific 20 people, and we're sending an email from a real person's email, rather than from info at KBM"

### Marketing as RFP Management

**Marcus's Observation:**
"Kind of unique because your marketing department is actually doing like some sales process really, right? Because you're doing RFPs"

**Marketing Team Role:**
- RFP response coordination
- Presentation development
- Client-facing materials creation
- Brand management
- Showroom coordination
- Not traditional demand generation

### Targeted Sector Strategy

**GM's Strategic Shift (Last Year):**
- Move away from mass communications
- Focus on specific sectors and industries
- Targeted to specific people within sectors
- Market-specific approaches (SF ≠ San Jose ≠ Sacramento)

**Result:**
- Better engagement
- Lower volume of outreach
- More personalized
- Higher quality interactions

---

## NETSUITE/ORION MARKETING CAPABILITIES

### Email Marketing Platform

**Capacity:**
- 120,000 emails/month included
- "Way more than we would ever use" - KBM Hoag

**Features:**
- Subscription Management: Automatic opt-in/opt-out tracking
- Templates: Available but KBM creates images in Google Slides
- Campaigns: Track opens, clicks, ROI
- Segments: Target by role, sector, geography, custom criteria

**KBM Hoag Current State:**
- **MailChimp:** Pay-as-you-go credits
- Less than 6 campaigns per year
- Discontinued quarterly newsletters (internal and external)
- Discontinued event invitations via mass email
- Shifted to personalized, relationship-based outreach

**MailChimp Challenges:**
- "MailChimp gets really pissed off when you try to load in Excel because they think you're going to spam a bunch of people" - Jenny
- Manual list creation and upload
- "Then most of it bounces anyways" - Jenny
- Can't segment by role or purpose effectively

**Decision:**
Email marketing functionality available in NetSuite but minimal implementation planned. Team can enable if needed post-go-live. Current low-volume, high-touch approach will continue.

### Contact Segmentation & Targeting

**Segment Capabilities:**
- **Role:** GC, broker, A&D firm, client, vendor, PM, CM, etc.
- **Sector/Vertical:** Healthcare, tech, corporate, government, education, etc.
- **Geography:** SF, San Jose, Sacramento markets
- **Relationship Type:** Client, prospect, influencer, partner
- **Custom Criteria:** Unlimited combinations

**Current Pain Point:**
- Core contact type options inadequate
  - "Are they the main contact? Are they finance? Is it procurement?"
  - "We don't know"
- Data entry inconsistent - can't trust segmentation
- "Poo in, poo out" - data quality issues prevent effective targeting
- One-size-fits-all messaging currently
- "Click rates aren't great so there's just really no way right now to target"

**Desired Future State:**
- Curated lists by role (brokers, PM firms, CM firms)
- Market-specific campaigns (Alex's market ≠ Jill's market ≠ Kate's market)
- Sector-specific targeting (healthcare trending up → tailored message)
- Quarterly market rate communications to specific groups
- Automated targeted campaigns if data quality improves

**Marketing Insight Quote:**
"If marketing had more insight into what some of those leads are and could see and track over time the sectors and how the market is changing, then it would be easier for that team to create proactively create content and target it"

### Communication Strategy

**Email Types:**

**1. Transactional (No Opt-In Required):**
- Order confirmations
- Rate changes to clients
- Process changes to vendors
- Invoices
- Important business communications

**2. Marketing (Opt-In Required):**
- Promotional campaigns
- Event invitations (if mass email)
- Newsletters

**Sending Options:**
- Individual user email (personalized, relationship-based)
- info@kbmhoag.com (operational)
- Campaign-based (bulk with tracking)
- Subscription status automatically managed
- Unsubscribe handling automatic

**Current Workaround:**
- Only pull contacts from specific date ranges
- Avoid spamming unsubscribed contacts
- Manual management of lists
- NetSuite will handle automatically

### Market Intelligence & Trend Tracking

**Current Gap:**
- No visibility into early-stage opportunities
- Can't track market trends systematically
- Can't proactively create content
- Reactive instead of strategic
- Limited insight into which sectors trending

**NetSuite Capabilities:**
- Pipeline visibility by sector
- Market trend dashboards
- Opportunity tracking from early stage
- Sector performance analysis
- Resource forecasting based on pipeline
- Content planning informed by data

**Use Cases:**
- Identify sectors trending up (healthcare growing → create targeted content)
- Quarterly market rate communications by tier
- Broker contact lists for targeted campaigns
- Territory-specific messaging (SF vs. San Jose vs. Sacramento)

---

## RFP MANAGEMENT

### Current Workflow

**Process Flow:**
1. RFP identified/received through relationship (BD rep or Account Manager)
2. Entered into Zendesk (maybe - not consistent)
3. When RFP formally arrives:
   - BD rep or Account Manager submits formal project request in **Asana**
   - Request includes:
     - Background information
     - Project links
     - Documentation
     - **Projected volume** (key metric for resource planning)
4. Marketing PM schedules kickoff call with stakeholders
5. Marketing team develops response
6. Volume tracking: Projected vs. Actual
   - Identify who over-estimates
   - Improve accuracy over time
   - Better resource allocation

**Pain Points:**
- Marketing has no visibility until formal request submitted
- Can't proactively prepare
- Can't track market trends from early-stage RFPs
- Resource allocation challenging without early visibility

### Enhanced RFP Workflow (NetSuite)

**Proposed Process:**
1. RFP identified → Create Opportunity in NetSuite immediately (CRM function)
2. BD/Account Manager enters preliminary information
3. When RFP formally received → Update opportunity, attach documents
4. Generate Quote/Proposal record
5. **Assign to Marketing team** (workflow/routing)
6. **Marketing PM visibility into pipeline**
7. Kickoff meeting scheduled
8. **Projected volume documented** on quote/project
9. Marketing develops response
10. Track: Projected vs. Actual volume
11. Close Won/Lost with reason codes
12. Analysis and learning

**Benefits for Marketing:**
- Early visibility into incoming RFPs
- Market trend intelligence from early-stage opportunities
- Proactive resource planning
- Better volume forecasting
- Historical performance by estimator
- Sector/market trend tracking
- Content opportunities identified

### Volume Tracking & Resource Planning

**Current Challenge:**
- People overestimate RFP volume
- Marketing resource allocation difficult
- Actual volume often significantly different from projected
- Can't plan team capacity effectively

**Solution:**
- Track **projected volume** on RFP/Quote
- Track **actual volume** on Sales Order/Project
- Report: Projected vs. Actual by user
- Identify patterns:
  - Who is most accurate?
  - Which sectors have largest variance?
  - Improve estimates over time
- Better resource allocation (marketing team capacity planning)

### Document Management

**RFP Documents:**
- Attach RFP documentation to opportunity/quote
- Link to Google Drive project folder
- Version control
- Team access
- Client-provided materials

**Response Documents:**
- Marketing-created presentations
- Proposals
- Supporting materials
- Link or attach to quote record
- Maintain for future reference
- Templates and reusable content library

---

## EVENT MANAGEMENT

### Current State

**Event Types:**

**1. Showroom Tours (Most Common)**
- Frequency: ~2 times per month currently
- Approach: Targeted invites (not mass email)
- Purposes:
  - Client tour
  - Finish review
  - Product demonstration
  - Relationship building

**2. Showroom Events**
- Cocktail receptions
- Product launches
- Industry gatherings
- Less frequent than tours

**3. Grand Openings / Major Events**
- Attendance tracking needed
- Invited list vs. actual attendees
- Including walk-ins
- Check-in process (exception, not typical)

### Current Process

**Invitation Approach:**
- Targeted personal email invitations
- **NOT mass MailChimp campaigns**
- Sent from individual user emails for personal touch
- "Hey, we want to invite these specific 20 people"

**RSVP Management:**
- Google Forms for RSVP (when needed)
- Manual tracking
- No systematic follow-up

**Showroom Event Form (Internal Coordination):**
- Headcount tracking
- Attendee list
- Food/beverage needs
- Room requirements
- Purpose/objectives
- Logistics planning for showroom manager

**No Systematic Tracking:**
- Who was invited (except major events)
- Who attended (no headcount at most events)
- Follow-up activities
- Conversion from events to opportunities
- ROI analysis

**Quote:**
"Who manages taking attendance? No one's taking headcount"

**Exception:**
"At our grand opening, we had people checking people in" (not typical)

### NetSuite Event Management Potential

**Capabilities:**
- Send invitations from NetSuite (can appear from individual user)
- RSVP tracking within platform
- Attendance dashboard
- Invited vs. attended reporting
- Create opportunities from event attendees
- Track event ROI
- Follow-up task automation

**KBM Hoag Response:**
- Question of value vs. effort
- Most events don't have formal attendance tracking
- Resource-intensive to implement
- Current approach (personal, informal) works for their model

**Decision:**
Minimal focus during implementation. Evaluate post-go-live if value emerges. Continue current approach of personal invites and Google Forms for major events requiring RSVP tracking.

---

## CONTACT DATA QUALITY & SEGMENTATION

### Current Challenges

**Core System Limitations:**
- Limited, unclear contact type options
- "Are they the main contact? Are they finance? Is it procurement?"
- "We don't know"
- No confidence in classification
- Can't segment effectively

**Data Entry Issues:**
- Manual data entry with no validation
- Inconsistent classification
- No chain of control for data
- Email opt-in/opt-out not tracked properly
- "Poo in, poo out" - data quality prevents targeting

**Impact on Marketing:**
- Can't create curated lists by role
- Can't segment by sector effectively
- One-size-fits-all messaging
- Poor click rates
- High bounce rates
- Ineffective campaigns

### NetSuite Solution

**Custom Contact Roles (Unlimited):**

**Proposed Roles (Examples):**
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

**Multiple Roles Per Contact:**
- If appropriate (someone might be both Decision Maker and Finance)
- Clear definitions
- Required field options
- Validation rules

### Market Sectors/Verticals

**Important for Segmentation & Targeting:**
- Healthcare (trending up)
- Technology
- Corporate Office
- Government
- Education
- Financial Services
- Legal
- Creative/Agency
- Hospitality
- Other

**Marketing Use Cases:**
- Targeted messaging by sector
- Market trend analysis
- Content creation (healthcare-specific materials)
- Opportunity forecasting
- Resource allocation
- Campaign planning

### Geography/Territory

**Markets:**
- San Francisco (Jill's territory)
- San Jose (Kate's territory)
- Sacramento (Alex's territory)

**Different by Market:**
- Industry mix varies
- Client types differ
- Competitive landscape unique
- Messaging needs distinct
- Rate structures may vary
- Relationship approaches different

**Need:**
Territory-based segmentation and reporting for targeted marketing by GM/territory.

---

## COMMUNICATION USE CASES

### Quarterly Market Rate Communications

**Current Need:**
- Communicate rate changes to clients
- Segment by tier (different rates for different clients)
- Quarterly or as-needed
- Currently manual list creation

**Future State:**
- Segment by client tier
- Send targeted rate communication
- Track opens/responses
- Automated list creation from NetSuite

### Vendor Process Changes

**Current Need:**
- Communicate process changes to vendors
- Update on new requirements
- Policy notifications
- Currently manual list and upload to MailChimp

**Future State:**
- Vendor contact segmentation
- Send from info@kbmhoag.com or operations user
- Track acknowledgment
- Automated vendor list

### Targeted Sector Campaigns

**Example: Healthcare Trending Up**
- Identify healthcare contacts (A&D, brokers, clients in healthcare)
- Create healthcare-specific content
- Send targeted message about healthcare expertise/case studies
- Track engagement
- Follow-up with interested contacts

### Broker/Influencer Outreach

**Current Approach:**
- Personal, one-to-one
- BD reps manage relationships
- No mass campaigns

**Potential Use:**
- Quarterly touchpoint from BD rep
- Personalized but from NetSuite
- Activity tracking
- Relationship nurturing automation

---

## SURVEYS & FEEDBACK

### Current State

**Customer Service Surveys:**
- Needed but not systematized
- Nolan mentioned having customer service survey
- No centralized tracking
- No trend analysis
- Manual process

**Vendor Surveys:**
- Occasional feedback requests
- No systematic approach
- No centralization

### NetSuite Capability

**Survey Functionality:**
- Create surveys within campaigns
- Send to segmented lists
- Track responses in NetSuite
- Results visible on customer/vendor records
- Trend analysis available
- Action item generation from feedback

**Potential Surveys:**
- Post-project customer satisfaction
- Vendor performance feedback
- Event feedback
- Service quality assessments
- Net Promoter Score (NPS)

**Decision:**
Low priority for Phase 1, but capability available. May implement post-go-live for customer service feedback.

---

## DASHBOARDS & ANALYTICS

### Marketing KPIs

**Available Metrics:**
- Campaign performance (open rates, click rates)
- Lead source tracking
- Conversion metrics (lead → opportunity → customer)
- Opportunity pipeline by source
- Sector performance trends
- Territory performance
- Event attendance (if tracked)
- Survey response rates

### Market Intelligence Dashboard

**Proposed View:**
- Opportunities by sector (trend over time)
- RFP volume by market/territory
- Win/loss by sector
- Projected volume vs. actual (by estimator)
- Pipeline by stage and sector
- Influencer engagement (activities logged)

**Value:**
- Proactive content planning
- Resource forecasting
- Strategic focus areas
- Competitive intelligence
- Market shift identification

---

## INTEGRATION WITH SALES PROCESS

### Lead Capture

**Web Form Integration:**
- Contact form submission → Lead created in NetSuite automatically
- Routing rules assign to appropriate team member
- Lead scoring and qualification workflows
- Conversion tracking

**Current Process:**
1. Contact form submission → Jenny (Admin)
2. Jenny qualifies lead
3. Routes to GM or appropriate account manager (if existing client)
4. Most submissions are: cleaning quotes (deleted), one-off requests, occasional legitimate leads

**Notable Success:**
Client requesting cubicles → order for touchdown cubicles

**Web Form Quality:**
"A lot of cleaning quotes or 'I inherited my grandmother's Newell Eames chair and need a pad for it'"

**Future State:**
- Same workflow but in NetSuite
- Better tracking of lead sources
- Conversion analysis
- Can market back to viable leads over time

### Opportunity Visibility

**Marketing Insight from Pipeline:**
- Which sectors have most opportunities?
- Which influencers generating most referrals?
- What project sizes trending?
- Geographic patterns?
- Seasonality?

**Content Planning:**
- Create materials for trending sectors
- Develop case studies for growing markets
- Influencer-specific content
- Sector thought leadership

### Handoff to Sales

**From Marketing to Sales:**
- Marketing qualifies RFP opportunity
- Develops response materials
- Hands to sales team for close
- Continues visibility for learning

**Feedback Loop:**
- Win/loss reasons inform future RFP responses
- Successful strategies replicated
- Messaging refined based on results

---

## REQUIREMENTS SUMMARY

### Functional Requirements

1. **Email Marketing:**
   - Campaign creation (light usage)
   - Subscription management (automatic)
   - Segmentation and targeting
   - Template management
   - Analytics (opens, clicks, conversions)

2. **Contact Segmentation:**
   - Custom role classifications
   - Sector/vertical assignments
   - Geography/territory
   - Relationship type
   - Combined criteria filtering

3. **Market Intelligence:**
   - Pipeline visibility by sector
   - Trend dashboards
   - Sector performance reporting
   - Early-stage opportunity visibility
   - RFP volume tracking

4. **RFP Management:**
   - Workflow routing to marketing team
   - Document attachment
   - Projected volume tracking
   - Actual vs. projected reporting
   - Team collaboration

5. **Event Management (Optional):**
   - Invitation capability
   - RSVP tracking
   - Attendance recording
   - Follow-up automation
   - ROI tracking

6. **Communication:**
   - Transactional emails (no opt-in required)
   - Marketing emails (opt-in managed)
   - Personalized from individual users
   - Operational from info@kbmhoag.com
   - Segmented vendor/client communication

7. **Surveys (Future):**
   - Customer satisfaction surveys
   - Vendor feedback
   - Event feedback
   - Response tracking
   - Trend analysis

### Technical Requirements

1. **Integrations:**
   - Web contact form → NetSuite lead creation
   - Google Drive folder linking
   - Email sending (individual user credentials)
   - Google Forms (potentially replace with NetSuite forms)

2. **Customizations:**
   - Custom contact roles
   - Sector/market classifications
   - RFP workflow routing
   - Volume tracking fields
   - Marketing team dashboards

3. **Data Quality:**
   - Validation rules for contact data
   - Required fields for segmentation
   - Duplicate prevention
   - Data cleanup during migration

4. **Reports/Dashboards:**
   - Marketing KPIs
   - Market intelligence dashboard
   - Sector trend analysis
   - Campaign performance
   - RFP volume and accuracy
   - Event ROI (if implemented)

---

## DECISIONS & ACTION ITEMS

### Decisions Made

1. **Email Marketing:** Minimal implementation during Phase 1
   - Capability available but not priority
   - Can enable post-go-live if needed
   - Team comfortable with current low-volume approach
   - Continue relationship-based, personal outreach

2. **Event Management:** Not a focus for implementation
   - Current process (personal invites, Google Forms) works
   - May revisit post-go-live if value identified
   - Major events: Consider attendance tracking

3. **RFP Process:** Will enhance with earlier visibility
   - Marketing team gets pipeline visibility
   - Volume tracking implemented
   - Workflow routing to be configured
   - Document management centralized

4. **Contact Segmentation:** Critical for future targeting
   - Custom roles to be defined
   - Sector/market classifications required
   - Data quality emphasis during implementation
   - Foundation for future targeted campaigns

5. **Communication Strategy:** Hybrid approach
   - Transactional: info@kbmhoag.com or user email
   - Targeted outreach: Personal user emails
   - Campaigns: Minimal, through NetSuite if used
   - Surveys: Centralized in NetSuite (future)

6. **Market Intelligence:** Enable proactive content planning
   - Pipeline visibility by sector
   - Trend tracking
   - Resource forecasting
   - Strategic focus areas

### Action Items

1. **Marketing Team:** Define desired contact roles and sectors for segmentation
2. **Marketing Team:** Evaluate MailChimp templates for NetSuite (low priority)
3. **Marketing Team:** Document RFP volume tracking needs
4. **Marketing Team:** Consider event management needs for future phase
5. **All:** Identify who should manage contact segmentation and data quality

---

## PAIN POINTS TO SOLVE

### Current Frustrations

1. **Limited Market Intelligence:**
   - No visibility into early-stage opportunities
   - Can't track market trends systematically
   - Can't proactively create content
   - Reactive instead of strategic
   - Don't know which sectors trending until too late

2. **Data Quality:**
   - Inconsistent contact classification
   - Can't trust segmentation
   - "Poo in, poo out"
   - No validation or standards
   - Can't create targeted lists

3. **Communication Challenges:**
   - Manual list management
   - Can't segment effectively
   - MailChimp limitations and complaints
   - High bounce rates
   - Opt-in/opt-out tracking manual
   - Poor campaign performance

4. **RFP Workflow:**
   - No visibility until formal request
   - Can't prepare proactively
   - Resource allocation challenging
   - Volume estimates unreliable
   - No systematic tracking of accuracy

5. **Event Tracking:**
   - No systematic invitation tracking
   - No attendance records (most events)
   - No follow-up automation
   - No ROI analysis
   - Informal process doesn't scale

6. **No Centralized Surveys:**
   - Customer service feedback scattered
   - Vendor feedback not systematized
   - No trend analysis
   - No action item tracking

### Future State Solutions

1. **Market Intelligence:**
   - Pipeline visibility from day one
   - Market trend dashboards
   - Sector performance tracking
   - Proactive content planning
   - Resource forecasting based on data
   - Strategic focus informed by trends

2. **Data Quality:**
   - Validation rules
   - Required fields
   - Standardized classifications
   - Duplicate prevention
   - Regular cleanup processes
   - Clean segmentation possible

3. **Effective Communication:**
   - Automated segmentation
   - One-click targeted campaigns
   - Subscription management automatic
   - Reduced manual effort
   - Better tracking and analytics
   - Improved campaign performance

4. **RFP Visibility:**
   - Early pipeline visibility
   - Proactive preparation
   - Better resource planning
   - Volume accuracy tracking
   - Historical performance data
   - Learning and improvement

5. **Event Management (If Implemented):**
   - Centralized invitation tracking
   - RSVP management
   - Attendance recording
   - Follow-up automation
   - ROI calculation
   - Scalable process

6. **Integrated Surveys:**
   - Campaign functionality for surveys
   - Results tracked in NetSuite
   - Trend analysis available
   - Action item generation
   - Customer/vendor record integration

---

## CHANGE MANAGEMENT CONSIDERATIONS

### Behavior Changes Required

1. **Data Quality Discipline:**
   - Consistent contact role classification
   - Sector assignment discipline
   - Required fields completion
   - Validation rule compliance

2. **Earlier RFP Entry:**
   - Create opportunities when first identified
   - Not waiting until formal request
   - Preliminary information captured
   - Marketing visibility from start

3. **Segmentation Mindset:**
   - Think about target audiences
   - Use segmentation for campaigns
   - Trust the data (once clean)
   - Move beyond one-size-fits-all

4. **System-Based Communication:**
   - Use NetSuite for campaigns (when appropriate)
   - Track activities in system
   - Log event invitations
   - Document responses

### Resistance Points

1. **Time Investment:**
   - Data entry takes time
   - Classification feels like overhead
   - Need to show ROI quickly

2. **Process Changes:**
   - Comfortable with MailChimp (even with limitations)
   - Google Forms simple and familiar
   - New system = new learning
   - Temporary productivity dip

3. **Personalization Concerns:**
   - Fear of losing personal touch
   - System-based = impersonal?
   - Relationship-based culture at risk?
   - Need to demonstrate how to maintain personal approach

### Success Factors

1. **Show Value Fast:**
   - Market intelligence visibility
   - Sector trend identification
   - Better campaign targeting (when data clean)
   - Resource forecasting accuracy

2. **Maintain Personal Touch:**
   - Demonstrate sending from individual emails
   - Show how to personalize within system
   - Relationship-based approach preserved
   - Technology enables, doesn't replace

3. **Data Quality Campaign:**
   - Clean data from start
   - Regular hygiene processes
   - Recognition for good practices
   - Show impact of clean data

4. **Training & Support:**
   - Role-specific training for marketing team
   - Quick reference guides
   - Ongoing support available
   - Documentation accessible

---

## INTEGRATION WITH OTHER PROCESSES

### Connection to CRM/Sales
- Lead capture from web forms
- Opportunity pipeline visibility
- RFP workflow handoff
- Contact data shared
- Activity visibility

### Connection to Order Management
- Opportunity → Quote workflow
- Customer information flow
- Project assignment
- Win/loss tracking

### Connection to Financial
- Campaign ROI tracking
- Event cost tracking
- Revenue attribution by source
- Budget management

### Connection to Business Intelligence
- Market trend reporting
- Sector performance analysis
- Campaign analytics
- Pipeline forecasting
- Source attribution

---

## TRAINING NEEDS

### Marketing Team
- Contact segmentation and list creation
- Email campaign creation (if/when needed)
- RFP workflow and volume tracking
- RSVP and event tracking (if implemented)
- Survey management (future)
- Analytics and reporting
- Market intelligence dashboards

### Sales/BD Team (Marketing Perspective)
- Early opportunity creation (for marketing visibility)
- Contact role classification (for segmentation)
- Sector assignment (for trend tracking)
- Activity logging (for relationship tracking)

### Admin (Jenny)
- Lead qualification and routing
- Web form lead management
- Contact database maintenance
- Duplicate management
- Data quality monitoring

---

## OPEN QUESTIONS FOR FUTURE SESSIONS

1. **Email Campaign Templates:**
   - Recreate current Google Slides approach in NetSuite?
   - Use NetSuite templates?
   - Training needed on template creation?

2. **Google Forms Replacement:**
   - Replace with NetSuite forms for RSVPs?
   - Keep Google Forms for simplicity?
   - Integration possible?

3. **Survey Strategy:**
   - Customer service survey requirements?
   - Vendor survey process?
   - Frequency and automation?
   - Who manages survey responses?

4. **Event Management:**
   - Post-go-live evaluation needed?
   - Attendance tracking valuable enough?
   - Integration with opportunity creation?
   - ROI calculation worth effort?

5. **Content Library:**
   - Where to store RFP response materials?
   - Version control approach?
   - Template management?
   - Reusable content organization?

6. **Market Intelligence:**
   - Specific dashboard requirements?
   - Frequency of trend review?
   - Who analyzes trends?
   - Content planning cadence?

7. **Segmentation Taxonomy:**
   - Final list of custom roles?
   - Final list of sectors?
   - Geography beyond current 3 markets?
   - Other segmentation criteria needed?

---

## SESSION QUOTES & INSIGHTS

**On Marketing Approach:**
- "Your marketing department is actually doing like some sales process really, right? Because you're doing RFPs" - Marcus
- "So much of what we do is relationship-based" - Team
- "We're being very selective... we're sending an email from a real person's email, rather than from info@" - Team

**On Data Quality:**
- "Poo in, poo out" - Team
- "The data entry part of it has never been clean enough to trust in" - Team
- "Click rates aren't great so there's just really no way right now to target" - Team

**On Current Challenges:**
- "MailChimp gets really pissed off when you try to load in Excel because they think you're going to spam a bunch of people" - Jenny
- "Then most of it bounces anyways" - Jenny
- "Who manages taking attendance? No one's taking headcount" - Team

**On Future Possibilities:**
- "If marketing had more insight into what some of those leads are and could see and track over time the sectors and how the market is changing, then it would be easier for that team to create proactively create content and target it" - Marketing Team

**On Strategic Shift:**
- Moved away from mass communications last year
- Focus on specific sectors and targeted outreach
- Better engagement even with lower volume
- Relationship-based approach reinforced

---

*End of Master Transcript: Marketing*


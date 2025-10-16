# MASTER TRANSCRIPT: MARKETING & CRM
## KBM Hoag NetSuite Orion Implementation

**Sources Combined:**
- Marketing.txt (Plaud AI Recording - Marketing/CRM Discovery)
- CRM.txt (Plaud AI Recording - CRM Discovery)  
- 07-29 Business Process Review_ Order Approval & Marketing Management.txt
- GMT20250917-200141_Recording.transcript.vtt (September 17, 2025 - Marketing & Lead Management Session)

**Date Range:** July-September 2025
**Business Process:** Marketing, Lead Management, CRM, RFP Management

---

## EXECUTIVE SUMMARY

KBM Hoag's marketing and CRM approach is unique in the furniture dealer industry - their marketing department actively participates in the sales process through RFP management rather than traditional mass marketing campaigns. The team uses a highly targeted, relationship-based approach focusing on specific sectors, influencers, and strategic accounts rather than broad email campaigns. Current systems (Zendesk for CRM, MailChimp for occasional email marketing) are disconnected from core business operations, leading to data quality issues and limited insight into market trends.

**Key Themes:**
- Relationship-based, targeted approach vs. mass marketing
- RFP management as core marketing function
- Need for clean, segmented contact data
- Desire for market intelligence and trend tracking
- Minimal email campaign usage (< 6 times/year)
- Event management (showroom tours, targeted events ~2x/month)

---

## NETSUITE/ORION MARKETING CAPABILITIES OVERVIEW

### Email Marketing
- **Capacity:** 120,000 emails/month included
  - "Way more than we would ever use" - KBM Hoag
- **Subscription Management:** Automatic opt-in/opt-out tracking
- **Templates:** Available but KBM Hoag creates images in Google Slides
- **Campaigns:** Track opens, clicks, ROI
- **Segments:** Target by role, sector, geography, custom criteria

**KBM Hoag Current Usage:**
- Pay-as-you-go MailChimp credits
- Less than 6 campaigns per year
- Discontinued quarterly newsletters (internal and external)
- Discontinued event invitations via mass email
- Shifted to personalized, relationship-based outreach

**Decision:** Email marketing functionality available but minimal implementation planned. Team can enable if needed post-go-live.

### Lead Capture & Management
- Web forms embedded in website create leads automatically in NetSuite
- Routing rules assign leads to appropriate team members
- Lead scoring and qualification workflows
- Conversion tracking

**Current Process:**
1. Contact form submission → Jenny (Admin)
2. Jenny qualifies lead
3. Routes to GM or appropriate account manager (if existing client)
4. Most submissions are: cleaning quotes (deleted), one-off requests, occasional legitimate leads

**Notable Success:** Client requesting cubicles → order for touchdown cubicles

**Web Form Quality:** "A lot of cleaning quotes or 'I inherited my grandmother's Newell Eames chair and need a pad for it'"

### Contact Segmentation & Targeting
- Segment by:
  - Role (GC, broker, A&D firm, client, vendor)
  - Sector/Vertical market (healthcare, tech, corporate, etc.)
  - Geography (SF, San Jose, Sacramento markets)
  - Custom criteria
  - Relationship type

**Current Pain Point:**
- Core contact type options inadequate (Main contact? Finance? Procurement?)
- Data entry inconsistent - can't trust segmentation
- "Poo in, poo out" - data quality issues prevent effective targeting
- One-size-fits-all messaging currently
- Click rates not great on broad campaigns

**Desired Future State:**
- Curated lists by role (brokers, PM firms, CM firms)
- Market-specific campaigns (Alex's market ≠ Jill's market ≠ Kate's market)
- Sector-specific targeting (healthcare trending up → tailored message)
- Quarterly market rate communications to specific groups
- Automated targeted campaigns if data quality improves

### Duplicate Detection & Management
- NetSuite native duplicate detection
- AI-enhanced duplicate identification
- Merge capabilities
- Prevention of duplicate creation

**Note:** Core lacks this feature

### Dashboards & Analytics
- Marketing KPIs
- Campaign performance
- Lead source tracking
- Conversion metrics
- Opportunity pipeline by source

---

## CRM: CURRENT STATE ANALYSIS

### System Architecture (Current)

**Zendesk (CRM):**
- Opportunity tracking
- Lead management
- Forecasting
- Manual data entry
- Not required for all team members
- Inconsistent usage and data quality

**Core:**
- Order management
- Customer database
- Manual transfer from Zendesk when deal closes

**Asana:**
- RFP project request workflow
- Marketing project kickoff coordination
- Projected volume tracking vs. actual
- Resource allocation planning

**Challenges:**
- Multiple disconnected systems
- Manual processes between systems
- No automatic data flow
- Limited visibility for marketing into sales pipeline
- Data quality varies widely by user

### Lead Sources & Inputs

**Primary Lead Sources:**
1. **Relationships/Influencers** (Primary)
   - Business Development reps own these relationships
   - General Managers manage their territory relationships
   - Brokers, A&D firms, clients, manufacturers
   - Tenant-in-the-market lists

2. **RFPs** (Significant)
   - Come through existing relationships
   - Project management firms, A&D firms, direct clients
   - Sometimes from manufacturers
   - Never "cold" RFPs to KBM Hoag

3. **Web Contact Form** (Minimal viable leads)
   - Most are non-viable (cleaning quotes, one-off requests)
   - Occasional legitimate opportunity

4. **Referrals**
   - Existing client referrals
   - Manufacturer referrals

### Business Development vs. Account Management Roles

**Business Development Reps (Jill, Kate, Alex):**
- Market-facing customer acquisition
- Relationship building
- Wining and dining influencers, brokers, clients
- Lead generation
- Market-specific focus (different by GM/region)

**Account Managers:**
- "Broad on purpose" - varies by individual
- Some mimic business development more closely
- Some function more like sales support
- Manage everything surrounding the project after handoff
- May also generate their own leads
- Project management responsibilities

**Variability:** Role execution depends on individual skill set and comp structure

### Opportunity Management Process (Current)

**Lead Entry (Optional):**
- BD reps/GMs *may* enter opportunities in Zendesk
- Not required - many don't
- Assign value and probability
- Inconsistent information captured:
  - Some add activities, tasks, contacts
  - Some just claim the lead ("licking everything and calling it theirs")
  - Wide variability in data quality

**Forecasting:**
- Account managers supposed to update for forecasting purposes
- Used for pipeline/revenue forecasting
- Accuracy varies by user

**Closing:**
- Mark as Closed Won or Closed Lost
- If Closed Won → manual transfer to Core
- "Dies in there" if lost
- No automatic sync between systems

### RFP Management Workflow (Current)

**Process Flow:**
1. RFP identified/received through relationship
2. Entered into Zendesk (maybe)
3. When RFP formally arrives:
   - BD rep or Account Manager submits formal project request in Asana
   - Request includes:
     - Background information
     - Project links
     - Documentation
     - **Projected volume** (key metric)
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

### Contact Management Challenges

**Data Quality Issues:**
- No standard contact classification in Core
- Contact types inadequate (Main? Finance? Procurement? Unknown)
- Manual data entry with no validation
- No chain of control for data
- Email opt-in/opt-out not tracked properly

**Communication Challenges:**
- Need to email clients (rate changes)
- Need to email vendors (process changes)
- Manual list creation and upload to MailChimp
- MailChimp "gets really pissed off" when loading Excel (spam prevention)
- "Most of it bounces anyways"
- Can't segment by role or purpose

**Surveys:**
- Customer service surveys needed
- Vendor surveys (Nolan has customer service survey)
- Currently no centralized system for survey management

---

## NETSUITE/ORION CRM: FUTURE STATE

### Opportunity Management

**Transaction Flow:**
- **Opportunity** → **Quote/Proposal** → **Sales Order**
- All stages visible and linked
- Project number/name consistent across all transactions
- Different transaction numbers (OP-#### / PR-#### / SO-####)

**Opportunity Record:**
- Pipeline tracking
- Forecasting
- Probability weighting
- Value tracking
- Source attribution
- Market/sector classification
- Related contacts and activities
- Document attachment

**Conversion:**
- One-click conversion: Opportunity → Quote
- Automatic data transfer
- Maintains linkage
- Audit trail preserved

**Forecasting:**
- Recommend opportunity-level forecasting (not quote-level)
- Prevents over-forecasting with multiple quotes
- Manual sync needed if multiple quotes with different values
- "Someone's gonna have to manage which quote amount should go back to the opportunity"

### Contact & Lead Management

**Lead Record:**
- Source tracking
- Qualification status
- Assignment rules
- Activity history
- Conversion to contact/customer

**Contact Record:**
- Role classification (customizable beyond Core limitations)
- Sector/market assignment
- Relationship type
- Activity tracking
- Communication preferences
- Opt-in/opt-out status (automatic management)
- Related opportunities and projects

**Segmentation Capabilities:**
- Unlimited custom criteria
- Role-based lists
- Sector-based lists
- Geography-based lists
- Combined criteria
- Dynamic vs. static lists

**Marketing Insight:**
- "If marketing had more insight into what some of those leads are and could see and track over time the sectors and how the market is changing, then it would be easier for that team to create proactively create content and target it"
- Visibility into broker contacts for targeted campaigns
- Quarterly market rate communications by tier
- Sector-specific content (healthcare, tech, corporate, etc.)

### Communication Management

**Email from NetSuite:**
- Send from individual user email (personalized)
- Send from info@kbmhoag.com (operational)
- Campaign-based (bulk with tracking)
- Subscription status automatically managed
- Unsubscribe handling automatic

**Transactional vs. Marketing Communication:**
- **Transactional** (no opt-in required):
  - Order confirmations
  - Rate changes
  - Process changes
  - Invoices
  - Important business communications
- **Marketing** (opt-in required):
  - Promotional campaigns
  - Event invitations (if mass email)
  - Newsletters

**Current Workaround:**
- Only pull contacts from specific date ranges
- Avoid spamming unsubscribed contacts
- Manual management of lists
- NetSuite will handle automatically

### Activity & Task Management

**For Opportunities:**
- Follow-up tasks
- Meeting scheduling
- Call logging
- Email tracking
- Document sharing
- Team collaboration

**Integration with Project Management:**
- When opportunity converts to project
- Hand-off to project team
- Continued visibility for BD/account manager
- Performance tracking (forecast vs. actual)

---

## RFP MANAGEMENT IN NETSUITE

### RFP Workflow Enhancement

**Proposed Improved Process:**
1. RFP identified → Create Opportunity in NetSuite immediately
2. BD/Account Manager enters preliminary information
3. When RFP formally received → Update opportunity, attach documents
4. Generate Quote/Proposal record
5. Assign to Marketing team (workflow/routing)
6. Marketing PM visibility into pipeline
7. Kickoff meeting scheduled
8. Projected volume documented on quote/project
9. Marketing develops response
10. Track: Projected vs. Actual volume
11. Close Won/Lost with reason codes
12. Analysis and learning

**Benefits:**
- Early visibility for marketing team
- Market trend intelligence
- Proactive resource planning
- Better volume forecasting
- Historical performance by estimator
- Sector/market trend tracking

### Volume Tracking & Accuracy

**Current Challenge:**
- People overestimate volume
- Resource allocation difficult
- Actual volume often significantly different

**Solution:**
- Track projected volume on RFP/Quote
- Track actual volume on Sales Order/Project
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

---

## EVENT MANAGEMENT

### Current State

**Event Types:**
1. **Showroom Tours** (Most common)
   - ~2 times per month currently
   - Targeted invites
   - Various purposes (client tour, finish review, product demo)
2. **Showroom Events**
   - Cocktail receptions
   - Product launches
   - Industry gatherings
   - Less frequent
3. **Grand Openings / Major Events**
   - Attendance tracking
   - Invited list vs. actual attendees
   - Including walk-ins

**Current Process:**
- Targeted personal email invitations (not mass MailChimp)
- Google Forms for RSVP (when needed)
- Showroom Event Form (coordination):
  - Headcount
  - Attendee list
  - Food/beverage needs
  - Room requirements
  - Purpose/objectives
  - Logistics planning for showroom manager

**No Systematic Tracking:**
- Who was invited
- Who attended
- Follow-up activities
- Conversion from events
- ROI analysis

### NetSuite Event Management Potential

**Capabilities:**
- Send invitations from NetSuite (can appear from individual)
- RSVP tracking
- Attendance dashboard
- Invited vs. attended
- Create opportunities from event attendees
- Track event ROI

**KBM Hoag Response:**
- "Who manages taking attendance? No one's taking headcount"
- Exception: Grand opening had check-in process
- Most events: No formal attendance tracking
- Question of value vs. effort

**Decision:** Minimal focus during implementation, evaluate post-go-live if value emerges

---

## ORDER APPROVAL & BUSINESS RULES

### Approval Workflow Capabilities (NetSuite/Orion)

**Business Rule Engine:**
- Define rule criteria
- Automatic routing to approvers
- Dashboard notifications for approvers
- Approval/rejection/exception handling
- Timestamp and audit trail
- Average approval time tracking

**Example Rules:**
- Customer PO number missing → route to Lorraine or sales manager
- Gross margin < 16% → route to CFO
- Order > $25,000 → route to Shannon (Project Coordinator Manager)
- Missing requirements (deposit, signed proposal, drawings, lookbook) → route to Matt
- Erosion > $1,500 cumulative → email approval required from Matt

**Complexity Caution:**
- More checks = slower process
- Must manage approvers
- Report on time-to-approve
- Find balance between control and speed

### Current Approval Process (KBM Hoag)

**Order Approval Rules:**
1. **Over $25,000:**
   - Goes to Shannon (Project Coordinator Manager) for approval
   
2. **Missing Requirements:**
   - Must have: Deposit, Signed proposal, Signed drawings, Signed lookbook
   - If any missing → approval from Matt required
   - "They do all day unabashedly, could care less" (ask Matt for exceptions)

3. **Erosion > $1,500 Cumulative:**
   - Email approval from Matt required
   - Example: $500 erosion + $1,000 more = $1,500 cumulative triggers approval
   - Purpose: Training insight ("new person often reason for erosion")
   - Problem-solving opportunity (cheaper alternatives)

**Matt's Erosion Review Philosophy:**
- Not about punishment
- Identifying training needs
- Problem-solving with more experience
- Example: Clay's crane rental story ($6K-$10K crane vs. $1.2K elevator technician)
- "If we're going to spend the money, let's spend it this way"

**Process Notes:**
- Matt responds quickly ("so good and quick about responding")
- Mark is backup for Matt
- PCs usually submit erosion requests on behalf of team
- Typically not excessive ("sounds like a lot, but it's not that much")

### Double Order Prevention

**Pain Point:**
- Biggest losses from double orders
- Same order placed twice unknowingly
- Example: 150 workstations ordered and owned before discovered (shipment notice)
- Shannon's approval supposed to catch double orders

**Challenge:**
- Difficult to automate detection
- Sometimes legitimately ordering similar items across projects
- Sometimes ordering in bulk (technically a "double order" but intentional)
- Don't want constant "Are you sure?" prompts (users will click yes without thinking)

**Potential Solution:**
- Query: Same total dollar amount within past 30 days
- Flag for review
- Not automatic rejection
- "Not a hard query"

### Vendor Credit Limits

**Need:**
- Track vendor credit limits for KBM Hoag
- Currently hit limits unexpectedly
- "Mad scramble at that nth hour because our order won't go through"

**Solution:**
- Vendor record: Credit limit field
- Warning at percentage threshold (e.g., 90%)
- Prevent PO creation if over limit
- Dashboard visibility
- "Sounds like just a pretty simple query"

---

## DATA QUALITY & SEGMENTATION

### Contact Role Classification

**Core Limitations:**
- Limited, unclear contact type options
- "Are they the main contact? Are they finance? Is it procurement?"
- "We don't know"
- No confidence in classification

**NetSuite Flexibility:**
- Custom contact roles (unlimited)
- Multiple roles per contact (if appropriate)
- Clear definitions
- Required field options
- Validation rules

**Proposed Roles (examples):**
- Primary Contact
- Decision Maker
- Finance/Accounting
- Procurement
- Facilities
- Project Manager
- Executive Sponsor
- Influencer (Broker, A&D)
- Manufacturer Rep

### Market Sectors/Verticals

**Important for Segmentation:**
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

**Use Cases:**
- Targeted messaging
- Market trend analysis
- Opportunity forecasting
- Resource allocation
- Content creation

### Geography/Territory

**Markets:**
- San Francisco (Jill's territory)
- San Jose (Kate's territory)
- Sacramento (Alex's territory)

**Different by Market:**
- Industry mix
- Client types
- Competitive landscape
- Messaging needs
- Rate structures

**Need:** Territory-based segmentation and reporting

---

## REQUIREMENTS SUMMARY

### Functional Requirements

1. **CRM:**
   - Opportunity tracking with forecasting
   - Lead capture and qualification
   - Contact segmentation (role, sector, geography)
   - Activity tracking
   - Duplicate detection

2. **Marketing:**
   - Email campaigns (light usage expected)
   - Subscription management (automatic)
   - Web form integration
   - Segmentation and targeting
   - Campaign analytics

3. **RFP Management:**
   - Document attachment
   - Projected volume tracking
   - Actual vs. projected reporting
   - Marketing team visibility
   - Workflow routing

4. **Approval Workflows:**
   - Order value thresholds
   - Missing requirements checking
   - Erosion tracking and approval
   - Double order detection
   - Audit trail and timestamps

5. **Communication:**
   - Transactional emails (no opt-in required)
   - Marketing emails (opt-in managed)
   - Personalized from individual users
   - Operational from info@kbmhoag.com
   - Vendor/client segmented communication

6. **Analytics:**
   - Market trend visibility
   - Sector performance
   - Lead source ROI
   - Opportunity pipeline
   - Forecast accuracy by user
   - Event attendance (if tracked)

### Technical Requirements

1. **Integrations:**
   - Web contact form → NetSuite lead creation
   - Google Drive folder linking
   - Email sending (individual user credentials)

2. **Customizations:**
   - Custom contact roles
   - RFP workflow
   - Volume tracking (projected vs. actual)
   - Approval rules configuration (up to 10 rules)
   - Business rule engine setup

3. **Data Migration:**
   - Contact data from Core
   - Opportunity history from Zendesk
   - Historical customer data
   - Contact segmentation/classification

4. **Reports/Dashboards:**
   - Marketing KPIs
   - Pipeline by source, sector, territory
   - Forecast accuracy report
   - Approval time tracking
   - User activity reports
   - Market trend analysis

---

## DECISIONS & ACTION ITEMS

### Decisions Made

1. **Email Marketing:** Minimal implementation during Phase 1
   - Capability available but not priority
   - Can enable post-go-live if needed
   - Team comfortable with current low-volume approach

2. **Event Management:** Not a focus for implementation
   - Current process (personal invites, Google Forms) works
   - May revisit post-go-live if value identified
   - Major events: Consider attendance tracking

3. **RFP Process:** Will enhance with earlier opportunity creation
   - Marketing visibility improved
   - Volume tracking implemented
   - Workflow routing to be configured

4. **Approval Rules:** Migrate current rules to NetSuite
   - Shannon to document current flowchart
   - Up to 10 rules in BRD budget
   - Double-order detection query to be built

5. **Contact Segmentation:** Critical for future targeting
   - Custom roles to be defined
   - Sector/market classifications required
   - Data quality emphasis during implementation

6. **Communication Strategy:** Hybrid approach
   - Transactional: info@kbmhoag.com or user email
   - Targeted outreach: Personal user emails
   - Campaigns: Minimal, through NetSuite if used
   - Surveys: Centralized in NetSuite

### Action Items

1. **Shannon:** Document approval workflow rules (flowchart)
2. **Marketing Team:** Define desired contact roles and sectors
3. **BD/Sales Team:** Define lead sources for tracking
4. **All:** Identify who should manage contact segmentation
5. **Marketing:** Evaluate MailChimp templates for NetSuite (low priority)
6. **Team:** Consider event management needs for future phase

---

## PAIN POINTS TO SOLVE

### Current Frustrations

1. **Disconnected Systems:**
   - Zendesk → Core manual transfer
   - Asana for RFP workflow separate
   - No integrated visibility

2. **Data Quality:**
   - Inconsistent entry in Zendesk
   - Can't trust segmentation
   - "Poo in, poo out"
   - No validation or standards

3. **Limited Marketing Intelligence:**
   - No visibility into early-stage opportunities
   - Can't track market trends
   - Can't proactively create content
   - Reactive instead of strategic

4. **Communication Challenges:**
   - Manual list management
   - Can't segment effectively
   - MailChimp limitations
   - Bounce management manual
   - Opt-in/opt-out tracking missing

5. **No Centralized Surveys:**
   - Customer service feedback scattered
   - Vendor feedback not systematized
   - No trend analysis

### Future State Solutions

1. **Single System:**
   - Opportunity → Quote → Order in one platform
   - Automatic data flow
   - Real-time visibility
   - Team collaboration

2. **Data Quality:**
   - Validation rules
   - Required fields
   - Standardized classifications
   - Duplicate prevention
   - Regular cleanup

3. **Marketing Intelligence:**
   - Pipeline visibility
   - Market trend dashboards
   - Sector performance tracking
   - Proactive content planning
   - Resource forecasting

4. **Effective Communication:**
   - Automated segmentation
   - One-click targeted campaigns
   - Subscription management automatic
   - Reduced manual effort
   - Better tracking and analytics

5. **Integrated Surveys:**
   - Campaign functionality for surveys
   - Results tracked in NetSuite
   - Trend analysis available
   - Action item generation

---

## UNIQUE ASPECTS OF KBM HOAG APPROACH

### Relationship-Based Marketing

**Not Traditional B2B Marketing:**
- No broad campaigns
- No mass email blasts (except rare occasions)
- No content marketing (minimal)
- No social media focus (mentioned)

**Instead:**
- Personal relationship cultivation
- One-to-one communication
- Targeted sector focus
- Influencer relationships (brokers, A&D firms)
- Strategic account management

**Quote:** "So much of what we do is relationship-based, and so we're being very selective of, like, hey, we want to invite these specific 20 people, and we're sending an email from a real person's email, rather than from info at KBM"

### Marketing as RFP Management

**Marketing Team Role:**
- Not traditional demand generation
- RFP response coordination
- Presentation development
- Client-facing materials
- Brand management
- Showroom coordination

**"Kind of unique because your marketing department is actually doing like some sales process really, right? Because you're doing RFPs" - Marcus

### Targeted Sector Strategy

**GM Focus (Last Year's Strategic Shift):**
- Move away from mass communications
- Focus on specific sectors and industries
- Targeted to specific people within sectors
- Market-specific approaches (SF ≠ San Jose ≠ Sacramento)

**Result:** Better engagement, though lower volume of outreach

---

## TRAINING NEEDS

### Marketing Team
- Contact segmentation and list creation
- Email campaign creation (if/when needed)
- RSVP and event tracking (if implemented)
- Survey management
- Analytics and reporting

### Sales/BD Team
- Opportunity creation and management
- Activity logging
- Contact role classification
- Forecasting and pipeline management
- RFP workflow

### Account Managers
- Contact management
- Opportunity updates
- Activity tracking
- Reporting

### Admin (Jenny)
- Lead qualification and routing
- Web form lead management
- Contact database maintenance
- Duplicate management

---

## INTEGRATION WITH OTHER PROCESSES

### Connection to Order Management
- Opportunity → Quote → Sales Order flow
- Customer data sync
- Contact information flow
- Project assignment

### Connection to Financial
- Opportunity value tracking
- Revenue forecasting
- Commission tracking (if based on opportunities)

### Connection to Operations
- RFP volume → resource planning
- Project kickoff from won opportunities
- Customer contact info for project team

### Connection to Business Intelligence
- Pipeline reporting
- Market trend analysis
- Forecast accuracy
- Conversion metrics
- Source attribution

---

## CHANGE MANAGEMENT CONSIDERATIONS

### Behavior Changes Required

1. **Consistent CRM Data Entry:**
   - Currently optional, needs to become standard
   - "Not required" → Required for visibility
   - Variability ("some people put activities, some don't") → Standardization

2. **Earlier Opportunity Creation:**
   - Currently: Enter when ready to forecast or at RFP arrival
   - Future: Create at first knowledge of potential

3. **Contact Role Classification:**
   - Currently: Unclear, inconsistent
   - Future: Standardized, required
   - Team needs to agree on classifications

4. **RFP Workflow:**
   - Currently: Asana project request
   - Future: NetSuite-based (still may use Asana for project execution)

### Resistance Points

1. **Sales Team:**
   - "Matt's philosophy: Sales will be our biggest pushback"
   - May resist structure
   - "Some people just licking everything and calling it theirs"
   - Need to demonstrate value for them

2. **Time Investment:**
   - Data entry takes time
   - Activity logging feels like overhead
   - Need to show ROI (better forecasting, reduced manual work elsewhere)

3. **Process Changes:**
   - Comfortable with current Zendesk + Core + Asana mix
   - New system = new learning
   - Temporary productivity dip expected

### Success Factors

1. **Executive Sponsorship:**
   - Matt's support critical
   - Clear expectations set
   - Accountability for usage

2. **Show Value Fast:**
   - Pipeline visibility
   - Market intelligence
   - Forecasting improvements
   - Reduced manual communication work

3. **Training & Support:**
   - Role-specific training
   - NetSuite champions identified
   - Ongoing support available
   - Documentation accessible

4. **Data Quality Campaign:**
   - Clean data from start
   - Regular hygiene
   - Recognition for good practices

---

## OPEN QUESTIONS FOR FUTURE SESSIONS

1. **Asana Integration:**
   - Continue using for task management?
   - Integrate with NetSuite or keep separate?
   - RFP kickoff in Asana or NetSuite?

2. **Google Forms:**
   - Replace with NetSuite forms?
   - Keep for simplicity?

3. **Survey Strategy:**
   - Customer service survey requirements?
   - Vendor survey process?
   - Frequency and automation?

4. **Event Management:**
   - Post-go-live evaluation needed?
   - Attendance tracking valuable?
   - Integration with opportunity creation?

5. **Contact Ownership:**
   - Who owns contact data quality?
   - Regular cleanup process?
   - Responsibility matrix?

6. **Segmentation Taxonomy:**
   - Final list of roles?
   - Final list of sectors?
   - Geography beyond current 3 markets?
   - Other segmentation criteria?

---

## SESSION QUOTES & INSIGHTS

**On Marketing Approach:**
- "Your marketing department is actually doing like some sales process really, right? Because you're doing RFPs" - Marcus
- "So much of what we do is relationship-based" - Team
- "We're being very selective... we're sending an email from a real person's email, rather than from info@" - Team

**On Data Quality:**
- "Poo in, poo out" - Team
- "Some people are actually working, and you have other people that are just licking everything and calling it theirs" - Kimmy
- "The data entry part of it has never been clean enough to trust in" - Team

**On Current Challenges:**
- "MailChimp gets really pissed off when you try to load in Excel because they think you're going to spam a bunch of people" - Jenny
- "Then most of it bounces anyways" - Jenny
- "Click rates aren't great so there's just really no way right now to target" - Team

**On Future Possibilities:**
- "If marketing had more insight into what some of those leads are and could see and track over time the sectors and how the market is changing, then it would be easier for that team to create proactively create content and target it" - Marketing Team

**On Events:**
- "Who manages taking attendance? No one's taking headcount" - Team
- "At our grand opening, we had people checking people in" - Team (exception, not rule)

**On Approval Philosophy:**
- "If we're going to spend the money, let's spend it this way" - Matt (on erosion review)
- "They do all day unabashedly, could care less... He's so good and quick about responding" - Team (on Matt's approval accessibility)

---

*End of Master Transcript: Marketing & CRM*


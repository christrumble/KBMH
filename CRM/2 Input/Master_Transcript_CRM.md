# MASTER TRANSCRIPT: CRM (CUSTOMER RELATIONSHIP MANAGEMENT)
## KBM Hoag NetSuite Orion Implementation

**Sources Combined:**
- CRM.txt (Plaud AI Recording - CRM Discovery)
- GMT20250917-200141_Recording.transcript.vtt (September 17, 2025 - Marketing & Lead Management Session)
- 07-29 Business Process Review_ Order Approval & Marketing Management.txt
- Relevant portions from Marketing.txt

**Date Range:** July-September 2025
**Business Process:** CRM (Lead Management, Opportunity Tracking, Sales Pipeline, Forecasting)

---

## EXECUTIVE SUMMARY

KBM Hoag's current CRM approach uses disconnected systems (Zendesk for opportunity tracking, Core for customer data, Asana for project workflows) with inconsistent data quality and manual processes between systems. The sales team's use of Zendesk is optional and variable - some diligently track opportunities while others just "lick everything and call it theirs." Lead sources are primarily relationship-based (influencers, brokers, A&D firms) rather than marketing-driven, with minimal viable leads from web forms. The shift to NetSuite will consolidate CRM functions, enforce better data quality through validation rules, provide pipeline visibility, enable accurate forecasting, and create a single integrated flow from Opportunity → Quote → Sales Order → Project.

**Key Themes:**
- Zendesk migration to NetSuite CRM
- Inconsistent data entry and quality
- Relationship-based lead generation
- Business Development vs. Account Manager roles
- Pipeline forecasting challenges
- Opportunity to quote conversion workflow
- Duplicate detection needs
- Contact role classification for segmentation

---

## CURRENT STATE ANALYSIS

### System Architecture

**Zendesk (CRM):**
- Opportunity tracking
- Lead management
- Forecasting/pipeline reporting
- Manual data entry
- **Not required** for all team members
- Inconsistent usage and data quality
- No automatic sync to other systems

**Core:**
- Order management
- Customer database (master)
- Manual transfer from Zendesk when deal closes
- Contact management (limited classifications)

**Asana:**
- RFP project request workflow
- Marketing project kickoff coordination
- Projected volume tracking vs. actual
- Resource allocation planning
- Separate from CRM/sales tracking

**Challenges:**
- Multiple disconnected systems
- Manual processes between systems
- No automatic data flow
- Limited visibility across teams
- Data quality varies widely by user
- "Dies in there" if opportunity lost (no learning)

### Lead Sources & Inputs

**Primary Lead Sources (In Order of Importance):**

**1. Relationships/Influencers (PRIMARY)**
- Business Development reps own these relationships
- General Managers manage their territory relationships
- Types of influencers:
  - Brokers
  - A&D firms (Architects & Designers)
  - Existing clients
  - Manufacturers
  - PM firms (Project Management)
  - CM firms (Construction Management)
- Tenant-in-the-market lists
- Relationship cultivation is core strategy

**2. RFPs (Significant Volume)**
- Come through existing relationships (never "cold")
- Sources:
  - Project management firms
  - A&D firms
  - Direct clients
  - Manufacturers
- "Never cold RFPs to KBM Hoag" - always relationship-based

**3. Web Contact Form (Minimal Viable Leads)**
- Most submissions non-viable:
  - Cleaning quotes (deleted)
  - "I inherited my grandmother's Newell Eames chair and need a pad for it"
  - One-off odd requests
- Occasional legitimate opportunity
- **Notable Success:** Client requesting cubicles → order for touchdown cubicles
- Jenny (Admin) qualifies and routes

**4. Referrals**
- Existing client referrals
- Manufacturer referrals
- Partner referrals
- Word-of-mouth

**Quote on Web Form Quality:**
"A lot of cleaning quotes or 'I inherited my grandmother's Newell Eames chair and need a pad for it'"

---

## TEAM STRUCTURE & ROLES

### Business Development Reps (Jill, Kate, Alex)

**Primary Function:**
- Market-facing customer acquisition
- Relationship building with influencers
- Wining and dining brokers, clients, A&D firms
- Lead generation through relationships
- Territory/market-specific focus:
  - Jill: San Francisco
  - Kate: San Jose
  - Alex: Sacramento

**Approach:**
- Different by GM/region
- Market-specific strategies
- Influencer relationship management
- Strategic account development

### Account Managers

**Role Definition:**
- "Broad on purpose" - varies by individual
- Depends on skill set and compensation structure
- Two general approaches:

**1. BD-Like Account Managers:**
- Mimic business development more closely
- Generate own leads
- Relationship-focused
- Client acquisition activities

**2. Sales Support Account Managers:**
- More project support focused
- Manage everything surrounding the project after handoff
- Less lead generation
- More execution and delivery

**Variability:**
"Role execution depends on individual skill set and comp structure"

**Project Management Responsibilities:**
- All account managers have some PM duties
- Varies by project complexity
- Coordinate with operations team
- Client relationship through project completion

---

## OPPORTUNITY MANAGEMENT (CURRENT PROCESS)

### Lead Entry (Optional - Therein Lies the Problem)

**Current Approach:**
- BD reps/GMs **may** enter opportunities in Zendesk
- **Not required** - many don't
- "Some people just licking everything and calling it theirs"
- Wide variability in what gets entered

**When Entered:**
- Assign opportunity value
- Assign probability percentage
- May or may not include:
  - Activities and tasks
  - Contact information
  - Background details
  - Next steps

**Data Quality Issues:**
- Some users diligent: Activities, tasks, contacts documented
- Some users minimal: Just claim the lead
- No validation or standards
- No accountability for completion
- Can't trust the data

**Quote (Kimmy):**
"Some people are actually working, and you have other people that are just licking everything and calling it theirs"

### Forecasting

**Purpose:**
- Account managers supposed to update opportunities
- Used for pipeline/revenue forecasting
- Executive visibility into future revenue
- Resource planning

**Accuracy Challenges:**
- Depends on who entered it
- Depends on update frequency
- Probability weighting subjective
- Value estimates vary in quality
- "The data entry part of it has never been clean enough to trust in"

**Current Reality:**
- Some forecasts accurate
- Some wildly off
- Hard to trust for planning
- Manual validation needed

### Opportunity Lifecycle

**Stages (Typical):**
1. Lead identified
2. Entered in Zendesk (maybe)
3. Qualification
4. Proposal/RFP stage
5. Negotiation
6. Close Won or Close Lost

**Close Won:**
- Manual transfer to Core
- Create customer record (if new)
- Begin order process
- Disconnect from Zendesk

**Close Lost:**
- Mark as lost
- "Dies in there"
- No automatic learning or analysis
- Minimal loss reason tracking
- No systematic follow-up

---

## NETSUITE CRM: FUTURE STATE

### Transaction Flow Integration

**Seamless Progression:**
- **Lead** → **Opportunity** → **Quote/Proposal** → **Sales Order** → **Project**
- All stages visible and linked
- Project number/name consistent across all
- Different transaction numbers but connected:
  - OP-#### (Opportunity)
  - PR-#### (Proposal)
  - SO-#### (Sales Order)

**Benefits:**
- No manual transfer between systems
- One-click conversion at each stage
- Automatic data transfer
- Complete audit trail
- Cross-functional visibility
- Maintains linkage throughout

**Quote (Marcus):**
"Opportunity → Quote → Sales Order, all stages visible and linked, project number/name consistent across all transactions"

### Lead Management

**Lead Record Capabilities:**
- Source tracking (web form, referral, event, relationship)
- Qualification status
- Assignment rules (automatic routing)
- Activity history
- Conversion to contact/customer
- Score/rating (if desired)

**Web Form Integration:**
- Contact form submission → Lead created automatically in NetSuite
- Routing rules assign to appropriate team member
- Qualification workflow
- Conversion tracking

**Current Process (Jenny):**
1. Contact form submission → Jenny (Admin)
2. Jenny qualifies lead
3. Routes to:
   - GM for new business
   - Appropriate account manager if existing client
   - Delete if junk (cleaning quotes, etc.)

**Future Process:**
- Same workflow but within NetSuite
- Better tracking of lead sources
- Conversion analysis over time
- Can nurture viable leads long-term
- Historical context maintained

### Opportunity Record

**Core Capabilities:**
- **Pipeline tracking** with stage management
- **Forecasting** with probability weighting
- **Value tracking** (projected revenue)
- **Source attribution** (where did it come from?)
- **Market/sector classification**
- **Related contacts** and relationships
- **Activity tracking** (calls, emails, meetings)
- **Document attachment** (RFPs, proposals, correspondence)
- **Team collaboration** (notes, tasks, assignments)

**Forecasting Recommendations:**
- Forecast from **Opportunity level** (not quote level)
- Prevents over-forecasting with multiple quotes
- If one opportunity has three quotes with different values:
  - Manual sync needed to update opportunity amount
  - "Someone's gonna have to manage which quote amount should go back to the opportunity"
- Accuracy depends on discipline

**Required Information (To Be Defined):**
- Minimum fields for opportunity creation
- Validation rules
- Probability guidelines by stage
- Value estimation standards
- Update frequency requirements

### Contact & Account Management

**Contact Record:**
- **Role classification** (customizable beyond Core limitations)
  - Examples: Primary Contact, Decision Maker, Finance, Procurement, Facilities, PM, Executive Sponsor, Influencer (Broker, A&D), Manufacturer Rep
- **Sector/market assignment** (Healthcare, Tech, Corporate, Government, Education, Legal, Creative, etc.)
- **Relationship type** (Client, Prospect, Influencer, Partner, Vendor)
- **Activity tracking** (all interactions logged)
- **Communication preferences**
- **Opt-in/opt-out status** (automatic management)
- **Related opportunities and projects** (full history)
- **Multiple roles per contact** (if appropriate)

**Account/Company Record:**
- Company information
- Industry/sector
- Territory assignment
- Account team
- Related contacts
- Opportunity history
- Project history
- Revenue history

**Segmentation Capabilities:**
- Unlimited custom criteria
- Role-based lists (all brokers, all A&D firms, all PMs)
- Sector-based lists (all healthcare contacts)
- Geography-based lists (San Francisco territory)
- Combined criteria (Healthcare brokers in SF)
- Dynamic vs. static lists
- Saved segments for reuse

### Activity & Task Management

**For Opportunities:**
- Follow-up tasks with due dates
- Meeting scheduling and logging
- Call logging with notes
- Email tracking (sent from NetSuite)
- Document sharing
- Team collaboration
- Reminders and alerts

**Integration with Project Management:**
- When opportunity converts to project
- Hand-off to operations/project team
- Continued visibility for BD/account manager
- Performance tracking (forecast vs. actual)
- Customer success monitoring
- Upsell/cross-sell identification

### Duplicate Detection & Management

**NetSuite Native Capabilities:**
- Duplicate detection during entry
- AI-enhanced duplicate identification
- Merge capabilities (combine records)
- Prevention of duplicate creation
- Deduplication workflows

**Current Core Limitation:**
- No duplicate detection
- Manual cleanup only
- Multiple records for same contact/company
- Data quality suffers

**Future Benefit:**
- Cleaner database
- Confident data
- Better reporting
- Improved customer experience

---

## APPROVAL WORKFLOWS & BUSINESS RULES

### Business Rule Engine Capabilities

**NetSuite/Orion Functionality:**
- Define rule criteria (flexible logic)
- Automatic routing to approvers
- Dashboard notifications for approvers
- Approval/rejection/exception handling
- Timestamp and audit trail
- Average approval time tracking per approver
- Bottleneck identification

**Example CRM-Related Rules:**
- Customer PO number missing → route to Lorraine or sales manager
- Gross margin < 16% → route to CFO
- Large order thresholds
- Missing customer information
- Credit hold situations
- Special pricing requests

**Complexity Caution:**
"More checks = slower process. Must manage approvers. Report on time-to-approve. Find balance between control and speed."

### Current Approval Process (KBM Hoag)

**Order Approval Rules:**

**1. Over $25,000:**
- Goes to Shannon (Project Coordinator Manager) for approval
- Shannon verifies completeness and readiness

**2. Missing Requirements:**
- Must have ALL of:
  - Deposit
  - Signed proposal
  - Signed drawings
  - Signed lookbook
- If any missing → approval from Matt required
- "They do all day unabashedly, could care less" (request exceptions from Matt)
- Matt: "So good and quick about responding"
- Mark is backup for Matt

**3. Erosion > $1,500 Cumulative:**
- Email approval from Matt required
- Example: $500 erosion + $1,000 more = $1,500 cumulative triggers approval
- **Purpose:** Training insight ("new person often reason for erosion")
- Problem-solving opportunity (find cheaper alternatives)
- "Sounds like a lot, but it's not that much" - happens infrequently

**Matt's Erosion Review Philosophy:**
- Not about punishment
- Identifying training needs
- Problem-solving with more experience
- **Example:** Clay's crane rental story
  - Clay: "We need to rent a crane!" ($6K-$10K plus permit plus traffic control)
  - Table doesn't fit in elevator or stairs
  - Matt's solution: Float table on top of elevator with technician on-site
  - Cost: $1,200
  - Lesson: "If we're going to spend the money, let's spend it this way"
- "Usually make the PCs do it" (submit erosion requests)

### Double Order Prevention

**Pain Point:**
- "Biggest losses from double orders"
- Same order placed twice unknowingly
- Example: 150 workstations ordered and owned before discovered (shipment notice)
- Shannon's approval supposed to catch
- Sometimes slips through

**Challenge with Automation:**
- Difficult to detect automatically
- Sometimes legitimately ordering similar items across different projects
- Sometimes ordering in bulk ("technically a 'double order' but intentional")
- Don't want constant "Are you sure?" prompts
- Users will click yes without thinking

**Potential Solution:**
- Query: Same total dollar amount within past 30 days
- Flag for manual review (not automatic rejection)
- Alert user and approver
- "Not a hard query" to build

**Action Item:** Build double-order detection query

### Vendor Credit Limits

**Need:**
- Track KBM Hoag credit limits with vendors
- Currently hit limits unexpectedly
- "Mad scramble at that nth hour because our order won't go through because we hit it"

**Solution:**
- Vendor record: Credit limit field
- Warning at percentage threshold (e.g., 90% of limit)
- Prevent PO creation if over limit
- Dashboard visibility for purchasing team
- "Sounds like just a pretty simple query"

**Implementation:**
- Field on vendor record
- Business rule for warning
- Dashboard portlet showing approaching limits
- Alert system for buyers

---

## DATA QUALITY & STANDARDIZATION

### Contact Role Classification

**Current Core Limitations:**
- Limited, unclear contact type options
  - "Are they the main contact?"
  - "Are they finance?"
  - "Is it procurement?"
- "We don't know"
- No confidence in classification
- Can't segment or target effectively

**NetSuite Flexibility:**
- Custom contact roles (unlimited options)
- Multiple roles per contact (if appropriate)
- Clear, defined roles
- Required field options (enforce entry)
- Validation rules (ensure quality)

**Proposed Roles (Examples to be Finalized):**
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

**Use Cases:**
- Targeted communication by role
- Segmented lists for campaigns
- Pipeline analysis by influencer type
- Relationship mapping
- Decision-maker visibility

### Market Sectors/Verticals

**Importance for CRM:**
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

**CRM Use Cases:**
- Opportunity forecasting by sector
- Pipeline analysis (which sectors growing?)
- Win/loss by sector (where do we win?)
- Resource allocation (focus on winning sectors)
- Territory planning
- Account strategy by sector

### Geography/Territory

**Markets:**
- San Francisco (Jill's territory)
- San Jose (Kate's territory)
- Sacramento (Alex's territory)

**Different by Market:**
- Industry mix varies (SF heavy tech, etc.)
- Client types differ
- Competitive landscape unique
- Win rates may vary
- Relationship approaches different
- Pricing strategies may differ

**CRM Needs:**
- Territory-based pipeline reporting
- BD rep performance by territory
- Opportunity assignment by geography
- Territory coverage analysis
- Market penetration metrics

### Data Entry Discipline

**Current Challenge:**
- "Poo in, poo out"
- No validation or standards
- Inconsistent entry
- Optional fields left blank
- Can't trust for reporting
- Can't segment effectively

**NetSuite Solution:**
- **Required fields** (can't save without)
- **Validation rules** (format, logic checks)
- **Picklists** (standardized options)
- **Dependent fields** (if A, then B required)
- **Default values** (reduce manual entry)
- **Duplicate prevention** (system checks)

**Cultural Change Needed:**
- Data quality becomes priority
- Recognition for good practices
- Accountability for clean data
- Regular hygiene processes
- Champion identified for data governance

**Quote:**
"The data entry part of it has never been clean enough to trust in"

---

## PIPELINE & FORECASTING

### Pipeline Management

**Visibility Needs:**
- Real-time pipeline by stage
- Pipeline by BD rep / Account Manager
- Pipeline by sector
- Pipeline by territory
- Aging analysis (opportunities stuck in stage)
- Velocity metrics (time in each stage)

**Stage Definitions (To Be Finalized):**
- Lead/Prospect
- Qualification
- Needs Analysis
- Proposal/RFP
- Negotiation
- Closed Won
- Closed Lost

**Probability by Stage:**
- To be defined (typically 10% → 90% as progress through stages)
- Consistent application needed
- Training on stage criteria
- Regular pipeline reviews

### Forecasting Accuracy

**Current Challenge:**
- Forecast accuracy varies by user
- No systematic tracking of accuracy
- Can't improve without measurement
- Executive confidence in forecast low

**NetSuite Capability:**
- Track forecast vs. actual by user
- Historical accuracy reporting
- Identify most accurate forecasters
- Learn from best practices
- Improve over time

**Forecast Types:**
- Commit (high confidence)
- Best Case (if everything goes well)
- Pipeline (everything weighted by probability)
- Historical (actual results for comparison)

### Win/Loss Analysis

**Current State:**
- "Dies in there" if lost
- Minimal loss reason tracking
- No systematic learning
- No competitor intelligence
- No pattern identification

**Future State:**
- Required loss reason codes
- Win reasons tracked too
- Competitor tracking
- Analysis by sector, size, type
- Feedback loop to improve
- Continuous learning

**Loss Reason Examples (To Be Defined):**
- Price
- Competitor
- Timing
- Requirements not met
- Relationship
- Other (specify)

---

## DASHBOARDS & ANALYTICS

### Sales/BD Dashboard

**Key Metrics:**
- My open opportunities
- My pipeline value
- My forecast (by type)
- My activities this week
- My overdue tasks
- My opportunities by stage
- Recent wins
- Opportunities needing attention

**Filters:**
- By date range
- By stage
- By sector
- By probability
- By value range

### Manager Dashboard

**Key Metrics:**
- Team pipeline
- Team forecast
- Individual performance
- Pipeline by stage
- Aging opportunities
- Win/loss trends
- Activity metrics
- Forecast accuracy by rep

**Filters:**
- "Me and My Team" (role-based)
- Individual team members
- Territory
- Sector
- Time period

**Quote (Marcus on Core Limitations):**
"That's been one of the frustrations with Core. They do allegedly have this hierarchy of permissions, roles and permissions, and, like, this is the manager. They report to that manager, and that manager is supposed to see everyone, and it doesn't. I've never gotten that."

**NetSuite Solution:**
"You have to have the right managers assigned for those filters to work. But if we set that up, if we set it up, it actually works. Good."

### Executive Dashboard

**Key Metrics:**
- Company-wide pipeline
- Forecast summary
- Pipeline by sector
- Pipeline by territory
- Win rate trends
- Average deal size
- Sales cycle length
- Conversion rates (lead → opp → customer)

**Drill-Down Capability:**
- Click any metric → see detail
- Investigate anomalies
- Identify opportunities
- Spot problems early

---

## REQUIREMENTS SUMMARY

### Functional Requirements

1. **Lead Management:**
   - Web form lead capture
   - Automatic routing
   - Qualification workflow
   - Source tracking
   - Conversion tracking

2. **Opportunity Management:**
   - Pipeline tracking by stage
   - Forecasting with probability
   - Value tracking
   - Source attribution
   - Sector/market classification
   - Activity tracking
   - Document attachment
   - Team collaboration

3. **Contact & Account Management:**
   - Role classification (custom, multiple)
   - Sector assignment
   - Relationship type
   - Activity history
   - Communication preferences
   - Opportunity/project history
   - Duplicate detection

4. **Approval Workflows:**
   - Order value thresholds
   - Missing requirements checking
   - Erosion tracking and approval
   - Double order detection
   - Vendor credit limit warnings
   - Audit trail and timestamps
   - Approval time tracking

5. **Forecasting & Analytics:**
   - Pipeline reporting
   - Forecast accuracy tracking
   - Win/loss analysis
   - Sector performance
   - Territory performance
   - Activity metrics
   - Conversion metrics

### Technical Requirements

1. **Integrations:**
   - Web contact form → NetSuite lead creation
   - Email integration (individual user credentials)
   - Calendar integration (if needed)
   - Document management (Google Drive linking)

2. **Customizations:**
   - Custom contact roles
   - Custom sectors/markets
   - Approval rules configuration (up to 10 rules)
   - Business rule engine setup
   - Double-order detection query
   - Vendor credit limit warnings
   - Custom dashboards by role

3. **Data Migration:**
   - Opportunity history from Zendesk
   - Contact data from Core
   - Account data from Core
   - Historical customer data
   - Contact classification/segmentation
   - Deduplication during migration

4. **Reports/Dashboards:**
   - Sales/BD rep dashboard
   - Manager dashboard
   - Executive dashboard
   - Pipeline reports
   - Forecast accuracy reports
   - Win/loss analysis
   - Activity reports
   - Approval time tracking

---

## DECISIONS & ACTION ITEMS

### Decisions Made

1. **Zendesk Migration:** Migrate to NetSuite CRM
   - Opportunity history to be imported
   - NetSuite becomes system of record
   - Zendesk to be retired

2. **Data Quality Focus:** Critical for success
   - Validation rules to be implemented
   - Required fields to be defined
   - Contact roles to be standardized
   - Sector classifications to be finalized
   - Regular cleanup processes

3. **Opportunity Entry:** Will become required (not optional)
   - Minimum fields to be defined
   - Training on importance
   - Accountability for compliance
   - Management oversight

4. **Approval Workflows:** Migrate current rules to NetSuite
   - Shannon to document current flowchart
   - Up to 10 rules in BRD budget
   - Double-order detection query to be built
   - Vendor credit limits to be tracked

5. **Forecasting:** Opportunity-level (not quote-level)
   - Prevent over-forecasting
   - Accuracy tracking by user
   - Continuous improvement approach

6. **Win/Loss Tracking:** Will be implemented
   - Required reason codes
   - Competitor tracking
   - Analysis for continuous learning

### Action Items

1. **Shannon:** Document approval workflow rules (flowchart)
2. **Sales/BD Team:** Define lead sources for tracking
3. **All:** Define contact roles taxonomy (final list)
4. **All:** Define sector/market classifications (final list)
5. **All:** Define opportunity stages and probabilities
6. **All:** Define win/loss reason codes
7. **All:** Identify who should manage contact data quality (owner)
8. **Marcus/Team:** Build double-order detection query

---

## PAIN POINTS TO SOLVE

### Current Frustrations

1. **Disconnected Systems:**
   - Zendesk → Core manual transfer
   - No integrated visibility
   - Opportunities "die" in Zendesk if lost
   - No learning from losses
   - Manual work between systems

2. **Data Quality:**
   - Inconsistent entry in Zendesk
   - Optional = ignored by many
   - "Some people just licking everything"
   - Can't trust for forecasting
   - Can't segment contacts
   - "Poo in, poo out"

3. **No Pipeline Visibility:**
   - Executive visibility limited
   - Can't see team pipeline easily
   - Can't track trends
   - Forecast accuracy unknown
   - No bottleneck identification

4. **Limited Collaboration:**
   - Siloed information
   - Account team can't see full picture
   - Handoff from sales to operations unclear
   - No activity history
   - Duplicate efforts

5. **No Learning from Losses:**
   - Lost opportunities disappear
   - No systematic analysis
   - No competitor intelligence
   - Can't identify patterns
   - Repeat mistakes

6. **Contact Management:**
   - Duplicate records (no detection)
   - Poor classification
   - Can't segment effectively
   - No relationship mapping
   - Limited contact information

### Future State Solutions

1. **Single Integrated System:**
   - Lead → Opportunity → Quote → Order in one platform
   - Automatic data flow (no manual transfer)
   - Real-time visibility across teams
   - Complete audit trail
   - Team collaboration enabled

2. **Data Quality:**
   - Validation rules enforce standards
   - Required fields ensure completeness
   - Standardized classifications
   - Duplicate prevention
   - Regular hygiene processes
   - Accountability and ownership

3. **Pipeline Visibility:**
   - Real-time dashboards
   - Drill-down capability
   - Trend analysis
   - Bottleneck identification
   - Forecast accuracy tracking
   - Continuous improvement

4. **Enhanced Collaboration:**
   - Shared visibility
   - Activity tracking
   - Document sharing
   - Task management
   - Clear handoffs
   - Team coordination

5. **Learning from Losses:**
   - Required loss reasons
   - Competitor tracking
   - Pattern analysis
   - Sector/territory insights
   - Strategy refinement
   - Continuous improvement

6. **Contact Management:**
   - Duplicate detection
   - Proper classification
   - Effective segmentation
   - Relationship mapping
   - Complete contact information
   - Role-based visibility

---

## CHANGE MANAGEMENT CONSIDERATIONS

### Behavior Changes Required

1. **Consistent CRM Data Entry:**
   - Currently optional → Will become required
   - "Not required" → Required for visibility
   - Minimal entry → Complete information
   - Variability → Standardization

2. **Earlier Opportunity Creation:**
   - Currently: Enter when ready to forecast
   - Future: Create at first knowledge of potential
   - Capture more early-stage opportunities
   - Better pipeline visibility

3. **Activity Logging:**
   - Currently: Minimal or none
   - Future: Log all significant interactions
   - Calls, meetings, emails tracked
   - History maintained for team

4. **Data Quality Discipline:**
   - Required fields completion
   - Contact role classification
   - Sector assignment
   - Validation rule compliance
   - Regular updates

### Resistance Points

1. **Sales Team Pushback:**
   - "Matt's philosophy: Sales will be our biggest pushback"
   - May resist structure
   - Data entry seen as overhead
   - "Licking everything" behavior needs to change
   - Need to demonstrate value

2. **Time Investment:**
   - Data entry takes time
   - Activity logging feels like bureaucracy
   - Need to show ROI (better forecasting, reduced manual work elsewhere)
   - Quick wins essential

3. **Process Changes:**
   - Comfortable with current Zendesk + Core + Asana mix
   - New system = new learning
   - Temporary productivity dip expected
   - Change fatigue possible

4. **Accountability:**
   - Data quality becomes visible
   - Forecast accuracy tracked
   - Activity levels measurable
   - Performance transparency
   - May create discomfort

### Success Factors

1. **Executive Sponsorship:**
   - Matt's support critical
   - Clear expectations set
   - Accountability for usage
   - Recognition for compliance
   - Consequences for non-compliance

2. **Show Value Fast:**
   - Pipeline visibility (immediate)
   - Forecast accuracy (measurable improvement)
   - Win/loss insights (strategic value)
   - Reduced manual work (time savings)
   - Better team collaboration

3. **Training & Support:**
   - Role-specific training
   - Sales/BD-focused approach
   - Quick reference guides
   - NetSuite champions identified
   - Ongoing support available
   - Documentation accessible

4. **Data Quality Campaign:**
   - Clean data from start (migration)
   - Regular hygiene (ongoing)
   - Recognition for good practices
   - Gamification possible
   - Shared ownership

5. **Incremental Adoption:**
   - Start with core functionality
   - Add sophistication over time
   - Build confidence gradually
   - Celebrate wins
   - Learn and adjust

---

## INTEGRATION WITH OTHER PROCESSES

### Connection to Marketing
- Lead capture from web forms
- Lead qualification and routing
- Contact segmentation shared
- Opportunity visibility for market intelligence
- Campaign source attribution
- Event attendee follow-up

### Connection to Order Management
- Opportunity → Quote conversion (one-click)
- Quote → Sales Order conversion
- Customer data sync
- Project assignment
- Commission tracking
- Performance metrics

### Connection to Financial
- Revenue forecasting from pipeline
- Opportunity value aggregation
- Commission calculations
- Credit checks
- Financial approvals
- Payment terms

### Connection to Operations
- Project kickoff from won opportunities
- Customer contact info for project team
- Resource planning from pipeline
- Capacity planning
- Hand-off workflow

### Connection to Business Intelligence
- Pipeline reporting
- Forecast accuracy analysis
- Win/loss trends
- Sector performance
- Territory performance
- Conversion metrics
- Source attribution

---

## TRAINING NEEDS

### Sales/BD Team
- Opportunity creation and management
- Activity logging best practices
- Contact role classification
- Forecasting and probability
- Pipeline management
- Stage progression criteria
- Win/loss reason selection
- Dashboard usage

### Account Managers
- Opportunity updates
- Contact management
- Activity tracking
- Quote creation from opportunity
- Handoff to operations
- Customer success tracking
- Upsell/cross-sell opportunity identification

### Admin (Jenny)
- Lead qualification and routing
- Web form lead management
- Contact database maintenance
- Duplicate detection and merge
- Data quality monitoring
- User support

### Managers (GMs)
- Team dashboard usage
- Pipeline reviews
- Forecast management
- Performance coaching
- Data quality oversight
- Report customization

---

## OPEN QUESTIONS FOR FUTURE SESSIONS

1. **Opportunity Stages:**
   - Final stage names?
   - Criteria for each stage?
   - Probability by stage?
   - Required fields by stage?

2. **Contact Ownership:**
   - Who owns contact data quality?
   - Regular cleanup process?
   - Responsibility matrix?
   - Data governance structure?

3. **Activity Logging:**
   - What activities must be logged?
   - Which are optional?
   - Automated activity capture?
   - Email integration level?

4. **Forecasting Process:**
   - Weekly, monthly reviews?
   - Who participates?
   - Accountability structure?
   - Accuracy targets?

5. **Win/Loss Analysis:**
   - Reason code taxonomy (final)?
   - Competitor list?
   - Review frequency?
   - Action planning process?

6. **Territory Assignment:**
   - Hard assignment vs. overlay?
   - How to handle shared accounts?
   - Split credit scenarios?
   - Reporting by territory?

7. **Account Planning:**
   - Strategic account identification?
   - Account planning process?
   - Review cadence?
   - Integration with CRM?

---

## SESSION QUOTES & INSIGHTS

**On Data Quality:**
- "Poo in, poo out" - Team
- "Some people are actually working, and you have other people that are just licking everything and calling it theirs" - Kimmy
- "The data entry part of it has never been clean enough to trust in" - Team

**On Current System:**
- "Dies in there" if opportunity lost (no learning)
- "Not required" for CRM entry (inconsistent usage)
- Zendesk → Core manual transfer (disconnected systems)

**On Roles:**
- "Broad on purpose" - Account Manager role variability
- "Role execution depends on individual skill set and comp structure"

**On Approval Philosophy (Matt's Erosion Review):**
- "If we're going to spend the money, let's spend it this way"
- "He's so good and quick about responding"
- "Usually make the PCs do it" (submit erosion requests)
- Clay's crane story: $10K crane vs. $1.2K elevator technician solution

**On Double Orders:**
- "Biggest losses from double orders"
- "150 workstations ordered and owned" before discovered

**On Lead Sources:**
- "Never cold RFPs to KBM Hoag" - always relationship-based
- Web forms: "A lot of cleaning quotes or 'I inherited my grandmother's Newell Eames chair and need a pad for it'"

**On Change Management:**
- "Matt's philosophy: Sales will be our biggest pushback"

**On NetSuite vs. Core:**
- "You have to have the right managers assigned for those filters to work. But if we set that up, if we set it up, it actually works." - Marcus on org structure

---

*End of Master Transcript: CRM*


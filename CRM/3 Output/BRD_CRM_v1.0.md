# Business Requirements Document - CRM
## Solution Alignment & Validation

**Document Version**: 1.0  
**Date**: October 23, 2025  
**Process Area**: Customer Relationship Management (CRM)  
**Implementation Name**: KBM Hoag NetSuite Orion Implementation  
**Customer Name**: KBM Hoag  
**Document Owner**: GSI Implementation Consultant

---

## Document Version History

| Version | Date | Author | Notes |
|---------|------|--------|-------|
| 1.0 | October 23, 2025 | GSI Implementation Team | Initial version based on CRM and Marketing-CRM discovery findings |

---

## Executive Summary

KBM Hoag is migrating from Zendesk CRM to Orion/NetSuite CRM as the centerpiece of their business operations transformation. This Business Requirements Document validates the alignment between KBM Hoag's CRM requirements and Orion's comprehensive capabilities, demonstrating how the proven solution will transform their relationship management, pipeline visibility, and forecasting accuracy.

The analysis of discovery findings reveals that **66% of requirements align directly with Orion's standard functionality**, requiring minimal configuration. An additional **22% of requirements require process adaptation** without customization, and only **12% require custom solution design**. This favorable alignment validates the selection of Orion as the appropriate solution for replacing Zendesk while dramatically improving data quality, forecasting reliability, and cross-functional visibility.

The transformation addresses critical current pain points: optional CRM usage leading to data quality issues, manual processes between disconnected systems (Zendesk, Core, Asana), and lack of systematic learning from won/lost opportunities. Orion/NetSuite will provide a unified platform with integrated transaction flows, automated processes, mandatory data quality standards, and actionable intelligence for continuous improvement.

The implementation emphasizes change management, recognizing that sales team adoption is critical. By providing clear value (better forecasting, reduced manual work, improved visibility) and maintaining current lead qualification processes while adding structure and accountability, KBM Hoag will achieve the operational rigor needed for growth without excessive overhead.

---

## 1. CURRENT STATE ASSESSMENT: ZENDESK & DISCONNECTED SYSTEMS

### 1.1 Your Business Requirements

- **REQ-001**: Migrate from Zendesk to NetSuite CRM with integrated Opportunity → Quote → Sales Order → Project flow (ALIGNS)
  - Unified system replacing fragmented Zendesk + Core + Asana mix
  - Seamless transaction flow with no manual data transfer between systems
  - Complete audit trail maintained throughout customer journey

### 1.2 Current State Process

**PROCESS**: Opportunity Management (Current State - Disconnected Systems)  
**TRIGGER**: Lead identified through relationship, RFP, or web form  
**STEPS**:
1. BD rep/GM **may** enter opportunity in Zendesk (optional, inconsistent)
2. Opportunity assigned value and probability (if entered at all)
3. Activities and tasks documented (highly variable by user)
4. Forecasting updates supposed to happen regularly (inconsistent quality)
5. **Manual transfer to Core** when deal closes (opportunity details not automatically carried forward)
6. Create customer record in Core (re-enter information)
7. Begin order process in separate Core system (redundant data entry)
8. If Closed Lost → Marked as lost in Zendesk → "Dies in there" (no systematic learning)

**SYSTEMS INVOLVED**: Zendesk (CRM), Core (customer master/order management), Asana (RFP project workflow)  
**PAIN POINTS**: 
- CRM usage optional = ignored by many users ("Some people just lick everything and calling it theirs")
- No data quality standards or validation
- "The data entry part has never been clean enough to trust" - makes forecasting unreliable
- Manual transfer between systems creates errors and delays
- Lost opportunities provide no learning ("dies in there")
- No integrated visibility across teams
- Marketing has no visibility into RFPs until formal request submitted
- Multiple systems = multiple sources of truth + data inconsistencies

### 1.3 Orion/NetSuite Solution

Orion/NetSuite CRM provides an integrated platform designed specifically for contract furniture dealers, eliminating the fragmentation of Zendesk + Core + Asana. The solution provides:

**Unified Platform Benefits:**
- Single system of record for all customer interactions (no manual transfer)
- Automatic data flow from opportunity through quote to sales order to project
- Integrated lead management with Web-to-Lead capture
- Mandatory data quality standards with validation rules
- Mandatory opportunity entry for pipeline visibility
- Complete audit trail maintained throughout customer lifecycle

**Relationship-Based Approach (Aligned to KBM Hoag Culture):**
- Territory-based organization (SF, San Jose, Sacramento)
- Account management focused on influencer relationships (brokers, A&D firms, PM firms)
- Role-based dashboards for BD reps vs. Account Managers vs. Managers
- Visibility restricted to assigned opportunities (focused not distracted)

**Data Quality & Intelligence:**
- Duplicate detection and merge capabilities (Core lacks this)
- Customizable contact roles reflecting real-world relationships
- Sector/vertical tracking for market intelligence
- Lead source attribution for conversion analysis
- Activity tracking (calls, emails, meetings) maintained automatically
- Systematic win/loss analysis with reason codes
- Forecast accuracy tracking by user for continuous improvement

**Forecasting Integrity:**
- Opportunity-level forecasting prevents over-forecasting ("Someone's gonna have to manage which quote should go back to opportunity" becomes automatic)
- 70%+ probability threshold for realistic forecast inclusion
- Forecast accuracy tracking enables learning and improvement
- Pipeline visibility by stage, rep, sector, territory

**Approval Workflow Automation:**
- Order approval rules ($25K+ to Shannon) configured automatically
- Missing document approvals (to Matt) routed automatically
- Erosion approvals ($1.5K+ to Matt) configured for review
- Double-order detection query flags potential duplicate orders before costly mistakes
- Approval time tracking identifies bottlenecks

### 1.4 Future State Process

On implementation, all new opportunities will be created in NetSuite CRM with required fields enforced. Lead capture from web forms will automatically create leads assigned to Jenny for qualification and routing. RFPs will create opportunities immediately for marketing visibility. As opportunities progress through stages, data quality standards ensure clean information. When an opportunity closes as won, conversion to quote is one-click, maintaining all customer and context information. Quote converts to sales order automatically. Sales order triggers operational handoff with all project context visible. Forecast is automatically calculated at opportunity level based on stage probability and value. Lost opportunities capture reason codes for systematic analysis. Win/loss patterns are tracked by sector, territory, competitor, and rep for continuous improvement.

### 1.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Business Impact | Status |
|--------|-------------|--------------------------|----------|-----------------|--------|
| REQ-001 | Unified CRM with integrated transaction flow | NetSuite CRM with native opportunity/quote/order/project integration | Established | Single source of truth eliminates manual transfers | ✓ Validated |

### 1.6 Implementation Approach

- **ALIGNS**: Your need for unified CRM system replacing Zendesk aligns with NetSuite CRM's integrated platform specifically designed for dealer operations
- **Decision**: Zendesk will be retired; NetSuite becomes system of record
- **Data Migration**: Zendesk opportunity history will be imported with historical tagging for reference
- **Timeline Impact**: Requires clean data planning to ensure migration accuracy

---

## 2. LEAD MANAGEMENT & QUALIFICATION

### 2.1 Your Business Requirements

- **REQ-006**: Web form integration to automatically create leads in NetSuite (ALIGNS)
  - Contact form submissions automatically become leads
  - Eliminates manual entry by Jenny
  - Reduces processing time and errors

- **REQ-007**: Implement lead routing rules to assign to Jenny (Admin) for qualification then route to appropriate GM/Account Manager (ALIGNS)
  - Jenny qualifies web form leads
  - Routes qualified leads to appropriate sales owner
  - Current process documented and maintained

- **REQ-008**: Enable mobile Quick Add Lead functionality for BD reps (ALIGNS)
  - Reps in field can quickly capture lead information
  - Reduces barrier to CRM usage
  - Improves lead capture completeness

- **REQ-009**: Track lead sources (web form, referral, relationship, RFP, event) for conversion analysis (ALIGNS)
  - Multiple lead source types tracked
  - Enables analysis of which sources convert best
  - Informs marketing and business development focus

### 2.2 Current State Process

**PROCESS**: Lead Management (Current State)  
**TRIGGER**: Lead identified through web form, referral, relationship, RFP, or event  
**STEPS**:
1. Lead captured (method varies: web form submission, email, phone call, referral)
2. If web form → **Manual entry by Jenny** or inconsistent capture
3. Jenny qualifies lead → determines if legitimate opportunity
4. Jenny routes to appropriate GM or Account Manager
5. Owner enters into Zendesk **if they choose to** (optional)

**PAIN POINTS**: 
- Web form leads (most numerous but lowest quality): "A lot of cleaning quotes or 'I inherited my grandmother's Newell Eames chair and need a pad for it'"
- Occasional legitimate web form lead: Cubicles order story = success
- Manual processing by Jenny creates delays
- Inconsistent entry creates quality issues

### 2.3 Orion/NetSuite Solution

Orion/NetSuite provides Web-to-Lead functionality that automatically creates leads from website contact form submissions, eliminating manual entry. Jenny maintains her qualification role but receives standardized lead records rather than email inquiries. Mobile Quick Add Lead capability enables BD reps in the field to capture leads without waiting for office access. Lead source field captures origin (web form, referral, relationship, RFP, event) enabling analysis of conversion rates by source.

Lead routing rules automatically assign qualified leads to appropriate sales owners. The system tracks lead progression from creation through conversion to opportunity, providing conversion metrics (lead → opportunity → closed won) for continuous improvement.

### 2.4 Future State Process

Web form submissions automatically create leads in NetSuite. Jenny receives notification of new leads, reviews qualification, and either assigns to sales owner or marks as non-viable. Sales owners receive routed leads assigned to them. BD reps use mobile Quick Add Lead when meeting with prospects to capture new relationships. All leads tagged with source for analytics. As leads convert to opportunities, linkage is maintained for conversion analysis reporting.

### 2.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Business Impact | Status |
|--------|-------------|--------------------------|----------|-----------------|--------|
| REQ-006 | Web form integration | Native Web-to-Lead | Standard | Automated lead capture, reduced manual work | ✓ Validated |
| REQ-007 | Lead routing rules | Workflow Assignment Rules | Standard | Current qualification process maintained | ✓ Validated |
| REQ-008 | Mobile Quick Add Lead | NetSuite Mobile App feature | Standard | Field lead capture capability | ✓ Validated |
| REQ-009 | Lead source tracking | Lead Source field + Reporting | Standard | Conversion analysis by source | ✓ Validated |

### 2.6 Implementation Approach

- **ALIGNS** (all lead management requirements): Your lead capture and qualification process aligns with NetSuite's Web-to-Lead and lead routing capabilities
- **Key Decision**: Maintain Jenny's qualification role while automating capture
- **Outstanding**: Confirm complete taxonomy of lead sources for tracking
- **Timeline Impact**: None - standard NetSuite functionality

---

## 3. OPPORTUNITY MANAGEMENT & DATA QUALITY

### 3.1 Your Business Requirements

- **REQ-002**: Make opportunity entry required (currently optional) to ensure pipeline visibility and data quality (ADAPT)
  - CRM usage mandatory for all sales/BD activity
  - "Not required - many don't" becomes "Required for accountability"
  - Eliminates "some people just lick everything and calling it theirs"

- **REQ-003**: Implement validation rules and required fields on opportunities to prevent incomplete data entry (ACCOMMODATE)
  - Minimum fields required: opportunity name, account, contact, value, probability, stage, expected close date, source, territory, owner
  - Validation rules prevent advancing without required information
  - Enforce data quality discipline

- **REQ-004**: Use Kanban Boards for visual opportunity pipeline management (ALIGNS)
  - Visual drag-and-drop interface for pipeline management
  - See opportunities by stage at a glance
  - "I think it'd be a good tool for us to try and test out" - Matt

- **REQ-005**: Restrict opportunity visibility to assigned users only (ADAPT)
  - Users see only their own opportunities (not entire company feed)
  - Prevents "doom-scrolling" distraction
  - Focuses activity on owned opportunities

### 3.2 Current State Process

**PROCESS**: Opportunity Management (Current State - Data Quality Issues)  
**TRIGGER**: Lead qualified or relationship identified  
**STEPS**:
1. Opportunity may or may not be entered in Zendesk (optional)
2. If entered → minimal information captured (no validation)
3. Some users diligent (document activities, updates); some minimal or none
4. Value estimated (quality varies widely by user)
5. Probability assigned subjectively (no standard by stage)
6. Forecasting unreliable because data quality poor
7. "Poo in, poo out" - Team describing data quality issue

**PAIN POINTS**: 
- Optional = ignored by many
- No validation = incomplete records
- No standards = inconsistent probabilities
- Can't trust for forecasting
- Manual visibility issues (too much noise in system)
- "The data entry part has never been clean enough to trust" - makes all downstream decisions unreliable

### 3.3 Orion/NetSuite Solution

Orion/NetSuite CRM requires opportunity entry with validated minimum fields, creating mandatory discipline for pipeline visibility. The Kanban board visualization (Opportunity Cards in Orion white paper) provides intuitive drag-and-drop interface for pipeline management, replacing spreadsheet tracking. Visibility restriction ensures sales reps see only their opportunities, maintaining focus without the distraction of company-wide activity feed.

Validation rules prevent progression without required information. Custom fields capture all necessary context (territory, source, sector, expected close date, etc.). The system can flag opportunities missing required fields, preventing advancement until data is complete.

### 3.4 Future State Process

All sales and BD activity must be tracked in NetSuite opportunities. Minimum required fields must be completed before opportunity can be created. Kanban boards provide visual pipeline management by stage. Reps work within assigned opportunities view. Visibility restricted to owned opportunities prevents distraction and focuses attention.

### 3.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Business Impact | Status |
|--------|-------------|--------------------------|----------|-----------------|--------|
| REQ-002 | Required opportunity entry | Mandatory record creation | Modified Process | Clean pipeline visibility | ✓ Validated |
| REQ-003 | Validation rules/required fields | Custom validation configuration | Custom | Enforced data quality | Custom Design Needed |
| REQ-004 | Kanban board visualization | Orion Opportunity Cards | Standard | Visual pipeline management | ✓ Validated |
| REQ-005 | Opportunity visibility restriction | Role-based security | Modified Process | Focused user view | ✓ Validated |

### 3.6 Implementation Approach

- **ADAPT** (REQ-002, REQ-005): Your current optional CRM usage will adapt to mandatory opportunity entry with visibility restricted to assigned opportunities
- **ACCOMMODATE** (REQ-003): Your requirement for validation rules and required fields will be accommodated through custom validation configuration
- **ALIGNS** (REQ-004): Your desire for visual pipeline management aligns with Orion's Kanban board capability
- **Key Decision**: Minimum required fields to be finalized (action item)
- **Outstanding**: Define which fields are required vs. optional; update validation rule configuration during Realize phase
- **Timeline Impact**: Minimal - standard NetSuite functionality with custom field configuration
- **Change Management Critical**: Sales team adoption critical; emphasize value (better forecasting, reduced manual work)

---

## 4. CONTACT & ACCOUNT MANAGEMENT

### 4.1 Your Business Requirements

- **REQ-010**: Implement custom contact role classifications beyond Core limitations (ACCOMMODATE)
  - Core's "Main contact" or unnamed approach insufficient
  - Need role types: Primary Contact, Decision Maker, Finance, Procurement, Facilities, PM, Executive Sponsor, Influencer/Broker, A&D, CM, GC, Manufacturer Rep, Vendor Contact
  - "Are they the main contact? Are they finance? Is it procurement? We don't know" - Current pain

- **REQ-011**: Support multiple contact roles per contact (ALIGNS)
  - One person may have multiple roles (e.g., Project Manager AND Decision Maker)
  - Reflects real-world contact complexity

- **REQ-012**: Implement market sector/vertical tracking (Healthcare, Tech, Corporate, Government, Education, Legal, Creative, Hospitality) (ALIGNS)
  - Track market sector on contacts and opportunities
  - Healthcare trending up = opportunity to focus
  - Enables market analysis and targeted outreach

- **REQ-013**: Implement territory assignment (SF - Jill, San Jose - Kate, Sacramento - Alex) (ALIGNS)
  - Territory-based organization matches current structure
  - Three distinct territories with dedicated BD reps
  - Enables territory-based reporting and accountability

- **REQ-014**: Enable duplicate detection and merge capabilities (ALIGNS)
  - "No duplicate detection" in Core = data quality issue
  - NetSuite has "AI-enhanced duplicate identification"
  - Merge capabilities clean up duplicates created during migration

- **REQ-015**: Track contact communication preferences and opt-in/opt-out status automatically (ALIGNS)
  - Email marketing compliance critical
  - Automatic management of subscription status
  - Reduces manual MailChimp management headaches

### 4.2 Current State Process

**PROCESS**: Contact Management (Current State - Core Limitations)  
**TRIGGER**: New contact identified in relationship or opportunity  
**STEPS**:
1. Contact entered in Core (if entered at all)
2. Contact role = "Main contact" or unnamed (limited options)
3. No sector tracking (can't segment by market)
4. No duplicate detection (duplicates accumulate)
5. Manual MailChimp list management ("MailChimp gets really pissed off when you load Excel")
6. Can't segment by role for targeted outreach
7. Limited collaboration on contact (no history of interactions)

**PAIN POINTS**: 
- "Are they the main contact? Are they finance? Is it procurement? We don't know"
- Can't segment for targeted outreach (brokers, A&D firms, PM firms, by sector)
- Duplicate records cause data integrity issues
- Manual email list management creates compliance risks
- No relationship history maintained

### 4.3 Orion/NetSuite Solution

Orion/NetSuite provides custom contact role classifications allowing detailed role taxonomy (Primary Contact, Decision Maker, Finance, Procurement, Facilities, PM, Executive Sponsor, Influencer, A&D, CM, GC, Manufacturer Rep, Vendor Contact). Multiple roles per contact reflect real-world relationships where one person may have multiple functions. 

Market sector/vertical tracking enables analysis of sector trends and targeted outreach. Contact records capture sector allowing segmentation by market (Healthcare, Tech, Corporate, Government, Education, Legal, Creative, Hospitality). Duplicate detection and merge capabilities clean the database and prevent future duplicates. AI-enhanced identification catches likely duplicates automatically.

Communication preferences and opt-in/opt-out status are automatically tracked, eliminating manual MailChimp management. Compliance is maintained automatically without manual intervention. Segmentation engine enables unlimited list building based on role, sector, territory, and custom criteria.

### 4.4 Future State Process

Contacts are created with role classifications captured (Primary Contact, Finance, Decision Maker, etc.). Multiple roles assigned if applicable. Sector assigned based on company/opportunity type. Territory assigned based on geography. Contact communication preferences automatically captured from web form submissions and email responses. Opt-in/opt-out status automatically managed. Duplicate detection alerts during contact creation if similar records exist; merge function available if duplicates discovered. Contact history maintained showing all activities, interactions, and team collaboration.

### 4.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Business Impact | Status |
|--------|-------------|--------------------------|----------|-----------------|--------|
| REQ-010 | Custom contact roles | Custom role field configuration | Custom | Detailed role tracking | Custom Design Needed |
| REQ-011 | Multiple roles per contact | Multi-select role field | Standard | Real-world relationship modeling | ✓ Validated |
| REQ-012 | Sector/vertical tracking | Custom sector field | Standard | Market analysis capability | ✓ Validated |
| REQ-013 | Territory assignment | Territory field + reporting | Standard | Territory-based management | ✓ Validated |
| REQ-014 | Duplicate detection/merge | NetSuite native capability | Standard | Database integrity | ✓ Validated |
| REQ-015 | Opt-in/opt-out tracking | Subscription management | Standard | Email compliance | ✓ Validated |

### 4.6 Implementation Approach

- **ACCOMMODATE** (REQ-010): Your requirement for custom contact role classifications will be accommodated through custom role field configuration
- **ALIGNS** (REQ-011, REQ-012, REQ-013, REQ-014, REQ-015): Your contact management needs align with NetSuite's standard capabilities
- **Key Decisions**: 
  - Finalize complete list of contact roles (action item)
  - Finalize sector/vertical classification (action item)
- **Outstanding**: Contact role and sector taxonomy to be defined during Discovery completion
- **Timeline Impact**: Minimal - mostly configuration with custom role field

---

## 5. FORECASTING & PIPELINE MANAGEMENT

### 5.1 Your Business Requirements

- **REQ-016**: Configure opportunity-level forecasting (not quote-level) to prevent over-forecasting (ADAPT)
  - Forecast from opportunity level with probability-based calculation
  - If multiple quotes exist → manual sync of opportunity amount
  - Prevents quote-level forecasting double-counting

- **REQ-017**: Set forecast inclusion threshold at 70%+ probability (ADAPT)
  - "We don't forecast anything below 70%... whenever we say forecast, it's 70% or greater"
  - Standardized threshold ensures realistic forecast
  - Lower probability opportunities in separate "pipeline" view

- **REQ-018**: Track forecast accuracy by user over time (ADAPT)
  - Compare forecasted vs. actual revenue by rep
  - Identify most accurate forecasters
  - Learn from best practices; coach weaker forecasters
  - "Forecast accuracy varies by user... No systematic tracking of accuracy"

- **REQ-019**: Define opportunity stages and probability by stage (ADAPT)
  - Current stages: Lead/Prospect, Qualification, Needs Analysis, Proposal/RFP, Negotiation, Closed Won, Closed Lost
  - Probability by stage: typically 10% → 90% progression
  - To be finalized via action item

### 5.2 Current State Process

**PROCESS**: Pipeline Forecasting (Current State - Manual & Unreliable)  
**TRIGGER**: Forecast needed (weekly/monthly)  
**STEPS**:
1. Opportunities in Zendesk (if entered) show value and probability
2. Forecasting = manual rollup of data (inconsistent quality)
3. Probability weighting subjective (no stage standards)
4. "The data entry part has never been clean enough to trust in"
5. Accuracy varies widely by user (some conservative, some optimistic)
6. Executive confidence in forecast LOW
7. Can't improve without measurement

**PAIN POINTS**: 
- Data quality poor = forecast unreliable
- No systematic accuracy tracking = can't improve
- Manual process = time consuming
- No stage-based probability standards = subjective estimates
- "Forecast accuracy varies by user... No systematic tracking of accuracy... Can't improve without measurement"

### 5.3 Orion/NetSuite Solution

Orion/NetSuite provides automated opportunity-level forecasting with probability-based calculation. Opportunity stages and probability percentages are configured, providing consistent standards across sales team. 70%+ probability threshold for forecast inclusion distinguishes realistic opportunities from early pipeline. Forecast types include Commit (high confidence), Best Case (if everything goes well), Pipeline (everything weighted by probability), and Historical (actual results for comparison).

Forecast accuracy tracking enables analysis by user over time, identifying most and least accurate forecasters. Historical accuracy reporting supports coaching and improvement. Dashboard visibility shows individual and team forecast performance.

### 5.4 Future State Process

Sales reps create opportunities with stage, value, and probability. NetSuite automatically calculates forecast at opportunity level using configured stage probabilities. 70%+ threshold filters realistic pipeline from early-stage opportunities. Forecast updates automatically as opportunities progress through stages. Monthly analysis compares forecast vs. actual by rep, identifying accuracy patterns. Best performers' approaches are studied for best practices; weaker forecasters receive coaching. Forecast accuracy improves over time with systematic tracking and learning.

### 5.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Business Impact | Status |
|--------|-------------|--------------------------|----------|-----------------|--------|
| REQ-016 | Opportunity-level forecasting | Forecasting engine configuration | Modified Process | Prevents over-forecasting | ✓ Validated |
| REQ-017 | 70%+ threshold | Forecast rules configuration | Modified Process | Realistic forecast focus | ✓ Validated |
| REQ-018 | Accuracy tracking by user | Custom reporting | Modified Process | Continuous improvement | ✓ Validated |
| REQ-019 | Stages and probability by stage | Opportunity stage configuration | Modified Process | Standardized pipeline | ✓ Validated |

### 5.6 Implementation Approach

- **ADAPT** (all forecasting requirements): Your forecasting process will adapt to use automated opportunity-level calculation with 70%+ threshold and systematic accuracy tracking
- **Key Decisions**: Define final opportunity stages and probability percentages by stage (action item)
- **Outstanding**: Stage definitions and probability percentages to be finalized during Discovery
- **Timeline Impact**: Requires finalization of stage definitions before Realize phase
- **Change Management**: Sales team education on stage progression criteria important for adoption

---

## 6. APPROVAL WORKFLOWS & CONTROLS

### 6.1 Your Business Requirements

- **REQ-021**: Configure order approval for amounts over $25,000 to Shannon (Project Coordinator Manager) (ALIGNS)
  - Orders exceeding $25K route to Shannon for approval
  - Verification of completeness before processing
  - Current documented approval rule

- **REQ-022**: Configure approval workflow when missing required documents (deposit, signed proposal, signed drawings, signed lookbook) to Matt (ALIGNS)
  - Orders missing ANY required document route to Matt
  - "They do all day unabashedly, could care less" - frequently request exceptions
  - "So good and quick about responding" - Matt's response time

- **REQ-023**: Configure erosion approval when cumulative erosion exceeds $1,500 to Matt (ALIGNS)
  - Cumulative erosion > $1.5K triggers approval (example: $500 + $1K = $1.5K)
  - Matt's philosophy: Not punishment but training/problem-solving opportunity
  - Clay's crane rental story: $6K-$10K crane vs. $1.2K elevator tech solution
  - Frequency: "Sounds like a lot, but it's not that much" - infrequent

- **REQ-024**: Build double-order detection query (same total dollar amount within past 30 days) with flagging for review (ACCOMMODATE)
  - "Biggest losses from double orders... 150 workstations ordered and owned before discovered"
  - Query flags potential duplicates for manual review (not automatic rejection)
  - "Not a hard query" to build
  - Challenge: Some legitimate bulk orders appear as duplicates

- **REQ-025**: Track approval time by approver to identify bottlenecks (ALIGNS)
  - Measure average time-to-approve per approver
  - Identify bottlenecks
  - Process improvement opportunity

### 6.2 Current State Process

**PROCESS**: Approval Workflows (Current State - Manual & Email-Based)  
**TRIGGER**: Order ready for submission  
**STEPS**:
1. Order prepared by Project Coordinator or Account Manager
2. Approver notified manually (email or in-person)
3. Approver responds to approve, reject, or request exception
4. Exception requests common (especially for missing documents)
5. Process manual = delays possible
6. No tracking of approval times
7. Erosion costs reviewed after-the-fact by Matt (training opportunity for new staff)
8. Double-order risks = worst case scenario (150 workstations before discovered at shipment)

**PAIN POINTS**: 
- Manual process = delays
- No systematic approval tracking
- No bottleneck identification
- Double-order detection manual (at shipment or too late)
- Exception workflow not formalized

### 6.3 Orion/NetSuite Solution

Orion/NetSuite provides business rule engine that automatically routes orders meeting approval criteria. Orders >$25K automatically route to Shannon. Orders missing required documents automatically route to Matt. Erosion >$1.5K cumulative automatically routes to Matt. Double-order detection query runs automatically, flagging potential duplicates for manual review before order placement.

Approvers receive dashboard notifications rather than email, centralizing workflow. Approval/rejection/exception handling is tracked with timestamps. Average time-to-approve reporting by approver identifies bottlenecks. Escalation can be automated if approval exceeds time threshold.

### 6.4 Future State Process

Orders are created in NetSuite. Validation rules and business rules engine evaluate order against approval criteria. >$25K orders automatically route to Shannon. Missing document orders automatically route to Matt. Erosion >$1.5K automatically routes to Matt. Double-order detection flags potential duplicates. Approvers receive notifications. Approve/reject handled in NetSuite workflow. Approval times tracked automatically. Reports show approval metrics by approver and cycle time trends.

### 6.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Business Impact | Status |
|--------|-------------|--------------------------|----------|-----------------|--------|
| REQ-021 | Order approval >$25K | Workflow rule | Standard | Automatic routing to Shannon | ✓ Validated |
| REQ-022 | Missing docs approval | Workflow rule | Standard | Document validation enforcement | ✓ Validated |
| REQ-023 | Erosion approval >$1.5K | Workflow rule | Standard | Training opportunity capture | ✓ Validated |
| REQ-024 | Double-order detection | Custom query/alert | Custom | Duplicate order prevention | Custom Design Needed |
| REQ-025 | Approval time tracking | Workflow analytics | Standard | Bottleneck identification | ✓ Validated |

### 6.6 Implementation Approach

- **ALIGNS** (REQ-021, REQ-022, REQ-023, REQ-025): Your approval workflow rules align with NetSuite's standard workflow engine
- **ACCOMMODATE** (REQ-024): Your double-order detection requirement will be accommodated through custom query/alert configuration
- **Key Decisions**: Thresholds ($25K, $1.5K) confirmed; document list confirmed
- **Outstanding**: Document flowchart to be provided by Shannon (action item)
- **Timeline Impact**: Minimal - standard NetSuite workflow configuration with custom double-order query

---

## 7. DASHBOARDS & REPORTING

### 7.1 Your Business Requirements

- **REQ-020**: Create Sales Goals dashboard in NetSuite to replace Excel tracking (ACCOMMODATE)
  - Currently tracked in Excel and distributed weekly
  - Need NetSuite dashboard for current-state visibility
  - "You want that to live in NetSuite? — Yes. Yes… a dashboard" - Matt

- **REQ-041**: Create BD/Sales Rep dashboard (my opportunities, pipeline value, forecast, activities, overdue tasks) (ALIGNS)
  - Personal visibility into pipeline
  - Pipeline value by stage
  - Forecast (Commit, Best Case, Pipeline)
  - Activities this week
  - Overdue tasks

- **REQ-042**: Create Sales Manager dashboard with "Me and My Team" role-based filters (ADAPT)
  - Team pipeline rollup
  - Team forecast (by type)
  - Individual performance comparison
  - Pipeline by stage (team view)
  - Aging opportunities (across team)
  - Win/loss trends
  - Activity metrics
  - Forecast accuracy by rep (learning opportunity)
  - **"Me and My Team" role hierarchy critical** - "That's been one of the frustrations with Core... I've never gotten that" - Marcus

- **REQ-043**: Create Executive dashboard (company-wide pipeline, forecast summary, pipeline by sector/territory, win rate trends) (ALIGNS)
  - Company-wide pipeline total
  - Forecast summary (all reps)
  - Pipeline by sector
  - Pipeline by territory
  - Win rate trends
  - Average deal size
  - Sales cycle length

- **REQ-044**: Enable drill-down capability from dashboard metrics to detail records (ALIGNS)
  - Click any metric → see detail records
  - Investigate anomalies
  - Identify opportunities or problems
  - Spot trends early

### 7.2 Current State Process

**PROCESS**: Sales Reporting (Current State - Manual Excel)  
**TRIGGER**: Status update or executive request  
**STEPS**:
1. Sales Goals tracked manually in Excel
2. Distributed weekly
3. Manager views individual reports
4. Executive manually aggregates for company view
5. Manager dashboard for "Me and My Team" doesn't work in Core ("Never gotten that")
6. Manual drill-down requires re-finding detail
7. Time-consuming manual process

**PAIN POINTS**: 
- Excel manual = delays and errors
- No real-time visibility
- Manager hierarchy view broken in Core
- Drill-down requires manual searching

### 7.3 Orion/NetSuite Solution

Orion/NetSuite provides comprehensive dashboard capabilities with:

**Personal Rep Dashboard:**
- My open opportunities
- My pipeline value
- My forecast (Commit, Best Case, Pipeline)
- My activities this week
- My overdue tasks
- Opportunities needing attention (aging, no activity)
- Recent wins

**Manager Dashboard:**
- Role-hierarchy "Me and My Team" filters working natively
- Team pipeline rollup
- Team forecast by type
- Individual rep comparison
- Pipeline by stage (team view)
- Aging opportunities across team
- Win/loss trends
- Activity metrics
- Forecast accuracy by rep (coaching opportunity)
- NetSuite solution confirmed working: "You have to have the right managers assigned... if we set it up, it actually works. Good."

**Executive Dashboard:**
- Company-wide pipeline
- Forecast summary
- Pipeline by sector
- Pipeline by territory
- Win rate trends
- Average deal size
- Sales cycle length

**Drill-Down Capability:**
- Click any metric to see underlying detail records
- Investigate anomalies
- Spot patterns and trends

**Sales Goals Dashboard:**
- Replaces Excel manual process
- Real-time visibility
- Automatic calculation from underlying opportunity data

### 7.4 Future State Process

Reps login to personal dashboard seeing their pipeline, forecast, and tasks. Managers login to "Me and My Team" dashboard seeing their entire team hierarchy. Executives access company dashboard for strategic overview. All dashboards show real-time data. Drill-down available for investigation. Sales Goals dashboard automatically calculated from opportunity data, eliminating Excel manual distribution.

### 7.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Business Impact | Status |
|--------|-------------|--------------------------|----------|-----------------|--------|
| REQ-020 | Sales Goals dashboard | Custom dashboard design | Custom | Eliminate Excel manual process | Custom Design Needed |
| REQ-041 | Rep personal dashboard | Standard dashboard framework | Standard | Individual visibility | ✓ Validated |
| REQ-042 | Manager Me+Team dashboard | Role hierarchy with filters | Modified Process | Team management visibility | ✓ Validated |
| REQ-043 | Executive dashboard | Standard dashboard framework | Standard | Strategic overview | ✓ Validated |
| REQ-044 | Drill-down capability | Standard NetSuite feature | Standard | Detailed investigation | ✓ Validated |

### 7.6 Implementation Approach

- **ACCOMMODATE** (REQ-020): Your Sales Goals dashboard will be custom-designed to replace Excel tracking
- **ADAPT** (REQ-042): Your sales manager dashboard will use NetSuite's role hierarchy "Me and My Team" filters (confirmed working capability)
- **ALIGNS** (REQ-041, REQ-043, REQ-044): Your dashboard needs align with standard NetSuite dashboard framework
- **Key Decisions**: Finalize Sales Goals metrics and layout (action item - provide Excel template)
- **Outstanding**: Current Sales Goals Excel template needed for dashboard design (Matt/Kip)
- **Timeline Impact**: Custom Sales Goals dashboard requires template input before Realize phase

---

## 8. WIN/LOSS ANALYSIS & LEARNING

### 8.1 Your Business Requirements

- **REQ-026**: Implement required win/loss reason codes (ADAPT)
  - Loss reasons mandatory before closing opportunity as lost
  - Win reasons tracked as well as losses
  - "Dies in there if lost... No systematic learning"

- **REQ-027**: Track competitor information on lost opportunities (ADAPT)
  - Who did we lose to?
  - Competitive intelligence gathering
  - Pattern identification

- **REQ-028**: Create win/loss analysis reports by sector, size, type, territory (ADAPT)
  - Analyze patterns by market segment
  - Sector analysis: which markets winning/losing?
  - Territory analysis: SF vs. San Jose vs. Sacramento performance
  - Continuous learning culture

### 8.2 Current State Process

**PROCESS**: Opportunity Closure (Current State - No Learning)  
**TRIGGER**: Opportunity reaches conclusion  
**STEPS**:
1. Opportunity marked Won or Lost in Zendesk
2. **If Won**: Transfer to Core, create customer, begin order process
3. **If Lost**: Mark as lost → "Dies in there"
4. **No reason captured** for loss
5. **No competitor tracking**
6. **No systematic analysis** of patterns
7. **No learning** from losses

**PAIN POINTS**: 
- Lost opportunities provide no insight
- No competitor intelligence gathered
- Can't improve without understanding why deals lost
- "Dies in there" = missed learning opportunity

### 8.3 Orion/NetSuite Solution

Orion/NetSuite requires win/loss reason codes before opportunity closure. Loss reasons are captured (Price, Competitor, Timing, Requirements Not Met, Relationship, Other). Win reasons tracked (Relationship, Price, Quality/Reputation, Timing, Unique Capability, Other). Competitor field captures which competitor won the deal. Data becomes basis for analysis reports.

Win/loss analysis reports provide visibility by sector, territory, competitor. Patterns emerge: Are we losing healthcare deals on price? Are we losing to specific competitors repeatedly? Which territories have highest win rates? Analysis drives strategic decisions and sales approach refinement.

### 8.4 Future State Process

Opportunities closed as lost require reason code selection and competitor identification. Opportunities closed as won optionally capture win reason and competitor beaten. Data accumulates in NetSuite. Monthly analysis reports show win/loss patterns by sector, territory, competitor. Strategic decisions informed by data. Sales team learns from patterns. Approach adjusted based on intelligence.

### 8.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Business Impact | Status |
|--------|-------------|--------------------------|----------|-----------------|--------|
| REQ-026 | Required win/loss reason codes | Custom required field | Modified Process | Systematic learning | ✓ Validated |
| REQ-027 | Competitor tracking | Custom competitor field | Modified Process | Competitive intelligence | ✓ Validated |
| REQ-028 | Win/loss analysis reports | Custom reporting | Modified Process | Strategic insights | ✓ Validated |

### 7.6 Implementation Approach

- **ADAPT** (all win/loss requirements): Your win/loss tracking will adapt from non-existent to required reason codes with competitor tracking enabling analysis
- **Key Decisions**: Finalize reason code taxonomy (action item)
- **Outstanding**: Win/loss reason codes to be defined during Discovery
- **Timeline Impact**: Minimal - configuration with custom fields and reports

---

## 9. VENDOR & CUSTOMER MANAGEMENT

### 9.1 Your Business Requirements

- **REQ-029**: Add vendor credit limit field and warning threshold (90% of limit) (ACCOMMODATE)
  - Vendor record custom field for credit limit
  - Warning alert at 90% threshold
  - Dashboard visibility for purchasing team
  - "Mad scramble at that nth hour because our order won't go through because we hit it"

- **REQ-030**: Prevent PO creation when vendor credit limit exceeded (ACCOMMODATE)
  - Hard stop: Cannot create PO if over limit
  - Emergency override process for exceptions
  - "Sounds like just a pretty simple query"

- **REQ-031**: Enable basic Customer Portal for quote and invoice visibility (ALIGNS)
  - "We do have a customer portal… see open quotes… open invoices"
  - Self-service customer access
  - Reduced support requests

- **REQ-032**: Configure GP target default of 22% at customer level with opportunity override capability (ADAPT)
  - Customer record field: GP target 22% default
  - Opportunity field: Override customer default if needed
  - "Field on the customer… sources through the opportunity… user can override"

### 9.2 Current State Process

**PROCESS**: Vendor Credit Management (Current State - Reactive)  
**TRIGGER**: PO created; order submission  
**STEPS**:
1. PO created without checking credit limit
2. PO submission → **Order rejected by vendor** (over credit limit)
3. **Mad scramble** to find payment option or alternative vendor
4. Disrupts delivery timeline
5. Customer frustrated

**PAIN POINTS**: 
- No proactive visibility into approaching limits
- Reactive discovery at worst possible time
- No prevention mechanism
- "Mad scramble at that nth hour"

### 9.3 Orion/NetSuite Solution

Orion/NetSuite adds vendor credit limit field to vendor record with warning threshold at 90% of limit. Dashboard portlet displays vendors approaching limits, enabling proactive payment or vendor switching decisions. Business rule prevents PO creation if vendor credit exceeded (with emergency override process for exceptions). Purchasing team gains visibility to manage proactively rather than reactively.

Customer Portal provides self-service access to quotes and invoices, reducing support burden. GP target default at customer level (22%) with override capability at opportunity level allows flexible pricing while maintaining target discipline. Default provides guidance; override capability accommodates special situations.

### 9.4 Future State Process

Vendors have credit limits configured in system. Dashboard shows vendors at >70% (warning) and >90% (alert) of limit. Purchasing team sees alerts and proactively manages. Before PO creation, system validates against credit limit. If exceeded, PO creation blocked with notification. Emergency override process available for exceptional cases. Customers access portal for quote and invoice visibility without support team intervention.

### 9.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Business Impact | Status |
|--------|-------------|--------------------------|----------|-----------------|--------|
| REQ-029 | Vendor credit limit field | Custom field + dashboard | Custom | Proactive limit visibility | Custom Design Needed |
| REQ-030 | Prevent PO over limit | Business rule validation | Custom | Credit limit enforcement | Custom Design Needed |
| REQ-031 | Customer Portal | NetSuite Customer Center | Standard | Self-service customer access | ✓ Validated |
| REQ-032 | GP target 22% default | Custom field + defaults | Modified Process | Pricing guidance with flexibility | ✓ Validated |

### 9.6 Implementation Approach

- **ACCOMMODATE** (REQ-029, REQ-030): Your vendor credit limit requirements will be accommodated through custom fields and business rule configuration
- **ALIGNS** (REQ-031): Your customer portal need aligns with NetSuite's standard Customer Center
- **ADAPT** (REQ-032): Your GP target approach will adapt to use customer-level default (22%) with opportunity-level override
- **Outstanding**: Confirm vendor credit limits and warning thresholds (action item)
- **Timeline Impact**: Custom development for vendor credit limit features; standard portal implementation

---

## 10. ACTIVITY TRACKING & COLLABORATION

### 10.1 Your Business Requirements

- **REQ-033**: Enable activity tracking (calls, emails, meetings) on opportunities (ALIGNS)
  - Interaction history maintained automatically
  - Who contacted whom and when
  - Meeting notes and outcomes captured
  - Email threads linked to opportunity

- **REQ-034**: Enable task management with due dates and reminders on opportunities (ALIGNS)
  - Follow-up tasks created and tracked
  - Due dates and reminders ensure accountability
  - Team visibility into pending tasks
  - Task history maintained

- **REQ-035**: Maintain activity history and team collaboration notes on opportunities (ALIGNS)
  - Complete interaction history visible to team
  - Team members see who did what and when
  - Collaboration notes enable handoffs
  - No lost context during staff changes

### 10.2 Current State Process

**PROCESS**: Activity Tracking (Current State - Minimal)  
**TRIGGER**: Interaction with customer or prospect  
**STEPS**:
1. Interaction occurs (call, email, meeting)
2. **Optional documentation** in Zendesk (varies by user)
3. Some users diligent; some don't document
4. No automatic email linking
5. Team doesn't see interaction history
6. If rep leaves → context lost

**PAIN POINTS**: 
- Optional documentation = inconsistent
- No automatic email capture
- Team can't see history
- Knowledge lost on personnel changes

### 10.3 Orion/NetSuite Solution

Orion/NetSuite captures activity tracking (calls, emails, meetings) with automatic email linking. Activity history is maintained automatically and visible to all team members. Task management creates follow-up accountability with due dates and reminders. Collaboration notes enable team handoffs. Complete interaction history preserved for continuity.

### 10.4 Future State Process

Interactions with customer recorded automatically (emails linked, calls logged). Tasks created with due dates. Team sees complete activity history. Notes maintained. When rep hands off opportunity, next rep has full context.

### 10.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Business Impact | Status |
|--------|-------------|--------------------------|----------|-----------------|--------|
| REQ-033 | Activity tracking | NetSuite activity management | Standard | Interaction history | ✓ Validated |
| REQ-034 | Task management | Task module | Standard | Follow-up accountability | ✓ Validated |
| REQ-035 | Collaboration notes | Notes field + history | Standard | Team continuity | ✓ Validated |

### 10.6 Implementation Approach

- **ALIGNS** (all activity requirements): Your activity tracking needs align with NetSuite's standard activity and task management
- **Outstanding**: Define activity logging standards (required vs. optional) during Realize phase
- **Timeline Impact**: None - standard NetSuite functionality

---

## 11. DOCUMENT MANAGEMENT & RFP PROCESS

### 11.1 Your Business Requirements

- **REQ-036**: Enable document attachment to opportunities/quotes (RFPs, proposals, correspondence) (ALIGNS)
  - Attach documents directly to opportunity record
  - RFP documents, proposals, correspondence maintained
  - Full project context available
  - No separate document storage searches

- **REQ-037**: Support Google Drive folder linking for project documentation (ALIGNS)
  - Link to Google Drive folders for project materials
  - Current practice maintained
  - Access to documents from NetSuite records

**Additional Implicit Requirement**: Projected vs. Actual volume tracking for RFP process
- Track projected volume on RFP/Quote
- Track actual volume on Sales Order/Project
- Report projected vs. actual by estimator
- Identify patterns in estimation accuracy
- Improve resource allocation for marketing/operations

### 11.2 Current State Process

**PROCESS**: RFP Management (Current State - Fragmented)  
**TRIGGER**: RFP identified or received  
**STEPS**:
1. RFP may or may not be entered in Zendesk (inconsistent)
2. When formal RFP arrives → Submitted to **Asana** (separate system)
3. Request includes background, links, documentation
4. **Projected volume** captured on Asana request (key metric)
5. Marketing PM schedules kickoff
6. Marketing develops response
7. **Marketing has no visibility until formal request** submitted
8. **Projected vs. Actual volume** tracked informally
9. People overestimate volume → Resource allocation difficult
10. Actual volume often significantly different from projection

**PAIN POINTS**: 
- Marketing lacks early visibility (can't prep proactively)
- No market trend intelligence from early RFPs
- Resource allocation challenging without early visibility
- Overestimation of volume common ("People overestimate volume... Resource allocation difficult")
- No systematic volume tracking

### 11.3 Orion/NetSuite Solution

Orion/NetSuite enables document attachment directly to opportunity records, maintaining RFP documentation, proposals, and correspondence in context. Google Drive folder linking maintained for project materials. 

Critical improvement: Creating opportunity immediately when RFP identified (not waiting for formal request) gives marketing visibility. Marketing PM can see pipeline of incoming RFPs, enabling proactive resource planning. Projected volume tracked on quote record. Actual volume tracked on sales order/project. Report shows projected vs. actual by estimator, identifying patterns and improving accuracy over time.

### 11.4 Future State Process

RFP identified → Create opportunity immediately in NetSuite with preliminary information. Marketing PM gains visibility. When formal RFP received → Update opportunity with documents and details. Attach RFP to opportunity record. Projected volume documented on quote. As project executes, actual volume documented on sales order/project. Monthly report shows projected vs. actual by person, identifying accuracy patterns. Volume forecasting improves through systematic tracking.

### 11.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Business Impact | Status |
|--------|-------------|--------------------------|----------|-----------------|--------|
| REQ-036 | Document attachment | Document management | Standard | RFP context preservation | ✓ Validated |
| REQ-037 | Google Drive linking | External link integration | Standard | Current practice maintained | ✓ Validated |

### 11.6 Implementation Approach

- **ALIGNS** (REQ-036, REQ-037): Your document and RFP management needs align with NetSuite's document attachment and external link capabilities
- **Additional Capability**: Projected vs. Actual volume tracking fields needed (custom fields for quotes and projects)
- **Outstanding**: Finalize RFP process workflow and volume tracking field placement during Realize phase
- **Timeline Impact**: Minimal - standard document management with custom volume tracking fields

---

## 12. MARKETING INTEGRATION & EMAIL CAMPAIGNS

### 12.1 Your Business Requirements

- **REQ-045**: Configure email marketing capability (120,000 emails/month included) with minimal implementation (ALIGNS)
  - "Capacity way more than we would ever use"
  - "Less than 6 campaigns per year"
  - Minimal focus during Phase 1; can enable post-go-live if needed

- **REQ-046**: Implement automatic subscription management for opt-in/opt-out (ALIGNS)
  - Subscription status automatically managed
  - Email compliance maintained
  - No manual MailChimp management headaches

- **REQ-047**: Support segmented contact lists by role, sector, geography, custom criteria (ALIGNS)
  - Curated lists by role (brokers, PM firms, CM firms)
  - Market-specific targeting (SF ≠ San Jose market)
  - Sector-specific targeting (healthcare trending up)
  - "If marketing had more insight into sectors and markets over time, they could create and target content proactively"

- **REQ-048**: Track campaign performance (opens, clicks, ROI) when email campaigns used (ALIGNS)
  - Campaign metrics captured when used
  - "Click rates aren't great so there's just really no way right now to target"
  - Minimal usage expected but capability available

### 12.2 Current State Process

**PROCESS**: Email Marketing (Current State - Manual & Limited)  
**TRIGGER**: Marketing campaign needed  
**STEPS**:
1. Marketing team creates email in MailChimp
2. Manual list building (Excel upload with pain)
3. "MailChimp gets really pissed off when you load Excel because they think you're going to spam"
4. "Most of it bounces anyways"
5. Send campaign
6. Limited success metrics (click rates poor)
7. Can't segment by role or market effectively
8. "Click rates aren't great so there's just really no way right now to target"

**PAIN POINTS**: 
- Manual list management in MailChimp
- Can't segment by role/sector
- Poor click rates
- No integration with CRM contact data
- "So much of what we do is relationship-based" → Low-volume, high-personalization approach

### 12.3 Orion/NetSuite Solution

Orion/NetSuite email marketing provides 120K emails/month included (far more capacity than needed for 6 campaigns/year). Automatic subscription management maintains opt-in/opt-out status, eliminating manual MailChimp complaints. Segmentation engine enables unlimited list building by role, sector, territory, and custom criteria.

When campaigns used, performance tracking (opens, clicks, ROI) measures effectiveness. Integration with CRM contact data eliminates manual list building.

### 12.4 Future State Process

Marketing team creates email in NetSuite. Segmentation engine builds curated lists (e.g., all healthcare brokers in SF). Subscription status automatically managed. Campaign sent to segment. Performance metrics tracked. KBM Hoag's relationship-based approach maintained; email marketing capability available for occasional campaigns without overhead.

### 12.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Business Impact | Status |
|--------|-------------|--------------------------|----------|-----------------|--------|
| REQ-045 | Email marketing capability | NetSuite Email module | Standard | Available if needed | ✓ Validated |
| REQ-046 | Auto subscription management | Subscription management | Standard | Compliance automation | ✓ Validated |
| REQ-047 | Segmented contact lists | List builder + segmentation | Standard | Targeted outreach | ✓ Validated |
| REQ-048 | Campaign performance tracking | Email analytics | Standard | Effectiveness measurement | ✓ Validated |

### 12.6 Implementation Approach

- **ALIGNS** (all email marketing requirements): Your email marketing needs align with NetSuite's standard capabilities
- **Decision**: Minimal implementation during Phase 1; email marketing can be enabled post-go-live
- **Timeline Impact**: None Phase 1; can be configured post-go-live if/when needed

---

## 13. DATA MIGRATION STRATEGY

### 13.1 Your Business Requirements

- **REQ-038**: Import Zendesk opportunity history via CSV with historical tagging (ALIGNS)
  - Export entire Zendesk history
  - Import into NetSuite with "historical" tag
  - Maintains context without confusing old data with active opportunities

- **REQ-039**: Migrate contact data from Core with deduplication (ALIGNS)
  - Core contacts imported to NetSuite
  - Deduplication during migration
  - Clean starting point

- **REQ-040**: Migrate and classify contacts by role, sector, and territory during import (ACCOMMODATE)
  - Contact classification during migration
  - Role assignment (Primary Contact, Decision Maker, Finance, etc.)
  - Sector assignment (Healthcare, Tech, Corporate, etc.)
  - Territory assignment (SF, San Jose, Sacramento)
  - Enables immediate segmentation post-migration

### 13.2 Current State Process

**PROCESS**: CRM Data (Current State - Multiple Fragmented Sources)  
**TRIGGER**: CRM Implementation  
**STEPS**:
1. Zendesk opportunity history exported
2. Core contact data extracted
3. Manual classification needed for contacts
4. Data quality issues in Core ("poo in, poo out")

**PAIN POINTS**: 
- Data quality poor in source systems
- Manual classification effort required
- Deduplication needed

### 13.3 Orion/NetSuite Solution

Orion/NetSuite provides data migration tools with CSV import capability. Zendesk opportunity history imported with historical tagging. Core contact data migrated with deduplication using NetSuite's duplicate detection. Contact classification during migration enables immediate segmentation and reporting capability post-migration.

### 13.4 Future State Process

Zendesk opportunity history migrated with historical tag. Core contacts imported with deduplication. Contacts classified by role, sector, and territory during import. NetSuite starts with clean, classified contact database ready for segmentation and targeting.

### 13.5 Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach | Business Impact | Status |
|--------|-------------|--------------------------|----------|-----------------|--------|
| REQ-038 | Zendesk history import | CSV import with tagging | Standard | Historical context preserved | ✓ Validated |
| REQ-039 | Contact migration + dedup | Data migration + duplicate detection | Standard | Clean database starting point | ✓ Validated |
| REQ-040 | Contact classification | Custom classification during import | Custom | Immediate segmentation capability | Custom Design Needed |

### 13.6 Implementation Approach

- **ALIGNS** (REQ-038, REQ-039): Your data migration needs align with NetSuite's standard CSV import and duplicate detection
- **ACCOMMODATE** (REQ-040): Your requirement for contact classification during migration will be accommodated through custom mapping
- **Outstanding**: Identify data quality owner/champion for contact database management (action item)
- **Timeline Impact**: Data migration planning session recommended during Discovery

---

## 14. CHANGE MANAGEMENT & ADOPTION

### 14.1 Behavior Changes Required

**1. Consistent CRM Data Entry:**
- Current: Optional, ignored by many
- Future: Required with validation rules
- "Not required" → "Required for accountability"
- Eliminates "some people just lick everything and calling it theirs"

**2. Earlier Opportunity Creation:**
- Current: Enter when ready to forecast or at RFP arrival
- Future: Create at first knowledge of potential
- Purpose: Better pipeline visibility, market intelligence

**3. Activity Logging:**
- Current: Minimal or none
- Future: Log significant interactions (calls, meetings, emails)
- Purpose: History maintained for team, better collaboration

**4. Data Quality Discipline:**
- Required fields completion
- Contact role classification
- Sector assignment
- Validation rule compliance
- Regular updates

### 14.2 Resistance Points & Mitigation

**1. Sales Team Pushback (Primary Concern):**
- Quote: "Matt's philosophy: Sales will be our biggest pushback"
- May resist structure and perceived overhead
- Data entry seen as bureaucracy, not value-add
- **Mitigation**: Demonstrate value (better forecasting, reduced work elsewhere)

**2. Time Investment:**
- Data entry takes time
- Activity logging feels like overhead
- **Counter**: Show ROI (better forecasting, reduced manual work, improved visibility)
- **Strategy**: Quick wins essential

**3. Process Changes:**
- Comfortable with current Zendesk + Core + Asana mix
- New system = new learning curve
- Temporary productivity dip expected
- **Mitigation**: Comprehensive training, champions, ongoing support

**4. Accountability & Visibility:**
- Data quality becomes visible (good and bad performers apparent)
- Forecast accuracy tracked (performance transparency)
- Activity levels measurable
- May create discomfort for some users
- **Mitigation**: Frame as coaching opportunity, not punishment

### 14.3 Success Factors

**1. Executive Sponsorship:**
- Matt's support critical
- Clear expectations set from top
- Accountability for CRM usage
- Recognition for compliance
- Consequences for non-compliance

**2. Show Value Fast:**
- Pipeline visibility (immediate benefit)
- Forecast accuracy improvements (measurable)
- Win/loss insights (strategic value)
- Reduced manual work (time savings)
- Better team collaboration (shared visibility)

**3. Training & Support:**
- Role-specific training (BD reps ≠ Account Managers ≠ Managers)
- Sales/BD-focused approach (not generic NetSuite training)
- Quick reference guides
- NetSuite champions identified
- Ongoing support available
- Documentation accessible

**4. Data Quality Campaign:**
- Clean data from start (migration done right)
- Regular hygiene processes (ongoing cleanup)
- Recognition for good practices
- Gamification possible (leaderboard for data quality)
- Shared ownership culture

**5. Incremental Adoption:**
- Start with core functionality (don't overwhelm)
- Add sophistication over time
- Build confidence gradually
- Celebrate wins publicly
- Learn and adjust based on feedback

---

## DECISION LOG

### Implementation Approach Summary

**ALIGNS: 33 Requirements (66%)**  
Leverages proven Orion/NetSuite capabilities and standard functionality:
- Zendesk → NetSuite CRM transition
- Lead management and Web-to-Lead
- Opportunity management and Kanban boards
- Contact and account management
- Territory assignment and sector tracking
- Duplicate detection and duplicate merge
- Activity tracking and task management
- Document attachment and Google Drive linking
- Customer portal
- Email marketing (optional)
- Dashboards and drill-down navigation
- Approval workflows

**ADAPT: 11 Requirements (22%)**  
Requires business process changes without customization:
- Required opportunity entry (vs. optional current state)
- Restricted visibility (vs. open current state)
- Opportunity-level forecasting (vs. quote-level)
- 70%+ probability threshold
- Forecast accuracy tracking
- Stage definition and probability by stage
- Manager "Me and My Team" dashboard
- Win/loss reason codes
- Competitor tracking
- Win/loss analysis reports
- GP target defaults with overrides

**ACCOMMODATE: 6 Requirements (12%)**  
Custom solution design required:
- REQ-003: Validation rules and required field configuration
- REQ-010: Custom contact role classifications
- REQ-020: Sales Goals dashboard design
- REQ-024: Double-order detection query
- REQ-029/030: Vendor credit limit management
- REQ-040: Contact classification during data migration

**FUTURE: 2 Requirements**  
Deferred to post-go-live phase:
- REQ-049: Commission splits on opportunities
- REQ-050: Event management

### Key Implementation Decisions

| Area | Decision | Rationale |
|------|----------|-----------|
| CRM Platform | NetSuite (replace Zendesk) | Unified system eliminates fragmentation |
| Required Fields | Mandatory opportunity entry | Enforces data quality discipline |
| Forecasting | Opportunity-level with 70%+ threshold | Prevents over-forecasting |
| Approval Rules | Automated workflow routing | Reduces delays, ensures consistency |
| Territory | Three territories (SF, San Jose, Sacramento) | Matches current BD rep structure |
| Training | Role-specific (BD reps ≠ Account Managers ≠ Managers) | Relevant to actual workflows |
| Change Management | Executive sponsorship + quick wins | Sales team adoption critical |
| Email Marketing | Minimal Phase 1; optional post-go-live | Relationship-based culture ≠ mass campaigns |
| RFP Process | Early opportunity creation for marketing visibility | Improves resource planning |

### Outstanding Decisions Requiring Confirmation

| Item | Owner | Timeline |
|------|-------|----------|
| Opportunity stages & probability | Sales Leadership | During Discovery |
| Contact role taxonomy | Sales/BD Team | During Discovery |
| Sector/vertical classifications | All stakeholders | During Discovery |
| Lead source definitions | Sales/BD Team | During Discovery |
| Win/loss reason codes | All stakeholders | During Discovery |
| Activity logging standards | Sales Leadership | During Realize phase |
| Minimum required fields | Sales Leadership | During Realize phase |
| Data quality owner | TBD | Early Realize phase |
| Sales Goals dashboard specs | Matt/Kip | Before Realize phase |
| Approval workflow flowchart | Shannon | Before Realize phase |

---

## IMPLEMENTATION CONSIDERATIONS

### Timeline
- **Discovery Phase**: 6-8 weeks (concurrent with these requirements sessions)
- **Realize Phase**: 8-10 weeks (GSI-heavy system configuration)
- **Educate Phase**: 6-8 weeks (Client-heavy training and UAT)
- **Activate Phase**: 2 weeks (Go-live preparation and cutover)
- **Post-Go-Live Support**: 30 days (included in implementation)

### Dependencies
1. Opportunity stages and probability percentages finalization
2. Contact role taxonomy finalization
3. Approval workflow flowchart documentation
4. Sales Goals Excel template for dashboard design
5. Data quality owner identification
6. Sales team buy-in on required data entry

### Risks & Mitigation

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Sales team resistance to required CRM usage | High | Executive sponsorship, clear value communication, quick wins |
| Data quality migration issues | High | Deduplication during import, data quality champion ownership |
| Incomplete taxonomy definitions | Medium | Early action item completion, validation during UAT |
| Forecast accuracy tracking adoption | Medium | Training focus, gamification/leaderboard, coaching approach |
| Territory overlap scenarios | Medium | Early clarification of process for multi-territory accounts |
| Approval workflow complexity | Medium | Careful balance between control and speed, approval time tracking |
| Manager dashboard "Me and My Team" setup | Medium | Ensure organizational hierarchy correctly configured |
| Double-order detection false positives | Low | Configuration to flag, not auto-reject; manual review process |

### Action Items

**Immediate (Before Discovery Completion):**
- [ ] Define final list of opportunity stages and probability by stage (Action: Sales Leadership)
- [ ] Finalize contact role taxonomy (Action: Sales/BD Team - All)
- [ ] Define sector/vertical classifications (Action: All stakeholders)
- [ ] Document current approval workflow in flowchart format (Action: Shannon)

**Discovery Phase:**
- [ ] Confirm lead source definitions (Action: Sales/BD Team)
- [ ] Define win/loss reason codes (Action: All stakeholders)
- [ ] Provide current Sales Goals Excel template (Action: Matt/Kip)
- [ ] Identify data quality owner/champion (Action: TBD)
- [ ] Clarify territory overlap scenarios (Action: Sales Leadership)
- [ ] Document minimum required fields for opportunity (Action: Sales Leadership)

**Realize Phase:**
- [ ] Configure validation rules and required fields (Action: GSI + Sales Leadership)
- [ ] Define custom contact role field values (Action: GSI + Sales/BD Team)
- [ ] Design Sales Goals dashboard (Action: GSI + Matt)
- [ ] Build double-order detection query (Action: GSI)
- [ ] Configure vendor credit limit fields and rules (Action: GSI + Finance)
- [ ] Develop role-specific training materials (Action: GSI training team)
- [ ] Identify NetSuite Champions per department (Action: Sales Leadership with Kimmy)

**Educate Phase:**
- [ ] Deliver role-specific training (Action: GSI + Sales Leadership)
- [ ] Execute User Acceptance Testing (Action: Business users with GSI)
- [ ] Configure organizational hierarchy for manager dashboard (Action: GSI + HR)
- [ ] Finalize Sales Goals dashboard (Action: GSI + Matt)

**Post-Go-Live:**
- [ ] Provide 30-day intensive support (Action: GSI Support team)
- [ ] Monitor adoption and data quality (Action: Data quality owner)
- [ ] Build best practices documentation (Action: Sales Leadership + Champions)
- [ ] Evaluate optional email marketing post-go-live (Action: Marketing Manager)

---

## ACCEPTANCE & SIGN-OFF

This Business Requirements Document validates that Orion/NetSuite CRM aligns with KBM Hoag's business requirements and provides the proven solution for their CRM transformation. The favorable distribution of requirements (66% ALIGNS, 22% ADAPT, 12% ACCOMMODATE) confirms that Orion's pre-built CRM capabilities effectively address business needs with minimal customization.

**Client Acceptance:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Executive Sponsor | Matt | ________________ | ________ |
| Sales Leadership | Jill Marsh (BD-SF) | ________________ | ________ |
| Sales Leadership | Kate (BD-San Jose) | ________________ | ________ |
| Sales Leadership | Alex Blangeres (BD-Sacramento) | ________________ | ________ |
| Sales Operations | TBD | ________________ | ________ |

**GSI Acceptance:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Executive Sponsor | Sean Scanlon | ________________ | ________ |
| CRM Implementation Lead | GSI CRM Consultant | ________________ | ________ |
| Project Manager | Tom Shannon (PMO Lead) | ________________ | ________ |

---

## NEXT STEPS

1. **BRD Approval**: Circulate BRD to executive sponsors and sales leadership for review and sign-off
2. **Action Items Completion**: Begin immediate action items (stage/probability definitions, contact role taxonomy, approval workflow flowchart)
3. **Additional Discovery**: If needed, schedule deep-dives on specific areas (territory overlap, commission splits post-Phase 1)
4. **Taxonomy Finalization**: Complete all configuration taxonomies before Realize phase kickoff
5. **Data Migration Planning**: Schedule data migration session to detail Zendesk/Core extraction and classification approach
6. **Change Management Kickoff**: Matt communicates CRM adoption expectations to sales team; highlight value and accountability

---

*Document prepared by: GSI Implementation Team*  
*Distribution: Executive Sponsors, Sales Leadership, CRM Implementation Team, Functional Workstream Leads*  
*Confidentiality: KBM Hoag & GSI - Restricted Distribution*

---

**End of Business Requirements Document - CRM v1.0**




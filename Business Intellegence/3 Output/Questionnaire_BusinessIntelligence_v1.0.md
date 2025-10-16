# Questionnaire - Business Intelligence & Reporting
**Version**: 1.0  
**Date**: 2025-10-15  
**Process Area**: Business Intelligence & Reporting

## Change Log
- **Date**: 2025-10-15
- **Version**: 1.0
- **Sources**: Master_Transcript_Business_Intelligence.md (July 2025)
- **Summary**: Initial discovery questionnaire created from Business Intelligence workshop transcripts covering dashboards, reporting, saved searches, data governance, and change management requirements.

## PROCESSED FILES
- Business Intellegence/2 Input/Master_Transcript_Business_Intelligence.md
  - Business Intelligence.txt (July 31, 2025)
  - 07-31 Workshop Operations transcript (Business Intelligence session portion)

## Decision Log

### Core Platform Decisions
- **REQ-001**: Use NetSuite native BI tools as primary platform (ALIGNS) - "Just to kind of give you the highlights of what's available to you inside NetSuite. So you have these core NetSuite BI tools. They are very powerful."
- **REQ-002**: Power BI remains optional for aged data analysis with live connection (ADAPT) - "I don't want to discourage you from using Power BI. If you love Power BI, use it, just keep in mind that the data is aged once it's out. But if you have a live connection, you've kind of mitigated that."

### Dashboard & Publishing Decisions
- **REQ-003**: Implement role-based dashboard publishing with lock-down capability (ACCOMMODATE) - "'I changed my dashboard.' I'm like, 'No, you're not doing that.' So then what I would do is I create a dashboard for them, publish it, and they can't change it."
- **REQ-004**: Build Orion-enhanced dashboard components for improved aesthetics (ALIGNS) - "We kind of think of NetSuite as kind of the home that you're living in all day. So it should look good. So you feel good about where you're living."
- **REQ-005**: Create department-specific dashboards on role centers (ALIGNS) - "You can have a dashboard on each one of these tabs. And the home is kind of like your default dashboard. And then the other ones are like process specific."
- **REQ-006**: Implement Reminders Portlet as daily work driver (ALIGNS) - "This reminders portlet is key. So you can write a safe search. You can put it in this reminders portlet. And this is really what everybody's work is on a daily basis."
- **REQ-007**: Enable both departmental and individual reminders portlets (ALIGNS) - "Was that by individual or could it be departmental?" - Lorraine; "Either one. Yep." - Marcus

### Report Standardization & Governance
- **REQ-008**: Establish "official" report designation with GSI/Orion prefix (ADAPT) - "The one thing I'll encourage you to do as we get into implementation is we prefix our saved search, the ones that we create, and then we also sometimes will nominate something as being like an official saved search."
- **REQ-009**: Implement public/private saved search controls (ALIGNS) - "If you're going to make your own search, make it public [or] no one else needs to see that."
- **REQ-010**: Create standardized report criteria and interpretation documentation (ADAPT) - "I want a revenue report for this time frame, and that revenue report can be written four or five different ways. Are you including taxes? Are you not including taxes?"

### Data Export & Security
- **REQ-011**: Implement role-based export permissions (all-or-nothing) (ALIGNS) - "For a given role there is a report export [permission] and that's what actually shows the button for like PDF and Excel and everything. You can turn that off on a role basis."
- **REQ-012**: Configure notification system for large data exports (>50MB) (ACCOMMODATE) - "Trigger system to alert if more than 50 megabytes of data are being downloaded."

### Reporting Functionality
- **REQ-013**: Utilize 400+ standard NetSuite reports with customization (ALIGNS) - "Standard reporting, NetSuite ships with over 400 standard reports. And that's everything from income statement, trial balance, balance sheet. And every single one of those reports can be customized."
- **REQ-014**: Implement as-of-date reporting capability for historical snapshots (ALIGNS) - "Reporting in NetSuite is unique because you can get the as of dates for those reports. So like what was my balance sheet as of September 1st. You can get that."
- **REQ-015**: Enable workbook analytics for pivot tables and charts (ALIGNS) - "We also have workbooks, which is like think of like Excel. It's called workbook analytics. So pivot table charts, you can build those out inside NetSuite."
- **REQ-016**: Configure SuiteQL access for technical users (ALIGNS) - "We have SuiteQL, which is NetSuite's kind of own version of SQL. You can, so that means you can write queries."

### Saved Search Features
- **REQ-017**: Enable inline editing from saved searches (ALIGNS) - "Whenever you see a pencil here, that means you can edit right here without having to go in and edit the whole record."
- **REQ-018**: Implement highlighting rules for visual indicators (ALIGNS) - "I'm going to say if the expected close date is before today that's a problem so I'm... somebody can easily come in here and say all right well I already know the status of this one."
- **REQ-019**: Enable mass update functionality (ALIGNS) - "There's also a mass update function that's a little more involved, but you can, in a safe search, do a mass update."

### KPIs & Scorecards
- **REQ-020**: Create sales rep scorecards for individual dashboards (ACCOMMODATE) - "So I would love them to see that on their own dashboard." - Wendy
- **REQ-021**: Build manager view scorecards showing team performance (ACCOMMODATE) - "And then if he was ever managing them on their dashboard, it shows them all of their people."
- **REQ-022**: Implement "me only" and "me and my team" filters (ALIGNS) - Discussion of individual vs. team views with proper org structure configuration

### Organizational Structure
- **REQ-023**: Configure proper manager hierarchy for filter functionality (ALIGNS) - "You have to have the right managers assigned for those filters to work. But if we set that up, if we set it up, it actually works."

### Executive Reporting
- **REQ-024**: Enable scheduled report distribution via email (ALIGNS) - "Can schedule reports and email automatically"
- **REQ-025**: Support executive financial review presentations from system (ALIGNS) - "When we would sit down and we would have our financial reports, I would just pull up the income statement, the balance sheet, trial balance, walk through it."

### Process Area Specific Reporting
- **REQ-026**: Build comprehensive Backlog 360 dashboard (ACCOMMODATE) - "We're building on a backlog 360 dashboard, so it's just one dashboard that has everything you could ever imagine for backlog in one place."
- **REQ-027**: Build comprehensive Bookings 360 dashboard (ACCOMMODATE) - Similar structure to Backlog 360

## Action Items

ACTION: Build department-specific dashboards for each process area (Finance, Sales, Pre-Quote, Order Management, Operations)  
ASSIGNED TO: GSI/Orion Implementation Team  
DUE: During implementation phase  
RELATED TO: REQ-003, REQ-005

ACTION: Create official report suite with standardized criteria documentation  
ASSIGNED TO: GSI/Orion with KBM Hoag input  
DUE: During implementation phase  
RELATED TO: REQ-008, REQ-010

ACTION: Define role-based export permissions by role  
ASSIGNED TO: TBD - Suggest: IT Security with Department Heads  
DUE: Before go-live  
RELATED TO: REQ-011, REQ-012

ACTION: Configure large export notification threshold and recipients  
ASSIGNED TO: TBD - Suggest: IT Security Lead  
DUE: Before go-live  
RELATED TO: REQ-012

ACTION: Properly configure organizational manager hierarchy  
ASSIGNED TO: TBD - Suggest: HR with IT Admin  
DUE: Before go-live  
RELATED TO: REQ-023

ACTION: Gather current report examples (Excel/Google Sheets) from all departments  
ASSIGNED TO: TBD - Suggest: Process Area Leads  
DUE: Early implementation phase  
RELATED TO: REQ-010, REQ-026, REQ-027

ACTION: Design sales rep scorecard layout and metrics  
ASSIGNED TO: Wendy (mentioned) with Sales Leadership  
DUE: TBD  
RELATED TO: REQ-020, REQ-021

ACTION: Define official report naming convention standards  
ASSIGNED TO: GSI/Orion with KBM Hoag  
DUE: Early implementation phase  
RELATED TO: REQ-008

ACTION: Validate SharePoint integration for reporting  
ASSIGNED TO: TBD - Suggest: IT Integration Lead  
DUE: TBD  
RELATED TO: Integration requirements

ACTION: Validate Google Drive integration for reporting  
ASSIGNED TO: TBD - Suggest: IT Integration Lead  
DUE: TBD  
RELATED TO: Integration requirements

ACTION: Identify which roles require SuiteQL access  
ASSIGNED TO: TBD - Suggest: IT with Department Heads (Kipp mentioned as technical user)  
DUE: Before go-live  
RELATED TO: REQ-016

ACTION: Create training materials on official report usage and interpretation  
ASSIGNED TO: GSI/Orion with KBM Hoag SMEs  
DUE: Before go-live  
RELATED TO: REQ-008, REQ-010

## Additional Sessions Needed

### Session: Export Security Policy Definition
- **Participants Needed**: IT Security Lead, Department Heads, Legal/Compliance if applicable
- **Questions to Address**: 
  • Which roles can export data?
  • Which roles cannot export?
  • What is the threshold for large export notifications? (Proposed: 50MB)
  • Who receives export notifications?
  • Are there any report-specific exceptions needed?
- **Priority**: High
- **Suggested Duration**: 90 minutes
- **Dependencies**: REQ-011, REQ-012
- **Evidence**: "Let's list that as a requirement, some permission around exporting and some notifications around if something was exported over a certain amount."

### Session: Official Reports Definition Workshop
- **Participants Needed**: Finance Lead, Sales Lead, Operations Lead, Order Management Lead, GSI/Orion
- **Questions to Address**: 
  • What are the critical reports for each department?
  • What criteria should each official report use?
  • How should report variations be handled?
  • Who authorizes official report changes?
  • What is the version control process?
- **Priority**: High
- **Suggested Duration**: 2-3 hours
- **Dependencies**: REQ-008, REQ-010
- **Evidence**: "We prefix our saved search, the ones that we create, and then we also sometimes will nominate something as being like an official saved search."

### Session: Dashboard Design Sessions by Department
- **Participants Needed**: Department-specific users and managers (separate sessions per department)
- **Questions to Address**: 
  • What KPIs should appear on department dashboard?
  • What reminders should be in reminders portlet?
  • Which reports should be immediately accessible?
  • What drill-down capabilities are needed?
  • Should dashboards be locked or customizable by users?
- **Priority**: Medium-High
- **Suggested Duration**: 90 minutes per department
- **Dependencies**: REQ-003, REQ-005, REQ-006
- **Evidence**: "We do spend some time on the dashboards building those out. It's actually part of the implementation"

## New Questions Identified

### Proposed New Question: BI-NEW-01. What is the approved threshold for large data export notifications?
- **Asked By**: Marcus (implied during export security discussion)
- **Context**: Need to define what constitutes a "large" export that triggers notifications
- **Suggested Placement**: Security & Compliance section
- **Evidence**: "Trigger system to alert if more than 50 megabytes of data are being downloaded."

### Proposed New Question: BI-NEW-02. Which roles should have dashboard customization locked vs. flexible?
- **Asked By**: Marcus (through example)
- **Context**: Manager control vs. user autonomy
- **Suggested Placement**: Dashboard Configuration section
- **Evidence**: "'I changed my dashboard.' I'm like, 'No, you're not doing that.' So then what I would do is I create a dashboard for them, publish it, and they can't change it."

### Proposed New Question: BI-NEW-03. What is the complete list of current Excel/Google Sheets reports that need to be recreated in NetSuite?
- **Asked By**: Implied from discussion
- **Context**: Need inventory of current reporting to ensure nothing is missed
- **Suggested Placement**: Current State Assessment
- **Evidence**: "You guys are doing a lot about a lot of reporting outside in Google sheets" - Marcus

### Proposed New Question: BI-NEW-04. Should Power BI be maintained post-implementation, and if so, for which use cases?
- **Asked By**: Marcus (offering option)
- **Context**: Decision needed on dual BI platform strategy
- **Suggested Placement**: Platform Strategy section
- **Evidence**: "I don't want to discourage you from using Power BI. If you love Power BI, use it, just keep in mind that the data is aged once it's out."

### Proposed New Question: BI-NEW-05. What are the specific metrics for sales rep scorecards?
- **Asked By**: Wendy (request)
- **Context**: Need detailed requirements for scorecard content
- **Suggested Placement**: KPI & Scorecard section
- **Evidence**: "So I would love them to see that on their own dashboard."

## Questionnaire Responses

### 1. SCOPE CONFIRMATION

**Question:** What is the scope of Business Intelligence & Reporting requirements for this implementation?

**Answer:**
Business Intelligence & Reporting encompasses:
- **Dashboards**: Role-based, department-specific dashboards with KPIs, charts, and drill-down capabilities
- **Standard Reporting**: 400+ NetSuite reports customized for KBM Hoag needs
- **Saved Searches**: Custom queries with inline editing, highlighting, and mass update
- **Workbook Analytics**: Excel-like pivot tables and charts within NetSuite
- **SuiteQL**: Advanced querying for technical users
- **Data Governance**: Official report designation, naming conventions, and standardization
- **Export Security**: Role-based permissions and large export notifications
- **Executive Reporting**: Financial review presentations and scheduled distribution
- **Process Area Reporting**: Marketing/CRM pipeline, Financial statements, Order Management backlog/bookings, Operations PM workload, Pre-Quote tracking

**User Stories:**
- As a CFO - Lorraine, I need real-time financial dashboards so that I can review financial health without waiting for manual report packages
- As a Sales Manager - Wendy, I need sales rep scorecards on individual dashboards so that team members can self-monitor performance
- As a Manager - Marcus (example), I need to lock team dashboards so that everyone reviews the same data during weekly meetings
- As an Account Manager, I need status reports to execute my job responsibilities
- As a Department Head, I need to know who is exporting large amounts of data so that I can prevent potential data breaches

**BRD Requirements:**
- [REQUIREMENT] Real-time dashboard access across all process areas (ID: REQ-001, Type: Functional)
- [REQUIREMENT] Role-based dashboard publishing with lock-down capability (ID: REQ-003, Type: Functional)
- [REQUIREMENT] Export security controls with notifications (ID: REQ-011, REQ-012, Type: Non-Functional, Security)
- [PRIORITY] Must-Have: Dashboards, Standard Reporting, Saved Searches, Data Governance
- [PRIORITY] Should-Have: Workbook Analytics, SuiteQL, Scheduled Distribution
- [PRIORITY] Nice-to-Have: Power BI integration with live connection

**Stakeholder Impact:**
- **Primary Users**: All employees - daily dashboard interaction
- **Secondary Users**: Executives - periodic financial review
- **Approvers**: Department Heads - official report designation, dashboard design
- **Impacted Parties**: Sales reps (scorecards), Managers (team visibility), IT Security (export controls)

**Evidence:**
- "At this point, do you feel there's anything we have yet to talk about from a reporting business intelligence standpoint and we can kind of go through the process areas again." - Marcus
- Coverage discussion included Marketing & CRM, Financials, Operations, Order Management

**Confidence Rating**: 95% - Comprehensive discussion of BI scope with explicit coverage of all process areas

**Outstanding Items:**
- Complete inventory of current Excel/Google Sheets reports needed

---

### 2. CURRENT STATE ASSESSMENT

**Question:** What is the current state of Business Intelligence & Reporting at KBM Hoag?

**Answer:**
Current state is characterized by **fragmented, manual, and inconsistent reporting** across the organization:

**Key Challenges:**
1. **Multiple Report Versions**: "Right now we have reports that are like, you know, Mark's version, Matt's version, Kip's version" - Same report name with different criteria, leading to trust issues
2. **Excel-Based Processes**: Heavy reliance on manual Excel report generation, not real-time
3. **Google Sheets Overload**: Multiple departments using Google Sheets for reporting, not integrated
4. **No Export Controls**: "Right now there's not a lot of control in Core to determine who can export what information" - Customer data vulnerable
5. **Broken Org Hierarchy**: "Me and my team" filters don't work in Core - "I've never gotten that"
6. **Manual Data Compilation**: Month-end executive packages require copy/paste from multiple sources
7. **Inconsistent Dashboards**: Users customize away required views, breaking manager-team alignment

**Specific Examples:**
- **Booking Report**: Currently in "Director's tab in shared folder" showing YTD performance and GP by sales rep
- **Financial Reporting**: Manual compilation needed for executive review when not co-located
- **Sales Goals**: Excel-based, distributed weekly
- **KPI Tracking**: Manual processes, "reporting is so manual"

**Current State Process:**

**PROCESS**: Monthly Financial Review  
**TRIGGER**: Month-end close completion  
**STEPS**:
1. Finance team generates multiple reports from various sources → Creates manual package
2. If executives not co-located → Package sent via email
3. Executive reviews static package → Questions arise
4. Follow-up meetings to drill into details → Additional reports requested
5. Cycle repeats → Time-consuming and error-prone

**SYSTEMS INVOLVED**: Core ERP, Excel, Google Sheets, Zendesk (historical)  
**PAIN POINTS**: 
- Multiple versions of "same" report with different numbers
- Manual compilation time-consuming
- No real-time data
- Trust issues: "people don't trust the reporting"
- "Singing from different songbooks"

**BRD Requirements:**
- [REQUIREMENT] Replace Excel/Google Sheets reporting with NetSuite native tools (ID: REQ-001, Type: Functional)
- [REQUIREMENT] Implement single source of truth reporting (ID: REQ-008, REQ-010, Type: Functional)
- [CONSTRAINT] All-or-nothing export permissions (cannot restrict by report)
- [RISK] User resistance to locked dashboards and official reports only
- [RISK] Change management for teams accustomed to creating own reports
- [PRIORITY] Must-Have

**Stakeholder Impact:**
- **Primary Users**: Finance team (manual processes), Sales team (Excel-based goals), All managers (inconsistent data)
- **Approvers**: Lorraine (CFO) - receives manual packages
- **Impacted Parties**: All employees creating personal report versions

**Evidence:**
- "With all these tools, some of the problems that I've seen companies run into with these tools. A lot of it comes down to people writing reports, naming them similar. They have different criteria. You have different numbers, and people don't trust the reporting." - Marcus
- "I want a revenue report for this time frame, and that revenue report can be written four or five different ways. Are you including taxes? Are you not including taxes? Are you looking at the net amount? Is that before discounts or after discounts? There's so many different ways to write that." - Marcus
- "This is like a constant problem of people looking at the data differently and then not trusting the reports. And it really kind of comes down to... We used to call it singing from the same songbook. Yeah. It's a different key." - Marcus

**Confidence Rating**: 95% - Extensive direct quotes about current pain points and specific examples

**Outstanding Items:**
- Complete list of all Excel/Google Sheets reports currently in use
- Current users with export access and data breach concerns
- Specific examples of report discrepancies that have caused issues

---

### 3. BUSINESS OBJECTIVES & STRATEGY

**Question:** What are the business objectives for Business Intelligence & Reporting in NetSuite/Orion?

**Answer:**
The overarching objective is to establish a **single source of truth** for all reporting with real-time data access:

**Primary Objectives:**
1. **"Singing from the Same Songbook"**: Eliminate multiple report versions and establish standardized official reports
2. **Real-Time Decision Making**: Replace manual, aged Excel reports with live NetSuite dashboards
3. **Daily Work Clarity**: Use Reminders Portlet to eliminate guessing about daily priorities - "you shouldn't have to guess"
4. **Manager-Team Alignment**: Lock dashboards for team consistency in weekly meetings
5. **Data Security**: Implement export controls and notifications to protect customer data
6. **Self-Service Analytics**: Enable drill-down and workbook analytics for users to answer own questions
7. **Executive Efficiency**: Provide real-time financial review capability without manual packages
8. **Aesthetic Excellence**: "The home you live in all day" should look good and feel good

**Strategic Approach:**
- **Dashboard Philosophy**: Department-specific centers with role-based publishing, personal home dashboard option
- **Report Governance**: GSI/Orion prefix for official reports, public/private controls, standardized criteria documentation
- **Change Management**: Lock-down capability for required views while allowing personal exploration
- **Progressive Adoption**: Start with official reports, allow personal searches if kept private

**User Stories:**
- As an Executive Team Member, I need real-time dashboards so that I can make decisions based on current data instead of aged snapshots
- As a Manager, I need locked team dashboards so that weekly meetings reference the same data and eliminate "I don't see that" excuses
- As a Department Head, I need official reports with documented criteria so that everyone interprets metrics consistently
- As a Daily User, I need a reminders portlet so that I know exactly what work to prioritize without guessing
- As an IT Security Lead, I need export notifications so that I can detect potential data exfiltration before damage occurs

**BRD Requirements:**
- [REQUIREMENT] Establish official report designation system (ID: REQ-008, Type: Functional)
- [FUNCTIONALITY] NetSuite Dashboards, Saved Searches, Workbook Analytics, Standard Reports
- [SOLUTIONDESIGN] Yes - Custom dashboard components, export notification system, official report framework
- [PRIORITY] Must-Have: Single source of truth, real-time dashboards, reminders portlet
- [PRIORITY] Should-Have: Locked dashboard publishing, official report framework
- [PRIORITY] Nice-to-Have: Orion-enhanced aesthetics

**Stakeholder Impact:**
- **Primary Users**: All employees - shift from Excel to NetSuite
- **Approvers**: Department Heads - designate official reports
- **Impacted Parties**: Report creators - can no longer create uncontrolled variants

**Evidence:**
- "We used to call it singing from the same songbook. Yeah. It's a different key." - Marcus
- "This is all the work that I have to work off of. Like it shouldn't, you shouldn't have to guess." - Marcus (on Reminders Portlet)
- "We kind of think of NetSuite as kind of the home that you're living in all day. So it should look good. So you feel good about where you're living." - Marcus
- "'I changed my dashboard.' I'm like, 'No, you're not doing that.' So then what I would do is I create a dashboard for them, publish it, and they can't change it." - Marcus

**Confidence Rating**: 95% - Clear articulation of strategy throughout transcript

**Outstanding Items:**
- Prioritization of objectives if timeline/budget constraints arise
- Specific success metrics to measure "singing from same songbook" achievement

---

### 4. DASHBOARD REQUIREMENTS

**Question:** What are the specific dashboard requirements for KBM Hoag?

**Answer:**
Comprehensive dashboard strategy with **role-based publishing, department-specific centers, and daily reminders portlet**:

**Dashboard Structure:**
1. **Home Tab**: Personal/default dashboard (customizable by user)
2. **Finance Center**: CFO and finance team dashboard
3. **Sales Center**: Pipeline, opportunities, scorecards
4. **Pre-Quote Center**: Pre-quote process dashboard
5. **Order Management Center**: Backlog 360, Bookings 360, acknowledgements
6. **Operations Center**: PM workload, resource utilization
7. **Additional Centers**: As needed per process area

**Dashboard Components:**
- **KPI Highlights**: Top of dashboard - key metrics (bank balance, revenue, expenses, profit, etc.)
- **Financial Overview Sections**: Period-over-period reporting with drill-down
- **Interactive Charts**: Filter-enabled, stackable filters, drill to detail
- **Saved Search Results**: Tables with inline editing capability
- **Reminders Portlet**: CRITICAL - daily work driver, actionable items
- **Recent Transactions**: Quick access to latest activities
- **Task Lists**: Personal and departmental tasks

**Publishing & Control:**
- **Role-Based Publishing**: Manager publishes dashboard to role (e.g., all sales reps)
- **Lock-Down Capability**: Published dashboards cannot be modified by users
- **Personal Option**: Users can still have personal dashboard on Home tab
- **Manager Control**: Ensures weekly meetings use same data, eliminates "I changed my dashboard" excuse

**Aesthetic Requirements:**
- **Orion-Enhanced Components**: Better visual appearance than standard NetSuite
- **Modern Look**: "Should look good" - "home you're living in all day"
- **User Experience Focus**: Pleasant daily interaction

**Reminders Portlet (Critical):**
- **Concept**: "All the work that I have to work off of" - no guessing
- **Content Examples**: Bills to pay, bills on hold, tasks to complete, acknowledgements to review, opportunities needing follow-up, phone calls to make, events scheduled, period close checklist
- **Functionality**: Click to drill down, work task list, mark complete, real-time updates
- **Scope**: Individual AND departmental versions

**Interactivity:**
- **Drill-Down Links**: From KPI to detail report to transaction level
- **On-the-Fly Filtering**: Change parameters dynamically
- **Real-Time Data**: No refresh needed
- **Export Options**: CSV, Excel, PDF (if role permits)

**Current State Process:**

**PROCESS**: Weekly Sales Team Meeting  
**TRIGGER**: Weekly scheduled meeting  
**STEPS** (Current - Core):
1. Manager prepares discussion points → References dashboard
2. Team members join meeting → Some have customized dashboards
3. Manager references opportunity → Team member says "I don't see that"
4. Meeting derailed → Time wasted reconciling different views
5. Decisions delayed → Accountability weakened

**STEPS** (Future - NetSuite with Locked Dashboard):
1. Manager prepares discussion points → References published dashboard
2. Team members join meeting → ALL have identical dashboard
3. Manager references opportunity → Everyone sees same data
4. Discussion productive → Decisions made efficiently
5. Accountability clear → Follow-up unambiguous

**SYSTEMS INVOLVED**: NetSuite, Orion Dashboard Components  
**PAIN POINTS SOLVED**: Dashboard customization breaking alignment, "I don't see that" excuses, inconsistent weekly meetings

**User Stories:**
- As a Sales Manager, I need to publish locked dashboards to my team so that weekly meetings reference identical data
- As a CFO, I need a financial overview dashboard with drill-down so that I can assess financial health and investigate details without requesting reports
- As an Employee, I need a reminders portlet so that I start each day knowing exactly what to work on
- As a Finance Team Member, I need a departmental reminders portlet showing bills to pay and period close tasks
- As a Manager, I need to see "me and my team" filters so that I can view my direct reports' performance
- As a Sales Rep, I need to see "me only" filter so that I focus on my own performance

**BRD Requirements:**
- [REQUIREMENT] Build department-specific dashboards for each center (ID: REQ-005, Type: Functional)
- [REQUIREMENT] Implement role-based dashboard publishing (ID: REQ-003, Type: Functional)
- [REQUIREMENT] Enable dashboard lock-down to prevent user customization (ID: REQ-003, Type: Functional)
- [REQUIREMENT] Implement reminders portlet for individual and departmental use (ID: REQ-006, REQ-007, Type: Functional)
- [REQUIREMENT] Use Orion-enhanced dashboard components (ID: REQ-004, Type: Non-Functional, Aesthetic)
- [FUNCTIONALITY] NetSuite Dashboard Framework, Saved Searches, KPI Components, Reminders Portlet
- [SOLUTIONDESIGN] Yes - Custom Orion components, lock-down configuration
- [PRIORITY] Must-Have: Department dashboards, reminders portlet, drill-down capability
- [PRIORITY] Should-Have: Lock-down capability, Orion-enhanced components
- [CONSTRAINT] Dashboard design sessions required per department (time investment)

**Stakeholder Impact:**
- **Primary Users**: All employees - daily dashboard interaction
- **Secondary Users**: Managers - team dashboard control
- **Approvers**: Department Heads - dashboard content approval
- **Impacted Parties**: Users who customized dashboards in Core - loss of control

**Evidence:**
- "This reminders portlet is key. So you can write a safe search. You can put it in this reminders portlet. And this is really what everybody's work is on a daily basis." - Marcus
- "'I changed my dashboard.' I'm like, 'No, you're not doing that.' So then what I would do is I create a dashboard for them, publish it, and they can't change it." - Marcus
- "We do spend some time on the dashboards building those out. It's actually part of the implementation, not software." - Marcus
- "Was that by individual or could it be departmental?" - Lorraine; "Either one. Yep." - Marcus
- "We kind of think of NetSuite as kind of the home that you're living in all day. So it should look good. So you feel good about where you're living." - Marcus

**Confidence Rating**: 98% - Extensive detailed discussion with specific examples

**Outstanding Items:**
- Specific KPIs for each department's dashboard
- Which roles should have locked vs. flexible dashboards
- Detailed reminders portlet content by department
- Executive dashboard requirements for Lorraine and Mark

---

### 5. STANDARD REPORTING REQUIREMENTS

**Question:** What standard reporting capabilities are required?

**Answer:**
Leverage **400+ standard NetSuite reports** with customization and as-of-date capability:

**Standard Reports Available:**
- Income Statement
- Balance Sheet
- Trial Balance
- Cash Flow
- AR/AP Aging
- Receive Not Invoiced
- Receive Not Scheduled
- Order Status Reports
- Backlog Reports (by line, by order, 360)
- Booking Reports (by line, by order, 360)
- Pipeline Reports
- And 390+ more

**Key Capabilities:**
1. **Customization**: "Every single one of those reports can be customized. So if you need a variation of that report, it's very simple."
2. **As-Of Date**: "Reporting in NetSuite is unique because you can get the as of dates for those reports. So like what was my balance sheet as of September 1st. You can get that."
3. **Export Options**: CSV, XLS, PDF - can schedule automated distribution
4. **Print Capability**: Direct printing from system

**Financial Reporting:**
- **Monthly Close**: Income statement, balance sheet, trial balance standard suite
- **Executive Review**: Real-time presentation capability vs. manual package
- **Historical Comparison**: Period-over-period using as-of dates
- **Drill-Down**: From summary report to detail transactions

**Process Area Reporting:**

**Marketing & CRM:**
- Pipeline reports
- Lead conversion
- Campaign ROI
- Opportunity tracking
- Sales rep performance

**Financial Management:**
- Income statement, balance sheet, trial balance
- Cash flow
- AR/AP aging
- Bank reconciliation
- Period close checklist

**Order Management:**
- Backlog 360 - "everything you could ever imagine for backlog in one place"
- Bookings 360 - similar comprehensive approach
- Acknowledgement tracking
- Fulfillment status
- Invoice tracking
- Customer PO utilization

**Operations:**
- PM workload
- Resource utilization
- Project status
- Work order completion
- Punch list tracking
- Time tracking reports

**Pre-Quote:**
- RFP tracking
- Quote pipeline
- Win/loss analysis
- Resource allocation

**Account Manager Status Reports:**
- Critical to account manager workflow
- Exists in production (not in demo account shown)

**User Stories:**
- As a CFO, I need as-of-date financial reports so that I can compare period-end snapshots and conduct historical analysis
- As an Executive, I need to present financial reports in real-time so that I can drill down to answer questions during review meetings without requesting follow-up reports
- As a Department Head, I need to export reports to Excel when necessary so that I can perform external analysis
- As an Account Manager, I need status reports so that I can execute my daily job responsibilities

**BRD Requirements:**
- [REQUIREMENT] Customize standard NetSuite reports for KBM Hoag needs (ID: REQ-013, Type: Functional)
- [REQUIREMENT] Enable as-of-date reporting capability (ID: REQ-014, Type: Functional)
- [REQUIREMENT] Configure export options (CSV, XLS, PDF) based on role permissions (ID: REQ-024, Type: Functional)
- [REQUIREMENT] Build Backlog 360 comprehensive dashboard (ID: REQ-026, Type: Functional)
- [REQUIREMENT] Build Bookings 360 comprehensive dashboard (ID: REQ-027, Type: Functional)
- [FUNCTIONALITY] NetSuite Standard Reports Module, Report Customization Tool
- [PRIORITY] Must-Have: Core financial reports, backlog/bookings, pipeline reports
- [PRIORITY] Should-Have: 360 comprehensive dashboards, historical as-of-date reports

**Stakeholder Impact:**
- **Primary Users**: Finance team (financial reports), Sales team (pipeline), Operations (PM workload), Order Management (backlog/bookings)
- **Secondary Users**: Executives (monthly review)
- **Approvers**: Department Heads (report customization approval)

**Evidence:**
- "Standard reporting, NetSuite ships with over 400 standard reports. And that's everything from income statement, trial balance, balance sheet. And every single one of those reports can be customized." - Marcus
- "Reporting in NetSuite is unique because you can get the as of dates for those reports. So like what was my balance sheet as of September 1st. You can get that." - Marcus
- "We're building on a backlog 360 dashboard, so it's just one dashboard that has everything you could ever imagine for backlog in one place." - Marcus
- "When we would sit down and we would have our financial reports, I would just pull up the income statement, the balance sheet, trial balance, walk through it." - Marcus

**Confidence Rating**: 95% - Clear discussion of capabilities and examples

**Outstanding Items:**
- Complete list of required report customizations
- Specific as-of-date report requirements by department
- Account manager status report detailed requirements

---

### 6. SAVED SEARCH REQUIREMENTS

**Question:** What saved search capabilities are required?

**Answer:**
Comprehensive **saved search functionality** with inline editing, highlighting, and governance:

**Core Functionality:**
- **Table View**: Lists of records with multiple columns
- **Filtering & Sorting**: Dynamic filters, multiple criteria
- **Export Capability**: CSV, Excel (if role permits)
- **Interactive Features**: Click to view, click to edit, drill to detail

**Inline Editing:**
- **Pencil Icon**: "Whenever you see a pencil here, that means you can edit right here without having to go in and edit the whole record"
- **Status Changes**: Update status without opening full record
- **Bulk Updates**: Work through lists efficiently
- **Context Maintenance**: See surrounding data while updating
- **Use Cases**: Opportunities (status changes), acknowledgements (mark complete), tasks (status updates), any list-based work

**Highlighting Rules:**
- **Visual Indicators**: Conditional formatting based on criteria
- **Color Coding**: Quick identification of issues
- **Example**: "If the expected close date is before today that's a problem" - highlight overdue in red
- **Priority Signaling**: Easy to spot high-priority items

**Mass Update:**
- **Bulk Operations**: Update multiple records simultaneously
- **Field Updates**: Change fields across multiple records
- **Data Cleanup**: Efficiency for large-scale changes
- **Process Automation**: Streamline repetitive tasks

**Saved Search Governance:**
- **Prefix Strategy**: GSI/Orion prefix for official searches
- **Official Designation**: Nominate specific searches as "official"
- **Public/Private Control**: "If you're going to make your own search, make it public [or] no one else needs to see that"
- **Visibility Control**: Public (all users), Private (personal only), Role-based (specific roles)

**Benefits:**
- **Efficiency**: Don't open each record individually
- **Context**: See list view while updating
- **Speed**: Bulk operations faster than one-by-one
- **Flexibility**: "For those of you that like tables of data and not visuals, we got them"

**User Stories:**
- As a Sales Rep, I need to inline-edit opportunity statuses from a saved search so that I can quickly update my pipeline without opening each record
- As a Manager, I need highlighting rules on saved searches so that I can quickly identify overdue items
- As a Department User, I need to create private saved searches so that I can explore data without cluttering the system for others
- As a Power User, I need mass update functionality so that I can efficiently process bulk changes
- As an Operations User, I need saved searches for task management so that I can work through task lists efficiently

**Current State Process:**

**PROCESS**: Updating Opportunity Statuses  
**TRIGGER**: Daily pipeline review  
**STEPS** (Current - inefficient):
1. User runs opportunity report → Views list in Excel or Core
2. User clicks first opportunity → Opens full record
3. User updates status field → Saves and closes
4. User clicks second opportunity → Opens full record
5. Repeat for 20-30 opportunities → 30-45 minutes

**STEPS** (Future - NetSuite with Inline Editing):
1. User opens opportunity saved search → Views list with inline edit
2. User clicks status pencil icon → Dropdown appears
3. User changes status → Auto-saves
4. User immediately clicks next status → Updates
5. Complete 20-30 opportunities → 5-10 minutes

**SYSTEMS INVOLVED**: NetSuite Saved Searches  
**PAIN POINTS SOLVED**: Opening/closing records repeatedly, time wasted, loss of context

**BRD Requirements:**
- [REQUIREMENT] Enable inline editing from saved searches (ID: REQ-017, Type: Functional)
- [REQUIREMENT] Implement highlighting rules for visual indicators (ID: REQ-018, Type: Functional)
- [REQUIREMENT] Enable mass update functionality (ID: REQ-019, Type: Functional)
- [REQUIREMENT] Implement public/private saved search controls (ID: REQ-009, Type: Functional)
- [REQUIREMENT] Prefix GSI/Orion saved searches (ID: REQ-008, Type: Non-Functional, Governance)
- [FUNCTIONALITY] NetSuite Saved Searches, Inline Editing, Highlighting Rules, Mass Update
- [PRIORITY] Must-Have: Saved searches, inline editing, official search designation
- [PRIORITY] Should-Have: Highlighting rules, mass update
- [PRIORITY] Nice-to-Have: Advanced highlighting logic

**Stakeholder Impact:**
- **Primary Users**: All users working with lists (opportunities, tasks, acknowledgements, etc.)
- **Power Users**: Mass update capability
- **Managers**: Official search control
- **Impacted Parties**: Users creating uncontrolled searches - governance applied

**Evidence:**
- "Whenever you see a pencil here, that means you can edit right here without having to go in and edit the whole record." - Marcus
- "So if I need to like quickly go through my opportunity list and change things, I can do that. But think about that for anything else in the system." - Marcus
- "I'm going to say if the expected close date is before today that's a problem" - Marcus (highlighting example)
- "There's also a mass update function that's a little more involved, but you can, in a safe search, do a mass update." - Marcus
- "If you're going to make your own search, make it public [or] no one else needs to see that." - Marcus

**Confidence Rating**: 95% - Detailed demonstration and discussion

**Outstanding Items:**
- Specific saved searches to be created for each department
- Highlighting rule standards for consistency
- Training on when to use inline edit vs. full record edit
- Guidelines for public vs. private search designation

---

### 7. WORKBOOK ANALYTICS REQUIREMENTS

**Question:** What workbook analytics capabilities are required?

**Answer:**
**Excel-like functionality within NetSuite** for pivot tables, charts, and interactive analysis:

**Core Capabilities:**
- **Pivot Tables**: Build within NetSuite
- **Charts & Graphs**: Multiple visualization options
- **Data Manipulation**: Excel-like interface
- **Interactive Filters**: Top-of-page filtering

**Example Shown:**
- **Pipeline Analysis**: Filter by team member, location, product type
- **Interactive Charts**: Click to drill down
- **Stackable Filters**: Multiple simultaneous filters
- **Role Limitation**: Can default to "me only" or "me and my team"

**Filter Capabilities:**
- **Me Only**: Individual sees only own data
- **Me and My Team**: Manager sees direct reports
- **Specific People**: Select individual team members
- **Date Ranges**: Flexible date filtering
- **Product Types**: "And just furniture" example
- **Location**: "The east" example
- **Stackable**: "And just furniture. And then all these are stackable. So you can set multiple filters"

**Visualization Options:**
- Charts (various types)
- Graphs
- Tables
- Combinations

**Dashboard Integration:**
- **Pinning**: "This is an analytics workbook and we're just pinning the results of it to a dashboard"
- **Live Data**: Real-time updates
- **Interactivity Preserved**: Filters work on dashboard

**Excel Replacement:**
- "Sometimes little things like this you have to do in Excel, but this is an analytics workbook"
- Goal to reduce Excel dependency

**User Stories:**
- As a Sales Manager, I need pipeline analytics with filters so that I can analyze team performance by location, product type, and time period
- As a Manager, I need "me and my team" filter so that I see my direct reports' data automatically
- As an Individual Contributor, I need "me only" filter default so that I focus on my own metrics
- As a Power User, I need to create custom pivot tables so that I can answer ad-hoc analysis questions without IT support

**BRD Requirements:**
- [REQUIREMENT] Enable workbook analytics for pivot tables and charts (ID: REQ-015, Type: Functional)
- [FUNCTIONALITY] NetSuite Workbook Analytics Module
- [PRIORITY] Should-Have: Workbook analytics reduces Excel dependency
- [CONSTRAINT] Requires proper org structure configuration for "me and my team" filters to work

**Stakeholder Impact:**
- **Primary Users**: Analysts, managers needing flexible analysis
- **Secondary Users**: Power users creating custom analytics
- **Impacted Parties**: Users currently building complex Excel analyses

**Evidence:**
- "We also have workbooks, which is like think of like Excel. It's called workbook analytics. So pivot table charts, you can build those out inside NetSuite." - Marcus
- "This has filters at the top so I can see, here's my pipeline, but here's everybody's pipeline. So if I was a manager and I had access to this, I could see everybody's." - Marcus
- "Can you limit what that click down is so they can only see theirs? Yep. It can be defaulted." - Marcus
- "And just furniture. Well, somebody's not selling over there in the east. And just furniture. And then all these are stackable. So you can set multiple filters and that'll influence what shows up." - Marcus

**Confidence Rating**: 90% - Clear demonstration with example, some details not fully explored

**Outstanding Items:**
- Specific workbook analytics to be created by department
- Training needs assessment for workbook analytics
- Power user identification for advanced analytics

---

### 8. SUITEQL REQUIREMENTS

**Question:** What SuiteQL (advanced querying) capabilities are required?

**Answer:**
**Advanced SQL-like querying** for technical users requiring custom reporting:

**Capability:**
- "SuiteQL, which is NetSuite's kind of own version of SQL. You can, so that means you can write queries"
- Bypass application layer
- Direct database queries
- Very fast execution
- Advanced reporting beyond standard tools

**Target Audience:**
- **Technical Users**: Kipp mentioned as example
- **Database-Savvy Staff**: Users comfortable with SQL syntax
- **Custom Report Needs**: When standard reports insufficient
- **Performance-Critical Queries**: When speed is essential

**Use Cases:**
- Complex multi-table joins
- Advanced calculations
- Custom data extracts
- Performance-optimized queries
- Ad-hoc technical analysis

**User Stories:**
- As a Technical User - Kipp, I need SuiteQL access so that I can write custom queries for complex reporting needs
- As a Data Analyst, I need to query the database directly so that I can perform advanced analysis not possible with standard tools

**BRD Requirements:**
- [REQUIREMENT] Configure SuiteQL access for technical users (ID: REQ-016, Type: Functional)
- [FUNCTIONALITY] NetSuite SuiteQL Module
- [PRIORITY] Should-Have: SuiteQL for advanced users
- [CONSTRAINT] Requires SQL knowledge - limited user base
- [RISK] Poorly written queries could impact performance

**Stakeholder Impact:**
- **Primary Users**: Kipp and other technical users
- **Secondary Users**: None (specialized capability)
- **Approvers**: IT - grant SuiteQL access permissions
- **Impacted Parties**: System performance if queries not optimized

**Evidence:**
- "We have SuiteQL, which is NetSuite's kind of own version of SQL. You can, so that means you can write queries." - Marcus
- Kipp identified as technical user in context

**Confidence Rating**: 85% - Capability discussed but not demonstrated in detail

**Outstanding Items:**
- Complete list of users requiring SuiteQL access
- SuiteQL governance and query review process
- Performance monitoring for custom queries
- Training needs for SuiteQL syntax

---

### 9. DATA EXPORT & SECURITY REQUIREMENTS

**Question:** What are the data export and security requirements?

**Answer:**
**Critical security concern** requiring role-based permissions and notification system:

**Current State Problem:**
"Right now there's not a lot of control in Core to determine who can export what information. So we haven't had this issue, but someone who was in sales and left one company and came to another company, you know, I could [export customer data]"

**Concerns:**
- Customer data theft
- Competitive intelligence
- Employee departure risks
- Data breach potential
- No ability to prevent customer list export in Core

**NetSuite Solution:**

**1. Role-Based Export Permissions:**
- "For a given role there is a report export [permission] and that's what actually shows the button for like PDF and Excel and everything. You can turn that off on a role basis"
- **Control**: Enable/disable export button per role
- **Limitation**: "It's an all-or-nothing setting" - cannot restrict per-report
- **Challenge**: "What if I want them to be able to export order details into Excel because they need to manipulate the data... there's like pros and cons to turning it off and on"

**2. Notification System (ACCOMMODATE):**
- **Proposed**: "Trigger system to alert if more than 50 megabytes of data are being downloaded"
- **Purpose**: Alert management to large data exports
- **Response**: Investigate and intervene if necessary
- **Limitation**: Won't prevent export, but provides awareness

**3. Workaround Reality:**
- "Another thing, too, just to be aware of, like, if you have a report and they don't have the ability to export it, they can technically, because it's browser-based, just highlight everything, Control-C, Control-V, and Excel, and they got it."
- **Reality**: Cannot completely prevent data extraction
- **Strategy**: Balance control vs. functionality, awareness vs. prevention

**Decision Made:**
"Let's list that as a requirement, some permission around exporting and some notifications around if something was exported over a certain amount."

**User Stories:**
- As an IT Security Lead, I need role-based export permissions so that I can control which users can extract data from the system
- As a Department Head, I need notifications for large data exports so that I can investigate potential data breaches before an employee departs
- As a Sales Manager, I need my team to export order details for analysis but not export customer lists
- As a Compliance Officer, I need audit trails of data exports so that I can demonstrate security controls

**BRD Requirements:**
- [REQUIREMENT] Implement role-based export permissions (ID: REQ-011, Type: Non-Functional, Security)
- [REQUIREMENT] Configure notification system for large data exports (ID: REQ-012, Type: Non-Functional, Security)
- [FUNCTIONALITY] NetSuite Role Permissions, Custom Workflow for Notifications
- [SOLUTIONDESIGN] Yes - Custom notification workflow for export monitoring
- [CONSTRAINT] All-or-nothing export permissions (cannot restrict per-report)
- [CONSTRAINT] Browser copy-paste workaround exists (cannot fully prevent)
- [RISK] Disabling export may reduce productivity for legitimate use cases
- [RISK] Notification after export - reactive not preventive
- [PRIORITY] Must-Have: Role-based permissions, notification system

**Stakeholder Impact:**
- **Primary Users**: IT Security - manage permissions
- **Secondary Users**: Department Heads - receive notifications
- **Approvers**: Executive Team - security policy
- **Impacted Parties**: All users - some lose export capability, some monitored

**Evidence:**
- "Right now there's not a lot of control in Core to determine who can export what information." - Speaker (KBM)
- "For a given role there is a report export [permission] and that's what actually shows the button for like PDF and Excel and everything. You can turn that off on a role basis." - Marcus
- "My first glance it is it's an all-or-nothing setting." - Marcus
- "Trigger system to alert if more than 50 megabytes of data are being downloaded." - Speaker (KBM)
- "Let's list that as a requirement, some permission around exporting and some notifications around if something was exported over a certain amount." - Speaker (KBM)

**Confidence Rating**: 95% - Explicit discussion and decision made

**Outstanding Items:**
- Which roles can export vs. which cannot (decision matrix)
- Final threshold for large export notifications (50MB proposed)
- Who receives export notifications (recipients list)
- Audit trail requirements and retention period
- Special exceptions process for legitimate large exports

---

### 10. REPORT STANDARDIZATION & GOVERNANCE

**Question:** What are the requirements for report standardization and governance?

**Answer:**
**"Singing from the Same Songbook"** - Establish official reports to eliminate trust issues:

**Core Problem:**
"With all these tools, some of the problems that I've seen companies run into with these tools. A lot of it comes down to people writing reports, naming them similar. They have different criteria. You have different numbers, and people don't trust the reporting."

**KBM Current State:**
"Right now we have reports that are like, you know, Mark's version, Matt's version, Kip's version."

**Example Scenario:**
"I want a revenue report for this time frame, and that revenue report can be written four or five different ways. Are you including taxes? Are you not including taxes? Are you looking at the net amount? Is that before discounts or after discounts? There's so many different ways to write that."

**Result:**
"This is like a constant problem of people looking at the data differently and then not trusting the reports. And it really kind of comes down to... We used to call it singing from the same songbook. Yeah. It's a different key."

**Solution Strategy:**

**1. Official Report Designation:**
- "The one thing I'll encourage you to do as we get into implementation is we prefix our saved search, the ones that we create, and then we also sometimes will nominate something as being like an official saved search"
- **Prefix**: GSI/Orion prefix for implementation-created reports
- **Designation**: Nominate specific searches as "official"
- **Communication**: Train users on which reports to use
- **Interpretation**: Document what criteria mean

**2. Public/Private Controls:**
- "If you're going to make your own search, make it public [or] no one else needs to see that"
- **Public**: Visible to others (official or shared searches)
- **Private**: Personal only (exploration, personal analysis)
- **Role-Based**: Only certain roles see (department-specific)

**Benefits:**
- Reduce clutter (fewer searches visible)
- Prevent confusion (clear which is official)
- Maintain standards (official reports controlled)
- Allow personal exploration (private searches permitted)

**3. Standardized Criteria:**
- Document exactly what each official report includes/excludes
- Define terms (e.g., "revenue" includes/excludes taxes, discounts, etc.)
- Establish interpretation guidelines
- Train on official report usage

**4. Version Control:**
- Who can modify official reports?
- How are changes approved?
- How are users notified of changes?
- How are old versions archived?

**User Stories:**
- As a Finance Manager, I need official report designation so that my team trusts the numbers and stops creating personal versions
- As an Executive, I need standardized report criteria so that I can make decisions knowing everyone interprets metrics the same way
- As a Department Head, I need to approve changes to official reports so that standards are maintained
- As a New Employee, I need to know which reports are official so that I don't create redundant versions
- As a Power User, I need to create private searches for exploration without cluttering the system for others

**BRD Requirements:**
- [REQUIREMENT] Establish official report designation with GSI/Orion prefix (ID: REQ-008, Type: Non-Functional, Governance)
- [REQUIREMENT] Implement public/private saved search controls (ID: REQ-009, Type: Functional)
- [REQUIREMENT] Create standardized report criteria documentation (ID: REQ-010, Type: Non-Functional, Documentation)
- [FUNCTIONALITY] NetSuite Saved Search Naming, Role-Based Visibility
- [SOLUTIONDESIGN] No - Standard NetSuite functionality with governance process
- [ASSUMPTION] Users will adopt official reports if clearly designated and trained
- [RISK] User resistance to official reports only (loss of autonomy)
- [RISK] Official reports may not meet every edge case need
- [PRIORITY] Must-Have: Official report strategy, naming convention
- [PRIORITY] Should-Have: Criteria documentation, training materials

**Stakeholder Impact:**
- **Primary Users**: All users - shift to official reports
- **Approvers**: Department Heads - approve official reports and changes
- **Impacted Parties**: Current report creators (Mark, Matt, Kip versions) - consolidate to official versions

**Evidence:**
- "With all these tools, some of the problems that I've seen companies run into with these tools. A lot of it comes down to people writing reports, naming them similar. They have different criteria. You have different numbers, and people don't trust the reporting." - Marcus
- "Right now we have reports that are like, you know, Mark's version, Matt's version, Kip's version." - Marcus
- "I want a revenue report for this time frame, and that revenue report can be written four or five different ways." - Marcus
- "This is like a constant problem of people looking at the data differently and then not trusting the reports. And it really kind of comes down to... We used to call it singing from the same songbook." - Marcus
- "The one thing I'll encourage you to do as we get into implementation is we prefix our saved search, the ones that we create, and then we also sometimes will nominate something as being like an official saved search." - Marcus

**Confidence Rating**: 98% - Extensive discussion with clear problem statement and solution

**Outstanding Items:**
- Complete list of official reports needed by department
- Who has authority to designate/change official reports?
- Process for requesting new official reports
- Training plan for official report adoption
- Change management strategy for users creating personal versions
- Naming convention standards beyond prefix

---

### 11. ORGANIZATIONAL HIERARCHY & FILTER REQUIREMENTS

**Question:** What are the organizational hierarchy and filter requirements?

**Answer:**
**Properly configured org structure** to enable "me and my team" filters that failed in Core:

**Current State Frustration:**
"That's been one of the frustrations with Core. They do allegedly have this hierarchy of permissions, roles and permissions, and, like, this is the manager. They report to that manager, and that manager is supposed to see everyone, and it doesn't. I've never gotten that."

**NetSuite Solution:**
"You have to have the right managers assigned for those filters to work. But if we set that up, if we set it up, it actually works. Good."

**Critical Success Factor:**
- Proper manager assignments in employee records
- Org structure configuration
- Manager hierarchy maintained

**Filter Types Needed:**
1. **Me Only**: Individual sees only own data (sales rep sees own opportunities)
2. **Me and My Team**: Manager sees direct reports (sales manager sees team's opportunities)
3. **Specific People**: Select individual team members
4. **Department**: All department members
5. **Role**: All users with specific role

**Use Cases:**
- **Sales Rep Scorecard**: "Me only" default - individual performance
- **Manager Scorecard**: "Me and my team" - Wendy mentioned "if he was ever managing them on their dashboard, it shows them all of their people"
- **Pipeline Analytics**: Manager filters to see team or individual rep
- **Reminders Portlet**: Individual or departmental views
- **Workbook Analytics**: Default to appropriate scope

**User Stories:**
- As a Sales Manager, I need "me and my team" filters to work so that I can see my direct reports' opportunities without manual filtering
- As a Sales Rep, I need "me only" default so that I focus on my own pipeline and am not overwhelmed by others' data
- As a Department Head, I need to filter by specific team members so that I can compare performance across individuals
- As an Employee, I need org structure to reflect my actual reporting relationship so that my manager has appropriate visibility

**BRD Requirements:**
- [REQUIREMENT] Configure proper manager hierarchy for filter functionality (ID: REQ-023, Type: Functional, Configuration)
- [REQUIREMENT] Implement "me and my team" filters throughout system (ID: REQ-022, Type: Functional)
- [FUNCTIONALITY] NetSuite Employee Records, Manager Assignment, Role-Based Filtering
- [CONSTRAINT] Requires accurate manager assignments maintained
- [RISK] Org structure changes must be maintained in system or filters break
- [PRIORITY] Must-Have: Manager hierarchy configuration, basic filter types
- [PRIORITY] Should-Have: Complex multi-level hierarchy support

**Stakeholder Impact:**
- **Primary Users**: Managers - rely on team filters
- **Secondary Users**: HR - maintain org structure
- **Approvers**: Executive Team - org structure accuracy
- **Impacted Parties**: All employees - reporting relationships must be accurate

**Evidence:**
- "That's been one of the frustrations with Core. They do allegedly have this hierarchy of permissions, roles and permissions, and, like, this is the manager. They report to that manager, and that manager is supposed to see everyone, and it doesn't. I've never gotten that." - Speaker (KBM)
- "You have to have the right managers assigned for those filters to work. But if we set that up, if we set it up, it actually works. Good." - Marcus
- "Can you limit what that click down is so they can only see theirs? Yep. It can be defaulted." - Marcus (on workbook analytics)

**Confidence Rating**: 90% - Clear frustration with current state and confirmation of NetSuite capability

**Outstanding Items:**
- Current org structure documentation (who reports to whom)
- Multi-level hierarchy requirements (skip-level visibility?)
- Matrix organization handling (dotted-line reporting)
- Process for maintaining manager assignments (HR responsibility?)
- Testing plan to validate filters work correctly after go-live

---

### 12. KPI & SCORECARD REQUIREMENTS

**Question:** What are the KPI and scorecard requirements?

**Answer:**
**Sales rep scorecards and departmental KPIs** on dashboards:

**Sales Rep Scorecards:**

**Current State:**
- "Booking report" exists in "Director's tab in shared folder"
- Shows year-to-date performance
- GP by sales rep
- Manual Excel distribution

**Future State Request:**
**Wendy**: "So I would love them to see that on their own dashboard. And then if he was ever managing them on their dashboard, it shows them all of their people."

**Requirements:**
- **Individual View**: Sales rep sees own scorecard on personal dashboard
- **Manager View**: Manager sees all team members' scorecards
- **Metrics**: Total revenue, total GP, year-to-date performance (based on current booking report)
- **Filters**: Me only (individual), me and my team (manager), specific people, date ranges

**Scorecard Components:**
- Revenue (actual vs. target)
- Gross Profit (actual vs. target, percentage)
- Number of projects
- Win rate
- Pipeline value
- Year-to-date trends
- Period comparisons

**Dashboard KPIs (Examples Shown):**
- **Finance Dashboard**: Bank balance, revenue, expenses, profit, period-over-period
- **Sales Dashboard**: Pipeline value, forecast, closed-won, conversion rate
- **Operations Dashboard**: PM workload, resource utilization, project status

**KPI Tracking:**
"Do you have any kind of like scorecards or anything like that that you do... they were really popular a few years ago but like you can have a scorecard by like maybe sales rep where [it] shows total revenue um total gp across all their projects."

**Current Challenge:**
"Forecasted versus actual… identify trends… reporting is so manual" - Current KPI tracking is manual process

**User Stories:**
- As a Sales Rep, I need my personal scorecard on my dashboard so that I can monitor my performance without requesting reports from management
- As a Sales Manager - Wendy, I need team scorecards on my dashboard so that I can see all direct reports' performance at a glance
- As a CFO, I need financial KPIs at the top of my dashboard so that I can assess financial health immediately upon login
- As a Department Head, I need to track KPIs in real-time so that I can identify trends without manual reporting

**BRD Requirements:**
- [REQUIREMENT] Create sales rep scorecards for individual dashboards (ID: REQ-020, Type: Functional)
- [REQUIREMENT] Build manager view scorecards showing team performance (ID: REQ-021, Type: Functional)
- [REQUIREMENT] Track KPIs: pipeline, forecast accuracy, win/loss trends (referenced in Decision Log from other transcript sections)
- [FUNCTIONALITY] NetSuite KPI Components, Saved Searches, Dashboard Publishing
- [SOLUTIONDESIGN] Yes - Custom scorecard design based on current booking report
- [PRIORITY] Should-Have: Sales rep scorecards (high business value but not core system operation)

**Stakeholder Impact:**
- **Primary Users**: Sales reps (individual scorecards), Sales managers (team scorecards)
- **Secondary Users**: Department heads (departmental KPIs)
- **Approvers**: Wendy (sales leadership) - scorecard design approval
- **Impacted Parties**: Sales team - visibility into performance metrics

**Evidence:**
- "Do you have any kind of like scorecards or anything like that that you do." - Marcus
- "You guys basically do that in the booking report right now okay right?" - Marcus
- "So I would love them to see that on their own dashboard. And then if he was ever managing them on their dashboard, it shows them all of their people." - Wendy

**Confidence Rating**: 90% - Clear request from Wendy, some details need refinement

**Outstanding Items:**
- Specific metrics for sales rep scorecard (beyond revenue and GP)
- Target-setting process for scorecard metrics
- Frequency of scorecard updates (real-time vs. daily/weekly)
- Scorecard design mockup approval
- Other department scorecards needed? (Operations, Finance, etc.)

---

### 13. EXECUTIVE REPORTING REQUIREMENTS

**Question:** What are the executive reporting requirements?

**Answer:**
**Real-time presentation capability** vs. manual packages for executive reviews:

**Current Challenge:**

**Lorraine's Question:**
"On that, like the dashboard is great, especially for the finance team in this instance, but then how are they, when it's month end and they come to present to Mark and I, how are they... do they have to export all of that into Excel or are they able to do the presentation through Orion?"

**Marcus Answer:**
"Yep. Yeah, we just have to, yeah. And whatever you want to see, we would just create that dashboard."

**Marcus's Experience:**
"When we would sit down and we would have our financial reports, I would just pull up the income statement, the balance sheet, trial balance, walk through it. There's usually... questions, drill down, figure out. AR is a great example. Like we look at the AR report and like, why the heck is this past 90 days? Drill down, find the invoice, task out the sales rep to call."

**Current Problem:**
"The problem is we're not, sometimes we're not all together to do a financial review. So I have to send it to somebody. Like this week, in case you're not here, do a package together and send it to me."

**Solution Options:**
1. **Real-Time Presentation**: Pull up dashboards and reports in system, drill down during meeting
2. **Scheduled Reports**: Automatically generate and email report packages
3. **Manual Package**: Compile reports when remote review needed

**Marcus Perspective:**
"If it makes sense to package it so it's easier for the executive team, I can understand why."

**Executive Review Process:**

**PROCESS**: Monthly Financial Review with Executives  
**TRIGGER**: Month-end close complete  
**STEPS** (Ideal - Real-Time):
1. Finance team schedules review meeting → Lorraine and Mark attend
2. Finance lead shares screen → Opens NetSuite financial dashboard
3. Walk through income statement, balance sheet, trial balance → Real-time data
4. Executive asks question → Drill down immediately to detail
5. Example: "Why is AR past 90 days high?" → Click AR report → Find invoice → Task sales rep from meeting
6. Meeting concludes → Action items already assigned in system

**STEPS** (Alternative - Remote):
1. Executives not available for live meeting → Need report package
2. Finance team schedules/generates reports → Automated export and email
3. Executives review offline → Follow-up questions via email
4. Follow-up meeting scheduled → Address questions

**SYSTEMS INVOLVED**: NetSuite Dashboards, Financial Reports, Scheduled Report Distribution  
**PAIN POINTS SOLVED**: Real-time drill-down, immediate answers, no manual package compilation

**Scheduled Report Distribution:**
"Can schedule reports and email automatically"
- Automated generation
- PDF/Excel delivery
- Distribution lists
- Frequency settings (daily, weekly, monthly)

**User Stories:**
- As a CFO - Lorraine, I need to present financial reports from NetSuite so that I can drill down to answer questions during executive review without requesting follow-up reports
- As an Executive - Mark, I need scheduled report packages when I cannot attend live review so that I can review financials asynchronously
- As a Finance Team Lead, I need to automate report distribution so that I don't manually compile packages for executive review
- As an Executive, I need to ask "why" questions during financial review and get immediate answers through drill-down

**BRD Requirements:**
- [REQUIREMENT] Support executive financial review presentations from system (ID: REQ-025, Type: Functional)
- [REQUIREMENT] Enable scheduled report distribution via email (ID: REQ-024, Type: Functional)
- [FUNCTIONALITY] NetSuite Dashboards, Financial Reports, Scheduled Report Distribution
- [PRIORITY] Must-Have: Real-time presentation capability, scheduled distribution
- [CONSTRAINT] Executives need NetSuite access for real-time review (or screen sharing)

**Stakeholder Impact:**
- **Primary Users**: Lorraine (CFO), Mark (Executive), Finance team (presenters)
- **Secondary Users**: Other executives receiving scheduled reports
- **Approvers**: Executive team - report package format approval

**Evidence:**
- "On that, like the dashboard is great, especially for the finance team in this instance, but then how are they, when it's month end and they come to present to Mark and I, how are they... do they have to export all of that into Excel or are they able to do the presentation through Orion?" - Lorraine
- "When we would sit down and we would have our financial reports, I would just pull up the income statement, the balance sheet, trial balance, walk through it. There's usually... questions, drill down, figure out." - Marcus
- "The problem is we're not, sometimes we're not all together to do a financial review. So I have to send it to somebody." - Marcus
- "If it makes sense to package it so it's easier for the executive team, I can understand why." - Marcus

**Confidence Rating**: 95% - Clear discussion of requirements and options

**Outstanding Items:**
- Executive dashboard design for Lorraine and Mark
- Scheduled report frequency and distribution list
- Report package format if needed for remote reviews
- Executive training on drill-down capability

---

### 14. PROCESS AREA SPECIFIC REPORTING

**Question:** What are the process-area-specific reporting requirements?

**Answer:**
**Comprehensive reporting across all process areas** with specialized dashboards:

**Marketing & CRM:**
- Pipeline reports (critical)
- Opportunity tracking by status, sales rep, probability
- Lead conversion metrics
- Campaign effectiveness (if marketing campaigns implemented)
- Sales rep performance metrics
- Kanban board views

**Financial Management:**
- **Standard Financial Reports**: Income statement, balance sheet, trial balance, cash flow
- **AR/AP**: Aging reports, collection tracking
- **Bank Reconciliation**: Period reconciliation tracking
- **Period Close Checklist**: Reminders portlet integration
- **Current Challenge**: "You guys are doing a lot about a lot of reporting outside in Google sheets"
- **Goal**: Move all financial reporting into NetSuite

**Order Management:**
- **Backlog 360**: "We're building on a backlog 360 dashboard, so it's just one dashboard that has everything you could ever imagine for backlog in one place"
  - Backlog by line
  - Backlog by order
  - Comprehensive view
- **Bookings 360**: Similar comprehensive structure
  - Bookings by line
  - Bookings by order
  - Comprehensive view
- **Acknowledgement Tracking**: Status and completion
- **Fulfillment Status**: Order progress tracking
- **Invoice Tracking**: Billing status
- **Customer PO Utilization**: PO tracking
- **Receive Not Invoiced**: Receiving to billing gap
- **Receive Not Scheduled**: Receiving to scheduling gap
- **Account Manager Status Reports**: Critical to daily workflow (exists in production)

**Operations:**
- PM workload visibility
- Resource utilization reporting
- Project status tracking
- Work order completion rates
- Punch list tracking
- Time tracking reports
- Installation tracking

**Pre-Quote:**
- RFP tracking
- Quote pipeline
- Win/loss analysis
- Resource allocation tracking

**Marcus Question:**
"At this point, do you feel there's anything we have yet to talk about from a reporting business intelligence standpoint and we can kind of go through the process areas again."

**Response:** Discussion confirmed coverage of all major process areas

**User Stories:**
- As an Order Management Lead, I need Backlog 360 dashboard so that I have everything about backlog in one place instead of multiple separate reports
- As a Finance Lead, I need to eliminate Google Sheets reporting so that all financial analysis is real-time in NetSuite
- As an Operations Manager, I need PM workload visibility so that I can balance resource allocation across projects
- As a Pre-Quote Lead, I need RFP tracking so that I can manage the pre-quote pipeline effectively
- As an Account Manager, I need status reports so that I can execute my daily job (critical workflow dependency)

**BRD Requirements:**
- [REQUIREMENT] Build comprehensive Backlog 360 dashboard (ID: REQ-026, Type: Functional)
- [REQUIREMENT] Build comprehensive Bookings 360 dashboard (ID: REQ-027, Type: Functional)
- [REQUIREMENT] Migrate Google Sheets financial reporting to NetSuite (implied, related to REQ-001)
- [REQUIREMENT] Create Account Manager status reports (mentioned as critical)
- [FUNCTIONALITY] NetSuite Standard Reports, Custom Dashboards, Saved Searches across all modules
- [SOLUTIONDESIGN] Yes - Backlog 360 and Bookings 360 are custom comprehensive dashboards
- [PRIORITY] Must-Have: Backlog 360, Bookings 360, Financial reports, Account Manager status reports
- [PRIORITY] Should-Have: PM workload, RFP tracking

**Stakeholder Impact:**
- **Primary Users**: Process area leads and teams for respective reports
- **Secondary Users**: Executives for cross-process area visibility
- **Impacted Parties**: Users currently maintaining Google Sheets and Excel reports

**Evidence:**
- "We're building on a backlog 360 dashboard, so it's just one dashboard that has everything you could ever imagine for backlog in one place." - Marcus
- "You guys are doing a lot about a lot of reporting outside in Google sheets" - Marcus
- "I don't know if we have it in this account. Every account manager currently uses status reports to do their jobs." - Marcus
- "At this point, do you feel there's anything we have yet to talk about from a reporting business intelligence standpoint and we can kind of go through the process areas again." - Marcus

**Confidence Rating**: 90% - High-level coverage confirmed, some details need refinement per process area

**Outstanding Items:**
- Detailed Backlog 360 component specifications
- Detailed Bookings 360 component specifications
- Complete Google Sheets inventory to migrate
- Account Manager status report detailed requirements
- PM workload report specifications
- RFP tracking requirements

---

### 15. INTEGRATION REQUIREMENTS

**Question:** What are the integration requirements for Business Intelligence & Reporting?

**Answer:**
**SharePoint and Google Drive integration** for document management with real-time reporting:

**Mentioned Integrations:**
- **SharePoint**: "I think we've mentioned already the SharePoint integration"
- **Google Drive**: Validation needed
- **Power BI** (Optional): With live connection to avoid aged data

**Integration Goals:**
- Keep reporting inside NetSuite system
- Always real-time data
- Document attachment and linking
- Avoid data aging from external tools

**Power BI Strategy:**
"I don't want to discourage you from using Power BI. If you love Power BI, use it, just keep in mind that the data is aged once it's out. But if you have a live connection, you've kind of mitigated that."

**Approach:**
- NetSuite native BI tools as primary platform
- Power BI optional for aged data analysis (if live connection implemented)
- SharePoint/Google Drive for document management, not reporting

**Scheduled Report Distribution:**
- Email system integration
- PDF/Excel delivery
- Automated generation and distribution
- Distribution list management

**User Stories:**
- As a User, I need SharePoint integration so that I can access documents from NetSuite without switching systems
- As a Power BI User, I need live connection to NetSuite so that I can use Power BI without working with aged data
- As an Executive, I need scheduled reports emailed automatically so that I receive timely information without requesting it

**BRD Requirements:**
- [REQUIREMENT] Validate SharePoint integration for reporting (Action Item identified)
- [REQUIREMENT] Validate Google Drive integration for reporting (Action Item identified)
- [REQUIREMENT] Configure Power BI live connection if Power BI is retained (ID: REQ-002, Type: Functional, Optional)
- [FUNCTIONALITY] SharePoint Connector, Google Drive Connector, Email Integration
- [PRIORITY] Should-Have: SharePoint/Google Drive integration
- [PRIORITY] Nice-to-Have: Power BI live connection

**Stakeholder Impact:**
- **Primary Users**: All users if SharePoint/Google Drive used organizationally
- **Secondary Users**: Power BI users (if any)
- **Approvers**: IT - integration configuration

**Evidence:**
- "I think we've mentioned already the SharePoint integration." - Marcus
- "I don't want to discourage you from using Power BI. If you love Power BI, use it, just keep in mind that the data is aged once it's out. But if you have a live connection, you've kind of mitigated that." - Marcus

**Confidence Rating**: 75% - Mentioned but not discussed in detail

**Outstanding Items:**
- Current usage of SharePoint and Google Drive
- Power BI current usage and future strategy decision
- Live connection technical requirements for Power BI
- Document management strategy (SharePoint vs. Google Drive vs. NetSuite native)

---

### 16. CHANGE MANAGEMENT & TRAINING

**Question:** What are the change management and training considerations for Business Intelligence & Reporting?

**Answer:**
**Significant behavior changes required** with structured training and dashboard discipline:

**Behavior Changes Required:**

**1. Use Official Reports:**
- Stop creating personal versions of reports
- Use designated official reports only
- Follow standardized interpretation
- Trust the single source of truth
- **Challenge**: Users accustomed to creating own versions

**2. Dashboard Discipline:**
- Accept published dashboards (cannot customize away)
- Don't resist locked views
- Use provided reminders portlet
- Resist urge to "make it your own"
- **Challenge**: Loss of perceived control

**3. Daily Reminders:**
- Start day with reminders portlet
- Work from system, not email/to-do lists
- Complete tasks inline
- Trust workflow
- **Challenge**: Changing daily habits

**4. Real-Time Mindset:**
- Stop creating static Excel snapshots
- Use live dashboards instead
- Drill down instead of export
- Embrace numbers that change throughout day
- **Challenge**: Comfort with static reports

**5. Export Discipline:**
- Export only when legitimately necessary
- Be aware of data sensitivity
- Use in-system analysis whenever possible
- Respect security controls
- **Challenge**: Current unrestricted export access

**Resistance Points:**

**1. Loss of Control:**
- "Can't customize my dashboard" - feels restrictive
- Manager controls what I see
- "I know what I need better than others"

**2. Learning Curve:**
- New saved search tool
- Different navigation (centers vs. single interface)
- Drill-down vs. export workflow
- Filter combinations

**3. Trust in System:**
- Must trust official reports
- Can't verify with own version
- Rely on others' criteria
- "What if the official report is wrong?"

**4. Export Limitations:**
- Can't extract customer lists
- Notifications for large exports
- All-or-nothing permissions
- Workaround temptation (copy-paste)

**5. Real-Time Adjustment:**
- Used to static Excel snapshots
- Numbers change throughout day
- Different from month-end package mindset
- Period-close timing matters

**Success Factors:**

**1. Reminders Portlet Clarity:**
- Eliminates guessing: "you shouldn't have to guess"
- Clear priorities daily
- Actionable items
- Immediate value perception

**2. Drill-Down Power:**
- See summary, drill to detail instantly
- Answer questions without waiting
- Self-service capability
- Empowerment

**3. Manager-Team Alignment:**
- Everyone seeing same dashboard
- Weekly meetings use same data
- No "I don't see that" excuses
- Clear accountability

**4. As-Of Date Historical:**
- Can still get month-end snapshots
- Historical comparisons possible
- Audit trail maintained
- Best of both worlds

**5. Aesthetic Appeal:**
- Orion-enhanced components look modern
- Pleasant daily experience
- "Home you live in all day"

**6. Inline Editing:**
- Update status without opening records
- Work through lists efficiently
- Immediate productivity gain
- Obvious time savings

**Training Focus Areas:**

**1. Official Report Usage:**
- Which reports are official
- How to interpret each report
- When to use which report
- What criteria mean (taxes included? discounts?)

**2. Saved Search Basics:**
- How to filter and sort
- How to export (if permitted)
- How to save personal searches
- Public vs. private designation

**3. Dashboard Navigation:**
- Centers vs. Home tab concept
- Drill-down technique
- Filter usage and stacking
- Refresh timing and real-time data

**4. Reminders Portlet:**
- How reminders appear
- How to work items from reminders
- How to complete and mark done
- How to prioritize daily work

**5. Inline Editing:**
- Pencil icon recognition
- Quick status changes
- Bulk operations
- When to use vs. full record edit

**6. Workbook Analytics:**
- Pivot table creation
- Chart building
- Filter stacking
- Pinning to dashboard

**7. Data Governance:**
- Why standardization matters
- Export security awareness
- Single source of truth concept
- "Singing from the same songbook" philosophy

**User Stories:**
- As a Manager, I need to communicate the "singing from the same songbook" philosophy so that my team understands why official reports matter
- As a Trainer, I need comprehensive training materials so that I can effectively teach report interpretation and NetSuite navigation
- As a New User, I need clear guidance on which reports are official so that I don't create unnecessary personal versions
- As a Change Management Lead, I need to address loss-of-control concerns so that users embrace locked dashboards

**BRD Requirements:**
- [REQUIREMENT] Create training materials on official report usage (Action Item identified)
- [REQUIREMENT] Document standardized report criteria (ID: REQ-010, Type: Non-Functional, Documentation)
- [ASSUMPTION] Users will adopt official reports if clearly trained and communicated
- [RISK] User resistance to locked dashboards (high change management need)
- [RISK] Continued creation of personal report versions despite training
- [PRIORITY] Must-Have: Training on official reports, dashboard navigation, reminders portlet

**Stakeholder Impact:**
- **Primary Users**: All employees - significant workflow changes
- **Trainers**: GSI/Orion + KBM Hoag SMEs - training delivery
- **Approvers**: Department Heads - reinforce standards
- **Change Agents**: Managers - model behavior and enforce standards

**Evidence:**
- "'I changed my dashboard.' I'm like, 'No, you're not doing that.'" - Marcus (change management example)
- "We used to call it singing from the same songbook." - Marcus (philosophy communication)
- "This is all the work that I have to work off of. Like it shouldn't, you shouldn't have to guess." - Marcus (success factor)

**Confidence Rating**: 90% - Clear implications from discussion, explicit examples of behavior changes

**Outstanding Items:**
- Training schedule and delivery approach
- Who trains whom (trainers identified?)
- Ongoing support model post-go-live
- How to measure adoption success
- Escalation process for users not following standards
- Communication plan for "singing from same songbook" philosophy

---

### 17. TECHNICAL REQUIREMENTS

**Question:** What are the technical requirements for Business Intelligence & Reporting implementation?

**Answer:**
**NetSuite native capabilities with Orion enhancements** and proper configuration:

**Platform:**
- NetSuite core BI tools
- Orion-enhanced dashboard components
- SuiteQL for advanced users
- Native workbook analytics

**Dashboard Technical Requirements:**
- Role-based publishing capability
- Lock-down/prevent customization configuration
- Department-specific center creation
- KPI component integration
- Orion visual enhancements

**Saved Search Technical Requirements:**
- Inline editing enablement
- Highlighting rules configuration
- Mass update capability
- Public/private visibility controls
- Naming convention enforcement

**Export Security Technical Requirements:**
- Role-based permission configuration
- Workflow for large export notifications (>50MB suggested)
- Alert recipient configuration
- Audit logging (implied)

**Organizational Structure Technical Requirements:**
- Employee record manager assignments
- Hierarchy configuration for filter functionality
- Multi-level org structure support
- Role-based data visibility rules

**Report Configuration:**
- 400+ standard report customization
- As-of-date capability (native to NetSuite)
- Scheduled report distribution setup
- Email integration for delivery

**Performance Considerations:**
- SuiteQL query monitoring (avoid performance impact)
- Dashboard load time optimization
- Saved search result set limits (implied)

**Integration Technical Requirements:**
- SharePoint connector configuration
- Google Drive connector configuration (if used)
- Power BI live connection (if Power BI retained)
- Email system integration for scheduled reports

**Data & Security:**
- Role-based data access
- Export permission configuration
- Notification workflow development
- Audit trail (export tracking)

**User Stories:**
- As an IT Administrator, I need to configure role-based permissions so that dashboard publishing and export controls work correctly
- As a System Administrator, I need to maintain org structure so that "me and my team" filters remain functional
- As a Developer, I need to build export notification workflow so that large data exports trigger alerts

**BRD Requirements:**
- [REQUIREMENT] Configure NetSuite with Orion enhancements (ID: REQ-004, Type: Technical)
- [REQUIREMENT] Develop large export notification workflow (ID: REQ-012, Type: Technical, Custom)
- [FUNCTIONALITY] NetSuite Platform, Orion Components, SuiteQL, Workflow Engine
- [SOLUTIONDESIGN] Yes - Orion dashboard components, export notification workflow
- [CONSTRAINT] NetSuite platform capabilities and limitations
- [CONSTRAINT] All-or-nothing export permissions (cannot customize per-report)
- [PRIORITY] Must-Have: Core platform configuration, role-based permissions, org structure

**Stakeholder Impact:**
- **Primary Users**: IT/System Administrators - configuration and maintenance
- **Secondary Users**: Developers - custom workflow development
- **Approvers**: IT Leadership - technical architecture approval

**Evidence:**
- "We do spend some time on the dashboards building those out. It's actually part of the implementation, not software." - Marcus
- "You have to have the right managers assigned for those filters to work. But if we set that up, if we set it up, it actually works." - Marcus
- "For a given role there is a report export [permission]" - Marcus
- "Trigger system to alert if more than 50 megabytes of data are being downloaded." - Speaker (KBM)

**Confidence Rating**: 85% - Technical details implied from functional discussion

**Outstanding Items:**
- Detailed technical architecture documentation
- Orion component specifications
- Export notification workflow technical design
- Performance SLAs and monitoring approach
- Backup and disaster recovery for BI configurations
- Custom development scope and timeline

---

## Outstanding Items Summary

### High Priority

**1. Export Security Policy (REQ-011, REQ-012)**
- Which roles can export vs. cannot?
- Final threshold for large export notifications (50MB proposed)
- Who receives notifications?
- Audit trail retention period

**2. Official Report Definition (REQ-008, REQ-010)**
- Complete list of official reports by department
- Who authorizes official designation?
- Update process for official reports
- Version control approach

**3. Dashboard Design (REQ-003, REQ-005, REQ-006)**
- Specific KPIs for each department dashboard
- Which roles have locked vs. flexible dashboards?
- Detailed reminders portlet content by department
- Executive dashboard design

**4. Organizational Hierarchy (REQ-023)**
- Current org structure documentation
- Process for maintaining manager assignments
- Multi-level hierarchy and matrix organization handling

**5. Process Area Specific Reports (REQ-026, REQ-027)**
- Backlog 360 component specifications
- Bookings 360 component specifications
- Account Manager status report requirements
- Complete Google Sheets/Excel inventory to migrate

### Medium Priority

**6. Sales Rep Scorecards (REQ-020, REQ-021)**
- Specific metrics beyond revenue and GP
- Target-setting process
- Design mockup approval

**7. Training & Change Management**
- Training schedule and delivery approach
- Trainer identification
- Communication plan for official report philosophy
- Adoption measurement approach

**8. Integration Details**
- Current SharePoint and Google Drive usage
- Power BI strategy decision
- Live connection technical requirements

### Lower Priority

**9. SuiteQL Access (REQ-016)**
- Complete list of users requiring access
- Query review and governance process
- Training on SuiteQL syntax

**10. Technical Architecture**
- Detailed technical specifications
- Performance SLAs
- Backup and disaster recovery

### Gap Analysis

**Areas NOT Discussed:**
- Mobile BI requirements (mobile dashboards, reports?)
- Scheduled report frequency preferences
- Report retention and archival
- Disaster recovery for BI configurations
- External user access (customers, vendors?) to reports
- API access for third-party BI tools beyond Power BI

**Assumptions Made:**
- Users have appropriate NetSuite licenses for BI tools
- Network bandwidth sufficient for real-time dashboard usage
- Orion enhancements included in implementation scope
- Training will be in-person or virtual sessions (not self-paced)

---

## CONCLUSION

This comprehensive Business Intelligence & Reporting questionnaire captures:
- 27 discrete requirements (REQ-001 through REQ-027)
- Critical pain point: Multiple report versions causing trust issues ("singing from different songbooks")
- Solution strategy: Official reports, locked dashboards, real-time data, reminders portlet as daily work driver
- Major change management challenge: User resistance to loss of dashboard control and official reports only
- Key success factors: Reminders portlet, drill-down capability, manager-team alignment, as-of-date historical, aesthetic appeal
- Multiple process area coverage: Marketing/CRM, Financial, Order Management, Operations, Pre-Quote
- Security focus: Export controls and notifications to prevent data breaches
- Implementation approach: Primarily ALIGNS with NetSuite native capabilities, some ACCOMMODATE for custom dashboards and notifications

**Next Steps:**
1. Conduct follow-up sessions as identified (Export Security Policy, Official Reports Definition, Dashboard Design by Department)
2. Gather current report examples from all departments
3. Design department-specific dashboards
4. Define export security policy
5. Configure organizational hierarchy
6. Build Orion-enhanced components
7. Develop training materials
8. Execute change management plan

---

*End of Questionnaire - Business Intelligence & Reporting v1.0*


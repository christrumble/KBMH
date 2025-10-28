
# Business Intelligence & Reporting Comprehensive Follow-Up Discovery Session
## KBMH NetSuite/Orion Implementation

**Date:** October 2025  
**Session Duration:** Comprehensive single session covering all interconnected topics  
**Priority:** High - Data governance, real-time dashboards, and reporting standards critical to decision-making  
**Participants Needed:**
- Lorraine (CFO) - Primary
- Marcus (Implementation Lead) - For BI strategy alignment
- Department Heads - For dashboard requirements (Finance, Sales, Operations, Order Management, Pre-Quote)
- Kipp (IT/Technical) - For SuiteQL and technical requirements
- IT Security Lead - For export controls and data governance

---

## OVERVIEW

This comprehensive follow-up session will address critical gaps between what was discovered and what's needed for successful Business Intelligence & Reporting configuration in NetSuite/Orion. The session covers 9 interconnected topic areas covering dashboard design, report standardization, organizational hierarchy, export security, scorecard metrics, executive reporting, process area reporting, integration requirements, and change management strategy.

**Session Agenda:**
1. Dashboard Architecture & Design Strategy
2. Official Report Definition & Criteria Standardization
3. Export Security Policy & Data Governance
4. Organizational Hierarchy & Filter Configuration
5. Sales Rep & Manager Scorecards
6. Executive Financial Reporting
7. Process Area Specific Reporting Requirements
8. Integration Strategy (SharePoint, Google Drive, Power BI)
9. Training, Change Management & Adoption Strategy
10. Decisions & Next Steps

---

## PART 1: CURRENT STATE KNOWLEDGE SUMMARY

### What We Know About Your BI & Reporting Landscape

Based on comprehensive discovery sessions, we have documented a strong understanding of your reporting challenges and vision:

#### **Your Current State Pain Points**
- **Multiple Report Versions**: "Mark's version, Matt's version, Kip's version" - Same report names with different criteria causing trust issues
- **Manual Excel/Google Sheets**: Heavy reliance on manual reporting outside NetSuite, "you guys are doing a lot about a lot of reporting outside in Google sheets"
- **No Export Controls**: "Right now there's not a lot of control in Core to determine who can export what information"
- **Broken Org Hierarchy**: "Me and my team" filters don't work in Core - manager hierarchy doesn't function
- **Month-End Manual Packages**: Finance compiles static packages because executives sometimes not co-located
- **Inconsistent Dashboards**: Users customize away required views, breaking manager-team alignment
- **People Don't Trust Reporting**: "People don't trust the reporting" due to multiple versions and "singing from different songbooks"

#### **Your Vision for NetSuite/Orion BI**
- **Single Source of Truth**: "Singing from the same songbook" - official reports everyone trusts
- **Real-Time Dashboards**: Replace Excel with live NetSuite dashboards accessible 24/7
- **Daily Reminders Portlet**: "This is all the work that I have to work off of - you shouldn't have to guess"
- **Department-Specific Centers**: Finance, Sales, Pre-Quote, Order Management, Operations centers with relevant KPIs
- **Manager-Team Alignment**: Locked dashboards so weekly meetings reference identical data
- **Aesthetic Excellence**: "The home you live in all day" should look good and feel good
- **Data Security**: Export controls and notifications to prevent customer data theft
- **Executive Efficiency**: Real-time financial review without manual package compilation

#### **Current Reporting Infrastructure**
- **400+ Standard NetSuite Reports** available for customization
- **Native NetSuite Tools**: Dashboards, saved searches, workbook analytics, SuiteQL
- **Orion Enhancements**: Better visual dashboard components for modern appearance
- **Role-Based Publishing**: Manager can publish locked dashboards to teams
- **Inline Editing & Highlighting**: Saved searches with productivity features
- **Scheduled Distribution**: Automated report emailing capability
- **As-Of Date Reporting**: Historical financial snapshots available

#### **Business Objectives Addressed**
- Eliminate report version confusion and trust issues
- Move reporting from manual Excel to real-time NetSuite
- Provide daily clarity on work priorities (reminders portlet)
- Enable real-time executive decision-making
- Improve data security and audit trail
- Establish consistent KPI interpretation across organization
- Create department-specific visibility and accountability

#### **Key Stakeholders & Their Needs**
- **Lorraine (CFO)**: Real-time financial dashboards, executive presentation capability, manager hierarchy working
- **Wendy**: Sales rep scorecards, team performance visibility, "me and my team" filters
- **Department Heads**: Official report designation authority, dashboard customization control
- **All Employees**: Daily reminders portlet, real-time data, role-appropriate views
- **IT Security**: Export permissions, large data export notifications, audit trails

---

## PART 2: COMPREHENSIVE DISCUSSION TOPICS

### TOPIC 1: DASHBOARD ARCHITECTURE & DESIGN STRATEGY

**Context:** NetSuite supports both home dashboard (customizable by user) and role-center dashboards (can be locked). Need to design overall dashboard strategy: how many centers, which roles lock vs. customize, what components on each, Orion visual enhancements.

**What We Know:**
- 7 proposed dashboard centers: Finance, Sales, Pre-Quote, Order Management, Operations, Home (personal), Executive
- Role-based publishing with lock-down capability possible
- Reminders portlet is critical daily work driver
- Orion-enhanced components improve aesthetics
- "Me only" and "Me and my team" filters needed throughout
- Users should not customize locked team dashboards
- Visual appearance matters ("home you live in all day")

**Discussion Points:**

1. **Dashboard Center Structure**
   - How many centers does KBM want? (Currently proposed: 7 centers)
   - Should each role center be accessible to all or restricted?
   - Home tab: Personal dashboard? Or just Orion default?
   - Executive dashboard requirements? (Lorraine/Mark specific?)
   - Should there be a "public" dashboard all employees see?

2. **Role-Based Publishing & Lock-Down Strategy**
   - Which roles should have locked team dashboards?
   - Which roles should allow personal customization?
   - Sales team: Should all reps see identical pipeline dashboard? (Yes)
   - Finance team: Should finance staff see identical financial dashboard? (Yes)
   - PMs: Should all PMs see identical PM dashboard? (Verify)
   - How to enforce lock-down? (Technical capability confirmation needed)

3. **Reminders Portlet Content by Department**
   - **Finance**: Bills to pay, bills on hold, period close checklist items, bank reconciliation tasks
   - **Sales/CRM**: Opportunities needing follow-up, phone calls to make, pending approvals, pipeline reviews
   - **Order Management**: Acknowledgements to review, backlog items needing attention, customer PO tracking alerts
   - **Operations**: PM workload assignments, work order approvals, punch items due
   - **Pre-Quote**: RFPs requiring response, resource allocation decisions
   - Individual vs. departmental reminders: What's needed?

4. **KPI Components on Each Dashboard**
   - **Finance Dashboard**: Bank balance, monthly revenue, expenses, profit, current vs. prior period, trial balance link
   - **Sales Dashboard**: Pipeline value, forecast, closed-won YTD, conversion rates, top opportunities
   - **Order Management Dashboard**: Backlog amount, bookings YTD, acknowledgement count, customer PO utilization
   - **Operations Dashboard**: PM workload, resource utilization, project status distribution
   - **Pre-Quote Dashboard**: RFPs in progress, average quote time, win/loss rate
   - How should KPIs be prioritized?

5. **Orion Component Enhancements**
   - What visual improvements does Orion provide beyond standard NetSuite?
   - Color schemes? Logo placement? Modern design elements?
   - Should Orion components be used across all dashboards or specific areas?
   - Executive dashboard: Should it get special Orion treatment?

6. **Drill-Down & Interactivity**
   - From KPI to detail report: What drill paths should exist?
   - Click-through should take users where? (To full report or transaction level?)
   - Filter stacking: Should multiple filters work together on dashboards?
   - Real-time updates: How often should dashboards refresh?

7. **Executive Dashboard Specific Requirements**
   - Lorraine's requested feature: "Can they present from Orion instead of exporting to Excel?"
   - What should Lorraine's personal dashboard show? (Financial snapshot?)
   - Mark's dashboard: Separate or similar to Lorraine's?
   - Should executive dashboard be accessible from anywhere?

---

### TOPIC 2: OFFICIAL REPORT DEFINITION & CRITERIA STANDARDIZATION

**Context:** "Singing from the same songbook" is critical to solving the trust issue. Need to identify all official reports, document exact criteria (taxes included? discounts? net vs. gross?), establish naming convention, control who can modify.

**What We Know:**
- GSI/Orion prefix for official reports planned
- Public/private saved search controls available
- Current problem: "Mark's version, Matt's version, Kip's version" with different results
- Revenue can be calculated 4-5 different ways depending on inclusions
- Users need standardized interpretation guidelines
- Version control process needed

**Discussion Points:**

1. **Complete Official Report Inventory**
   - **Financial Reports**: Which ones are "official"?
     - Income statement (monthly)
     - Balance sheet (period-end)
     - Trial balance
     - Cash flow
     - AR aging
     - AP aging
     - Receive not invoiced
     - Receive not scheduled
     - Others?
   - **Sales Reports**:
     - Pipeline report
     - Booking report
     - Forecast accuracy
     - Sales rep performance
     - Conversion analysis
     - Others?
   - **Order Management Reports**:
     - Backlog 360
     - Bookings 360
     - Account manager status reports
     - Customer PO utilization
     - Others?
   - **Operations Reports**:
     - PM workload
     - Resource utilization
     - Project status
     - VRA tracking
     - Others?
   - **Pre-Quote Reports**:
     - RFP tracking
     - Quote pipeline
     - Win/loss analysis
     - Others?

2. **Criteria Standardization for Each Report**
   - **Revenue Report**: Does it include taxes, discounts, or not? Net or gross?
   - **GP Report**: Calculated how? What cost inclusions/exclusions?
   - **Aging Reports**: What date used for aging? How are hold statuses treated?
   - **Backlog**: Only unfulfilled? Exclude cancelled? Include pending?
   - **Bookings**: What constitutes a booking? (SO created? Invoice sent? Cash received?)
   - **Pipeline**: What opportunity stages included? (Prospects? Qualified leads? Active quotes?)
   - Document exact formula/calculation for each

3. **Naming Convention Standards**
   - Prefix: GSI/Orion/ for all official reports?
   - Department prefix: Sales/, Finance/, Operations/ etc.?
   - Date range indicator? Or assume current/YTD?
   - Examples: "GSI/Finance/Income_Statement_Monthly" or simpler?
   - How to distinguish "official" from user personal searches?

4. **Governance & Update Process**
   - Who authorizes official report changes? (Department heads? Lorraine?)
   - What triggers a report update? (Business rule change? Regulatory requirement?)
   - Version control: How to track old versions?
   - User notification: How are users informed of changes?
   - Legacy versions: Can users still access old versions or deprecate?

5. **Criteria Documentation Requirements**
   - For each official report, document:
     - Exact filters and criteria
     - Calculation methods
     - Include/exclude rules
     - How to interpret results
     - When to use this report vs. another similar report
   - Who writes this documentation? (Department heads? Marcus/GSI?)
   - Format? (Wiki? PDF guide? In-system help text?)
   - Accessibility to all users?

6. **Training on Official Reports**
   - When should training occur? (Before go-live? After?)
   - Who trains users? (Department heads? Dedicated trainer?)
   - How are new employees trained on official reports?
   - What happens if someone creates personal version of official report?
   - How to enforce "use official reports only" philosophy?

7. **Special Cases & Exceptions**
   - Can executives create personal versions? (For their own analysis?)
   - Can power users create personal searches if private?
   - Are there any reports that should NOT be in official suite?
   - How to handle "one-time" reporting requests?

---

### TOPIC 3: EXPORT SECURITY POLICY & DATA GOVERNANCE

**Context:** Data breach risk identified as high priority. Current Core has no export controls. NetSuite can restrict export by role but not by report (all-or-nothing). Need clear policy on who can export, thresholds for large export notifications, audit trail requirements.

**What We Know:**
- Current vulnerability: Sales employee could export entire customer list
- NetSuite limitation: Export permissions are per-role, not per-report
- Workaround exists: Users can copy-paste from browser
- Proposal: Large export notifications (>50MB suggested threshold)
- 48 states with nexus = large customer database
- Bank requesting data visibility
- Need audit trail of exports

**Discussion Points:**

1. **Role-Based Export Permission Matrix**
   - **Sales roles**: Can export order details? (Yes) Customer lists? (No)
   - **Finance roles**: Can export all financial data? (Yes)
   - **Operations roles**: Can export time/resource data? (Yes)
   - **Pre-Quote roles**: Can export proposal data? (Probably)
   - **Executive roles**: Can export all data? (Probably yes)
   - **External contractors**: Should they be able to export? (Probably no)
   - IT Security: Can export all data? (Yes, for administration)
   - New employees: Default export capability? (No, restrict first 90 days?)

2. **Large Export Notification Threshold**
   - 50MB proposed - is this right? Too high? Too low?
   - What types of exports would exceed threshold?
     - Entire customer database? (Could easily exceed 50MB)
     - Full financial history?
     - All project data for year?
   - Should threshold vary by user role?
   - Should threshold vary by report/data type?

3. **Large Export Notification Recipients**
   - IT Security team? (Primary recipient for investigation)
   - Department head? (For context on why export occurred)
   - Executive team? (Awareness only)
   - CFO/Lorraine? (For sensitive financial data?)
   - Should notification include: User name, data volume, data type, timestamp, destination?

4. **Audit Trail Requirements**
   - What to log for each export?
     - User ID
     - Date/time
     - Data type/report name
     - Volume of data
     - File format (Excel, PDF, CSV)
     - Destination (if trackable)
   - Retention period? (1 year? 3 years? Forever?)
   - Who has access to audit logs? (IT Security? Executives? Internal audit?)
   - Regular audit report? (Monthly? Quarterly?)

5. **Special Cases & Exceptions**
   - Legitimate large exports: How to approve/document?
   - Recurring reports: Should large export notification only trigger first time?
   - Scheduled report distribution: Does it count as "export"?
   - Archive exports: Should they be treated differently?
   - Customer/vendor requests: How to handle?

6. **Data Security During Export**
   - Encryption in transit?
   - Password protection on downloaded files?
   - Can users export to personal cloud (OneDrive, Google Drive)?
   - Export file cleanup/deletion requirement?
   - Mobile device policy for exported data?

7. **Audit & Compliance**
   - Bank requirements: What data access/export documentation needed?
   - Regulatory compliance: Any industry requirements?
   - Internal audit: What reports needed?
   - Breach response: What happens if unauthorized export detected?
   - Contractual obligations: Customer agreements about data security?

---

### TOPIC 4: ORGANIZATIONAL HIERARCHY & FILTER CONFIGURATION

**Context:** Core failed with "me and my team" filters. NetSuite can work if org structure configured correctly. This is foundation for scorecards, manager views, and accurate reporting. Must be maintained in HR system.

**What We Know:**
- Core frustration: Filters "don't work" - "I've never gotten that"
- NetSuite requirement: Proper manager assignments needed
- Current opportunity: "You have to have the right managers assigned... if we set it up, it actually works"
- Filter types needed: "Me only," "Me and my team," role-based, department-based
- Scope: All employees must have accurate reporting relationships

**Discussion Points:**

1. **Current Organizational Structure**
   - Can someone provide org chart? (Current as of today?)
   - Who reports to whom? (All direct reports to each manager?)
   - Any matrix organizational relationships? (Dotted-line reporting?)
   - Multiple managers for anyone? (Project-based reporting?)
   - Skip-level relationships? (Should VP see CEO direct reports? Or only direct reports?)

2. **Manager Hierarchy Configuration**
   - Employee record: Who is listed as manager?
   - Process: Who maintains manager relationships? (HR? IT Admin?)
   - Change management: When employee changes roles, who updates?
   - Frequency: How often do manager relationships change?
   - Accuracy: Current state - what % of employee records have correct managers?

3. **Filter Type Requirements**
   - **"Me Only"**: Individual sees only their own data
     - Sales rep sees only their opportunities
     - Designer sees only their time entries
     - PM sees only their work orders
   - **"Me and My Team"**: Manager sees direct reports
     - Sales manager sees team opportunities
     - Finance manager sees team activities
     - Operations manager sees PM workloads
   - **"Me, My Team, and My Manager"**: Skip-level visibility? (Needed?)
   - **"My Department"**: All members of specific department?
   - **"My Role"**: All users with same role? (Sales reps to sales reps?)

4. **Filter Application Across System**
   - Dashboards: Which dashboards should have "me/team" filters?
   - Scorecards: Sales rep scorecard defaults to "me only," manager scorecard shows team?
   - Reports: Can filters be applied to saved searches? (Drill-down capability?)
   - Workbook Analytics: "Me and my team" filters on pivot tables?
   - Reminders Portlet: Should reminders be filtered by person/department?

5. **Multi-Level Hierarchy**
   - Sample organization:
     - CEO
       - VP Finance (Lorraine)
         - Finance Manager
           - Finance Clerks
       - VP Operations (Matt)
         - PM Manager (Wendy)
           - PMs
         - Operations Manager
           - Receiving team
       - VP Sales
         - Sales Manager
           - Sales Reps
       - Pre-Quote Lead (Kimmy)
         - Account Managers
   - How many levels? (Is this depth correct?)
   - Should CEO see all employees? (Or just direct reports?)

6. **Department Assignment**
   - Should each employee be assigned to a department? (Finance, Sales, Operations, etc.)
   - How to handle cross-functional roles? (Kipp = IT, but works across all departments)
   - Should department be separate from manager hierarchy? (Yes, usually)
   - Department used for filtering? (Departmental reminders, reports)

7. **Contractor & Vendor Relationships**
   - Should contractors appear in org hierarchy? (Probably not)
   - Can contractors access dashboards/reports? (Through vendor center separately)
   - Impact of contractors on "me and my team" filters? (None - they're external)

---

### TOPIC 5: SALES REP & MANAGER SCORECARDS

**Context:** Wendy requested: "I would love them to see that on their own dashboard. And then if he was ever managing them on their dashboard, it shows them all of their people." Scorecards replace manual booking report distribution with real-time dashboard visibility.

**What We Know:**
- Current: Booking report in "Director's tab in shared folder"
- Shows YTD performance and GP by sales rep
- Wendy wants rep to see personal scorecard on dashboard
- Manager to see all team members' scorecards
- Based on "org structure with me and my team filters"
- Visual layout not yet designed

**Discussion Points:**

1. **Sales Rep Scorecard Metrics**
   - What metrics should appear on scorecard?
     - Total Revenue (YTD)?
     - Total Gross Profit (YTD)?
     - GP Margin %?
     - Number of projects?
     - Win rate?
     - Pipeline value?
     - Forecast accuracy?
     - Commission earned?
   - Should it compare actual vs. target? (If targets exist)
   - How to handle new reps without prior year comparison?
   - Should scorecard show monthly detail or just YTD total?

2. **Scorecard Visual Layout**
   - Large KPI tiles at top? (Revenue, GP, Margin%)
   - Trending chart below? (Month-by-month bars or line?)
   - Comparison to team average? (This rep vs. other reps)
   - Comparison to company average?
   - Comparison to prior year same period?
   - Ranking: Where does this rep rank among team?
   - Goals/targets: Visual progress bars?

3. **Manager Scorecard Requirements**
   - **Single View of All Team Members**: Card per team member or table view?
   - Metrics: Same as individual scorecard or summarized?
   - Sorting options: By name? By revenue? By GP? By margin?
   - Filtering: Show all team members or filtered view?
   - Drill-down: Click team member card to see details?
   - Team totals: Summary row at bottom?

4. **Data Update Frequency**
   - How often should scorecards update?
     - Real-time? (Every transaction)
     - Daily? (Overnight refresh)
     - Weekly? (Every Monday morning)
     - Monthly? (Monthly close complete)
   - Should there be a "last updated" timestamp?
   - If GL close happens mid-month, which period shows?

5. **Scorecard Distribution & Notifications**
   - Dashboard access: Always available or sent as report?
   - Email notification: "Your monthly scorecard is ready"?
   - Frequency: When sent? (End of month? First of month?)
   - Recipients: All reps get their scorecard automatically?
   - Managers: Auto-receive team scorecard?
   - Executive: Should Wendy/VP get summary scorecard? (All teams?)

6. **Special Cases & Exceptions**
   - New sales reps: When does scorecard start showing? (First transaction? After 30 days?)
   - Departing reps: Do they still appear on manager scorecard? (Yes, until when?)
   - Transferred reps: What happens to prior history? (Stays with old manager? Transfer history?)
   - Sales managers: Do they get their own "manager" scorecard showing their personal sales?
   - Temporary assignments: How to handle?

7. **Target Setting & Goals**
   - Should scorecards show sales targets/goals?
   - Who sets targets? (Sales leadership? Individual negotiation?)
   - How are targets managed? (Annual? Quarterly? Rolling?)
   - Variance reporting: Actual vs. target with % variance?
   - Bonus impact: Does scorecard factor into commission/bonus calculations?

8. **Other Department Scorecards**
   - Should operations have PM scorecards? (PM workload, project count, utilization?)
   - Should finance have department scorecards? (Month-end completion, days to close?)
   - Should pre-quote have account manager scorecards? (Quote win rate, average quote time?)
   - Should each department have similar structure?

---

### TOPIC 6: EXECUTIVE FINANCIAL REPORTING

**Context:** Lorraine's question: "Do they have to export all of that into Excel or are they able to do the presentation through Orion?" Goal is real-time presentation capability for financial reviews, with scheduled report distribution when executives not co-located.

**What We Know:**
- Current problem: Manual month-end package compilation
- Executive not always co-located for live review
- Finance sends static package via email when needed
- Marcus example: "Pull up income statement, balance sheet, trial balance, walk through it, drill down to figure out"
- Need drill-down capability: "Why is AR past 90 days? Click AR report, find invoice, task sales rep"
- Scheduled reports needed for asynchronous review

**Discussion Points:**

1. **Real-Time Presentation Capability**
   - Who presents? (Finance lead? Lorraine herself?)
   - Frequency: Weekly? Monthly? As-needed?
   - Duration: How long does presentation typically take? (30 min? 1 hour?)
   - Screen sharing: Can presenter share real-time dashboard with others in same room?
   - Remote presentation: Will executives join via Zoom/Teams? (Needs secure access)

2. **Executive Dashboard Design**
   - What's on Lorraine's personal dashboard?
     - Bank balance (how often updated?)
     - Current month revenue/expenses/profit
     - Current month vs. prior month comparison
     - YTD vs. last year YTD
     - Trial balance link
     - Key alerts/variances
   - What's on executive review dashboard (for all executives)?
     - Same as above but company-wide?
     - Multiple executive users? (Lorraine, Mark, others?)
   - Should dashboards be customizable or locked?

3. **Drill-Down Workflow During Presentation**
   - From KPI: Click to drill to related report
   - From report summary: Click to detail transactions
   - Example workflow: "Bank balance $X" → "Why is it $X instead of $Y?" → Click to ledger detail → Find variance
   - How many levels of drill-down needed? (2 levels? 3 levels? More?)
   - Should drill-down preserve filters/parameters?

4. **Financial Report Suite**
   - Which reports always needed for executive review?
     - Income statement (current month, YTD, prior year comparison)
     - Balance sheet (current period, prior period)
     - Trial balance (current period, prior period)
     - Cash flow (current month, YTD, prior year)
     - AR aging (over 30, 60, 90 days)
   - Other reports sometimes needed? (Bank reconciliation? GL detail? Variance analysis?)
   - How to customize date ranges during presentation?

5. **Scheduled Report Distribution**
   - When should reports be generated/sent?
     - Day after month-end close? (Automatic? Manual trigger?)
     - What time of day? (Morning so executives have it for meetings?)
   - Who receives reports? (Lorraine, Mark, Board if applicable?)
   - Format: Excel? PDF? Both?
   - Contents: Which reports included in package?
   - Folder/structure: How is multi-report package organized?

6. **Executive Access & Security**
   - Who has access to executive dashboards? (All executives? Just CFO?)
   - Can executives see other divisions/subsidiary info if applicable? (Whole company? Just their area?)
   - Export capability: Can executives export reports for board meetings?
   - Mobile access: Can executives view dashboards on tablet/phone while traveling?
   - Data currency: Is cached data okay or must it be current?

7. **Monthly Close Timeline**
   - When close completes: "Books are closed"
   - When can finance run executive reports? (Immediately? Next day?)
   - When does financial dashboard update? (Same time reports available?)
   - Scheduled reports: When should they send? (Morning after close complete?)
   - If close delayed, how does that impact reporting?

---

### TOPIC 7: PROCESS AREA SPECIFIC REPORTING REQUIREMENTS

**Context:** Different departments have different reporting needs. Finance needs AR aging, Order Management needs backlog 360, Sales needs pipeline, Operations needs PM workload. Each needs tailored dashboards and reports.

**What We Know:**
- 400+ standard NetSuite reports available to customize
- Need Backlog 360 and Bookings 360 comprehensive dashboards
- "Account manager status reports exist in production" but need detailed requirements
- Operations uses Google Sheets for reporting - need to migrate
- Finance doing "a lot about a lot of reporting outside in Google sheets"
- Backlog 360: "everything you could ever imagine for backlog in one place"

**Discussion Points:**

1. **Financial Management Reporting**
   - **Month-End Close**:
     - Income statement variations needed? (By department? By project type?)
     - Balance sheet: Need detail drilling? (To GL accounts? To transactions?)
     - Trial balance: Used for what? (Reconciliation? Reporting?)
     - Check for close completeness: "Period close checklist" - what items tracked?
     - Bank reconciliation: How tracked? (In system? Separately?)
   - **AR/AP Reporting**:
     - AR aging: How many buckets? (30, 60, 90+? Or more granular?)
     - AR detail: By customer? By invoice? Both?
     - AP aging: Similar structure?
     - Unapplied credits tracking?
   - **Google Sheets Migration**:
     - What Google Sheets reports currently used?
     - Which are most critical to replace first?
     - Which are one-time reports vs. recurring?
     - Any calculation/formula complexity that's hard to replicate?

2. **Sales & CRM Reporting**
   - **Pipeline Reports**:
     - What stages should appear? (Prospect, Lead, Qualified, Proposal, Won, Lost?)
     - By sales rep? By team? By territory?
     - By product type? By customer type?
     - Probability weighting? (50% of opportunities weighted in forecast)
     - Expected close date accuracy?
   - **Booking Report**:
     - What constitutes "booking"? (Firm order? Proposal accepted? Signed agreement?)
     - YTD bookings tracking?
     - Forecast accuracy: Bookings vs. forecast?
   - **Sales Rep Performance**:
     - Revenue production?
     - Margin/GP production?
     - Number of projects?
     - Win rate?

3. **Order Management Reporting**
   - **Backlog 360** (comprehensive dashboard):
     - By line item (revenue $, GP $, GM %, status)
     - By order (total revenue, total GP, order status)
     - Filter by product type? By customer? By timeline?
     - Aging: How old is backlog? (Less than 30 days, 30-60, 60-90, 90+?)
     - Critical backlog: Over budget? Over timeline? Over spec?
   - **Bookings 360**:
     - Similar structure to Backlog 360?
     - Or different layout/metrics?
   - **Acknowledgement Tracking**:
     - How many pending? (Unreviewed?)
     - How many past due? (Expected review date passed?)
     - Review status: % complete vs. total?
   - **Customer PO Tracking**:
     - Total PO amount vs. utilization?
     - % of PO used?
     - Remaining balance?
     - At-risk POs (approaching limit)?
   - **Account Manager Status Reports**:
     - What information do account managers need?
     - Current use: How critical to daily workflow?
     - Format/content: What should be included?

4. **Operations Reporting**
   - **PM Workload Management**:
     - PM assignments: Who's assigned to what?
     - Current utilization: How busy is each PM?
     - Capacity: Who has room for more projects?
     - Timeline: When are milestones due?
     - Resource visualizer: Wendy's Google Sheet calendar - should NetSuite replace it?
   - **Project Status**:
     - By phase (planning, design, approval, delivery, installation, post-install)?
     - At-risk projects: Over budget? Behind schedule? Quality issues?
     - VRA tracking: Open VRAs? Expected credits?
     - Punch list status: Open items? Aging?
   - **Time Tracking**:
     - Time to invoice lag: How long after work before billed?
     - PM hours by project: Actual cost vs. estimated?
     - Design hours by project: Cost variance?

5. **Pre-Quote Reporting**
   - **RFP Pipeline**:
     - Active RFPs: How many? By account manager? By size?
     - Quote timeline: How long does typical quote take?
     - RFP by stage: Received, in-progress, submitted, won, lost?
     - Account manager workload: How many RFPs in flight?
   - **Quote Accuracy**:
     - Quote to actual margin variance: How accurate are quotes?
     - Scope creep tracking: Change orders as % of original quote?

6. **Cross-Functional Reporting**
   - What reports need data from multiple areas?
     - Project profitability: Quote → Acknowledgement → Backlog → Actual costs → Final project GP
     - Revenue recognition: Quote date → Acknowledgement → Invoice → AR aging
     - Resource allocation: Pre-quote hours → Design hours → PM hours → Installation hours
   - Should these be combined in dashboards or separate reports?

---

### TOPIC 8: INTEGRATION STRATEGY

**Context:** SharePoint and Google Drive integration mentioned but not detailed. Power BI optional if live connection used. Strategy needed: How to keep reporting in NetSuite, use integrations only for document management and optional aged analysis.

**What We Know:**
- SharePoint integration mentioned but not detailed
- Google Drive integration needs validation
- Power BI optional: "If you love Power BI, use it, just keep in mind that the data is aged once it's out"
- Live connection recommended if Power BI used
- Goal: Keep reporting inside NetSuite for real-time data
- Scheduled report distribution: Email integration for automatic delivery

**Discussion Points:**

1. **SharePoint Integration**
   - Current usage: How is SharePoint used today?
   - Content stored: What documents in SharePoint?
   - Integration goal: Should users access SharePoint from NetSuite? (Link integration?)
   - Document management: Where should new reports be stored? (SharePoint or NetSuite document library?)
   - Access patterns: How often do users reference SharePoint documents?
   - Discovery/search: Should SharePoint docs be searchable from NetSuite?

2. **Google Drive Integration**
   - Current usage: Google Drive heavily used for reporting and file storage
   - Sheets inventory: Which Google Sheets contain critical data?
     - Wendy's PM workload calendar?
     - Finance reporting sheets?
     - Sales tracking sheets?
     - Others?
   - Migration plan: Should we move these to NetSuite or keep in Google Drive?
   - Integration: Access from NetSuite? Or keep separate?
   - Authentication: How to handle Google Drive access credentials?

3. **Power BI Strategy Decision**
   - Current usage: Is anyone using Power BI today?
   - Future plan: Should Power BI be part of solution? (Or use NetSuite only?)
   - If Power BI retained:
     - Live connection required? (To avoid aged data)
     - Technical feasibility: Can NetSuite and Power BI live connect?
     - Cost: Licensing considerations?
     - Support: Who maintains Power BI models/reports?
   - If Power BI abandoned:
     - Workbook analytics replaces pivot table needs?
     - SuiteQL replaces advanced query needs?
     - Training needed for users to shift tools?

4. **Email Integration (Scheduled Reports)**
   - Standard capability: NetSuite can email scheduled reports
   - Configuration: Which reports should auto-send?
   - Distribution lists: Who receives each report?
   - Timing: What time of day should reports send?
   - Format: Excel, PDF, or both?
   - Frequency: Daily, weekly, monthly?

5. **Data Integration from External Systems**
   - Paylocity: Time tracking via journal entry import (already planned)
   - ServiceNet: Miller Knoll pricing integration (Order Management)
   - ServiceTime: Intermarket orders (Order Management)
   - Others: Any other systems that feed BI data?
   - Report impact: How do these integrations affect reporting?

6. **Audit Trail & Compliance Integrations**
   - Export audit logs: Should they integrate with compliance system?
   - Data governance: Are there external compliance requirements?
   - Bank reporting: Format/structure requirements for bank data requests?
   - Legal hold: Any e-discovery or legal hold requirements?

---

### TOPIC 9: TRAINING, CHANGE MANAGEMENT & ADOPTION STRATEGY

**Context:** Significant behavior change required. Users accustomed to creating own reports must use official reports. Loss of dashboard customization control. "You're not doing that" enforcement needed. Daily reminders portlet requires habit change.

**What We Know:**
- Marcus quote: "'I changed my dashboard.' I'm like, 'No, you're not doing that.'" - Enforcement needed
- Philosophy: "Singing from the same songbook" - must be understood and embraced
- Adoption risk: Users may continue creating personal reports despite training
- Reminders portlet: New daily workflow requires behavior change
- Dashboard discipline: Users resist locked dashboards initially
- Productivity gains: Inline editing, drill-down, no export/copy needed

**Discussion Points:**

1. **Change Management Strategy**
   - **Philosophy Communication**: "Singing from the same songbook" - what does this mean?
     - Everyone uses same criteria, same calculations, same interpretation
     - Eliminates trust issues and conflicting numbers
     - Enables confident decision-making
   - **Rollout approach**: Big bang or phased? (All dashboards live or department by department?)
   - **Soft launch**: Parallel run period where old reports still available?
   - **Cutover date**: When do old reports go away?

2. **Training Schedule & Delivery**
   - Timeline: When relative to go-live?
     - Pre-go-live: 1 week before? 2 weeks?
     - Go-live week: Training during implementation week?
     - Post-go-live: Ongoing support period?
   - Format: In-person? Virtual? Self-paced? Hybrid?
   - Duration: 1-hour sessions? Half-day? Full-day training?
   - Who trains: GSI team? KBM subject matter experts? Both?
   - Train-the-trainer: Should KBM staff become trainers for ongoing training?

3. **Training Content by Audience**
   - **Executive/Leadership training** (Lorraine, Mark, Matt):
     - Dashboard access and navigation
     - Real-time reporting capability
     - Drill-down techniques
     - Scheduled report distribution setup
   - **Finance team training** (month-end close, reporting):
     - Financial dashboard navigation
     - Standard report suite (income statement, balance sheet, trial balance, AR aging)
     - Reminders portlet for period close tasks
     - Report interpretation guidelines
   - **Sales/CRM team training**:
     - Pipeline dashboard
     - Sales rep scorecard (personal)
     - Manager scorecard (if manager)
     - Opportunity status inline editing
     - "Me and my team" filters
   - **Order Management team training**:
     - Backlog 360 dashboard
     - Bookings 360 dashboard
     - Account manager status reports
     - Customer PO tracking
   - **Operations team training**:
     - PM workload dashboard
     - Resource visualizer (when ready)
     - Project status reporting
     - VRA tracking
   - **All employees training**:
     - Reminders portlet overview (critical)
     - How to find reports
     - When to use which report
     - Who to contact for questions
     - What to do if they need a "new" report

4. **Key Messaging & Philosophy**
   - **"Single Source of Truth"**: Why it matters
   - **"Singing from the Same Songbook"**: Everyone reads same music
   - **"Real-Time Data"**: Stop using static Excel snapshots
   - **"No More Guessing"**: Reminders portlet tells you what to do
   - **"Productivity Gains"**: Inline editing saves time, drill-down saves back-and-forth
   - **"Locked Dashboards"**: It's not restricting you, it's aligning the team

5. **Resistance Management**
   - **"I like my own version"**: Address loss of control
     - Explain: Lock-down is for team dashboards, not your personal Home tab
     - Benefit: Weekly meetings are more productive when everyone sees same data
     - Training: Show time savings from aligned meetings
   - **"I need a different report"**: Address "official reports only"
     - Process: Submit request to department head for evaluation
     - Official report creation: If request has merit, becomes official for all
     - Personal searches: Can create private searches for personal exploration (don't name them "revenue")
   - **"The system doesn't show what I need"**: Address Excel users
     - Transition plan: Gradual move from Excel to NetSuite
     - Workbook analytics: Covers most Excel pivot table needs
     - SuiteQL: For power users who really need custom queries
   - **"I don't trust the numbers"**: Address reporting trust issues
     - Transparency: Document all official report criteria
     - Accountability: Who authorized this official report?
     - Testing: Run side-by-side with old reports to validate

6. **User Support Model Post-Go-Live**
   - Help desk: Who handles "I can't find the dashboard" questions?
   - Report changes: Who approves changes to official reports?
   - New report requests: How to handle?
   - Feedback/complaints: Where do they go?
   - SLA: How quickly should questions be answered? (Same day? Next business day?)
   - Escalation: When do issues go to department heads vs. IT?

7. **Success Measurement**
   - What indicates successful adoption?
     - Dashboard access frequency (are people using it?)
     - Personal report creation (are people creating personal versions despite training?)
     - User satisfaction (survey at 90 days post-go-live?)
     - Report accuracy (fewer conflicts about numbers?)
     - Decision-making speed (meetings faster because aligned on data?)
   - Metrics to track:
     - Dashboard usage by department
     - Official report vs. personal report usage
     - Export volume and trends
     - Time to answer business questions
     - Financial close timeline (should improve if reporting complete)

---

## PART 3: OUTSTANDING DECISIONS REQUIRED

The following strategic decisions are pending and need to be made during this session to proceed with configuration:

### DECISION 1: Dashboard Architecture & Component Strategy
**Decision Maker:** Lorraine (CFO) with Department Heads  
**Impact:** High - Affects user adoption and decision-making effectiveness  
**Status:** Design session required

**Options:**
1. **Minimalist Approach**: 3-4 key dashboards (Finance, Sales, Operations, Home)
2. **Comprehensive Approach**: 7+ dashboards (Finance, Sales, Pre-Quote, Order Mgmt, Operations, Executive, Home)
3. **Hybrid Approach**: Core dashboards for all, plus optional specialty dashboards

---

### DECISION 2: Export Security Policy
**Decision Maker:** IT Security Lead with Executive Team  
**Impact:** High - Critical for data protection  
**Status:** Policy needs to be defined

**Options:**
1. **Restrictive**: Only certain roles can export; large export notifications at 25MB
2. **Balanced**: Most roles can export; large export notifications at 50MB
3. **Permissive**: All roles can export; notifications at 100MB

---

### DECISION 3: Official Report Inventory & Criteria Documentation
**Decision Maker:** Department Heads with Finance Lead  
**Impact:** High - Foundation for "singing from same songbook"  
**Status:** Complete inventory and criteria needed

**Questions:**
- Which reports are truly "official"? (Every standard report or just key ones?)
- Who maintains documentation? (Department heads? Marcus/GSI?)
- How detailed should documentation be? (One-page? Full specification?)

---

### DECISION 4: Organizational Hierarchy Accuracy
**Decision Maker:** HR with IT Admin  
**Impact:** Critical - If org structure wrong, "me and my team" filters fail  
**Status:** Current state assessment needed

**Questions:**
- Is current org hierarchy accurate in system? (% accuracy?)
- Who maintains manager relationships? (HR process?)
- How frequently do relationships change?
- Are there any matrix relationships to handle?

---

### DECISION 5: Power BI Future State
**Decision Maker:** Executive Team  
**Impact:** Medium - Affects BI platform strategy  
**Status:** Strategic decision needed

**Options:**
1. **NetSuite Only**: Use NetSuite native tools; retire Power BI
2. **Power BI Live Connection**: Integrate Power BI with live NetSuite connection
3. **Dual Platform**: Some reports in NetSuite, some in Power BI (maintain both)

---

## PART 4: PRE-WORK & PREPARATION

To make the most of this comprehensive session, please prepare the following:

### Dashboard Architecture Topic:
- [ ] Confirm which departments/centers are needed
- [ ] Confirm who should have dashboard access (all employees? Role-specific?)
- [ ] Confirm whether dashboards should be locked or customizable per role
- [ ] Identify current Orion component capabilities
- [ ] Determine if separate Executive dashboard needed

### Official Reports Topic:
- [ ] Inventory all current reports (Excel, Google Sheets, Core reports in use)
- [ ] Identify which reports are most critical
- [ ] For each critical report: Document exact criteria and calculation method
- [ ] Identify conflicts between "versions" of same report
- [ ] List who should be "official report approvers" by department

### Export Security Topic:
- [ ] List all user roles and current export needs
- [ ] Identify which data is most sensitive (customer lists? Financial data?)
- [ ] Propose large export notification threshold
- [ ] Determine if special cases/exceptions needed
- [ ] Confirm audit trail requirements

### Organizational Hierarchy Topic:
- [ ] Provide current org chart
- [ ] Identify any inaccuracies in current manager relationships
- [ ] Confirm manager hierarchy maintenance process (HR responsibility?)
- [ ] List any special cases (matrix organizations, contractors, etc.)

### Scorecard Topic:
- [ ] Provide sample current Booking Report (format, metrics)
- [ ] Identify other scorecards needed (Operations? Pre-Quote? Finance?)
- [ ] Specify targets/goals if applicable
- [ ] Confirm update frequency preference

### Executive Reporting Topic:
- [ ] Confirm monthly financial review process
- [ ] Identify who should have access to executive dashboards
- [ ] Confirm scheduled report distribution needs
- [ ] Provide sample current month-end package

### Process Area Reporting Topic:
- [ ] Finance: Provide inventory of current Excel/Google Sheets reporting
- [ ] Sales: Define what metrics matter most
- [ ] Order Management: Define Backlog 360 and Bookings 360 requirements
- [ ] Operations: Specify PM workload visibility needs
- [ ] Pre-Quote: Define RFP and quote tracking needs

### Integration Topic:
- [ ] Current usage of SharePoint, Google Drive, Power BI
- [ ] Integration goals for each platform
- [ ] Decision: Power BI future (keep? retire? live connection?)

### Training Topic:
- [ ] Identify internal trainers (KBM staff who will help train)
- [ ] Confirm training approach (in-person, virtual, hybrid)
- [ ] Identify any users who will need extended support
- [ ] Confirm timeline for training relative to go-live

---

## PART 5: SESSION DELIVERABLES & SUCCESS CRITERIA

At the completion of this comprehensive follow-up session, we will have:

### Documentation Deliverables:
1. **Dashboard Architecture Document** - Dashboard centers, roles, lock-down strategy, component list
2. **Official Report Definition Document** - All official reports with exact criteria and documentation
3. **Export Security Policy** - Role permissions matrix, notification thresholds, audit trail requirements
4. **Organizational Hierarchy Roadmap** - Current state accuracy assessment, maintenance process, filter configuration approach
5. **Scorecard Specification** - Metrics, visual layout, update frequency, distribution method
6. **Executive Reporting Procedure** - Dashboard access, drill-down workflow, scheduled distribution setup
7. **Process Area Reporting Requirements** - Detailed requirements per department
8. **Integration Strategy Document** - SharePoint, Google Drive, Power BI decisions and configuration
9. **Training & Change Management Plan** - Schedule, curriculum, audience-specific content, success metrics

### Decisions Finalized:
- [ ] Dashboard architecture selected (minimalist, comprehensive, or hybrid)
- [ ] Export security policy defined
- [ ] Official report inventory complete
- [ ] Organizational hierarchy accuracy confirmed
- [ ] Power BI future state decided
- [ ] Training delivery approach selected

### Requirements Confirmed:
- [ ] All official reports identified and criteria documented
- [ ] All scorecard metrics and visual layouts approved
- [ ] Executive reporting workflow approved
- [ ] Process area specific requirements detailed
- [ ] All dashboards specified (name, content, role, lock status)
- [ ] Org hierarchy accuracy confirmed (or plan to fix identified)
- [ ] Export security policy approved

### Implementation Impact Assessed:
- [ ] Custom development scope (if any beyond standard NetSuite)
- [ ] Orion enhancement needs identified
- [ ] User training requirements by role/department
- [ ] Change management risks identified with mitigation
- [ ] Data migration requirements (if moving existing reports)
- [ ] Integration configuration scope

---

## PART 6: NEXT STEPS AFTER SESSION

Once this comprehensive follow-up session is complete:

1. **Finalize BRD** - Incorporate all clarifications and decisions into Business Requirements Document
2. **Create Dashboard Specifications** - Detail each dashboard with mockups
3. **Document Official Report Criteria** - Create standardized criteria documentation for each official report
4. **Configure Organizational Hierarchy** - Validate and correct manager relationships in system
5. **Develop Export Notification Workflow** - Begin custom development if threshold-based notification needed
6. **Design Scorecard Components** - Create scorecard dashboard layouts
7. **Configure Role-Based Permissions** - Set up dashboard publishing, export controls, report access
8. **Prepare Training Materials** - Create audience-specific training on official reports and dashboards
9. **Plan Change Management Communication** - Develop messaging strategy for "singing from same songbook"
10. **Schedule Training Sessions** - Confirm trainer availability and participant schedules

---

## APPENDIX: REFERENCE MATERIALS

### Related Documents:
- **Questionnaire_BusinessIntelligence_v1.0.md** - Comprehensive questionnaire with 27 requirements
- **Requirements_Map_BusinessIntelligence_v1.0.md** - Requirements classified by implementation approach
- **Master_Transcript_Business_Intelligence.md** - Full transcript from discovery sessions
- **GapAnalysis_BusinessIntelligence.md** - Gap analysis from discovery

### Key Requirements Requiring Follow-Up:
- **REQ-003**: Dashboard lock-down capability - TOPIC 1
- **REQ-008-010**: Official report designation and standardization - TOPIC 2
- **REQ-011-012**: Export security and notifications - TOPIC 3
- **REQ-023**: Org hierarchy for filters - TOPIC 4
- **REQ-020-021**: Sales rep and manager scorecards - TOPIC 5
- **REQ-024-025**: Executive reporting capability - TOPIC 6
- **REQ-026-027**: Backlog 360 and Bookings 360 - TOPIC 7

### Contact Information:
- **Primary Contact:** Lorraine (CFO)
- **Department Contacts:** Finance/Sales/Operations/Pre-Quote Leads
- **Technical Contact:** Kipp (IT/SuiteQL)
- **IT Security Contact:** IT Security Lead
- **GSI Lead:** Marcus (Implementation Lead)

---

**Document Version:** 1.0  
**Created:** October 2025  
**Status:** Ready for comprehensive single session scheduling

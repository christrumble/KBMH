# MASTER TRANSCRIPT: BUSINESS INTELLIGENCE & REPORTING
## KBM Hoag NetSuite Orion Implementation

**Sources Combined:**
- Business Intelligence.txt (July 31, 2025)
- 07-31 Workshop Operations transcript (Business Intelligence session portion)

**Date Range:** July 2025
**Business Process:** Business Intelligence, Reporting, Dashboards, Analytics

---

## EXECUTIVE SUMMARY

Business Intelligence and Reporting at KBM Hoag currently relies heavily on manual Excel-based processes, Google Sheets, and inconsistent report versions created by different team members. The primary challenge is multiple people creating similar reports with different criteria, leading to trust issues and "singing from different songbooks." NetSuite/Orion will provide real-time dashboards, 400+ standard reports, workbook analytics, saved searches, and SuiteQL for advanced querying. Critical success factors include establishing "official" reports, role-based dashboard publishing, data export controls, and training the team to use standardized reporting to maintain a single source of truth.

**Key Themes:**
- Multiple report versions causing trust issues
- Real-time vs. aged data
- Dashboard philosophy (home you live in all day)
- Role-based publishing
- Export security and controls
- Reminders portlet as daily work driver
- Saved searches vs. official reports
- "Singing from the same songbook"

---

## NETSUITE BI TOOLS OVERVIEW

### Core BI Capabilities

**Marcus:**
"Just to kind of give you the highlights of what's available to you inside NetSuite. So you have these core NetSuite BI tools. They are very powerful."

**Available Tools:**

1. **Dashboards**
   - KPIs and highlights
   - Visual components
   - Interactive charts
   - Drill-down to detail
   - Real-time data

2. **Standard Reporting**
   - 400+ built-in reports
   - Fully customizable
   - As-of date capability
   - Export options

3. **Workbook Analytics**
   - Excel-like interface
   - Pivot tables
   - Charts and graphs
   - Data manipulation

4. **SuiteQL**
   - NetSuite's SQL variant
   - Bypass application layer
   - Write custom queries
   - Fast execution

5. **Data Export**
   - CSV, Excel, PDF
   - Scheduled exports
   - Role-based permissions
   - Print capabilities

### Power BI Consideration

**Marcus:**
"I don't want to discourage you from using Power BI. If you love Power BI, use it, just keep in mind that the data is aged once it's out. But if you have a live connection, you've kind of mitigated that."

**Implication:**
- NetSuite has strong native BI tools
- Power BI still an option
- Live connection needed to avoid aged data
- Native tools recommended for real-time needs

---

## DASHBOARD PHILOSOPHY

### "The Home You Live In"

**Marcus:**
"We do spend some time on the dashboards building those out. It's actually part of the implementation, not software. But we'll talk some more about what's available there."

**Philosophy:**
"We kind of think of NetSuite as kind of the home that you're living in all day. So it should look good. So you feel good about where you're living."

**Aesthetics Matter:**
- Orion builds enhanced dashboard components
- Better visual appearance than standard NetSuite
- Part of implementation service
- Departmental customization

### Dashboard Components

**Built by Orion:**
- Enhanced visual components
- Better styling than NetSuite default
- Modern appearance
- User experience focus

**Available Elements:**
- KPI highlights (top of dashboard)
- Financial overview sections
- Charts and graphs (interactive)
- Saved search results
- Reminders portlet (critical)
- Recent transactions
- Task lists

---

## REPORTING TRUST CHALLENGE

### The Problem

**Marcus:**
"With all these tools, some of the problems that I've seen companies run into with these tools. A lot of it comes down to people writing reports, naming them similar. They have different criteria. You have different numbers, and people don't trust the reporting."

**Current State at KBM:**
"Right now we have reports that are like, you know, Mark's version, Matt's version, Kip's version."

**Common Scenario:**
"I want a revenue report for this time frame, and that revenue report can be written four or five different ways. Are you including taxes? Are you not including taxes? Are you looking at the net amount? Is that before discounts or after discounts? There's so many different ways to write that."

### Root Cause

**Inconsistent Criteria:**
- Same report name
- Different filters
- Different fields included/excluded
- Different calculation methods
- Different date ranges

**Result:**
- Different numbers for "same" metric
- Trust issues
- Debates about which is correct
- Time wasted reconciling

**Marcus:**
"It seems like a consistent problem... This is like a constant problem of people looking at the data differently and then not trusting the reports. And it really kind of comes down to... We used to call it singing from the same songbook. Yeah. It's a different key."

---

## SOLUTION: OFFICIAL REPORTS & STANDARDS

### Saved Search Prefix

**Marcus:**
"The one thing I'll encourage you to do as we get into implementation is we prefix our saved search, the ones that we create, and then we also sometimes will nominate something as being like an official saved search."

**Strategy:**
- Prefix GSI/Orion-created searches
- Designate "official" searches
- Communicate usage standards
- Train on interpretation

### Public vs. Private

**Marcus:**
"You can encourage them to... There's a little box that is make public. If you're going to make your own search, make it public [or] no one else needs to see that."

**Permission Controls:**
- Public: Visible to others
- Private: Personal only
- Role-based: Only certain roles see
- Control what searches proliferate

**Benefits:**
- Reduce clutter
- Prevent confusion
- Maintain standards
- Allow personal exploration

### Publishing Dashboards

**Marcus:**
"You have the ability to publish dashboards to people's [roles]... like all the other little menus on the top are all called centers so like there's a finance center and you can publish to a given role exactly what you want that dashboard to look like, so that they don't need to go and make their own searches."

**Lock-Down Capability:**
"When I was managing... people would get ambitious and they'd write some of their own saved searches and I would say hey dude like you have an opportunity here and you haven't you haven't done a follow-up on this opportunity in x amount of time. He goes, 'I don't [see it], what are you talking about? I don't see that anywhere.' I'm like, 'Are you [kidding]? It's on your dashboard.' 'No, I changed my dashboard.' I'm like, 'No, you're not doing that.' So then what I would do is I create a dashboard for them, publish it, and they can't change it."

**Benefits:**
- Manager controls what team sees
- Everyone looking at same data
- Weekly meetings use same dashboard
- Cannot customize away required views

**Personal Dashboards:**
- Can still have own dashboard on Home tab
- Published dashboards on role-specific centers
- Both coexist

---

## DASHBOARD DEEP DIVE

### Financial Overview Example

**Demo Shown:**
- KPIs at top (highlights)
- Bank balance
- Period-over-period reporting
- Revenue, expenses, profit
- Drilldown links

**Interactivity:**
"Anytime you see that link, that means you can drill down and get right down to the base information. So if I click on revenue, that's going to take me to most likely my income statement."

**From Income Statement:**
- Further drill to detailed report
- Change parameters on the fly
- Real-time data

**Quote:**
"So that's another thing that's nice about the dashboards is it's linked to the detail information."

### Executive Team Presentation

**Lorraine's Question:**
"On that, like the dashboard is great, especially for the finance team in this instance, but then how are they, when it's month end and they come to present to Mark and I, how are they... do they have to export all of that into Excel or are they able to do the presentation through Orion?"

**Marcus Answer:**
"Yep. Yeah, we just have to, yeah. And whatever you want to see, we would just create that dashboard."

**Marcus's Experience:**
"When we would sit down and we would have our financial reports, I would just pull up the income statement, the balance sheet, trial balance, walk through it. There's usually... questions, drill down, figure out. AR is a great example. Like we look at the AR report and like, why the heck is this past 90 days? Drill down, find the invoice, task out the sales rep to call."

**Challenge:**
"The problem is we're not, sometimes we're not all together to do a financial review. So I have to send it to somebody. Like this week, in case you're not here, do a package together and send it to me."

**Solution:**
- Can schedule reports and email automatically
- Can package for executives if needed
- "If it makes sense to package it so it's easier for the executive team, I can understand why."

---

## REMINDERS PORTLET (CRITICAL)

### Concept

**Marcus:**
"This reminders portlet is key. So you can write a safe search. You can put it in this reminders portlet. And this is really what everybody's work is on a daily basis."

**Daily Work Driver:**
"In fact, let me jump over to, I think financial management might have more on the reminders portlet. So I'm, I work in your organization. I come in, I log in the day and I see my reminders portlet. This is all the work that I have to work off of. Like it shouldn't, you shouldn't have to guess."

**Example Reminders:**
- Bills to pay
- Bills on hold
- Tasks to complete
- Acknowledgements to review
- Opportunities needing follow-up
- Phone calls to make
- Events scheduled

### Actionable, Not Just Informational

**Quote:**
"All of these, they're not just informational. I can drill down and get to that task list and work on that task list from there."

**Workflow:**
1. See reminder
2. Click to drill down
3. Work the task list
4. Mark complete
5. Next reminder

### Department vs. Individual

**Lorraine:**
"Was that by individual or could it be departmental?"

**Marcus:**
"Either one. Yep. So what's nice is as we talked about publishing the dashboard, so you can publish this dashboard to your financial team. They could still have their own dashboard on the Home tab for some other things that they want to track. But, yeah, you have control over that."

**Example (Financial Team Reminders):**
- Bills to pay
- Bills on hold
- Tasks to complete
- Period close checklist items
- Bank reconciliation items
- Credit memos to process

---

## SAVED SEARCHES

### Functionality

**Table View:**
- List of records
- Multiple columns of data
- Filters and sorting
- Export capability

**Interactive Features:**
- Click to view record
- Click to edit record
- Change status inline
- Drill to detail

**Marcus:**
"For those of you that like tables of data and not visuals, we got them."

### Inline Editing

**Pencil Icon:**
"Whenever you see a pencil here, that means you can edit right here without having to go in and edit the whole record."

**Example:**
"So I can change my status here to in discussion and that's going to update it and you can see my probabilities linked to it just changed."

**Use Case:**
"So if I need to like quickly go through my opportunity list and change things, I can do that. But think about that for anything else in the system. If I have a list of acknowledgements that I need to go through and mark and complete... My tasks, actually, this is a great way to manage your task list because you can drill down, but you can also change the status from here."

**Benefits:**
- Don't have to open each record
- Bulk updates faster
- See context while updating
- Maintain list view

### Highlighting Rules

**Visual Indicators:**
- Conditional formatting
- Highlight by criteria
- Color coding
- Quick identification

**Example (Expected Close Date):**
- Past dates highlighted red
- Future dates normal
- Easy to spot overdue items

**Marcus Demo:**
"I'm going to go in here and show you just how easy this is... I'm going to say if the expected close date is before today that's a problem so I'm... somebody can easily come in here and say all right well I already know the status of this one, this one is the expected close date is going to be some time in the future."

**Result:**
- Work right off saved searches
- Visual priority indication
- Quick status assessment

### Mass Update

**Capability:**
"There's also a mass update function that's a little more involved, but you can, in a safe search, do a mass update."

**Use Cases:**
- Bulk status changes
- Field updates across multiple records
- Data cleanup
- Process automation

---

## CENTERS & TABS

### Tab Structure

**Question:**
"The tabs at the top are each of the different portals, if you will, or centers? Centers. And then you have a dashboard within each of those?"

**Marcus:**
"Yeah. Or a number of dashboards. Okay. Because my thought was is like you have one dashboard, and you're like, how do I, where do I even know where to look for everything? You just be scrolling. You can have a dashboard on each one of these tabs. And the home is kind of like your default dashboard. And then the other ones are like processor specific."

**Examples:**
- Home (default/personal dashboard)
- Finance Center
- Sales Center
- Pre-Quote Center
- Order Management Center
- Operations Center
- Etc.

**Use Case:**
"So if you were in pre-quote, you could have a dashboard built about what you need to do for pre-quote. Exactly."

---

## STANDARD REPORTS

### Scope

**Marcus:**
"Standard reporting, NetSuite ships with over 400 standard reports. And that's everything from income statement, trial balance, balance sheet. And every single one of those reports can be customized."

**Customization:**
"So if you need a variation of that report, it's very simple. We'll show you how to do that."

### As-Of Date Capability

**Unique Feature:**
"I mentioned this yesterday, but it bears repeating. Reporting in NetSuite is unique because you can get the as of dates for those reports. So like what was my balance sheet as of September 1st. You can get that."

**Comparison:**
"Where some of the other business intelligence tools are dynamic. So you just need to keep that in mind. So it kind of comes down to which tool is appropriate for what you're looking for."

**Use Cases:**
- Historical comparisons
- Period-end snapshots
- Audit trails
- Regulatory reporting

### Export Options

**Capabilities:**
"Pretty much on everything, you can export the data. You can schedule to get exported. You can print it. You can export it to CSV, XLS for Excel, anything you want there."

---

## WORKBOOK ANALYTICS

### Excel-Like Functionality

**Description:**
"We also have workbooks, which is like think of like Excel. It's called workbook analytics. So pivot table charts, you can build those out inside NetSuite."

**Example Shown:**
- Pipeline analysis
- Filter by team member, location, product type
- Interactive charts
- Drill-down capability
- Multiple visualization options

**Interactivity:**
"This has filters at the top so I can see, here's my pipeline, but here's everybody's pipeline. So if I was a manager and I had access to this, I could see everybody's."

**Role Limitation:**
"Can you limit what that click down is so they can only see theirs? Yep. It can be defaulted."

**Stacking Filters:**
"And just furniture. Well, somebody's not selling over there in the east. And just furniture. And then all these are stackable. So you can set multiple filters and that'll influence what shows up."

**Excel Replacement:**
"So again, sometimes little things like this you have to do in Excel, but this is an analytics workbook and we're just pinning the results of it to a dashboard."

---

## SUITEQL

### Capability

**Marcus:**
"We have SuiteQL, which is NetSuite's kind of own version of SQL. You can, so that means you can write queries."

**Technical Details:**
- Bypass application layer
- Direct database queries
- Very fast execution
- Advanced reporting

**Target Audience:**
- Technical users (Kipp)
- Database-savvy staff
- Custom report needs
- Performance-critical queries

---

## DATA EXPORT SECURITY

### Current Core Problem

**Quote:**
"Right now there's not a lot of control in Core to determine who can export what information. So we haven't had this issue, but someone who was in sales and left one company and came to another company, you know, I could [export customer data], but that company, there was no way for me to export my customer data. In Core, I can't prevent that from happening right now. Is that the same in NetSuite or?"

**Concerns:**
- Customer data theft
- Competitive intelligence
- Employee departure risks
- Data breach potential

### NetSuite Solutions

**Permission-Based:**
"For a given role there is a report export [permission] and that's what actually shows the button for like PDF and Excel and everything. You can turn that off on a role basis."

**Limitation:**
"It's an all-or-nothing setting."

**Challenge:**
"But not off a per-report basis. Like what if I want them to be able to export order details into Excel because they need to manipulate the data or stack it a certain way... there's like pros and cons to turning it off and on."

**Marcus:**
"My first glance it is it's an all-or-nothing setting."

### Notification System

**Proposed:**
"The good news about Core is that it's actually really complicated to do it, so... [someone exporting] in Google Drive, for instance, there's a setting that I... An export starts and it's COCUS not data notified. Someone says dumping gigabytes of data. What's going on? I mean, I don't know that it would stop them, but at least it would alert me and I could..."

**Solution:**
"Trigger system to alert if more than 50 megabytes of data are being downloaded."

### Workaround Risk

**Marcus:**
"Another thing, too, just to be aware of, like, if you have a report and they don't have the ability to export it, they can technically, because it's browser-based, just highlight everything, Control-C, Control-V, and Excel, and they got it. So just something to think about there."

**Reality:**
- Can't completely prevent data extraction
- Role-based permissions help
- Notifications provide awareness
- Balance control vs. functionality

### Requirement

**Action Item:**
"Let's list that as a requirement, some permission around exporting and some notifications around if something was exported over a certain amount."

---

## REPORTING ACROSS PROCESS AREAS

### Coverage

**Marcus:**
"At this point, do you feel there's anything we have yet to talk about from a reporting business intelligence standpoint and we can kind of go through the process areas again."

**Already Discussed:**

**Marketing & CRM:**
- Pipeline reports critical
- Opportunity tracking
- Lead conversion
- Campaign effectiveness

**Financials:**
- Standard financial reports (P&L, balance sheet, trial balance)
- "You guys are doing a lot about a lot of reporting outside in Google sheets"
- Goal: Get reporting into system

**Operations:**
- PM workload visibility
- Resource utilization
- Project status
- Installation tracking

**Order Management:**
- Backlog reporting
- Booking reports
- Acknowledgement tracking
- Fulfillment status

---

## SCORECARDS & KPIs

### Sales Rep Scorecards

**Marcus:**
"Do you have any kind of like scorecards or anything like that that you do... they were really popular a few years ago but like you can have a scorecard by like maybe sales rep where [it] shows total revenue um total gp across all their projects."

**Current State:**
"You guys basically do that in the booking report right now okay right?"

**Booking Report:**
- Director's tab in shared folder
- Shows year-to-date performance
- GP by sales rep

**Wendy's Request:**
"So I would love them to see that on their own dashboard. And then if he was ever managing them on their dashboard, it shows them all of their people."

**Filters Needed:**
- Me only (individual view)
- Me and my team (manager view)
- Specific people
- Date ranges

---

## ORG STRUCTURE & HIERARCHY

### Core Frustration

**Quote:**
"That's been one of the frustrations with Core. They do allegedly have this hierarchy of permissions, roles and permissions, and, like, this is the manager. They report to that manager, and that manager is supposed to see everyone, and it doesn't. I've never gotten that."

**NetSuite Difference:**

**Marcus:**
"That's one of the downsides, like, managing the org structure in NetSuite. You have to have the right managers assigned for those filters to work. But if we set that up, if we set it up, it actually works. Good."

**Key:**
- Must properly configure org structure
- Manager assignments critical
- Then filters work correctly
- "Me and my team" filters functional

---

## SAMPLE DASHBOARDS

### Financial Overview

**Components Shown:**
- KPIs at top (bank balance, revenue, etc.)
- Period-over-period reporting
- Financial summary sections
- Drill-down links
- Real-time data

**Use Case:**
- CFO daily view
- Quick financial health check
- Access to detail when needed

### Sales Dashboard

**Pipeline View:**
- Graphical representation
- Filter by status
- Filter by sales rep
- Interactive charts
- Stackable filters

**Tables:**
- Open opportunities
- Inline editing (status changes)
- Drill to detail
- Task creation

**Marcus:**
"And I understand it because I think this is a little bit quicker for me too. So here's my open opportunities as a sales rep. I can do some filtering here just to show different statuses. I can click on view from here. I can go to edit. I can start scheduling activities from here."

### Reminders Portlet

**Critical Daily Tool:**
- Bills to pay
- Bills on hold
- Tasks to complete
- Overdue items
- Scheduled events

**Actionable:**
- Click to work item
- Complete from reminder view
- Real-time updates

---

## REPORTING EXAMPLES

### Backlog Reporting

**Marcus:**
"We're building on a backlog 360 dashboard, so it's just one dashboard that has everything you could ever imagine for backlog in one place."

**Reports Available:**
- Backlog by line
- Backlog by order
- Backlog 360 (comprehensive)

### Booking Reporting

**Similar Structure:**
- Bookings by line
- Bookings by order
- Bookings 360 (comprehensive)

### Other Standard Reports

**Mentioned:**
- Receive not invoiced
- Receive not scheduled
- Order status reports
- Director's performance tab

---

## ACCOUNT MANAGER STATUS REPORTS

### Current Process

**Question:**
"Can I look at the status report in order management?"

**Marcus:**
"I don't know if we have it in this account. Every account manager currently uses status reports to do their jobs."

**Implication:**
- Exists in production
- Not in demo account
- Critical to account manager workflow

---

## INTEGRATION & DATA SOURCES

### SharePoint Integration

**Mentioned:**
"I think we've mentioned already the SharePoint integration."

**Also on List:**
- Google Drive integration validation
- Keep reporting inside system
- Always real-time data

---

## REPORTING BY PROCESS AREA SUMMARY

### Marketing & CRM
- Pipeline reports
- Lead conversion
- Campaign ROI
- Opportunity tracking
- Sales rep performance

### Financial Management
- Income statement
- Balance sheet
- Trial balance
- Cash flow
- AR/AP aging
- Bank reconciliation
- Period close checklist

### Order Management
- Backlog 360
- Bookings 360
- Acknowledgement tracking
- Fulfillment status
- Invoice tracking
- Customer PO utilization

### Operations
- PM workload
- Resource utilization
- Project status
- Work order completion
- Punch list tracking
- Time tracking reports

### Pre-Quote
- RFP tracking
- Quote pipeline
- Win/loss analysis
- Resource allocation

### Project Management
- Project health
- Budget vs. actual
- Milestone tracking
- Task completion
- Resource loading

---

## DECISIONS & ACTION ITEMS

### Decisions Made

1. **Official Report Strategy:**
   - Prefix GSI/Orion reports
   - Designate official versions
   - Publish to roles (lock down)
   - Prevent dashboard customization (for some roles)

2. **Dashboard Approach:**
   - Department-specific dashboards
   - Role-based publishing
   - Manager-controlled views
   - Personal dashboard option on Home tab

3. **Reminders Portlet:**
   - Use as daily work driver
   - Critical component
   - Department and individual versions

4. **Export Controls:**
   - Implement role-based export permissions
   - Notification system for large exports (>50MB)
   - All-or-nothing limitation acknowledged

5. **Reporting Standards:**
   - Standardize key reports
   - Train on interpretation
   - Single source of truth approach
   - "Singing from same songbook"

### Action Items

1. **GSI/Orion:**
   - Build department-specific dashboards
   - Create official report suite
   - Configure export permissions
   - Set up large export notifications
   - Establish naming conventions

2. **Reporting Requirements:**
   - Gather all current report examples
   - Define official versions
   - Document criteria and interpretation
   - Build training materials

3. **Org Structure:**
   - Properly configure manager hierarchy
   - Enable "me and my team" filters
   - Test role-based permissions

4. **Scorecard Design:**
   - Sales rep scorecard for own dashboard
   - Manager view of team scorecards
   - Filter options

5. **Integration:**
   - Validate SharePoint integration
   - Validate Google Drive integration
   - Confirm real-time data flow

### Open Questions

1. **Export Security:**
   - What threshold for notification? (Proposed: 50MB)
   - Which roles can export?
   - Which roles cannot?
   - Special exceptions?

2. **Official Reports:**
   - Complete list of official reports needed
   - Who authorizes official designation?
   - Update process for official reports
   - Version control approach

3. **Dashboard Publishing:**
   - Which roles get locked dashboards?
   - Which roles can customize?
   - Override process for special cases

4. **Training:**
   - How to ensure consistent interpretation?
   - What's training schedule?
   - Who trains whom?
   - Ongoing support model

5. **Power BI:**
   - Continue using or not?
   - Live connection setup
   - Which reports stay in Power BI?
   - Integration approach

---

## PAIN POINTS TO SOLVE

### Current Frustrations

1. **Multiple Report Versions:**
   - "Mark's version, Matt's version, Kip's version"
   - Different numbers from "same" report
   - Trust issues
   - Time wasted reconciling

2. **Excel-Based Reporting:**
   - Manual report generation
   - Outdated information
   - Not real-time
   - Labor-intensive

3. **Google Sheets Overload:**
   - Multiple departments using
   - Not integrated
   - Duplication of effort
   - Version control issues

4. **Core Export Security:**
   - No controls
   - Customer data vulnerable
   - Competitive intelligence risk

5. **Org Hierarchy Failure:**
   - "Me and my team" filters don't work in Core
   - Manager visibility broken
   - Manual workarounds

6. **Manual Data Compilation:**
   - Month-end package for executives
   - Copy/paste from multiple sources
   - Time-consuming
   - Error-prone

7. **Inconsistent Dashboards:**
   - Users customize away required views
   - Managers can't reference same data
   - Training challenges

### Future State Solutions

1. **Official Reports:**
   - Designated official versions
   - Standardized criteria
   - Documented interpretation
   - Single source of truth
   - "Singing from same songbook"

2. **Real-Time Dashboards:**
   - Live data
   - No manual refresh
   - Drill-down to detail
   - Self-service analytics

3. **Published Dashboards:**
   - Role-based control
   - Lock down required views
   - Manager-team alignment
   - Consistent weekly meetings

4. **Export Controls:**
   - Role-based permissions
   - Notification system
   - Activity monitoring
   - Reduced risk

5. **Working Org Hierarchy:**
   - Proper configuration
   - Functional filters
   - Manager visibility
   - Team views

6. **Executive Reporting:**
   - Real-time dashboard access
   - Scheduled automated reports
   - Packaged delivery option
   - Drill-down capability

7. **Reminders Portlet:**
   - Daily work clarity
   - No guessing
   - Actionable lists
   - Automated workflow

---

## QUOTES & INSIGHTS

**On Reporting Trust:**
"A lot of it comes down to people writing reports, naming them similar. They have different criteria. You have different numbers, and people don't trust the reporting... This is like a constant problem."

**On Current State:**
"Right now we have reports that are like, you know, Mark's version, Matt's version, Kip's version."

**On The Problem:**
"I want a revenue report for this time frame, and that revenue report can be written four or five different ways. Are you including taxes? Are you not including taxes? Are you looking at the net amount? Is that before discounts or after discounts? There's so many different ways to write that."

**On Singing from Same Songbook:**
"We used to call it singing from the same songbook. Yeah. It's a different key."

**On Dashboard Philosophy:**
"We kind of think of NetSuite as kind of the home that you're living in all day. So it should look good. So you feel good about where you're living."

**On Reminders Portlet:**
"This is all the work that I have to work off of. Like it shouldn't, you shouldn't have to guess."

**On Inline Editing:**
"So if I need to like quickly go through my opportunity list and change things, I can do that. But think about that for anything else in the system."

**On Dashboard Control:**
"'I changed my dashboard.' I'm like, 'No, you're not doing that.' So then what I would do is I create a dashboard for them, publish it, and they can't change it."

**On Executive Presentations:**
"When we would sit down and we would have our financial reports, I would just pull up the income statement, the balance sheet, trial balance, walk through it. There's usually... questions, drill down, figure out."

**On As-Of Date Reporting:**
"Reporting in NetSuite is unique because you can get the as of dates for those reports. So like what was my balance sheet as of September 1st. You can get that."

**On Export Security:**
"Another thing, too, just to be aware of, like, if you have a report and they don't have the ability to export it, they can technically, because it's browser-based, just highlight everything, Control-C, Control-V, and Excel, and they got it. So just something to think about there."

**On Core Org Structure:**
"That's been one of the frustrations with Core. They do allegedly have this hierarchy of permissions, roles and permissions, and, like, this is the manager. They report to that manager, and that manager is supposed to see everyone, and it doesn't. I've never gotten that."

**On NetSuite Org Structure:**
"You have to have the right managers assigned for those filters to work. But if we set that up, if we set it up, it actually works."

---

## CHANGE MANAGEMENT CONSIDERATIONS

### Behavior Changes Required

1. **Use Official Reports:**
   - Stop creating personal versions
   - Use designated official reports
   - Follow standardized interpretation
   - Trust the single source

2. **Dashboard Discipline:**
   - Accept published dashboards
   - Don't customize away required views
   - Use provided reminders portlet
   - Resist urge to "make it your own"

3. **Daily Reminders:**
   - Start day with reminders portlet
   - Work from system, not email
   - Complete tasks inline
   - Trust workflow

4. **Real-Time Mindset:**
   - Stop creating static snapshots
   - Use live dashboards
   - Drill down instead of export
   - Embrace real-time data

5. **Export Discipline:**
   - Export only when necessary
   - Be aware of data sensitivity
   - Use in-system analysis
   - Respect security controls

### Resistance Points

1. **Loss of Control:**
   - Can't customize dashboard
   - Manager controls what I see
   - Feels restrictive
   - "I know what I need"

2. **Learning Curve:**
   - New tool (saved searches)
   - Different navigation
   - Drill-down vs. export
   - Filter combinations

3. **Trust in System:**
   - Must trust official reports
   - Can't verify with own version
   - Rely on others' criteria
   - "What if it's wrong?"

4. **Export Limitations:**
   - Can't extract customer list
   - Notifications for large exports
   - All-or-nothing permissions
   - Workaround temptation

5. **Real-Time Adjustment:**
   - Used to static reports
   - Numbers change throughout day
   - Different from Excel snapshot
   - Period-close timing matters

### Success Factors

1. **Reminders Portlet Clarity:**
   - Eliminates guessing about daily work
   - Clear priorities
   - Actionable items
   - Immediate value

2. **Drill-Down Power:**
   - See summary, drill to detail
   - Answer questions immediately
   - No waiting for reports
   - Self-service

3. **Manager-Team Alignment:**
   - Everyone seeing same dashboard
   - Weekly meetings use same data
   - No "I don't see that" excuses
   - Accountability

4. **As-Of Date Historical:**
   - Can still get month-end snapshots
   - Historical comparisons possible
   - Audit trail maintained
   - Best of both worlds

5. **Aesthetic Appeal:**
   - Orion-enhanced components
   - Looks modern
   - Pleasant to use daily
   - "Home you live in"

6. **Inline Editing:**
   - Update status without opening records
   - Work through lists efficiently
   - Immediate productivity gain
   - Obvious time savings

### Training Focus

1. **Official Report Usage:**
   - Which reports are official
   - How to interpret
   - When to use which
   - What criteria mean

2. **Saved Search Basics:**
   - How to filter
   - How to export (if permitted)
   - How to save personal searches
   - Public vs. private

3. **Dashboard Navigation:**
   - Centers vs. Home
   - Drill-down technique
   - Filter usage
   - Refresh timing

4. **Reminders Portlet:**
   - How reminders appear
   - How to work items
   - How to complete tasks
   - How to prioritize

5. **Inline Editing:**
   - Pencil icon recognition
   - Quick status changes
   - Bulk operations
   - When to use vs. full edit

6. **Workbook Analytics:**
   - Pivot table creation
   - Chart building
   - Filter stacking
   - Pinning to dashboard

7. **Data Governance:**
   - Why standardization matters
   - Export security awareness
   - Single source of truth concept
   - "Singing from same songbook"

---

## INTEGRATION POINTS

### Document Management

**SharePoint:**
- Keep reporting in system
- Real-time data
- Integrated documents

**Google Drive:**
- Validation needed
- Integration approach
- Document links

### Email Systems

**Scheduled Reports:**
- Automated generation
- PDF/Excel delivery
- Distribution lists
- Frequency settings

### Workflow Automation

**Reminders Portlet:**
- Saved search integration
- Status-driven workflows
- Task automation
- Alert systems

---

## PERFORMANCE METRICS STRATEGY

### Real-Time KPIs

**Available:**
- Revenue
- GP
- Cash balance
- AR/AP aging
- Open orders
- Backlog
- Pipeline

### Historical Trends

**As-Of Date Capability:**
- Month-over-month
- Year-over-year
- Same period last year
- Custom date ranges

### Comparative Analysis

**Period-Over-Period:**
- Current vs. prior month
- Current vs. budget
- Current vs. forecast
- Current vs. same period last year

---

*End of Master Transcript: Business Intelligence & Reporting*


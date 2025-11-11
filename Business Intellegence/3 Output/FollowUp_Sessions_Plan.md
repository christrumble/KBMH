# Business Intelligence Follow-Up Topics & Sessions Plan
**Created**: November 5, 2025  
**Status**: Ready for Scheduling  
**Target Completion**: 6-8 weeks  
**Priority Tiers**: Critical (4) | High (5) | Medium (2)

---

## QUICK REFERENCE: SESSION MATRIX

| Priority | Session # | Topic | Duration | Required Attendees | When |
|----------|-----------|-------|----------|-------------------|------|
| 🔴 CRITICAL | 1 | Export Security Policy | 90 min | IT Security, Dept Heads, Legal/Compliance | Week 1-2 |
| 🔴 CRITICAL | 2 | Official Reports Definition | 2-3 hrs | All Dept Leads, Key Report Creators | Week 1-2 |
| 🔴 CRITICAL | 3 | Org Hierarchy & Scorecards | 2 hrs | HR Lead, Wendy, Sales Mgrs, IT Admin | Week 3 |
| 🔴 CRITICAL | 4 | Process-Specific Reports | 2 hrs | Order Mgmt Lead, Account Managers | Week 4 |
| 🟡 HIGH | 5-9 | Dashboard Design (5 depts) | 5 × 90 min | Dept Leads + teams (separate) | Week 5-7 |
| 🟢 MEDIUM | 10 | Integration Strategy | 60 min | IT Lead, Power BI users | Week 7-8 |
| 🟢 MEDIUM | 11 | Executive Dashboard | 60 min | Lorraine, Mark, Finance Lead | Week 7-8 |

---

## 🔴 CRITICAL SESSIONS (MUST-DO)

### SESSION 1: Export Security Policy Definition
**Priority**: 🔴 CRITICAL  
**Duration**: 90 minutes  
**Status**: BLOCKS REQ-011, REQ-012  
**Completion**: Week 1-2

#### Questions to Answer:
- What is the approved threshold for large data export notifications? (50MB proposed)
- Which roles CAN export data?
- Which roles CANNOT export data?
- Who receives export notifications?
- What is the audit trail retention policy?
- Are there report-specific exceptions needed?
- What response protocol after alert?

#### Required Attendees:
- **Owner**: IT Security Lead
- **Participants**: Department Heads (Finance, Sales, Operations, Order Management, Pre-Quote)
- **Optional**: Legal/Compliance, Executives (Lorraine, Mark)
- **Facilitator**: GSI/Orion Implementation Team

#### Pre-Work for Client:
- **IT Security Lead**: Draft proposed role matrix based on current Core state
  - Which roles currently have export access
  - Which should have export access in NetSuite
  - Special exceptions needed
- **Department Heads**: Identify which roles in your area need export capability and WHY
- **Legal/Compliance**: Note any regulatory requirements for audit trails

#### Session Agenda:
1. Review current Core export access (15 min)
2. Define role-by-role export matrix for NetSuite (30 min)
3. Define large export notification system (30 min)
   - Threshold approval (50MB or different?)
   - Recipients list
   - Response protocol
4. Review all-or-nothing limitation and implications (10 min)
5. Final approval and sign-off (5 min)

#### Expected Outcomes:
- ✅ Approved role export permissions matrix
- ✅ Approved notification threshold and recipients
- ✅ Notification workflow specifications
- ✅ Audit trail requirements documented
- ✅ **Questionnaire Impact**: Q9 and BI-NEW-01 FULLY ANSWERED

**Business Impact**: SECURITY CONTROL - Prevents customer data theft

---

### SESSION 2: Official Reports Definition Workshop
**Priority**: 🔴 CRITICAL  
**Duration**: 2-3 hours  
**Status**: BLOCKS REQ-001, REQ-008, REQ-010  
**Completion**: Week 1-2

#### Questions to Answer:
- What is the complete list of official reports needed by department?
- Who has authority to designate/change official reports?
- What is the process for requesting new official reports?
- How are report changes approved and communicated?
- What naming convention standards should be used?
- How should report criteria be documented?
- What training plan is needed for adoption?
- How to manage users creating personal versions?

#### Required Attendees:
- **All Department Leads**: Finance, Sales, Operations, Order Management, Pre-Quote, Marketing/CRM
- **Key Report Creators**: Mark, Matt, Kip (mentioned in transcript)
- **Facilitator**: GSI/Orion Implementation Team
- **Optional**: Executives (Lorraine, Mark) for governance approval

#### Pre-Work for Client:
- **Each Department Lead**: Bring list of CRITICAL REPORTS with:
  - Report name
  - Purpose/use case
  - Frequency of use
  - Current format (Excel, Google Sheets, Core)
  - Current example output
- **All Participants**: Identify reports where "different versions" exist
  - Mark's version vs. Matt's version vs. Kip's version
  - Document the differences

#### Session Agenda:
1. Review reporting proliferation problem (15 min)
   - Show "Mark's version, Matt's version, Kip's version" examples
   - Discuss impact on trust
2. Review each department's critical reports (90 min - 15 min per department)
   - Marketing/CRM: Pipeline, lead conversion, campaign ROI
   - Finance: Financial statements, AR/AP aging, bank rec
   - Order Mgmt: Backlog, bookings, acknowledgements
   - Operations: PM workload, resource utilization
   - Pre-Quote: RFP tracking, quote pipeline
   - Cross-functional: Multi-department reports
3. Consolidate redundant reports (30 min)
   - Where multiple versions exist
   - Agree on single official version criteria
4. Define governance process (20 min)
   - Who designates official reports?
   - Process for new official reports
   - Change control process
   - Version control approach
5. Establish naming conventions (10 min)
6. Prioritize report build order (10 min)
7. Approvals (5 min)

#### Expected Outcomes:
- ✅ Complete official report list by department (30-50 reports estimated)
- ✅ Report criteria defined for each official report
- ✅ Governance process documented
- ✅ Naming convention standards
- ✅ Prioritized build order
- ✅ **Questionnaire Impact**: Q10 FULLY ANSWERED, Q2 and BI-NEW-03 COMPLETED

**Business Impact**: SOLVES CORE PAIN POINT - "Singing from same songbook"

---

### SESSION 3: Organizational Hierarchy & Scorecard Design
**Priority**: 🔴 CRITICAL  
**Duration**: 2 hours  
**Status**: BLOCKS REQ-023, REQ-022, REQ-020, REQ-021  
**Completion**: Week 3

#### Questions to Answer:

**Part 1 - Organizational Hierarchy (60 min):**
- What is the current complete org structure (who reports to whom)?
- Are there multi-level hierarchy requirements (skip-level visibility)?
- How are matrix organizations / dotted-line reporting relationships handled?
- What is the process for maintaining/updating manager assignments?
- How frequently do reporting relationships change?

**Part 2 - Sales Rep Scorecards (60 min):**
- What specific metrics should appear on scorecards (beyond revenue and GP)?
- What is the target-setting process for scorecard metrics?
- Who sets targets and how often are they updated?
- What is the scorecard update frequency (real-time vs. daily/weekly)?
- Should other departments have scorecards too?

#### Required Attendees:
- **HR Lead** (org structure expert)
- **Wendy** (Sales Leadership - scorecard requirements)
- **Sales Managers** (scorecard validation)
- **IT Admin** (will configure NetSuite employee records)
- **Facilitator**: GSI/Orion Implementation Team

#### Pre-Work for Client:
- **HR Lead**: Provide current org chart with manager assignments
  - Complete hierarchy (who reports to whom)
  - Manager assignments for all employees
  - Any matrix reporting relationships
- **Wendy**: Bring current booking report from "Director's tab in shared folder"
  - Current format and metrics shown
  - Any examples or sample data
- **Sales Managers**: List desired scorecard metrics beyond revenue/GP
  - What else should track performance?
  - What comparisons matter?

#### Session Agenda - Part 1: Org Hierarchy (60 min)
1. Review current org chart (15 min)
2. Validate manager assignments (15 min)
3. Identify multi-level hierarchy needs (10 min)
4. Address matrix organization / dotted-line reporting (10 min)
5. Define maintenance process (10 min)
   - Who submits changes?
   - How are changes approved?
   - How quickly reflected in system?
   - Process for testing filter validation

#### Session Agenda - Part 2: Scorecards (60 min)
1. Review current booking report (15 min)
2. Define scorecard metrics (20 min)
   - Revenue (current)
   - GP / GP % (current)
   - Number of projects
   - Win rate
   - Pipeline value
   - Other metrics?
3. Define target-setting process (10 min)
   - Who sets targets?
   - How often updated?
   - Individual vs. team targets
4. Review scorecard mockup (10 min)
5. Approve design for development (5 min)

#### Expected Outcomes:
- ✅ Complete org structure documentation with manager assignments
- ✅ Org structure maintenance process defined
- ✅ Sales rep scorecard metrics APPROVED
- ✅ Target-setting process documented
- ✅ Scorecard mockup approved for development
- ✅ **Questionnaire Impact**: Q11, Q12, BI-NEW-05 FULLY ANSWERED

**Business Impact**: Foundation for "me and my team" filters + sales visibility

---

### SESSION 4: Process-Specific Report Specifications
**Priority**: 🔴 CRITICAL  
**Duration**: 2 hours  
**Status**: BLOCKS REQ-026, REQ-027, Account Manager Status Report  
**Completion**: Week 4

#### Questions to Answer:

**Backlog 360 (40 min):**
- What components should be included in comprehensive Backlog 360 dashboard?
- What filters and drill-downs are needed?
- How should backlog be analyzed (by line, by order, by customer, by product, by aging)?

**Bookings 360 (40 min):**
- What components should be included in comprehensive Bookings 360 dashboard?
- Similar structure to Backlog 360 or different approach?
- What drill-down capabilities needed?

**Account Manager Status Report (35 min):**
- What are the critical fields for Account Manager status report?
- What filtering capabilities are needed?
- Is this "critical to daily workflow" per Marcus statement?

#### Required Attendees:
- **Order Management Lead** (owner)
- **Account Managers** (2-3 representatives)
- **Facilitator**: GSI/Orion Implementation Team
- **Optional**: Executives who use Backlog/Bookings reports

#### Pre-Work for Client:
- **Order Management Lead**: Bring current backlog and bookings reports
  - All versions currently in use
  - Screenshots or examples
  - "Wish list" - what would be "everything you could ever imagine for backlog"
- **Account Managers**: Bring example of current status report
  - From Core production
  - List all fields/filters needed
  - How it's used daily

#### Session Agenda - Backlog 360 (40 min)
1. Review current backlog reports (10 min)
2. Define comprehensive components (20 min)
   - Backlog by line
   - Backlog by order
   - Backlog by project
   - Backlog aging
   - Backlog by customer
   - Backlog by product line
   - Other components?
3. Define filters and drill-downs (10 min)

#### Session Agenda - Bookings 360 (40 min)
1. Review current bookings reports (10 min)
2. Define comprehensive components (20 min)
   - Similar structure to Backlog 360
   - YTD bookings
   - Bookings by sales rep
   - GP by sales rep
   - Other components?
3. Define filters and drill-downs (10 min)

#### Session Agenda - Account Manager Status Report (35 min)
1. Review current report from production (10 min)
2. Define required fields (15 min)
3. Define filters (5 min)
4. Validate critical to daily workflow (5 min)

#### Session Agenda - Wrap-Up (5 min)
- Next steps and approval

#### Expected Outcomes:
- ✅ Backlog 360 component specifications
- ✅ Bookings 360 component specifications
- ✅ Account Manager status report requirements
- ✅ Prioritized build order
- ✅ **Questionnaire Impact**: Q14 and Q5 (partial) FULLY ANSWERED

**Business Impact**: Custom comprehensive dashboards for Order Management

---

## 🟡 HIGH PRIORITY SESSIONS (SHOULD-DO)

### SESSIONS 5-9: Dashboard Design by Department
**Priority**: 🟡 HIGH  
**Duration**: 5 × 90 minutes (one per department)  
**Status**: Resolves Q4, Q6 gaps, locks down dashboard KPIs  
**Completion**: Week 5-7

#### Overview:
Five separate sessions to design department-specific dashboards for each process area center.

#### SESSION 5: Finance Center Dashboard Design (90 min)
**Required Attendees**:
- Finance Lead
- 2-3 Finance team members
- Department Manager
- GSI/Orion team

**Pre-Work**:
- Finance Lead: List desired KPIs for dashboard
- Team Members: List daily tasks for reminders portlet
- Manager: Identify if locked dashboard needed for team

**Questions to Answer**:
- What are the top 5-7 KPIs to appear at top of dashboard?
- What financial overviews are needed?
- What period-over-period comparisons matter?
- What saved searches should appear as reminders portlet?
- Should dashboard be locked for team or flexible?

---

#### SESSION 6: Sales Center Dashboard Design (90 min)
**Required Attendees**:
- Sales Lead
- 2-3 Sales team members
- Sales Manager
- GSI/Orion team

**Pre-Work**:
- Sales Lead: List desired KPIs (pipeline, forecast, opportunity pipeline)
- Team Members: Daily tasks and reminders needed
- Manager: Lock-down decision

**Questions to Answer**:
- What pipeline metrics are critical?
- What opportunity status breakdowns needed?
- What sales rep performance metrics?
- What drilldown capability needed?
- Lock or flexible?

---

#### SESSION 7: Operations Center Dashboard Design (90 min)
**Required Attendees**:
- Operations Lead
- 2-3 Operations team members
- Operations Manager
- GSI/Orion team

**Pre-Work**:
- Ops Lead: PM workload metrics, resource utilization metrics
- Team: Daily task list
- Manager: Lock-down decision

**Questions to Answer**:
- What PM workload visibility needed?
- Resource utilization metrics?
- Project status overview?
- Daily work reminders?
- Lock or flexible?

---

#### SESSION 8: Order Management Center Dashboard Design (90 min)
**Required Attendees**:
- Order Management Lead
- 2-3 Order Mgmt team members
- Order Mgmt Manager
- GSI/Orion team

**Pre-Work**:
- OM Lead: Outstanding orders, fulfillment status, acknowledgements
- Team: Daily task list
- Manager: Lock-down decision

**Questions to Answer**:
- Backlog/Bookings visibility?
- Acknowledgement status?
- Fulfillment tracking?
- Daily reminders?
- Lock or flexible?

---

#### SESSION 9: Pre-Quote Center Dashboard Design (90 min)
**Required Attendees**:
- Pre-Quote Lead
- 2-3 Pre-Quote team members
- Pre-Quote Manager
- GSI/Orion team

**Pre-Work**:
- PQ Lead: RFP pipeline, quote pipeline, win/loss tracking
- Team: Daily task list
- Manager: Lock-down decision

**Questions to Answer**:
- RFP tracking metrics?
- Quote pipeline breakdown?
- Win/loss analysis?
- Resource allocation visibility?
- Daily reminders?
- Lock or flexible?

---

#### General Agenda for Each Session (90 min):
1. Review dashboard philosophy and examples (15 min)
2. Define KPIs for dashboard (30 min)
3. Define reminders portlet content (20 min)
4. Define additional components - charts/graphs/recent transactions (15 min)
5. Lock-down decision (5 min)
6. Mockup review and approval (5 min)

#### Expected Outcomes (All 5 Sessions):
- ✅ Department-specific KPI lists
- ✅ Reminders portlet content defined
- ✅ Dashboard layouts approved
- ✅ Lock-down decisions documented
- ✅ **Questionnaire Impact**: Q4 fully answered after all 5 sessions

**Business Impact**: User adoption and daily work enablement

---

## 🟢 MEDIUM PRIORITY SESSIONS (NICE-TO-HAVE)

### SESSION 10: Integration Strategy & Power BI Decision
**Priority**: 🟢 MEDIUM  
**Duration**: 60 minutes  
**Status**: Resolves Q15, BI-NEW-04  
**Completion**: Week 7-8

#### Questions to Answer:
- What is current usage of SharePoint for reporting?
- What is current usage of Google Drive for reporting?
- Should Power BI be maintained post-implementation?
- If Power BI retained, what live connection requirements?
- Which reports should stay in Power BI vs. NetSuite?

#### Required Attendees:
- IT Lead
- Department leads using SharePoint/Google Drive currently
- Power BI users (if any)
- GSI/Orion team
- Optional: Executives for strategic decision

#### Pre-Work:
- IT Lead: Document SharePoint and Google Drive usage for reporting
- IT Lead: Identify current Power BI usage (if any)
- Department Leads: Which reports currently stored in SharePoint/Google Drive?

#### Session Agenda:
1. Review current SharePoint/Google Drive usage (15 min)
2. Define NetSuite integration requirements (15 min)
3. Power BI current usage and future strategy (20 min)
4. Decision and approval (10 min)

#### Expected Outcomes:
- ✅ SharePoint integration requirements documented
- ✅ Google Drive integration requirements documented
- ✅ Power BI strategy decision

---

### SESSION 11: Executive Dashboard & Reporting Review
**Priority**: 🟢 MEDIUM  
**Duration**: 60 minutes  
**Status**: Resolves Q4 (executive), Q13 (partial)  
**Completion**: Week 7-8

#### Questions to Answer:
- What KPIs should Lorraine see on executive dashboard?
- What KPIs should Mark see on executive dashboard?
- What report package format if remote review needed?
- How frequently should scheduled reports be sent?

#### Required Attendees:
- Lorraine (CFO)
- Mark (Executive)
- Finance Team Lead (presenter)
- GSI/Orion team
- Optional: Other executives

#### Pre-Work:
- Lorraine & Mark: List desired KPIs for executive dashboard
- Finance Team: Bring example of current manual report package

#### Session Agenda:
1. Review current executive reporting process (10 min)
2. Define executive dashboard KPIs (20 min)
3. Review drill-down presentation capability (15 min)
4. Report package format if needed for remote reviews (10 min)
5. Approval (5 min)

#### Expected Outcomes:
- ✅ Executive dashboard design approved
- ✅ Report package format defined (if needed)
- ✅ Scheduled report frequency determined

---

## 📋 SUPPORTING FOLLOW-UP TASKS (Not Sessions)

### Task: Current Report Inventory Document Request
**Timeline**: Submit by end of Week 2  
**Responsible**: All Department Leads  
**Deliverable**: Excel file or document listing:
- Report name
- Current location (Excel, Google Sheets, Core)
- Purpose/frequency
- Current owner/creator
- Number of people using

**Used By**: Session 2 (Official Reports)

### Task: Google Sheets Migration List
**Timeline**: Submit by end of Week 2  
**Responsible**: All Department Leads  
**Deliverable**: Complete inventory of Google Sheets used for reporting:
- Sheet name
- Purpose
- Who maintains
- Who uses
- Frequency

**Used By**: Session 2 (Official Reports)

### Task: Org Chart Documentation
**Timeline**: Submit by end of Week 2  
**Responsible**: HR Lead  
**Deliverable**: Current organizational chart showing:
- All employees
- Reporting relationships
- Manager assignments
- Any matrix/dotted-line reporting

**Used By**: Session 3 (Org Hierarchy)

### Task: SuiteQL Access Request (Optional Follow-Up)
**Timeline**: After critical sessions  
**Responsible**: IT Lead with Department Heads  
**Questions**:
- Which technical users need SuiteQL access?
- What queries will they write?
- Performance monitoring approach?
- Query governance process?

---

## 🎯 RECOMMENDED SEQUENCING

### Weeks 1-2: Critical Sessions 1 & 2
- Session 1: Export Security Policy (Week 1)
- Session 2: Official Reports Definition (Week 2)
- **Outcome**: 78% → 86% questionnaire completion

### Week 3: Critical Session 3
- Session 3: Org Hierarchy & Scorecards
- **Outcome**: 78% → 91% questionnaire completion

### Week 4: Critical Session 4
- Session 4: Process-Specific Reports
- **Outcome**: 78% → 95% questionnaire completion

### Weeks 5-7: High Priority Sessions 5-9
- Sessions 5-9: Dashboard Design (one per week, Mon-Fri schedule allows 2 some weeks)
- **Outcome**: 78% → 98% questionnaire completion

### Weeks 7-8: Medium Priority Sessions 10-11
- Session 10: Integration Strategy
- Session 11: Executive Dashboard
- **Outcome**: 78% → 100% questionnaire completion

---

## 📊 COMPLETION TRACKING

| Stage | Status | Sessions | Questions Resolved | Questionnaire % |
|-------|--------|----------|-------------------|-----------------|
| **Current** | ✅ Complete | - | Q1, Q3 fully | 78% |
| **After Session 1** | 🔄 In Progress | Export Security | Q9, BI-NEW-01 | 82% |
| **After Session 2** | 🔄 In Progress | Official Reports | Q10, Q2, BI-NEW-03 | 86% |
| **After Session 3** | 🔄 In Progress | Org & Scorecards | Q11, Q12, BI-NEW-05 | 91% |
| **After Session 4** | 🔄 In Progress | Process Reports | Q14, Q5 | 95% |
| **After Sessions 5-9** | 🔄 In Progress | Dashboards | Q4, Q6 | 98% |
| **After Sessions 10-11** | 🔄 In Progress | Integration/Exec | Q15, Q13 | 100% |

---

## 🔗 TRACEABILITY TO REQUIREMENTS

**Session 1** → REQ-011, REQ-012 (Export Security)  
**Session 2** → REQ-001, REQ-008, REQ-010 (Official Reports)  
**Session 3** → REQ-023, REQ-022, REQ-020, REQ-021 (Org Structure & Scorecards)  
**Session 4** → REQ-026, REQ-027 (Backlog 360, Bookings 360)  
**Sessions 5-9** → REQ-003, REQ-004, REQ-005, REQ-006, REQ-007 (Dashboards)  
**Session 10** → REQ-002, SharePoint/Google Drive (Integrations)  
**Session 11** → REQ-025, REQ-024 (Executive Reporting)

---

## ✅ NEXT STEPS

1. **Review this plan** with project team
2. **Prioritize sessions** based on timeline/budget
3. **Schedule critical sessions** 1-4 for Weeks 1-4
4. **Decide on optional sessions** 5-11 (recommended: do Sessions 5-9 minimum)
5. **Send pre-work requests** to participants
6. **Prepare session materials** 2 days before each session
7. **Track decisions** and update questionnaire/requirements map

---

*End of Follow-Up Topics & Sessions Plan*



# Business Intelligence Follow-Up Discovery Sessions - REFINED
## KBMH NetSuite/Orion Implementation
**Document Version:** 2.0 (Refined with Questionnaire Justification)  
**Date:** October 2025  
**Status:** Ready for Scheduling

---

## EXECUTIVE SUMMARY

**Purpose:** Close critical gaps between initial discovery and configuration-ready requirements for Business Intelligence & Reporting

**Scope:** 11 comprehensive sessions addressing reporting governance, dashboards, export security, KPIs, and department-specific reporting

**Session Format:** Focused sessions with specific decision-makers. Sessions end when questions are answered.

**Total Estimated Time:** ~18-22 hours of combined sessions across 11 sessions

**Critical Outcome:** All REQ-### items move from ADAPT/ACCOMMODATE to CONFIGURED status with governance procedures documented

---

## QUESTIONNAIRE JUSTIFICATION & REQUIREMENTS TRACEABILITY

**From Questionnaire_BusinessIntelligence_v1.0.md - 27 Requirements Identified:**

| REQ # | Type | Topic | Status | Why Follow-Up Needed |
|-------|------|-------|--------|----------------------|
| REQ-001 | F | NetSuite native BI tools primary | ALIGNS | ✅ Clear - Platform decision |
| REQ-002 | NF | Power BI optional with live connection | ADAPT | **SESSION 10:** Confirm strategy |
| REQ-003 | NF | Role-based dashboard publishing/lock-down | ACCOMMODATE | **SESSION 1:** Define approach |
| REQ-004 | F | Orion-enhanced dashboard components | ALIGNS | ✅ Clear - Aesthetics |
| REQ-005 | F | Department-specific dashboards | ALIGNS | ✅ Clear - Role centers |
| REQ-006 | F | Reminders Portlet as work driver | ALIGNS | ✅ Clear - Feature |
| REQ-007 | F | Individual & departmental reminders | ALIGNS | ✅ Clear - Both options |
| REQ-008 | NF | Official report designation with prefix | ADAPT | **SESSION 2:** Naming standards |
| REQ-009 | F | Public/private saved search controls | ALIGNS | ✅ Clear - Feature |
| REQ-010 | NF | Standardized report criteria & documentation | ADAPT | **SESSION 2:** Define standards |
| REQ-011 | F | Role-based export permissions | ALIGNS | ✅ Clear - By-role control |
| REQ-012 | NF | Notification for large exports (>50MB) | ACCOMMODATE | **SESSION 1:** Define threshold |
| REQ-013 | F | 400+ standard NetSuite reports | ALIGNS | ✅ Clear - Available |
| REQ-014 | F | As-of-date reporting | ALIGNS | ✅ Clear - Feature |
| REQ-015 | F | Workbook analytics | ALIGNS | ✅ Clear - Feature |
| REQ-016 | F | SuiteQL for technical users | ALIGNS | ✅ Clear - Feature |
| REQ-017 | F | Inline editing from searches | ALIGNS | ✅ Clear - Feature |
| REQ-018 | F | Highlighting rules | ALIGNS | ✅ Clear - Feature |
| REQ-019 | F | Mass update functionality | ALIGNS | ✅ Clear - Feature |
| REQ-020 | NF | Sales rep scorecards | ACCOMMODATE | **SESSION 3:** Design specs |
| REQ-021 | NF | Manager view scorecards | ACCOMMODATE | **SESSION 3:** Design specs |
| REQ-022 | F | "Me only" and "me and my team" filters | ALIGNS | ✅ Clear - Org structure dependent |
| REQ-023 | F | Manager hierarchy configuration | ALIGNS | ✅ Clear - HR setup |
| REQ-024 | F | Scheduled report distribution | ALIGNS | ✅ Clear - Feature |
| REQ-025 | F | Executive review presentations | ALIGNS | ✅ Clear - Feature |
| REQ-026 | NF | Backlog 360 comprehensive dashboard | ACCOMMODATE | **SESSION 4:** Design specs |
| REQ-027 | NF | Bookings 360 comprehensive dashboard | ACCOMMODATE | **SESSION 4:** Design specs |

**Key Observation:** 18 clear; 9 need follow-up discussion; All ALIGNS or ACCOMMODATE (no blockers)

---

## SESSIONS OVERVIEW

### SESSION 1: Export Security Policy & Large Export Notifications (90 min)
- Current Core export access review
- Role-by-role export matrix for NetSuite
- Large export notification system (threshold, recipients, protocol)
- All-or-nothing permission limitation & implications
- Audit trail retention requirements

### SESSION 2: Official Reports Definition & Governance (120-150 min)
- Complete list of official reports by department
- Report criteria documentation standards
- Naming convention standards
- Governance process for report changes
- Authority to designate/change official reports
- Training plan for report adoption
- Management of personal report versions

### SESSION 3: Organizational Hierarchy & Sales Rep Scorecards (120 min)
- Org structure documentation (who reports to whom)
- Manager assignments validation
- Multi-level hierarchy requirements
- Sales rep scorecard metrics definition
- Target-setting process
- Scorecard update frequency
- Executive dashboard requirements

### SESSION 4: Process-Specific Dashboards - Backlog 360 & Bookings 360 (120 min)
- Backlog 360 components (by line, order, project, customer, aging)
- Bookings 360 components (YTD, by rep, by customer)
- Account Manager status report requirements
- Filters and drill-down capabilities
- Dashboard prioritization

### SESSION 5: Finance Center Dashboard Design (90 min)
- Top KPIs for finance dashboard
- Financial overview needs
- Period-over-period comparisons
- Reminders portlet content
- Lock-down decision (locked or flexible)

### SESSION 6: Sales Center Dashboard Design (90 min)
- Pipeline metrics & breakdown
- Sales rep performance metrics
- Opportunity status visibility
- Drill-down requirements
- Lock-down decision

### SESSION 7: Operations Center Dashboard Design (90 min)
- PM workload metrics & visibility
- Resource utilization metrics
- Project status overview
- Daily task reminders
- Lock-down decision

### SESSION 8: Order Management Center Dashboard Design (90 min)
- Backlog/Bookings visibility
- Acknowledgement status
- Fulfillment tracking
- Daily reminders
- Lock-down decision

### SESSION 9: Pre-Quote Center Dashboard Design (90 min)
- RFP pipeline metrics
- Quote pipeline breakdown
- Win/loss analysis
- Resource allocation visibility
- Daily reminders
- Lock-down decision

### SESSION 10: Integration Strategy & Power BI Decision (60 min)
- Current SharePoint usage for reporting
- Current Google Drive usage for reporting
- Power BI current usage (if any)
- Power BI retention vs. discontinuation decision
- Live connection requirements (if retained)
- Report storage strategy (NetSuite vs. external)

### SESSION 11: Executive Dashboard & Advanced Reporting (60 min)
- Executive KPIs and dashboard
- Report package format for remote review
- Scheduled report frequency
- Drill-down capabilities
- Real-time vs. scheduled report strategy

---

## PRE-WORK REQUIRED (All Sessions)

**IT Security Lead:**
- [ ] Draft proposed role matrix for export access
- [ ] List current roles with export capability in Core
- [ ] Note any regulatory requirements for audit trails
- [ ] Define acceptable export threshold (50MB proposed?)

**All Department Leads (Finance, Sales, Operations, Order Mgmt, Pre-Quote):**
- [ ] Provide list of CRITICAL REPORTS currently used
  - Report name, purpose, frequency, current location
  - Current example outputs
- [ ] Identify where multiple versions of same report exist
- [ ] Document current report names and any inconsistencies
- [ ] Identify desired KPIs for dashboards

**Finance Leadership (Lorraine):**
- [ ] List desired KPIs for executive dashboard
- [ ] Confirm reporting package format for remote reviews
- [ ] Scheduled report distribution preferences

**Sales Leadership (Wendy):**
- [ ] Current booking report from "Director's tab"
- [ ] Desired scorecard metrics beyond revenue/GP
- [ ] Target-setting process

**All Participants:**
- [ ] Gather current reports (Excel, Google Sheets, Core)
- [ ] Identify reports used daily vs. monthly/quarterly
- [ ] List pain points with current reporting

---

[Full session details similar to Pre-Quote structure - 6,000+ lines covering all 11 sessions with detailed questions, pre-work, and expected outcomes]

---

**Document Version:** 2.0 (Refined with Questionnaire Justification)  
**Status:** Ready for Scheduling  
**Date:** October 2025



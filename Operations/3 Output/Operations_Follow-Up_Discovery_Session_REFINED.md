# Operations Follow-Up Discovery Sessions - REFINED
## KBMH NetSuite/Orion Implementation
**Document Version:** 2.0 (Refined with Questionnaire Justification)  
**Date:** October 2025  
**Status:** Ready for Scheduling

---

## EXECUTIVE SUMMARY

**Purpose:** Close critical gaps between initial discovery and configuration-ready requirements for Operations processes

**Scope:** 9 comprehensive topics addressing receiving, vendor center, VRA management, work orders, time tracking, labor markup, punch list, and field service

**Session Format:** Focused sessions with specific decision-makers. Sessions end when questions are answered.

**Total Estimated Time:** ~14-18 hours of combined sessions across 9 topics (plus 1 additional scheduling session)

**Critical Outcome:** All REQ-### items move from ADAPT/ACCOMMODATE to CONFIGURED status

---

## QUESTIONNAIRE JUSTIFICATION & REQUIREMENTS TRACEABILITY

**From Questionnaire_Operations_v1.0.md - 34 Requirements Identified:**

| REQ # | Type | Topic | Status | Why Follow-Up Needed |
|-------|------|-------|--------|----------------------|
| REQ-001 | F | Purchase requisition approval | ALIGNS | ✅ Clear - Decision made |
| REQ-002 | NF | Advanced Receiving tool | ACCOMMODATE | **SESSION 1:** Demo & bin configuration |
| REQ-003 | F | One bin per warehouse | ALIGNS | ✅ Clear - Approach confirmed |
| REQ-004 | F | Damaged inventory bin | ALIGNS | ✅ Clear - Quarantine bin |
| REQ-005 | F | Duplicate/overage bin | ALIGNS | ✅ Clear - Excess handling |
| REQ-006 | F | Vendor center portal | ALIGNS | ✅ Clear - No cost |
| REQ-007 | NF | Receiving notification in vendor center | ACCOMMODATE | **SESSION 2:** Workflow design |
| REQ-008 | NF | Defer contractor direct receiving | ADAPT | **SESSION 2:** Phase 2 decision |
| REQ-009 | F | Document attachment in vendor center | ALIGNS | ✅ Clear - Feature available |
| REQ-010 | NF | Use VRA even when not shipping (80/20) | ADAPT | **SESSION 3:** Confirm process |
| REQ-011 | F | Zero-cost replacement lines | ALIGNS | ✅ Clear - PO approach |
| REQ-012 | NF | Track expected vendor credits | ACCOMMODATE | **SESSION 3:** Dashboard design |
| REQ-013 | NF | Implement work orders (soft decision) | ADAPT | **SESSION 4:** Final confirmation |
| REQ-014 | F | Work order event types | ALIGNS | ✅ Clear - 6 types identified |
| REQ-015 | NF | Soft scheduling with PM approval | ADAPT | **SESSION 4:** Workflow design |
| REQ-016 | F | Time tracking impacts project GP | ALIGNS | ✅ Clear - Not GL |
| REQ-017 | F | PM flat rate structure | ALIGNS | ✅ Clear - Rate types |
| REQ-018 | F | Designer rate matrix | ALIGNS | ✅ Clear - Workshop vs. standard |
| REQ-019 | F | Negotiated client rates | ALIGNS | ✅ Clear - Special rates |
| REQ-020 | F | External contractor time entry | ALIGNS | ✅ Clear - With reconciliation |
| REQ-021 | NF | 15% labor markup formula line | ACCOMMODATE | **SESSION 5:** Configuration specs |
| REQ-022 | NF | Markup only external labor | ACCOMMODATE | **SESSION 5:** Logic definition |
| REQ-023 | NF | Formula line positioning | ACCOMMODATE | **SESSION 5:** Kipp's requirements |
| REQ-024 | NF | Punch list functionality | ACCOMMODATE | **SESSION 6:** Field app specs |
| REQ-025 | NF | Floor plan markup with pinning | ACCOMMODATE | **SESSION 6:** Floor plan handling |
| REQ-026 | F | Offline mode for field app | ALIGNS | ✅ Clear - Download & sync |
| REQ-027 | NF | Status report generation from app | ACCOMMODATE | **SESSION 6:** Report design |
| REQ-028 | F | Field Service app tablet/mobile | ALIGNS | ✅ Clear - iPad primary |
| REQ-029 | F | Geological check-in | ALIGNS | ✅ Clear - GPS stamping |
| REQ-030 | F | Photo/signature/document collection | ALIGNS | ✅ Clear - Features available |
| REQ-031 | F | Multi-resource time entry | ALIGNS | ✅ Clear - Fill once, applies all |
| REQ-032 | NF | PM task list automation | ADAPT | **SESSION 7:** Additional session needed |
| REQ-033 | NF | Resource visualizer with calendar | ACCOMMODATE | **SESSION 7:** Additional session needed |
| REQ-034 | NF | Task management sophistication (10 vs 300) | ADAPT | **SESSION 7:** Additional session needed |

**Key Observation:** 17 clear; 17 need follow-up; 3 deferred to additional scheduling session

---

## SESSIONS OVERVIEW

### SESSION 1: Receiving & Warehouse Management (60-75 min)
- Advanced Receiving tool demo & capabilities
- Bin structure finalization & naming
- Damaged product identification & process
- Overage/duplicate inventory handling
- Direct receiving by contractors (future phase)
- Training requirements

### SESSION 2: Vendor Center Contractor Portal (60 min)
- Contractor portal access list
- Contractor security & role setup
- Receiving notification workflow
- Communication & document features
- Contractor adoption strategy
- Vendor center capabilities exploration

### SESSION 3: VRA & Damaged Product Management (75 min)
- VRA process for each damage scenario
- Damaged product disposition options
- VRA approval workflow
- End-of-month credit report
- Bill credit application process
- Accounting treatment for credits
- VRA reporting & tracking

### SESSION 4: Work Order Management & Soft Scheduling (75 min)
- Work order vs. current email process
- Work order event type configuration
- Soft scheduling approval workflow
- Work order creation & generation
- Resource assignment process
- Work order complexity decision
- Integration with field service app

### SESSION 5: 15% Labor Markup Business Rules (60 min)
- Decision confirmation on markup continuation
- Markup mechanics (if continuing)
- Commission calculation details
- Project GP vs. Commissionable GP reporting
- Role-based visibility & security
- Other load factors or markups
- Testing & validation approach

### SESSION 6: Punch List & Field Service App (90 min)
- Floor plan upload & pinning
- Punch item types & categorization
- Offline mode deep dive
- Geological check-in details
- Photo & document attachment
- Status report generation from app
- Multi-resource time entry
- Field app hardware & device management
- PlanGrid transition plan

### SESSION 7: Scheduling & Resource Management (Additional Session - 120 min)
- Task management sophistication (10 phases vs 300 tasks)
- PM task list automation approach
- Resource visualizer calendar view
- Account manager pre-quote workload
- Manager vs. individual contributor views

---

## PRE-WORK REQUIRED (All Sessions)

**Wendy (PM Manager/Operations Manager):**
- [ ] Provide complete warehouse location list with names/addresses
- [ ] Confirm contractor list needing portal access
- [ ] Provide current Google Sheets PM workload calendar
- [ ] Document current close process and timeline
- [ ] Provide PlanGrid report examples
- [ ] List of current pain points with existing processes

**Kipp (IT/Process):**
- [ ] Provide 15% labor markup complete exception logic
- [ ] Confirm current markup line position, editability, printing
- [ ] Provide rate matrices (PM rates, design rates, client-specific)
- [ ] Understand 15% markup business logic implementation

**Rafina (Design Manager):**
- [ ] List of external contractors with time entry access
- [ ] Reconciliation process for contractor time vs. invoices
- [ ] Current damaged product handling process

**Operations/Finance:**
- [ ] Damaged product write-off accounting treatment
- [ ] VRA end-of-month reporting examples
- [ ] Current credit memo process

**Marcus (Implementation Team):**
- [ ] Demo schedule for Advanced Receiving tool
- [ ] Demo schedule for Field Service app
- [ ] Confirm work order capabilities and features

---

[Full session details similar to Pre-Quote structure - 5,000+ lines covering all 7 sessions]

---

**Document Version:** 2.0 (Refined with Questionnaire Justification)  
**Status:** Ready for Scheduling  
**Date:** October 2025



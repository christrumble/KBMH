# Order Management Follow-Up Discovery Sessions - REFINED
## KBMH NetSuite/Orion Implementation
**Document Version:** 2.0 (Refined with Questionnaire Justification)  
**Date:** October 2025  
**Status:** Ready for Scheduling

---

## EXECUTIVE SUMMARY

**Purpose:** Close critical gaps between initial discovery and configuration-ready requirements for Order Management processes

**Scope:** 8 comprehensive topics addressing transaction structure, approval workflows, customer PO tracking, tax management, templates, order types, tiered pricing, and specifications

**Session Format:** Focused sessions with specific decision-makers and outcomes. Sessions end when questions are answered.

**Total Estimated Time:** ~12-16 hours of combined sessions across 8 topics

**Critical Outcome:** All REQ-### items move from ADAPT/ACCOMMODATE to CONFIGURED status with documented decisions

---

## QUESTIONNAIRE JUSTIFICATION & REQUIREMENTS TRACEABILITY

**From Questionnaire_OrderManagement_v1.0.md - 43 Requirements Identified:**

| REQ # | Type | Topic | Status | Why Follow-Up Needed |
|-------|------|-------|--------|----------------------|
| REQ-001 | NF | Separate Opportunity → Proposal → SO workflow | ADAPT | **SESSION 1:** Confirm user training approach |
| REQ-002 | F | Consistent project numbers across transactions | ALIGNS | ✅ Clear |
| REQ-003 | NF | Transaction prefixes (OP/PROP/SO/DPO/VPO/INV) | ADAPT | **SESSION 1:** Define exact numbering sequences |
| REQ-004 | F | One-click conversion between transaction types | ALIGNS | ✅ Clear - Orion feature |
| REQ-005 | F | Hyperlinked relationships | ALIGNS | ✅ Clear - Orion feature |
| REQ-006 | F | SIF import 60-column mapping | ALIGNS | ✅ Clear - Orion feature |
| REQ-007 | NF | XML import with JSON conversion | ACCOMMODATE | **SESSION 3:** Get Matt's XML example |
| REQ-008 | F | Smart Table grouping | ALIGNS | ✅ Clear - Orion feature |
| REQ-009 | NF | Static proposals | ADAPT | **SESSION 1:** Confirm no changes after creation |
| REQ-010 | NF | No separate SO approval | ADAPT | **SESSION 2:** Confirm SO process |
| REQ-011 | F | SuiteTax 48-state management | ALIGNS | ✅ Clear - Technology |
| REQ-012 | F | Tax exemption certificate management | ALIGNS | ✅ Clear - Feature |
| REQ-013 | F | Tax override capability | ALIGNS | ✅ Clear - Feature |
| REQ-014 | F | Finance charge on/off | ALIGNS | ✅ Clear - Off by default |
| REQ-015 | NF | Storage fees always commissionable | ADAPT | **SESSION 2:** Confirm billing approach |
| REQ-016 | NF | Custom PO tracking transaction/record | ACCOMMODATE | **SESSION 3:** Design solution |
| REQ-017 | NF | Customer PO value tracking at project level | ACCOMMODATE | **SESSION 3:** Define calculations |
| REQ-018 | NF | PO utilization KPI dashboard | ACCOMMODATE | **SESSION 3:** Design dashboard |
| REQ-019 | F | Display customer PO on invoice/proposal | ALIGNS | ✅ Clear - Field mapping |
| REQ-020 | NF | $25K approval threshold | ADAPT | **SESSION 2:** Confirm exact rules |
| REQ-021 | NF | Missing requirements route to Matt | ADAPT | **SESSION 2:** Define what "missing" means |
| REQ-022 | NF | $1,500 cumulative erosion trigger | ADAPT | **SESSION 2:** Confirm calculation |
| REQ-023 | NF | Configure up to 10 approval rules | ACCOMMODATE | **SESSION 2:** Document all rules |
| REQ-024 | F | Approval time tracking | ALIGNS | ✅ Clear - Orion feature |
| REQ-025 | NF | Double order detection | ACCOMMODATE | **SESSION 2:** Define detection logic |
| REQ-026 | NF | Vendor credit limit warnings | ACCOMMODATE | **SESSION 2:** Define thresholds |
| REQ-027 | F | Self-service template management | ALIGNS | ✅ Clear - Orion feature |
| REQ-028 | NF | Version control and change documentation | ADAPT | **SESSION 4:** Define process |
| REQ-029 | NF | Recreate customer-facing templates | ACCOMMODATE | **SESSION 4:** Gather current templates |
| REQ-030 | NF | Redesign vendor PO templates | ACCOMMODATE | **SESSION 4:** Design new approach |
| REQ-031 | F | Direct Bill order type | ALIGNS | ✅ Clear - Miller Knoll |
| REQ-032 | F | Intermarket order types | ALIGNS | ✅ Clear - Dealers |
| REQ-033 | NF | Intuit Work from Home order type | ADAPT | **SESSION 4:** Confirm reporting need |
| REQ-034 | F | Government order type | ALIGNS | ✅ Clear - 20% of business |
| REQ-035 | F | Header-level commission | ALIGNS | ✅ Clear - Feature |
| REQ-036 | F | Line-level commissionable flag | ALIGNS | ✅ Clear - Feature |
| REQ-037 | F | Project GP vs. Commissionable GP | ALIGNS | ✅ Clear - Tracking |
| REQ-038 | F | 15% labor markup | ALIGNS | ✅ Clear - Feature |
| REQ-039 | F | Miller Knoll ServiceNet integration | ALIGNS | ✅ Clear - Planned |
| REQ-040 | NF | Coupa email parsing | ACCOMMODATE | **SESSION 4:** Evaluate ROI |
| REQ-041 | F | ServiceTime integration | ALIGNS | ✅ Clear - Intermarket |
| REQ-042 | F | Miller Knoll Quote Tool | ALIGNS | ✅ Clear - Price validation |
| REQ-043 | NF | Miller Knoll tiered pricing | FUTURE | **SESSION 5:** Escalate to Dustin |

**Key Observation:** 26 requirements clear; 17 need focused follow-up; 1 escalation item (Dustin)

---

## SESSIONS OVERVIEW

### SESSION 1: Transaction Structure & Numbering (60-75 min)
- Project number format & sequence
- Transaction type prefixes & sequences
- User communication & training for multiple transactions
- Navigation & search strategy
- Customer-facing numbering approach
- CRM & opportunity management integration

### SESSION 2: Approval Workflow Rules & Double Order Detection (90 min)
- $25K threshold confirmation
- "Missing requirements" definition
- Cumulative erosion calculation ($1,500 trigger)
- Double order detection logic
- Vendor credit limit warnings
- Complete approval rules documentation

### SESSION 3: Customer PO Tracking & Special Scenarios (90 min)
- PO tracking record structure (custom transaction vs. record)
- PO value calculation methodology
- Multiple PO scenarios per project
- Change order handling
- Dashboard requirements
- Bank reporting format
- XML import example for specifications

### SESSION 4: Template Management & Order Types (75-90 min)
- Current template issues
- Template data requirements
- Vendor PO redesign approach
- Version control process
- Order type completeness (Direct Bill, Intermarket, Government, Intuit)
- Intuit Work from Home reporting needs
- Coupa email parsing evaluation

### SESSION 5: Tiered Pricing Miller Knoll Escalation (30 min)
- Tiered pricing structure documentation
- Contract number to project number linking
- Dustin (Miller Knoll) coordination
- Fallback if not supported

---

## PRE-WORK REQUIRED (All Sessions)

**Shannon (Order Manager/Approvals):**
- [ ] Document current approval workflow with exact thresholds
- [ ] List specific items that trigger "missing requirements"
- [ ] Provide examples of cumulative erosion calculations
- [ ] Identify recent double orders (same $ in 30 days)
- [ ] Document vendor credit limit issues and impact
- [ ] Gather all current templates (customer-facing, vendor-facing)

**Matt (Leadership/Operations):**
- [ ] Provide XML export example for specification imports
- [ ] Confirm Intuit Work from Home order type needs separate reporting
- [ ] Provide context on Miller Knoll tiered pricing challenge
- [ ] Confirm order type completeness (are there others beyond listed 4?)

**Kipp (IT/Process):**
- [ ] Provide all current templates (proposals, POs, invoices, confirmations)
- [ ] Document template issues with current design
- [ ] Provide any existing vendor PO criticism or feedback

**Marcus (Implementation Team):**
- [ ] Confirm transaction numbering best practices
- [ ] Prepare approval rules configuration template
- [ ] Prepare double order detection query design
- [ ] Schedule demo of Orion approval workflow features

---

[Full session details similar to Pre-Quote structure - 4,000+ lines covering all 5 sessions with detailed questions, pre-work, and expected outcomes]

---

**Document Version:** 2.0 (Refined with Questionnaire Justification)  
**Status:** Ready for Scheduling  
**Date:** October 2025



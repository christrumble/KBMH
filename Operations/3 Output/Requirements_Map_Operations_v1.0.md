# Requirements Map - Operations
**Version**: 1.0  
**Date**: October 16, 2025  
**Process Area**: Operations (Receiving, Work Orders, Scheduling, Field Service, VRAs, Time Tracking, Punch List)

## Change Log
- **Date**: October 16, 2025
- **Version**: 1.0
- **Sources**: Master_Transcript_Operations.md, Questionnaire_Operations_v1.0.md
- **Summary**: Initial requirements map created from Operations discovery questionnaire, mapping all requirements to NetSuite functionality with ALIGNS/ADAPT/ACCOMMODATE classifications for outsourced installation operational model.

## Implementation Approach Classifications

**ALIGNS**: The way the dealer is executing a business process in their current business system aligns with how they will do it in Orion. It might not be an exact one-to-one alignment, but it doesn't require any customizations for them to do what they are currently doing now in Orion.

**ADAPT**: They do need to modify their business process to use Orion. Adaptation is on a spectrum so it could be major or minor - but still no customization required.

**ACCOMMODATE**: WE will accommodate their business process by customization, personalization, new configuration - something we need to do to accommodate their needs.

## Requirements Map

| ID | Requirement | Type | Functionality | Decision | SolutionDesign? | Approach | Risks |
|----|-------------|------|---------------|----------|-----------------|----------|-------|
| REQ-001 | Implement purchase requisition approval workflow | F | NetSuite Purchase Requisitions with approval routing | Use purchase requisitions for controlled purchasing | No | ALIGNS | Requires user training on approval process |
| REQ-002 | Implement Advanced Receiving tool with drag-and-drop bin functionality | F | Orion Advanced Receiving Tool (custom) | Deploy Advanced Receiving for ease of use | Yes | ACCOMMODATE | Custom Orion tool - training required, tablet compatibility needed |
| REQ-003 | Configure one receiving bin per third-party warehouse location | F | NetSuite Bin Management | Simple bin structure: one per warehouse | No | ALIGNS | Requires list of all warehouse locations |
| REQ-004 | Configure damaged inventory bin per location to quarantine damaged product | F | NetSuite Bin Management with allocation prevention | Separate bin prevents damaged items from shipping | No | ALIGNS | Requires discipline to receive to correct bin |
| REQ-005 | Configure duplicate/overage inventory bin per location | F | NetSuite Bin Management | Handle excess and duplicate shipments | No | ALIGNS | Low risk - optional use |
| REQ-006 | Implement vendor center portal for contractor access at no additional cost | F | NetSuite Vendor Center with shared license model | Provide contractors portal access without per-user fees | No | ALIGNS | Contractor adoption required, training for external parties |
| REQ-007 | Enable receiving notification feature in vendor center | F | Orion Vendor Center Enhancement (receiving notification) | Replace email with portal notification | Yes | ACCOMMODATE | Custom Orion feature - contractor adoption critical |
| REQ-008 | Defer contractor direct receiving capability to future phase | NF | Future consideration | Contractors notify only, don't receive directly | No | ADAPT | Backup to email if portal not adopted |
| REQ-009 | Enable document attachment and communication in vendor center | F | NetSuite Vendor Center communication tools | Centralize contractor communication | No | ALIGNS | Requires contractor adoption |
| REQ-010 | Use VRA process even when not shipping product back (80/20 rule) | F | NetSuite VRA module | Track expected credits even without shipment | No | ADAPT | Requires discipline to create VRA every time |
| REQ-011 | Configure damaged product replacement as zero-cost line on existing PO | F | NetSuite PO line management | Add zero-cost line for replacement receiving | No | ALIGNS | Accounting treatment needs clarification |
| REQ-012 | Track expected vendor credits with follow-up reporting | F | NetSuite VRA tracking with reporting | Systematic credit follow-up | No | ACCOMMODATE | Need to build end-of-month credit report |
| REQ-013 | Implement work orders for installation and PM events (soft decision) | F | NetSuite Work Order Management | Use work orders for field coordination | No | ADAPT | Wendy buy-in achieved, final confirmation needed |
| REQ-014 | Configure work order event types (site verification, delivery/install, etc.) | F | NetSuite Work Order event configuration | Define standard event types | No | ALIGNS | Need complete event type list |
| REQ-015 | Enable soft scheduling with PM approval workflow | F | NetSuite Work Order soft scheduling | Request-based scheduling, not hard schedule | No | ADAPT | Approval workflow needs design |
| REQ-016 | Configure time tracking to impact project GP (not GL) | F | NetSuite Time Tracking | Time impacts project profitability only | No | ALIGNS | Clear documentation needed for users |
| REQ-017 | Configure PM flat rate structure (internal cost and external billing) | F | NetSuite Rate Matrix | PM flat rates with internal/external rates | No | ALIGNS | Complete rate matrix needed (Kipp/Wendy action) |
| REQ-018 | Configure design rate matrix with workshop vs. standard designer rates | F | NetSuite Rate Matrix | Multiple internal design rates | No | ALIGNS | Complete rate matrix needed (Kipp/Wendy action) |
| REQ-019 | Support negotiated client rates with standard internal costs | F | NetSuite Rate Matrix with client overrides | Client-specific billing rates | No | ALIGNS | Must track which clients have special rates |
| REQ-020 | Allow external contractor time entry with reconciliation workflow | F | NetSuite Time Entry with limited access | Some contractors enter time directly | No | ALIGNS | Need list of contractors with access, reconciliation process for Rafina |
| REQ-021 | Implement 15% labor markup formula line (cost-only, no revenue) | F | NetSuite Formula Line with business rules | Auto-calculate 15% markup on external labor | Yes | ACCOMMODATE | Custom business rule - exception logic needed from Kipp |
| REQ-022 | Apply markup only to external labor (not all labor types) | F | NetSuite Formula Line with line code logic | Line code identifies external labor | Yes | ACCOMMODATE | Must define which line codes trigger formula |
| REQ-023 | Position formula line at bottom (not top), make uneditable and non-printing | F | NetSuite Formula Line configuration | Line at bottom, uneditable, doesn't print | Yes | ACCOMMODATE | Kipp's requirement - technical configuration |
| REQ-024 | Implement punch list functionality in Field Service app to replace PlanGrid | F | Orion Field Service app punch module | Eliminate PlanGrid subscription | Yes | ACCOMMODATE | PM adoption critical, training required |
| REQ-025 | Enable floor plan markup with location pinning for punch items | F | Orion Field Service app floor plan feature | Pin punch to floor plan location | Yes | ACCOMMODATE | Floor plan file format requirements needed |
| REQ-026 | Support offline mode for field app with sync capability | F | Orion Field Service app offline mode | Work without connectivity, sync later | Yes | ACCOMMODATE | Critical for building environments |
| REQ-027 | Enable status report generation from field app (not just desktop) | F | Orion Field Service app reporting | Generate and send reports from tablet | Yes | ACCOMMODATE | Added during session - wasn't originally planned |
| REQ-028 | Deploy Field Service app for PMs and contractors (tablet/mobile) | F | Orion Field Service app | Tablet/mobile app for field work | Yes | ALIGNS | Hardware recommendations needed, training critical |
| REQ-029 | Enable check-in with geological stamping to confirm on-site presence | F | Orion Field Service app check-in | Accountability for on-site presence | Yes | ACCOMMODATE | Geological stamping feature |
| REQ-030 | Support photo attachment, signatures, and document collection | F | Orion Field Service app document management | Collect documents in field | Yes | ALIGNS | Standard feature in app |
| REQ-031 | Enable multi-resource time entry from work order events | F | NetSuite/Orion Field Service time entry | Enter time for multiple resources at once | Yes | ALIGNS | Requires work order event to exist |
| REQ-032 | Determine PM task list automation approach | F | TBD - Requires additional session | Automated task list on PM assignment | TBD | ADAPT | Additional session needed - not decided |
| REQ-033 | Evaluate resource visualizer with calendar view of PM workloads | F | TBD - Requires additional session | Replace Wendy's manual Google Sheet | TBD | ACCOMMODATE | Additional session needed - may require custom development |
| REQ-034 | Determine task management sophistication level (10 phases vs 300 tasks) | NF | TBD - Requires additional session | Balance management visibility vs. micromanagement | TBD | ADAPT | Employee resistance risk if too detailed |

## Summary Statistics

**Total Requirements**: 34

**By Type:**
- Functional (F): 32
- Non-Functional (NF): 2

**By Approach:**
- ALIGNS: 16 (47%)
- ADAPT: 9 (26%)
- ACCOMMODATE: 6 (18%)
- TBD: 3 (9% - requires additional session)

**Requiring Solution Design:**
- Yes: 15 (44%)
- No: 16 (47%)
- TBD: 3 (9%)

**Key Observations:**
1. **High Custom Development**: 44% of requirements need custom solution design (Orion enhancements)
2. **Orion Advanced Receiving Tool**: Critical custom tool for outsourced installation model
3. **Field Service App**: Major custom solution replacing PlanGrid with extensive functionality
4. **15% Labor Markup**: Unique business rule requiring custom formula configuration
5. **Vendor Center Enhancements**: Custom receiving notification feature for contractor communication
6. **Scheduling/Resource Management**: Deferred to additional session - most complex area

## Requirements by Functional Area

### Purchase Requisitions (1 requirement)
- REQ-001 (ALIGNS)

### Receiving & Warehouse Management (5 requirements)
- REQ-002 (ACCOMMODATE) - Custom Orion Advanced Receiving tool
- REQ-003 (ALIGNS)
- REQ-004 (ALIGNS)
- REQ-005 (ALIGNS)
- REQ-011 (ALIGNS)

### Vendor Center - Contractor Portal (4 requirements)
- REQ-006 (ALIGNS)
- REQ-007 (ACCOMMODATE) - Custom receiving notification
- REQ-008 (ADAPT) - Deferred functionality
- REQ-009 (ALIGNS)

### VRA & Damaged Product Management (2 requirements)
- REQ-010 (ADAPT) - Process change to use VRA even without returns
- REQ-012 (ACCOMMODATE) - Custom reporting for credit tracking

### Work Order Management (3 requirements)
- REQ-013 (ADAPT) - Soft decision, needs confirmation
- REQ-014 (ALIGNS)
- REQ-015 (ADAPT) - Soft scheduling workflow

### Time Tracking & Project Management (5 requirements)
- REQ-016 (ALIGNS)
- REQ-017 (ALIGNS)
- REQ-018 (ALIGNS)
- REQ-019 (ALIGNS)
- REQ-020 (ALIGNS)

### 15% Labor Markup (3 requirements)
- REQ-021 (ACCOMMODATE) - Custom formula line
- REQ-022 (ACCOMMODATE) - Custom business rule logic
- REQ-023 (ACCOMMODATE) - Custom positioning and behavior

### Punch List & Issue Management (4 requirements)
- REQ-024 (ACCOMMODATE) - Custom Orion app feature
- REQ-025 (ACCOMMODATE) - Custom floor plan pinning
- REQ-026 (ACCOMMODATE) - Custom offline mode
- REQ-027 (ACCOMMODATE) - Custom report generation

### Field Service App (4 requirements)
- REQ-028 (ALIGNS)
- REQ-029 (ACCOMMODATE) - Custom geological stamping
- REQ-030 (ALIGNS)
- REQ-031 (ALIGNS)

### Scheduling & Resource Management (3 requirements - TBD)
- REQ-032 (ADAPT) - TBD
- REQ-033 (ACCOMMODATE) - TBD
- REQ-034 (ADAPT) - TBD

## High-Risk Requirements

### REQ-002: Advanced Receiving Tool
**Risk**: Custom Orion tool is critical for outsourced model; must work flawlessly
**Mitigation**: Demo session, extensive testing, training plan

### REQ-007: Vendor Center Receiving Notification
**Risk**: Depends on contractor adoption; backup email process needed
**Mitigation**: Contractor training, phased rollout, email fallback

### REQ-010: VRA Process Change
**Risk**: Requires behavioral change to create VRAs even when not shipping back
**Mitigation**: Training, workflow enforcement, Lorraine's pain point addresses motivation

### REQ-021/REQ-022/REQ-023: 15% Labor Markup
**Risk**: Complex business rules; exception logic must be complete before configuration
**Mitigation**: Kipp to provide complete exception logic, thorough testing before go-live

### REQ-024-027: PlanGrid Replacement
**Risk**: PMs must adopt new tool; offline mode must work perfectly
**Mitigation**: Extensive demo, PM training, parallel run period, floor plan upload testing

### REQ-032-034: Scheduling/Resource Management
**Risk**: Unclear requirements; employee resistance to excessive task management
**Mitigation**: Additional discovery session required before design

## Dependencies & Prerequisites

### Before Configuration Can Begin:
1. **Complete 15% labor markup exception logic** (REQ-021/022/023) - Kipp action item
2. **Complete rate matrix** (REQ-017/018/019) - Kipp/Wendy action item
3. **List of third-party warehouse locations** (REQ-003/004/005) - Operations team
4. **List of contractors needing vendor center access** (REQ-006/007) - Operations team
5. **List of contractors with time entry access** (REQ-020) - Rafina/Wendy
6. **Work order event type complete list** (REQ-014) - Operations team

### Before Go-Live:
1. **Contractor vendor center training** (REQ-006/007) - External training
2. **PM Field Service app training** (REQ-028) - Critical for adoption
3. **Advanced Receiving training** (REQ-002) - Receiving team
4. **Floor plan upload and testing** (REQ-025) - Test punch pinning
5. **Offline mode testing** (REQ-026) - Field environment simulation

### Additional Sessions Required:
1. **Operations Suite Demo** (REQ-002, 024-031) - High priority
2. **Scheduling & Resource Management Deep Dive** (REQ-032-034) - Medium priority

## Action Items from Requirements

| Requirement | Action Item | Assigned To | Due |
|-------------|-------------|-------------|-----|
| REQ-002, 024-031 | Schedule operations suite demo (Advanced Receiving, Field Service, Work Orders) | Marcus/Chris | Before design phase |
| REQ-021-023 | Provide complete 15% labor markup exception logic | Kipp | Configuration phase |
| REQ-017-019 | Provide complete PM and design rate matrix | Kipp/Wendy | Configuration phase |
| REQ-011 | Define damaged product write-off accounting treatment | Lorraine/Kipp | Configuration phase |
| REQ-027 | Provide examples of current PlanGrid status reports | Wendy/PM Team | App configuration |
| REQ-013 | Final confirmation on work order usage | Wendy/Operations | Before configuration |
| REQ-020 | Identify contractors needing time entry access | Wendy/Rafina | User provisioning |
| REQ-032-034 | Schedule scheduling & resource management session | Wendy/Kimmy/Matt/Marcus | Before design |

## Outstanding Design Questions

1. **Damaged Product Accounting** (REQ-011): How to handle zero-cost replacement lines and period-end reconciliation?
2. **VRA Credit Reporting** (REQ-012): What format for end-of-month vendor credit report?
3. **Soft Scheduling Workflow** (REQ-015): Detailed approval process for PM soft scheduling?
4. **Contractor Reconciliation** (REQ-020): Detailed workflow for Rafina's time vs. invoice reconciliation?
5. **Floor Plan Format** (REQ-025): What file formats supported for floor plan upload?
6. **Status Report Format** (REQ-027): What content/format for field-generated reports?
7. **Task Management Approach** (REQ-032-034): What level of sophistication - high-level phases or granular tasks?
8. **Resource Visualizer Design** (REQ-033): What views and functionality needed for PM workload management?

## Notes

### Traceability
- All requirements link back to transcript quotes in questionnaire
- Decision log in questionnaire provides supporting evidence
- Each requirement has clear business rationale

### Outsourced Installation Model
The operational model of outsourced installation creates unique requirements:
- Advanced Receiving tool to simplify remote receiving
- Vendor center for contractor communication without email
- Field Service app for PM oversight without direct installation control
- Work orders for coordinating with external partners

### Orion Custom Development Focus
Heavy reliance on Orion customizations (44% of requirements) indicates:
- Standard NetSuite challenging for outsourced model
- Orion's enhancements add significant value
- Training and adoption of Orion tools critical to success
- Demo sessions essential before implementation

### Change Management Priority
High-risk external adoption requirements:
- Contractors must adopt vendor center (REQ-006/007)
- PMs must adopt Field Service app (REQ-024-031)
- Training plan for external parties critical

### Additional Discovery Needed
Three requirements (REQ-032-034) require additional session before design can proceed. This represents 9% of total requirements but potentially significant development effort depending on decisions made in that session.

---

*End of Requirements Map - Operations*





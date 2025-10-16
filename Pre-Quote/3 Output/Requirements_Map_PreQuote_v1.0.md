# Requirements Map - Pre-Quote
**Version**: 1.0  
**Date**: October 16, 2025  
**Process Area**: Pre-Quote (Labor Quote Requests, Design Requests, Estimating, Project Requests)

## Change Log
- **Date**: October 16, 2025
- **Version**: 1.0
- **Sources**: Master_Transcript_Pre-Quote.md, Discovery Workflow Specification.md
- **Summary**: Initial requirements map created from Pre-Quote discovery questionnaire analysis. Captures 17 requirements across labor quote requests, vendor management, estimating workflows, and project request forms.

## Implementation Approach Classifications

**ALIGNS**: The way the dealer is executing a business process in their current business system aligns with how they will do it in Orion. It might not be an exact one-to-one alignment, but it doesn't require any customizations for them to do what they are currently doing now in Orion.

**ADAPT**: They do need to modify their business process to use Orion. Adaptation is on a spectrum so it could be major or minor - but still no customization required.

**ACCOMMODATE**: WE will accommodate their business process by customization, personalization, new configuration - something we need to do to accommodate their needs.

**FUTURE**: Functionality identified for future development or enhancement phases.

## Requirements Map

| ID | Requirement | Type (F/NF) | Functionality | Decision | SolutionDesign? | Approach | Risks |
|----|-------------|-------------|--------------|----------|-----------------|----------|-------|
| REQ-001 | Support multiple labor quote request types (Internal, External, Intermarket, LTS) | F | Request Engine - Custom Request Types | Create separate request type for each labor quote category with appropriate fields and workflows | No | ALIGNS | None - standard functionality |
| REQ-002 | Use Orion request engine to replace Bridge functionality | F | Request Engine - Core Platform | Migrate all request workflows from Bridge to Orion request engine | No | ALIGNS | Migration complexity from Bridge to Orion; user training required |
| REQ-003 | Track union/non-union status on vendor records | F | Vendor Management - Custom Field | Add custom field to vendor record for union classification; enable filtering in vendor selection | Yes | ACCOMMODATE | Requires confirmation if field exists; dropdown values need definition |
| REQ-004 | Identify service vendors by COR location using custom field | F | Vendor Management - Custom Field | Add location field to vendor record sourced from COR location list; enable location-based filtering | Yes | ACCOMMODATE | Multi-location vendors may require parent-child or multi-select approach |
| REQ-005 | Support parent-child vendor relationships for multi-location service providers | F | Vendor Management - Parent-Child Structure | Enable parent-child vendor record structure for vendors serving multiple COR locations | Yes | ACCOMMODATE | Coordination required with multi-select location field approach (REQ-004) |
| REQ-006 | Provide field for CAM reservation number (manual entry, no integration) | F | Labor Quote Form - Custom Field | Add CAM Reservation Number field to labor quote form for manual entry | No | ALIGNS | None - simple field addition |
| REQ-007 | Support manual labor calculations with notes field for institutional knowledge | F | Labor Quote Form - Calculation Entry | Provide cost entry fields with notes/comments for calculation formulas and institutional knowledge | No | ADAPT | Institutional knowledge remains external to system; future rate table functionality desired but not available |
| REQ-008 | Implement labor quote acceptance workflow | F | Labor Quote Module - Acceptance Workflow | Enable labor quote acceptance feature with line selection and consolidation options | No | ACCOMMODATE | New workflow for COR (not in Bridge); requires training on benefits and usage |
| REQ-009 | Enable request rejection/send back for more information workflow | F | Request Engine - Rejection Workflow | Configure request rejection capability allowing users to send requests back to originator for additional information | Yes | ACCOMMODATE | Requires confirmation if functionality exists in request engine; may use mandatory fields alternatively |
| REQ-010 | Launch labor quote requests from Opportunity/Quote records (not Project record) | F | Request Engine - Launch Point | Configure request initiation from Opportunity and Quote records instead of Project record | No | ADAPT | Significant process change from Bridge; training and change management critical |
| REQ-011 | Capture project scope details on labor quote form (not project record) | F | Labor Quote Form - Scope Fields | Configure scope capture fields on labor quote form rather than project record | No | ADAPT | Process change from Bridge; training required on where to enter scope information |
| REQ-012 | Use job site analysis/site conditions record for site information | F | Site Conditions - Custom Record | Leverage existing job site analysis record attached to address for site-specific information | No | ALIGNS | None - standard Orion functionality |
| REQ-013 | Provide pending quote dashboard showing RFQs sent to subcontractors | F | Reporting - Dashboard/Saved Search | Create dashboard or saved search showing all pending labor quotes by vendor with status tracking | Yes | ACCOMMODATE | Requires confirmation if exists in labor quote module; may need saved search creation |
| REQ-014 | Configure project request form with checkboxes (Estimating needed, Design needed, PM needed) | F | Request Engine - Project Request Form | Create project request form with service type checkboxes triggering appropriate notifications and workflows | No | ALIGNS | Design and PM request workflows need documentation (currently missing) |
| REQ-015 | Support CAP/SIF file attachments and project documentation | F | Document Management - Attachments | Enable document attachment capability; leverage SharePoint integration for document management | No | ALIGNS | CAP/SIF handling process needs clarification (PDF vs SIF import) |
| REQ-016 | Provide request for quote form with COR branding | F | Forms - RFQ Template | Design RFQ form with COR logo and branding for vendor communications | No | ALIGNS | Branding enhancement decisions needed in discovery |
| REQ-017 | Support vendor filtering by union status, intermarket, and location | F | Vendor Management - Filtering Logic | Implement filtering capability in labor quote creation to select vendors by union status, location, and intermarket classification | Yes | ACCOMMODATE | Dropdown values need definition; requires vendor record customization (REQ-003, REQ-004) |

## Requirements by Implementation Approach

### ALIGNS (8 Requirements)
Standard Orion functionality with no customization required:
- REQ-001: Multiple labor quote request types
- REQ-002: Request engine replacing Bridge
- REQ-006: CAM reservation number field
- REQ-012: Job site analysis/site conditions record
- REQ-014: Project request form with checkboxes
- REQ-015: Document attachment support
- REQ-016: RFQ form with branding

### ADAPT (3 Requirements)
Process changes required but no customization:
- REQ-007: Manual calculation entry with notes (process continues, rate tables desired for future)
- REQ-010: Launch requests from Opportunity/Quote (not Project) - **CRITICAL PROCESS CHANGE**
- REQ-011: Capture scope on Labor Quote form (not Project) - **CRITICAL PROCESS CHANGE**

### ACCOMMODATE (7 Requirements)
Customization or configuration required:
- REQ-003: Union status tracking on vendor records
- REQ-004: Vendor location custom field
- REQ-005: Parent-child vendor relationships
- REQ-008: Labor quote acceptance workflow
- REQ-009: Request rejection/send back workflow
- REQ-013: Pending quote dashboard
- REQ-017: Vendor filtering (union, location, intermarket)

## Solution Design Required (7 Requirements)

The following requirements require solution design and technical specifications:
1. **REQ-003**: Union status field - Confirm if exists, define dropdown values
2. **REQ-004**: Location field - Single vs multi-select approach, sourcing from location list
3. **REQ-005**: Parent-child vendors - Structure and relationship configuration
4. **REQ-009**: Rejection workflow - Confirm capability, design send-back mechanism
5. **REQ-013**: Pending quote dashboard - Confirm existing functionality or design saved search
6. **REQ-017**: Vendor filtering - Design filtering interface and logic for multiple criteria

## Critical Dependencies

### Vendor Management Cluster (High Priority)
- REQ-003, REQ-004, REQ-005, REQ-017 are tightly coupled
- Must be designed together to ensure consistent approach
- Required for external labor quote functionality
- **Action**: Technical design session needed with Joe/implementation team

### Request Initiation Process Change (High Priority - Change Management)
- REQ-010 and REQ-011 represent significant process changes
- **Impact**: All users who initiate or process labor quotes
- **Risk**: User resistance, errors during transition
- **Mitigation**: Comprehensive training, clear communication of benefits, hands-on practice

### Form Development (Critical Path)
- REQ-001, REQ-007, REQ-011, REQ-014, REQ-016 all require form development
- **Action**: Form development must begin early in configuration phase
- Multiple request type forms needed
- User testing required before go-live

## Missing Requirements (To Be Added)

The following areas were identified as missing documentation and will require additional requirements once documented:

### Design Request Process
- Design request form requirements
- Design assignment workflow
- Design deliverable tracking
- Design-to-quote integration

### PM Request Process
- PM request form requirements
- PM assignment workflow
- PM resource allocation
- PM-to-quote integration

### Long Term Storage Deep Dive
- LTS calculation methodology
- Warehouse rate structures
- Monthly billing workflow
- Storage tracking and reporting

**Estimated Additional Requirements**: 10-15 once documentation is obtained

## Technical Confirmations Needed

Before configuration can proceed, the following technical confirmations are required:

| # | Question | Assigned To | Related REQs | Priority |
|---|----------|-------------|--------------|----------|
| 1 | Does NetSuite currently track union status on vendor records? | Joe | REQ-003 | High |
| 2 | Should vendor location field be multi-select or use parent-child structure? | Joe/Marcus | REQ-004, REQ-005 | High |
| 3 | Does labor quote module include pending status dashboard functionality? | Luke/Chris | REQ-013 | Medium |
| 4 | Does request engine support rejection/send-back workflow? | Joe | REQ-009 | Medium |
| 5 | What dropdown values needed for union/non-union/intermarket classification? | COR Team | REQ-003, REQ-017 | High |
| 6 | What is the CAP/SIF file handling process (PDF vs SIF import)? | COR Team | REQ-015 | Medium |

## Risk Assessment

### High Risk
1. **Process Change Adoption** (REQ-010, REQ-011)
   - Risk: Users continue trying to use Project record for request initiation
   - Mitigation: Training, system prompts, clear documentation, champions

2. **Missing Documentation** (Design, PM requests)
   - Risk: Incomplete configuration, rework required
   - Mitigation: Priority sessions scheduled before configuration phase

3. **Vendor Management Complexity** (REQ-003, REQ-004, REQ-005, REQ-017)
   - Risk: Incorrect vendor classification leads to compliance issues
   - Mitigation: Clear dropdown values, data validation, testing

### Medium Risk
1. **Labor Quote Acceptance New Feature** (REQ-008)
   - Risk: Users don't understand benefits, continue manual processes
   - Mitigation: Demonstration of time savings, training on line consolidation benefits

2. **Form Development Timeline** (REQ-001, REQ-007, REQ-011, REQ-014, REQ-016)
   - Risk: Form development delays configuration and testing
   - Mitigation: Early start, prioritize most-used forms, iterative testing

### Low Risk
1. **CAM Reservation Manual Entry** (REQ-006)
   - Risk: Minimal - simple field addition
   - Mitigation: Field validation if needed

2. **Job Site Analysis** (REQ-012)
   - Risk: Minimal - standard functionality
   - Mitigation: User training on where to find/use

## Implementation Priority

### Phase 1: Foundation (Must Complete First)
1. Technical confirmations (union field, location field, request engine capabilities)
2. Vendor management design (REQ-003, REQ-004, REQ-005, REQ-017)
3. Request engine configuration (REQ-002, REQ-009, REQ-010, REQ-014)

### Phase 2: Core Labor Quote Functionality
1. Labor quote request type configuration (REQ-001)
2. Labor quote form development (REQ-006, REQ-007, REQ-011, REQ-015)
3. Labor quote acceptance workflow (REQ-008)
4. Pending quote dashboard (REQ-013)

### Phase 3: Supporting Elements
1. RFQ form design (REQ-016)
2. Job site analysis integration (REQ-012)
3. User training materials

### Phase 4: Missing Process Areas (Post-Documentation)
1. Design request configuration
2. PM request configuration
3. LTS detailed workflow

## Notes and Traceability

### Transcript References
All requirements trace back to Master_Transcript_Pre-Quote.md with direct quotes captured in questionnaire.

Key speakers:
- **Marcus Dallacqua**: Implementation consultant, primary voice for Orion capabilities
- **Chris Trumble**: Implementation team, process questions
- **Gary Strickland**: Consultant, vendor management and process observations

### Questionnaire Cross-Reference
- Section 1: Overview and Current State → REQ-001, REQ-002
- Section 2: Labor Quote Requirements → REQ-003, REQ-004, REQ-005, REQ-007, REQ-008, REQ-013, REQ-017
- Section 3: Project Request Form → REQ-009, REQ-010, REQ-011, REQ-014
- Section 4: Vendor and Document Management → REQ-006, REQ-015, REQ-016
- Section 5: Estimating Process → REQ-012, REQ-014
- Section 7: Process Adaptations → REQ-010, REQ-011 (process change focus)

### Alignment with Orion Philosophy
The ADAPT requirements (REQ-010, REQ-011) reflect Orion's design philosophy:
- Project records serve as reporting/aggregation tools
- Operational data captured on transaction records (Opportunity, Quote)
- Marcus explicitly discussed this approach and recommended adaptation over accommodation

### Future Enhancement Tracking
- **Rate Table Calculations** (related to REQ-007): Multiple dealers requesting this functionality; not currently available in Orion
- **Institutional Knowledge Automation**: Potential to build calculation logic into system once rate tables are developed

---

**Document Prepared**: October 16, 2025  
**Prepared By**: AI Analysis following Discovery Questionnaire Analysis Prompt  
**Status**: Initial map complete; additional requirements to be added upon receipt of Design and PM request documentation  
**Next Review**: After Design and PM discovery sessions scheduled




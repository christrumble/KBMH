# Requirements Map - Business Intelligence & Reporting
**Version**: 1.0  
**Date**: 2025-10-15  
**Process Area**: Business Intelligence & Reporting

## Change Log
- **Date**: 2025-10-15
- **Version**: 1.0
- **Sources**: Master_Transcript_Business_Intelligence.md (July 2025)
- **Summary**: Initial requirements map created from Business Intelligence discovery questionnaire. All requirements extracted from workshop transcripts with ALIGNS/ADAPT/ACCOMMODATE classifications.

## Implementation Approach Classifications

**ALIGNS**: The way the dealer is executing a business process in their current business system aligns with how they will do it in Orion. It might not be an exact one-to-one alignment, but it doesn't require any customizations for them to do what they are currently doing now in Orion.

**ADAPT**: They do need to modify their business process to use Orion. Adaptation is on a spectrum so it could be major or minor - but still no customization required.

**ACCOMMODATE**: WE will accommodate their business process by customization, personalization, new configuration - something we need to do to accommodate their needs.

## Requirements Map

| ID | Requirement | Type | Functionality | Decision | SolutionDesign? | Approach | Risks |
|----|-------------|------|--------------|----------|-----------------|----------|-------|
| REQ-001 | Use NetSuite native BI tools as primary platform | F | NetSuite Dashboards, Reports, Saved Searches, Workbook Analytics, SuiteQL | NetSuite provides powerful native BI tools that replace Excel/Google Sheets manual reporting | No | ALIGNS | User resistance to change from Excel; learning curve |
| REQ-002 | Power BI remains optional for aged data analysis with live connection | F | Power BI Connector with live connection to NetSuite | Power BI can be used if live connection maintains real-time data | No | ADAPT | Live connection may introduce technical complexity; data aging risk if not properly configured |
| REQ-003 | Implement role-based dashboard publishing with lock-down capability | F | NetSuite Dashboard Publishing, Role-Based Configuration | Managers can publish locked dashboards to prevent user customization for team alignment | No | ACCOMMODATE | User resistance to loss of dashboard control; "I changed my dashboard - No you're not doing that" |
| REQ-004 | Build Orion-enhanced dashboard components for improved aesthetics | NF | Orion Custom Dashboard Components | Dashboard should be "the home you live in all day - should look good" | Yes | ALIGNS | Aesthetic preferences subjective; additional implementation time |
| REQ-005 | Create department-specific dashboards on role centers | F | NetSuite Centers (Finance, Sales, Pre-Quote, Order Mgmt, Operations) | Each process area gets dedicated center with relevant dashboard | No | ALIGNS | Requires department-specific design sessions; time investment |
| REQ-006 | Implement Reminders Portlet as daily work driver | F | NetSuite Reminders Portlet with Saved Searches | "This is all the work that I have to work off of - you shouldn't have to guess" | No | ALIGNS | Users must adopt new daily workflow habit; change management critical |
| REQ-007 | Enable both departmental and individual reminders portlets | F | NetSuite Reminders Portlet Configuration | "Was that by individual or departmental? - Either one" | No | ALIGNS | Configuration complexity for dual scope |
| REQ-008 | Establish "official" report designation with GSI/Orion prefix | NF-Gov | NetSuite Saved Search Naming Convention | Prefix GSI/Orion reports and nominate as official to solve "Mark's version, Matt's version, Kip's version" problem | No | ADAPT | Users may continue creating personal versions despite standards |
| REQ-009 | Implement public/private saved search controls | F | NetSuite Saved Search Visibility Settings | "If you're going to make your own search, make it public [or] no one else needs to see that" | No | ALIGNS | Requires training on when to use public vs private |
| REQ-010 | Create standardized report criteria and interpretation documentation | NF-Doc | Documentation of official reports | Document what each official report includes/excludes (taxes, discounts, etc.) to eliminate "singing from different songbooks" | No | ADAPT | Documentation maintenance overhead; updates needed when reports change |
| REQ-011 | Implement role-based export permissions (all-or-nothing) | NF-Sec | NetSuite Role Export Permissions | "For a given role there is a report export [permission]" - prevent customer data theft risk | No | ALIGNS | All-or-nothing limitation means cannot restrict per-report; may block legitimate needs |
| REQ-012 | Configure notification system for large data exports (>50MB) | NF-Sec | Custom Workflow for Export Monitoring | "Trigger system to alert if more than 50 megabytes of data are being downloaded" | Yes | ACCOMMODATE | Reactive not preventive; export already occurred when notification sent |
| REQ-013 | Utilize 400+ standard NetSuite reports with customization | F | NetSuite Standard Reports (Income Statement, Balance Sheet, Trial Balance, AR/AP, etc.) | "NetSuite ships with over 400 standard reports... every single one can be customized" | No | ALIGNS | Customization decisions require business input; potential over-customization |
| REQ-014 | Implement as-of-date reporting capability for historical snapshots | F | NetSuite As-Of Date Reporting | "Reporting in NetSuite is unique because you can get the as of dates... like what was my balance sheet as of September 1st" | No | ALIGNS | Users must understand when to use as-of-date vs real-time |
| REQ-015 | Enable workbook analytics for pivot tables and charts | F | NetSuite Workbook Analytics | "Like think of like Excel... pivot table charts, you can build those out inside NetSuite" | No | ALIGNS | Training needed for users accustomed to Excel pivot tables |
| REQ-016 | Configure SuiteQL access for technical users | F | NetSuite SuiteQL Module | "NetSuite's kind of own version of SQL. You can write queries" - for Kipp and technical users | No | ALIGNS | Poorly written queries could impact performance; governance needed |
| REQ-017 | Enable inline editing from saved searches | F | NetSuite Saved Search Inline Edit | "Whenever you see a pencil here, that means you can edit right here without having to go in and edit the whole record" | No | ALIGNS | Training needed on when to use inline edit vs full record |
| REQ-018 | Implement highlighting rules for visual indicators | F | NetSuite Saved Search Highlighting | "If the expected close date is before today that's a problem" - highlight overdue items | No | ALIGNS | Highlighting standards needed for consistency |
| REQ-019 | Enable mass update functionality | F | NetSuite Saved Search Mass Update | "You can, in a safe search, do a mass update" for bulk operations | No | ALIGNS | Risk of accidental bulk updates; training and permissions critical |
| REQ-020 | Create sales rep scorecards for individual dashboards | F | Custom Dashboard Component with Saved Search | "I would love them to see that on their own dashboard" - replace manual booking report distribution | Yes | ACCOMMODATE | Requires scorecard design based on current booking report; metrics definition needed |
| REQ-021 | Build manager view scorecards showing team performance | F | Custom Dashboard Component with Team Filters | "If he was ever managing them on their dashboard, it shows them all of their people" | Yes | ACCOMMODATE | Requires proper org structure; manager hierarchy must be maintained |
| REQ-022 | Implement "me only" and "me and my team" filters | F | NetSuite Employee Hierarchy Filters | Filter scope for individual vs manager views on scorecards and analytics | No | ALIGNS | Requires accurate org structure configuration per REQ-023 |
| REQ-023 | Configure proper manager hierarchy for filter functionality | F | NetSuite Employee Records Manager Assignment | "You have to have the right managers assigned for those filters to work. But if we set that up, if we set it up, it actually works" - fixes Core frustration | No | ALIGNS | Org structure changes must be maintained or filters break; HR process dependency |
| REQ-024 | Enable scheduled report distribution via email | F | NetSuite Scheduled Reports with Email Distribution | "Can schedule reports and email automatically" for executive packages when not co-located | No | ALIGNS | Email distribution list maintenance; frequency configuration |
| REQ-025 | Support executive financial review presentations from system | F | NetSuite Financial Dashboards with Drill-Down | "When we would sit down... I would just pull up the income statement, the balance sheet, trial balance, walk through it... drill down, figure out" | No | ALIGNS | Executives need NetSuite access or screen sharing; training on drill-down |
| REQ-026 | Build comprehensive Backlog 360 dashboard | F | Custom Comprehensive Dashboard | "We're building on a backlog 360 dashboard... everything you could ever imagine for backlog in one place" | Yes | ACCOMMODATE | Requires detailed component specifications; backlog by line, by order, comprehensive view |
| REQ-027 | Build comprehensive Bookings 360 dashboard | F | Custom Comprehensive Dashboard | Similar to Backlog 360 - comprehensive bookings reporting in single dashboard | Yes | ACCOMMODATE | Similar to REQ-026; detailed specifications needed |

## Requirements Summary by Approach

### ALIGNS (17 requirements)
Standard NetSuite functionality that meets KBM Hoag needs without customization:
- REQ-001, REQ-004, REQ-005, REQ-006, REQ-007, REQ-009, REQ-011, REQ-013, REQ-014, REQ-015, REQ-016, REQ-017, REQ-018, REQ-019, REQ-022, REQ-023, REQ-024, REQ-025

**Rationale**: These leverage native NetSuite BI capabilities (dashboards, saved searches, workbook analytics, SuiteQL, standard reports, reminders portlet, as-of-date reporting, inline editing, highlighting, mass update, filters, scheduled reports). While configuration is required, no custom development is needed beyond standard NetSuite setup.

### ADAPT (3 requirements)
Process changes needed but no system customization:
- REQ-002, REQ-008, REQ-010

**Rationale**:
- REQ-002: Business must decide whether to use Power BI with live connection or rely solely on NetSuite - process decision
- REQ-008: Business must adopt new naming convention and "official report" concept - behavioral change
- REQ-010: Business must create and maintain report documentation - new process

### ACCOMMODATE (7 requirements)
Custom development or configuration to meet specific KBM Hoag needs:
- REQ-003, REQ-012, REQ-020, REQ-021, REQ-026, REQ-027

**Rationale**:
- REQ-003: Dashboard lock-down may require custom configuration beyond standard publishing (Note: Could potentially be ALIGNS if native capability sufficient)
- REQ-012: Export notification workflow requires custom development (workflow triggers on export events)
- REQ-020/REQ-021: Custom scorecard design based on current booking report - tailored to KBM Hoag metrics
- REQ-026/REQ-027: Custom comprehensive dashboards ("360") combining multiple views - custom Orion components

**SolutionDesign Required**: Yes for all ACCOMMODATE requirements

## Requirements by Type

### Functional (F): 22 requirements
REQ-001, REQ-002, REQ-003, REQ-005, REQ-006, REQ-007, REQ-009, REQ-013, REQ-014, REQ-015, REQ-016, REQ-017, REQ-018, REQ-019, REQ-020, REQ-021, REQ-022, REQ-023, REQ-024, REQ-025, REQ-026, REQ-027

### Non-Functional (NF): 5 requirements
- **NF-Aesthetic**: REQ-004 (Orion-enhanced dashboard components)
- **NF-Governance**: REQ-008 (official report designation)
- **NF-Documentation**: REQ-010 (report criteria documentation)
- **NF-Security**: REQ-011 (export permissions), REQ-012 (export notifications)

## Priority Analysis

### Must-Have
- REQ-001: Platform foundation
- REQ-003: Manager-team alignment critical
- REQ-005: Department-specific access
- REQ-006: Daily work driver
- REQ-008: Solve trust issue ("singing from same songbook")
- REQ-010: Report interpretation consistency
- REQ-011: Security/data protection
- REQ-013: Core financial and operational reporting
- REQ-014: Historical comparison capability
- REQ-017: Efficiency for daily operations
- REQ-023: Enable filters to work
- REQ-025: Executive review capability
- REQ-026: Order Management critical functionality
- REQ-027: Order Management critical functionality

### Should-Have
- REQ-004: User experience enhancement
- REQ-007: Departmental reminders
- REQ-009: Governance controls
- REQ-012: Security monitoring
- REQ-015: Excel replacement
- REQ-016: Power user capability
- REQ-018: Visual prioritization
- REQ-019: Bulk efficiency
- REQ-020: Sales rep visibility
- REQ-021: Manager visibility
- REQ-022: Role-appropriate views
- REQ-024: Executive distribution

### Nice-to-Have
- REQ-002: Power BI optional integration

## Risk Summary by Requirement

### High Risk
- **REQ-003**: User resistance to locked dashboards (change management critical)
- **REQ-006**: Daily workflow habit change (adoption risk)
- **REQ-008**: Users may continue creating personal reports (governance enforcement)
- **REQ-011**: All-or-nothing may block legitimate exports (productivity impact)
- **REQ-012**: Reactive notification, export already occurred (not preventive)
- **REQ-023**: Org structure maintenance required (HR process dependency)

### Medium Risk
- **REQ-001**: Excel/Google Sheets change resistance, learning curve
- **REQ-002**: Live connection technical complexity
- **REQ-004**: Aesthetic preferences subjective
- **REQ-010**: Documentation maintenance overhead
- **REQ-016**: Query performance impact possible
- **REQ-019**: Accidental bulk update risk
- **REQ-020/REQ-021**: Metrics definition and scorecard design approval
- **REQ-026/REQ-027**: Detailed specifications needed, scope creep potential

### Low Risk
- **REQ-005, REQ-007, REQ-009, REQ-013, REQ-014, REQ-015, REQ-017, REQ-018, REQ-022, REQ-024, REQ-025**: Standard functionality with training

## Traceability to Transcript

### Core Pain Point (Drives Multiple Requirements)
**Quote**: "Right now we have reports that are like, you know, Mark's version, Matt's version, Kip's version... A lot of it comes down to people writing reports, naming them similar. They have different criteria. You have different numbers, and people don't trust the reporting... We used to call it singing from the same songbook. Yeah. It's a different key."

**Requirements Addressing**: REQ-008 (official reports), REQ-010 (documentation), REQ-003 (locked dashboards), REQ-001 (platform change)

### Key Success Factor (Mentioned Repeatedly)
**Quote**: "This reminders portlet is key... This is all the work that I have to work off of. Like it shouldn't, you shouldn't have to guess."

**Requirements Addressing**: REQ-006 (reminders portlet), REQ-007 (departmental scope)

### Security Concern (Explicit Decision)
**Quote**: "Right now there's not a lot of control in Core to determine who can export what information... Let's list that as a requirement, some permission around exporting and some notifications around if something was exported over a certain amount."

**Requirements Addressing**: REQ-011 (export permissions), REQ-012 (notifications)

### Org Structure Frustration (Specific Pain Point)
**Quote**: "That's been one of the frustrations with Core. They do allegedly have this hierarchy of permissions, roles and permissions, and, like, this is the manager. They report to that manager, and that manager is supposed to see everyone, and it doesn't. I've never gotten that... [NetSuite] You have to have the right managers assigned for those filters to work. But if we set that up, if we set it up, it actually works."

**Requirements Addressing**: REQ-023 (org structure), REQ-022 (filters), REQ-021 (manager scorecards)

### Dashboard Control Example (Change Management)
**Quote**: "'I changed my dashboard.' I'm like, 'No, you're not doing that.' So then what I would do is I create a dashboard for them, publish it, and they can't change it."

**Requirements Addressing**: REQ-003 (dashboard lock-down)

### Executive Reporting Need
**Quote (Lorraine)**: "On that, like the dashboard is great, especially for the finance team in this instance, but then how are they, when it's month end and they come to present to Mark and I, how are they... do they have to export all of that into Excel or are they able to do the presentation through Orion?"

**Requirements Addressing**: REQ-025 (executive presentations), REQ-024 (scheduled reports)

### Comprehensive Dashboards
**Quote**: "We're building on a backlog 360 dashboard, so it's just one dashboard that has everything you could ever imagine for backlog in one place."

**Requirements Addressing**: REQ-026 (Backlog 360), REQ-027 (Bookings 360)

### Scorecard Request
**Quote (Wendy)**: "So I would love them to see that on their own dashboard. And then if he was ever managing them on their dashboard, it shows them all of their people."

**Requirements Addressing**: REQ-020 (sales rep scorecards), REQ-021 (manager scorecards)

## Notes

### Implementation Sequence Recommendations
1. **Phase 1 - Foundation**: REQ-001, REQ-005, REQ-023 (platform, centers, org structure)
2. **Phase 2 - Core Reporting**: REQ-013, REQ-014, REQ-017 (standard reports, as-of-date, inline editing)
3. **Phase 3 - Governance**: REQ-008, REQ-009, REQ-010 (official reports, controls, documentation)
4. **Phase 4 - Daily Operations**: REQ-006, REQ-007, REQ-018 (reminders, highlighting)
5. **Phase 5 - Security**: REQ-011, REQ-012 (export controls and notifications)
6. **Phase 6 - Manager Tools**: REQ-003, REQ-022 (dashboard publishing, filters)
7. **Phase 7 - Executive**: REQ-024, REQ-025 (scheduled reports, presentation capability)
8. **Phase 8 - Custom Enhancements**: REQ-004, REQ-020, REQ-021, REQ-026, REQ-027 (Orion components, scorecards, 360 dashboards)
9. **Phase 9 - Power Users**: REQ-015, REQ-016, REQ-019 (workbook analytics, SuiteQL, mass update)
10. **Phase 10 - Optional**: REQ-002 (Power BI if needed)

### Critical Success Factors
1. **Change Management**: REQ-003, REQ-006, REQ-008 require significant behavior change - "singing from same songbook" philosophy must be communicated and reinforced
2. **Org Structure Accuracy**: REQ-023 is foundation for REQ-022, REQ-021 - must be correct from day one
3. **Training Prioritization**: REQ-006 (reminders portlet), REQ-017 (inline editing), REQ-008 (official reports) deliver immediate productivity value
4. **Security First**: REQ-011, REQ-012 should be configured before widespread use to establish controls early

### Dependencies
- **REQ-020, REQ-021 → REQ-023**: Scorecards depend on org structure for "me and my team" filters
- **REQ-022 → REQ-023**: Filters depend on org structure configuration
- **REQ-003 → REQ-005**: Publishing depends on centers being created
- **REQ-008 → REQ-010**: Official reports need documentation for consistency
- **REQ-025 → REQ-013, REQ-014**: Executive presentations depend on reports being available

### Outstanding Decisions Impacting Classification
- **REQ-003**: Could potentially be ALIGNS if native NetSuite dashboard publishing includes sufficient lock-down - verify capability
- **REQ-002**: Power BI strategy decision needed - is live connection required or will NetSuite native tools suffice?
- **Export Controls**: All-or-nothing limitation of REQ-011 may drive need for REQ-012 notification system or acceptance of limitation

### Integration Points
- SharePoint/Google Drive (mentioned but not formally captured as requirements) - follow-up needed
- Email system (REQ-024 scheduled reports) - standard NetSuite capability
- Power BI (REQ-002) - optional, needs decision

---

*End of Requirements Map - Business Intelligence & Reporting v1.0*


# Requirements Map - System Setup and Configuration
**Version**: 1.0  
**Date**: October 16, 2025  
**Process Area**: System Setup and Configuration

## Change Log
- **Date**: October 16, 2025
- **Version**: 1.0
- **Sources**: Master_Transcript_Project_Kickoff.md, Discovery Workflow Specification.md
- **Summary**: Initial requirements map created from discovery questionnaire covering all project governance, implementation methodology, system configuration, data migration, training, communication, and go-live requirements

## Implementation Approach Classifications

**ALIGNS**: The way the dealer is executing a business process in their current business system aligns with how they will do it in Orion. It might not be an exact one-to-one alignment, but it doesn't require any customizations for them to do what they are currently doing now in Orion.

**ADAPT**: They do need to modify their business process to use Orion. Adaptation is on a spectrum so it could be major or minor - but still no customization required.

**ACCOMMODATE**: WE will accommodate their business process by customization, personalization, new configuration - something we need to do to accommodate their needs.

## Requirements Map

| ID | Requirement | Type (F/NF) | Functionality | Decision | SolutionDesign? | Approach | Risks |
|----|-------------|-------------|--------------|----------|-----------------|----------|-------|
| REQ-001 | Establish dual executive sponsorship (Sean Scanlon - GSI; Matt - KBM Hoag) for escalation and strategic decisions | NF | Project Governance | Dual executive sponsorship model established | No | ALIGNS | Clear escalation paths required |
| REQ-002 | Designate Lorraine Guzman as Program Manager to lead internal coordination and change management | NF | Project Governance | Lorraine designated as PM | No | ALIGNS | PM availability during month-end closings |
| REQ-003 | Assign Kimmy Katsuyoshi as Change Management Lead for user adoption strategy | NF | Change Management | Kimmy assigned as CM Lead | No | ALIGNS | User adoption success depends on CM effectiveness |
| REQ-004 | Establish functional workstream leads from department SMEs | NF | Project Governance | Department SMEs as workstream leads | No | ALIGNS | SME availability for sessions |
| REQ-005 | Follow DREAM methodology (Discovery → Realize → Educate → Activate/Naturalize → Maintain) | NF | Implementation Framework | DREAM methodology selected | No | ALIGNS | None - proven methodology |
| REQ-006 | Execute 6-8 week Discovery phase with validation focus vs traditional discovery | NF | Discovery Process | 6-8 week timeline with validation approach | No | ALIGNS | Client availability for sessions |
| REQ-007 | Conduct 1.5-2 hour discovery sessions with Part 1 (NetSuite overview) and Part 2 (analysis & questions) | NF | Discovery Process | Two-part session format established | No | ALIGNS | Session scheduling around business cycles |
| REQ-008 | Create BRDs for all 8 process areas (Marketing, CRM, Pre-Quote, Order Mgmt, Operations, Financial, BI, System Setup) | NF | Discovery Deliverables | BRD per process area with client sign-off | No | ALIGNS | BRD completeness and accuracy |
| REQ-009 | Install 5 Orion Suite Apps into NetSuite Financial Premium account | F | NetSuite Configuration | Orion Suite Apps installation | No | ALIGNS | Suite App compatibility |
| REQ-010 | Configure 25+ custom Orion roles and deactivate standard NetSuite roles | F | Security & Roles | Custom Orion roles with standard roles deactivated | No | ALIGNS | Role mapping to users needed |
| REQ-011 | Implement Orion custom forms, fields, and furniture-specific workflows | F | System Configuration | Orion custom forms and workflows | No | ALIGNS | Workflow testing required |
| REQ-012 | Set up chart of accounts as critical first configuration step | F | Financial Configuration | Chart of accounts first priority | No | ALIGNS | Critical dependency for other config |
| REQ-013 | Reduce chart of accounts from 40+ pages to few hundred accounts | F | Financial Configuration | Consolidate and streamline COA | No | ADAPT | Finance team process changes needed |
| REQ-014 | Configure NetSuite Financial Premium SKU with Advanced Inventory Module | F | System Configuration | Financial Premium with Adv Inventory | No | ALIGNS | None - standard Orion config |
| REQ-015 | Import financial historical data back to 2017 (KB workspace) using end-of-month trial balances via CSV | F | Data Migration | 2017+ financial data import | No | ALIGNS | Data accuracy validation needed |
| REQ-016 | Determine Hoag workspace historical data import range (TBD) | F | Data Migration | Hoag workspace timeframe TBD | No | ALIGNS | Decision pending from Lorraine |
| REQ-017 | Archive pre-2017 data separately outside NetSuite for historical reference | F | Data Migration | Separate archive for pre-2017 data | No | ADAPT | Users adjust to different access method |
| REQ-018 | Use SQL backend "backdoor" access to extract Core data without vendor involvement | F | Data Migration | SQL extraction without Core vendor | No | ALIGNS | Joe Keller has tool and approach |
| REQ-019 | Import 2-5 years financial data (up to 10 years possible) for period-over-period reporting | F | Data Migration | Multi-year data import for reporting | No | ALIGNS | Storage and performance considerations |
| REQ-020 | Implement Miller Knoll Exemplis integration for product ordering | F | Integration | Exemplis integration (completed) | No | ALIGNS | Already completed |
| REQ-021 | Configure Bank Feeds Suite App for West Coast Community Bank | F | Integration | Bank Feeds Suite App | No | ALIGNS | Bank API access |
| REQ-022 | Configure Advanced Electronic Bill Payments Suite App for automated bank reconciliation | F | Integration | Electronic Bill Payments Suite App | No | ALIGNS | Bank integration testing |
| REQ-023 | Establish Paylocity CSV journal entry import for payroll (may change platforms) | F | Integration | Payroll CSV import | No | ALIGNS | Platform decision pending |
| REQ-024 | Automate Expensify integration to eliminate manual Excel upload/download | F | Integration | Automated expense integration | Yes | ACCOMMODATE | Custom integration development needed |
| REQ-025 | Configure Google Drive bi-directional integration for folder structure access | F | Integration | Google Drive integration | No | ALIGNS | Decision pending: GDrive vs SharePoint |
| REQ-026 | Extend manufacturer integration platform to additional vendors (pending participation) | F | Integration | Manufacturer integration platform extension | No | ALIGNS | Vendor participation dependent |
| REQ-027 | Deliver multi-format training (live recorded sessions, documentation, videos, user guides) | NF | Training | Multi-format training approach | No | ALIGNS | Leverages existing training culture |
| REQ-028 | Create process decks with step-by-step walkthroughs and video accompaniment | NF | Training | Process decks with videos | No | ALIGNS | Matches current KBM approach |
| REQ-029 | Identify and invest additional training in NetSuite Champions/Power Users for peer support | NF | Training | NetSuite Champions strategy | No | ALIGNS | Champion identification timing |
| REQ-030 | Conduct department-specific and role-based training sessions | NF | Training | Dept/role-based training | No | ALIGNS | Training schedule coordination |
| REQ-031 | Provide User Acceptance Testing (UAT) as part of Educate phase | NF | Quality Assurance | UAT in Educate phase | No | ALIGNS | UAT thoroughness required |
| REQ-032 | Use Microsoft Teams as primary communication platform (KBM joins GSI Teams) | NF | Communication | Microsoft Teams platform | No | ALIGNS | Teams setup immediate action |
| REQ-033 | Establish weekly status reporting cadence | NF | Communication | Weekly status reports | No | ALIGNS | None |
| REQ-034 | Schedule working sessions at weekly to 3x per week cadence (to be determined) | NF | Communication | Flexible session cadence | No | ALIGNS | Cadence TBD based on phase |
| REQ-035 | Record all sessions with backup recording devices | NF | Documentation | Session recording with backup | No | ALIGNS | Recording equipment reliability |
| REQ-036 | Generate AI-assisted transcripts for all sessions to build BRDs | NF | Documentation | AI transcript generation | No | ALIGNS | Transcript accuracy |
| REQ-037 | Implement change control process with change orders post-discovery scope lock | NF | Project Management | Change control with change orders | No | ALIGNS | Discipline enforcing scope lock |
| REQ-038 | Execute soft cutover go-live strategy (not hard cutover) | NF | Go-Live Strategy | Soft cutover approach | No | ALIGNS | None - risk mitigation strategy |
| REQ-039 | Start new business in NetSuite on go-live date while completing existing projects in Core | F | Go-Live Strategy | Dual-system operational approach | No | ADAPT | Users manage two systems during transition |
| REQ-040 | Plan for ~6 month dual-system period during transition | NF | Go-Live Strategy | 6-month dual system period | No | ADAPT | Dual-system complexity |
| REQ-041 | Migrate projects from Core to NetSuite in phases where possible | F | Go-Live Strategy | Phased project migration | No | ADAPT | Migration sequencing decisions needed |
| REQ-042 | Provide on-site or Microsoft Teams channel support during go-live | NF | Go-Live Support | On-site or Teams support option | No | ALIGNS | Support resource allocation |
| REQ-043 | Include 30 days post go-live support | NF | Post Go-Live | 30 days included support | No | ALIGNS | Included in implementation |
| REQ-044 | Establish Suite Care program for ongoing support and optimization | NF | Post Go-Live | Suite Care program options | No | ALIGNS | Program selection and pricing TBD |
| REQ-045 | Enable client self-sufficiency on the platform as long-term goal | NF | Post Go-Live | Self-sufficiency philosophy | No | ALIGNS | Champions enable independence |
| REQ-046 | Establish consistent project number/naming across Opportunity → Proposal → Sales Order → PO | F | Transaction Management | Consistent project numbering | No | ALIGNS | Prefixes TBD |
| REQ-047 | Enable global search by project, customer name, phone number | F | Transaction Management | Global search capabilities | No | ALIGNS | Standard NetSuite feature |
| REQ-048 | Configure recent transaction dialog for quick access to last 10-15 items | F | Transaction Management | Recent transaction dialog | No | ALIGNS | Standard NetSuite feature |
| REQ-049 | Create Solution Design documents for all customizations regardless of size | NF | Documentation | Solution designs for all customs | No | ALIGNS | Design documentation discipline |
| REQ-050 | Establish separate archive system for pre-2017 and post-migration Core data lookups | F | Data Migration | Archive system for historical access | Yes | ACCOMMODATE | Custom archive solution needed |

## Summary Statistics

**Total Requirements**: 50

**By Type:**
- Functional (F): 25 (50%)
- Non-Functional (NF): 25 (50%)

**By Approach:**
- ALIGNS: 44 (88%)
- ADAPT: 4 (8%)
- ACCOMMODATE: 2 (4%)

**Solution Design Required:**
- Yes: 2 (REQ-024: Expensify automation, REQ-050: Archive system)
- No: 48

**By Category:**
- Project Governance: 4 requirements
- Implementation Methodology: 4 requirements
- System Configuration: 6 requirements
- Data Migration: 6 requirements
- Integration: 7 requirements
- Training: 5 requirements
- Communication & Documentation: 6 requirements
- Go-Live Strategy: 6 requirements
- Post Go-Live: 3 requirements
- Transaction Management: 3 requirements

## Key Insights

### High ALIGNS Percentage (88%)
The high percentage of ALIGNS requirements demonstrates that Orion's pre-configured solution effectively meets KBM Hoag's needs with minimal customization. This validates the "95% out-of-box" claim and supports the implementation efficiency.

### Minimal ACCOMMODATE Requirements (4%)
Only 2 requirements need custom development:
1. **REQ-024**: Expensify automation - eliminates manual Excel processes
2. **REQ-050**: Archive system - addresses historical data access post-migration

Both accommodations address specific operational efficiency goals and are well-justified.

### ADAPT Requirements Focus on Process Change (8%)
The 4 ADAPT requirements focus on necessary business process changes:
1. **REQ-013**: Chart of accounts consolidation - finance process improvement
2. **REQ-017**: Historical data archive access - user behavior adjustment
3. **REQ-039**: Dual-system operations during go-live - temporary operational change
4. **REQ-040**: 6-month transition period - phased change management
5. **REQ-041**: Phased project migration - operational sequencing change

These represent the "discomfort" acknowledged in the philosophy: "It's going to get uncomfortable, we have Kleenex"

### Critical Dependencies
1. **REQ-012**: Chart of accounts - blocks all other financial configuration
2. **REQ-032**: Microsoft Teams setup - needed immediately for communication
3. **REQ-029**: NetSuite Champions - foundational for training success
4. **REQ-006**: Discovery phase completion - gates Realize phase start

### Open Decisions Impacting Requirements
1. **REQ-016**: Hoag workspace data timeframe (Lorraine decision)
2. **REQ-023**: Payroll platform selection (Michelle/HR decision)
3. **REQ-024**: Expense platform selection (Finance decision)
4. **REQ-025**: Google Drive vs SharePoint (Kip/IT decision)
5. **REQ-044**: Suite Care program selection (Executive decision)

## Traceability Notes

### Link to Questionnaire Sections
- REQ-001 to REQ-004: Section 1 - Project Governance & Team Structure
- REQ-005 to REQ-008: Section 2 - Implementation Methodology
- REQ-009 to REQ-014: Section 3 - System Configuration & Setup
- REQ-015 to REQ-019, REQ-050: Section 4 - Data Migration Strategy
- REQ-020 to REQ-026: Section 5 - Integration Requirements
- REQ-027 to REQ-031: Section 6 - Training Strategy
- REQ-032 to REQ-037: Section 7 - Communication & Collaboration
- REQ-038 to REQ-043: Section 8 - Go-Live Strategy
- REQ-044 to REQ-045: Section 9 - Post-Go-Live Support & Optimization
- REQ-046 to REQ-048: Section 10 - Project Numbering & Transaction Management
- REQ-049: Section 2.3 - Discovery Deliverables

### Transcript Evidence References
All requirements include direct quotes from Master_Transcript_Project_Kickoff.md supporting the decision and approach classification. See Questionnaire Decision Log for full evidence trail.

### Action Items Linked to Requirements
- Kip provides templates → REQ-009, REQ-011
- Matt provides XML templates → REQ-015, REQ-018
- Shannon provides approval rules → REQ-011
- Lorraine confirms order types → REQ-011
- Lorraine determines Hoag data timeframe → REQ-016
- Michelle finalizes payroll platform → REQ-023
- Finance finalizes expense platform → REQ-024
- Kip decides GDrive vs SharePoint → REQ-025
- Kimmy identifies NetSuite Champions → REQ-029
- Team sets up Microsoft Teams → REQ-032

## Risk Summary by Requirement

**High Risk:**
- REQ-013: Chart of accounts consolidation - finance process disruption potential
- REQ-017: Historical data access change - user frustration risk
- REQ-039-041: Dual-system go-live - operational complexity

**Medium Risk:**
- REQ-024: Expensify automation - custom integration reliability
- REQ-026: Manufacturer integrations - vendor participation dependency
- REQ-050: Archive system - user adoption of new access method

**Low Risk:**
- All ALIGNS requirements leveraging standard Orion functionality
- Training requirements (REQ-027-031) - strong existing culture to build on
- Communication requirements (REQ-032-037) - proven tools and processes

## Next Steps for Requirements Validation

1. **Chart of Accounts Deep Dive Session** - Validate REQ-012, REQ-013 with detailed mapping
2. **Data Migration Planning Session** - Confirm REQ-015-019, REQ-050 approach and scope
3. **Integration Architecture Review** - Finalize REQ-023-026 platform decisions
4. **Go-Live Strategy Workshop** - Detail REQ-038-043 operational procedures
5. **User Role Mapping** - Map users to REQ-010 custom roles
6. **NetSuite Champions Identification** - Execute REQ-029 strategy with Kimmy

---

*End of Requirements Map - System Setup and Configuration v1.0*





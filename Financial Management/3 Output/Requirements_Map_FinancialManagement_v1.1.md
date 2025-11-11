# Requirements Map - Financial Management
**Version**: 1.1  
**Date**: October 28, 2025  
**Process Area**: Financial Management (Accounting, GL, AP, AR, Banking, Reporting, Closing)

## Change Log
- **Date**: October 28, 2025
- **Version**: 1.1
- **Sources**: Questionnaire_FinancialManagement_v1.0.md, Financial_Management_Follow-Up_Discovery_Session.md, FW-Follow-Up-Project-Orion-Finance-transcript.json
- **Summary**: Enhanced requirements map with follow-up discovery session insights. Added session dependency cross-references, decision point clarity with decision makers and timelines, implementation complexity notes, and custom development scope details for ACCOMMODATE items.

## PROCESSED FILES
- Questionnaire_FinancialManagement_v1.0.md (v1.0 source)
- Financial_Management_Follow-Up_Discovery_Session.md (Framework for 8 follow-up sessions)
- FW-Follow-Up-Project-Orion-Finance-transcript.json (October 2025 follow-up meetings)

## Implementation Approach Classifications

**ALIGNS**: The way the dealer is executing a business process in their current business system aligns with how they will do it in Orion. It might not be an exact one-to-one alignment, but it doesn't require any customizations for them to do what they are currently doing now in Orion.

**ADAPT**: They do need to modify their business process to use Orion. Adaptation is on a spectrum so it could be major or minor - but still no customization required.

**ACCOMMODATE**: WE will accommodate their business process by customization, personalization, new configuration - something we need to do to accommodate their needs.

## Requirements Map

| ID | Requirement | Type (F/NF) | Functionality | Decision | SolutionDesign? | Approach (ALIGNS/ADAPT/ACCOMMODATE) | Session | Decision Maker | Timeline | Risks |
|----|-------------|-------------|--------------|----------|-----------------|-------------------------------------|---------|----------------|----------|-------|
| REQ-001 | Configure single NetSuite subsidiary for consolidated KB+Hoag operations | F | Subsidiary Setup | Single subsidiary for merged entity | No | ALIGNS | - | Team | Initial config | None - standard configuration |
| REQ-002 | Implement 13 accounting periods on calendar year basis | F | Accounting Periods | 13 periods (not standard 12) - Lorraine's preference | No | ADAPT | - | Lorraine | Initial config | Users must understand 13-period calendar vs typical 12 |
| REQ-003 | Configure US Dollar as single currency (no multi-currency) | F | Currency Setup | USD only | No | ALIGNS | - | Team | Initial config | None - simplifies configuration |
| REQ-004 | Implement native SuiteTax for 48-state nexus management with automatic calculation | F | SuiteTax | Native SuiteTax (not Avalara) | No | ALIGNS | - | Team | Initial config | Nexus configuration complexity; ongoing compliance maintenance |
| REQ-005 | Configure tax exemption certificate management with expiration tracking and dashboard | F | SuiteTax | Certificate tracking with dashboard | No | ALIGNS | - | Team | Initial config | Manual certificate upload and maintenance; expiration monitoring |
| REQ-006 | Configure SuiteTax for use tax handling in Illinois and Missouri | F | SuiteTax | Use tax for IL/MO (eliminates "trick" workaround) | No | ALIGNS | - | Team | Initial config | Compliance validation for both states |
| REQ-007 | Enable gross receipts tax reporting by ship-to location | F | SuiteTax Reports | Standard ship-to location reporting | No | ALIGNS | - | Marcus | Initial config | None - standard report |
| REQ-008 | Implement bank feeds integration with West Coast Community Bank | F | Bank Feeds Suite App | Auto-import transactions, auto-matching | No | ALIGNS | SESSION 5 | Marcus | Before go-live | Bank integration setup; positive pay process TBD |
| REQ-009 | Enable Advanced Electronic Bill Payments for ACH directly from NetSuite | F | Advanced Electronic Bill Payments | ACH from NetSuite, skip bank portal | No | ALIGNS | SESSION 5 | Marcus/Lorraine | Before go-live | Coastal registration required; bank integration testing |
| REQ-010 | Configure bill payment approval workflow with Lorraine as approver | F | Bill Payment Approval | Lorraine approves Monday payment runs | No | ADAPT | SESSION 5 | Lorraine/Guada/Michael | Before detailed design | Workflow details TBD; remittance process TBD; can Lorraine remove items in-system? |
| REQ-011 | Enable Cash360 Dashboard for cash flow forecasting | F | Cash360 Dashboard | Standard dashboard for cash flow | No | ALIGNS | SESSION 5 | Marcus | Initial config | None - standard feature |
| REQ-012 | Configure credit card reconciliation as bank account (upload statement, auto-match) | F | Bank Reconciliation | Credit card as bank account, CSV import | No | ALIGNS | - | Marcus | Before go-live | Manual statement export from ARC Bank; not live feed |
| REQ-013 | Evaluate and implement Expensify integration via Suite App | F | Expensify Suite App | Auto-sync from Expensify to NetSuite | No | ALIGNS | SESSION 6 | Lorraine | Before configuration | **DECISION PENDING**: Expensify vs. RAMP platform choice required |
| REQ-014 | Evaluate RAMP as alternative to Expensify with NetSuite integration | F | RAMP Integration | Alternative to Expensify (demo both) | No | ALIGNS | SESSION 6 | Lorraine | Before configuration | **DECISION PENDING**: RAMP vs. Expensify; user change management if switching |
| REQ-015 | Support project vs. G&A allocation for expense reports | F | Expense Coding | Project (COGS) vs. G&A allocation required | Yes | ACCOMMODATE | SESSION 6 | Lorraine | Before configuration | Must ensure integration supports project coding; field mapping critical; line-level coding needs clarification |
| REQ-016 | Consolidate chart of accounts from 40+ pages to few hundred accounts | F | Chart of Accounts | Reduce from 40+ pages to few hundred | Yes | ACCOMMODATE | SESSION 2 | Lorraine/Celine/Kevin | URGENT - Before data migration | Major design effort; all transactions/reports impacted; user memorization; extensive training required; historical reporting impact |
| REQ-017 | Migrate historical financial data back to 2017 (trial balances, period-over-period) | F | Data Migration | 8 years history (2017-2025) | No | ALIGNS | - | Lorraine | Before go-live | Data quality validation; SQL extraction from Core; period-over-period reporting dependent on REQ-016 |
| REQ-018 | Enable CSV import of journal entries with automated reversal capability | F | Journal Entry Import, Reversal JE | CSV import, automated reversal | No | ALIGNS | - | Marcus | Before go-live | None - standard functionality; major improvement over Core (solves prior tracking issues) |
| REQ-019 | Determine if automated allocation transactions will be implemented | F | Allocations | Optional - Matt/Mark decision pending | Maybe | ADAPT | SESSION 3 | Matt/Mark | Before configuration | **DECISION PENDING**: Implementation required only if approved; if implemented, requires allocation rules definition |
| REQ-020 | Implement NetSuite Period Close Checklist to replace Excel-based process | F | Period Close Checklist | System-guided checklist (not Blackline/Flowcast) | No | ALIGNS | SESSION 4 | Lorraine/Celine/Kevin | Before detailed design | Checklist customization to KBM needs; timeline reduction goal (from 10 days to 5-7 days); close process optimization opportunity significant |
| REQ-021 | Configure ability to close AP/AR modules separately from GL | F | Period Close | Flexible module closing via checklist | No | ALIGNS | SESSION 4 | Lorraine | Before detailed design | Determine optimal close sequence: parallel vs. sequential? |
| REQ-022 | Open all 13 periods at year start, close progressively | NF | Period Management | Open full year in December, close as go | No | ADAPT | SESSION 4 | Marcus (best practice) | Before go-live | Process change; December reminder critical; avoid opening >1 year ahead |
| REQ-023 | Determine if 15% labor markup (contingency line) will continue in NetSuite | F | Labor Costing | Optional - Matt/Mark decision (impacts commission) | Maybe | ADAPT | SESSION 3 | Matt/Mark (DECISION REQUIRED) | BEFORE CONFIGURATION | **CRITICAL DECISION PENDING**: Major impact on commission calculations, sales compensation, custom development scope; if continuing, may require custom script |
| REQ-024 | Maintain separate Project GP vs. Commissionable GP reporting and KPIs | F | Project Accounting, Reporting | Two GP metrics for different audiences | Yes | ACCOMMODATE | SESSION 3 | Lorraine/Kipp | Before detailed design | Custom reporting/dashboards required; role-based visibility; calculation logic dependent on REQ-023 decision |
| REQ-025 | Configure role-based permissions for different GP visibility | NF | Role/Permission Setup | Sales see Commissionable GP; Management sees Project GP | Yes | ACCOMMODATE | SESSION 3 | Lorraine | Before detailed design | Permission design critical; user role definition; testing; dependent on REQ-023 decision |
| REQ-026 | Evaluate NetSuite Fixed Asset module vs. continuing Bloomberg | F | Fixed Asset Module | May replace Bloomberg (cost ~$4K) | No | ADAPT | SESSION 7 | Lorraine/Marcus | Before implementation | **DECISION PENDING**: Evaluation required; Bloomberg comparison; migration of existing assets; cost-benefit analysis critical |
| REQ-027 | Configure CSV journal entry import from Paylocity (or new payroll provider) | F | Journal Entry Import | CSV import with department allocation | No | ALIGNS | - | Lorraine/HR | Before go-live | Provider decision pending; flexible for any provider; integration approach remains similar regardless of provider |
| REQ-028 | Evaluate new HR platform/payroll provider integration | F | Payroll Integration | May change from Paylocity | No | ADAPT | - | Lorraine/HR | Before implementation | **DECISION PENDING**: Provider evaluation in progress; may change from Paylocity; CSV approach flexible |
| REQ-029 | Maintain Stripe integration for credit card payment acceptance | F | Payment Processing | Keep Stripe (incidental use, ~$100/year) | No | ALIGNS | - | Marcus | Initial config | No change needed; low priority; maintain current setup |
| REQ-030 | Support wire transfer processing for international payments | F | Wire Transfers | International wires (expensive, low volume) | No | ADAPT | SESSION 5 | Marcus/Lorraine | Before go-live | **CLARIFICATION NEEDED**: Confirm if in Advanced Electronic Bill Payments or manual bank portal required; low volume but important for vendor relationships |
| REQ-031 | Configure finance charge capability (off by default, available as deterrent) | F | Finance Charges | Available but not used (13 years) | No | ALIGNS | - | Team | Initial config | None - standard feature, turned off by default |
| REQ-032 | Implement pro forma invoice for customer deposit management | F | Pro Forma Invoice | Liability account, auto-apply to invoice | No | ALIGNS | - | Team | Before go-live | None - standard functionality; reference Order Management transcript for full details |
| REQ-033 | Configure vendors that are also customers (Intermarket dealers) | F | Vendor/Customer Setup | Dual setup for Intermarket dealers | No | ALIGNS | - | Shannon/Team | Before go-live | Setup process; hundreds of dealers; coordination with Shannon's team; first-time setup pain point |
| REQ-034 | Implement vendor credit limit tracking with warning alerts | F | Vendor Management | Track limits, warn at threshold | Yes | ACCOMMODATE | SESSION 8 | Lorraine/Purchasing | Before go-live | **CUSTOM DEVELOPMENT REQUIRED**: Alert/warning system; threshold definition (recommend 90%?); determine alert mechanism (email vs. dashboard vs. hard stop); credit utilization calculation; "mad scramble" pain point significant |
| REQ-035 | Define revenue recognition rules and timing (at Sales Order or Invoice) | F | Revenue Recognition | Complex rules by order type; white paper in progress | Yes | ACCOMMODATE | SESSION 1 | Lorraine/Marcus | BEFORE DETAILED DESIGN | **HIGH COMPLEXITY**: Major design effort; compliance-critical; white paper review pending; special scenarios (mockup, direct bill, government, E-commerce) need documentation; auditor involvement recommended |
| REQ-036 | Maintain project-level revenue/cost tracking with linked transactions | F | Project Accounting | All transactions linked to project; KPI dashboard | No | ALIGNS | SESSION 1 | Team | Before go-live | None - standard project accounting; dependent on REQ-035 for recognition timing |
| REQ-037 | Create real-time financial dashboards to replace manual Excel reports | F | Financial Dashboards | Real-time vs. manual Excel; automated reports | No | ALIGNS | - | Lorraine | Before go-live | Dashboard design; user requirements; dependent on REQ-024/025 for GP metric visibility |
| REQ-038 | Configure project-level KPI dashboards (real-time GP, revenue/cost tracking, commission reporting) | F | Project KPI Dashboards | Project GP, Commissionable GP, real-time tracking | Yes | ACCOMMODATE | SESSION 3 | Lorraine/Kipp | Before go-live | Custom dashboard for two GP metrics; role-based visibility; calculation logic; dependent on REQ-023/024/025 decisions |

## Summary Statistics

**Total Requirements**: 38

**By Type:**
- Functional (F): 36
- Non-Functional (NF): 2

**By Approach:**
- ALIGNS: 26 (68%)
- ADAPT: 9 (24%)
- ACCOMMODATE: 3 core + 6 dependent on decisions (24%)

**Requires SolutionDesign (ACCOMMODATE + Complex):**
- REQ-015: Project vs. G&A expense allocation
- REQ-016: Chart of accounts consolidation
- REQ-024: Project GP vs. Commissionable GP reporting
- REQ-025: Role-based GP visibility
- REQ-034: Vendor credit limit warning alerts
- REQ-035: Revenue recognition rules
- REQ-038: Project-level KPI dashboards
- REQ-019: Automated allocations (if implemented - decision pending)
- REQ-023: 15% labor markup (if continued - decision pending)

**Total SolutionDesign Required**: 9 (24%) - plus 2 conditional on decisions

**Critical Decisions Pending (HIGH IMPACT)**:
1. **REQ-023**: Continue 15% labor markup? (Matt/Mark) - Commission impact HIGH
2. **REQ-035**: Revenue recognition rules - Compliance-critical
3. **REQ-016**: Chart of Accounts design - Foundational and URGENT

**Medium Priority Decisions Pending**:
4. **REQ-013/014**: Expensify vs. RAMP? (Lorraine)
5. **REQ-026**: NetSuite FA module vs. Bloomberg? (Lorraine)
6. **REQ-019**: Implement automated allocations? (Matt/Mark)

## Key Decisions Pending (from Follow-Up Sessions)

| Decision | REQ-ID | Context | Decision Maker | Timeline | Impact |
|----------|--------|---------|----------------|----------|--------|
| 15% Labor Markup Continuation | REQ-023 | Current practice in Core; affects commission calculations | Matt/Mark | BEFORE CONFIGURATION | **HIGH** - Affects sales compensation, custom dev scope |
| Revenue Recognition Rules | REQ-035 | Complex, compliance-critical, white paper pending review | Lorraine/Marcus | BEFORE DETAILED DESIGN | **HIGH** - Compliance risk if not documented properly |
| Chart of Accounts Design | REQ-016 | 40+ pages to few hundred accounts consolidation | Lorraine/Celine/Kevin | **URGENT** - BEFORE DATA MIGRATION | **HIGH** - Foundational to all transactions |
| Expense Platform Selection | REQ-013/014 | Expensify Suite App vs. RAMP integration | Lorraine | BEFORE CONFIGURATION | Medium - User adoption impact |
| Fixed Asset Module Evaluation | REQ-026 | NetSuite FA vs. Bloomberg (costs ~$4K) | Lorraine/Marcus | BEFORE IMPLEMENTATION | Medium - Cost and integration management |
| Automated Allocations | REQ-019 | Optional feature; pending leadership decision | Matt/Mark | BEFORE CONFIGURATION | Medium - P&L reporting impact |
| Payroll Provider | REQ-027/028 | Continue Paylocity or change | Lorraine/HR | BEFORE IMPLEMENTATION | Medium - Integration approach affected |

## High-Risk Requirements

| REQ-ID | Requirement | Risk Description | Severity | Mitigation |
|--------|-------------|------------------|----------|-----------|
| REQ-016 | Chart of accounts consolidation | Massive change (40+ pages to few hundred); impacts all transactions and reports; high user training burden | **CRITICAL** | Dedicated SESSION 2; comprehensive mapping; phased user training; extensive testing; historical reporting validation |
| REQ-035 | Revenue recognition rules | Complex, compliance-critical; errors impact financials and audit; white paper needs review | **CRITICAL** | Dedicated SESSION 1; white paper review with Marcus; auditor consultation recommended; detailed documentation; ASC 606 validation |
| REQ-023 | 15% labor markup decision | If eliminated: major sales compensation change; if continued: requires custom script development; commission impact | **HIGH** | Matt/Mark final decision REQUIRED; sales team communication plan if changing; commission impact analysis |
| REQ-024/025/038 | Project GP vs. Commissionable GP | Custom calculation logic; role-based visibility complex; commission impact; dependent on REQ-023 | **HIGH** | SESSION 3 detailed requirements; calculation validation; user acceptance testing; parallel testing first few months |
| REQ-004 | 48-state nexus management | Ongoing compliance; certificate maintenance; audit risk | HIGH | SuiteTax configuration validation; certificate upload process; expiration monitoring dashboard |
| REQ-009 | Advanced Electronic Bill Payments | Critical AP process; high dollar amounts ($3M runs); vendor impact | HIGH | Thorough testing; parallel run with NACHA fallback; remittance confirmation verification; vendor communication plan |
| REQ-015 | Project vs. G&A expense allocation | Must work with Expensify/RAMP integration; COGS accuracy critical | Medium | Dependent on SESSION 6 platform selection; integration testing; project coding validation; user training on line-level coding |
| REQ-034 | Vendor credit limit tracking | Custom development required; "mad scramble" pain point; operational efficiency | Medium | SESSION 8 requirements definition; alert mechanism clarification; testing for accuracy of credit utilization calculations |

## Integration Dependencies

| Integration | REQ-IDs | Status | Notes | Session |
|-------------|---------|--------|-------|---------|
| West Coast Community Bank | REQ-008, REQ-009, REQ-011 | Confirmed partner | Positive pay process TBD; wire support TBD; Cache360 setup | SESSION 5 |
| Expensify | REQ-013, REQ-015 | Suite App available | **DECISION PENDING**: Demo needed vs. RAMP; project coding verification | SESSION 6 |
| RAMP | REQ-014, REQ-015 | Alternative option | **DECISION PENDING**: Demo needed vs. Expensify; compare UX and capabilities | SESSION 6 |
| Paylocity | REQ-027, REQ-018 | Current provider | **DECISION PENDING**: May change; CSV approach flexible | - |
| Stripe | REQ-029 | Current provider | Keep as-is; incidental use (~$100/year); low priority | - |
| TaxConnect | REQ-006 | Being replaced | Transition to SuiteTax eliminates third party dependency | - |
| Bloomberg | REQ-026 | Evaluation needed | **DECISION PENDING**: May replace with NetSuite FA module (~$4K cost) | SESSION 7 |

## Sessions Needed for Requirements

### CRITICAL/URGENT Sessions (Must Complete Before Configuration):

1. **SESSION 2: Chart of Accounts Design & Mapping** (REQ-016)
   - **Priority**: URGENT - Foundational
   - **Participants**: Lorraine, Celine, Kevin, Implementation Team
   - **Duration**: 2-3 hours
   - **Pre-Work Required**: 
     - Export current Core COA (40+ pages)
     - Identify most-used vs. rarely-used accounts
     - List any known duplicates
   - **Deliverables**: Proposed structure, mapping document, account numbering scheme
   - **Timeline**: ASAP - Before data migration planning

2. **SESSION 1: Revenue Recognition & Project Accounting** (REQ-035, REQ-036)
   - **Priority**: HIGH - Compliance-critical
   - **Participants**: Lorraine, Kipp, Marcus, possibly external auditor
   - **Duration**: 1-2 hours
   - **Key Topics**: 
     - Revenue recognition timing by order type
     - Special scenarios (mockup, direct bill, government, E-commerce)
     - White paper review
     - ASC 606 compliance requirements
   - **Deliverables**: Detailed revenue recognition rules, special scenario procedures, white paper validation
   - **Timeline**: Before detailed design phase

3. **SESSION 3: Commission Structure & GP Calculation** (REQ-023, REQ-024, REQ-025, REQ-038)
   - **Priority**: HIGH - Sales compensation impact
   - **Participants**: Lorraine, Kipp, Matt, Mark, Sales Leadership
   - **Duration**: 1-2 hours
   - **Key Decision**: **15% labor markup - continue or eliminate?**
   - **Deliverables**: 
     - Commission calculation rules documented
     - GP reporting/dashboard requirements
     - Role-based permissions matrix
     - If continuing 15% markup: custom development scope
   - **Timeline**: Before configuration phase

### HIGH PRIORITY Sessions (Must Complete Before Detailed Design):

4. **SESSION 4: Period Close Process Optimization** (REQ-020, REQ-021, REQ-022)
   - **Participants**: Lorraine, Celine, Kevin, AP Team
   - **Duration**: 1-2 hours
   - **Key Topics**: 
     - Detailed 10-day Excel close process walkthrough
     - Bottleneck identification
     - NetSuite Checklist customization
     - Timeline reduction goals (target 5-7 days)
   - **Deliverables**: Detailed close procedure, checklist steps, task assignments, approval gates
   - **Timeline**: Before detailed design

5. **SESSION 5: Bill Payment & Cash Management Workflow** (REQ-008, REQ-009, REQ-010, REQ-011, REQ-030)
   - **Participants**: Lorraine, Guada, Michael, Marcus
   - **Duration**: 1 hour
   - **Key Topics**: 
     - Payment approval workflow (can Lorraine remove items in-system?)
     - Remittance process (automatic vs. manual)
     - Wire transfer handling
     - Positive pay requirements
     - Cash flow forecasting needs
   - **Deliverables**: Detailed workflow, remittance procedure, wire handling approach, positive pay documentation
   - **Timeline**: Before detailed design

6. **SESSION 6: Expense Management System Decision** (REQ-013, REQ-014, REQ-015)
   - **Participants**: Lorraine, AP Team, sample expense submitters
   - **Duration**: 1.5-2 hours
   - **Key Decision**: **Expensify Suite App OR RAMP?**
   - **Key Topics**: 
     - Demo both platforms
     - Project vs. G&A allocation requirements
     - User experience evaluation
     - Project coding requirements
     - Cost comparison
   - **Deliverables**: Platform selection decision, project coding specs, approval workflow, integration requirements
   - **Timeline**: Before configuration

7. **SESSION 7: Fixed Asset Management Decision** (REQ-026)
   - **Participants**: Lorraine, Marcus, Implementation Team
   - **Duration**: 45 minutes - 1 hour
   - **Key Decision**: **NetSuite FA module OR continue Bloomberg?**
   - **Key Topics**: 
     - Bloomberg current usage and costs
     - NetSuite FA module capabilities
     - Cost-benefit analysis
     - Migration approach for existing assets
   - **Deliverables**: Module selection decision, cost analysis, migration plan (if switching)
   - **Timeline**: Before implementation

8. **SESSION 8: Vendor Credit Limit Tracking & Alerts** (REQ-034)
   - **Participants**: Lorraine, Purchasing Team, Shannon
   - **Duration**: 30-45 minutes
   - **Key Topics**: 
     - Warning threshold definition (recommend 90%)
     - Alert mechanism (email vs. dashboard vs. hard stop)
     - Custom development requirements
     - Process for handling warnings
   - **Deliverables**: Warning threshold, alert recipients, alert mechanism, custom dev scope
   - **Timeline**: Before go-live

## Dependency Graph

```
REQ-016 (COA Design) [SESSION 2]
  ├─ Foundational for all other requirements
  └─ Required for: REQ-017 (Historical Data Migration)

REQ-035 (Revenue Recognition) [SESSION 1]
  ├─ Compliance-critical
  └─ Related to: REQ-036 (Project-level revenue/cost tracking)

REQ-023 (15% Labor Markup Decision) [SESSION 3] **CRITICAL GATE**
  ├─ Affects: REQ-024 (Project GP vs. Commissionable GP)
  ├─ Affects: REQ-025 (Role-based permissions)
  ├─ Affects: REQ-038 (KPI dashboards)
  └─ Affects: Commission structure and sales compensation

REQ-024/025/038 (GP Metrics & Dashboards) [SESSION 3]
  ├─ Dependent on: REQ-023 decision
  └─ Related to: REQ-015 (Project vs. G&A expense allocation)

REQ-013/014 (Expense Platform) [SESSION 6] **DECISION GATE**
  └─ Affects: REQ-015 (Project coding capability)

REQ-026 (Fixed Assets) [SESSION 7] **DECISION GATE**
  └─ Independent - no other REQ dependencies
```

## Implementation Complexity by Requirement

### Simple (Low Risk, Standard NetSuite Features):
REQ-001, REQ-003, REQ-004, REQ-005, REQ-007, REQ-011, REQ-012, REQ-018, REQ-021, REQ-029, REQ-031, REQ-032, REQ-033, REQ-036, REQ-037

### Moderate (Process Changes, Some Configuration):
REQ-002, REQ-006, REQ-008, REQ-009, REQ-017, REQ-027, REQ-028, REQ-030

### Complex (Custom Development, Design Decisions, High Risk):
REQ-010, REQ-013/014, REQ-015, REQ-016, REQ-019, REQ-020, REQ-022, REQ-023, REQ-024, REQ-025, REQ-026, REQ-034, REQ-035, REQ-038

## Quality Assurance Checklist

- [x] All 38 requirements verified from v1.0
- [x] Session dependencies mapped for each requirement
- [x] Decision points clearly identified with decision makers
- [x] Timeline clarity added (Before config, Before detailed design, Before go-live)
- [x] ACCOMMODATE items with custom development scope identified
- [x] Risk assessment completed for high-impact requirements
- [x] Integration dependencies documented with status
- [x] Critical path items (REQ-016, REQ-035, REQ-023) highlighted
- [x] Follow-up session framework integrated throughout
- [x] Dependency graph showing requirement relationships

---

*End of Requirements Map - Financial Management v1.1*





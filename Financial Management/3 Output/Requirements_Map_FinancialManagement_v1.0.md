# Requirements Map - Financial Management
**Version**: 1.0  
**Date**: October 15, 2025  
**Process Area**: Financial Management (Accounting, GL, AP, AR, Banking, Reporting, Closing)

## Change Log
- **Date**: October 15, 2025
- **Version**: 1.0
- **Sources**: Master_Transcript_Financial_Management.md
- **Summary**: Initial requirements map created from Financial Management discovery questionnaire, with 38 requirements classified by implementation approach

## Implementation Approach Classifications

**ALIGNS**: The way the dealer is executing a business process in their current business system aligns with how they will do it in Orion. It might not be an exact one-to-one alignment, but it doesn't require any customizations for them to do what they are currently doing now in Orion.

**ADAPT**: They do need to modify their business process to use Orion. Adaptation is on a spectrum so it could be major or minor - but still no customization required.

**ACCOMMODATE**: WE will accommodate their business process by customization, personalization, new configuration - something we need to do to accommodate their needs.

## Requirements Map

| ID | Requirement | Type (F/NF) | Functionality | Decision | SolutionDesign? | Approach (ALIGNS/ADAPT/ACCOMMODATE) | Risks |
|----|-------------|-------------|--------------|----------|-----------------|-------------------------------------|-------|
| REQ-001 | Configure single NetSuite subsidiary for consolidated KB+Hoag operations | F | Subsidiary Setup | Single subsidiary for merged entity | No | ALIGNS | None - standard configuration |
| REQ-002 | Implement 13 accounting periods on calendar year basis | F | Accounting Periods | 13 periods (not standard 12) - Lorraine's preference | No | ADAPT | Users must understand 13-period calendar vs typical 12; reporting adjustments |
| REQ-003 | Configure US Dollar as single currency (no multi-currency) | F | Currency Setup | USD only | No | ALIGNS | None - simplifies configuration |
| REQ-004 | Implement native SuiteTax for 48-state nexus management with automatic calculation | F | SuiteTax | Native SuiteTax (not Avalara) | No | ALIGNS | Nexus configuration complexity; ongoing compliance maintenance |
| REQ-005 | Configure tax exemption certificate management with expiration tracking and dashboard | F | SuiteTax | Certificate tracking with dashboard | No | ALIGNS | Manual certificate upload and maintenance; expiration monitoring |
| REQ-006 | Configure SuiteTax for use tax handling in Illinois and Missouri | F | SuiteTax | Use tax for IL/MO (eliminates "trick" workaround) | No | ALIGNS | Compliance validation for both states |
| REQ-007 | Enable gross receipts tax reporting by ship-to location | F | SuiteTax Reports | Standard ship-to location reporting | No | ALIGNS | None - standard report |
| REQ-008 | Implement bank feeds integration with West Coast Community Bank | F | Bank Feeds Suite App | Auto-import transactions, auto-matching | No | ALIGNS | Bank integration setup; rule configuration; positive pay process TBD |
| REQ-009 | Enable Advanced Electronic Bill Payments for ACH directly from NetSuite | F | Advanced Electronic Bill Payments | ACH from NetSuite, skip bank portal | No | ALIGNS | Coastal registration required; bank integration testing; wire support TBD |
| REQ-010 | Configure bill payment approval workflow with Lorraine as approver | F | Bill Payment Approval | Lorraine approves Monday payment runs | No | ADAPT | Workflow details TBD (can she remove items or only approve/reject?); remittance process TBD |
| REQ-011 | Enable Cash360 Dashboard for cash flow forecasting | F | Cash360 Dashboard | Standard dashboard for cash flow | No | ALIGNS | None - standard feature |
| REQ-012 | Configure credit card reconciliation as bank account (upload statement, auto-match) | F | Bank Reconciliation | Credit card as bank account, CSV import | No | ALIGNS | Manual statement export from ARC Bank; not live feed |
| REQ-013 | Evaluate and implement Expensify integration via Suite App | F | Expensify Suite App | Auto-sync from Expensify to NetSuite | No | ALIGNS | Integration testing; receipt attachment verification |
| REQ-014 | Evaluate RAMP as alternative to Expensify with NetSuite integration | F | RAMP Integration | Alternative to Expensify (demo both) | No | ALIGNS | User change management if switching from Expensify |
| REQ-015 | Support project vs. G&A allocation for expense reports | F | Expense Coding | Project (COGS) vs. G&A allocation required | Yes | ACCOMMODATE | Must ensure integration supports project coding; field mapping critical |
| REQ-016 | Consolidate chart of accounts from 40+ pages to few hundred accounts | F | Chart of Accounts | Reduce from 40+ pages to few hundred | Yes | ACCOMMODATE | Major design effort; all transactions/reports impacted; user memorization |
| REQ-017 | Migrate historical financial data back to 2017 (trial balances, period-over-period) | F | Data Migration | 8 years history (2017-2025) | No | ALIGNS | Data quality validation; SQL extraction from Core; period-over-period reporting |
| REQ-018 | Enable CSV import of journal entries with automated reversal capability | F | Journal Entry Import, Reversal JE | CSV import, automated reversal | No | ALIGNS | None - standard functionality; major improvement over Core |
| REQ-019 | Determine if automated allocation transactions will be implemented | F | Allocations | Optional - Matt/Mark decision pending | Maybe | ADAPT | Decision pending; if implemented, requires allocation rules definition |
| REQ-020 | Implement NetSuite Period Close Checklist to replace Excel-based process | F | Period Close Checklist | System-guided checklist (not Blackline/Flowcast) | No | ALIGNS | Checklist customization to KBM needs; timeline reduction goal (from 10 days) |
| REQ-021 | Configure ability to close AP/AR modules separately from GL | F | Period Close | Flexible module closing via checklist | No | ALIGNS | None - standard feature |
| REQ-022 | Open all 13 periods at year start, close progressively | NF | Period Management | Open full year in December, close as go | No | ADAPT | Process change; December reminder critical; avoid opening >1 year ahead |
| REQ-023 | Determine if 15% labor markup (contingency line) will continue in NetSuite | F | Labor Costing | Optional - Matt/Mark decision (impacts commission) | Maybe | ADAPT | Decision pending; if continuing, may require custom script; commission impact |
| REQ-024 | Maintain separate Project GP vs. Commissionable GP reporting and KPIs | F | Project Accounting, Reporting | Two GP metrics for different audiences | Yes | ACCOMMODATE | Custom reporting/dashboards required; role-based visibility; calculation logic |
| REQ-025 | Configure role-based permissions for different GP visibility | NF | Role/Permission Setup | Sales see Commissionable GP; Management sees Project GP | Yes | ACCOMMODATE | Permission design critical; user role definition; testing |
| REQ-026 | Evaluate NetSuite Fixed Asset module vs. continuing Bloomberg | F | Fixed Asset Module | May replace Bloomberg (cost ~$4K) | No | ADAPT | Evaluation required; Bloomberg comparison; migration of existing assets |
| REQ-027 | Configure CSV journal entry import from Paylocity (or new payroll provider) | F | Journal Entry Import | CSV import with department allocation | No | ALIGNS | Provider decision pending; flexible for any provider |
| REQ-028 | Evaluate new HR platform/payroll provider integration | F | Payroll Integration | May change from Paylocity | No | ADAPT | Provider evaluation in progress; CSV approach flexible |
| REQ-029 | Maintain Stripe integration for credit card payment acceptance | F | Payment Processing | Keep Stripe (incidental use, ~$100/year) | No | ALIGNS | No change needed; low priority |
| REQ-030 | Support wire transfer processing for international payments | F | Wire Transfers | International wires (expensive, low volume) | No | ADAPT | Confirm if in Advanced Electronic Bill Payments or manual bank portal |
| REQ-031 | Configure finance charge capability (off by default, available as deterrent) | F | Finance Charges | Available but not used (13 years) | No | ALIGNS | None - standard feature, turned off |
| REQ-032 | Implement pro forma invoice for customer deposit management | F | Pro Forma Invoice | Liability account, auto-apply to invoice | No | ALIGNS | None - standard functionality |
| REQ-033 | Configure vendors that are also customers (Intermarket dealers) | F | Vendor/Customer Setup | Dual setup for Intermarket dealers | No | ALIGNS | Setup process; hundreds of dealers; coordination with Shannon's team |
| REQ-034 | Implement vendor credit limit tracking with warning alerts | F | Vendor Management | Track limits, warn at threshold (90%?) | Yes | ACCOMMODATE | Custom alert/warning required; threshold definition; prevent PO creation? |
| REQ-035 | Define revenue recognition rules and timing (at Sales Order or Invoice) | F | Revenue Recognition | Complex rules by order type; white paper in progress | Yes | ACCOMMODATE | Major design effort; compliance critical; dedicated session needed |
| REQ-036 | Maintain project-level revenue/cost tracking with linked transactions | F | Project Accounting | All transactions linked to project; KPI dashboard | No | ALIGNS | None - standard project accounting |
| REQ-037 | Create real-time financial dashboards to replace manual Excel reports | F | Financial Dashboards | Real-time vs. manual Excel; automated reports | No | ALIGNS | Dashboard design; user requirements; role-based access |
| REQ-038 | Configure project-level KPI dashboards (real-time GP, revenue/cost tracking, commission reporting) | F | Project KPI Dashboards | Project GP, Commissionable GP, real-time tracking | Yes | ACCOMMODATE | Custom dashboard for two GP metrics; role-based visibility; calculation logic |

## Summary Statistics

**Total Requirements**: 38

**By Type:**
- Functional (F): 36
- Non-Functional (NF): 2

**By Approach:**
- ALIGNS: 26 (68%)
- ADAPT: 9 (24%)
- ACCOMMODATE: 3 (8%)

**Requires SolutionDesign (ACCOMMODATE + Complex):**
- REQ-015: Project vs. G&A expense allocation
- REQ-016: Chart of accounts consolidation
- REQ-019: Automated allocations (if implemented - decision pending)
- REQ-023: 15% labor markup (if continued - decision pending)
- REQ-024: Project GP vs. Commissionable GP reporting
- REQ-025: Role-based GP visibility
- REQ-034: Vendor credit limit warning alerts
- REQ-035: Revenue recognition rules
- REQ-038: Project-level KPI dashboards

**Total SolutionDesign Required**: 9 (24%) - plus 2 conditional on decisions

## Key Decisions Pending

1. **REQ-023**: Continue 15% labor markup? (Matt/Mark) - **HIGH IMPACT** on commission
2. **REQ-019**: Implement automated allocations? (Matt/Mark) - Impacts P&L reporting
3. **REQ-013/014**: Expensify vs. RAMP? (Lorraine) - Demo both
4. **REQ-026**: NetSuite FA module vs. Bloomberg? (Lorraine) - Cost-benefit analysis
5. **REQ-027/028**: Continue Paylocity or new provider? (Lorraine/HR) - HR platform evaluation

## High-Risk Requirements

| REQ-ID | Requirement | Risk Description | Mitigation |
|--------|-------------|------------------|------------|
| REQ-016 | Chart of accounts consolidation | Massive change (40+ pages to few hundred); impacts all transactions and reports | Dedicated design session; comprehensive mapping; phased user training; extensive testing |
| REQ-035 | Revenue recognition rules | Complex, compliance-critical; errors impact financials | Dedicated session; white paper review; detailed documentation; auditor involvement |
| REQ-024/025/038 | Project GP vs. Commissionable GP | Custom calculation logic; role-based visibility; commission impact | Detailed requirements session; calculation validation; user acceptance testing |
| REQ-004 | 48-state nexus management | Ongoing compliance; certificate maintenance; audit risk | SuiteTax configuration validation; certificate upload process; expiration monitoring |
| REQ-009 | Advanced Electronic Bill Payments | Critical AP process; high dollar amounts ($3M runs); vendor impact | Thorough testing; parallel run; fallback to NACHA file; remittance confirmation |
| REQ-015 | Project vs. G&A expense allocation | Must work with Expensify/RAMP integration; COGS accuracy | Integration testing; project coding validation; user training |

## Integration Dependencies

| Integration | REQ-IDs | Status | Notes |
|-------------|---------|--------|-------|
| West Coast Community Bank | REQ-008, REQ-009 | Confirmed partner | Positive pay process TBD; wire support TBD |
| Expensify | REQ-013, REQ-015 | Suite App available | Demo needed; project coding verification |
| RAMP | REQ-014, REQ-015 | Alternative option | Demo needed; compare to Expensify |
| Paylocity | REQ-027 | Current provider | May change; CSV approach flexible |
| Stripe | REQ-029 | Current provider | Keep as-is; incidental use |
| TaxConnect | REQ-006 | Being replaced | Transition to SuiteTax eliminates third party |
| Bloomberg | REQ-026 | Evaluation | May replace with NetSuite FA module |

## Sessions Needed for Requirements

### High Priority Sessions:

1. **Revenue Recognition & Project Accounting** (REQ-035, REQ-036)
   - Participants: Lorraine, Kipp, Marcus, Operations
   - Duration: 1-2 hours
   - Critical for financial compliance

2. **Chart of Accounts Design & Mapping** (REQ-016)
   - Participants: Lorraine, Celine, Kevin, Implementation Team
   - Duration: 2-3 hours
   - Foundational to all transactions

3. **Commission Structure & GP Calculation** (REQ-023, REQ-024, REQ-025, REQ-038)
   - Participants: Lorraine, Kipp, Matt, Sales Leadership
   - Duration: 1-2 hours
   - High impact on sales compensation

## Notes

### Traceability:
- All requirements extracted from Questionnaire_FinancialManagement_v1.0.md
- Direct transcript quotes available in questionnaire for each requirement
- Decision authority identified for each pending decision
- Action items and follow-up sessions documented in questionnaire

### Classification Methodology:
- **ALIGNS**: Standard NetSuite functionality with minimal configuration
- **ADAPT**: Requires process change but no customization (e.g., 13 periods vs. 12, approval workflow adjustments)
- **ACCOMMODATE**: Requires custom development, complex configuration, or custom reports/dashboards (e.g., dual GP metrics, COA consolidation, revenue recognition rules)

### Risk Assessment:
- Highest risk: REQ-016 (COA consolidation) and REQ-035 (revenue recognition)
- Change management focus: REQ-016 (COA), REQ-023 (labor markup if changed), REQ-020 (Excel to NetSuite checklist)
- Integration testing critical: REQ-008, REQ-009, REQ-013/014, REQ-015

### Success Factors:
- Lean finance team will appreciate automation (quick wins with bank feeds, expense integration, electronic payments)
- Lorraine's prior experience with modern accounting software (Blackline/Flowcast)
- Kipp's hybrid finance/IT role bridges technical and business needs
- Clear pain points (40+ page COA, 10-day manual close, manual expense processing) drive motivation

---

*End of Requirements Map - Financial Management v1.0*




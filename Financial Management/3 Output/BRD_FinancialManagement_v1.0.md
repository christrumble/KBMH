# Business Requirements Document
## Solution Alignment & Validation

**Financial Management - Accounting, GL, AP, AR, Banking, Reporting & Period Close**

---

## Project Information

| Field | Value |
|-------|-------|
| **Implementation Name** | KB+Hoag Orion Implementation |
| **Customer Name** | KB+Hoag |
| **Solution** | Orion/NetSuite Financial Management Suite |
| **Process Area** | Financial Management |
| **Document Owner** | Implementation Consultant |
| **Document Date** | November 13, 2025 |

### Document Version History

| Revision | Date | Author | Summary |
|----------|------|--------|---------|
| 1.0 | November 13, 2025 | Implementation Team | Initial BRD based on discovery findings, questionnaire v1.1, and requirements map v1.1 |

---

## Executive Summary

KB+Hoag, formed through the merger of KB and Hoag operations, requires a modern, integrated financial management solution to replace their current system built on NetSuite Core. The organization currently operates with significant manual processes, a large and unwieldy chart of accounts (40+ pages), and a 10-day accounting close cycle that relies on Excel-based workflows.

The proven Orion/NetSuite Financial Management solution directly addresses these operational challenges by providing:

- **Integrated financial management** across accounting, banking, accounts payable/receivable, and reporting
- **Automated processes** that eliminate manual steps in payment processing, expense management, and financial reporting
- **Real-time visibility** into project profitability, cash flow, and financial metrics through consolidated dashboards
- **Streamlined period close** with guided checklists and automated processes, reducing close time from 10 days to an estimated 5-7 days
- **Proven capabilities** used by similar furniture dealerships to manage complex project-based accounting

The implementation will validate that standard Orion/NetSuite functionality aligns with KB+Hoag's business requirements, requiring minimal customization while delivering significant operational efficiency gains. Eight critical follow-up discovery sessions have been identified to finalize requirements before the configuration phase, particularly around revenue recognition rules, chart of accounts design, and commission structure decisions.

---

## Financial Management Business Requirements

### Overview of Process Area

Financial management at KB+Hoag encompasses the complete accounting lifecycle: from transaction origination through accounts payable and accounts receivable management, to period-end closing, financial reporting, and compliance. The organization manages consolidated operations across merged KB and Hoag entities, requiring a single subsidiary structure with 13 accounting periods per year (non-standard configuration).

KB+Hoag's finance team is lean but highly skilled, including the CFO/Controller (Lorraine), a hybrid finance/IT specialist (Kipp), and dedicated GL and AP specialists (Celine, Kevin, Guada, and Michael). This team is motivated for modernization, having worked through the merger integration and understanding the limitations of their current system. The team has prior exposure to modern accounting software (Lorraine has used Blackline/Flowcast in previous roles) and is realistic about implementation complexity.

### Current State Challenges

**Current System Limitations:**
- **40+ page Chart of Accounts** - Unwieldy structure with significant redundancy; difficult to manage and report against
- **10-day Manual Period Close** - Excel-based process with manual reconciliations, JEs, and reporting; time-consuming and error-prone
- **Manual Payment Processing** - Requires staff to log into bank portal to upload payment files; extra step in ACH workflow
- **No Automated Reversal Journal Entries** - Manual tracking of reversals, creating audit issues (abandoned in prior system due to tracking challenges)
- **Workaround Tax Processes** - SuiteTax "trick" workaround for use tax in Illinois/Missouri; non-standard approach
- **Manual Expense Reports** - No integrated expense management platform; data must be manually entered into GL
- **No Real-Time Reporting** - Financial reports generated manually; period-over-period analysis requires Excel consolidation
- **Third-Party Fixed Assets Tools** - Bloomberg usage for asset management; adds cost and system integration complexity

**Stakeholder Pain Points:**
- Lorraine: "The 40+ page chart is unwieldy and difficult to manage"
- Kipp: "We had to create a workaround in Core because it wouldn't handle use tax natively"
- Team: "Our 10-day close process is mostly Excel; there's definitely room for optimization"
- Purchasing Team: "We hit vendor credit limits unexpectedly and it creates a mad scramble at the nth hour"

---

## Business Requirements by Functional Area

### 1. Company Structure & Setup (Foundational)

#### Your Business Requirements

**REQ-001:** Configure single NetSuite subsidiary for consolidated KB+Hoag operations (ALIGNS)
- Single subsidiary for merged entity reflects streamlined organizational structure
- Evidence: "Single NetSuite subsidiary... KB + Hoag merged operations... Consolidated financial reporting" - Team decision

**REQ-002:** Implement 13 accounting periods on calendar year basis (ADAPT)
- Non-standard configuration reflecting KB+Hoag's business cycle preference
- Evidence: "I would like 13. 13. Core only does 12. Okay. So it was, like, 13. Yep." - Lorraine
- Implementation Note: Users will need training on 13-period calendar vs. typical 12-period standard

**REQ-003:** Configure US Dollar as single currency (no multi-currency) (ALIGNS)
- Simplified approach appropriate for US-based operations
- Evidence: "We're all in U.S. dollar" - Team

#### Current State Process

KB+Hoag currently operates as a consolidated entity across merged KB and Hoag locations, managed within a single Core subsidiary. The company uses a calendar year with 13 periods (13 four-week periods instead of traditional monthly accounting). All transactions occur in US dollars with no international operations requiring multi-currency handling.

#### Orion/NetSuite Solution

Orion/NetSuite provides robust subsidiary configuration capabilities that align with KB+Hoag's consolidated, single-entity structure. The solution enables straightforward subsidiary setup for merged operations, maintaining clear separation of legal entities where needed while supporting consolidated financial reporting and KPI tracking across the combined organization.

NetSuite fully supports non-standard accounting calendars, including 13-period configurations. While 13 periods represents a departure from NetSuite's default 12-period calendar, this configuration is well-supported by the platform and allows KB+Hoag to continue its established business cycle without requiring workarounds or customization. Period management is centralized, and users access the same period structure across all modules, ensuring consistency.

Currency configuration in NetSuite is straightforward for USD-only operations. By configuring USD as the base currency with no multi-currency processing enabled, KB+Hoag simplifies transaction entry, eliminates currency conversion overhead, and maintains standard reporting processes. This approach is appropriate for the organization's current and foreseeable operations.

#### Future State Process

At go-live, KB+Hoag's finance team will navigate to a simplified subsidiary structure with consolidated KB+Hoag operations managed within a single subsidiary. The 13-period calendar will be automatically applied across all financial modules—no manual period management required. All new transactions will default to USD, and the system will enforce this standard globally.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-001 | Single subsidiary for KB+Hoag | Subsidiary configuration and consolidation | ALIGNS |
| REQ-002 | 13 accounting periods (non-standard) | Custom calendar support | ADAPT |
| REQ-003 | US Dollar only (no multi-currency) | Currency setup and transaction defaults | ALIGNS |

---

### 2. Tax Management (Compliance-Critical)

#### Your Business Requirements

**REQ-004:** Implement native SuiteTax for 48-state nexus management with automatic calculation (ALIGNS)
- Automatic tax calculation based on ship-to address across all nexus states
- Evidence: "48 states with nexus registration... Automatic calculation based on ship-to address... Native SuiteTax (not Avalara)" - Team decision
- Implementation Note: Native SuiteTax eliminates third-party Avalara dependency; significant advantage for compliance automation

**REQ-005:** Configure tax exemption certificate management with expiration tracking and dashboard (ALIGNS)
- Proactive certificate expiration monitoring prevents compliance violations
- Evidence: "Tax exemption certificate management... Effective date tracking... Dashboard for expiring certificates... Compliance reporting" - Discovery discussion

**REQ-006:** Configure SuiteTax for use tax handling in Illinois and Missouri (ALIGNS)
- Eliminates current "trick" workaround that has required non-standard Core configuration
- Evidence: "CORE won't do use tax, so we have to kind of trick it" - Kipp; "SuiteTax handles this natively" - Marcus
- Strategic Benefit: Removes workaround dependency, improving system reliability and audit compliance

**REQ-007:** Enable gross receipts tax reporting by ship-to location (ALIGNS)
- Standard ship-to location reporting supports revenue aggregation by region
- Evidence: "We need the sales revenue number based on ship to location... isn't ship to location the standard way of calculating it" - Kipp/Marcus

#### Current State Process

KB+Hoag currently manages tax compliance across 48 states with nexus registration. Tax calculation is complex, requiring manual verification across multiple state jurisdictions. Use tax handling in Illinois and Missouri requires a workaround in Core that was not natively supported. Tax exemption certificates are tracked, but expiration monitoring is manual, creating compliance risk. Gross receipts tax reporting requires manual consolidation by ship-to location.

#### Orion/NetSuite Solution

Orion/NetSuite delivers comprehensive tax management through native SuiteTax integration, which automatically calculates sales tax for all 48 states where KB+Hoag has nexus. SuiteTax determines applicable tax rates and rules based on ship-to addresses, transaction types, and customer tax status—all without manual intervention. This eliminates the need for Avalara or other third-party tax engines and ensures consistency across all transactions.

Use tax handling in Illinois and Missouri is fully supported through SuiteTax, eliminating the workaround currently required in Core. NetSuite's native approach ensures proper tax treatment for these jurisdictions while maintaining audit compliance. Tax exemption certificates are managed within SuiteTax with automatic expiration tracking and dashboard alerts, enabling proactive compliance monitoring. When certificates approach expiration, the dashboard flags them for renewal, preventing accidental tax charging on exempt transactions.

Gross receipts tax reporting integrates directly with transaction data, automatically aggregating revenue by ship-to location without manual consolidation. Standard NetSuite reports provide this view natively, supporting both compliance reporting and business intelligence analysis.

#### Future State Process

At transaction entry, NetSuite will automatically calculate appropriate sales tax based on ship-to address and customer tax classification. For exempt customers, users will reference current exemption certificates, with the system alerting if certificates are near expiration. At period end, tax reporting by state and location will be available through standard reports without manual consolidation. Compliance validation will occur through SuiteTax's built-in reporting, significantly reducing manual compliance effort.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-004 | 48-state nexus, auto-calculation | Native SuiteTax with 48-state support | ALIGNS |
| REQ-005 | Certificate expiration tracking | SuiteTax certificate management and dashboard | ALIGNS |
| REQ-006 | Use tax for IL/MO (no workaround) | Native SuiteTax use tax support | ALIGNS |
| REQ-007 | Gross receipts reporting by location | Standard SuiteTax location-based reporting | ALIGNS |

---

### 3. Banking & Cash Management (Operational Efficiency)

#### Your Business Requirements

**REQ-008:** Implement bank feeds integration with West Coast Community Bank (ALIGNS)
- Automatic daily transaction import eliminates manual bank reconciliation data entry
- Evidence: "West Coast Community Bank... Confirmed as part of NetSuite Bank Feeds program... Automatic transaction feed into NetSuite" - Discovery discussion
- Implementation Note: West Coast Community Bank is confirmed NetSuite partner; integration is straightforward

**REQ-009:** Enable Advanced Electronic Bill Payments for ACH directly from NetSuite (ALIGNS)
- ACH payment submission directly from NetSuite eliminates bank portal login step
- Evidence: "Advanced Electronic Bill Payments (part of edition)... Pay via ACH directly from NetSuite... Skip manual bank portal upload step" - Marcus
- Implementation Note: Significantly streamlines AP workflow for Guada and Michael

**REQ-010:** Configure bill payment approval workflow with Lorraine as approver (ADAPT)
- Structured workflow with Lorraine as final approver maintains financial controls
- Evidence: "Guada or Michael compile proposed payment run... Bring to Lorraine with amounts... Lorraine reviews and approves... Sometimes $3M" - Process description
- Outstanding Item: Workflow details require clarification in SESSION 5 (Can Lorraine remove items in-system? Approval mechanism? Remittance confirmation process?)

**REQ-011:** Enable Cash360 Dashboard for cash flow forecasting (ALIGNS)
- Real-time cash position and forecasting visibility supports financial planning
- Evidence: "Cash360 Dashboard... Cash flow forecasting functionality... Part of configured system" - Marcus

**REQ-012:** Configure credit card reconciliation as bank account (upload statement, auto-match) (ALIGNS)
- Credit card treated as bank account with statement import and auto-matching
- Evidence: "Treat credit card like another bank account... Upload statement (likely CSV)... Use same reconciliation process" - Marcus

#### Current State Process

KB+Hoag currently uses West Coast Community Bank for primary operations. Payment processing requires staff to prepare a payment list, bring it to Lorraine for approval, then manually log into the bank portal to upload ACH payment files—an extra step in the workflow. Bank reconciliation requires manual data entry from bank statements. Credit card reconciliation follows a separate process. Cash flow visibility is limited to manual Excel consolidation.

#### Orion/NetSuite Solution

Orion/NetSuite provides integrated banking capabilities that dramatically simplify KB+Hoag's cash management processes. Through the Bank Feeds Suite App, West Coast Community Bank transactions automatically flow into NetSuite daily, eliminating manual statement entry. The system matches incoming deposits, payments, and other transactions to existing records, with exceptions flagged for manual review. This automation reduces reconciliation time from days to hours and improves cash visibility.

Advanced Electronic Bill Payments enables Guada and Michael to prepare ACH payments directly within NetSuite, with Lorraine approving through the system's workflow interface. Once approved, payments are submitted electronically to the bank for processing—no manual bank portal upload required. This streamlines the process, reduces error potential, and creates an audit trail of approvals within the financial system.

NetSuite's Cash360 Dashboard provides real-time visibility into KB+Hoag's cash position across all accounts, including forecasting based on pending transactions, receivables, and payables. Lorraine and finance leadership can view projected cash flow for planning and decision-making without manual consolidation. The dashboard updates automatically, ensuring decision-makers always have current information.

Credit card reconciliation is simplified by treating the corporate card as a bank account within NetSuite. Statement files (CSV format) are imported using the same bank reconciliation process, with transactions auto-matched to expenses. This unified approach reduces training needs and creates consistency across all account reconciliation.

#### Future State Process

Each morning, NetSuite automatically imports transactions from West Coast Community Bank and other connected accounts. Finance staff review exceptions and match remaining items. When payment runs are needed, Guada and Michael prepare them in NetSuite. Lorraine reviews the proposed payment list in-system, approves (or removes items as needed), and submits. NetSuite sends the ACH file electronically to the bank—no manual portal login required. Credit card reconciliation follows the same import-and-match process, eliminating separate processes.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-008 | Bank feeds from West Coast Community | Bank Feeds Suite App integration | ALIGNS |
| REQ-009 | ACH payments directly from NetSuite | Advanced Electronic Bill Payments | ALIGNS |
| REQ-010 | Bill payment approval workflow | Workflow approval engine with Lorraine as approver | ADAPT |
| REQ-011 | Cash360 forecasting dashboard | Native Cash360 Dashboard | ALIGNS |
| REQ-012 | Credit card as bank account, auto-match | Bank reconciliation for card statements | ALIGNS |

#### Implementation Considerations

- **SESSION 5 Required:** Bill payment workflow details (approval mechanism, item removal capability, remittance process)
- **Bank Integration Testing:** Comprehensive testing with West Coast Community Bank before go-live
- **Positive Pay Process:** Confirm if currently used with bank; if so, integrate into payment workflow
- **Wire Transfer Handling:** Clarify if Advanced Electronic Bill Payments supports wires or if manual bank portal required
- **Payment Exception Handling:** Define procedures for failed ACH attempts and retry processes

---

### 4. Expense Management (User Adoption Focus)

#### Your Business Requirements

**REQ-013:** Evaluate and implement Expensify integration via Suite App (ALIGNS)
- Expensify Suite App available for automatic sync from Expensify to NetSuite
- Evidence: "Expensify Integration (Suite App available)... Absolutely talk to each other. You can just sync data... Automated data sync from Expensify to NetSuite" - Discovery discussion
- Outstanding Item: **DECISION PENDING** - Expensify vs. RAMP platform choice requires SESSION 6

**REQ-014:** Evaluate RAMP as alternative to Expensify with NetSuite integration (ALIGNS)
- RAMP offers NetSuite integration with potentially better mobile UX
- Evidence: "Lorraine interested in moving from Expensify to RAMP... RAMP has NetSuite integration too... Could potentially demo both" - Discovery discussion
- Strategic Note: "Receipt capture from phone, boom, get assigned" - appealing UX for users
- Outstanding Item: **DECISION PENDING** - RAMP vs. Expensify platform choice requires SESSION 6

**REQ-015:** Support project vs. G&A allocation for expense reports (ACCOMMODATE)
- Dual allocation structure distinguishes project costs (COGS) from general overhead
- Evidence: "We have two different... our cost structure. our COA, we had to create a cost to go into cost of goods sold, specifically identified as a project cost, and then we have general G&A-type stuff" - Lorraine
- Implementation Note: Requires integration between expense platform and NetSuite project coding
- Outstanding Item: Determine if line-level or report-level project coding required (SESSION 6)

#### Current State Process

KB+Hoag currently uses Expensify for expense management. Users submit expense reports through Expensify, requiring manual entry into the GL by project vs. G&A classification. Some users express frustration with the Expensify interface. Expense data sync to NetSuite is not currently automated, creating delays and data entry errors. Project coding must be done manually after expense submission.

#### Orion/NetSuite Solution

Orion/NetSuite enables seamless integration with both Expensify and RAMP through Suite App integrations, eliminating manual data entry between the expense platform and NetSuite. With Expensify Suite App, expense reports submitted in Expensify automatically sync to NetSuite with project and GL coding attached—no manual entry required. The same capability is available through RAMP, which additionally offers a modern mobile interface with receipt capture ("receipt capture from phone, boom, get assigned") that may improve user adoption and submission frequency.

The integration automatically allocates expenses to the correct GL accounts based on project vs. G&A classification coded during expense entry. This ensures accurate project costing without manual GL reconciliation. Real-time project cost tracking becomes possible, supporting the KPI dashboard requirements (REQ-038).

Both platforms (Expensify and RAMP) support line-level project coding, allowing expenses to be precisely attributed to the correct project and cost type. This level of detail enables accurate project-level GP calculations (REQ-024) and supports the revenue recognition process (REQ-035).

#### Future State Process

Users submit expense reports in their chosen platform (Expensify or RAMP), coding each line item with a project and GL account. The platform automatically syncs to NetSuite, creating expense entries with correct project and GL coding. Finance staff review for approval (if workflows require it), and expenses automatically post to the GL in real-time. Project dashboards immediately reflect updated project costs. No manual GL entry required—significant efficiency gain.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-013 | Expensify Suite App integration | Native Suite App available | ALIGNS |
| REQ-014 | RAMP integration option | RAMP NetSuite integration available | ALIGNS |
| REQ-015 | Project vs. G&A allocation | Line-level project coding in platforms | ACCOMMODATE |

#### Implementation Considerations

- **SESSION 6 Required:** Platform selection (Expensify vs. RAMP); demo both before decision
- **User Preference Assessment:** Gather input from current Expensify users on RAMP mobile UX
- **Project Coding Requirements:** Define if line-level or report-level coding is required
- **Approval Workflow:** Confirm if expense approvals needed before GL posting
- **Cost Analysis:** Compare Expensify vs. RAMP annual costs for budget planning
- **Change Management:** If switching to RAMP, plan training and cutover strategy

---

### 5. Chart of Accounts & Data Migration (Foundational)

#### Your Business Requirements

**REQ-016:** Consolidate chart of accounts from 40+ pages to few hundred accounts (ACCOMMODATE)
- Significant reduction in account structure improves usability and reporting
- Current State: "40+ pages of accounts in Core... Unwieldy and difficult to manage... Target: Few hundred accounts" - Discovery discussion
- Implementation Note: Major design effort; all transactions and reports depend on this structure
- Outstanding Item: **SESSION 2 REQUIRED** - Detailed COA design, mapping, and account numbering scheme
- Critical Pre-Work: Export current Core COA with usage frequency analysis

**REQ-017:** Migrate historical financial data back to 2017 (trial balances, period-over-period) (ALIGNS)
- 8 years of historical data (2017-2025) supports trend reporting and audit requirements
- Evidence: "Back to 2017 (Lorraine's decision)... Historical data back to 2017... Older data exported and archived" - Lorraine
- Implementation Note: Dependent on REQ-016 completion (new COA structure must be finalized first)

#### Current State Process

KB+Hoag currently maintains a 40+ page chart of accounts in NetSuite Core. The large structure reflects accumulated account additions without consolidation. Some accounts are duplicated, others rarely used, and the overall structure is difficult for users to navigate. Reporting requires manual consolidation across many accounts. Historical data from 2017 forward is maintained in Core.

#### Orion/NetSuite Solution

Orion/NetSuite's flexible account structure enables KB+Hoag to consolidate from 40+ pages to a streamlined few hundred accounts while maintaining financial reporting accuracy. Through strategic use of NetSuite's Class, Department, and Project dimensions, the new structure can significantly reduce account proliferation while maintaining all reporting needs. Rather than creating new accounts for each cost center or project type, these dimensions provide the granularity users need without account explosion.

The chart of accounts redesign represents a foundational effort that will improve system usability, reporting clarity, and financial analysis. NetSuite's Account Mapping and CoA tools support this transformation, allowing historical data to be properly reclassified to the new structure. Comprehensive mapping documentation will be created to ensure all transactions transition correctly.

Historical data migration from Core will map to the new chart of accounts structure, maintaining 8 years of period-over-period reporting capability. NetSuite supports flexible data import, allowing trial balances and historical period closings to be imported with proper account mapping. This ensures Lorraine's requirement for historical trend analysis is fully supported.

#### Future State Process

KB+Hoag will operate with a consolidated, few-hundred-account chart of accounts organized by logical business categories: revenue streams, COGS by type, operating expenses by function, balance sheet accounts, and equity. Project-level detail that previously required separate accounts is now captured through project coding. Users will find the new structure more intuitive and reporting will be clearer. Historical reporting remains available through account mapping, showing prior-year data reclassified to current structure for true period-over-period comparison.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-016 | 40+ page COA to few hundred accounts | Custom COA design with dimension-based structure | ACCOMMODATE |
| REQ-017 | Historical data 2017-2025 with mapping | Data import with CoA mapping | ALIGNS |

#### Implementation Considerations

- **SESSION 2 REQUIRED:** Chart of Accounts design and mapping (URGENT - foundational)
- **Pre-Work:** Export complete current Core COA with GL balances and transaction frequency by account
- **Design Effort:** 2-3 hours with finance team to identify most-used accounts, consolidation opportunities, and new structure
- **Mapping Documentation:** Comprehensive mapping document from old to new COA for user reference
- **User Training:** Significant training required for new account numbers and structure
- **Account Numbering Scheme:** Define new numbering logic (e.g., 1xxx = Revenue, 4xxx = COGS, etc.)
- **Testing:** Validate that all transactions map correctly to new structure in test environment
- **Parallel Validation:** Consider running new COA in parallel with old for first period to validate accuracy

---

### 6. Journal Entries & Allocations (Automation)

#### Your Business Requirements

**REQ-018:** Enable CSV import of journal entries with automated reversal capability (ALIGNS)
- CSV import supports payroll entries from Paylocity with automatic reversal capability
- Evidence: "CSV import of journal entries... Payroll entries imported from Paylocity... Automated reversal journal entries" - Discovery discussion
- Strategic Benefit: Addresses prior tracking issues that caused reversal JE abandonment in Core

**REQ-019:** Determine if automated allocation transactions will be implemented (ADAPT)
- Optional feature; decision pending with leadership (Matt/Mark)
- Evidence: "Optional to implement... Decision pending with leadership... I don't know that he knows that he wants to, or doesn't... These numbers were never offered heavy" - Discovery discussion
- Outstanding Item: Leadership decision required before configuration

#### Current State Process

KB+Hoag currently imports payroll entries from Paylocity as CSV files, manually entering them as journal entries in the GL. Reversal journal entries were abandoned in Core due to tracking complexity—manual reversals create errors and audit confusion. Any allocation transactions are handled outside the system.

#### Orion/NetSuite Solution

Orion/NetSuite provides native CSV import capability for journal entries, enabling a direct integration with Paylocity (or any other system producing CSV output). This eliminates manual JE entry and ensures payroll charges flow to the GL accurately and consistently. More importantly, NetSuite's native reversal journal entry functionality includes automatic tracking and reversal scheduling, solving the tracking issues that caused abandonment in Core. Users can set reversals to occur automatically on a specified date—no manual tracking required, no audit confusion.

Automated allocation transactions are a standard NetSuite feature, available for implementation if KB+Hoag decides to use them. These allocations can be scheduled to run regularly, applying formulas or percentages to charge costs across departments or projects. If leadership approves this capability, NetSuite provides the infrastructure; if not approved, simpler methods can accomplish needed allocations.

#### Future State Process

Each payroll period, CSV files from Paylocity are imported through a standard import process. Journal entries post to the GL automatically with proper account coding. If reversals are needed (rare for payroll, more common for period-end entries), reversal JEs are scheduled automatically—no manual tracking. If automated allocations are approved, NetSuite will automatically apply allocation formulas on a schedule, eliminating manual allocation processes.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-018 | CSV JE import with auto-reversal | Native JE import and reversal capability | ALIGNS |
| REQ-019 | Automated allocations (optional) | Standard allocation module (decision pending) | ADAPT |

#### Implementation Considerations

- **CSV Import Specification:** Define exact CSV format expected from Paylocity
- **Paylocity Integration:** Confirm current CSV export capability; if changing payroll providers, ensure new provider supports CSV export
- **Reversal Rules:** Define which JEs require reversals and scheduling rules
- **SESSION 3 Related:** REQ-019 allocation decision affects commission and GP calculations
- **Testing:** Validate that CSV imports create correct GL postings with no manual intervention needed

---

### 7. Period Close Process (Operational Efficiency)

#### Your Business Requirements

**REQ-020:** Implement NetSuite Period Close Checklist to replace Excel-based process (ALIGNS)
- System-guided period close process replaces current 10-day Excel workflow
- Evidence: "10 days to close accounting period... All managed via Excel... NetSuite: Built-in Checklist... Step-by-step process" - Discovery discussion
- Strategic Goal: Reduce close timeline from 10 days to estimated 5-7 days
- Outstanding Item: SESSION 4 required for detailed close process optimization

**REQ-021:** Configure ability to close AP/AR modules separately from GL (ALIGNS)
- Flexible module closing enables AP/AR to close before GL if ready
- Evidence: "Can close AP/AR separately and go through checklist... Flexible closing process... Close modules as ready" - Marcus best practice

**REQ-022:** Open all 13 periods at year start, close progressively (ADAPT)
- Open full year at once (December) instead of opening periods one at a time
- Evidence: "Open entire year at once... Set December reminder to open next year... Don't open more than one year ahead" - Marcus best practice
- Implementation Note: Process change for finance team; requires December year-end task

#### Current State Process

KB+Hoag currently closes accounting periods over 10 days using an Excel-based workflow. The close process includes manual reconciliations, journal entry consolidation, and manual report generation. All steps are tracked in spreadsheets rather than the financial system. Periods are opened one at a time rather than in bulk. The process is sequential rather than using parallel workflows where possible.

#### Orion/NetSuite Solution

Orion/NetSuite provides a native Period Close Checklist feature that guides finance staff through close procedures step-by-step, eliminating manual tracking of close activities in Excel. The checklist includes configurable tasks, assigned owners, and deadline tracking. As staff complete tasks (reconciliations, JEs, etc.), they mark them complete in the system. The checklist provides visibility into close progress and prevents premature GL closing until all prerequisites are met.

By moving from an Excel-based process to a system-guided workflow, KB+Hoag can reduce close time from 10 days to an estimated 5-7 days. This improvement comes from: (1) elimination of manual step tracking, (2) parallel processing where possible (AP/AR can close separately from GL), (3) automated reconciliation matching, and (4) system-driven reports eliminating manual consolidation. Lorraine, with her prior Blackline/Flowcast experience, will recognize this approach as best-practice close management.

NetSuite supports flexible module closing, enabling AP and AR to be closed in the period checklist at different times than the GL. If AP reconciliations complete early, that module can be closed without waiting for GL reconciliation. This flexibility enables parallel workflows and earlier close start for faster overall completion.

Period opening can be configured to open the full calendar year at once (all 13 periods) during December year-end planning. This eliminates the need to open periods one at a time and ensures the full year is available for planning and cutoff testing. A system reminder can be set to remind staff in December to open the following year.

#### Future State Process

In early December, system reminder alerts the finance team to open the next 13 accounting periods. With one click, all periods are created for the upcoming year. When a period close begins, the checklist is automatically generated with all standard close procedures: bank reconciliations, AP/AR aging reviews, inter-company reconciliations, recurring JE posting, etc. Team members access the checklist from their dashboard, mark tasks complete as they finish them, and the system prevents GL closing until all prerequisite tasks are done.

AP/AR close in parallel with GL close if ready. A typical close might proceed: AP completes reconciliation on day 2, marks AP module closed; AR completes on day 3, marks AR module closed; GL completes remaining reconciliations on days 4-5 and closes GL. Overall close timeline of 5-7 days—compressed from the current 10 days.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-020 | Period Close Checklist (vs. Excel) | Native Period Close Checklist module | ALIGNS |
| REQ-021 | Close AP/AR separately from GL | Flexible module closing in checklist | ALIGNS |
| REQ-022 | Open full year at once | Bulk period creation and year-end automation | ADAPT |

#### Implementation Considerations

- **SESSION 4 REQUIRED:** Detailed close process optimization
- **Pre-Work:** Document current 10-day Excel-based close process step-by-step
- **Bottleneck Analysis:** Identify which steps take longest; prioritize optimization
- **Reconciliation Requirements:** Define frequency and timing for bank, AP/AR, and inter-company reconciliations
- **Checklist Customization:** Configure NetSuite checklist with KBM-specific procedures
- **Close Procedure Documentation:** Create written procedures for each close task
- **Timeline Validation:** Confirm 5-7 day target is realistic based on detailed process review
- **Training:** Train finance staff on new NetSuite checklist process
- **Parallel Running:** Run Excel close in parallel with NetSuite for first few cycles to validate accuracy

---

### 8. Labor Markup & Costing (Strategic Decision)

#### Your Business Requirements

**REQ-023:** Determine if 15% labor markup (contingency line) will continue in NetSuite (ADAPT)
- Current practice: 15% contingency added to all labor cost estimates; impacts commission calculations
- Evidence: "That may be up for debate as to whether or not we would want to keep that... Matt and Mark decision... Commission is paid on that... Can be replicated in NetSuite if continuing" - Kipp
- Outstanding Item: **CRITICAL DECISION REQUIRED** - Matt/Mark (Leadership) must decide before configuration
- Strategic Impact: HIGH - Affects sales compensation structure and custom development scope

**REQ-024:** Maintain separate Project GP vs. Commissionable GP reporting and KPIs (ACCOMMODATE)
- Dual reporting: True project gross profit vs. gross profit used for commission calculations
- Evidence: "That's why we have two... that's why we have a different set of KPIs. So, we have a set of KPIs for project gross profit, and then we have commissionable gross profit" - Kipp
- Outstanding Item: SESSION 3 required for detailed GP calculation and reporting requirements

**REQ-025:** Configure role-based permissions for different GP visibility (ACCOMMODATE)
- Sales sees Commissionable GP (reflects commission basis); Management sees true Project GP
- Evidence: "Permission Control: Different people see different KPIs... Role-based visibility... Sales may see commissionable GP... Management sees true project GP" - Discussion
- Outstanding Item: SESSION 3 required for role-based visibility matrix

#### Current State Process

KB+Hoag currently applies a 15% contingency markup to all labor cost estimates in Core. This markup is included in project revenue calculations and affects gross profit calculations. Commission calculations are based on the commissionable GP (including the 15% markup), not the true project GP. Management tracks both metrics separately using different KPI sets. Real-time visibility into both GP metrics is limited.

#### Orion/NetSuite Solution

Orion/NetSuite provides flexible project accounting capabilities that support both current-state practices (if the 15% markup continues) and alternative approaches (if eliminated). The solution includes:

**If 15% Markup Continues:** NetSuite supports labor markup through project costing rules or custom script development. Revenue recognized would include the contingency markup, and commission calculations would be based on commissionable GP (markup included). The Project Record module aggregates real-time project financial metrics, and custom dashboards can display both Project GP (true profit) and Commissionable GP (markup-included profit) simultaneously. Role-based visibility ensures sales teams see commissionable GP while management sees true project GP.

**If 15% Markup is Eliminated:** NetSuite project accounting uses actual labor costs without markup, and both teams view the same true project GP. This simplifies reporting and eliminates dual GP tracking. Commission structures would need to be recalibrated based on true project profitability.

The Commission Module within Orion/NetSuite automates commission calculations based on defined rules. Whether commissions are based on true project GP or commissionable GP (with markup), the module supports flexible calculation logic. Event-driven triggers ensure commissions are calculated at the appropriate project milestone (booking, invoice, or payment collection).

#### Future State Process

Once leadership makes the 15% markup decision, NetSuite will be configured accordingly:

**Scenario A (Markup Continues):** Project revenue includes 15% contingency markup. Revenue recognition captures this. Commissionable GP (with markup) is automatically calculated and displayed on sales dashboards. Management dashboards show true project GP (without markup). Commissions are calculated monthly based on commissionable GP. Both metrics flow to the KPI dashboard (REQ-038) with role-based visibility.

**Scenario B (Markup Eliminated):** Project revenue reflects actual labor costs without contingency. All stakeholders view the same true project GP. Commissions are recalculated based on true project profitability. KPI dashboards show single GP metric. Commission structure needs communication to sales team.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-023 | 15% labor markup decision | Flexible project costing (depends on leadership decision) | ADAPT |
| REQ-024 | Project GP vs. Commissionable GP tracking | Dual GP calculation and Project Record | ACCOMMODATE |
| REQ-025 | Role-based GP visibility | Permission configuration and custom dashboards | ACCOMMODATE |

#### Implementation Considerations

- **SESSION 3 REQUIRED:** Commission structure and GP calculation deep dive
- **Leadership Decision:** Matt/Mark MUST decide on 15% markup before configuration begins
- **Commission Structure Documentation:** If continuing markup, detail commission calculation rules
- **Dashboard Requirements:** Define specific KPI requirements for both GP metrics
- **Role Definitions:** Define user roles and GP visibility permissions
- **Custom Development Scope:** If continuing 15% markup, evaluate if custom scripts required or standard config sufficient
- **Sales Team Communication:** If eliminating markup, plan communication strategy and Q&A
- **Testing:** Validate commission calculations using historical data from current system

---

### 9. Fixed Asset Management (Strategic Decision)

#### Your Business Requirements

**REQ-026:** Evaluate NetSuite Fixed Asset module vs. continuing Bloomberg (ADAPT)
- Current: Bloomberg for fixed asset management and depreciation
- Opportunity: NetSuite Fixed Asset module may eliminate third-party tool
- Evidence: "I just want to know if NetSuite can meet our needs, and do we need that fixed asset stuff? [Currently] paying for a third party to do that. Bloomberg." - Lorraine; "I think the fixed asset module's gonna handle what you need." - Marcus
- Outstanding Item: **DECISION REQUIRED** - Evaluate NetSuite FA module vs. Bloomberg; cost-benefit analysis

#### Current State Process

KB+Hoag currently uses Bloomberg for fixed asset management, including depreciation calculations, asset tracking, and reporting. Bloomberg adds cost (approximately $4K annually based on discussion) and requires separate system management from NetSuite Core. Asset depreciation is calculated outside NetSuite.

#### Orion/NetSuite Solution

Orion/NetSuite includes a native Fixed Asset module that provides comprehensive asset management, depreciation scheduling, and reporting capabilities. The module supports multiple depreciation methods (straight-line, declining balance, MACRS, Section 179), book vs. tax depreciation tracking, and automated annual depreciation schedules.

If NetSuite's Fixed Asset module meets KB+Hoag's needs, adopting it would eliminate the Bloomberg cost (~$4K annually), eliminate separate system management, and integrate asset depreciation directly into GL closing procedures. Asset disposals would automatically generate proper GL entries, and asset-level reporting would be available without manual consolidation.

Migration from Bloomberg to NetSuite FA would involve importing existing assets, establishing depreciation schedules matching current Bloomberg rules, and testing to ensure all prior depreciation transfers correctly. This is a straightforward data conversion for a well-understood asset population.

#### Future State Process

If NetSuite FA is adopted: Asset acquisitions are recorded in NetSuite with proper asset class and depreciation method. Annual depreciation is calculated automatically according to defined schedules. During period close, depreciation journal entries are generated and post to the GL. Asset disposal triggers automatic GL entries for gain/loss. Bloomberg is discontinued, eliminating redundant system costs.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-026 | NetSuite FA module vs. Bloomberg | Native Fixed Asset module evaluation | ADAPT |

#### Implementation Considerations

- **SESSION 7 REQUIRED:** Fixed asset module evaluation and decision
- **Bloomberg Comparison:** Document current Bloomberg features and cost
- **Current Assets:** Export current asset population from Bloomberg with depreciation schedules
- **NetSuite FA Capability Review:** Confirm NetSuite FA module supports all depreciation methods used by KB+Hoag
- **Cost-Benefit Analysis:** Compare Bloomberg annual cost vs. NetSuite FA implementation effort
- **Migration Plan:** If adopting NetSuite FA, plan asset data import and depreciation schedule setup
- **Testing:** Validate depreciation calculations match Bloomberg rules for existing assets

---

### 10. Payroll Integration (Flexible Integration)

#### Your Business Requirements

**REQ-027:** Configure CSV journal entry import from Paylocity (or new payroll provider) (ALIGNS)
- Payroll system integration through CSV-based journal entry import
- Evidence: "CSV download from Paylocity... Journal entry import to NetSuite... Department Allocation: Allocations done before import" - Current process
- Flexible: Works with any payroll provider supporting CSV export (not Paylocity-specific)

**REQ-028:** Evaluate new HR platform/payroll provider integration (ADAPT)
- Current: Paylocity; evaluation underway for potential change
- Evidence: "Paylocity: Current payroll provider... May change (evaluation ongoing)... HR platform evaluation in progress" - Discovery discussion
- Outstanding Item: Decision pending on new HR/payroll platform

#### Current State Process

KB+Hoag currently uses Paylocity for payroll processing. Payroll entries are downloaded as CSV files and manually entered as journal entries in the GL. Department allocations are done before import to ensure proper GL coding.

#### Orion/NetSuite Solution

Orion/NetSuite supports flexible payroll integration through CSV-based journal entry import. This approach is provider-neutral—whether using Paylocity, Guidepoint, ADP, or any other payroll system—if the provider exports CSV data, NetSuite can import it. This flexibility protects KB+Hoag's investment during payroll platform evaluation.

The import process is identical regardless of payroll provider: CSV file from payroll system → NetSuite import → journal entries post to GL with proper department/project coding. Department allocations can be done in the payroll system before export (current approach) or in NetSuite before posting, depending on workflow preference.

If KB+Hoag selects a new HR/payroll platform as part of the broader implementation, the CSV import approach continues to work. No custom integration required—standard NetSuite functionality handles the process.

#### Future State Process

Each payroll period, CSV file from Paylocity (or new payroll provider if selected) is exported. File is imported to NetSuite using standard JE import process. Entries post to GL with proper coding. No manual data entry required. Department allocations are already embedded in the import file, so GL posting is complete.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-027 | CSV JE import from Paylocity | Standard JE import (provider-neutral) | ALIGNS |
| REQ-028 | Evaluate new HR/payroll provider | CSV approach works with any provider | ADAPT |

#### Implementation Considerations

- **CSV Format Specification:** Define exact CSV format expected from Paylocity (and new provider if selected)
- **Department Coding:** Confirm department allocation is done in payroll system or in NetSuite post-import
- **Payroll Platform Decision:** If changing providers, ensure new provider supports CSV export capability
- **Testing:** Validate payroll imports create correct GL entries with proper coding
- **Timeline:** HR/payroll evaluation should be completed before configuration phase

---

### 11. Payment Processing (Integration Simplification)

#### Your Business Requirements

**REQ-029:** Maintain Stripe integration for credit card payment acceptance (ALIGNS)
- Current: Stripe for credit card payments on invoices
- Approach: Keep Stripe; minimal use (~$100/year); working well
- Evidence: "Payment link embedded in invoice hyperlink... Very rare we take a credit card... Stripe: Transaction-based pricing only... Stay with Stripe currently (works fine, incidental use)" - Discussion

**REQ-030:** Support wire transfer processing for international payments (ADAPT)
- Current: Wire transfers for international payments (expensive, low volume)
- Approach: Determine if Advanced Electronic Bill Payments supports wires or if manual bank portal required
- Evidence: "Wires restricted to international (expensive)... Module question: ACH only or wire support too?... If not integrated: Manual entry in bank portal" - Discussion
- Outstanding Item: SESSION 5 clarification required (wire support in Advanced Electronic Bill Payments)

#### Current State Process

KB+Hoag currently accepts credit card payments through Stripe embedded in invoice hyperlinks. Usage is rare (~$100/year costs). Wire transfers for international payments are processed manually through the bank portal. Volume is low but important for vendor relationships.

#### Orion/NetSuite Solution

Orion/NetSuite maintains Stripe integration for credit card acceptance. The approach remains unchanged—payment links embedded in invoices, transaction-based pricing, minimal cost for low-volume usage. NetSuite's native Stripe connector handles payment processing and reconciliation to AR.

For wire transfers, NetSuite's Advanced Electronic Bill Payments module supports both ACH and wire transfer processing, depending on bank capabilities. West Coast Community Bank should be queried to confirm wire support. If supported, wires can be submitted directly from NetSuite using the same approval workflow as ACH payments—no bank portal login required. If not supported, wire transfers would continue through manual bank portal entry (low frequency, acceptable workaround).

#### Future State Process

Credit card payments continue as they do now—payment links in invoices, transactions processed through Stripe, minimal cost, no change to workflow.

For wire transfers: If bank supports wire processing through NetSuite, wires are prepared in NetSuite, approved by Lorraine, and submitted electronically. If not supported, wire instructions are prepared in NetSuite but submitted manually through bank portal (rare occurrence, low operational impact).

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-029 | Stripe payment acceptance (maintain) | Native Stripe integration | ALIGNS |
| REQ-030 | Wire transfer support (international) | Potentially via Advanced Electronic Bill Payments | ADAPT |

#### Implementation Considerations

- **SESSION 5 Required:** Confirm wire transfer support with West Coast Community Bank
- **Stripe Configuration:** Verify current Stripe setup works with NetSuite; no changes needed
- **Wire Transfer Fallback:** If wires not supported in NetSuite, document manual process

---

### 12. Customer Financial Management (Controls & Processes)

#### Your Business Requirements

**REQ-031:** Configure finance charge capability (off by default, available as deterrent) (ALIGNS)
- Current: Not used in 13 years; available as threat/deterrent for customer late payments
- Approach: Configure but leave off by default; available if policy changes
- Evidence: "Never implemented in 13 years (Lorraine)... Deterrent/threat only... Most dealers want to threaten. They don't actually follow through" - Lorraine

**REQ-032:** Implement pro forma invoice for customer deposit management (ALIGNS)
- Current: Not formalized; deposits tracked manually
- Approach: Pro forma invoice creates liability (not revenue), auto-applies to final invoice
- Evidence: "Not revenue-recognizing transaction... Liability account... Deposit collection... Automatically applies to final invoice when generated" - Discovery discussion

#### Current State Process

KB+Hoag has never implemented finance charges on customer invoices despite having the capability in Core. Finance charges remain available as a "threat" for delinquent customers but are rarely (if ever) applied. Customer deposits are collected and tracked outside the invoice system.

#### Orion/NetSuite Solution

Orion/NetSuite includes finance charge capabilities configured but disabled by default. If KB+Hoag policy changes in the future (e.g., adopt firm late payment penalties), finance charges can be activated with a simple configuration change. This approach maintains the deterrent capability without implementing active charges.

Pro forma invoices in NetSuite create a non-revenue-recognizing transaction linked to a customer liability account. When a customer makes a deposit, a pro forma invoice is generated with the deposit amount coding to the liability account. The liability is reduced and revenue recognized when the final invoice is generated and the deposit is applied. This standardizes the deposit process, creates an audit trail, and ensures deposit accounting is correct and traceable.

#### Future State Process

Finance charges remain configured but off by default. If leadership decides to implement late payment charges, a configuration change activates them—no development required.

For deposits: When a customer provides a deposit, a pro forma invoice is generated for the deposit amount, coding to the AR liability account. When the final invoice is generated, the deposit pro forma is automatically applied, reducing the invoice amount and eliminating the deposit liability.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-031 | Finance charge deterrent | Native finance charge module (disabled) | ALIGNS |
| REQ-032 | Pro forma for deposit management | Standard pro forma invoice capability | ALIGNS |

---

### 13. Vendor Management (Efficiency & Control)

#### Your Business Requirements

**REQ-033:** Configure vendors that are also customers (Intermarket dealers) (ALIGNS)
- Current: Some dealers are both vendors (supply products) and customers (buy products)
- High Volume: Hundreds of intermarket dealer relationships
- Evidence: "Dealers must be set up as both vendor AND customer... Pain point for first-time dealer setup... High volume (Shannon: hundreds of outbound transactions)" - Discussion
- Implementation Note: Coordination with Shannon's team (Product Coordinator Manager) for setup

**REQ-034:** Implement vendor credit limit tracking with warning alerts (ACCOMMODATE)
- Current: Credit limits tracked informally; organization hits limits unexpectedly
- Problem: "Track KBM credit limits with vendors... Hit limits unexpectedly: Mad scramble at that nth hour... Need warnings/alerts" - Discussion
- Outstanding Item: **CUSTOM DEVELOPMENT REQUIRED** - Warning threshold, alert mechanism, and credit utilization logic need SESSION 8 definition

#### Current State Process

KB+Hoag has hundreds of dealer relationships where a dealer is both a vendor (supplies products) and a customer (purchases products). Manual vendor setup is time-consuming and error-prone for first-time dealer configuration. Vendor credit limits are tracked informally, and the organization frequently discovers it has exceeded a vendor's credit limit when attempting a purchase—creating operational delays and vendor relationship issues.

#### Orion/NetSuite Solution

Orion/NetSuite supports vendor-customer dual relationships through standard vendor and customer records linked to the same business entity. NetSuite handles the dual relationships cleanly—vendor transactions flow through AP, customer transactions flow through AR, with no confusion. This is a standard configuration used by many industries with complex supplier-customer dynamics.

For vendor credit limit tracking, Orion/NetSuite supports custom alert configuration. The solution will track KB+Hoag's credit limits with each vendor, monitor open purchase orders and unpaid bills against those limits, and alert relevant staff when usage reaches a defined threshold (e.g., 90% of limit). Alert mechanisms can include email notifications, dashboard widgets, or hard purchase order blocks—depending on business preference.

Custom development will define the alert logic, threshold configuration, and recipient lists. This is a valuable operational control that prevents the "mad scramble at the nth hour" when credit limits are unexpectedly exceeded.

#### Future State Process

When setting up a new intermarket dealer relationship, a single entity record is created in NetSuite with both vendor and customer modules enabled. The dual relationship is configured once and works across all transactions. No more pain-point first-time setup for hundreds of dealers.

Vendor credit limits are established in the vendor record. NetSuite automatically monitors utilization (open POs + unpaid bills) against the limit. When usage reaches 90%, a warning is sent to relevant staff (e.g., purchasing manager, Lorraine). Staff can view current utilization on a dashboard and take action to manage the limit (pay down, request limit increase, or adjust purchasing plans). No more unexpected limit discoveries.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-033 | Dual vendor-customer setup (dealers) | Standard vendor/customer dual relationship | ALIGNS |
| REQ-034 | Vendor credit limit tracking & alerts | Custom alert system with threshold monitoring | ACCOMMODATE |

#### Implementation Considerations

- **SESSION 8 Required:** Vendor credit limit tracking requirements and alert design
- **Warning Threshold:** Define at what % of limit alerts trigger (recommend 90%)
- **Alert Mechanism:** Define if email, dashboard widget, or hard PO block
- **Custom Development:** Alert logic and threshold configuration may require custom script
- **Credit Utilization Calculation:** Define if includes open POs, unpaid bills, or both
- **Testing:** Validate alert accuracy using test vendor records
- **Documentation:** Document warning process and escalation if limits exceeded

---

### 14. Revenue & Cost Recognition (Compliance-Critical)

#### Your Business Requirements

**REQ-035:** Define revenue recognition rules and timing (at Sales Order or Invoice) (ACCOMMODATE)
- Complex Decision: When does revenue recognize? Sales order creation or invoice generation?
- Special Scenarios: Mockup orders, direct bill, government orders, E-commerce require specific rules
- Evidence: "Decision point: When does revenue recognize?... Typically at sales order or invoice... May need special rules for certain order types... White paper mentioned" - Discovery discussion
- Outstanding Item: **HIGH COMPLEXITY - SESSION 1 REQUIRED** - White paper review, special scenario documentation, auditor consultation recommended

**REQ-036:** Maintain project-level revenue/cost tracking with linked transactions (ALIGNS)
- Current: Project-based accounting with transactions linked to projects
- Approach: All transactions link to projects; project-level revenue/cost aggregation; KPI dashboard at project level
- Evidence: "All transactions linked to project... Project-level revenue/cost aggregation... KPI dashboard at project level" - Discussion
- Related: Dependent on REQ-035 (revenue recognition timing) for proper implementation

#### Current State Process

KB+Hoag currently operates with project-based accounting but revenue recognition rules are informal and may vary by order type. Special scenarios (mockup orders, direct bill) have handling guidelines but not formally documented. Cost tracking at project level is available but revenue recognition is not formalized, creating potential compliance and financial reporting issues.

#### Orion/NetSuite Solution

Orion/NetSuite provides sophisticated revenue recognition capabilities through the Project Record module and Cost Recognition customization. The solution supports:

**Revenue Recognition Rules:** NetSuite can be configured to recognize revenue at either sales order creation or invoice generation, depending on KB+Hoag's business practices and ASC 606 requirements. Rules can be specified by order type, customer segment, or other criteria. Special scenarios (mockup orders not generating revenue, direct bill orders with special terms, government contract orders with progress billing requirements, E-commerce orders with fulfillment triggers) can be handled with specific revenue recognition rules.

**Project-Level Tracking:** All transactions (sales orders, invoices, costs, time entries) link to projects. The Project Record module aggregates revenue, costs, gross profit, and other metrics at the project level in real-time. This creates single source of truth for project financial performance.

**Revenue-Cost Matching:** Cost Recognition ensures costs recognized match revenue timing. If revenue is recognized at sales order, costs recognized at that point. If revenue recognized at invoice, costs recognized then. This ensures proper WIP (Work in Progress) accounting and financial statement accuracy.

The solution integrates with the KPI dashboard (REQ-038) to provide real-time project profitability visibility to appropriate stakeholders.

#### Future State Process

Once revenue recognition rules are documented and approved (SESSION 1 outcome), NetSuite is configured with those rules. For each transaction:

1. Sales order is created and order type identified
2. Revenue recognition rule applied to order type
3. Revenue recognized according to rule (or held in WIP if rules specify)
4. Costs incurred, tracked at project level
5. Revenue and costs continuously matched
6. Project Record aggregates real-time project profitability
7. KPI dashboards reflect current project financial status

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-035 | Revenue recognition rules by order type | Custom revenue recognition configuration | ACCOMMODATE |
| REQ-036 | Project-level revenue/cost tracking | Project Record module and project tracking | ALIGNS |

#### Implementation Considerations

- **SESSION 1 REQUIRED:** Revenue recognition rules deep dive (CRITICAL)
- **White Paper Review:** Marcus mentioned Orion whitepaper on revenue recognition; must be reviewed and validated
- **ASC 606 Compliance:** Confirm recognition rules meet ASC 606 standards; auditor consultation recommended
- **Special Scenarios:** Document handling for mockup orders, direct bill, government contracts, E-commerce
- **Unbilled Revenue:** Clarify if unbilled revenue/deferred revenue tracking needed
- **Testing:** Validate recognition rules using historical orders and comparing to manual calculations
- **Auditor Involvement:** Consider inviting external auditor to SESSION 1 for compliance review

---

### 15. Financial Reporting (Real-Time Visibility)

#### Your Business Requirements

**REQ-037:** Create real-time financial dashboards to replace manual Excel reports (ALIGNS)
- Current: Manual Excel-based financial reporting; period-over-period requires consolidation
- Approach: Real-time dashboards, period-over-period analysis, automated report generation
- Evidence: "Real-time reporting... Period-over-period analysis... Custom dashboards... Automated report generation" - Discussion

**REQ-038:** Configure project-level KPI dashboards (real-time GP, revenue/cost tracking, commission reporting) (ACCOMMODATE)
- Project-Level Metrics: Real-time gross profit, revenue/cost tracking, commission reporting at project level
- Dual GP Tracking: If 15% markup continues, dashboard shows both Project GP and Commissionable GP
- Role-Based Visibility: Sales see Commissionable GP; Management sees true Project GP
- Evidence: "KPI dashboards... Real-time GP visibility... Revenue/cost tracking... Commission reporting" - Discussion
- Outstanding Item: SESSION 3 required for detailed dashboard requirements

#### Current State Process

KB+Hoag currently generates financial reports manually in Excel. Period-over-period analysis requires consolidating data from multiple periods and manual calculation. Project profitability visibility is limited. Commission reporting is manual. Real-time reporting is not available—reports reflect data as of last consolidation.

#### Orion/NetSuite Solution

Orion/NetSuite provides native financial dashboarding through configurable widgets and reports. Real-time dashboards display key financial metrics (revenue, costs, GP, cash flow, etc.) with automatic updates. Users can create custom dashboards showing metrics relevant to their role: finance leadership sees overall company performance, project managers see project-level metrics, sales see commission tracking, etc.

Period-over-period analysis is built into reports—users select periods to compare and the system automatically generates comparative analysis. Manual Excel consolidation is eliminated. Standard financial reports (P&L, balance sheet, cash flow, GL) are available on demand.

Project-level KPI dashboards leverage the Project Record module to display real-time project metrics: revenue to date, costs to date, gross profit (true and/or commissionable), GP margin, project status, schedule vs. actual. Dashboards can be configured with dual GP metrics if the 15% markup continues (REQ-023 decision determines this).

Role-based visibility ensures sales teams see commissionable GP (commission basis) while management sees true project GP (actual profitability). This supports the dual KPI requirement (REQ-024, REQ-025) and ensures each stakeholder sees the metrics relevant to their role.

Commission reporting integrates with the Commission Module, displaying real-time commission accruals by sales rep. Commissions can be viewed by project, customer, time period, or other dimensions, supporting commission verification and sales team incentive communication.

#### Future State Process

Financial leadership accesses a dashboard showing consolidated company financial performance: revenue MTD/YTD, costs, gross profit, cash position, key ratios. Reports are always current—no manual consolidation.

Project managers view project dashboards showing current-project KPIs: revenue to date vs. estimate, costs to date vs. budget, projected final GP, project schedule status. Real-time visibility supports proactive project management.

Sales teams view commission dashboards showing current commission accruals, commission by project, commission by customer. Transparency supports commission verification and compensation clarity.

During period close, P&L, balance sheet, and cash flow reports are generated automatically with period-over-period comparison. No manual Excel work required.

#### Solution Validation

| REQ-ID | Requirement | Orion/NetSuite Capability | Approach |
|--------|-------------|---------------------------|----------|
| REQ-037 | Real-time financial dashboards | Native NetSuite dashboards and reporting | ALIGNS |
| REQ-038 | Project-level KPI dashboards (dual GP) | Custom dashboards with Project Record metrics | ACCOMMODATE |

#### Implementation Considerations

- **SESSION 3 Required:** Detailed KPI dashboard requirements (dependent on REQ-023 decision)
- **Dashboard Design:** Define specific metrics, layout, and drill-down capabilities for each user role
- **Period-Over-Period Setup:** Configure standard period comparison logic in reports
- **Commission Reporting:** Define commission dashboard metrics (by rep, project, customer, time period)
- **Role-Based Access:** Define which user roles see which dashboards
- **Testing:** Validate dashboard calculations using known financial data
- **User Training:** Train users on dashboard navigation, filtering, and exporting capabilities

---

## Implementation Approach Summary

### ALIGNS (68% of requirements - Standard Functionality)

The following requirements align with standard Orion/NetSuite capabilities and require no customization:

**Subsidiary & Currency:** REQ-001, REQ-003
**Tax Management:** REQ-004, REQ-005, REQ-006, REQ-007
**Banking & Cash Management:** REQ-008, REQ-009, REQ-011, REQ-012
**Expense Management (Platforms):** REQ-013, REQ-014
**Data Migration:** REQ-017
**Journal Entries:** REQ-018
**Period Close:** REQ-020, REQ-021
**Fixed Assets:** REQ-026 (if adopted)
**Payroll Integration:** REQ-027
**Payment Processing:** REQ-029
**Customer Financial:** REQ-031, REQ-032
**Vendor Setup:** REQ-033
**Project Tracking:** REQ-036
**Financial Reporting:** REQ-037

These 26 requirements represent proven, standard NetSuite functionality used by similar businesses. Implementation follows established NetSuite best practices with no custom development required.

### ADAPT (24% of requirements - Process Changes)

The following requirements require business process modification to use standard NetSuite functionality:

**Accounting Periods:** REQ-002 (13-period calendar - non-standard configuration)
**Bill Payment Approval:** REQ-010 (workflow process change)
**Expense Coding:** REQ-015 (workflow integration between Expensify/RAMP and NetSuite)
**Period Management:** REQ-022 (bulk year-opening vs. one-period-at-a-time)
**Labor Markup:** REQ-023 (decision required on continuation)
**Fixed Assets:** REQ-026 (evaluation required; may require migration from Bloomberg)
**Payroll Provider:** REQ-028 (evaluation of new provider; CSV approach works with any provider)
**Wire Transfers:** REQ-030 (if supported by bank; otherwise manual workaround)

These 9 requirements require KB+Hoag to modify how they execute certain processes to align with NetSuite's standard approach. No customization required—just business process adjustment.

### ACCOMMODATE (8% of requirements - Custom Configuration/Development)

The following requirements require custom configuration, solution design, or minor customization:

**Chart of Accounts:** REQ-016 (design effort for 40+ page to few-hundred consolidation)
**Project GP Tracking:** REQ-024 (dual GP metric reporting and calculation)
**Role-Based GP Visibility:** REQ-025 (permission configuration for different GP views)
**Vendor Credit Limits:** REQ-034 (custom alert system with threshold monitoring)
**Revenue Recognition:** REQ-035 (custom rules by order type; compliance-critical design)
**Project KPI Dashboards:** REQ-038 (custom dashboard design with dual GP metrics)

These 6 requirements represent higher-complexity items requiring custom configuration or solution design. Most involve reporting/dashboard customization (ACCOMMODATE) rather than complex custom development. The revenue recognition requirement (REQ-035) is the highest complexity due to compliance implications.

### Conditional Requirements (Pending Decisions)

**REQ-019:** Automated Allocations - Implementation optional pending Matt/Mark leadership approval
**REQ-023:** 15% Labor Markup - Decision required on continuation vs. elimination
**REQ-026:** Fixed Assets - Decision required on NetSuite FA module vs. Bloomberg
**REQ-013/014:** Expense Platform - Decision required on Expensify vs. RAMP

---

## Critical Path & Dependencies

### Phase 1: Foundation Setup (Before Detailed Design)

1. **SESSION 2 - Chart of Accounts Design (REQ-016)** [URGENT]
   - Conduct detailed export and analysis of current 40+ page COA
   - Design few-hundred-account structure with dimension strategy
   - Create mapping document from old to new COA
   - Timeline: ASAP - affects all subsequent data planning
   - Owner: Lorraine, Celine, Kevin
   - Duration: 2-3 hours

2. **SESSION 1 - Revenue Recognition Rules (REQ-035, REQ-036)** [HIGH PRIORITY]
   - Review Orion whitepaper on revenue recognition
   - Define revenue recognition timing by order type
   - Document special scenarios (mockup, direct bill, government, E-commerce)
   - Confirm ASC 606 compliance
   - Timeline: Before detailed design phase
   - Owner: Lorraine, Marcus, possibly auditor
   - Duration: 1-2 hours

### Phase 2: High-Impact Decisions (Before Configuration)

3. **SESSION 3 - Commission & GP Calculation (REQ-023, REQ-024, REQ-025, REQ-038)** [HIGH PRIORITY]
   - **DECISION: Continue 15% labor markup or eliminate?** (Matt/Mark)
   - Define commission calculation rules
   - Design dual GP dashboard (if markup continues)
   - Define role-based visibility
   - Timeline: Before configuration
   - Owner: Lorraine, Kipp, Matt/Mark, Sales Leadership
   - Duration: 1-2 hours

4. **SESSION 6 - Expense Platform (REQ-013, REQ-014, REQ-015)** [HIGH PRIORITY - DECISION]
   - **DECISION: Expensify Suite App OR RAMP?**
   - Demo both platforms
   - Define project coding requirements
   - Timeline: Before configuration
   - Owner: Lorraine, AP Team
   - Duration: 1.5-2 hours

### Phase 3: Operational Process Design (Before Detailed Design)

5. **SESSION 4 - Period Close Optimization (REQ-020, REQ-021, REQ-022)** [HIGH PRIORITY]
   - Document detailed 10-day close process
   - Identify bottlenecks and optimization opportunities
   - Design NetSuite Period Close Checklist
   - Set realistic timeline reduction goals (5-7 days)
   - Timeline: Before detailed design
   - Owner: Lorraine, Celine, Kevin, AP Team
   - Duration: 1-2 hours

6. **SESSION 5 - Bill Payment Workflow (REQ-008, REQ-009, REQ-010, REQ-030)** [HIGH PRIORITY]
   - Confirm bill payment approval workflow mechanics
   - Define remittance process (automatic vs. manual)
   - Determine wire transfer handling in Advanced Electronic Bill Payments
   - Timeline: Before detailed design
   - Owner: Lorraine, Guada, Michael, Marcus
   - Duration: 1 hour

### Phase 4: Detailed Configuration Requirements (Before Go-Live)

7. **SESSION 7 - Fixed Asset Module (REQ-026)** [MEDIUM PRIORITY - DECISION]
   - **DECISION: NetSuite FA module OR continue Bloomberg?**
   - Compare Bloomberg features and costs
   - Evaluate NetSuite FA capabilities
   - Timeline: Before implementation
   - Owner: Lorraine, Marcus
   - Duration: 45 min - 1 hour

8. **SESSION 8 - Vendor Credit Limits (REQ-034)** [MEDIUM PRIORITY]
   - Define warning threshold (recommend 90%)
   - Determine alert mechanism
   - Document custom development requirements
   - Timeline: Before go-live
   - Owner: Lorraine, Purchasing Team
   - Duration: 30-45 min

---

## Solution Design Details

### ACCOMMODATE Items Requiring Custom Solution Design

#### 1. Chart of Accounts Consolidation (REQ-016)

**Design Challenge:** Current 40+ page structure must consolidate to few hundred accounts while maintaining reporting capability.

**Solution Design Approach:**
- Strategic use of NetSuite dimensions (Classes, Departments, Projects) to reduce account proliferation
- Account grouping by business logic: Revenue streams, COGS by type, Operating expenses by function, Balance sheet
- New account numbering scheme (e.g., 1xxx = Revenue, 4xxx = COGS, 5xxx = Operating, etc.)
- Mapping document ensuring no revenue/cost items are lost in consolidation
- Historical data reclassification to new structure

**Pre-Implementation Work:**
- Export complete current Core COA
- Identify most-used accounts (80/20 analysis)
- List any duplicates or rarely-used accounts
- Propose new structure with dimension strategy
- Create detailed mapping from old to new

**Testing & Validation:**
- Sample transaction testing in new structure
- Report validation comparing old and new structures
- Historical reporting validation (prior-year comparisons work correctly)

#### 2. Dual GP Metrics (REQ-024, REQ-025)

**Design Challenge:** Track both true project GP and commissionable GP (including 15% markup if continued). Display appropriately by role.

**Solution Design Approach:**
- Custom calculation logic in Project Record for both metrics
- Role-based visibility using NetSuite permission roles
- Dashboard design showing appropriate metric by role
- Commission calculation based on commissionable GP

**Implementation:**
- If 15% markup continues: Custom script or formula calculating both metrics
- If 15% eliminated: Single true GP metric visible to all
- Sales dashboards display commissionable GP
- Management dashboards display true project GP

**Testing:**
- Validate both metrics calculate correctly using historical project data
- Confirm role-based visibility works as designed
- User acceptance testing with sales team and management

#### 3. Vendor Credit Limit Alerts (REQ-034)

**Design Challenge:** Monitor credit utilization against limits and alert when threshold reached.

**Solution Design Approach:**
- Credit limit field in vendor record
- Automated monitoring of open POs + unpaid bills vs. limit
- Threshold definition (recommend 90% utilization)
- Alert mechanism: Email, dashboard widget, or hard PO block
- Custom script or workflow rule calculating utilization

**Configuration:**
- Vendor credit limit field setup
- Alert recipients and escalation rules
- Threshold percentage configuration
- Alert trigger logic

**Testing:**
- Create test vendors with credit limits
- Place orders to trigger 75%, 90%, and 100% utilization
- Validate alerts trigger at correct thresholds
- Confirm alert recipients receive notifications

#### 4. Revenue Recognition Rules (REQ-035)

**Design Challenge:** Support complex revenue recognition by order type; ensure ASC 606 compliance.

**Solution Design Approach:**
- Revenue recognition rules by order type: Standard, Mockup, Direct Bill, Government, E-commerce
- Rule parameters: Revenue recognized at Sales Order or Invoice; special handling for payment collection if required
- Integration with Cost Recognition ensuring costs match revenue timing
- WIP accounting for deferred revenue scenarios
- Unbilled/deferred revenue tracking if needed

**Documentation:**
- White paper review and validation
- Revenue recognition rules by order type with examples
- Special scenario handling procedures
- ASC 606 compliance documentation

**Testing:**
- Sample orders for each type with revenue recognition validation
- Deferred revenue testing (if applicable)
- Cost vs. revenue matching verification
- Auditor review of recognition logic

#### 5. Project-Level KPI Dashboards (REQ-038)

**Design Challenge:** Real-time project profitability dashboards with role-based GP visibility.

**Solution Design Approach:**
- Project Record module aggregating revenue, costs, GP metrics
- Dual GP metrics if 15% markup continues (dependent on REQ-023)
- Custom dashboard design with project-level KPIs
- Commission tracking dashboard
- Role-based dashboard visibility

**Metrics Displayed:**
- Revenue to date vs. estimate
- Costs to date vs. budget
- Gross profit (true and/or commissionable)
- GP margin percentage
- Project status and schedule
- Commission accruals by rep

**Implementation:**
- Dashboard template design
- KPI definition and calculation rules
- Role-based access configuration
- Data refresh frequency (real-time or periodic)

**Testing:**
- Validate dashboard calculations using known project data
- Performance testing with large datasets
- User acceptance testing by intended dashboard users

---

## Outstanding Items & Pre-Implementation Decisions

### Critical Decisions Pending (HIGH IMPACT)

| Decision | REQ-ID | Decision Maker | Timeline | Impact |
|----------|--------|----------------|----------|--------|
| 15% Labor Markup Continuation | REQ-023 | Matt/Mark (Leadership) | **BEFORE CONFIGURATION** | **HIGH** - Affects sales compensation, custom dev scope, commission calculations |
| Expense Platform Selection | REQ-013/014 | Lorraine | BEFORE CONFIGURATION | Medium - User adoption, platform costs |
| Fixed Asset Module Decision | REQ-026 | Lorraine/Marcus | BEFORE IMPLEMENTATION | Medium - Cost, third-party dependency |
| Automated Allocations | REQ-019 | Matt/Mark | BEFORE CONFIGURATION | Medium - Optional; P&L reporting impact |

### Foundational Pre-Work (Before Detailed Design)

| Item | REQ-ID | Owner | Timeline |
|------|--------|-------|----------|
| Current COA Export & Analysis | REQ-016 | Lorraine/Celine/Kevin | **URGENT** - ASAP |
| Chart of Accounts Design | REQ-016 | Lorraine/Celine/Kevin | Before data migration |
| Revenue Recognition White Paper Review | REQ-035 | Lorraine/Marcus | Before detailed design |
| Revenue Recognition Rules Documentation | REQ-035 | Lorraine/Marcus | before detailed design |
| Period Close Process Documentation | REQ-020/021/022 | Lorraine/Celine/Kevin | Before detailed design |

---

## Implementation Timeline & Next Steps

### Immediate Actions (This Week)

1. **Schedule SESSION 2 - Chart of Accounts Design**
   - Participants: Lorraine, Celine, Kevin, Implementation Consultant
   - Pre-Work: Export current Core COA with transaction frequency by account
   - Duration: 2-3 hours
   - Output: Proposed new COA structure, mapping document, account numbering scheme

2. **Schedule SESSION 1 - Revenue Recognition**
   - Participants: Lorraine, Kipp, Marcus, possibly auditor
   - Pre-Work: Review Orion whitepaper on revenue recognition
   - Duration: 1-2 hours
   - Output: Documented revenue recognition rules by order type, white paper validation

### Week 2-3 Actions

3. **Obtain Leadership Decisions**
   - Schedule with Matt/Mark to finalize REQ-023 (15% markup) and REQ-019 (automated allocations)
   - Timeline: 15 minutes decision-level conversation

4. **Schedule SESSION 3 - Commission & GP Calculation**
   - Participants: Lorraine, Kipp, Matt/Mark, Sales Leadership
   - Timing: Immediately after leadership decisions on REQ-023
   - Duration: 1-2 hours
   - Output: Commission calculation rules, GP dashboard requirements, role-based visibility matrix

5. **Schedule SESSION 4 - Period Close Optimization**
   - Participants: Lorraine, Celine, Kevin, AP Team
   - Duration: 1-2 hours
   - Output: Detailed close procedure, checklist steps, timeline reduction plan

### Week 4 Actions

6. **Schedule SESSION 5 - Bill Payment Workflow**
   - Participants: Lorraine, Guada, Michael, Marcus
   - Duration: 1 hour
   - Output: Detailed payment workflow, remittance procedure, wire handling

7. **Schedule SESSION 6 - Expense Platform Decision**
   - Participants: Lorraine, AP Team, sample submitters
   - Duration: 1.5-2 hours
   - Pre-Work: Demo both Expensify and RAMP platforms
   - Output: Platform selection, project coding requirements, integration specs

### Before Configuration Phase

8. **Schedule SESSION 7 - Fixed Asset Module Evaluation**
   - Participants: Lorraine, Marcus
   - Duration: 45 min - 1 hour
   - Output: Fixed asset module decision, cost-benefit analysis, migration plan (if needed)

9. **Complete All Pre-Implementation Documentation**
   - Chart of Accounts mapping (from SESSION 2)
   - Revenue Recognition rules (from SESSION 1)
   - Commission calculation rules (from SESSION 3)
   - Period Close procedures (from SESSION 4)
   - Bill Payment workflow (from SESSION 5)
   - Expense platform integration specs (from SESSION 6)

### Before Go-Live

10. **Schedule SESSION 8 - Vendor Credit Limit Configuration**
    - Participants: Lorraine, Purchasing Team
    - Duration: 30-45 min
    - Output: Credit limit alert configuration

11. **Comprehensive Testing**
    - User acceptance testing on all configured processes
    - Historical data validation
    - Report accuracy verification
    - Performance testing
    - Security and permission testing

---

## Implementation Considerations & Change Management

### Key Success Factors

1. **Lorraine's Prior ERP Experience**
   - Used Blackline/Flowcast in previous roles
   - Understands modern accounting software capabilities
   - Will champion period close optimization and real-time reporting
   - Can validate new processes as improvements

2. **Lean Finance Team Benefits**
   - Small team size means automation gains are highly visible
   - Bank feeds, electronic payments, and expense sync will generate quick wins
   - Reversal JE automation solves known prior pain point (abandoned in Core)
   - Real-time dashboards will be appreciated by management

3. **Clear Pain Point Awareness**
   - Team knows current limitations (40+ page COA, 10-day close, manual processes)
   - Already motivated for improvement
   - Realistic expectations about implementation complexity
   - Strong stakeholder engagement

### Potential Resistance Points

1. **Chart of Accounts Restructuring**
   - Long-standing account numbers may be memorized by users
   - Training critical for new structure adoption
   - Mapping reference guide essential during transition
   - Recommend parallel running of COA for first few periods

2. **15% Labor Markup Decision (If Eliminated)**
   - Major philosophy change affecting sales compensation
   - Sales team communication plan required
   - Commission impact analysis needed
   - Change champion needed from sales leadership

3. **Period Close Process Change (Excel to NetSuite)**
   - Lorraine and team are comfortable with Excel
   - New NetSuite checklist requires trust in system-guided process
   - Training focus needed on new workflow
   - Quick wins on timeline reduction will help adoption (if achievable)

4. **Expense Platform Change (If Switching to RAMP)**
   - Users familiar with Expensify
   - RAMP requires new learning curve
   - Mobile UX improvements could help adoption
   - Early user involvement in demo/selection recommended

### Recommended Change Management Approach

1. **Early Stakeholder Engagement**
   - Include all 8 follow-up sessions before configuration
   - Get final decisions on pending items early
   - Build team ownership of new processes
   - Involve change champions (Lorraine for close, Kipp for integration, Celine/Kevin for GL)

2. **Quick Wins Strategy**
   - Prioritize easy integrations (bank feeds, electronic payments) for early value
   - Automated reversal JE implementation will address known pain point
   - Real-time dashboards for quick reporting improvements
   - Generate momentum for larger changes

3. **Comprehensive Training & Documentation**
   - Detailed mapping documents for COA transition
   - Process documentation for new period close workflow
   - User guides for new dashboard access and reporting
   - FAQ addressing common questions/concerns
   - Video tutorials for complex processes

4. **Parallel Running (First Few Cycles)**
   - Run Excel close in parallel with NetSuite for first 2-3 periods
   - Compare results to build confidence in system
   - Identify process adjustments needed
   - Transition to NetSuite-only when team is confident

5. **Communication Plan**
   - Kick-off meeting with all finance staff
   - Regular update meetings during implementation
   - FAQs addressing concerns
   - Recognition of team contributions to successful implementation
   - Celebrate quick wins and early success

---

## Quality Assurance & Validation

### Pre-Implementation Validation

- [ ] All 38 requirements verified from discovery findings
- [ ] Business requirements aligned with Orion/NetSuite capabilities
- [ ] Implementation approach (ALIGNS/ADAPT/ACCOMMODATE) justified for each requirement
- [ ] Outstanding items captured with clear owners and timelines
- [ ] Decision gates identified with decision makers and deadlines
- [ ] Critical path dependencies documented
- [ ] Pre-work items assigned to appropriate owners
- [ ] Follow-up session schedule established

### During Configuration

- [ ] Chart of accounts mapping validated (every old account maps to new structure)
- [ ] Revenue recognition rules tested with sample orders by type
- [ ] Commission calculations validated against historical data
- [ ] Period close checklist steps mirror documented procedures
- [ ] Bank feed integration tested with actual West Coast Community Bank account
- [ ] Bill payment approval workflow tested with sample payments
- [ ] Dashboard calculations verified against manual calculations
- [ ] Role-based visibility confirmed for GP metrics
- [ ] Data migration testing (historical data integrity)

### User Acceptance Testing

- [ ] Finance team completes UAT procedures
- [ ] All 8 follow-up sessions completed before UAT
- [ ] Outstanding items resolved before UAT
- [ ] Sample transactions tested end-to-end
- [ ] Reports validated for accuracy
- [ ] Dashboards tested by intended user roles
- [ ] Performance acceptable during peak usage
- [ ] Security and permission controls validated

### Post-Implementation

- [ ] Parallel run comparison for first period close
- [ ] Production data validation
- [ ] Process monitoring for first 90 days
- [ ] User support and FAQ updates
- [ ] Optimization opportunities identified

---

## Appendix: Requirements Map Summary

### All 38 Requirements at a Glance

**Company Structure & Setup (3):** REQ-001, REQ-002, REQ-003
**Tax Management (4):** REQ-004, REQ-005, REQ-006, REQ-007
**Banking & Cash Management (5):** REQ-008, REQ-009, REQ-010, REQ-011, REQ-012
**Expense Management (3):** REQ-013, REQ-014, REQ-015
**Chart of Accounts & Data (2):** REQ-016, REQ-017
**Journal Entries & Allocations (2):** REQ-018, REQ-019
**Period Close (3):** REQ-020, REQ-021, REQ-022
**Labor Markup & Costing (3):** REQ-023, REQ-024, REQ-025
**Fixed Assets (1):** REQ-026
**Payroll Integration (2):** REQ-027, REQ-028
**Payment Processing (2):** REQ-029, REQ-030
**Customer Financial Management (2):** REQ-031, REQ-032
**Vendor Management (2):** REQ-033, REQ-034
**Revenue & Cost Recognition (2):** REQ-035, REQ-036
**Financial Reporting (2):** REQ-037, REQ-038

**Approach Summary:**
- ALIGNS: 26 requirements (68%)
- ADAPT: 9 requirements (24%)
- ACCOMMODATE: 3 requirements + 6 conditional (24%)

---

## Executive Sign-Off

This Business Requirements Document has been prepared based on comprehensive discovery sessions, questionnaires, and requirements mapping for KB+Hoag's Financial Management implementation on Orion/NetSuite.

The document validates that the proven Orion/NetSuite Financial Management solution aligns with KB+Hoag's business requirements, with 68% of requirements aligned to standard functionality, 24% requiring process adaptation, and 8% requiring custom configuration or solution design.

**Recommended Next Steps:**
1. Review and approve BRD
2. Schedule the 8 follow-up discovery sessions per implementation timeline
3. Complete critical pre-work items (Chart of Accounts export, revenue recognition white paper review)
4. Finalize leadership decisions on REQ-023, REQ-019, and REQ-026
5. Proceed to detailed configuration phase upon completion of follow-up sessions

---

**Prepared by:** Implementation Consultant
**Date:** November 13, 2025
**Document Status:** Ready for Stakeholder Review and Approval
**Next Review:** Upon completion of 8 follow-up discovery sessions

---

*End of Business Requirements Document - Financial Management v1.0*


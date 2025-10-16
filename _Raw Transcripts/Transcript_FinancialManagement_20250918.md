# KBMH Discovery Transcript - Financial Management

**Original File:** GMT20250918-211018_Recording.transcript.vtt  
**Date:** September 18, 2025  
**Duration:** ~2+ hours  
**Process Area:** Financial Management

---

## Session Overview

Comprehensive discovery session covering all aspects of financial management including AP, AR, GL, project accounting, revenue recognition, expense management, and financial reporting.

## Finance Team Structure

### Team Members & Locations
- **Lorraine** - Finance Leader/Controller
- **Guada** - Accounts Payable
- **Celine** - General Ledger
- **Kevin** - General Ledger
- **Michael** - Accounts Payable (Philippines location)
- **[Name]** - Accounts Receivable (San Jose office)
- **Kip** - Former controller, now IT but still involved in finance operations

**Team Description:** "Lean but mighty" finance team spread across multiple locations

---

## Key Topics Covered

### 1. Company Structure & Setup
- **Single Subsidiary** - One legal entity
- **Multiple Locations** - Offices in different cities
- **Calendar Year** - Fiscal year aligns with calendar year
- **13 Accounting Periods** - Preferred (Core currently limited to 12)

### 2. Accounting Periods & Close
- **Current:** 12 periods in Core (limitation)
- **Desired:** 13 periods in NetSuite
- **Fiscal Year:** Calendar year (January - December)
- **Period Close Process:** Discussed need for efficient month-end close

### 3. Currency & Exchange Rates
- **US Dollar only** - No foreign currency transactions
- **No multi-currency needs** - Simplifies implementation

### 4. Tax Management

#### Sales Tax
- **Sweet Tax** (formerly SuiteTax) implementation confirmed
- **Most states:** Standard sales tax
- **Exceptions:** Illinois and Missouri

#### Use Tax
- **Illinois and Missouri only** - Different nexus definitions
- **Current workaround:** "Tricking" Core to handle use tax
- **Current provider:** TaxConnect (third-party service)
- **Sweet Tax will handle:** Both sales and use tax scenarios

### 5. Purchase Orders & Vendor Management
- **Extensive PO discussion** in prior session (Order Management)
- **Vendor acknowledgments** process
- **Product coordinators** (Shannon's team) work with vendors
- **Vendor invoice processing** through AP team
- **Three-way match:** PO → Receipt → Invoice

### 6. Journal Entries & Allocations
- **Standard journal entries** for adjustments
- **Allocation needs** to be determined
- **Period-end close entries**

### 7. Banking & Cash Management
- **West Coast Community Bank** - Mentioned for bank feeds
- **Bank feed integration** confirmed
- **Cash management processes** discussed

### 8. Credit Card Management
- **Corporate card programs** in use
- **Employee expense cards**
- **Reconciliation process** needs improvement

### 9. Budgeting & Planning
- **Budget creation** requirements
- **Variance analysis** needs
- **Forecasting capabilities** desired

### 10. Project Accounting (CRITICAL TOPIC)

#### Labor Margin Contingency - 15% Load Factor
**Current Core Process:**
- Automatic addition of 15% to all labor costs
- Example: $100 labor line → automatically adds $15 contingency line
- **Product code trigger:** "Labor" product code triggers the rule
- **Purpose:** Encourage higher margins on unpredictable labor costs
- **Impact:** Reduces apparent margin but doesn't hit GL
- **Commission impact:** Affects GP calculation for commissions

**Philosophy:**
- Product costs are predictable (PO = cost)
- Labor is unpredictable until field work begins
- 15% contingency provides risk buffer
- Never costs against these contingency lines

**GSI Response:**
- Other dealers do similar (typically 3% of revenue vs 15% of cost)
- Can be configured as cost-only line in NetSuite
- Percentage-based calculation on cost of revenue

**Decision Point:**
- Matt and Mark need to decide if keeping this practice
- **Commission consideration:** Currently paid after this reduction

#### Project GP vs Commissionable GP
- **Two sets of KPIs** required:
  1. **Project Gross Profit** - True financial performance
  2. **Commissionable Gross Profit** - Includes load factor and other adjustments

**User Permissions:**
- Different roles see different GP figures
- Sales team sees commissionable GP
- Finance sees actual GP

### 11. Revenue & Cost Recognition (MAJOR TOPIC)

**White Paper Provided:**
- GSI has detailed white paper on revenue recognition in NetSuite
- Different from Core's approach
- **Review required:** Lorraine needs to understand differences

**Key Considerations:**
- Project-based revenue recognition
- Percentage of completion methodology
- Milestone-based recognition
- Timing differences from Core

### 12. Vendor & AP Management

#### Current Process
- **Vendor invoices** received by AP team (Guada, Michael)
- **Product coordinators** verify receipt and accuracy
- **Three-way matching** before payment
- **Payment terms** management
- **1099 vendor** tracking needed

#### AP Team Distribution
- **US-based:** Guada
- **Philippines:** Michael (bed head in morning meetings!)
- **Workload distribution** across time zones

### 13. Expense Management

#### Current State
- **Expensify** - Currently in use
- **Evaluation ongoing** - May change to different platform
- **Manual process:** 
  1. Employee submits expense report in Expensify
  2. Kip approves
  3. Kevin downloads Excel spreadsheet
  4. Kevin uploads to Core
  5. Kevin manually matches for reconciliation

#### Desired State
- **Integration with NetSuite** - Eliminate manual steps
- **Automatic reconciliation** - Expense system → NetSuite
- **Cost allocation:**
  - Project costs (COGS)
  - G&A expenses

**Two Cost Types:**
1. **Project Costs** - Cost of goods sold, tied to specific projects
2. **G&A Costs** - General & administrative overhead

### 14. Asset Management
- **Fixed asset tracking** required
- **Depreciation** calculations
- **Asset lifecycle** management

### 15. Financial Security & Permissions
- **Role-based access** to financial data
- **Separation of duties** for AP
- **Period lock** after close
- **Audit trail** requirements

### 16. Financial Reporting & Analytics

#### Standard Reports Needed
- **P&L** by period, location, department
- **Balance Sheet**
- **Cash flow statements**
- **Trial balance**
- **General ledger detail**
- **AP aging**
- **AR aging**

#### Project-Specific Reports
- **Project profitability** by project
- **Labor vs materials** analysis
- **Commissionable GP** vs actual GP
- **Budget vs actual** by project

#### Management Reports
- **KPI dashboards** for executives
- **Department performance**
- **Margin analysis**
- **Commission calculations**

---

## Requirements Identified

### Functional Requirements
1. **13 accounting periods** (vs Core's 12)
2. **Sweet Tax implementation** for sales and use tax
3. **Project accounting** with dual GP views (actual and commissionable)
4. **15% labor load factor** (if keeping this practice)
5. **Expense integration** with chosen platform (Expensify or alternative)
6. **Fixed asset management**
7. **Budget and forecasting** capabilities
8. **Multi-location reporting**
9. **Commission calculations** based on commissionable GP
10. **AP workflow** with three-way matching

### Technical Requirements
1. **Bank feed integration** (West Coast Community Bank)
2. **Sweet Tax configuration** for IL and MO use tax
3. **Expense management integration** (replacing manual Excel process)
4. **Revenue recognition** rules and automation
5. **Project cost allocation** (COGS vs G&A)
6. **Custom KPI calculations** for project and commissionable GP
7. **Role-based financial security**
8. **1099 vendor tracking and reporting**

### Data Migration Requirements
1. **Chart of Accounts** - Early priority, needed immediately
2. **Historical financials** - 2017 forward (confirmed scope)
3. **End-of-month trial balances** - CSV import for historical periods
4. **Vendor master** - Including 1099 status
5. **Customer master** - With payment terms and credit limits
6. **Open AR** - Outstanding invoices
7. **Open AP** - Outstanding bills
8. **Work in progress** - Active project costs

---

## Integration Touchpoints

### With Order Management
- PO creation and approval
- Receipt of goods/services
- Vendor invoice matching
- Project cost application

### With Project Management (Orion)
- Project budgets
- Actual costs vs budget
- Labor and materials allocation
- Project profitability

### With Payroll (Paylocity)
- **Remains separate** - Paylocity not going away
- Labor cost allocation to projects
- Employee expense reimbursements
- Benefits and overhead allocation

### With Operations
- Inventory valuation
- Cost of goods sold
- Labor burden rates
- Overhead allocation

---

## Critical Decisions Needed

1. **Keep or eliminate 15% labor load factor?** (Matt/Mark decision)
2. **Which expense management platform?** (Expensify or alternative)
3. **Historical data cutoff** - Confirm 2017 as starting point
4. **Chart of accounts structure** - Need early in Realize phase
5. **Revenue recognition methodology** - Review white paper and decide

---

## Pain Points & Improvement Goals

### Current Challenges
1. **Manual expense reconciliation** - Time-consuming, error-prone
2. **Limited reporting** in Core - Can't get basic information
3. **Two systems for project financials** - Core limitations
4. **12 vs 13 periods** - Forced workarounds
5. **Commission calculations** - Manual, complex with load factors

### Desired Improvements
1. **Automated expense processing** - Eliminate Excel downloads
2. **Real-time project profitability** - No waiting for month-end
3. **Flexible reporting** - Create own reports without IT help
4. **Single source of truth** - All financial data in one system
5. **Better cash flow visibility** - Bank feeds and dashboards

---

## Source File Location
Original VTT file: `GMT20250918-211018_Recording.transcript.vtt`

**Next Steps:**
1. Review revenue recognition white paper
2. Decide on 15% labor load factor continuation
3. Choose expense management platform
4. Finalize chart of accounts structure
5. Confirm historical data migration scope (2017 forward)
6. Define commissionable GP calculation rules
7. Map Sweet Tax configuration for IL/MO use tax


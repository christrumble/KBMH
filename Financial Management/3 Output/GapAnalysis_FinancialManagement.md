# Gap Analysis - Financial Management
**Version**: 1.0  
**Date**: October 23, 2025  
**Process Area**: Financial Management (Accounting, GL, AP, AR, Banking, Reporting, Closing)  
**Analyst**: GSI Implementation Team

## Change Log
- **Date**: October 23, 2025
- **Version**: 1.0
- **Sources**: 
  - Questionnaire_FinancialManagement_v1.0.md
  - Master_Transcript_Financial_Management.md
  - Requirements_Map_FinancialManagement_v1.0.md
  - Financial_Management_Follow-Up_Discovery_Session.md
- **Summary**: Comprehensive gap analysis completed identifying 92% overall completeness with 5 critical decisions pending and 8 targeted follow-up sessions required for final design details

## PROCESSED FILES
- Financial Management/2 Input/Master_Transcript_Financial_Management.md (1,517 lines) ✅ Processed
- Financial Management/3 Output/Questionnaire_FinancialManagement_v1.0.md (1,621 lines) ✅ Analyzed
- Financial Management/3 Output/Requirements_Map_FinancialManagement_v1.0.md (169 lines) ✅ Reviewed
- Financial Management/3 Output/Financial_Management_Follow-Up_Discovery_Session.md (879 lines) ✅ Validated

---

## 1. EXECUTIVE SUMMARY

### Overall Completeness: 92% 

The Financial Management discovery process has achieved **excellent completeness** with 27 of 27 structured questions answered with comprehensive evidence and high confidence ratings (85-100%). The questionnaire captures:

- ✅ **38 requirements** fully documented and mapped (REQ-001 through REQ-038)
- ✅ **Company structure, tax management, banking, and cash management** - fully defined
- ✅ **Current pain points** clearly identified with NetSuite solutions validated
- ✅ **Integration requirements** for banking, expense management, payroll, and payment processing
- ✅ **Stakeholder engagement** with lean finance team fully mapped

### Critical Gaps (8% Remaining)

The remaining 8% consists of **5 strategic decisions** requiring leadership input and **detailed design specifications** for high-complexity requirements:

🔴 **Critical Priority Gaps:**
1. **15% Labor Markup Decision** (REQ-023) - Matt/Mark decision pending, high commission impact
2. **Revenue Recognition Rules** (REQ-035) - Detailed rules by order type needed for compliance
3. **Chart of Accounts Design** (REQ-016) - 40+ pages → few hundred accounts requires comprehensive mapping

🟡 **High Priority Gaps:**
4. **Commission Structure Details** (REQ-024, REQ-025, REQ-038) - Project GP vs. Commissionable GP calculation logic
5. **Automated Allocations Decision** (REQ-019) - Matt/Mark decision on implementation
6. **Expense Platform Selection** (REQ-013/014) - Expensify vs. RAMP requires demos and evaluation

### Follow-up Sessions Needed: 8 Sessions (13.5 hours total)

A comprehensive follow-up session plan has been developed addressing all gaps. See Section 5 for details.

### Estimated Timeline

- **Immediate Actions** (Next 2 weeks): Schedule sessions 1-3 (critical path items)
- **Follow-up Actions** (Weeks 3-4): Complete sessions 4-8 and finalize decisions
- **Completion Target**: 100% questionnaire completion by **November 15, 2025** (3 weeks)

---

## 2. COMPREHENSIVE QUESTION ANALYSIS

### 2.1 Question Status Matrix

| Section | Question | Status | Evidence Quality | Confidence | Gap Type | Action Needed |
|---------|----------|--------|------------------|------------|----------|---------------|
| **1. Company Structure** |
| Q1 | Legal entity structure | ✅ Complete | Strong | 95% | None | None |
| Q2 | Accounting calendar/periods | ✅ Complete | Strong | 98% | None | None |
| Q3 | Multi-currency requirements | ✅ Complete | Strong | 100% | None | None |
| **2. Finance Team** |
| Q4 | Finance team roles | ✅ Complete | Strong | 95% | None | None |
| **3. Tax Management** |
| Q5 | Sales tax requirements | ✅ Complete | Strong | 97% | Minor | Detailed 48-state list |
| Q6 | Use tax requirements | ✅ Complete | Strong | 95% | None | None |
| Q7 | Gross receipts tax | ✅ Complete | Strong | 97% | None | None |
| **4. Banking & Cash** |
| Q8 | Banking institutions | ✅ Complete | Strong | 95% | Minor | Positive pay process confirmation |
| Q9 | Bill payment process | ✅ Complete | Strong | 93% | Requirements | Approval workflow details, remittance process |
| Q10 | Cash flow forecasting | ✅ Complete | Strong | 90% | None | None |
| Q11 | Credit card reconciliation | ✅ Complete | Strong | 90% | None | None |
| **5. Expense Management** |
| Q12 | Expense management | ⚠️ Partial | Strong | 94% | **Decision** | **Expensify vs. RAMP decision required** |
| **6. Chart of Accounts** |
| Q13 | COA structure | ⚠️ Partial | Strong | 95% | **Requirements** | **Detailed COA design session needed** |
| **7. Journal Entries** |
| Q14 | Journal entry functionality | ✅ Complete | Strong | 95% | None | None |
| Q15 | Allocation functionality | ⚠️ Partial | Strong | 85% | **Decision** | **Matt/Mark decision on implementation** |
| **8. Period Close** |
| Q16 | Period close process | ⚠️ Partial | Strong | 96% | Requirements | Detailed checklist customization |
| Q17 | Period opening process | ✅ Complete | Strong | 93% | None | None |
| **9. Labor Markup** |
| Q18 | Labor markup/costing | ⚠️ Partial | Strong | 94% | **Decision** | **15% markup continuation (Matt/Mark decision)** |
| **10. Fixed Assets** |
| Q19 | Fixed asset management | ⚠️ Partial | Strong | 88% | Decision | NetSuite FA vs. Bloomberg evaluation |
| **11. Payroll** |
| Q20 | Payroll integration | ✅ Complete | Strong | 90% | Minor | Provider decision (flexible approach) |
| **12. Payments** |
| Q21 | Credit card payments (customers) | ✅ Complete | Strong | 95% | None | None |
| **13. Customer Financial** |
| Q22 | Finance charges | ✅ Complete | Strong | 100% | None | None |
| Q23 | Customer deposits | ✅ Complete | Strong | 92% | None | None |
| **14. Vendor Management** |
| Q24 | Vendor management | ⚠️ Partial | Strong | 94% | Requirements | Credit limit warning threshold definition |
| **15. Revenue/Cost Recognition** |
| Q25 | Revenue recognition | ⚠️ Partial | Strong | 82% | **Requirements** | **Detailed recognition rules by order type** |
| **16. Historical Data** |
| Q26 | Historical data migration | ✅ Complete | Strong | 94% | Minor | Final cutoff date confirmation |
| **17. Reporting** |
| Q27 | Financial reporting | ✅ Complete | Strong | 91% | Minor | Detailed dashboard requirements (BI session) |
| **18. Compliance** |
| Q28 | Compliance/auditing | ✅ Complete | Moderate | 88% | None | May emerge during implementation |
| **19. Integrations** |
| Q29 | Third-party integrations | ✅ Complete | Strong | 93% | None | None |

### 2.2 Categorized Results

- **✅ Fully Answered** (21 questions, 78%): Questions with complete, well-evidenced answers
- **⚠️ Partially Answered** (6 questions, 22%): Questions with good information but missing design details or decisions
- **❌ Not Answered** (0 questions, 0%): No unanswered questions identified

### 2.3 Organic Discovery Questions Captured

The discovery process captured numerous organic questions beyond the original questionnaire. Key examples:

| Organic Question | Source | Status | REQ-ID |
|------------------|--------|--------|---------|
| What is the remittance process for bill payments? | Lorraine concern during payment workflow discussion | ⚠️ Partial | REQ-010 |
| How do we handle expense allocation to COGS vs. G&A? | Expense management discussion | ⚠️ Partial | REQ-015 |
| What are specific period close completion criteria? | Period close discussion | ⚠️ Partial | REQ-020 |
| What threshold for vendor credit limit warnings? | Vendor management pain point | ⚠️ Partial | REQ-034 |
| How does 15% labor markup affect two GP metrics? | Commission structure discussion | ⚠️ Partial | REQ-023, REQ-024 |

**Assessment**: Organic discovery was excellent. The team probed beyond surface-level answers to understand underlying business logic, particularly around commission structure, GP metrics, and project accounting.

---

## 3. INFORMATION GAPS ANALYSIS

### 3.1 Critical Priority Gaps (🔴 Must Address for Configuration)

#### GAP 1: 15% Labor Markup Continuation Decision
- **Missing Information**: Matt/Mark strategic decision on whether to continue 15% labor markup practice
- **Why Important**: Affects commission calculations, custom development scope, sales compensation structure
- **Current State**: Core automatically adds 15% cost line when labor entered; commission paid after markup reduces GP
- **Who Has Answer**: Matt/Mark (Leadership)
- **How to Get**: Dedicated commission structure session (Session 3)
- **Related REQs**: REQ-023 (labor markup decision), REQ-024 (dual GP metrics), REQ-025 (role-based permissions)
- **Impact**: High - If continuing, requires custom script development; if eliminating, major process and commission impact

#### GAP 2: Revenue Recognition Rules by Order Type
- **Missing Information**: Detailed revenue recognition timing and rules for each order type (standard, mockup, direct bill, intermarket, government, e-commerce)
- **Why Important**: Compliance-critical; errors impact financials and audit requirements
- **Current State**: "Sales order = revenue recognition" but special scenarios need definition
- **Who Has Answer**: Lorraine (CFO), Kipp (Finance/IT), Operations team for process context
- **How to Get**: Dedicated revenue recognition session (Session 1), white paper review
- **Related REQs**: REQ-035 (revenue recognition rules), REQ-036 (project-level tracking)
- **Impact**: Critical - Core financial process requiring detailed documentation and validation

#### GAP 3: Chart of Accounts Consolidation & Mapping
- **Missing Information**: Proposed new COA structure, mapping from 40+ pages to "few hundred accounts", account numbering scheme
- **Why Important**: Foundational to all transactions; impacts reporting, training, historical data migration
- **Current State**: 40+ pages unwieldy and difficult to manage; need consolidated structure
- **Who Has Answer**: Lorraine, Celine (GL), Kevin (GL), Implementation Team for NetSuite best practices
- **How to Get**: Dedicated COA design workshop (Session 2) - 2 hours
- **Related REQs**: REQ-016 (COA consolidation)
- **Impact**: High - Affects all users, all transactions, all reports; requires extensive mapping and training

### 3.2 High Priority Gaps (🟡 Important for Project Success)

#### GAP 4: Commission Structure & GP Calculation Logic
- **Missing Information**: Exact commission calculation formulas, Project GP vs. Commissionable GP distinction in NetSuite, role-based dashboard specs
- **Why Important**: Affects sales compensation, custom dashboard requirements, role-based security design
- **Current State**: Two GP metrics exist (Project GP for management, Commissionable GP for sales); 15% markup affects commissionable GP
- **Who Has Answer**: Lorraine, Kipp, Matt (Leadership), Sales Leadership
- **How to Get**: Commission structure session (Session 3) - 90 minutes
- **Related REQs**: REQ-023 (15% markup), REQ-024 (dual GP metrics), REQ-025 (role-based permissions), REQ-038 (KPI dashboards)
- **Impact**: High - Commission accuracy critical for sales team trust and compensation

#### GAP 5: Automated Allocation Implementation Decision
- **Missing Information**: Whether to implement automated allocation transactions or continue paper-only allocations
- **Why Important**: Impacts month-end process, P&L reporting design, stat account requirements
- **Current State**: "P&Ls that show allocation, they're just on paper" - no allocation transactions in Core
- **Who Has Answer**: Matt/Mark (Leadership)
- **How to Get**: Decision discussion (can be part of Session 3 or separate executive briefing)
- **Related REQs**: REQ-019 (allocation decision)
- **Impact**: Medium - Optional feature; if implemented, requires allocation rules definition

#### GAP 6: Expense Management Platform Selection
- **Missing Information**: Final decision between Expensify Suite App integration vs. switching to RAMP
- **Why Important**: User experience, change management scope, training requirements, cost
- **Current State**: Using Expensify but process is manual and users resistant; Lorraine interested in RAMP
- **Who Has Answer**: Lorraine (CFO), AP team (Guada/Michael), sample expense report submitters
- **How to Get**: Demo both options (Session 6), evaluate project coding capability and user experience
- **Related REQs**: REQ-013 (Expensify), REQ-014 (RAMP), REQ-015 (project allocation requirement)
- **Impact**: Medium - Both options workable; decision affects training and change management approach

### 3.3 Medium Priority Gaps (🟢 Helpful for Optimization)

#### GAP 7: Period Close Checklist Customization Details
- **Missing Information**: Specific KBM checklist steps, task assignments, completion criteria, target timeline (vs. current 10 days)
- **Why Important**: Operational efficiency, clear accountability, timeline reduction goals
- **Who Has Answer**: Lorraine, Celine, Kevin, Kipp (all involved in month-end close)
- **How to Get**: Period close optimization session (Session 4) - 60 minutes
- **Related REQs**: REQ-020 (period close checklist), REQ-021 (module close flexibility)
- **Impact**: Medium - Standard feature with customization needs

#### GAP 8: Bill Payment Workflow Approval Details
- **Missing Information**: Can Lorraine remove items from payment batch or only approve/reject whole run? Remittance automatic or manual trigger?
- **Why Important**: Workflow efficiency, Lorraine's approval preferences, vendor relationship management
- **Who Has Answer**: Lorraine, Guada, Michael (AP Dynamic Duo)
- **How to Get**: Bill payment workflow session (Session 5) - 45 minutes
- **Related REQs**: REQ-010 (bill payment approval workflow)
- **Impact**: Medium - Workflow design detail

#### GAP 9: Vendor Credit Limit Warning Threshold
- **Missing Information**: Specific percentage or dollar threshold for credit limit warnings (suggested: 90%)
- **Why Important**: Prevents "mad scramble at that nth hour" when hitting vendor credit limits unexpectedly
- **Who Has Answer**: Purchasing team, Shannon (Product Coordinator Manager), Lorraine
- **How to Get**: Vendor credit limit session (Session 8) - 20 minutes
- **Related REQs**: REQ-034 (vendor credit limit tracking)
- **Impact**: Medium - Custom alert development

#### GAP 10: Fixed Asset Module Evaluation
- **Missing Information**: Final decision on NetSuite FA module vs. continuing Bloomberg; detailed requirements comparison
- **Why Important**: Cost savings potential, system consolidation, feature parity validation
- **Who Has Answer**: Lorraine (CFO), Implementation Team for capability assessment
- **How to Get**: Fixed asset decision session (Session 7) - 30 minutes
- **Related REQs**: REQ-026 (FA module evaluation)
- **Impact**: Low-Medium - Either option viable; decision affects Bloomberg contract and migration scope

### 3.4 Minor Gaps (Low Priority, Can Be Addressed During Implementation)

- **Positive Pay Process**: Confirm with West Coast Community Bank after NetSuite connection (REQ-008)
- **Wire Transfer Support**: Confirm if included in Advanced Electronic Bill Payments module (REQ-030)
- **Payroll Provider**: Final decision (Paylocity or new provider) - CSV approach flexible regardless (REQ-027/028)
- **48-State Nexus List**: Detailed list of all 48 states with nexus (REQ-004)
- **Historical Data Cutoff**: Final confirmation of 2017 start date for trial balances (REQ-017)
- **Dashboard Requirements**: Detailed BI dashboard specs (handled in separate BI session per notes)

---

## 4. STAKEHOLDER ENGAGEMENT ANALYSIS

### 4.1 Well-Represented Roles (Excellent Input Received)

| Stakeholder | Role | Engagement Level | Key Contributions |
|-------------|------|------------------|-------------------|
| **Lorraine** | CFO/Controller | ⭐⭐⭐⭐⭐ Primary | Decision authority, process knowledge, pain points, prior modern system experience (Blackline/Flowcast) |
| **Kipp** | Former Controller/IT | ⭐⭐⭐⭐⭐ Primary | Deep finance knowledge, technical understanding, "touches everything," 15-year company history |
| **Guada & Michael** | Accounts Payable | ⭐⭐⭐⭐ Strong | Bill payment process, vendor relationships, product coordinator collaboration, Monday payment runs |
| **Implementation Team (Marcus)** | GSI Consultant | ⭐⭐⭐⭐⭐ Primary | NetSuite expertise, solution validation, best practices, white paper creation |

### 4.2 Under-Represented Roles (Need More Involvement)

| Stakeholder | Role | Current Engagement | Needed For | Specific Sessions |
|-------------|------|-------------------|------------|-------------------|
| **Matt & Mark** | Leadership | ⚠️ Referenced but not directly participated | **Critical Decisions**: 15% labor markup, automated allocations | Session 3 (Commission Structure) |
| **Celine & Kevin** | General Ledger | 🔶 Minimal (mentioned by role) | Chart of Accounts design, period close checklist | Session 2 (COA Design), Session 4 (Period Close) |
| **AR Person** | Accounts Receivable (San Jose) | 🔶 Not engaged yet | AR close process, collections, customer deposits | May need targeted AR session |
| **Sales Leadership** | Sales Management | 🔶 Not engaged yet | Commission structure validation, GP metric usage | Session 3 (Commission Structure) |
| **Shannon** | Product Coordinator Manager | 🔶 Referenced but not directly engaged | Vendor relationships, intermarket dealers, credit limits | Session 8 (Vendor Credit Limits) - optional attendance |

### 4.3 Missing Stakeholders

| Stakeholder | Role | Why Needed | Priority |
|-------------|------|-----------|----------|
| **Matt/Mark** | Leadership (CEO/President) | **CRITICAL**: 15% labor markup decision, automated allocation decision | 🔴 Critical - Must participate in Session 3 |
| **Sales Rep(s)** | Sample Sales Team Member | Commission structure validation, GP dashboard requirements, user perspective on 15% markup | 🟡 High - 1-2 sales reps for Session 3 |
| **HR Team** | Human Resources | Payroll provider evaluation status, new HR platform decision | 🟢 Medium - Can provide update asynchronously |

### 4.4 Decision-Maker Involvement

**Strong Decision Authority Identified:**
- ✅ Lorraine (CFO/Controller) - Primary decision maker for all financial processes, clearly empowered
- ✅ Kipp (Finance/IT Partner) - Subject matter expert and influencer, deeply involved
- ⚠️ Matt/Mark (Leadership) - **NEED DIRECT ENGAGEMENT** for strategic decisions (15% markup, allocations)

**Assessment**: Finance team decision authority is clear and strong. Leadership engagement needed specifically for strategic business practice decisions (labor markup continuation, allocation implementation).

---

## 5. FOLLOW-UP MEETING PLAN

**Note**: A comprehensive 879-line `Financial_Management_Follow-Up_Discovery_Session.md` document has been created and validated. The plan below summarizes and prioritizes the 8 sessions identified.

### Critical Path Sessions (Must Schedule First - Next 2 Weeks)

#### **SESSION 1: Revenue Recognition Rules & Project Accounting**
- **Priority**: 🔴 CRITICAL (Compliance requirement, foundational to financial accuracy)
- **Purpose**: Address REQ-035 (revenue recognition rules), REQ-036 (project-level tracking)
- **Required Attendees**: Lorraine (CFO), Kipp (Finance/IT), Marcus (Implementation), Operations representative
- **Duration**: 90 minutes
- **Pre-work for Client**: 
  - Review current revenue recognition practices by order type
  - Gather examples of special scenarios (mockups, direct bill, intermarket, government orders)
  - Current accounting policy documentation (if exists)
- **Consultant Preparation**: Revenue recognition white paper review, ASC 606 compliance requirements
- **Expected Outcome**: Detailed revenue recognition rules documented by order type, compliance validation, implementation approach defined
- **Success Criteria**: 
  - Revenue recognition timing defined for each order type
  - Special scenarios documented with handling procedures
  - Compliance requirements validated
  - Auditor requirements understood

#### **SESSION 2: Chart of Accounts Design & Mapping Workshop**
- **Priority**: 🔴 CRITICAL (Foundational to all transactions and reporting)
- **Purpose**: Address REQ-016 (COA consolidation from 40+ pages to few hundred accounts)
- **Required Attendees**: Lorraine (CFO), Celine (GL), Kevin (GL), Marcus (Implementation), Kipp (as needed)
- **Duration**: 2 hours (longest session - requires detailed design time)
- **Pre-work for Client**: 
  - **CRITICAL**: Export complete current Core chart of accounts (account numbers, descriptions, types, usage frequency)
  - Identify top 50 most-used accounts
  - List accounts that are duplicates or rarely used
  - Bring any existing COA consolidation ideas
- **Consultant Preparation**: NetSuite COA best practices, example dealer COA structures, segmentation strategy (Classes/Departments vs. account proliferation)
- **Expected Outcome**: 
  - Proposed NetSuite COA structure with account numbering scheme
  - Mapping document from old COA to new COA
  - Account categories and ranges defined
  - Implementation plan with user training requirements
- **Success Criteria**: 
  - Target of "few hundred accounts" achieved in design
  - All current transactions can be mapped to new structure
  - Finance team approves proposed structure
  - Historical data migration approach validated

#### **SESSION 3: Commission Structure & GP Calculation Deep Dive**
- **Priority**: 🔴 CRITICAL (High impact on sales compensation, requires leadership decision)
- **Purpose**: Address REQ-023 (15% labor markup decision), REQ-024 (dual GP metrics), REQ-025 (role-based permissions), REQ-038 (KPI dashboards)
- **Required Attendees**: 
  - **MUST HAVE**: Matt/Mark (Leadership - for 15% markup decision)
  - **MUST HAVE**: Lorraine (CFO), Kipp (Finance/IT)
  - **HIGHLY RECOMMENDED**: Sales Leadership, 1-2 sales reps (commission validation)
- **Duration**: 90 minutes
- **Pre-work for Client**: 
  - **CRITICAL**: Matt/Mark availability confirmation
  - Sample commission calculations (current process)
  - Examples of Project GP vs. Commissionable GP reports
  - List of who currently sees which GP metric (role-based visibility documentation)
- **Consultant Preparation**: Custom script development estimate (if 15% markup continues), dashboard design options, role-based security configuration approach
- **Expected Outcome**: 
  - **DECISION**: 15% labor markup continues or is eliminated
  - If continuing: Implementation approach defined (custom script requirements)
  - Commission calculation rules fully documented
  - GP reporting and dashboard requirements specified
  - Role-based permissions matrix defined
- **Success Criteria**: 
  - Matt/Mark decision on 15% markup finalized
  - Commission calculation logic validated by sales team
  - GP dashboard mockups approved by stakeholders
  - Role-based visibility requirements clear

### High Priority Sessions (Schedule Within 3-4 Weeks)

#### **SESSION 4: Period Close Process Optimization**
- **Priority**: 🟡 HIGH (Operational efficiency, timeline reduction opportunity)
- **Purpose**: Address REQ-020 (period close checklist), REQ-021 (AP/AR close flexibility)
- **Required Attendees**: Lorraine (CFO), Celine (GL), Kevin (GL), Kipp (as needed)
- **Duration**: 60 minutes
- **Pre-work for Client**: 
  - Current Excel close checklist
  - Breakdown of typical close timeline (which steps take how many days)
  - List of recurring journal entries posted each month
  - Reconciliation procedures and timing
- **Consultant Preparation**: NetSuite period close checklist best practices, typical timeline benchmarks for similar clients
- **Expected Outcome**: NetSuite Period Close Checklist customized to KBM needs, task assignments defined, target timeline established (goal: reduce from 10 days)

#### **SESSION 5: Bill Payment & Cash Management Workflow Details**
- **Priority**: 🟡 HIGH (Critical AP process, high dollar amounts, workflow clarity needed)
- **Purpose**: Address REQ-010 (bill payment approval workflow details)
- **Required Attendees**: Lorraine (CFO), Guada (AP), Michael (AP)
- **Duration**: 45 minutes
- **Pre-work for Client**: 
  - Sample payment run details (how compiled, how approved)
  - List of vendors requiring prepayments
  - West Coast Community Bank positive pay requirements (if known)
- **Consultant Preparation**: Advanced Electronic Bill Payments workflow options, remittance handling approaches, positive pay integration
- **Expected Outcome**: Bill payment approval workflow fully defined, remittance process confirmed (automatic or manual), positive pay process documented

#### **SESSION 6: Expense Management System Decision & Project Coding**
- **Priority**: 🟡 HIGH (User experience, project coding requirement critical)
- **Purpose**: Address REQ-013 (Expensify), REQ-014 (RAMP), REQ-015 (project allocation)
- **Required Attendees**: Lorraine (CFO), Guada/Michael (AP - current processors), 2-3 sample expense submitters (Matt, field team members)
- **Duration**: 45 minutes (plus separate demo time for both platforms)
- **Pre-work for Client**: 
  - Schedule demos: Expensify Suite App and RAMP (GSI to coordinate)
  - Sample expense reports showing project vs. G&A allocation needs
  - Current Expensify usage metrics (reports/month, users, costs)
- **Consultant Preparation**: Coordinate Expensify and RAMP demo sessions, prepare project coding evaluation criteria
- **Expected Outcome**: **DECISION**: Expensify Suite App OR RAMP, project coding requirements validated, integration specifications defined

### Medium Priority Sessions (Can Be Scheduled Flexibly During Implementation)

#### **SESSION 7: Fixed Asset Management Decision**
- **Priority**: 🟢 MEDIUM (Cost savings opportunity, either option viable)
- **Purpose**: Address REQ-026 (NetSuite FA module vs. Bloomberg evaluation)
- **Required Attendees**: Lorraine (CFO), Marcus (Implementation for capability review)
- **Duration**: 30 minutes
- **Pre-work for Client**: 
  - List of fixed assets in Bloomberg (categories, quantities)
  - Bloomberg feature list (what you use, what you need)
  - Bloomberg annual cost
  - Sample depreciation report
- **Consultant Preparation**: NetSuite FA module capabilities overview, migration approach, cost comparison
- **Expected Outcome**: **DECISION**: NetSuite FA module OR continue Bloomberg, migration plan if NetSuite FA, cost-benefit analysis

#### **SESSION 8: Vendor Credit Limit Tracking & Alerts**
- **Priority**: 🟢 MEDIUM (Custom development scoping)
- **Purpose**: Address REQ-034 (vendor credit limit tracking with warnings)
- **Required Attendees**: Lorraine (CFO), Purchasing team representative, Shannon (Product Coordinator Manager - optional)
- **Duration**: 20 minutes
- **Pre-work for Client**: 
  - List of vendors with credit limits and amounts
  - Examples of recent credit limit issues
  - Identify who should receive alerts
- **Consultant Preparation**: Custom alert development options, dashboard widget design, PO blocking vs. warning approach
- **Expected Outcome**: Warning threshold defined (e.g., 90%), alert mechanism specified, custom development requirements documented

### Decisions That Can Be Handled Asynchronously

**DECISION: Automated Allocation Implementation** (REQ-019)
- Can be addressed in Session 3 with Matt/Mark, or via separate executive briefing
- Low urgency: Optional feature, may continue paper-only allocations

**DECISION: Payroll Provider** (REQ-027/028)
- Can be confirmed via email/meeting with HR team
- Low impact: CSV import approach flexible regardless of provider
- Just need timeline for decision

---

## 6. PRIORITY CLASSIFICATION

### 🔴 Critical Priority - Must Address Before Configuration (5 items)

| Gap | Question/REQ | Missing Information | Business Impact | Who Can Answer | How to Get | Session |
|-----|--------------|---------------------|-----------------|----------------|------------|---------|
| **GAP-1** | REQ-023 | 15% labor markup continuation decision | Commission calculations, custom development scope, sales compensation structure | Matt/Mark | Session 3 | Session 3 (90 min) |
| **GAP-2** | REQ-035 | Revenue recognition rules by order type | Financial compliance, audit requirements, revenue accuracy | Lorraine, Kipp, Operations | Session 1 | Session 1 (90 min) |
| **GAP-3** | REQ-016 | Chart of accounts structure and mapping | All transactions, reporting, training, historical data | Lorraine, Celine, Kevin | Session 2 | Session 2 (120 min) |
| **GAP-4A** | REQ-024 | Project GP vs. Commissionable GP calculation logic | Custom dashboard development, reporting accuracy | Lorraine, Kipp, Matt | Session 3 | Session 3 (90 min) |
| **GAP-4B** | REQ-025 | Role-based permissions for GP visibility | Security design, dashboard access control | Lorraine, Kipp | Session 3 | Session 3 (90 min) |

**Total Critical Path Time**: 5.5 hours across 3 sessions

### 🟡 High Priority - Important for Successful Go-Live (4 items)

| Gap | Question/REQ | Missing Information | Business Impact | Who Can Answer | How to Get | Session |
|-----|--------------|---------------------|-----------------|----------------|------------|---------|
| **GAP-5** | REQ-019 | Automated allocation decision | Month-end process design, P&L reporting | Matt/Mark | Session 3 or async | Decision discussion |
| **GAP-6** | REQ-013/014 | Expensify vs. RAMP decision | User experience, training, change management | Lorraine, AP team, users | Session 6 + demos | Session 6 (45 min) |
| **GAP-7** | REQ-020 | Period close checklist details | Operational efficiency, timeline reduction | Lorraine, Celine, Kevin | Session 4 | Session 4 (60 min) |
| **GAP-8** | REQ-010 | Bill payment approval workflow | Workflow efficiency, Lorraine's preferences | Lorraine, Guada, Michael | Session 5 | Session 5 (45 min) |

**Total High Priority Time**: 2.5 hours across 3 sessions (plus demo time for GAP-6)

### 🟢 Medium Priority - Helpful for Optimization (3 items)

| Gap | Question/REQ | Missing Information | Business Impact | Who Can Answer | How to Get | Session |
|-----|--------------|---------------------|-----------------|----------------|------------|---------|
| **GAP-9** | REQ-034 | Vendor credit limit warning threshold | Prevents vendor credit limit surprises | Lorraine, Purchasing, Shannon | Session 8 | Session 8 (20 min) |
| **GAP-10** | REQ-026 | Fixed asset module evaluation | Cost savings, system consolidation | Lorraine, Implementation Team | Session 7 | Session 7 (30 min) |
| **GAP-11** | REQ-027/028 | Payroll provider decision | Integration approach (flexible regardless) | Lorraine, HR Team | Email/async | No session needed |

**Total Medium Priority Time**: 50 minutes across 2 sessions

### ⚪ Low Priority - Can Be Addressed During Implementation

- Positive pay process confirmation with bank (REQ-008)
- Wire transfer module support confirmation (REQ-030)
- Detailed 48-state nexus list (REQ-004)
- Final historical data cutoff date (REQ-017)
- BI dashboard detailed requirements (handled in separate BI session)

---

## 7. CONSULTANT ACTION PLAN

### 7.1 Immediate Actions (Next 1-2 Weeks)

| Priority | Action | Owner | Due Date | Dependencies |
|----------|--------|-------|----------|--------------|
| 🔴 CRITICAL | **Schedule Session 1: Revenue Recognition** (90 min) with Lorraine, Kipp, Marcus, Operations | GSI Project Manager | Nov 1, 2025 | Lorraine availability |
| 🔴 CRITICAL | **Schedule Session 2: COA Design Workshop** (120 min) with Lorraine, Celine, Kevin, Marcus | GSI Project Manager | Nov 4, 2025 | **Pre-work**: COA export from Core |
| 🔴 CRITICAL | **Schedule Session 3: Commission Structure** (90 min) with Matt/Mark, Lorraine, Kipp, Sales Leadership | GSI Project Manager | Nov 6, 2025 | **CRITICAL**: Matt/Mark availability confirmation |
| 🔴 CRITICAL | **Request Pre-Work from Client**: COA export, commission calculation examples, period close checklist | GSI BA | Oct 28, 2025 | Celine/Kevin for COA export |
| 🟡 HIGH | **Coordinate Demos**: Expensify Suite App and RAMP integrations | GSI Technical Team | Nov 8, 2025 | Vendor availability |
| 🟡 HIGH | **Prepare Revenue Recognition White Paper** for Session 1 review | Marcus | Oct 30, 2025 | None |
| 🟡 HIGH | **Prepare COA Best Practices** and example dealer structures for Session 2 | Marcus | Nov 1, 2025 | None |

### 7.2 Follow-up Actions (Weeks 3-4)

| Priority | Action | Owner | Due Date | Dependencies |
|----------|--------|-------|----------|--------------|
| 🟡 HIGH | **Schedule Session 4: Period Close** (60 min) with Lorraine, Celine, Kevin | GSI Project Manager | Nov 11, 2025 | Session 2 complete (COA impacts close) |
| 🟡 HIGH | **Schedule Session 5: Bill Payment Workflow** (45 min) with Lorraine, Guada, Michael | GSI Project Manager | Nov 13, 2025 | Banking integration approach confirmed |
| 🟡 HIGH | **Schedule Session 6: Expense Management Decision** (45 min) with Lorraine, AP team, sample users | GSI Project Manager | Nov 15, 2025 | After demos completed |
| 🟢 MEDIUM | **Schedule Session 7: Fixed Asset Decision** (30 min) with Lorraine, Marcus | GSI Project Manager | Nov 18, 2025 | Bloomberg comparison prepared |
| 🟢 MEDIUM | **Schedule Session 8: Vendor Credit Limits** (20 min) with Lorraine, Purchasing, Shannon (opt) | GSI Project Manager | Nov 20, 2025 | None |
| 🟡 HIGH | **Confirm Decisions Asynchronously**: Automated allocations (Matt/Mark), Payroll provider (HR team) | GSI BA | Nov 20, 2025 | None |

### 7.3 Completion Actions (Post-Sessions)

| Action | Owner | Due Date | Dependencies |
|--------|-------|----------|--------------|
| **Update Questionnaire**: Incorporate all session findings into Questionnaire_FinancialManagement_v2.0.md | GSI BA | Nov 25, 2025 | All 8 sessions complete |
| **Update Requirements Map**: Refine REQ classifications, add design details from sessions | GSI BA | Nov 25, 2025 | All 8 sessions complete |
| **Create Solution Design Specs**: For ACCOMMODATE requirements (REQ-015, REQ-016, REQ-024, REQ-025, REQ-034, REQ-035, REQ-038) | GSI Solution Architect | Dec 2, 2025 | Updated requirements map |
| **Finalize BRD**: Complete BRD_FinancialManagement_v1.0.md with all requirements validated | GSI BA | Dec 6, 2025 | Solution design specs complete |
| **Client Sign-off**: Present BRD to Lorraine and Matt/Mark for approval | GSI Project Manager | Dec 9, 2025 | BRD finalized |
| **Configuration Planning**: Sequence configuration tasks based on dependencies | GSI Technical Lead | Dec 13, 2025 | BRD approved |

---

## 8. SUCCESS METRICS

### 8.1 Completion Targets

| Milestone | Current Status | After Critical Sessions (Wks 1-2) | After All Sessions (Wk 3-4) | Target Date |
|-----------|----------------|-----------------------------------|------------------------------|-------------|
| **Overall Questionnaire Completion** | **92%** | **96%** (critical gaps closed) | **100%** (all gaps closed) | Nov 20, 2025 |
| **Critical Decisions Made** | 0 of 5 | 3 of 5 (15% markup, allocations, revenue recognition rules) | 5 of 5 (+ expense platform, FA module) | Nov 20, 2025 |
| **Requirements Validated** | 38 REQs documented | 38 REQs with design details | 38 REQs fully specified | Nov 25, 2025 |
| **Solution Design Specs** | 0 of 9 ACCOMMODATE REQs | 4 of 9 (revenue recognition, COA, GP metrics, permissions) | 9 of 9 (all ACCOMMODATE REQs) | Dec 2, 2025 |
| **BRD Completion** | Not started | 50% (requirements complete, solution design in progress) | 100% (BRD ready for approval) | Dec 6, 2025 |
| **Client Sign-off** | Not applicable | Not applicable | BRD approved by Lorraine & Matt/Mark | Dec 9, 2025 |

### 8.2 Session Completion Tracking

| Session | Duration | Priority | Target Date | Pre-Work Status | Scheduled? | Complete? |
|---------|----------|----------|-------------|-----------------|------------|-----------|
| Session 1: Revenue Recognition | 90 min | 🔴 Critical | Nov 1 | ⏳ Pending | ⬜ No | ⬜ No |
| Session 2: COA Design | 120 min | 🔴 Critical | Nov 4 | 🔴 **COA export required** | ⬜ No | ⬜ No |
| Session 3: Commission Structure | 90 min | 🔴 Critical | Nov 6 | 🔴 **Matt/Mark confirmation required** | ⬜ No | ⬜ No |
| Session 4: Period Close | 60 min | 🟡 High | Nov 11 | ⏳ Pending | ⬜ No | ⬜ No |
| Session 5: Bill Payment | 45 min | 🟡 High | Nov 13 | ⏳ Pending | ⬜ No | ⬜ No |
| Session 6: Expense Management | 45 min | 🟡 High | Nov 15 | 🟡 Demo scheduling needed | ⬜ No | ⬜ No |
| Session 7: Fixed Assets | 30 min | 🟢 Medium | Nov 18 | ⏳ Pending | ⬜ No | ⬜ No |
| Session 8: Vendor Credit Limits | 20 min | 🟢 Medium | Nov 20 | ⏳ Pending | ⬜ No | ⬜ No |
| **TOTAL** | **8.5 hours** | | | | | |

### 8.3 Quality Metrics

| Quality Gate | Current | Target | Status |
|--------------|---------|--------|--------|
| **Confidence Rating (Average)** | 92% | 95%+ | 🟢 Excellent baseline |
| **Must-Have Requirements Confidence** | 94% (36 REQs) | 98%+ | 🟡 Gap sessions will elevate |
| **Critical Gaps Remaining** | 5 gaps | 0 gaps | 🔴 Sessions 1-3 required |
| **High Priority Gaps Remaining** | 4 gaps | 0 gaps | 🟡 Sessions 4-6 required |
| **Decisions Pending** | 5 decisions | 0 decisions | 🔴 Leadership engagement required |
| **ACCOMMODATE REQs with Solution Design** | 0 of 9 (0%) | 9 of 9 (100%) | 🔴 Post-session design work |

---

## 9. DECISION LOG (DECISIONS DETECTED DURING ANALYSIS)

### Confirmed Decisions from Discovery

| Decision ID | Decision | Decision Maker | Status | Date | REQ-ID | Evidence |
|-------------|----------|----------------|--------|------|--------|----------|
| DEC-FM-001 | Single NetSuite subsidiary for consolidated KB+Hoag operations | Team | ✅ **CONFIRMED** | Sept 2025 | REQ-001 | "Single NetSuite subsidiary... KB + Hoag merged operations" |
| DEC-FM-002 | 13 accounting periods (not 12) on calendar year basis | Lorraine | ✅ **CONFIRMED** | Sept 2025 | REQ-002 | "I would like 13. 13. Core only does 12." - Lorraine |
| DEC-FM-003 | US Dollar only (no multi-currency) | Team | ✅ **CONFIRMED** | Sept 2025 | REQ-003 | "We're all in U.S. dollar" |
| DEC-FM-004 | Native SuiteTax (not Avalara) for 48-state sales tax | Team | ✅ **CONFIRMED** | Sept 2025 | REQ-004 | "Native SuiteTax (not Avalara)" |
| DEC-FM-005 | Implement bank feeds with West Coast Community Bank | Team | ✅ **CONFIRMED** | Sept 2025 | REQ-008 | "Confirmed as part of NetSuite Bank Feeds program" |
| DEC-FM-006 | Advanced Electronic Bill Payments for ACH | Team | ✅ **CONFIRMED** | Sept 2025 | REQ-009 | "Pay via ACH directly from NetSuite" |
| DEC-FM-007 | NetSuite Period Close Checklist (not Blackline/Flowcast) | Lorraine/Marcus | ✅ **CONFIRMED** | Sept 2025 | REQ-020 | "Use NetSuite native checklist (Marcus)... No need for separate Blackline/Flowcast" |
| DEC-FM-008 | Open all 13 periods at year start, close progressively | Marcus/Team | ✅ **CONFIRMED** | Sept 2025 | REQ-022 | "Open entire year at once... Set December reminder" - Best practice |
| DEC-FM-009 | Maintain Stripe for customer credit card payments | Team | ✅ **CONFIRMED** | Sept 2025 | REQ-029 | "Stay with Stripe currently (works fine, incidental use)" |
| DEC-FM-010 | Migrate financial data back to 2017 | Lorraine | ✅ **CONFIRMED** | Sept 2025 | REQ-017 | "Back to 2017 (Lorraine's decision)" |

### Pending Decisions Requiring Follow-Up

| Decision ID | Decision | Decision Maker | Status | Target Date | REQ-ID | Impact |
|-------------|----------|----------------|--------|-------------|--------|--------|
| DEC-FM-011 | **15% labor markup continuation** | **Matt/Mark** | ⏳ **PENDING** | Nov 6, 2025 | REQ-023 | 🔴 **HIGH** - Commission impact, custom development |
| DEC-FM-012 | **Automated allocation transactions implementation** | **Matt/Mark** | ⏳ **PENDING** | Nov 6, 2025 | REQ-019 | 🟡 MEDIUM - P&L reporting design |
| DEC-FM-013 | **Expensify Suite App vs. RAMP** | **Lorraine** | ⏳ **PENDING** | Nov 15, 2025 | REQ-013/014 | 🟡 MEDIUM - User experience, training |
| DEC-FM-014 | **NetSuite FA module vs. continue Bloomberg** | **Lorraine** | ⏳ **PENDING** | Nov 18, 2025 | REQ-026 | 🟢 LOW-MEDIUM - Cost savings opportunity |
| DEC-FM-015 | **Payroll provider (Paylocity or new)** | **Lorraine/HR** | ⏳ **PENDING** | Nov 20, 2025 | REQ-027/028 | 🟢 LOW - CSV approach flexible |

---

## 10. RISK ASSESSMENT

### High-Risk Requirements Requiring Close Attention

| REQ-ID | Requirement | Risk Description | Likelihood | Impact | Mitigation Strategy | Status |
|--------|-------------|------------------|------------|--------|---------------------|--------|
| **REQ-016** | Chart of accounts consolidation (40+ pages → few hundred) | Massive change impacts all transactions, reports, user muscle memory | High | High | Dedicated 2-hour design workshop, comprehensive mapping, phased user training, extensive testing, go-live reference guides | Session 2 planned |
| **REQ-035** | Revenue recognition rules by order type | Complex, compliance-critical; errors impact financials and audit | Medium | Very High | Dedicated 90-min session, white paper review, auditor involvement, detailed documentation, validation testing | Session 1 planned |
| **REQ-024** | Project GP vs. Commissionable GP reporting | Custom calculation logic required, commission accuracy critical | Medium | High | Detailed requirements session, calculation validation, extensive testing, sales team sign-off | Session 3 planned |
| **REQ-023** | 15% labor markup (if continuing) | Custom script development, commission impact, decision pending | High | High | **CRITICAL**: Matt/Mark decision required; if continuing, thorough development and testing; if eliminating, communication plan | Session 3 planned |
| **REQ-004** | 48-state nexus tax management | Ongoing compliance, certificate maintenance, audit risk | Medium | High | SuiteTax configuration validation, certificate upload process documentation, expiration monitoring dashboard | Low risk - standard feature |
| **REQ-009** | Advanced Electronic Bill Payments ($3M payment runs) | Critical AP process, high dollar amounts, vendor relationship impact | Medium | High | Thorough testing, parallel run period, fallback to NACHA file, remittance confirmation process | Session 5 planned |
| **REQ-015** | Project vs. G&A expense allocation | Must integrate with Expensify/RAMP, COGS accuracy critical | Medium | Medium | Integration testing, project coding validation, user training | Session 6 planned |

### Change Management Risks

| Risk | Description | Likelihood | Impact | Mitigation |
|------|-------------|------------|--------|------------|
| **COA Change Resistance** | Users memorized account numbers over years; 40+ pages to few hundred major adjustment | High | Medium | Early communication, training with mapping reference guide, side-by-side comparison reports, phased rollout |
| **15% Markup Elimination (if decided)** | Sales team resistance if commission calculation changes | Medium | High | Executive communication from Matt/Mark, commission impact analysis, advance notice (6+ months?), grandfathering options |
| **Expense Platform Change** | If switching to RAMP from Expensify, users must learn new system | Medium | Low | Strong UX demo to show ease of use, mobile-first training, early adopter champions, parallel run period |
| **Period Close Process Change** | From Excel to system-guided checklist - trust in automation | Low | Low | Lorraine's prior Blackline/Flowcast experience helps; show time savings; parallel run first month |

---

## 11. RECOMMENDATIONS & NEXT STEPS

### Immediate Priorities (Next 5 Business Days)

1. **Schedule Critical Path Sessions 1-3** (Nov 1, 4, 6) 
   - **CRITICAL**: Confirm Matt/Mark availability for Session 3
   - Block Lorraine's calendar for all three sessions
   - Ensure Celine/Kevin availability for Session 2

2. **Request Critical Pre-Work**
   - COA export from Core (Celine/Kevin) - **REQUIRED** for Session 2
   - Commission calculation examples (Lorraine/Kipp)
   - Period close checklist (Lorraine)

3. **Prepare Session Materials**
   - Revenue recognition white paper (Marcus)
   - COA best practices and examples (Marcus)
   - Commission structure analysis (GSI BA)

### Short-Term Actions (Weeks 1-2)

4. **Complete Critical Path Sessions** (Sessions 1-3)
   - Finalize revenue recognition rules
   - Design and approve new COA structure
   - **Obtain 15% labor markup decision from Matt/Mark**
   - Define commission calculation logic

5. **Coordinate Demos** (Expensify & RAMP)
   - Schedule with vendors
   - Invite Lorraine, AP team, sample expense submitters
   - Evaluate project coding capabilities

### Medium-Term Actions (Weeks 3-4)

6. **Complete Remaining Sessions** (Sessions 4-8)
   - Period close optimization
   - Bill payment workflow details
   - Expense management decision
   - Fixed asset evaluation
   - Vendor credit limit tracking

7. **Finalize Async Decisions**
   - Automated allocations (Matt/Mark)
   - Payroll provider (HR team)

### Deliverable Updates (Week 4-5)

8. **Update Discovery Artifacts**
   - Questionnaire_FinancialManagement_v2.0.md (incorporate all session findings)
   - Requirements_Map_FinancialManagement_v2.0.md (add design details)

9. **Create Solution Design Specs**
   - REQ-015: Project vs. G&A expense allocation
   - REQ-016: Chart of accounts mapping
   - REQ-024: Dual GP metrics (Project vs. Commissionable)
   - REQ-025: Role-based permissions matrix
   - REQ-034: Vendor credit limit alerts
   - REQ-035: Revenue recognition rules
   - REQ-038: Project-level KPI dashboards

10. **Finalize BRD**
    - Complete BRD_FinancialManagement_v1.0.md
    - Present to Lorraine and Matt/Mark for approval

### Success Indicators

✅ **Week 1-2**: Critical decisions made (15% markup, revenue recognition rules, COA structure approved)  
✅ **Week 3**: All 8 sessions completed, all decisions finalized  
✅ **Week 4**: Updated questionnaire and requirements map v2.0 delivered  
✅ **Week 5**: Solution design specs complete for all ACCOMMODATE requirements  
✅ **Week 6**: BRD finalized and approved by client leadership

---

## APPENDIX A: SESSION SCHEDULING TEMPLATE

```
EMAIL SUBJECT: Financial Management Follow-Up Discovery Sessions - Scheduling Request

Dear Lorraine, Matt, Mark, and Finance Team,

Following our comprehensive financial management discovery sessions in September, we have achieved 92% completeness on requirements gathering - excellent progress! To reach 100% and finalize the Business Requirements Document, we need to schedule 8 targeted follow-up sessions totaling 8.5 hours over the next 3-4 weeks.

These sessions will close critical gaps including:
- Revenue recognition rules (compliance-critical)
- Chart of accounts consolidation design (40+ pages to few hundred accounts)
- Commission structure and 15% labor markup decision (Matt/Mark decision required)
- And 5 additional optimization sessions

CRITICAL PATH SESSIONS (Must Schedule First - Week of Nov 1):

SESSION 1: Revenue Recognition Rules & Project Accounting
- Date/Time: [Proposed: November 1, 2-3:30 PM]
- Duration: 90 minutes
- Required: Lorraine, Kipp, Marcus, Operations representative
- Purpose: Define revenue recognition rules by order type for compliance

SESSION 2: Chart of Accounts Design & Mapping Workshop  
- Date/Time: [Proposed: November 4, 9-11 AM]
- Duration: 120 minutes (longest session)
- Required: Lorraine, Celine, Kevin, Marcus
- Purpose: Design new COA structure and mapping from current 40+ pages
- **PRE-WORK REQUIRED**: Celine/Kevin to export complete current Core COA

SESSION 3: Commission Structure & GP Calculation Deep Dive
- Date/Time: [Proposed: November 6, 10-11:30 AM]
- Duration: 90 minutes
- Required: **Matt/Mark (CRITICAL)**, Lorraine, Kipp, Sales Leadership (opt)
- Purpose: **15% labor markup decision**, commission calculations, dual GP metrics
- **PRE-WORK REQUIRED**: Matt/Mark availability confirmation

[Continue with Sessions 4-8 details...]

Please confirm availability for Sessions 1-3 by October 25th. We will schedule Sessions 4-8 once the critical path is complete.

Thank you,
[GSI Project Manager]
```

---

## APPENDIX B: PRE-WORK CHECKLIST

### Session 1: Revenue Recognition (Nov 1)
- [ ] Review current revenue recognition practices by order type
- [ ] Gather examples: mockup orders, direct bill, intermarket, government orders
- [ ] Current accounting policy documentation (if exists)
- [ ] List special scenarios that need handling procedures

### Session 2: COA Design (Nov 4) - **CRITICAL PRE-WORK**
- [ ] **Export complete Core chart of accounts** (account #, description, type, usage frequency)
- [ ] **Identify top 50 most-used accounts**
- [ ] **List duplicate or rarely used accounts**
- [ ] Bring any existing COA consolidation ideas or drafts

### Session 3: Commission Structure (Nov 6) - **CRITICAL ATTENDANCE**
- [ ] **Confirm Matt/Mark availability** (required for 15% markup decision)
- [ ] Prepare sample commission calculations (current process)
- [ ] Examples of Project GP vs. Commissionable GP reports
- [ ] Document who currently sees which GP metric (role-based visibility)

### Session 4: Period Close (Nov 11)
- [ ] Current Excel close checklist
- [ ] Breakdown of typical close timeline (steps and days)
- [ ] List of recurring journal entries posted each month
- [ ] Reconciliation procedures and timing

### Session 5: Bill Payment (Nov 13)
- [ ] Sample payment run details (how compiled, how approved)
- [ ] List of vendors requiring prepayments
- [ ] West Coast Community Bank positive pay requirements (if known)

### Session 6: Expense Management (Nov 15)
- [ ] GSI to schedule: Expensify Suite App and RAMP demos
- [ ] Sample expense reports (project vs. G&A allocation examples)
- [ ] Current Expensify usage metrics (reports/month, users, costs)
- [ ] List primary expense submitters to invite to demos

### Session 7: Fixed Assets (Nov 18)
- [ ] List of fixed assets in Bloomberg (categories, quantities)
- [ ] Bloomberg feature list (what you use, what you need)
- [ ] Bloomberg annual cost
- [ ] Sample depreciation report from Bloomberg

### Session 8: Vendor Credit Limits (Nov 20)
- [ ] List of vendors with credit limits and amounts
- [ ] Examples of recent credit limit issues
- [ ] Identify who should receive credit limit warning alerts

---

## APPENDIX C: REQUIREMENTS NEEDING SOLUTION DESIGN (ACCOMMODATE)

| REQ-ID | Requirement | Why ACCOMMODATE | Solution Design Needed |
|--------|-------------|-----------------|------------------------|
| REQ-015 | Project vs. G&A expense allocation | Custom field mapping, integration configuration | Integration spec with project coding fields |
| REQ-016 | COA consolidation (40+ pages → few hundred) | Major restructure, comprehensive mapping, custom configuration | New COA structure, mapping document, migration plan |
| REQ-024 | Project GP vs. Commissionable GP reporting | Custom calculation logic, dual metrics | Calculation specification, saved searches, custom reports |
| REQ-025 | Role-based permissions for GP visibility | Custom permission sets, role configuration | Permission matrix, role definitions, security design |
| REQ-034 | Vendor credit limit tracking with alerts | Custom alert/warning mechanism | Alert threshold logic, dashboard widget, email notifications |
| REQ-035 | Revenue recognition rules by order type | Complex business rules, compliance requirements | Recognition rules document, validation logic, audit trail |
| REQ-038 | Project-level KPI dashboards | Custom dashboards for dual GP metrics | Dashboard mockups, KPI definitions, data sources |

**Optional (Pending Decisions):**
| REQ-ID | Requirement | Condition | Solution Design Needed |
|--------|-------------|-----------|------------------------|
| REQ-019 | Automated allocations | If Matt/Mark decide to implement | Allocation rules, stat accounts, transaction automation |
| REQ-023 | 15% labor markup | If Matt/Mark decide to continue | Custom script for automatic line addition, trigger logic |

**Total Solution Design Effort**: 7-9 specifications (depending on decisions)

---

*End of Gap Analysis - Financial Management v1.0*


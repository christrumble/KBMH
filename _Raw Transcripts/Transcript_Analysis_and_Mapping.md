# KBMH Discovery Transcript Analysis and Mapping

## Executive Summary
Three discovery transcripts were recorded between September 17-18, 2025. Analysis shows coverage of general kickoff, Marketing/CRM, and Financial Management. Several business process areas lack dedicated transcription.

---

## Transcript Mapping

### Transcript 1: GMT20250917-154358_Recording.cc.vtt
**Date:** September 17, 2025 (PM - 1:06 PM - 1:38 PM)  
**Duration:** ~32 minutes  
**Session Type:** Project Kickoff & Methodology Overview

**Topics Covered:**
- DREAM methodology (Discovery, Realize, Educate, Actualize, Maintain/Maximize)
- Discovery process framework (Current State, Objectives, Requirements - Functional & Technical)
- Deliverables: BRDs, Solution Designs, Business Process Questionnaires
- Timeline expectations (6-8 weeks for discovery)
- Data migration strategy overview
- Go-live approach (soft cutover vs hard cutover)
- Post-implementation support (Suite Care program)
- General Q&A about the implementation

**Process Area Mapping:** General/Cross-Functional  
**Recommendation:** Keep in main folder or create a "0 - Project Kickoff" folder

---

### Transcript 2: GMT20250917-200141_Recording.transcript.vtt
**Date:** September 17, 2025 (PM - 8:00 PM session)  
**Duration:** ~2 hours  
**Session Type:** Marketing and Lead Management / CRM Discovery

**Topics Covered:**
- Email marketing (MailChimp current state, NetSuite email marketing capabilities - 120K emails/month)
- Lead capture and management (web forms, contact us forms)
- Lead sources: Influencers, brokers, A&D firms, RFPs, web forms
- CRM functionality (currently using Zendesk)
- Business development reps vs account managers (roles and responsibilities)
- RFP workflow and management
- Lead qualification and routing
- Asana integration for marketing project requests
- Opportunity management and forecasting
- Lead-to-quote conversion process
- Marketing project volume tracking

**Process Area Mapping:**
- **Primary:** Marketing (60%)
- **Secondary:** CRM (40%)

**Recommendation:** 
- Copy to both `Marketing/2 Input/` and `CRM/2 Input/` folders
- This transcript should inform both Marketing and CRM questionnaires

---

### Transcript 3: GMT20250918-211018_Recording.transcript.vtt
**Date:** September 18, 2025  
**Duration:** ~2+ hours  
**Session Type:** Financial Management Discovery

**Topics Covered:**
- Finance team structure (AP, AR, GL teams in multiple locations including Philippines)
- Company structure and subsidiary setup
- Accounting periods (13 periods preferred vs Core's 12)
- Calendar year fiscal year
- Tax management (Sweet Tax for sales tax, use tax in IL & MO)
- Purchase Orders and vendor acknowledgments
- Journal entries and allocations
- Banking and cash management
- Credit card management
- Budgeting and planning
- Period close processes
- Customer financial management
- Project accounting
- Revenue and cost recognition (NetSuite vs Core differences)
- Vendor and AP management
- Expense management (travel reimbursement, project costs vs G&A)
- Asset management (fixed assets)
- Financial reporting and analytics
- Commission calculations
- Labor margin contingency (15% load factor on labor costs)
- Commissionable GP vs actual GP

**Process Area Mapping:**
- **Primary:** Financial Management (100%)

**Recommendation:** 
- Copy to `Financial Management/2 Input/` folder
- This is comprehensive financial management coverage

---

## Process Area Coverage Analysis

### ✅ GOOD TRANSCRIPTION COVERAGE

| Process Area | Transcript(s) | Coverage Quality | Notes |
|--------------|---------------|------------------|-------|
| **Marketing** | Transcript 2 | Excellent | Comprehensive coverage of marketing operations, lead management, RFP process |
| **CRM** | Transcript 2 | Very Good | CRM workflow, Zendesk usage, opportunity management well documented |
| **Financial Management** | Transcript 3 | Excellent | Thorough coverage of all financial processes, AP, AR, GL, project accounting |

### ⚠️ PARTIAL/INDIRECT COVERAGE

| Process Area | Mentioned In | Coverage Quality | Notes |
|--------------|--------------|------------------|-------|
| **Order Management** | Transcript 3 | Partial | POs and vendor acknowledgments discussed; likely more in a separate session |
| **System Setup and Configuration** | Transcript 1, 3 | Partial | Chart of accounts, subsidiary setup, but not comprehensive |

### ❌ MISSING TRANSCRIPTION

| Process Area | Status | Priority | Recommended Focus Areas |
|--------------|--------|----------|-------------------------|
| **Business Intelligence** | No dedicated transcript | HIGH | Reporting requirements, dashboards, KPIs, data analytics needs, Excel exports, decision-making processes |
| **Operations** | No dedicated transcript | HIGH | Operational workflows, warehouse/logistics, inventory management (if applicable), field operations |
| **Order Management** | Likely incomplete | MEDIUM-HIGH | Full order-to-cash cycle, quote-to-order conversion, order processing, change orders |
| **Pre-Quote** | No dedicated transcript | MEDIUM-HIGH | Estimating process, labor quotes, internal/LTS/subs quoting, quote preparation workflow |
| **System Setup and Configuration** | Incomplete | MEDIUM | User roles, permissions, security, system administration, integrations beyond what's mentioned |

---

## Recommendations for Next Steps

### 1. **Organize Existing Transcripts**
```
Business Intelligence/2 Input/
  (no transcripts yet)

CRM/2 Input/
  └─ GMT20250917-200141_Recording.transcript.vtt (COPY)

Financial Management/2 Input/
  └─ GMT20250918-211018_Recording.transcript.vtt (MOVE)

Marketing/2 Input/
  └─ GMT20250917-200141_Recording.transcript.vtt (COPY)

Operations/2 Input/
  (no transcripts yet)

Order Management/2 Input/
  (check if there are other sessions)

Pre-Quote/2 Input/
  (no transcripts yet)

System Setup and Configuration/2 Input/
  (no transcripts yet)

0 - Project Kickoff/ (NEW FOLDER)
  └─ GMT20250917-154358_Recording.cc.vtt (MOVE)
```

### 2. **Schedule Additional Discovery Sessions**

**CRITICAL GAPS:**
- **Business Intelligence** - Need dedicated session on reporting, analytics, dashboards
- **Pre-Quote** - Estimating and labor quote processes (note: there are already documents in Creative-Office-Resources/Pre-Quote)
- **Operations** - Operational workflows and processes
- **Order Management** - Complete order processing cycle (may have been partially covered)

**FOLLOW-UP NEEDED:**
- Review any other recorded sessions that may not be in the main folder
- Check if sessions were held for the above areas but not recorded/transcribed
- Confirm Order Management had a full dedicated session

### 3. **Integration Points to Explore**
Based on transcripts, these integration topics need deeper exploration:
- Asana (currently used for task management and marketing project requests)
- Google Drive (document management)
- Expensify or alternative expense management platform
- MailChimp migration to NetSuite email marketing
- Zendesk data migration and CRM setup

### 4. **Document Cross-References**
The Marketing/CRM transcript references:
- Asana workflow for RFP requests
- Zendesk opportunity tracking
- Core data that needs migration

The Financial transcript references:
- Core PO and invoice processes
- Tax Connect (third-party tax software)
- Commission calculation methodologies

These should inform requirements in multiple BRDs.

---

## Action Items

1. **Immediate:**
   - [ ] Copy Transcript 2 to both Marketing and CRM input folders
   - [ ] Move Transcript 3 to Financial Management input folder
   - [ ] Move Transcript 1 to a new "0 - Project Kickoff" folder
   - [ ] Review calendar for any additional discovery sessions that may have been recorded

2. **Short-term:**
   - [ ] Schedule discovery sessions for: Business Intelligence, Pre-Quote, Operations
   - [ ] Confirm Order Management session was fully covered
   - [ ] Review whether System Setup needs additional dedicated time

3. **Documentation:**
   - [ ] Update questionnaires with insights from existing transcripts
   - [ ] Flag integration requirements (Asana, Google Drive, Expensify, etc.) for technical requirements gathering

---

## Notes
- All transcripts are in VTT (WebVTT) format with timestamps
- Transcript 2 and 3 are quite lengthy (60K+ and 44K+ tokens respectively)
- Consider using the AI discovery questionnaire analysis prompts on these transcripts to extract detailed requirements
- The kickoff transcript provides valuable context about GSI's DREAM methodology and overall approach


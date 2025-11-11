# Discovery Session - Specific Questions to Ask
**Comprehensive Single Session - 3.5 Hours**

---

## SECTION 1: DRAFT PURCHASE ORDER WORKFLOW (45 minutes)

### Current State Questions

**To Kipp:**
1. What specific issues are you referring to when you say "POs are a shitstorm of information"?
2. Can you show examples of what makes current POs difficult?
3. What information on a PO is most important to vendors?
4. What information is unnecessary or confusing?

**To Shannon:**
5. How many times are POs revised or corrected after creation?
6. What errors or issues do you see with current POs?
7. Is there any approval process for POs currently, even informal?
8. How often do vendors ask for clarification on current POs?

**To Operations Manager:**
9. How are decisions made about splitting a single SO into multiple POs?
10. Is there any review or draft stage before POs go to vendors currently?
11. What triggers PO creation in your current process?

### Draft PO Workflow Questions

**To Kipp:**
12. What would a "draft PO" concept accomplish that current POs don't?
13. What should be different about a draft PO vs. a final vendor PO?
14. Who should review draft POs before they go to vendors?
15. What should they be checking or approving?

**To Shannon:**
16. Would you want to see draft POs? How would you use them?
17. When should a draft PO become a final vendor PO?
18. What's the trigger for that conversion - who decides and based on what?
19. How should approval routing work? Who approves and in what sequence?

**To Matt:**
20. Should executive approval be required for draft POs, or just operational review?
21. Are there dollar thresholds or special conditions for approval?

**To Operations Manager:**
22. How does the Smart Table grouping (by floor, area, phase) relate to draft PO creation?
23. Do you create one draft from multiple grouped items, or separate drafts?
24. How many draft POs would typically come from a single sales order?

### PO Template Redesign Questions

**To Kipp:**
25. If you were redesigning these POs today, what would the new layout look like?
26. What information should be in the top section? What should be emphasized?
27. What should vendors see first? Second? Third?
28. Are there vendor-requested changes you've heard about?

**To Shannon:**
29. From the operations side, what information do you wish was more clear on POs?
30. Do vendors ever respond to current POs with questions or issues?
31. What would make your PO management job easier?

### Decisions to Make

- **Who approves draft POs?** (Shannon, Kipp, Operations Lead, Matt?)
- **What is the approval criteria?** (Pricing check? Accuracy check? Completeness?)
- **When does draft convert to vendor PO?** (After approval? After date certain?)
- **How are POs transmitted to vendors?** (Email, EDI, portal?)

---

## SECTION 2: CUSTOMER PO TRACKING SOLUTION (45 minutes)

### Bank Reporting Questions

**To Finance Lead:**
1. What specific data does the bank require about customer POs?
2. What does the bank do with this data? (Collateral, compliance, verification?)
3. How often does the bank need this data? (Monthly, quarterly, on-demand?)
4. What format does it need to be in? (Spreadsheet, report format, dashboard access?)
5. Are there regulatory or compliance requirements driving this?

**To Matt:**
6. How is the bank using PO tracking data? What's their concern?
7. Is this a compliance requirement or a lending condition?

### Customer PO Scenarios Questions

**To Finance Lead:**
8. Walk me through your typical customer PO scenarios:
   - How often do you get a single PO per project?
   - How often do you get multiple POs per project?
   - How often do you get blanket POs?
   - How often do customers issue change orders or amendments to POs?

9. When you have multiple POs on one project, do they need to be aggregated for tracking? How?
10. For blanket POs, how do you know the remaining balance? Manual tracking?
11. When a change order arrives, how do you handle it? New PO value or amendment?
12. Do you ever have scenarios where orders aren't covered by a customer PO?

**To Shannon:**
13. Of these scenarios, which do you encounter most frequently?
14. Which scenarios cause the most problems or delays?
15. What happens when someone exceeds a PO limit? How do you find out?

### Solution Design Questions

**To Finance Lead (the decision maker):**
16. Should we track customer POs in a separate system entity, or attach to existing orders?
17. Who will enter the customer PO information? (Finance, Order entry, Project coordinators?)
18. How often does this information need to be entered or updated? (Once per project? As orders are created?)
19. Should the customer PO value update automatically as invoices are created, or manual?

**To Shannon:**
20. From your perspective, how would you want to interact with customer PO tracking?
21. Would you look up PO info during order entry? During invoicing? Both?

**To IT Lead:**
22. Can we pull invoice amounts automatically into a tracking system, or would this be manual?

### Dashboard & Alert Questions

**To Finance Lead:**
23. What dashboard do you need to see?
    - Total PO value?
    - Amount billed to date?
    - Remaining balance?
    - Percent utilized?
    - Per-PO or project-level view?

**To Shannon:**
24. When should alerts trigger for exceeding PO limits?
    - At 75% utilized? 80%? 90%?
    - Or should each customer have different thresholds?

25. Who should get the alerts?
    - Finance? Orders team? Both?
    - What should they do when they get the alert?

**To Matt:**
26. What's the benefit to KBM Hoag of having customer PO visibility?
27. Is this a competitive advantage in how you communicate with customers?

### Decisions to Make

- **Storage approach**: Custom record vs. custom transaction vs. hybrid?
- **Data entry process**: Who enters, when, how often?
- **Dashboard view**: Per-PO or project-level?
- **Alert thresholds**: What % triggers warnings?
- **Auto-calculation**: Manual or automatic remaining balance?

---

## SECTION 3: E-PORTALS & COUPA INTEGRATION (35 minutes)

### E-Portals Overview Questions

**To Shannon:**
1. When you mention "e-portals," what are you referring to specifically?
2. Are you using Coupa portal? Any other portals? (Miller Knoll portal? Others?)
3. What processes currently go through these portals? (Order entry? Invoice transmission? Reporting?)

**To IT Lead:**
4. What portals do we currently have access to?
5. Are there existing integrations with our systems, or is everything manual?

### Coupa Email Process Questions

**To Shannon (detailed walkthrough):**
6. Walk me through the Coupa process step-by-step:
   - How do emails arrive?
   - What data is in the email?
   - What do you do with the email?
   - How does an order get created?
   - How does the invoice go back?

7. How many Coupa orders do you process per month?
8. How long does each one take you? (Start to finish)
9. Do all Coupa emails have the same format, or are there variations?
10. When there's a variation, what do you do?
11. Have you ever had problems with Coupa email format changes?
12. Are there any orders you can't process through email? If so, what do you do?

### Coupa Automation Decision Questions

**To Shannon:**
13. If this could be automated, how much time would you save?
    - Time per order: ___ minutes
    - Orders per month: ___
    - Total time saved: ___ hours/month

14. What would you do with that time if it were freed up?
15. Are there errors or problems with the manual process that automation would solve?

**To IT Lead:**
16. Can email parsing reliably extract the right data from Coupa emails?
17. What would be the implementation effort?
18. What's the maintenance burden once it's set up?
19. What could go wrong? (Email format changes, data anomalies, etc.)
20. How reliable would this be? What's the error rate estimate?

**To Matt (financial/strategic):**
21. Is this worth the investment in your view?
22. Does reducing Shannon's workload free her up for higher-value work?
23. What's the ROI threshold you'd need to see?

### Other E-Portal/Integration Questions

**To Shannon:**
24. Besides Coupa, are there other portals or integration needs we should discuss?

**To IT Lead:**
25. What's the status of Miller Knoll ServiceNet integration?
26. What's the status of ServiceTime integration?
27. Are there any other manufacturer integrations we need to plan for?

### Decisions to Make

- **Coupa automation**: Automate now? Manual process? Future phase?
- **Implementation approach**: Email parsing, API, other?
- **Timeline**: When should this be implemented?
- **Maintenance responsibility**: Who owns ongoing maintenance?

---

## SECTION 4: QUICK-GAP CLOSURE (30 minutes)

### Order Types Question

**To Matt/Shannon/Kipp:**
1. We've identified these order types:
   - Direct Bill (~$1M/yr, 1%)
   - Intermarket Inbound (~40/yr)
   - Intermarket Outbound (thousands/yr)
   - Intuit Work from Home
   - Government (20% of business)
   
   Is this complete? Are there any other order types we should track?

2. Are the volume estimates accurate?

### Quote Versioning Questions

**To Shannon/Sales:**
3. When a customer requests changes to a quote:
   - Do you create a new quote/proposal, or modify the existing one?
   - How do you track which version is current?
   - How do you make sure everyone is looking at the latest version?

4. How often do you have to issue revised quotes?

### Deposit Management Questions

**To Finance Lead:**
5. What's the standard deposit percentage or amount you require?
6. When/how is the deposit applied to the final invoice?
7. Do you ever handle proforma invoices? When and how?
8. Do you have milestone-based payment scenarios? How do they work?
9. Are there customers with different deposit terms?

### Sales Order Form Fields Questions

**To Operations/Shannon:**
10. When you create a sales order (moving from proposal), what additional fields do you need that weren't on the proposal?
11. Specifically, what date fields do you capture at SO stage?
12. Are any of these required, or all optional?
13. Are there other fields beyond dates? If so, what?

### Customer Hierarchy Questions

**To Finance/Sales:**
14. Do you have customers with parent-child relationships? (Parent company with multiple subsidiaries?)
15. Do you need consolidated billing across multiple customer entities?
16. Do government entities need to be grouped under agencies?

### Completeness Confirmation

**To All:**
17. Are we missing anything? Any critical questions we haven't covered?
18. Are all your gaps answered at 85%+ confidence?

---

## DECISION TRACKER

Use this during the session to document all decisions:

### Section 1: Draft PO
- [ ] Draft PO approval authority: ________________
- [ ] Approval criteria: ________________
- [ ] Draft → Vendor PO conversion decision: ________________
- [ ] Transmission method: ________________
- [ ] PO template redesign specifics: ________________

### Section 2: Customer PO Tracking
- [ ] Storage approach (record/transaction/hybrid): ________________
- [ ] Data entry process: ________________
- [ ] Dashboard KPIs: ________________
- [ ] Alert thresholds: ________________
- [ ] Bank reporting format: ________________
- [ ] Auto vs. manual calculations: ________________

### Section 3: E-Portals & Coupa
- [ ] Coupa automation decision: ________________
- [ ] Implementation approach: ________________
- [ ] Timeline: ________________
- [ ] ServiceNet status: ________________
- [ ] ServiceTime status: ________________
- [ ] Other portal needs: ________________

### Section 4: Gap Closure
- [ ] Order types validated: ________________
- [ ] Quote versioning process: ________________
- [ ] Deposit policies: ________________
- [ ] SO form fields: ________________
- [ ] Customer hierarchy needs: ________________

---

## REQUIRED PARTICIPANTS & THEIR EXPERTISE

| Person | Sections | Expertise |
|--------|----------|-----------|
| **Kipp** | 1, 4 | PO design, operations, templates |
| **Shannon** | 1, 2, 3, 4 | Processing, workflows, volume data, pain points |
| **Matt** | 1, 2 | Approvals, strategy, financial decisions |
| **Finance Lead** | 2, 4 | Customer POs, bank requirements, deposits, hierarchy |
| **Marcus** | All | Facilitate, document, capture decisions |
| **Operations Manager** | 1 | PO splitting, smart table grouping |
| **IT Lead** | 3, 4 | Integration feasibility, technical specs |

---

## TIMING

- Section 1 (Draft PO): 45 min → ~25 questions
- Section 2 (Customer PO Tracking): 45 min → ~27 questions
- Break: 15 min
- Section 3 (E-Portals): 35 min → ~26 questions
- Section 4 (Quick Gaps): 30 min → ~17 questions
- Wrap-up: 10 min
- **Total: 3.5 hours**

---

## HOW TO USE THIS

1. **Print or display this document** during the session
2. **Go through each section** in order
3. **Ask the specific questions** - write down answers
4. **Use decision tracker** to capture decisions
5. **After each section**, confirm: "Are we at 85%+ confidence on this?"
6. **At end**, confirm: "Have we closed all gaps?"

**Result**: Questionnaire v1.2 at 100% complete with all decisions documented.


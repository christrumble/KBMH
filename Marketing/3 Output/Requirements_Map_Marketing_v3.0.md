# Requirements Map - Marketing
**Version**: 3.0  
**Date**: 2025-10-15  
**Process Area**: Marketing (Campaigns, Events, Content, Market Intelligence)

## Change Log
- **Date**: 2025-10-15
- **Version**: 3.0
- **Sources**: Marketing/2 Input/Master_Transcript_Marketing.md; Marketing/2 Input/MRK & CRM Outline & Questionnaire
- **Summary**: Complete requirements mapping from Master_Transcript_Marketing.md. Focused on Marketing-specific requirements (separate from CRM). All 25 marketing requirements classified with evidence traceability.

## Implementation Approach Classifications

**ALIGNS**: The way the dealer is executing a business process in their current business system aligns with how they will do it in Orion. It might not be an exact one-to-one alignment, but it doesn't require any customizations for them to do what they are currently doing now in Orion.

**ADAPT**: They do need to modify their business process to use Orion. Adaptation is on a spectrum so it could be major or minor - but still no customization required.

**ACCOMMODATE**: WE will accommodate their business process by customization, personalization, new configuration - something we need to do to accommodate their needs.

**FUTURE**: Functionality to be evaluated or implemented in a future phase, not Phase 1.

## Requirements Map

| ID | Requirement | Type (F/NF) | Functionality | Decision | SolutionDesign? | Approach | Risks |
|----|-------------|-------------|--------------|----------|-----------------|----------|-------|
| REQ-M001 | Continue relationship-based, targeted marketing approach | NF | Business Process | System must support targeted segmentation vs. mass campaigns; personal email sending | No | ALIGNS | Over-building campaign automation that won't be used |
| REQ-M002 | Minimal email marketing implementation in Phase 1 | NF | NetSuite Email Marketing | Low volume (<6/year); 120K/month capacity available but underutilized | No | ALIGNS | Under-investment if needs grow; over-investment if unused |
| REQ-M003 | Support marketing as RFP coordination function | F | Workflow/Process Design | Marketing team receives RFP requests, coordinates response, not demand generation | Yes | ADAPT | Requires workflow routing; different from typical marketing setup |
| REQ-M004 | Multi-dimensional contact segmentation (role, sector, geography) | F | CRM Custom Fields + Saved Searches | Enable targeting by role AND sector AND territory combinations | Yes | ACCOMMODATE | Complex taxonomy definition; data quality dependency; user adoption |
| REQ-M005 | Data quality controls and validation rules | NF | Data Validation + Required Fields | Required fields for segmentation; validation rules; prevent "poo in, poo out" | Yes | ACCOMMODATE | User resistance to required fields; data entry burden |
| REQ-M006 | Custom contact role definitions including influencer types | F | Custom Contact Roles | Define: GC, broker, A&D, PM, CM, Decision Maker, Finance, Procurement, Facilities, etc. | Yes | ACCOMMODATE | Taxonomy workshop needed; training required; governance |
| REQ-M007 | Market sector/vertical classifications | F | Custom Industry/Sector Field | Healthcare, Tech, Corporate, Government, Education, Financial, Legal, Creative, Hospitality | Yes | ACCOMMODATE | Sector definition workshop; single vs. multi-select; maintenance |
| REQ-M008 | Territory-based segmentation (SF, San Jose, Sacramento) | F | Territory Fields + Assignment Rules | Track and segment by GM territory; market-specific messaging | No | ADAPT | Territory reassignment process; account ownership conflicts |
| REQ-M009 | Transactional vs. marketing email with subscription management | F | Email Subscription Status | Automatic opt-in/out tracking; transactional emails bypass opt-in | No | ALIGNS | Compliance risk if misused; user education on transactional vs. marketing |
| REQ-M010 | Quarterly targeted communications to specific segments | F | Campaign Management + Saved Searches | Curated lists (brokers, PM firms); market rate updates; value-add content | No | ADAPT | List maintenance governance; content creation burden; quarterly discipline |
| REQ-M011 | Personalized email sending from individual user accounts | F | Email Integration | Send from user email (not info@) for personal touch; activity tracking | No | ALIGNS | Deliverability if too many senders; user email reputation risk |
| REQ-M012 | Replace MailChimp with NetSuite | F | NetSuite Email Marketing | Consolidate to NetSuite; eliminate manual Excel uploads and bounces | No | ADAPT | Template migration; user training on new interface; feature parity gaps |
| REQ-M013 | Minimal event tracking for Phase 1 | F | Campaign Events (Optional) | Basic event capability available; continue Google Forms; evaluate post-launch | No | ALIGNS | Low adoption if too complex; May never be used; wasted configuration |
| REQ-M014 | Evaluate event management post-go-live | F | Campaign Events | ROI tracking, RSVP, attendance; evaluate 3-6 months post-launch if value identified | No | FUTURE | May remain unused; resource investment vs. value uncertain |
| REQ-M015 | Marketing early visibility into RFP opportunities | F | Custom CRM Permissions + Views | Marketing team sees pipeline without full CRM access; early RFP identification | Yes | ACCOMMODATE | Permission complexity; data security; custom views/dashboards required |
| REQ-M016 | Track projected vs. actual RFP volume by submitter | F | Custom Opportunity Fields + Reports | Volume forecasting; accuracy tracking; resource planning; identify overestimators | Yes | ACCOMMODATE | Custom fields; reporting logic; Philippines team time integration |
| REQ-M017 | RFP workflow routing to marketing team | F | Workflow Automation + Request Engine | Replace Asana; assign to Marketing PM; document attachment; collaboration | Yes | ACCOMMODATE | Workflow design; form design; project tracking integration; training |
| REQ-M018 | Document attachment to opportunities/quotes | F | File Attachment + Google Drive Integration | RFP docs, responses, materials; link Google Drive folders; version control | No | ALIGNS | Storage limits if not using Google Drive integration; 100GB NetSuite limit |
| REQ-M019 | Marketing visibility into pipeline trends by sector | F | Custom Dashboard + Saved Searches | Marketing team views sector trends without full pipeline access | Yes | ACCOMMODATE | Dashboard design; permission configuration; access controls |
| REQ-M020 | Market intelligence dashboard for content planning | F | Custom Dashboard + Analytics | Sector trends, RFP volume, win/loss by sector, pipeline by stage and sector | Yes | ACCOMMODATE | Complex dashboard requirements; multiple views; drill-down capability |
| REQ-M021 | Sector performance analysis for strategic planning | F | Custom Reports + Analytics | Identify trending sectors; inform content strategy; resource forecasting | Yes | ACCOMMODATE | Reporting design; KPI definitions; trend analysis logic |
| REQ-M022 | Customer satisfaction surveys post-project | F | Survey Campaigns | Post-delivery feedback; NPS; trend analysis; action items | No | FUTURE | Phase 1 low priority; evaluate 6+ months post-launch with Customer Service |
| REQ-M023 | Survey functionality within NetSuite campaigns | F | Campaign Surveys | Create surveys, track responses, results on records, trend analysis | No | FUTURE | Dependent on REQ-M022 decision; native capability available |
| REQ-M024 | Web form lead capture with automatic creation | F | Web-to-Lead Forms | Contact form → NetSuite lead; auto-routing; integration with website | No | ALIGNS | Form spam risk; routing logic; low lead quality expected (mostly deletions) |
| REQ-M025 | Google Drive integration for file management | F | Google Drive Connector | Files represented in NetSuite but stored in Drive; avoid 100GB NetSuite limit | Yes | ACCOMMODATE | Integration configuration; dual storage strategy; link management; governance |

## Totals by Approach
- **ALIGNS**: 8 requirements (32%)
- **ADAPT**: 5 requirements (20%)
- **ACCOMMODATE**: 10 requirements (40%)
- **FUTURE**: 2 requirements (8%)

**Total**: 25 Marketing-specific requirements

## Customization Summary

**Solution Design Required (SolutionDesign? = Yes): 12 requirements**

### High Complexity Customizations:
1. **Multi-dimensional segmentation system** (REQ-M004, M005, M006, M007, M008) - Custom fields, taxonomy, validation rules, governance
2. **Marketing intelligence dashboard suite** (REQ-M019, M020, M021) - Custom dashboards, permissions, analytics
3. **RFP workflow and volume tracking** (REQ-M016, M017) - Custom workflow, fields, reporting
4. **Marketing team restricted pipeline visibility** (REQ-M015) - Complex permission matrix

### Medium Complexity Customizations:
5. **Google Drive integration** (REQ-M025) - Connector configuration, governance
6. **RFP request engine** (REQ-M017) - Form design, workflow routing

## Critical Dependencies

**Blocking Configuration Phase:**
1. Contact role taxonomy definition (REQ-M006) → Blocks segmentation implementation
2. Sector/vertical classification list (REQ-M007) → Blocks industry field configuration
3. Territory assignment rules (REQ-M008) → Blocks geographic segmentation

**Blocking Go-Live:**
4. Data quality validation rules (REQ-M005) → Required for clean segmentation
5. Marketing pipeline visibility permissions (REQ-M015) → Security/access configuration
6. RFP workflow design (REQ-M017) → Replaces critical Asana process

**Post-Go-Live Evaluation:**
7. Event management adoption (REQ-M013, M014) → Evaluate 3-6 months post-launch
8. Customer satisfaction surveys (REQ-M022, M023) → Evaluate with Customer Service team

## Risk Analysis

### High Risk Requirements:
- **REQ-M004, M005, M006, M007**: Segmentation depends entirely on data quality and user adoption. If users don't classify contacts properly, entire segmentation strategy fails.
- **REQ-M015**: Marketing visibility into sales pipeline creates potential for internal competition/conflict. Careful permission design needed.
- **REQ-M020, M021**: Market intelligence dashboards require consistent opportunity data entry by sales team. Garbage in = garbage out.

### Medium Risk Requirements:
- **REQ-M002, M012**: Email marketing may be over-invested given minimal usage (<6/year). Could defer more setup to post-launch.
- **REQ-M016, M017**: RFP workflow replaces critical Asana process. Must be fully functional at go-live or maintain Asana parallel.
- **REQ-M003**: Marketing-as-RFP-coordination is non-traditional. Off-the-shelf training won't apply; custom training needed.

### Low Risk Requirements:
- **REQ-M013, M014**: Event management is explicitly low priority and deferrable. No risk if not implemented.
- **REQ-M024**: Web form integration standard functionality. Low lead quality expected but not system risk.

## Data Migration Considerations

**From MailChimp:**
- Email templates (if desired) - Low priority per team
- Historical campaign performance (optional)
- Subscription/opt-out status (if tracked) - Currently manual

**From Core/Zendesk:**
- Contact records (clean and classify during migration - CRITICAL)
- Basic segmentation data (if exists)
- Historical email preferences (if tracked)

**Data Cleansing Requirements (CRITICAL):**
Based on "poo in, poo out" comments, data migration must include:
1. Contact role classification project - Manual review and classification
2. Sector/industry assignment - Research and assign to all contacts
3. Territory assignment - Assign to appropriate GM territory
4. Duplicate detection and merge - Clean database before go-live
5. Opt-in status research - Determine subscription status for marketing contacts

**Estimated Effort**: Data classification could be significant manual effort depending on contact volume.

## Integration Requirements

**External Systems:**
1. **Website contact form** → NetSuite (web-to-lead) - Standard integration
2. **Google Drive** → NetSuite - Requires connector configuration (REQ-M025)
3. **Outlook/Gmail** → NetSuite - Email integration for activity tracking
4. **Philippines team time tracking system** → NetSuite (mentioned for RFP volume tracking)

**Internal NetSuite Integration:**
- Marketing module → CRM (opportunity visibility with restrictions)
- Marketing module → Project Management (RFP workflow)
- Marketing module → Reporting/Analytics (dashboards)

## Training Requirements

**Marketing Team:**
- Contact segmentation and list creation (CRITICAL)
- Email campaign creation (light training - minimal usage)
- RFP workflow and volume tracking (replaces Asana)
- Market intelligence dashboard usage
- Event management (if implemented)
- Survey creation (future phase)

**Sales/BD Team (Marketing Impact):**
- Early opportunity creation for marketing visibility
- Contact role classification (critical for segmentation)
- Sector assignment (critical for trend tracking)
- Data quality standards

**Admin (Jenny):**
- Lead qualification and routing
- Web form lead management
- Contact database maintenance and segmentation
- Duplicate detection and merge
- Data quality monitoring

## Success Metrics

**Phase 1 Success Criteria:**
1. **Data Quality**: >90% of contacts properly classified by role and sector
2. **Segmentation Usage**: Marketing team creates at least 3 saved searches/segments
3. **RFP Workflow**: 100% of RFPs routed through NetSuite (Asana retired)
4. **Market Intelligence**: Marketing team actively uses sector trend dashboard weekly
5. **Email Consolidation**: MailChimp retired; all campaigns through NetSuite

**6-Month Post-Launch Success Criteria:**
6. **Targeted Communications**: At least quarterly communications to segmented lists
7. **Volume Tracking**: Projected vs. actual volume tracked on all RFPs
8. **ROI Visibility**: Marketing team reports proactive content creation based on sector trends
9. **User Adoption**: Sales team consistently classifies contacts (>85% compliance)

**12-Month Evaluation Criteria:**
10. **Event Management**: Decision on event tracking adoption based on ROI
11. **Survey Implementation**: Decision on customer satisfaction survey deployment
12. **Campaign Frequency**: Increase from <6/year to quarterly targeted campaigns

## Notes and Recommendations

### Critical Success Factors:
1. **Data quality is foundation** - Without clean, classified contact data, segmentation and market intelligence fail
2. **Taxonomy workshop is blocking** - Cannot configure until roles and sectors defined
3. **Change management focus** - Sales team must adopt contact classification discipline
4. **Marketing team training** - Non-traditional marketing role requires custom training approach
5. **Realistic expectations** - Don't over-invest in email marketing given minimal usage

### Implementation Recommendations:
1. **Phase 1 Focus**: Segmentation foundation, RFP workflow, market intelligence dashboards
2. **Phase 1 Defer**: Event management, surveys, advanced campaign automation
3. **Parallel Run**: Consider Asana parallel for 2-4 weeks during RFP workflow transition
4. **Data Migration**: Budget significant time for contact classification project
5. **Permission Design**: Careful design of marketing pipeline visibility to avoid sales conflict

### Traceability:
- All requirements link back to Master_Transcript_Marketing.md
- Evidence quotes available in Questionnaire_Marketing_v3.0.md
- Implementation approach classifications follow standard definitions
- SolutionDesign flag identifies customization requirements

---

*End of Requirements Map v3.0*





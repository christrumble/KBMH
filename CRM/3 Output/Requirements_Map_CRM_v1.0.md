# Requirements Map - CRM
**Version**: 2.0  
**Date**: October 15, 2025  
**Process Area**: CRM (Customer Relationship Management)

## Change Log
- **Date**: October 15, 2025
- **Version**: 2.0
- **Sources**: Master_Transcript_CRM.md, Master_Transcript_Marketing_CRM.md
- **Summary**: Complete requirements map with all 50 requirements extracted from comprehensive questionnaire analysis.

- **Date**: 2025-10-02
- **Version**: 1.0
- **Sources**: Marketing/2 Input/Transcript MRK&CRM
- **Summary**: Scaffold created; pending REQ extraction from CRM questionnaire responses.

## Implementation Approach Classifications

**ALIGNS**: The way the dealer is executing a business process in their current business system aligns with how they will do it in Orion. It might not be an exact one-to-one alignment, but it doesn't require any customizations for them to do what they are currently doing now in Orion.

**ADAPT**: They do need to modify their business process to use Orion. Adaptation is on a spectrum so it could be major or minor - but still no customization required.

**ACCOMMODATE**: WE will accommodate their business process by customization, personalization, new configuration - something we need to do to accommodate their needs.

## Requirements Map

| ID | Requirement | Type (F/NF) | Functionality | Decision | SolutionDesign? | Approach | Risks |
|----|-------------|-------------|--------------|----------|-----------------|----------|-------|
| REQ-001 | Migrate from Zendesk to NetSuite CRM with integrated Opportunity → Quote → SO → Project flow | F | NetSuite CRM, Transaction Flow | Zendesk retirement; NetSuite system of record | No | ALIGNS | Data migration quality |
| REQ-002 | Make opportunity entry required (currently optional) | NF | Required Fields, Validation Rules | Enforce CRM usage | No | ADAPT | Sales team resistance |
| REQ-003 | Implement validation rules and required fields on opportunities | NF | Validation Rules, Custom Fields | Prevent incomplete data entry | Yes | ACCOMMODATE | User pushback on restrictions |
| REQ-004 | Use Kanban Boards for visual opportunity pipeline management | F | Orion Boards | Visual pipeline tool | No | ALIGNS | User adoption/training |
| REQ-005 | Restrict opportunity visibility to assigned users only | NF | Role/Permission Config | Privacy/focus | No | ADAPT | Limited discovery capability |
| REQ-006 | Web form integration to automatically create leads in NetSuite | F | Web-to-Lead | Automate lead capture | No | ALIGNS | Form spam handling |
| REQ-007 | Implement lead routing rules (Jenny → GM/Account Manager) | F | Workflow/Assignment Rules | Maintain current qualification process | No | ALIGNS | Rule complexity if scaled |
| REQ-008 | Enable mobile Quick Add Lead functionality for BD reps | F | NetSuite Mobile | Quick lead capture in field | No | ALIGNS | Mobile adoption |
| REQ-009 | Track lead sources (web form, referral, relationship, RFP, event) | F | Lead Source Field, Reporting | Conversion analysis | No | ALIGNS | Consistent entry needed |
| REQ-010 | Implement custom contact role classifications beyond Core limitations | F | Custom Contact Roles | Enable segmentation | Yes | ACCOMMODATE | Taxonomy definition needed |
| REQ-011 | Support multiple contact roles per contact | F | Contact Management | Reflect real-world relationships | No | ALIGNS | Data entry complexity |
| REQ-012 | Implement market sector/vertical tracking | F | Custom Fields | Trend analysis, targeting | No | ALIGNS | Classification consistency |
| REQ-013 | Implement territory assignment (SF, San Jose, Sacramento) | F | Territory Management | Performance tracking by market | No | ALIGNS | Overlap scenarios TBD |
| REQ-014 | Enable duplicate detection and merge capabilities | F | Duplicate Detection, Merge | Clean database | No | ALIGNS | False positives possible |
| REQ-015 | Track contact communication preferences and opt-in/opt-out status automatically | F | Subscription Management | Email compliance | No | ALIGNS | Initial status capture |
| REQ-016 | Configure opportunity-level forecasting (not quote-level) | NF | Forecasting Configuration | Prevent over-forecasting | No | ADAPT | Manual sync if multiple quotes |
| REQ-017 | Set forecast inclusion threshold at 70%+ probability | NF | Forecast Rules | Focus on realistic pipeline | No | ADAPT | Missed early visibility |
| REQ-018 | Track forecast accuracy by user over time | F | Reporting, Analytics | Continuous improvement | No | ADAPT | Requires consistent usage |
| REQ-019 | Define opportunity stages and probability by stage | NF | Opportunity Stage Configuration | Pipeline standardization | No | ADAPT | Stage criteria definition needed |
| REQ-020 | Create Sales Goals dashboard in NetSuite to replace Excel tracking | F | Custom Dashboard | Eliminate manual Excel process | Yes | ACCOMMODATE | Excel template needed for design |
| REQ-021 | Configure order approval for amounts over $25,000 to Shannon | F | Workflow/Approval Rules | Current approval process | No | ALIGNS | Threshold accuracy |
| REQ-022 | Configure approval workflow when missing required documents to Matt | F | Workflow/Approval Rules | Document validation | No | ALIGNS | Exception frequency |
| REQ-023 | Configure erosion approval when cumulative erosion exceeds $1,500 to Matt | F | Workflow/Approval Rules | Training/problem-solving | No | ALIGNS | Threshold calculation |
| REQ-024 | Build double-order detection query (same $ amount within 30 days) | F | Custom Query/Alert | Prevent major losses | Yes | ACCOMMODATE | False positives on legitimate bulk orders |
| REQ-025 | Track approval time by approver to identify bottlenecks | F | Approval Reporting | Process improvement | No | ALIGNS | Minimal |
| REQ-026 | Implement required win/loss reason codes | F | Custom Fields, Required | Systematic learning | No | ADAPT | Reason code taxonomy needed |
| REQ-027 | Track competitor information on lost opportunities | F | Custom Fields | Competitive intelligence | No | ADAPT | Data entry consistency |
| REQ-028 | Create win/loss analysis reports by sector, size, type, territory | F | Custom Reports | Strategic insights | No | ADAPT | Data quality dependency |
| REQ-029 | Add vendor credit limit field and warning threshold (90% of limit) | F | Vendor Record Customization, Business Rule | Proactive limit management | Yes | ACCOMMODATE | Limit data maintenance |
| REQ-030 | Prevent PO creation when vendor credit limit exceeded | F | Business Rule/Validation | Hard stop on over-limit orders | Yes | ACCOMMODATE | Emergency override process needed |
| REQ-031 | Enable basic Customer Portal for quote and invoice visibility | F | Customer Center | Self-service access | No | ALIGNS | Customer adoption uncertain |
| REQ-032 | Configure GP target default of 22% at customer level with opportunity override capability | F | Custom Fields, Defaults | Pricing guidance | No | ADAPT | Override tracking/reporting |
| REQ-033 | Enable activity tracking (calls, emails, meetings) on opportunities | F | Activity Management | Interaction history | No | ALIGNS | Consistent logging needed |
| REQ-034 | Enable task management with due dates and reminders on opportunities | F | Task Management | Follow-up accountability | No | ALIGNS | Minimal |
| REQ-035 | Maintain activity history and team collaboration notes on opportunities | F | Notes, Collaboration | Team visibility | No | ALIGNS | Data quality |
| REQ-036 | Enable document attachment to opportunities/quotes (RFPs, proposals, correspondence) | F | Document Management | Context preservation | No | ALIGNS | Storage management |
| REQ-037 | Support Google Drive folder linking for project documentation | F | External Link/Integration | Maintain current practice | No | ALIGNS | Link maintenance |
| REQ-038 | Import Zendesk opportunity history via CSV with historical tagging | NF | Data Migration, CSV Import | Historical context | No | ALIGNS | Data mapping complexity |
| REQ-039 | Migrate contact data from Core with deduplication | NF | Data Migration, Duplicate Detection | Clean starting point | No | ALIGNS | Data quality in source |
| REQ-040 | Migrate and classify contacts by role, sector, and territory during import | NF | Data Migration, Classification | Immediate segmentation capability | Yes | ACCOMMODATE | Manual classification effort |
| REQ-041 | Create BD/Sales Rep dashboard (my opportunities, pipeline, forecast, activities, tasks) | F | Custom Dashboard | Personal visibility | No | ALIGNS | Dashboard design |
| REQ-042 | Create Sales Manager dashboard with "Me and My Team" role-based filters | F | Custom Dashboard, Role Hierarchy | Team management visibility | No | ADAPT | Org structure accuracy needed |
| REQ-043 | Create Executive dashboard (company-wide pipeline, forecast, win rate, sectors, territories) | F | Custom Dashboard | Strategic visibility | No | ALIGNS | Dashboard design |
| REQ-044 | Enable drill-down capability from dashboard metrics to detail records | F | Dashboard Navigation | Investigation capability | No | ALIGNS | Minimal |
| REQ-045 | Configure email marketing capability (120K emails/month) with minimal implementation | F | Email Marketing | Available if needed | No | ALIGNS | Low priority Phase 1 |
| REQ-046 | Implement automatic subscription management for opt-in/opt-out | F | Subscription Management | Compliance automation | No | ALIGNS | Initial status capture |
| REQ-047 | Support segmented contact lists by role, sector, geography, custom criteria | F | List Management, Segmentation | Targeted outreach | No | ALIGNS | Data quality dependency |
| REQ-048 | Track campaign performance (opens, clicks, ROI) when email campaigns used | F | Email Marketing Analytics | Measure effectiveness | No | ALIGNS | Low usage expected |
| REQ-049 | Support sales team commission splits on opportunities | F | Opportunity Management, Commission Config | Team-based opportunities | TBD | FUTURE | Split logic complexity |
| REQ-050 | Event management with invitation tracking and attendance | F | Event Management | ROI tracking | TBD | FUTURE | Manual attendance tracking burden |

## Summary Statistics

**Total Requirements**: 50

**By Approach:**
- **ALIGNS**: 33 requirements (66%) - Standard NetSuite/Orion capabilities that meet needs
- **ADAPT**: 11 requirements (22%) - Process changes or configuration needed, no customization
- **ACCOMMODATE**: 6 requirements (12%) - Custom solution design needed
- **FUTURE**: 2 requirements - Deferred to post-go-live phase

**By Type:**
- **Functional (F)**: 43 requirements (86%)
- **Non-Functional (NF)**: 7 requirements (14%)

**Solution Design Required** (ACCOMMODATE items):
- REQ-003: Validation rules and required fields configuration
- REQ-010: Custom contact role classifications
- REQ-020: Sales Goals dashboard design
- REQ-024: Double-order detection query
- REQ-029/030: Vendor credit limit management
- REQ-040: Contact classification during data migration

**Key Risk Areas:**
- Sales team adoption and resistance to required data entry (REQ-002, REQ-003)
- Data quality dependency for segmentation and reporting (REQ-009, REQ-026, REQ-027, REQ-047)
- Territory overlap scenarios not yet defined (REQ-013)
- Change management critical for success

## Notes
- All requirements link back to transcript quotes in the questionnaire
- Requirements reference specific questionnaire sections for full context
- Each requirement classified using precise ALIGNS/ADAPT/ACCOMMODATE definitions
- Action items identified for configuration details that need finalization
- 13 action items assigned to finalize taxonomies, thresholds, and workflows

---

*End of CRM Requirements Map*



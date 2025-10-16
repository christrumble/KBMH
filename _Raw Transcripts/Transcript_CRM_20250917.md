# KBMH Discovery Transcript - CRM & Sales Management

**Original File:** GMT20250917-200141_Recording.transcript.vtt  
**Date:** September 17, 2025 (Evening Session - 8:00 PM start)  
**Duration:** ~2 hours  
**Process Area:** CRM (Primary), Marketing (Secondary)

---

## Session Overview

This session focused on customer relationship management, sales processes, opportunity tracking, and the lead-to-order conversion workflow at KBMH.

## Key Topics Covered

### Current CRM System - Zendesk
- Opportunity tracking and management
- **Optional usage** - Sales team not required to use consistently
- Forecasting tool for account managers
- Lead and opportunity lifecycle management
- Manual data entry with variable detail levels

### Sales Team Structure

#### Business Development Representatives
- Customer-facing relationship builders
- Market presence (wining, dining)
- Engage influencers, brokers, A&D firms, clients
- Lead generation and qualification
- Relationship-driven opportunities

#### Account Managers
- Hybrid role (varies by individual)
- Some focus on lead generation (like BD reps)
- Some focus on project management (sales support)
- Manage all stakeholders after lead conversion
- Incentive/comp tied to skill set and role focus
- Intentionally broad role definition for flexibility

### Lead-to-Order Workflow

#### Lead Sources
1. **Influencer Relationships** (Primary)
   - Brokers
   - Architecture & Design (A&D) firms
   - Project management firms
   - Existing client relationships
2. **RFPs** - Formal requests for proposals
3. **Web Forms** - Online contact (low conversion)
4. **Manufacturers** - Partner referrals

#### Current Process Flow
1. **Lead Creation**
   - Comes through relationship (BD rep or account manager)
   - Rarely comes directly to "KBMH" - usually through a person's network
   - Web form submissions (mostly low-value service requests)

2. **Lead Qualification**
   - BD rep or account manager assesses opportunity
   - Determines if it's new or existing client
   - Evaluates project potential

3. **Opportunity Creation in Zendesk**
   - Sales person **may** create opportunity record (not required)
   - Assign value and probability
   - **Data quality varies significantly** - some detailed, some minimal
   - Account managers supposed to update for forecasting

4. **RFP Stage** (if applicable)
   - Formal RFP request arrives
   - Project request submitted to marketing via Asana
   - Marketing creates RFP response
   - Tracked separately from standard opportunities

5. **Conversion Decision**
   - Opportunity marked "Closed Won" or "Closed Lost"
   - **Closed Won** - Manually moved to Core ERP
   - **Closed Lost** - Dies in Zendesk

### Pain Points & Challenges

#### Data Quality & Consistency
- **Inconsistent usage** - Not all sales people use Zendesk
- **Variable detail** - Amount of information varies by person
- **No enforcement** - System is optional, not required
- **Forecasting issues** - Hard to predict pipeline accurately

#### Manual Processes
- No automatic integration between Zendesk and Core
- Manual data re-entry when opportunity wins
- Opportunity data doesn't flow through to project
- Lost history when moving systems

#### Visibility & Reporting
- Limited real-time pipeline visibility
- Difficult to track team performance
- Can't easily see lead source effectiveness
- RFP tracking separate from opportunity tracking

### Requirements Identified

#### Functional Requirements
1. **Contact & Account Management**
   - Centralized customer database
   - Relationship tracking (brokers, A&D firms, clients)
   - Duplicate detection and management
   - Contact segmentation and categorization

2. **Opportunity Management**
   - Lead-to-opportunity conversion
   - Pipeline tracking and visualization
   - Probability and value forecasting
   - Stage management (qualification → proposal → negotiation → close)
   - Win/loss tracking and analysis

3. **Sales Process Automation**
   - Automatic lead routing based on account ownership
   - Workflow for existing vs new client leads
   - Opportunity-to-order conversion (no re-entry)
   - Integration with project creation

4. **Territory & Assignment**
   - Lead assignment to appropriate GM or account manager
   - Territory management for BD reps
   - Account ownership rules

5. **Activity Tracking**
   - Customer interactions and touchpoints
   - Meeting notes and follow-ups
   - RFP submissions and responses

#### Technical Requirements
1. **Zendesk Migration**
   - Migrate existing opportunity data
   - Preserve historical won/lost records
   - Maintain contact and account relationships
   - Data quality cleanup during migration

2. **Integration with NetSuite**
   - Seamless opportunity-to-quote conversion
   - Quote-to-order workflow
   - Project creation from won opportunities
   - No manual data re-entry

3. **Reporting & Dashboards**
   - Sales pipeline by rep/team
   - Win/loss analysis by source, rep, product
   - Forecast accuracy tracking
   - Lead source effectiveness

4. **Mobile Access**
   - BD reps need field access
   - Activity logging from mobile
   - Quick opportunity updates

### NetSuite CRM Capabilities to Leverage
- Built-in opportunity management
- Quote-to-order automation
- Customer 360-degree view
- Sales forecasting and pipeline
- Territory management
- Activity tracking and calendaring
- Mobile app access
- Customizable sales stages
- Workflow automation for approvals
- Integration with project management (Orion)

### Integration Touchpoints

#### With Marketing (see Marketing transcript)
- Lead handoff from marketing to sales
- RFP opportunity tracking
- Marketing campaign response tracking
- Lead source attribution

#### With Order Management
- Quote creation from opportunity
- Proposal generation
- Order creation upon close
- Project kickoff workflow

#### With Financial Management
- Revenue forecasting
- Commission calculations
- Customer credit management
- Payment terms and history

---

## Specific KBMH Process Considerations

### Relationship-Driven Sales
- Most opportunities come through personal relationships
- BD reps "own" their influencer relationships
- Account managers manage client relationships
- System needs to support relationship mapping

### RFP Process Complexity
- RFPs are a major sales channel
- Marketing heavily involved in RFP response
- Need to track RFP opportunities separately
- Volume and resource allocation critical

### Flexible Sales Roles
- Intentionally broad account manager role
- Some AMs act like BD reps
- System should support role flexibility
- Permissions and workflows need customization

---

## Cross-References to Other Process Areas

### Marketing (40% overlap with this session)
- See `Transcript_Marketing_20250917.md` for lead generation and RFP process
- Marketing project requests via Asana
- Email campaigns and lead nurture

### Pre-Quote
- Opportunity to quote conversion
- Estimating process
- Labor and product quoting

### Order Management  
- Quote to order conversion
- Project creation
- Sales order processing

---

## Source File Location
Original VTT file: `GMT20250917-200141_Recording.transcript.vtt`

**Note:** This transcript shares content with Marketing transcript. See `Transcript_Marketing_20250917.md` for marketing-specific details from the same session.

**Next Steps:**
1. Define CRM data migration strategy from Zendesk
2. Configure NetSuite opportunity stages to match KBMH process
3. Establish lead assignment and routing rules
4. Design sales dashboards and forecasting reports
5. Determine BD rep vs Account Manager permissions and roles


# Master Transcript - Pre-Quote (Labor & Design Requests)

**Source**: Pre-Quote Transcript.txt (Creative Office Resources)  
**Date**: Session documented pre-2025  
**Participants**: Marcus Dallacqua (Consultant), Chris Trumble (Implementation), Gary Strickland (Consultant)  
**Process Area**: Pre-Quote (Labor Quote Requests, Design Requests, Estimating, Project Requests)

**Companion Documents**:
- Labor Quote - Internal, LTS and Subs W GS NOTES 03.13.25.docx
- Labor Quote - Internal, LTS and Subs.docx
- Project Request Review– Interior Construction Estimating.docx

---

## Overview

This transcript documents a walkthrough session where the implementation team reviewed Creative Office Resources' (COR) pre-quote processes, focusing on:
- Labor quote requests (internal, long-term storage, subcontractors)
- Estimating workflows
- Project request management
- Union requirements
- Vendor management
- CAM reservation system integration

## Key Topics & Excerpts

### 1. Labor Quote Request Types

**LTS Definition**:
> **Chris Trumble**: "Oh, LTS is long term storage."

**Request Types in Bridge**:
> **Marcus Dallacqua**: "The quoting team toggles between quoting and intermarket quote requests. Okay. So they have different quote request types. So labor quote request types. Which is fine. We support that. That maps over to our request engine that can. Can create different types of labor quotes. Internal, external, intermarket, in. In. That's fine."

> **Chris Trumble**: "So on our labor requests, is there types in the labor request type or do they need two different request types, one for this kind of quote and one for this kind of quote?"

> **Marcus Dallacqua**: "Yeah, it's two different request types. So you would create a request type specific for labor quote internal, another one for labor quote external, another one for labor quote internal, intermarket, something like that. Yep. But they're all pretty easy to make."

**Bridge vs Orion Request Engine**:
> **Marcus Dallacqua**: "Yeah, I did notice that. So they're using Bridge for this, which, you know, again we have. We're in good shape because Bridge is very similar to Connect, which Joe built. And then Joe brought a lot of that functionality into Orion. So in fact, I think our request engine is going to better than what they have in Bridge."

> **Chris Trumble**: "There hasn't been a lot of scrutiny on the request engine, but I think it's pretty basic. Right. It's a custom record in NetSuite. It's not like Joe's specific architecture."

> **Marcus Dallacqua**: "It is. It's a suite... It's a suitelet that loads jQuery. Okay... Yeah, it'll at some point need to be reworked. We don't have to mention that in our documentation for this transcript."

### 2. Project Request Form & Workflow

**Project Request Initiates Process**:
> **Marcus Dallacqua**: "Request flows to a shared email inbox. So they're using complete project request form. So using that project request form to kick this off, which. That'll map to our project record that's automatically being created. Quoting team reviews the request. So they have a team that just does quotes."

**Labor Quote Scope Coverage**:
> **Marcus Dallacqua**: "Project request form. Okay, so we're familiar with this quoting. So yeah, our labor quote request covers all of this scope, all of that requirements. That's all going to map over Nicely. Oh yeah. This is like mentioning the hours potentially if they're going to be doing. If they already know at this point that they'll be doing it outside of regular business hours. And our labor quote captures that requirement."

### 3. Union Requirements

**Union Labor Requirements**:
> **Marcus Dallacqua**: "They have union. So that's a key call out is they have union requirements generally dictated by the building owners. If union workers are required, the work must come from a union subcontractor. Okay, so that's fine. We have that union or non union for our labor quote requests or if we don't have it in the basic. That's part of the. That's why we have a request engine. It allows us to build that stuff out."

> **Chris Trumble**: "So when they say cannot be quoted internally, then that just means that they have to select a contract. The labor request becomes an external request and it has to go to one of the ones that uses union labor."

**Action Item - Track Union Status on Vendor Records**:
> **Marcus Dallacqua**: "So that's a, that's something that we need to find out. Maybe not discovery but just a takeaway for us to do. We do we track vendors and if they're union or not on our vendor record. Okay, so that might even just be something we can ask Joe like Joe. Hey, for, you know, for the requirement that they use union vendors. Do we. Do we currently track that on our vendor record? If not, we can create the custom field and then the drop downs for the custom field. We need to know what those would be. Is it just union or non union? Something like that. Pretty easy."

### 4. CAP/SIF Files and Documentation

**CAP File Handling**:
> **Marcus Dallacqua**: "Generally CAT files and project plans... Okay, so they're actually sending the SIF. Are they sending the SIF file to the..."

> **Chris Trumble**: "No PDFs?"

> **Marcus Dallacqua**: "Oh, these documents are generally CAT files and project plans. Oh, so they probably export the sif instead of SIF they export as a PDF. Maybe... No, CAP is actually the software that they use to generate the sif."

> **Marcus Dallacqua**: "So what I'm curious about is are they using CAP to generate a PDF of the specifications, which is all the transaction lines. They're all the lines. So that's something we need to think we need to call out for discovery is what requirement they have at this point because we don't. I guess, I guess they would just export CAP as a PDF if that's what they're doing, attach it to the labor quote and call it good."

> **Chris Trumble**: "It just doesn't really make a lot of Sense. Because a capsif would just look like a wall of text in PDF. You have to bring it into something for it to make any sense. Right."

> **Marcus Dallacqua**: "Unless they're printing out the table. Unless it prints out the table, it won't be like in cap they see a table like our smart table. So if they choose PDF, it might just print that table where CIF is that text file. That's all arranged weird. So. Yeah, we'll figure that out."

### 5. Long Term Storage Quote Process

**LTS Quote Workflow**:
> **Marcus Dallacqua**: "Long term storage quote process, which we've already covered in quoting, but I guess. Or in order management, but I guess it also falls in here too, because you're going to get a quote from the warehouse. The warehouse, yeah. Or your labor. Your external labor or the warehouse sales rate."

> **Chris Trumble**: "Yeah. This one says they get a monthly surge quote from the warehouse in the calculation table. In the quote calculation process, they got to figure out thus the cubic footage or whatever it's going to take up and base it on that. And the warehouse calculates that."

> **Marcus Dallacqua**: "Yeah. Okay... Yeah. Yep, that makes sense."

### 6. CAM Reservation Number

**CAM System Integration (Manual)**:
> **Gary Strickland**: "What about the CAM reservation number? Where does that come from?"

> **Marcus Dallacqua**: "So they're using cam. CAM is that piece of software, Customer asset management software that they're using. And so they're going to set it up in cam and then CAM has a number for that record and that's the reservation number and they're just linking it here."

> **Gary Strickland**: "So that integration will need to be done."

> **Marcus Dallacqua**: "No, there's actually no integration. What they're doing here, they're just. They're doing it one system and copying the number over into their current system through Bridge. And we would have them do the same thing. We'll just have a field for a reservation number."

### 7. Labor Quote Calculations

**Manual Calculations Outside System**:
> **Marcus Dallacqua**: "Now it looks to me that they're doing quoting actual calculations inside of Bridge. Let's walk through here and see if that's the case. Because if that's the case, we do not have that currently in our system."

> **Marcus Dallacqua**: "The team manually calculates rate in hours and adds the total to the cost column. So, okay, so they're not actually doing the calculations in here, they're doing it outside the system and then manually plugging them in here, which is fine."

> **Gary Strickland**: "So we can support that."

> **Marcus Dallacqua**: "Yeah, we could support that. That's not a problem. Ideally, eventually what we want to do is have the ability for them to do their Calculations right in the system based on rate tables. We have a lot of dealers who want that, but we don't have that currently."

**Institutional Knowledge in Formulas**:
> **Chris Trumble**: "There's like a little institutional knowledge there where it says like if you go back up it says It's X times 1.52 rounded to the nearest 50. Even if there's like a notes field or somewhere where we can capture that."

> **Marcus Dallacqua**: "So yeah, it'll get captured. It's interesting that they're doing it that way, but again they're doing that all outside the system in probably Excel or something like that."

**Form Development Need**:
> **Chris Trumble**: "So form development is going to be important."

> **Marcus Dallacqua**: "Yeah, for sure."

### 8. Handoff from Operations to Sales

**Quote Completion Workflow**:
> **Marcus Dallacqua**: "And then they send quote to... Sales. Why do they send it to sales? Oh, after it's been done. Oh yeah, they sent it back to sales. So that's the handoff from the operations team back to the sales team. I'm calling it operations, but I don't think they call it operations. And then the sales team. So this is interesting step here. So Gary, just so you know, I guess it does go back to sales currently. And then the sales team determines, I guess."

### 9. Labor Quote Acceptance Feature

**Orion Feature Not in Bridge**:
> **Marcus Dallacqua**: "Yeah, but there's another step that we have that I don't think they have and that's the labor quote acceptance. So there's all these quotes that come back, especially if you're going external. And then at some point you have to say, okay, for this quote, I'm going to accept for this, sorry, this quote record in netsuite. I'm going to accept this labor quote. And then you link the particular labor quote to the quote record. And then there's this pop up that we have that allows them to determine what information from the labor quote will pass over to the quote. And so you have all these lines that they've itemized for costs on the labor quote, which is important for visibility. But they might not Want to show all those lines to the customer on the NetSuite quote record."

> **Marcus Dallacqua**: "So they have the ability there to consolidate that or summarize that or itemize it because some might need itemized. That step is called labor quote acceptance. And I don't think they have that. I'm not sure if they have that here in Bridge or not. I haven't seen it yet. But just so you know, something we'll look for in discovery is if they have a labor quote acceptance procedure."

> **Marcus Dallacqua**: "Yeah, so there's no like. So that step of bringing over the quoted information to the actual proposal or netsuite quote, they don't look like they have that. So that. That would be an improvement to their processes. That labor quote acceptance feature that we have."

### 10. External Subcontractor Selection

**Vendor Filtering by Union Status and Location**:
> **Gary Strickland**: "It looks like this is where they're kind of drilling down where union, non union. But the vendors are set up. So they've got to have something on the vendor record that says it's union or non union."

> **Marcus Dallacqua**: "Yeah, I think so. But then also they're also dependent on the location, the COR location, which makes sense. So we probably then need to identify our vendors by location. At least the service vendors. So not the product vendors, but service vendors. So here's a requirement and it's a pretty easy one for us to do. I know this is kind of early in the process, but just for a note, we'll need a requirement to identify service vendors in NetSuite by COR location."

> **Chris Trumble**: "It's just a custom field on the vendor record for service vendors."

> **Marcus Dallacqua**: "Yeah, because I don't think there's a location field on there now, but we'll just create a custom one and source it from the location."

**Union, Intermarket, and Location Dropdown**:
> **Marcus Dallacqua**: "Yeah, yeah. And then union intermarket. Okay. So this is where they differentiate between union, non union, intermarket. Yeah. And then cor. So we'll have to figure out like what that list of drop downs are. And you know, we might be able to handle that better than how they're doing it now. So we'll definitely dig in during discovery on that."

**Parent-Child Vendor Relationships**:
> **Gary Strickland**: "And something to consider. If the vendors service multiple or their parent company have divisions, we would probably want to use parent child on the vendor record. Like I said, they have just say it's, you know, Marcus installation. But they have a Massachusetts office and a state New York office. Yeah. You know, think about how to do that."

> **Marcus Dallacqua**: "Yeah, we might need to make that location field a multi select. Yeah, that could be. They could be Used across multi. Multi locations."

### 11. Request for Quote Forms and Branding

**RFQ Form**:
> **Marcus Dallacqua**: "Okay, good. They're just. Yeah, they're just attaching documents, which is fine. That's where that SharePoint integration is gonna be really helpful for them. Okay. We have a nice request for quote. So this is their form, I guess, you know, for their request for quote during discovery. We'll ask them if they want to upgrade this. There's no. There's not much branding on it, but that's fine. You know, that's how they want it."

> **Gary Strickland**: "I mean this is actually their logo. It may print in their colors, but that's actually their logo that they have on their website. Yep."

### 12. Pending Quotes Dashboard

**Tracking RFQs Sent to Subcontractors**:
> **Marcus Dallacqua**: "So then there's a little dashboard pending quote pending from sub so they could see everything they sent out for bid."

> **Gary Strickland**: "This is also a bridge."

> **Marcus Dallacqua**: "Yep. So that's something Luke or Chris. We need to figure out if we have that on the labor quote. I think that there might be a section on the labor quote that shows everybody that they sent it to and the status. We'll need to double check that because if we don't have that, we might just have to create a safe search."

### 13. Estimating Process (Interior Construction)

**Project Request Review for Estimating**:
> **Marcus Dallacqua**: "Yeah, sorry. Project request review Interior Construction Estimating. Okay. Yeah, this is. This falls under their operations order management. So this falls under operations, which makes sense to me. All this process overview is good. Sales Account Manager submits notifications. Go to. Oh, so the project request, which was an email, I think notifications go to estimating manager. Design Manager wants to sign another email sent to estimator for review. Estimator reviews Project request. Does the estimator have all the information needed to provide a quote? Aspira can be Quinn. Okay, Pretty basic."

**Project Request Checkboxes**:
> **Marcus Dallacqua**: "So this kind of follows the same path. Enbridge. They start with the project request and then if estimating is needed, they mark it. Oh, it's interesting here on this project request, do you need estimated. Is the estimated needed. Design needed, PM needed?"

**Missing Documentation for Design and PM**:
> **Marcus Dallacqua**: "So one thing we need to look for, and we don't have it in this bucket right now of pre quote, but there should be documentation for design and PM requests. So that should be in this pre quote section as well. Chris, do you have access to SharePoint?"

> **Chris Trumble**: "There's nothing on design. Let me look for pm... Yeah, design might be under that whole COR studio."

> **Marcus Dallacqua**: "Okay. So they probably didn't get the design and PM request."

### 14. Request Initiation Point (Adapt Requirement)

**Launching Requests from Project Record vs Opportunity/Quote**:
> **Marcus Dallacqua**: "So this is something interesting to note. They initiate these estimating or requests for estimates from the project record in Orion. They'll do it from the opportunity record or the quote record, not necessarily the project record. So again, the way that we treat the project record is it's almost a reporting tool and an aggregation tool. They don't do much at the project level. It's kind of automatically aggregating information and generating reports. And they'll launch things like a request for labor quote from the opportunity or quote record. So that's something to make sure that we emphasize during discovery. That'll be a shift in their process, something that they'll have to adapt to. Now that's a good example of align, adapt or accommodate. It definitely doesn't align. They will need to adapt. We could build an accommodation for them to do that, but I don't... I would push back on it. I don't see a reason why to accommodate that."

### 15. Project Scope Details

**Where Scope is Captured**:
> **Marcus Dallacqua**: "Project scope. So this is interesting. Okay, so like they're filling out the project scope details and we would typically do this elsewhere, but they're okay, so they're doing it. Yeah, we would do this on the. On the labor quote form, not on the project form. So this is going to be different for them. We would put in these requirement fields and they'd have to fill them out."

### 16. Site Conditions / Job Site Analysis

**Site Conditions Record**:
> **Marcus Dallacqua**: "Okay, so here's another thing. The site conditions. So they review the site conditions. So they do have a record for site conditions like we do. Just so you know, Gary, our site conditions record is attached to the address. So the address record in NetSuite is. It's actually. They have what they call the address book, and it is actually a record. And so we have our own customer record that's attached to the address itself and we link to it in different places. But, yeah, we have all of this on the site conditions record. Or I think. Is it called site conditions or job site analysis? I don't remember, Chris."

> **Chris Trumble**: "Originally it was called job site analysis."

> **Marcus Dallacqua**: "And then we change it to site conditions."

> **Chris Trumble**: "No, I think. Well, I think the industry term is site conditions, and we change it to job site analysis because it's deeper than what most people are doing."

### 17. Request Rejection Workflow

**Sending Request Back for More Information**:
> **Marcus Dallacqua**: "Notes. They're just basically saying just. Yeah, they're checking. Yeah, we have that too. That maps over. Attach your documents. That's normal stuff. Once they click on. So then they can send it back to Siddharth. Oh, okay. This is because they have. So they have a process where if you don't give them enough information, they can send it back for more information. Chris, will you just make a note for Joe to make sure that I think we have a process for that on the labor quote request, or were..."

> **Chris Trumble**: "We handling it with not allowing them to submit something that didn't have all the required fields?"

> **Marcus Dallacqua**: "Yeah, so you can do that with my mandatory fields. But a lot of times you don't do that because they're progressively making that record."

> **Gary Strickland**: "That's the challenge is if they're required, it's not going to let you save it."

> **Chris Trumble**: "And then later we're asking Joe if he's built any logic in there. To be able to send it back."

> **Marcus Dallacqua**: "Yeah, to send it back for more information. I believe there was."

---

## Session Conclusion

**End of Pre-Quote Documentation**:
> **Chris Trumble**: "Yeah, I was gonna say it's. That's all of it for pre quote."

> **Gary Strickland**: "Yeah, I think we need to wait for. We can go and look at this next section."

---

## Key Requirements Identified

### Labor Quote Requirements
1. Support multiple labor quote request types (Internal, External, Intermarket, LTS)
2. Union/non-union vendor tracking
3. Vendor location-based filtering
4. Parent-child vendor relationships
5. Labor quote acceptance workflow
6. Pending quote dashboard/report
7. Rate calculation support (manual entry with institutional knowledge capture)
8. CAP/SIF file attachment handling
9. CAM reservation number field
10. Request form customization capabilities

### Estimating Requirements
1. Project request form with checkboxes (Estimating needed, Design needed, PM needed)
2. Estimator assignment by location
3. Project scope capture on appropriate forms
4. Site conditions/job site analysis record
5. Request rejection/send back workflow
6. Document attachment support

### Process Adaptations
1. **ADAPT**: Launch requests from Opportunity/Quote records (not Project record)
2. **ADAPT**: Capture project scope on labor quote form (not project record)
3. **ACCOMMODATE**: Custom vendor fields (union status, location, intermarket)
4. **ALIGNS**: Request engine supports multiple request types
5. **ALIGNS**: Job site analysis record exists

### Outstanding Items
1. Design request documentation missing
2. PM request documentation missing
3. Confirmation needed: labor quote pending status tracking functionality
4. Confirmation needed: request rejection workflow in request engine
5. Rate table functionality for future phase

---

**Document Prepared**: October 16, 2025  
**Prepared For**: KBMH Pre-Quote Discovery Analysis





# Instructions: Organizing Discovery Transcripts

## Quick Summary
You have 3 transcripts that need to be organized into your business process folders:

## File Organization Steps

### Step 1: Copy Marketing/CRM Transcript (to 2 locations)
**File:** `GMT20250917-200141_Recording.transcript.vtt`

**Copy to BOTH:**
1. `Marketing\2 Input\GMT20250917-200141_Recording.transcript.vtt`
2. `CRM\2 Input\GMT20250917-200141_Recording.transcript.vtt`

**Why:** This transcript covers both Marketing (lead management, email marketing, RFPs) and CRM (Zendesk, opportunity tracking, sales workflow)

---

### Step 2: Move Financial Management Transcript
**File:** `GMT20250918-211018_Recording.transcript.vtt`

**Move to:**
- `Financial Management\2 Input\GMT20250918-211018_Recording.transcript.vtt`

**Why:** This transcript exclusively covers financial management topics (AP, AR, GL, tax, commissions, etc.)

---

### Step 3: Keep Project Kickoff Transcript in Main Folder (or create new folder)
**File:** `GMT20250917-154358_Recording.cc.vtt`

**Option A:** Keep in main KBMH folder (current location)  
**Option B:** Create a new folder `0 - Project Kickoff` and move it there

**Why:** This is the general project kickoff and methodology overview, not specific to any one process area

---

## Quick PowerShell Commands (if files unlock)

```powershell
# Navigate to KBMH folder
cd "C:\Users\ChrisTrumble\OneDrive - Global Systems Integration\Documents\Repos\KBMH"

# Copy Marketing/CRM transcript to Marketing
Copy-Item "GMT20250917-200141_Recording.transcript.vtt" -Destination "Marketing\2 Input\"

# Copy Marketing/CRM transcript to CRM
Copy-Item "GMT20250917-200141_Recording.transcript.vtt" -Destination "CRM\2 Input\"

# Move Financial transcript
Move-Item "GMT20250918-211018_Recording.transcript.vtt" -Destination "Financial Management\2 Input\"

# Optional: Move kickoff transcript
# New-Item -Path "0 - Project Kickoff" -ItemType Directory
# Move-Item "GMT20250917-154358_Recording.cc.vtt" -Destination "0 - Project Kickoff\"
```

---

## Alternative: Use Windows Explorer

If files are locked due to OneDrive sync:

1. Open Windows Explorer
2. Navigate to the KBMH folder
3. Right-click `GMT20250917-200141_Recording.transcript.vtt` → Copy
4. Navigate to `Marketing\2 Input\` → Paste
5. Navigate to `CRM\2 Input\` → Paste
6. Go back to main folder, right-click `GMT20250918-211018_Recording.transcript.vtt` → Cut
7. Navigate to `Financial Management\2 Input\` → Paste

---

## What's Missing?

After organizing, you'll still need transcripts for:

### **CRITICAL - No Coverage:**
- ❌ **Business Intelligence** - Reporting, dashboards, analytics requirements
- ❌ **Pre-Quote** - Estimating process, labor quotes (though you have documents in Creative-Office-Resources)
- ❌ **Operations** - Operational workflows, warehouse, field operations

### **Partial Coverage:**
- ⚠️ **Order Management** - Partially covered in Financial session (POs mentioned), but may need dedicated session
- ⚠️ **System Setup and Configuration** - Mentioned in kickoff, but not comprehensive

### **Good Coverage:**
- ✅ **Marketing** - Covered in Sept 17 evening session
- ✅ **CRM** - Covered in Sept 17 evening session  
- ✅ **Financial Management** - Covered in Sept 18 session

---

## Next Steps After Organization

1. **Review your calendar:** Were there other discovery sessions recorded that aren't in the main folder?

2. **Schedule missing sessions:** Business Intelligence, Pre-Quote, Operations need dedicated discovery time

3. **Process existing transcripts:** Use your AI discovery questionnaire analysis prompts on the transcripts now properly filed

4. **Cross-reference:** The Marketing/CRM transcript mentions:
   - Asana workflow
   - Zendesk data
   - RFP processes
   
   These details should inform requirements in multiple BRDs.

---

**See `Transcript_Analysis_and_Mapping.md` for detailed analysis of what's in each transcript.**


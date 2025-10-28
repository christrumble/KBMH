# AI-Assisted Discovery Workflow Specification

## Objective
Establish a repeatable, AI-assisted discovery workflow that aggregates all `In_` inputs across multiple sessions, applies consistent evidence and tagging ([REQUIREMENT], [DECISIONS], [FUNCTIONALITY], [SOLUTIONDESIGN], [ASSUMPTION], [CONSTRAINT], [RISK], [PRIORITY]), iteratively completes and updates the questionnaire to close gaps, maps requirements to Orion/NetSuite capabilities, and produces `Out_` deliverables—culminating in a validated, traceable BRD with minimal rework and high confidence.

## Scope & Constraints
- One process area per project folder.
- Multi-session iterations; new inputs may arrive between runs.
- Single folder; outputs must be created as Claude artifacts named exactly as the `Out_` filename.

## File Conventions
- Inputs: Files in `INPUT/` folder (e.g., `Transcript_CEO.md`, `Notes_Operations.md`, `Email_Clarification.md`).
- Outputs: Files in `OUTPUT/` folder (e.g., `Questionnaire_OrderMgmt.md`, `Requirements_Map_OrderMgmt.md`, `BRD_OrderMgmt_v1.0.md`).
- Versioning: append `vX.Y` to major deliverables; maintain a brief Change Log.

## Standard Tags
- [REQUIREMENT] (Type: Functional | Non-Functional)
- [DECISIONS]
- [FUNCTIONALITY]
- [SOLUTIONDESIGN]
- [ASSUMPTION]
- [CONSTRAINT]
- [RISK]
- [PRIORITY] (Must-Have | Should-Have | Nice-to-Have)

## Decision Detection Cues
- Explicit: "decision", "decided", "confirmed".
- Implicit: "we will/won't", "we'll use", "standard [feature]", "aligns", "adapt", "accommodate", "future phase".

## Implementation Approach Classifications

**ALIGNS**: The way the dealer is executing a business process in their current business system aligns with how they will do it in Orion. It might not be an exact one-to-one alignment, but it doesn't require any customizations for them to do what they are currently doing now in Orion.

**ADAPT**: They do need to modify their business process to use Orion. Adaptation is on a spectrum so it could be major or minor - but still no customization required.

**ACCOMMODATE**: WE will accommodate their business process by customization, personalization, new configuration - something we need to do to accommodate their needs.

## Coverage Check (Every Prompt)
1) List all files in the `INPUT/` folder; mark processed vs new.
2) Analyze all new input files; summarize sources in the output.
3) Maintain/update a "PROCESSED FILES" section in outputs.

## Requirement IDs
- Assign `REQ-###` to each requirement and carry through Questionnaire → Requirements Map → BRD.

## Required Artifacts
1) Questionnaire (Questionnaire_[Area].md in OUTPUT/ folder)
   - Evidence-backed answers with confidence ratings
   - Tags applied; Decision Log section
   - Reviewed/Processed files list

2) Requirements Map (Requirements_Map_[Area].md in OUTPUT/ folder)
   - Columns: ID | Requirement | Type | Functionality | Decision | SolutionDesign? | Approach (ALIGNS/ADAPT/ACCOMMODATE/FUTURE) | Risks

3) BRD (BRD_[Area]_vX.Y.md in OUTPUT/ folder)
   - Based on completed questionnaire and requirements map
   - Includes Solution Validation table and Implementation Approach

## Quality Gates Before BRD
- No critical gaps remaining for Must-Have requirements.
- Confidence ≥ 85% for Must-Haves.
- Each `REQ-###` mapped to an approach (ALIGNS/ADAPT/ACCOMMODATE/FUTURE).

## Prompt Standards (Reference Block)
- Use the Legend: `In_` = inputs; `Out_` = outputs.
- Apply Standard Tags above.
- Always run the Coverage Check.
- Always produce a named `Out_*` artifact and include a top-level Change Log (date, sources, summary of changes).

## Prompt Catalog
- `1 Discovery Questionnaire Analysis Promp.md` – Analyze all new `In_` files, complete the questionnaire for the process area with evidence, tags, confidence; produce `Out_Questionnaire_[Area].md`.
- `2 Discovery Questionnaire Update Prompt.md` – Update existing questionnaire using only new `In_` files; classify changes (ENHANCE/REVISE/ELEVATE/COMPLETE); produce `Out_Questionnaire_[Area]_Updated.md`.
- `3 Discovery Questionnaire Completeness A.md` – Assess completeness, produce status matrix, gaps, and follow-up plan; produce `Out_GapAnalysis_[Area].md`.
- `4 BRD Analysis Two-Phase Process.md` – Validate BRD draft vs final, map requirements to solutions and approaches; produce `Out_BRD_Analysis_[Area]_vX.Y.md`.
- `5 Generate Business Requirements Document from Discovery Questionnaire.md` – Generate the BRD from questionnaire + requirements map; produce `Out_Questionnaire_[Area]_vX.Y.md`.

## Standards Appendix (Copy-Paste Block)
Use this block at the top of any prompt:

Legend: `In_` = inputs; `Out_` = outputs. Coverage Check: list all `In_` files; mark processed vs new; analyze all new. Standard Tags: [REQUIREMENT] (Type: Functional | Non-Functional), [DECISIONS], [FUNCTIONALITY], [SOLUTIONDESIGN], [ASSUMPTION], [CONSTRAINT], [RISK], [PRIORITY]. Decision Detection: explicit ("decision", "decided", "confirmed") and implicit ("we will/won't", "we'll use", "standard", "aligns", "adapt", "accommodate", "future phase"). Requirements: assign and carry `REQ-###` through Questionnaire → Requirements Map → BRD. Outputs: create a named `Out_*` artifact with a top Change Log (date, sources, summary) and a PROCESSED FILES section.

## Change Log
- v1.0 – Initial specification established.











Output Validation Checklist Prompt

Follow Prompt Standards in `Instructions/Discovery Workflow Specification.md`.

Purpose
Validate any `Out_*` artifact (Questionnaire, Requirements Map, Gap Analysis, BRD) before proceeding to the next step.

Inputs
- Target artifact filename (e.g., `Questionnaire_[Area]_v1.1.md` in OUTPUT/ folder)
- All current files in INPUT/ folder (for quick coverage sanity)

Checks
- Header
  - Contains Change Log (date, version, sources summary)
  - Contains PROCESSED FILES section (for analysis outputs)
- Requirements
  - Every requirement labeled with `REQ-###`
  - Type provided (Functional/Non-Functional)
  - Priorities present for Must/Should/Nice
- Decisions
  - Decision Log present with `[DECISIONS]`, `[FUNCTIONALITY]`, `[SOLUTIONDESIGN]`
  - Each decision references `REQ-###`
- Evidence
  - Quotes attributed (speaker, source file)
  - Confidence rules followed (no numeric < 80%; use Insufficient evidence instead)
- Mapping (if Requirements Map/BRD)
  - Each `REQ-###` mapped to approach (ALIGNS/ADAPT/ACCOMMODATE/FUTURE)
  - Risks captured where applicable
- Consistency
  - Naming matches `Out_*` convention with version suffix
  - Area name consistent throughout

Output (Claude Artifact)
- Create artifact: `Validation_Report_[Area]_for_[TargetFile]_v1.0.md` (save in OUTPUT/ folder)
- Include Pass/Fail per check with fixes required
- Summarize missing items and recommended edits


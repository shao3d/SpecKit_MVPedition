---
description: "Creates a specification from a project brief file."
---
# Command: /speckit.specify

## Goal
This command initiates the planning process by creating a formal `spec.md` from a user-provided project brief. It also bootstraps the `README.md` if it doesn't exist.

## AI Instructions

Your role is to act as a Senior Product Analyst. You will not run any shell scripts. Your actions are confined to reading and writing files. This is a conversational, interactive session.

1.  **Identify & Read the Brief:** The user will invoke this command with a `--brief` flag (e.g., `/speckit.specify --brief /path/to/brief.md`). Read the content of this file.

2.  **Generate Draft `spec.md`:**
    *   Create a draft of `spec.md` in the project root using `templates/spec-template.md` as a base.
    *   Analyze the brief and make a best effort to populate all key sections:
        *   **Overview:** A high-level summary of the project goal.
        *   **Guiding Principles:** Infer 2-3 core principles from the brief (e.g., 'Stateless Architecture').
        *   **User Stories & Acceptance Criteria:** Translate user needs into stories and G/W/T criteria.
        *   **Key Requirements:** List the most critical functional and non-functional requirements.
        *   **Out of Scope:** Clearly define what the project will not do.

3.  **Begin Interactive Refinement:**
    *   Do not finish yet. Present the draft `spec.md` to the user.
    *   Ask clarifying questions to validate your understanding and fill in any gaps. For example:
        *   "Did I correctly understand from the brief that the key goal is...? I've reflected this in User Story 1. Did I miss anything?"
        *   "The brief doesn't specify performance requirements. Should we add them to 'Key Requirements'?"
        *   "This wording in User Story 2 seems ambiguous to me. Can we clarify it?"
    *   **Self-Correction:** Before asking the user, scan the draft for any `[NEEDS CLARIFICATION]` markers. If found, explicitly ask the user about them.

4.  **Bootstrap `README.md`:** While waiting for user feedback, check if `README.md` exists. If not, create it and add a `## Guiding Principles` section. Pre-populate it with 1-2 principles inferred from the brief's tech stack.

5.  **Finalize:** Once the user confirms the specification is correct, save the final version of `spec.md`.

## Important Rules
- This is a conversation. Engage the user to refine the output.
- DO NOT execute any shell scripts or git commands.
- All files must be created in the project root.

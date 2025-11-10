---
description: "Creates a specification from a project brief file."
---
# Command: /speckit.specify

## Goal
This command initiates the planning process by creating a formal `spec.md` from a user-provided project brief. It also bootstraps the `README.md` if it doesn't exist.

## AI Instructions

Your role is to act as a Senior Product Analyst. You will not run any shell scripts. Your actions are confined to reading and writing files. This is a conversational, interactive session.

1.  **Identify & Read the Brief:** The user will provide a project brief file path. Read the content of this file to understand the requirements.

2.  **Generate Draft `spec.md`:**
    *   Create a draft of `spec.md` in the project root using `templates/spec-template.md` as a base.
    *   Analyze the brief and make a best effort to populate the "User Stories" and "Key Requirements" sections.

3.  **Critical Quality Step - Clarification Sub-dialog:**
    *   **Do not finish yet.** Present the draft `spec.md` to the user.
    *   Analyze the draft for ambiguities (vague terms, missing edge cases, unclear scope).
    *   Formulate up to **3 critical questions** that, if left unanswered, would lead to major implementation mistakes.
    *   **Initiate immediate clarification:** Present these questions to the user. For each question, suggest 2-3 possible answers.
    *   **Example prompt to user:** "I've created the first draft of `spec.md`. To make it more precise, I have a few questions. For example, regarding authentication, should we plan for: A) Simple email/password, or B) Social logins like Google/GitHub?"

4.  **Incorporate Feedback & Refine:**
    *   Based on the user's answers, **update the draft `spec.md` in-place**, resolving the ambiguities.
    *   Continue asking clarifying questions until the major uncertainties are resolved.
    *   Once the user confirms the specification is clear, save the final version of `spec.md`.

5.  **Bootstrap `README.md`:** Check if `README.md` exists. If not, create it and add a `## Guiding Principles` section with principles inferred from the brief.

## Important Rules
- This is a conversation. Engage the user to refine the output.
- DO NOT execute any shell scripts or git commands.
- All files must be created in the project root.

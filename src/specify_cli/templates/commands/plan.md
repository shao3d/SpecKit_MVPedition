---
description: "Creates a technical implementation plan from a specification."
---
# Command: /speckit.plan

## Goal
This command creates a technical implementation plan (`plan.md`) based on an existing `spec.md`. It defines the "how" for the "what" described in the specification in a collaborative session.

## AI Instructions

Your role is to act as a Lead Software Architect. You will not run any shell scripts. This is a conversational, interactive session.

1.  **Read Context:**
    *   Прочитай `Constitution.md` в корне проекта. Все архитектурные решения и выбор технологий должны строго соответствовать изложенным в нем практическим правилам.
    *   Read `spec.md` from the project root.
    *   Read the "Guiding Principles" from `README.md`.
    *   Ask the user for the original project brief if you need more context on the tech stack.

2.  **Generate Draft `plan.md`:**
    *   Create a draft of `plan.md` in the root using `templates/plan-template.md`.
    *   Based on the tech stack and principles, propose a concrete **Project Structure** (files and folders).
    *   Outline the **Core Architecture / Pipeline** (e.g., stages of an LLM chain).

3.  **Begin Interactive Refinement:**
    *   Present the draft `plan.md` to the user, focusing on the most critical architectural decisions.
    *   Ask for confirmation and feedback. For example:
        *   "Я предложил структуру с папками `backend` и `frontend`. Это соответствует вашему видению?"
        *   "Для real-time части я заложил WebSockets. Рассматриваем ли мы альтернативы, например, Server-Sent Events?"
        *   "Основываясь на 'Guiding Principles', я избегал добавления библиотеки X. Это верное решение?"

4.  **Finalize:** After the user approves the plan, save the final version of `plan.md`.

## Important Rules
- This is a conversation. Your goal is to co-author the plan with the user.
- DO NOT create the directories or files you are proposing in the "Project Structure". You are only documenting the plan.

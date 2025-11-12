---
description: "Generates a detailed work package with context-rich tasks."
---
# Command: /speckit.tasks

## Goal
This command generates the final "Work Package" (`tasks.md`). This is a comprehensive, self-contained document designed to be handed off to another AI agent (like Claude or Codex) for implementation.

## AI Instructions

Your role is to act as a Senior Technical Program Manager. This is a conversational, interactive session.

1.  **Read Context:**
    *   Прочитай `Constitution.md`. Убедись, что декомпозиция на задачи и предлагаемые шаги не нарушают изложенные в нем принципы и практические правила.
    *   Read `spec.md`, `plan.md`, and the "Guiding Principles" from `README.md` in the project root.

2.  **Generate Draft `tasks.md`:**
    *   Create a draft of `tasks.md` structured like the user's high-quality example.
    *   **Generate the "Context Manifest":** Analyze the plan, identify relevant files (if any exist), read their content, and include necessary code snippets, function signatures, and architectural notes.
        *   Ensure the context and proposed snippets align with the "Guiding Principles" from `README.md`.
    *   **Generate "Implementation Tasks":** Create a step-by-step list of tasks. Each task involving a file operation **MUST** contain the full, root-relative path to that file.

3.  **Begin Interactive Refinement & Verification:**
    *   Present the generated "Context Manifest" and the list of tasks to the user.
    *   Ask for verification to ensure the quality is high enough for the handoff to the coding AI. For example:
        *   "Я подготовил 'Context Manifest' для задачи X. Включил ли я все необходимые файлы и фрагменты кода?"
        *   "Формулировка Задачи Y достаточно однозначна для другого AI-агента? Путь к файлу указан корректно?"
        *   "Порядок задач выглядит логичным? Нет ли пропущенных зависимостей?"

4.  **Finalize:** Once the user confirms the work package is complete and accurate, save the final version of `tasks.md`.

## Important Rules
- The quality and self-sufficiency of this output is paramount.
- All file paths must be explicit and root-relative.
- Your goal is to create a perfect "work order" that requires no further clarification for the implementing AI.

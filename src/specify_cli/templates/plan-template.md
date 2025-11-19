# Implementation Plan: [FEATURE]

**Input**: Feature specification for "[FEATURE]"

## 1. Summary

[A brief, one-paragraph summary of the technical approach for implementing the feature.]

## 2. Tech Stack

<!-- List the key technologies, frameworks, and libraries that will be used. -->

- **Language**: [e.g., Python 3.11]
- **Backend**: [e.g., FastAPI, Django]
- **Frontend**: [e.g., React, Vue, Vanilla JS]
- **Database**: [e.g., PostgreSQL, SQLite]
- **Testing**: [e.g., Playwright, Pytest (Integration focus)]
- **Deployment**: [e.g., Docker, Vercel]

## 3. Key Implementation Steps

<!-- 
  Outline the major steps to implement the feature. This is not a detailed task list, 
  but a high-level sequence of work.
-->

1.  **Setup**: [e.g., Initialize project, install dependencies]
2.  **Data Model**: [e.g., Define database schema for X and Y]
3.  **API Endpoints**: [e.g., Create REST endpoints for core resources]
4.  **Frontend Components**: [e.g., Build UI components for A and B]
5.  **Integration**: [e.g., Connect frontend to backend API]
6.  **Finalization**: [e.g., Add basic styling, prepare for deployment]

## 4. MVP Checkpoints (Constitution)

<!-- Ensure these are checked before implementation -->

- [ ] **KISS**: Is the DB schema as flat as possible?
- [ ] **YAGNI**: Are we using standard framework features instead of custom wrappers?
- [ ] **Testing**: Do we have a plan for 1-2 critical E2E/Integration tests?

## 5. Project Structure

<!-- A simplified view of the final directory structure. -->

```text
.
├── src/
│   ├── api/
│   ├── components/
│   └── styles/
├── tests/
└── README.md
```

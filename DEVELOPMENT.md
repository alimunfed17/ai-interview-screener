# Mini AI Interview Screener – Development Notes

## Overview

This document explains why and how the backend for the Mini AI Interview Screener was built. It includes design decisions, technology choices, and the step-by-step process of implementation.

---

## Technology Stack Decisions

| Layer |	Technology  |	Reasoning |
|---------|------------|----------|
| **Language**  |	Python 3.10+ |	Python provides a rich ecosystem for AI/ML, fast prototyping, and strong async support. |
| **Framework** |	FastAPI |	FastAPI allows rapid API development, built-in validation with Pydantic, asynchronous endpoints, and automatic API documentation via Swagger/OpenAPI. |
| **LLM**	| Google Gemini 2.5 Flash |	Provides fast, accurate, and structured JSON output. The “Flash” variant is optimized for low-latency multi-candidate evaluation. |
| **Validation**  |	Pydantic v2 |	Ensures request/response bodies follow strict schemas, preventing malformed data from breaking the API. |
| **Server**  |	Uvicorn (ASGI)  |	High-performance server for async FastAPI applications, suitable for real-time evaluation APIs. |
| **Configuration** |	python-dotenv |	Manages environment variables (e.g., Gemini API key) securely.  |

**Decision Summary**:
The focus was on **speed, reliability, and maintainable code structure**. FastAPI + Pydantic ensures strong typing, Gemini gives structured LLM output, and Python allows for rapid development.

--- 

## Step-by-Step Development Process

### Step 1: Define the Schema

- Created **Pydantic models** for:

  - `CandidateAnswer` – single candidate input

  - `EvaluateResponse` – AI evaluation response

  - `RankRequest` – array of candidate answers

  - `RankResponse` – ranked candidates list

- **Purpose**: ensures clean, predictable request and response data.

---

### Step 2: Build the API Routes

- Implemented two main FastAPI routers:

  **1**. `/evaluate-answer/` – evaluates a single candidate answer

  **2**. `/rank-candidates/` – evaluates multiple candidates and sorts by score

- **Why**: separating routers makes the code modular, easy to maintain, and testable.

---

### Step 3: Integrate the LLM Client

- Created a **Gemini client wrapper** in `app/core/gemini.py`

- Used `client.models.generate_content` to send prompts and receive responses

- Added `extract_json` utility to safely parse JSON from the LLM output

- **Why**: Ensures LLM responses are consistent and structured, allowing the API to always return valid JSON.

---

### Step 4: Prompt Engineering

- Designed `EVAL_PROMPT` to instruct the LLM to:

  - Return ONLY JSON

  - Include `score`, `summary`, and `improvement`

  - Avoid extra text, markdown, or explanations

- **Why**: Guarantees predictable parsing and avoids runtime errors from unstructured LLM outputs.

---

### Step 5: Implement Business Logic

- `/evaluate-answer`:

  - Sends a single candidate answer to Gemini

  - Parses the JSON

  - Returns structured `EvaluateResponse`

- `/rank-candidates`:

  - Loops over all candidates

  - Evaluates each via Gemini

  - Sorts results by `score` descending

  - Returns `RankResponse`

- **Why**: Stepwise, modular approach ensures clarity, maintainability, and ease of debugging.

---

### Step 6: Error Handling & Validation
- Added checks for:
  - LLM response parsing (`extract_json`)
  - Score validity (1–5)
  - Exception handling for Gemini API errors
- **Why**: Ensures API is robust and doesn’t fail silently during production use.

---

### Step 7: Project Structure & Maintainability
```bash
app/
  api/
    routes/
      evaluate_answer.py
      rank_candidates.py
    schemas.py
  core/
    gemini.py
  utils/
    extract_json.py
    prompts.py
main.py
```

- **Why**: Separating concerns (schemas, routes, LLM client, utils) makes the codebase scalable and easy to extend (e.g., adding new LLMs or endpoints).

---

### Step 8: Testing & Verification

- Verified endpoints with:

  - `curl` requests

  - Local FastAPI Swagger UI

- Confirmed correct:

  - JSON structure

  - Score sorting

  - Handling of invalid LLM responses

---

### Step 9: Documentation

- Added **README.md** with:
- Tech stack
- Features
- API endpoints
- Example requests
- Developer notes
- Added **DEVELOPMENT.md** (this file) to explain engineering decisions.

---

## Key Takeaways

- **Start with schema first**: ensures API consistency and easy validation.
- **Modular router design**: allows easy scaling and testing.
- **LLM integration via a client wrapper**: isolates AI logic and allows switching LLMs easily.
- **Prompt engineering**: critical to get structured output reliably from an LLM.
- **Validation & error handling**: prevents runtime failures from unstructured LLM responses.

---

- This document demonstrates my engineering thought process, from schema design → API → LLM integration → error handling → deployment readiness.


# Mini AI Interview Screener (Backend Only)
A lightweight FastAPI-based backend service that evaluates candidate answers using Google Gemini and ranks candidates based on LLM-generated scores.

---

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Developer Notes](#developer-notes)
- [DEVELOPMENT](#Development)
- [LICENSE](#license)

---

## Features
### 1. Evaluate Candidate Answers
- Accepts a single candidate response.
- Sends the answer to an LLM (Gemini / OpenAI / Claude / LLaMA).
- Performs AI-based evaluation on:
    - Score (1–5)
    - One-line summary
    - One improvement suggestion

### 2. Rank Multiple Candidates
- Accepts an array of candidate answers.
- Evaluates each answer via the LLM using the same evaluation prompt.
- Assigns a score (1–5) to each candidate.
- Sorts candidates from highest score → lowest score.
- Returns an ordered list with:
    - Original answer
    - Score
    - Summary
    - Improvement suggestion

### 3. FastAPI Auto Documentation Included
- Automatic Swagger UI
- Automatic ReDoc UI
- Interactive JSON testing directly from browser

---

## Tech Stack
| Layer	| Technology |
|-------|------------|
|Language	| Python 3.10+ |
| Framework	| FastAPI |
| LLM  | Google Gemini |
| Validation |	Pydantic v2 | 
| Server |	Uvicorn |

---

## Project Structure
```bash
ai-interview-screener/
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── evaluate_answer.py
│   │   │   └── rank_candidates.py
│   │   ├── main.py
│   │   └── schemas.py
│   ├── core/
│   │   └── gemini.py
│   ├── utils/
│   │   ├── extract_json.py
│   │   └── prompts.py
│   └── main.py
├── .gitignore
├── .env.example 
├── README.md
└── requirements.txt
```

---

## Setup & Installation
### 1. Clone the Repository
```bash
git clone https://github.com/alimunfed17/ai-interview-screener.git
cd ai-interview-screener
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root based on `.env.example`:
```bash
LLM_API_KEY=gemini-api-key
```

### 5. Run the Application
```bash
uvicorn app.main:app --reload
```
- Server runs on → http://localhost:8000

### 6. Open API Docs
- Visit → http://localhost:8000/docs
- FastAPI’s interactive Swagger UI lets you test all endpoints directly.

---

## Example `.env.example`
```bash
LLM_API_KEY=gemini-api-key
```

---


## API Endpoints – Mini AI Interview Screener

| Category | Method	 |  Endpoint	                    | Summary / Description 	            | Auth Required |
|----------|---------|----------------------------------|---------------------------------------|---------------|
| Evaluation	   | POST	 | `/api/v1/evaluate-answer`	        | Evaluates a single candidate’s answer and returns structured AI feedback.                | False         |
| Ranking	   | POST	 | `/api/v1/rank-candidates/`	            | Evaluates multiple answers and returns sorted candidates by score.    | False         |

---

## Schema References Summary

| Schema Name	                    |   Used In             |	Purpose                                       |
|-----------------------------------|-----------------------|-------------------------------------------------|
| CandidateAnswer   |	Evaluate / Rank |	Input model for a single answer |
| EvaluateResponse  |	Evaluate    |	Structure of LLM response   |
| RankRequest   |	Rank    |	Request containing list of candidate answers    |
| RankedCandidates  |	Rank    |	Ranked output including score + summary |
| RankResponse  |	Rank    |	Final ordered list returned to client   |


---

## Example API Calls

### Evaluate a Single Answer

[Evaluate Answer Route](assets/Evaluate-Answer.png)

```bash
curl -X POST "http://localhost:8000/api/v1/evaluate-answer/" \
  -H "Content-Type: application/json" \
  -d '{
    "answer": "I believe leadership is about inspiring your team to achieve goals together."
  }'
```

-----

### Rank Multiple Candidates

[Rank Candidates Route](assets/Rank-Candidates.png)

```bash
curl -X POST "http://localhost:8000/api/v1/rank-candidates/" \
  -H "Content-Type: application/json" \
  -d '{
    "candidates": [
      { "answer": "Leadership is about inspiring others to achieve goals." },
      { "answer": "I focus on managing tasks and deadlines efficiently." },
    ]
  }'
```

----

## Developer Notes

- The architecture follows a modular **FastAPI structure**: routes, schemas, and LLM integration are separated for maintainability.
- `extract_json()` safely parses the JSON returned from Google Gemini, ensuring the API always returns structured responses.
- LLM evaluation is **model-agnostic**, so you can replace Gemini with OpenAI, Claude, or LLaMA without changing the backend structure.

---

## DEVELOPMENT 

- The architecuture is explained in ***[DEVELOPMENT.md](./DEVELOPMENT.md)***

---

## LICENSE

- Please go through the ***[LICENSE](./LICENSE)*** to know about terms and conditions.
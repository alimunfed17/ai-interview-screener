from fastapi import APIRouter, HTTPException
from app.api.schemas import CandidateAnswer, EvaluateResponse
from app.utils.extract_json import extract_json
from app.utils.prompts import EVAL_PROMPT
from app.core.gemini import client

router = APIRouter(prefix="/evaluate-answer", tags=["evaluate-answer"])

@router.post("/", response_model=EvaluateResponse)
def evaluate_answer(answer: CandidateAnswer):
    prompt = EVAL_PROMPT.replace("{answer}", answer.answer)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    parsed = extract_json(response.text)

    if not parsed:
        raise HTTPException(status_code=500, detail="Invalid JSON returned from Gemini")

    return EvaluateResponse(**parsed)

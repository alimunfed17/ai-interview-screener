from fastapi import APIRouter, HTTPException

from app.api.routes.evaluate_answer import EVAL_PROMPT, client
from app.api.schemas import RankResponse, RankRequest, RankedCandidates
from app.core.gemini import GEMINI_MODEL
from app.utils.extract_json import extract_json


router = APIRouter(prefix="/rank-candidates", tags=["rank-candidates"])

@router.post("/", response_model=RankResponse)
def rank_candidates(payload: RankRequest):
    ranked_result = []

    for candidate in payload.candidates:
        prompt = EVAL_PROMPT.replace("{answer}", candidate.answer)

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        parsed = extract_json(response.text)

        if not parsed:
            raise HTTPException(status_code=500, detail="Invalid JSON from Gemini.")
        
        ranked_result.append(
            RankedCandidates(
                answer=candidate.answer,
                score=parsed["score"],
                summary=parsed["summary"],
                improvement=parsed["improvement"]
            )
        )

    ranked_result.sort(key=lambda x: x.score, reverse=True)
    return RankResponse(ranked=ranked_result)
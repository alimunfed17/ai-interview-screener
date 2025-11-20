from typing import List
from pydantic import BaseModel

class CandidateAnswer(BaseModel):
    answer: str

class EvaluateResponse(BaseModel):
    score: int
    summary: str
    improvement: str

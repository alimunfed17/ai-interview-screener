from typing import List
from pydantic import BaseModel

class CandidateAnswer(BaseModel):
    answer: str

class EvaluateResponse(BaseModel):
    score: int
    summary: str
    improvement: str

class RankedCandidates(BaseModel):
    answer: str
    score: int
    summary: str
    improvement: str

class RankRequest(BaseModel):
    candidates: List[CandidateAnswer]

class RankResponse(BaseModel):
    ranked: List[RankedCandidates]
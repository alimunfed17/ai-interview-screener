from fastapi import APIRouter
from app.api.routes import evaluate_answer, rank_candidates

api_router = APIRouter()

api_router.include_router(evaluate_answer.router)
api_router.include_router(rank_candidates.router)
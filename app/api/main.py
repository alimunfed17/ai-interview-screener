from fastapi import APIRouter
from app.api.routes import evaluate_answer

api_router = APIRouter()

api_router.include_router(evaluate_answer.router)
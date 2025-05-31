from fastapi import APIRouter, HTTPException, status
from typing import List
from datetime import datetime

from app.models.question import QuestionCreate, Question, QuestionResponse

router = APIRouter(
    prefix="/questions",
    tags=["questions"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=QuestionResponse, status_code=status.HTTP_201_CREATED)
async def create_question(question: QuestionCreate):
    """
    Create a new question.
    
    This is a dummy endpoint - replace with your logic later.
    """
    # Dummy response - replace with actual database logic
    dummy_question = Question(
        id=1,
        title=question.title,
        content=question.content,
        difficulty=question.difficulty,
        category=question.category,
        tags=question.tags,
        created_at=datetime.now()
    )
    
    return QuestionResponse(
        message="Question created successfully",
        question=dummy_question
    )

@router.get("/", response_model=List[Question])
async def get_questions():
    """
    Get all questions.
    
    This is a dummy endpoint - replace with your logic later.
    """
    # Dummy response - replace with actual database logic
    return []

@router.get("/{question_id}", response_model=Question)
async def get_question(question_id: int):
    """
    Get a specific question by ID.
    
    This is a dummy endpoint - replace with your logic later.
    """
    # Dummy response - replace with actual database logic
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Question not found"
    ) 
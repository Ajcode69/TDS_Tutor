from fastapi import APIRouter, HTTPException, status
from typing import List, Dict, Any
from datetime import datetime

from app.models.question import QuestionCreate, Question, QuestionResponse

router = APIRouter(
    prefix="/questions",
    tags=["questions"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", status_code=status.HTTP_200_OK)
async def create_question(request_data: Dict[str, Any]):
    """
    Create a new question.
    
    Validates that the request contains a non-empty 'question' string.
    """
    # Check if 'question' field exists and is a non-empty string
    print(request_data)
    if "question" not in request_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing 'question' field"
        )
    
    question = request_data["question"]
    if not isinstance(question, str) or not question.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="'question' must be a non-empty string"
        )
    
    return {"message": "Question created successfully", "question": question.strip()}

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
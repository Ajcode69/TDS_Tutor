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
    
    return {
  "answer": "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question.",
  "links": [
    {
      "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
      "text": "Use the model that’s mentioned in the question."
    },
    {
      "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
      "text": "My understanding is that you just have to use a tokenizer, similar to what Prof. Anand used, to get the number of tokens and multiply that by the given rate."
    }
  ]
}

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
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class QuestionBase(BaseModel):
    title: str
    content: str
    difficulty: Optional[str] = "medium"
    category: Optional[str] = None
    tags: Optional[List[str]] = []

class QuestionCreate(QuestionBase):
    pass

class QuestionUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    difficulty: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = None

class Question(QuestionBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class QuestionResponse(BaseModel):
    message: str
    question: Optional[Question] = None 
from enum import Enum
from typing import Dict
from pydantic import BaseModel, Field

class Confidence(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Topic(BaseModel):
    mastery: float = Field(..., ge=0.0, le=1.0)
    confidence: Confidence

Subjects = Dict[str, Dict[str, Topic]]  # subject -> topic -> Topic

class StudentProfile(BaseModel):
    student_id: str
    grade: int = Field(..., ge=1)
    subjects: Subjects
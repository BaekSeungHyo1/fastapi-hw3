from pydantic import BaseModel
from typing import List

class Course(BaseModel):
    course_code: str
    course_name: str
    credits: int
    grade: str 

class StudentRequest(BaseModel):
    student_id: str
    name: str
    courses: List[Course]

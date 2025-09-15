import json
from typing import Annotated
from pydantic import BaseModel,  Field,validator
import uuid
from datetime import date, datetime, timedelta

class Student(BaseModel):
    id: uuid.UUID
    name: str
    date_of_birth: date
    GPA: Annotated[float, Field(ge=0, le=4)]
    course: str | None = None
    department: str
    fees_paid: bool
    
    @validator("date_of_birth")
    def ensure_16_or_over(cls, v):
        sixteen_years_ago = datetime.now() - timedelta(days=365*16)
        if v > sixteen_years_ago.date():
            raise ValueError("Student must be 16 or over")
        return v

def main():
    with open("students_v1.json") as f:
        data = json.load(f)
        data.append({"id": "d15782d9-3d8f-4624-a88b-c8e836569df8", "name": "Eric Travis", "date_of_birth": "2010-05-25", "GPA": "4.0", "course": "Computer Science", "department": "Science and Engineering", "fees_paid": False})
    for student in data:
        print(Student(**student))
    
if __name__ == "__main__":
    main()

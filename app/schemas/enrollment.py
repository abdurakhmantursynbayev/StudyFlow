from pydantic import BaseModel, ConfigDict
from app.schemas.user import StudentShort
from app.schemas.course import CourseShort
from datetime import date


class EnrollmentCreate(BaseModel):
    model_config = ConfigDict(
        extra="forbid"
    )

    course_id: int

class EnrollmentRead(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    student: StudentShort
    course: CourseShort
    created_at: date

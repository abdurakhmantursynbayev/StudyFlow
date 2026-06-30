from pydantic import BaseModel, ConfigDict
from datetime import date
from app.schemas.user import TeacherShort

class CourseCreate(BaseModel):
    model_config = ConfigDict(
        extra="forbid"
    )

    title: str
    description: str
    

class CourseRead(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    title: str
    description: str
    created_at: date
    teacher: TeacherShort


class CourseUpdate(BaseModel):
    model_config = ConfigDict(
        extra="forbid"
    )

    title: str | None = None
    description: str | None = None


class CourseShort(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    title: str
    
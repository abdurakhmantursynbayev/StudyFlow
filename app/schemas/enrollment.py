from pydantic import BaseModel, ConfigDict


class EnrollmentCreate(BaseModel):
    model_config = ConfigDict(
        extra="forbid"
    )

    course_id: int
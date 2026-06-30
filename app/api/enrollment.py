from fastapi import APIRouter, Depends, HTTPException, status
from app.dependencies import get_db
from sqlalchemy.orm import Session
from app.crud.enrollment import enroll_student
from typing import Annotated
from app.schemas.enrollment import EnrollmentCreate, EnrollmentRead

router = APIRouter(
    tags=["ENROLLMENT"]
)

@router.post("/me/courses/", response_model=EnrollmentRead, status_code=status.HTTP_201_CREATED)
def enroll_student_(student_id: int, enrollment_data: EnrollmentCreate, db: Annotated[Session, Depends(get_db)]):
    new_enrollment = enroll_student(db, enrollment_data, student_id)
    if new_enrollment is None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Course not found or enrollment already exists")
    return new_enrollment
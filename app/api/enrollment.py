from fastapi import APIRouter, Depends, HTTPException, status
from app.dependencies import get_db
from sqlalchemy.orm import Session
from app.crud.enrollment import enroll_student, get_student_courses, delete_enrollment, get_course_students
from typing import Annotated
from app.schemas.enrollment import EnrollmentCreate, EnrollmentRead
from app.schemas.course import CourseRead
from app.schemas.user import StudentShort

router = APIRouter(
    tags=["ENROLLMENT"]
)

@router.post("/me/courses/", response_model=EnrollmentRead, status_code=status.HTTP_201_CREATED)
def create_enrollment(student_id: int, enrollment_data: EnrollmentCreate, db: Annotated[Session, Depends(get_db)]):
    new_enrollment = enroll_student(db, enrollment_data, student_id)
    if new_enrollment is None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Course not found or enrollment already exists")
    return new_enrollment

@router.get("/me/courses", response_model=list[CourseRead])
def get_student_courses_(student_id: int, db: Annotated[Session, Depends(get_db)]):
    courses = get_student_courses(db, student_id)
    return courses

@router.delete("/me/courses/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_enrollment_(course_id: int, student_id: int, db: Annotated[Session, Depends(get_db)]):
    enrollment = delete_enrollment(db, student_id, course_id)
    if enrollment is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return

@router.get("/courses/{course_id}/students", response_model=list[StudentShort])
def get_course_students_(course_id: int, db: Annotated[Session, Depends(get_db)]):
    students = get_course_students(db, course_id)
    if students is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return students


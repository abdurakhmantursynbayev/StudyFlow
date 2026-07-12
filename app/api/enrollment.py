from fastapi import APIRouter, Depends, HTTPException, status
from app.dependencies import get_db
from sqlalchemy.orm import Session
from app.crud.enrollment import enroll_student, get_student_courses, delete_enrollment, get_course_students, get_enrollment
from typing import Annotated
from app.schemas.enrollment import EnrollmentCreate, EnrollmentRead
from app.schemas.course import CourseRead
from app.schemas.user import StudentShort
from app.models.user import User
from app.dependencies import get_current_user
from app.crud.course import get_course_by_id
from app.enums.role import Role
 
router = APIRouter(
    tags=["ENROLLMENT"]
)

#==========
@router.post(
    "/me/courses/", 
    response_model=EnrollmentRead, 
    status_code=status.HTTP_201_CREATED
)
def create_enrollment(
        enrollment_data: EnrollmentCreate,
        current_user: Annotated[User, Depends(get_current_user)],
        db: Annotated[Session, Depends(get_db)]
    ):
    if current_user.role != Role.STUDENT:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only students can enroll in courses"
        )
    if get_course_by_id(db, enrollment_data.course_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    enrollment = get_enrollment(db, current_user.id, enrollment_data.course_id)
    if enrollment is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Enrollment already exists"
        )
    new_enrollment = enroll_student(db, enrollment_data, current_user.id)
    return new_enrollment

#==========
@router.get(
    "/me/courses", 
    response_model=list[CourseRead]
)
def get_student_courses_(
        current_user: Annotated[User, Depends(get_current_user)], 
        db: Annotated[Session, Depends(get_db)]
    ):
    courses = get_student_courses(db, current_user.id)
    return courses

#==========
@router.delete(
    "/me/courses/{course_id}", 
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_enrollment_(
        course_id: int, 
        current_user: Annotated[User, Depends(get_current_user)], 
        db: Annotated[Session, Depends(get_db)]
    ):
    enrollment = get_enrollment(db, current_user.id, course_id)
    if enrollment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Enrollment not found"
        )
    delete_enrollment(db, current_user.id, course_id)

#==========
@router.get(
    "/courses/{course_id}/students", 
    response_model=list[StudentShort]
)
def get_course_students_(
        course_id: int, 
        db: Annotated[Session, Depends(get_db)]
    ):
    course = get_course_by_id(db, course_id)
    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    
    students = get_course_students(db, course_id)
    return students


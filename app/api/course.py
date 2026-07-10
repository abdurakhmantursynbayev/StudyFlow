from fastapi import (
    APIRouter, 
    Depends, 
    HTTPException, 
    status
)
from app.schemas.course import (
    CourseRead, 
    CourseCreate, 
    CourseUpdate
)
from app.dependencies import get_db
from sqlalchemy.orm import Session
from typing import Annotated
from app.crud.course import (
    create_course,
    get_courses, 
    get_course_by_title, 
    get_course_by_id, 
    update_course, 
    delete_course
)
from app.dependencies import get_current_user
from app.models.user import User
from app.enums.role import Role



router = APIRouter(
    prefix="/courses",
    tags=["COURSE"]
)

@router.post("/", response_model=CourseRead, status_code=201)
def create_new_course(
        course_data: CourseCreate,
        current_user: Annotated[User, Depends(get_current_user)],
        db: Annotated[Session, Depends(get_db)]
    ):
    if current_user.role != Role.TEACHER:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Student cannot create course"
        )
    return create_course(db, current_user.id, course_data)


@router.get("/", response_model=list[CourseRead])
def get_all_courses(db: Annotated[Session, Depends(get_db)]):
    return get_courses(db)


@router.get("/title/", response_model=list[CourseRead])
def search_course_by_name(title: str, db: Annotated[Session, Depends(get_db)]):
    return get_course_by_title(db, title)

@router.get("/{course_id}", response_model=CourseRead)
def search_course_by_id(course_id: int, db: Annotated[Session, Depends(get_db)]):
    course =  get_course_by_id(db, course_id)
    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return course

@router.patch("/{course_id}", response_model=CourseRead)
def update_course_(course_id: int, course_new_data: CourseUpdate, db: Annotated[Session, Depends(get_db)]):
    course = update_course(db, course_id, course_new_data)
    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return course
@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course_(teacher_id: int, course_id: int, db: Annotated[Session, Depends(get_db)]):
    ans = delete_course(db, course_id, teacher_id)
    if ans is None: 
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Course not found")
    elif ans:
        return 
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not teacher's course or forbidden to delete")
    
from fastapi import APIRouter
from app.schemas.course import CourseRead, CourseCreate, CourseUpdate
from app.dependencies import get_db
from sqlalchemy.orm import Session
from typing import Annotated
from app.schemas.user import TeacherShort

router = APIRouter(
    prefix="courses",
    tags=["COURSE"]
)

# @router.post("/", response_model=CourseRead)
# def create_new_course(teachershort_data: TeacherShort, course_data: CourseCreate, db: Annotated[Session, get_db]):
    
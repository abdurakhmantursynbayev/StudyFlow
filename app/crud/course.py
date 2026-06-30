from sqlalchemy.orm import Session
from app.schemas.course import CourseCreate, CourseUpdate
from app.models.course import Course
from sqlalchemy import select


def create_course(db: Session, teacher_id: int, new_course_data: CourseCreate) -> Course:
    new_course = Course(
        title = new_course_data.title,
        description = new_course_data.description,
        teacher_id = teacher_id
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    
    return new_course

def get_course_by_id(db: Session, course_id: int) -> Course | None:
    return db.get(Course, course_id)

def get_course_by_title(db: Session, course_title: str) -> list[Course]:
    courses = db.execute(select(Course).where(Course.title == course_title)).scalars().all()
    return courses


def update_course(db: Session, course_id: int, update_data: CourseUpdate) -> Course | None:
    course = db.get(Course, course_id)
    if course is None:
        return None
    
    update_data_dict = update_data.model_dump(exclude_unset=True)

    for key, value in update_data_dict.items():
        setattr(course, key, value)
    
    db.commit()
    db.refresh(course)
    return course

def delete_course(db: Session, course_id: int, teacher_id: int) -> bool | None:
    course = db.get(Course, course_id)
    if course is None:
        return None

    if course.teacher_id == teacher_id:
        db.delete(course)
        db.commit()
        return True
    else:
        return False

def get_courses(db: Session) -> list[Course]:
    courses = db.execute(
        select(Course)
    ).scalars().all()
    return courses

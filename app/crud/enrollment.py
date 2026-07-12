from sqlalchemy.orm import Session
from app.schemas.enrollment import EnrollmentCreate
from app.models.enrollment import Enrollment
from app.models.course import Course
from sqlalchemy import select
from app.models.user import User


def enroll_student(db: Session, enrollment_data: EnrollmentCreate, student_id: int) -> Enrollment | None:
    
    new_enrollment = Enrollment(
        student_id = student_id,
        course_id = enrollment_data.course_id
    )

    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    return new_enrollment


def get_enrollment(db: Session, student_id: int, course_id: int) -> Enrollment | None:
    enrollment = db.get(Enrollment, (student_id, course_id))
    return enrollment


def get_student_courses(db: Session, student_id: int) -> list[Course]:
    stmt = (
        select(Course)
        .join(Enrollment, Enrollment.course_id == Course.id)
        .where(Enrollment.student_id == student_id)
    )

    data = db.execute(stmt).scalars().all()
    return data

def get_course_students(db: Session, course_id: int) -> list[User]:
    course = db.get(Course, course_id)
    if course is None:
        return None

    stmt = (
        select(User)
        .join(Enrollment, Enrollment.student_id == User.id)
        .where(Enrollment.course_id == course_id)
    )
    
    data = db.execute(stmt).scalars().all()
    return data

def delete_enrollment(db: Session, student_id: int, course_id: int) -> Enrollment | None:
    enrollment = db.get(Enrollment, (student_id, course_id))
    db.delete(enrollment)
    db.commit()
    
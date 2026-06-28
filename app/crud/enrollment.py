from sqlalchemy.orm import Session
from app.schemas.enrollment import EnrollmentCreate
from app.models.enrollment import Enrollment
from app.models.course import Course


def enroll_student(db: Session, enrollment_data: EnrollmentCreate, student_id: int) -> Enrollment | None:
    course = db.get(Course, enrollment_data.course_id)
    if course is None:
        return None

    enrollment = db.get(Enrollment, (student_id, enrollment_data.course_id))
    if enrollment is not None:
        return None
    
    new_enrollment = Enrollment(
        student_id = student_id,
        course_id = enrollment_data.course_id
    )

    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    return new_enrollment


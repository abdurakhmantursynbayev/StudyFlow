from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.course import Course


class Enrollment(Base):
    __tablename__ = "enrollments"

    student_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        primary_key=True
    )
    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id"),
        primary_key=True
    )
    created_at: Mapped[date] = mapped_column(
        default=date.today
    )

    #connection with course
    course: Mapped["Course"] = relationship(
        back_populates="enrollments"
    )

    #connection with student(user)
    student: Mapped["User"] = relationship(
        back_populates="enrollments"
    )



    

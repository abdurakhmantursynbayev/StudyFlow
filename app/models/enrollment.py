from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from datetime import date


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
from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey
from datetime import date
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.user import User
    from app.models.enrollment import Enrollment

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text)
    created_at: Mapped[date] = mapped_column(default=date.today)

    teacher_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )
    #connection with teacher(user)
    teacher: Mapped["User"] = relationship(
        back_populates="teacher_courses"
    )

    #connection with enrollment
    enrollments: Mapped[list["Enrollment"]] = relationship(
        back_populates="course",
        cascade="all, delete-orphan"
    )



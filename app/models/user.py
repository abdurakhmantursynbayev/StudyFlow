from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum
from app.enums.role import Role
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.course import Course
    from app.models.enrollment import Enrollment

class User(Base):
    __tablename__= "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    full_name: Mapped[str] = mapped_column(String(100))
    hashed_password: Mapped[str] = mapped_column(String(255))
    role: Mapped[Role] = mapped_column(Enum(Role))
    created_at: Mapped[date] = mapped_column(default=date.today)

    #connection with course 1->n
    teacher_courses: Mapped[list["Course"]] = relationship(
        back_populates="teacher", 
        cascade="all, delete-orphan"
    )
    #connection with enrollment
    enrollments: Mapped[list["Enrollment"]] = relationship(
        back_populates="student",
        cascade="all, delete-orphan"
    )



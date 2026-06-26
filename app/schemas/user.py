from pydantic import BaseModel, ConfigDict
from app.enums.role import Role
from datetime import date


class UserCreate(BaseModel):
    model_config = ConfigDict(
        extra="forbid"
    )

    username: str
    full_name: str
    password: str
    role: Role

class UserRead(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )
    id: int
    username: str
    full_name: str
    role: Role
    created_at: date

class UserUpdate(BaseModel): 
    model_config = ConfigDict(
        extra= "forbid" 
    )

    username: str | None = None
    full_name: str | None = None
    


class TeacherShort(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    full_name: str
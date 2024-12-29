from datetime import datetime
from typing import Any
from pydantic import BaseModel, Field, EmailStr, UUID4
from beanie import PydanticObjectId

from app.api.views.users.models import UserModel


class UserBase(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    superuser: bool = False


class UserOut(UserBase):
    uid: UUID4
    created_at: datetime
    modified_at: datetime


class UserCreate(UserBase):
    uid: UUID4


class UserUpdate(BaseModel):
    uid: UUID4
    name: str | None = Field(None)
    email: EmailStr | None = Field(None)
    superuser: bool | None = Field(None)

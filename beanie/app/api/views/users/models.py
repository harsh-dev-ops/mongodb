from typing import Annotated, List
import uuid
from beanie import BackLink, Document, Indexed, Link
from app.database.models.base import BaseDocument
from pydantic import UUID4, BaseModel, Field

class UserModel(BaseDocument):
    uid: UUID4 = Field(default_factory=uuid.uuid4, unique=True, index=True)
    name: str
    email: str
    superuser: bool = False

    class Settings:
        name = "users"
    
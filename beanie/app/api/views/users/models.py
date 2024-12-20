import uuid
from beanie import Document
from app.database.models.base import Base
from pydantic import UUID4, BaseModel, Field

class UserModel(Base):
    uid: UUID4 = Field(default_factory=uuid.uuid4, unique=True, index=True)
    name: str
    email: str
    superuser: bool = False
    
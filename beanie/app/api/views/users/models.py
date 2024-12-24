from typing import Annotated, List
import uuid
from beanie import BackLink, Document, Indexed
from app.database.models.base import Base
from pydantic import UUID4, BaseModel, Field, Link

class UserModel(Base):
    id: Annotated[int, Indexed(unique=True)]
    uid: UUID4 = Field(default_factory=uuid.uuid4, unique=True, index=True)
    name: str
    email: str
    superuser: bool = False
    # messages: List[BackLink["ChatModel"]]
    # chat_rooms: List[BackLink["ChatRoomModel"]]

    class Settings:
        name = "users"
    
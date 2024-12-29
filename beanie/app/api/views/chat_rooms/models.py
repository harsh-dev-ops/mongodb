from typing import List, Annotated
import uuid
from beanie import Link, Indexed
from app.api.views.chats.models import ChatModel
from app.api.views.users.models import UserModel
from app.database.models.base import Base
from pydantic import UUID4, Field

class ChatRoomModel(Base):
    id: Annotated[int, Indexed()]
    uid: UUID4 = Field(default_factory=uuid.uuid4, unique=True, index=True)
    name: str
    members: List[UUID4] = []

    class Settings:
        name = "chat_rooms"
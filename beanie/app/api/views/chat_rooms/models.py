from typing import List
import uuid
from beanie import Document, Link
from app.api.views.chats.models import ChatModel
from app.api.views.users.models import UserModel
from app.database.models.base import Base
from pydantic import UUID4, BaseModel, Field

class ChatRoomModel(Base):
    uid: UUID4 = Field(default_factory=uuid.uuid4, unique=True, index=True)
    name: str
    messages: List[Link[ChatModel]]
    members: List[Link[UserModel]]

    class Settings:
        name = "chat_rooms"
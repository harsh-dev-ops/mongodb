from typing import List, Annotated
import uuid
from beanie import Link, Indexed
from app.api.views.chats.models import ChatModel
from app.api.views.users.models import UserModel
from app.database.models.base import BaseDocument
from pydantic import UUID4, Field

class ChatRoomModel(BaseDocument):
    uid: UUID4 = Field(default_factory=uuid.uuid4, unique=True, index=True)
    name: str = ""
    members: List[UUID4] = []
    mode: str = "OneToOne"
    
    class Settings:
        name = "chat_rooms"
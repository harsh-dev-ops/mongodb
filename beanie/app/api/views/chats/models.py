from typing import List
import uuid
from beanie import BackLink, Document, Link, PydanticObjectId
from app.api.views.users.models import UserModel
from app.database.models.base import Base
from pydantic import UUID4, BaseModel, Field

class ChatModel(Base):
    text: str
    author_id: int
    chat_room_uid: UUID4

    class Settings:
        name = "messages"

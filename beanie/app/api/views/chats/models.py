from typing import List
import uuid
from beanie import BackLink, Document, Link, PydanticObjectId
from app.database.models.base import BaseDocument
from pydantic import UUID4, Field

class ChatModel(BaseDocument):
    text: str
    author_uid: UUID4
    chat_room_uid: UUID4

    class Settings:
        name = "messages"

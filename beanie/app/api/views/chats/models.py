from typing import List
import uuid
from beanie import BackLink, Document, Link
from app.api.views.users.models import UserModel
from app.database.models.base import Base
from pydantic import UUID4, BaseModel, Field

class ChatModel(Base):
    text: str
    author: Link["UserModel"]
    # read_by: List[Link["ReadRecipient"]]

    class Settings:
        name = "messages"

class ReadRecipient(Base):
    user_id: int
    class Settings:
        name = "read_recipients"
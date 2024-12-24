import uuid
from beanie import BackLink, Document, Link
from app.api.views.users.models import UserModel
from app.database.models.base import Base
from pydantic import UUID4, BaseModel, Field

class ChatModel(Base):
    text: str
    author: Link["UserModel"]

    class Settings:
        name = "messages"
    
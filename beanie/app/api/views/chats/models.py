from typing import List, Optional
from app.api.views.users.crud import UserCrud
from app.api.views.users.models import UserModel
from app.database.models.base import BaseDocument
from pydantic import UUID4, Field

class ChatModel(BaseDocument):
    text: str
    author_uid: UUID4
    chat_room_uid: UUID4
    author: UserModel = Field(default = None, exclude=True)

    class Settings:
        name = "messages"


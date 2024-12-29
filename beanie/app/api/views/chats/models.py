from typing import List, Optional
from app.api.views.users.crud import UserCrud
from app.api.views.users.models import UserModel
from app.database.models.base import BaseDocument
from pydantic import UUID4, Field
from beanie import Link

class ChatModel(BaseDocument):
    text: str
    chat_room_uid: UUID4
    author: Link["UserModel"]

    class Settings:
        name = "messages"


from typing import List, Annotated
import uuid
from beanie import Link
from app.api.views.users.models import UserModel
from app.database.models.base import BaseDocument
from pydantic import UUID4, Field

class ChatRoomModel(BaseDocument):
    uid: UUID4 = Field(default_factory=uuid.uuid4, unique=True, index=True)
    name: str = ""
    members: List[Link[UserModel]]
    mode: str = "OneToOne"
    
    class Settings:
        name = "chat_rooms"

    # {"members.$id": ObjectId("YOUR_USER_OBJECTID_HERE")}
    # { "members.$id": { "$all": [ObjectId1, ObjectId2, ..., ObjectIdN] } }
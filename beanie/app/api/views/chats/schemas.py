from beanie import PydanticObjectId
from pydantic import BaseModel, UUID4, EmailStr


class CreateMessage(BaseModel):
    sent_to: UUID4
    sent_by: UUID4
    text: str


class CreateGroupMessage(BaseModel):
    sent_by: UUID4
    chat_room_uid: UUID4
    text: str


class UpdateMessage(BaseModel):
    objId: PydanticObjectId
    text: str | None = None

class UserOut(BaseModel):
    id: PydanticObjectId
    uid: UUID4
    name: str
    email: EmailStr

class ChatMessageOut(BaseModel):
    id: PydanticObjectId
    text: str
    author: UserOut | None = None

    


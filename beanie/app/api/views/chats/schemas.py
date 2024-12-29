from beanie import PydanticObjectId
from pydantic import BaseModel, UUID4


class CreateMessage(BaseModel):
    sent_to: int
    sent_by: int
    text: str


class CreateGroupMessage(BaseModel):
    sent_by: int
    chat_room_uid: UUID4
    text: str


class UpdateMessage(BaseModel):
    objId: PydanticObjectId
    text: str | None = None

    


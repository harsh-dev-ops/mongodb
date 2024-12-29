from beanie import PydanticObjectId
from pydantic import BaseModel, UUID4


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

    


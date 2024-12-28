from beanie import PydanticObjectId
from pydantic import BaseModel


class CreateMessage(BaseModel):
    sent_to: PydanticObjectId
    sent_by: PydanticObjectId
    text: str


class CreateGroupMessage(BaseModel):
    sent_by: PydanticObjectId
    group_id: PydanticObjectId
    text: str


class UpdateMessage(BaseModel):
    id: PydanticObjectId
    text: str | None = None

class UpdateGroupMessage(BaseModel):
    id: PydanticObjectId
    text: str | None = None

    


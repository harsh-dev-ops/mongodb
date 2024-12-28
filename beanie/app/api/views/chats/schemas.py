from beanie import PydanticObjectId
from pydantic import BaseModel, UUID4


class CreateMessage(BaseModel):
    sent_to: int
    sent_by: int
    text: str


class CreateGroupMessage(BaseModel):
    sent_by: int
    group_id: UUID4
    text: str


class UpdateMessage(BaseModel):
    id: PydanticObjectId
    text: str | None = None

class UpdateGroupMessage(BaseModel):
    id: PydanticObjectId
    text: str | None = None

    


from beanie import PydanticObjectId
from pydantic import BaseModel, UUID4


class ChatRoomOut(BaseModel):
    id: PydanticObjectId
    name: str
    mode: str

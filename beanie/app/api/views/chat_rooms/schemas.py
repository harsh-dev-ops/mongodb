from datetime import datetime
from beanie import Link, PydanticObjectId
from bson import ObjectId
from pydantic import BaseModel, UUID4, EmailStr
from typing import List

class RoomMemberOut(BaseModel):
    id: PydanticObjectId
    uid: UUID4
    name: str
    email: EmailStr

class ChatRoomOut(BaseModel):
    id: PydanticObjectId
    name: str
    mode: str
    created_at: datetime
    modified_at: datetime
    members: List[Link[dict]]


class CreateRoom(BaseModel):
    name: str
    member_ids: List[PydanticObjectId] | None = None
    mode: str = "SubTask"


class UpdateRoom(BaseModel):
    id: str
    name: str
    mode: str = "SubTask"

class AddMembers(BaseModel):
    id: str
    member_ids: List[PydanticObjectId]

class RemoveMembers(BaseModel):
    id: str
    member_ids: List[PydanticObjectId]
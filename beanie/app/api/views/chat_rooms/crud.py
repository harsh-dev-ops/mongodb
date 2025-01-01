
from typing import List
from beanie import PydanticObjectId
from bson import DBRef, ObjectId, Binary
from pydantic import UUID4
from app.api.views.users.models import UserModel
from app.database.crud.base import BaseCrud
from app.api.views.chat_rooms.models import ChatRoomModel


class ChatRoomCrud(BaseCrud):
    def __init__(self, model=ChatRoomModel):
        super().__init__(model=model)

    async def get_user_rooms(self, user_id: ObjectId, mode: str, page: int = 1, page_size: int = 50):
        
        rooms = self.model.find({'members.$id': user_id},{'mode': mode})
        return await self.pagination(rooms, page, page_size)
    
    async def create_room(self, data:dict):

        member_ids = data.pop('member_ids', [])
        members = [DBRef(UserModel.Settings.name, member_id) for member_id in member_ids]
        return await self.create({**data, 'members': members})
    
    async def add_members(self, _id: PydanticObjectId, member_ids: List[PydanticObjectId]):
        room: ChatRoomModel = await self.model.get(_id)
        room.members.extend(
            [DBRef(UserModel.Settings.name, member_id) for member_id in member_ids]
        )
        await room.save()
        return room
    
    async def remove_members(self, _id: PydanticObjectId, member_ids: List[PydanticObjectId]):
        
        room: ChatRoomModel = await self.model.get(_id)
        for member_id in member_ids:
            room.members.remove(
                DBRef(UserModel.Settings.name, member_id)
                )
        await room.save()
        return room
    
    async def get_room_members(self, chat_room_id: str, page: int = 1, page_size: int = 50):
        room: ChatRoomModel = await self.get(chat_room_id)
        return room.members




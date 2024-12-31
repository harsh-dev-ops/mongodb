from bson import ObjectId
from pydantic import UUID4

from beanie import PydanticObjectId
from app.api.views.chat_rooms.crud import ChatRoomCrud
from app.api.views.chat_rooms import schemas


class ChatRoomService:
    def __init__(self, chat_room_crud: ChatRoomCrud):
        self.chat_room_crud = chat_room_crud

    async def get_chat_rooms(self, user_uid: ObjectId, mode: str, page: int = 1, page_size: int = 50):
        return await self.chat_room_crud.get_user_rooms(user_uid, mode, page, page_size)

    async def get_room_members(self, chat_room_id: str, page: int = 1, page_size: int = 50):
        return await self.chat_room_crud.get_room_members(chat_room_id, page, page_size)
    
    async def get_chat_room(self, chat_room_uid: UUID4):
        pass
    
    async def create_chat_room(self, payload: schemas.CreateRoom):
        data = payload.model_dump(exclude_none=True)
        return await self.chat_room_crud.create_room(data)

    async def update_chat_room(self, payload):
        pass

    async def add_room_members(payload):
        pass

    async def remove_room_members(payload):
        pass

    async def delete_chat_room(chat_room_uid: UUID4):
        pass

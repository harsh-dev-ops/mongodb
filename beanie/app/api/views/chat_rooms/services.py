from pydantic import UUID4

from beanie import PydanticObjectId
from app.api.views.chat_rooms.crud import ChatRoomCrud
from app.api.views.chat_rooms import schemas


class ChatRoomService:
    def __init__(self, chat_room_crud: ChatRoomCrud):
        self.chat_room_crud = chat_room_crud

    async def get_chat_rooms(self, user_uid: UUID4, page: int = 1, page_size: int = 50):
        pass

    async def get_room_members(self, chat_room_uid: UUID4, page: int = 1, page_size: int = 50):
        pass
    
    async def get_chat_room(self, chat_room_uid: UUID4):
        pass
    
    async def create_chat_room(self, payload):
        pass

    async def update_chat_room(self, payload):
        pass

    async def add_room_members(payload):
        pass

    async def remove_room_members(payload):
        pass

    async def delete_chat_room(chat_room_uid: UUID4):
        pass

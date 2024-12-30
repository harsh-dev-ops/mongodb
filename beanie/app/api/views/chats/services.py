import uuid

from beanie import PydanticObjectId
from app.api.views.chats.crud import ChatCrud
from app.api.views.chats import schemas


class ChatService:
    def __init__(self, chat_crud: ChatCrud):
        self.chat_crud = chat_crud

    async def get_chats(self, chat_room_uid: uuid.UUID, page: int = 1, page_size: int = 10):
        return await self.chat_crud.get_group_messages(chat_room_uid, page, page_size)

    async def get_chat(self, objId: PydanticObjectId):
        chat = await self.chat_crud.get(objId)
        return chat

    async def create_message(self, payload: schemas.CreateMessage):
        return await self.chat_crud.create_1to1_message(payload.model_dump())

    async def create_group_message(self, payload: schemas.CreateGroupMessage):
        return await self.chat_crud.create_group_message(payload.model_dump())

    async def update_message(self, payload: schemas.UpdateMessage):
        return await self.chat_crud.update(
            payload.objId, payload.model_dump(exclude=['objId']))

    async def delete_message(self, objId: PydanticObjectId):
        return await self.chat_crud.delete(objId)
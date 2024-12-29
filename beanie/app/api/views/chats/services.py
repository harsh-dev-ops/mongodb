import uuid

from beanie import PydanticObjectId
from app.api.views.chats.crud import ChatCrud
from app.api.views.chats import schemas


class ChatService:
    def __init__(self, chat_crud: ChatCrud):
        self.chat_crud = chat_crud

    def get_chats(self, chat_room_uid: uuid.UUID):
        pass

    async def get_chat(self, objId: PydanticObjectId):
        chat = await self.chat_crud.get(objId)
        author = await self.chat_crud.get_author(chat.author_uid)
        chat.author = author
        return chat


    async def create_message(self, payload: schemas.CreateMessage):
        return await self.chat_crud.create_message(payload.model_dump())

    def create_group_message(self, payload: schemas.CreateGroupMessage):
        pass

    def update_message(self, payload: schemas.UpdateMessage):
        pass

    def delete_message(self, objId: PydanticObjectId):
        pass
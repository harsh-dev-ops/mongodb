import uuid

from beanie import PydanticObjectId
from app.api.views.chats.crud import ChatCrud
from app.api.views.chats import schemas


class ChatService:
    def __init__(self, chat_crud: ChatCrud):
        self.chat_crud = chat_crud

    def get_chats(self, chat_room_uid: uuid.UUID):
        pass

    def get_chat(self, objId: PydanticObjectId):
        pass

    def create_chat(self, payload: schemas.CreateMessage):
        pass

    def create_group_message(self, payload: schemas.CreateGroupMessage):
        pass

    def update_message(self, payload: schemas.UpdateMessage):
        pass

    def delete_message(self, objId: PydanticObjectId):
        pass
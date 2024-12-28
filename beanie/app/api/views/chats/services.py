import uuid
from app.api.views.chats.crud import ChatCrud
from app.api.views.chats import schemas


class ChatService:
    def __init__(self, chat_crud: ChatCrud):
        self.chat_crud = chat_crud

    def get_chats(self, group_uid: uuid.UUID):
        pass

    def get_chat(self, _id: str):
        pass

    def create_chat(self, payload: schemas.CreateMessage):
        pass

    def create_group_message(self, payload: schemas.CreateGroupMessage):
        pass

    def update_message(self, payload: schemas.UpdateMessage):
        pass

    def update_group_message(self, payload: schemas.UpdateGroupMessage):
        pass

    def delete_message(self, _id: str):
        pass
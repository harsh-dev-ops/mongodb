from app.database.crud.base import BaseCrud
from app.api.views.chats.models import ChatModel


class ChatCrud(BaseCrud):
    def __init__(self, model=ChatModel):
        super().__init__(model=model)
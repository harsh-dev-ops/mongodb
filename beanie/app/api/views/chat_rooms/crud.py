
from pydantic import UUID4
from app.api.views.users.crud import UserCrud
from app.database.crud.base import BaseCrud
from app.api.views.chat_rooms.models import ChatRoomModel


class ChatRoomCrud(BaseCrud):
    def __init__(self, model=ChatRoomModel):
        super().__init__(model=model)
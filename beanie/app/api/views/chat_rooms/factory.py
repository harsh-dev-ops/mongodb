from app.api.views.chat_rooms.crud import ChatRoomCrud
from app.api.views.chat_rooms.services import ChatRoomService

class ChatRoomServiceFactory:
    def chat_room_service(self):
        return ChatRoomService(ChatRoomCrud())
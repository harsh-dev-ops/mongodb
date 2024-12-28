from app.api.views.chats.crud import ChatCrud
from app.api.views.chats.services import ChatService

class ChatServiceFactory:
    def chat_service(self):
        return ChatService(ChatCrud())
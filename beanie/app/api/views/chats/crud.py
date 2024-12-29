from app.database.crud.base import BaseCrud
from app.api.views.chats.models import ChatModel
from app.api.views.chat_rooms.models import ChatRoomModel


class ChatCrud(BaseCrud):
    def __init__(self, model=ChatModel):
        super().__init__(model=model)

    async def create_message(self, data: dict):

        sent_to, sent_by = data['sent_to'], data['sent_by']

        chat_room = await ChatRoomModel.find({
            "members": {"$all": [sent_to, sent_by]}
            }).first_or_none()
        
        if not chat_room:
            chat_room = ChatRoomModel(members=[sent_to, sent_by])
            await chat_room.insert()

        chat = await self.create({
            'author_uid': sent_by, 
            'text': data['text'], 
            'chat_room_uid': chat_room.uid
        })

        return chat








from beanie import PydanticObjectId
from bson import ObjectId
from pydantic import UUID4
from app.api.views.users.crud import UserCrud
from app.database.crud.base import BaseCrud
from app.api.views.chats.models import ChatModel
from app.api.views.chat_rooms.models import ChatRoomModel


class ChatCrud(BaseCrud):
    def __init__(self, model: ChatModel=ChatModel):
        super().__init__(model=model)

    async def get_author(self, author_uid: UUID4):
        user_crud = UserCrud()
        return await user_crud.get_by_uid(author_uid)
        
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

        author = await self.get_author(chat.author_uid)
        chat.author = author
        return chat








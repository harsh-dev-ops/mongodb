from beanie import PydanticObjectId
from bson import ObjectId
from pydantic import UUID4
from app.api.views.users.crud import UserCrud
from app.database.crud.base import BaseCrud
from app.api.views.chats.models import ChatModel
from app.api.views.chat_rooms.models import ChatRoomModel


class ChatCrud(BaseCrud):
    def __init__(self, model=ChatModel):
        super().__init__(model=model)
        
    async def create_1to1_message(self, data: dict):

        sent_to, sent_by = data['sent_to'], data['sent_by']
        chat_room = await ChatRoomModel.find({"members": {
            "$all": [sent_to, sent_by]
            }}).first_or_none()
        
        if not chat_room:
            chat_room = ChatRoomModel(members=[sent_to, sent_by])
            await chat_room.insert()

        return await self.create_message(
            sent_by,{'text': data['text'],'chat_room_uid': chat_room.uid})
        
    async def create_message(self, author_uid: UUID4, data: dict):
        user_crud = UserCrud()
        author = await user_crud.get_by_uid(author_uid)
        return await self.create({**data,'author': author})
    
    async def create_group_message(self, data: dict):
        sent_by = data.pop('sent_by')
        chat_room = await ChatRoomModel.find({"members": sent_by}).first_or_none()
        await self.missing_obj(chat_room)
        return await self.create_message(sent_by, data)

    async def get_group_messages(self, chat_room_uid: UUID4, 
                                 page: int = 1, page_size: int = 10):
        messages = self.model.find(
            self.model.chat_room_uid == chat_room_uid, fetch_links=True)
        return await self.pagination(messages, page, page_size)
from beanie import PydanticObjectId
from fastapi import APIRouter

import uuid
from app.api.views.chats.factory import ChatServiceFactory
from app.api.views.chats.schemas import CreateMessage, CreateGroupMessage, UpdateMessage


router = APIRouter()

@router.get('/{chat_room_uid}')
async def get_chats(chat_room_uid: uuid.UUID):
    factory = ChatServiceFactory()
    service = factory.chat_service()
    return await service.get_chats(chat_room_uid)

@router.get('/{objId}')
async def get_chat(objId: PydanticObjectId):
    factory = ChatServiceFactory()
    service = factory.chat_service()
    return await service.get_chat(objId)

@router.post('')
async def create_message(payload: CreateMessage):
    factory = ChatServiceFactory()
    service = factory.chat_service()
    return await service.create_message(payload)


@router.patch('')
async def update_message(payload: UpdateMessage):
    factory = ChatServiceFactory()
    service = factory.chat_service()
    return await service.update_message(payload)


@router.post('/group-message')
async def create_group_message(payload: CreateGroupMessage):
    factory = ChatServiceFactory()
    service = factory.chat_service()
    return await service.create_group_message(payload)


@router.delete('/{objId}')
async def delete_message(objId: PydanticObjectId):
    factory = ChatServiceFactory()
    service = factory.chat_service()
    return await service.delete_message(objId)
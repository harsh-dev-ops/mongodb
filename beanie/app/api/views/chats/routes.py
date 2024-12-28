from beanie import PydanticObjectId
from fastapi import APIRouter, status

import uuid
from app.api.views.chats.factory import ChatServiceFactory
from app.api.views.chats.schemas import CreateMessage, CreateGroupMessage, UpdateGroupMessage, UpdateMessage


router = APIRouter()

@router.get('/{group_uid}')
async def get_chats(group_uid: uuid.UUID):
    factory = ChatServiceFactory()
    service = factory.chat_service()
    return await service.get_chats(group_uid)

@router.get('/{_id}')
async def get_chat(_id: PydanticObjectId):
    factory = ChatServiceFactory()
    service = factory.chat_service()
    return await service.get_chat(_id)

@router.post('/message')
async def create_chat(payload: CreateMessage):
    factory = ChatServiceFactory()
    service = factory.chat_service()
    return await service.create_chat(payload)


@router.post('/group-message')
async def create_group_message(payload: CreateGroupMessage):
    factory = ChatServiceFactory()
    service = factory.chat_service()
    return await service.create_group_message(payload)


@router.patch('/message')
async def update_message(payload: UpdateMessage):
    factory = ChatServiceFactory()
    service = factory.chat_service()
    return await service.update_message(payload)


@router.patch('/group-message')
async def update_group_message(payload: UpdateGroupMessage):
    factory = ChatServiceFactory()
    service = factory.chat_service()
    return await service.update_group_message(payload)


@router.delete('/{_id}')
async def delete_message(_id: PydanticObjectId):
    factory = ChatServiceFactory()
    service = factory.chat_service()
    return await service.delete_message(_id)
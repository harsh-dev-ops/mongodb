from fastapi import APIRouter, status
import uuid
from pydantic import UUID4

from app.api.views.chat_rooms.factory import ChatRoomServiceFactory


router = APIRouter()


@router.get('/{user_uid}')
async def get_chat_rooms(user_uid: UUID4, page: int = 1, page_size: int = 50):
    factory = ChatRoomServiceFactory()
    service = factory.chat_room_service()
    return await service.get_chat_rooms(user_uid, page, page_size)

@router.get('/members')
async def get_room_members(chat_room_uid: UUID4, page: int = 1, page_size: int = 50):
    factory = ChatRoomServiceFactory()
    service = factory.chat_room_service()
    return await service.get_room_members(chat_room_uid, page, page_size)


@router.get('')
async def get_chat_room(chat_room_uid: UUID4):
    factory = ChatRoomServiceFactory()
    service = factory.chat_room_service()
    return await service.get_chat_room(chat_room_uid)


@router.post('')
async def create_chat_room(payload):
    factory = ChatRoomServiceFactory()
    service = factory.chat_room_service()
    return await service.create_chat_room(payload)

@router.patch('')
async def update_chat_room(payload):
    factory = ChatRoomServiceFactory()
    service = factory.chat_room_service()
    return await service.update_chat_room(payload)

@router.post('/add-members')
async def add_room_members(payload):
    factory = ChatRoomServiceFactory()
    service = factory.chat_room_service()
    return await service.add_room_members(payload)


@router.post('/remove-members')
async def remove_room_members(payload):
    factory = ChatRoomServiceFactory()
    service = factory.chat_room_service()
    return await service.remove_room_members(payload)


@router.delete('')
async def delete_chat_room(chat_room_uid: UUID4):
    factory = ChatRoomServiceFactory()
    service = factory.chat_room_service()
    return await service.delete_chat_room(chat_room_uid)

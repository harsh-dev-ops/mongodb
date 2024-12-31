from beanie import PydanticObjectId
from bson import ObjectId
from fastapi import APIRouter, status
import uuid
from typing import List
from pydantic import UUID4

from app.api.views.chat_rooms.factory import ChatRoomServiceFactory
from app.api.views.chat_rooms.schemas import ChatRoomOut, CreateRoom, RoomMemberOut


router = APIRouter()


@router.get('/{user_uid}', response_model=List[ChatRoomOut], status_code=status.HTTP_200_OK)
async def get_chat_rooms(user_uid: PydanticObjectId, mode="OneToOne", page: int = 1, page_size: int = 50):
    factory = ChatRoomServiceFactory()
    service = factory.chat_room_service()
    return await service.get_chat_rooms(user_uid, mode, page, page_size)

@router.get('/members/{chat_room_id}', response_model=List[RoomMemberOut])
async def get_room_members(chat_room_id: str, page: int = 1, page_size: int = 50):
    factory = ChatRoomServiceFactory()
    service = factory.chat_room_service()
    return await service.get_room_members(chat_room_id, page, page_size)


@router.get('')
async def get_chat_room(chat_room_uid: UUID4):
    factory = ChatRoomServiceFactory()
    service = factory.chat_room_service()
    return await service.get_chat_room(chat_room_uid)


@router.post('', response_model=ChatRoomOut)
async def create_chat_room(payload: CreateRoom):
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

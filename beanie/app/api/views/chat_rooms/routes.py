from beanie import PydanticObjectId
from fastapi import APIRouter, status

import uuid
from pydantic import UUID4


router = APIRouter()


@router.get('/{user_id}')
async def get_chat_rooms(user_id: int):
    pass

@router.get('/members')
async def get_room_members(chat_room_uid: uuid.UUID):
    pass


@router.get('/{chat_room_uid}')
async def get_chat_room(chat_room_uid: UUID4):
    pass


@router.post('')
async def create_chat_room(payload):
    pass


@router.patch('')
async def update_chat_room(payload):
    pass


@router.post('/add-members')
async def add_room_members(payload):
    pass


@router.post('/remove-members')
async def remove_room_members(payload):
    pass


@router.delete('/{chat_room_uid}')
async def delete_chat_room(chat_room_uid: uuid.UUID):
    pass
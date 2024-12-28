from beanie import PydanticObjectId
from fastapi import APIRouter, status

from app.api.views.chats.factory import *
from app.api.views.chats.schemas import CreateMessage, CreateGroupMessage, UpdateGroupMessage, UpdateMessage
from app.api.views.chats.services import *


router = APIRouter()

@router.get('/{group_uid}')
async def get_chats(group_uid: uuid.UUID):
    pass

@router.get('/{_id}')
async def get_chat(_id: PydanticObjectId):
    pass

@router.post('/message')
async def create_chat(payload: CreateMessage):
    pass


@router.post('/group-message')
async def create_group_message(payload: CreateGroupMessage):
    pass


@router.patch('/message')
async def update_message(payload: UpdateMessage):
    pass


@router.patch('/group-message')
async def update_group_message(payload: UpdateGroupMessage):
    pass


@router.delete('/{_id}')
async def delete_message(_id: PydanticObjectId):
    pass
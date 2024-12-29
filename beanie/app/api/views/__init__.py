from fastapi import APIRouter

from app.api.views.users.routes import router as user_router
from app.api.views.chats.routes import router as chat_router
from app.api.views.chat_rooms.routes import router as chat_room_router

api_router = APIRouter()

api_router.include_router(
    user_router,
    prefix='/users',
    tags=['Users']
)

api_router.include_router(
    chat_router,
    prefix='/chats',
    tags=['Chats']
)

api_router.include_router(
    chat_room_router,
    prefix='/chat-rooms',
    tags=['Chat Rooms']
)
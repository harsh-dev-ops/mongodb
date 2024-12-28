from fastapi import APIRouter

from app.api.views.users.routes import router as user_router
from app.api.views.chats.routes import router as chat_router

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
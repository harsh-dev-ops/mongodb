import uuid
from fastapi import APIRouter, status

from app.api.views.users.factory import UserServiceFactory
from app.api.views.users.schema import UserCreate, UserOut, UserUpdate
from app.api.views.users.services import UserService


router = APIRouter()


@router.get('')
async def get_all_users():
    factory = UserServiceFactory()
    service = factory.user_service()
    return await service.get_users()


@router.get(
    '/{uid}',
    summary="Get user by id",
    response_model=UserOut
)
async def get_user(uid: uuid.UUID):
    factory = UserServiceFactory()
    service = factory.user_service()
    return await service.get_user(uid)


@router.post(
    '',
    summary="Create user",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(payload: UserCreate):
    factory = UserServiceFactory()
    service = factory.user_service()
    return await service.create_user(payload)


@router.patch(
    '',
    summary="Update user",
    response_model=UserOut,
    status_code=status.HTTP_200_OK,
)
async def update_user(payload: UserUpdate):
    factory = UserServiceFactory()
    service = factory.user_service()
    return await service.update_user(payload)


@router.delete(
    '/{uid}',
    summary="Delete user",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(uid: uuid.UUID):
    factory = UserServiceFactory()
    service = factory.user_service()
    return await service.delete_user(uid)

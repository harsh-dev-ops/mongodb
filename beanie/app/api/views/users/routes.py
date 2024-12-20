import uuid
from fastapi import APIRouter, status

from app.api.views.users.schema import UserCreate, UserOut, UserUpdate
from app.api.views.users.services import UserService


router = APIRouter()

@router.get('')
async def get_all_users():
    return await UserService().get_users()



@router.get(
    '/{uid}',
    summary="Get user by id",
    response_model=UserOut
)
async def get_user(uid: uuid.UUID):
    return await UserService().get_user(uid)


@router.post(
    '',
    summary="Create user",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(payload: UserCreate):
    return await UserService().create_user(payload)


@router.patch(
    '',
    summary="Update user",
    response_model=UserOut,
    status_code=status.HTTP_200_OK,
)
async def update_user(payload: UserUpdate):
    return await UserService().update_user(payload)


@router.delete(
    '/{uid}',
    summary="Delete user",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(uid: uuid.UUID):
    return await UserService().delete_user(uid)

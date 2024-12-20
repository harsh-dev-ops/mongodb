from fastapi import APIRouter, status

from app.api.views.users.schema import UserCreate, UserOut
from app.api.views.users.services import UserService


router = APIRouter()

@router.get('')
async def get_all_users():
    return await UserService().get_users()



@router.get(
    '/{user_id}',
    summary="Get user by id",
    response_model=UserOut
)
async def get_user(user_id: str):
    return await GetUser.user(user_id)


@router.post(
    '',
    summary="Create user",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(payload: UserCreate):
    return await UserService().create_user(payload)


@router.patch(
    '/{user_id}',
    summary="Update user",
    response_model=UserOut,
    status_code=status.HTTP_200_OK,
)
async def update_user(user_id: str):
    return {}


@router.delete(
    '/{user_id}',
    summary="Delete user",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(user_id: str):
    return None

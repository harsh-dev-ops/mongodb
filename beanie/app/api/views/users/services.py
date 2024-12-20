from app.api.views.users.crud import BaseCrud, UserCrud
from app.api.views.users.schema import UserCreate


class UserService:
    def __init__(self,
                 user_crud = UserCrud()):
        self._user_crud = user_crud

    async def get_users(self):
        return await self._user_crud.get_all()
    

    async def create_user(self, payload: UserCreate):
        return await self._user_crud.create(payload.model_dump())
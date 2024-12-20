import uuid
from app.api.views.users.crud import BaseCrud, UserCrud
from app.api.views.users import schema


class UserService:
    def __init__(self, user_crud: UserCrud):
        self._user_crud = user_crud

    async def get_users(self):
        return await self._user_crud.get_all()
    
    async def get_user(self, uid: uuid.UUID):
        return await self._user_crud.get_by_uid(uid)
    

    async def create_user(self, payload: schema.UserCreate):
        return await self._user_crud.create(payload.model_dump())

    async def update_user(self, payload: schema.UserUpdate):
        user_uuid = payload.uid
        user = await self._user_crud.get_by_uid(user_uuid)
        data = payload.model_dump(exclude=['uid'], exclude_none=True)
        return await self._user_crud.update_obj(user, data)
    
    async def delete_user(self, uid: uuid.UUID):
        user = await self._user_crud.get_by_uid(uid)
        await self._user_crud.delete_obj(user)



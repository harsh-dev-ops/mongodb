
from app.database.crud.base import BaseCrud
from app.api.views.users.models import UserModel


class UserCrud(BaseCrud):
    def __init__(self, model=UserModel):
        super().__init__(model=model)

    async def get_by_id(self, id: int):
        obj = await self.model.find(self.model.id == id).first_or_none()
        await self.missing_obj(obj)
        return obj
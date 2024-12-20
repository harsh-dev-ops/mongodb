
from app.database.crud.base import BaseCrud
from app.api.views.users.models import UserModel


class UserCrud(BaseCrud):
    def __init__(self, model=UserModel):
        super().__init__(model=model)

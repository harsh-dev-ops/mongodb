from app.api.views.users.crud import UserCrud
from app.api.views.users.services import UserService

class UserServiceFactory:
    def user_service(self):
        return UserService(UserCrud())
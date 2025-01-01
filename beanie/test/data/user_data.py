import uuid
from beanie import PydanticObjectId
from faker import Faker
from pydantic import UUID4, BaseModel, EmailStr


class UserSchema(BaseModel):
    id: PydanticObjectId | None = None
    name: str
    email: EmailStr
    uid: str


faker = Faker()


class UserData:
    def __init__(self):
        self.users = []

    @property
    def user_uids(self) -> list:
        return [user.uid for user in self.users]

    def generate(self) -> BaseModel:
        data = {
            "name": faker.name(),
            "email": faker.email(),
            "superuser": False,
            "uid": str(uuid.uuid4())
        }
        user = UserSchema(**data)
        self.users.append(user)
        return user

    def remove(self, user: UserSchema) -> None:
        self.users.remove(user)
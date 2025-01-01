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

    def generate(self) -> UserSchema:
        data = {
            "name": faker.name(),
            "email": faker.email(),
            "superuser": False,
            "uid": str(uuid.uuid4())
        }
        user = UserSchema(**data)
        self.users.append(user)
        return user

    def update(self) -> list:
        data = {
            "name": faker.name(),
            "email": faker.email()
        }
        for key, value in data.items():
            setattr(self.users[0], key, value)
        return self.users[0]

    def remove(self, user: UserSchema) -> None:
        self.users.remove(user)

    def remove_all(self) -> None:
        self.users = []

    @property
    def user_uids(self) -> list:
        return [user.uid for user in self.users]

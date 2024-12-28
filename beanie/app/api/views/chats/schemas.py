from pydantic import BaseModel


class CreateMessage(BaseModel):
    sent_to: int
    sent_by: int
    text: str


class CreateGroupMessage(BaseModel):
    sent_by: int
    group_id: str
    text: str


class UpdateMessage(BaseModel):
    _id: str
    text: str | None = None

class UpdateGroupMessage(BaseModel):
    _id: str
    text: str | None = None

    


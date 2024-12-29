from beanie import Document, before_event, after_event
from pydantic import Field
from datetime import datetime


class BaseDocument(Document):
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(
        default_factory=datetime.now)

    @after_event
    def update_updated_at(self):
        self.upadte_at = datetime.now()
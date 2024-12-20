from beanie import Document
from typing import List
from datetime import datetime

from fastapi import HTTPException
from app.database.models.base import Base


class CrudMixins:
    def __init__(self, model: Document):
        self.model = model

    async def missing_obj(
        self,
        obj: Document
    ) -> None:
        if obj is None:
            raise HTTPException(404, "Object not found")
        return None


class BaseCrud(CrudMixins):
    def __init__(self, model: Document):
        super().__init__(model=model)

    async def get_all(self) -> List[Document]:
        all_obj = await self.model.find_all(
        ).sort("-created_at"
               ).to_list()
        return all_obj

    async def get_by_uid(self, uid: str) -> Document:
        obj = await self.model.find(self.model.uid == uid).first_or_none()
        return obj

    async def create(self, data: dict) -> Document:
        obj = self.model(**data)
        return await obj.insert()

    async def update(self, id: str, data: dict) -> Document:
        obj = await self.model.find_one(self.model.id == id)
        await self.missing_obj(obj)
        if obj:
            obj.update(**data)
            return obj

    async def delete(self, id: str) -> Document:
        obj = await self.model.find_one(self.model.id == id)
        await self.missing_obj(obj)
        if obj:
            return obj.delete()

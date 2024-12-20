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
        await self.missing_obj(obj)
        return obj

    async def create(self, data: dict) -> Document:
        obj = self.model(**data)
        return await obj.insert()

    async def update(self, id: str, data: dict) -> Document:
        obj = await self.model.find_one(self.model.id == id)
        await self.update_obj(obj, data)
    
    async def update_obj(self, obj: Base, data: dict) -> Document:
        await self.missing_obj(obj)
        for key, value in data.items():
            setattr(obj, key, value)
        await obj.save()
        return obj

    async def delete(self, id: str) -> Document:
        obj = await self.model.find_one(self.model.id == id)
        await self.delete_obj(obj)
    
    async def delete_obj(self, obj: Document):
        await self.missing_obj(obj)
        await obj.delete()


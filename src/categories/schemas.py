from typing import List

from src.schemas import BaseSchema


class BaseCategorySchema(BaseSchema):
    title: str
    points: List[str]


class CategoryCreate(BaseCategorySchema):
    pass


class CategoryResponse(BaseCategorySchema):
    id: int

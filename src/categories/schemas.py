from typing import List, Optional

from src.schemas import BaseSchema


class BaseCategorySchema(BaseSchema):
    title: str
    points: List[str]


class CategoryCreate(BaseCategorySchema):
    pass


class CategoryUpdate(BaseSchema):
    title: Optional[str] = None
    points: Optional[List[str]] = None


class CategoryResponse(BaseCategorySchema):
    id: int

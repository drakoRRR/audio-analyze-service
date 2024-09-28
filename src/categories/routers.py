from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.categories.schemas import CategoryCreate, CategoryResponse, CategoryUpdate
from src.categories.services import delete_category, get_all_categories, update_category, create_category
from src.database import get_db


categories_router = APIRouter()


@categories_router.post("/", response_model=CategoryResponse)
async def create_category_route(category: CategoryCreate, db: AsyncSession = Depends(get_db)):
    return await create_category(db, category)


@categories_router.put("/{category_id}", response_model=CategoryResponse)
async def update_category_route(category_id: int, category_data: CategoryUpdate, db: AsyncSession = Depends(get_db)):
    return await update_category(db, category_id, category_data)


@categories_router.delete("/{category_id}", response_model=dict)
async def delete_category_route(category_id: int, db: AsyncSession = Depends(get_db)):
    await delete_category(db, category_id)
    return {"message": "Category deleted successfully"}


@categories_router.get("/", response_model=list[CategoryResponse])
async def get_all_categories_route(db: AsyncSession = Depends(get_db)):
    return await get_all_categories(db)
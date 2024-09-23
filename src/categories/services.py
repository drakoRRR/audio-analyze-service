from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from src.categories.dal import create_category_in_db, get_category_by_id, get_all_categories_from_db, update_category_in_db, \
    delete_category_from_db
from src.categories.schemas import CategoryCreate


async def create_category(db: AsyncSession, category_data: CategoryCreate):
    points = ','.join(category_data.points)
    return await create_category_in_db(db, category_data.title, points)


async def update_category(db: AsyncSession, category_id: int, category_data: CategoryCreate):
    category = await get_category_by_id(db, category_id)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    category.title = category_data.title
    category.points = ','.join(category_data.points)

    for call in category.calls:
        if not any(point in call.transcription for point in category_data.points):
            category.calls.remove(call)

    return await update_category_in_db(db, category)


async def delete_category(db: AsyncSession, category_id: int):
    category = await get_category_by_id(db, category_id)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    for call in category.calls:
        call.categories.remove(category)

    await delete_category_from_db(db, category)


async def get_all_categories(db: AsyncSession):
    return await get_all_categories_from_db(db)

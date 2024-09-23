from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from src.models import Category


async def create_category_in_db(db: AsyncSession, title: str, points: str):
    new_category = Category(title=title, points=points)
    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)
    return new_category


async def get_category_by_id(db: AsyncSession, category_id: int):
    result = await db.execute(select(Category).filter(Category.id == category_id))
    return result.scalars().first()


async def get_all_categories_from_db(db: AsyncSession):
    result = await db.execute(select(Category))
    return result.scalars().all()


async def update_category_in_db(db: AsyncSession, category: Category):
    await db.commit()
    await db.refresh(category)
    return category


async def delete_category_from_db(db: AsyncSession, category: Category):
    await db.delete(category)
    await db.commit()

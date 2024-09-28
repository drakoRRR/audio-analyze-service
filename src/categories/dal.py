from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session, joinedload
from src.models import Category


async def create_category_in_db(db: AsyncSession, title: str, points: str):
    new_category = Category(title=title, points=points)
    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)

    return {
        "id": new_category.id,
        "title": new_category.title,
        "points": new_category.points.split(",")
    }


async def get_category_by_id(db: AsyncSession, category_id: int):
    result = await db.execute(
        select(Category).options(joinedload(Category.calls)).filter(Category.id == category_id)
    )
    return result.scalars().first()


async def get_all_categories_from_db(db: AsyncSession):
    result = await db.execute(select(Category))
    categories = result.scalars().all()

    return [
        {
            "id": category.id,
            "title": category.title,
            "points": category.points.split(",")
        }
        for category in categories
    ]


async def update_category_in_db(db: AsyncSession, category: Category):
    await db.commit()
    await db.refresh(category)
    return {
        "id": category.id,
        "title": category.title,
        "points": category.points.split(",")
    }


async def delete_category_from_db(db: AsyncSession, category: Category):
    await db.delete(category)
    await db.commit()


async def extract_categories_from_transcription(db: AsyncSession, transcription: str):
    transcription = transcription.lower()

    result = await db.execute(select(Category))
    db_categories = result.scalars().all()

    matched_categories = []

    for category in db_categories:
        points = category.points.split(", ")
        for point in points:
            if point.lower() in transcription:
                matched_categories.append({
                    "title": category.title,
                    "points": [point]
                })
                break

    return matched_categories


async def create_or_get_categories(db: AsyncSession, categories_data: list):
    categories = []
    for category_data in categories_data:
        title = category_data['title']

        result = await db.execute(select(Category).filter(Category.title == title))
        category = result.scalars().first()

        if not category:
            category = Category(
                title=category_data['title'],
                points=", ".join(category_data.get('points', []))
            )
            db.add(category)
            await db.commit()
            await db.refresh(category)

        categories.append(category)

    return categories

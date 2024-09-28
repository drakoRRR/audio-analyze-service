from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models import Category


DEFAULT_CATEGORIES = [
    {
        "title": "Visa and Passport Services",
        "points": ["Border crossing", "International documentation"]
    },
    {
        "title": "Diplomatic Inquiries",
        "points": ["Embassy contacts", "Diplomatic privileges"]
    },
    {
        "title": "Travel Advisories",
        "points": ["Travel warnings", "Health advisories"]
    },
    {
        "title": "Consular Assistance",
        "points": ["Emergency assistance", "Lost passports"]
    },
    {
        "title": "Trade and Economic Cooperation",
        "points": ["Trade agreements", "Economic partnerships"]
    }
]


async def create_default_categories(db: AsyncSession):
    for category_data in DEFAULT_CATEGORIES:
        result = await db.execute(select(Category).filter(Category.title == category_data["title"]))
        category = result.scalars().first()

        if not category:
            category = Category(
                title=category_data["title"],
                points=", ".join(category_data["points"])
            )
            db.add(category)

    await db.commit()

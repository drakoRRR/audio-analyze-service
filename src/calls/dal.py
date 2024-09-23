from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models import Call


async def create_call_in_db(db: AsyncSession, audio_url: str):
    new_call = Call(audio_url=audio_url)
    db.add(new_call)
    await db.commit()
    await db.refresh(new_call)
    return new_call


async def get_call_by_id(db: AsyncSession, call_id: int):
    result = await db.execute(select(Call).filter(Call.id == call_id))
    return result.scalars().first()


async def update_call_in_db(db: AsyncSession, call: Call):
    await db.commit()
    await db.refresh(call)
    return call

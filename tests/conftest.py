import asyncio

import pytest

from src.config import DATABASE_TEST_URL
from typing import AsyncGenerator
from httpx import AsyncClient

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import sessionmaker

from src.main import fastapi_app
from src.database import Base, get_db


test_engine = create_async_engine(DATABASE_TEST_URL, future=True)
test_session = sessionmaker(test_engine, expire_on_commit=False, class_=AsyncSession)


async def test_get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for getting async session"""
    session: AsyncSession = test_session()
    try:
        yield session
    finally:
        await session.close()


@pytest.fixture(scope="session")
async def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def client():
    fastapi_app.dependency_overrides[get_db] = test_get_db
    async with AsyncClient(app=fastapi_app, base_url="http://test") as client:
        yield client
    fastapi_app.dependency_overrides.clear()


@pytest.fixture(scope="function")
async def db_async_session():
    async with test_session() as session:
        yield session

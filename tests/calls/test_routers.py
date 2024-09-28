import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Call


async def test_get_call(client: AsyncClient, db_async_session: AsyncSession):
    call = Call(id=1, audio_url="http://test.local/test_audio1.mp3", transcription="test transcription")
    db_async_session.add(call)
    await db_async_session.commit()

    response = await client.get(f"/api/call/{call.id}")

    assert response.status_code == 200

    response_data = response.json()
    assert response_data["id"] == call.id


async def test_get_call_not_found(client: AsyncClient):
    response = await client.get("/api/call/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Call not found"}

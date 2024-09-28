from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.calls.dal import get_call_by_id
from src.calls.schemas import CallResponse, CallCreate
from src.calls.services import process_audio_call
from src.database import get_db


call_router = APIRouter()


@call_router.post("/", response_model=dict)
async def create_call_route(call_data: CallCreate, db: AsyncSession = Depends(get_db)):
    call = await process_audio_call(db, call_data.audio_url)
    return {"id": call.id}


@call_router.get("/{call_id}", response_model=CallResponse)
async def get_call_route(call_id: int, db: AsyncSession = Depends(get_db)):
    call = await get_call_by_id(db, call_id)
    if not call:
        raise HTTPException(status_code=404, detail="Call not found")
    return call

from typing import Optional, List

from pydantic import HttpUrl

from src.schemas import BaseSchema


class CallCreate(BaseSchema):
    audio_url: HttpUrl


class CallResponse(BaseSchema):
    id: int
    name: Optional[str] = None
    location: Optional[str] = None
    emotional_tone: Optional[str] = None
    transcription: Optional[str] = None
    categories: List[str]

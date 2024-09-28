import os

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.concurrency import run_in_threadpool

from src.calls.dal import create_call_in_db, update_call_in_db
from src.categories.dal import extract_categories_from_transcription, create_or_get_categories
from src.ml_scripts.emotion_detection import detect_emotion
from src.ml_scripts.extract_data_from_text import extract_name_and_location
from src.ml_scripts.speech_recognition import transcribe_audio
from src.calls.utils import download_audio_file, delete_file


async def process_audio_call(db: AsyncSession, audio_url: str):
    local_file_path = await download_audio_file(audio_url)

    try:
        transcription = await transcribe_audio(local_file_path)
        name, location = extract_name_and_location(transcription)
        emotional_tone = await run_in_threadpool(detect_emotion, transcription)

        new_call = await create_call_in_db(db, audio_url=str(audio_url))
        new_call.transcription = transcription
        new_call.name = name
        new_call.location = location
        new_call.emotional_tone = emotional_tone

        categories_data = await extract_categories_from_transcription(db, transcription)
        categories = await create_or_get_categories(db, categories_data)
        for category in categories:
            new_call.categories.append(category)

        return await update_call_in_db(db, new_call)
    finally:
        delete_file(local_file_path)

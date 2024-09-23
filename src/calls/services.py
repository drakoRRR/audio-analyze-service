from sqlalchemy.ext.asyncio import AsyncSession

from src.calls.dal import create_call_in_db, update_call_in_db
from src.ml_scripts.emotion_detection import detect_emotion
from src.ml_scripts.extract_data_from_text import extract_name_and_location
from src.ml_scripts.speech_recognition import transcribe_audio


async def process_audio_call(db: AsyncSession, audio_url: str):
    transcription = await transcribe_audio(audio_url)
    name, location = extract_name_and_location(transcription)
    emotional_tone = await detect_emotion(transcription)

    new_call = await create_call_in_db(db, audio_url=audio_url)
    new_call.transcription = transcription
    new_call.name = name
    new_call.location = location
    new_call.emotional_tone = emotional_tone

    return await update_call_in_db(db, new_call)

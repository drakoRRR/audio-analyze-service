import speech_recognition as sr
from fastapi import BackgroundTasks
from fastapi.concurrency import run_in_threadpool


async def transcribe_audio(audio_url: str):
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(audio_url)

    def sync_transcription():
        with audio_file as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio)

    return await run_in_threadpool(sync_transcription)

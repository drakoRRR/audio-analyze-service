import speech_recognition as sr
from fastapi import BackgroundTasks
from fastapi.concurrency import run_in_threadpool


async def transcribe_audio(file_path: str):
    recognizer = sr.Recognizer()

    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)

    return await run_in_threadpool(recognizer.recognize_sphinx, audio)

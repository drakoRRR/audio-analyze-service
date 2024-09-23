from transformers import pipeline
from fastapi.concurrency import run_in_threadpool


async def detect_emotion(text: str):
    classifier = pipeline("sentiment-analysis")
    result = await run_in_threadpool(classifier, text)
    return result[0]['label']

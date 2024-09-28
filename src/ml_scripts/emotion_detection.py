# from transformers import pipeline
# from fastapi.concurrency import run_in_threadpool
#
#
# async def detect_emotion(text: str):
#     classifier = pipeline("sentiment-analysis")
#     result = await run_in_threadpool(classifier, text)
#     return result[0]['label']
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def detect_emotion(text: str):
    analyzer = SentimentIntensityAnalyzer()
    result = analyzer.polarity_scores(text)

    if result['compound'] >= 0.05:
        return "Positive"
    elif result['compound'] <= -0.05:
        if result['neg'] >= 0.6:
            return "Angry"
        else:
            return "Negative"
    else:
        return "Neutral"

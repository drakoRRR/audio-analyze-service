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

from textblob import TextBlob

def example_sentiment(texts):
    return [(t, TextBlob(t).sentiment.polarity) for t in texts]
